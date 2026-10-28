# Highway Rob-bery: report

An agent-played game of Dynasty with six players: the Emperor, the Official, the Gentry, the Silk and Rice Peasants, and the Warlord. Provinces 4 and 7 were empty. Each seat was a tool-less `dynasty-player` agent in character, every cast member in the province their name puns on. One Storyteller session per two-year chapter refereed through the engine. A Director session chose the deck, wrote the actor's notes and handoffs, steered between chapters, and ruled on three questions in the last two years. The deck was shuffled with seed `297` (`seed.md`).

**It ended in Year 12 in survival.** Rob, the Warlord, was one name short of his objective when Clark called a revolt on Paddy's debt to stop the last work going up. Rob held the only soldiers on the board, and Reina, Clark and Paddy backed him, so he was acclaimed Emperor. He built the Province 3 Reservoir at once and ended the game. Reina, who drew the throne, finished in the desert with his army.

The record:
- `game.py`: 372 entries, with `RESULT = export(...)`; run it with `run.py`.
- `log/year1–12/`: every prompt and reply.
- `ledger.md`, `diaries/` and `narration.md`.
- `state/setup.json` and `year1–12.json`.
- `handoff/chapter-0–5.md`.

## The arc, and how it changed

`scenario.md` began with "the Warlord's campaign is the story": Rob's raids against a table paying more and more to stop him. Before Chapter 1, Manish changed it twice:
- **Rob takes the throne and wins,** with time to reign, as mean a ruler as he likes. A collapse under him would be just as good.
- **Most players end on a lost seat,** through infighting and many seat changes.

The actor's notes were rewritten towards infighting rather than a coalition (`seed.md`, steering log). Both halves of the arc happened. Rob got no reign, though: he ended the game the moment he took the throne.

## The story in brief

**Chapter 1, "Neat Handwriting" (Setup–Year 2).** Rob put a soldier on the Wall strip and one at sea, refused tax, announced "Clark first" and raided everyone else. Reina, with no Scholar at the table, made Rob her I Ching reader at 5 a year, a salary as a bribe. Clark whispered Rich's squares to Rob, and Rob read the whisper out to the table. Every piece of stock was sold by Year 2, and Rich held a full set.

**Chapter 2, "Straight Up the Steps" (Years 3–4).** Rich took the throne from Reina. A year later Silke, her purse topped up by her quarter of the Jar's price, took the Official's seat from Clark. Rob took his first piece, Paddy's Jar.

**Chapter 3, "A Chair So Keen to Be Sat In" (Years 5–6).** Silke took the throne from Rich, and Reina took it back from Silke. Land opened at ×2, and the table bought 12 squares. Rich was runner-up on all three of Year 6's lots, each by one grain. Rob: "Three Emperors in two years. I've never seen a chair so keen to be sat in."

**Chapter 4, "A Grain Past Careful" (Years 7–8).** Reina paid the whole of 14 new squares, and the reserve fell to 14.5. Paddy won the Jar on his fourth try and took the Gentry's seat from Silke. Rob was still on one piece: every seat change sent his targets' pieces back to stock just before his soldiers reached them.

**Chapter 5, "Two Scrolls in the Sand" (Years 9–10).** The population reached ×4. Clark took the Official's seat back from Rich. Rob took Clark's Scroll and refused every offer for the pieces on his desert: Clark's 60, then 100. Reina doubled his reading money to 20 to keep the Scrolls there. No stock was left anywhere.

**Chapter 6, "Grain Doesn't Sit in a Chair" (Years 11–12).** The ×4 harvest sank Paddy: he sold his pieces back to the pile at 2 each and fell into debt. Rob took Rich's Customs House, leaving Silke, who held one piece two marches away, as his last name. Reina built the Wall above Provinces 2 and 3, and in Year 12 declared the Reservoir, the last work. Clark called a revolt on Paddy's debt, and Paddy, Rich, Silke and Rob agreed. Reina paid off the debt in the same round, too late. In the acclamation Rich led in grain (975.5), but Rob led in soldiers (3) and friends (Reina, Clark and Paddy).

## Verdicts

Survival ending (§18): each player's final seat against the one they drew, grain breaking ties.

| Player | Drew | Ended | Grain | Verdict |
|---|---|---|---|---|
| Rob | Warlord | Emperor | 281.5 | won |
| Paddy | Rice Peasant | Gentry | 0 | won |
| Clark | Official | Official | 86.5 | held |
| Rich | Gentry | Silk Peasant | 975.5 | lost |
| Silke | Silk Peasant | Rice Peasant | 675 | lost |
| Reina | Emperor | Warlord | 60 | lost |

Three of six lost, one held. The richest player, Rich, lost.

**Seven seat changes, four of them on the throne:**
- Year 3: Rich took the throne from Reina.
- Year 4: Silke took the Official's seat from Clark.
- Year 5: Silke took the throne from Rich.
- Year 6: Reina took the throne back from Silke.
- Year 8: Paddy took the Gentry's seat from Silke.
- Year 9: Clark took the Official's seat back from Rich.
- Year 12: Rob was acclaimed Emperor and Reina became the Warlord.

Two diaries misstate their verdicts (Reina and Rich each call theirs a win). They're kept word for word, with the fact in each reply file's ruling.

## What the rules did

- **Scarcity drove the infighting.** With two pieces of each type and three collectors for each, someone was always one short. Every climb to the throne returned three pieces to auction, so the chairs kept turning. Lot after lot went by a single grain: Paddy alone lost four that way, and Rich all three in Year 6.
- **Seat changes protected the Warlord's targets.** A displaced player returns everything, and a mover's pieces go to a new province, so again and again a piece Rob was a round or two from went back to stock or moved away first (Rich's Bowl in Year 9 is the clearest case). After eleven years he had three of his four names. The objective (one piece from each player, by name) is hard at six when the players keep moving.
- **A raided piece leaves the game.** By Year 10 both Land Deeds and a Jar stood on Rob's desert, and every set at the table ran through him. He sold none of them, and nobody else could finish a set.
- **×4 broke the harvests** of anyone without land. Paddy, as Gentry, had none, sold his pieces back at 2 each and went into debt. That debt was the cause of the revolt that ended the game.
- **Revolt was the Warlord's road to the throne,** not his objective. Chaos made the acclamation count soldiers, and Rob had the only ones on the board. Nobody bought a soldier all game: Reina paid Rob instead, every year, which matched her note.
- **New land** was bought every year from the doubling, 81 squares in all: Province 5 39, Province 6 24, Province 1 14 and Province 2 4 (on its strip, once the Wall stood), mostly half-paid by the crown. It made Rich (Silk) and Silke (Rice) the richest players by far, and it didn't stop either of them losing their seats.

## Steering

All in `seed.md`'s steering log:
- **The deck:** seed 297 kept. It gives five calm years at ×1, then ×2 in Year 6 and ×4 from Year 9, and Rob plays only one disaster.
- **The actor's notes:** written before Chapter 1, then rewritten for Manish's new arc: infighting, climbers, and Rob means to have the throne. Rob's note was given more urgency before Chapter 4 and an anti-hoarding line before Chapter 6.
- **Storyteller's tips:** four, all public, from the rules and the board:
  - Rob, Year 7: be inside the provinces before the auctions.
  - Rob, Year 9: he may sell raided realia.
  - Silke, Year 11: the remaining Deeds and Jar are on Rob's desert.
  - Rob, Year 12: the last work ends the game before the march; a revolt on a debt stops the works, and Chaos is decided by grain, soldiers and friends.
- **The Year 12 tip was given mid-chapter,** by message, because a handoff would have come too late. Without it the Reservoir would have ended the game in the works step with Rob one name short, which is the full game's ending again. Clark, not Rob, called the revolt.
- **Length:** "about ten years" became twelve. Two spare Storytellers were parked, and one played Chapter 6.

## Rulings made during the game

By the Director (Manish away overnight), each logged in the ledger as a precedent and open to his review:
- **A harvest that sinks a player is a payment falling due** (Year 11). They sell realia back to the pile first, with no private sale ahead of it (RULINGS, "Running out of grain").
- **Before the last owed work is built, every seat gets one turn** (Year 12): pass, call or back a revolt, or deal.
- **A revolt stands if two others agree in the same simultaneous round in which the cause is removed** (Year 12). Reina paid off Paddy's debt in the round the agreements came in. As with the auction precedent (049), an act made while the others' answers were being set doesn't undo them, and her gift stands. **The alternative** was to give the Emperor's answer seat-order priority, which removes the cause before anyone agrees. That would have ended the game with the build and Reina on the throne. If Manish prefers it, Year 12 can be replayed from `state/year11.json`.

By Manish, before play: **bought soldiers stay with the seat** on a seat change (RULINGS, "Bought soldiers after a seat change"). `swap()` was changed for it; no soldier was bought in this game.

The Storytellers' own precedents (about forty) are in the ledger's rulings section.

## Usage

| | 5-hour window | Weekly |
|---|---|---|
| End of Chapter 2 | 4% | 17% |
| End of Chapter 4 | 15% | 20% |
| End of Chapter 5 | 21% | 21% |
| End of Chapter 6 (end) | 27% | 23% |

Storyteller context at each chapter's end: about 372k, 377k, 424k, 417k, 460k and 505k. Six seats saved less than hoped:
- **The prompt backlog:** each prompt's "since your last turn" backlog and the launches cost the most.
- **The ledger:** the entries grew until they were trimmed before Chapter 6.
- **Revolt:** its round of five full prompts was the most expensive step in the game.

## Continuity and drift

- **Voices held across seven seat changes.** Reina stayed the gracious builder on three seats. Rich stayed the fawner, with promises kept to the letter. Silke counted everyone's grain. Clark kept his book "with dates". Paddy was "a grain past careful". Rob stayed the gleeful villain who named his targets, and lied about them in Year 1.
- **Drift:** "a grain past careful" spread from Paddy to Rich's Year 6 diary. It's mild, and it wasn't fed.
- **Hand-written text:** one launch line to Silke was mistyped by hand in Chapter 6, and it's logged. Everything else went out as printed.
- **The ledger trim:** the Chapter 6 Storyteller trimmed every ledger entry before its launches. The ledger was never committed, so **the full entries to Year 10 survive only in the Year 1–10 prompts in `log/`** (each launch carried them), not in git.

## Engine and tool gaps

**Not applied by the engine** (scripted as `act()`s), as before: minimum bids and the unsold-lot rule; the Emperor's Share; Imperial Charity; the Utility Tax; the one-project rule and prerequisites.

**Tool bugs found, not fixed** (shared tools, left for the main session):
- `briefs.py`'s I Ching menu says the Emperor "owes" an appointed reader a salary. An appointee is paid only at the Emperor's choice.
- `briefs.py`'s endgame line says "can end next year" a year early once the year's one project is built. Each time, a public note gave the true date.
- `briefs.py`'s free menu reminds a player that new land is open even under Chaos, when no works or land are allowed.
- `DIRECTOR.md` describes a public tip as `note --to <Player>`, but `--to` shows a note only to its recipient. File a public tip with no `--to`.

**The harness:**
- Bash commands with an en dash, or heredocs with backticks, break the shell wrapper. Every Storyteller wrote such things with the file tools or a small `.py` script.
- A Director's message sent while a Storyteller is mid-turn is queued until that turn ends. The Year 12 tip arrived one prompt late for that reason.

## For the page

`highway-robbery` is finished and ready to be built into `playthroughs-real.html`. The title, subtitle ("Six players · twelve years · the Warlord on the throne") and description are in `game.py`'s `setup()`. `build_real.py` wasn't touched: the main session adds the game or drops it from `IN_PROGRESS` and rebuilds.
