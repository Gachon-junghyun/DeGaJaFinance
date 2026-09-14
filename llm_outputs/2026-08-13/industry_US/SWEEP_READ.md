# SWEEP_READ — industry_US · 2026-08-13 · Stage 4/11 (L1·SWEEP)

> The **reading**, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json`,
> `US_LIVE_SHORTLIST.json`, `../CYCLE_EXPOSURE.md`. This file holds only what those cannot say.
> Analytical only (P4).

## §0 · Instrument health, read BEFORE the numbers

`SECTOR_FLOW_US.json §scoring` = **`n_axes` 3 · `vel_coverage` 0.170 · `scored` 300 ·
`dropped_missing_axis` 0.** **Every name scored on the same three axes** — the 2026-08-09
per-name axis-drop defect (worth up to **+0.5**) did **not** recur.

⚠⚠ **A decision this stage made and is stating rather than burying.** The news tunnel came back
**after** the sweep ran (MACRO §0: `fts search Nvidia` → **3,830** at 22:20 KST vs **5/5 URLError**
at 22:14). **The sweep was NOT re-run on 4 axes.** Reason, in order: (i) the Δ baseline
`history.json["2026-08-11"]` is **`nonews`/3-axis**, so a 4-axis re-run would make today's Δ an
apples-to-oranges subtraction and **fail PREFLIGHT G2**, which currently PASSes; (ii) a re-run
overwrites the `"2026-08-12"` snapshot key and would break the next run's baseline too.
⇒ **3-axis is carried deliberately, and `vel_coverage 17.0%` describes the tunnel, not the news.**

## §1 · Universe headline

**n = 300 · wflow −0.193 · 🟢 16 / 🔴 76** (`SECTOR_FLOW_US.json §universe`). Δ = **one settled
session** (08-11 → 08-12), 300/300 names.

## §2 · Cross-checks against the MACRO matrix — three CONFIRM, three CONTRADICT

| MACRO §G said | Flow says | Verdict |
|---|---|---|
| **ENRG OW− held**, price leg intact | **rank 1 on BOTH axes** (`§sector_rotation`), the only sector with a positive Δ *and* positive levels on both, no flipper | ✅ **CONFIRM** |
| **HLTH N+ held**, best long window | **rank 2 on both axes, gap 0.011 — the tightest cap-vs-equal agreement of 11** | ✅ **CONFIRM, with a deceleration flag**: Δ has gone **+0.157 (08-12) → −0.014 (today)**. The level agrees; the change no longer does |
| **UTIL UW held** | **0 of 15 names at `OBV 매집 ∧ RS20>0` — the only REAL absence on the board, second run running** | ✅ **CONFIRM, and it is the strongest confirmation on the page** |
| ★ **IT: an argument for promotion** (positive on all four price windows, best sector on the print day, FINRA covering) | 🚨 **The flow axis refuses it and splits internally**: IT holds **the most 🟢 of any sector (6) AND the most 🔴 (19)**, wflow −0.136 / eqflow −0.100 both negative, **21 of 56 at the pre-condition** | ⚠⚠ **CONTRADICT — and the contradiction is INTERNAL to IT, not between price and flow.** A sector that is simultaneously the board's biggest accumulator and its biggest distributor is not one object. **ROTATION must not resolve this by picking the axis it likes** |
| ★★ **MATR N− held**, "the sector is now one name" (NEM exc5 +12.6 vs XLB exc5 −0.47) | 🚨 **Flow does not support "one name"**: **6 of 12 Materials names sit at `OBV 매집 ∧ RS20>0` — a 50% rate, 2nd-highest on the board**, and **eqflow −0.029 is far less negative than wflow −0.106** (LIN 24.7%, G3 flipper) | ⚠⚠ **CONTRADICT.** The *price* window says one name; the *accumulation* axis says half the sector. **Both are true of different windows** — MACRO measured 5 sessions, OBV measures the money's direction. Handed to ROTATION as a contradiction, not a resolution |
| **STPL UW− held** | 🚨 **Δ +0.120 is the LARGEST positive Δ on the entire board**, from the sector sitting at the second-lowest tilt | ⚠ **CONTRADICT on the change axis only.** Levels still agree with the UW− (wflow −0.103, eqflow −0.130, breadth 0.00, **3 of 19** at the pre-condition). **A one-session Δ is n=1 (S1)** — this is a watch item, not a promotion case |

⚠ **Two more gaps worth naming because they decide which axis ROTATION may use:**
**COMM `wflow −0.708` vs `eqflow −0.111` = a 0.597 gap, the widest on the board** (GOOGL-owned), and
**DISC `wflow −0.374` vs `eqflow −0.063` = 0.311** (AMZN-owned). **Neither sector is on the G3 flip
list**, so `wflow` is technically admissible — but a 0.6 gap means the cap-weighted number is a
statement about one company, and both sectors' Δ are the board's worst (**COMM −0.234 · DISC −0.194**).

## §3 · The filter artifact, measured again — **M144's SEVENTH replication, and it is now 100%**

**98 names sit at `OBV 매집 ∧ RS20 > 0` and are NOT tagged 🟢. All 98 — 100.0% — are blocked by
`vol_surge < 1.2` alone.** Not one is blocked by any other axis.

⇒ **`breadth` and the 🟢 count are, on this board, a `vol_surge` filter wearing a breadth label.**
Every sector reading 0.00 breadth must be checked against its pre-condition count before the zero is
cited as evidence:

| Sector | at `OBV 매집 ∧ RS20>0` | breadth | Reading |
|---|---|---|---|
| **Health Care** | **19 / 32 = 59%, the highest RATE on the board** | **0.00** | 🚨 **artifact — not evidence of anything** |
| **Materials** | **6 / 12 = 50%** | **0.00** | 🚨 **artifact** |
| Industrials | 22 / 50 (highest count) | 0.02 | artifact |
| Information Technology | 21 / 56 | 0.11 | mixed — see §2 |
| **Utilities** | **0 / 15** | **0.00** | ✅ **REAL absence** |
| Real Estate / Cons. Staples | 3 / 12 · 3 / 19 | 0.00 · 0.00 | weak, but not zero |

★ **This is the same axis `ic_ledger` scores NEGATIVE** (`vol_surge` h=1 t −3.08, the only
Bonferroni-clearing cell) **while `sector_flow` weights it POSITIVE.** ⚠ That measurement is **KR**
and **R3/W1 bar transferring it** — but the *structural* point stands without it: **one axis is
deciding 100% of the 🟢 tags on the US board**, and no one has measured its sign on US data (`D243`).

## §4 · Shortlist composition — **read the absences, and one presence that should not exist**

`US_LIVE_SHORTLIST.json`: **15 names** (mcap ≥ $10B ∧ 🟢가속, capped at top-15 by flow).
**Clean-rise set (🟢 ∧ low-short/covering): 7.** **Crowded-short (squeeze fuel, NOT a buy): 1.**

**Sectors producing ZERO shortlist names: Health Care · Materials · Utilities · Real Estate ·
Consumer Staples.** Diagnosed before being cited, per the stage rule:
- **HLTH's zero and MATR's zero are §3 artifacts** — 19/32 and 6/12 of them are accumulating with
  positive RS and are excluded by `vol_surge` alone. **These absences are not evidence.**
- **UTIL's zero is real** (0/15 at the pre-condition). **RE and STPL are thin but non-zero** (3/12, 3/19).
- ⇒ **Of five absent sectors, only one absence carries information.** A stage reading "five sectors
  produced nothing" as breadth collapse would be wrong on four of them.

🚨🚨 **The presence that should not exist: `EA` is in the shortlist.**
It carries **flow +0.67 · OBV +0.74 (the highest OBV of the 15) · RS20 +0.1 · short z +1.01**, and it
is flagged **`new_green`** — one of only **five fresh ignitions** on the board (LITE · MPC · **EA** ·
ALL · BAC). **`EA` went private 2026-08-04/05.** This is **`R56` on day 29**, and it has now
progressed through three stages of damage: a stale price (08-05) → **a null 08-12 close** (PREFLIGHT
G5) → **a top-15 shortlist slot with the highest OBV in the set** (today). ⚠ **20% of this run's
`new_green` ignitions are a non-trading security**, and any COMM breadth number inherits it.

## §5 · Cycle exposure — ✅ no GAP

`../CYCLE_EXPOSURE.md` (book: real KIS, read-only): **AI-compute/semis rank 1 — epicentre 16.89% vs
need ≥12.0%** (AVGO · NVDA · ANET) ✅ · **Energy/oil-refining rank 2 — 10.8% vs need ≥8.0%**
(MPC · PSX) ✅ · Missile-defense rank 3 — 5.72% (RTX), **no threshold set ⇒ ⚪ n/a, not a pass**.
**No top-rank cycle GAP.** ⚠ The rank-3 ⚪ is an unset registry threshold, i.e. **unmeasured, not clean.**
