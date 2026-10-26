# Rulings

Every rules question this project has settled, in one place. The 1969 game spreads its rules across eight booklets, a General Instructions sheet and the printing on the can. They sometimes disagree, and often say nothing. This file records what was decided, why, and where the decision lives.

**Everyone working on this repo, human or Claude, adds their rulings here.** That includes clarifications that never become a numbered rulebook note, and the assumptions the playthrough engine makes. If you decide how a rule works, write it down here before you build on it. If a question comes up that you can't settle from the sources, put it under [Open questions](#open-questions) and ask Manish. Don't invent an answer.

Each entry gives the question, the ruling, the reasoning, and where it's recorded. "Note N" means the numbered note in `combined-dynasty-rulebook.html`: a pink box where the rule applies, repeated in Appendix D with the original wording. Notes are numbered in reading order, so adding one renumbers every later note. When that happens, update this file and every `Note N` reference in `playthrough-sim/`.

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
| 7 | Is tax owed on a negative income? | No |
| 8 | What is the extra realia each province starts with at 4–5 players? | A pattern, not a ruling. It's always the one type that province never needs: 2 and 5 swap, and 3 → 6 → 4 → 7 → 3 form a ring |
| 9 | Is unsold stock on the map? | No. A piece goes on a square in the buyer's province the moment it's bought or traded. Returned pieces rejoin their province's unsold stock. Otherwise the Warlord could raid most of his objective in Round Two |
| 10 | Can a Peasant become Emperor directly? | No. The peasants' Objectives sections govern over the shared "Becoming Emperor" boilerplate. A Peasant must first take an upper-class seat |
| 11 | Where does a returned piece go if its home province is empty? | To the province that started the game holding it, to be auctioned again as soon as possible |
| 12 | One public works project per round, but the Emperor's booklet allows "any number of sections" | One project per round. A project may be any number of sections of the same work |
| 13 | What does reclaiming a raided square do? | Removes the marker. The square still can never be raided again |
| 14 | Booklets: soldiers capture horizontally only. General Instructions: horizontally and vertically | The General Instructions win: capture orthogonally, never diagonally. Movement may be diagonal |
| 15 | How far do the Warlord's soldiers move? | One square a round, like every soldier. "Anywhere" means no square is off limits. Every crossing of a river or public work costs 5 |
| 16 | What does Chaos stop? | No tax, salaries or public works until a new Emperor emerges. Harvests continue and the Warlord still raids |
| 17 | How is the game scored? | Final province against starting province, grain surplus as the tiebreak. An Emperor still on the throne has won |
| 18 | The eight-round short game | An addition, not a reading of the rules. Agree before setup; score as normal |
| 19 | The Scholar's realia at six players (missing from the booklet) | Two Bamboo Brushes, like every other province |

## Clarifications

These follow from the rules rather than overriding them, so they get a plain sentence in the rulebook (or none) rather than a numbered note.

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

**Ruling.** Only after that province's population has doubled (24 million for Provinces 2–4, 28 million for 1 and 5–7). Provinces 2 and 3 must also have all four Wall links above them built. Each square costs 20 from the Harvest Pile and yields 20 every round afterwards; the cost and the yield are negotiated with the Emperor.

**Recorded in** rulebook Section 13 and every province's reference card.

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

**Why.** The Warlord's booklet lets him go "across water", but Note 15 says Provinces 4 and 5 can be reached only through the gap in the west, which is true only if the coast is closed. Confirmed by Manish on 2026-10-25.

### Moving onto a square

**Ruling.** A Warlord soldier that steps onto an un-raided square of an occupied province raids it; that isn't optional. Stepping onto undeveloped land, a raided square or a square of an unoccupied province raids nothing and costs nobody anything (Note 4). Any soldier may stand still for a round. Soldiers of the same owner may share a square ("marched together as a group"); a square holding an enemy soldier can be entered only by capturing it, horizontally or vertically (Note 14).

**Why.** Section 14: "A Warlord soldier raids the square it moves onto." Confirmed by Manish on 2026-10-25, as was stacking for one owner only.

### Placing pieces

**Ruling.** Realia can't go on a raided square or under a palace or cut-out, and a palace or cut-out can't go on a square holding realia. A soldier may stand on a square holding realia. Realia the Warlord takes goes on a square of his own territory. Wall links and canal sections are built in the order printed on the map (link 1 first, section 1 first).

**Why.** A raided square "may hold realia" only after reclaiming (Note 13), so before that it can't. The cut-out rule is the Setup guidance. Confirmed by Manish on 2026-10-25.

### Bought soldiers after a seat change

**Ruling.** A bought soldier belongs to the player who bought it, and stays where it stands when that player changes seats. It still can't move until the Warlord has raided the province it was bought in.

**Why.** Soldiers are bought with the player's own grain, and on a seat change the mover keeps their grain. Recommended to Manish on 2026-10-25; he asked which made more sense and hasn't overruled it. What happens to a *displaced* player's soldiers is unsettled (see Open questions); the engine refuses that case, and no playthrough needs it.

## I Ching cards

The deck in `i-ching.json` is reworded. Its effects follow the 1969 cards, and these are the readings it settles on.

| Card | Question | Ruling |
|---|---|---|
| Population Doubles (×3) | The original says "if this card has been played twice" | Read as "if the population has already doubled twice". A doubling takes effect at most twice in a game, matching the 600 million cap (Note 6) |
| Population Grows by Half (×2) | "if this card has been played once before" | The increase by half takes effect once in a game |
| The Canal Gives Way | "you must pay the Emperor 2 million" / "the Emperor must start over" | "You" is the province player. Where both of a province's canal sections are finished, that province pays the Emperor 2. Where one section stands, the Emperor must rebuild it. Unfinished work is lost |
| The Wall Is Breached | Are links destroyed? | No. Provinces 1–3 each pay 5 for repairs; a province with no Wall built above it pays 2 to the Harvest Pile instead |
| Storms and Raiders | Must a province with no public works still pay the 2? | Yes. The card names Provinces 4–7 and says each pays |
| Imperial Charity | Where is the "Emperor's Treasure Chest"? | It is the Emperor's own reserve, where taxes go (Section 8), not the Harvest Pile |
| The Emperor's Share | What is split 50/50? | The extra harvest a province's public works produce that round |
| Public Utility Tax | Does the Emperor pay it too? | No. The Emperor collects it, so Province 1 doesn't pay itself: 2 from every other occupied province and 2 more from each of those with a public work. (Playthrough reading, used in games 1, 3 and 4.) |
| Storms and Raiders | Where do the repair payments go? | To the Harvest Pile, like other damages. (Playthrough reading.) |
| Any card | What if a named province is empty? | Its part of the card is skipped: nobody pays, nobody plays its disaster |

## The map

`map.svg` and `map.json` were redrawn from a photo of the cloth, so province borders may be off by a square here and there.

- **Grid:** 30 × 22 squares. Rows A–V run north to south, columns 1–30 west to east, and a square is named like H12.
- **Undeveloped land:** three kinds, per rulebook Section 3: the Warlord's territory (`8` in `map.json`), the strip below the Wall (`n`), and the sea (`S`). Beyond the Wall (`B`) is off the edge of the settled country but still on the board.
- **The Wall:** 12 links, 4 above each of Provinces 3, 2 and 1, west to east.
- **The Grand Canal:** 8 sections, 2 each in Provinces 1, 4, 5 and 6.

## Playthrough engine

The engine in `playthrough-sim/` makes some assumptions so it can keep a ledger. They're listed in full in `playthrough-sim/docs/rules-model.md` under "Rulings the engine relies on" and "Simplifications". The ones a table would also meet:

- **Debt is allowed.** Grain can go negative. The rules don't address it.
- **Disasters follow the seat.** A player who moves into a province carries on that booklet's disasters where the last occupant left off.
- **The Harvest Pile is finite.** It starts at 2,500 million, the face value of the bags in the box, less the 60 dealt to each player.
- **Warlord's objective:** one piece of realia per player; a later raid on the same player replaces the earlier entry.
- **Every soldier is tracked square by square.** The engine refuses a step longer than one square, a second move in a round, a province's soldiers moving before the Warlord's, a bought soldier moving before its province is raided, a diagonal capture, and a raid the Warlord's disaster forbids. Tolls and raids are computed from the squares, not chosen by the script.
- **The Warlord's disasters.** "No raids on Provinces 5, 6 or 7" and "no raids this year" stop raids only; his soldiers may still walk onto squares that don't raid.
- **New evenings, new booklets.** Each playthrough after the first three deals the booklets afresh (`setup(cast=...)`); a player id is still the seat that player drew.

### Readings the playthroughs rely on

Judgement calls made while writing the games. None overrides a rule; each fills a silence the way a table would. Raise any of them with Manish if they look wrong.

- **The Warlord's objective counts raids, not holdings.** "Raid a different piece of realia from each player" is met by the raid itself: a piece he has since sold back or on still counts, and a piece he once sold to a player counts when he raids it back from that player. Game 5 takes a Customs House, Jar, Scroll and Vase from four different players, plus a palace, so it satisfies the strictest reading too.
- **The Warlord may sell raided realia privately**, to anyone, as an ordinary trade; the buyer places it at once (Note 9). Games 2 and 5.
- **Private deals are allowed for anything**, including paying a player to leave a piece unguarded or a Gentry to hold a piece (games 3 and 5). The engine records only the grain.
- **A bought soldier may be placed on its buyer's own realia** (games 2 and 5); it then guards the piece, since the Warlord can take it only by capturing first, straight on.
- **Twenty in hand caps a useful bid.** A player who must keep 20 to change seats can't usefully bid past their grain less 20 for a piece that completes their set (game 5, Year 7).
- **Authored stopping points.** The short game stops after the agreed eight rounds (Note 18). Game 5 stops when the Warlord takes the throne: the rules don't end the game there, but the table agrees to.
- **The Warlord may bid at auction.** Nothing forbids it. What he buys goes on a square of his own territory, where no raid can reach it, and he may sell it privately (games 1 and 5). Selling a raided piece back is a private trade, so the Warlord keeps the whole price; nothing goes to the Harvest Pile (games 2 and 5).
- **A capture can also be a raid.** A Warlord soldier that captures a bought soldier standing on an un-raided province square raids that square too, and may take the realia on it (game 5). During a "no raids" disaster that capture is refused, because the raid is (game 4).
- **The Emperor's Share card and tax.** Tax is levied on the round's income before the share is paid, and rent paid or received never enters taxable income (games 4 and 5).
- **Returned pieces are re-auctioned at the next auction step**, which is the same round's if the seat change comes before the auction (Section 10, "as soon as possible").
- **A player may decline the throne.** Noah, holding every piece but one in game 1, chooses not to buy the last: nothing obliges a player to complete a set.

## Open questions

Raise these with Manish before relying on an answer.

- **The strip along the southern river between Provinces 3 and 7.** No dotted border seems to claim it, so `map.json` treats it as the Warlord's undeveloped land. Check against the cloth.
- **A displaced player's bought soldiers.** When a player is replaced in a seat change, do their soldiers go to the player who replaced them, stay theirs, or return to the Warlord's stock? The booklets don't say. No playthrough needs an answer yet; the engine refuses the case.

- **Does a palace-only round trigger the Pagoda rule?** The Emperor's booklet: "Build one Public Works project. If you are building none of the systems, you must build the Marble Pagoda." The palaces aren't systems (the systems are the Wall, the Canal, the irrigation system and the reservoirs), so read literally, every round that builds the Summer or Winter Palace and no system must also build the Pagoda, which one project a round (Note 12) doesn't allow. All five playthroughs read it as "when you build nothing else, build the Pagoda": a palace may be built in a round without a system, and the Pagoda is built in its own round. Not yet confirmed.
- **The Warlord's soldiers when he changes seats.** When the Warlord completes his objective and takes another seat (game 5), who commands the Warlord soldiers standing on the board, and the bought soldiers of the player he displaces? Game 5 stops at that moment, so it doesn't need an answer.

(Answered on 2026-10-25 and moved to Clarifications: which rivers charge a toll, and who is paid for crossing a Wall link or canal section.)
