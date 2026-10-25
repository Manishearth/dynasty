# playthrough-sim

The scripts that generate `../playthrough.html`: three annotated games of Dynasty, played by the same group of friends on three evenings.

| Game | Table | Length | How it ends |
|---|---|---|---|
| `game1_full.py` | All eight provinces | 12 years | A revolt, then Chaos; a wheat farmer becomes Emperor |
| `game2_peasant.py` | Emperor, three peasants, Warlord | 9 years | Every public work is built — the survival ending |
| `game3_short.py` | Emperor, Official, Gentry, Scholar | 8 rounds | The short-game rule; the Official takes the throne |

These are **authored** games, not simulated ones. A person wrote every choice: what each player bids, what they say and what they're thinking. The engine does all the arithmetic and refuses illegal moves, so every number on the page comes from the rules, but the outcome is the author's.

## Quick start

From the repository root, with Python 3.9 or later and no other dependencies:

```sh
python3 playthrough-sim/build.py                  # rebuild ../playthrough.html
python3 playthrough-sim/trace.py game2_peasant.py # print everyone's grain after every line of one game
```

`build.py` takes an optional output path: `python3 playthrough-sim/build.py /tmp/test.html`.

## What's in the folder

| Path | What it is |
|---|---|
| `engine.py` | The rules: harvests, consumption, tax, rent, auctions, raids, disasters, public works, seat changes, the board, and scoring |
| `cards.py` | The twenty I Ching cards: what each does to the harvest and population, and the reworded text from `../i-ching.json` that the page shows |
| `game1_full.py`, `game2_peasant.py`, `game3_short.py` | One script per game, in play order |
| `build.py` | Runs each game in a fresh namespace and writes the page |
| `trace.py` | Prints a ledger of one game, for checking numbers while writing |
| `template/head.html` | The page's HTML and CSS, up to the opening of the data block |
| `template/tail.html` | The page's JavaScript, from the end of the data block |
| `docs/` | Detailed documentation (below) |

## Documentation

| Document | Read it when you want to… |
|---|---|
| [`docs/writing-a-game.md`](docs/writing-a-game.md) | edit a game or write a new one: script anatomy, a worked example, the voice conventions, and a checklist |
| [`docs/engine-api.md`](docs/engine-api.md) | look up what a function takes, what it changes, and what it records |
| [`docs/rules-model.md`](docs/rules-model.md) | know which rules the engine enforces, which the script must respect, and which rulings it depends on |
| [`docs/page-format.md`](docs/page-format.md) | change the page: the build pipeline, the data format, and how the page uses it |

## The workflow

1. **Edit a game script.** Change a bid, a line, a tax rate, a build.
2. **Run `trace.py` on it.** Every line prints with everyone's grain afterwards. If the dialogue quotes a number — "I've got sixty", "seventy per cent of nothing" — check it against the ledger. Changing anything early in a game moves every number after it, so re-check the lines downstream of your edit.
3. **Run `build.py`.** It runs all three games; any rule the engine enforces fails loudly here, with the player and the reason.
4. **Open the page and click through the years you touched.**

## What the engine refuses

The engine raises an error, naming the player and the reason, if a script:

- draws the same I Ching card twice in one game;
- changes seats without the complete set for that seat and 20 grain in hand;
- puts a peasant on the throne, or lets anyone but the Official, Gentry, Scholar or Warlord take it;
- splits a public work so the shares don't add up to its cost.

It also does these automatically, so the script can't get them wrong:

- plays personal disasters in booklet order, computing the fractional ones from the actual income, harvest or grain;
- starts public-works bonuses on the round after a work is built;
- runs the Harvest Pile as a real bank that starts at 2,500 million, pays out harvests, and takes back negative years;
- returns pieces to their province when a player is replaced, and sends any piece whose province is empty back to the province that started with it (rulebook Note 11);
- scores the game by Section 18 of the rulebook, including the rule that an Emperor still on the throne has won.

Some rules can't be checked from the ledger alone and are the script's responsibility — the Warlord's soldier count, disasters that stop raids, prerequisite buildings, order of play. [`docs/rules-model.md`](docs/rules-model.md) lists them.

## License

CC BY-SA 4.0, like the rest of the repository. Dynasty © 1969 Onoma Productions; this is an unofficial fan project.
