# HANDOVER — industry_US · 2026-09-06 (Sun) · Stage 2 / L1·HANDOVER

> Read before anything is decided. Inherits the **analytical carry**, not the coverage ledger.
> **Sources read this run.** Shared spines: `handoff/STANDING_VIEW.md` (§1 regime call, §2 chain head,
> §5 retracted ledger through the 2026-09-06 KR block, §6 open contradictions, the asof chain incl.
> the 09-05 US and 09-06 KR entries), `handoff/SCENARIOS.md` (master index, the un-split master
> scoring log, the dated settle queue, the 09-05 US and 09-06 KR blocks). This desk's halves:
> `handoff/STANDING_VIEW_US.md` (§2a/2b/2c fact rows + the §3a registry, 09-05 append in full),
> `handoff/SCENARIOS_US.md` (**scanned mechanically end-to-end — 152 row-blocks, every settle date
> parsed**, see §3b). Method: `handoff/RESEARCH.md` Parts A/B/C, `handoff/README.md`.
> **Other-market file opened**: the 09-06 `industry_kr` blocks in both spines, for `R130`–`R133`,
> the settle-queue confirmation, and the KR-independent replication of this desk's news-tunnel finding.
> Prior-run reports opened as primary sources: `llm_outputs/2026-09-05/industry_US/HANDOVER.md`
> (the fold-in provenance) and `llm_outputs/2026-09-02/industry_US/MACRO_REPORT.md` §D (the frozen
> observables of `P125`·`P126`·`P127`·`P128`).
> Mechanical ledger cross-queried: `module_report_tags show` — **81 reports · 303 names · 12 sectors**,
> refreshed 2026-09-06T09:24 by the KR run.
> ⚠ **Read honestly**: the spines total **3.6 MB**. §1–§6 of `STANDING_VIEW.md` were read as structure
> plus targeted extraction, not linearly; the per-run append blocks were read in full for the two most
> recent runs (09-05 US, 09-06 KR) and by header index before that. `SCENARIOS_US.md` was read
> **mechanically in full** (parser, not eye) plus in prose for every row named below. This is stated
> because "read the spine" and "grepped the spine" are different claims and the file is now large
> enough that the difference matters — registered as **`D528`**.
> **P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.**

---

## 0 · The carry state — the 09-05 pre-commitment was checked, and it is **PARTIALLY** met

The 09-05 run wrote, in its own §0: *"This run pre-commits to the writeback at run end and names it
here so the commitment is checkable."* **It is checkable, so this run checked it.**

| target | 09-05 US run wrote? | evidence |
|---|:--:|---|
| `handoff/STANDING_VIEW.md` §5 retracted (`R129`) + §6 (`C29`) + asof chain | ✅ **yes** | file mtime 09-05 23:33; block at line 4097 |
| `handoff/STANDING_VIEW_US.md` §2a/2b/2c (`M1281`–`M1327`) + §3a registry (22 names) | ✅ **yes** | mtime 09-05 23:37; block at line 1394 |
| `handoff/SCENARIOS_US.md` new brackets `S145`·`S146`·`S147`·`S142-ANNEX` | ✅ **yes** | mtime 09-05 23:08 (written **inside** PREMORTEM, per that run's own decision #6) |
| `handoff/SCENARIOS.md` **MASTER INDEX** rows for the four new brackets + settle queue | ✅ **yes** | block at line 2448 |
| `handoff/SCENARIOS.md` **MASTER SCORING LOG** — the 8 folded verdicts + 1 VOID + `P101` | 🚨 **NO** | **no scoring-log block was appended by the 09-05 US run at all** |

★★ **So `D490` did not reproduce in its gross form — three of four files were written — but it
reproduced in a sharper one: a writeback that fills the INDEX and skips the LOG.**

- `P101`'s `FIRED-C` reaches `SCENARIOS.md` **only inside the KR desk's 09-06 prose** (line 2510,
  *"the 09-05 US run scored it"*) — a sentence about a verdict, not a verdict row.
- **`S110`'s VOID has no verdict line anywhere in `SCENARIOS.md`.** Its master-index row (line 1091)
  still reads **`ARMED`**.
- The other eight (`S109`·`S105`·`S106`·`S107`·`S114`·`S132`·`S138`·`S141`) appear in the log only
  inside the **KR desk's 09-05 §B finding** — a paragraph that deliberately *names* them without
  copying them (`D464-KR`: never overwrite another desk's row) and hands the fold-in to the next US
  run. **This run is that run.**

⇒ Filed as **`M1352`** and **`D529`**: *a per-run writeback is not one act but four, and the
scoring log is the one that gets dropped, because it is the only one that requires transcribing
another stage's output rather than appending the current stage's.*

⇒ **Action taken inside this stage, not deferred** (following the 09-05 run's own precedent for
`S145`–`S147`, and because `D490`/`D504`/`D529` are three of this run's dig items): the nine folded
verdicts and `P101` are transcribed into the master scoring log **now**, and the four `D504`-class
propositions are written into the master index **now**. See §3d. **Transcription, not re-scoring
(`D242`).**

---

## 1 · Instrument health inherited FIRST (`preflight/PREFLIGHT.md`, written 22:09–22:19 KST)

**PREFLIGHT ran and exists.** Its verdicts govern every number below.

| gate | verdict | what it removes from this run |
|---|---|---|
| **G0** | ✅ **PASS — third consecutive clean run** (1/301 NaN on all 14 sessions, `EA` only; **partial-NaN names 0**) | nothing, except any verdict on **`EA`** |
| **G1** | 🔴 sweep news axis **16.72%** (50/299) · ✅ direct path 6/6 · ★ mechanism replicated a 3rd time | 🚫 no theme-freshness / velocity / "it is quiet" **from the sweep**, *including* the 50 that scored — they are the 50 largest caps |
| **G2** | 🟡 **scale continuous, NOVELTY ZERO** — `asof` 2026-09-04 == the 09-05 run's `asof` | 🚫 **Δflow may not be worded as "today's move"**; all 11 sectors are numerically identical to the 09-05 file |
| **G3** | ✅ full 11-row list printed (1 flipper by the flag; **2 by issuer**) | 🚫 no `wflow` verdict on **Cons. Disc.** (AMZN 40.2%) or **Comm. Services** (Alphabet 76.6% under two tickers) |
| **G4** | 🔴 **12 / 11 / 10** units across 250/500/750d | 🚫 no single-number concentration claim; `--days` on the same line |
| **G5** | 🔴 universe **53 days** stale (cover ✅ 11/11, missing 0) | 🚫 no cap-weight / sector cap share / `top1_w%` / issuer share cited as current |
| **G6** | 🔴 accrual **0.55/day, 1.8×** slow | `kelly_size --ic` is "mechanical 1/4" if used at all |
| **G7** | 🟡 **45/47** `--help` clean; chart live 3/3 | 🚫 no `margin_history` output |

★ **The one gate that MOVED, and it moved against this run.**
**`G2` flipped from a clean PASS to a split verdict.** The 09-05 run earned an unqualified Δ column
because both sides of the subtraction were post-heal. **Today the subtraction is not stale, it is
NULL**: today's `asof` and yesterday's `asof` are the same settled Friday, and the sector table
reproduces to the last decimal on all nine compared fields across 11 sectors. The `delta` column is
still the **09-03 → 09-04** change the 09-05 run reported. ⇒ **Filed as `M1353`. The rest of this run
must get its novelty from the non-price instruments, or it is restating Friday.**

★ **And the one that replicated hardest.** `G1`'s mechanism reproduced a third time with the wall
moving by exactly one slot — velocities at universe positions **0–49** today against **0–48**
yesterday, contiguous, zero gaps, zero exceptions — which converts the wall from a *fixed name list*
into a **volume threshold at ~100 queries**. Recovery clock: dead t+20/+40s, **alive t+60/+80/+100s
(3/3, identical count 3841)**. ★★ **The KR desk measured the same structure independently this
morning on a different universe and got a different constant** — `M1329-KR`: prefix **0–57**,
coverage **7.03%**. **Same mechanism, different constant, two markets, no import** (`W1` satisfied:
the KR *number* stays in KR; the *structure* is confirmed twice). Filed as **`M1354`**.

**Citable flow object today: the PRIMARY `SECTOR_FLOW_US.json`** (299 scored, 3-axis `nonews`, asof
**2026-09-04**), **with its Δ column labelled `09-03 → 09-04` and not otherwise.**

★ **Clock fact.** Sunday; NYSE closed Sat and Sun. Last settled session **2026-09-04**, complete.
`D74`/`D426` intraday contamination is structurally absent for a second consecutive run. ⚠ **And
tomorrow is not a session either — 2026-09-07 is Labor Day** (`D507`, measured by the 09-05 run and
carried by the KR desk this morning). **The next US settled close is Tuesday 2026-09-08.**

---

## 2 · Inherited standing view — carried unchanged unless MACRO measures otherwise

- **The repricing's LEG FLIPPED, and the flip is the freshest macro fact on the board.** `[measured]`
  `M1283`: the 3-session (Δ`breakeven_10y` − Δ`real_10y`) spread ran **−11.0 bp = the 5.2nd
  percentile (08-31) → +6.0 bp = the 88.5th (09-03)**. **Re-measured independently this run and
  reproduced exactly**: −11.0 (08-28) → −11.0 (08-31) → −8.0 (09-01) → −0.0 (09-02) → **+6.0 (09-03)
  = the 88.1st percentile of trailing 252** (p05 −11.0 · p15 −6.0 · p50 0.0 · **p85 +5.0** · p95 +9.0).
  ⚠ **+6.0 is ABOVE `P125`'s branch-A line of +5.0 — and it is a REFERENCE STATE, not a score**
  (§3c). `P121`'s policy-path frame is under live challenge from its own registered falsifier.
- **US credit sits at a one-year TIGHT while nominal yields print multi-decade highs.** `[measured]`
  `M1236`/`M1286`, re-pulled: `hy_oas` **2.65 (09-03) = the 2.0th percentile of 252** · `ig_oas`
  **0.81** · `NFCI` **−0.558** (08-28, weekly). Still the strongest fact standing against a FIN UW.
- **Energy's OW is a CHAIN-POSITION bet, re-specified to DISTILLATE.** `[measured]` `M1297`/`M1311`:
  distillate crack at the **95.6th** percentile, distillate−gasoline spread at the **98.4th**, QoQ
  distillate rate **accelerating +26.0 → +40.5** while the blended 3-2-1 decelerates. ⚠ Carried with
  its three named negatives (`M1312` Form 144 at 4.2×/2.9× base; `M1313` five-year-high op margins
  set on a **pre-spike** quarter; `M1322` both held refiners above consensus mean).
- **IT is not one bet, and the map of which half is weak is DATED.** `[measured]` `M1314` (sub-node
  spread **20.07pp** over five sessions against a ~−0.16% sector move ≈ **75×**), `M1315`/`M1282`
  (`P101` `FIRED-C` at −6.511pp with participation inverting 91.7%/16.7% → **21.1%/73.0%**; the
  5-session drag is **EDA + security software**, not semicap). `M1251` is **dated, not retracted**.
- **Utilities is two buckets under one label.** `[measured]` `M1316` — merchant power (`CEG`, `VST`)
  is the only positive-`rs20` pair; every regulated name carries `rs60` −6.5 to −20.6.
- **The AI-power lane's money is in GENERATION and leaving ELECTRICAL EQUIPMENT.** `[measured]`
  `M1317`/`M1301` — four of five components names 🔴분산 with rs20 negative at all five; the book's
  only lane holding is `ETN`, the lane's single distributing name. `S146` settles **09-14**.
- **Communication Services has been carried on a number wrong by ~0.66.** `[measured]` `M1206`/`D459`
  — **reproduced a 12th time today at 0.661** (G3): ex-both-Alphabet-classes `wflow` −0.389 → +0.272,
  with `eqflow` **−0.035** independently agreeing the sector is flat.
- **Two open, unowned exposures.** `T` and `CBRE` are ~16.6% of real invested capital with no thesis
  (`C23`/`M1169`); `S107` settled `FIRED-C` on 09-03 without resolving the orphan.

**`[inferred]` rows carried but NOT citable as evidence:** the "duration event is global" reading
(EVENT_ALPHA Card 3, `STORY-ONLY`); the "memory shortage is demand not capacity" reading on `MU`
(its contracted-volume share is `unknown`, `C3`, and `M1305`-class evidence is inadmissible on that
node until read).

### §5 retracted ledger — read BEFORE forming today's view

Nothing in today's opening frame matches a retracted entry. Six retractions bind this run:

- **`R120`** (09-01) — the 5m-proxy error bound. Moot; the proxy is retired (G0), third run.
- **`R122`-KR** (09-02) — missing bars move a benchmark window's **start**. `W1` bars the KR content;
  the **check** transfers and was re-run: today's cache is **1 NaN/session (`EA` only) with ZERO
  partial-NaN names**, so no 20-session window is holed for any scored name. Stated because checked.
- **`R127`-KR** (09-05) — *"the index close does not exist because the vendor lacks it."* Its general
  form is adopted as a US rule: **a vendor's silence is not the world's silence.** ★ Applied twice
  today: (i) `G1`'s whole finding is that a `None` meant *our own outage*, not *no news*; (ii) the
  "no new session" claim was checked on a **second instrument** — a direct `yfinance` ETF pull
  returned last index date **2026-09-04** with the identical board (`SMH` +2.61 · `SPY` −0.39 ·
  `XLY` −1.33 · `^VIX` +1.47), agreeing with the sweep's `asof`. Two instruments, one answer.
- **`R128`-KR** (09-05) — a one-day vocabulary spike is not an axis migration. Binds EVENT_ALPHA.
- 🆕 **`R129`** (09-05, this desk) — *"`S130` is a dead thread."* Killed by the thread's own curve
  (4→28→9, peak 28) and `theme-age` 🟡ACCELERATING 3.11×. **Binds today**: `S130` settles 09-10 and
  must not be inherited as dead a fourth time.
- 🆕 **`R130`–`R133`-KR** (09-06) — four **self**-refutations inside one KR run, all of the same
  class: *a level difference between two nodes was read as two judgement units, and residual
  correlation refused the split.* `W1` bars the KR content (Korean metals). ★ **Its general form is
  adopted and is live on this desk today**: `M1316` splits Utilities into merchant vs regulated and
  `M1314` splits IT into software vs hardware — **neither split has been checked against residual
  correlation.** Carried into the dig list as **`D530`**, not asserted as an error.

### §6 open contradictions — carried, not resolved

| id | state this run |
|---|---|
| **`C21`** RSI convention | untouched |
| **`C22`** the two ledgers name different hands | **quiet, 16th consecutive run.** 0 due on both; legacy **0/0**. Totals moved 293→**300** rejections and 312→**321** misses since 09-05, i.e. the KR run filed 9 new conditional rows and none is legacy |
| **`C23`** three books, none self-identifying | 🚨 **reproduced a 7th time AND the instrument degraded further** (§6). `cycle_exposure` reads the real KIS book ($5,255 invested of ≈$11,022 ⇒ **52.3% cash**); `exposure_rule state` now returns **a BLANK invested-% field** ("계좌조회 실패"), so its band gap is unquotable from `state` at all today and survives only in `show`'s stored 85.2%. **Human call (P5)** |
| **`C24`** copper spec at the 100th percentile vs a Materials bucket | carried a **7th** run. Materials **−0.025 `wflow` / −0.107 `eqflow`**, Δ −0.037 — unchanged, because nothing new was measured. **`P102` settles the two-name question 09-09** and this run must not move it early (`D343`) |
| **`C25`** two instruments read OBV's sign oppositely | carried; no US re-measurement today (no new bars). The KR narrowing is `W1`-barred and the US has no investor-type feed |
| **`C26`** primary vs repaired sweep disagree | ✅ **closed-by-disappearance, 3rd run** — no repaired file exists or is needed |
| **`C27`** `MSTR`'s two rejections give opposite answers | carried; `due` surfaces them **09-18 / 09-22**. ⚠ `MSTR`'s standing rejection is still unexamined (`D463`, §4) |
| **`C28`** a revival condition can be true on the day it is written | carried |
| **`C29`** an axis with opposite signs on two instruments | 🚨 **the KR desk added a 2nd and 3rd leg this morning.** ① `vol_surge` h=1 clears Bonferroni **NEGATIVE for a 4th consecutive run** (n=45 · n_eff 45 · IC −0.0414 · **t(NW) −3.61**, re-run today, unchanged) while `sector_flow`'s 🟢 gate weights it **positive**; ② `M1328-KR` — the same gate's *velocity* leg is absent on **92.8%** of names; ③ `M1337-KR` — the three names the axis pushed up all have **negative 20-day excess**. ⇒ **the 🟢 label stands on the product of two defects.** ✅ The US instrument exists now: **`S145` settles 09-11**. **Authority is a human call (P5)** |

### 🆕 No new contradiction opened by this stage
Today's findings are **defects with mechanical fixes**, not carried tensions, and are registered as
`D528`–`D533` rather than as `C30`. Stated explicitly because opening a `C` is the easier move and
the ledger is only useful if `C` means "two defensible readings", not "something is wrong".

---

## 3 · Scenario settlement — **0 due, and the zero was earned by an exhaustive scan, not by reading the queue**

> Run clock **KST 2026-09-06 22:09 → 23:0x = Sun 09:09 ET.** NYSE **closed**, and closed all weekend.
> Last settled US session **2026-09-04**, complete and already fully scored by the 09-04/09-05 runs.

**Scored by this run: 0. `EXPIRED`: 0. Silent skips: 0. Blocked and named: 3. Folded into the master
log by this run: 10 (9 verdicts + `P101`). Newly surfaced as never-logged: 5.**

### 3a · The queue says zero — and the queue is a forward-looking object, so it was not trusted alone

The dated settle queue (`SCENARIOS.md`, updated by the 09-05 US run) has **no 09-05 and no 09-06
cell**; its next cell is **2026-09-08** (`S127`·`S128`·`S129`·`S140`·`P122`·`P123`·`P128`). The KR
desk verified the same thing this morning. **But a settle queue only lists rows someone remembered to
put in it**, which is precisely the defect `D504` names. So this run also ran the back-scan below.

### 3b · ★★ The exhaustive back-scan — and it found five rows the queue cannot see

`SCENARIOS_US.md` was parsed mechanically: **152 row-blocks**, every header settle date extracted,
**105 rows with a settle date on or before 2026-09-06**, each cross-searched for a verdict token
(`FIRED-*` / `VOID` / `EXPIRED` / `AMBIGUOUS`) in the master log and in the US file.

| row | settle date | days past | where its verdict actually lives | class |
|---|---|--:|---|---|
| **`S16`** (Meta Q2, COMM sector-vs-name) | **2026-07-29** | **39** | 🚨 **nowhere.** Master log line 28 still reads verdict `—`; the only later mention is a *tracking* note ("categorical leg recorded, windows open") | **never scored** |
| **`S24`** (MSFT/META/AMZN capex → the Utilities leg) | **2026-07-29** | **39** | 🚨 **nowhere.** Master-index row only; last state is the same 07-30 tracking line | **never scored** |
| **`S42`** (this-run's-own INDU verdict, bracketed against itself) | **2026-08-12** | **25** | 🚨 **nowhere.** Last state 07-30, *"tracking branch B"* | **never scored** |
| **`S25`** (RE OW−, DLR rs20 vs peer median) | 2026-08-08 | 29 | ✅ **scored** `FIRED (threshold met) — ZERO-INFORMATION`, 2026-08-02 — **but the row lives in `SCENARIOS_US.md` line 1259, not in the shared master log** | **logged in the wrong file** |
| **`S110`** (`HPE` − `DELL` pair) | 2026-09-03 | 3 | ✅ **VOID** derived 09-04 (`D488`, both names printed inside the window) — **lives only in two run reports; master index still reads `ARMED`** | **`D494-KR` class** |

★★ **`S16`, `S24` and `S42` are the first genuinely `EXPIRED`-class rows this desk has surfaced in
weeks, and they were invisible because every run inherited the *queue* rather than re-scanning the
*file*.** The three share a signature: all were registered in the **2026-07-23 → 07-29 PREMORTEM
cohort**, all had their last recorded state written as an **interim "tracking" line on 2026-07-30**,
and the desk then had a multi-day gap. **An interim tracking line reads like a scoring to a later
run's grep, and that is why nobody caught them.** Filed as **`M1355`** and **`D531`**.

⚠ **This run does NOT score them.** Three of the four legs need capex-guide readings and a rs20 peer
median as of **07-29 / 08-12**, and reconstructing a threshold six weeks later is exactly what
`D242` forbids. **They are marked `EXPIRED-UNSCORED` with the reason, which is the honest verdict**;
a human may re-register any of them with a fresh date (P5).

### 3c · Due but NOT READABLE at this run's clock — named, not skipped (`D427`, **7th reproduction**)

Re-pulled `module_macro_us --days 400 --json` this run. **The split publication reproduces exactly:**

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `T10YIE` **2.35** · `RRPONTSYD` 0.675 | `DGS2` **4.34** · `DGS10` 4.77 · `DGS5` 4.52 · `DGS30` 5.25 · **`DFII10` 2.42** · `hy_oas` 2.65 · `ig_oas` 0.81 · `VIXCLS` 14.32 · `SOFR` 3.66 | `WALCL` 09-02 · `DTWEXBGS` **08-28** · `NFCI` 08-28 |

| row | settle condition | reference state (**explicitly NOT a score**, `D242`) |
|---|---|---|
| **`P121`** | first `[FRED]` close covering 09-04 | A needs `DGS2` ≥ 4.50 **and** `T10YIE` ≤ 2.36; B needs `DGS2` ≤ 4.18. At 09-03: `DGS2` **4.34** = neither; `T10YIE` **2.35** would satisfy A's second leg alone |
| **`P114`** | same | — |
| **`P125`** | *"the first observation where **BOTH** `T10YIE` and `DFII10` carry 2026-09-04"* | 3-session (Δbreakeven − Δreal) through 09-03 = **+6.0 bp = the 88.1st percentile**, i.e. **above branch A's +5.0 line**. Recomputed from source this run, not inherited |

★ **`P125`'s construction is still working, and today it earns a sharper statement.** Its observable
names the **joint** date. It is therefore **unscoreable rather than mis-scoreable** — and today that
matters more than usual, because a calendar-dated version of the same row would have been scored
**branch A** on a `DFII10` value that does not exist yet. **The row is protecting itself from a
verdict it would have gotten wrong.** Filed as **`M1356`**.

★ **The block now has a floor, not just a reason.** `2026-09-07` is **Labor Day** (`D507`); H.15 does
not publish on a federal holiday. ⇒ **these three rows are blocked through at least 2026-09-08 — a
fourth consecutive run**, and that is a calendar fact, not a hope. **Not `EXPIRED`** — the settle
condition has not arrived.

### 3d · ★ Fold-in executed INSIDE this stage — 10 verdicts transcribed into the master scoring log

**Transcribed, not re-scored** (`D242`; provenance = `llm_outputs/2026-09-04/industry_US/HANDOVER.md`
§3a and `llm_outputs/2026-09-05/industry_US/HANDOVER.md` §3a/§3c, both derived against the
pre-registered observables at the time).

| row | observable | measured | verdict |
|---|---|---|---|
| `S109` | `FRO` exc5 vs `SPY`, 08-26 → 09-02 | **+10.363pp** | ★ **FIRED-A** (≥ +8.043) |
| `S105` | [`MRVL` exc10] − [`AVGO` exc10] @ 09-03 | **−14.917pp** | ★★ **FIRED-A** (≤ −10.836) |
| `S106` | `MSFT` exc10 vs `SPY` @ 09-03 | **+4.635pp** | **FIRED-C** |
| `S107` | `EW{T,VZ}` exc10 vs `SPY` @ 09-03 | **+2.105pp** | **FIRED-C** |
| `S110` | [`HPE` exc5] − [`DELL` exc5] @ 09-03 | −9.289pp (would be B) | 🚨 **VOID** — both names printed inside the window (`D488`) |
| `S114` | `EW{NUE,STLD}` exc5, 08-26 → 09-03 | **+3.134pp** | ★ **FIRED-B** (≥ +0.826) |
| `S132` | `AVGO` exc1, first settled close after the print | **−3.792pp** | **FIRED-C** (±9.00) |
| `S138` | same observable, wider band | **−3.792pp** | **FIRED-C** (±11.00) |
| `S141` | `SMH` exc1 vs `SPY`, 09-02 → 09-03 | **−0.662pp** | **FIRED-C** (A +1.802 / B −1.732) |
| **`P101`** | `EW{SW n=19}` − `EW{HW n=37}`, 5 sessions to 09-04 | **−6.511pp**, participation **21.1% vs 73.0%** | ★★ **FIRED-C** (A ≥ +3.196 / B ≤ −7.906) |

⚠ `S141`'s near-miss is carried with the verdict, not instead of it (`D505`): the sector move the row
was built to catch printed **+3.00pp on 09-04**, one bar outside its window.

### 3e · ★ Four `D504`-class propositions written into the master index by this stage

`P125`·`P126`·`P127`·`P128` were registered inside `llm_outputs/2026-09-02/industry_US/MACRO_REPORT.md`
§D and have **never** existed in `SCENARIOS.md`'s master index — which is why `P101`, their sibling,
went 10 days unscored. **`P128` settles 2026-09-08, two days out**, and the KR desk explicitly named
it *"the next US run's #1 priority."* This run opened the 09-02 MACRO report, read the four frozen
observables verbatim, and wrote them into the index (§ writeback). **Registration content is copied
unchanged; no threshold is touched (`D242`).**

### 3f · Still armed, no date reached — nothing dropped

`S127`·`S140`·`P122`·`P123`·**`P128`** (09-08) · `S128`·`S129`·`S136`·`S137`·**`P102`**·**`P126`**
(09-09) · `S130`·**`P127`** (09-10) · `S125`·`S135`·`S142`+ANNEX·`S145`·`P137`·`P138` (09-11) ·
`S123` (09-12) · `P111`·`S133`·`S146`·`S147`·`P136` (09-14) · `P124` (09-18) ·
`S37`·`S40`·`S48`·`S122` (09-30) · `P67`·`P81`·`P85`·`P87`–`P89`·`P115`–`P117`·`S3`·`S4`.

⚠ **`P102` reference state, since `C24` turns on it** (explicitly **not** a score, settles 09-09):
Materials is **−0.025 `wflow` / −0.107 `eqflow`**, Δ −0.037 — **unchanged from 09-05 because no new
session was measured.** That is branch **B**'s shape, which the row disclosed as its favourite.

### 3g · Named again rather than dropped
**`S8` — 40th consecutive run unscoreable.** Date field still `[blank]`. **A human must `VOID` it or
re-register it with a date (P5).** The 40th writing of this line is the finding.

⚠ **`D472` measured rather than asserted this run.** The parser found **63 row-blocks in
`SCENARIOS_US.md` that still contain the token `ARMED` while carrying a settle date already past.**
Header hygiene and scoring are two different writes and only one has ever happened. **This run fixes
the ten it folds in (§3d) and reports the residual as a number for the first time** — `M1357`.

---

## 4 · Both ledgers audited — quiet, 16th consecutive run, and the totals moved

| ledger | total | resolved | legacy (no condition) | **due today** | vs 09-05 |
|---|---:|---:|---:|---:|---|
| `reject_ledger` | **300** | **185** | **0** | **0** | total 293 → 300 (**+7 new conditional rows**) |
| `missed_ledger` | **321** | **207** | **0** | **0** | total 312 → 321 (**+9**) |

Both `due` calls were run (not substituted with `score`). Both return *"확인할 항목 없음"*.

★ **The zero is genuine and the movement proves it.** No row resolved (no new session to resolve
against), but **16 new rows were filed by the 09-06 KR run and every one carries a condition** —
legacy stays **0/0** for a 16th run. `carryover.md`'s own warning is honoured: a clean `due` is not
health; the **legacy count** is, and it cannot shrink further, so the standing check is now "does it
stay at 0 as new rows are filed." **This run: yes, on 16 new rows.**

🚨 **`D463` binds ALPHA and is loaded now, not at ALPHA.** `due` answers *"what is owed a re-check"*,
not *"is this name currently rejected."* Standing rejections live at ALPHA, with their carried state:
- **`MSTR`** — 09-01 `L.vehicle없음`, recheck **09-22**. The best 5-session name in the IT software leg
  (+12.17% as of 09-03) with OBV +0.326 매집 and rs20 +43.2. **Rejection stands, still unexamined**
  for a third consecutive run (`C27`).
- **`CRM`** — 08-31 `B.모멘텀only`, revives 09-30; needs rs20 > +20 **AND** a new dated catalyst.
- **`INTU`** — 08-31 `G.섹터중립`, revives 09-30; needs IT back to OW **or** z < −1.0.
- **`VST`** — 08-14 `G.섹터중립`, reaffirmed 09-04 on an OBV cut missed by **0.003** (`C5`), while its
  `obv_norm` is now **+0.207 = four times that cut**. **Surfaced, not overturned.**
- **`TSLA`** — 09-05 `K.본문반증`, recheck **09-19**. **rare-earth complex** — `L.vehicle없음`, 09-19.
- **`VLO`/`DLR`/`CIEN`/`GLW`** — reaffirmed 09-04; none has a recheck date before 09-15.

### 4a · Cross-desk debt: none outstanding
The 09-04 US run's 19 assigned KR rows were discharged by the KR desk on 09-05 (30 rows resolved).
**No US-assigned row is pending on the KR side and none is pending here.** Recorded so a closed
hand-off is visibly closed.

---

## 5 · What changed in the tape since the last carry — **nothing, and that is the finding**

**Last settled session 2026-09-04, identical to the 09-05 run's.** Verified on **two independent
instruments** (`R127`-KR's rule): the sweep's cached `asof` and a direct `yfinance` ETF pull, which
returns last index date 2026-09-04 and the byte-identical board.

| | 09-03 → **09-04** (settled; **re-verified, not re-measured**) |
|---|---|
| tone | narrow — one sector carried the tape against a lower index |
| `SPY` | **−0.39%** |
| leaders | **`SMH` +2.61** · `XLK` +0.70 · `XLI` +0.41 · `IWM` +0.28 · `QQQ` +0.18 · `XLU` +0.12 |
| laggards | `XLY` −1.33 · `XLC` −1.19 · `XLV` −1.04 · `XLE` −0.87 · `GLD` −0.84 · `XLP` −0.80 · `XLF` −0.79 · `XLRE` −0.72 · `XLB` −0.34 |
| vol | `^VIX` **+1.47%** to 14.53 |

**The sweep, asof 2026-09-04 — presented as a LEVEL table with the Δ column dated, per G2:**

| sector | wflow | eqflow | Δ (**09-03 → 09-04**) | breadth | top1 | issuer-flip? |
|---|---:|---:|---:|---:|---|:--:|
| **Energy** | **+0.440** | **+0.562** | **+0.054** | 0.19 | XOM 30.5% | no |
| Health Care | +0.098 | +0.190 | −0.043 | 0.03 | LLY 19.4% | no |
| Utilities | +0.071 | +0.050 | −0.037 | 0.00 | NEE 17.7% | no |
| Materials | −0.025 | −0.107 | −0.037 | 0.08 | LIN 24.7% | no |
| Information Technology | −0.090 | −0.195 | −0.010 | 0.02 | NVDA 19.4% | no |
| Real Estate | −0.116 | −0.124 | −0.020 | 0.00 | WELL 16.9% | no |
| Financials | −0.118 | −0.023 | −0.004 | 0.02 | BRK-B 13.9% | no |
| Consumer Staples | −0.182 | −0.098 | −0.018 | 0.05 | WMT 28.9% | no |
| **Consumer Discretionary** | **−0.255** | −0.280 | −0.004 | 0.04 | **AMZN 40.2%** | 🚫 **YES** |
| Industrials | −0.379 | −0.354 | **+0.082** | 0.04 | CAT 8.7% | no |
| **Comm. Services** | **−0.389** | **−0.035** | +0.007 | 0.00 | **Alphabet 76.6% (2 classes)** | 🚫 **YES** |

⚠ **Every cell above is identical to the 09-05 file.** Downstream stages may use it as **state**;
none may use it as **change**. ⚠ Cap weights rest on a **53-day-old** vector (G5) — where `wflow` and
`eqflow` disagree, `eqflow` is the citable one.

### 5a · Instrument facts this run adds
- The 08-28 heal held a **third** session; **partial-NaN names = 0**, which is the test that separates
  a vendor hole from a structurally absent name. `EA` is the second kind.
- The news-tunnel wall moved **49 → 50** while remaining contiguous with zero gaps ⇒ it is a **query
  volume** threshold (~100), not a name list (`M1354`).
- `D427` reproduced on a **7th** run, with a **holiday floor** attached for the first time (`M1356`).
- Risk-unit membership across 250/500/750d is unchanged from 09-05 **because all three windows end on
  the same 09-04** — recorded so the stability is not misread as a new confirmation (`C4`, n=1 day).

---

## 6 · Exposure state carried forward (size context for BET/ALPHA — **not** a size)

| book | reading | state |
|---|---|---|
| **Real KIS account** (`cycle_exposure`, 2026-09-06) | total ≈ **$11,022** · invested **$5,255** ⇒ **52.3% cash** | ✅ **no top-rank cycle GAP**: AI-compute epicenter **17.48%** (bar ≥12%, holds `NVDA`/`ANET`), Energy/refining **10.47%** (bar ≥8%, holds `MPC`/`PSX`), missile-defense **3.64%** (no bar set) |
| **KR contest / timefolio** (`exposure_rule`) | verdict **정상** · target **95%** · **current % = BLANK** · band gap **unquotable from `state`** | `show --tail 8` still stores **85.2% invested**, band gap **−9.8pp**, cumulative **−9.79pp = cash −5.32 + selection −4.47**, **n=18** |

⚠ **Not a cold start** (n=18) and **not `밴드미설정`**.
🚨 **NEW degradation, and it is the reason the band gap must be quoted from `show` and not from
`state` today.** `exposure_rule state` printed *"수익분해 불가: NAV/투자비중이 없다(계좌조회 실패)"*
and left both the current-% and gap fields **empty**, flagging `🚨투자비중미상`. The KR desk logged
the same blank this morning (`D483-KR`). The 85.2% above is a **stored** value from the ledger, not a
live read. Filed as **`M1358`**.
🚨 **`n` has now been flat at 18 for FIVE calendar days** (09-01, 09-03, 09-04 rows exist but carry no
decomposition columns). The report's own note asks this denominator to rise by 1/day. The 09-04 run
recorded the stall at three days, the 09-05 run at four; **it is now five and still not resolved.**
🚨 The KR-measured **55% → 95% target jump in one session while the position did not move**
(`M1266-KR`) still stands under the 95% figure above. **Quoted as inherited context, not a size input.**
⚠ `exposure_rule` prints **🚨🚨ARMED (`TIMEFOLIO_EXECUTE=1`)** on all 48 ledger rows. Recorded because
it is on the instrument's own output. **This run issues no order of any kind.**

---

## 7 · RESEARCH triggers loaded as BINDING constraints (not summarised)

| group | fires when | IDs | binds, this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO and every stage.** ★ `C1` is the run's governing trigger: **every Δ must name its baseline as `09-03 → 09-04`** because today's snapshot re-reads the same session (G2). ★ `C3` live twice: **`EA` is unmeasurable, not absent**, and **`exposure_rule`'s current-% is blank, not zero** (§6). ★ `C4` live: the risk-unit grouping's "stability" vs 09-05 is n=1 day. ★ `C5` live: units agree at dist 0.40–0.60 and diverge only at the chosen 0.65 |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test.** ★ `S2` is the run's second governing trigger and it fired three ways: the news null is **our own outage** (G1); the "no new session" null is **the calendar**, checked on a second vendor; the "0 rows due" null was **diagnosed by an exhaustive back-scan** and turned out to hide 5 rows (§3b). ★ `S5` live: the 250d window (249 obs) again has the highest fit (+0.8511) with the lowest ARI (0.3874) |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators/money_trail.** ★ `D1`/`D5` live and *satisfied*: the settled-session claim was checked on two independent providers; `D427` reproduced on a fresh pull. ★ `D3` live: `hy_oas` **level** is at the 2.0th percentile while its **5-session change** is +2 bp — different objects, and `P128` is written on the change. ★ `D4` **stands down** — weekend, no partial bar |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★ `W1` live four ways and **satisfied in all four**: the KR `ic_ledger` verdict, `R127`/`R128`-KR, `R130`–`R133`-KR, and `M1329-KR`'s news constant — **each named, none imported; the KR news constant (58) is explicitly NOT used as the US constant (50)**. ★ `W5` load-bearing: `M1314`'s 20.07pp IT sub-node spread against a ~0.16% sector move bars any IT-wide verdict |
| **L** (lenses) | — | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★ `L1` live: `M1311` — the distillate crack's **rate** is accelerating while the blended rate decelerates. ★ `L2` live on `MPC`/`PSX`/`VLO` (five-year-high op margins earned on a **pre-spike** quarter, `M1313`). ★ `L3` live: `D503`'s width criticism binds every bracket PREMORTEM writes today |

### Dig list ranked for today (candidate DEEP / PREMORTEM assignments)

| rank | dig | why today |
|---|---|---|
| **1** | 🆕 **`D529`** — a writeback is four writes and the **scoring log** is the one dropped | measured on this desk's own 09-05 run: 3 of 4 targets written, the log skipped. **Repaired inside this stage** (§3d) rather than filed |
| **2** | 🆕 **`D531`** — an **interim "tracking" line reads like a verdict** to a later run's scan | the mechanism behind `S16`·`S24`·`S42` going 39/39/25 days unscored and invisible (§3b). The fix is mechanical: tracking rows take a distinct token |
| **3** | **`D504`** — a `D449` row absent from the master index is unscoreable by anyone but its author | **`P128` settles 09-08.** Repaired inside this stage for `P125`–`P128` (§3e) |
| **4** | **`D427`** — H.15 series publish on different days | **7th reproduction**, now with a **holiday floor**: blocked through ≥09-08, a 4th consecutive run |
| **5** | **`D502`** — chunk the news fan-out **and** insert a ≥60s idle | replicated a 3rd time today, and the KR desk reproduced the *structure* independently with a different constant — the strongest form the evidence has had |
| **6** | **`D459`** — collapse dual-class issuers before `top1_w` | **12th reproduction**, 0.661 today; silently bars a whole sector verdict again |
| **7** | 🆕 **`D530`** — a sub-node split is checked against **residual correlation** before it becomes two judgement units | the general form of the KR desk's `R130`/`R133`. **This desk currently runs two unchecked splits**: Utilities merchant-vs-regulated (`M1316`) and IT software-vs-hardware (`M1314`) |
| **8** | **`D463`** — check **standing** rejections, not just `due`, before ALPHA tags | `MSTR` unexamined a 3rd run; `VST`'s OBV is now 4× the cut it missed by 0.003 |
| **9** | 🆕 **`D532`** — the catalyst calendar has **no market-holiday row** | Labor Day 09-07 governs three blocked rows and had to be learned from a dig (`D507`), not from `catalyst_calendar`. A one-line fix with a live consequence |
| **10** | 🆕 **`D533`** — the **09-10 double binary** (US Aug PPI ∧ KOSPI200 quad witching) is unbracketed and the KR desk cannot bracket it | KR has no PREMORTEM block and said so explicitly. **PREMORTEM's item this run**, D-4 |
| **11** | 🆕 **`D528`** — a spine at 3.6 MB makes "read" and "grepped" different claims | stated at the head of this file rather than hidden. `handoff_compact` is `OVER` on every file; compaction is a **human-approval** item (P5) |
| **12** | **`D472`** — a scored row's header still reads `ARMED` | **counted for the first time: 63 blocks.** Ten repaired this run |
| **13** | **`D395`/`D428`** → **`C29`** — the US desk has no `ic_ledger` | 4th consecutive Bonferroni-clearing run against a gate that weights the axis the other way; `S145` is the first US instrument, settles 09-11 |
| **14** | **`D416`** — the AI-power cycle has no registry row | `P123` settles 09-08; `S146` 09-14; the lane's only book holding is its one distributing name |
| **15** | **`D488`** — the earnings-date field is wrong and every VOID clause reads it | unfixed; it is why `S110` is a VOID rather than a `FIRED-B` |
| **16** | **`D446`** — a rolling-window axis states bars-present per name | kept live deliberately; it is the detector that would have caught the 08-28 outage on day one |
| **17** | **`D282`** — DRIFT at +0.6h vs its 3–6h spec | 8 reproductions; the fix is scheduling, i.e. human |
| **18** | **`D379`** — PREFLIGHT reads §5 first | **10th run unwired**; done manually again today |
| **19** | **`D10`** — news-body boilerplate | open code defect, **server console required (P6)**, human-approval item — carried, not re-discovered |
| **20** | **`D9`** — does a holdco mismatch **block** or only **warn** | half-closed; the remainder is a human call |

### 🆕 Registered by this stage (IDs from `module_evidence next-id`; highest existing `M1351` / `D527`)

- **`M1352`** — *The 09-05 US writeback reached 3 of its 4 targets; the master scoring log received
  nothing.* `STANDING_VIEW.md` (23:33), `STANDING_VIEW_US.md` (23:37) and `SCENARIOS_US.md` (23:08)
  all carry 09-05 US blocks; `SCENARIOS.md` carries a 09-05 US **MASTER INDEX** block and **no
  scoring-log block**. `[measured]`
- **`M1353`** — *Today's sweep contains zero new market information: `asof` 2026-09-04 == the 09-05
  run's `asof`, and all 11 sectors reproduce identically on `wflow`, `eqflow`, `delta`, `breadth`,
  `n`, `top1`, `top1_w`, `wflow_ex_top1` and `top1_flips_sign`.* `[measured]`
- **`M1354`** — *The news-tunnel wall is a query-VOLUME threshold, not a name list: universe positions
  0–48 on 09-05 and 0–49 on 09-06, contiguous with zero gaps both times, at ~2 queries/name ≈ ~100
  queries. The KR desk measured the same structure independently at a different constant (0–57,
  coverage 7.03%).* `[measured]`
- **`M1355`** — *Three US-owned rows (`S16` 07-29, `S24` 07-29, `S42` 08-12) are 39/39/25 days past
  settle with no verdict anywhere; all three share a 2026-07-30 interim "tracking" line as their last
  recorded state.* `[measured]`
- **`M1356`** — *`D427`'s block on `P121`/`P114`/`P125` now has a calendar floor: `2026-09-07` is
  Labor Day, so H.15 cannot publish before 09-08 — a 4th consecutive blocked run, known in advance
  rather than discovered.* `[measured]`
- **`M1357`** — *`SCENARIOS_US.md` contains 63 row-blocks carrying the token `ARMED` alongside a
  settle date already past (152 blocks parsed, 105 with a past settle date).* `[measured]`
- **`M1358`** — *`exposure_rule state` returned a blank current-invested-% field with
  `🚨투자비중미상`; the 85.2% figure survives only as a stored ledger value in `show`.* `[measured]`
- **`D528`** — *A carry file large enough that a run cannot read it linearly must have its reading
  METHOD declared at the head of the report — "read in full", "read by header index", "parsed
  mechanically" are three different claims.* **Origin**: `handoff/` totals 3.6 MB; `STANDING_VIEW.md`
  alone is 758 KB and a 180-line slice returned 71 KB.
- **`D529`** — *A per-run writeback is four independent writes, and the master scoring log is the one
  that gets dropped, because it is the only one requiring transcription of an EARLIER stage's output
  rather than an append of the current stage's.* **Origin**: `M1352`.
- **`D530`** — *A sub-node split is checked against residual correlation before it is treated as two
  judgement units.* **Origin**: the general form of `R130`/`R133`-KR (a steel-vs-nonferrous split
  dissolved at cross-node residual correlation +0.3905 > the within-group +0.3834). **Two live US
  splits are currently unchecked**: `M1316` (Utilities merchant vs regulated) and `M1314` (IT
  software vs hardware).
- **`D531`** — *An interim "tracking" line is written with a token no verdict scan will match, because
  a later run's grep cannot distinguish "we looked at it on the way" from "we settled it."*
  **Origin**: `M1355`.
- **`D532`** — *The catalyst calendar carries market holidays as first-class rows.* **Origin**: Labor
  Day 2026-09-07 governs three blocked scenario rows and appears nowhere in
  `catalyst_calendar --days 12`; the desk learned it from `D507`, a dig.
- **`D533`** — *A binary that falls on BOTH desks' calendars is bracketed by whichever desk has a
  PREMORTEM block, and the assignment is written down.* **Origin**: 2026-09-10 carries US August PPI
  **and** KOSPI200 quadruple witching; the KR desk has no PREMORTEM block and named the gap
  explicitly (`M1349-KR`, `D391-KR` 3 runs).

---

## 8 · Stale flags and cleared suspensions

| item | asof | state |
|---|---|---|
| `us_top300.csv` cap weights | **2026-07-15** | 🔴 **53 days** vs a ≤8 bar. Every `wflow` / `top1_w%` / issuer share is weighted 7½ weeks stale. `us_all_v2_candidate.csv` (08-10) exists, **not wired**; switching is a human-approval item |
| `handoff/*.md` carry | **2026-09-06 ~09:2x** | ✅ **fresh (13h)**, written by the KR run — **and it now DOES contain this desk's 09-05 output** in three of four files (§0) |
| `SECTOR_FLOW_US.json` `asof` | **2026-09-04** | ⚠ **fresh file, stale session** — re-downloaded today, but the newest bar it can carry is Friday's. Two calendar days old and **staying that way until 09-08** (Labor Day) |
| `DGS2`/`DGS10`/`DGS5`/`DGS30`/`DFII10`/`hy_oas`/`ig_oas` | **2026-09-03** | 🔴 the **09-04 payroll rate reaction is still not in this run**; three rows blocked (`D427`, 7th), floor 09-08 |
| `DTWEXBGS` | **2026-08-28** | ⚠ **9 days** — the dollar leg of any policy-vs-risk read is over a week behind. Recurring |
| `NFCI` | 2026-08-28 | weekly by construction — not a defect, stated so it is not re-flagged |
| `08-28` vendor hole | healed 2026-09-04 | ✅ cleared for a **3rd** session, with **0 partial-NaN names**. `D446` stays live — the heal does not retire the detector |
| `exposure_rule` ledger `n` | **flat at 18 since 09-02** | 🔴 **5 days**, worse than the 4 the 09-05 run logged |
| `exposure_rule state` current-% | **blank today** | 🚨 **new** — account query failed; the band gap is quotable only from `show`'s stored value (`M1358`) |
| `S8` date field | `[blank]` | 🔴 **40th run** — human `VOID` or re-registration required (P5) |
| `TIMEFOLIO_EXECUTE=1` armed flag | live on all 48 ledger rows | 🚨 human-owned operational flag, not an analytical one |

**Cleared suspension converted to a dig instruction:** the 09-05 run's `G2` grant ("the Δ column is
citable again") **has NOT cleared into a standing permission** — it was granted because both sides of
the subtraction were post-heal, and today the same test yields the opposite conclusion for a
different reason (a null subtraction). ⇒ **The standing instruction stands and is reinforced: state
which two dates a Δ spans, every run, on the same line as the Δ.** Folded into `D446`'s scope.

---

## 9 · Self-refutations and inherited refutations (§4c / `D48`) — written down, not edited away

1. ★★ **This stage's own first framing of §3 was "0 due, per the queue" — and the stage then refuted
   it.** The settle queue and the KR desk both said zero, and that would have been a defensible place
   to stop; every prior run has stopped there. The exhaustive back-scan run **after** that sentence
   was drafted found **five rows the queue cannot see**, three of them 25–39 days past settle with no
   verdict anywhere (`M1355`). ⇒ **"0 due" was true of the queue and false of the file.** The earlier
   framing is not deleted; §3a states it and §3b breaks it.
2. ★★ **The 09-05 run's own pre-commitment is refuted by this run's check of it — and that is the
   pre-commitment working, not failing.** That run wrote *"names it here so the commitment is
   checkable."* Checked: 3 of 4 targets written, the scoring log skipped (`M1352`). **A commitment
   that can be found to be partially unmet is a better instrument than one that cannot be checked at
   all**, and the correct response is to repair it in this run (§3d/§3e) rather than to re-issue the
   promise. `D490`'s gross form did not reproduce; a sharper form did (`D529`).
3. ★ **An inherited claim of this desk's was re-measured today and reproduced exactly — which is
   weaker evidence than it looks.** The 3-session (Δbreakeven − Δreal) flip to **+6.0 bp = the 88th
   percentile** was recomputed from a fresh FRED pull and matched `M1283` to the decimal. **But the
   underlying series has not published a new observation**, so this is the same measurement made
   twice, not a replication. Recorded because "re-measured and confirmed" is exactly the sentence
   that would launder a null into evidence on a weekend run (`C1`/`S2`).
4. ★ **Two of this desk's own live sub-node splits are now exposed by another desk's self-refutation
   and are NOT defended here.** `M1316` (Utilities: merchant vs regulated) and `M1314` (IT: software
   vs hardware) are both "a level difference between two nodes" — the exact object `R130`/`R133`-KR
   dissolved this morning under residual correlation. **`W1` bars importing the KR conclusion, and
   this stage does not import it**; it registers the *test* as `D530` and hands it to DEEP. The
   splits stand today because they are unfalsified, not because they were checked.
5. **Zero self-refutations would itself be a finding.** Four are recorded. Three came from **running
   a measurement after the sentence was written**; one came from **checking another run's written
   promise**. None came from re-reading prose.

---

## ✅ EXIT CHECK — HANDOVER

- [x] Shared spines read (`STANDING_VIEW.md` §1 regime · §2 chain · §5 retracted ledger through the
      09-06 KR block · §6 contradictions · asof chain; `SCENARIOS.md` master index + master scoring
      log + settle queue through the 09-06 KR block), plus `STANDING_VIEW_US.md` (09-05 append in
      full incl. the 22-name §3a registry), `SCENARIOS_US.md` (**parsed end-to-end, 152 blocks**,
      plus prose for every row named), `RESEARCH.md` Parts A/B/C, `README.md`. **Other-market
      material opened**: the 09-06 KR blocks in both spines. Mechanical ledger cross-queried
      (`module_report_tags show`: 81 / 303 / 12). ⚠ **Reading method declared at the head of this
      file** (`D528`) rather than claimed uniformly.
- [x] **Retracted ledger read BEFORE forming today's view** (§2). No claim here matches a retracted
      entry. `R127`-KR's general form applied twice; `R130`–`R133`-KR's general form registered as
      `D530` and turned against **this desk's own** two splits (§9.4), with the KR content left in KR.
- [x] **Every past-dated row scored, folded in, or explicitly named.** 0 newly scoreable (0 new
      settled sessions — verified against the queue **and** an exhaustive 152-block back-scan);
      **10 verdicts folded into the master scoring log inside this stage**; **3 blocked-and-named with
      reference states and a calendar floor** (`P121`·`P114`·`P125`); **3 marked `EXPIRED-UNSCORED`
      with reasons** (`S16`·`S24`·`S42`) and **2 mis-filed verdicts named** (`S25`·`S110`);
      `S8` named for a 40th time. **0 silent skips.**
- [x] **`reject_ledger.py due` run** — **0 due**, legacy **0**, totals **300/185**. The zero is shown
      to be structural (no new session) while the totals moved +7, so the ledger is live.
- [x] **`missed_ledger.py due` run** — **0 due**, legacy **0**, totals **321/207**, +9. Sign inversion
      noted; the two ledgers' `excess` columns are **not** summed anywhere in this run.
- [x] **Exposure state read and carried** (§6): verdict **정상**, target **95%**, **current % BLANK
      today** (`M1358`) with the stored 85.2% / −9.8pp quoted from `show`, cumulative **−9.79pp =
      cash −5.32 + selection −4.47**, **n=18 and stalled 5 days**. Not a cold start; not
      `밴드미설정`. Real-book side carried separately (52.3% cash, no cycle GAP) with `C23` attached.
- [x] 🚨 **Instrument health inherited before any number is trusted** (§1) — `PREFLIGHT.md` read in
      full; every FAIL converted into a named revocation and applied above (no sweep velocity cited;
      no `wflow` verdict on CD or COMM; `--days` carried with every unit count; no cap weight cited
      as current; **every Δ dated `09-03 → 09-04`**).
- [x] **Self-refutations written down, not edited away** (§9) — four, three from post-hoc measurement
      and one from checking another run's promise.
- [x] Stale rows flagged with `asof`; the one apparent cleared suspension (`G2`'s Δ grant) is shown
      **not** to have cleared and is converted into a standing instruction rather than a silent trust.
- [x] `[measured]` / `[inferred]` tags preserved; the two `[inferred]` carries are named and barred
      from evidence use (§2).
- [x] **RESEARCH triggers loaded as binding constraints**, grouped C/S/D/W + lenses L, each with the
      downstream stage it binds and a live instance (§7). `C1` and `S2` named as this run's two
      governing triggers.
- [x] `HANDOVER.md` written. **`handoff/` writes performed INSIDE this stage** (§3d/§3e) rather than
      deferred, following the 09-05 run's own precedent and because `D490`/`D504`/`D529` are three of
      this run's dig items. The remaining end-of-run writeback covers §5 fact rows, §6, the dig list
      and the asof chain.
- [x] No position sizing, no buy/sell language anywhere in the carry (P4).

---

## 📋 Stage run log — open decisions resolved without a human

1. **Whether to score `S16`/`S24`/`S42` now that they are surfaced** — resolved as **mark
   `EXPIRED-UNSCORED` with the reason, do NOT score**. Reconstructing a 39-day-old capex-guide
   threshold is what `D242` forbids; a human may re-register them (P5).
2. **Whether to fold the 10 verdicts in at run end or inside this stage** — resolved as **inside the
   stage**, matching the 09-05 run's own decision #6 for `S145`–`S147`, because three of the last six
   US runs did not reach their writeback.
3. **Which value of the KR contest book's invested % to carry** — resolved as **quote `show`'s stored
   85.2% and label it stored**, since `state`'s live field is blank (`M1358`). No number is invented
   for the blank (P5).
