# How the engine models the rules

The engine is a ledger and a referee, not an opponent. It computes every number the rules determine and refuses moves the rules forbid, and it leaves every *choice* — bids, tax rates, which work to build and where, which square to march to, what to say — to the script. This document says exactly where that line falls, and which rulings it depends on.

Section and note numbers refer to `rulebook.html`. Every ruling, including the engine's own assumptions, is also listed in [`../../RULINGS.md`](../../RULINGS.md), which is the master list. Add a new ruling there first.

- [Computed by the engine](#computed-by-the-engine)
- [Enforced by the engine](#enforced-by-the-engine)
- [The script's responsibility](#the-scripts-responsibility)
- [Rulings the engine relies on](#rulings-the-engine-relies-on)
- [The map](#the-map)
- [Simplifications](#simplifications)
- [The Harvest Pile](#the-harvest-pile)

## Computed by the engine

| What | How |
|---|---|
| Income | `harvest + public-works bonus − consumption × population multiple` (Section 7). Harvest is 100/75/50, or 40/30/20 for the Warlord; consumption is 40, 60 for the Emperor and 20 for the Warlord. |
| Population | The multiple starts at 1 and is multiplied by each population card drawn: × 2 or × 1.5. |
| Tax | `rate × income` rounded down to the half million, nothing on negative income (Section 9, Note 8). |
| Rent | A flat rate from each occupied peasant province to the Gentry (Section 5). |
| Auctions | The seller keeps a quarter of the price rounded down to the half million; the rest goes to the Harvest Pile (Section 10). A lot of realia sold back to the pile pays the whole price to the pile. |
| New land | 20 a square into the Harvest Pile; 20 a round more harvest for the province from the next round (Section 13). |
| Running out of grain | A piece sold back to the pile pays 2 and joins the pile's stock; a shortfall left after selling is a debt, carried as negative grain that every receipt pays down (Note 7). |
| Soldier sales | 20 each; the Warlord keeps 5 and 15 goes to the pile (Section 14). |
| Raids | From the square a Warlord soldier steps onto: 5, or 10 in Province 1; a palace costs the Emperor 20; realia may be taken instead. Nothing in an empty province (Note 4). |
| Tolls | 5 for each river, built Wall link, built canal section or cut-out a Warlord soldier's step crosses (Section 14, Note 16). |
| Captures | A step onto an enemy soldier's square, horizontally or vertically, removes it (Note 15). |
| Public-works bonuses | Canal sections +10 each to their province; the Province 2 irrigation system +10; the reservoirs in 3 and 7 +20. They start the round **after** the work is built. |
| Disasters | The next one in the seat's booklet, with fractional amounts computed from the actual income, harvest or grain and rounded down to the half million. |
| Rounding | Every computed payment (commission, tax, fractional disaster) rounds down to a multiple of 0.5, in the payer's favour: `pay_down` (Section 8). |
| Seat changes | Who returns which pieces, the transfer of the displaced player's grain, and the 60 drawn from the pile (Section 11). |
| Starting stock and objectives | By player count, from the booklets (Section 10, Section 11). |
| Public works owed | Only works in occupied provinces (Note 4). |
| Scoring | Section 18, including the Emperor-holds-the-throne rule. |

## Enforced by the engine

The build stops with an error naming the player and the problem if a script:

| Rule | Source |
|---|---|
| Draws the same I Ching card twice in a game | Section 15: the deck is not reshuffled |
| Starts Round One before the Setup round has dealt grain, taken stock and placed the Warlord's army | Section 4 |
| Places the Warlord's army anywhere but undeveloped land | Section 4 |
| Moves any soldier more than one square in a round, or twice in a round | Section 14, Note 16 |
| Moves a soldier into the sea | Note 16 (see [The map](#the-map)) |
| Moves a province's soldiers before the Warlord's in the same round | Section 5 |
| Moves a bought soldier before the Warlord has raided the province it was bought in | Section 14 |
| Captures diagonally, or steps onto another player's soldier | Note 15 |
| Raids where the Warlord's disaster forbids it | Booklet 8 |
| Takes realia that isn't on the raided square | Section 14 |
| Places bought or traded realia anywhere but an empty, un-raided square of the owner's province | Section 10, Note 10 |
| Puts a palace outside Province 1, or a cut-out of the wrong size or outside its province, or either on realia | Sections 2 and 12 |
| Builds more than four Wall links above a province or two canal sections in one | Section 12 |
| Buys new land before the population has doubled, on the strip below the Wall before the four links above the province are finished (Provinces 1, 2 and 3), in the wrong region, not touching the province, or without the Emperor sharing the cost | Section 13 |
| Lets a population card pass its own cap (two doublings, one increase by half, 600 million) | The cards |
| Auctions a piece the seller doesn't have, or lets the seller or the Emperor win a lot | Section 10 |
| Makes a payment that would put a player in debt while they still hold realia | Note 7 |
| Lets a player in debt bid, pay a share of a public work, buy a soldier, change seats (other than by Chaos acclamation) or pay in a voluntary deal; or lets anyone bid or deal beyond the grain in hand | Note 7 |
| Changes seats without every piece the seat requires, or with less than 20 grain in hand | Section 11 |
| Puts anyone but the Official, Gentry, Scholar or Warlord on the throne | Section 11, Note 11 |
| Moves a peasant anywhere but Provinces 2–7 | Section 11 |
| Splits a public work so the shares don't sum to its cost | — |

## The script's responsibility

These rules matter, but checking them would need information the ledger doesn't hold, so the script must get them right. The [checklist in the writing guide](writing-a-game.md#checklist) covers them.

| Rule | Source |
|---|---|
| Order of play within a round | Section 5, Note 5 |
| One public-works project per round, though a project may be several sections of one work | Note 13 |
| The Winter Palace before canal sections in Provinces 4, 5 and 6; the Summer Palace before the Wall and the Province 1 canal | Section 12 |
| The Marble Pagoda is built in a round when no system is being built | Section 12 |
| Every seller auctions one piece a round until their stock is empty | Section 10 |
| Returned pieces are auctioned again as soon as possible | Section 10 |
| Every bidder wants the piece | — |
| Which pieces a player sells back before going into debt, enough to cover the payment or all of them, and that voluntary payments are marked `deal=True` | Note 7 |
| The Harvest Pile auctions every piece it holds at the next auction, after the provinces' lots | Note 7 |
| Card effects other than harvest and population (levies, disasters, imperial charity) | Section 15 |
| Development of new land and sea only after the population has doubled | Section 13 |
| Revolt needs two other players to agree on a listed cause; while any player is in debt, the debt is itself a cause | Section 16, Note 7 |
| Chaos stops tax, salaries and public works until a new Emperor emerges | Note 17 |
| Sensible play on the board: a bought soldier left level with a Warlord soldier can be captured, because he moves first | Section 14 |

## Rulings the engine relies on

The original materials leave some questions open. Where the engine needed an answer it uses the ruling recorded in the rulebook or in `RULINGS.md`:

| Question | Ruling | Where |
|---|---|---|
| Is tax owed on a negative income? | No | Note 8 |
| How are fractional payments rounded? | Down to the half million, in the payer's favour | Section 8, `RULINGS.md` |
| How many of each piece exist at 4–5 players? | One of each province's own type, two of its never-needed type | Section 10, Note 9 |
| How much new land can a province buy, and is it the round's project? | Any number of squares, every round; it isn't the one project | Section 13, `RULINGS.md` |
| Can the Warlord raid new land? | Yes: a bought square is part of its province | Section 13 |
| What happens when grain runs out? | Sell realia back first, then debt; a player in debt can't spend; the mover in a seat change takes a debt with the grain; a Chaos acclamation may seat a player in debt; and a debt is a cause for revolt | Note 7 |
| Is unsold stock on the map? | No; a piece is placed on a square the moment it's bought or traded, so raids can't take stock | Note 10 |
| Where does a returned piece go if its home province is empty? | To the province that started the game holding it | Note 12 |
| Is the Province 1 Wall owed when Provinces 2 and 3 are empty? | Yes — four links | Appendix A, Emperor's booklet |
| Who does the Official's, Gentry's and Scholar's work when those seats are empty? | Whoever the Emperor appoints; no rent without a Gentry | Note 3 |
| How far does a soldier move? | One square a round, the Warlord's included, diagonals allowed | Note 16 |
| Which way can a soldier capture? | Horizontally or vertically, never diagonally | Note 15 |
| Must a Warlord soldier raid the un-raided province square it steps onto? | Yes. Undeveloped land, raided squares and empty provinces raid nothing | Section 14, `RULINGS.md` |
| Which rivers charge the toll, and who is paid? | Both; the province stepped into, nobody in undeveloped land | `RULINGS.md` |
| What counts as crossing a public work, and who is paid? | A step that cuts a built Wall link or canal section, or lands on a cut-out; paid to the province the work belongs to | `RULINGS.md` |
| Is a raid on a canal, irrigation or reservoir square special? | No — an ordinary raid; the work is undamaged. The Wall can't be raided | Section 14, `RULINGS.md` |
| Does a palace raid count toward the Warlord's objective? | Yes — the booklets call the palaces the Emperor's realia, and the Emperor pays the structure's cost | Booklets 1 and 8 |
| Can two soldiers share a square? | Only the same owner's; an enemy square is entered only by capture | `RULINGS.md` |
| Where can realia go? | Not on a raided square, nor under a palace or cut-out | Note 14, `RULINGS.md` |
| What happens to bought soldiers when their owner changes seats? | They stay theirs, where they stand | `RULINGS.md` |
| How is the game scored? | By final province against starting province; an Emperor still on the throne has won | Section 18, Note 18 |
| Does a short game need special scoring? | No; Section 18 works from any stopping point | Note 19 |

## The map

The board is `../map.json`, the same geometry as `../map.svg`: 30 × 22 squares, rows A–V, columns 1–30. The engine reads it at start-up, so it's never copied by hand.

- **Undeveloped land** is the Warlord's territory (`8`) and the strip below the Wall (`n`). The Warlord's army starts there.
- **The sea** is closed to soldiers. Note 16 says Provinces 4 and 5 can be reached only through the gap in the west, which is only true if soldiers can't walk the coast.
- **Crossing** is tested geometrically: a step crosses a river, Wall link or canal section when the line between the two squares' centres cuts the printed path.
- **The geography** gives every province a character. Provinces 7 and 3 lie along the frontier. Province 1 faces the strip below the Wall. Provinces 4 and 5 are deep: from the desert, the only way in is the notch at M15–O18, where the southern river runs along the border between them, so a soldier walking that border pays a toll at almost every step. Province 4's north-east corner is a back door from Province 1 into the top of Province 5. A soldier may walk through an empty province without raiding or paying anyone.

## Simplifications

- **Negotiation is authored.** Cost-sharing, bribes, trades and promises are written by hand; the engine records the money that changes hands.
- **Disasters follow the seat.** A player who moves into a province continues its booklet's disasters where the last occupant left off. The booklets don't say; this is the simpler reading.
- **One Warlord objective entry per player.** `warlord_got` keeps one entry per player — the most recent piece raided from them — because the Warlord's objective is one piece from each.
- **Reclaiming raided squares isn't modelled** (Note 14). No playthrough needs it.

## The Harvest Pile

The pile is a real bank. It starts at 2,500 million — the face value of the bags in the box — and the Setup round deals 60 from it to each player.

**Out:** every positive income, the 60 dealt at setup, and 60 to each player displaced by a seat change.
**In:** every negative income, each auction price less the seller's commission, 15 of each soldier sale, disasters, repair levies, and damages.

Early in a game, when harvests outrun consumption, the pile drains. Once the population grows, incomes go negative and the whole country pays into it. In A slow trashfire (game 2) the pile reaches its lowest point in Year 9 and is fuller by the end than it had been since Year 2 — the bank is the one thing in the country that gets richer as everyone starves. `trace.py` prints the pile on every line.
