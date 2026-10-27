# Game 5 — Land, Robbed. The Warlord completes his objective and takes the throne.
setup([1,2,3,5,7,8], "robbed", "Land, Robbed",
      "Six players · ten years · the Warlord takes the throne",
      "Noah and Paddy sit out. Reina Osorio draws the throne, and Robert Land draws the Warlord — announcing every move a year before he makes it, and it works. Eight pieces of realia for four collectors, and two soldiers.",
      short="6 players · 10 years")

# ============================== SETUP ==============================
R(0, "The booklets fall differently", None, "Six players: the Emperor, the Official, the Gentry, two peasants and the Warlord (rulebook Section 4 and Appendix A). No Scholar, so the Emperor appoints someone to read I Ching. Each realia province holds two of its own pieces, and each collector needs one from each of the other three.")
act("Noah and Paddy sit this one out. The six remaining booklets are shuffled and drawn: Reina Osorio draws the Emperor, Clark the Official, Rich the Gentry, Silke the Silk Peasant, Graham the Wheat Peasant, and Robert Land the Warlord.", TH(
 ("Reina","The throne. I know exactly how this chair gets taken."),
 ("Rob","The Warlord. I'm going to tell you every move, and you're going to use it to put soldiers exactly where I'll be."),
 ("Silke","Silk Peasant. The fields, just a better class of field.")), map_hl=[1,2,3,5,7,8])
say("Rob","I'll tell you where my soldiers are going, every year, before they go.", TH(
 ("Rob","It may cost me, and I'm doing it anyway. Every soldier moves one square a year and the board is face up. The trick isn't hiding where I'm going. It's going somewhere a soldier can't follow."),
 ("Rich","He's announcing his raids. Either he's learned nothing or he's learned something.")))
act("Rich sets out the Harvest Pile: twenty-five hundred million in bags of every size, where everyone can see it.", TH(
 ("Rich","I bank the pile and I collect the rent. Tonight I'm the rules."),
 ("Graham","The landlord's counting the bank. Same as ever.")), map_hl=[3])
deal_grain("Rich deals 60 to each of the six players. That's the first year's harvest.", TH(
 ("Rich","Three hundred and sixty out of the pile before anyone's done anything."),
 ("Clark","Sixty. And I've got the tax to collect on top of it, which is a sentence I didn't expect to enjoy.")))
act("Reina Osorio appoints Silke Weber to read the I Ching and keep the population count, at the Scholar's salary of 5. Silke shuffles the twenty cards and lays them face down.", TH(
 ("Silke","Five a year to read the omens to the Emperor. I'll read very clearly.")), map_hl=[1,5])
take_stock("Clark, Rich, Silke and Graham each take two pieces of their own realia out of the box. Eight pieces in all, and they wait beside the board until they're sold.", TH(
 ("Clark","Two Customs Houses. Every collector needs one piece from each of the other three provinces, and there are only two of each. Three people want every piece."),
 ("Graham","Eight pieces, twelve wants. Four of us are going to be one short whatever happens. That's the game."),
 ("Rob","And every piece that goes on a square is one I can stand on.")))
act("Clark cuts out the Province 2 Irrigation System (one square by two), Rich the Province 3 Reservoir (two by three), and Graham the Province 7 Reservoir (two by two). Nobody sits in Provinces 4 or 6, so nothing is owed there.", TH(
 ("Rich","Two by three. The biggest cut-out in the box, and every square of it charges a soldier five to step on."),
 ("Graham","Two by two. Now I have to ask for it."),
 ("Reina","Three cut-outs and three palaces. I've got a long list and nobody to split the palaces with.")), map_hl=[2,3,7])
place_army({"W1":"N18", "W2":"E22"}, "Rob stands his two soldiers on undeveloped land: W1 on N18, the notch beside Provinces 4, 5 and 7; W2 on E22, in the strip under the Wall, at the eastern end above the Emperor's province.", TH(
 ("Rob","N18 is one step from Silke's province and one from Graham's. E22 is above Reina. I'll say it plainly: the one in the north walks the Emperor's province, ten a square and twenty for any palace on the way, and then goes on to whatever Clark puts in Province 2. The Emperor isn't on my list, but her reserve is. The one in the south is going to whoever's nearest. I've got two, and they each have a job."),
 ("Reina","He's put one where every square of my province is within five of it.")))

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
rents()
say("Reina","Thirty-five per cent. Collect it, Clark.", TH(
 ("Reina","I'd rather have the grain."),
 ("Clark","Thirty-five, year one. She's not even pretending.")))
taxes(.35)
act("Robert Land declines to pay tax.", TH(
 ("Rob","My booklet's silent on tax.")), map_hl=[8])
say("Reina","The Summer Palace. I'll put it at G17.", TH(
 ("Reina","Twenty for the key to the Wall. G17 is the corner by Province 2, five squares from his soldier in the strip. Every square I own is within five of one of his two."),
 ("Rob","Five squares. Four of them in Province 1, at ten each. I'll be there in year five, and she'll have paid me forty to watch me arrive."),
 ("Graham","She's building the thing the Warlord needs, and telling him where it is. It's the only way to build it.")))
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="G17")
say("Reina","No soldiers, Rob. I'm not buying any.", TH(
 ("Reina","A soldier only catches a Warlord who walks up beside it. He's not going to walk up beside anything of mine. Twenty a soldier, five of it to him, to guard one square of thirty-four. I'll pay the tribute instead."),
 ("Rob","She's not buying from me. She knows exactly why that's right, and so do I.")))
lot(2,"CH",[
 B(3,5), B(7,6),
 B(5,8,"Eight.", TH(
   ("Silke","Eight, and it's going next to the notch, on O19, one step from his soldier."),
   ("Graham","She's putting it where he can take it. On purpose.")))],
 hover=TH(("Silke","He's going to get one piece from each of us; that's his whole objective. I'd rather choose which and when. A Customs House now, one step from his soldier, and then he leaves me alone."),
          ("Graham","A ransom. She's paying the Warlord in advance. ...that's actually sensible.")), at="O19")
lot(3,"LD",[
 B(2,5), B(5,6),
 B(7,7,"Seven.","Seven. I need a Scroll, and Silke's just spent her eight on a ransom.")],
 hover="Graham puts it on S13, the far corner of Province 7, five squares from the soldier in the notch.", at="S13")
lot(5,"DJ",[
 B(2,6), B(3,7),
 B(7,8,"Eight.", TH(
   ("Graham","Eight, and it goes on O17, next to the notch. Silke's right. One piece each, and I'll pick mine."),
   ("Rich","Two ransoms in one round. The peasants have unionised against a single soldier.")))],
 hover=TH(("Graham","O17 is one step from N18. He takes the Jar, I buy it back, and the Scroll in the corner is never worth his walk."),
          ("Rob","The peasants are paying me to go away. I'll take it. I'll even go away.")), at="O17")
lot(7,"VA",[
 B(3,6),
 B(2,8,"Eight.", TH(
   ("Clark","Eight. G13, near the top of my province. Nine squares from the soldier in the strip and seven from the other. The furthest square I own from either of them."),
   ("Rob","Nine squares. He's measured it.")))],
 hover="Clark puts it on G13.", at="G13")
march({"W1":"O19", "W2":"F21"}, "Rob's soldiers move as announced: W1 steps onto O19 and takes Silke's Customs House; W2 steps into Province 1 at F21.", TH(
 ("Rob","Silke's ransom, collected the round it was offered, and ten from the Emperor. One piece from each of you, and that's one."),
 ("Silke","He paid a toll to my province crossing the river to get it. I've been paid five to be robbed."),
 ("Reina","Ten. The first of four.")),
 take={"W1":("CH","N12")})
say("Rob","The Customs House goes to whoever pays most. I'm saying that now, so nobody thinks I lied later.", TH(
 ("Rob","Silke may want it back. Graham needs one too. So does Rich. It's the most useful thing I own."),
 ("Silke","He's auctioning my ransom. I should have read the small print, except he said it out loud.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 for collecting the tax and Silke 5 for reading the cards.")

# ============================== YEAR 2 ==============================
R(2, "Fortune and misfortune", "goodevil")
say("Silke","Good harvest for all. Provinces 2, 4, 6 and 8 play a personal disaster. Nobody's in 4 or 6, so that's Clark and Rob.", TH(
 ("Silke","Reading it for the Emperor. Five a year to bring bad news."),
 ("Clark","Of course it's me.")))
harvest("Rich pays out the harvest from the Harvest Pile.")
rents()
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Clark","Four million for a driver."),
 ("Rich","It hits whoever sits in that chair.")))
disaster(8,"wounded in the legs in his last battle. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Rob","So W1 walks back into the notch and waits for Graham's Jar to be worth the step. W2 keeps going."),
 ("Graham","A year's grace for the Jar I put out as a ransom. I'll take it, I suppose.")))
taxes(.35)
say("Clark","Majesty. The irrigation. Fifteen from me, fifteen from you, ten a year forever.", TH(
 ("Clark","Half each, and it pays back in three years."),
 ("Reina","Half of thirty for a permanent rise in his tax. I'd be a fool to refuse.")))
build("Province 2 Irrigation System", 30, {1:15,2:15}, key="irr2", at="I15:I16", hover=TH(
 ("Clark","I15 and I16, in the east of my province, by the river. Any soldier that steps on it pays me five."),
 ("","Cost split: Reina 15, Clark 15.")))
lot(2,"CH",[
 B(7,9),
 B(3,10,"Ten.", TH(
   ("Rich","Ten. Customs Houses are the one thing in this game that are scarce and also mine to want."),
   ("Graham","There's one more, and Rob's holding it. Fine.")))],
 hover="Rich puts it on K10, deep in the west of Province 3, as far from both soldiers as his province goes.", at="K10")
lot(3,"LD",[
 B(2,7),
 B(5,9,"Nine.", TH(
   ("Silke","Nine. P26, the far end of Province 5 by the sea. I've paid my ransom. I don't intend to pay it twice."),
   ("Clark","That was the last Scroll in the stock. I've got a Vase, I'm about to buy a Jar, and I'll be one Scroll short.")))],
 at="P26")
lot(5,"DJ",[
 B(3,8),
 B(2,10,"Ten.", TH(
   ("Clark","Ten, and it's going on J12. My Vase at the top of my province and my Jar at the bottom, as far apart as I can get them."),
   ("Rich","That's the Jar I needed. There were two, and one's a ransom.")))],
 hover="Clark puts it on J12, far from both soldiers.", at="J12")
lot(7,"VA",[
 B(2,None,"I have one.","I've got a Vase. Let the others fight over this one."),
 B(5,7),
 B(3,9,"Nine.", TH(
   ("Rich","Nine. K9, next to my Customs House, at the western edge. Two of three, and the one I'm missing is the Jar."),
   ("Silke","That was the last Vase. I'm missing it, and the Customs House he took."))),
 B(5,None,"Out.","Out. Nine's more than I've got to spare after the Scroll.")],
 at="K9")
sell_soldiers([(2,"J12")], "Clark buys a soldier from Rob and stands it on his Dragon Jar at J12.", TH(
 ("Clark","A soldier on the Jar. Twenty. Nobody can raid a square with my soldier on it unless he takes it straight on, and if he comes straight at it, mine takes his."),
 ("Rob","His soldier can't move until I've raided Province 2. I haven't. I'm noting that, out loud, as promised."),
 ("Reina","He's noting it. I'd be more worried by that than he is.")))
march({"W1":"O18", "W2":"F20"}, "Rob moves: W1 back to O18 in the notch; W2 to F20, raiding Province 1 again.", TH(
 ("Rob","Ten from the Emperor. Three squares to the palace."),
 ("Reina","Twenty paid, forty to come. The palace cost me twenty to build.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 3 ==============================
R(3, "Rain and flood", "rainflood")
say("Silke","Good harvest for Provinces 1, 3, 6 and 7. Rivers flood in 2, 4, 5 and 8.", TH(
 ("Silke","Bad for me, bad for Clark, bad for Rob. I read a flood over my own province without blinking."),
 ("Graham","Good for me. I'm going to need it.")))
harvest("Rich pays out the harvest from the Harvest Pile.")
rents()
taxes(.40)
say("Graham","Majesty. The reservoir.", TH(
 ("Graham","The crown pays all of it, sixty million. I'm asking in year three, while it's cheap."),
 ("Reina","Sixty. This year.")))
build("Province 7 Reservoir", 60, {1:60}, key="res7", at="Q15:R16", hover=TH(
 ("Graham","Q15 to R16, the middle of Province 7, between the notch and my Scroll. Anything coming for the Scroll pays me five to cross it."),
 ("Reina","Sixty from the crown, in year three.")))
march({"W1":"O17", "W2":"F19"}, "Rob's southern soldier steps onto O17 and takes Graham's Dragon Jar; the northern one raids Province 1 at F19.", TH(
 ("Rob","Graham's ransom. Two of four: Silke and Graham. The peasants are done paying me. And ten from Reina; two squares to the palace."),
 ("Graham","Exactly as planned. Now I buy it back."),
 ("Reina","Thirty paid. I can see the palace from his square.")),
 take={"W1":("DJ","N13")})
say("Graham","How much for the Jar? And how much for the Customs House?", TH(
 ("Graham","The Jar's mine. The Customs House is Silke's, and it's the piece I'm missing. With both I'm complete."),
 ("Silke","He's going to buy my ransom. With his ransom. And then take somebody's chair."),
 ("Rob","He's asked both questions at once. I'll answer them next year, when he's had a good harvest.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
say("Silke","Population increases by half. Good harvest for everyone. Consumption up by half, forever.", TH(
 ("Silke","A hundred and fifty million."),
 ("Reina","I'm not going to be here in seven years. One way or another.")))
harvest("Rich pays out the harvest from the Harvest Pile.")
rents()
taxes(.50)
say("Reina","The Winter Palace. G26.", TH(
 ("Reina","The canal in Province 5 needs it, and Silke wants her canal. G26, the far corner, by the sea. Every palace he stands on is twenty out of the reserve, and he's two squares from the first. This one I've put as far from him as my province goes."),
 ("Rob","Eight squares the wrong way for twenty. She's right, I won't. The first one's on my road.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="G26")
give(8, 7, "DJ", at="O16")
act("Graham buys back his Dragon Jar from Rob for 15, and puts it on O16.", TH(
 ("Graham","Fifteen for the Jar I paid eight for. Ransom has a price."),
 ("Rob","And it isn't counted against me. He paid; I raided. The raid's on the books.")), {pid(7):-15, pid(8):15}, map_hl=[7,8], deal=True)
act("Rob sells Silke's Customs House to the highest bidder. Silke offers 20; Graham offers 30.", TH(
 ("Silke","Twenty is everything I can spare. He'll go higher."),
 ("Graham","Thirty. It completes me. I'm sorry, Silke. No — I'm not, quite."),
 ("Rob","As announced in year one. Highest bidder.")), map_hl=[5,7,8])
give(8, 7, "CH", at="O15")
act("Graham buys Silke's old Customs House from Rob for 30, and puts it on O15.", TH(
 ("Graham","Scroll, Jar, Customs House. Three of three, and more than twenty in hand."),
 ("Rich","He's looking at me."),
 ("Clark","He's looking at both of us. Either chair will do.")), {pid(7):-30, pid(8):30}, map_hl=[7,8], deal=True)
swap(7,3,"Graham Garner declares a complete set and replaces Richard Baron. Graham becomes Gentry of Province 3; Rich becomes Wheat Peasant of Province 7.", TH(
 ("Graham","Hand back the Scroll — it's native to Province 3 — keep the Jar and the Customs House, and take every bag Rich is holding. They go on K11 and L10, next to where his were, at the far west of the province. Wheat to landlord. I bank the pile now."),
 ("Rich","Robbed by the rules: somebody climbing over me with every bag I own in their pocket."),
 ("Rob","And Rich is now in the province my soldier lives in, with nothing on the board. He'll have to buy something. And put it somewhere.")),
 at={"DJ":"K11", "CH":"L10"})
say("Rich","Province 7. With the reservoir. Well.", TH(
 ("Rich","Sixty from the pile and a booklet that says I'm hard-working. The reservoir's the only thing in this province that isn't a raid square."),
 ("Graham","Reina built it for me, and now it's his. Somebody's always building Province 7 a reservoir for somebody else.")))
act("The pieces handed back in the seat change go up for auction this round: Clark sells the Customs House, Graham the Scroll, and Rich the Vase.", TH(
 ("Graham","My Scroll goes back to Province 3, and Province 3 is me now. I auction my own piece the same evening I handed it in."),
 ("Clark","Three pieces back on the table, and one of them is the Scroll I'm missing.")), map_hl=[2,3,7])
lot(2,"CH",[
 B(5,6),
 B(7,8,"Eight.","Eight. I need everything in Province 7 now, and the Customs House is first."),
 B(5,9,"Nine.", TH(
   ("Silke","Nine. My Customs House back, in a manner of speaking. Now I'm missing a Vase."),
   ("Rich","She's outbid me for a Customs House I used to own. Tonight everything I bid on used to be mine."))),
 B(7,None,"Have it.","Out. I've got sixty from the pile and a whole set to buy.")],
 hover="Silke puts it on P25, next to her Scroll by the sea.", at="P25")
lot(3,"LD",[
 B(7,6),
 B(2,10,"Ten.", TH(
   ("Clark","Ten. It's the piece I'm missing. Vase, Jar, Scroll — I'm complete, and I'm the Official."),
   ("Reina","He's the Official. If he completes, he can take my seat."))),
 B(8,12,"Twelve.", TH(
   ("Rob","Twelve. I have no use for a Scroll. I have a great deal of use for the Official not having one."))),
 B(2,15,"Fifteen."),
 B(8,20,"Twenty.", TH(
   ("Rob","Twenty. I'll go higher. He knows I'll go higher."),
   ("Clark","He's got more grain than me and nothing to spend it on but this."))),
 B(2,None,"Out.","Out. One Scroll in the world, and the man who's robbing the Emperor owns it.")],
 hover="Rob puts it on N14, in his own territory, in plain sight.", at="N14")
lot(7,"VA",[
 B(5,8,"Eight.","Customs House, Scroll, and this. One lot and I'm complete."),
 B(8,12,"Twelve.", TH(
   ("Rob","Twelve. If Silke gets it she's complete, and the chair she'd take is Clark's. Then Clark has nothing on the board, and I can't take a piece from a player who owns none."),
   ("Silke","He's bidding against me to protect his own target. That's the most honest act of sabotage I've ever seen."))),
 B(5,16,"Sixteen."),
 B(8,25,"Twenty-five.", TH(
   ("Rob","Twenty-five. Two pieces this round I have no use for, to stop two people climbing past the one I'm robbing."))),
 B(5,None,"Out.","Out. Eighty-odd in grain, and the Warlord has nearly twice that and nothing else to spend it on.")],
 hover="Rob puts it on N15, beside the Scroll, in plain sight.", at="N15")
march({"W1":"P16", "W2":"F18"}, "Rob moves: W1 into Province 7 at P16, raiding Rich's new province; W2 to F18, raiding Province 1.", TH(
 ("Rob","Five from Rich, ten from Reina. W2 is one square from the palace."),
 ("Rich","My first act as a wheat farmer is to pay a Warlord.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 5 ==============================
R(5, "Heaven has favourites", "heaven")
say("Silke","Good harvest for 2, 4 and 5. Bad for 1, 3, 6, 7 and 8.", TH(
 ("Silke","Good for me and Clark. Bad for the Emperor, the new Gentry, the new wheat farmer and the Warlord."),
 ("Graham","My first year as landlord and heaven doesn't like me. Fair.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents(hover="Graham collects rent from Silke and Rich. Rich used to collect it from him.")
taxes(.50)
build("Grand Canal in Province 5 — 2 sections", 80, {1:80}, canal={5:2})
say("Silke","Two sections in my province. Thank you, Majesty.", TH(
 ("Silke","Twenty a year from next year. It's nice to be on the receiving end."),
 ("Reina","Eighty on someone else's ditch. Silke, you'll notice I'm doing it in the right order.")))
march({"W2":"G17"}, "Rob's northern soldier steps onto G17 and raids the square holding the Summer Palace. The Emperor pays him the cost of the structure: 20.", TH(
 ("Rob","Year five, as announced. Twenty for the palace, and it doesn't count: the Emperor's not on my list. Still two of four, Silke and Graham. Clark and Rich left."),
 ("Reina","Ten, ten, ten, ten and twenty. Sixty for the privilege of being right about the date, and the palace is still standing."),
 ("Clark","He was never walking at her. He's in the corner next to my province.")))
say("Rob","Rich. I'll sell you the Scroll. Eight.", TH(
 ("Rob","He needs it — Customs House, Scroll, Jar for Province 7. I'm selling it to him at a loss, and he'll put it in Province 7, where my soldier is. Both of us know that."),
 ("Rich","He's offering me a bargain and telling me it's bait. I want to refuse on principle and I can't afford principle.")))
give(8, 3, "LD", at="S13")
act("Rich buys the Land Deed Scroll from Rob for 8, and puts it on S13, the far corner of Province 7.", TH(
 ("Rich","S13. The corner Graham used. Three squares from his soldier, with the reservoir in the way."),
 ("Rob","Three squares. Thank you, Rich.")), {pid(7):-8, pid(8):8}, map_hl=[7,8], deal=True)
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 6 ==============================
R(6, "Shared increase", "share")
say("Silke","Average harvest. And every province with a public work shares the increase with the Emperor, fifty-fifty.", TH(
 ("Silke","That's Clark's irrigation, Rich's reservoir and my canal. Five, ten and ten to the crown."),
 ("Reina","Three ditches I paid for, paying me back. I could get used to this card.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
act("Each province with a public work pays the Emperor half its increase: 5 from Clark, 10 from Rich, 10 from Silke.", TH(
 ("Rich","Ten of the reservoir's twenty to the crown. The reservoir I didn't ask for, in the province I didn't choose."),
 ("Clark","Five. Half a ditch.")),
 {pid(2):-5, pid(7):-10, pid(5):-10, pid(1):25}, map_hl=[1,2,5,7])
rents()
taxes(.50)
say("Graham","The reservoir in my province, Majesty. Forty and forty.", TH(
 ("Graham","I paid nothing for the one in Province 7. I'll pay half of this one. A landlord should."),
 ("Reina","Graham offering to pay. I've seen everything now.")))
build("Province 3 Reservoir", 80, {1:40,3:40}, key="res3", at="L12:M14", hover=TH(
 ("Graham","L12 to M14, the south edge of the province, between the desert and my Customs House. Six squares that charge a soldier five each to step on."),
 ("","Cost split: Reina 40, Graham 40.")))
march({"W1":"Q15", "W2":"F16"}, "Rob moves: W1 onto the Province 7 Reservoir at Q15, raiding it and paying the toll; W2 back out of Province 1 to F16 in the strip.", TH(
 ("Rob","W1 is two squares from Rich's Scroll. W2 is going along the strip, not through Province 2. I'll explain why next year, if nobody's worked it out."),
 ("Rich","He paid me five to stand on my reservoir and charged me five for standing on it. Net nothing, and he's closer."),
 ("Reina","He's walking round Province 2. Not through it. Clark — your soldier.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 7 ==============================
R(7, "Steady weather", "winds")
say("Silke","Steady weather. Neither feast nor famine: an average harvest for this year.", TH(
 ("Silke","Average at a hundred and fifty. Everyone with a public work is positive. Graham's the only one without, and he's the landlord."),
 ("Graham","I have a reservoir. It started paying this year. I'd like that noted.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents()
taxes(.50)
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="J23", hover=TH(
 ("Reina","No system this round, so the booklet says Pagoda. J23, in the bottom corner, a long way off his road. He's had his twenty from the Summer Palace, and he won't walk back for another."),
 ("","Reina pays the 20.")))
say("Rob","This year: W1 to R14, next to Rich's Scroll. W2 to F15, along the strip.", TH(
 ("Rob","As promised. And the explanation, since nobody's said it: I haven't raided Province 2 once. Clark's soldier can't move until I do. I don't intend to until the last step."),
 ("Clark","...he's right. It's been standing on my Jar for five years and it isn't allowed to take a single step."),
 ("Reina","I worked that out last year. I said 'your soldier' and nobody heard the rest of the sentence.")))
march({"W1":"R14", "W2":"F15"}, "Rob's soldiers move as announced: W1 into R14, raiding Province 7 beside Rich's Scroll; W2 along the strip to F15.", TH(
 ("Rob","Five from Rich. W1 is one square from the Scroll. W2 is two from Clark's Vase."),
 ("Rich","One square. I could buy a soldier and stand it on the Scroll. Province 7's been raided, so mine could actually move."),
 ("Graham","He could. He's about to do something else instead. I can see it on his face.")))
say("Rich","Ladies and gentlemen. My Scroll is on S13, and three people at this table care what happens to it.", TH(
 ("Rich","Clark wants it to complete his set and take the throne. Reina wants me to guard it so Rob can't finish. Rob wants it left exactly where it is. I'm a wheat farmer with one piece of realia. I'd like offers."),
 ("Silke","He's auctioning his own raid."),
 ("Reina","It's the most Rich thing I have ever seen.")))
say("Clark","Forty. Sell me the Scroll and I'm complete, and the throne's mine before his soldier gets anywhere.", TH(
 ("Clark","I'd take it in a heartbeat."),
 ("Rob","He'd be Emperor, and off my list, and every piece he owns goes back to the box, the Vase I've been walking at since year one included. Reina gets his chair with nothing in it. Rich has sold the only piece he owns. That's two players on my list with empty provinces, and I need a piece from each. Rich would buy one. Reina would keep hers empty out of spite, and she'd be right to. I'd rather not start over."),
 ("Reina","He's right. If Clark sits here, I'd never own a thing again.")))
say("Reina","Forty-five, Rich, to buy a soldier and stand it on that Scroll.", TH(
 ("Reina","I won't buy a soldier for myself. I'll buy one for Rich. If his piece is guarded by a soldier that can move, Rob can't touch it with one."),
 ("Rich","The Emperor is bidding to protect my property. I've waited all evening for this.")))
say("Rob","Sixty, to leave it where it is.", TH(
 ("Rob","Sixty to a man for not doing anything. It's the most honest thing I've bought all evening."),
 ("Reina","I could go higher. Then I'm buying Rich a soldier with the Wall money, and he still has to stand it there. I'm out.")))
say("Clark","Ninety.", TH(
 ("Clark","If I complete, I change places with Reina and she hands me the imperial reserve. Ninety is cheap for a throne."),
 ("Rob","He's right. It is cheap.")))
say("Rob","A hundred and ten.")
say("Clark","A hundred and fifteen.", TH(
 ("Clark","That leaves me twenty-four and a half. The booklet wants twenty in hand when I declare. I've got four and a half of room."),
 ("Graham","He's bidding to the decimal place.")))
say("Rob","A hundred and twenty.", TH(
 ("Rob","He can't. A hundred and twenty would leave him nineteen and a half. The twenty-in-hand rule just bid against him."),
 ("Clark","Out. Beaten by a rule I've read a hundred times.")))
act("Rich takes Rob's hundred and twenty and leaves his Land Deed Scroll unguarded on S13.", TH(
 ("Rich","A hundred and twenty for not buying a soldier."),
 ("Graham","He sold the Emperor's throne for a hundred and twenty million and his own Scroll for nothing. In that order."),
 ("Reina","I'd be furious if it weren't exactly what I'd have done.")), {pid(7):120, pid(8):-120}, map_hl=[7,8])
sell_soldiers([(2,"G13")], "Clark buys a second soldier from Rob and stands it on his Vase at G13.", TH(
 ("Clark","If I can't move my soldiers, I can at least stand one on the piece he wants. He'll have to come straight at it."),
 ("Rob","Straight at it from F13, which is in the strip, where your soldier can't reach me because it can't move. Thank you for the twenty. I keep five."),
 ("Clark","I know. I'm buying it anyway. I'd rather lose it to a capture than to a walk.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 8 ==============================
R(8, "A careless year", "careless")
say("Silke","Good harvest for all. And every player plays a personal disaster.", TH(
 ("Silke","Every one of us. Including the Warlord, and his second disaster is the wedding. No raids this year."),
 ("Rob","No raids. Nobody said anything about walking.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents()
disaster(1,"the Arabian horse throws her. The trainer is lashed twenty times.", TH(
 ("Reina","Four, and a trainer with twenty lashes."),))
disaster(2,"the imperial barge rams a lock gate on the new canal during his inspection. He pays for the damage rather than lose face.", TH(
 ("Clark","Ten. For a gate on a canal in a province that isn't mine."),))
disaster(3,"the head chef retires after forty years and is promised a house and a pension.", TH(
 ("Graham","Five for a chef. I've been the landlord for four years and I've already got staff."),
 ("Rich","My chef. My pension. My chair.")))
disaster(5,"bandits are driven off by a young warrior; she must raise a shrine to him.", TH(
 ("Silke","Four to a stranger with a sword. The actual man with swords took my Customs House in the first round and sold it to Graham."),
 ("Graham","For thirty. I'd like that noted too.")))
disaster(7,"the Emperor takes his eldest daughter into the imperial household. He must feast the village.", TH(
 ("Rich","Two million, and look who the card says took her."),))
say("Rich","A high honour, they tell me.",
 "I'm in debt to everyone at this table for something.")
disaster(8,"a trusted lieutenant runs off with his daughter. No raids this year — too busy feasting the newlyweds.", TH(
 ("Rob","Five, and a wedding. W1 stays beside the Scroll. W2 walks. I announced it."),
 ("Reina","He's keeping both of his well away from anyone who can move.")))
taxes(.50)
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
say("Reina","Two links of Wall. It keeps out the horsemen from the north.", TH(
 ("Reina","It doesn't keep out the one in the strip. He's below it. Everybody's soldiers have always been below it."),
 ("Clark","She's building the Wall in the year a soldier is walking along the bottom of it.")))
march({"W2":"F14"}, "Rob's northern soldier walks along the strip to F14. No raid.", TH(
 ("Rob","F14, at an angle to Clark's Vase. Next year F13, straight above it. The year after, the Vase."),
 ("Clark","Two of my soldiers in Province 2, both frozen. I've got forty million worth of statues.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 9 ==============================
R(9, "Imperial charity", "chest")
say("Silke","Average harvest. And the Emperor opens her purse: two million to every player from the Emperor's reserve.", TH(
 ("Silke","Ten from Reina, two each."),
 ("Reina","Two million each, the year before I lose the throne. It's printed. I'll pay it.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
act("Imperial charity: 2 million from the Emperor's reserve to every other player.", TH(
 ("Rob","Two million from the Emperor to the Warlord. I'll put it towards the throne."),
 ("Reina","Of course he will.")),
 {pid(s):2 for s in ACTIVE if s != 1} | {pid(1):-10}, map_hl=[1])
rents()
taxes(.50)
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
say("Reina","My canal. If I'm leaving, I'm leaving a ditch.", TH(
 ("Reina","Twenty a year for whoever sits here next. I've a fair idea who."),
 ("Rob","She's building my canal. That's very generous.")))
march({"W1":"S13", "W2":"F13"}, "Rob's soldiers move as announced: W1 steps onto S13 and takes Rich's Land Deed Scroll; W2 to F13, straight above Clark's Vase.", TH(
 ("Rob","Three of four. Silke, Graham, Rich. Clark's Vase next year, and his soldier on it can't move."),
 ("Rich","A hundred and twenty for my Scroll, and he took the Scroll. I'm comfortably ahead."),
 ("Clark","F13. Straight above my soldier. If my soldier could move it would take him. It can't.")),
 take={"W1":("LD","N16")})
say("Clark","Reina. Buy a soldier. Anything.", TH(
 ("Clark","His soldier's in the strip. Reina's province has been raided five times, so Reina's soldiers could move."),
 ("Reina","From Province 1, a soldier bought now stands on F17 at best. It's four squares from F13 and it moves after him. It arrives the year after he does. I did that sum in year one."),
 ("Rob","She did. That's why she never bought one.")))
salaries({2:5, 5:5}, text="Reina pays Clark 5 and Silke 5.")

# ============================== YEAR 10 ==============================
R(10, "A bad harvest", "dribble1")
say("Silke","The seed rotted, the rains came late, and the ox went lame. Bad harvest.", TH(
 ("Silke","The last card I'll read to this Emperor."),
 ("Reina","Read it slowly.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents()
taxes(.50)
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
say("Reina","The last two links above my own province. If I'm leaving, the Wall over the throne room is finished.", TH(
 ("Reina","Eighty out of the reserve, which I'm about to hand to Rob anyway. I'd rather it went into stone."),
 ("Rob","She's spending my inheritance on a wall. That's fair. It's her wall.")))
say("Rob","This year: W2 to G13. Clark's soldier, then Clark's Vase.", TH(
 ("Rob","Straight down. It's the only move I've announced all evening that anybody could have stopped, and the only way to stop it was to have raided Province 2 for me."),
 ("Clark","I'd like it on the record that I'd have paid him to raid me."),
 ("Graham","Nobody at this table has ever wanted to be raided before. It's a first.")))
march({"W2":"G13"}, "Rob's northern soldier steps down from F13 onto G13, captures Clark's soldier, and takes his Vase as tribute.", TH(
 ("Rob","Four of four. A Customs House from Silke, a Jar from Graham, a Scroll from Rich, a Vase from Clark. A piece from every player who holds one."),
 ("Clark","The first raid on Province 2 all evening, and it's the one that ends it."),
 ("Reina","He's done it with two soldiers, ten years, and a timetable.")),
 take={"W2":("VA","N17")})
swap(8,1,"Robert Land has raided a piece of realia from every other player who holds realia, and changes places with the Emperor. Rob takes the throne of Province 1; Reina Osorio becomes the Warlord.", TH(
 ("Rob","The booklet: when you've raided a piece from each player who holds realia, you may change places with any player, including the Emperor. Every piece I took goes back to its province, and I take every bag in the imperial reserve."),
 ("Reina","The desert. I know where everything is."),
 ("Silke","He told us where he was going for ten years. We all wrote it down. It didn't help.")))
say("Rob","I'll build the rest of the Wall, and the canal in Province 5 gets dredged. And I'll tell you the tax rate a year in advance.", TH(
 ("Rob","An honest Emperor. We'll see how long that lasts. Telling people where you'll be gets you crowned, if you're standing somewhere they can't reach."),
 ("Reina","Two soldiers standing in other people's provinces, and every one of you knows the timetable. I'll be announcing nothing.")))
act("The table calls it there. A Warlord has completed his objective and taken the throne; the game is scored where it stands.", TH(
 ("Rich","I finish in the wheat fields with a hundred and twenty million of the Warlord's money. Somehow I'm in the best mood at this table."),
 ("Graham","Wheat to landlord. I bought my way up with a Customs House the Warlord took off Silke. I'm not proud. I'm in Province 3."),
 ("Clark","Held. Two soldiers, both frozen, one captured. I'm going to read the soldier rules again."),
 ("Reina","Emperor to Warlord. It's the only demotion in this game that comes with a better view.")), map_hl=list(ACTIVE), big=True)

RESULT = export(
 "The Warlord completed his objective — a piece of realia raided from every other realia-holding player — and changed places with the Emperor. The table stopped there, and every player is scored by the province they finished in against the one they drew.",
 ["Rob announced every move a year before he made it. What mattered was where he stood. His northern soldier walked the length of the Emperor's province, sixty in tolls with the Summer Palace on the way, though the Emperor was never on his list. It was going to Clark's Vase, which it took from the strip under the Wall without ever raiding Province 2, so that neither of Clark's soldiers was allowed to move.",
  "The peasants paid ransom. Silke and Graham each put a piece beside the Warlord's soldier in the first year so he would take it and leave, and Rob sold Silke's Customs House to Graham, who used it to complete his set and take Rich's chair. Rich, now a wheat farmer, auctioned off the fate of his own Scroll between the Official, the Emperor and the Warlord, and took Rob's hundred and twenty for leaving it unguarded — half a million more than Clark could pay and still keep twenty in hand. Rob paid it to keep Clark off the throne: crowned, Clark would have dropped off his list and left two players on it with nothing to raid, Rich and the dethroned Reina.",
  "Reina Osorio refused to buy soldiers, paid sixty in tribute to a soldier that was only passing through, and finishes the evening in the desert."])
