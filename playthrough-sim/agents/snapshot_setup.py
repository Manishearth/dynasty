"""Save state/setup.json: the state at the end of the Setup round (before Year 1).
Runs the game's game.py up to its Year 1 marker. Run from the game's folder:
python ../../playthrough-sim/agents/snapshot_setup.py"""
import json, os
SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # playthrough-sim/
ns = {"SIM_DIR": SIM}
for p in ("cards.py", "engine.py"):
    p = os.path.join(SIM, p)
    exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
src = open("game.py", encoding="utf-8").read()
cut = src.index("# ============================== YEAR 1")
exec(compile(src[:cut], "game.py[setup]", "exec"), ns)
snap = dict(entry=len(ns["ENTRIES"]) - 1, round=ns["CUR_ROUND"], state=ns["snap"](),
            soldiers=ns["SOLDIERS"], mult=ns["MULT"])
os.makedirs("state", exist_ok=True)
json.dump(snap, open("state/setup.json", "w", encoding="utf-8"), indent=1, default=str)
print(snap["state"]["grain"], snap["soldiers"])
