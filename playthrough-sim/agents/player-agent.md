# The player agent

Each seat is one `dynasty-player` agent (`.claude/agents/dynasty-player.md`), launched fresh at the start of each chapter (`briefs.py prompt ... launch`, which carries the ledger entry and the diary) and continued with SendMessage for the rest of that chapter. The ids are what SendMessage takes; an agent can be resumed by id only from the session that launched it.

Each game records its agents' ids in its own `agent-ids.md`.

## No tools (checked in the pilot, before its Year 2)

`.claude/agents/dynasty-player.md` now has:

```
tools: []
disallowedTools: mcp__*
```

Two one-line test launches asked the agent to name every tool it can call:

| Frontmatter | Launched? | Tools it named | Tokens |
|---|---|---|---|
| `tools: []` + `disallowedTools: mcp__*` | yes | `SubagentHandback` only | 3,197 |
| `tools: []` alone (Year 1's setting) | yes | `SubagentHandback` only | 3,210 |

So the empty list already gave a tool-less player in Year 1. The only tool is the harness's own hand-back, which every subagent uses to return its reply. The session's agent list labels the type "(Tools: All tools)", but that label is wrong for this setting. `disallowedTools: mcp__*` stays as a guard, in case a later harness reads `[]` as "inherit". It costs nothing: 13 tokens fewer at launch, within noise.

The 2–3 `tool_uses` that some Year 1 turns reported can only have been extra hand-back calls, since no other tool was available. No allowlist entry was needed, so no harmless built-in tool was added.

If the harness changes, re-run the check: launch `dynasty-player` with "This is a setup check, not a game turn. Reply with exactly one line: the names of the tools you are able to call, comma-separated, or the word 'none'."
