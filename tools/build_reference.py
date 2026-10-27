#!/usr/bin/env python3
"""Generate reference-cards.html: two-sided, half-letter reference cards.

One general card (turn order, realia, money, the Harvest Pile, public works),
one "Running the round" card (a script for whoever runs the round) and one card per province (income table, duties, objective, what you are owed,
new land, personal disasters). Numbers follow rulebook.html.

Run from the repo root:  python3 tools/build_reference.py
Pure Python, no dependencies. Piece glyphs are added by tools/add_glyphs.py.
"""
import html
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "reference-cards.html")
sys.path.insert(0, HERE)
import add_glyphs  # noqa: E402
from glyphs import GLYPHS  # noqa: E402

E = html.escape

# --------------------------------------------------------------------------
# Shared data
# --------------------------------------------------------------------------

REALIA = {2: "Customs House", 3: "Land Deed Scroll", 4: "Bamboo Brush",
          5: "Dragon Jar", 6: "Wooden Bowl", 7: "Vase"}
PLURAL = {2: "Customs Houses", 3: "Land Deed Scrolls", 4: "Bamboo Brushes",
          5: "Dragon Jars", 6: "Wooden Bowls", 7: "Vases"}
ROLE = {1: "Emperor", 2: "Official", 3: "Gentry / Landholder", 4: "Scholar",
        5: "Silk Peasant", 6: "Rice Peasant", 7: "Wheat Peasant", 8: "Warlord"}
# The emblem in a province card's header: the realia it sells, or the Emperor's Winter Palace.
MARK = {1: "winter-palace", 2: "customs-house", 3: "land-deed-scroll", 4: "bamboo-brush",
        5: "dragon-jar", 6: "wooden-bowl", 7: "vase", 8: "soldier"}
CLASS = {1: "imperial", 2: "upper", 3: "upper", 4: "upper",
         5: "lower", 6: "lower", 7: "lower", 8: "outside"}

ROWS = ["×1", "×1½", "×2", "×3", "×4", "×6"]
MULT = [1, 1.5, 2, 3, 4, 6]


def income_table(base, harvest):
    """Rows of (pop, consumption, good, avg, bad)."""
    out = []
    for label, m in zip(ROWS, MULT):
        c = int(base * m)
        out.append((label, c) + tuple(h - c for h in harvest))
    return out


def signed(n):
    return f"+{n}" if n > 0 else ("0" if n == 0 else f"−{-n}")


TURN = [
    ("Scholar", "I Ching",
     "Turn the top card and read it aloud. Apply any population change and any Personal Disasters it calls for."),
    ("Gentry", "Harvest",
     "Pay every player the harvest the card names, from the Harvest Pile, plus what their Public Works and new harvest squares add."),
    ("Peasants", "Rent",
     "Each Peasant pays the Gentry at least 5 — only if the Gentry asks."),
    ("Emperor", "Tax declared",
     "One percentage for everyone, 10% to 90%."),
    ("Official", "Tax paid",
     "Everyone but the Emperor pays that share of this year's harvest income to the Official, who hands it to the Emperor. No tax on a loss."),
    ("Emperor", "Public Works",
     "Build one project. Cost-shares and new harvest squares are negotiated and bought now."),
    ("All, from Province 1 up", "Auction",
     "Each player auctions one piece of their realia. The Warlord raids instead."),
    ("Provinces", "Soldiers",
     "After the Warlord has moved, your soldiers may move one square."),
    ("Emperor", "Salaries",
     "Pay the Official and the Scholar at least 5 each."),
]

MONEY = [
    ("Harvest", "Good 100 · average 75 · bad 50. Warlord 40 · 30 · 20."),
    ("Tax", "10–90% of harvest income only. None on a loss or from the Emperor."),
    ("Rent", "5 or more from each Peasant to the Gentry, if demanded."),
    ("Salaries", "5 or more each to the Official and the Scholar."),
    ("Auction", "Minimum bid 2 (the seller may set it higher). Seller keeps 25%; 75% goes to the Pile. The Emperor never bids."),
    ("Sell back", "Any realia to the Pile for 2."),
    ("Raid", "5 per new square, 10 in Province 1. Realia: 5, the piece, or its cost. Palace or pagoda: its full cost. Other works: an ordinary raid."),
    ("Soldiers", "20 each from the Warlord, who keeps 25%; the rest to the Pile."),
    ("Crossing water", "The Warlord pays 5 per soldier that crosses a river or a public work, to that province."),
    ("New harvest square", "Only once your population has doubled (×2). 20 from the Pile; yields +20 every round after. Share cost and yield with the Emperor."),
    ("Changing seats", "Complete your set and hold 20. The player you replace draws 60 from the Pile."),
]

PILE_OUT = ["Every player's harvest", "New harvest squares, when bought",
            "60 to a player who is replaced"]
PILE_IN = ["Fines and personal disasters", "75% of every auction price",
           "75% of every soldier sold", "Realia sold back, at 2 each"]

WORKS = [
    ("Summer Palace", "1", "20", "—", "First, before the Wall and the canal in 1"),
    ("Winter Palace", "1", "20", "—", "First, before the canal in 4, 5, 6"),
    ("Marble Pagoda", "1", "20", "—", "In any round nothing else is built"),
    ("Great Wall", "4 links over each of 1, 2, 3", "40 each", "—", "4 links open the land below"),
    ("Grand Canal", "2 sections in each of 1, 4, 5, 6", "40 each", "+10 each", "Emperor pays in 5, 6"),
    ("Irrigation System", "2", "30", "+10", "Shared"),
    ("Reservoir", "3", "80", "+20", "Shared"),
    ("Reservoir", "7", "60", "+20", "Emperor pays"),
]

# The "Running the round" card: (step, who, what to say, what to check).
SCRIPT = [
    ("I Ching", "Scholar",
     "Scholar, turn the top card and read it to us.",
     "The population counter moved, if it changed. Everyone knows their harvest. Any Personal Disasters and levies are paid to the Pile."),
    ("Harvest", "Gentry",
     "Gentry, pay out the harvest.",
     "Everyone has their grain: harvest, + Public Works bonuses, + 20 per new harvest square, − what their people eat. Anyone short sells realia back at 2, then goes into debt."),
    ("Rent", "Peasants",
     "Gentry, are you asking for rent?",
     "Each Peasant asked has paid at least 5. Not asked, not owed."),
    ("Tax declared", "Emperor",
     "Emperor, what is the tax this year?",
     "One rate for everyone, 10% to 90%."),
    ("Tax paid", "Official",
     "Pay the Official your share of this year’s harvest income.",
     "Harvest income only: no rent, salaries, commissions or tolls. Rounded down to the half million. A loss pays nothing; the Emperor pays none; the Warlord may refuse. The Official then hands all of it to the Emperor."),
    ("Public Works", "Emperor",
     "Emperor, what are you building?",
     "One project: any number of sections of one work. Palaces before what needs them; nothing else built means the Marble Pagoda. Cost shares paid; new harvest squares bought from the Pile."),
    ("Auction", "Provinces 2 to 7, in order",
     "Province 2, what are you selling?",
     "One piece each; minimum bid 2. The Emperor never bids. Seller keeps ¼, rounded down to the half million; the rest to the Pile. The buyer places it at once. Then the Pile auctions anything sold back to it. The Warlord raids instead."),
    ("Soldiers", "Provinces",
     "Anyone moving soldiers?",
     "Only after the Warlord’s have moved; one square each. A bought soldier stays put until its province has been raided."),
    ("Salaries", "Emperor",
     "Emperor, pay the Official and the Scholar.",
     "At least 5 each."),
]

ROUND_ONE = [
    "No I Ching card and no harvest: start at step 3, rent.",
    "The 60 everyone starts with counts as the year’s harvest income, so it is what tax is charged on.",
    "Everything from rent onward runs as normal, the auction and the Warlord’s first raids included.",
]
CHAOS = [
    "<b>Stopped:</b> no tax, no salaries, no Public Works, and so no new harvest squares (no Emperor to share the cost).",
    "<b>Still on:</b> harvests are paid, and the Warlord still rides. The fallen Emperor keeps Province 1 for now.",
    "It ends when the table accepts a new Emperor (the most grain, friends or soldiers, or a mix), even mid-round: the new Emperor then declares tax, builds and pays salaries that round.",
]
END_CHECKS = [
    "The population counter shows the current figure.",
    "Works built this round add to harvests from <b>next</b> round.",
    "Who is in debt? Until it’s paid they can’t bid, trade realia, give grain, share costs, buy soldiers or change seats, and everything they receive pays it first.",
    "Realia sold back to the Pile goes up at the next auction. Realia returned on a seat change goes home, to be sold again.",
    "Is every public work owed now built? Then the game is over: the reign was glorious.",
]
ANYTIME = [
    "Trade, bribe, threaten and make deals. No deal is binding.",
    "Buy soldiers from the Warlord: 20 each.",
    "Sell realia back to the Pile for 2.",
    "Keep your grain secret, or be cagey about it.",
    "Revolt, if two other players agree the Emperor has failed.",
]

# --------------------------------------------------------------------------
# Per-province data
# --------------------------------------------------------------------------

STUCK = {2: 5, 3: 6, 4: 7, 5: 2, 6: 4, 7: 3}   # the realia you start with and never need
NEED45 = {2: [7, 6, 3, 4], 3: [7, 5, 2, 4], 4: [6, 5, 2, 3],
          5: [3, 4, 7, 6], 6: [2, 3, 7, 5], 7: [2, 4, 5, 6]}

REPLACE = {
    1: "You cannot climb; you can only fall. The Official, Gentry, Scholar or Warlord takes the throne by completing their objective. You then take their seat and draw 60 from the Pile.",
    2: "The Emperor or any other player.",
    3: "The Emperor or any other player.",
    4: "The Emperor or any other player.",
    5: "The Gentry, Scholar, Official or another Peasant. Never the throne directly.",
    6: "The Official, Scholar or another Peasant. Never the throne directly.",
    7: "The Gentry, Scholar, Official or another Peasant. Never the throne directly.",
    8: "Any player, including the Emperor.",
}

DUTIES = {
    1: ["Declare the tax: one rate, 10–90%, for everyone.",
        "Build one Public Works project. In a round you build nothing else, build the Marble Pagoda.",
        "At the end of the round, pay the Official and the Scholar at least 5 each.",
        "Settle disputes. Negotiate with the upper class first.",
        "Never bid at an auction."],
    2: ["Collect the tax from everyone and hand it to the Emperor. Watch for cheats.",
        "Pay your own tax.",
        "Auction one Customs House.",
        "Receive at least 5 salary at the end of the round."],
    3: ["Run the Harvest Pile: pay out every harvest and handle every payment in and out.",
        "Demand rent of at least 5 from each Peasant. If you forget, you don't get it.",
        "Pay your tax. Auction one Land Deed Scroll."],
    4: ["From Round Two, turn the I Ching card and read it aloud.",
        "Keep the population count and announce every change.",
        "Pay your tax. Auction one Bamboo Brush.",
        "Receive at least 5 salary at the end of the round."],
    5: ["Pay the Gentry at least 5 rent, if asked.",
        "Pay your tax. Auction one Dragon Jar."],
    6: ["Pay the Gentry at least 5 rent, if asked.",
        "Pay your tax. Auction one Wooden Bowl."],
    7: ["Pay the Gentry at least 5 rent, if asked.",
        "Pay your tax. Auction one Vase."],
    8: ["Move every soldier one square, any direction.",
        "Raid one unraided square per soldier: 5, or 10 in Province 1.",
        "Raiding realia: demand 5, the piece itself, or its cost.",
        "Raiding the Summer Palace, Winter Palace or Marble Pagoda: the Emperor pays you its full cost (20). The building stays.",
        "Any other square, canal and reservoir squares included, is an ordinary raid, and the work is undamaged.",
        "Sell soldiers to anyone who asks: 20 each, you keep 25%.",
        "Pay 5 per soldier that crosses a river or a public work, the Great Wall included. The Wall stands outside the provinces, so it can't be raided.",
        "Pay your tax, or refuse: only soldiers or politics can make you. You hold no realia and never auction."],
}

OWED = {
    # The Emperor's rows carry a fifth column: what must stand first.
    1: [("Summer Palace", "20", "You", "—", "—"), ("Winter Palace", "20", "You", "—", "—"),
        ("Marble Pagoda", "20", "You", "—", "An idle round"),
        ("Great Wall ×12", "40 each", "Share with 2 and 3", "—", "Summer Palace"),
        ("Grand Canal ×2 in 1", "40 each", "You", "+10 each", "Summer Palace"),
        ("Grand Canal ×2 in 4", "40 each", "Share with 4", "+10 each", "Winter Palace"),
        ("Grand Canal ×2 in 5, 6", "40 each", "You", "+10 each", "Winter Palace"),
        ("Irrigation System in 2", "30", "Share with 2", "+10", "—"),
        ("Reservoir in 3", "80", "Share with 3", "+20", "—"),
        ("Reservoir in 7", "60", "You", "+20", "—")],
    2: [("Irrigation System", "30", "Share with the Emperor", "+10"),
        ("Great Wall, 4 links above you", "40 each", "Share with the Emperor", "—")],
    3: [("Reservoir", "80", "Share with the Emperor", "+20"),
        ("Great Wall, 4 links above you", "40 each", "Share with the Emperor", "—")],
    4: [("Grand Canal, 2 sections", "40 each", "Share with the Emperor", "+10 each")],
    5: [("Grand Canal, 2 sections", "40 each", "The Emperor", "+10 each")],
    6: [("Grand Canal, 2 sections", "40 each", "The Emperor", "+10 each")],
    7: [("Reservoir", "60", "The Emperor", "+20")],
    8: [],
}
OWED_NOTE = {
    1: "Build only where there is a player. The game ends, gloriously, when everything owed is built.",
    2: "Both must be built before the game can end.",
    3: "Both must be built before the game can end.",
    4: "The Winter Palace must stand first.",
    5: "The Winter Palace must stand first.",
    6: "The Winter Palace must stand first.",
    7: "Your only public work, and the crown pays for all of it.",
    8: "Nothing is owed to you. Everything you have, you take.",
}

NEWLAND = {
    1: "That is 28 million people. Build on the sea, or on the strip below the Wall once your four Wall links stand.",
    2: "That is 24 million people, and all four Wall links above you must stand. Build on the strip below the Wall.",
    3: "That is 24 million people, and all four Wall links above you must stand. Build on the strip below the Wall.",
    4: "That is 24 million people. Build on the sea.",
    5: "That is 28 million people. Build on the sea.",
    6: "That is 28 million people. Build on the sea or on the Warlord's land.",
    7: "That is 28 million people. Build on the Warlord's land next to you.",
    8: None,
}

DISASTERS = {
    1: [("Thrown by a gift horse", "4"), ("The Prince breaks an ivory treasure", "10"),
        ("The burning of the books", "30")],
    2: [("Your chariot crashes; pension for the driver", "4"),
        ("The imperial barge rams a lock gate", "10"),
        ("A nephew gambles away the tax", "half your income this round")],
    3: [("A pension for the retiring chef", "5"), ("Replacing art stolen in a raid", "10"),
        ("Bandits empty your granary", "half your grain")],
    4: [("Your research notes burn", "4"), ("Baffling translations anger the Emperor", "10"),
        ("An error in the new calendar", "a third of your grain")],
    5: [("A shrine to the warrior who saved you", "4"), ("A flash flood takes the ditch", "10"),
        ("Your son steals a chicken", "half this round's harvest")],
    6: [("Your water buffalo breaks a leg", "4"), ("Fire takes your house and grain", "10"),
        ("You inherit a debt", "half this year's income")],
    7: [("A feast for your daughter's honour", "2"), ("Your blacksmith shop burns", "5"),
        ("Two treasures break on the road", "a third of this year's income")],
    8: [("Wounded in the legs", "no raids on 5, 6, 7 this round"),
        ("Your daughter elopes with a rival", "5, and no raids this year"),
        ("Robbed by your own men", "half your grain")],
}

STATS = {1: ("14M", 60, (100, 75, 50)), 2: ("12M", 40, (100, 75, 50)),
         3: ("12M", 40, (100, 75, 50)), 4: ("12M", 40, (100, 75, 50)),
         5: ("14M", 40, (100, 75, 50)), 6: ("14M", 40, (100, 75, 50)),
         7: ("14M", 40, (100, 75, 50)), 8: ("8M", 20, (40, 30, 20))}

CHARACTER = {
    1: "The Son of Heaven: forceful, thoughtful, just. You care for the masses, not for petty misfortunes, and your word is law.",
    2: "Harsh and practical. You serve the Emperor to the letter, take every bribe worth taking, and want the throne.",
    3: "Greedy, and kind to anyone above you. You want more land and more people under you; the Peasants are your children and your income.",
    4: "A dreamer and an honest one. You would rule to bring peace and learning to the land, and you always keep your word.",
    5: "Simple and hard-working, tied to your mulberry trees and silkworms. You revolt only when the choice is starvation.",
    6: "Simple, honest and used to Nature's cruelties. You pray for survival and revolt only when the choice is starvation.",
    7: "Patient beyond measure. You will do almost anything to survive, but revolt only when the choice is starvation.",
    8: "Cruel and vicious. You lie, cheat and above all steal, and you mean to buy enough soldiers to take the throne.",
}

EXTRA = {
    1: ("Beware the Warlord", "Every raid on your province costs you 10, not 5. A raid on the Summer Palace, Winter Palace or Marble Pagoda costs its full price, and the building stays."),
    8: ("Your army", "2 soldiers at 5–6 players, 4 at 8 or more, starting anywhere on undeveloped land. A raided square can never be raided again, but you may stand on it. Soldiers capture by moving onto a soldier orthogonally, never diagonally. Bought soldiers stay frozen in their province until you raid it."),
}

# --------------------------------------------------------------------------
# HTML pieces
# --------------------------------------------------------------------------


def table(head, rows, cls=""):
    h = "".join(f"<th>{c}</th>" for c in head)
    b = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<table class="{cls}"><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table>'


def head(title, sub, kind, p=None):
    """A province card shows its emblem in the header's corner."""
    corner = ""
    if p in MARK:
        corner = (f'<svg class="mark" viewBox="0 0 10 10" aria-hidden="true">'
                  f'<path d="{GLYPHS[MARK[p]][2]}" fill-rule="evenodd" fill="currentColor"/></svg>')
    return f'<header class="ch {kind}"><div><h2>{title}</h2><p>{sub}</p></div>{corner}</header>'


def foot():
    return '<footer class="cf">Dynasty (1969) · unofficial reference card · CC BY-SA 4.0</footer>'


def general_front():
    steps = "".join(
        f'<li><span class="n">{i}</span><div><b>{E(what)}</b><span class="who">{E(who)}</span>'
        f'<p>{E(desc)}</p></div></li>' for i, (who, what, desc) in enumerate(TURN, 1))
    realia = table(["Realia", "Sold by", "Realia", "Sold by"],
                   [(REALIA[a], f"{a} · {ROLE[a].split(' /')[0]}", REALIA[b], f"{b} · {ROLE[b]}")
                    for a, b in ((2, 5), (3, 6), (4, 7))], "realia")
    return (head("The round", "Everyone · one round is one year", "general") +
            '<section><h3>Turn order</h3>'
            '<p class="small">Round One has no I Ching and no harvest, so it starts at step 3, rent. '
            'Its taxable income is the 60 everyone starts with.</p>'
            f'<ol class="turn">{steps}</ol>'
            '<p class="anytime"><b>At any time:</b> trade, bribe, threaten, make deals; no deal is binding. '
            'You may keep your grain secret. '
            'Revolt needs two other players to agree the Emperor has failed.</p></section>'
            f'<section><h3>Realia</h3>{realia}</section>' + foot())


def general_back():
    money = "".join(f"<dt>{E(k)}</dt><dd>{E(v)}</dd>" for k, v in MONEY)
    pile = table(["Out of the Pile", "Into the Pile"],
                 [(PILE_OUT[i] if i < len(PILE_OUT) else "", PILE_IN[i]) for i in range(len(PILE_IN))],
                 "pile")
    works = table(["Work", "Province", "Cost", "Adds / yr", "Note"],
                  [(E(w), E(p), c, a, E(n)) for w, p, c, a, n in WORKS], "works")
    return (head("Money and building", "Everyone · all figures in millions of bags of grain", "general") +
            f'<section><h3>Money at a glance</h3><dl class="money">{money}</dl></section>'
            f'<section><h3>The Harvest Pile</h3>{pile}'
            '<p class="small">The Gentry runs the Pile. Taxes are not the Pile: they go to the Emperor\'s own reserve.</p></section>'
            f'<section><h3>Public Works</h3>{works}'
            '<p class="small">The Emperor builds one project a round; any number of sections of one work counts as one project.</p></section>'
            + foot())


def running_front():
    steps = "".join(
        f'<li><span class="n">{i}</span><div><b>{E(what)}</b><span class="who">{E(who)}</span>'
        f'<p class="say">“{E(say)}”</p><p class="check">{E(check)}</p></div></li>'
        for i, (what, who, say, check) in enumerate(SCRIPT, 1))
    return (head("Running the round", "Read each line aloud, then check before moving on", "general") +
            f'<ol class="turn script">{steps}</ol>' + foot())


def running_back():
    def ul(items, cls=""):
        return f'<ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    return (head("Running the round", "Round One, Chaos and the end of a round", "general") +
            f'<section><h3>Round One</h3>{ul(ROUND_ONE, "duties")}</section>'
            f'<section><h3>During Chaos</h3>{ul(CHAOS, "duties")}</section>'
            f'<section><h3>Before the next round</h3>{ul(END_CHECKS, "checks")}</section>'
            f'<section class="anytime"><b>Any time, any step</b>{ul(ANYTIME, "duties")}</section>'
            + foot())


def objective(p):
    if p == 1:
        return "<p>Stay in power. Build every public work you owe and your reign ends in glory.</p>"
    if p == 8:
        return "<p>Raid a different piece of realia from each player. Then take any seat, the throne included.</p>"
    four = ", ".join(REALIA[r] for r in NEED45[p])
    extra = REALIA[STUCK[p]]
    return table(["Players", "Collect, plus 20 in grain"],
                 [("4–5", four), ("6", "One piece from each other player who holds realia"),
                  ("7+", f"{four}, and a {extra}")], "obj")


def start_stock(p):
    if p in (1, 8):
        return ""
    return (f'<p class="small"><b>You sell {PLURAL[p]}.</b> You start with one {REALIA[p]} and two '
            f'{PLURAL[STUCK[p]]} at 4–5 players (you never need those), two {PLURAL[p]} at 6, four at 7+.</p>')


def player_front(p):
    pop, eats, h = STATS[p]
    sub = f"Province {p} · population {pop} · eats {eats} · harvest {h[0]}/{h[1]}/{h[2]}"
    duties = "".join(f"<li>{E(d)}</li>" for d in DUTIES[p])
    return (head(f"{p} · {E(ROLE[p])}", sub, CLASS[p], p) +
            f'<p class="char">{E(CHARACTER[p])}</p>'
            f'<section><h3>Each round</h3><ul class="duties">{duties}</ul></section>'
            f'<section><h3>Your objective</h3>{objective(p)}{start_stock(p)}</section>'
            f'<section><h3>Who you may replace</h3><p>{E(REPLACE[p])}</p></section>'
            + (f'<section><h3>{E(EXTRA[p][0])}</h3><p>{E(EXTRA[p][1])}</p></section>' if p in EXTRA else "")
            + disasters(p) + foot())


def disasters(p):
    dis = "".join(f"<li><span>{E(t)}</span><b>{E(c)}</b></li>" for t, c in DISASTERS[p])
    return (f'<section><h3>Personal disasters</h3><ol class="dis">{dis}</ol>'
            '<p class="small">Paid to the Harvest Pile. When I Ching calls for one, play the next in order; '
            'after the third, start again.</p></section>')


def player_back(p):
    pop, eats, h = STATS[p]
    rows = [(a, b, signed(c), signed(d), signed(e)) for a, b, c, d, e in income_table(eats, h)]
    inc = table(["Population", "Eats", "Good", "Average", "Bad"], rows, "income").replace(
        "<thead><tr>", '<thead><tr><th class="blank"></th><th class="blank"></th>'
                       '<th class="grp" colspan="3">Base income</th></tr><tr>', 1)
    owed = ""
    if p == 1:
        owed = table(["Work", "Cost", "Who pays", "Adds / yr", "Requires"],
                     [(E(a), b, E(c), d, E(r)) for a, b, c, d, r in OWED[p]], "owed")
    elif OWED[p]:
        owed = table(["Work", "Cost", "Who pays", "Adds / yr"], [(E(a), b, E(c), d) for a, b, c, d in OWED[p]], "owed")
    owed += f'<p class="small">{E(OWED_NOTE[p])}</p>'
    nl = ""
    if NEWLAND[p]:
        nl = (f'<section><h3>New harvest squares</h3><p><b>Only available once your population has doubled (×2).</b> {E(NEWLAND[p])} '
              '20 each from the Pile, +20 every round after. Share cost and yield with the Emperor.</p></section>')
    return (head(f"{p} · {E(ROLE[p])}", "Income, works and new land", CLASS[p], p) +
            f'<section><h3>Your income each year</h3>{inc}'
            '<p class="small">Income = base (harvest − what your people eat) + what your works add'
            + ('' if p == 8 else ' + 20 per new harvest square you own') + '. '
            + ('' if p == 1 else 'This is what you pay tax on. ')
            + 'Population ×1 is 100M nationally; ×6 is 600M, the ceiling.</p></section>'
            f'<section><h3>Public works owed to you</h3>{owed}</section>' + nl
            + foot())


CSS = """
:root{--canvas:#E4DDCB;--paper:#fff;--ink:#16150F;--soft:#5C584A;--rule:#C9C1AC;
  --verm:#C8291A;--walnut:#6E4A2C;--slate:#3D5568;--mono:"Courier New",Courier,monospace}
*{box-sizing:border-box}
body{margin:0;background:var(--canvas);color:var(--ink);font:16px/1.5 "Helvetica Neue",Helvetica,Arial,sans-serif}
.wrap{max-width:76rem;margin:0 auto;padding:2rem 1rem 4rem}
.top{background:var(--verm);color:#fff;padding:2rem 2rem 1.6rem;margin-bottom:1.4rem}
.top h1{margin:0;font-size:1.9rem;letter-spacing:.14em;text-transform:uppercase}
.top p{margin:.5rem 0 0;font-family:var(--mono);font-size:.8rem;letter-spacing:.1em;text-transform:uppercase}
.intro{background:var(--paper);padding:1.6rem 2rem;margin-bottom:1.6rem}
.intro p{margin:0 0 .6rem}
.pair{display:flex;flex-wrap:wrap;gap:1.2rem;justify-content:center;margin-bottom:2rem}
.pairlabel{font:700 .8rem var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--soft);
  text-align:center;margin:0 0 .6rem}
.card{width:5.5in;height:8.5in;background:var(--paper);display:flex;flex-direction:column;
  padding:.25in .3in .2in;font-size:9.6pt;line-height:1.34;overflow:hidden;position:relative;
  box-shadow:0 1px 0 rgba(0,0,0,.2)}
@media (max-width:760px){.card{width:100%;height:auto}}
/* card header: a thin bar in the tier's colour rather than a solid band, to save ink */
.ch{display:flex;justify-content:space-between;align-items:flex-start;
  margin:0 0 .1in;padding:.07in 0 .06in;border-top:.09in solid var(--tier);border-bottom:1.5px solid var(--ink)}
.ch.general{--tier:var(--ink)}.ch.imperial{--tier:var(--verm)}
.ch.upper{--tier:#2B2A24}.ch.lower{--tier:var(--walnut)}.ch.outside{--tier:var(--slate)}
.ch h2{margin:0;font-size:15pt;letter-spacing:.06em;text-transform:uppercase;color:var(--tier)}
.ch p{margin:.15em 0 0;font:8pt var(--mono);letter-spacing:.06em;color:var(--soft)}
.ch .mark{flex:none;width:.42in;height:.42in;color:var(--tier)}
section{margin:0 0 .11in}
h3{margin:0 0 .05in;font:700 7.6pt var(--mono);letter-spacing:.14em;text-transform:uppercase;color:var(--verm);
  border-bottom:1.5px solid var(--ink);padding-bottom:.03in}
p{margin:0 0 .04in}
.small{font-size:8pt;color:var(--soft)}
table{width:100%;border-collapse:collapse;font-size:8.6pt}
th{font:700 6.8pt var(--mono);letter-spacing:.08em;text-transform:uppercase;text-align:left;
  padding:.02in .04in;border-bottom:1px solid var(--ink)}
td{padding:.025in .04in;border-bottom:.5px solid var(--rule);vertical-align:top}
table.income td,table.income th{text-align:right;font-family:var(--mono);font-size:10.5pt;padding:.045in .06in}
table.income td:first-child,table.income th:first-child{text-align:left}
table.income td:nth-child(3){font-weight:700}
table.income td:nth-child(2),table.income th:nth-child(2){color:var(--soft);border-right:1.5px solid var(--ink)}
table.income th.grp{text-align:center;border-bottom:.5px solid var(--rule);padding-bottom:0}
table.income th.blank{border-bottom:0}
table.works{font-size:7.8pt} table.works td:nth-child(3),table.works td:nth-child(4){white-space:nowrap}
table.pile{font-size:8.2pt}
table.obj td:first-child{white-space:nowrap;font-family:var(--mono);width:3.4em}
table.owed td:nth-child(2){white-space:nowrap}
ol.turn{list-style:none;margin:.04in 0;padding:0}
ol.turn li{display:flex;gap:.08in;padding:.035in 0;border-bottom:.5px solid var(--rule)}
ol.turn .n{flex:none;width:.2in;height:.2in;border-radius:50%;background:var(--verm);color:#fff;
  font:700 8pt/0.2in var(--mono);text-align:center}
ol.turn b{font-size:9.6pt}
ol.turn .who{font:7pt var(--mono);letter-spacing:.08em;text-transform:uppercase;color:var(--soft);margin-left:.08in}
ol.turn p{margin:.01in 0 0;font-size:8.6pt}
.anytime{font-size:8.6pt;border:1px solid var(--rule);padding:.05in .08in;margin-top:.06in}
dl.money{display:grid;grid-template-columns:auto 1fr;gap:.015in .1in;margin:0;font-size:8.4pt}
dl.money dt{font-weight:700;white-space:nowrap}dl.money dd{margin:0}
ul.duties{margin:0;padding-left:1.1em}ul.duties li{margin:0 0 .025in}
.char{font-style:italic;font-size:8.8pt;color:#3A372E;margin:0 0 .1in}
ol.script li{padding:.04in 0}
ol.script p.say{font-style:italic;font-size:9pt;color:var(--ink);margin:.015in 0 0}
ol.script p.check{font-size:8.2pt;color:var(--soft);margin:.01in 0 0}
ul.checks{list-style:none;margin:0;padding:0}
ul.checks li{position:relative;padding-left:1.4em;margin:0 0 .04in}
ul.checks li::before{content:"";position:absolute;left:0;top:.15em;width:.75em;height:.75em;border:1.2px solid var(--ink)}
section.anytime{padding:.07in .1in}section.anytime ul{margin-top:.03in}
ol.dis{margin:0;padding-left:1.3em}ol.dis li{margin:0 0 .02in}
ol.dis li span{margin-right:.4em}ol.dis li b{white-space:nowrap}
.cf{margin-top:auto;font:6.6pt var(--mono);letter-spacing:.08em;color:#9A9384;text-align:center;padding-top:.05in}
.piece{white-space:nowrap}
.dense{display:contents}
.dense dl.money{font-size:8pt;gap:.005in .1in}
.dense table.works,.dense table.pile{font-size:7.6pt}
.dense td{padding:.015in .04in}
.dense section{margin-bottom:.08in}
.print{display:none}
@media print{
  @page{size:letter landscape;margin:0}
  body{background:#fff}
  .screen{display:none}
  .print{display:block}
  .sheet{width:11in;height:8.5in;display:flex;break-after:page;page-break-after:always}
  .sheet .card{box-shadow:none;border-right:1px dashed #BBB}
  .card,ol.turn .n{-webkit-print-color-adjust:exact;print-color-adjust:exact}
}
"""


def build():
    cards = [("General", general_front(), '<div class="dense">' + general_back() + '</div>'),
             ("Running the round", running_front(), running_back())]
    cards += [(f"Province {p} · {ROLE[p]}", player_front(p), player_back(p)) for p in range(1, 9)]

    screen = "".join(
        f'<p class="pairlabel">{E(name)}</p><div class="pair"><div class="card">{f}</div>'
        f'<div class="card">{b}</div></div>' for name, f, b in cards)

    # Print: two cards per landscape letter sheet. The back sheet holds the same two
    # cards in swapped order, so they line up when printed duplex, flipped on the short edge.
    # Sheet 1: two general cards. Sheet 2: two "Running the round" cards. Then the provinces.
    order = [cards[0], cards[0], cards[1], cards[1]] + cards[2:]
    sheets = []
    for i in range(0, len(order), 2):
        a, b = order[i], order[i + 1]
        sheets.append(f'<div class="sheet"><div class="card">{a[1]}</div><div class="card">{b[1]}</div></div>')
        sheets.append(f'<div class="sheet"><div class="card">{b[2]}</div><div class="card">{a[2]}</div></div>')

    page = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dynasty — Reference Cards</title>
<style>{CSS}</style>
</head>
<body>
<div class="screen">
<div class="wrap">
<header class="top"><h1>Reference Cards</h1><p>Dynasty (1969) · a general card, a card for running the round, and one card per province, two-sided</p></header>
<div class="intro">
<p>Every player gets the <b>general card</b> (the round, the realia, the money and the public works) and the
<b>card for their own province</b> (income table, duties, objective, what they are owed, personal disasters).
Whoever runs the round, usually the Emperor or whoever is teaching the game, also gets <b>Running the round</b>:
a script for each step, with what to check before moving on. Each card is half a letter sheet, front and back.</p>
<p><b>To print:</b> print this page on letter paper, landscape, <b>double-sided, flipped on the short edge</b>,
with background graphics on. You get six sheets: two general cards, two Running the round cards, then provinces
1–2, 3–4, 5–6 and 7–8.
Cut each sheet down the middle. If the backs come out upside down, switch to flipping on the long edge.
Print the first sheet again for more general cards.</p>
<p class="small">Figures are in millions of bags of grain and follow the rulebook.</p>
</div>
{screen}
</div>
</div>
<div class="print">{"".join(sheets)}</div>
</body>
</html>
"""
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:
        f.write(page)
    add_glyphs.main(OUT)


if __name__ == "__main__":
    build()
