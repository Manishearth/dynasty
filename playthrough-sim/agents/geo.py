"""Board geometry for prompts, computed by the engine (dist, tolls, owner), never by hand.

  python geo.py                 # the state at the end of game.py (run from the game's folder), reach within 2 rounds
  python geo.py --rounds 1      # within 1 round
  python geo.py --at W1=P19,W2=R24   # other soldier squares (what-if), Warlord soldiers only

Prints:
  - each Warlord soldier's next steps (raid value, piece, tolls), as run.py --steps does;
  - each placed piece of realia and its distance to every Warlord soldier;
  - each occupied province: its nearest square to each soldier, the squares some soldier
    can reach within N rounds, and the squares no soldier can reach within N rounds.
A soldier stands on a square after k rounds if dist <= k (every square is open to it).
"""
import sys
from run import run_ns, steps

def ranges(ns, sqs):
    """['Q21','Q22','R19'] -> 'Q21–Q22, R19' (consecutive columns in a row run together)."""
    rows = {}
    for q in sqs:
        r, c = ns["rc"](q); rows.setdefault(r, []).append(c)
    out = []
    for r in sorted(rows):
        cs = sorted(rows[r]); start = prev = cs[0]
        for c in cs[1:] + [None]:
            if c is not None and c == prev + 1:
                prev = c; continue
            a, b = ns["sqname"](r, start), ns["sqname"](r, prev)
            out.append(a if a == b else f"{a}–{b}")
            if c is not None: start = prev = c
    return ", ".join(out) or "none"

def report(ns, rounds=2, at=None):
    sol = {i: s["sq"] for i, s in ns["SOLDIERS"].items() if s["side"] == "W"}
    if at: sol.update(at)
    d = ns["dist"]; SH = ns["SHORT"]
    print(f"Warlord soldiers: {sol}")
    for i, s in ns["SOLDIERS"].items():
        if s["side"] != "W": print(f"Bought soldier {i} ({SH[s['owner']]}) on {s['sq']}")
    if not at:
        for i in sol:
            print(f"\n{i} next steps:")
            for l in steps(ns, i): print("  " + l)
    print("\nRealia on the board:")
    for q, v in ns["board"].items():
        if v.get("realia"):
            print(f"  {v['realia']} ({SH[v['owner']]}) on {q}: " +
                  ", ".join(f"{i} {d(q, s)}" for i, s in sol.items()))
    for p in ns["ACTIVE"]:
        if p == 8: continue
        sq = ns["squares_of"](p)
        best = {i: min(sq, key=lambda q: d(q, s)) for i, s in sol.items()}
        near = ", ".join(f"{i} {d(best[i], s)} ({best[i]})" for i, s in sol.items())
        reach = [q for q in sq if any(d(q, s) <= rounds for s in sol.values())]
        safe = [q for q in sq if q not in reach]
        print(f"\nProvince {p} ({SH[ns['pid'](p)]}): nearest square to each soldier: {near}")
        print(f"  reachable within {rounds} round(s): {ranges(ns, reach)}")
        print(f"  out of reach for {rounds} round(s): {ranges(ns, safe)}")

if __name__ == "__main__":
    a = sys.argv[1:]
    n = int(a[a.index("--rounds")+1]) if "--rounds" in a else 2
    at = dict(x.split("=") for x in a[a.index("--at")+1].split(",")) if "--at" in a else None
    report(run_ns(), n, at)
