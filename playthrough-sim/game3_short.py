# Game 3 — the short game. Four players, the upper provinces, eight rounds.
setup([1,2,3,4], "short", "The short game",
      "Four players · eight rounds · a race for the throne",
      "Short on time. Just the Emperor and the three upper provinces — no Warlord, no peasants, so no rent and no raids. The table agrees to stop after eight rounds and score from where everyone's sitting.", short="4 players · 8 rounds")

# ============================== SETUP ==============================
R(0, "Eight rounds", None, "Four players: the Emperor, the Official, the Gentry and the Scholar (rulebook Section 4 and Appendix A). No Warlord, so nobody raids and no soldiers are sold; no peasants, so no rent. Nothing is owed to Provinces 5, 6 or 7.")
act("Four booklets go in the box: the upper group. Shuffled and drawn.", TH(
 ("Reina","The Emperor. Three players who each want my chair, and eight rounds to get it."),
 ("Clark","Official. My booklet practically instructs me to skim. I'm going to take it seriously."),
 ("Noah","Scholar. Worst income, best information. I read the cards.")), map_hl=[1,2,3,4])
act("The table agrees to the short game: eight rounds, then score by province.", TH(
 ("Noah","Eight rounds means nobody finishes the public works — eight hundred and ten million of them, with only three of us paying tax. This is a game about who's sitting where at the end."),
 ("Clark","Then it's a game about the throne. Three of us can take it. Only one of us will."),
 ("Reina","Eight rounds of being the one they're all trying to replace. Eight is fine.")), map_hl=[1,2,3,4])
say("Rich","No peasants. Nobody to collect rent from. What exactly does a landlord do in this game?", TH(
 ("Rich","Bank the Harvest Pile and fawn. My card says I'm a fawner. I'm going to be the best fawner this table has ever seen."),
 ("Reina","He's going to be a problem. He's already being charming.")))
act("Rich sets out the Harvest Pile in stacks where everyone can see it.", TH(
 ("Rich","Two hundred and forty out, and the pile won't notice. Four of us can't drain twenty-five hundred million in eight rounds if we try."),
 ("Clark","He's counting it with the care of a man who expects to be asked about it later.")), map_hl=[3])
deal_grain("Rich deals 60 to each player from the pile. It's the first year's harvest.")
take_stock("Clark, Rich and Noah take their realia out of the box: one piece of their own and two of the kind they'll never need. It waits beside the board.", TH(
 ("Noah","One Brush and two Vases. There's one Customs House, one Scroll and one Brush in the world tonight, and each of us needs two of them."),
 ("Rich","Three single pieces and three people who each need two. Somebody's going to be holding the piece somebody else needs. Probably me."),
 ("Reina","Three of them, and only one throne. My favourite arithmetic.")))
act("Noah shuffles the twenty I Ching cards. Clark cuts out the Province 2 Irrigation System, one square by two; Rich cuts out the Province 3 Reservoir, two by three.", TH(
 ("Clark","One by two. The cheapest water work in the book, which means it's the one that gets built."),
 ("Rich","Two by three. The biggest cut-out in the box, for a landlord with no tenants."),
 ("Noah","No Warlord tonight. For once it doesn't matter where anybody puts anything.")), map_hl=[2,3,4])

# ============================== YEAR 1 ==============================
R(1, "Eight rounds", None, "No card is drawn. The 60 million each player holds is the first harvest.")
CUR_INC.update({s:60 for s in ACTIVE})
say("Reina","Thirty per cent. And Clark — the irrigation, this year. Fifteen each.", TH(
 ("Reina","I know what order to build in: whatever raises somebody's harvest, first. Clark's ditch raises his income, which raises my tax. It's the cheapest good thing on the list."),
 ("Clark","She's opening with my ditch. She's either learned something or she's buying me. Both, probably.")))
say("Clark","I'll collect it personally, Majesty.", TH(
 ("Clark","Personally. You learn a lot watching people count out tax."),
 ("Noah","He said 'personally' the way a man says 'privately'.")))
taxes(.30)
build("Province 2 Irrigation System", 30, {1:15,2:15}, key="irr2", at="I13:I14", hover=TH(
 ("Clark","I13 and I14, below my pieces. No Warlord to charge a toll, so I've put it where it waters the most squares I'm looking at."),
 ("","Cost split: Reina 15, Clark 15.")))
lot(2,"DJ",[
 B(4,6), B(3,8,"Eight.", TH(
   ("Rich","Clark's put up a Jar, not his Customs House. Everyone's doing the same arithmetic: sell your doubles first, hold the single piece the other two both want."),
   ("Noah","He's right. There's one of each of our own pieces and two people want every one of them.")))],
 hover='Rich puts it on K16, in the middle of Province 3. With no Warlord, the only consideration is that it looks well from his chair.', at='K16')
lot(3,"WB",[
 B(2,6), B(4,8,"Eight.","Eight for a Bowl. Rich is selling his doubles first too. Nobody's touching the singles until they have to.")],
 hover="Noah puts it on K21, near the canal's printed line.", at='K21')
lot(4,"VA",[
 B(3,6), B(2,8,"Eight.", TH(
   ("Clark","Eight. One each, all round, at eight. We've all agreed on a price without saying a word. That's how you know this table has played together before."),
   ("Reina","Three auctions and they've all paid exactly eight. I'm watching a cartel form and I can't bid.")))],
 hover='Clark puts it on H14, in the middle of Province 2.', at='H14')
salaries()

# ============================== YEAR 2 ==============================
R(2, "A careless year", "careless")
harvest()
disaster(1,"the Arabian horse throws her. The trainer is lashed twenty times.", TH(
 ("Reina","Four, and a trainer who gets lashed for it. The Emperor's disasters are other people's."),
 ("Rich","At this point the trainer should be lashing the horse.")))
disaster(2,"the chariot drops a wheel on a garrison inspection. He pays the crippled driver's pension.", TH(
 ("Clark","Four for a pension. That driver is doing very well out of me."),
 ("Noah","There are no garrisons — there's no Warlord. He's inspecting troops that aren't there.")))
disaster(3,"the head chef retires and is promised a house and a pension.", TH(
 ("Rich","Five, and there are no peasants to grumble that their buffalo got nothing. A very quiet chef retirement."),))
disaster(4,"the candle, the fire, the lost notes on the migratory habits of the swallow.", TH(
 ("Noah","A whole book on swallows, and the candle read it first."),
 ("Clark","He should write a book about losing the swallow book.")))
taxes(.40)
say("Reina","Rich, your reservoir. Forty and forty.", TH(
 ("Reina","Eighty, twenty a year to Province 3 forever, and half of that comes back to me as tax. Building it now is just good arithmetic."),
 ("Rich","She's buying me with my own reservoir. I'm delighted. I'm going to let her think it worked.")))
say("Rich","Your Majesty is too generous.",
 "She is too generous. She's also about to find out that a reservoir buys one year of gratitude and no more.")
build("Province 3 Reservoir", 80, {1:40,3:40}, key="res3", at="L10:M12", hover=TH(
 ("Rich","L10 to M12, the south-west corner of my province. Two by three, the biggest thing on the board tonight, and nobody coming to walk across it."),
 ("","Cost split: Reina 40, Rich 40.")))
lot(2,"DJ",[
 B(4,8,"Eight.","Clark set the minimum at eight, and Rich already has a Jar, so it's only me. One Jar each. Next round, the singles.")],
 hover='Noah puts it on K22, next to his Bowl.', at='K22')
lot(3,"WB",[
 B(2,8,"Eight.","Minimum of eight again, and Noah already has a Bowl. The cartel holds. Two of four for everybody, and next round we stop being friends.")],
 hover='Clark puts it on H15, next to his Vase.', at='H15')
lot(4,"VA",[
 B(3,8,"Eight.", TH(
   ("Rich","Eight. And now each of us holds two of four, and each of us is selling our single piece next round to the two people who want it."),
   ("Noah","Next round is the whole game.")))],
 hover='Rich puts it on K17, next to his Jar.', at='K17')
salaries()

# ============================== YEAR 3 ==============================
R(3, "Heaven has favourites", "heaven")
harvest()
say("Noah","Good for Clark and me. Bad for Reina and Rich. And the singles go up this round.", TH(
 ("Noah","I've got a good harvest and my Brush to sell. Clark wants it and Rich wants it. I want Clark's Customs House and Rich's Scroll."),
 ("Rich","Bad harvest the round the singles come up. I'm going to have to be clever instead of rich.")))
taxes(.40)
say("Reina","The Winter Palace. Twenty.", TH(
 ("Reina","Not for me — it's the key to Noah's canal. Nothing in Province 4 gets built until this stands."),
 ("Noah","She's unlocking my canal. Noted. Appreciated. Not enough to change how I bid.")))
build("Winter Palace", 20, {1:20}, key="Winter Palace", at="H20", hover=TH(
 ("Reina","H20. With no Warlord there's nobody to hide from, so it goes in the middle where I can see it."),
 ("","Reina pays the 20.")))
lot(2,"CH",[
 B(3,10), B(4,14), B(3,18,"Eighteen."),
 B(4,22,"Twenty-two.", TH(
   ("Noah","Twenty-two. Three of four. I need Rich's Scroll and that's it."),
   ("Rich","He's outbid me on the one piece I needed most, in the round my harvest was bad. I'll remember the date."))),
 B(3,None,"Take it.","Out. Bad harvest. And I can do something cleverer than outbid him.")],
 hover='Noah puts it on K23, in a neat row with the others.', at='K23')
lot(3,"LD",[
 B(4,12,None,"Twelve. If I get this I'm complete."),
 B(2,16), B(4,20),
 B(2,25,"Twenty-five.", TH(
   ("Clark","Twenty-five. Noah would be complete if he won this. I'd rather he wasn't. Three of four for me as well, and I need a Brush."),
   ("Noah","He'd rather I wasn't. I asked for it, really. I said 'if I get this I'm complete' out loud."))),
 B(4,None,"Out.","Out. I've just spent twenty-two and I need twenty in hand at the end, and Clark collects everyone's tax. And I told the whole table exactly what this piece meant to me. Lesson.")],
 hover='Clark puts it on H13, and turns it so the seal faces Noah.', at='H13')
lot(4,"BB",[
 B(2,14,None,"Fourteen. The Brush makes me complete."),
 B(3,18), B(2,22),
 B(3,26,"Twenty-six.", TH(
   ("Rich","Twenty-six with a bad harvest behind me. Clark would be complete with this, so it's worth more to me as a wall than as a Brush."),
   ("Clark","Rich just paid twenty-six to stand in my way. I respect it. I'm going to undo it."))),
 B(2,None,"Out.","Out. Fine. It's not going anywhere. Rich can't use it without Noah's Customs House, and Noah won't sell that.")],
 hover='Rich puts it on K18, at the end of his row, where Clark can see it from his chair.', at='K18')
act("Every piece is sold. Each of the three is one piece short — and the piece each one needs is held by the next.", TH(
 ("","Clark needs the Brush, which Rich holds. Rich needs the Customs House, which Noah holds. Noah needs the Scroll, which Clark holds. Whoever sells first makes somebody else Emperor and gives up their own chance."),
 ("Reina","A perfect circle with me in the middle. As long as nobody sells, nobody takes my seat."),
 ("Noah","A three-way standoff in a game with no dice. It's going to be decided by talking.")), map_hl=[2,3,4])
salaries()

# ============================== YEAR 4 ==============================
R(4, "The population increases", "half1")
harvest()
taxes(.50)
say("Noah","Forty and forty for my canal, Majesty?", TH(
 ("Noah","My province is the only one without a public work. A fair split is half."),
 ("Reina","Half. I'm keeping Noah happy. The happiest person at this table is the one least likely to be bribed.")))
build("Grand Canal in Province 4 — 2 sections", 80, {1:40,4:40}, canal={4:2})
say("Clark","Rich. The Brush. Name a price.", TH(
 ("Clark","Opening the talking. He paid twenty-six for it; he'll want double."),
 ("Rich","He's asked first. The one who asks first pays most.")))
say("Rich","Noah — what's the Customs House worth to you?", TH(
 ("Rich","I'm not answering Clark. I'm asking Noah whether he'll sell me the piece that makes *me* Emperor. Make them both nervous."),
 ("Noah","He's trying to start a bidding war over the throne, and I'm one of the things being bid on.")))
say("Noah","I'll sell you the Customs House the day Clark sells me the Scroll.", TH(
 ("Noah","That's not a price, it's the shape of the problem. None of us can buy without selling, and selling ends us."),
 ("Clark","He's honest even when he's being difficult. It's exhausting.")))
say("Clark","I'm not selling the Scroll.", "Of course I'm not. Noah would be Emperor by dinner.")
say("Reina","Nobody needs to sell anything. Four more years of this is fine by me.",
 "Fine by me in particular. Every round nobody sells is a round I stay on the throne.")
salaries()

# ============================== YEAR 5 ==============================
R(5, "The public utility tax", "utility")
harvest()
act("Public Utility Tax: 2 from each province, and 2 more from each province with a public work — that's all four.", TH(
 ("Reina","Twelve million from three people. I've built something in every province, so every province pays the extra two. I'd call that a dividend."),
 ("Clark","She decreed it. The card decreed it. We'll all pretend it was her.")),
 {1:12,2:-4,3:-4,4:-4}, map_hl=[1,2,3,4])
taxes(.50)
build("Summer Palace", 20, {1:20}, key="Summer Palace", at="H21", hover=TH(
 ("Reina","H21, beside the Winter Palace."),
 ("","Reina pays the 20.")))
say("Reina","Richard. A word.", TH(
 ("Reina","Rich holds the Brush Clark needs. If Rich doesn't sell, Clark can't climb. The Emperor can't bid at auction. Nothing in the rules says the Emperor can't pay someone to sit still."),
 ("Noah","She's going to bribe the Gentry. On the throne. In front of everyone. I love this game.")))
say("Reina","Forty million, and the Brush stays where it is for the rest of my reign.", TH(
 ("Reina","Forty from the treasury. It's what one Wall link would have cost me, and a Wall link never kept anyone off my throne."),
 ("Rich","For the rest of her reign. She chose those words. I'm going to treasure those words.")))
say("Rich","Your Majesty has my word. For the rest of your reign.", TH(
 ("Rich","I'm going to keep that promise to the letter."),
 ("Noah","He repeated her exact words back to her. Nobody repeats exact words unless they're planning to use them.")))
act("Reina Osorio pays Richard Baron 40 to hold the Bamboo Brush for the rest of her reign.", TH(
 ("Reina","Money well spent. Possibly."),
 ("Clark","She's paid him forty to say no to me. So he has a price. Now we know it's above forty.")),
 {1:-40,3:40}, map_hl=[1,3], deal=True)
salaries()

# ============================== YEAR 6 ==============================
R(6, "The Wall is breached", "breach")
harvest()
act("The card's levy: the Wall is attacked, but none has been built, so Provinces 1, 2 and 3 each pay 2 to the Harvest Pile for damages.", TH(
 ("Reina","Damages to a wall that doesn't exist. There's nothing to breach."),
 ("Rich","I'm the banker. I'm paying myself two million for damages to nothing.")),
 {1:-2,2:-2,3:-2}, map_hl=[1,2,3], pile_delta=6)
disaster(4,"his translations invent so many new words that the Emperor docks half of four years' salary.", TH(
 ("Noah","Ten. Half my salary for four years, docked by a card. She's going to say it wasn't her."),
 ("Reina","I don't dock anything. I've given up saying so.")))
taxes(.50)
say("Noah","Majesty, he'll sell. It's on his card: he takes advantage of anyone foolish enough not to watch him.", TH(
 ("Noah","I'm honest. My card says I always tell the truth. So I'm telling her. It costs me nothing, because I can't stop him either."),
 ("Rich","The Scholar has just read my personality card aloud to the Emperor. Rude. Accurate.")))
say("Reina","I know what his card says, Noah. I've paid for the rest of my reign.",
 "And he said 'for the rest of your reign,' and I've just realised what that sentence does if somebody ends it.")
build("Grand Canal in Province 1 — 2 sections", 80, {1:80}, canal={1:2})
say("Clark","Rich. Fifty.", TH(
 ("Clark","Forty was her number. Fifty is mine."),
 ("Rich","Fifty. Not yet.")))
say("Rich","I gave the Emperor my word, Clark. For the rest of her reign.", TH(
 ("Rich","I'm reminding everyone of the wording. Nobody's listening closely enough."),
 ("Noah","I'm listening closely enough.")))
salaries()

# ============================== YEAR 7 ==============================
R(7, "A bad harvest", "dribble1")
harvest()
taxes(.50)
build("Great Wall — 2 links, above Provinces 2 and 3", 80, {1:40,2:20,3:20}, wall={2:1,3:1})
say("Reina","Two links of the Wall. Somebody has to start it.", TH(
 ("Reina","Seventh round of eight, with everything productive built. A wall's the only thing left on my list. I'm building it with what's left."),
 ("Clark","She's spending the treasury on bricks. I'd have kept some back.")))
say("Clark","Rich. Seventy. And you keep the commission on whatever you sell me next.", TH(
 ("Clark","Seventy, and I'll have every bag of her treasury the moment I sit down. It's not my money I'm spending, really — it's hers, a round early."),
 ("Rich","Seventy. That's thirty more than the Emperor paid me to hold it.")))
say("Rich","Done.", TH(
 ("Rich","I promised to hold it for the rest of her reign. Clark's about to end her reign. I'll have held it for every single minute of it."),
 ("Reina","'For the rest of your reign.' It was. He kept his word exactly."),
 ("Noah","I did tell her.")))
give(3, 2, "BB", at="H12")
act("Richard Baron sells the Bamboo Brush to Clark Grafton for 70.", TH(
 ("Rich","Twenty-six to buy it, forty from the Emperor to keep it, seventy from Clark to sell it. A hundred and ten in, for a brush I paid twenty-six for and could never use."),
 ("Clark","Four of four, and twenty in hand. More than twenty.")), {2:-70, 3:70}, map_hl=[2,3], deal=True)
swap(2,1,"Clark Grafton declares a complete set and declares himself Emperor. Clark takes the throne of Province 1; Reina becomes Official of Province 2.", TH(
 ("Clark","Return all my realia, keep my own grain, and the Emperor must give me her entire reserve. Official to Emperor in seven rounds. The rules have handed me the country."),
 ("Reina","He takes the treasury and I take his chair and sixty from the pile. Emperor to Official in one swap."),
 ("Noah","And now I need the Scroll Clark just handed back to Rich. Rich has the Scroll. Rich has everything.")))
say("Reina","I'll collect it personally, Majesty.", TH(
 ("Reina","His line. I've been waiting all night to say it to him."),
 ("Clark","She's going to skim. Everyone knows she's going to skim. Her card practically instructs her to.")))
say("Clark","My card says I'm just and reasonably compassionate.", TH(
 ("Clark","A card telling me who to be. This one's better than the last."),
 ("Rich","He's going to be insufferable for one round.")))
salaries()

# ============================== YEAR 8 ==============================
R(8, "The last round", "share")
harvest()
act("The card's levy: every province with a public work shares the increase with the Emperor. Provinces 2, 3 and 4 pay Clark half their increase.", TH(
 ("Clark","Five from Reina's ditch, ten from Rich's reservoir, ten from Noah's canal. My first round on the throne and the card gives me twenty-five for works she built."),
 ("Reina","He's collecting dividends on my reign. Fine. I'll be collecting his tax.")),
 {pid(2):-5, pid(3):-10, pid(4):-10, pid(1):25}, map_hl=[1,2,3,4])
say("Clark","Forty per cent. Lower than hers, on purpose.", TH(
 ("Clark","One round left, so low tax costs me nothing that matters and looks generous in the transcript."),
 ("Noah","He's governing for the epilogue.")))
taxes(.40, collector="Reina, now the Official, collects the tax")
build("Marble Pagoda", 20, {1:20}, key="Marble Pagoda", at="G24", hover=TH(
 ("Clark","G24, by the sea, a good distance from her two palaces. My monument, not hers."),
 ("","Clark pays the 20.")))
say("Clark","The Pagoda. My first public work.", TH(
 ("Clark","Twenty. The booklet says the Emperor builds it when there's nothing else. There's plenty else. I wanted one."),
 ("Reina","He built a monument in his only round. I built three ditches and a reservoir in seven and they're paying him.")))
lot(3,"WB",[
 B(2,4,"Four.", TH(
   ("Reina","Four for a Bowl. Province 2 needs a Scroll, a Brush, a Vase and a Bowl. I've got one round. I'm starting anyway."),
   ("Rich","She's starting a set in the last round. I like her.")))],
 hover="Reina puts it on H14, where Clark's Vase used to stand.", at='H14')
act("Rich holds back the Land Deed Scroll and auctions the Bowl instead. Noah needs the Scroll to finish — and to take the throne.", TH(
 ("Rich","I could sell Noah the Scroll for the best price of the night. Then he'd be Emperor, and I'd be exactly where I am, with an Emperor who keeps his promises. I prefer one who owes me."),
 ("Noah","He's selling the Bowl. The Scroll stays in his hand. Eight rounds, and the honest man finishes where he started."),
 ("Clark","Rich just kept me on the throne by choosing which piece to auction. I'm going to owe him for that, and he knows it.")), map_hl=[3,4])
lot(4,"VA",[
 B(2,4,"Four.", TH(
   ("Reina","Two of four, in one round, for eight million. The new Official is off to a good start."),
   ("Noah","My Vase, to the woman who used to be my Emperor. Four. Fine.")))],
 hover='Reina puts it on H15, next to the Bowl.', at='H15')
salaries()
act("Eight rounds. The short game ends and the table scores from where everyone is sitting.", TH(
 ("Clark","Official to Emperor. Two rounds ago I was paying fifty for a brush nobody would sell me."),
 ("Rich","Held. And the most grain at the table that isn't sitting in the treasury. Ask the tiebreak."),
 ("Noah","Held, and honest the whole way, and the only person who told the Emperor the truth. Nobody wins for that. I'd do it again.")), map_hl=[1,2,3,4], big=True)

RESULT = export(
 "The table played the eight-round short game, so nobody finished the public works; players are ranked by the province they finished in against the one they drew, with grain as the tiebreak.",
 ["Clark climbed from Official to Emperor in seven rounds, by paying seventy for a brush the Emperor had paid forty to keep off the market.",
  "Rich kept his promise to Reina to the letter — he held the Brush for the rest of her reign, and then he ended her reign. He also chose, in the final round, which piece to sell, and that choice kept Noah off the throne.",
  "Noah was honest throughout, warned the Emperor exactly what would happen, and finished where he began. The short game rewards the person who controls the last piece, not the person who tells the truth about it."])
