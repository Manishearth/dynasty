# Design intent

These are Manish's standing preferences, gathered from the conversations. Treat them as requirements unless he says otherwise.

## Working with Manish

- **Ask clarifying questions.** He explicitly likes them. For anything expensive to redo or open to interpretation, ask first and put a recommended option first. A "Discuss first" answer means he wants the trade-offs laid out before any work starts.
- **Keep it fun.** His standing preference: "I want our sessions to be fun. If you are not having fun, let me know and we can do something else!"
- **Order work when he asks.** For example, "Do rulebook work first so I can continue improving the rulebook in a second conversation." He often runs several sessions in parallel.
- **Git:** commit when he asks, staging your own paths explicitly. Push only when he says so; on 2026-10-25 he said "You may push automatically" for the design-docs work.
- **Don't overwrite parallel work.** Another session may be editing the rulebook, the map or the rulings. Stay inside your task's files, and check before writing (see "Working in parallel" in `project.md`).
- **Record rulings.** Every rules decision, clarification or engine assumption goes in `RULINGS.md` with a short reason; anything the sources can't settle goes under its Open questions for him.

## The rulebook (`rulebook.html`)

**Structure and voice**
- A modern rulebook: general concepts first (Part One, Sections 1–19), then one section per province (Part Two, Sections 20–27), then appendices. A: setting up by player count. B: a worked round. C: player reference cards. D: editor's notes and rulings.
- Manish's own wording, not the booklets' (see copyright in `project.md`). Short original quotes sit in `.orig` blocks with a `<cite>`.
- **No gendered pronouns in the rulebook.** Use "you", "the player" or singular "they". (The playthroughs are different: there the players are people with names.)
- Don't add text about mobile UI to documents. The page should just work on phones without saying so.

**Notes and rulings**
- Wherever the originals are silent or contradict each other, the ruling appears as a pink `.note` box at the point where it matters: `<div class="note"><b>Note N</b> …</div>`. It appears again in full in Appendix D, with the original wording, so a table can overrule it: `<h3>Note N · Title</h3>`.
- **Number notes in reading order, one number per note.** Adding a note renumbers every later one. Update all cross-references in the rulebook ("see Note 3"), the table in `RULINGS.md`, and the note numbers cited anywhere in `playthrough-sim/` (grep for `Note \d+`).
- Pink chips (`<span class="cost">`) are **sums of money only**, never note references. The introduction says so.

**Specific choices already made**
- Components: each item is a bold lead-in paragraph ("**The map.**", "**Grain.**", "**47 wooden pieces.**"). Small all-caps table captions looked wrong there and were removed.
- Province bands, the row of 1–8 boxes, appear at the top of each Part Two province page as **links** to the other province pages. Section 6 (The provinces) has no band.
- Naming: Provinces 3 and 7 have a **Reservoir**. Province 2 has an **Irrigation System**, because the booklet's Province 2 system has ditches and dams but no reservoir. "Reservoir / Irrigation System" is gone everywhere. In the plural, write "the irrigation system and the two reservoirs".
- Cut-outs: the game gives no size for the irrigation system or the reservoirs. Use Manish's wording: "There is no single correct size, but we have some suggestions here". Show the suggested size as a small drawing of squares, not "1 × 2" text: Province 2 is 1 × 2, Province 7 is 2 × 2, Province 3 is 2 × 3. No "where the sizes come from" explanation.
- Realia placement is highlighted in setup step 3 and under Starting stock: unsold stock waits beside the board, and a bought or traded piece must go on a square in the buyer's province immediately.
- Piece names in running text get glyphs, via `tools/add_glyphs.py`.
- **Reservoir is capitalised wherever its glyph appears**: "the Reservoir", "two Reservoirs". `add_glyphs.py` and the playthrough page do this themselves (the `CAPITALISE` set), so new text can't slip.

## The playthroughs (`playthrough.html`)

**What the page is**
- A game selector at the top, one button per game, linked to the URL hash (`#full`, `#peasant`, `#short`, `#complete`, `#six`). Under it, a **Setup** tab, one tab per year, and a Result tab.
- The transcript separates **actions** from **dialogue**. Auction lots expand to show the bid ladder.
- Side panels: an **annotated board**, an **objectives tracker** (each realia province's set, plus the Warlord's), **public works** (owed vs built, with a running total) and **players** (seat, grain, the Harvest Pile).
- **The board is the real map**, drawn the way `map.svg` draws it: the page lays `map-board.svg` (the map without its frame, coordinates, title, legend or labels) under its own marks, and draws the Wall and Canal in the map's style once built. It shows provinces, undeveloped land, the strip below the Wall, beyond the Wall, the sea, rivers, the Wall links and canal sections (dashed until built), palaces and cut-outs where they were placed, realia on their squares, raid squares, and every soldier. A line that moves soldiers draws the steps as arrows.
- Clicking a line, or stepping with the arrow keys or Step buttons, shows the board and panels as they were after that line.
- Works on phones: one column below 900 px, compact game buttons below 640 px, tooltips pinned to the bottom of the screen on touch.
- Piece glyphs are the shared `images/` SVGs, the same as the rulebook.

**Voice** (more detail in `playthrough-sim/docs/writing-a-game.md`)
- Prose is playful and natural, and the sessions should be fun to read.
- **Dialogue is roleplay**: players speak in character, as their province, inside the fiction.
- **Thoughts (hovers) are the players, not the characters**: people who know they're playing a board game. They reason about rules, count pieces, count squares, quote booklets and enjoy the bit, the way a tabletop RPG player who also likes strategy thinks. Use **several voices** per note: a move plus the reactions of the people it lands on.
- **Full names in the players table, short names in the transcript.**
- **Every number quoted in dialogue or thoughts must match the ledger** (`trace.py`), and every distance must match the board. Changing anything early in a game shifts everything after it.
- The games are **evenings in order** with the same friends, and they remember the earlier ones. A player can refer only to evenings they played in. Don't repeat a joke from an earlier evening unless a character is quoting it on purpose.
- **The Setup tab** is a short scene (8–12 entries) following rulebook Section 4 and Appendix A for that player count: booklets drawn, grain dealt, stock beside the board, the Warlord's army placed, the Harvest Pile set out, the I Ching shuffled, cut-outs made. Each game gives it its own flavour.

**Rules fidelity**
- These are **authored** games: a person wrote every choice. The engine does all the arithmetic and refuses illegal moves, so every number on the page follows from the rules. Use the guards; never weaken one to make a story fit. Change the story instead.
- The I Ching deck is the real twenty-card deck in a game-consistent order, never repeating a card within a game. The page shows the reworded text from `i-ching.json`.
- The Harvest Pile is a real bank: 2,500 at the start, less 60 per player.
- Disasters are applied in booklet order. Public-works bonuses start the round after the work is built. Seat changes need the complete set and 20 grain in hand.
- **Be strict about soldiers** (Note 16). Every soldier, the Warlord's included, moves at most one square a round, diagonals allowed; a Warlord soldier raids the square it steps onto; crossing a river or a public work costs 5; bought soldiers start in their owner's province and can't move until it's been raided, and then move after the Warlord's; capture is horizontal or vertical only. The engine tracks every square and refuses illegal moves.
- **Placement is a choice.** Every piece placed on the board goes on a square the player picks, and the hover says why. Realia is placed the moment it's bought or traded (Note 10). Palaces go on chosen squares of Province 1; cut-outs at their suggested sizes. A player keeps a precious piece deep inside their province, away from the frontier; the Warlord thinks about the same geography from the other side.
- **The constraints should make the games more interesting, not flatter**: marches that take planning, frontier provinces under pressure, deep provinces that are hard to reach, soldiers worth buying. When the map forces a change, the arc stays: "the overall arc should stay the same. if things need to move around, they can. try to keep it as interesting as the original."
- When a rules question comes up that the sources don't settle, stop and ask Manish, and record the answer in `RULINGS.md`. Don't invent a ruling.

**The map's geography.** How exposed each province is: the squares touching undeveloped land (the Warlord's territory and the strip below the Wall, not the sea, which soldiers can't enter), and the steps from that land to the province's deepest square.

| Province | Squares | Touching undeveloped land | Deepest square |
|---|---|---|---|
| 7 Wheat | 28 | 16 | 2 |
| 3 Gentry | 38 | 19 | 3 |
| 2 Official | 20 | 6 | 3 |
| 6 Rice | 20 | 7 | 3 |
| 1 Emperor | 34 | 7 | 5 |
| 4 Scholar | 23 | 3 | 6 |
| 5 Silk | 24 | 2 | 7 |

Provinces 7 and 3 are the frontier. Province 1 faces the strip below the Wall. Provinces 4 and 5 are reached from the desert only through the notch at M15–O18, where the southern river runs along their border and charges a toll at almost every step, and Province 4's north-east corner is a back door from Province 1 into the top of Province 5. Soldiers may walk through an empty province without raiding.

**The games** (the first three chosen by Manish from options; the last two asked for as "a fourth game that has 8 players and runs to full public works completion, and a fifth game that works with 6 players (and ends however you'd like)")
1. **Full game**: 8 players, 12 years, ends in revolt and Chaos; Graham takes the throne.
2. **Peasant game**: 5 players (the Emperor, three peasants, the Warlord), 9 years. It ends in **survival**: every public work gets built, with Reina still on the throne.
3. **Short game**: 4 players (the upper group), the 8-round short-game rule; Clark, the Official, takes the throne.
4. **Long game**: 8 players with the booklets dealt afresh, 10 years; a compact to build everything, and it gets built.
5. **Six-player game**: 6 players, 10 years; the Warlord completes his objective and takes the throne.
