# Scenario: The Warlord's game

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first: it says how to start a game, how far steering may go, and how the parked Storytellers work.

**The table:** 6 players: Reina Osorio (Emperor, 1), Clark Grafton (Official, 2), Richard Baron (Gentry, 3), Silke Weber (Silk Peasant, 5), Paddy Doyle (Rice Peasant, 6), Robert Land (Warlord, 8). About 10 years, in two-year chapters.

**Working title:** "The Warlord's game", subtitle "Six players · in progress". Write the real subtitle once the game ends (players · years · how it ended), in `game.py`'s `setup()`.

**Target arc: the Warlord's campaign is the story.** Rob raids his way to four pieces, one from each realia-holding player, and enters the social order, while the table pays more and more to stop him. The ideal ending is a near miss or a late success that the table could have prevented with one more soldier. Acceptable alternative: the provinces' bought soldiers stop him for good, if it takes them real grain and a real coalition.

**What it tests.**
- **The Warlord rules added since the scripted games:** hiring reinforcements (army cap 3 at six players), soldiers at sea, "realia: 5 or the piece", and a palace raid costing 20 and leaving the palace standing.
- **"A new Warlord"** if the seat changes hands.
- **Bought soldiers** as the provinces' only defence: who pays for them, and who free-rides.

## The deck

- **Recommended seed: 297.** The Warlord plays one personal disaster all game, in Year 7 (Careless Prosperity; his first is "no raids this year"), so nothing stops his raids before then. Two lean early years (split floods, then a bad harvest), then the population doubles in Year 6 and again in Year 9 (×4). Every other seat also plays one disaster, in Year 7.
- Scout it: `python ../../playthrough-sim/agents/deck_scout.py 297 --seats 1,2,3,5,6,8 --years 10`.
- Alternatives (no Warlord disaster before Year 7, at most one all game, land in Years 4–6): 268, 910, 1076.

## Levers

These are suggestions; the Director judges what the game needs between chapters. Actor's notes go in each character's `ledger.md` entry (the **Playing it** line), which every launch prompt carries.

- **Actor's notes:** Rob as a villain who has realised he's the villain and is enjoying it, announcing his targets; Reina as an Emperor who would rather pay the Warlord than build soldiers; Clark selling information about everyone's squares.
- **Storyteller's tips:** distances are on every board card already, so tips should be about coalitions: who has paid for a soldier and who is free-riding.
- If Rob is hopeless by Year 5 (two pieces short and no soldiers left), a tip to him about reinforcements and the sea is fair.
