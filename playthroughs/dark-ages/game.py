# The Dark Ages: an agent-played game of Dynasty. Scenario and steering: scenario.md; deck: seed.md.
# Every say and aside is the reply of the agent playing that seat (see log/yearN/).
# The Storyteller writes the act lines and refs the moves; the engine keeps the books.
# The narrator's lines are not part of the game: they live in narration.md, never here.
# Each chapter opens with a "# ===== CHAPTER N: <title>" marker.
setup([1, 2, 3, 5, 6, 8], "dark-ages", "The Dark Ages",
      "Six players · in progress",
      "Six players. The population doubles in the third year and the harvests fail. The table revolts, and nobody can win the acclamation for a while.",
      short="6 players")

# ============================== SETUP ==============================
R(0, "Setup", None, "Six players: the Emperor, the Official, the Gentry, the Silk and Rice Peasants and the Warlord (rulebook Section 4 and Appendix A). No Scholar, so the Emperor appoints someone to read I Ching and count the population, at the Scholar's salary of 5 (Note 3). Each realia province holds two pieces of its own realia, and each collector needs one from each of the other three. The Warlord starts with two soldiers.")
act("Six booklets: Reina Osorio draws the Emperor, Clark Grafton the Official, Richard Baron the Gentry, Silke Weber the Silk Peasant, Paddy Doyle the Rice Peasant and Robert Land the Warlord.", map_hl=[1,2,3,5,6,8])
deal_grain("Rich, the Gentry, sets out the Harvest Pile and deals 60 to each player. It is the first year's harvest.")
take_stock("Clark, Rich, Silke and Paddy each take two pieces of their own realia out of the box. They wait beside the board until they're sold.")
act("Clark cuts out the Province 2 Irrigation System, one square by two; Rich the Province 3 Reservoir, two by three. They're set aside until built. Nobody sits in Provinces 4 or 7, so nothing is owed there.", map_hl=[2,3])
# Reina's first prompt: who reads I Ching (then the shuffle). Rob's first prompt: his two soldiers (place_army) and his tax stance.

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 each player was dealt is the first harvest, and the tax is levied on it.")
