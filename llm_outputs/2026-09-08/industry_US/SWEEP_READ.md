# SWEEP_READ — industry_US · 2026-09-08 (Tue) · Stage 4 / L1·SWEEP

> **The reading, not a second copy of the data.** Sector rows live in `SECTOR_FLOW_US.json
> §sector_rotation`; per-name rows in `US_LIVE_SHORTLIST.json`. Neither is reprinted here.

## 0 · Instrument health line, read BEFORE the numbers

`SECTOR_FLOW_US.json §scoring` = `{vel_axis: false, vel_coverage: 0.1739, n_axes: 3, scored: 299,
dropped_missing_axis: 0}`.

🚨 **The news axis is DEAD this run — 52 of 299 (17.39%) against an 80% bar — and the cause is the
PIPE, not silence.** Probed, not assumed: 8/8 named queries answered **immediately before** the sweep
(NVIDIA 3,886 · Apple 1,295 · Tesla 919 · samsung 411 · SK hynix 244 on `--scope foreign`; the
no-scope continuity re-probes moved vs 09-07: NVIDIA 3,761→**3,892**, Apple 1,282→**1,297**),
**0/4 immediately after it**, and **2/2 again after ~5 minutes of probe-free idleness**. Fifth
consecutive replication. The 52 measured names are **exactly universe ranks 1–52, contiguous, zero
gaps** — a size-selected sample. `dropped_missing_axis = 0` and all 299 scored on the same 3 axes, so
the scale is internally consistent and continuous with 09-07 (`3 / nonews / 299`).

⇒ **No theme-freshness or velocity number in this run comes from the sweep, and no sector or name is
called "quiet" from it.** Absolute for **Utilities · Materials · Real Estate**, which have **zero**
measured names each — for a fifth run.

**And `asof` is 2026-09-04 for the FOURTH consecutive run** (11/11 sectors byte-identical to 09-07 on
11/11 fields). Today that is a **clock** fact, not a market fact: the desk runs pre-open. Δflow is the
**09-03 → 09-04** change and is not read as movement.

## 1 · Universe headline — three numbers

**n = 299 · universe `wflow` mix: 2 sectors positive-on-`eqflow` of 11 · 🟢 11 vs 🔴 92 (8.4 : 1).**

## 2 · Cross-checks against the MACRO matrix — one confirmation, one artifact, one contradiction

**① CONFIRMS Energy `OW`, and it is the only clean confirmation on the board.** Energy is the only
sector with **zero 🔴 names (0 of 16)** while the universe runs 92 red, and it supplies **3 of the
shortlist's 11 names** — the largest single-sector block. Two of the three (`SLB`, `WMB`) carry
`[FINRA]` short-z **−1.21 / −1.16 = low-short/short-cover**, i.e. the rise is not short-driven. The
MACRO matrix reached `OW` from price breadth (15/16 on `exc5`, `exc20` median +11.52); the flow
instrument reaches it from a different direction and agrees. ⚠ Both are computed on the **same
2026-09-04 close**, so this is agreement between two axes, not two dates.

**② The board's three zero-🟢 sectors are a FILTER ARTIFACT and must not be read as evidence — `D561`
reproduces with the same decisive pair as 09-07.**
`Utilities 0/15 · Communication Services 0/12 · Real Estate 0/12` produce no 🟢 and therefore no
shortlist name. Diagnosed rather than cited:

| | `flow_score` | rank | `velocity`? | `vol_surge` | `obv_state` | tag |
|---|--:|--:|:--:|--:|---|---|
| **CEG** (Utilities) | **+0.644** | 124 | **no** | 0.96 | 매집 | **🟡** |
| **PG** (Staples) | **+0.231** | 34 | **YES** | 0.89 | 매집 | **🟢** |

`CEG`'s flow score is **2.8× PG's** and **higher than `RSG` (+0.631), which IS on the shortlist** — and
its `vol_surge` is *higher* than PG's. The only field that separates them is `velocity`, which exists
solely for ranks ≤ 52. **`VST` +0.619, `NEE` +0.353, `WELL` +0.360, `WBD` +0.490, `META` +0.469, `T`
+0.406, `VZ` +0.390 are all 매집 and all 🟡 for the same reason.** ⇒ **ROTATION may not read
"Utilities/RE/COMM produced no shortlist name" as a flow verdict.** This is `D561` on its second
independent run, with the identical pair.

**③ CONTRADICTS the matrix in three buckets, and in each case the flow side is the weaker instrument.**
`TSLA` 🟢 sits in **Consumer Discretionary (UW**, `eqflow` −0.280, `exc20` median −5.27**)**; `RSG` and
`DE` 🟢 sit in **Industrials (UW−**, the board's worst 20-session basket, −5.90 median**)**; `PG` 🟢
sits in **Consumer Staples (UW)**. **All eleven 🟢 names carry `obv_state = 매집`**, and **7 of the 11
have no velocity at all** — so for those seven the 🟢 gate was unlocked by **OBV alone**, which this
desk grades **C** and which `C29` records as carrying a *measured sign conflict* against `vol_surge`.
⇒ **Read as 🟡-with-a-stated-disagreement, per the L2's own instruction.** The matrix's price-and-
breadth reading governs; these are single-name accumulation tells inside falling buckets.

## 3 · Flippers handed to ROTATION (it may not promote/demote on these)

**1 of 11 by the built-in flag** — **Consumer Discretionary / `AMZN` (`top1_w` 40.2%)**, `wflow`
−0.255 → ex-top1 **+0.068**.
**A second, larger one the flag cannot see** — **Communication Services / Alphabet, 76.6% under
`GOOGL`+`GOOG`**; the flag reads `False` because it counts tickers, not issuers. Ex-issuer `wflow`
−0.389 → **+0.272**, swing **0.661** (`D459`, 14th run). ⚠ Both `top1_w` figures rest on a **55-day-old**
cap vector (G5), so where weighted and equal-weighted disagree the **equal-weighted** cut is citable.

## 4 · Shortlist — composition read through its absences

11 names pass `mcap ≥ $10B ∧ 🟢가속`. **Sector coverage: Energy 3 · Industrials 2 · IT / Health Care /
Materials / Cons.Disc / Financials / Staples 1 each · Utilities, Real Estate, Comm. Services 0.**
The three zeros are the artifact of §2②, **not** a flow reading. The composition's own signal is that
**8 of 11 sectors could produce at most one name**, which is what an 8.4:1 red/green universe looks
like.

`[FINRA]` verdicts, which are the part the JSON adds: **✅ clean-rise (low short / covering) — `SLB`,
`HOOD`, `WMB`, `PG`** · **⚡ crowded-short (squeeze fuel, turn-conditional, not a buy) — `RSG` z
+2.61** · the other six 🟡 normal. ⚠ US has **no investor-type feed**; this is a short-pressure proxy
and `HANDOVER §3b′` records that the same class of C-grade axis is currently contested on `MSTR`.

## 5 · Held-but-not-in-universe — invariant PASSES, and the exposure has moved next door

✅ **All 11 US holdings** (ANET AVGO ETN HPE MET MPC NDAQ NUE NVDA PSX RTX) are in `us_top300.csv`
**and** all 11 are scored. **Missing: 0.** The 2026-08-10 `TSM`/`LNG` failure does not reproduce on
held names.

🚨 **But the same defect now bites a LIVE SCENARIO instead of a holding.** `NRG` and `TLN` are
**NOT IN THE UNIVERSE** — and both sit inside **`P127`'s basket, which settles 2026-09-10**. So does
every LNG name (`LNG`, `GLNG`, `FLNG`), which is why MACRO had to register **`P145`** on a
directly-priced basket rather than on any sweep output. ⇒ **`D563` is confirmed on its named cases:
the universe gap is a *scoring* exposure, not only a measurement one.**

## 6 · Cycle exposure — no GAP, and the registry's own hole is the finding

`cycle_exposure` (REAL KIS book, read-only): **AI-compute 17.57% epicenter vs need ≥12.0% ✅** ·
**Energy/oil-refining 10.73% vs ≥8.0% ✅** · Missile-defense 3.64% ⚪ (no threshold set).
**Verdict: no top-rank cycle GAP.** Nothing goes to ALPHA's action bracket from here.

⚠ Two carried caveats, both unchanged:
- **`D416`** — the registry still has **no AI-power row**, so *"the book holds 0% of the power layer"*
  remains **unstatable**. `P123` settles on exactly that layer **today**, and `P127` on 09-10.
- **`C23`, 12th reproduction** — this tool reads total ≈ **₩15,149,158 / $10,978** while
  `module_paper_book status` reads **₩17,791,092** and `exposure_rule` stores **85.2%** invested with
  its current-% **blank**. Four legs, four numbers, none self-identifying.

---

## ✅ EXIT CHECK — SWEEP

- [x] `scoring` block read and quoted (`n_axes` 3 · `vel_coverage` 17.39% · `dropped_missing_axis` 0);
      coverage < 80% ⇒ **"news axis dead this run"** stated, with the cause **probed** (pipe, 8/8 → 0/4
      → 2/2) rather than assumed.
- [x] Every `top1_flips_sign` sector listed with `top1` and `top1_w`, **plus** the issuer-level flip the
      flag cannot see, both handed to ROTATION as no-promote buckets.
- [x] Held-but-not-in-universe check run — **0 missing on holdings**; the live-scenario exposure
      (`NRG`, `TLN`, and the whole gas chain) reported as 🚨 rather than left downstream.
- [x] Sweep completed → `SECTOR_FLOW_US.json`; ranking and 🟢/🔴 counts read.
- [x] `US_LIVE_SHORTLIST.json` written; `[FINRA]` short-pressure verdicts read.
- [x] `CYCLE_EXPOSURE.md/.json` read — no GAP; the registry's AI-power hole (`D416`) carried.
- [x] **No table reprinted from the JSONs** — sector rows and per-name rows are cited by artifact. The
      only table here is the two-row `CEG`/`PG` diagnostic, which exists in no artifact.
- [x] At least one cross-check that confirms (Energy) and one that contradicts (three UW buckets with
      🟢 names) the MACRO matrix, **and every absence diagnosed as artifact vs evidence before use**.
