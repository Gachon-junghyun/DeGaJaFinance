# SWEEP_READ — industry_US — 2026-07-23

> Stage 3/10 (SWEEP). **The reading, not a second copy of the data.** Numbers live in
> `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `../CYCLE_EXPOSURE.md`. Sector rows and per-name
> rows are **cited by artifact, never reprinted**. Not advice.

**asof `SECTOR_FLOW_US.json` = 2026-07-22 close.** The 07-23 US session has not opened, and today's
oil/rate shock (MACRO §A-2) is **not** in any number below.

---

## 1. Universe headline

**n = 300 · wflow +0.13 · 🟢 25 / 🔴 70** (`SECTOR_FLOW_US.json §universe`). Mildly positive on
mega-cap weight; **2.8 reds per green** underneath it.

---

## 2. Cross-checks against the MACRO transmission matrix

### ★ 2.1 — CONTRADICTS: Health Care is the **top-flow sector on the board**, and the desk has carried it UW

`§sector_rotation` ranks **Health Care #1 on wflow (+0.351)** with **eqflow +0.155** and **6 green / 3
red** — the most greens of any sector. MACRO §E carries it **N−** (already upgraded from UW because the
tariff threads ENDED). **The money says the upgrade did not go far enough.**

What makes this hard to dismiss as a tag artifact: the six greens are confirmed on the **A-grade** axis,
not just the C-grade one. JNJ / ABBV / ABT / LLY / MRK / UNH are all positive on **both RS20 and RS60
vs SPY** (benchmark named, C1) with OBV agreeing. Per **D6** that is momentum carrying the proposition
and OBV merely corroborating — the correct order.

⚠ Two honest qualifiers. (a) It is also the **only sector besides Real Estate with a negative day-over-day
delta (−0.102)**, i.e. the strongest flow on the board is *decelerating*. (b) PFE is 🟡 and negative on
both axes — the sector is not uniform (**W5**).

### ★ 2.2 — CONTRADICTS: Info Tech's positive wflow is **entirely mega-cap**, and its breadth is the worst on the board

**wflow +0.201 vs eqflow −0.144** — a **0.345 spread, the widest divergence of any sector** — on
**4 green / 22 red of 56**. IT also posts the board's **largest positive delta (+0.319)**, so a reader
looking at wflow or delta alone would call IT the day's improving sector. **Breadth says the opposite.**
MACRO §E holds IT at **N**; this supports holding, and specifically warns ROTATION not to read IT's
positive wflow as sector health.

### ★ 2.3 — CONFIRMS, and upgrades the reason: Financials is the **only breadth-led sector on the board**

**eqflow +0.320 > wflow +0.253** — the only sector where the equal-weighted read exceeds the
cap-weighted one, on 7 green / 3 red. MACRO §E softened Financials to **OW−** because 2s10s flattened
and removed the steepener leg. **The flow says the surviving reason is breadth, not the mega-caps** —
which is a *different* and more durable justification than the one that just broke. C (−0.672, 🔴)
remains the single genuinely broken bank, replicating `STANDING_VIEW`. GS has improved from −0.450
(07-22) to −0.057.

### 2.4 — CONTRADICTS on timing: Industrials is **negative on flow** the same morning its two largest primes printed record backlogs

`§sector_rotation` has Industrials at **wflow −0.065 / eqflow −0.044, 2 green / 12 red, breadth 0.04**.
MACRO §E holds it **N+** on RTX's $289B and LMT's record $230.4B backlog — both of which printed at
**06:30 ET on 07-23**, i.e. **after** this sweep's asof. This is a clean, dated instance of the
`reject_ledger`'s own `A.flow미도착` class (thesis right, money not there yet), and it is stated as a
**timing gap**, not as a refutation in either direction.

⚠ **M26 did NOT replicate — it decayed.** The carried finding (5 primes wflow **+0.250, zero reds**
vs capital goods **−0.455**, spread **0.705**) measures on today's file as: primes mean **+0.081** with
**one red (LHX −0.440)**, capital-goods sample mean **−0.204**, **spread 0.285 — a 60% compression in
two sessions.** Prime RS20 vs SPY is now a median **+0.5** (flat). The "Industrials is two opposite
things" split is still directionally there but is **much weaker than the carried number**, and DEEP must
use today's figure, not M26's.

### 2.5 — CONFIRMS: M24 replicates almost exactly, on an independent date — R7 holds

Real Estate's reds are **digital infrastructure** (AMT/EQIX/DLR/CCI, all 🔴, mean **RS20 −9.85 vs SPY**)
while the classic-duration REITs are **bid** (WELL/VTR/SPG, all OBV-accumulating, mean **RS20 +8.37 vs
SPY**). **Spread 18.2pp** — M24 measured **18.2pp** on 07-21. Two independent dates, same magnitude.
**R7 is not a one-day artifact**, and MACRO §E's upgrade of Real Estate from UW to N− with an
instruction to *split* rather than tilt is supported. ⚠ RE nonetheless owns the **worst delta on the
board (−0.139)** and **0 greens of 12** — "split it" is not "own it".

---

## 3. Shortlist composition — the absences, each diagnosed

`US_LIVE_SHORTLIST.json` (15 names, floor $10B, 🟢가속 filter). Composition by count: **Financials 6 ·
Health Care 3 · Staples 1 · Industrials 2 (services/rail, not primes) · Energy 1 · mega-cap tech 2**.

| Absence | Diagnosis |
|---|---|
| **Refiners (VLO/MPC/PSX) — absent** | ★ **Filter artifact, not evidence — the exact failure this stage's spec warns about.** All three are **OBV-accumulating with RS20 +22 to +26 vs SPY**, the strongest 20-day relative in the sector, and all three are 🟡 solely because `vol_surge` is 0.87–0.92 (<1.2). They were filtered by a volume test, not by a flow test. ⚠ Counter-caveat the artifact does *not* remove: their margin KPI (the 3-2-1 crack) fell **−11.2%** on 07-23, after this file's asof (MACRO §D-P4) |
| **Semis / semicap — absent (0 of 56 IT names except AAPL/META)** | **Mixed, and the mix is the finding.** AMAT/LRCX/KLAC/INTC are all 🔴 with OBV distributing — but all four are **positive on RS60 vs SPY (+28.1 / +14.5 / +6.3 / +19.6)** while deeply negative on RS20 (−7.3 / −15.9 / −14.1 / −24.3). That is the signature of a **pullback inside an uptrend**, which is exactly what **S6 branch A** is registered to test tonight. Per **D6** the A-grade momentum read may not be overridden by the C-grade OBV tag — so this absence is **not** admissible as evidence that the equipment leg is broken |
| **Security/observability (PANW/CRWD/FTNT/DDOG) — absent** | ★ **Filter artifact, and a measured cost.** All four are positive on **both** RS20 and RS60 vs SPY (RS60 **+83.1 / +63.5 / +79.2 / +85.1**), three are OBV-accumulating, and all four are 🟡 because `vol_surge` is **0.68–0.78**. M28 replicates cleanly; the tag does not see it |
| **Utilities · Real Estate · Materials — absent** | **Genuine.** All three have **0 greens** (`§sector_rotation`), so there is nothing for the filter to drop. Consistent with MACRO §E |
| **Defense primes — absent** | **Genuine as of 07-22**, and superseded by §2.4's timing gap |

### ★ M25 replicated on an independent date — the 🟢 tag is a volume test wearing a flow label

Measured on today's file: **`velocity` is `None` on all 300 rows** (unchanged), so `has_conviction`
reduces to OBV, and 🟢 requires **OBV ∧ RS20>0 ∧ vol_surge≥1.2**. **93 names pass OBV-accumulating ∧
RS20>0; only 25 are 🟢. 68 are blocked by `vol_surge` alone** (07-22: 99 blocked — same mechanism,
same order of magnitude).

**Consequence for this run, stated once:** the shortlist's three most interesting absences above are
**all** `vol_surge` casualties, and two of them (refiners, security) are the desk's best-measured
A-grade momentum. **Downstream stages must treat a US 🟡 as "not volume-surging", not as "no flow".**
Fixing the gate is open dig **D11** (needs human approval).

---

## 4. Cycle-exposure GAP `[../CYCLE_EXPOSURE.md]`

🚨 **GAP — Energy / oil-refining (rank 2): epicenter exposure 0.0% vs required 8.0% (−8.00pp).**
The book touches the cycle only through adjacent/fuel names (KMI, LNG) — beta to the consequence,
none to the engine. Rank-1 AI-compute is compliant at 12.25% (need 12.0%); rank-3 missile-defense has
no threshold set. **Handed to ALPHA's action bracket.**

⚠ **This GAP must be read with a live objection attached, or it is misleading.** The guard's own
wording is *"a crowded tape gates the ADDs, not the core's existence."* Today the objection is **not a
crowded tape** — it is that the cycle's **own engine deteriorated**: the 3-2-1 crack fell **−11.2%** on
07-23 while crude rose 5.2% (MACRO §D-P4), the fourth observation in the desk's C4 detachment counter.
A structural GAP flag and a deteriorating KPI are different objects; both go forward, neither cancels
the other.

⚠ **Registry defects, carried not re-discovered (D20):** the registry is `data/cycles/cycle_registry.json`,
`updated 2026-07-17` — **6 days stale** — while `cycle_exposure.py`'s own output footer still prints
`data_build/cycles/cycle_registry.json`, **a path that does not exist**. There is still **no AI-security
row**, so no GAP can fire against the book's 0% exposure to the theme MACRO registered as **P7** and the
one whose thread peaked at 23 outlets this week. Rank-1's epicenter list still scores **MU (RS60 +88.5)
and AVGO (−10.8)** as the same bucket — ~99pp of dispersion inside one "epicenter", so 12.25%
compliance is not a statement about owning the engine (**W5**). Human approval required for all three.

---

## 5. Handoff to ROTATION

Four cross-checks that change something, in order of how much:
1. **Health Care is #1 on flow with 6 A-grade-confirmed greens** — against a standing UW/N−. The
   sharpest belief-vs-money disagreement on the board (§2.1).
2. **IT is mega-cap-only** (wflow +0.201 / eqflow −0.144, 4 green : 22 red) — hold, do not chase the
   delta (§2.2).
3. **Financials' surviving reason is breadth, not the steepener** that broke this morning (§2.3).
4. **M26 decayed 60% and M24 replicated exactly** — one carried number must be refreshed, the other
   is now twice-measured (§2.4, §2.5).
