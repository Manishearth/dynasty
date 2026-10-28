# Years 7–8, replayed (set aside)

The replay of Years 7–8: Chapter 4, "On the Slate" (log 073–101), played from the end of Year 6 by the parked Storyteller after the first take of Years 7–10 was set aside. Played through to the Years 7–8 diaries. Manish then decided that the first take is the live record after all, and this replay was set aside in its place.

**What happened:**
- **Seats: no changes.** Graham bought Paddy's Dragon Jar before the harvest (12, and 6 more asked after it), completed the Wheat set, and stayed the Wheat Peasant. Silke stayed Emperor, Reina the Silk Peasant and Paddy the Rice Peasant.
- **Land, 13 → 16 squares,** all in Year 8. Year 7's crown was in debt after the harvest, so no land was bought that year.
- **Works: none.** The Great Wall (160) and the Grand Canal (160) are still owed.
- **End of Year 8:** Silke (Emperor) 0, with the crown owing Graham 30 (Year 7's loan of 25 back and Year 8's deferred 5 for the I Ching); Reina −30; Paddy 8; Graham 22.

**Why it was set aside:** heavier steering left the land count where it was: 16 squares at the end of Year 8 in both takes. The first take is the less steered and livelier record. Nothing was played wrong.

**Slips, as the Chapter 7 Storyteller logged them:** Silke's launch prompt dropped a sentence of her character line; 085's board card was trimmed by hand; 080 was regenerated once before it was sent.

**What's here** (everything moved out of the live record; nothing was deleted):
- `game-years7-8.py`: the script from the Chapter 4 marker on.
- `log-year7/`, `log-year8/`: every prompt and reply, 073–101 (the diaries are 098–101).
- `bids-y7.json`, `bids-y8.json`: the bids for each year.
- `state-year7.json`, `state-year8.json`: the snapshots.
- `talk-years7-8.jsonl`: table talk records 104 on (50 records).
- `seen-years7-8-replay.json`: `seen.json` as the replay left it (everyone at 152, after `seen all`).
- `ledger-years7-8-replay.md`: the whole ledger as the replay left it, its Year 7 tip included.
- `diaries-years7-8.md`: each player's `## Years 7–8` entry.
- `narration-years7-8.md`, `log-years7-8.md`: the Chapter 4 lines of `narration.md` and `log.md` (rows 073–101 and the usage line).
- `agent-ids-years7-8.md`: the "Chapter 4, replayed" section of `agent-ids.md`.

The live record is the first take of Years 7–10 again, restored from `../years7-10-first-take/`: `game.py` runs clean to 237 entries, round 10, the same state as `state/year10.json` (Reina, Emperor, 15.5; Graham 60; Silke 73.5; Paddy 15; pile 2336; 22 squares). Its ledger is the first take's, with the replay's rulings that are still true of the rules carried over and marked; the replay's tip stays out.
