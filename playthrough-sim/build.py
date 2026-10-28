"""Build ../playthrough-scripted.html from the game scripts.

Usage (from the repo root):  python3 playthrough-sim/build.py [out.html]
See README.md and docs/ in this folder. The agent-played games are built into
../playthrough.html by agents/build_real.py, from the same templates.
"""
import json, re, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
GAMES = ["game1_full.py", "game2_trashfire.py", "game3_short.py", "game4_peasant.py", "game5_six.py",
         "game6_quiet.py", "game7_dark.py"]
# The page's title and heading, and the link to the other playthrough page.
PAGE = dict(title="Dynasty Scripted Playthroughs", heading="Dynasty — Scripted playthroughs",
            other_href="playthrough.html", other_label="The games played by agents →")

def keys(scripts):
    """The game keys (page addresses) of these scripts, read from their setup() calls."""
    out = []
    for g in scripts:
        m = re.search(r'setup\(\[[^\]]*\],\s*"([^"]+)"', open(os.path.join(HERE, g), encoding="utf-8").read())
        if m: out.append(m.group(1))
    return out

def load_engine(ns):
    """Load the cards and the engine into ns. Every entry's state also records whether Chaos holds
    (the engine's CHAOS flag), so the page can show it on the board."""
    for p in (os.path.join(HERE, "cards.py"), os.path.join(HERE, "engine.py")):
        exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    snap = ns["snap"]
    ns["snap"] = lambda: dict(snap(), chaos=bool(ns.get("CHAOS")))

def run_ns(game):
    """Run one game script in a fresh namespace and return the namespace."""
    ns = {"SIM_DIR": HERE}
    load_engine(ns)
    p = os.path.join(HERE, game)
    exec(compile(open(p, encoding="utf-8").read(), p, "exec"), ns)
    return ns

def run(game):
    return run_ns(game)["RESULT"]

def main(out, scripts=None, page=PAGE, forward=None):
    """scripts: game scripts to build, absolute or relative to this folder (default GAMES).
    page: the title, heading and link to the other page. forward: {game key: page} for games
    that live on another page, so an old address lands on the right one."""
    games = [run(g) for g in (scripts or GAMES) if os.path.exists(os.path.join(HERE, g))]
    data = json.dumps({"games": games}, ensure_ascii=False, separators=(",", ":"))
    data = data.replace("</", "<\\/")
    head = open(os.path.join(HERE, "template", "head.html"), encoding="utf-8").read()
    tail = open(os.path.join(HERE, "template", "tail.html"), encoding="utf-8").read()
    # piece names to mark with a glyph, shared with tools/add_glyphs.py
    sys.path.insert(0, os.path.join(HERE, "..", "tools"))
    from add_glyphs import js_terms, PIECE_CSS
    from glyphs import GLYPHS
    # glyph sizes in running text, the same rules the rulebook gets
    head = head.replace("/*PIECE_CSS*/", PIECE_CSS.rstrip("\n"))
    tail = tail.replace("/*PIECE_TERMS*/[]", js_terms())
    # the soldier glyph's outline, drawn on the board in each side's colour
    tail = tail.replace("/*SOLDIER_PATH*/''", json.dumps(GLYPHS["soldier"][2]))
    for mark, k in (("PAGE_TITLE", "title"), ("PAGE_HEADING", "heading"),
                    ("OTHER_HREF", "other_href"), ("OTHER_LABEL", "other_label")):
        head = head.replace(f"/*{mark}*/", page[k])
    tail = tail.replace("/*FORWARD*/{}", json.dumps(forward or {}))
    open(out, "w", encoding="utf-8", newline="\n").write(head + data + tail)
    print(f"wrote {out}: {len(games)} games, {sum(len(g['entries']) for g in games)} entries")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "playthrough-scripted.html"))
