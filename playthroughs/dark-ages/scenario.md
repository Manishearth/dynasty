# Scenario: The Dark Ages

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first: it says how to start a game, how far steering may go, and how the parked Storytellers work.

**The table:** 6 players: Reina Osorio (Emperor, 1), Clark Grafton (Official, 2), Richard Baron (Gentry, 3), Silke Weber (Silk Peasant, 5), Paddy Doyle (Rice Peasant, 6), Robert Land (Warlord, 8). About 12 years, in two-year chapters.

**Working title:** "The Dark Ages", subtitle "Six players · in progress". Write the real subtitle once the game ends (players · years · how it ended), in `game.py`'s `setup()`.

**Target arc: an early revolt, a stretch of Chaos, then a recovery.** The population doubles in Year 3 and the next three harvests are lean. A hard-taxing Emperor, or one who can't pay, faces a revolt around Years 4–6. The acclamation count (Section 16) splits the table, so Chaos lasts a year or more, with no tax, salaries or works while the harvest, the rent and the Warlord carry on. Then a new Emperor rebuilds through land in the good Years 7–10. Acceptable alternatives: a revolt that resolves at once (Chaos lasting one round); or no revolt, if the table visibly came within a vote of one.

**What it tests.**
- **Revolt, Chaos and the acclamation count,** which no agent game has played yet.
- **Debt as a cause for revolt** (Note 7).
- **The deposed Emperor's position:** they stay in Province 1 and pay its consumption.
- **Recovery through land** under a new Emperor.

## The deck

- **Recommended seed: 350.** An average harvest in Year 2, the population doubles in Year 3 (land opens), then a split year, a bad harvest and Utility Tax: bare incomes are negative for most seats in Years 4–6. Years 7–10 are good or steady, the room for a recovery. Then a second doubling in Year 11 and a bad harvest in Year 12 (×4), so stop by Year 10–11 or let the last years bite. Personal disasters cluster in Years 7–9.
- Scout it: `python ../../playthrough-sim/agents/deck_scout.py 350 --seats 1,2,3,5,6,8 --years 12`.
- Alternatives (land by Year 3, two lean early years, no second doubling before Year 8): 200, 446, 513. Avoid decks like 64, which reach ×4 by Year 4 and leave no room to recover.

## Levers

These are suggestions; the Director judges what the game needs between chapters. Actor's notes go in each character's `ledger.md` entry (the **Playing it** line), which every launch prompt carries.

- **Actor's notes** are the main lever. Reina is a builder in a hurry: she means to tax hard while incomes are positive and build the Wall before the population comes. Clark keeps a paper trail of every deferral and knows the revolt clauses by heart. Rob would rather be standing nearby when it goes than cause it.
- **Storyteller's tips:** the six causes for revolt plus debt, and the acclamation's three counts (grain, soldiers, friends), once a revolt is in the air.
- **Don't force the revolt.** If the table forgives itself through Years 4–6, record that as the result and change the subtitle.
