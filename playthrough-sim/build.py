"""Build ../playthrough.html from the game scripts.

Usage (from the repo root):  python3 playthrough-sim/build.py [out.html]
See README.md and docs/ in this folder.
"""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
GAMES = ["game1_full.py", "game2_peasant.py", "game3_short.py", "game4_complete.py", "game5_six.py"]

def run_ns(game):
    """Run one game script in a fresh namespace and return the namespace."""
    ns = {"SIM_DIR": HERE}
    for f in ("cards.py", "engine.py", os.path.basename(game)):
        p = os.path.join(HERE, f)
        exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    return ns

def run(game):
    return run_ns(game)["RESULT"]

def main(out):
    games = [run(g) for g in GAMES if os.path.exists(os.path.join(HERE, g))]
    data = json.dumps({"games": games}, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")
    head = open(os.path.join(HERE, "template", "head.html"), encoding="utf-8").read()
    tail = open(os.path.join(HERE, "template", "tail.html"), encoding="utf-8").read()
    # piece names to mark with a glyph, shared with tools/add_glyphs.py
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    from add_glyphs import js_terms
    tail = tail.replace("/*PIECE_TERMS*/[]", js_terms())
    open(out, "w", encoding="utf-8").write(head + data + tail)
    print(f"wrote {out}: {len(games)} games, {sum(len(g['entries']) for g in games)} entries")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "playthrough.html"))
