# History

A chronological log of requests and decisions. Quotes are Manish's own words. Earlier stretches survive only as summaries, so they're less detailed.

Entries before "Renumbered games, land everywhere" use the old game numbers; that section has the map.

## Before the clean repo (summarised)

- Manish owns a 1969 copy of Dynasty: map, pieces, I Ching cards and the eight booklets. He wanted the per-role booklets turned into a **modern rulebook that explains general concepts first and then the per-role rules**.
- Claude worked out the pieces from photos and scans, and drafted the rulebook as a single HTML page, which was published.
- Next came an **interactive playthrough** page: one tab per year, a transcript separating actions from dialogue, hover reasoning, an annotated map, bid ladders for auctions, and an objectives tracker. The voice was tuned over several rounds: dialogue as roleplay, thoughts as several players who know they're playing, in the tone of a tabletop RPG player. Full names go in the players table and short names in the transcript. Mobile support was added. Manish asked not to put mobile-UI text into documents.
- A "How long a game takes" section was added to the rulebook ("yeah go ahead"), including the short-game rule.
- Game 1 was later audited against the real cards and rules. Fixes: an invented Year 8 card, wrong harvest qualities, missing and out-of-order disasters, inconsistent realia sets, a fictional Harvest Pile, an illegal seizure of stock, and several wrong amounts. All were corrected and every quoted number re-checked.

## Multiple playthroughs

- "Actually, could you add multiple playthroughs? Maybe tabs at the top for selecting between them. This is a full game, but maybe add a game with fewer players, and a short game?"
- Choices: **5-player peasant game**; **4-player upper game, 8 rounds**; the survival ending: **"Yes, in the small game"**.
- The engine grew rule guards (seat-change legality, card uniqueness, a real Harvest Pile bank, disasters in booklet order, a `home()` rule for returned pieces that became a rulebook note). The page gained the game selector with hash links.
- "files are in C:\Users\manishearth\dev\dynasty. There's a git repo there, I can push when needed."

## The clean repo (the copyright conversation)

- The copyright question: the booklets are under copyright until 2064, an orphan work. Manish had already rewritten the rules in his own words, and wanted to archive the PDFs (scans go on his personal site, not GitHub).
- "we'd want to have a reusable map and something listing the i ching cards". The cards "are not real i ching".
- "I made a new dynasty-new folder… Try to make the map somewhat pretty". That produced `map.svg`/`map.json` (an accurate 30 × 22 grid redrawn from a photo of the board), `i-ching.json`/`.html` (reworded cards), `images/` glyphs, and `add_glyphs.py`.
- Glyphs were wired into the playthrough, and `cards.py` switched to the reworded card text.
- That conversation flagged that the rulebook's schematic map didn't match `map.svg`. Manish: "yeah i'll work on the rulebook soon".

## Moving the playthrough to dynasty-new

- "Okay, we have moved over to the dynasty-new folder. All work on the playthrough should continue there."
- "Make sure to move over the sim folder (playthrough-sim) and give it detailed documentation". That produced `playthrough-sim/README.md` and the four documents in `docs/`.

## Cut-outs

- "what are the sizes of the reservoir/irrigation pieces? can we update the setup instructions … to be abundantly clear about them?"
- "the wood and canal pieces have slots on the map for them. see if you can understand the intent of the game as to their size"
- "If there is no single size that is fine!"
- "wait, and don't change the rulebook yet since a different task is working on it" … then "ok you can go ahead and edit the rulebook now".
- Follow-up edits:
  - Drop the "where the size comes from" section.
  - "What the booklet says it holds" becomes "what it holds".
  - Replace the long explanation with "there is no single correct size, but we have some suggestions here".
  - Show the suggested cut-out as "a small drawing of squares".
- Asked whether the booklet is inconsistent about "Irrigation System" and "Reservoir/Irrigation". It isn't: the names reflect whether the system contains a reservoir (see "Naming the water works" in `RULINGS.md`).

## Rulebook fixes from screenshots

- "the formatting of '47 wooden pieces' is incorrect here". It was a small caps table caption; it's now a bold lead-in like the other components.
- "the provinces section should not have the province list at the top". Removed.
- "in the per-province sections, the province list should be clickable". The bands are now links.

## Realia on the map

- "realia are supposed to be placed on the map." The rule was already in Section 10, from the booklets.
- Then the question was whether unsold starting stock goes on the map. Manish: "putting them on the map worries me about the lack of space (especially with large reservoirs), putting them off the map makes it unclear when they go on, and it allows players to hide stuff from the warlord. thoughts?"
- After the analysis: "okay, that works!", which became Note 10.

## Latest round

- "let's consistently call it reservoir. Please update the rulebook and the playthroughs". Clarified: **only Provinces 3 and 7**; Province 2 stays Irrigation System.
- "during setup, and in the realia page under starting stock, we should highlight that players must place realia immediately on the board". Clarified: **bought pieces go on at once**, which keeps Note 10.
- Playthrough requests (done in the Claude Code session below):
  - "Playthroughs should have a setup tab that shows the players setting things up"
  - "Replace Ken Nakamura with Noah Lott"
  - "The folder now has an accurate map, rather than a representational one. Can the playthroughs be improved to use this? This may change the game flow, please carefully recheck that the game runs the same."
- "Do rulebook work first so I can continue improving the rulebook in a second conversation." Done: the naming and placement edits.
- Warlord movement: Claude raised the booklet's two sentences and asked. Manish chose "Discuss first", then, after the analysis, "Yeah, update the rulebook first". Note 16 is now one square a round.
- "We shall migrate to claude code. Can you make a handoff folder … I don't want to lose any design intent. Do not yet hand off the prompt, let us discuss the task first". That produced this folder, then called `handoff/`, with a task prompt for Claude Code.

## The first Claude Code session (2026-10-25)

The handoff prompt asked for four changes to the playthroughs: the Reservoir naming, the Noah Lott rename, a Setup tab in each game, and moving the games onto the accurate map with strict soldier rules. Manish: "the overall arc should stay the same. if things need to move around, they can. try to keep it as interesting as the original."

- **Rules questions asked first.** River tolls go to the province stepped into, nothing in undeveloped land; a Wall link or canal section is crossed when a step cuts its line, a cut-out when a soldier steps on it, and palaces aren't crossed; soldiers of one owner may share a square. On a bought soldier after a seat change Manish asked "Which makes more sense in the game mechanics?"; the answer was that it stays with the player who bought it, like grain. All recorded in `RULINGS.md`.
- "why back up the sim page? can you make a git commit instead?" — a baseline commit before the rework, instead of scratch copies.
- "note that other conversations are working on other files here so be careful modifying non-playthrough stuff" — see "Working in parallel" in `project.md`.
- A draft of the re-routed peasant game and its Setup tab was shown first. Manish confirmed the judgement calls: "Yes on the sea. Yes on works tolls. yes on raids, yes on realia" — soldiers can't enter the sea (Note 16's "only through the gap" depends on it), a soldier stepping onto an un-raided province square always raids it, realia can't go on raided squares or under works.
- "You should continue till completion. Also, design a fourth game that has 8 players and runs to full public works completion, and a fifth game that works with 6 players (and ends however you'd like). Continue to noodle on improving the flow of the games and having good banter and internal thought process." Games 4 and 5 were written; game 4 deals the booklets afresh (`setup(cast=...)`), game 5 ends with the Warlord on the throne.
- From the rulebook session: a raid on a canal, irrigation or reservoir square is an ordinary raid, and the Wall can't be raided; and `RULINGS.md` became the single list of rulings, which every session now adds to.
- Two independent reviews checked the games against the rules and the ledger. They found auction-rule slips (pieces not re-auctioned, players passing up the piece that completes their set without a reason), canal costs charged to the wrong provinces, and many quoted numbers and cross-evening references that were off. All were fixed.
- "rename handoff/ to design/ and clean up the files so that they are not just about the handoff but rather permanent live docs for design. You may push automatically" — this folder.

## Names and glyphs (2026-10-25)

- "Let's also rename Noah Lott to Noah Tall." The Scholar's pun is now "know-it-all". The short name stays Noah.
- "Make sure "reservoir" is always in caps in all docs when it has the image next to it." Wherever a glyph marks the word, it reads **Reservoir** (or **Reservoirs**). `tools/add_glyphs.py` capitalises it when it adds the glyph, and the playthrough page does the same in the browser, so new text can't slip.

## Reference cards (2026-10-25, the clean-repo conversation)

- "Two sets of reference cards; one per-player, one general one. General one contains turn order/stuff like that (ask me which things make sense to include). per-player includes the harvest tables, the things they need to collect, the things they need to do each round, what they are owed. Cards should be two sided. make a separate html page like we did for the i ching."
- Asked which extras belong on the general card. Picked: public works, money at a glance, Harvest Pile in/out, realia ownership. Not picked: the population and I Ching tracker, climbing seats, revolt and Chaos, game end. Size: half letter.
- Corrections: new harvest squares "should say 'only available after 2x population'"; income tables "should probably also mention +20M per new harvest square"; the Warlord's card should say he can demand the full cost from the Emperor when raiding the Emperor's buildings, then "Should we split this into 'raiding realia' and 'raiding emperor works'?" (yes).
- "it seems like the warlord can't raid the wall, right?" Right: it stands outside every province. Raids on canal, irrigation and reservoir squares became ordinary raids ("just a plain sentence is fine. I think clarifications also belong in RULINGS"). `RULINGS.md` was created as the single list.
- "Let's go ahead and hand this off to claude-code as well." That produced [`reference-cards.md`](reference-cards.md).

## The map's look in the playthrough (2026-10-25)

- "Would it be possible to use the fancier map.svg-like rendering in the playthrough? of course with the stuff around the borders removed and the labels removed. It might be worth splitting map.svg into layers somehow so that it can be reused this way." `tools/build_map.py` now draws the map as named layers; `map.svg` stacks them all, and `map-board.svg` holds only the ground, which the playthrough uses as its board. The page keeps its own small player labels.
- "I don't think we need a local preview server since you can just give me links to open in my browser. Clean that up." `.claude/launch.json` is gone; give Manish `file:///` links.


## The rulebook's contents, phone tables and map (2026-10-25)

- "For the instructions can you have the table of contents follow as a sidebar when scrolling on desktop (and perhaps have a topbar that can be clicked on mobile). it should remain printable". A script at the end of the rulebook copies the Contents list into a fixed sidebar (76rem and wider) or a tap-to-open bar (narrower), marking the section being read. Both are hidden in print; the Contents page still prints.
- "Yes, make the wide tables fit on phone screens." Tables tighten their padding and header type at 640px and below; every table fits at 375px.
- "Also please use the new fancy map in the rulebook instead of the 'representative' one". Section 3 now shows `map.svg`. On that map the Warlord's land also borders Provinces 4 and 5, so the expansion paragraph says so.
- "Also when done rename to rulebook.html". `combined-dynasty-rulebook.html` is now `rulebook.html`, and every reference to it was updated.

## Running out of grain (2026-10-25)

- Manish chose "sell before you sink" (the task in `handoff/PROMPT-negative-grain.md`): sell realia back to the Harvest Pile first, then debt, and a player in debt is locked out of spending. The details he settled: a piece sold back "should go to the harvest pile and auctioned off during auction. harvest pile auctions off all unused pieces during the next auction"; a Chaos acclamation may seat a player in debt; a bid must be covered by grain in hand; a displaced player's debt passes to the mover.
- "You can also make rulebook changes. Make sure to add all of these to RULINGS." It became rulebook Note 7 (Section 8, with an Appendix D entry); the old Notes 7–19 are now 8–20 everywhere they're cited. `RULINGS.md` records it, with two new open questions (a negative Emperor's salaries, selling soldiers back).
- The engine enforces it (`sell_back`, `lot(PILE, ...)`, `act(..., deal=True)`, the debt guards). Only game 1 ever runs out: Clark, Graham, Rich and Rob now sell their last pieces in Years 11 and 12 before sinking, and the Harvest Pile ends the game holding them.
- "Add the first suggestion: a player in debt counts as facing starvation, so debt is itself a listed cause for revolt." Section 16 now lists debt as a seventh cause, after the six from the booklets, with Note 7 and its Appendix D entry saying so.

## New land, and independent games (2026-10-25)

- From the "Harvest tile purchase patterns" session: nobody bought new harvest squares because only game 1 ever reached a doubled population, and the engine couldn't model them. Manish: "update the engine to support harvest tile purchase … mention in the rulebook and RULINGS that players can buy an unlimited number of harvest tiles per turn, but also that this route is only available later in the game because of the 2x population requirement". He chose: a game 4 land rush, bought squares raidable like the province, and purchases separate from the round's one project.
- Game 4 had drawn both "half" cards, which the cards' own caps forbid; the engine now enforces them. Its Year 8 card became a doubling, and Years 8–10 became the land rush: the Pagoda in Year 8, land everywhere, the Wall from the land's tax in Year 9, the crown's own canal last. Clark, locked out, sells his complete set back to the pile.
- "I've noticed that the last two playthroughs seem to treat the player names as fungible for setup. Please use the players matching the roles for each game set up … Don't think of these as multiple sequential playthroughs with persistent personalities, each one is an independent playthrough … keep each bit of banter to be within the same game." And: "don't change the actual game content. just shuffle the names around." Games 4 and 5 were renamed so everyone sits in their own province, and every cross-game reference in games 2–5 was removed. The engine's `cast=` option is gone.

## Renumbered games, land everywhere (2026-10-25)

- Manish renumbered and retitled the games. Old → new: 1 → 2, 2 → 4, 3 → 3, 4 → 1, 5 → 5.
  1. `game1_full.py`, "The full game" (was game 4, "The long game", `game4_complete.py`).
  2. `game2_trashfire.py`, "A slow trashfire" (was game 1, "The full game", `game1_full.py`).
  3. `game3_short.py`, "The short game", unchanged.
  4. `game4_peasant.py`, "The peasant game" (was game 2, `game2_peasant.py`).
  5. `game5_six.py`, "Land, Robbed" (was "The six-player game"); Rob Land wins it.
  The page keys are now `full`, `trashfire`, `short`, `peasant` and `robbed`.
- Every game but the fifth now reaches a doubled population and buys land:
  - **Game 2**: in Year 10 Reina refuses to subsidise Silke's sea and buys E18 and E19 below the Wall for Province 1 alone, 40. Graham cites it in the revolt, and takes the throne with 152.
  - **Game 3**: the Year 7 card is now a doubling. Noah buys K25, J25 and K26, sea, with Reina paying half (30 each). Verdicts unchanged; Rich wins the tiebreak outright with 146.5.
  - **Game 4**: the Year 8 card is now a doubling. Rob threatens revolt over cause six; Paddy pays Reina 130 and most of the Wall to keep the game ending. Silke (T16, T17, the Warlord's land), Graham (R25, S26, sea) and Paddy (M26, N26, sea) buy land, the crown paying 10 of each 40. Still the survival ending with Reina at 2.5; verdicts unchanged, and Rob finishes richest with 157.
- The top-level `README.md` now describes `playthrough.html` as five games, not three (off `open-work.md`).

## The strip below the Wall opens per province (2026-10-25)

- Manish noticed Reina developing the strip below the Wall with the links above her unfinished. The Emperor's booklet: "You or Provinces 2 and 3 may develop the New Land below the Great Wall when 4 sections in each Province have been built." He chose the per-province reading. The engine now gates Province 1's strip squares on its own four links; Reina's purchases in games 1 and 2 moved to the sea (F23–F26 and H25; F23 and F24) with identical ledgers.

