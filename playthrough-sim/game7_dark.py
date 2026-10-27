# Game 7 — The Dark Ages. Six players: an early revolt, years of Chaos, and a recovery.
setup([1,2,3,5,6,8], "dark", "The Dark Ages",
      "Six players · twelve years · Chaos, then recovery",
      "Noah and Graham sit out. Reina taxes hard to build the Wall before the population comes, and the table revolts in Year 3. Nobody can win the acclamation, so Chaos lasts three years: no tax, no salaries, no public works, while the harvest, the rent and the Warlord carry on.",
      short="6 players · 12 years")

# ============================== SETUP ==============================
R(0, "Six booklets", None, "Six players: the Emperor, the Official, the Gentry, the Silk and Rice Peasants and the Warlord (rulebook Section 4 and Appendix A). No Scholar, so the Emperor appoints someone to read I Ching. Each realia province holds two of its own pieces, each collector needs one from each of the other three, and the Warlord starts with two soldiers.")
act("Noah and Graham sit this one out. Six booklets are shuffled and drawn: Reina Osorio draws the Emperor, Clark the Official, Rich the Gentry, Silke the Silk Peasant, Paddy the Rice Peasant, and Robert Land the Warlord.", TH(
 ("Reina","The throne. 'You must see to the welfare of your people at all times.' I intend to, whether they like it or not."),
 ("Clark","The Official. 'Surrendering your moral values whenever there is a gain to be made in your goal of becoming the Emperor.' It's less a personality than a job description."),
 ("Rob","The Warlord. Two soldiers at six players. I'll make them count.")), map_hl=[1,2,3,5,6,8])
act("Rich sets out the Harvest Pile, twenty-five hundred million in bags of eight sizes, where everyone can see it.", TH(
 ("Rich","I bank the pile and I collect the rent. Both of those happen every year whatever else is going on at this table. I find that restful."),
 ("Paddy","He said 'whatever else is going on' like he knows something.")), map_hl=[3])
deal_grain("Rich deals 60 to each of the six players. That's the first year's harvest.", TH(
 ("Rich","Three hundred and sixty out before anyone's done a thing."),
 ("Silke","Sixty. A good harvest is a hundred and my family eats forty. Out of the sixty I owe the Gentry five and the Emperor whatever she says.")))
act("Reina Osorio appoints Paddy Doyle to read the I Ching and keep the population count, at the Scholar's salary of 5. Paddy shuffles the twenty cards and lays them face down.", TH(
 ("Reina","Somebody honest holding the clock. Paddy can't read a card without his face telling the table what it means, and that's the job."),
 ("Paddy","Five a year to turn over cards. Five of the twenty raise the population, it says in the rulebook. I'm going to be the one who reads those out.")), map_hl=[1,6])
take_stock("Clark, Rich, Silke and Paddy each take two pieces of their own realia out of the box: Customs Houses, Scrolls, Dragon Jars and Wooden Bowls. Eight pieces in all, beside the board until they're sold.", TH(
 ("Clark","Every collector needs one piece from each of the other three provinces, and there are two of each. Three of us want every piece. Somebody is always going to be one short."),
 ("Rob","Beside the board, not on it. I'll wait until they're on squares.")))
act("Clark cuts out the Province 2 Irrigation System, one square by two, and Rich the Province 3 Reservoir, two by three. Nobody sits in Provinces 4 or 7, so nothing is owed there.", TH(
 ("Rich","Two by three. The biggest cut-out in the box."),
 ("Clark","One by two. The cheapest system on the list. Which makes it the one she can't refuse."),
 ("Reina","Three palaces, twelve links of Wall, six canal sections and two systems. Eight hundred and ninety million. I've read the list twice.")), map_hl=[2,3])
place_army({"W1":"E21", "W2":"T21"}, "Robert Land stands his two soldiers on undeveloped land: W1 on E21, in the strip below the Wall, one step from the Emperor's province; W2 on T21, in the desert below the rice fields.", TH(
 ("Rob","Province 1 pays ten a raid and everybody else pays five, so one goes to the throne. The other sits under Paddy, because the south of this board is two peasants and two empty provinces, and I can walk through an empty province without paying anyone."),
 ("Paddy","T21 is one step from three of my squares."),
 ("Reina","E21. He's looking straight down at my fields.")))
say("Reina","I'll tell you all now what kind of reign this is going to be.", TH(
 ("Reina","Five cards raise the population and none of them lowers it. The harvest never grows. The only money in this game that keeps pace with the people is new land, and the strip below the Wall only opens when the Wall above it stands. So: tax hard now, while everyone's harvest is positive, and build the Wall before the cards come."),
 ("Clark","She's announcing a plan in the Setup round. I'm going to need a pen."),
 ("Rich","She's right, which is the trouble. Being right is going to cost all of us a great deal of grain.")))
say("Rob","Majesty. I look forward to it.",
 "A hard-taxing Emperor and a table of people who'll resent every bag. I don't have to do anything. I just have to be standing here when it goes.")

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
rents()
say("Reina","Fifty per cent.", TH(
 ("Reina","Fifty in Year One. The General Instructions call that the British rate, and put dictatorships at eighty or ninety. I'm somewhere sensible, for now."),
 ("Silke","Thirty of my sixty, and five to Rich before that. I've kept twenty-five of the first harvest of my life."),
 ("Clark","I collect it. Whatever she asks for, I'm the face they see when they hand it over. I'm noting that.")))
taxes(.50)
act("Robert Land declines to pay tax.", TH(
 ("Rob","Nothing in my booklet says I pay tax. She can send soldiers. She'd have to buy them from me."),
 ("Reina","I'm not going to fight that this year. The Warlord's tax was never in my plan."),
 ("Paddy","So he keeps all of his sixty and I keep twenty-five.")), map_hl=[8])
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="J24", hover=TH(
 ("Reina","Twenty, and it has to come first: the Wall above my province needs the Summer Palace standing. J24, the bottom corner of Province 1, by the sea. Five squares from his soldier by the shortest road, and every one of those squares is mine and pays ten."),
 ("Rob","Five squares. I can count to five."),
 ("","Reina pays the 20.")))
lot(2,"CH",[
 B(3,5),
 B(5,6,None,"Six. I need one, and there are two."),
 B(6,7,"Seven.", TH(
   ("Paddy","Seven. Customs House, Scroll, Jar: that's my set, and I'm starting with the hardest one to get, because three of us want it."),
   ("Rich","I want it too. There's another next year, and the Bowl's coming up in three lots."))),
 B(5,None,"Out.","Out. Twenty-five is what I've got for the whole year.")],
 hover="Paddy puts it on Q22, the top row of Province 6, three squares from the desert to the south.", at="Q22")
lot(3,"LD",[
 B(2,5),
 B(5,6,"Six.", TH(
   ("Silke","Six. Scroll, Customs House, Bowl. One down."),
   ("Clark","I need a Scroll. I need a Bowl as well, and I'd rather fight for the one that matters.")))],
 hover="Silke puts it on M25, in the top corner of Province 5, as far from the desert as her province goes.", at="M25")
lot(5,"DJ",[
 B(6,6),
 B(2,8,"Eight.", TH(
   ("Clark","Eight. Rich wants a Jar, Paddy wants a Jar, and there are two. I'd like one of them to be mine before they work that out."),
   ("Paddy","There's another next year. I can wait a year.")))],
 hover="Clark puts it on J13, at the bottom of Province 2, as far from the strip as his province goes.", at="J13")
lot(6,"WB",[
 B(2,5),
 B(3,6,"Six.", TH(
   ("Rich","Six. Customs House, Jar, Bowl is my set, and I'll take the cheap one while it's cheap."),
   ("Clark","Two of my three are being bought by other people at six.")))],
 hover="Rich puts it on K12, three squares from the desert in every direction. Province 3 is frontier on three sides, and that's as deep as it goes.", at="K12")
march({"W1":"F22", "W2":"S21"}, "Robert Land raids Province 1 at F22 and Province 6 at S21.", TH(
 ("Rob","Ten from the crown, five from the rice. One square nearer the palace."),
 ("Reina","Ten. Four more squares to J24, and each one is ten."),
 ("Paddy","Five. I've paid the Gentry, the Emperor and the Warlord, in that order, in my first year.")))
salaries({2:5, 6:5}, text="Reina pays Clark 5 for collecting the tax and Paddy 5 for reading the cards.")

# ============================== YEAR 2 ==============================
R(2, "Fortune and misfortune", "goodevil")
say("Paddy","Good harvest for everyone. Provinces 2, 4, 6 and 8 play a personal disaster. Nobody's in 4, so that's Clark, me and Rob.", TH(
 ("Paddy","First card of the game, and I've read myself a disaster."),
 ("Clark","A good harvest. She'll want most of it.")))
harvest()
rents()
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Clark","Four. The cheapest thing that will happen to me this year."),
 ("Rich","It's always the chariot with him.")))
disaster(6,"the only water buffalo breaks its leg in the middle of planting.", TH(
 ("Paddy","Four for the buffalo. I read the card, and the card read me."),))
disaster(8,"wounded in the legs in his last battle. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Rob","So the southern soldier stands on the square he raided last year and admires the rice. The northern one doesn't care about his legs."),
 ("Silke","A year off for me and Paddy. Province 1 doesn't get one.")))
say("Reina","Seventy per cent.", TH(
 ("Reina","Seventy of a good harvest is forty-two from each of them. I need eighty this year and eighty a year for five years after it. If I wait for the cards, the cards will have taken it first."),
 ("Silke","Forty-two. Out of sixty. After rent."),
 ("Clark","'The Emperor consistently demands taxes which are too excessive.' Cause two. One year isn't consistent. Two is.")))
taxes(.70)
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2}, hover=TH(
 ("Reina","Links 9 and 10. Eighty, all mine. Two more above my province and my strip opens; four above Clark's and four above Rich's and theirs do."),
 ("Rich","She's building the land we'll want after the population doubles, with the grain we'd have used to live until it does."),
 ("Paddy","It's a wall. I farm rice at the other end of the country."),
 ("","Reina pays the 80.")))
lot(2,"CH",[
 B(5,7), B(3,8),
 B(5,9,"Nine.","Nine. I've got thirty-four after the tax, and the Bowl comes up after this. I can't do this twice."),
 B(3,10,"Ten.", TH(
   ("Rich","Ten. Customs House and Bowl; one Jar to go."),
   ("Silke","That was the last one. Scroll and Bowl to come, and the Customs House I need is in Rich's province and Paddy's, and they both need theirs."))),
 B(5,None,"Out.")],
 hover="Rich puts it on K11, next to his Bowl.", at="K11")
lot(3,"LD",[
 B(2,6),
 B(6,8,"Eight.", TH(
   ("Paddy","Eight. Customs House and Scroll. One Jar, and there's one Jar left in the stock."),
   ("Clark","There goes my Scroll. Silke has the other.")))],
 hover="Paddy puts it on Q23, beside his Customs House.", at="Q23")
lot(5,"DJ",[
 B(6,8),
 B(3,10,"Ten."),
 B(6,11,"Eleven.","Eleven, and it's my last piece. I've got twenty and a half."),
 B(3,12,"Twelve.", "Twelve and it's my last piece too. One of us finishes today."),
 B(8,14,"Fourteen.", TH(
   ("Rob","Fourteen for a pot. Two men each one Jar from a complete set, and the Jar's sitting in front of them. I'd much rather it sat in front of me."),
   ("Rich","He doesn't need it. He doesn't need anything. He wants us not to have it."),
   ("Paddy","And that's both of us one short, for fourteen."))),
 B(3,None,"Let him have it.","I could go to fifteen. He'd go to sixteen, and he'd enjoy it. He'll sell it later. Everything Rob owns is for sale."),
 B(6,None,"I can't.","Twenty and a half, a year of rent ahead, and he'd only go higher. I can't.")],
 hover="Rob puts it on K4, deep in the desert, where nobody's soldier but his will ever walk.", at="K4")
lot(6,"WB",[
 B(2,6),
 B(5,8,"Eight.", TH(
   ("Silke","Eight. Scroll and Bowl. One Customs House, and both of them are on other people's squares."),
   ("Clark","And that's both Bowls gone. I've got a Jar and nothing else, and every piece I need has been sold.")))],
 hover="Silke puts it on M24, next to her Scroll.", at="M24")
act("All eight pieces are sold. Every province's stock is empty.", TH(
 ("","Clark has a Jar and needs a Scroll and a Bowl. Rich has a Customs House and a Bowl and needs a Jar. Silke has a Scroll and a Bowl and needs a Customs House. Paddy has a Customs House and a Scroll and needs a Jar. The spare Jar is in Rob's desert."),
 ("Rob","Two players need the one thing I own. I'd like to thank the Gentry for not going to fifteen.")), map_hl=[2,3,5,6,8])
march({"W1":"G23"}, "Robert Land's northern soldier raids Province 1 at G23. The southern one stands still.", TH(
 ("Rob","Ten from the crown. Three squares to the palace. The other one's legs are bad."),
 ("Reina","Twenty in two years. I took a hundred and sixty-eight in tax this year, so I can bear it. I'm aware that's not what the table will hear.")))
salaries({2:5, 6:5}, text="Reina pays Clark 5 and Paddy 5.")

# ============================== YEAR 3 ==============================
R(3, "A careless year", "careless")
say("Paddy","Good harvest for everyone, and every player plays a personal disaster.", TH(
 ("Paddy","Everyone. Even Rob. I read that bit twice."),
 ("Reina","A good harvest. Seventy per cent of a good harvest is another hundred and sixty-eight.")))
harvest()
rents()
disaster(1,"the Arabian horse throws her. The trainer is lashed twenty times.", TH(
 ("Reina","Four. The horse came via the Silk Route, apparently. Silke, I hope you charged for it."),))
disaster(2,"the imperial barge rams a lock gate on the new canal during his inspection. He pays for the damage himself rather than lose face.", TH(
 ("Clark","Ten for a lock gate on a canal that doesn't exist. She's built a palace and two links of wall, and I'm paying for the canal."),
 ("Rich","The card says 'a portion of the Grand Canal has been finished'. No portion has. He's going to bring that up.")))
disaster(3,"the head chef retires after forty years and is promised a house and a pension.", TH(
 ("Rich","Five for the chef. My misfortunes are all household staff."),))
disaster(5,"bandits attack her family and are beaten off by a young warrior. She raises a shrine to him.", TH(
 ("Silke","Four to a stranger with a sword. The Warlord charges five for the opposite service."),))
disaster(6,"fire takes the house and the grain reserve. He borrows to get the family through the year.", TH(
 ("Paddy","Ten. The buffalo last year and the house this year."),))
disaster(8,"a trusted lieutenant runs off with his daughter. No raids this year; he is too busy feasting the newlyweds.", TH(
 ("Rob","Five for the feast, and a year with no raids. Of all the years to be at a wedding."),
 ("Clark","A year when the Warlord can't ride. Hold that thought.")))
say("Reina","Seventy per cent again.", TH(
 ("Reina","Eighty a year for the Wall, and the cards are getting closer. I said in the Setup round what this reign would be. I meant it."),
 ("Silke","Forty-two again."),
 ("Clark","Twice. That's 'consistently'.")))
say("Clark","Before I collect it, Majesty: no. I revolt.", TH(
 ("Clark","Section 16. Anyone may revolt at any time, if two other players agree a cause exists. I've got two causes, and two peasants who've just been told to hand over forty-two of their sixty for the second year running."),
 ("Reina","Before he collects it. He waited until the number was out of my mouth."),
 ("Rob","The Official. Of course it's the Official.")))
say("Clark","Cause two: the Emperor consistently demands taxes which are too excessive. Seventy last year, seventy this year. Cause five: the Emperor cannot control the Warlord. He's never paid a bag of tax, and he's raided her own province twice.", TH(
 ("Clark","Read off the page. Every one of them has the same list in their own booklet."),
 ("Reina","Both true, both written down, and both in the service of a Wall that would have fed every one of them in five years.")))
say("Silke","Agreed. Seventy per cent is taking the harvest, not taxing it.", TH(
 ("Silke","Twenty-five of the harvest kept in Year One, thirteen in Year Two. My booklet says I revolt only if the alternative is starvation. Forty-two of sixty, twice, is how starvation starts."),
 ("Reina","She's right about the arithmetic. She's wrong about what the money was for.")))
say("Paddy","Agreed. And he raided me in Year One and nobody's done anything about it.", TH(
 ("Paddy","It feels odd, saying it out loud to her face. She appointed me. But forty-two is forty-two."),
 ("Rich","Two agree. That's all it needs.")))
say("Rich","Majesty, I'm not part of this.", TH(
 ("Rich","Not part of it, and not against it. If there's no Emperor, there's no tax, and nobody stops rent. I'll be loyal right up to the moment there's nothing left to be loyal to."),
 ("Clark","He's not part of it. He's just sitting very still and smiling.")))
act("REVOLT. Clark, Silke and Paddy stand against the throne. The price of revolt is CHAOS: no tax is declared, no salaries are paid and no public works are built until a new Emperor emerges. The harvest is still paid, the rent is still owed, and the Warlord still rides.", TH(
 ("Reina","Two years of building, two hundred and eighty-four in the reserve, and the Wall a sixth done."),
 ("Clark","Nobody pays anything to anyone in Province 1 until we've chosen who sits there."),
 ("Paddy","I have to say it: nobody pays me to read the cards either.")), map_hl=[1,2,5,6], big=True)
say("Rich","Then we'd better agree how a new Emperor emerges. The book says the most money, the most friends, the most soldiers, or any combination.", TH(
 ("Rich","I bank the pile. I'm the obvious person to propose the procedure, and the procedure is going to matter more than anything else this evening."),
 ("Clark","He's volunteering to count. Watch the counter.")))
say("Rich","I propose we count all three. Grain in hand, soldiers on the board, and friends: the players who stand behind a claim, one claim each. One qualification is enough when nobody holds another. If two people each hold a different one, it takes a combination: whoever leads in more of the three than anyone else.", TH(
 ("Rich","'One of the following.' If one man has the money and another the soldiers, 'one of' seats them both, and the throne has one chair. So a combination breaks the tie. Ties in a count mean nobody leads it. And the Emperor we've just deposed can't claim her own throne back, so her reserve isn't counted."),
 ("Rob","Fine by me. I'm the only one with soldiers."),
 ("Silke","Fine. It's the only reading where my standing behind someone means anything.")))
say("Clark","Agreed. I claim the throne.", TH(
 ("Clark","I lit it, I collect the tax, I know where the reserve is. I'd assumed I had the most grain. I should have counted before I said that."),
 ("Rich","He hadn't counted.")))
say("Rob","And so do I. Two soldiers. Nobody else has one.", TH(
 ("Rob","Most soldiers is a qualification, and I've had it since the Setup round. Nobody's bought a single soldier off me in three years."),
 ("Reina","He's claiming my throne at a table where he's never paid a bag of tax. The book lets him.")))
say("Rich","Then for the record, so do I. A hundred and twenty and a half in hand, which is more than either of you.", TH(
 ("Rich","Rent before tax, every year, and I bought two pieces cheap. Clark's got a hundred, Rob a hundred and six. I'm the richest man at the table who isn't sitting on the throne."),
 ("Clark","The landlord. I revolted, and the landlord has the money."),
 ("Paddy","Ten a year from me and Silke, three years running. That's where his lead came from.")))
say("Silke","I'm not standing behind anyone. I agreed the tax was too high. I didn't agree that any of you would make it lower.", TH(
 ("Silke","Until somebody's Emperor, nobody taxes me at all. I'd like a year of keeping my harvest before I choose who takes it."),
 ("Paddy","Same. No Emperor, no tax. I can live with that for a year.")))
say("Reina","And I won't stand behind any of you.", TH(
 ("Reina","If an acclaimed Emperor takes my seat, I get theirs: the Gentry's, or Clark's, or the desert. While nobody's acclaimed, I'm still the one sitting in Province 1. If this ends in collapse, the book says nobody wins, which is better than three of them winning and me losing. So, no."),
 ("Rob","She'd rather the country stayed broken than hand it over. I recognise that. I respect it."),
 ("Clark","She's the only player at this table with nothing to gain from an Emperor.")))
act("The first count. Most grain: Rich, 120.5. Most soldiers: Rob, 2. Most friends: nobody, because nobody has any. Rich and Rob lead one each, Clark none, so nobody leads in more than anyone else. No Emperor emerges. Chaos.", TH(
 ("Rich","One each. I'd expected that. I'd half hoped for it."),
 ("Clark","I started a revolution and came third in the count."),
 ("Rob","And here's the beauty of it. While there's no Emperor, nobody's going to stop me doing anything.")), map_hl=[3,8])
act("No auction: every province's stock is empty. The Warlord's soldiers stand still: his disaster forbids any raid this year.", TH(
 ("Rob","A wedding. The first year of Chaos, and I'm at a wedding."),
 ("Reina","The one year he can't come for me is the one year it doesn't matter.")), map_hl=[8])
act("No salaries are paid. Chaos, Year 3: no tax collected, no public work built, no salaries for Clark or Paddy.", TH(
 ("Clark","Five a year for collecting tax. There's no tax. I'd been quietly expecting this one."),
 ("Paddy","I read the card anyway. Somebody has to."),
 ("Reina","Two hundred and eighty-four in the reserve, and nothing to spend it on but myself.")), map_hl=[1,2,6])

# ============================== YEAR 4 ==============================
R(4, "The holiday", "winds")
say("Paddy","Average harvest. Everyone.", TH(
 ("Paddy","Thirty-five for each of us peasants, and nobody's going to take any of it but Rich and Rob."),
 ("Silke","Thirty-five, less five rent, and that's it. No tax. This is the first year of my life I've kept my harvest.")))
harvest()
rents()
say("Silke","Nobody's declaring a tax, then.", TH(
 ("Silke","Forty-two last year. Nothing this year. I'm in no hurry to choose an Emperor."),
 ("Rich","Thirty-five plus ten in rent, and not a bag to anyone. Chaos is the best government I've ever lived under.")))
say("Reina","There's nobody to declare it.", TH(
 ("Reina","Fifteen on an average harvest, once the court's eaten its sixty, and Rob's soldier is one step from my next square. Everyone else at this table keeps thirty-five this year. I keep five."),
 ("Clark","Every year this goes on, there's less in that reserve for whoever takes it. Including me.")))
say("Rob","Paddy. A proposal.", TH(
 ("Rob","One friend. Just one, while nobody else has any, and I lead soldiers and friends: two of three. By the Gentry's own count, that's the throne."),
 ("Rich","He's right. One friend wins it for him. Nobody move."),
 ("Paddy","Why is he looking at me?")))
say("Rob","Stand behind me and the Dragon Jar's yours. Your set's complete. And not one of my soldiers sets foot in Province 6 again.", TH(
 ("Rob","He needs the Jar. I've had it in the desert since Year Two for a moment exactly like this."),
 ("Paddy","My set. Customs House, Scroll, Jar. I'd be complete today."),
 ("Silke","And Rob would be Emperor, Reina would be the Warlord, and the tax would be whatever Rob says it is.")))
say("Paddy","You raided me in Year One, Rob. No.", TH(
 ("Paddy","It's a good offer, and I'm not overly ambitious. That's the reason. A set would get me a better chair. Rob on the throne gets every province raided by the man who collects the tax."),
 ("Rob","Worth asking. It's a long game."),
 ("Clark","Note that the only thing keeping the Warlord off the throne is a rice farmer's grudge.")))
march({"W1":"H24", "W2":"R22"}, "Robert Land moves. The northern soldier raids Province 1 at H24, two squares from the Summer Palace; the southern one raids Province 6 at R22.", TH(
 ("Rob","Ten from the old reserve and five from the rice. Nobody's going to buy a soldier to stop me, because nobody's going to be Emperor long enough to need one."),
 ("Reina","Two steps from the palace. Whoever owns this country when he gets there pays for it."),
 ("Paddy","R22 is next to my pieces. That was the 'not one of my soldiers' bit, I think.")))
act("Chaos, Year 4: no tax, no public work, no salaries.", TH(
 ("Rich","At seventy per cent I'd have handed over twenty-four and a half this year. I'm aware who's paying for my holiday."),
 ("Reina","It's me. Fifteen came in from the harvest, ten went to Rob, and no tax. Five up, in a year I'd have been a hundred up."),
 ("Clark","Nothing for the Wall. The two links stand above Province 1 and nobody's built a third.")), map_hl=[1])

# ============================== YEAR 5 ==============================
R(5, "The population doubles", "double1")
say("Paddy","Population doubles. Good harvest for everyone. Two hundred million people, and every province eats twice what it did.", TH(
 ("Paddy","Eighty for each of us now, against a good harvest of a hundred. Twenty on the best year the deck has. An average year loses five and a bad one thirty."),
 ("Reina","A hundred and twenty for Province 1, on a harvest of a hundred. Minus twenty on a good year. This is the card I taxed you for."),
 ("Rob","Forty for me, on forty. I break even and raid for profit. Same as always.")))
harvest()
rents()
say("Silke","It opens the land, though. Section 13: once the population has doubled, I can buy squares of sea. Twenty each, twenty a year back.", TH(
 ("Silke","The one thing on this board that grows with the people. I've got a hundred and twenty-five. I could buy five squares today and be a hundred better off every year."),
 ("Rich","Read the next line, Silke.")))
say("Rich","'The cost must be shared with the Emperor.' Bought in the Public Works step. There is no Emperor, and Chaos stops public works.", TH(
 ("Rich","No Emperor, no share, no land. The table agreed that reading in about four seconds, because nobody could find a hole in it."),
 ("Silke","The cure is on the table and nobody's allowed to buy it."),
 ("Reina","I could pay a share. I'm sitting in Province 1."),
 ("Clark","You're sitting in it. You're not the Emperor of it. That was the point of the revolt.")))
say("Silke","Then I want an Emperor. Rich: stand for it, and I'll stand behind you.", TH(
 ("Silke","He has the most grain, so with one friend he leads two of three. One friend is all it takes, and I'm choosing to be it, because I'd rather have a landlord as Emperor than no land."),
 ("Rich","There it is. One peasant stands up and I'm on the throne.")))
say("Rich","Gladly. And I'll promise you this, to the letter: the crown pays half of every square you buy for as long as I'm Emperor, and the canal in Province 5 is the first system I build.", TH(
 ("Rich","'System.' The Winter Palace has to come first and it isn't a system. I'll keep every word of that promise, and I chose every word."),
 ("Silke","Half of every square. That's all I wanted.")))
say("Clark","Paddy. Fifteen now, and the same promise from me, if you stand behind me.", TH(
 ("Clark","I can't win this count. I'm third in grain and I've no soldiers. But if Paddy stands behind me, friends are one each, and a tie leads nobody. Rich goes back to one of three. I don't need to win to stop him."),
 ("Rich","He's not buying a friend. He's buying a tie."),
 ("Rob","Lovely. Keep going.")))
say("Paddy","Done. I've paid Rich rent for five years. I'm not paying him tax as well.", TH(
 ("Paddy","Fifteen for standing in a particular place. I'm not overly ambitious. Nothing in my booklet says I can't be paid."),
 ("Silke","He's blocking the land he wants as much as I do, for fifteen, because he doesn't like his landlord."),
 ("Paddy","I do want the land. I'll get it next year. From Clark.")))
act("Clark Grafton pays Paddy Doyle 15 to stand behind his claim.", TH(
 ("Clark","Write it down: fifteen, Year 5, for one friend. I'm keeping receipts for this whole reign that hasn't started."),), {pid(2):-15, pid(6):15}, map_hl=[2,6], deal=True)
act("The second count. Most grain: Rich, 195.5. Most soldiers: Rob, 2. Most friends: a tie, Silke behind Rich and Paddy behind Clark, so nobody leads it. Rich and Rob lead one each. No Emperor emerges. Chaos.", TH(
 ("Rich","One friend short. The one friend Clark paid fifteen for."),
 ("Clark","I'm third in grain, I've got no soldiers and I've got exactly as many friends as the richest man in the country. That's leverage."),
 ("Reina","Two years of this, and the treasury the winner gets is down to two hundred and sixty-nine.")), map_hl=[2,3,5,6,8])
march({"W1":"I24", "W2":"Q21"}, "Robert Land raids Province 1 at I24, beside the Summer Palace, and Province 6 at Q21.", TH(
 ("Rob","Ten from the treasury, five from Paddy. One more step and the northern soldier is standing on the Summer Palace, and somebody will owe me twenty for it."),
 ("Paddy","Q21. Fifteen from Clark, five to Rob. I'm ten up on the year's politics."),
 ("Reina","Next year he takes the palace. Whoever's sitting here pays.")))
act("Chaos, Year 5: no tax, no public work, no salaries, and the first year anyone could have bought new land. Nobody did.", TH(
 ("Silke","A hundred and twenty-odd in my hands, and twenty a square for land that pays twenty a year, and I'm not allowed to buy any of it."),
 ("Rich","Every year this goes on, I'm richer and the throne's poorer. I'd like to be honest that those two facts are in tension."),
 ("Reina","Minus twenty on the harvest and ten to Rob. The reserve's down thirty, the first year it's gone down.")), map_hl=[1,5,6])

# ============================== YEAR 6 ==============================
R(6, "A bad harvest", "dribble1")
say("Paddy","Bad harvest. Everyone.", TH(
 ("Paddy","Fifty against eighty. Minus thirty for each of us, before rent. Nobody at this table makes a bag this year except Rich's rent."),
 ("Reina","Minus seventy for Province 1. The reserve pays it."),
 ("Rob","Minus twenty. I'll raid it back.")))
harvest()
rents()
act("The holiday is over. Every province's income is negative, so a tax would have collected nothing anyway; the rent still comes due; and the land, the one investment that pays, still can't be bought.", TH(
 ("Silke","Minus thirty-five with the rent, and I'll be raided before the year's out. Last year Chaos was a holiday. This year it's just a famine with nobody in charge."),
 ("Paddy","Eighty-seven and a half left. A year ago I had a hundred and twelve."),
 ("Rich","Minus twenty for me, with the rent. The first year Chaos has cost me anything. I notice I've started to want an Emperor."),
 ("Reina","A hundred and eighty-nine. It was two hundred and eighty-four the day they revolted.")), map_hl=[1,2,3,5,6,8])
say("Clark","Rich. You can't win without me, and I can't win at all. Let's talk about the price.", TH(
 ("Clark","A hundred and ten in hand, minus thirty a year on a bad card, and the treasury I revolted for has lost ninety-five while I watched. Every year I hold this tie I'm poorer and so is the throne I'm blocking. Time to sell the block."),
 ("Rich","He's been waiting for the year when his tie was worth more sold than kept."),
 ("Rob","No. No, no. Don't do this.")))
say("Clark","Twenty now. The Wall above Province 2 before anybody else's, so my strip opens first. And the crown pays twenty of the thirty for my irrigation.", TH(
 ("Clark","Written down, signed, in front of five witnesses. Rich keeps promises to the letter. So I'm writing the letter."),
 ("Rich","The Wall above Province 2 first. Not the Wall first: the Wall above Province 2 first, before the Wall above 1 or 3. I can live with that.")))
say("Rich","Done. Every word.", TH(
 ("Rich","Twenty to Clark leaves me a hundred and fifty-five and a half. Clark goes to a hundred and thirty, Rob's on a hundred and twenty-six. Still the most grain. And now the most friends."),
 ("Silke","He's checked he's still the richest before he paid. Of course he has.")))
act("Rich Baron pays Clark Grafton 20, and Clark stands behind Rich's claim.", TH(
 ("Clark","Fifteen out to Paddy last year, twenty back from Rich this year. I've made five out of the revolution, and kept my chair."),), {pid(3):-20, pid(2):20}, map_hl=[2,3], deal=True)
say("Paddy","Then I'm behind Rich too. Clark's not claiming, and I want my land.", TH(
 ("Paddy","Clark paid me to stand behind Clark. Clark's now standing behind Rich. I'm following the money, which is apparently a thing I do now."),
 ("Rich","Three friends. I didn't have one a year ago.")))
say("Rob","Most soldiers. I still claim.", TH(
 ("Rob","One of three. A man with three friends and the most grain beats a man with two soldiers and no friends. I knew that before anyone said it. I've spent three years hoping nobody would agree on anything."),
 ("Reina","He'd have had it in Year 4 for one rice farmer.")))
act("The third count. Most grain: Rich, 155.5. Most soldiers: Rob, 2. Most friends: Rich, with Silke, Clark and Paddy behind him. Rich leads in two of the three. Richard Baron is acclaimed Emperor.", TH(
 ("Rich","Three years ago I said I wasn't part of this. I wasn't. I was just standing nearest the door when it opened."),
 ("Clark","I lit the fire, I came third in the first count, and I'm the one who put him on the throne. For twenty, and a Wall."),
 ("Silke","Half of every square. He said it to the letter. I was listening to every letter.")), map_hl=[1,2,3,5,6,8], big=True)
say("Reina","I didn't stand behind anyone. I want that on the record.", TH(
 ("Reina","Province 3, the landlord's chair, sixty from the pile and a booklet that tells me to be selfish and greedy. The reserve goes to him: a hundred and eighty-nine of it. It was two hundred and eighty-four."),
 ("Rich","On the record, Majesty. Former Majesty.")))
swap(3,1,"Richard Baron takes the throne of Province 1. Reina Osorio takes Province 3: the Gentry, the Harvest Pile and the rents.", TH(
 ("Rich","A hundred and eighty-nine of reserve on top of my hundred and fifty-five and a half. My Customs House and Bowl go back to Provinces 2 and 6, to be sold again. I'm the Emperor of a country that has lost ninety-five of its treasury and three years of building."),
 ("Reina","Sixty from the pile, from my own hands now: I'm the banker. It's more than the peasants had when I taxed them."),
 ("Rob","I'd like everyone to notice that the Chaos ended without anybody doing anything about me.")), check=False)
say("Rich","Chaos is over. I declare a tax of fifty per cent.", TH(
 ("Rich","Fifty of nothing. Every income is negative this year and Note 8 says nobody pays tax on a negative income. I'm declaring it so the number is fifty and not seventy, for the record."),
 ("Silke","Fifty. Of minus thirty. I'll take it.")))
taxes(.50)
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="G18", hover=TH(
 ("Rich","Twenty. The Winter Palace has to stand before any canal in 4, 5 or 6, and I promised Silke the canal in Province 5 would be the first system. A palace isn't a system. Next year, the canal. G18, at the western end of the province, six squares from the soldier standing beside the Summer Palace."),
 ("Silke","'First system.' I heard him say it and I didn't hear what it meant."),
 ("","Rich pays the 20.")))

say("Silke","Majesty. Four squares of sea, and the crown pays half.", TH(
 ("Silke","M26, N26, O27 and P27, down the coast of Province 5. Forty of mine and forty of his, and next year they pay me eighty. He can walk on the sea like anywhere else, but his nearest soldier is four steps off and about to stand on a palace. Five a raid if he comes; twenty a year a square if he doesn't."),
 ("Rich","Half of every square. To the letter.")))
buy_land(1, ["H25", "I25", "J25", "G27"], {1:80}, "New land: Rich buys four squares of sea for Province 1, at H25, I25, J25 and G27, and pays for them alone.", TH(
 ("Rich","Province 1 eats a hundred and twenty a year and harvests a hundred on its best year. Eighty a year from the sea makes the throne pay for itself. The strip's shut to me until the last two links above my province stand, so it's the sea. His soldier on I24 is one step from three of them. He can take ten from each once. They pay twenty a year each for ever."),
 ("Reina","Eighty on the crown's own land, the year he takes the crown. I'd have done the same. I'd have done it in Year 5.")))
buy_land(5, ["M26", "N26", "O27", "P27"], {5:40, 1:40}, "New land: Silke buys four squares of sea along the coast of Province 5, at M26, N26, O27 and P27. Silke pays 40, the crown 40.", TH(
 ("Silke","Eighty a year from next year, on a province that loses five on an average harvest."),
 ("Clark","He's keeping the promise. I'm watching how he keeps mine.")))
buy_land(6, ["Q26", "R25", "S26", "T23"], {6:40, 1:40}, "New land: Paddy buys three squares of sea off Province 6, at Q26, R25 and S26, and one square of the Warlord's desert below it, at T23. Paddy pays 40, the crown 40.", TH(
 ("Paddy","Three in the sea and one on his sand. My booklet's the only one that offers both. The sea squares are four and five steps from his southern soldier, and T23 is three: if he spends a year walking to one square of desert, that's a year he isn't walking to my pieces."),
 ("Rob","He's put a field in my desert and three in the sea. I can walk on all of it."),
 ("Rich","Half of four squares. Two hundred and forty in land this year, a hundred and sixty of it the crown's, and I'm still the only one who can afford to be Emperor.")))
lot(2,"CH",[
 B(3,8,"Eight.", TH(
   ("Reina","Eight. The Gentry needs a Customs House, a Jar and a Bowl, and the Gentry may take the throne. I know where the throne is. I was sitting on it this morning."),
   ("Rich","She's bidding for my chair with sixty from the pile."))),
 B(5,10,"Ten."),
 B(3,14,"Fourteen."),
 B(5,16,"Sixteen.", TH(
   ("Silke","Sixteen, and that's my set: Scroll, Bowl, Customs House. Thirty-four and a half left, and twenty is all a seat change needs."),
   ("Reina","She'd go to thirty. I'd be left with nothing to buy the other two."))),
 B(3,None,"Take it.","Out. Sixty, and two more pieces to find, one of them in the desert. Not this year.")],
 hover=TH(("Silke","L24, the top corner of Province 5, next to the Scroll and the Bowl. Three pieces in one corner, as far from the desert as my province goes."),
          ("Paddy","Silke's complete. Clark, she's looking at your chair.")), at="L24")
say("Silke","I'm not moving yet. The sea pays me eighty next year.", TH(
 ("Silke","Complete with twenty in hand. If I take Clark's chair today, my squares stay in Province 5 and he gets their eighty a year. I can climb any year I like. I'll climb when the last work is about to go up."),
 ("Clark","She's going to farm the sea until the end and then take my seat. I'd do exactly the same.")))
lot(6,"WB",[
 B(3,6),
 B(2,8),
 B(3,10,"Ten.","Ten. Fifty left after this, and the harvest's negative."),
 B(2,12,"Twelve.", TH(
   ("Clark","Twelve. Jar and Bowl. One Scroll, and Silke has one and Paddy has the other."),
   ("Reina","Both pieces I needed, sold to other people in one round. I'm the Gentry with nothing."))),
 B(3,None,"Out.")],
 hover="Clark puts it on J14, beside his Jar at the bottom of Province 2.", at="J14")
march({"W1":"J24", "W2":"R21"}, "Robert Land's northern soldier steps onto the Summer Palace at J24; his southern soldier raids Province 6 at R21.", TH(
 ("Rob","The palace, in the first year of the new reign. Six years of walking, and the new Emperor pays for the old Emperor's palace. It doesn't count toward my objective. Palaces don't. But twenty's twenty, whoever's sitting on the throne."),
 ("Rich","Twenty, the cost of the structure. I've been Emperor for one round."),
 ("Reina","I put it there in Year One so he'd have to walk the length of my province to reach it. He did.")))
salaries({2:5, 6:5}, text="Rich pays Clark 5 for collecting the tax and Paddy 5 for reading the cards.", hover="The first salaries since Year 2. Rich keeps Paddy on as the card reader.")
act("Three years of Chaos, counted. No tax collected in Years 3, 4 or 5; no public work built; no salaries paid. Robert Land raided four squares while it lasted, and the Summer Palace in the round it ended. The imperial reserve fell from 284 to 189 before it changed hands. Nobody could buy a square of land in the year the population doubled.", TH(
 ("Reina","At seventy per cent those three years would have brought in three hundred and twenty-odd. Eight links of Wall."),
 ("Rich","And I'd be eighty poorer. Everyone at this table except the Emperor came out of Chaos richer than they went in. That's why it lasted."),
 ("Silke","Until the doubling. Then it was just the dark."),
 ("Rob","A hundred and six the day they revolted, a hundred and fifty-one tonight. I'd do it again.")), map_hl=list(ACTIVE))

# ============================== YEAR 7 ==============================
R(7, "Storms and raiders", "repairs")
say("Paddy","Good harvest for everyone. Provinces 4 to 7 pay 2 each to repair their public works, and Provinces 1, 2, 3 and 8 play a personal disaster.", TH(
 ("Paddy","Nobody's in 4 or 7. So Silke and I pay two each for works we haven't got yet, and the Emperor, Clark, Reina and Rob play disasters."),
 ("Rob","My third. Oh no. I know what my third is.")))
harvest()
say("Reina","Rents are seven.", TH(
 ("Reina","My booklet says selfish and greedy, and Section 17 says the booklet is a rule. Three years ago I was taxing them for a Wall. This year I'm charging them for the soil. They've each just been paid a hundred."),
 ("Silke","Seven. From the woman who was our Emperor twelve months ago."),
 ("Rich","I collected five for six years and never once raised it. I'm choosing to feel virtuous about that.")))
rents(7, hover="Reina's rate, from this year on. The Gentry may raise it at any time.")
act("Repairs: Silke and Paddy each pay 2 to the Harvest Pile.", TH(
 ("Silke","Two for repairs to a canal that doesn't exist. Rich says it's next on his list."),), {pid(5):-2, pid(6):-2}, map_hl=[5,6], pile_delta=4)
disaster(1,"the six-year-old Prince breaks the Empress's favourite ivory figure, five hundred years old. Several new ones are promised.", TH(
 ("Rich","Ten. I've had a Prince for one year and he's already broken something priceless."),
 ("Reina","That was my Empress's figure, technically.")))
disaster(2,"a nephew by marriage, hired to help collect the tax, loses a portion of it at Mah Jong. The family makes up the loss.", TH(
 ("Clark","Half my income. Ten. The first year there's been any tax to lose since Year 2, and my nephew's lost it."),))
disaster(3,"the house was stripped by a warlord's raid; the artisans deliver new canvasses, scrolls and carvings.", TH(
 ("Reina","Ten for art. A year in the Gentry's booklet and I'm redecorating."),
 ("Rob","She's paying for redecorating after a warlord. I'd like the credit.")))
disaster(8,"a concussion in a riding accident; while he lies in a coma, half his wealth is stolen by his own men.", TH(
 ("Rob","Half my grain. Seventy-five and a half. Three years of the best raiding this country's ever seen, and my own lieutenants took half of it while I was asleep."),
 ("Clark","The Warlord's booklet just did what four of us couldn't do in three years."),
 ("Paddy","I'm trying not to look happy. I'm not managing.")))
say("Rich","Fifty per cent.", TH(
 ("Rich","Fifty, of a good year. Silke and Paddy each made a hundred on land the crown paid half of. They each pay me fifty of it back."),
 ("Silke","Fifty of a hundred is more than seventy of sixty. I'm aware of that. I'm still better off than I've ever been."),
 ("Clark","He's taxing at fifty and nobody's revolting, because the land's paying. It was never about the rate. It was about what we kept.")))
taxes(.50)
build("Grand Canal — 2 sections each in Provinces 1, 5 and 6", 240, {1:240}, canal={1:2, 5:2, 6:2}, hover=TH(
 ("Rich","The first system, as promised, and the crown pays for every section in 5 and 6: the book says so. Province 1's two go in as well, because it's the same work, and one project a round is the only limit I can't negotiate. Twenty a year for each of the three provinces, from next year."),
 ("Silke","The canal in Province 5, the first system. To the letter."),
 ("Reina","Two hundred and forty in one year. The land pays for it. I was taxing for it before there was any land."),
 ("","Rich pays the 240.")))
buy_land(5, ["L26"], {5:10, 1:10}, "New land: Silke buys one more square of sea, at L26, beside her corner. Silke pays 10, the crown 10.", TH(
 ("Silke","One more. Five squares. I could buy more, and the crown couldn't pay its half."),
 ("Rich","After the canal I've got sixty-four and a half. Half of every square. I can afford half of two.")))
buy_land(6, ["T25"], {6:10, 1:10}, "New land: Paddy buys one more square of sea, at T25, off the bottom corner of Province 6. Paddy pays 10, the crown 10.", TH(
 ("Paddy","The sea this time. One square of desert is a test. Two would be a gift. He can walk on the sea too, but at least it isn't his."),
 ("Rob","He's learning. Slowly. One square a year, like my soldiers.")))
march({"W1":"J23", "W2":"S22"}, "Robert Land raids Province 1 at J23 and Province 6 at S22.", TH(
 ("Rob","Half my grain gone, and I'm still raiding. Ten from the Emperor, five from Paddy. S22 is one step from his first desert square."),
 ("Rich","Ten. He's walking along the bottom of my province one square a year."),
 ("Paddy","One step from T23. I can see where he's going.")))
salaries({2:5, 6:5}, text="Rich pays Clark 5 and Paddy 5.")

# ============================== YEAR 8 ==============================
R(8, "The Emperor's share", "share")
say("Paddy","Average harvest. Every province with a public work splits the extra harvest it produces with the Emperor, fifty-fifty.", TH(
 ("Paddy","My canal's twenty. Ten of it to Rich. The land isn't a public work, so the land's all mine."),
 ("Rich","The canal I paid two hundred and forty for pays me back forty this year, counting my own twenty. I'll take it.")))
harvest()
rents(7)
act("The Emperor's Share: Silke's canal and Paddy's canal each pay Rich half their extra harvest, 10 each.", TH(
 ("Silke","Ten of my twenty. He built it with his own grain, and the book says so. Fair."),
 ("Clark","No public work in Province 2 yet, so nothing to share. For the first time in this game, I'm glad of it.")), {pid(5):-10, pid(6):-10, pid(1):20}, map_hl=[1,5,6])
taxes(.50)
say("Clark","Majesty. The Wall above Province 2, before anybody else's. It's written down.", TH(
 ("Clark","The year it's due, and I'm asking in front of everybody. Four links, a hundred and sixty. I'll pay forty: the deal says the crown builds it first, not that the crown pays for it all."),
 ("Rich","I'm keeping it to the letter, and the letter didn't say who pays. He's noticed. He's offering forty before I can ask for eighty.")))
build("Great Wall — 4 links above Province 2", 160, {1:120, 2:40}, wall={2:4}, hover=TH(
 ("Rich","Links 5 to 8. The Wall above Province 2 before anybody else's, including mine."),
 ("Clark","My strip's open. Four links, and the land under them is mine to develop the day they stand."),
 ("Reina","Six links of Wall now, and four of them are Clark's. I built the first two.")))
buy_land(2, ["F12", "F13", "F14"], {2:45, 1:15}, "New land: Clark buys three squares of the strip below the Wall, at F12, F13 and F14. Clark pays 45, the crown 15.", TH(
 ("Clark","Forty-five of mine, fifteen of his. He promised Silke half and never promised me anything about land. I wrote my own contract and forgot a clause."),
 ("Rich","Five a square for Clark. I'm entirely within the letter."),
 ("Rob","The strip. My northern soldier's on the other side of the country, and walking.")))
say("Silke","Two more squares of sea for me, Majesty, and two for Paddy. Half each, as promised.", TH(
 ("Silke","A hundred and six in hand. I could pay all of my half twice over."),
 ("Paddy","Same. I've got a hundred and twenty-two and nowhere better to put it.")))
say("Rich","Half of every square you buy, as promised. This year I can't pay the half, so this year you don't buy.", TH(
 ("Rich","Seventy-nine and a half, and two salaries and a raid still to come. Forty for their four squares leaves me nothing if the next card is a bad one. I promised half of every square they buy. I never promised they could buy one whenever they liked. To the letter."),
 ("Silke","He's right. I listened to every word of it and I didn't hear that one."),
 ("Clark","Welcome to the contract, Silke.")))
march({"W1":"I22", "W2":"T23"}, "Robert Land's northern soldier raids Province 1 at I22; the southern one steps onto Paddy's new land at T23 and raids it.", TH(
 ("Rob","Paddy's field in my desert. It's part of his province now, the book says, so it pays like his province. And ten from the Emperor."),
 ("Paddy","Five. Two years walking to one square of desert, and five for it. I said it was a test. I'm not sure who passed."),
 ("Rich","He's walking west along my province now, ten a square, and every square he leaves behind is one he can never raid again. I'll let him walk.")))
salaries({2:5, 6:5}, text="Rich pays Clark 5 and Paddy 5.")

# ============================== YEAR 9 ==============================
R(9, "The Wall is breached", "breach")
say("Paddy","Good harvest for everyone. Three links of the Wall are breached: Provinces 1, 2 and 3 pay 5 each for repairs, or 2 to the Harvest Pile if there's no wall above them. Provinces 4 to 8 play a personal disaster.", TH(
 ("Paddy","And that's me, Silke and Rob for disasters. My third one is half of this year's income. On the best year I've ever had."),
 ("Reina","No wall above Province 3, so I pay two. The cheapest thing that's happened to me since Year 3.")))
harvest()
rents(7)
act("Repairs to the Wall: Rich and Clark pay 5 each; Reina, with no wall above Province 3, pays 2 in damages. All of it goes to the Harvest Pile.", TH(
 ("Clark","Five to repair a wall that was finished eleven months ago."),
 ("Rich","Five for mine. Two links above Province 1, and both of them Reina's.")), {pid(1):-5, pid(2):-5, pid(3):-2}, map_hl=[1,2,3], pile_delta=12)
disaster(5,"a flash flood washes away the irrigation ditch she and her sons built over the years.", TH(
 ("Silke","Ten. I've got a canal and five squares of sea now. I'll dig the ditch again."),))
disaster(6,"he inherits a large debt as head of the family, and pays half the year's income to settle it.", TH(
 ("Paddy","Half of a hundred and forty. Seventy. Four years ago a hundred and forty would have been a dream, and today half of it goes to a dead uncle."),
 ("Rob","Seventy. The second-biggest disaster of the game, after mine, and it was a rice farmer. The land's made him worth robbing.")))
disaster(8,"wounded in the legs in his last battle. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Rob","My southern soldier's standing on Paddy's desert and can't touch the next square. The northern one doesn't care."),))
taxes(.50)
say("Rich","Six links. The four above Province 3 and the last two above mine. The whole Wall.", TH(
 ("Rich","Two hundred and forty, one project. Reina, the Gentry's share of the Wall above Province 3 is negotiable. I'm proposing forty."),
 ("Reina","Forty, for land below it that opens the minute it's built. I'd have asked Rich for eighty, when I sat where he does. Forty.")))
build("Great Wall — the last 6 links, four above Province 3 and two above Province 1", 240, {1:200, 3:40}, wall={3:4, 1:2}, hover=TH(
 ("Rich","Links 1 to 4, and 11 and 12. Twelve of twelve. Reina started the Wall in Year 2, I finished it in Year 9, and there were three years in between when nobody was allowed to lay a stone."),
 ("Reina","The thing I was taxing them for. It's finished, and it's his."),
 ("Clark","Every strip on the map is open now.")))
buy_land(3, ["G10", "G11"], {3:30, 1:10}, "New land: Reina buys two squares of the strip below the Wall, at G10 and G11, above Province 3. Reina pays 30, the crown 10.", TH(
 ("Reina","Forty for the Wall, thirty for the land under it. I'm a landlord with land."),
 ("Rich","Five a square, to the former Emperor. I'm told that's generous.")))
buy_land(2, ["F15", "F16"], {2:30, 1:10}, "New land: Clark buys two more squares of the strip, at F15 and F16. Clark pays 30, the crown 10.", TH(
 ("Clark","Five squares. A hundred a year from my strip, and I'm the man who blocked it for a year."),))
march({"W1":"I21"}, "Robert Land's northern soldier raids Province 1 at I21, crossing the Grand Canal to get there. The southern soldier stands still.", TH(
 ("Rob","Five to Rich for crossing his canal, ten from Rich for the raid. Five a year for walking into the most expensive province on the board."),
 ("Rich","The canal I built pays me a toll for the raid on me. I'm choosing to call that a discount.")))
salaries({2:5, 6:5}, text="Rich pays Clark 5 and Paddy 5.")

# ============================== YEAR 10 ==============================
R(10, "The Canal Gives Way", "canal")
say("Paddy","The Canal Gives Way. Average harvest. All unfinished canal work is lost. Where both sections in a province are finished, that province pays the Emperor 2. Provinces 2, 3, 7 and 8 play a personal disaster.", TH(
 ("Paddy","All unfinished canal work. There isn't any. He built all six sections in one year. So the card costs me two, Silke two, and nothing gives way."),
 ("Rich","If I'd built them one section at a time, the way the money told me to, this card would have taken the half-finished ones. I'm going to take some credit for that."),
 ("Reina","My third disaster. Half my grain.")))
harvest()
rents(7)
act("The Canal Gives Way: both sections stand in Provinces 5 and 6, so Silke and Paddy pay Rich 2 each. Province 1's canal is the crown's own. Nothing is lost.", TH(
 ("Silke","Two for a canal that didn't give way."),), {pid(5):-2, pid(6):-2, pid(1):4}, map_hl=[1,5,6])
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Clark","Four. The chariot again. Back to the start of my booklet."),))
disaster(3,"floods, banditry and hungry peasants: bandits break into the warehouses and carry off half the grain.", TH(
 ("Reina","Half of everything I've got, to bandits, because the peasants of my province are starving. My peasants aren't starving. They've got canals and the sea. The booklet doesn't care."),
 ("Silke","She raised my rent to seven and the booklet sent bandits. I didn't do anything. I'd like that recorded."),
 ("Rich","It's in the Gentry's booklet. I spent six years in that chair waiting for it and it never came.")))
disaster(8,"a trusted lieutenant runs off with his daughter. No raids this year; he is too busy feasting the newlyweds.", TH(
 ("Rob","Another wedding. A different daughter, I hope."),))
say("Rich","Forty per cent.", TH(
 ("Rich","Down from fifty. The works left are the irrigation, the Reservoir and the Pagoda: a hundred and thirty, and three rounds to build them in, one a round. I don't need fifty. My booklet says just and reasonably compassionate now, and Section 17 says the booklet is a rule."),
 ("Clark","He's lowering the tax. The Gentry who smiled through the revolt is lowering the tax."),
 ("Paddy","Forty. In Year 3 it was seventy and I revolted.")))
taxes(.40)
say("Clark","Majesty. The irrigation system, with the crown paying twenty of the thirty. It's written down.", TH(
 ("Clark","Second clause of the deal, collected. I kept the paper from Year 6."),
 ("Rich","Every word.")))
build("Province 2 Irrigation System", 30, {1:20, 2:10}, key="irr2", at="H14:H15", hover=TH(
 ("Clark","H14 and H15, in the middle of my province, away from the strip and away from my pieces. Ten a year from next year, and a toll on anything of Rob's that steps on it."),
 ("Rich","Twenty of the thirty. To the letter."),
 ("","Cost split: Rich 20, Clark 10.")))
say("Reina","As the Gentry, I bank the Harvest Pile. For the record: it's down to eight hundred and twenty-five.", TH(
 ("Reina","It was twenty-five hundred at the start of the game. At the end of Year 6 it was over nineteen hundred: that year every harvest was negative and paid into it, and so did every square of land we bought. Now it pays out four hundred a year to people who own land. The pile is what's paying for the recovery."),
 ("Rich","And there are two rounds left to pay. It'll hold. I've done the sum."),
 ("Paddy","The bank is the only thing in the country getting poorer. I don't mind.")))
march({"W1":"J20", "W2":"S22"}, "Robert Land's soldiers walk without raiding: the northern one steps out of Province 1 into empty Province 4 at J20, the southern one back onto a raided square at S22.", TH(
 ("Rob","No raids this year, so I'm repositioning. Province 4's empty: I can walk through it without paying anyone. Silke's corner is four steps from J20."),
 ("Silke","Four steps, and there are two works left to build. He'd need four years."),
 ("Paddy","And the other one's walking back toward my pieces.")))
salaries({2:5, 6:5}, text="Rich pays Clark 5 and Paddy 5.")

# ============================== YEAR 11 ==============================
R(11, "A bad harvest", "dribble2")
say("Paddy","Bad harvest. Everyone.", TH(
 ("Paddy","Fifty against eighty, the same card as Year 6. That year every province at this table lost money. This year, with the land and the canal, I make ninety."),
 ("Silke","Ninety for me too. In Year 6 this card cost me thirty-five."),
 ("Rob","Minus twenty for me. I'm the only one at the table this card still hurts. I'd like some sympathy.")))
harvest()
rents(7)
act("Every province but the Warlord's has a positive income on a bad harvest: the land, the canals and the irrigation carry them.", TH(
 ("Clark","Eighty, with five squares of strip and the irrigation. The same card in Year 6 cost me thirty."),
 ("Reina","Ten. Two squares of strip and no Reservoir yet. The worst income at the table, after Rob's, and it's the Gentry's."),
 ("Rich","Thirty for Province 1. The sea pays the court's dinner now.")), map_hl=[1,2,3,5,6])
say("Rich","Thirty per cent.", TH(
 ("Rich","Down again. Two works left, the Reservoir and the Pagoda, a hundred between them. I've got two hundred and ninety-two and a half. The tax is to pay the court, now, not to build."),
 ("Silke","Thirty. The lowest rate of the game, five years after the Dark Ages ended."),
 ("Clark","Reina asked for seventy to build the Wall before the cards came. He's asking for thirty because the Wall's built. Same reign, really. Different end.")))
taxes(.30)
say("Rich","The Province 3 Reservoir. Reina, the Gentry's share is negotiable.", TH(
 ("Rich","Eighty, and twenty a year to Province 3 forever. I'll offer sixty from the crown."),
 ("Reina","Twenty from me, for twenty a year. If I were still sitting where he is, I'd have asked for forty.")))
build("Province 3 Reservoir", 80, {1:60, 3:20}, key="res3", at="L10:M12", hover=TH(
 ("Reina","L10 to M12, in the west of Province 3, between the desert and the middle of the province. Three reservoirs, four canals and a thousand miles of ditches, and any soldier of Rob's that steps on them pays me five."),
 ("Rich","The cut-out I made in the Setup round. I never got to build it from that chair."),
 ("","Cost split: Rich 60, Reina 20.")))
march({"W1":"I20", "W2":"R23"}, "Robert Land's northern soldier steps back across the river into Province 1 at I20 and raids it; the southern one raids Province 6 at R23, one step from Paddy's pieces.", TH(
 ("Rob","Five to Rich for the river, ten from Rich for the raid. And R23 is one step from Paddy's Customs House and his Scroll. Next year, one of them is mine."),
 ("Paddy","One step. Next year."),
 ("Silke","There's one work left after this one, and it's the Pagoda. Next year's march may never come.")))
salaries({2:5, 6:5}, text="Rich pays Clark 5 and Paddy 5.")

# ============================== YEAR 12 ==============================
R(12, "Heaven has favourites", "heaven")
say("Paddy","Heaven has favourites. Good harvest for Provinces 2, 4 and 5. Bad for 1, 3, 6, 7 and 8.", TH(
 ("Paddy","Bad for me. Still ninety, with the land."),
 ("Silke","Good for me, and good for Clark. Which matters, this year.")))
harvest()
rents(7)
say("Reina","The Harvest Pile has a thousand and fifteen in it. It paid out four hundred this harvest.", TH(
 ("Reina","I bank it, so I'm the one who says it. Two more harvests like this one and the pile couldn't pay a third. The land rush has been paid for by the bank, and the bank is running down."),
 ("Rich","Then it's a good thing this is the last year."),
 ("Silke","Twenty-five hundred at the start. A thousand now, and four hundred a year going out. Somebody should be counting."),
 ("Reina","Somebody was.")))
say("Rich","Thirty per cent. And then the Marble Pagoda, and every work this country owes is standing.", TH(
 ("Rich","Twenty for the Pagoda, the last of eight hundred and ninety. The book says the game ends when they're built. I'd like everybody to do whatever they're going to do before I build it."),
 ("Reina","He's warning the table that the clock stops this round. Generous. Also true."),
 ("Clark","Everybody's looking at Silke.")))
taxes(.30)
say("Rob","Paddy. The Dragon Jar. Forty, and you're complete.", TH(
 ("Rob","My soldier's one step from his Scroll, and the game ends before I march. After the Pagoda goes up, that Jar's worth nothing to me at all. Forty for a piece I paid fourteen for in Year Two. The last thing I'll ever sell anyone."),
 ("Paddy","He offered it to me in Year 4 for the throne. Now he wants forty.")))
say("Paddy","No thank you, Rob.", TH(
 ("Paddy","With the Jar I'd take Clark's chair, or Silke's after she moves. Province 6 has five squares of land, a canal and ninety a year in a bad harvest. I came here a rice farmer, I'm still a rice farmer, and I've got three hundred in hand. I'm not overly ambitious. It says so in the booklet, and for once I agree with it."),
 ("Rob","Twice. He's turned me down twice. I'd respect it if it weren't so expensive."),
 ("Rich","Three hundred and two in hand, and he's turning down a seat change. I've never understood Paddy, and I collected his rent for six years.")))
say("Silke","Then it's my turn. Clark: I've held a complete set since Year 6.", TH(
 ("Silke","Scroll, Bowl, Customs House, and twenty in hand. Six years on the sea while the land paid. My booklet lets me replace the Gentry or the Official. Two is higher than three, and Clark taught me what a contract is."),
 ("Clark","Six years she's been complete and smiling at me. I'd have done exactly the same. I'm still not going to enjoy it."),
 ("Reina","She's choosing Clark over me. I'm not sure whether to be relieved or insulted.")))
swap(5,2,"Silke Weber declares a complete set and replaces Clark Grafton. Silke becomes Official of Province 2; Clark becomes Silk Peasant of Province 5.", TH(
 ("Silke","The Customs House goes back to Province 2's stock, since it's native to my new seat. I keep the Scroll and the Bowl, on J13 and J12, where Clark kept his pieces, and I take every bag Clark is holding. Silk farmer to tax collector."),
 ("Clark","Sixty from the pile, five squares of Silke's sea, a canal, and a booklet that says I'm simple and hard-working. I lit the revolt in Year 3. I'd like that on the record too."),
 ("Paddy","She left him the land, the canal and the sea. He's the best-off Silk Peasant this country has ever had.")),
 at={"LD":"J13", "WB":"J12"})
say("Clark","I suppose I'll pay Reina the rent.", TH(
 ("Clark","Seven a year to the woman I deposed. She'll enjoy that, and there isn't going to be a next year to collect it in."),
 ("Reina","I'd have raised it to ten for you.")))
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="H18", hover=TH(
 ("Rich","H18, at the western end of the province beside the Winter Palace. The last twenty. Every public work owed at this table: three palaces, twelve links of the Great Wall, six sections of the Grand Canal, the irrigation system and the Province 3 Reservoir."),
 ("Reina","Eight hundred and ninety. I paid a hundred of it as Emperor and sixty as the Gentry."),
 ("","Rich pays the 20.")))
act("Every public work is built. The game ends in survival: the nation has fed itself, and the Emperor's reign has been a glorious one, though it isn't the reign that started it.", TH(
 ("Rich","Glorious, the book says. Nine years ago I was the landlord who said he wasn't part of the revolt."),
 ("Reina","I taxed them to build it before the cards came, and they revolted. Then the cards came, and nobody could build anything. Then he built it with land that only existed because the cards came. I was right about everything except the people."),
 ("Rob","Two soldiers, twelve years, a palace, and fifty in grain after my lieutenants took their half. I never entered the social order. I'll be back."),
 ("Paddy","I read every card in this game. The last one said heaven has favourites. It's the first one I've agreed with.")), map_hl=list(ACTIVE), big=True)

RESULT = export(
 "Every public work was built in Year 12, the survival ending. Players are ranked by the province they finished in against the one they drew.",
 ["Reina Osorio taxed hard from the first year to build the Great Wall before the population came, and the table revolted in Year 3 over the rate. The revolt cost the country three years: no tax, no salaries and no public works, while the harvest, the rent and the Warlord went on as before. For the two years before the population doubled, Chaos was a holiday for everyone but the throne, and that was why it lasted.",
  "Nobody could win the acclamation. The table counted grain, soldiers and friends, and a claim needed more of them than any rival's. Rich had the most grain from Year 3, and Rob had the only soldiers. Reina refused to back anyone, so that she would at least not lose to one of them; the peasants refused while there was no tax to pay; and when the doubling came and the land could not be bought without an Emperor, Clark paid Paddy to keep the friends tied. It ended in Year 6, after a bad harvest, when Clark sold his support to Rich for twenty and two promises.",
  "Rich kept every promise to the letter, and the recovery ran on new land: the crown paid half of every peasant's square and all of the canals, and the tax that land paid built the rest of the Wall. The imperial reserve that Rich inherited had fallen from 284 to 189 during Chaos. By Year 11 a bad harvest left every province but the Warlord's in profit. The Harvest Pile paid for it: it fell from over nineteen hundred at the end of Year 6 to 975 at the end of the game, paying out four hundred a year once the land came in, and it had two more harvests like the last left in it.",
  "Silke Weber completed her set in Year 6 and waited six years on the land before taking Clark's chair in the last round. Paddy Doyle twice refused the Dragon Jar that would have completed his: once in Year 4, when it would have put the Warlord on the throne, and once at the end, because he didn't want to move. Robert Land finished where he started, which is all a Warlord can do without his objective."])
