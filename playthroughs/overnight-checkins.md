# Overnight check-ins

## 2026-10-28 02:53

- **The peasant's game:** progressing. Year 9 finished, Chapter 6's Storyteller is running.
- **Highway Rob-bery:** progressing. Year 8 finished, Chapter 5's Storyteller is running.
- **All's Quiet on the Western Front:** progressing. Year 3 finished, Chapter 2's Storyteller is running.
- **The Dark Ages:** no Director yet.
- **Blocked:** nothing.
- **Usage:** 5-hour window 18% (resets 06:10), weekly 20%.
- **Page:** rebuilt, uncommitted. The peasant's game shows through Year 9, Rob-bery through Year 8, Western Front through Year 3. 1,474 entries.

## 2026-10-28, a decision for Manish: the peasant's game

The peasant's game is paused after Year 10, waiting on Manish. Nothing is broken.

- **Where it stands:** Years 6 and 10 have each been replayed once. Nobody is in debt, Reina has the throne back, and 200 of the 520 works are built.
- **What's coming:** Year 11 brings the third doubling (x6). Province 1 then eats 360 a year with 4 squares of land, so the crown falls about 145 into debt even on a good harvest, and a crown in debt shuts land for everyone.
- **What the replays showed:** the agents still keep their grain for the throne race, not for the crown's land.
- **Options:**
  - (a) The Director's recommendation: an agreed stop after Year 12 (Note 19), announced when Chapter 6 opens.
  - (b) Play on, and let it collapse if it does.
  - (c) More rewinds.
- **Main session's view:** (b). The scenario calls this a design check and says "if the table collapses anyway, let it: that's the answer", and an early stop would hide the result.
- **Answer it** in the Director's session or here. Chapter 6 waits until then.

## 2026-10-28, Highway Rob-bery finished

- **Result:** survival in Year 12, with Rob, the Warlord, on the throne. Clark called a revolt on Paddy's debt. Rob held the only soldiers on the board and was acclaimed Emperor, then built the last Reservoir.
- **Verdicts:** Rob and Paddy won, Clark held, and Rich, Silke and Reina lost. Reina ends as the Warlord.
- **The page:** rebuilt with the game finished ("Six players · twelve years · the Warlord on the throne"). The peasant's game shows through Year 10 (paused, decision above) and Western Front through Year 6. 1,793 entries, uncommitted.
- **For Manish to review** (REPORT.md, "Rulings made during the game"): the revolt stood even though Reina paid off the debt in the same round. The other reading puts Reina on the throne, and Year 12 can be replayed from state/year11.json.
- **Tool bugs left for the morning** (briefs.py, which Western Front is still using):
  - the I Ching menu says an appointed reader is "owed" a salary;
  - the endgame note says "can end next year" a year early once that year's project is built;
  - the free menu offers land under Chaos.
- **Fixed overnight:** DIRECTOR.md now says to file a public tip without --to.

## 2026-10-28, a decision for Manish: Western Front and an empty Harvest Pile

**The question:** what happens when the Harvest Pile can't pay a harvest?
- **When it arose:** after Year 9 the pile was at 477, and Year 10 (x6, a good harvest, plus the land) could pay out about 720.
- **What the rules say:** RULINGS.md treats the pile as finite (2,500) and has no rule for it running dry. The Dark Ages came close too.

**The provisional reading, so play continues:** every harvest is paid in full, and the pile goes below zero as its own debt, repaid by whatever flows into it. No player's payout changes. It's logged in western-front/ledger.md. If Manish rules otherwise, Year 10 can be replayed from state/year9.json.

**The alternatives:**
- pay in seat order until the pile is empty;
- pay pro rata;
- add bags, which is the same as the reading.

**Main session's view:** keep the reading, and treat the pile as unlimited, the way most games treat the bank. Bags running out is a limit of the box, not a rule, and the pile already acts as the game's sink.

**The arc happened:** Graham climbed from Wheat Peasant to Scholar to Emperor by Year 6.

## 2026-10-28 04:53

- **The peasant's game:** blocked on Manish (stop after Year 12, or play on). Year 10 finished. Expected; nothing to do overnight.
- **Highway Rob-bery:** finished.
- **All's Quiet on the Western Front:** progressing. Year 9 finished, and the next chapter is running on the "spare 1" Storyteller session. Year 10 is playing under the provisional pile-debt reading.
- **The Dark Ages:** no Director.
- **Usage:** 5-hour window 32% (resets 06:10), weekly 24%.
- **Page:** rebuilt, uncommitted. The peasant's game shows through Year 10, Western Front through Year 9, and Highway Rob-bery as finished.


## 06:53

- **Western Front: finished** in Year 13, survival. Rich (drew Gentry) ended on the throne; Graham, Rich and Silke won. REPORT.md and README are written. The Director's end message didn't go out because its message cap was hit, so its report is in the status file and REPORT.md. Years 10-13 rest on the provisional Harvest Pile reading (the pile ended at -4,836.5); another ruling means replaying from year9.json. Tool notes: briefs.py's endgame note was wrong twice (the Pagoda needs a year to itself), and two player agents made tool calls.
- **Peasant's game:** still waiting on Manish at Year 10. The Director has been idle since about 03:02.
- **Highway Rob-bery:** finished (Year 12).
- **Dark Ages:** no Director.
- **Usage:** 0% of the 5-hour window (it resets at 11:10), 25% weekly.
- **Page:** Western Front dropped from IN_PROGRESS and IN_PROGRESS_TITLE; the peasant's game stays at 10. Rebuilt: 7 games, 2,114 entries. Uncommitted.

## 08:53

- No change since 06:53; no session has been active since about 06:15.
- **Peasant's game:** still waiting on Manish at Year 10.
- **Highway Rob-bery** (Year 12) and **Western Front** (Year 13): finished.
- **Dark Ages:** no Director.
- **Usage:** 1% of the 5-hour window, 25% weekly.
- **Page:** already current (7 games, 2,114 entries), so not rebuilt. Uncommitted.

## 10:10 (after Western Front's message)

- **Harvest Pile:** Manish said no ruling is needed, so the pile never runs out and Western Front stands as played. Changes:
  - RULINGS.md, design-intent.md and rules-model.md now say the pile pays in full, even below zero.
  - engine.py swap() now always pays the displaced player's full 60.
  - Western Front's hand-made 60 to Noah (Year 12) no longer moves grain; its text loses "provisional reading".
  - Every finished game re-runs to the same grain, pile and entry count.
- **Peasant's game:** rewound to the end of Year 6 (old Years 7-10 are in outtakes/). The Chapter 7 Storyteller is replaying Years 7-8. IN_PROGRESS is now 6.
- **Page:** rebuilt, 7 games, 1,995 entries. Uncommitted.

## 10:53

- **Peasant's game: progressing.** The first take of Years 7-10 is restored as the live record (the Years 7-8 replay is in outtakes/years7-8-replay/). The Chapter 6 Storyteller is running a closing scene before Year 11: the table may agree to stop and score. Last finished year: 10.
- **Dark Ages: blocked on Manish.** The deck (seed 350), actor's notes and setup are done. Its seven Storytellers aren't parked yet, because the app won't let a session start sessions on a turn begun by another session's message. It needs Manish to type a go-ahead in the Director's session.
- **Highway Rob-bery** and **Western Front:** finished.
- **Usage:** 5% of the 5-hour window (it resets at 11:10), 26% weekly.
- **Page:** the peasant's game is back to Year 10. Rebuilt: 7 games, 2,123 entries. Uncommitted.

## 12:53

- **Peasant's game: progressing.** Year 11 is finished; the closing vote didn't end the game. The Chapter 9 Storyteller is playing Year 12, with a third vote on stopping after its salaries. If anyone still says no, it stops before Year 13 for Manish. Last finished year: 11.
- **Dark Ages: progressing.** Manish's go-ahead got it moving. Chapters 1-2 are done (Years 1-4); Storyteller 3 is playing Chapter 3 (Years 5-6), with a revolt looking close. Last finished year: 4.
- **Highway Rob-bery** and **Western Front:** finished.
- **Usage:** 6% of the 5-hour window (resets 16:20), 28% weekly.
- **Page:** peasant's game through Year 11, the Dark Ages through Year 4 (subtitle now "in progress"). Rebuilt: 7 games, 2,275 entries. Uncommitted.

## 13:05 (peasant's game finished)

- **Peasant's game: finished.** An agreed stop after Year 12 (Note 19): everyone in the seat they drew, Reina winning by keeping the throne. Dropped from IN_PROGRESS; the page shows it in full (313 entries).
- **Page:** rebuilt: 7 games, 2,306 entries. Uncommitted.
- **For Manish:** the Director's open rules question (should a mid-game agreed stop be allowed, and can one player block it?) and three briefs.py notes in peasant-game-status.md.

## 14:53

- **Dark Ages: finishing.** All twelve years are played (state/year12.json) and game.py has its ending; the Director is writing REPORT.md and hasn't declared it done yet. Page shows it through Year 12, still marked in progress.
- **Peasant thrive: progressing.** Manish chose a seed and play began; Chapter 2 (Years 3-4) is running, with the later chapters' Storytellers parked. Last finished year: 3. Added to the page (GAMES, last) through Year 3.
- **Unlucky peasants rematch** (peasant-draw), **Highway Rob-bery**, **Western Front:** finished.
- **Usage:** 18% of the 5-hour window (resets 16:20), 31% weekly. Nothing blocked.
- **Page** (now playthrough.html): rebuilt, 8 games, 2,625 entries. Uncommitted.

## 15:05 (the Dark Ages finished)

- **Dark Ages: finished.** An agreed stop after Year 12 with no revolt ever called: Clark, Silke and Paddy won, Rob held, Reina and Rich lost. Dropped from IN_PROGRESS and IN_PROGRESS_TITLE; the page shows it in full, subtitled "no revolt, the Official on the throne".
- **Page:** rebuilt, 8 games, 2,625 entries; Peasant thrive is the only live game (through Year 3). Uncommitted.
- **For later:** the Director's tool gaps in dark-ages/REPORT.md ("Engine and tool gaps").

## 15:40 (Peasant thrive finished)

- **Peasant thrive: finished.** Survival in Year 9 on seed 8535: all 520 in works built, nobody ever in debt, no rewinds. Paddy (drew Rice) won on the throne; Graham held; Silke and Reina lost. Dropped from IN_PROGRESS; the page shows it in full.
- **Page:** rebuilt, 8 games, 2,756 entries. No game is in progress. Uncommitted.
- **For Manish:** the report's possible ruling on the game ending when the last work is built, before that year's auctions.
