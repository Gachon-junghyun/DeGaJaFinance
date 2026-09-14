# SECTOR_DEEP_MATR — Materials · 2026-08-13 (Thu) · all prices SETTLED 2026-08-12

> **benchmark: SPY** on every relative number in this file (C1). ROTATING track ⇒ **FULL FRESH MAP**
> (last covered 2026-08-10). Analytical only — **zero buy/sell language, zero sizing (P4).**
> No 2026-08-13 bar is used anywhere. Both halves of every rate (C2). OBV never carries a claim alone (D6).
> **G1 binding**: the sweep's news-velocity column is NOT citable and is not cited. Every news item below
> comes from **this file's own `module_news_data` calls**, quoted with the call timestamp.

---

## §0 · THE ASSIGNED QUESTION — RESOLUTION VERDICT

**Question**: *the PRICE says Materials is one name; the ACCUMULATION axis says half the sector. Which window is right?*

### 0a. Verdict, in one line

> **The PRICE window is right, the ACCUMULATION window is a 20-day trailing artifact that has ALREADY
> inverted — and both are describing the past. The window that carries information is a THIRD one
> (commodity QoQ *rate* + estimate revisions), and it condemns the very name the price window found.**

This is a resolution, not a split decision. Four measurements force it, in order of weight.

### 0b. The accumulation screen is **partly a restatement of the price window**, not independent of it

The desk's "6 of 12" is `OBV accumulating AND rs20 > 0`. **`rs20 > 0` is itself a trailing-20-session
relative-return filter vs SPY.** So "6 of 12 are accumulating" already contains "6 of 12 outperformed
SPY over 20 sessions." The two windows are **not two witnesses**; one is partly reading the other's
notes. Any spread computed between the accumulating and non-accumulating halves **over a trailing
window is tautological by construction** and is not offered here as evidence.

The six (desk axes, settled 08-12): **NEM · SHW · ECL · APD · NUE · STLD** — $419.5B of $957.9B =
**43.8% of sector cap**, i.e. "half" by count (6/12) but **under half by weight**.

### 0c. On the 5-session window, **four of the six accumulating names are NEGATIVE**

Self-computed, yfinance `auto_adjust=False`, 5 settled sessions to 2026-08-12, excess vs **SPY**
(SPY 5d +0.351%). Every OBV state below is stated only alongside its RS20/RS60 momentum reading (D6).

| Basket | 5-session excess vs SPY |
|---|---|
| **ACC-6** (OBV accumulating & rs20>0) | **+1.132** |
| **ACC-5, ex-NEM** | **−1.171** ← negative |
| **NON-6** (the other six) | **−2.443** |
| **XLB** (the sector ETF) | **−0.465** |
| **NEM alone** | **+12.642** |

⇒ **The accumulating half's positive number is entirely NEM.** Strip NEM and the "accumulation" basket
is **negative in absolute terms** (−1.171 vs SPY). It only "wins" because the other half lost more.
**SHW −2.915 · ECL −2.817 · NUE −1.417 · STLD −1.396** are all negative on this window while all four
still carry OBV-accumulating states with positive RS20 (SHW +6.1, ECL +0.7, NUE +12.4, STLD +9.4).
**That is the signature of a decaying 20-day screen, not of a live 5-day sector leg.**

### 0d. Out-of-sample, the accumulation axis has **no measurable forward edge in this sector**

Because the in-sample spread is tautological (§0b), the axis was tested **properly lagged**: form the
basket on the rule at date *t*, measure **t → t+5** forward excess vs SPY. **⚠ Object discipline (D1/D2):
this uses MY OWN reconstruction of OBV (sign-of-close × volume, cumulative, 20-session change > 0) and
MY OWN rs20 (20d return − SPY 20d return), NOT the desk's `obv_norm`. It is a different object and is
labelled as one.** Universe = the 12 names, 2025-01-01 → 2026-08-12.

| Statistic | Value |
|---|---|
| Observations | **335** (overlapping) |
| Mean forward spread, accumulating − non-accumulating | **+0.233 pp** |
| Median | +0.177 pp |
| sd | 3.067 |
| **Hit rate (spread > 0)** | **177 / 335 = 52.8%** |
| t-stat | **1.39** — and **overstated**, because overlapping 5-day windows are not independent |

⇒ **A coin flip.** The reconstruction's current selection is **7 names — APD, ECL, FCX, NEM, NUE, SHW,
STLD** — which differs from the desk's six by including **FCX** (desk state: 중립, RS20 +11.2, RS60 +5.3).
**Two implementations of "accumulation" disagree on the sector's membership.** An axis that cannot
reproduce its own basket across implementations, and scores 52.8% when lagged, **cannot carry a sector
verdict.** [measured — not [unverified]]

### 0e. The **third window** inverts the price story — and it is the one with information

| Name | 5-session excess vs SPY | Current-yr consensus, 90d | 30d revision breadth |
|---|---|---|---|
| **NEM** | **+12.642** (sector's price leader) | **10.30 → 9.35 = −9.2%** | **1↑ / 11↓** |
| **FCX** | **−0.596** (flat, ignored by both windows) | **+14.6%** | **12↑ / 1↓** |
| **NUE** | −1.417 | +28.6% | 6↑/3↓ (30d) · **0↑/1↓ (7d)** — decelerating at the margin |
| **LIN** | −2.717 | ⚠ current-yr field reads **0.00 ⇒ `unknown` (C3)** | — |

⚠⚠ **LIN's "−100.0%" is an ARTIFACT of a 0.00 denominator and is NOT reported as a collapse anywhere
in this file.** LIN's estimate trend is **`unknown` (C3)**.

**The price window found exactly one name, and it is the one name the revision axis is cutting 11-to-1.
The revision axis's own leader (FCX, 12↑/1↓) is a name the price window does not see at all.**

### 0f. Why the price window's "one name" is right for a reason **it did not state**

The reason is **not** that NEM dominates the cap — **NEM is only 11.6% of sector cap**, and the desk's
own `S57` scoring on 08-10/08-11 correctly established the move was broad then (ex-NEM cap-weighted
+1.203, equal-weighted +0.908, 8 of 12 positive). The reason is that **on 08-12 that breadth vanished
and NEM did not**: **10 of 12 names are negative** on the 5-session excess vs SPY, and NEM's +12.642
sits **27× the magnitude of the sector's own −0.465 move.** The 08-10/08-11 breadth was real; it lasted
two sessions and died on the CPI session, where **XLB's exc1 of −1.49 was the worst of any sector.**

**⇒ `S57` FIRED-A on a real two-session leg. `S77` is measuring whether it was more than two sessions.
As of 2026-08-12 the S77 observable (11 non-NEM names, equal-weight 5-session excess vs SPY) reads
−1.865 — inside band C, 0.18pp from neither branch but tracking toward B.**

Self-computed S77 track, so the settle is not a surprise:

| Settled close | S77 observable | vs branches (A ≥ +2.03 · B ≤ −2.04) |
|---|---|---|
| 2026-08-07 | +1.209 | C |
| 2026-08-10 | +1.272 | C |
| 2026-08-11 | **+0.908** (registration state) | C |
| **2026-08-12** | **−1.865** | **C — 0.175pp from branch B** |

**One more session of the 08-12 shape settles S77 into B.** ⚠ The contrary axis registered with S77
stands: **XLB FINRA short-vol 5v5 trend +13.2 rising is the steepest of nine sector ETFs** — if that
short is right, **both** directional readings are early.

---

## §1 · FULL FRESH VALUE-CHAIN MAP — left to right, with the BINDING CONSTRAINT named

Eight nodes. **Binding constraint = the thing that caps throughput. Strong demand is NOT a bottleneck
and is never listed as one below** — where demand is strong it is recorded as *not* the constraint.

```
[1] ENERGY & SCRAP        [2] EXTRACTION         [3] SMELT / REFINE      [4] PRIMARY CONVERSION
    power · natgas ·   →     NEM (gold)       →   concentrate →       →    NUE STLD (EAF steel)
    scrap steel · air        FCX (copper)         cathode/doré             LIN APD (ASU / SMR gases)
                                                  ★★★ BINDING
         ↓                                            ↓                          ↓
[5] FORMULATION            [6] AGGREGATES         [7] FABRICATION        [8] END DEMAND
    SHW (coatings)      →     CRH VMC MLM      →     service centers  →     data centres · fabs ·
    ECL (hygiene)             cement/aggregate       fabricators            nonres construction ·
    CTVA (ag chem)                                                          healthcare · food
```

| # | Node | Names (cap, % sector) | **BINDING CONSTRAINT** | Sub-node dispersion, 5-session excess vs SPY, settled 08-12 |
|---|---|---|---|---|
| 1 | **Energy & scrap inputs** | *(not in universe)* | Input cost, not capacity. **Oil QoQ rate +27.6% → −14.5%** (§2) — the input side is *loosening*, which relieves rather than binds | n/a |
| 2 | **Extraction** | NEM $110.8B (11.6%) · FCX $98.7B (10.3%) | **Ore grade / mine availability.** Dated: *"Codelco's El Teniente two-year setback deepens copper fears"* — a **two-year** supply removal at a single mine | NEM **+12.642** · FCX **−0.596** — the two extraction names are **13.2pp apart** |
| 3 | **Smelting / refining** | *(no US-listed pure-play in `us_top300`)* | ★★★ **THE SECTOR'S BINDING CONSTRAINT. Smelter/refinery throughput and its geographic concentration** — *"China's copper smelting grip worries veteran metallurgist"*, *"Copper: Near record highs on tight supply – ING"*. **Demand is explicitly NOT the constraint** — customer capex is *rising* (§4: MSFT +16%, AMZN +12%, MU +22% QoQ) | **Unpriceable in this universe — the binding node has no listed expression.** This is the map's single most important structural fact |
| 4 | **Primary conversion** | NUE $55.5B · STLD $36.0B · LIN $236.8B (24.7%) · APD $62.4B | **Steel: the index-linked contract repricing lag, not order books** (§3b — 85% of NUE sheet sales reprice monthly/quarterly to market indices). **Gases: on-site plant capital + a 10–20yr contractual ceiling** (§3a) — *not* demand | NUE −1.417 · STLD −1.396 · LIN −2.717 · APD **+2.692** — **APD and LIN are 5.4pp apart inside one "gases" label** |
| 5 | **Formulation / specialty** | SHW $79.1B · ECL $75.7B · CTVA $52.6B | SHW/ECL: `unknown` (C3) — not established this run. CTVA: **Black Sea grain disruption is a *price* event its equity is not expressing** (§7) | SHW −2.915 · ECL −2.817 · CTVA **−4.342 (worst in sector)** |
| 6 | **Aggregates / cement** | CRH $74.3B · VMC $39.3B · MLM $36.6B | **Not customer spend** — the data-centre customers are still accelerating capex (§4). Constraint is `unknown` (C3); the *flow* gap is the third run in a row with no confirmation | CRH −2.361 · VMC −2.579 · MLM −2.062 — **tight cluster, uniformly negative** |
| 7 | **Fabrication / distribution** | *(service centers, fabricators — not in universe)* | Per NUE 10-K, this node is the steel mills segment's direct customer | not measurable in this universe |
| 8 | **End demand** | *(customers — see §4)* | ★ **Demand is NOT binding at any node measured.** Every disclosed customer capex series in §4 that matters (hyperscaler, memory) is **rising** QoQ | n/a |

**Structural note carried and re-verified**: Materials has **zero names in the mcap top-50**, so its
sweep-level aggregate cannot move on that bar regardless of run count. Everything above is name-level
or primary-source.

---

## §2 · ★★★ QoQ RATE-OF-CHANGE SERIES — the commodity nodes

**The level is the distraction. Two consecutive declines in the RATE is the signal.** Quarterly average
of settled daily closes (yfinance, `auto_adjust=False`), then QoQ % change of that average. **⚠ The
2026-09-30 bucket is a PARTIAL quarter (2026-07-01 → 2026-08-12) and is marked `p` — it is shown but
never counted as a completed decline.**

### 2a. Traded commodity nodes

| Quarter | **Copper** HG=F | rate | **Gold** GC=F | rate | **Steel** HRC=F | rate | *Oil* CL=F (input) | rate |
|---|---|---|---|---|---|---|---|---|
| 2024-12 | 4.228 | +0.0% | 2661.8 | +7.6% | 697.4 | +2.0% | 70.32 | −6.6% |
| 2025-03 | 4.571 | +8.1% | 2867.9 | +7.7% | 805.4 | +15.5% | 71.42 | +1.6% |
| 2025-06 | 4.718 | +3.2% | 3279.8 | +14.4% | 895.8 | +11.2% | 63.68 | −10.8% |
| 2025-09 | 4.844 | +2.7% | 3461.8 | +5.5% | 838.8 | −6.4% | 64.99 | +2.1% |
| 2025-12 | 5.150 | +6.3% | 4147.3 | **+19.8%** | 860.0 | +2.5% | 59.14 | −9.0% |
| 2026-03 | 5.791 | **+12.5%** | 4863.4 | +17.3% | 984.4 | **+14.5%** | 72.67 | +22.9% |
| 2026-06 | 6.162 | **+6.4%** ▼1 | 4514.0 | **−7.2%** ▼2 | 1088.9 | **+10.6%** ▼1 | 92.70 | +27.6% |
| **2026-09p** | **6.369** ← series HIGH | **+3.4%** ▼2p | 4121.2 | **−8.7%** ▼3p | **1169.6** ← series HIGH | **+7.4%** ▼2p | 79.28 | −14.5% |

### 2b. What the rate says that the level hides

| Node | Two consecutive declines in the RATE? | Read |
|---|---|---|
| **GOLD** | ✅ **YES — on COMPLETE quarters alone** (+19.8 → +17.3 → **−7.2**), and the rate is now **NEGATIVE**, extending to −8.7% partial | ★★★ **Fully qualified. The signal has fired.** The quarterly average gold price is *falling*, not merely rising more slowly |
| **COPPER** | ⚠ **One complete (+12.5 → +6.4), second only on the partial quarter** | The **level is at a series high ($6.369)** and the tape is calling it a record — *"Copper jumps to its highest level ever"* — while the **rate has fallen by 73% from its Q1 peak.** Sits against a **100th-percentile spec long** |
| **STEEL** | ⚠ **One complete (+14.5 → +10.6), second only on the partial quarter** | Same shape: **level at a series high ($1,169.6)**, rate down 49% from Q1. Still strongly positive |
| **INDUSTRIAL GASES** | ❌ **OPPOSITE — re-accelerating** | No traded spot exists; proxied by revenue (§2c) |

★★★ **The single most important line in this file**: **gold is the ONLY node where the two-consecutive-
decline signal is fully qualified on completed quarters — and gold's equity, NEM, is the name the PRICE
window identified as "the one name" (+12.642 excess vs SPY).**

### 2c. The gases node has no traded price — so the rate is taken from revenue

Quarterly Total Revenue, QoQ rate. **⚠ NUE 2026-06 and CTVA 2026-06 are NaN in the source; the "0.00"
those rows produce is a pad artifact and is reported as `unknown` (C3), NOT as flat.**

| Node | Name | QoQ revenue rate series (oldest → newest) | Two consecutive declines? |
|---|---|---|---|
| **Gases** | **LIN** | +1.4% → +1.7% → **+0.2%** → **+5.8%** | ❌ **No — re-accelerating**, and +5.8% is its best in five quarters |
| **Gases** | APD | +4.8% → −2.0% → +2.2% → −0.3% | ❌ No — choppy, amplitude ±5pp |
| **Copper** | **FCX** | −8.1% → −19.2% → **+10.7%** → **+12.8%** | ❌ **Opposite — two consecutive RISES** |
| **Gold** | **NEM** | +3.9% → **+23.4%** → **+7.2%** → **−16.3%** | ✅ **YES — two consecutive declines, ending NEGATIVE** |
| **Steel** | STLD | +5.8% → −8.6% → +17.9% → +17.0% | ❌ No |
| **Steel** | NUE | +8.0% → +0.8% → −9.8% → +23.5% → `unknown` | ❌ No (latest quarter unavailable) |

★★★ **Triple confirmation on ONE name, from three independent axes**: gold's spot QoQ rate has two
complete-quarter declines into negative (§2a); **NEM's own revenue QoQ rate has two consecutive declines
into negative (−16.3%)**; and NEM's estimate revisions are **−9.2% / 1↑11↓**. **Three axes, one
conclusion, on the sector's price leader.**

★★ **And the mirror image**: **FCX's revenue rate is rising two quarters running (+10.7%, +12.8%) with
estimates +14.6% / 12↑1↓ — while its price excess vs SPY is −0.596.** The name with the strongest rate
and revision evidence has the flattest price.

---

## §3 · CONTRACT TERMS read from filings — because "margin must mean-revert" needs terms, not vibes

### 3a. LIN — the take-or-pay structure, and it **is** producing the QoQ series

`python -X utf8 -m module_business_us LIN --json` → **10-K, filed 2026-02-25, period 2025-12-31**
(`0001628280-26-011430`). Quoted from Item 1:

> *"On-site product supply contracts generally are total requirement contracts with terms typically
> ranging from 10-20 years and containing minimum purchase requirements and price escalation provisions."*

and on the cost side:

> *"The company mitigates electricity, natural gas, and hydrocarbon price fluctuations contractually
> through pricing formulas, surcharges, cost pass-through and tolling arrangements."*

⚠ **Precision (D1/D2)**: the literal phrase *"take-or-pay"* does **not** appear in Item 1. The
**mechanism** does — *minimum purchase requirements* over *10–20 years* is take-or-pay in substance.
Stated as mechanism-present / term-absent, not as a quotation of a word the filing does not use.
⚠ **The on-site share of total LIN revenue is `unknown` (C3)** — not disclosed in the section read.

**Does the contractual ceiling produce the QoQ series? YES — and the amplitude proves it.**

| Name | QoQ revenue rate, 5-quarter range | Amplitude | Contract structure |
|---|---|---|---|
| **LIN** | +0.2% to +5.8% | **5.6 pp** | Minimum purchase + escalation + cost pass-through, 10–20yr |
| **FCX** | −19.2% to +12.8% | **32.0 pp** | Commodity-priced |

⇒ **LIN's revenue rate moves in a band one-sixth as wide as FCX's.** A **"LIN's margin must
mean-revert"** claim therefore **fails on the terms**: escalation clauses and cost pass-through
insulate the margin in **both** directions, so there is no cyclical mean for it to revert to on the
timescale the price is moving. **The contractual floor-and-ceiling is visible directly in the measured
QoQ amplitude.** This is also why LIN's −2.717 excess vs SPY and 분산 OBV state (RS20 −9.1, RS60 −9.8)
**cannot be a demand read** — its revenue rate *re-accelerated* to +5.8% in the same window.

### 3b. NUE — the contracts are **NOT** a ceiling. They are an index-linked LAG

`python -X utf8 -m module_business_us NUE --json` → **10-K, filed 2026-02-25, period 2025-12-31**
(`0001193125-26-071575`):

> *"We estimate that approximately 85% of our sheet steel sales in 2025 were to contract customers.
> These sheet sales contracts are noncancellable agreements that generally incorporate monthly or
> quarterly price adjustments reflecting changes in the current market-based indices and/or raw material
> cost, and typically have terms ranging from six to 12 months."*

⚠ **Scope (C3/C4)**: **85% is of SHEET sales only**, not of total sales. Steel mills is **62% of sales
to external customers** (same 10-K). **The contracted share of NUE total revenue is `unknown` (C3).**

★★★ **This inverts the usual reading.** Contract cover is normally cited as protection. Here the terms
say the opposite: **monthly-or-quarterly repricing to market indices means the contracts transmit HRC,
they do not damp it — with a lag of one to two quarters, and no more.**

⇒ **A measured, terms-grounded lead/lag claim** (requirement 8 — this is derived from contract language,
not from a price correlation): **HRC's rate deceleration (+14.5% → +10.6% → +7.4%p) must reprice into
~85% of NUE's sheet book within one to two quarters.** And the estimate axis is **already turning
exactly on that schedule**: **+28.6% over 90d, but 6↑/3↓ over 30d and 0↑/1↓ over 7d.** The
deceleration at the margin is not noise — **it is what the contract terms predict.**

⚠ **Any claim about lead/lag between the commodity rate and the equity's excess return vs SPY that is
NOT derived from these contract terms is `[unverified]` in this file — no such correlation was measured.**

### 3c. "Cheap on forward multiple" — every such claim carries margin-in-own-history AND revision trend

`scripts/margin_history.py`, re-run this run against SEC XBRL. Forward P/E `[live 2026-08-13]`.

| Name | Fwd P/E | FY2025 gross margin | Position in own history | **Estimate-revision trend** | Verdict on "cheap" |
|---|---|---|---|---|---|
| **NEM** | **10.97** | ⚠ **`unavailable`** — `margin_history.py` returns *"연간 데이터 없음"*; NEM's XBRL gross-margin tag does not resolve. **Tooling gap, `unknown` (C3), not skipped** | `unknown` (C3) | **−9.2% / 90d · 1↑11↓** | ★★★ **NOT established as cheap.** The multiple is falling because the **denominator** is being cut 11-to-1. With the margin percentile unavailable, **the one axis that could distinguish "cheap" from "peak-earnings trap" is missing** |
| **FCX** | 16.52 | **26.1%** vs own 15-yr **median 28.9%** (range −87.7% to +47.7%) | **Below median** | **+14.6% / 90d · 12↑1↓** | Below-median margin **and** rising estimates — the one name here where "cheap" is not contradicted by its own denominator. Not statistically cheap on multiple |
| **NUE** | 14.49 | **11.9%** vs own 19-yr **median 11.9%** | ★ **Exactly the median** | +28.6%/90d but **0↑/1↓ over 7d** | **Median margin, mid multiple** — no valuation edge in either direction; the forward bet is the backlog, and §3b says the contract reprices against it |
| **STLD** | 13.84 | `not re-run this run` (C3) | — | — | No claim made |
| **LIN** | **24.59** | ⚠ *"연간 데이터 없음"* — **tooling gap, `unknown` (C3)** | `unknown` | ⚠ **`unknown` (C3)** — current-yr field reads 0.00; **the "−100.0%" is an ARTIFACT** | **No "cheap" claim is possible on LIN this run** — two of the three required axes are unavailable |
| SHW 26.61 · ECL 29.44 · APD 21.17 · CTVA 18.29 | — | not re-run | — | — | No claim made |

---

## §4 · The nodes' CUSTOMERS, and their DISCLOSED spend

Customers are named **from the filings**, and their spend is measured from **their own disclosed
quarterly capital expenditure** (QoQ rate — not levels, per §2's discipline).

**Named by the filings**: LIN serves *"healthcare, chemicals and energy, manufacturing, metals and
mining, food and beverage, and electronics"* (10-K FY2025, Item 1). NUE's steel mills segment *"sells its
products primarily to steel service centers, fabricators and manufacturers"*, with end markets *"tied to
… nonresidential construction, durable goods and capital spending"* (10-K FY2025, Item 1).
⚠ **FCX and NEM customer disclosure is `unknown` (C3) — `module_business_us FCX` and `NEM` returned
empty stdout on two attempts this run (JSONDecodeError on an empty payload). Tooling gap, stated not skipped.**

| Node | Customer proxy | Disclosed capex, QoQ rate (4 most recent reported quarters) | Read |
|---|---|---|---|
| **Aggregates + steel** (CRH/VMC/MLM, NUE/STLD) | **MSFT** | +14% → **+54%** → +3% → **+16%** | ★ **Accelerating.** The customer is spending |
| | **AMZN** | +29% → +9% → +13% → **+12%** | ★ **Steady double-digit.** The customer is spending |
| **Gases — electronics** (LIN/APD) | **MU** | +93% → −5% → +18% → **+22%** | ★ **Accelerating** — corroborates *"Linde (LIN) vs. Air Products (APD): Racing for the Chip Boom"* |
| | INTC | −32% → +44% → +4% → **−30%** | Choppy, no trend |
| **Gases — chemicals/energy** (LIN/APD) | DOW | −15% → +1% → −11% → +26% | Small base ($0.63B), choppy |
| | LYB | −25% → +11% → −40% → **+0%** | ★ **$0.27B and flat** — this customer is **not** spending |
| **Copper — wire/utility** (FCX) | NEE | +20% → −10% → +44% → −11% | Choppy |
| | ETN | +37% → −12% → +120% → −51% | Choppy, small base |

★★ **The finding this table produces**: **at every node where the equity is weak, the customer is
strong.** Aggregates are the three-run flow laggards (CRH −2.361, VMC −2.579, MLM −2.062 vs SPY) while
their data-centre customers post +16% and +12% QoQ capex. **This is why §1 lists demand as NOT the
binding constraint anywhere.** ★ And it **splits LIN's own customer base**: electronics capex
accelerating (MU +22%), chemicals capex flat on a small base (LYB $0.27B, +0%) — **which is the direct
mechanism behind LIN's revenue rate re-accelerating to +5.8% while its price fell 2.717 vs SPY.**

⚠ **Print dates for the observables that are not yet disclosed** are given in §8 rather than asserted here.

---

## §5 · SUB-SECTOR DISPERSION — the sector label is the wrong unit

Equal-weight 5-session excess vs **SPY**, settled 2026-08-12:

| Sub-sector | Names | Excess vs SPY |
|---|---|---|
| **Gold** | NEM | **+12.642** |
| **Gases** | LIN, APD | −0.012 |
| **Copper** | FCX | −0.596 |
| **Steel** | NUE, STLD | −1.407 |
| **Aggregates** | CRH, VMC, MLM | −2.334 |
| **Coatings / hygiene** | SHW, ECL | −2.866 |
| **Ag chemicals** | CTVA | **−4.342** |
| | **SPREAD (max − min)** | **16.984 pp** |
| | **XLB, the "sector move"** | **−0.465 pp** |

> ### ⇒ **The dispersion is 36.5× the sector move. On this bar, "Materials" is not a unit of analysis.**

Any statement of the form *"Materials is doing X"* on 2026-08-12 is **arithmetically dominated by which
sub-sector you happen to weight.** This is the mechanical reason the desk's own **G3 flipper rule**
exists here — and note the flip runs the *other* way from the price story: **`wflow` −0.106 flips to
+0.115 ex-LIN**, i.e. **the aggregate is distorted by LIN (24.7%, the sector's worst flow name, RS20
−9.1 / RS60 −9.8 with a 분산 OBV state), not by NEM (11.6%).** **The "one name" distorting the
cap-weighted flow number and the "one name" carrying the price are DIFFERENT NAMES, pulling in opposite
directions.** No verdict in this file rests on `wflow`.

Admissible axes only, restated: **eqflow −0.029 · delta −0.037 · breadth 0.00 · 0 green / 3 red of 12.**

---

## §6 · FRAME-TRANSFER QUESTION — asked and answered with a measurement

> **Q: A sector label is a claim that its members share a driver. Transfer the frame from equity-sector
> accounting to factor accounting: if "Materials" is a real object, its sub-sectors' excess returns vs
> SPY should co-move. Do they — and if not, what are the real objects?**

Pairwise correlation of the seven sub-sector **excess-vs-SPY daily return** series, trailing 60 sessions:

| | gold | copper | steel | gases | coat/hyg | aggreg | ag |
|---|---|---|---|---|---|---|---|
| **gold** | 1.00 | **0.65** | 0.09 | 0.01 | −0.08 | 0.16 | −0.03 |
| **copper** | **0.65** | 1.00 | 0.20 | −0.13 | **−0.24** | 0.01 | −0.07 |
| **steel** | 0.09 | 0.20 | 1.00 | 0.12 | 0.33 | 0.37 | 0.21 |
| **gases** | 0.01 | −0.13 | 0.12 | 1.00 | 0.43 | 0.29 | **0.58** |
| **coat/hyg** | −0.08 | −0.24 | 0.33 | 0.43 | 1.00 | **0.70** | 0.38 |
| **aggreg** | 0.16 | 0.01 | 0.37 | 0.29 | **0.70** | 1.00 | 0.28 |
| **ag** | −0.03 | −0.07 | 0.21 | **0.58** | 0.38 | 0.28 | 1.00 |

**Mean off-diagonal correlation = 0.202** (max +0.70, min −0.24).

And the driver that separates them — correlation of each sub-sector's excess vs SPY with **UUP**'s daily
return, 60 sessions:

| gold | copper | steel | coat/hyg | aggreg | ag | gases |
|---|---|---|---|---|---|---|
| **−0.53** | **−0.35** | −0.03 | 0.00 | +0.06 | +0.12 | +0.24 |

> ### **A: No. There are TWO objects wearing one label.**
>
> **(i) A dollar-priced metals complex** — gold and copper, correlated **+0.65** with each other and
> **−0.53 / −0.35** to the dollar. Its driver is USD and mine supply.
> **(ii) A domestic-industrial complex** — gases, coatings/hygiene, aggregates, ag, correlated **+0.28 to
> +0.70** among themselves and **0.00 to +0.24** to the dollar. Its driver is customer capex (§4).
> **Steel straddles both** (+0.20 to copper, +0.37 to aggregates, −0.03 to USD).
>
> **This is the deep answer to §0's question.** The PRICE window is reading object (i), where one name is
> at a JV-event extreme. The ACCUMULATION window is averaging across (i) and (ii), which have a mean
> correlation of 0.202 — **it is computing a mean over a bimodal distribution, and the mean of a bimodal
> distribution describes neither mode.** *That* is why the two windows disagree: **they are not two
> readings of one sector, they are one reading each of two different sectors.**

---

## §7 · CHAIN-HOP CANDIDATES — from this file's own calls, timestamped (G1)

All items below are from **`module_news_data` calls made by this file**, `CALL_TS 2026-08-13T14:11:04Z`
through `14:11:34Z`. The sweep's velocity column is **not** used.

**`chain-hop "copper smelter treatment charge" --days 7`** → **0 articles scanned, 0 candidates.**
Recorded as a null result, not as absence of the theme — the same window's `fts search` returned 453
copper hits, so **the chain-hop scanner and the FTS index disagree on the same corpus.** Tool
inconsistency, flagged.

**`fts search` results, all `--days 7`:**

| Query | Hits | Most load-bearing items |
|---|---|---|
| `copper` | **453** | *"Codelco's El Teniente two-year setback deepens copper fears"* (mining, 08-05) · *"Copper: Near record highs on tight supply – ING"* (fxstreet, 08-07) · *"China's copper smelting grip worries veteran metallurgist"* (mining, 08-05) · *"Copper jumps to its highest level ever"* (CNBC, 08-06) |
| `El Teniente` | **11** | *"Copper Prices Supported by Supply Concerns"* (hellenicshipping, 08-06) · *"Copper Scales Record Levels on Supply Worries"* (08-07) |
| `Newmont` | **116** | *"Newmont's rally is running hot: Stock gains 12% in one week; more upside ahead?"* (seekingalpha, 08-11) |
| `Novorossiysk` | **40** | *"Russia's Black Sea Port of Novorossiysk on Fire, NASA Data Show"* (bloomberg, 08-12) · *"Russia warns of 'chaos' in global food market after Ukraine pummels grain terminals"* (scmp, **08-13**) · ★ *"Kyiv stops strikes on Russian port after request from JD Vance"* (semafor, **08-12**) |
| `industrial gases` | 4 | *"Linde (LIN) vs. Air Products (APD): Racing for the Chip Boom"* (08-06) |
| `Nucor steel` | **0** | Null — no US-corpus steel-specific item in 7 days |
| `steel tariff` | **0** | Null |

### 7a. Candidates, and why none reaches chain-hop eligibility

- ★★★ **Copper supply → the smelting node (node 3).** The theme is **heavily headline-named (453 hits,
  CNBC/ING/Reuters-tier)** — by the chain-hop definition it is **already crowded, not a hop.** The genuine
  hop would be a **smelter/refiner**, and **node 3 has no `us_top300` expression** (§1). **The binding
  constraint is unexpressable in this universe.** FCX is the only listed proxy and it is the *mine* side.
- ★★ **Black Sea grain → CTVA/ADM.** ⚠ **This file's own call materially updates EVENT_ALPHA Card 6's
  "BUILDING" read**: alongside the fire and the Turkish transit restrictions, **`semafor` 08-12 reports
  Kyiv halting strikes on the port at JD Vance's request** — a **de-escalation datapoint dated the same
  day**. The thread is **contested, not monotonically building.** Both US-universe expressions remain
  unconfirmed by flow: **CTVA is the sector's worst name at −4.342 excess vs SPY with a 분산 OBV state
  (RS20 −12.9, RS60 −12.6)**; CF/MOS/NTR/BG are outside `us_top300`. **No eligibility.**
- **NEM's 12% week is independently corroborated** — the seekingalpha 08-11 body reports the same ~12%
  one-week gain this file measures as **+12.642 excess vs SPY** (D5: two independent sources agree).
- **AI → power → copper (FCX)**: the customer capex is confirmed rising (§4) but **FCX's excess vs SPY is
  −0.596 with a 중립 OBV state (RS20 +11.2, RS60 +5.3)** — the composite tag, not OBV alone, is what
  withholds confirmation. **No flow confirmation for the third consecutive run.**

**No Materials chain-hop candidate reached eligibility this run.**

---

## §8 · TRACK-KPIs AND ANTI-SIGNALS — dated observables

| # | Observable | Reads at settled 2026-08-12 | Confirms / falsifies |
|---|---|---|---|
| 1 | **`S77`** — 11 non-NEM names, equal-weight 5-session excess vs SPY, settles **2026-08-19** | **−1.865** (self-computed; band C) | **0.175pp from branch B (≤ −2.04).** One more 08-12-shaped session settles it into B = the UW's first NEM-free confirmation. **A ≥ +2.03 forces a tilt change** |
| 2 | ★★★ **Gold QoQ rate, 3rd consecutive decline** — completed **Q3 2026 (prints 2026-10-01)** | **−7.2% (Q2, complete) → −8.7% (Q3 partial)** | A completed third decline = the deceleration is a trend, and NEM's +12.642 excess vs SPY was the top |
| 3 | ★★ **Copper QoQ rate, 2nd COMPLETE decline** — Q3 2026 average, **prints 2026-10-01** | +12.5 → +6.4 (1 complete) → +3.4%p | **A completed second decline fires the signal on copper while the LEVEL is at a series high.** This is the file's cleanest forward test |
| 4 | ★★ **Steel HRC QoQ rate, 2nd COMPLETE decline** — Q3 2026, **prints 2026-10-01** | +14.5 → +10.6 (1 complete) → +7.4%p | Per §3b's contract terms, this reprices into ~85% of NUE's **sheet** book within 1–2 quarters |
| 5 | **NUE 7-day revision breadth** | **0↑ / 1↓** (vs 6↑/3↓ at 30d, +28.6% at 90d) | ★ **The contract-lag prediction's live tell.** Continued 7d deterioration = §3b confirmed |
| 6 | **FCX estimate breadth holding 12↑/1↓** while price excess vs SPY stays flat | **+14.6% / 90d, −0.596 excess** | The widest price-vs-fundamental gap in the sector. Convergence either way resolves §0e |
| 7 | **NEM 8-K for the Nevada JV settlement on EDGAR** | Not confirmed filed as of this run | Terms should confirm the $1.95bn figure and the IPO-consent language |
| 8 | **Copper spec net COT** — next Tuesday snapshot | **+77,123 = 100th percentile — the ceiling** | ⚠ **It cannot go higher by definition.** Any decline = the crowded long capping, against a decelerating rate (§2a) |
| 9 | **Gold spec net COT** | +197,634, **29th percentile — neutral** | ★ **Gold positioning is NOT crowded** — so NEM's move is not a positioning unwind risk; it is an earnings-quality risk (§0e) |
| 10 | **XLB FINRA short-vol 5v5 trend** | **+13.2 rising — steepest of nine sector ETFs** (level z −0.46) | S77's registered contrary axis. If the short is right, **both** §0 windows are early |
| 11 | **NUE short-vol z** | **−1.68, GREEN covering** | Covering into a decelerating commodity rate = the disagreement to watch |
| 12 | **XLB implied move ±1.2%** (D1 2026-08-14) · **P/C 0.26 = complacent** | — | **Any S77 move inside ±1.2% is LOW-INFORMATION** until a later session extends beyond it |
| 13 | **Broad USD `DTWEXBGS`** | **119.06, −1.41 over 30 days** | §6 says this is the driver of **object (i) only** (gold −0.53, copper −0.35). A USD reversal hits metals and **leaves gases/aggregates/ag untouched** |
| 14 | **Customer capex, next prints**: MSFT/AMZN (Sep–Oct FY reports), MU (late Sep) | MSFT **+16%**, AMZN **+12%**, MU **+22%** QoQ | **Demand is not the binding constraint (§1).** A QoQ rate turning negative at MSFT *or* AMZN would be the first evidence that it might become one |
| 15 | **Aggregates flow** (CRH/VMC/MLM) | −2.361 / −2.579 / −2.062 excess vs SPY | **Three runs, no confirmation, while customer capex accelerates.** Either the flow is wrong or the chain is |
| 16 | ★ **Black Sea de-escalation** — whether the JD Vance strike-halt (semafor 08-12) holds | Contested; CTVA −4.342 excess vs SPY, 분산 OBV (RS20 −12.9) | ⚠ **Anti-signal, registered**: if the halt holds and grain prices retrace, **EVENT_ALPHA Card 6's "BUILDING" label is falsified** |

### 8a. ★ Anti-signals against **this file's own** verdict

Registered so the verdict is falsifiable rather than merely argued:

1. **If `S77` settles branch A (≥ +2.03) on 2026-08-19**, §0's verdict is **WRONG**: a NEM-free
   sector leg would exist, the accumulation window would have been reading it correctly, and the
   08-12 collapse would have been the one-session artifact — not the 08-10/08-11 breadth.
2. **If NEM's 30-day revision breadth turns net-positive** while gold's Q3 rate completes above −7.2%,
   §2b's "triple confirmation" collapses to one axis (price) and §0e's inversion fails.
3. **If FCX's 12↑/1↓ breadth deteriorates without its price falling**, §0e's "third window" loses the
   name that makes it more than a bearish read on NEM.
4. **If the accumulation axis's forward spread over the NEXT 20 settled sessions exceeds +1.0pp**, the
   52.8% / t=1.39 out-of-sample result in §0d was an unlucky sample and the axis deserves rehabilitation.

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
