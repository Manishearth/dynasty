# Game 2 — the peasant game. Five players, ends with every Public Work built.
setup([1,5,6,7,8], "peasant", "The peasant game",
      "Five players · nine years · everything gets built",
      "The Emperor and three peasants, and the Warlord. No Official, no Gentry, no Scholar — so no rent, and Reina hands out their jobs herself. She builds the reservoir first.", short="5 players · 9 years")

def appoint(text, hover, hl):
    act(text, hover, map_hl=hl)

# ============================== SETUP ==============================
R(0, "Appointments", None, "Five players: the Emperor, the three peasants and the Warlord (rulebook Section 4 and Appendix A). Nobody sits in Provinces 2, 3 or 4, so nothing is owed to them and nobody does their jobs unless the Emperor says so.")
act("Five booklets go in the box: the Emperor, the three peasants and the Warlord. Shuffled and drawn.", TH(
 ("Rob","Warlord. I'm starting to think the booklet chooses me."),
 ("Graham","Wheat. The booklet has opinions about me."),
 ("Reina","Emperor. Good. I've got plans.")), map_hl=[1,5,6,7,8])
say("Reina","There's no Official, no Gentry and no Scholar at this table, so I'm handing out their jobs.", TH(
 ("Reina","An Official skims, a banker fawns and a Scholar won't tell you the truth — it's all in their booklets. With nobody in those seats I get to choose who does each job, and I'm choosing on purpose."),
 ("Graham","She's nervous. She's being organised about it, but she's nervous.")))
appoint("Reina appoints Paddy Doyle to bank the Harvest Pile. Paddy sets out the bags where everyone can see them.", TH(
 ("Reina","The steadiest hands at the table, and the least likely to make a speech about it."),
 ("Paddy","Twenty-five hundred million in bags of every size, and I'm the one counting it. I've never held money I didn't owe someone. Exciting."),
 ("Rob","Not me? I'm hurt. I'd have been a wonderful banker.")), [1,6])
deal_grain("Paddy deals 60 to each player from the Harvest Pile. It's the first year's harvest.", TH(
 ("Paddy","Sixty, five times. Three hundred out of the pile before anybody's done anything."),
 ("Silke","Sixty, and no rent to pay out of it. I can feel the absence of a landlord already.")))
appoint("Reina appoints Graham Garner to read the I Ching and keep the population count, at the Scholar's salary of 5 a year. Graham shuffles the twenty cards and lays them face down.", TH(
 ("Reina","The man who counted my deferrals out loud for ten years can count the people. If the clock's going to be in somebody's hands, I want it in the hands of the person most likely to say what it says."),
 ("Graham","Five a year to read her the bad news. She's paying me to do what I'd do for free."),
 ("Silke","She's put her loudest critic on salary. That's either very wise or very funny.")), [1,7])
take_stock("Silke, Paddy and Graham take their realia out of the box: one piece of their own and two of the piece they'll never need. It waits beside the board until it's sold.", TH(
 ("Silke","A Dragon Jar and two Customs Houses. One Jar in the world, and two other people who need it."),
 ("Graham","Off the board until it's sold, so Rob can't raid it out of the box. That rule saves the whole table."),
 ("Rob","Nine pieces and not one of them on a square yet. I can wait.")))
act("Graham cuts out the Province 7 Reservoir: a paper square two by two, set aside until it's built.", TH(
 ("Graham","Two by two. The rulebook says there's no single correct size and gives you one anyway. I cut it out first, before anyone could tell me it wasn't needed."),
 ("Reina","He made it before I'd said a word. I'm reading that as a request."),
 ("Paddy","There's no Province 2 or 3 at this table, so it's the only cut-out we need.")), map_hl=[7])
place_army({"W1":"O18", "W2":"E21"}, "Robert Land stands his two soldiers on undeveloped land: one on O18, the notch where Provinces 4, 5 and 7 meet; one on E21, in the strip under the Wall, a step from the Emperor's door.", TH(
 ("Rob","The notch is the only way into the south-east that doesn't go through somebody's living room. From O18 I can step into Silke's province or Graham's. And E21 is one square from Province 1, where every raid is worth ten."),
 ("Reina","Seven squares of my province touch that strip. He's chosen the one that looks straight at the throne room."),
 ("Graham","And the other one's on my doorstep. Province 7 touches the desert on every side; there's no square I own that's more than two steps from it.")))
say("Reina","Robert. One square a year, the rulebook says. Even yours.", TH(
 ("Reina","His soldiers aren't weather. They walk, and I can see them coming."),
 ("Rob","One square a year, and my booklet says I may go anywhere. I intend to go everywhere, slowly.")))

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
say("Reina","I'll collect my own tax. Thirty per cent.", TH(
 ("Reina","No Official means nobody stands between me and the money, and nobody stands between me and the blame either. Thirty because it's year one and I'm going to need them to like me in year eight."),
 ("Paddy","No rent, either. No Gentry, no landlord. I'm going to enjoy this game.")))
taxes(.30, collector="Reina collects the tax herself")
act("Robert Land declines to pay tax. Again.", TH(
 ("Rob","Nothing in my booklet says I pay tax. Cheapest precedent I'll ever buy."),
 ("Reina","Fine. I've stopped planning around his tax. I'm planning around his soldiers.")), map_hl=[8])
say("Reina","Then I'll be buying soldiers from you, Robert, sooner than you'd like.",
 "He'll take the money, because the booklet makes him sell. That's the one lever I have, and I mean to pull it.")
say("Rob","Twenty each, Majesty. Same as always.", TH(
 ("Rob","She's going to arm herself. Good. I keep five of every twenty, and her soldiers can't move until I've raided her anyway."),
 ("Graham","He says 'same as always' like we're old friends. We are, unfortunately.")))
say("Reina","First build. The Winter Palace.", TH(
 ("Reina","Not because I want a palace. Because the booklet says I can't touch a single canal section in Provinces 5 and 6 until it stands. It's the key to everybody else's ditch."),
 ("Silke","She's built a palace and somehow it's for us.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="H24", hover=TH(
 ("Reina","H24, on the coast, three squares in from the strip. Deep enough that he can't reach it this year; not so deep that he raids his way across my whole province at ten a square getting there."),
 ("Rob","Three squares. I'll be there in three years. I'll be ringing the bell every year on the way."),
 ("","Reina pays the 20.")))
lot(5,"CH",[
 B(6,4), B(7,5),
 B(6,6,"Six.", TH(
   ("Paddy","There are two of these and two of us who want one. Graham'll get the other. Six is fine."),
   ("Graham","I'll take the next. There's no Official at this table — Customs Houses are just pottery that two of us need.")))],
 hover="Paddy puts it on S23, on the south edge of his province, well away from both soldiers.", at="S23")
lot(6,"BB",[
 B(5,5), B(7,6,"Six.","Two Brushes, and Silke and I both need one. No point fighting over the first of two.")],
 hover=TH(("Graham","Q16, in the middle of Province 7. Two squares from the desert, which in my province is as deep as it gets."),
          ("Rob","Two squares from the desert, and one of mine is standing on the desert.")), at="Q16")
lot(7,"LD",[
 B(6,5), B(5,6,"Six.", TH(
   ("Silke","Six, and there's another next year for Paddy. The pairs are easy. It's the single pieces — my Jar, Paddy's Bowl, Graham's Vase — that'll be the fight."),
   ("Paddy","She's worked it out already. One of each of our own pieces, and the other two of us both want it.")))],
 hover=TH(("Silke","P26, out east by the sea. Province 5 is seven squares deep and the only door is a two-square gap by the notch. I'm putting everything I own at the far end of the hallway, by the sea."),), at="P26")
march({"W1":"P17", "W2":"F22"}, "Robert Land's soldiers step in: one into Province 7 at P17, one into Province 1 at F22.", TH(
 ("Rob","Graham for five, the Emperor for ten. And P17 is next to Graham's Brush. I'm not taking it yet. I'm standing next to it so he can look at me."),
 ("Graham","He's one square from my Brush. Right. Noted."),
 ("Reina","Ten on the first raid of the night. He's coming for the palace, one square a year, and he's going to charge me for every one.")))
salaries({7:5}, text="Reina pays Graham the Scholar's salary of 5.", hover="Graham reads the cards and keeps the count. Nobody else at this table is on a salary.")

# ============================== YEAR 2 ==============================
R(2, "Fortune and misfortune", "goodevil")
say("Graham","Good harvest for all. Provinces 2, 4, 6 and 8 play a personal disaster — and 2 and 4 are empty, so that's Paddy and Rob.", TH(
 ("Graham","First card I read and I've already had to do the empty-province arithmetic out loud. Nobody's in 2 or 4. The card doesn't know that, but the table does."),
 ("Paddy","Of course it's me.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
disaster(6,"the only water buffalo breaks its leg in the middle of planting.", TH(
 ("Paddy","Banker for one round and the first thing I pay out of my own pocket is a buffalo."),
 ("Rob","Four for a buffalo. I'd have charged him five for the field.")))
disaster(8,"wounded in the legs. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Rob","So the soldier next to Graham's Brush stands still for a year, and the one in Province 1 keeps walking."),
 ("Graham","A year's grace for the Brush. I'll take it."),
 ("Reina","Which means his only raid lands on me, at ten. His bad card is my bad card.")))
taxes(.35, collector="Reina collects the tax herself")
say("Graham","Majesty, the reservoir.", TH(
 ("Graham","My booklet says the crown pays for it all, sixty million. Might as well ask early."),
 ("Reina","He said it on the second round. He's going to say it every round until I build it.")))
say("Reina","Yes. This round. Sixty.", TH(
 ("Reina","If I say 'after the Wall', he'll count the deferrals out loud until the table revolts. Twenty a year forever for the province with the worst land. It's the best sixty I'll spend tonight."),
 ("Graham","...oh. Oh, she means it."),
 ("Silke","He doesn't know what to do with his hands.")))
build("Province 7 Reservoir", 60, {1:60}, key="res7", at="R14:S15", hover=TH(
 ("Graham","R14 to S15, the south-west corner, away from the notch. It's a public work, so every time his soldier steps onto it he pays me five. I've built a moat that charges admission."),
 ("Rob","He's put it where I'd walk if I came from the south. I wasn't going to come from the south."),
 ("","Reina pays the 60.")))
say("Graham","I had a speech ready for year eleven.",
 "I genuinely did. Nine deferrals' worth of it. I'll have to find something else to be angry about.")
lot(5,"CH",[
 B(7,8,"Eight.","Eight for the other Customs House. Paddy had the first; this one's mine, as agreed in a silence nobody admitted to.")],
 hover=TH(("Graham","S13, the far corner from his soldier. Four squares from P17. I've got one soldier to worry about down here and I can count to four."),), at="S13")
lot(6,"BB",[
 B(5,7,"Seven.","Seven for the second Brush. Graham had the first. The pairs are going exactly the way the pairs should go.")],
 hover="Silke puts it on P25, next to her Scroll, at the sea end of Province 5.", at="P25")
lot(7,"LD",[
 B(6,7,"Seven.", TH(
   ("Paddy","Two of four. Now the hard part — I need Graham's Vase and Silke's Jar, and so does somebody else for each."),
   ("Graham","Everybody's two of four. Next round, all three of us sell the one piece we've got that the other two both want.")))],
 hover="Paddy puts it on S24, beside his Customs House. Nobody's soldier is anywhere near the south edge.", at="S24")
march({"W2":"G23"}, "Robert Land's northern soldier steps to G23 and raids Province 1 — the only raid his wounded legs allow. His southern soldier stays beside Graham's Brush.", TH(
 ("Rob","Ten from the Emperor again, and one square nearer the palace. The other one just stands there. Standing there is a kind of raid, if Graham's watching."),
 ("Reina","G23. One more square and he's on the palace."),
 ("Graham","I'm watching.")))
salaries({7:5}, text="Reina pays Graham 5.")

# ============================== YEAR 3 ==============================
R(3, "Rain and flood", "rainflood")
say("Graham","Good harvest for Provinces 1, 3, 6 and 7. Rivers flood in 2, 4, 5 and 8. So — good for Reina, Paddy and me. Bad for Silke and Rob.", TH(
 ("Graham","And my reservoir pays its first twenty this year. I read that card with a straight face, which took effort."),
 ("Silke","Bad harvest the year before I need every bag. Brilliant.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
taxes(.40, collector="Reina collects the tax herself")
say("Reina","Forty. Graham's reservoir earns its first twenty this year, and part of that twenty is mine.", TH(
 ("Reina","A public work raises a province's harvest, which raises its tax. That's the thing worth understanding early: a ditch pays the crown back. A wall never does."),
 ("Graham","She's taxing my reservoir. Fair. It's her reservoir too. I just live next to it.")))
build("Grand Canal in Province 5 — 2 sections", 80, {1:80}, canal={5:2})
say("Silke","Two sections in my province, and the crown pays.", TH(
 ("Silke","Twenty a year from next year, forever. I'm flooded and broke this round and the Emperor just bought me a river."),
 ("Rob","Two sections of canal across the road into Province 5. That's a public work I have to pay five to cross. I'm being taxed by infrastructure.")))
lot(5,"DJ",[
 B(6,8), B(7,10),
 B(6,12,None,"Twelve. One Jar in the world. I need it, Graham needs it."),
 B(7,15,"Fifteen.", TH(
   ("Graham","Fifteen. My reservoir paid me twenty this year and I'm spending most of it on the one Jar in existence. That's three of four."),
   ("Paddy","He's got a reservoir and I've got a bad buffalo. Fine."))),
 B(6,None,"Go on.","I'll get one somewhere. There's always somewhere.")],
 hover="Graham puts it on R13, on the west edge, next to his Customs House and as far from the soldier at P17 as he can get it.", at="R13")
lot(6,"WB",[
 B(5,6), B(7,9,None,"Nine. If I take the Bowl as well I'm complete."),
 B(5,11,"Eleven.", TH(
   ("Silke","Eleven out of a flooded year. If Graham gets this, he's done and I'm farming silk forever."),
   ("Graham","She's right. That's exactly what happens if I win it."))),
 B(7,14,"Fourteen.", TH(
   ("Graham","Fourteen. That's four of four. Now I need twenty in hand and a peasant to replace — and Silke's province is the best in the country."),
   ("Silke","He's looking at my seat."))),
 B(5,None,"Out.","Out. The Vase is next and I need that too. If I spend it all here I lose both.")],
 hover="Graham puts it on Q13. Everything he owns is now on the west edge of Province 7 except the Brush, which he bought first and put in the middle.", at="Q13")
lot(7,"VA",[
 B(5,7), B(6,9), B(5,12),
 B(6,14,"Fourteen.", TH(
   ("Paddy","Fourteen and I'm three of four. Missing a Jar, and Graham owns the only one."),
   ("Silke","And there's no point my winning it. I'd need the Bowl to finish, and Graham has the only Bowl."))),
 B(5,None,"Keep it.","Graham holds the Jar Paddy needs and the Bowl I need. Every set at this table runs through Graham now.")],
 hover="Paddy puts it on S25, the corner where the rice fields meet the sea.", at="S25")
march({"W1":"Q16"}, "Robert Land's southern soldier steps onto Q16 and takes Graham's Bamboo Brush as tribute.", TH(
 ("Rob","Two years I've stood next to it. My booklet: raid a square holding realia and I can take the realia. Graham finished his set this very round. Now he hasn't. And that's the first piece toward my own objective — one piece from every player."),
 ("Graham","He took the Brush. The one piece I bought before I'd worked out where he'd be standing. He's got a Brush and no use for it except that I need it."),
 ("Reina","He's going for his objective. One piece from each player, a palace from me. If he finishes, he can take my seat.")),
 take={"W1":("BB","K4")})
say("Graham","How much for it?", TH(
 ("Graham","Not angry yet. Angry later. Price first."),
 ("Rob","He's asked how much. That's the most fun sentence in this game.")))
say("Rob","Ask me again when I've raided everybody once.",
 "I'm not selling it until it's worth more as a sale than as a block. He has to want it more every year. It's on K4, in the desert, where nobody's soldier is ever going to walk.")
march({"W2":"H24"}, "Robert Land's northern soldier steps onto H24 and raids the square holding the Winter Palace. The Emperor pays him the cost of the structure: 20.", TH(
 ("Rob","Palace squares count as the Emperor's realia, and I take the cost. That's two of my four in one year — Graham's Brush, Reina's palace. Silke and Paddy left."),
 ("Reina","Ten, ten and twenty: forty for a palace I only built as a key. I watched him walk to it for three years and paid for every step."),
 ("Graham","He's playing to win, not to spoil.")))
salaries({7:5}, text="Reina pays Graham 5.")

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
say("Graham","Population increases by one half. Good harvest for everyone. A hundred and fifty million people, and everybody's consumption goes up by half, forever.", TH(
 ("Graham","Mine goes forty to sixty, and my reservoir covers twenty of it. That's what a reservoir is for. I'd like everyone to notice that the arithmetic works when somebody builds something."),
 ("Silke","My canal starts paying this year. Twenty. I can feel the difference already and it hasn't arrived.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
taxes(.50, collector="Reina collects the tax herself")
say("Reina","Fifty. It's a good year and two of you have a public work paying into it.", TH(
 ("Reina","Fifty on a good year with bonuses. Graham's income is sixty now, Silke's sixty. The ditches are paying for the next ditch, and I have three more to buy."),
 ("Paddy","Mine's the only province without one. Next, please.")))
build("Grand Canal in Province 6 — 2 sections", 80, {1:80}, canal={6:2})
say("Paddy","Two sections in my province. Thank you, Majesty.", TH(
 ("Paddy","Every peasant province has a public work now. I've never seen this happen."),
 ("Rob","Two more canals to pay tolls on. The whole country's turning into water.")))
march({"W1":"R17", "W2":"I23"}, "Robert Land moves both soldiers: R17 in Province 7, and I23, deeper into Province 1.", TH(
 ("Rob","Five from Graham, ten from the Emperor. The northern one's heading south now. There's a door at the bottom of Province 1 into Province 4, and nobody lives in Province 4."),
 ("Reina","He's not leaving. He's passing through. Province 4's empty, so he can walk across it for nothing, and on the other side of it is Silke.")))
say("Reina","Two soldiers, Robert. Forty.", TH(
 ("Reina","Cause five is 'the Emperor cannot control the Warlord.' I've been raided four times, so mine can move the moment they're on the board."),
 ("Rob","She's buying them with her own money. I keep ten. Every soldier anyone buys makes me richer, and none of them can move until I've raided them. Hers can. That's new.")))
sell_soldiers([(1,"J24"), (1,"G22")], "Reina buys two soldiers from Robert Land and stands them on J24 and G22.", TH(
 ("Reina","J24 is the corner he has to pass to get south, and it's at an angle from him, so he can't capture it. A soldier only takes another straight on, never diagonally."),
 ("Silke","The Emperor has an army. It's two soldiers, but it's an army."),
 ("Rob","Diagonal. She's read the capture rule. Pity.")))
salaries({7:5}, text="Reina pays Graham 5.")

# ============================== YEAR 5 ==============================
R(5, "Shared increase", "share")
say("Graham","Average harvest. And every province with a public work shares the increase with the Emperor, fifty-fifty.", TH(
 ("Graham","That's all three of us. Silke, Paddy and me each pay her ten. The card just gave Reina thirty for building our ditches."),
 ("Reina","Thirty, because every peasant province has a work to share. That's what building things buys.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
act("Each province with a public work pays the Emperor half its increase: 10 each from Silke, Paddy and Graham.", TH(
 ("Silke","Ten of my twenty back to the crown. I'll take it. Two years ago my twenty didn't exist."),
 ("Paddy","First year my canal pays and half of it goes straight back to her. I'm choosing to call that rent.")),
 {pid(5):-10, pid(6):-10, pid(7):-10, pid(1):30}, map_hl=[1,5,6,7])
taxes(.50, collector="Reina collects the tax herself")
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="G18", hover=TH(
 ("Reina","G18, at the far end of the province from where his soldier went. He's in Province 4 by next year and I'd like him to have to turn round."),
 ("","Reina pays the 20.")))
say("Reina","The Summer Palace. Not for me — the booklet won't let me start my own canal or the Wall without it.",
 "Twenty for the key to the last two systems. Every palace I build this game is a padlock on something useful.")
say("Graham","Robert. The Brush.", TH(
 ("Graham","I've got everything else, and he's got his raid on me counted already. The Brush is just furniture to him now."),
 ("Rob","He's right, and he knows he's right, so the price is the only interesting part left.")))
say("Rob","Thirty-five.", TH(
 ("Rob","He's got a hundred and forty-odd and a reservoir. Thirty-five is what it's worth to a man who's about to take the best province in the country."),
 ("Silke","The best province in the country. That's mine. He's pricing my seat.")))
give(8, 7, "BB", at="P15")
act("Graham Garner buys back his Bamboo Brush from Robert Land for 35, and puts it on P15.", TH(
 ("Graham","Thirty-five for a Brush I bought for six. Rob made thirty-five on a piece of wood by standing next to it for two years and then on it."),
 ("Rob","I'd like that sentence carved on something.")), {pid(7):-35, pid(8):35}, map_hl=[7,8], deal=True)
swap(7,5,"Graham Garner declares a complete set and replaces Silke Weber. Graham becomes Silk Peasant of Province 5; Silke becomes Wheat Peasant of Province 7.", TH(
 ("Graham","Hand back the Jar — it's native to Province 5 — keep the rest, and take every bag Silke's holding. Wheat to silk in five years. My Customs House, Brush and Bowl go on O26, P25 and P26, at the sea end where Silke kept hers. And the province I'm leaving has the reservoir Reina built for me, which is now Silke's reservoir."),
 ("Silke","He's taken my seat, my grain and my canal, and given me his reservoir. It's the best thing in Province 7 and it's the only reason I'm not furious."),
 ("Reina","Graham climbed, and the province he left behind is better off than the one he took. I'll take that.")),
 at={"CH":"O26", "BB":"P25", "WB":"P26"})
say("Silke","I'm keeping your reservoir, Graham.", TH(
 ("Silke","Twenty a year, forever, and I didn't pay for it. That's the one good piece of furniture in this whole swap."),
 ("Graham","She's right. I built my own replacement's income. I'd do it again.")))
march({"W1":"R16", "W2":"J22"}, "Robert Land moves: R16 in Province 7, and J22, into empty Province 4.", TH(
 ("Rob","Five from Silke, who owns nothing yet for me to take. And the northern one's out of Province 1. Province 4 has nobody in it, so nobody to raid — and nobody to pay a toll to when I cross the river."),
 ("Silke","My first raid as a wheat farmer, and it's on the square next to my own reservoir.")))
troops({"Reina1":"K24", "Reina2":"H22"}, "Reina's soldiers follow him south: one to K24 in Province 4, on the road to Province 5; one to H22.", TH(
 ("Reina","K24 sits between him and the top of Province 5, and it isn't straight beside him, so he can't take it. He moves first every year. I must never end a turn level with him, only at an angle or further off."),
 ("Rob","She's learned the dance. Whoever moves first takes. I always move first.")))
salaries({7:5}, text="Reina pays the I Ching reader 5 — now Silke, who took over Graham's job with his province.", hover="Reina hands the reader's job to whoever holds Province 7, and that's Silke now.")

# ============================== YEAR 6 ==============================
R(6, "A bad harvest", "dribble1")
say("Silke","The seed rotted, the rains came late, and the ox went lame. Bad harvest.", TH(
 ("Silke","First card I read in my new job and it's this one. Bad for everyone. My reservoir covers it. Graham's canal covers him. Reina's the one who'll feel it."),
 ("Reina","Minus forty for the crown. Three works still to buy and one bad year. Fine. I've planned for a bad year.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
taxes(.50, collector="Reina collects the tax herself")
say("Reina","No system this year. The booklet says when I'm not building a system I build the Pagoda. Twenty.", TH(
 ("Reina","The cheapest thing on my list, in the worst year so far. My canal and the Wall wait for a harvest that can pay for them."),
 ("Graham","The Pagoda is the thing she builds when she's got nothing else she can afford. That's the right order.")))
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="G19", hover=TH(
 ("Reina","G19, next to the Summer Palace, at the top of the province. Everything precious I own is now as far from Province 4 as I can put it."),
 ("","Reina pays the 20.")))
lot(5,"DJ",[
 B(6,10,"Ten.", TH(
   ("Paddy","Ten. The Jar's back on the table and I've had the other three since year three."),
   ("Graham","I'm the seller. I get a quarter of whatever Paddy pays for it. I'd like him to pay a lot."))),
 B(7,11,None,"Eleven. I need a Jar too now. I need everything now."),
 B(6,16,"Sixteen.", TH(
   ("Paddy","Sixteen and that's four of four. Twenty in hand, a province to take — and the province with the canal and the good land is Graham's now."),
   ("Graham","He's looking at me the way I looked at Silke."))),
 B(7,None,"Have it.","Sixty-odd in grain and nothing else. He's got nearly twice that, and he only needs this one piece.")],
 hover="Paddy puts it on S22, with the rest of his pieces along the south edge.", at="S22")
lot(6,"BB",[
 B(7,4,"Four.", TH(
   ("Silke","Four for a Brush. Start again, in a new province, from nothing. It goes on O16, three squares from his soldier. In Province 7 there's no such thing as far."),
   ("Rob","She's put a piece of realia on a square. I've noticed.")))], at="O16")
act("Silke puts the returned Land Deed Scroll up for auction. Nobody bids.", TH(
 ("Silke","Paddy has one, and Province 7 doesn't need one. Graham does, but Paddy's just bought the Jar that takes Graham's seat, so anything Graham buys tonight goes straight back in the box. It sits there."),
 ("Paddy","The one piece at this table that nobody wants.")), map_hl=[7])
swap(6,5,"Paddy Doyle declares a complete set and replaces Graham Garner. Paddy becomes Silk Peasant of Province 5; Graham becomes Rice Peasant of Province 6.", TH(
 ("Paddy","Hand back the Jar, keep the rest, and take every bag Graham's holding — which is everything Silke had, plus everything he had. I'm not overly ambitious, it says so on my card. I'm also not stupid."),
 ("Graham","I took Silke's seat and her grain a year ago. He's just done the same thing to me, with my grain and hers. I can't even be angry. I wrote this move."),
 ("Silke","The richest man at this table started the evening growing rice.")),
 at={"CH":"L25", "LD":"M25", "VA":"N25"})
say("Graham","Fair.", TH(
 ("Graham","One word. It's the only honest one available."),
 ("Rob","Two of them have robbed each other blind without me lifting a finger. I love the peasant game.")))
say("Paddy","L25, M25, N25. The top corner of Province 5. Seven squares from the gap.", TH(
 ("Paddy","The deepest squares in the country. The notch is the only way in from the desert, and it's at the other end."),
 ("Reina","Seven squares from the gap. Three from his soldier in Province 4. Paddy, nobody comes in by the gap any more. He came in the back door."),
 ("Paddy","...oh.")))
march({"W1":"Q17", "W2":"K22"}, "Robert Land moves: Q17 in Province 7, and K22, across Province 4 towards the corner.", TH(
 ("Rob","Five from Silke. And the other one's three squares from Paddy's corner, and two squares from Reina's soldier on K24: too far for either of us to take the other."),
 ("Silke","He's walking towards my Brush. One square a year, and I can't move it. Realia stays where it's put."),
 ("Reina","Two squares from mine. Too far for him to take it, too far for me to take him. He can count squares as well as I can.")))
say("Reina","Paddy. Buy a soldier, and stand it on your realia.", TH(
 ("Reina","Rob can only take a piece by stepping onto its square. If Paddy's soldier stands on it, he has to come at it straight on and capture first, and my two will be beside it."),
 ("Paddy","I've got a Customs House, a Scroll and a Vase, and a man in Province 4 who wants one of them.")))
sell_soldiers([(5,"L25")], "Paddy buys a soldier from Robert Land and stands it on his Customs House at L25.", TH(
 ("Paddy","Twenty to the man who's coming for me. It can't move until he's raided Province 5, and it doesn't need to. It just has to stand on the nearest piece."),
 ("Rob","Everyone's buying soldiers. I'm going to be rich and outnumbered.")))
troops({"Reina2":"I22"}, "Reina's soldier on K24 holds its square; the other comes south to I22.", TH(
 ("Reina","K24 stays. From there it can step straight down onto L24, the one empty square he'd have to cross to get into the corner. I'm not guarding his square. I'm guarding the one he needs."),
 ("Rob","She's guarding the square I'd walk onto. Not the square I'm on. She really has read it.")))
salaries({7:5}, text="Reina pays Silke 5 for reading the cards.")

# ============================== YEAR 7 ==============================
R(7, "Repairs", "repairs")
say("Silke","Good harvest for all. Provinces 4, 5, 6 and 7 pay two each for repairs to their public works. And 1, 2, 3 and 8 play a personal disaster.", TH(
 ("Silke","Empty provinces skipped, that's two each from Paddy, Graham and me, and a disaster each for Reina and Rob."),
 ("Rob","Three disasters in my booklet and two of them stop me raiding. I keep drawing both.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
act("Repairs: Provinces 5, 6 and 7 each pay 2 to the Harvest Pile.", "Storms and raiders, according to the card.",
    {pid(5):-2, pid(6):-2, pid(7):-2}, map_hl=[5,6,7], pile_delta=6)
disaster(1,"the Arabian horse throws her. The trainer is lashed twenty times.", TH(
 ("Reina","Four. The horse throws me and the trainer pays. It's a very consistent booklet."),
 ("Graham","Twenty lashes for the trainer. He's having a worse evening than any of us.")))
disaster(8,"a lieutenant runs off with his daughter. No raids this year — too busy feasting the newlyweds.", TH(
 ("Rob","Year seven, two of four, three squares from Paddy's corner and two from Silke's Brush, and I'm at a wedding."),
 ("Reina","A year's grace. I'm spending it on my canal.")))
taxes(.50, collector="Reina collects the tax herself")
say("Reina","My canal. Two sections, eighty.", TH(
 ("Reina","Every peasant province has had its public work for years. I've earned my own ditch."),
 ("Paddy","Nobody's going to say anything. That's what three ditches first buys you.")))
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
lot(5,"DJ",[
 B(6,6,"Six.", TH(
   ("Graham","Six for a Jar. Province 6 needs a Customs House, a Scroll, a Vase and a Jar, and I've got eighty-odd and nothing on the board. Start somewhere."),
   ("Paddy","I'm selling him back the Jar I took his seat with. Six is fine.")))],
 hover="Graham puts it on S20, at the west end of the rice fields, as far as Province 6 gets from Paddy's corner and Reina's soldiers.", at="S20")
act("Graham puts up the Brush he had to hand back, and Silke the Scroll. Nobody bids.", TH(
 ("Silke","Why would I buy a Brush? I've got one already, and he's two squares from it."),
 ("Graham","I need the Scroll. I'd also need Paddy's Vase, the only one in the world, and he's standing a soldier next to it. A Scroll gets me nowhere.")), map_hl=[6,7])
march({"W1":"P17", "W2":"L23"}, "Robert Land walks his soldiers to the wedding the long way: back onto his old raid square at P17, and on to L23 in Province 4. Neither raids.", TH(
 ("Rob","No raids, but nobody said no walking. P17 is next to Silke's Brush. L23 is one step from Paddy's corner. The wedding's very well placed."),
 ("Silke","He's raided P17 already, so he can stand on it all he likes. One square from my Brush. Again."),
 ("Paddy","One square from my corner, and the only empty square between us is the one Reina's watching.")))
say("Silke","A soldier costs twenty. The Brush cost four. He can have it.", TH(
 ("Silke","I could buy one and stand it on O16. Twenty to guard four. Graham did that sum in year two and lost his set. My sum's different: I've got one piece and three to go."),
 ("Rob","She's done the arithmetic out loud. I like a table that shows its working.")))
say("Reina","Your soldier, Paddy, and mine. That's the corner.", TH(
 ("Reina","Two soldiers between him and three squares of realia. He moves first, so he'll always see the trap. The point is that every way in is a trap."),
 ("Rob","She's built a wall of soldiers around a man growing silk. Not the wall I expected.")))
salaries({7:5}, text="Reina pays Silke 5.")

# ============================== YEAR 8 ==============================
R(8, "Steady weather", "winds")
say("Silke","Steady weather. Neither feast nor famine: an average harvest for this year.", TH(
 ("Silke","An average harvest at a hundred and fifty per cent, with a public work in every province. Everyone's positive. Without the ditches this card would have been a funeral."),
 ("Reina","Two projects left. Four Wall links. If nothing goes wrong, I finish next year.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
taxes(.50, collector="Reina collects the tax herself")
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
act("Paddy puts up the Customs House that came back to him, Graham the Bowl, and Silke the Scroll. Nobody bids.", TH(
 ("Silke","The Customs House and the Bowl, two of the pieces I need, on the table at once. And the game ends next year. I can't finish a set of four in two rounds, and anything I put down, he walks to."),
 ("Graham","A Customs House I need, for a set that needs Paddy's Vase. No."),
 ("Paddy","Three lots, no bids. The table's stopped collecting. It's building now.")), map_hl=[5,6,7])
say("Reina","Two links. Two more next year and every public work this country owes is standing.", TH(
 ("Reina","The Wall is last, and it's only four links, because only my province is under it."),
 ("Graham","Four links instead of twelve, because nobody's sitting in 2 or 3. The Wall was always the most expensive thing on the list and the least useful. Building it last is the whole trick.")))
march({"W1":"O16"}, "Robert Land's southern soldier steps onto O16 and takes Silke's Bamboo Brush as tribute.", TH(
 ("Rob","Three of four. Graham, Reina, Silke. Three squares in three years, and one of them at a wedding. One piece from Paddy and I can take any seat at this table — and there's only one seat I want."),
 ("Silke","I owned it for two years and watched him walk to it."),
 ("Reina","Three of four, and it's the last year he'll get. Paddy's corner is all that's left.")),
 take={"W1":("BB","K5")})
march({"W2":"L24"}, "Robert Land's northern soldier steps into Province 5 at L24 and raids it, one square from Paddy's Customs House.", TH(
 ("Rob","Next year it's over, so it's now or never. L24 is the only way in. Paddy's soldier is on the Customs House, Reina's is beside the square, and I'm stepping onto it anyway. Five for the raid, five back to Paddy for crossing the river, and maybe she blinks."),
 ("Paddy","He's raided Province 5. My soldier can move now. It doesn't need to."),
 ("Reina","He knows. He's doing it anyway.")))
troops({"Reina1":"L24"}, "Reina's soldier steps down from K24 onto L24 and captures one of Robert Land's soldiers on the edge of Province 5.", TH(
 ("Reina","Captured, straight on, the way the General Instructions allow. I took a soldier off him with one I bought from him."),
 ("Rob","She bought it from me. I sold her the soldier that just captured my soldier. I'd like that noted as the funniest thing that has ever happened to me."),
 ("Graham","Cause five, 'the Emperor cannot control the Warlord.' Struck off, live, in front of everybody.")))
salaries({7:5}, text="Reina pays Silke 5.")

# ============================== YEAR 9 ==============================
R(9, "The last of the Wall", "chest")
say("Silke","Average harvest. And moved by the suffering of her people, the Emperor opens her purse: two million to every player from the Emperor's reserve.", TH(
 ("Silke","The card says 'his'. I changed it to 'her' reading it. Nobody stopped me."),
 ("Reina","Eight million out of the reserve in the year I need every bag for the Wall. I'll pay it. It's printed.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
act("Imperial charity: 2 million from the Emperor's reserve to every other player.", TH(
 ("Reina","Eight, and I don't need it to buy anything."),
 ("Paddy","Two million. I'm the richest person at the table and the Emperor just gave me two million. I'm going to hold it up to the light.")),
 {pid(s):2 for s in ACTIVE if s != 1} | {pid(1):-8}, map_hl=[1])
taxes(.50, collector="Reina collects the tax herself")
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
assert all_built(), "not every public work is built"
act("Every public work the country owes is standing. The game ends: the players have survived, and the Emperor's reign has been a glorious one.", TH(
 ("Reina","Nine years. A reservoir in year two, two canals before my own, the Pagoda in the bad year and the Wall last. The order was the whole game. Two and a half million left in the treasury — 'too low a grain reserve' by anyone's reading, and it doesn't matter, because there's nothing left to build."),
 ("Graham","Three doubling cards still in the deck. We stopped before they came. That's the other half of the trick, and nobody planned it."),
 ("Rob","Three of four. One raid short, and the raid I needed was standing in the far corner of Province 5 behind two soldiers.")), map_hl=list(ACTIVE), big=True)
say("Silke","For the record, I'd like it noted that I lost.", TH(
 ("Silke","Silk to wheat. I fell two provinces. I've got Graham's reservoir and Rob's raid squares, and the satisfaction of having read every card since year six."),
 ("Graham","She's not wrong. Survival's a team result. The seats aren't.")))
say("Reina","Same time next week?",
 "Next time I'd like to be a peasant.")

RESULT = export(
 "Every public work was built, so this is the first ending: the players survived and the Emperor's reign was a glorious one. Players are still ranked by the province they finished in against the one they drew.",
 ["Reina kept the throne and finished the list — which by Section 18 is a win for the Emperor. The order did it: productive works first, palaces only when they unlocked something, and the Wall last.",
  "The peasants spent the evening taking each other's seats. Graham climbed from wheat to silk, Paddy climbed over Graham, and Silke fell from silk to wheat — but every one of them finished with a public work paying into their province.",
  "Robert Land came within one raid of the throne. One soldier walked three years to the Winter Palace and on through empty Province 4 to the back door of Province 5, where the Emperor captured it with a soldier she had bought from him. The last piece he needed sat in the deepest corner of the country."])
