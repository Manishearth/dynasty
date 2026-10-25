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
import re as _re

NAMES = {1:"Reina Osorio",2:"Clark Grafton",3:"Richard Baron",4:"Ken Nakamura",
         5:"Silke Weber",6:"Paddy Doyle",7:"Graham Garner",8:"Robert Land"}
SHORT = {1:"Reina",2:"Clark",3:"Rich",4:"Ken",5:"Silke",6:"Paddy",7:"Graham",8:"Rob"}
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

# ------------------------------------------------------------------ setup
def setup(active, key, title, subtitle, blurb, short=""):
    """Start a game. active: the seats in play. key: URL fragment (#key).
    title/subtitle/short: the game selector button. blurb: the line under the header.
    Deals 60 grain to everyone, fills each province's realia stock by player count,
    and takes the starting grain out of a 2,500-million Harvest Pile."""
    global ACTIVE, PLAYERS, seat, grain, stock, held, bonus, raids, pw, board
    global pile, ENTRIES, ROUNDS, META, MULT, CUR_Q, CUR_INC, CUR_HARV
    global dis_next, used_cards, pending_bonus, warlord_got
    ACTIVE = sorted(active)
    PLAYERS = list(ACTIVE)
    seat = {s:s for s in ACTIVE}
    grain = {p:60.0 for p in PLAYERS}
    pile = PILE_START - 60*len(PLAYERS)
    n = len(ACTIVE)
    stock = {}
    for s in ACTIVE:
        if s in REALIA:
            if n <= 5:   stock[s] = {REALIA[s]:1, NEVER[s]:2}
            elif n == 6: stock[s] = {REALIA[s]:2}
            else:        stock[s] = {REALIA[s]:4}
    held = {p:{} for p in PLAYERS}
    bonus = {s:0 for s in ACTIVE}
    pending_bonus = {}
    raids = {s:0 for s in range(1,9)}
    pw = {"Summer Palace":0,"Winter Palace":0,"Marble Pagoda":0,
          "wall":{1:0,2:0,3:0},"canal":{1:0,4:0,5:0,6:0},"irr2":0,"res3":0,"res7":0}
    board = {}
    ENTRIES = []; ROUNDS = []
    MULT = 1; CUR_Q = {}; CUR_INC = {}; CUR_HARV = {}
    dis_next = {s:0 for s in ACTIVE}
    used_cards = set()
    global warlord_got, ROB_N, rob_pos
    warlord_got = {}
    ROB_N = (4 if len(ACTIVE) >= 8 else 2) if 8 in ACTIVE else 0
    rob_pos = []
    META = dict(key=key, title=title, subtitle=subtitle, blurb=blurb, short=short)

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
    if 2 in ACTIVE: o.append(["Province 2 Irrigation",1,30])
    if 3 in ACTIVE: o.append(["Province 3 Reservoir",1,80])
    if 7 in ACTIVE: o.append(["Province 7 Reservoir",1,60])
    return o

def built_count(name):
    if name == "Great Wall": return sum(pw["wall"].values())
    if name == "Grand Canal": return sum(pw["canal"].values())
    return {"Province 2 Irrigation":pw["irr2"],"Province 3 Reservoir":pw["res3"],
            "Province 7 Reservoir":pw["res7"]}.get(name, pw.get(name, 0))

def all_built():
    return all(built_count(n) >= t for n,t,_ in owed())

def home(t):
    """Where a returned piece goes: its native province, or, if that province is empty,
    the province that started the game holding it (rulebook Note 11)."""
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
                raids={str(k):v for k,v in raids.items()},
                pw={k:(dict((str(a),b) for a,b in v.items()) if isinstance(v,dict) else v) for k,v in pw.items()},
                bonus={str(k):v for k,v in bonus.items()},
                board={k:dict(v) for k,v in board.items()},
                pile=round(pile,2), mult=MULT,
                rob={str(k):v for k,v in warlord_got.items()})

def _apply(d):
    for k,v in (d or {}).items():
        grain[k] = round(grain[k]+v, 2)

def act(text, hover=None, deltas=None, map_hl=None, pile_delta=0, big=False):
    """A game event: a bold, clickable line in the transcript.
    deltas: {player_id: grain change}. pile_delta: change to the Harvest Pile.
    map_hl: seats to highlight on the board. big: style as a turning point."""
    global pile
    _apply(deltas); pile = round(pile+pile_delta, 2)
    ENTRIES.append(dict(k="act", t=text, h=_norm(hover), who=None,
        d={str(k):v for k,v in (deltas or {}).items()}, hl=map_hl or [],
        state=snap(), big=big))

def say(who, text, hover=None):
    """Table talk: an in-character line. Changes nothing. hover is the thought behind it."""
    ENTRIES.append(dict(k="say", t=text, h=_norm(hover, who), who=who, d={}, hl=[], state=snap()))

# ------------------------------------------------------------------ rounds
def R(n, title, card=None, card_text=None):
    """Start a round. card is a key in CARDS (None for round one)."""
    global MULT, CUR_Q
    for s,v in pending_bonus.items(): bonus[s] += v
    pending_bonus.clear()
    q = None
    if card:
        assert card not in used_cards, "card drawn twice: "+card
        used_cards.add(card)
        c = CARDS[card]; card_text = c["text"]
        q = c["q"]
        if c.get("pop"): MULT = MULT * c["pop"]
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
    d = {}; e = pid(1); lines = []
    for s in ACTIVE:
        if s == 1 or s in skip: continue
        inc = CUR_INC[s] + (extra or {}).get(s,0)
        t = round(max(0,inc)*rate, 2)
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
    pay = pay or {s:5 for s in (2,4) if s in ACTIVE}
    if not pay: return
    e = pid(1); d = {e:0}
    for s,a in pay.items(): d[pid(s)] = d.get(pid(s),0)+a; d[e] -= a
    label = text or ("Salaries: " + ", ".join(f"{a:g} to the {ROLE[s]}" for s,a in pay.items()) + ".")
    act(label, hover or "The Emperor owes the Official and the Scholar at least 5 a year.", d,
        map_hl=[1]+list(pay.keys()))

PW_BONUS = {"irr2":(2,10),"res3":(3,20),"res7":(7,20)}
def build(name, cost, split, wall=None, canal=None, key=None, hover=None, text=None):
    """split: {seat: amount}. wall/canal: {seat: n}. key: 'Summer Palace', 'irr2', ..."""
    d = {}
    for s,a in split.items(): d[pid(s)] = d.get(pid(s),0)-a
    assert abs(sum(split.values())-cost) < 1e-6, (name, cost, split)
    for s,n in (wall or {}).items(): pw["wall"][s] += n
    for s,n in (canal or {}).items():
        pw["canal"][s] += n; pending_bonus[s] = pending_bonus.get(s,0)+10*n
    if key:
        pw[key] = 1
        if key in PW_BONUS:
            s,b = PW_BONUS[key]; pending_bonus[s] = pending_bonus.get(s,0)+b
    act(text or f"Public works: {name} — {cost:g} paid.",
        hover or ("Cost split: "+", ".join(f"{SHORT[pid(s)]} {a:g}" for s,a in split.items())+"."),
        d, map_hl=list(split.keys()))

def disaster(s, text, hover=None):
    """Play the next personal disaster in seat s's booklet."""
    global pile
    i = dis_next[s] % 3; dis_next[s] += 1
    kind, v = DISASTERS[s][i]
    p = pid(s)
    if kind == "fixed": amt = v
    elif kind == "frac_income": amt = round(max(0, CUR_INC[s])*v, 2)
    elif kind == "frac_harvest": amt = round(CUR_HARV[s]*v, 2)
    elif kind == "frac_grain": amt = round(max(0, grain[p])*v, 2)
    else: amt = 0
    act(f"{SHORT[p]}'s disaster #{i+1}: {text}" + (f" — {amt:g} to the Harvest Pile." if amt else ""),
        hover, {p:-amt} if amt else None, map_hl=[s], pile_delta=amt)
    return kind

def lot(sell, typ, ladder, hover=None):
    """ladder: list of (bidder_seat, amount|None, text|None, hover|None). Last numeric bid wins."""
    global pile
    bids = []
    for b,amt,txt,hov in ladder:
        bids.append(dict(who=SHORT[pid(b)], t=txt or (spell(amt)+"." if amt is not None else "Out."),
                         h=_norm(hov, SHORT[pid(b)]), amt=amt))
    win = [r for r in ladder if r[1] is not None][-1]
    wb, price = win[0], win[1]
    stock[sell][typ] -= 1
    if stock[sell][typ] <= 0: del stock[sell][typ]
    held[pid(wb)][typ] = held[pid(wb)].get(typ,0)+1
    place(wb, typ, pid(wb))
    d = {pid(wb):-price}
    d[pid(sell)] = d.get(pid(sell),0) + price*0.25
    pile = round(pile + price*0.75, 2)
    _apply(d)
    note = (f"{SHORT[pid(wb)]} pays {price:g}. {SHORT[pid(sell)]} keeps {price*0.25:g} as commission; "
            f"{price*0.75:g} goes to the Harvest Pile.")
    h = _norm(hover) or []
    h = h + [{"w":"","t":note}]
    ENTRIES.append(dict(k="lot", t=f"{RNAME[typ]} — {SHORT[pid(wb)]} takes it for {price:g}.",
        h=h, who=None, bids=bids, d={str(k):v for k,v in d.items()},
        hl=[sell, wb], state=snap()))

def B(seat, amt, text=None, th=None):
    """One bid in a lot ladder. amt=None is a pass. text defaults to the amount in words."""
    return (seat, amt, text, th)

def raid(rows, text="Robert Land raids.", hover=None):
    """rows: [(seat, tribute)]. Marks an unraided square per row and moves a soldier there.
    Tribute is 5, or 10 in Province 1. The script must respect the soldier count."""
    d = {}; txt = []
    for s,amt in rows:
        raids[s] += 1; mark_raid(s)
        d[pid(s)] = d.get(pid(s),0)-amt; d[pid(8)] = d.get(pid(8),0)+amt
        txt.append(f"Province {s} pays {amt:g}")
    act(text, hover or ("A raided square can never be raided again. "+", ".join(txt)+"."),
        d, map_hl=[s for s,_ in rows]+[8])

PALACE_CELL = {"Summer Palace":(2,21),"Winter Palace":(2,23),"Marble Pagoda":(2,25)}
def raid_take(s, typ, text, hover=None):
    """The Warlord raids a square in seat s holding realia typ and takes the piece."""
    p = pid(s)
    for k,v in list(board.items()):
        if v.get("realia")==typ and v.get("owner")==p and not v.get("raid"):
            v.pop("realia"); v.pop("owner",None); v["raid"]=True; _move_soldier(k); break
    else:
        mark_raid(s)
    raids[s] += 1
    held[p][typ] -= 1
    if held[p][typ] <= 0: del held[p][typ]
    held[pid(8)][typ] = held[pid(8)].get(typ,0)+1
    place(8, typ, pid(8))
    warlord_got[p] = typ
    act(text, hover, None, map_hl=[s,8])

def raid_palace(name, text, hover=None):
    """The Warlord raids the square holding one of the Emperor's buildings; the Emperor pays its cost."""
    r,c = PALACE_CELL[name]; k = f"{r},{c}"
    cell = board.get(k,{}); cell["raid"]=True; board[k]=cell; _move_soldier(k)
    raids[1] += 1
    warlord_got[pid(1)] = name
    act(text, hover, {pid(1):-20, pid(8):20}, map_hl=[1,8])

def sell_soldiers(buyers, text, hover=None):
    """Each seat in buyers pays the Warlord 20 for a soldier; he keeps 5, 15 to the pile."""
    global pile
    d = {}
    for s in buyers:
        d[pid(s)] = d.get(pid(s),0)-20; d[pid(8)] = d.get(pid(8),0)+5
        place_soldier(s)
    act(text, hover, d, map_hl=list(buyers)+[8], pile_delta=15*len(buyers))

def give(frm, to, typ):
    """Move one piece of realia between players (by player id) for a private trade.
    The grain side of the trade is a separate act() with deltas."""
    held[frm][typ] -= 1
    if held[frm][typ] <= 0: del held[frm][typ]
    held[to][typ] = held[to].get(typ,0)+1
    for k,v in list(board.items()):
        if v.get("realia")==typ and v.get("owner")==frm and not v.get("raid"):
            del board[k]; break
    place(sid(to), typ, to)

def swap(a, b, note, hover=None, draw=60, check=True):
    """Player in seat a replaces player in seat b. check=False for a Chaos acclamation."""
    global pile
    pa, pb = pid(a), pid(b)
    if check:
        if a == 8:
            pass   # the Warlord's objective is raided realia, checked by the script
        else:
            missing = [t for t in need_for(a) if not held[pa].get(t)]
            assert not missing, f"{SHORT[pa]} can't change seats; missing {missing}"
            assert grain[pa] >= 20, f"{SHORT[pa]} needs 20 grain in hand, has {grain[pa]}"
        if b == 1: assert a in (2,3,4,8), "only the Official, Gentry, Scholar or Warlord may take the throne"
        if a in (5,6,7): assert b in (2,3,4,5,6,7), "a peasant may replace the Gentry, Scholar, Official or a peasant"
    if b in REALIA:                       # pieces native to the new seat go back to auction
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
    unplace_all(pb); unplace_all(pa)
    grain[pa] = round(grain[pa]+grain[pb], 2); grain[pb] = 0.0
    take = min(draw, max(0,pile)); grain[pb] = round(grain[pb]+take, 2); pile = round(pile-take, 2)
    seat[a], seat[b] = pb, pa
    for t,c in held[pa].items():
        for _ in range(c): place(b, t, pa)
    ENTRIES.append(dict(k="act", t=note, h=_norm(hover), who=None, d={}, hl=[a,b], state=snap(), big=True))

WORD = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()
def spell(n):
    if n != int(n): return f"{n:g}"
    n = int(n)
    if n <= 20: return WORD[n].capitalize()
    t = {20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety"}
    return t[n-n%10] + ("-"+WORD[n%10] if n%10 else "")

# ------------------------------------------------------------------ board
COLS, ROWS = 30, 17
def _reg(r,c):
    if c >= 27: return 'S' if r >= 2 else '.'
    if r == 0: return 'W' if 7 <= c <= 26 else '.'
    if r == 1: return 'n' if 7 <= c <= 26 else '.'
    if c <= 6: return '8'
    if 2 <= r <= 6:  return '3' if c <= 13 else ('2' if c <= 20 else '1')
    if 7 <= r <= 10: return '3' if c <= 13 else ('4' if c <= 20 else '5')
    if 11 <= r <= 13:return '7' if c <= 13 else ('6' if c <= 20 else '5')
    return '7' if c <= 13 else '6'
GRID = [[_reg(r,c) for c in range(COLS)] for r in range(ROWS)]
CELLS = {str(p):[(r,c) for r in range(ROWS) for c in range(COLS) if GRID[r][c]==str(p)] for p in range(1,9)}

# squares the page draws public works on; pieces and raids never land here
RESERVED = {(2,21),(2,23),(2,25),(5,22),(5,23),(9,17),(9,18),(8,22),(8,23),(12,16),(12,17),(5,15),(6,8),(16,8)}
def _free(p, want_realia=False):
    for (r,c) in CELLS[str(p)]:
        if (r,c) in RESERVED: continue
        k = f"{r},{c}"; cell = board.get(k,{})
        if want_realia and cell.get("realia") and not cell.get("raid"): return k
        if not want_realia and not cell.get("realia") and not cell.get("raid") and not cell.get("own_soldier"): return k
    return None
def place(p, typ, owner):
    """Put a piece on the first free square in seat p (purchased realia must be placed)."""
    k = _free(p)
    if k: board[k] = {"realia":typ, "owner":owner}
def unplace_all(p):
    for k,v in list(board.items()):
        if v.get("realia") and not v.get("raid") and v.get("owner")==p: del board[k]
def _move_soldier(k):
    rob_pos.append(k)
    while len(rob_pos) > ROB_N:
        old = rob_pos.pop(0)
        if old in board: board[old].pop("soldier", None)
    if k in board: board[k]["soldier"] = True

def mark_raid(p, take=False):
    k = _free(p, want_realia=take) or _free(p)
    if k:
        cell = board.get(k,{}); cell["raid"] = True; board[k] = cell
        if take: cell.pop("realia", None)
        _move_soldier(k)

def capture_soldier(text, hover=None):
    """One of the Warlord's soldiers is captured and removed from play."""
    global ROB_N
    ROB_N -= 1
    if rob_pos:
        old = rob_pos.pop(0)
        if old in board: board[old].pop("soldier", None)
    act(text, hover, None, map_hl=[8])
def place_soldier(p):
    """A bought soldier, drawn in blue, on the last free square of seat p."""
    for (r,c) in reversed(CELLS[str(p)]):
        if (r,c) in RESERVED: continue
        k = f"{r},{c}"
        if not board.get(k,{}).get("soldier") and not board.get(k,{}).get("own_soldier"):
            cell = board.get(k,{}); cell["own_soldier"] = True; board[k] = cell; return

# ------------------------------------------------------------------ export
def export(results_note, epilogue):
    """Score the game (Section 18) and return everything the page needs.
    Assign the result to RESULT at the end of the script."""
    res = []
    for p in PLAYERS:
        fin = sid(p); st = p
        v = "won" if fin < st else ("lost" if fin > st else "held")
        if st == 1 and fin == 1: v = "won"      # Section 18: an Emperor still on the throne has won
        res.append(dict(name=NAMES[p], short=SHORT[p], start=st, startrole=ROLE[st],
                        fin=fin, finrole=ROLE[fin], verdict=v, grain=round(grain[p],2)))
    return dict(meta=META, active=ACTIVE, names={str(p):NAMES[p] for p in PLAYERS},
        short={str(p):SHORT[p] for p in PLAYERS}, role={str(s):ROLE[s] for s in range(1,9)},
        rname=RNAME, need={str(s):need_for(s) for s in ACTIVE if s in REALIA},
        owed=owed(), entries=ENTRIES, rounds=ROUNDS, results=res,
        results_note=results_note, epilogue=epilogue,
        grid=[''.join(r) for r in GRID])
