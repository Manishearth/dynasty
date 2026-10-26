# The cast

The same eight friends play every game. Each name is a **pun on the province the player sits in**, and Manish chose them to be subtle: they sound like real people until you hear the joke. The Scholar was originally Ken Nakamura, then Noah Lott ("know a lot"), and is now **Noah Tall** ("know-it-all"); every script uses the current name.

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

In the engine, `NAMES` and `SHORT` hold the cast keyed by player id, which is the seat each one draws.

## Every game is its own game

The playthroughs are independent games, not evenings in a series. In every one, each player sits in the province their name puns on; nobody remembers another game, and the banter stays inside the game it's in. Each game reuses the same eight people and the same voices.

## What happened

**The full game** (`game1_full.py`, 8 players, 10 years). Reina builds the Province 7 Reservoir first, and the table signs a compact to build everything: one work a year, the split agreed in advance, Clark keeping the minutes. Rob, as Warlord, announces every raid a year ahead. In Year 8 the population doubles and every income falls to zero or below; the table answers with a land rush, the crown paying a quarter of every square, and the new land's tax pays for the rest of the Wall. Clark, locked out of the land, sells his complete set back to the pile in the last year. Silke captures one of Rob's soldiers during the Warlord's wedding. Every work is built by Year 10.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Emperor | won (held the throne) |
| Clark | Official → Official | held (complete in Year 5, never declared) |
| Rich | Gentry → Wheat Peasant | lost |
| Noah | Scholar → Rice Peasant | lost |
| Silke | Silk → Scholar | won |
| Paddy | Rice → Silk Peasant | won |
| Graham | Wheat → Gentry | won |
| Rob | Warlord → Warlord | held |

**A slow trashfire** (`game2_trashfire.py`, 8 players, 12 years). The Emperor builds palaces and the Wall, the peasants' reservoir never comes, and Graham counts the deferrals out loud. In Year 10, when the population doubles, Reina refuses to subsidise Silke's sea and in the same minute buys two squares of the strip below the Wall, E18 and E19, for Province 1 alone, 40. The table revolts in Year 11: Graham cites the land among his causes, and Clark cites his own debt. Chaos follows, and Graham becomes Emperor with 152. Rob's four soldiers walk real routes, and the river along the 4/5 border charges his notch soldier at almost every step. In the last two years Clark, Graham, Rich and Rob sell their realia back to the Harvest Pile before they sink into debt. Then the table decides to stop: Graham does the sum out loud (420 left to build, 427 between the five solvent players, no tax because every income is negative, land shut to Provinces 2 and 3 behind the unfinished Wall and to the two players in debt, two doubling cards still in the deck) and calls it.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Wheat Peasant | lost |
| Clark | Official → Silk Peasant | lost (ends in debt) |
| Rich | Gentry → Rice Peasant | lost (ends in debt) |
| Noah | Scholar → Official | won |
| Silke | Silk Peasant → Scholar | won |
| Paddy | Rice Peasant → Gentry | won |
| Graham | Wheat Peasant → Emperor | won |
| Rob | Warlord → Warlord | held (ends 1 in debt) |

**The short game** (`game3_short.py`, 4 players, 8 rounds). The upper group only: no Warlord and no peasants, so no rent and no raids. The population doubles in Round 7, and Noah talks Reina into paying half of three squares of sea for Province 4, K25, J25 and K26, 30 each. Clark wins the throne by buying the Bamboo Brush for 70 after Reina bribed Rich with 40. Rich finishes with the most grain, 146.5, and wins the tiebreak outright.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Official | lost |
| Clark | Official → Emperor | won |
| Rich | Gentry → Gentry | held |
| Noah | Scholar → Scholar | held |

**The peasant game** (`game4_peasant.py`, 5 players, 9 years). The Emperor, three peasants and the Warlord. With no Official, Gentry or Scholar, there's no rent, and Reina appoints people to do those jobs. She builds the reservoir first. In Year 8 the population doubles and leaves the crown with half a million. Rob threatens a revolt over cause six, the Emperor not subsidising new land, and Paddy, who would take the throne in Chaos and doesn't want it, pays Reina 130 and most of the Wall to keep the game ending. Silke buys two squares of the Warlord's land (T16, T17), Graham two of sea (R25, S26) and Paddy two of sea (M26, N26), the crown paying 10 of each 40. Rob's northern soldier walks three years to the Winter Palace and on through empty Province 4 to the back door of Province 5, where Reina captures it with a soldier she bought from him. Every public work is finished in Year 9, which is the survival ending, with Reina still down to 2.5; Rob finishes richest, with 157.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Emperor | won (held the throne) |
| Silke | Silk → Wheat Peasant | lost |
| Paddy | Rice → Silk Peasant | won |
| Graham | Wheat → Rice Peasant | won |
| Rob | Warlord → Warlord | held (3 of 4 objective pieces) |

**Land, Robbed** (`game5_six.py`, 6 players, 10 years). Noah and Paddy sit out. Rob, as Warlord, announces every move a year ahead, and it works: he raids a different piece from every player and a palace from Reina, and changes places with the Emperor. The table stops there. The title is the Warlord's name, and what he does.

| Player | Start → finish | Verdict |
|---|---|---|
| Reina | Emperor → Warlord | lost |
| Clark | Official → Official | held |
| Rich | Gentry → Wheat Peasant | lost |
| Silke | Silk → Silk Peasant | held |
| Graham | Wheat → Gentry | won |
| Rob | Warlord → Emperor | won |
