# The page: build pipeline and data format

`playthrough.html` is one self-contained file: HTML and CSS, a JSON block holding every game, and the JavaScript that renders them. Nothing is fetched at runtime, so the file works from disk, from GitHub Pages, or as an email attachment.

- [The build](#the-build)
- [The data format](#the-data-format)
- [Entries](#entries)
- [State snapshots](#state-snapshots)
- [How the page uses the data](#how-the-page-uses-the-data)
- [Changing the page](#changing-the-page)

## The build

```
template/head.html   ─┐
JSON from the games  ─┼─►  playthrough.html
template/tail.html   ─┘
```

`build.py`:

1. For each file in `GAMES`, creates an empty namespace and runs `cards.py`, `engine.py` and the game script in it, then takes the game's `RESULT`.
2. Serialises `{"games": [RESULT, ...]}` as compact JSON, escaping `</` so the data can't close its own `<script>` tag.
3. Writes `head.html + JSON + tail.html`.

`head.html` ends inside `<script id="data" type="application/json">`; `tail.html` begins with the closing `</script>`. The page reads the data with `JSON.parse(document.getElementById('data').textContent)`.

The build is deterministic: the same scripts always produce a byte-identical page, so a diff of `playthrough.html` reflects only real changes.

## The data format

```jsonc
{
  "games": [
    {
      "meta":    { "key": "trashfire", "title": "A slow trashfire",
                   "subtitle": "Eight players · twelve years · ends in revolt",
                   "short": "8 players · 12 years", "blurb": "All eight provinces. …" },
      "active":  [1,2,3,4,5,6,7,8],           // seats in play
      "names":   { "1": "Reina Osorio", … },  // player id → full name
      "short":   { "1": "Reina", … },         // player id → short name
      "role":    { "1": "Emperor", … },       // seat → role, all eight
      "rname":   { "CH": "Customs House", … },
      "need":    { "2": ["LD","BB","DJ","WB","VA"], … },   // seat → realia required
      "owed":    [["Summer Palace",1,20], ["Great Wall",12,40], …],  // [name, count, cost each]
      "rounds":  [ { "n": 0, "title": "Eight strangers to the box", "card": "All eight provinces…",
                     "start": 0, "mult": 1 }, … ],
      "entries": [ … ],                       // see below
      "results": [ { "name": "Reina Osorio", "short": "Reina", "start": 1, "startrole": "Emperor",
                     "fin": 7, "finrole": "Wheat Peasant", "verdict": "lost", "grain": 60.0 }, … ],
      "results_note": "The game ended in collapse…",
      "epilogue": ["Three of the four who improved…", …],
      "grid": ["BBBBBBBBBBBBBBBBBBBBBBBBBBBSSS", …],   // map.json's 22 rows of 30 squares
      "map":  { "rivers": {"north": [[x,y], …], "south": […]},  // paths in grid units
                "coast": [[x,y], …],
                "wall":  { "1": [[[x,y],[x,y]], …], … },        // four links above each of 1, 2, 3
                "canal": { "1": [[[x,y], …], …], … } }          // two sections in each of 1, 4, 5, 6
    },
    …
  ]
}
```

`rounds[i].start` is the index of the round's first entry; a round runs until the next round's `start`. `mult` is the population multiple during that round. Round `n: 0` is the Setup round; its `card` is a line about the table rather than an I Ching card.

In `grid`, each character is a region: `1`–`7` a province, `8` the Warlord's territory, `n` the strip below the Wall, `B` beyond the Wall, `S` the sea. Paths in `map` are in grid units: (0, 0) is the top-left corner of A1, one unit per square.

## Entries

Every entry has these fields:

| Field | Meaning |
|---|---|
| `k` | `"act"`, `"say"` or `"lot"` |
| `t` | The line's text |
| `h` | The hover: `null`, or a list of `{"w": speaker, "t": thought}`; `w` is `""` for an unattributed note |
| `who` | For `say`, the speaker's short name; otherwise `null` |
| `d` | Grain changes on this line, `{player: delta}` — informational |
| `hl` | Seats to highlight on the board |
| `mv` | Soldier steps made on this line, `[[from, to, side]]`, drawn as arrows; `side` is `"W"` for the Warlord's, `"B"` for a bought soldier |
| `state` | The full game state after this line (below) |

`act` entries may also have `"big": true` (a turning point, styled differently). `lot` entries also have `bids`: a list of `{"who", "t", "h", "amt"}`, where `amt` is `null` for a pass.

## State snapshots

| Field | Shape | Meaning |
|---|---|---|
| `grain` | `{player: number}` | Every player's grain |
| `seat` | `{seat: player}` | Who sits where |
| `held` | `{player: {code: n}}` | Realia owned |
| `stock` | `{seat: {code: n}}` | Realia waiting to be auctioned |
| `raids` | `{seat: n}` | Squares raided per province |
| `pw` | object | Public works built: palaces and `irr2`/`res3`/`res7` as 0/1, `wall` and `canal` as `{seat: n}` |
| `at` | `{key: [square]}` | The squares each palace and cut-out stands on |
| `bonus` | `{seat: n}` | Harvest bonus in effect |
| `board` | `{square: {realia, owner, raid}}` | Every square holding realia or a raid marker, keyed like `"H12"` |
| `sol` | `[[id, side, square, owner]]` | Every soldier in play |
| `pile` | number | The Harvest Pile |
| `mult` | number | Population multiple |
| `rob` | `{player: code or palace}` | The Warlord's objective progress |

All dictionary keys are strings, as JSON requires; the page converts with `+key` or `String(n)` where needed.

Snapshots are complete rather than incremental: any entry can be shown on its own, which is what makes clicking a line in the middle of a year work. The cost is size, almost all of it snapshots.

## How the page uses the data

**Game selector.** One button per game, from `meta`. Choosing a game sets the address fragment to `#key`; opening the page with a fragment, or changing it, loads that game.

**Tabs.** Setup, then one per year, then Result. A tab shows the round's header (title, and the card text or, for Setup, the table) and its entries.

**Selecting an entry.** Clicking a line — or stepping with the arrow keys or the Step buttons — draws that entry's `state` in the side panel:

| Panel | Drawn from |
|---|---|
| Board | `../map-board.svg` as the ground, the printed map without frame or labels; `grid` for hatching provinces not in `active` and for highlights; `map` for the rivers, and for the Wall links and canal sections, solid when `pw` says they're built and dashed while owed; `at` for palaces and cut-outs; `board` for pieces and raid squares; `sol` for soldiers; `mv` for this line's moves; `hl` for highlighted provinces |
| Objectives | `need` and `held` for each realia province; `rob` for the Warlord |
| Public works | `owed` against `pw`, with a running total in millions |
| Players | `seat`, `grain` and the pile |

**Notes.** Any entry or bid with an `h` gets a dotted underline. On a mouse device the note follows the pointer; on a touch device a tap opens it pinned to the bottom of the screen with a Close button. Keyboard focus also opens it.

**Lots.** A `lot` entry is a `<details>` element; its summary is the clickable action, and opening it shows the bid ladder.

**Result.** `results_note`, a table of `results`, and the `epilogue` paragraphs.

## Changing the page

| To change | Edit |
|---|---|
| Colours, type, layout | The CSS in `template/head.html`. The palette is the variables at the top of `:root`. |
| The header, panel titles, hint text | The markup at the end of `template/head.html` |
| Rendering, panels, interaction | The script in `template/tail.html` |
| The board's geography | `../map.json`, through `tools/build_map.py`. The engine and the page both read it; nothing is copied by hand. |
| How the board is drawn | `drawMap()` in `template/tail.html`. The ground is `../map-board.svg`, which `tools/build_map.py` writes from the same layers as `map.svg`; the page draws only this game's state on it |
| Province labels on the map | `LBL` in `template/tail.html`, in grid units |

## What changed (the Δ)

Every step whose state differs from the step before gets a Δ button at its right edge. Hovering it (tapping, on a touch screen) lists each player and the Harvest Pile with what they gained or lost, all as symbols: grain, realia (held or still unsold), public works and new harvest squares (credited to the player of the province they stand in), and soldiers. `holdings()` in `tail.html` reduces a state to those counts, and `deltas(k)` diffs entry `k` against entry `k − 1`; nothing extra is stored in the data. A seat change therefore shows the province's works and stock moving between the two players.

After any change, rebuild and check the page on a phone-width window as well as a desktop one; the layout switches to a single column below 900 px and to compact game buttons below 640 px.

## Piece glyphs

Pieces are drawn with the shared SVGs in `../images/` (one per realia, public work and soldier), the same files the rulebook uses:

- **Board and objectives.** `tail.html` maps realia codes to files in `IMG` and public works to files in `WORKIMG`. Board squares draw them with `<image>`; raided realia and built works are shown white on their coloured square.
- **Soldiers.** The soldier glyph is drawn as a path, not an `<image>`, so it can take each side's colour: black for the Warlord's, blue for bought soldiers, with a white halo. `build.py` copies its outline from `tools/glyphs.py` into `SOLDIER` in place of the `/*SOLDIER_PATH*/''` placeholder. `gsol()` draws the same shape in the legend and the Δ list.
- **Running text.** At load, a `MutationObserver` puts a glyph before every piece name the page writes: the transcript, tooltips, the works panel, the results. It skips SVG and the board legend, which is keyed to the board's own marks. The names to match come from `TERMS` in `tools/add_glyphs.py`; `build.py` copies them into the page in place of the `/*PIECE_TERMS*/[]` placeholder, so the playthrough and the rulebook always match. The glyph sizes come the same way: `build.py` puts `PIECE_CSS` from `add_glyphs.py` in place of `/*PIECE_CSS*/` in `head.html`. The board legend keeps a fixed size of its own.

To change a glyph, edit `tools/glyphs.py`, run `python3 tools/glyphs.py`, and both pages pick it up. The script rewrites every file in `images/`, and the committed files carry provenance metadata the script doesn't write, so restore the glyphs you didn't change (`git checkout -- images/<name>.svg`) before committing.
