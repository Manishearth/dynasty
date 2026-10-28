"""Build ../../playthroughs-real.html from the agent-played games in ../../playthroughs/.

Usage (from the repo root):  python playthrough-sim/agents/build_real.py [out.html]

Each game is playthroughs/<name>/game.py, run through the same engine and page templates
as the hand-written playthroughs (playthrough-sim/build.py). GAMES lists the games that go
on the page, in order; a game folder not listed here (the trial year) stays off it.

A game still being played goes in IN_PROGRESS with the last finished year: its script runs
only up to the next year's marker (so the year being played now stays off the page),
and the builder adds the ending the script doesn't have yet, saying it's unfinished.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.dirname(HERE))
import build

GAMES = ["full-game", "short-game", "highway-robbery", "western-front",
         "peasant-collapse", "dark-ages", "peasant-draw"]
# The last finished year to show (the script is cut at the next year's marker): moved on by the
# Director as each year closes. Drop the game from here once its game.py has its own ending
# (RESULT = export(...)).
IN_PROGRESS = {}    # e.g. {"full-game": 12} while a game is being played
# A game not started yet shows its setup only, until its first year is played.
IN_PROGRESS.update({g: 0 for g in ("dark-ages",)})
IN_PROGRESS.update({"dark-ages": 4})
# The game selector's title and subtitle while a game is still being played (its game.py keeps
# its own until the game ends, when the subtitle gets the result).
IN_PROGRESS_TITLE = {"dark-ages": ("The Dark Ages", "Six players · in progress")}
# The line under the game picker while a game is being played: the table and the story so far,
# updated by the Director as the story moves (its game.py gets the full story when it ends).
IN_PROGRESS_BLURB = {}

def run_partial(path, year):
    stop = f"# ============================== YEAR {year + 1} "
    ns = {"SIM_DIR": build.HERE}
    for p in (os.path.join(build.HERE, "cards.py"), os.path.join(build.HERE, "engine.py")):
        exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    src = open(path, encoding="utf-8").read()
    if stop in src: src = src[:src.index(stop)]
    exec(compile(src, path, "exec"), ns)
    n = ns["CUR_ROUND"]
    if not n:
        return ns["export"]("Not started yet: this is the table as it's set up. The game is played by agents, a chapter at a time.",
                            "To be played.")
    return ns["export"](
        f"Still being played: this is the game so far, to the end of Year {n}. The seats below are where everyone sits "
        "now, compared with the seat they drew; nothing is settled until the game ends.",
        f"To be continued. The game so far runs to the end of Year {n}.")

_run = build.run
def run(game):
    name = os.path.basename(os.path.dirname(game))
    if name not in IN_PROGRESS: return _run(game)
    res = run_partial(game, IN_PROGRESS[name])
    if name in IN_PROGRESS_TITLE:
        res["meta"] = dict(res["meta"], title=IN_PROGRESS_TITLE[name][0], subtitle=IN_PROGRESS_TITLE[name][1])
    if name in IN_PROGRESS_BLURB:
        res["meta"] = dict(res["meta"], blurb=IN_PROGRESS_BLURB[name])
    return res
build.run = run

if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "playthroughs-real.html")
    build.main(out, [os.path.join(ROOT, "playthroughs", g, "game.py") for g in GAMES])
