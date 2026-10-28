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
act("Reina hands out the table jobs of the empty seats for the whole game: Graham Garner banks the Harvest Pile and pays out every harvest, Paddy Doyle collects the tax, and Silke Weber reads the I Ching card each year and keeps the population counter, for the Scholar's 5 a year from the crown.", map_hl=[1,5,6,7])
say("Reina", "Right, everyone gets a job, so nobody can say the crown played favourites. Graham, you hold the Harvest Pile, since wheat people count carefully. Paddy, you collect the tax, and please be gentle with your neighbours. Silke, you read the I Ching, and the crown pays you five a year to tell us honestly what the heavens say.",
 "Reina: The coast is where a revolt would start, so the only paid post goes to Silke and the tax goes through Paddy's hands, which ties both coastal provinces to the throne. Graham sits inland and gets the bank, which gives him a reason to keep the pile honest and the books quiet.")
act("Silke shuffles the I Ching deck and sets it face down. The first card is turned in Year 2.", map_hl=[5])

# ===== CHAPTER 1: You Already Had a Brush
# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 each player was dealt is the first harvest, and the tax is levied on it.")
CUR_INC.update({s:60 for s in ACTIVE})
say("Reina", "Forty percent this year, friends. That's twenty-four from each of you, and you still keep more than you hand over. The crown pays for the Summer Palace on its own, and next year we start on the Wall and the canals.",
 "Reina: The tax brings in 72, Silke's salary costs 5 and the palace costs 20, so the crown ends the year at 107 with the Wall and the Province 1 canal now open to build. I'm taxing firmly while incomes are positive and building every year, and I'm keeping a reserve back for the day the population doubles and the land starts costing money.")
taxes(.40, collector="Paddy collects the tax for the crown")
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="G20", text="Public works: Reina builds the Summer Palace on G20, in Province 1. It must stand before any Wall link or the Province 1 canal.", hover="Reina pays the 20. 500 of the works are still owed.")
act("The auctions. Each seller holds two types beside the board and chooses which goes up: Silke the Dragon Jar, the only one in the game, minimum 4; Paddy one of his two Bamboo Brushes, minimum 4; Graham one of his two Land Deed Scrolls, minimum 2. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Silke", "Thank you, Your Majesty. Five a year to read the heavens is fair, and I'll read them honestly, good news or bad. The Dragon Jar goes up first, opening at four. It's a lovely piece, and nobody at this table has much money, so I'm not going to pretend it's worth forty.",
 "Silke: I sell the Dragon Jar first because nobody's set seems to need it, so I won't be handing anyone a piece of the throne. I'm keeping the Customs Houses back until I can see who wants them badly, and my grain is going on a Brush and a Bowl when Paddy's lots come up.")
say("Paddy", "Thank you, Reina, I'll be gentle with the collecting, I promise. Right then, one Bamboo Brush from the rice country, starting at four. It's a good honest brush, and I've got another just like it for next year, so nobody needs to go mad over it.",
 "Paddy: I've got two brushes and only the one bowl, so the brush goes first and the bowl stays scarce for when somebody really wants it. I need every grain for the Jar, the Vase and the rest, so I'm watching what Silke and Graham chase before I spend a thing.")
say("Graham", "One Land Deed Scroll, opening at two. I've got two of them, so whoever wants paper on the land had better start now.",
 "Graham: I've got two scrolls and only one vase, so the scrolls have to start going first or I'll still be stuck with one in year three. Starting at two costs me nothing, and I want to see who at this table bids on deeds before any new land opens.")
act("The Storyteller tells Silke that Paddy's and Graham's sets both need the Dragon Jar.", map_hl=[5])
say("Silke", "Well, I was wrong about the Dragon Jar. Paddy, Graham, it turns out you both need it and there's only the one, so it opens at four and the two of you can sort it out between you. I'll take a polite interest in the brush and the scroll, and I won't be emptying my purse on either.",
 "Silke: I've just learned my jar is the one piece both my rivals can't do without, so I keep it at four and let them outbid each other while I collect a quarter of the price. I'm bidding modestly on the brush and the scroll because there's a second of each next year, and if those two wear each other down over the jar, both will come cheap.")
lot(5, "DJ", [
 B(6, 14, "Graham, I won't pretend I don't want that Jar, because I do, and so do you. If we fight over it, the Harvest Pile gets fat and we both go hungry. Still, there's only the one, so I'll bid what's sensible.",
   "Paddy: There's only one Dragon Jar in the whole game, and Graham needs it the same as I do, so I'll stretch for it, but I'm not emptying the sack. Graham's got two Land Deeds, so if I miss the first one cheap there's another next year."),
 B(7, 16, "Only one Dragon Jar in the whole game, so I'll bid on it, and I won't be shy about it.",
   "Graham: There's only one jar, and whoever doesn't get it can never finish a set, so I'll go further for it than for anything else."),
 B(6, 17),
 B(7, None, "Fair enough. I'll stop there, I've counted what I can afford.")],
 hover=TH(("", "Graham went to 16 to keep the Jar from Paddy; Paddy would have gone to 18 to keep it from Graham."),
          ("Paddy", "It goes on R22, in the middle of the paddies.")), at="R22")
say("Paddy", "Seventeen. That's more grain than I like to spend on anything I can't eat, but there was only the one. Sorry, Graham, you pushed me right to the edge there. She goes in the middle of the paddies where I can keep an eye on her.",
 "Paddy: That's the only Dragon Jar in the game, so now Graham can't finish his set without coming to me first. I've got 19 grain left, which is thin, and I lost the scroll to Silke on a tie, so next year I'll have to be cleverer about the second one.")
lot(6, "BB", [
 B(7, 4, "Paddy, you've got two brushes. If one ends up in Silke's hands this year, that's fine by me, there's another one next spring.",
   "Graham: The brush isn't worth a fight, because Paddy has to put the second one up next year anyway."),
 B(5, 5),
 B(7, None, "Fair enough. I'll stop there, I've counted what I can afford.")],
 hover="Silke puts the Brush on P25, at the far end of the coast.", at="P25")
lot(7, "LD", [
 B(6, 6), B(5, 6),
 B(6, None, "Fair enough, it's yours. I'm not paying more than the pot's worth to me.")],
 hover="Both limits stood at six, and a tie goes to the earlier seat: Silke, in Province 5, before Paddy in 6. Silke puts the Scroll on P26, beside her Brush.", at="P26")
say("Silke", "A brush and a deed for eleven, and four back from my Jar. Thank you, gentlemen. Paddy, enjoy the Jar. Seventeen is a lot of rice to hand over for one pot.",
 "Silke: That's two of my four pieces for a net seven, while Paddy and Graham paid thirty-three between them to fight over a jar. I've put mine at the far end of the coast, out of the way of any canal the crown wants to dig, and I'm watching Paddy now, because he has a Bowl and the Jar.")
salaries({5:5}, text="Reina pays Silke 5 for reading the I Ching, the Scholar's salary.", hover="Nobody else at this table is on a salary.")

# ============================== YEAR 2 ==============================
R(2, "The canal gives way", "canal")
act("Silke turns the first I Ching card: The Canal Gives Way. An average harvest for every province. No canal has been dug, so none is lost. Provinces 2, 3, 7 and 8 play a personal disaster; 2, 3 and 8 are empty, so that's Graham. The population holds at 100 million, x1.", map_hl=[7])
say("Silke", "The heavens say: 'The Canal Gives Way. The engineers blame the river. The river declines to comment.' Average harvest in every province. Any unfinished Grand Canal work is lost, and since nobody has dug a canal yet, the crown loses nothing. Provinces 2, 3, 7 and 8 play a Personal Disaster, so Graham, I'm sorry, but that's you. The population holds at one hundred million, times one, so read the first row of your tables.",
 "Silke: Graham turns his disaster card while I sit on a brush and a deed with a quiet harvest coming. I need the Bowl from Paddy and the Vase from Graham, and Graham with a disaster on top of him might sell cheaper than he'd like.")
harvest("Graham pays out the harvest from the Harvest Pile.")
disaster(7, "a late frost blackens the edge of the wheat.")
say("Reina", "Forty percent again, which comes to fourteen each on a thin year. Graham, I'm sorry about the frost. The crown digs the whole northern canal this year, both sections in one go, so the river has nothing half-finished to swallow. Your Reservoir is on the list, and it's coming.",
 "Reina: That card wipes out half-dug canals, so I'm building both sections at once for 80; the canal pays the crown 20 a year from now on and has paid for itself in four. After the tax, Silke's salary and the canal I'm down to about 79, and that's still a cushion for when the land opens.")
taxes(.40, collector="Paddy collects the tax for the crown")
build("Grand Canal", 80, {1:80}, canal={1:2}, text="Public works: Reina digs both sections of the Grand Canal in Province 1 in one year, one project. They add 20 to her harvest from next year.", hover="Reina pays the 80. 420 of the works are still owed.")
act("The auctions. Silke has only Customs Houses left, so one goes up; Paddy puts up his second Bamboo Brush, minimum 4, and keeps the Wooden Bowl back; Graham puts up his last Land Deed Scroll, minimum 5, and keeps the Vase back.", map_hl=[5,6,7])
say("Paddy", "Second brush, as promised, Graham, same as the first, opening at four. And I'm sorry about the frost. Losing two to a cold night is hard on anybody.",
 "Paddy: Graham bid on the last brush and lost it, so I reckon he'll want this one, and the quarter I keep helps fill my sack back up. The Wooden Bowl's the only one in the game, so I'm holding it back until someone really needs it.")
say("Graham", "The other Land Deed Scroll. Minimum five. Paddy, you went to six for the last one.",
 "Graham: Paddy has the only jar now, so I can't finish a set unless that changes, and I've written that down. Until then I sell to whoever's shown they'll pay: Paddy and Silke both went to six on the first scroll, so I'm setting the floor just under that.")
say("Silke", "One Customs House, opening at three. It's good for trade and a quiet port. As for the brush and the scroll, I already have mine, gentlemen, so I'm only watching. Mostly.",
 "Silke: These are the last brush and the last scroll in the game, and Graham needs one while Paddy needs the other. If I buy both, I'm the only peasant who can still finish a set. Their Bowl and Vase still have to go up for auction whether they like it or not, so all I have to do is keep enough grain to win them.")
lot(5, "CH", [
 B(6, 4, "Graham, there are two Customs Houses and two of us after them. Let's not feed the Harvest Pile. You take this one, I'll only put in a small bid, and next year you leave the second one to me. That's fair, isn't it?",
   "Paddy: I'll go high for it and keep the Customs House cheap, and if Graham shakes on the deal I get the second one next year without a fight."),
 B(7, 5, "Paddy. Silke has two Customs Houses, and you and I need one each. I won't bid against you on this one if you leave the next one to me. No point feeding the Pile.",
   "Graham: Two Customs Houses and two buyers is just arithmetic, so there's no reason for a war over them."),
 B(6, None, "No, that's past what it's worth to me. Go on, it's yours.")],
 hover=TH(("", "Each offered the other this one and the next, and both bid anyway: Graham's limit was 6, Paddy's 4."),
          ("Graham", "It goes on Q15.")), at="Q15")
say("Graham", "Q15. Thank you, Paddy, the next one's yours, as agreed.")
lot(6, "BB", [
 B(7, 5, "The brush I'll take at Paddy's price.",
   "Graham: The brush nobody else needs should come to me cheap. I can't finish without the jar, and I know it, but I'm still collecting pieces in case the jar ever moves."),
 B(5, 6),
 B(7, None, "No. I've counted it.")],
 hover=TH(("", "Silke already holds a Brush; she bid only against Graham, and would have gone to 13 to keep this one from him."),
          ("Silke", "It goes on P24, beside the other one.")), at="P24")
say("Graham", "Silke. You already had a brush.",
 "Graham: Silke paid six for a brush she didn't need, only so I couldn't have it. Paddy has the jar and she has both brushes now, so I've lost two pieces I needed to people who say they're only watching, and I'm noting every one of them.")
say("Silke", "Two brushes on my coast, so I'll be the best-lettered peasant in China. Graham, I'm sorry, but six is cheap for a good brush, and you agreed it was Paddy's price.",
 "Silke: Graham can't finish a set now, because every brush in the game is on my shore. Paddy outbid me for the scroll, so he's the one I race from here: I need his Bowl and Graham's Vase, and I have to keep my grain dry for both.")
lot(7, "LD", [
 B(6, 5, "And yes, I'll be bidding on that last scroll, I won't pretend otherwise.",
   "Paddy: That's the last Land Deed in the game and I'm the only one who still needs it, so it's the piece I can't lose."),
 B(5, 12), B(6, 13),
 B(5, None)],
 hover=TH(("", "Silke already holds a Scroll; she bid only against Paddy, up to 12. Paddy would have gone to 15."),
          ("Paddy", "It goes on R23, beside the Jar.")), at="R23")
say("Paddy", "Thirteen, and Silke, you made me earn every grain of it, for a scroll you already had. Graham, we crossed our wires on who got which Customs House, but you've got this one now, so by my reckoning the last one's mine next year and you'll stand aside. I'll hold you to that, same as I'd hold myself.",
 "Paddy: The scroll goes right beside the Jar, so that's two of my four, and both were the only ones left. All I need now is that last Customs House and Graham's Vase, and Silke bidding twelve on a scroll she didn't need tells me she's watching me now.")
salaries({5:5}, text="Reina pays Silke 5 for reading the I Ching.", hover="Nobody else at this table is on a salary.")

# ===== CHAPTER 2: The Mandate Moves to the Coast
# ============================== YEAR 3 ==============================
R(3, "The villages grow", "half2")
act("Silke turns the second I Ching card: Population Grows by Half. A good harvest for every province, and no disasters. The population rises to 150 million, x1.5, and every province eats half as much again.", map_hl=[1,5,6,7])
say("Silke", "\"Population Grows by Half. The villages are noisier than they used to be.\" Good harvest everywhere, no disasters named. The counter goes to 150 million, so that's times one and a half, everyone. Read the x1.5 row, and remember your mouths just got hungrier too. Honest reading, as promised.",
 "Silke: One more doubling and the new land opens at twenty a square, and I'm the one sitting on fifty-five grain while Paddy scrapes along at twenty-nine. My Customs House goes on sale this year, and a bigger crowd makes it worth more, so I'll price it accordingly.")
harvest("Graham pays out the harvest from the Harvest Pile.")
say("Reina", "A good year, and a good year is when the crown asks for more. Fifty percent, which is twenty a head, and you each still clear twenty. Graham, I said the Reservoir was coming, and it's coming now. The crown puts in forty if you put in twenty, and it pays you twenty a year from next harvest, so your share is back in your pocket after one year. Silke, your five, as always.",
 "Reina: Bad years bring in nothing, so I'm taxing the fat one at fifty and spending it on the promise I made Graham before he starts to doubt it. With his twenty in the split I keep the reserve near a hundred and twenty-four, which is the money I'll need when the land opens at times two.")
taxes(.50, collector="Paddy collects the tax for the crown")
say("Graham", "Twenty in, twenty back each year from next harvest. That pays for itself in one year, Reina, and I don't argue with a number like that. Build it.",
 "Graham: Twenty grain buys me twenty a year for as long as the game runs, which beats anything going at auction. The Vase goes up later and I'll want every grain the other two have left to be bid against each other, not spent on me.")
build("Province 7 Reservoir", 60, {1:40, 7:20}, key="res7", at="O16:P17", text="Public works: Reina and Graham build the Province 7 Reservoir, two squares by two, on O16 to P17, the crown paying 40 and Graham 20. It adds 20 to Graham's harvest from next year.", hover="The 60 goes into the Harvest Pile. 360 of the works are still owed.")
act("The auctions. Each seller has one piece left, so each goes up: Silke's last Customs House, minimum 15; Paddy's Wooden Bowl, minimum 4; Graham's Vase, minimum 8. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Graham", "I said I'd stand aside on the Customs House, so I'm standing aside. Paddy, it's yours to win. The Bowl I'll bid on, and the Vase opens at eight. There's only one, and two of you need it.",
 "Graham: The Bowl's no use to me unless someone trades me a brush or the jar, but if I hold it, Silke's set stops with me, and that's the first leverage I've had in this game. The Vase at eight: one of them will pay it, and the more they bid against each other, the more my quarter comes to.")
say("Paddy", "Graham and I shook on this Customs House last year, and I'm grateful he's keeping to it. Silke, I'll not pretend I don't want your Vase too, Graham, so I'll bid it honestly and no higher than I can stand. And the Bowl goes up at four. It's a good bowl, and I'll not give it away.",
 "Paddy: The House should come cheap if Graham keeps his word, and he always has. Then everything I've got goes on the Vase, as long as I still have twenty left over to finish the set, because if Silke gets that Vase she's one step from me, and I can't have that.")
say("Silke", "My last Customs House starts at fifteen, Paddy. It's the only one left in China, and you know exactly what it's worth to you. As for the pottery, I'm only bidding to keep the kiln-men honest.",
 "Silke: Whatever Paddy pays for my Customs House he can't spend on the Vase, and I get a quarter of it back for my trouble. If I get the Bowl and the Vase this year, I hold four of the five with grain enough to finish, and the reader of cards turns into the one who picks the next Emperor.")
act("Silke's Customs House opens at 15. Paddy, the only bidder, would go to 8, so nobody meets the minimum: it stays beside the board and must go up again next year at 2.", map_hl=[5,6])
lot(6, "WB", [
 B(7, 8), B(5, 9), B(7, 12), B(5, 13),
 B(7, None, "That's past what it's worth to me. Take it.")],
 hover=TH(("", "Graham would have gone to 12 only to keep the Bowl from Silke; Silke would have gone to 24 to keep it from Graham."),
          ("Silke", "She puts the Bowl on P23.")), at="P23")
lot(7, "VA", [
 B(6, 20), B(5, 21), B(6, 24), B(5, 25),
 B(6, None, "That's more than this farm can spare. Fair bidding to you.")],
 hover=TH(("", "Paddy went to 24 to keep the Vase from Silke; Silke would have gone to 40 to keep it from Paddy."),
          ("Silke", "She puts the Vase on P22, beside the Bowl.")), at="P22")
say("Silke", "A bowl and a vase on the coast, next to my brushes and my deed. Thank you, Paddy, and thank you, Graham, both very fair prices. I'm only putting them on the shelf. For now.",
 "Silke: Brush, scroll, bowl and vase all sit in a row on my coast, and I still have thirty-seven grain, well past the twenty I need, so the set is complete. The Customs House I couldn't sell may be my last real bargaining chip, and now everyone at this table is wondering whose seat I'll take.")
swap(5, 1, "Silke Weber declares a complete set (Bamboo Brush, Land Deed Scroll, Wooden Bowl, Vase) and 37 grain, and takes the throne: with no upper class at this table, the Silk Peasant may. Silke becomes Emperor of Province 1; Reina Osorio becomes Silk Peasant of Province 5. A new Emperor returns all her realia: both Bamboo Brushes and the Wooden Bowl go back to Province 6's stock, the Land Deed Scroll and the Vase to Province 7's, to be auctioned again. Silke takes the crown's reserve of 129; Reina draws 60 from the Harvest Pile. The unsold Customs House stays in Province 5's stock, now Reina's to sell.",
 hover="Silke: That's a hundred and sixty-six grain and the whole empire, and every piece goes back to the stock to be sold again, so the race starts over with me as the one to beat. Reina knows the throne better than anyone, so she's the one I'll be watching from up here.")
say("Silke", "Brush, scroll, bowl and vase, and grain to spare. Reina, the cards have been reading honestly all along, and this year they say the Mandate moves to the coast. I take the throne. Don't worry, the I Ching still needs a reader, and I'll pay a fair five for one.")
act("Silke hands out the table jobs as the new Emperor: Graham Garner keeps the Harvest Pile and now also reads the I Ching and keeps the population counter, at 5 a year; Paddy Doyle keeps collecting the tax. Reina holds no job.", map_hl=[1,6,7])
say("Silke", "Graham keeps the Harvest Pile and takes the cards, at five a year, the same as I got. Paddy keeps the tax. Reina, rest those hands for a year, you've earned it. I'll run an honest crown, but not a soft one.",
 "Silke: Graham can't build a set any time soon, so the jobs and the five grain go to the one friend who has nothing to gain from my fall. Reina and Paddy are the ones who'll be racing for those pieces again, and I'd rather not hand either of them a crown salary to bid with.")
salaries({7:5}, text="Silke pays Graham 5 for reading the I Ching from next year.", hover="Nobody else at this table is on a salary.")

# ============================== YEAR 4 ==============================
R(4, "The seed rotted", "dribble2")
act("Graham turns the third I Ching card: Bad Harvest. A bad harvest for every province, and no disasters. The population holds at 150 million, x1.5.", map_hl=[1,5,6,7])
say("Graham", "\"Bad Harvest. The seed rotted, the rains came late, and the ox went lame. All provinces collect a bad harvest.\" The counter stays at 150 million, so it's still times one and a half, everyone. Read the bad-harvest row at x1.5. No disasters named. And Your Majesty, a bad year is a poor year for fifty percent.",
 "Graham: Silke paid twenty-five for my Vase, and a turn later it's back in my stock to sell again, which is the best piece of luck I've had. The tax is what I'm watching now: we get a thin harvest this year, and our new Emperor just found out what the throne costs to keep.")
harvest("Graham pays out the harvest from the Harvest Pile; a negative income is paid into it.")
say("Silke", "Graham's right, a rotten year is no year to squeeze anyone. Thirty percent, and only Graham owes it, three grain. The crown pays for the Winter Palace itself, and that opens the way for canals on the coast, Reina's and Paddy's.",
 "Silke: A light tax costs me almost nothing, and a twenty-grain palace that unlocks their canals gives the two hungry ones a reason to want me to stay. I'm keeping the reserve deep, because when the population doubles I'll have to buy land, and they'll have to buy it too.")
taxes(.30, collector="Paddy collects the tax for the crown")
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="H21", text="Public works: Silke builds the Winter Palace on H21, in Province 1. It must stand before the canals in Provinces 5 and 6.", hover="Silke pays the 20, into the Harvest Pile. 340 of the works are still owed.")
act("The auctions. Reina's Customs House went unsold last year, so it must go up again at 2. Paddy puts up the Wooden Bowl, minimum 6, and keeps both Bamboo Brushes back; Graham puts up the Vase, minimum 10, and keeps the Land Deed Scroll back.", map_hl=[5,6,7])
say("Paddy", "The Bowl's come home to me again, so up it goes. Six to start. Graham went to twelve for it last year, so I don't think six is asking much. And Reina, I'm sorry about the throne. That Customs House of yours at two is the first good news I've had in a year.",
 "Paddy: Graham and Reina both fancy that Bowl now, and every quarter-share I get from the sale goes toward the Vase. Silke beat me by a single grain last year, and I won't let it happen twice.")
say("Graham", "The Vase again. It's still the only one in China, and last year it went for twenty-five. It opens at ten.",
 "Graham: Paddy needs it and so does Reina's new seat, and both of them have short purses after a rotten year, so ten is a floor they can reach but not one they'll get it under. I'll keep the Scroll back for next year, so I've always got something they need.")
say("Reina", "Well. Silke played the long game and played it beautifully, and I'll say so on the record. The coast is mine now, so I'm starting over like everyone else: my Customs House is up at two, cheap, and I'll be bidding on the pottery, but nobody's going to see me burn my grain to get it.",
 "Reina: I've lost the throne and I'm down to fifty, so I'm doing what Silke did: get hold of the scarce piece, which is the one Vase in China, and only pay for the Bowl if it comes cheap. Whatever happens I keep twenty-plus back, because the set means nothing without the grain to claim with.")
say("Paddy", "Reina, I'll take that Customs House off your hands, and gladly. Graham, ten's a fair start for the Vase. I'll say it plainly to everyone: if I get the House and the Vase both, I've got my set, and I'll still have my twenty grain kept by.",
 "Paddy: The House should come cheap because I'm the only one who needs it, so this year it comes down to the Vase. I'll go as high as I can and still keep the twenty grain the set needs, and not a single grain past that.")
say("Graham", "The Customs House is Paddy's business, not mine. I'll bid for the Bowl, though, because I need it, and I won't lose it by one grain twice.",
 "Graham: The brushes are back in Paddy's stock now, so my set's alive again if I take this Bowl. And Reina can't finish hers without it, so I'll go a little further to keep it off the coast.")
lot(5, "CH", [B(6, 2)],
 hover=TH(("", "Nobody bid against Paddy; his limit was 10."),
          ("Paddy", "It goes on R24, beside the Scroll.")), at="R24")
lot(6, "WB", [
 B(5, 6), B(7, 7), B(5, 8), B(7, 9),
 B(5, None, "Take it, it's yours. I'll be back for the next one.")],
 hover=TH(("", "Reina stopped at 8; Graham would have gone to 12, or 15 to keep the Bowl from her."),
          ("Graham", "It goes on Q16, beside his Customs House.")), at="Q16")
lot(7, "VA", [
 B(6, 10), B(5, 11), B(6, 21), B(5, 22),
 B(6, 22.5, "Twenty-two and a half, and that's every grain I can spare and still keep my twenty. I won't pretend I've got more, Reina. If you go past it, it's yours, and I'll shake your hand.",
   "Paddy: If I win at that, I'm left with exactly twenty grain and holding the full set, Jar, Deed, House and Vase. Reina can outbid me if she wants it badly enough, but it'll cost her nearly half of what she's got."),
 B(5, 23.5, "Paddy, you told the whole table that the Vase finishes your set, and I've just come off the throne, so I know exactly what that sentence means. Sorry, the Vase is coming to the coast.",
   "Reina: Paddy has to keep twenty in hand to declare, so anything much over twenty-two is out of his reach as a set-maker, and twenty-six makes sure he can't get there. It costs me some grain, but it stops a second coup this year and gives me the one piece nobody else can get."),
 B(6, None, "That's past what the paddies can bear. Well bid, and good luck to you with it.")],
 hover=TH(("", "A close lot: Reina's limit was 22 and Paddy's 21, so each had one raise, Reina to 26 and Paddy to 22.5."),
          ("Reina", "It goes on P22, where Silke had it.")), at="P22")
say("Paddy", "Right next to the Deed, there. Well played, Reina, I said I'd shake your hand and I will. But the Vase only has to come back round once, and when it does, I'll be the one waiting for it.",
 "Paddy: That's three of my four pieces sitting in a row at R22 to R24. Reina's got the Vase now, but she has nothing else, so if she climbs before I do, every piece goes back to stock and the Vase comes back up for auction.")
say("Graham", "Nine. I lost by one grain last year, so it's a pleasure to win by one this time. It goes next to my Customs House. Paddy, those two brushes in your stock: I'll be bidding on one when it comes up.",
 "Graham: Customs House and Bowl now, so I need a brush from Paddy's stock and that Jar. And Reina's paid twenty-three and a half for a Vase with no Bowl to go beside it, so she's stuck until I sell or she buys mine.")
say("Reina", "Back on the shelf where Silke had it, P22. Paddy, I'll take that handshake, and I mean it. You bid honestly and you stopped where you said you'd stop.",
 "Reina: That leaves me with twenty-seven and the only Vase in China, so whoever wants the throne next goes through the coast. Now I need the scroll, the brush and the bowl, and I need to rebuild my grain while I collect them.")
salaries({7:5}, text="Silke pays Graham 5 for reading the I Ching, as she promised.", hover="Nobody else at this table is on a salary.")

# ===== CHAPTER 3: Every Grain into the Ground
# ============================== YEAR 5 ==============================
R(5, "The villages are noisier", "half1")
act("Graham turns the fourth I Ching card: Population Grows by Half. The population has already grown by half once, so only the good harvest counts: a good harvest for every province, and no disasters. The population holds at 150 million, x1.5.", map_hl=[1,5,6,7])
say("Graham", "\"Population Grows by Half.\" It has already grown by half once, so that part doesn't count. Only the good harvest does. The counter stays at 150 million, times one and a half. Everyone reads the good-harvest column on the x1.5 row. Nobody plays a disaster this year.",
 "Graham: A good year with my Reservoir under it means the most grain I've had yet. The land is still shut until the population doubles, so I'm keeping it all together, and I'll want to see how much Paddy is asking for a brush.")
harvest("Graham pays out the harvest from the Harvest Pile.")
say("Silke", "A good harvest is a good year for everyone, the throne included. Forty percent, and in return the capital gets a Pagoda you can see from the coast. Reina, Paddy, look out your windows: that's your tax standing up in marble.",
 "Silke: Fifty-six in, twenty out for the cheapest work on the list, and Graham's five for the cards. The reserve goes up to about a hundred and eighty, which is what I'll need the day the population doubles and I have to buy land square by square. Graham owes the most this year and he's the one I'm paying, so watch whether he grumbles.")
taxes(.40, collector="Paddy collects the tax for the crown")
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="G22", text="Public works: Silke builds the Marble Pagoda on G22, in Province 1. It may only be built in a year when nothing else is, and it is the year's only project.", hover="Silke pays the 20, into the Harvest Pile. 320 of the works are still owed.")
act("The auctions. Paddy and Graham each hold only one type beside the board: Paddy puts up a Bamboo Brush, minimum 2, and Graham the Land Deed Scroll, minimum 6. Reina has nothing left in stock. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Reina", "Forty in a good year, Silke, and a Pagoda besides. I'll take that, and I'll hold you to the coast canal next. Graham, nobody else at this table needs that scroll, so let's not feed the Harvest Pile for nothing: open it at the minimum and it's mine for a few grain. Paddy, you've got two brushes, so there's one for each of us if Graham and I don't drive the first one up.",
 "Reina: Fifty-one grain, twenty held back for the claim, so I can spend about thirty this year on a scroll and a brush together. The scroll should go cheap because I'm the only one who needs it, but I'm watching Graham on the brush, because he owns the Bowl I still need, and I don't want him buying the same things I'm buying.")
say("Paddy", "Just the one Bamboo Brush from me, at two, and somebody's welcome to it. The Deed's no use to me, I've got one already on my paddies, so I'll keep my hands in my pockets for that one, Graham.",
 "Paddy: I'm not saying what anything's worth to me this year, not after last time. Every grain I don't spend on a lot I don't need goes towards the Vase and the twenty I have to hold back, and that's all I'm thinking about.")
say("Graham", "There are two brushes, Reina, so neither of us has to bleed for the first one. I'll go to a fair price and stop there. The Scroll opens at six. That's less than I paid to stand aside for Paddy's Customs House.",
 "Graham: Fourteen is my number. Past that the second brush comes cheaper next year, and three quarters of anything I overpay goes into the Pile. Reina is the one to watch: she has fifty-one grain, and she needs a brush as much as I do.")
lot(6, "BB", [
 B(7, 2), B(5, 6), B(7, 10), B(5, 12), B(7, 13),
 B(5, None, "Go on then. Paddy has a second brush, and I can wait a year.")],
 hover=TH(("", "Reina stopped at 12; Graham would have gone to 14."),
          ("Graham", "It goes on Q17, beside the Bowl.")), at="Q17")
lot(7, "LD", [B(5, 6)],
 hover=TH(("", "Nobody bid against Reina; her limit was 8."),
          ("Reina", "It goes on P23, beside the Vase.")), at="P23")
say("Graham", "Thirteen, one more than you, Reina. Paddy still has a brush in his stock, and it'll come cheaper than mine did. Enjoy the Scroll.",
 "Graham: That's three of the four: the Customs House, the Bowl and now the Brush, all in a row on the Q line. All I lack is the Dragon Jar, and Paddy is the only one who has one, so I'll be reminding him who stood aside for his Customs House.")
say("Reina", "Thank you, Graham. Six was a fair opening and I won't forget it. The deed goes next to the Vase, so the coast has two pieces now. Enjoy the brush, and save the second one for me, Paddy.",
 "Reina: That's two of four for forty-five grain left, and it means the Bowl in Graham's hands is the piece I'll have to buy, so I'll keep things friendly with him. He outbid me by one grain for the brush, so he's counting my shelf the same way I failed to count Silke's.")
salaries({7:5}, text="Silke pays Graham 5 for reading the I Ching.", hover="Nobody else at this table is on a salary.")

# ============================== YEAR 6 ==============================
R(6, "Fat years make large families", "double1")
act("Graham turns the fifth I Ching card: Population Doubles. A good harvest for every province, and no disasters. The population doubles for the first time, from 150 million to 300 million, x3, and new land opens: 20 a square, yielding 20 a year from next year.", map_hl=[1,5,6,7])
say("Graham", "\"Population Doubles. Fat years make large families.\" A good harvest in every province, but the counter goes to 300 million. That's times three now, so read the times-three row. Everyone's consumption doubles from here. Feed them while you still can.",
 "Graham: Six more mouths to the square and land still at twenty. This is the year I've been saving for, and I'll be buying squares before the other two have finished their sums.")
harvest("Graham pays out the harvest from the Harvest Pile; a negative income is paid into it.")
say("Silke", "Three hundred million mouths, and not one province with a grain of income to tax. So no marble this year. Every grain the crown has goes into the ground. I'll pay five on every square any of you buys, and I'm buying four for the north myself. Fill your fields first, then come and ask me for canals. Reina, the coast canal is still coming. It comes once there's a harvest to pay for it.",
 "Silke: A square pays twenty a year and a canal section pays ten for forty, so the Wall and the Canal can wait until somebody here has a taxable income again. Four squares gets the north close to even and leaves me about twenty in reserve for a bad harvest. Reina's down to twenty-five and holds the Vase and the Scroll, so she's the one I'm watching while everyone else plants.")
taxes(.40, collector="Paddy collects the tax for the crown")
act("Public works: Silke builds nothing this year. The Great Wall (160) and the Grand Canal (160) are still owed.", map_hl=[1])
buy_land(1, ["F23", "F24", "F25", "F26"], {1:80}, "New land: Province 1 buys four squares of sea, F23 to F26, for 80, paid by the crown into the Harvest Pile. Each yields 20 from next year's harvest.")
say("Reina", "Silke, five a square is a kind offer to someone who has the grain. I have twenty-five. Here's every grain I can put in the ground, twenty for two squares, and I'm asking the crown to match it, ten a square. Three hundred million mouths on the coast is your problem as much as mine, and an empty coast doesn't pay for canals.",
 "Reina: Two squares cuts my loss from forty-five a year to five. That keeps me out of debt, which means I can still buy and the coast doesn't revolt on Silke's watch. I'm asking her for twice what she offered, because if she won't feed the coast she'll be in trouble long before I am.")
say("Silke", "Eight a square, Reina. That's sixteen from the crown and twenty-four from you, and you've got twenty-five, so both squares go in the ground. I'm not tipping my last grain into the sea when Paddy and Graham haven't asked yet and Graham still needs paying for the cards. The coast gets its fields and the crown keeps its feet.",
 "Silke: Ten a square would bring me down to fifteen before Graham's five and the others' shares, and a broke crown can't pay anyone's share next year, Reina's included. At eight she still gets both squares, so nobody can call it a refusal, and the four grain I keep might be what keeps me out of debt.")
say("Reina", "Eight a square, done. Both squares go in the ground, and the coast keeps its feet as well, Silke. That's one grain left in my purse, so nobody at this table should be afraid of me this year.",
 "Reina: With both squares my average year goes from losing forty-five to losing five, so I'm close enough to even that one decent harvest gets me back on my feet. Being down to one grain also tells the table I'm no threat for the throne, and that's useful while I wait for Paddy's brush.")
buy_land(5, ["N26", "N27"], {5:24, 1:16}, "New land: Province 5 buys two squares of sea, N26 and N27, for 40: Reina pays 24 and the crown 16, 8 a square. Each yields 20 from next year's harvest.")
say("Paddy", "Three squares for the south-east, Silke. That's forty-two from me and six a square from the crown, and I know what's left in your chest after Graham's paid, so I'm not asking for Reina's eight. Three hundred million mouths won't eat pots, and I'd rather owe nobody than sit on grain while my paddies go hungry.",
 "Paddy: Three squares is what it takes to stop losing forty-five grain a year, and if the game ends next year they still pay back more than I put in. It leaves me well short of the Vase for now, but a man in debt can't buy anything, and I don't fancy being that man.")
say("Silke", "Five a square, Paddy, as I offered at the start. You can cover forty-five and still have grain in your pocket, and Reina couldn't. Once Graham's paid there's barely a handful left in the chest, and he hasn't asked for his share yet. I won't leave the south centre with nothing just to give the south-east one more grain a square.",
 "Silke: At six a square Graham's land would get nothing at all, and refusing a province its share is how revolts start. Paddy can pay the extra three grain easily, so he can grumble about it. He's got no grounds to march.")
say("Paddy", "Five a square it is, Silke, and fair enough. Graham's got to eat as well. Three squares go into the south-east, and I'll be back to four and a half grain, same as when I started out.",
 "Paddy: Three squares is exactly what I need to stop the paddies losing grain every year, so I'd sooner be poor and steady than keep nineteen and watch it drain away. The Vase can wait a bit longer. It'll come round again.")
buy_land(6, ["R25", "R26", "S26"], {6:45, 1:15}, "New land: Province 6 buys three squares of sea, R25, R26 and S26, for 60: Paddy pays 45 and the crown 15, 5 a square. Each yields 20 from next year's harvest.")
say("Graham", "Four squares for the south centre, Silke. One a square from the crown, four in all, and that still leaves your chest enough for my five. I've done the sums. I don't need your eight, and I'm not leaving you short to pay me.",
 "Graham: At three hundred million I'm twenty-five short a year, and four squares make that a profit of fifty-five, with twenty-seven and a half still in my purse for the Jar. I asked the crown for its last four grain so that when Silke's chest is empty, nobody can say I left her owing.")
buy_land(7, ["T14", "T15", "T16", "T17"], {7:76, 1:4}, "New land: Province 7 buys four squares of the Warlord's land, T14 to T17, for 80: Graham pays 76 and the crown 4, 1 a square. Each yields 20 from next year's harvest.")
act("The auctions. Paddy holds only one type beside the board, so his last Bamboo Brush goes up, minimum 2. Reina and Graham have nothing left in stock. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Reina", "One grain in my purse and the minimum is two, so the brush is safe from me this year, Paddy. Keep it on your shelf if nobody bids. I'll be good for it once the coast fields come in.",
 "Reina: Every grain I had went into land, so I can't bid for the brush. The only other player who'd want it is Graham, and he already has one. With luck it stays unsold until I can afford it next year.")
say("Paddy", "Two grain, and not a grain more, so it's open to anybody who wants it this year. If nobody does, Reina, it'll be on my shelf waiting for you once the coast comes in.",
 "Paddy: Nobody at this table has grain to spare, so I'd be daft to ask for more than the minimum. If it sells I'll get half a grain, and if it doesn't I've lost nothing, and I'll have a buyer next year.")
say("Graham", "Pass. I've got a brush, and I know what it looks like when someone buys a second one just to keep it from somebody. I won't do that. Paddy, the piece I'm waiting on is your Jar. I stood aside for your Customs House, and when you're ready to talk about that Jar, I'll be the one at this table with grain.",
 "Graham: Reina can't reach two grain, so a bid from me would only have bought a brush I don't need, and three quarters of it would have gone into the pile. My twenty-seven and a half is for the Jar, and with the whole table broke, I'm the only buyer Paddy's going to find.")
act("Paddy's Bamboo Brush opens at 2, and nobody bids: Reina has 1 grain, and Graham already holds a brush. It stays beside the board and must go up again next year at 2.", map_hl=[6])
salaries({7:5}, text="Silke pays Graham 5 for reading the I Ching.", hover="Nobody else at this table is on a salary. It takes the crown's last 5.")

# ===== CHAPTER 4: On the Slate
# ============================== YEAR 7 ==============================
R(7, "The seed rotted", "dribble3")
act("Graham turns the sixth I Ching card: Bad Harvest. A bad harvest for every province, and no disasters. The population holds at 300 million, x3. This year's incomes: Silke -30, Reina -30, Paddy -10, Graham +30. Before the harvest is paid out, the table may give, lend or trade.", map_hl=[1,5,6,7])
say("Graham", "Bad Harvest. \"The seed rotted, the rains came late, and the ox went lame.\" Every province collects a bad harvest. The counter stays at three hundred million, so that's times three. Read your bad-year row at x3 and count it before you spend anything you don't have.",
 "Graham: Bad years are where my Reservoir and those four squares pay off: I'll still come out ahead when nobody else at this table does. Paddy will feel it worst, and a man who's short of grain is a man who'll finally put a price on his Jar.")
say("Silke", "Well. The ox went lame on all of us except Graham. The crown has nothing in the chest because every grain went into the ground last year, just as I promised. Graham, lend the crown thirty and you get thirty-five back from the first good harvest, before a single brick goes on the Wall. A crown in debt can't put a grain into anyone's land, and next year we'll all want those squares. Reina, Paddy, hold onto what you have. Nobody here is going to starve this year.",
 "Silke: Graham is the only one at the table with grain, and he's also the only one I can tax. So I'd much rather borrow from him politely than squeeze him and leave the throne in debt. If he says yes he's my creditor, and a creditor wants the Empress to stay put.")
say("Reina", "Graham, you're the only one at this table with a harvest this year, so I'll say it plainly. Lend me twenty-nine and I'll pay you back thirty-four, and you have my word in front of everyone that I won't bid against you for anything you want next year. You can carry the crown and the coast both: after your thirty comes in you'll have sixty-two and a half. Silke, I'm not trying to take your loan away from you. I just don't want to be the first person at this table to go into debt.",
 "Reina: A woman in debt can't bid, and Paddy's brush goes up at two, so I need twenty-nine grain more than I need my pride. Graham can afford both of us. The real question is whether he'd rather have the crown owing him or me.")
say("Paddy", "Graham, I'm short five and a half this year, and I'd rather ask you out loud than lose my pots to the Harvest Pile at two apiece. Lend me six and you'll have seven back from my first harvest before I spend a grain on anything else. It's the smallest ask at the table, and you know I paid what I owed on the Customs House.",
 "Paddy: Minus ten on four and a half leaves me in the hole, and if I can't cover it they sell my Jar, Deed and House at two each, and that's my whole set gone. Six from Graham keeps everything on my paddies, and I'll sleep badly until he's paid back.")
say("Graham", "Paddy, you asked me for six. I'll give you twelve, outright, for the Jar. That covers your harvest, you keep your other pots, and nothing goes to the Pile at two. Silke, I'll lend the crown twenty for twenty-five back, which is what I can spare. Reina, I'm sorry. I can't carry the whole coast, and I've already said where my grain is going.",
 "Graham: The Jar is worth twelve to Paddy and the whole game to me, and with it in my hand I've got my set and the twenty to spend on it. Silke gets enough to stay out of the worst of it and owes me for it, and I'd like her to remember that the next time she reaches for a brush she doesn't need.")
act("Graham lends the crown 20 before the harvest, to be repaid 25 from the first good year's tax, before any building. He declines Reina's request, and offers Paddy 12 for the Dragon Jar instead of a loan.", "Grain may be given or lent at any time (Section 5); no deal is binding.", {pid(7): -20, pid(1): 20}, map_hl=[1,7], deal=True)
say("Paddy", "Graham, that Jar cost me more than any field I ever planted, and twelve's a thin price for the piece that finishes your set. Make it twelve now and six more when your harvest comes in, and you'll still have the twenty to change seats. If twelve is truly all you've got in you, I'll shake on twelve anyway, because I'd rather it went to you than to the Pile at two.",
 "Paddy: Either way the Jar's leaving me: it goes to Graham, or all three of my pots go back to the Pile and I'm left with half a grain. So I'll ask what's fair, I won't haggle so hard I lose the lot, and I'll keep my eye on Graham, because he's about to have a full set and a harvest.")
give(pid(6), pid(7), "DJ", at="Q18")
act("Graham buys Paddy's Dragon Jar for 12, before the harvest. Paddy's ask of 6 more after the harvest is still open. The Jar moves from R22 to Q18, beside Graham's Customs House, Bowl and Brush: the Wheat Peasant's set is complete.", "A trade of a piece on the board, at any time (Section 5).", {pid(7): -12, pid(6): 12}, map_hl=[6,7], deal=True)
sell_back(pid(5), ["VA", "LD"], "Reina can't cover her -30 from the 1 she holds, so before the harvest is paid both her pieces go back to the Harvest Pile at 2 each: the Vase from P22 and the Land Deed Scroll from P23. They go into the pile's own stock, which it auctions after the provinces' lots.", "Sell before you sink: a payment that would take a player below zero is first covered by selling realia on the board back at 2 a piece; only the shortfall left becomes a debt.")
harvest("Graham pays out the harvest from the Harvest Pile; a negative income is paid into it. The crown goes from 20 to -10 and Reina from 5 to -25, both in debt; Paddy ends at 6.5 and Graham at 30.5.")
say("Graham", "Paddy, you said you'd shake on twelve, and you meant it. That's why you get the other six. Here. And I'm staying where I am. Province 7 is the best farm on this board, and I'm not trading it for anybody's debt.",
 "Graham: Reina's seat comes with minus twenty-five and Paddy's comes with a worse farm than mine, so either swap hands my Reservoir and four new squares to someone else. The set stays on Q15 to Q18 with twenty-four and a half behind it, ready to use the year the numbers say so, and that year isn't this one.")
act("Graham pays Paddy the 6 more he asked for the Jar, 18 in all, and keeps the Wheat seat with his set on the board.", "Any payment between players is a deal (Section 5).", {pid(7): -6, pid(6): 6}, map_hl=[6,7], deal=True)
say("Silke", "Graham, you'll get your twenty-five back in the first good year, exactly as agreed. But a man who can pay eighteen for a Jar in a rotten harvest can pay fifteen in tax. That's fifty percent, and since you're the only one with a harvest, you're the only one who owes it. It clears the crown's debt and leaves five for the land. Paddy, the first square anyone buys this year gets five from the throne. Reina, get out of debt and I'll be back at your side. Nobody builds this year, because nobody can afford to.",
 "Silke: Graham just finished his set with twenty-four in his hand, and suddenly the only honest man at this table is twenty grain away from my chair. Fifteen in tax leaves him nine and a half, so whatever he says about staying put, this year he can't move.")
taxes(.50, collector="Paddy collects the tax for the crown")
act("Public works: Silke builds nothing this year. The Great Wall (160) and the Grand Canal (160) are still owed. The tax has paid the crown's debt, leaving it 5; it offers 5 on the first square any province buys this year and 1 on each after. Reina is in debt, so she can't buy land.", map_hl=[1])
say("Paddy", "Thank you, Silke, and I mean it, but even with your five a square's fifteen to me, and I've only twelve and a half. I'm not going into debt for land, so I'll hold what I've got and come back for a square when I can pay my own share of it. And Graham, thank you for the six. You didn't have to give it.",
 "Paddy: I sold the Jar, so the Vase can't finish my set any more, and I'll sit on this twelve and a half and not lose my head at the auction. Graham's holding a full set and says he won't move, and I'll believe that for exactly as long as he doesn't move.")
say("Graham", "Fifteen from the only harvest at this table, a year after I paid seventy-six to plant the crown's fields. I've written it down, Silke. No land for me this year. Nine and a half doesn't make a square, and I don't buy what I can't pay for.",
 "Graham: That leaves me at nine and a half: under the twenty a seat change costs, and twenty-five owed to me by the woman who just taxed me for it. She once took a brush she didn't need. Now she's taken half the one harvest in China. I'm counting both.")
act("No new land this year: Paddy and Graham each decline, and Reina is in debt. The board stays at thirteen squares. The Storyteller notes that Graham's 76 in Year 6 bought Province 7's own squares, T14 to T17.", map_hl=[6,7])
act("The auctions. Paddy's Bamboo Brush, unsold last year, must open at 2. Then the Harvest Pile's own stock goes up: the Vase and the Land Deed Scroll Reina sold back, minimum 2 each. Graham has nothing left in stock and Reina is in debt, so she can't bid. The Emperor doesn't bid.", map_hl=[5,6,7])
say("Paddy", "Three times I've reached for that Vase. I'll put a couple of grain on it this time and no more, because without the Jar it's only a pretty pot, and I'm not paying over the odds for a pretty pot.",
 "Paddy: The Vase can't finish anything for me now, but at two or three grain I'd rather it sat on my paddies than went back round to someone who needs it more. Graham's got the Jar I'd need to go with it, so I'll keep the rest of my grain for land next year.")
say("Graham", "I'm passing on all three. I've got my set, and every grain I spend at auction is three-quarters gone to the Pile. Paddy, the Vase is yours to take if you want it.",
 "Graham: Nine and a half grain, and I need twenty to use the set. I won't get there by buying pots I don't need. Paddy owes me some goodwill now, and I'd rather he spent his grain than I spent mine.")
act("Paddy's Bamboo Brush opens at 2 and nobody bids: Reina is in debt, and Graham already holds a brush. It stays beside the board and must go up again next year at 2.", map_hl=[6])
lot(0, "VA", [B(6, 2)],
 hover=TH(("", "Graham passed; Paddy's limit was 4. A pile lot's price goes to the pile whole."),
          ("Paddy", "It goes on R22, where the Jar used to sit.")), at="R22")
act("The Harvest Pile's Land Deed Scroll draws no bid at 2. It stays in the pile's stock and goes up again next year at 2.", map_hl=[5])
say("Paddy", "Two grain for the Vase, after all that. Thank you for standing aside, Graham. It's going where the Jar used to sit, so I'll see that empty spot every morning.",
 "Paddy: I've got the Vase, the Scroll and the Customs House now, so all I'm missing is the Jar on Graham's farm. If he ever wants to sell it back, I'll have the grain ready, and I'll have to be patient until then.")
salaries({7:5}, text="Silke pays Graham 5 for reading the I Ching.", hover="Nobody else at this table is on a salary. It takes the crown's last 5; the crown ends the year at 0, owing Graham 25 on his loan.")

# ============================== YEAR 8 ==============================
R(8, "Who paid for the ditch", "share")
act("Graham turns the seventh I Ching card: The Emperor's Share. An average harvest for every province, and no disasters; the population holds at 300 million, x3. Every province with a public work pays the Emperor half the extra harvest it brings: only Province 7's Reservoir (+20) is outside the crown's province, so Graham pays Silke 10 after the harvest. This year's incomes: Silke -5 (then +10), Reina -5, Paddy +15, Graham +55 (then -10). Before the harvest is paid out, the table may give, lend or trade.", map_hl=[1,5,6,7])
say("Graham", "The Emperor's Share. \"The Emperor would like to remind you who paid for the ditch.\" Average harvest everywhere, three hundred million, so read the x3 row. Every province with a Public Works gives the Emperor half of what it adds this round. I'll remind the table that I paid twenty of that ditch myself.",
 "Graham: The only working Reservoir is mine, so half of my twenty goes to Silke, on top of last year's fifteen in tax and the twenty-five she still owes me. I'm keeping count, and it's a long list now.")
say("Silke", "Graham, you wrote it down, so write this down too. The ten you send the crown for that Reservoir goes back into your fields this year, ten a square, and Paddy gets the same. Reina, I can't hand you grain I haven't got, but the coast is still my first canal when the chest can carry it. This is an ordinary year, and I mean to tax it like one.",
 "Silke: With Reina's shelf empty and her chest in debt, no Silk set at this table is coming for my chair, and Graham's wheat can only take Paddy's seat or Reina's. So this year I can afford to be generous with Graham, and I'd rather have him angry at the coast than at me.")
say("Reina", "Graham, last year you told me you couldn't carry the whole coast, and you were right, you couldn't. This year you'll clear fifty-nine after the Emperor's Share. Thirty of that gets me out of the hole, and I pay back thirty-six the first year the coast makes money. I've got nothing left to sell, so all I can offer is my word and my voice: you've heard me keep my word once already, and until you're paid back I side with you on every tax rate. Silke, if he does it, I want your share on my first square, the way you promised Paddy his.",
 "Reina: In debt I can't buy land, I can't bid and I can't claim, so I'm a ghost at my own table, and Graham is the only one who can make me real again. My vote is the only thing I have left to sell, and after a fifty percent tax on him alone, he might just want it.")
say("Paddy", "Graham, you've told the whole table you're staying on the best farm in China, so the Jar's no use to you except sitting on a shelf. I'll give you twenty for it after the harvest, two more than you paid, and in grain I've actually got. Reina, I'm sorry, I've nothing to spare for the coast, but I won't vote you down on the tax either.",
 "Paddy: With the Jar back I'd have the whole set again, and then I'd only need to save the twenty to make it count. I'm not saying out loud whose seat I'd be looking at, but Reina's in the hole, and whoever I replace draws sixty from the Pile, which might be the kindest thing anyone does for her this year.")
harvest("Graham pays out the harvest from the Harvest Pile; a negative income is paid into it.")
act("The Emperor's Share: Province 7's Reservoir adds 20 to Graham's harvest, so he pays Silke half of it, 10. The crown goes from -5 to 5.", "The Emperor's Share card: provinces with works pay the Emperor half their works bonus this round.", {pid(7): -10, pid(1): 10}, map_hl=[1,7])
say("Graham", "Reina, I'm sorry. Thirty grain in exchange for \"the first year the coast makes money\" is a promise with no date on it, and the tax hasn't been called yet. Paddy, I paid eighteen for that Jar in the worst year we've had, and twenty won't buy it back. A set on my shelf is worth more to me than two grain.",
 "Graham: If Paddy has the Jar with his Vase, he's a Scroll and a Brush from a set, and then he could take my seat and my farm with it. So the Jar stays on Q18. I'm keeping my fifty-nine and a half whole until Silke names her rate, because last year she showed me what an \"ordinary\" tax looks like.")
say("Silke", "Fifty percent. That's thirty-five out of a table that just paid Graham fifty-five, and every grain of it goes back into the ground. One square for the north so the throne stops eating its own reserve, and ten a square on your first two, Paddy, Graham, just as I said. Reina, once you're clear of debt, the coast canal is the first stone I lay.",
 "Silke: I'd rather squeeze Graham into buying fields at half price than leave him sitting on sixty grain, and the square for Province 1 finally stops the crown bleeding five a year. The Wall and the Canal can wait. Every year they wait is another year I'm Empress.")
taxes(.50, collector="Paddy collects the tax for the crown")
act("Public works: Silke builds nothing this year. The Great Wall (160) and the Grand Canal (160) are still owed.", map_hl=[1])
buy_land(1, ["E23"], {1:20}, "New land: Province 1 buys one square of sea, E23, for 20, paid by the crown into the Harvest Pile. It yields 20 from next year's harvest. The crown offers 10 a square on the first two squares Paddy or Graham buy this year, and 1 a square after.")
say("Paddy", "My mistake, I counted the tax wrong. Just the one square, then, R27, ten from me and ten from the crown. That leaves the crown's other ten for Graham's first square, which is only fair.",
 "Paddy: I'd sooner keep eight grain in hand than ask the throne for more than it promised. One more paddy means next year's harvest is twenty better, and I don't owe anybody anything.")
buy_land(6, ["R27"], {6:10, 1:10}, "New land: Province 6 buys one square of sea, R27, for 20: Paddy pays 10 and the crown 10. It yields 20 from next year's harvest.")
say("Graham", "One square, T18. Ten from me and ten from the crown, as promised. Thank you, Paddy, for leaving it there. That's twenty a year for ten of mine, and even I can't argue with those numbers.",
 "Graham: For ten grain I get at least twenty back, even if the Wall ends the game next year. A second square at nineteen would leave me with three, below the twenty the set needs to move, and I've learned at this table to keep a margin.")
buy_land(7, ["T18"], {7:10, 1:10}, "New land: Province 7 buys one square of the Warlord's land, T18, for 20: Graham pays 10 and the crown 10. It yields 20 from next year's harvest. Sixteen squares now.")
act("The auctions. Paddy's Bamboo Brush must open at 2, unsold last year, and then the Harvest Pile's Land Deed Scroll at 2. Reina is in debt and can't bid; the Emperor doesn't.", map_hl=[5,6,7])
say("Paddy", "I've already got a Scroll, so I'm passing on this one. Reina, I'd keep it back for you if I could, but the rules won't let me. The Brush is still on my shelf for whoever wants it.",
 "Paddy: Eight grain's all I've got, and a second Scroll would only be paper. I'll keep it for the harvest and see whether Graham changes his mind about the Jar.")
say("Graham", "I'm passing on both. I have twenty-two, and twenty of it is spoken for.",
 "Graham: The only one who needs these is Reina, and she's thirty in debt and can't bid. They can stay in stock, and my set keeps the two grain of margin it has.")
act("Nobody bids: Paddy's Bamboo Brush and the Harvest Pile's Land Deed Scroll both stay unsold, and both go up again next year at 2.", map_hl=[5,6])
say("Silke", "Graham, the chest is empty because every grain went into your field, Paddy's and mine. I won't put the crown into debt to pay you with grain I'd only have to borrow back. Your five goes on the slate, so that's thirty owed, and it's the first thing paid out of next year's tax. Same jobs as before. Nobody at this table has done them badly.",
 "Silke: Graham told us twenty of his twenty-two is spoken for, and twenty is the price of changing seats, so I'll keep him reading my cards where I can see him. Paddy or Reina had better be counting too.")
act("Salaries: the crown holds 0, so Silke defers Graham's 5 for the I Ching; the crown now owes Graham 30 (the Year 7 loan's 25 and this 5), to be paid first from next year's tax. The jobs stay as they are for Year 9: Paddy collects the tax; Graham banks the Harvest Pile and reads the I Ching.", "An appointee's pay is the Emperor's choice (Note 3).", map_hl=[1,7])
