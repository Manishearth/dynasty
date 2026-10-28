# Chance and steering in the short game

The Director nudges this game towards the arc in `scenario.md`. Any steering is the Director's, made before the game or between chapters through a handoff, and is listed below when it happens. A Storyteller never steers on its own.

- **Seed:** `39`, recommended in `scenario.md` and confirmed by the Director before Chapter 1.
- **How the deck is shuffled:** the twenty card keys from `cards.py`, sorted alphabetically, then `random.Random(39).shuffle(keys)` (Python 3).
- **Deck order, top first** (Year 1 draws no card, so the first of these is Year 2's):

  1. share · 2. heaven · 3. breach · 4. utility · 5. double3 · 6. dribble3 · 7. half2 · 8. canal · 9. double1 · 10. chest · 11. repairs · 12. dribble2 · 13. goodevil · 14. rainflood · 15. careless · 16. winds · 17. blight · 18. half1 · 19. dribble1 · 20. double2

  The players are never shown this list, and the narrator never hints at it. Population cards past their caps are still drawn in order; the engine treats a capped one as a good harvest.

- **Booklets:** not drawn by chance. Each player sits in the province their name puns on: Reina 1, Clark 2, Rich 3, Noah 4.

## Steering log

- **Before Chapter 1, the deck:** seed 39 stands. `deck_scout.py` on 39, 15, 38 and 80 (seats 1–4, 8 years): 39 is the only one that reaches ×3 by Year 8 (doubles in Year 6, grows by half in Year 8), so the last two rounds are the hungry ones and every seat's bare income is negative in Years 7–8. Its Year 3 card (Heaven Has Favourites) gives the Emperor and the Gentry a bad harvest and the Official and the Scholar a good one, which opens a gap early without settling anything. One personal disaster (the Scholar's, Year 4). The others stop at ×2, and 80 has three disasters and two lean years early.
- **Before Chapter 1, the actor's notes:** the **Playing it** line in each `ledger.md` entry, a stance for each character (`scenario.md`'s suggestions). At four players each seller's own piece is the only one in the game, and both rivals need it.
- **Before Chapter 1, the ending:** `game.py` sets `LAST_ROUND = 8`, so every prompt's board card gives the round count and the Note 19 scoring, and the land notes in Years 7–8 say a square can't pay back in time. Each Storyteller says the count at the table when its chapter opens.
- **Before Chapter 3, the actor's notes:** Reina's and Clark's **Playing it** lines are rewritten for their new seats (Clark took the throne in Year 3). Reina is now the deposed Empress working her way back; Clark is an Emperor who uses the tax, the works and the reserve as leverage. Rich's and Noah's are unchanged.
- **Before Chapter 3, one Storyteller's tip, to Rich (Year 5):** the Deed is the one piece Noah still needs, and Reina needs it too; its seller sets the minimum, and an unmet lot must go up again next year at 2. Why: Noah was one piece from a set with the Deed forced up in Year 5, and the arc wants the throne race open past Year 5. The tip states only what the table can see and the rules (`scenario.md`: a blocking tip is fair game if one player runs away).
- **Chapter 3, Year 5, the tip as given:** sent word for word as a `note --to Rich` before his piece prompt (057). Rich set the Deed at 95; Noah, the only bidder able to meet it, paid it and completed his set, then replaced Reina as the Official rather than take the throne.
- **Before Chapter 4:** Rich's **Playing it** line is rewritten, since his Scroll is sold ("keeping a hand on whatever piece his rivals still need"). No tips in the last chapter: the race is open, with the Customs House and the Bowl at 2 in Year 7, and every auction prompt already says who needs each lot. The Storyteller says at the table, before Year 7, that these are the last two rounds (Note 19).
- **After the game (not steering):** in Year 8 the Storyteller gave its standing correction of a public misstatement of the rules. Noah had said a set could only come from the auctions, and the correction said pieces on the board may be traded. The deciding trade followed. See `REPORT.md`, "Steering".
