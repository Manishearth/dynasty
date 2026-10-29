# Player agents: the Dark Ages

Each seat is one `dynasty-player` agent (`.claude/agents/dynasty-player.md`), launched fresh at the start of each chapter (`briefs.py prompt ... launch`, which carries the ledger entry and the diary) and continued with SendMessage for the rest of that chapter. An agent can be resumed by id only from the session that launched it.

## Sessions

- **Director:** `local_7b00875e-66cd-4e57-815e-ea787c8f35b1`
- **Storytellers**, parked before Chapter 1 (top-level, in the "playthrough-dark" sidebar section), one per two-year chapter:

| Session | Id | Chapter |
|---|---|---|
| Dark Ages Storyteller 1 | `local_24943e22-4ded-4437-99f3-8260b93c2ff5` | 1 (Setup to Year 2) |
| Dark Ages Storyteller 2 | `local_36618063-ccb2-4482-8911-b7319f0d1b70` | 2 (Years 3–4) |
| Dark Ages Storyteller 3 | `local_5f365bc1-4904-4108-8d08-1f970b67a3ee` | 3 (Years 5–6) |
| Dark Ages Storyteller 4 | `local_84f2baca-dfd1-436b-922e-fe0cd307abb5` | 4 (Years 7–8) |
| Dark Ages Storyteller 5 | `local_b3a12e75-928c-44f8-8ebd-57678a4c36c2` | 5 (Years 9–10) |
| Dark Ages Storyteller 6 | `local_7a3c57c5-08aa-4c70-af3f-5fefe4457f6a` | 6 (Years 11–12) |
| Dark Ages Storyteller 7 | `local_c517a769-a146-46c8-aad1-e0dbbb4da6c2` | 7 (Years 13–14) |

More Storytellers will be started if the game runs past Year 14.

## Chapter 1 (Setup to Year 2)

Launched by Dark Ages Storyteller 1 (`local_24943e22-4ded-4437-99f3-8260b93c2ff5`).

| Seat | Player | Agent id |
|---|---|---|
| 8 Warlord | Rob | `a1d363b50e0394535` |
| 1 Emperor | Reina | `ad8b7ef6e73cc8dd9` |
| 3 Gentry | Rich | `a77b8321549d36d33` |
| 2 Official | Clark | `a75fb1bb50193e8a5` |
| 5 Silk Peasant | Silke | `a14395f88571bef31` |
| 6 Rice Peasant | Paddy | `afdfa49bcd710b920` |

## Chapter 2 (Years 3-4)

Launched by Dark Ages Storyteller 2 (`local_36618063-ccb2-4482-8911-b7319f0d1b70`).

| Seat | Player | Agent id |
|---|---|---|
| 1 Emperor | Reina | `a5d8da0265b4ba478` |
| 3 Gentry | Rich | `a79cf11fd23e803d8` |
| 2 Official | Clark | `a96be669724d14f86` |
| 5 Silk Peasant | Silke | `a163e7d96c94b4b14` |
| 6 Rice Peasant | Paddy | `acb3c4445f415fd57` |
| 8 Warlord | Rob | `ab52be4aea115e31a` |

## Chapter 3 (Years 5-6)

Launched by Dark Ages Storyteller 3 (this chapter's session, started by the Director).

| Seat | Player | Agent id |
|---|---|---|
| 5 Silk Peasant | Silke | `a627d6da42915252b` |
| 3 Gentry | Reina | `aef1f9019038aee70` |
| 1 Emperor | Clark | `ab4ac258d04ec5790` |
| 2 Official | Rich | `aaf98779d92deb198` |
| 6 Rice Peasant | Paddy | `aba52680ec808de5c` |
| 8 Warlord | Rob | `a14220f0d9dcfda3b` |
