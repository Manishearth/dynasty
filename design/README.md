# Design

The living design documents for the Dynasty revival: what the project is, what Manish wants from it, who the playthrough cast are, how we got here, what's still open, and what went wrong along the way. They're for anyone picking up work on this repo, human or Claude.

| File | What it holds |
|---|---|
| [`project.md`](project.md) | What the project is, every file in the repo, how to build it, the copyright constraints, and how parallel sessions share the repo |
| [`design-intent.md`](design-intent.md) | Manish's standing preferences for the rulebook and the playthroughs. Treat these as requirements. |
| [`cast.md`](cast.md) | The eight friends in the playthroughs: names (they're puns), how each one thinks, and what happened to them in each game |
| [`history.md`](history.md) | A chronological log of requests and decisions, with Manish's own wording where it matters |
| [`open-work.md`](open-work.md) | Work still to do, open questions, and known issues |
| [`warlord-balance.md`](warlord-balance.md) | Simulated Warlord campaigns (`tools/warlord_sim.py`): what they model, the results, and why the Warlord hires reinforcements and gets a palace wildcard at eight players |
| [`lessons.md`](lessons.md) | Mistakes caught along the way, worth not repeating |
| [`reference-cards.md`](reference-cards.md) | The printable reference cards: what Manish asked for, the layout, printing, and where each number comes from |

Rules questions don't live here. [`../RULINGS.md`](../RULINGS.md) is the single list of every ruling, clarification and engine assumption, with its reasoning, and its Open questions section is where unsettled rules wait for Manish. The playthrough generator documents itself in [`../playthrough-sim/`](../playthrough-sim/README.md).

**Keep these current.** When a decision is made, add it to `history.md`; when work is finished, take it off `open-work.md`; when a preference becomes clear, put it in `design-intent.md`. If something here disagrees with the files, the files win, and this folder should be fixed.

How Manish likes to work: he likes clarifying questions. Ask before starting anything expensive or ambiguous, with a recommended option first. He wants the sessions to be fun.
