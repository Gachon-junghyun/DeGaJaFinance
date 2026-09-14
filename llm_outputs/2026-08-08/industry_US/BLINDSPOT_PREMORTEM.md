# BLINDSPOT_PREMORTEM — industry_US · 2026-08-08 (Sat) · Stage 6/10 ★US-only

> Four adversarial lenses, run as a **parallel Agent fan-out in ONE message** — not in-context.
> (The 08-03 and 08-04 runs self-reported in-context execution as a weakness; 08-07 restored the
> fan-out. This run keeps it, a second consecutive time.)
> Zero buy/sell language and zero sizing anywhere in this file (P4).

## ★★★ HEADLINE — three of the four lenses corrected THIS RUN'S OWN EARLIER STAGES

This is the outcome the stage exists to produce, and it happened on three independent axes:

| # | What an earlier stage of THIS run wrote | Which lens killed it, and with what |
|---|---|---|
| **1** | **MACRO §F warning #4**: *"three of the eleven tilts (ENRG, MATR, UTIL) are driven by the SAME variable — the path of rate expectations"* | **Lens 2.** **Wrong grouping.** ENRG's tape is dominated by the **Hormuz supply narrative**, not real yields — XLE is **−6.95pp vs SPY over 5 sessions and already past its own bearish bracket (S60, ≤ −5.05)** for reasons unrelated to rates. **The actual concentration is INDU + FIN + MATR + UTIL — four tilts, four GICS labels, one event**: a *hawkish-or-neutral* CPI keeps December's 77% hike intact and the curve steep-but-contained, and **a cool CPI hits all four simultaneously.** ⇒ **the warning was one tilt too small AND named the wrong member.** **Adopted; MACRO's version is superseded** |
| **2** | **The PREMORTEM brief itself** (written by this stage) stated *"AMD, MU, VST, GEV, CAT all show strongly negative rs20 against positive-or-flat rs60"* | **Lens 3.** **True of 2 of 5.** Measured rs60 vs SPY: AMD **+3.1** · MU **+9.7** (positive) · **VST −9.0 · GEV −12.4 · CAT −12.4 (NEGATIVE on BOTH windows)**. ⇒ three of the five are **not** "a dip inside an uptrend" by their own RS geometry; **the brief handed the lens a false premise and the lens refused it.** ⚠ **Recorded as this stage's own error, not smoothed** |
| **3** | **`EVENT_ALPHA.md` Card 1's stated KILL condition**: *"if the PUCT/ERCOT audit is reported as a freeze covering already-announced projects, the card is dead — Kilby is a Reeves County project inside ERCOT"* | **Lens 4.** **The premise is wrong: Project Kilby is BEHIND-THE-METER generation, explicitly routed AROUND the ERCOT interconnection queue.** ⇒ **Abbott's audit does not gate it**, and Card 1's kill condition **cannot fire by construction** — the same defect class as **R46** (a kill condition naming the wrong object: then a strait vs a facility, here a queue vs a private wire). ⇒ **Card 1's kill condition is VOID and replaced in §4** |

★ **And one lens confirmed the desk rather than correcting it**: **Lens 1 independently declined HLTH**
for the same reason ROTATION did, on evidence ROTATION did not have — **every HLTH green's next
earnings date is 10+ weeks out** (BMY 10-29 · AMGN 11-04 · WAT 10-30 · IDXX 11-02 · MRK 10-29). **The
best breadth on the board has no clock.**

---

## §1 · Lens 1 — UNDER-COMPUTED LEGS → **one PROMOTE-TO-DEEP**

| Leg | Named exposure | Catalyst in window | Verdict |
|---|---|---|---|
| **IT / optical-interconnect** | **COHR** 🟢가속 flow +0.833, rs20 vs SPY **+14.4**, rs60 −3.4 · **`vol_surge` 1.30, `velocity` None ⇒ VOLUME-lit, not a velocity artifact** · peer **LITE** 🟡 +0.615, rs20 +8.6 · but **CIEN −0.906 and GLW −0.756 are deep red — the layer is NOT moving as a block** | ✅ **COHR earnings 2026-08-13**, confirmed independently by this orchestrator against yfinance's calendar (`Earnings Date 2026-08-13`, consensus EPS **1.617**, revenue **$1.981bn**). ⚠ **Lens 1 flagged a source conflict** — a Barchart/Yahoo title reads *"Mark Your Calendars for August 12"*. **Resolved to 08-13 on the calendar object; the conflict is recorded, not hidden** (a `D18` instance) | 🟢 **PROMOTE-TO-DEEP** |
| **HLTH breadth** | BMY 🟢 (`vol_surge` 1.31) · AMGN 🟢 (1.23) · WAT 🟢 (1.24) · IDXX 🟢 (1.44) — **volume-lit** · MRK 🟢 (0.90, `velocity` 1.73 — **velocity-lit, the one exception**) | 🚫 **NONE — every name reports 10+ weeks out** | **WITHIN-RUN-WATCH** |
| **UTIL / AI-power** | **CEG 🟡중립 flow −0.034** (not green at all), rs20 vs SPY +4.9, rs60 **−12.8** · **PCG 🟡 +0.604** (UTIL's best flow score) but rs20 **−0.7** = price-flat on `vol_surge` 1.54 | 🚫 **NONE.** CEG **already printed 08-06** (Q2 EPS $2.55 vs $1.91 y/y, plus **920 MW of new long-term PPAs including a Walmart nuclear deal**) — **before this window opens.** The PUCT/ERCOT audit has **no scheduled resolution date** | **WITHIN-RUN-WATCH (weak)** |

### 🟢 A 5th DEEP slot is PROMOTED: **DEEP-IT (optical/interconnect)**

**Grounds, all three measured**: (i) **COHR is the board's ONLY `new_green` across 300 names**;
(ii) it is **volume-lit**, so it is not the R59/D205 velocity artifact that hollowed out Energy's and
Financials' flow ranks this run; (iii) it has a **name-specific dated catalyst inside the window
(08-13)** — the only one any lens found — **and `S48` already owns this exact node** (registered
2026-07-28, settles 09-30). ⇒ **N = 4 → 5.** **DEEP slots: continuous [INDU, ENRG] · rotating [MATR,
FIN] · promoted [IT-optical].**
⚠ **What the promotion must NOT assume**: **CIEN −0.906 and GLW −0.756 are deep red**, so the DEEP's
first job is to establish whether this is an *interconnect layer* igniting or **a single name**.

---

## §2 · Lens 2 — REGIME-FLIP / BOTH-SIDES → two brackets registered, one existing bracket disarmed

### 2a · 🚨🚨 **`S61` is not merely reachable — it is statistically PRE-DETERMINED to fire, and that is a NEW defect class**

**Measured**: S61's observable sits **−4.184 against branch B's −4.19 — a 0.006pp gap** — while the
instruments carrying it price **±7.2% (STNG) and ±8.7% (FRO)** implied moves through their D13
(08-21) expiry. ⇒ **the bracket will cross branch B on ordinary noise regardless of what happens in
the strait.**

> ⚠⚠ **`S61-ANNEX` is EXTENDED (S61 is NOT re-frozen, bands unchanged): an S61 branch-B fire may NOT
> be read as evidence about Hormuz, in either direction.** MACRO §E already recorded that branch B's
> *label* is wrong (the mechanism is tonne-mile destruction, not absent premium). **Lens 2 adds that
> its *information content* is also gone.** **Both defects are on the record BEFORE the 08-12 settle.**

★★★ **This is the sibling of `D206` and it is the opposite failure**: D206 catalogued a branch that
became **unreachable** (S62's branch A, 19.16pp away at its settle). **S61's branch B has become
INEVITABLE.** ⇒ **new dig `D216`: reachability must be checked in BOTH directions — a branch sitting
inside a fraction of the observable's own implied move is as uninformative as one sitting outside its
range.** **Both are now measured on this desk within one week.**

### 2b · ⚠ The option-implied thresholds do not span the event the desk cares about

| Instrument | Implied move | Expiry | Spans CPI (08-12) / PPI (08-13)? |
|---|---|---|---|
| **GLD ±0.8% · TLT ±0.5% · QQQ ±1.0%** | small | **D2 = 08-10** | 🚫 **NO — these expire BEFORE the print and price NONE of it** |
| **XLU ±1.8% · XLE ±2.7% · XLB ±2.1% · JPM ±2.1%** | — | D6 = 08-14 | ✅ yes |
| **USO ±5.0%** | — | D4 = 08-12 | ✅ **the cleanest single-event read for CPI day itself** |
| STNG ±7.2% · FRO ±8.7% · CPER ±5.3% · UUP ±0.9% | — | D13 = 08-21 | ✅ but absorbs two weeks of noise |

⚠⚠ **`S50-ANNEX`'s standing warning reproduces**: *the straddle covers the path to expiry, not the
event.* **A D2 straddle quoted against a D4 binary is not "what is priced" — it is a different
question.** **Named so no stage quotes GLD's ±0.8% as the CPI's implied move.**

⇒ ★ **And this immediately downgrades `S57`**: its branch A sits **0.59pp away** while **XLB's own
D6 implied move is ±2.1%** — **the threshold is INSIDE what is already priced**, so a branch-A fire
carries little information even before `S57-ANNEX`'s three meaning-failures are applied.
**`S57-ANNEX` is EXTENDED with this fourth measurement. S57 is NOT re-frozen.**

### 2c · New primary evidence on Hormuz, dated today — and it points BOTH ways (C2)

- **Against a reopening** `[IRGC statement, 2026-08-08]`: **"Hormuz to open if US accepts Iran's
  terms"**, and the reopening **"does not depend on how talks with Oman develop"** ⇒ **conditional and
  multi-party — and it explicitly detaches the process from the Oman channel that `S52`'s branch-A
  evidence ran through.**
- **Escalation, same window** `[dw 2026-08-08]`: **the UAE says Iran targeted a tanker transiting
  Hormuz.**
- **For a reopening** `[wsj 08-05]`: oil declined *"amid growing optimism over reopening"* ⇒ **the
  de-escalation case is already IN the tape** (XLE −6.95pp vs SPY over 5 sessions).

⇒ **`S52` FIRED-C on 08-06 and is not reopened.** But **the IRGC line is the FIFTH escalating
near-miss the threshold has refused**, and it is the first that **detaches the mechanism from the
Oman channel**. **Handed to the next run as S52's successor-registration question.**

### 2d · 🆕 **`S71` — the CPI→PPI divergence, the one genuinely un-covered falsifiable gap**

> **ID checked at write time (D137/D76)**: `grep S71` and `grep S72` = **0 hits in all nine
> `handoff/*.md`**. Highest existing **S70 (US, registered by this run's MACRO) / S56-KR (KR)**.

**Why it exists.** Lens 2's finding: **a cool CPI followed by a hot PPI is the one path that hits all
four members of the real correlated cluster (INDU · FIN · MATR · UTIL) and leaves none of them
relieved** — MATR/UTIL rally 08-12 then reverse 08-13. **No registered bracket covers a two-day
divergence**, and **every existing row settles either 08-11 (before CPI) or 08-12/13 on a level, not
on a reversal.** ⇒ **the desk currently has no instrument that can tell a real CPI reaction from
noise.**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (the CPI reaction was REAL)** | **Δ ≥ +1.57pp** — i.e. XLU's 1-session excess vs SPY on **08-13** MINUS its 1-session excess vs SPY on **08-12**, ≥ the 85th percentile | The two prints agree; the duration read established on CPI day **extends**. The four-tilt cluster's exposure is directional and must be treated as one bet |
| **B (the CPI reaction REVERSED)** | **Δ ≤ −1.69pp** (15th percentile) | PPI contradicts CPI ⇒ **any conclusion drawn from the CPI print alone is falsified**, and the whipsaw is the finding |
| **C** | between | The two prints did not disagree materially. No conclusion changes |

- **Frozen observable**: `XLU` minus `SPY`, **1-session % excess on settled daily closes**, yfinance,
  `auto_adjust=False`, **benchmark named inline (C1)**; the quantity is the **08-13 value minus the
  08-12 value**. **Anchor and endpoint are both in the future at registration ⇒ no look-ahead.**
- ★ **D93 executed BEFORE freezing.** Trailing **252** settled sessions of that exact day-over-day
  change: **mean +0.0063pp · sd 1.6268pp · q15 −1.686 · q85 +1.571.** **Bands taken at the measured
  quantiles, not round numbers.** ⚠ **The estimator's centre is +0.0063, not zero** — disclosed at
  registration (this desk's D93 bias, now reproduced a **sixth** time).
- **Why XLU is the leg**: it is the **most rate-sensitive** of the four cluster members and the one
  with **no live bracket at all** (S62 settled; S63's DUR composite settles 08-13 on a *level*, not a
  reversal). **Lens 2 named it explicitly.**
- **Information content (L3)**: **branch B FALSIFIES** — it kills any conclusion drawn from CPI day.
  **Branch A confirms and also sizes the cluster question.** **Neither is degenerate**: ±1.6pp against
  an sd of 1.63pp is a **~1σ** ask over one session, and **XLU's own D6 implied move is ±1.8%**, so
  both branches sit **at the edge of, not inside, what is priced.** ⇒ **this bracket passes the test
  S57 fails.**
- ⚠ **Anti-signal, BOTH sides (the D191 two-sided rule)**: **(a)** if **either** print is delayed or
  released off-schedule, the row is **`VOID`**, not re-dated; **(b)** if a **non-macro, XLU-specific
  event** lands on 08-12 or 08-13 (a large-cap utility M&A headline, an ERCOT emergency), the row is
  **`AMBIGUOUS`** — the contamination class that VOIDed S43 and that S52's own scoring caught.
- **Owner**: `industry_US`. **Settles at the 2026-08-13 settled close.**

### 2e · 🆕 **`S72` — is the four-tilt cluster ONE bet? Lens 2's claim, bracketed against itself**

**Why it exists.** Lens 2 asserts the real concentration is **INDU + FIN + MATR + UTIL**, not MACRO's
**ENRG + MATR + UTIL**. **Two stages of one run now disagree about which tilts are correlated**, and
**the desk has been burned by correlated tilts wearing different GICS labels three times (R7, R10,
S62).** ⇒ **the disagreement is registered rather than resolved by picking a side (§6 discipline).**

| Branch | Frozen observable | Meaning |
|---|---|---|
| **A (Lens 2 is right — it IS one bet)** | On the **08-12 CPI-day settled close**, the **1-session excess vs SPY of XLI, XLF, XLB and XLU all carry the SAME SIGN** | Four GICS labels, one macro exposure. **MACRO's warning was one tilt too small and named the wrong member**, and the board's real risk unit is 4-wide |
| **B (MACRO is right — ENRG belongs and INDU/FIN do not)** | **XLE's 1-session excess vs SPY shares the sign of XLB and XLU on 08-12, while XLI and XLF do NOT** | The rate path is the shared driver and Energy is inside it; Lens 2's Hormuz-detachment argument fails |
| **C** | any other sign pattern | **Neither decomposition survives** — the labels are not a risk unit and **both stages were wrong** |

- **Frozen observable**: 1-session % excess vs **SPY** (named inline) of **XLI, XLF, XLB, XLU, XLE** on
  the **2026-08-12 settled close**, yfinance, `auto_adjust=False`.
- **State at registration, disclosed**: on the **08-07** settle the five read **XLI −0.38 · XLF −0.97
  · XLB +0.71 · XLU −0.08 · XLE −1.75** ⇒ **branch A is NOT currently true** (XLB's sign differs),
  and **branch B is NOT currently true** (XLE and XLU agree but XLB does not). **Today is a C.**
- **Information content (L3)**: **all three branches change a conclusion**, and **C is the modal and
  most informative** — it would retire a risk-unit framing both stages currently use. ⚠ **This is a
  SIGN-PATTERN bracket, so no D93 band is needed** and none is invented; **its weakness is that a
  near-zero excess can flip sign on noise**, and that is disclosed here rather than discovered at
  scoring: **any leg reading |excess| < 0.20pp is recorded as `flat` and the row scores `AMBIGUOUS`
  rather than being forced into a sign.**
- ⚠ **Anti-signal, BOTH sides**: **(a)** a CPI delay ⇒ **`VOID`**; **(b)** an intraday circuit-breaker
  or a market-wide halt truncating 08-12 ⇒ **`VOID`**.
- **Owner**: `industry_US`. **Settles at the 2026-08-12 settled close.**

---

## §3 · Lens 3 — MOMENTUM RE-TAGS, and the one that changes a live bracket's reading

| Name | Tag | The KPI it is judged on (not price) | Last-20 share of the 60d excess vs SPY | Flip condition |
|---|---|---|---|---|
| **PLTR** | **EXTENDED-BUT-LIVE**, flagged | Revision breadth **3↑/0↓** 30d current-yr and next-yr, FY +9.3%/90d. ⚠ **L2 peak-margin: op margin 26.8→33.3→40.9→46.2→47.1% = the PEAK of its own trailing 5Q, at a 74.8× forward multiple** — **not** the low-multiple/peak-margin trap but **its inverse: a peak margin at a peak multiple** | **RS60−RS20 = −11.5** ⇒ days 21–60 were *negative*; **the entire 60d excess is a last-20 event** | any single downgrade breaking 100% breadth, or a **sequential** margin decline |
| **ANET** | **EXTENDED-BUT-LIVE** — textbook pause, not distribution | Revision breadth **unanimous and accelerating**: current-qtr 3↑/0↓, FY 3↑/0↓, **next-FY 4↑/0↓, +15.4%/90d**. OBV still 매집 (+0.158) | **RS60−RS20 = +29.1** ⇒ **broad-based**; the 20-day cooling is small next to the base | OBV turns 분산, or rs20 stays negative through the next print |
| **MPC · VLO · PSX** | **EXTENDED-BUT-LIVE, and UNDER-recognised by price** | ★★★ **FY 30d revision breadth 13↑/0↓ (MPC) · 13↑/2↓ (VLO) · 13↑/2↓ (PSX)** with **FY EPS +84% / +49% / +60% over 90 days** | **RS60−RS20 = +10.9 / +12.1 / +5.7** ⇒ **broad-based, the opposite shape to COHR and NEM** | crack reversal, or FY breadth turning net-negative |
| 🚨 **NEM** | **EXHAUSTED on the KPI axis** | ★★★ **Revision breadth is strongly NEGATIVE: current-qtr 0↑/9↓ · FY 1↑/9↓ · next-FY 2↑/13↓ · FY estimate −8.9%/90d.** **Estimates are being CUT while the price rips on gold spot** | **RS60−RS20 = −26.5**, the most extreme last-20 concentration checked, on a 60-day base that is itself **−10.4pp vs SPY** | revision breadth turning net-positive, or gold giving back the week |
| **SHOP** | EXTENDED-BUT-LIVE, weaker | FY 30d **2↑/3↓** — breadth *decelerating* while price accelerates. Margin 17.6% vs 20.3% two quarters back = **mid-range, not peak** | **RS60−RS20 = +25.8** ⇒ broad-based | one more FY downgrade tips breadth net-negative |
| **COHR** | EXTENDED-BUT-LIVE, **event-shaped** | FY 30d 4↑/0↓, next-FY 5↑/1↓, +7.5%/90d | **RS60−RS20 = −17.8** ⇒ the whole move sits on a **negative** 60-day base | **the 08-13 print itself** |
| **FCX** | data gap, leaning **EXHAUSTED** | `[unavailable]` — revision breadth and margin not pulled | RS60−RS20 = −10.0, flat base | **copper COT went 96th → 100th percentile, +9,842 ADDED** — more crowded, not less |

### 3a · ★★★ **NEM independently confirms `S57-ANNEX`, from an axis the annex never used**

`S57-ANNEX` was registered in MACRO §E on **flow and positioning** grounds (0🟢 of 12; the dollar's
spec long at the 81st percentile and building; copper at the 100th). **Lens 3 arrives at the same
verdict from ESTIMATE REVISIONS — a completely independent instrument — and it is the strongest
version of the finding yet**: *the single name carrying the entire Materials move is having its
earnings estimates cut 9-to-1 while its price makes a 7-week high.* ⇒ **the annex now rests on four
independent legs (flow · dollar positioning · copper positioning · revision breadth).**

### 3b · The reversals, adjudicated on non-price evidence

| Name | Verdict | The non-price evidence |
|---|---|---|
| **AMD** | **dip inside a live cycle** | Q3 guidance **$13.0bn vs $12.51bn consensus — a BEAT**; the stock fell because it *"wasn't enough"* `[yahoo_finance 08-06]`. Revision breadth **11↑/1↓** FY 30d, +19.8%/90d next-yr ⇒ **a valuation reset on a beat, not deterioration** |
| **CAT** | **dip inside a live cycle** | ★ **Record $72.1bn order backlog (+$9.4bn in-quarter)**, raised 2026 sales-growth target, **cut** its full-year tariff-cost forecast `[Reuters/yahoo 08-04]`. FINRA short-vol z **0.74 = normal**, no distribution signature |
| 🚨 **VST** | **closer to DISTRIBUTION** | **The only name in the set where two non-price instruments agree**: FINRA short-vol **z +1.56 🔴극단**, and revision breadth **net negative** (FY 1↑/2↓, next-yr **0↑/3↓**, next-yr EPS −1.1%/90d) |
| **MU** | **mixed — an early-crack signal** | ★★★ Trailing breadth is extreme (FY 29↑/1↓, +26.7%/90d) **but stale against a fresh driver-based caution**: **Citi cut its target to $1,150 from $1,400 on a forecast that DRAM/NAND pricing "could begin slowing… with prices likely peaking in Q2 next year"** `[yahoo_finance 08-08]` |
| **GEV** | **genuinely AMBIGUOUS — `[unavailable]`** | Current-yr breadth 7↑/10↓ but **next-yr 16↑/2↓, +2.8%**. No fresh negative catalyst in a 7-day sweep. **Lens 3 declined to force a call** |

★★★ **The MU item is the most consequential single sentence any lens returned**, because it lands
directly on **`STANDING_VIEW.md §1 — the desk's regime call** (*"memory is a price-cycle industry in
rate-of-change deceleration while its level stays tight"*). **A sell-side house has now put a DATE on
the deceleration — "prices likely peaking in Q2 next year."** ⚠ **It is a sell-side forecast, not a
measurement, and it does NOT update `M1` (the TrendForce contract series).** It is recorded as a
**third-party corroboration of the regime call's direction with a dated horizon**, tagged
`[news, single house]`, **and it may not be cited as evidence** — but **`S3` (4Q26 DRAM contract
guidance) and `S4` (Micron FQ4) are the rows that will settle it, and both are already armed.**

---

## §4 · Lens 4 — CYCLE EXPOSURE: a code defect, a mis-slotted chain, and a stale registry rationale

### 4a · 🚨🚨 **A CODE finding: the rank-3 GAP check cannot fire, and setting the threshold will not fix it**

`scripts/cycle_exposure.py:87`:
```
gap = (cyc["rank"] <= 2) and (epi_pct_tot < min_epicenter_pct)
```
⇒ **the `rank <= 2` clause excludes rank-3 categorically, regardless of any floor value.** The
`⚪ 기준 미설정` that every recent run has reported as *"a registry field a human must set"* is
**only half the defect** — **setting `min_epicenter_pct` for rank 3 changes nothing while the boolean
gate stands.** ⇒ **new dig `D217`. Both the value and the predicate must change together, and both are
human-gated.**

⚠ **And it has a measured cost, today**: `KIS_DESK_20260808.md` records **RTX cut 4 → 3 shares
(7.29% → 5.47% of book)**, with the stated reason being **the gate's structural non-firing** — i.e.
**a position moved because a guard could not fire, not because a thesis changed.**
⚠ **Threshold design (proposed, NOT set — P5):** the rank-3 rationale is specifically that **RTX
decouples from the other primes**, so a floor should key on **RTX's relative-accumulation edge over
the {LMT, NOC, GD, LHX} median (OBV / RS60 spread)** — a test of the registry's own stated logic —
rather than an arbitrary %-of-book number that cannot test it.

### 4b · The rank-3 rationale is STALE — the complex has converged

`core_pick_why` (dated 07-17) singles RTX out because LMT/NOC were *"distributing"*. **Measured today,
all five primes are 🟡중립 with OBV 매집 together** (rs20 / rs60, both vs **SPY**):

| | RTX | LMT | NOC | GD | LHX |
|---|---|---|---|---|---|
| rs20 | **+11.4** | +9.9 | +3.5 | +2.1 | −3.8 |
| rs60 | **+19.9** | +8.1 | −2.4 | +8.4 | −12.1 |

⇒ **RTX is still best-in-complex, but the registry's reason for treating it as *differentiated* rather
than sector-beta no longer holds.** ⚠ And **no RTX-specific news thread exists in a 7-day foreign
window** — verified independently by Lens 4 (`fts search RTX Raytheon --days 5 --scope foreign
--mode and` returns one analyst peer-comparison piece built around an 08-03 SPY-6 radar test, i.e.
commentary, not a catalyst).

### 4c · ★★★ The AI-power chain is not a missing CYCLE — it is a **MIS-SLOTTED** one, and that is worse

Lens 4's finding, and it corrects **this run's own EVENT_ALPHA framing** (see the headline table):

- **Project Kilby is BEHIND-THE-METER gas generation, explicitly routed around the ERCOT
  interconnection queue** ⇒ **Abbott's PUCT/ERCOT audit does not gate it.** **Card 1's kill condition
  is VOID by construction — the R46 class.**
- **The chain's participants are already in the registry with the WRONG driver attached**:
  **CVX sits in Energy/oil-refining's EPICENTER list** (`cycle_registry.json` line 22) though Kilby
  has nothing to do with crack spreads; **GEV sits in AI-compute's *adjacent* list** though it is
  power hardware, not compute; **CAT, TPL and EMR appear nowhere in the registry at all.**
- ⇒ **Measured epicenter exposure to the chain: effectively 0%.** The only touch is a pre-existing
  **ETN** sliver (4.12% of total) registered against AI-compute generically.
- ⚠⚠ **And `cycle_exposure.py` structurally cannot see it**: the chain IS already a scored bracket
  (**S62**, which FIRED-B on 08-07), **but S62 lives in `SCENARIOS_US.md` and the registry lives in
  `cycle_registry.json`** — **two ledgers, no link.** ⇒ **`D218`: a bracket that scores a cycle is
  invisible to the instrument that measures exposure to it.**

### 4d · **Card 1's KILL CONDITION, REPLACED**

The VOID condition is replaced with one that can actually fire on the corrected mechanism:

> **NEW KILL for EVENT_ALPHA Card 1**: *the card dies if **GEV and CAT both remain 🔴분산 through the
> 2026-08-13 sweep** while **CVX and MSFT remain 🟢** — i.e. the market sustains its verdict that the
> named suppliers do not capture the contract's value.* **A behind-the-meter project is not gated by a
> queue audit, so the regulatory kill was never available; the money is.**

### 4e · The two reconciliation claims — **both TESTED, both CONFIRMED**

- **XOM / S31**: `cycle_registry.json` **does** list XOM in the Energy epicenter set, but
  `CYCLE_EXPOSURE.json`'s **held** epicenter is **MPC, PSX only — XOM is not held.** S31's text
  (*"the only Energy name the book holds"*) is **false against today's read.** ✅ And XOM was
  **sanity-checked live** (last 153.04, `vol_surge` 0.88 ≠ 0, OHLC non-degenerate) — **not the EA
  failure mode.**
- **RTX / no live thread**: ✅ **confirmed by an independent pull** (§4b).

---

## §5 · Both-sides brackets per binary → handed to ALPHA's action bracket

| Binary | Against-us branch | Named expression (⚠ descriptive, NOT a recommendation) | Trigger | Invalidation |
|---|---|---|---|---|
| **CPI 2026-08-12** | **COOL** (core ≤ 0.15% m/m) — hits **all four** of INDU/FIN/MATR/UTIL at once | GLD · CPER · XLU · TLT long-duration/reflation vs **SPY**; UUP the short leg | core CPI m/m **≤ 0.15%**, **or** the 2y breaking **below 4.10%** (from 4.202%) within 24h | core **≥ 0.30%** m/m, or the 2y holding **> 4.20%** through the 08-13 close |
| **CPI 2026-08-12** | **HOT** (core ≥ 0.30% m/m) — **confirms** UTIL UW and MATR N−, but **hits ENRG N+** while XLE is already past S60's branch B | USO (**±5.0%, D4 = the cleanest single-event read**) · UUP · XLE vs **SPY** | core **≥ 0.30%** m/m | core ≤ 0.15%, **or a <2bp 2y move on the print (a dead reaction — itself a finding)** |
| **PPI 2026-08-13** | **cool CPI THEN hot PPI** — the only path that whipsaws every cluster member | same basket, **re-measured against the 08-12 close, NOT the pre-CPI anchor** | PPI final-demand **≥ +0.30% m/m the day after a CPI ≤ 0.15%** | both prints agree in direction | 
| **Hormuz (undated)** | **the stall/escalation branch** — already partly in the tape (XLE −6.95pp vs SPY) | STNG · FRO · USO vs **SPY** ⚠ **none of the four tanker names is in `us_top300`, so no flow tag exists for any of them (C3)** | a **dated** IRGC/Omani confirmation of transit resumption, **or** a second tanker incident confirmed by a shipping-insurer-grade source within 72h | **7 days pass with no confirmed transit change and no further incident** — the narrative stalls rather than resolves |

⚠⚠ **`S71` covers the PPI-divergence row and `S72` covers the cluster question. The two CPI rows are
covered by `S70` (credit) and `S63` (the DUR composite, 08-13) and need no new registration** — **and
saying so is the L3 discipline: if neither branch would change a conclusion, the bracket is spent
elsewhere.**

---

## §6 · Cycle-GAP flag and what goes to BET

| Flag | State |
|---|---|
| **Registry rank ≤ 2** | ✅ **no GAP** — AI-compute 19.74% (need 12.0%), Energy 10.23% (need 8.0%) |
| ⚠ **AI-compute's composition** | **Thinner than the headline**: **NVDA rs60 vs SPY −3.30 and AVGO rs60 −2.70** — two of three epicenter names are RS60-negative and **only ANET (+27.60) carries the 60-day window.** The floor clears on a 20-day repair |
| 🚨 **AI-power / behind-the-meter** | **~0% measured epicenter exposure**, and **structurally invisible** (§4c). ⚠ **This is a coverage finding, NOT a case for adding exposure** — the money is 🔴 on the named supplier layer (GEV −0.756, CAT −0.223) |
| 🚨 **rank-3** | **The GAP predicate cannot fire (D217)**, its rationale is stale (§4b), its held name has no live thread, **and the position was cut today because the guard could not fire** |

**To BET §B (candidates):** **COHR only** — the board's only `new_green`, volume-lit, with a
confirmed **08-13** catalyst and an existing bracket (`S48`) on its node. ⚠ **Everything else in this
file is analysis, not a candidate**, and the STORY-ONLY names (NEM · CVX · MSFT · GEV · CAT · STNG ·
FRO · CEG · PCG) are **explicitly withheld.**

## ✅ EXIT CHECK

- [x] **Four lenses run as a parallel Agent fan-out in ONE message** — not in-context (2nd consecutive run)
- [x] **Every under-computed leg either PROMOTED or logged as within-run watch** — 1 promoted
      (IT-optical → **N = 4 → 5**), 2 logged. **None silently dropped**
- [x] **Both-sides brackets produced for every binary in the window** (§5). ⚠ **No binary sits ≤48h**,
      so the ≤48h mandate does not trigger on the clock — **it is honoured anyway on the 08-12 CPI**,
      because one print moves four tilts
- [x] **Momentum re-tags with flip conditions** (§3) — **and one of them (NEM) independently confirms
      a bracket-annex from a fourth, unrelated instrument**
- [x] **Cycle-GAP flag with core expressions** (§6), **and the two reconciliation claims were TESTED
      rather than repeated** — both confirmed
- [x] **NOT all four lenses agreed with the draft.** **Three corrected this run's own earlier stages**,
      which is the stage's stated default expectation and it was met
- [x] **New brackets registered with frozen observables and measured bands**: **S71** (D93 executed,
      trailing-252 quantiles, non-zero centre disclosed) · **S72** (sign-pattern, no invented band,
      its own weakness disclosed at registration) · **S57-ANNEX and S61-ANNEX both EXTENDED, neither
      parent re-frozen**
- [x] **New digs: D216** (reachability is two-sided — an inevitable branch is as uninformative as an
      unreachable one) · **D217** (the rank-3 GAP predicate cannot fire regardless of threshold) ·
      **D218** (a bracket that scores a cycle is invisible to the instrument measuring exposure to it)
- [x] **No position sizing and no buy/sell language anywhere (P4)**
