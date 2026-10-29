"""Dynasty (1969) playthrough engine.

A game script is exec'd in a fresh namespace after cards.py and this file, so every
name here is a global the script can call directly. See docs/engine-api.md.

Two kinds of number identify people, and mixing them up is the most common mistake:
  * a SEAT is a province, 1-8. Rules attach to seats (Province 2 collects tax).
  * a PLAYER ID is the seat that player drew at setup. Grain and realia attach to
    players, because players move between seats.
pid(seat) gives the player sitting in a seat; sid(player) gives the seat a player is in.
Functions that take deltas or `give()` use player ids; everything else takes seats.
"""
import re as _re, json as _json, os as _os, math as _math

# The cast, keyed by player id: the seat each one draws. Their names are puns on those
# provinces, and in every game each player sits in their own.
NAMES = {1:"Reina Osorio",2:"Clark Grafton",3:"Richard Baron",4:"Noah Tall",
         5:"Silke Weber",6:"Paddy Doyle",7:"Graham Garner",8:"Robert Land"}
SHORT = {1:"Reina",2:"Clark",3:"Rich",4:"Noah",5:"Silke",6:"Paddy",7:"Graham",8:"Rob"}
ROLE  = {1:"Emperor",2:"Official",3:"Gentry",4:"Scholar",5:"Silk Peasant",
         6:"Rice Peasant",7:"Wheat Peasant",8:"Warlord"}
REALIA = {2:"CH",3:"LD",4:"BB",5:"DJ",6:"WB",7:"VA"}
NEVER  = {2:"DJ",3:"WB",4:"VA",5:"CH",6:"BB",7:"LD"}   # the type each province never needs
RNAME = {"CH":"Customs House","LD":"Land Deed Scroll","BB":"Bamboo Brush",
         "DJ":"Dragon Jar","WB":"Wooden Bowl","VA":"Vase"}
CONS = {1:60,2:40,3:40,4:40,5:40,6:40,7:40,8:20}
HARV = {s:{"good":100,"avg":75,"bad":50} for s in range(1,8)}
HARV[8] = {"good":40,"avg":30,"bad":20}

# Personal disasters, in booklet order. ("fixed", n) | ("frac_income", f) |
# ("frac_grain", f) | ("frac_harvest", f) | ("noraid", n)
DISASTERS = {
 1:[("fixed",4),("fixed",10),("fixed",30)],
 2:[("fixed",4),("fixed",10),("frac_income",.5)],
 3:[("fixed",5),("fixed",10),("frac_grain",.5)],
 4:[("fixed",4),("fixed",10),("frac_grain",1/3)],
 5:[("fixed",4),("fixed",10),("frac_harvest",.5)],
 6:[("fixed",4),("fixed",10),("frac_income",.5)],
 7:[("fixed",2),("fixed",5),("frac_income",1/3)],
 8:[("noraid",0),("fixed",5),("frac_grain",.5)],
}

PILE_START = 2500.0   # 40x0.5 + 50x1 + 40x2 + 50x5 + 20x10 + 20x20 + 10x50 + 10x100

def TH(*pairs):
    """Build a multi-voice hover note: TH(("Rob","thought"), ("Reina","reaction"))."""
    return [{"w":w,"t":t} for w,t in pairs]
def _norm(h, default=""):
    if not h: return None
    if isinstance(h, list): return h
    m = _re.match(r'^([A-Z][a-z]+): (.*)$', h, _re.S)
    if m: return [{"w":m.group(1),"t":m.group(2)}]
    return [{"w":default,"t":h}]

# ------------------------------------------------------------------ the map
# The board is ../map.json: 22 rows A-V, 30 columns 1-30, a square named like "H12".
# Grid characters: 1-7 a province, 8 the Warlord's territory, n the strip below the
# Wall, B beyond the Wall, S the sea. Paths (rivers, Wall links, canal sections) are in
# grid units: (0,0) is the top-left corner of A1, one unit per square.
_MAP = _json.load(open(_os.path.join(globals().get("SIM_DIR", "."), "..", "map.json"), encoding="utf-8"))
GRID = _MAP["grid"]
ROWS, COLS = len(GRID), len(GRID[0])
UNDEVELOPED = "8nS"          # where the Warlord's army may start (Section 4), the sea included
# Soldiers may stand on and cross the sea (RULINGS.md, "The sea is open to soldiers").
RIVERS = _MAP["rivers"]      # {"north": path, "south": path}
WALL_LINKS = {p:[l for l in sorted(_MAP["great_wall_links"], key=lambda l:l["link"]) if l["above_province"]==str(p)]
              for p in (1,2,3)}
CANAL_SECTIONS = {p:[s for s in sorted(_MAP["grand_canal_sections"], key=lambda s:s["section"]) if s["province"]==str(p)]
                  for p in (1,4,5,6)}
PALACES = ("Summer Palace","Winter Palace","Marble Pagoda")
CUTOUT = {"irr2":(2,(1,2),"the Province 2 Irrigation System"),
          "res3":(3,(2,3),"the Province 3 Reservoir"),
          "res7":(7,(2,2),"the Province 7 Reservoir")}   # key: (province, size, name)

def rc(name):
    """'H12' -> (row, col), both from 0. Refuses a square that isn't on the board."""
    m = _re.fullmatch(r"([A-Z])(\d{1,2})", name or "")
    assert m, f"not a square: {name!r}"
    r, c = ord(m.group(1))-65, int(m.group(2))-1
    assert 0 <= r < ROWS and 0 <= c < COLS, f"{name} is off the board"
    return r, c
def sqname(r, c): return f"{chr(65+r)}{c+1}"
def region(name):
    r, c = rc(name); return GRID[r][c]
def prov(name):
    """The province a square is in, or None for undeveloped land, beyond the Wall or the sea."""
    g = region(name); return int(g) if g in "1234567" else None
def owner(name):
    """The province a square belongs to: its own, or the one that bought it as new land."""
    return prov(name) or land.get(name)
def dist(a, b):
    """Rounds a soldier needs to walk from a to b, diagonals allowed."""
    (r1,c1),(r2,c2) = rc(a), rc(b); return max(abs(r1-r2), abs(c1-c2))
def _orth(a, b):
    (r1,c1),(r2,c2) = rc(a), rc(b); return abs(r1-r2)+abs(c1-c2) == 1
def squares(p):
    """Every square of province p (or region character p), in reading order."""
    return [sqname(r,c) for r in range(ROWS) for c in range(COLS) if GRID[r][c] == str(p)]

def _centre(name):
    r, c = rc(name); return (c+.5, r+.5)
def _ccw(a, b, c): return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
def _segx(p1, p2, q1, q2):
    return _ccw(q1,q2,p1)*_ccw(q1,q2,p2) < 0 and _ccw(p1,p2,q1)*_ccw(p1,p2,q2) < 0
def _cuts(a, b, path):
    """Does the step from square a to square b (centre to centre) cross this path?"""
    p1, p2 = _centre(a), _centre(b)
    return any(_segx(p1, p2, path[i], path[i+1]) for i in range(len(path)-1))

def tolls(a, b):
    """The transportation fees a Warlord soldier owes for the step a -> b, as
    [(province, what was crossed)]. 5 each, paid to the province (Section 14, Note 16):
    a river pays the province the soldier steps into, nothing if that's undeveloped land;
    a built Wall link, canal section or cut-out pays the province it belongs to.
    An unoccupied province is owed nothing (Note 4)."""
    out = []
    to = owner(b)
    for name, path in RIVERS.items():
        if _cuts(a, b, path) and to in ACTIVE: out.append((to, f"the {name} river"))
    for p, links in WALL_LINKS.items():
        for l in links[:pw["wall"][p]]:
            if _cuts(a, b, [l["from"], l["to"]]) and p in ACTIVE: out.append((p, "the Great Wall"))
    for p, secs in CANAL_SECTIONS.items():
        for s in secs[:pw["canal"][p]]:
            if _cuts(a, b, s["path"]) and p in ACTIVE: out.append((p, "the Grand Canal"))
    for k, (p, _, name) in CUTOUT.items():
        if b in pw_at.get(k, ()) and p in ACTIVE: out.append((p, name))
    return out

# ------------------------------------------------------------------ setup
def setup(active, key, title, subtitle, blurb, short=""):
    """Start a game. active: the seats in play. key: URL fragment (#key).
    title/subtitle/short: the game selector button. blurb: the line under the header.
    Each player sits in their own province: the player id is the seat.
    The table starts empty: the Setup round (R(0, ...)) deals the grain, takes the
    starting stock out of the box and places the Warlord's army."""
    global ACTIVE, PLAYERS, seat, grain, stock, held, bonus, raids, pw, pw_at, board, pile_stock, land, pop_cards
    global pile, ENTRIES, ROUNDS, META, MULT, CUR_Q, CUR_INC, CUR_HARV, CUR_ROUND
    global dis_next, used_cards, pending_bonus, warlord_got, SOLDIERS, ARMY, NORAID
    global _troops_round, _done, _named, hired, LAST_BUILD, CHAOS, CALLED
    ACTIVE = sorted(active)
    PLAYERS = list(ACTIVE)
    seat = {s:s for s in ACTIVE}
    grain = {p:0.0 for p in PLAYERS}
    pile = PILE_START
    stock = {}
    pile_stock = {}        # realia sold back to the Harvest Pile, auctioned at the next auction
    held = {p:{} for p in PLAYERS}
    bonus = {s:0 for s in ACTIVE}
    pending_bonus = {}
    raids = {s:0 for s in range(1,9)}
    pw = {"Summer Palace":0,"Winter Palace":0,"Marble Pagoda":0,
          "wall":{1:0,2:0,3:0},"canal":{1:0,4:0,5:0,6:0},"irr2":0,"res3":0,"res7":0}
    pw_at = {}             # work key -> the squares it stands on
    board = {}             # square -> {"realia", "owner"} and/or {"raid": True}
    land = {}              # new harvest square -> the province that bought it (Section 13)
    pop_cards = {2: 0, 1.5: 0}   # population changes that have taken effect, by kind
    SOLDIERS = {}          # id -> {"side": "W" or "B", "owner", "sq", "home", "moved"}
    ARMY = (4 if len(ACTIVE) >= 8 else 2) if 8 in ACTIVE else 0
    NORAID = {}            # round -> provinces the Warlord may not raid this round
    _troops_round = None
    _done = set(); _named = set()
    hired = {}             # round -> soldiers the Warlord hired (RULINGS.md, reinforcements)
    LAST_BUILD = None      # the round the last public work was built in (one project a round, N13)
    CALLED = None          # a revolt called and not yet settled: play waits (revolt_called)
    CHAOS = False          # set by revolt() (or the script) after a revolt; cleared once acclamation() seats an Emperor
    ENTRIES = []; ROUNDS = []
    MULT = 1; CUR_Q = {}; CUR_INC = {}; CUR_HARV = {}; CUR_ROUND = None
    dis_next = {s:0 for s in ACTIVE}
    used_cards = set()
    warlord_got = {}
    META = dict(key=key, title=title, subtitle=subtitle, blurb=blurb, short=short)

def deal_grain(text, hover=None):
    """Setup: the Harvest Pile deals every player 60 (Section 4)."""
    global pile
    assert CUR_ROUND == 0 and "grain" not in _done
    _done.add("grain")
    pile -= 60*len(PLAYERS)
    act(text, hover, {p:60 for p in PLAYERS}, map_hl=list(ACTIVE))

def take_stock(text, hover=None):
    """Setup: each realia province takes its starting stock out of the box. It waits
    beside the board until it's auctioned (Note 10). At 4-5 players: one of its own and
    two of its NEVER type; at 6, two of its own; at 7 or more, four of its own."""
    assert CUR_ROUND == 0 and "stock" not in _done
    _done.add("stock")
    n = len(ACTIVE)
    for s in ACTIVE:
        if s in REALIA:
            if n <= 5:   stock[s] = {REALIA[s]:1, NEVER[s]:2}
            elif n == 6: stock[s] = {REALIA[s]:2}
            else:        stock[s] = {REALIA[s]:4}
    act(text, hover, map_hl=[s for s in ACTIVE if s in REALIA])

def place_army(at, text, hover=None):
    """Setup: the Warlord stands his soldiers on squares of undeveloped land.
    at: {soldier id: square}; the ids are W1, W2, ... and there must be one per soldier
    (four at eight players, two at five or six)."""
    assert CUR_ROUND == 0 and 8 in ACTIVE and "army" not in _done
    assert sorted(at) == [f"W{i}" for i in range(1, ARMY+1)], f"the Warlord has {ARMY} soldiers: W1..W{ARMY}"
    for i, q in at.items():
        assert region(q) in UNDEVELOPED, f"{i} must start on undeveloped land, not {q}"
        SOLDIERS[i] = dict(side="W", owner=pid(8), sq=q, home=8, moved=None)
    _done.add("army")
    act(text, hover, map_hl=[8])

def need_for(s):
    """The realia types the player in seat s must collect, by player count."""
    n = len(ACTIVE)
    if s not in REALIA: return []
    if n <= 5: return [t for t in ["CH","LD","BB","DJ","WB","VA"] if t not in (REALIA[s], NEVER[s])]
    if n == 6: return [REALIA[o] for o in ACTIVE if o in REALIA and o != s]
    return [t for t in ["CH","LD","BB","DJ","WB","VA"] if t != REALIA[s]]

def owed():
    """[name, how many, cost each] for every public work owed at this table.
    Works in an unoccupied province are not owed (Emperor's booklet)."""
    o = [["Summer Palace",1,20],["Winter Palace",1,20],["Marble Pagoda",1,20]]
    w = sum(4 for s in (1,2,3) if s in ACTIVE); o.append(["Great Wall",w,40])
    c = sum(2 for s in (1,4,5,6) if s in ACTIVE); o.append(["Grand Canal",c,40])
    if 2 in ACTIVE: o.append(["Province 2 Irrigation System",1,30])
    if 3 in ACTIVE: o.append(["Province 3 Reservoir",1,80])
    if 7 in ACTIVE: o.append(["Province 7 Reservoir",1,60])
    return o

def built_count(name):
    if name == "Great Wall": return sum(pw["wall"].values())
    if name == "Grand Canal": return sum(pw["canal"].values())
    return {"Province 2 Irrigation System":pw["irr2"],"Province 3 Reservoir":pw["res3"],
            "Province 7 Reservoir":pw["res7"]}.get(name, pw.get(name, 0))

def all_built():
    return all(built_count(n) >= t for n,t,_ in owed())

def home(t):
    """Where a returned piece goes: its native province, or, if that province is empty,
    the province that started the game holding it (rulebook Note 12)."""
    native = [k for k,v in REALIA.items() if v==t][0]
    if native in ACTIVE: return native
    for s in ACTIVE:
        if s in NEVER and NEVER[s] == t: return s
    return native

def pid(s): return seat[s]
def sid(p):
    for s,q in seat.items():
        if q == p: return s

# ------------------------------------------------------------------ log
def snap():
    return dict(grain={str(p):round(grain[p],2) for p in PLAYERS},
                seat={str(s):seat[s] for s in ACTIVE},
                held={str(p):dict(held[p]) for p in PLAYERS},
                stock={str(s):dict(v) for s,v in stock.items()},
                pile_stock=dict(pile_stock),
                raids={str(k):v for k,v in raids.items()},
                pw={k:(dict((str(a),b) for a,b in v.items()) if isinstance(v,dict) else v) for k,v in pw.items()},
                at={k:list(v) for k,v in pw_at.items()},
                bonus={str(k):v for k,v in bonus.items()},
                board={k:dict(v) for k,v in board.items()},
                land={k:v for k,v in land.items()},
                sol=[[i, s["side"], s["sq"], s["owner"]] for i,s in SOLDIERS.items()],
                pile=round(pile,2), mult=MULT,
                rob={str(k):v for k,v in warlord_got.items()})

# Negative grain ("sell before you sink"): a payment that would take a player below
# zero must first be covered by selling realia back to the Harvest Pile at 2 each
# (sell_back); only then may grain go negative, as a debt to the pile. A player in
# debt is locked out of voluntary spending: bids, purchases, trades, bribes, shares
# of public works, soldiers, seat changes. Grain received pays the debt first, which
# a single signed number does by itself. A debt is also a cause for revolt (Section 16);
# revolts are the script's to write, so the engine only records the debt.

def _apply(d):
    for k,v in (d or {}).items():
        after = round(grain[k]+v, 2)
        assert not (v < 0 and after < 0 and held[k]), \
            f"{SHORT[k]} would go into debt ({after:g}) while holding {held[k]}: sell_back() first"
        grain[k] = after

def _spend(p, amount, what):
    """A voluntary payment: refused in debt, or beyond the grain in hand."""
    assert grain[p] >= 0, f"{SHORT[p]} is in debt ({grain[p]:g}) and can't {what}"
    assert not (CHAOS and p == pid(1)), f"the treasury is sealed under Chaos: {SHORT[p]} can't {what} (RULINGS)"
    assert amount <= grain[p] + 1e-9, f"{SHORT[p]} has {grain[p]:g} and can't {what} for {amount:g}"

def act(text, hover=None, deltas=None, map_hl=None, pile_delta=0, big=False, moves=None, deal=False):
    """A game event: a bold, clickable line in the transcript.
    deltas: {player_id: grain change}. pile_delta: change to the Harvest Pile.
    map_hl: seats to highlight on the board. big: style as a turning point.
    moves: [[from, to, side]] soldier steps to draw as arrows (set by march/troops).
    deal: the payments are voluntary (a trade, a bribe, a gift), so a payer in debt,
    or one paying more than they hold, is refused."""
    global pile
    if deal:
        for k,v in (deltas or {}).items():
            if v < 0: _spend(k, -v, "pay in a deal")
    _apply(deltas); pile = round(pile+pile_delta, 2)
    ENTRIES.append(dict(k="act", t=text, h=_norm(hover), who=None,
        d={str(k):v for k,v in (deltas or {}).items()}, hl=map_hl or [],
        state=snap(), big=big, mv=moves or []))

def say(who, text, hover=None):
    """Table talk: an in-character line. Changes nothing. hover is the thought behind it."""
    ENTRIES.append(dict(k="say", t=text, h=_norm(hover, who), who=who, d={}, hl=[], state=snap(), mv=[]))

# ------------------------------------------------------------------ rounds
def R(n, title, card=None, card_text=None):
    """Start a round. n=0 is the Setup round. card is a key in CARDS (None for rounds 0 and 1)."""
    global MULT, CUR_Q, CUR_ROUND
    _waiting("R")
    if n == 1:
        missing = {"grain","stock"} - _done
        if ARMY: missing |= {"army"} - _done
        assert not missing, f"setup isn't finished: {sorted(missing)}"
    assert CUR_ROUND is None or n == CUR_ROUND+1, f"round {n} follows round {CUR_ROUND}"
    CUR_ROUND = n
    for s,v in pending_bonus.items(): bonus[s] += v
    pending_bonus.clear()
    q = None
    if card:
        assert card not in used_cards, "card drawn twice: "+card
        used_cards.add(card)
        c = CARDS[card]; card_text = c["text"]
        q = c["q"]
        pop = c.get("pop")
        # The cards' own caps (RULINGS.md): a doubling takes effect at most twice and never
        # past 600 million (x6); the increase by half takes effect once. Otherwise the
        # card is only a good harvest.
        if pop == 2 and (pop_cards[2] >= 2 or MULT * 2 > 6): pop = None
        if pop == 1.5 and pop_cards[1.5] >= 1: pop = None
        if pop: MULT = MULT * pop; pop_cards[pop] += 1
    if isinstance(q, str): q = {s:q for s in ACTIVE}
    CUR_Q = q or {}
    ROUNDS.append(dict(n=n, title=title, card=card_text, start=len(ENTRIES), mult=MULT))

def income(s, q=None):
    """Harvest + public-works bonus - consumption x population multiple, for seat s."""
    q = q or CUR_Q[s]
    return HARV[s][q] + bonus[s] - CONS[s]*MULT

def harvest(note=None, hover_extra=None):
    """The Gentry (or appointee) pays each province its income for the year."""
    global pile
    _waiting("harvest")
    d = {}; parts = []
    for s in ACTIVE:
        inc = income(s); d[pid(s)] = inc
        CUR_INC[s] = inc; CUR_HARV[s] = HARV[s][CUR_Q[s]] + bonus[s]
        parts.append(f"{SHORT[pid(s)]} {inc:+g}")
    tot = sum(d.values())
    who = note or ("The Gentry pays out the harvest." if 3 in ACTIVE else "The harvest is paid out.")
    h = [{"w":"","t":"Harvest minus consumption, paid from the Harvest Pile (or paid into it, when it's negative). "+", ".join(parts)+"."}]
    if hover_extra: h = hover_extra + h
    act(who, h, d, map_hl=list(ACTIVE), pile_delta=-tot)

def rents(rate=5, note=None, hover=None):
    """Each occupied peasant province pays the Gentry. Does nothing with no Gentry."""
    _waiting("rents")
    if 3 not in ACTIVE: return
    d = {}; g = pid(3)
    for s in (5,6,7):
        if s in ACTIVE:
            d[pid(s)] = d.get(pid(s),0)-rate; d[g] = d.get(g,0)+rate
    act(note or f"Rents: each peasant pays the Gentry {rate:g}.",
        hover or "The Gentry may raise this at any time, and gets nothing by forgetting to ask.", d, map_hl=[3,5,6,7])

def taxes(rate, skip=(8,), collector=None, hover=None, extra=None):
    """The Emperor's tax at `rate` (0.30 = 30%) on this round's income; negative income
    pays nothing. skip: seats that refuse (the Warlord by default).
    extra: {seat: additional taxable income}. Returns the total collected."""
    _waiting("taxes")
    assert not CHAOS, "no tax under Chaos (Note 17)"
    d = {}; e = pid(1); lines = []
    for s in ACTIVE:
        if s == 1 or s in skip: continue
        inc = CUR_INC[s] + (extra or {}).get(s,0)
        t = pay_down(max(0,inc)*rate)
        if t: d[pid(s)] = d.get(pid(s),0)-t; d[e] = d.get(e,0)+t
        lines.append(f"{SHORT[pid(s)]} {t:g}")
    who = collector or ("The Official collects the tax" if 2 in ACTIVE else "The tax is collected")
    tot = sum(v for k,v in d.items() if k != e)
    act(f"{who} at {int(round(rate*100))}% — {-tot:g} to the crown.",
        hover or ("No tax is owed on a negative income. "+", ".join(lines)+"."), d, map_hl=[1,2])
    return -tot

def salaries(pay=None, text=None, hover=None):
    """The Emperor pays salaries. Default: 5 each to the Official and Scholar if present.
    pay: {seat: amount} for appointees (the peasant game pays its card reader this way)."""
    _waiting("salaries")
    assert not CHAOS, "no salaries under Chaos (Note 17)"
    pay = pay or {s:5 for s in (2,4) if s in ACTIVE}
    if not pay: return
    e = pid(1); d = {e:0}
    for s,a in pay.items(): d[pid(s)] = d.get(pid(s),0)+a; d[e] -= a
    label = text or ("Salaries: " + ", ".join(f"{a:g} to the {ROLE[s]}" for s,a in pay.items()) + ".")
    act(label, hover or "The Emperor owes the Official and the Scholar at least 5 a year.", d,
        map_hl=[1]+list(pay.keys()))

PW_BONUS = {"irr2":(2,10),"res3":(3,20),"res7":(7,20)}
def _work_at(q):
    for k, sqs in pw_at.items():
        if q in sqs: return k
    return None
def _rect(spec):
    """'P14:Q15' -> every square in that rectangle."""
    a, b = spec.split(":")
    (r1,c1),(r2,c2) = rc(a), rc(b)
    return [sqname(r,c) for r in range(min(r1,r2), max(r1,r2)+1) for c in range(min(c1,c2), max(c1,c2)+1)], \
           (abs(r1-r2)+1, abs(c1-c2)+1)

def build(name, cost, split, wall=None, canal=None, key=None, hover=None, text=None, at=None):
    """split: {seat: amount}. wall/canal: {seat: n}. key: 'Summer Palace', 'irr2', ...
    at: where a palace ('G20') or a cut-out ('P14:Q15') goes; the Wall and the Canal
    have printed places on the map, built in link and section order."""
    global LAST_BUILD
    _waiting("build")
    assert not CHAOS, "no public works under Chaos (Note 17)"
    LAST_BUILD = CUR_ROUND
    d = {}
    for s,a in split.items(): d[pid(s)] = d.get(pid(s),0)-a
    assert abs(sum(split.values())-cost) < 1e-6, (name, cost, split)
    for s,a in split.items():
        if a > 0: _spend(pid(s), a, f"pay a share of {name}")
    for s,n in (wall or {}).items():
        assert s in WALL_LINKS and pw["wall"][s]+n <= 4, f"only four Wall links above Province {s}"
        pw["wall"][s] += n
    for s,n in (canal or {}).items():
        assert s in CANAL_SECTIONS and pw["canal"][s]+n <= 2, f"only two canal sections in Province {s}"
        pw["canal"][s] += n; pending_bonus[s] = pending_bonus.get(s,0)+10*n
    if key:
        assert not pw[key], f"{key} is already built"
        if key in PALACES:
            assert at and prov(at) == 1, f"the {key} goes on a square in Province 1, not {at}"
            sqs = [at]
        elif key in CUTOUT:
            p, size, label = CUTOUT[key]
            assert at, f"say where {label} goes: at='P14:Q15'"
            sqs, dims = _rect(at)
            assert sorted(dims) == sorted(size), f"{label} is {size[0]} x {size[1]}, not {dims[0]} x {dims[1]}"
            assert all(prov(q) == p for q in sqs), f"{label} must lie inside Province {p}"
        else: sqs = []
        for q in sqs:
            assert not board.get(q,{}).get("realia"), f"{q} holds realia"
            assert not _work_at(q), f"{q} already holds {_work_at(q)}"
        if sqs: pw_at[key] = sqs
        pw[key] = 1
        if key in PW_BONUS:
            s,b = PW_BONUS[key]; pending_bonus[s] = pending_bonus.get(s,0)+b
    # the cost goes to the Harvest Pile (RULINGS, "Paying for a Public Work pays the Harvest Pile")
    act(text or f"Public works: {name} — {cost:g} paid.",
        hover or ("Cost split: "+", ".join(f"{SHORT[pid(s)]} {a:g}" for s,a in split.items())+"."),
        d, map_hl=list(split.keys()), pile_delta=cost)

LAND_WHERE = {1:"nS", 2:"n", 3:"n", 4:"S", 5:"S", 6:"S8", 7:"8"}   # where each province may develop (its booklet)
def buy_land(s, squares, split, text, hover=None):
    """Province s buys new harvest squares from the Harvest Pile (Section 13), 20 each,
    any number in a round, alongside the round's one public work. Only once the
    population has at least doubled, and the strip below the Wall only once all four
    links above the province stand (Provinces 1, 2 and 3; Province 1 may take the sea
    before that). split: {seat: amount} summing to 20 per square; the Emperor must
    share the cost. Each square sits on the undeveloped land or sea the province's
    booklet names, touching the province or a square it has already bought, and adds
    20 to the province's harvest from the next round. It becomes part of the province:
    the Warlord can raid it."""
    global pile
    _waiting("buy_land")
    assert CUR_ROUND and CUR_ROUND >= 1
    assert not CHAOS, "no new land under Chaos: there's no Emperor to share the cost (RULINGS, readings)"
    assert s in ACTIVE and s in LAND_WHERE, f"Province {s} can't develop new land"
    assert MULT >= 2, f"the population must have doubled before anyone develops (it's x{MULT:g})"
    if s in (2, 3): assert pw["wall"][s] == 4, f"Province {s} needs all four Wall links above it first"
    cost = 20*len(squares)
    assert abs(sum(split.values())-cost) < 1e-6, (cost, split)
    if s != 1: assert split.get(1, 0) > 0, "the cost must be shared with the Emperor"
    mine = set(squares_of(s))
    for q in squares:
        assert region(q) in LAND_WHERE[s], f"Province {s} develops {LAND_WHERE[s]!r} squares, not {q}"
        if s == 1 and region(q) == "n":
            assert pw["wall"][1] == 4, f"the strip below the Wall opens to Province 1 only once its four links stand ({q})"
        assert q not in land, f"{q} has already been developed"
        assert not board.get(q, {}).get("realia"), f"{q} holds the Warlord's {RNAME[board[q]['realia']]}"
        assert any(dist(q, m) == 1 for m in mine), f"{q} doesn't touch Province {s} or its new land"
        mine.add(q)
    for t,a in split.items():
        if a > 0: _spend(pid(t), a, f"pay toward new land in Province {s}")
    for q in squares: land[q] = s
    pending_bonus[s] = pending_bonus.get(s,0) + 20*len(squares)
    act(text, hover or ("Cost split: "+", ".join(f"{SHORT[pid(t)]} {a:g}" for t,a in split.items())+
        f". 20 a square into the Harvest Pile; each yields 20 a round from next year."),
        {pid(t):-a for t,a in split.items()}, map_hl=[s], pile_delta=cost)

def squares_of(s):
    """Province s's own squares and the new land it has bought."""
    return squares(s) + [q for q,o in land.items() if o == s]

def disaster(s, text, hover=None):
    """Play the next personal disaster in seat s's booklet. The Warlord's first two
    stop raids this round (on 5-7, then everywhere); the engine refuses a raid that breaks that."""
    global pile
    i = dis_next[s] % 3; dis_next[s] += 1
    kind, v = DISASTERS[s][i]
    p = pid(s)
    if kind == "fixed": amt = v
    elif kind == "frac_income": amt = pay_down(max(0, CUR_INC[s])*v)
    elif kind == "frac_harvest": amt = pay_down(CUR_HARV[s]*v)
    elif kind == "frac_grain": amt = pay_down(max(0, grain[p])*v)
    else: amt = 0
    if s == 8 and i == 0: NORAID[CUR_ROUND] = {5,6,7}
    if s == 8 and i == 1: NORAID[CUR_ROUND] = set(range(1,8))
    act(f"{SHORT[p]}'s disaster #{i+1}: {text}" + (f" — {amt:g} to the Harvest Pile." if amt else ""),
        hover, {p:-amt} if amt else None, map_hl=[s], pile_delta=amt)
    return kind

# ------------------------------------------------------------------ realia
def _place(code, owner, at):
    """A bought or traded piece goes on a square of its owner's province at once (Note 10)."""
    s = sid(owner)
    ok = region(at) == "8" and at not in land if s == 8 else prov(at) == s
    where = "the desert nobody has bought" if s == 8 else f"Province {s}"
    assert ok, f"{SHORT[owner]}'s {RNAME[code]} must go in {where}, not {at}"
    cell = board.get(at, {})
    assert not cell.get("realia"), f"{at} already holds a {RNAME[cell.get('realia','')] if cell.get('realia') else ''}"
    assert not cell.get("raid"), f"{at} has been raided; realia can't go there"
    assert not _work_at(at), f"{at} is under {_work_at(at)}"
    board[at] = dict(cell, realia=code, owner=owner)

def _lift(code, owner):
    for k, v in board.items():
        if v.get("realia") == code and v.get("owner") == owner:
            v.pop("realia"); v.pop("owner")
            if not v: del board[k]
            return k
    raise AssertionError(f"{SHORT[owner]} has no {RNAME[code]} on the board")

def pay_down(x):
    """A computed payment rounds down to the half million, in the payer's favour
    (rulebook, The Harvest Pile): commissions, tax, and the fractional disasters."""
    return _math.floor(round(x, 6) * 2) / 2

PILE = 0   # lot(PILE, ...): the Harvest Pile auctions realia sold back to it
def lot(sell, typ, ladder, hover=None, at=None):
    """Auction one piece of typ from seat sell's stock, or from the Harvest Pile's
    with sell=PILE. ladder: B(...) bids; the last numeric bid wins. at: the square in
    the winner's province where they place it. A bid must be covered by the bidder's
    grain, and nobody in debt may bid."""
    global pile
    _waiting("lot")
    src = pile_stock if sell == PILE else stock.get(sell,{})
    assert src.get(typ), f"{'The Harvest Pile' if sell == PILE else 'Province %d' % sell} has no {RNAME[typ]} to sell"
    assert at, f"say where the winner puts the {RNAME[typ]}: at='H12'"
    bids = []
    for b,amt,txt,hov in ladder:
        if amt is not None: _spend(pid(b), amt, f"bid {amt:g}")
        bids.append(dict(who=SHORT[pid(b)], t=txt or (spell(amt)+"." if amt is not None else "Out."),
                         h=_norm(hov, SHORT[pid(b)]), amt=amt))
    win = [r for r in ladder if r[1] is not None][-1]
    wb, price = win[0], win[1]
    assert wb != sell and wb != 1, "neither the seller nor the Emperor bids"
    src[typ] -= 1
    if src[typ] <= 0: del src[typ]
    held[pid(wb)][typ] = held[pid(wb)].get(typ,0)+1
    _place(typ, pid(wb), at)
    d = {pid(wb):-price}
    if sell == PILE:
        pile = round(pile + price, 2)
        note = f"{SHORT[pid(wb)]} pays {price:g}, all of it to the Harvest Pile."
    else:
        com = pay_down(price*0.25)
        d[pid(sell)] = d.get(pid(sell),0) + com
        pile = round(pile + price - com, 2)
        note = (f"{SHORT[pid(wb)]} pays {price:g}. {SHORT[pid(sell)]} keeps {com:g} as commission; "
                f"{price - com:g} goes to the Harvest Pile.")
    _apply(d)
    h = _norm(hover) or []
    h = h + [{"w":"","t":note}]
    ENTRIES.append(dict(k="lot", t=f"{RNAME[typ]} — {SHORT[pid(wb)]} takes it for {price:g}.",
        h=h, who=None, bids=bids, d={str(k):v for k,v in d.items()},
        hl=[s for s in (sell, wb) if s], state=snap(), mv=[]))

def sell_back(p, codes, text, hover=None):
    """Player p sells pieces of realia back to the Harvest Pile at 2 each, lifting them
    off the board into the pile's own stock, which it auctions at the next auction
    (lot(PILE, ...)). Before a payment would put p in debt, the script must sell enough
    of p's pieces to cover it, or all of them; p chooses which, and the hover says why."""
    for t in codes:
        assert held[p].get(t), f"{SHORT[p]} holds no {RNAME[t]} to sell back"
        _lift(t, p)
        held[p][t] -= 1
        if not held[p][t]: del held[p][t]
        pile_stock[t] = pile_stock.get(t,0) + 1
    act(text, hover, {p: 2*len(codes)}, map_hl=[sid(p)], pile_delta=-2*len(codes))

def B(seat, amt, text=None, th=None):
    """One bid in a lot ladder. amt=None is a pass. text defaults to the amount in words."""
    return (seat, amt, text, th)

def give(frm, to, typ, at):
    """Move one piece of realia between players (by player id) for a private trade.
    at: the square in the new owner's province. The grain is a separate act()."""
    assert held[frm].get(typ), f"{SHORT[frm]} holds no {RNAME[typ]}"
    _lift(typ, frm)
    held[frm][typ] -= 1
    if held[frm][typ] <= 0: del held[frm][typ]
    held[to][typ] = held[to].get(typ,0)+1
    _place(typ, to, at)

def _unplace_all(p):
    for k,v in list(board.items()):
        if v.get("owner") == p:
            v.pop("realia"); v.pop("owner")
            if not v: del board[k]

def swap(a, b, note, hover=None, draw=60, check=True, at=None):
    """Player in seat a replaces player in seat b. check=False for a Chaos acclamation.
    at: where the mover's pieces go in the new province, {code: square or [squares]}.
    Every soldier stays with its seat: bought ones pass to whoever now holds the seat they were
    bought for, the Warlord's army likewise, and a new Warlord's objective starts afresh (RULINGS, "A new Warlord"). The mover takes the displaced
    player's grain whatever its sign, so a debt passes to the mover; the displaced player
    draws 60 from the pile. A Chaos acclamation (check=False) may seat a player in debt."""
    global pile
    _waiting("swap")
    pa, pb = pid(a), pid(b)
    if check:
        if a == 8:
            pass   # the Warlord's objective is raided realia, checked by the script
        else:
            missing = [t for t in need_for(a) if not held[pa].get(t)]
            assert not missing, f"{SHORT[pa]} can't change seats; missing {missing}"
            assert grain[pa] >= 20, f"{SHORT[pa]} needs 20 grain in hand, has {grain[pa]}"
        assert grain[pa] >= 0, f"{SHORT[pa]} is in debt and can't change seats"
        assert not (CHAOS and b == 1), "under Chaos the throne passes only by acclamation (RULINGS): acclamation()"
        if b == 1: assert a in (2,3,4,8) or (a == 5 and not set(ACTIVE) & {2,3,4}), \
            "only the Official, Gentry, Scholar or Warlord may take the throne (or the Silk Peasant, with no upper class at the table)"
        if a in (5,6,7) and b != 1: assert b in (2,3,4,5,6,7), "a peasant may replace the Gentry, Scholar, Official or a peasant"
    if b in REALIA:                      # pieces native to the new seat go back to auction
        t = REALIA[b]
        if t in held[pa]:
            stock.setdefault(b,{}); stock[b][t] = stock[b].get(t,0)+held[pa].pop(t)
    if b == 1:                            # becoming Emperor: return everything
        for t,c in list(held[pa].items()):
            o = home(t)
            stock.setdefault(o,{}); stock[o][t] = stock[o].get(t,0)+c
        held[pa] = {}
    for t,c in list(held[pb].items()):    # the displaced player returns everything
        o = home(t)
        stock.setdefault(o,{}); stock[o][t] = stock[o].get(t,0)+c
    held[pb] = {}
    _unplace_all(pb); _unplace_all(pa)
    grain[pa] = round(grain[pa]+grain[pb], 2); grain[pb] = 0.0
    grain[pb] = round(grain[pb]+draw, 2); pile = round(pile-draw, 2)   # in full, even below zero (RULINGS)
    seat[a], seat[b] = pb, pa
    for s in SOLDIERS.values():           # bought soldiers stay with the seat too (RULINGS)
        if s["side"] == "B" and s["owner"] in (pa, pb): s["owner"] = pb if s["owner"] == pa else pa
    if 8 in (a, b):                      # the army stays with the seat; the objective starts afresh
        for s in SOLDIERS.values():
            if s["side"] == "W": s["owner"] = seat[8]
        warlord_got.clear()
    want ={t:([v] if isinstance(v,str) else list(v)) for t,v in (at or {}).items()}
    assert {t:len(v) for t,v in want.items()} == {t:c for t,c in held[pa].items()}, \
        f"say where {SHORT[pa]}'s pieces go: {held[pa]}"
    for t, sqs in want.items():
        for q in sqs: _place(t, pa, q)
    ENTRIES.append(dict(k="act", t=note, h=_norm(hover), who=None, d={}, hl=[a,b], state=snap(), big=True, mv=[]))

def _waiting(what):
    assert not CALLED, f"a revolt is called and not yet settled, so play waits ({what}): revolt() or revolt_dropped() first (RULINGS)"

def revolt_called(text, hover=None):
    """A revolt is called with two others agreeing (Section 16). Until it stands (revolt()) or is
    dropped (revolt_dropped()), play waits: only talk, persuasion, deals and the Emperor's answer,
    and no seat change, no step of the round (RULINGS, calling off a revolt; Manish, 2026-10-28)."""
    global CALLED
    assert not CHAOS and not CALLED, "a revolt is already under way"
    CALLED = text
    act(text, hover, map_hl=list(ACTIVE), big=True)

def revolt_dropped(text, hover=None):
    """The revolt fails: the caller and two others no longer all back it. Play resumes."""
    global CALLED
    assert CALLED, "no revolt has been called"
    CALLED = None
    act(text, hover, map_hl=list(ACTIVE))

def revolt(text, hover=None):
    """A revolt stands (Section 16, RULINGS "Calling off a revolt"): Chaos begins. Until an Emperor is
    acclaimed there is no tax, salaries, public works or new land, and the treasury in Province 1 is
    sealed: the deposed Emperor can't spend it, though Province 1's harvest, raids, disasters and card
    effects still run through it (RULINGS, the sealed treasury)."""
    global CHAOS, CALLED
    assert not CHAOS, "Chaos has already begun"
    CHAOS = True; CALLED = None
    act(text, hover, map_hl=list(ACTIVE), big=True)

def acclaim_counts(claims):
    """claims: {claimant seat: [backer seats]}. Each claimant's grain in hand, soldiers on the board
    (the ones they control: the Warlord's army, or soldiers bought for their province) and friends
    (the players backing them, never themselves). Returns ({seat: (grain, soldiers, friends)},
    {count: leading seat or None}, the acclaimed seat or None) (RULINGS, counting the acclamation)."""
    backers = [b for bs in claims.values() for b in bs]
    assert 1 not in claims, "the deposed Emperor can't claim the throne"
    assert len(backers) == len(set(backers)), "each player backs one claim at most"
    assert not set(backers) & set(claims), "a claimant isn't their own friend, and can't back a rival"
    counts = {s: (grain[pid(s)], sum(1 for o in SOLDIERS.values() if o["owner"] == pid(s)), len(bs))
              for s, bs in claims.items()}
    lead = {}
    for i, k in enumerate(("grain", "soldiers", "friends")):
        top = max((c[i] for c in counts.values()), default=0)
        at = [s for s, c in counts.items() if c[i] == top]
        lead[k] = at[0] if len(at) == 1 and top > 0 else None   # a tie leads nobody
    n = {s: sum(1 for v in lead.values() if v == s) for s in claims}
    best = max(n.values(), default=0)
    win = [s for s, v in n.items() if v == best]
    return counts, lead, (win[0] if best and len(win) == 1 else None)

def acclamation(claims, text=None, hover=None):
    """Count the acclamation under Chaos (RULINGS, counting the acclamation). A claimant who leads in
    one count is acclaimed if no rival leads in another; otherwise the one who leads in more of the
    three. With a winner, they take the throne and the sealed treasury, whatever its sign, the deposed
    Emperor takes their seat and draws 60, and Chaos ends. Returns the acclaimed seat, or None."""
    global CHAOS
    assert CHAOS, "an acclamation is counted only under Chaos"
    counts, lead, win = acclaim_counts(claims)
    word = {"grain": "grain", "soldiers": "soldiers", "friends": "friends"}
    rows = [f"{SHORT[pid(s)]}: grain {c[0]:g}, soldiers {c[1]}, friends {c[2]}"
            + (" (" + ", ".join(SHORT[pid(b)] for b in claims[s]) + ")" if claims[s] else "") for s, c in counts.items()]
    leads = "; ".join(f"most {word[k]}: " + (SHORT[pid(v)] if v else "nobody") for k, v in lead.items())
    res = (f"{NAMES[pid(win)]} is acclaimed Emperor." if win else "No Emperor emerges. Chaos goes on.")
    act(text or f"The acclamation is counted. {leads}. {res}",
        hover or ("The claims: " + "; ".join(rows) + "."), map_hl=sorted(claims), big=bool(win))
    if win:
        new = NAMES[pid(win)]; old = NAMES[pid(1)]
        swap(win, 1, f"{new} takes the throne of Province 1 and the sealed treasury. {old} takes {new}'s seat as the {ROLE[win]}.", check=False)
        CHAOS = False
    return win

WORD = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
def spell(n):
    if n != int(n): return f"{n:g}"
    n = int(n)
    if n >= 100:
        rest = n % 100
        return WORD[n//100].capitalize() + " hundred" + (" and " + spell(rest).lower() if rest else "")
    if n <= 20: return WORD[n].capitalize()
    t = {20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
    return t[n-n%10] + ("-"+WORD[n%10] if n%10 else "")

# ------------------------------------------------------------------ soldiers
# Every soldier stands on a square and moves at most one square a round, diagonals
# included (Section 14, Note 16). The Warlord's soldiers are W1, W2, ...; a bought
# soldier is named after its buyer: Reina1, Reina2, Paddy1, ...

def rob_n():
    """The Warlord's soldiers still in play."""
    return sum(1 for s in SOLDIERS.values() if s["side"] == "W")

def _at(q, side=None):
    return [i for i,s in SOLDIERS.items() if s["sq"] == q and (side is None or s["side"] == side)]

def _step(i, to):
    s = SOLDIERS.get(i)
    assert s, f"no soldier {i}"
    assert CUR_ROUND and CUR_ROUND >= 1, "soldiers move from Round One"
    assert s["moved"] != CUR_ROUND, f"{i} has already moved this round"
    frm = s["sq"]
    assert dist(frm, to) == 1, f"{i} is on {frm}; {to} is {dist(frm,to)} squares away, and a soldier moves one square a round"
    return s, frm

def _capture(i, frm, to, side):
    """i moves onto a square held by the other side: legal only horizontally or vertically."""
    foes = _at(to, "B" if side == "W" else "W")
    if not foes: return None
    assert _orth(frm, to), f"{i} can't capture on {to} from {frm}: captures are horizontal or vertical, never diagonal"
    assert len(foes) == 1, f"{to} holds {len(foes)} soldiers"
    del SOLDIERS[foes[0]]
    return foes[0]

def march(moves, text=None, hover=None, take=None):
    """The Warlord moves. moves: {soldier: square}, one square each, before any province's
    soldiers move this round. A soldier that steps onto an un-raided square of an occupied
    province raids it: 5, or 10 in Province 1; a palace square costs the Emperor 20.
    take: {soldier: (code, square)} to take the realia on the raided square as tribute,
    placing it on a square of the Warlord's territory. Tolls are paid automatically."""
    _waiting("march")
    assert 8 in ACTIVE
    assert _troops_round != CUR_ROUND, "the Warlord moves before the provinces' soldiers"
    take = take or {}
    d = {}; w = pid(8); notes = []; mv = []; hl = {8}
    def pay(p, amt):
        d[p] = d.get(p,0) - amt; d[w] = d.get(w,0) + amt
    for i, to in moves.items():
        s, frm = _step(i, to)
        assert s["side"] == "W", f"{i} isn't the Warlord's"
        got = _capture(i, frm, to, "W")
        if got: notes.append(f"{i} captures {got} on {to}.")
        for p, what in tolls(frm, to):
            d[w] = d.get(w,0) - 5; d[pid(p)] = d.get(pid(p),0) + 5
            notes.append(f"{i} crosses {what}: 5 to {SHORT[pid(p)]}.")
            hl.add(p)
        s["sq"] = to; s["moved"] = CUR_ROUND
        mv.append([frm, to, "W"])
        p = owner(to); cell = board.get(to, {})
        raids_here = p in ACTIVE and not cell.get("raid")
        assert raids_here or i not in take, f"{i} doesn't raid {to}, so it can't take anything there"
        if not raids_here: continue
        assert p not in NORAID.get(CUR_ROUND, ()), f"the Warlord's disaster forbids raiding Province {p} this round"
        hl.add(p); payer = pid(p); work = _work_at(to)
        if work in PALACES:
            pay(payer, 20)
            # the Emperor holds no realia, but at eight players one palace raid may stand in
            # for one player's piece (RULINGS.md); it's recorded once, under "palace"
            if len(ACTIVE) >= 8 and "palace" not in warlord_got: warlord_got["palace"] = work
            notes.append(f"{i} raids the {work} on {to}: the Emperor pays the cost of the structure, 20.")
        elif i in take:
            code, where = take[i]
            assert cell.get("realia") == code and cell.get("owner") == payer, f"{to} holds no {RNAME[code]} of {SHORT[payer]}'s"
            cell.pop("realia"); cell.pop("owner")
            held[payer][code] -= 1
            if not held[payer][code]: del held[payer][code]
            held[w][code] = held[w].get(code,0) + 1
            _place(code, w, where)
            warlord_got[payer] = code
            notes.append(f"{i} raids {to} and takes {SHORT[payer]}'s {RNAME[code]}.")
        else:
            amt = 10 if p == 1 else 5
            pay(payer, amt)
            notes.append(f"{i} raids {to} in Province {p}: {amt} from {SHORT[payer]}.")
        cell["raid"] = True; board[to] = cell
        raids[p] += 1
    h = _norm(hover) or []
    if notes: h = h + [{"w":"","t":" ".join(notes)}]
    act(text or "Robert Land moves.", h or None, d, map_hl=sorted(hl), moves=mv)

def hire_soldier(at, text, hover=None):
    """The Warlord hires one soldier at the end of his turn (RULINGS.md, "The Warlord hires
    reinforcements"): 20 to the Harvest Pile, on a square of his own territory, at most one
    a round, and his army may grow to one more than it started with. It moves next round."""
    global pile
    _waiting("hire_soldier")
    assert 8 in ACTIVE
    assert hired.get(CUR_ROUND, 0) == 0, "the Warlord hires at most one soldier a round"
    assert rob_n() < ARMY + 1, f"the Warlord's army may grow only to {ARMY + 1}"
    assert region(at) == "8" and not _at(at), f"a hired soldier stands on an empty square of the Warlord's territory, not {at}"
    w = pid(8)
    _spend(w, 20, "hire a soldier")
    n = 1
    while f"W{n}" in SOLDIERS or f"W{n}" in _named: n += 1
    SOLDIERS[f"W{n}"] = dict(side="W", owner=w, sq=at, home=8, moved=CUR_ROUND)
    _named.add(f"W{n}")
    hired[CUR_ROUND] = 1
    act(text, hover, {w: -20}, map_hl=[8], pile_delta=20)

def sell_soldiers(buys, text, hover=None):
    """buys: [(seat, square), ...]; each pays the Warlord 20 for a soldier standing on
    that square of the buyer's province. He keeps 5 of each and 15 goes to the pile."""
    global pile
    _waiting("sell_soldiers")
    d = {}; w = pid(8)
    for s, q in buys:
        p = pid(s)
        assert prov(q) == s, f"a bought soldier starts in its buyer's province: {q} isn't in Province {s}"
        assert not _at(q, "W"), f"a Warlord soldier stands on {q}"
        assert all(SOLDIERS[o]["owner"] == p for o in _at(q)), f"another player's soldier stands on {q}"
        _spend(p, 20, "buy a soldier")
        n = 1
        while f"{SHORT[p]}{n}" in _named: n += 1
        SOLDIERS[f"{SHORT[p]}{n}"] = dict(side="B", owner=p, sq=q, home=s, moved=None)
        _named.add(f"{SHORT[p]}{n}")
        d[p] = d.get(p,0)-20; d[w] = d.get(w,0)+5
    act(text, hover, d, map_hl=[s for s,_ in buys]+[8], pile_delta=15*len(buys))

def troops(moves, text, hover=None):
    """A province's soldiers move, after the Warlord's (Section 14). moves: {soldier: square}.
    A bought soldier can't move until the Warlord has raided the province it was bought in.
    Stepping horizontally or vertically onto a Warlord soldier captures it."""
    global _troops_round
    _waiting("troops")
    mv = []; notes = []
    for i, to in moves.items():
        s, frm = _step(i, to)
        assert s["side"] == "B", f"{i} is the Warlord's"
        assert raids[s["home"]] > 0, f"{i} can't move until the Warlord has raided Province {s['home']}"
        others = [o for o in _at(to, "B") if SOLDIERS[o]["owner"] != s["owner"]]
        assert not others, f"{to} holds another player's soldier"
        got = _capture(i, frm, to, "B")
        if got: notes.append(f"{i} captures the Warlord's {got} on {to}.")
        s["sq"] = to; s["moved"] = CUR_ROUND
        mv.append([frm, to, "B"])
    _troops_round = CUR_ROUND
    h = _norm(hover) or []
    if notes: h = h + [{"w":"","t":" ".join(notes)}]
    act(text, h or None, None, map_hl=sorted({prov(m[1]) or 8 for m in mv}), moves=mv)

# ------------------------------------------------------------------ export
def export(results_note, epilogue, no_winners=False):
    """Score the game (Section 18) and return everything the page needs.
    Assign the result to RESULT at the end of the script. no_winners: the game ended in
    collapse (Section 18), so nobody won or lost; the page shows a dash for every verdict."""
    res = []
    for p in PLAYERS:
        fin = sid(p); st = p
        v = "won" if fin < st else ("lost" if fin > st else "held")
        if st == 1 and fin == 1: v = "won"      # Section 18: an Emperor still on the throne has won
        if no_winners: v = "none"
        res.append(dict(name=NAMES[p], short=SHORT[p], start=st, startrole=ROLE[st],
                        fin=fin, finrole=ROLE[fin], verdict=v, grain=round(grain[p],2)))
    return dict(meta=META, active=ACTIVE, names={str(p):NAMES[p] for p in PLAYERS},
        short={str(p):SHORT[p] for p in PLAYERS}, role={str(s):ROLE[s] for s in range(1,9)},
        rname=RNAME, need={str(s):need_for(s) for s in ACTIVE if s in REALIA},
        owed=owed(), entries=ENTRIES, rounds=ROUNDS, results=res,
        results_note=results_note, epilogue=epilogue,
        grid=GRID, map=dict(rivers=RIVERS, coast=_MAP["coast"],
            wall={str(p):[[l["from"], l["to"]] for l in v] for p,v in WALL_LINKS.items()},
            canal={str(p):[s["path"] for s in v] for p,v in CANAL_SECTIONS.items()}))
