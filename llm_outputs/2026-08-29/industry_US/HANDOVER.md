# HANDOVER — industry_US · 2026-08-29 (Stage 2 / L1·HANDOVER)

> Run fires **2026-08-29 22:1x KST = Sat 09:1x ET**. **US markets are closed and the 2026-08-28
> session is fully settled.** That is the opposite of the last three US runs, which fired pre-market
> and had to defer every row keyed on the same day's close. **Rows keyed on the 08-28 US close are
> due today; rows keyed on a `[FRED]` bar covering 08-28 are mostly NOT** (§2f).
> P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.

---

## 0 · Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-08-29/industry_US/preflight/PREFLIGHT.md` **was run** (Stage −1, this run).
**4 FAIL / 3 PASS.** The rights it removes bind every stage after this one:

| Gate | Verdict | What this run may NOT do |
|---|---|---|
| G1 news axis (`vel_coverage` **16.72%**, 50/299; probes alive: NVDA 5353 / LLY 191 / NUE 23 / MPC 19) | **FAIL** | No news-velocity or theme-freshness citation, anywhere. No "quiet"/"no news" verdict on any name or sector. `BET_SHEET §B` freshness tags read `UNMEASURED (G1 FAIL)`. **And the partial velocity subset may not be used cross-sectionally** — coverage is `us_top300` **ranks 1–50, contiguous** ⇒ a mega-cap-only sample |
| G2 scale continuity (`n_axes`=3 on 10 snapshots 08-19→08-28) | **PASS** | conditional: SWEEP re-reads `§scoring.n_axes` **and `§asof`** before any Δflow subtraction. 🚨 **This PASS is materially qualified by §11a of this file — the qualification is appended, not substituted** |
| G3 sector-sign ownership (flippers **2 of 11**: Info Tech/`NVDA`, Health Care/`LLY`) | **PASS** | **IT and HLTH may not be promoted or demoted on `wflow`** (ROTATION §2). Rank them on `eqflow`/`breadth`, say so inline. 🚨 **And see §1d — `R108`, filed this morning, attacks the flipper instrument itself** |
| G4 risk-unit stability (250d **11** / 500d **10** / 750d **10**; groupings differ) | **FAIL** | No bare concentration number. Every unit count carries its `--days` on the same line |
| G5 universe covers holdings (11/11 covered; file **45 days** old) | **FAIL** (staleness leg) | `wflow` is not a **current** weighting. Prefer `eqflow` on disagreement; tag `wflow` with its 45-day age wherever used |
| G6 accrual rate (19 files / 38 days = **0.50/day**, 2.0× slow; **no file accrued for 08-29**) | **FAIL** | No IC-backed sizing language. Any fraction is "mechanical 1/4 — IC not yet estimable" |
| G7 tool liveness (26 exit-0; `module_chart` verified live by real invocation) | **PASS** | ⚠ but `module_chart NVDA --read` returned exit 0 with **`nan` in 3 of 5 fields** — read the field, do not infer a number from a zero exit code |

★ **The gate that mattered most today is not in the table.** PREFLIGHT measured the *snapshot's*
health and passed its `asof` field as clean. **§11a of this file refutes that reading with a
measurement PREFLIGHT did not take.** The refutation is written down, not edited back into Stage −1.

---

## 1 · Inherited standing view — and **two process failures to name first**

### 1a 🚨 The US analytical carry has now missed **two consecutive writebacks** — `D394`, escalated

Measured, not inferred:
- `handoff/STANDING_VIEW_US.md` mtime **2026-08-26 23:31**. `grep "2026-08-27"` → **0 hits**;
  `grep "2026-08-28"` → 2 hits, both **forward references written on 08-26** ("re-derive at the
  08-28/08-31 run"), not writeback rows.
- ⇒ **The newest US per-name carry this run inherits is `asof` 2026-08-26 = 3 days old**, not 1.
  `D394` was registered by the 08-28 run *because this had already happened once*. **It happened
  again in the same run that registered it.**

### 1b 🚨🚨 Worse, and new: **the 08-28 run scored five rows and none of them reached the ledger**

`llm_outputs/2026-08-28/industry_US/HANDOVER.md §2a–§2e` contains full, sourced verdicts for
**`S79` (A / U-MIXED) · `S81` (C, AMBIGUOUS) · `P83` (FIRED-B) · `P96` (FIRED-B) · `S119` (FIRED-C)**.
`handoff/SCENARIOS.md` contains **none of them**. Its last US scoring block is dated **08-27**; the
only 08-28 block in the file is the **KR** desk's (`S115`·`P90`·`S117`·`P77`, all correctly landed).
The 08-28 US run produced `HANDOVER.md`, `MACRO_REPORT.md`, `SECTOR_FLOW_US.json`,
`SECTOR_ROTATION.md`, `SWEEP_READ.md`, `EVENT_ALPHA.md` — and **no `BLINDSPOT_PREMORTEM.md`, no
`SECTOR_DEEP_*`, no `BET_SHEET.md`**. ⇒ **the run terminated between ROTATION and PREMORTEM, and its
writeback pass never executed.**

⇒ **`D400` registered** (§8): *a scoring verdict that exists only in a run directory is not scored.*
**This run's §2 lands all five** rather than re-deriving them (§2a).
⚠ One thing the 08-28 run got **right** and I checked before assuming otherwise: its claim that
`P77`·`P90`·`S115`·`S117` were already settled by the KR desk **is true** — that block is in the
log under a `# ═══` heading, which a `^##` grep misses. Verified before writing, not after.

### 1c Regime call (shared spine §1, carried unchanged)

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]` — the equity tracks the **second derivative** of price, not the level, which is why
> "shortage persists" and "stocks struggle" are both true.

⚠ Carried with its tag intact. **`[inferred]` — it may not be cited as evidence** for any new
proposition this run. It frames; it does not prove.

### 1d Retracted ledger (§5) — read BEFORE forming today's view. **Three entries bind, one of them filed today**

- 🚨 **`R108` — filed 2026-08-29 ~11:00 KST by `industry_kr`, i.e. eleven hours before this run's
  PREFLIGHT, and PREFLIGHT did not read it.** It retracts *"the `rs20` bench-misalignment bias is a
  constant offset, therefore CROSS-SECTIONAL RANK survives and may be cited"* — a claim that was
  **written into PREFLIGHT's G0 exemption and used by ROTATION to cite sector ranks and flipper lists
  for roughly ten runs.** Killed by a controlled rebuild holding session, universe, axes and formulas
  constant and moving **only** the bench bar: **19 of 28 sectors change rank, universe `wflow`
  +0.333 → +0.172, greens 67 → 44, and the flipper set changes membership 5 → 3** (`M1029`).
  - **The mechanism is in shared scoring code, not in a KR market fact**: `flow_score` applies
    `clip(rs20 / 8.0)`, so a constant offset **in pp** is **not** constant **in score space** — names
    already at the ±1 cap lose nothing, names inside the band lose the full amount. I confirmed the
    line exists in the US path too: `scripts/sector_flow.py:173` is `clip(rs20 / 8.0)`, one shared
    function for both markets.
  - **`W1` applies to the conclusion, not to the code.** The *measured magnitudes* (19/28, 67→44) are
    KR and are **not** transferred. What transfers is that **a saturating transform converts a uniform
    input bias into a non-uniform output bias** — which is arithmetic, and which this desk's own
    file executes.
  - 🚫 **Right removed by inheritance, on top of PREFLIGHT's**: G3's flipper list may be used to
    **withhold** a promotion (its conservative direction) but **may not be cited as evidence that the
    nine non-flippers are clean.** `R108`'s specimen is precisely a case where the flipper rule
    **blocked a demotion the aligned data permitted** — the guard fired on the wrong bucket.
- **`R103`** — *"the news axis fails because the 300-query SWEEP overloads the tunnel"* → RETRACTED
  2026-08-26 by `M947`. PREFLIGHT reproduced the rank prefix a **5th** time today and wrote it up as a
  **reproduction, not a discovery** — ✅ `D379`'s *first* failure mode did not recur. **Its second did**
  (§11b). ⚠ And the mechanism has since been narrowed further by `M1027`: a bare client with no sweep
  running is cut at a contiguous prefix of **11**, not ~102, recovering in ~93s ⇒ **the fixed-quota arm
  is dead; a rate-dependent sticky ban survives.**
- **`R89`** — *"the refiners pay WITHOUT the barrel"* → RETRACTED 2026-08-21. Its registered successor
  instrument `P83` **also failed** (§2a) ⇒ **the desk has no surviving instrument that separates the
  refining excess from the barrel, and this run may not re-assert separation on any instrument.**
- **`R106`** (July PCE printed 08-26, not 08-28) and **`R107`** (a rate event's pre-pricing cannot be
  read from a close-to-close difference) carried; **`R109`** (KIS `--investor` 10-row cap is a display
  limit) is KR-instrument and does not bind this desk.

### 1e Open contradictions (§6) — carried, **not** resolved

- **`C22` — registered this morning by `industry_kr`, carried here unresolved**: the desk's two
  ledgers name different hands (`kr_live_shortlist` tags real-hands on `foreign OR institution`;
  `reject_ledger` revival conditions are written `foreign AND retail-negative`) and returned opposite
  verdicts on the same name in the same run. **Its US-side instance is the one that binds me**: the
  `missed_ledger` row for `HII` requires *"`HII` enters the universe via `build_us_universe.py
  --include`"* — **a condition that observes our own builder, not the market, and therefore cannot
  fire on its own.** ⚠ And G5 measures that builder's output at **45 days old**. Carried; which hand
  a revival condition should name is a human call.
- **`C21`** (RSI convention, US 08-27) carried untouched — this run has not yet invoked
  `us_setup_screener`.
- **`D9`** (measured-unit vs book-label mismatch: block or warn?) and **`MAX_THEME_PCT` counting as 2
  what residual correlation measures as 1** — reproduced in **all three** G4 windows today. Carried.

### 1f Per-name carry, `asof` 2026-08-26 (⚠ **3 days**, see §1a) — tags preserved

| Name | Carried state | Tag | Stale? |
|---|---|---|---|
| `MPC`·`PSX`·`VLO` | Refining **margin, not crude beta**: `exc20` +12.57/+11.70/+10.51, `exc60` +41.41/+33.45/+37.80, all OBV 매집, the three smallest negative flow deltas in a sector where E&P ran −0.52…−0.57 (`M952`) | `[measured]` | ⚠ 3d — **and its separation instrument is dead** (§1d `R89`/`P83`) |
| `XOM` (ENRG top1) | The sweep's only Energy red; flow −0.590, OBV 분산, Δ −0.424. In `reject_ledger` (`K.본문반증`), recheck 09-09 | `[measured]` | ⚠ 3d. ✅ **No longer a G3 flipper** — the 08-28 restriction on ENRG is lifted |
| `NVDA` (held) | The epicenter; printed 08-26 AMC, +8.738% on 08-27 | `[measured]` | ⚠ 3d — **and §2b measures the give-back: −4.57% on 08-28** |
| `AVGO` (held) | Worst `rs60` on the book (−24.1), `exc5` −5.920 = 9.9th %ile, FINRA **z −2.17 / 5v5 −10.4▼**. Prints **2026-09-02**; `S127` armed (settle 09-08) | `[measured]` | ⚠ 3d. **D-4. `D295` re-derivation still unmet, 4th run** |
| `ANET` (held) | OBV 매집, `rs20 +17.4 / rs60 +12.3` against FINRA z +2.06 = board's highest short pressure. Two-sided, no stamp | `[measured]` | ⚠ 3d |
| `MRVL` | The only confirmed-early hand-off whose **denominator is rising** (+13.2% NY) | `[measured]` | ✅ **superseded by §2b — `S116` settled and the print is in the tape** |
| `COIN` | Board's #1 flow (+0.978) on the board's **worst revision book** (CY +1.01 → −2.06 = −303.5%). **Carried ONLY with its denominator attached** | `[measured]` | ⚠ 3d |
| `HOOD` | The clean version of the same node: `exc5/20/60` +22.66/+17.46/+17.62, positive revisions on all four | `[measured]` | ⚠ 3d |
| `MSTR` | Not a runner, not cheap — 2.52× forward off a −115.3% CY consensus. Rejected (`H.밸류소진`), recheck 09-16 | `[measured]` | ⚠ 3d |
| `MRK` | Health Care's only 🟢 — **and it trades ABOVE its mean target** (upside −4.4%) ⇒ `L2` on the sector's only green | `[measured]` | ⚠ 3d. **HLTH is a G3 flipper again today** |
| `MET`·`NDAQ` (held) | Both in `S128`'s **decay** basket (`rs20<0 ∧ rs60>0`); `S128` settles 09-09 | `[measured]` | ⚠ 3d |
| `RTX` (held) | 🔴분산, `delta −0.629` = book's largest negative. Its cycle has **no threshold set**; `W4` unpaid **210 days** | `[measured]` | ⚠ 3d |
| `NUE` (held) | Two instruments, neither a turn: screener "leader pullback" at +22% over 200DMA vs `module_chart` NEUTRAL/CHOP, OBV 분배 −65%, RSI 22.4 | `[measured]` | ⚠ 3d |
| `EQIX`·`DLR`·`IRM` | The carried data-centre grouping is **not observed** (`M953`). ⚠ n=1 frame | `[measured]` | ⚠ 3d |
| optical (`LITE`·`COHR`) | 🚨 `cycle_registry.json` still has **no optical row, 13th run** (`D250`) ⇒ exposure **unmeasurable, not zero** | `[measured]` | ⚠ 3d |
| `MU` | Carried as *"does not print until **09-24**"* — used as the base-rate for `S118`'s anti-signal | `[measured]` | 🔴 **CORRECTED this run**: `Micron Technology to Report Fiscal Fourth Quarter Results on **September 30, 2026**` (`yahoo_finance` 08-26). **The carried date was 6 days early.** `M1044` |

---

## 2 · Scenarios settled this run

> Scored **only** against the pre-registered observable and threshold (`D242`). No band re-derived,
> no threshold improvised. ★ `D393-KR` applied first: `SCENARIOS.md`'s master log tail was read
> **before** anything was written here — which is how §1b was found and how the 08-28 run's claim
> about `P77`/`P90` was **confirmed correct** rather than assumed wrong.

### 2a · RECOVERY — the 08-28 run's five verdicts, **reproduced from source and landed**

I did not re-score these. I **re-derived the arithmetic independently and checked it against the
08-28 run's printed values**, because a second scoring of a frozen observable that returns a
different number is the "same fact, two values" failure this repo's evidence rule exists to stop.

| id | 08-28 verdict | my independent reproduction | match |
|---|---|---|---|
| **`S79` L1** | `FIRED-A`, NVDA excess **+8.083pp** | NVDA 209.66→227.98 **+8.7381%**, SPY 766.08→771.10 **+0.6553%** ⇒ **+8.0828pp** | ✅ exact |
| **`S79` L2** | `U-MIXED`; AVGO +3.830pp, TSM +1.645pp | AVGO 355.59→371.54 **+4.4854%** ⇒ **+3.8301pp**; TSM 417.69→427.30 **+2.3007%** ⇒ **+1.6454pp** | ✅ exact |
| **`S81`** | `C` (AMBIGUOUS by its own anti-signal), excess **+3.082pp** | AVGO +4.1487 · ANET +5.3157 · HPE +1.8151 ⇒ EW **+3.7598%**; SPY +0.6776% ⇒ **+3.0822pp** | ✅ exact |
| **`P83`** | `FIRED-B`, change **−13.562** | (4.4803−3.2629)×42 = **51.1308** (08-20) → (4.2787−3.3842)×42 = **37.5690** (08-27) ⇒ **−13.5618** | ✅ exact |
| **`P96`** | `FIRED-B`, 3-2-1 crack 5-session change **+4.874** | 08-20 **66.2554** → 08-27 **71.1294** ⇒ **+4.8740** | ✅ exact |
| **`S119`** | `FIRED-C`, invariant across 3 enumerations | XLE −1.299% · RSPG −0.363% · SPY +0.999% ⇒ **−2.299pp / −1.363pp**, both inside ±2.60 | ✅ exact |

⇒ **All six legs reproduce to four decimals. The verdicts are landed as the 08-28 run wrote them,
with attribution to that run**, not re-attributed to today. The recovery is the fix for §1b; it is
**not** a re-scoring, and no threshold was touched.
★ **What `S79` L2 established stands and is inherited**: on the one observable day, **neither the
250d split nor the 500/750d merge described the tape** ⇒ G4's cross-window disagreement is not
resolved by observation either. The desk has **no validated grouping for event risk**.
★ **What `P83` established stands**: `R89`'s successor separator collapsed 13.6 points in five
sessions. **Separation may not be re-asserted this run on any instrument.**

### 2b · `S116` — `MRVL` 08-27 print · **`FIRED-C`**, and the branch is invariant across a broken instrument

Frozen: **`MRVL` − `AVGO` 1-session excess** on the first settled close after the print (**08-28**),
each vs its own 08-27 close. A ≥ +12.0pp · B ≤ −12.0pp · C between.

🚨 **The price instrument is defective for the 2026-08-28 session and I did not pick a value — I
tested whether the branch depends on the pick** (`C5`, the `S119` precedent):

| reading | MRVL | AVGO | spread | branch | distance to B |
|---|---|---|---|---|---|
| `fast_info.last_price` (corroborated, see §2e) | **−10.2837%** | **−0.7402%** | **−9.5435pp** | **C** | 2.456pp |
| `repair=True` (synthetic, disclosed) | −10.3748% | −0.6513% | −9.7235pp | **C** | 2.276pp |

⇒ **`FIRED-C` on both readings. Invariant.**
- **Anti-signal probed, NOT fired**: *"an announced acquisition of, or by, either company inside
  08-24 → 08-28."* `Marvell` returns **482** foreign hits over 7d and **380** over 4d — the pipe is
  loud on this name — and the window's content is *"Marvell Leads AI Stocks Lower After Earnings That
  Narrowly Topped Estimates"* and *"Marvell forecasts $18B fiscal 2028 revenue, driven by data center
  growth of more than 60%"* (`seekingalpha` 08-27). **No corporate action.** ⚠ Absence argued from a
  **loud** query, not from a zero-hit one (`D94`).
- ⚠ **Margin disclosed, and it is the interesting part**: the row's B prose reads *"the share shift was
  over-priced; `AVGO`'s −14.7 rs60 was a discount, not a franchise loss."* The realised spread is
  **−9.54pp, i.e. 79% of the way to B** on a beat-and-raise print. **C is the verdict; the direction
  is not neutral, and saying so is not the same as moving the line.** `M1039`.

### 2c · `S118` — is `NVDA`'s print about the PRINTER or about MEMORY? · **`FIRED-C`**

Frozen: **`EW{MU,SNDK,WDC}` 2-session excess vs `NVDA`**, 08-26 close → 08-28 close.
A ≥ +6.50pp · B ≤ −6.50pp · C between.

| reading | MU | SNDK | WDC | EW | NVDA | spread | branch | distance to B |
|---|---|---|---|---|---|---|---|---|
| `fast_info.last_price` | −0.5904% | −0.9597% | −2.0112% | **−1.1871%** | **+3.7632%** | **−4.9503pp** | **C** | 1.550pp |
| `repair=True` (synthetic) | −0.7976% | −1.0635% | −1.8191% | −1.2267% | +3.9254% | −5.1521pp | **C** | 1.348pp |

⇒ **`FIRED-C` on both readings. Invariant.**
- **Anti-signal probed, and the near-miss is disclosed rather than buried.** The condition is *"a
  memory-maker pre-announcement **or guidance revision** with a named date inside 08-24 → 08-28."*
  The window contains ***"Micron Technology to Report Fiscal Fourth Quarter Results on September 30,
  2026"*** (`yahoo_finance` 08-26) — **an announcement carrying a named date**, but it is an
  earnings-*calendar* notice, **neither a pre-announcement nor a guidance revision**. ⇒ **NOT fired**,
  on the row's own words. Also in-window and also not qualifying: *"Micron Announces Leadership
  Appointments"* (08-26). **Recorded with its sources so a later run can overturn this on evidence
  rather than re-litigate it.**
- ★ **And that same item corrects a carried fact the row leaned on**: the registration's base-rate
  argument was *"`MU` does not print until **09-24**."* It prints **09-30**. The base rate was
  argued from a wrong date and **happens to be safer than claimed**, not less safe. `M1044`.
- ⚠ **The spread is 76% of the way to B**, i.e. toward *"the print is about NVDA."* Both this row and
  `S116` land in C leaning the same way — **and they are not independent**, since `NVDA`'s +3.76%
  two-session move is inside both. **Named here so no downstream stage counts them twice** (`D343`).

### 2d · The 08-28 session read across `S79` → `S116`/`S118` — one number, stated once

`NVDA` **227.98 (08-27) → 217.55 (08-28) = −4.575%**. `S79` measured the +8.08pp print reaction on
08-27; today's two rows measure the session after it. **These are one price path read at two points,
not two independent confirmations** (`D343`). No stage may cite them as separate evidence.

### 2e · 🚨 `M1040` — the price instrument returned **three different values for one settled close**, and one route is corroborated

This is the run's largest instrument finding and it was found by trying to score `S116`.

**Measured, all on 2026-08-29 ~22:2x KST, one provider (`yfinance`), three surfaces:**

| surface | NVDA 08-28 | SPY 08-28 | MRVL 08-28 |
|---|---|---|---|
| `yf.download(...)` daily bar | **NaN** | **NaN** | **NaN** |
| `yf.download(..., repair=True)` | 217.89 (`Repaired? True`) | 769.35 | 216.40 |
| `Ticker.fast_info['last_price']` | **217.55** | **769.35** | **216.62** |

- **The 08-28 row is present with Volume and with Open/High/Low — only `Close` is NaN.** NVDA 08-28:
  O **227.33** / H **229.26** / L **216.81** / C **NaN** / V **194,036,188**. The session happened.
- **This is the same defect the KR desk measured this morning on its own universe** (`M1026`: a
  phantom 08-28 bar for **831 of 833** KR names). ⚠ **It is not a transfer — I measured it on US
  names myself** — and the **signature differs**: KR lost all of OHLC, **US lost Close only**. `M1041`.
- ★ **The tie is broken by measurement, not by preference.** The KR run, running eleven hours earlier
  through a different path, quoted `NVDA` 08-28 = **217.55** and `SPY` = **769.35**, and published a
  four-session `S103` preview of **+1.663pp**. Recomputing that preview from **my** `fast_info` values
  returns **+1.6630pp** — byte-identical. ⇒ **`fast_info.last_price` is the settled close; the
  `repair=True` value (217.89) is the outlier and is synthetic by its own flag.** `M1042`.
- 🚫 **Right removed for this run**: **`repair=True` output may not be used as a settled price**
  anywhere downstream. Where an 08-28 close is needed, it comes from `fast_info.last_price`, and both
  readings are shown wherever a threshold is within one reading's width of the other.
- ⚠ A **second provider was attempted and failed** — Stooq returned **HTTP 404** for every US symbol
  tried. Logged as a failed lookup (§12); `D5`'s cross-provider check is therefore **unmet**, and the
  corroboration above is *temporal + cross-path within one provider*, which is weaker. **Stated, not
  glossed.**
- ⚠ `fast_info['previous_close']` disagrees with the daily bar's 08-27 close (**226.149** vs
  **227.98**). Not used, and not diagnosed — recorded as a fourth disagreement inside the same
  instrument. `M1043`.

### 2f · Named, NOT scored — every one with its reason (zero silent skips)

| id | why not scored |
|---|---|
| **`S120`** | Frozen observable is *"the first observation where **BOTH** `DGS30` and `T10YIE` carry 2026-08-28."* Measured: `T10YIE` **has 08-28 (2.31)**; `DGS30`'s last `[FRED]` observation is **08-27 (5.19)**. ⇒ **not readable. Stays ARMED, NOT `EXPIRED`.** ✅ **This is the row's own observation-lag clause working exactly as designed** — the clause was written in at registration precisely so this would be a deferral and not a discovery, which is what `S102` lacked for five runs |
| **`S111`** | `BAMLC0A0CM` (`ig_oas`) last `[FRED]` observation **08-27 = 0.79**; the row needs the first close covering **08-28**. **Stays ARMED.** ⚠ Pre-settle read disclosed rather than discovered later: 0.79 sits inside **C** (A ≥ 0.85 / B ≤ 0.77), 2bp above B — 🚫 **do not inherit that as "C fired"** |
| **`P67`** | Same lag: `hy_oas` last **08-27 = 2.63** vs a **≥ 2.85%** line. **Stays ARMED.** ⚠ 2.63 is **22bp below** the threshold; disclosed, not scored |
| **`S103`** | Handed here by the KR run this morning. Registered to settle **2026-08-29, a Saturday**; its `"first settled close on/after"` clause moves it to **08-31**. **NOT due, NOT `EXPIRED`.** 4-session preview **+1.663pp** vs bands ±5.0pp — reproduced independently (§2e) and **explicitly not a score** |
| **`S124`** | 🚨 **The 08-28 HANDOVER listed this as settling 08-28. It settles 2026-08-31** (cross-sectional IT breadth count at the 08-31 close). Corrected here; **not due** |
| `S92` `S94` `S104` `S112` | settle **08-31**. ⚠ `S104` carries the `R106` date defect in its title (*"July PCE 2026-08-28"* when PCE printed 08-26); **its settle date is later and no threshold is touched** |
| `P86` | PCE conjunct **met**; rate conjunct unreadable (`DGS2` 4.20 on 08-27 vs A ≤ 4.10 / B ≥ 4.32). **Stays ARMED** |
| `P97` | unreadable — `DTWEXBGS` (`dxy`) last observation **08-21**, seven days behind the joint date the row requires. **`D333`'s 11th reproduction** |
| `S109` (`FRO`) · `P81` `P85` `P87`–`P89` | not yet due (09-02 and later) |
| `S127` `S128` `S129` `S130` | armed, settle 09-08 / 09-09 / 09-09 / 09-10 |
| **`S8`** | ⛔ unscoreable for a **31st** consecutive run — date field still `[blank]`. **Named again rather than dropped.** A human must `VOID` it or re-register it with a date (P5) |
| KR-owned rows | zero due; earliest `S67-KR` **09-04** |

---

## 3 · Both ledgers audited — symmetric, per `carryover §3b/§3c`

| ledger | total | resolved | **legacy (no revival/entry condition)** | **due today** |
|---|---|---|---|---|
| `reject_ledger` | **249** | 151 | **0** | **0** |
| `missed_ledger` | **265** | 157 | **0** | **0** |

- ⚠ **A clean `due` is not read as proof of health** (the stage says so). The real evidence is the
  **legacy count, 0 on both for a 12th consecutive run**, and both totals grew (247→249, 258→265)
  while legacy stayed 0 — i.e. new rows are still being entered *with* conditions.
- **Zero rows carried a second HANDOVER unresolved.** No process failure on this axis.
- 🚨 **But `C22` (§1e) says the count is not the whole test**: a row can be conditional, non-legacy,
  and still **unable to fire**, because its condition observes our own builder rather than the market
  (`HII`). **A clean legacy count does not detect that class.** Carried, not resolved.
- ⚠ `missed_ledger`'s `excess` sign is **inverted** relative to `reject_ledger`. Not summed anywhere.

---

## 4 · Exposure state — carried as size context for BET/ALPHA (read-only; this stage never `log`s)

`exposure_rule.py state` (settled 08-28, bench `069500.KS`): rule state **정상**, *"발화 조건 없음"*.
Bench −1.791% on the day, −2.62% off its 20-day high, **+9.27% off its 20-day low**.
Target invested **95%**; `state` could not read current % (*"수익분해 불가 — NAV/투자비중이 없다"*).
`show --tail 8` **does** carry it: **invested 85.5%**, band gap **−9.5pp** (🚨밴드이탈), unchanged from
08-26 and 08-27 (−9.5 / −9.6 / −9.5).

**Cumulative decomposition, n=16 (unchanged)**: total excess **−11.68pp = cash −5.94pp + selection −5.74pp.**
- ⚠ **n=16, and it did not move.** The tool's own line: *"a month gets n≈20, and only then may the
  sign be asked"* (`C4`). Carried as **accumulation, not as an edge and not as a verdict on selection.**
- ⚠ Not a cold start (43 ledger rows) ⇒ the 2026-07-31 cold-start caveat does not apply.
- 🚨 **Standing alarm, unchanged and not this desk's to clear**: `ARMED (TIMEFOLIO_EXECUTE=1)` on
  every row. Reported because it is on the instrument's own output; **no action taken** (P4/P6).
- ⚠ Every ledger row is tagged **미정착봉 (live intraday)** — including the 08-28 row, written while
  that session was open. Given §2e and §11a, that tag is a live caveat, not boilerplate.

---

## 5 · Signal scoreboard (`ic_ledger score`) — the standing item is **unchanged**, and so is its constraint

`vol_surge` h=1: **n=39 · n_eff=39.0 · mean IC −0.0444 · t(NW) −3.84 · 26% positive · 필요n 11**,
graded **★유의(다중비교 통과)** — clears Bonferroni |t| > 2.8. `vol_surge` h=5 agrees in sign
(−0.0380, t −2.18, 단독기준); h=10 agrees but `n_eff 2.6` ⇒ **unquotable**. Identical to 08-28 —
**n did not advance**, which is `G6`'s FAIL showing up on a second instrument.

- ✅ Still the **only** cell on the board clearing the multiple-comparison bar at a quotable `n_eff`,
  and it still agrees independently with `M224`. The standing note stands: `sector_flow`'s 🟢 verdict
  weights `vol_surge` **positively** while the measured sign is **negative**.
- 🚫 **It does NOT license flipping the gate this run.** (i) **P4** — a gate change is a code/human
  decision. (ii) ★ **`W1`** — this ledger is **`KR`-labelled**; importing a KR-measured axis sign into
  the US desk is the exact cross-market transfer `W1` forbids, and the protocol's own N=4 note says a
  US change *"needs its own measurement first."* ⇒ carried as **a KR result with an unmeasured US
  implication**; the US-side measurement stays registered as `D395`, **unmet for a 2nd run**.
- ⚠ **14 of 21 cells remain unquotable** (`n_eff < 4`). Not quoted anywhere in this run.
- ⚠ Regime label required and stated: the window spans the **08-13 → 08-28 drawdown-and-rebound**
  band. A crash-window IC does not generalise.

---

## 6 · Reconciliation — belief (`handoff/`) vs coverage (`module_report_tags show`)

| finding | detail |
|---|---|
| **Coverage that is now a run behind** | `module_report_tags` reads `REPORT/industry_US/` and every US file there is dated **2026-08-27** — `BET_SHEET`, `SECTOR_ROTATION`, `EVENT_ALPHA`, `SWEEP_READ`, `BLINDSPOT_PREMORTEM`, `ACTION_TICKETS`, `CYCLE_EXPOSURE`. **The 08-28 run copied nothing**, consistent with §1b (it died before its writeback). ⇒ **the mechanical ledger and the analytical carry are stale by different amounts (2 days vs 3 days)** — and that gap is itself the reconciliation finding |
| **Belief without coverage** | `LITE`/`COHR` (optical) carry a standing §3a row and `cycle_registry.json` has **no optical row for a 13th run** (`D250`) ⇒ the belief is **un-instrumented**, not merely uncovered |
| **Resolved-but-live** | none surfaced this run |
| **Stale index** | `SECTOR_DEEP_SEMI.md` in `REPORT/` is dated **2026-07-15 (45 days)** while the AI-compute complex is the book's largest concentration — and `S79` L2 measured that complex's grouping as **U-MIXED**, i.e. undescribed by either candidate unit. **The coverage is stale on exactly the object the desk cannot group** |
| **Coverage without belief** | six US sectors carry a DEEP from the last two weeks (`COMM` `IT` `MATR` `UTIL` `FIN` `RE` `DISC` `INDU` `ENRG` `HLTH` `STPL`) with one or two standing §3a names each. Candidate DEEP material for ROTATION |

---

## 7 · Stale flags and cleared suspensions

- **Every §3a US row is `asof` 2026-08-26 = 3 days** (§1a). Horizon for a daily desk is 1 day ⇒
  **all flagged stale**, and the cause is **two missing writebacks**, not an aging market.
- `us_top300.csv` **45 days** (G5) — the single defect behind the stale weights, the news-coverage
  frontier, **and** each sector's `top1` identity (which is what G3 tests).
- **Cleared suspension → dig, not silent trust**: `D295` (re-derive `S127`'s `AVGO` bands from the
  options market once the straddle chain rolls past the 09-02 print) became actionable on the 08-28
  roll and is **still unmet, 4th run**. `AVGO` prints **D-4**. **Dig for this run's PREMORTEM (§8).**
- ⚠ **Do not retroactively clean the 08-22/23/24 stale-`asof` stretch.** Those snapshots stay
  unreadable for Δflow.
- ⚠ **New contaminated stretch, registered not cleaned**: the **2026-08-28 daily-close bar** is
  unreadable via `yf.download` for US names (§2e). Prior runs' figures are **not** retro-corrected;
  they carry this annotation instead.

---

## 8 · Dig list, ranked for today

| rank | dig | why today |
|---|---|---|
| 1 | **`D400` (new)** — *a verdict that exists only in a run directory is not scored.* **Positive form**: the writeback pass verifies `grep "<id>" handoff/SCENARIOS.md` returns ≥1 hit **for every id the run scored**, before the run is called complete | five verdicts were lost this way on 08-28 (§1b); recovered today, but only because someone looked |
| 2 | **`D394`** (registered 08-28, **recurred in its own run**) — a run's report set is not its carry. **Positive form**: verify `grep "<today>" handoff/STANDING_VIEW_US.md` ≥1 hit before completion | it has now cost the desk **3 days** of per-name carry |
| 3 | **`D401` (new)** — **PREFLIGHT's `asof` gate reads a field, not a bar.** `SECTOR_FLOW_US.json`'s `asof` is set to the **bench frame's last index date**, which a phantom/intraday bar satisfies. **Positive form**: G2 compares the snapshot's `last` for one liquid name against that date's **settled** close and reports the gap in % | measured today at **+4.6% (NVDA, 08-28 file)** — §11a |
| 4 | **`D402` (new)** — **`repair=True` fabricates a settled price and flags it only in a column nobody reads.** **Positive form**: any settled-price read asserts `Repaired? == False`, or falls back to `fast_info.last_price` and says which it used | it produced a value **0.34 away** from the corroborated close today (§2e) |
| 5 | **`D295`** — re-derive `S127`'s `AVGO` bands from a straddle spanning the 09-02 print | **D-4**; unmet for 4 runs |
| 6 | **`D379`** — PREFLIGHT's DIFF column reads yesterday's *frozen* file, so a late retraction is invisible. **Recurred today in its second form** (§11b): `R108` was filed 11 hours before PREFLIGHT ran and PREFLIGHT did not read it | 4th reproduction; prescription still unapplied |
| 7 | **`D395`** — the `vol_surge` result is **KR-measured**; build the US-side `ic_ledger` cell before any US gate change is discussed (`W1`) | unmet for a 2nd run |
| 8 | **`D250`** — no optical row in `cycle_registry.json`, **13th run** ⇒ optical exposure unmeasurable | two §3a names ride it |
| 9 | **`D9`** (block or warn on unit/label mismatch) · **`D10`** (news-body boilerplate; needs a server console, `P6`) · **`C22`** (which hand a revival condition names) | carried untouched — human items |

---

## 9 · RESEARCH triggers loaded as **binding constraints**, and what they bind

| group | fires when | binds, this run |
|---|---|---|
| **C** — C1 baseline · C2 both halves · C3 unknown column · **C4 "indistinguishable"** · **C5 arbitrary choice** | you cite a number | **MACRO, every stage.** `C5` is live twice today (§2b/§2c's two-surface invariance test) and `C4` in §4 (n=16, which did **not** advance) |
| **S** — S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · **S5 short samples** · S6 future labels | a statistical claim | any stage citing a test. `S5` binds G4's 250d window and `M953`'s n=1 frame |
| **D** — D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D5 cross-provider** · **D6 signal grade (OBV is C)** | you read data | **SWEEP · ALPHA · L2 indicators.** 🚨 **`D5` is UNMET this run** — the second provider 404'd (§2e). `D6` binds every OBV 매집/분산 word downstream |
| **W** — **W1 cross-market transfer** · W2 inherited lead/lag · W3 real≠profitable · **W4 name the customers** · W5 sub-sector dispersion · W6 reader's-market spine | you write a conclusion | **DEEP · BET · ROTATION.** `W1` binds §5 **and** the `R108` inheritance in §1d — where I separated the KR *magnitudes* (not transferred) from the shared *code mechanism* (transferred, because it is arithmetic in a file both desks run). `W4` unpaid on `RTX` for **210 days** |
| **L** (lenses) — L1 second derivative · **L2 peak-margin trap** · L3 branch information content | — | **DEEP · PREMORTEM.** `L2` binds `MPC`/`PSX`/`VLO`/`MRK`/`MSTR`. `L1` binds the `[inferred]` regime call itself |

---

## 10 · Catalyst injection — ≤48h binaries and the PREMORTEM obligation they create

`catalyst_calendar --days 14` → **5 binaries in window** (down from 7 on 08-28 — the 08-28 cluster has passed):

| when | event | bracket state |
|---|---|---|
| **D-2 · 2026-08-31 — INSIDE 48h** | **MSCI quarterly review** (calendar tags it `[derived≈]`, non-binary, but the passive print is concentrated at that close) | `S92` `S94` `S104` `S112` `S124` all settle **08-31**, and `S103` lands there too. **Six rows on one date** — `D343` in force |
| D-4 · 2026-09-02 | **`AVGO` earnings** (held) | `S127` armed (settle 09-08) — bands **hand-set**; `D295` says re-derive and it is **unmet, 4th run** |
| D-6 · 2026-09-04 | Aug Employment / NFP | `S126` covers it (`XLI` exc5, settle 09-04) |
| D-12 / D-13 · 09-10 / 09-11 | Aug PPI · Aug CPI | ⚠ **no bracket found on either.** Named as a gap for PREMORTEM |
| **undated** | *"Iran 'Strait of Hormuz open' statement"* (TACO trigger) | 🚨 **Still undated, 2nd run.** A **temporary Iran–Oman Hormuz transit deal was struck 2026-08-26** (`foreignpolicy`/`semafor`/`aljazeera`, recorded by the 08-28 run). The calendar has not absorbed it |

⇒ **PREMORTEM (Stage 7) inherits a hard obligation**: a **both-sides** bracket for every ≤48h binary
not already spanned. **A one-way tilt into a known binary is a protocol violation.** The two most
plausibly uncovered are **Aug PPI/CPI (09-10/09-11, zero rows)** and the **Hormuz state change**,
which is a live fact wearing an "undated" label.
⚠ **`S124` is the one cross-sectional row on 08-31** and it tests **this desk's own IT underweight**;
it is the row whose B branch vindicates the desk, which is stated so nobody reads C as a win.

---

## 11 · What this run has asserted and then refuted, so far (`§4c` / `D48`) — **two, both left standing**

### 11a 🚨 PREFLIGHT G2 wrote *"today's baseline is clean"* and this stage refuted it one hour later

PREFLIGHT G2 checked that `SECTOR_FLOW_US.json`'s `asof` field equals its filename date for
08-25→08-28 and wrote **"✅ 08-25 → 08-28 each carry an `asof` equal to their own filename date …
today's baseline is clean."**

**That sentence is true about the field and false about the bar.** Measured after it was written:

| snapshot | its `asof` | its `last` for NVDA | that date's **settled** close | gap |
|---|---|---|---|---|
| 08-27 file | 2026-08-27 | **224.17** | **227.98** | **−1.67%** |
| 08-28 file | 2026-08-28 | **227.46** | **217.55** | **+4.56%** |

Both `last` values sit **inside their own date's intraday range** (08-27 H/L 230.47/220.90; 08-28
H/L 229.26/216.81), which excludes "it is the prior close" and "it is an adjusted value". ⇒ **the
snapshots' terminal bars are LIVE INTRADAY prints taken minutes after the 09:1x ET open**, and
`sector_flow.py:507-509` sets `asof` from the **bench frame's last index date**, which an intraday
row satisfies. `M1045`.

⇒ **A `Δflow` between two snapshots is a difference between two intraday photographs, each labelled
with a settled date.** The G2 verdict is **left standing at PASS** — it measures axis-count
continuity, and that is continuous — but the additional constraint is **appended, not substituted**,
and it is handed to SWEEP as a binding one: *the snapshot's own `asof` is not evidence that the bar
settled.* Registered as **`D401`**. 🚫 **No stage may describe a `SECTOR_FLOW_US.json` figure as a
settled reading this run.**

### 11b 🚨 PREFLIGHT built its whole DIFF column without reading a retraction filed eleven hours earlier

`D379`'s prescription on file is *"PREFLIGHT reads `STANDING_VIEW.md §5` before building the column."*
**PREFLIGHT did not**, and `R108` — which retracts the citability of exactly the cross-sectional rank
and flipper output that G3 emits — was filed at ~11:00 KST by `industry_kr`, about eleven hours
before Stage −1 ran. The consequence is visible in the artifact: PREFLIGHT's ADDENDUM calls the new
IT/`NVDA` flipper *"the highest-consequence addition of the window"* **without knowing the desk had
retracted the instrument's rank output that morning.**

The PREFLIGHT text is **not edited**. The correction is carried in §1d as an **additional** removed
right, and `D379` is re-ranked (§8, rank 6) as **reproduced for a 4th time** — twice now in a run
that also names it.

⚠ **A third thing worth a line, because zero self-refutations usually means the controls were not
adversarial**: the genuinely adversarial checks this stage ran were §2a's six-leg reproduction of a
prior run's arithmetic (**all six matched to four decimals**), §2b/§2c's two-surface invariance test,
and §2e's temporal cross-check of `fast_info` against the KR run's independent 08-28 read
(**+1.6630pp vs +1.663pp**). **Those three survived, and that is reported as a result.** The two that
did not survive are above.

---

## 12 · Failed lookups this stage (per the unattended-run rule)

| lookup | result |
|---|---|
| **Stooq** (`https://stooq.com/q/d/l/?s=<sym>.us&i=d`) — attempted as the `D5` second provider for the 08-28 closes | **HTTP 404** on every symbol (`nvda.us` `spy.us` `mrvl.us` `avgo.us` `mu.us` `sndk.us` `wdc.us`). Retried once with a raw-response diagnostic; same. **`D5` unmet — stated in §9, not glossed** |
| `yf.download` daily `Close` for **2026-08-28**, all US names | **NaN** (Volume and OHL present). Not a lookup failure so much as a provider defect — recorded as `M1040`–`M1043` rather than as a gap |

---

## ✅ EXIT CHECK
- [x] Shared spines (`STANDING_VIEW.md` §1/§5/§6, `SCENARIOS.md` master log + index) + `STANDING_VIEW_US.md` §3a + `SCENARIOS_US.md` + `RESEARCH.md` Part C read; **`SCENARIOS_KR.md`/the KR blocks opened** — which is how `S103`'s Saturday settle and the `R108`/`C22` filings were inherited. `module_report_tags show` cross-queried (§6).
- [x] **Retracted ledger read BEFORE today's view formed** (§1d). `R108` (filed today), `R103`, `R89` all bind; `R89`'s successor `P83` is the row §2a lands.
- [x] **Every past-dated scenario scored or named with a reason** (§2a–§2f). Zero silent skips. `S8` named for a **31st** run. The 08-28 run's five orphaned verdicts **recovered and landed**, not silently re-scored.
- [x] `reject_ledger.py due` run — **0 due, 0 legacy** of 249 (§3). Not substituted with `score`.
- [x] `missed_ledger.py due` run — **0 due, 0 legacy** of 265 (§3). Signs not summed. ⚠ `C22` records that a clean legacy count does not detect an unfireable condition.
- [x] **Exposure state read and carried** (§4): 정상 · target 95% · current **85.5%** · gap **−9.5pp** · cumulative **−11.68pp = cash −5.94 + selection −5.74, n=16 (unmoved)**. Not a cold start; `C4` stated.
- [x] 🚨 **Instrument health inherited before any number was trusted** (§0) — `PREFLIGHT.md` exists, written by this run's Stage −1. Four FAILs converted into explicit removed rights, **plus two removed rights PREFLIGHT could not have written** (§11a `D401`, §1d `R108`).
- [x] **Claims this run asserted and then refuted are written down, not edited away** (§11a, §11b) — and the three adversarial checks that *survived* are reported too.
- [x] Stale rows flagged with `asof` (§1f, §7); the cleared `D295` suspension carried as a dig for a 4th run, not as a trust; a **new** contaminated stretch (the 08-28 daily bar) registered rather than cleaned.
- [x] `[measured]`/`[inferred]` preserved on every carried claim; the `[inferred]` regime call is explicitly barred from being cited as evidence (§1c).
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L, with the stages they bind named** (§9) — including the one that is **unmet** (`D5`).
- [x] `HANDOVER.md` written. `handoff/*.md` writeback happens **at run end** — and §1a/§1b are exactly why this run will verify that both the carry **and** the scoring landed.
- [x] **No position sizing and no buy/sell language anywhere above** (P4).
