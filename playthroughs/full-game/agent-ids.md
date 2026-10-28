# Player agents: the full game

Each seat is one `dynasty-player` agent (`.claude/agents/dynasty-player.md`), launched fresh at the start of each chapter (`briefs.py prompt ... launch`, which carries the ledger entry and the diary) and continued with SendMessage for the rest of that chapter. An agent can be resumed by id only from the session that launched it.

## Chapter 1 (Setup–Year 2)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 8 Warlord | Rob | a558d88f04d1a33d8 | 001 (Setup) |
| 3 Gentry | Rich | aeb4a8a302391cf55 | 002 (Year 1 rent) |
| 1 Emperor | Reina | a808cee9ee71c2e1c | 003 (Year 1 crown) |
| 2 Official | Clark | a3c16de1dc58a6703 | 004 (Year 1 collect) |
| 4 Scholar | Noah | a7774e5a2ab6b6f1a | 008 (Year 1 auctions) |
| 5 Silk | Silke | ac624be70d5242910 | 009 (Year 1 auctions) |
| 6 Rice | Paddy | a60460b648be90ae6 | 010 (Year 1 auctions) |
| 7 Wheat | Graham | ad02ca845264eb316 | 011 (Year 1 auctions) |

## Chapter 2 (Years 3–4)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Noah | a8f4b170fe579c946 | 040 (Year 3 I Ching) |
| 3 Gentry | Reina | a103df0ee475ab026 | 041 (Year 3 rent) |
| 1 Emperor | Rich | ab72ea2212238aa60 | 042 (Year 3 crown) |
| 2 Official | Clark | a27e9f0fe42c7f588 | 043 (Year 3 collect) |
| 5 Silk | Silke | a225bea0799dce037 | 047 (Year 3 auctions) |
| 6 Rice | Paddy | a2f308ab73a4d5f04 | 048 (Year 3 auctions) |
| 7 Wheat | Graham | a5a4af00f819c237c | 049 (Year 3 auctions) |
| 8 Warlord | Rob | a9c03fae6d36bba6f | 050 (Year 3 auctions) |

## Chapter 3 (Years 5–6)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Noah | a7f7dd808225a0af2 | 078 (Year 5 I Ching) |
| 3 Gentry | Reina | a489bad34cc57a45c | 079 (Year 5 rent) |
| 1 Emperor | Rich | ae2201f58f9df2976 | 080 (Year 5 crown) |
| 2 Official | Graham | a3fec45d9c7b01063 | 082 (Year 5 collect) |
| 5 Silk | Silke | ac321c58e2a0e4a5d | 086 (Year 5 auctions) |
| 6 Rice | Paddy | ace8f878546173990 | 087 (Year 5 auctions) |
| 7 Wheat | Clark | a2afecae5de68b94a | 088 (Year 5 auctions) |
| 8 Warlord | Rob | aaf3a77143ef16323 | 089 (Year 5 auctions) |

## Chapter 4 (Years 7–8)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Graham | a7da96a6d34cd17f1 | 116 (Year 7 I Ching; a first launch, a3fc9f5b500f79fd8, was sent an empty prompt by mistake and stopped unplayed) |
| 3 Gentry | Noah | aef6e125f143b93e0 | 117 (Year 7 rent) |
| 1 Emperor | Rich | ab78db3d8b3649d95 | 118 (Year 7 crown) |
| 2 Official | Silke | af9c675341c5257c6 | 119 (Year 7 collect) |
| 5 Silk | Reina | a6f8dafa45b1d6887 | 123 (Year 7 auctions) |
| 6 Rice | Paddy | a81fb681a30050356 | 124 (Year 7 auctions) |
| 7 Wheat | Clark | af7ecf3d663795af7 | 125 (Year 7 auctions) |
| 8 Warlord | Rob | ab82208014094e752 | 126 (Year 7 auctions) |

## Chapter 5 (Years 9–10)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Graham | a4fe5495eafab4a00 | 155 (Year 9 I Ching) |
| 3 Gentry | Paddy | af95d0daf160e5598 | 156 (Year 9 rent) |
| 1 Emperor | Silke | a9ad43ae1a4c8e111 | 157 (Year 9 crown) |
| 2 Official | Rich | af3c83e11b99e8843 | 158 (Year 9 collect) |
| 5 Silk | Reina | aeb189e44d1f7c416 | 162 (Year 9 auctions) |
| 6 Rice | Noah | a01138d874528206f | 163 (Year 9 auctions) |
| 7 Wheat | Clark | a059cbb90340edb85 | 164 (Year 9 auctions) |
| 8 Warlord | Rob | ae9ee48bd581308f4 | 165 (Year 9 auctions) |

## Chapter 6 (Years 11–12)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Silke | aacfaae4ae63faa84 | 199 (Year 11 I Ching) |
| 3 Gentry | Reina | a48858ec634471ccb | 200 (Year 11 rent) |
| 1 Emperor | Graham | a113ea2105feda400 | 201 (Year 11 crown) |
| 2 Official | Rich | aea7ffcc87795e5a8 | 203 (Year 11 collect) |
| 5 Silk | Clark | a91fe319eea426808 | 207 (Year 11 auctions) |
| 6 Rice | Noah | a055dcc4c89e7f89c | 208 (Year 11 auctions) |
| 7 Wheat | Paddy | a5b595eb43b271cd5 | 209 (Year 11 auctions) |
| 8 Warlord | Rob | af6be42bb51338522 | 210 (Year 11 auctions) |

(Two stray launches by mistake, both unplayed: ab9788ec92e2e2b54, sent the word "noop" before 201, and aad2c5d4ae0b4a604, sent a "sent by mistake, reply ok" line before Paddy's 224.)

## Chapter 7 (Year 13)

| Seat | Player | Agent id | Launched at |
|---|---|---|---|
| 4 Scholar | Silke | abd81774499b69a0c | 244 (Year 13 I Ching) |
| 3 Gentry | Rich | af924b08107f00508 | 245 (Year 13 rent) |
| 1 Emperor | Reina | a24be7f3108d06943 | 246 (Year 13 crown) |
| 2 Official | Graham | a2e6ef603cb380275 | 247 (Year 13 collect) |
| 5 Silk | Clark | a99a575065ac01c8a | 253 (Year 13 last words) |
| 6 Rice | Noah | ad987b49a6a997270 | 254 (Year 13 last words) |
| 7 Wheat | Paddy | aaf966e90142c09ca | 255 (Year 13 last words) |
| 8 Warlord | Rob | a8aff7d8400d6466e | 256 (Year 13 last words) |
