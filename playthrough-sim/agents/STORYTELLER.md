# How the Storyteller runs a chapter

**Where things live.** The tools and these notes are in `playthrough-sim/agents/`. Each game has its own folder, `playthroughs/<name>/`: `game.py`, `log/`, `log.md`, `ledger.md`, `diaries/`, `narration.md`, `talk.jsonl`, `seen.json`, `bids/`, `state/`, `handoff/`, `agent-ids.md` and `seed.md`. Run every tool from the game's folder, as `python ../../playthrough-sim/agents/run.py` (likewise `briefs.py`, `geo.py`, `snapshot_setup.py`); below, `python run.py` is short for that. `rules-digest.md` and `storyteller-voice.md` are shared by every game.

Read first: the latest `handoff/chapter-N.md` (if any), `rules-digest.md`, `storyteller-voice.md`, `ledger.md`, `agent-ids.md`, then the last round's files in `log/`. Work from the game's folder.

## A chapter

A chapter is two years, named in your brief. Stop at the end of the last one. **Stop rule:** if your context passes about 450k, finish the year you're in and end the chapter there (diaries and close as usual), and tell the Director.

1. **Launch a fresh `dynasty-player` agent for every seat**, with `python briefs.py prompt <NNN> <Player> launch --menu <file>` at that player's first turn of the chapter. The launch carries the character sheet, the player's `ledger.md` entry and their diary (`diaries/<name>.md`). Add the chapter's agent ids to `agent-ids.md`.
2. **Play the years** as below.
3. **Narrate** in the voice of `storyteller-voice.md`: a chapter title, a line to open each year, and a line at each turning point. They go only into `narration.md`, under the chapter's heading, each tagged with the log number it follows. **The narrator isn't part of the game and won't appear on the playthrough page,** so never put narration in `game.py`. The script's own `act()` lines (plain events, as before) must give every say and aside the context it needs on their own. Mark each chapter's start in the script with a `# ===== CHAPTER N: <title>` comment.
4. **Diaries.** After the last round, file the closing catch-up as `event` lines, then send each player `briefs.py prompt <NNN> <Player> diary --years "Years A–B"`. It carries the catch-up as table talk and asks only for the entry (reply `diary: ...`), then run `seen all`. Append each reply, word for word, to `diaries/<name>.md` under a `## Years A–B` heading.
5. **Close:** ledger current, a snapshot per round, `log.md` rows, usage at the start and end. Then stop and report.

## Each turn

1. **State, from the engine.**
   - `python run.py` prints the ledger tail, the board and everyone's grain.
   - `python geo.py --rounds 2` prints reach and out-of-reach squares, and each piece's distance from each soldier.
   - Never work out a distance by hand.
2. **Write the prompt once.** `python briefs.py prompt <NNN> <Player> <auction|march|free|launch> ...` builds it from the engine state and from everything said since that player's last prompt. It writes `log/yearN/NNN-player-prompt.md` and prints the text; send that text unchanged with SendMessage. For a `free` decision, write only the menu in a scratch file and pass `--menu`.
   - **Every prompt opens with the player's board card** (from Chapter 2; Manish's call). `briefs.py` generates it from the engine and `geo.py`, for that player only and in the same layout every time: grain, what they hold and still need, each Warlord soldier's distance in rounds to each of their pieces and to their nearest unraided square, their squares out of reach this year and next, and whether their province has been raided (so whether soldiers they buy can move). The Warlord's card gives the objective (from the engine's raid record, the palace wildcard included at eight players) and each soldier's distance to every piece and unraided palace; the Emperor's gives the distance to each palace. Never write or edit a card by hand; the players stay tool-less, and this is how they see the board.
3. **Record the reply.**
   - Write it to `log/yearN/NNN-player-reply.md`, word for word, then `---` and your ruling.
   - Then `python briefs.py heard <NNN> <reply file>` files its say and whisper as table talk.
   - File what happened with `python briefs.py event "..."`, and any correction with `python briefs.py note "..." [--to Player]`.
4. **Legality from code.**
   - Add the move to `game.py` (say as text, aside as hover) and run `python run.py`.
   - Announce the move only after it runs clean.
   - If the engine refuses it, the move is illegal: tell the player why and give them the menu again.
5. **Check the lines against the board.** If a public line or a whisper misstates the board, the cash or the rules, file a `note` for the listeners. Bluffing about intentions isn't corrected. If an aside misstates something, log it in the ruling and state the fact plainly in that player's next prompt.

## New land, every year once it opens

From the first doubling, new land (§13) is a standing option in the Public Works step: every eligible seat (the peasants, the Scholar, the Official and Gentry once their Wall links stand, and the Emperor through `crown`) gets a `land` prompt for it each year, even when nobody has asked. It lists the squares they can buy now. Pass the Emperor's offer from the crown's year as `--offer "<what the crown pays per square>"`, so the buyer sees it. A `free` prompt in the public works step can carry a one-line reminder too (`--land`); other `free` prompts (rent, soldiers) don't. The board card already gives each player their own numbers (a square pays for itself in a year; how many they need now and after the next card). Offer it plainly and never steer: the choice, and the cost of not buying, is theirs. The pilot, the peasant game (`playthroughs/peasant-collapse/`), never bought a square and collapsed into debt.

## The table jobs, step by step

Each job is its holder's own prompt, so the upper class plays its part in the year. With the seat empty, the Emperor's appointee does it in a `free` prompt, or it's a plain `act()`.

| Step | Who | Prompt |
|---|---|---|
| 1 I Ching | Scholar | `iching`, after `R(n, card)` runs: the card text and the population counter |
| 2–3 Harvest, rent | Gentry | `rent`, after `harvest()` runs: the payout and the rent (unasked, none) |
| 4, 6, 9 Tax, works, salaries | Emperor | `crown`: the taxable incomes, the tax at each rate, every work owed with who pays and what must stand first, salaries, and new land from the first doubling |
| 5 Tax paid | Official | `collect --rate <n>`: what each owes |
| 6 New land | each eligible seat | `land` (below) |
| 7 Auctions | every bidder | `auctions` (below) |
| 8 March | Warlord | `march` |

A shared work's split, a bribe or a subsidy goes to the other party as a `free` prompt. Ask in table order and keep it moving: one prompt per player per step at most.

## Auctions, batched by year

At eight players there are up to seven lots a year (Provinces 2–7, then any pieces sold back to the pile), so each bidder gets **one prompt a year** for all of them.

- `briefs.py prompt <NNN> <Player> auctions --lots 2:CH,3:LD,4:BB,5:DJ,6:WB,7:VA` (add `0:<code>` for a pile lot) to every player but the Emperor, the Warlord included. Each replies once: for every lot, pass or a ceiling and an optional `keep from <name> up to <n>`; for their own lot, its minimum; one `if I drop out:` line.
- Put everything in one JSON file (`bids/yN.json`) and run `python briefs.py resolve bids/yN.json`. It settles the lots **in order**: a winner's grain drops and a seller's quarter is added before the next lot, and any later limit above a bidder's remaining grain is cut to it. For each lot it prints the winner, the price (one step over the runner-up's limit against the winner), each bidder's highest bid and a `lot()` ladder. Ties go by seat order.
- Then send each lot's buyer one short message, `briefs.py prompt ... place --lot <seat>:<code>[,<seat>:<code>] --price <n>[,<n>]`, asking where to put it (one message for every lot a buyer won), and play the `lot()` calls in order with those squares.
- **Live raise only for a near-tie:** the resolver prints `CLOSE` only when the winner's limit is within one step of the runner-up's and the price is 10 or more. Then send just the top two one raise-or-pass message each, covering all their close lots at once, as a `free --short` prompt (no state block: they have just seen it). Otherwise the ceilings stand.
- **Stay lean:** check each move with `run.py --quiet` (ok, the last line, the grain); print the full board only when you need it.
- Narrate each climb from the ceilings. Use each loser's say for their bid and their drop-out line for their pass. A small table may still run one lot at a time (`auction --lot ... --min ...`).

## A revolt

Run it as a short exchange, not a single round of answers (R: Calling off a revolt):
1. **The call:** the caller names the cause, and each other player agrees or doesn't. With two agreeing, call `revolt_called("...")`. **From then on play waits** (Manish, 2026-10-28): no step of the round and no seat change, a set included, until the revolt stands or is dropped. Anyone may argue, persuade, promise or deal in the meantime, and the engine refuses everything else.
2. **The answer:** with two agreeing, the Emperor gets a `free` prompt to answer: pay, cut the tax, fund land, or promise.
3. **Stand or take it back:** the caller and each backer get a `free --short` prompt with the answer, and either stand by the revolt or take it back.

It stands only with the caller and two others still behind it. If answers cross, ask the players what they meant; never decide who came first by seat order. If it fails, call `revolt_dropped("...")` and play resumes where it stopped. When it stands, call `revolt("...")` in `game.py`, which starts Chaos. The engine then refuses tax, salaries, works, new land, any voluntary payment out of the sealed treasury, and any seat change onto the throne. Every board card carries the Chaos line.

**The acclamation.** Give each player an `acclaim` prompt (`briefs.py prompt 031 Silke acclaim --claims "Rich:Paddy;Rob"`, with the claims so far): claim, back one claimant, or stand aside. Then count them with `acclamation({claimant_seat: [backer seats]})`. It records the three counts. With a winner, it seats them on the throne with the treasury and ends Chaos; with none, Chaos goes on, and the table may count again whenever the claims change.

## Rules misreadings

Correct any public misstatement of the rules, as always. That includes reasoning a player states, in public or in an aside, that rests on a wrong rule. For example, "a revolt only hands Rich the throne" is wrong when no set can take the throne under Chaos. Correct the rule with a public `note`, never the plan, and file it in the ledger's rulings. If a misreading seems to be steering the game away from its arc, or a rule's consequence looks unintended, tell the Director straight away. Don't wait for the end of the year: the Director may steer mid-chapter when a situation calls for it (Manish, 2026-10-28).

## Reporting to the Director

SendMessage the Director only: at the end of each year (one short paragraph: what happened, your context size); at the end of the chapter; and when something needs a decision (a safeguard trip, an engine error, a rules question, the usage limits). Don't stop for anything else.

## End of each round

- Update `ledger.md`: promises, offers declined, grudges, running bits, best lines, and new precedents.
- Save the state: `python run.py --snapshot yearN`.
- Add the round's rows to `log.md`, with the tokens each completion notice reported.
- Record usage at the start and end of a session (`get_usage`).

## Rulings made during the game

A rule Manish settles mid-game goes in the ledger, the log and `RULINGS.md`, but never on the page as news ("a new ruling, taking effect now"). The page plays as though the rule had always been there. If the table needs it, state the rule plainly at the point where it applies. A player who asks for a ruling at the table, and gets an answer, is part of the game and stays.

## Two traps in the tools

- **`act(deltas=...)` is keyed by player id, not seat.** After a seat change the two differ, so look the player up with `pid(seat)`.
- **Bash drops non-ASCII text silently,** and fails on heredocs with backticks. Write files with the Write and Edit tools instead.

## Framing (unchanged)

- Never ask a player for its reasoning or thinking, or why it "really" did something. Never ask it to justify a move afterwards.
- Never read an agent's transcript; use only the reply it returns.
- The aside is a performance for viewers: "a line to the camera, talking the audience through your move".
- If a safeguard trips, stop at once. Record the exact message that was being sent, and report it.
