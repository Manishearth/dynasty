"""Print everyone's grain, and the Harvest Pile, after every entry of one game.
Soldier moves are listed under the line that makes them.

Usage (from the repo root):
  python3 playthrough-sim/trace.py game2_peasant.py            # the ledger
  python3 playthrough-sim/trace.py game2_peasant.py --board 57 # the board after entry 57
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build import run_ns

def board(ns, i):
    """The board after entry i as text: one character per square. Province squares show
    their number, raided squares x, realia a letter, soldiers W (Warlord) or b (bought)."""
    st = ns["ENTRIES"][i]["state"]; G = ns["GRID"]
    out = [[ch for ch in row] for row in G]
    def put(q, ch):
        r, c = ns["rc"](q); out[r][c] = ch
    for k, v in st["at"].items():
        for q in v: put(q, "P" if k in ns["PALACES"] else "R")
    for q, v in st["board"].items():
        if v.get("raid"): put(q, "x")
        if v.get("realia"): put(q, v["realia"][0].lower() if not v.get("raid") else "X")
    for sid, side, q, _ in st["sol"]: put(q, "W" if side == "W" else "b")
    lines = ["    " + "".join(str((c+1) % 10) for c in range(len(G[0])))]
    for r, row in enumerate(out): lines.append(f" {chr(65+r)}  " + "".join(row))
    lines.append("soldiers: " + ", ".join(f"{s}@{q}" for s, _, q, _ in st["sol"]))
    lines.append("realia: " + ", ".join(f"{v['realia']}@{q}({ns['SHORT'][v['owner']]})"
                                        for q, v in st["board"].items() if v.get("realia")))
    return "\n".join(lines)

if __name__ == "__main__":
    ns = run_ns(sys.argv[1])
    if len(sys.argv) > 3 and sys.argv[2] == "--board":
        print(board(ns, int(sys.argv[3]))); sys.exit()
    E, SH = ns["ENTRIES"], ns["SHORT"]
    starts = {r["start"]: r for r in ns["ROUNDS"]}
    for i, e in enumerate(E):
        if i in starts:
            r = starts[i]; print(f"\n=== {'SETUP' if r['n'] == 0 else 'YEAR %d' % r['n']} ({r['title']}) population x{r['mult']}")
        g = e["state"]["grain"]
        tag = {"act": "A", "say": "S", "lot": "L"}[e["k"]]
        gs = " ".join(f"{SH[int(k)][:3]}{v:g}" for k, v in g.items())
        print(f"[{i:3}] {tag} {(e.get('who') or ''):6} {e['t'][:66]:66} | {gs} | pile {e['state']['pile']:g}")
        if e.get("mv"):
            print("        moves: " + ", ".join(f"{a}->{b}" for a, b, _ in e["mv"]) +
                  "   now: " + ", ".join(f"{s}@{q}" for s, _, q, _ in e["state"]["sol"]))
