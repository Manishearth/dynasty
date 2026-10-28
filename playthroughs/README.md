# Playthroughs played by agents

One folder per game, each the complete record of a game played by agents: the script the page is built from (`game.py`), every prompt and reply (`log/`, indexed in `log.md`), the ledger, the diaries, the narration, the state snapshots and the chapter handoffs. The code and notes for playing a game are in `../playthrough-sim/agents/`. The games listed in `build_real.py` are built into `../playthroughs-real.html`, which will eventually replace `playthrough.html`.

| Folder | Game | On the page |
|---|---|---|
| `full-game/` | **"The full game"**: all eight provinces. Still being played, so the page shows the chapters checked so far. | yes, in progress |
| `short-game/` | **"The short game"**: the Emperor and the upper class, four players, stopped after eight rounds as agreed (Note 19). The throne changed hands twice. In the last round Rich, one piece short, bought Noah's Brush in a private trade and took it from Clark. See its `REPORT.md`. | once the page is rebuilt |
| `highway-robbery/` | **"Highway Rob-bery"**: six players with the Warlord, twelve years. Seven seat changes, four of them on the throne, then a revolt on a peasant's debt in the last year, and the Warlord, one name short of his objective, was acclaimed Emperor and built the last work himself. See its `REPORT.md`. | once the page is rebuilt |
| `western-front/` | **"All's Quiet on the Western Front"**: seven players, no Warlord, thirteen years, every work built. The throne changed hands nine times and every player sat on it; three peasants climbed through an upper-class seat to the throne. At x6 the harvests outgrew the engine's 2,500 cap on the Harvest Pile; play went on as if the bank never runs out, which the rules allow. Rich, the Gentry, ended on the throne. See its `REPORT.md`. | once the page is rebuilt |
| `peasant-collapse/` | **"Peasant collapse"**: the Emperor, three peasants and the Warlord, five players, eight years. Nobody bought new land, the population tripled, every player fell into debt, and the table gave up in Year 8: an economic collapse. See its `REPORT.md`. | yes |
| `trial-year1/` | A first trial year of the peasant table, played before the tools were fixed. Kept for reference. | no |
| `peasant-draw/` | **"Peasant draw"**: the rematch, on Peasant collapse's own deck, with the Emperor and three peasants, no Warlord. Four players, twelve years, an agreed stop. The table bought land every year from the year it opened and the throne changed hands three times, but no work was built after Year 5. At the second doubling (x6) in Year 11 the crown fell deep into debt. Steered hard for survival (Manish asked that it not collapse), with two years rewound and replayed and a set-aside replay of Years 7–8, all in `outtakes/`. The table voted three times on stopping where it sat; Silke refused until she had won back the seat she drew, and after Year 12 all four agreed. Reina won by keeping the throne. See its `REPORT.md`. | once the page is rebuilt |

### Up next

Seeded and waiting for a Director, in the suggested order. Each folder holds the setup (`game.py`), a recommended deck (`seed.md`), the arc to nudge towards and the levers for it (`scenario.md`), and empty ledger, log, narration and agent-id files. The Director starts from `../playthrough-sim/agents/DIRECTOR.md`.

| Folder | Table | The arc |
|---|---|---|
| `dark-ages/` | **"The Dark Ages"**. 6, with the Warlord | An early revolt, a stretch of Chaos, then a recovery |

Peasant collapse was played as `playthrough-sim/pilot/` and first filed as `peasant-failure/`, so its logs and handoffs still mention those paths. Likewise Peasant draw was played and first filed as "The peasant's game" in `peasant-game/`.
