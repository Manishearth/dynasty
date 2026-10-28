# Player agents: the peasant's game

Each seat is one `dynasty-player` agent (`.claude/agents/dynasty-player.md`), launched fresh at the start of each chapter (`briefs.py prompt ... launch`, which carries the ledger entry and the diary) and continued with SendMessage for the rest of that chapter. An agent can be resumed by id only from the session that launched it.
