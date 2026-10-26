# Game 6 — All's Quiet on the Western Front. Seven players, no Warlord, ten years.
setup([1,2,3,4,5,6,7], "quiet", "All's Quiet on the Western Front",
      "Seven players · ten years · no Warlord",
      "Seven players and no Warlord: no raids, no soldiers, and nobody in the desert. Everything is fought over with grain instead: rents, retainers and minimum bids. The Emperor pays a man every year to keep one Dragon Jar off the market, the population doubles, the peasants farm the Warlord's empty land, and a silk farmer climbs twice to the throne.",
      short="7 players · 10 years")

# ============================== SETUP ==============================
R(0, "Seven at the table", None, "Seven players: all seven provinces and no Warlord (rulebook Section 4, Note 2 and Appendix A). Every province holds four pieces of its own realia, and each player must collect one piece of every type but their own, plus 20 million in hand. With no raids and no soldiers this is the pure economic game. Every public work in the book is owed: three palaces, twelve links of Wall, eight canal sections, the irrigation system and the two reservoirs, 1,030 million in all.")
act("Robert Land can't come tonight, so seven sit down. Seven booklets, shuffled and drawn face down: Reina draws the Emperor, Clark the Official, Rich the Gentry, Noah the Scholar, Silke the Silk Peasant, Paddy the Rice Peasant and Graham the Wheat Peasant.", TH(
 ("Reina","The throne. Every other booklet has a page on how to replace me, and tonight there's nobody in the desert for me to point at while they read it."),
 ("Graham","Wheat. Province 7 touches the desert on three sides, and the desert is empty. I've never had a quieter border."),
 ("Clark","The Official. 'Seeks bribes.' I'll need someone to bribe me. There are six candidates and I like all of them.")), map_hl=[1,2,3,4,5,6,7])
act("The Warlord's booklet goes back in the box, with the sixteen soldiers and the forty pink raid squares. Seven players is the one game with no Warlord in it (Note 2).", TH(
 ("Noah","One of the six causes for revolt just went with him. 'Cannot control the Warlord' needs a Warlord. That leaves five, and the new one, debt."),
 ("Paddy","Nobody raids. Nobody sells soldiers. My booklet tells me soldiers are my only defence, and there's nothing to buy and nothing to defend against."),
 ("Silke","No soldiers means the only weapon at this table is grain. I like my chances.")))
say("Reina","So nobody at this table gets to blame the desert. Whatever goes wrong in this country, one of us did it.", TH(
 ("Reina","Including me. Especially me. The Emperor's mistakes all have her name on them, and tonight there's no Warlord to share the credit."),
 ("Rich","She's saying it first so it sounds like leadership. It's also true.")))
act("Rich, the Gentry, sets out the Harvest Pile where everyone can see it: twenty-five hundred million in bags of eight sizes.", TH(
 ("Rich","I bank the pile and I collect the rent. In a game with no Warlord, the man with the money is the most dangerous person at the table, and that's me."),
 ("Graham","He counted it twice. He'll count ours more often.")), map_hl=[3])
deal_grain("Rich deals 60 to each of the seven players from the Harvest Pile. That's the first year's harvest.", TH(
 ("Rich","Four hundred and twenty out before anyone's moved."),
 ("Paddy","Sixty. The booklet says a good harvest is a hundred and my family eats forty. So I'm doing well. Am I doing well?")))
take_stock("Each of the six realia provinces takes its four pieces out of the box. They wait beside the board until they're sold.", TH(
 ("Noah","Twenty-four pieces. Each of us six needs five, one of every kind but our own: thirty wants and twenty-four pieces. Six of those wants go unmet at any moment, and then somebody climbs, and the pieces come back, and it starts again."),
 ("Silke","Four Dragon Jars beside my seat. Every upper-class set needs a Jar, and I'm the only peasant whose set doesn't. I'm going to enjoy selling these.")))
act("Clark cuts the Province 2 Irrigation System out of paper at one square by two, Rich the Province 3 Reservoir at two by three, and Graham the Province 7 Reservoir at two by two. They're set aside until they're built.", TH(
 ("Graham","Two by two, and the crown pays for all of it. My booklet says so. I'll be reading that sentence aloud at intervals."),
 ("Rich","Two by three. The biggest bit of paper in the box. With no soldiers to charge for crossing it, it's just a very large ditch. I'll take it."),
 ("Clark","One by two. The cheapest work on the list, which means it's the first one built.")), map_hl=[2,3,7])
act("Noah, the Scholar, shuffles the twenty I Ching cards and lays them face down. Nobody looks; the first card is turned in Year 2.", TH(
 ("Noah","Five of the twenty raise the population: three double it and two add half. The deck stops counting at six hundred million. With no Warlord, those five cards are the only enemy we've got."),
 ("Reina","The Scholar holds the clock. Tonight the clock is the villain.")), map_hl=[4])
say("Reina","The list is a thousand and thirty. The works that grow food first, then the palaces they need, and the Wall last.", TH(
 ("Reina","The ditches pay back every year: the irrigation, the reservoirs, the canals. The Wall feeds nobody until the population doubles and the land under it opens. If the Wall's last, the crown never pays for a wall it doesn't need yet."),
 ("Clark","She's announced the order of the list. I'm writing it down. When she changes it, I'll read it back to her."),
 ("Graham","'The works that grow food first.' My reservoir grows food. I'm writing that down too.")))

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
rents(hover=TH(
 ("Rich","Five from each of the three. Fifteen a year for owning the land they stand on. The booklet says 'at least five'. At least."),
 ("Silke","He said 'at least' to himself. I heard him.")))
say("Reina","Thirty per cent. Low, because I want you to remember I started low.", TH(
 ("Reina","A hundred and eight to the crown on a first harvest of sixty each. Enough for the cheapest ditch and the salaries."),
 ("Clark","I collect it. I collect it honestly, because there's nothing to skim yet. Ask me again when there is.")))
taxes(.30, collector="Clark collects the tax")
say("Reina","The Province 2 irrigation system. Thirty, and ten a year back. Clark, half?", TH(
 ("Reina","The cheapest work in the book that grows anything. The Official pays half, so it costs the crown fifteen."),
 ("Clark","Fifteen from me for ten a year forever. I'd be a fool to haggle. I'm going to haggle anyway, for the minutes."),
 ("Graham","The crown's first ditch, and it's the Official's. Mine costs sixty and the crown pays all of it. I can see why it's not first.")))
say("Clark","Half, Majesty. Minuted: the first work, the Official's, half and half.")
build("Province 2 Irrigation System", 30, {1:15,2:15}, key="irr2", at="I14:I15", hover=TH(
 ("Clark","I14 and I15, down the middle of Province 2. There's nobody coming to cross it, so it goes where it waters the most squares."),
 ("Reina","Fifteen from the crown, fifteen from the Official. A thousand to go.")))
lot(2,"CH",[
 B(5,4), B(3,7,"Seven.", TH(
   ("Rich","Seven, in the first lot of the game. Landlords buy early. The rent paid for it."),
   ("Silke","He bought it with my five. I'll remember which five.")))],
 at="K12", hover="Rich puts it on K12, in the middle of Province 3, where he can see it from his chair.")
lot(3,"LD",[
 B(7,4), B(2,6,"Six.", TH(
   ("Clark","Six for a Scroll from the man who banks the pile. I'll want a receipt."),
   ("Graham","Four was my number. I'll get one later. There are three more.")))],
 at="H13", hover="Clark puts it on H13, beside the irrigation he's just paid half for.")
lot(4,"BB",[
 B(7,5,"Five.","Five for a Brush. The first piece of my five, and nobody fought me for it.")],
 at="Q15", hover="Graham puts it on Q15, in the middle of the wheat. There's nobody on the border to hide it from, so it goes where he'd put a vase of flowers.")
lot(5,"DJ",[
 B(6,5,"Five.", TH(
   ("Paddy","Five for a Jar. I need one of everything except Bowls, and I'm starting with the one Silke's selling."),
   ("Silke","A quarter of five is one. My first honest money.")))],
 at="R21", hover="Paddy puts it on R21, the middle of the rice fields.")
lot(6,"WB",[
 B(5,5,"Five.","Five. Paddy's selling and Paddy's my neighbour. We'll be buying from each other all night.")],
 at="P24", hover="Silke puts it on P24, in the silk farms by the sea: out of habit, as far from the desert as Province 5 goes.")
lot(7,"VA",[
 B(3,5,"Five.","Five for a Vase. I'll get a better price later; there are three more."),
 B(4,6,"Six.","Six. I'm the Scholar, the worst-paid upper-class seat at the table, and I'm buying the thing Rich is waiting to buy cheaper.")],
 at="K21", hover="Noah puts it on K21, the middle of Province 4.")
salaries()

# ============================== YEAR 2 ==============================
R(2, "Steady weather", "winds")
say("Noah","Steady weather. Neither feast nor famine. Nobody writes poems about years like this. An average harvest for everyone.", TH(
 ("Noah","Nineteen cards left, and all five population cards still in them."),
 ("Graham","Average, and quiet. Thirty-five each after we eat. The desert's very quiet.")))
harvest()
rents(hover="Five each. A Gentry who forgets the rent isn't playing the game, and this one hasn't forgotten.")
taxes(.40, collector="Clark collects the tax")
say("Graham","Majesty. The Province 7 Reservoir. Sixty, and your booklet says the crown pays all of it.", TH(
 ("Graham","Every year, the same sentence, until it's a revolt clause. 'Delayed too long in building public works.' Mine is the one work she pays for alone, so every year it doesn't exist is her decision and nobody else's."),
 ("Reina","He's right that it's mine. He's going to be right every year."),
 ("Rich","There's no Warlord for her to blame. There's just Graham, reading out her booklet.")))
say("Reina","Year five, Graham. The Winter Palace this year, so the canals can start; then the canals, then you.", TH(
 ("Reina","The canals feed three provinces and the palace is their key. The reservoir feeds one. That's the order of the list, and I said it out loud on the first night."),
 ("Graham","Year five. I'm counting from today."),
 ("Clark","Minuted: 'Year five, Graham.' I underlined the five.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="H21", hover=TH(
 ("Reina","H21, in the middle of the throne room. A palace is a key, not a house; it opens the canals in 4, 5 and 6. With nobody to raid it, I can put it where it looks well from the window."),
 ("","Reina pays the 20.")))
lot(2,"CH",[
 B(6,5), B(5,7,"Seven.","Seven. Two of five, and they're both from neighbours.")],
 at="P25", hover="Silke puts it on P25, beside her Bowl by the sea.")
lot(3,"LD",[
 B(7,5), B(4,7,"Seven.", TH(
   ("Noah","Seven. Two of five, a Vase and a Scroll."),
   ("Graham","Five was mine. That's two Scrolls gone.")))],
 at="L21", hover="Noah puts it on L21, under his Vase.")
lot(4,"BB",[
 B(3,7,"Seven.","Seven for a Brush. Two of five: a Customs House and a Brush.")],
 at="L12", hover="Rich puts it on L12, under his Customs House.")
lot(5,"DJ",[
 B(7,6,"Six.", TH(
   ("Graham","Six. Two of five, a Brush and a Jar."),
   ("Silke","Six for a Jar. I'll put the price up when the upper class starts wanting them.")))],
 at="Q16", hover="Graham puts it on Q16, next to his Brush, near where the reservoir is going to go if it ever comes.")
lot(6,"WB",[
 B(2,7,"Seven.","Seven for a Bowl. Two of five, a Scroll and a Bowl. I'm the Official; I can afford to buy what I need when I need it.")],
 at="H12", hover="Clark puts it on H12, next to his Scroll.")
lot(7,"VA",[
 B(3,6,"Six.","Six. The second Vase, and nobody's bidding against me but people who need it more."),
 B(6,7,"Seven.", TH(
   ("Paddy","Seven. Two of five, a Jar and a Vase."),
   ("Rich","Again by one. I'll have the third.")))],
 at="R22", hover="Paddy puts it on R22, next to his Jar.")
salaries()

# ============================== YEAR 3 ==============================
R(3, "Fortune and misfortune", "goodevil")
say("Noah","Good harvest for everyone. And Provinces 2, 4, 6 and 8 play a personal disaster. That's Clark, me, Paddy, and Province 8, which is nobody.", TH(
 ("Noah","A card that names an empty province skips it. Province 8 is just sand tonight."),
 ("Paddy","It's my buffalo. I know it's my buffalo.")))
harvest()
say("Rich","Friends. Eight a year, from now on. And my last two Scrolls open at two, for anyone who'll pay it.", TH(
 ("Rich","'May negotiate to raise the rent at any time.' All three of them need a Scroll, and I'm the only man who sells them. So the price of a cheap opening is three a year of rent. That's not greed, it's a trade, and I'll keep my end of it to the letter."),
 ("Silke","Three a year, for the right to bid two on a Scroll that somebody else will outbid me for. I'll take it. I need the Scroll more than he needs the three."),
 ("Graham","I need a Scroll. I'll pay the eight. He knows I'll pay the eight.")))
say("Paddy","Eight. Fine. You'll ask me again next year, and I'll still say fine.")
rents(8, note="Rents: each peasant pays the Gentry 8, as agreed.", hover=TH(
 ("Rich","Twenty-four a year instead of fifteen. Minuted, I assume."),
 ("Clark","Minuted: the Gentry's rent, eight, and his last two Scrolls opening at two. I don't pay rent. I just enjoy the paperwork.")))
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Clark","Four for a pension. There's no army to inspect tonight, and the chariot still found a tree."),
 ("Reina","The garrisons are empty and the Official still has a disaster about them.")))
disaster(4,"he falls asleep over his notes on the migratory habits of the swallow, and the candle takes them.",
 "Noah: Four million. I was going to write about swallows. Now I'll write about candles.")
disaster(6,"the only water buffalo breaks its leg in the middle of planting.", TH(
 ("Paddy","I said it was the buffalo."),
 ("Graham","Four for a buffalo, in the year his rent went up three. Write that down, Clark.")))
taxes(.40, collector="Clark collects the tax")
say("Reina","The Province 3 Reservoir. Eighty. Rich, forty?", TH(
 ("Reina","Twenty a year back for the Gentry, and he can afford half: rent, a good harvest and nothing much to buy."),
 ("Rich","Forty, Majesty, and gladly. A reservoir on my own land, half paid by the crown. I'll fawn about it later; I'm counting now."),
 ("Graham","Eighty for the landlord's reservoir in year three. Mine's sixty and it's year five. I'm not saying anything. I'm counting.")))
build("Province 3 Reservoir", 80, {1:40,3:40}, key="res3", at="K16:L18", hover=TH(
 ("Rich","K16 to L18, two rows by three, on the east side of Province 3. Six squares of paper. With nobody to charge for walking across it, it's an ornament that grows food."),
 ("Clark","Minuted: the crown forty, the Gentry forty. Third work.")))
lot(2,"CH",[
 B(7,5), B(6,8,"Eight.","Eight. Three of five: Jar, Vase, Customs House. A Scroll and a Brush to go.")],
 at="R20", hover="Paddy puts it on R20, beside his Jar.")
lot(3,"LD",[
 B(7,6,"Six.","Six. He said two and he kept his word: the Scroll opened at two. Then Silke bid."),
 B(5,8,"Eight.", TH(
   ("Silke","Eight. Three of five. The cheap opening was for all of us, not just Graham."),
   ("Graham","The third Scroll, and I'm paying eight a year in rent for the right to lose it. One left.")))],
 at="O25", hover="Silke puts it on O25, in the corner of Province 5 by the sea, beside the rest.")
lot(4,"BB",[
 B(2,8,"Eight.","Eight. Three of five: Scroll, Bowl, Brush.")],
 at="G13", hover="Clark puts it on G13, at the top of Province 2, by the strip under the Wall.")
lot(5,"DJ",[
 B(2,7), B(3,9,"Nine.", TH(
   ("Rich","Nine for the Jar. Three of five. Every upper-class set needs one and there are only four, so they'll get dearer."),
   ("Clark","Seven was my number. There's one more Jar in Silke's stock. I'll have that one.")))],
 at="K11", hover="Rich puts it on K11, beside his Customs House and Brush in the middle of Province 3.")
lot(6,"WB",[
 B(7,8,"Eight.","Eight. Three of five, and I'm the only one still short of a Customs House and a Scroll.")],
 at="P15", hover="Graham puts it on P15, next to his Brush and Jar: three pieces in a row in the middle of the wheat.")
lot(7,"VA",[
 B(3,8,"Eight.","Eight for the third Vase. I said I'd have the third."),
 B(2,9,"Nine.", TH(
   ("Clark","Nine. Four of five. A Jar and I'm complete, and the last Jar's in Silke's stock."),
   ("Rich","By one again. Three Vases, and I've lost every one of them by a single million. One left.")))],
 at="H15", hover="Clark puts it on H15, beside the irrigation.")
salaries()

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
say("Noah","Population grows by half. Good harvest for everyone. A hundred and fifty million people.", TH(
 ("Noah","Consumption up by half, forever: forty to sixty for every province but the crown's, which goes from sixty to ninety. Seventeen cards left, four population cards still in them, and one of those is the other half card, which won't count."),
 ("Silke","Forty a year on a good harvest instead of sixty. With rent at eight.")))
harvest()
rents(8)
taxes(.50, collector="Clark collects the tax")
say("Reina","The canals. All six sections in Provinces 4, 5 and 6, this year. Two hundred and forty. The crown pays for 5 and 6; Noah, forty for yours?", TH(
 ("Reina","Ten a section a year into the three provinces with the most mouths. The people grew this morning; the ditches have to go in now. Two hundred from the crown, because the booklet says so for 5 and 6."),
 ("Noah","Forty, the Scholar's share, for twenty a year. I'll pay it and I'll mean it."),
 ("Graham","The canals, year four. The palace was year two. Year five is next year. I'm still counting.")))
build("Grand Canal — 2 sections each in Provinces 4, 5 and 6", 240, {1:200,4:40}, canal={4:2,5:2,6:2}, hover=TH(
 ("Clark","Minuted: the crown two hundred, the Scholar forty. Six hundred and sixty of the thousand and thirty left."),
 ("Paddy","A canal in my province, and I paid nothing for it. I'd like it noted that I'm grateful and suspicious.")))
lot(2,"CH",[
 B(7,6), B(4,8,"Eight.", TH(
   ("Noah","Eight. Three of five, and a Jar next."),
   ("Graham","Six was mine. The last Customs House. I'm short of a Customs House and a Scroll, and the stock's nearly gone.")))],
 at="M21", hover="Noah puts it on M21, at the bottom of Province 4 by the canal.")
lot(3,"LD",[
 B(7,7,"Seven.","Seven for the last Scroll. He opened it at two, as promised."),
 B(6,9,"Nine.", TH(
   ("Paddy","Nine. Four of five. A Brush and I'm done."),
   ("Graham","Four Scrolls, and I've bid on all four, and I've paid eight in rent since last year for the privilege. I'm not complaining. I'm keeping count.")))],
 at="R19", hover="Paddy puts it on R19, the top row of the rice fields.")
lot(4,"BB",[
 B(6,6), B(5,10,"Ten.","Ten. Four of five. A Vase and I'm complete."),
 B(6,None,"Out.","Ten's too dear for a Brush. There'll be another when somebody climbs; there always is.")],
 at="O24", hover="Silke puts it on O24, beside her Scroll.")
lot(5,"DJ",[
 B(2,8), B(4,9,"Nine.", TH(
   ("Noah","Nine for the last Jar. Four of five. I need a Bowl now, and the Bowls are going."),
   ("Clark","Eight was my last bid on the last Jar. Four of five, and the piece I'm short of is the one every upper-class set needs.")))],
 at="L20", hover="Noah puts it on L20, next to his Scroll.")
lot(6,"WB",[
 B(3,10,"Ten.","Ten. Four of five. The last Bowl. One Vase and I'm complete.")],
 at="L11", hover="Rich puts it on L11, beside his Jar.")
lot(7,"VA",[
 B(3,10,"Ten.", TH(
   ("Rich","Ten for the last Vase. I let three go by a million each. Not this one."),
   ("Silke","He needs it to complete. So do I."))),
 B(5,12,"Twelve.", TH(
   ("Silke","Twelve. Five of five. I'm complete, and he isn't."),
   ("Rich","Four Vases in the game, and I've been outbid on every one of them by a million or two. I was waiting for a cheaper one. There isn't a cheaper one."))),
 B(3,None,"No.","Twelve and rising for the piece that would make me Emperor. I'd pay it. I'm not going to pay it in front of the woman who just told me she's complete.")],
 at="P26", hover="Silke puts it on P26, completing the corner by the sea.")
act("The last realia are sold. Every province's stock is empty.", TH(
 ("Noah","Board check. Silke's complete. Rich needs a Vase, Clark a Jar, Paddy a Brush, I need a Bowl, Graham a Customs House and a Scroll. Every piece the rest of us need is in somebody else's set, and only a climb sends one back."),
 ("Reina","Silke's complete. She may replace the Gentry, the Scholar, the Official or a peasant. She's looking at the Gentry. The Gentry's looking at his rent book.")), map_hl=[2,3,4,5,6,7])
say("Silke","I'm complete. I'll tell you what I'm doing with it in the morning.", TH(
 ("Silke","A seat change can happen at any time, and next year's card is turned first thing. I'd like to see what the weather does to Province 3 and Province 5 before I choose which one I wake up in."),
 ("Rich","She's going to take my chair. She's waiting to see whether it rains on it first.")))
salaries()

# ============================== YEAR 5 ==============================
R(5, "Rain and flood", "rainflood")
say("Noah","Spring floods. Good harvest for Provinces 1, 3, 6 and 7. Bad for 2, 4 and 5.", TH(
 ("Noah","And for 8, which is sand. Province 3 good, Province 5 bad. I read it looking at Silke."),
 ("Silke","There it is.")))
swap(5,3,"Silke Weber declares a complete set and replaces Richard Baron. Silke becomes Gentry of Province 3; Rich becomes Silk Peasant of Province 5.", TH(
 ("Silke","Hand back the Scroll, which belongs to Province 3, keep the rest, and take every bag Rich holds: a hundred and forty-one. A good harvest in the province I've just moved into, and a bad one in the one I've just left. And the rent he raised to eight is mine now, and he pays it."),
 ("Rich","Sixty from the pile, a bad harvest, and a landlord. I set the rent at eight two years ago. I'm about to pay it to the woman who paid it to me."),
 ("Reina","The Gentry's chair moved and the rent stayed where it was. That's what a rent is.")),
 at={"CH":"K13", "BB":"K14", "WB":"L13", "VA":"L14"})
say("Silke","K13, K14, L13, L14. Beside the reservoir Rich paid half for.", TH(
 ("Silke","Twenty a year from his reservoir, and his rent, and his banking. The Silk Peasant's set never needed a Jar. Every upper-class set does. I'm one short now, and the only Jar in stock is the one he's just handed back."),
 ("Rich","My Jar went back to Province 5, which is me. I'm selling it. To her, if she wants it, at a price.")))
harvest("Silke, the new Gentry, pays out the harvest.")
rents(8, note="Rents: each peasant pays the Gentry 8.", hover=TH(
 ("Rich","Eight, to Silke. I negotiated this."),
 ("Graham","Same rent, new landlord. Write it down, Clark.")))
taxes(.50, collector="Clark collects the tax")
say("Reina","Graham. The Province 7 Reservoir. Sixty, from the crown.", TH(
 ("Reina","Year five, as I said in year two. I'd like it noted that I said a year and kept it."),
 ("Graham","Four years of asking. It's on time by her calendar and late by mine. Twenty a year from next year."),
 ("Clark","Minuted: 'Year five, Graham.' Struck through, with the date.")))
build("Province 7 Reservoir", 60, {1:60}, key="res7", at="R16:S17", hover=TH(
 ("Graham","R16 to S17, in the south of the wheat. Nobody's coming from the desert to walk across it, so it goes where the fields are flattest."),
 ("","The crown pays the 60, as the booklet says.")))
lot(2,"CH",[
 B(7,6), B(5,8,"Eight.", TH(
   ("Rich","Eight for the Customs House I handed back. I need all five again, and I'm starting with the one I used to own."),
   ("Graham","Six was mine.")))],
 at="P23", hover="Rich puts it on P23, in the silk fields where Silke kept her pieces.")
lot(3,"LD",[
 B(7,8,"Eight.","Eight for the Scroll Silke handed back."),
 B(5,9,"Nine.", TH(
   ("Rich","Nine for my own Scroll, sold by the woman who took my chair. I'm starting again."),
   ("Graham","Five Scrolls. I've bid on all five and lost every one of them, the first four sold by the man who's just outbid me for the fifth."))),
 B(7,None,"No.", TH(
   ("Graham","I'd still be a Customs House short, and the doubling's coming one of these years. When it comes, every bag I hold is a square of the Warlord's desert, and there's no Warlord in it. I'm keeping the bags."),
   ("Noah","He's choosing land over a chair. In a game scored by chairs. He's done the sum some other way.")))],
 at="P24", hover="Rich puts it on P24, beside the Customs House.")
lot(4,"BB",[
 B(5,4), B(6,8,"Eight.", TH(
   ("Paddy","Eight. Five of five. I'm complete."),
   ("Reina","Paddy's complete. He can replace the Official, the Scholar or a peasant, and he's looking at the Official.")))],
 at="S20", hover="Paddy puts it on S20, in the rice fields beside the others.")
say("Rich","My Jar. Clark's one Jar short of the throne. So is Silke.", TH(
 ("Rich","The Official needs a Jar; the Gentry needs a Jar; the Scholar's got one. Every upper-class set has a Jar in it, and the only one on sale is mine. I'm sitting on the key to the throne room. I'm a silk farmer with forty, and I'm sitting on the key to the throne room."),
 ("Clark","He's right. Four of five, and a Jar makes me Emperor. With a hundred and sixteen in hand I'd pay a great deal for it."),
 ("Silke","And I have two hundred and fifty-odd.")))
say("Silke","Forty for it, Rich.", TH(
 ("Silke","Forty out loud, so the table can do the sum. A quarter of forty is his commission: ten."),
 ("Rich","Ten in my hand if she wins it. Ten a year in my hand if somebody pays me not to sell it.")))
say("Rich","Majesty. A quarter of what Silke offers, every year, and my Jar opens at whatever Silke holds, less nineteen and a half.", TH(
 ("Rich","The minimum bid is two, 'but you may set any higher minimum you like.' Set it at her grain less nineteen and a half and she can never pay it and keep the twenty she needs to change seats, however rich she gets. Nobody else can come near it. I'll keep it to the letter, as long as the crown keeps paying."),
 ("Reina","Ten a year to keep both of them out. It's the cheapest wall in the country."),
 ("Clark","He's selling the crown a lock on a door he owns. Minuted: the Jar retainer, year one.")))
act("Reina pays Rich 10 to keep the Jar's minimum where he named it.", TH(
 ("Reina","The Emperor's booklet doesn't mention retainers. It does mention remaining in power."),
 ("Silke","Ten a year. She'll be paying more next year. I'll see to it.")), {pid(1):-10, pid(5):10}, map_hl=[1,5], deal=True)
act(f"Rich puts up the Dragon Jar at a minimum of {grain[pid(3)]-19.5:g}: Silke's grain, less nineteen and a half. Nobody can meet it, and it stays in his stock.", TH(
 ("Rich","It's on sale. It's been offered, as the booklet says. It'll be offered again next year, at whatever she has then."),
 ("Clark","Two hundred and thirty-five. I've got a hundred and sixteen. The arithmetic has never been less on my side.")), map_hl=[5])
lot(6,"WB",[
 B(5,4), B(4,8,"Eight.", TH(
   ("Noah","Eight for the Bowl. Five of five. I'm complete."),
   ("Reina","Noah's complete, and the Scholar may take the throne.")))],
 at="M22", hover="Noah puts it on M22, by the canal at the bottom of Province 4.")
say("Noah","I'm complete, Majesty. I'm not taking your chair. You have my word.", TH(
 ("Noah","My booklet says I dream of becoming Emperor to bring peace to the land, so that everyone can study poetry. Look at the desert. There's peace. I'll study the poetry from here."),
 ("Reina","The honest one is free. The landlord costs ten a year."),
 ("Silke","He means it. That's the worst kind of obstacle.")))
say("Reina","Paddy. If you're choosing, take the Official's chair.", TH(
 ("Reina","If Paddy replaces Clark, Clark goes to the rice fields, and a Rice Peasant can't take the throne however many Jars he buys. One climb removes one threat."),
 ("Paddy","The Official's the highest chair I'm allowed. The Emperor's asking me to take it. I didn't think it worked like that."),
 ("Clark","She's just told him to take my seat. In front of me. I'm writing that down, in ink.")))
say("Paddy","I'll sleep on it. And I won't take yours, Majesty, whatever I end up holding.", TH(
 ("Paddy","I'm a rice farmer. I'm complete. I can't quite believe either of those, and I'd like a night before I find out what happens to the man I'm replacing."),
 ("Reina","Two promises in one round, and neither cost me anything.")))
salaries()

# ============================== YEAR 6 ==============================
R(6, "Imperial charity", "chest")
swap(6,2,"Paddy Doyle declares a complete set and replaces Clark Grafton. Paddy becomes Official of Province 2; Clark becomes Rice Peasant of Province 6.", TH(
 ("Paddy","Hand back the Customs House, which belongs to Province 2, keep the rest, and take every bag Clark holds. A hundred and twenty-one. I've never held two hundred of anything."),
 ("Clark","Sixty from the pile, the rice fields, and the whole set back in the box. Four of five, one Jar short, and the Emperor told a rice farmer to take my chair. I have it minuted."),
 ("Noah","He's taken the Official's chair and he's one piece short of the throne. Climbing on: a climber's always one short of the next one. And the piece he's short of is a Bowl, and the Bowls belong to Province 6.")),
 at={"LD":"H13", "BB":"H14", "DJ":"I13", "VA":"J13"})
say("Paddy","H13, H14, I13 and J13, round the irrigation.", TH(
 ("Paddy","Where Clark kept his Scroll, beside the ditch he paid half for. It seemed polite."),
 ("Clark","He's put my furniture back where my furniture was, except it's his.")))
say("Clark","Province 6 sells Bowls. I'm Province 6.", TH(
 ("Clark","My own Bowl, the one I handed back, is the only one in stock. Paddy needs it for the throne. I'm the seller."),
 ("Paddy","He's going to make me pay for it. I'd make me pay for it.")))
say("Silke","Imperial charity. An average harvest, and two from the crown to each of us.", TH(
 ("Silke","Twelve from the crown, which has three hundred. It won't notice. It will notice next year."),))
harvest("Silke pays out the harvest.")
rents(8, note="Rents: each peasant pays the Gentry 8.", hover=TH(
 ("Clark","Eight to Silke, my first year in the rice fields. I collected her tax for five years. Now I pay her rent."),))
act("Imperial Charity: Reina gives 2 from the crown's reserve to every other player.", TH(
 ("Reina","Twelve. The card calls it charity. I call it the cheapest goodwill I'll buy all game."),
 ("Rich","Two. I'll put it toward my retainer's retainer.")), {**{p:2 for p in PLAYERS if p != pid(1)}, pid(1):-12}, map_hl=[1,2,3,4,5,6,7])
taxes(.50, collector="Paddy collects the tax")
say("Reina","The Summer Palace. Twenty. The key to the Wall and my own canal.", TH(
 ("Reina","The last palace on the list but one. It opens the work I've put last on purpose."),
 ("Paddy","I collected the tax for the first time and the first thing it bought was a palace. I'd expected to feel something.")))
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="G24", hover=TH(
 ("Reina","G24, on the north-east side of Province 1, looking at the sea."),
 ("","Reina pays the 20.")))
lot(2,"CH",[
 B(6,4), B(7,6,"Six.", TH(
   ("Graham","Six for the Customs House Paddy handed back. Four of five. A Scroll, and there's one in Silke's stock."),
   ("Clark","Four. I'm starting again too, with sixty and a buffalo with a history.")))],
 at="Q14", hover="Graham puts it on Q14, at the top of his row of pieces in the wheat.")
lot(3,"LD",[
 B(7,6,"Six.","Six. The sixth Scroll I've bid on, and the last piece I need."),
 B(6,7,"Seven.", TH(
   ("Clark","Seven for the Scroll I handed back. I need it again."),
   ("Graham","Six. That's six Scrolls I've bid on. Every one of them gone by one or two, to somebody climbing past me or somebody falling past me."))),
 B(7,None,"No.", TH(
   ("Graham","I could go to eight and be complete. Then I'd climb, and whoever I climbed over would get the reservoir I asked for for four years, a year after it was built. I'd rather keep the reservoir, and the grain for when the desert opens."),
   ("Noah","He's turned down a chair for a ditch. He'll tell you it's arithmetic.")))],
 at="R21", hover="Clark puts it on R21, in the middle of the rice fields where Paddy kept his Jar.")
lot(4,"BB",[
 B(5,6), B(6,8,"Eight.","Eight for my own Brush back. Two of five. A Customs House, a Jar and a Vase to go, and the Jar's behind Rich's minimum."),
 B(5,None,"Out.","Eight's a lot for a Brush when I've no Bowl in sight.")],
 at="R22", hover="Clark puts it on R22, beside the Scroll.")
say("Silke","Sixty for the Jar this year, Rich.", TH(
 ("Silke","A quarter of sixty is fifteen. I'm not trying to buy the Jar. I'm trying to raise the price of keeping me out."),
 ("Reina","Fifteen. She's bidding against the crown, and the lot is my patience.")))
act("Reina pays Rich 15, a quarter of Silke's offer, to keep the Jar's minimum where it is.", TH(
 ("Rich","To the letter: a quarter of what she offers. Fifteen this year."),
 ("Reina","Twenty-five over two years for a pot nobody's bought.")), {pid(1):-15, pid(5):15}, map_hl=[1,5], deal=True)
act(f"Rich puts up the Dragon Jar at a minimum of {grain[pid(3)]-19.5:g}. Nobody can meet it.", TH(
 ("Rich","Offered, as required. Unsold, as paid for."),
 ("Clark","A Rice Peasant needs a Jar too. He's set the price for a Gentry. I'm not even in the auction; I'm in the audience.")), map_hl=[5])
say("Clark","Majesty. Ten a year, and my Bowl opens at whatever Paddy holds, less nineteen and a half.", TH(
 ("Clark","Rich has shown me how. The Official's one Bowl short of the throne, and I'm the only man who sells Bowls."),
 ("Reina","Paddy's given me his word. His word costs nothing. Yours costs ten. I'll take his."),
 ("Paddy","She's trusting me. I'd better be trustworthy. I've never been tested before.")))
say("Reina","No, Clark. Sell it.", TH(
 ("Reina","A promise from Noah, a promise from Paddy, and a retainer on Rich. That's every door I can see."),
 ("Clark","Then I'll sell it dear.")))
lot(6,"WB",[
 B(2,40,"Forty.", TH(
   ("Clark","Forty: the minimum I set. Paddy pays it, and I get ten. He's paying me with my own grain, which he took this morning."),
   ("Paddy","Forty for a Bowl. Five of five. I'm a complete Official, and I promised not to use it."))),
 B(5,None,"Not at forty.","Forty for a Bowl, with no Brush and no Jar to go with it. I'm a silk farmer.")],
 at="J14", hover="Paddy puts it on J14, below the irrigation, at the bottom of Province 2.")
say("Paddy","I'm complete, Majesty. I said I wouldn't, and I won't.", TH(
 ("Paddy","Two climbs to the throne, for a peasant. I'm ready for the second one, and I'm putting it down. I like being trusted more than I thought I would."),
 ("Silke","Two complete men who've promised her not to, and a third man paid to keep me out. Everyone's keeping the Emperor in her chair except the Emperor."),
 ("Reina","Noah's word, Paddy's word, and Rich's price. That's my wall.")))
lot(7,"VA",[
 B(6,5), B(5,7,"Seven.", TH(
   ("Rich","Seven for the Vase Clark handed back. Three of five: Customs House, Scroll, Vase. I'd like it noted that this is the fifth Vase I've bid on, and the first I've won."),
   ("Clark","Five was mine. I need a Vase, a Customs House and a Jar.")))],
 at="P25", hover="Rich puts it on P25, beside the Customs House.")
salaries()

# ============================== YEAR 7 ==============================
R(7, "The population doubles", "double1")
say("Noah","The population doubles. Good harvest for everyone. Three hundred million people.", TH(
 ("Noah","A hundred and twenty a year to feed a province, against a harvest of a hundred and whatever the ditches add. Every province with a twenty-a-year work lands on nothing. The crown eats a hundred and eighty and grows a hundred. Fourteen cards left, and two of them are doublings."),
 ("Reina","Minus eighty a year for the crown, until something changes. The something is in Section 13.")))
harvest()
say("Clark","Silke. Eight a year in rent, on an income of nothing.", TH(
 ("Clark","Rice Peasant, good harvest, the canal the crown paid for: nought. Then eight to the Gentry. I'd like that minuted as the first grievance of the doubling."),
 ("Silke","When I paid it, it was eight. Rich set it, and Rich is paying it too."),
 ("Graham","Eight, on nought. I'm adding it to the list.")))
say("Silke","The rent's eight. It was eight when I was in the fields.", TH(
 ("Silke","The booklet says the Gentry treats the peasants as children. I'm treating them exactly as I was treated."),
 ("Rich","I set it at eight to sell a Scroll cheap. I didn't think I'd be the one paying it at three hundred million.")))
rents(8, note="Rents: each peasant pays the Gentry 8.")
taxes(.50, collector="Paddy collects the tax")
say("Paddy","Fifty per cent, Majesty, of nothing. Not a bag. The only incomes above nought are nobody's.", TH(
 ("Paddy","My own income's minus ten: the Official's harvest, the irrigation, and a hundred and twenty mouths."),
 ("Reina","Nobody pays tax on nought. The country's tax base went this morning, with the card.")))
say("Graham","Majesty. Section 13. The population's doubled. New land is open.", TH(
 ("Graham","Twenty a square from the Harvest Pile, twenty a year from every square, and no limit. Province 7 develops the Warlord's land. The Warlord's land is empty. It's been empty for seven years. There isn't a soldier on it or a pink square anywhere on the board."),
 ("Clark","The Rice Peasant may take the sea or the desert. I'll take the desert, because there's nobody in it."),
 ("Silke","And the Gentry may take the strip under the Wall, once the four links above Province 3 are built. None of them are.")))
say("Reina","No system this year: the Marble Pagoda. And the crown pays a quarter of every square anybody buys.", TH(
 ("Reina","Five a square. The booklet says the cost must be shared; it doesn't say how. I have two hundred and fifty-seven and minus eighty a year, and I need my own land before anyone's."),
 ("Graham","A quarter. I'd hoped for half. Half was the reasonable number. I'm writing down the unreasonable one."),
 ("Clark","Minuted: five a square from the crown. Grievance, Graham's, number I've lost count.")))
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="F18", hover=TH(
 ("Reina","F18, the north corner of the throne room. The building that does nothing, in the year everything else is land."),
 ("","Reina pays the 20.")))
buy_land(1, ["F23","E23","G27","H25","I25","J25"], {1:120}, "New land: Reina buys six squares of sea for Province 1, along the coast at E23, F23, G27, H25, I25 and J25.", TH(
 ("Reina","A hundred and twenty, all from the crown, because it's the crown's own land. A hundred and twenty a year from next year, and the throne room stops starving. The strip under the Wall stays shut to me until my own four links stand."),
 ("Noah","Six squares. She's bought exactly enough sea to turn minus eighty into plus forty on a good year. She's done the sum.")))
buy_land(7, ["P12","Q12","R12","S12","T13"], {7:75, 1:25}, "New land: Graham buys five squares of the Warlord's desert for Province 7, at P12, Q12, R12, S12 and T13, the crown paying 25.", TH(
 ("Graham","Seventy-five from me. A hundred a year from next year, on ground that in any other game would have a soldier on it by spring. The western front. Nobody's there. Nobody's coming."),
 ("Paddy","He's farming the Warlord's front garden and the Warlord's not even in the building."),
 ("Clark","The quietest border in the history of the game, and he's ploughing it.")))
buy_land(6, ["T19","T20","T21"], {6:45, 1:15}, "New land: Clark buys three squares of the Warlord's desert for Province 6, at T19, T20 and T21, the crown paying 15.", TH(
 ("Clark","Forty-five, almost all I have, for sixty a year. The Official never got land. The Rice Peasant gets the desert on the first morning. I've been demoted into the only good job in the country."),
 ("Silke","He's happy. He's actually happy.")))
buy_land(5, ["P27","O27","N26"], {5:45, 1:15}, "New land: Rich buys three squares of sea for Province 5, at P27, O27 and N26, the crown paying 15.", TH(
 ("Rich","Forty-five. Sixty a year from the sea. The Silk Peasant may take the sea, and the landlord may not take anything, because his Wall isn't built. I'm better off in the fields than I was in the chair."),
 ("Silke","He's right, and he'll still pay me eight.")))
buy_land(4, ["K25","J26","K26"], {4:45, 1:15}, "New land: Noah buys three squares of sea for Province 4, at K25, J26 and K26, the crown paying 15.", TH(
 ("Noah","Forty-five, and sixty a year back. The arithmetic's been against the Scholar since the first card. It's finally on my side."),))
say("Paddy","And the Official's land is under the Wall, and the Wall's not built.", TH(
 ("Paddy","Four links above Province 2, a hundred and sixty, and not one of them standing. Silke's the same. The two of us who climbed are the two of us locked out."),
 ("Silke","The landlord's land is behind a Wall built against horsemen from the north, and there aren't any. It's a gate with nothing on the other side but my own fields.")))
say("Silke","Eighty for the Jar this year, Rich.", TH(
 ("Silke","A quarter of eighty is twenty. I watch the crown's reserve; everybody can. It's about to get thin."),
 ("Reina","Twenty, in the year the crown's income went to minus eighty.")))
act("Reina pays Rich 20, a quarter of Silke's offer, to keep the Jar's minimum where it is.", TH(
 ("Reina","Forty-five over three years for a Jar that's never been sold."),
 ("Rich","To the letter.")), {pid(1):-20, pid(5):20}, map_hl=[1,5], deal=True)
act(f"Rich puts up the Dragon Jar at a minimum of {grain[pid(3)]-19.5:g}. Nobody can meet it.", TH(
 ("Rich","Offered, as the booklet says. Unsold, as the crown pays."),
 ("Noah","The only piece in the country that's been on sale for three years.")), map_hl=[5])
salaries()
say("Silke","Seventeen in the crown's reserve, Majesty.", TH(
 ("Silke","'The Emperor has too low a grain reserve.' Section 16, cause three. I'd need two others to agree, and Graham has a list and Clark has the minutes. Then Chaos, and the new Emperor is whoever has the most money, which is me. I'm not doing it. A revolt is a vote. The Jar is a purchase. I prefer purchases."),
 ("Graham","I'd agree. I'd like it known I'd agree. I'm not being asked."),
 ("Reina","Seventeen. She's told me she has the votes and isn't using them. That's not mercy. That's a price list.")))

# ============================== YEAR 8 ==============================
R(8, "The canal holds", "canal")
say("Noah","The Canal Gives Way. Average harvest. All unfinished canal work is lost: there isn't any. Where both sections stand, the province pays the Emperor 2. And Provinces 2, 3, 7 and 8 play a disaster.", TH(
 ("Noah","The crown built Provinces 4, 5 and 6 whole and hasn't started its own, so nothing falls in. Me, Rich and Clark pay two each for our finished canals. Paddy, Silke and Graham play disasters; 8 is sand."),
 ("Reina","Unfinished work is lost, and I haven't got any. Six, for once, coming in.")))
harvest(hover_extra=[{"w":"Graham","t":"The desert's first year. Province 7: seventy-five, the reservoir's twenty and a hundred from five squares of sand, against a hundred and twenty to eat. Seventy-five to the good. Last year it was nought."}])
rents(8, note="Rents: each peasant pays the Gentry 8.")
act("The Canal Gives Way: Noah, Rich and Clark, whose provinces' canals stand finished, pay the Emperor 2 each.", TH(
 ("Clark","Two, for a canal I never paid for in a province I never asked to be in. Minuted anyway."),
 ("Rich","Two. The card calls it a contribution."),), {pid(4):-2, pid(5):-2, pid(6):-2, pid(1):6}, map_hl=[1,4,5,6])
disaster(2,"the imperial barge rams a lock gate on the new canal during his inspection. He pays for the damage rather than lose face.", TH(
 ("Paddy","Ten, in the year the canal gives way. Our canal held. My barge didn't."),
 ("Clark","That was my disaster. I'd have enjoyed it.")))
disaster(3,"the head chef retires after forty years and is promised a house and a pension.", TH(
 ("Silke","Five for a chef. I've been the Gentry for three years, and I've inherited Rich's kitchen staff."),
 ("Rich","That was my chef. I hired him.")))
disaster(7,"the Emperor takes his eldest daughter into the imperial household. He must feast the village.", TH(
 ("Graham","Two million. And look who the card says took her."),
 ("Reina","That's the card, not me. ...it's going on his list, isn't it.")))
taxes(.50, collector="Paddy collects the tax")
say("Paddy","Ninety to the crown, Majesty. Every bag of it from new land.", TH(
 ("Paddy","Graham thirty-seven and a half, and Clark, Rich and Noah seventeen and a half each. The four of them who bought land are the only four with an income."),
 ("Graham","The desert pays more tax than the throne room. Nobody's raided it.")))
say("Reina","My own canal. Two sections in Province 1, eighty.", TH(
 ("Reina","Twenty a year back, and the crown needs it more than anyone: a hundred and twenty a year from the sea, twenty from the canal, and a hundred and eighty mouths."),
 ("Clark","Minuted: the Grand Canal in Province 1. The crown, eighty. Everything on the list is built but the Wall."),
 ("Graham","Four hundred and eighty to go, all of it Wall, and not one link standing.")))
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
buy_land(7, ["T14"], {7:19, 1:1}, "New land: Graham buys a sixth square of desert for Province 7, at T14, the crown paying 1.", TH(
 ("Graham","Nineteen from me, one from the crown. 'The cost must be shared.' One million in twenty is a share. It's the smallest share the booklet allows, and she's found it."),
 ("Reina","I've got forty-eight, and the retainer's twenty-five. One is what I have for him."),
 ("Clark","Minuted: one. With a drawing of a very small bag.")))
say("Silke","A hundred for the Jar this year, Rich.", TH(
 ("Silke","Twenty-five. Watch her reserve."),
 ("Reina","Twenty-five, after the canal and Graham's square. That leaves me twenty-two, before salaries.")))
act("Reina pays Rich 25, a quarter of Silke's offer, to keep the Jar's minimum where it is.", TH(
 ("Reina","Seventy over four years. The cost of a pot that has never left its shelf."),
 ("Rich","To the letter. I've made seventy on a Jar I still own. The landlord's chair was never this good.")), {pid(1):-25, pid(5):25}, map_hl=[1,5], deal=True)
act(f"Rich puts up the Dragon Jar at a minimum of {grain[pid(3)]-19.5:g}. Nobody can meet it.", map_hl=[5])
salaries()
say("Graham","Majesty. Your reserve's at twelve.", TH(
 ("Graham","'Too low a grain reserve.' 'Delayed too long in building public works': not one link of the Wall in eight years. And I've got a list: six Scrolls, the reservoir in year five, five a square and then one. I'm not revolting. I'm reading it out, so it's been said."),
 ("Silke","He's reading my cause for me. I still prefer the Jar."),
 ("Reina","Twelve. Two causes, read aloud, by the quietest man at the table.")))

# ============================== YEAR 9 ==============================
R(9, "Heaven has favourites", "heaven")
say("Noah","Heaven has favourites. Good harvest for Provinces 2, 4 and 5. Bad for 1, 3, 6 and 7.", TH(
 ("Noah","Twelve cards left. Two doublings among them, and if either comes the country is six hundred million and the crown eats three hundred and sixty."),
 ("Silke","Bad for Province 3. Minus fifty. I don't mind. I'm not planning to stay.")))
harvest()
rents(8, note="Rents: each peasant pays the Gentry 8.")
taxes(.50, collector="Paddy collects the tax")
say("Silke","A hundred and sixty for the Jar, Rich.", TH(
 ("Silke","A quarter is forty. I can see the crown's reserve from here, and so can everyone else. She can pay Rich forty, or she can build something. She can't do both."),
 ("Rich","Forty, Majesty. To the letter.")))
say("Reina","The Wall above Province 2. Four links, a hundred and sixty. Paddy, sixty?", TH(
 ("Reina","A hundred and twenty-two in the reserve. A hundred for the crown's share of the Wall, or forty for Rich and one link I could just about pay. One link a year finishes the Wall in year twenty, and there are two doublings in twelve cards. At six hundred million the crown loses a hundred and forty-five a year, sea and canal included. I can keep the chair or I can keep the list. Not both."),
 ("Paddy","Sixty. The four links above me open my strip. I promised her I'd never take her chair, and she's paying for my land with it."),
 ("Silke","She's chosen the Wall. She knows what it costs her. I'll finish it.")))
build("Great Wall — the 4 links above Province 2", 160, {1:100, 2:60}, wall={2:4}, hover=TH(
 ("Clark","Minuted: the crown a hundred, the Official sixty. Four links of twelve, in year nine."),
 ("Graham","The first links of a Wall built against horsemen from the north, and there aren't any. The only thing it's ever kept out is Paddy, from his own strip. Now it lets him in.")))
buy_land(2, ["F13","F14"], {2:38, 1:2}, "New land: with the four links above Province 2 standing, Paddy buys two squares of the strip below the Wall, F13 and F14, the crown paying 2.", TH(
 ("Paddy","Thirty-eight from me, one a square from the crown. Forty a year. It's the first thing I've bought in this chair that grows."),
 ("Reina","Two. The last two I'll spend as Emperor, probably.")))
say("Reina","No retainer this year, Rich.", TH(
 ("Reina","Twenty in the reserve and salaries to pay. I could have kept Silke out one more year, and the Wall in Province 2 would still be a line on the map. Silke has nearly three hundred. She'll finish it, because finishing it is the only way to keep the chair once she has it."),
 ("Rich","To the letter: my minimum was hers less nineteen and a half for as long as the crown paid. The crown has stopped. So has the minimum.")))
lot(5,"DJ",[
 B(3,160,"A hundred and sixty. As offered.", TH(
   ("Silke","A hundred and sixty. Five of five, as Gentry. I'm complete, with a hundred and odd left, and the throne's one sentence away."),
   ("Rich","Forty to me as commission. Seventy in retainers, forty now. A hundred and ten for a pot I bought for nine."),
   ("Clark","I need a Jar too. I've got about twenty. I'm not even bidding; I'm watching.")))],
 at="M14", hover="Silke puts it on M14, at the bottom of Province 3, for the length of one sentence.")
salaries()
swap(3,1,"Silke Weber declares a complete set and replaces Reina Osorio. Silke becomes Emperor of Province 1; Reina becomes Gentry of Province 3.", TH(
 ("Silke","Everything goes back to where it came from: the Customs House, the Brush, the Bowl, the Vase and the Jar. I take the imperial reserve, which is ten, and the throne room, and six squares of sea Reina bought, and a hundred and eighty mouths. Silk farmer to the throne in two climbs."),
 ("Reina","Sixty from the Harvest Pile and the Gentry's chair. And the strip that opens when the four links above Province 3 stand, and she's going to build them."),
 ("Noah","My promise was to the chair, not to the woman in it. It stands. Paddy?"),
 ("Paddy","Mine too. I've promised two Emperors now.")), )

# ============================== YEAR 10 ==============================
R(10, "The Emperor's share", "share")
say("Noah","The Emperor's Share. Average harvest. Every province with a public work splits the extra harvest it produces with the Emperor, half and half.", TH(
 ("Noah","Every province but the throne has a work, and the throne has its canal. Fifty-five to the crown, on top of the tax."),
 ("Silke","The first card I hear as Emperor pays me fifty-five. I'd like to thank the ditches.")))
harvest("Reina, the new Gentry, pays out the harvest.")
rents(8, note="Rents: each peasant pays the Gentry 8.", hover=TH(
 ("Reina","Twenty-four to me. I set the tax for nine years. I'm collecting the rent Rich set and Silke kept."),
 ("Rich","Eight, to my third landlord.")))
act("The Emperor's Share: each province with a public work pays Silke half its increase: 5 from Paddy, 10 each from Reina, Noah, Rich, Clark and Graham.", TH(
 ("Graham","Ten, half my reservoir's twenty. The reservoir I asked for for four years, paying the Emperor who didn't build it."),
 ("Silke","Fifty-five. And Paddy's tax coming.")), {pid(2):-5, pid(3):-10, pid(4):-10, pid(5):-10, pid(6):-10, pid(7):-10, pid(1):55}, map_hl=[1,2,3,4,5,6,7])
taxes(.50, collector="Paddy collects the tax")
say("Silke","The Wall. All eight links that are left, above Provinces 1 and 3. Three hundred and twenty. Reina, the Gentry's share is forty.", TH(
 ("Silke","Every work the country owes, standing this morning, and the game ends with me on the throne. I can pay it alone, just. I'd rather the woman who wrote the list paid for the last line of it."),
 ("Reina","She's asked me for forty. I can see what's in the stock: the Customs House, the Brush, the Jar, the Bowl and the Vase she handed back last night. The Gentry's set, exactly. At the next auction I could buy all five, and next spring take the chair back. If the Wall waits a year."),
 ("Clark","The Customs House, the Jar and the Vase are mine to buy at that auction too. If there is one.")))
say("Rich","Majesty. Build the four above Province 1 this year, and the rest next year. Forty, for your patience.", TH(
 ("Rich","There's a Brush and a Bowl in the stock, and with them I'm complete again, with twenty in hand and more. One more auction and I'm back in a chair. The game ends the moment the last link stands, before anyone sells anything."),
 ("Silke","He's offering me forty to keep the game going long enough for him to climb over somebody. He paid nine for that Jar. I paid him a hundred and sixty.")))
say("Silke","No, Rich.")
say("Rich","Then Section 16. The Emperor has delayed too long in building public works: ten years, and the Wall's a third built. I'll revolt, if two of you agree.", TH(
 ("Rich","A revolt is Chaos, and Chaos builds nothing. That's an auction. That's all I want."),
 ("Clark","Agreed. I've got the minutes: every deferral, every year. Ten years of them."),
 ("Noah","One more. He needs one more. It isn't going to be me.")))
say("Noah","No. I gave my word to the chair.")
say("Paddy","No. I've got forty a year coming off that strip.", TH(
 ("Paddy","And I promised. And I'm surprised to still be in this chair, and I'd like to finish surprised."),))
say("Graham","No. It's quiet. Leave it quiet.", TH(
 ("Graham","Ten years and not one pink square on the board. Six squares of the Warlord's desert growing wheat, and not a soldier in sight. I've lost six Scrolls by a million or two each, the reservoir five years late, and five a square from the crown and then one. I have a list. It's a good list. I'm not starting the first fight of the game in the last year of it."),
 ("Rich","The quietest man at the table, with the longest list, and he won't use it."),
 ("Clark","Minuted: 'Leave it quiet.' Graham, year ten.")))
say("Reina","No. And here's the forty.", TH(
 ("Reina","The five pieces are sitting in the stock, and one more auction would put them in my hands. I wrote the list on the first night: the works that grow food first, the palaces they need, and the Wall last. It's the last line. I'm paying for it."),
 ("Silke","She could have held out for a year and an auction. She's paying to lose. I'll remember that she did."),
 ("Rich","Two votes. I needed three. Nobody blames the Warlord, and nobody revolts.")))
build("Great Wall — the last 8 links, above Provinces 1 and 3", 320, {1:280, 3:40}, wall={1:4, 3:4})
assert all_built(), "not every public work is built"
act("Every public work the country owes is standing: three palaces, twelve links of the Great Wall, eight sections of the Grand Canal, the irrigation system and the two reservoirs. The game ends: the players have survived, and the Emperor's reign has been a glorious one. It lasted a year.", TH(
 ("Silke","Ten years, two climbs, a hundred and sixty for a Jar and two hundred and eighty for a Wall. I started in the silk fields, paying rent to Rich."),
 ("Reina","Nine years on the throne, and the list finished, with my name on every line of it but the last eight links. I'd do the order again. I'd pay Rich less."),
 ("Noah","Nobody raided anyone, and nobody revolted. The only weapons were rent, a retainer and a minimum bid.")), map_hl=[1,2,3,4,5,6,7], big=True)
say("Clark","For the record: I sold Paddy the Bowl for forty, and I was the one who should have been paid not to.", TH(
 ("Clark","Rich found the trick in year five and made a hundred and ten from it. I found it in year six, and the Emperor said Paddy's word was cheaper. It was."),
 ("Paddy","It was. I'd like it minuted that it was.")))
act("After the last link, Noah turns the next card over, because everyone wants to know. Population Doubles.", TH(
 ("Noah","Six hundred million, one card away. The crown would have eaten three hundred and sixty and grown two hundred and forty, with the sea and the canal and a good harvest. Nobody would have paid tax again."),
 ("Graham","Not even the desert. Six squares of it makes nought, at six hundred million."),
 ("Silke","We finished a year early. That's what a year early looks like.")), map_hl=[4])

RESULT = export(
 "Every public work was built, so this is the first ending: the players survived and the Emperor's reign was a glorious one. Players are ranked by the province they finished in against the one they drew.",
 ["Silke Weber started in the silk fields and finished on the throne, the peasant who climbed twice. She took the Gentry's chair from Rich in Year 5, the morning the floods gave Province 3 a good harvest and Province 5 a bad one, and the throne from Reina in Year 9. Then she finished the Wall with her own grain, a year before the next card would have taken the population to six hundred million.",
  "Reina held the throne for nine years with three walls of her own: Noah's word and Paddy's, which cost her nothing, and a retainer to Rich, which cost seventy. Rich, the man she paid, had been the landlord until Silke climbed over him, and as Silk Peasant he held the only Dragon Jar on the market. When the doubling left the crown with twelve in its reserve, Reina chose the Wall over the retainer, and let the Jar go. In the last year she declined a revolt and an auction that might have given her the throne back, and paid forty toward the work that ended the game.",
  "Paddy climbed once, from the rice fields to the Official's chair, completed the Official's set the next year and promised not to use it. Clark fell from Official to Rice Peasant, and found the desert. Rich fell from Gentry to Silk Peasant and made a hundred and ten from a Jar he bought for nine. Noah completed his set in Year 5, gave his word, and kept it. Graham never completed his set: he lost six Scrolls by a million or two each, and spent the grain on the Warlord's land instead.",
  "There was no Warlord, so there were no raids, no soldiers and no tolls, and the western desert, which in every other game belongs to the man who raids from it, was wheat and rice fields by Year 8. Nobody could blame the Warlord. The country's dangers were the population clock, the Emperor's choices, the Gentry's rent and the climbers, and every one of them was paid in grain."])
