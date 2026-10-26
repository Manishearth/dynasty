# The project

**Dynasty** is a 1969 board game by Onoma Productions: a canvas map of eight Chinese provinces on a square grid, wooden realia (status objects) and public works, bags of grain as money, twenty "I Ching" event cards, and eight per-role instruction booklets. There is no single rulebook: each player reads only their own booklet, plus a sheet of General Instructions and the order of play printed on the can. Manish owns a copy.

The goal is a modern, unofficial revival:

1. **A modern rulebook** (`combined-dynasty-rulebook.html`). General concepts first (Part One), then one section per province (Part Two), then appendices: setup by player count, a worked round, reference cards, and editor's notes and rulings.
2. **A single list of rulings** (`RULINGS.md`). Every question the originals leave open, how it was settled and why, including the assumptions the playthrough engine makes, plus the open questions waiting for Manish.
3. **Annotated playthroughs** (`playthrough.html`). Five complete games played by the same group of eight friends on five evenings, on the real board, shown year by year with a Setup tab first. Each line is an action or a piece of in-character dialogue, and hovering shows what the players were thinking. A board, an objectives tracker, public works and player panels follow along.
4. **Reusable, copyright-clean assets.** A redrawn map (`map.svg`, `map.json`), a reworded I Ching card list (`i-ching.html`, `i-ching.json`), printable reference cards (`reference-cards.html`), and piece glyphs (`images/`).

The repo is `C:\Users\manishearth\dev\dynasty-new`, pushed to GitHub as `Manishearth/dynasty` on the `main` branch, licensed CC BY-SA 4.0. The original scans and photos are kept **off** GitHub, on manishearth.net/dynasty. The older folder `C:\Users\manishearth\dev\dynasty` still holds the scans and the pre-clean history; don't work there.

## Copyright constraints

- The booklets are © 1969 Onoma Productions. Renewal was automatic for 1964–77 works, so they're under copyright until the end of 2064. The company is defunct, making it an orphan work, but still protected.
- Rules, mechanics, roles and the grid layout are free to use. The specific prose, the card flavour text and the artwork are not.
- So: the map is a redrawn SVG, not a traced photo. The I Ching cards are reworded in `i-ching.json` with new flavour. The playthrough shows only the reworded card text (`cards.py` takes its text from `i-ching.json`). Scans and photos never go into this repo.
- The rulebook is Manish's rewrite in his own words. It still has some short quotes from the originals (`.orig` blocks, and the original wording in Appendix D). Manish is aware of this, and it's his call.

## Repository map

| Path | What it is | Made by |
|---|---|---|
| `combined-dynasty-rulebook.html` | The rulebook; one self-contained HTML file | Manish's rewrite, edited by several sessions |
| `RULINGS.md` | Every ruling, clarification and engine assumption, with reasons; the open rules questions | Every session adds to it |
| `design/` | These design documents | Every session keeps them current |
| `playthrough.html` | Generated. Never edit by hand; rebuild it | `playthrough-sim/build.py` |
| `playthrough-sim/` | Generator for the playthrough page: the engine, the cards, five game scripts, page templates, and docs | the playthrough sessions |
| `playthrough-sim/README.md`, `docs/*.md` | Writing a game, the engine API, the rules model, the page format | the playthrough sessions |
| `map.json` | The board square by square: 30 × 22 grid, rows A–V, columns 1–30. Legend, Great Wall links, Grand Canal sections, rivers and coast as paths in grid units. The playthrough engine and page both read it | `tools/build_map.py` |
| `map.svg` | Printable redrawn map, drawn as named layers (terrain, grid, borders, coast, rivers, canal, wall, labels, frame) that Inkscape shows as layers | `tools/build_map.py` |
| `map-board.svg` | The same map's ground alone: terrain, grid, province borders, coast and rivers, with no frame, labels or printed works. For pages that draw their own state on the board; the playthrough uses it | `tools/build_map.py` |
| `i-ching.json`, `i-ching.html` | The twenty cards, reworded | `tools/build_events.py` |
| `reference-cards.html` | Printable two-sided reference cards: one general card and one per province | `tools/build_reference.py` |
| `images/*.svg` | One glyph per piece (realia, palaces, wall, canal, irrigation, reservoir) | `tools/glyphs.py` |
| `tools/add_glyphs.py` | Puts a glyph before every piece name in the rulebook and the I Ching page. Also exports `js_terms()`, which the playthrough build uses so the page marks the same words | the map/cards session |
| `README.md`, `LICENSE` | Repo front page and CC BY-SA 4.0 | |

## Building

```sh
python3 playthrough-sim/build.py                       # rebuild playthrough.html (all five games)
python3 playthrough-sim/trace.py game1_full.py          # ledger: everyone's grain after every line
python3 playthrough-sim/trace.py game1_full.py --board 57   # the board after entry 57
python3 tools/add_glyphs.py combined-dynasty-rulebook.html  # re-run after editing rulebook text
python3 tools/build_map.py                              # regenerate map.svg, map-board.svg, map.json
python3 tools/build_events.py                           # regenerate i-ching.html / .json
python3 tools/build_reference.py                        # regenerate reference-cards.html
python3 tools/glyphs.py                                 # regenerate images/
```

These need Python 3.9 or later and no other dependencies. The playthrough build is deterministic: the same scripts always produce a byte-identical page. Use that to check that a refactor changed nothing. `add_glyphs.py` is idempotent too: running it twice changes nothing. Every generator writes UTF-8 with Unix line endings, on Windows as well.

The pages are plain files: open them straight from disk in a browser (for example `file:///C:/Users/manishearth/dev/dynasty-new/playthrough.html#full`). Glyphs load from `images/` beside them. There's no need for a preview server; give Manish file links to open.

## Working in parallel

Manish usually runs several sessions at once: one on the rulebook, one on the playthroughs, one on the map and cards. They share this repo.

- **Stay inside the files your task owns.** For playthrough work that's `playthrough-sim/` and the generated `playthrough.html`. Treat everything else as read-only unless Manish says otherwise.
- **`RULINGS.md` and `design/` are shared.** Add to them with small, targeted edits, never a wholesale rewrite, so you don't overwrite another session's entries.
- **Stage paths explicitly** when committing (`git add playthrough-sim playthrough.html`), never `git add -A`, so another session's work in progress doesn't land in your commit.
- **Check before writing** to a file another session might be editing: look at `git status` and the diff, and never overwrite newer work.
- Commit when Manish asks. He has allowed pushing to `main` on request.

The project began in several claude.ai conversations, which couldn't run commands and copied files out and back by hand: the original modernization (rulebook draft and the first playthroughs), the copyright and clean-repo conversation (map, cards, glyphs), a rulebook conversation, and a short one that renamed the Scholar to Noah Lott. Since then the work has moved to Claude Code sessions; see `history.md`.
