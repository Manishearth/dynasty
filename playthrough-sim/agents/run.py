"""The Storyteller's referee: run a game's game.py through the engine the way build.py's
run_ns does (cards.py, then engine.py, then the script), then print the state.

Run from the game's folder (playthroughs/<name>/), where game.py, state/ and the logs live:

  python ../../playthrough-sim/agents/run.py                 # ledger tail + board + soldiers
  python ../../playthrough-sim/agents/run.py --snapshot NAME # also save state/NAME.json
  python ../../playthrough-sim/agents/run.py --steps W1      # the squares W1 can step to, with raids and tolls
  python ../../playthrough-sim/agents/run.py --script other.py   # another script
"""
import os, sys, json
HERE = os.getcwd()                      # the game's folder
SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # playthrough-sim/
sys.path.insert(0, SIM)

SCRIPT = os.path.join(HERE, sys.argv[sys.argv.index("--script")+1] if "--script" in sys.argv else "game.py")

def run_ns():
    ns = {"SIM_DIR": SIM}
    for p in (os.path.join(SIM, "cards.py"), os.path.join(SIM, "engine.py"), SCRIPT):
        exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    return ns

def board_text(ns):
    G = ns["GRID"]; out = [list(r) for r in G]
    def put(q, ch):
        r, c = ns["rc"](q); out[r][c] = ch
    for k, v in ns["pw_at"].items():
        for q in v: put(q, "P" if k in ns["PALACES"] else "R")
    for q, v in ns["board"].items():
        if v.get("raid"): put(q, "x")
        if v.get("realia"): put(q, v["realia"][0].lower())
    for i, s in ns["SOLDIERS"].items(): put(s["sq"], "W" if s["side"] == "W" else "b")
    lines = ["    " + "".join(str((c+1) % 10) for c in range(len(G[0])))]
    for r, row in enumerate(out): lines.append(f" {chr(65+r)}  " + "".join(row))
    return "\n".join(lines)

def steps(ns, sid):
    s = ns["SOLDIERS"][sid]; r0, c0 = ns["rc"](s["sq"]); out = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            r, c = r0+dr, c0+dc
            if (dr, dc) == (0, 0) or not (0 <= r < ns["ROWS"] and 0 <= c < ns["COLS"]): continue
            q = ns["sqname"](r, c); g = ns["GRID"][r][c]
            o = ns["owner"](q); raid = o in ns["ACTIVE"] and not ns["board"].get(q, {}).get("raid")
            piece = ns["board"].get(q, {}).get("realia")
            foe = [i for i, t in ns["SOLDIERS"].items() if t["sq"] == q and t["side"] != s["side"]]
            if foe and dr and dc: continue          # an enemy square is entered only by capture, never diagonally
            if raid and o in ns["NORAID"].get(ns["CUR_ROUND"], ()):
                out.append(f"{q} [{g}] BARRED: no raids on Province {o} this round (the step would have to raid)"); continue
            out.append(f"{q} [{g}] raid={'10' if raid and o == 1 else ('5' if raid else '-')}"
                       f"{' piece='+piece if piece else ''}{' CAPTURES '+','.join(foe) if foe else ''}"
                       f" tolls={ns['tolls'](s['sq'], q)}")
    return out

if __name__ == "__main__":
    ns = run_ns()
    E, SH = ns["ENTRIES"], ns["SHORT"]
    for e in E[-12:]:
        g = e["state"]["grain"]
        print(f"{e['k']:3} {(e.get('who') or ''):6} {e['t'][:70]:70} | " +
              " ".join(f"{SH[int(k)][:3]}{v:g}" for k, v in g.items()) + f" | pile {e['state']['pile']:g}")
    print(board_text(ns))
    print("soldiers:", {i: s["sq"] for i, s in ns["SOLDIERS"].items()})
    print("realia:", {q: (v["realia"], SH[v["owner"]]) for q, v in ns["board"].items() if v.get("realia")})
    print("stock:", ns["stock"], "held:", {SH[p]: dict(h) for p, h in ns["held"].items() if h})
    print("grain:", {SH[p]: ns["grain"][p] for p in ns["PLAYERS"]}, "pile:", ns["pile"])
    a = sys.argv[1:]
    if "--steps" in a:
        for l in steps(ns, a[a.index("--steps")+1]): print(" ", l)
    if "--snapshot" in a:
        name = a[a.index("--snapshot")+1]
        os.makedirs(os.path.join(HERE, "state"), exist_ok=True)
        snap = dict(entry=len(E)-1, round=ns["CUR_ROUND"], state=ns["snap"](),
                    soldiers=ns["SOLDIERS"], mult=ns["MULT"], cards_drawn=sorted(ns.get("_drawn", [])) if "_drawn" in ns else None)
        with open(os.path.join(HERE, "state", name + ".json"), "w", encoding="utf-8") as f:
            json.dump(snap, f, indent=1, default=str)
        print("saved state/" + name + ".json")
