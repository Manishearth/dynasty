#!/usr/bin/env python3
"""Generate i-ching.html and i-ching.json: the twenty I Ching (event) cards.

Effects follow the 1969 deck; the wording and flavour lines are new.
Run from the repo root:  python3 tools/build_events.py
"""
import html
import json
import os

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

# Each entry: id, copies, title, flavour, effects (list of lines), kind
# Province 8 is the Warlord.
CARDS = [
    dict(id="drought", copies=1, kind="harvest", title="Drought",
         flavor="Not a cloud in months. The locusts, at least, are having a fine year.",
         effects=["All provinces collect an <b>average harvest</b>."]),
    dict(id="steady", copies=1, kind="harvest", title="Steady Weather",
         flavor="Neither feast nor famine. Nobody writes poems about years like this.",
         effects=["All provinces collect an <b>average harvest</b>."]),
    dict(id="bad", copies=3, kind="harvest", title="Bad Harvest",
         flavor="The seed rotted, the rains came late, and the ox went lame.",
         effects=["All provinces collect a <b>bad harvest</b>."]),
    dict(id="floods", copies=1, kind="harvest", title="Spring Floods",
         flavor="Heaven waters the land generously. In some places, far too generously.",
         effects=["Provinces 1, 3, 6, 7: <b>good harvest</b>.",
                  "Provinces 2, 4, 5, 8: <b>bad harvest</b>."]),
    dict(id="favourites", copies=1, kind="harvest", title="Heaven Has Favourites",
         flavor="Some fields shine, some fields sulk.",
         effects=["Provinces 2, 4, 5: <b>good harvest</b>.",
                  "Provinces 1, 3, 6, 7, 8: <b>bad harvest</b>."]),
    dict(id="double", copies=3, kind="population", title="Population Doubles",
         flavor="Fat years make large families.",
         effects=["All provinces collect a <b>good harvest</b>.",
                  "The population <b>doubles</b>, and every province's consumption doubles with it.",
                  "If the population is already 600 million, or the population has already doubled twice, "
                  "ignore this card except for the good harvest."]),
    dict(id="half", copies=2, kind="population", title="Population Grows by Half",
         flavor="The villages are noisier than they used to be.",
         effects=["All provinces collect a <b>good harvest</b>.",
                  "The population <b>increases by one half</b>, and so does every province's consumption.",
                  "If the population is already 600 million, or it has already grown by half once, "
                  "ignore this card except for the good harvest."]),
    dict(id="careless", copies=1, kind="disaster", title="Careless Prosperity",
         flavor="Good times make careless people.",
         effects=["All provinces collect a <b>good harvest</b>.",
                  "Every player plays a <b>Personal Disaster</b>."]),
    dict(id="even", copies=1, kind="disaster", title="Fortune and Misfortune",
         flavor="Plenty for everyone, and trouble for some.",
         effects=["All provinces collect a <b>good harvest</b>.",
                  "Provinces 2, 4, 6, 8 play a <b>Personal Disaster</b>."]),
    dict(id="storms", copies=1, kind="disaster", title="Storms and Raiders",
         flavor="A fine crop, and a fine season for gales, bandits and the Warlord's sense of humour.",
         effects=["All provinces collect a <b>good harvest</b>.",
                  "Provinces 4, 5, 6, 7 each pay <b>2 million</b> to repair their Public Works.",
                  "Provinces 1, 2, 3, 8 play a <b>Personal Disaster</b>."]),
    dict(id="canal", copies=1, kind="works", title="The Canal Gives Way",
         flavor="The engineers blame the river. The river declines to comment.",
         effects=["All provinces collect an <b>average harvest</b>.",
                  "All <b>unfinished</b> Grand Canal work is lost. In a province where both canal sections are "
                  "finished, that province pays the Emperor <b>2 million</b>. Where only one section stands, "
                  "the Emperor must build it again.",
                  "Provinces 2, 3, 7, 8 play a <b>Personal Disaster</b>."]),
    dict(id="wall", copies=1, kind="works", title="The Wall Is Breached",
         flavor="The harvest is in, and so are the horsemen from the north.",
         effects=["All provinces collect a <b>good harvest</b>.",
                  "Three Great Wall links are breached. Provinces 1, 2, 3 each pay <b>5 million</b> for repairs; "
                  "a province with no wall built above it pays <b>2 million</b> in damages to the Harvest Pile instead.",
                  "Provinces 4, 5, 6, 7, 8 play a <b>Personal Disaster</b>."]),
    dict(id="charity", copies=1, kind="money", title="Imperial Charity",
         flavor="Moved by the suffering of his people, the Emperor opens his purse. Slightly.",
         effects=["All provinces collect an <b>average harvest</b>.",
                  "Every player receives <b>2 million</b> from the Emperor's reserve."]),
    dict(id="share", copies=1, kind="money", title="The Emperor's Share",
         flavor="The Emperor would like to remind you who paid for the ditch.",
         effects=["All provinces collect an <b>average harvest</b>.",
                  "Every province with a Public Works splits the extra harvest it produces "
                  "<b>50/50</b> with the Emperor this round."]),
    dict(id="tax", copies=1, kind="money", title="Utility Tax",
         flavor="A new levy, for the upkeep of things you may or may not have.",
         effects=["All provinces collect an <b>average harvest</b>.",
                  "Every province pays the Emperor a <b>2 million</b> utility tax.",
                  "Every province with a Public Works pays <b>2 million</b> more."]),
]
assert sum(c["copies"] for c in CARDS) == 20

KIND = {"harvest": ("Harvest", "#B8860B"), "population": ("Population", "#C8291A"),
        "disaster": ("Disaster", "#6E4A2C"), "works": ("Public Works", "#3D5568"),
        "money": ("Treasury", "#2E5E4E")}

# Glyphs for the two public works the cards name
GLYPH = {"canal": "grand-canal", "wall": "great-wall"}


def strip(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def card_html(c):
    kind, col = KIND[c["kind"]]
    glyph = (f'<img class="cg" src="images/{GLYPH[c["id"]]}.svg" alt="">'
             if c["id"] in GLYPH else "")
    effects = "".join(f"<li>{e}</li>" for e in c["effects"])
    return (f'<article class="card k-{c["kind"]}">'
            f'<div class="top"><span class="kind" style="background:{col}">{kind}</span>'
            f'<span class="iching">易經</span></div>'
            f'<h3>{glyph}{html.escape(c["title"])}</h3>'
            f'<p class="flav">{html.escape(c["flavor"])}</p>'
            f'<ul>{effects}</ul>'
            f'<div class="foot">Dynasty · I Ching</div></article>')


def build():
    rows = "".join(
        f'<tr><td class="n">{c["copies"]}</td><td><b>{html.escape(c["title"])}</b>'
        f'<span class="tk" style="background:{KIND[c["kind"]][1]}"></span></td>'
        f'<td>{"<br>".join(c["effects"])}</td></tr>' for c in CARDS)
    cards = "".join(card_html(c) for c in CARDS for _ in range(c["copies"]))
    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dynasty — I Ching Cards</title>
<style>
:root{{--canvas:#E4DDCB;--paper:#fff;--ink:#16150F;--soft:#5C584A;--rule:#C9C1AC;
  --verm:#C8291A;--pink:#F2416F;--card:#F7A6BB;--mono:"Courier New",Courier,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--canvas);color:var(--ink);
  font:16px/1.55 "Helvetica Neue",Helvetica,Arial,sans-serif}}
.wrap{{max-width:60rem;margin:0 auto;padding:2rem 1rem 5rem}}
header{{background:var(--verm);color:#fff;padding:2.2rem 2rem 1.8rem;margin-bottom:1.4rem}}
header h1{{margin:0;font-size:1.9rem;letter-spacing:.14em;text-transform:uppercase}}
header p{{margin:.5rem 0 0;font-family:var(--mono);font-size:.8rem;letter-spacing:.1em;text-transform:uppercase}}
.sheet{{background:var(--paper);padding:2.4rem 2.6rem;margin-bottom:1.4rem}}
@media (max-width:640px){{.sheet{{padding:1.5rem 1.1rem}}}}
h2{{font-size:1.15rem;letter-spacing:.09em;text-transform:uppercase;margin:0 0 1rem;
  border-bottom:2px solid var(--ink);padding-bottom:.45rem}}
table{{width:100%;border-collapse:collapse;font-size:.94rem}}
th{{font:700 .72rem var(--mono);letter-spacing:.1em;text-transform:uppercase;text-align:left;
  padding:.5rem .6rem;border-bottom:2px solid var(--ink)}}
td{{padding:.6rem;border-bottom:1px solid var(--rule);vertical-align:top}}
td:nth-child(2){{width:11.5rem}}
td.n{{font-family:var(--mono);text-align:right;width:2.5rem}}
.tk{{display:inline-block;width:.6rem;height:.6rem;border-radius:50%;margin-left:.45rem}}
.legend{{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;font-size:.85rem;color:var(--soft);margin:.9rem 0 0}}
.legend span::before{{content:"";display:inline-block;width:.6rem;height:.6rem;border-radius:50%;
  margin-right:.35rem;background:var(--c)}}
.note{{color:var(--soft);font-size:.9rem}}
.deck{{display:grid;grid-template-columns:repeat(auto-fill,minmax(15.5rem,1fr));gap:1rem}}
.card{{background:var(--card);border-radius:10px;padding:.9rem 1rem .8rem;display:flex;flex-direction:column;
  min-height:20rem;box-shadow:0 1px 0 rgba(0,0,0,.2);break-inside:avoid;position:relative;
  border:1px solid rgba(0,0,0,.08)}}
.card .top{{display:flex;justify-content:space-between;align-items:center}}
.kind{{font:700 .66rem var(--mono);letter-spacing:.12em;text-transform:uppercase;color:#fff;
  padding:.18rem .45rem;border-radius:3px}}
.iching{{font-family:"Songti SC",STSong,SimSun,"Noto Serif CJK TC",serif;font-size:1.05rem;color:#8E1E2E;opacity:.75}}
.card h3{{margin:.75rem 0 .35rem;font-size:1.12rem;letter-spacing:.04em;text-transform:uppercase;line-height:1.2}}
.card h3 .cg{{width:1.05em;height:1.05em;vertical-align:-.15em;margin-right:.3em}}
.flav{{font-style:italic;font-size:.88rem;margin:0 0 .6rem;color:#4A2A30}}
.card ul{{margin:0;padding-left:1.05rem;font-size:.9rem;line-height:1.4}}
.card li{{margin:0 0 .35rem}}
.card .foot{{margin-top:auto;padding-top:.5rem;font:700 .6rem var(--mono);letter-spacing:.14em;
  text-transform:uppercase;color:#8E1E2E;opacity:.6;text-align:center}}
footer{{font-size:.8rem;color:var(--soft);text-align:center}}
@media print{{
  @page{{size:letter;margin:.2in}}
  body{{background:#fff}} header,.sheet.ref,footer,.noprint{{display:none}}
  .wrap{{max-width:none;padding:0}} .sheet{{padding:0;margin:0}}
  .deck{{grid-template-columns:repeat(3,2.5in);gap:0;justify-content:center}}
  .card{{width:2.5in;height:3.5in;min-height:0;box-shadow:none;border:1px dashed #999;border-radius:0;
    -webkit-print-color-adjust:exact;print-color-adjust:exact;padding:.12in;font-size:.9em}}
  .card ul{{font-size:.78rem}} .flav{{font-size:.74rem}} .card h3{{font-size:.92rem}}
}}
</style>
</head>
<body>
<div class="wrap">
<header><h1>I Ching Cards</h1><p>Dynasty (1969) · the twenty event cards, reworded</p></header>

<section class="sheet ref">
<h2>How they are used</h2>
<p>The Scholar shuffles all twenty cards face down at the start of the game. From Round Two on, the Scholar turns one card
at the start of every round and reads it aloud, and everyone does what it says. The deck is not reshuffled.
When a card calls for a <b>Personal Disaster</b>, each named player plays the next disaster from their own booklet, in order.
Province 8 is the Warlord.</p>
<p class="note">The cards' effects follow the original deck. The titles and the italic lines are new and are
there for flavour only. Fifteen different cards make up the deck; some come in several copies.</p>
</section>

<section class="sheet ref">
<h2>The deck at a glance</h2>
<table><thead><tr><th>Copies</th><th>Card</th><th>Effect</th></tr></thead><tbody>{rows}</tbody></table>
<div class="legend">{"".join(f'<span style="--c:{c}">{n}</span>' for n, c in KIND.values())}</div>
</section>

<section class="sheet">
<h2 class="noprint">Printable cards</h2>
<p class="note noprint">Print this page to get all twenty cards at standard playing-card size (2.5 × 3.5 in), nine to a letter sheet.
Turn on “background graphics” in the print dialog to keep the pink.</p>
<div class="deck">{cards}</div>
</section>

<footer>Unofficial fan revival. Dynasty © 1969 Onoma Productions. This text is CC BY-SA 4.0.</footer>
</div>
</body>
</html>
"""
    with open(os.path.join(OUT, "i-ching.html"), "w", encoding="utf-8") as f:
        f.write(page)
    data = [dict(c, effects=[strip(e) for e in c["effects"]]) for c in CARDS]
    with open(os.path.join(OUT, "i-ching.json"), "w", encoding="utf-8") as f:
        json.dump({"_about": "Dynasty I Ching (event) cards. 'copies' sums to 20. Province 8 is the Warlord.",
                   "cards": data}, f, indent=1, ensure_ascii=False)


if __name__ == "__main__":
    build()
