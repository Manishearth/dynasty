# Rules digest: the peasant table

The rules this table needs, for a Storyteller who hasn't read `rulebook.html`. **§** is a rulebook section, **N** a rulebook note, **App** an appendix, **R:** a heading in `RULINGS.md`. The engine (`engine.py`) enforces most of what follows; where it doesn't, the line says *(script)*, and the Storyteller must check by hand.

The table is Reina (1, Emperor), Silke (5, Silk Peasant), Paddy (6, Rice Peasant), Graham (7, Wheat Peasant) and Rob (8, Warlord). Provinces 2, 3 and 4 are empty. They owe and are owed nothing (N4), but soldiers may walk through them; that raids nothing and pays nobody.

## Setup (§4, App A)

- Everyone starts with **60**, which is Round One's harvest.
- **Starting stock** waits beside the board until sold (N10):
  - Silke: 1 Dragon Jar and 2 Customs Houses.
  - Paddy: 1 Wooden Bowl and 2 Bamboo Brushes.
  - Graham: 1 Vase and 2 Land Deed Scrolls.
- **Rob's army:** 2 soldiers, placed on undeveloped land (desert, the strip below the Wall, or the sea).
- **Cut-out:** the Province 7 Reservoir, 2 × 2.
- **Jobs:** no Official, Gentry or Scholar, so the Emperor appoints the banker, the card reader and the tax collector (N3). There is **no rent**. Reina pays her appointed card reader 5 a year by her own choice (game 4's precedent); it isn't owed.

## Objectives (§11, the province sections, App A)

| Seat | Must collect, plus 20 grain | Holds and must sell | Never needs |
|---|---|---|---|
| 5 Silke | Scroll, Brush, Vase, Bowl | Jar ×1, Customs House ×2 | Customs House |
| 6 Paddy | Customs House, Scroll, Vase, Jar | Bowl ×1, Brush ×2 | Brush |
| 7 Graham | Customs House, Brush, Jar, Bowl | Vase ×1, Scroll ×2 | Scroll |

- **Pairs and singles** (§10, N9). Each pair is enough for the two peasants who need it. Each single (Jar, Bowl, Vase) is wanted by both other peasants, and there's only one. So only one peasant can complete a set at a time.
- **A complete set** lets a peasant replace another peasant (or the Official, Gentry or Scholar, but those seats are empty here). A Wheat or Rice Peasant can't take the throne. **But the Silk Peasant can** (Manish's ruling, Year 4; R: The Silk Peasant stands in for the upper class; §11, N11, §24). At a table with no Official, Gentry or Scholar, Silk is the peasants' upper class. A Silk Peasant who completes the Silk set (Scroll, Brush, Vase, Bowl) plus 20 grain may take the throne as in Becoming Emperor: they return their realia; the Emperor hands over the whole reserve, draws 60 and takes the Silk seat. Wheat and Rice climb to Silk first (either may go straight there), so every peasant is two completed sets from the throne. The engine allows `swap(5, 1)` at this table.
  - **No moving into an empty province 2–4** (Manish, for this sim only; not a ruling for the game at large). A complete set replaces another *player*.
- **Changing seats** (§11):
  - The mover keeps their grain plus all of the displaced player's grain, and returns pieces native to the new seat.
  - The displaced player returns everything and draws 60 from the pile.
  - Bought soldiers stay with their owner (R: Bought soldiers after a seat change).
  - The engine (`swap`) checks the set, the 20 grain, and who may go where.
- **Rob's objective:** raid one piece from each of Silke, Paddy and Graham. Then he may swap with anyone, the throne included. Palaces don't count at 5 players (R: The Warlord's objective leaves out the Emperor).
- **Reina's objective:** stay on the throne. The game ends in survival when every public work owed is built (§18).

## A round (§5, N5)

Round One skips the card and the harvest: the 60 is the harvest, and tax is levied on it. From Round Two:

1. **I Ching** (the card reader). Turn the next card in `seed.md`'s order and apply it (below).
2. **Harvest:** income = harvest + works bonus − consumption × population multiple (§7).
   - Peasants: 100/75/50 harvest, 40 eaten.
   - Emperor: 100/75/50 harvest, 60 eaten.
   - Rob: 40/30/20 harvest, 20 eaten.
   - At ×1 that's peasants +60/+35/+10, Reina +40/+15/−10, Rob +20/+10/0. Negative income is paid into the pile.
3. Rent: none at this table.
4. **Tax declared** (§9): one rate for all, 10%–90%, on each province's harvest income.
   - Rounded down to the half million (§8). No tax on negative income (N8).
   - Rob may refuse to pay.
   - Rent, commissions, tolls, tribute and deals aren't taxable.
5. **Tax paid** to the Emperor's reserve, which is her own grain in the engine.
6. **Public works** (§12): the Emperor builds **one project** *(script)*. Several sections of one work count as one project (N13). New land purchases come here too.
7. **Auction**, in province order (5, 6, 7) (§10):
   - Each seller must auction one piece a round until their stock is gone, and chooses which.
   - Minimum bid 2; the seller may set it higher.
   - The seller keeps ¼ of the price, rounded down to the half million; ¾ goes to the Harvest Pile (§8: "every bid drains the empire").
   - The Emperor doesn't bid. Rob may.
   - A bid must be covered by grain in hand.
   - The winner places the piece at once on an empty, unraided square of their province, not under a work (§10, N10, N14).
   - Rob raids instead of auctioning. Then the pile auctions any pieces sold back to it.
8. **Soldiers** (§14): **Rob's move first**, then the provinces' bought soldiers.
9. **Salaries:** Reina pays her appointees, if she chose to.

Trading, bribes, threats and promises may happen at any time. **No deal is binding** (§5).

## The Warlord and soldiers (§14, N15, N16)

- **Moving.** Every soldier moves at most one square a round, diagonals allowed. The sea is open to all soldiers (R: The sea is open to soldiers). A soldier may stand still.
- **Raids.** A Warlord soldier stepping onto an **unraided square of an occupied province** must raid it (R: Moving onto a square):
  - 5 from the player, or **10 in Province 1**;
  - **20 on a palace square** (the palace stays; R: A raided palace stays standing);
  - or, if a piece stands there, **the piece instead of the 5** (R: Raiding realia).
  - A raided square is never raided again.
- **Tolls.** Each step that crosses a river, a built Wall link, a built canal section or a cut-out costs Rob 5, paid to the province (R: Which rivers charge a toll; R: What counts as crossing). The engine computes them; `run.py --steps` lists them.
- **Buying soldiers.** Anyone may buy a soldier from Rob, and he must sell: 20, of which he keeps 5 and 15 goes to the pile.
  - It stands on a square of the buyer's province.
  - It **can't move until Rob has raided that province.**
- **Hiring.** After his march, Rob may hire one soldier a round for 20, paid to the pile, on his own desert (`8` squares). His army may grow to **3** at this table (R: The Warlord hires reinforcements). It moves from the next round.
- **Capture.** A soldier captures by stepping onto an enemy soldier **straight on** (horizontally or vertically), never diagonally. The captured soldier is removed. Only the same owner's soldiers share a square.
- **Guarding.** A soldier standing on a piece guards it. To take the piece, a raider must first capture the guard straight on, which means ending a move beside it, where the guard can capture it first. One raider can't break a free guard; two can. An unraided province's guard can't move, so a guard near the border is a gift (§14 "Guarding a piece").
- **A new Warlord** (P19; Manish, after Year 6; R: A new Warlord; §14): the army stays with the seat, where it stands, under the same cap, and the new Warlord may hire as before. The objective starts afresh: only raids the new Warlord makes count. The targets are every other player in a realia-holding seat (5, 6, 7), still leaving out the Emperor. The engine's `swap()` hands over the soldiers and clears the raid record.
- **Booklet disasters:** Rob's first is no raids on 5–7 this round; his second is 5, plus no raids at all this round (the engine refuses those raids).

## Cards and disasters (§15, `cards.py`)

The deck isn't reshuffled; each card is drawn once. The engine applies the harvest and the population. Everything else is *(script)*:

| Card | Harvest | Also |
|---|---|---|
| careless | good | every player plays a disaster |
| goodevil | good | 2, 4, 6, 8 play one (here Paddy and Rob) |
| repairs | good | 4–7 pay 2 to the pile; 1, 2, 3, 8 play a disaster |
| canal | average | unfinished canal destroyed; 2, 3, 7, 8 play one |
| breach | good | Wall breached: 1–3 pay 5 each to repair, or 2 to the pile if no Wall is built; 4–8 play one |
| chest | average | the Emperor gives every player 2 |
| share | average | provinces with works pay the Emperor half their bonus |
| utility | average | 2 from every province to the Emperor, 2 more from each with a work |
| rainflood | good 1, 3, 6, 7; bad 2, 4, 5, 8 | |
| heaven | good 2, 4, 5; bad 1, 3, 6, 7, 8 | |
| double1–3 | good | population ×2, counts at most twice |
| half1–2 | good | population ×1.5, counts once |
| blight, winds | average | |
| dribble1–3 | bad | |

**Disasters** are played in booklet order and follow the seat, not the player:

| Seat | #1 | #2 | #3 |
|---|---|---|---|
| Emperor | 4 | 10 | 30 |
| Silk | 4 | 10 | half the round's harvest |
| Rice | 4 | 10 | half the round's income |
| Wheat | 2 | 5 | a third of the round's income |
| Warlord | no raids on 5–7 | 5, and no raids at all | half his grain |

## Public works owed here (App A, §12): 520, all paid by the crown

| Work | Cost | Effect, prerequisite |
|---|---|---|
| Summer Palace | 20 | needed before the Wall and the Province 1 canal |
| Winter Palace | 20 | needed before the canals in 5 and 6 |
| Marble Pagoda | 20 | built in a round when nothing else is built |
| Great Wall, links 9–12 above Province 1 | 40 each | four built opens Province 1's strip for new land |
| Grand Canal, 2 sections each in 1, 5, 6 | 40 each | +10 harvest per section from the next round |
| Province 7 Reservoir | 60 | +20 harvest from the next round; a 2 × 2 cut-out in Province 7 |

The engine doesn't check prerequisites or the one-project rule *(script)*.

## New land (§13, R: New harvest squares)

- **When:** only after the population has doubled (a ×2 card).
- **Cost and yield:** 20 a square from the pile, yielding 20 a round from the next round. Any number of squares, alongside the round's one project. The Emperor must pay part of every purchase, and may pay all of it.
- **It's the strongest move in the game, and the pilot never made it.** A square pays for itself in one year. Breaking even in an average year takes 1 square at ×2, 3 at ×3 and 9 at ×6. A player in debt can't pay their share, so the time to buy is before the losses start. Every eligible player's board card shows their own numbers (`briefs.py`); from the first doubling, offer new land in every peasant's and the Emperor's menu, every year, and never tell them what to buy. A rich Emperor is encouraged to subsidise generously, up to the whole cost: every square raises that province's taxable income and its share of the works (§13).
- **Where:**
  - Silke: the sea.
  - Paddy: the sea or the Warlord's land.
  - Graham: the Warlord's land.
  - Reina: the sea, or the strip once her four Wall links stand.
- A bought square is part of the province and can be raided.

## Grain running out (§8, N7)

- A payment that would take a player below zero must first be covered by selling realia back to the pile at 2 each (`sell_back`).
- Any shortfall left is a debt. A player in debt can't bid, buy, trade, give grain, fund works or change seats, and every bag they receive pays the debt first.
- Debt is a cause for revolt.
- Voluntary payments use `act(..., deal=True)`.

## Revolt and Chaos (§16, N17)

- **Who may revolt:** any player, if two others agree that one of these causes exists:
  - the Emperor is unjust;
  - her taxes are consistently excessive;
  - her reserve is too low;
  - she has delayed the works too long;
  - she can't control the Warlord;
  - she won't subsidise new land;
  - or any player is in debt.
- **Chaos:** no tax, salaries or works until a new Emperor is acclaimed by counting grain, soldiers and friends. A claimant who leads in one count is acclaimed if no rival leads in another; otherwise the claimant who leads in more counts.

## Ending and scoring (§18, N18)

- The game ends when every owed work is built (survival), or when the table gives up (collapse; no winners).
- Each player compares the seat they hold at the end with the seat they drew:
  - a lower number is a win; the same seat is a hold; a higher number is a loss;
  - the Emperor still on the throne has won;
  - a Warlord who has entered the social order has won.
- Ties are broken by grain.

## Personality (§17)

Players must act in character: the booklet personalities are rules. Peasants revolt only when starvation threatens, though they want to climb. The Warlord lies freely. Bluffing and caginess about grain and plans are allowed; the Storyteller corrects only misstatements of the board, the cash or the rules.
