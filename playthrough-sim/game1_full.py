# Game 1 — the full game. Eight players, fresh booklets, and every public work gets built.
setup([1,2,3,4,5,6,7,8], "full", "The full game",
      "Eight players · ten years · everything gets built",
      "All eight provinces, and a table that signs a compact before the first card: one work a year, the split agreed in advance, and every public work in the book built. The Warlord announces every raid a year ahead, and keeps his word.",
      short="8 players · 10 years")

# ============================== SETUP ==============================
R(0, "Fresh booklets", None, "All eight provinces (rulebook Section 4 and Appendix A). Every province holds four pieces of its own realia, the Warlord takes four soldiers, and every public work in the book is owed to somebody: three palaces, twelve links of Wall, eight canal sections, the irrigation system and the two reservoirs. Each realia player must collect one piece of every type except their own, plus 20 million in hand; the Warlord takes his four soldiers and the 40 raid squares.")
act("Eight booklets, shuffled and drawn face down. Reina draws the Emperor, Clark the Official, Rich the Gentry, Noah the Scholar, Silke the Silk Peasant, Paddy the Rice Peasant, Graham the Wheat Peasant — and Rob the Warlord.", TH(
 ("Graham","Wheat. The worst land on the board, and a reservoir the crown is meant to pay for. I'm going to ask for it early."),
 ("Silke","Silk. Province 5, down in the far corner by the sea. The sea's open to his soldiers, so nowhere's out of reach. It's just a long walk."),
 ("Rob","Warlord. I'm the one who says the arithmetic out loud. Tonight I am the arithmetic."),
 ("Reina","The throne. Every other booklet has a section on how to replace me. I'd better start building.")), map_hl=list(range(1,9)))
say("Reina","Before anyone opens a bag: the Province 7 Reservoir goes first. This year.", TH(
 ("Reina","The booklet says the crown pays for this one in full, and 'delayed too long in building Public Works' is a revolt cause. Graham was going to ask in year two. I'd rather he never had to."),
 ("Graham","She's building it for me. She's building it at me, which is different, and I'll take both."),
 ("Paddy","It's sixty million out of the crown in year one, and it's a public apology. I'd like to be the one who points that out later.")))
say("Reina","And then all of it. Every palace, every link, every section, every ditch. I want a compact: one work a year, and we agree the split before the card is turned.", TH(
 ("Reina","A thousand and thirty million. The crown can't pay for that alone. The only way the whole list gets built is if the people who'll use it pay into it."),
 ("Clark","A compact. She's turned the Emperor's booklet into a co-op. I'm in, and I'm keeping the minutes."),
 ("Rich","I'm the Gentry. My booklet says I'm greedy. I'll sign anything that's cheaper than a revolt."),
 ("Rob","Nobody's asked the Warlord to sign. That's correct. I wouldn't.")))
deal_grain("Rich, the Gentry, sets out the Harvest Pile and deals 60 to each player.", TH(
 ("Rich","Twenty-five hundred in the pile, four hundred and eighty out of it before anyone's moved. The banker sees every bag. I like this job already."),
 ("Noah","He counts fast. He counts like a man who expects to be poor.")))
take_stock("Each realia province takes its four pieces out of the box. They wait beside the board, off the map, until they're sold.", TH(
 ("Silke","Four Dragon Jars beside my seat and not one of them on a square. Off the board, Rob can't touch them."),
 ("Graham","Four Vases. Five pieces I need, four of every type in existence, and five of us wanting each one. Somebody's always going to be one short.")))
act("The cut-outs are made at the suggested sizes: Clark cuts the Province 2 Irrigation System one square by two, Rich the Province 3 Reservoir two by three, Graham the Province 7 Reservoir two by two.", TH(
 ("Rich","Two by three. The biggest piece of paper in the box. A cut-out's a public work, so every time a soldier steps on it Rob pays me five. I'm making it exactly the size it says and not one square less."),
 ("Clark","One by two. Mine's the smallest and it pays the least. Story of the Official."),
 ("Graham","Two by two, and I cut it out myself. I'd like it on the board before the paper curls.")), map_hl=[2,3,7])
act("Noah, the Scholar, shuffles the twenty I Ching cards and lays them face down. Nobody looks.", TH(
 ("Noah","I hold the clock. Five population cards in twenty. I shall read them in my most reassuring voice."),
 ("Rob","He's going to read the doubling card like it's good news. I'd have read it like a weather warning. We each get the Scholar we deserve.")))
place_army({"W1":"F14", "W2":"E19", "W3":"M16", "W4":"T18"},
 "Rob stands his four soldiers on undeveloped land: F14 under the Wall, above Province 2; E19, a step from the throne room; M16, in the notch beside Province 3; and T18, under the wheat and rice fields.", TH(
 ("Rob","One soldier for each kind of target. F14 looks at the Official's province. E19 looks at Province 1, where every raid is ten. M16 sits in the notch, next to Rich's fields and two steps from the door into Province 4. T18 is on Graham's doorstep, and Paddy's."),
 ("Silke","He's left the gap at O18 empty, and he could have stood one in the sea off my coast and didn't. The nearest he has is T18, five steps from my province. He's coming the long way, or he's coming last."),
 ("Reina","Two of the four are aimed at the upper class. He's worked out that the rich pay better.")))
say("Rob","I'll tell you where they're going, every year, before they go. Nothing in my booklet says I can't.", TH(
 ("Rob","Honest to a fault. It's my whole personality and I'm not putting it down for a booklet. A Warlord who announces his raids is still a Warlord. He's just a punctual one."),
 ("Paddy","He's going to tell us exactly where he's robbing us and we still won't be able to stop him. That's not honesty, that's a threat with good manners."),
 ("Silke","Oh, I like him.")))

# ============================== YEAR 1 ==============================
R(1, "The compact", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
rents()
say("Reina","Thirty per cent. Low, because the compact is going to ask you for more than tax.", TH(
 ("Reina","Thirty is fine. Thirty plus a share of every ditch is the real number, and everybody knows it."),
 ("Clark","I collect it. Honestly. My booklet says I'm corruptible, and I'm choosing to read that as 'available'.")))
taxes(.30, collector="Clark collects the tax")
act("Rob declines to pay tax.", TH(
 ("Rob","I looked. Twice. The Warlord's booklet never mentions tax. If it did, I'd pay it."),
 ("Reina","He'd pay it. He'd actually pay it. I believe him, and it doesn't help.")), map_hl=[8])
build("Province 7 Reservoir", 60, {1:60}, key="res7", at="R17:S18", hover=TH(
 ("Graham","R17 to S18, the south-east corner of my province, right under his soldier on T18. A cut-out is a public work. Every time he steps onto it, he pays me five to cross. It's a toll gate."),
 ("Reina","Sixty out of the crown. The booklet says the crown pays the lot for this one, and this time the crown does."),
 ("Rob","He's put it where my soldier would walk in. I'll walk in anyway. I'll just pay for the privilege.")))
say("Graham","Thank you, Majesty.", TH(
 ("Graham","Two words, and I've never meant two words more. Twenty a year from next year, in the province with the worst land on the board."),
 ("Reina","Ten years late. You're welcome.")))
lot(2,"CH",[
 B(6,4), B(3,5),
 B(6,6,None,"Six. Rice farmer's money. I need one of everything and I'd like to start cheap."),
 B(3,7,"Seven.", TH(
   ("Rich","Seven, and I collected rent from him ten minutes ago. Landlords outbid tenants. That's not cruelty, it's cash flow."),
   ("Paddy","There are three more. I'll be patient. I've never been patient in my life, but I'll try it.")))],
 at="K14", hover="Rich puts it on K14, in the middle of Province 3, two rows from the notch and five columns from the desert.")
lot(3,"LD",[
 B(4,5),
 B(5,6,None,"Six. I'm Silk. I need a Scroll and I can bid early, before everyone works out they're scarce."),
 B(4,8,"Eight.", TH(
   ("Noah","Eight. I'm the Scholar now — worst income at the table, five a year from the crown and whatever the weather sends. I'm buying while I can still afford to be seen buying."),
   ("Silke","He outbid me by two on a Scroll. Two's nothing.")))],
 at="K21", hover="Noah puts it on K21, the centre of Province 4. Province 4 only touches the desert at its south-west corner, on the far side from here.")
lot(4,"BB",[
 B(7,4), B(2,6,"Six.","Six. The Official needs a Brush and the Official collects everyone's tax. I'm the richest bidder in year one by a long way.")],
 at="H14", hover="Clark puts it on H14, in the middle of Province 2. J14 would be two rows further from his soldier on F14, but it's on the south edge, against the notch side of Province 3.")
lot(5,"DJ",[
 B(3,5), B(7,7,"Seven.", TH(
   ("Graham","Seven for a Jar. Silke's the seller, and I'm happy to buy from her."),
   ("Silke","I get a quarter. One and a half. My first honest money of the night.")))],
 at="Q14", hover="Graham puts it on Q14, at the far end of Province 7 from his soldier at T18. Four squares from him, which in Province 7 is a long way.")
lot(6,"WB",[
 B(4,4), B(5,6,"Six.","Six. One Bowl. Paddy's selling, and I'll be friendly with Paddy, because Paddy's rice fields sit between my silk and the desert.")],
 at="O25", hover="Silke puts it on O25, in the top corner of Province 5, by the sea, seven steps from his nearest soldier on T18.")
lot(7,"VA",[
 B(2,5), B(6,7,"Seven.", TH(
   ("Paddy","Seven for a Vase. He ran the auction like a sale at a vicarage."),
   ("Graham","I'm the seller. I get one and a half. I used to get the whole tax take. I'm enjoying this more than I did then.")))],
 at="R22", hover="Paddy puts it on R22, the middle row of Province 6. T row under him is desert all the way along; the middle is the furthest he can get.")
say("Rob","This year: G14 in Province 2, F19 in Province 1, L16 in Province 3, and S18, which is Graham's reservoir. I'll pay for crossing it.", TH(
 ("Rob","Four raids, announced. I'm not bluffing. I'm reading you the itinerary."),
 ("Clark","He named the square. He named my square. I put my Brush on H14 and he's going to stand on G14 and look at it."),
 ("Graham","He's walking onto my reservoir to raid me, and paying me five to do it. I make nothing and he makes nothing. It's the most polite raid in history.")))
march({"W1":"G14", "W2":"F19", "W3":"L16", "W4":"S18"}, "Rob's soldiers step in exactly where he said: G14, F19, L16 and S18.", TH(
 ("Rob","Five, ten, five, five — and five back to Graham for treading on his reservoir. Twenty net. I said I'd pay and I paid."),
 ("Rich","L16. He's one square from the edge of my province and two from my Customs House."),
 ("Reina","Ten from me in year one. Every one of these is a square of the throne room he can never raid again. I'm choosing to see it as fencing.")))
salaries()

# ============================== YEAR 2 ==============================
R(2, "Fortune and misfortune", "goodevil")
say("Noah","Good harvest for all. And Provinces 2, 4, 6 and 8 play a personal disaster — Clark, me, Paddy and Rob.", TH(
 ("Noah","I read my own disaster in my most reassuring voice. It didn't help."),
 ("Rob","Mine's the legs. I know it's the legs. It's always the legs.")))
harvest()
rents()
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Clark","Four for a pension. I'm just going to pay it."),
 ("Paddy","He's pre-empting my joke. That's very Official of him.")))
disaster(4,"he falls asleep over his notes on the migratory habits of the swallow, and the candle takes them.", TH(
 ("Noah","Four million and a year of research I never did. I was going to write about swallows. Now I'll have to write about candles."),
 ("Rob","A man wrote a book about swallows and a candle read it first.")))
disaster(6,"the only water buffalo breaks its leg in the middle of planting.", TH(
 ("Paddy","My buffalo. Of course it's my buffalo."),
 ("Rich","I'd like it known that it was never my buffalo's fault.")))
disaster(8,"wounded in the legs in the last battle. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Rob","Called it. The legs. So the southern soldier stands still, and the other three keep walking north."),
 ("Graham","A year off. My Jar sits there with nobody walking toward it.")))
taxes(.40, collector="Clark collects the tax")
say("Reina","The compact. The Winter Palace this year, so the canals can start. Twenty, and it's mine to pay.", TH(
 ("Reina","A palace I don't want, because the booklet says no canal in 4, 5 or 6 until it stands. Every palace on my list is a key, not a house."),
 ("Silke","She's building a key to my canal. I'll take a palace for that.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="H22", hover=TH(
 ("Reina","H22, three steps from his soldier on F19. I could put it further, but every step further is another square of my province he raids at ten on the way. Three steps is a price I can see."),
 ("Rob","Three squares. Twenty from Reina on the way and twenty when I arrive. I'll put it on the itinerary.")))
lot(2,"CH",[
 B(7,6), B(5,8,"Eight.", TH(
   ("Silke","Eight. Customs House, two of five. I need a Scroll still, and a Brush, and a Vase."),
   ("Graham","He got the jump on me. There are two more.")))],
 at="O26", hover="Silke puts it on O26, next to her Bowl, in the corner of Province 5 by the sea.")
lot(3,"LD",[
 B(7,6,"Six.","Six for a Scroll. Two of five, and nobody fought me, because they're all watching the Vases.")],
 at="P14", hover="Graham puts it on P14, beside his Jar on the west side of Province 7, away from the soldier at S18.")
lot(4,"BB",[
 B(6,5), B(5,7,"Seven.","Seven. Three of five. I need a Scroll and a Vase now, and the Scrolls are going.")],
 at="P25", hover="Silke puts it on P25. Everything she owns is now in the far corner of Province 5, three squares wide.")
lot(5,"DJ",[
 B(3,6), B(4,8,"Eight.", TH(
   ("Noah","Eight. Two of five. Four Jars in the world and five of us who need one. Somebody's going to be short, and I'd rather it wasn't the Scholar."),
   ("Rich","I'll take the next one. There's always a next one, until there isn't.")))],
 at="L21", hover="Noah puts it on L21, beside his Scroll, in the middle of Province 4.")
lot(6,"WB",[
 B(2,5), B(7,6,"Six.", TH(
   ("Graham","Six for a Bowl. Three of five: Jar, Scroll, Bowl. Customs House and Brush to go."),
   ("Clark","I'll let him have it. I'm being polite, and I can get a Bowl next year.")))],
 at="Q13", hover="Graham puts it on Q13, the west edge, beside his Scroll and Jar. Three pieces in a cluster, five squares from the soldier at S18.")
lot(7,"VA",[
 B(5,6), B(3,8,"Eight.","Eight, and I collect rent on the seller. It's like buying from yourself with extra steps.")],
 at="K12", hover="Rich puts it on K12, two squares west of his Customs House, in the thick of Province 3 where the notch soldier has to walk past both.")
say("Rob","This year: H15 in Province 2, G20 in Province 1, K16 in Province 3. The southern soldier's legs are bad, so it waits.", TH(
 ("Rob","Three raids, announced. And H15 is next to Clark's Brush on H14. I'm not taking it yet. I'm making him look at it."),
 ("Clark","He's next to my Brush. He's going to take it next year and tell me first.")))
march({"W1":"H15", "W2":"G20", "W3":"K16"}, "Rob's northern soldiers step in: H15, G20, K16. The southern one waits at S18.", TH(
 ("Rob","Five, ten, five. G20 is two steps from the palace."),
 ("Rich","K16 is two squares from my Customs House on K14. He's walking along my fields like a man on a pavement.")))
sell_soldiers([(2,"H13")], "Clark buys a soldier from Rob and stands it on H13, beside his Brush.", TH(
 ("Clark","Twenty to the man walking toward my Brush. Province 2 has been raided, so it can move. It's on the other side of my Brush from his soldier on H15, two squares off, so he can't reach it. If he steps onto my Brush, he's straight beside it, and I take him."),
 ("Rob","Clever. I keep five of it. He's paid me five to make my next raid harder."),
 ("Silke","That's the move. Never stand straight beside him. Stand where he wants to go.")))
salaries()


# ============================== YEAR 3 ==============================
R(3, "Rain and flood", "rainflood")
say("Noah","Good harvest for Provinces 1, 3, 6 and 7. The rivers flood in 2, 4, 5 and 8.", TH(
 ("Noah","Bad for me, bad for Clark, bad for Silke and bad for Rob. Good for the Emperor, the landlord, Paddy and Graham. I read it as if it were fair."),
 ("Silke","Province 5 floods. The far corner of the board, and the river finds it anyway.")))
harvest()
rents()
taxes(.40, collector="Clark collects the tax")
say("Clark","My irrigation, Majesty. Thirty. I'll pay half.", TH(
 ("Clark","Fifteen down, ten a year, forever. It should be built in year one of every game."),
 ("Paddy","He's quoting me. Nobody's ever quoted me approvingly before. I'm going to be insufferable.")))
build("Province 2 Irrigation System", 30, {1:15,2:15}, key="irr2", at="I15:J15", hover=TH(
 ("Clark","I15 and J15, straight under his soldier on H15. If he wants to walk south through my province, he walks across my irrigation and pays me five a step."),
 ("Rob","He's paved my road with tolls. I respect a man who monetises a ditch."),
 ("Reina","Fifteen from the crown, fifteen from the Official. That's how the compact's meant to look.")))
lot(2,"CH",[
 B(6,8), B(7,10,"Ten.", TH(
   ("Graham","Ten. Four of five. A Brush and I'm done — and I'll be done in Province 7, beside a reservoir somebody else finally built, climbing out of it."),
   ("Paddy","He's racing me for the same chairs.")))],
 at="P13", hover="Graham puts it on P13, the far west of Province 7, beside his other pieces and five squares from the soldier on S18.")
lot(3,"LD",[
 B(2,7), B(5,9,"Nine.","Nine. Four of five, and the last one's a Vase. Graham's selling Vases. Graham owes me nothing and I've been charming to him for an hour.")],
 at="P26", hover="Silke puts it on P26, in her corner by the sea, eight steps from his nearest soldier on S18, whether he comes through the gap at O18 or round by the coast.")
lot(4,"BB",[
 B(6,6,"Six.","Six for a Brush. Two of five. I'm slow, but I'm cheap.")],
 at="R21", hover="Paddy puts it on R21, beside his Vase, in the middle row of Province 6.")
lot(5,"DJ",[
 B(2,7), B(3,9,"Nine.", TH(
   ("Rich","Nine. Three of five. I need a Brush and a Bowl, and the Brushes are going to a rice farmer for six."),
   ("Clark","I need a Jar too. Seven was what I could spare with a pension to pay and a Bowl and a Vase still to buy. There are more Jars to come.")))],
 at="K13", hover="Rich puts it on K13, between his Vase and his Customs House. He's building a row.")
lot(6,"WB",[
 B(3,6), B(2,8,"Eight.","Eight. Two of five. I'm buying where Rich's bidding, because Rich has rent and I have a pension to pay.")],
 at="I13", hover="Clark puts it on I13, directly below his own soldier on H13 and well away from Rob's.")
lot(7,"VA",[
 B(5,7), B(2,9,"Nine.", TH(
   ("Clark","Nine. Three of five. A Scroll and a Jar, and I'm out of the Official's chair and into something with fewer pensions."),
   ("Silke","He took my Vase. There are two more. I'm being patient. Patience is new."))),
 B(5,None,"There's two more.","Two more Vases in Graham's stock, and only Noah and I still want one after this. I can wait a year.")],
 at="I12", hover="Clark puts it on I12, the west edge of Province 2, beside his Bowl.")
say("Rob","This year: I16 in Province 2, H21 in Province 1, K15 in Province 3, and R17 — Graham's reservoir. I'll pay him for it.", TH(
 ("Rob","Announced. I16 goes round Clark's irrigation instead of across it; I'm honest, not stupid. K15 is one step from Rich's Customs House. And every square next to my southern soldier is either Paddy's or Graham's paper, so paper it is."),
 ("Rich","One step. He's told me he's one step from my Customs House next year."),
 ("Graham","Three from my Jar, and he pays me five to stand on my own reservoir while he does it. I've four pieces and that's the one I'd have to buy back from him.")))
march({"W1":"I16", "W2":"H21", "W3":"K15", "W4":"R17"}, "Rob's soldiers step in: I16, H21, K15 and R17.", TH(
 ("Rob","Five, ten, five, five, less five to Graham for the reservoir. H21 is one step from the Winter Palace."),
 ("Reina","Next year he raids my palace and tells me first."),
 ("Clark","I16 is one square from my irrigation. He's going round it. A ditch that works by being avoided is still working.")))
say("Reina","Twenty for the palace raid. Forty for two soldiers to stop it. He can have the palace.", TH(
 ("Reina","A palace is a key, not a house. It unlocked the canals the day it was built. If he raids it I pay twenty once, and nothing it unlocked comes undone."),
 ("Rob","She's done the arithmetic and it says I get a palace. I'd have said the same.")))
say("Rich","Twenty for a soldier? He takes five off me for a raid. I'll take the five and put the rent up.", TH(
 ("Rich","My booklet says greedy, and greedy says twenty is four raids. The Customs House cost me seven. I'm gambling he wants grain more than pottery."),
 ("Silke","She's gambling against a man who just told her which square he's standing next to. Don't."),
 ("Rob","He's right that I'd rather have grain. He's wrong about which I'd rather have from him.")))
sell_soldiers([(7,"Q15")], "Graham buys a soldier from Rob and stands it on Q15.", TH(
 ("Graham","Q15, beside my Jar, two squares from his soldier. Every way into my Jar runs straight past my soldier. It's the first soldier I've ever bought that's defending something I own."),
 ("Rob","Another soldier sold. Five for me. My itinerary is the best advertising in the game.")))
salaries()

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
say("Noah","Population increases by one half. Good harvest for everyone. A hundred and fifty million people.", TH(
 ("Noah","Consumption up by half, forever. Mine goes from forty to sixty. A Scholar's harvest doesn't move."),
 ("Rob","One of five. I'd count them out loud, but I'm the Warlord tonight. Somebody else has to.")))
harvest()
rents()
taxes(.50, collector="Clark collects the tax")
say("Reina","The canals. All six sections in Provinces 4, 5 and 6, this year, in one go. Two hundred and forty. My booklet says the crown pays for 5 and 6. Province 4's share is the one I'm allowed to ask about. Noah — forty?", TH(
 ("Reina","Ten a section a year, forever, into the three provinces with the most mouths to feed. If the population's going up, the ditches have to go in before it does. Two hundred from the crown is the biggest cheque of the evening, and the booklet wrote it, not me."),
 ("Noah","Forty from the Scholar, the worst income at the table, for the one canal the booklet lets her charge for. Twenty a year from next year. I'll pay it, and I'll say thank you, and I'll mean about half of it."),
 ("Silke","The crown pays for mine. It says so in her booklet. I'd have offered forty and she knows it. She didn't take it. She's honest about the booklet.")))
build("Grand Canal — 2 sections each in Provinces 4, 5 and 6", 240, {1:200,4:40}, canal={4:2,5:2,6:2})
say("Clark","Minuted: the crown two hundred, Noah forty. Nobody protesting, which is a first.", TH(
 ("Clark","I'm keeping the minutes of the compact on the back of my booklet. Every split, every name. If anyone revolts later, they'll have to argue with the minutes."),
 ("Paddy","A public work in my province and I paid nothing for it. I'd like it noted that I'm suspicious.")))
lot(2,"CH",[
 B(4,9), B(6,10,"Ten.", TH(
   ("Paddy","Ten. Three of five. A Scroll and a Jar to go."),
   ("Noah","He outbid me for the last Customs House. I need one. I'll get one when somebody climbs and hands theirs back.")))],
 at="Q22", hover="Paddy puts it on Q22, the top row of Province 6, as far from the desert under him as it goes.")
lot(3,"LD",[
 B(2,8,"Eight.","Eight. Four of five: Scroll, Brush, Bowl and Vase. One Jar, and there's one Jar left, in Silke's stock, with Paddy wanting it too.")],
 at="H12", hover="Clark puts it on H12, the north-west corner, with his other pieces on the west side away from his soldiers.")
lot(4,"BB",[
 B(6,6), B(7,8,"Eight.", TH(
   ("Graham","Eight. Five of five. I'm complete in year four, with my own reservoir paying me twenty. I'm not moving yet. I want the right chair."),
   ("Reina","He's complete. He's looking at the Official. Clark is looking back at him from inside it.")))],
 at="Q16", hover="Graham puts it on Q16, beside his soldier on Q15 and the reservoir. It's the most defended square in Province 7.")
lot(5,"DJ",[
 B(2,6,"Six.","Six. The last Jar, and it would finish me."),
 B(6,8,"Eight.","Eight. Four of five. A Scroll and I'm done."),
 B(2,10,"Ten.","Ten. That's a fifth of what I've got."),
 B(6,14,"Fourteen.", TH(
   ("Paddy","Fourteen. The crown just paid for my canal, so I've got forty I wasn't expecting to have, and I'm spending it on the one piece Clark needs. There are no Scrolls left in the stock. Someone has to climb and hand one back."),
   ("Clark","The crown paid for his canal and he's using the change to outbid me."))),
 B(2,None,"Have it.","Fourteen for a Jar, with a pension and the Wall coming, and Province 2's share of the Wall is going to be mine. I'll get one when somebody climbs and hands theirs back.")],
 at="R20", hover="Paddy puts it on R20, beside his Brush.")
lot(6,"WB",[
 B(3,7), B(4,9,"Nine.", TH(
   ("Noah","Nine. Three of five. I need a Customs House and a Vase, and the Customs Houses are gone. I'm the Scholar; I can read the shape of this. Somebody climbs, things come back, and I wait."),
   ("Rich","I needed that Bowl. I'm two short now.")))],
 at="L20", hover="Noah puts it on L20, with his Scroll and Jar in the middle of Province 4.")
lot(7,"VA",[
 B(4,8), B(5,10,"Ten.", TH(
   ("Silke","Ten. Five of five. I'm complete, in a province his soldiers have never set foot in, and nobody's ever raided me."),
   ("Noah","Out. A Customs House and a Vase short, and the stock's empty.")))],
 at="N25", hover="Silke puts it on N25, completing the corner: five pieces on five squares, six to eight steps from his nearest soldier, the one on H21 walking to the Winter Palace.")
act("The last realia are sold. Every province's stock is empty.", TH(
 ("Noah","Board check. Graham and Silke are complete. Clark needs a Jar. Paddy needs a Scroll. Rich needs a Brush and a Bowl. I need a Customs House and a Vase. Every piece we're missing is sitting in a completed set."),
 ("Paddy","So the only way the rest of us finish is if the two who are done climb, and hand back what they don't need. Their climbing is our auction.")), map_hl=[2,3,4,5,6,7])
say("Rob","This year: the Winter Palace on H22. I17 in Province 1, across the river — that's five back to Reina. K14, which is Rich's Customs House. And R16 in Province 7.", TH(
 ("Rob","Twenty for the palace from Reina, and the Customs House from Rich, the first piece of my objective. Both announced twelve months ago. Nobody can say they weren't told."),
 ("Graham","R16 is at an angle from my soldier, so he's safe there, and my Brush on Q16 is straight beside it. If he steps onto the Brush, he's straight beside my soldier too. My soldier is working by being looked at."),
 ("Rich","I said grain. I was wrong. Silke told me I was wrong and I said it anyway.")))
march({"W2":"H22", "W1":"I17", "W3":"K14", "W4":"R16"}, "Rob's soldiers step in: the Winter Palace on H22, I17, Rich's Customs House on K14, and R16.", TH(
 ("Rob","One of my six. One different piece from every other player who holds realia, so not the crown and not the palaces. I've told you that too. The Customs House goes on M5, in the desert, where anyone who wants it can come and ask."),
 ("Reina","Twenty for the palace and ten for I17, less five for his toll. I'd budgeted for exactly this."),
 ("Rich","My Customs House. Three of five down to two of five, and he told me a year ago. Greedy is a terrible strategy when the other man is honest.")), take={"W3":("CH","M5")})
salaries()


# ============================== YEAR 5 ==============================
R(5, "Shared increase", "share")
say("Noah","Average harvest. And every province with a public work shares the increase with the Emperor, half and half.", TH(
 ("Noah","Five provinces with a ditch now. I read it out and watched three peasants, an Official and myself do the same sum: half of every bonus, straight back to the crown."),
 ("Reina","The compact pays twice. Once in the harvest, once on this card. I didn't plan it. I'll take it.")))
harvest()
rents()
act("Each province with a public work pays the Emperor half its increase: 5 from Clark, 10 each from Noah, Silke, Paddy and Graham.", TH(
 ("Paddy","The crown paid for my canal, and half its first year's yield goes straight back to the crown. Minute that, Clark."),
 ("Clark","Minuted. 'Paddy: nothing in, twenty out, ten back.' It reads better than he'd like."),
 ("Reina","Forty-five to the crown. Every bag of it goes back into the next work. That's the compact.")),
 {pid(2):-5, pid(4):-10, pid(5):-10, pid(6):-10, pid(7):-10, pid(1):45}, map_hl=[1,2,4,5,6,7])
taxes(.50, collector="Clark collects the tax")
say("Reina","The Summer Palace this year. It's the key to the Wall and my own canal.", TH(
 ("Reina","The cheapest project left. Twenty, from the crown. Nobody has to vote on a palace that's only a padlock."),
 ("Rob","She'll put it as far from my soldier as she can. I'll walk there. She knows I'll walk there.")))
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="G26", hover=TH(
 ("Reina","G26, the far corner of Province 1, against the sea. Four squares from his soldier on H22. He'll raid me three times at ten on the way and take twenty at the end. I'd rather that than lose it next year — and in four years it won't matter."),
 ("Rob","Three squares at ten and twenty at the end. Fifty from the crown, and not a piece of it toward my objective. Grain's grain. She's priced it. So have I.")))
swap(7,3,"Graham Garner declares a complete set and replaces Richard Baron. Graham becomes Gentry of Province 3; Rich becomes Wheat Peasant of Province 7.", TH(
 ("Graham","Hand back the Scroll — it's native to Province 3 — keep the rest, and take every bag Rich's holding. I've been the Emperor, a wheat farmer and an Official. Banker is the only chair left I haven't been thrown out of."),
 ("Rich","He took my Customs House last year and now he's taken my chair. I went from landlord to wheat in one sentence. And I get his reservoir, which Reina built him, which nobody built me."),
 ("Reina","The woman who never built that reservoir has climbed out from beside it. The man who's inherited it is the landlord who wouldn't buy a soldier.")),
 at={"CH":"H9", "BB":"H10", "DJ":"I8", "WB":"I9"})
say("Graham","H9, H10, I8, I9. The west end of Province 3, against the desert.", TH(
 ("Graham","Every soldier he has is east of the north river, and the nearest is four squares from here. The desert's empty. I'm putting my furniture where his army isn't, not where the map says is deep."),
 ("Rob","He's right. All four of mine are east. I'd have to walk back across Province 3 to reach him, raiding Graham all the way, and telling him first."),
 ("Silke","Deep is relative. Deep is how far the nearest soldier is.")))
say("Clark","Minuted: Graham, Gentry. Rich, wheat. The compact transfers with the chair.", TH(
 ("Clark","Whoever holds Province 3 pays Province 3's share. I wrote it that way on purpose, on the first page, in year one."),
 ("Rich","I'm being held to a compact by a footnote I didn't read.")))
lot(3,"LD",[
 B(7,5,"Five.","Five. I'm a wheat farmer with nothing. A Scroll's a start."),
 B(6,8,"Eight.", TH(
   ("Paddy","Eight for the Scroll Graham handed back. Five of five. I'm complete — in Province 6, in year five — and I'd like everyone to remember I started this game with a buffalo."),
   ("Rich","Out. He's got the crown's canal money. I've got a reservoir I didn't ask for.")))],
 at="Q23", hover="Paddy puts it on Q23, the top row of Province 6, next to his Customs House and away from the desert under the rice fields.")
lot(5,"DJ",[
 B(7,6), B(2,9,"Nine.", TH(
   ("Clark","Nine for the Jar Rich handed back. Five of five. I'm the Official, I'm complete, and my booklet says that when I'm complete I may declare myself Emperor."),
   ("Reina","He's complete. He can take my seat. He's looking at the minutes.")))],
 at="G12", hover="Clark puts it on G12, the north-west corner of Province 2, beside his Scroll.")
say("Clark","I'm complete, Majesty. The booklet says I can have your chair.", TH(
 ("Clark","I can. Five pieces and the grain. I've read the clause twice. And the minutes on the back of my booklet say the man in that chair has paid more into the compact than the rest of us put together."),
 ("Reina","If he declares, I hand him the treasury and he finishes the list, or he doesn't. I can't stop him. I'm not going to try. I'm going to let him decide in front of everybody."),
 ("Paddy","This is the most interesting thing that's happened all night and nobody's even rolled anything.")))
say("Clark","Not yet. Finish it first.", TH(
 ("Clark","I'm not giving it up. I'm putting it off. If he finishes the list, the game ends and I've held. If he stops, I take the chair and finish it myself. Either way the country gets its Wall."),
 ("Rob","He's turned the throne into a guarantee. The Emperor's working for him now."),
 ("Reina","I've been threatened before. Never this politely.")))
lot(7,"VA",[
 B(4,7,"Seven.", TH(
   ("Noah","Seven for the Vase Rich handed back. Four of five. One Customs House and I'm done, and there won't be one until someone climbs."),
   ("Silke","I've got a Customs House. I'm complete, and I'm sitting on the piece he needs.")))],
 at="M22", hover="Noah puts it on M22, beside the canal in Province 4.")
say("Silke","I'm complete too. Not this year.", TH(
 ("Silke","If I climb, my pieces leave a corner he's never walked toward for Province 4, and Rob's first soldier is walking toward Province 4. I'll see which way he turns before I move my furniture into his path."),
 ("Noah","She's complete, she's looking at my chair, and she's waiting to see where the Warlord goes first. I'm the Scholar. I'm the one person at the table being politely queued for.")))
say("Rob","This year: J18 in Province 3. H23 in Province 1. K13, toward the new Gentry. Q17 in Province 7.", TH(
 ("Rob","J18 is the odd corner of Province 3 by the river, which costs me five to cross and pays Graham five for the raid — he's even. H23 is the first of my four steps to the Summer Palace. K13 starts the long walk west."),
 ("Graham","He's announced a four-year walk to my furniture, one square at a time. I have four years to think of something."),
 ("Rich","Q17. Province 7. My province now. He's raiding me before I've unpacked.")))
march({"W1":"J18", "W2":"H23", "W3":"K13", "W4":"Q17"}, "Rob's soldiers step in: J18, H23, K13 and Q17.", TH(
 ("Rob","Graham twice, Reina once, Rich once. And five to Graham for the river."),
 ("Reina","Ten. Three squares to go."),
 ("Rich","Five, on my first year as a wheat farmer. And Graham's soldier is still standing on Q15 in my province, guarding nothing, and it isn't mine.")))
salaries()

# ============================== YEAR 6 ==============================
R(6, "Heaven has favourites", "heaven")
say("Noah","Good harvest for Provinces 2, 4 and 5. Bad for 1, 3, 6, 7 and 8.", TH(
 ("Noah","Good for me. For once, good for me. I'll be reading this card to myself later."),
 ("Silke","Good for Province 5, and his soldier turned toward Province 4 anyway. I've waited a year. I'm taking the chair.")))
harvest()
rents()
taxes(.50, collector="Clark collects the tax")
say("Reina","The Province 3 Reservoir. Eighty. Forty from the crown, forty from the Gentry.", TH(
 ("Reina","Half for the province that gets twenty a year forever. It's the right split."),
 ("Graham","When I was Emperor, Noah paid half of this and I paid the other half. Now I'm the Gentry, paying Noah's half. The board has a long memory.")))
build("Province 3 Reservoir", 80, {1:40,3:40}, key="res3", at="K16:L18", hover=TH(
 ("Graham","K16 to L18, two rows by three, against the notch. Two of those squares are already raided, so they can't be raided again, and every step onto the paper costs his soldiers five. If he comes in through the notch he comes in across water."),
 ("Rob","He's built his reservoir as a turnstile. Six squares of toll right where I'd walk in. It's the most expensive piece of paper on the board."),
 ("Clark","Minuted: the crown forty, Graham forty.")))
swap(5,4,"Silke Weber declares a complete set and replaces Noah Tall. Silke becomes Scholar of Province 4; Noah becomes Silk Peasant of Province 5.", TH(
 ("Silke","Hand back the Brush, keep the rest, take every bag Noah has. Silk farmer to the woman who reads the I Ching. I'll read it like a weather warning."),
 ("Noah","I bought a Vase for seven last year. It's going straight back into the box, and the Customs House I needed is coming with the man who's taking my chair."),
 ("Rob","She's taken the clock off Noah.")),
 at={"CH":"K23", "LD":"K24", "WB":"L23", "VA":"M23"})
act("The pieces Silke and Noah handed back go up for auction: a Brush from Silke, a Jar from Noah, a Bowl from Paddy, a Vase from Rich. Nobody bids.", TH(
 ("Noah","I've been the Silk Peasant for ninety seconds and I own nothing. I'm not buying pottery until I know which chair I'll be sitting in next year."),
 ("Rich","Nobody's bidding, so next year they'll be cheaper. I'm a wheat farmer. I can wait for cheaper."),
 ("Graham","The Vase would make me a complete Gentry. I've no use for that. I'll let it sit.")), map_hl=[4,5,6,7])
say("Silke","K23, K24, L23 and M23. The east side of Province 4, against the sea.", TH(
 ("Silke","His soldier on J18 is five squares from here, and the one on H23 is busy walking to Reina's palace. I know exactly how he thinks: I'd go for the furniture in the middle. So it isn't in the middle."),
 ("Rob","He's not wrong. I was going for the middle.")))
say("Rob","This year: K19 in Province 4. G24 in Province 1. J12 — no, that's Clark's, and his soldier's watching it. L13, in Province 3. And Q18.", TH(
 ("Rob","K19 opens Province 4 for Silke. G24 is the second step to the palace. L13 keeps walking west toward Graham. Q18 is next to the rice fields, where Paddy keeps five pieces in a row like a shop window."),
 ("Paddy","He's described my province as a shop window. In front of everybody."),
 ("Silke","K19. Five from me on my first year in the chair. Of course it is.")))
march({"W1":"K19", "W2":"G24", "W3":"L13", "W4":"Q18"}, "Rob's soldiers step in: K19, G24, L13 and Q18.", TH(
 ("Rob","Silke, Reina, Graham, Rich. Two squares from the Summer Palace."),
 ("Reina","Two more. I've stopped flinching at ten."),
 ("Rich","Q18. That's two raids on me in two years, and my booklet says I'm simple and hard-working. I'm working very hard at being robbed.")))
sell_soldiers([(6,"R21")], "Paddy buys a soldier from Rob and stands it on R21, on his Brush.", TH(
 ("Paddy","R21, on my Brush, between my Jar and my Vase. His soldier on Q18 has to come through Q19 or R19 to reach the rice fields. Twenty to a man who told me where he'd be. I'm paying him for the information."),
 ("Rob","Five for me. I'd like to thank Paddy for his custom. He's still not getting a discount.")))
salaries()


# ============================== YEAR 7 ==============================
R(7, "The public utility tax", "utility")
say("Silke","Average harvest. Two million from every province to the Emperor, and two more from every province with a public work.", TH(
 ("Silke","My first card as Scholar. I read it like a weather warning, as promised. Every province but the throne has a public work now. That's twenty-six to Reina for building them."),
 ("Reina","The card says I decreed it. I'd like it minuted that I didn't, and that I'm keeping it.")))
harvest()
rents()
act("Public Utility Tax: 2 from every province, and 2 more from each of Provinces 2 to 7, which all have public works.", TH(
 ("Clark","Minuted: twenty-six to the crown. Nobody's adding it to a list of grievances."),
 ("Rich","Four from me for a reservoir I didn't pay for, didn't place and didn't want to stand next to.")),
 {pid(2):-4, pid(3):-4, pid(4):-4, pid(5):-4, pid(6):-4, pid(7):-4, pid(8):-2, pid(1):26}, map_hl=list(range(1,9)))
taxes(.50, collector="Clark collects the tax")
say("Reina","The Wall. Six links, two above each of Provinces 1, 2 and 3. Two hundred and forty. I'll pay half. Clark and Graham pay sixty each.", TH(
 ("Reina","The one work on the list that feeds nobody, and it's the biggest. I'm building it after every ditch, with the people under it paying for it."),
 ("Clark","Sixty for two links that raise nothing. I'll pay it. The minutes say I would."),
 ("Graham","I spent nine years on this wall once, and it fed nobody. Sixty is a bargain for watching somebody else do it right.")))
build("Great Wall — 6 links, two above each of Provinces 1, 2 and 3", 240, {1:120,2:60,3:60}, wall={1:2,2:2,3:2})
say("Clark","Minuted: the crown a hundred and twenty, Clark sixty, Graham sixty. Half the Wall.", TH(
 ("Clark","Six of twelve. The minutes are three pages now. Nobody's argued with a single line."),
 ("Paddy","Nobody's argued because nobody under the Wall is a peasant. I'd like to see these minutes when it's a peasant's turn to pay for something useless.")))
swap(6,5,"Paddy Doyle declares a complete set and replaces Noah Tall. Paddy becomes Silk Peasant of Province 5; Noah becomes Rice Peasant of Province 6.", TH(
 ("Paddy","Hand back the Jar, keep the rest, take every bag Noah has. Rice to silk."),
 ("Noah","Scholar at seven o'clock, Silk Peasant at eight, Rice Peasant at nine. I've fallen two provinces in two years without ever being raided."),
 ("Silke","He's taken my old seat. The corner up by Province 4, five steps from his nearest soldiers. I was never raided in that province. He might be.")),
 at={"CH":"L24", "LD":"L25", "BB":"M24", "VA":"M25"})
say("Paddy","L24, L25, M24, M25. The top corner of Province 5.", TH(
 ("Paddy","Province 4 is between Rob's soldier on K19 and this corner, and Silke's in it, and Silke is the most suspicious woman I've ever met. The one on G24 could come down the coast, but it's been walking to the Summer Palace since the day Reina built it, and it's two steps off."),
 ("Silke","He's using me as his back door. I'm flattered. I'm also charging him nothing, which is new.")))
lot(3,"LD",[
 B(7,4,"Four.", TH(
   ("Rich","Four for the Scroll. Start again. I need one of everything except a Vase, and I've got one Scroll and sixty million."),
   ("Graham","I'm the seller. I get a quarter. I used to be the Gentry buying these for nine.")))],
 at="P15", hover="Rich puts it on P15, beside Graham's old soldier on Q15. It isn't his soldier, but it stands next to his Scroll, and Rob doesn't know whose side it's on.")
act("Silke puts up the Brush she handed back, Paddy the Jars, Noah the Bowl, Rich the Vase. Nobody bids.", TH(
 ("Noah","Nobody poor has the years, and nobody rich wants what a fifth piece would mean. Three to go. The set I'd need would take five."),
 ("Graham","The Vase would complete me as Gentry. A complete Gentry has one move left, and it's the throne. I'm not running for it. The compact's finishing the list."),
 ("Silke","A Jar would complete me as Scholar, and the only chair above the Scholar is Reina's. Tonight I'd rather watch her earn it."),
 ("Paddy","A Bowl and I'm complete again, and every chair I could climb into belongs to someone whose name is in the minutes. I've been the man who climbs over people. Tonight I'm in the minutes."),
 ("Rich","I'd buy the Jar for two. I'm not bidding two in front of all of you. I've got some dignity left, and it's the only thing I own.")), map_hl=[4,5,6,7])
say("Rob","This year: K20 in Province 4. G25 in Province 1. K12 in Province 3. Q19 in Province 6.", TH(
 ("Rob","K20 is one step nearer Silke's furniture. G25 is the third step to the Summer Palace. K12 is Graham's, on the way west. And Q19 is Noah's new province, which has nothing in it to take but five million."),
 ("Silke","He's coming for my corner. I know what I'd do from K20. I'd go through the middle."),
 ("Noah","Five. I've been in this province for six minutes.")))
march({"W1":"K20", "W2":"G25", "W3":"K12", "W4":"Q19"}, "Rob's soldiers step in: K20, G25, K12 and Q19.", TH(
 ("Rob","Silke, Reina, Graham, Noah. One square from the Summer Palace."),
 ("Reina","One square. I said I'd let him. I've let him four times."),
 ("Paddy","Q19. That's Province 6 raided. My soldier on R21 can move now. It's mine, it's standing in Noah's province, and there's nothing of mine left in it.")))
sell_soldiers([(4,"K22")], "Silke buys a soldier from Rob and stands it on K22.", TH(
 ("Silke","K22. Two squares from his soldier on K20, and between him and my four pieces. If he comes along row K he's straight beside it. It's very strange paying the man I'm defending against."),
 ("Rob","Five for me. She haggled. I didn't let her.")))
troops({"Paddy1":"Q22"}, "Paddy's soldier starts north from R21 toward Province 5: one square, to Q22.", TH(
 ("Paddy","Province 6 has been raided, so it can move. It's going to walk to my corner in Province 5. It'll take four years. There are three left. I'm doing it anyway."),
 ("Noah","There's a soldier walking out of my province that belongs to the man who just took my grain. It's the most Paddy thing I've ever seen.")))
salaries()

# ============================== YEAR 8 ==============================
R(8, "The population doubles", "double1")
say("Silke","The population doubles. Good harvest for everyone. Three hundred million people, and every province eats twice what it did.", TH(
 ("Silke","A hundred and twenty a year for a peasant to eat, against a harvest of a hundred and whatever the ditch adds. Every peasant with a ditch lands on zero. The crown eats a hundred and eighty."),
 ("Reina","A hundred and eighty, against a harvest of a hundred, and no canal of my own yet. Minus eighty a year until something changes."),
 ("Noah","Zero, on a good harvest. Nobody pays tax on zero. Clark is about to collect nothing from a whole country.")))
harvest()
rents()
taxes(.50, collector="Clark collects the tax")
say("Clark","Fifty per cent of nothing, Majesty. Not a bag. The only positive income on the board is nobody's.", TH(
 ("Clark","I wrote it in the minutes as a zero and then underlined it. Six years of collecting and the doubling took the whole tax base in one card."),
 ("Reina","The Wall was going to be this year. Two hundred and forty. Not on minus eighty a year it isn't.")))
say("Graham","Majesty. Section 13. The population's doubled. New land is open.", TH(
 ("Graham","Twenty a square from the Harvest Pile, twenty a year from every square, forever. It's the only income in the book that grows with the people. And there's no limit on how many you buy."),
 ("Rich","Twenty a year for twenty once. It pays for itself in a year. Why has nobody said this before?"),
 ("Noah","Because until this card nobody was allowed to. The booklet makes you wait until the crisis has started. It's started.")))
say("Reina","Then the compact grows a page. Every square anyone buys, the crown pays a quarter. The Pagoda this year, the Wall when the land has paid for it, and my canal last.", TH(
 ("Reina","The booklet says the cost must be shared with the Emperor. Five a square from the crown, fifteen from the province. And the tax takes its share of the harvest the land brings in, so the crown gets its five back by next year."),
 ("Clark","Minuted: the land compact. Five a square from the crown, fifteen from the province, no limit. Provinces 2 and 3 can't join until the Wall above them is finished. That's me."),
 ("Graham","And me. Four links above Province 3 before I can touch the strip under the Wall. Two are built.")))
say("Reina","No system this year, so the booklet says the Marble Pagoda. Twenty.", TH(
 ("Reina","My canal is eighty for twenty a year. Eighty of land is eighty a year. The canal can wait for the last year; the Pagoda is the cheapest way to keep the booklet happy while the land goes in."),
 ("Clark","Minuted: the Marble Pagoda, the crown, twenty. The building that does nothing, built in the year everything else is land.")))
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="F17", hover=TH(
 ("Reina","F17, the north-west corner of Province 1, the one square of the throne room his soldiers have never walked toward."),
 ("Rob","She's right. I'd have walked there eventually. I'd have told her first."),
 ("","Reina pays the 20.")))
buy_land(1, ["F23", "F24", "F25", "F26", "H25"], {1:100}, "New land: Reina buys five squares of sea for Province 1, along the coast at F23 to F26 and H25.", TH(
 ("Reina","A hundred, all from the crown, because it's the crown's own land. A hundred a year from next year: the throne room stops starving. The strip under the Wall stays shut to me until my own four links stand, and two are built. So, the sea. His soldier on G25 is one step from four of these. He can raid each square once, at ten. Each one pays twenty a year for ever."),
 ("Rob","The sea, right beside my soldier. Ten a square when I step on one, and she keeps the harvest. She's done the sum before I could.")))
buy_land(4, ["K25", "J25", "K26"], {4:45, 1:15}, "New land: Silke buys three squares of sea for Province 4, at K25, J25 and K26, the crown paying 15.", TH(
 ("Silke","Forty-five from me. The sea's as open to his soldiers as the desert, and the nearest is three steps up the coast on G25. But that one's going to Reina's palace, and from there a raid on me is five a square. Sixty a year from next year."),
 ("Rob","She's bought land beside the road I'm walking. I'll remember it's there.")))
buy_land(5, ["M26", "N26", "O27"], {5:45, 1:15}, "New land: Paddy buys three squares of sea for Province 5, at M26, N26 and O27, the crown paying 15.", TH(
 ("Paddy","Forty-five. My corner of the province gets a coast. Sixty a year, and his nearest soldier's six steps off."),
 ("Clark","Minuted. Paddy: three squares, forty-five in, sixty a year back. It reads better than he'd like.")))
buy_land(6, ["Q26", "R25"], {6:30, 1:10}, "New land: Noah buys two squares of sea for Province 6, at Q26 and R25, the crown paying 10.", TH(
 ("Noah","Thirty is most of what I've got. Two squares, forty a year. The arithmetic is the only thing in this game that's ever been on my side, and it finally is."),
 ("Rich","Noah's bought the sea with his last thirty. I'm about to do something stupider.")))
buy_land(7, ["Q12", "R12"], {7:30, 1:10}, "New land: Rich buys two squares of the Warlord's desert for Province 7, at Q12 and R12, the crown paying 10.", TH(
 ("Rich","Province 7 has no sea. The only land I can develop is his. Two squares of the desert, thirty from me, forty a year, and both of them standing in his own country."),
 ("Rob","He's farming my desert. I'd like to announce now, a year ahead as always, that I'll be visiting it."),
 ("Graham","He's built a wheat field in the Warlord's front garden. It's the bravest thing anybody's done tonight.")))
lot(4,"BB",[
 B(7,3,"Three.","Three for a Brush. Two of five. It's not going to happen, but it's three, and I'd rather lose with pottery than without it.")],
 at="P16", hover="Rich puts it on P16, next to his Scroll, on the other side of Graham's soldier.")
act("Paddy puts up the Jars, Noah the Bowl, Rich the Vase. Nobody bids.", TH(
 ("Paddy","My lot. My pottery. Nobody wants it. Everybody's buying land."),
 ("Silke","The Jar finishes me, and finishing me means asking for the throne. Not tonight."),
 ("Graham","I'm the banker. Bankers don't need Vases.")), map_hl=[5,6,7])
say("Rob","This year: the Summer Palace on G26. L21 in Province 4. J12 in Province 2. And P20, into Province 5.", TH(
 ("Rob","G26 doesn't count toward my objective; no palace does. It's twenty from Reina, after thirty on the way, and I said I'd go there three years ago. I'm going. The new land waits until next year: I announce first."),
 ("Reina","He's walked four squares to raid a palace that's no use to his objective, because it's fifty from the crown door to door and because he said he would. Twenty for his word. I've paid worse."),
 ("Silke","L21 goes round my soldier. At an angle. He's learned the dance.")))
march({"W2":"G26", "W1":"L21", "W3":"J12", "W4":"P20"}, "Rob's soldiers step in: the Summer Palace on G26, L21, J12 and P20.", TH(
 ("Rob","Twenty, five, five, five. I went round Paddy's canal, not across it. I'm honest; I'm not generous."),
 ("Clark","J12. Straight beside my Vase and two from my soldier. And five more out of a purse that was nearly empty."),
 ("Paddy","P20. Into my province through the front door, four squares from my corner. My soldier's still walking.")))
say("Silke","Four cards left in the deck that make the Warlord play a disaster, out of thirteen. And his next disaster is the wedding.", TH(
 ("Silke","His first disaster is the legs, and he had that in year two. His second is the wedding: no raids at all, for a year. If he can't raid, he can't capture onto a square that hasn't been raided."),
 ("Rob","She's reading my booklet back to me. From memory."),
 ("Reina","Four in thirteen. Worse than one in three. She's going to bet on it.")))
sell_soldiers([(4,"K21")], "Silke buys a second soldier and stands it on K21, straight above Rob's soldier on L21.", TH(
 ("Silke","Straight beside him. If he can raid next year, he takes it, and I've given him five and a soldier. If he draws a wedding, he can't step onto K21 or L22 without raiding, and he can't stay where he is."),
 ("Rob","She's offering me a soldier. That's either a gift or a trap, and with Silke it has never once been a gift.")))
troops({"Silke1":"L22", "Paddy1":"P23"}, "Silke's first soldier steps to L22, beside Rob's on L21. Paddy's soldier steps to P23.", TH(
 ("Silke","L22 and K21. Both straight beside him, both on squares nobody's raided. Every way out of L21 is either a raid or straight beside one of mine."),
 ("Paddy","P23, across the rice fields' border into my province. Three squares from the soldier on P20. I'm not doing anything clever with it. It's walking home."),
 ("Clark","Silke's put two soldiers next to his and dared him. It's the most Silke thing I've ever seen.")))
salaries()


# ============================== YEAR 9 ==============================
R(9, "Storms and raiders", "repairs")
say("Silke","Good harvest for all. Provinces 4, 5, 6 and 7 pay two each for repairs to their public works. And Provinces 1, 2, 3 and 8 play a personal disaster.", TH(
 ("Silke","Eight. Province 8 plays a disaster. I read it slowly. I've waited a year to read it slowly."),
 ("Rob","The wedding. It's the wedding. She bet four in thirteen and she won."),
 ("Reina","Province 1 plays one too. Mine's the horse. It's always the horse.")))
harvest(hover_extra=[{"w":"Silke","t":"The land's first year. Province 4: a hundred, twenty from the canal and sixty from the sea, against a hundred and twenty to eat. Sixty to the good. Last year it was zero."}])
rents()
act("Repairs: Provinces 4, 5, 6 and 7 each pay 2 to the Harvest Pile.", "Storms and raiders, according to the card. Every one of them has a public work to repair now.",
    {pid(4):-2, pid(5):-2, pid(6):-2, pid(7):-2}, map_hl=[4,5,6,7], pile_delta=8)
disaster(1,"the Arabian horse throws her. The trainer is lashed twenty times.", TH(
 ("Reina","Four. It's always the horse."),
 ("Graham","Twenty lashes for the trainer. He's having a worse evening than any of us.")))
disaster(2,"the imperial barge rams a lock gate on the new canal during his inspection. He pays for the damage rather than lose face.", TH(
 ("Clark","Ten. Six sections of canal in this country and I rammed a gate on one of them."),
 ("Paddy","At least it's a real lock. Progress.")))
disaster(3,"the head chef retires after forty years and is promised a house and a pension.", TH(
 ("Graham","Five for a chef. I started this game in the wheat fields and now I have a household staff. The disasters get more comfortable as you climb."),
 ("Rich","That was my chef. I hired him.")))
disaster(8,"a trusted lieutenant runs off with his daughter. No raids this year — he's too busy feasting the newlyweds.", TH(
 ("Rob","No raids. So my soldier on L21 can't step onto any square nobody's raided, and every square he could reach that has been raided is straight beside one of Silke's. He can stay, or he can step beside a soldier. Either way Silke takes him. And Rich's desert farm gets a year's grace."),
 ("Rich","A year's grace for the wheat in the desert. I'll take it.")))
taxes(.50, collector="Clark collects the tax")
say("Clark","A hundred to the crown, Majesty. Every bag of it grown on land that didn't exist last year.", TH(
 ("Clark","Silke thirty, Paddy thirty, Noah twenty, Rich twenty. The four provinces that bought land are the only four with an income. Last year this line was a zero."),
 ("Reina","The land paid the tax, and the tax pays for the Wall. That's the whole compact in one line.")))
say("Reina","The rest of the Wall. Six links, two hundred and forty. Eighty from the crown, a hundred from Graham, thirty each from Silke and Paddy.", TH(
 ("Reina","The last big number. After this it's only my canal."),
 ("Graham","A hundred. The last two links above Province 3 are the only thing between me and the strip under the Wall, and I've got two hundred and twenty-eight. I'd have paid more.")))
build("Great Wall — the last 6 links, two above each of Provinces 1, 2 and 3", 240, {1:80,3:100,4:30,5:30}, wall={1:2,2:2,3:2})
say("Clark","Minuted, with a star: the Great Wall, all twelve links. This year: the crown eighty, Graham a hundred, Silke thirty, Paddy thirty.", TH(
 ("Clark","Four hundred and eighty, split by the people it protects and the people the land made rich enough to pay."),
 ("Noah","Twelve links. The Wall I said would never be finished, finished by wheat in the desert and rice in the sea.")))
buy_land(3, ["G9", "G10", "G11"], {3:45, 1:15}, "New land: with the Wall above Province 3 finished, Graham buys three squares of the strip below it, G9, G10 and G11, the crown paying 15.", TH(
 ("Graham","The Wall's done, so the strip is mine to farm. Forty-five, and sixty a year from next year. I've waited since last year's card."),
 ("Rob","The strip below the Wall, right by my western soldier's road. I'll announce it next year.")))
say("Clark","I can't, Majesty. Nine and a half. The fifteen is more than I have.", TH(
 ("Clark","The Wall above Province 2 is finished, so the strip is open to me at last, and I'm the one person at the table who can't afford my share. The doubling put the Official at minus ten a year and a barge took ten more."),
 ("Reina","The Official, locked out of the land by the Wall and then by his own purse. I'd lend it to him if the compact let me.")))
act("Paddy puts up the Jars, Noah the Bowl, Rich the Vase. Nobody bids.", TH(
 ("Paddy","Still not buying the Bowl. One year left. A set I'd never use is just furniture with a grudge."),
 ("Rich","I'm two of five. I'd need a Jar, a Bowl and a Customs House, and the Customs House is in Rob's desert. I'd also need about four more years."),), map_hl=[5,6,7])
act("Rob's soldiers stand where they are. The wedding keeps every one of them out of an unraided square.", TH(
 ("Rob","W1 stays on L21. If I step to K20 I'm straight beside Silke's soldier on K21, and every other square is a raid I'm not allowed. Staying is the honest way to lose him."),
 ("Silke","He announced it. He announced his own capture. I'd have hidden behind the wedding cake.")), map_hl=[8])
troops({"Silke1":"L21"}, "Silke's soldier steps from L22 onto L21 and captures one of Rob's soldiers.", TH(
 ("Silke","Captured, straight across. I'd like that carved on something."),
 ("Rob","Three left. She bet on my booklet and won. I'd like everyone to know she played it honestly. She told us the odds out loud."),
 ("Reina","Two soldiers bought from the Warlord, and one of his taken with them.")))
salaries()

# ============================== YEAR 10 ==============================
R(10, "The last of the list", "winds")
say("Silke","Steady weather. Neither feast nor famine: an average harvest.", TH(
 ("Silke","Average, at three times the people. Every peasant with new land is above water. Clark has none, and he isn't."),
 ("Reina","Three doubling cards were in the deck, and one came. We built on it instead of starving on it. That's the trick.")))
sell_back(2, ["LD", "BB", "DJ", "WB", "VA"], "Clark sells his whole set back to the Harvest Pile: Scroll, Brush, Jar, Bowl and Vase, for 2 each.", TH(
 ("Clark","Minus thirty-five on the harvest, and fourteen and a half in hand. The rule says sell before I sink. Five pieces at two each: the whole set, and I still end ten and a half in debt."),
 ("Reina","The complete set, the one that could have had my chair any year since the fifth, gone to the bank for ten. He never declared, and now he can't."),
 ("Rich","Ten million for a complete set. The pile has never had a better day.")))
harvest()
rents()
say("Reina","Sixty per cent this year. It's the last year, and my canal is the last work.", TH(
 ("Reina","Nineteen in the reserve after the harvest, and the canal is eighty. Sixty per cent of what the land brings in is just enough."),
 ("Clark","Sixty. The first time she's gone above fifty. Minuted, without a star: it's the year the list ends.")))
taxes(.60, collector="Clark collects the tax")
say("Reina","My canal. Two sections in Province 1. Eighty, from the crown.", TH(
 ("Reina","The last work on the list, and the only one that pays me back. I built it tenth because land paid better."),
 ("Clark","Minuted, last line: the Grand Canal in Province 1, the crown, eighty.")))
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
assert all_built(), "not every public work is built"
act("Every public work the country owes is standing: three palaces, twelve links of the Great Wall, eight sections of the Grand Canal, the irrigation system and the two reservoirs. The game ends: the players have survived, and the Emperor's reign has been a glorious one.", TH(
 ("Reina","Ten years. The reservoir first, then every ditch, then the land when the doubling came, the Wall out of what the land brought in, and my own canal last. A thousand and thirty million, and the minutes say who paid every bag."),
 ("Clark","Four pages now. The land compact got a page of its own."),
 ("Rob","One piece of six, told a year ahead, and twenty for each palace I walked to. The honest Warlord announces his way out of the throne. I'd do it again.")), map_hl=list(range(1,9)), big=True)
say("Clark","For the record, I never declared.", TH(
 ("Clark","Complete since year five, and the throne one sentence away. I waited for the list to be finished. Then the doubling took my income, the Wall above me kept me off the land until there was nothing left to buy it with, and this morning I sold the set back to the pile for ten. I've held. The Official's only way up was the throne, and I spent it on a guarantee."),
 ("Reina","He could have had it in year five, six or seven. He waited for the list instead. I'd like that minuted too.")))
say("Graham","Build the reservoir, Reina.", TH(
 ("Graham","It's what I'd have said in year one if she hadn't done it before I asked."),
 ("Reina","Already built.")))

RESULT = export(
 "Every public work was built, so this is the first ending: the players survived and the Emperor's reign was a glorious one. Players are still ranked by the province they finished in against the one they drew.",
 ["Reina kept the throne and finished the list in ten years — which by Section 18 is a win for the Emperor. The compact did it: one work a year, the split agreed before the card was turned, and the people who used each work paying into it.",
  "When the population doubled in year eight and every income fell to zero or below, the table bought new land: the crown paid a quarter of every square, the provinces the rest, and the harvest from the strip under the Wall, the sea and the Warlord's desert paid the tax that finished the Wall.",
  "Three players climbed. Graham rose from the wheat fields to the Gentry, Silke from silk to the Scholar's chair, and Paddy from rice to silk. Clark completed his set in year five and chose not to take the throne. Noah fell two provinces without ever being raided, and Rich fell from landlord to wheat farmer the year after he decided a soldier wasn't worth twenty.",
  "Rob announced every raid a year ahead and got one of the six pieces he needed, though his long walks through the throne room to both palaces paid him well. The players used his honesty to buy soldiers where he said he'd be, and in year nine Silke captured one of his soldiers during the Warlord's wedding."])
