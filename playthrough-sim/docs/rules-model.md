# How the engine models the rules

The engine is a ledger, not an opponent. It computes every number the rules determine and refuses moves the rules forbid, and it leaves every *choice* — bids, tax rates, which work to build, who to raid, what to say — to the script. This document says exactly where that line falls, and which rulebook rulings the engine depends on.

Section and note numbers refer to `combined-dynasty-rulebook.html`.

- [Computed by the engine](#computed-by-the-engine)
- [Enforced by the engine](#enforced-by-the-engine)
- [The script's responsibility](#the-scripts-responsibility)
- [Rulings the engine relies on](#rulings-the-engine-relies-on)
- [Simplifications](#simplifications)
- [The Harvest Pile](#the-harvest-pile)

## Computed by the engine

| What | How |
|---|---|
| Income | `harvest + public-works bonus − consumption × population multiple` (Section 7). Harvest is 100/75/50, or 40/30/20 for the Warlord; consumption is 40, 60 for the Emperor and 20 for the Warlord. |
| Population | The multiple starts at 1 and is multiplied by each population card drawn: × 2 or × 1.5. |
| Tax | `rate × income`, nothing on negative income (Section 9, Note 7). |
| Rent | A flat rate from each occupied peasant province to the Gentry (Section 5). |
| Auctions | The seller keeps a quarter; three quarters go to the Harvest Pile (Section 10). |
| Soldier sales | 20 each; the Warlord keeps 5 and 15 goes to the pile (Section 14). |
| Public-works bonuses | Canal sections +10 each to their province; Province 2 irrigation +10; reservoirs in 3 and 7 +20. They start the round **after** the work is built. |
| Disasters | The next one in the seat's booklet, with fractional amounts computed from the actual income, harvest or grain. |
| Seat changes | Who returns which pieces, the transfer of the displaced player's grain, and the 60 drawn from the pile (Section 11). |
| Starting stock and objectives | By player count, from the booklets (Section 10, Section 11). |
| Public works owed | Only works in occupied provinces (Note 4). |
| Scoring | Section 18, including the Emperor-holds-the-throne rule. |

## Enforced by the engine

The build stops with an error naming the player and the problem if a script:

| Rule | Source |
|---|---|
| Draws the same I Ching card twice in a game | Section 15: the deck is not reshuffled |
| Changes seats without every piece the seat requires | Section 11 |
| Changes seats with less than 20 grain in hand | Section 11 |
| Puts anyone but the Official, Gentry, Scholar or Warlord on the throne | Section 11, Note 10 |
| Moves a peasant anywhere but Provinces 2–7 | Section 11 |
| Splits a public work so the shares don't sum to its cost | — |

## The script's responsibility

These rules matter, but checking them would need information the ledger doesn't hold, so the script must get them right. The [checklist in the writing guide](writing-a-game.md#checklist) covers them.

| Rule | Source |
|---|---|
| Order of play within a round | Section 5, Note 5 |
| One public-works project per round, though a project may be several sections of one work | Note 12 |
| The Winter Palace before canal sections in Provinces 4, 5 and 6; the Summer Palace before the Wall and the Province 1 canal | Section 12 |
| The Marble Pagoda is built in a round when no system is being built | Section 12 |
| Every seller auctions one piece a round until their stock is empty | Section 10 |
| Returned pieces are auctioned again as soon as possible | Section 10 |
| The Emperor never bids; a seller doesn't bid on their own lot | Section 10 |
| The Warlord raids at most one square per soldier per round | Section 14 |
| Bought soldiers can't move until the Warlord has raided that province | Section 14 |
| Disasters that stop raids are obeyed | Booklet 8 |
| Card effects other than harvest and population (levies, disasters, imperial charity) | Section 15 |
| A raid takes realia only from a square where it has been placed — never from unsold stock | Section 10, Note 9 |
| Development of new land and sea only after the population has doubled | Section 13 |
| Revolt needs two other players to agree on a listed cause | Section 16 |
| Chaos stops tax, salaries and public works until a new Emperor emerges | Note 16 |

## Rulings the engine relies on

The original materials leave some questions open. Where the engine needed an answer it uses the rulebook's ruling:

| Question | Ruling | Rulebook |
|---|---|---|
| Is tax owed on a negative income? | No | Note 7 |
| How many of each piece exist at 4–5 players? | One of each province's own type, two of its never-needed type | Section 10, Note 8 |
| Where does a returned piece go if its home province is empty? | To the province that started the game holding it | Note 11 |
| Is the Province 1 Wall owed when Provinces 2 and 3 are empty? | Yes — four links | Appendix A, Emperor's booklet |
| Who does the Official's, Gentry's and Scholar's work when those seats are empty? | Whoever the Emperor appoints; no rent without a Gentry | Note 3 |
| How is the game scored? | By final province against starting province; an Emperor still on the throne has won | Section 18, Note 17 |
| Does a short game need special scoring? | No; Section 18 works from any stopping point | Note 18 |
| Is unsold stock on the map? | No; a piece is placed when it is bought or traded, so raids can't take stock | Note 9 |
| Does a palace raid count toward the Warlord's objective? | Yes — the booklets call the palaces the Emperor's realia, and he must pay the structure's cost | Booklet 1, Booklet 8 |

## Simplifications

- **Soldier movement isn't simulated.** Soldiers appear where they raid, and bought soldiers are drawn in their owner's province. Moves, captures and guarding are narrated by the script; the engine tracks only how many soldiers the Warlord has left. The rulebook now limits every soldier, the Warlord's included, to one square a round (Note 15); the current games predate that ruling and still need re-routing.
- **Positions on the board are representative.** Pieces go on the first free square of their province, not a square a player chose. The page's map is a schematic of the canvas board, not a copy of it.
- **Negotiation is authored.** Cost-sharing, bribes, trades and promises are written by hand; the engine records the money that changes hands.
- **Debt is allowed.** Grain can go negative, which the rules don't address. The full game ends with players in debt, and the epilogue says so.
- **Disasters follow the seat.** A player who moves into a province continues its booklet's disasters where the last occupant left off. The booklets don't say; this is the simpler reading.
- **One Warlord objective entry per player.** `warlord_got` keeps one entry per player — the most recent piece raided from them — because the Warlord's objective is one piece from each.

## The Harvest Pile

The pile is a real bank. It starts at 2,500 million — the face value of the bags in the box — less the 60 dealt to each player.

**Out:** every positive income, and 60 to each player displaced by a seat change.
**In:** every negative income, three quarters of each auction price, 15 of each soldier sale, disasters, repair levies, and damages.

Early in a game, when harvests outrun consumption, the pile drains. Once the population grows, incomes go negative and the whole country pays into it. In the full game the pile reaches its lowest point in Year 9 and is fuller by the end than it had been since Year 2 — the bank is the one thing in the country that gets richer as everyone starves. `trace.py` prints the pile on every line.
