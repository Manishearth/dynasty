# The short game: report

An agent-played game of Dynasty at four seats: the Emperor and the three upper provinces, with no Warlord and no peasants. The table agreed before setup to stop after eight rounds (Note 19). Each seat was a tool-less `dynasty-player` agent in character, every cast member in the province their name puns on. One Storyteller session per two-year chapter refereed through the engine, and a Director session chose the deck, wrote the actor's notes, checked each chapter and steered towards the arc in `scenario.md`. The deck was seed `39` (`seed.md`).

**It ended at the agreed stop, after Year 8,** with 300 of the 810 owed in public works built. The throne changed hands twice: Reina to Clark in Year 3, and Clark to Rich in the last round. Rich (drew 3, ends 1) and Noah (drew 4, ends 2) won. Clark (drew 2, ends 3) and Reina (drew 1, ends 4) lost. Reina ended with the most grain, 165.

The record:
- `game.py`: 192 entries, with `RESULT = export(...)`; run it with `run.py`.
- `log/year1–8/`: every prompt and reply.
- `ledger.md`, `diaries/` and `narration.md`.
- `state/setup.json` and `year1–8.json`.
- `handoff/chapter-0–4.md`.

## The story in brief

**Chapter 1, "Good Things Come to Those Who Wait" (Years 1–2).** At four seats each seller holds one piece of its own, the only one in the game and needed by both rivals, plus two of a type it never needs. All three sellers sold the spare type and held their own piece back. Lots went for 8–12. Everyone ended Year 2 holding 2 of 4.

**Chapter 2, "The Most Expensive Receipt in the Empire" (Years 3–4).** Year 3 forced the three single pieces up, each at 40. Clark won the Deed and the Brush, completed his set and took the throne from Reina: "Noah, enjoy the Customs House. It's the most expensive receipt in the empire." His pieces went back to stock, so Rich and Noah each had two types again, and each kept his key piece back while selling the other. Clark raised the tax to 50%, and whispered Rich a Reservoir in exchange for keeping the Deed home.

**Chapter 3, "Ninety-Five Fits" (Years 5–6).** The Director's one tip went to Rich (below). He set the Deed at 95, and Noah, the only bidder who could meet it, paid it. Noah declined the throne, since his Deed would have gone back to Rich's stock for Reina to buy, and took the Official's chair from Reina instead. In Year 6 the population doubled and new land opened. The first unsold lots came that year: Noah's Customs House and Rich's Bowl, each at 150. Rich paid 21 for Reina's Vase to keep it from Noah.

**Chapter 4, "Nothing but the Throne" (Years 7–8).** The Customs House reopened at 2 and Rich took it. Noah paid 32 for Reina's Brush to keep it from Rich. That left the arc's position exactly: two players each one piece short, each holding the piece the other needed. In Year 8 Noah said in public that a set could only come from the auctions, and the Storyteller corrected it: pieces on the board may be traded. Rich then whispered Noah 60 for the Brush and promised to take only the throne. Noah said the deal out loud and took it, and Rich replaced Clark: "I'll take the throne, and nothing but the throne, exactly as I told Noah."

## Verdicts

| Player | Drew | Ends | Result | Grain |
|---|---|---|---|---|
| Richard Baron | Gentry (3) | Emperor (1) | won | 134.5 |
| Noah Tall | Scholar (4) | Official (2) | won | 87 |
| Clark Grafton | Official (2) | Gentry (3) | lost | 60 |
| Reina Osorio | Emperor (1) | Scholar (4) | lost | 165 |

## Against the scenario

- **Target arc: a race for the throne decided in the last two rounds. Met.** The throne changed hands twice, and the deciding change came in the eighth round. At the end of Year 7, Rich and Noah were each a single piece short. A tighter finish wasn't possible: the last set was completed by one trade between the two of them.
- **The unsold-lot rule at its sharpest.** It mattered less than expected. Sellers didn't hold their key pieces back with unmeetable minimums. They kept them in stock by selling another type first, which the rules allow, and which the one-round limit doesn't touch. Every single piece sold the first year it went up, at 40 or the seller's price. The rule came into play only in Year 6 (two lots at 150), and its main effect was the Customs House selling at 2 in Year 7.
- **The short-game ending with agents who know the count. It worked.** Every board card carried "Year r of 8" from `LAST_ROUND`. In Year 8 the players reasoned about it out loud. Reina and Rich bought no land because it "never pays a single harvest". Noah saw that any seat but his own was still a win. Rich paid salaries at the minimum because "grain breaks ties". Nobody tried to stretch the game.
- **Population pressure arriving late.** It arrived on time (×2 in Year 6, ×3 in Year 8) but bit lightly. Nobody fell into debt, and Reina's eight sea squares made her the richest player.

## Steering

All logged in `seed.md`:
- **The deck:** seed 39, the only candidate to reach ×3 by Year 8.
- **Actor's notes:** written before Chapter 1. Reina's and Clark's were rewritten before Chapter 3, after they changed seats, and Rich's before Chapter 4, after he sold his Scroll. A note gives a stance, never a move.
- **One Storyteller's tip,** to Rich in Year 5: the Deed is the one piece Noah needs, its seller sets the minimum, and an unmet lot must go up again next year at 2. Rich set 95 and Noah met it, so the tip didn't stop Noah. It did make him pay 95 for the piece.
- **The ending:** the table was told at setup, and again before the last chapter, that it stops after eight rounds.

**Not steering, but it shaped the ending:** in Year 8 the Storyteller corrected Noah's public misstatement that a set could only come from the auctions. It was the standing ruling for any public misstatement of the rules (a note and a plain act, worded only as the rule). The trade followed at once, and Reina's line, Rich's aside and Rich's diary all cite it. Without the correction, the throne might well have stayed with Clark. The correction was required, and it stands. A later table may want to know that one rules correction can decide a short game.

## Rules and rulings

- **Which piece goes up is the seller's choice** (Manish, confirmed during the game). At four or five seats each seller holds two types, so this is a live decision every year. The Storytellers asked each seller in a short `free` prompt before the auctions.
- **A lot that draws no bid even at 2.** Rich's Bowl went unsold at 150 in Year 6, then at the floor of 2 in Years 7 and 8, and ended in stock. The rule says it must go up again at 2, and nothing more. That's fine, since it was his last stock and had to go up anyway. But the rule doesn't say what happens to a piece nobody wants at any price.
- **The crown and auctions.** Clark, as Emperor, whispered that the crown would bid against Noah for the Deed. The Storyteller noted to both that the Emperor doesn't bid (§10).
- **No ruling needed.** A private trade of pieces on the board was legal at any time, and the engine moved the piece (`give`) and the grain (`act(..., deal=True)`).

## Tools

**Changed during the game** (`playthrough-sim/agents/briefs.py`, uncommitted):
- `LAST_ROUND`: a game sets it in `game.py` to get the round count on every board card, a short-game endgame note in its last two rounds, and the right length in the launch intro. Games without it are unchanged. Nine prompt kinds for the full game came out byte-identical.
- `has_warlord`: with no seat 8, the prompts leave out Warlord, soldier and raid lines. Year 1's collect prompt had gone out with "The Warlord may refuse to pay" before the fix. Nothing on the page names the Warlord.

**`DIRECTOR.md`** gained "Messages and the page": the app's cap of about 10 cross-session messages per session, status files instead of yearly reports, and page rebuilds only for a Director told it's the only one running.

**Still open:** `swap()` deltas and `act(deltas=...)` are keyed by player id, not seat. A first try at the Year 8 trade was keyed by seat and paid the wrong player, and was fixed before anything ran on. Bash heredocs with non-ASCII text fail silently in this environment, so every session used the Write tool.

## Usage

- **Storyteller context at each chapter's end:** about 290k, 300k, 346k and 315k. Four seats fit two-year chapters comfortably, under the 450k stop line.
- **Plan usage:** from 10% to 20% of the 5-hour window, and from 13% to 15% weekly, over the whole game.
- **Messages:** the Director hit the app's cross-session cap once, between Chapters 2 and 3, until Manish replied. After that the game moved to the status-file pattern.

## Continuity and drift

- **Voices held.** Reina managed and counted. Clark kept his grievance book. Rich fawned and kept his promises "to the letter". Noah said every number out loud. Noah also lost four lots by a single grain, a running bit he named himself before he finally "won by a grain" in Year 7.
- **Slips were caught and corrected.** About twenty small misstatements are listed in the ledger's rulings, each corrected by a note to the table or in that player's next prompt. Early asides mentioned peasants and raiders that this table doesn't have.
