# Year 13, first take (set aside)

The first time Year 13 was played (Chapter 7, "Every Square, in Full", log 244–276). Manish set it aside after the chapter, and the year is being replayed from the end of Year 12.

**Why:** with one work left (the Province 2 Irrigation System, 30), the game would end the moment it was built. The table spent 520 on new land anyway, the Emperor having promised to pay "every new square, in full". Land bought in the last year pays nothing back. The crown went from 474 to 4, nothing was built, and Reina ended the year 22 in debt. The replay gives every player a plain note that late land doesn't pay (see `handoff/chapter-7.md`).

**What's here** (everything moved out of the live record; nothing was deleted):
- `game-year13.py`: the script from the Chapter 7 marker on.
- `log-year13/`: every prompt and reply.
- `bids-y13.json`, `year13.json` (the end-of-year snapshot), `talk-year13.jsonl` (table talk records 361 on), `seen-end-of-year13.json`.
- `ledger-end-of-year13.md`: the whole ledger as Chapter 7 left it.
- `narration-chapter7.md`, `log-chapter7.md`, `agent-ids-chapter7.md`, `diaries-year13.md`: the Year 13 parts of those files.

The live record was restored to the end of Year 12. `game.py` runs to the same state as `state/year12.json`, and each ledger entry is the one each player was launched with in Year 13. The ruling made during this take, that unsold stock is sold only at auction, stands (RULINGS.md).
