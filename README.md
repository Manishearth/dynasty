# Dynasty (1969)

This contains a recreation of the 1969 board game "Dynasty".

The original scans can be found on https://manishearth.net/dynasty/.

## What's here

| File | What it is |
|---|---|
| `index.html` | The landing page: links to everything below and to the original scans |
| `rulebook.html` | The rules, rewritten as one modern rulebook |
| `RULINGS.md` | Every rules question settled so far, with reasons. Add yours here |
| `playthrough.html` | Annotated games played by AI agents, one to a seat; their records are in `playthroughs/` |
| `playthrough-scripted.html` | The older scripted playthroughs: seven example games, each written start to finish by one author: two at eight players, a four-player short game, a five-player peasant game, two six-player games and a seven-player game |
| `map.svg` | The board, redrawn: seven provinces on a 30 × 22 grid (rows A–V, columns 1–30). Drawn as named layers, so Inkscape can show or hide each one |
| `map-board.svg` | The board's ground alone, without frame, labels or printed works, for pages that draw on top of it (the playthrough does) |
| `map.json` | The same board as data: which region each square belongs to, plus the rivers, coast, Great Wall links and Grand Canal sections |
| `i-ching.html` | The twenty I Ching (event) cards: a reference table and print-and-cut cards |
| `i-ching.json` | The same cards as data |
| `reference-cards.html` | Printable two-sided reference cards: one general card for everyone and one card per province |
| `style/` | The stylesheets for the rulebook and the reference cards: `base.css` (the palette, shared), one layout file per page, and `themes/`, alternative looks unlocked by clicking a page's title five times quickly |
| `images/` | One SVG glyph per piece: the six realia, the public works and the soldier |
| `tools/` | Scripts that generate the map, the I Ching cards, the reference cards and the glyphs |
| `playthrough-sim/` | The engine and game scripts that generate both playthrough pages, with their own [documentation](playthrough-sim/README.md) |

## Regenerating

All the scripts are plain Python 3 with no dependencies. Run them from the repo root:

```sh
python3 tools/build_map.py      # map.svg, map-board.svg, map.json
python3 tools/glyphs.py         # images/*.svg
python3 tools/build_events.py   # i-ching.html, i-ching.json
python3 tools/build_reference.py # reference-cards.html
python3 tools/add_glyphs.py rulebook.html   # put a glyph before every piece name
python3 tools/add_glyphs.py i-ching.html
python3 playthrough-sim/agents/build_real.py # playthrough.html
python3 playthrough-sim/build.py # playthrough-scripted.html
```

`add_glyphs.py` can be run again safely: it removes the glyphs it added before adding them back.
`tools/add_theming.py rulebook.html` puts the theme scripts into the rulebook the same way (the reference-card build runs it itself).

## License

Everything in this repository is CC BY-SA 4.0 (see `LICENSE`). That license covers this
rewrite only, not the original game. Dynasty © 1969 Onoma Productions. This is an
unofficial fan project.
