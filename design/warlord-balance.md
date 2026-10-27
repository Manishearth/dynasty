# Warlord balance: simulated campaigns

The question (Manish, 2026-10-27): the Warlord's task should "not feel impossible", everyone should "feel the threat of the Warlord", and the task "should not be too easy either". Should the Warlord be able to replace lost soldiers, should bought soldiers act before their province is raided, and should a palace count toward his objective?

`tools/warlord_sim.py` plays many Warlord campaigns on the real board to compare the options. This note records what it models, what it found, and what was adopted. The rules themselves are in `RULINGS.md` ("The Warlord's objective leaves out the Emperor", "The Warlord hires reinforcements").

## What the simulator models

- **The board** is `map.json`. Soldiers move one square a round, diagonals included. Captures are straight on only, and the Warlord moves first. Stepping onto an un-raided square of an occupied province raids it: 5, 10 in Province 1, 20 for a palace, or the realia on it. River crossings cost the Warlord 5.
- **The provinces** place one piece of realia a round for the first four rounds, on their deepest free square (one time in five, carelessly), and the Emperor builds palaces in Years 1, 2 and 5. Each province buys guards up to a random budget once the Warlord comes within five squares of its pieces or raids it. The budget per province is 0–1 at **low** defence (average 0.3), 0–2 at **medium** (average 1) and 1–3 at **high** (average 2), with only the 8 mercenaries in the box for everyone. Guards prefer to stand on their most threatened piece, step away from squares a Warlord soldier could capture them from, and capture any Warlord soldier that ends straight beside them.
- **The Warlord** starts his army where it covers the provinces' deep squares best and plays a greedy campaign: each soldier heads for a different needed piece, avoids ending beside an active guard unless it's taking a piece, and will step beside a guard on a piece as bait when he has a soldier to spare. He earns 10 a round early on, nothing in the middle years and loses 10 a round late, plus raids and his 5 from each soldier sold. One round in ten, a disaster stops his raids.
- **Not modelled:** the I Ching cards beyond that, seat changes, deals and bribes, announcements, the Emperor's money, Wall and canal tolls. Both sides play greedily, not well. Treat the numbers as comparisons between rules, not predictions for a table.

Games run for 10 years at eight and six players and 9 at five, the lengths of the playthroughs. The six-player table is Provinces 1, 2, 3, 5, 7 and 8; the five-player table is the peasant game's.

## Results

How often the Warlord completes his objective (and the median year he does), at low / medium / high defence. 60 games a cell for the first table, 100 for the second.

| Rule set | 8 players | 6 players | 5 players |
|---|---|---|---|
| **A**: closed sea, a palace counts as the Emperor's piece (as first read) | 12 / 0 / 0% | 7 / 3 / 0% | 25 / 3 / 0% |
| **B**: open sea, Emperor left out (the rules before this change) | 40 / 13 / 2% | 22 / 7 / 3% | 67 / 25 / 12% |
| **C**: B + hiring up to the number of players | 93 / 67 / 38% | 90 / 75 / 40% | 97 / 85 / 55% |
| **D**: C + one palace may stand in for a player at eight | 98 / 83 / 68% | 93 / 72 / 37% | 93 / 78 / 55% |
| **E**: D + bought soldiers move in their own province from the start | 100 / 63 / 52% | 87 / 67 / 37% | 98 / 73 / 60% |
| **G**: B + the eight-player palace wildcard | 67 / 10 / 3% | 23 / 10 / 5% | 63 / 25 / 7% |

| Rule set (B + the eight-player wildcard, plus) | 8 players | 6 players | 5 players |
|---|---|---|---|
| **H**: hiring only to replace losses | 83 / 51 / 36% (year 7–8) | 22 / 13 / 2% | 66 / 49 / 16% |
| **J**: hiring up to the starting army + 1 | 93 / 61 / 39% (year 7–8) | 72 / 44 / 14% (year 8–9) | 95 / 60 / 37% (year 6–8) |
| **K**: hiring up to the starting army + 2 | 95 / 78 / 61% | 85 / 49 / 30% | 97 / 80 / 56% |

Other measures, for J: almost every realia province is raided at least once (94–98%), and at eight players the Emperor 2–3 times a game. The Warlord loses 2–6 soldiers a game and hires 2–6.

## What it shows

- **Before this change the objective was rarely completed** once the provinces defended at all: 13% at eight players with medium defence, 7% at six.
- **Hiring is the strongest lever.** Replacing losses (H) roughly quadruples completion at eight players. Hiring up to the number of players (C, Manish's first idea for the cap) makes the objective close to certain.
- **The palace wildcard matters at eight players** (G against B, D against C), where it lets the Warlord skip his worst target and brings him into Province 1.
- **The home guard barely matters** (E against D). The province's soldiers move right after the Warlord in the same round, so the raid that wakes a guard lets it act at once. Its real weakness is narrower: a frozen guard on a piece by the border is a free capture-and-take. The rulebook now says so in Section 14, instead of changing the rule.
- **Guards work when they stand on a piece.** A lone raider can't take a guarded piece; it takes two soldiers and a sacrifice. That makes defence a choice of which pieces to guard, since the Warlord needs only one piece from each player.

## What was adopted

**J and the eight-player wildcard.** The Warlord may hire one soldier a round for 20, after he moves, on his own territory, up to one more than his starting army. At eight players one palace raid may stand in for one player's piece. Bought soldiers still wait for their province's first raid. At medium defence the Warlord completes his objective in roughly half of the simulated games, around Year 8; with strong defence, in a third or fewer. Against careless defence, he nearly always does.

The six-player table is the hardest for him, with four targets and two soldiers. If play shows it's too hard, the next lever is a starting army of three at six players.

## Re-running

```bash
python tools/warlord_sim.py --games 100 --variants BGHJK
```

`--trace 8 J --defence medium --seed 3` prints one game round by round. The variants are defined at the top of the script.
