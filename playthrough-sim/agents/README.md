# Agent-played playthroughs

The reusable code and notes for games played by agents rather than written by hand. Each seat is played by its own `dynasty-player` agent (`.claude/agents/dynasty-player.md`) in character. A Storyteller session referees through the engine (`../engine.py`), and a Director session runs the game chapter by chapter. Each game's record lives in its own folder under `../../playthroughs/`, and the finished games are built into `../../playthrough.html`, the main playthrough page. The older scripted games are in `playthrough-scripted.html`.

| File | What it is |
|---|---|
| `DIRECTOR.md` | How the Director runs a game: choosing the deck, the actors' notes, a Storyteller per chapter, checking each chapter, steering toward the game's `scenario.md` |
| `STORYTELLER.md` | How a Storyteller runs a chapter: launching players, turns, auctions by ceiling, narration, closing. Start here. |
| `rules-digest.md` | The rules a Storyteller needs, compact enough to read instead of the rulebook, with section numbers |
| `storyteller-voice.md` | The narrator's voice, shared by every game |
| `player-agent.md` | The player agent: how it's launched and continued, and the check that it has no tools |
| `run.py` | The referee: runs a game's `game.py` through the engine and prints the state (`--steps`, `--snapshot`) |
| `geo.py` | Board geometry for prompts (reach, distances, safe squares), computed by the engine, never by hand |
| `briefs.py` | Writes every prompt from the engine state and the table talk, logs it once, and resolves ceiling auctions. Works at any table: the seats, roles, objectives and table jobs come from the engine. Menus for the Emperor's year, the Official's tax, the Gentry's rent, the Scholar's card, new land, the march, and a year's auctions in one prompt |
| `deck_scout.py` | Scouts I Ching deck orders before a game: what a seed's shuffle does to each year (harvests, population, incomes, disasters), and a search for seeds that fit a test |
| `snapshot_setup.py` | Saves `state/setup.json`, the state before Year 1 |
| `build_real.py` | Builds `playthrough.html` from the games it lists |

Run the tools from a game's folder, for example:

```sh
cd playthroughs/peasant-collapse
python ../../playthrough-sim/agents/run.py
```

Build the page from the repository root:

```sh
python playthrough-sim/agents/build_real.py
```

The rules for running a game safely, which the Storyteller notes also give: keep the framing theatrical (a player's aside is a line to the camera, never a request for its reasoning), never read an agent's transcript, and take every distance and every legality check from the engine.
