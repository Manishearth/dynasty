# Scenario: Highway Rob-bery

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first: it says how to start a game, how far steering may go, and how the parked Storytellers work.

**The table:** 6 players: Reina Osorio (Emperor, 1), Clark Grafton (Official, 2), Richard Baron (Gentry, 3), Silke Weber (Silk Peasant, 5), Paddy Doyle (Rice Peasant, 6), Robert Land (Warlord, 8). About 10 years, in two-year chapters.

**Working title:** "Highway Rob-bery", subtitle "Six players · in progress". Write the real subtitle once the game ends (players · years · how it ended), in `game.py`'s `setup()`.

**Target arc: the Warlord's campaign is the story.** Rob raids his way to four pieces, one from each realia-holding player, and enters the social order, while the table pays more and more to stop him. **Manish's arc (2026-10-28): Rob takes the throne and wins.** The table's infighting leaves him the openings: Clark and Rich both want the throne, Silke and Paddy race for the same scarce pieces, Reina spends on works and bribes rather than soldiers, and nobody wants to pay for a defence that protects a rival. Rob wreaks havoc and causes everyone pain on the way up. The target is the throne around Years 6–8, leaving him a few years to reign; he may be a mean ruler. Public works should keep getting built so that he could run the game to completion, but a collapse soon after he takes over is just as good: Rob inherits a broken kingdom (the ×4 years from Year 9) with no way to fix it. Reina, displaced, becomes the new Warlord with his army.

**And most players end on a lost seat (Manish, 2026-10-28).** The bickering should turn into seat changes, many of them. A displaced player drops into the climber's old seat, so a busy table strands people below the seat they drew: Reina loses when Rob takes the throne, Clark and Rich when peasants climb past them, Silke if she climbs and is pushed back down into Paddy's seat. Rob wins wherever he ends except seat 8, so even a later climber taking the throne from him leaves him a winner. Paddy is the hardest to make lose (only seat 8 does it), so four of six losing is the realistic "most".

**Raids and swaps pull against each other.** A raided piece sits on Rob's desert, out of play, and with two pieces of each type and three to a set, early piece raids starve the swapping. When Rob takes the throne, every piece he holds goes back to stock and is auctioned again, so the climbing restarts under him.

**Path (a target, not a script):**
- Chapters 1–2 (Years 1–4): pieces reach the board, the rivalries form, and the first sets change seats. Rob postures, sells soldiers, takes bribes and raids grain more than pieces.
- Chapter 3 (Years 5–6): more swaps; Rob turns to pieces and hires his third soldier; land opens and grain goes to land rather than defence.
- Chapter 4 (Years 7–8): the last piece and the throne (Year 7's disaster bars raids on 5–7, so likely Year 8). Whoever is on the throne then becomes the Warlord.
- Chapter 5 (Years 9–10): Rob's reign, as mean as he likes, at ×4. The returned pieces set the climbing going again beneath him while the kingdom breaks.

If the players stop him anyway, let them, and record it.

**Bought soldiers stay with the seat** (Manish's ruling, 2026-10-28, now in `RULINGS.md` and the engine): a seat change hands each side's soldiers to whoever now holds their seat, so buying one defends a province, not a player.

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
