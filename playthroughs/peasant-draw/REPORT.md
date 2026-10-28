# Peasant draw: report

Played and recorded as "The peasant's game" in `playthroughs/peasant-game/`, so its logs, handoffs, ledger and steering log use that name and path.

An agent-played game of Dynasty at four seats: the Emperor and the three peasants, with no Warlord. It was a rematch of Peasant collapse (`peasant-collapse/`) on the same deck, seed `20261027` (`seed.md`). Each seat was a tool-less `dynasty-player` agent in character, every cast member in the province their name puns on. Storyteller sessions refereed through the engine, one per chapter or replay. A Director session wrote the actor's notes and the tips, checked every chapter, and steered towards survival.

**It ended at an agreed stop after Year 12,** with the crown 294.5 in debt and 200 of the 520 owed in public works built. The table voted three times to stop where it sat (Note 19). Silke said no until she had won back the seat she drew, and then all four agreed. Every player finished in the seat they drew. Reina won by keeping the throne; Silke, Paddy and Graham held.

**The finding:** on this deck, buying land isn't enough. The table bought land every year from the year it opened, the crown paid a share of every square, and loans before bad harvests kept everyone out of debt through Year 10. It still reached the second doubling in Year 11 with 22 squares, about 18 short. Province 1 is the hungriest and only the crown can buy its land. When the population doubled, the crown fell 145 into debt on a good harvest, and land shut for everyone. Two set-aside takes and a replay of Years 7–8 under heavier steering changed the land count by one or two squares at most (below). Peasant collapse fell because nobody bought land; this table bought it, and the deck still beat it.

The record:
- `game.py`: 313 entries, with `LAST_ROUND = 12` and `RESULT = export(...)`; run it with `run.py`.
- `log/year1–12/`: every prompt and reply.
- `ledger.md`, `diaries/` and `narration.md`.
- `state/setup.json` and `year1–12.json`, plus `year12-end.json`.
- `handoff/`: every brief. Never staged.
- `outtakes/`: three set-aside takes, each with a README.

## The story in brief

**Chapter 1, "You Already Had a Brush" (Years 1–2).** Reina taxed at 40% and built fast: the Summer Palace, then both Province 1 canal sections in one year. Paddy bought the only Dragon Jar for 17. Silke, who needed neither, bought a Brush and a Scroll anyway, and was two pieces from the throne by the end of Year 2.

**Chapter 2, "The Mandate Moves to the Coast" (Years 3–4).** Reina built the Province 7 Reservoir with Graham's 20. Silke won the Bowl for 13 and the Vase for 25, completed her set and took the throne in Year 3. Reina went to the coast with 60 from the Pile. Silke built the Winter Palace in the bad harvest of Year 4. Reina took the Vase from Paddy on a live raise to stop his set.

**Chapter 3, "Every Grain into the Ground" (Years 5–6).** Silke built the Marble Pagoda and ended Year 5 with a reserve of 180. Land opened in Year 6 with the first doubling (×3). The table bought 13 squares, and the crown paid for Province 1's four and a share of every other square, ending at 0. The year was played twice (below).

**Chapter 4, "Wheat to Silk to the Throne" (Years 7–8).** A bad harvest put the crown and Reina in debt. Graham bought Paddy's Jar, took Reina's Silk seat and her debt, then bought the Pile's Vase and Scroll and took the throne from Silke, all in Year 7. In Year 8 Reina completed a Wheat set and took the coast back. Four seat changes in two years drew 240 from the Pile. Graham offered a canal section and Silke refused to pay more than 10 of it: "every year that canal stays unbuilt is another year this game keeps going."

**Chapter 5, "Priced to the Grain" (Years 9–10).** Two more bad harvests. Each year someone lent the crown grain before the harvest, Silke 13 and then Reina 29, so nobody went into debt. Land reached 22 squares. Reina needed one Scroll, and Silke set its minimum at 53, exactly Reina's grain less the 20 a claim needs. Reina paid it and took back the throne she had lost seven years before. Year 10 was played twice (below).

**Chapter 6, "Two for the Bowl" (the vote, Years 11–12, and the end).** Before Year 11's card the table was asked whether to stop where it sat. Reina and Paddy said yes, and so did Graham after a correction of fact (he had misread the province he drew). Silke said no: "I sat down tonight as the Silk Peasant and I'm not standing up two provinces further south." The population doubled (×6) and the crown fell 136.5 into debt on a good harvest. Land shut, and nothing was built. Silke said no again, one Wooden Bowl short of a set. In Year 12 Paddy had to put the Bowl up. Silke took it for 2, went back to the Silk seat she drew carrying Graham's debt, and Graham went back to the wheat with 60. Asked a third time, all four agreed. Silke: "I said one more year, and then I'd be the one asking you to stop. I'm not asking, Reina, I'm agreeing."

## Verdicts

| Player | Drew | Ends | Result | Grain |
|---|---|---|---|---|
| Reina Osorio | Emperor (1) | Emperor (1) | won | −294.5 (the crown) |
| Silke Weber | Silk Peasant (5) | Silk Peasant (5) | held | 48.5 |
| Graham Garner | Wheat Peasant (7) | Wheat Peasant (7) | held | 60 |
| Paddy Doyle | Rice Peasant (6) | Rice Peasant (6) | held | 0 |

The throne went Reina → Silke (Year 3) → Graham (Year 7) → Reina (Year 10). Paddy, still owing Silke 23.5 by promise, never changed seats.

## Against the scenario

- **Target arc: the peasants survive the deck that broke the last table. Partly met.**
  - Everyone stayed out of debt through Year 10, and a peasant took the throne twice, both times from the Silk seat.
  - But only 200 of the 520 owed in works were built, nothing after Year 5. The game didn't survive the second doubling: it stopped by agreement while it still could.
  - Without the stop, Year 13 would have opened with the crown near −300 and two peasants with almost nothing left.
- **Land bought ahead. It worked as far as the grain allowed, and that wasn't far enough.**
  - Thirteen squares in the year land opened, the table's whole reserve.
  - Then about two a year, because two bad harvests in three years at ×3 leave the whole table only 20–60 grain of surplus a year.
  - Every board card showed each province's need at the next population card, and the agents read it out loud. Knowing didn't make the grain.
- **Imperial subsidy.** Every Emperor paid a share of every square, and Silke paid all of Province 1's in Year 6.
  - The trap is that Province 1's land is the crown's alone, and the crown's only income is tax on positive incomes, which dried up from Year 6.
  - A crown at 0 can't subsidise anyone. A crown in debt shuts land for the whole table.
  - This is the rule the deck leans on hardest.
- **Silk standing in for the upper class. Worth doing, every time.** Three climbs reached the throne from the Silk seat. Seat changes were also the table's best source of new grain: each displaced player drew 60 from the Pile.
- **Debt as a fear.** It kept the table out of debt for ten years. Lending before the harvest became a habit from Year 7, and no deal was broken. Once debt came, at ×6, nobody revolted.

## Steering

All logged in `seed.md`. Manish's direction before Chapter 1 was that **this game should not end in collapse**, so the Director steered much harder than the scenario's "steer lightly", with notes, tips and rewinds. The rules and the engine were never bent.
- **Actor's notes:** rewritten after every seat change, and each time a take was replayed. From Year 6 the Emperor's note had her leading the table out loud: land first, care at auction, loans before lean harvests. Manish suggested the direction come from the Emperor.
- **Tips:** one public tip to all four in each of Chapters 1, 3, 4 and 5, and second tips in the replays (Manish allowed them). Each tip only restated the rules or the board cards: the crown may pay any part of a square, debt bars land, a crown in debt shuts land for everyone, grain may be lent before the harvest, the 60 draw, and the next card's need.
- **Rewinds** (Manish's standing permission), each kept whole in `outtakes/`:
  - **Year 6, first take:** 9 squares, a canal section, the crown emptied before a bad harvest. Replayed for 13 squares.
  - **Year 10, first take:** 21 squares and about 150 grain held idle. Replayed for 22 squares and the throne back to Reina.
  - **Years 7–10 set aside, then restored.** After Year 10 Manish asked whether an Emperor urging the table into land could save it. The record went back to the end of Year 6, and Years 7–8 were replayed with Silke as a helpful Empress asking for every spare grain to go into land and the crown. The replay ended Year 8 with 16 squares, exactly what the first take had, with no seat changes and so none of the 60 draws. Manish then restored the first take as the live record, as the less steered and livelier one. The replay is in `outtakes/years7-8-replay/`.
- **The ending:** the Director proposed an agreed stop before the second doubling. Each vote opened with the same public tip on Note 19 and §18 scoring, and the players decided. Manish chose to play on after each refusal rather than rewind it.

## Rules and rulings

The full list is in the ledger's rulings. The ones that shaped the game:
- **The Grand Canal is one work** (Note 13). All its sections in Provinces 5 and 6 are one project, so two projects were left after Year 5, not three. The Director's early handoffs had it wrong, and it was corrected in Year 6.
- **A crown in debt can't pay a land share,** so land shuts for everyone. That's the RULINGS reading that every square needs some crown share, and it is the rule that decided the game.
- **A displaced player draws 60 from the Pile; the climber takes the seat's debt** (Year 7, Graham taking Reina's −25; Year 12, Silke taking Graham's −19.5).
- **An appointee's pay is the Emperor's choice** (N3). The crown in debt deferred salaries from Year 11.
- **A piece can't be held back two rounds running.** This is what forced the Bowl up in Year 12, and with it the end.
- **A table can agree to stop mid-game.** Note 19 says "agree before setup". The table here agreed after Year 12, on the RULINGS precedent for authored stopping points. Manish has since confirmed that a table may agree to stop partway through (RULINGS, authored stopping points).

## Tools

**Changed during the game, with the main session's OK:**
- `engine.py`: `swap()` refused a legal Silk-to-throne climb (line 614). The main session fixed it; Silke's Year 3 swap ran unchecked by hand until then.
- `briefs.py` `endgame_note`: the two-projects wording said a square "pays back once … at best", which is backwards, and it hid the break-even line. Reworded, and only this game's cards changed.

**Still open** (sent to the main session, not edited):
- The `iching` prompt tells an appointed reader "the Emperor owes you at least 5", but an appointee's pay is the Emperor's choice (N3).
- The `free` and `auctions` prompts carry the "New land is open" line even when the crown is in debt and land is shut. Silke tried to buy a square because of it in Year 11.
- In the Years 7–8 replay, Silke's launch prompt dropped a sentence of her long Playing it line. This may be a length cut in `briefs.py`.

## Usage

- **Storyteller context at chapter ends:** 287k, 295k, 258k (Year 6 replay), 425k, 330k (Year 10 replay), 392k (Year 11 and the second vote) and 357k (Year 12 and the third vote). The replay of Years 7–8 ended at 398k.
- **Each year at ×3 or more cost a Storyteller 125–150k.** Two-year chapters fit under the 450k stop line, but only just.
- **Ten Storyteller sessions in all:** five parked before play, a backup, three more Manish asked for, and one fresh one for Year 12.

## Continuity and drift

- **Voices held** through three rewinds and a restore. Reina managed and counted the crown's books. Silke was sharp and priced things "to the grain". Paddy was earnest, never changed seats, and "hated owing anybody anything" to the last half-grain. Graham counted, and twice took a seat only when the numbers suited him.
- **Corrections of fact,** each a public note: the one-project canal, Graham's misread province at the first vote, and the Bowl having to go up in Year 12. All were worded as the rule, never as advice.
