# Open work

What's still to do, what's waiting on Manish, and the known issues. Take an item off when it's done, and say so in `history.md`. Open *rules* questions live in [`../RULINGS.md`](../RULINGS.md#open-questions), not here.

## Waiting on Manish

- **The rules questions in `RULINGS.md`**, especially a displaced player's bought soldiers, and who commands the Warlord's soldiers once he takes the throne. The playthroughs avoid needing an answer to either. (The Pagoda rule was settled on 2026-10-26.)
- **Additions to the province cards**, measured on 2026-10-26 but not built (see `reference-cards.md`): the round as a 3 × 3 grid with the player's own steps tinted, objective slots, an "any time" box, and a one-face glossary card. Only the peasant fronts have room for all three province additions; the Warlord's front has room for none.
- **The Running the round card's Chaos box** states three playthrough readings as rules (the deposed Emperor keeps Province 1, no land is bought during Chaos, Chaos can end mid-round). Confirm them, or soften the card.
- **The strip along the southern river between Provinces 3 and 7**: `map.json` treats it as the Warlord's land. Check against the cloth.
- **New land for the Official and the Gentry: watch it in playtests.** Every province waits for the population to double, but Provinces 2 and 3 also need the Summer Palace and their four Wall links (180 shared with the Emperor, two of the Emperor's one-a-round projects) before their strip opens, while 4–7 open at once and 1 has the sea. Rent, salaries and the tax purse offset some of it. In the scripted games 2 and 3 got land one to three years after everyone else, or never (full game, All's Quiet, The Dark Ages). It's in the original booklets, so any fix is a house rule. Options raised on 2026-10-27: open the strip link by link under each built link (smallest change), have the crown pay more of the Wall, or leave it. Manish: watch it first.
- **Pun names.** Reina Osorio and Robert Land were floated for a later pun touch-up; nothing has been decided (see `cast.md`).

## The playthroughs

- **Read games 1 and 5 for voice.** They were drafted by parallel agents and checked by an independent review for rules, numbers and continuity, but deserve a read for flow and banter like the other three got.
- **Province labels on the board** sit at fixed spots (`LBL` in `playthrough-sim/template/tail.html`) and sometimes overlap a piece or a cut-out. Readable, but could be smarter.
- **Not modelled:** reclaiming a raided square (Note 14). No game needs it yet.

## The rulebook

- **Section 19**: the short-game paragraph ends with `<span class="cost">Note 19</span>`, but `.cost` chips are for sums of money. It should probably be a plain reference. Flag it to the rulebook session rather than fixing it silently.
- **Appendix D, the worked round**, has the Warlord pay the Rice Peasant a river toll on the way to raid Province 6 in Round One. On the real map no river lies between the desert and Province 6, so the example may want a different province.

## The reference cards

See [`reference-cards.md`](reference-cards.md).

- **Catch up with the newer rulings.** The cards predate several entries in `RULINGS.md`. The Warlord's card says a crossing costs 5, but not that it's paid to the province stepped onto, that soldiers can't enter the sea, or that stepping onto an un-raided province square always raids it.
- **Utility Tax.** `RULINGS.md` says the Emperor doesn't pay it. The reworded card in `i-ching.json` and `i-ching.html` (from `tools/build_events.py`) still says "Every province pays the Emperor". Reword it to "every other province", and check the reference cards for the same slip.
- **Duplex printing is untested.** Print one sheet double-sided before printing all five, and fix the back-sheet order in `build()` if the backs don't line up.
- **Blank space.** The backs of the peasant and Warlord cards are half empty. Fine as is; ask Manish before filling them.

## The repo

- **The old repo** at `C:\Users\manishearth\dev\dynasty` has stray writes from before the move (a `playthrough.html`, rulebook edits, a link in `index.html`, a `sim/` folder). Manish was told how to revert them. Don't work there.

## Checks to keep running

- The playthrough build is deterministic; `trace.py` gives the ledger, `trace.py --board N` the board.
- After any change to a game, re-check every quoted number and distance downstream of it.
- Click every tab and line in a browser at desktop width and at 390 px: no JS errors, no horizontal overflow.
