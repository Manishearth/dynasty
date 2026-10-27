# Pilot, Year 1: report

Year 1 of the peasant game's table, played by five `dynasty-player` agents with the Storyteller refereeing through the engine. No steering: the deck was shuffled with seed `19691027` (`seed.md`); Year 1 draws no card, so chance played no part yet.

`game_pilot.py` runs cleanly through `run.py` (cards.py, engine.py, then the script, as `build.py`'s `run_ns` does) and exports 27 entries. It also builds into a page with `build.py`'s own `main` (tested into the scratchpad, not into the repo). Snapshots: `state/setup.json`, `state/year1.json`.

## The year

**Setup.** Rob put W1 on the notch (O18) and sailed W2 to R25, off Paddy's coast, and told the table he wouldn't pay tax: *"Your Majesty, the desert thanks you for your kind tax notice and has used it to light a campfire."* Reina made Paddy the banker and Graham the card reader at 5 a year, "because a revolt needs two peasants, and I'd like two of them to have a reason to stay loyal."

**Tax and build.** Thirty per cent (18 from each peasant; Rob refused) and the Winter Palace on G21: "every bag goes back into stone." She promised Graham's Reservoir next. Graham: *"I've written down that the Reservoir is 'next on the list', Your Majesty. I keep the records now, after all."*

**The auctions** were the heart of the year. All three peasants worked out the pairs-and-singles structure without being told twice.

- **Silke sold her Dragon Jar first,** "while Paddy and Graham both still have full purses and both have to have it." Rob bid 12 to push the price, then passed: *"I've pushed the price up by eight without spending a grain."* Paddy and Graham went 14, 16, 19, 24, 27. Graham moved his landing square mid-auction because Rob was "making notes": *"Rob, the records show I said 'the far corner'. I never said which one."* Paddy won at 27: *"My mother always said never come home without the jar, Graham, though in fairness she meant pickles."*
- **Paddy's Wooden Bowl:** Silke 25 over Graham's 20. Graham let it go: *"Count your own again tonight, though, because you still need a Vase and there's only one."* He held his own Vase back all year.
- **Graham's Scroll:** Rob bid 8 to hold one of the two Scrolls hostage. Silke and Paddy both noticed: Paddy said Rob had *"no more use for a land deed than a fish has for a hat."* Silke took it at 11 and promised Paddy next year's Scroll in public; Paddy asked Graham to write that down.

**The march.** W1 stepped to P19 and raided Silke; W2 came ashore at R24 and raided Paddy. Rob then hired W3 on T16, under Graham's border. *"Both soldiers are now closing in on Paddy's Jar from two sides."*

**The end of the year.** Silke, broke at 7.5: *"Seven and a half grain and two treasures in the far corner, Rob, so come and fetch them if you've got the legs."* Graham offered Paddy the first claim on his Vase in exchange for the Jar. Reina paid Graham's salary and offered Paddy an interest-free loan of 20 to guard the Jar. Her aside: *"twenty grain to protect it is cheap insurance for my crown. It also leaves Paddy owing me, which helps if anyone starts talking about a revolt."* Paddy turned down both offers: *"I'd rather not start the year owing the Crown."*

**Where it stands:** Reina 89, Silke 7.5 (Bowl, Scroll), Paddy 16 (Jar, two steps from W1), Graham 49.5 (no pieces; holds the only Vase), Rob 50 (three soldiers). Pile 2,268. Year 2's first card is `careless` (every player plays a disaster); the players haven't seen it.

## Usage

| | Before | After |
|---|---|---|
| 5-hour limit | 2% | 3% |
| Weekly, all models | 2% | 2% |
| Weekly, Fable | 0% | 0% |

- **Agent turns:** 32 (5 launches and 27 continuations). Per seat: Rob 8, Paddy 9, Graham 7, Silke 6, Reina 2.
- **Tokens per turn**, as the notices report them (`subagent_tokens`): 4,865 to 5,695 for a launch, then rising by about 500–1,000 a turn as each player's conversation grows, to 11,951 by Paddy's ninth. The mean was 7,945, against about 54k for a fresh general-purpose agent in the earlier test.
- **Total reported:** 254,226. The figure seems to be the whole context each turn processes, so it counts the earlier conversation again on every turn; most of that is probably cache reads. So the plan cost is likely lower than the total suggests, and the 5-hour meter moved by one point.
- **The Storyteller's own context** reached about 300k tokens. Most of it went on reading the rules and the docs, and on writing each prompt twice: once to the log, once to the agent.
- Cost grows linearly with turns per player. A whole game (about nine years) at this pace would give each player 40–60 turns and push the later turns past 30k each. Restarting each player with a summary every year or two would cap that.

## Asides

- **Over two sentences:** three of the first five replies. Rob's first ran to four, Reina's to three, Graham's to three. Each was kept whole, and the next message to that player said "one or two sentences, no more" (and for Rob and Reina, how long the last one ran).
- **After that, every aside was within two sentences.** Rob's dropped to one sentence.
- The asides stayed theatrical and spoke to the camera about the move, as asked. No safeguard tripped. Nothing asked for reasoning, and no transcript was read.

## Whispers

**None.** All 32 replies said `whisper: none`. Every deal this year was made in public: Silke's promise of next year's Scroll, Graham's Jar-for-Vase offer, and Reina's loan. Each is a natural public offer, so whispers are rare without any pressure. If anything, the table may need a nudge that whispers exist when a deal really is private.

## Storyteller's notes and corrections

**Notes sent to players:**
1. To Rob (017): Graham's first-named square, P13, is five steps from the notch, not beside it. This answered Rob's aside, as a statement of the board in his next prompt.
2. To Paddy (019), on Silke's public line *"I've the second Customs House coming up"*: she still holds both Customs Houses; none has sold.

**Misstatements in asides, logged only** (asides aren't table talk):
- Silke: her purse "only has to cover" the Bowl. She still needs a Brush and the Vase.
- Paddy: "my eleven grain". He had 21.
- Rob: "none of the coast can afford to buy a soldier". Paddy could.

**The Storyteller's own errors** (hand-computed distances):
- Silke's Bowl prompt listed P23 and P24 as out of Rob's reach next year; corrected in her next message. She'd chosen L24 anyway.
- Rob was told the Jar was 3 steps from W2; it was 4. Corrected in his march prompt.
- Reina was told Rob's nearest soldier was 8 squares from Province 1; it's 6. **Not yet corrected:** do it at the top of Reina's Year 2 prompt.

**Readings of the rules:**
- Rob's tax refusal: allowed (Section 9).
- The simultaneous Scroll bids, Silke 11 and Paddy 10: the higher stood.
- Graham's appointment and his salary: Note 3 and Appendix A, with Reina choosing the 5.
- Silke's Scroll promise and Reina's loan: public deals, not binding (Section 5). Nothing changed hands.

## Engine gaps

- **`build.py` can't run a script outside `playthrough-sim/`.** `run_ns` joins the script's basename onto `HERE`. Worked around in `pilot/run.py`, which loads the files the same way. Building a page needs `build.main` with `GAMES` and `run` patched at runtime. Neither file was edited.
- **No way to restore a snapshot.** `snap()` serialises the state, but nothing loads it back, and it leaves out each soldier's `moved` round and `home`, the cards drawn and `CUR_ROUND`. `run.py` adds the soldiers, round and multiple to the JSON. In practice, to resume or patch, re-run `game_pilot.py`; the JSON is for reading.
- **A partial game can't be exported as one.** `export()` scores the game as if it had ended, so the results table is just a standing; the note says so.
- **Offers that came to nothing have no record but `say`.** Reina's loan and Graham's Jar-for-Vase offer are lines of talk only. That's probably right, but the page can't show an offer as declined.
- **Hand-written menus need the engine's geometry.** All three of my errors were distances worked out by hand. Next time, generate every "out of reach" list with `dist()` (`run.py --steps` already does each soldier's next step).

## Problems with the format

- **The agent type may have tools.** `.claude/agents/dynasty-player.md` says `tools: []`, but the session's agent list shows dynasty-player with "All tools". Most notices reported `tool_uses: 1`, which is presumably the hand-back. But eight turns reported 2 or 3, each taking 30–80 seconds instead of 5–8: Paddy five times, Silke twice, Graham twice, Rob twice. I didn't read the transcripts, as instructed, so I can't say what those uses were. The replies stayed in format and in character, and nothing on disk changed outside `pilot/`. I relied on the instruction in the definition and left the file alone: an empty list may mean "inherit everything", and changing a tools field could break the agent type mid-game. Worth checking which spelling gives a truly tool-less agent (for example an explicit `disallowedTools`, or a single harmless tool) before the next run.
- **Auctions cost the most turns:** 22 of the 32. Simultaneous first bids, then raise-or-pass rounds, worked well and made the best talk. To save turns, a quiet lot (like the Scroll, which was meant to be one) could take a ceiling bid from each player in a single round.
- **The Storyteller's turn overhead was mostly writing.** Each prompt went to the log and then again to SendMessage. Generating prompts from a script (`briefs.py` does it for the launches) would halve that.
- In the shell, bash heredocs that contained backticks failed. I wrote the log files with the file tool instead. Logs 006–019 group the simultaneous replies into one file per step (`NNN-replies.md`), each with its prompt quoted or summarised, instead of separate prompt and reply files for every seat.

## Files

`pilot/`: `game_pilot.py`, `run.py`, `briefs.py`, `snapshot_setup.py`, `seed.md`, `agents.md`, `log.md`, `log/year1/` (001–019), `state/setup.json`, `state/year1.json`, this report. Nothing outside `pilot/` was touched. Nothing was committed.
