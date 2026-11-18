"""Re-place a playthrough's one-square harvest squares as 2 x 2 ones, without changing play.

Games played before harvest squares were found to cover 2 x 2 map squares bought land one map
square at a time (their scripts set LAND_BLOCK = 1). This finds a 2 x 2 harvest square for each
of those purchases, in order: on the same ground, free, touching the province or its land as it
stood then, covering the square originally bought where it can (so talk of 'F23' stays true).
Then it replays the game and checks that nothing but the land changed.

Usage (from the repo root):
  python tools/replace_land.py playthroughs/short-game/game.py            # report only
  python tools/replace_land.py playthroughs/short-game/game.py --write    # rewrite the script
  python tools/replace_land.py playthroughs/peasant-thrive/game.py --until 7 --write
      # for a replay from Year 7: cut the script at Year 7's marker, re-place the land
      # bought before it, and check Years 1-6 replay unchanged

--until N cuts the script at "# ===... YEAR N", or at the year's R(N, ...) line where the script
has no marker (git keeps the rest). Without --write nothing is
written. The rewrite replaces, inside each buy_land call only, every square bought by the
corner of its new harvest square; check the call's text reads right afterwards ("F23 to F26").
"""
import ast, json, os, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "playthrough-sim"))
import build

G = json.load(open(os.path.join(ROOT, "map.json"), encoding="utf-8"))["grid"]
ROWS, COLS = len(G), len(G[0])
def rc(n): return ord(n[0]) - 65, int(n[1:]) - 1
def nm(r, c): return f"{chr(65 + r)}{c + 1}"
def block(r, c): return ((r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1))
LAND_LINE = re.compile(r"^LAND_BLOCK = 1\b[^\n]*\r?\n", re.M)

def run(src, path):
    """Run a game script's source through the engine; returns the page data."""
    ns = {"SIM_DIR": build.HERE}
    build.load_engine(ns)
    exec(compile(src, path, "exec"), ns)
    if "RESULT" in ns: return ns["RESULT"]
    return ns["export"]("", "")

def purchases(src):
    """[(line, seat, [squares])] for every buy_land call, in script order."""
    out = []
    for n in ast.walk(ast.parse(src)):
        if isinstance(n, ast.Call) and getattr(n.func, "id", None) == "buy_land":
            out.append((n.lineno, ast.literal_eval(n.args[0]), ast.literal_eval(n.args[1])))
    return sorted(out)

def ring(cells):
    """The squares touching these (diagonals included)."""
    return frozenset((a + i, b + j) for a, b in cells for i in (-1, 0, 1) for j in (-1, 0, 1))

def solve(buys, avoid=frozenset(), limit=50000):
    """A 2 x 2 corner for every square bought, or None. Depth-first, best candidates first.
    avoid: squares a piece stands on at some point, which new land may cover only where it was bought."""
    items = [(ln, p, rc(q)) for ln, p, qs in buys for q in qs]
    near = {p: ring((r, c) for r in range(ROWS) for c in range(COLS) if G[r][c] == str(p)) for p in range(1, 8)}
    steps = [0]
    def cands(q, taken, nearp):
        reg = G[q[0]][q[1]]; out = []
        for r in range(ROWS - 1):
            for c in range(COLS - 1):
                cs = block(r, c)
                if any(G[a][b] != reg or (a, b) in taken or ((a, b) in avoid and (a, b) != q) for a, b in cs): continue
                if not any(x in nearp for x in cs): continue
                out.append((0 if q in cs else 10 + abs(r - q[0]) + abs(c - q[1]), (r, c)))
        return sorted(out)[:6]
    def go(i, taken, near, sol):
        steps[0] += 1
        if steps[0] > limit: return None
        if i == len(items): return sol
        ln, p, q = items[i]
        for _, (r, c) in cands(q, taken, near[p]):
            cs = block(r, c)
            got = go(i + 1, taken | frozenset(cs), {**near, p: near[p] | ring(cs)}, sol + [(ln, nm(*q), nm(r, c))])
            if got is not None: return got
        return None
    return go(0, frozenset(), near, [])

def rewrite(src, sol):
    """Swap, inside each buy_land call, every square bought for its harvest square's corner."""
    bycall = {}
    for ln, old, new in sol: bycall.setdefault(ln, {})[old] = new
    lines = src.splitlines(keepends=True); starts = [0]
    for l in lines: starts.append(starts[-1] + len(l))
    off = lambda ln, col: starts[ln - 1] + len(lines[ln - 1].encode("utf-8")[:col].decode("utf-8"))
    spans = [(off(n.lineno, n.col_offset), off(n.end_lineno, n.end_col_offset), n.lineno)
             for n in ast.walk(ast.parse(src)) if isinstance(n, ast.Call) and getattr(n.func, "id", None) == "buy_land"]
    for a, b, ln in sorted(spans, reverse=True):
        m = bycall[ln]
        pat = re.compile(r"\b(" + "|".join(sorted(map(re.escape, m), key=len, reverse=True)) + r")\b")
        src = src[:a] + pat.sub(lambda x: m[x.group(1)], src[a:b]) + src[b:]
    return src

def same_play(a, b):
    """None if two runs differ only in their land (and buy_land text), else where they part."""
    skip = {"land", "lb", "lblock"}
    if len(a["entries"]) != len(b["entries"]): return f"entry count {len(a['entries'])} -> {len(b['entries'])}"
    for i, (x, y) in enumerate(zip(a["entries"], b["entries"])):
        sx = {k: v for k, v in (x.get("state") or {}).items() if k not in skip}
        sy = {k: v for k, v in (y.get("state") or {}).items() if k not in skip}
        if sx != sy:
            return f"entry {i} ({str(x.get('t'))[:70]}): {[k for k in sx if sx.get(k) != sy.get(k)]}"
    return None

def main():
    args = sys.argv[1:]
    path = args[0]; write = "--write" in args
    until = int(args[args.index("--until") + 1]) if "--until" in args else None
    src = open(path, encoding="utf-8", newline="").read()
    if not LAND_LINE.search(src): sys.exit(f"{path} has no LAND_BLOCK = 1 line: its land is already 2 x 2")
    if until:
        mark = re.search(rf"^# =+ YEAR {until} ", src, re.M) or re.search(rf"^R\({until},", src, re.M)
        if not mark: sys.exit(f"no Year {until} marker in {path}")
        src = src[:mark.start()]
    buys = purchases(src)
    n = sum(len(q) for *_, q in buys)
    before = run(src, path)
    pieces = frozenset(rc(q) for e in before["entries"] for q in ((e.get("state") or {}).get("board") or {}))
    sol = solve(buys, pieces)
    if sol is None:
        sys.exit(f"{n} squares bought{' before Year ' + str(until) if until else ''}: they don't all fit as 2 x 2 harvest squares. Try an earlier --until.")
    new = LAND_LINE.sub("", rewrite(src, sol), count=1)
    after = run(new, path)
    diff = same_play(before, after)
    moved = sum(1 for ln, old, corner in sol if rc(old) not in block(*rc(corner)))
    print(f"{n} squares re-placed; {n - moved} still cover the square originally bought, {moved} moved.")
    if diff: sys.exit(f"Play changes at {diff}: re-place by hand around it.")
    print("Replays unchanged apart from the land.")
    if write:
        open(path, "w", encoding="utf-8", newline="").write(new)
        print(f"Wrote {path}" + (f", cut at Year {until}." if until else "."))

if __name__ == "__main__":
    main()
