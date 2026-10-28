# All's Quiet on the Western Front: report

An agent-played game of Dynasty for seven players, the one table with no Warlord. Each seat was a `dynasty-player` agent in character, every cast member in the province their name puns on. Seven chapter Storytellers refereed through the engine. A Director chose the deck, wrote the actor's notes and the handoffs, and checked each year. Four games ran in this checkout overnight, so the page wasn't rebuilt during play.

**It ended in Year 13 in survival:** every one of the 1,030 owed in public works was built. Rich, who drew the Gentry, ends on the throne: he built the Marble Pagoda, the last work, in the works step. That came before the auction where Graham and Reina were each one Jar short of a set.

**The target arc happened, three times over.** The arc was a peasant who climbs twice, to the throne, through grain politics alone. Graham went from Wheat to Scholar to Emperor (Years 5–6). Paddy went from Rice to Official to Emperor in one auction (Year 6). Silke went from Silk to Gentry to Emperor (Years 7 and 9). **The throne changed hands nine times, and all seven players sat on it.**

The record:
- `game.py`: 588 entries, with `RESULT = export(...)`; run it with `run.py`.
- `log/year1–13/`: every prompt and reply.
- `ledger.md`, with every ruling as a precedent; `diaries/`; `narration.md`.
- `state/setup.json` and `year1–13.json`.
- `handoff/chapter-0–6.md`.
- `seed.md`: the deck and the steering log.

## The story in brief

- **Chapter 1, "Whoever Waits Loses the Throne" (Years 1–2).** Bids were cheap at 4–6, and the upper class won every lot. Noah completed the Scholar's set mid-auction in Year 2 and took the throne from Reina at once.
- **Chapter 2, "Four Emperors and a Vase" (Years 3–4).**
  - Year 3: the peasants won their first pieces after a public tip to Silke.
  - Year 4, the doubling: land opened. Noah bought Province 4's only coast for the crown, and owned the mistake.
  - Three throne changes followed in one auction: Reina, then Rich, then Clark.
- **Chapter 3, "One Rung at a Time" (Years 5–6).**
  - Year 5: Clark's crown paid 15 of every 20 on land and fell from 297 to 2. Graham completed the Wheat set and replaced Noah as Scholar, the first peasant climb.
  - Year 6: Paddy went from Rice to Official to Emperor in two lots, and Graham bought the Vase and took the throne from him one lot later.
- **Chapter 4, "One Grain Over" (Years 7–8).**
  - Graham's crown built the whole Wall above Provinces 1 and 2, and paid for land, ending at 0.5 both years. Clark and then Noah lent it the salaries.
  - Silke climbed from Silk to Gentry.
  - Reina priced the last Jars at 300, and the lot went unsold.
- **Chapter 5, "Whoever Waits" (Year 9).** The Jar reopened at 2, under the unsold-lot rule this game was meant to test. Silke bought it at 201 and took the throne. Noah, in the wheat field, then went to Scholar and on to the throne in the same auction.
- **Chapter 6, "The Price Rises with the Chair" (Years 10–11).**
  - Year 10, ×6: the harvest paid out more than the engine's 2,500 cap on the Harvest Pile allows. Noah built all four remaining canal sections. Rich went from Rice to Silk to Gentry in one auction.
  - Year 11: Graham priced the Jar at 400, Rich paid it and took the throne, and Graham completed a Silk set and held it.
- **Chapter 7, "The Mortar Ready" (Years 12–13).**
  - Year 12: Rich built the Province 2 Irrigation System alone. Graham priced the Jar at 800, and it went unsold. Graham used his held set to take the Gentry's seat.
  - Year 13: Rich taxed 20% and built the Pagoda, and the game ended before the Jar could open at 2.

## Verdicts

Survival ending (§18): each player's final seat against the one they drew, with grain breaking ties.

| Player | Drew | Ended | Grain | Verdict |
|---|---|---|---|---|
| Rich | Gentry | Emperor | 1,985 | won |
| Graham | Wheat Peasant | Gentry | 1,694 | won (one Jar short of the throne) |
| Silke | Silk Peasant | Scholar | −150.5 | won, in debt |
| Clark | Official | Official | 473.5 | held |
| Paddy | Rice Peasant | Wheat Peasant | 1,307 | lost |
| Noah | Scholar | Silk Peasant | 1,135 | lost |
| Reina | Emperor | Rice Peasant | 892.5 | lost (one Jar short) |

There were sixteen seat changes. Nine went to the throne: Noah, Reina, Rich, Clark, Paddy, Graham, Silke, Noah, Rich.

## What the rules did

- **No Warlord made the auction everything.** With no raids, every seat change came from a complete set shown after a lot, often several in one auction. The same thing drove the full game, but here nothing else competed with it. The table's own precedents (mid-auction swaps, displaced players bidding on the lots left, two climbs by one player in one auction) are in `ledger.md`.
- **The unsold-lot rule worked as meant.** Twice a seller priced the last Jars out of reach: Reina at 300 in Year 8, Graham at 800 in Year 12. Each time the lot reopened at 2 the next year, once deciding the throne (Year 9). The rule turned a block into a one-year delay.
- **The Gentry's rent stayed small.** Rich asked 10 in Year 4, and Graham paid the minimum 5. Reina's loyalty rents in Year 6 drew 5, 10 and 15 from a 15 asked. Graham asked 100 in Year 13, and only the minimum was paid. Rent above 5 is voluntary, so it never became a weapon.
- **The Emperor's subsidy did.** Three crowns offered 15 of every 20 on land, uncapped, and emptied the reserve: Clark in Year 5, Graham in Year 7 (and 10 in 20 in Year 8). Noah offered the whole 20 in Year 10. No revolt followed, although "the reserve is too low" was available for years.
- **Revolt with no Warlord never happened.** Silke was in debt three times (Years 10–13), a standing cause, and nobody called one. Debt was always cleared by the next salary, except at the very end.
- **New land made the endgame.** The table bought from Year 4 on. By ×6 the land carried the economy: Graham's 57-square coast drew +1,020 in Year 11 alone.

## Needs a ruling

1. **Is the Harvest Pile finite at all? Settled: no ruling needed, and the game stands as played.** Manish, 2026-10-28, on learning the cap is the engine's and not the rules': "I think we don't need a ruling here, so this game is done". What's left is a tool and notes fix (below).
   - **No rule says it is.** Rulebook §8 lists the bags in the box, which total 2,500, but never says the Pile is limited or what happens when the bags run out.
   - **The cap is the engine's assumption.** It's listed under the engine's assumptions in `RULINGS.md` ("The Harvest Pile is finite"), and `engine.py` hard-codes `PILE_START = 2500`.
   - **What a real cap would mean.** All the grain in the game, counting the players, the crown and the Pile, would be fixed at 2,500. With seven players, 2,080 is left in the Pile after setup.
   - **This game went past it.** At ×6 the land's yield outgrew the box: Year 10's harvest took the Pile to −80, and Year 11's to −937.5. It ended at **−4,836.5**, so the players and the crown held about 7,300 between them, roughly three times the box.
   - **What I did.** To keep play going, I had every payout made in full, the Pile going below zero, a displaced player's 60 draw included. Nothing was prorated. In effect that's a bank that never runs out, with the bags only as a physical inventory.
   - **So Years 10–13 stand.** Still to do in shared files: `RULINGS.md` ("The Harvest Pile is finite") and the design notes should say the bags are an inventory, not a limit, and `swap()`'s draw of `max(0, pile)` should pay the full 60. The Storytellers patched that draw with an `act()` when it mattered (Year 12).
2. **Salaries after the ending.** The game ends in the works step, so the year's salaries are never paid, and Silke ends 150.5 in debt with her declared 115 unpaid. The verdict is unaffected (scoring ignores debt).
3. **Pieces stranded by a seat change.** Noah's purchase of Province 4's only coast in Year 4 left it with no square of new land for the rest of the game. That's legal, but harsh, and may deserve a line in §13.

## Steering

All of it is logged in `seed.md`, chapter by chapter.
- **The deck:** seed 74, as recommended. Land opened in Year 4, with a long squeeze to ×6 in Year 10.
- **Actor's notes:** a stance per character, rewritten between chapters for whoever had changed seats. That was most players, most chapters.
- **Four public tips:**
  - Silke, Year 3: no peasant had won a lot; the climb ladder; the Scholar was the poorest seat.
  - Graham, Year 7: the works as five projects, Year 11 at the earliest. This undercounted: the Wall took two years.
  - Noah, Year 10: four projects, Year 13 at the earliest.
  - Two conditional tips lapsed, in Years 6 and 10, because the table had already done what they were for.
- **Length:** two-year chapters, except Chapter 5, which was cut to Year 9 for context. That meant seven chapters, on five planned Storytellers and two spares.

## Usage

- **Plan:** the weekly all-models figure went from 18% to 25% over the whole game. The 5-hour window never passed 35%, and Fable weekly stayed at 0%.
- **Storyteller context at each chapter's end:** about 402k, 482k, 561k, 514k, 426k (one year), 610k and 452k. Mid-auction seat changes are the expensive part: Year 6 and Year 9 took about 240k and 300k on their own.
- **Director:** about 275k over the game.

## Continuity, drift and slips

- **Catchphrases:** Clark's two "books" stayed mostly his; Reina borrowed them once. "Rich's pile" for the Harvest Pile was corrected early. Rich's "terribly sorry" and "to the letter" held as his for thirteen years.
- **Hand edits to prompts,** each logged:
  - one added line (105, Chapter 3);
  - the stale automatic land line stripped after swaps (Chapters 4, 6 and 7);
  - the wrong endgame line stripped (Chapters 6 and 7).
- **A rollback trace.** Chapter 5's Storyteller began Year 10 before my close order arrived, and rolled it back. Silke's agent had already turned the ×6 card, and her Year 9 diary, kept word for word, mentions it. Play was unaffected, since she turned the same card first in Year 10, but the Year 9 diary on the page names a card not yet drawn.
- **Player agents using tools.** Two completion notices (Noah and Graham, Chapter 3) showed a player agent making two tool calls. The agent definition allows tools, though the players are meant to be tool-less. No reply showed knowledge the table couldn't have, but it's worth closing in `.claude/agents/dynasty-player.md`.

## Engine and tool gaps

- **`briefs.py` `endgame_note`** ignores the one-project rule and the Pagoda's own year:
  - with two projects left after this year's works step, it says "can end next year";
  - with one left after the works step, it says "this year".

  It needs to know whether this year's works step has passed. Shared tool, not edited.
- **`briefs.py` `free` and `place` prompts after the land step** still append the land reminder, listing the mover's old province.
- **`swap()`'s draw** is capped at `max(0, pile)` (above).
- **Bash on Windows:** heredocs or command lines with non-ASCII text (en dashes, middle dots) or backticks fail with exit 127. Every Storyteller wrote files with the Write tool and ran small Python scripts.
- **Still not applied by the engine** (scripted as `act()`s): minimum bids and the unsold-lot rule; the one-project rule and prerequisites; the Utility card; the Wall breach; disasters for the Good and Evil and breach cards.
