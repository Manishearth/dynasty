# Handoff after Chapter 7 ("Not Signing for the Ditch": Year 13, played afresh)

For the Chapter 8 Storyteller. Your chapter is **Year 14, and on until the game ends** (or the stop rule ends the chapter at a year's end). The files hold the details: `ledger.md`, `narration.md`, `diaries/`, `log/year13/`, `state/year13.json`. **Don't read `outtakes/`, and never mention it.**

The rules from earlier handoffs that still hold:
- the standing rules (`chapter-0.md`);
- the tip rules (`chapter-3.md`);
- the unsold-lot rule, corrections in place, and launch text sent exactly as printed (`chapter-4.md`);
- hunger, land and revolt (`chapter-5.md`);
- **how the game ends and how to write the ending** (`chapter-6.md`, "How the game ends"): read that section closely.

Read first: `../../playthrough-sim/agents/STORYTELLER.md`, `rules-digest.md` ("Grain running out", "Revolt and Chaos", "Ending and scoring"), `storyteller-voice.md`, then `ledger.md`, `agent-ids.md` and the last few files of `log/year13/`.

## A new ruling: announce it first (Manish, after Year 13)

**The crown may build a negotiated work alone if it pays the whole cost.** A province's agreement governs only its own share: it can refuse to pay, but it can't stop a work the crown pays for in full (§12: "Neither side can force the other" means neither can force the other to *pay*). It's going into `RULINGS.md`.

In Year 13, Graham, the Official, refused the Province 2 Irrigation System even at the crown's whole cost, so that the game wouldn't end. That refusal no longer blocks the build.

- Before anything else in Year 14, announce it as one `act()` line ("A ruling: the crown may build a negotiated work alone if it pays the whole cost; a province can refuse to pay its share, but can't stop the work"). Then file a `note` to all.
- Add it to the ledger's precedents as "Manish, after Year 13". Also record that he confirmed the Chapter 7 Storyteller's rulings: a crown in debt pays only the 5 each that salaries require, not a larger declared sum (anything above 5 is a gift, and a player in debt can't give, N7); and a crown in debt can't pay for a work (N7).

## Where the game stands (end of Year 13)

| Seat | Now | Drew | Grain |
|---|---|---|---|
| 1 Emperor | Reina | Emperor | **−16 (in debt)** |
| 2 Official | Graham | Wheat | 58.5 |
| 3 Gentry | Rich | Gentry | 70 |
| 4 Scholar | **Noah** (since Year 13) | Scholar | 122.5 |
| 5 Silk | Clark | Official | 89.5 |
| 6 Rice | **Silke** | Silk | 64.5 |
| 7 Wheat | Paddy | Rice | 55 |
| 8 Warlord | Rob | Warlord | 198.5 |

- **Works owed: 30, the Province 2 Irrigation System.** Building it ends the game. Under the new ruling the crown can build it alone, **once it's out of debt**.
- **Noah needs only a Bowl.** He's upper class, so with a set he could take the throne. Silke sells Province 6's last Bowl. A player who takes the throne also takes the crown's grain, whatever its sign, debt included.
- **Rob** needs raided pieces from two of Graham, Rich and Silke; the palace wildcard is already used.
- **The crown's debt is a cause for revolt** (§16). Nobody proposed one in Year 13.
- **The deck:**
  - Year 14 draws `double3`: a good harvest, and **the population doubles to ×6**, its cap.
  - Year 15 draws `double1`, past its cap, so it's only a good harvest.

  The engine applies both. Don't hint at either.

## Year 14's arithmetic (from the engine; for you, not to state as a forecast)

A good harvest at ×6, with works bonuses and new land:

| Seat | Player | Income |
|---|---|---|
| 1 | Reina | −120 |
| 2 | Graham | +160 |
| 3 | Rich | −60 |
| 4 | Noah | −20 |
| 5 | Clark | +240 |
| 6 | Silke | +60 |
| 7 | Paddy | −40 |
| 8 | Rob | −80 |

- **Taxable income totals 460** (Graham, Clark, Silke). The crown is at about −136 after the harvest, and the tax pays its debt first. So a rate of about 36% or more gets the crown out of debt and leaves the 30 to build the ditch, ending the game in the works step that same year.
- Lower, and the crown stays in debt; then only a seat change or someone else paying the whole 30 can end it.
- Nobody may pay for a work from debt (N7). A province can pay the whole 30 if it wants: a share is voluntary, so only the payer has to be out of debt.

The players can do this arithmetic themselves from their cards. Let them.

## Steering

Tips: at most one per player, public (`chapter-3.md`). A fair one, if the Emperor is plainly missing it: under the new ruling, the crown can build the last work itself once it's out of debt, and the tax pays the debt first (N7).

## Tools

- **Launches carry the land note now:** `launch:free` (or any `launch:<kind>`) carries the new-land reminder; plain `launch` with `--menu` doesn't, so prefer `launch:free --menu`.
- **The endgame note** ("the game can end this year") is about the works left, not anyone's intent, so it stays true after an Emperor declines to build.
- **After a mid-auction seat change,** check each `place` prompt names the right seller (the seat's current player), and fix the prompt file before sending if not.

## This chapter

**Year 14, and on until the game ends,** under the stop rule (finish the year in which you pass 450k).

When the last work is built, write the ending as `chapter-6.md` describes:
- the ending act;
- each player's last words;
- `RESULT = export(results_note, epilogue)`;
- the final diaries (`## Year 14`, or the years played).

Leave the `setup()` title, subtitle and blurb alone. If a revolt is proposed, tell the Director at once. Report at each year's end and at the end. Mark the chapter with `# ===== CHAPTER 8: <title>` before Year 14's marker.
