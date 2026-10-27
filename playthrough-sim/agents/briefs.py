"""The Storyteller's prompt generator. Every prompt is written once: this script builds it
from the engine's state (the game's game.py) and the table talk recorded so far, writes it to
the log, and prints it to send with SendMessage (or Agent, for a launch).

Run from the game's folder (playthroughs/<name>/), as python ../../playthrough-sim/agents/briefs.py ...:

  python briefs.py heard 021 log/year2/021-silke-reply.md   # file a reply's say and whisper as table talk
  python briefs.py event "Paddy buys the Jar for 27 and puts it on R21."
  python briefs.py prompt 022 Silke auction --lot 6:BB --min 5
  python briefs.py prompt 022 Rob march
  python briefs.py prompt 022 Paddy free --menu menu.md     # any other decision; the menu is your text
  python briefs.py prompt 022 Silke launch --menu menu.md   # a fresh agent: the character brief first
  python briefs.py resolve bids.json                         # settle a lot from ceilings
  add --dry to any prompt to print it without writing the log or marking it seen

Each prompt opens with everything said and done at the table since that player's last
prompt (talk.jsonl, seen.json), then the state that matters to them, then the menu and the
reply format. Geometry comes from geo.py and the engine, never by hand.

A launch (a fresh agent for a seat, at the start of every chapter) also carries that
character's entry in ledger.md and their diary so far (diaries/<name>.md).

The trial year's launch prompts (trial-year1/log/year1/003-005) were written by the first
version of this file; the brief text below is the same, with the auction economics, the
whisper line, the ledger entry and the diary added.
"""
import json, os, sys
from run import run_ns, steps
from geo import ranges

# Prompts go to log/year{N}/, N being the round game.py has reached (Setup counts as Year 1).
TALK, SEEN = "talk.jsonl", "seen.json"
# Seats change hands (a completed set replaces a player), so roles, the table and the auction's
# seat order always come from the engine's current seats, never from the booklets drawn.
ROLE = {1: "Emperor", 5: "Silk Peasant", 6: "Rice Peasant", 7: "Wheat Peasant", 8: "Warlord"}
WHERE = {1: "Province 1, the north-east, under the Great Wall", 5: "Province 5, the east coast",
         6: "Province 6, the south-east coast", 7: "Province 7, the south centre", 8: "the western and southern desert"}

def seat_of(ns, player): return ns["sid"](PLAYERS[player]["pid"])

def seat_order(ns): return sorted(PLAYERS, key=lambda n: seat_of(ns, n))

PLAYERS = {
 "Reina": dict(pid=1, full="Reina Osorio", pron="she",
   voice="She manages the table: she plans years ahead, and she knows when she's walking into a revolt clause."),
 "Silke": dict(pid=5, full="Silke Weber", pron="she",
   voice="She gets sharper as she gets squeezed."),
 "Paddy": dict(pid=6, full="Paddy Doyle", pron="he",
   voice="He's earnest and a little surprised to be winning."),
 "Graham": dict(pid=7, full="Graham Garner", pron="he",
   voice="He gets quieter and more precise as the grievance builds."),
 "Rob": dict(pid=8, full="Robert Land (\"Rob\")", pron="he",
   voice="He's realised he's the villain, and he's having a wonderful time."),
}

def table_text(ns):
    who = []
    for n in seat_order(ns):
        t = seat_of(ns, n); full = PLAYERS[n]["full"]
        who.append(f"{full} is the {ROLE[t]}, holding {WHERE[t]}." if t == 8 else f"{full} is the {ROLE[t]} ({WHERE[t]}).")
    return ("## The table\n\nFive players, about nine years. " + " ".join(who) +
            " Provinces 2, 3 and 4 are empty, so nobody pays rent, and the Emperor hands out their jobs.")

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
    r = parse_reply(path)
    if r.get("say"): add_talk(dict(n=n, kind="say", who=who, text=r["say"].strip('"')))
    w = r.get("whisper", "none")
    if w and w.lower().strip(' ".') != "none":
        to = w.split(":")[0].replace("To", "").strip()
        add_talk(dict(n=n, kind="whisper", who=who, to=to, text=w.split(":", 1)[1].strip()))
    print(f"filed {who}'s say" + (" and whisper" if "to" in locals() else ""))

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
def free_squares(ns, seat):
    """Squares a newly bought piece may stand on: the seat's own, unraided, empty, not under a work."""
    busy = {q for v in ns["pw_at"].values() for q in v}
    return [q for q in ns["squares_of"](seat) if q not in busy
            and not ns["board"].get(q, {}).get("raid") and not ns["board"].get(q, {}).get("realia")]

def safe_squares(ns, seat, rounds=2):
    sol = [s["sq"] for s in ns["SOLDIERS"].values() if s["side"] == "W"]
    return [q for q in free_squares(ns, seat) if all(ns["dist"](q, s) > rounds for s in sol)]

def state_block(ns, player):
    SH, R = ns["SHORT"], ns["RNAME"]; p = PLAYERS[player]["pid"]; seat = ns["sid"](p)
    g = ", ".join(f"{'**you %g**' % ns['grain'][q] if q == p else '%s %g' % (SH[q], ns['grain'][q])}" for q in ns["PLAYERS"])
    lines = [f"## The board now (after {'Setup' if not ns['CUR_ROUND'] else 'Year %d' % ns['CUR_ROUND']}'s steps so far)", "", f"- **Grain:** {g}."]
    pieces = [f"{SH[v['owner']]}'s {R[v['realia']]} on {q}" for q, v in ns["board"].items() if v.get("realia")]
    lines.append("- **Realia on the board:** " + ("; ".join(pieces) or "none") + ".")
    st = [f"{SH[ns['pid'](s)]}: " + ", ".join(f"{n} {R[t]}" for t, n in v.items()) for s, v in ns["stock"].items() if v]
    lines.append("- **Still beside the board (unsold):** " + ("; ".join(st) or "nothing") + ".")
    sol = [f"{i} on {s['sq']}" + ("" if s["side"] == "W" else f" ({SH[s['owner']]}'s)") for i, s in ns["SOLDIERS"].items()]
    lines.append("- **Soldiers:** " + (", ".join(sol) or "none yet") + ".")
    raided = sorted({ns["owner"](q) for q, v in ns["board"].items() if v.get("raid")} - {None})
    lines.append("- **Provinces raided so far** (their bought soldiers may move): " + (", ".join(map(str, raided)) or "none") + ".")
    if seat in ns["REALIA"]:
        need = [t for t in ns["need_for"](seat) if not ns["held"][p].get(t)]
        have = [R[t] for t, n in ns["held"][p].items() if n]
        lines.append(f"- **You hold:** {', '.join(have) or 'no realia'}. **Still needed:** {', '.join(R[t] for t in need) or 'nothing'}, and 20 grain.")
    if seat == 8:
        got = ", ".join(f"{SH[q]}'s {R[t]}" for q, t in ns["warlord_got"].items()) or "nothing yet"
        lines.append(f"- **Your objective so far:** {got} (one piece raided from each of Silke, Paddy and Graham).")
    return "\n".join(lines)

def dist_lines(ns):
    d = ns["dist"]; SH = ns["SHORT"]
    sol = {i: s["sq"] for i, s in ns["SOLDIERS"].items() if s["side"] == "W"}
    out = []
    for q, v in ns["board"].items():
        if v.get("realia"):
            out.append(f"{SH[v['owner']]}'s {ns['RNAME'][v['realia']]} ({q}): " + ", ".join(f"{i} {d(q, s)}" for i, s in sol.items()))
    return out

# ------------------------------------------------------------------ the board card
def board_card(ns, player):
    """A few lines at the top of every prompt, for this player only, always in the same layout.
    Every distance is the engine's dist() in rounds (one step a round)."""
    SH, R, d = ns["SHORT"], ns["RNAME"], ns["dist"]
    p = PLAYERS[player]["pid"]; seat = ns["sid"](p)
    sol = {i: s["sq"] for i, s in ns["SOLDIERS"].items() if s["side"] == "W"}
    raided = lambda q: ns["board"].get(q, {}).get("raid")
    out = [f"## Your board card ({'Setup' if not ns['CUR_ROUND'] else 'Year %d' % ns['CUR_ROUND']}, from the engine)", ""]
    have = ", ".join(f"{R[v['realia']]} {q}" for q, v in ns["board"].items() if v.get("realia") and v["owner"] == p)
    if seat == 8:
        got = ", ".join(f"{SH[q]}'s {R[t]}" for q, t in ns["warlord_got"].items()) or "nothing yet"
        left = [SH[ns["pid"](s)] for s in ns["ACTIVE"] if s in ns["REALIA"] and ns["pid"](s) not in ns["warlord_got"]]
        out.append(f"- **Grain** {ns['grain'][p]:g}. **Army** {len(sol)} of {ns['ARMY']+1}. **Objective:** raided {got}; still to raid a piece from {', '.join(left) or 'nobody'}.")
        if have: out.append(f"- **Pieces on your desert:** {have}. (Only raided pieces count toward your objective; the line above names them. A piece won at auction counts nothing.)")
        pcs = [(q, v) for q, v in ns["board"].items() if v.get("realia") and v["owner"] != p]
        out.append("- **Your soldiers:** " + (", ".join(f"{i} {sq}" for i, sq in sol.items()) or "none") + ".")
        out.append("- **Each piece, rounds from each soldier:** " + ("; ".join(
            f"{SH[v['owner']]}'s {R[v['realia']]} {q}: " + ", ".join(f"{i} {d(q, sq)}" for i, sq in sol.items())
            for q, v in sorted(pcs, key=lambda kv: kv[1]["owner"])) or "no pieces on the board") + ".")
        return "\n".join(out)
    if seat in ns["REALIA"]:
        need = [R[t] for t in ns["need_for"](seat) if not ns["held"][p].get(t)]
        out.append(f"- **Grain** {ns['grain'][p]:g}. **Hold:** {have or 'nothing'}. **Still need:** {', '.join(need) or 'nothing'}, and 20 grain.")
    else:
        left = sum((n - ns["built_count"](w)) * c for w, n, c in ns["owed"]())
        out.append(f"- **Grain** {ns['grain'][p]:g}. **Objective:** keep the throne. **Works still owed:** {left:g}.")
    mine = ns["squares_of"](seat)
    open_ = [q for q in mine if not raided(q)]
    if sol:
        pcs = [(q, v) for q, v in ns["board"].items() if v.get("realia") and v["owner"] == p]
        if pcs:
            out.append("- **Warlord soldiers to your pieces** (rounds): " + "; ".join(
                f"{R[v['realia']]} {q}: " + ", ".join(f"{i} {d(q, sq)}" for i, sq in sol.items()) for q, v in pcs) + ".")
        if open_:
            near = {i: min(open_, key=lambda q: d(q, sq)) for i, sq in sol.items()}
            out.append("- **Nearest unraided square of yours:** " + ", ".join(f"{i} {d(near[i], sq)} ({near[i]})" for i, sq in sol.items()) + ".")
        far1 = [q for q in mine if all(d(q, sq) > 1 for sq in sol.values())]
        far2 = [q for q in mine if all(d(q, sq) > 2 for sq in sol.values())]
        out.append(f"- **Out of every Warlord soldier's reach this year:** {ranges(ns, far1)}. **This year and next:** {ranges(ns, far2)}.")
    else:
        out.append("- **Warlord soldiers:** none on the board yet.")
    hit = any(raided(q) for q in mine)
    mine_sol = [f"{i} on {s['sq']}" for i, s in ns["SOLDIERS"].items() if s["side"] != "W" and s.get("owner") == p]
    out.append(f"- **Your province has {'been raided, so soldiers you buy can move' if hit else 'not been raided, so soldiers you buy cannot move yet'}.**"
               + (f" Yours: {', '.join(mine_sol)}." if mine_sol else ""))
    land = land_line(ns, seat)
    if land: out.append(land)
    return "\n".join(out)

def land_line(ns, seat):
    """New land (Section 13): what a square earns, and how many this province needs to break
    even in an average year now and after the next population card. From the engine's tables."""
    if seat not in ns["LAND_WHERE"]: return None
    m, pc = ns["MULT"], ns["pop_cards"]
    steps = []
    if pc[2] < 2 and m * 2 <= 6: steps.append(m * 2)
    if pc[1.5] < 1: steps.append(m * 1.5)
    nxt = max(steps) if steps else None
    extra = ns["bonus"][seat] + ns["pending_bonus"].get(seat, 0)
    avg = lambda mult: ns["HARV"][seat]["avg"] + extra - ns["CONS"][seat] * mult
    sq = lambda mult: max(0, -(-(-avg(mult)) // 20)) if avg(mult) < 0 else 0
    n = lambda k: f"{k:g} square" + ("" if k == 1 else "s")
    ahead = f" If the next population card comes (x{nxt:g}), you'd need {n(sq(nxt))} more than you have." if nxt else ""
    if m >= 2:
        return (f"- **New land is open** (Section 13): 20 a square, and the Emperor may pay any part of it. Each adds 20 "
                f"to every harvest from next year, so it pays for itself in one year. Your average-year income now: {avg(m):+g}; "
                f"to break even you'd need {n(sq(m))} more than you have.{ahead} Buy ahead: in debt you can't pay your share."
                + (" As Emperor you may pay any part of anyone's squares, even all of it: every square you fund raises "
                   "that province's taxable income and what it can put toward the works." if seat == 1 else ""))
    return (f"- **New land opens when the population doubles** (now x{m:g}). Then each square costs 20 and adds 20 a year. "
            f"At x2 you'd need {n(sq(2))} to break even in an average year, and more after the next card; save for them.")

# ------------------------------------------------------------------ the menus
def menu_auction(ns, player, lot, minimum):
    sell, typ = lot.split(":"); sell = int(sell); R, SH = ns["RNAME"], ns["SHORT"]
    p = PLAYERS[player]["pid"]; seat = ns["sid"](p)
    wants = [SH[ns["pid"](s)] for s in ns["ACTIVE"] if s in ns["REALIA"] and s != sell
             and typ in ns["need_for"](s) and not ns["held"][ns["pid"](s)].get(typ)]
    left = ns["stock"][sell].get(typ, 0)
    where = (f"a square of your desert (name one)" if seat == 8 else
             f"a square of your province. Out of every Warlord soldier's reach for two rounds: {ranges(ns, safe_squares(ns, seat))}")
    return f"""## Your move: {SH[ns['pid'](sell)]}'s {R[typ]}, minimum {minimum:g}

Who still needs one: {', '.join(wants) or 'nobody'}. {SH[ns['pid'](sell)]} has {left} in stock (this is {'the last' if left == 1 else 'one of ' + str(left)}).

You reply **once** for this lot; the Storyteller runs it as a rising auction from everyone's limits and narrates the climb.

- **pass** — most lots draw one or two serious bidders; passing is normal.
- **ceiling:** the most you'll pay (up to your grain).
- **keep from:** optional, `<name> up to <n>`: a higher limit you'd pay only to stop that player getting it.
- **square if you win:** {where}.
- **if I drop out:** one short line you'd say as you drop out (used only if you do).

{ECONOMICS}"""

def fmt_auction():
    return "move: pass | ceiling <n>; keep from <name> up to <n> (optional); square <square>\n"

def menu_march(ns):
    out = ["## Your move: the march", "", "Each soldier steps one square (diagonals allowed) or stands still. raid=5 (10 in Province 1) takes 5 from that province's player, or the piece standing there instead; '-' raids nothing. Tolls are 5 each, paid to the province."]
    for i, s in ns["SOLDIERS"].items():
        if s["side"] != "W": continue
        out += ["", f"**{i} on {s['sq']}:**"] + [f"- {l}" for l in steps(ns, i)] + ["- stay"]
    out += ["", "**Distances (rounds) from each piece to your soldiers:**"] + [f"- {l}" for l in dist_lines(ns)]
    n = sum(1 for s in ns["SOLDIERS"].values() if s["side"] == "W")
    if n < ns["ARMY"] + 1:
        out += ["", f"**Then, optionally, hire** one soldier for 20 on a square of your desert. Army {n} of {ns['ARMY']+1}."]
    if ns["CUR_ROUND"] in ns["NORAID"]:
        out += ["", f"**No raids this round on provinces {sorted(ns['NORAID'][ns['CUR_ROUND']])}** (your disaster); soldiers may still walk."]
    return "\n".join(out)

def fmt_march(ns):
    ws = [i for i, s in ns["SOLDIERS"].items() if s["side"] == "W"]
    return "move: " + "; ".join(f"{i} <square or stay>" for i in ws) + "; hire: <no, or a square>\n"

# ------------------------------------------------------------------ prompts
def launch_text(player, ns):
    d = PLAYERS[player]; short = player
    return f"""You're playing {d['full']} at a recorded game night. The game is Dynasty, a 1969 board game about ancient China. {short} is the {ROLE[seat_of(ns, player)]}. {d['voice']} {short} is "{d['pron']}".

This is a performance, so stay in {short}'s voice. Use no tools and read no files; just write your reply. I'm the Storyteller: I'll message you again each time it's your turn, with what's been said at the table, so keep track of the game as it goes.

{table_text(ns)}

{WHISPER}
""" + continuity(player)

def continuity(player):
    """For a launch: the character's ledger entry and their diary so far, if any."""
    out = []
    if os.path.exists("ledger.md"):
        led = open("ledger.md", encoding="utf-8").read()
        head = next((h for h in led.split("\n## ")[1:] if h.startswith(PLAYERS[player]["full"].split(" (")[0])), None)
        if head:
            body = head.split("\n", 1)[1].strip()
            if body: out.append(f"## Where {player} stands (the game's record so far)\n\n{body}")
    d = os.path.join("diaries", player.lower() + ".md")
    if os.path.exists(d):
        body = open(d, encoding="utf-8").read().split("\n", 1)[-1].strip()
        if body: out.append(f"## {player}'s diary so far, in {'her' if PLAYERS[player]['pron'] == 'she' else 'his'} own words\n\n{body}")
    return ("\n" + "\n\n".join(out) + "\n") if out else ""

def prompt(n, player, kind, lot=None, minimum=None, menu=None, dry=False):
    ns = run_ns(); short = player
    parts = []
    if kind == "launch": parts.append(launch_text(player, ns))
    parts.append(board_card(ns, player))
    heard_ = since(player)
    if heard_: parts.append("## At the table since your last turn\n\n" + "\n\n".join(heard_))
    parts.append(state_block(ns, player))
    if kind == "auction":
        parts.append(menu_auction(ns, player, lot, minimum)); fmt = fmt_auction() + FORMAT_TAIL + "\nif I drop out: <one short line>"
    elif kind == "march":
        parts.append(menu_march(ns)); fmt = fmt_march(ns) + FORMAT_TAIL
    else:
        parts.append(open(menu, encoding="utf-8").read().strip()); fmt = "move: <your choice>\n" + FORMAT_TAIL
    if kind != "launch": parts.append(WHISPER)
    parts.append("## Your reply\n\nReply in exactly this format:\n\n```\n" + fmt.format(short=short) + "\n```")
    text = "\n\n".join(parts) + "\n"
    if dry: print(text); return
    folder = f"log/year{max(1, ns['CUR_ROUND'] or 0)}"; os.makedirs(folder, exist_ok=True)
    path = f"{folder}/{n}-{player.lower()}-prompt.md"
    assert not os.path.exists(path), f"{path} exists; prompts are written once"
    open(path, "w", encoding="utf-8").write(text)
    mark_seen(player)
    print(f"=== wrote {path}; send this ===\n{text}")

# ------------------------------------------------------------------ ceiling auctions
def resolve(path):
    """bids.json: {"min": 5, "step": 1, "bids": {"Silke": {"ceiling": 12, "keep": {"Graham": 15}}, "Rob": "pass"}}
    A rising auction from the limits. A bidder's limit against the current leader is their keep-from
    figure for that leader if they gave one, else their ceiling. The winner pays one step over the
    runner-up's limit against them (never more than their own limit). Ties go by seat order."""
    J = json.load(open(path, encoding="utf-8")); step = J.get("step", 1); mn = J["min"]
    bids = {k: v for k, v in J["bids"].items() if v != "pass"}
    def lim(a, b): return max(bids[a].get("ceiling", 0), bids[a].get("keep", {}).get(b, 0)) if b else bids[a].get("ceiling", 0)
    ORDER = seat_order(run_ns())
    order = sorted(bids, key=ORDER.index)
    # Open outcry in steps: whoever isn't leading and whose limit against the leader covers the
    # next step raises by one step, earliest seat first. Stops when nobody can.
    leader, price, top = None, None, {}
    while True:
        need = mn if price is None else price + step
        rivals = [a for a in order if a != leader and lim(a, leader) >= need]
        if not rivals: break
        leader, price = rivals[0], need; top[leader] = price
    if leader is None: print("No bids: nobody buys it."); return
    # Ties go by seat order: an earlier seat whose limit equals the winning price, with the
    # winner unable to go higher against them, takes it at that price.
    for a in order:
        if a != leader and ORDER.index(a) < ORDER.index(leader) and lim(a, leader) >= price and lim(leader, a) <= price:
            leader = a; top[a] = price; break
    runner = max((a for a in order if a != leader), key=lambda a: lim(a, leader), default=None)
    # The price: one step over the runner-up's limit against the winner, capped at the winner's own.
    if runner and lim(runner, leader) >= mn:
        price = min(lim(leader, runner), lim(runner, leader) + step)
    else:
        price = mn
    print(f"Winner: {leader} at {price:g}.")
    # Each loser's highest bid is their limit against the winner (or the minimum's step below the price).
    seq = sorted([(a, min(lim(a, leader), price - step)) for a in order if a != leader and lim(a, leader) >= mn],
                 key=lambda kv: (kv[1], ORDER.index(kv[0]))) + [(leader, price)]
    print("Each bidder's highest bid: " + ", ".join(f"{a} {b:g}" for a, b in seq))
    print("Ladder for lot(): " + ", ".join(f"B({a}, {b:g})" + ("" if a == leader else f", B({a}, None)") for a, b in seq))
    if runner:
        gap = lim(leader, runner) - lim(runner, leader)
        print(f"Runner-up: {runner}, limit {lim(runner, leader):g} against {leader}; {leader}'s limit {lim(leader, runner):g}.")
        if gap <= 2 * step:
            print(f"CLOSE: offer {leader} and {runner} one live raise-or-pass message each.")

if __name__ == "__main__":
    a = sys.argv[1:]
    def opt(k): return a[a.index(k)+1] if k in a else None
    if a[0] == "heard": heard(a[1], a[2])
    elif a[0] == "event": add_talk(dict(kind="event", text=a[1])); print("filed")
    elif a[0] == "note": add_talk(dict(kind="note", text=a[1], to=opt("--to"))); print("filed")
    elif a[0] == "prompt":
        prompt(a[1], a[2], a[3], lot=opt("--lot"), minimum=float(opt("--min")) if opt("--min") else None, menu=opt("--menu"), dry="--dry" in a)
    elif a[0] == "resolve": resolve(a[1])
    else: print(__doc__)
