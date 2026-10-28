# Rules digest

The rules a Storyteller needs, for any table from the peasant game's five to the full eight, compact enough to read instead of `rulebook.html`. **§** is a rulebook section, **N** a rulebook note, **App** an appendix, **R:** a heading in `RULINGS.md`. The engine (`engine.py`) enforces most of what follows; where it doesn't, the line says *(script)*, and the Storyteller must check by hand. Who sits where comes from the engine and the game's `ledger.md`, never from this file: seats change hands.

**Seats.** 1 Emperor, 2 Official, 3 Gentry, 4 Scholar (the upper class), 5 Silk, 6 Rice, 7 Wheat Peasant (the lower class), 8 Warlord. An empty province owes and is owed nothing (N4); soldiers may walk through it, which raids nothing and pays nobody.

## Setup (§4, App A)

- Everyone starts with **60**, which is Round One's harvest.
- **Starting stock** waits beside the board until sold (N10). Each realia province (2–7) holds:
  - at 4–5 players, one piece of its own and two of the type it never needs;
  - at 6, two of its own;
  - at 7 or 8, **four of its own**.
- **The Warlord's army:** 4 soldiers at eight players, 2 at five or six, on undeveloped land (desert, the strip below the Wall, or the sea). The army may grow by one (R: The Warlord hires reinforcements).
- **Cut-outs**, for each occupied province: Province 2 Irrigation System 1 × 2, Province 3 Reservoir 2 × 3, Province 7 Reservoir 2 × 2.
- **The table jobs** (§5, Part Two):
  - **The Gentry** sets out and banks the Harvest Pile, and pays out every harvest.
  - **The Scholar** shuffles the I Ching and reads a card each year from Year 2, and keeps the population counter (100 million × the multiple).
  - **The Official** collects the tax for the crown.
  - A job whose seat is empty goes to whoever the Emperor appoints (N3). With no Gentry there's no rent.

## Objectives (§11, the province sections, App A)

**Realia seats (2–7)** collect a set plus 20 grain in hand. `need_for(seat)` in the engine is the authority; the board card prints it.

| Players | Each realia seat collects |
|---|---|
| 4–5 | the four types its booklet lists (all but its own and its "never" type) |
| 6 | one piece native to each other realia-holding province at the table |
| 7–8 | **one of every type except its own** (five pieces) |

At eight players every type has four pieces and five players want each one, so somebody is always one short.

**Who may replace whom** with a complete set (§11; the engine's `swap` checks the set, the 20 grain and the seats):
- An upper-class player (2, 3, 4) may take the throne, or replace any other player.
- A peasant (5, 6, 7) may replace the Official, Gentry, Scholar or another peasant, never the Emperor. **Only at a table with no upper class** may the Silk Peasant take the throne (R: The Silk Peasant stands in for the upper class); at eight, a peasant climbs to 2–4 first.
- **Changing seats:** the mover keeps their grain plus all of the displaced player's grain, and returns pieces native to the new seat to its stock. Becoming Emperor returns everything, and the old Emperor hands over the whole reserve. The displaced player returns everything and draws 60 from the pile. Every soldier stays with its seat: the mover's bought soldiers pass to the displaced player, and the displaced player's to the mover (R: Bought soldiers after a seat change).

**The Warlord** raids one piece from each player in a realia-holding seat, leaving out the Emperor (R: The Warlord's objective leaves out the Emperor). **At eight players only, one raid on the Summer Palace, Winter Palace or Marble Pagoda may stand in for any one player's piece**; the engine records it in `warlord_got` under `"palace"`. Then he may change places with anyone, the throne included. A seat counts as realia-holding even when its player holds nothing at the moment (R: readings). The board card prints the objective from the engine.

**A new Warlord** (R: A new Warlord): the army stays with the seat, where it stands, under the same cap; the objective starts afresh and counts only the new Warlord's own raids. `swap()` does both.

**The Emperor** stays on the throne. The game ends in survival when every public work owed is built (§18).

## A round (§5, N5)

Round One starts at step 3: no card, no harvest (the 60 is the harvest), and the tax is levied on the 60. **Rent is still asked in Round One** (R: Rent in Round One).

1. **I Ching** (the Scholar). Turn the next card in `seed.md`'s order and apply it (below). Announce the population.
2. **Harvest** (the Gentry pays it out): income = harvest + works bonus + new land − consumption × population multiple (§7).

   | Seat | Harvest good / avg / bad | Eats | Income at ×1 |
   |---|---|---|---|
   | 1 Emperor | 100 / 75 / 50 | 60 | +40 / +15 / −10 |
   | 2–7 | 100 / 75 / 50 | 40 | +60 / +35 / +10 |
   | 8 Warlord | 40 / 30 / 20 | 20 | +20 / +10 / 0 |

   Negative income is paid into the pile.
3. **Rent** (the Gentry): at least 5 from each peasant, **only if asked**; unasked, it isn't paid. A higher rent is negotiated. `rents(rate)`.
4. **Tax declared** (the Emperor; §9): one rate for all, 10%–90%, on each province's harvest income.
   - Rounded down to the half million (§8). No tax on negative income (N8).
   - The Warlord may refuse (R: The Warlord may refuse to pay tax).
   - Rent, salaries, commissions, tolls, tribute and deals aren't taxable.
5. **Tax paid** (the Official collects and delivers it) to the Emperor's reserve, which is the Emperor's own grain in the engine. `taxes(rate, collector=...)`.
6. **Public works** (the Emperor; §12): **one project** a year *(script)*; any number of sections of one work is one project (N13). Cost shares and new land are negotiated here.
7. **Auction**, in province order (2 to 7), then the pile's sold-back pieces (§10):
   - Each seller must auction one piece a round until their stock is gone; at seven or more each holds only its own type.
   - Minimum bid 2; the seller may set it higher. **A lot that goes unsold must be offered again the next round, with the minimum at 2** (R: An unsold lot reopens at 2): a seller may hold a piece back for one round, never two in a row. `briefs.py ... auctions --floor <lot>`.
   - The seller keeps ¼ of the price, rounded down to the half million; ¾ goes to the pile.
   - The Emperor doesn't bid. The Warlord may.
   - A bid must be covered by grain in hand; nobody in debt bids.
   - The winner places the piece at once on an empty, unraided square of their own province (not new land, not under a work) (§10, N10, N14).
   - The Warlord raids instead of auctioning.
8. **Soldiers** (§14): the Warlord's move first, then the provinces' bought soldiers.
9. **Salaries** (the Emperor): **at least 5 each to the Official and the Scholar**, every year (the Emperor's, Official's and Scholar's booklets). `salaries({2: n, 4: n})`. Appointees are paid only if the Emperor chooses.

Trading, bribes, threats and promises may happen at any time. **No deal is binding** (§5).

## The Warlord and soldiers (§14, N15, N16)

- **Moving.** Every soldier moves at most one square a round, diagonals allowed. The sea is open to all soldiers (R: The sea is open to soldiers). A soldier may stand still.
- **Raids.** A Warlord soldier stepping onto an **unraided square of an occupied province** must raid it (R: Moving onto a square):
  - 5 from the player, or **10 in Province 1**;
  - **20 on a palace square** (the palace stays; R: A raided palace stays standing);
  - or, if a piece stands there, **the piece instead of the 5** (R: Raiding realia).
  - A raided square is never raided again.
- **Tolls.** Each step that crosses a river, a built Wall link, a built canal section or a cut-out costs the Warlord 5, paid to the province. The engine computes them; `run.py --steps` lists them.
- **Buying soldiers.** Anyone may buy a soldier from the Warlord, who must sell: 20, of which he keeps 5 and 15 goes to the pile. It stands on a square of the buyer's province and **can't move until the Warlord has raided that province.**
- **Hiring.** After the march, the Warlord may hire one soldier a round for 20, paid to the pile, on his own desert. The army may grow to its starting size + 1 (5 at eight players). It moves from the next round.
- **Capture.** A soldier captures by stepping onto an enemy soldier **straight on** (horizontally or vertically), never diagonally. Only the same owner's soldiers share a square.
- **Guarding.** A soldier standing on a piece guards it. To take the piece, a raider must first capture the guard straight on, so it must end a move straight beside the guard, where the guard may capture it first. That's why one raider can't break a guard that's free to move, and two can (one as the bait). An unraided province's guard can't move, so a guard near the border is a gift.
- **The Warlord's disasters:** the first is no raids on 5–7 this round; the second is 5, plus no raids at all this round (the engine refuses those raids).

## Cards and disasters (§15, `cards.py`)

The deck isn't reshuffled; each card is drawn once. The engine applies the harvest and the population. Everything else is *(script)*:

| Card | Harvest | Also |
|---|---|---|
| careless | good | every player plays a disaster |
| goodevil | good | 2, 4, 6, 8 play one |
| repairs | good | 4–7 pay 2 to the pile; 1, 2, 3, 8 play a disaster |
| canal | average | unfinished canal destroyed; 2, 3, 7, 8 play one |
| breach | good | Wall breached: 1–3 pay 5 each to repair, or 2 to the pile if no Wall is built above them; 4–8 play one |
| chest | average | the Emperor gives every player 2 |
| share | average | provinces with works pay the Emperor half their bonus |
| utility | average | 2 from every province to the Emperor, 2 more from each with a work |
| rainflood | good 1, 3, 6, 7; bad 2, 4, 5, 8 | |
| heaven | good 2, 4, 5; bad 1, 3, 6, 7, 8 | |
| double1–3 | good | population ×2, counts at most twice, never past ×6 |
| half1–2 | good | population ×1.5, counts once |
| blight, winds | average | |
| dribble1–3 | bad | |

A card that names an empty province does nothing there. **Disasters** are played in booklet order and follow the seat, not the player:

| Seat | #1 | #2 | #3 |
|---|---|---|---|
| 1 Emperor | 4 | 10 | 30 |
| 2 Official | 4 | 10 | half the round's income |
| 3 Gentry | 5 | 10 | half their grain |
| 4 Scholar | 4 | 10 | a third of their grain |
| 5 Silk | 4 | 10 | half the round's harvest |
| 6 Rice | 4 | 10 | half the round's income |
| 7 Wheat | 2 | 5 | a third of the round's income |
| 8 Warlord | no raids on 5–7 | 5, and no raids at all | half his grain |

## Public works (App A, §12)

Only works in occupied provinces are owed (`owed()` in the engine). With all eight seats that's **1,030**:

| Work | Cost | Who pays | Effect, prerequisite |
|---|---|---|---|
| Summer Palace | 20 | the crown | needed before the Wall and the Province 1 canal |
| Winter Palace | 20 | the crown | needed before the canals in 4, 5 and 6 |
| Marble Pagoda | 20 | the crown | built in a round when nothing else is |
| Great Wall, 4 links above each of 1, 2, 3 | 40 each | crown for 1; negotiated with 2 and 3 | four links above a province open its strip for new land |
| Grand Canal, 2 sections each in 1, 4, 5, 6 | 40 each | crown for 1, 5, 6; negotiated with 4 | +10 harvest per section from the next round |
| Province 2 Irrigation System | 30 | negotiated | +10 harvest |
| Province 3 Reservoir | 80 | negotiated | +20 harvest |
| Province 7 Reservoir | 60 | the crown | +20 harvest |

"Negotiated" means the province and the Emperor haggle over the split, and the Emperor will expect a share of the increase; neither can force the other to pay (§12). **But the crown may build any work it pays for in full,** province's agreement or not (R: The crown may build a negotiated work alone). The engine doesn't check prerequisites or the one-project rule *(script)*. Paying for a work pays the Harvest Pile (R).

## New land (§13, R: New harvest squares)

- **When:** only after the population has doubled (a ×2 card). Provinces 2 and 3 also need all four Wall links above them; Province 1's strip needs its own four, though it may take the sea before.
- **Where**, touching the province or land it has bought: 1 the sea or the strip; 2 and 3 the strip; 4 and 5 the sea; 6 the sea or the Warlord's land; 7 the Warlord's land. The Warlord buys none.
- **Cost and yield:** 20 a square into the pile, yielding 20 a round from the next round. Any number of squares, alongside the round's one project. The Emperor must pay part of every other province's purchase, and may pay all of it.
- **It's the strongest move in the game, and the pilot never made it.** A square pays for itself in one year. Breaking even in an average year takes a seat in 2–7 one square at ×2, three at ×3, five at ×4 and nine at ×6; the Emperor three, six, nine and fifteen. A player in debt can't pay their share, so the time to buy is before the losses start. Every eligible player's board card shows their own numbers; from the first doubling, offer new land to every eligible player every year (`briefs.py ... land`), and never tell them what to buy. A rich Emperor is encouraged to subsidise generously, up to the whole cost: every square raises that province's taxable income and its share of the works.
- A bought square is part of the province and can be raided. Realia still goes on the province's own squares.

## Grain running out (§8, N7)

- A payment that would take a player below zero must first be covered by selling realia on the board back to the pile at 2 each (`sell_back`). Unsold stock can't be sold back.
- Any shortfall left is a debt. A player in debt can't bid, buy, trade, give grain, fund works or change seats, and every bag they receive pays the debt first.
- Debt is a cause for revolt.
- Voluntary payments use `act(..., deal=True)`.

## Revolt and Chaos (§16, N17)

- **Who may revolt:** any player, if two others agree that one of these causes exists: the Emperor is unjust; taxes are consistently excessive; the reserve is too low; the works have been delayed too long; the Emperor can't control the Warlord; the Emperor won't subsidise new land; or any player is in debt.
- **Calling one off:** once two others agree, the Emperor may answer (pay, cut the tax, promise anything). The caller and each backer then stands by it or takes it back, and it stands only with the caller and two others still behind it. The players settle any question of who answered first; no seat order decides it (R: Calling off a revolt).
- **Under Chaos,** set `CHAOS = True` in `game.py` at the revolt and `CHAOS = False` at the acclamation: the engine then refuses works and new land, and `briefs.py` stops offering land.
- **Chaos:** no tax, salaries or works until a new Emperor is acclaimed by counting grain, soldiers and friends. A claimant who leads in one count is acclaimed if no rival leads in another; otherwise the claimant who leads in more counts (R: Counting the acclamation). Harvests are still paid and the Warlord still rides.
- **No seat change takes the throne under Chaos:** a set or the Warlord's objective can still replace any other seat (R: No seat change takes the throne under Chaos).
- **The sealed treasury:** at the revolt nobody may spend the reserve on anything voluntary. Province 1's harvest, raids on it, the Emperor's disasters and the "Emperor" cards still run through it. The deposed Emperor has no purse and can't claim. The new Emperor takes it whatever its sign, and the deposed Emperor takes their old seat and draws 60 (R: The sealed treasury).
- **The counts:** soldiers are those the claimant commands (the Warlord's army, or those bought for the claimant's province, moving or not; Province 1's count for nobody). Friends are the other players backing the claim. Soldiers are still for sale under Chaos, at 20 from the Warlord.

## Ending and scoring (§18, N18)

- The game ends when every owed work is built (survival), or when the table gives up (collapse; no winners).
- Each player compares the seat they hold at the end with the seat they drew: a lower number is a win; the same seat is a hold; a higher number is a loss. The Emperor still on the throne has won; a Warlord who has entered the social order has won.
- Ties are broken by grain.

## Personality (§17)

Players must act in character: the booklet personalities are rules. The Emperor negotiates with the upper class first. The Official can be bribed. The Gentry is greedy, fawns on his peers, and doesn't forget the rent. The Scholar always keeps his promises. Peasants revolt only when starvation threatens, though they want to climb. The Warlord lies freely. Bluffing and caginess about grain and plans are allowed; the Storyteller corrects only misstatements of the board, the cash or the rules.
