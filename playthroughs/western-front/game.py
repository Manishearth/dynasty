# All's Quiet on the Western Front: an agent-played game of Dynasty. Scenario and steering: scenario.md; deck: seed.md.
# Every say and aside is the reply of the agent playing that seat (see log/yearN/).
# The Storyteller writes the act lines and refs the moves; the engine keeps the books.
# The narrator's lines are not part of the game: they live in narration.md, never here.
# Each chapter opens with a "# ===== CHAPTER N: <title>" marker.
setup([1, 2, 3, 4, 5, 6, 7], "western-front", "All's Quiet on the Western Front",
      "Seven players · no Warlord · in progress",
      "Seven players and no Warlord: no raids, no soldiers, nobody in the desert. Everything is fought over with grain instead.",
      short="7 players")

# ============================== SETUP ==============================
R(0, "Setup", None, "Seven players: all seven provinces and no Warlord (rulebook Section 4, Note 2 and Appendix A). No raids and no soldiers, so this is the pure economic game. Every province holds four pieces of its own realia, and every public work in the book is owed.")
act("Seven booklets: Reina Osorio draws the Emperor, Clark Grafton the Official, Richard Baron the Gentry, Noah Tall the Scholar, Silke Weber the Silk Peasant, Paddy Doyle the Rice Peasant and Graham Garner the Wheat Peasant.", map_hl=[1,2,3,4,5,6,7])
act("The Warlord's booklet goes back in the box, with the soldiers and the raid squares. Seven players is the one game with no Warlord (Note 2).")
deal_grain("Rich, the Gentry, sets out the Harvest Pile and deals 60 to each player. It is the first year's harvest.")
take_stock("Each of the six realia provinces takes its four pieces of its own realia out of the box. They wait beside the board until they're sold.")
act("Clark cuts out the Province 2 Irrigation System, one square by two; Rich the Province 3 Reservoir, two by three; Graham the Province 7 Reservoir, two by two. They're set aside until built.", map_hl=[2,3,7])
act("Noah, the Scholar, shuffles the twenty I Ching cards and lays them face down.", map_hl=[4])
# From here the players' own choices.

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 each player was dealt is the first harvest, and the tax is levied on it.")
