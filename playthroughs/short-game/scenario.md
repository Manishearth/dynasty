# Scenario: The short game

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first: it says how to start a game, how far steering may go, and how the parked Storytellers work.

**The table:** 4 players: Reina Osorio (Emperor, 1), Clark Grafton (Official, 2), Richard Baron (Gentry, 3), Noah Tall (Scholar, 4). About 8 years, in two-year chapters.

**Working title:** "The short game", subtitle "Four players · eight rounds · in progress". Write the real subtitle once the game ends (players · years · how it ended), in `game.py`'s `setup()`.

**Target arc: a race for the throne that's decided in the last two rounds.** The throne changes hands at least once, and the eighth round ends with two players a single piece apart. Acceptable alternative: Reina holds the throne to the end by playing the three of them off against each other, as long as it's close.

**What it tests.**
- **The unsold-lot rule at its sharpest.** At four players each province's own piece is a single piece that both rivals need. A seller can now hold it back for one round, then must offer it at 2. Watch whether that settles the throne race or just times it.
- **The short-game ending (Note 19)** with agents who know the count.
- **Population pressure arriving late:** with seed 39, the first population card comes in Year 6 and another in Year 8, so the last rounds are the hungry ones.

## The deck

- **Recommended seed: 39.** Share, a split harvest (Heaven Has Favourites), the Wall breach, Utility Tax, then the population doubles in Year 6, a bad harvest in Year 7 and the population grows by half in Year 8. Years 2–5 are comfortable, and every province's bare income goes negative in Years 7–8, just as the race ends. Personal disasters: only the Scholar's, once (Year 4).
- Scout it: `python ../../playthrough-sim/agents/deck_scout.py 39 --seats 1,2,3,4 --years 8`.
- Alternatives that passed the same test (first population card in Years 4–6, no more than ×3 by Year 8, one lean year early at most): 15, 38, 80.

## Levers

These are suggestions; the Director judges what the game needs between chapters. Actor's notes go in each character's `ledger.md` entry (the **Playing it** line), which every launch prompt carries.

- **Actor's notes:** Reina as a diplomat who keeps the three of them bidding against each other; Clark gleeful about leverage over the single Customs House; Rich fawning while hoarding his Scroll; Noah saying the arithmetic out loud, including who's one piece away.
- **Storyteller's tips** (public, strategy only) are the main lever for a close finish: the round count, who is one piece away, the hold-back-one-round rule.
- Don't let the table settle the throne by Year 5: if one player runs away, a tip to the other two about blocking is fair game.
