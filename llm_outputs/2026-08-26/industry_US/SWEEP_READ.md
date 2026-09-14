# SWEEP_READ — industry_US · 2026-08-26 (Stage 2 / L1·SWEEP)

> **The reading, not a second copy of the data.** Numbers live in `SECTOR_FLOW_US.json`,
> `US_LIVE_SHORTLIST.json`, `CYCLE_EXPOSURE.json` and stay on disk all run.
> 🚫 No 11-sector ranking table and no per-name shortlist table is reprinted here — cite the artifact.
> Sweep `asof` = **2026-08-26** ⇒ ⚠ it ran on an **UNSETTLED pre-market bar**, unlike MACRO §E which
> was rebuilt on the **08-25 settled close**. The two frames are one session apart **by construction**
> and that difference is used below, not smoothed over.

---

## 1. Universe headline — three numbers

**n = 299 scored (300 requested) · universe `wflow` −0.160 · 6 🟢 / 71 🔴.**

**Six greens out of 299 is the narrowest board this desk has printed**, and eight of eleven sectors
carry breadth **0.00**. ⚠ See §5 before reading that as information.

---

## 2. 🚨 The instrument's own health line, read FIRST

```
scoring: {vel_axis: false, vel_coverage: 0.1706, n_axes: 3, scored: 299, dropped_missing_axis: 0}
```

### 2a · G2's conditional did NOT fire — Δflow is scale-legal this run
`n_axes` = **3**, identical to 08-20 · 08-21 · 08-22 · 08-23 · 08-24 · 08-25. PREFLIGHT flagged that a
recovery to ≥80% coverage would make `n_axes` = 4 and **retro-illegalise every Δ against the 3-axis
history**. **It did not recover. Subtraction against the recent history is legal**, and the `delta`
column is therefore quotable. ✅ **The check PREFLIGHT demanded was actually run.**

### 2b · 🚨🚨 The six-run "the tunnel drops under burst load" diagnosis is REFUTED, and the real cause is now named

The desk has carried, for six runs and in yesterday's PREFLIGHT verbatim, that the news axis fails
because *"the failure tracks **burst load**, not source silence — the 300-query sweep is the differing
variable."* **That is wrong, and the sweep's own output disproves it in two lines:**

1. **The 51 names that got a velocity reading today are `us_top300` ranks 1–51 — CONTIGUOUS,
   `rk == range(1, 52)`, zero gaps.**
2. **They are the SAME 51 tickers as on 2026-08-25. Overlap 51 of 51. Zero added, zero dropped.**

**A stochastic tunnel drop under burst load cannot produce a contiguous rank prefix, and it cannot
produce the identical set twice.** ⇒ **The news axis is not dying. It is CAPPED** — the sweep queries
the top ~51 names by market cap and stops. `vel_coverage` 17.06% is `51 / 299`, and it will read
17.06% on every run until the cap changes.

★ **Two consequences the desk has never stated:**
- **G1 and G5 are the SAME defect.** *Which* names get a news reading is decided by a **rank prefix of
  a 42-day-old market-cap file.** A name that fell out of the top 51 in those 42 days is silently
  unmeasurable, and a name that rose into it is silently measured.
- **The 08-25 run's own `M856` already recorded the contiguity** (*"ranks 0–50, CONTIGUOUS"*) **while
  its own PREFLIGHT wrote the burst-load diagnosis in the same run.** The two halves of one run
  contradicted each other and nothing reconciled them. ⇒ registered as **`M947`** and **`D366`**.

🚫 **The removed citation right is UNCHANGED** — 17.06% is still far below the 80% bar and no
theme-freshness or news-velocity ranking is admissible this run. **What changes is the diagnosis, not
the permission**, and a wrong diagnosis is what keeps a defect unfixed for six runs.

---

## 3. 🚨 The flipper list changed AGAIN between PREFLIGHT and this stage — 3rd consecutive run — and it TRIPLED

| | PREFLIGHT baseline (08-25 snapshot) | **This run's own sweep (08-26)** |
|---|---|---|
| Flippers | **1 of 11** — Health Care (`LLY`) | **3 of 11** |

**Today's full flipper list, handed to ROTATION** (`SECTOR_FLOW_US.json §sector_rotation[].top1_flips_sign`):

| Sector | `top1` | `top1_w` | `wflow` | `eqflow` |
|---|---|---:|---:|---:|
| **Consumer Discretionary** | `AMZN` | **40.2%** | +0.035 | **−0.270** |
| **Materials** | `LIN` | 24.7% | −0.059 | −0.106 |
| **Energy** | `XOM` | 30.5% | −0.111 | −0.011 |

Eight sectors print `false`: Information Technology (`NVDA` 19.4), Financials (`BRK-B` 13.9),
**Health Care (`LLY` 19.4)**, Industrials (`CAT` 8.7), **Consumer Staples (`WMT` 28.9)**,
Communication Services (`GOOGL` 38.3), Real Estate (`WELL` 16.9), Utilities (`NEE` 17.7).

⇒ **Corrections applied in place, exactly as the 08-25 run did when PREFLIGHT's STPL restriction went stale:**
- 🔴 **LIFTED**: the Health Care weighted-flow restriction. HLTH prints `false` on this run's own snapshot.
- 🟢 **ATTACHED**: **Consumer Discretionary, Materials and Energy may NOT be promoted or demoted on the
  weighted-flow bucket.** They must be ranked on `eqflow` and `breadth`, with the substitution stated inline.
- ⚠ **This matters immediately**: MACRO §E carries **Materials `N+`** and **Energy `OW`**. **Both are
  now flipper buckets.** MACRO ranked both on **price and participation**, not on `wflow`, so **neither
  verdict is invalidated** — but ROTATION must not reach for `wflow` to defend either.
- ⚠ **`D297` continues to be honoured regardless of the flag**: `GOOGL` + `GOOG` ≈ **76.6%** of a
  12-name Comm Svcs bucket while `top1_flips_sign` prints `false` (**a demonstrated false negative,
  `M877`**). **No `wflow` claim is made on COMM at any cut, 8th run.**

★ **Three consecutive runs in which the flipper set moved between the PREFLIGHT baseline and the same
run's own sweep** (STPL → HLTH → {DISC, MATR, ENRG}). **Flipper identity has no run-to-run persistence
and must never be inherited from memory or from yesterday's file.**

---

## 4. Held-but-not-in-universe check — 🚨 the sweep lost a name, and it is the one MACRO already named

- **All 11 held US names were scored.** Coverage leg clean: `ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA
  PSX RTX`, zero outside. **The desk can tag everything it holds.** ✅
- 🚨 **300 requested, 299 scored. The missing name is `EA`** — independently predicted by MACRO
  `M937` an hour earlier (6 price observations in a 90-day frame, last bar 2026-08-10, **$50.69bn,
  Communication Services**). **The sweep's own 299/300 confirms it**, and the sweep emits **no name
  for the drop** — only a count. ⇒ **G5's staleness leg now has a priced, named, doubly-confirmed
  casualty**, and it shrank Comm Svcs from 13 names to 12 in both instruments.
- ⚠ **Every one of the 11 holdings is 🟡중립 and every one carries `vol_surge` < 1.0** (0.45 – 0.93).
  See §5 — on this bar that is a property of the bar, not of the names.

---

## 5. 🚨 `D355`, 2nd run — read this before reading any 🟢, any breadth 0.00, or any "ignition"

The sweep ran at 09:1x ET on a bar carrying **median 2.48% of the prior session's volume**
(mean 3.73%, p90 6.75%, **0 of 299 names above 50%**) — measured this run, worse than 08-25's 3.18%.

⇒ **`vol_surge` is structurally crushed, and `vol_surge` is one of the three axes the 🟢 tag needs.**
- **6 🟢 of 299** and **breadth 0.00 in 8 of 11 sectors** are therefore **not readable as narrowness.**
- **1 `new_green` (`KLAC`, Δ +0.64) — and its own `vol_surge` is 0.56.** 🚫 **An "ignition" flagged on
  a sub-1.0 surge on a 2.48%-volume bar is not an ignition; it is unreadable.** The 08-25 run found
  **100%** of its `new_green` list to be artifacts; this run declines to read its single one at all.
- ✅ **One thing IS better than 08-25**: **zero of today's 6 greens are velocity-derived** (all carry
  `velocity: None`), against 4 of 8 withdrawn yesterday. Today's greens rest on OBV ∧ RS20 ∧ surge.
- ⚠ **But three of the six have `vol_surge` < 1.0** (`MRVL` 0.60 · `KLAC` 0.56 · `ORCL` 0.41) and a
  fourth is at 1.18 (`MRK`). **Only `COIN` (1.56) and `MSTR` (1.49) clear a 1.2 surge bar.**

---

## 6. Cross-checks against the MACRO transmission matrix — where money and price DISAGREE

> This is the file's reason to exist and ROTATION's direct input. `eqflow` is the citable weighting
> (G5); `wflow` is stamped 42-day-old caps wherever it appears.

### 🔴 CONTRADICTION 1 — **Information Technology. The flow instrument does not support the underweight.**
MACRO holds **`IT = UW`** on price breadth (36/56 negative `exc5`, settled 08-25).
The sweep says **`eqflow −0.009` = 3rd best of 11**, and **4 of the board's 6 greens are IT names**
(`MSTR`, `MRVL`, `ORCL`, `KLAC`), with the sector's most greens and only 6 reds of 56.
⇒ **Price says worst-but-two; money says third-best.** **This is `C16` in its purest form** and it is
now pointed at the desk's single largest sector call. **Which side is the money on: the flow side.**
🚫 Neither instrument is graded highly enough to overrule the other, so **the contradiction is carried
to ROTATION, not resolved here** — and ROTATION must state which one it ranked on.

### 🔴 CONTRADICTION 2 — **Energy. The crack broke and the refiners' OBV is still accumulating.**
MACRO has Energy at the board's **worst `exc1` (−1.991)** and **worst `exc5` (−2.763, 14/16 negative)**,
with the registered crack kill FIRED on settled bars.
The sweep has Energy at **`eqflow −0.011` = 4th best of 11**, and **`MPC` and `PSX` both read OBV
`매집`** with `rs20` +10.4/+9.9 and **`rs60` +36.8/+30.9**.
⇒ **The commodity broke on 08-25; the equity accumulation signal has not yet turned.** ⚠ **`D6`: OBV
is a C-grade axis** and this is precisely the case it is weakest in (a two-session price break has not
had time to enter a 20-day OBV slope). **Stated as a disagreement with a known lag, not as support.**
★ This is exactly what **`P100`** was registered to settle.

### 🟢 CONFIRMATION 1 — **Consumer Staples: money confirms the demotion, independently of price.**
MACRO demoted **`STPL N+ → N`** on price (board's worst `exc1 −1.233`, 17/19 negative on twenty).
The sweep, independently: **`eqflow −0.404` = 10th of 11**, **0 🟢 / 8 🔴 of 19**, breadth 0.00.
⇒ **Both instruments agree, from different data.** ✅ And **the G3 restriction that blocked exactly
this demotion on 08-25 is gone on both snapshots** — `WMT` prints `false` today.

### 🟢 CONFIRMATION 2 — **Utilities and Real Estate: the two families agree at the bottom, as `C16` predicts.**
Sweep: `UTIL eqflow −0.564` (worst of 11, 0🟢/10🔴 of 15) · `RE −0.430` (2nd worst, 0🟢/3🔴).
MACRO: `UTIL exc20 −7.923` (worst, 14/15 negative) · `RE exc20 −4.608`.
⇒ **`C16`'s registered shape — *"the two lists agree only at the BOTTOM and invert at the TOP"* —
replicates on a third consecutive frame.** That is the contradiction's most stable property.

### 🟢 CONFIRMATION 3 — **Industrials.**
Sweep: `eqflow −0.229` (8th) with **12 reds — the most on the board** and **0 greens of 50**.
MACRO: negative on all three windows, 40/50 negative on twenty, tariffs effective 09-08.
⇒ **Agreement. The `UW−` is the run's best-supported sector verdict on both instruments.**

### ⚠ HALF-CONTRADICTION — **Materials.**
MACRO ranks it **best on `exc5` (+3.740)** and explicitly calls it *a two-name bet wearing a sector
label* (`FCX` +20.69, `NEM` +16.72; the other ten `exc20` median **−8.211**).
Sweep: **`eqflow −0.106`, 0 🟢 / 1 🔴 of 12, breadth 0.00**, and it is now a **flipper** (`LIN` 24.7%).
⇒ **The sweep does not contradict MACRO's number — it corroborates MACRO's *reading*.** A sector with
the board's best price excess and **zero** greens is not a sector move. **`P102` brackets it.**

---

## 7. Shortlist composition — the ABSENCES, each diagnosed

**6 names survive the filter** (`mcap ≥ $10B` ∧ 🟢가속, top-15 by flow) — `US_LIVE_SHORTLIST.json`.
Sector composition: **Information Technology 4 · Financials 1 · Health Care 1.**
**Zero names from Energy, Industrials, Materials, Utilities, Real Estate, Comm Svcs, Cons Disc, Cons Staples.**

**Diagnosis of the absences — filter artifact vs evidence, one by one:**

| Absence | Verdict | Why |
|---|---|---|
| **Energy (0 of 16)** | 🚫 **FILTER ARTIFACT — do not cite** | This is the **verbatim 2026-07-21 precedent the protocol names**: `MPC` (flow **+0.572**, OBV **매집**, `rs20 +10.4`, `rs60 +36.8`) and `PSX` (**+0.505**, 매집, +9.9, +30.9) are the **1st and 2nd highest flow scores among all 11 holdings** and are tagged **🟡 only**. Their `vol_surge` is **0.83 / 0.75 on a 2.48%-volume bar** (`D355`). **The absence is the surge axis, not the money** |
| **Industrials (0 of 50)** | ✅ **EVIDENCE** | 12 reds — the board's most — plus `eqflow −0.229`, and MACRO negative on all three windows. **Three instruments agree.** The one holding, `ETN`, carries OBV 매집 and flow +0.439 but `vol_surge` 0.59 |
| **Utilities (0 of 15) · Real Estate (0 of 12)** | ✅ **EVIDENCE** | Worst and 2nd-worst `eqflow`, 10 and 3 reds, and the worst two `exc20` in MACRO. **Nothing to diagnose away** |
| **Consumer Staples (0 of 19)** | ✅ **EVIDENCE** | 8 reds, `eqflow` 10th of 11, and MACRO's worst single session. **Confirms the demotion** |
| **Materials (0 of 12)** | ⚠ **BOTH** | Genuine (breadth 0.00, `eqflow` negative) **and** artifact-adjacent — `FCX`/`NEM` are the board's two strongest 20-day names on price and neither is 🟢. **This is the sharpest single instance of `C16` on the board** |
| **Comm Svcs (0 of 12) · Cons Disc (0 of 28)** | ⚠ **UNDER-DETERMINED** | Both are **flipper or effective-flipper buckets** (`AMZN` 40.2% flips; `GOOGL`+`GOOG` 76.6% with a false-negative flag). **A breadth-0.00 reading on a bucket whose sign belongs to one name is not a sector statement.** Reported as unreadable |

★ **The composition itself is the finding**: **4 of 6 shortlist names are Information Technology** —
the sector MACRO put at `UW`. **`MRVL` (flow +0.44, `rs20 +41.7` = the board's best, ✅ low-short /
short-cover, `shortZ −1.11`) prints TOMORROW, 08-27, and is the object of `S116`.**

---

## 8. Cycle-exposure GAP — ✅ downgraded to ⚠ UNDER-DETERMINED (`D250`, 12th run)

`cycle_exposure --json` reports **no GAP**: AI-compute epicenter **16.69%** (need ≥12.0) via `NVDA`,
`ANET`; Energy/refining **9.7%** (need ≥8.0) via `MPC`, `PSX`; missile-defense 3.83% (`RTX`, no
threshold set). Book total ≈ **$11,022**, invested **$5,135**.

🚨 **The ✅ is not trustworthy and the reason is 12 runs old**: `cycle_registry.json` still has **no
optical / interconnect row** (`D250`/`M731`), on a run where `COHR` and `LITE` were the **largest
single contributors** to `P79` entering branch B. **An epicenter percentage computed against a
registry that omits a live chain layer cannot say "no gap."** ⇒ **⚠ UNDER-DETERMINED, handed to
ALPHA's action bracket as an open flag rather than a clean pass.**

---

## 9. What this stage hands ROTATION

1. **Flipper restrictions**: **Cons Disc · Materials · Energy** may not be promoted/demoted on
   weighted flow. **Health Care's restriction is LIFTED.** COMM is treated as a flipper regardless of
   its flag (`D297`, 8th run).
2. **`C16` is live and pointed at the largest call on the board**: `IT` is 3rd-best on `eqflow` with
   4 of 6 greens, and worst-but-two on price breadth. **ROTATION must state which instrument it ranked
   on, inline.**
3. **Three sector verdicts are confirmed by both instruments** — `INDU UW−`, `UTIL UW−`, `STPL N`.
4. **Energy's disagreement is dated and bracketed** (`P100`, settle 09-01): commodity broken, OBV
   still 매집, `exc20` +4.428.
5. 🚫 **Nothing in this run may be promoted on a `new_green`, a breadth-0.00 reading, or a `vol_surge`
   comparison** — the bar is 2.48% of a normal session (`D355`).
6. **New instrument findings for `RESEARCH.md`**: **`M947`** (the velocity set is a contiguous,
   run-invariant rank prefix ⇒ a cap, not a drop) and **`D366`** (its remedy).

## ✅ EXIT CHECK
- [x] `scoring` block read and quoted; coverage **17.06% < 80% ⇒ "news axis dead this run"** stated,
      and the cause **probed and re-diagnosed** (contiguous rank prefix, identical set two runs
      running ⇒ **a cap, not a pipe drop**) rather than assumed.
- [x] **Every `top1_flips_sign` sector listed with `top1` and `top1_w`** (3 named, 8 explicitly false)
      and handed to ROTATION with the restriction stated.
- [x] Held-but-not-in-universe check run: **0 of 11 holdings outside**; the one unscored name (`EA`)
      is named and cross-confirmed against MACRO `M937`.
- [x] Sweep completed → `SECTOR_FLOW_US.json`; sector ranking and `new_green` read (and the single
      `new_green` **declined** as unreadable, with the reason).
- [x] `US_LIVE_SHORTLIST.json` written; FINRA short-pressure verdicts read.
- [x] `CYCLE_EXPOSURE` GAP read; the ✅ **downgraded to ⚠ UNDER-DETERMINED** and handed to ALPHA.
- [x] **No table that exists in the JSONs is reprinted** — the flipper table is a 3-row exception
      because the protocol *requires* that specific list be written out in full.
- [x] Cross-checks stated in both directions: **3 contradictions, 3 confirmations, 1 half**, each
      naming which side the money is on.
- [x] **Shortlist absences diagnosed one by one** — 4 evidence, 1 filter artifact (Energy, with the
      2026-07-21 precedent named), 1 both, 2 under-determined.
