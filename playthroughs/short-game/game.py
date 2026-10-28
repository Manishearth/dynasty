# The short game: an agent-played game of Dynasty. Scenario and steering: scenario.md; deck: seed.md.
# Every say and aside is the reply of the agent playing that seat (see log/yearN/).
# The Storyteller writes the act lines and refs the moves; the engine keeps the books.
# The narrator's lines are not part of the game: they live in narration.md, never here.
# Each chapter opens with a "# ===== CHAPTER N: <title>" marker.
setup([1, 2, 3, 4], "short-game", "The short game",
      "Four players · eight rounds · in progress",
      "The Emperor and the three upper provinces, and the table agrees to stop after eight rounds. No Warlord, no peasants: a race for the throne.",
      short="4 players · 8 rounds")

# ============================== SETUP ==============================
R(0, "Setup", None, "Four players: the Emperor, the Official, the Gentry and the Scholar (rulebook Section 4 and Appendix A). No Warlord, so nobody raids and no soldiers are sold; no peasants, so no rent, and nothing is owed to Provinces 5, 6 or 7. The table agrees to the short game: eight rounds, then score from where everyone sits (Note 19). Each realia province holds one piece of its own realia and two of the one type it never needs.")
act("Four booklets: Reina Osorio draws the Emperor, Clark Grafton the Official, Richard Baron the Gentry and Noah Tall the Scholar.", map_hl=[1,2,3,4])
act("The table agrees to stop after eight rounds and score from where everyone sits.", map_hl=[1,2,3,4])
deal_grain("Rich, the Gentry, sets out the Harvest Pile and deals 60 to each player. It is the first year's harvest.")
take_stock("Clark, Rich and Noah take their realia out of the box: one piece of their own and two of the type they'll never need. It waits beside the board until it's sold.")
act("Clark cuts out the Province 2 Irrigation System, one square by two; Rich the Province 3 Reservoir, two by three. They're set aside until built.", map_hl=[2,3])
act("Noah, the Scholar, shuffles the twenty I Ching cards and lays them face down.", map_hl=[4])
# From here the players' own choices.

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 each player was dealt is the first harvest, and the tax is levied on it.")
