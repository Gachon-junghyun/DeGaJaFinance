# SWEEP_READ — industry_US · 2026-08-05 · **asof 2026-08-04 settled**

> Reading only. Every table lives in `SECTOR_FLOW_US.json` (§universe · §sector_rotation · §names)
> and `US_LIVE_SHORTLIST.json`. Nothing below reprints them.

## 0 · ⚠⚠ D74 handled — and QUANTIFIED, because the market opened mid-stage

**The first sweep pull completed at 09:33 ET, three minutes after the open, and the price cache
carried a live `2026-08-05` bar.** The contaminated run was kept, the cache was **trimmed to
≤ 2026-08-04**, and the sweep was **re-run**. Both outputs were diffed.

**What three minutes of unsettled tape did to the sector verdicts:**

| | |
|---|---|
| mean \|Δ wflow\| across 11 sectors | **0.102** |
| range | **−0.238 (Energy eqflow) → +0.247 (Comm wflow)** |
| green-count swings | **Financials +3 · Energy +2 · IT +2 · Real Estate −1 · Industrials −4** |

★★★ **A 3-minute-old bar manufactured 2 Energy greens and destroyed 4 Industrials greens.** The
08-03 run's controlled experiment measured 10 manufactured greens at a much later clock; **this run
measures the effect at three minutes and it is already verdict-changing.** ⇒ **D74 is not a
late-morning problem, it is an at-the-bell problem.** **The shipped `SECTOR_FLOW_US.json` is the
TRIMMED one.**

⚠ `us_live_shortlist.py` ran after the trim and reports `asof 2026-08-04` ✅.
⚠ **`us_top300.csv` is 21 days stale** (script warning) — market caps are old; **the mcap floor and
the wflow weights inherit that staleness.** Named, not fixed (weekly rebuild is a human item).

## 1 · Universe headline — three numbers

**n = 300 · wflow +0.055 · 🟢 13 / 🔴 87.**
⇒ **the board is 6.7× more red than green while its aggregate flow score is barely positive.**

## 2 · **D161 executed — which axis lit each green** (no green quoted without decomposition)

**All 13 greens satisfy all three axes** — `vol_surge ≥ 1.2` **13/13**, OBV 매집 **13/13**,
RS20 > 0 **13/13**. ⇒ **no green on this board is a single-axis artifact.** That is the clean answer.

⚠⚠ **But the decomposition surfaces the opposite problem, and it is bigger.** Because the tag is a
**conjunction**, `vol_surge` does not inflate the green list — **it censors it.** And `vol_surge` is
the axis whose IC cleared Bonferroni **NEGATIVE** on the KR ledger this morning (h=1 −0.0488,
t(NW) −2.93, n_eff 18) while the US ledger reads it **positive and 구분 불가** (+0.0267, t +1.36,
n_eff 14). **W1 — the KR kill does not transfer. But the censoring is measurable on THIS board:** §3.

## 3 · ★★★ The cross-check that contradicts the MACRO matrix — Energy's zero is a FILTER, not a fact

**MACRO §G wrote ENRG `OW− → OW−−`. The sweep says the money disagrees, and then says why the sweep
itself cannot see it.**

- **Energy carries the board's HIGHEST wflow (+0.360)** — and **0 greens, breadth 0.00.**
- **Diagnosis (the L1 requires absences be diagnosed before they are cited):** of the 16 Energy
  names, **13 carry OBV 매집** and **11 carry RS20 > 0** — but **`vol_surge` is below 1.2 on all 16**
  (max 1.20, on the one name that is 🔴). ⇒ **Energy fails the green gate on the volume axis alone,
  with both other axes passing on the large majority.**
- **This is a verbatim reproduction of the 2026-07-21 precedent** the L1 records (*"an ENRG shortlist
  of 0 turned out to be a 🟢-tag filter artifact — the refiners were OBV-accumulating but tagged
  🟡"*). **Same sector, same mechanism, 15 days later, and nothing was changed in between.**
- ★ **Control, so this is not a story about Energy**: in **Utilities**, the four names with the
  HIGHEST `vol_surge` (1.25–1.32) are **all 🔴분산**. **On this board high volume goes with
  distribution and accumulation goes with quiet volume** — which is the direction the KR IC ledger
  measured, arrived at independently here on US names. ⚠ **n is one board, one day; this
  corroborates, it does not establish (D6 · S1).**

⇒ **ROTATION must not read "ENRG breadth 0.00" as evidence of anything.** The admissible Energy
statement today is: **wflow top-of-board, `delta −0.133` (decelerating), volume absent — and the
accumulation count quoted only WITH its price partner (RULE D6: 13 of 16 OBV 매집 **and** 11 of 16
RS20 > 0 vs SPY; the OBV leg never carries the sentence alone).**

## 4 · The cross-check that CONFIRMS the matrix, and the one that overturns it

| MACRO §G line | Sweep | Verdict |
|---|---|---|
| **UTIL UW** | worst on **both** axes (wflow −0.353 / eqflow −0.349), **10 reds of 15** | ✅ **confirmed, and it is the only sector where price and flow agree without qualification** |
| **MATR UW−** | wflow −0.132 **but `delta +0.138`, the board's 3rd-best acceleration** | ⚠ **partial contradiction** — price is confirming the UW (XLB exc5 −4.76) while flow is improving. **Carried, not resolved.** |
| **IT N+** | `delta +0.158` (2nd-best) but **3 greens of 56, breadth 0.05, 17 reds** | ⚠ **the +4.98% XLK session is NOT in the breadth.** The tape and the flow disagree; **the tape is one session, the flow is 20** |
| **INDU N** | 🚨 **the only sector with `eqflow (+0.156) > wflow (+0.116)` ⇒ breadth-led**, and it holds **5 of the board's 13 greens** and **3 of the 7 new-🟢 ignitions** | ❌ **OVERTURNED. The matrix's `N` understates the one sector where money is broadening rather than concentrating.** |

### ★★★ And the Industrials green cluster has a name the sector label hides (W5)

The five Industrials greens are **ETN · EMR · AME · PWR · TRI**. **Four of the five are electrical
equipment and grid construction** — Eaton, Emerson, Ametek, Quanta. **Three of them (EMR · AME · PWR)
are NEW-🟢 ignitions today.**

⇒ **On the same board, the AI-power buildout's ELECTRICAL-EQUIPMENT leg is igniting while its
UTILITY leg is the worst sector measured.** **That is a single-cycle, two-sub-sector inversion, and
no line of the MACRO matrix contains it** — because the matrix's unit is the GICS label and the
cycle crosses two of them. **This is ROTATION's #1 question and a DEEP candidate.**
⚠ **PWR's RS60 is −13.1 against RS20 +2.4** — an ignition off a hole, not a run (the **D154 /
M149** shape). **The cluster is not uniform and must not be quoted as if it were.**

## 5 · Shortlist — 13 names, and the absences are the finding

`US_LIVE_SHORTLIST.json` holds the rows. **Sectors producing ZERO shortlist names: Energy ·
Utilities · Materials · Consumer Staples · Communication Services.**

- **Energy 0 — FILTER ARTIFACT, diagnosed §3.** Not evidence.
- **Utilities 0 — EVIDENCE.** 10 of 15 are outright 🔴 with OBV 분산; there is nothing to filter out.
- **Materials 0 — MIXED.** NUE (+0.502 OBV 매집, RS20 +17.3) and STLD (+0.312, +12.3) are the
  sector's top two and both fail only on `vol_surge` (0.97 / 0.92) ⇒ **the same censoring as Energy,
  on a smaller sample.** ⚠ **Steel accumulating while the sector's price lags is exactly the
  `delta +0.138` in §4** — the two observations are the same fact seen twice.
- **Staples 0 · Comm 0 — EVIDENCE**, both negative on both axes.

**Short-pressure verdicts (FINRA z, the US substitute for KR's investor actuals — context, not a
trigger):** clean-rise **PLTR (−1.40) · BMY (−2.50) · MET (−1.63)**; crowded-short
**MSFT (+2.44) · FTNT (+2.07)**.

⚠⚠ **Two of this desk's three rejections filed on 2026-08-04 are today's #1 and #5 greens**:
**GRMN** (flow +0.987, the board's best) and **BMY** (+0.956, and the board's *cleanest* short
reading at z −2.50). **Named here, not resolved** — both rows carry `revives_if` conditions with
recheck dates, and firing them one session later on a single day's flow would be exactly the
overreaction the ledger exists to prevent. **Handed to EVENT_ALPHA and to the next HANDOVER's `due`
audit.**

## 6 · D126 — which side of the oscillation this run landed on

**`velocity` is non-null on 0 of 300 rows** ⇒ this run landed on the **0/300** side.
⇒ **`has_conviction` reduces to the 3-axis price/volume unanimity (M25), with no news leg at all**,
which is the condition under which §3's censoring is strongest. **Stated so the series stays
interpretable across runs.**

## 7 · Cycle exposure — 🚨 GAP, and its magnitude is still `unknown`

`CYCLE_EXPOSURE.md/.json` (day-folder root) reports **rank-2 Energy/oil-refining epicenter 2.88% vs
a required 8.0% ⇒ 🚨 GAP, margin −5.12pp**, book touching the cycle only via LNG (adjacent/fuel).
Rank-1 AI-compute is ✅ at 19.85% (AVGO · NVDA · TSM).

⚠⚠ **R39 binds: the Energy registry tag is wrong ("XOM is 0% refining" is retracted), so this GAP's
MAGNITUDE is `unknown` (C3) and may not be quoted as a level.** ★ **What is new and IS quotable is
the direction of travel: the gap widened because the book fully exited XLE on 2026-08-04** — and
**S60**, the bracket registered for that exit, exists precisely because the desk has no ledger that
scores a sale. **Handed to ALPHA's action bracket as a flagged-but-unquantified 🚨.**

---

**Handed to ROTATION:** (1) **INDU is breadth-led and the matrix says N** — overturn or defend;
(2) **the electrical-equipment ↔ utility inversion inside one cycle** — the run's sharpest W5
object; (3) **ENRG's 0 greens is a volume-axis censor, not a flow fact**; (4) **MATR's price and
flow point opposite ways** and two brackets (S36 · S57) already sit on the price side.
