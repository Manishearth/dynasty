# Replaying the playthroughs with 2 × 2 harvest squares

On 2026-11-18 Manish found that a harvest square in the original box covers 2 × 2 squares of the map, not one. Every playthrough so far bought land one square at a time. This note says where each game stands, and how to replay the parts that can't be fixed in place so the old rule can be dropped.

## What changes

The board has room for about **8** harvest squares on the strip below the Wall (Provinces 1–3), **27** in the sea (1, 4, 5, 6) and **47** on the Warlord's land (6, 7). Province 4 touches the sea only near K25, so one neighbour's square there can shut it out. Under the old rule the long games bought far more than that: Western Front 199 map squares, Dark Ages 126, Protection Money 93, Highway Rob-bery 81.

So in a long game land runs out. At ×6, breaking even in an average year takes nine harvest squares a province, and the sea can't hold nine each for four provinces. The works have to carry more of the load. That's a design consequence, not a bug, but none of the playthroughs has tested it yet.

## Where each game stands

`tools/replace_land.py` re-places a game's land as 2 × 2 harvest squares, keeping each one over the square originally bought where it can, and checks that the replay is unchanged apart from the land.

| Game | Years | Land | Status | To drop the old rule |
|---|---|---|---|---|
| Scripted: game2, game3, game4, game7 | 10 | 2–21 squares | **Re-placed**, play unchanged | Done |
| Scripted: game1 | 10 | 18 | **Re-placed**, play unchanged | Done |
| Scripted: game5 | 10 | none | Unaffected | Done |
| Short game | 8 | 12 | **Re-placed**, play unchanged | Done |
| Peasant draw | 12 | 22 | **Re-placed**, play unchanged | Done |
| Peasant collapse | 8 | none | Unaffected | Done |
| Scripted: game6 | 10 | 23, from Year 7 | Old rule | Rewrite Years 7–10 by hand |
| Full game | 13 | 34, all in Year 12 | Old rule | Replay Years 12–13 |
| Peasant thrive | 9 | 38, from Year 5 | Old rule | Replay Years 7–9 (Years 1–6 re-place cleanly) |
| Highway Rob-bery | 12 | 81, from Year 6 | Old rule | Replay Years 7–12 (Years 1–6 re-place cleanly) |
| Protection Money | 12 | 93, from Year 3 | Old rule | Replay Years 7–12 (Years 1–6 re-place cleanly) |
| All's Quiet on the Western Front | 13 | 199, from Year 4 | Old rule | Replay Years 7–13 (Years 1–6 re-place cleanly) |
| The Dark Ages | 14 | 126, from Year 6 | Old rule | Replay Years 10–14 (Years 1–9 re-place cleanly) |

"Old rule" games set `LAND_BLOCK = 1` at the top of their script and still build and display as they were played.

## Ways to replay

### 1. Restart from the first year that doesn't fit (recommended)

The same restart the Dark Ages used (see its `REPORT.md`), from a later year:

1. `python tools/replace_land.py playthroughs/<game>/game.py --until N --write` cuts the script at Year N, re-places the land bought before it, drops the `LAND_BLOCK = 1` line, and checks Years 1 to N−1 replay unchanged. Every earlier year, talk and result stands.
2. The Director starts a Storyteller from Year N, with the chapter handoff and the diaries written at the end of Year N−1. The deck is the game's own (`seed.md`), so the same cards come.
3. From Year N, `briefs.py` offers land as 2 × 2 harvest squares named by their top-left corner, and the players meet the shortage for real.

The table's history up to Year N stays exactly as it was, so the replay needs no new setup, and the narration and reports for those years still hold. The cost is roughly the replayed years' share of the prompts, from the game's `log/` counts:

| Game | Replay | Player prompts in those years originally |
|---|---|---|
| Full game | Years 12–13 | 49 |
| Peasant thrive | Years 7–9 | 31 |
| Highway Rob-bery | Years 7–12 | 107 |
| Protection Money | Years 7–12 | 95 |
| Western Front | Years 7–13 | 164 |
| The Dark Ages | Years 10–14 | 65 |

**Start with the full game and Peasant thrive.** Each is two or three years, and they're the cheapest way to see how a table copes when land runs short.

**For the land-rush games, the replay is the playtest.** Those four bought three to seven times the land the board can hold. Their endings, survival in three of them, rested on that land, so a replay may well end differently. That's worth knowing before the rulebook's advice on land ("buy as soon as you can") is left as it stands. A direction file (`direction.md`) can steer the story's shape if a particular ending matters, as the Dark Ages did.

### 2. Rewrite by hand (scripted games)

game6 is a scripted game, written start to finish by one agent. Nothing has to be replayed with players: Years 7–10 can be rewritten with the land re-placed and the incomes that follow from it.

### 3. Cut the record short (cheapest, loses the endings)

Stop a game at the last year whose land fits, and end it with a note that the record stops there because of the rule change. Nothing is replayed, but the land-rush games lose their last four to seven years, including how they ended. Not recommended except as a stopgap.

### 4. Keep them as old-rule games (current state)

They play and display as they were, with the note in their scripts. The page doesn't yet say so to a reader; if they stay, each game's blurb should get one line ("played with one-square harvest squares, before the 2 × 2 rule").

## The tool

```
python tools/replace_land.py <game.py> [--until N] [--write]
```

Without `--write` it only reports. It fails if the land can't all fit (then try an earlier `--until`) or if re-placing it would change play, for instance a Warlord soldier now stepping onto new land and raiding it. It also keeps new land off any square a piece of realia stands on at some point (the Warlord's raided pieces stand in the Warlord's desert). In every game checked so far, play didn't change.
