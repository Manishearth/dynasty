# How the Director runs a game

The Director is one session per game. It never plays a seat or referees a move: it chooses the deck, gives the actors their notes, starts a Storyteller for each chapter, checks each chapter's record, and nudges the game towards the arc in the game's `scenario.md`. The Storyteller runs the table (`STORYTELLER.md`); the players are `dynasty-player` agents with no tools.

## Before Chapter 1

1. **Read** the game's `scenario.md`, then `STORYTELLER.md`, `rules-digest.md` and the game's `seed.md`. Check whether your startup brief says **you're the only Director running**. That decides whether you may rebuild the page (see "Messages and the page" below). If it doesn't say, assume you aren't.
2. **Test the deck.** The I Ching deck is the game's only chance. Run `deck_scout.py` on the recommended seed and on the alternatives, from the game's folder:

   ```sh
   python ../../playthrough-sim/agents/deck_scout.py 350 --seats 1,2,3,5,6,8 --years 12
   python ../../playthrough-sim/agents/deck_scout.py --search 1-20000 --seats 1,2,3,5,6,8 --years 12 --where "land<=3 and lean_early>=2"
   ```

   It shows the year each population card takes effect, the bare income of every seat each year, the lean years and who plays a personal disaster. Pick the deck that gives the arc room to happen, not one that forces it. Then rewrite `seed.md`'s seed and deck order (the scout prints the line to paste), and say why in its steering log.
3. **Write the actor's notes.** Each character's `ledger.md` entry has a **Playing it** line. A note gives the character a stance for this game, in a sentence or two: "a builder in a hurry, who means to tax hard while incomes are positive". It never gives them a move to make, a number or a result. Every launch prompt carries the entry, so the note reaches the player at each chapter.
4. **Snapshot the setup.** Run `python ../../playthrough-sim/agents/snapshot_setup.py` once the setup lines in `game.py` are final. In a game with a Warlord, the Storyteller places the army in the first prompt (`place_army`) and snapshots again.
5. **Park the Storytellers.** Start a session for every chapter at once, in one turn Manish approves, up to seven. Each brief says only: you are a chapter Storyteller for `<game>`; wait for a message telling you which chapter. Start them in this session's permission mode, or they hold messages for approval. When a chapter is due, wake the next one with SendMessage: the chapter number and years, the handoff to read, the rule changes since the game began, and any steering for this chapter. A parked session costs nothing until it's woken.
6. **Make each Storyteller a top-level session, in your section.** A session you start nests under you, and the app then wakes you every time it ends a turn, which floods you with messages. Straight after starting each Storyteller:
   - **Detach it:** `mcp__ccd_session_mgmt__detach_session` with its id. It keeps reporting to you by SendMessage, at the end of each year and of its chapter (`STORYTELLER.md`), which is all you need.
   - **File it with you:** look up your own sidebar section (`mcp__ccd_session_mgmt__get_session` with `"self"`, then `mcp__ccd_sidebar__list_sections` for its id), and move the Storyteller there with `mcp__ccd_sidebar__move_sessions`. If you aren't in a section, use the game's section if Manish named one, or else "Playthrough".

## Each chapter

- **Wake the next Storyteller** with the chapter's brief. Don't brief a chapter before the last one has closed.
- **Check the record** when it reports: `run.py` runs clean, `game.py` has the chapter marker, the ledger and diaries are current, and the narration isn't in `game.py`. Check its figures against the engine (`run_ns`: seats, stock, `held`, `owed()`), not against the Storyteller's prose. The short game's check caught a handoff that said 1,030 owed in works at a table that owed 810.
- **Revisit every actor's note** before the next chapter. A note goes stale once its character changes seats or sells the piece it names. Rewrite it only between chapters, and log each rewrite in `seed.md`.
- **Write the handoff** (`handoff/chapter-N.md`): where the game stands, open threads, and any steering for the next chapter.
- **Leave `game.py` alone mid-chapter.** If it needs a change while a Storyteller is playing, ask the Storyteller to make it. To see how far a chapter has got, look at the times on its `log/` files, not at its transcript.
- **Record each finished year** in your status file (below). Rebuild the page only if you're the only Director running.

## Messages and the page

**The message cap.** The desktop app lets a session send about 10 messages to other sessions after Manish last typed in it. Past that it pauses them until he types again, and overnight nobody does. So spend messages only where nothing else will do:
- **Wake each chapter's Storyteller:** one message per chapter.
- **A note to a Storyteller** only when something truly needs one.
- **One message to the main session when the game ends.** None during play, unless something needs Manish's decision. Then the game waits for the morning.

A Storyteller's reports to you come out of its own allowance, not yours. Keep the Storyteller reporting at the end of each year and of the chapter (`STORYTELLER.md`), and don't reply unless you must.

**Status, without messages.** After each finished year that you've checked, add one line to `<game>-status.md` in the shared notes folder named in your startup prompt: what happened, the grain, any steering, and the last year rebuilt on the page. It costs no messages, and the main session reads it in the morning.

**The page.** `build_real.py` rebuilds every game into one file, `playthroughs-real.html`, so two Directors rebuilding at once would race.
- **If your startup brief says you're the only Director running:** you own the page. Rebuild live after each checked year, without asking: set your game's `IN_PROGRESS` entry to that year, run `python playthrough-sim/agents/build_real.py` from the repo root, and note it in your status file. Touch only your game's lines in `build_real.py`.
- **Otherwise:** don't rebuild, and don't edit `build_real.py`. The status file records your last finished year, and the main session rebuilds every game at once in the morning.

**Shared tools.** `engine.py`, `briefs.py`, `run.py` and the guides serve every game. Before changing one, ask the main session, since another Director may be in the same file. After the change, compare `briefs.py ... --dry` prompts against HEAD for every game, and make sure only the cases you meant to change differ.

## Steering

Manish wants each game nudged towards its arc. The Director may steer, between chapters, with these levers:

| Lever | How | Limits |
|---|---|---|
| The deck | The seed, chosen before Chapter 1 with `deck_scout.py` | Never reorder the deck once play has started |
| Actor's notes | The **Playing it** line in `ledger.md` | A stance, never a move. Change it between chapters, never mid-chapter |
| Storyteller's tips | A public `note` beginning "Storyteller's tip:" and naming the player. File it without `--to`, which would show the note only to that player | Strategy from what the table can see; at most one per player per chapter; never the deck, anyone's asides, whispers or limits. Each tip goes in `ledger.md` under "Storyteller's tips" |
| Length | Where a chapter or the game stops. For an agreed short game (Note 19), set `LAST_ROUND = n` in `game.py`, and `briefs.py` puts the round count, the scoring and the late-land warning on every card | Say so at the table before the last chapter starts |

Never steer by misstating a rule, the board or anyone's grain; by changing what the engine computes; by writing a player's words; by passing one player another's hidden information; or by reading an agent's transcript. The players' choices stay theirs. **If the game goes somewhere else, let it,** record what happened, and change the subtitle. A design-check game (its `scenario.md` says so) is steered lightly or not at all, since its result is evidence.

List every piece of steering in `seed.md`'s steering log when it happens: what, when and why.

**Rules corrections aren't steering, but they can decide a game.** The Storyteller must correct any public misstatement of the rules. In the short game, its note that pieces on the board may be traded was followed at once by the trade that took the throne. Expect this, and report it in `REPORT.md` under "Not steering, but…".

**What a small table does to the auction.** At four or five seats each seller holds two types and chooses which goes up. A seller sells the other type first and holds the key piece back, so the unsold-lot rule rarely fires. A scenario meant to test that rule needs sellers who hold only one type.

## The end

- Give the game its title and subtitle in `game.py`'s `setup()` (players · years · how it ended), and the result and epilogue in `export()`; pass `no_winners=True` for a collapse.
- Write `REPORT.md`: what happened, what the rules did, and anything that needs a ruling.
- If you own the page, drop the game from `IN_PROGRESS` in `build_real.py` and rebuild. Otherwise, say in your status file and your final message that it's ready to drop. Either way, update `playthroughs/README.md`.
- Send the main session your one message: the result, and where `REPORT.md` is.

The framing rules from `STORYTELLER.md` hold for the Director too: the aside is a line to the camera, never a request for reasoning, and no one reads an agent's transcript.
