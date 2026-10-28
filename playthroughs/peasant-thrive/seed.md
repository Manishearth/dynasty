# Chance and steering in Peasant thrive

The Director nudges this game towards the arc in `scenario.md`. Any steering is the Director's, made before the game or between chapters through a handoff, and is listed below when it happens. A Storyteller never steers on its own.

- **Seed:** `8535`, chosen by Manish on 2026-10-28.
- **How the deck is shuffled:** the twenty card keys from `cards.py`, sorted alphabetically, then `random.Random(8535).shuffle(keys)` (Python 3).
- **Deck order, top first** (Year 1 draws no card, so the first of these is Year 2's):

  1. repairs · 2. breach · 3. blight · 4. double1 · 5. share · 6. utility · 7. careless · 8. chest · 9. goodevil · 10. canal · 11. double3 · 12. dribble3 · 13. double2 · 14. heaven · 15. dribble2 · 16. winds · 17. dribble1 · 18. half1 · 19. half2 · 20. rainflood

  The players are never shown this list, and the narrator never hints at it. Population cards past their caps are still drawn in order; the engine treats a capped one as a good harvest.

- **Booklets:** not drawn by chance. Each player sits in the province their name puns on: Reina 1, Silke 5, Paddy 6, Graham 7.

## Why this deck

The two earlier peasant tables drew seed 20261027. On that deck:
- the population grew by half in Year 3, so land opened at ×3 with the Year 6 doubling, when every bare income was already negative under every card;
- bad harvests followed in Years 7, 9 and 10, which left no surplus to put into land;
- Province 1 needs six squares at ×3, and only the crown can buy them, but the crown's tax income had dried up, and a crown in debt shuts land for everyone;
- the third population card made it ×6 in Year 11, when the throne's province needs fifteen squares.

The pilot bought no land and collapsed in Year 8. The peasant's game bought land every year and was still about 18 squares short at Year 11; it stopped by agreement after Year 12 with 200 of 520 built.

**What matters is the order of the population cards.** With the doubling first, land opens at ×2, where a peasant needs one square to break even and the crown three, so a square bought then pays back while incomes are still positive.

**The search** (Director, 2026-10-28). `deck_scout.py` measures the deck but not whether the works get built, so the Director wrote a scratch model, outside the repo, that plays each deck with a plain policy: tax, one project a year (Reservoir, then the Canal, the palaces, the Wall), land bought up to bad-harvest break-even once it opens, and a crown in debt shutting land. It has knobs for grain lost to auctions (15–45% of positive income), tax (25–40%), the crown's reserve and lending. On seed 20261027 it stalls at 120–240 built, as both games did. Of seeds 1–20000, 721 have the doubling first in Years 4–6, fail without land and finish with it; five finished by Year 10 under every stress setting. Manish chose 8535 from the shortlist of 8535, 17152 and 19860.

**Seed 8535:** `deck_scout.py 8535 --seats 1,5,6,7 --years 14`

| Year | Card | × | Emperor | Peasants | Note |
|---|---|---|---|---|---|
| 1 | — | 1 | +60 | +60 | |
| 2 | repairs | 1 | +40 | +60 | good; the Emperor plays a disaster, 5–7 pay 2 |
| 3 | breach | 1 | +40 | +60 | good; 5–7 play a disaster, Province 1 pays 2 or 5 |
| 4 | blight | 1 | +15 | +35 | average |
| 5 | double1 | **2** | −20 | +20 | good; **land opens** |
| 6 | share | 2 | −45 | −5 | average; the Emperor's Share |
| 7 | utility | 2 | −45 | −5 | average; Utility Tax |
| 8 | careless | 2 | −20 | +20 | good; every player plays a disaster |
| 9 | chest | 2 | −45 | −5 | average; Imperial Charity |
| 10 | goodevil | 2 | −20 | +20 | good; Province 6 plays a disaster |
| 11 | canal | 2 | −45 | −5 | average; unfinished canal work lost; Province 7 plays a disaster |
| 12 | double3 | **4** | −140 | −60 | good; second doubling |
| 13 | dribble3 | 4 | −190 | −110 | bad |
| 14 | double2 | 4 | −140 | −60 | capped: a good harvest |

Bare income is harvest − consumption, before works, land and tax. No bad harvest until Year 13; the population reaches ×6 only in Year 19 (half1, card 18). The model finishes the works in Year 9–10 at every stress setting, and never finishes without land.

**What the table must do:** build steadily through Years 1–4 at ×1 (good harvests in Years 1–3); buy some land from Year 5, roughly three squares for Province 1 and one or two per peasant at ×2; and finish the works before Year 12's doubling, after which the throne's province needs about nine squares.

## Steering log

- **Before Chapter 1, the deck:** seed 8535 (Manish's choice, 2026-10-28), for the reasons above.
- **Before Chapter 1, the actor's notes:** the **Playing it** line in each `ledger.md` entry. Each is a stance in which land is one good use of grain among several (the works' bonuses, the climb, a reserve), since Manish has seen tables buy land "willy nilly" in other games and wants it kept in proportion. Reina a builder who means to see the works finished on her watch; Silke sharp and ambitious, who wants a throne worth having; Paddy earnest and careful with every grain; Graham counting what each grain brings back. No moves, numbers or results.
- **Steering planned:**
  - Chapter 1: one Storyteller's tip to Reina in Year 1, on the works owed (six projects, one a year, tax only on positive incomes).
  - Chapter 3: one tip to each player in Year 5, the year land opens: a square yields 20 a year from the next harvest; the board card shows the need; the crown may pay any part of a square; debt bars buying, and a crown in debt shuts land for everyone; and land is bought alongside the year's project, not instead of it.
  - No rewinds planned. If the works are far from done by the end of Year 10, the Director may offer an agreed stop before Year 12's card.
- **Chapters 1–2, as played:** Reina's works tip went out word for word in Year 1. No other steering. Two seat changes: Graham Wheat → Silk (Year 3), Paddy Rice → Silk (Year 4), so Silke is Wheat and Graham Rice. 240 built by the end of Year 4, 280 owed.
- **Before Chapter 3, all four actor's notes rewritten** for the new seats (`ledger.md`). Reina: still the builder, but her province is the hungriest and the crown no longer the richest purse, so she minds the reserve and will ask the provinces she watered to share the rest. Paddy: the richest player and one climb from the throne, who would rather his grain did some good, for his province or the table. Graham: counting and starting over, weighing a piece, a field or his new canals alike. Silke: sharp, two provinces from where she began, climbing back without sinking the table. Why: the old lines named the drawn seats (Graham's "the Reservoir in his own province"), and at ×2 from Year 5 the crown runs at about −45 in an average year while the peasants run positive, so the works left (280, the Wall above all) need the crown to husband its grain and the rich provinces to share. Stances only; land is named only as one use of grain among several.
- **Chapter 3, the land tip as planned,** to all four at once in Year 5, after the harvest and before Reina's crown prompt (`handoff/chapter-2.md`): what a square costs and yields, the crown's share and debt, land alongside the year's project, the provinces may share a palace or the Wall, and the board card's need. All rules any player can read.
- **Chapter 3, as played:** the tip went out word for word in Year 5. The table bought 13 squares that year and 6 more in Year 6 (19: Province 1 5, 5 4, 6 5, 7 5), with the crown paying 5 a square toward every province's. Mostly bought ahead of the next population card, alongside a palace and a canal section, not instead of them. Paddy took the throne in Year 6 with the Silk set; Reina is the Silk Peasant. 300 built, 220 owed.
- **Before Chapter 4, all four actor's notes rewritten** for the new seats. Paddy: an Emperor he never expected to be, who means his reign to finish what Reina started. Reina: the deposed Empress on the coast she watered, wanting the throne back and watching the new crown's spending. Silke: one piece from climbing back, and knowing who holds it. Graham: counting, holding the piece Silke needs, weighing a piece or a share in the works. Why: Paddy's and Reina's lines named their old seats. Land is no longer named in any note: at ×2 every province now runs positive in an average year, and Manish wants land kept in proportion, so the notes point at the works and the climbs. No tips this chapter.
- **During Chapter 4, Manish's direction (2026-10-28):** after Year 7's 12 squares, with every province already past what the next population card needs, the Emperor should tell the peasants not to spend more on land, and steering is better done through the Emperor's direction where possible. A rewind was allowed. **The Director's call: no rewind.** By the time the direction came, Year 8 was at its land step: Paddy had raised all four Wall links (160) in the same year as offering half of every square, so only the Pagoda is left and the game can end in Year 9. The extra squares (7 in Year 8, 38 in all) change nothing in the outcome, and replaying would need fresh agents for a cosmetic gain. Instead, Paddy's note for Chapter 5 will have him close the land offer out loud, as the Emperor's own judgment. Manish agreed to keep Year 8 as played.
- **Chapter 4, as played:** the Grand Canal finished (Year 7) and all four Wall links (Year 8); only the Pagoda owed. 38 squares. Silke bought the Bowl for 111 and replaced Graham as Rice (Year 8). Seats: Paddy 1, Reina 5, Silke 6, Graham 7.
- **Before Chapter 5, all four actor's notes rewritten.** Paddy: one work left; the table has land enough and the crown's grain belongs to finishing the reign, and he says so plainly (Manish's direction, through the Emperor). Reina: one piece from the throne, wanting the works finished but rather from the throne. Silke: the richest at the table, two pieces from Silk, knowing a purse buys nothing after the game. Graham: back in the Wheat seat he drew, empty-shelved. No tips. **The ending as the rules stand:** the Emperor's booklet requires the Pagoda in any round nothing else is built, and nothing else is owed, so Year 9's public-works step should end the game in survival, before the auctions where Reina could buy the Bowl. Only a revolt that stands (Chaos bars works) could stop it, and only if the players raise it. The handoff puts the rule to the Storyteller as written and suggests nothing.
- **Chapter 5, as played (the end):** a rule note quoted the Pagoda rule to Paddy before his crown prompt. He taxed 30%, offered half of every square again (his note's stance on land didn't take), and built the Pagoda. The game ended in survival in Year 9's public-works step; nobody raised a revolt. Paddy won, Graham held, Silke and Reina lost.
