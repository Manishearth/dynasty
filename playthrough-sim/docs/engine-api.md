# Engine API reference

Everything in `engine.py` and `cards.py`, grouped by purpose. Every name is a global inside a game script.

**Conventions used below.** *seat* is a province, 1–8. *player* is a player id — the seat that player drew at setup. *hover* is a string, a `"Name: thought"` string, or a list from `TH(...)`. Every function that records an entry takes a full state snapshot at that moment; see [`page-format.md`](page-format.md#state-snapshots) for what a snapshot holds.

- [Constants](#constants)
- [Game state](#game-state)
- [Setup and rounds](#setup-and-rounds)
- [Recording entries](#recording-entries)
- [Money](#money)
- [Public works](#public-works)
- [Realia and auctions](#realia-and-auctions)
- [Seat changes](#seat-changes)
- [The Warlord](#the-warlord)
- [Disasters](#disasters)
- [Queries](#queries)
- [The board](#the-board)
- [Ending](#ending)
- [The cards](#the-cards)

## Constants

| Name | Value |
|---|---|
| `NAMES`, `SHORT` | Player id → full name and short name. 1 Reina Osorio, 2 Clark Grafton, 3 Richard Baron (Rich), 4 Ken Nakamura, 5 Silke Weber, 6 Paddy Doyle, 7 Graham Garner, 8 Robert Land (Rob). |
| `ROLE` | Seat → role: Emperor, Official, Gentry, Scholar, Silk/Rice/Wheat Peasant, Warlord. |
| `REALIA` | Seat → the realia native to it: 2 `CH`, 3 `LD`, 4 `BB`, 5 `DJ`, 6 `WB`, 7 `VA`. |
| `NEVER` | Seat → the realia type that seat's objective never asks for: 2 `DJ`, 3 `WB`, 4 `VA`, 5 `CH`, 6 `BB`, 7 `LD`. At 4–5 players each province also starts holding two of these. |
| `RNAME` | Realia code → name: Customs House, Land Deed Scroll, Bamboo Brush, Dragon Jar, Wooden Bowl, Vase. |
| `CONS` | Seat → consumption at base population: 60 for Province 1, 20 for Province 8, 40 for the rest. |
| `HARV` | Seat → harvest by quality: `{"good": 100, "avg": 75, "bad": 50}`, or 40/30/20 for Province 8. |
| `DISASTERS` | Seat → its three personal disasters in booklet order (see [Disasters](#disasters)). |
| `PILE_START` | 2,500 — the value of the physical Harvest Pile. |
| `PW_BONUS` | The irrigation and reservoirs' bonuses: `irr2` → Province 2 +10, `res3` → Province 3 +20, `res7` → Province 7 +20. |
| `PALACE_CELL` | Where each palace is drawn: row 2, columns 21, 23 and 25. |
| `GRID`, `CELLS`, `COLS`, `ROWS`, `RESERVED` | The 30 × 17 board (see [The board](#the-board)). |

## Game state

These globals are created by `setup()` and changed by everything else. Read them freely; prefer the functions for writing.

| Name | Shape | Meaning |
|---|---|---|
| `ACTIVE` | `[seat]` | The seats in play, sorted. |
| `PLAYERS` | `[player]` | Player ids — the same numbers as `ACTIVE` at setup. |
| `seat` | `{seat: player}` | Who is sitting where. |
| `grain` | `{player: float}` | Each player's grain. Can go negative: that is debt. |
| `held` | `{player: {code: n}}` | Realia each player owns. |
| `stock` | `{seat: {code: n}}` | Realia each province still has to auction, including pieces returned to it. |
| `pile` | float | The Harvest Pile. |
| `bonus` | `{seat: int}` | Permanent harvest bonus from public works, in effect this round. |
| `pending_bonus` | `{seat: int}` | Bonuses from works built this round; added to `bonus` when the next round starts. |
| `pw` | dict | What's built: `"Summer Palace"`, `"Winter Palace"`, `"Marble Pagoda"`, `irr2`, `res3`, `res7` as 0/1; `wall` as `{1: n, 2: n, 3: n}` links above each province; `canal` as `{1: n, 4: n, 5: n, 6: n}` sections in each. |
| `raids` | `{seat: n}` | Squares raided in each province. |
| `board` | `{"r,c": {...}}` | What's on each square (see [The board](#the-board)). |
| `MULT` | float | The population multiple: 1, 1.5, 2, 3, … |
| `CUR_Q` | `{seat: "good"/"avg"/"bad"}` | This round's harvest quality. |
| `CUR_INC`, `CUR_HARV` | `{seat: float}` | This round's income and gross harvest, set by `harvest()`. |
| `warlord_got` | `{player: code or palace}` | The Warlord's objective so far: what he has raided from whom. |
| `ROB_N` | int | The Warlord's soldiers still in play. |
| `ENTRIES`, `ROUNDS` | lists | The transcript and the round index. |

## Setup and rounds

### `setup(active, key, title, subtitle, blurb, short="")`

Start a game. Resets all state.

- `active` — the seats in play, e.g. `[1,2,3,4]`.
- `key` — the game's id in the page address (`#key`).
- `title`, `subtitle`, `short` — the game-selector button; `short` replaces `subtitle` on phones.
- `blurb` — the paragraph under the page header.

Effects: everyone has 60 grain; the pile is 2,500 less the grain dealt; each realia province's `stock` is set by player count — at 4–5 players, one of its own and two of its `NEVER` type; at 6, two of its own; at 7 or more, four of its own. The Warlord gets four soldiers at 8 players, two otherwise.

### `R(n, title, card=None, card_text=None)`

Start round `n`. Applies any bonuses pending from last round's works, then draws `card` — a key in `CARDS` — setting `CUR_Q` from the card's harvest and multiplying `MULT` for a population card. A card already drawn this game raises an error.

For round one pass `card=None` and the text to show as `card_text`. Records a round marker (not an entry).

## Recording entries

### `act(text, hover=None, deltas=None, map_hl=None, pile_delta=0, big=False)`

A game event — a bold, clickable line.

- `deltas` — `{player: change}`. Applied before the snapshot.
- `pile_delta` — change to the Harvest Pile.
- `map_hl` — seats to highlight on the board.
- `big` — style the line as a turning point (seat changes use this).

### `say(who, text, hover=None)`

Table talk: `who` is a short name. Changes nothing. A plain-string hover is attributed to `who`.

### `TH(*pairs)`

Build a multi-voice hover: `TH(("Rob", "..."), ("Reina", "..."))`.

## Money

### `harvest(note=None, hover_extra=None)`

Pay every active province its income — `HARV[seat][quality] + bonus − CONS[seat] × MULT` — from the pile (negative income is paid into it). Sets `CUR_INC` and `CUR_HARV`. `note` replaces the line's text; the hover lists every income. `hover_extra` (a list) is prepended to the hover.

### `rents(rate=5, note=None, hover=None)`

Each occupied peasant province pays the Gentry `rate`. Does nothing if Province 3 is empty.

### `taxes(rate, skip=(8,), collector=None, hover=None, extra=None)`

The Emperor's tax: `rate` (0.5 = 50%) of each province's `CUR_INC`, paid to whoever holds Province 1. Negative income pays nothing. `skip` — seats that pay nothing (the Warlord by default). `collector` — replaces "The Official collects the tax". `extra` — `{seat: income}` added to the taxable income for this call only. Returns the total collected.

### `salaries(pay=None, text=None, hover=None)`

The Emperor pays `pay` — `{seat: amount}` — defaulting to 5 each to Provinces 2 and 4 when present. Does nothing if nobody is owed.

## Public works

### `build(name, cost, split, wall=None, canal=None, key=None, hover=None, text=None)`

One public-works project.

- `split` — `{seat: amount}`; must sum to `cost`.
- `key` — for single works: `"Summer Palace"`, `"Winter Palace"`, `"Marble Pagoda"`, `"irr2"`, `"res3"`, `"res7"`.
- `wall` — `{seat: links}` built above provinces 1, 2 or 3.
- `canal` — `{seat: sections}` built in provinces 1, 4, 5 or 6. Each section adds 10 to that province's harvest from next round.
- `text` — replaces "Public works: *name* — *cost* paid."

The engine does **not** check prerequisites or the one-project-per-round rule.

### `owed()`, `built_count(name)`, `all_built()`

`owed()` lists `[name, count, cost each]` for every work owed at this table: the three palaces, four Wall links per occupied province among 1–3, two canal sections per occupied province among 1, 4, 5 and 6, and each irrigation or reservoir whose province is occupied. `built_count(name)` counts what's built; `all_built()` is true when everything owed stands.

## Realia and auctions

### `lot(sell, typ, ladder, hover=None)`

Auction one piece of `typ` from seat `sell`'s stock. `ladder` is a list of `B(...)` bids; the last numeric bid wins. The winner pays the price, the seller receives a quarter, three quarters go to the pile, and the piece is placed on a square in the winner's province. A commission note is appended to `hover`.

### `B(seat, amt, text=None, th=None)`

One bid. `amt=None` is a pass. `text` defaults to the amount spelled out ("Twenty-two.") or "Out." for a pass. `th` is the bidder's hover; a plain string is attributed to the bidder.

### `give(frm, to, typ)`

Move one piece between **players** for a private trade, and re-place it on the board. Record the grain with a separate `act(..., deltas)` after it.

### `need_for(seat)`

The realia codes the player in `seat` must collect. At 4–5 players: every type except the seat's own and its `NEVER` type. At 6: one native to each other occupied realia province. At 7 or more: every type except its own.

### `home(code)`

Where a returned piece goes: its native province, or, if that province is empty, the province that started the game holding it (rulebook Note 11).

## Seat changes

### `swap(a, b, note, hover=None, draw=60, check=True)`

The player in seat `a` replaces the player in seat `b`.

With `check=True` (the default) it first asserts that the mover holds everything `need_for(a)` requires, has at least 20 grain, and may move to `b`: only seats 2, 3, 4 and 8 may take Province 1; a peasant may only take 2–7. Use `check=False` for a Chaos acclamation.

Then: pieces native to `b` held by the mover return to `b`'s stock; if `b` is the throne, all the mover's pieces return home; the displaced player returns everything; the mover takes all of the displaced player's grain; the displaced player draws `draw` (60) from the pile, or what's left if the pile is lower; the seats swap; the mover's pieces are re-placed in the new province. Records a `big` act.

## The Warlord

### `raid(rows, text="Robert Land raids.", hover=None)`

`rows` — `[(seat, tribute)]`. For each: an unraided square in that province is marked, a Warlord soldier moves there, and the province's player pays `tribute` to the Warlord. Use 10 for Province 1 and 5 elsewhere.

### `raid_take(seat, typ, text, hover=None)`

The Warlord raids the square holding the player's `typ` piece and takes it. The piece moves to the Warlord, the square is marked raided, and the raid is recorded in `warlord_got`.

### `raid_palace(name, text, hover=None)`

The Warlord raids a palace square; the Emperor pays him 20, the structure's cost. Recorded in `warlord_got`.

### `sell_soldiers(buyers, text, hover=None)`

Each seat in `buyers` (repeat a seat to buy two) pays 20; the Warlord keeps 5 of each and 15 goes to the pile. A blue soldier is drawn in the buyer's province.

### `capture_soldier(text, hover=None)`

The Warlord loses a soldier: `ROB_N` drops by one and the oldest soldier disappears from the board.

The engine moves soldiers onto raided squares and keeps only the last `ROB_N` of them on the board, but it does **not** stop a script from raiding more squares than the Warlord has soldiers.

## Disasters

### `disaster(seat, text, hover=None)`

Play the next disaster in `seat`'s booklet; after the third, it starts again. The amount is computed from the booklet:

| Kind | Amount |
|---|---|
| `fixed` | The printed amount |
| `frac_income` | A fraction of this round's income (Officials, Rice and Wheat Peasants) |
| `frac_harvest` | A fraction of this round's gross harvest (Silk Peasant) |
| `frac_grain` | A fraction of the player's grain (Gentry, Scholar, Warlord) |
| `noraid` | Nothing paid — the Warlord can't raid Provinces 5–7 this round. **The script must comply.** |

The amount goes to the Harvest Pile, and the line reads "*Name*'s disaster #*n*: *text* — *amount* to the Harvest Pile." Write `text` as the event itself; the engine adds the number and the cost.

| Seat | #1 | #2 | #3 |
|---|---|---|---|
| 1 Emperor | 4 | 10 | 30 |
| 2 Official | 4 | 10 | half the round's income |
| 3 Gentry | 5 | 10 | half their grain |
| 4 Scholar | 4 | 10 | a third of their grain |
| 5 Silk Peasant | 4 | 10 | half the round's harvest |
| 6 Rice Peasant | 4 | 10 | half the round's income |
| 7 Wheat Peasant | 2 | 5 | a third of the round's income |
| 8 Warlord | no raids on 5–7 | 5, and no raids this year | half their grain |

Disasters follow the seat, not the player: someone who moves into a province continues that booklet from where it stands.

## Queries

| Function | Returns |
|---|---|
| `pid(seat)` | The player id in a seat. |
| `sid(player)` | The seat a player is in. |
| `income(seat, q=None)` | The seat's income this round, or at quality `q`. |
| `spell(n)` | A number in words, as used for default bid text: "Twenty-two". |

## The board

The page draws a 30-column × 17-row grid. `GRID[row][col]` is one character:

| Character | Region |
|---|---|
| `1`–`8` | A province |
| `W` | The Great Wall strip (row 0, columns 7–26) |
| `n` | New land below the Wall (row 1) |
| `S` | The sea (columns 27–29) |
| `.` | Margin |

Each square in `board` (keyed `"row,col"`) may hold:

| Key | Meaning |
|---|---|
| `realia`, `owner` | A piece and the player who owns it |
| `raid` | The square has been raided and can never be raided again |
| `soldier` | One of the Warlord's live soldiers is here |
| `own_soldier` | A soldier someone bought from the Warlord |

`place(seat, code, player)` puts a piece on the province's first free square; `place_soldier(seat)` puts a bought soldier on its last free square; `mark_raid(seat, take=False)` raids its first free (or, with `take`, first piece-holding) square; `unplace_all(player)` lifts a player's pieces off the board.

`RESERVED` lists the squares where the page draws palaces, canal sections, irrigation and reservoirs. Pieces and raids never land there. **If you move a public-works drawing position in `template/tail.html` (`CANALPOS`, `WORKPOS`, the palace columns), update `RESERVED` to match.**

## Ending

### `export(results_note, epilogue)`

Score the game and return the dictionary the page uses (see [`page-format.md`](page-format.md#the-data-format)). Assign it to `RESULT`.

Scoring follows Section 18: a player who finishes in a lower-numbered province than the one they drew has won, a higher-numbered one has lost, the same one has held — except that an Emperor still on the throne has won. `results_note` is one sentence above the results table; `epilogue` is a list of paragraphs below it.

## The cards

`cards.py` defines `CARDS`, a dictionary of the twenty I Ching cards. Each entry has:

- `text` — the card's wording, exactly as printed;
- `q` — the harvest: `"good"`, `"avg"` or `"bad"` for everyone, or a `{seat: quality}` dictionary for split cards;
- `pop` — for population cards only, the multiplier (2 or 1.5).

| Key | Harvest | Other effect (scripted) |
|---|---|---|
| `blight` | average | — |
| `repairs` | good | 4–7 pay 2 for repairs; 1, 2, 3, 8 play a disaster |
| `canal` | average | unfinished canal destroyed; 2, 3, 7, 8 play a disaster |
| `breach` | good | Wall breached; 1–3 pay; 4–8 play a disaster |
| `rainflood` | good 1, 3, 6, 7; bad 2, 4, 5, 8 | — |
| `chest` | average | the Emperor gives every player 2 |
| `double1`, `double2`, `double3` | good | population doubles (counts at most twice) |
| `share` | average | provinces with public works share the increase 50/50 with the Emperor |
| `utility` | average | 2 from every province, 2 more from each with a public work |
| `heaven` | good 2, 4, 5; bad 1, 3, 6, 7, 8 | — |
| `winds` | average | — |
| `dribble1`, `dribble2`, `dribble3` | bad | — |
| `half1`, `half2` | good | population × 1.5 (counts once) |
| `careless` | good | every player plays a disaster |
| `goodevil` | good | 2, 4, 6, 8 play a disaster |

The engine applies the harvest and the population change. It does not enforce the cards' own caps ("if this card has been played twice, collect a good harvest instead"): drawing a third doubling card or a second half card would multiply the population anyway. Don't draw them, or the population will pass the 600-million ceiling the cards set.
