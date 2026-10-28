# Peasant thrive: an agent-played game of Dynasty. Scenario and steering: scenario.md; deck: seed.md.
# Every say and aside is the reply of the agent playing that seat (see log/yearN/).
# The Storyteller writes the act lines and refs the moves; the engine keeps the books.
# The narrator's lines are not part of the game: they live in narration.md, never here.
# Each chapter opens with a "# ===== CHAPTER N: <title>" marker.
setup([1, 5, 6, 7], "peasant-thrive", "Peasant thrive",
      "Four players · in progress",
      "The Emperor and the three peasants again, no Warlord, on a fresh deck.",
      short="4 players")

# ============================== SETUP ==============================
R(0, "Setup", None, "Four players: the Emperor and the three peasants (rulebook Section 4 and Appendix A). No Warlord, so nobody raids and no soldiers are sold. No Official, Gentry or Scholar, so nobody collects rent, and the Emperor appoints a banker for the Harvest Pile, a tax collector and someone to read I Ching and count the population, at the Scholar's salary of 5 (Note 3). Nothing is owed to Provinces 2, 3 or 4. Each realia province holds one piece of its own realia and two of the one type it never needs. With no upper class at the table, the Silk Peasant stands in for it: a Silk Peasant who completes the objective may take the throne (Section 11).")
act("Four booklets: Reina Osorio draws the Emperor, Silke Weber the Silk Peasant, Paddy Doyle the Rice Peasant and Graham Garner the Wheat Peasant.", map_hl=[1,5,6,7])
deal_grain("Reina sets out the Harvest Pile and deals 60 to each player. It is the first year's harvest.")
take_stock("Silke, Paddy and Graham take their realia out of the box: one piece of their own and two of the type they'll never need. It waits beside the board until it's sold.")
act("Graham cuts out the Province 7 Reservoir, two squares by two, and sets it aside until it's built.", map_hl=[7])
act("Reina hands out the table jobs of the empty seats for the whole game: Graham Garner banks the Harvest Pile and pays out every harvest, Silke Weber collects the tax, and Paddy Doyle reads the I Ching card each year and keeps the population counter, for the Scholar's 5 a year from the crown.", map_hl=[1,5,6,7])
say("Reina", "Right, one job each, so nobody can say the crown has favourites. Graham, you hold the Harvest Pile and pay it out fairly. Silke, you bring the tax in honestly. Paddy, you read the I Ching, and the crown pays you five a year so the cards stay kind to all of us. Ten years is a long time, friends, and I mean to see the Wall finished with every one of you still at the table.",
 "Reina: Giving each peasant a job means each has a stake in the order holding, and the five a year to Paddy is cheap insurance on the man who keeps the population counter. Five out of sixty hurts a little now, but a revolt costs far more than that.")
act("Paddy shuffles the I Ching deck and sets it face down. The first card is turned in Year 2.", map_hl=[6])

# ===== CHAPTER 1: Three Deals Honoured at One Table
# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 each player was dealt is the first harvest, and the tax is levied on it.")
CUR_INC.update({s:60 for s in ACTIVE})
say("Reina", "Thirty percent, friends: fair on a good year and nothing that pinches. The first thing the crown builds is the Reservoir in Province 7, because a work that feeds people pays for itself. Graham, enjoy the water. Palaces can wait a year, and so can my vanity.",
 "Reina: Fifty-four comes in, sixty goes on the Reservoir and five to Paddy, which leaves me forty-nine. The extra twenty a year in Graham's harvest is taxable for the rest of the game, so the crown earns it back. Next year the Winter Palace, to open the canals for Silke and Paddy.")
taxes(.30, collector="Silke collects the tax for the crown")
build("Province 7 Reservoir", 60, {1:60}, key="res7", at="O16:P17", text="Public works: Reina builds the Province 7 Reservoir, two squares by two, on O16 to P17, and the crown pays the whole 60. It adds 20 to Graham's harvest from next year.", hover="The 60 goes into the Harvest Pile. 460 of the works are still owed.")
say("Silke", "A Customs House, friends, and the coast keeps its books honest. Four to open. Cheap, for the piece that tells you what everyone else is moving.",
 "Silke: I've got two of these and one Jar, so the Customs House goes first and I keep the rare piece back until the table's hungrier for it. I'm keeping the opening low because what I want is grain in my hand, not a lot that sits unsold and has to go up again next year at two.")
say("Paddy", "Thank you, Reina, I'll read the cards straight, whatever they say. I'm putting up a Bamboo Brush, starting at four, same as Silke. I've two of them, so whoever misses this one gets another go next year.",
 "Paddy: I'm selling a brush first because I have two of them to get rid of, and I'm keeping the single Wooden Bowl back in case somebody turns out to really want it. I'm watching Silke. She opened at four, and I'd like to see what she pays for things before I spend a grain of my own.")
say("Graham", "Thank you for the water, Reina. I'll keep the Harvest Pile to the last grain, and you can count it after me any time you like. I'm putting up a Land Deed Scroll at four, same as my neighbours. Land is what this game ends up being about, so it seems fair to sell the paper for it early.",
 "Graham: I've got two Scrolls and only one Vase, so the Scroll goes first, the way Silke and Paddy each led with the piece they have two of. Every one of us has a piece the others need, so I'll watch what they pay for theirs before I decide what mine is worth.")
act("The auctions. Each seller holds two types beside the board and chooses which goes up: Silke a Customs House, Paddy a Bamboo Brush and Graham a Land Deed Scroll, each with a minimum of 4. Silke keeps the Dragon Jar back, Paddy the Wooden Bowl and Graham the Vase. The Emperor doesn't bid.", map_hl=[5,6,7])
lot(5, "CH", [
 B(7, 7, "Each of these pieces has another copy behind it, friends, so I won't bleed the table for any of them. Seven's my limit, no further. Paddy, if you'd rather not race me on the Customs House, take this one cheap and leave me first go at next year's. I'll say the same to Silke about the Brush.",
   "Graham: Three quarters of every grain bid goes into the pile and doesn't come back, so a war over a piece with two more copies behind it just makes us all poorer. I'll pay a fair price, and if someone outbids me I'll wait for the next copy."),
 B(6, 8, "There are two of everything here, friends, so there's no need to bleed each other dry. Here's an offer for the whole table: Graham, if you take this Customs House cheap, I'll stay out of it and have the second one next year. Silke, if you let me have this Land Deed, I'll stay out when Graham's second one comes up. If you'd rather bid, that's fine too, but I won't go far.",
   "Paddy: Every grain we throw at each other goes to the Harvest Pile, so I'm offering to split the two pairs fairly instead of fighting. I'm keeping my ceilings low because I still have to buy the Jar and the Vase and keep twenty grain back, and I'd rather wait a year for a piece than overpay for it."),
 B(7, None, "Fine, it's yours. I'll be waiting for the next one.")],
 hover=TH(("", "Graham's limit was 7, Paddy's 8."),
          ("Paddy", "It goes on Q19.")), at="Q19")
lot(6, "BB", [
 B(7, 7),
 B(5, 8, "There are two of each, friends, so let's not bleed the Harvest Pile over the first one. Graham, if you want this Brush badly, take it and I'll have the second next year. Paddy, the same goes for the Deed. If not, I'll go to eight and no further.",
   "Silke: I need both of these, but each one has a twin coming, so a war over the first copy is grain thrown into the Pile. I've capped myself at eight so I keep a cushion for tax and for land once the population doubles."),
 B(7, None)],
 hover=TH(("", "Graham's limit was 7, Silke's 8."),
          ("Silke", "It goes on P26, in the corner of the coast.")), at="P26")
lot(7, "LD", [
 B(5, 8), B(6, 9),
 B(5, None, "Fine, it's yours. The second one has my name on it.")],
 hover=TH(("", "Silke's limit was 8; Paddy would have gone to 10."),
          ("Paddy", "It goes on Q20, beside the Customs House.")), at="Q20")
say("Paddy", "Well, I didn't expect to win both of those, so thank you, both of you, and sorry it cost more than any of us wanted. Next year's Customs House is Graham's and next year's Deed is Silke's. I've got mine now, so I'll stay out of both, as I said I would.",
 "Paddy: That's two of my four pieces in the first year, which I didn't expect, but it cost me seventeen and I've only got twenty-seven grain left. Now I have to be careful with every grain until the Dragon Jar and the Vase come up.")
say("Silke", "The Brush goes down on the coast, tucked in the corner where nobody's going to build over it. Paddy, you'll have the Deed, and I'm holding you to it: Graham's second one is mine.",
 "Silke: I've put it in the far corner so it stays out of the way of any public works and leaves my open squares free for land later. Paddy beat me to the Deed by one grain, so I'll be watching that second copy closely.")
salaries({6:5}, text="Reina pays Paddy 5 for reading the I Ching, the Scholar's salary.", hover="Nobody else at this table is on a salary.")

# ============================== YEAR 2 ==============================
R(2, "Storms and raiders", "repairs")
act("Paddy turns the first I Ching card: Storms and Raiders. Every province collects a good harvest. Silke, Paddy and Graham each pay 2 to the Harvest Pile to repair their public works (Province 4 is empty); Reina plays the first personal disaster in the Emperor's booklet (Provinces 2, 3 and 8 are empty). The population holds at 100 million, x1.", map_hl=[6])
say("Paddy", "Storms and Raiders, friends. The good news first: every province gets a good harvest this year. Provinces 4, 5, 6 and 7 each pay two to repair their public works, and that includes me. Provinces 1, 2, 3 and 8 play a Personal Disaster, so Reina, I'm sorry, that's you, and you'll need to turn the next one in your booklet. Population stays at a hundred million, times one, so everybody reads the first row of the income table.",
 "Paddy: A good harvest is welcome when I'm down to thirty-two grain, and paying two for repairs won't hurt much. I'm a bit worried about Reina's disaster, though, because if the crown has to tighten its belt, the tax goes up for all of us.")
harvest("Graham pays out the harvest from the Harvest Pile.")
act("Storms and Raiders: Silke, Paddy and Graham each pay 2 to the Harvest Pile for repairs.", deltas={pid(5):-2, pid(6):-2, pid(7):-2}, pile_delta=6, map_hl=[5,6,7])
disaster(1, "a rare horse, sent up the Silk Road as tribute, throws the Emperor in her excitement to ride it.")
say("Reina", "Thirty again. Steady is how I mean to run this house. This year it's the Winter Palace, and before you call it vanity, it's the gate to the canals. Silke, Paddy, your water comes next, one section at a time.",
 "Reina: Sixty in, twenty on the Palace, five to Paddy, which puts the reserve near a hundred and twenty after that horse cost me four. That's my cushion for doubled population and new land. With the Winter Palace up, I can put canals into Provinces 5 and 6 every year, and each one raises a taxable harvest.")
taxes(.30, collector="Silke collects the tax for the crown")
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="H20", text="Public works: Reina builds the Winter Palace on H20, in Province 1, and the crown pays the 20. It must stand before the canals in Provinces 5 and 6.", hover="The 20 goes into the Harvest Pile. 440 of the works are still owed.")
act("The auctions. Silke puts up her second Customs House, minimum 4, and keeps the Dragon Jar back; Paddy his second Bamboo Brush, minimum 4, keeping the Wooden Bowl back; Graham his last Land Deed Scroll, minimum 6, keeping the Vase back. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Silke", "Here's the second Customs House, as promised. Graham, it's got your name on it, so long as nobody goes back on their word. Four to open, same as last year.",
 "Silke: Paddy said publicly he'd stay out of this one, so Graham should get it cheap, and the deal holding means Paddy has to keep his hands off Graham's second Deed for me. I'm keeping the Dragon Jar back, because the last piece I sell is the one the table will want most.")
say("Paddy", "Here's the second Bamboo Brush, friends, at four. Silke said this one ought to go to Graham, and I'd be glad to see it go to him without a fight. Thank you for the Winter Palace, Reina. I'll gladly take water whenever the crown can spare it.",
 "Paddy: Graham lost the first brush to Silke, so putting the second one up now gives him a fair shot and keeps him friendly to me. The Wooden Bowl can wait until next year.")
say("Graham", "Last of the Scrolls, minimum six. Silke, it's yours to claim, and Paddy has told the whole table he's staying out. I'll take him at his word. I took him at his word last year too.",
 "Graham: Paddy offered me that Customs House cheap and then bid a grain over me for it, so this year I'm holding everyone to what they've said out loud. Silke wants this Scroll, and six only asks her to pay something near what she bid last time.")
say("Paddy", "I said I'd stay out, and I'm staying out. Graham, that Customs House is yours, and Silke, the Deed is yours, and I won't raise a finger on either. The Brush is still four if anyone wants it.",
 "Paddy: I already have those two pieces, so passing costs me nothing, and keeping my word now means Silke and Graham might trust me when the Jar and the Vase come up. Those are the two lots I'll really be fighting for.")
say("Silke", "Graham, the Brush is yours, I'm staying out of it. And Paddy, that Deed is the last one on the board, so if you've changed your mind about standing aside, say it now, to my face.",
 "Silke: That's the last Land Deed in the game, and without it I can't get to the throne, so I'll go to twenty if someone tries to block me. I'm leaving Graham's Brush alone, since fighting him for it would only fill the Harvest Pile.")
lot(5, "CH", [
 B(7, 4, "Thank you, Silke. Thank you, Paddy. I'll take you both at your word and bid four on each. Anyone who bids against me on the last copies is making a statement, and I'll remember it.",
   "Graham: I'm the only one who still needs these two, and they're the last copies on the table, so the ceilings sit well above the minimum. Nobody's going to keep my set from me for a few grain.")],
 hover=TH(("", "Nobody else bid; Graham would have gone to 20."),
          ("Graham", "It goes on S17.")), at="S17")
lot(6, "BB", [B(7, 4)],
 hover=TH(("", "Nobody else bid; Graham would have gone to 20."),
          ("Graham", "It goes on S18.")), at="S18")
lot(7, "LD", [B(5, 6)],
 hover=TH(("", "Nobody else bid; Silke would have gone to 20."),
          ("Silke", "It goes on P25.")), at="P25")
say("Graham", "Four and four. That's how it ought to go, friends. Thank you both. They're going down at the far end of the province, out of the way of any work the crown wants to build.",
 "Graham: That's two of the four, bought for eight grain, against the fourteen I nearly spent losing them last year. I put them out on the edge so no canal or road ever has a reason to sit on top of them.")
say("Silke", "The Deed goes down beside the Brush. Thank you, Graham, and thank you, Paddy, for keeping your word. Three deals honoured at one table, which must be a record for China.",
 "Silke: Six grain for the last Land Deed in the game is a bargain, and now I'm two pieces short of the set: Paddy's Bowl and Graham's Vase. They each hold the last copy of the piece I need, so from here on I'm the most polite woman on the coast.")
salaries({6:5}, text="Reina pays Paddy 5 for reading the I Ching.", hover="Nobody else at this table is on a salary.")

# ===== CHAPTER 2: The Set's Made to Be Used
# ============================== YEAR 3 ==============================
R(3, "The Wall is breached", "breach")
act("Paddy turns the I Ching card: The Wall Is Breached. Every province collects a good harvest. No Wall stands above Province 1, so Reina pays 2 in damages to the Harvest Pile instead of 5 for repairs (Provinces 2 and 3 are empty); Silke, Paddy and Graham each play the first personal disaster in their booklets (Provinces 4 and 8 are empty). The population holds at 100 million, x1.", map_hl=[6])
say("Paddy", "\"The Wall Is Breached.\" Good harvest for every province, so the barns are full, but horsemen have come through three links of the Great Wall. Provinces 1, 2 and 3 pay 5 million each for repairs, or 2 million into the Harvest Pile where no wall stands above them. Provinces 4 to 8 each play a Personal Disaster, and that's Silke, Graham and myself, so we each turn the next one in our booklets. Population is still 100 million, times one, so read the x1 row of your income tables. Sorry, Reina, the wall bill's yours. And sorry to the rest of us too.",
 "Paddy: A good harvest and a disaster for me in the same year. Whatever my booklet says, I'm still keeping twenty grain back, because the Jar and the Vase haven't come up yet and that's where my seventy-eight have to go.")
harvest("Graham pays out the harvest from the Harvest Pile.")
act("The Wall Is Breached: no Wall stands above Province 1, so Reina pays 2 in damages to the Harvest Pile.", deltas={pid(1):-2}, pile_delta=2, map_hl=[1])
disaster(5, "bandits attack the Silk Peasant's family and are beaten off by a young warrior, and a shrine to him must be built.")
disaster(6, "the Rice Peasant's only water buffalo breaks its leg, and the planting stops until a new one is found.")
disaster(7, "the Emperor catches sight of the Wheat Peasant's eldest daughter on a trip to the capital and takes her into the imperial household as a maid to an imperial daughter, and by tradition he must give a feast for his relatives and friends.")
say("Reina", "Thirty again. Steady hands, steady house. The Wall bill's paid and the barns are full, so the water I promised starts flowing now: both sections of the canal in Province 5 this year, Silke. Paddy, yours is next year, both sections, and you have my word on it in front of everyone.",
 "Reina: Sixty in, eighty out, and Paddy's five comes off as well, so the reserve drops to about one-thirty-three. That's still enough for land when the population doubles, and now Silke's harvest pays me back ten more a section every year. Doing the whole canal at once, and naming Paddy's year out loud, keeps either of them from feeling like they're the one being kept waiting.")
taxes(.30, collector="Silke collects the tax for the crown")
build("Grand Canal", 80, {1:80}, canal={5:2}, text="Public works: Reina digs both sections of the Grand Canal in Province 5, Silke's, at the crown's cost of 80. Each adds 10 to Silke's harvest from next year.", hover="The 80 goes into the Harvest Pile. The Winter Palace, which the canals in Provinces 5 and 6 need first, already stands. 360 of the works are still owed.")
act("The auctions. Each seller has one piece left, the only one of its kind, and must put it up: Silke the Dragon Jar, minimum 15, which Paddy and Graham both need; Paddy the Wooden Bowl, minimum 2, which Silke and Graham both need; Graham the Vase, minimum 10, which Silke and Paddy both need. Each peasant is two pieces short of a set. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Silke", "Thank you, Majesty. Two canal sections in Province 5, and I'll remember who dug them. Gentlemen, the Jar goes up first, and it's the only one in the world. I'll be honest: I'd rather it went to whichever of you lets me have my Bowl or my Vase cheaply than to whoever shouts loudest. Every grain we throw at each other goes into the Harvest Pile and helps none of us.",
 "Silke: Paddy and Graham each need my Jar, and I need one piece from each of them, so whoever wins the Jar has less left to fight me with. I've capped both of my bids at under forty, so even if I win both lots I keep enough for the twenty-grain set fee and a little left over.")
lot(5, "DJ", [
 B(6, 45, "Silke's right, and I'll say it plainly so nobody's guessing. My Bowl goes up at the minimum, 2 grain, so whoever needs it isn't held to ransom by me. I need the Jar and the Vase as much as anyone, though, so I'll bid what they're worth to me and stop there. If Graham beats me to the Jar, I'll shake his hand and that's that.",
   "Paddy: Each ceiling leaves me over twenty grain if I win both, so I can't overreach whatever happens. Graham's got the deepest pockets for the Jar, so I'm keeping an eye on him, but I won't pay double just to spite a neighbour."),
 B(6, None, "That's past what it's worth to me. It's yours, and well bought."),
 B(7, 46, "Paddy, I heard you, and I'll take that handshake on the same terms: I'll bid what the Jar is worth to me and not a grain past it. The Vase goes up at ten, which is fair for the only one in the world, and I'll ask nobody to thank me for it.",
   "Graham: If I take the Jar and the Bowl and still have the twenty spare, the set is mine this year, and I've done the sums so that even at my top price I keep twenty-five and a half. Last year I lost fourteen grain being polite, so this year I'm being exact.")],
 hover=TH(("", "Paddy's limit was 45. Graham would have gone to 60, and to 70 to keep it from Paddy."),
          ("Graham", "It goes on S16.")), at="S16")
lot(6, "WB", [
 B(5, 38), B(5, None, "Too rich for a silk farmer this year. Enjoy it, and mind you don't go hungry carrying it home."),
 B(7, 39)],
 hover=TH(("", "Silke's limit was 38; Graham would have gone to 50."),
          ("Graham", "It goes on S15.")), at="S15")
lot(7, "VA", [
 B(5, 36), B(5, None, "Too rich for a silk farmer this year. Enjoy it, and mind you don't go hungry carrying it home."),
 B(6, 37)],
 hover=TH(("", "Silke's limit was 36; Paddy would have gone to 45."),
          ("Paddy", "It goes on Q21.")), at="Q21")
say("Graham", "Paddy, here's my hand, as promised. Silke, thank you for the Bowl's company. That makes four pieces in a row on the S line, and I'll leave the table to count what that means.",
 "Graham: Forty-six and thirty-nine, well under my limits, so I've got the Jar, the Bowl, the Customs House, the Brush and about seventy grain, and the set is complete. Now I'm watching Silke and Paddy, because one of them is about to find out that the Wheat Peasant doesn't stay a peasant.")
say("Paddy", "The Vase goes on Q21, next to my Deed. Graham, that's the Jar and the Bowl both, so you've got the whole set, and I said I'd shake your hand, so here it is. Fairly won. Silke, I'm sorry it came down to the two of us on the Vase. I had to have it.",
 "Paddy: With the only Jar sitting in Graham's province, my set can't be finished at auction now, so the Vase is something I hold rather than something that finishes anything. That makes Graham the man to watch at this table from here on, and I mean to keep my grain for land and my people.")
act("Graham holds the Wheat Peasant's whole set, a Customs House, a Bamboo Brush, the Dragon Jar and the Wooden Bowl, and 69.5 grain, so he may replace another peasant (Section 11). Only the Silk Peasant may take the throne at this table.", map_hl=[7])
say("Graham", "Silke, in Year One you offered me the Brush and then outbid me by a grain. I wrote it down. The Reservoir's yours now, twenty a year, and I hope it treats you as well as it treated me. Majesty, I'll look after your two canal sections in Province 5 properly.",
 "Graham: I'm swapping the Reservoir's twenty for her canals' twenty and taking 190 grain, and the Silk Peasant is the only seat at this table that leads to the throne. All I need now is a Deed and Paddy's Vase, and I'll be counting every grain until I have them.")
swap(7, 5, "Graham Garner replaces Silke Weber as the Silk Peasant of Province 5. He takes her 120.5 grain with his own. The Dragon Jar, native to Province 5, goes back into its stock, for Graham to auction; his Customs House, Bamboo Brush and Wooden Bowl go on P24, P23 and P22. Silke returns her Bamboo Brush and Land Deed Scroll, draws 60 from the Harvest Pile and becomes the Wheat Peasant of Province 7, with its Reservoir.",
     hover="Graham: 69.5 + 120.5 = 190. Silke's Brush goes to Province 6's stock and her Deed to Province 7's, the provinces that started with them (Provinces 3 and 4 are empty). As the Silk Peasant, Graham still needs a Land Deed Scroll and the Vase; with them he may take the throne. Silke, as the Wheat Peasant, needs a Customs House, a Bamboo Brush, the Dragon Jar and the Wooden Bowl.",
     at={"CH":"P24","BB":"P23","WB":"P22"})
salaries({6:5}, text="Reina pays Paddy 5 for reading the I Ching.", hover="Nobody else at this table is on a salary.")

# ============================== YEAR 4 ==============================
R(4, "Drought", "blight")
act("Paddy turns the I Ching card: Drought. Every province collects an average harvest, and nothing else happens. The population holds at 100 million, x1.", map_hl=[6])
say("Paddy", "\"Drought. Not a cloud in months. The locusts, at least, are having a fine year.\" All provinces collect an average harvest, and nobody plays a disaster this time, thank heaven. The population is still 100 million, times one, so read the x1 row again. Welcome to Province 7, Silke. I hope the Reservoir does right by you.",
 "Paddy: Strange how it's gone: I've got three of my four pieces, and the one I'm missing, the Jar, is up for auction from Graham's stock this very year. He'll know how much I want it, so I've got to work out what it's really worth to me and still keep my twenty grain back.")
harvest("Graham pays out the harvest from the Harvest Pile.")
say("Reina", "Thirty, same as every year. Nobody at this table can say I've squeezed them. Paddy, I gave you my word last year in front of everyone, so both sections of your canal go in this year and the crown pays all of it. Graham, congratulations on Province 5, and on its water. You're the richest at the table now, and I'll be watching that Land Deed Scroll auction with real interest.",
 "Reina: Keeping my word to Paddy costs me eighty and brings the reserve down to about a hundred and six. But Paddy is sitting on the one Vase Graham needs for the throne, and I'd like him to feel he owes the crown something before Graham starts making offers.")
taxes(.30, collector="Silke collects the tax for the crown")
build("Grand Canal", 80, {1:80}, canal={6:2}, text="Public works: Reina digs both sections of the Grand Canal in Province 6, Paddy's, at the crown's cost of 80, as she promised him last year. Each adds 10 to Paddy's harvest from next year.", hover="The 80 goes into the Harvest Pile. The Grand Canal in Provinces 5 and 6 is finished; the two sections in Province 1 wait on the Summer Palace. 280 of the works are still owed.")
act("The auctions. Each seller has one piece in stock and must put it up: Graham the Dragon Jar, minimum 60, the last piece Paddy needs and one Silke needs too; Paddy a Bamboo Brush, minimum 2, which Silke needs; Silke a Land Deed Scroll, minimum 60, which Graham needs. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Graham", "The Jar's the last one in the world and it finishes a set, so it goes up at sixty. Anyone who thinks that's dear can wait a year and see what it costs then. Silke, I'll want your Deed, and I'll pay a fair price for it, more than a fair one if I have to.",
 "Graham: A finished set for Paddy means he can sit in my chair and take my 228, so I'd rather keep the Jar off the market for a year than sell him the key to my own barn. The Deed is the only piece I can actually buy, so I'll pay well for it, and more if the crown starts bidding against me.")
act("A lot that goes unsold must go up again the next year with its minimum at 2.")
lot(5, "DJ", [
 B(6, 60, "Graham, sixty's steep and you know it, but it's the last piece I need, so I'll meet you there and not run off into the clouds after it. The Brush goes up at 2 again, same as the Bowl did. Silke, it's yours for a song if you want it. And Majesty, thank you for the canal. You said you'd dig it and you did.",
   "Paddy: If I win the Jar I've got the whole set, and the canal will be watering Province 6 from next year whatever I end up doing with it. Seventy-five is my limit, which still leaves me over forty grain, and I'll leave the Deed to Graham and Silke to settle between them.")],
 hover=TH(("", "Nobody else bid; Paddy would have gone to 75."),
          ("Paddy", "It goes on Q22.")), at="Q22")
lot(6, "BB", [
 B(7, 2, "Well. Year One gets written down at this table and paid back in Year Three. I'll remember that, Graham, I've a long memory of my own. The Deed goes up at sixty, the same price you put on the Jar, so you can hardly call it dear. Paddy, thank you for the Brush at two. That's the first kind price I've had all night.",
   "Silke: I've gone from two pieces short of the throne to four short of anything, and the only card I hold now is the one Deed Graham needs, so he pays me his own price for it. I'm staying out of the Jar fight and buying the cheap Brush, because the Jar is the man's last piece and I can't win it. (Silke whispers to Paddy: \"Graham's one Vase short of the throne now, and the only one is sitting on your board. If you won't sell him the way up, I'll back you on anything you want at this table.\" The Storyteller reminds Paddy that Graham still needs a Land Deed Scroll as well as the Vase.)")],
 hover=TH(("", "Nobody else bid; Silke would have gone to 12."),
          ("Silke", "It goes on S18.")), at="S18")
lot(7, "LD", [B(5, 60)],
 hover=TH(("", "Nobody else bid; Graham would have gone to 90."),
          ("Graham", "It goes on P21.")), at="P21")
say("Paddy", "The Jar goes on Q22, in a row with the others: Customs House, Deed, Vase and Jar. I didn't think I'd ever say it, but that's my whole set. Graham, you'll understand the Vase isn't going anywhere now, since it's part of what I hold, and I'd sooner everyone heard me say that than have any of you hoping otherwise.",
 "Paddy: Silke offered to back me in a whisper, but I'd rather say where the Vase stands out loud, and it stays with me. Now I've got a full set and the grain to go with it, and I'm only just starting to think about what to do with that.")
say("Silke", "S18, where Graham's Brush used to stand. Two grain for it, and it's the first thing I've owned in Province 7. Graham, enjoy the Deed. Fifteen of that sixty is mine, so I'll thank you for the price you named.",
 "Silke: Graham has the Deed now and one piece, the Vase, between him and the throne, and the only Vase is on Paddy's board. Paddy has his whole set, so who does what next matters more than my two-grain Brush.")
say("Graham", "Sixty for sixty, Silke. That's fair, and I'll write it down as fair. Paddy, you've got your set now, so I'll shake your hand the way you shook mine, and I'll ask you to remember who sold you that Jar without a fight.",
 "Graham: That leaves me only the Vase short of the throne, and it's sitting on Paddy's Q21. The trouble is that Paddy's set is finished as of tonight, so I'll be watching where he decides to sit.")
act("Paddy holds the Rice Peasant's whole set, a Customs House, a Land Deed Scroll, the Vase and the Dragon Jar, and 58.5 grain, so he may replace another peasant (Section 11). Graham, the Silk Peasant, needs only the Vase to take the throne.", map_hl=[6])
say("Paddy", "Graham, I won't pretend this is easy to do to the man who sold me the Jar without a fight, and I'll not forget that. But the set's made to be used, and I'd be a fool to sit on it. I'm taking the Silk Peasant's seat. Province 6 is yours now, and Reina's canal goes with it, so you'll have good water to start on. And the Jar goes up from Province 5 at the fairest price I can put on it.",
 "Paddy: Graham was one Vase short of the throne and I was holding it, so by taking his seat I end that race, and I'm the only one left on the road to the crown with a Brush and a Bowl still to find. I'm sorry to do it to him, and I'm going to be very careful with his grain.")
swap(6, 5, "Paddy Doyle replaces Graham Garner as the Silk Peasant of Province 5. He takes Graham's 183.5 grain with his own. The Dragon Jar, native to Province 5, goes back into its stock, for Paddy to auction; his Customs House, Land Deed Scroll and Vase go on P24, P23 and P22. Graham returns his Customs House, Bamboo Brush, Wooden Bowl and Land Deed Scroll, draws 60 from the Harvest Pile and becomes the Rice Peasant of Province 6, with its two new canal sections.",
     hover="Paddy: 58.5 + 183.5 = 242. Graham's Customs House goes to Province 5's stock, his Brush and the Wooden Bowl to Province 6's, and his Deed to Province 7's (Note 12: the provinces that started with them, or their own). As the Silk Peasant, Paddy still needs a Bamboo Brush and the Wooden Bowl; with them he may take the throne. Graham, as the Rice Peasant, needs a Customs House, a Land Deed Scroll, the Dragon Jar and the Vase.",
     at={"CH":"P24","LD":"P23","VA":"P22"})
salaries({5:5}, text="Reina pays Paddy 5 for reading the I Ching.", hover="Nobody else at this table is on a salary.")

# ===== CHAPTER 3: TITLE
R(5, "The population doubles", "double1")
act("Paddy turns the I Ching card: Population Doubles. Every province collects a good harvest, and the population doubles to 200 million, x2, so every province eats twice what it did. With the population doubled, new land is open (Section 13): 20 a square, yielding 20 a year from the next harvest, and the Emperor must pay part of every square.", map_hl=[5])
say("Paddy", "\"Population Doubles.\" Good harvest for every province this year, but the counter goes from one hundred million to two hundred million, so we're all on the x2 row now. Everyone's consumption doubles from here, so check your tables before you count your grain. And if it comes round again we'll be at x4, so anyone running thin, Graham, I'm looking at you kindly, ought to think about new land while it's twenty a square.",
 "Paddy: A good harvest this year, but every mouth to feed counts double from now on, and Graham's down to sixty with my Brush and Bowl in his stock. I'd sooner he stayed on his feet and sold them to me fair than went under and they got tangled up in somebody's debts.")
harvest("Graham pays out the harvest from the Harvest Pile.")
