# Writing a game

A game script is a sequence of calls in play order. The engine keeps the books; the script decides what each player does and says. This guide covers how a script is put together, walks through one round, and ends with the voice conventions and a checklist.

- [How a script runs](#how-a-script-runs)
- [Seats and players](#seats-and-players)
- [Setting up](#setting-up)
- [The board](#the-board)
- [A round, in order](#a-round-in-order)
- [The three kinds of entry](#the-three-kinds-of-entry)
- [Auctions](#auctions)
- [Running out of grain](#running-out-of-grain)
- [Private trades](#private-trades)
- [Changing seats](#changing-seats)
- [Soldiers](#soldiers)
- [Card effects the engine doesn't apply](#card-effects-the-engine-doesnt-apply)
- [Ending the game](#ending-the-game)
- [A worked round](#a-worked-round)
- [Voice: dialogue and thoughts](#voice-dialogue-and-thoughts)
- [Checklist](#checklist)
- [Adding a game](#adding-a-game)

## How a script runs

`build.py` runs each game in a fresh, empty namespace: first `cards.py`, then `engine.py`, then the game script. Every engine function and constant is therefore a plain global — there are no imports in a game script. When the script finishes it must have assigned `RESULT = export(...)`; `build.py` collects the three results and writes them into the page.

Each call that records something — `act`, `say`, `lot`, the helpers built on them — appends one **entry** to the transcript and takes a full **snapshot** of the game state at that moment. Clicking an entry on the page shows that snapshot: the board, the grain, the objectives and the works. This has one consequence that matters while writing:

> **Change the state first, then record it.** A snapshot is taken when the entry is recorded. If you move a piece with `give()` *after* the `act()` that announces it, the page shows the old position on that line.

## Seats and players

Two kinds of number identify people:

- A **seat** is a province, 1–8. Rules attach to seats: Province 2 collects the tax, Province 8 raids.
- A **player id** is the seat that player drew at setup — Reina is player 1, Clark player 2, and so on. Grain and realia attach to players, because players move between seats.

At the start of every game the two are the same. After the first seat change they aren't. `pid(seat)` gives the player sitting in a seat; `sid(player)` gives the seat a player is in.

Most functions take **seats** — `taxes`, `build`, `lot`, `disaster`, `swap`, `sell_soldiers`. Three things take **player ids**, because they are about people rather than provinces:

- the `deltas` dictionary of `act()` (who gains or loses grain),
- `give(frm, to, typ)` (who hands a piece to whom),
- the keys of `grain` and `held`.

When a delta is about a province rather than a person, write it with `pid()` so it stays right after seats change:

```python
# Year 8 of the full game: whoever holds Province 2 pays the Emperor half its irrigation bonus.
act("Noah's irrigation pays Reina 5.", hover, {pid(2): -5, pid(1): 5})
```

Writing `{2: -5, 1: 5}` there would charge Clark — player 2 — who had already been moved to Province 4.

## Setting up

```python
setup([1,5,6,7,8], "peasant", "The peasant game",
      "Five players · nine years · everything gets built",
      "A second evening, same friends. ...",
      short="5 players · 9 years")
```

| Argument | Meaning |
|---|---|
| `active` | The seats in play. The player count decides starting realia, objectives and the size of the Warlord's army. |
| `key` | The game's id in the page address: `playthrough.html#peasant` opens this game. |
| `title`, `subtitle`, `short` | The game-selector button: title, the full subtitle, and the short subtitle used on phones. |
| `blurb` | The paragraph under the header. |
| `cast` | Optional `{seat: short name}`: who drew which booklet. Leave it out and everyone draws the seat they drew on the first evening, as in the first three games; games 4 and 5 deal them afresh. |

`setup` leaves the table empty. **The Setup round** (round 0, the Setup tab on the page) is a short scene, usually 8–12 entries, that follows rulebook Section 4 and Appendix A for the player count. Three calls do the bookkeeping, and the engine won't start Round One until they have run:

```python
R(0, "Appointments", None, "Five players: the Emperor, the three peasants and the Warlord ...")
act("Five booklets go in the box ... they land in the same hands as last week.", hover)
deal_grain("Paddy deals 60 to each player from the Harvest Pile.", hover)
take_stock("Silke, Paddy and Graham take their realia out of the box ... It waits beside the board.", hover)
act("Graham cuts out the Province 7 Reservoir: a paper square two by two ...", hover)
place_army({"W1":"O18", "W2":"E21"}, "Robert Land stands his two soldiers on undeveloped land ...", hover)
```

Around them, write the rest of Section 4 as the table lives it: the booklets drawn, the Gentry (or an appointee) setting out the Harvest Pile, the Scholar (or an appointee) shuffling the I Ching, and the cut-outs made for each water work owed. Give each game its own flavour: the peasant game's Setup is Reina handing out the missing officers' jobs; the short game's is the table agreeing to stop after eight rounds.

**Round one has no card.** The 60 grain is the first harvest, so there's no `harvest()` call; tax is levied on that 60. Tell the engine so before calling `taxes()`:

```python
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s: 60 for s in ACTIVE})
```

## The board

Every piece in the game stands on a real square of `../map.json`, named like `H12`: row letter A–V, column 1–30. **Placement is a choice**, and the script makes it:

- A bought or traded piece of realia goes on a square of the buyer's province at once (Note 10): `lot(..., at="Q16")`, `give(..., at="P15")`, `swap(..., at={"CH": "L25", ...})`.
- The Emperor's palaces go on squares of Province 1: `build(..., key="Winter Palace", at="H24")`.
- A cut-out covers a rectangle of its province at its suggested size: `build(..., key="res7", at="R14:S15")` for the 2 × 2 Province 7 reservoir.
- The Wall and the Canal have printed places on the map; they need no `at`.

**The hover says why.** A player keeping a precious piece deep inside their province, away from the frontier and from where the Warlord's soldiers stand, is thinking about geography — so let them think it out loud: "Q16, in the middle of Province 7. Two squares from the desert, which in my province is as deep as it gets." The Warlord thinks about the same geography from the other side. With no Warlord at the table, placement still gets a reason, even if the reason is that it looks well from the player's chair.

To see the board while writing, run `python3 playthrough-sim/trace.py game2_peasant.py --board 57`: it prints every square after entry 57, with each soldier and piece listed. `dist(a, b)` says how many rounds a soldier needs between two squares, and `tolls(a, b)` what a step would cost the Warlord.

## A round, in order

The order below follows the can's Order of Play, with rents, salaries and soldiers placed where the booklets put them (rulebook Section 5). Skip any step that doesn't apply.

```python
R(4, "The population increases", "half1")   # 1. draw the card: harvest quality, population
harvest()                                    # 2. pay each province its income
rents()                                      # 3. peasants pay the Gentry (no-op with no Gentry)
disaster(6, "the buffalo breaks its leg.")   #    if the card calls for disasters
taxes(.50)                                   # 4–5. the Emperor's rate; negative income pays nothing
build("Grand Canal in Province 6 — 2 sections", 80, {1: 80}, canal={6: 2})   # 6. one project
lot(5, "DJ", [...], at="Q24"); lot(6, "BB", [...], at="R13")   # 7. auctions, in seller order
march({"W1": "O19"})                        #    the Warlord moves instead of auctioning
troops({"Reina1": "K24"}, "...")             # 8. provinces' soldiers, after the Warlord
salaries()                                   # 9. Official and Scholar, 5 each
```

`R(n, title, card)` starts a round. The `card` is a key from `cards.py` — `"half1"`, `"dribble2"`, `"heaven"` — and sets this round's harvest quality for every province and, for population cards, the population multiple. Each card can be drawn once per game; the engine refuses a repeat. The card's full text appears in the round header on the page.

`harvest()` pays every active province `harvest + bonus − consumption × population` from the Harvest Pile. A negative income is paid *into* the pile.

`taxes(rate)` charges each province (except the Emperor's, and the Warlord's unless you pass `skip=()`) `rate × income`, and pays it to whoever holds Province 1. With no Official at the table, pass `collector="Reina collects the tax herself"` to change the wording.

`build(name, cost, split, ...)` records one public work. `split` is `{seat: amount}` and must add up to `cost`. Pass what was built — `key="Summer Palace"`, `key="res7"`, `wall={1: 2}`, `canal={5: 2}` — so the board and the works panel update and the bonus starts next round. The rulebook allows one project per round, and a project may be several sections of the same work (Note 13).

`salaries()` pays the Official and Scholar 5 each, at the end of the round. In a game without them, pass appointees: `salaries({7: 5}, text="Reina pays Graham 5.")`.

## The three kinds of entry

| Call | Shown as | Changes state? | Use it for |
|---|---|---|---|
| `act(text, hover, deltas)` | A bold, clickable line | Yes, if you pass `deltas` | Anything that happens in the game: a payment, a trade, an announcement |
| `say(who, text, hover)` | A smaller, indented line in quotes | Never | Table talk — what a player says out loud |
| `lot(sell, typ, ladder)` | A bold line that opens into its bids | Yes | One auction lot |

The engine's helpers — `harvest`, `taxes`, `build`, `march`, `swap` and the rest — record `act` entries for you.

Every entry can carry a **hover**: the thoughts behind it. A hover is one of:

- a plain string, attributed to the speaker of a `say`, or unattributed on an `act`;
- a string starting with a name and a colon — `"Rob: I keep five of every twenty."` — attributed to that player;
- a multi-voice note built with `TH`:

```python
say("Rob", "Business.", TH(
    ("Rob",    "Honestly? Yes. But I've also just blocked the only two players who could climb past me."),
    ("Rich",   "And there goes mine as well. He's ended two of us with one bid."),
))
```

On the page a single voice is labelled "Rob is thinking"; several voices are labelled "At the table".

## Auctions

A lot is one piece of realia from one province's stock, with the whole bidding ladder:

```python
# Year 4 of the full game: Graham (seat 7) sells the last Vase.
lot(7, "VA", [
    B(5, 8),                                       # Silke bids 8; the text defaults to "Eight."
    B(4, 10),                                      # Noah bids 10
    B(5, 12, "Twelve."),
    B(8, 20, "Twenty. For a pot.", TH(("Rob", "..."), ("Graham", "..."))),
    B(4, None, "He can keep it for now.", "I'll buy it off him later."),    # a pass
    B(5, None, "I can't go higher.", "Fifty-odd left and a soldier to buy."),
], hover="Rob puts it on K4, next to his Bowl. Two pieces in the desert, and neither is any use to him.",
   at="K4")
```

Rob wins at 20: his is the last numeric bid, and the piece goes straight onto K4.

`lot(sell, typ, ladder, hover=None, at=...)`:

- `sell` is the **seat** selling. Each seat must auction one piece a round until its stock is empty; the seller chooses which.
- `typ` is the realia code: `CH` Customs House, `LD` Land Deed Scroll, `BB` Bamboo Brush, `DJ` Dragon Jar, `WB` Wooden Bowl, `VA` Vase.
- Each `B(seat, amount, text=None, thought=None)` is one bid. `amount=None` is a pass. The **last numeric bid wins.**
- `at` is the square in the winner's province where they put the piece; the lot's `hover` is the place to say why.

The engine moves the piece to the winner and onto that square, charges the winner, pays the seller a quarter as commission, sends the rest to the Harvest Pile, and adds a commission note to the hover. It refuses a winning bid by the seller or the Emperor.

Two things the engine doesn't check, so check them yourself:

- **Bidders should want the piece.** Look up what each seat needs (`need_for(seat)`, or the objectives panel on the page) and what they already hold. A player bidding on a piece they already own is the most common slip.
- **Bidders need the grain.** `trace.py` shows each player's grain before the lot.

When nobody bids, don't call `lot` — record it as an `act` ("Nobody bids on the Brush.") and leave the piece in stock.

## Running out of grain

When a payment would take a player below zero, they must first sell realia back to the Harvest Pile (rulebook Note 7). Write it before the payment, with the player choosing the pieces:

```python
# Year 11 of the full game: the drought harvest is about to sink Clark.
sell_back(2, ["BB"], "Clark sells his Bamboo Brush back to the Harvest Pile for 2. ...", hover)
harvest()
```

If they're still short, their grain goes negative. That's a debt: they can't bid, deal, pay toward a public work, buy soldiers or change seats until it's paid. At the next auction, after the provinces' lots, the pile auctions what it bought back with `lot(PILE, ...)`, or the table lets it sit ("Nobody bids"). Debt is pressure, not decoration: let it show in who can't bid and who sells what.

## Private trades

The rules allow trading at any time. A trade is a `give()` for the piece and an `act()` for the grain — in that order, so the snapshot shows the piece moved:

```python
give(8, 7, "BB", at="P15")             # player ids: Rob hands Graham the Brush, which goes on P15
act("Graham Garner buys back his Bamboo Brush from Robert Land for 35, and puts it on P15.", hover,
    {pid(7): -35, pid(8): 35}, map_hl=[7, 8], deal=True)
```

## Changing seats

```python
swap(7, 5, "Graham Garner declares a complete set and replaces Silke Weber. ...", hover,
     at={"CH": "O26", "BB": "P25", "WB": "P26"})
```

`swap(a, b, note, hover, at=...)` moves the player in seat `a` into seat `b`. Before doing anything it checks that the player in seat `a` holds every piece seat `a` requires, has 20 grain in hand, and is allowed to move to seat `b` (rulebook Section 11 and Note 11). If any check fails, the build stops with the reason.

It then does what the booklets say: the mover hands back pieces native to the new seat (and everything, if becoming Emperor); the displaced player hands back everything; the mover takes all of the displaced player's grain; the displaced player draws 60 from the Harvest Pile. The mover's remaining pieces go onto the squares in `at`, one per piece, in the new province. Bought soldiers stay with the player who bought them, where they stand.

A Chaos acclamation isn't a completed set, so it skips the checks: `swap(7, 1, note, hover, check=False)`.

After a swap, seat numbers and player ids diverge. Re-read [Seats and players](#seats-and-players) before writing any `act` deltas.

## Soldiers

Every soldier stands on a square and moves at most one square a round, in any direction, diagonals included (Section 14, Note 16). The engine tracks them all and refuses an illegal move, the way it refuses an illegal seat change.

| Call | What happens |
|---|---|
| `place_army({"W1": sq, ...}, text, hover)` | Setup: the Warlord's soldiers stand on undeveloped land. Four at eight players, two at five or six. |
| `march({"W1": sq, ...}, text, hover, take=None)` | The Warlord moves. Each listed soldier steps one square; a step onto an un-raided square of an occupied province raids it. |
| `sell_soldiers([(seat, sq), ...], text, hover)` | Each buyer pays 20 for a soldier standing on that square of their own province; the Warlord keeps 5. |
| `troops({"Reina1": sq, ...}, text, hover)` | Bought soldiers move, after the Warlord's. |

A **raid** is what happens when a Warlord soldier steps onto an un-raided square of an occupied province, and it isn't optional: plan the route so the soldier raids where the Warlord means to. The tribute is 5, or 10 in Province 1; a palace square costs the Emperor 20 and counts toward the Warlord's objective; `take={"W1": ("BB", "K4")}` takes the realia on the square instead, and the Warlord puts it on K4 in his own territory. A soldier that steps onto undeveloped land, a raided square or a square of an empty province raids nothing, so a march can take years to reach anywhere worth raiding. That's the point.

**Tolls** are computed: 5 for each river, Wall link, canal section or cut-out a step crosses, paid to the province. They can make a route a wash — the southern river runs right along the border of Provinces 4 and 5, so a soldier walking it pays at almost every step. Let the players notice.

**A disaster that stops raids** ("no raids on Provinces 5, 6 or 7", "no raids this year") makes `march` refuse those raids. The soldiers may still walk.

**Bought soldiers** start on a square of the buyer's province and can't move until the Warlord has raided that province. Then they move one square a round, after the Warlord's. A soldier captures by stepping onto an enemy soldier horizontally or vertically, never diagonally. That gives the board its tactics: **the Warlord always moves first**, so a bought soldier that ends a round level with a Warlord soldier (straight beside it) can be captured, and one that ends at an angle can't. A defender guards the square the Warlord needs to step onto, not the square he's on. Standing a bought soldier on a piece of realia means the Warlord can only take it by capturing first, straight on.

`trace.py --board N` and `dist()` are the tools for planning a march; write the route before the dialogue, and let the hovers talk about it.

## Card effects the engine doesn't apply

`R()` applies a card's harvest quality and population change. Everything else on a card is the script's job, written as an `act` with deltas:

| Card | What to script |
|---|---|
| `careless`, `goodevil`, `repairs`, `canal`, `breach` | `disaster(seat, ...)` for each province the card names that is in play |
| `utility` | 2 from every province and 2 more from each with a public work, to the Emperor |
| `share` | Each province with a public work pays the Emperor half its bonus |
| `chest` | The Emperor pays every other player 2 |
| `repairs` | 2 to the Harvest Pile from each named province in play (`pile_delta`) |
| `breach` | 5 each from Provinces 1–3 to repair walls, or 2 each to the pile if no wall has been built |
| `canal` | Unfinished canal sections are destroyed; completed provinces pay the Emperor 2 |

Cards name provinces, not players, and some named provinces may be empty. Say so in the dialogue: the card reader in the peasant game does the "nobody's in 2 or 4" arithmetic out loud, which is what a real table does.

## Ending the game

A game ends when every owed public work is built (`all_built()` is true), when the table collapses into revolt and Chaos, or — in the short game — after the agreed number of rounds. End the script with:

```python
RESULT = export(
    "One sentence on how the game ended and how it is scored.",
    ["Epilogue paragraph one.", "Paragraph two.", "Paragraph three."])
```

`export` scores every player by Section 18 — a lower-numbered province than they drew is a win, a higher one a loss, the same one held, and an Emperor still on the throne has won — and packages the game for the page.

## A worked round

Year 2 of the peasant game, trimmed. The comments explain each choice.

```python
R(2, "Fortune and misfortune", "goodevil")              # good harvest; P2, 4, 6, 8 play disasters
say("Graham", "Good harvest for all. ... and 2 and 4 are empty, so that's Paddy and Rob.",
    TH(("Graham", "First card I read and I've already had to do the empty-province arithmetic out loud."),
       ("Paddy",  "Of course it's me.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")   # Paddy is the appointed banker
disaster(6, "the only water buffalo breaks its leg in the middle of planting.",
         TH(("Paddy", "Banker for one round and the first thing I pay out of my own pocket is a buffalo.")))
disaster(8, "wounded in the legs. No raids on Provinces 5, 6 or 7 this year.",   # march will refuse a raid there
         TH(("Rob",   "So the soldier next to Graham's Brush stands still for a year ..."),
            ("Reina", "Which means his only raid lands on me, at ten.")))
taxes(.35, collector="Reina collects the tax herself")         # no Official at this table
build("Province 7 Reservoir", 60, {1: 60}, key="res7", at="R14:S15",   # +20 for P7 from next round
      hover=TH(("Graham", "R14 to S15, away from the notch. Every time his soldier steps onto it he pays me five.")))
lot(5, "CH", [B(7, 8, "Eight.", "Paddy had the first; this one's mine.")],
    hover=TH(("Graham", "S13, the far corner from his soldier. Four squares from P17.")), at="S13")
march({"W2": "G23"}, "Robert Land's northern soldier steps to G23 and raids Province 1 ...")   # 10 from Reina
salaries({7: 5}, text="Reina pays Graham 5.")                   # the appointed card reader
```

Run `python3 playthrough-sim/trace.py game2_peasant.py` and every one of those lines appears with each player's grain afterwards, and each march with the soldiers' squares.

## Voice: dialogue and thoughts

The page has two registers, and keeping them apart is most of what makes it read like a table rather than a report.

**Dialogue (`say`) is roleplay.** Players speak in character, as their province, inside the fiction: "Majesty, the reservoir." "Twenty. For a pot." It can be playful, pointed or flat, but it's something a person would say across a table.

**Thoughts (hovers) are the player, not the character.** The people behind the pieces know they're playing a board game. They reason about the rules, count pieces, quote booklets, notice what the cards do, and enjoy the bit while doing the maths — the way a strategic tabletop player who also likes roleplay thinks. Give each player their own way of thinking:

- **Reina** manages the table: plans years ahead, knows when she's walking into a revolt clause.
- **Clark** is gleeful about leverage and keeps a paper trail of grievances.
- **Rich** fawns out loud and calculates underneath; keeps promises to the letter.
- **Noah** is honest to a fault and the one who says the arithmetic out loud.
- **Silke** gets sharper as she gets squeezed.
- **Paddy** is earnest and a little surprised to be winning.
- **Graham** gets quieter and more precise as the grievance builds.
- **Rob** has realised he's the villain and is having a wonderful time.

**Use several voices.** The best notes are a move plus the reactions of the people it lands on. Thoughts can be one word.

**Numbers must match the ledger.** If a thought says "I've got sixty," the trace must show about sixty at that line. "Sixty-odd", "about eight" and "a quarter of everything I have" are fine; a wrong figure isn't. The ledger changes when anything earlier changes, so re-check downstream lines after every edit.

**Names.** The transcript uses short names (Reina, Clark, Rich, Noah, Silke, Paddy, Graham, Rob); the players table uses full names. That's automatic — just write short names in `say` and in thoughts.

**The evenings happen in order.** The same friends play game 1, then 2, 3, 4 and 5, and they remember. A player can refer to an earlier evening only if they played in it:

| Evening | Who played | Who sat out |
|---|---|---|
| 1, the full game | everyone, each in the province their name puns on | — |
| 2, the peasant game | Reina, Silke, Paddy, Graham, Rob | Clark, Rich, Noah |
| 3, the short game | Reina, Clark, Rich, Noah | Silke, Paddy, Graham, Rob |
| 4, the long game | everyone, booklets dealt afresh | — |
| 5, the six-player game | Rob, Silke, Clark, Reina, Graham, Noah | Rich, Paddy |

So in game 3 it's Clark's second time, not his third; and Rob was the Warlord on evenings 1 and 2 only.

## Checklist

Before building:

- [ ] The Setup round deals grain, takes stock and places the army, and covers the rest of Section 4 for this player count.
- [ ] Every `act` delta is keyed by player id — use `pid(seat)` for anything about a province.
- [ ] State changes (`give`, manual stock edits) come before the `act` that announces them.
- [ ] No card is drawn twice in one game.
- [ ] Disasters are played for every province the card names that is in play.
- [ ] Every placed piece has a square, and the hover says why that square.
- [ ] Every march follows a route that makes sense for the Warlord, and no bought soldier is left where he'd simply capture it.
- [ ] Prerequisites: the Winter Palace before canals in 4, 5 and 6; the Summer Palace before the Wall and the Province 1 canal.
- [ ] One public-works project per round.
- [ ] Every bidder needs the piece and can afford the bid.
- [ ] Before any payment that would sink a player, they sell back realia (`sell_back`), and voluntary payments are marked `deal=True`.
- [ ] Every number in dialogue or thoughts matches the trace at that line, including distances on the board ("three squares from his soldier").

After building:

- [ ] `build.py` finishes without an error.
- [ ] Click through the years you changed; check the board, the objectives panel and the works panel.

## Adding a game

1. Copy the shortest script, `game3_short.py`, to `gameN_something.py`.
2. Change the `setup` call: seats in play, a new `key`, titles and blurb, and a `cast` if the booklets fall differently this evening.
3. Write its Setup round.
4. Add the file name to `GAMES` in `build.py`.
5. Write it, tracing as you go. Record any new ruling in `../../RULINGS.md`.

The page builds its game selector, tabs and panels from whatever `build.py` gives it; nothing in the template needs to change.

