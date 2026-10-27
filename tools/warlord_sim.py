"""Simulated Warlord campaigns, to balance the soldier rules.

A Monte Carlo model of the Warlord against the provinces on the real board
(map.json): king moves one square a round, captures straight on only, raids on
stepping onto an un-raided square of an occupied province, river tolls. The
economy and the auctions are abstracted: each realia province places one piece a
round for the first four rounds on its deepest free square (sometimes carelessly),
the Emperor builds palaces, provinces buy guards to a random budget when the
Warlord comes near, and the Warlord plays a greedy campaign for his objective.

It compares rule variants (see VARIANTS) at 8, 6 and 5 players and reports how
often and how fast the Warlord completes his objective, what it costs him, and how
widely the raids spread. It is a balance probe, not a full game: no I Ching, no seat
changes, no deals.

  python tools/warlord_sim.py                 # the full table (a few minutes)
  python tools/warlord_sim.py --games 50      # quicker
  python tools/warlord_sim.py --trace 8 C     # one game, round by round
"""
import argparse, json, os, random, statistics
from collections import deque

HERE = os.path.dirname(os.path.abspath(__file__))
MAP = json.load(open(os.path.join(HERE, "..", "map.json"), encoding="utf-8"))
G = MAP["grid"]; ROWS, COLS = len(G), len(G[0])
RIVERS = list(MAP["rivers"].values())
SQ = [(r, c) for r in range(ROWS) for c in range(COLS)]
KING = [(a, b) for a in (-1, 0, 1) for b in (-1, 0, 1) if (a, b) != (0, 0)]
ORTH = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def name(q): return f"{chr(65+q[0])}{q[1]+1}"
def reg(q): return G[q[0]][q[1]]
def prov(q): return int(reg(q)) if reg(q) in "1234567" else None
def on(q): return 0 <= q[0] < ROWS and 0 <= q[1] < COLS
def nb(q, ds=KING): return [(q[0]+a, q[1]+b) for a, b in ds if on((q[0]+a, q[1]+b))]
def orth(a, b): return abs(a[0]-b[0]) + abs(a[1]-b[1]) == 1
def kd(a, b): return max(abs(a[0]-b[0]), abs(a[1]-b[1]))

def _ccw(a, b, c): return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
def _cross(a, b):
    p1, p2 = (a[1]+.5, a[0]+.5), (b[1]+.5, b[0]+.5)
    n = 0
    for path in RIVERS:
        for i in range(len(path)-1):
            q1, q2 = path[i], path[i+1]
            if _ccw(q1, q2, p1)*_ccw(q1, q2, p2) < 0 and _ccw(p1, p2, q1)*_ccw(p1, p2, q2) < 0:
                n += 1; break
    return n
RIVER_X = {}
def rivers(a, b):
    k = (a, b)
    if k not in RIVER_X: RIVER_X[k] = _cross(a, b)
    return RIVER_X[k]

# ------------------------------------------------------------------ variants
# sea: soldiers may enter the sea.  emperor: "palace" (a palace raid is the Emperor's
# piece), "none" (the Emperor isn't a target), "wild8" (none, but at 8 players one
# palace raid may stand in for one player's piece).  recruit: the Warlord buys a soldier
# for 20, one a round, after his march, on his own desert, up to the player count.
# guard: "wait" (bought soldiers move once their province is raided), "home" (they
# move inside their own province at once, anywhere once raided).
VARIANTS = {
    "A": dict(label="1969 as we first read it: closed sea, palace counts", sea=False, emperor="palace", recruit=False, guard="wait"),
    "B": dict(label="Now: open sea, Emperor left out", sea=True, emperor="none", recruit=False, guard="wait"),
    "C": dict(label="B + Warlord recruits", sea=True, emperor="none", recruit=True, guard="wait"),
    "D": dict(label="C + palace wildcard at 8", sea=True, emperor="wild8", recruit=True, guard="wait"),
    "E": dict(label="D + home guard", sea=True, emperor="wild8", recruit=True, guard="home"),
    "F": dict(label="D, palace wildcard at every count", sea=True, emperor="wild", recruit=True, guard="wait"),
    "G": dict(label="B + palace wildcard at 8 (no recruiting)", sea=True, emperor="wild8", recruit=False, guard="wait"),
    "H": dict(label="G + recruits only replace losses", sea=True, emperor="wild8", recruit="replace", guard="wait"),
    "I": dict(label="G + recruits cost 40", sea=True, emperor="wild8", recruit=True, guard="wait", cost=40),
    "J": dict(label="G + recruits up to the starting army + 1", sea=True, emperor="wild8", recruit="replace", extra=1, guard="wait"),
    "K": dict(label="G + recruits up to the starting army + 2", sea=True, emperor="wild8", recruit="replace", extra=2, guard="wait"),
}
TABLES = {8: [1, 2, 3, 4, 5, 6, 7, 8], 6: [1, 2, 3, 5, 7, 8], 5: [1, 5, 6, 7, 8]}
YEARS = {8: 10, 6: 10, 5: 9}
DEFENCE = {"low": (0, 0, 1), "medium": (0, 1, 1, 2), "high": (1, 2, 2, 3)}   # guards a province will buy

class Game:
    def __init__(self, n, v, defence, rng, log=False):
        self.n, self.v, self.rng, self.log = n, VARIANTS[v], rng, log
        self.seats = TABLES[n]
        self.realia_seats = [s for s in self.seats if 2 <= s <= 7]
        self.walk = set(q for q in SQ if reg(q) != "S" or self.v["sea"])
        und = "8nS" if self.v["sea"] else "8n"
        self.start_ok = [q for q in SQ if reg(q) in und]
        # depth of each province square: steps from the nearest walkable non-province square
        out = [q for q in self.walk if prov(q) is None]
        self.depth = self.bfs(out)
        self.T = YEARS[n]
        self.realia = {}           # square -> owner seat
        self.palaces = {}          # square -> name
        self.raided = set()
        self.hit = {s: 0 for s in self.seats}       # raids suffered per seat
        self.woke = set()                            # seats raided at least once
        self.got = set()                             # seats whose piece the Warlord has raided
        self.palace_counted = False
        self.cash = 60.0
        self.lost = self.recruited = self.guards_bought = 0
        self.budget = {s: rng.choice(DEFENCE[defence]) for s in self.realia_seats}
        if 1 in self.seats:
            self.budget[1] = rng.choice(DEFENCE[defence]) if self.v["emperor"] != "none" else 0
        self.guards = []                             # [square, seat]
        self.done = None
        self.mercs = 8                               # the second colour in the box
        k = 4 if n >= 8 else 2
        self.cap = k + self.v.get("extra", 0) if self.v["recruit"] == "replace" else n
        self.cost = self.v.get("cost", 20)
        self.W = self.place_army(k)

    # ---- helpers
    def bfs(self, sources, block=frozenset()):
        d = {q: 0 for q in sources}; dq = deque(sources)
        while dq:
            q = dq.popleft()
            for p in nb(q):
                if p in self.walk and p not in d and p not in block:
                    d[p] = d[q] + 1; dq.append(p)
        return d
    def say(self, *a):
        if self.log: print(" ", *a)
    def wild(self):
        e = self.v["emperor"]
        return e == "wild" or (e == "wild8" and self.n >= 8)
    def needed(self):
        """Seats whose piece the Warlord still needs, and whether a palace would help."""
        need = [s for s in self.realia_seats if s not in self.got]
        if self.v["emperor"] == "palace" and 1 in self.seats and 1 not in self.got:
            return need, True
        if self.wild() and not self.palace_counted and need:
            return need, True
        return need, False
    def complete(self):
        need, _ = self.needed()
        if self.v["emperor"] == "palace":
            return not need and (1 in self.got or 1 not in self.seats)
        if self.wild() and self.palace_counted:
            return len(need) <= 1
        return not need
    def target_squares(self):
        need, pal = self.needed()
        t = [q for q, s in self.realia.items() if s in need and q not in self.raided]
        if pal: t += [q for q in self.palaces if q not in self.raided]
        return t

    def place_army(self, k):
        # greedy k-median over the provinces' deep squares
        deep = {s: max(self.depth.get(q, 0) for q in SQ if prov(q) == s) for s in self.realia_seats + ([1] if 1 in self.seats else [])}
        cores = {s: [q for q in SQ if prov(q) == s and self.depth.get(q, 0) >= deep[s] - 1] for s in deep}
        fields = {s: self.bfs(cores[s]) for s in cores}
        pos = []
        for _ in range(k):
            def cost(q):
                return sum(min([fields[s].get(p, 99) for p in pos + [q]]) for s in fields)
            cand = self.rng.sample(self.start_ok, 160)
            pos.append(min(cand, key=cost))
        return pos

    # ---- the provinces
    def place_pieces(self, t):
        if t <= 4:
            for s in self.realia_seats:
                free = [q for q in SQ if prov(q) == s and q not in self.realia and q not in self.raided
                        and all(g[0] != q for g in self.guards)]
                if not free: continue
                if self.rng.random() < 0.2:
                    q = self.rng.choice(free)                       # a careless placement
                else:
                    top = max(self.depth[q] for q in free)
                    q = self.rng.choice([q for q in free if self.depth[q] >= top])
                self.realia[q] = s
        if 1 in self.seats and t in (1, 2, 5):
            free = [q for q in SQ if prov(q) == 1 and q not in self.palaces and q not in self.raided]
            top = max(self.depth[q] for q in free)
            q = self.rng.choice([q for q in free if self.depth[q] >= top - (0 if t == 1 else 1)])
            self.palaces[q] = {1: "Summer Palace", 2: "Winter Palace", 5: "Marble Pagoda"}[t]

    def treasures(self, s):
        if s == 1: return list(self.palaces)
        return [q for q, o in self.realia.items() if o == s]

    def guard_score(self, q, s, me=None):
        """How well a guard on q protects seat s's treasures, less the risk of standing there.
        Standing on a piece is the strong defence: a Warlord soldier can take it only by
        capturing the guard straight on, which means first ending a move beside it."""
        sc = 0.0
        for r in self.treasures(s):
            if r in self.raided: continue
            w = 1.0 / (1 + min([kd(r, x) for x in self.W] or [9]))
            if q == r: sc += 4 * w
            ring = [p for p in nb(r) if prov(p) == s]
            sc += 0.5 * w * sum(1 for p in ring if orth(p, q))
        if any(orth(q, x) for x in self.W):
            sc -= 3.0                            # the Warlord moves first: he'd capture it
        if any(g[0] == q and g is not me for g in self.guards):
            sc -= 2.0                            # one guard per square is enough
        return sc

    def buy_guards(self):
        for s, b in self.budget.items():
            have = sum(1 for g in self.guards if g[1] == s)
            if have >= b or self.mercs <= 0: continue
            tr = [r for r in self.treasures(s) if r not in self.raided]
            if not tr: continue
            near = min(kd(r, x) for r in tr for x in self.W) if self.W else 99
            if near > 5 and s not in self.woke: continue
            cand = [q for q in SQ if prov(q) == s and q not in self.palaces and all(g[0] != q for g in self.guards)]
            if not cand: continue
            q = max(cand, key=lambda q: self.guard_score(q, s) + self.rng.random() * 0.01)
            self.guards.append([q, s]); self.mercs -= 1
            self.cash += 5; self.guards_bought += 1
            self.say(f"Province {s} buys a guard on {name(q)}")

    def active(self, g, where):
        if g[1] in self.woke: return True
        return self.v["guard"] == "home" and prov(where) == g[1]

    def guards_move(self):
        taken = set()
        for g in self.guards:
            hits = [x for x in self.W if orth(g[0], x) and x not in taken and self.active(g, x)]
            if hits:
                x = hits[0]; taken.add(x)
                self.W.remove(x); self.lost += 1
                self.say(f"Guard of {g[1]} captures the Warlord's soldier on {name(x)}")
                g[0] = x
                continue
            if not self.active(g, g[0]): continue
            cand = [g[0]] + [p for p in nb(g[0]) if prov(p) == g[1] and p in self.walk
                             and all(h[0] != p for h in self.guards if h is not g) and p not in self.W]
            g[0] = max(cand, key=lambda q: self.guard_score(q, g[1], g) + (0.05 if q == g[0] else 0))

    # ---- the Warlord
    def warlord_move(self, t, noraid):
        targets = self.target_squares()
        fields = {q: self.bfs([q]) for q in targets}
        # assign soldiers to distinct targets greedily
        pairs = sorted(((fields[q].get(w, 99), i, q) for i, w in enumerate(self.W) for q in targets))
        aim, used = {}, set()
        for d, i, q in pairs:
            if i in aim or q in used: continue
            aim[i] = q; used.add(q)
        for i, q in [(i, q) for d, i, q in pairs if i not in aim]:
            aim[i] = q
        new = []
        for i, w in enumerate(list(self.W)):
            if w not in self.W: continue
            best, bs = w, -1e9
            for p in [w] + [p for p in nb(w) if p in self.walk]:
                gd = [g for g in self.guards if g[0] == p]
                if gd and not orth(w, p): continue                     # enter a guard's square only straight on
                s = prov(p)
                raid = s in self.seats and s != 8 and p not in self.raided and p != w
                if raid and noraid: continue
                sc = 0.0
                need, pal = self.needed()
                if raid and self.realia.get(p) in need: sc += 1000
                if raid and pal and p in self.palaces: sc += 800
                if raid: sc += 10 if s == 1 else 5
                if gd: sc += 30
                # a raid here wakes this province's guards before they move
                danger = any((self.active(g, p) or (raid and g[1] == s)) and orth(g[0], p)
                             for g in self.guards if g[0] != p)
                # a guard standing on a piece he needs: getting beside it straight on sets up a
                # capture-raid next round, worth a soldier when he has one to spare
                bait = any(orth(g[0], p) and self.realia.get(g[0]) in need and g[0] not in self.raided
                           for g in self.guards)
                if bait: sc += 200
                if danger and sc < 800:
                    spare = len(self.W) >= 3 or (self.v["recruit"] and self.cash >= self.cost)
                    sc -= 150 if spare else 400
                if i in aim:
                    sc -= 20 * fields[aim[i]].get(p, 60)
                if p != w and s in self.seats and s != 8: sc -= 5 * rivers(w, p)
                sc += self.rng.random()
                if sc > bs: best, bs = p, sc
            self.step(i, w, best, noraid)

    def step(self, i, w, p, noraid):
        if p == w: return
        k = self.W.index(w); self.W[k] = p
        s = prov(p)
        if s in self.seats and s != 8 and rivers(w, p): self.cash -= 5 * rivers(w, p)
        for g in [g for g in self.guards if g[0] == p]:
            self.guards.remove(g); self.say(f"Warlord captures {g[1]}'s guard on {name(p)}")
        if s in self.seats and s != 8 and p not in self.raided and not noraid:
            self.raided.add(p); self.hit[s] += 1; self.woke.add(s)
            need, pal = self.needed()
            if self.realia.get(p) in need:
                self.got.add(self.realia.pop(p)); self.say(f"Warlord takes {s}'s piece on {name(p)}")
            elif p in self.palaces:
                self.cash += 20
                if pal:
                    if self.v["emperor"] == "palace": self.got.add(1)
                    else: self.palace_counted = True
                self.say(f"Warlord raids the {self.palaces[p]} on {name(p)}")
            else:
                self.cash += 10 if s == 1 else 5

    def recruit(self):
        if not self.v["recruit"] or len(self.W) >= self.cap or self.cash < self.cost: return
        targets = self.target_squares()
        desert = [q for q in SQ if reg(q) == "8" and q not in self.W]
        if targets:
            f = self.bfs(targets)
            q = min(desert, key=lambda q: f.get(q, 99) + self.rng.random())
        else:
            q = self.rng.choice(desert)
        self.W.append(q); self.cash -= self.cost; self.recruited += 1
        self.say(f"Warlord recruits a soldier on {name(q)}")

    def play(self):
        for t in range(1, self.T + 1):
            self.say(f"Year {t}: army {len(self.W)}, cash {self.cash:g}, got {sorted(self.got)}"
                     f"{' +palace' if self.palace_counted else ''}")
            self.place_pieces(t)
            self.cash += 10 if t <= 4 else (0 if t <= 7 else -10)
            self.buy_guards()
            noraid = self.rng.random() < 0.1
            self.warlord_move(t, noraid)
            if self.complete():
                self.done = t; self.say(f"Objective complete in year {t}"); break
            self.recruit()
            self.guards_move()
            if not self.W and not self.v["recruit"]:
                break
        return self

def progress(g):
    need = len(g.realia_seats) + (1 if g.v["emperor"] == "palace" and 1 in g.seats else 0)
    have = len(g.got) + (1 if g.palace_counted else 0)
    return min(have, need) / need

def run(n, v, defence, games, seed):
    rng = random.Random(seed)
    out = [Game(n, v, defence, rng).play() for _ in range(games)]
    done = [g.done for g in out if g.done]
    spread = statistics.mean(sum(1 for s in g.realia_seats if g.hit[s]) / len(g.realia_seats) for g in out)
    emp = statistics.mean(g.hit.get(1, 0) for g in out)
    return dict(pct=100 * len(done) / games, year=statistics.median(done) if done else None,
                prog=100 * statistics.mean(progress(g) for g in out),
                lost=statistics.mean(g.lost for g in out), rec=statistics.mean(g.recruited for g in out),
                spread=100 * spread, emp=emp, guards=statistics.mean(g.guards_bought for g in out))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--games", type=int, default=200)
    ap.add_argument("--trace", nargs=2, metavar=("PLAYERS", "VARIANT"))
    ap.add_argument("--defence", default="medium")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--variants", default="".join(VARIANTS))
    a = ap.parse_args()
    if a.trace:
        Game(int(a.trace[0]), a.trace[1], a.defence, random.Random(a.seed), log=True).play()
        return
    print("| Players | Defence | Variant | Completes | Median year | Progress | Soldiers lost | Recruited | Provinces raided | Raids on Emperor | Guards bought |")
    print("|---|---|---|---|---|---|---|---|---|---|---|")
    for n in (8, 6, 5):
        for defence in ("low", "medium", "high"):
            for v in a.variants:
                r = run(n, v, defence, a.games, a.seed)
                print(f"| {n} | {defence} | {v} | {r['pct']:.0f}% | {r['year'] or '—'} | {r['prog']:.0f}% | "
                      f"{r['lost']:.1f} | {r['rec']:.1f} | {r['spread']:.0f}% | {r['emp']:.1f} | {r['guards']:.1f} |", flush=True)
    print()
    for k in a.variants: print(f"- {k}: {VARIANTS[k]['label']}")

if __name__ == "__main__":
    main()
