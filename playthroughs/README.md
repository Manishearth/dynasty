# Playthroughs played by agents

One folder per game, each the complete record of a game played by agents: the script the page is built from (`game.py`), every prompt and reply (`log/`, indexed in `log.md`), the ledger, the diaries, the narration, the state snapshots and the chapter handoffs. The code and notes for playing a game are in `../playthrough-sim/agents/`. The games listed in `build_real.py` are built into `../playthroughs-real.html`, which will eventually replace `playthrough.html`.

| Folder | Game | On the page |
|---|---|---|
| `full-game/` | **"The full game"**: all eight provinces. Still being played, so the page shows the chapters checked so far. | yes, in progress |
| `peasant-collapse/` | **"Peasant collapse"**: the Emperor, three peasants and the Warlord, five players, eight years. Nobody bought new land, the population tripled, every player fell into debt, and the table gave up in Year 8: an economic collapse. See its `REPORT.md`. | yes |
| `trial-year1/` | A first trial year of the peasant table, played before the tools were fixed. Kept for reference. | no |

### Up next

Seeded and waiting for a Director, in the suggested order. Each folder holds the setup (`game.py`), a recommended deck (`seed.md`), the arc to nudge towards and the levers for it (`scenario.md`), and empty ledger, log, narration and agent-id files. The Director starts from `../playthrough-sim/agents/DIRECTOR.md`.

| Folder | Table | The arc |
|---|---|---|
| `short-game/` | **"The short game"**. 4: the Emperor and the upper class, eight rounds | A race for the throne, decided in the last two rounds |
| `peasant-game/` | **"The peasant's game"**. 4: the Emperor and the peasants, no Warlord | Peasant collapse's own deck again, now with land bought ahead: a design check, steered lightly |
| `highway-robbery/` | **"Highway Rob-bery"**. 6, with the Warlord | The Warlord's campaign: a near miss or a late success |
| `western-front/` | **"All's Quiet on the Western Front"**. 7: no Warlord | A peasant climbs twice to the throne through grain politics alone |
| `dark-ages/` | **"The Dark Ages"**. 6, with the Warlord | An early revolt, a stretch of Chaos, then a recovery |

Peasant collapse was played as `playthrough-sim/pilot/` and first filed as `peasant-failure/`, so its logs and handoffs still mention those paths.
