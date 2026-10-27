# The pilot game: report

An agent-played game of Dynasty at the peasant game's five-player table, from a fresh setup to its natural end. Five tool-less `dynasty-player` agents played the seats in character. Four Storyteller sessions, one per two-year chapter, refereed through the engine, and a Director session checked each chapter and wrote the handoffs. There was no steering: the deck was shuffled with seed `20261027` (`seed.md`).

**It ended in Year 8 in an economic collapse.** After the population tripled, every income was negative under every card. Every player went into debt, and the table voted unanimously, in character, to give up (§18). A collapse has no winners. 200 of the 520 owed in public works were built.

The record: `game_pilot.py` (run with `run.py`), `log/year1–8/` (102 numbered turns), `ledger.md` (rulings P1–P22), `diaries/`, `narration.md`, `state/setup.json` and `year1–8.json`, and `handoff/chapter-1–3.md`. Not built into `playthrough.html`; that's Manish's call.

## The story in brief

**Chapter 1, "The Only Bowl in China" (Setup–Year 2).**
- Rob placed his army on the notch and below Paddy's coast, and refused tax.
- Reina taxed at 40% and built the Summer Palace, then the first Province 1 canal section.
- Paddy took the only Dragon Jar from Graham, 17 to 16. Both had offered to stand aside for a favour, and both bid anyway.
- Silke paid 25 for the only Wooden Bowl after a live raise against Graham.
- A canal card injured Rob's soldiers, and Year 2 passed without a raid.

**Chapter 2, "A Lovely Thing to Lose" (Years 3–4).**
- Every promise was kept at the minimum price (2), until the Vase. Silke asked Paddy to stand aside, as she had for him; he wouldn't ("I can't give you the whole game for a favour like that"). He won it 29 to 28 and replaced Silke as the Silk Peasant: the first seat change.
- In Year 4 a bad harvest on a population half again as large sent every province into the pile.
- Graham bought the Jar, and Rob's soldiers took their first piece, Graham's Brush.
- Manish ruled that the Silk Peasant may take the throne. That made Silke's Bowl, promised to Graham, the piece that would crown Paddy.

**Chapter 3, "Next Year's Another Year" (Years 5–6).**
- Paddy kept his word and stayed out of the Bowl, which would have won him the throne. Graham bought it for 2.
- The population doubled in Year 6, so there was no tax and no works.
- Graham bought his raided Brush back from Rob for 30, completed his Wheat set and took Paddy's seat as Silk.
- Rob's march captured Silke's newly bought guard and took her Scroll in the same step, then took Paddy's Scroll. That finished his objective, and he took the throne with 185. Reina went to the desert as the Warlord, keeping the army under Manish's new-Warlord ruling (P19).

**Chapter 4, "A Lovely Thing to Owe" (Years 7–8).**
- Year 7's bad harvest put Silke and Paddy in debt.
- Rob, as Emperor, paid for his first public work, the last Province 6 canal section.
- Graham bought a Scroll and stood one Vase short of the throne, with exactly 20 grain. Paddy held the Vase back until Silke could bid too.
- In Year 8 the Emperor's Share card put everyone into debt. Graham had to sell all four of his pieces back to the pile at 2 each, and nothing was left on the board.
- Silke proposed giving up, and all five said yes, Graham last.

## Verdicts

A collapse has no winners (§18). The seats where the table stopped, with the seat verdicts `export()` records "for the record only" (its results note says the collapse means nobody won):

| Player | Drew | Ended | Grain | Seat verdict |
|---|---|---|---|---|
| Reina | Emperor | Warlord | −5 | lost |
| Silke | Silk Peasant | Rice Peasant | −67 | lost |
| Paddy | Rice Peasant | Wheat Peasant | −57.5 | lost |
| Graham | Wheat Peasant | Silk Peasant | −12 | won |
| Rob | Warlord | Emperor | −45 | won |

If the page is built, it should make the no-winners ending plain, so the "won" column doesn't read as a result.

Three seat changes: Paddy replaced Silke as Silk (Year 3); Graham replaced Paddy as Silk, and Rob took the throne from Reina (both Year 6).

## Best lines

- Rob, to the Emperor: "The Emperor pays the desert, she just doesn't know it yet." (001)
- Silke: "Your Vase is no good to me without the Bowl, Graham, and you know it, so that offer was empty." (027) Graham: "Now that you have the Bowl, it's no good to you without the Vase." (028)
- Silke, losing the Vase and her seat: "Take it, Paddy. And remember I'm the one who held the bank while you did it." (044)
- Paddy: "I can't give you the whole game for a favour like that." (045)
- Rob: "Mind you, it's a lovely thing to own, and a lovely thing to lose." (042)
- Graham: "Without it a jar is no use to you, it's just a pot." (052)
- Paddy, passing up the throne: "a man who breaks his word the minute it gets expensive was never worth the trust in the first place." (065)
- Rob, raiding: "Paddy, your customs house is under new management, and my man's very good with paperwork." (068)
- Reina, leaving the throne: "I built you a lovely house. Now you get to pay for the rest of the street." (080)
- Rob: "Lovely thing to own, a canal. Very hard to start a revolt about." (Year 7)
- Reina, at the end: "It was the best-run collapse I've ever had the honour to sit through."
- Graham, at the end: "everyone at this table kept their word to me this year. I didn't expect to write that twice."
- Rob's diary: "nobody's noticed the desert never made any."
- The narrator (075): "Robert Land, who never paid a grain of tax, walks into the Winter Palace with 185 and the book."

## Why it collapsed: the income figures

Income is harvest + works bonus − consumption × the population multiple (`engine.income`). Consumption is 60 for the Emperor, 40 for each peasant and 20 for the Warlord. The works bonuses at the end were +20 for Province 1 (two canal sections) and +20 for Province 6 (two canal sections), with none for 5, 7 or 8.

**The population cards:**

| Year | Card | Effect | Multiple |
|---|---|---|---|
| 3 | half2, Population Grows by Half | counted | ×1.5 |
| 5 | half1, Population Grows by Half | capped: the half counts once, so only a good harvest | ×1.5 |
| 6 | double1, Population Doubles | counted | **×3** |

`double3` (Year 11 in the deck order) and `double2` (Year 18) were never drawn. Either would have taken the table to ×6.

**Each seat's income by harvest** (with the end-of-game bonuses):

| Seat (holder at the end) | ×1 good / avg / bad | ×1.5 | ×3 (final) |
|---|---|---|---|
| 1 Emperor (Rob), +20 | 60 / 35 / 10 | 30 / 5 / −20 | **−60 / −85 / −110** |
| 5 Silk (Graham) | 60 / 35 / 10 | 40 / 15 / −10 | **−20 / −45 / −70** |
| 6 Rice (Silke), +20 | 80 / 55 / 30 | 60 / 35 / 10 | **0 / −25 / −50** |
| 7 Wheat (Paddy) | 60 / 35 / 10 | 40 / 15 / −10 | **−20 / −45 / −70** |
| 8 Warlord (Reina) | 20 / 10 / 0 | 10 / 0 / −10 | **−20 / −30 / −40** |

At ×3, no seat is positive under any harvest; the best case is Silke's 0 on a good harvest. No tax is raised on negative income (N8), so the crown can't fund works, and a player in debt can't bid, buy land or fund anything (N7).

**Two things made it fatal rather than just hard:**
- **Unsold stock can't be sold back.** The engine allows selling back only pieces on the board (P20). Silke and Paddy each had pieces still in stock, but nothing on the board, so they went straight into debt.
- **New land came too late.** It opens with the doubling and yields 20 a square, but needs grain up front. By Year 7 only Graham and Rob had any, and Year 7's bad harvest took it.

Year 7 (bad) and Year 8 (average, plus the Emperor's Share) finished it. For comparison, peasant game 4 survived its Year 8 doubling only because Paddy paid Reina 130.

## Usage

| | 5-hour window | Weekly (all models) |
|---|---|---|
| Before Chapter 1 | 3% | 2% |
| After Chapter 1 | 5% | 3% |
| After Chapter 2 | 8% | 4% |
| After Chapter 3 | 10% | 4% |
| After Chapter 4 (end) | 12% | 5% |

- **Weekly Fable usage:** 0% throughout. Everything stayed within the Max plan, and no limit came close.
- **Storyteller context at the end of each chapter:** 357k, 400k, 360k and 328k. Two-year chapters are about the most one Storyteller can hold; the 400k stop rule never had to cut a chapter short.
- **Player agent turns:** 102 numbered log entries plus the diary requests. The completion notices reported 1,614,326 tokens in all (`log.md`). As in the trial year, that figure counts each player's whole context on every turn, so most of it is probably cache reads.
- **Director:** about 300k of context over the whole game.

## Drift and continuity problems

- **Record-keeping spread from Graham to everyone.** Silke's Chapter 1 diary ends "So do I now"; Reina kept "the tally"; by Chapter 2 the peasants swore by "Reina's book"; Rob's farewell asks "the minutes" to show things. Each handoff said not to feed the bit, and the Storytellers didn't, but the players fed it to each other through the ledger and the diaries. It became the table's shared joke rather than Graham's: arguably good table texture, but it's continuity drift.
- **Narration ran long.** The voice held (chronicle register, no favourites, no spoilers), but lines crept to three sentences and dense arithmetic in every chapter despite the handoff notes. One factual error (068) was corrected with a later narration line, not rewritten, which worked well. The Chapter 4 Storyteller wrote the ending narration to a stray `narration.md` at the repo root (a wrong relative path), then moved it into `pilot/` and deleted the stray file. Nothing else landed outside `pilot/`.
- **Stale diaries (Chapter 2).** Diaries were requested before the last news of Year 4 reached the players, so three described an outdated board. From Chapter 3 on, a closing catch-up went out first.
- **A wrong objective at the table (Year 5).** The Storyteller, and the Director's own summary, said Paddy as Silk needed a Customs House again after Rob raided his. Silk never needs one. It was corrected at the table by a note to all, plus fixes to the ledger and the narration. The board cards were right throughout; the error came from hand-written text.
- **Rulings crossing in flight.** Manish's Silk-throne ruling reached the Chapter 2 Storyteller only after it had finished, and the Storyteller and the Director then wrote it into the ledger at the same time, giving two P15s. Merged as P14. Cross-session messages queue until the receiving session's turn ends, so a ruling sent mid-chapter can land late.
- **Hand-written facts.** One hand-computed distance (Chapter 1), one invented bid line (Chapter 1, removed), and a grain figure in a note (Chapter 2). All caught. Board cards (from Chapter 2) removed most of this class of error.
- **Voices held across seat changes.** Paddy stayed earnest on three different seats; Rob stayed gleeful as Emperor; Reina stayed the manager as Warlord. No player slipped into the old seat's persona. Fresh agents each chapter, briefed from the ledger entry and their own diary, kept continuity well: no player contradicted their earlier promises. After Chapter 1's Jar and Customs House, where Paddy and Graham each offered to stand aside and then bid anyway, every public promise was kept, often at the cost of the game (Paddy and the Bowl).
- **Whispers.** Rare, as intended.
- **Safeguards.** None tripped. No agent was asked for its reasoning, and no transcript was read.

## Engine and tool gaps

**Fixed during the game (main session, `engine.py`):**
- `build()` took the works money from the payers and paid it to nobody. It now pays the Harvest Pile (commit 700da83). Only the pile moved: 2041 → 2161 at the end of Year 4.
- `swap()` now allows `swap(5, 1)` at a table with no upper class (P14).
- `swap()` now hands the Warlord's soldiers to the new Warlord and clears `warlord_got` (P19, commit 3f70877).

**Still open:**
- **Unsold stock can't be sold back** to cover a payment (P20). Should it count as realia for "sell before you sink"?
- **The population caps.** With the Wall unbuildable and two doublings left, ×3 is already terminal at five players. Worth checking the caps and the doubling count against the peasant table.
- **The Emperor's Share card** isn't applied by the engine; it was scripted as an act.
- **The Warlord's no-raid disaster:** the engine refuses the raid. The march menu now marks those squares `BARRED`.
- **From the trial year,** still true: no snapshot restore; `export()` scores a partial game as if it had ended; `build.py` can't run a script outside `playthrough-sim/`.

**Tools (`pilot/`):**
- `briefs.py` gained the board card, the ledger entry and the diary at launch.
- It now takes roles, the table and auction tie order from the engine's current seats, not the booklets. Before that fix, the Year 3 seat swap would have broken the Year 4 ties.
- The Bash tool fails on backticks in heredocs and on non-ASCII text; every Storyteller hit it and used the file tool instead.

**Harness:**
- A session can't start another session on a turn that a cross-session message began, so every chapter after the first needed Manish's click.
- `clear_session` was refused by the auto-mode classifier, so Storyteller sessions weren't reused.
- Detaching each Storyteller and having it message the Director only at year ends kept the Director quiet between years.
