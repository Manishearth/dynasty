# Year 10, first take (set aside)

The first time Year 10 was played (Chapter 5, log 119–132), played through to its salaries, the closing catch-up and the Years 9–10 diaries. The Director set it aside, with Manish's standing authorisation for rewinds in this game. The year is to be replayed from the end of Year 9 by another Storyteller with fresh agents.

**What happened:** Heaven Has Favourites: a good harvest on the coast (Province 5), a bad one in Provinces 1, 6 and 7, and the crown −30 again. Before the harvest Reina lent the crown 29, to be repaid 31 out of the year's tax. Graham named 40% in advance, collected 56, and repaid Reina 31 and Silke the 15 he owed her from Year 9. No work was built: Graham offered a Grand Canal section at 39 from the province and 1 from the crown, and Reina and Paddy declined. Three squares were bought at 0.5 a square from the crown: R27 for Paddy, U15 and V14 for Silke, bringing the board to 21. Province 7's Land Deed Scroll went unsold, since Silke's minimum was 75 and Reina's limit 70. Year 10 ended with the crown at 0 and owing nobody, Reina 90, Silke 59.5 and Paddy 14.5, with nobody in debt. That left about 150 grain held idle rather than put into land.

**Why it was set aside:** the cards say the next population card may come, and at ×6 the crown would fall about 160 into debt even on a good harvest. A crown in debt can't pay its share of any square, so land would shut for the whole table, and the table had ended Year 10 holding its grain instead of putting it into land. Nothing was played wrong. The replay gets new notes and a tip.

**What's here** (everything moved out of the live record; nothing was deleted):
- `game-year10.py`: the script from the Year 10 header on.
- `log-year10/`: every prompt and reply, 119–132 (the diaries are 129–132).
- `bids-y10.json`: the Year 10 bids.
- `talk-year10.jsonl`: table talk records 193 on.
- `seen-year10-take.json`: `seen.json` as the take left it (everyone at 212, after `seen all`).
- `ledger-year10-take.md`: the whole ledger as the take left it.
- `diaries-years9-10.md`: the four `## Years 9–10` diary entries.
- `narration-year10.md`, `log-year10.md`: the Year 10 lines of `narration.md` and `log.md` (rows 119–132 and the Chapter 5 usage line), and the chapter title the take gave, "A Price Where It Hurts".
- `state-year10.json`: the Year 10 snapshot.
- No Year 10 rows were ever added to `agent-ids.md`; the Chapter 5 agents were launched in Year 9 and stay listed there.

The live record was restored to the end of Year 9. `game.py` stops after Year 9's salaries and runs to the same state as `state/year9.json` (Reina 52, Silke 50.5, Paddy 10, Graham 1.5; pile 2386). `talk.jsonl` ends at record 192. `seen.json` is back at each player's last Year 9 prompt: Graham 179, Paddy 182, Silke and Reina 188. The ledger is back at its end-of-Year-9 entries, keeping the Year 9 tip and the Year 9 rulings. The Chapter 5 marker in `game.py` and `narration.md` reads "TBD" again.
