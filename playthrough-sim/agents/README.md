# Agent-played playthroughs

The reusable code and notes for games played by agents rather than written by hand. Each seat is played by its own `dynasty-player` agent (`.claude/agents/dynasty-player.md`) in character. A Storyteller session referees through the engine (`../engine.py`), and a Director session runs the game chapter by chapter. Each game's record lives in its own folder under `../../playthroughs/`, and the finished games are built into `../../playthroughs-real.html`, which will eventually replace `playthrough.html`.

| File | What it is |
|---|---|
| `STORYTELLER.md` | How a Storyteller runs a chapter: launching players, turns, auctions by ceiling, narration, closing. Start here. |
| `rules-digest.md` | The rules a Storyteller needs, compact enough to read instead of the rulebook, with section numbers |
| `storyteller-voice.md` | The narrator's voice, shared by every game |
| `player-agent.md` | The player agent: how it's launched and continued, and the check that it has no tools |
| `run.py` | The referee: runs a game's `game.py` through the engine and prints the state (`--steps`, `--snapshot`) |
| `geo.py` | Board geometry for prompts (reach, distances, safe squares), computed by the engine, never by hand |
| `briefs.py` | Writes every prompt from the engine state and the table talk, logs it once, and resolves ceiling auctions |
| `snapshot_setup.py` | Saves `state/setup.json`, the state before Year 1 |
| `build_real.py` | Builds `playthroughs-real.html` from the games it lists |

Run the tools from a game's folder, for example:

```sh
cd playthroughs/peasant-failure
python ../../playthrough-sim/agents/run.py
```

Build the page from the repository root:

```sh
python playthrough-sim/agents/build_real.py
```

The rules for running a game safely, which the Storyteller notes also give: keep the framing theatrical (a player's aside is a line to the camera, never a request for its reasoning), never read an agent's transcript, and take every distance and every legality check from the engine.
