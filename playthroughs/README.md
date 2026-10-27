# Playthroughs played by agents

One folder per game, each the complete record of a game played by agents: the script the page is built from (`game.py`), every prompt and reply (`log/`, indexed in `log.md`), the ledger, the diaries, the narration, the state snapshots and the chapter handoffs. The code and notes for playing a game are in `../playthrough-sim/agents/`. The games listed in `build_real.py` are built into `../playthroughs-real.html`, which will eventually replace `playthrough.html`.

| Folder | Game | On the page |
|---|---|---|
| `full-game/` | **"The full game"**: all eight provinces. Still being played, so the page shows the chapters checked so far. | yes, in progress |
| `peasant-collapse/` | **"The peasant game"**: the Emperor, three peasants and the Warlord, five players, eight years. Nobody bought new land, the population tripled, every player fell into debt, and the table gave up in Year 8: an economic collapse. See its `REPORT.md`. | yes |
| `trial-year1/` | A first trial year of the peasant table, played before the tools were fixed. Kept for reference. | no |

The peasant game was played as `playthrough-sim/pilot/` and first filed as `peasant-failure/`, so its logs and handoffs still mention those paths.
