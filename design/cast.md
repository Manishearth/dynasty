# The cast

The same eight friends play every evening. Each name is a **pun on the province the player drew on the first evening**, and Manish chose them to be subtle: they sound like real people until you hear the joke. The Scholar was originally Ken Nakamura, then Noah Lott ("know a lot"), and is now **Noah Tall** ("know-it-all"); every script uses the current name.

| Seat drawn (game 1) | Full name | Short | The pun |
|---|---|---|---|
| 1 Emperor | Reina Osorio | Reina | *reina* is Spanish for "queen" |
| 2 Official | Clark Grafton | Clark | clerk + graft |
| 3 Gentry | Richard Baron | Rich | a rich baron |
| 4 Scholar | Noah Tall | Noah | "know-it-all" |
| 5 Silk Peasant | Silke Weber | Silke | silk weaver (*Weber* is German for "weaver") |
| 6 Rice Peasant | Paddy Doyle | Paddy | rice paddy |
| 7 Wheat Peasant | Graham Garner | Graham | grain garner |
| 8 Warlord | Robert Land | Rob | rob land / robber |

From the pun chat: Manish rejected "Reed" because there were too many R names. He liked loud groan-worthy puns as long as the name has a real surname. Reina Osorio and Robert Land were floated as candidates for a later pun touch-up; nothing has been decided.

## How each one thinks (the hover voice)

From `playthrough-sim/docs/writing-a-game.md`:

- **Reina** manages the table: plans years ahead, knows when she's walking into a revolt clause.
- **Clark** is gleeful about leverage and keeps a paper trail of grievances.
- **Rich** fawns out loud and calculates underneath; keeps promises to the letter.
- **Noah** is honest to a fault and the one who says the arithmetic out loud.
- **Silke** gets sharper as she gets squeezed.
- **Paddy** is earnest and a little surprised to be winning.
- **Graham** gets quieter and more precise as the grievance builds.
- **Rob** has realised he's the villain and is having a wonderful time.

The pronouns the scripts use: Reina, Silke: she. Clark, Rich, Paddy, Graham, Rob, and Noah: he.

In the engine, `CAST_NAMES` and `CAST_SHORT` hold the cast keyed by their first-evening seat. A game where the booklets fall differently passes `setup(cast={seat: short name})`.

## What happened

**Evening 1: the full game** (`game1_full.py`, 8 players, 12 years, 210 entries). The Emperor builds palaces and the Wall, the peasants' reservoir never comes, and Graham counts the deferrals out loud until the table revolts. Chaos follows, and Graham becomes Emperor. On the real map Rob's four soldiers walk real routes; the river along the 4/5 border charges his notch soldier at almost every step, and he ends 5 in debt.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Wheat Peasant | lost |
| Clark | Official → Silk Peasant | lost (ends in debt) |
| Rich | Gentry → Rice Peasant | lost (ends in debt) |
| Noah | Scholar → Official | won |
| Silke | Silk Peasant → Scholar | won |
| Paddy | Rice Peasant → Gentry | won |
| Graham | Wheat Peasant → Emperor | won |
| Rob | Warlord → Warlord | held |

**Evening 2: the peasant game** (`game2_peasant.py`, 5 players, 9 years, 121 entries). The Emperor, three peasants and the Warlord. With no Official, Gentry or Scholar, there's no rent, and Reina appoints people to do those jobs. She remembers game 1 and builds the reservoir first. Rob's northern soldier walks three years to the Winter Palace and on through empty Province 4 to the back door of Province 5, where Reina captures it with a soldier she bought from him. Every public work is finished in Year 9, which is the survival ending, with Reina down to 2.5.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Emperor | won (held the throne) |
| Silke | Silk → Wheat Peasant | lost |
| Paddy | Rice → Silk Peasant | won |
| Graham | Wheat → Rice Peasant | won |
| Rob | Warlord → Warlord | held (3 of 4 objective pieces) |

**Evening 3: the short game** (`game3_short.py`, 4 players, 8 rounds, 89 entries). The upper group only: no Warlord and no peasants, so no rent and no raids. Clark wins the throne by buying the Bamboo Brush for 70 after Reina bribed Rich with 40.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Official | lost |
| Clark | Official → Emperor | won |
| Rich | Gentry → Gentry | held |
| Noah | Scholar → Scholar | held |

**Evening 4: the long game** (`game4_complete.py`, 8 players, 10 years, 169 entries). The booklets are dealt afresh. Graham draws the throne and builds the Province 7 Reservoir first; the table signs a compact to build everything, one work a year with the split agreed in advance, and Silke keeps the minutes. Noah, as Warlord, announces every raid a year ahead. Rob captures one of his soldiers during the Warlord's wedding. Every work is built by Year 10.

| Player | Start → finish | Verdict |
|---|---|---|
| Graham | Emperor → Emperor | won (held the throne) |
| Silke | Official → Official | held (complete, never declared) |
| Paddy | Gentry → Wheat Peasant | lost |
| Rich | Scholar → Rice Peasant | lost |
| Rob | Silk → Scholar | won |
| Clark | Rice → Silk Peasant | won |
| Reina | Wheat → Gentry | won |
| Noah | Warlord → Warlord | held |

**Evening 5: the six-player game** (`game5_six.py`, 6 players, 10 years, 136 entries). Rich and Paddy sit out. Rob draws the throne and Noah the Warlord again, still announcing every move, and this time it works: he raids a different piece from every player and a palace from Rob, and changes places with the Emperor. The table stops there.

| Player | Start → finish | Verdict |
|---|---|---|
| Rob | Emperor → Warlord | lost |
| Silke | Official → Official | held |
| Clark | Gentry → Wheat Peasant | lost |
| Reina | Silk → Silk Peasant | held |
| Graham | Wheat → Gentry | won |
| Noah | Warlord → Emperor | won |

## Who played when

| Evening | Who played | Who sat out |
|---|---|---|
| 1, the full game | everyone, in their pun provinces | — |
| 2, the peasant game | Reina, Silke, Paddy, Graham, Rob | Clark, Rich, Noah |
| 3, the short game | Reina, Clark, Rich, Noah | Silke, Paddy, Graham, Rob |
| 4, the long game | everyone, booklets dealt afresh | — |
| 5, the six-player game | Rob, Silke, Clark, Reina, Graham, Noah | Rich, Paddy |

A player can refer only to evenings they played in. Some facts the scripts lean on: Reina was Emperor on evenings 1, 2 and 3; Rob was the Warlord on evenings 1 and 2 only, and has sold the table five soldiers; Noah was the Warlord on evenings 4 and 5; the Province 7 Reservoir was built on evenings 2 and 4 and never on 1.
