# Lessons

Mistakes caught along the way, worth not repeating. Add to this when something slips.

**Game logic**
- **Use the real cards, in order, once each.** The first draft of game 2 invented a Year 8 card, used the wrong harvest quality in Year 4, and skipped or reordered disasters in Year 3. The engine now refuses a repeated card. Card effects other than harvest and population (levies, disasters, charity) are still the script's job.
- **Key grain changes by player, not seat.** `act()` takes changes keyed by player id. Use `pid(seat)`. One card effect paid the wrong person because it used a seat number.
- **Mutate state before recording the entry.** Each entry snapshots the state *after* the line.
- **Let the guards bite.** The seat-change guard caught Paddy swapping with 17.5 grain (the rule is 20). The fix was to change the story: a raid moved from Province 6 to Province 5. Don't weaken the guard.
- **Raids never take unsold stock**, only pieces placed on squares (Note 10). Game 2 once had an illegal seizure of stock.
- **Returned pieces from empty provinces** go to the province that started with them (`home()`, Note 12), and **returned pieces are auctioned again at the next auction step**. Two games left returned pieces sitting in stock for years.
- **One piece a round per seller, until the stock is empty.** A seller once put up two pieces in one round; another province's stock was never offered again.
- **Players act on their own sets.** Several players silently passed up the one piece that would complete their set, and some bid on pieces they already owned. If a player declines, the hover says why; that's often a good beat (Noah refusing the throne in game 2).
- **The crown pays for what the booklet says it pays for.** A draft charged the peasants for their own canal sections; only some works are negotiable.
- **Plan soldiers on the board before writing the dialogue.** Under Note 16 the Warlord can only raid where a soldier steps, so a raid schedule written for the story ("Province 3 one year, Province 5 the next") may be impossible. Use `trace.py --board N` and `dist()`. Remember the Warlord moves first: a bought soldier left straight beside his soldier gets captured.
- **Tolls add up.** Re-routing game 2 cost Rob 30 in tolls and left him in debt. Let the players notice instead of routing around it.

**Numbers and voice**
- **Re-check every quoted number after any edit**, because everything downstream shifts. `trace.py` prints the ledger line by line. Earlier slips: the chest at 16 instead of 14, Reina at −80 instead of −60, miscounted rungs in one of Clark's auctions, "three links left" when there were six.
- **Distances and geometry are numbers too.** "Three squares from his soldier", "at an angle", "the deepest square", "the south coast" all have to match the board. The reviews caught a dozen of these.
- **Each game stands alone.** The games were once written as a series of evenings with cross-game callbacks and a reshuffled cast; Manish asked for independent games with everyone in their own province. Keep banter inside one game.
- **Population cards have caps.** Game 1 once drew both "half" cards and multiplied twice; the second should only have been a good harvest. The engine now enforces the caps.

**Page**
- Changing the hash must switch games (there's a `hashchange` listener).
- On phones the results table overflowed (fixed with `.tablewrap`), and the game buttons ran off screen (fixed with a compact grid and short subtitles; five games wrap to two rows). Re-check at 390 px after any layout change.
- Map labels overlapped the work markers on the old schematic board, and still sometimes overlap pieces on the real one.
- A browser can cache the old page while you test: add a query string (`?v=2`) after rebuilding.

**Files**
- **Never hand-edit `playthrough.html` or `playthrough-scripted.html`**; rebuild them.
- **Stay in your own files.** Other sessions edit the rulebook, the map, `RULINGS.md` and these docs at the same time. Stage paths explicitly when committing.
- Before editing the rulebook, check for parallel edits. Apply changes to the current text, then re-run `add_glyphs.py` and check the diff.
- `add_glyphs.py` matches piece names in prose, and once matched "Three reservoirs" in a booklet description. Reword or check the diff after every run.
- Renumbering notes touches the rulebook, `RULINGS.md` and the `playthrough-sim` docs and comments. Grep for `Note \d+` everywhere.
- Writing files from PowerShell can add a byte-order mark and garble em dashes. Write UTF-8 without a BOM.
- Python's text mode writes `\r\n` on Windows. A tool run there once rewrote every line of the rulebook; every generator now passes `newline="\n"`.
- `add_glyphs.py` used to add a blank line before `<script id="piece-glyphs">` on every run; its strip pattern now takes the trailing newline too, so reruns change nothing.
