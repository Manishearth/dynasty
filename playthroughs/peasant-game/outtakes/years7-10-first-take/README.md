# Years 7–10, first take (set aside)

The first time Years 7–10 were played: Chapter 4 (Years 7–8, log 073–104) and Chapter 5 (Years 9–10, log 105–135, with Year 10 itself replayed once). Played through to the Years 9–10 diaries. Manish asked for a rewind to the end of Year 6, under his standing direction that this game should not end in collapse, and the Director set all four years aside so they can be replayed with new notes and tips.

**What happened:**
- **Seats.** In Year 7 Graham bought Paddy's Dragon Jar for 10 before the harvest, completed the Wheat set, replaced Reina as the Silk Peasant, then took the throne from Silke at the auctions with a Silk set. Reina went to the wheat (Province 7) and Silke to the silk (Province 5). In Year 8 Reina completed the Wheat set and took the Silk seat back, sending Silke to the wheat. In Year 10 Reina completed the Silk set and took the throne back, sending Graham to the silk. Paddy stayed the Rice Peasant throughout.
- **Four 60 draws** from the Harvest Pile, one for each displaced player: Reina (Year 7, 079), Silke (Year 7, 085), Silke (Year 8, 099), Graham (Year 10, 130).
- **Land, 13 → 22 squares:** K25, K26, Q26 (Year 8); Q27, U14 (Year 9); N28, R27, U15, U16 (Year 10). The crown's share fell from 5 a square in Year 8 to 1 a square in Years 9 and 10, and Province 1 bought none.
- **Works: none.** The Great Wall (160) and the Grand Canal (160) are still owed. A shared Province 5 canal section was offered in Years 8, 9 and 10 and declined each time.
- **Three bad harvests out of four** (Years 7, 9 and, outside the coast, 10). The crown was in debt after Year 7's harvest and was kept out of it in Years 9 and 10 by pre-harvest loans (Silke 13, Reina 29), each repaid in full from the next tax.
- **End of Year 10:** Reina (Emperor) 15.5, Silke 73.5, Paddy 15, Graham 60; pile 2336; 22 squares; nobody in debt.

**Why it was set aside:** the crown ended Year 10 with 15.5 and 320 still owed. At Year 11's ×6 it would fall about 145 into debt even on a good harvest, and a crown in debt can't pay its share of any square, which shuts land for the whole table. Replaying only Year 10 couldn't close that gap, and Year 6's replay had already put every grain into land, so Years 7–10 are where the room is. Nothing was played wrong.

**What's here** (everything moved out of the live record; nothing was deleted):
- `game-years7-10.py`: the script from the Chapter 4 marker on.
- `log-year7/` … `log-year10/`: every prompt and reply, 073–135 (the diaries are 101–104 and 132–135).
- `bids-y7.json` … `bids-y10.json`: the bids for each year.
- `state-year7.json` … `state-year10.json`: the snapshots.
- `talk-years7-10.jsonl`: table talk records 104 on (118 records).
- `seen-years7-10-take.json`: `seen.json` as the take left it (everyone at 221, after `seen all`).
- `ledger-years7-10-take.md`: the whole ledger as the take left it, Year 10 replayed included.
- `diaries-years7-10.md`: each player's `## Years 7–8` and `## Years 9–10` entries.
- `narration-years7-10.md`, `log-years7-10.md`: the Chapter 4 and 5 lines of `narration.md` and `log.md` (rows 073–135 and the two usage lines), with both chapter titles, "Wheat to Silk to the Throne" and "Priced to the Grain".
- `agent-ids-years7-10.md`: the "Chapter 4", "Chapter 5" and "Year 10, replayed" sections of `agent-ids.md`.
- `../year10-first-take/` stays where it is. It's the first take of a Year 10 that is now itself set aside: Year 10 was played twice, and both versions are out of the live record.

**The restored live record**, at the end of Year 6: `game.py` stops after Year 6's salaries and runs clean (118 entries, round 6) to exactly the state in `state/year6.json`: Silke (Emperor) 0, Reina 1, Paddy 4.5, Graham 32.5; pile 2462; 13 squares. `talk.jsonl` ends at record 103 (the end-of-Year-6 catch-up), and `seen.json` has all four players at 103, as `seen all` left it after the Years 5–6 diaries. The diaries end at `## Years 5–6`. The ledger is back at its end-of-Year-6 entries (the character entries as the Chapter 4 launch prompts carried them, the four **Playing it** lines as they were), with the tips through Year 6 replayed. Every ruling made in Years 7–10 that is still true of the rules is kept, marked with its year. `narration.md`, `log.md` and `agent-ids.md` end at Chapter 3.
