#!/usr/bin/env python3
"""Put a piece glyph (images/*.svg) in front of every mention of a piece.

Usage: python3 tools/add_glyphs.py rulebook.html
Idempotent: earlier glyph markup is stripped before it is re-added.

HTML text gets an <img> of images/<glyph>.svg. Labels inside inline SVG
diagrams can't hold an <img>, so the piece name is wrapped in a spaced-out
<tspan class="pg">, and a small script draws the glyph into that gap in the
label's own colour when the page loads.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from glyphs import GLYPHS  # noqa: E402

# (regex, glyph). Longer names come first so "Land Deed Scroll" wins over "Scroll".
TERMS = [
    (r"Reservoir / Irrigation Systems?", "reservoir"),
    (r"[Rr]eservoir systems?", "reservoir"),
    (r"(?<!three )(?<!large )[Rr]eservoirs?", "reservoir"),
    (r"[Ii]rrigation [Ss]ystems?|Irrigation", "irrigation"),
    (r"Summer Palace|SUMMER PALACE", "summer-palace"),
    (r"Winter Palace|WINTER PALACE", "winter-palace"),
    (r"Marble Pagoda|MARBLE PAGODA|(?<=the )pagoda", "marble-pagoda"),
    (r"Great Wall|GREAT WALL", "great-wall"),
    (r"Grand Canal|GRAND CANAL|canal(?!s)", "grand-canal"),
    (r"Customs Houses?|customs houses?", "customs-house"),
    (r"Land Deed Scrolls?|Land Deeds?|land deed scrolls?|Scrolls?", "land-deed-scroll"),
    (r"Bamboo Brush(?:es)?|bamboo brush(?:es)?|Brush(?:es)?", "bamboo-brush"),
    (r"Dragon Jars?|dragon jars?|Jars?", "dragon-jar"),
    (r"Wooden Bowls?|wooden bowls?|Bowls?", "wooden-bowl"),
    (r"Vases?|vases?", "vase"),
    (r"[Ss]oldiers?|SOLDIERS?", "soldier"),
]
PATTERN = re.compile(r"\b(?:" + "|".join(f"(?P<g{i}>{t})" for i, (t, _) in enumerate(TERMS)) + r")\b")

CSS = ("\n/* ---------- piece glyphs ---------- */\n"
       ".piece{white-space:nowrap}\n"
       ".piece img{width:1.05em;height:1.05em;margin-right:.18em;vertical-align:-.17em}\n")

SKIP = re.compile(r"(<head\b.*?</head>|<svg\b.*?</svg>|<script\b.*?</script>|<style\b.*?</style>)",
                  re.S | re.I)
OLD = re.compile(r'<span class="piece"><img src="images/[a-z-]+\.svg" alt="">(.*?)</span>')
OLD_SVG = re.compile(r'<tspan class="pg" data-g="[a-z-]+" dx="1.1em">(.*?)</tspan>')
OLD_JS = re.compile(r'\n?<script id="piece-glyphs">.*?</script>\n?', re.S)
SVG_TEXT = re.compile(r"(<text\b[^>]*>)(.*?)(</text>)", re.S)

JS = """
<script id="piece-glyphs">
(function(){
var G=%s;
function run(){
  document.querySelectorAll('svg tspan.pg').forEach(function(t){
    var txt=t.closest('text'), p;
    var cs=getComputedStyle(t), s=parseFloat(cs.fontSize)||12, ls=parseFloat(cs.letterSpacing)||0;
    if(ls)t.setAttribute('dx',s*1.1+ls*2);
    try{p=t.getStartPositionOfChar(0);}catch(e){return;}
    var g=document.createElementNS('http://www.w3.org/2000/svg','path');
    g.setAttribute('d',G[t.getAttribute('data-g')]);
    g.setAttribute('fill-rule','evenodd');
    g.setAttribute('fill',getComputedStyle(txt).fill);
    g.setAttribute('transform','translate('+(p.x-s*1.02-2*ls)+','+(p.y-s*0.8)+') scale('+(s*0.09)+')');
    txt.parentNode.insertBefore(g,txt);
  });
}
if(document.readyState!=='loading')run();else document.addEventListener('DOMContentLoaded',run);
})();
</script>
"""


def js_terms():
    """TERMS as JSON for pages that add glyphs in the browser (the playthrough).
    A third element of true marks a piece whose name is capitalised with its glyph."""
    return json.dumps([[t, g, g in CAPITALISE] for t, g in TERMS])


def glyph_of(m):
    for i, (_, glyph) in enumerate(TERMS):
        if m.group(f"g{i}"):
            return glyph


# Pieces whose name is always capitalised where it carries a glyph ("Reservoir").
CAPITALISE = {"reservoir"}


def shown(m):
    t = m.group(0)
    return t[0].upper() + t[1:] if glyph_of(m) in CAPITALISE else t


def tag(m):
    return f'<span class="piece"><img src="images/{glyph_of(m)}.svg" alt="">{shown(m)}</span>'


def svg_tag(m):
    return f'<tspan class="pg" data-g="{glyph_of(m)}" dx="1.1em">{shown(m)}</tspan>'


def svg_text(chunk):
    def one(t):
        parts = re.split(r"(<[^>]+>)", t.group(2))
        body = "".join(p if p.startswith("<") else PATTERN.sub(svg_tag, p) for p in parts)
        return t.group(1) + body + t.group(3)
    return SVG_TEXT.sub(one, chunk)


def text_only(chunk):
    # split into tags and text; rewrite text only
    parts = re.split(r"(<[^>]+>)", chunk)
    return "".join(p if p.startswith("<") else PATTERN.sub(tag, p) for p in parts)


def main(path):
    s = open(path, encoding="utf-8").read()
    s = OLD.sub(r"\1", s)
    s = OLD_SVG.sub(r"\1", s)
    s = OLD_JS.sub("", s)
    if "piece glyphs" not in s:
        s = s.replace("</style>", CSS + "</style>", 1)
    pieces = SKIP.split(s)
    s = "".join(svg_text(p) if p[:4].lower() == "<svg" else
                p if SKIP.fullmatch(p) else text_only(p) for p in pieces)
    if 'class="pg"' in s:
        js = JS % json.dumps({k: d for k, (_, _, d) in GLYPHS.items()})
        s = s.replace("</body>", js + "</body>", 1) if "</body>" in s else s + js
    open(path, "w", encoding="utf-8", newline="\n").write(s)
    counts = {}
    for g in re.findall(r'images/([a-z-]+)\.svg|data-g="([a-z-]+)"', s):
        g = g[0] or g[1]
        counts[g] = counts.get(g, 0) + 1
    print(counts)


if __name__ == "__main__":
    main(sys.argv[1])
