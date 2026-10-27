"""Build ../../playthroughs-real.html from the agent-played games in ../../playthroughs/.

Usage (from the repo root):  python playthrough-sim/agents/build_real.py [out.html]

Each game is playthroughs/<name>/game.py, run through the same engine and page templates
as the hand-written playthroughs (playthrough-sim/build.py). GAMES lists the games that go
on the page, in order; a game folder not listed here (the trial year) stays off it.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import build

GAMES = ["peasant-collapse"]

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "playthroughs-real.html")
    build.main(out, [os.path.join(ROOT, "playthroughs", g, "game.py") for g in GAMES])
