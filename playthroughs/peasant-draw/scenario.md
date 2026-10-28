# Scenario: The peasant's game

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first: it says how to start a game, how far steering may go, and how the parked Storytellers work.

**The table:** 4 players: Reina Osorio (Emperor, 1), Silke Weber (Silk Peasant, 5), Paddy Doyle (Rice Peasant, 6), Graham Garner (Wheat Peasant, 7). About 10 years, in two-year chapters.

**Working title:** "The peasant's game", subtitle "Four players · in progress". Write the real subtitle once the game ends (players · years · how it ended), in `game.py`'s `setup()`.

**Target arc: the peasants survive the deck that broke the last table.** Everyone stays out of debt, or climbs back out; a peasant takes the Silk seat and then the throne; most of the works get built. This is a design check of the rules changed since Peasant collapse ("buy as soon as you can, and buy ahead", "a rich Emperor should pay more", Silk as the upper class), so **steer lightly**. If the table collapses anyway, let it: that's the answer, and it matters more than a good story.

**What it tests.**
- **Land bought ahead.** Peasant collapse (`peasant-collapse/`) never bought a square. Land opens in Year 6 here, the same year the population reaches ×3, so a province needs about three squares at once just to break even on an average harvest.
- **Imperial subsidy.** Reina can pay any part of a square, up to all of it.
- **Silk standing in for the upper class:** whether the climb is worth doing.
- **Debt as a fear.** Debt stays punishing, so the table has to forgive rent or tax or deal its way out.

## The deck

- **Recommended seed: 20261027, Peasant collapse's own deck.** It makes the rematch a fair comparison: the Canal gives way in Year 2, the population grows by half in Year 3, then a bad harvest, then it doubles in Year 6 (×3) and three bad harvests follow by Year 10. Bare incomes go negative in Year 4 and stay there from Year 6.
- Scout it: `python ../../playthrough-sim/agents/deck_scout.py 20261027 --seats 1,5,6,7 --years 10`.
- If Manish would rather the rematch had a fairer deck than the old one: `--where "land<=4 and lean_early<=1"` finds decks where land opens earlier.

## Levers

These are suggestions; the Director judges what the game needs between chapters. Actor's notes go in each character's `ledger.md` entry (the **Playing it** line), which every launch prompt carries.

- **Actor's notes:** Reina as an Emperor who means to keep her people out of debt, and knows the crown can pay a whole square. Paddy earnest and careful with every grain; Silke sharp; Graham counting.
- **Storyteller's tips:** new land is already a standing prompt every year once it opens (STORYTELLER.md). One tip each the year land opens is fair; beyond that, let the table choose.
- **No stacking beyond the seed.** Record in `seed.md` anything you do steer, since this game's result is evidence.
