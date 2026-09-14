# HANDOVER — industry_US · 2026-08-27 (Stage 2 / L1·HANDOVER)

> Inheritance stage. Transports what this desk already believes, already pre-committed to, and already
> got wrong. **No sizing, no buy/sell language (P4).** English-pure runtime.
> **Run clock: 2026-08-27 22:1x KST = 09:1x ET — US PRE-MARKET, before the 09:30 open.**
> ⇒ **the terminal settled US close is 2026-08-26.** Every date-dependent statement below is written
> against that bar, not against today's.

---

## 0. Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-08-27/industry_US/preflight/PREFLIGHT.md` **exists and ran before this stage.**

| Gate | Verdict | What this run may NOT do |
|---|---|---|
| G1 news axis | **FAIL** (`vel_coverage` 17.06%, 7th consecutive run below the 80% bar) | 🚫 no theme-freshness / news-velocity citation in **any** stage; 🚫 no "quiet"/"no news" verdict on any name or sector; every `BET §B` freshness row must read `UNMEASURED (G1 FAIL)`; 🚫 **no cross-sectional use of the partial velocity subset** — its coverage is a market-cap rank prefix |
| G2 scale continuity | **PASS** (`n_axes` 3 on all seven snapshots 08-20 → 08-26) | Δflow subtraction is scale-legal, **conditional** on SWEEP re-reading `§scoring.n_axes` before differencing |
| G3 sector-sign owner | **PASS** (list emitted, **3 of 11**) | 🚫 **Consumer Discretionary (`AMZN`), Materials (`LIN`), Energy (`XOM`) may not be promoted/demoted on the weighted-flow bucket** — substitute `eqflow`/`breadth` and say so inline |
| G4 risk-unit stability | **FAIL** (250d → 11 units · 500d → 10 · 750d → 10, groupings differ) | 🚫 no bare concentration number — **every unit count carries its `--days` on the same line** |
| G5 universe covers holdings | **FAIL** (staleness leg: `us_top300.csv` **43 days** old; coverage leg clean, 11 of 11) | 🚫 `wflow` is not a **current** weighting; prefer `eqflow` on disagreement, tag `wflow` with its 43-day stamp |
| G6 accrual rate | **FAIL** (18 files / 36 days = 0.50/day, **2.0× slower**) | 🚫 no IC-backed sizing language — any fraction is **"mechanical 1/4 — IC not yet estimable (G6 FAIL)"** |
| G7 tool liveness | **PASS** (26 exit-0; `module_chart` non-standard, verified live by real invocation) | — |

⚠ **An instrument that returns a number is not an instrument that works.** G7 passing removes no other
gate's FAIL — G1 is the standing proof: `module_news_data --help` exits 0 and single queries answer
correctly, and the axis it feeds is 17% covered.

★ **PREFLIGHT carries a CORRECTION appended by this stage** — see §6 below. Its gate verdicts are
unaffected; what was withdrawn is a **priority claim**, and the withdrawal is appended, not edited in.

---

## 1. Inherited standing view

### 1.1 Regime call (§1, shared spine) — **carried unchanged, tag preserved**
> **"Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight."**
> `[inferred]` — built on the measured chain (M1–M6, M18), never promoted to `[measured]`.

**Carried, not re-derived.** One new settled session is `n = 1` (`S5`) and does not test a regime call.
⚠ **`[inferred]` may be carried; it may not be cited as evidence** for a new proposition downstream.

★ **But today it received its first genuine forward test, and the test AGREED** — see §2, `P90`.
The chain's prediction was *"tight level + decelerating rate ⇒ **pass-through**, not pricing power."*
`NVDA`'s 08-26 print guided FQ3 gross margin **down 100bp** while naming **memory/DRAM cost** as the
cause. That is one observation and is recorded as such; the regime call's own designated test remains
**`MU`'s 2026-09-24 print**.

### 1.2 Standing sector verdicts inherited from the 2026-08-26 ROTATION (the baseline MACRO must not silently move)
```
ENRG OW · HLTH OW · MATR N · COMM N · DISC N · FIN N · STPL N− · RE N− · INDU UW− · UTIL UW− · IT UW
```
🚨 **Written out here on purpose.** `D358-KR` has now fired **five** times across the two desks, and its
mechanism every time was a stage inheriting a verdict from the *run-before-last*: 08-26 US MACRO carried
`MATR N+` when the standing verdict was `N`; this morning's KR MACRO carried `IT N` when the standing
verdict was `N−`. **MACRO §E of this run must reconcile against the line above before writing a verdict.**
**`STPL` is `N−`, demoted 08-26 — not `N`.**

### 1.3 Per-name carry (§3a US registry, latest row wins) — 11 US book names
| name | theme label | carried thesis state | stale? |
|---|---|---|---|
| `NVDA` | AI-compute-EPICENTER | largest single position; **printed 08-26 AMC** — the carry is now one session out of date on its central fact | ⚠ **refresh today** |
| `AVGO` | AI-compute-EPICENTER | carried with **its customer unnamed for the life of the position** (`W4` open); bracketed by `S127` (09-08); prints **09-02** | ⚠ `W4` open |
| `ANET` | AI-compute-EPICENTER | FINRA short-vol z **+2.06** (board's highest, 08-25) against accumulating OBV — the `C18` disagreement | ⚠ `C18` |
| `HPE` | AI-compute-chain | FINRA z −1.73 / 5v5 −13.2▼ (a large exit) | — |
| `MPC` · `PSX` | energy-refining | the registered refiner kill **FIRED on settled bars 08-26** (5-session crack rate −2.862 → −1.675) on a re-measured **36.1%** unconditional base rate ⇒ a one-in-three marker | ⚠ live |
| `MET` | life-insurer/FIN | Financials' reds live in one node — insurance/brokers, 26% of names carrying 70% of reds (`M955`) | — |
| `NDAQ` | exchanges/FIN | capital-markets node nets ≈ 0 | — |
| `NUE` | steel/MATR | `MATR` is a G3 flipper today ⇒ sector-level `wflow` unusable by rule | ⚠ G3 |
| `RTX` | defense-missile | — | — |
| `028050` · `316140` | KR (owned by the sibling desk) | `028050` **+5.23% on 08-26 attributed to an unverified Russian-state-wire ceasefire report** (KR run's `M-…`); **`316140` new-share listing 869.7만주 on 08-31** | ⚠ KR-owned |

**Stale-check result**: **no `asof` older than this run's horizon on any of the 11**, because the 08-26
run rewrote §3a in full. The one genuinely stale object is **`NVDA`'s row**, stale by exactly one
event — its own print — and that is repaired in §2 rather than flagged and left.
⚠ Carried forward from the 08-26 run's own self-correction: the §3a stale-flag is **a documentation
gap, not an unexamined-name gap** — the recheck function migrated to the mechanical ledgers, which are
clean (§4).

### 1.4 Retracted ledger (§5) — **read BEFORE forming today's view**, per the stage rule
Nothing this run intends to assert matches a retracted claim, **with one exception, which is disclosed
rather than dropped** (§6). The two most recent retractions bind directly on today's stages:
- **`R103`** (2026-08-26) — *"the news axis fails because the 300-query sweep overloads the tunnel"* is
  **DEAD**. The axis is **CAPPED**: 51 names = `us_top300` ranks 1–51, contiguous, byte-identical across
  runs (`M947`). **G1 and G5 are the same defect** — a rank prefix of a 43-day-old cap file decides who
  gets a news reading. 🚫 **No stage may write "the tunnel dropped under load" today.**
- **`R104`** (2026-08-26) — the `RUBIN` **z 8.4** figure is **VOID as a partial-day artifact** (the same
  8 articles / 5 outlets measure z 3.3 against a complete-day denominator). `D354`'s *observation*
  survives; its **magnitude may not be quoted.**
- Older and still binding: `R93` (Warsh's speech moved to 08-27~29 **after** `S108` froze),
  `R47`, and the `[RECONSTRUCTED]` block `R27`–`R45` — **binding as prohibitions, but their numbers may
  not be quoted as original measurements** (the 08-05 truncation incident).

### 1.5 Open contradictions (§6) — carried deliberately, **not** resolved by picking a side
| id | Status inherited today |
|---|---|
| **`C15`** · the `vol_surge` gate | **Re-measured this run and the split is unchanged and maximal**: US `h=1` **t(NW) +3.40, n_eff 33.0** vs KR `h=1` **−3.61, n_eff 38.0** — *the same axis, opposite signs, both clearing Bonferroni (|t| > 2.8)*. `W1` forbids importing either side. **Human-gated; `sector_flow` still weights it positively.** |
| **`C16`** · the two admissible instrument families disagree | Still live and still pointed at the largest sector call: `IT` is `eqflow` rank 2 of 11 with the 2nd-lowest red-rate against `exc5 −1.449` with 36 of 56 negative, verdict `UW`. Routed to **`P101` (settles 09-04)**. |
| **`C17`** · value chains split across ≥3 sector labels | US arm is an **open dig, not a measurement** — `D250`/`M731`'s optical/interconnect gap logged **12 times**, never tested as a `C17` instance. |
| **`C18`** · the two short-interest instruments disagree about **direction** | Carried. FINRA daily short-volume z (a **flow**) vs `module_flow` short-interest %float (a **stock**). Fired on `MRVL`, `NVDA`, `ANET` on 08-25. **Neither is graded highly enough to overrule the other; neither is an axis in `ic_ledger`, which is why it is a contradiction and not a bug.** |
| **`C19`** · (KR-registered 08-27) revival conditions whose observable is a **desk action** | Ported here as a **check on this desk's own ledger writes**: any `--revives-if` this run files must contain a market-side conjunct. |
| **`C20`** · (KR-registered 08-27) the `base ≥ 100` theme filter excluded the term that actually moved the session | Carried. Relevant to any freshness filter this run would use — **moot today by G1 anyway.** |
| `C14` · `C10` · `C1` · `C2`-successor | Carried unchanged. |

---

## 2. Scenarios — every past-dated row settled or explicitly named

### 2.1 ✅ SCORED THIS RUN — `P90` → **branch A (FIRED-A)**

**`P90`** — *"Is `NVDA`'s >15% price increase a MARGIN EXPANSION or a COST PASS-THROUGH?"*
(registered 2026-08-23; owner `industry_US`; handed to this desk by the 2026-08-27 `industry_kr` run,
which supplied *"adjusted GM 75%, in line"* and correctly declined to score an unowned row).

**Branch A required BOTH legs. Both are met on the printed document:**

| Leg | Threshold as registered | Measured | Verdict |
|---|---|---|---|
| 1 | guided next-quarter GM **≤** reported quarter's GM | **FQ3 guide ~74.0%** vs **FQ2 reported 75.0%** ⇒ **−100bp** | ✅ met |
| 2 | reported quarter's GM does **not** exceed the prior quarter's by more than **50bp** | **FQ2 75.0%** vs **FQ1 74.9%** ⇒ **+10bp** | ✅ met |

- **Source, quoted to the body** (`yahoo_finance` 08-27, Q2 earnings dissection): *"gross margin rose to
  75% in the quarter, compared with 74.9% in the previous quarter and 72.4% a year earlier"*, and
  *"guidance falling from 75% in the second quarter to about 74% in the third quarter."*
  Corroborated independently by a second body (`nasdaq`/`fool` 08-26 20:19 EDT): *"fiscal third-quarter
  gross margin guide of 74% is 100 basis points lower than what it just reported for the fiscal second
  quarter."* **Two outlets, same two numbers** (`D311` satisfied).
- **The mechanism is named in the document, not inferred**: the reporting attributes the compression to
  **memory/DRAM cost**, quantified in one body as *"a 2% gross margin hit from DRAMs."* A third body
  (`seekingalpha` 08-26, earnings-call transcript) records the company **resetting its longer-run gross
  margin outlook to 72%–73%** alongside ~70% FY2028 revenue growth.
- **Primary-source cross-check on the revenue leg** — `module_fundamentals_us NVDA` pulled **SEC XBRL
  $96.22bn** for the quarter ended **2026-07-26** against the press figure **$96.2bn**, and reported
  **yfinance ↔ XBRL agreement 4/4 quarters within 5%**. *(The GM figures themselves are non-GAAP and
  come from bodies; see the construction note below.)*
- **Anti-signal (VOID) checked, did not fire**: `NVDA` **did** report on 2026-08-26 and **did** guide
  gross margin. No publication failure.
- **What branch A means, stated as registered**: *the cost curve is binding.* It **confirms** the desk's
  regime-call chain on its first forward test, and it carries opposite implications for `AVGO` (09-02,
  bracketed by `S127`) and the memory complex.

⚠ **Construction finding, recorded rather than improvised around** (`§2` rule: an ambiguous observable is
a finding about the scenario, not a licence to invent a threshold): **`P90` never specified GAAP vs
non-GAAP**, and its leg-2 tolerance is **50bp** while the press quotes GM to **0.1pp**. The measured
+10bp gap survives that ambiguity comfortably (it would take a >5× error to reach the line), and leg 1
clears by 100bp — **so the row is scoreable as written and is scored.** But the next GM-threshold row
must name the basis. ⇒ registered as **`D380`** in §7.

⚠ **Joint-scoring obligation, declared at `S115`'s registration, is NOT yet dischargeable**: `S115`
states it is *"scored jointly with `P90`"* — branch A **with** margin expansion falsifies `P90`, branch A
**with** flat margin confirms it. `S115`'s own observable is `NVDA`'s **08-27 session**, which has not
traded (§2.2). **`P90` is scored on its own document today; the joint reading is owed by the next run**
and is named here so it cannot be dropped silently.

### 2.2 ⏸ NOT YET SETTLEABLE — seven rows whose observable is **tonight's 08-27 close** (this is a clock fact, not a skip)

| row | observable | why it cannot be read at 09:1x ET |
|---|---|---|
| **`S79`** | `NVDA` 1-session excess vs `SPY` on the **2026-08-27** session | the session has not opened |
| **`S81`** | EW{`AVGO`,`ANET`,`HPE`} 2-session excess vs `SPY`, 08-25 close → **08-27 close** | same |
| **`S115`** | `NVDA` 1-session return + excess on **08-27** | same |
| **`S117`** | `MU` 1-session excess vs `NVDA` on **08-27** | same |
| **`S119`** | EW Energy basket 3-session excess vs `SPY`, 08-24 → **08-27 close** | same |
| **`P83`** | (`HO=F` − `RB=F`) × 42, change from the 08-20 settle, at the **08-27** close | same |
| **`P96`** | 3-2-1 crack **5-session rate on settled closes** at the **08-27** close | same |

🚨 **This is a structural property of the schedule, not an accident, and it is the eighth-plus instance
of the `D355`/`D364` class**: the US desk fires at **KST 22:xx = ET pre-market**, so **every row it
writes with a same-day settle is unreadable by the run that inherits it on that day** and must wait for
the *next* run. Seven rows on one date. **They are named here, with their thresholds intact and their
owner unchanged, so the next run inherits an explicit obligation rather than a gap.**
⚠ **They are NOT marked `EXPIRED`** — an `EXPIRED` mark means the observable came and went unscored.
Here the observable **has not occurred yet.** Marking them expired would be a false negative on the
desk's own scoreboard.
⚠ `S81` carries a registered anti-signal that is **live** and must be evaluated at scoring, not now:
*"a separate ≤48h macro binary on 2026-08-26/27 ⇒ AMBIGUOUS."* **Jackson Hole opens 08-27** and
**Warsh's first speech as Chair falls 08-27~29** (`R93`). The next run must rule on that clause
explicitly before reading `S81`'s branch.

### 2.3 ⏸ DEFERRED, observable not published — **`P77`** (`D333` reproduces for a **10th** time)
- **Required**: `DGS30` at *the first `[FRED]` close covering **2026-08-26***. Branch A ≤ **5.18**,
  branch B ≥ **5.38**, C between (C the disclosed favourite at ~80%).
- **Measured this run** `[FRED]`: `DGS30` series **ends 2026-08-25 at 5.17**. There is **no 08-26 bar.**
  Cross-checked across the whole rate block — `DGS10`/`DGS2`/`DGS5`/`DFII10` all end **08-25**;
  `T10YIE` and `SOFR` carry **08-26**; `DTWEXBGS` ends **08-21**; `NFCI` **08-21**.
  ⇒ the **last joint rate date is 08-25**, one day short.
- 🚨 **Named, not skipped, and this is its second consecutive deferral** (the KR desk deferred it this
  morning for the identical reason). **A third deferral without a resolution is a process failure to
  name in bold**, on the same footing as an unscored `EXPIRED` row.
- ⚠ **State disclosed without scoring**: the last published value, **5.17, sits 1bp INSIDE branch A**
  (≤ 5.18). 🚫 **This is not a score and may not be handed downstream as one** — `P77`'s frozen
  observable is the 08-26 bar, not the 08-25 bar, and `D93`'s own baseline puts a ±10bp move at
  roughly p10/p90 per 5 observations. The row stays **ARMED**.

### 2.4 ✅ Taken by the sibling desk this morning — recorded, not re-scored (ownership confers no exclusivity, but double-scoring does)
`S101` → **FIRED-C** (spread −0.744pp; its VOID anti-signal actively measured at 0 of 10 in-window
earnings) · `P78` → **FIRED-B** (range 4.889 → 1.440pp, crossing the entire C band in one session with
its leg ordering inverted) · `P80` → **FIRED-C** (robust to which bar is read).

### 2.5 Scoreboard for this stage
**Scored 1** (`P90` → A) · **Not-yet-settleable 7** (§2.2) · **Deferred on an unpublished observable 1**
(`P77`) · **Taken by the sibling desk 3** (§2.4) · **`EXPIRED` 0** · **silent skips 0.**
⚠ **`S8` is unscoreable for a 28th consecutive run.** It is named again rather than dropped; a row that
has been unscoreable for 28 runs is evidence about the *row's construction*, and retiring it is a human
call this desk keeps deferring.

---

## 3. Both ledgers audited — the scoreboard is symmetric or it is not a scoreboard

| ledger | total | resolved | **due (recheck date passed)** | **legacy (no revival/entry condition ever set)** |
|---|---|---|---|---|
| `reject_ledger.py due` | **242** | 146 | **0** | **0** |
| `missed_ledger.py due` | **251** | 148 | **0** | **0** |

- **Legacy count is 0 on both sides for a 16th consecutive run** — that is the line the stage rule says
  to cross-check, and it is the only real evidence the practice has taken hold. It is **not** flat at a
  bad number; it is flat at zero, having been drawn down from a historical legacy stock of 24.
- ⚠ **A clean `due` is not proof of health** (stage rule, stated explicitly). What it proves is that
  **no row's scheduled date has arrived**, not that the rows are well-built. `C19` (registered by the
  sibling desk this morning) says exactly the opposite about their *content*: three rows carry revival
  conditions whose observable is a **desk action**, so no market outcome can ever settle them. **That
  class is a `due`-invisible defect** — it will never surface here.
- 🚫 **The two ledgers' `excess` columns are NOT summed anywhere in this run**: the sign is inverted
  between them (`missed`: `excess > 0` means missing it cost us).
- ⚠ `missed_ledger score` still carries the **seeded, outcome-selected first 6 rows** (harvested from
  `leak_scan --top`, i.e. from names that had already risen). Class means may be quoted as
  **accumulation**, never as an edge.

---

## 4. Exposure state — inherited as **size context**, read-only (this stage never runs `log`)

- `exposure_rule.py state` → rule state **정상 / normal** (prior: normal), trigger conditions absent.
  Benchmark `069500.KS` close 109,135, **+1.323%** on the day, −0.84% from its 20-day high.
- 🚨 **`state` could NOT read the account** — it prints **`투자비중미상` (invested-% unknown)** and
  **"수익분해 불가: NAV/투자비중이 없다"**. ⇒ **the invested % below is STATED from the accrued ledger
  row, not substituted by this stage** (P5).
- `exposure_rule.py show --tail 10` → **42 rows**; the 2026-08-27 row reads **invested 85.4%**,
  **target 95%**, ⇒ **band gap −9.6pp** (flagged `🚨밴드이탈 −9.6pp` by the tool itself).
- **Cumulative decomposition, n = 15**: **total excess −13.48pp = cash −6.21pp + selection −7.27pp.**
  ⚠ **n = 15 is not a sign** (`C4`) — the tool says so in its own output. Both components are negative,
  which at least removes the 2026-07-31 ambiguity where a lead was almost entirely cash weight.
- ⚠ **Not a cold start** (42 rows), so the 4-state verdict is readable — but **9 of the last 10 rows are
  `live`, i.e. unsettled intraday bars**; only the 08-14 row is `settled`. Treat the daily excess
  decomposition as provisional.
- 🚨 **Standing alarm on every row, carried forward unresolved**: `ARMED (TIMEFOLIO_EXECUTE=1)`. **This
  desk issues no orders and touches no `--execute` path.** Recorded because a research run that reads
  the ledger should see that the mirror is armed.

---

## 5. Signal scoreboard (`ic_ledger`) — does this desk's ranking have a sign yet?

`axis_inflection.py` → 16 axis files written. `ic_ledger.py log` → **0 new rows** (no newly-resolved
cells; a new run/session must pass). `ic_ledger.py score --market us` → **15 tests, 405 ledger rows.**

**Quotable cells only (`n_eff ≥ 4`), Bonferroni threshold |t| > 2.8:**

| axis | h | n | n_eff | mean IC | t(NW) | 필요n | reading |
|---|---|---|---|---|---|---|---|
| `rs60` | 5 | 27 | 5.4 | **−0.1310** | **−5.46** | 2 | ★ clears Bonferroni, **NEGATIVE** |
| `vol_surge` | 1 | 33 | 33.0 | **+0.0398** | **+3.40** | 12 | ★ clears Bonferroni, **POSITIVE** |
| `rs60` | 1 | 33 | 33.0 | −0.0635 | −2.77 | 18 | single-test only, same sign as h=5 |
| `obv_norm` · `rs20` · `flow_score` (h=1,5) | | 27–33 | 5.4–33.0 | −0.02…−0.05 | −0.9…−1.4 | 36–165 | indistinguishable |

- 🚨 **`C15` re-measured and unchanged**: US `vol_surge` h=1 **+3.40** vs KR **−3.61**, both
  Bonferroni-passing, opposite signs, `n_eff` 33 and 38. **`W1` forbids importing either into the other
  market.** `sector_flow` still weights `vol_surge` **positively** in `flow_score`. **Human-gated —
  this run does not flip the gate** (P4).
- **`rs60` h=5 at t(NW) −5.46 is this desk's strongest measured cell**, and `S128` (settles 09-09) is its
  **first out-of-sample test**, with branch B written to kill it before it becomes doctrine.
- 🚫 **Six of fifteen cells carry `n_eff < 4` and are unquotable** — including `rs60` h=10 (t −3.87) and
  `obv_norm` h=10 (t −3.03), which would otherwise look decisive. Overlapping forward windows inflate t.
- ⚠ **Regime label required and supplied**: the accrual window is a **rising, high-dispersion AI-led
  tape with two percentile-extreme defensive/AI rotations inside it** (`P79`, `P98`). A crash-window IC
  would not generalize, and neither does this one.
- ⚠ `필요n` is quoted only for the `n ≥ 10` cells above, per the small-n instability rule.

---

## 6. 🚨 What this run asserted and then refuted — written down, not edited away (`§4c`, `D48`)

**One self-refutation this run, caught one stage after it was written.**

**The assertion** (PREFLIGHT §G1, written at Stage 1): that the contiguous-rank-prefix measurement was
**"★ New this run"**, and that *"yesterday's phrasing 'the failure tracks burst load' was directionally
right but the wrong shape."*

**The refutation** (this stage, on reading `handoff/STANDING_VIEW.md` §5): **the finding is one run old
and was already retracted by this desk.** `R103`, filed **2026-08-26**, killed the burst-load diagnosis
on `M947` — *the 51 velocity-measured names are `us_top300` ranks 1–51, contiguous, byte-identical to
08-25's set.* This morning's `industry_kr` run cites `R103` by name in `D371-KR`.

**What survives / what dies.** The *measurement* stands and is now a **third independent reproduction**;
the **removed right it produced is unchanged and still binds**. What is withdrawn is the **priority
claim** and the implied liveness of the burst-load diagnosis. **PREFLIGHT's text was left standing with
the correction appended below it**, per the append-only rule.

**Why the stage could not see it — a real mechanism, not carelessness.** PREFLIGHT's `vs-yesterday` DIFF
column (`D358-KR`, executed the day it was registered) compares **today's PREFLIGHT against yesterday's
PREFLIGHT.md**. Yesterday's file is **frozen at the moment it was written**, and the burst-load sentence
was retracted **later in that same run**. The retraction lives in `STANDING_VIEW.md`, which PREFLIGHT
does not read — by design, since it runs before HANDOVER. ⇒ **`D358-KR`'s remedy has a blind spot: a
diagnosis retracted late in run N is invisible to the DIFF column in run N+1, which reads the
pre-retraction text as if it were the standing view.** Registered as **`D379`** in §7.

⚠ **Zero self-refutations would itself be a finding.** One, caught by the next stage's own mandated read
rather than by a human, is the control working.

---

## 7. Dig list ranked for today, + two new digs registered by this stage

> **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`, excluding this
> run's own files: **`D379` `D380` → 0 hits.** Current highest before this append: **`D378-KR`**
> (2026-08-27 `industry_kr`). ⚠ `D76`'s collision class checked against **both** desks' allocations.

### New this stage
| # | Finding | Positive-form remedy |
|---|---|---|
| **`D379`** | 🚨 **The `vs-yesterday` DIFF column reads a frozen artifact, so a diagnosis retracted late in run N is invisible in run N+1.** Measured today: PREFLIGHT G1 re-derived and re-announced a finding that `R103` had **already retracted 24 hours earlier**, because the only thing it diffs against is yesterday's `PREFLIGHT.md` — which still contains the pre-retraction sentence. The retraction lives in `STANDING_VIEW.md §5`, which PREFLIGHT does not read (it runs before HANDOVER, correctly). **The remedy for one blind spot (`D358-KR`) created another.** | **PREFLIGHT grep-checks `handoff/STANDING_VIEW.md §5` for the ID of any claim it is about to repeat from yesterday's file, and prints `[RETRACTED r=<Rnn>]` beside that DIFF row.** A grep, not a read — it costs one pass and needs no ordering change. ✅ **Applied by hand this run**: the correction is appended to `PREFLIGHT.md` under its own heading, gate verdicts untouched. |
| **`D380`** | ⚠ **A margin-threshold bracket was registered without naming GAAP vs non-GAAP, and with a tolerance finer than its own likely source.** `P90`'s leg 2 is *"the reported quarter's gross margin does not exceed the prior quarter's by more than **50bp**"* — but the row never says which basis, and the press quotes GM to 0.1pp while GAAP and non-GAAP GM differ by percentage points. **It was scoreable today only because the measured gap (+10bp) and the leg-1 gap (−100bp) both clear the ambiguity by a wide margin.** A closer print would have been unscoreable, which is `S8`'s failure mode arriving through a different door | **Every accounting-metric bracket names its basis (GAAP / non-GAAP / company-adjusted) and its source document class in the registration table, and sets its tolerance no finer than that source's published precision.** ✅ Applied to this run's own reading: both bases are stated wherever `P90` is cited downstream. |

### Carried digs, ranked by what they cost **this** run
1. **`D355` / `D364` — the run fires before its own day exists.** Top of the list, because it is the
   direct cause of **seven unsettleable rows** (§2.2) and, on the 08-26 run, of a sweep on a stub bar
   (median volume **2.48%** of the prior session, 0 of 299 names above 50%). **Every price and news
   instrument this run touches inherits it.** Candidate DEEP-adjacent question: is any of this desk's
   output improved by running pre-market at all?
2. **`R103` / `D366` + G5 — G1 and G5 are one defect.** A rank prefix of a **43-day-old** cap file
   decides which 51 names get a news reading. Rebuilding `us_top300.csv` would move *both* gates.
   **Human-approval item** (it is a data rebuild, not a research task).
3. **`D333` — 10th reproduction, and now it is blocking a row twice.** `P77` deferred two runs running.
4. **`D294` — 8th reproduction.** `action_bracket` names a binary and then reports none exist.
   `ACTION_TICKETS.md` hand-built for a 4th consecutive run.
5. **`D369` — the tag extractor manufactures verdicts from prose**, reproduced at scale on KR this
   morning (39 of 58 rows read `LIVE`/`FRESH`/`GO` while ALPHA issued zero). 🚨 **Binding on this run's
   own handoff write**: with G1 FAILed, every freshness row will read `UNMEASURED`, and the ledger must
   not be allowed to convert that into a `GO`.
6. **`D250` / `M731` — 13th run** with no optical/interconnect row in `cycle_registry.json`, on a board
   where `COHR`/`LITE` sit inside `S128`'s reversal basket. **This is the strongest standing candidate
   for a DEEP mandate** and the `C17` US arm at the same time.
7. **`D297` — 9th run**: `GOOGL`+`GOOG` ≈ 76.6% of a 12-name Comm Svcs bucket while
   `top1_flips_sign` prints **false**. COMM remains un-measurable by rule.
8. **`D341`** — `OKLO`, `LYB`, `DOW`, `FRO`, `X`, `AA` outside `us_top300`; **`FRO` prints 08-28 with
   `S109` armed.**
9. **`D343` — 08-28 carries NINE rows.** Any registration this run makes must avoid it and say why.
10. **`D10`** — open code defect (news-body boilerplate); needs **human approval + a server console**
    (FTS writes are server-only, P6). Carried, not re-discovered.
11. **`D371-KR`** — the KR cap test proposed off `R103`. **Not this desk's to run** (`W1`), noted so the
    US side does not duplicate it.

---

## 8. RESEARCH rules loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | **Binds, this run** |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · **C3 unknown column** · C4 "indistinguishable" · **C5 arbitrary choice** | **every stage.** `C4` is live on the exposure decomposition (n=15) and on every `ic_ledger` cell below Bonferroni. `C5` is live on `risk_units`' 0.65 threshold and on every sector grouping choice. |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · **S4 in-sample ≠ done** · **S5 short samples** · S6 future labels | **HANDOVER §5, MACRO, ALPHA.** `S5` is why the regime call is carried on `n=1`. `S4` is why `rs60` h=5 needs `S128`. |
| **D** | you read data | D1 second venue · **D2 proxy sign** · D3 signed vs unsigned · **D4 regime contamination** · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators · L2 money_trail.** `D6` binds every OBV-based 매집/분산 claim to grade C. `D5` is discharged on `NVDA` revenue (yfinance ↔ SEC XBRL, 4/4 within 5%). |
| **W** | you write a conclusion | **W1 cross-market transfer** · W2 inherited lead/lag · W3 real ≠ profitable · **W4 name the customers** · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** `W1` is the live constraint on `C15` (US +3.40 vs KR −3.61 — neither may cross). `W4` is **open on `AVGO`** for the life of the position and `S116` (08-28) is the row that would close it. |
| **L** | lenses, not triggers | L1 second derivative · **L2 peak-margin trap** · L3 branch information content | **DEEP · PREMORTEM.** `L2` is live on the refiners (`MPC`/`PSX` held, kill fired 08-26) **and now on `NVDA`** — `P90` branch A is `L2`'s mechanism arriving on the epicenter. |

⚠ **Loaded as constraints, not as a summary.** The specific ones that will bite downstream are named
above with the object they bite.

---

## 9. Reconciliation — belief vs coverage (`module_report_tags show`)

- **Coverage without a standing belief**: `SECTOR_DEEP_SEMI.md` last written **2026-07-15** and
  `SECTOR_DEEP_CONSUMER.md` **2026-08-16** are the two stalest US sector files in the ledger, and
  **`SEMI` is the epicenter of the #1 cycle** — the name-level carry is dense but the *sector* file is
  six weeks old. Candidate DEEP mandate.
- **Belief without coverage**: **`COMM` is un-measurable by rule for a 9th run** (`D297`) while carrying
  a standing `N` — a verdict that no admissible instrument currently supports or contradicts.
- **Resolved-but-live**: none flagged this run.
- 🚨 **Ledger hygiene warning inherited (`D369`) and binding on this run's own writeback**: the extractor
  tagged `HOOD` and `COIN` **`CONFIRMED FRESH GO LIVE`** off prose in a report whose every freshness row
  read `UNMEASURED (G1 FAIL)`. **A downstream desk reading the ledger would see a verdict the 08-26 run
  explicitly refused to issue.** With G1 FAILed again today, the same trap is armed again.

---

## ✅ EXIT CHECK
- [x] Shared spines read (`STANDING_VIEW.md` — regime call §1, measured chain §2, retracted ledger §5 in
      full including the 08-05 truncation notice, open contradictions §6; `SCENARIOS.md` scoring log +
      master index) **plus** this desk's halves (`STANDING_VIEW_US.md`, `SCENARIOS_US.md`) and
      `RESEARCH.md` Parts A/B/C.
- [x] **The other market's files opened** — `STANDING_VIEW.md`'s 2026-08-27 `industry_kr` asof entry and
      the KR dig block were read, and they are why `S101`/`P78`/`P80` are recorded as already-taken
      (§2.4) and why `C19`/`C20`/`D371-KR` appear in the carry.
- [x] Mechanical ledger cross-queried (`module_report_tags show`) — §9.
- [x] **Retracted ledger read BEFORE forming today's view**, and it immediately caught one of this run's
      own claims (§6). `R103`/`R104` bind named stages.
- [x] **Every past-dated scenario scored or explicitly named**: 1 scored (`P90` → A), 7 not-yet-settleable
      with the clock reason stated (§2.2), 1 deferred on an unpublished observable (`P77`, `D333` 10th),
      3 recorded as taken by the sibling desk. **`EXPIRED` 0 · silent skips 0.**
- [x] `reject_ledger.py due` run — **0 due, 0 legacy**; legacy-count line reported (16th run at zero).
- [x] `missed_ledger.py due` run — **0 due, 0 legacy**; signs never summed across the two ledgers.
- [x] **Exposure state read and carried** — `정상`, target 95% vs accrued **85.4%**, band gap **−9.6pp**,
      cumulative n=15 total **−13.48pp** = cash −6.21 + selection −7.27. 🚨 `state` could not read the
      account (`투자비중미상`) — the invested % is **stated from the ledger row, not substituted**, and
      **not a cold start** (42 rows).
- [x] 🚨 **Instrument health inherited before any number was trusted** — §0, with each FAIL rendered as a
      removed citation right.
- [x] **One self-refutation written down, not edited away** (§6) — and the mechanism that produced it
      registered as a dig (`D379`).
- [x] Stale rows flagged with their `asof`; the one genuinely stale object (`NVDA`'s row, stale by its
      own print) is repaired in §2 rather than merely flagged.
- [x] `[measured]` / `[inferred]` tags preserved — the regime call is carried as `[inferred]` and is
      **not** used as evidence for any new proposition in this file.
- [x] RESEARCH triggers loaded **as binding constraints**, grouped C/S/D/W + L, each named against the
      stage and the object it binds (§8).
- [x] `HANDOVER.md` written. `handoff/*.md` writeback is **owed at run end** (append-only for
      retractions), per the stage contract.
- [x] **No position sizing, no buy/sell language anywhere** (P4).
