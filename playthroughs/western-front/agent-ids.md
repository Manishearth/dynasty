# Player agents: All's Quiet on the Western Front

Each seat is one `dynasty-player` agent (`.claude/agents/dynasty-player.md`), launched fresh at the start of each chapter (`briefs.py prompt ... launch`, which carries the ledger entry and the diary) and continued with SendMessage for the rest of that chapter. An agent can be resumed by id only from the session that launched it.

## Storyteller sessions (parked before Chapter 1)

- Chapter 1 (Years 1–2): `local_401a281a-d944-4bef-8386-ab6cdb5714c9`
- Chapter 2 (Years 3–4): `local_af978a42-3ef5-4dbb-a8d9-062869d89199`
- Chapter 3 (Years 5–6): `local_bd5443c9-cf04-4f9c-abda-c9fbeaea8796`
- Chapter 4 (Years 7–8): `local_8647216a-deec-4f37-9ecf-c6a8e46a23d5`
- Chapter 5 (Years 9–10): `local_fe02a158-7d17-4c61-b2eb-8aee0b6651e7`
- Spares, for a restart or a chapter past Year 10: `local_01ab03b0-deac-4c1d-b3f8-497e481a350b`, `local_3c36cdbf-933e-4142-98a2-90313b6b701c`, `local_450ba9c7-2e24-4c5a-8c7e-b1419a1fc6c4`

## Chapter 1 (Years 1–2)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 3 Gentry | Rich | a59f46423c94ae70d | 001 (Year 1 rent) |
| 1 Emperor | Reina | afef81aae62154dcc | 002 (Year 1 crown) |
| 2 Official | Clark | ae4dcae8dc01ac418 | 003 (Year 1 collect) |
| 4 Scholar | Noah | a58f6eeb4e49a75ec | 007 (Year 1 auctions) |
| 5 Silk | Silke | af21eb7be9b8689dc | 008 (Year 1 auctions) |
| 6 Rice | Paddy | ac3d9f7950e76275e | 009 (Year 1 auctions) |
| 7 Wheat | Graham | a9ed943ecf2038917 | 010 (Year 1 auctions) |

## Chapter 2 (Years 3–4)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Reina | a66e01219e11d1904 | 036 (Year 3 I Ching) |
| 3 Gentry | Rich | a84ebcf69a98c97da | 037 (Year 3 rent) |
| 1 Emperor | Noah | adb9075898cd81333 | 038 (Year 3 crown) |
| 2 Official | Clark | a46b429ce894b4b23 | 040 (Year 3 collect) |
| 5 Silk | Silke | a20bd7311dbabf0ea | 044 (Year 3 auctions) |
| 6 Rice | Paddy | a6362385717578bd8 | 045 (Year 3 auctions) |
| 7 Wheat | Graham | ab3a0389d6c1a2247 | 046 (Year 3 auctions) |

## Chapter 3 (Years 5–6)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Noah | a4fc690ce11b0b5d0 | 084 (Year 5 I Ching) |
| 3 Gentry | Reina | a175b3d808ebd280d | 085 (Year 5 rent) |
| 1 Emperor | Clark | a491130e8b4ce7f50 | 086 (Year 5 crown) |
| 2 Official | Rich | a153fadd0dda2f807 | 087 (Year 5 collect) |
| 5 Silk | Silke | a4bf3a525989daf64 | 091 (Year 5 land) |
| 6 Rice | Paddy | af3b3807691f0443a | 092 (Year 5 land) |
| 7 Wheat | Graham | a61c6fdcc322f034b | 093 (Year 5 land) |

## Chapter 4 (Years 7–8)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Paddy | aaf4f8c2325d05ffb | 137 (Year 7 I Ching) |
| 3 Gentry | Reina | a22b12b18b9d0863d | 138 (Year 7 rent) |
| 1 Emperor | Graham | adb94992571fc0620 | 139 (Year 7 crown) |
| 2 Official | Clark | ad5c8307e8ffb4ad3 | 140 (Year 7 collect) |
| 5 Silk | Silke | a65c07ea900482189 | 143 (Year 7 rent and land) |
| 6 Rice | Rich | a9c8b264504e6fadd | 144 (Year 7 land) |
| 7 Wheat | Noah | a89d6c43f07b8e59b | 145 (Year 7 rent and land) |

## Chapter 5 (Years 9-10)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Paddy | a0ee1675764f23744 | 186 (Year 9 I Ching) |
| 3 Gentry | Silke | a558402ba1ff3495d | 187 (Year 9 rent) |
| 1 Emperor | Graham | a0404d4cc465d49df | 188 (Year 9 crown) |
| 2 Official | Clark | a97dfc4f162460967 | 189 (Year 9 collect) |
| 5 Silk | Reina | aa1bd6c8b823380ef | 193 (Year 9 rent and land) |
| 6 Rice | Rich | a62685dc44a226c80 | 194 (Year 9 rent and land) |
| 7 Wheat | Noah | adad74f2ad02fa7b3 | 195 (Year 9 rent and land) |

## Chapter 6 (Years 10-11)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Silke | a538a20eeab84549d | 218 (Year 10 I Ching) |
| 3 Gentry | Graham | a606ddd5af9d767b5 | 219 (Year 10 rent) |
| 1 Emperor | Noah | ac11b53ac3ffdd60f | 220 (Year 10 crown) |
| 2 Official | Clark | a5b006c487621a73b | 221 (Year 10 collect) |
| 5 Silk | Reina | a62ffdb3610b1f5d1 | 223 (Year 10 rent and land) |
| 6 Rice | Rich | a8bdbd2124e6028f5 | 224 (Year 10 rent and land) |
| 7 Wheat | Paddy | a715824564c7e282c | 225 (Year 10 rent and land) |

## Chapter 7 (Years 12–13), Storyteller session local_450ba9c7-2e24-4c5a-8c7e-b1419a1fc6c4

| Seat | Player | Agent | First prompt |
|---|---|---|---|
| 4 Scholar | Silke | ad69718053981cab4 | 270 (Year 12 I Ching) |
| 3 Gentry | Noah | a05e83e7c9f8d7fec | 271 (Year 12 rent) |
| 1 Emperor | Rich | a095e55777aae0de1 | 272 (Year 12 crown) |
| 2 Official | Clark | a111b6ecfad622e64 | 273 (Year 12 collect) |
| 5 Silk | Graham | af8aa49bac8a819fa | 276 (Year 12 rent and land) |
| 6 Rice | Reina | ac773193eee15aea9 | 277 (Year 12 rent and land) |
| 7 Wheat | Paddy | a023f747285a45821 | 278 (Year 12 rent and land) |
