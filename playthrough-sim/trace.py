"""Print everyone's grain, and the Harvest Pile, after every entry of one game.

Usage (from the repo root):  python3 playthrough-sim/trace.py game2_peasant.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import HERE

def run(game):
    ns = {}
    for f in ("cards.py", "engine.py", game):
        p = os.path.join(HERE, os.path.basename(f))
        exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    return ns

if __name__ == "__main__":
    ns = run(sys.argv[1])
    E, SH = ns["ENTRIES"], ns["SHORT"]
    starts = {r["start"]: r for r in ns["ROUNDS"]}
    for i, e in enumerate(E):
        if i in starts:
            r = starts[i]; print(f"\n=== YEAR {r['n']} ({r['title']}) population x{r['mult']}")
        g = e["state"]["grain"]
        tag = {"act": "A", "say": "S", "lot": "L"}[e["k"]]
        gs = " ".join(f"{SH[int(k)][:3]}{v:g}" for k, v in g.items())
        print(f"[{i:3}] {tag} {(e.get('who') or ''):6} {e['t'][:66]:66} | {gs} | pile {e['state']['pile']:g}")
