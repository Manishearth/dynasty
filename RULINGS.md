# Rulings

Every rules question this project has settled, in one place. The 1969 game spreads its rules across eight booklets, a General Instructions sheet and the printing on the can. They sometimes disagree, and often say nothing. This file records what was decided, why, and where the decision lives.

**Everyone working on this repo, human or Claude, adds their rulings here.** That includes clarifications that never become a numbered rulebook note, and the assumptions the playthrough engine makes. If you decide how a rule works, write it down here before you build on it. If a question comes up that you can't settle from the sources, put it under [Open questions](#open-questions) and ask Manish. Don't invent an answer.

Each entry gives the question, the ruling, the reasoning, and where it's recorded. "Note N" means the numbered note in `rulebook.html`: a pink box where the rule applies, repeated in Appendix D with the original wording. Notes are numbered in reading order, so adding one renumbers every later note. When that happens, update this file and every `Note N` reference in `playthrough-sim/`.

- [Rulebook notes](#rulebook-notes)
- [Clarifications](#clarifications)
- [I Ching cards](#i-ching-cards)
- [The map](#the-map)
- [Playthrough engine](#playthrough-engine)
- [Open questions](#open-questions)

## Rulebook notes

These are the numbered notes, as of this writing. Appendix D has the full text and the original wording.

| Note | Question | Ruling |
|---|---|---|
| 1 | The can numbers the Warlord 5 and the peasants 6–8 | The map and all eight booklets win: peasants are 5–7 and the Warlord is 8 |
| 2 | The can leaves the Warlord out of the seven-player game | It stands. The Warlord's booklet lists armies for 5–6 and 8+ players only |
| 3 | Who does the Official's, Gentry's and Scholar's jobs when nobody holds the seat? | No Official: the Emperor collects tax or appoints a collector. No Scholar: the Emperor appoints someone to read I Ching and count population, and pays them the 5 salary. No Gentry: the Emperor appoints someone to bank the Harvest Pile, and nobody collects rent |
| 4 | What about unoccupied provinces? | The crown need not build there (Emperor's booklet). Their realia stays in the box, and no rent is owed for an empty peasant province |
| 5 | What order does a round go in? | The can's Order of Play, with rents (start of round), salaries (end of round) and provincial soldiers (after the Warlord moves) slotted in from the booklets |
| 6 | The printed income tables end at inconsistent populations | Consumption is always proportional to population. Tables are indexed by multiple (×1 to ×6); the cards cap the nation at 600 million, which is ×6 |
| 7 | What happens when a payment would take a player's grain below zero? | Sell before you sink: sell realia back to the Harvest Pile at 2 each, your choice of pieces, until the payment is covered or you have none left; then the shortfall is a debt to the pile. In debt you can't bid, buy, trade, give grain, pay toward a public work, buy soldiers or change provinces, and grain received pays the debt first. A player in debt counts as facing starvation, so debt is a seventh cause for revolt. Scoring is unchanged. See "Running out of grain" below |
| 8 | Is tax owed on a negative income? | No |
| 9 | What is the extra realia each province starts with at 4–5 players? | A pattern, not a ruling. It's always the one type that province never needs: 2 and 5 swap, and 3 → 6 → 4 → 7 → 3 form a ring |
| 10 | Is unsold stock on the map? | No. A piece goes on a square in the buyer's province the moment it's bought or traded. Returned pieces rejoin their province's unsold stock. Otherwise the Warlord could raid most of his objective in Round Two |
| 11 | Can a Peasant become Emperor directly? | No. The peasants' Objectives sections govern over the shared "Becoming Emperor" boilerplate. A Peasant must first take an upper-class seat |
| 12 | Where does a returned piece go if its home province is empty? | To the province that started the game holding it, to be auctioned again as soon as possible |
| 13 | One public works project per round, but the Emperor's booklet allows "any number of sections" | One project per round. A project may be any number of sections of the same work |
| 14 | What does reclaiming a raided square do? | Removes the marker. The square still can never be raided again |
| 15 | Booklets: soldiers capture horizontally only. General Instructions: horizontally and vertically | The General Instructions win: capture orthogonally, never diagonally. Movement may be diagonal |
| 16 | How far do the Warlord's soldiers move? | One square a round, like every soldier. "Anywhere" means no square is off limits. Every crossing of a river or public work costs 5 |
| 17 | What does Chaos stop? | No tax, salaries or public works until a new Emperor emerges. Harvests continue and the Warlord still raids |
| 18 | How is the game scored? | Final province against starting province, grain surplus as the tiebreak. An Emperor still on the throne has won, and so has a Warlord who has entered the social order at all |
| 19 | The eight-round short game | An addition, not a reading of the rules. Agree before setup; score as normal |
| 20 | The Scholar's realia at six players (missing from the booklet) | Two Bamboo Brushes, like every other province |

## Clarifications

These follow from the rules rather than overriding them, so they get a plain sentence in the rulebook (or none) rather than a numbered note. Rulebook Appendix E lists each one in its Clarifications table, and its I Ching table mirrors the card readings below: when you add or change one here, change it there too.

### Raiding a public work

**Ruling.** A raid on a square holding the Grand Canal, the irrigation system or a reservoir is an ordinary raid: 5 from that province's player, or 10 in Province 1. The work is not damaged. Only realia and the Emperor's three buildings get special raid outcomes.

**Why.** The rules give special outcomes for exactly two cases: realia ("5, the realia, or its cost") and the Summer Palace, Winter Palace and Marble Pagoda ("the Emperor must pay the full cost of the structure"). Everything else defaults to an ordinary raid. Full cost would also break the economy. A canal section costs 40 and the Province 3 reservoir 80, against a normal raid of 5 and a soldier price of 20, so raiding works would become the Warlord's whole strategy and building them a liability. It's also unclear who would pay for a work the crown funded. The rules already make works an obstacle for the Warlord, through the crossing toll. Damage to works comes from the I Ching deck ("The Canal Gives Way", "The Wall Is Breached", "Storms and Raiders").

**Recorded in** rulebook Section 14 (one sentence after the palace rule) and the Warlord's reference card. Decided 2026-10-25, in the "copyright-free dynasty-new" conversation.

### The Great Wall can't be raided

**Ruling.** The Wall stands on the northern border, outside every province, so there's no square on it to raid. A Warlord soldier crossing a Wall link pays the 5 toll like any other public work.

**Why.** A raid is a soldier landing on an unraided square inside a province (Section 14). The Wall sits on undeveloped ground on both the original cloth and `map.svg`. The toll applies to "any public works".

**Recorded in** the Warlord's reference card.

### Cut-out sizes for the irrigation system and reservoirs

**Ruling.** There's no single correct size. Suggestions: Province 2 irrigation system 1 × 2 squares, Province 7 reservoir 2 × 2, Province 3 reservoir 2 × 3. A cut-out goes on empty squares in its own province, not on realia. It counts as a public work for the crossing toll. It isn't realia, so a raid on a square under it is an ordinary raid (see above).

**Why.** The booklets say only "Design your own. Make a paper cut-out." The map has printed slots only for the Wall and the Canal, roughly 1–1.5 squares per link or section. The suggestions scale with what each booklet says the system holds.

**Recorded in** the rulebook (Components and Setup), as guidance, not a note.

### Naming the water works

**Ruling.** Provinces 3 and 7 have a **Reservoir**; Province 2 has an **Irrigation System**. In the plural: "the irrigation system and the two reservoirs".

**Why.** The booklets are consistent. Province 2's system ("ditches, dikes, small canals and dams") contains no reservoir; 3's and 7's do ("Reservoir/Irrigation System"). Manish shortened the long name.

### New harvest squares

**Ruling.** Only after that province's population has doubled (24 million for Provinces 2–4, 28 million for 1 and 5–7). The strip below the Wall opens to Provinces 1, 2 and 3 only once all four Wall links above that province are built (see below); Province 1 may develop the sea before then. Each square costs 20 from the Harvest Pile and yields 20 every round afterwards, starting with the next round's harvest; the cost and the yield are negotiated with the Emperor.

The details, settled by Manish on 2026-10-25:

- **No limit.** A province may buy any number of squares in a round, every round. The purchases aren't the round's one public-works project (Note 13): the Emperor still builds a project as well.
- **Late by design.** Because a province's population must first double, this route only opens late in the game, once a doubling card has come. A square repays its cost in one round, so once it opens it's the best investment on the board.
- **A bought square is part of its province.** The Warlord can raid it, and a soldier stepping onto one raids it; it counts for tolls and Note 4 like the province's own squares. Squares in the sea are out of every soldier's reach.
- **The Emperor must share the cost.** "The cost must be shared with the Emperor": the playthrough engine requires the crown to pay some part of every province's purchase (the crown's own squares it pays alone).

Two readings the playthroughs add, from the booklets' wording: each province develops the ground its booklet names (2 and 3 the strip below the Wall, 4 and 5 the sea, 6 the sea or the Warlord's land, 7 the Warlord's land, 1 the strip or the sea), and each square must touch the province or a square it has already bought.

**Recorded in** rulebook Section 13, every province's reference card, and `playthrough-sim/engine.py` (`buy_land`).

### The strip below the Wall opens province by province

**Ruling.** A province may develop the strip below the Wall only once the four links above *that* province stand. This applies to Province 1 as well as 2 and 3. Province 1 may develop the sea before then.

**Why.** The Emperor's booklet: "You or Provinces 2 and 3 may develop the New Land below the Great Wall when 4 sections in each Province have been built." So the Emperor is gated too, which the rulebook had missed. "4 sections in each Province" could mean all twelve links, but the Official's and Gentry's booklets gate their land on "all four links", their own, and only the per-province reading lets all three booklets agree. Settled by Manish on 2026-10-25. The playthroughs had Reina buy strip squares with two and three of her links built; both purchases are now sea.

**Recorded in** rulebook Section 13, Province 1's table in Section 20, Appendices B and E, the reference cards, and `playthrough-sim/engine.py` (`buy_land`).

### Which Wall links are above which province

**Ruling.** Numbered west to east, links 1–4 belong to Province 3, links 5–8 to Province 2 and links 9–12 to Province 1. The map labels each group. "The four links above your province" means that province's group, for who shares the cost, which tolls it is paid, and when its strip opens.

**Why.** The cloth prints twelve links in a row spelling GREAT WALL, with no province numbers, and the booklets only say "four links above your province". The provinces don't sit neatly under the Wall: links 9–12 (W, A, L, L) are clearly over Province 1, east of the river; Province 2 sits inside the river's northern loop, under only about two links; and Province 3 lies south of Province 2, nowhere under the Wall, so its links stand over the Warlord's land. Twelve links, three provinces and "four links" each leave one split that keeps the provinces in their west-to-east order. Settled by Manish on 2026-10-25.

**Recorded in** rulebook Section 12 and Appendix E, `map.svg` (labels), and `tools/build_map.py` (`WALL_GROUPS`, which writes `above_province` in `map.json`).

### A palace raid counts toward the Warlord's objective

**Ruling.** Yes. The booklets treat the palaces as the Emperor's realia, and the Emperor pays the structure's cost.

**Recorded in** `playthrough-sim/docs/rules-model.md`.

### Is the Province 1 Wall owed when Provinces 2 and 3 are empty?

**Ruling.** Yes, its four links. Note 4 excuses works in unoccupied provinces, and Province 1 is occupied.

**Recorded in** `playthrough-sim/docs/rules-model.md`, from Appendix A and the Emperor's booklet.

### Which rivers charge a toll, and who is paid

**Ruling.** Both rivers. A Warlord soldier pays 5 for each river its step crosses, to the province whose square it steps onto. A step that lands on undeveloped land or beyond the Wall pays nobody: the river there runs through the Warlord's own country. An unoccupied province is owed nothing (Note 4).

**Why.** The booklet pays the fee "to the Province player"; the province entered is the one whose ground the soldier has just crossed into. Manish chose this on 2026-10-25, in the Claude Code playthrough session.

**Recorded in** `playthrough-sim/engine.py` (`tolls()`) and `docs/rules-model.md`.

### What counts as crossing a public work, and who is paid

**Ruling.** A Wall link or canal section is crossed when a step, drawn from square centre to square centre, cuts its printed line, the same test as a river. A cut-out is crossed when a soldier steps onto one of its squares. Palaces aren't crossed: landing on one is already a raid that costs the Emperor 20. The toll goes to the province the work belongs to: a Wall link's province is the one it stands above, a canal section's the one it's in. Only built works charge.

**Why.** Manish chose this on 2026-10-25 in the playthrough session ("lines + cut-outs"; the payee as the work's own province).

**Recorded in** `playthrough-sim/engine.py` (`tolls()`).

### Soldiers stay out of the sea

**Ruling.** No soldier may stand on a sea square.

**Why.** The Warlord's booklet lets him go "across water", but Note 16 says Provinces 4 and 5 can be reached only through the gap in the west, which is true only if the coast is closed. Confirmed by Manish on 2026-10-25.

### Moving onto a square

**Ruling.** A Warlord soldier that steps onto an un-raided square of an occupied province raids it; that isn't optional. Stepping onto undeveloped land, a raided square or a square of an unoccupied province raids nothing and costs nobody anything (Note 4). Any soldier may stand still for a round. Soldiers of the same owner may share a square ("marched together as a group"); a square holding an enemy soldier can be entered only by capturing it, horizontally or vertically (Note 15).

**Why.** Section 14: "A Warlord soldier raids the square it moves onto." Confirmed by Manish on 2026-10-25, as was stacking for one owner only.

### Placing pieces

**Ruling.** Realia can't go on a raided square or under a palace or cut-out, and a palace or cut-out can't go on a square holding realia. A soldier may stand on a square holding realia. Realia the Warlord takes goes on a square of his own territory. Wall links and canal sections are built in the order printed on the map (link 1 first, section 1 first).

**Why.** A raided square "may hold realia" only after reclaiming (Note 14), so before that it can't. The cut-out rule is the Setup guidance. Confirmed by Manish on 2026-10-25.

### Bought soldiers after a seat change

**Ruling.** A bought soldier belongs to the player who bought it, and stays where it stands when that player changes seats. It still can't move until the Warlord has raided the province it was bought in.

**Why.** Soldiers are bought with the player's own grain, and on a seat change the mover keeps their grain. Recommended to Manish on 2026-10-25; he asked which made more sense and hasn't overruled it. What happens to a *displaced* player's soldiers is unsettled (see Open questions); the engine refuses that case, and no playthrough needs it.

### Running out of grain (Note 7)

**Ruling.** Manish's "sell before you sink". When a payment a player owes would take their grain below zero (a negative harvest, tax, rent, a disaster, a card's levy, the Warlord's tribute, a salary the Emperor owes), the player first sells realia back to the Harvest Pile at 2 each, choosing the pieces, until the payment is covered or they have none left. Then the shortfall is a debt to the pile. While in debt they can't bid, buy, trade, give grain, pay a share of a public work, buy soldiers or change seats, and every bag they receive pays the debt first. Scoring is unchanged (Section 18).

The details, settled by Manish on 2026-10-25:

- **Where a piece sold back goes.** Into the Harvest Pile's own stock. "harvest pile auctions off all unused pieces during the next auction." The pile's lots come after the provinces' lots, and the whole price goes to the pile, since there's no seller to keep a commission. (The order within the auction is the playthroughs' reading.)
- **A Chaos acclamation is allowed in debt.** It isn't a player completing a set; the table chooses. The new Emperor takes the imperial reserve, which pays the debt first. Game 2's ending relies on this.
- **A bid must be covered by grain in hand.** Buying is locked out in debt, so a purchase can never be what puts a player there.
- **A displaced player's debt passes to the mover.** The mover takes all of the displaced player's grain, whatever its sign; the displaced player then draws 60 from the pile as usual.
- **Debt is a cause for revolt.** A player in debt counts as facing starvation, which the peasants' booklets name as the one thing that drives them to revolt ("only if the alternative is death or starvation"). So while any player is in debt, the debt is a seventh cause, alongside the six in Section 16. It still needs two other players to agree, and the player in debt may be the one revolting. Manish added this on 2026-10-25.

**Why.** Nothing in the originals covers it. Note 8 covers only tax on a negative income. The hints: the Rice Peasant's fire ("you must borrow grain"), the General Instructions' "deficit spending program", and the peasants who revolt "only if the alternative is death or starvation".

**Recorded in** rulebook Section 8 and Note 7, with the hints in Appendix D, and the seventh cause in Section 16; `playthrough-sim/engine.py` (`sell_back`, `lot(PILE, ...)`, the debt guards).

### Rounding to the half million

**Ruling.** Every payment worked out as a fraction rounds down to the half million, in favour of whoever pays. That covers the auction commission (the seller keeps a quarter of the price rounded down; the Harvest Pile takes the rest, so a sale of 9 gives 2 and 7, of 7 gives 1.5 and 5.5, of 5 gives 1 and 4), the tax (each player's rate × income rounded down), and the personal disasters that take a half or a third of income, harvest or grain. The Warlord's soldier commission is a quarter of 20, so it never needs rounding.

**Why.** The smallest bag in the box is half a million, so a quarter million can't change hands. Rounding in the payer's favour means nobody is ever asked for grain the rules didn't strictly demand. Set by Manish on 2026-10-25.

**Recorded in** rulebook Section 8 (the general rule), restated in Sections 9 (tax), 10 (commission) and 15 (disasters) and in the worked round (Appendix C); `playthrough-sim/engine.py` (`pay_down`).

## I Ching cards

The deck in `i-ching.json` is reworded. Its effects follow the 1969 cards, and these are the readings it settles on.

| Card | Question | Ruling |
|---|---|---|
| Population Doubles (×3) | The original says "if this card has been played twice" | Read as "if the population has already doubled twice". A doubling takes effect at most twice in a game, matching the 600 million cap (Note 6) |
| Population Grows by Half (×2) | "if this card has been played once before" | The increase by half takes effect once in a game. The playthrough engine enforces both caps: a capped card is just a good harvest |
| The Canal Gives Way | "you must pay the Emperor 2 million" / "the Emperor must start over" | "You" is the province player. Where both of a province's canal sections are finished, that province pays the Emperor 2. Where one section stands, the Emperor must rebuild it. Unfinished work is lost |
| The Wall Is Breached | Are links destroyed? | No. Provinces 1–3 each pay 5 for repairs; a province with no Wall built above it pays 2 to the Harvest Pile instead. The repairs go to the Harvest Pile too. (Playthrough reading, game 7.) |
| Storms and Raiders | Must a province with no public works still pay the 2? | Yes. The card names Provinces 4–7 and says each pays |
| Imperial Charity | Where is the "Emperor's Treasure Chest"? | It is the Emperor's own reserve, where taxes go (Section 8), not the Harvest Pile |
| The Emperor's Share | What is split 50/50? | The extra harvest a province's public works produce that round |
| Public Utility Tax | Does the Emperor pay it too? | No. The Emperor collects it, so Province 1 doesn't pay itself: 2 from every other occupied province and 2 more from each of those with a public work. (Playthrough reading, used in games 1, 2 and 3.) |
| Storms and Raiders | Where do the repair payments go? | To the Harvest Pile, like other damages. (Playthrough reading.) |
| The Canal Gives Way | What does Province 1 pay for its own finished canal? | Nothing: the Emperor would be paying himself. (Playthrough reading, game 7.) |
| The Emperor's Share | Is new land's harvest shared? | No. New land isn't a public work. (Playthrough reading, game 7.) |
| Any card | What if a named province is empty? | Its part of the card is skipped: nobody pays, nobody plays its disaster |

## The map

`map.svg` and `map.json` were redrawn from a photo of the cloth, so province borders may be off by a square here and there.

- **Grid:** 30 × 22 squares. Rows A–V run north to south, columns 1–30 west to east, and a square is named like H12.
- **Undeveloped land:** three kinds, per rulebook Section 3: the Warlord's territory (`8` in `map.json`), the strip below the Wall (`n`), and the sea (`S`). Beyond the Wall (`B`) is off the edge of the settled country but still on the board.
- **The Wall:** 12 links, 4 above each of Provinces 3, 2 and 1, west to east.
- **The Grand Canal:** 8 sections, 2 each in Provinces 1, 4, 5 and 6.

## Playthrough engine

The engine in `playthrough-sim/` makes some assumptions so it can keep a ledger. They're listed in full in `playthrough-sim/docs/rules-model.md` under "Rulings the engine relies on" and "Simplifications". The ones a table would also meet:

- **Debt follows Note 7.** The engine refuses a payment that would put a player in debt while they still hold realia (the script must call `sell_back` first), refuses bids, purchases, voluntary deals (`act(..., deal=True)`), shares of public works and soldier purchases by a player in debt or beyond their grain, and refuses a seat change by a player in debt, except a Chaos acclamation.
- **Payments round down to the half million.** Commissions, tax and fractional disasters go through `pay_down`, so no ledger ever shows a quarter million.
- **Disasters follow the seat.** A player who moves into a province carries on that booklet's disasters where the last occupant left off.
- **The Harvest Pile is finite.** It starts at 2,500 million, the face value of the bags in the box, less the 60 dealt to each player.
- **Warlord's objective:** one piece of realia per player; a later raid on the same player replaces the earlier entry.
- **Every soldier is tracked square by square.** The engine refuses a step longer than one square, a second move in a round, a province's soldiers moving before the Warlord's, a bought soldier moving before its province is raided, a diagonal capture, and a raid the Warlord's disaster forbids. Tolls and raids are computed from the squares, not chosen by the script.
- **The Warlord's disasters.** "No raids on Provinces 5, 6 or 7" and "no raids this year" stop raids only; his soldiers may still walk onto squares that don't raid.
- **Every playthrough is its own game.** The same eight names appear in each, every player in the province their name puns on, and nothing carries from one game to another.

### Readings the playthroughs rely on

Judgement calls made while writing the games. None overrides a rule; each fills a silence the way a table would. Raise any of them with Manish if they look wrong.

- **The Warlord's objective counts raids, not holdings.** "Raid a different piece of realia from each player" is met by the raid itself: a piece he has since sold back or on still counts, and a piece he once sold to a player counts when he raids it back from that player. Game 5 takes a Customs House, Jar, Scroll and Vase from four different players, plus a palace, so it satisfies the strictest reading too.
- **The Warlord may sell raided realia privately**, to anyone, as an ordinary trade; the buyer places it at once (Note 10). Games 4 and 5.
- **Private deals are allowed for anything**, including paying a player to leave a piece unguarded or a Gentry to hold a piece (games 3 and 5). The engine records only the grain.
- **A bought soldier may be placed on its buyer's own realia** (games 4 and 5); it then guards the piece, since the Warlord can take it only by capturing first, straight on.
- **Twenty in hand caps a useful bid.** A player who must keep 20 to change seats can't usefully bid past their grain less 20 for a piece that completes their set (game 5, Year 7).
- **Authored stopping points.** The short game stops after the agreed eight rounds (Note 19). Game 5 stops when the Warlord takes the throne: the rules don't end the game there, but the table agrees to.
- **The Warlord may bid at auction.** Nothing forbids it. What he buys goes on a square of his own territory, where no raid can reach it, and he may sell it privately (games 2 and 5). Selling a raided piece back is a private trade, so the Warlord keeps the whole price; nothing goes to the Harvest Pile (games 4 and 5).
- **A capture can also be a raid.** A Warlord soldier that captures a bought soldier standing on an un-raided province square raids that square too, and may take the realia on it (game 5). During a "no raids" disaster that capture is refused, because the raid is (game 1).
- **The Emperor's Share card and tax.** Tax is levied on the round's income before the share is paid, and rent paid or received never enters taxable income (games 1 and 5).
- **Returned pieces are re-auctioned at the next auction step**, which is the same round's if the seat change comes before the auction (Section 10, "as soon as possible").
- **A player may decline the throne.** Noah, holding every piece but one in game 2, chooses not to buy the last: nothing obliges a player to complete a set.
- **Rent is negotiable, and an agreed rate stays with the seat.** The Gentry may agree a rate with the peasants for a concession; each later Gentry collects the same (game 6).
- **A seller's minimum bid may be anything**, even tied to one player's grain. A lot nobody meets stays in stock and is offered again every round, and a player may pay the seller to keep a minimum where it is (game 6, a private deal).
- **A seat change may be declared after the round's card is turned and before the harvest**, so the mover collects the new province's harvest (game 6). Section 5 allows deals "at any point in the round".
- **"Sharing the cost" of new land** is satisfied by any share from the crown, even 1 a square (game 6).
- **A revolt short of two supporters simply doesn't happen** (game 6).
- **During Chaos:** the deposed Emperor stays in Province 1, pays its consumption and takes its raids, and her grain is the reserve the next Emperor takes (games 2 and 7). No new land can be bought, since there is no Emperor to pay the share (game 7). A revolt declared after the tax is announced but before it is paid voids that year's tax, and Chaos can end mid-round: the new Emperor declares tax, builds, buys land and pays salaries in the round of the acclamation (game 7).
- **How the acclamation is counted** (game 7, proposed at the table by Rich). Each claimant's grain in hand, soldiers on the board, and friends (players backing that claim, one claim each) are counted. One qualification is enough if no rival leads in another; otherwise the claimant who leads in more of the three wins, and a tie in any count leads nobody. The deposed Emperor can't claim and her grain isn't counted, but she may back a claimant; the Warlord may claim. Section 16 only lists the qualifications, so this is the playthroughs' procedure, not the rulebook's.
- **A seat change in the last round, before the last work is built, counts for scoring** (game 7).

## Open questions

Raise these with Manish before relying on an answer.

- **A negative Emperor.** Under Note 7 a crown in debt can't pay toward public works; it still declares and collects tax. Does it still owe salaries (they're payments owed, so they'd deepen the debt), or does an empty reserve excuse them? "Too low a grain reserve" is already a revolt cause, which may be all that's needed. No playthrough has an Emperor in debt.
- **Selling soldiers back.** The rules give no price for selling a soldier back to the Warlord or the pile, so the playthroughs never do it. Should a player in trouble be able to?
- **The strip along the southern river between Provinces 3 and 7.** No dotted border seems to claim it, so `map.json` treats it as the Warlord's undeveloped land. Check against the cloth.
- **A displaced player's bought soldiers.** When a player is replaced in a seat change, do their soldiers go to the player who replaced them, stay theirs, or return to the Warlord's stock? The booklets don't say. No playthrough needs an answer yet; the engine refuses the case.

- **Does a palace-only round trigger the Pagoda rule?** The Emperor's booklet: "Build one Public Works project. If you are building none of the systems, you must build the Marble Pagoda." The palaces aren't systems (the systems are the Wall, the Canal, the irrigation system and the reservoirs), so read literally, every round that builds the Summer or Winter Palace and no system must also build the Pagoda, which one project a round (Note 13) doesn't allow. All five playthroughs read it as "when you build nothing else, build the Pagoda": a palace may be built in a round without a system, and the Pagoda is built in its own round. Not yet confirmed.
- **The Warlord's soldiers when he changes seats.** When the Warlord completes his objective and takes another seat (game 5), who commands the Warlord soldiers standing on the board, and the bought soldiers of the player he displaces? Game 5 stops at that moment, so it doesn't need an answer.

(Answered on 2026-10-25 and moved to Clarifications: which rivers charge a toll, and who is paid for crossing a Wall link or canal section.)
