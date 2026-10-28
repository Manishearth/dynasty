# Chance and steering in the peasant rematch

The Director nudges this game towards the arc in `scenario.md`. Any steering is the Director's, made before the game or between chapters through a handoff, and is listed below when it happens. A Storyteller never steers on its own.

- **Seed:** `20261027`, recommended in `scenario.md`. **The Director confirms it, or picks another with `deck_scout.py` and rewrites this section, before Chapter 1.**
- **How the deck is shuffled:** the twenty card keys from `cards.py`, sorted alphabetically, then `random.Random(20261027).shuffle(keys)` (Python 3).
- **Deck order, top first** (Year 1 draws no card, so the first of these is Year 2's):

  1. canal · 2. half2 · 3. dribble2 · 4. half1 · 5. double1 · 6. dribble3 · 7. share · 8. dribble1 · 9. heaven · 10. double3 · 11. goodevil · 12. blight · 13. careless · 14. utility · 15. rainflood · 16. repairs · 17. double2 · 18. winds · 19. breach · 20. chest

  The players are never shown this list, and the narrator never hints at it. Population cards past their caps are still drawn in order; the engine treats a capped one as a good harvest.

- **Booklets:** not drawn by chance. Each player sits in the province their name puns on: Reina 1, Silke 5, Paddy 6, Graham 7.

## Steering log

- (none yet)
