Director that spawns storyteller and player subagents. Agents like responding to things so auctions by default go much higher than one would otherwise want.

Surprising game mechanic: holding back an item by setting minumum bid very high!

agents refusing to end the game when it makes sense


Sometimes resistent to my attempts to steer things. Actors, amirite?

you can get good steering by reminding them of the right facts at the right moments

# Director fixing things

The crown is short of money:

At 40% tax the crown raises only about 60 in a good year once the population is half again as large.
After Year 5 little income is left to tax unless the table buys land.
So I’ve changed Reina’s actor’s note: she now taxes hard in good years, since bad years bring no tax, and builds the cheap works in lean ones. It’s logged in seed.md. There are no tips this chapter.




# rule gaps

Large economies break assumptions nobody had tested. At ×4–×6 with lots of new land, the Harvest Pile cap, harvest debt and “sell before you sink” all came up for the first time. The cap turned out to be the engine’s own assumption, not a rule. Before trusting a rule the engine enforces, check it against the rulebook.
Simultaneous rounds need a priority rule. The Rob-bery revolt was decided by whether Reina’s same-round payoff counted. Revolts, payoffs and acclamations need a stated order.
The game’s end is easy to get wrong. briefs.py’s endgame line was a year off in two games: it doesn’t know that a project needs its year to itself, or whether the works step has already passed. Players plan around it, so it needs to be right.
Seat changes protect the Warlord’s targets. With six players who keep changing seats, the Warlord’s “one piece from each player” objective almost never completes. Rob got the throne through a revolt instead. If the Warlord should be able to win his own way, his objective needs another look.
Small tables blunt the unsold-lot rule. Sellers with two types sell the other one first and hold the key piece back. A scenario meant to test that rule needs sellers who hold only one type.