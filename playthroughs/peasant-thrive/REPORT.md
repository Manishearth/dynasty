# Peasant thrive: report

An agent-played game of Dynasty at four seats: the Emperor and the three peasants, with no Warlord. It's the third peasant table, with the same cast as Peasant collapse and Peasant draw, but on a deck chosen with Manish so that the table had room to succeed. Each seat was a tool-less `dynasty-player` agent in character. Five Storyteller sessions refereed through the engine, one per two-year chapter. A Director session chose the deck, wrote the actor's notes, checked every chapter and wrote the handoffs.

**It ended in survival in Year 9.** Every one of the 520 owed in public works was built, nobody was ever in debt, and no year was rewound. Paddy, who drew the Rice Peasant, ended on the throne and won. Graham held his Wheat seat. Silke and Reina each ended a seat below the one they drew.

**The finding:** on a deck where the population doubles before it grows by half, the peasant table thrives with light steering. Land opened in Year 5 at ×2, while every province still fed itself, so land was something to buy ahead rather than a rescue. The crown built a work every year and finished three years before the second doubling. The two earlier tables drew the same deck as each other, where land opened only at ×3 and the third population card made it ×6 in Year 11. Between Peasant draw and this game, the only rule changes (the Harvest Pile never running out, an agreed stop partway through) played no part. The order of the population cards made the difference.

The record:
- `game.py`: 107 log entries, 192 engine entries, `RESULT = export(...)`; run it with `run.py`.
- `log/year1–9/`: every prompt and reply.
- `ledger.md`, `diaries/` and `narration.md`.
- `state/setup.json`, `year1–8.json` and `year9-end.json`.
- `handoff/`: every brief. Never staged.
- `seed.md`: the deck, why it was chosen, and the steering log.

## The story in brief

**Chapter 1, "Three Deals Honoured at One Table" (Years 1–2).** Reina taxed at 30% and built the Province 7 Reservoir before any palace, then the Winter Palace. All three peasants proposed not fighting over first copies, then all bid anyway; in Year 2 every promise was kept.

**Chapter 2, "The Set's Made to Be Used" (Years 3–4).** Graham won the Jar and the Bowl by a grain each, completed his set and took Silke's Silk seat, with a grudge from Year 1 he had written down. A year later Paddy bought the Jar from Graham at 60 and took the Silk seat from him. Reina dug both canal sections in Provinces 5 and 6, as she had promised in public.

**Chapter 3, "Paid as I Said I Would" (Years 5–6).** The population doubled, and land opened. The table bought 13 squares, and Reina paid five a square towards everyone's, which emptied the reserve. She repaid a whispered debt to Graham in public, to the half grain. Paddy paid 70 for a Brush and 120 for the Wooden Bowl and took the throne in Year 6.

**Chapter 4, "I've Written Mine Down Too" (Years 7–8).** Paddy taxed at 30%, finished the Grand Canal and raised all four Wall links in one year. He also paid half of every province's land, and the table reached 38 squares. Silke paid 111 for the last Wooden Bowl, one grain over Reina, and took Graham's Rice seat: "you wrote down your reason. I've written mine down too."

**Chapter 5, "An Awful Lot of Fair Dealing" (Year 9).** Only the Marble Pagoda was owed, and the Emperor's booklet requires it in any round nothing else is built. Paddy built it in the public-works step, which ended the game before the auctions where Reina could have bought the Bowl and taken the throne back.

## Verdicts

| Player | Drew | Ends | Result | Grain |
|---|---|---|---|---|
| Reina Osorio | Emperor (1) | Silk Peasant (5) | lost | 168 |
| Silke Weber | Silk Peasant (5) | Rice Peasant (6) | lost | 570 |
| Paddy Doyle | Rice Peasant (6) | Emperor (1) | won | 454 (the crown) |
| Graham Garner | Wheat Peasant (7) | Wheat Peasant (7) | held | 217.5 |

Four seat changes: Graham Wheat → Silk (Year 3), Paddy Rice → Silk (Year 4), Paddy Silk → throne (Year 6), Silke Wheat → Rice (Year 8).

## Against the scenario

- **Target arc: a peasant table that ends in survival. Met.** All 520 built by Year 9; nobody in debt at any point; no rewinds.
- **Whether a fair deck is enough. Yes, with room to spare.** The crown built a work in every one of the nine years. It finished three years before the second doubling (Year 12) and ten before ×6 (Year 19).
- **Land in proportion. Partly.** In the year land opened, the table bought land alongside a palace, as the tip said. But once Paddy paid half of every square, in Years 7 and 8, the peasants kept buying past what the next population card needed: 38 squares against roughly 20. It cost the outcome nothing (the Wall went up in the same year), but it's the "willy nilly" buying Manish had seen elsewhere, and a half subsidy is what set it off.
- **The works as the clock. Yes.** The game ended because the works were done, not because anyone agreed to stop.

## Steering

All logged in `seed.md`.
- **The deck:** seed 8535, Manish's choice from a shortlist of three (8535, 17152, 19860). See "The deck search" below.
- **Actor's notes:** written before Chapter 1 and rewritten before every later chapter, since every chapter changed a seat. Land was named only as one use of grain among several, and from Chapter 4 not at all.
- **Tips:** two in all. Year 1, to Reina, on the works owed. Year 5, to all four, on the rules of land, including that land is bought alongside the year's project and that the provinces may share a palace or the Wall.
- **Manish's direction in Chapter 4:** after Year 7's 12 squares, the Emperor should tell the table it had land enough, since steering is better done through the Emperor. A rewind was allowed. By then Year 8's land step was under way and the Wall had gone up in the same year, so the Director didn't rewind (Manish agreed) and gave Paddy that stance for Year 9. It didn't take: in his last crown turn Paddy again offered half of every square. The game ended in that step, so no square was bought.

## The deck search

`deck_scout.py` shows what a deck does to each year but not whether the works can be built. The Director wrote a scratch model, outside the repo, that plays a deck with a plain policy: tax, one project a year, land up to bad-harvest break-even once it opens, a crown in debt shutting land, and knobs for grain lost at auction, tax rate, the crown's reserve and lending. On seed 20261027, the two earlier games' deck, it stalls at 120–240 built, as both games did.

Of seeds 1–20000, about a fifth finish the works under a harsh policy. Most of those finish only because no population card arrives before Year 7, which would make a dull game. 721 have the doubling first in Years 4–6, fail without land and finish with it; five finished by Year 10 at every stress setting. 8535 was the safest of those.

The model was close on the timing (it predicted Year 9–10) but not on the land: it bought about 11 squares, while the table bought 38.

**Worth considering for the scout:** a "works finished by year N" measure, under a plain policy like the model's, would let a Director find decks like this without a scratch script. The scout is shared, so that's Manish's call.

## Rules findings

- **The last work ends the game at the moment it stands, before the auctions** (§18). With the Pagoda compulsory in any round nothing else is built, the Emperor who holds the throne when only the Pagoda is left can end the game, and win, in the public-works step. Here that cost Reina the throne: she needed one piece that would have come up at auction later that year. Nobody objected, and it's the rules as written, but it hands the ending to the sitting Emperor. If that's unwanted, a ruling could have the round finish, or the Pagoda go up last.
- **The Wall in one project.** All four links above Province 1 went up in one year (N13), 160 at once. Nothing wrong with it; it shows how fast a rich crown can finish.
- **A crown subsidy drives land.** Five a square (Year 5) and ten (Years 7–8) were both enough to make land the obvious buy for every peasant, past need.
- **No ruling needed during play.** The Storyteller's precedents are in the ledger.

## Tools

No shared tool was changed. For the guides (the Storytellers' notes, kept in the shared notes folder):
- **`build()` needs `key=` and `at=` for a palace or the Pagoda,** or `all_built()` doesn't count it.
- **`briefs.py ... launch --menu f --land` drops the land reminder;** `launch:free --menu f --land` keeps it.
- **After a seat change, salary keys are the appointee's new seat.** One salary went to the wrong seat in Year 4 and was corrected in the engine and the snapshot. The two diaries that quote the wrong figures stand word for word.
- **An en dash in a Bash command fails outright** in this shell; diary prompts and ledger edits went through Python files.
- **`sed -i` turned `game.py` LF;** the repo stores it LF, so no harm.
- **A prompt built too early** (twice) was caught before sending, deleted, and rebuilt with the player's `seen.json` index reset.
- **`briefs.py heard` strips a leading quote** from a say that starts with a quoted card name.

## Usage

| Chapter | 5-hour window | Weekly | Storyteller context, start → end |
|---|---|---|---|
| 1 (Years 1–2) | 14% → 16% | 30% → 31% | 112k → 271k |
| 2 (Years 3–4) | 16% → 18% | 31% | 116k → 303k |
| 3 (Years 5–6) | 19% → 21% | 31% → 32% | 108k → 380k |
| 4 (Years 7–8) | 21% → 24% | 32% → 33% | 136k → 345k |
| 5 (Year 9) | 25% → 26% | 33% | 115k → 187k |

The figures are for the whole account, so they include the other games running at the same time. Six Storytellers were parked; Chapter 6's was never needed.

## Continuity and drift

- **Voices held** through four seat changes. Paddy stayed earnest and kept every promise on three seats. Graham counted and wrote things down. Silke remembered and paid back. Reina managed, and praised the man who took her throne.
- **Grudges paid in kind.** Graham took Silke's seat in Year 3 over a Year 1 grudge; Silke took Graham's in Year 8 over Year 3, quoting him. Nobody fed the bit to anyone else.
- **Promises.** Every public promise was kept, including the Emperor's works promises and Paddy's salaries. The one whispered debt was repaid in public.
- **Safeguards.** None tripped. No agent was asked for its reasoning, and no transcript was read.
