#!/usr/bin/env python3
"""Generate map.svg and map.json for the Dynasty revival.

The board is a 30 x 22 grid of squares. All geometry below is given in grid
units: (0, 0) is the top-left corner of the board, x grows east, y grows south.
Features were measured from a photo of a 1969 copy and then redrawn; nothing
here is traced artwork.

Run from the repo root:  python3 tools/build_map.py
Pure Python, no dependencies.
"""

import json
import math
import os

COLS, ROWS = 30, 22
CELL = 40                    # px per square
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 70, 150, 150
OUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# --------------------------------------------------------------------------
# Geography (grid units)
# --------------------------------------------------------------------------

# The northern river: rises in the west, loops north around Province 2,
# then runs east between Provinces 1 and 4 to the sea.
NORTH_RIVER = [(7.1, 9.2), (6.3, 8.2), (6.7, 7.6), (7.8, 7.5), (9.6, 7.3),
               (10.4, 6.6), (11.7, 5.4), (12.5, 4.0), (13.1, 2.7), (14.0, 2.35),
               (15.3, 2.7), (16.2, 3.3), (16.1, 4.4), (15.95, 5.6), (16.0, 7.4),
               (16.0, 8.85), (16.4, 8.65), (18.1, 8.7), (20.0, 8.85), (21.5, 9.2),
               (22.8, 9.8), (23.75, 10.05)]

# The southern river: rises in the west, runs east between Province 4 and
# Provinces 5 / 7 to the sea.
SOUTH_RIVER = [(6.2, 17.7), (6.4, 18.5), (7.0, 18.3), (7.6, 18.7), (8.4, 18.2),
               (8.6, 17.2), (8.5, 16.2), (9.1, 15.7), (10.2, 15.65), (11.5, 15.2),
               (12.3, 14.5), (13.5, 13.8), (14.2, 13.0), (15.0, 12.8), (16.1, 12.95),
               (17.3, 14.0), (17.9, 14.35), (18.6, 13.9), (19.0, 13.35), (19.6, 13.4),
               (20.5, 14.05), (21.4, 13.7), (22.5, 12.7), (23.5, 11.45), (24.5, 11.7)]

# Coastline, north to south. The sea lies to the east.
COAST = [(27.2, 0.0), (26.9, 0.7), (25.5, 2.1), (24.3, 2.45), (23.9, 3.3),
         (22.7, 4.0), (21.8, 4.35), (21.7, 4.85), (22.2, 5.6), (23.4, 6.3),
         (24.0, 6.0), (24.4, 5.6), (25.3, 5.45), (25.9, 5.6), (26.3, 6.1),
         (26.1, 6.5), (25.6, 6.55), (25.1, 7.0), (24.7, 7.1), (24.3, 7.4),
         (23.9, 8.3), (23.6, 9.0), (23.75, 10.05), (24.1, 10.4), (24.6, 11.0),
         (24.5, 11.7), (25.1, 12.0), (25.4, 12.7), (25.0, 13.4), (24.7, 13.6),
         (25.4, 13.5), (26.0, 14.0), (26.3, 14.5), (26.0, 15.3), (25.7, 15.9),
         (25.3, 16.1), (25.0, 16.5), (24.6, 17.1), (24.4, 17.5), (24.2, 17.9),
         (24.5, 18.5), (24.6, 19.0), (24.0, 19.5), (23.5, 20.0), (23.0, 20.4),
         (22.2, 21.2), (21.7, 21.6), (21.3, 22.0)]

# Great Wall: twelve links, west to east. Links 1-4 stand above Province 3,
# 5-8 above Province 2 and 9-12 above Province 1.
WALL_LINKS = [((2.6, 5.5), (3.2, 4.7)), ((3.5, 4.4), (4.6, 3.4)),
              ((5.1, 3.0), (6.4, 3.3)), ((6.7, 3.7), (8.1, 4.3)),
              ((8.6, 4.7), (10.1, 4.5)), ((10.4, 4.3), (11.8, 4.1)),
              ((12.6, 3.7), (14.1, 3.4)), ((14.3, 3.4), (15.4, 2.8)),
              ((15.8, 2.4), (17.2, 1.8)), ((17.4, 2.0), (18.7, 1.8)),
              ((19.4, 1.9), (20.7, 2.3)), ((21.7, 2.2), (23.3, 2.5))]

# Grand Canal: eight sections, two in each of Provinces 1, 4, 5 and 6.
CANAL_SECTIONS = [
    ("1", [(20.7, 6.2), (21.0, 7.6)]),
    ("1", [(21.0, 7.6), (21.45, 9.1)]),
    ("4", [(21.75, 9.6), (22.3, 10.3)]),
    ("4", [(22.3, 10.3), (22.75, 11.2)]),
    ("5", [(21.6, 13.75), (22.35, 14.6)]),
    ("5", [(22.35, 14.6), (22.5, 15.9)]),
    ("6", [(22.5, 16.1), (22.3, 17.3)]),
    ("6", [(22.3, 17.3), (22.6, 18.6)]),
]

# Province outlines. Where a river forms a border the outline follows it.
def _slice(path, a, b):
    """Points of `path` from index a to b inclusive (reversed if a > b)."""
    return path[a:b + 1] if a <= b else list(reversed(path[b:a + 1]))

NR, SR, CO = NORTH_RIVER, SOUTH_RIVER, COAST
PROVINCES = {
    "1": [(16.0, 5.0), (21.75, 5.0)] + _slice(CO, 8, 22) + _slice(NR, 21, 14) + [(16.0, 5.0)],
    "2": [(11.0, 6.0), (16.0, 6.0), (16.0, 10.0),
          (11.0, 10.0), (11.0, 7.0), (10.5, 6.8)],
    "3": [(7.1, 9.2), (7.6, 9.4), (7.6, 12.8), (12.7, 12.9), (13.9, 12.4),
          (18.0, 12.4), (18.0, 8.7), (16.4, 8.65), (16.0, 8.85), (16.0, 10.0),
          (11.0, 10.0), (11.0, 7.0), (10.5, 6.8)] + _slice(NR, 4, 0),
    "4": [(18.0, 8.7), (20.0, 8.85), (21.5, 9.2), (22.8, 9.8)]
         + _slice(CO, 22, 25) + _slice(SR, 23, 16) + [(18.0, 14.2)],
    "5": [(18.0, 14.2)] + _slice(SR, 16, 24) + _slice(CO, 26, 36)
         + [(18.0, 16.0)],
    "6": [(18.0, 16.0)] + _slice(CO, 36, 42) + [(24.35, 19.0), (18.0, 19.0)],
    "7": [(12.0, 15.6), (12.8, 14.8), (13.8, 14.0), (16.4, 14.0), (18.0, 15.2),
          (18.0, 19.0), (12.0, 19.0)],
}

# Two sides of the Great Wall: everything north of this line is beyond it.
WALL_LINE = [(0, 6.2), (2.6, 5.5)] + [p for link in WALL_LINKS for p in link] \
            + [(26.0, 2.3), (30, 2.3)]

ROLE = {
    "1": ("Emperor", "皇帝"), "2": ("Official", "官員"),
    "3": ("Gentry", "士紳"), "4": ("Scholar", "學者"),
    "5": ("Silk Peasant", "蠶農"), "6": ("Rice Peasant", "稻農"),
    "7": ("Wheat Peasant", "麥農"),
}
# Hand-placed label anchors (grid units), tuned to sit clear of rivers.
LABEL_AT = {"1": (18.4, 6.6), "2": (13.2, 8.0), "3": (11.4, 11.3),
            "4": (19.8, 11.4), "5": (19.5, 15.4), "6": (19.9, 17.6),
            "7": (14.8, 16.9)}

TINT = {"1": "#E9B949", "2": "#E3A08A", "3": "#B9C98F", "4": "#9FBBD3",
        "5": "#D9A9C3", "6": "#A9CDB8", "7": "#E6CC8F"}

# --------------------------------------------------------------------------
# Geometry helpers
# --------------------------------------------------------------------------

def inside(pt, poly):
    x, y = pt
    hit = False
    for i in range(len(poly)):
        (x1, y1), (x2, y2) = poly[i], poly[(i + 1) % len(poly)]
        if (y1 > y) != (y2 > y):
            if x < x1 + (y - y1) * (x2 - x1) / (y2 - y1):
                hit = not hit
    return hit


def interp_x(path, y):
    """x of the first crossing of horizontal line y by a polyline, or None."""
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        if min(y1, y2) <= y <= max(y1, y2) and y1 != y2:
            return x1 + (y - y1) * (x2 - x1) / (y2 - y1)
    return None


def interp_y(path, x):
    for (x1, y1), (x2, y2) in zip(path, path[1:]):
        if min(x1, x2) <= x <= max(x1, x2) and x1 != x2:
            return y1 + (x - x1) * (y2 - y1) / (x2 - x1)
    return None


def classify(cx, cy):
    """Region code for the square whose centre is (cx, cy)."""
    for code, poly in PROVINCES.items():
        if inside((cx, cy), poly):
            return code
    # Sea: east of the coastline at this row (the coast spans every row).
    cxo = interp_x(COAST, cy)
    if cxo is not None and cx > cxo:
        return "S"
    wy = interp_y(WALL_LINE, cx)
    if wy is not None and cy < wy:
        return "B"                          # beyond the Great Wall
    if cy < 7.0 and cx > 7.6:
        return "n"                          # the strip below the Wall
    return "8"                              # the Warlord's undeveloped land


def grid():
    g = [[classify(c + .5, r + .5) for c in range(COLS)] for r in range(ROWS)]
    # Tidy squares that a river or the coast left stranded: a square with no
    # same-region neighbour joins the most common neighbouring province.
    for _ in range(3):
        for r in range(ROWS):
            for c in range(COLS):
                ch = g[r][c]
                if ch in "BS":
                    continue
                nb = [g[rr][cc] for rr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1))
                      if 0 <= rr < ROWS and 0 <= cc < COLS]
                if ch in nb:
                    continue
                provs = [x for x in nb if x in "1234567"]
                if provs:
                    g[r][c] = max(set(provs), key=provs.count)
    return ["".join(row) for row in g]


def px(p):
    return (MARGIN_X + p[0] * CELL, MARGIN_TOP + p[1] * CELL)


def smooth(points, closed=False, tension=0.5):
    """Catmull-Rom spline through grid points, as an SVG path string."""
    P = [px(p) for p in points]
    if len(P) < 3:
        return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in P)
    d = f"M{P[0][0]:.1f},{P[0][1]:.1f}"
    n = len(P)
    rng = range(n) if closed else range(n - 1)
    for i in rng:
        p0 = P[(i - 1) % n] if (closed or i > 0) else P[0]
        p1, p2 = P[i], P[(i + 1) % n]
        p3 = P[(i + 2) % n] if (closed or i + 2 < n) else P[-1]
        c1 = (p1[0] + (p2[0] - p0[0]) * tension / 3, p1[1] + (p2[1] - p0[1]) * tension / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * tension / 3, p2[1] - (p3[1] - p1[1]) * tension / 3)
        d += f" C{c1[0]:.1f},{c1[1]:.1f} {c2[0]:.1f},{c2[1]:.1f} {p2[0]:.1f},{p2[1]:.1f}"
    return d + (" Z" if closed else "")


def col_label(c):
    return str(c + 1)


def row_label(r):
    return chr(ord("A") + r)

# --------------------------------------------------------------------------
# SVG
# --------------------------------------------------------------------------

def build_svg(g):
    W = MARGIN_X * 2 + COLS * CELL
    H = MARGIN_TOP + ROWS * CELL + MARGIN_BOTTOM
    x0, y0 = MARGIN_X, MARGIN_TOP
    x1, y1 = x0 + COLS * CELL, y0 + ROWS * CELL
    out = []
    a = out.append
    a(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
      f'width="{W}" height="{H}" role="img" '
      f'aria-label="Map of Dynasty: seven provinces on a {COLS} by {ROWS} grid">')
    a("""<defs>
  <filter id="paper" x="0" y="0" width="100%" height="100%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="3" seed="7" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0.45  0 0 0 0 0.36  0 0 0 0 0.22  0 0 0 0.10 0"/>
    <feComposite in2="SourceGraphic" operator="in"/>
    <feBlend in="SourceGraphic" mode="multiply"/>
  </filter>
  <filter id="soft" x="-5%" y="-5%" width="110%" height="110%">
    <feGaussianBlur stdDeviation="2.2"/>
  </filter>
  <pattern id="waves" width="34" height="18" patternUnits="userSpaceOnUse">
    <path d="M0 12 q8.5 -7 17 0 t17 0" fill="none" stroke="#5E8FA8" stroke-width="1.1" opacity=".45"/>
  </pattern>
  <pattern id="steppe" width="16" height="16" patternUnits="userSpaceOnUse" patternTransform="rotate(35)">
    <line x1="0" y1="0" x2="0" y2="16" stroke="#B59B6E" stroke-width="1" opacity=".35"/>
  </pattern>
  <pattern id="dunes" width="46" height="30" patternUnits="userSpaceOnUse">
    <path d="M4 20 q9 -8 18 0 M26 8 q7 -6 14 0" fill="none" stroke="#9C7F52" stroke-width="1.1" opacity=".5"/>
  </pattern>
  <pattern id="dots" width="10" height="10" patternUnits="userSpaceOnUse">
    <circle cx="5" cy="5" r=".9" fill="#9C7F52" opacity=".45"/>
  </pattern>
</defs>""")
    a('<style>'
      '.t{font-family:"Palatino Linotype",Palatino,"Book Antiqua",Georgia,serif;fill:#3B2E1E}'
      '.h{font-family:"Songti SC","STSong","SimSun","Noto Serif CJK TC","Noto Serif CJK SC",serif;fill:#7A2E1E}'
      '</style>')

    # Page and board backgrounds
    a(f'<rect width="{W}" height="{H}" fill="#EFE4CB"/>')
    a(f'<rect width="{W}" height="{H}" fill="#EFE4CB" filter="url(#paper)"/>')

    # Region fills, square by square
    base = {"B": "#DCC9A2", "8": "#EADCBD", "n": "#EEE3C8", "S": "#EADCBD"}
    over = {"B": "url(#dunes)", "8": "url(#steppe)", "n": "url(#dots)"}
    for r, row in enumerate(g):
        for c, ch in enumerate(row):
            x, y = x0 + c * CELL, y0 + r * CELL
            shown = ch
            if ch == "S":   # sea squares the coastline cuts: show the land part in the neighbour's colour
                for rr, cc in ((r, c - 1), (r - 1, c), (r + 1, c), (r, c + 1)):
                    if 0 <= rr < ROWS and 0 <= cc < COLS and g[rr][cc] in TINT:
                        shown = g[rr][cc]
                        break
            fill = TINT.get(shown) or base[shown]
            op = ' fill-opacity=".62"' if shown in TINT else ""
            a(f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" fill="{fill}"{op}/>')
    for code, pat in over.items():
        for r, row in enumerate(g):
            for c, ch in enumerate(row):
                if ch == code:
                    a(f'<rect x="{x0 + c * CELL}" y="{y0 + r * CELL}" width="{CELL}" height="{CELL}" fill="{pat}"/>')

    # Sea: a smooth shape east of the coast, laid over the squares
    coast_d = smooth(COAST)
    sea_d = coast_d + f" L{x1},{y1} L{x1},{y0} Z"
    a(f'<clipPath id="seaclip"><path d="{sea_d}"/></clipPath>')
    a(f'<path d="{sea_d}" fill="#C9DDE3"/>')
    a(f'<path d="{sea_d}" fill="url(#waves)"/>')
    a(f'<g clip-path="url(#seaclip)"><path d="{coast_d}" fill="none" stroke="#6F9FB6" '
      f'stroke-width="22" opacity=".35" filter="url(#soft)"/></g>')
    for k, (dx, op) in enumerate([(9, .45), (17, .3), (26, .18)]):
        a('<g clip-path="url(#seaclip)">')
        shifted = [(x + dx / CELL, y) for x, y in COAST]
        a(f'<path d="{smooth(shifted)}" fill="none" stroke="#4E7F98" stroke-width="1" '
          f'stroke-dasharray="{6 + 4 * k} {5 + 3 * k}" opacity="{op}"/>')
        a('</g>')

    # Grid
    for c in range(COLS + 1):
        x = x0 + c * CELL
        a(f'<line x1="{x}" y1="{y0}" x2="{x}" y2="{y1}" stroke="#5B4A33" stroke-width=".8" opacity=".38"/>')
    for r in range(ROWS + 1):
        y = y0 + r * CELL
        a(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="#5B4A33" stroke-width=".8" opacity=".38"/>')

    # Province borders: dotted ink along square edges between different provinces
    def is_prov(ch):
        return ch in TINT
    segs = []
    for r in range(ROWS):
        for c in range(COLS):
            ch = g[r][c]
            if c + 1 < COLS and g[r][c + 1] != ch and (is_prov(ch) or is_prov(g[r][c + 1])) \
                    and "S" not in (ch, g[r][c + 1]):
                X = x0 + (c + 1) * CELL
                segs.append((X, y0 + r * CELL, X, y0 + (r + 1) * CELL))
            if r + 1 < ROWS and g[r + 1][c] != ch and (is_prov(ch) or is_prov(g[r + 1][c])) \
                    and "S" not in (ch, g[r + 1][c]):
                Y = y0 + (r + 1) * CELL
                segs.append((x0 + c * CELL, Y, x0 + (c + 1) * CELL, Y))
    a('<g stroke="#3B2E1E" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="0.1 6" fill="none">')
    for s in segs:
        a(f'<line x1="{s[0]}" y1="{s[1]}" x2="{s[2]}" y2="{s[3]}"/>')
    a('</g>')

    # Coastline itself
    a(f'<path d="{coast_d}" fill="none" stroke="#2F5D75" stroke-width="3.2" stroke-linejoin="round"/>')

    # Rivers: dark bank, light water
    for river in (NORTH_RIVER, SOUTH_RIVER):
        d = smooth(river)
        a(f'<path d="{d}" fill="none" stroke="#2F6C92" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>')
        a(f'<path d="{d}" fill="none" stroke="#8CC3DD" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')

    # Grand Canal: towpath double line with section ticks and numbers
    a('<g>')
    for i, (prov, pts) in enumerate(CANAL_SECTIONS, 1):
        d = smooth(pts)
        a(f'<path d="{d}" fill="none" stroke="#2E5E4E" stroke-width="7" stroke-linecap="butt"/>')
        a(f'<path d="{d}" fill="none" stroke="#9CCFC0" stroke-width="3" stroke-linecap="butt"/>')
        (ax, ay), (bx, by) = px(pts[0]), px(pts[-1])
        L = math.hypot(bx - ax, by - ay)
        nx, ny = -(by - ay) / L, (bx - ax) / L
        for (tx, ty) in ((ax, ay), (bx, by)):
            a(f'<line x1="{tx - nx * 7:.1f}" y1="{ty - ny * 7:.1f}" x2="{tx + nx * 7:.1f}" '
              f'y2="{ty + ny * 7:.1f}" stroke="#2E5E4E" stroke-width="2"/>')
        mx, my = (ax + bx) / 2, (ay + by) / 2
        a(f'<g transform="translate({mx + nx * 15:.1f},{my + ny * 15:.1f})">'
          f'<circle r="8" fill="#F6EEDC" stroke="#2E5E4E" stroke-width="1.2"/>'
          f'<text class="t" font-size="10" font-weight="bold" text-anchor="middle" dy="3.5" '
          f'style="fill:#2E5E4E">{i}</text></g>')
    a('</g>')

    # Great Wall: rampart with crenellations on the north face
    a('<g>')
    for i, ((ax, ay), (bx, by)) in enumerate(WALL_LINKS, 1):
        (X1, Y1), (X2, Y2) = px((ax, ay)), px((bx, by))
        L = math.hypot(X2 - X1, Y2 - Y1)
        ux, uy = (X2 - X1) / L, (Y2 - Y1) / L
        nx, ny = uy, -ux                        # points "north-ish"
        if ny > 0:
            nx, ny = -nx, -ny
        a(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="#6B4B2E" stroke-width="9" stroke-linecap="square"/>')
        a(f'<line x1="{X1:.1f}" y1="{Y1:.1f}" x2="{X2:.1f}" y2="{Y2:.1f}" stroke="#C9A877" stroke-width="5" stroke-linecap="square"/>')
        k, t = 0, 2.0
        while t + 4 <= L:
            cx, cy = X1 + ux * t + nx * 6.5, Y1 + uy * t + ny * 6.5
            a(f'<rect x="-2" y="-2.5" width="4" height="5" fill="#6B4B2E" '
              f'transform="translate({cx:.1f},{cy:.1f}) rotate({math.degrees(math.atan2(uy, ux)):.1f})"/>')
            t += 7
            k += 1
        mx, my = (X1 + X2) / 2 - nx * 15, (Y1 + Y2) / 2 - ny * 15
        a(f'<text class="t" x="{mx:.1f}" y="{my + 4:.1f}" font-size="11" font-weight="bold" '
          f'text-anchor="middle" style="fill:#6B4B2E">{i}</text>')
    a('</g>')
    a(f'<text class="t" x="{px((12.5, 1.05))[0]:.1f}" y="{px((12.5, 1.05))[1]:.1f}" font-size="15" '
      f'letter-spacing="9" text-anchor="middle" font-style="italic" style="fill:#6B4B2E">THE GREAT WALL</text>')

    # Region labels
    for code, (lx, ly) in LABEL_AT.items():
        X, Y = px((lx, ly))
        name, han = ROLE[code]
        a(f'<g transform="translate({X:.1f},{Y:.1f})">'
          f'<rect x="-62" y="-32" width="124" height="58" rx="3" fill="#F6EEDC" fill-opacity=".86" '
          f'stroke="#3B2E1E" stroke-width="1"/>'
          f'<rect x="-58" y="-28" width="116" height="50" rx="2" fill="none" stroke="#3B2E1E" stroke-width=".5"/>'
          f'<text class="t" y="-7" font-size="12" letter-spacing="3" text-anchor="middle">PROVINCE {code}</text>'
          f'<text class="t" y="12" font-size="15" font-weight="bold" font-style="italic" text-anchor="middle">{name}</text>'
          f'<g transform="translate(62,-32)"><rect x="-10" y="-10" width="20" height="20" fill="#B5321F"/>'
          f'<text class="t" y="5" font-size="14" font-weight="bold" text-anchor="middle" style="fill:#F6EEDC">{code}</text></g>'
          f'</g>')
    for (lx, ly), lines, size in [((3.9, 11.6), ["UNDEVELOPED LAND", "the Warlord’s territory"], 15),
                                  ((3.0, 2.0), ["BEYOND THE WALL"], 12),
                                  ((27.6, 9.0), ["THE", "EASTERN", "SEA"], 15)]:
        X, Y = px((lx, ly))
        for k, line in enumerate(lines):
            italic = ' font-style="italic"' if k and lines[0] != "THE" else ""
            fs = size if k == 0 or lines[0] == "THE" else size - 2
            a(f'<text class="t" x="{X:.1f}" y="{Y + k * (size + 6):.1f}" font-size="{fs}" letter-spacing="3" '
              f'text-anchor="middle"{italic} opacity=".8">{line}</text>')
    X, Y = px((3.9, 12.8))
    a(f'<text class="h" x="{X:.1f}" y="{Y + 12:.1f}" font-size="20" text-anchor="middle" opacity=".7">軍閥</text>')

    # Coordinates
    for c in range(COLS):
        X = x0 + c * CELL + CELL / 2
        for Y in (y0 - 10, y1 + 21):
            a(f'<text class="t" x="{X}" y="{Y}" font-size="12" text-anchor="middle" opacity=".75">{col_label(c)}</text>')
    for r in range(ROWS):
        Y = y0 + r * CELL + CELL / 2 + 4
        for X in (x0 - 14, x1 + 14):
            a(f'<text class="t" x="{X}" y="{Y}" font-size="12" text-anchor="middle" opacity=".75">{row_label(r)}</text>')

    # Frame
    a(f'<rect x="{x0 - 28}" y="{y0 - 28}" width="{x1 - x0 + 56}" height="{y1 - y0 + 56}" '
      f'fill="none" stroke="#3B2E1E" stroke-width="3"/>')
    a(f'<rect x="{x0 - 34}" y="{y0 - 34}" width="{x1 - x0 + 68}" height="{y1 - y0 + 68}" '
      f'fill="none" stroke="#3B2E1E" stroke-width="1"/>')
    a(f'<rect x="{x0}" y="{y0}" width="{x1 - x0}" height="{y1 - y0}" fill="none" stroke="#3B2E1E" stroke-width="1.6"/>')
    for (cx, cy) in [(x0 - 31, y0 - 31), (x1 + 31, y0 - 31), (x0 - 31, y1 + 31), (x1 + 31, y1 + 31)]:
        a(f'<rect x="{cx - 9}" y="{cy - 9}" width="18" height="18" fill="#B5321F" transform="rotate(45 {cx} {cy})"/>')

    # Title block
    a(f'<text class="t" x="{x0 - 34}" y="62" font-size="46" letter-spacing="14" font-weight="bold">DYNASTY</text>')
    a(f'<text class="h" x="{x0 + 318}" y="60" font-size="34">王朝</text>')
    a(f'<text class="t" x="{x0 - 32}" y="92" font-size="15" font-style="italic">'
      f'The Seven Provinces — a redrawn board for the 1969 game, {COLS} × {ROWS} squares</text>')

    # Compass
    cx, cy = x1 + 4, 72
    a(f'<g transform="translate({cx},{cy})">'
      f'<circle r="30" fill="none" stroke="#3B2E1E" stroke-width="1"/>'
      f'<circle r="25" fill="none" stroke="#3B2E1E" stroke-width=".5"/>'
      f'<path d="M0,-27 L6,0 L0,27 L-6,0Z" fill="#3B2E1E"/>'
      f'<path d="M-27,0 L0,5 L27,0 L0,-5Z" fill="#8A7658"/>'
      f'<path d="M0,-27 L6,0 L-6,0Z" fill="#B5321F"/>'
      f'<text class="t" y="-36" font-size="13" font-weight="bold" text-anchor="middle">N</text></g>')

    # Legend
    ly = y1 + 62
    items = []
    lx = x0 - 30
    a(f'<g transform="translate({lx},{ly})">')
    # river
    a('<path d="M0,10 q15,-12 30,0 t30,0" fill="none" stroke="#2F6C92" stroke-width="8" stroke-linecap="round"/>'
      '<path d="M0,10 q15,-12 30,0 t30,0" fill="none" stroke="#8CC3DD" stroke-width="3" stroke-linecap="round"/>'
      '<text class="t" x="72" y="9" font-size="14">River</text>'
      '<text class="t" x="72" y="26" font-size="12" font-style="italic">the Warlord pays a toll to cross</text>')
    # wall
    a('<g transform="translate(285,0)">'
      '<line x1="0" y1="12" x2="58" y2="12" stroke="#6B4B2E" stroke-width="9"/>'
      '<line x1="0" y1="12" x2="58" y2="12" stroke="#C9A877" stroke-width="5"/>'
      + "".join(f'<rect x="{2 + 7 * k}" y="2" width="4" height="5" fill="#6B4B2E"/>' for k in range(8)) +
      '<text class="t" x="72" y="9" font-size="14">Great Wall link</text>'
      '<text class="t" x="72" y="26" font-size="12" font-style="italic">12 links, 4 above each of Provinces 3, 2, 1</text></g>')
    # canal
    a('<g transform="translate(615,0)">'
      '<line x1="0" y1="12" x2="58" y2="12" stroke="#2E5E4E" stroke-width="7"/>'
      '<line x1="0" y1="12" x2="58" y2="12" stroke="#9CCFC0" stroke-width="3"/>'
      '<line x1="0" y1="5" x2="0" y2="19" stroke="#2E5E4E" stroke-width="2"/>'
      '<line x1="58" y1="5" x2="58" y2="19" stroke="#2E5E4E" stroke-width="2"/>'
      '<text class="t" x="72" y="9" font-size="14">Grand Canal section</text>'
      '<text class="t" x="72" y="26" font-size="12" font-style="italic">8 sections, 2 each in Provinces 1, 4, 5, 6</text></g>')
    # border
    a('<g transform="translate(945,0)">'
      '<line x1="0" y1="12" x2="58" y2="12" stroke="#3B2E1E" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="0.1 6"/>'
      '<text class="t" x="72" y="9" font-size="14">Province border</text>'
      '<text class="t" x="72" y="26" font-size="12" font-style="italic">squares are named row + column, e.g. H12</text></g>')
    a('</g>')
    a(f'<text class="t" x="{x0 - 34}" y="{H - 22}" font-size="11" opacity=".7">'
      f'Unofficial fan redraw. Dynasty © 1969 Onoma Productions; this drawing is CC BY-SA 4.0.</text>')
    a('</svg>')
    return "\n".join(out)


def main():
    g = grid()
    svg = build_svg(g)
    with open(os.path.join(OUT_DIR, "map.svg"), "w", encoding="utf-8") as f:
        f.write(svg)
    data = {
        "_about": "Dynasty board, square by square. Rows A-V top to bottom, "
                  "columns 1-30 west to east; a square is named like 'H12'.",
        "cols": COLS, "rows": ROWS,
        "legend": {"1": "Province 1 (Emperor)", "2": "Province 2 (Official)",
                   "3": "Province 3 (Gentry)", "4": "Province 4 (Scholar)",
                   "5": "Province 5 (Silk Peasant)", "6": "Province 6 (Rice Peasant)",
                   "7": "Province 7 (Wheat Peasant)",
                   "8": "Undeveloped land: the Warlord's territory",
                   "n": "Undeveloped land: the strip below the Great Wall",
                   "B": "Beyond the Great Wall", "S": "The sea"},
        "grid": g,
        "great_wall_links": [{"link": i, "above_province": "3" if i <= 4 else "2" if i <= 8 else "1",
                              "from": a, "to": b} for i, (a, b) in enumerate(WALL_LINKS, 1)],
        "grand_canal_sections": [{"section": i, "province": p, "path": pts}
                                 for i, (p, pts) in enumerate(CANAL_SECTIONS, 1)],
        "rivers": {"north": NORTH_RIVER, "south": SOUTH_RIVER},
        "coast": COAST,
        "_geometry_units": "Paths are in grid units: (0,0) is the board's top-left corner, "
                           "one unit per square.",
    }
    with open(os.path.join(OUT_DIR, "map.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, indent=1, ensure_ascii=False)
    print("\n".join(g))
    counts = {}
    for row in g:
        for ch in row:
            counts[ch] = counts.get(ch, 0) + 1
    print(dict(sorted(counts.items())))


if __name__ == "__main__":
    main()
