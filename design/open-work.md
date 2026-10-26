# Open work

What's still to do, what's waiting on Manish, and the known issues. Take an item off when it's done, and say so in `history.md`. Open *rules* questions live in [`../RULINGS.md`](../RULINGS.md#open-questions), not here.

## Waiting on Manish

- **The rules questions in `RULINGS.md`**, especially the Pagoda rule (does a palace-only round have to build the Pagoda?), a displaced player's bought soldiers, and who commands the Warlord's soldiers once he takes the throne. The playthroughs avoid needing an answer to the last two, and read the Pagoda rule as "build it when you'd otherwise build nothing".
- **The strip along the southern river between Provinces 3 and 7**: `map.json` treats it as the Warlord's land. Check against the cloth.
- **Pun names.** Reina Osorio and Robert Land were floated for a later pun touch-up; nothing has been decided (see `cast.md`).

## The playthroughs

- **Read games 4 and 5 for voice.** They were drafted by parallel agents and checked by an independent review for rules, numbers and continuity, but deserve a read for flow and banter like the first three got.
- **Province labels on the board** sit at fixed spots (`LBL` in `playthrough-sim/template/tail.html`) and sometimes overlap a piece or a cut-out. Readable, but could be smarter.
- **Not modelled:** reclaiming a raided square (Note 13) and developing new land or sea (Section 13). No game needs them yet; a game that does will need engine support.

## The rulebook

- **Section 19**: the short-game paragraph ends with `<span class="cost">Note 18</span>`, but `.cost` chips are for sums of money. It should probably be a plain reference. Flag it to the rulebook session rather than fixing it silently.
- **Section 3**: the schematic map put Province 6 in the middle and 5 on the coast, which doesn't match `map.svg`. Manish said he'd handle it; check whether it's done.
- **Appendix B, the worked round**, has the Warlord pay the Rice Peasant a river toll on the way to raid Province 6 in Round One. On the real map no river lies between the desert and Province 6, so the example may want a different province.

## The repo

- **The top-level `README.md`** describes `playthrough.html` as three games; there are five.
- **`add_glyphs.py`** used to add a blank line before `<script id="piece-glyphs">` on every run. Check the diff after running it.
- **The old repo** at `C:\Users\manishearth\dev\dynasty` has stray writes from before the move (a `playthrough.html`, rulebook edits, a link in `index.html`, a `sim/` folder). Manish was told how to revert them. Don't work there.

## Checks to keep running

- The playthrough build is deterministic; `trace.py` gives the ledger, `trace.py --board N` the board.
- After any change to a game, re-check every quoted number and distance downstream of it.
- Click every tab and line in a browser at desktop width and at 390 px: no JS errors, no horizontal overflow. Serve the repo over HTTP so the glyphs load.
