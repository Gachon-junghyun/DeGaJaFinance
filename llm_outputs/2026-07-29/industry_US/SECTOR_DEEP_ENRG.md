# SECTOR_DEEP_ENRG — Energy — industry_US — 2026-07-29 (Wed) · CONTINUOUS-TRACK → **DELTA-LED**

> Continuous slot (5th consecutive run). Structure carried by reference to
> `llm_outputs/2026-07-28/industry_US/SECTOR_DEEP_ENRG.md`; this file leads with the delta.
> All prices **settled 2026-07-28**. Benchmark **SPY** inline (C1). Zero buy/sell language (P4).

## 1 · THE DELTA — the kill line moved away a SECOND time, and by more

Settled series `[own calc, yfinance CL/RB/HO/BZ continuous]`:

```
              WTI     Brent   3-2-1 crack  gasoline crack  distillate crack  diesel−gas gap   CL vol
2026-07-23   92.19   100.69      66.492         54.659          90.157           35.50       401,934
2026-07-24   89.31    96.78      64.304         53.318          86.275           32.96       365,438
2026-07-27   82.61    88.36      68.117         57.137          90.077           32.94       352,813 ⚠
2026-07-28   79.26    84.09    ★ 72.219       ★ 60.789        ★ 95.078           34.29       352,813 ⚠
──────────────────────────────────────────────────────────────────────────────────────────────────────
2026-07-29   84.46    89.94      64.116         50.801          90.747           39.95       141,531 ⚠UNSETTLED
```

- ★★★ **On the settled 07-28 close the 3-2-1 crack printed 72.219 and the distillate crack 95.078 —
  both window highs — with WTI at 79.26, a window low.** **MACRO P4's one-axis anti-signal (a settled
  3-2-1 below 60) is now 12.22 points away**, from 8.12 on 07-27 and 4.30 on 07-24. **Crude −14.0%
  from its 07-23 peak while the distillate crack rose +5.5% over the same stretch.**
- ★★ **That is S8 branch B in its cleanest measured form to date** — input-cost relief, not margin loss.
- ⚠⚠ **And the live tape is running the other way.** The **unsettled** 07-29 bar (**141,531 CL contracts
  ≈ 40% of a session**, US market barely open at this run's clock) shows **WTI +6.6% to 84.46 with the
  3-2-1 collapsing to 64.1.** **Inadmissible as a measurement** (R17/D83); quoted only so a later
  reader knows the direction of travel at the run clock. **No verdict is taken from it.**
- ⚠ **D86/M202 reproduces a SECOND time**: **07-27 and 07-28 carry a byte-identical CL volume of
  352,813**, and the 07-28 run recorded **365,438** for 07-27, since revised. ⇒ **the volume field is
  both forward-filled AND revised, so "check the volume to see whether the bar settled" is unusable on
  this stretch.** The settled/unsettled call above rests on the 07-29 bar's **2.4× smaller** volume.

## 2 · The ROTATION divergence, resolved — the absence is instrumental, not informational

**ROTATION's question**: Energy carries the **board's #1 wflow (+0.380)** with **eqflow +0.253** — and
produces **0 🟢 of 16, breadth 0.000**, while **XLE was the 2nd-worst 5-day sector (−1.59%)**.

**Verdict: FILTER ARTIFACT, and it is measurable.** **8 of the 16 names pass `OBV-매집 ∧ RS20>0` and
8 of 8 are blocked by `vol_surge` alone.** The three that matter:
**MPC** (surge 0.96, RS20 +18.1 / RS60 +20.2) · **PSX** (0.95, +18.3 / +11.8) · **XOM** (0.85,
+12.5 / −3.9). The board-wide mechanism replicated a **7th** time this run (SWEEP §4).
⇒ **The money is arriving in Energy without a volume surge.** A 🟢 count is not a flow verdict here.
⚠ **This does not make it accumulation** — OBV is C-grade (D6) and may corroborate, never carry. The
A-grade axis (RS20 vs SPY) agrees, which is why the verdict is "instrumental absence", not "bullish".

## 3 · Lens L2 — and the two halves of L2 DISAGREE on the refiners

**Margin percentile** `[own calc, SEC XBRL, scripts/margin_history.py]`:

| Name | FY25 gross margin | Own series | Percentile | Forward P/E | To mean target |
|---|---|---|---|---|---|
| **MPC** | **10.0%** | FY2018–2025, max 14.5 (FY22) · min 5.8 (FY20) · **median 10.5** | **BELOW its own median, ≈37.5th** | **11.27×** | **−2.9%** |
| **PSX** | **12.3%** | FY2016–2025, max 25.9 (FY16) · min 8.4 (FY21) · **median 12.1** | **just above its own median, ≈55th** | **11.06×** | **−2.1%** |
| **VLO** | ⚠ **`연간 데이터 없음`** | — | ⚠ **STRUCTURAL BLANK, 5th consecutive run (D56)** | 12.24× | −5.8% |
| **XOM** | ⚠ **`연간 데이터 없음`** | — | ⚠ ★ **NEW BLANK — the same failure class as VLO's, on a second Energy name** | 14.85× | **+6.3%** |

★ **New this run: `margin_history.py XOM` returns `연간 데이터 없음`.** ⇒ **L2 is now unrunnable on
TWO of the four Energy names this desk carries.** **No percentile is invented for either, and neither
is called cheap** (the D56 discipline, extended).

**Estimate momentum** `[module_fundamentals_us, §추정치 모멘텀]` — 90-day change in consensus EPS:

| Name | Current qtr | Next qtr | Current yr | **Next yr** | Trailing → Forward EPS |
|---|---|---|---|---|---|
| **MPC** | +60.1% | **+106.7%** | +72.3% | **+35.1%** | **$15.18 → $27.77 (+83%)** |
| **VLO** | +27.2% | **+76.7%** | +52.2% | **+35.8%** | $13.69 → $25.12 (+83%) |
| **PSX** | +36.1% | +60.1% | +49.4% | **+25.1%** | $10.13 → $18.98 (+87%) |
| **XOM** | +9.1% | +9.6% | +9.6% | **+4.1%** | $5.88 → $10.59 |

★★ **The finding: L2's two halves point opposite ways here, and that is the honest state.**
- The **margin percentile** says the refiners are **mid-cycle, not at peak** — MPC is *below* its own
  8-year median. That is the **third independent replication** of M176/M207.
- The **revision book** says the denominator is **racing** — MPC's next-year consensus is up
  **+35.1% in 90 days** and its forward EPS is **83% above trailing**. Under the L2 rule
  (*"a low multiple whose estimates are being revised up that steeply is consensus chasing"*),
  **an 11.3× forward multiple built on a denominator that has already doubled is not cheapness.**
- ⇒ **The correct statement is neither "cheap" nor "peak-margin trap": the margin is mid-cycle and
  the consensus is at the top of its own revision cycle.** Both halves are reported; neither alone is
  the answer (**C2**). ⚠ **And all three refiners trade AT or BELOW their mean targets**, so the
  sell-side has already moved.

## 4 · Dispersion (W5) — the sector label is the wrong unit, measured

Days-21-to-60 excess vs SPY (= RS60 − RS20), settled 07-28:

| Refiners | | Integrated / E&P / services | |
|---|---|---|---|
| VLO | **+3.30** | XOM | **−16.02** |
| MPC | **+2.30** | CVX | −16.79 |
| **PSX** | ⚠ **−5.91** | COP | −21.49 |
| | | SLB | −22.80 |
| | | BKR | **−23.00** |

- **Spread MPC → BKR = 25.3pp on one window, against a sector 5-day move of −1.59%.**
  ⇒ **"Energy" is the wrong unit of analysis and this file says so.**
- ⚠ ★ **M177's clean split is degrading at the `core_pick` end for a second consecutive run: PSX has
  flipped NEGATIVE (−5.91)** while MPC and VLO stay positive. **The registry's human-locked
  `core_pick` is the leg that is deteriorating**, and that is a fact for a human, not a stage.

## 5 · Players, chain and the customers (W4)

**Chain, left → right**: crude supply (OPEC+ / Russia / Hormuz transit) → **crude price (WTI 79.26)**
→ **refining throughput — THE BOTTLENECK** → **product cracks (distillate 95.078, gasoline 60.789)**
→ distribution (KMI 🟡 −0.16, surge 1.33) → **the buyers of distillate (airlines, freight, rail)**.

**The binding constraint is distillate conversion capacity, not crude.** Evidence: the crack rose
**+5.5%** while crude fell **−14.0%** over four settled sessions — a level of *product* scarcity
independent of the input.

**Customers named, and their disclosed spend checked (W4 / dig D23)** — carried, and it does **not**
close cleanly:
- **DAL (07-10) · UAL (07-16) · FDX (06-24) · LUV (07-23)**: fuel costs **+66% to +84% YoY** at all
  four; **UAL and LUV cut or missed Q3 guidance explicitly citing fuel/crack costs** (M34).
- **UPS (07-28, S20 FIRED-B)**: **raised** FY guidance on revenue $91.2bn / adj EPS ~$7.22, and
  **five outlets itemised the drivers with NO fuel line.**
- ⇒ **4 of 5 confirm and the 5th refutes. That is a DISPERSION finding (W5), not a closure** — and
  the honest next question is why the largest US distillate buyer is the one that did not feel it.
  ★ **UAL's own tape agrees with the odd-one-out reading**: UAL is **🔴분산 −0.76 with RS20 −8.4 but
  RS60 +34.4** — it kept its 60-day gain and lost the last 20.

## 6 · Track KPIs and anti-signals — stated as observables

| # | Observable | Now | Kills the thesis at |
|---|---|---|---|
| 1 | **Settled 3-2-1 crack** | **72.219** | **< 60** (12.22 away) |
| 2 | **Settled distillate crack** | **95.078** | **< 80** (15.08 away) |
| 3 | Diesel − gasoline gap | **34.29** | sustained < 30 |
| 4 | **XOM RS20 vs SPY, with RS60 alongside (S31)** | **+12.50 / −3.52** | RS20 ≤ 0 by **2026-08-05** ⇒ war premium |
| 5 | Refiner revision breadth | VLO next-yr **10↑:3↓ (30d)** | a first net-down month |
| 6 | HY OAS | 2.81% | ≥3.10% ⇒ **S26/S41** own it, not this |

**Dated catalysts**: **VLO 07-30** (implied **±4.8%**, D2; short 4.3% float **covering**, DTC 3.2;
FINRA 5v5 **+6.0▲**) · **Russian diesel export ban EXPIRES 07-31** (M93) · **XOM 07-31** (implied
**±4.1%**, D2; FINRA 5v5 **+8.2▲ = the board's largest short build**) · **MPC 08-04** · **PSX 08-05**.

## 7 · Verdict for BET

**The delta is with the tilt and the composition is against the `core_pick`.** The margin engine
widened on settled data for a second session and the one-axis kill moved further away; the sector's
🟢 absence is an instrument artifact, not evidence; **and the leg that is deteriorating is PSX, the
human-locked `core_pick`, whose days-21-60 excess has now flipped negative while MPC's stayed
positive.** ⚠ **Both L2 halves are reported and they disagree** — mid-cycle margin against a
top-of-cycle revision book — so **no cheapness claim is made on any of the four**, and on **VLO and
XOM it is structurally impossible to make one** (D56 ×2).

## ✅ EXIT CHECK
- [x] Continuous-track file **LED with the delta**; unchanged structure carried by reference.
- [x] flow → players → IR/primary → chain map → bottleneck → KPI/anti-signal all present.
- [x] ROTATION's flagged divergence (**#1 wflow with 0 🟢**) carries an **explicit resolution verdict** (§2).
- [x] **Commodity node carries a rate-of-change series, not just levels** (§1, four settled sessions).
- [x] **Every multiple is stated next to its margin percentile AND its revision trend** (§3) — and where
      the percentile is structurally unobtainable (**VLO, XOM**) **no cheapness claim is made.**
- [x] **Customers named and their disclosed spend checked** (§5): 4 confirm, **UPS refutes**, reported
      as dispersion rather than closure.
- [x] **No lead/lag claim is made or inherited** in this file.
- [x] Sub-sector dispersion stated (**25.3pp on days-21-60 vs a −1.59% sector move**) with the explicit
      statement that the sector label is the wrong unit.
- [x] Linter run (§ appended at BET stage batch).
