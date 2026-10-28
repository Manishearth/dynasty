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
