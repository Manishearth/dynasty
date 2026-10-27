# Trial year: log

The Year 1 part of `pilot/log.md`, archived with the trial. Paths below are relative to this folder (`trial-year1/`).

## Year 1 of a five-player game (`log/year1/`)

The peasant game's table, from a fresh setup: Reina (Emperor, 1), Silke (5), Paddy (6), Graham (7), Rob (Warlord, 8). Each seat is one `dynasty-player` agent, launched once and continued with SendMessage (`agents.md` has the ids). Chance: `seed.md`. The script: `game_pilot.py`, run with `run.py`. State snapshots: `state/setup.json`, `state/year1.json`. Report: `REPORT-year1.md`.

Token figures are the `subagent_tokens` each completion notice reported.

| # | Seat(s) | Step | Files | Tokens |
|---|---|---|---|---|
| 001 | Rob | Setup: place the army, tax stance (launch) | `001-rob-prompt.md`, `001-rob-reply.md` | 4,865 |
| 002 | Reina | Setup appointments; Year 1 tax, build, soldiers (launch) | `002-reina-prompt.md`, `002-reina-reply.md` | 5,695 |
| 003 | Silke | Choose her lot: the Dragon Jar, min 8 (launch) | `003-silke-prompt.md`, `003-silke-reply.md` | 5,245 |
| 004 | Paddy | Choose his lot: the Wooden Bowl, min 10 (launch) | `004-paddy-prompt.md`, `004-paddy-reply.md` | 5,402 |
| 005 | Graham | Choose his lot: a Scroll, min 4; Vase held back (launch) | `005-graham-prompt.md`, `005-graham-reply.md` | 5,415 |
| 006 | Paddy, Graham, Rob | Lot 1, Jar: first bids 14, 16, 12 | `006-*-prompt.md`, `006-replies.md` | 6,379 + 6,431 + 6,100 |
| 007 | Paddy, Rob | Jar: Paddy 19, Rob passes | `007-replies.md` | 6,998 + 6,739 |
| 008 | Graham | Jar: 24 | `008-graham-reply.md` | 7,267 |
| 009 | Paddy | Jar: 27 | `009-paddy-reply.md` | 7,663 |
| 010 | Graham | Jar: passes; Paddy wins at 27 | `010-graham-reply.md` | 8,003 |
| 011 | Silke, Graham, Rob | Lot 2, Bowl: first bids 18, 20, 12 | `011-prompts.md`, `011-replies.md` | 6,484 + 8,762 + 7,663 |
| 012 | Silke, Rob | Bowl: Silke 25, Rob passes | `012-replies.md` | 7,167 + 8,059 |
| 013 | Graham | Bowl: passes; Silke wins at 25 | `013-graham-reply.md` | 9,795 |
| 014 | Paddy, Silke, Rob | Lot 3, Scroll: first bids 6, 5, 8 | `014-prompts.md`, `014-replies.md` | 8,722 + 7,954 + 8,797 |
| 015 | Silke, Paddy | Scroll: 11 and 10 | `015-replies.md` | 8,596 + 9,339 |
| 016 | Paddy, Rob | Scroll: both pass; Silke wins at 11 | `016-replies.md` | 9,896 + 9,346 |
| 017 | Rob | March W1 → P19, W2 → R24; hire W3 on T16 | `017-rob-prompt.md`, `017-rob-reply.md` | 10,841 |
| 018 | Paddy, Silke, Graham, Reina | End of year: soldiers, salaries, offers | `018-prompts.md`, `018-replies.md` | 10,877 + 9,602 + 11,033 + 7,140 |
| 019 | Paddy | Declines Reina's loan of 20 | `019-paddy-reply.md` | 11,951 |

32 agent turns, 254,226 tokens reported in all.

## Before Year 2 (`log/year2/`, not started)

Year 2 prompts are written by `briefs.py` (see `STORYTELLER.md`), which keeps the table talk in `talk.jsonl` and each player's place in it in `seen.json`. Filed so far: a Storyteller's note to Reina (Rob's nearest soldier is 6 squares from Province 1, not 8), which opens her first Year 2 prompt. Tool check for the player agents: `agents.md`.
