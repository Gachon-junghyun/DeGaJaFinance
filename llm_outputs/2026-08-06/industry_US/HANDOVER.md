# HANDOVER — industry_US · 2026-08-06 (Thu) · STAGE 1, runs before MACRO

## 0. Run clock

**09:11 ET · 22:11 KST · 19 minutes BEFORE the US open.**

| | |
|---|---|
| Last settled US equity session | **2026-08-05 (Wed)** |
| Last settled session used by the prior (08-05) run | **2026-08-04 (Tue)** |
| New settled US price information since the last run | **ONE FULL SESSION — and it is the session that settles four brackets** |
| US market state at stage start | **PRE-MARKET (closed).** No 08-06 equity bar exists |
| FRED state | `asof` **2026-08-04** for the daily series (T10YIE prints 08-05) — **one business day stale, normal for FRED, not a fault** |

★ **Second consecutive run opening before the bell.** Every equity price, RS and flow figure in this
stage is stamped **`asof 2026-08-05 settled`**. ⚠ **The run WILL cross 09:30 ET** — SWEEP must
re-check and trim, and must report which side of the open its cache was built on (D74).

---

## 1. Inheritance read

| File | Read | Note |
|---|---|---|
| `handoff/STANDING_VIEW.md` (SHARED SPINE) | ✅ **with the inherited incident banner** | §1 regime · §4 asymmetry · §5 retracted ledger · §6 contradictions C1–C10. ⛔ **§2/§3 are pre-split copies — ignored** |
| `handoff/STANDING_VIEW_US.md` | ✅ | §2 US fact rows · §3a per-name registry — **intact, authoritative** |
| `handoff/SCENARIOS.md` (SHARED SPINE) | ✅ | scoring log + MASTER INDEX |
| `handoff/SCENARIOS_US.md` | ✅ | **S30 · S31 · S36 · S49 · S50 · S52 · S53 · S55 · S56 · S57 · S61 · S62 read in full** |
| `handoff/SCENARIOS_KR.md` | ✅ **opened and checked for past-dated rows this desk owes** | **ZERO.** The 2026-08-06 `industry_kr` run (08:19 KST) scored its own board including S17. No KR row is past-dated and unowned. |
| `handoff/RESEARCH.md` | ✅ Part A triggers · Part B lenses · Part C dig list | loaded as **binding constraints**, §6 below |
| `module_report_tags show` | ✅ | reconciled in §5 |

### 1a. The inherited data-integrity incident still binds this run's writeback

`handoff/STANDING_VIEW.md` was truncated to 0 bytes by the 2026-08-05 `industry_kr` writeback
(`'w'` mode + `UnicodeEncodeError`) and rebuilt from a 07-29 snapshot (**D165**, human-gated).

| Part | State | How this run may use it |
|---|---|---|
| §§1–6, R1–R26 | verbatim from the 07-29 snapshot | ✅ quotable |
| asof chain 07-29 → 08-05 | re-inserted verbatim | ✅ quotable |
| **R27–R45** | **`[RECONSTRUCTED]`** | ⚠ **they BIND, their numbers may not be quoted as the original measurement** |
| **R45** | **content unrecoverable** | 🚨 this run **cannot certify** that no claim of its own re-imports R45. Stated, not waved. |

⚠⚠ **Pre-committed here, before it happens: this run's writeback appends via `Edit`, never a
whole-file `'w'` rewrite of a spine.** (Same pre-commitment the 08-05 US run made and kept.)

### 1b. §5 retracted ledger read BEFORE forming today's view — the five that bind today

- **R46** — *"a confirmed Hormuz reopening normalises a product spread"* is dead as a **category
  error**: a strait is a transit route; the spread was created by a **facility**. ⚠⚠ **This binds
  harder today than on any prior run**, because §2a below found the mirror-image trap already live in
  the feed (a "refineries shut" cluster that reads as Iran and is **Russia**).
- **R43** — a refining print is **not** generically an inventory artifact. ⚠ W1: measured on Korean refiners.
- **R41** — *"the largest / most X on the board"* is withdrawn **as a method**. ⇒ no superlative in
  this run without naming the population scanned (C1/C5).
- **R40** — a security under a live bid is a **merger-arb security**, not a fundamental expression.
  ⇒ applied prospectively in §3 to **PYPL** (57.93 against a 60.50 bid).
- **R39** — *"XOM is 0% refining"* is dead ⇒ the Energy GAP magnitude is `unknown` (C3), and **S31's
  own branch labels still contain the retracted phrase** — scored on the frozen observable regardless,
  meaning-inheritance recorded (§2b).

⚠ Cross-check: **no claim formed in this HANDOVER matches a live retracted entry**, complete against
R1–R44 and R46, **incomplete by construction against R45**.

---

## 2. ★★★ Scenarios — four windows closed on the 08-05 settle and all four are scored

### 2a. The fact that governs the run: the primary text branch A demanded ARRIVED, and it still fails branch A

`module_news_data search --scope foreign --days 2 Hormuz` → **312 foreign hits, 0 domestic**
(08-05 count was 225 — **the cluster grew 39% in one day**).

**S52 branch A requires**: *"a **dated** Strait-reopening term in a **primary text** — a signed-agreement
text, an official US Treasury/State statement, or **a direct Iran-government statement carrying a date
or 'effective' language**. NOT a headline paraphrase, NOT a repeat of the 08-02 conditional wording."*

★★★ **On 2026-08-05 a direct Iran-government statement arrived — the exact evidence CLASS branch A
named — and it carries neither a date nor effective language.** Full body, Iran Foreign Ministry
spokesperson **Esmaeil Baghaei**, on the record Wednesday `[hellenicshipping 2,626자 · guardian ·
euronews · bbc 3,153자 · scmp · upi · ft · aljazeera 3,525자 — 8+ independent outlets]`:

> Iran and Oman have agreed on the **geographic coordinates for a shipping route** through the Strait
> of Hormuz. A joint announcement is **"in its final stage, provided certain third parties do not
> interfere."** ⚠ **"Any agreement between Iran and Oman does not, by itself, guarantee security in
> the strategic waterway."**

And the counter-evidence in the same breath (**C2**, both halves): `guardian`, citing **a senior
Iranian source and two regional officials via Reuters** — they **"pushed back against assertions by
Donald Trump that a deal reopening the strait was imminent, saying important details still had to be
agreed"**; the proposed deal **"would give Tehran control over ships entering the gulf"**.

⇒ **S52 = FIRED-C (neither branch) — provisional, see the honesty note below.**
- **Branch A NOT met.** Coordinates of a route ≠ a dated reopening. **No date. No "effective"
  language. An explicit disclaimer that it does not guarantee passage.**
- **Branch B NOT met** — and this is where **R46's lesson paid for itself**. The feed carries
  *"strikes have deepened a nationwide gasoline shortage, with several major refineries shut down"*
  in two 08-05 articles that surface on an `Iranian AND refinery AND strike` query. **Body-read: the
  refineries are RUSSIAN, not Iranian** — Ukrainian drones, **24 of Russia's 34 largest refineries hit
  this year**, `[nasdaq/Barchart body + oilprice body, corroborating]`. **A headline-level read of that
  cluster would have fired branch B on the wrong country.** No strike on named **Iranian** energy
  infrastructure is reported in the window.
- ⚠ **HONESTY NOTE, stated rather than buried**: S52's window is *"by 2026-08-06"* and this stage runs
  at **09:11 ET on 08-06** — roughly **15 hours of the final day remain, including the whole US
  session and AMC.** The verdict above is scored on everything published through this clock and is
  **re-checked at DRIFT (stage 10) before writeback.** If either branch fires intraday, DRIFT owns the
  correction.

### ★★★ 2a-bis. The finding this stage hands to MACRO ahead of everything else

**The distillate bottleneck's physical object has a name, and it is not the Strait of Hormuz.**

| Measured | Value | Source |
|---|---|---|
| Russian crude processing, July 2026 | **3.51–3.6 mbpd = lowest since May 2002 (24-year low)**, ~⅓ below the seasonal average (2020–25 norm 5.3–5.6) | `[oilprice body 08-03, citing Bloomberg/Moscow Times]` + `[nasdaq/Barchart body, EA Analytics]` — **two independent bodies** |
| Ukrainian refinery strikes | **18 Russian refineries struck in July** (previous record 17); **>50 attacks this year hitting at least 24 of Russia's 34 largest refineries**; Omsk (440 kbpd, Russia's largest) among them | same two bodies |
| Russian fuel rationing | **~90% of Russian regions** under some form of fuel rationing or reported supply issue as of end-June | `[nasdaq/Barchart body]` |
| ⚠⚠ **Russian diesel/gasoline export ban** | **EXTENDED, not expired** — *"Last week, Russia extended its ban on most diesel and gasoline exports"* | `[oilprice body 08-03]` |
| Russia's rank | **world's #2 diesel exporter, after the US** | `[Vortexa via nasdaq/Barchart]` |

★★★ **S49's own registration named "Russian diesel-export-ban expiry 2026-07-31" as a dated catalyst.
It did not expire. It was extended.** That is a measured fact about the branch-B fire's *meaning* —
it belongs beside the **S49-ANNEX** objections, not inside the frozen score (S49 is **not** re-opened).

★★★ **And this is exactly the discrimination S55 exists to perform.** Applying **R46's rule** — *name
the physical object that sets the spread* — the object setting the distillate leg is **Russian
refining capacity plus a Russian export ban**, not a strait. **Opening Hormuz moves crude transit; it
does not restart a bombed refinery.** ⇒ **the "S49-B means the bottleneck is releasing" reading now
has a named physical counter-object**, and **S55's branch B is the live hypothesis, not the tail one.**
⚠ **C4 scope**: this does not assert the distillate premium rebuilds. It asserts that the mechanism
being priced (Hormuz) and the mechanism that built the spread (Russian refining) are **different
objects**, and the desk has been quoting one against the other.

### 2b. The four brackets that closed on the 2026-08-05 settle — SCORED

⚠ **Estimator verified before use (C1).** The RS convention was re-derived from scratch and
**reproduces the 08-05 run's independently-computed 08-04 figures to 0.1pp on all five names**:
STX −1.02 (they wrote −1.0) · MU −8.03 (−8.0) · WDC −0.07 (−0.1) · XOM RS20 +5.50 / RS60 −0.40
(+5.5 / −0.4) · XLB 5-day excess −4.76 (−4.76). **The instrument is not in question; only the bar is new.**

| ID | Frozen observable | **08-05 settled** | **Verdict** | vs the 08-05 pre-commitment |
|---|---|---|---|---|
| **S30** | median **RS20 vs SPY of {STX, MU, WDC}** > 0 (A) / ≤ 0 (B) | STX **−5.87** · MU **−9.13** · WDC **−8.93** ⇒ **median −8.93** | ★★ **FIRED-B** | pre-committed **B at a 1.0pp margin**; final bar **B by 8.93pp** |
| **S31** | XOM RS20 vs SPY **> +10** (A) / **≤ 0** (B) | **XOM RS20 +4.17 · RS60 +0.52** | 🚨 **`AMBIGUOUS`** — structural | pre-committed `AMBIGUOUS`; **confirmed on the final bar** |
| **S36** | XLB 5-day excess vs SPY **> 0 AND green count 0** (A) / **≤ 0 or greens > 0** (B) | **XLB −3.79pp** vs SPY | **FIRED-B** | pre-committed **B by 4.76pp**; final bar **B by 3.79pp** |
| **S53** | MPC + PSX guide: capture stable/improving (A) / compression·hedging lag·turnaround drag (B) / mixed (C) | **both A** — see below | **FIRED-A** (confirmatory, LOW information *by its own registration*) | was **carried**; now settled |

**★★ S30 — the knife-edge did not merely hold, it inverted direction.** The bracket's own compression
story ran **−23.7 (registration, 07-24) → −9.55 (08-03) → −1.0 (08-04) → −8.93 (08-05)**. Nine
sessions of relentless convergence toward branch A **reversed −7.9pp in a single session.** ⇒
**M149's decaying-stock reading is NOT falsified; the roll-off defence holds.**
★★★ **And the registration's own control pair says what the reversal means, in the direction the
desk did NOT get to claim**: DELL and HPE were **both already positive** on 08-04 (+3.84 / +15.87 on
08-05), so had S30 flipped, **the registration pre-committed the reading to IT-beta, not memory.**
It did not flip — so **the memory leg reversed while the IT-beta control pair stayed positive**,
which is the cleanest *memory-specific* signature the bracket could have produced. **Recorded because
the 08-05 HANDOVER wrote the opposite contingency down in advance and would have been bound by it.**

**★★ S31 — a bracket with a HOLE, confirmed twice.** A needs > +10, B needs ≤ 0, and **XOM finished
at +4.17, inside the unassigned corridor, exactly where it sat all week (+5.5 on 08-04).** Per L3,
`AMBIGUOUS` is **a finding about the scenario, not about the market**: the two branches do not
partition the observable's range and the **modal** outcome was given no meaning at registration.
⚠ Its branch labels also inherit **R39**. ⇒ **PREMORTEM must re-register with an exhaustive
partition, or retire it.** ★ One measured detail worth carrying: the 13.1pp RS20/RS60 gap at
registration closed to **+3.65pp (4.17 − 0.52)** and it closed **by RS20 falling, not RS60 rising** —
which is the exhaustion geometry the bracket was written to detect, arriving without a scoreable branch.

**★ S53 — both legs A, and the run records the dissent inside the print rather than smoothing it.**
- **PSX (08-05)**: revenue **$52.04bn (+55.3% y/y)**, EPS **$9.41 vs $7.68 consensus (+22.5%
  surprise)**; **worldwide refining margin $24.08/bbl vs a $23.15 four-analyst estimate**; guide —
  *"expects soaring refining margins will last through the next quarter and **into 2027**, as the
  impacts of supply disruptions from the war in Iran likely will continue to weigh on markets for
  fuels such as gasoline and diesel"* `[seekingalpha body + bloomberg title + Reuters via google_en,
  3 independent outlets]`. ⇒ **stable-to-improving capture. Branch A.**
- **MPC (08-04)**: *"Beats Q2 Earnings and Revenue Estimates"*, *"Q2 2026 earnings beat on refining
  margin surge"* `[nasdaq 4,847자 + yahoo_finance bodies]`; MPLX growth capex $2.9bn, 12.5%
  distribution growth targeted 2026–27. ⇒ **Branch A.**
- ⚠⚠ **C2 — the half that does not confirm, quoted in the same breath**: PSX's **Atlantic
  Basin/Europe margin printed $14.44/bbl against a $19.77 four-analyst estimate — a 27% MISS**, the
  only regional miss in the disclosure (Western/Pacific $29.65 vs $19.93, Central $29.56 vs $26.35,
  Gulf Coast $24.25 vs $22.42 all beat). **Branch A is scored on the guide, as registered. The
  regional dispersion is recorded as a fact, not folded into the verdict** — and **W5 (sub-sector
  dispersion) says a single "refining margin" label is again the wrong unit.**
- ⚠ **Registration's own caveat binds: n ≈ 1.** The prints are date-clustered 08-04/08-05 and are not
  independent samples (S1). **Branch A can only confirm; it changes no conclusion.**

### 2c. Every other ARMED row — classified and checked

**Condition-settled, against today's `[FRED]` pull (`asof` 08-04, T10YIE 08-05):**

| ID | Kill/branch line | Reading | Buffer | Δ vs 08-05 |
|---|---|---|---|---|
| **S9** | real 10y (`DFII10`) **≥ 2.55** | **2.40** | ✅ **15bp** | widened 12 → 15bp |
| **S23 / S51** | derived 2s10s **≤ +0.20** | `DGS10` **4.63** − `DGS2` **4.20** = **+0.43** | **23bp** | ⚠ flattened 2bp — **second consecutive move toward the line** |
| **S26** | HY OAS **≥ 3.10** | **2.73** | **37bp** | widened 32 → 37bp |
| **S41** | IG OAS **≥ 0.90** | **0.78** | **12bp** | unchanged |
| **S8** | Hormuz *"Strait open"* — **undated `[blank]`** | 🚨🚨 **5th consecutive run carried as un-scoreable, on the exact event that has now driven the tape for four sessions.** Must be `VOID`ed or re-registered **by a human**. Named for the fifth time, not dropped. |
| **S55** | (HO% − CL%) 5-session, anchor 08-04 → endpoint **08-11** | window **open, not elapsed** — nothing scored. See §2a-bis: its branch B now has a **named physical object** |
| **S57** | XLB 5-session excess **> +1.9** (A) / **< −2.4** (B) by 08-12 | running **−3.79pp** ⇒ inside branch B's region, **1.39pp past its line**. Not scored |
| **S61** | STNG+FRO vs SPY → 08-12 | running: **STNG RS20 −7.51 · FRO −4.55**, both negative and both **turned negative inside the last two sessions**. Not scored — but see §3, the STNG ledger row resolved on the same measurement |
| **S62** | {EMR,ETN,AME,PWR} median RS20 − XLU RS20 → **08-07** | **settles tomorrow** — named so the 08-07 run cannot discover it late |

**Date-settled, all future — dates recorded, no action:** S2 · S3 (~09/10) · S4 (~09 late) ·
**S5 (08-11)** · S13 (08-12) · S14/S14-num · S16 · S19 · S24 (08-12) · **S25 (08-08)** · S26 (08-12) ·
**S35 + S35-ANNEX (08-07)** · S37 (09-30) · S40 (09-30) · S41 (08-12) · S42 (08-12) · S46 (08-13) ·
**S47 (08-07)** · S48 (09-30) · **S51 (08-10, NFP 08-07)** · **S54 (08-10)** · **S56 (08-11, SPCX
unlock is TODAY 08-06)** · S57 (08-12) · **S58 (08-11)** · **S59 (08-12)** · **S60 (08-11)** ·
**S61 (08-12)** · **S62 (08-07)**.

**`EXPIRED` = 0 · silent skips = 0 · past-dated rows unscored = 0.**

⚠ **S56's underlying event is today.** The 08-05 feed already carries *"US Equity Markets Mixed as
SpaceX, AMD Shares Drop"* and *"US Equity Indexes Mixed as SpaceX Hits Nasdaq"* `[yahoo_finance]`
— **the unlock is being traded before it happens.** The bracket's window runs to 08-11 and is **not**
scored here; the pre-unlock drift is recorded so the 08-11 scoring is not read as a clean event study.

---

## 3. Both ledgers audited — SIX rows were due and FIVE were resolved this run

```
reject_ledger.py due  → 113 rows · 34 resolved · legacy (no revives_if) 0 · recheck-date due 6
missed_ledger.py due  →  63 rows ·  1 resolved · legacy (no enters_if)  0 · recheck-date due 0
```

⚠⚠ **Six due rows is the largest batch this desk has faced** — the 07-23 rejection cohort's
recheck dates all landed on the same day. **None is carried silently.**

| Filed | Ticker | Class | Call | The measurement that decided it |
|---|---|---|---|---|
| 07-23 | **STNG** | `A.flow미도착` | **reaffirmed** | revives_if needs RS20 vs SPY positive **3 consecutive** sessions. The streak reached **2** (07-31 +6.34, 08-03 +4.71) and **broke**: 08-04 −0.36, **08-05 −7.51**. ★ Cause is nameable and is not a flow judgement — **the Hormuz repricing deflates the war-risk tanker premium the rejection said had never arrived.** FRO reads the same sign (−4.55) |
| 07-23 | **STT** | `E.상관가드` | **reaffirmed** | Leg 1 fails on a hard fact: **MA was not trimmed or exited** (the 08-04 executions were MET +7, NDAQ +7, XLE −10 exit). ⚠ **Honest qualifier: STT's own structure IMPROVED** — CQ 30d breadth **4up:0down → 9up:0down**, next-q 5:0, CY 13:0, NY 14:0, CQ estimates +10.9%/90d. **The reaffirm rests on the correlation guard, not on the name** |
| 07-23 | **DDOG** | `B.모멘텀only` | **reaffirmed** | Leg 1: **PLAY23 still empty, no valuation factor measured ⇒ C5 unresolved** (D15). Leg 2 is **unreadable in the form registered** — CQ breadth now reads **1up:0down** while **36up:0down sits in the NEXT-quarter field**; the analyst cluster rolled the quarter boundary (**DDOG prints 08-06 pre-market**). RS20 +5.18 holds. ⇒ **new registration defect, §8** |
| 07-23 | **LMT** | `H.밸류소진` | **reaffirmed** | Both legs fail wide. Gap ran **514.36 → 568.59 (+10.54%)**; half-retrace needs ≤ **541.5**. The **lowest settled close since is 569.20**; today 577.60 = **+12.3% above the pre-gap close.** The gap has never been half-retraced. RTX not exited (RS20 +10.79) |
| 07-24 | **PYPL** | `H.밸류소진` | **reaffirmed** | An **AND** with exactly one leg flipped. ✅ **Leg 2 IS now met**: next-q breadth **0up:4down → 4up:1down**. ❌ Leg 1: the Stripe bid is **neither accepted nor lapsed** (freshest coverage 07-28, still framed as live). ★ **Sharpened, not repeated**: PYPL closed **57.93 against a 60.50 bid = 4.2% below terms** ⇒ it is a **merger-arb security**, the exact class **R40** identified. Its RS20 +26.82 is a bid, not a business |
| 07-28 | **JNJ** | `K.본문반증` | ⏳ **DEFERRED WITHIN THIS RUN — to SWEEP, not to the next run** | Its `revives_if` is *"a green with `vol_surge` ≥ 1.2, **or** any green from outside the HLTH top-6 by cap"* — **both legs read off `SECTOR_FLOW_US.json`, which stage 2 produces.** Resolving it now would mean quoting yesterday's flow file against a condition about today's. **Named here so it cannot be lost; SWEEP owns the `resolve` call.** |

- **Rejection ledger: legacy count 0 for a 10th consecutive run.** Rows 106 → **113**.
- **Missed ledger: 63 rows (56 → 63), 0 legacy, 0 due, 1 resolved.** ★ **`resolved` moved off zero for
  the first time** (0 of 56 → 1 of 63) — the 08-05 run named this as worsening two runs running.
  First rechecks still ahead: **08-14 (KR 073240, 000150)**, **08-16 (US ADM, CTAS)**, **08-18**.
- ⚠ **Signs are opposite and are NOT summed.** No combined figure appears in this run.
- ⚠ `missed_ledger score`'s first six rows remain `outcome_selected` (**D106**) — accumulation, never
  an edge. **Not quoted.**

---

## 4. Exposure state — the 방어 verdict held and the band breach NARROWED without the book moving

```
python -X utf8 scripts/exposure_rule.py state   → 2026-08-06, bench 069500.KS, [live/미정착]
```

| Field | 08-05 | **08-06** |
|---|---|---|
| Rule state | **방어** (직전 복귀) | **방어 (직전 방어)** — the transition consolidated |
| Bench close | 104,300 (+3.96%) `[정착]` | **98,900 (−5.18%)** · vs 20d high **−18.0%** · vs 20d low **+12.85%** · volume **0.62×** |
| Target invested | 55% | **55%** |
| Current invested (ledger row) | *(query failed)* | **70.9%** |
| **Band gap** | 🚨 +16.1pp | 🚨 **+15.9pp (밴드이탈, over-invested)** |
| Ledger depth | 29 rows | **30 rows**; cumulative decomposition **n=4** |

**Cumulative: total excess −2.13pp = cash −1.12pp + selection −1.00pp (n=4).**
⚠ **n=4 is indistinguishable from zero (C4)** and is quoted only to keep the counter rising.
⚠⚠ **And the cumulative figures MOVED from the 08-05 read (−9.16 = −4.03 + −5.14) to (−2.13 = −1.12 +
−1.00) on the same n=4.** The decomposition is **not stable at n=4** — recorded as a property of the
instrument at this sample size, not as an improvement in performance.

**Four caveats, unchanged in force:**
1. **This is the KR book's exposure rule** (`069500.KS`, KR contest bands). **NOT a US sizing input;
   no US stage may size off it (W1).**
2. `state` returns **`투자비중미상`** (no account query); `show` carries the **70.9%** row. **The `show`
   figure is quoted**, discrepancy stated.
3. 🚨 **`ARMED(TIMEFOLIO_EXECUTE=1)` is set in the environment — 4th consecutive run.** This is a
   **read-only research run**: no orders, no `--execute`, no order-desk staging. Recorded because a
   standing armed flag is something a human should see.
4. ⚠ The **08-05** ledger row carries `🚨timefolio조회실패:CDPError` and the **08-06** row is tagged
   `⚠미정착봉(장중·KIS실시간)`. **Not cold-starting** (30 rows) ⇒ the *state* verdict is quotable; the
   *decomposition* is not (caveat above).

---

## 5. Reconciliation — belief vs coverage (`module_report_tags show`)

| Class | Finding |
|---|---|
| **Belief without coverage** | **TSM and LNG** — held names **outside `us_top300`** ⇒ **no flow, RS or short axis exists for either.** TSM is a rank-1-cycle epicenter the grading instrument cannot see. **Unchanged for 8 runs**; needs a universe change (human). ⚠ **LNG prints TODAY** (it is on the 08-06 pre-market list beside COP/CEG/TRGP) **and the desk cannot measure it** |
| **Coverage without belief** | **SPG · ADM · CTAS · TRI · GM** — measured flow rows, no 4Phase ⇒ no thesis may be built on them. Filed as **coverage gaps, not rejections** |
| **Resolved-but-live** | 🚨 **PSX — `ACTION_TICKETS.md` still carries `CORE-STARTER (BUY) PSX` while ALPHA filed it 🔴RESOLVED on 08-02.** ⚠⚠ `core_pick` is **HUMAN-LOCKED and was NOT modified**. **D19 firing for a 10th consecutive run**; its rationale still descends from **R8, retracted 2026-07-22**. ★★ **And PSX printed last night with the single best guide language on the sheet** — which makes the stale ticket *look* vindicated by an argument it never made. **Named, not fixed, and the coincidence is flagged precisely so it is not mistaken for confirmation** |
| **Silently unindexable** | **28 of 300 universe tickers** return 0 regardless of coverage (M152 `_US_STOP`): A · AIG · ALL · C · CAT · CB · COST · **D** · F · FAST · **GS** · **ICE** · KR · LOW · **MA** · MET · MS · NOW · O · ON · PEG · PM · Q · SO · **T** · TT · **V** · **WELL**. ⚠⚠ **MA is on this list and §3's STT resolution turns on MA's holding status** — that status was taken from the **execution record**, not from a coverage read, precisely because a zero here is uninformative. ⚠⚠ **MET is on it too** and S58 scores 08-11 |

---

## 6. RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 indistinguishable · C5 arbitrary choice | **MACRO · every stage.** ★★★ **C1 was EXECUTED not cited** — the RS estimator was re-derived and reproduced the prior run's five independent figures to 0.1pp before any bracket was scored. ★★ **C2 binds three places today**: Hormuz expectation vs the Reuters pushback; PSX's four regional margin beats vs its **Atlantic Basin miss**; and the exposure ledger's moving decomposition |
| **S** | you make a statistical claim | S1 date-fold · S2 null · S3 power · S4 in-sample≠done · S5 short samples · S6 future labels | **Any stage citing a test.** ★★ **S1 binds §2b hardest** — four brackets settled on **one** final bar each, and **S30 moved 7.9pp on that single bar.** ★ **S5 binds §9's IC read** |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade** | **SWEEP · ALPHA.** ★★ **D74 binds SWEEP the moment the run crosses 09:30 ET.** ★★★ **D6 binds §2a hardest**: of the top Hormuz hits, the wsj/bloomberg/ft items are `[no body]` = **title-only, C-grade, direction only** — **the verdict was taken from the 2,626/3,153/3,525자 bodies, never from a title** |
| **W** | you write a conclusion | W1 cross-market · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** ★★★ **W1 binds twice**: the KR exposure rule is not a US input, and **`vol_surge`'s KR result does not transfer** (§9). ★★ **W5 binds the Energy verdict directly** — PSX's regional spread runs **$14.44 to $29.65 per barrel inside one company**, so "refining margin" is the wrong unit before "Energy" even is |
| **L** | lenses | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★★★ **L3 binds S31 for a second consecutive run** — a bracket whose branches do not partition its observable produced `AMBIGUOUS` **twice**, which is now a pattern, not an accident. ⚠ **L2 unrunnable on 61% of names attempted (M233)** — no cheapness claim where `margin_history` is blank (VLO · XOM · PLD · CSX · UNP · NSC) |

---

## 7. Stale flags and cleared suspensions

| Row | `asof` | Flag |
|---|---|---|
| Seed chain **M1–M19** | 2026-07 / 07-22 | ⚠ **M6 (MU fwd P/E 6.31×) is 15 days stale, superseded twice.** Cite M206 |
| **M22** 3-2-1 crack "99.5th pctile" | 07-21 | ⚠⚠ **DEAD as a level** (R30/D95). **Changes only** |
| **COT file** | 07-31 release | 🚨 **Byte-identical stale snapshot for a 5th read; next publication 2026-08-07 (tomorrow).** ⇒ **no copper/NDX/WTI positioning percentile may be leaned on this run.** Binds SWEEP and PREMORTEM |
| **`DTWEXBGS`** | 08-04 | ✅ **119.70, 3m +1.1%**, mid-range ⇒ **S57's premise holds: the Materials dollar leg is dormant by construction** |
| **`DFII10`** | 08-04 | ✅ **2.40 — buffer widened a second consecutive print** (12 → 15bp). ★ **The 07-2x "closest kill line on the board" framing is now two prints stale in the desk's favour** |
| **`NFCI`** | 07-31 | **−0.53**, loosening. No kill line |
| **`T10YIE`** | **08-05** | **2.22%, −0.23pp/90d** — ★ the **only** FRED series with an 08-05 print, and it is at the **bottom of its 365-day range (2.18–2.50)** |
| **`CATALYST_WATCH.json`** | 08-06 | ⚠ **D18 has fired 15+ times across both desks.** Not trusted as the binary source; MACRO re-pulls at ≥10 days (D26). ⚠ **D141: the STRUCTURAL block reads an empty data file** |
| **`core_pick` / `ACTION_TICKETS`** | 08-02 | 🚨 **D19, 10th run.** Human-locked, stale, and its own date (08-05) has now passed |
| **000660 ADR flow suspension** | ongoing | **STILL ON.** KR-owned; scored by the 08-06 KR run. **Not a US-desk read** |

**Cleared suspensions converted to dig instructions: ONE.** The **breakeven** series printed 08-05 at
**2.22%, a 365-day low neighbourhood, while the real 10y fell to 2.40% and crude fell 12%+ over three
sessions.** ⇒ **MACRO must decide whether falling breakevens + falling real rates + falling crude is a
disinflationary-relief signature or a demand signal** — the two have opposite sector implications and
**the desk has not distinguished them.**

---

## 8. Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's shape |
|---|---|---|
| **1** | ★★★ **The distillate spread's physical object is RUSSIAN refining, not the Strait.** 24-year-low processing, 24 of 34 largest refineries hit, export ban **extended** not expired, #2 diesel exporter. | **This is the run's central finding and it re-points S55's branch B at a named object.** ⇒ **DEEP-ENRG's mandate.** ⚠ **The trap is live in the feed** — an `Iranian AND refinery AND strike` query surfaces Russian refinery shutdowns at the top. **R46's rule is what caught it** |
| **2** | ★★★ **S31 produced `AMBIGUOUS` twice, and S8 is on its 5th unscoreable carry — on the exact event driving the tape.** | **Two Energy brackets are structurally unable to produce information.** **PREMORTEM owns re-registration with an exhaustive partition** (S31) and must state plainly that **S8 needs a human `VOID`** |
| **3** | ★★ **New registration defect: a breadth condition pinned to "current quarter" silently changes meaning at a quarter roll** (surfaced by DDOG's `revives_if`, §3). | Same family as **D157** (a branch comparing y/y against a sequential guide) and **D46**. **Three instances now — this is a class, and the fix is one sentence in the registration template: name the field AND the fiscal period** |
| **4** | ★★ **`vol_surge` cleared Bonferroni on the KR ledger yesterday and FELL BACK BELOW IT today** (§9). | **The desk's first-ever pre-registered gate condition to fire un-fired itself in one session.** ⇒ **the interim rule (decompose which axis lit a green) is validated; the gate change stays un-made (P4)** |
| **5** | ★★ **PSX's intra-company margin spread is 2.05× ($14.44 Atlantic Basin vs $29.65 Western/Pacific)** while the desk carries one "refining" label. | **W5 with a receipt.** Feeds DEEP-ENRG directly and is the first hard number the desk has on **geographic** dispersion inside a refiner |
| **6** | ★ **US `rs60` h=1: IC −0.0942, t(NW) −2.54, n_eff 14 — 유의(단독), NOT Bonferroni**, negative sign at two horizons. | **The desk's own 60-day relative-strength ranking carries a negative sign on the US board.** ⚠ Crash+rebound window; **reported, not acted on (P4)** |
| **7** | **D9 · D10 · D11 · D15 · D17 · D19 · D20 · D22 · D104 · D141 · D151 · D152 · D155 · D157 · D159 · D161 · D165** *(open defects, human-gated)* | Carried forward, not silently re-discovered. **D165 (truncation) and D155 (the wall-clock date bug) destroy or falsify data rather than merely cost a stage** |

**New digs registered by this stage:** the quarter-roll defect (rank 3) — **ID assigned at writeback.**
**ID counters verified at read time** (D137's grep requirement, run against all `handoff/*.md`):
**highest `M###` = M415 · `D###` = D182 · `R##` = R48 · `S##` = S62 (US)** ⇒ this run takes
**M416+ · D183+ · R49+ · S63+**.

---

## 9. ★★ The signal scoreboard — a pre-registered gate condition fired yesterday and UN-FIRED today

| Market | Axis | h | n | n_eff | mean IC | t(NW) | verdict |
|---|---|---|---|---|---|---|---|
| **KR** | `vol_surge` | 1 | 19 | 19.0 | **−0.0439** | **−2.65** | **유의(단독)** — ⚠ **was −2.93 = Bonferroni-clear on 08-05** |
| **US** | `rs60` | 1 | 14 | 14.0 | **−0.0942** | **−2.54** | 유의(단독), **not** Bonferroni |
| **US** | `vol_surge` | 1 | 14 | 14.0 | **+0.0267** | +1.36 | **구분 불가 — and the sign is OPPOSITE KR's** |

★★★ **The 08-05 KR run recorded `vol_surge` clearing Bonferroni (t −2.93, n_eff 18) as *"a
pre-registered gate condition FIRED on the desk's own instrument"* and registered D161 on it. One
session later, at n_eff 19, it reads t −2.65 — back below the |t| > 2.8 line.** ⇒ **exactly the
instability S5 and the 필요n caveat predict at this sample size, observed on the desk's own headline
result within 24 hours.**

**What this settles and what it does not:**
- ✅ **The interim RULE is vindicated and it transfers as method (not as a conclusion, W1)**: *no stage
  cites a 🟢 tag without decomposing which axis lit it.* **A gate that flips across one session is a
  gate whose output must be decomposed every time.** Binds **SWEEP · ROTATION · ALPHA**.
- ⛔ **The gate change stays un-made (P4).** `sector_flow`'s 🟢 verdict still weights `vol_surge`
  **positively** while the KR ledger measures it **negative** — but the evidence just moved back below
  the desk's own pre-registered threshold. **Do not flip a live shared module on a result that
  un-fired.**
- ⚠ **W1 twice over**: the KR sign is negative, the US sign is **positive**, both `구분 불가`-to-marginal.
  **Neither market's reading may be imported into the other.**
- ⚠ **Regime label, as the unit requires**: the window is a crash-plus-rebound stretch. **A
  crash-window IC does not generalise.**
- ⚠ **`n_eff < 4` cells (14 of 21 KR, 11 of 15 US) are not quoted anywhere in this run.**

---

## 10. What this stage hands forward

1. ★★★ **The physical object that built the distillate spread is Russian refining capacity plus an
   EXTENDED Russian export ban — not the Strait of Hormuz.** S49's registration named that ban's
   *expiry* as a dated catalyst; **it did not expire.** ⇒ **S55's branch B has a named object; DEEP-ENRG
   owns it.** S49 is **not** re-opened.
2. ★★★ **S52 = C (provisional).** The **evidence class branch A demanded arrived** — a direct
   Iran-government statement, 8+ outlets — **and it carries no date, no "effective" language, and an
   explicit disclaimer that it does not guarantee passage.** DRIFT re-checks before writeback.
3. ★★ **R46's category rule caught a live trap**: an `Iranian AND refinery AND strike` query surfaces
   **Russian** refinery shutdowns at the top. **A title-level read fires S52-B on the wrong country.**
4. **Four brackets scored on the 08-05 settle: S30 FIRED-B (reversed 7.9pp off the knife-edge, with the
   IT-beta control pair NOT confirming ⇒ a memory-specific signature), S31 `AMBIGUOUS` for a second
   time (branch hole — PREMORTEM must re-register or retire), S36 FIRED-B, S53 FIRED-A (confirmatory,
   low information by its own registration, with the Atlantic Basin miss recorded beside it).**
5. **Six rejection rows came due — five resolved on fresh measurement, one (JNJ) deferred to SWEEP
   INSIDE this run** because its condition reads off the flow file stage 2 produces. **Zero rows cross
   a second HANDOVER unexamined; legacy 0 for a 10th run.** ★ **The missed ledger's `resolved` count
   moved off zero.**
6. ★★ **The desk's first pre-registered gate condition fired on 08-05 and un-fired on 08-06.** Method
   rule transfers; **the code change does not get made (P4)**.
7. ⚠ **The COT file is stale for a 5th read; it publishes tomorrow (08-07).** No positioning percentile
   may be leaned on today.
8. **Today/tonight is dense: DDOG · COP · CEG · LNG · TRGP · SRE · BDX · WBD print pre-market; the
   SPCX unlock is today (S56, already being traded ahead); S62 settles 08-07 alongside S35/S47 and
   NFP.** **PREMORTEM must produce both-sides brackets** — a one-way tilt into a known binary is a
   protocol violation, **and S58 exists because that violation already happened once.**
9. ⚠ **`ARMED(TIMEFOLIO_EXECUTE=1)` is set for a 4th run.** This run touches nothing executable.

**No position sizing, no buy/sell language appears anywhere in this carry (P4).**

---

## 11 · ⚠⚠ Retention budget

`python -X utf8 scripts/handoff_compact.py --budget-only` — **run at writeback (stage 10) so the
figure reflects this run's own additions rather than a mid-run snapshot.** The 08-05 run measured the
US read at **877.4 KB against a 250 KB budget, growing +158.1 KB in one day**, and escalated
compaction from an efficiency item to a **safety** item: the larger these files get, the longer a
writeback holds a handle open, and the more a single encoding fault destroys (**D165**).
★ **Fourth consecutive run naming it. The instrument exists (`handoff_compact.py`, non-destructive —
facts move to `ARCHIVE_FACTS.md` and stay greppable). What is missing is that nobody runs it.**
