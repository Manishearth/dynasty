"""The Storyteller's prompt generator. Every prompt is written once: this script builds it
from the engine's state (the game's game.py) and the table talk recorded so far, writes it to
the log, and prints it to send with SendMessage (or Agent, for a launch).

Run from the game's folder (playthroughs/<name>/), as python ../../playthrough-sim/agents/briefs.py ...:

  python briefs.py heard 021 log/year2/021-silke-reply.md   # file a reply's say and whisper as table talk
  python briefs.py event "Paddy buys the Jar for 27 and puts it on R21."
  python briefs.py note "..." [--to Player]                  # a correction, to all or to one
  python briefs.py seen all                                  # after the closing catch-up, sent by hand: everyone is up to date

  python briefs.py prompt 022 Silke launch --menu menu.md    # a fresh agent: the character brief first
  python briefs.py prompt 022 Reina launch:crown             # a launch carrying any menu below (launch:auctions --lots ...)
  python briefs.py prompt 022 Reina crown                    # the Emperor's year: tax, one work, salaries, land
  python briefs.py prompt 022 Rich rent                      # the Gentry: pays the harvest, asks the rent
  python briefs.py prompt 022 Clark collect --rate 40        # the Official: collects the declared tax
  python briefs.py prompt 022 Noah iching                    # the Scholar: reads the card, the population
  python briefs.py prompt 022 Paddy land                     # new land (from the first doubling)
     (--offer "half of every square": what the Emperor said in the crown's year they'd pay)
  python briefs.py prompt 099 Paddy diary --years "Years 11-12"   # the chapter-end diary entry (reply: diary: ...)
  python briefs.py prompt 022 Silke auctions --lots 2:CH,3:LD,5:DJ   # every lot of the year at once
     (--floor 3:LD: lots unsold last round, which must open at 2)
  python briefs.py prompt 022 Silke place --lot 5:DJ --price 12      # a buyer places what they won (short)
  python briefs.py prompt 022 Silke auction --lot 6:BB --min 5       # one lot (small tables)
  python briefs.py prompt 022 Rob march
  python briefs.py prompt 022 Silke acclaim --claims "Rich:Paddy;Rob"   # under Chaos: claim, back or stand aside, with the count
  python briefs.py prompt 022 Paddy free --menu menu.md      # any other decision; the menu is your text
     (--land: add the new-land reminder, for a decision in the public works step; --offer as for land)

  python briefs.py resolve bids.json                         # settle one lot, or a year's lots, from ceilings
  add --dry to any prompt to print it without writing the log or marking it seen
  add --short to leave out the state block (the card stays): for follow-ups, and for any prompt late in a long chapter

Each prompt opens with the player's board card, then everything said and done at the table
since that player's last prompt (talk.jsonl, seen.json), then the state that matters to them,
the menu and the reply format. Geometry comes from geo.py and the engine, never by hand.

Nothing here names a player: the cast, the seats, the roles, the objectives and the jobs all
come from the engine (NAMES, SHORT, ROLE, ACTIVE, need_for, warlord_got, owed), so the same
script runs the five-player peasant table and the full eight.

A launch (a fresh agent for a seat, at the start of every chapter) also carries that
character's entry in ledger.md and their diary so far (diaries/<name>.md).
"""
import json, os, sys
from run import run_ns, steps
from geo import ranges

# Prompts go to log/year{N}/, N being the round game.py has reached (Setup counts as Year 1).
TALK, SEEN = "talk.jsonl", "seen.json"

# The cast (design/cast.md), keyed by player id, which is the seat each one draws. The engine
# holds the names; this holds what the engine doesn't: pronoun and the voice.
CAST = {
 1: ("she", "She manages the table: she plans years ahead, and she knows when she's walking into a revolt clause."),
 2: ("he", "He's gleeful about leverage, and he keeps a paper trail of grievances."),
 3: ("he", "He fawns out loud and calculates underneath, and he keeps his promises to the letter."),
 4: ("he", "He's honest to a fault, and he's the one who says the arithmetic out loud."),
 5: ("she", "She gets sharper as she gets squeezed."),
 6: ("he", "He's earnest and a little surprised to be winning."),
 7: ("he", "He gets quieter and more precise as the grievance builds."),
 8: ("he", "He's realised he's the villain, and he's having a wonderful time."),
}
NICK = {8: "Rob"}     # a short name that isn't the start of the full one: Robert Land ("Rob")

# Seats change hands (a completed set replaces a player), so roles, the table and the auction's
# seat order always come from the engine's current seats, never from the booklets drawn.
WHERE = {1: "Province 1, the north-east, under the Great Wall",
         2: "Province 2, the north, under the Great Wall",
         3: "Province 3, the north-west, under the Great Wall and against the desert",
         4: "Province 4, the centre-east, inland with a short stretch of coast",
         5: "Province 5, the east coast", 6: "Province 6, the south-east coast",
         7: "Province 7, the south centre", 8: "the western and southern desert"}
# The upper class's table jobs (rulebook §5, §9, Part Two). With the seat empty, the Emperor appoints (N3).
JOB = {2: "collects the tax for the crown; the Emperor pays the Official at least 5 a year for it",
       3: "runs the Harvest Pile and pays out every harvest, and may ask each peasant for rent of at least 5 a year (unasked, it isn't paid)",
       4: "reads the I Ching card each year and keeps the population counter; the Emperor pays the Scholar at least 5 a year for it"}
APPOINTED = {2: "collect the tax", 3: "bank the Harvest Pile", 4: "read the I Ching card"}
NUM = "zero one two three four five six seven eight".split()

def short_of(ns, p): return ns["SHORT"][p]
def pid_of(ns, player):
    for p in ns["PLAYERS"]:
        if ns["SHORT"][p] == player: return p
    raise SystemExit(f"{player} isn't at this table: {[ns['SHORT'][p] for p in ns['PLAYERS']]}")
def seat_of(ns, player): return ns["sid"](pid_of(ns, player))
def seat_order(ns): return [ns["SHORT"][ns["pid"](s)] for s in ns["ACTIVE"]]
def full(ns, p):
    n = ns["NAMES"][p]; s = NICK.get(p)
    return f'{n} ("{s}")' if s else n
def who_in(ns, seat): return ns["SHORT"][ns["pid"](seat)] if seat in ns["ACTIVE"] else None

def table_text(ns):
    A = ns["ACTIVE"]; R = ns["ROLE"]; who = []
    for s in A:
        f = full(ns, ns["pid"](s))
        who.append(f"{f} is the {R[s]}, holding {WHERE[s]}." if s == 8 else f"{f} is the {R[s]} ({WHERE[s]}).")
    last = last_round(ns)
    length = f"{NUM[last] if last < len(NUM) else last} rounds, then the table stops (Note 19)" if last else "about ten years"
    out = f"{NUM[len(A)].capitalize()} players, {length}. " + " ".join(who)
    empty = [s for s in range(2, 8) if s not in A]
    if empty:
        out += f" Province{'s' if len(empty) > 1 else ''} {', '.join(map(str, empty))} {'are' if len(empty) > 1 else 'is'} empty: nothing is owed there and nobody is paid."
    jobs = [f"{who_in(ns, s)}, the {R[s]}, {JOB[s]}." for s in (2, 3, 4) if s in A]
    gone = [APPOINTED[s] for s in (2, 3, 4) if s not in A]
    if gone: jobs.append("The Emperor appoints someone to " + (", ".join(gone[:-1]) + " and " if len(gone) > 1 else "") + gone[-1] + ".")
    if 3 not in A: jobs.append("With no Gentry, nobody pays rent.")
    return "## The table\n\n" + out + "\n\n" + " ".join(jobs)

ECONOMICS = ("**Auctions drain the table.** Three quarters of every price goes to the Harvest Pile and only a quarter "
  "to the seller, so a bidding war makes everyone poorer: grain that would have paid tax and built the works. "
  "Settling a contested piece by a public deal before the auction (one of you stands aside for a favour, or for "
  "first claim on the next piece) is legitimate (rulebook Section 8).")
WHISPER = ("**Whispers** exist for a genuinely private deal, one that can't be made in public. "
  "They're still rare: most turns, write \"none\".")
FORMAT_TAIL = """say: <what {short} says out loud to the whole table, a line or two>
aside: <one or two sentences, no more, that {short} says to the camera, talking the audience through the move. The other players can't hear it.>
whisper: <"none", or "To <name>: ..." (rare: only a genuinely private deal)>"""

# ------------------------------------------------------------------ talk and what each player has heard
def load_talk():
    if not os.path.exists(TALK): return []
    return [json.loads(l) for l in open(TALK, encoding="utf-8") if l.strip()]

def add_talk(rec):
    t = load_talk(); rec["i"] = len(t)
    with open(TALK, "a", encoding="utf-8") as f: f.write(json.dumps(rec, ensure_ascii=False) + "\n")

def load_seen():
    return json.load(open(SEEN, encoding="utf-8")) if os.path.exists(SEEN) else {}

def parse_reply(path):
    """The move, say, aside, whisper and 'if I drop out' fields of a reply file (above its '---')."""
    body = open(path, encoding="utf-8").read().split("\n---")[0]
    out, key = {}, None
    for line in body.splitlines():
        low = line.lower()
        for k in ("move", "say", "aside", "whisper", "if i drop out"):
            if low.startswith(k + ":"):
                key = k; out[k] = line[len(k)+1:].strip(); break
        else:
            if key and line.strip() and not line.startswith("#"): out[key] += " " + line.strip()
    return out

def heard(n, path):
    who = os.path.basename(path).split("-")[1].capitalize()
    r = parse_reply(path); whispered = False
    if r.get("say"): add_talk(dict(n=n, kind="say", who=who, text=r["say"].strip('"')))
    w = r.get("whisper", "none")
    if w and w.lower().strip(' ".') != "none":
        to = w.split(":")[0].replace("To", "").strip()
        add_talk(dict(n=n, kind="whisper", who=who, to=to, text=w.split(":", 1)[1].strip())); whispered = True
    print(f"filed {who}'s say" + (" and whisper" if whispered else ""))

def since(player):
    """Table talk and events this player hasn't been told yet (never their own lines or asides)."""
    last = load_seen().get(player, -1); out = []
    for t in load_talk():
        if t["i"] <= last: continue
        if t["kind"] == "event": out.append(t["text"])
        elif t["kind"] == "note" and t.get("to") in (None, player): out.append(f"(Storyteller's note: {t['text']})")
        elif t["kind"] == "say" and t["who"] != player: out.append(f"{t['who']}: \"{t['text']}\"")
        elif t["kind"] == "whisper" and t["to"] == player:
            out.append(f"**{t['who']} whispers to you** (passed on by the Storyteller): \"{t['text']}\"")
    return out

def mark_seen(player):
    s = load_seen(); t = load_talk(); s[player] = t[-1]["i"] if t else -1
    json.dump(s, open(SEEN, "w", encoding="utf-8"), indent=1)

# ------------------------------------------------------------------ state, from the engine
def has_warlord(ns):
    """Seat 8 is at the table. Without it nothing raids and no soldiers are sold, so the prompts never mention them."""
    return 8 in ns["ACTIVE"]

def free_squares(ns, seat):
    """Squares a newly bought piece may stand on: the seat's own, unraided, empty, not under a work."""
    busy = {q for v in ns["pw_at"].values() for q in v}
    own = ns["squares"](8) if seat == 8 else ns["squares"](seat)   # pieces go on the province itself (N10)
    return [q for q in own if q not in busy
            and not ns["board"].get(q, {}).get("raid") and not ns["board"].get(q, {}).get("realia")]

def safe_squares(ns, seat, rounds=2):
    sol = [s["sq"] for s in ns["SOLDIERS"].values() if s["side"] == "W"]
    return [q for q in free_squares(ns, seat) if all(ns["dist"](q, s) > rounds for s in sol)]

def warlord_objective(ns):
    """The Warlord's objective from the engine's raid record (warlord_got): one raided piece from
    each player in a realia-holding seat (not the Emperor); at eight players a palace raid, which
    the engine records under "palace", stands in for any one of them (RULINGS, the Warlord's objective).
    Returns (got {pid: code}, left [pid], wildcard allowed, palace raided or None, complete)."""
    targets = [ns["pid"](s) for s in ns["ACTIVE"] if s in ns["REALIA"]]
    wg = ns["warlord_got"]
    got = {p: t for p, t in wg.items() if p in targets}
    left = [p for p in targets if p not in got]
    wild = len(ns["ACTIVE"]) >= 8
    palace = wg.get("palace") if wild else None
    return got, left, wild, palace, (not left) or (bool(palace) and len(left) == 1)

def objective_text(ns):
    SH, R = ns["SHORT"], ns["RNAME"]
    got, left, wild, palace, done = warlord_objective(ns)
    out = "raid one piece from each player in a realia-holding seat, not the Emperor"
    if wild: out += " (at eight players one raid on a palace or the Marble Pagoda may stand in for any one player's piece)"
    out += ". Raided so far: " + (", ".join(f"{SH[p]}'s {R[t]}" for p, t in got.items()) or "nothing yet")
    if palace: out += f", and the {palace} (the palace wildcard)"
    out += ". Still to raid: " + (", ".join(SH[p] for p in left) or "nobody")
    if palace and len(left) > 1: out += f" (the palace stands in for one of them, so any {len(left)-1})"
    if done: out += ". **Complete:** you may change places with any player, the throne included"
    return out + "."

def palace_lines(ns, sol):
    """Unraided palace squares and each Warlord soldier's distance to them."""
    d = ns["dist"]; out = []
    for k in ns["PALACES"]:
        for q in ns["pw_at"].get(k, ()):
            if not ns["board"].get(q, {}).get("raid"):
                out.append(f"{k} {q}: " + ", ".join(f"{i} {d(q, sq)}" for i, sq in sol.items()))
    return out

def state_block(ns, player):
    SH, R = ns["SHORT"], ns["RNAME"]; p = pid_of(ns, player); seat = ns["sid"](p)
    g = ", ".join(f"{'**you %g**' % ns['grain'][q] if q == p else '%s %g' % (SH[q], ns['grain'][q])}" for q in ns["PLAYERS"])
    lines = [f"## The board now (after {'Setup' if not ns['CUR_ROUND'] else 'Year %d' % ns['CUR_ROUND']}'s steps so far)", "", f"- **Grain:** {g}. **Harvest Pile:** {ns['pile']:g}."]
    pieces = [f"{SH[v['owner']]}'s {R[v['realia']]} on {q}" for q, v in ns["board"].items() if v.get("realia")]
    lines.append("- **Realia on the board:** " + ("; ".join(pieces) or "none") + ".")
    st = [f"{SH[ns['pid'](s)]}: " + ", ".join(f"{n} {R[t]}" for t, n in v.items()) for s, v in ns["stock"].items() if v]
    if ns["pile_stock"]: st.append("the Harvest Pile (sold back): " + ", ".join(f"{n} {R[t]}" for t, n in ns["pile_stock"].items()))
    lines.append("- **Still beside the board (unsold):** " + ("; ".join(st) or "nothing") + ".")
    if has_warlord(ns):
        sol = [f"{i} on {s['sq']}" + ("" if s["side"] == "W" else f" ({SH[s['owner']]}'s)") for i, s in ns["SOLDIERS"].items()]
        lines.append("- **Soldiers:** " + (", ".join(sol) or "none yet") + ".")
        raided = sorted({ns["owner"](q) for q, v in ns["board"].items() if v.get("raid")} - {None})
        lines.append("- **Provinces raided so far** (their bought soldiers may move): " + (", ".join(map(str, raided)) or "none") + ".")
    left = sum(max(0, n - ns["built_count"](w)) * c for w, n, c in ns["owed"]())
    lines.append(f"- **Population** x{ns['MULT']:g}. **Public works still owed:** {left:g}.")
    if seat in ns["REALIA"]:
        need = [t for t in ns["need_for"](seat) if not ns["held"][p].get(t)]
        have = [R[t] for t, n in ns["held"][p].items() if n]
        lines.append(f"- **You hold:** {', '.join(have) or 'no realia'}. **Still needed:** {', '.join(R[t] for t in need) or 'nothing'}, and 20 grain.")
    return "\n".join(lines)

def dist_lines(ns):
    d = ns["dist"]; SH = ns["SHORT"]
    sol = {i: s["sq"] for i, s in ns["SOLDIERS"].items() if s["side"] == "W"}
    out = []
    for q, v in ns["board"].items():
        if v.get("realia"):
            out.append(f"{SH[v['owner']]}'s {ns['RNAME'][v['realia']]} ({q}): " + ", ".join(f"{i} {d(q, s)}" for i, s in sol.items()))
    if len(ns["ACTIVE"]) >= 8 and "palace" not in ns["warlord_got"]:
        out += [l + " (the palace wildcard)" for l in palace_lines(ns, sol)]
    return out

# ------------------------------------------------------------------ the board card
def board_card(ns, player):
    """A few lines at the top of every prompt, for this player only, always in the same layout.
    Every distance is the engine's dist() in rounds (one step a round)."""
    SH, R, d = ns["SHORT"], ns["RNAME"], ns["dist"]
    p = pid_of(ns, player); seat = ns["sid"](p)
    sol = {i: s["sq"] for i, s in ns["SOLDIERS"].items() if s["side"] == "W"}
    raided = lambda q: ns["board"].get(q, {}).get("raid")
    out = [f"## Your board card ({'Setup' if not ns['CUR_ROUND'] else 'Year %d' % ns['CUR_ROUND']}, from the engine)", ""]
    last = last_round(ns)
    if last:
        out.append(f"- **The short game:** {'Setup' if not ns['CUR_ROUND'] else 'Year %d' % ns['CUR_ROUND']} of {last}. The table stops after "
                   f"Year {last} and scores from where everyone sits (Note 19, §18): a lower-numbered province than you drew wins, "
                   "the same one holds, the Emperor wins by keeping the throne, and the larger grain surplus breaks ties.")
    if ns.get("CALLED"):
        out.append("- **A revolt has been called** and is not yet settled, so play waits: no step of the round and no seat change "
                   "until it stands or is dropped. Anyone may argue, persuade, promise or deal; the Emperor may answer it. It stands "
                   "only if the caller and two others still back it.")
    if ns.get("CHAOS"): out.append(chaos_line(ns, p, seat))
    elif ns.get("REVOLT_LINE"): out.append(REVOLT_LINE)
    have = ", ".join(f"{R[v['realia']]} {q}" for q, v in ns["board"].items() if v.get("realia") and v["owner"] == p)
    if seat == 8:
        out.append(f"- **Grain** {ns['grain'][p]:g}. **Army** {len(sol)} of {ns['ARMY']+1}. **Objective:** " + objective_text(ns))
        if have: out.append(f"- **Pieces on your desert:** {have}. (Only raided pieces count toward your objective; the line above names them. A piece won at auction counts nothing.)")
        pcs = [(q, v) for q, v in ns["board"].items() if v.get("realia") and v["owner"] != p]
        out.append("- **Your soldiers:** " + (", ".join(f"{i} {sq}" for i, sq in sol.items()) or "none") + ".")
        out.append("- **Each piece, rounds from each soldier:** " + ("; ".join(
            f"{SH[v['owner']]}'s {R[v['realia']]} {q}: " + ", ".join(f"{i} {d(q, sq)}" for i, sq in sol.items())
            for q, v in sorted(pcs, key=lambda kv: kv[1]["owner"])) or "no pieces on the board") + ".")
        pal = palace_lines(ns, sol)
        if pal:
            tag = (" A raid on one costs the Emperor 20; one such raid may stand in for a player's piece."
                   if len(ns["ACTIVE"]) >= 8 and "palace" not in ns["warlord_got"] else " A raid on one costs the Emperor 20.")
            out.append("- **Unraided palaces, rounds from each soldier:** " + "; ".join(pal) + "." + tag)
        return "\n".join(out)
    if seat in ns["REALIA"]:
        need = [R[t] for t in ns["need_for"](seat) if not ns["held"][p].get(t)]
        out.append(f"- **Grain** {ns['grain'][p]:g}. **Hold:** {have or 'nothing'}. **Still need:** {', '.join(need) or 'nothing'}, and 20 grain. "
                   f"**With the set you may replace:** {may_replace(ns, seat)}.")
    elif ns.get("CHAOS"):
        out.append(f"- **Deposed.** You still sit in Province 1, beside the sealed treasury ({ns['grain'][p]:g}): you can't spend it, "
                   "and you can't claim the throne. You may back one claimant, and promise anything. At the acclamation you take "
                   "the new Emperor's old seat and draw 60 from the Harvest Pile.")
    else:
        left = sum(max(0, n - ns["built_count"](w)) * c for w, n, c in ns["owed"]())
        out.append(f"- **Grain (the crown's reserve)** {ns['grain'][p]:g}. **Objective:** keep the throne. **Works still owed:** {left:g}.")
    mine = ns["squares_of"](seat)
    open_ = [q for q in mine if not raided(q)]
    if sol:
        pcs = [(q, v) for q, v in ns["board"].items() if v.get("realia") and v["owner"] == p]
        if pcs:
            out.append("- **Warlord soldiers to your pieces** (rounds): " + "; ".join(
                f"{R[v['realia']]} {q}: " + ", ".join(f"{i} {d(q, sq)}" for i, sq in sol.items()) for q, v in pcs) + ".")
        if seat == 1:
            pal = palace_lines(ns, sol)
            if pal:
                out.append("- **Warlord soldiers to your unraided palaces** (rounds; a raid costs you 20"
                           + ("; at eight players one such raid counts toward the Warlord's objective" if len(ns["ACTIVE"]) >= 8 else "")
                           + "): " + "; ".join(pal) + ".")
        if open_:
            near = {i: min(open_, key=lambda q: d(q, sq)) for i, sq in sol.items()}
            out.append("- **Nearest unraided square of yours:** " + ", ".join(f"{i} {d(near[i], sq)} ({near[i]})" for i, sq in sol.items()) + ".")
        # only squares a new piece may stand on (unraided, empty, not under a work), so the lists double as placement advice
        place = free_squares(ns, seat)
        far1 = [q for q in place if all(d(q, sq) > 1 for sq in sol.values())]
        far2 = [q for q in place if all(d(q, sq) > 2 for sq in sol.values())]
        out.append(f"- **Free squares for a new piece out of every Warlord soldier's reach this year:** {ranges(ns, far1)}. **This year and next:** {ranges(ns, far2)}.")
    elif 8 in ns["ACTIVE"]:
        out.append("- **Warlord soldiers:** none on the board yet.")
    if 8 in ns["ACTIVE"]:
        hit = any(raided(q) for q in mine)
        mine_sol = [f"{i} on {s['sq']}" for i, s in ns["SOLDIERS"].items() if s["side"] != "W" and s.get("owner") == p]
        out.append(f"- **Your province has {'been raided, so soldiers you buy can move' if hit else 'not been raided, so soldiers you buy cannot move yet'}.**"
                   + (f" Yours: {', '.join(mine_sol)}." if mine_sol else ""))
    land = land_line(ns, seat)
    if land: out.append(land)
    return "\n".join(out)

# Only a game whose game.py sets REVOLT_LINE = True puts this on every card (the Dark Ages, from 2026-10-28).
REVOLT_LINE = ("- **Revolt** (§16): at any step, any player may call a revolt by naming a cause, if two others agree it exists. "
               "The causes: the Emperor is unjust; taxes are consistently excessive; the reserve is too low; the works have been "
               "delayed too long; the Emperor can't control the Warlord; the Emperor won't subsidise new land; any player is in debt. "
               "The Emperor may answer it (pay, cut the tax, promise anything), and it stands only if the caller and two others still "
               "back it. Then comes Chaos: no tax, salaries, public works or new land until a new Emperor is acclaimed. "
               "Under Chaos no set can take the throne: it passes only by acclamation, counted on grain in hand, soldiers "
               "on the board and friends.")

def chaos_line(ns, p, seat):
    """Under Chaos (§16, N17, RULINGS: the sealed treasury, counting the acclamation), on every card."""
    e = ns["pid"](1)
    line = ("- **Chaos** (§16): there is no Emperor. Until one is acclaimed there's no tax, no salaries, no public works and "
            "no new land; the harvest, the rent, the auctions and the Warlord carry on. "
            f"The treasury in Province 1 is sealed ({ns['grain'][e]:g}): nobody may spend it, Province 1's harvest, raids and "
            "disasters still run through it, and the acclaimed Emperor inherits it, debt and all. No seat change takes the throne. "
            "Anyone but the deposed Emperor may claim it, and the claims are counted on grain in hand, soldiers on the board "
            "and friends (the players backing a claim; nobody is their own friend). Lead one count with no rival leading another, "
            "or lead more counts than anyone, and you're acclaimed; otherwise Chaos goes on.")
    if seat != 1:
        n = sum(1 for o in ns["SOLDIERS"].values() if o["owner"] == p)
        line += f" **If you claim:** grain {ns['grain'][p]:g}, soldiers {n}."
    return line

def may_replace(ns, seat):
    """Who a complete set lets this seat replace (§11), as the engine's swap() checks it."""
    SH, A = ns["SHORT"], ns["ACTIVE"]
    upper_empty = not set(A) & {2, 3, 4}
    if (seat in (2, 3, 4) or (seat == 5 and upper_empty)) and ns.get("CHAOS"):
        ok = [s for s in A if s not in (seat, 8, 1)]
        head = "any other player, but not the throne (under Chaos it passes only by acclamation)"
    elif seat in (2, 3, 4) or (seat == 5 and upper_empty):
        ok = [s for s in A if s != seat and s != 8]
        head = "the Emperor (the throne) or any other player"
    else:
        ok = [s for s in A if s in (2, 3, 4, 5, 6, 7) and s != seat]
        head = "the Official, Gentry, Scholar or another peasant, not the Emperor (a peasant climbs to the upper class first)"
    return head + ": " + ", ".join(f"{SH[ns['pid'](s)]} ({ns['ROLE'][s]})" for s in ok)

def last_round(ns):
    """The agreed last round of a short game (Note 19), or None. Only a game whose game.py sets
    LAST_ROUND = <n> has one; every other game runs to §18's ending, unchanged."""
    return ns.get("LAST_ROUND")

def auctions_begun(ns):
    """True once this year's auctions have started: the public-works step (land included) is over."""
    start = ns["ROUNDS"][-1]["start"] if ns["ROUNDS"] else 0
    return any(e["k"] == "lot" for e in ns["ENTRIES"][start:])

def works_done(ns):
    """True once this year's one project (N13) is built, or its works step is over."""
    return ns.get("LAST_BUILD") == ns["CUR_ROUND"] or auctions_begun(ns)

def endgame_note(ns):
    """Near the end, new land may never pay back: a square pays from next year's harvest, and the game
    ends the moment the last owed work is built (§18), or after the agreed last round (Note 19). From the
    engine's owed() and built_count(); the Great Wall or the Grand Canal, any number of sections, is one
    project (N13). None until it matters."""
    last, r = last_round(ns), ns["CUR_ROUND"] or 0
    if last and r >= last:
        return (f"**This is the last round:** the table agreed to stop after Year {last} and score from where everyone sits "
                "(Note 19, §18). A square of new land pays from next year's harvest, so a square bought now never pays back. "
                "Grain in hand breaks ties at the end.")
    left = [(w, (n - ns["built_count"](w)) * c) for w, n, c in ns["owed"]() if ns["built_count"](w) < n]
    years = len(left) + works_done(ns)            # one project a year; this year's counts only if still to come
    if last and r == last - 1 and years != 1:     # one work left can end it sooner: that note says so
        return (f"**One round after this one:** the table stops after Year {last} (Note 19). A square of new land bought now "
                f"pays back once at best, from Year {last}'s harvest. Grain in hand breaks ties at the end.")
    if years > 2 or not left: return None         # nothing owed: the game is over
    what = " and ".join(f"the {w} ({c:g})" for w, c in left)
    if years == 1:
        return (f"**The game can end this year:** {what} is still owed, and the game ends the moment the last work "
                "is built, before the auction (§18). A square of new land pays from next year's harvest, so a square bought now "
                "may never pay back. Grain in hand breaks ties at the end.")
    if len(left) == 1:
        done = ("this year's project is already built" if ns.get("LAST_BUILD") == r else "this year's works step is over")
        return (f"**The game can end next year:** {what} is still owed, and {done} (one project a year, §12), "
                "so it can go up next year at the earliest, and the game ends the moment it does "
                "(§18). A square of new land bought now pays back once if the game ends next year, and 20 more for every year "
                "it runs on.")
    return (f"**The game can end next year:** two projects are still owed, {what}, one a year (§12), and the game ends the "
            "moment the last is built (§18). A square of new land bought now pays back once if the game ends next year, "
            "and 20 more for every year it runs on.")

def land_open(ns, seat):
    """None if the seat may buy new land now, else why not (§13, engine buy_land)."""
    if seat not in ns["LAND_WHERE"] or seat not in ns["ACTIVE"]: return "no new land for this seat"
    if ns.get("CHAOS"): return "no new land under Chaos: there's no Emperor to share the cost"
    if ns["MULT"] < 2: return f"the population hasn't doubled (x{ns['MULT']:g})"
    if seat in (2, 3) and ns["pw"]["wall"][seat] < 4:
        return f"your strip opens once all four Wall links above you stand ({ns['pw']['wall'][seat]} of 4 built)"
    return None

def land_frontier(ns, seat):
    """The undeveloped squares this seat may buy next: the ground its booklet names, touching the
    province or its new land (more open up as squares are bought). From the engine's tables."""
    ok = ns["LAND_WHERE"][seat]
    if seat == 1 and ns["pw"]["wall"][1] < 4: ok = ok.replace("n", "")
    mine = ns["squares_of"](seat)
    return [ns["sqname"](r, c) for r in range(ns["ROWS"]) for c in range(ns["COLS"])
            if ns["GRID"][r][c] in ok and ns["sqname"](r, c) not in ns["land"]
            and not ns["board"].get(ns["sqname"](r, c), {}).get("realia")   # the Warlord's pieces stand on his desert
            and any(ns["dist"](ns["sqname"](r, c), m) == 1 for m in mine)]

def land_line(ns, seat):
    """New land (Section 13): what a square earns, and how many this province needs to break
    even in an average year now and after the next population card. From the engine's tables."""
    if seat not in ns["LAND_WHERE"] or seat not in ns["ACTIVE"]: return None
    m, pc = ns["MULT"], ns["pop_cards"]
    steps_ = []
    if pc[2] < 2 and m * 2 <= 6: steps_.append(m * 2)
    if pc[1.5] < 1: steps_.append(m * 1.5)
    nxt = max(steps_) if steps_ else None
    extra = ns["bonus"][seat] + ns["pending_bonus"].get(seat, 0)
    avg = lambda mult: ns["HARV"][seat]["avg"] + extra - ns["CONS"][seat] * mult
    sq = lambda mult: max(0, -(-(-avg(mult)) // 20)) if avg(mult) < 0 else 0
    n = lambda k: f"{k:g} square" + ("" if k == 1 else "s")
    ahead = f" If the next population card comes (x{nxt:g}), you'd need {n(sq(nxt))} more than you have." if nxt else ""
    shut = land_open(ns, seat)
    end = endgame_note(ns)
    next_year = bool(end) and end.startswith("**The game can end next year")   # two projects: the break-even line stays
    if m >= 2 and not shut and end and not next_year:
        return "- " + end + (f" Your average-year income now: {avg(m):+g}." if seat != 1 else
            " As Emperor, keep enough in the reserve to build what's still owed: a crown in debt can't pay a share of a work (N7).")
    if m >= 2 and not shut:
        return (f"- **New land is open** (Section 13): 20 a square, and the Emperor may pay any part of it. Each adds 20 "
                f"to every harvest from next year, so it pays for itself in one year. Your average-year income now: {avg(m):+g}; "
                f"to break even you'd need {n(sq(m))} more than you have.{ahead} Buy ahead: in debt you can't pay your share."
                + (" As Emperor you may pay any part of anyone's squares, even all of it: every square you fund raises "
                   "that province's taxable income and what it can put toward the works." if seat == 1 else "")
                + (" " + end if next_year else ""))
    if m >= 2:
        return (f"- **New land is shut to you for now:** {shut}. Your average-year income now: {avg(m):+g}; "
                f"to break even you'd need {n(sq(m))}.{ahead}")
    wall = (" Your only new land is the strip below the Wall, which also needs all four links above you built "
            f"({ns['pw']['wall'][seat]} of 4 now)." if seat in (2, 3) else "")
    return (f"- **New land opens when the population doubles** (now x{m:g}). Then each square costs 20 and adds 20 a year. "
            f"At x2 you'd need {n(sq(2))} to break even in an average year, and more after the next card; save for them.{wall}")

# ------------------------------------------------------------------ the menus
def lot_parts(ns, lot):
    sell, typ = lot.split(":"); sell = int(sell)
    src = ns["pile_stock"] if sell == 0 else ns["stock"].get(sell, {})
    seller = "the Harvest Pile" if sell == 0 else ns["SHORT"][ns["pid"](sell)]
    return sell, typ, src.get(typ, 0), seller

def wants_of(ns, sell, typ):
    SH = ns["SHORT"]
    return [SH[ns["pid"](s)] for s in ns["ACTIVE"] if s in ns["REALIA"] and s != sell
            and typ in ns["need_for"](s) and not ns["held"][ns["pid"](s)].get(typ)]

def where_text(ns, seat):
    if seat == 8: return "a square of your desert (name one)"
    if not has_warlord(ns): return f"a square of your province. Free squares: {ranges(ns, free_squares(ns, seat))}"
    return f"a square of your province. Out of every Warlord soldier's reach for two rounds: {ranges(ns, safe_squares(ns, seat))}"

def menu_auction(ns, player, lot, minimum):
    R = ns["RNAME"]; sell, typ, left, seller = lot_parts(ns, lot)
    seat = seat_of(ns, player)
    return f"""## Your move: {seller}'s {R[typ]}, minimum {minimum:g}

Who still needs one: {', '.join(wants_of(ns, sell, typ)) or 'nobody'}. {seller} has {left} in stock (this is {'the last' if left == 1 else 'one of ' + str(left)}).

You reply **once** for this lot; the Storyteller runs it as a rising auction from everyone's limits and narrates the climb.

- **pass** — most lots draw one or two serious bidders; passing is normal.
- **ceiling:** the most you'll pay (up to your grain).
- **keep from:** optional, `<name> up to <n>`: a higher limit you'd pay only to stop that player getting it.
- **square if you win:** {where_text(ns, seat)}.
- **if I drop out:** one short line you'd say as you drop out (used only if you do).

{ECONOMICS}"""

def fmt_auction():
    return "move: pass | ceiling <n>; keep from <name> up to <n> (optional); square <square>\n"

def menu_auctions(ns, player, lots, floor=()):
    """Every lot of the year in one prompt: a ceiling (and an optional keep-from) for each.
    floor: lots that went unsold last round, which must open at 2 this time (Manish, Year 8)."""
    R = ns["RNAME"]; p = pid_of(ns, player); seat = ns["sid"](p)
    assert seat != 1, "the Emperor doesn't bid (§10)"
    need = [R[t] for t in ns["need_for"](seat) if not ns["held"][p].get(t)] if seat in ns["REALIA"] else []
    out = ["## Your move: this year's auctions, all at once", "",
           f"There are {len(lots)} lots this year, sold in this order. Give your limits for every lot now; the Storyteller "
           "settles them one after another as rising auctions and narrates each climb. If you win a lot, you'll be asked "
           "where to place it.", ""]
    mine = []
    for i, lot in enumerate(lots, 1):
        sell, typ, left, seller = lot_parts(ns, lot)
        if sell and ns["pid"](sell) == p:
            if lot in floor:
                out.append(f"{i}. **`{lot}` your own {R[typ]}** ({left} in stock). It went unsold last round, so it must open at 2 this time (the house rule). You can't bid on it.")
                continue
            mine.append(lot)
            out.append(f"{i}. **`{lot}` your own {R[typ]}** ({left} in stock). You can't bid on it. Set its minimum: 2, or more if you like. If nobody meets it, it must go up again next round at 2.")
            continue
        out.append(f"{i}. **`{lot}` {seller}'s {R[typ]}** ({left} in stock). Still needed by: {', '.join(wants_of(ns, sell, typ)) or 'nobody'}. "
                   + ("It went unsold last round, so it opens at 2." if lot in floor else
                      f"Minimum 2 unless {seller} sets it higher{' (the pile sets none)' if sell == 0 else ''}; a ceiling under the minimum counts as a pass."))
    out += ["", f"**You still need:** {', '.join(need) or 'nothing for your own set'}. **Your grain:** {ns['grain'][p]:g}. "
            "**Everyone's:** " + ", ".join(f"{ns['SHORT'][q]} {ns['grain'][q]:g}" for q in ns["PLAYERS"]) + ".",
            "",
            "- **pass** on a lot, or a **ceiling**: the most you'll pay for it.",
            "- **keep from:** optional, `<name> up to <n>`: a higher limit you'd pay only to stop that player getting it.",
            "- Your limits are settled lot by lot, in order. If you've already won an earlier lot, a later limit above the grain you have left is cut to it.",
            "- Most lots draw one or two serious bidders; passing is normal.",
            "", ECONOMICS]
    return "\n".join(out), mine

def fmt_auctions(ns, player, lots, mine):
    lines = ["move:"]
    for lot in lots:
        lines.append(f"  {lot}: " + ("minimum <n>" if lot in mine else "pass | ceiling <n>; keep from <name> up to <n> (optional)"))
    return "\n".join(lines) + "\n"

def menu_place(ns, player, lot, price):
    """lot and price may be comma lists ('3:LD,5:DJ' and '7,8') for a buyer who won several lots."""
    R = ns["RNAME"]; lots = lot.split(","); prices = (price or "").split(",")
    won = []
    for i, l in enumerate(lots):
        sell, typ, left, seller = lot_parts(ns, l)
        pr = prices[i] if i < len(prices) and prices[i] else None
        won.append(f"{seller}'s {R[typ]}" + (f" for {pr}" if pr else ""))
    one = len(lots) == 1
    return f"""## You won {' and '.join(won)}

Place {'it' if one else 'each'} now (Note 10), {'on' if one else 'each on its own'} {where_text(ns, seat_of(ns, player))}. A piece can't go {'on a raided square or ' if has_warlord(ns) else ''}under a work."""

def menu_march(ns):
    out = ["## Your move: the march", "", "Each soldier steps one square (diagonals allowed) or stands still. raid=5 (10 in Province 1) takes 5 from that province's player, or the piece standing there instead; '-' raids nothing. Tolls are 5 each, paid to the province."]
    for i, s in ns["SOLDIERS"].items():
        if s["side"] != "W": continue
        out += ["", f"**{i} on {s['sq']}:**"] + [f"- {l}" for l in steps(ns, i)] + ["- stay"]
    out += ["", "**Taking a piece:** a step marked `piece=` raids a square with realia on it. You take the piece or the 5; "
            "to take the piece, add `take: <soldier> <square of your desert>`, where it will stand (an empty desert square)."]
    desert = [q for q in ns["squares"](8) if q not in ns["land"] and not ns["board"].get(q, {}).get("realia")]
    for q, v in ns["board"].items():
        # only soldiers whose step list offers this square as a raid (no diagonal step onto a guard, no raided square)
        near = [i for i, s in ns["SOLDIERS"].items() if s["side"] == "W"
                and any(l.startswith(q + " ") and "piece=" in l and "raid=-" not in l for l in steps(ns, i))]
        if v.get("realia") and v["owner"] != ns["pid"](8) and near:
            best = sorted(desert, key=lambda d: (ns["dist"](d, q), d))[:4]
            out.append(f"- {ns['SHORT'][v['owner']]}'s {ns['RNAME'][v['realia']]} on {q} ({', '.join(near)} can step there): "
                       f"the nearest empty desert squares are {', '.join(best)}.")
    out += ["", "**Distances (rounds) from each piece to your soldiers:**"] + [f"- {l}" for l in dist_lines(ns)]
    n = sum(1 for s in ns["SOLDIERS"].values() if s["side"] == "W")
    if n < ns["ARMY"] + 1:
        out += ["", f"**Then, optionally, hire** one soldier for 20 on a square of your desert. Army {n} of {ns['ARMY']+1}."]
    if ns["CUR_ROUND"] in ns["NORAID"]:
        out += ["", f"**No raids this round on provinces {sorted(ns['NORAID'][ns['CUR_ROUND']])}** (your disaster); soldiers may still walk."]
    return "\n".join(out)

def fmt_march(ns):
    ws = [i for i, s in ns["SOLDIERS"].items() if s["side"] == "W"]
    return "move: " + "; ".join(f"{i} <square or stay>" for i in ws) + "; take: <none, or soldier and desert square>; hire: <no, or a square>\n"

# Who pays for each work (the Emperor's booklet; §12): the crown outright, or a split negotiated with the province.
PAYS = {"Summer Palace": "you", "Winter Palace": "you", "Marble Pagoda": "you", "Province 7 Reservoir": "you",
        "Province 2 Irrigation System": "negotiate with Province 2", "Province 3 Reservoir": "negotiate with Province 3"}

def works_lines(ns):
    """Every work owed at this table, what's built, the next piece, who pays and what must stand first."""
    pw, A = ns["pw"], ns["ACTIVE"]; out = []
    sp, wp = pw["Summer Palace"], pw["Winter Palace"]
    for name, n, cost in ns["owed"]():
        b = ns["built_count"](name)
        if name == "Great Wall":
            for s in (1, 2, 3):
                if s not in A: continue
                k = pw["wall"][s]
                pay = "you" if s == 1 else f"negotiate with Province {s}"
                pre = "" if sp else "; needs the Summer Palace first"
                out.append(f"- Great Wall above Province {s}: {k} of 4 links built, 40 each ({pay}{pre}). All four open that province's strip for new land.")
            continue
        if name == "Grand Canal":
            for s in (1, 4, 5, 6):
                if s not in A: continue
                k = pw["canal"][s]
                pay = "you" if s in (1, 5, 6) else f"negotiate with Province {s}"
                pre = "" if (sp if s == 1 else wp) else f"; needs the {'Summer' if s == 1 else 'Winter'} Palace first"
                out.append(f"- Grand Canal in Province {s}: {k} of 2 sections built, 40 each, +10 harvest each ({pay}{pre}).")
            continue
        state = "built" if b >= n else "not built"
        extra = {"Marble Pagoda": "; built in a year when nothing else is", "Province 2 Irrigation System": ", +10 harvest",
                 "Province 3 Reservoir": ", +20 harvest", "Province 7 Reservoir": ", +20 harvest"}.get(name, "")
        out.append(f"- {name}: {state}, {cost:g} ({PAYS.get(name, 'you')}{extra}).")
    return out

def menu_crown(ns):
    """The Emperor's year: the tax rate, the one project, the salaries, and new land."""
    SH = ns["SHORT"]; A = ns["ACTIVE"]; inc = ns["CUR_INC"]; e = ns["pid"](1)
    assert not ns.get("CHAOS"), "no crown's year under Chaos: there is no Emperor"
    out = ["## Your move: the crown's year", ""]
    if inc:
        rows = [f"{SH[ns['pid'](s)]} {inc[s]:+g}" for s in A if s != 1]
        out.append("**Taxable income this year** (harvest income only; none is owed on a negative income): " + ", ".join(rows) + ".")
        def take(r): return sum(ns["pay_down"](max(0, inc[s]) * r) for s in A if s != 1)
        def war(r): return f" ({SH[ns['pid'](8)]} {ns['pay_down'](max(0, inc[8]) * r):g})" if has_warlord(ns) else ""
        out.append("**The tax at each rate**" + (", with the Warlord's part, which the Warlord may refuse to pay"
                                                  if has_warlord(ns) else "") + ": "
                   + ", ".join(f"{r}% {take(r/100):g}{war(r/100)}" for r in (20, 30, 40, 50, 60)) + ".")
    else:
        out.append("**Taxable income:** not paid out yet this year.")
    left = sum(max(0, n - ns["built_count"](w)) * c for w, n, c in ns["owed"]())
    out += ["", f"**Your reserve:** {ns['grain'][e]:g}. **Works still owed:** {left:g}. **One project a year** (any number of sections of one work counts as one):"]
    out += works_lines(ns)
    sal = [f"the {ns['ROLE'][s]} ({SH[ns['pid'](s)]})" for s in (2, 4) if s in A]
    out += ["", "**Decide:**", "- **tax:** one rate for everyone, 10% to 90%.",
            "- **build:** one project, and the split if a province shares it (they must agree; the Storyteller asks them)."]
    if sal: out.append(f"- **salaries**, paid at the end of the year: at least 5 each to {' and '.join(sal)}.")
    if ns["MULT"] >= 2:
        out.append("- **new land:** the share you'll pay of other provinces' squares this year (you must pay some part of each, "
                   "and may pay all), and any squares for Province 1. A rich Emperor does well to pay a large share: every square raises "
                   "that province's taxable income for good. Refusing to subsidise new land is a cause for revolt (§16).")
        if not land_open(ns, 1):
            out.append(f"  **Squares Province 1 can buy now** (each must touch the province or land it has already bought): {ranges(ns, land_frontier(ns, 1))}.")
        end = endgame_note(ns)
        if end: out.append("  " + end + " Keep enough in the reserve to build what's still owed: a crown in debt can't pay a share of a work (N7).")
    return "\n".join(out)

def fmt_crown(ns):
    s = "move: tax <n>%; build <project> (split: <who pays what>)"
    if 2 in ns["ACTIVE"] or 4 in ns["ACTIVE"]: s += "; salaries " + ", ".join(f"{ns['ROLE'][k]} <n>" for k in (2, 4) if k in ns["ACTIVE"])
    if ns["MULT"] >= 2: s += "; land: <your share per square, and any squares for Province 1>"
    return s + "\n"

def menu_rent(ns):
    """The Gentry pays out the harvest, then asks the rent (or doesn't)."""
    SH = ns["SHORT"]; A = ns["ACTIVE"]; inc = ns["CUR_INC"]
    peas = [SH[ns["pid"](s)] for s in (5, 6, 7) if s in A]
    out = ["## Your move: the harvest and the rent"]
    if inc and ns["CUR_ROUND"] and ns["CUR_ROUND"] > 1:
        out += ["", "**You pay out the harvest** from the pile (the engine's figures; negative incomes are paid into it): "
                + ", ".join(f"{SH[ns['pid'](s)]} {inc[s]:+g}" for s in A) + "."]
    out += ["", f"**Rent.** You may ask each peasant ({', '.join(peas) or 'none at the table'}) for a rental of at least 5 this year. "
            "If you don't ask, it isn't paid. Raising it above 5 is a negotiation with the peasants, at any time. "
            "Rent isn't taxable income.",
            "", "Peasants' grain now: " + ", ".join(f"{SH[ns['pid'](s)]} {ns['grain'][ns['pid'](s)]:g}" for s in (5, 6, 7) if s in A) + "."]
    return "\n".join(out)

def salary_line(ns, player, seat, job):
    """The holder of the seat is owed its salary; an appointee doing the job isn't (rules-digest step 9)."""
    if seat_of(ns, player) == seat: return "The Emperor owes you a salary of at least 5 at the end of the year."
    return (f"You do this as the Emperor's appointee, not as the {job}: you're paid only what the Emperor chooses to pay "
            "you, at the end of the year.")

def parse_claims(ns, claims):
    """--claims "Rich:Silke,Paddy;Rob": each claimant by short name, then their backers. -> {seat: [seats]}."""
    out = {}
    for part in filter(None, (claims or "").split(";")):
        who, _, back = part.partition(":")
        out[seat_of(ns, who.strip())] = [seat_of(ns, b.strip()) for b in back.split(",") if b.strip()]
    return out

def menu_acclaim(ns, player, claims):
    """Under Chaos: claim the throne, back a claimant, or stand aside, with the count as the claims stand now."""
    assert ns.get("CHAOS"), "an acclamation is counted only under Chaos"
    SH = ns["SHORT"]; seat = seat_of(ns, player); cl = parse_claims(ns, claims)
    out = ["## Your move: the acclamation", ""]
    if cl:
        counts, lead, win = ns["acclaim_counts"](cl)
        for s, c in counts.items():
            out.append(f"- **{SH[ns['pid'](s)]}** claims: grain {c[0]:g}, soldiers {c[1]}, friends {c[2]}"
                       + (" (" + ", ".join(SH[ns['pid'](b)] for b in cl[s]) + ")" if cl[s] else "") + ".")
        out.append("- **Leading now:** " + "; ".join(f"{k} " + (SH[ns['pid'](v)] if v else "nobody")
                                                     for k, v in lead.items()) + ". "
                   + (f"As the claims stand, {SH[ns['pid'](win)]} would be acclaimed." if win else "As the claims stand, nobody would be acclaimed."))
    else:
        out.append("- **Nobody has claimed the throne yet.**")
    out.append("A tie in a count leads nobody.")
    out.append("")
    if seat == 1:
        out.append("You're the deposed Emperor: you can't claim, but you may back one claimant, or stand aside.")
    else:
        out.append("Claim the throne yourself, back one claimant (your backing counts as one friend for them), or stand aside. "
                   "A claimant can't back anyone. The claims can be counted again whenever they change.")
    return "\n".join(out)

def menu_collect(ns, rate, player):
    """The Official collects the tax the Emperor declared and delivers it to the crown."""
    assert not ns.get("CHAOS"), "no tax under Chaos"
    SH = ns["SHORT"]; A = ns["ACTIVE"]; inc = ns["CUR_INC"]; r = float(rate) / 100
    rows = [f"{SH[ns['pid'](s)]} {ns['pay_down'](max(0, inc[s]) * r):g}" for s in A if s != 1] if inc else []
    tot = sum(ns["pay_down"](max(0, inc[s]) * r) for s in A if s != 1) if inc else 0
    out = ["## Your move: collecting the tax", "",
           f"The Emperor has declared **{rate}%**. Owed on this year's harvest income, rounded down to the half million: "
           + (", ".join(rows) + f"; {tot:g} in all" if rows else "nothing paid out yet") + "."
           + (" The Warlord may refuse to pay their part." if has_warlord(ns) else "")
           + " You collect it and deliver it to the crown, and you make certain nobody cheats.",
           "", salary_line(ns, player, 2, "Official")]
    return "\n".join(out)

def menu_iching(ns, player):
    """The Scholar turns the year's card (already applied by the engine) and keeps the counter."""
    rd = ns["ROUNDS"][-1]; prev = ns["ROUNDS"][-2]["mult"] if len(ns["ROUNDS"]) > 1 else 1
    m = ns["MULT"]
    pop = (f"The population changes: x{prev:g} to **x{m:g}**, so the counter reads **{100*m:g} million**."
           if m != prev else f"The population stays at x{m:g}: the counter reads {100*m:g} million.")
    return f"""## Your move: the I Ching

You turn this year's card and read it aloud to the table:

> {rd['card'] or 'No card this year.'}

{pop} Announce the figure and the multiple, so everyone reads the right row of their income table. If the card names provinces that play a personal disaster, each plays the next one in their booklet.

{salary_line(ns, player, 4, "Scholar")}"""

def offer_line(offer):
    """What the Emperor said in the crown's year they'd pay toward each square (--offer, the Storyteller's words)."""
    return f" **The crown's offer this year:** {offer}." if offer else ""

def menu_land(ns, player, offer=None):
    SH = ns["SHORT"]; p = pid_of(ns, player); seat = ns["sid"](p)
    shut = land_open(ns, seat)
    if shut: return f"## New land\n\nNot this year: {shut}."
    if ns["grain"][p] < 0: return "## New land\n\nYou're in debt, so you can't pay a share this year (N7)."
    front = land_frontier(ns, seat)
    share = ("You pay; you may buy any number of squares." if seat == 1 else
             "The cost is shared with the Emperor, who must pay some part of every square and may pay all of it; "
             "say what you'll pay and what you're asking the crown for." + offer_line(offer))
    return f"""## Your move: new land (Section 13)

New land is open to you this year, in the public works step. Each square costs 20 to the Harvest Pile and adds 20 to your harvest every year from next year, so it pays for itself in a single year. {share}

**Squares you can buy now** (each must touch your province or land you've already bought, so buying opens the next ring): {ranges(ns, front)}.
{'New land can be raided like any other square of your province.' + chr(10) if has_warlord(ns) else ''}{chr(10) + endgame_note(ns) + chr(10) if endgame_note(ns) else ''}
Your board card above gives your own numbers. Buying nothing is also a choice."""

def fmt_land(ns, player):
    if land_open(ns, seat_of(ns, player)) or ns["grain"][pid_of(ns, player)] < 0: return "move: none\n"
    return "move: none | land <squares>; I pay <n>, asking the crown for <n>\n"

# ------------------------------------------------------------------ prompts
def launch_text(player, ns):
    p = pid_of(ns, player); seat = ns["sid"](p); pron = CAST[p][0]
    job = (f" {player} also has a table job: the {ns['ROLE'][seat]} {JOB[seat]}." if seat in JOB else "")
    return f"""You're playing {full(ns, p)} at a recorded game night. The game is Dynasty, a 1969 board game about ancient China. {player} is the {ns['ROLE'][seat]}. {CAST[p][1]} {player} is "{pron}".{job}

This is a performance, so stay in {player}'s voice. Use no tools and read no files; just write your reply. I'm the Storyteller: I'll message you again each time it's your turn, with what's been said at the table, so keep track of the game as it goes.

{table_text(ns)}

{WHISPER}
""" + continuity(ns, player) + direction(player)

def direction(player):
    """For a launch: the actor's brief from the game's direction.md, if it has one (the Dark Ages, from
    2026-10-28, on Manish's word). The shared story, then this player's own part. Never shown to the table."""
    if not os.path.exists("direction.md"): return ""
    txt = open("direction.md", encoding="utf-8").read()
    parts = {h.split("\n", 1)[0].strip(): h.split("\n", 1)[1].strip() for h in txt.split("\n## ")[1:] if "\n" in h}
    out = [parts.get("The story", "")]
    if parts.get(player): out.append(f"**Your part, {player}:** " + parts[player])
    out.append(parts.get("The rule", ""))
    return "\n## The story tonight (for you as the actor, never for the table)\n\n" + "\n\n".join(x for x in out if x) + "\n"

def continuity(ns, player):
    """For a launch: the character's ledger entry and their diary so far, if any."""
    p = pid_of(ns, player); out = []
    if os.path.exists("ledger.md"):
        led = open("ledger.md", encoding="utf-8").read()
        head = next((h for h in led.split("\n## ")[1:] if h.startswith(ns["NAMES"][p])), None)
        if head:
            body = head.split("\n", 1)[1].strip()
            if body: out.append(f"## Where {player} stands (the game's record so far)\n\n{body}")
    d = os.path.join("diaries", player.lower() + ".md")
    if os.path.exists(d):
        body = open(d, encoding="utf-8").read().split("\n", 1)[-1].strip()
        if body: out.append(f"## {player}'s diary so far, in {'her' if CAST[p][0] == 'she' else 'his'} own words\n\n{body}")
    return ("\n" + "\n\n".join(out) + "\n") if out else ""

def land_reminder(ns, player, offer=None):
    """From the first doubling, new land can ride along in a free menu of an eligible seat (--land)."""
    seat = seat_of(ns, player)
    if (seat in ns["LAND_WHERE"] and not land_open(ns, seat) and ns["grain"][pid_of(ns, player)] >= 0 and not ns["all_built"]()
            and not auctions_begun(ns)):
        return ("**New land is open to you** this year (your card gives your numbers): squares you can buy now: "
                f"{ranges(ns, land_frontier(ns, seat))}. Add `land <squares>; I pay <n>, asking the crown for <n>` to your move if you want any."
                + (offer_line(offer) if seat != 1 else "") + (" " + endgame_note(ns) if endgame_note(ns) else ""))
    return None

def prompt(n, player, kind, lot=None, minimum=None, menu=None, dry=False, lots=None, rate=None, price=None, short=False, floor=None, years=None,
           offer=None, land=False, claims=None):
    ns = run_ns(); pid_of(ns, player)
    parts = []
    # "launch" carries a --menu file; "launch:<kind>" (launch:crown, launch:auctions, ...) carries that kind's menu
    launch = kind.split(":")[0] == "launch"
    if launch:
        parts.append(launch_text(player, ns)); kind = kind.split(":")[1] if ":" in kind else "launch"
    # --short: leave out the long state block (the card stays: it's short and from the engine).
    # place is a quick follow-up to a prompt the player just had, so it leaves out the card too.
    if kind not in ("place", "diary"): parts.append(board_card(ns, player))
    short = short or kind in ("place", "diary")
    heard_ = since(player)
    if heard_: parts.append("## At the table since your last turn\n\n" + "\n\n".join(heard_))
    if not short: parts.append(state_block(ns, player))
    drop = "\nif I drop out: <one short line, used for any lot you drop out of>"
    if kind == "auction":
        parts.append(menu_auction(ns, player, lot, minimum)); fmt = fmt_auction() + FORMAT_TAIL + "\nif I drop out: <one short line>"
    elif kind == "auctions":
        lots = lots.split(","); m, mine = menu_auctions(ns, player, lots, (floor or "").split(","))
        parts.append(m); fmt = fmt_auctions(ns, player, lots, mine) + FORMAT_TAIL + drop
    elif kind == "place":
        parts.append(menu_place(ns, player, lot, price))
        fmt = "move: " + "; ".join(f"{l} <square>" for l in lot.split(",")) + "\n" + FORMAT_TAIL
    elif kind == "march":
        parts.append(menu_march(ns)); fmt = fmt_march(ns) + FORMAT_TAIL
    elif kind == "crown":
        parts.append(menu_crown(ns)); fmt = fmt_crown(ns) + FORMAT_TAIL
    elif kind == "rent":
        parts.append(menu_rent(ns)); fmt = "move: rent <n> from each peasant | rent <name> <n>, ... | no rent\n" + FORMAT_TAIL
    elif kind == "collect":
        parts.append(menu_collect(ns, rate, player)); fmt = "move: collect as declared | <anything else you do>\n" + FORMAT_TAIL
    elif kind == "iching":
        parts.append(menu_iching(ns, player)); fmt = "move: read\n" + FORMAT_TAIL
    elif kind == "land":
        parts.append(menu_land(ns, player, offer)); fmt = fmt_land(ns, player) + FORMAT_TAIL
    elif kind == "acclaim":
        parts.append(menu_acclaim(ns, player, claims)); fmt = "move: claim the throne | back <claimant> | stand aside\n" + FORMAT_TAIL
    elif kind == "diary":     # the chapter's close: the entry only, no move, say or aside
        full_ = ns["NAMES"][pid_of(ns, player)]
        parts.append(f"## {player}'s diary\n\nThe evening's chapter is over. Write {full_}'s diary entry for "
                     f"{years or 'these years'}: a few sentences in {player}'s own voice, about what happened, what it cost, "
                     "and what comes next. Nobody at the table reads it.")
        fmt = "diary: <the entry, a few sentences>\n"
    else:
        parts.append(open(menu, encoding="utf-8").read().strip()); fmt = "move: <your choice>\n" + FORMAT_TAIL
        rem = land_reminder(ns, player, offer) if kind == "free" and land else None
        if rem: parts.append(rem)
    if not launch and kind != "diary": parts.append(WHISPER)
    parts.append("## Your reply\n\nReply in exactly this format:\n\n```\n" + fmt.format(short=player) + "\n```")
    text = "\n\n".join(parts) + "\n"
    if dry: print(text); return
    folder = f"log/year{max(1, ns['CUR_ROUND'] or 0)}"; os.makedirs(folder, exist_ok=True)
    path = f"{folder}/{n}-{player.lower()}-prompt.md"
    assert not os.path.exists(path), f"{path} exists; prompts are written once"
    open(path, "w", encoding="utf-8").write(text)
    mark_seen(player)
    print(f"=== wrote {path}; send this ===\n{text}")

# ------------------------------------------------------------------ ceiling auctions
def settle(mn, step, bids, ORDER):
    """One rising auction from the limits. bids: {name: {"ceiling": n, "keep": {name: n}}}.
    A bidder's limit against the current leader is their keep-from figure for that leader if they
    gave one, else their ceiling. The winner pays one step over the runner-up's limit against them
    (never more than their own limit). Ties go by seat order. Returns a dict, or None for no sale."""
    def lim(a, b): return max(bids[a].get("ceiling", 0), bids[a].get("keep", {}).get(b, 0)) if b else bids[a].get("ceiling", 0)
    order = sorted(bids, key=ORDER.index)
    # Open outcry in steps: whoever isn't leading and whose limit against the leader covers the
    # next step raises by one step, earliest seat first. Stops when nobody can.
    leader, price = None, None
    while True:
        need = mn if price is None else price + step
        rivals = [a for a in order if a != leader and lim(a, leader) >= need]
        if not rivals: break
        leader, price = rivals[0], need
    if leader is None: return None
    # Ties go by seat order: an earlier seat whose limit equals the winning price, with the
    # winner unable to go higher against them, takes it at that price.
    for a in order:
        if a != leader and ORDER.index(a) < ORDER.index(leader) and lim(a, leader) >= price and lim(leader, a) <= price:
            leader = a; break
    runner = max((a for a in order if a != leader), key=lambda a: lim(a, leader), default=None)
    if runner and lim(runner, leader) >= mn:
        price = min(lim(leader, runner), lim(runner, leader) + step)
    else:
        price = mn
    seq = sorted([(a, min(lim(a, leader), price - step)) for a in order if a != leader and lim(a, leader) >= mn],
                 key=lambda kv: (kv[1], ORDER.index(kv[0]))) + [(leader, price)]
    close = None
    if runner and lim(runner, leader) >= mn:
        close = (runner, lim(runner, leader), lim(leader, runner))
    return dict(winner=leader, price=price, seq=seq, runner=close)

def report(r, step):
    if not r: print("No bids: nobody buys it."); return
    w, price = r["winner"], r["price"]
    print(f"Winner: {w} at {price:g}.")
    print("Each bidder's highest bid: " + ", ".join(f"{a} {b:g}" for a, b in r["seq"]))
    print("Ladder for lot(): " + ", ".join(f"B({a}, {b:g})" + ("" if a == w else f", B({a}, None)") for a, b in r["seq"]))
    if r["runner"]:
        runner, rl, wl = r["runner"]
        print(f"Runner-up: {runner}, limit {rl:g} against {w}; {w}'s limit {wl:g}.")
        # a near-tie worth a live raise: within one step, on a lot that matters (price 10 or more)
        if wl - rl <= step and r["price"] >= 10:
            print(f"CLOSE: offer {w} and {runner} one live raise-or-pass message each.")

def resolve(path):
    """One lot:  {"min": 5, "step": 1, "bids": {"Silke": {"ceiling": 12, "keep": {"Graham": 15}}, "Rob": "pass"}}
    A year's lots (batched; settled in order, each bidder's limits cut to the grain they have left,
    and each seller's quarter added to theirs before the next lot):
      {"step": 1, "lots": [{"lot": "2:CH", "min": 2}, {"lot": "5:DJ", "min": 6}],
       "bids": {"Rich": {"2:CH": {"ceiling": 8}, "5:DJ": {"ceiling": 6, "keep": {"Graham": 10}}}, "Rob": "pass"}}
    In the lot() ladder the seat is the bidder's seat now (`run.py` prints them)."""
    J = json.load(open(path, encoding="utf-8")); step = J.get("step", 1)
    ns = run_ns(); ORDER = seat_order(ns)
    if "lots" not in J:
        bids = {k: v for k, v in J["bids"].items() if v != "pass"}
        report(settle(J["min"], step, bids, ORDER), step); return
    SH = ns["SHORT"]; byname = {SH[p]: p for p in ns["PLAYERS"]}
    grain = {SH[p]: ns["grain"][p] for p in ns["PLAYERS"]}
    for L in J["lots"]:
        lot, mn = L["lot"], L.get("min", 2)
        sell = int(lot.split(":")[0]); seller = SH[ns["pid"](sell)] if sell else None
        print(f"\n=== {lot} (minimum {mn:g}) ===")
        bids = {}
        for name, b in J["bids"].items():
            if b == "pass" or not isinstance(b, dict) or b.get(lot) in (None, "pass"): continue
            if name == seller or ns["sid"](byname[name]) == 1: print(f"  ({name} can't bid on this lot; ignored)"); continue
            if grain[name] < 0: print(f"  ({name} is in debt and can't bid; ignored)"); continue
            x = dict(b[lot]); cap = grain[name]
            cut = {k: v for k, v in [("ceiling", x.get("ceiling", 0))] + list(x.get("keep", {}).items()) if v > cap}
            if cut:
                x["ceiling"] = min(x.get("ceiling", 0), cap)
                x["keep"] = {k: min(v, cap) for k, v in x.get("keep", {}).items()}
                print(f"  ({name}'s limits cut to the {cap:g} grain left)")
            bids[name] = x
        r = settle(mn, step, bids, ORDER); report(r, step)
        if r:
            grain[r["winner"]] -= r["price"]
            if seller: grain[seller] += ns["pay_down"](r["price"] * 0.25)
    print("\nGrain after the auctions: " + ", ".join(f"{k} {v:g}" for k, v in grain.items()))

if __name__ == "__main__":
    a = sys.argv[1:]
    def opt(k): return a[a.index(k)+1] if k in a else None
    if not a: print(__doc__)
    elif a[0] == "heard": heard(a[1], a[2])
    elif a[0] == "event": add_talk(dict(kind="event", text=a[1])); print("filed")
    elif a[0] == "note": add_talk(dict(kind="note", text=a[1], to=opt("--to"))); print("filed")
    elif a[0] == "prompt":
        prompt(a[1], a[2], a[3], lot=opt("--lot"), minimum=float(opt("--min")) if opt("--min") else None, menu=opt("--menu"),
               dry="--dry" in a, lots=opt("--lots"), rate=opt("--rate"), price=opt("--price"), floor=opt("--floor"), years=opt("--years"),
               short="--short" in a, offer=opt("--offer"), land="--land" in a,
               claims=opt("--claims"))
    elif a[0] == "resolve": resolve(a[1])
    elif a[0] == "seen":       # after a message sent by hand to everyone (the closing catch-up): all of them are up to date
        ns = run_ns()
        for p in (ns["PLAYERS"] if a[1] == "all" else [pid_of(ns, a[1])]): mark_seen(ns["SHORT"][p])
        print("marked seen:", a[1])
    else: print(__doc__)
