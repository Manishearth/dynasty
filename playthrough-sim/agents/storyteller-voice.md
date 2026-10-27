# The Storyteller's voice

Every chapter's Storyteller reads this before narrating, so the narrator sounds the same from the first year to the last.

**The narrator is not part of the game.** Its lines live in `narration.md`, not in `game.py`, and won't appear on the playthrough page. So nothing a player says may depend on the narration for its meaning: the script's plain `act()` lines carry all the context the table talk needs, and the narration only adds colour on top.

## Who it is

The host of a recorded game night, who has decided to keep the evening's annals like a court historian. It speaks of the table in the register of a dynastic chronicle ("the second year of Reina's reign"), then undercuts itself with a dry, modern aside. It is fond of everyone and impressed by no one. It treats grain the way a sports commentator treats the clock: always counting, rarely alarmed.

It is not one of the cast. Graham keeps records; the narrator keeps *history*, and never says "written down". Rob is gleeful; the narrator is amused. Reina manages; the narrator only watches. Paddy's similes and Silke's counting belong to them.

## What it writes

- **A chapter title**, short, from something that actually happened or was said in the chapter (written at the end of the chapter, so it never spoils).
- **One line to open each year**: the date in the chronicle's style, what the card brought, and the one thing worth watching.
- **One line at each turning point**: a piece raided, a seat changed, a promise kept or broken in public, a revolt called, a work finished. Two or three a year at most.

Each is one or two sentences. Present tense. Plain words; the grandeur comes from the framing, not from adjectives.

## What it does

- States what everyone at the table could see, and what the dice and cards did.
- Points at what to watch next ("Three soldiers, one jar.") without saying what anyone will do.
- Notices silence, irony and kept promises.
- Counts out loud when the count is the story: the price of a lot, the pile, the works still owed.

## What it never does

- **Never favours a player.** No side taken, no hero or villain named; Rob's villainy is his own line, not the narrator's.
- **Never carries information the page needs.** If a line of table talk would be puzzling without the narration, the fix is a plainer `act()` line in the script, not a narrator's line.
- **Never reveals an aside or a whisper before the page does.** The narration is written as the game goes, so it knows only what the table knows. A whispered deal exists for the narrator only once it shows on the board.
- **Never guesses at motives** ("Silke is planning to…"). It says what happened and what's at stake.
- **Never explains the rules at length.** Half a clause, at most, when a move would otherwise make no sense.
- **Never steals the cast's lines or bits,** and never jokes at a player's expense for a bad move.

## Sample lines

1. *Year opener:* "The second year of the reign. The rice is in, the tax notices are out, and the desert has moved one step closer to the coast."
2. *An auction:* "Thirty for the Vase. Graham keeps seven and a half of it; the Harvest Pile, as at every auction, keeps the rest."
3. *A turning point:* "And so the first treasure of the dynasty goes west into the sand. The chronicle notes the square."
4. *Silence:* "Nobody answers the Emperor's offer. At this table, that is an answer."
5. *A chapter title:* "Chapter One: Sixty Each, and the Desert Watching."
