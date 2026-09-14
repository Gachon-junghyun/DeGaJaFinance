# HANDOVER — industry_US · 2026-08-30 (Stage 2 / L1·HANDOVER)

> Run fires **2026-08-30 22:1x KST = Sun 09:1x ET**. **US markets closed; the 2026-08-28 session is
> the last one that happened, and it settled two days ago.** No new US session has occurred since the
> 08-29 run scored it. ⇒ **the price-keyed scenario board is unchanged**, and the only rows that could
> have matured are the `[FRED]`-keyed ones (§2c).
> P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.

---

## 0 · Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-08-30/industry_US/preflight/PREFLIGHT.md` **was run** (Stage −1, this run).
**6 FAIL / 1 qualified PASS.** The rights it removes bind every stage after this one:

| Gate | Verdict | What this run may NOT do |
|---|---|---|
| **G0** bar completeness (08-28 Close NaN **301/301**; 5m proxy err **0.018% mean / 0.045% max**, n=24) | **FAIL, proxy-recovered** | No 08-28 close taken from the daily endpoint, the book, `status`, or `pulse`. ✅ The 08-28 session **may** be cited from the 5m proxy **with the proxy label on the same line** |
| **G1** news axis (`vel_coverage` **17.06%**, 51/299) | **FAIL** on the sweep axis | No theme-freshness / news-velocity citation **sourced from the sweep**; no "sector X is quiet". ✅ Direct queries live (6/6 pre-sweep, 4/4 post-sweep, **5/5 on names the sweep had failed**) |
| **G2** scale continuity (`n_axes` 3 = 3) | **PASS (idling)** | `scored=0` ⇒ **no Δflow, no "newly green", no flow-rose/fell list.** The last valid US sweep observation is the **08-28 run** |
| **G3** sector-sign ownership (`sector_rotation` = `[]`) | **FAIL** | **No `wflow` promotion/demotion in ROTATION §2**, and `eqflow`/`breadth` are in the same empty file. Sector calls must come from axes outside the sweep and say so inline |
| **G4** risk-unit stability (250d **11** / 500d **10** / 750d **10**, memberships differ) | **FAIL** | No bare concentration number; the `--days` rides on the same line. **Whether ANET·ETN·AVGO·NVDA are one bet or four is unmeasured** |
| **G5** universe covers holdings (**11/11**; file **46 days**) | **FAIL** (staleness leg) | `wflow` is not a current weighting. G3's prohibition dominates anyway |
| **G6** accrual (20 files / 40 days = **0.50/day**, 2.0× slow) | **FAIL** | No IC-backed sizing language; any fraction is "mechanical 1/4" |
| **G7** tool liveness (35/37 exit 0; `module_chart` renders **0/3** US tickers) | **FAIL** | **No US chart shape/pattern verdict.** Structural levels must be computed from the series and labelled as such |

★ **The gate that mattered most is G0, and it did not resolve the way the inheritance predicted.**
The 08-29 run handed forward *"the 08-28 daily bar is unreadable for US names"* and stopped there,
using `fast_info.last_price` for the handful of names it needed. **This run found a route that
recovers the whole session and measured its error before using it** (PREFLIGHT §G0(c)) — and that
route **independently reproduces the 08-29 run's `fast_info` reads to the cent** (§11a).

---

## 1 · Inherited standing view — and **one process failure that has now run four days**

### 1a 🚨🚨 `D394`: the US per-name carry has missed **three consecutive writebacks**, and the miss is now **partial in a diagnosable way**

Measured this run, not inherited:

| file | mtime | last labelled US block | 08-29 hits | 08-30 hits |
|---|---|---|---:|---:|
| `handoff/SCENARIOS.md` | **2026-08-29 23:05** | **08-29 `industry_US`** ✅ | 14 | 0 |
| `handoff/SCENARIOS_US.md` | **2026-08-29 23:05** | **08-29 `industry_US`** ✅ | 4 | 0 |
| `handoff/STANDING_VIEW.md` (spine) | 2026-08-29 11:03 (**KR** run) | **2026-08-27** `industry_US` | 8 — **all KR** | 0 |
| `handoff/STANDING_VIEW_US.md` | **2026-08-26 23:31** | **2026-08-26** | **0** | 0 |
| `handoff/RESEARCH.md` | 2026-08-29 11:04 (**KR** run) | — | 7 — **all KR** | 0 |

⇒ **The finding is sharper than "the writeback failed".** The 08-29 run's writeback **half-landed**:
- ✅ **The scoring half landed.** `S79`·`S81`·`P83`·`P96`·`S119`·`S116`·`S118` are all present in
  `SCENARIOS.md`. **`D400` — registered by that run one day earlier — worked.** A dig that was
  written on 08-29 morning and closed by 08-29 night is the fastest close on this desk's board.
- ❌ **The standing-view half did not.** `STANDING_VIEW_US.md` has not been appended since **08-26**;
  the spine's last US block is **08-27**. ⇒ **the §3a per-name carry this run inherits is `asof`
  2026-08-26 = 4 days old**, and it was 3 days old yesterday, which means it aged by exactly the
  amount a missed run ages it.
- ⇒ **`D394` is not "sometimes the writeback dies"; it is "one of the two writeback targets is
  reliable and the other is not."** Registered in that form (§8 rank 1). ★ This is a *better* dig than
  the one inherited, because it is falsifiable in one grep and it names which file to fix.

### 1b Regime call (shared spine §1, carried unchanged)

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]` — the equity tracks the **second derivative** of price, not the level, which is why
> "shortage persists" and "stocks struggle" are both true.

⚠ Carried with its tag intact. **`[inferred]` — it may not be cited as evidence** for any new
proposition this run. It frames; it does not prove.

### 1c Retracted ledger (§5) — read BEFORE forming today's view. **Four entries bind, and one is *re-armed* by today's data**

- 🚨 **`R103`** — *"the news axis fails because the 300-query SWEEP overloads the tunnel"* → **RETRACTED
  2026-08-26** by `M947` (the 51 measured names were a **contiguous rank prefix**, which load-shedding
  cannot produce). ★ **Today's PREFLIGHT measurement cuts against the retraction, and I am recording
  that rather than quietly re-adopting the killed claim:**
  - The 08-28 run's 50 successes are **NOT a contiguous prefix** — they sit at index 8, 19, 20, 25 …
    296, 298, scattered across the whole universe. I checked this specifically because `R103` was
    killed on the contiguity claim.
  - **5/5 names the sweep recorded as `velocity: null` answered normally when queried directly**
    ~2 minutes later (QCOM 0.98 · DIS 0.70 · ADBE 1.03 · PFE 0.74 · T 0.75).
  - ⇒ **What the two observations jointly support is neither the retracted claim nor its replacement**:
    the survivors are the **highest-article-count names** (mega-caps + semis), i.e. the pattern is
    *selection by article volume under a limiter*, not a rank prefix and not stochastic load-shedding.
  - 🚫 **This does NOT resurrect `R103`** — `R103`'s specific mechanism (burst load ⇒ stochastic drop)
    is still refuted, and re-asserting a retracted claim needs a **new** measurement that names the old
    one, which is what this bullet is. Registered as **`D412`** (§8) so the next run tests the
    article-count hypothesis directly instead of re-litigating either side.
  - ✅ **Unchanged either way**: the *permission* is the same. 17.06% is far below 80%; **G1 FAILs**.
- **`R108`** (filed 08-29 by `industry_kr`) — *"the `rs20` bench-misalignment bias is a constant
  offset, therefore cross-sectional RANK survives"* → **RETRACTED**; the mechanism is
  `clip(rs20 / 8.0)` in **shared** code (`scripts/sector_flow.py:173`), so a uniform input bias
  becomes a non-uniform output bias wherever the transform saturates. ★ **It binds this run in an
  unusual way: today there is no rank to defend.** `sector_rotation` is empty, so `R108`'s object does
  not exist this run. **Carried, not exercised.** ⚠ `W1` still applies to its *magnitudes* (19/28
  sectors, 67→44 greens are KR numbers and are not transferred); what transfers is the arithmetic.
- **`R89`** — *"the refiners pay WITHOUT the barrel"* → RETRACTED 08-21, and its registered successor
  separator **`P83` also failed** (`FIRED-B`, −13.56 in five sessions). ⇒ **the desk still has no
  surviving instrument separating refining excess from the barrel, and this run may not re-assert
  separation on any instrument.** ⚠ This binds directly today, because **`MPC +1.47%` and `PSX +1.76%`
  were two of the four strongest names on the 08-28 proxy tape** (§1e) — exactly the observation that
  would tempt a separation claim.
- **`R106`** (July PCE printed 08-26, not 08-28) · **`R107`** (a rate event's pre-pricing is not
  readable from a close-to-close difference) carried. **`R109`** is a KR instrument row and does not
  bind this desk.

### 1d Open contradictions (§6) — carried, **not** resolved

- **`C22`** — the desk's two ledgers name different hands, and its **US instance** is the one that
  binds: the `missed_ledger` row for `HII` revives on *"`HII` enters the universe via
  `build_us_universe.py --include`"* — **a condition that observes our own builder, not the market.**
  ⚠ And G5 measures that builder's output at **46 days**. ⇒ the condition is non-legacy, conditional,
  and **still cannot fire**. Carried; which hand a revival condition should name is a human call.
- **`C21`** (RSI convention) carried untouched — `us_setup_screener` not invoked yet this run.
- **`D9`** (measured-unit vs book-label mismatch: block or warn?) — reproduced in **all three** G4
  windows again today, and the 250d/500d disagreement is on **the book's largest cluster**. Carried.

### 1e Per-name carry, `asof` 2026-08-26 (⚠ **4 days**, §1a) — tags preserved, **and the 08-28 tape appended to each**

★ The carried rows are 4 days stale, but the **08-28 session is now readable** (G0 proxy). I am
attaching that one measured number to each row rather than re-deriving the thesis, so the staleness is
visible and the newest fact is not lost.

| Name | Carried state (`asof` 08-26) | 08-28 (5m-proxy close, err ≤0.05%) | Tag |
|---|---|---|---|
| `NVDA` (held) | The epicenter; printed 08-26 AMC, +8.738% on 08-27 | **217.54 · −4.58%** — the give-back, already scored inside `S116`/`S118` | `[measured]` |
| `AVGO` (held) | Worst `rs60` on the book (−24.1); FINRA z −2.17. **Prints 2026-09-02**; `S127` armed (settle 09-08) | **368.68 · −0.77%** — held up while the complex fell | `[measured]` ⚠ **D-3. `D295` unmet, 5th run** |
| `ANET` (held) | OBV 매집, `rs20 +17.4 / rs60 +12.3` against the board's **highest** FINRA short pressure (z +2.06) | **195.31 · −2.87%** | `[measured]` |
| `ETN` (held) | AI-power/electrical; in the 500/750d unit with `ANET`, separate at 250d | **402.67 · −3.21%** | `[measured]` |
| `HPE` (held) | AI-compute-chain; prints **2026-09-03** and the calendar cannot see it | **52.29 · −3.90%** — the book's **worst** 08-28 name | `[measured]` |
| `MPC`·`PSX` (held) | Refining **margin, not crude beta** (`exc60` +41.4/+33.5, OBV 매집) — **but the separation instrument is dead** (`R89`/`P83`) | **368.88 · +1.47%** and **244.03 · +1.76%** — the tape's **two best book names** | `[measured]` ⚠ separation may not be re-asserted |
| `MET`·`NDAQ` (held) | Both in `S128`'s **decay** basket (`rs20<0 ∧ rs60>0`); settles 09-09 | **96.50 · +0.26%** · **99.31 · −0.04%** | `[measured]` |
| `NUE` (held) | Two instruments, neither a turn: +22% over 200DMA vs NEUTRAL/CHOP, OBV 분배 −65% | **250.51 · −0.74%** | `[measured]` |
| `RTX` (held) | 🔴분산, `delta −0.629` = book's largest negative. Cycle has **no threshold set**; `W4` unpaid **211 days** | **211.72 · −0.17%** | `[measured]` |
| `XOM` (ENRG top1) | The sweep's only Energy red; in `reject_ledger` (`K.본문반증`), recheck **09-09** | (proxy captured; XLE **+0.59%**) | `[measured]` |
| `MRK` | Health Care's only 🟢 — **and it trades ABOVE its mean target** (upside −4.4%) ⇒ `L2` | — | `[measured]` |
| `COIN` / `HOOD` / `MSTR` | `COIN`: #1 flow on the **worst revision book** (−303.5%), carried **only with its denominator**. `HOOD`: the clean version. `MSTR`: rejected `H.밸류소진`, recheck 09-16 | — | `[measured]` |
| `EQIX`·`DLR`·`IRM` | The carried data-centre grouping is **not observed** (`M953`). ⚠ n=1 frame | — | `[measured]` |
| optical (`LITE`·`COHR`) | 🚨 `cycle_registry.json` still has **no optical row** ⇒ exposure **unmeasurable, not zero** | — | `[measured]` ⚠ `D250`, **14th run** |
| `MU` | Prints **2026-09-30** (corrected 08-29 from a carried 09-24) | — | `[measured]` |

★ **What the 08-28 tape adds that the carry did not have** — and it is one line, stated once so no
downstream stage double-counts it (`D343`): **the four worst names on the book that day (HPE −3.90,
ETN −3.21, ANET −2.87, NVDA −4.58) are the four the 250d window calls separate risk units and the
500/750d windows merge into two.** ⇒ **G4's unresolved disagreement is not academic; it is a
disagreement about the group that actually moved together on the last observable session.** This is
an observation, not a regrouping — it is the second such observation (the first was `S79` L2's
`U-MIXED` on 08-27), and **two observations both pointing at "the desk has no validated grouping"** is
what the dig list needs to carry, not a new grouping.

---

## 2 · Scenarios — **zero due**, every deferral named with its reason (zero silent skips)

> No US session has occurred since the 08-29 run scored the board. **Price-keyed rows cannot have
> matured.** The only maturation channel open today was `[FRED]`, and it did not open (§2c).

### 2a · Price-keyed rows — not due, because no new close exists
`S103` (settle written 08-29, a Saturday; its *"first settled close on/after"* clause moves it to
**2026-08-31**) · `S92` `S94` `S104` `S112` `S124` (all settle **08-31**) · `S126` (09-04) ·
`S127` (09-08) · `S128` `S129` (09-09) · `S130` (09-10) · `S109`·`P81`·`P85`·`P87`–`P89` (09-02+).
**None due. None `EXPIRED`.**
⚠ `S104` still carries the `R106` date defect **in its title** (*"July PCE 2026-08-28"* when PCE
printed 08-26); its settle date is later and **no threshold is touched** by saying so.

### 2b · Rows scored on 08-29 — verified landed, not re-scored
`S79`·`S81`·`P83`·`P96`·`S119`·`S116`·`S118` all present in `handoff/SCENARIOS.md` (§1a).
**I did not re-score them.** ★ Re-scoring a frozen observable is how a desk ends up with two values
for one fact; the check performed was *presence in the ledger*, which is the `D400` test.

### 2c · `[FRED]`-keyed rows — the one channel that could have matured, and it did not

Pulled fresh this run (`module_macro_us --days 30 --json`, 19 series):

| series | last `[FRED]` observation | the row waiting on it | still ARMED? |
|---|---|---|---|
| `DGS30` (us_30y) | **08-27** = 5.19 | **`S120`** (needs BOTH `DGS30` and `T10YIE` carrying 08-28) | ✅ **ARMED, not `EXPIRED`** |
| `T10YIE` (breakeven_10y) | **08-28** = 2.31 | — (its half is ready; the conjunct is not) | — |
| `BAMLC0A0CM` (ig_oas) | **08-27** = 0.79 | **`S111`** (first close covering 08-28) | ✅ ARMED |
| `BAMLH0A0HYM2` (hy_oas) | **08-27** = 2.63 | **`P67`** (≥ 2.85%) | ✅ ARMED |
| `DGS2` (us_2y) | **08-27** = 4.20 | **`P86`** (PCE conjunct **met**; rate conjunct unreadable) | ✅ ARMED |
| `DTWEXBGS` (dxy) | **08-21** — **nine days behind** | **`P97`** | ✅ ARMED · 🚨 **`D333`'s 12th reproduction** |

⇒ **Identical to yesterday, and that is the correct outcome, not a failure**: the H.15 daily series
post one business day in arrears, so Friday 08-28's values publish **Monday 08-31**. The rows'
observation-lag clauses are doing exactly what they were written to do.
⚠ **Pre-settle readings disclosed here rather than discovered later, and none of them is a score**:
`ig_oas` 0.79 sits inside **C** (A ≥ 0.85 / B ≤ 0.77), **2bp above B**; `hy_oas` 2.63 is **22bp below**
`P67`'s line; `DGS2` 4.20 sits between `P86`'s A ≤ 4.10 and B ≥ 4.32. 🚫 **No stage may inherit any of
these three as "the branch fired."**
⚠ `DTWEXBGS` at **nine days** is worse than the seven the 08-29 run recorded — the gap is **widening**,
which is the part of `D333` that has never been diagnosed.

### 2d · `S8` — ⛔ unscoreable for a **32nd** consecutive run
Date field still `[blank]`. **Named again rather than dropped.** A human must `VOID` it or re-register
it with a date (P5). ★ 32 runs is long enough that the *naming* is now the finding: a row that cannot
be scored and cannot be killed is consuming a slot in every HANDOVER's exit check.

### 2e · KR-owned rows
Zero due; earliest `S67-KR` settles **09-04**. `SCENARIOS_KR.md` opened and checked (the ownership rule
says a past-dated row in the other file is still this run's to score — there is none).

---

## 3 · Both ledgers audited — symmetric, per `carryover §3b/§3c`

| ledger | total | resolved | **legacy (no revival/entry condition)** | **due today** |
|---|---|---|---|---|
| `reject_ledger` | **251** (was 249) | 151 | **0** | **0** |
| `missed_ledger` | **269** (was 265) | 157 | **0** | **0** |

- ⚠ **A clean `due` is not read as proof of health.** The evidence that matters is the **legacy count,
  0 on both for a 13th consecutive run**, while both totals grew (249→251, 265→269) — i.e. new rows
  keep being entered **with** conditions.
- **Zero rows carried a second HANDOVER unresolved.** No process failure on this axis.
- 🚨 **`C22` (§1d) is the standing caveat**: a row can be conditional, non-legacy, and still unable to
  fire because its condition observes our own builder. **A clean legacy count does not detect that class.**
- ⚠ `missed_ledger`'s `excess` sign is **inverted** relative to `reject_ledger`. Not summed anywhere.

---

## 4 · Exposure state — carried as size context for BET/ALPHA (read-only; this stage never `log`s)

`exposure_rule.py state` (settled 08-28, bench `069500.KS`): rule state **정상**, *"발화 조건 없음"*.
Bench **−1.791%** on the day, **−2.62%** off its 20-day high, **+9.27%** off its 20-day low, volume 1.041×.
Target invested **95%**; `state` could not read current % (*"수익분해 불가 — NAV/투자비중이 없다"*).
`show --tail 8` carries it: **invested 85.5%**, band gap **−9.5pp** (🚨밴드이탈).

**Cumulative decomposition, n=16 (unchanged for a third run)**: total excess **−11.68pp = cash −5.94pp
+ selection −5.74pp.**
- ⚠ **n did not advance.** The tool's own line: *"a month gets n≈20, and only then may the sign be
  asked"* (`C4`). Carried as **accumulation, not as an edge and not as a verdict on selection.**
  ★ **n has now been 16 for three consecutive runs while the calendar advanced three days** — that is
  the same stalled-accrual signature `G6` reports on the snapshot side, on a second instrument.
- ⚠ Not a cold start (43 ledger rows) ⇒ the 2026-07-31 cold-start caveat does not apply.
- 🚨 **Standing alarm, unchanged and not this desk's to clear**: `ARMED (TIMEFOLIO_EXECUTE=1)` on every
  row. Reported because it is on the instrument's own output; **no action taken** (P4/P6).
- ⚠ Every ledger row is tagged **미정착봉 (live intraday)**, including 08-28. Given G0, that tag is a
  live caveat, not boilerplate.

---

## 5 · Signal scoreboard (`ic_ledger score`) — the standing item **advanced**, and its constraint did not

`vol_surge` h=1: **n=40 · n_eff=40.0 · mean IC −0.0400 · t(NW) −3.32 · 28% positive · 필요n 15**,
graded **★유의(다중비교 통과)** — clears Bonferroni |t| > 2.8. `vol_surge` h=5 agrees in sign
(−0.0365, t −2.12, 단독기준); h=10 agrees but `n_eff 2.7` ⇒ **unquotable**.
★ **n advanced 39 → 40** (it had been flat on 08-28→08-29), so this instrument, unlike §4's, is
still accruing.

- ✅ Still the **only** cell on the board clearing the multiple-comparison bar at a quotable `n_eff`,
  and it still agrees independently with `M224`. The standing note stands: **`sector_flow`'s 🟢 verdict
  weights `vol_surge` positively while the measured sign is negative.**
- 🚫 **It does NOT license flipping the gate this run.** (i) **P4** — a gate change is a code/human
  decision. (ii) ★ **`W1`** — I verified the label rather than inheriting it: `ic_ledger log` prints
  **`총 1014행 · market=kr`**. **The ledger is KR-only.** Importing a KR-measured axis sign into the US
  desk is the exact cross-market transfer `W1` forbids, and the protocol's own N=4 note says a US
  change *"needs its own measurement first."* ⇒ **`D395` unmet for a 3rd run**, now with the
  confirming measurement attached.
- ⚠ **14 of 21 cells remain unquotable** (`n_eff < 4`). Not quoted anywhere in this run.
- ⚠ Regime label required and stated: the window spans the **08-13 → 08-28 drawdown-and-rebound** band.
  A crash-window IC does not generalise.

---

## 6 · Reconciliation — belief (`handoff/`) vs coverage (`module_report_tags show`)

| finding | detail |
|---|---|
| ★ **The two halves have swapped which one is stale** | `REPORT/industry_US/` is now dated **2026-08-29** across the board (`BET_SHEET`, `SECTOR_ROTATION`, `EVENT_ALPHA`, `SWEEP_READ`, `BLINDSPOT_PREMORTEM`, `ACTION_TICKETS`, `CYCLE_EXPOSURE`, `HANDOVER`, `MACRO_REPORT`, `preflight/`, 4× `SECTOR_DEEP_*`). ⇒ **the mechanical ledger caught up; the analytical carry did not** (08-26). Yesterday the gap was 2 vs 3 days; today it is **1 vs 4** — the two are diverging, not converging |
| **Belief without coverage** | `LITE`/`COHR` (optical) carry a standing §3a row and `cycle_registry.json` has **no optical row for a 14th run** (`D250`) ⇒ the belief is **un-instrumented**, not merely uncovered |
| **Resolved-but-live** | none surfaced this run |
| **Stale index** | `SECTOR_DEEP_SEMI.md` in `REPORT/` is dated **2026-07-15 (46 days)** while the AI-compute complex is the book's largest concentration — **and §1e measured that same complex as the four worst names on the last observable session.** The coverage is stale on exactly the object the desk cannot group |
| **Coverage without belief** | eleven US sectors carry a DEEP from the last two weeks (`COMM` `IT` `HLTH` `ENRG` fresh 08-29; `MATR` `UTIL` `FIN` `RE` `DISC` `INDU` `STPL` older) with one or two standing §3a names each. Candidate DEEP material for ROTATION |

---

## 7 · Stale flags and cleared suspensions

- **Every §3a US row is `asof` 2026-08-26 = 4 days** (§1a). Horizon for a daily desk is 1 day ⇒ **all
  flagged stale**, and the cause is **three missing writebacks**, not an aging market.
- `us_top300.csv` **46 days** (G5) — behind the stale weights, the news-coverage frontier, **and** each
  sector's `top1` identity (which is what G3 tests, when G3 has a file to test).
- **Cleared suspension → dig, not silent trust**: `D295` (re-derive `S127`'s `AVGO` bands from the
  options market once the straddle chain rolls past the 09-02 print) is **unmet, 5th run**, with
  `AVGO` now at **D-3**.
- ⚠ **Do not retroactively clean the 08-22/23/24 stale-`asof` stretch**, nor the **2026-08-28 daily-bar**
  stretch registered on 08-29. Prior figures are **not** retro-corrected; they carry the annotation.
  ★ **New this run**: the 08-28 stretch is **no longer unreadable** — it is readable *by a different
  route with a measured error* (G0(c)). **That does not clean the old figures**; it means new work may
  use the session, and every use says which route it used.

---

## 8 · Dig list, ranked for today

| rank | dig | why today |
|---|---|---|
| 1 | **`D394`, re-specified** — the writeback has **two targets and only one is reliable**. **Positive form**: the run's completion check greps `STANDING_VIEW_US.md` for today's date, **separately** from the `SCENARIOS.md` grep `D400` already installed | measured today: the scenario half landed at 08-29 23:05, the standing-view half has not moved since **08-26** — **4 days** of per-name carry lost |
| 2 | **`D412` (new)** — the news-axis survivor set is **selected by article volume**, not by rank position and not at random. **Positive form**: next run logs, for 20 sampled names, `(rank, base_article_count, velocity_returned?)` and reports the correlation | today's PREFLIGHT falsified the "contiguous prefix" reading (successes at index 8…298) **and** measured 5/5 recovery on failed names ⇒ neither `R103` nor its replacement describes the data |
| 3 | **`D413` (new)** — **a settled US close is recoverable from the 5m endpoint when the daily bar is void**, at **0.018% mean error**. **Positive form**: PREFLIGHT's G0 runs the D-1 proxy-vs-official validation every run and publishes the error, so the fallback is pre-authorised rather than improvised mid-run | it converted an unreadable session into a citable one today, on the single most informative session for the book's largest cluster |
| 4 | **`D295`** — re-derive `S127`'s `AVGO` bands from a straddle spanning the 09-02 print | **D-3**; unmet for **5** runs |
| 5 | **`D395`** — build the **US-side** `ic_ledger` cell; the `vol_surge` result is KR-only (`market=kr`, verified this run) before any US gate change is discussed (`W1`) | unmet for a **3rd** run, now with the confirming label measurement |
| 6 | **`D333`** — `DTWEXBGS` publication lag, now **9 days** and widening | **12th** reproduction; never diagnosed |
| 7 | **`D250`** — no optical row in `cycle_registry.json`, **14th run** ⇒ optical exposure unmeasurable | two §3a names ride it |
| 8 | **`S8`** — 32 runs unscoreable with a blank date; needs a human `VOID` or a date (P5) | the naming itself is now the finding (§2d) |
| 9 | **`D9`** (block or warn on unit/label mismatch) · **`D10`** (news-body boilerplate; server console, `P6`) · **`C22`** (which hand a revival condition names) | carried untouched — human items |

---

## 9 · RESEARCH triggers loaded as **binding constraints**, and what they bind

| group | fires when | binds, this run |
|---|---|---|
| **C** — C1 baseline · C2 both halves · C3 unknown column · **C4 "indistinguishable"** · **C5 arbitrary choice** | you cite a number | **MACRO, every stage.** `C4` binds §4 (n=16, third run unmoved) and §5's 14 unquotable cells. `C5` binds every 08-28 proxy number (the route is a choice, so the route is named) |
| **S** — S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · **S5 short samples** · S6 future labels | a statistical claim | any stage citing a test. `S5` binds G4's 250d window (249 days, tool's own warning) and `M953`'s n=1 frame |
| **D** — D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D5 cross-provider** · **D6 signal grade (OBV is C)** | you read data | **SWEEP · ALPHA · L2 indicators.** 🚨 **`D5` is UNMET again** — the second provider (Stooq) is now behind a JS proof-of-work challenge, not a 404 (§12); the corroboration in §11a is **three paths inside one provider**, which is weaker and is stated as such. `D6` binds every OBV word downstream |
| **W** — **W1 cross-market transfer** · W2 inherited lead/lag · W3 real≠profitable · **W4 name the customers** · W5 sub-sector dispersion · W6 reader's-market spine | you write a conclusion | **DEEP · BET · ROTATION.** `W1` binds §5 (verified `market=kr`) **and** `R108`'s inheritance in §1c, where the KR magnitudes are held back and only the arithmetic transfers. `W4` unpaid on `RTX` for **211 days** |
| **L** (lenses) — L1 second derivative · **L2 peak-margin trap** · L3 branch information content | — | **DEEP · PREMORTEM.** `L2` binds `MPC`/`PSX`/`MRK`/`MSTR` — ★ and binds them *harder today*, because `MPC`/`PSX` were the tape's two best book names on 08-28 while `R89`/`P83` say the desk cannot separate that from the barrel. `L1` binds the `[inferred]` regime call itself |

---

## 10 · Catalyst injection — ≤48h binaries and the PREMORTEM obligation they create

`catalyst_calendar --days 14` → **5 binaries in window**:

| when | event | bracket state |
|---|---|---|
| **D-1 · 2026-08-31 — INSIDE 48h** | **MSCI quarterly review** (`[derived≈]`, non-binary by the calendar's own tag, but the passive print concentrates at that close) | `S92` `S94` `S104` `S112` `S124` settle **08-31**, and `S103` lands there. **Six rows on one date** — `D343` in force |
| **D-3 · 2026-09-02** | **`AVGO` earnings** (held) | `S127` armed (settle 09-08) — bands **hand-set**; `D295` unmet, **5th run** |
| D-5 · 2026-09-04 | Aug Employment / NFP | `S126` covers it (`XLI` exc5, settle 09-04) |
| D-11 / D-12 · 09-10 / 09-11 | **Aug PPI** `[bls✓]` · **Aug CPI** `[bls~est]` | ⚠ **no bracket on either.** Named as a gap for PREMORTEM for a **2nd** run |
| **undated** | *"Iran 'Strait of Hormuz open' statement"* (TACO trigger) | 🚨 **Still undated, 3rd run.** A temporary Iran–Oman Hormuz transit deal was struck **2026-08-26**; the calendar has not absorbed it |

⇒ **PREMORTEM (Stage 7) inherits a hard obligation**: a **both-sides** bracket for the **08-31 cluster**
(inside 48h) and for every other dated binary not already spanned. **A one-way tilt into a known binary
is a protocol violation.**
⚠ **`S124` is the one cross-sectional row on 08-31 and it tests this desk's own IT underweight** — the
row whose B branch vindicates the desk. Stated here so nobody reads C as a win.
⚠ **A second thing about 08-31 that today's instrument state makes sharper**: six rows settle on the
first session after a session the desk could only read through a proxy. **If the daily endpoint is
still void on 08-31, six verdicts land on proxy-derived closes at once.** Named now, not discovered then.

---

## 11 · What this run has asserted and then refuted, or independently corroborated (`§4c` / `D48`)

### 11a ✅ The 08-28 close: a **third** independent path, and it agrees to the cent
Not a refutation — a survived adversarial check, reported because §4c says a run with zero of either
usually did not run controls.

| path | NVDA 08-28 | SPY 08-28 | who measured it |
|---|---|---|---|
| `Ticker.fast_info['last_price']` | **217.55** | **769.35** | 08-29 `industry_US` run (`M1042`) |
| `yf.download(..., repair=True)` | 217.89 *(synthetic, flagged)* | 769.35 | 08-29 run — **ruled out as the outlier** |
| **5-minute bar, last print 15:55 ET** | **217.54** | **769.38** | **this run** |

⇒ **1 cent apart on NVDA, 3 cents on SPY.** A path the 08-29 run never tried lands on its corroborated
value. ⚠ **This is still not `D5` satisfied** — all three are `yfinance`. It is *three surfaces of one
provider*, and I am not upgrading it to cross-provider corroboration (§12).

### 11b 🚨 I inherited *"the ghost bar is the KR bug"* and the measurement refused it
The natural reading of the inheritance — KR ghosted on 08-29, US ghosted on 08-30, same signature —
predicts the **same locus**, i.e. the bench. The KR run proved its case by swapping the bench and
watching `rs20/rs60` come back. **I ran that exact experiment and it did not reproduce**: trimming SPY's
ghost row alone left `rs20`/`rs60` NaN on NVDA, XOM, LLY, GOOGL and JPM. **Both** sides had to be
trimmed. ⇒ **the transfer was wrong and is written down rather than quietly corrected**; PREFLIGHT
§G0(b) carries the falsification in full.
★ **The second-order finding is the one worth keeping**: `obv_norm` also moves under the repair
(NVDA −0.020 → +0.036), because the ghost row carries **real volume with a missing close**. A defect
described as "the close is missing" is in fact **also a volume-signed-wrong defect**, and `D6` already
grades OBV as a C-signal.

---

## 12 · Failed lookups this stage (per the unattended-run rule)

| lookup | result |
|---|---|
| **Stooq** (`https://stooq.com/q/d/l/?s={spy,nvda}.us&i=d`) — attempted as the `D5` second provider | **Not a 404 this time** — the host now returns a **JavaScript proof-of-work challenge page** for every symbol. ⇒ **abandoned deliberately**: solving it would be bot-detection circumvention, which this desk does not do. **`D5` unmet — stated, not glossed.** ⚠ And the failure *changed shape* since 08-29 (404 → challenge), so "Stooq is down" is the wrong carry; **"Stooq is closed to us"** is the right one |
| `yf.download` daily `Close` for **2026-08-28**, all US names | **NaN, 301/301.** Not a lookup failure but a provider defect — recorded as G0 and **recovered** via the 5m route (§11a), not carried as a gap |
| `module_chart` on `NVDA`/`ANET`/`SPY` | **exit 1, 0/3** — downstream of the same defect. No US chart citation this run (G7) |

---

## ✅ EXIT CHECK
- [x] Shared spines (`STANDING_VIEW.md` §1/§5/§6, `SCENARIOS.md` master log + index) + `STANDING_VIEW_US.md` §3a + `SCENARIOS_US.md` + `RESEARCH.md` read; **`SCENARIOS_KR.md` opened** and confirmed to hold no past-dated row this run must score (§2e). `module_report_tags show` cross-queried (§6).
- [x] **Retracted ledger read BEFORE today's view formed** (§1c). `R103`·`R108`·`R89`·`R106`·`R107` all handled; ★ `R103` is the one today's data touches, and the new measurement is filed as **`D412`** rather than being used to quietly re-adopt a retracted claim.
- [x] **Every past-dated scenario scored or named with a reason** (§2a–§2e). **Zero due, zero silent skips.** `S8` named for a **32nd** run. The 08-29 run's seven verdicts **verified present in the ledger**, not re-scored.
- [x] `reject_ledger.py due` run — **0 due, 0 legacy** of 251 (§3). Not substituted with `score`.
- [x] `missed_ledger.py due` run — **0 due, 0 legacy** of 269 (§3). Signs not summed. `C22` records that a clean legacy count does not detect an unfireable condition.
- [x] **Exposure state read and carried** (§4): 정상 · target 95% · current **85.5%** · gap **−9.5pp** · cumulative **−11.68pp = cash −5.94 + selection −5.74, n=16 — third run unmoved**. Not a cold start; `C4` stated.
- [x] 🚨 **Instrument health inherited before any number was trusted** (§0) — `PREFLIGHT.md` exists, written by this run's Stage −1. Six FAILs converted into explicit removed rights, **and one FAIL converted into a conditional right** (G0's proxy, with its measured error).
- [x] **Claims asserted and then refuted are written down, not edited away** (§11b — the KR-locus transfer I inherited and falsified); the check that **survived** is reported too (§11a).
- [x] Stale rows flagged with `asof` (§1e, §7); `D295` carried as a dig for a 5th run; the 08-28 contaminated stretch **not retro-cleaned**, and the fact that it is now readable by another route is stated as a forward permission, not a retro-correction.
- [x] `[measured]`/`[inferred]` preserved on every carried claim; the `[inferred]` regime call is explicitly barred from being cited as evidence (§1b).
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L, with the stages they bind named** (§9) — including the one that is **unmet** (`D5`).
- [x] `HANDOVER.md` written. `handoff/*.md` writeback happens **at run end** — and §1a is exactly why this run will verify **both** targets separately, not one.
- [x] **No position sizing and no buy/sell language anywhere above** (P4).
