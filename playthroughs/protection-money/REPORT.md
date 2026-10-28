# Protection Money: report

Planned and played as "The Dark Ages" (folder `dark-ages/`, now `protection-money/`); renamed by Manish after the game, since the revolt and Chaos it was named for never came.

An agent-played game of Dynasty with six players: the Emperor, the Official, the Gentry, the Silk and Rice Peasants, and the Warlord. Provinces 4 and 7 were empty. Each seat was a tool-less `dynasty-player` agent in character, every cast member in the province their name puns on. One Storyteller session per two-year chapter refereed through the engine. A Director session chose the deck, wrote the actor's notes and handoffs, and steered lightly between chapters. The deck was shuffled with seed `350` (`seed.md`).

**It stopped after Year 12, as agreed, with no revolt called in twelve years.** Rich, the Gentry, took the throne with a set in Year 2 and ruled for ten years. Clark held a complete set beside the throne all that time, paid thirty a year by Rich to leave it unused, and in Year 12 he used it. The pieces his climb sent back to auction carried Paddy and then Silke into the Official's seat the same night. 310 of the works were never built.

The record:
- `game.py`: 378 entries, with `RESULT = export(...)`; run it with `run.py`.
- `log/year1–12/`: every prompt and reply.
- `ledger.md`, `diaries/` and `narration.md`.
- `state/setup.json` and `year1–12.json`.
- `handoff/chapter-2–6.md` (the Director's) and `handoff/storyteller-4–6-notes.md` (the Storytellers').

## The arc, and how it changed

`scenario.md` aimed at **an early revolt, a stretch of Chaos, then a recovery**: the population doubles in Year 3, the next three harvests are lean, and a hard-taxing or broke Emperor faces a revolt around Years 4–6. Its fallbacks were a revolt that resolves at once, or no revolt if the table visibly came within a vote of one.

**None of that happened. No revolt was ever called**, so revolt, Chaos and the acclamation count are still untested by agents. The table didn't come within a vote: nobody even asked for agreement. Every diary from Year 4 to Year 6 named the pressure (a reserve of 19.5, then 4, then 0, against Clark's thirty a year), but nobody called it.

Why the revolt never came, as far as the record shows:
- **Rich never gave a cause that stuck.** He taxed 30% every year and never went into debt; his line was "the crown ends this year at zero, but it ends it owing nobody". He paid towards every peasant square from the doubling on, so "won't subsidise new land" never applied. He also kept every promise to Clark to the grain.
- **Land arrived before the lean years.** The doubling came in Year 3, a year before the bad harvests, and the crown half-funded the first squares at once. By Year 5 the peasants' land carried them through. The booklets say peasants revolt "only when starvation threatens", and it never did.
- **Clark's set did the work a revolt would have done.** He was the player best placed to call one, and he was being paid not to act. A set takes the throne with no allies, so he had no reason to share it in an acclamation.
- **The Warlord sank instead of the crown.** At ×4 it was Rob who went into debt, in Year 12, with no time left for anyone to call a revolt on it.

The scenario's "recovery through land" did happen, but under the same Emperor and without a fall first: 93 squares were bought, and the crown's reserve went from 0 in Year 6 to 443 in Year 11.

## The story in brief

**Chapter 1, "The Knife Held Up" (Setup–Year 2).** Reina appointed Clark to read the I Ching, taxed 50% and built the Summer Palace. Rich won the Customs House, Jar and Bowl in Year 1: a complete set, which he held ("the knife is worth more held up than swung"). Rob's raid took him below the 20 grain he needed. The Year 2 harvest put it back, and at the rent step Rich took the throne. Clark won the Jar and Bowl in a live raise against Reina for a second complete set, and named his price for not using it: thirty a year. Rich paid it publicly and promised "not one grain short and not one day late".

**Chapter 2, "Not One Grain Short" (Years 3–4).** The population doubled and land opened. Rich built the Winter Palace and the Marble Pagoda, and half-funded every peasant square. Clark spent 44 on a spare Jar and Bowl, just to keep them from Reina. Every piece of stock was sold by Year 3. Rob took his first piece, Reina's Customs House. The reserve fell to 19.5.

**Chapter 3, "Owing Nobody" (Years 5–6).** Two lean years. A Storyteller's tip read the causes for revolt and the acclamation counts out to the table. Rich kept 30%, built almost nothing, paid Clark, and ended Year 6 on exactly 0, in debt to nobody. Rob took Paddy's Customs House. Silke bought land every year.

**Chapter 4, "A Grievance with a Number on It" (Years 7–8).** Good harvests. Rich dug canals in Provinces 5 and 6 and built two Wall links, both over his own province; Clark wrote the grievance down. Reina doubled the rent to 10. Silke reached 24 squares. Rob's W2 stood one round from Silke's Scroll, his last name, and his second disaster barred all his raids.

**Chapter 5, "A Very Short Rental" (Years 9–10).** Silke bought a soldier, stood it on her Scroll, and captured Rob's raider when it stepped beside it. Rich finished the Wall over Province 1 and built two links over Province 2. He bought a soldier of his own, which Rob captured at once. The reserve recovered to 188.

**Chapter 6, "I Never Sold You the House" (Years 11–12).** At ×4 Rob's harvest sank him: he sold Paddy's Customs House back for 30 and the other two pieces to the Pile at 2. Silke bought the Customs House and her own Jar (301, to keep it from Paddy) and was one Bowl short. Clark refused her 300, then 500 with an oath, for his spare. In Year 12 he collected the tax and took the throne with the set he'd held since Year 2. His pieces went back to auction: Paddy won the Scroll and Jar at 13 each and took the Official's seat from Rich, and Silke won a Bowl at 17 and took it from Paddy.

## Verdicts

Agreed stop after Year 12 (§18, Notes 18–19): each player's final seat against the one they drew, grain breaking ties.

| Player | Drew | Ended | Grain | Verdict |
|---|---|---|---|---|
| Clark | Official | Emperor | 930 | won |
| Silke | Silk Peasant | Official | 2,328 | won |
| Paddy | Rice Peasant | Silk Peasant | 60 | won |
| Rob | Warlord | Warlord | −28.5 (in debt) | held |
| Reina | Emperor | Gentry | 107 | lost |
| Rich | Gentry | Rice Peasant | 55 | lost |

**Four seat changes:** Year 2, Rich took the throne from Reina; Year 12, Clark took the throne from Rich, then Paddy took the Official's seat from Rich, then Silke took it from Paddy.

## What the rules did

- **A held set is a standing threat, and it can be rented.** Two sets completed in the first two years, and the second was held for ten years and paid off annually. Nothing in the rules makes a set decay or expire. This is the game's main finding: a held set and a salary did the work the scenario expected of a revolt.
- **Six players, two pieces of each type, and every piece was sold by Year 3.** After that there were no auctions at all for eight years, until pieces came back through the Warlord's sell-back and Clark's climb. The middle of the game was land, works and the Warlord.
- **Land early made the lean years painless.** The crown's half-subsidies from the first doubling meant the peasants' squares were paying before the bad harvests came. The peasant collapse game bought none and collapsed; this table bought 93 (Province 5 54, Province 6 25, Province 1 11, Province 2 3) and never had a player in debt until Rob in Year 12. Reina's Province 3 never got its Wall, so it never bought a square.
- **×4 ruined the landless.** Rob's harvest was −40 in Year 11 and he had nothing but pieces to sell. Clark, with three squares bought only that year, fell from 228 to 153; Reina, with none, was carried by her rents of 50 and 25.
- **A guard works as the rulebook says.** One bought soldier on Silke's Scroll stopped Rob for four years; his raider stepped beside it, and the guard captured it.
- **The Warlord's objective** stalled at three of four. The raided pieces stayed on his desert until his own harvest forced him to sell them.

## Steering

All in `seed.md`'s steering log:
- **The deck:** seed 350 kept, the scenario's recommendation. Of the four scouted, it alone had three lean years (4–6) followed by four good ones (7–10).
- **The actor's notes:** written before Chapter 1 from the scenario's levers. Rewritten before Chapter 2 for Rich, Reina and Clark, because the throne had changed hands. Unchanged after that.
- **One Storyteller's tip,** in Year 5, to Paddy and public: the seven causes for revolt, how one is called off, and the acclamation's three counts. Rules only. It didn't produce a revolt.
- **Length:** stopped after Year 12 (`LAST_ROUND = 12`, set before Chapter 6). 430 was still owed in five works, which at one project a year couldn't be finished before about Year 15, and Years 11–12 were the scenario's last chance at a revolt.
- **Not steered:** I didn't push for a revolt once the lean years passed without one. The scenario says not to force it.

## Not steering, but…

- **Correcting a misreading of the guard rule.** Storyteller 5 read `rules-digest.md`'s "One raider can't break a free guard; two can" as a separate rule the engine fails to enforce, and suggested refusing such captures by hand. The rulebook (§14, "Guarding a piece") makes it a consequence of move order. The Chapter 6 handoff said to enforce nothing by hand. Had that ruling stood, a lone Warlord soldier could never have taken a guarded piece.
- **Public rules corrections** (all in the ledger), none of which decided anything: Clark's Year 9 reading left out Province 8's disaster, and Silke repeated an out-of-date reserve figure in Year 10. A Year 12 note pointed out that the Emperor doesn't bid.

## Rulings to look at

The Storytellers' precedents are in `ledger.md` (about 35). These five go beyond the written rules and may want a ruling from Manish:
- **(Y6, 084) A raider may take the 5 on a piece's square instead of the piece; that square is then raided, so the piece can never be taken from it.** This follows from "5 or the piece" and "a raided square is never raided again", but it gives a cheap way to make a piece permanently safe (Clark's Scroll on I15).
- **(Y11, 144) The Warlord's raids stay on his record when the raided pieces leave his hands** (by sale or sell-back). This was read from RULINGS "A new Warlord", where the objective is things done.
- **(Y11, 144) A harvest that will sink a player is a payment falling due.** Before it was paid, Rob could raise grain by a private sale (he sold Paddy his Customs House for 30) and then had to sell back. This is a little looser than Highway Rob-bery's Year 11 precedent, which allowed no private sale ahead of the sell-back.
- **(Y12, 169) A seat change may be made at any step, and when a seat change and an offer cross, the step order decides.** Clark took the throne in the collect step, and Silke's 500 for his Bowl, sent in the land step, reached him after he no longer held it. RULINGS lets the players settle crossings in a revolt, but this one was settled by step order.
- **(Y12, 169–177) Two sets completed in one auction:** each buyer was asked in the order the sets were completed, the later one hearing the earlier's choice.

## Usage

| | 5-hour window | Weekly |
|---|---|---|
| End of Chapter 2 | 5% | 28% |
| End of Chapter 3 | 8% | 29% |
| End of Chapter 4 | 10% | 29% |
| End of Chapter 5 | 12% | 29% |
| End of Chapter 6 (end) | 17% | 31% |

Storyteller context at each chapter's end: about 393k, 365k, 337k, 333k, 395k and 567k. Chapter 6 went past the 450k stop line in Year 12 and, under the stop rule, finished the year. Launch prompts ran 13–16k characters each, and every continuation carried its catch-up, so pasting prompts was the main cost. The spare Storyteller (7) was never woken.

## Continuity and drift

- **Voices held.** Clark kept his book "in my best hand" for twelve years and ended wearing it ("the man who keeps the paper trail ends up wearing it as a crown"). Rich fawned and kept every promise to the letter. Silke counted everyone's grain out loud. Paddy was careful and owed nobody. Rob smiled, lied, and paid his tax for "a nice clean reputation for the night I stop being nice". Reina's Year 4 line came true: the man paid to guard the crown was the one best placed to take it.
- **Two slips in Chapter 6,** both caught and logged in the ledger. A fault in the Storyteller's script helper re-inserted Year 11's last block before Year 12's first prompt; it was removed and the prompt regenerated before any player saw it. And a few continuation messages carried a slightly abridged board card; the prompt files hold the full cards.

## Engine and tool gaps

**Still not applied by the engine** (scripted as `act()`s): minimum bids and the unsold-lot rule; the cards' extra effects (the Utility Tax, Breach, Repairs) and personal disasters; the one-project rule and prerequisites.

**Tool gaps found** (shared tools; the first three were fixed by the main session after the game, 2026-10-28):
- **`briefs.py`'s crown and collect menus assume the Warlord refuses tax.** Rob paid every year, and every Storyteller corrected the line by hand.
- **`briefs.py`'s land menus don't carry the crown's per-square offer,** and its `free` prompt appends the new-land reminder to non-land prompts (rent, soldiers). Storytellers 4–6 patched both by hand.
- **`rules-digest.md`'s guard line reads like a separate rule.** Suggest: "A raider must end a move straight beside the guard, which may then capture it; so one raider can't break a guard that's free to move, but two can."
- **A bought soldier's move** has no prompt type; Storytellers 5–6 used a `free --short` prompt after the Warlord's march.

**The harness:**
- Bash commands with non-ASCII characters (§, en dashes), or heredocs with backticks, silently do nothing. Every Storyteller, and the Director, hit it.
- Two Storytellers wrote their hand-over notes into the Director's own notes folder rather than the shared one. Chapters 4–6 put them in `handoff/` instead, which worked better.

## For the page

`protection-money` (then `dark-ages`) is finished and built into `playthrough.html`. The title ("Protection Money"), subtitle ("Six players · twelve years · the Emperor pays to keep his throne") and description are in `game.py`'s `setup()`. `build_real.py` wasn't touched: the main session adds the game or drops it from `IN_PROGRESS` and rebuilds.
