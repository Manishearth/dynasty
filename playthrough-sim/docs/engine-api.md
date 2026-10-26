# Engine API reference

Everything in `engine.py` and `cards.py`, grouped by purpose. Every name is a global inside a game script.

**Conventions used below.** *seat* is a province, 1–8. *player* is a player id — the seat that player drew at setup. *square* is a board square named like `"H12"`: row letter A–V, column 1–30. *hover* is a string, a `"Name: thought"` string, or a list from `TH(...)`. Every function that records an entry takes a full state snapshot at that moment; see [`page-format.md`](page-format.md#state-snapshots) for what a snapshot holds.

- [Constants](#constants)
- [Game state](#game-state)
- [Setup and rounds](#setup-and-rounds)
- [Recording entries](#recording-entries)
- [Money](#money)
- [Public works](#public-works)
- [Realia and auctions](#realia-and-auctions)
- [Seat changes](#seat-changes)
- [Soldiers](#soldiers)
- [Disasters](#disasters)
- [Queries](#queries)
- [The board](#the-board)
- [Ending](#ending)
- [The cards](#the-cards)

## Constants

| Name | Value |
|---|---|
| `NAMES`, `SHORT` | Player id → full name and short name. Every player sits in the province their name puns on: 1 Reina Osorio, 2 Clark Grafton, 3 Richard Baron (Rich), 4 Noah Tall, 5 Silke Weber, 6 Paddy Doyle, 7 Graham Garner, 8 Robert Land (Rob). |
| `LAND_WHERE` | Province → the regions it may develop as new land: 1 `nS`, 2 and 3 `n`, 4 and 5 `S`, 6 `S8`, 7 `8`. |
| `ROLE` | Seat → role: Emperor, Official, Gentry, Scholar, Silk/Rice/Wheat Peasant, Warlord. |
| `REALIA` | Seat → the realia native to it: 2 `CH`, 3 `LD`, 4 `BB`, 5 `DJ`, 6 `WB`, 7 `VA`. |
| `NEVER` | Seat → the realia type that seat's objective never asks for: 2 `DJ`, 3 `WB`, 4 `VA`, 5 `CH`, 6 `BB`, 7 `LD`. At 4–5 players each province also starts holding two of these. |
| `RNAME` | Realia code → name: Customs House, Land Deed Scroll, Bamboo Brush, Dragon Jar, Wooden Bowl, Vase. |
| `CONS` | Seat → consumption at base population: 60 for Province 1, 20 for Province 8, 40 for the rest. |
| `HARV` | Seat → harvest by quality: `{"good": 100, "avg": 75, "bad": 50}`, or 40/30/20 for Province 8. |
| `DISASTERS` | Seat → its three personal disasters in booklet order (see [Disasters](#disasters)). |
| `PILE_START` | 2,500 — the value of the physical Harvest Pile. |
| `PW_BONUS` | The water works' bonuses: `irr2` → Province 2 +10, `res3` → Province 3 +20, `res7` → Province 7 +20. |
| `PALACES` | `("Summer Palace", "Winter Palace", "Marble Pagoda")` — the Emperor's three buildings. |
| `CUTOUT` | Work key → `(province, size, name)`: `irr2` 1 × 2, `res3` 2 × 3, `res7` 2 × 2. |
| `GRID`, `ROWS`, `COLS` | The board from `../map.json`: 22 strings of 30 characters (see [The board](#the-board)). |
| `RIVERS`, `WALL_LINKS`, `CANAL_SECTIONS` | The rivers, the twelve Wall links (by the province they stand above) and the eight canal sections (by province), as paths in grid units, from `map.json`. |
| `UNDEVELOPED` | `"8n"` — the regions where the Warlord's army may start. |

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
| `pw_at` | `{key: [square]}` | The squares each palace and cut-out stands on. |
| `raids` | `{seat: n}` | Squares raided in each province. |
| `board` | `{square: {...}}` | Realia and raid markers on each square (see [The board](#the-board)). |
| `land` | `{square: seat}` | New harvest squares and the province that bought each. |
| `SOLDIERS` | `{id: {...}}` | Every soldier in play: `side` (`"W"` for the Warlord's, `"B"` for bought), `owner` (player id), `sq`, `home` (the province it was bought in), `moved` (the round it last moved). |
| `ARMY` | int | The Warlord's starting soldiers: 4 at eight players, 2 at five or six, 0 with no Warlord. |
| `NORAID` | `{round: {seat}}` | Provinces the Warlord's disaster forbids him to raid that round. |
| `MULT` | float | The population multiple: 1, 1.5, 2, 3, … |
| `CUR_ROUND` | int | The round in progress; 0 is Setup. |
| `CUR_Q` | `{seat: "good"/"avg"/"bad"}` | This round's harvest quality. |
| `CUR_INC`, `CUR_HARV` | `{seat: float}` | This round's income and gross harvest, set by `harvest()`. |
| `warlord_got` | `{player: code or palace}` | The Warlord's objective so far: what he has raided from whom. |
| `ENTRIES`, `ROUNDS` | lists | The transcript and the round index. |

## Setup and rounds

### `setup(active, key, title, subtitle, blurb, short="")`

Start a game. Resets all state. The table starts empty: no grain dealt, no stock out of the box, no soldiers on the board. The Setup round does those.

- `active` — the seats in play, e.g. `[1,2,3,4]`.
- `key` — the game's id in the page address (`#key`).
- `title`, `subtitle`, `short` — the game-selector button; `short` replaces `subtitle` on phones.
- `blurb` — the paragraph under the page header.

### `R(n, title, card=None, card_text=None)`

Start round `n`. The population cards obey their own caps: a doubling takes effect at most twice and never past ×6, the increase by half once; past that the card is only a good harvest. Rounds go 0, 1, 2, … in order; 0 is the Setup round, shown as the Setup tab. Applies any bonuses pending from last round's works, then draws `card` — a key in `CARDS` — setting `CUR_Q` from the card's harvest and multiplying `MULT` for a population card. A card already drawn this game raises an error. Starting round 1 raises an error if the Setup round hasn't dealt the grain, taken the stock and placed the Warlord's army.

For rounds 0 and 1 pass `card=None` and the text to show as `card_text`: for Setup, a line about the table; for round 1, that the 60 is the first harvest. Records a round marker (not an entry).

### `deal_grain(text, hover=None)`

Setup only. The Harvest Pile deals every player 60 (Section 4).

### `take_stock(text, hover=None)`

Setup only. Each realia province takes its starting stock out of the box: at 4–5 players one of its own and two of its `NEVER` type; at 6, two of its own; at 7 or more, four of its own. The stock waits beside the board until it's auctioned (Note 10).

### `place_army(at, text, hover=None)`

Setup only. The Warlord stands his soldiers on undeveloped land. `at` is `{id: square}` with ids `W1`, `W2`, … — exactly one per soldier — and every square must be Warlord's territory (`8`) or the strip below the Wall (`n`).

## Recording entries

### `act(text, hover=None, deltas=None, map_hl=None, pile_delta=0, big=False, moves=None)`

A game event — a bold, clickable line.

- `deltas` — `{player: change}`. Applied before the snapshot.
- `pile_delta` — change to the Harvest Pile.
- `map_hl` — seats to highlight on the board.
- `big` — style the line as a turning point (seat changes use this).
- `moves` — `[[from, to, side]]` soldier steps to draw as arrows. `march` and `troops` fill this in; scripts rarely need it.

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

### `build(name, cost, split, wall=None, canal=None, key=None, hover=None, text=None, at=None)`

One public-works project.

- `split` — `{seat: amount}`; must sum to `cost`.
- `key` — for single works: `"Summer Palace"`, `"Winter Palace"`, `"Marble Pagoda"`, `"irr2"`, `"res3"`, `"res7"`.
- `at` — where a single work stands. A palace takes one square of Province 1: `at="H24"`. A cut-out takes a rectangle of its own province, written corner to corner: `at="R14:S15"`. Its size must match `CUTOUT` (either way round). Neither may cover a square holding realia or another work.
- `wall` — `{seat: links}` built above provinces 1, 2 or 3, at most four each. Links are drawn in the order printed on the map.
- `canal` — `{seat: sections}` built in provinces 1, 4, 5 or 6, at most two each. Each section adds 10 to that province's harvest from next round.
- `text` — replaces "Public works: *name* — *cost* paid."

Use the names `"Province 2 Irrigation System"`, `"Province 3 Reservoir"` and `"Province 7 Reservoir"`. The engine does **not** check prerequisites or the one-project-per-round rule.

### `buy_land(seat, squares, split, text, hover=None)`

Province `seat` buys new harvest squares from the Harvest Pile (Section 13): 20 each, any number, in the Public Works step, alongside the round's one project. `split` is `{seat: amount}` summing to 20 per square, and the Emperor must pay some part of every province's purchase. The engine refuses it before the population has doubled, on the strip below the Wall before all four links above the province stand (Provinces 1, 2 and 3), on a region the province's booklet doesn't name (`LAND_WHERE`), or on a square that doesn't touch the province or land it has already bought. Each square adds 20 to the province's harvest from the next round, and becomes part of the province: a Warlord soldier stepping onto it raids it.

### `owed()`, `built_count(name)`, `all_built()`

`owed()` lists `[name, count, cost each]` for every work owed at this table: the three palaces, four Wall links per occupied province among 1–3, two canal sections per occupied province among 1, 4, 5 and 6, and each irrigation system or reservoir whose province is occupied. `built_count(name)` counts what's built; `all_built()` is true when everything owed stands.

## Realia and auctions

### `lot(sell, typ, ladder, hover=None, at=None)`

Auction one piece of `typ` from seat `sell`'s stock. `ladder` is a list of `B(...)` bids; the last numeric bid wins. The winner pays the price, the seller receives a quarter rounded down to the half million (`pay_down`), the rest goes to the pile, and the piece is placed at once on `at`, a square of the winner's province (Note 10). `at` is required, and the hover should say why the winner chose it. The engine refuses a square outside the winner's province, a square already holding realia, a raided square, or one under a palace or cut-out; it also refuses a lot the seller has no stock for, and a winning bid by the seller or the Emperor. A commission note is appended to `hover`.

### Running out of grain (Note 7)

A payment that would take a player below zero must first be covered by selling realia back to the Harvest Pile. Every payment the engine makes checks this: if the player would end in debt while still holding a piece, the build stops and names them. Grain may then go negative; that's a debt, and anything the player receives pays it down.

- `sell_back(player, codes, text, hover=None)` — the player sells those pieces back at 2 each. They come off the board into `pile_stock`. Sell enough to cover the coming payment, or everything; the hover says which pieces and why.
- `lot(PILE, typ, ladder, ...)` — the Harvest Pile auctions a piece it holds (`PILE` is 0). The whole price goes to the pile. Run the pile's lots after the provinces' lots at the next auction.
- `act(..., deal=True)` — marks the payments in an act as voluntary: a trade, a bribe, a gift. A payer in debt, or one paying more than they hold, is refused. Leave it off for payments owed (levies, card effects).
- A bid, a share of a public work and a soldier purchase are all voluntary: each is refused from a player in debt or beyond their grain.

### `B(seat, amt, text=None, th=None)`

One bid. `amt=None` is a pass. `text` defaults to the amount spelled out ("Twenty-two.") or "Out." for a pass. `th` is the bidder's hover; a plain string is attributed to the bidder.

### `give(frm, to, typ, at)`

Use `act(..., deal=True)` for the grain side of a trade, so the debt guard applies.

Move one piece between **players** for a private trade: it's lifted from its square and placed at once on `at` in the new owner's province. Record the grain with a separate `act(..., deltas)` after it.

### `need_for(seat)`

The realia codes the player in `seat` must collect. At 4–5 players: every type except the seat's own and its `NEVER` type. At 6: one native to each other occupied realia province. At 7 or more: every type except its own.

### `home(code)`

Where a returned piece goes: its native province, or, if that province is empty, the province that started the game holding it (rulebook Note 12).

## Seat changes

### `swap(a, b, note, hover=None, draw=60, check=True, at=None)`

The player in seat `a` replaces the player in seat `b`.

With `check=True` (the default) it first asserts that the mover holds everything `need_for(a)` requires, has at least 20 grain, and may move to `b`: only seats 2, 3, 4 and 8 may take Province 1; a peasant may only take 2–7. Use `check=False` for a Chaos acclamation. It also refuses if the displaced player owns bought soldiers, which no ruling covers yet.

Then: pieces native to `b` held by the mover return to `b`'s stock; if `b` is the throne, all the mover's pieces return home; the displaced player returns everything; the mover takes all of the displaced player's grain, debt included; the displaced player draws `draw` (60) from the pile, or what's left if the pile is lower; the seats swap; the mover's remaining pieces go on squares of the new province, given by `at` as `{code: square}` or `{code: [squares]}`, one per piece. Bought soldiers stay with their owner and where they stand. Records a `big` act.

## Soldiers

Every soldier stands on a square and moves at most one square a round, diagonals included (Section 14, Note 16). The Warlord's soldiers are `W1`, `W2`, …; a bought soldier is named after its buyer: `Reina1`, `Reina2`, `Paddy1`. No soldier may enter the sea.

### `march(moves, text=None, hover=None, take=None)`

The Warlord moves. `moves` is `{soldier: square}`, each one square from where it stands; any soldier left out stands still. Call `march` more than once in a round to narrate soldiers separately, but each soldier moves once per round, and all of them before any province's soldiers move (`troops`).

For each step, in order:

1. **Capture.** A step onto a square holding a bought soldier captures it, and is only allowed horizontally or vertically.
2. **Tolls.** 5 for each river, built Wall link, built canal section or cut-out the step crosses (see `tolls()`), paid to the province concerned.
3. **Raid.** A step onto an un-raided square of an occupied province raids it: 5 from that province's player, or 10 in Province 1; on a palace square, the Emperor pays the structure's cost, 20, and the palace counts toward the Warlord's objective. To take the realia on the square instead, pass `take={soldier: (code, square)}`: the piece moves to the Warlord, onto that square of his territory, and counts toward his objective. A raid the Warlord's disaster forbids this round raises an error. A step onto undeveloped land, a raided square or a square of an empty province raids nothing.

Records one act with every grain change, the moves drawn as arrows, and a note of each capture, toll and raid appended to the hover.

### `sell_soldiers(buys, text, hover=None)`

`buys` is `[(seat, square), ...]`. Each buyer pays the Warlord 20 for a soldier that stands on that square of the buyer's own province; he keeps 5 of each and 15 goes to the pile. The square must not hold a Warlord soldier or another player's soldier.

### `troops(moves, text, hover=None)`

Bought soldiers move, after the Warlord's (Section 5). `moves` is `{soldier: square}`, one square each. A soldier can't move until the Warlord has raided the province it was bought in. A step onto a Warlord soldier captures it, horizontally or vertically only; a step onto another player's soldier is refused.

### `rob_n()`

The Warlord's soldiers still in play.

### `tolls(a, b)`

The fees a Warlord soldier would owe for the step `a → b`, as `[(province, what was crossed)]`. A step crosses a river, Wall link or canal section when the line between the two squares' centres cuts it; it crosses a cut-out when it lands on one of its squares. Rivers pay the province stepped into, and nothing when that's undeveloped land; works pay the province they belong to. An unoccupied province is owed nothing. `march` calls this; scripts can call it to plan a route.

## Disasters

### `disaster(seat, text, hover=None)`

Play the next disaster in `seat`'s booklet; after the third, it starts again. The amount is computed from the booklet:

| Kind | Amount |
|---|---|
| `fixed` | The printed amount |
| `frac_income` | A fraction of this round's income (Officials, Rice and Wheat Peasants) |
| `frac_harvest` | A fraction of this round's gross harvest (Silk Peasant) |
| `frac_grain` | A fraction of the player's grain (Gentry, Scholar, Warlord) |
| `noraid` | Nothing paid |

The amount goes to the Harvest Pile, and the line reads "*Name*'s disaster #*n*: *text* — *amount* to the Harvest Pile." Write `text` as the event itself; the engine adds the number and the cost.

The Warlord's first disaster forbids raids on Provinces 5–7 this round, and his second forbids raids anywhere this round; `march` refuses a raid that breaks either. His soldiers may still walk onto squares that don't raid.

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
| `rc(square)`, `sqname(r, c)` | Square name ↔ (row, column) from 0. `rc` refuses a square off the board. |
| `region(square)` | The square's character in `GRID`. |
| `prov(square)` | The province 1–7 a square is in, or `None`. |
| `owner(square)` | The province a square belongs to, counting new land. |
| `squares_of(p)` | A province's own squares and the new land it has bought. |
| `squares(p)` | Every square of province (or region character) `p`. |
| `dist(a, b)` | Rounds a soldier needs to walk from `a` to `b`. |

## The board

`GRID` is `map.json`'s grid: 22 rows (A–V) of 30 columns (1–30). Each square is one character:

| Character | Region |
|---|---|
| `1`–`7` | A province |
| `8` | The Warlord's territory |
| `n` | The strip below the Great Wall |
| `B` | Beyond the Wall |
| `S` | The sea |

Each square in `board` (keyed by its name) may hold:

| Key | Meaning |
|---|---|
| `realia`, `owner` | A piece and the player who owns it |
| `raid` | The square has been raided and can never be raided again |

Soldiers live in `SOLDIERS`, works in `pw` and `pw_at`. The Wall and the Canal have printed places on the map, so the board needs only their counts; palaces and cut-outs stand where `build(at=...)` put them.

`trace.py game.py --board N` prints the board after entry `N` as text, with every soldier and piece listed — the quickest way to plan a march.

## Ending

### `export(results_note, epilogue)`

Score the game and return the dictionary the page uses (see [`page-format.md`](page-format.md#the-data-format)). Assign it to `RESULT`.

Scoring follows Section 18: a player who finishes in a lower-numbered province than the one they drew has won, a higher-numbered one has lost, the same one has held — except that an Emperor still on the throne has won. `results_note` is one sentence above the results table; `epilogue` is a list of paragraphs below it.

## The cards

`cards.py` defines `CARDS`, a dictionary of the twenty I Ching cards. Each entry has:

- `text` — the card's wording, from the reworded deck in `../i-ching.json`;
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

The engine applies the harvest and the population change. It does not enforce the cards' own caps ("if the population has already doubled twice, collect a good harvest instead"): drawing a third doubling card or a second half card would multiply the population anyway. Don't draw them, or the population will pass the 600-million ceiling the cards set.
