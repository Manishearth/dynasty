# Chance in the full game

No pre-steering (Manish, before Chapter 1): the deck is shuffled, not stacked, and no story beats are planned. Manish then allowed some steering "to make the story fun and interesting", at the Director's judgement, during the game. Any steering is the Director's, made between chapters through a handoff, and is listed here when it happens. A Storyteller never steers on its own.

## Steering log

- **From Chapter 4 (Year 7), Manish:** the Storyteller may nudge players with good strategy advice. Each tip is a public `note --to <Player>` beginning "Storyteller's tip:", using only what the table can see; at most one per player per chapter; never the deck order, nor anyone's asides, whispers or limits. Every tip is listed in `ledger.md` under "Storyteller's tips" (rules in `handoff/chapter-3.md`).
- **Year 13 replayed, Manish:** the first take, where the table bought 520 of land in the year the last work could end the game and the crown ended in debt with the work unbuilt, was set aside to `outtakes/year13-first-take/`, and the year is replayed from the end of Year 12 with the same deck. From the replay on, the tools tell every player plainly when the game can end this year or next, that new land pays only from next year's harvest, and that a crown in debt can't pay for a work (`briefs.py`, `endgame_note`).
- **A ruling, not steering (Manish, after the Year 13 replay):** the crown may build a negotiated work alone if it pays the whole cost. A province can refuse its share, but can't veto the work (RULINGS). In the replay the Official had refused the last work so that the game wouldn't end.
- **Year 13 replayed a second time, Manish:** the second take was set aside to `outtakes/year13-second-take/`, and the year is replayed again from the end of Year 12, with the crown-builds-alone ruling announced at its start.

- **Seed:** `19691108`.
- **How the deck was shuffled:** the twenty card keys from `cards.py`, sorted alphabetically, then `random.Random(19691108).shuffle(keys)` (Python 3).
- **Deck order, top first** (Year 1 draws no card, so the first of these is Year 2's):

  1. dribble1 · 2. winds · 3. careless · 4. share · 5. breach · 6. chest · 7. heaven · 8. dribble3 · 9. repairs · 10. half2 · 11. double2 · 12. dribble2 · 13. double3 · 14. double1 · 15. goodevil · 16. blight · 17. rainflood · 18. utility · 19. canal · 20. half1

  So Year N draws card N−1: Year 2 dribble1, Year 3 winds, … Year 11 half2, Year 12 double2.

  The players are never shown this list, and the narrator never hints at it. Population cards past their caps are still drawn in order; the engine treats a capped one as a good harvest.

- **Booklets:** not drawn by chance. All eight sit in the province their name puns on: Reina 1, Clark 2, Rich 3, Noah 4, Silke 5, Paddy 6, Graham 7, Rob 8.
