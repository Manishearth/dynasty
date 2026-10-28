# Handoff after Chapter 7 ("Every Square, in Full": Year 13)

For the Chapter 8 Storyteller. Your chapter is **Year 14, and on until the game ends** (or the stop rule ends the chapter at a year's end). The files hold the details: `ledger.md`, `narration.md`, `diaries/`, `log/year13/`, `state/year13.json`.

The rules from earlier handoffs that still hold:
- the standing rules (`chapter-0.md`);
- the tip rules (`chapter-3.md`);
- the unsold-lot rule, corrections in place, and launch text sent exactly as printed (`chapter-4.md`);
- hunger, land and revolt (`chapter-5.md`);
- **how the game ends and how to write the ending** (`chapter-6.md`, "How the game ends"): read that section closely.

Read first: `../../playthrough-sim/agents/STORYTELLER.md`, `rules-digest.md` ("Grain running out", "Revolt and Chaos", "Ending and scoring"), `storyteller-voice.md`, then `ledger.md`, `agent-ids.md` and the last few files of `log/year13/`.

## Where the game stands (end of Year 13)

**The game didn't end in Year 13.** Reina offered to build the last work at the crown's full cost, then promised the crown would pay "every new square, in full". The table bought 520 of land on her word, and the crown went from 474 to 4. She asked Graham to pay 26 of the 30 for the irrigation; he refused ("your words, not mine"), and nothing was built. Then Rob raided her for 10 she didn't have.

| Seat | Now | Drew | Grain |
|---|---|---|---|
| 1 Emperor | Reina | Emperor | **−22 (in debt)** |
| 2 Official | Graham | Wheat | 86.5 |
| 3 Gentry | Rich | Gentry | 66.5 |
| 4 Scholar | **Noah** (since Year 13) | Scholar | 153.5 |
| 5 Silk | Clark | Official | 66.5 |
| 6 Rice | **Silke** | Silk | 64.5 |
| 7 Wheat | Paddy | Rice | 54.5 |
| 8 Warlord | Rob | Warlord | 198.5 |

- **Works owed: 30, the Province 2 Irrigation System,** negotiated with Graham. Building it ends the game.
- **Reina is in debt.** A player in debt can't pay a share of a work, buy, bid, trade or give grain, and every bag she receives pays the debt first (N7). So the crown can't build until its grain is back above zero, or someone else pays the whole 30. Debt is also **a cause for revolt** (§16): any player may revolt if two others agree. Chaos means no tax, salaries or works until a new Emperor is acclaimed. Nobody has proposed one yet.
- **Population ×3, 60 squares of new land** bought in all. Clark now holds 18 of them.
- **Rob** needs raided pieces from two of Graham, Rich and Silke, the palace wildcard already used. The cards print it.
- **The deck:**
  - Year 14 draws `double3`: a good harvest, and **the population doubles again, to ×6**. That's the cap: the doubling has now counted twice.
  - Year 15 draws `double1`, past its cap, so it's only a good harvest.

  The engine applies both. Don't hint at either before it's turned.

## Year 14's arithmetic (from the engine; for you, not to state as a forecast)

A good harvest at ×6, by seat, including works bonuses and new land:

| Seat | Player | Income |
|---|---|---|
| 1 | Reina | −120 |
| 2 | Graham | +100 |
| 3 | Rich | −40 |
| 4 | Noah | −20 |
| 5 | Clark | +240 |
| 6 | Silke | +100 |
| 7 | Paddy | −40 |
| 8 | Rob | −80 |

- Only Graham, Clark and Silke owe tax. At a rate r the tax brings in 440 × r: 88 at 20%, 220 at 50%.
- The tax comes after the harvest, so Reina's −120 lands first: about −142 before the tax.
- The tax pays her debt first. She needs about 172 in tax to fund the 30 herself, so a rate of about 40% or more. Alternatively, Graham, or anyone, could pay the whole 30: a share is a voluntary payment, so it's only the payer who can't be in debt.

All of this is public arithmetic the players can do from their own cards. Let them do it.

## Steering

Tips are at most one per player this chapter, public, using only what the table can see (`chapter-3.md`). The ending is the players'. A fair tip, if the decision is plainly being missed: to the Emperor, that a player in debt can't pay a share of a work, so the tax rate decides whether the crown can build this year (N7).

## Tools and gaps

- **A forced payment beyond a player's grain** (Rob's raid on a crown holding 4) becomes a debt. That's N7 working as written, not an engine gap: a player who holds no realia simply goes into debt.
- If a player names no squares for pieces they have to place, ask them in a `--short` follow-up rather than choosing for them.

## This chapter

**Year 14, and on until the game ends,** under the stop rule (finish the year in which you pass 450k). When the last work is built, write the ending as `chapter-6.md` describes:
- the ending act;
- each player's last words;
- `RESULT = export(results_note, epilogue)`;
- the final diaries (`## Year 14`, or the years played).

Leave the `setup()` title, subtitle and blurb alone; the Director writes those at the end.

If a revolt is proposed, tell the Director at once and play it by the digest. Otherwise report at each year's end and at the end. Mark the chapter with `# ===== CHAPTER 8: <title>` before Year 14's marker.
