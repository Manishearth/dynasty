# Scenario: The Dark Ages (second attempt)

For the Director. Read `playthrough-sim/agents/DIRECTOR.md` first. The first attempt, planned under this name, became "Protection Money" (`../protection-money/`, with its `REPORT.md`): nobody called a revolt in twelve years.

**The table:** 6 players, the same cast as the first attempt so the two games compare: Reina Osorio (Emperor, 1), Clark Grafton (Official, 2), Richard Baron (Gentry, 3), Silke Weber (Silk Peasant, 5), Paddy Doyle (Rice Peasant, 6), Robert Land (Warlord, 8). About 14 years, in two-year chapters.

**Working title:** "The Dark Ages", subtitle "Six players · in progress".

**Target arc (Manish, 2026-10-28): the dynasty falls into Chaos and stays there a significant stretch, then recovers to the survival ending, every work built.** Unlike most games, this one is steered towards its arc. **It must reach completion:** if the recovery is failing, consider rewinding a year (Manish).

## Why the first attempt never revolted (the diagnosis)

1. **Revolting was never on anyone's menu.** No prompt or board card said a revolt could be called, and peasants got no prompt between the tax's declaration and its payment.
2. **The revolt was aimed at the lean years, when it gains nothing.** With negative incomes nobody owes tax, so Chaos saves nothing and costs the crown's land subsidies. A revolt pays while incomes are positive and the tax is high. The scripted Dark Ages (`playthrough-sim/game7_dark.py`) shows it: revolt at x1, and "Chaos was a holiday, and that was why it lasted."
3. **A set did a revolt's job.** The hard-taxing Emperor lost the throne to a set in Year 2, and the one natural rebel held a set, which takes the throne where a revolt only brings Chaos. He was then paid to wait.
4. **The Emperor removed every cause.** 30% tax, land paid towards, no debt. The single tip, rules only, came in Year 5, a year with nothing to gain.

## The design

- **Revolt early, at x1, against a high tax.** The deck gives four x1 years (2–5) with positive incomes. Reina, proud and in a hurry to build, taxes hard. Each board card carries the causes for revolt (`REVOLT_LINE = True` in `game.py`), and in Years 2–4 every seat that pays tax gets a short prompt after the declaration: pay, or call or back a revolt. A revolt called before the tax is paid voids that year's tax (game 7's precedent).
- **Chaos as a holiday, Years 3–5:** no tax while the harvests are positive; the rent, the auctions and Rob's raids go on. The acclamation stays split: Rob claims and leads in soldiers, a rich claimant leads in grain, and the peasants sell their friendship dearly.
- **Chaos turns to famine, Years 6–7:** the population doubles in Year 6, and nobody may buy land without an Emperor. Year 7 is a bad harvest at x2. Province 1's sealed treasury drains visibly. Hunger draws the friends together, or a claimant buys soldiers past Rob.
- **Recovery, Years 8–14:** x2 throughout, mostly average harvests. The new Emperor subsidises land and builds a project a year. About 850 is owed if the two palaces go up before the revolt. Years 15+ are x3 (half1 in Year 15) and a bad Year 16; decide at Year 14 whether to play on.

## Rulings this game relies on (Manish, 2026-10-28)

Written up in the shared notes (`dark-ages-chaos-rulings.md`), going into the rulebook through the main session:
- Under Chaos the throne passes only by acclamation: no set, and not the Warlord's objective.
- **The sealed treasury:** nothing voluntary is paid from the reserve. Province 1's harvest, raids, disasters and the Emperor's card effects run through it, and the new Emperor inherits it whatever its sign. The chest card in Year 4 pays out of it.
- The acclamation counts the soldiers a claimant controls; a claimant isn't their own friend.

The engine applies them: `revolt()`, `acclamation()`, the `acclaim` prompt, and the guards on tax, salaries, the treasury and the throne.

## Fallbacks

- **No revolt by the end of Chapter 2:** a second tip, on the reserve or on debt, and rewritten notes.
- **An acclamation that settles at once:** a short Chaos. Record it, and steer the recovery.
- **Chaos that never settles:** the Year 6 tip (land needs an Emperor) should break it, and then an acclamation tip.
- **A recovery that fails:** rewind a year from `state/` and replay it (Manish allows it), logged in `seed.md` and kept in `outtakes/`.
