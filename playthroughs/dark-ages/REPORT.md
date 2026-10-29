# The Dark Ages: report

The second attempt at the Dark Ages; the first became `../protection-money/`. An agent-played game of Dynasty with six players: the Emperor, the Official, the Gentry, the Silk and Rice Peasants, and the Warlord. Provinces 4 and 7 were empty. Each seat was a tool-less `dynasty-player` agent in character, each cast member in the province their name puns on. A Storyteller session per chapter refereed through the engine, and a Director session steered. **Unlike any game before it, this one was steered openly towards a chosen arc (Manish's brief): a revolt, a long Chaos, then recovery to survival.** The deck was shuffled with seed `5130` (`seed.md`).

**It ended in Year 14 in survival.** The table revolted in Year 2 and spent four years in Chaos, with the acclamation split three ways. In Year 6, the year the population doubled, it acclaimed Clark, who then built a work every year until the Marble Pagoda, the last, went up in Year 14. It is the first agent game to play a standing revolt, a long Chaos and a contested acclamation.

**The record:**
- `game.py`, ending `RESULT = export(...)`; run it with `run.py`.
- `log/year1–14/`: every prompt and reply.
- `ledger.md`, `diaries/`, `narration.md`, `state/`, `handoff/`.
- `direction.md`: the actor's brief, in its last version (earlier versions are described in `seed.md`).
- **The outtakes** are in `outtakes/`, so the history of the steering survives:
  - `attempt-1/`: Years 1–6 of the first run.
  - `year1-rewind/`: a Year 1 revolt, taken back.
  - `year2-rewind/` and `year5-rewind/`: Years 2–5 of the restart.

## Verdicts

| Player | Drew | Ended | Grain | Verdict |
|---|---|---|---|---|
| Clark | Official | Emperor | 1,365.5 | won |
| Silke | Silk Peasant | Silk Peasant | 2,991.5 | held |
| Paddy | Rice Peasant | Rice Peasant | 2,170.5 | held |
| Rich | Gentry | Gentry | 530 | held |
| Rob | Warlord | Warlord | 61.5 | held |
| Reina | Emperor | Official | 354 | lost |

**One seat change:** the Year 6 acclamation, Clark to the throne and Reina to his seat as Official.

## The story in brief

- **Chapter 1, "Heaven's Own Share" (Setup–Year 2).**
  - Reina taxed 50% and built the Summer Palace. Clark won a complete set in Year 1 and held it.
  - In Year 2 Reina taxed 50% again. Silke and Rob called "taxes are consistently excessive", and Clark, Rich and Paddy all backed it.
  - Reina's answer was proud, with no cut, and nobody took the revolt back. **Chaos began**, and the reserve was sealed at 195.
  - The first acclamation split: Clark led in friends (Silke), Rich in grain, Rob in soldiers.
- **Chapter 2, "Swords Eat" (Years 3–4).** Chaos as a holiday: no tax, no works. Rob took both Land Deeds, breaking Clark's and Paddy's sets. The sealed treasury grew to 236 on Province 1's own harvests. Clark put his canals into the record.
- **Chapter 3, "A Figure, Not a Speech" (Years 5–6).**
  - Paddy set a public deadline: a real figure for a Province 6 canal.
  - In Year 6, straight after the doubling card, Paddy moved to Clark. Then Reina, Silke, Rich and Rob all backed him, and **Clark was acclaimed**, with the treasury (251) for his reserve.
  - He taxed 30%, built the Winter Palace and paid all of each province's first two squares of land.
  - Rich won the Jar that would have let him take the throne straight back, and held it.
- **Chapter 4, "Fat Year or Thin" (Years 7–8).** The canals in Provinces 6 and 5, each dug whole. The reserve fell to 0.5, then refilled from the new land. Clark moved the Wall back a year, in public.
- **Chapter 5, "Counted Into the Mortar" (Years 9–10).** Ten Wall links in Year 9 (crown 340, Rich 40, Reina 20) at a 50% tax, and the last two in Year 10. The Great Wall stood whole.
- **Chapter 6, "The Ink Holds" (Years 11–12).** The Province 3 Reservoir (crown 60, Rich 20), then the Province 1 canal from the crown alone, at a tax cut to 20%.
- **Chapter 7, "The Last Line of the Book" (Years 13–14).** The Province 2 Irrigation, then the Pagoda alone. Survival.

## The steering, and what it shows

All in `seed.md`'s steering log. The short version: **notes and tips couldn't produce a revolt against rational agents. An actor's brief could.**

1. **Attempt 1 (Years 1–6, now an outtake).**
   - **The steering:** seed 5130; actor's notes pushing a hard Emperor and a revolt coalition; a revolt line on every board card; a pay-or-revolt prompt after each tax declaration; and five tips.
   - **No revolt in six years.** Cheap sets moved the throne twice, in Years 3 and 4. Each new Emperor cut the tax to 20% and closed every cause, and Clark's aside said so outright.
   - **One tip backfired:** a public note that Chaos disarms a set was acted on first by the set-holder, who took the throne before any revolt.
2. **The restart from the setup.**
   - **The new notes:** Reina taxed very hard, Rob was wantonly destructive (Manish's idea), and the factions were Clark and Silke against Rich and Paddy.
   - **Year 1:** a revolt was called at once, and Manish had it rewound so that it would come in Year 2.
   - **Years 2, 3, 4 and 5:** a revolt was called every year and dropped every year. In Years 2, 4 and 5 Rich took his agreement back for a price: "agreeing is not deposing", the second time for his 40 for the Reservoir.
3. **The rewind to the end of Year 1, with an actor's brief** (`direction.md`, Manish's idea).
   - **What it is:** the cast are actors and know the story's shape. It's carried in every launch prompt and forbidden at the table.
   - **Year 2:** the revolt stood at once, with all five backing it.
   - **Rewritten between chapters:** first "Chaos holds", then "the table moves when Chaos costs more than it saves, in the year of the doubling", then "the recovery", then "the last works".
   - **The players chose every move.** Not one reply leaked the brief in fourteen years.
4. **Mid-chapter steering:** two notes sent with `note --to`.
   - **Reina, Year 4 (attempt 2):** her monuments before the provinces' canals. It leaked as "the Director in my head" in her diary, so DIRECTOR.md now frames such notes as "a note on playing your character".
   - **Rich, Year 6:** a set is leverage, not a ladder, sent before the auction that could have unseated Clark.

## What the rules did

- **A held set beats a revolt.** A set-holder loses their road to the throne under Chaos, so no upper-class set-holder backed a revolt until the brief told them the story.
- **The Emperor's answer can be a bribe.** Under the calling-off ruling, "pay ... or promise anything", the Emperor can pay one backer personally. Rich sold his agreement back three times.
- **Chaos at x1 is a holiday.** No tax, and every harvest positive. The sealed treasury even grew, from 195 to 251, on Province 1's own harvests.
- **The doubling ends Chaos.** No land can be bought without an Emperor, and that was the lever: the acclamation came in the year of the doubling, with every player backing one claimant.
- **The acclamation's three counts** split exactly as designed while the claims were rival: grain to Rich, soldiers to Rob, friends to Clark. A single claimant with five friends leads every count.
- **The sealed treasury worked:** nobody spent it, Province 1's harvests, raids, disasters and the chest card ran through it, and Clark inherited it whole.
- **A called revolt stopping play** (Manish's ruling) kept the set-holders from jumping onto the throne mid-revolt. It mattered in Year 2.
- **Land paid for everything.** 126 squares were bought (Province 5 54, Province 6 39, Province 1 14, Province 2 11, Province 3 8). By the end the peasants paid almost all the tax, and the crown could cut it to 20% and still build every year.
- **One project a year is the clock.** 850 was owed at the acclamation. The game finished in Year 14 only because the Wall went up as ten links in one project.
- **The Harvest Pile ended at −4,973,** paying in full below zero, as ruled.

## Rulings made for this game (now in the rulebook, through the main session)

Written up for the main session in the shared notes (`dark-ages-chaos-rulings.md`), for `RULINGS.md` and the rulebook:
- (a) Under Chaos the throne passes only by acclamation; no set, and not the Warlord's objective.
- (b) The sealed treasury.
- (d) The acclamation counts the soldiers a claimant controls, and nobody is their own friend.
- (e) A called revolt stops play until it stands or is dropped.
- (f) Storytellers correct rules misreadings in players' stated reasoning, and the Director may steer mid-chapter.

## Rulings to look at

- **Answered by Manish, no ruling needed:**
  - *Should the Emperor's answer to a revolt have to address its cause, rather than pay off one backer?* No. A backer may sell their agreement back.
  - *Should a revolt give its backers something even when they don't win the acclamation?* No.
- **(Y6, Storyteller 8) Chaos ends mid-round:** the acclaimed Emperor taxed, built and bought land in the same round. Game 7's precedent, played here for real.

## Tool gaps found

**Fixed during the game** (shared tools, with Manish's OK; other games' prompts checked byte-for-byte):
- **Engine:** `revolt_called()`, `revolt_dropped()`, `revolt()`, `acclaim_counts()` and `acclamation()`.
- **Engine guards under Chaos:** on tax, salaries and spending from the treasury, on a seat change onto the throne, and on every step while a revolt is pending.
- **`briefs.py` board card:** the Chaos line, the deposed Emperor's line and the waiting line. `may_replace` drops the throne under Chaos, and the crown and collect menus refuse under Chaos.
- **`briefs.py` prompts:** the `acclaim` prompt kind, the `REVOLT_LINE` flag, and `direction.md` support in launches.
- **Docs:** `STORYTELLER.md` (the revolt procedure, and "Rules misreadings") and `DIRECTOR.md` (mid-chapter steering, notes that never name the Director).

**Still open:**
- **The Warlord's tribute** can be placed on another province's bought land on the desert (`briefs.py`'s march list and the engine's `_place`). It was worked round by hand.
- **The land lists** offered squares already taken (Paddy's T23, T24, U21).
- **The march menu** once offered a diagonal step onto a guarded piece.
- **The crown prompt** doesn't carry Province 1's own land list.
- **`warlord_got`** keeps one raid per province, so a later take overwrites an earlier one on the card. It's harmless, since the objective counts provinces.
- **The harness:** Bash drops non-ASCII text and `$VAR`s. Every Storyteller wrote files with Write, Edit or small scripts.

## For the page

- **Title, subtitle and description:** in `game.py`'s `setup()`.
- **The outtakes** in `outtakes/` aren't part of the live game and shouldn't be on the page.
- **Reina's Years 3–4 diary in `outtakes/year2-rewind/`** contains the "Director in my head" leak. It isn't in the live diaries.
- **`build_real.py` wasn't touched.** The main session adds the game and rebuilds.
