# DEEP ① · ENRG — 2026-07-25 (Sat) ★US-only · **CONTINUOUS TRACK (6 of last 7 runs) · NARROWED TO ONE QUESTION**

> Stage 7 / L1·DEEP. `--market us`, news `--scope foreign`. **Zero buy/sell, zero sizing.** Analytical only.
> **Benchmark for every relative figure in this file: SPY.** Named inline anyway (C1).
> **Run clock — Saturday, US market CLOSED. Every price in this file is the 2026-07-24 settled close.**
> No incomplete bar appears anywhere in this file (R17 / D48 binding).
> **Carried by reference, NOT re-printed:** `llm_outputs/2026-07-24/industry_US/SECTOR_DEEP_ENRG.md`
> — the value-chain map, the tanker leg, the chain-hop ledger, the FINRA baseline-artifact finding
> (§2b / M95), the measured lead-lag matrix (§8 / M96), the annual and quarterly margin tables (§4),
> and the CHART_READ blocks. **This file writes only the mandate and only what moved.**

---

## §0 · THE VERDICT ON THE MANDATE, FIRST

**The operative frame is the INVENTORY frame (the "FOR" side) — and it is operative not because Morgan
Stanley says so, but because the issuer says so in an SEC filing.**

**The number that decides it.** MPC's own 10-K MD&A, Item 7, on the record: *"Our Refining & Marketing
segment results for 2025 versus 2024 reflect higher realized refining margins supported by stable demand
and by gasoline and distillate inventory levels in the U.S. that were at or below five-year averages."*
And MPC's **first-listed** Item 1A margin risk bullet is *"global and regional inventory levels and
availability of and demand for feedstocks and refined products."* `[measured, primary — SEC 10-K via
module_business_us MPC, extracted this run; VLO's Item 1A still returns empty]`. **The AGAINST case
measures a price. The FOR case measures the variable the issuer itself names as the cause of that price.
On the issuer's own stated causal axis, the two are not symmetric evidence.**

**Three measurements settle the rest of it, all on settled closes I computed myself:**

1. ★★ **The first negative week of the advance is a GASOLINE event, not a diesel event.** Weekly settled
   means, week ending 2026-07-24 vs 07-17: composite **67.647 → 67.043 = −0.89% WoW** (confirmed to the
   mandate's figure), but underneath it the **distillate crack ROSE again, 87.301 → 88.405 (+1.27%)**
   while the **gasoline crack FELL, 57.820 → 56.362 (−2.52%)**, and the **weekly-mean diesel-minus-gasoline
   gap WIDENED, 29.481 → 32.043**. The bottleneck both banks describe is the distillate leg, and on the
   only resolution at which a week is a week, that leg did not roll.
2. ★★ **The AGAINST case's headline premise is false as stated, and I correct it rather than carry it.**
   *"the first narrowing of the entire run-up"* — on **settled daily closes the diesel-gas gap narrowed on
   10 of the 24 sessions since 2026-06-19**, including **−5.86 on 07-15** (2.3× larger than 07-24's −2.54)
   and **−3.11 on 07-17**, both inside the run-up. What is true about 07-24 is only that it narrowed;
   **"first" is wrong on the settled series.** Filed as **R19** (§7) — ⚠ renumbered from R18 at run end: R18 was already taken by the 2026-07-25 industry_kr run (its own M-04 self-backtest). ⚠ **S1**: 07-24 is n = 1 either way.
3. ★★ **The L1 rule that would have carried the AGAINST case has not fired — and, backtested, does not
   work on this series.** L1 asks for **two consecutive declines in the rate**; the acceleration series
   is **+5.733 → −10.104**, i.e. **one**. And over 130 settled weeks (2024-01 → 2026-07-24),
   **P(4-week-forward crack decline | two consecutive negative accelerations) = 37.0% (n = 27) against an
   unconditional base rate of 43.1%.** The conditioning subtracts information. **`indistinguishable`
   (C4) — not "rejected"**; the rule is binding on this desk and it should be re-specified, not ignored.
   ★ Its most recent completed firing was **2026-07-10**, and the four weeks that followed ran **+9.21%**.

**The ONE observable that separates the two frames, with a date: the EIA Weekly Petroleum Status Report's
distillate fuel oil stocks against the five-year average — next print Wednesday 2026-07-29, one day before
VLO.** That is the exact series MPC's MD&A names and the exact series Morgan Stanley/Argus model. If US
distillate stocks re-enter the five-year band while the weekly distillate crack falls, the FOR frame is
done; if they stay below it, a −0.89% composite week driven by gasoline is noise inside the thesis.

**⚠ The FOR case already has one dated primary contradiction and it must be carried.** Fujairah Oil
Industry Zone data for the week ended 2026-07-20, published 07-22 — **two days newer than the oilprice
piece the mandate quotes** — shows **middle distillates (jet/diesel) ROSE 35% to a three-month high of
1.506M bbl**, while **light distillates fell 37% to a record low of 1.121M bbl** `[news, body-read,
Platts/FOIZ via hellenicshipping]`. **One of the FOR case's five named hubs has inverted, and it inverted
in the same direction as the gasoline-versus-diesel split above, with the signs swapped.** Fujairah is a
bunkering hub, not a US or European balance point — scope stated, not hidden.

---

## §1 · The delta since 2026-07-24

| # | What is new | Settled evidence | Grade |
|---|---|---|---|
| 1 | **The week completed and turned negative** — M94's `+0.12% WoW` is superseded by a full settled week | **67.647 → 67.043 = −0.89%**, acceleration **−10.10pp** from +9.21. Level still **88.9th pctile of 90d / 96.0th of 250d** | `[measured]` |
| 2 | ★★ **SLB +11.01% on 07-24 = +8.15σ on its own σ20 — the largest single-name move in the sector, and it is an EARNINGS PRINT** | **8-K Item 2.02 filed 2026-07-24** (`module_disclosure_us SLB`) + Q2 2026 call transcript, 07-24 09:30 ET. Next print **2026-10-23**. ⇒ the Equipment & Services **delta +0.212** and **SLB delta +0.414** that the flow file flags are **the event's own footprint** | `[measured, primary]` |
| 3 | **R8 holds a FOURTH consecutive run — and then inverts on the other year** | Forward P/E **MPC 10.59 < PSX 10.96 < VLO 12.16**. On **CY26** consensus: **MPC 7.69 < VLO 8.58 < PSX 9.88** — PSX becomes the *most* expensive | `[measured]` |
| 4 | **All three price-to-target gaps compressed; targets were raised while prices fell** | Above mean target: **VLO +4.5%** (was +6.4%) · **MPC +1.7%** (was +5.0%) · **PSX +1.3%** (was +2.2%). XOM **−5.9% below** target (upside) | `[measured]` |
| 5 | ★ **MPC's Item 1A and MD&A extracted for the first time** — a second issuer's primary text, and it names the disputed variable | §0. **VLO's `risk_factors` is still an empty string** — the 07-24 tool gap has not closed | `[measured, primary]` |
| 6 | **No detachment on 07-24 — the equities moved WITH the crack** | crack log-return **−3.35%**; SPY-residuals **VLO −1.06% · MPC −1.11% · PSX −0.21% · XOM −0.05%**. **Sign-disagreement streak = 0.** Rolling-60 same-day correlation still **rising** (VLO 0.412 vs 0.267 twenty sessions ago) | `[measured]` |
| 7 | **Zero dated company events between now and the prints** | `module_disclosure_us --days 30`: VLO 1 × 8-K (Item 7.01, 07-16) · MPC 1 × 8-K (07-29 item-unclassified) · PSX **zero 8-Ks**, Form 4s only | `[measured, primary]` |

**⚠ C4 counter NOT incremented** (M96 froze it as under-powered). Item 6 is recorded as an observation only.
**⚠ Data-integrity note, reproducing from 07-24**: yfinance reports **identical volume for 07-23 and 07-24**
on all three legs (CL 401,934 / RB 25,390 / HO 22,882) while the closes differ. **The volume column is not
trustworthy; the close column is.** No conclusion in this file uses futures volume.

---

## §2 · Lens L1 — the RATE table, on settled closes only

Weekly means of the settled 3-2-1 crack, `(2·RB·42 + HO·42 − 3·CL)/3`, own calc, every point a complete
settled week (W-FRI):

| Week ending | Crack | WoW % | **Accel (ΔWoW)** | Gasoline | Distillate | **Gap (D−G)** | n |
|---|---|---|---|---|---|---|---|
| 2026-05-22 | 53.869 | −4.88% | −6.40 | 47.806 | 65.997 | 18.192 | 5 |
| 2026-05-29 | 49.594 | −7.94% | −3.06 | 43.287 | 62.208 | 18.921 | 4 |
| 2026-06-05 | 45.040 | −9.18% | −1.25 | 36.632 | 61.854 | 25.222 | 5 |
| 2026-06-12 | 47.033 | +4.43% | +13.61 | 40.540 | 60.019 | 19.480 | 5 |
| 2026-06-19 | 49.233 | +4.68% | +0.25 | 45.641 | 56.418 | 10.777 | 4 |
| 2026-06-26 | 55.649 | +13.03% | +8.35 | 52.518 | 61.911 | 9.392 | 5 |
| 2026-07-03 | 59.858 | +7.56% | −5.47 | 55.972 | 67.630 | 11.658 | 4 |
| 2026-07-10 | 61.941 | +3.48% | −4.08 | 55.505 | 74.813 | 19.308 | 5 |
| 2026-07-17 | 67.647 | +9.21% | +5.73 | 57.820 | 87.301 | 29.481 | 5 |
| **2026-07-24** | **67.043** | **−0.89%** | **★ −10.10** | **56.362** | **88.405** | **★ 32.043** | **5** |

**Read.** Ten weekly points, all settled. The composite's rate has turned negative for the first time in
the advance — **and the two legs inside it are moving in opposite directions for the third consecutive
week.** Distillate WoW: **+9.24 → +10.62 → +16.69 → +1.27**. Gasoline WoW: **+6.58 → −0.84 → +4.17 →
−2.52**. **The distillate leg is decelerating hard (accel −15.43pp) but has not turned; the gasoline leg
has turned twice in four weeks.** L1's own signal — two consecutive rate declines — **is one week away
from firing** and would fire on the week ending 2026-07-31.

⚠ **And L1's signal, measured, is not worth what the rule assumes** (§0 point 3): 37.0% hit rate against
a 43.1% base rate, n = 27, 130 weeks. **I am reporting the rule's fire condition and its measured
uselessness in the same breath rather than quietly using it.** Recommended to the registry: re-specify
L1 with a **magnitude** condition (cumulative pp of rate decline), not a two-observation count.

**Crude, for completeness** `[measured, settled]`: Brent **100.69 → 96.78 = −3.88%**, WTI **92.19 → 89.31
= −3.12%**. **Both legs of the crack's inputs fell; the composite fell less than either product leg's
own fall would imply, which is what a widening gap looks like.**

---

## §3 · Primary-source check

| Source | What it says | Grade |
|---|---|---|
| **MPC 10-K, Item 7 MD&A** | Realized margin expansion attributed to *"stable demand and… gasoline and distillate inventory levels in the U.S. that were at or below five-year averages"* | `[measured, primary]` |
| **MPC 10-K, Item 1A** (first four margin bullets) | 1 *"inventory levels and availability of and demand for feedstocks and refined products"* · 2 *"transportation infrastructure cost and availability"* · 3 *"utilization levels and capacities of other refineries in our markets and globally"* · 4 *"development by competitors of new refining or renewable conversion capacity"* | `[measured, primary]` |
| **MPC 10-K, Item 1** | **~3.0M bpd** capacity, three segments (R&M, Midstream, Renewable Diesel) — the structural reason its crack beta is diluted (M98, carried) | `[measured, primary]` |
| **MPC 10-K forward statement** | *"the U.S. refining industry's current structural advantages… will support a constructive environment for U.S. refiners"* — ⚠ **S6: this is a company FORWARD-LOOKING LABEL, not a measurement**, and is tagged as one | `[measured, primary — label]` |
| **EIA, week ended 2026-07-17** (via body) | US refinery utilization **96.2%**, against **94.7%** the same week of 2025; **PADD2 and PADD4 at 100%**; commercial crude stocks **6% below** the five-year average. ⚠ **C2 — the WoW/sequential figure is `[blank]`**; the body carries only the year-ago comparison | `[news]` |
| **FOIZ / Platts, week ended 2026-07-20** | Fujairah **middle distillates +35% to a three-month high (1.506M bbl)**; light distillates **−37% to a record low (1.121M bbl)**; total stocks **−16%**, first drop in five weeks | `[news, body-read]` |
| **oilprice, 2026-07-19/20 — the adaptation counter-piece, from the SAME outlet as the FOR case and one day earlier** | European refiners pushed **jet yields to record levels**; **US jet fuel output above 2M bpd on a 4-week average for the first time**; US product exports at record highs; **IEA released 400M bbl in March, its largest ever**; Saudi Yanbu flows to Europe **above pre-closure levels by early June**; European jet stocks **~38M bbl = under one month of cover** | `[news, body-read]` |
| **India export tax** | *"India Hikes Diesel and Jet Fuel Export Tax"* — **headline present in three oilprice sidebars, body absent from the corpus.** ★ If real, it **throttles** the A4 anti-signal (India's 866k → 1.55M bpd export ramp), i.e. it cuts **for** the margin, not against it | `[news, headline-only — NOT promoted]` |
| **VLO / MPC / PSX EDGAR, 30 days** | **No M&A, no capacity, no guidance-revision 8-K at any of the three.** Nothing is dated on their own filing records before their prints | `[measured, primary]` |
| **Russia's diesel export ban** | Imposed 07-08, **expires 2026-07-31** (M93, carried). **No lift, extension or modification appears in any body in the 8-day window** | `[measured absence]` |

**The synthesis, stated once.** The record-jet-yield piece and the record-diesel-margin piece are **the same
fact from two ends**: refiners maximise middle-distillate yield **because** the distillate crack pays — which
is simultaneously why utilization is 96.2% and why the supply response already shows in export volumes.
**The margin is real (M92) and the mechanism that ends it is running (M93). What is new this run is that
the mechanism has a policy brake (India's export tax, `[news]`-grade) and a dated release valve (the Russian
ban expiry, 07-31) pointing opposite ways in the same week.**

---

## §4 · Customers (W4) — UPS 2026-07-28 is the fifth and last

**D23 is 4/5 closed and carried by reference** (DAL 07-10, UAL 07-16, FDX 06-24, LUV 07-23; fuel **+66% to
+84% YoY**, and on the **sequential** axis two of the four — UAL and LUV — cut or missed near-term guidance
citing fuel, while FDX absorbed it sequentially with no demand impact cited). **No customer figure is
re-derived here.**

**UPS prints 2026-07-28** `[measured — yfinance calendar, consensus **EPS $1.664 on revenue $21.84B**]`.
It is the largest US distillate buyer in the set and the only one whose fuel line is **contractually
recovered** through a published surcharge table rather than through fares.

**What specifically to read from it, pre-registered:**
1. **Fuel expense quantified YoY *and* sequentially.** A YoY-only disclosure is half a print (C2).
2. ★ **The surcharge recovery ratio.** If UPS recovers ~100% of the increase, the refiners' margin is a
   **pass-through to the freight buyer**, not a transfer from the carrier — which changes who ultimately
   funds the distillate crack and therefore where it breaks.
3. **Fuel-attributed or volume-attributed guidance change.** UPS is Industrials' lowest-flow, only
   negative-delta, only-cheap name (M111: 14.25× forward, +0.6% to target). Fuel-attributed makes the
   channel 3-of-5; volume-attributed says the freight cycle, not the crack, binds at the customer end.
4. ★ **The falsifier** (A8): fuel a **non-event** at the largest US distillate buyer would contradict §0's
   inventory frame at the point of consumption.

---

## §5 · Dispersion (W5) — is "Energy" the right unit?

Own calc, equal-weight nodes, settled to 2026-07-24, **excess return vs SPY** named inline (C1):

| Horizon | Refining (VLO/MPC/PSX) | Integrated (XOM/CVX) | E&P (5) | Services (SLB/BKR) | Midstream (4) | **Max−min node spread** | XLE own move | **Ratio** |
|---|---|---|---|---|---|---|---|---|
| 1d | −0.76 | +0.01 | −0.26 | **+6.44** | −0.84 | **7.28pp** | +0.40% | **18.01×** |
| 5d | −0.56 | +5.81 | +4.86 | +7.53 | +1.00 | 8.08pp | +3.36% | 2.40× |
| 20d | **+19.68** | +12.96 | +10.00 | +4.91 | −0.15 | 19.83pp | +10.22% | 1.94× |
| **60d** | **+24.60** | **+0.56** | **−4.33** | **−14.31** | **+2.21** | **★ 38.91pp** | **+4.05%** | **★ 9.60×** |

★ **W5 fires harder than on any prior run, and the ratio is now 9.60× on 60 sessions (was 5.93× on 07-23).**
XLE moved **+4.05%** over 60 sessions while its own sub-nodes diverged by **38.91pp**. **A label that moves
4% while its constituents diverge by 39pp is averaging five different bets, not describing one.**
⇒ **"Energy" must not be used as the unit of analysis.** The 60-day spread widened this run **because of
the services leg** (−14.31pp), not because refining extended.

⚠ **The countervailing measurement, carried and not softened.** PREMORTEM measured the SPY-residual
correlations **MPC–VLO +0.878 · VLO–PSX +0.848 · MPC–PSX +0.846 · XOM–XLE +0.911**. **On price the three
refiners are one risk unit with three tickers; on fundamentals they are three businesses** (M98 crack-betas
0.836 / 0.307 / 0.238). **Both are true. The reconciliation is unchanged: they move together on the crack
headline and separate on 07-30 / 08-04 / 08-05.** ★ The **RS20/RS60 split** is the same complaint in flow's
own units: **15 of 16 Energy names are positive on RS20 vs SPY, but 9 of 16 are negative on RS60** — the
sector's 20-day strength is broad and its 60-day strength is three names.

⚠ **D6 note on the flow tags.** All three refiners carry `obv=매집` (C-grade) — admissible here only because
the A-grade axis agrees: **RS60 vs SPY MPC +29.1 · VLO +22.1 · PSX +21.4**. All three are **🟡 rather than
🟢 solely because `vol_surge` is 0.85–0.96** — the M75 volume-gate mechanism, now replicated a **sixth** time.
**That is a filter artifact, not evidence about the refining leg.**

---

## §6 · Adjudicating Lens 3's **EXHAUSTED** tag on VLO

**Verdict: the tag survives on ONE of its three legs. On the other two VLO is `indistinguishable` (C4)
from MPC and PSX, and on one of them the tag points at the wrong name.**

| Leg | Lens 3's claim | My own measurement (settled 07-24, vs SPY) | Adjudication |
|---|---|---|---|
| **Concentration** | *80.2% of VLO's 60-day excess was earned in the last 20 sessions* | **Confirmed exactly: VLO 80.2%** (60d +22.40pp, 20d +17.97pp, days 21–60 **+4.43pp**). **But PSX is 89.7%** (60d +22.03, 20d +19.75, days 21–60 **+2.28pp**) and MPC is 72.6% | ★ **REFUTED as a discriminator.** On its own axis VLO is the **least** concentrated of the two it is being separated from. The axis describes the **node**, not the name |
| **Revisions** | *current-quarter breadth is a coin-flip, 7↑:5↓ (30d), 6↑:5↓ (7d) — the only refiner being cut* | **Confirmed: VLO 6↑/5↓ (7d), 7↑/5↓ (30d)**, current-Q consensus **$10.13 unchanged for a third consecutive run**. **MPC 2↑/0↓ (7d), 5↑/2↓ (30d); PSX 2↑/0↓ (7d), 6↑/2↓ (30d)** | ★★ **UPHELD, and it is the only leg that separates VLO.** Consensus has stopped marking the quarter VLO reports in five days while still marking up the quarter after it (next-Q $11.57 → $13.31 in 7 days) |
| **Valuation** | *4.3% above mean target on 12.2× forward* | **Confirmed: $302.50 vs mean target $289.47 = +4.5% above; forward P/E 12.16.** But **the "forward" year is FY27** — the far side of consensus's own cliff. **On CY26 the ranking inverts: MPC 7.69× < VLO 8.58× < PSX 9.88×** | ⚠ **YEAR-DEPENDENT — and the desk has been quoting one year.** R8's ordering (MPC<PSX<VLO) holds on FY27 and reverses on CY26 |

**The forward cliff is not a VLO idiosyncrasy and must stop being carried as one.** CY26 → FY27 consensus:
**VLO 35.24 → 24.88 = −29.4% · MPC 40.22 → 29.19 = −27.4% · PSX 20.92 → 18.86 = −9.8% · XOM 11.24 → 10.73
= −4.5%.** ⇒ **Consensus already models a ~28% earnings decline at the two pure refiners.** The L2
"peak-margin trap" as usually stated — *a low multiple with steeply rising estimates is consensus chasing* —
**does not describe what is in front of us**: the multiple everyone quotes is computed on the **post-decline**
year, and FY27 itself is being marked **up** (VLO next-year 8↑/3↓ over 7 days, +34.8%/90d). **The honest
statement is that consensus is chasing the near quarters and has already de-rated the far one; the trap
would be assuming the de-rate is conservative.**

**★ One thing Lens 3 did not measure and it matters: the analyst book.** VLO's recommendation split is
**3 Strong Buy / 7 Buy / 7 Hold / 2 Sell / 1 Strong Sell = 10 buy-side against 10 not**, the weakest of the
three (PSX 12 against 8; MPC 9 against 9). **That is consistent with the revision leg and independent of it.**

**Net: EXHAUSTED is the wrong word for what was measured, and `RE-RATED WITH A SPLIT BOOK` is the right one.**
The concentration number is a property of the refining node (all three ≥72.6%); what is specific to VLO is
that **it is the only one where the sell side is divided on the quarter it reports in five days.**
`indistinguishable` on price behaviour; **separated on the estimate book.** **Resolves 2026-07-30.**

---

## §7 · KPIs and anti-signals, as dated observables

**KPIs — settled closes only (R17 / D48 binding).**

| # | KPI | Reading, 2026-07-24 settled | Next |
|---|---|---|---|
| 1 | **3-2-1 crack, level** | **64.304** · **88.9th pctile of 90d** (41.14–69.45) · **96.0th of 250d** | Mon 2026-07-27 settle |
| 2 | ★ **Crack WEEKLY RATE** (the L1 metric) | **−0.89% WoW** (67.043 vs 67.647), accel **−10.10** — one negative acceleration, **L1 needs two** | week ending 2026-07-31 |
| 3 | ★ **The two legs, read separately** | gasoline **56.362 (−2.52% WoW)** · distillate **88.405 (+1.27% WoW)** · **weekly gap 32.043, still widening** | weekly |
| 4 | ★★ **EIA distillate stocks vs the 5-year band** — **the mandate's separator** | not measurable in this repo; last body-read datum is crude stocks **6% below** the 5-yr average, week to 07-17 | **2026-07-29** — ⚠ no EIA module; body-read only |
| 5 | **VLO current-Q consensus + breadth** | **$10.13, unchanged for a 3rd run; 6↑/5↓ (7d), 7↑/5↓ (30d)** — still the only refiner being cut | resolves **2026-07-30** |
| 6 | **R8 ordering** | FY27: **MPC 10.59 < PSX 10.96 < VLO 12.16** (4th consecutive hold) · **CY26 inverts: MPC 7.69 < VLO 8.58 < PSX 9.88** | daily |
| 7 | **XOM as the control** | crack correlation **+0.076** (n=536) and rolling-60 **+0.011**; RS60 vs SPY **+0.4**; revisions 0↑/2↓ (7d) | XOM prints **2026-07-31** |
| 8 | **FINRA short-vol z** — **demoted** (M95), context never a trigger | carried unchanged from 07-24 | daily |

**Anti-signals — dated, each able to fire against this file.**

| # | Anti-signal | Threshold | State | Distance |
|---|---|---|---|---|
| **A1 ★ RESTATED** | **The one-axis kill.** The old conjunction (crack < 60 **AND** WTI > $90) became unreachable when WTI settled at **89.31** — the crude leg is dropped by declaration, not by drift | **Settled 3-2-1 crack < 60.00**, one axis | **64.304** | **$4.30 — armed, and closer than at any point in the run-up** |
| **A2** | Two consecutive **weekly means** below 60.00 | — | 67.647, 67.043 | not near |
| **A3 ★ RESTATED** | **The distillate bottleneck releases.** Restated to the weekly mean because the daily gap narrowed on 10 of 24 sessions inside the advance (§0, R19) and a daily reading cannot carry it | **Weekly-mean gap below 25**, or **two consecutive weekly declines** in it | weekly gap **32.043 and still widening**; **zero** consecutive weekly declines | far |
| **A4** | Competitor supply response (PSX Item 1A + MPC Item 1A bullets 3–4) | A second month of Indian/Asian export ramp **with** a falling weekly distillate crack | India ramp real (866k → 1.55M bpd) but **distillate crack still rising**, and an **India export-tax headline** now cuts the other way `[news, headline-only]` | **has NOT fired** |
| **A5** | **The Russian ban expires 2026-07-31** (M93) — the 2023 ban was partly lifted after two weeks | Ban lapses **and** the weekly distillate crack falls in the following week | no lift, extension or modification in any body, 8-day window | **2026-07-31** |
| **A6** | **This file's own falsifier**: VLO reports gross margin **< 10.0%** | — | — | **2026-07-30** |
| **A7** | The §5 dispersion claim's falsifier: the three print within ~1pp of each other on gross margin | — | — | **2026-08-05** |
| **A8 ★ new** | **UPS discloses fuel as a non-event** (no YoY-plus-sequential fuel quantification, or a volume-attributed rather than fuel-attributed guidance change) | — | — | **2026-07-28** |

**Dated calendar**: **UPS 07-28** ($1.664 / $21.84B) · **EIA WPSR 07-29** · **VLO 07-30** ($10.126 / $38.43B;
implied ±6.6% exp 07-31, = **2.50× its own settled σ20 of 2.64% and 1.12× √5σ** — mildly event-priced) ·
**STNG 07-30** ($5.031; ±10.0% exp 08-21) · **Russian ban expiry 07-31** · **XOM 07-31** ($3.692) ·
**CVX 07-31** ($5.541) · **MPC 08-04** ($13.952 — up from $13.871 yesterday; ±10.1% exp 08-21) ·
**PSX 08-05** ($7.501).

**★ Proposed correction, filed for `handoff/STANDING_VIEW.md` §5:**

| # | Claim | Killed by | Date |
|---|---|---|---|
| **R19** | **"the diesel-minus-gasoline gap NARROWED 35.50 → 32.96 — the first narrowing of the entire run-up"** — this run's SECTOR_ROTATION §3 mandate and EVENT_ALPHA Card 5 | **On settled daily closes the gap narrowed on 10 of the 24 sessions since 2026-06-19**, including **−5.86 on 07-15** (2.3× larger) and **−3.11 on 07-17**. ★ What survives: the 07-24 narrowing is real and is n=1 (S1). What is withdrawn: **"first"**, and any inference that rests on the event being unprecedented | 2026-07-25 |

---

## §8 · What I could not measure this run

- **EIA distillate stocks as a first-party series** — no EIA module in this repo. **KPI #4, the mandate's own
  separator, is body-read only.** This is the single largest instrument gap in the file and it is the one
  the verdict depends on. **Dig: an EIA WPSR fetcher is the highest-value missing tool on this desk.**
- **VLO Item 1A** — `module_business_us VLO --json` still returns `risk_factors: ""` (second run). MPC's
  extracted cleanly and was substituted. ★ **The cause is now diagnosed, not just observed**: on accession
  `0001628280-26-011499` the `edgartools` TenK parser falls back to the legacy path **for `Item 1`**, and
  the fallback blanks the whole extraction — **even though the new parser's own section list contains
  `part_i_item_1a`**. The section exists and is being discarded by a fallback triggered on a *different*
  item. **Dig: read `part_i_item_1a` directly instead of routing through the Item 1 fallback.**
- **The India diesel/jet export-tax body** — headline present in three sidebars, body absent from the corpus.
  Rate, effective date and product scope are all **`[blank]`**. Not promoted above `[news, headline-only]`.
- **ARA and Singapore middle-distillate stocks** — the FOR case names five hubs; only **Fujairah** returned a
  dated primary print in the window. **Three of five are `[blank]`.**
- **Options flow / market-maker hedging** — unchanged (M95 (iii) remains `[inferred]`).
- **Tonne-miles / a tanker freight index** — unchanged; the tanker leg stays `indistinguishable`.

---

## ✅ EXIT CHECK

- [x] **§0 leads with the verdict on the narrowed mandate**, names the operative frame on a **primary
      source (MPC's own 10-K MD&A and Item 1A)**, and gives **the one dated separator: EIA distillate
      stocks vs the 5-year band, 2026-07-29**.
- [x] **Delta-led** — the value-chain map, tanker leg, chain-hop ledger, FINRA baseline finding, lead-lag
      matrix and CHART_READ are **carried by reference** to the 07-24 file and **not reprinted**.
- [x] **§2 is a rate-of-change table on settled closes, 10 weekly points**, with WoW, acceleration, both
      product legs and the gap — **and the L1 rule is backtested (37.0% vs a 43.1% base rate, n=27) rather
      than obeyed on faith**.
- [x] **§3 grades every number** `[measured, primary]` / `[measured]` / `[news]` / `[news, headline-only]` /
      `[measured absence]`. Blanks left blank.
- [x] **§4 names UPS 2026-07-28** with four pre-registered things to read and a falsifier (A8).
- [x] **§5 states the sector label is the wrong unit and puts the ratio on it (9.60× / 18.01×)**, plus the
      RS20/RS60 breadth split, and carries the countervailing +0.846–0.878 correlations undiluted.
- [x] **§6 adjudicates Lens 3**: **1 leg upheld (revisions), 1 refuted as a discriminator (concentration —
      PSX is 89.7% vs VLO's 80.2%), 1 shown year-dependent (valuation)**. Tag re-worded, not deleted.
- [x] **§7 restates the one-axis kill (settled crack < 60, crude removed) — distance $4.30** — and restates
      A3 to a weekly basis because the daily version was falsified.
- [x] **R19 filed** — this run's own upstream premise corrected on settled data.
- [x] **C4 counter NOT incremented** (M96). **C1 benchmark SPY named inline.** **C2 both halves, or the
      missing half declared `[blank]`.** **S1 applied to 07-24.** **D6: OBV quoted only beside RS vs SPY.**
- [x] **Zero buy/sell language, zero sizing, zero position language.** Analytical only.
