# Game 2 — the peasant game. Five players, ends with every Public Work built.
setup([1,5,6,7,8], "peasant", "The peasant game",
      "Five players · nine years · everything gets built",
      "A second evening, same friends. The Emperor and three peasants, and the Warlord. No Official, no Gentry, no Scholar — so no rent, and Reina hands out their jobs herself. She remembers the first game, and builds the reservoir first.", short="5 players · 9 years")

def appoint(text, hover, hl):
    act(text, hover, map_hl=hl)

# ============================== YEAR 1 ==============================
R(1, "Appointments", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
say("Reina","There's no Official, no Gentry and no Scholar at this table, so I'm handing out their jobs.", TH(
 ("Reina","Last time I had an Official who skimmed, a banker who fawned and a Scholar who wouldn't tell me the truth. This time I get to choose who does each job, and I'm choosing on purpose."),
 ("Graham","She's nervous. She's being organised about it, but she's nervous.")))
appoint("Reina appoints Paddy Doyle to bank the Harvest Pile.", TH(
 ("Reina","The steadiest hands at the table, and the least likely to make a speech about it."),
 ("Paddy","I've never held money I didn't owe someone. Exciting."),
 ("Rob","Not me? I'm hurt. I'd have been a wonderful banker.")), [1,6])
appoint("Reina appoints Graham Garner to read the I Ching and keep the population count, at the Scholar's salary of 5 a year.", TH(
 ("Reina","The man who counted my deferrals out loud for ten years can count the people. If the clock's going to be in somebody's hands, I want it in the hands of the person most likely to say what it says."),
 ("Graham","Five a year to read her the bad news. She's paying me to do what I'd do for free."),
 ("Silke","She's put her loudest critic on salary. That's either very wise or very funny.")), [1,7])
say("Reina","And I'll collect my own tax. Thirty per cent.", TH(
 ("Reina","No Official means nobody stands between me and the money, and nobody stands between me and the blame either. Thirty because it's year one and I'm going to need them to like me in year eight."),
 ("Paddy","No rent, either. No Gentry, no landlord. I'm going to enjoy this game.")))
taxes(.30, collector="Reina collects the tax herself")
act("Robert Land declines to pay tax. Again.", TH(
 ("Rob","Same precedent as last time. It held for twelve years then."),
 ("Reina","Fine. I've stopped planning around his tax. I'm planning around his soldiers.")), map_hl=[8])
say("Reina","Then I'll be buying soldiers from you, Robert, sooner than you'd like.",
 "He'll take the money, because the booklet makes him sell. That's the one lever I have, and last time I never pulled it.")
say("Rob","Twenty each, Majesty. Same as always.", TH(
 ("Rob","She's going to arm herself. Good. I keep five of every twenty and her soldiers can't move until I've raided her anyway."),
 ("Graham","He says 'same as always' like we're old friends. We are, unfortunately.")))
say("Reina","First build. The Winter Palace.", TH(
 ("Reina","Not because I want a palace. Because the booklet says I can't touch a single canal section in Provinces 5 and 6 until it stands. It's the key to everybody else's ditch."),
 ("Silke","She's built a palace and somehow it's for us.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace")
lot(5,"CH",[
 B(6,4), B(7,5),
 B(6,6,"Six.", TH(
   ("Paddy","There are two of these and two of us who want one. Graham'll get the other. Six is fine."),
   ("Graham","I'll take the next. There's no Official at this table — Customs Houses are just pottery that two of us need.")))])
lot(6,"BB",[
 B(5,5), B(7,6,"Six.","Two Brushes, and Silke and I both need one. No point fighting over the first of two.")])
lot(7,"LD",[
 B(6,5), B(5,6,"Six.", TH(
   ("Silke","Six, and there's another next year for Paddy. The pairs are easy. It's the single pieces — my Jar, Paddy's Bowl, Graham's Vase — that'll be the fight."),
   ("Paddy","She's worked it out already. One of each of our own pieces, and the other two of us both want it.")))])
raid([(6,5),(7,5)], hover="Peasants first, same as last time. A raided square can never be raided again.")
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
 ("Rob","So this year it's the Emperor or nothing. The Emperor it is, then."),
 ("Reina","Which means his raid lands on me, at ten. His bad card is my bad card.")))
taxes(.35, collector="Reina collects the tax herself")
say("Graham","Majesty, the reservoir.", TH(
 ("Graham","Old habit. Different game, same booklet — the crown pays for it all, sixty million."),
 ("Reina","He said it on the second round. Last time he said it on the second round too.")))
say("Reina","Yes. This round. Sixty.", TH(
 ("Reina","Last game I said 'after the Wall' nine times and finished the evening in the wheat fields. Twenty a year forever for the province with the worst land. It's the best sixty I'll spend tonight."),
 ("Graham","...oh. Oh, she means it."),
 ("Silke","He doesn't know what to do with his hands.")))
build("Province 7 Reservoir/Irrigation System", 60, {1:60}, key="res7")
say("Graham","I had a speech ready for year eleven.",
 "I genuinely did. Nine deferrals' worth of it. I'll have to find something else to be angry about.")
lot(5,"CH",[
 B(7,8,"Eight.","Eight for the other Customs House. Paddy had the first; this one's mine, as agreed in a silence nobody admitted to.")])
lot(6,"BB",[
 B(5,7,"Seven.","Seven for the second Brush. Graham had the first. The pairs are going exactly the way the pairs should go.")])
lot(7,"LD",[
 B(6,7,"Seven.", TH(
   ("Paddy","Two of four. Now the hard part — I need Graham's Vase and Silke's Jar, and so does somebody else for each."),
   ("Graham","Everybody's two of four. Next round, all three of us sell the one piece we've got that the other two both want.")))])
raid([(1,10)], text="Robert Land raids Province 1 — the only place his wounded legs will carry him.",
     hover="His disaster keeps him out of 5, 6 and 7, so his one raid this year lands on the Emperor at ten.")
salaries({7:5}, text="Reina pays Graham 5.")

# ============================== YEAR 3 ==============================
R(3, "Rain and flood", "rainflood")
say("Graham","Good harvest for Provinces 1, 3, 6 and 7. Rivers flood in 2, 4, 5 and 8. So — good for Reina, Paddy and me. Bad for Silke and Rob.", TH(
 ("Graham","And my reservoir pays its first twenty this year. I read that card with a straight face, which took effort."),
 ("Silke","Bad harvest the year before I need every bag. Brilliant.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
taxes(.40, collector="Reina collects the tax herself")
say("Reina","Forty. Graham's reservoir earns its first twenty this year, and part of that twenty is mine.", TH(
 ("Reina","A public work raises a province's harvest, which raises its tax. That's the thing I never understood last game: a ditch pays the crown back. A wall never does."),
 ("Graham","She's taxing my reservoir. Fair. It's her reservoir too. I just live next to it.")))
build("Grand Canal in Province 5 — 2 sections", 80, {1:80}, canal={5:2})
say("Silke","Two sections in my province, and the crown pays.", TH(
 ("Silke","Twenty a year from next year, forever. I'm flooded and broke this round and the Emperor just bought me a river."),
 ("Rob","Two sections of canal in Province 5. That's a public work I have to pay five to cross. I'm being taxed by infrastructure.")))
lot(5,"DJ",[
 B(6,8), B(7,10),
 B(6,12,None,"Twelve. One Jar in the world. I need it, Graham needs it."),
 B(7,15,"Fifteen.", TH(
   ("Graham","Fifteen. My reservoir paid me twenty this year and I'm spending most of it on the one Jar in existence. That's three of four."),
   ("Paddy","He's got a reservoir and I've got a bad buffalo. Fine."))),
 B(6,None,"Go on.","I'll get one somewhere. There's always somewhere.")])
lot(6,"WB",[
 B(5,6), B(7,9,None,"Nine. If I take the Bowl as well I'm complete."),
 B(5,11,"Eleven.", TH(
   ("Silke","Eleven out of a flooded year. If Graham gets this, he's done and I'm farming silk forever."),
   ("Graham","She's right. That's exactly what happens if I win it."))),
 B(7,14,"Fourteen.", TH(
   ("Graham","Fourteen. That's four of four. Now I need twenty in hand and a peasant to replace — and Silke's province is the best in the country."),
   ("Silke","He's looking at my seat."))),
 B(5,None,"Out.","Out. The Vase is next and I need that too. If I spend it all here I lose both.")])
lot(7,"VA",[
 B(5,7), B(6,9), B(5,12),
 B(6,14,"Fourteen.", TH(
   ("Paddy","Fourteen and I'm three of four. Missing a Jar, and Graham owns the only one."),
   ("Silke","And there's no point my winning it. I'd need the Bowl to finish, and Graham has the only Bowl."))),
 B(5,None,"Keep it.","Graham holds the Jar Paddy needs and the Bowl I need. Every set at this table runs through Graham now.")])
raid_take(7, "BB", "Robert Land raids Province 7 and takes Graham's Bamboo Brush as tribute.", TH(
 ("Rob","My booklet: raid a square holding realia and I can take the realia. Graham was one turn from a full set. Now he isn't. And that's the first piece toward my own objective — one piece from every player."),
 ("Graham","He took the Brush. He's got a Brush and no use for it except that I need it."),
 ("Reina","He's going for his objective this time. One piece from each player, a palace from me. If he finishes, he can take my seat.")))
say("Graham","How much for it?", TH(
 ("Graham","Not angry yet. Angry later. Price first."),
 ("Rob","He's asked how much. That's the most fun sentence in this game.")))
say("Rob","Ask me again when I've raided everybody once.",
 "I'm not selling it until it's worth more as a sale than as a block. He has to want it more every year.")
raid([(6,5)], text="Robert Land raids Province 6.")
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
 ("Paddy","Every peasant province has a public work now. I've never seen this happen. Last game this happened to nobody."),
 ("Rob","Two more canals to pay tolls on. The whole country's turning into water.")))
raid_palace("Winter Palace", "Robert Land raids the square holding the Winter Palace. The Emperor pays him the cost of the structure: 20.", TH(
 ("Rob","Palace squares count as the Emperor's realia, and I take the cost. That's two of my four — Graham's Brush, Reina's palace. Silke and Paddy left."),
 ("Reina","Two of four. If he gets a piece from both of the others he can take any seat at this table, and he will take mine."),
 ("Graham","He's playing to win this time. Last game he played to spoil.")))
say("Reina","Two soldiers, Robert. Forty.", TH(
 ("Reina","Cause five is 'the Emperor cannot control the Warlord.' Last time I never bought a single soldier. This time I've been raided, so mine can move, and I'm buying two."),
 ("Rob","She's buying them with her own money. I keep ten. Every soldier anyone buys makes me richer, and none of them can move until I've raided them. Hers can. That's new.")))
sell_soldiers([1,1], "Reina buys two soldiers from Robert Land.", TH(
 ("Reina","Forty to the shop that sells the army I'm defending against. I know. I'm doing it anyway."),
 ("Silke","The Emperor has an army. It's two soldiers, but it's an army.")))
raid([(5,5)], text="Robert Land's other soldier raids Province 5.")
salaries({7:5}, text="Reina pays Graham 5.")

# ============================== YEAR 5 ==============================
R(5, "Shared increase", "share")
say("Graham","Average harvest. And every province with a public work shares the increase with the Emperor, fifty-fifty.", TH(
 ("Graham","That's all three of us. Silke, Paddy and me each pay her ten. The card just gave Reina thirty for building our ditches."),
 ("Reina","Last game this card cost Ken five and that was the whole effect. This game it's thirty. That's what building things buys.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
act("Each province with a public work pays the Emperor half its increase: 10 each from Silke, Paddy and Graham.", TH(
 ("Silke","Ten of my twenty back to the crown. I'll take it. Two years ago my twenty didn't exist."),
 ("Paddy","First year my canal pays and half of it goes straight back to her. I'm choosing to call that rent.")),
 {pid(5):-10, pid(6):-10, pid(7):-10, pid(1):30}, map_hl=[1,5,6,7])
taxes(.50, collector="Reina collects the tax herself")
build("Summer Palace", 20, {1:20}, key="Summer Palace")
say("Reina","The Summer Palace. Not for me — the booklet won't let me start my own canal or the Wall without it.",
 "Twenty for the key to the last two systems. Every palace I build this game is a padlock on something useful.")
say("Graham","Robert. The Brush.", TH(
 ("Graham","I've got everything else, and he's got his raid on me counted already. The Brush is just furniture to him now."),
 ("Rob","He's right, and he knows he's right, so the price is the only interesting part left.")))
say("Rob","Thirty-five.", TH(
 ("Rob","He's got a hundred and forty-odd and a reservoir. Thirty-five is what it's worth to a man who's about to take the best province in the country."),
 ("Silke","The best province in the country. That's mine. He's pricing my seat.")))
give(8, 7, "BB")
act("Graham Garner buys back his Bamboo Brush from Robert Land for 35.", TH(
 ("Graham","Thirty-five for a Brush I bought for six. Rob made thirty-five on a piece of wood by standing on it."),
 ("Rob","I'd like that sentence carved on something.")), {pid(7):-35, pid(8):35}, map_hl=[7,8])
swap(7,5,"Graham Garner declares a complete set and replaces Silke Weber. Graham becomes Silk Peasant of Province 5; Silke becomes Wheat Peasant of Province 7.", TH(
 ("Graham","Hand back the Jar — it's native to Province 5 — keep the rest, and take every bag Silke's holding. Wheat to silk in five years. And the province I'm leaving has the reservoir Reina built for me, which is now Silke's reservoir."),
 ("Silke","He's taken my seat, my grain and my canal, and given me his reservoir. It's the best thing in Province 7 and it's the only reason I'm not furious."),
 ("Reina","Graham climbed, and the province he left behind is better off than the one he took. I'll take that.")))
say("Silke","I'm keeping your reservoir, Graham.", TH(
 ("Silke","Twenty a year, forever, and I didn't pay for it. That's the one good piece of furniture in this whole swap."),
 ("Graham","She's right. I built my own replacement's income. I'd do it again.")))
raid([(6,5),(7,5)], hover="Rob's raid on Province 7 lands on Silke, who owns nothing yet for him to take.")
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
 ("Graham","Last game she built the Pagoda in year three, with peasants waiting. This game it's the thing she builds when she's got nothing else she can afford. That's the right order.")))
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda")
lot(5,"DJ",[
 B(6,10,"Ten.", TH(
   ("Paddy","Ten. The Jar's back on the table and I've had the other three since year three."),
   ("Graham","I'm the seller. I get a quarter of whatever Paddy pays for it. I'd like him to pay a lot."))),
 B(7,11,None,"Eleven. I need a Jar too now. I need everything now."),
 B(6,16,"Sixteen.", TH(
   ("Paddy","Sixteen and that's four of four. Twenty in hand, a province to take — and the province with the canal and the good land is Graham's now."),
   ("Graham","He's looking at me the way I looked at Silke."))),
 B(7,None,"Have it.","Sixty-odd in grain and nothing else. He's got nearly twice that, and he only needs this one piece.")])
lot(6,"BB",[
 B(7,4,"Four.", TH(
   ("Silke","Four for a Brush. Start again, in a new province, from nothing."),
   ("Rob","She's put a piece of realia on a square. I've noticed.")))])
act("Silke puts the returned Land Deed Scroll up for auction. Nobody bids.", TH(
 ("Silke","Graham has one, Paddy has one, and Province 7 doesn't need one. Nobody needs a Scroll. It sits there."),
 ("Paddy","The one piece at this table that nobody wants.")), map_hl=[7])
swap(6,5,"Paddy Doyle declares a complete set and replaces Graham Garner. Paddy becomes Silk Peasant of Province 5; Graham becomes Rice Peasant of Province 6.", TH(
 ("Paddy","Hand back the Jar, keep the rest, and take every bag Graham's holding — which is everything Silke had, plus everything he had. I'm not overly ambitious, it says so on my card. I'm also not stupid."),
 ("Graham","I took Silke's seat and her grain a year ago. He's just done the same thing to me, with my grain and hers. I can't even be angry. I wrote this move."),
 ("Silke","The richest man at this table started the evening growing rice.")))
say("Graham","Fair.", TH(
 ("Graham","One word. It's the only honest one available."),
 ("Rob","Two of them have robbed each other blind without me lifting a finger. I love the peasant game.")))
raid_take(7, "BB", "Robert Land raids Province 7 and takes Silke's Bamboo Brush as tribute.", TH(
 ("Rob","Three of four. Graham, Reina, Silke. One piece from Paddy and I can take any seat at this table — and there's only one seat I want."),
 ("Silke","I owned it for one round. He took it the round I put it down."),
 ("Reina","Three of four. And Paddy's pieces are sitting on open squares in Province 5.")))
say("Reina","Paddy. Buy a soldier, and stand it on your realia.", TH(
 ("Reina","Rob can only raid an un-raided square. If Paddy's soldier sits on his pieces, Rob has to land somewhere empty. And mine can move now — I'm sending both of them toward Province 5."),
 ("Paddy","I've got a Customs House, a Scroll and a Vase, and a man in the desert who wants one of them.")))
sell_soldiers([5], "Paddy buys a soldier from Robert Land.", TH(
 ("Paddy","Twenty to the man who's coming for me. It can move — he raided Province 5 back when it was Silke's."),
 ("Rob","Everyone's buying soldiers. I'm going to be rich and outnumbered.")))
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
 ("Reina","Four. Same horse as last time. It's a very consistent horse."),
 ("Graham","Same disaster, same twenty lashes. The trainer's having a worse evening than any of us.")))
disaster(8,"a lieutenant runs off with his daughter. No raids this year — too busy feasting the newlyweds.", TH(
 ("Rob","Year seven, three of four, one piece from Paddy away from the throne, and I'm at a wedding."),
 ("Reina","A year's grace. I'm spending it on the Wall.")))
taxes(.50, collector="Reina collects the tax herself")
say("Reina","My canal. Two sections, eighty.", TH(
 ("Reina","Last game I built this one for myself and got called out for it. This time every peasant province has had its public work for years. I've earned my own ditch."),
 ("Paddy","Nobody's going to say anything. That's what three ditches first buys you.")))
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
lot(5,"DJ",[
 B(6,6,"Six.", TH(
   ("Graham","Six for a Jar. Province 6 needs a Customs House, a Scroll, a Vase and a Jar, and I've got eighty-odd and nothing on the board. Start somewhere."),
   ("Paddy","I'm selling him back the Jar I took his seat with. Six is fine.")))])

act("Graham puts up the Brush and the Bowl he had to hand back. Nobody bids.", TH(
 ("Graham","Silke needs both. Silke has ninety-odd and a man who takes whatever she puts down."),
 ("Silke","Why would I buy a Brush? He'll take it off the square before I've finished paying.")), map_hl=[6])
say("Reina","Your soldiers, Paddy. Both of mine are on the edge of Province 5.", TH(
 ("Reina","Four soldiers between us and three squares of his realia. Next year Rob's soldiers come back from the wedding."),
 ("Rob","She's built a wall of soldiers around a man growing silk. Not the wall I expected.")))
salaries({7:5}, text="Reina pays Silke 5.")

# ============================== YEAR 8 ==============================
R(8, "Steady weather", "winds")
say("Silke","Steady weather. Neither feast nor famine: an average harvest for this year.", TH(
 ("Silke","An average harvest at a hundred and fifty per cent, with a public work in every province. Everyone's positive. Last game this card would have been a funeral."),
 ("Reina","Two projects left. Four Wall links. If nothing goes wrong, I finish next year.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
taxes(.50, collector="Reina collects the tax herself")
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
say("Reina","Two links. Two more next year and every public work this country owes is standing.", TH(
 ("Reina","Last game I spent three hundred and sixty on a wall that fed nobody, first. This game the Wall is last, and it's only four links, because only my province is under it."),
 ("Graham","Four links instead of twelve, because nobody's sitting in 2 or 3. The Wall was always the most expensive thing on the list and the least useful. Building it last is the whole trick.")))
act("Robert Land sends both soldiers into Province 5. Paddy's soldier stands on his Vase; Reina's two hold the squares beside it.", TH(
 ("Rob","Three pieces of realia on three squares, and every one of them has a soldier on it or next to it. I can land on an empty square for five. I can't land on a piece."),
 ("Paddy","I've been standing on a vase for a year. It's the most important thing I've done all game.")), map_hl=[5,8])
capture_soldier("Reina's soldier captures one of Robert Land's soldiers on the edge of Province 5.", TH(
 ("Reina","Captured, horizontally, the way the General Instructions allow. Last game I never once controlled the Warlord. This game I took a soldier off him with one I bought from him."),
 ("Rob","She bought it from me. I sold her the soldier that just captured my soldier. I'd like that noted as the funniest thing that has ever happened to me."),
 ("Graham","Cause five, 'the Emperor cannot control the Warlord.' Struck off, live, in front of everybody.")))
raid([(5,5)], text="Robert Land's last soldier raids an empty square in Province 5.",
     hover="Five million and a raid square, but no realia. He's still three of four.")
salaries({7:5}, text="Reina pays Silke 5.")

# ============================== YEAR 9 ==============================
R(9, "The last of the Wall", "chest")
say("Silke","Average harvest. And moved by the suffering of her people, the Emperor opens her purse: two million to every player from the Emperor's reserve.", TH(
 ("Silke","The card says 'his'. I changed it to 'her' reading it. Nobody stopped me."),
 ("Reina","Eight million out of the reserve in the year I need every bag for the Wall. I'll pay it. It's printed.")))
harvest("Paddy pays out the harvest from the Harvest Pile.")
act("Imperial charity: 2 million from the Emperor's reserve to every other player.", TH(
 ("Reina","Last game this card cost me fourteen and bought me nothing. This one costs eight and I don't need it to buy anything."),
 ("Paddy","Two million. I'm the richest person at the table and the Emperor just gave me two million. I'm going to hold it up to the light.")),
 {pid(s):2 for s in ACTIVE if s != 1} | {pid(1):-8}, map_hl=[1])
taxes(.50, collector="Reina collects the tax herself")
build("Great Wall — 2 links above Province 1", 80, {1:80}, wall={1:2})
assert all_built(), "not every public work is built"
act("Every public work the country owes is standing. The game ends: the players have survived, and the Emperor's reign has been a glorious one.", TH(
 ("Reina","Nine years. A reservoir in year two, three canals before my own, the Pagoda in the bad year and the Wall last. It's the same list I had last game in a different order, and the order was the whole game. Twenty-two million left in the treasury — 'too low a grain reserve' by anyone's reading, and it doesn't matter, because there's nothing left to build."),
 ("Graham","Three doubling cards still in the deck. We stopped before they came. That's the other half of the trick, and nobody planned it."),
 ("Rob","Three of four. One raid short, and the raid I needed was standing on a vase.")), map_hl=list(ACTIVE), big=True)
say("Silke","For the record, I'd like it noted that I lost.", TH(
 ("Silke","Silk to wheat. The first game I climbed a province and this one I fell two. I've got Graham's reservoir and Rob's raid squares, and the satisfaction of having read every card since year six."),
 ("Graham","She's not wrong. Survival's a team result. The seats aren't.")))
say("Reina","Same time next week?",
 "And this time I'd like to be a peasant.")

RESULT = export(
 "Every public work was built, so this is the first ending: the players survived and the Emperor's reign was a glorious one. Players are still ranked by the province they finished in against the one they drew.",
 ["Reina kept the throne and finished the list — which by Section 18 is a win for the Emperor. The difference from the full game was order, not money: productive works first, palaces only when they unlocked something, and the Wall last.",
  "The peasants spent the evening taking each other's seats. Graham climbed from wheat to silk, Paddy climbed over Graham, and Silke fell from silk to wheat — but every one of them finished with a public work paying into their province.",
  "Robert Land came within one raid of the throne. He stopped one piece short, with one soldier left, after the Emperor captured the other with a soldier she had bought from him."])
