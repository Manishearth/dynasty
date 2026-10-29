# Player agents: the Dark Ages

Each seat is one `dynasty-player` agent (`.claude/agents/dynasty-player.md`), launched fresh at the start of each chapter (`briefs.py prompt ... launch`, which carries the ledger entry and the diary) and continued with SendMessage for the rest of that chapter. An agent can be resumed by id only from the session that launched it.

Restarted from the setup on 2026-10-28; attempt 1's sessions and agents are in `outtakes/attempt-1/agent-ids.md`. Then **rewound to the end of Year 1**: Years 2–5 are in `outtakes/year2-rewind/` and `outtakes/year5-rewind/`. The Chapter 2 and Year 5 tables below are those outtakes' agents. Storytellers 1–6 are archived. Launch prompts now also carry `direction.md`.

## Sessions

- **Director:** `local_7b00875e-66cd-4e57-815e-ea787c8f35b1`
- **Storytellers** (top-level, in the "playthrough-dark" sidebar section):

| Session | Id | Chapter |
|---|---|---|
| Dark Ages Storyteller 4 (archived) | `local_84f2baca-dfd1-436b-922e-fe0cd307abb5` | 1: Setup and Year 1 (kept); Year 2 (rewound) |
| Dark Ages Storyteller 5 (archived) | `local_b3a12e75-928c-44f8-8ebd-57678a4c36c2` | 2, Years 3–4 (rewound) |
| Dark Ages Storyteller 6 (archived) | `local_7a3c57c5-08aa-4c70-af3f-5fefe4457f6a` | Year 5 (rewound) |
| Dark Ages Storyteller 7 | `local_c517a769-a146-46c8-aad1-e0dbbb4da6c2` | 1, from Year 2, and 2 (Years 3–4) |
| Dark Ages Storyteller 8 | `local_4b3aa100-08e7-4ca9-be30-83a63964d9c7` | 3 (Years 5–6) |
| Dark Ages Storyteller 9 | `local_ae3306dd-050e-44e0-85c9-dd7759a62fe2` | 4 (Years 7–8) |
| Dark Ages Storyteller 10 | `local_03079c9a-d8cb-4007-b8f1-459428f27c39` | 5 (Years 9–10) |
| Dark Ages Storyteller 11 | `local_071a23fb-0c82-425a-ad16-2365a35c0984` | 6 (Years 11–12), parked |
| Dark Ages Storyteller 12 | `local_ccb4c1e2-a354-46bb-97b3-c27cfdb963b5` | 7 (Years 13–14), parked |

## Chapter 1 (Setup to Year 2)

Launched by Dark Ages Storyteller 4 (`local_84f2baca-dfd1-436b-922e-fe0cd307abb5`).

Setup and Year 1 up to the tax (all six replaced after the Year 1 rewind; see outtakes/year1-rewind/):

| Seat | Player | Agent id |
|---|---|---|
| 8 Warlord | Rob | `a880dd4f9499a22cc` |
| 1 Emperor | Reina | `a59207d5e75fe8a9f` |
| 3 Gentry | Rich | `a414ecbd354e9c87f` |
| 2 Official | Clark | `af0366e1dc40ce004` |
| 5 Silk Peasant | Silke | `a6980832732a22588` |
| 6 Rice Peasant | Paddy | `ae2566f492c51ad5a` |

After the Year 1 rewind (fresh agents):

| Seat | Player | Agent id |
|---|---|---|
| 2 Official | Clark | `a9c7912630203ee88` |
| 3 Gentry | Rich | `ad8f91b08ffa64231` |
| 5 Silk Peasant | Silke | `a62adb70a1b632b5e` |
| 6 Rice Peasant | Paddy | `a717f427b1ae93ec4` |
| 8 Warlord | Rob | `a8ea207ad1f06fb09` |
| 1 Emperor | Reina | `a008d285ea8ebf014` |

## Chapter 2 (Years 3–4)

Launched by Dark Ages Storyteller 5 (`local_b3a12e75-928c-44f8-8ebd-57678a4c36c2`).

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor | Reina | `aca5b87aaac11181b` |
| 3 Gentry | Rich | `a7bf2033bbbd726a7` |
| 2 Official | Clark | `a4c1ee91b5dfe6fa3` |
| 5 Silk Peasant | Silke | `a9f2726d251ba3401` |
| 6 Rice Peasant | Paddy | `a7604110efc42acac` |
| 8 Warlord | Rob | `ac847bec7b2be1e5a` |

## Chapter 3, Year 5 first run (rewound; see outtakes/year5-rewind/)

Launched by Dark Ages Storyteller 6 (`local_7a3c57c5-08aa-4c70-af3f-5fefe4457f6a`).

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor | Reina | `affb459062c9718e2` |
| 3 Gentry | Rich | `a57f04f4ce2e9c939` |
| 2 Official | Clark | `a0c298d1076cb788e` |
| 5 Silk Peasant | Silke | `a585671c51764107d` |
| 6 Rice Peasant | Paddy | `af3a5fee27f92f756` |
| 8 Warlord | Rob | `a066ce4d8e54ebf56` |

## Chapter 1, Year 2 onwards (live; Storyteller 7, local_c517a769-a146-46c8-aad1-e0dbbb4da6c2)

| Seat | Player | Agent id |
|---|---|---|

## Chapter 1, from Year 2 (the replay with the actor's brief)

Launched by Dark Ages Storyteller 7, fresh for every seat, each launch carrying `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor | Reina | `a45e4a4f4a051562e` |
| 3 Gentry | Rich | `a7ed9f376171812ed` |
| 2 Official | Clark | `a8986829c37394bac` |
| 5 Silk Peasant | Silke | `a7f9b86a49e83be4d` |
| 6 Rice Peasant | Paddy | `aab215db6fd4e4f45` |
| 8 Warlord | Rob | `a6abd5e6c5a33ce57` |

## Chapter 2 (Years 3-4)

Launched by Dark Ages Storyteller 7 (continuing), fresh for every seat, each launch carrying the Chapter 2 `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor (deposed) | Reina | `a290d5965cbd47baa` |
| 3 Gentry | Rich | `a190f016a2053e2e6` |
| 8 Warlord | Rob | `aaaf07ecbcdd49483` |
| 2 Official | Clark | `af492d4a4b2bae712` |
| 5 Silk Peasant | Silke | `a1cfd546038ad0bde` |
| 6 Rice Peasant | Paddy | `a95bcf30b8058c697` |

## Chapter 3 (Years 5-6)

Launched by Dark Ages Storyteller 8 (`local_4b3aa100-08e7-4ca9-be30-83a63964d9c7`), fresh for every seat, each launch carrying the Chapter 3 `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor (deposed) | Reina | `ac130af49b8103d6b` |
| 3 Gentry | Rich | `a818d7a0e08b51684` |
| Rob | `a9bb4ad9f73c1bd8c` |
| Clark | `a5e7576055d1885f7` |
| Silke | `abf952255550a9f6f` |
| Paddy | `a1f43c5ed70d131dd` |

## Chapter 4 (Years 7-8), the recovery

Launched fresh for every seat by the Chapter 4 Storyteller (started by the Director), each launch carrying the Chapter 4 `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor | Clark | `a7f0df6afb754068b` |
| 5 Silk Peasant | Silke | `afdf50bfb54b4cb17` |
| 3 Gentry | Rich | `ac2029a9e0fbe9c53` |
| 2 Official | Reina | `a79c5bf572c5eb38b` |
| 6 Rice Peasant | Paddy | `a3a1b8aecb4cc95d1` |
| 8 Warlord | Rob | `ac6970d6b6405d5dd` |

## Chapter 5 (Years 9-10), the heavy works

Launched fresh for every seat by the Chapter 5 Storyteller (started by the Director), each launch carrying the Chapter 5 `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 5 Silk Peasant | Silke | `a0c69a25891d43068` |
| 3 Gentry | Rich | `a10de38e61ab34839` |
| 1 Emperor | Clark | `a7556da7bb5232a68` |
| 2 Official | Reina | `adf19deeefc9ae3ba` |
| 6 Rice Peasant | Paddy | `a13e5f6ba2c5de61f` |
| 8 Warlord | Rob | `a06e98af1583e7c3d` |

## Chapter 6 (Years 11-12), the last works

Launched fresh for every seat by the Chapter 6 Storyteller (started by the Director), each launch carrying the Chapter 6-7 `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 5 Silk Peasant | Silke | `a99e65274c16f48b8` |
| 3 Gentry | Rich | `a46a7186b86c5a9e6` |
| 1 Emperor | Clark | `a7b96f401ee318863` |
| 2 Official | Reina | `a07c62864837de95c` |
| 6 Rice Peasant | Paddy | `a5840758d831d1014` |
| 8 Warlord | Rob | `a79277ab827619950` |

## Chapter 7 (Years 13-14), the last chapter

Launched fresh for every seat by the Chapter 7 Storyteller (started by the Director), each launch carrying the Chapter 6-7 `direction.md`.

| Seat | Player | Agent id |
|---|---|---|
| 5 Silk Peasant | Silke | `ab126649118eaded9` |
| 3 Gentry | Rich | `aa1c9e3217f593f5e` |
| 1 Emperor | Clark | `a7b19abf35f54062e` |
| 2 Official | Reina | `ad76b9203faacb250` |
| 6 Rice Peasant | Paddy | `a72d7e744aafd127d` |
| 8 Warlord | Rob | `a952a5eb7e1c3c209` |
