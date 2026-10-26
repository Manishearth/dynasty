# Game 5 — the six-player game. The Warlord completes his objective and takes the throne.
setup([1,2,3,5,7,8], "six", "The six-player game",
      "Six players · ten years · the Warlord takes the throne",
      "A fifth evening. Rich and Paddy sit out. Robert Land draws the throne, and Noah Tall draws the Warlord for the second week running — still announcing every move a year before he makes it, and this time it works. Eight pieces of realia for four collectors, and two soldiers.",
      short="6 players · 10 years",
      cast={1:"Rob", 2:"Silke", 3:"Clark", 5:"Reina", 7:"Graham", 8:"Noah"})

# ============================== SETUP ==============================
R(0, "The booklets fall differently", None, "Six players: the Emperor, the Official, the Gentry, two peasants and the Warlord (rulebook Section 4 and Appendix A). No Scholar, so the Emperor appoints someone to read I Ching. Each realia province holds two of its own pieces, and each collector needs one from each of the other three.")
act("Rich and Paddy sit this one out. The six remaining booklets are shuffled and drawn: Robert Land draws the Emperor, Silke the Official, Clark the Gentry, Reina the Silk Peasant, Graham the Wheat Peasant, and Noah Tall the Warlord, again.", TH(
 ("Rob","Two evenings in the desert, one on a silk farm, and now the throne. I know exactly how this chair gets taken. I've walked to it."),
 ("Noah","The Warlord, two weeks running. Last week I told you every move and you used it to put soldiers exactly where I'd be. Two of seven. I've been thinking about it all week."),
 ("Reina","Silk Peasant. Last week I climbed out of the wheat fields. This week the booklet's put me back in the fields, just a better class of field.")), map_hl=[1,2,3,5,7,8])
say("Noah","Same as last week: I'll tell you where my soldiers are going, every year, before they go.", TH(
 ("Noah","It cost me last week, and I'm doing it anyway. Every soldier moves one square a year and the board is face up. The trick isn't hiding where I'm going. It's going somewhere a soldier can't follow."),
 ("Clark","He announced his raids last week and finished with two of seven. He's announcing them again. Either he's learned nothing or he's learned something."),
 ("Rob","Something. I captured one of his soldiers last week. He's been very quiet about it.")))
act("Clark sets out the Harvest Pile: twenty-five hundred million in bags of every size, where everyone can see it.", TH(
 ("Clark","I bank the pile and I collect the rent. In the full game I was robbed twice by the rules. Tonight I'm the rules."),
 ("Graham","The landlord's counting the bank. Same as ever.")), map_hl=[3])
deal_grain("Clark deals 60 to each of the six players. That's the first year's harvest.", TH(
 ("Clark","Three hundred and sixty out of the pile before anyone's done anything."),
 ("Silke","Sixty. And I've got the tax to collect on top of it, which is a sentence I didn't expect to enjoy.")))
act("Robert Land appoints Reina Osorio to read the I Ching and keep the population count, at the Scholar's salary of 5. Reina shuffles the twenty cards and lays them face down.", TH(
 ("Rob","The woman who sat on this throne three times reads the omens to me. If anyone at this table knows what a bad card does to an Emperor, it's her."),
 ("Reina","Five a year to read the man who walked to my Winter Palace one square at a time. I'll read very clearly."),
 ("Noah","An ex-Emperor reading the cards to an ex-Warlord, while the actual Warlord watches. Rob's the only one at this table in a booklet he's never had.")), map_hl=[1,5])
take_stock("Silke, Clark, Reina and Graham each take two pieces of their own realia out of the box. Eight pieces in all, and they wait beside the board until they're sold.", TH(
 ("Silke","Two Customs Houses. Every collector needs one piece from each of the other three provinces, and there are only two of each. Three people want every piece."),
 ("Graham","Eight pieces, twelve wants. Four of us are going to be one short whatever happens. That's the game."),
 ("Noah","And every piece that goes on a square is one I can stand on.")))
act("Silke cuts out the Province 2 Irrigation System (one square by two), Clark the Province 3 Reservoir (two by three), and Graham the Province 7 Reservoir (two by two). Nobody sits in Provinces 4 or 6, so nothing is owed there.", TH(
 ("Clark","Two by three. The biggest cut-out in the box, and every square of it charges a soldier five to step on."),
 ("Graham","Two by two. I cut this one out on the first two evenings, and last week I built it myself in my first year on the throne. It's strange to be asking for it again."),
 ("Rob","Three cut-outs and three palaces. I've got a long list and nobody to split the palaces with.")), map_hl=[2,3,7])
place_army({"W1":"N18", "W2":"E22"}, "Noah stands his two soldiers on undeveloped land: W1 on N18, the notch beside Provinces 4, 5 and 7; W2 on E22, in the strip under the Wall, at the eastern end above the Emperor's province.", TH(
 ("Noah","N18 is one step from Reina's province and one from Graham's. E22 is above Rob. I'll say it plainly: the one in the north is going to the Emperor's palace, wherever he puts it, and the one in the south is going to whoever's nearest. Last week I had four soldiers and spread them thin. This week I've got two, and they each have a job."),
 ("Rob","He's put one where every square of my province is within five of it. I did exactly the same thing to Reina."),
 ("Reina","He did. I paid ten a square for three years.")))

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
rents()
say("Rob","Thirty-five per cent. Collect it, Silke.", TH(
 ("Rob","Higher than Reina opened in the full game. She went low and bought goodwill and lost the throne anyway. I'd rather have the grain."),
 ("Silke","Thirty-five, year one. He's not even pretending."),
 ("Reina","He watched me be reasonable for eleven years. This is the lesson he took.")))
taxes(.35)
act("Noah Tall declines to pay tax.", TH(
 ("Noah","My booklet's silent on tax. Rob set the precedent on the first two evenings and I kept it last week."),
 ("Rob","I invented that refusal. I can't even be cross.")), map_hl=[8])
say("Rob","The Summer Palace. I'll put it at G17.", TH(
 ("Rob","Twenty for the key to the Wall. G17 is the corner by Province 2, five squares from his soldier in the strip. Every square I own is within five of one of his two. I know, because I've done this sum from the other side."),
 ("Noah","Five squares. Four of them in Province 1, at ten each. I'll be there in year five, and he'll have paid me forty to watch me arrive."),
 ("Graham","He's building the thing the Warlord needs, and telling him where it is. It's the only way to build it.")))
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="G17")
say("Rob","No soldiers, Noah. I'm not buying any.", TH(
 ("Rob","Five soldiers I sold this table on the first two evenings, and last week I bought two from Noah and captured one of his with them. A soldier only catches a Warlord who walks up beside it. He's not going to walk up beside anything of mine twice. Twenty a soldier, five of it to him, to guard one square of thirty-four. I'll pay the tribute instead."),
 ("Noah","He's not buying from me. He knows exactly why that's right, and so do I.")))
lot(2,"CH",[
 B(3,5), B(7,6),
 B(5,8,"Eight.", TH(
   ("Reina","Eight, and it's going next to the notch, on O19, one step from his soldier."),
   ("Graham","She's putting it where he can take it. On purpose.")))],
 hover=TH(("Reina","He's going to get one piece from each of us; that's his whole objective. I'd rather choose which and when. A Customs House now, one step from his soldier, and then he leaves me alone."),
          ("Graham","A ransom. She's paying the Warlord in advance. ...that's actually sensible.")), at="O19")
lot(3,"LD",[
 B(2,5), B(5,6),
 B(7,7,"Seven.","Seven. I need a Scroll, and Reina's just spent her eight on a ransom.")],
 hover="Graham puts it on S13, the far corner of Province 7, five squares from the soldier in the notch.", at="S13")
lot(5,"DJ",[
 B(2,6), B(3,7),
 B(7,8,"Eight.", TH(
   ("Graham","Eight, and it goes on O17, next to the notch. Reina's right. One piece each, and I'll pick mine."),
   ("Clark","Two ransoms in one round. The peasants have unionised against a single soldier.")))],
 hover=TH(("Graham","O17 is one step from N18. He takes the Jar, I buy it back, and the Scroll in the corner is never worth his walk."),
          ("Noah","The peasants are paying me to go away. I'll take it. I'll even go away.")), at="O17")
lot(7,"VA",[
 B(3,6),
 B(2,8,"Eight.", TH(
   ("Silke","Eight. G13, near the top of my province. Nine squares from the soldier in the strip and seven from the other. The furthest square I own from either of them."),
   ("Noah","Nine squares. She's measured it.")))],
 hover="Silke puts it on G13.", at="G13")
march({"W1":"O19", "W2":"F21"}, "Noah's soldiers move as announced: W1 steps onto O19 and takes Reina's Customs House; W2 steps into Province 1 at F21.", TH(
 ("Noah","Reina's ransom, collected the round it was offered, and ten from the Emperor. One piece from each of you, and that's one."),
 ("Reina","He paid a toll to my province crossing the river to get it. I've been paid five to be robbed."),
 ("Rob","Ten. The first of four.")),
 take={"W1":("CH","N12")})
say("Noah","The Customs House goes to whoever pays most. I'm saying that now, so nobody thinks I lied later.", TH(
 ("Noah","Reina may want it back. Graham needs one too. So does Clark. It's the most useful thing I own."),
 ("Reina","He's auctioning my ransom. I should have read the small print, except he said it out loud.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 for collecting the tax and Reina 5 for reading the cards.")

# ============================== YEAR 2 ==============================
R(2, "Fortune and misfortune", "goodevil")
say("Reina","Good harvest for all. Provinces 2, 4, 6 and 8 play a personal disaster. Nobody's in 4 or 6, so that's Silke and Noah.", TH(
 ("Reina","Reading it for the Emperor I used to be. I don't miss the chair. I miss the salary."),
 ("Silke","Of course it's me.")))
harvest("Clark pays out the harvest from the Harvest Pile.")
rents()
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Silke","Four million for a driver. The same chariot, the same wheel, the same tree as last week. It's a very consistent tree."),
 ("Clark","That one hit me in the full game. It hits whoever sits in that chair.")))
disaster(8,"wounded in the legs in his last battle. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Noah","So W1 walks back into the notch and waits for Graham's Jar to be worth the step. W2 keeps going."),
 ("Graham","A year's grace for the Jar I put out as a ransom. I'll take it, I suppose.")))
taxes(.35)
say("Silke","Majesty. The irrigation. Fifteen from me, fifteen from you, ten a year forever.", TH(
 ("Silke","The same deal Clark made in the full game, and I watched it pay back in three years."),
 ("Rob","Half of thirty for a permanent rise in her tax. I'd be a fool to refuse. I've been a lot of things at this table.")))
build("Province 2 Irrigation System", 30, {1:15,2:15}, key="irr2", at="I15:I16", hover=TH(
 ("Silke","I15 and I16, in the east of my province, by the river. Any soldier that steps on it pays me five."),
 ("","Cost split: Rob 15, Silke 15.")))
lot(2,"CH",[
 B(7,9),
 B(3,10,"Ten.", TH(
   ("Clark","Ten. Customs Houses are the one thing in this game that are scarce and also mine to want."),
   ("Graham","There's one more, and Noah's holding it. Fine.")))],
 hover="Clark puts it on K10, deep in the west of Province 3, as far from both soldiers as his province goes.", at="K10")
lot(3,"LD",[
 B(2,7),
 B(5,9,"Nine.", TH(
   ("Reina","Nine. P26, the far end of Province 5 by the sea. I've paid my ransom. I don't intend to pay it twice."),
   ("Silke","That was the last Scroll in the stock. I've got a Vase, I'm about to buy a Jar, and I'll be one Scroll short.")))],
 at="P26")
lot(5,"DJ",[
 B(3,8),
 B(2,10,"Ten.", TH(
   ("Silke","Ten, and it's going on J12. My Vase at the top of my province and my Jar at the bottom, as far apart as I can get them."),
   ("Clark","That's the Jar I needed. There were two, and one's a ransom.")))],
 hover="Silke puts it on J12, far from both soldiers.", at="J12")
lot(7,"VA",[
 B(2,None,"I have one.","I've got a Vase. Let the others fight over this one."),
 B(5,7),
 B(3,9,"Nine.", TH(
   ("Clark","Nine. K9, next to my Customs House, at the western edge. Two of three, and the one I'm missing is the Jar."),
   ("Reina","That was the last Vase. I'm missing it, and the Customs House he took."))),
 B(5,None,"Out.","Out. Nine's more than I've got to spare after the Scroll.")],
 at="K9")
sell_soldiers([(2,"J12")], "Silke buys a soldier from Noah and stands it on her Dragon Jar at J12.", TH(
 ("Silke","A soldier on the Jar. Twenty. Nobody can raid a square with my soldier on it unless he takes it straight on, and if he comes straight at it, mine takes his."),
 ("Noah","Her soldier can't move until I've raided Province 2. I haven't. I'm noting that, out loud, as promised."),
 ("Rob","He's noting it. I'd be more worried by that than she is.")))
march({"W1":"O18", "W2":"F20"}, "Noah moves: W1 back to O18 in the notch; W2 to F20, raiding Province 1 again.", TH(
 ("Noah","Ten from the Emperor. Three squares to the palace."),
 ("Rob","Twenty paid, forty to come. The palace cost me twenty to build.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 3 ==============================
R(3, "Rain and flood", "rainflood")
say("Reina","Good harvest for Provinces 1, 3, 6 and 7. Rivers flood in 2, 4, 5 and 8.", TH(
 ("Reina","Bad for me, bad for Silke, bad for Noah. I read a flood over my own province without blinking. I've had worse years in better chairs."),
 ("Graham","Good for me. I'm going to need it.")))
harvest("Clark pays out the harvest from the Harvest Pile.")
rents()
taxes(.40)
say("Graham","Majesty. The reservoir.", TH(
 ("Graham","I said it to Reina for nine years in the full game. Last week I was the one on the throne, and I built it in my first year. Saying it to Rob is new."),
 ("Rob","I was there the first time. I watched her say 'after the Wall' for nine years. Sixty. This year.")))
build("Province 7 Reservoir", 60, {1:60}, key="res7", at="Q15:R16", hover=TH(
 ("Graham","Q15 to R16, the middle of Province 7, between the notch and my Scroll. Anything coming for the Scroll pays me five to cross it."),
 ("Rob","Sixty from the crown, in year three. Reina, you deferred it nine times in the full game, and you built it in year two of the peasant game. I'm somewhere in between."),
 ("Reina","Noted. Bitterly.")))
march({"W1":"O17", "W2":"F19"}, "Noah's southern soldier steps onto O17 and takes Graham's Dragon Jar; the northern one raids Province 1 at F19.", TH(
 ("Noah","Graham's ransom. Two of five: Reina and Graham. The peasants are done paying me. And ten from Rob; two squares to the palace."),
 ("Graham","Exactly as planned. Now I buy it back."),
 ("Rob","Thirty paid. I can see the palace from his square.")),
 take={"W1":("DJ","N13")})
say("Graham","How much for the Jar? And how much for the Customs House?", TH(
 ("Graham","The Jar's mine. The Customs House is Reina's, and it's the piece I'm missing. With both I'm complete."),
 ("Reina","He's going to buy my ransom. With his ransom. And then take somebody's chair."),
 ("Noah","He's asked both questions at once. I'll answer them next year, when he's had a good harvest.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
say("Reina","Population increases by half. Good harvest for everyone. Consumption up by half, forever.", TH(
 ("Reina","A hundred and fifty million. The last time I heard this card from the throne, I lost the throne three years later."),
 ("Rob","I'm not going to be here in seven years. One way or another.")))
harvest("Clark pays out the harvest from the Harvest Pile.")
rents()
taxes(.50)
say("Rob","The Winter Palace. G26.", TH(
 ("Rob","The canal in Province 5 needs it, and Reina wants her canal. G26, the far corner, by the sea. He only needs one palace. He's two squares from the first. This one's just a palace."),
 ("Noah","He's right. I only need one. He's built me a spare.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="G26")
give(8, 7, "DJ", at="O16")
act("Graham buys back his Dragon Jar from Noah for 15, and puts it on O16.", TH(
 ("Graham","Fifteen for the Jar I paid eight for. Ransom has a price."),
 ("Noah","And it isn't counted against me. He paid; I raided. The raid's on the books.")), {pid(7):-15, pid(8):15}, map_hl=[7,8])
act("Noah sells Reina's Customs House to the highest bidder. Reina offers 20; Graham offers 30.", TH(
 ("Reina","Twenty is everything I can spare. He'll go higher."),
 ("Graham","Thirty. It completes me. I'm sorry, Reina. No — I'm not, quite."),
 ("Noah","As announced in year one. Highest bidder.")), map_hl=[5,7,8])
give(8, 7, "CH", at="O15")
act("Graham buys Reina's old Customs House from Noah for 30, and puts it on O15.", TH(
 ("Graham","Scroll, Jar, Customs House. Three of three, and more than twenty in hand."),
 ("Clark","He's looking at me."),
 ("Silke","He's looking at both of us. Either chair will do.")), {pid(7):-30, pid(8):30}, map_hl=[7,8])
swap(7,3,"Graham Garner declares a complete set and replaces Clark Grafton. Graham becomes Gentry of Province 3; Clark becomes Wheat Peasant of Province 7.", TH(
 ("Graham","Hand back the Scroll — it's native to Province 3 — keep the Jar and the Customs House, and take every bag Clark's holding. They go on K11 and L10, next to where his were, at the far west of the province. Wheat to landlord. I bank the pile now."),
 ("Clark","Robbed by the rules again. Twice in the full game, and now tonight: somebody climbing over me with every bag I own in their pocket."),
 ("Noah","And Clark's now in the province my soldier lives in, with nothing on the board. He'll have to buy something. And put it somewhere.")),
 at={"DJ":"K11", "CH":"L10"})
say("Clark","Province 7. With the reservoir. Well.", TH(
 ("Clark","Sixty from the pile and a booklet that says I'm hard-working. The reservoir's the only thing in this province that isn't a raid square."),
 ("Graham","I built my own replacement's income in the peasant game. Rob built this one. Somebody's always building Province 7 a reservoir for somebody else.")))
act("The pieces handed back in the seat change go up for auction this round: Silke sells the Customs House, Graham the Scroll, and Clark the Vase.", TH(
 ("Graham","My Scroll goes back to Province 3, and Province 3 is me now. I auction my own piece the same evening I handed it in."),
 ("Silke","Three pieces back on the table, and one of them is the Scroll I'm missing.")), map_hl=[2,3,7])
lot(2,"CH",[
 B(5,6),
 B(7,8,"Eight.","Eight. I need everything in Province 7 now, and the Customs House is first."),
 B(5,9,"Nine.", TH(
   ("Reina","Nine. My Customs House back, in a manner of speaking. Now I'm missing a Vase."),
   ("Clark","She's outbid me for a Customs House I used to own. Tonight everything I bid on used to be mine."))),
 B(7,None,"Have it.","Out. I've got sixty from the pile and a whole set to buy.")],
 hover="Reina puts it on P25, next to her Scroll by the sea.", at="P25")
lot(3,"LD",[
 B(7,6),
 B(2,10,"Ten.", TH(
   ("Silke","Ten. It's the piece I'm missing. Vase, Jar, Scroll — I'm complete, and I'm the Official."),
   ("Rob","She's the Official. If she completes, she can take my seat."))),
 B(8,12,"Twelve.", TH(
   ("Noah","Twelve. I have no use for a Scroll. I have a great deal of use for the Official not having one."),
   ("Rob","I did that in the full game. Eighty for a bowl. He's done it for twelve."))),
 B(2,15,"Fifteen."),
 B(8,20,"Twenty.", TH(
   ("Noah","Twenty. I'll go higher. She knows I'll go higher."),
   ("Silke","He's got more grain than me and nothing to spend it on but this."))),
 B(2,None,"Out.","Out. One Scroll in the world, and the man who's robbing the Emperor owns it.")],
 hover="Noah puts it on N14, in his own territory, in plain sight.", at="N14")
lot(7,"VA",[
 B(5,8,"Eight.","Customs House, Scroll, and this. One lot and I'm complete."),
 B(8,12,"Twelve.", TH(
   ("Noah","Twelve. If Reina gets it she's complete, and the chair she'd take is Silke's. Then Silke has nothing on the board, and I can't take a piece from a player who owns none."),
   ("Reina","He's bidding against me to protect his own target. That's the most honest act of sabotage I've ever seen."))),
 B(5,16,"Sixteen."),
 B(8,25,"Twenty-five.", TH(
   ("Noah","Twenty-five. Two pieces this round I have no use for, to stop two people climbing past the one I'm robbing."),
   ("Rob","Eighty for a bowl, in the full game. I'd like it on the record that I taught him this."))),
 B(5,None,"Out.","Out. Eighty-odd in grain, and the Warlord has nearly twice that and nothing else to spend it on.")],
 hover="Noah puts it on N15, beside the Scroll, in plain sight.", at="N15")
march({"W1":"P16", "W2":"F18"}, "Noah moves: W1 into Province 7 at P16, raiding Clark's new province; W2 to F18, raiding Province 1.", TH(
 ("Noah","Five from Clark, ten from Rob. W2 is one square from the palace."),
 ("Clark","My first act as a wheat farmer is to pay a Warlord. In the full game it took me nine years to get this low.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 5 ==============================
R(5, "Heaven has favourites", "heaven")
say("Reina","Good harvest for 2, 4 and 5. Bad for 1, 3, 6, 7 and 8.", TH(
 ("Reina","Good for me and Silke. Bad for the Emperor, the new Gentry, the new wheat farmer and the Warlord."),
 ("Graham","My first year as landlord and heaven doesn't like me. Fair.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents(hover="Graham collects rent from Reina and Clark. Clark used to collect it from him.")
taxes(.50)
build("Grand Canal in Province 5 — 2 sections", 80, {1:80}, canal={5:2})
say("Reina","Two sections in my province. Thank you, Majesty.", TH(
 ("Reina","Twenty a year from next year. I built this canal for Silke in the peasant game. It's nice to be on the receiving end."),
 ("Rob","Eighty on someone else's ditch. Reina, you'll notice I'm doing it in the right order.")))
march({"W2":"G17"}, "Noah's northern soldier steps onto G17 and raids the square holding the Summer Palace. The Emperor pays him the cost of the structure: 20.", TH(
 ("Noah","Year five, as announced. Three of five: Reina, Graham, the Emperor. Silke and Clark left."),
 ("Rob","Ten, ten, ten, ten and twenty. Sixty for the privilege of being right about the date."),
 ("Silke","Three of five. And he's in the corner next to my province.")))
say("Noah","Clark. I'll sell you the Scroll. Eight.", TH(
 ("Noah","He needs it — Customs House, Scroll, Jar for Province 7. I'm selling it to him at a loss, and he'll put it in Province 7, where my soldier is. Both of us know that."),
 ("Clark","He's offering me a bargain and telling me it's bait. I want to refuse on principle and I can't afford principle.")))
give(8, 3, "LD", at="S13")
act("Clark buys the Land Deed Scroll from Noah for 8, and puts it on S13, the far corner of Province 7.", TH(
 ("Clark","S13. The corner Graham used. Three squares from his soldier, with the reservoir in the way."),
 ("Noah","Three squares. Thank you, Clark.")), {pid(7):-8, pid(8):8}, map_hl=[7,8])
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 6 ==============================
R(6, "Shared increase", "share")
say("Reina","Average harvest. And every province with a public work shares the increase with the Emperor, fifty-fifty.", TH(
 ("Reina","That's Silke's irrigation, Clark's reservoir and my canal. Five, ten and ten to the crown."),
 ("Rob","Three ditches I paid for, paying me back. I could get used to this card.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
act("Each province with a public work pays the Emperor half its increase: 5 from Silke, 10 from Clark, 10 from Reina.", TH(
 ("Clark","Ten of the reservoir's twenty to the crown. The reservoir I didn't ask for, in the province I didn't choose."),
 ("Silke","Five. Half a ditch.")),
 {pid(2):-5, pid(7):-10, pid(5):-10, pid(1):25}, map_hl=[1,2,5,7])
rents()
taxes(.50)
say("Graham","The reservoir in my province, Majesty. Forty and forty.", TH(
 ("Graham","I paid nothing for the one in Province 7. I'll pay half of this one. A landlord should."),
 ("Rob","Graham offering to pay. I've seen everything now.")))
build("Province 3 Reservoir", 80, {1:40,3:40}, key="res3", at="L12:M14", hover=TH(
 ("Graham","L12 to M14, the south edge of the province, between the desert and my Customs House. Six squares that charge a soldier five each to step on."),
 ("","Cost split: Rob 40, Graham 40.")))
march({"W1":"Q15", "W2":"F16"}, "Noah moves: W1 onto the Province 7 Reservoir at Q15, raiding it and paying the toll; W2 back out of Province 1 to F16 in the strip.", TH(
 ("Noah","W1 is two squares from Clark's Scroll. W2 is going along the strip, not through Province 2. I'll explain why next year, if nobody's worked it out."),
 ("Clark","He paid me five to stand on my reservoir and charged me five for standing on it. Net nothing, and he's closer."),
 ("Rob","He's walking round Province 2. Not through it. Silke — your soldier.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 7 ==============================
R(7, "Steady weather", "winds")
say("Reina","Steady weather. Neither feast nor famine: an average harvest for this year.", TH(
 ("Reina","Average at a hundred and fifty. Everyone with a public work is positive. Graham's the only one without, and he's the landlord."),
 ("Graham","I have a reservoir. It started paying this year. I'd like that noted.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents()
taxes(.50)
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="J23", hover=TH(
 ("Rob","No system this round, so the booklet says Pagoda. J23, in the bottom corner. He's already got his palace off me. This one's just a pagoda."),
 ("","Rob pays the 20.")))
say("Noah","This year: W1 to R14, next to Clark's Scroll. W2 to F15, along the strip.", TH(
 ("Noah","As promised. And the explanation, since nobody's said it: I haven't raided Province 2 once. Silke's soldier can't move until I do. I don't intend to until the last step."),
 ("Silke","...he's right. It's been standing on my Jar for five years and it isn't allowed to take a single step."),
 ("Rob","I worked that out last year. I said 'your soldier' and nobody heard the rest of the sentence.")))
march({"W1":"R14", "W2":"F15"}, "Noah's soldiers move as announced: W1 into R14, raiding Province 7 beside Clark's Scroll; W2 along the strip to F15.", TH(
 ("Noah","Five from Clark. W1 is one square from the Scroll. W2 is two from Silke's Vase."),
 ("Clark","One square. I could buy a soldier and stand it on the Scroll. Province 7's been raided, so mine could actually move."),
 ("Graham","He could. He's about to do something else instead. I can see it on his face.")))
say("Clark","Ladies and gentlemen. My Scroll is on S13, and three people at this table care what happens to it.", TH(
 ("Clark","Silke wants it to complete her set and take the throne. Rob wants me to guard it so Noah can't finish. Noah wants it left exactly where it is. I'm a wheat farmer with one piece of realia. I'd like offers."),
 ("Reina","He's auctioning his own raid."),
 ("Rob","It's the most Clark thing I have ever seen.")))
say("Silke","Forty. Sell me the Scroll and I'm complete, and the throne's mine before his soldier gets anywhere.", TH(
 ("Silke","Last week I completed my set and didn't take the throne. This week I'd take it in a heartbeat."),
 ("Noah","She'd be Emperor, and her pieces would go back to the box, and I'd need a palace from her instead of a Vase. I'd rather not start over.")))
say("Rob","Forty-five, Clark, to buy a soldier and stand it on that Scroll.", TH(
 ("Rob","I won't buy a soldier for myself. I'll buy one for Clark. If his piece is guarded by a soldier that can move, Noah can't touch it with one."),
 ("Clark","The Emperor is bidding to protect my property. I've waited three evenings for this.")))
say("Noah","Sixty, to leave it where it is.", TH(
 ("Noah","Sixty to a man for not doing anything. It's the most honest thing I've bought all evening."),
 ("Rob","I could go higher. Then I'm buying Clark a soldier with the Wall money, and he still has to stand it there. I'm out.")))
say("Silke","Ninety.", TH(
 ("Silke","If I complete, I change places with Rob and he hands me the imperial reserve. Ninety is cheap for a throne."),
 ("Noah","She's right. It is cheap.")))
say("Noah","A hundred and ten.")
say("Silke","A hundred and fifteen.", TH(
 ("Silke","That leaves me twenty-four and three-quarters. The booklet wants twenty in hand when I declare. I've got four and three-quarters of room."),
 ("Graham","She's bidding to the decimal place.")))
say("Noah","A hundred and twenty.", TH(
 ("Noah","She can't. A hundred and twenty would leave her nineteen and three-quarters. The twenty-in-hand rule just bid against her."),
 ("Silke","Out. Beaten by a rule I've read a hundred times.")))
act("Clark takes Noah's hundred and twenty and leaves his Land Deed Scroll unguarded on S13.", TH(
 ("Clark","A hundred and twenty for not buying a soldier. In the full game I skimmed for six years and never made that much in one sentence."),
 ("Graham","He sold the Emperor's throne for a hundred and twenty million and his own Scroll for nothing. In that order."),
 ("Rob","I'd be furious if it weren't exactly what I'd have done.")), {pid(7):120, pid(8):-120}, map_hl=[7,8])
sell_soldiers([(2,"G13")], "Silke buys a second soldier from Noah and stands it on her Vase at G13.", TH(
 ("Silke","If I can't move my soldiers, I can at least stand one on the piece he wants. He'll have to come straight at it."),
 ("Noah","Straight at it from F13, which is in the strip, where your soldier can't reach me because it can't move. Thank you for the twenty. I keep five."),
 ("Silke","I know. I'm buying it anyway. I'd rather lose it to a capture than to a walk.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 8 ==============================
R(8, "A careless year", "careless")
say("Reina","Good harvest for all. And every player plays a personal disaster.", TH(
 ("Reina","Every one of us. Including the Warlord, and his second disaster is the wedding. No raids this year."),
 ("Noah","No raids. Nobody said anything about walking.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents()
disaster(1,"the Arabian horse throws him. The trainer is lashed twenty times.", TH(
 ("Rob","Four. Reina's horse. I've inherited the stable."),
 ("Reina","It's a very consistent horse.")))
disaster(2,"the imperial barge rams a lock gate on the new canal during her inspection. She pays for the damage rather than lose face.", TH(
 ("Silke","Ten. For a gate on a canal in a province that isn't mine."),
 ("Clark","That one cost me ten in the full game. It was a hypothetical lock then too.")))
disaster(3,"the head chef retires after forty years and is promised a house and a pension.", TH(
 ("Graham","Five for a chef. I've been the landlord for four years and I've already got staff."),
 ("Clark","My chef. My pension. My chair.")))
disaster(5,"bandits are driven off by a young warrior; she must raise a shrine to him.", TH(
 ("Reina","Four to a stranger with a sword. The actual man with swords took my Customs House in the first round and sold it to Graham."),
 ("Graham","For thirty. I'd like that noted too.")))
disaster(7,"the Emperor takes his eldest daughter into the imperial household. He must feast the village.", TH(
 ("Clark","Two million, and look who the card says took her."),
 ("Rob","That card was Graham's line in the full game. 'A high honour, they tell me.'"),
 ("Graham","It was a good line. Use it.")))
say("Clark","A high honour, they tell me.",
 "Stolen, and properly attributed in my head. I'm in debt to everyone at this table for something.")
disaster(8,"a trusted lieutenant runs off with his daughter. No raids this year — too busy feasting the newlyweds.", TH(
 ("Noah","Five, and a wedding. W1 stays beside the Scroll. W2 walks. I announced it."),
 ("Rob","Last week I captured one of his soldiers during this exact wedding. He's keeping both of his well away from anyone who can move.")))
taxes(.50)
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
say("Rob","Two links of Wall. It keeps out the horsemen from the north.", TH(
 ("Rob","It doesn't keep out the one in the strip. He's below it. Everybody's soldiers have always been below it."),
 ("Silke","He's building the Wall in the year a soldier is walking along the bottom of it.")))
march({"W2":"F14"}, "Noah's northern soldier walks along the strip to F14. No raid.", TH(
 ("Noah","F14, at an angle to Silke's Vase. Next year F13, straight above it. The year after, the Vase."),
 ("Silke","Two of my soldiers in Province 2, both frozen. I've got forty million worth of statues.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 9 ==============================
R(9, "Imperial charity", "chest")
say("Reina","Average harvest. And the Emperor opens his purse: two million to every player from the Emperor's reserve.", TH(
 ("Reina","Ten from Rob, two each. This card cost me fourteen from the throne in the full game."),
 ("Rob","Two million each, the year before I lose the throne. It's printed. I'll pay it.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
act("Imperial charity: 2 million from the Emperor's reserve to every other player.", TH(
 ("Noah","Two million from the Emperor to the Warlord. I'll put it towards the throne."),
 ("Rob","Of course he will.")),
 {pid(s):2 for s in ACTIVE if s != 1} | {pid(1):-10}, map_hl=[1])
rents()
taxes(.50)
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
say("Rob","My canal. If I'm leaving, I'm leaving a ditch.", TH(
 ("Rob","Twenty a year for whoever sits here next. I've a fair idea who."),
 ("Noah","He's building my canal. That's very generous.")))
march({"W1":"S13", "W2":"F13"}, "Noah's soldiers move as announced: W1 steps onto S13 and takes Clark's Land Deed Scroll; W2 to F13, straight above Silke's Vase.", TH(
 ("Noah","Four of five. Reina, Graham, Rob, Clark. Silke's Vase next year, and her soldier on it can't move."),
 ("Clark","A hundred and twenty for my Scroll, and he took the Scroll. I'm comfortably ahead."),
 ("Silke","F13. Straight above my soldier. If my soldier could move it would take him. It can't.")),
 take={"W1":("LD","N16")})
say("Silke","Rob. Buy a soldier. Anything.", TH(
 ("Silke","His soldier's in the strip. Rob's province has been raided five times, so Rob's soldiers could move."),
 ("Rob","From Province 1, a soldier bought now stands on F17 at best. It's four squares from F13 and it moves after him. It arrives the year after he does. I did that sum in year one."),
 ("Noah","He did. That's why he never bought one.")))
salaries({2:5, 5:5}, text="Rob pays Silke 5 and Reina 5.")

# ============================== YEAR 10 ==============================
R(10, "A bad harvest", "dribble1")
say("Reina","The seed rotted, the rains came late, and the ox went lame. Bad harvest.", TH(
 ("Reina","The last card I'll read to this Emperor."),
 ("Rob","Read it slowly.")))
harvest("Graham pays out the harvest from the Harvest Pile.")
rents()
taxes(.50)
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
say("Rob","The last two links above my own province. If I'm leaving, the Wall over the throne room is finished.", TH(
 ("Rob","Eighty out of the reserve, which I'm about to hand to Noah anyway. I'd rather it went into stone."),
 ("Noah","He's spending my inheritance on a wall. That's fair. It's his wall.")))
say("Noah","This year: W2 to G13. Silke's soldier, then Silke's Vase.", TH(
 ("Noah","Straight down. It's the only move I've announced all evening that anybody could have stopped, and the only way to stop it was to have raided Province 2 for me."),
 ("Silke","I'd like it on the record that I'd have paid him to raid me."),
 ("Graham","Nobody at this table has ever wanted to be raided before. It's a first.")))
march({"W2":"G13"}, "Noah's northern soldier steps down from F13 onto G13, captures Silke's soldier, and takes her Vase as tribute.", TH(
 ("Noah","Five of five. A Customs House from Reina, a Jar from Graham, a palace from Rob, a Scroll from Clark, a Vase from Silke. A different piece from every player."),
 ("Silke","The first raid on Province 2 all evening, and it's the one that ends it."),
 ("Rob","I walked to Reina's palace one square a year in the peasant game and stopped one piece short. He's done it with two soldiers, ten years, and a timetable.")),
 take={"W2":("VA","N17")})
swap(8,1,"Noah Tall has raided a different piece of realia from every player, and changes places with the Emperor. Noah takes the throne of Province 1; Robert Land becomes the Warlord.", TH(
 ("Noah","The booklet: when you've raided a piece from each player, you may change places with any player, including the Emperor. Every piece I took goes back to its province, and I take every bag in the imperial reserve."),
 ("Rob","The desert. Again. I know where everything is."),
 ("Reina","He told us where he was going for ten years. We all wrote it down. It didn't help.")))
say("Noah","I'll build the rest of the Wall, and the canal in Province 5 gets dredged. And I'll tell you the tax rate a year in advance.", TH(
 ("Noah","An honest Emperor. We'll see how long that lasts. Last week I learned that telling people where you'll be gets you captured. This week I learned it gets you crowned, if you're standing somewhere they can't reach."),
 ("Rob","Two soldiers standing in other people's provinces, and every one of you knows the timetable. I'll be announcing nothing.")))
act("The table calls it there. A Warlord has completed his objective and taken the throne; the game is scored where it stands.", TH(
 ("Clark","I finish in the wheat fields with a hundred and twenty million of the Warlord's money. Somehow I'm in the best mood at this table."),
 ("Graham","Wheat to landlord. I bought my way up with a Customs House the Warlord took off Reina. I'm not proud. I'm in Province 3."),
 ("Silke","Held. Two soldiers, both frozen, one captured. I'm going to read the soldier rules again before next week."),
 ("Rob","Emperor to Warlord. It's the only demotion in this game that comes with a better view.")), map_hl=list(ACTIVE), big=True)

RESULT = export(
 "The Warlord completed his objective — a different piece of realia raided from every other player — and changed places with the Emperor. The table stopped there, and every player is scored by the province they finished in against the one they drew.",
 ["Noah announced every move a year before he made it, as he had the week before. The difference was where he stood. He took the Emperor's palace by walking at it for five years, and he took Silke's Vase from the strip under the Wall without ever raiding her province, so that neither of her soldiers was allowed to move.",
  "The peasants paid ransom. Reina and Graham each put a piece beside the Warlord's soldier in the first year so he would take it and leave, and Noah sold Reina's Customs House to Graham, who used it to complete his set and take Clark's chair. Clark, now a wheat farmer, auctioned off the fate of his own Scroll between the Official, the Emperor and the Warlord, and took Noah's hundred and twenty for leaving it unguarded — a quarter of a million more than Silke could pay and still keep twenty in hand.",
  "Robert Land spent two evenings as the Warlord and one on a silk farm before he drew the throne. He refused to buy soldiers, paid sixty in tribute for one palace, and finishes the evening back in the desert."])
