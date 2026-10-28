# The peasant's game: an agent-played game of Dynasty. Scenario and steering: scenario.md; deck: seed.md.
# Every say and aside is the reply of the agent playing that seat (see log/yearN/).
# The Storyteller writes the act lines and refs the moves; the engine keeps the books.
# The narrator's lines are not part of the game: they live in narration.md, never here.
# Each chapter opens with a "# ===== CHAPTER N: <title>" marker.
setup([1, 5, 6, 7], "peasant-game", "The peasant's game",
      "Four players · in progress",
      "The Emperor and the three peasants, no Warlord, and the same deck that ruined the last peasant table. This time the rulebook tells them to buy land early and ahead.",
      short="4 players")

# ============================== SETUP ==============================
R(0, "Setup", None, "Four players: the Emperor and the three peasants (rulebook Section 4 and Appendix A). No Warlord, so nobody raids and no soldiers are sold. No Official, Gentry or Scholar, so nobody collects rent, and the Emperor appoints a banker for the Harvest Pile, a tax collector and someone to read I Ching and count the population, at the Scholar's salary of 5 (Note 3). Nothing is owed to Provinces 2, 3 or 4. Each realia province holds one piece of its own realia and two of the one type it never needs. With no upper class at the table, the Silk Peasant stands in for it: a Silk Peasant who completes the objective may take the throne (Section 11).")
act("Four booklets: Reina Osorio draws the Emperor, Silke Weber the Silk Peasant, Paddy Doyle the Rice Peasant and Graham Garner the Wheat Peasant.", map_hl=[1,5,6,7])
deal_grain("Reina sets out the Harvest Pile and deals 60 to each player. It is the first year's harvest.")
take_stock("Silke, Paddy and Graham take their realia out of the box: one piece of their own and two of the type they'll never need. It waits beside the board until it's sold.")
act("Graham cuts out the Province 7 Reservoir, two squares by two, and sets it aside until it's built.", map_hl=[7])
# Reina's first prompt: her three appointments (banker, tax collector, I Ching reader at 5 a year), then the shuffle.

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 each player was dealt is the first harvest, and the tax is levied on it.")
