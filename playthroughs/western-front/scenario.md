# Scenario: All's Quiet on the Western Front

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first: it says how to start a game, how far steering may go, and how the parked Storytellers work.

**The table:** 7 players: Reina Osorio (Emperor, 1), Clark Grafton (Official, 2), Richard Baron (Gentry, 3), Noah Tall (Scholar, 4), Silke Weber (Silk Peasant, 5), Paddy Doyle (Rice Peasant, 6), Graham Garner (Wheat Peasant, 7). About 10 years, in two-year chapters.

**Working title:** "All's Quiet on the Western Front", subtitle "Seven players · no Warlord · in progress". Write the real subtitle once the game ends (players · years · how it ended), in `game.py`'s `setup()`.

**Target arc: a peasant climbs twice, to the throne, through grain politics alone.** Rents, retainers, minimum bids and bought favours do the work the Warlord does in other games. Land opens early (Year 4), and the provinces that buy it pull away. Acceptable alternative: an upper-class player takes the throne, if a peasant got as far as an upper-class seat on the way.

**What it tests.**
- **The unsold-lot rule** where it was born: game 6's Emperor paid to keep the only Dragon Jar off the market for years, which is now legal for one round only.
- **The Gentry's rent as a weapon,** and the Emperor's subsidy, with no Warlord to blame.
- **Revolt with no Warlord:** five causes plus debt.

## The deck

- **Recommended seed: 74.** Average harvests in Years 2 and 3, the population doubles in Year 4 (land opens), then a bad harvest, a split year, growth by half in Year 8 (×3), a bad harvest, and a second doubling in Year 10 (×6). It's a long squeeze with one shock at the end, which rewards buying land in Years 4–7. Few personal disasters.
- Scout it: `python ../../playthrough-sim/agents/deck_scout.py 74 --seats 1,2,3,4,5,6,7 --years 10`.
- Alternatives (land in Years 4–5, ×3 or more by Year 10, one lean year early at most): 10, 113, 116.

## Levers

These are suggestions; the Director judges what the game needs between chapters. Actor's notes go in each character's `ledger.md` entry (the **Playing it** line), which every launch prompt carries.

- **Actor's notes:** Silke as the one peasant whose set needs no Dragon Jar, and who knows every upper-class set does; Rich as a landlord who means to raise the rent the year land opens; Reina as an Emperor who subsidises land for whoever stays loyal.
- **Storyteller's tips:** the climb ladder (a peasant needs an upper-class seat first) and the hold-back rule.
- If no peasant has a seat by Year 6, a tip about the cheapest upper-class set is fair.
