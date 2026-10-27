"""Single source for the piece glyphs (10x10 viewBox).

The realia were redrawn from photos of the original turned pieces on 2026-10-26.
`python3 tools/glyphs.py` writes one standalone SVG per piece into images/.
"""
import math
import os
import re

WALNUT, SLATE, INK = "#6E4A2C", "#3D5568", "#16150F"

GLYPHS = {
    # realia: turned walnut pieces, drawn from the originals (a squat cap with a ring and knob,
    # a scroll on its rollers, a ringed brush, a hooped barrel, a footed bowl, a turned vase)
    "customs-house": ("Customs House", WALNUT,
        "M5 3.2L5.7 4.1L4.3 4.1zM1.6 4.2L1.6 4.64L8.4 4.64L8.4 4.2z"
        "M1.79 4.96L2.2 5.3L2.5 6.1L2.5 9.2L7.5 9.2L7.5 6.1L7.8 5.3L8.21 4.96z"),
    "land-deed-scroll": ("Land Deed Scroll", WALNUT,
        "M1.34 6.65L2.12 6.2L1.64 5.38L2.16 5.08L2.36 5.43L6.69 2.93L6.49 2.58L7.01 2.28L7.48 3.1"
        "L8.26 2.65L8.66 3.35L7.88 3.8L8.36 4.62L7.84 4.92L7.64 4.57L3.31 7.07L3.51 7.42L2.99 7.72"
        "L2.52 6.9L1.74 7.35z"),
    "bamboo-brush": ("Bamboo Brush", WALNUT,
        "M8.71 7.93L8.71 7.51L8.14 6.94L6.94 8.14L7.51 8.71L7.93 8.71z"
        "M7.87 6.67L7.15 5.95L5.95 7.15L6.67 7.87zM6.88 5.68L6.16 4.96L4.96 6.16L5.68 6.88z"
        "M5.89 4.69L5.18 3.97L4.85 3.72L3.72 4.85L3.97 5.18L4.69 5.89z"
        "M4.55 3.49L1.71 1.64L1.64 1.71L3.49 4.55z"),
    "dragon-jar": ("Dragon Jar", WALNUT,
        "M3 2L2.72 2.84L7.28 2.84L7 2z"
        "M2.63 3.16L2.43 4.26L2.35 5.3L2.43 6.74L2.63 7.84L7.37 7.84L7.57 6.74L7.65 5.7L7.57 4.26"
        "L7.37 3.16z"
        "M2.72 8.16L3 9L7 9L7.28 8.16z"),
    "wooden-bowl": ("Wooden Bowl", WALNUT,
        "M1.2 3L1.21 3.39L8.79 3.39L8.8 3.34L8.8 3z"
        "M1.28 3.71L1.63 4.86L2.2 5.87L2.71 6.52L4.04 7.73L4.1 7.86L4.04 7.99L5.96 7.99L5.9 7.9"
        "L5.96 7.73L7.29 6.52L7.8 5.87L8.37 4.86L8.72 3.71z"
        "M3.6 8.31L3.55 8.42L3.5 8.9L6.5 8.9L6.45 8.42L6.4 8.31z"),
    "vase": ("Vase", WALNUT,
        "M3.65 1.3L3.63 1.71L3.72 1.82L4.07 2L4.15 2.1L4.28 2.48L4.28 2.82L4.16 3.04L3.17 3.92"
        "L2.69 4.42L2.51 4.67L2.41 4.93L2.35 5.32L2.39 5.71L2.5 6.1L2.81 6.61L4.1 8.1L4.11 8.28"
        "L3.97 8.45L3.65 9.1L6.35 9.1L6.03 8.45L5.89 8.28L5.9 8.1L7.29 6.48L7.5 6.1L7.65 5.45"
        "L7.59 4.93L7.41 4.55L6.41 3.51L5.84 3.04L5.72 2.82L5.72 2.48L5.85 2.1L5.93 2L6.28 1.82"
        "L6.37 1.71L6.35 1.3z"),
    # public works
    "great-wall":    ("Great Wall link", SLATE,
                      "M1.2 3.4h1.6v1.4h1.4V3.4h1.6v1.4h1.4V3.4h1.6V8.8H1.2z"),
    "grand-canal":   ("Grand Canal section", SLATE,
                      "M.8 2.4h8.4v1.5H.8zM.8 8.1h8.4v1.5H.8zM1.3 5.9c1.2-1 2.4-1 3.7 0s2.5 1 3.7 0v1.3c-1.2 1-2.5 1-3.7 0s-2.5-1-3.7 0z"),
    "summer-palace": ("Summer Palace", SLATE,
                      "M.6 4.8C2.6 4.6 3.9 3.6 5 2.2c1.1 1.4 2.4 2.4 4.4 2.6l-.9.9h-7zM2.2 5.9h5.6v3.2H5.8V7.2H4.2v1.9H2.2z"),
    "winter-palace": ("Winter Palace", SLATE,
                      "M2 3.6C3.4 3.4 4.3 2.6 5 1.6c.7 1 1.6 1.8 3 2l-.6.7H2.6zM3.4 4.4h3.2v1H3.4z"
                      "M.6 6.2c1.8-.2 3-.6 4.4-1.1 1.4.5 2.6.9 4.4 1.1l-.8.8H1.4zM1.8 7.1h6.4v2H5.7V8H4.3v1.1H1.8z"),
    "marble-pagoda": ("Marble Pagoda", SLATE,
                      "M4.75.5h.5v1.3h-.5zM3.2 2.7 5 1.7l1.8 1zM4 2.7h2v1H4zM2.6 4.5 5 3.6l2.4.9zM3.6 4.5h2.8v1.1H3.6z"
                      "M1.9 6.5 5 5.5l3.1 1zM3 6.5h4v2.6H3zM2.2 9.1h5.6v.6H2.2z"),
    "irrigation":    ("Irrigation System", SLATE,
                      "M5 1c1.3 1.7 1.9 2.7 1.9 3.4a1.9 1.9 0 0 1-3.8 0C3.1 3.7 3.7 2.7 5 1zM1 7h8v.9H1zM1 8.6h8v.9H1z"),
    "reservoir":     ("Reservoir", SLATE,
                      "M.8 9.2 2.4 1.8h1.5v7.4zM4.6 3.4h4.6v5.8H4.6zM5.2 5c.6-.6 1.2-.6 1.8 0s1.2.6 1.8 0v.9c-.6.6-1.2.6-1.8 0s-1.2-.6-1.8 0zM5.2 7.1c.6-.6 1.2-.6 1.8 0s1.2.6 1.8 0V8c-.6.6-1.2.6-1.8 0s-1.2-.6-1.8 0z"),
    # soldiers: a helmeted bust, plume, helmet, face and shoulders kept apart
    "soldier":       ("Soldier", INK,
                      "M5 1.2 5.55 2.7H4.45zM3.3 4.4A1.7 1.7 0 0 1 6.7 4.4zM3.8 4.75h2.4v.55a1.2 1.2 0 0 1-2.4 0z"
                      "M1.6 9.2C1.6 7.4 3 6.8 5 6.8s3.4.6 3.4 2.4z"),
}


def _points(d):
    """Points along a path (absolute or relative M L H V C S A Z), curves and arcs sampled."""
    toks = re.findall(r"[MLHVCSAZmlhvcsaz]|-?(?:\d+\.?\d*|\.\d+)", d)
    pts, i, cmd = [], 0, None
    x = y = sx = sy = 0.0
    last_c = None

    def num():
        nonlocal i
        i += 1
        return float(toks[i - 1])

    while i < len(toks):
        if toks[i].isalpha():
            cmd = toks[i]
            i += 1
            if cmd in "Zz":
                x, y = sx, sy
                last_c = None
                continue
        rel = cmd.islower()
        c = cmd.upper()
        ox, oy = (x, y) if rel else (0.0, 0.0)
        if c == "M":
            x, y = num() + ox, num() + oy
            sx, sy = x, y
            cmd = "l" if rel else "L"
            pts.append((x, y))
        elif c == "L":
            x, y = num() + ox, num() + oy
            pts.append((x, y))
        elif c == "H":
            x = num() + (x if rel else 0)
            pts.append((x, y))
        elif c == "V":
            y = num() + (y if rel else 0)
            pts.append((x, y))
        elif c in "CS":
            if c == "C":
                c1 = (num() + ox, num() + oy)
            else:
                c1 = (2 * x - last_c[0], 2 * y - last_c[1]) if last_c else (x, y)
            c2 = (num() + ox, num() + oy)
            e = (num() + ox, num() + oy)
            for k in range(1, 21):
                t = k / 20
                pts.append(tuple((1 - t) ** 3 * p0 + 3 * (1 - t) ** 2 * t * p1 + 3 * (1 - t) * t * t * p2 + t ** 3 * p3
                                 for p0, p1, p2, p3 in zip((x, y), c1, c2, e)))
            last_c = c2
            x, y = e
            continue
        elif c == "A":
            rx, ry, _, large, sweep = abs(num()), abs(num()), num(), num(), num()
            ex, ey = num() + ox, num() + oy
            # endpoint to centre parameterisation (no rotation in these glyphs)
            dx, dy = (x - ex) / 2, (y - ey) / 2
            lam = (dx / rx) ** 2 + (dy / ry) ** 2
            if lam > 1:
                rx, ry = rx * lam ** .5, ry * lam ** .5
            num_ = rx * rx * ry * ry - rx * rx * dy * dy - ry * ry * dx * dx
            co = (max(num_, 0) / (rx * rx * dy * dy + ry * ry * dx * dx)) ** .5
            if large == sweep:
                co = -co
            cx, cy = co * rx * dy / ry + (x + ex) / 2, -co * ry * dx / rx + (y + ey) / 2
            a0 = math.atan2((y - cy) / ry, (x - cx) / rx)
            a1 = math.atan2((ey - cy) / ry, (ex - cx) / rx)
            da = a1 - a0
            if sweep and da < 0:
                da += 2 * math.pi
            elif not sweep and da > 0:
                da -= 2 * math.pi
            for k in range(1, 33):
                a = a0 + da * k / 32
                pts.append((cx + rx * math.cos(a), cy + ry * math.sin(a)))
            x, y = ex, ey
        last_c = None
    return pts


def bounds(key):
    """The glyph's ink box in its 10 x 10 viewBox: (x0, y0, x1, y1)."""
    pts = _points(GLYPHS[key][2])
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    return min(xs), min(ys), max(xs), max(ys)


def inline_css(cap=.7, gap=.18):
    """CSS that sizes each glyph in running text so its ink runs from the baseline to the
    cap height (cap, in em), with its side margins trimmed to the ink plus a small gap."""
    out = []
    for k in GLYPHS:
        x0, y0, x1, y1 = bounds(k)
        h = cap * 10 / (y1 - y0)
        em = lambda v: f"{v:.3f}".rstrip("0").rstrip(".") + "em"
        out.append(f'.piece img[src$="/{k}.svg"]{{width:{em(h)};height:{em(h)};vertical-align:{em(-(10 - y1) / 10 * h)};'
                   f'margin:0 {em(gap - (10 - x1) / 10 * h)} 0 {em(-x0 / 10 * h)}}}')
    return "\n".join(out) + "\n"


def svg(key):
    name, color, d = GLYPHS[key]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10" width="40" height="40">'
            f'<title>{name}</title><path fill="{color}" fill-rule="evenodd" d="{d}"/></svg>\n')


if __name__ == "__main__":
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "images")
    os.makedirs(out, exist_ok=True)
    for k in GLYPHS:
        with open(os.path.join(out, k + ".svg"), "w", encoding="utf-8", newline="\n") as f:
            f.write(svg(k))
    print(sorted(os.listdir(out)))
