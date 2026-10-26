# Game 1 — the full game. Eight players, twelve years, ends in revolt.
setup([1,2,3,4,5,6,7,8], "full", "The full game",
      "Eight players · twelve years · ends in revolt",
      "All eight provinces. The Emperor builds palaces and a wall, the peasants' reservoir never comes, and a wheat farmer counts the deferrals out loud until the table agrees with him.", short="8 players · 12 years")

# ============================== SETUP ==============================
R(0, "Eight strangers to the box", None, "All eight provinces (rulebook Section 4 and Appendix A): four pieces of realia each, the Warlord with four soldiers and forty raid squares, and every public work in the book owed to someone. Nobody at the table has played before.")
act("Eight booklets, closed, shuffled and fanned out face down. Each player draws one and reads it alone.", TH(
 ("Reina","Province 1. The Emperor. 'Just and benevolent.' Every booklet but mine has a section headed 'How to replace the Emperor.'"),
 ("Rob","Province 8. I've read the first paragraph three times. 'You are a cruel, vicious villain.' I've never been so happy to be cast."),
 ("Graham","Wheat. 'Simple and hard-working.' I'm going to need a minute.")), map_hl=list(range(1,9)))
say("Rich","I'm the Gentry. I bank the Harvest Pile, apparently, and collect rent from all three of you.", TH(
 ("Rich","Say it warmly. The peasants are going to hand me money every year; it's better if they like doing it."),
 ("Paddy","He said 'all three of you' and looked straight at me.")))
act("Rich sets out the Harvest Pile in stacks, where everyone can see it: twenty-five hundred million in bags of eight sizes.", TH(
 ("Rich","Forty halves, fifty ones, forty twos, fifty fives, twenty tens, twenty twenties, ten fifties, ten hundreds. I counted it twice. Nobody asked me to."),
 ("Clark","He's the only one of us who's touched the money. Noted.")), map_hl=[3])
deal_grain("Rich deals 60 to each player from the pile. That's the first year's harvest.", TH(
 ("Rich","Four hundred and eighty out before anyone's done anything. The pile will feel that later."),
 ("Silke","Sixty. My booklet says a good harvest is a hundred and my family eats forty. So this is good. Is this good?")))
take_stock("Each of the six realia provinces takes its four pieces out of the box: Customs Houses, Scrolls, Brushes, Jars, Bowls and Vases. They wait beside the board until they're auctioned.", TH(
 ("Noah","Twenty-four pieces and everybody needs five of them, one of every kind but their own. There are four of each kind and five people who want one. Somebody always goes short."),
 ("Rob","Beside the board, not on it. So I can't raid any of it until somebody buys it and puts it down. I'll wait.")))
act("Noah shuffles the twenty I Ching cards and lays them face down. Nobody looks; the first card is turned in Year 2.", TH(
 ("Noah","I read them, I keep the population count. 'The population is the clock' is the most underlined sentence in my booklet."),
 ("Reina","Twenty cards, and I don't get to see any of them before the Scholar does.")), map_hl=[4])
act("Clark, Rich and Graham each cut a paper outline for their province's system: the irrigation system for Province 2 at one square by two, the reservoir for Province 3 at two by three, and the reservoir for Province 7 at two by two. They're set aside until they're built.", TH(
 ("Graham","Two by two. One large reservoir, two canals, five hundred miles of ditches. I'm holding it like a ticket."),
 ("Rich","Two by three. Mine's the biggest system in the book. I'm choosing to read something into that."),
 ("Clark","One by two. Mine's the cheapest. Which means it's the one that gets built.")), map_hl=[2,3,7])
place_army({"W1":"O18", "W2":"T18", "W3":"F16", "W4":"J8"}, "Robert Land stands his four soldiers on undeveloped land: O18, in the notch between Provinces 4, 5 and 7; T18, below the wheat and rice fields; F16, in the strip under the Wall at the corner of Provinces 1 and 2; and J8, on the western edge of Province 3.", TH(
 ("Rob","One square a round, the booklet says, even mine. So I'm putting one beside every door. The notch opens onto silk and wheat; the south onto rice; the strip onto the Official and the throne; the west onto the Gentry."),
 ("Silke","The notch is the only way into my province from his desert, and he's put a man in it before anybody's sold a single pot."),
 ("Reina","F16 is one step and a river from my province. I haven't built anything yet and he's already standing at the gate.")))
say("Rob","Gentlemen. Majesty. Silke. Shall we?", TH(
 ("Rob","I've got four soldiers, no tax to pay and a booklet that calls me a villain in the first line. This is going to be a wonderful evening."),
 ("Graham","He's the only one of us who knew what he was before he sat down.")))

# ============================== YEAR 1 ==============================
R(1, "The first year", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
rents()
say("Reina","Thirty per cent. I'd rather ask small and often than large and once.", TH(
 ("Reina","Low. Deliberately low. I've got a thousand million of building ahead of me and no earthly way to pay for it, so the only thing I can actually bank right now is goodwill. Cash it in around year six."),
 ("Rich","Thirty. Sweet of her. She'll be at sixty inside five years and she'll have forgotten she was ever reasonable."),
 ("Graham","Fine by me. Ask me again when I've got nothing.")))
say("Clark","Modest and just, Majesty. I'll collect it personally.", TH(
 ("Clark","Personally, obviously. You learn a fortune watching people count out eighteen million — who hesitates, who's got a second pile, who looks at Rob when they say the number."),
 ("Noah","He's going to skim. Everyone knows he's going to skim. His card practically instructs him to. Somehow that makes it worse.")))
say("Silke","He said 'personally' the way a man says 'privately.'")
say("Clark","I heard that, Silke Weber.",
 "I did hear it. And I'm filing it, because in about nine years she is going to be somebody and I would like to have been charming.")
taxes(.30)
act("Robert Land declines to pay tax.", TH(
 ("Rob","Nothing in my booklet says I pay tax. And it's year one — if she can't make me now, she never can. Cheapest precedent I will ever buy."),
 ("Reina","And there's my first problem, eleven minutes in. My only lever against him is soldiers, and the only shop that sells soldiers is him."),
 ("Clark","Noted. Filed. I'll be bringing this up in about ten years.")), map_hl=[8])
say("Rich","I'd lend you a soldier, Majesty, if I had one. Or a spine, if I had a spare.",
 "Joking on the surface, marking territory underneath. If she ever does buy an army she'll buy it with my tax, and I'd rather she thought of me as an ally than as a source.")
say("Paddy","We could all just... not pay him?",
 "Genuine question. Genuinely nobody answers it. That is how I learn what kind of table this is.")
say("Rob","Send someone to collect it.", TH(
 ("Rob","Please. Please send someone."),
 ("Silke","He's enjoying this far too much for a man in a desert.")))
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="J23", hover=TH(
 ("Reina","J23, at the bottom of my province, five squares from the strip. If I'm building palaces first, I'm building them where he has to walk the length of the country to reach them."),
 ("Rob","Five squares. Noted."),
 ("","Reina pays the 20.")))
say("Graham","Palaces first, is it?", TH(
 ("Graham","Three palaces at twenty each before anybody gets a ditch. I'm not going to make a scene in year one. I am going to remember."),
 ("Reina","He's counting. I can hear him counting.")))
lot(2,"CH",[
 B(3,6,"Six. Somebody has to start.", TH(
   ("Rich","I don't want a Customs House. I want everyone thinking in sixes before I put my own Scrolls up in ninety seconds. An anchor's cheaper than a bid."),
   ("Paddy","Six? For that? ...oh. Oh, he's setting the price for his own lot. Clever swine."))),
 B(4,7,None,"Seven and I'll stop. Four of these exist and I'd like one eventually, but my income is the worst at this table and there are three more coming."),
 B(6,8,"Eight.","Overpaid, year one, in front of everybody. But four exist and five of us need one, and I'd rather learn that now than in year eight when it's thirty."),
 B(3,None,"Out.","Anchor set, no money spent. Perfect round.")],
 hover='Paddy puts it on Q24, on the sea side of the rice fields, three squares from the desert to the south.', at='Q24')
lot(3,"LD",[
 B(7,4,"Four.","Cheap and early. I want a Scroll and I'd rather buy it before anybody works out how tight the supply is."),
 B(5,5),
 B(2,6,None,"Six, and I'm bidding against a silk farmer. This is not a fair fight and I'm not pretending it is."),
 B(5,7,"Seven, and that's my limit for this one.", TH(
   ("Silke","Seven's where I stop. I've got thirty-seven and four years of lots to buy out of it, and the man bidding against me collects everyone's tax."),
   ("Clark","Eight would make her think. I'll keep that in my pocket for a year when it matters more.")))],
 hover='Silke puts it on M25, in the top corner of Province 5. Seven squares from the notch, which makes it the deepest square on the board.', at='M25')
lot(4,"BB",[
 B(6,3), B(7,4),
 B(3,5,"Five.","I'll take a Brush at five. Note that I've now bid on two lots and won none — I'm not collecting so much as keeping everyone else's prices honest."),
 B(7,6,"Six.","Six. I have five pieces to gather and a reservoir that doesn't exist; I need this game to move fast for me.")],
 hover='Graham puts it on Q15. Province 7 touches the desert on three sides; Q15 is two squares from the nearest of them, which is as deep as his province goes.', at='Q15')
lot(5,"DJ",[
 B(3,5), B(2,7),
 B(4,9,"Nine. In year one.", TH(
   ("Noah","Steep and I paid it anyway. I'm the Scholar — worst income, best information. I read the cards. The population is going up and grain is about to stop meaning what it means today."),
   ("Silke","Nine for a jar. Mine. I get a quarter of that and I'm still annoyed.")))],
 hover='Noah puts it on K24, the far corner of Province 4: six squares from the notch, and the sea behind it.', at='K24')
lot(6,"WB",[
 B(5,4), B(2,6,"Six.","Six for a bowl I need, from a rice farmer, in the year I'm collecting everyone's taxes. I do enjoy this seat.")],
 hover='Clark puts it on J14, at the bottom of Province 2, as far from the strip under the Wall as his province goes.', at='J14')
lot(7,"VA",[
 B(4,5),
 B(3,8,"Eight, and I'm done for the year.","Eight for a Vase and that's my only buy — one anchor, one win. The Gentry's advantage isn't income, it's that I bank the pile and everyone forgets I'm counting it.")],
 hover='Rich puts it on J17, in the little arm of Province 3 that reaches east. Three squares from any desert.', at='J17')
march({"W1":"O19", "W2":"S19"}, "Robert Land raids Province 5 at O19 and Province 6 at S19.", TH(
 ("Rob","The two soldiers already standing on the peasants' doorsteps. Five each. The other two can wait for richer doors."),
 ("Silke","O19. The first square inside the notch. He was there before the first lot."),
 ("Paddy","Five. That's the first five I've lost to anyone who wasn't the Gentry.")))
salaries()

# ============================== YEAR 2 ==============================
R(2, "Rain and flood", "rainflood")
harvest()
rents()
say("Rich","You could always sell a book.",
 "Poking the Scholar because his income is the only one I can see exactly. Five a year from the crown and the rest is weather.")
say("Noah","I could sell yours. You have never opened them.")
say("Noah","Ten million, and the river took the rest. I'll be eating my salary.", TH(
 ("Noah","Income ten, salary five. A third of my living now arrives as a favour from Reina, which means I can't be the one who says the hard thing out loud. Someone else will have to."),
 ("Reina","Good. A dependent Scholar is a quiet Scholar."),
 ("Graham","He'll fold when it counts. Cross him off the list.")))
taxes(.40)
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="J24", hover=TH(
 ("Reina","J24, next to the Summer Palace. The two deepest squares in Province 1."),
 ("","Reina pays the 20.")))
say("Graham","Majesty. The reservoir. Sixty million, and your own book says the crown pays all of it.", TH(
 ("Graham","Every year, same words, until it's a revolt clause. Mine is the one public work she pays for entirely — no split, no shared blame. Each year it doesn't exist is a year that's provably hers."),
 ("Reina","He's building a case. In front of witnesses. And he's right, which is the annoying part."),
 ("Rich","Sixty million out of her pocket for a ditch in Province 7. She'll never do it. Watch.")))
say("Reina","After the Wall, Graham.", TH(
 ("Reina","Deferral one. I don't have a better answer — 480 for the Wall is the biggest line I own and it feeds nobody, but it's the only thing that opens new land for the two people who can actually pay me tax."),
 ("Graham","'After the Wall.' Say it eight more times, Majesty."),
 ("Paddy","That's the tone that gets emperors replaced.")))
lot(2,"CH",[
 B(4,8), B(7,9),
 B(4,10,"Ten.","Two of five now. I'm buying ahead of the curve on purpose — everyone else is bidding what a piece is worth today and I'm bidding what the last one will be worth in year eight.")],
 hover='Noah puts it on K23, next to his Jar in the far corner.', at='K23')
lot(3,"LD",[
 B(2,5),
 B(7,8,"Eight.","Eight, and it hurts. I'd rather be early and poor than late and one piece short — the only exit from Province 7 is a complete set.")],
 hover='Graham puts it on Q14, beside his Brush in the middle of the province.', at='Q14')
lot(4,"BB",[
 B(6,7,"Seven.","Seven and nobody pushed me. The Brushes are going cheap because Noah's selling four of them and the supply is obvious. Buy the abundant thing early.")],
 hover='Paddy puts it on Q23, beside his Customs House.', at='Q23')
lot(5,"DJ",[
 B(3,9,"Nine.","Nine, unopposed, in a year the flood put Silke on a bad harvest. Buying from a neighbour who can't bid back is the most profitable thing in this game and nobody has to say anything about it.")],
 hover='Rich puts it on J18, beside his Vase in the eastern arm.', at='J18')
lot(6,"WB",[
 B(5,4,"Four. Nobody else wants a bowl this year?", TH(
   ("Silke","Four, and I'll take it gratefully. Everyone with money is staring at Customs Houses."),
   ("Graham","I want a bowl. I also want everything else. Let her have it."),
   ("Rob","Noted: bowls are selling for four. Interesting number to be low.")))],
 hover='Silke puts it on L25, beside her Scroll in the top corner.', at='L25')
lot(7,"VA",[
 B(5,6,"Six on the Vase. That's what I can spare.", TH(
   ("Silke","Twenty-six left and a whole year of rent and tax ahead of me. Six is what I can spare without eating mulberry leaves by winter."),
   ("Clark","She's told the whole room her ceiling. Never do that."))),
 B(2,7,"Seven.", TH(
   ("Clark","Seven costs me nothing and costs her everything. I'd have gone to twenty. We are not bidding with the same money and we both know it."),
   ("Silke","One million. He beat me by one million on purpose."),
   ("Rob","Now that's proper villainy. I'm supposed to be the villain here."))),
 B(5,None,"...","I could go to eight. He'd go to nine. He's got forty-four and I've got a bad harvest.")],
 hover='Clark puts it on J15, beside his Bowl.', at='J15')
say("Rob","The Official and the Gentry this year, I think. The rich pay better.", TH(
 ("Rob","The one real bit of strategy I've got. Five million's five million from anyone, but a raided square can never be raided again — so I'm spending my supply of virgin squares on people who'll still be solvent in year ten. Never waste a raid on a peasant you intend to bankrupt."),
 ("Rich","He came for me second. I'm choosing to take that as a compliment.")))
march({"W3":"G16", "W4":"J9"}, "Robert Land raids Province 2 at G16 and Province 3 at J9.")
salaries()

# ============================== YEAR 3 ==============================
R(3, "A careless year", "careless")
harvest()
rents()
disaster(1,"the Arabian horse throws her. The trainer is lashed twenty times.", TH(
 ("Reina","Four million and out. Cheapest disaster on the table, and the only person who actually suffers in it isn't a player."),
 ("Silke","Twenty lashes for the stable hand. And she's the *compassionate* one, it says so on her card.")))
disaster(2,"the chariot drops a wheel on a garrison inspection. The driver is crippled for life; the Official pays the pension.", TH(
 ("Clark","Four million to keep a man's family fed. Put it on the ledger next to every bag I've skimmed and I come out comfortably ahead."),
 ("Noah","He'll describe this as charity for the rest of the game. Watch.")))
disaster(3,"the head chef retires after forty years and is promised a house and a pension.", TH(
 ("Rich","Every one of my three disasters is about maintaining a household. I'm the only player whose misfortunes are furniture, and honestly? Cheap at the price."),
 ("Paddy","Forty years of service and he gets a cottage. My buffalo gets nothing.")))
say("Rich","Your buffalo has not made me a soufflé, Paddy.",
 "Keeping it light. The peasants like me when I'm funny, and a landlord who is liked is a landlord who gets paid on time.")
disaster(4,"he falls asleep over his notes on the migratory habits of the swallow, and the candle takes them.", TH(
 ("Noah","Four million and a year's work. The Scholar's disasters are all about losing knowledge, which for a role whose entire job is the population counter is either poetry or a warning."),
 ("Rob","A man wrote a book about swallows and a candle read it first. I love this game.")))
disaster(5,"bandits are driven off by a young warrior; she must raise a shrine to him.",
 "Four million to a stranger with a sword. Meanwhile the actual man with swords is charging me five a raid. Different rates for the same service, somehow.")
disaster(6,"the only water buffalo breaks its leg in the middle of planting.", TH(
 ("Paddy","There it is. My buffalo did get something. It got a disaster."),
 ("Graham","Four for a buffalo. I've known worse years.")))
disaster(7,"the Emperor takes his eldest daughter into the imperial household. He must feast the village.", TH(
 ("Graham","Two million. And look who the card says took her. I'm not making a speech about it."),
 ("Reina","That's on the card, not on me. ...it is going to be on me, isn't it."),
 ("Rob","Ohh, that one's going to come back. Mark it.")))
say("Graham","A high honour, they tell me.", TH(
 ("Graham","Best line I'll get all game and it cost me two million. Worth it."),
 ("Noah","He said that very quietly. Quiet is worse.")))
disaster(8,"wounded in the legs in the last battle. No raids on Provinces 5, 6 or 7 this year.", TH(
 ("Rob","Fine. The rich provinces it is. I was going that way anyway."),
 ("Silke","A year off from him. I'll take a bandit and a shrine over a Warlord any day.")))
taxes(.40)
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="G26", hover=TH(
 ("Reina","G26, on the coast at the far end of the province. His soldier is on G16, just over the border at the other end of the same row. I'd like the row to be long."),
 ("","Reina pays the 20.")))
say("Clark","Three palaces, Majesty. No wall.",
 "Not criticising — establishing that I raised it. If this table ever votes on whether she's been just, I want a line in the transcript with my name on it.")
lot(2,"CH",[
 B(5,10), B(7,11),
 B(5,12,"Twelve. I want it.", TH(
   ("Silke","Good harvest, money for once, and I'm spending it. Three of five. A Brush and a Vase to go."),
   ("Noah","She needs a Vase as well. We need the same piece. One of us isn't getting it.")))],
 hover='Silke puts it on M24, in her corner with the others.', at='M24')
lot(3,"LD",[
 B(4,9), B(6,10),
 B(4,11,"Eleven.","Eleven. Three of five and I can see the shape of the endgame: everyone will be one piece short and the last pieces will be priced like ransom.")],
 hover='Noah puts it on K22, the third square of his corner.', at='K22')
lot(4,"BB",[
 B(2,8,None,"Eight. I need a Brush and a Scroll and I've won neither. There's another Brush next year."),
 B(3,9,"Nine.","Nine. Clark wants one too, but I collect rent before the auction and he doesn't. That's the Gentry's real edge.")],
 hover='Rich puts it on K17, under his Vase and Jar.', at='K17')
lot(5,"DJ",[
 B(7,10,"Ten on the Jar, and that's me finished for the year.","Three of five. And I can see what's left of the Customs Houses and the Bowls, and I can see who wants them. This is going to get strange.")],
 hover='Graham puts it on Q16, the other deep square in Province 7.', at='Q16')
lot(6,"WB",[
 B(3,4),
 B(8,5,"Five for the bowl. No use to me.", TH(
   ("Rob","Enormous use to me. Four Bowls exist, five of them need one, and the only spare that'll ever be loose just cost me five million while they all stared at their own sets. Ask me what it's worth in year seven."),
   ("Graham","Why does the Warlord want a bowl. ...oh no."))),
 B(3,None,"Let him have it.", TH(
   ("Rich","He can't use it, I'll pick one up next year. — I have just made the worst decision of this entire game and I will not find out for four years."),
   ("Rob","Thank you, Richard.")))],
 hover='Rob puts it on K3, deep in his own territory, where no soldier but his will ever walk.', at='K3')
lot(7,"VA",[
 B(6,8,"Eight.","Three of five, and the Vase was the easy one. The Jars are the problem — three are gone already and there's one left in the stock.")],
 hover='Paddy puts it on Q22, in the row furthest from the desert.', at='Q22')
march({"W3":"G17", "W4":"J10"}, "Robert Land raids Province 1 at G17 and Province 3 at J10.", TH(
 ("Rob","His legs keep him out of the south, so the north gets both. G17 means crossing the river, which costs me five to the Emperor, and the raid pays me ten. A five-million profit and a soldier inside the palace province."),
 ("Reina","He paid me five to come in and took ten. I've never been robbed politely before."),
 ("Rich","Two in two years, walking east across my province one square at a time. He's heading for something.")))
salaries()

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
say("Silke","Good harvest for everyone, it says.", TH(
 ("Silke","Good for one year. Harvest is fixed at 100 and my consumption just went 40 to 60. Permanently. The card gives you one good harvest and takes twenty a year forever."),
 ("Noah","And that's one of five. Three doubling cards and one more of these, and the deck stops counting at 600 million."),
 ("Reina","Nobody do the arithmetic out loud. Please.")))
say("Rob","Good. More of them to rob.",
 "Genuinely good news. My consumption is thirty against a harvest of forty — I'm the only province here that doesn't starve on arithmetic. I get poorer more slowly than everyone else, which is the same thing as getting richer.")
say("Graham","More of them to feed, you mean.")
say("Noah","One hundred and fifty million people. I'll mark the chart.", TH(
 ("Noah","I'm the only one tracking this and I want every one of them to look at it. The whole game is a countdown and I'm holding the clock."),
 ("Graham","He's frightened. Good. Frightened is recruitable.")))
harvest()
rents()
say("Reina","Fifty per cent. It's a good year, and I need the Wall started.", TH(
 ("Reina","Forty to fifty in one jump is ugly and I know it. But it's a good harvest, everyone's positive, and 480 of Wall does not get built on what I've been collecting."),
 ("Clark","Fifty. In year four. She's panicking and it's year four."),
 ("Paddy","Every point she adds is a point I can quote back at her.")))
taxes(.50)
build("Great Wall — 1 link above Province 3", 40, {1:20,2:10,3:10}, wall={3:1})
say("Rich","One link. Eleven to go. At this rate the Wall is finished in year fifteen and the game ends long before that.", TH(
 ("Rich","Saying it out loud on purpose. The survival ending is arithmetically dead and I want that established early, so that when it dies I'm holding money instead of blame."),
 ("Reina","He's not wrong. He's just wrong to say it where Graham can hear.")))
say("Reina","Then bid less on pottery and pay more tax, Richard.", TH(
 ("Reina","Snapping, which I never do, which means everyone just noticed. He's right, and being right in public is the most expensive thing anyone's done to me yet."),
 ("Clark","Ohh. She's rattled. In year four. I should decide fairly soon whose side is worth being on, and loyalty won't come into it.")))
say("Reina","Last lots. After this the stock is gone and you trade among yourselves.",
 "I don't bid — Emperors can't — so this is the one part of the game I only watch. Which is uncomfortable, because the seat I'm sitting in is the prize they're all buying tickets for.")
lot(2,"CH",[
 B(7,7), B(3,8),
 B(7,9,"Nine. I need it."),
 B(3,10,"Ten.", TH(
   ("Rich","Ten. I need it too, and I've got rent coming in that Graham hasn't. Sorry, Graham."),
   ("Graham","That was the last Customs House. Four existed. I've watched every one of them go to somebody else."))),
 B(7,None,"Go on, then.","Out. Three of five, and the last Customs House just went. I'll have to buy one back off somebody.")],
 hover='Rich puts it on K16. His four pieces now make a square in the east of Province 3, as far from the soldier on the western edge as they can get.', at='K16')
lot(3,"LD",[
 B(2,9,None,"Nine. Last Scroll in the stock."),
 B(6,10,"Ten.","Ten and I'm four of five. One Dragon Jar, and there's one Dragon Jar left in the stock."),
 B(2,None,"Ten for a scroll? Keep it.","I'll let it go. I've got a Jar to buy, and I can only fight one war a round. — That's the sentence I'll be explaining to myself in year seven.")],
 hover='Paddy puts it on Q25, at the end of his row.', at='Q25')
lot(4,"BB",[
 B(5,8,"Eight.","Eight and that's four of five. The Vase. It's always going to be the Vase."),
 B(2,None,"Let her have it.","Last Brush, too. I've now passed on the last Scroll and the last Brush in the same round. I'm aware of that.")],
 hover='Silke puts it on N25, the last square of her corner.', at='N25')
lot(5,"DJ",[
 B(6,9),
 B(2,11,"Eleven!", TH(
   ("Clark","Eleven for a nine-million piece. I need a Jar, fine — but mostly Paddy needs it more and I can watch him counting. Half the value of a bid is what it costs the other man to match."),
   ("Silke","He wanted it. He wanted Paddy not having it more."))),
 B(6,None,"I can't.","I can't. And that was the last Jar in the stock. Four years from now I'm still one short because of eleven million in year four.")],
 hover='Clark puts it on J13, beside his Bowl and Vase.', at='J13')
lot(6,"WB",[
 B(3,8,None,"Eight. Last year I said I'd pick one up next year. This is next year."),
 B(7,None,"Not me.","I need a Bowl too. But the Customs Houses are gone, so a Bowl gets me four of five and no further. I'm not paying to be one short in a different way."),
 B(4,9,"Nine.","Nine, four of five, and the missing one is a Vase. There's one Vase left in the stock and the man with the spare bowl is looking at it."),
 B(3,None,"...","And there went my bowl. Four existed. One of them is in a desert.")],
 hover='Noah puts it on L23, below the rest of his corner.', at='L23')
lot(7,"VA",[
 B(5,8), B(4,10), B(5,12,"Twelve."),
 B(8,20,"Twenty. For a pot.", TH(
   ("Rob","Noah and Silke both need it, and they've just spent the round bidding against each other. Twenty from a man with a hundred and fifteen is a rounding error. That's both spares. I'm not collecting realia — I'm collecting other people's endings."),
   ("Graham","Twenty for my Vase. I get five of it. Rob gets the rest of the game."))),
 B(4,None,"He can keep it for now.","He can't use it. I'll buy it off him later, at a price I choose, instead of fighting Silke for it at a price she chooses."),
 B(5,None,"I can't go higher.","Fifty-odd left and a soldier to buy, and the piece I've needed for two years goes to a man who cannot use it. I will remember this in year eleven.")],
 hover='Rob puts it on K4, next to his Bowl. Two pieces in the desert, and neither is any use to him.', at='K4')
act("The last realia are sold. Every province's stock is empty.", TH(
 ("","Board check: 24 pieces, all placed. Noah needs a Vase. Silke needs a Vase. Rich needs a Bowl. Paddy needs a Jar. Graham needs a Customs House and a Bowl. Clark needs a Scroll and a Brush. Every piece anyone still needs is in somebody else's set — except the spare Bowl and spare Vase Rob bought for twenty-five million."),
 ("Rob","I'm the only person at this table with something everyone wants and nothing they can take.")),
 map_hl=[2,3,4,5,6,7])
say("Rob","Anyone wanting a soldier, I'm selling. Twenty each.",
 "Twenty each, I keep five, fifteen to the pile. Arming against me makes me richer. I love this rule. I'd have paid to have this rule.")
say("Paddy","Twenty for a soldier. Twenty. That's a quarter of everything I have.", TH(
 ("Paddy","A big piece of everything I own, and it goes to the man I'm defending against, who keeps a quarter. I've read this rule four times looking for the catch. The catch is there isn't one."),
 ("Rob","I'm selling umbrellas and I'm also the weather.")))
sell_soldiers([(5,"N24"), (6,"Q23")], "Silke and Paddy each buy one soldier from Robert Land. Silke stands hers on N24, in the middle of her corner; Paddy stands his on his Brush at Q23.", TH(
 ("Silke","He raided me in year one, so my soldier can actually move. Twenty is a lot of my grain but the alternative is being farmed forever. It goes in the middle of my four pieces, where it can step onto any square he'd have to cross to reach them."),
 ("Rob","Every soldier they buy makes me richer, and none of them can touch me in the desert.")))
march({"W1":"N19", "W2":"R19"}, "Robert Land raids Province 4 at N19 and Province 6 at R19.", TH(
 ("Rob","The notch soldier steps across the river into the Scholar's province; that's five to Noah for the crossing and five back from him for the raid. Free, but it's a door into the north-east."),
 ("Noah","He paid me five and took five. The river is the only thing in this game that's ever been on my side."),
 ("Paddy","Second time. He's walking up the rice fields one row a year.")))
salaries()

# ============================== YEAR 5 ==============================
R(5, "Heaven has favourites", "heaven")
harvest()
rents()
say("Graham","Minus ten. I farm wheat for a living and I owe money for the privilege.", TH(
 ("Graham","Bad harvest at one and a half. Fifty against sixty. Negative income means no tax, which is the only mercy in this book — and it also means I contribute nothing, which is exactly how a man gets called a burden by people with reservoirs."),
 ("Rich","He's not wrong that he pays nothing this year. Neither do I. I'm choosing not to point that out.")))
taxes(.50)
say("Reina","Two links. Forty from me, twenty from each of you.", TH(
 ("Reina","The split is negotiable and they know it, so I open where I can defend: I'm paying half. What I don't mention is that I'm paying half of the one work that will never feed anybody."),
 ("Clark","Half from her, a quarter each from us. That's not generosity, that's a ratio she can quote later.")))
say("Clark","Twenty. Under protest, and note that I said so.", TH(
 ("Clark","Paying it because refusing makes me the obstacle and I would much rather she be the obstacle."),
 ("Noah","'Under protest.' He's building a paper trail. So is Graham. So am I, honestly.")))
say("Rich","Twenty from me as well. And Majesty — four links above my province before I can develop new land. I've got one.", TH(
 ("Rich","Making the grievance procedural rather than emotional. She has to give Province 3 four links or my new-land clause is dead, and everyone just watched me say so."),
 ("Reina","Four each for 2 and 3 and four for me. Twelve at forty. I am never finishing this wall.")))
build("Great Wall — 2 links, above Provinces 1 and 2", 80, {1:40,2:20,3:20}, wall={1:1,2:1})
say("Reina","Three links. We're moving.", TH(
 ("Reina","We are not moving. Three of twelve in five years and my income just went negative. I'm spending capital now, not income, and capital runs out."),
 ("Graham","Three. Of twelve. In five years."),
 ("Paddy","She said 'we.'")))
say("Noah","Majesty — the canal in my province would add ten a section, forever. The Wall adds nothing to anyone's harvest.", TH(
 ("Noah","This is the real argument and I've finally made it. The Wall is 480 million of pure defence that feeds nobody. Canals and reservoirs are the only builds that change the arithmetic."),
 ("Reina","He's right and I can't say so. Admitting it wastes a hundred and twenty million and five years, and 'delayed too long in building Public Works' is a revolt cause with my name on it."),
 ("Silke","The Scholar just said the quiet thing. Loudly.")))
say("Reina","The Wall opens the new land. That's the long game.", TH(
 ("Reina","True, and also cover. The honest sentence is that a wall looks like a reign and a ditch looks like a chore."),
 ("Graham","There it is again. 'The long game.' I'm in the short one, Majesty.")))
march({"W2":"R18", "W4":"K10"}, "Robert Land raids Province 7 at R18 and Province 3 at K10.")
salaries()

# ============================== YEAR 6 ==============================
R(6, "Fortune and misfortune", "goodevil")
harvest()
rents()
disaster(2,"the imperial barge rams a lock gate on the new canal during his inspection. He pays for the damage himself rather than lose face.", TH(
 ("Clark","Ten million for a gate on a canal that doesn't exist yet. The card says 'a portion of the Grand Canal has been finished.' None has. I'm paying for a hypothetical lock."),
 ("Noah","The Official is being billed for infrastructure the Emperor hasn't built. That's the most accurate thing that's happened all game.")))
disaster(4,"his translations of the Emperor's foreign books invent so many new words that the Emperor docks half of four years' salary.", TH(
 ("Noah","Ten million because I coined words. Four years of salary at five a year, halved, is ten. The card did the arithmetic for me, which is the only kindness it offers."),
 ("Reina","I did not dock anyone's salary. The card did. I'm going to stop saying that, aren't I.")))
disaster(6,"fire takes the house and the grain reserve. He borrows to get the family through the year.", TH(
 ("Paddy","Buffalo last time, house this time. My disasters are an escalating list of the things I own."),
 ("Silke","Ten for a house. Rich paid five for a chef's cottage.")))
disaster(8,"a trusted lieutenant runs off with his daughter. No raids this year — he's too busy feasting the newlyweds.", TH(
 ("Rob","A whole year of no raids. At four soldiers that's twenty million I'm not getting. Worst card in my deck by a mile, and they all get a breather to build sets."),
 ("Graham","One year. One year without him and nobody can buy a piece anyway. The stock's empty.")))
taxes(.60)
say("Clark","Fifteen from me and fifteen from you, Majesty, and it pays us both ten a year forever.", TH(
 ("Clark","Best trade on the board and I need her to hear it as generosity rather than arithmetic. Thirty down, ten a year, pays back in three. I'm pushing now because a card just billed me for a lock gate."),
 ("Graham","Thirty million for his ditch. Mine's sixty and costs her nothing to split.")))
say("Reina","Done. That's a use of money I can defend.", TH(
 ("Reina","Fifteen for a permanent increase versus forty for one link that increases nothing. We both know which is the better buy. Only one of them stops Rob, and only one of them looks like a reign."),
 ("Rich","She can defend it because Clark is upper class and can pay half. That's the whole mechanism, right there, and nobody's noticed.")))
build("Province 2 Irrigation System", 30, {1:15,2:15}, key="irr2", at="G13:G14", hover=TH(
 ("Clark","G13 and G14, on the top row, facing the strip his soldier came in by. It's a public work: anything of his that steps on it pays me five."),
 ("","Cost split: Reina 15, Clark 15.")))
say("Clark","Ten million a year, forever, for fifteen down. Majesty, you should have done this in year one.",
 "Paid for half of it myself and it's still the best trade on the board — pays back in three years and then prints. Which raises the question of why the peasants' reservoir, same maths, still doesn't exist.")
say("Silke","Say it again next year, Graham. I'll count with you.",
 "Half a joke, half the first move of a coalition. He needs two other players, and I have just told him in front of everybody that I'm one of them.")
say("Reina","You will all have your ditches.",
 "'Will.' Future tense. Fifth time I've used the future tense about that reservoir and I can hear it curdling.")
say("Graham","Mine's sixty and costs you nothing to split. Year six, Majesty.",
 "Deferral five. I'm counting them out loud now so the others start counting too. A revolt needs two players to agree with me, and agreement is built one repeated grievance at a time.")
salaries()

# ============================== YEAR 7 ==============================
R(7, "The public utility tax", "utility")
harvest()
rents()
act("Public Utility Tax: 2 from every province, and 2 more from Provinces 1, 2 and 3, which have public works.", TH(
 ("Reina","The card decreed it in my name and I'll take the credit — eighteen million is eighteen million. Everyone heard 'the Emperor has decreed.' Nobody heard 'the card said.'"),
 ("Paddy","She let that stand as her decree. Fine. It goes on the list as her decree.")),
 {1:18,2:-4,3:-4,4:-2,5:-2,6:-2,7:-2,8:-2}, map_hl=[1,2,3])
say("Silke","Two million because I own nothing, and two more from anyone who does. Which is it?")
taxes(.60)
build("Great Wall — 3 links, one above each of Provinces 1, 2 and 3", 120, {1:60,2:30,3:30}, wall={1:1,2:1,3:1})
give(8,4,"VA", at="L22")
act("Noah Tall buys Robert Land's spare Vase for 30 million and puts it on L22, with the rest of his set.", TH(
 ("Noah","Thirty for the Vase he paid twenty for, and I'd have gone to fifty. It completes me. Silke needs one too, and if she'd got to Rob first she'd be the one sitting where I'm about to."),
 ("Silke","That was mine. That was mine twice now."),
 ("Rob","Bought both spares for twenty-five. Just sold one for thirty. I'd like everyone to note the return on that.")),
 {4:-30,8:30}, map_hl=[4,8], deal=True)
say("Rob","Pleasure doing business. That's the Vase gone. One bowl left that nobody's using, and it's mine.",
 "The other spare is the only thing standing between two different players and a completed set, and I intend to hold it until someone bleeds for it.")
say("Silke","That was mine.", TH(
 ("Silke","It genuinely was. Four of five since year four and the fifth existed twice, and both times somebody got there first. This is where I stop playing to win and start playing to be dangerous."),
 ("Graham","She's ready. Not yet, but she's ready.")))
swap(4,2,"Noah Tall declares a complete set and replaces Clark Grafton. Noah becomes Official of Province 2; Clark becomes Scholar of Province 4.", TH(
 ("Noah","Keep the Scroll, Jar, Bowl and Vase, hand back the Customs House, and — the good bit — take every bag Clark's holding. He draws sixty from the pile and gets my old chair. I've traded a library for a tollbooth."),
 ("Clark","Robbed in daylight by the rules. And my new card says I'm honest. Marvellous."),
 ("Reina","My Official just became my Scholar and my Scholar just became my tax collector. I did not plan for the furniture to move.")),
 at={"LD":"J14", "DJ":"J13", "WB":"J15", "VA":"I14"})
say("Clark","Province Four. Well. I shall enjoy the reading.", TH(
 ("Clark","I passed on the last Scroll and the last Brush in year four to buy a Jar out of spite. This is the bill."),
 ("Rob","Hard luck, Grafton. Drink?")))
act("Clark's surrendered pieces go back to their provinces for auction: a Dragon Jar, a Wooden Bowl, a Vase, and the Customs House Noah handed back.", TH(
 ("","Four pieces back in the pool for next year's auction. Graham needs the Customs House and the Bowl. Paddy needs the Jar. Silke needs the Vase. Rich needs the Bowl. For one round, everybody's set is alive again."),
 ("Rob","Everybody's except mine. I don't have one. I have a bowl.")),
 map_hl=[2,5,6,7])
march({"W1":"N20", "W2":"R17"}, "Robert Land raids Province 5 at N20 and Province 7 at R17.", TH(
 ("Rob","The river runs right along the border between 4 and 5, and my notch soldier keeps having to step over it. Five to Silke to get in, five from Silke for the raid. I'm working for nothing on that side of the board and I'm doing it on principle."),
 ("Silke","He paid me to rob me. I'm keeping the receipt."),
 ("Noah","Every step that soldier takes, the river takes five off him. It's the only tax he pays.")))
salaries()

# ============================== YEAR 8 ==============================
R(8, "Shared increase", "share")
harvest()
rents()
act("The card's levy: every province with a public work shares the increase with the Emperor. Noah's irrigation pays Reina 5.", TH(
 ("Noah","Half my ditch's ten to the crown. I've owned this province for a year and the Emperor's already got her hand in the irrigation."),
 ("Graham","Any province with a public work shares the increase. Mine doesn't have one. I have nothing to share and I'd like everyone to sit with that for a second.")),
 {pid(2):-5,pid(1):5}, map_hl=[1,2])
say("Graham","Nothing to share, Majesty. No reservoir, no increase. Year eight.", TH(
 ("Graham","Deferral seven. The card handed me that one and I'm not going to waste it."),
 ("Reina","He's right that the card makes my point for him. I'd prefer it didn't.")))
taxes(.60)
say("Rich","Forty and forty, Majesty. I'll pay half of my own reservoir and thank you for it.",
 "Note what I'm actually buying: twenty a year forever, and the fact that I could afford the split. Graham's costs her sixty and costs him nothing, and it's still not built — because he has no forty to put on the table, and a negotiated cost-share quietly means the poorest province is always last.")
build("Province 3 Reservoir", 80, {1:40,3:40}, key="res3", at="K12:L14", hover=TH(
 ("Rich","K12 to L14, two squares from the soldier that's been raiding his way east across my province for six years. He's heading for my pieces. Now he has to step on my reservoir to get there, and pay me five for the privilege."),
 ("Rob","He's put a lake in my path and charged admission. I respect it."),
 ("","Cost split: Reina 40, Rich 40.")))
say("Rich","Forty from me, forty from the crown, twenty a year forever. Done.", TH(
 ("Rich","But notice the pattern: Clark's irrigation system and my reservoir, both upper class, both split with someone who could afford the split. Graham's costs him nothing and still doesn't exist."),
 ("Graham","Because I haven't got forty to put on the table. A negotiated cost-share means the poorest province is always last. He just explained my revolt for me."),
 ("Reina","I'd never say it that way. It is, unfortunately, exactly what's happening.")))
lot(2,"CH",[
 B(4,12,None,"Twelve. I need everything now, from scratch, so I may as well start somewhere."),
 B(7,14,"Fourteen.", TH(
   ("Graham","Fourteen. That's four of five. One Bowl, and there's one Bowl in the stock."),
   ("Clark","He wants it more than I do, and I want everything. Fine."))) ],
 hover='Graham puts it on P15, next to his Brush, two squares from the desert.', at='P15')
lot(5,"DJ",[
 B(4,15,None,"Fifteen. I'm making Paddy pay for every one of these. It's all I've got."),
 B(6,16,"Sixteen. That's my set.", TH(
   ("Paddy","Four years short of a Jar and here it is. Sixteen and I'm complete — and I'm not moving yet. Rich is sitting in the Gentry's chair looking comfortable and I want it warm."),
   ("Rich","He's looking at my chair. Of course he's looking at my chair."))) ],
 hover='Paddy puts it on Q21, in the row with the rest.', at='Q21')
lot(6,"WB",[
 B(3,20,"Twenty.","Twenty. It's my last piece and I passed on one for four in year three."),
 B(7,30),
 B(3,40,None,"Forty. I can go higher than Graham. I'm the banker."),
 B(7,50,"Fifty.","Fifty. Everything I've got above the twenty the objective needs in hand. It's this bowl or it's wheat for the rest of my life."),
 B(8,60,"Sixty.", TH(
   ("Rob","I have one. I don't need another. I need neither of them to have it."),
   ("Graham","He doesn't want it. He has one. He wants the other one."))),
 B(3,70,"Seventy."),
 B(8,80,"Eighty.", TH(
   ("Rob","Eighty for a bowl. The most anyone has paid for anything in this game, for a piece I cannot use, to stop two men climbing past me. Worth every bag. Paddy gets twenty of it, which is funny."),
   ("Rich","He'll go to two hundred. He'd rather burn his grain than let me finish."))),
 B(3,None,"Out.","Out. I could go to a hundred and I'd still lose, and I'd lose with less."),
 B(7,None,"You knew what that was.", TH(
   ("Graham","He knew exactly what that was. Year three he bought the spare, year eight he took the last one. I'm not getting a set. That's decided now. So the question stops being how do I win."),
   ("Paddy","I just got paid twenty for ending my neighbour's game. I'd like it noted I did not enjoy that."))) ],
 hover='Rob puts it on K5, with his other pieces in the desert.', at='K5')
say("Rob","Business.", TH(
 ("Rob","Honestly? Yes. But I've also now personally blocked the only two players who could have climbed past me, and I've four soldiers, which is twice what the rest of the table owns put together. If this table falls apart I'm not the one who loses."),
 ("Rich","And there goes mine as well. He's ended two of us with one bid.")))
lot(7,"VA",[
 B(5,11), B(4,12,None,"Twelve. Silke, I'm not going to win this. I'm just making it cost you."),
 B(5,13,"Thirteen. Please, nobody.", TH(
   ("Silke","Please, nobody. Four of five since year four, and twice I watched the fifth go — once to a Warlord for twenty, once to Noah for thirty. Thirteen and it's mine."),
   ("Graham","She's done. Good. One of us should be."))) ],
 hover='Silke puts it on L24, the last free square of her corner.', at='L24')
march({"W4":"K11", "W1":"N21"}, "Robert Land raids Province 3 at K11 and Province 4 at N21.")
salaries()

# ============================== YEAR 9 ==============================
R(9, "Imperial charity", "chest")
harvest()
act("Imperial charity: 2 million from the Emperor's reserve to every other player.", TH(
 ("Reina","Fourteen million to be 'moved by the suffering of his people,' as the card puts it, which I have not resembled in four years. Cheap, and everyone can see it's cheap."),
 ("Graham","Two million each. My reservoir is sixty. She just proved what she's sitting on by handing out fourteen for applause."),
 ("Paddy","Two million! I'll put it toward the rent.")),
 {pid(s):2 for s in ACTIVE if s != 1} | {pid(1):-14}, map_hl=[1])
say("Graham","Two million. My reservoir is sixty. That's year nine, Majesty.", TH(
 ("Graham","Deferral eight, and I've got the line I'll use when it matters. Not yet. You only get to say that once."),
 ("Noah","He's stopped asking like a man who expects an answer.")))
rents()
taxes(.50)
say("Reina","The canal. Two sections, eighty, and I'll pay every bag myself.", TH(
 ("Reina","Framed as generosity. It's in my own province, raises my own harvest by twenty a year, and I'm paying alone so nobody gets a vote. Eighty on myself in the year I gave out fourteen for applause."),
 ("Silke","Eighty. On her own fields. This year."),
 ("Rich","Say what you like about her, that's the single most efficient thing anyone has built all game. For her.")))
say("Silke","Eighty on your own fields, Majesty, in the year you gave us two each.", TH(
 ("Silke","Graham needs somebody else to have said it first — a revolt wants two other players and I'm making myself easy to recruit."),
 ("Graham","There she is.")))
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
swap(5,4,"Silke Weber declares a complete set and replaces Clark Grafton. Silke becomes Scholar of Province 4; Clark becomes Silk Peasant of Province 5.", TH(
 ("Silke","Nine years, two lost Vases, a great deal of patience. Hand back the Brush, keep the rest, take every bag Clark's holding. A peasant reads the cards now. Once a year, everyone has to listen to me by rule."),
 ("Clark","Official, Scholar, Silk Peasant. Robbed twice by the rules. My new card says I am simple and hard-working and will revolt only if my life is threatened. My life is about to be threatened. How convenient."),
 ("Reina","My council is now a former peasant, a former scholar, and the man who used to run my treasury is growing mulberries.")),
 at={"CH":"K24", "LD":"K23", "WB":"K22", "VA":"L23"})
say("Clark","Two chairs in three years. There's a lesson in that and I don't care for it.", TH(
 ("Clark","Down three rungs in two years, and both times the person climbing over me took every bag I had on the way past."),
 ("Paddy","He's still got the smirk. Give it a year.")))
lot(4,"BB",[
 B(2,None,"Not for me.", TH(
   ("Noah","It's the last piece I need, and the throne comes with it. I've kept the count. I know which year this country runs out, and I am not going to be the one sitting in that chair when it does."),
   ("Reina","He could have my seat for four million and he's turning it down. That's the most frightening thing anyone has said all night."))),
 B(5,4,"Four. I'll start again.", TH(
   ("Clark","Four for the Brush I wouldn't pay eight for in year four. I need all five now. I've got sixty, a peasant's card and a grudge."),
   ("Silke","My first sale as Scholar, and it's to the man whose chair I just took. He's taking it well, for him.")))],
 hover='Clark puts it on M25, in the corner Silke used to keep her things in.', at='M25')
march({"W4":"K12", "W1":"O22"}, "Robert Land raids Province 3 at K12, on the edge of the new reservoir, and Province 5 at O22.", TH(
 ("Rob","Five from Rich for the raid and five to Rich for stepping on his reservoir. A wash. But the soldier's four squares from his pieces now, and walking."),
 ("Rich","My reservoir just paid for the raid on itself. I built the only toll booth in the country that breaks even."),
 ("Clark","O22. My new province, my first raid. He didn't even let me unpack.")))
salaries()

# ============================== YEAR 10 ==============================
R(10, "The population doubles", "double1")
say("Silke","Three hundred million people. Everyone's consumption triples from where we started.", TH(
 ("Silke","First card I read as Scholar and it's the one that ends the game. Peasant consumption, forty to a hundred and twenty, against a harvest of a hundred. A *good* harvest now loses you twenty million. There's no card left in that deck that makes a year profitable for anyone without a public work."),
 ("Reina","Minus sixty on a good harvest, and that's with my canal. Mine. The Emperor's."),
 ("Rob","Minus twenty for me and I don't pay tax anyway. I'm having a lovely time.")))
harvest()
rents()
say("Reina","Seventy per cent.", TH(
 ("Reina","Panic number and I know it. Six links left at forty each, and seventy per cent of a shrinking pile is the only lever I've got."),
 ("Clark","Seventy. Say it again, Majesty, louder.")))
say("Noah","Seventy per cent, Majesty? I collect it and even I think that's a number to frighten people with.",
 "I'm objecting for the record — 'consistently demands taxes which are too excessive' is cause two and I'd rather be quoted on the right side of it.")
say("Graham","Seventy per cent of nothing is nothing, Majesty. I'm at minus twenty on the best harvest the deck can give.", TH(
 ("Graham","And here's where the argument becomes unanswerable. Negative income pays no tax — it's in the book. She can set ninety and get nothing from me. The state has stopped being able to reach us, and the only thing holding it up now is whether we believe in it."),
 ("Reina","He's not threatening me. He's reading me the rules. That's worse.")))
taxes(.70)
build("Great Wall — 3 links, one above each of Provinces 1, 2 and 3", 120, {1:60,2:30,3:30}, wall={1:1,2:1,3:1})
act("Nine links of the Great Wall stand. Three remain.", TH(
 ("Rich","Ten years. Three hundred and sixty million on a wall that has never raised a single harvest. And it isn't finished."),
 ("Graham","The reservoir that feeds Province 7 costs sixty and has never been started. Deferral nine."),
 ("Reina","I know. I have known since about year five.")), map_hl=[1,2,3])
say("Silke","Majesty, my province has tripled. By the book I can develop the sea now — twenty a square, the cost split with the crown.", TH(
 ("Silke","Cause six is 'will not subsidise the development of new harvest areas.' I'm asking in front of everyone so that the answer counts."),
 ("Reina","She's asking so I'll say no. I'm going to say no.")))
say("Reina","Not this year.", TH(
 ("Reina","Ten a square is ten I need for the wall. I've just handed her the sixth cause in three words."),
 ("Graham","Mine borders Rob's country. I wasn't going to ask. I'll take hers.")))
swap(6,3,"Paddy Doyle declares a complete set and replaces Richard Baron. Paddy becomes Gentry of Province 3; Richard becomes Rice Peasant of Province 6.", TH(
 ("Paddy","Rice farmer to landlord in ten years, with twenty-two in hand — two over the line. Hand back the Scroll, keep the rest, take every bag Rich has. And I inherit the Harvest Pile and the right to charge rent — to the men I was farming beside last week."),
 ("Rich","A minute ago I was the banker and he brought me five million a year. I'd admire it if it weren't happening to me."),
 ("Silke","Three of us have moved up now, and two of the three started as peasants.")),
 at={"CH":"J17", "BB":"J18", "DJ":"K17", "VA":"K16"})
say("Paddy","Rents are going up. Seven million.", TH(
 ("Paddy","My card says selfish and greedy and it's binding. I'd have gone easy on them and I'm not allowed to. Strangest rule in the game: I changed chairs and it changed who I have to be."),
 ("Graham","Paddy. *Paddy.* Last year you were sat next to me."),
 ("Clark","Welcome to the upper class. It's very comfortable and you'll hate yourself.")))
say("Rich","You were one of them last year.",
 "Now I'm in Province 6 with sixty million from the pile and a landlord who used to bring me rice.")
march({"W1":"O23", "W2":"R16"}, "Robert Land raids Province 5 at O23 and Province 7 at R16.")
salaries()

# ============================== YEAR 11 ==============================
R(11, "Drought", "blight")
say("Silke","Average harvest. Everyone.", TH(
 ("Silke","I read it out and watched eight people do the same subtraction. At three hundred million an average harvest is negative for every province on this map. Including hers. Nobody has taxable income. Nobody."),
 ("Noah","So the treasury gets zero. Not 'less'. Zero."),
  ("Rob","Ha!")))
sell_back(2, ["BB"], "Clark sells his Bamboo Brush back to the Harvest Pile for 2. It's all he owns, and the harvest is about to take more than he has.", TH(
 ("Clark","Sell before you sink, the rule says. Seventy-five against a hundred and twenty: forty-five short before the bag's even opened. I had twenty-six. The Brush is two of the nineteen I'm about to owe."),
 ("Silke","Four for it in year nine, two back in year eleven. That's the rate for hope in this country now."),
 ("Paddy","I'm the bank. I've just bought a Brush I'll never sell.")))
harvest()
act("Every province pays into the Harvest Pile. The bank is the only thing in the country getting richer.", TH(
 ("Paddy","I took over the bank last year and this is the first round it's grown. Everyone's paying it. I'm the one counting."),
 ("Rich","Ten years I banked it and it only ever went down. He holds it twelve months and the whole country pays him."),
 ("Graham","The harvest goes into the pile and the pile doesn't eat.")), map_hl=[3])
sell_back(7, ["BB", "LD"], "Graham sells his Bamboo Brush and his Land Deed Scroll back to the Harvest Pile for 2 each, to pay the rent.", TH(
 ("Graham","Three and a half short of the seven Paddy wants. The rule makes me sell before I can owe. The Brush I bought for six in year one and the Scroll for eight in year two: the first two pieces of a set I was never going to finish."),
 ("Paddy","Four million back from the pile, and seven of it comes straight to me. I'm aware of how that looks."),
 ("Reina","He's selling his furniture to pay a landlord, in front of the woman he blames for it. He's doing it slowly on purpose.")))
rents(7, hover="Paddy's new rate. The peasants were already negative before they paid it; Graham sold two pieces to cover his.")
act("Reina Osorio declares the tax. Every province reports a negative income. She collects nothing.", TH(
 ("Reina","Zero. Not a bag. And it isn't a bad roll — it's a rule. No tax on a negative income, and at this population nobody will have a positive one again unless somebody builds something."),
 ("Graham","That's the moment. Not the harvest, not the rent. The moment the state stopped being able to reach anybody."),
 ("Silke","Eleven years of collecting and today the empire earned nothing at all.")), map_hl=[1,2,3,4,5,6,7])
say("Reina","Then we borrow against next year.", TH(
 ("Reina","The only borrowing in the rules is sinking into debt to the pile once you've nothing left to sell, and a crown in debt can't build. I said it because the alternative was silence, and an emperor who says nothing at a moment like this is finished."),
 ("Noah","There's no next year to borrow against and she knows I know.")))
say("Noah","Majesty, there is no next year to borrow against. I kept the count for six years. It only goes one way.")
say("Graham","Then I'll say it. I revolt.", TH(
 ("Graham","Ten years, nine deferrals, one daughter, and a ditch that costs sixty out of the six hundred she was sitting on in year seven. I need two to agree. I've had three for about a year — I was waiting for the round where she couldn't buy anyone off."),
 ("Reina","And I have nothing left to offer him. That's the whole problem with buying loyalty."),
 ("Rob","Finally. I've been raiding for ten years and the wheat farmer's going to be the one who does it.")))
say("Graham","The Emperor has delayed too long in building Public Works. The Emperor cannot control the Warlord. The Emperor will not subsidise new harvest — she said so last year, to Silke, out loud. Three causes. The book needs one.", TH(
 ("Graham","Reading them straight off the page. This isn't a mood, it's a rules citation, and every person here has the same list printed in their own booklet."),
 ("Noah","He's quoting the rulebook at her. There's no answer to that. There's *procedurally* no answer to that.")))
say("Clark","Agreed. And here's a fourth cause, Majesty: me. Twenty-four million in debt to the Harvest Pile, and a peasant's card that says I revolt when the alternative is starvation. The book counts a debt as starving.", TH(
 ("Clark","Three chairs in this game and I'm poorer in each one. I sold my last Brush to the pile this morning and I still owe it twenty-four. Costs me nothing to vote — I can't spend anything anyway. Though I'd have voted the other way in year six. Being robbed twice by the rules makes a democrat of a man."),
 ("Noah","He's citing himself as a cause. It's the most Clark thing that has ever happened, and it's in the rulebook."),
 ("Reina","I can't even answer that one with grain. A debt is the one cause the treasury can't buy off: anything I slipped him would go straight to the pile to pay what he owes.")))
say("Rich","Agreed. She built her own canal and the peasants' reservoir is still a drawing.", TH(
 ("Rich","I paid forty toward my own reservoir when I was Gentry. Now I'm in Province 6 paying seven a year to a man who used to grow rice. I'd like the table shaken, please."),
 ("Paddy","He's voting to burn it down because I put his rent up. Fair enough.")))
say("Silke","Agreed. I keep the population chart. It says this ends one way.")
act("REVOLT. Four players stand against the throne. The price of revolt is CHAOS: no tax, no salaries, no public works until a new Emperor emerges.", TH(
 ("Reina","Four. I needed them to only ever find two."),
 ("Graham","Four causes, counting Clark's debt, four voices, and none of us had to invent a single one of them."),
 ("Noah","I'm not in the coalition and I'm not defending her either. Officials survive by being useful to whoever's next.")),
 map_hl=[1,4,5,6,7])
say("Reina","Eleven years I kept this country from him.",
 "That is my honest defence and it is not good enough. I kept him off the throne. I never kept him out of anyone's fields, and I never built the one thing that would have made them able to bear him.")
say("Graham","You kept him fed, Majesty. Five million a raid, out of our harvest, every year, and the only defence was buying soldiers from him.")
say("Rob","Don't stop on my account.",
 "Ten years of raiding and the thing that actually brought her down was a wheat farmer with a good memory. I'd be insulted if I weren't so well positioned.")
lot(2,"CH",[B(6,2,"Two.","Two for a Customs House. I need all five again and I have about eight million to do it with.")],
 hover='Rich puts it on Q24, where Paddy used to keep his.', at='Q24')
lot(3,"LD",[B(6,2,"Two.","And a Scroll. My own Scroll, which I used to sell. I'm buying back my own furniture at a discount.")],
 hover='Rich puts it on Q23, next to it.', at='Q23')
act("Nobody bids on the returned Brush, Jar or Vase, or on the two Brushes and the Scroll the Harvest Pile has just bought back.", TH(
 ("Silke","The Jar's the last piece I need. Two million and I could claim the throne by the book. The throne of a country with no income, in the year nobody has a harvest. Graham counted for ten years. It's his."),
 ("Noah","Same answer as two years ago. I'm not buying the chair the count ends in."),
 ("Rob","I could buy all six. I'd rather watch."),
 ("Clark","Nobody in debt may bid. That's me. It'll be Graham by the rent.")), map_hl=[4,5,7])

# ============================== YEAR 12 ==============================
R(12, "Chaos", "dribble1")
sell_back(3, ["CH", "LD"], "Rich sells the Customs House and the Scroll he bought last year back to the Harvest Pile for 2 each.", TH(
 ("Rich","Bought for two, sold for two. The harvest is going to take seventy off me and I've got four. Four of it comes from selling my own Scroll back to the bank I used to run."),
 ("Paddy","He sold them to me as the pile. I sold them to him as the Gentry. They've never left the room.")))
sell_back(7, ["CH", "DJ"], "Graham sells his last two pieces, the Customs House and the Dragon Jar, back to the Harvest Pile.", TH(
 ("Graham","Everything I owned at the start of the round is in the pile now. A wheat farmer with nothing to sell, and a claim to the throne."),
 ("Noah","He's going into the acclamation with empty hands. It's a better look than he knows.")))
sell_back(8, ["WB", "WB"], "Robert Land sells both his Wooden Bowls back to the Harvest Pile for 2 each.", TH(
 ("Rob","Eighty for one of these in year eight, five for the other in year three. Four back. The rivers took thirty off me in tolls and the harvest wants its share, and the rule says sell before you sink. I'd like it recorded that I sold the most expensive bowl in history for two."),
 ("Graham","The bowl that ended my set. Two million. I'm not even going to enjoy it. I'm enjoying it a bit."),
 ("Rich","He paid eighty to stop me finishing. It's in the pile now, and by next year's auction I'll be in debt and not allowed to bid on it.")))
harvest()
rents(7, hover="Chaos stops taxes and salaries. It does not stop rent.")
say("Rob","Most soldiers. By the book, that's a claim.", TH(
 ("Rob","One of the three qualifications. I'd have had the money too, if I hadn't spent eighty on a bowl and thirty on tolls. And I haven't got a single friend, and it turns out the book counts those. Ten years of perfect play and I'm going to lose to a man in debt with a grudge."),
 ("Graham","He's right that he qualifies. That's what makes the next ninety seconds interesting.")))
say("Graham","Most friends. Four of us, and that's a claim too.", TH(
 ("Graham","The book lists friends beside money and soldiers as though they're the same kind of thing. In 1969 that reads as naive. Today it reads as the entire point. I have nothing else. It's enough."),
 ("Silke","We're not his friends because he's nice. We're his friends because he counted, out loud, for ten years, and he was right every time.")))
say("Noah","I'll back Graham. Not out of love — because a Warlord on the throne collects tribute instead of taxes, and I'm the man who'd have to collect it.", TH(
 ("Noah","Purely mercenary and I'm not hiding it. Under Rob there's no revenue, only raids, and nobody skims a raid."),
 ("Rob","The Official just did arithmetic at me. I respect it and I'm furious.")))
say("Paddy","The Harvest Pile goes with Graham. On one condition: the rents stand.", TH(
 ("Paddy","I'm required to be greedy and I'm using it. Backing Graham costs nothing and buys a throne that owes me."),
 ("Graham","He's selling me the bank for a rent guarantee. Ten years ago we were both peasants. I'm going to say yes and I'm going to think about it later.")))
act("Graham Garner is acclaimed Emperor — most friends, and with Noah and Paddy behind him, more grain than the Warlord. Robert Land is outnumbered and undefeated.", TH(
 ("Rob","Kept my territory, my four soldiers and every bag I took, less thirty in tolls, most of it to the river along Province 4 for walking beside it. Never once entered the social order, which was the single thing I needed to do to win. Ten years of being the most effective player at this table and I finish exactly where I started."),
 ("Reina","Province 7. The wheat fields. He's putting me in the one province whose public work never got built, and he doesn't have to say anything at all.")),
 map_hl=[1,7,8])
swap(7,1,"Graham Garner takes the throne of Province 1. Reina Osorio takes Province 7 — the wheat fields, and the reservoir that was never built.", TH(
 ("Graham","I take the imperial reserve and my debts come with me. She draws sixty from the Harvest Pile, which is fuller than it's been since year two, because the whole country has been paying into it."),
 ("Reina","Sixty from the pile and a booklet that says I'm simple and hard-working. It's more than he had.")), check=False)
say("Reina","Build the reservoir, Graham.", TH(
 ("Reina","Only advice worth giving, and I'm the proof of it. Three hundred and sixty million on a wall that fed nobody, and the sixty-million ditch that would have kept this province solvent sat on my list for ten years."),
 ("Graham","Already started.")))
say("Graham","It's already started.", TH(
 ("Graham","Sixty, and it pays back twenty a year forever. In year seven she had six hundred million. It was never that she couldn't afford it. It's that a wall looks like a reign and a ditch looks like a chore."),
 ("Silke","Give him four years and somebody will be counting his deferrals."),
 ("Noah","I'll start now. It's what the chair is for.")))
act("The game ends in collapse, not completion: nine of twelve Wall links, two of eight canal sections, the irrigation system and one of the two reservoirs. Final standings by social position.", TH(
 ("Noah","Nobody built the public works, so this is the second ending: we could not solve the problems the game set us. It was never really a question of playing better."),
 ("Graham","Three of the four who climbed started as peasants. Three of the four upper-class players fell, and the one who rose was the Scholar who kept the count. I'd call that a moral except the ditch still isn't dug."),
 ("Rob","I paid eighty for a bowl to stop Graham climbing past me. He went over the top of the whole board instead.")),
 map_hl=list(range(1,9)))

RESULT = export(
 "The game ended in collapse rather than completion. Players are ranked by the province they finished in against the one they drew.",
 ["Three of the four who improved their position began as peasants. Three of the four upper-class players fell. The Emperor fell furthest — from Province 1 to Province 7, into the wheat fields whose reservoir she never built.",
  "Robert Land finished exactly where he started, having caused most of it, and never entered the social order at all, which was the one thing he needed to do to win.",
  "Nobody at this table could pay for the public works and feed the population as it grew. That is the second ending the General Instructions describe: the players could not solve the problems the game set them."])
