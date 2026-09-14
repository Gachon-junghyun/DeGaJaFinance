# HANDOVER — industry_US · 2026-08-07 (Fri) · STAGE 1, runs before MACRO

## 0. Run clock

**09:10 ET · 22:10 KST · 20 minutes BEFORE the US open — and 40 minutes AFTER the July NFP print.**

| | |
|---|---|
| Last settled US equity session | **2026-08-06 (Thu)** |
| Last settled session used by the prior (08-06) run | **2026-08-05 (Wed)** |
| New settled US price information since the last run | **ONE FULL SESSION** |
| US market state at stage start | **PRE-MARKET (closed).** No 08-07 equity bar exists |
| ★★★ **Macro state** | **July Employment Situation printed 08:30 ET = 40 min before this stage read.** The observable a live bracket (S51) and a live tilt (FIN OW) both hang on **already exists** |
| FRED state | daily series `asof` **2026-08-05**; **`T10YIE` prints 08-06** — one business day stale, normal, not a fault |

★ **Third consecutive run opening before the bell — and the FIRST in which a dated macro binary
printed BEFORE stage 1 read.** Every equity, RS and flow figure in this stage is stamped
**`asof 2026-08-06 settled`** (verified: the yfinance panel's last bar is **2026-08-06**, SPY 768.56).
⚠ **The run WILL cross 09:30 ET** — SWEEP must re-check and trim and must state which side of the
open its cache was built on (**D74**).

---

## 1. Inheritance read

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (SHARED SPINE) | ✅ | §1 regime · §2 seed chain · §4 asymmetry · §5 retracted ledger **R1–R55** · §6 contradictions. ⛔ **§2/§3 are pre-split copies — ignored** (the M22–M256 collision the ID audit reports is that artifact, not a new fault) |
| `handoff/STANDING_VIEW_US.md` | ✅ | §2 US fact rows through **M465** · §3a per-name registry — intact, authoritative |
| `handoff/SCENARIOS.md` (SHARED SPINE) | ✅ | master scoring log + MASTER INDEX, **including the 08-07 KR appends** |
| `handoff/SCENARIOS_US.md` | ✅ | **S8 · S25 · S30 · S31 · S35 · S35-ANNEX · S36 · S47 · S50 · S51 · S52 · S53 · S55 · S57 · S61 · S62 · S65 read in full** |
| `handoff/SCENARIOS_KR.md` | ✅ **opened and checked for past-dated rows this desk owes** | **ZERO.** The 2026-08-07 `industry_kr` run (08:45 KST) scored its own board (S50-KR FIRED-A) and closed its condition-settled class. No KR row is past-dated and unowned |
| `handoff/RESEARCH.md` | ✅ Groups C/S/D/W + lenses L · Part C dig list through **D201** | loaded as **binding constraints**, §6 below |
| `module_report_tags show` | ✅ | reconciled in §5 |

**ID counters verified at read time** (D137's grep requirement, run against all `handoff/*.md` with
`scripts/handoff_id_audit.py` plus an independent regex sweep): **highest `M###` = M465 · `D###` =
D201 · `R##` = R55 · `S##` = S65 (US) / S55-KR (KR)** ⇒ this run takes **M466+ · D202+ · R56+ · S66+**.

### 1a. The inherited data-integrity incident still binds this run's writeback

`handoff/STANDING_VIEW.md` was truncated to 0 bytes by the 2026-08-05 `industry_kr` writeback
(`'w'` mode + `UnicodeEncodeError`) and rebuilt from a 07-29 snapshot (**D165**, human-gated).
**R27–R45 remain `[RECONSTRUCTED]`** — they BIND, their numbers may not be quoted as the original
measurement — and **R45's content is unrecoverable**, so this run **cannot certify** that no claim of
its own re-imports it. Stated, not waved.

⚠⚠ **Pre-committed here, before it happens: this run's writeback appends via `Edit`/append, never a
whole-file `'w'` rewrite of a spine.** Same pre-commitment the 08-05, 08-06 US and 08-07 KR runs made
and kept — this would be the **fifth** consecutive run holding it.

### 1b. §5 retracted ledger read BEFORE forming today's view — the six that bind today

- ★★★ **R11** — *"the long-end move is bear-STEEPENING — term premium, not cut-pricing"* is dead.
  ⚠⚠ **This binds harder today than on any run since it was written**, because **today's NFP creates
  the mirror-image trap**: a curve that steepens on a *weak* print in a *hike-risk* regime is a **BULL**
  steepener, and R11's lesson is precisely that a 2s10s move must be decomposed into which leg moved
  before it is given a name. **§2a-bis is that decomposition, executed in advance.**
- ★★★ **R50** — *"Financials' rank-1 breadth (0.15) and its 5 new-🟢 carry the promotion to OW"* is
  retracted as a **cited leg** (the `velocity` axis blinks 51/300 → 0 → 0 → 51 and FIN breadth tracks
  it 1:1). **The OW verdict survived on mega-cap wflow rank-1-under-every-removal — not on breadth.**
  ⇒ **no stage today may re-cite breadth or `new_green` for FIN**, and **S65 exists because of it.**
- **R49** — the HLTH OW− was **withdrawn** the same run it was made; HLTH is **N**. ⇒ nothing today
  may treat Health Care as promoted.
- **R46** — *"a confirmed Hormuz reopening normalises a product spread"* is dead as a **category
  error** (a strait is a transit route; the spread was built by a **facility**). Confirmed on the
  record by the object's own operator (M418, XOM CEO). ⇒ the Iran feed still requires body reads.
- **R41** — *"the largest / most X on the board"* is withdrawn **as a method** ⇒ no superlative in
  this run without naming the population scanned (C1/C5).
- **R51 · R52** — two `SECTOR_ROTATION` deltas whose **stated reasons** were arithmetic identities
  (Energy's wflow−eqflow gap; Materials' eqflow/Δ). ⇒ **a concentration gap is not evidence** unless
  the population and its cap share are stated in the same sentence.

⚠ Cross-check: **no claim formed in this HANDOVER matches a live retracted entry**, complete against
R1–R44 and R46–R55, **incomplete by construction against R45**.

---

## 2. ★★★ Scenarios — the binary printed before the stage, and three of the four rows handed to this desk are already CLOSED

### 2a. The observable that governs the run: July payrolls CONTRACTED, and the regime makes that DOVISH

**Corroborated across 5+ independent outlets, two on full bodies:**

| Measured | Value | Source |
|---|---|---|
| **July nonfarm payrolls** | **−23,000** (a contraction) | `[guardian 2,662자 body · cnbc 2,573자 body · bloomberg title · wsj title · investing_en ×3]` |
| **Consensus** | **+83,000**, unemployment unchanged at **4.2%** | `[cnbc 08-06 pre-print body, 4,423자]` (fxstreet's pre-print survey read **+80K**) |
| **Prior two months** | **revised DOWN by 74,000 in total** | `[guardian body]` |
| **Unemployment rate** | **4.1%** — a **downtick** from 4.2% | `[investing_en "eases to 4.1%" · bloomberg "Unemployment Rate Falls" · wsj "unemployment ticked lower" · marketwatch "unemployment rate dips"]` |
| June baseline | **+57,000** (about half of consensus); rate fell 4.3% → 4.2% **driven by 720,000 people leaving the workforce** | `[guardian body]` |
| Corroborating pre-prints | **ADP +44K** vs +70K expected (June +98K) · **JOLTS openings −178,000 to 7.4m** · **Challenger July layoffs ~33,500 = lowest in two years** | `[fxstreet bodies ×2 · guardian body]` |

⚠ **C2 / D5 — a contradiction inside one body, resolved by counting sources rather than by
preference.** The guardian body writes *"The unemployment rate, however, held steady at 4.1%"* two
sentences after writing that June's rate *"dropped to 4.2%"* — internally inconsistent. **Four other
outlets independently read the rate as falling.** ⇒ **the level 4.1% is carried (5-way corroborated);
the word "steady" is treated as a single-body error and is NOT carried.**

★★★ **The regime inverts the standard reading of this print, and getting it backwards is the whole
risk.** This Fed is debating a **HIKE**, not a cut:

- **CME FedWatch September *hike* odds fell 67% → 56%** on the 08-05 ADP/ISM misses `[fxstreet, two
  independent bodies same day]`.
- **The FOMC held 3.50–3.75% on 07-29 with three hike dissents** (M425, carried).
- **Fed Governor Lisa Cook, on record 08-05**: *"Although the hiring rate is low, the unemployment rate
  remains steady because layoffs are also low"* — and she *"will support a rate hike ahead"* if
  inflation does not improve `[cnbc body]`.
- **June annualised inflation 3.5%, +0.8pp y/y** `[guardian body]`.

⇒ **A contracting payroll print is DOVISH in this regime.** Its curve signature is a **front-end
rally = BULL steepener**, not the bear steepener the FIN thesis was built on.
⚠ **`[investing_en title-only, D6 C-grade, direction only]`: *"US futures extend gains after July
nonfarm payrolls data."*** Recorded as direction, never as magnitude.

### ★★★ 2a-bis. S51's OWN registered caveat has become the live case — and it disarms the branch that would otherwise read as confirmation

**S51 (registered 2026-07-31, settles 08-10 on the 08-07 settled close)**
frozen observable: **derived 2s10s = `DGS10` − `DGS2` [FRED]**.
- **Branch A** (with the OW): 2s10s **≥ +0.35** ⇒ *"the bear steepener persists → NIM thesis intact,
  FIN OW− confirmed on its fresh mechanism."*
- **Branch B** (against us): **≤ +0.20** ⇒ bear flattener, NIM mechanism breaks.
- **Its own registration text, verbatim**: *"**Bull-steepener caveat**: a >20bp front-end **rally**
  would be a bull steepener with recession/credit fear — 2s10s could widen while FIN still suffers.
  That is NOT scored here."*

★★★ **The −23K print with the unemployment rate ticking DOWN and hike odds falling is precisely that
caveat's case.** ⇒ **if branch A fires on tonight's close, it may NOT be read as confirming the
Financials tilt.** The bracket said so at registration; this stage is collecting on it rather than
discovering it after the fact.

⚠⚠ **And the exposure is larger than when the caveat was written**: the 08-06 ROTATION promoted
**FIN OW− → OW**, and **R50 retracted the leg it cited**. So the tilt now rests on mega-cap wflow
rank-1 (which survived) while **the rate mechanism's only live bracket has a pre-declared blind spot
that today's print walked into.** ⇒ **PREMORTEM owns a both-sides bracket on the bull-steepener leg;
no live row covers it.**
⚠ **The credit overlay S51 named is checkable and does NOT fire yet**: *"if HY OAS breaks >2.90% on
the same print, read it as the credit-fear overlay separately"* — HY OAS is **2.75% (08-05)**, 15bp
below that line. **The next HY print is the discriminator between "dovish relief" and "recession
fear", and the desk does not yet have it.** (C3 — `unknown`, not benign.)

### 2b. ⚠⚠ Which rows are actually past-dated — and a nameable defect that mis-stated it

The **2026-08-07 `industry_kr` HANDOVER** handed this desk, explicitly and correctly in intent,
*"the US rows dated 2026-08-07 (S35 · S35-ANNEX · S47 · S62, and S65's NFP trigger)"* as deliberately
unscored. **Three of those four are already closed:**

| Row | Actual state | Where |
|---|---|---|
| **S35** | **FIRED-A**, dated 2026-07-29 | scored **2026-08-02 HANDOVER (industry_US)**, in the master log |
| **S47** | **FIRED-B** | scored **2026-08-02 HANDOVER (industry_US)**, in the master log |
| **S35-ANNEX** | **an annex, not a bracket** — registered 08-02 by DEEP-UTIL, has no branches and cannot fire | `SCENARIOS_US.md` |
| **S62** | ✅ **genuinely open** — settles on **tonight's** 08-07 close | below |

🚨 **New defect — `D202`: a bracket's own section header in `SCENARIOS_US.md` keeps reading `ARMED`
after the shared log scores it.** `## S35 — … · ARMED · 2026-07-29/30 → 2026-08-07` and
`## S47 — … · ARMED · → 2026-08-07` are the strings a reader sees; the verdicts live only in
`SCENARIOS.md`'s log, 800 lines away in a different file. ⇒ **every subsequent HANDOVER re-derives a
closed row as open**, and the 08-06 US run's own §2c did exactly that before the KR run repeated it.
**Cost this run: three of four handed rows.** Cheap fix, human-gated: stamp the verdict into the
header at scoring time.

**S62 — pre-commitment on the last settled bar, so tonight's settle cannot be read selectively.**

Frozen observable: **(median RS20 vs SPY of {EMR, ETN, AME, PWR}) − (XLU RS20 vs SPY)**, settled
closes, bench SPY inline. Branch **A ≤ −5.91** (15th pct) · **B ≥ +7.42** (85th pct) · C between.

| Leg | 08-06 settled RS20 vs SPY |
|---|---|
| EMR | **+11.63** |
| ETN | **+8.20** |
| AME | **+5.65** |
| PWR | **−2.29** |
| **median** | **+6.925** |
| XLU | **−6.12** |
| **spread** | **+13.045** |

Path: **+14.51 (08-04, registration) → +13.045 (08-06)**. ⇒ **tracking branch B, 5.6pp above its
line.** **Pre-committed verdict: B**, and the condition under which that is wrong is stated now —
**XLU would have to gain ≈5.6pp on the INDU median in one session**, against **XLU's own 08-07
straddle of ±2.0%** and EMR ±3.0% / ETN ±3.4% (the implied moves frozen at registration).
⚠⚠ **The named risk is asymmetric and is inside the bracket's blind spot: VST prints today (D-0), and
VST sits in XLU — not in the four-name INDU leg.** A large VST beat compresses the spread toward A
**without the leg this spread is long moving at all.** That is a mechanism, not a threshold change:
**S62 is NOT re-frozen.** DRIFT (if the run reaches the settle) or the 08-08 run owns the score.

**S35 / S47 post-fire context — recorded, explicitly NOT a re-score** (a settled verdict is not
reopened, the S44-leg-2 precedent):
- regulated-7 median RS20 vs SPY = **−6.06** (WEC −8.26 · ETR −8.77 · EXC −4.53 · SO −4.63 ·
  XEL −4.84 · AEP −8.66 · D −6.06).
- On **S35-ANNEX's own successor construction** (regulated-**SIX**, ex-D, because D is under a live
  all-stock bid): **−6.55.** ⇒ the annex's finding that *"the UW− case is stronger without D"* holds a
  second time, 4 sessions later.
- **S47's spread = −6.06 − (−10.98) = +4.92** ⇒ still inside branch B's region, which the annex
  measured to be **the modal state (true 70% of 40 sessions)** — so this is a base rate, not evidence.
- ★ **New measurement, and it runs against the annex's convergence story**: **D/NEE = 0.7896 against
  the 0.8138 deal ratio = a 3.07% discount, WIDENED from the 2.2% the annex measured on 08-02.** The
  contamination S35-ANNEX found is **not resolving**, so any future use of D in a utilities basket
  remains disqualified.

### 2c. Every other ARMED row — classified and checked

**Condition-settled, against today's `[FRED]` pull** (`asof` 08-05; `T10YIE` 08-06):

| ID | Kill / branch line | Reading | Buffer | Δ vs 08-06 |
|---|---|---|---|---|
| **S9** | real 10y (`DFII10`) **≥ 2.55** | **2.41** | ✅ **14bp** | ⚠ narrowed 15 → **14bp** |
| **S23 / S51** | derived 2s10s **≤ +0.20** | `DGS10` **4.63** − `DGS2` **4.18** = **+0.45** | **25bp** | ★ **widened 23 → 25bp — this REVERSES the "second consecutive move toward the line" the 08-06 run flagged.** M424's *"three consecutive flattening prints is an 18.9% base-rate event"* reading is upheld: it did not continue |
| **S26** | HY OAS **≥ 3.10** | **2.75** | **35bp** | narrowed 37 → **35bp** |
| **S41** | IG OAS **≥ 0.90** | **0.78** | **12bp** | unchanged |
| **S8** | Hormuz *"Strait open"* — **undated `[blank]`** | 🚨🚨 **6th consecutive run carried as un-scoreable.** Must be `VOID`ed or re-registered **by a human** (P5). Named for the sixth time, not dropped |
| **S55** | (HO% − CL%) 5-session, endpoint **08-11** | window **open, not elapsed** — nothing scored. Its branch B has a named physical object (M417) |
| **S57** | XLB 5-session excess **> +1.9** (A) / **< −2.4** (B) by 08-12 | running **−2.596** ⇒ inside branch B's region, but by only **0.196pp** | ⚠ **moved TOWARD the line, not away** (−3.79 → −2.596). Not scored |
| **S61** | STNG+FRO vs SPY → 08-12 | **STNG −2.07 · FRO +5.96** | ★★ **FRO has FLIPPED POSITIVE** (−4.55 → +5.96) and STNG improved sharply (−7.51 → −2.07) | **Not scored — but named in §3 because the STNG rejection was `reaffirmed` 24 hours ago on exactly this axis** |
| **S65** | median RS20 {JPM,BAC,WFC,BRK-B} → **08-11** | **+3.805** (JPM +3.97 · BAC +4.09 · WFC −1.46 · BRK-B +3.64) vs registration **+3.405** | branch **C** (A ≤ +0.34 · B ≥ +6.81) | ★ **The companion "BRK-B is DRAGGING the median" note is now numerically dead: ex-BRK-B reads +3.97 vs +3.805 with it = a 0.17pp gap** (it was +5.219 vs +3.405 at registration). ⇒ **the 08-06 within-run correction — that this was an n=4 estimator artifact, not a BRK-B fact — is confirmed on fresh data** |
| **S30** | scored **FIRED-B** on the 08-05 settle | post-fire the median fell **further** to **−13.35** (STX −6.41 · MU −13.35 · WDC −24.13) | — | **Context only. The verdict is not reopened** |

**Date-settled, all future — dates recorded, no action:** S2 · S3 (~09/10) · S4 (~09 late) ·
**S5 (08-11)** · S13 (08-12) · S14/S14-num · S16 · S19 · S24 (08-12) · **S25 (08-08 — already
FIRED / pre-declared ZERO-INFORMATION on 08-02, D122)** · S26 (08-12) · S37 (09-30) · S40 (09-30) ·
S41 (08-12) · S42 (08-12) · S46 (08-13) · S48 (09-30) · **S51 (08-10, and see §2a-bis)** ·
**S54 (08-10)** · **S55 (08-11)** · **S56 (08-11)** · S57 (08-12) · **S58 (08-11)** · **S59 (08-12)** ·
**S60 (08-11)** · **S61 (08-12)** · **S63 (08-13, CPI 08-12)** · **S64 (08-13)** · **S65 (08-11)**.

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**

---

## 3. Both ledgers audited — the first run with BOTH `due` lists empty AND both legacy counts zero

```
reject_ledger.py due  → 120 rows · 42 resolved · legacy (no revives_if) 0 · recheck-date due 0
missed_ledger.py due  →  73 rows · 32 resolved · legacy (no enters_if)  0 · recheck-date due 0
```

⚠⚠ **A clean `due` is NOT proof the ledger is healthy — the unit says so itself, and this run obeys
it.** The evidence that the practice is taking hold is the **legacy count**, and it is **0 for an
11th consecutive run** on the rejection side. Growth: rejections **113 → 120 (+7)**, resolutions
**34 → 42**; missed **63 → 73 (+10)**, resolutions **1 → 32**.

★ **The missed ledger's `resolved` count moved 1 → 32 in a single day** — the 08-07 KR run closed a
30-row batch. ⚠⚠ **And exactly one of those closures was retracted the same day it was made**
(**R54**: 090430 was `reaffirmed` on a query artifact — `수출` is 2 characters so the trigram index
returns a permanent 0, and `화장품 수출` hits `fts search`'s default `--mode and`; the same 5-day
window read with the 3-character `수출액` returns **44** hits, and the print existed). ⇒ **a resolved
count is a throughput measure, not a quality measure**, and this run does not quote it as progress.

**The one deferral from yesterday was collected, not lost.** The 08-06 HANDOVER deferred **JNJ**
`K.본문반증` to its own SWEEP because the revival condition read off the flow file stage 2 produces.
Verified in `out/reject_ledger_resolutions.jsonl`: resolved **`revived`, asof 2026-08-06**, on both
legs (AMGN 1.27 · BMY 1.55 · IDXX 1.43 all clearing `vol_surge` ≥ 1.2; BMY cap-rank 16 and IDXX 27
both outside the HLTH top-6) — **with the scope stated in the row itself**: what was revived is the
**Health Care flow node**, not JNJ, which still reads 🟡 / `vol_surge` 0.88 / RS20 −5.5.

⚠ **One row is named as a candidate for the NEXT `due` cycle rather than acted on now**: **STNG** was
`reaffirmed` on 08-06 because its revival condition (RS20 vs SPY positive 3 consecutive sessions)
broke at 2. **On the 08-06 settle STNG is −2.07 (from −7.51) and FRO is +5.96 (from −4.55)** — the
axis has moved materially in the row's favour inside one session. **Its recheck date has not arrived,
so `resolve` is not called** (calling it early would be the mirror of moving a threshold); the
movement is recorded here so the next `due` firing reads it as expected rather than as news.

⚠ **Signs are opposite and are NOT summed.** No combined figure appears in this run.
⚠ `missed_ledger score`'s first six rows remain `outcome_selected` (**D106**) — accumulation, never
an edge. **Not quoted.**

---

## 4. Exposure state — the band breach has essentially CLOSED, and the decomposition moved AGAIN at n=4

```
python -X utf8 scripts/exposure_rule.py state   → 2026-08-07, bench 069500.KS
```

| Field | 08-06 | **08-07** |
|---|---|---|
| Rule state | 방어 (직전 방어) | **방어 (직전 방어)** — third consecutive session |
| Bench close | 98,900 (−5.18%) | **98,090 (−0.819%)** · vs 20d high **−18.67%** · vs 20d low **+11.93%** · volume **0.604× [정착]** |
| Target invested | 55% | **55%** |
| Current invested (ledger row) | 70.9% | **55.5%** |
| **Band gap** | 🚨 +15.9pp (밴드이탈) | ✅ **+0.5pp — no 밴드이탈 flag on today's row** |
| Ledger depth | 30 rows | **31 rows**; cumulative decomposition still **n=4** |

**Cumulative: total excess −5.68pp = cash −2.03pp + selection −3.65pp (n=4).**
⚠⚠ **This is the THIRD consecutive run in which the same n=4 decomposition prints materially
different numbers**: 08-05 read **−9.16 = −4.03 + −5.14**, 08-06 read **−2.13 = −1.12 + −1.00**,
today reads **−5.68 = −2.03 + −3.65**. **That instability is a property of the instrument at n=4, not
a performance change**, and it is quoted only to keep the counter rising (**C4**).

**Four caveats, unchanged in force:**
1. **This is the KR book's exposure rule** (`069500.KS`, KR contest bands). **NOT a US sizing input;
   no US stage may size off it (W1).**
2. `state` returns **`투자비중미상`** (no account query); `show` carries the **55.5%** row. **The
   `show` figure is quoted**, discrepancy stated.
3. 🚨 **`ARMED(TIMEFOLIO_EXECUTE=1)` is set in the environment — 5th consecutive run.** This is a
   **read-only research run**: no orders, no `--execute`, no order-desk staging. Recorded because a
   standing armed flag is something a human should see.
4. ⚠ The **08-05 and 08-06** rows carry `🚨timefolio조회실패:CDPError` and today's row is
   `⚠미정착봉(장중·KIS실시간)`. **Not cold-starting** (31 rows) ⇒ the *state* verdict is quotable; the
   *decomposition* is not (caveat above).

---

## 5. Reconciliation — belief vs coverage (`module_report_tags show`)

| Class | Finding |
|---|---|
| **Belief without coverage** | **TSM and LNG** — held names **outside `us_top300`** ⇒ **no flow, RS or short axis exists for either.** TSM is a rank-1-cycle epicenter the grading instrument cannot see. **Unchanged for 9 runs**; needs a universe change (human). ⚠ **LNG printed 08-06 and the desk still cannot measure it** |
| **Coverage without belief** | **SPG · ADM · CTAS · TRI · GM** — measured flow rows, no 4Phase ⇒ no thesis may be built on them. Filed as **coverage gaps, not rejections** |
| **Resolved-but-live** | 🚨 **PSX — `ACTION_TICKETS.md` still carries `CORE-STARTER (BUY) PSX` while ALPHA filed it 🔴RESOLVED on 08-02.** ⚠⚠ `core_pick` is **HUMAN-LOCKED and was NOT modified**. **D19 firing for an 11th consecutive run**; its rationale still descends from **R8, retracted 2026-07-22**, and the ticket's own date (08-05) is two sessions past |
| **Silently unindexable** | **28 of 300 universe tickers** return 0 regardless of coverage (M152 `_US_STOP`): A · AIG · ALL · C · CAT · CB · COST · **D** · F · FAST · GS · ICE · KR · LOW · MA · **MET** · MS · NOW · O · ON · PEG · PM · Q · SO · T · TT · V · WELL. ⚠⚠ **`D` and `SO` are BOTH on this list and BOTH are S35 legs** — the regulated-basket work in §2b is done on directly-computed prices for exactly this reason. ⚠ **MET is on it and S58 scores 08-11** |

---

## 6. RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 indistinguishable · C5 arbitrary choice | **MACRO · every stage.** ★★★ **C1 was EXECUTED not cited** — the RS20 convention was re-derived from `module_flow/_price_flow.py:37` and every bracket figure in §2 recomputed from raw settled closes with SPY inline. ★★★ **C2 binds twice today**: the NFP print's two halves point OPPOSITE ways (payrolls −23K vs an unemployment rate that FELL), and one body contradicts four others on the rate's direction. ★★ **C3 binds the credit overlay** — HY OAS's next print is the discriminator and it does not exist yet |
| **S** | you make a statistical claim | S1 date-fold · S2 null · S3 power · S4 in-sample≠done · S5 short samples · S6 future labels | **Any stage citing a test.** ★★ **S1 binds §2b** — S62 settles on ONE bar, and S30 moved 7.9pp on a single bar four sessions ago. ★★ **S5 binds §9 hardest**: the US IC ledger's own n went 14 → 18 in one day and the desk must not read the sign as newly stable |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade** | **SWEEP · ALPHA.** ★★ **D74 binds SWEEP the moment the run crosses 09:30 ET.** ★★★ **D6 binds §2a**: the wsj/bloomberg NFP items are `[no body]` = title-only, C-grade, **direction only** — the numbers were taken from the 2,662자 guardian and 4,423자 cnbc bodies. ★★ **D5 binds §2a's rate reading** — one body's *"held steady"* against four outlets' *"fell"* |
| **W** | you write a conclusion | W1 cross-market · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★★★ **W1 binds twice**: the KR exposure rule is not a US input, and **`vol_surge`'s KR sign does not transfer — the US ledger measures it POSITIVE (§9).** ★★ **W5 binds Utilities directly**: the regulated leg reads −6.55 while the AI-power leg reads −10.98, a 4.4pp internal spread inside one GICS label |
| **L** | lenses | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★★★ **L3 binds §2a-bis**: S51's branch A is **structurally low-information under today's print** because its own caveat pre-declared that a bull steepener satisfies it without confirming the thesis. **A branch that can be satisfied by the wrong mechanism is the S31 branch-hole pattern in a different costume.** ⚠ **L2 unrunnable on 61% of names attempted (M233)** — no cheapness claim where `margin_history` is blank |

---

## 7. Stale flags and cleared suspensions

| Row | `asof` | Flag |
|---|---|---|
| ★★ **COT file** | **07-31 release** | 🚨🚨 **Byte-identical stale snapshot for a SIXTH read, verified instrument by instrument against the S32 annex's published pull**: NDX 5th · S&P500 82nd · R2K 57th (wk −8,137) · UST10Y 13th (+3,587) · UST2Y 55th (+30,023) · USD 72nd · WTI 10th · NatGas 3rd · **Copper 96th** · Gold 23rd · Silver 29th. **The CFTC publishes TODAY ~15:30 ET — after this stage and after most of this run.** ⇒ **no copper/NDX/WTI positioning percentile may be leaned on.** ⚠ **D104 is why the staleness is invisible: the tool prints no `asof`** |
| **`T10YIE`** | **08-06** | **2.26%**, **+4bp from 2.22 (08-05)** — the only series with an 08-06 print. ⇒ the 08-06 run's *"bottom of the 365-day range (2.18–2.50)"* framing is **one print less true**; still low, no longer at the floor |
| **`DFII10`** | 08-05 | **2.41 — the buffer NARROWED for the first time in three prints** (15 → 14bp). Recorded against the 08-06 run's *"two prints stale in the desk's favour"* line, which no longer holds |
| **`DTWEXBGS`** | **07-31** | ⚠ **119.70, seven calendar days stale.** S57's premise (*"the Materials dollar leg is dormant by construction"*) currently holds **by staleness, not by measurement** ⇒ **that is `unknown` (C3), not confirmation** |
| **`NFCI`** | 07-31 | **−0.53**, loosening. No kill line |
| **`HY OAS` / `IG OAS`** | 08-05 | **2.75 / 0.78.** ⚠ **HY is the named discriminator for S51's credit overlay (>2.90) and it has not printed since the payroll data** |
| Seed chain **M1–M19** | 2026-07 / 07-22 | ⚠ **M6 (MU fwd P/E 6.31×) is 16 days stale, superseded twice.** Cite M206 |
| **M22** 3-2-1 crack "99.5th pctile" | 07-21 | ⚠⚠ **DEAD as a level** (R30/D95). **Changes only** |
| **`CATALYST_WATCH.json`** | 08-07 | **5 binaries in window: NFP D-0 (already printed) · VST earnings D-0 · CPI 08-12 · PPI 08-13 · Hormuz undated.** ⚠ **D18 again — VST is the ONLY earnings binary the calendar carries today**, and the 08-06 run's handoff named eight prints for that day of which the calendar had none. ⚠ **D141: the `[STRUCTURAL]` block reads an empty data file and prints "(none in window)"** — which is a capability gap, not a clean calendar |
| **`core_pick` / `ACTION_TICKETS`** | 08-02 | 🚨 **D19, 11th run.** Human-locked, stale, own date passed |
| **000660 ADR flow suspension** | ongoing | **STILL ON.** KR-owned; scored by the 08-07 KR run. **Not a US-desk read** |

**Cleared suspensions converted to dig instructions: ONE.** The 08-06 run left MACRO a question —
*"is falling breakevens + falling real rates + falling crude a disinflationary-relief signature or a
demand signal?"* — and **today's payroll print is the first hard evidence on it.** ⇒ **MACRO must
now resolve it with the labour data in hand, and the two readings have opposite sector implications:
relief favours the duration-short tilts, demand-weakness attacks the cyclical OWs (INDU, ENRG) the
desk is currently long.** The question is no longer un-evidenced; it is contested.

---

## 8. Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's shape |
|---|---|---|
| **1** | ★★★ **A dovish payroll contraction in a HIKE-risk regime, against a Financials tilt promoted to OW yesterday on a leg that was retracted the same day (R50) — and the only bracket owning FIN's rate mechanism pre-declared that today's curve shape satisfies its confirming branch WITHOUT confirming the thesis (§2a-bis).** | **The run's central finding.** ⇒ **MACRO must decompose the 2s10s move into which leg moved (R11's rule), and PREMORTEM must produce a both-sides bracket on the bull-steepener leg — no live row owns it.** ⚠ The binary is ≤48h behind us, not ahead, which is the protocol's harder case: a one-way read *after* the print is the same violation as a one-way tilt *into* it |
| **2** | 🚨 **`D202` — a scored bracket's header keeps reading `ARMED`, so closed rows are handed forward as open.** | **Measured cost this morning: three of the four rows handed to this desk (S35, S47, S35-ANNEX) were already closed on 08-02.** Cheap, human-gated fix; the alternative is that every HANDOVER re-derives resolved brackets forever |
| **3** | ★★ **`S8` on its 6th consecutive un-scoreable carry**, on the event that has driven the tape for six sessions. | **A human `VOID` or re-registration (P5).** The KR desk has now also named it and cannot rule on it. **Six runs is no longer a carry, it is an unpaid debt** |
| **4** | ★★ **The US IC ledger had FOUR run-observations unaccrued** because `ic_ledger.py log` was being run without `--market us` (n 14 → **18** after one accrual, 55 rows). ⇒ **`D203`.** | **The desk's own clock was running slow on the market it grades most.** ★ Reassuring half: the sign and magnitude barely moved (`rs60` h=1: −0.0942/t −2.54 → **−0.0829/t −2.67**). **The finding is the process gap, not the number** |
| **5** | ★★ **COT stale for a 6th read, publishing TODAY at 15:30 ET, with D104 making the staleness invisible.** | **Copper 96th percentile is a load-bearing Materials input and it is a week old.** ⇒ **either DRIFT re-pulls after 15:30 ET, or no stage cites a percentile.** Fixing D104 (print an `asof`) is one line |
| **6** | ★ **D's merger-arb discount WIDENED 2.2% → 3.07%** (D/NEE 0.7896 vs the 0.8138 ratio) while the regulated-six median (−6.55) stays below the seven-name median (−6.06). | **S35-ANNEX's contamination is not resolving**, so **D stays disqualified from any utilities basket** and the successor construction it proposed (exclude live all-stock targets; require persistence or a band > 2.08pp σ) is the template PREMORTEM should use |
| **7** | ★ **S57 moved 1.19pp TOWARD its own branch line** (−3.79 → −2.596, and B needs < −2.4) while **S61's FRO leg flipped positive**. | **Two brackets are now within a session of changing which branch region they sit in.** Named so neither is discovered late — the S21/S35 failure shape |
| **8** | **D9 · D10 · D11 · D15 · D17 · D18 · D19 · D20 · D22 · D26 · D37 · D104 · D122 · D137 · D141 · D149 · D151 · D152 · D155 · D157 · D159 · D161 · D165 · D183 – D192** *(open defects, human-gated)* | Carried forward, not silently re-discovered. **D165 (truncation) and D155 (wall-clock date bug) destroy or falsify data rather than merely cost a stage.** ⚠ **D183 (the blinking `velocity` axis) binds SWEEP today** — it is the instrument R50 was retracted on |

**New digs registered by this stage: `D202` (ARMED-header staleness) · `D203` (US IC accrual gap).**

---

## 9. ★★ The signal scoreboard — the US ledger's own clock had been running slow

`axis_inflection.py` → `ic_ledger.py log` → `log --market us` → `score --market us`.

| Market | Axis | h | n | n_eff | mean IC | t(NW) | verdict |
|---|---|---|---|---|---|---|---|
| **US** | `rs60` | 1 | **18** | 18.0 | **−0.0829** | **−2.67** | **유의(단독)**, **NOT** Bonferroni (|t| > 2.8) |
| **US** | `vol_surge` | 1 | **18** | 18.0 | **+0.0348** | **+2.00** | **구분 불가 — and the sign is OPPOSITE KR's** |
| **KR** | `vol_surge` | 1 | 19 | 19.0 | **−0.0439** | **−2.65** | 유의(단독) — was −2.93 (Bonferroni-clear) on 08-05, −2.65 on 08-06 |

★★★ **The finding is procedural.** `ic_ledger.py log` had been run **without `--market us`**, so the
US board accrued nothing for four runs; today's `log --market us` wrote **55 rows at once** and n went
**14 → 18**. **Yesterday's HANDOVER quoted "n=14" as a fresh reading; it was an under-accrued one.**
⇒ **`D203`.**

**What this settles and what it does not:**
- ✅ **The sign survived the accrual.** `rs60` h=1 went **−0.0942 / t −2.54 (n=14)** → **−0.0829 /
  t −2.67 (n=18)** — mean IC shrank slightly, t rose slightly, **still short of Bonferroni.** After
  the `mention_z` episode (필요n 44 at n=7 → 757 at n=14) a signal that holds through a 4-observation
  jump is worth noting, and is **not** worth acting on (P4).
- ⛔ **The `sector_flow` gate change stays un-made.** The module weights `vol_surge` **positively**;
  **KR measures it negative (t −2.65) and the US measures it POSITIVE (t +2.00).** ⇒ **W1: neither
  market's reading may be imported into the other, and a live shared module is not flipped on two
  results that disagree in sign.**
- ✅ **The interim RULE stands and binds SWEEP · ROTATION · ALPHA**: *no stage cites a 🟢 tag without
  decomposing which axis lit it.* **D183 (the blinking `velocity` axis) is the reason it exists.**
- ⚠ **`n_eff < 4` cells (7 of 15 US, 14 of 21 KR) are not quoted anywhere in this run.** Two US cells
  print `t −29.03` and `t −7.22` at `n_eff 1.0` and **2.6**; both are the overlapping-window artifact
  the unit was built to catch.
- ⚠ **Regime label, as the unit requires**: the window is a **crash-plus-rebound** stretch. **A
  crash-window IC does not generalise.**

---

## 10. What this stage hands forward

1. ★★★ **July payrolls CONTRACTED −23,000 against a +83,000 consensus, with the prior two months
   revised down 74,000 — and the unemployment rate FELL to 4.1%.** The two halves of one report point
   opposite ways (**C2**), and **because this Fed is debating a HIKE (three dissents on 07-29, Cook on
   record 08-05, Sept hike odds 67% → 56%), a weak print is DOVISH and its curve signature is a BULL
   steepener.**
2. ★★★ **S51's own registered bull-steepener caveat has become the live case.** If 2s10s holds ≥ +0.35
   on tonight's close, **branch A fires and may NOT be read as confirming the FIN tilt** — the bracket
   said so at registration. ⇒ **MACRO decomposes the curve move by leg (R11); PREMORTEM owns a
   both-sides bracket on the bull-steepener leg, which no live row covers.** **HY OAS 2.75% is 15bp
   from the credit-fear line S51 named, and it has not printed since the data.**
3. ★★ **Three of the four rows handed to this desk this morning were already closed** (S35 FIRED-A,
   S47 FIRED-B on 08-02; S35-ANNEX is an annex). **Only S62 is genuinely open, and it settles tonight
   at +13.045 tracking branch B, 5.6pp above its line** — with **VST printing today from inside XLU,
   the one mechanism that can move the spread toward A without touching the leg it is long.**
   ⇒ **`D202`.**
4. **Condition-settled rows all re-measured**: S9 buffer **narrowed** 15 → 14bp; **S23/S51 WIDENED
   23 → 25bp, reversing the two-session flattening**; S26 35bp; S41 12bp unchanged. **S8 carried
   un-scoreable for a 6th run and named again — it needs a human.**
5. **Both ledgers came back empty on `due` with zero legacy rows — a first.** Reported **with** the
   unit's own warning that a clean `due` is not a healthy ledger, and with the 090430/R54 case as
   evidence that a resolved count is throughput, not quality. **Yesterday's JNJ deferral was
   collected inside the 08-06 run, as promised.**
6. ★★ **The US IC ledger had four runs unaccrued (`--market us` never passed); n 14 → 18 on one
   accrual, and `rs60` h=1's negative sign SURVIVED the jump** (−0.0829, t −2.67, still short of
   Bonferroni). ⇒ **`D203`**. **`vol_surge` remains sign-opposite across the two markets and the gate
   change stays un-made (P4).**
7. ⚠ **COT is stale for a 6th read and publishes at 15:30 ET today** — after this stage. **No
   positioning percentile may be leaned on**, Copper's 96th included.
8. **The exposure band breach essentially closed (+15.9pp → +0.5pp) without a state change (방어,
   target 55%)**, and **the n=4 decomposition moved materially for a third consecutive run**
   (−9.16 → −2.13 → −5.68). **KR-only; not a US sizing input (W1).**
9. ⚠ **`ARMED(TIMEFOLIO_EXECUTE=1)` is set for a 5th run.** This run touches nothing executable.

**No position sizing, no buy/sell language appears anywhere in this carry (P4).**

---

## 11 · ⚠⚠ Retention budget — measured, and worse than when it was last named

```
python -X utf8 scripts/handoff_compact.py --budget-only
```

| File | Size | Budget | Over |
|---|---|---|---|
| `RESEARCH.md` | **312.4 KB** | 85 | **+227** |
| `STANDING_VIEW.md` | **225.7 KB** | 45 | **+181** |
| `STANDING_VIEW_US.md` | **188.6 KB** | 50 | **+139** |
| `SCENARIOS_US.md` | **188.3 KB** | 50 | **+138** |
| `SCENARIOS.md` | **100.1 KB** | 20 | **+80** |
| **US run reads** | **1026.5 KB** | **250** | 🚨 **+777** |

**§2 fact rows: 533, averaging 0.55 KB/row against a ≤ 0.35 KB rule** (fattest 1.21 KB, M340).

🚨 **The US read has crossed one megabyte** — it was **877.4 KB** when the 08-05 run escalated this
from an efficiency item to a **safety** item, so it has grown **+149 KB in two days**. **Fifth
consecutive run naming it.** The instrument exists (`handoff_compact.py`, **non-destructive** — facts
move to `ARCHIVE_FACTS.md` and stay greppable; the 07-25 pass lost 0 of 154). **What is missing is
that nobody runs it**, and after **D165** the argument is no longer about context cost: the larger
these files are, the longer a writeback holds a handle open and the more one encoding fault destroys.
⚠ **Re-run at writeback (stage 10) so the figure includes this run's own additions.**
