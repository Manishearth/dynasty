# The full game: report

An agent-played game of Dynasty with all eight provinces, from a fresh setup to its natural end. Each seat was a tool-less `dynasty-player` agent in character, every cast member in the province their name puns on. One Storyteller session per chapter refereed through the engine, and a Director session checked each chapter, wrote the handoffs and rebuilt `playthroughs-real.html` after every year. The deck was shuffled with seed `19691108` (`seed.md`), with no pre-steering.

**It ended in Year 13 in survival:** every one of the 1,030 owed in public works was built, under four Emperors. Reina, who drew the throne, lost it in Year 2 and won it back in Year 12. In Year 13 she built the last work, the Province 2 Irrigation System, herself.

The record:
- `game.py`: 516 entries, with `RESULT = export(...)`; run it with `run.py`.
- `log/year1–13/`: every prompt and reply.
- `ledger.md`, `diaries/` and `narration.md`.
- `state/setup.json` and `year1–13.json`.
- `handoff/chapter-0–6.md`.
- `outtakes/`: two set-aside takes of Year 13 (below).

## The story in brief

**Chapter 1, "Very Civilised" (Setup–Year 2).** Rob stood his four soldiers a step from every province but the throne's. Lots sold for 6–8. Rich, the Gentry, kept the rent at the minimum, bid on exactly the pieces he'd announced, and took the throne from Reina in Year 2, "with the deepest respect".

**Chapter 2, "I'll Remember the Price" (Years 3–4).** Rich built only in his own Province 1. Graham won nothing for two years, then five pieces, "Not on a tie. Not twice", and took the Official's seat from Clark: "I'll take the seat, and the pen." Rob raided his first two pieces.

**Chapter 3, "A Price for a Throne" (Years 5–6).** Three seat changes in one auction, and nobody took the throne. Whoever sits on it can be unseated by the next complete set, reserve and all. The Official's chair changed hands four times in two years. Noah set a Scroll's minimum at 365, half a grain past Reina's reach: "a price for a throne, not for a scroll". Silke finally won and took the Official's seat.

**Chapter 4, "Paddy, Settled" (Years 7–8).** Silke paid Reina's 150 for the last Jar and took the throne, its first change since Year 2. Clark and Paddy kept a two-year public deal, and Paddy took Noah's Gentry seat.

**Chapter 5, "What One More Round Costs" (Years 9–10).** Graham completed a set two lots into an auction and took the throne. Reina climbed through the Gentry's seat. 210 of the works were left, in three projects.

**Chapter 6, "Fifty, to the Letter" (Years 11–12).** The first population card came in Year 11, after ten years at ×1, and in Year 12 the population doubled to ×3. Graham, as Emperor, paid 15 of every 20 on new land, and the table bought 34 squares. The crown went from 634 to 6. Graham then whispered to Rich to make Reina pay "what my chair is worth". Rich promised "no Deed under fifty", and Reina paid exactly 50 and took the throne back.

**Chapter 7, "Thirty Grain and a Shovel" (Year 13), the third take.** Manish's new ruling was announced first: the crown may build a negotiated work alone if it pays the whole cost. Reina taxed at 20% and built the irrigation for 30, over Graham's public objection: "A gift to Province 2 that closes every other shelf at this table isn't a gift to Province 2." The game ended in the works step, before the auction.

### The two set-aside takes of Year 13 (`outtakes/`)

- **First take:** with one work left, Reina promised the crown would pay "every new square, in full". The table bought 520 of land, and the crown went from 474 to 4. Graham wouldn't pay 26 of the 30, nothing was built, and a raid left the crown 22 in debt. Manish set it aside: land bought in the last year can't pay back. The tools now say so to every player once the game can end this year or next (`briefs.py`, `endgame_note`).
- **Second take:** Graham, the Official, refused the irrigation even at the crown's whole cost and with 100 on top, so that the game wouldn't end ("You said nobody would have a reason to sign anything, so I'm not signing for the ditch"). The crown ended 16 in debt. Manish ruled that the crown may build a negotiated work alone if it pays the whole cost (RULINGS, Clarifications; rulebook §12), and asked for the year to be replayed with the ruling in force.

Each take was restored from the end of Year 12 by script, and verified against `state/year12.json`. Every cut piece is in `outtakes/` with a README.

## Verdicts

Survival ending (§18): each player's final seat against the one they drew, grain breaking ties.

| Player | Drew | Ended | Grain | Verdict |
|---|---|---|---|---|
| Reina | Emperor | Emperor | 494 | won (held the throne at the end) |
| Graham | Wheat Peasant | Official | 98 | won |
| Silke | Silk Peasant | Scholar | 92.5 | won |
| Rich | Gentry | Gentry | 48.5 | held |
| Rob | Warlord | Warlord | 178.5 | held (two names short of his objective) |
| Clark | Official | Silk Peasant | 100.5 | lost |
| Noah | Scholar | Rice Peasant | 145.5 | lost |
| Paddy | Rice Peasant | Wheat Peasant | 52.5 | lost |

**Thirteen seat changes, four of them on the throne:**
- Rich (Year 2);
- Silke (Year 7);
- Graham (Year 9);
- Reina (Year 12).

**Rob** never bought a lot. He raided Clark's Scroll, Noah's Customs House, Paddy's Jar and the Winter Palace (the eight-player wildcard), and needed two more names.

## Best lines

- Rich, taking the throne: "you've been a gracious, moderate and very civilised sovereign, and I've loved every grain of it… with the deepest respect, I'll take the throne." (Year 2)
- Graham: "Not on a tie. Not twice. Eighteen, Silke." Then, taking the Official's seat: "I'll take the seat, and the pen." (Year 4)
- Rob: "The desert doesn't buy, it collects."
- Reina: "I'd be Empress for exactly one auction." Noah: "I'd have been a very expensive Emperor for one auction." (Year 5)
- Rob: "The chair passes round this table faster than the gravy."
- Clark: "a fresh page headed 'Paddy, settled', which is the first page in that ledger that isn't a grievance." (Year 7)
- Graham, on the crown's canal: "the first gift from the crown that came without a receipt attached."
- Graham: "I've just learned what happens to a man who keeps his set in a drawer for one more round." (Year 9)
- Clark's diary: "the man waiting on the last lot is the one who gets eaten."
- Reina: "I can count to one auction." (Year 12)
- Rich's diary: "I kept my promise to the letter and it did him no good at all. I'll write that down as a lesson in how narrow a promise ought to be."
- Graham's diary: "when you spend the whole treasury to be generous, you get thanked in the minutes, and then the minutes go to whoever has the most grain left."
- Graham, at the end: "Nobody here will live long enough to drink from it." Reina: "I thought I'd spare you all one more afternoon of it."
- Rob, at the end: "W3 and W5 were close enough to read the price tags."

## New land: did the table buy it, and how did it go?

**Yes, and it saved the game.**
- **The doubling came late.** In this shuffle the first population card arrived in Year 11, so new land opened only in Year 12, at ×3.
- **The land rush.** The tools put land in every eligible menu from the doubling, with each player's own break-even numbers. Graham, as Emperor, paid 15 of every 20, and the table bought **34 squares** that year: Province 1 6, 2 6, 3 3, 4 2, 5 7, 6 6 and 7 4.
- **What it did.** In the final year Clark's sea alone paid +90 at ×3. Nobody went into debt in the take that counts. The contrast is Peasant collapse, which bought no land and collapsed at ×3.
- **The cost.** The crown's reserve fell from 634 to 6. Reina rebuilt it from tax and won the throne back the same year.
- **The lesson from the outtakes** is the other side of it: land bought in the last year can't pay back. The first take of Year 13 spent 520 on it and stalled. The endgame note now in `briefs.py` tells players when the game can end this year or next.

## Steering

None up front. During the game, all logged in `seed.md`:
- **Strategy tips:** from Chapter 4, at most one per player per chapter, public, and using only what the table could see. Three were given:
  - Rich, Year 7: the works owed and the population cards to come; he built a canal.
  - Silke, Year 9: four projects left; she built the Wall above Province 2.
  - Rich, Year 12: his strip opens only with the Wall above it; he negotiated it with the crown.
- **Year 13 replayed twice,** as above.
- **Rules settled by Manish during the game:**
  - an unsold lot reopens at 2 the next round;
  - unsold stock is sold only at auction;
  - the crown may build a negotiated work alone;
  - pieces move to the new province on a seat change (the rulebook kept as written).

  The first three are now in `RULINGS.md` and the rulebook.

## Usage

| | 5-hour window | Weekly (all models) |
|---|---|---|
| Before Chapter 1 | 13% | 5% |
| After Chapter 1 | 16% | 6% |
| After Chapter 2 (the window reset mid-chapter) | 2% | 7% |
| After Chapter 3 | 6% | 8% |
| After Chapter 4 | 9% | 8% |
| After Chapter 5 | 13% | 9% |
| After Chapter 6 | 16% | 10% |
| After Year 13, first take (reset) | 4% | 11% |
| After Year 13, second take | 7% | 12% |
| After Year 13, third take (end) | 9% | 12% |

- **Fable weekly usage:** 0% throughout. Everything stayed well within the Max plan, and no limit came close.
- **Storyteller context at each chapter's end:** about 484k, 500k, 517k, 500k, 575k, 565k, then 480k, 490k and 335k for the three takes of Year 13. Two-year chapters at eight seats always passed the 450k line during their second year; the stop rule ("finish the year") held them there.
- **What cut context:** quiet engine checks (`run.py --quiet`); short follow-ups (`--short`); one auction prompt per bidder per year (batched); live raises only on near-ties of 10 or more.
- **Director:** about 610k of context over the whole game.

## Continuity and drift

- **"The minutes" became everyone's.** Clark's ledger of grievances ("page one, line one") was quoted back by Rich and Rob in Chapter 1 and used by the whole table by Chapter 4. It's the same drift Peasant collapse had with Graham's records. The handoffs kept the Storytellers from feeding it.
- **Voices held across thirteen seat changes.** Reina stayed the manager on four seats, Rich the fawner who keeps promises "to the letter", Noah the honest arithmetic, Graham the quiet scorekeeper ("I'll remember the price"), and Rob the gleeful villain.
- **Public slips** were caught by notes: grain totals, who paid what, seat names, and several players believing a peasant could take the throne directly. The last one stopped once the board card said whom a set lets you replace.
- **Hand-written text got in where the tools were bypassed:**
  - Chapter 3 trimmed auction prompts by hand.
  - Two launches paraphrased a character line (Chapters 4 and 7).
  - Three stray empty launches went out by mistake (Chapters 4 and 6), none played.
  - Each was logged, and each led to a tool fix (`--short` keeps the card; launches go out exactly as printed).
- **Corrections on the page:** a bold "correction from the Storyteller" entry (Year 5's Vase priced at 62, not 61) was replaced, at Manish's request, by fixing the original lot. Corrections now go where the mistake is.
- **Diaries are in character,** and their small slips are kept word for word: Reina's last entry says she paid salaries the ending made moot.
- **Narration** held its register, mostly one or two sentences a line. It's off the page, in `narration.md`.

## Engine and tool gaps

**Not applied by the engine** (scripted as `act()`s):
- the Emperor's Share, the Wall breach, Storms and Raiders' repairs, and Imperial Charity;
- minimum bids and the unsold-lot rule;
- the one-project-a-year rule and the works' prerequisites.

**Fine as it is:**
- A forced payment beyond a player's grain becomes a debt, which is Note 7 as written.
- `give()` moves only placed pieces, which matches the stock ruling.

**A seat change mid-auction** needs provisional squares in `game.py` for the displaced player's just-won piece; the precedent is in the ledger.

**Tools built or fixed during the game** (`playthrough-sim/agents/`):
- `briefs.py` works at any table:
  - job menus (crown, rent, collect, I Ching), land, and the batched auctions with `--floor`;
  - multi-lot `place`, `--short`, `launch:<kind>`, `diary` and `seen all`;
  - board cards that name whom a set can replace, and free squares only;
  - the Warlord's objective from the engine (with the palace wildcard);
  - desert squares for a raided piece;
  - the endgame land note.
- `run.py --quiet`, and palace raids shown as 20.
- `build_real.py` builds games in progress year by year, with title and description overrides.

**The Bash tool** fails on heredocs with backticks or non-ASCII text. Every Storyteller used the file tools instead.

**The harness:**
- A session can start another only on a turn Manish began, so every chapter after the first was a card for him to click.
- Detaching each Storyteller, and having it message the Director only at year ends, kept the Director quiet between years.
