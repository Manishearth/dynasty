"""Scout I Ching deck orders before a game: what a seed's shuffle does to the years.

The deck is the game's only chance: the booklets are dealt by name, and each seat's
personal disasters come in booklet order. A game's deck is shuffled the same way every
time (seed.md): the twenty card keys from cards.py, sorted, then
random.Random(seed).shuffle(keys). Year 1 draws no card, so Year N draws card N-1.

    python deck_scout.py 19691108 --seats 1,2,3,4,5,6,7,8 --years 10
        one seed, year by year: the card, the harvest, the population multiple, each
        seat's bare income (harvest - consumption, before works, land, tax and rent),
        and who plays a personal disaster. Then the seed's numbers (below) and a deck
        list to paste into seed.md.
    python deck_scout.py --search 1-5000 --seats 1,5,6,7 --years 10 --where "land<=4 and lean_early>=2"
        every seed in the range whose numbers pass the test, best first (--top, default 10).

The numbers a --where test can use:
    land          first year the population has doubled (x2 or more), so new land opens; 99 if never
    mult          the multiple in the last year;  mult_at[y] the multiple in year y
    lean[y]       how many active seats have a bad harvest in year y (0 when y draws no card)
    lean_early    years 2-5 in which most active seats have a bad harvest
    lean_late     the same from year 6 to the last
    red[y]        how many active seats (not the Warlord) have a negative bare income in year y
    red_first     first year any non-Warlord seat's bare income is negative; 99 if never
    dis[s]        personal disasters seat s plays over the game;  dis_by[s][y] up to year y
    pop_years     the years a population card takes effect
The Warlord's first personal disaster is "no raids this year" (engine DISASTERS[8]).

The scout knows only the deck, so it says nothing about what the players do with it.
It reads cards.py and engine.py's tables, so it follows any change to either.
"""
import argparse, os, random, re

SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # playthrough-sim/
ns = {}
exec(open(os.path.join(SIM, "cards.py"), encoding="utf-8").read(), ns)
CARDS = ns["CARDS"]
eng = open(os.path.join(SIM, "engine.py"), encoding="utf-8").read()
for line in eng.splitlines():   # the tables only, not the whole engine
    if re.match(r"(CONS|HARV)\b", line): exec(line, ns)
CONS, HARV = ns["CONS"], ns["HARV"]

# Which provinces play a personal disaster, from each card's text ("every player" for careless).
def disaster_seats(key):
    t = CARDS[key]["text"]
    if "Every player plays a Personal Disaster" in t: return set(range(1, 9))
    m = re.search(r"Provinces ([\d, ]+) (?:each )?play a Personal Disaster", t)
    return {int(x) for x in re.findall(r"\d", m.group(1))} if m else set()

def deck(seed):
    keys = sorted(CARDS); random.Random(seed).shuffle(keys); return keys

def play(seed, seats, years):
    """Year by year: (year, card, quality by seat, multiple, bare income by seat, disaster seats)."""
    mult, taken, rows = 1, {2: 0, 1.5: 0}, []
    order = deck(seed)
    for y in range(1, years + 1):
        if y == 1:
            rows.append((1, None, {s: "good" for s in seats}, 1, {s: 60 for s in seats}, set()))
            continue
        key = order[y - 2]; c = CARDS[key]; pop = c.get("pop")
        if pop == 2 and (taken[2] >= 2 or mult * 2 > 6): pop = None   # engine.R's caps
        if pop == 1.5 and taken[1.5] >= 1: pop = None
        if pop: mult *= pop; taken[pop] += 1
        q = c["q"] if isinstance(c["q"], dict) else {s: c["q"] for s in range(1, 9)}
        inc = {s: HARV[s][q[s]] - CONS[s] * mult for s in seats}
        rows.append((y, key, {s: q[s] for s in seats}, mult, inc, disaster_seats(key) & set(seats)))
    return rows

def numbers(rows, seats):
    years = len(rows); civil = [s for s in seats if s != 8]
    lean = {r[0]: sum(1 for s in seats if r[2][s] == "bad") for r in rows}
    lean[1] = 0
    most = lambda y: lean[y] * 2 > len(seats)
    red = {r[0]: sum(1 for s in civil if r[4][s] < 0) for r in rows}
    dis_by = {s: {} for s in seats}
    for s in seats:
        n = 0
        for r in rows:
            n += s in r[5]; dis_by[s][r[0]] = n
    prev, pop_years = 1, []
    for r in rows:
        if r[3] != prev: pop_years.append(r[0])
        prev = r[3]
    return dict(
        land=next((r[0] for r in rows if r[3] >= 2), 99),
        mult=rows[-1][3], mult_at={r[0]: r[3] for r in rows},
        lean=lean, lean_early=sum(1 for y in range(2, min(5, years) + 1) if most(y)),
        lean_late=sum(1 for y in range(6, years + 1) if most(y)),
        red=red, red_first=next((y for y in sorted(red) if red[y]), 99),
        dis={s: dis_by[s][years] for s in seats}, dis_by=dis_by, pop_years=pop_years)

ROLE = {1: "Emp", 2: "Off", 3: "Gen", 4: "Sch", 5: "Silk", 6: "Rice", 7: "Whe", 8: "War"}

def show(seed, seats, years):
    rows = play(seed, seats, years); n = numbers(rows, seats)
    print(f"seed {seed}, seats {','.join(map(str, seats))}, {years} years")
    print("year  card       x    " + "".join(f"{ROLE[s]:>7}" for s in seats) + "   disasters")
    for y, key, q, mult, inc, dis in rows:
        cells = "".join((f"{inc[s]:+g}" + ("." if q[s] == "bad" else " ")).rjust(7) for s in seats)
        print(f"{y:>4}  {key or '-':<10} {mult:<5g} {cells}   {','.join(map(str, sorted(dis))) or '-'}")
    print("(bare income: harvest - consumption, before works, land, tax and rent; '.' marks a bad harvest)")
    print(f"land opens: {'Year ' + str(n['land']) if n['land'] < 99 else 'never'} · population cards take effect in "
          f"{', '.join('Year ' + str(y) for y in n['pop_years']) or 'no year'} · last multiple x{n['mult']:g}")
    print(f"lean years (most seats bad): {n['lean_early']} in Years 2-5, {n['lean_late']} after · "
          f"first negative bare income: {'Year ' + str(n['red_first']) if n['red_first'] < 99 else 'never'}")
    print("personal disasters: " + ", ".join(f"{ROLE[s]} {n['dis'][s]}" for s in seats))
    print("\nFor seed.md (top first; Year N draws card N-1):\n")
    print("  " + " · ".join(f"{i}. {k}" for i, k in enumerate(deck(seed), 1)))

def search(lo, hi, seats, years, where, top, sort):
    hits = []
    for seed in range(lo, hi + 1):
        n = numbers(play(seed, seats, years), seats)
        if eval(where, dict(n)): hits.append((eval(sort, dict(n)) if sort else 0, seed, n))
    hits.sort(key=lambda h: h[0])
    print(f"{len(hits)} of {hi - lo + 1} seeds pass: {where}")
    for _, seed, n in hits[:top]:
        print(f"  {seed:>7}  land Y{n['land'] if n['land'] < 99 else '-'}  pop {n['pop_years']}  x{n['mult']:g}  "
              f"lean {n['lean_early']}+{n['lean_late']}  red from Y{n['red_first'] if n['red_first'] < 99 else '-'}  "
              f"disasters {dict((ROLE[s], v) for s, v in n['dis'].items())}")

if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("seed", nargs="?", type=int)
    ap.add_argument("--seats", default="1,2,3,4,5,6,7,8")
    ap.add_argument("--years", type=int, default=10)
    ap.add_argument("--search", help="a seed range, like 1-5000")
    ap.add_argument("--where", default="True", help="a Python test over the numbers above")
    ap.add_argument("--sort", default="", help="an expression to sort the hits by, lowest first (write --sort=-x for a leading minus)")
    ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args()
    seats = [int(x) for x in a.seats.split(",")]
    if a.search:
        lo, hi = map(int, a.search.split("-"))
        search(lo, hi, seats, a.years, a.where, a.top, a.sort)
    else:
        show(a.seed, seats, a.years)
