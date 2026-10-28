## Your board card (Year 11, from the engine)

- **Grain** 107. **Army** 3 of 3. **Objective:** raid one piece from each player in a realia-holding seat, not the Emperor. Raided so far: Paddy's Land Deed Scroll, Clark's Land Deed Scroll. Still to raid: Rich, Silke.
- **Pieces on your desert:** Dragon Jar T17, Land Deed Scroll O18, Land Deed Scroll M15. (Only raided pieces count toward your objective; the line above names them. A piece won at auction counts nothing.)
- **Your soldiers:** W1 J14, W2 M24, W3 P22.
- **Each piece, rounds from each soldier:** Clark's Wooden Bowl J16: W1 2, W2 8, W3 6; Rich's Customs House L25: W1 11, W2 1, W3 4; Rich's Wooden Bowl P26: W1 12, W2 3, W3 4; Rich's Dragon Jar O19: W1 5, W2 5, W3 3; Silke's Customs House S25: W1 11, W2 6, W3 3.
- **Unraided palaces, rounds from each soldier:** Summer Palace G26: W1 12, W2 6, W3 9; Winter Palace H21: W1 7, W2 5, W3 8; Marble Pagoda F17: W1 4, W2 7, W3 10. A raid on one costs the Emperor 20.

## At the table since your last turn

Clark: "Silke, a public offer, so it goes in the book in ink: I stay out of the Customs House altogether, you take it at the minimum, and you let me have the Jar. You'd still be one Scroll short, the same as me, and neither of us has fed three quarters of our grain to the pile fighting over pottery. If you'd rather bid me up, you'll win it, and I'll write down exactly what it cost you."

Rich: "A Customs House I already have, and I'd never be so greedy as to take a second one off a lady who needs it. Bid away, Silke, Clark. I'm only here to admire the pile filling up."

Silke: "Let me count it for you all, since I'm the one who always does: Clark, seventy-two and a half; Rob, a hundred and seven; Paddy, minus nineteen and a half; and me, three hundred and fifty. Five pieces in four years I've lost by a single grain, so this year I've added two to every limit I set, and anyone who wants to beat me will have to do it with Rich's purse."

The auction: Silke takes the Customs House at 2, unopposed. The Dragon Jar goes to Rich at 113, one grain past Silke's 112 (Clark stopped at 52; Rich would have gone to 351 to keep it from Silke). Both prices go to the pile. Rob passed both.

Silke: "Two grain for a Customs House, and one grain short on the Jar. Six pieces now I've lost by a single grain, and this time I added the two. Rich, a hundred and thirteen for a pot you don't need: that's four hundred and three and a half left in your sack, and I hope it sits very prettily on your mantel."

Rich: "Silke, I'm sorry, truly. One grain, and this time it was mine, and I know exactly how that feels from the other side. The Jar goes somewhere quiet, and I'll say nothing more about it, having learned that lesson from Rob at some expense."

Silke puts her Customs House on S25; Rich puts the Dragon Jar on O19.

## Your move: the march

Each soldier steps one square (diagonals allowed) or stands still. raid=5 (10 in Province 1) takes 5 from that province's player, or the piece standing there instead; '-' raids nothing. Tolls are 5 each, paid to the province.

**W1 on J14:**
- I13 [2] raid=- tolls=[]
- I14 [2] raid=- tolls=[]
- I15 [2] raid=- tolls=[(2, 'the Province 2 Irrigation System')]
- J13 [2] raid=- tolls=[]
- J15 [2] raid=5 tolls=[(2, 'the Province 2 Irrigation System')]
- K13 [3] raid=5 tolls=[]
- K14 [3] raid=5 tolls=[]
- K15 [3] raid=5 tolls=[]
- stay

**W2 on M24:**
- L23 [4] raid=- tolls=[]
- L24 [5] raid=- tolls=[]
- L25 [5] raid=5 piece=CH tolls=[(5, 'the south river')]
- M23 [4] raid=- tolls=[]
- M25 [5] raid=- tolls=[]
- N23 [5] raid=- tolls=[]
- N24 [5] raid=- tolls=[]
- N25 [5] raid=5 tolls=[]
- stay

**W3 on P22:**
- O21 [5] raid=- tolls=[]
- O22 [5] raid=5 tolls=[]
- O23 [5] raid=- tolls=[(5, 'the Grand Canal')]
- P21 [5] raid=- tolls=[]
- P23 [5] raid=5 tolls=[(5, 'the Grand Canal')]
- Q21 [6] raid=5 tolls=[]
- Q22 [6] raid=5 tolls=[]
- Q23 [6] raid=5 tolls=[(6, 'the Grand Canal')]
- stay

**Taking a piece:** a step marked `piece=` raids a square with realia on it. You take the piece or the 5; to take the piece, add `take: <soldier> <square of your desert>`, where it will stand (an empty desert square).
- Rich's Customs House on L25 (W2 can step there): the nearest empty desert squares are M18, N18, M17, N17.

**Distances (rounds) from each piece to your soldiers:**
- Rob's Dragon Jar (T17): W1 10, W2 7, W3 5
- Rob's Land Deed Scroll (O18): W1 5, W2 6, W3 4
- Clark's Wooden Bowl (J16): W1 2, W2 8, W3 6
- Rich's Customs House (L25): W1 11, W2 1, W3 4
- Rich's Wooden Bowl (P26): W1 12, W2 3, W3 4
- Rob's Land Deed Scroll (M15): W1 3, W2 9, W3 7
- Silke's Customs House (S25): W1 11, W2 6, W3 3
- Rich's Dragon Jar (O19): W1 5, W2 5, W3 3

**Whispers** exist for a genuinely private deal, one that can't be made in public. They're still rare: most turns, write "none".

## Your reply

Reply in exactly this format:

```
move: W1 <square or stay>; W2 <square or stay>; W3 <square or stay>; take: <none, or soldier and desert square>; hire: <no, or a square>
say: <what Rob says out loud to the whole table, a line or two>
aside: <one or two sentences, no more, that Rob says to the camera, talking the audience through the move. The other players can't hear it.>
whisper: <"none", or "To <name>: ..." (rare: only a genuinely private deal)>
```
