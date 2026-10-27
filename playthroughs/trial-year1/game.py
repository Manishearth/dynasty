# Pilot — an agent-played game of Dynasty. Five players: the peasant game's table.
# Every say and aside is the reply of the agent playing that seat (see log/year1/).
# The Storyteller writes the act lines and refs the moves; the engine keeps the books.
# Seed and deck order: seed.md.
setup([1,5,6,7,8], "pilot", "The pilot game",
      "Five players · played by agents",
      "The Emperor, three peasants and the Warlord, each played by its own agent. The Storyteller referees with the engine.",
      short="5 players · agents")

# ============================== SETUP ==============================
R(0, "Setup", None, "Five players: the Emperor, the three peasants and the Warlord (rulebook Section 4 and Appendix A). Nobody sits in Provinces 2, 3 or 4, so nothing is owed to them, and their table jobs go to whoever the Emperor names (Note 3).")
act("Five booklets: Reina Osorio draws the Emperor, Silke Weber the Silk Peasant, Paddy Doyle the Rice Peasant, Graham Garner the Wheat Peasant and Robert Land the Warlord.", map_hl=[1,5,6,7,8])
deal_grain("The Harvest Pile deals 60 to each player. It is the first year's harvest.")
take_stock("Silke, Paddy and Graham take their realia out of the box: one piece of their own and two of the piece they'll never need. It waits beside the board until it's sold.")
act("Graham cuts out the Province 7 Reservoir, two squares by two, and sets it aside until it's built.", map_hl=[7])
# 001 Rob
place_army({"W1":"O18", "W2":"R25"}, "Robert Land stands his two soldiers on undeveloped land: W1 on O18, the notch where Provinces 5 and 7 meet, and W2 on R25, in the sea off Paddy's coast.",
 "Rob: The notch puts W1 one step from both Silke and Graham, and R25 sits off Paddy's coast with five of his squares in reach, so all three peasants have to place their first realia knowing I'm watching. Keeping my sixty grain is just the cherry on top. Let them find out what a booklet that says \"refuse\" is worth.")
say("Rob", "Your Majesty, the desert thanks you for your kind tax notice and has used it to light a campfire. Silke, Graham, Paddy: lovely provinces. Do think hard about where you put your new treasures. I certainly will be.")

# 002 Reina
act("Reina appoints Paddy Doyle to bank the Harvest Pile, and Graham Garner to read the I Ching and keep the population count at the Scholar's salary of 5 a year. She'll collect the tax herself.", map_hl=[1,6,7])

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
say("Reina", "Thirty percent, friends: eighteen from each of you, and every bag goes back into stone. The Winter Palace goes up this year so the Canal can reach Silke's and Paddy's coasts, and Graham's Reservoir is next on my list. Rob, enjoy your campfire. Deserts get cold, and that's the only warmth you'll get from this court.",
 "The Winter Palace is the key that opens the canals, which means bigger harvests and more to tax later. I've given jobs to Paddy and Graham because a revolt needs two peasants, and I'd like two of them to have a reason to stay loyal. G21 sits inland in the middle of my province, about as far from Rob's ships and his desert as I can put it, because a raid on a palace square costs me double.")
taxes(.30, collector="Reina collects the tax herself")
act("Robert Land declines to pay tax.", map_hl=[8])
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="G21", text="Reina builds the Winter Palace on G21 and pays the 20.")

# 003 Silke: puts up the Jar; 006-010 the bidding
say("Silke", "There's only one Dragon Jar in all of China, gentlemen, and two of you need it. Opening at eight. Paddy, Graham, do be generous. Rob, you can bid too if you like, but I promise it won't keep you warm.",
 "I'm selling the single piece first, while Paddy and Graham both still have full purses and both have to have it. Whatever they spend fighting each other now is grain they won't have when I'm the one bidding on their Vase and Bowl.")
lot(5, "DJ", [
 B(8, 12, "Twelve, Silke. It's a beautiful jar, and it would look very handsome out on the dunes where nobody else could reach it. Gentlemen, you're welcome to save it from me.",
   "I don't need the Jar, but every bag of grain Paddy and Graham spend outbidding me is a bag they can't spend on buying my soldiers."),
 B(6, 14, "Fourteen for the Jar, Silke. It's a lovely jar and I'd give it a good home, well back from the sea. Graham, no hard feelings, I hope. I'll be fair with you over the Bowl in a minute, and that's a promise.",
   "Graham and I both need this one, so I've gone in firm to put him off without emptying my sack, because I've still four pieces to buy and twenty grain to keep. If it's mine it goes on R21, where neither of Rob's soldiers can get at it this year or next."),
 B(7, 16, "Sixteen. That's double the opening, Silke, so you can see I mean it. If it comes home with me it goes in the far corner by the desert, well away from anyone's boots.",
   "There's only one Jar, and if Paddy gets it I have no way of finishing, so I'm putting in a serious bid now and keeping enough back for the Bowl. Whatever I win goes on P13, five steps from Rob's nearest soldier."),
 B(8, None, "Sixteen! Graham, you've outbid a man who has no use for it at all. Very well, I bow out. And thank you for telling the whole table it'll sit in the far corner by the desert. I'll make a note of that, since you're the one keeping records.",
   "I've pushed the price up by eight without spending a grain, and Graham has just told me where the Jar is going: right next to my notch."),
 B(6, 19, "Nineteen. I'm sorry, Graham, I truly am, but there's only the one Jar and I can't go home without it. Rob, I'm afraid the dunes will have to manage on their own.",
   "There's no second Dragon Jar, so if I lose this one my objective's finished, and I've decided to pay what it takes. Every grain Graham spends chasing it is a grain he can't spend on my Bowl later, so this fight doesn't cost me as much as it looks."),
 B(7, 24, "Twenty-four. Paddy, none of us has room for hard feelings this year. And Rob, the records show I said 'the far corner'. I never said which one.",
   "If Paddy gets the only Jar I can't finish, so I'm going to twenty-four and leaving eighteen in the bag for the Bowl. I've also moved it from P13 to S13, which is just as far from his soldiers, now that Rob's 'making notes'."),
 B(6, 27, "Twenty-seven. My mother always said never come home without the jar, Graham, though in fairness she meant pickles. That's my last word on it, I think. Well, probably.",
   "That leaves me fifteen, plus my quarter of whatever the Bowl fetches, and the harvest starts coming in next year, so I can still buy the Scroll, the Vase and the Customs House and keep my twenty. If Graham goes higher, he'll have hardly anything left to bid on my Bowl with."),
 B(7, None, "Pass. It's yours at twenty-seven, Paddy. Give your mother my regards. I've written it down.",
   "If I won at twenty-eight I'd have fourteen left for the Bowl against Silke's full purse, so I'm letting Paddy empty his bag on the Jar instead. When my Vase comes up he'll have very little to bid with, and Silke and I can settle the rest."),
], hover="Paddy: If it's mine it goes on R21, where neither of Rob's soldiers can get at it this year or next.", at="R21")

# 004 Paddy: puts up the Bowl; 011-013 the bidding
say("Paddy", "Right, well, I'll not keep anyone waiting. There's only the one Wooden Bowl, and Silke and Graham both need it, so here it is, minimum ten. I'm told that's a fair price for a good bowl. And Rob, I can see your fellow out there paddling off my coast, so I'll thank him to keep his boots dry.",
 "There's only one bowl and two people who need it, so I'm putting it up while Silke and Graham each still have forty-odd grain to fight over it. I keep a quarter of whatever it goes for, and I'm holding off on Rob's soldiers until I've got something on my land worth guarding.")
lot(6, "WB", [
 B(8, 12, "Twelve for the Bowl, Paddy. Twenty-seven for a pickle jar, and now you've fifteen left to defend the coast. Silke, Graham, I'd hate to see a good bowl go to waste out in the sand.",
   "Paddy's down to fifteen, so he can't afford one of my soldiers now, and that Jar on R21 is three steps away from both of mine. Meanwhile I'll keep putting a floor under the Bowl so Silke and Graham bleed a bit more."),
 B(5, 18, "Eighteen for the Bowl, Paddy. And thank you for the twenty-seven; my quarter's already in the jar, so to speak. Graham, you've just spent a lot of breath on the far corner. Do you really want to spend grain on a bowl too?",
   "Paddy just spent his purse down to fifteen, so this Bowl is really between Graham and me, and I'd rather open high and look like I mean it than get dragged up in twos. If I win, it goes in the far north at L24, six steps from anything Rob owns."),
 B(7, 20, "Twenty for the Bowl. I'll be quick about it, Silke, before you've counted your six and a half.",
   "Paddy has the only Jar now, so I won't finish without making a deal with him. Holding the Bowl and the Vase gives me two things that both of them need."),
 B(8, None, "Twenty! Too rich for a simple desert man. Ladies, gentlemen, carry on. I'll just sit here and count how much grain stays in my pocket while you empty yours.",
   "I passed without spending a grain again, and whichever of them wins, the Bowl has to go down on a square I'll be marching toward next."),
 B(5, 25, "Twenty-five. I've counted my six and a half, Graham, and I've counted yours too. You've still got a Jar to chase and a Customs House to buy from me. How many of those can forty-two pay for?",
   "There's only one Bowl, and without it my objective is dead, so I can't let it go. Graham's purse has to cover the Jar fight he's already lost, my Customs House and this, and mine only has to cover this, so I'm going to make him feel every grain."),
 B(7, None, "Pass. It's yours at twenty-five, Silke. You counted my grain correctly. Count your own again tonight, though, because you still need a Vase and there's only one.",
   "With Paddy holding the only Jar, the Bowl would only have been worth something as a way of blocking Silke, and not for twenty-six. Now both of them have spent heavily and both still need my Vase, so I'm the one with something left to sell."),
], hover="Silke: If I win, it goes in the far north at L24, six steps from anything Rob owns.", at="L24")

# 005 Graham: puts up a Scroll; 014-016 the bidding
say("Graham", "One Land Deed Scroll, minimum four. There are two of them and there are two of you, so there's no need to fight over it. The Vase stays beside the board for now. I've written down that the Reservoir is 'next on the list', Your Majesty. I keep the records now, after all.",
 "Silke and Paddy each need a deed, so that's an easy, quiet sale. They both need the Vase too, and there's only one, so I'm keeping it back until they've had a harvest and have something to fight with. I'm not giving Rob twenty a soldier until I own something worth guarding.")
lot(7, "LD", [
 B(5, 5, "Five for the Scroll. There are two of them, Paddy, so I'm not fighting you for this one. Take it if you want it, and I'll have the other next year at whatever price Graham can still get.",
   "I'm down to twenty-three and a half after the Bowl, and with two Scrolls on offer there's no reason to bleed for this one. A cheap bid in case nobody cares; if Paddy wants it, he can drain his purse instead of mine."),
 B(6, 6, "Six for the Scroll, Graham. Silke, there's two of them, so whichever of us gets this one, the other gets next year's. No sense us burning grain over it after the day we've both had.",
   "There are two Scrolls and only two of us need one, so I'm not going to start a bidding war over it. I've got twenty-one and I need twenty at the end, so I'm keeping it cheap and the harvest can carry me from here."),
 B(8, 8, "Eight for the Scroll, Graham. Silke, Paddy, you've both got about twenty grain left and a whole coastline to look after. Bid carefully, now.",
   "There are two Scrolls, so even if I win this one it's only a cheap way to make one of them wait a year, and squeezing two peasants who are both down to twenty-odd grain suits me fine."),
 B(6, 10, "Ten. Rob, you've no more use for a land deed than a fish has for a hat. Silke, if he gets this one, there's only one left for the two of us, so I'll hold the line here if you don't mind.",
   "Rob's only bidding to hold one of the two Scrolls hostage, so Silke and I end up fighting over the other, and I'd sooner pay a bit more now than a lot more next year. I'm down to eleven after this, so it's the harvest I'm counting on now."),
 B(5, 11, "Eleven. Rob, you don't need a Scroll, you need someone to sell it back to at three times the price. Paddy, he's not bidding against me, he's bidding against both of us. I'll take this one, and next year's is yours, no fight from me.",
   "If Rob wins a Scroll, there's only one left for Paddy and me, and that turns a friendly pair into another Jar war. Eleven hurts, but it keeps it off the desert, and it keeps Paddy on my side for next year's lot."),
 B(6, None, "I'll pass, Silke, and I'll hold you to that in front of everyone: next year's Scroll is mine, and no fight from you. Graham, you're keeping the records, so write that down for me, would you?",
   "Silke wants it as much as I do, and she's promised me the next one in front of the whole table, so I'm saving my eleven grain instead of helping Rob push the price up. If Rob goes higher than her, at least she's the one paying for it this time, not me."),
 B(8, None, "Silke, you wound me. I'd never sell anything back at three times the price. Twice, maybe. Take it at eleven, with my blessing. Do let me know which square you choose.",
   "Silke is down to about twelve grain now, so none of the coast can afford to buy a soldier from me, and that's worth more than any scroll."),
], hover="Silke: L25, beside the Bowl in the far north of my province.", at="L25")

# 017 Rob: the march and a hire
march({"W1":"P19", "W2":"R24"}, "Robert Land's soldiers step in: W1 from the notch to P19, raiding Silke's Province 5, and W2 ashore from the sea to R24, raiding Paddy's Province 6.",
 "Rob: Both soldiers are now closing in on Paddy's Jar from two sides, and the new man at T16 is waiting for wherever Graham puts that Vase.")
say("Rob", "Five from you, Silke, and five from you, Paddy. Think of it as a toll for all that lovely bidding. And Graham, don't feel left out. I've just hired a friend to sit under your southern border and keep you company.")
hire_soldier("T16", "Robert Land hires a third soldier, W3, for 20 and stands it on T16, in the desert under Graham's southern border.")

# 018-019 End of Year 1: the provinces' soldiers (none bought), table talk, salaries
say("Silke", "Pass. Seven and a half grain and two treasures in the far corner, Rob, so come and fetch them if you've got the legs. Graham, I've the second Customs House coming up and you need one. Let's talk about that Vase before either of us spends a grain we can't spare.",
 "I'm nearly broke, but I hold half my set and it's six steps from any soldier, so this year I let the harvest refill me. The Vase is the only piece that can still kill me, and Graham needs my Customs House, so that's where my leverage goes next.")
say("Paddy", "Five grain for a wet pair of boots on my beach, Rob, that's daylight robbery. Your Majesty, if the Canal's coming to my coast, I'd be grateful if it came with a guard or two. I'll be buying my own as soon as the rice is in.",
 "I can't afford a soldier until the harvest comes in, but the harvest comes first thing next year, before Rob's man at P19 can reach the Jar, so I'll buy a guard and stand him on R21 then. Until then I'm keeping my head down and my sixteen grain in my pocket.")
say("Graham", "No soldiers. There's nothing in my province to guard but the dirt, Rob, and your friend is welcome to stare at it. Paddy, I've written it down: next year's Scroll is yours, by Silke's word. I've also written down that I'm the only one with a Vase. You and I should talk about that Jar before I put the Vase up. Your Majesty, my five, when you're ready.",
 "Silke has seven and a half grain and Paddy has sixteen, I've got forty-four and a half, and they both need my Vase, so this year has gone better than it looks. The Jar is my only problem, and Paddy is the one who needs a Vase badly enough to talk about it.")
act("Nobody buys a soldier, so no province's soldiers move.")
salaries({7:5}, text="Reina pays Graham the card reader's 5.")
say("Reina", "Graham, here are your five, and you can write down that I pay on time. Paddy, the Crown will lend you twenty, interest-free, so you can put a guard on that Jar. Rob, you'll be selling a soldier to the man you're hunting. Business is business, isn't it?",
 "Rob only takes the throne if he gets one piece from every peasant, and the Jar sitting two steps from his soldier is his easiest one, so twenty grain to protect it is cheap insurance for my crown. It also leaves Paddy owing me, which helps if anyone starts talking about a revolt.")
say("Paddy", "That's a kind offer, Your Majesty, and I won't forget it, but I'd rather not start the year owing the Crown. The rice comes in before Rob's man can get anywhere near my Jar, and I'll buy my guard then, cash on the nail. Graham, the Jar's not going anywhere, I'm afraid; I need it as much as you do. But I'll pay you fair grain for that Vase when it goes up, and you've seen I don't haggle mean.",
 "Rob's soldier at P19 is two steps from the Jar, so it can't reach it before the harvest lets me buy a guard on my own money, and twenty grain of debt to the Emperor would only make me easier to lean on. I'm not trading the Jar away either: I need it, and Graham will come back to me for grain soon enough.")

# ============================== END OF THE PILOT (Year 1) ==============================
RESULT = export("The pilot stops after Year 1; the scores below are only where everyone stands.",
 ["Year 1 of an agent-played game. Year 2 starts from state/year1.json."])
