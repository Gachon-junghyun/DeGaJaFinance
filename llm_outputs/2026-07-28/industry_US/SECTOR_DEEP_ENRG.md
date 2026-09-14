# SECTOR_DEEP_ENRG — industry_US — 2026-07-28 (Tue) · **CONTINUOUS TRACK → led with the DELTA**

> Structure carried by reference to `llm_outputs/2026-07-27/industry_US/SECTOR_DEEP_ENRG.md`.
> Flow `asof 2026-07-27 settled`. Benchmark **SPY** inline (C1). Analytical only (P4).
> ⚠ **Written in-run, not by a subagent** — see `BLINDSPOT_PREMORTEM.md` §0 for what that costs.

---

## 1 · THE DELTA — the kill line moved AWAY, and two prior runs read it backwards

Settled series `[own calc, yfinance CL/RB/HO/BZ; settled-only is a rule (R17)]`, **QoQ-style
rate-of-change series, not levels** (lens L1):

| Date | WTI | 3-2-1 crack | **Δ crack** | gasoline crack | distillate crack | diesel−gas gap |
|---|---|---|---|---|---|---|
| 07-22 | 86.83 | 66.865 | — | 56.587 | 87.420 | 30.83 |
| 07-23 | 92.19 | 66.492 | **−0.373** | 54.659 | 90.157 | 35.50 |
| 07-24 | 89.31 | 64.304 | **−2.188** | 53.318 | 86.275 | 32.96 |
| **07-27 (last settled)** | **82.61** | ★ **68.117** | ★ **+3.813** | 57.137 | ★ **90.077** | 32.94 |
| 07-28 ⚠ **UNSETTLED** | 81.36 | 63.823 | −4.294 | 51.788 | 87.892 | **36.10** |

**★★★ The finding: on the settled 07-27 close the composite ROSE 5.9% while crude fell 7.5%.**
- **P4's anti-signal (a settled 3-2-1 crack below 60) is now 8.12 points away, up from 4.30 on 07-24.**
- The **rate** series shows **one** decline then a reversal — **lens L1's two-consecutive-declines
  condition has NOT fired**, and M129 already measured that conditioning on it *subtracts* information
  here (37.0% vs a 43.1% unconditional base rate, n=27 over 130 settled weeks).
- ★★ **S8 branch B in its cleanest form**: crude −7.5%, **distillate crack +4.4% to 90.077**.

### ⚠ The correction this delta forces, and it is against two of the desk's own runs

| Run | What it read for 07-27 | Volume state of the bar it used |
|---|---|---|
| 07-27 `industry_US` | crack **61.665**, distillate 85.614 (labelled ⚠INTRADAY, correctly) | CL 174,048 of 401,934 = **43%** |
| 07-28 `industry_kr` | WTI **81.560**, distillate crack **85.075**, buffer *"only ~1.075"* | an **electronic tick**, re-pulled twice and drifting |
| **This run (settled)** | **WTI 82.61 · crack 68.117 · distillate 90.077** | the settled 07-27 bar |

**Reconstruction**: their inputs imply **HO ≈ 3.9675**, which sits between today's **07-28 low 3.9392**
and **open 3.9750** ⇒ **they were reading a 2026-07-28 electronic tick wearing 07-27's date. D83, the
sixth instance.** ★ **The S8 verdict `FIRED-B` is invariant across all three readings** (distillate ≥84
on every one). **The buffer is not**: 6.08 on the settle, 3.89 on today's unsettled bar, and **1.075
reproduces from neither.**

★ **New defect that breaks D83's own detector — D86**: on 2026-07-27 **all four contracts carry a
Volume byte-identical to their own 07-24 value** (CL 365,438 · HO 23,447 · RB 27,562 · BZ 33,923),
while every OHLC differs and is internally consistent. **A forward-filled volume field means "check the
volume to see whether the bar settled" cannot be applied to that date.**

---

## 2 · The divergence ROTATION §3 handed here — RESOLVED, and it resolves against the tag

**The question**: Energy is **#1 on wflow (+0.435) with the board's best breadth (0.19)**, yet its three
🟢 are **SLB, XOM and CVX** while the three refiners are 🟡.

**Verdict: the refiner absence is a FILTER ARTIFACT and the integrated greens are VELOCITY paths.**

| Name | tag | flow | RS20 / RS60 vs SPY | `vol_surge` | `velocity` | OBV |
|---|---|---|---|---|---|---|
| **MPC** | 🟡 | +0.656 | **+21.6 / +25.3** | 0.98 | None | 매집 |
| **PSX** | 🟡 | +0.644 | **+19.7 / +15.9** | 0.96 | None | 매집 |
| **VLO** | 🟡 | +0.534 | **+16.2 / +17.5** | 0.84 | None | 매집 |
| **XOM** | 🟢 | +0.675 | +12.0 / **−3.8** | **0.82** | **3.02** | 매집 |
| **CVX** | 🟢 | +0.568 | +9.7 / **−5.0** | **0.78** | **2.14** | 매집 |
| **SLB** | 🟢 | +0.789 | +8.3 / **−11.4** | **1.22** | None | 매집 |

⇒ **All three refiners pass OBV 매집 ∧ RS20>0 and are blocked by `vol_surge` alone** — the exact
mechanism replicating for a sixth time. **XOM and CVX are green with `vol_surge` BELOW the refiners'**,
cleared on news velocity. **Only SLB's green is a volume path.**
★ **Consequence, stated plainly: the sector's 🟢 tag currently points at the two names with NEGATIVE
RS60 and away from the three with the strongest two-window agreement on the board.**

---

## 3 · Sub-sector dispersion — the sector label is the wrong unit, measured

**Days 21–60 excess vs SPY (= RS60 − RS20)**, settled 07-27:

| Node | Names | days 21–60 |
|---|---|---|
| **Integrated / E&P / services** | XOM **−15.8** · CVX −14.7 · COP **−21.4** · OXY −22.0 · SLB **−19.6** · BKR **−21.6** · FANG −15.9 · EOG −7.4 · DVN −20.3 | **every one negative** |
| **Refining** | **MPC +3.8** · **VLO +1.3** · **PSX −3.8** | near zero |
| **Midstream** | WMB +3.2 · KMI +1.6 · OKE −2.6 · TRGP +6.3 | mixed, all 🟡/🔴 |

**RS20 spread inside "Energy": +21.6 (MPC) to −10.5 (WMB) = 32.1pp, against the sector ETF's own
5-day move of +0.72%.** ⇒ **The dispersion exceeds the sector's move by ~45×; the sector label is the
wrong unit of analysis and this file says so.**

★★ **M177 replicates on the integrated leg and DEGRADES on the refining leg.** M177 (07-27) measured
refiners at **+4.1 / +7.8 / +1.6**; today they are **+1.3 / +3.8 / −3.8** — **PSX has flipped
negative.** The clean split is narrowing: the refiners' base is thinning, even though their RS20
remains the sector's best.

---

## 4 · Lens L2 — margin percentile beside every multiple, and one is a structural blank

| Name | Forward P/E | Mean target vs price | **FY2025 gross margin, own history** | Percentile |
|---|---|---|---|---|
| **MPC** | **11.23×** | ⚠ **−2.6% (price is ABOVE the mean target)** | **10.0%**, series FY2018–2025, max 14.5% (2022), min 5.8% (2020), median 10.5% | ★ **~37.5th — BELOW its own median** |
| **PSX** | — | — | **12.3%**, 10-year series, max 25.9% (2016), min 8.4% (2021), median 12.1% | ★ **~60th** |
| **VLO** | **12.15×** | ⚠ **−5.1% (price is ABOVE the mean target)** | **`[blank]` — `margin_history.py` returns *"연간 데이터 없음"* for a FOURTH consecutive run (D56)** | ⛔ **unobtainable.** ⚠ **L2 forbids calling VLO cheap without one, and this file does not** |

⇒ **M176 replicates independently on both measurable names: the refiners are NOT at peak margin.**
The low forward multiples come from the **FY26→FY27 consensus cliff (M23)**, not from a peaking
denominator — **which is the inverse of the trap L2 usually catches.**

**Estimate momentum, read WITH the multiple (the stage's binding rule):**

| Name | +1y EPS, 90d change | +1y breadth (30d) | ⚠ the 7-day column |
|---|---|---|---|
| **MPC** | **+44.1%** (20.26 → 29.19) | 6↑ : 3↓ | ★★ **+1y 7-day breadth is 1↑ : 2↓ — the FAR book has turned DOWN at MPC while the near book runs +119.7%/90d on next-quarter.** First occurrence |
| **VLO** | **+34.8%** (18.46 → 24.88) | 10↑ : 3↓ | ⚠ **current-quarter 30d breadth 7↑ : 5↓ — the most contested near book of any name measured this run.** The 07-30 print lands on it |

★ **Both refiners now trade ABOVE their mean analyst targets** (−2.6% / −5.1%). **A rising estimate
series that price has already outrun is consensus chasing on both legs**, and it is stated rather
than read as cheapness.

---

## 5 · The customers (W4) — and the answer went the wrong way this morning

D23 has been open for two runs. **It closes at 4 of 5, with the fifth REFUTING the other four.**

| Customer | Print | Fuel disclosure |
|---|---|---|
| DAL · UAL · FDX · LUV | 06-24 → 07-23 | **fuel costs +66% to +84% YoY at all four; UAL and LUV cut or missed Q3 guidance explicitly citing fuel/crack** (M34) |
| ★ **SkyWest** *(new this run)* | thread `[REIGNITED] 3→4→2→2` | *"SkyWest Q2 Profit Falls On Higher Fuel Costs"* — a **sixth** customer, same direction |
| ★★ **UPS** | **2026-07-28, this morning** | ⚠⚠ **RAISED FY guidance** (revenue $91.2bn, adj EPS ~$7.22) on adj EPS $1.76 vs $1.66; **fuel appears in NONE of five outlet write-ups.** **S20 scored `FIRED-B`** |

⇒ **W4 is NOT closed. It is a dispersion finding (W5)**: five air/regional carriers pay the crack
visibly and the largest US ground-freight buyer does not. **The honest reading is that the distillate
bottleneck transmits to jet fuel far more than to ground diesel**, which narrows the "real dollars are
moving through the crack" argument to the aviation channel rather than removing it.
⚠ **The UPS call transcript is not in the corpus at run clock** — the fuel leg is `[partially
verified]` (D85), and this file does not conclude past that.

---

## 6 · Anti-signals and track KPIs — stated as observables

| # | Anti-signal (kills the leg) | Distance today |
|---|---|---|
| 1 | **Settled 3-2-1 crack below 60** | **8.12 points** (was 4.30 on 07-24) |
| 2 | **Distillate crack below 80** | **10.08 points** (90.077) |
| 3 | **XOM RS20 vs SPY reverting to ≤ 0 by 08-05** (S31 branch B) | **+12.0**, and ⚠ **RS60 fell +0.4 → −3.8**, so the 13.1pp gap **WIDENED to 15.8pp** — it closed by RS60 falling, not RS20 |
| 4 | **HY OAS ≥3.10% on a close** ⇒ S26 owns it, not this | **31bp** (2.79%) |

**Physical counter-evidence still accumulating on the other side (C2 — both halves):**
- ★ **Russia's diesel export ban EXPIRES 2026-07-31** (M93) — the single dated item against the leg.
- **Singapore and Fujairah stock builds** = **two of M128's five named hubs inverted.**
- **India on track for 1.55M bpd of July light/middle-distillate exports vs 866k in May** (M93).
- ⚠ **Against those**: the physical thread is **BUILDING** — *Tankers Divert to Egypt*, **Saudi Red Sea
  crude exports −41% since March**, Red Sea traffic at a multi-month low, **Japan backing overseas
  pipelines to reduce Hormuz dependence**.

**Track KPIs**: settled 3-2-1 crack · the diesel−gasoline gap (**36.10 on today's unsettled bar — the
widest in the visible series**) · WTI COT percentile (**11th**, next print 07-31) · XOM RS20 vs SPY
with RS60 quoted alongside.

**Dated catalysts**: **VLO 07-30 (±5.7% implied, expiry 07-31 D3 — event-covering)** · **STNG 07-30
(S21)** · **Russian ban expiry 07-31** · **XOM 07-31 (±4.0%, skew +14.3 = the highest downside-fear
skew measured)** · **MPC 08-04** · **PSX 08-05**.

---

## 7 · The cross-market vote against this leg, recorded rather than argued away

**HANDOVER §2 scored S33** on the first KR session that opened with the crack's recovery public.
**Raw: FIRED-A (+6.95pp median excess). Beta-adjusted: branch B (−3.57pp).** On a −11.19% benchmark
day pure beta predicts **+10.51pp**; the realised **+6.95pp is 3.57pp below frozen mechanics.**

⇒ **One vote for the war-premium side of C4, from the market that trades the same margin, on the
adjusted axis.** ⚠ **It does not close C4** — the test was swamped by a −10.8% index event whose named
driver (CXMT) is an unrelated axis; **n=1 on a contaminated date (S1)**. **C4 remains
`indistinguishable`.**

★ **And it is why ROTATION declined the flow-carried promote to OW** despite Energy holding **#1 wflow
and #1 breadth on the board** — logged there, not re-argued here.

---

## 8 · Chain-hop — attempted and unusable, stated per the stage rule

`chain-hop "Hormuz transit fee"` scanned **1 article** (D58); single-token `chain-hop "tanker"` returned
**GOOG/GOOGL/NDAQ/TSLA** as its top "headline-named" names — **embedded market-data widgets, not
content (D10, now measured on the US side)**. ⇒ **The chain map in §3 was built BY HAND from
`SECTOR_FLOW_US.json`, and this file claims NO coverage of un-named beneficiaries one hop down.**

⚠ **Instrument gap carried unchanged**: the tanker names **STNG · FRO · INSW · DHT · TNK** — the
literal beneficiaries of the building physical thread — are **four-of-five outside `us_top300`**, so
this desk cannot tag them. **STNG only**: 🟡, RS20 +6.6 / RS60 −7.1, news velocity **0.00×**, short
**4.8% of float covering**, implied **±8.7% (expiry 08-21, D24)**.
