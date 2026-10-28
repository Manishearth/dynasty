# Chance and steering in All's Quiet on the Western Front

The Director nudges this game towards the arc in `scenario.md`. Any steering is the Director's, made before the game or between chapters through a handoff, and is listed below when it happens. A Storyteller never steers on its own.

- **Seed:** `74`, recommended in `scenario.md` and confirmed by the Director before Chapter 1 (see the steering log).
- **How the deck is shuffled:** the twenty card keys from `cards.py`, sorted alphabetically, then `random.Random(74).shuffle(keys)` (Python 3).
- **Deck order, top first** (Year 1 draws no card, so the first of these is Year 2's):

  1. blight · 2. utility · 3. double2 · 4. dribble2 · 5. goodevil · 6. heaven · 7. half2 · 8. dribble1 · 9. double3 · 10. breach · 11. double1 · 12. rainflood · 13. canal · 14. chest · 15. half1 · 16. share · 17. dribble3 · 18. careless · 19. repairs · 20. winds

  The players are never shown this list, and the narrator never hints at it. Population cards past their caps are still drawn in order; the engine treats a capped one as a good harvest.

- **Booklets:** not drawn by chance. Each player sits in the province their name puns on: Reina 1, Clark 2, Rich 3, Noah 4, Silke 5, Paddy 6, Graham 7.

## Steering log

- **Before Chapter 1, the deck:** seed 74 stands. `deck_scout.py 74 --seats 1,2,3,4,5,6,7 --years 10`: average harvests in Years 2–3 (+35 bare for 2–7, +15 for the Emperor), so there are two years to buy pieces before anything bites. ×2 arrives in Year 4 (land opens), followed by a bad harvest in Year 5 (every seat −30 or worse), Good and Evil in Year 6 (disasters for 2, 4, 6), Heaven Has Favourites in Year 7 (bad for 1, 3, 6, 7, good for 2, 4, 5), ×3 in Year 8, a bad harvest in Year 9 and ×6 in Year 10. Only three personal disasters in ten years. Bare income goes negative from Year 4 and stays there, so land bought in Years 4–7 pays and a province without it slides. That is the slow grain squeeze the arc needs.
  - The alternatives were scouted and set aside. **10** goes to ×4 in Year 5 and stays −60 or worse for every seat: too fast for two climbs. **113** opens land only in Year 5, at ×3, and has three lean years after that. **116** is at ×3 by Year 4, and every seat plays a disaster in Year 3 or 6, which is chance doing the arc's work.
- **Before Chapter 1, the actor's notes:** each `ledger.md` entry's **Playing it** line, a stance taken from `scenario.md`'s suggestions:
  - Reina favours the loyal with the crown's land money;
  - Rich is a landlord who means the rent to rise with the land;
  - Silke knows every other set needs one of her Jars, and hers needs none;
  - Clark has a price;
  - Noah keeps his word and says the arithmetic out loud;
  - Paddy would sooner own than owe;
  - Graham climbs patiently, one rung at a time.

  None gives a move, a number or a result.
- **Manish, before Chapter 1:** the arc has few story beats, so let the game proceed however it goes. Steering stays light: the notes, and tips only where the plan below calls for them. Then, also from Manish: the Director judges the levers chapter by chapter and tries to keep the game interesting. He has a small preference for a satisfying ending over a table that's simply stuck, but not a large one. The likely levers:
  - re-notes that follow whoever climbs, and whoever they displace;
  - the climb-ladder tip;
  - a hold-back tip to Silke;
  - the cheapest-set tip if nobody has climbed by Year 6.

  The rent, revolts and debt are left alone.
- **Before Chapter 2 (after Year 2), the actor's notes:**
  - Noah, now Emperor: the fairest sovereign, who keeps every promise and knows the crown may fund land.
  - Reina, now Scholar: the deposed Empress, working back to the chair on a thin purse.
  - Graham: "buys when a thing is cheap" became "pays what a piece really costs at this table". Nothing has been cheap, and none of the peasants has won any of the twelve lots, so the old wording held him back from the climb.

  Silke, Paddy, Clark and Rich are unchanged.
- **Before Chapter 2, one tip, to Silke, in her Year 3 auctions prompt** (public; everything in it is on the board): twelve lots, no peasant has won one; a peasant's set can replace the Official, Gentry or Scholar, not the Emperor; and at the end of Year 2 the Scholar's seat was held by the poorest player. **Why:** the arc needs a peasant to climb. The peasants hold nothing, and the board card's ladder alone hasn't moved them. The Scholar seat (Reina, 40) is the cheapest rung to take, and the table can see that.
- **Before Chapter 3 (after Year 4), the actor's notes:** new lines for the four who changed seats in Year 4's auction:
  - Clark: an Emperor who treats every grain the crown spends as a favour to be repaid.
  - Rich: the fallen landlord, an Official openly for sale (the booklet's bribable Official).
  - Reina: twice an Empress, now the Gentry, setting the rent by loyalty. This tests the Gentry's rent as a weapon.
  - Noah: back on the Scholar's stool, keeping his old promises.

  The peasants are unchanged.
- **Before Chapter 3, one conditional tip:** at the start of Year 6's auctions, if no peasant has changed seats, the peasant holding the most pieces gets a public tip. It says: a peasant's set replaces the Official, Gentry or Scholar, and the climber keeps the displaced player's grain; the board card shows what those three hold. **Why:** after Year 4 the peasants (Paddy and Graham, two pieces each) are the furthest along, but nobody has said aloud that a climb takes the displaced player's grain. The tip uses only the rules and the board.
- **Year 6: the arc happened without a tip.** Graham climbed Wheat → Scholar (Year 5) → Emperor (Year 6). Paddy climbed Rice → Official → Emperor within the Year 6 auction, then lost the throne to Graham. The conditional Year 6 tip lapsed.
- **Before Chapter 4 (after Year 6), the actor's notes:** new lines for the five who changed seats: Graham (Emperor), Clark (Official again), Paddy (Scholar), Rich (Rice) and Noah (Wheat). Silke and Reina are unchanged.
- **Before Chapter 4, one tip, to Graham, in his Year 7 crown prompt:** the 690 owed, as five projects, so the earliest survival ending is Year 11. **Why:** Manish prefers, slightly, a game that ends satisfyingly over a stuck one. The deck reaches ×6 in Year 10, so the table needs to see early how long the works will take. All public arithmetic.
- **Year 7:** Graham's tip given as briefed. Silke climbed Silk → Gentry without a tip.
- **Before Chapter 5 (after Year 8), the actor's notes:** new lines for Reina (now Silk Peasant: the richest harvest and the last Jars) and Silke (now Gentry, one set from the throne). The others are unchanged.
- **Before Chapter 5, one conditional tip:** if Year 9 builds no work, Year 10's Emperor gets a public tip that the Province 2 Irrigation, Province 3 Reservoir and Province 4 canal are negotiated works the province may pay for in full. **Why:** the crown has been at 0.5 two years running, and ×6 arrives in Year 10. The tip keeps the ending reachable without telling anyone what to do. It's only the rules.
- **Year 9:** the conditional tip lapsed, since the Province 6 canal was built. Chapter 5 closed at Year 9 for context. Noah climbed Wheat → Scholar → Emperor in one auction, the second peasant to climb twice to the throne.
- **Before Chapter 6 (after Year 9), the actor's notes:** new lines for Noah (Emperor), Silke (Scholar), Graham (Gentry) and Paddy (Wheat). The others are unchanged.
- **Before Chapter 6, one tip, to Noah, in his Year 10 crown prompt:** the 290 owed, as four projects, so the earliest survival ending is Year 13. **Why:** the same as Graham's Year 7 tip, updated (that one's Year 11 assumed the Wall in one year). It keeps the ending in view at ×6.
- **Provisional rules reading (Director, Year 9), awaiting Manish:** if the Harvest Pile can't pay a harvest, it pays in full and goes below zero as its own debt. Year 10 can be replayed from `state/year9.json` if Manish rules otherwise. **Settled after the game (2026-10-28):** the 2,500 cap is the engine's assumption, not a rule (§8 only lists the bags), and Manish said "I think we don't need a ruling here, so this game is done". Years 10–13 stand.
- **Year 10:** Noah's tip given as briefed. **Year 11:** the provisional Pile reading was extended to a displaced player's 60 draw, which wasn't needed in the end (the Pile was positive at the seat change).
- **Before Chapter 7 (after Year 11), the actor's notes:** new lines for Rich (back on the throne), Reina (Rice) and Graham (holding a complete set). No tips in the last chapter.
- **Steering planned:** no tips in Chapter 1. From Chapter 2 (Years 3–4, when land opens), at most one public Storyteller's tip per player per chapter, from what the table can see. The climb ladder (a peasant needs an upper-class seat before the throne) and the hold-back rule are the likely ones. If no peasant holds an upper-class seat by Year 6, a tip on the cheapest upper-class set is fair. Every tip is logged here when it's given.
