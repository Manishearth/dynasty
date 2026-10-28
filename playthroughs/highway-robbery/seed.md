# Chance and steering in Highway Rob-bery

The Director nudges this game towards the arc in `scenario.md`. Any steering is the Director's, made before the game or between chapters through a handoff, and is listed below when it happens. A Storyteller never steers on its own.

- **Seed:** `297`, recommended in `scenario.md`. **The Director confirms it, or picks another with `deck_scout.py` and rewrites this section, before Chapter 1.**
- **How the deck is shuffled:** the twenty card keys from `cards.py`, sorted alphabetically, then `random.Random(297).shuffle(keys)` (Python 3).
- **Deck order, top first** (Year 1 draws no card, so the first of these is Year 2's):

  1. rainflood · 2. dribble1 · 3. share · 4. chest · 5. double1 · 6. careless · 7. dribble2 · 8. double2 · 9. double3 · 10. utility · 11. blight · 12. canal · 13. heaven · 14. winds · 15. half2 · 16. dribble3 · 17. breach · 18. half1 · 19. goodevil · 20. repairs

  The players are never shown this list, and the narrator never hints at it. Population cards past their caps are still drawn in order; the engine treats a capped one as a good harvest.

- **Booklets:** not drawn by chance. Each player sits in the province their name puns on: Reina 1, Clark 2, Rich 3, Silke 5, Paddy 6, Rob 8.

## Steering log

- (none yet)
