# BET_SHEET — industry_US · 2026-08-08 (Sat) · Stage 8/10 (L1·BET)

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split it.
> All prices and flow tags are **settled 2026-08-07** closes (`SECTOR_FLOW_US.json`, `asof 2026-08-07`).
> Benchmark **SPY** named inline on every relative number (C1).
> **P4 — sizing language below is INFLUENCE ILLUSTRATION ONLY. Zero buy/sell recommendation.**

## ⚠⚠ READ THIS BEFORE ANY SECTION — what the DEEPs actually returned

**This run's five DEEP agents corrected the desk on four separate objects.** Every section below is
written on the corrected numbers, not on the sweep's face value:

1. 🚨 **The `🟢` tag means two different things and the split is exact.** Of 23 greens, **15 are
   volume-lit** (`vol_surge` > 1.0) and **8 are news-velocity-lit** (`vol_surge` < 1.0, on a stable
   ~50-name whitelist). **Both Energy greens and 3 of 4 Financials greens are velocity-lit on
   BELOW-average volume.** ⇒ **no candidate below is admitted on a green tag alone.**
2. 🚨 **XLB's 5-session excess ex-NEM is +0.194**, against **+1.307** as reported and **+1.9** to fire
   S57's branch A. Ex-{NEM, ALB, FCX} it is **−0.485 — a sign flip.**
3. 🚨 **All three big banks' own 10-Q rate-sensitivity tables score a short-end-down move as
   NII-NEGATIVE** (JPM −$1.2bn · BAC −$1.8bn · WFC −$1.4bn per 100bp).
4. 🚨 **A second delisted security was found**: **X (US Steel)** returns no yfinance data — Nippon
   Steel's take-private completed. **EA remains 🟢 in today's sweep.** Two delisted names in one
   universe file (**D207 / D215**).

**Candidate set construction (the stage's own rule): DEEP thesis leaders ∪ `us_setup_screener` setups
∪ `US_LIVE_SHORTLIST.json`.** ⚠ **The shortlist's own Financials absence is a 0.003-wide truncation
artifact** (SWEEP §5), so the union was taken against the **full flow JSON**, not the top-15 cut.

---

# §IT-OPTICAL — the only CONFIRMED-EARLY name on the board

## COHR · Coherent Corp.

### §A · Numbers

| Metric | Value | Cross-check |
|---|---|---|
| Price (settled 08-07) | **$379.13** | yfinance |
| Market cap | **$74.2bn** | — |
| Forward P/E | **45.29×** | XBRL ↔ yfinance agree |
| Trailing P/E | 181.40× | — |
| PEG | 0.92 | — |
| P/B | 6.94 | — |
| Forward EPS | **8.371** vs trailing 2.09 | ⚠ **forward is 4.0× trailing — a racing denominator (L2's inverse trap)** |
| 52-week range | **$84.35 – $440.00** | price sits 14% below the high |
| Target mean / median | $394.62 / $400.00 (low 230, high 465) | +4.1% to mean |
| Analyst mix (0m) | 4 strong-buy · 12 buy · 5 hold · **0 sell** | — |
| ★ **FY2025 gross margin** | **35.2%** | **~25th percentile of its own 17-year history** (range 30.9–42.3%, median 37.9%) |
| Revision breadth (30d) | next-qtr **4↑/0↓** · FY **4↑/0↓** · next-FY **5↑/1↓, +7.5%/90d** | `module_fundamentals_us` |

★★ **L2 verdict, stated rather than skipped**: this is **NOT** the peak-margin/low-multiple trap. It is
**its mirror — a BELOW-median margin (25th percentile) paired with a 45.3× forward multiple. The market
is paying for a margin recovery the trailing data does not yet show.**

### §B · Thesis + freshness placeholder

**The board's ONLY `new_green` across 300 names**, and it is **volume-lit** (`vol_surge` 1.30,
`velocity` None) — not the artifact that hollowed out Energy's and Financials' flow ranks this run.
Datacenter & Communications revenue is **$1.362bn in Q3 FY26, +40.6% YoY, now 75% of total company
revenue**; COHR states it is doubling internal InP output by end-2026 and again by 2027.

★★★ **DEEP-IT's verdict is narrower than the tag: this is a SUB-LAYER bifurcation, not a layer
igniting.** COHR + **LITE** (active AI-datacentre optics, hyperscaler demand pool) are warm-to-hot;
**CIEN** (carrier capex) and **GLW** (passive, diversified) are being distributed. *"Optical" appearing
in all four 10-Ks does not make them one trade.*

**Freshness: 🟢LIVE** — `theme_age` was **not** consulted for this tag (it has returned zero
green-FRESH for eleven consecutive foreign measurements, so it cannot issue one by construction, F1).
**The tag is issued on the `new_green` ignition + a dated catalyst + an existing bracket on the node**,
and **that basis is stated rather than laundered through a gate that cannot fire.** **ALPHA owns the
final freshness stamp.**

### §C · Flow / positioning

| Axis | Reading | Grade |
|---|---|---|
| `flow_score` | **+0.833** | sweep |
| rs20 vs **SPY** | **+14.40** | A-grade price |
| rs60 vs **SPY** | ⚠ **−3.40** | **the entire rs20 sits on a NEGATIVE 60-day base** |
| `vol_surge` | **1.30** | ✅ volume-lit |
| OBV (`module_flow`) | **+0.271 매집** | ⚠ **C-grade (RULE D6) — quoted only alongside the volume and short axes, never alone** |
| FINRA short-vol | ratio **61.2%, z +1.24, 5v5 +15.4▲** | ⚠ **short pressure is RISING while OBV accumulates — two-sided positioning, not one-way conviction** |
| ATM straddle | **±14.8%, expiry 2026-08-14** | ✅ **EVENT-PRICED — the expiry is one day AFTER the print.** (Contrast Lens 2's D2-expiry instruments, which price nothing) |
| Short interest | 5.2% of float, DTC 1.6, covering | thin — no mechanical squeeze fuel |

### §D · Competition / peers

| Peer | Flow | rs20 vs SPY | Fwd P/E | GM percentile | Read |
|---|---|---|---|---|---|
| **LITE** | 🟡 +0.615 | **+8.6** | 47.5× | `[unavailable]` (XBRL only FY2013–18) | **Same demand pool.** ★ **Reports 2026-08-12, ONE DAY BEFORE COHR** |
| **CIEN** | 🔴 −0.906 | **−12.9** | 42.8× | ~29th | Carrier capex — a structurally different pool |
| **GLW** | 🔴 −0.756 | **−15.6** | 38.4× | **~60th** | Passive layer; the 07-28 crash was a **GUIDE miss**, not a demand miss. **Cheapest multiple, closest to its own mid-point — value-and-unloved** |
| **ANET** | 🟡 +0.472 | −1.5 | — | — | **rs60 vs SPY +27.60** — the strongest 60-day of any node; a pause, not distribution |

⚠ **Node gap named**: **DSP/retimer silicon (CRDO) is not in `us_top300` ⇒ no name in the universe
captures that node.** **AAOI** surfaced body-proximate but is **also outside the universe ⇒ no flow
cross-check ⇒ per the binding rule it CANNOT reach this sheet.**

### §E · Refutation + dated catalyst

**What kills it:**
- **rs60 vs SPY is −3.4** ⇒ **a last-20-day event, not a multi-month re-rating.** A second sweep
  without a confirming print retires the tag.
- **Rising short-vol z (+1.24, 5v5 +15.4▲) against accumulating OBV** — if the short leg wins, the
  ignition was a squeeze, not accumulation.
- **A revenue beat with flat-or-down gross-margin guidance** leaves a 45.3× multiple unsupported by
  the one metric that should support it.
- ⚠ **The `vol_surge` axis that lit it is the axis this desk's KR ledger scores NEGATIVE** (t −2.06)
  while the US ledger scores it positive (t +1.80). **W1 forbids importing either. The tag is not
  evidence of edge.**

**Dated catalysts:** ★ **LITE prints 2026-08-12** (the precursor read) · ★★ **COHR prints 2026-08-13**
(consensus EPS 1.617, revenue $1.981bn) · **`S48` settles 2026-09-30**, its observable now **−5.6**
(from −17.5 at registration), **inside the AMBIGUOUS band**. 🚨 **S48's basket {CIEN, ANET, AVGO, MRVL}
does NOT contain COHR — the one name igniting in this layer is not measured by the bracket on its own
node.**

---

# §ENRG — the sector was demoted, and its strongest evidence is in the names the gate does not tag

## MPC · VLO · PSX

### §A · Numbers

| | MPC | VLO | PSX |
|---|---|---|---|
| Price (settled 08-07) | $298.20 | $298.31 | $203.91 |
| Market cap | $83.7bn | $85.9bn | $81.8bn |
| **Forward P/E** | **10.04** | **10.76** | **10.24** |
| PEG · P/B | 1.48 · 4.42 | 4.08 · 3.71 | 1.19 · 2.87 |
| Target mean (upside) | $316.61 (**+6.2%**) | $309.79 (**+3.8%**) | $214.26 (**+5.1%**) |
| ★ **FY 30d revision breadth** | **13↑ / 0↓** | 13↑ / 2↓ | 13↑ / 2↓ |
| ★ **FY EPS, 90-day change** | **49.80 vs 27.03 = +84.3%** | **41.66 vs 27.95 = +49.0%** | **25.52 vs 15.91 = +60.4%** |
| ★ **FY2025 gross margin percentile** | **37.5th** (n=8) | **`[unavailable]`** — XBRL tag pairing breaks | **60th** (n=10) |

★★★ **The single most striking pairing on this sheet**: **estimates up 49–84% over 90 days against
mean-target upside of 3.8–6.2%**, and **the target upside COMPRESSED from +5.4–8.1% one session ago.**
⇒ **the revision-vs-target gap is WIDENING, not resolving.**
⚠ **L2 discipline honoured: MPC's 10.04× sits on a 37.5th-percentile margin (not a peak) and PSX's
10.24× on a 60th-percentile margin. VLO's margin percentile is `[unavailable]`, so VLO's 10.76× is NOT
called cheap — the pairing cannot be built (C3).**
⚠ **The forward-P/E ORDERING has flipped for a SECOND time in two runs** (08-07 had PSX cheapest) ⇒
**a third flip would mean the ranking itself carries no information.** Recorded now, not after.

### §B · Thesis + freshness

**Sector demoted OW− → N+ on flow decay** (eqflow +0.209 → +0.078, **Δ sign flip +0.196 → −0.084**).
**But the demote is a SECTOR statement and the refining leg is a different object**: DEEP-ENRG measured
**India's July refined-fuel exports at a one-year high (1.53m b/d, +27%), explicitly "cargoes headed to
regions previously supplied by West Asia and Russia" with Europe named** `[Kpler via toi 08-04]` — and
**the same reporting says Europe remains short**, while **US diesel inventories are down enough that
"the world's biggest diesel exporter has limited space to boost exports, even with refineries running
at record rates."** ⇒ **the US Gulf basin remains the marginal supplier of last resort.**

**Freshness: 🟡PARTIAL** on all three — **the flow gate tags them 🟡, `module_flow` tags MPC and VLO
🟢가속. The two instruments disagree and the disagreement is reported (D208), not resolved.**

### §C · Flow / positioning

| Name | sweep tag | `module_flow` tag | `vol_surge` | rs20 / rs60 vs SPY | FINRA short-vol |
|---|---|---|---|---|---|
| **MPC** | 🟡중립 (+0.414) | **🟢가속 / OBV 매집** | **1.01** | +2.70 / **+13.60** | — |
| **VLO** | 🟡중립 (+0.535) | **🟢가속 / OBV 매집** | **1.09** | +3.90 / **+16.00** | ✅ **z −1.71, ratio 48.0% → 33.5% = pressure LEAVING** |
| **PSX** | 🟡중립 (+0.394) | 🟡중립 | 1.12 | +5.80 / +11.50 | — |
| *SLB (context)* | 🔴분산 | 🔴분산 | 0.73 | — | the only outright distribution of the six |

⚠ **RULE D6**: the OBV readings above are C-grade and are quoted **only** with `vol_surge` and the
FINRA short axis. **The verdict rests on three axes agreeing, not on OBV.**

### §D · Competition / peers

**XOM 🟢가속 (+0.694)** — the shortlist's only "clean rise" (short-z **−0.59**). ⚠⚠ **DECOMPOSED and
it splits into two separate claims**: the **short-interest axis is genuinely clean** `[measured]`, but
the **green tag is velocity-lit** (`vol_surge` 0.88) and **RS60 − RS20 = −11.0 ⇒ the entire "rise" sits
on a NEGATIVE 60-day base.** 🚨 **And XOM is NOT in the book**, while bracket **S31** describes it
throughout as *"the only Energy name the book holds"* — **reproduced on a fresh deterministic pull for
the second consecutive run.**
**CVX 🟢가속 (+0.586)** — ⚠ **mis-slotted**: it sits in `cycle_registry.json`'s **oil-refining
epicenter** list, but its live driver is **Project Kilby, a 20-year 2.67 GW behind-the-meter gas deal
with Microsoft — no crack-spread content at all.** RS60 − RS20 = −7.7, same negative-base shape.

### §E · Refutation + dated catalyst

**What kills it:** ⚠ **the crack's own second derivative is moving AGAINST the physical case.** Own
calc (B1 — the rate, not the level): the distillate crack's **rate declined for a SECOND consecutive
session** (+1.534 → −0.033) and **the level turned negative for the first time this run**
(85.754 → 85.721). **A THIRD consecutive rate decline confirms release, not scarcity.**
⚠ **And six of six energy names fell on a bar crude rose +1.15% with Brent above $83** — **n = 1 (S1),
and R12 forbids calling a streak off one bar**, but **a second such session makes it an event.**

**Dated catalysts:** **`S55` settles 2026-08-11** (HO% − CL% from the 08-04 anchor, currently
**+0.318pp, deep in C**; A ≤ −3.0, B ≥ +6.5) · **`S67` settles 2026-08-13** (median rs20 vs SPY of
{MPC, VLO, PSX} = **+3.852** today) · **`S60` settles 2026-08-11** (XLE 5-session excess vs SPY
**−6.954, already 1.90pp past branch B's −5.05**) · **MPC's straddle ±7.1%, expiry 08-21.**

---

# §INDU — the board's only overweight, and its supply layer is the board's worst flow

## GEV · CAT (both REJECTED to the ledger this stage — see §Ledger) · EMR

### §A · Numbers

| | GEV | EMR |
|---|---|---|
| Price (settled 08-07) | $990.32 | $158.26 |
| Market cap | $263.8bn | $88.3bn |
| Forward P/E · PEG · P/B | **39.87** · 1.70 · **22.05** | 21.88 · 1.82 · 4.33 |
| Target mean (upside) | $1,231.48 (**+24.4%**) | $169.81 (+7.3%) |
| Revision breadth (30d) | **current-yr 7↑/10↓** · **next-yr 16↑/2↓, +2.8%** | — |
| Backlog / RPO | **$176.3bn total backlog, +37% YoY; RPO $94.4bn** | — |

### §B · Thesis

★★★ **DEEP-INDU's headline: the two INDU names with the deepest primary-filing AI-power disclosure are
the two worst flow scores on the entire 300-name board.** GEV's **10-K names the driver verbatim** —
*"remaining performance obligations… rising electricity demand from hyperscalers and data centers"* —
with a **~7,000-unit gas-turbine installed base, ~1,800 under LTSAs, ~10-year average remaining
contract life**, and **1H26 orders +89% YoY (Power +99%, Electrification +131%, Wind −11%)**.
CAT posted a **record $72.1bn backlog (+$9.4bn in-quarter)**, **raised** its 2026 sales-growth target
and **cut** its tariff-cost forecast, with **Q1 power-gen sales +41% YoY to $2.8bn** explicitly
*"driven primarily by data center applications."*

★★ **And the Kilby contract does NOT add to that.** Chevron's own executive states the equipment was
**"reserved very early — a year and a half ago"** ⇒ **the GEV and CAT allocations were booked in
H1 2025 and are already inside the backlogs both companies have reported.** **Kilby is not new order
intake; it is a disclosure of something already counted.**

**Freshness: 🔴RESOLVED on the flow axis for both** — see §E.

### §C · Flow / positioning

| Name | Flow | rs20 / rs60 vs SPY | OBV | `vol_surge` | FINRA |
|---|---|---|---|---|---|
| **GEV** | 🚨 **−0.756 — worst of 300** | **−11.70 / −12.40** | **−0.264** | 0.67 | — |
| **CAT** | 🚨 **−0.223** | **−14.00 / −12.40** | −0.156 | 1.05 | **z 0.74 = normal, NO distribution signature** |
| **EMR** | 🟢 **+0.911 (board #3)** | +11.50 / +10.50 | +0.629 | **1.44 (volume-lit)** | — |
| PWR | 🟡 −0.033 | **−0.41** / −17.02 | +0.056 | 0.76 | the only negative leg of S62's basket |

⚠⚠ **The inversion persists and is now legible**: **EMR mentions data centres ZERO times in its
primary filings and carries the sector's #1 flow score; PWR mentions them 16 times and is the only
negative leg of the bracket built on that node.**

### §D · Competition / peers

The electrical node {EMR, ETN, AME, PWR} was **S62's basket, which settled FIRED-B at +13.252 and is
now SPENT** — and **degenerate**: branch A was **19.16pp away.** ⇒ **DEEP-INDU's recommendation is that
any successor bracket freeze GEV against its OWN node, not re-run the same four names against XLU.**

### §E · Refutation + dated catalyst

**Both flow rejections have a DATED, company-specific, non-demand cause — which is exactly why they are
rejections and not verdicts:**
- **GEV**: the **07-22 adjusted-EBITDA/EPS miss** on **Wind-segment losses and capacity-ramp spending**,
  at **~40× this year's adjusted EBITDA**. **Current-year breadth 7↑/10↓ reflects the miss; next-year
  16↑/2↓ reflects unimpaired backlog confidence.** The negative is **segment-specific, not a
  demand-side repudiation.**
- **CAT**: an **08-04 post-beat fade** — gapped to **$922.00 open / $935.00 intraday high**, closed
  **$876.54** the same session, then **$871.08 → $856.96 → $842.19** = **−3.9% over three sessions.**
  **A sold-the-beat pattern, not distribution** (short-vol z 0.74 is normal).

**Dated catalysts:** **GEV next earnings 2026-10-28** · **CAT rs20 vs SPY crossing above 0, re-check
2026-08-14** · **GEV's own "at least 125 GW under contract by year end" marker** · ⚠ **`S64` settles
2026-08-13 and its first live test FAILED**: crude rose +1.15% on 08-07 and **BOTH XLE (−1.75pp) and
XLI (−0.38pp) fell vs SPY — the hypothesised hedge did not appear.**

---

# §MATR — the sector's own falsifier is 0.59pp from firing on two names

### §A · Numbers — L2 applied name by name (a multiple without a margin percentile is not a valuation)

| Ticker | Fwd P/E | EV/EBITDA | FY2025 GM | **Own-history percentile** | Read |
|---|---|---|---|---|---|
| **NEM** | 10.69 | 6.79 | `[unavailable]` | **`[unavailable]`** | **Not a valuation** — the pairing cannot be built (tooling gap, flagged not skipped) |
| **FCX** | 17.03 | 12.39 | 26.1% | 46.7% (n=15) | Mid-range margin, elevated multiple |
| **NUE** | **14.48** | 11.93 | 11.9% | **52.6%** (n=19) | Median margin; the **+57% backlog build** is a forward bet the multiple has begun to price |
| **STLD** | 13.91 | **15.48** | 13.2% | 42.1% (n=19) | Multiple ahead of the current margin print |
| **DOW** | 15.91 | 9.56 | 6.3% | **12.5% — TROUGH** | **Not cheap** (15.9×) on the **lowest GM in its own 8-year history** |
| **LYB** | **9.24** | 8.70 | 8.5% | **6.7% — the 15-YEAR MINIMUM** | ★ **The classic countercyclical setup, and a DIFFERENT object from DOW's more expensive version of the same trough** |
| **CF** | 10.42 | 5.58 | 38.5% | **78.9% — NEAR-PEAK** | 🚨 **The textbook L2 trap: a cheap-looking multiple on a top-quintile margin** |

### §B · Thesis

★★★ **The sector's headline number is two names.** XLB's 5-session excess vs SPY is **+1.307**;
**ex-NEM it is +0.194**; **ex-{NEM, ALB, FCX} it is −0.485 (a sign flip)**. **The sector itself carries
0🟢 of 12 and breadth 0.000.** ⇒ **`S57-ANNEX` holds on six independent legs.**

★★ **The one genuinely new thesis in the sector is STEEL, and it is a primary-source finding.**
**NUE's FY2025 10-K**: *"Backlogs for the steel mills segment at the end of 2025 were at historically
high levels"* — **$3.35bn vs $2.13bn = +57% y/y**, driver named as **"growing demand from data center
construction."** **STLD's 10-K**: backlog *"extending through the first half of 2026,"* demand *"largely
driven by the commercial, data center, manufacturing, warehouse, and healthcare sectors."*
**Section 232 tariffs (up to 50%) block the import competition.** ⇒ **BOTH a demand pull AND a
protected pricing regime.**

**Freshness: 🟡PARTIAL** (NUE, STLD, LYB) · **🔴RESOLVED** (NEM, CF — both to the ledger).

### §C · Flow / positioning — and the gate mechanism, verified

**NUE** rs20 vs SPY **+17.50**, rs60 **+13.90**, OBV **+0.611**, **`vol_surge` 0.95** → 🟡중립.
**STLD** rs20 **+12.50**, rs60 **+8.00**, OBV **+0.396**, **`vol_surge` 0.90** → 🟡중립.
✅ **Verified mechanically**: `module_flow`'s gate needs **3 of 4** axes (OBV 매집 · rs20 > 0 ·
`vol_surge` ≥ **1.2** · velocity ≥ 1.2). Both names **clear 2 and fail 2** — and since **velocity is
`None` for both**, **raising `vol_surge` alone to 1.2 is sufficient to cross the gate.**
⇒ **the 🟡 tag is a DETECTION-GATE artifact of a volume proxy that two large, low-beta, steadily-traded
names structurally under-clear — not a fundamental verdict.**
**NEM** 🟡중립 (+0.476), rs20 **+16.10**, rs60 **−10.40**, `vol_surge` 0.93. **FCX** 🟡 (+0.130),
**OBV −0.071 = NOT accumulating** — against copper's **100th-percentile COT long.**

### §D · Competition / peers — the fertilizer/chemicals leg is THREE constraints, not one

**5-session excess vs SPY: CF −12.17 · LYB −7.52 · DOW −6.65 · CTVA −5.90 · BALL −5.75 · CE −5.37.**
- **CF** — a **feedstock-cost margin miss**: gas at **$4.57/MMBtu vs $3.68 a year ago (+24%)**, an
  08-05 revenue *and* EPS miss (−6.2% after hours) after a **51% YTD run**.
- **DOW / LYB** — **structural overcapacity** (a global base-chemicals overbuild "not fully solved
  until 2030", worked off via European closures) **plus** the unwind of a **Hormuz-driven
  North-American ethane cost advantage** that had powered Dow's most profitable quarter in four years.
- **CTVA** — **segment pricing** (Crop Protection price −2% y/y, LatAm/APAC) under a **Q4 2026 spin-off
  overhang.**

### §E · Refutation + dated catalyst

**What kills the steel thesis:** the backlog is a **forward** claim; **NUE's current margin is only at
its own 52.6th percentile**, so the multiple is paying for conversion that has not printed.
⚠ **And both cross-sector chains the sector should confirm show NO flow**: **FCX OBV −0.071** (the
AI→power→copper chain) and **VMC −0.599 / MLM −0.668, the two worst flow scores in the entire
12-name Materials universe** (the Texas data-centre → aggregates chain). ⇒ **the narrative-vs-money gap
is not confined to Energy and Utilities; it reproduces inside Materials.**

**Dated catalysts:** **`S57` branch A fires at ANY settled close through 2026-08-12** (⚠ **check the
ex-NEM print FIRST**) · **copper's next COT, Tuesday 08-11 close, published 08-14** · **CF's Q3 gas
cost per MMBtu** · **the 08-12 CPI**, which is what the gold leg is actually trading.

---

# §FIN — the sector was demoted, and its own filings explain why

### §A · Numbers

**PRU**: price $121.28 · mcap $41.8bn · **forward P/E 8.27** · PEG 1.32 · **P/B 1.32** ·
target mean $106.93 (⚠ **BELOW the current price — a −11.8% implied**).
⚠ **L2: PRU's margin/ROTCE percentile was not computed this run ⇒ `[unavailable]`. The 8.27× is NOT
called cheap.**

### §B · Thesis

★★★ **The finding is negative and it is the strongest measured statement in this file.** DEEP-FIN
pulled the **forward-looking 12-month rate-sensitivity tables** from four 10-Qs filed within the week:

| Bank | **Short-end DOWN** (the 08-07 shape) | **Long-end UP** |
|---|---|---|
| JPM (10-Q 08-06) | **−$1.2bn** | +$1.1bn |
| BAC (10-Q 07-31) | **−$1.8bn** | +$0.2bn |
| WFC (10-Q 07-28) | **−$1.4bn** | +$0.4bn |

⇒ **all three independently score a bull steepener as NII-NEGATIVE.** **This is `[measured]`, not
inferred, and it falsifies reading the 08-07 curve move as a NIM tailwind** — corroborating S51's
pre-committed refusal with three first-party numbers.
⚠ **C2, the other half**: all three remain **asset-sensitive to rate LEVEL**. *"It's volume now, not
rates"* describes the **realised** Q2 print, not the **forward exposure**. Both are true; they are not
the same claim.

### §C · Flow — one name in 47

🚨 **Applying the full accumulation gate (`vol_surge` ≥ 1.2 ∧ OBV 매집 ∧ rs20 > 0 vs SPY) to all 47
Financials names returns EXACTLY ONE: PRU** (`vol_surge` 1.36, rs20 +2.70). Sector-wide **mean
`vol_surge` is 0.826** — the typical name trades below its own volume average. **KKR (1.14) and MET
(1.15) have the accumulation shape and miss the volume bar; XYZ and IBKR have the volume and are in
OBV 분산.**
🚨 **Only 8 of 47 names carry a populated `velocity` field — JPM, BAC, WFC, BRK-B, GS, MS, MA, V** —
and **3 of those 8 are the sector's velocity-lit greens.** ⇒ **the whitelist artifact and the D9
market-cap concentration are THE SAME EIGHT NAMES**, so any un-decomposed Financials aggregate
compounds both defects at once.

### §D · Competition / peers

**Ex-BRK-B (46 names)**: eqflow **0.0497 → 0.039 (−22%)** · wflow **0.1722 → 0.1124 (−35%)** · the
**wflow-over-eqflow premium falls +0.1225 → +0.0734, a 40% reduction on removing one name.**
**WFC**: ⚠ **the credit hypothesis was WRONG** — NCOs **−11% y/y**, commercial NCOs **18bp → 10bp**,
NPAs **−$559mm**, ACL coverage **1.45% → 1.40%** *"driven by improved credit performance"*, short-vol
**z −1.57 (covering)**. **The real story is margin: NIM 2.68% → 2.47% → 2.43% while loans grew +12% and
NII only +5%.** Its rs20 (−2.32) sits at the **regional-bank sub-node mean (−1.23 vs SPY)**, not with
its money-centre peers ⇒ **a labelling mismatch, not a hidden credit story.**

### §E · Refutation + dated catalyst

🚨🚨 **A live contamination risk, flagged before it fires**: **Berkshire reported Q2 2026 TODAY,
2026-08-08 — net earnings $25.667bn vs $12.370bn y/y (operating $12.983bn vs $11.160bn, +16.3%)** —
**a day earlier than expected and one day AFTER the 08-07 close every number in this section is
computed from.** **BRK-B is 13.94% of sector cap and one of only three velocity-lit greens.**
⇒ **a large Monday move could push `S65`'s median toward branch B for a reason ORTHOGONAL to the
NIM/curve mechanism S65 tests.** ⚠ **Ex-WFC and ex-BRK-B counterfactuals of the median are both +3.44
vs +3.352 actual, so BRK-B is not currently swinging the branch** — but **if B fires on a BRK-B move,
it is contamination, not vindication.**

**Dated catalysts:** **`S65` settles 2026-08-11** (median rs20 {JPM,BAC,WFC,BRK-B} = **+3.352**;
A ≤ +0.34 · B ≥ +6.81 — **genuinely two-sided, 3.01 / 3.46pp**) · **`S70` at the first FRED close
covering 08-07, expect 2026-08-10** (**branch B ≥ 2.96% is the only branch with real information;
branch A requires no widening at all**) · **`S66` same clock, largely inheriting S70's credit leg.**

---

# §CROSS-SECTOR — LIVE_SHORTLIST names outside the DEEP sectors

| Name | Sector | Flow | rs20 vs SPY | Note |
|---|---|---|---|---|
| **PLTR** | IT | +1.000 | **+33.20** | ⚠ **L2: op margin 26.8 → 33.3 → 40.9 → 46.2 → 47.1% = the PEAK of its own 5-quarter history, at a 74.8× forward multiple — a peak margin at a peak multiple.** RS60 − RS20 = **−11.5** ⇒ the whole 60-day excess is a last-20 event |
| **SHOP** | IT | +1.000 | +21.30 | RS60 − RS20 = **+25.8** = broad-based, but **FY breadth 2↑/3↓ is DECELERATING while price accelerates** |
| **WAT** | HLTH | +0.704 | +5.70 | ⚡ **the shortlist's only crowded-short (z +2.27)** — squeeze fuel conditional on a turn, **never a standalone reading** |
| **BMY · AMGN · IDXX** | HLTH | +0.839 / +0.794 / +0.649 | +10.0 / +10.7 / +1.7 | ✅ **volume-lit** (1.31 / 1.23 / 1.44). ⚠ **HLTH's promotion was declined for a 3rd run on its own registered anti-signal**, and **every one of these names reports 10+ weeks out (BMY 10-29 · AMGN 11-04 · IDXX 11-02)** — **best breadth on the board, no clock** |
| 🚨 **EA** | COMM | +0.671 | +0.10 | 🚨🚨 **A DELISTED SECURITY, still 🟢가속 and still ON THE SHORTLIST**, with the board's highest `vol_surge` (3.66) and highest OBV (0.749) — both computed from a liquidation print. **The FINRA proxy even returned a real short-z (+0.79) rather than an error.** **NOT a candidate. D207 / D215.** |

**⚠ Epicenter-starter module: NOT triggered.** `cycle_exposure` reports **no GAP** on any rank ≤ 2
cycle (AI-compute 19.74% vs 12.0% floor; Energy 10.23% vs 8.0%). ⚠ **But PREMORTEM Lens 4 found the
rank-3 GAP predicate is `rank <= 2 AND …`, so rank 3 CANNOT fire regardless of threshold (D217)**, and
**the AI-power / behind-the-meter chain has ~0% measured epicenter exposure while being structurally
invisible to the registry (D218).**

---

# §LEDGER — every name set aside is now a scored record

**5 rejections filed, all with both required fields** (`reject_ledger.py add` refuses either missing):

| Ticker | Class | Revives if | Recheck |
|---|---|---|---|
| **NEM** | `A.flow미도착` | FY revision breadth turns net-positive **OR** XLB clears +1.9 with NEM contributing < ⅓ | **2026-08-13** |
| **GEV** | `A.flow미도착` | flow_score ≥ 0 **OR** current-year revision breadth turns net-positive | 2026-08-14 |
| **CAT** | `A.flow미도착` | rs20 vs SPY crosses above 0 | 2026-08-14 |
| **CF** | `H.밸류소진` | GM percentile falls below its own 19-year median **OR** gas < $4.00/MMBtu | 2026-08-21 |
| **VST** | `C.차트붕괴` | FY revision breadth net-positive **AND** short-vol z < 0 | 2026-08-20 |

**4 missed entries filed, all `--sample prospective`** (the only stratum from which an edge can be
estimated — the seeded `outcome_selected` block is quoted nowhere):

| Ticker | Class | Enters if | Recheck |
|---|---|---|---|
| **PRU** | `M.숏리스트탈락` | FIN returns to OW **OR** PRU enters the top-15 flow cut with OBV 매집 intact | 2026-08-20 |
| **LITE** | `Q.확신부족` | tags 🟢가속 **OR** its 08-12 print guides Cloud & Networking above consensus | 2026-08-20 |
| **NUE** | `M.숏리스트탈락` | `vol_surge` crosses 1.2 with OBV 매집 and rs20 > 0 intact | 2026-08-20 |
| **LYB** | `Q.확신부족` | GM percentile rises above the 20th **OR** a disclosed price increase follows the European closures | 2026-08-21 |

⚠ **The line between the two ledgers was respected mechanically** — `missed_ledger add` refuses any
ticker × date already in the rejection ledger, and none of the four collided. **PRU and NUE are
`missed`, not `rejected`, because in both cases the desk never argued against them: PRU fell outside a
0.003-wide top-15 cut and NUE was blocked by a detection gate. Neither is a judgement.**

## ✅ Stage notes

- **Candidate set = DEEP leaders ∪ screener setups ∪ LIVE_SHORTLIST**, taken against the **full flow
  JSON** rather than the top-15 cut, **because the cut's Financials absence was diagnosed as a
  truncation artifact.**
- **Every number is cross-checked XBRL ↔ yfinance where both exist; blanks are stated as blanks**
  (VLO's and NEM's margin percentiles, LITE's margin series, PRU's ROTCE percentile — all
  **`[unavailable]`**, none substituted).
- **Sizing language: none. This sheet ranks evidence, not positions (P4).**

---

# §B-FRESHNESS — ALPHA stage (9/10), appended 2026-08-08

## ★★★ The gate that issues 🟢LIVE has the SAME query-form defect as three other tools — measured today

`theme-age` was run on this run's four live theses **and then re-run on their single-token
components**, `--scope foreign` throughout:

| Theme string as a phrase | verdict | n | Single token | verdict | n | accel |
|---|---|---|---|---|---|---|
| `"AI datacenter optics"` | **🔴FADING** | **2** | **`optics`** | ⚪ECHO | **1,389** | 1.6× |
| — | — | — | **`transceiver`** | **🟡ACCELERATING** | **140** | **2.99×** |
| `"gas turbine data center"` | **⚫SILENT** | **0** | **`turbine`** | **🟡ACCELERATING** | **612** | **2.18×** |
| `"steel data center"` | **⚫SILENT** | **0** | **`steel`** | ⚪ECHO | **1,759** | 1.58× |
| `"distillate export"` | 🟡ACCELERATING | 7 | **`distillate`** | **🟡ACCELERATING** | **687** | **2.29×** |
| — | — | — | `polysilicon` | 🟡ACCELERATING | 63 | **21.86×** |

🚨🚨 **A multi-word theme string returns n ≈ 0–7 while its own components return n = 63–1,759, and a
zero-n theme is reported as ⚫SILENT or 🔴FADING — which is INDISTINGUISHABLE from a dead theme.**
⇒ **`theme-age` is the FOURTH tool in the R25 / D166 / D209 quoted-phrase silent-failure class, and it
is the one that decides this desk's headline freshness tag.** **New dig `D219`.**

★★★ **And this partially REFRAMES `F1`.** The desk has recorded *"🟢FRESH = 0 for eleven consecutive
foreign measurements"* as arithmetic — the gate needs ≤14-day age and the board's themes are older.
**That remains true on the single-token forms** (`transceiver` 73d · `polysilicon` 64d · everything
else ≥90d, so **🟢FRESH is still structurally unissuable and this is a 12th consecutive zero**). ⚠ **But
part of the historical zero is a QUERY-FORM artifact rather than a property of the market**, and **the
two readings have never been separated before.** ⇒ **the single-token measurement is the honest one and
is what is used below.**

⚠⚠ **The tag inversion is concrete**: the optical/interconnect thesis this run promoted a 5th DEEP slot
for reads **🔴FADING** on the phrase form and **🟡ACCELERATING (2.99×, n=140)** on `transceiver`.
**Had ALPHA used the phrase form, it would have killed its own promoted thesis on a query defect.**

## The tags

| Name | Tag | Basis, and the residual |
|---|---|---|
| **COHR** | **🟢LIVE** | ⚠ **NOT issued by `theme_age`** — that gate cannot fire (F1, 12th run). Issued on: the board's **only `new_green` of 300**, **volume-lit** (`vol_surge` 1.30), an **event-priced straddle (±14.8%, expiry 08-14 — one day AFTER the print)**, a **dated catalyst 2026-08-13**, and an **existing bracket (S48) on its node**. **The basis is stated rather than laundered through a gate that cannot fire.** ⚠ **Residual: rs60 vs SPY −3.4 — a last-20-day event on a negative base.** **Re-check 2026-08-13 (the print).** |
| **MPC** | **🟡PARTIAL** | FY revision breadth **13↑/0↓**, FY EPS **+84.3%/90d**, margin at the **37.5th percentile (not a peak)**, `module_flow` 🟢가속/매집 on `vol_surge` 1.01. **Residual: the sweep gate tags it 🟡 and the two modules disagree (D208); and the crack's own rate has declined two consecutive sessions.** **Dated re-check: 2026-08-11 (S55) and 2026-08-13 (S67).** |
| **VLO** | **🟡PARTIAL** | Same revision shape (13↑/2↓, +49.0%/90d) plus **FINRA short-vol z −1.71, ratio 48.0% → 33.5% = pressure LEAVING**. ⚠ **Residual and it is specific: VLO's margin percentile is `[unavailable]` — the XBRL tag pairing breaks — so its 10.76× forward multiple is NOT called cheap (L2, C3).** **Re-check 2026-08-13.** |
| **PSX** | **🟡PARTIAL** | 13↑/2↓, +60.4%/90d, margin **60th percentile**. **Residual: 🟡 on BOTH instruments — the one refiner where the two modules agree, and they agree on neutral.** **Re-check 2026-08-13.** |
| **NUE** | **🟡PARTIAL** | 10-K backlog **$3.35bn vs $2.13bn = +57% y/y** naming **data-centre construction**; rs20 vs SPY **+17.50**, OBV +0.611. ⚠ **Residual is MECHANICAL, not fundamental: blocked from 🟢 by `vol_surge` 0.95 alone, and because `velocity` is `None`, raising that ONE axis to 1.2 is sufficient to cross the gate.** **Filed to the missed ledger with exactly that as the entry condition. Re-check 2026-08-20.** |
| **STLD** | **🟡PARTIAL** | Same shape (rs20 +12.50, OBV +0.396, `vol_surge` 0.90). **Residual: EV/EBITDA 15.48 is the richest of the steel pair against a 42.1st-percentile margin — the multiple is ahead of the print.** **Re-check 2026-08-20.** |
| **EMR** | **🟡PARTIAL** | Board's **#3 flow score (+0.911)**, **volume-lit** (1.44), rs20 vs SPY +11.50. ⚠ **Residual, and it is the sector's open question: EMR mentions data centres ZERO times in its primary filings while carrying the node's best flow.** **Re-check 2026-08-14.** |
| **GEV** | **🔴RESOLVED** | Worst flow of 300 (−0.756), OBV −0.264. **DROPPED from the bettable list.** **Ledger row filed** (`A.flow미도착`, revives on flow ≥ 0 **or** current-year breadth turning net-positive, **2026-08-14**) |
| **CAT** | **🔴RESOLVED** | rs20 vs SPY −14.00 on a record backlog. **DROPPED.** **Ledger row filed** (`A.flow미도착`, revives on rs20 > 0, **2026-08-14**) |
| **NEM** | **🔴RESOLVED** | Revisions cut **9-to-1** while price makes a 7-week high; sector 0🟢 of 12. **DROPPED.** **Ledger row filed** (`A.flow미도착`, **2026-08-13**) |
| **CF** | **🔴RESOLVED** | **78.9th-percentile margin** at a 10.4× forward multiple = the L2 trap; the 08-05 double miss. **DROPPED.** **Ledger row filed** (`H.밸류소진`, **2026-08-21**) |
| **VST** | **🔴RESOLVED** | Short-vol **z +1.56** AND revision breadth negative on both years. **DROPPED.** **Ledger row filed** (`C.차트붕괴`, **2026-08-20**) |
| 🚨 **EA** | **🔴RESOLVED — and NOT for a market reason** | **A delisted security still tagged 🟢가속 and still on the live shortlist.** ⚠ **No ledger row is filed**: a rejection ledger scores *judgements*, and there is no judgement here — **this is `D207`/`D215`, a universe-integrity defect. Filing it as a rejection would corrupt the ledger's own statistics.** |

⚠ **Momentum-only flags (RS/volume green, accumulation axis disagreeing) — graded before use (D6):**
**PLTR** (rs20 vs SPY +33.20, `vol_surge` 1.91) and **SHOP** (+21.30, 2.09) are **volume-lit with
positive OBV, so the axes AGREE** ⇒ **no momentum-only stamp is issued.** ⚠ But **PLTR carries an L2
warning of the opposite kind — op margin at the peak of its own 5-quarter history (47.1%) against a
74.8× forward multiple, with RS60 − RS20 = −11.5**, so **the whole 60-day excess is a last-20 event.**
**WAT is the board's only crowded-short (z +2.27)** — **squeeze fuel conditional on a turn, never a
standalone reading** — and it is **not** issued a tag.

## Names carried into ALPHA that received NO tag — written to the missed ledger, not left silent

**PRU · LITE · NUE · LYB**, all filed `--sample prospective` (see §LEDGER above).
★ **NUE appears in BOTH lists deliberately and it is not a contradiction**: it carries a **🟡PARTIAL
tag** (it is tracked) **and** a **missed-ledger row** (it never reached the candidate cut, for a
mechanical reason). **The two ledgers answer different questions, and the line between them was
enforced by the script rather than by memory.**

## ✅ ALPHA exit notes

- **`theme_age` run FIRST, before any live search** — and the run that mattered was the **re-run on
  single tokens**, which is what produced **`D219`**.
- **`--positioning` used on the finalist only** (COHR ±14.8%), **with its expiry checked against the
  event date** — the exact failure the 08-07 run was burned by.
- **Every 🔴 is DROPPED and logged as a ledger row with `--revives-if` and `--recheck-date`**, not as
  prose. **Every 🟡 carries an explicit dated re-check** and is handed to `carryover` — **a 🟡 is an
  appointment, not a shelf.**
- **Tags follow the NAME, not the sector's turn in the rotation.** MPC/VLO/PSX keep their tags although
  ENRG was demoted today; NUE/STLD keep theirs regardless of MATR's next slot.
- **`ACTION_TICKETS.md` written at the day-folder root** with an ALPHA §0 recording that **D155 did NOT
  reproduce** and that **D204's hard-coded cut-cycle reaction function DID.**
- **No sizing and no buy/sell language (P4).**
