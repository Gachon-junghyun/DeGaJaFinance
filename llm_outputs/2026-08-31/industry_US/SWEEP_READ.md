# SWEEP_READ — industry_US · 2026-08-31 (Mon) · Stage 4 / L1·SWEEP

> The reading, not a second copy of the data. Sector rows live in
> **`SECTOR_FLOW_US_REPAIRED.json §sector_rotation`**; per-name rows in **`US_LIVE_SHORTLIST.json`**
> and **`…REPAIRED.json §names`**. Nothing below reprints them.

## 0 · 🚨 Instrument health line — read before any number

**The primary `SECTOR_FLOW_US.json` scoring block**: `n_axes` **3** · `vel_coverage` **15.72%** ·
`scored` **0** · `dropped_missing_axis` **299**. **The file is empty and may not be cited** (`G3`).

- **News axis: DEAD this run** (15.72% < 80%), **for the pipe, not for the news** — and that was
  probed, not assumed. `fts` canonical probe **6/6 pre-sweep · 4/4 post-sweep**; direct
  `news_velocity` on **8 names answered 8/8**, including the two lowest-flow names in the entire
  299-name universe (`GWW` 0.69 · `PCAR` 1.12). ⇒ **the ~84% the sweep could not measure are not
  quiet; the sweep's own 300-query burst rate-limits itself.** 🚫 No "sector X is quiet" claim appears
  anywhere in this run.
- **Price axis: DEAD this run too, and independently.** The 08-28 daily bar carries `Close = NaN` for
  **301/301** tickers — **third calendar day, unhealed**. The whole universe scored **0**.
- ✅ **Repaired**: the 08-28 close was recovered from the **5m endpoint** (78/78 bars) and validated at
  **0.0181% mean / 0.0448% max** error (n=24, 0 names above 0.05%). Patch statistics: **300 patched ·
  1 trimmed (`EA`, no 5m data) · 9 names with <78 bars**. Result: **299/299 scored, `n_axes` 3,
  `mode = nonews`** — the same scale as the 08-27 snapshot, so **Δ is legal** and is quoted with its
  label everywhere.
- ★ **Cross-run agreement**: rebuilt today from a fresh cache by a fresh script, the repaired sector
  table matches the 08-30 run's independent reconstruction to **≤0.002 on 11 of 11 sectors**.

## 1 · Universe headline — three numbers

**n = 299** (of 300 requested; `EA` unscoreable) · **cap-weighted flow −0.136** ·
**🟢 4 / 🔴 73**, breadth **1.3%**.

## 2 · Flippers handed to ROTATION — it may NOT promote or demote these buckets on `wflow`

**3 of 11 sectors flip sign when their top-1 name is removed:**

| sector | top-1 | top-1 weight | `wflow` → ex-top1 |
|---|---|---:|---|
| Consumer Discretionary | **AMZN** | **40.2%** | −0.262 → **+0.056** |
| Energy | **XOM** | **30.5%** | −0.097 → **+0.074** |
| Information Technology | **NVDA** | **19.4%** | +0.033 → **−0.016** |

★ **And one `D424` case the flipper guard does not catch.** `D424` (KR-registered today) says
`top1_flips_sign = False` does **not** mean the top-1 owns the sign. **Health Care is that case
here**: it does not flip, yet `wflow` **+0.021** against **ex-`LLY` +0.095** ⇒ **`LLY` is a drag on a
sector that is materially stronger underneath it**, and the guard is silent because the sign never
changed. **Handed to ROTATION as an explicit exception**, not as a clean bucket.
For completeness, the mirror case — a non-flipper whose top-1 is **holding the bucket up** — is
**Real Estate alone** (−0.338 → **−0.415** without `WELL`). Consumer Staples is the `LLY` shape again
in miniature (−0.264 → **−0.130** without `WMT`, i.e. the top-1 drags).

## 3 · Cross-checks against the MACRO matrix — where the money agrees and where it does not

| MACRO §D says | the money says | verdict |
|---|---|---|
| **Energy `N → OW`** on `[news]` escalation + WTI COT at the 43rd %ile | **`wflow` −0.097, `eqflow` +0.005, Δ −0.046, 0 greens in 16** — and the negative is **`XOM` alone** (ex-`XOM` **+0.074**) | 🚨 **CONTRADICTION, and it is the informative one.** The flow axis is asof **08-28**, i.e. **two days before the strikes**. The money has not voted on this event yet. ⇒ ROTATION must treat Energy's flow reading as **pre-event**, not as a refutation |
| **Materials `OW`** | **rank 1 of 11: `wflow` +0.225, Δ +0.197 (largest positive delta on the board), 0 reds in 12, ex-top1 +0.233** | ✅ **CONFIRMS, and broadly** — this is the one bucket where `wflow`, `eqflow`, breadth and Δ all point the same way. ⚠ `C24` unresolved: copper COT sits at the **100th** percentile against it |
| **Health Care `OW`** | `eqflow` **+0.135** > `wflow` **+0.021** | ✅ **CONFIRMS — breadth-led, not mega-cap-narrow.** The gap *is* the confirmation: the sector is stronger where the index weight is not |
| **Comm. Services `OW → OW−`** | `eqflow` **+0.080** > `wflow` **−0.422**; Δ **−0.162 = worst on the board** | ⚖ **SPLIT.** Level says the bucket is fine underneath `GOOGL`+`GOOG` (~85% of cap, both 🔴분산); Δ says it is deteriorating fastest. **The one-notch cut rests on Δ and says so** |
| **IT `N`** | `wflow` **+0.033** but `eqflow` **−0.034**, **13 reds of 56**, **3 greens** | ✅ **CONFIRMS the `N`.** Cap-weight positive, equal-weight negative — the textbook narrow tape. ⚠ Not the worst breadth on the board this run (Industrials is), which is a change from prior runs |
| **Industrials `UW`** | **17 reds of 50 — the largest red count on the board**, Δ **−0.129**, ex-top1 −0.291 with `CAT` only 8.7% | ✅ **CONFIRMS, and it is genuinely broad** — no single name to blame |
| **Cons. Disc. `UW`** | 12 reds of 28, **but `AMZN` owns the sign** | ⚖ **The UW survives on breadth, not on `wflow`** — stated in §D and repeated here so ROTATION cannot pick up the barred axis |
| **Utilities `UW` (strongest)** | **−0.549, worst of eleven, 10 reds of 15, ex-top1 −0.525** | ✅ **CONFIRMS, no flipper problem** |
| **Financials `OW−`** | −0.072 with **Δ +0.073**, **0 greens in 47** | ⚖ **Improving but still empty.** Zero greens in the largest bucket after IT is the fact ROTATION should weigh against the positive Δ |
| **Real Estate `UW`** | −0.338 with **Δ +0.078** and ex-top1 **−0.415** | ✅ CONFIRMS the level; ⚠ the positive Δ off a deep base is recorded, not acted on |
| **Cons. Staples `N`** | −0.264 with **Δ +0.080**; ex-`WMT` **−0.130** (better without it) | ⚖ Consistent with `N`; the sector is less bad than its cap weight implies |

★ **The one sentence ROTATION most needs from this file**: **the flow axis is asof 2026-08-28 and the
run's largest macro event happened on 2026-08-30/31.** Every agreement above is an agreement about a
tape that predates the escalation, and the Energy contradiction is that fact showing itself.

## 4 · Shortlist — and the absences are the finding

**4 names** clear `mcap ≥ $10B` + tag 🟢가속: they are in `US_LIVE_SHORTLIST.json`. Three carry
✅ low-short/short-covering (`shortZ` −0.76 / −0.92 / −1.41); one is △normal.

**What is absent, diagnosed:**

| absence | diagnosis |
|---|---|
| **7 of 11 sectors produce zero shortlist names** (Energy, Financials, Industrials, Utilities, Real Estate, Comm. Services, Cons. Disc.) | **Evidence, not artifact, for 5 of them** — those buckets contain **0 greens** outright. **Artifact for Materials**: it is the board's rank-1 sector and produces **0 shortlist names** because its best names are tagged **🟡중립, not 🟢** (`FCX` +0.767, `NEM` +0.644 are both 🟡). ⇒ **the 🟢-tag filter is again hiding the strongest sector**, exactly the 2026-07 ENRG-refiners failure repeating on a different bucket |
| **Energy: 0 names** on the day Energy was promoted `N → OW` | **Filter + timing, not evidence.** `SLB` reads flow **+0.661** with OBV **+0.318 매집** and `rs20` **+12.6 vs SPY** — comfortably shortlist-grade on the numbers — and is excluded by the 🟢 tag. It also carries the board's **most extreme FINRA short-vol reading (`z +2.40`, 5v5 **+9.0▲**)** and announced a **$3.4bn data-center acquisition today**. **Named here rather than lost to a tag filter** |
| **`news` column is `n/a` for all 4 shortlist names** | Expected — `vel_coverage` 15.72%, the axis is out of the score. **Not read as "no news"** (`G1`) |
| **`CRM`'s +1.000 is at the score cap** | Its print already fired **2026-08-27** ⇒ post-earnings drift, not a pending catalyst. Carried from the 08-30 registry, unchanged |

## 5 · Held-but-not-in-universe — 🚨 the registry, not the book

- **Both books are fully covered this run**: all 11 paper holdings **and** both real-account-only names
  (`CBRE`, `T`) are present in `us_top300.csv` (300 rows). **Missing 0.**
- 🚨 **But the cycle registry's own epicenter names are not**: **`TSM`, `SMCI` and `LNG` are absent
  from the universe** while `cycle_registry.json` lists `TSM`/`SMCI` in the rank-1 AI-compute
  epicenter. ⇒ **the desk cannot flow-tag two of the names its own registry calls the epicenter**
  (`M1103`, reproduced). `LNG` is the long-running case.
- ⚠ **`LITE` and `COHR` ARE in the universe** — so the optical gap (`D250`, **16th run**) is a
  **registry** gap, not a universe gap. That distinction is new and narrows the fix.
- ⚠ `us_top300.csv` is **47 days old** (`G5`) ⇒ 🚫 cap-weight is not "current size" anywhere above.

## 6 · Cycle-exposure GAP → handed to ALPHA

`cycle_exposure.py` (**REAL KIS book**, read-only): **no top-rank GAP.** AI-compute epicenter
**16.91%** vs a 12.0% floor (`NVDA`,`ANET`; `ETN` adjacent) · Energy/refining **10.17%** vs 8.0%
(`MPC`,`PSX`) · Missile-defense 3.82% (no floor set). Invested **$5,188.76 of $11,045.42** ⇒
**53.0% cash**.
- ⚠ **`C23` again**: this verdict is about the **real** book; `PREFLIGHT G5` validated the **paper**
  book. The exposure ledger reads a **third** book at 85.3% invested. **Any ALPHA/BET sizing line must
  name its book.**
- ⚠ **A "no GAP" verdict cannot be produced for a cycle with no registry row** — AI-power/grid
  (`D416`) and optical (`D250`) are **unmeasurable, not zero**.

## ✅ EXIT CHECK
- [x] `scoring` block read and quoted (§0), coverage **15.72% < 80%** ⇒ **"news axis dead this run"**
      stated, and the cause **probed** (8/8 direct answers ⇒ pipe, not silence) rather than assumed.
- [x] Every `top1_flips_sign` sector listed with its top-1 and weight (§2) — **plus** the `D424`
      non-flipping exception the guard misses.
- [x] Held-but-not-in-universe check run (§5): **book 0 missing**, but **registry epicenter names
      `TSM`/`SMCI`/`LNG` missing — reported as 🚨 here, not left for a later stage**.
- [x] Sweep done → primary `SECTOR_FLOW_US.json` (empty, recorded as the honest artifact) +
      `SECTOR_FLOW_US_REPAIRED.json` (299 scored). Sector ranking and Δ read; **new-🟢**: 4 greens,
      none newly ignited vs 08-27 (`CRM`/`A`/`MSTR`/`INTU` were all already green).
- [x] `US_LIVE_SHORTLIST.json` written from the repaired file; short-pressure verdicts read.
- [x] `CYCLE_EXPOSURE` GAP read (§6) — no 🚨 GAP; the book-identity caveat is handed to ALPHA.
- [x] **No table here exists in the JSONs** — sector rows and per-name rows are cited by artifact.
- [x] At least one cross-check that contradicts MACRO: **Energy** (§3), with the contradiction
      diagnosed as an **asof-date** problem rather than a disagreement; and every shortlist absence
      diagnosed as evidence vs filter artifact (§4).
