# HANDOVER — industry_US · 2026-08-31 (Mon) · Stage 2 / L1·HANDOVER

> Runtime `--market us`. Inheritance step: read the carry BEFORE forming any view.
> Run clock **KST 22:09–22:5x = ET 09:09–09:5x, Monday, PRE-OPEN.** The 08-31 US session had not
> begun when this stage executed. Last completed US session **Fri 2026-08-28**.
> IDs issued by `module_evidence next-id` (M1125–M1144 · D426–D433 reserved; highest existing
> **M1124** / **D425**), not hand-grepped.

---

## 0 · Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-08-31/industry_US/preflight/PREFLIGHT.md` **was run** (protocol `preflight`), this
run, before this stage. Verdicts: **G0 🔴 · G1 🔴 · G2 ⚠PASS(idling) · G3 🔴 · G4 🔴 · G5 🔴 · G6 🔴 ·
G7 🔴.** The binding consequences this stage carries forward into every later stage:

| Revoked today | Which stages it binds |
|---|---|
| Any number in the **primary** `SECTOR_FLOW_US.json` (empty, `scored=0`) | SWEEP · ROTATION · DEEP · BET |
| `wflow`-based **promotion or demotion of IT, Energy, Consumer Discretionary** — one name owns each sign | ROTATION §2 |
| **News velocity / theme freshness / "sector X is quiet"** *sourced from the sweep* (15.72% coverage; 8/8 direct re-probes alive) | SWEEP · ROTATION · EVENT_ALPHA · DEEP |
| **08-28 closes from the daily endpoint, `module_paper_book status`, or `pulse`** — those print **08-27** under a current-day label | every stage |
| **US chart shape/pattern** (`module_chart` 0/3 live tickers) | DEEP · BET |
| **Concentration as a single number** (G4) · **cap-weighted "current size"** (G5, universe 47d stale) · `kelly_size --ic` as evidenced (G6) | SIZE · BET · ALPHA |
| **Anything about the 08-31 tape** — the market had not opened | every stage |

**Granted today, with a mandatory label on the same line as the number:**
- the **08-28 session via the 5m proxy** (err **0.0181% mean / 0.0448% max**, n=24) — label
  `5m-proxy close (err ≤0.05%)`;
- **`SECTOR_FLOW_US_REPAIRED.json`** (299 scored, 3-axis nonews, asof 08-28) — label `repaired sweep`;
- **Δflow vs the 08-27 snapshot** (299/299 common names, same `nonews` mode) — label
  `repaired sweep, 08-27 → 08-28`;
- **direct** news queries (≤11 consecutive, ~90 s pause if refused).

★ **`M1125` [measured] — the ghost bar is now T+3 and did not heal across a weekend.** 08-28 Close
`NaN` for **301/301** tickers in a cache downloaded today; 08-24/25/26/27 all **0/16**. On 08-30 this
was honestly loggable as a transient; it is now a **standing hole**, and the desk should plan for it
to be there tomorrow rather than wait it out.

★ **`M1126` [measured] — the repair reproduced independently to ≤0.002 on 11 of 11 sectors.**
Rebuilt today from a fresh cache by a freshly written script with no reference to the 08-30 output:
Materials +0.225/+0.225 · IT +0.034/+0.033 · HLTH +0.021/+0.021 · FIN −0.072/−0.072 · ENRG
−0.097/−0.097 · DISC −0.262/−0.262 · STPL −0.264/−0.264 · INDU −0.317/−0.317 · RE −0.338/−0.338 ·
COMM −0.424/−0.422 · UTIL −0.548/−0.549. Two independent reconstructions of one session agreeing is a
better warrant for the proxy than a single run's internal error estimate.

---

## 1 · Inherited standing view

### 1a. Regime call — carried unchanged, `[inferred]`, still barred from citation as evidence
The 08-30 asof-chain entry carries the regime call with its `[inferred]` tag **intact and explicitly
barred**, and records its first dated public challenge (Micron's CEO, 08-24 and 08-28: the memory
cycle's boom-bust playbook is breaking). **`P111` (settles 09-14) is the registered test.** This stage
does not move the call and does not cite it.

### 1b. Sector verdicts carried in from 2026-08-30
`FIN OW−` · `HLTH OW` · `COMM OW` · `MATR OW` · `IT N` · `ENRG N` · `STPL N` · `DISC UW` · `INDU UW` ·
`RE UW` · `UTIL UW`. DEEP that run: continuous `[MATR, HLTH]`, rotating `[FIN, COMM]`, PREMORTEM-promoted
`[IT]` = 5 slots. **These are inherited, not re-derived here** — ROTATION owns the verdicts.

⚠ **Three of the eleven cannot be re-argued on `wflow` today** (PREFLIGHT G3): IT, Energy and
Consumer Discretionary each have their sign owned by one name (NVDA 19.4% · XOM 30.5% · AMZN 40.2%).
⚠ **`D424` (registered by the KR desk today) applies to this board and was checked**: a
`top1_flips_sign=False` bucket can still be a one-name story in the *opposite* direction. Checked on
the repaired file — **Materials passes the check honestly**: `wflow +0.225` with `top1 LIN` and
`ex-top1 +0.233`, i.e. LIN is a mild *drag* and the positive is broad (0 reds in 12 names). **Health
Care is the one to watch**: `wflow +0.021` vs `ex-top1 +0.095` ⇒ **LLY is dragging a sector that is
materially more positive underneath it**, which is the `D424` shape with the sign the guard does not
look for.

### 1c. Retracted ledger (§5) — read BEFORE forming today's view
Read in full through the tail. The entries that bind this run:

| id | what may not resurface |
|---|---|
| **`R110`** (08-30) | "The foreign news ingest has been dark for two days." **The server was current; the client mirror was 38 h stale.** ⇒ any "the news went quiet" claim must first state which side was queried. Hormuz reads **0.80 (fading)**, not 1.04 |
| **`R111`** (08-30) | "`MU` has no take-or-pay and the desk's take-or-pay frame does not transfer to memory." **Killed by a superseding filing** — the FY26Q3 10-Q describes take-or-pay with binding volumes, a ceiling and a floor. ⇒ the frame **does** transfer; a decelerating QoQ under a dated ceiling is arithmetic hitting a cap, not demand |
| **`R112`** (08-30) | "`GOOG` is missing from the per-name JSON." False — `GOOG` is present and is COMM's worst row; the 13th row is `EA` (`flow_score: null`) |
| **`R113`** (08-31 KR) | "KRX has not yet traded Jackson Hole." Killed by 08-28 domestic primary reporting. ⇒ do not assume a KRX-side event is unpriced because the speech post-dated the close |
| **`R114`** (08-31 KR) | A PREFLIGHT sentence retracted **by the run that wrote it**, because command order was reconstructed from memory rather than file mtime. ⇒ **`D400-KR`: reconstruct observation times from mtime.** ✅ **Complied with this run** — PREFLIGHT's timeline was written from the actual command sequence in one session with no background reordering, and the two background jobs (sweep, embed sync) are named with their own log files |

⚠ **`R89` + `P83` still bar any refining-margin-vs-barrel separation claim** — relevant because `MPC`
and `PSX` are again the book's two best 08-28 names (+1.47% / +1.76%, 5m-proxy close, err ≤0.05%).

### 1d. Open contradictions carried, NOT resolved
- **`C21`** — the RSI convention question, untouched again. ⚠ Related measured defect stands:
  `us_setup_screener`'s loader drops the void bar, so **any RSI it prints is computed to 08-27**.
- **`C22`** — the two ledgers name different hands; the `HII` revival condition observes our own
  builder rather than the market. **No new sample: both `due` runs returned 0 rows today.**
- **`C23`** — **two books, and every stage reads whichever one its tool opens.** ★ **Reproduced with
  fresh numbers this run, and it is now the largest un-owned figure on the sheet** (§4).
- **`C24`** — Materials' flow axis and its positioning axis point opposite ways
  (`eqflow` rank 1, zero reds in 12, against copper spec net at the 100th percentile of its year).
  **Reproduced today**: Materials is again rank 1 (`wflow +0.225`, `eqflow +0.164`, 0 reds/12).
  ⚠ Not resolved by picking a side.
- **`C25`** (new, KR-registered 08-31) — the desk's two instruments read OBV's **sign** oppositely on
  one name. Carried; the US analogue is untested.

---

## 2 · Scenario scoring — every past-dated row named

### 2a. 🚨 Zero rows scored this run, and the reason is structural, not a skip

★ **`M1127` [measured] — this desk fires PRE-OPEN, so a row whose observable is "date D's US close"
can never be scored by the run dated D.** The task fires at **KST 22:09 = ET 09:09**, twenty-one
minutes before the NYSE open. Confirmed against the desk's own record: the 08-29 run described itself
as *"the first US run in four to have its own settle date behind it rather than ahead of it"* and
scored `S116`/`S118` off the **08-28** session, not its own date. ⇒ **`D426`** (below). This is the
US-side generalization of the KR desk's `D402-KR`, which reached the same conclusion from the other
side of the clock eight hours earlier today.

### 2b. Rows settling **2026-08-31** — NOT DUE, not `EXPIRED`

| id | observable | status |
|---|---|---|
| **`S92`** | Mandatory Hormuz bracket (3 branches) · settle 08-31 | **NOT DUE** — needs the 08-31 settled close; the session had not opened. Scoreable on the **09-01** run |
| **`S94`** | The cycle registry cannot see the cycles this desk finds · settle 08-31 | **NOT DUE** — same |
| **`S103`** | `NVDA` 5-session excess vs `SPY`, first settled close on/after 08-29 ⇒ **08-31** | **NOT DUE** — same. ⚠ **Not `EXPIRED`**: 08-29 was a Saturday and the `on/after` clause moved it. ⚠ Pre-settle read carried and **explicitly not a score**: the 08-29 run reproduced the KR preview at **+1.6630pp** |
| **`S104`** | (title still carries the `R106` date defect — July PCE printed 08-26, not 08-28) | **NOT DUE** — settle is later and no threshold is touched |
| **`S112`** | Mandatory Jackson Hole bracket, owns the PCE print inside its window · settle 08-31 | **NOT DUE** — same |
| **`S124`** | Cross-sectional count of `us_top300` IT names with positive `exc5` vs `SPY` · settle 08-31 | **NOT DUE** — same. ⚠ It is the **only cross-sectional row** on this date and **branch B is the branch that vindicates the desk's own `IT` underweight**, stated so a `C` is not later read as a win |
| **`S131`** | ★ **The mandatory ≤48h bracket** — MSCI 08-31 rebalance, `RSP` − `SPY` 1-session excess, A ≥ +1.30pp / B ≤ −1.30pp | **NOT DUE** — the rebalance prints into today's close, which has not happened. **The row is armed and correctly placed; the desk simply cannot observe it yet** |

⚠ **`D242` complied with**: no threshold was adjusted to make any of these seven scoreable early, and
no pre-settle read is recorded as a verdict. ★ The desk's own §E observation from 08-29 is carried
verbatim as the reason: **"a pre-settle read is not a weak version of a verdict; on this desk's record
it has been an inverted one"** — three for three (`S101`, `P78`, `P96`).

### 2c. Rows blocked on `[FRED]` — re-measured today, still unreadable

★ **`M1128` [measured] — the FRED H.15 dailies are stalled at 08-27 for a third calendar day, and
the stall is *partial within one release*.** Pulled `module_macro_us --days 30 --json` at 22:2x KST:

| series | last obs | value |
|---|---|---|
| `DGS2` · `DGS5` · `DGS10` · `DGS30` · `DFF` | **2026-08-27** | 4.20 · 4.38 · 4.67 · 5.19 · 3.63 |
| `DFII10` (real 10y) | **2026-08-27** | 2.34 |
| `VIXCLS` | **2026-08-27** | 14.51 |
| `BAMLH0A0HYM2` (hy_oas) · `BAMLC0A0CM` (ig_oas) | **2026-08-27** | 2.63 · 0.79 |
| **`T10YIE` (breakeven 10y)** | **2026-08-28** | **2.31** |
| `RRPONTSYD` · `SOFR` | **2026-08-28** | 0.175 · 3.65 |
| `DTWEXBGS` (dollar index) | **2026-08-21** | 118.0628 |

★ **`T10YIE` is arithmetically `DGS10 − DFII10`. It carries 08-28 while both of its own constituents
stop at 08-27** — so the upstream values exist and the published set is internally inconsistent.
That is a *different* defect from "the release is late", and it matters because **`S120`'s observable
requires BOTH `DGS30` and `T10YIE` to carry 08-28** and was written expecting them to arrive together.
⇒ **`D427`** (below).

| id | requirement | today's read | status |
|---|---|---|---|
| **`S120`** | first observation where **both** `DGS30` and `T10YIE` carry 08-28 | `T10YIE` ✅ 08-28 · `DGS30` ❌ 08-27 | **ARMED**, not `EXPIRED`. ✅ the row's own observation-lag clause working as designed, 2nd consecutive run |
| **`S111`** | `ig_oas` close covering 08-28 | ends 08-27 = **0.79** | **ARMED**. ⚠ pre-settle disclosed: 0.79 sits in **C**, **2 bp above B** (A ≥ 0.85 / B ≤ 0.77) — 🚫 **not** to be inherited as "C fired" |
| **`P67`** | `hy_oas` ≥ 2.85% | ends 08-27 = **2.63** ⇒ **22 bp below** | **ARMED**, disclosed not scored |
| **`P86`** | PCE conjunct **met**; rate conjunct on `DGS2` | 4.20 @08-27 vs A ≤ 4.10 / B ≥ 4.32 | **ARMED** |
| **`P97`** | joint date on `DTWEXBGS` | ends **08-21** = **10 days behind**, widened from 9 | **ARMED**. ★ **`D333`'s 13th reproduction**, and the lag is still growing run over run |

### 2d. Named again rather than dropped
- **`S8`** — ⛔ **unscoreable for a 33rd consecutive run**; date field still `[blank]`. A human must
  `VOID` it or re-register it with a date (P5). **Named, not dropped.**
- **`S3`** (~2026-09/10) · **`S4`** (~2026-09 late) — dates unparsed by design; not due.
- **KR-owned rows** — zero due (the KR run proved its own zero by grep this morning; earliest
  `S67-KR` is 09-04).
- Not yet due: `S109`(FRO, 09-02+) · `S126` · `S127` · `S128` · `S129` · `S130` · `S132`–`S135` ·
  `P81` `P85` `P87`–`P89` `P114`–`P117`.

**Total: 0 scored · 7 not-due-by-clock · 5 blocked on `[FRED]` · 1 unscoreable (`S8`) · 0 silent skips.**

---

## 3 · Both ledgers audited — symmetric, per `carryover.md` §3c

| ledger | rows | resolved | **legacy (no revival/entry condition)** | **due today** |
|---|---:|---:|---:|---:|
| `reject_ledger.py due` | 259 | 151 | **0** | **0** |
| `missed_ledger.py due` | 277 | 157 | **0** | **0** |

★ **`M1129` [measured] — the legacy count is 0 on both sides, which is the evidence the practice took
hold.** `carryover.md` warns that a clean `due` run is not proof of health and that only a **shrinking
legacy count** is. It has reached zero on both ledgers: every one of the 536 rows now carries a
condition and a date. ⇒ **the "24 of 25 rows had no `revives_if`" state that cost +41.2pp and +26.9pp
on one name is fully closed.** Nothing is being carried forward unexamined this run.
⚠ **The signs are inverted between the two ledgers and are not summed.**
⚠ `missed_ledger score`'s first 6 rows remain a seeded, outcome-selected block — quoted as
*accumulation*, never as an edge.

---

## 4 · Exposure state carried as size context — and it exposes `C23` again

**Not cold-starting**: `exposure_rule.py show` returns **44 rows**, most recent **2026-08-31**.

| | value |
|---|---|
| rule state | **정상 (normal)** — no firing condition |
| target invested | **95%** |
| **actual invested (08-31 row)** | **85.3%** ⇒ **band gap −9.7pp**, the 12th consecutive session outside the band |
| cumulative decomposition (n=17) | **total excess −12.51pp = cash −5.88pp + selection −6.63pp** |
| alarm | 🚨🚨 `ARMED (TIMEFOLIO_EXECUTE=1)` |

⚠ `exposure_rule.py state` printed **"투자비중 미상"** (no account query) while `show` has the number —
the verdict line and the ledger line disagree about whether the weight is known. Reported as read; not
substituted (P5).

### ★ `C23` / `D415` — reproduced with today's numbers, and the un-owned figure is now the cash

**`M1130` [measured].** The three instruments this stage ran name **three different books**:

| instrument | book it read | invested | names |
|---|---|---|---|
| `module_paper_book status` | **paper** | — | **13** (11 US + `028050`, `316140`) |
| `cycle_exposure.py` | **real KIS** | **$5,188.76 of $11,045.42 total** | **5 US** tagged (`NVDA`·`ANET`·`ETN`·`MPC`·`PSX`) + `RTX` |
| `exposure_rule.py show` | **KR contest / timefolio** | **85.3%** | — |

⇒ **the real US account is 53.0% cash** ($5,857 of $11,045 un-invested) at the same moment the
exposure instrument reports **85.3% invested against a 95% target**. **Those two numbers are about
different books and neither output says so.** `PREFLIGHT G5` again validated the universe against the
**paper** book (11/11) while `cycle_exposure` again audited the **real** account. The 08-30 finding
that **`T` (~13.6% of real invested capital) is owned by no thesis** is carried **unresolved** — `T`
does not appear in `CYCLE_EXPOSURE.json`'s name lists at all, so it is still invisible to every
instrument except the balance call.
⚠ **Which book is authoritative for research is a human call (P5).** Not resolved here.
★ **For BET/ALPHA**: *any* sizing sentence this run must name its book on the same line. The two
answers to "how much room is there" are **53% cash** and **−9.7pp under a 95% target**, and they are
not reconcilable inside this run.

**`M1131` [measured] — no top-rank cycle GAP on the real book.** AI-compute epicenter **16.91%**
(need ≥12.0, margin +4.91pp, `NVDA`+`ANET`, `ETN` adjacent) · Energy/refining **10.17%** (need ≥8.0,
margin +2.17pp, `MPC`+`PSX`) · Missile-defense **3.82%** (no threshold set). ⚠ Per `C23` this verdict
**applies to the real book only**, and per `D416`/`D250` the registry still has **no AI-power/grid
ranked row** and **no optical row**, so "0% exposure" is unstatable for those, not measured as zero.

---

## 5 · Signal scoreboard — one cell changed state, and W1 forbids acting on it here

`axis_inflection.py` ran (16 axis files); `ic_ledger.py log` accrued **0 new rows** (`총 1014행 ·
market=kr` — **still KR-only**, `D395`'s condition unchanged); `ic_ledger.py score` read.

★ **`M1132` [measured] — `vol_surge` at h=1 now CLEARS Bonferroni for the first time.**

| axis | h | n | n_eff | mean IC | t(NW) | positive | verdict |
|---|---:|---:|---:|---:|---:|---:|---|
| **`vol_surge`** | **1** | **40** | **40.0** | **−0.0400** | **−3.32** | 28% | ★ **significant, passes multiple-comparison (|t| > 2.8)** |
| `vol_surge` | 5 | 35 | 7.0 | −0.0365 | −2.12 | 34% | significant on a standalone bar only |
| `obv_norm` | 5 | 35 | 7.0 | −0.0597 | −2.17 | 29% | standalone only |
| `flow_score` | 1 | 40 | 40.0 | −0.0375 | −1.36 | 45% | indistinguishable |
| `rs20` | 1 | 39 | 39.0 | −0.0421 | −1.23 | 44% | indistinguishable |

The standing item said *"do not flip the gate until it clears Bonferroni."* **It has now cleared** —
`n_eff = 40` (non-overlapping, h=1), sign **negative**, agreeing with **M224**, **while `sector_flow`
still weights `vol_surge` positively in its 🟢 verdict.**

🚫 **And this run may not act on it.** The ledger is **`market=kr`**. Flipping a **US** gate on a **KR**
measurement is precisely the `W1` cross-market-transfer violation this repo keeps logging — the same
reasoning that kept the US DEEP budget at **N=4** when `industry_kr` cut to N=2. ⇒ **the observation is
carried, the gate is not touched, and the prescription is `D428`: the US desk needs its own
`ic_ledger` before this can bind here.** (`D395` is thereby escalated from "still KR-only" to "now
blocking a result that has actually arrived".)
⚠ 14 of 21 cells remain unquotable (`n_eff < 4`); `필요n` is not quoted for any cell with `n < 10`.
⚠ Regime label for the window: a hawkish-repricing stretch (Warsh 08-28), not a crash window.

---

## 6 · Stale-check

| carry | age at this run | action |
|---|---|---|
| Sector verdicts (08-30) | **1 run**, and **zero new US settled sessions** since | fresh enough to inherit; ROTATION re-derives on the repaired sweep |
| Regime call `[inferred]` | carried since before 08-30, tested by `P111` (09-14) | carried, not cited |
| `us_top300.csv` | **47 days** | 🚫 cap-weight may not be called "current size" (G5) |
| `DTWEXBGS` | **10 days** behind | `P97` unreadable; `D333` 13th reproduction |
| H.15 dailies | **3 days** behind | five rows blocked (§2c) |
| `cycle_registry.json` | no ranked AI-power row (`D416`), no optical row (`D250`, **16th run**) | "0% exposure" unstatable for both |
| **Suspensions whose clearing date has passed** | **none found** | — |
| Contaminated stretch: the **2026-08-28 daily-close bar** | registered 08-29 | ⚠ **not retro-cleaned**; prior runs' figures keep their note |

---

## 7 · Dig list ranked for today (candidate DEEP / stage assignments)

**New this run:**

| id | dig (positive form) | measured origin |
|---|---|---|
| **`D426`** | ★★ *A scenario observing date **D**'s US close is registered to settle **D+1**, with the KST hour it becomes observable written beside it.* | `M1127`: this desk fires **09:09 ET, pre-open**. **Seven rows** (`S92`·`S94`·`S103`·`S104`·`S112`·`S124`·`S131`) all sat "due today" and **none could be read**, including the run's own mandatory ≤48h bracket. US-side twin of `D402-KR` |
| **`D427`** | ★ *A row requiring **two** FRED series on the same date checks whether they publish together, and names a fallback if one is derived from the other.* | `M1128`: **`T10YIE` carries 08-28 while `DGS10` and `DFII10`, the two series it is computed from, stop at 08-27.** `S120` needs `DGS30` **and** `T10YIE` together and is blocked for a 2nd run by exactly this split |
| **`D428`** | ★★ *Before a US gate is changed on an axis result, the run states which market's `ic_ledger` produced it; a KR-only cell may be reported but may not move a US gate.* | `M1132`: **`vol_surge` h=1 cleared Bonferroni (t −3.32, n_eff 40)** — the first axis result strong enough to act on, and it is `market=kr`. Escalates `D395` from a note to a block |
| **`D429`** | *A ghost/void bar that survives **two** runs is recorded as a standing hole with a patch-at-the-reader prescription, not carried a third time as a transient.* | `M1125`: the 08-28 `Close = NaN` survived a full weekend, 301/301, and the second run's honest response was still to rebuild the same scratch patch from zero |
| **`D430`** | *A run that reports "0 scored" states, in the same line, how many rows were **not due** vs **blocked** vs **unscoreable** — a bare zero cannot be told apart from a skip.* | This run scored 0 for the 2nd consecutive time; the composition (**7 / 5 / 1**) is the informative part, and the 08-30 run's "zero" carried the same ambiguity |

**Carried, unmet, with run counts:** `D250` optical registry row — **16th run** · `D333` `DTWEXBGS`
lag — **13th reproduction, now 10 days** · `D379` PREFLIGHT reads §5 first — **5th run unwired** ·
`D394` standing-view writeback — both halves verified separately this run · `D395` — **escalated to
`D428`** · `D411`/`D412` news-axis instrumentation — **unaddressed; today's 8/8 direct probe is a
3rd reproduction of the underlying fact** · `D415` two books — **reproduced with fresh numbers (§4),
still human-owned** · `D416` AI-power ranked row · `D418` mirror-cursor gate — **partially executed**
(cursor read **2026-08-31T08:03:31**, set by this morning's KR run ⇒ **14 h stale**; `embed sync` run
this stage per the MACRO L2 spec — the step `R110` says the 08-30 run skipped — pulling **5,363
received / 5,346 newly embedded**, 543,000 total, cursor now **2026-08-31T22:07:10**. ⚠ The gate's
*other* half, comparing against the remote index's newest article date, is still not automated) ·
`D420` `AVGO` 09-02 vs 09-03
calendar mismatch — **still open, and `S132` is armed on the disputed date** · `D421` `action_bracket`
window mismatch · `D422` `drift_watch` anchor · `D424` — **checked against today's board (§1b)** ·
`S8` — **33rd run unscoreable**.

**Ranked as candidate DEEP mandates for this run** (ROTATION owns the final picks):
1. **Health Care** — `D424` shape with the sign the guard misses: `wflow +0.021` vs `ex-top1 +0.095`
   (LLY dragging a broader positive). It is also a continuous-track slot and `S133` settles 09-14.
2. **Materials** — `C24` is now reproduced twice (rank 1 on flow, copper spec net at the 100th
   percentile). The contradiction is the mandate, not the ranking.
3. **IT** — three of the four flipper/one-name problems live here, and `S124` (settling on the next
   run) tests the desk's own IT underweight cross-sectionally.
4. **Financials / Communication Services** — rotating-track carry from 08-30; `S134` settles 09-04.

---

## 8 · ≤48h binary catalysts injected at run start (protocol requirement)

`catalyst_calendar.py --days 5` → **3 binaries in window**:

| when | event | bracket status |
|---|---|---|
| **D-0 · 2026-08-31** | **MSCI quarterly review** (STRUCTURAL, passive volume concentrates on the effective close) | ✅ **owned by `S131`** (ARMED, `RSP` − `SPY` 1-session excess, ±1.30pp). The mandatory ≤48h obligation is **already satisfied by an armed row**; issuing a second would re-freeze a live threshold (`D242`) |
| **D-2 · 2026-09-02** | **`AVGO` earnings** | ✅ **owned twice** — `S132` (±9.00pp, settles 09-03) and `S127` (09-08). ⚠ **`D420` unresolved**: the issuer's calendar says **09-03**, `catalyst_calendar` says **09-02** |
| **D-4 · 2026-09-04** | **August NFP** | ✅ spanned twice — `S126` (five sessions in) and `P114` (five sessions out) |
| undated | Iran "Strait of Hormuz open" (TACO trigger) | spanned three ways (`P107`·`P112`·`P117`); **`S8` itself remains dateless, 33rd run** |

⇒ **PREMORTEM (Stage 7) inherits: every binary in the window already carries a both-sides bracket.**
A one-way tilt into any of them would be a protocol violation, and the rows to check against are the
ones named above.

---

## ✅ EXIT CHECK
- [x] Shared spines read (`STANDING_VIEW.md`, `SCENARIOS.md`) plus this desk's `STANDING_VIEW_US.md`,
      `SCENARIOS_US.md`, `RESEARCH.md`. **`SCENARIOS_KR.md` opened** to confirm the KR side's zero-due
      claim rather than inheriting it. Mechanical ledger cross-queried (`module_report_tags show`).
- [x] **Retracted ledger read before forming today's view** (§1c). No claim in this run matches a
      retracted entry; `R110`'s prescription (`embed sync` before reading `brief`/`thread`) was
      **executed** this stage rather than skipped.
- [x] **Every past-dated scenario scored or explicitly named with a reason.** 0 scored ·
      7 not-due-by-clock · 5 `[FRED]`-blocked · 1 unscoreable (`S8`, 33rd) · **0 silent skips**.
- [x] `reject_ledger.py due` run — **0 due, 0 legacy**. `missed_ledger.py due` run — **0 due,
      0 legacy**. Signs not summed. **Legacy count reported and it is not flat: it has reached zero.**
- [x] Exposure state read and carried (§4), **not cold start** (44 rows), band gap **−9.7pp**, and the
      book contradiction it exposes is named rather than averaged.
- [x] **Instrument health inherited before any number was trusted** (§0) — `PREFLIGHT.md` was run this
      run and every FAILED gate's revocation is written into this file as a binding constraint.
- [x] Method rules loaded as constraints: **C5** (arbitrary threshold — `D424` check, G4 windows),
      **D5** (cross-provider — inherited as met at index and name level on 08-28, `M1091`/`M1099`),
      **D6** (OBV is C-grade), **W1** (the `vol_surge` result is NOT transferred), **S1/S5**
      (`n_eff`, short samples), **D48** (nothing edited; `M1125` appends to the T+1 reading rather
      than rewriting it).

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **MACRO** (Stage 3).
> ⚠ MACRO inherits: `[FRED]` H.15 is 3 days stale with a partial-publication split (`M1128`);
> `embed sync` has been run this stage; the 08-28 tape is available only as a labeled 5m proxy.
