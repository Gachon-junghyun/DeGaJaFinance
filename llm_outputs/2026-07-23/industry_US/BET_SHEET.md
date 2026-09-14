# BET_SHEET — industry_US — 2026-07-23

> Stage 8/10. **ONE file, per-sector sections** — downstream desks glob this exact filename, never split it.
> Numbers + business + flow per candidate. **Zero buy/sell recommendation, zero position sizing (P4).**
> Every relative number names its benchmark (**C1**). Flow tags asof **2026-07-22 close** — the US
> 07-23 session was not open at run time (09:1x ET). Fundamentals pulled **2026-07-23**.
> Freshness tags in §B are placeholders filled by the **ALPHA** stage.

**Candidate set construction** = (DEEP-agent thesis leaders) ∪ (LIVE_SHORTLIST names, incl. cross-sector)
∪ (PREMORTEM promotions). DEEP sectors: **ENRG · FIN · HLTH · IT**.

⚠ **Two measurement caveats binding on every number below.**
1. **M25** — the 🟢 tag needs OBV ∧ RS20>0 ∧ `vol_surge`≥1.2, and `velocity` is `None` on all 300 US
   rows, so **68 of 300** names passing OBV+RS20 are blocked by `vol_surge` alone. **🟡 means "not
   volume-surging", not "no flow".** Most of the strongest names on this sheet are 🟡 for that reason.
2. **D6/D2** — RS20/RS60 are **A-grade**; OBV and the 🟢🟡🔴 tag are **C-grade corroborant only**.
   FINRA short-z is a proxy whose **sign was measured to invert** through market-maker hedging — it is
   texture, never directional on its own, and "short building = bearish" is on the **rejected** list.

---

# §ENRG — Energy

**Sector state** (`SECTOR_FLOW_US.json §sector_rotation`, asof 07-22): wflow **+0.283 (#2 of 11)** ·
eqflow +0.118 · breadth 0.06 · 1🟢/0🔴 of 16 · Δ +0.035.
**DEEP verdict**: the sector is **three legs with three different KPIs**, and they gave three
different answers today. `SECTOR_DEEP_ENRG.md` is the authority; the numbers below are the sheet.

## §A · Numbers

| | fwd P/E | trail P/E | PEG | P/B | mean target | upside | CY EPS (Δ90d) | NY EPS (Δ90d) | CQ breadth 30d | CY breadth 30d |
|---|---|---|---|---|---|---|---|---|---|---|
| **XOM** | 14.70 | 26.51 | 1.29 | 2.57 | $167.14 | **+6.0%** | 11.15 (**+10.7%**) | 10.61 (+4.6%) | **0↑:4↓** | 1↑:3↓ |
| **CVX** | 15.56 | 34.40 | 0.79 | 2.12 | $214.13 | **+8.6%** | 14.53 (**+19.7%**) | 12.51 (+6.6%) | **0↑:3↓** | 2↑:3↓ |
| **VLO** | 12.73 | 23.15 | 4.08 | 3.94 | $287.28 | **−9.3%** | 34.61 (**+54.2%**) | 24.22 (+34.6%) | 7↑:5↓ | 9↑:3↓ |
| **MPC** | **10.99** | 21.12 | 1.59 | 5.61 | $298.12 | **−7.1%** | 37.33 (**+70.7%**) | 27.63 (+39.4%) | 5↑:2↓ | 4↑:2↓ |
| **PSX** | 11.72 | 21.21 | 1.23 | 3.02 | $203.89 | **−5.1%** | 20.66 (**+51.0%**) | 18.72 (+24.6%) | 6↑:2↓ | 7↑:1↓ |

★ **Two facts in this table matter more than the multiples.**
1. **All three refiners trade ABOVE their consensus targets** (−9.3% / −7.1% / −5.1% "upside").
   The tape has run past the sell side — while consensus EPS was revised **+51% to +71% over 90 days**
   with positive breadth. **Per lens L2 that is consensus chasing a peaking denominator, not
   cheapness** — the same arithmetic signature the desk already documented on MU. **A low forward
   multiple here is a symptom.** The FY26→FY27 cliff is already on file (M23): VLO **−31.6%** ·
   MPC **−25.8%** · PSX **−7.2%**.
2. **The two integrateds have NEGATIVE current-quarter revision breadth** (XOM 0↑:4↓, CVX 0↑:3↓ over
   30 days) **on the week crude rose 5.2%.** Estimates are being cut into a rising oil price. That is
   a genuine disagreement between the tape and the sell side, and it is not explained on this sheet.

⚠ **R8 re-checked on today's numbers and it HOLDS.** On the forward basis pulled 07-23 the order is
**MPC 10.99 < PSX 11.72 < VLO 12.73**; on the FY26 basis (M23) it was MPC 8.8 < VLO 9.4 < PSX 10.8.
**PSX is not the cheapest on either basis.** The surviving PSX argument remains its **−7.2% FY27
cliff**. ⚠ `core_pick` is **human-locked** and was not modified.

## §B · Thesis + freshness `[ALPHA fills]`

- **XOM** `[freshness: → §ALPHA]` — the sector's **only 🟢가속 and a `new_green` ignition**, RS20 **+8.6 vs SPY**.
  Crude-leg exposure whose KPI (the crude price) is **accelerating**, not deteriorating. ⚠ Its own
  estimate breadth is negative (0↑:4↓).
- **VLO · MPC · PSX** `[freshness: → §ALPHA]` — **refining margin, and the margin moved against them today.**
  ★ **DEEP corrected the desk's own framing** and the correction is carried here, not buried: the C4
  "detachment counter" is **not a continuous streak of 4**. Pulling the actual 07-22 closes,
  VLO/MPC/PSX **fell −1.2% / −1.2% / −0.4%** while crude rose and the crack fell — the equities
  tracked the margin **down**, which is the opposite of detachment. **Corrected count: 3 confirmed
  (07-17, 07-20, 07-21) · 1 broken (07-22) · 1 unconfirmed-intraday (07-23).** Not 4, not 5.
- ★ **DEEP's second finding, which changes what the crack collapse means**: today's move is a
  **gasoline**-crack story, not diesel. The gasoline crack fell **−19.7%** against distillate's
  **−3.6%**, so the distillate-gasoline gap **widened 30.3 → 38.5**. **The Atlantic-basin diesel
  bottleneck — the actual binding constraint in the refining thesis — is intact.** A single 3-2-1
  headline number hid two opposite moves.

## §C · Flow / positioning

| | flow | tag | RS20 vs SPY | RS60 vs SPY | OBV | FINRA short-z (07-22) |
|---|---|---|---|---|---|---|
| XOM | +0.688 | **🟢가속 · new_green** | **+8.6** | −1.0 | accumulating | **+4.46 — the board's extreme** |
| VLO | +0.617 | 🟡 (`vol_surge` 0.91) | **+25.7** | +27.1 | accumulating | +0.67 normal |
| MPC | +0.594 | 🟡 (0.87) | **+25.2** | **+36.2** | accumulating | +0.40 normal |
| PSX | +0.622 | 🟡 (0.92) | **+22.2** | +25.1 | accumulating | +1.03 normal |
| CVX | +0.187 | 🟡 | +7.8 | −0.5 | neutral | — |

**COT context, not a trigger**: WTI **10%ile**, NatGas **6%ile** (Tuesday-close print, unchanged for a
third reading — per **S1** that is **one** observation, not three). Next new print **Fri 2026-07-24**,
which is scenario **S8**'s own registered cross-check. ⚠ COT extremes are on the **rejected** list as a
contrarian trigger and appear here only as cushion attached to an independent reason.

## §D · Competition / peers

Refining peers move as one on the crack and separate on **complexity and geography**: PSX's smaller
FY27 cliff (−7.2%) is a mix statement (midstream + chemicals + marketing), not a valuation statement.
Integrateds (XOM/CVX) and services (SLB RS60 **−19.8 vs SPY**) are **not** substitutes for the refining
leg — the RS60 spread across "Energy" runs **MPC +36.2 to SLB −19.8 = 56pp vs SPY**, wider than the
sector's own move. **W5: "Energy" is the wrong unit of analysis and this sheet says so.**

## §E · Refutation + dated catalyst

- **Kills the refining leg**: the crack keeps compressing **and** the equities stop tracking it —
  i.e. the detachment count reaches **5**. Currently **3 confirmed**.
- **Kills the crude leg**: a Hormuz/"strait open" statement (**S8**, undated `[blank]` — not guessed).
- **Dated**: **WTI COT print Fri 2026-07-24** · **VLO earnings 2026-07-30** · **STNG 2026-07-30** ·
  **UPS 2026-07-28** (the last unread customer).
- ★ **Customer check closed (W4 / dig D23, open for weeks — 4 of 5 now read).** **DAL (07-10) · UAL
  (07-16) · FDX (06-24) · LUV (07-23)**: fuel costs **+66% to +84% YoY** across all four, and **UAL and
  LUV both cut or missed Q3 guidance explicitly citing fuel/crack costs.** Real dollars are moving
  through the crack — which **confirms the margin is economically real** but does **not** settle
  margin-vs-war-premium. **UPS remains unread, prints 07-28.**

---

# §FIN — Financials

**Sector state**: wflow **+0.253 (#3)** · eqflow **+0.320** · breadth 0.15 · 7🟢/3🔴 of 47 · Δ +0.041.

★ **The OW's reason changed today, and DEEP then corrected the desk's reading of the replacement.**
ROTATION restored FIN to OW on "eqflow > wflow = the board's only breadth-led sector." **DEEP measured
it and the gap actually NARROWED** — eqflow−wflow went **+0.145 → +0.067** even as the green count rose
5 → 7. **That is the opposite of concentration masquerading as breadth**, and it is also weaker than
the headline the rotation stage wrote. Both corrections are carried.

## §A · Numbers

| | fwd P/E | trail P/E | PEG | P/B | mean target | upside | CY EPS (Δ90d) | CQ breadth 30d | CY breadth 30d |
|---|---|---|---|---|---|---|---|---|---|
| **GS** | 14.65 | 16.59 | 1.54 | 2.93 | $1,134.40 | +5.6% | 70.78 (**+19.5%**) | **8↑:0↓** | **9↑:0↓** |
| **JPM** | 13.99 | 14.83 | 1.73 | 2.60 | $369.70 | +6.9% | 24.07 (+7.8%) | 5↑:1↓ | 4↑:1↓ |
| **STT** | 12.11 | 16.28 | **0.78** | 2.12 | $198.75 | +7.6% | 13.66 (+10.2%) | **4↑:0↓** | **4↑:0↓** |
| **USB** | 10.92 | 12.61 | 2.13 | 1.62 | $70.07 | **+10.9%** | 5.24 (+3.2%) | 2↑:1↓ | 4↑:1↓ |
| **TRV** | 12.55 | 10.06 | 2.36 | 2.36 | $354.71 | **−5.3%** | 33.97 (+21.1%) | 2↑:1↓ | 2↑:0↓ |
| **CB** | 11.88 | 12.26 | 3.12 | 1.82 | $364.09 | +5.2% | 27.27 (**+1.1%**) | 2↑:1↓ | 2↑:2↓ |
| **V** | 23.50 | 30.42 | 1.56 | 18.75 | $402.66 | **+15.2%** | 13.15 (+2.2%) | **5↑:0↓** | **7↑:0↓** |
| **MA** | 23.05 | 30.41 | 1.65 | 69.39 | $644.24 | **+22.5%** | 19.67 (+0.4%) | **0↑:1↓** | 4↑:0↓ |

★ **GS remains the board's cleanest revision-vs-flow dislocation** — **8↑:0↓ and 9↑:0↓**, CY EPS
**+19.5% over 90 days**, on a **14.65×** forward multiple, against a flow score of **−0.057** and
**RS20 −1.5 vs SPY** (RS60 **+13.8 vs SPY**). The standing read — a **de-rate against an activity
peak**, not credit and not rates — survives: HY OAS is **2.69%**, 6bp off a 365-day low.
★ **V vs MA is the sharpest same-industry pair on this sheet**: identical business, identical 🟢-class
flow, **opposite revision books** (V **5↑:0↓ / 7↑:0↓** vs MA **0↑:1↓ / 4↑:0↓**) and MA carries the
larger nominal upside (+22.5%). **V prints 07-29, MA prints 07-30** — a clean, dated fundamentals-vs-flow test.

## §B · Thesis + freshness `[ALPHA fills]`

- **The steepener leg is dead** `[freshness: → §ALPHA]`. 2s10s went **+0.39 → +0.37 (−2bp)** because the 2y made
  a **120-day high at 4.26%** while the 10y rose only +3bp to 4.63% `[FRED, asof 07-21]`. **Bear-
  flattening is the mechanical opposite of what the super-regional bank leg needs.**
- **Concentration, quantified** `[freshness: → §ALPHA]` — DEEP's C5-declared grouping (banks n=9 · capital
  markets n=5 · payments+insurance n=16 · other n=17): **payments+insurance is 34% of names but 45% of
  gross positive flow, at 2× the sector's cap-weighted mean (+0.518 vs +0.253)**. **Banks are a genuine
  second leg** (clearing the sector average on both counts). **Capital markets nets to ≈zero (+0.005)**
  — SCHW's bid exactly offset by a **four-name de-rate cohort (GS, MS, IBKR, HOOD)**, all sharing the
  positive-RS60 / negative-RS20-vs-SPY shape.
- **C is confirmed uniquely broken among the nine banks** (the only one negative on **both** RS20
  −10.7 and RS60 −1.4 vs SPY) — **but not uniquely broken sector-wide**: APO, PGR, MSCI and BRK-B are
  also double-negative. `STANDING_VIEW`'s claim is upheld **with its scope corrected**.

## §C · Flow / positioning

| | flow | tag | RS20 vs SPY | RS60 vs SPY | FINRA short-z (07-22) |
|---|---|---|---|---|---|
| JPM | +0.503 | **🟢가속** | +2.3 | +8.3 | **+1.89 spike** |
| STT | +0.66 | 🟢 (shortlist) | +4.7 | — | **−1.45 — low-short / covering, the cleanest on the sheet** |
| TRV | +0.933 | 🟢 (sector's top flow) | +15.5 | +18.2 | +1.00 normal |
| USB | +0.69 | 🟢 | +5.5 | — | +0.81 normal |
| CB | +0.685 | 🟢 | +1.5 | — | +0.39 normal |
| V | +0.603 | 🟢 | +5.7 | — | **+2.13 spike** |
| MA | +0.622 | 🟢 | +7.1 | — | −0.03 flat |
| GS | −0.057 | 🟡 | **−1.5** | **+13.8** | +0.86 normal |
| C | −0.672 | **🔴분산** | **−10.7** | −1.4 | — |

⚠ **Short-z is read as texture only** (rule **D2**: the FINRA proxy's sign was measured to invert
through market-maker hedging). Nothing on this sheet is argued from it.

## §D · Competition / peers

Three sub-nodes that do **not** substitute: money-center banks (rate/credit), capital markets
(activity cycle — currently mean-reverting off a record quarter), payments+insurance (consumer volume
+ float income). The sub-node spread inside "Financials" exceeds the sector's own move.

## §E · Refutation + dated catalyst

- **Kills the OW**: **S14** branch B — MA's cross-border volume misses and {MA, V, PYPL} RS20 vs SPY
  flips negative within 5 sessions ⇒ "breadth" was a consumer-spend concentration and **FIN loses its
  second reason in nine days** (the first, the steepener, broke 07-23).
- **The other kill runs the opposite way**: **S9** branch A — real 10y **<2.20% with breakeven rising**
  ⇒ the life/annuity leg (MET, PRU, AFL directly; TRV, CB second-order) loses its driver **at the same
  moment the Utilities/RE underweight reverses**. ★ **DEEP's refinement: the hawkish side is NOT a
  mirror image** — today it is expressed as **bear-flattening**, which hurts the regional steepener
  leg rather than the life insurers or STT. **The two branches hit different names.**
- **Dated**: **V earnings 2026-07-29 (FOMC day itself)** · **MA earnings 2026-07-30** · **FOMC 07-29** ·
  **June PCE 07-30**.
- **Sharpened S14 observable (from DEEP)**: V and MA report on **consecutive days** with **opposite
  revision books** — V's estimates rising **+1.7%/90d** while MA's fall **−1.7%/90d** on an identical
  green tag. That pair, not MA alone, is the cleanest fundamentals-vs-flow test available.

---

# §HLTH — Health Care

**Sector state**: wflow **+0.351 = #1 of 11** · eqflow +0.155 · **breadth 0.19 = best on the board** ·
**6🟢/3🔴 of 32 = most greens** · ⚠ **Δ −0.102 — one of only two negative day-over-day deltas on the
entire board** (Real Estate is the other, and every other sector re-accelerated).

## §A · Numbers

| | fwd P/E | trail P/E | PEG | mean target | upside | CY EPS (Δ90d) | NY EPS (Δ90d) | CQ breadth 30d | CY breadth 30d |
|---|---|---|---|---|---|---|---|---|---|
| **JNJ** | 19.94 | 29.74 | 4.14 | $270.59 | +5.7% | 11.67 (+0.8%) | 12.84 (+1.0%) | 1↑:1↓ | 2↑:0↓ |
| **ABT** | 16.64 | 32.66 | 2.01 | $118.67 | **+17.6%** | 5.51 (+0.5%) | 6.07 (0.0%) | 0↑:1↓ | 0↑:1↓ |
| **ABBV** | 15.66 | 124.37 | 0.42 | $266.89 | +4.7% | 14.13 (**−0.5%**) | 16.28 (+1.3%) | 1↑:1↓ | 2↑:2↓ |
| **LLY** | 26.11 | 41.63 | 1.57 | $1,270.37 | +8.5% | 34.74 (+1.4%) | 44.91 (+6.8%) | 1↑:1↓ | 2↑:1↓ |
| **UNH** | 18.91 | 31.94 | 1.43 | $475.23 | +12.0% | 19.81 (+9.8%) | 22.44 (+10.6%) | **2↑:3↓** | 3↑:2↓ |
| ~~MRK~~ | 13.40 | 36.16 | 11.69 | $134.04 | +3.5% | 2.76 (**−46.0%**) | 9.66 (−0.6%) | **0↑:0↓** | **0↑:0↓** |
| ~~HUM~~ | 24.52 | 41.91 | 2.29 | $347.96 | **−11.5%** | 8.96 (+2.8%) | 16.03 (+6.6%) | 5↑:1↓ | 4↑:0↓ |

★ **The revision books here are flat to negative across the board** — JNJ +0.8%, ABT +0.5%, ABBV
**−0.5%**, LLY +1.4% over 90 days, with breadth clustered around 1↑:1↓. **Compare the refiners
(+51% to +71%) or GS (+19.5%).** ⇒ **This sector's #1 flow rank is NOT being driven by an earnings
upgrade cycle.** UNH is the only genuine upgrade (+9.8% CY, +10.6% NY) and its **current-quarter
breadth is negative (2↑:3↓)** — both halves stated (C2).

## §B · Thesis + freshness `[ALPHA fills]`

- **The disagreement** `[freshness: → §ALPHA]` — money says #1, the desk said underweight for multiple runs.
  **DEEP's verdict is `indistinguishable` (C4)**, and the reason is honest: **six greens on ONE date
  is n≈1, not n=6 (S1)**, the **delta is negative**, and the wflow/eqflow gap (0.196) says the flow is
  **mega-cap-concentrated** — only **3 of 7 sub-nodes** carry it (devices-ex-ABT, distributors and
  facilities are flat-to-negative).
- **The risk-off alternative, weighed rather than dismissed** `[freshness: → §ALPHA]` — VIX **16.64 → 19.13**,
  crude +5.2%, real 10y at a 120-day high all argue "defensive rotation". **But credit does not
  confirm**: HY OAS **2.69%**, 6bp off a 365-day low, and NFCI is loosening a 5th week. **Mixed. Not
  resolved.**
- ★ **The tariff overhang moved from `unknown` to a DATED two-track policy** — DEEP closed it:
  **(i)** branded-drug **100% Section 232** tariff, **effective since April 2026**, with **LLY, PFE and
  Novo Nordisk already exempted** via 3-year MFN pricing deals; **(ii)** a newly announced
  **generic-drug** tariff — **0% until Aug 2026, 100% from Aug 2028, 200% from Aug 2029** — aimed at
  Indian generic makers, i.e. **indirect** read-through to this sector's large-caps.
  **That reframes the 07-22 "up-to-200% pharma tariff" headline entirely**: the 200% is a **2029**
  generics number, not an imminent large-cap hit, and the desk's largest names are **already
  exempted**. ⚠ The 07-23 news absence remains a **C3 unknown** (n=9 articles, 48.4% of clusters
  withheld) — the policy was resolved from **filings and dated policy text**, not from the day's feed.

## §C · Flow / positioning

| | flow | tag | RS20 vs SPY | RS60 vs SPY | OBV | short-z |
|---|---|---|---|---|---|---|
| ABT | +0.850 | 🟢 | +9.2 | +5.7 | accumulating | +0.80 normal |
| JNJ | +0.698 | 🟢 | +5.0 | +7.7 | accumulating | **+2.61 spike** |
| TMO | +0.628 | 🟡 | **+10.3** | +7.4 | accumulating | — |
| ABBV | +0.596 | 🟢 | +6.0 | **+22.8** | accumulating | +0.55 normal |
| MRK | +0.579 | 🟢 | +4.7 | +9.2 | accumulating | — |
| UNH | +0.572 | 🟢 | +3.5 | +16.8 | accumulating | +0.53 normal |
| LLY | +0.504 | 🟢 | +3.2 | **+26.9** | accumulating | — |
| PFE | −0.391 | 🟡 | −1.5 | **−12.8** | distributing | — |
| HUM | — | 🟡 | +8.8 | **+80.0** | accumulating | −0.85 |

## §D · Competition / peers

**W5, and it is decisive here**: pharma / managed care / devices / tools are four different businesses.
**LLY +26.9 against PFE −12.8 RS60 vs SPY is a ~40pp spread inside one label**, and HUM at **+80.0 vs
SPY** sits 93pp above PFE. **The sector label is the wrong unit of analysis.**

## §E · Refutation + dated catalyst

- **Kills the upgrade**: HC's wflow drops out of the top 3, **or** the **negative delta (−0.102)**
  persists 5 sessions ⇒ it was a one-day defensive rotation, not a re-rate. **The negative delta is
  already leaning that way and is stated up front, not discovered later.**
- **Dated**: **HUM + UNH-adjacent managed-care prints 2026-07-29** · generic-tariff step **Aug 2026**.
- ⚠ **A blank that matters**: no health-care thread exists in the 145 alive threads. **Money without
  narrative** — the L2's own warning that you then don't know what you're holding.

---

# §IT — Information Technology  ★ **written as a SPLIT, not a sector**

**Sector state**: wflow **+0.201** vs eqflow **−0.144** — a **0.345 spread, the widest wflow/eqflow
divergence of any sector** — on **4🟢/22🔴 of 56**, breadth 0.07, and the **largest delta on the board
(+0.319)**. A reader looking at wflow or delta alone would call IT the improving sector. **Breadth says
the opposite.** `SECTOR_DEEP_IT.md` is the authority; there is deliberately **no single IT verdict**.

## Leg 1 — SPENDERS

**Deserve MORE underweight, on multiple compression rather than weak demand.** GOOGL already ran the
experiment: capex raised to **$195–205B** (S1 **FIRED-A**) and **the stock fell**. MSFT's **RS60 is
already −12.8 vs SPY** going into its **07-29** print, and it is 🟢가속·new_green on RS20 +2.5 vs SPY —
the two windows disagree. ⚠ **GICS boundary stated**: MSFT and AAPL are Info Tech; **META and GOOGL are
Communication Services** — the "spender" leg crosses two GICS sectors and any sector-level tilt
therefore cannot express it cleanly. **S13** is the registered cross-condition test (07-29).

## Leg 2 — SUPPLIERS (semicap + memory/storage)

**Deserve LESS underweight.** All nine names carry the same signature: **negative RS20, positive RS60
vs SPY** = a pullback inside an uptrend. **Per D6 their 🔴 tags (C-grade) cannot override that A-grade
signal**, so the reds are **not admissible** as evidence the equipment leg is broken.

| | fwd P/E | PEG | mean target | upside | CY EPS (Δ90d) | NY EPS (Δ90d) | CQ breadth 30d | flow / tag | RS20 / RS60 vs SPY | short-z |
|---|---|---|---|---|---|---|---|---|---|---|
| **AMAT** | 33.90 | 1.43 | $623.06 | +9.1% | 12.26 (+10.8%) | 16.75 (**+19.0%**) | **25↑:0↓** | −0.268 🔴 | **−7.3 / +28.1** | **+1.84 spike** |
| **LRCX** | 39.76 | 1.86 | $368.26 | **+14.1%** | 5.68 (+6.4%) | 8.10 (+12.8%) | 1↑:0↓ | −0.308 🔴 | **−15.9 / +14.5** | +1.03 |
| **KLAC** | 42.29 | 2.24 | $234.04 | +7.8% | 3.70 (+1.2%) | 5.13 (+6.4%) | 3↑:1↓ | −0.308 🔴 | **−14.1 / +6.3** | −0.15 |
| **MU** | **6.46** | **0.14** | $1,507.38 | **+51.7%** | 73.44 (+27.0%) | 153.74 (**+52.9%**) | **25↑:0↓** | −0.309 🔴 | **−10.7 / +88.5** | **+1.62 spike** |

★ **MU is the peak-margin trap at maximum amplitude, and the sheet says so next to the multiple**
(lens **L2**, mandatory): gross margin **84.6% = 100th percentile of a 17-year SEC series**, **+25.7pp
above the FY2018 peak of 58.9%**, median **32.0%**, with **two negative-margin years inside 17**
(FY2009 −9.2%, FY2023 −9.1%). The **6.46× forward P/E and 0.14 PEG are the arithmetic signature of a
peaking denominator**, not cheapness — confirmed by **+52.9% NY EPS revision over 90 days on
29↑:0↓**. **A first downgrade in a 29:0 name is a bigger event than the multiple.**
★ **The price-cycle rate series (lens L1)**, which is what actually matters: server DRAM contract
prices **+90~95% → +58~63% → +13~18% QoQ**. **Two consecutive declines in the RATE.** New capacity:
SK M15X + Micron Idaho **mid-2027**, Samsung P5 **2028** — the *level* stays tight, and the level is
the distraction. ⚠ Open contradiction **C1** (LTA price floors cap the upside *and* floor the
downside) is **unmeasured and carried, not resolved.**

★ **AMAT / LRCX / KLAC now have written thesis lines** — they had **four reports each and none**
(HANDOVER §7 named this as the run's coverage gap, and DEEP closed it). AMAT's **25↑:0↓** current-
quarter breadth with **+19.0% NY EPS over 90 days** is the strongest revision book in the trio.

## Leg 3 — SECURITY / OBSERVABILITY

| | fwd P/E | PEG | mean target | upside | CY EPS (Δ90d) | NY EPS (Δ90d) | CQ breadth 30d | flow / tag | RS20 / RS60 vs SPY |
|---|---|---|---|---|---|---|---|---|---|
| **DDOG** | 85.72 | 1.59 | $264.99 | +7.2% | 2.42 (**+12.1%**) | 2.88 (+9.6%) | **37↑:0↓** | +0.500 🟡 (surge 0.70) | **+9.5 / +85.1** |
| **PANW** | 78.26 | 3.79 | $333.50 | +3.3% | 3.77 (+2.2%) | 1.95 (**−15.1%**) | **40↑:1↓** | +0.539 🟡 (0.77) | **+13.4 / +83.1** |
| **FTNT** | 44.38 | 3.57 | $127.38 | **−16.3%** | 3.16 (+6.0%) | 3.43 (+3.6%) | **38↑:0↓** | −0.035 🟡 (0.78) | **+2.9 / +79.2** |
| ~~CRWD~~ | 117.51 | 6.22 | $190.85 | +4.0% | 1.23 (+1.5%) | 1.56 (+1.3%) | **29↑:11↓** | +0.428 🟡 (0.68) | +8.8 / +63.5 |

★ **All four are 🟡 for one reason and it is not flow** — `vol_surge` 0.68–0.78 against a 1.2 gate
(M25). Three of four are OBV-accumulating and **all four are A-grade positive on both RS windows vs
SPY**. **A blanket IT underweight arithmetically shorts the four cleanest live instances of the desk's
only A-grade verified signal.**
⚠ **PANW's far-book decay is real and now quantified**: current-quarter **40↑:1↓** against **next-year
EPS −15.1% over 90 days**. `STANDING_VIEW` flagged this as a **suspected vendor artifact** and it is
**still unresolved** — carried, not laundered.
⚠ **FTNT trades 16.3% BELOW-target-inverted — i.e. above the mean target** on the cleanest revision
book on the entire board (38↑:0↓ / 39↑:0↓). Both halves stated.
⚠ **Open contradiction C5 is CARRIED, NOT RESOLVED**: the strongest *measured* momentum meets the
weakest *measured* valuation discipline, and **this repo has never measured a valuation factor**.
Gating on the multiple would let an unmeasured axis veto a measured one; declaring "momentum wins"
ignores that PLAY23 — the experiment that would settle it — **has never produced a result** (dig D15).

## Compute — a separate boat, and the numbers say why

NVDA **RS60 −2.9 vs SPY**, AVGO **−10.8 vs SPY**, both 🟡; AMD **+54.1 vs SPY** with FY27 EPS still
climbing *this week* (12.96 → 13.10 → 13.31 → 13.46 across 60→30→7→0 days). Against the memory chain's
**+88.5 (MU)**. **Do not fold compute into a memory verdict** — `STANDING_VIEW`'s standing instruction,
re-confirmed on today's numbers.

## Tonight's test — INTC, 2026-07-23 AMC (S6)

**Frozen observable UNCHANGED**: an externally **named** 18A/foundry customer, **or** capex/utilisation
guided up. ⚠ **Magnitude annotation only**: S6 registered **±4.4% at a D0 expiry** and called it
*"a FLOOR, not a fair estimate"*; a fresh pull gives **±12.7% (expiry 07-24, D1, covers the event)** —
**2.9× the registered figure. The floor caveat is measured to have been correct.**
★ **DEEP found, reported, and correctly declined to use**: **Fortinet was named Intel's first foundry
customer (07-21/22) — but on Intel 4, a mature node, not 18A.** That is a genuine **Leg 2 ↔ Leg 3**
link and it **does not satisfy S6's frozen observable.** Recorded rather than stretched.

## Dispersion (W5)

**MU +88.5 vs AVGO −10.8 RS60 vs SPY = a 99.3pp spread inside one GICS label** — wider than the
sector's own day-move (Δ +0.319, the largest on the board). **"Information Technology" is the wrong
unit of analysis, and this sheet does not issue a sector verdict.**

---

# §X — Cross-sector LIVE_SHORTLIST names (included or explicitly dropped)

The 15-name shortlist is `US_LIVE_SHORTLIST.json`. Six are Financials and three Health Care (covered
above). The remaining six:

| Ticker | Sector | flow · RS20 vs SPY · short-z | Disposition |
|---|---|---|---|
| **AAPL** | IT | +0.721 🟢 new_green · +8.8 · −0.43 | **Included** — the only mega-cap 🟢 with **positive RS60 (+15.5 vs SPY)** as well as RS20. It sits in neither the spender nor the supplier leg (no hyperscaler capex line), so it is carried as its own row rather than forced into the IT split |
| **META** | Comm Svc | +0.650 🟢 new_green · +9.7 · +0.19 | **Included by reference** — bracketed as **S16** (is COMM N− a sector verdict or a misapplied single-name one?) and its capex line is inside **S13**. Not re-argued here |
| **CTAS** | Industrials | +0.82 🟢 · +17.4 · **+1.78 crowded-short** | **Dropped from the sheet** — Industrials is **N** after ROTATION, and CTAS is a uniform-services name with no link to the primes backlog thesis or to any DEEP sector. ⚠ Dropped for **scope**, not on a measured refutation, so **no ledger entry is filed** |
| **CSX** | Industrials | +0.71 🟢 · +6.3 · **−2.08 = the cleanest low-short/covering read on the board** | **Dropped from the sheet, flagged as the best un-owned read in the shortlist** — a rail with clean short structure and positive RS20 vs SPY, in a sector at N. Same scope reason; **no ledger entry** |
| **PM** | Staples | +0.79 🟢 · +6.9 · +0.47 | **Dropped** — Staples is N, and PM's own revision breadth is **0↑:5↓ over 30 days** (Lens 1 measured it). Next print **2026-10-21**, i.e. no catalyst in any reasonable window |
| **JNJ · ABT · ABBV · USB · CB · STT · MA · V · TRV** | — | — | Already in §HLTH / §FIN above |

---

# §Z — Set-aside names → `reject_ledger` (dig D27 closed this run)

★ **This desk had entered ZERO rejections in the ledger's entire history — all 25 prior rows were KR.**
Every US run drops ~296 of 300 swept names and 7 of 11 sectors and logged none of it, so no US reason
class had any score. **Four US rows were filed this run**, each with the mandatory `--revives-if` and
`--recheck-date` (script-enforced since 2026-07-23; no bypass exists):

| Ticker | Class | Measured reason | Revives if | Recheck |
|---|---|---|---|---|
| **STNG** | `A.flow미도착` | The Bab el-Mandeb thread is BUILDING (11→9→9→12 outlets, theme-age **108.86×**) while **RS20 −0.7 / RS60 −5.0 vs SPY** — the literal beneficiary is not being bought | RS20 vs SPY turns positive and holds **3 consecutive sessions** while the thread stays ≥8 outlets | **2026-08-06** |
| **MRK** | `B.모멘텀only` | One of HLTH's six greens (flow +0.579, RS20 +4.7 / RS60 +9.2 vs SPY) but **current-year consensus EPS fell −46.0% over 90 days on 0↑:0↓ breadth** — flow without a denominator | CY revision breadth turns positive (≥2↑:0↓ over 30d), **or** the CY estimate stops falling for two consecutive weekly pulls | **2026-08-13** |
| **HUM** | `H.밸류소진` | **RS60 +80.0 vs SPY (5th of 300)** but price is **11.5% above** the mean target and **next-quarter consensus EPS flipped to −0.14 from +0.50 (−128.2%)** — consensus models a loss the price has not taken | The **07-29** print beats **and** next-quarter guidance returns to positive EPS, **or** price closes back below the mean target | **2026-07-31** |
| **CRWD** | `B.모멘텀only` | Weakest **measured** revision book of the four security names — **29↑:11↓** vs 37–40↑:0–1↓ at DDOG/PANW/FTNT. ★ Filed on that measured axis and **explicitly NOT on the 117× multiple**: rule **C5** forbids an unmeasured valuation axis vetoing a measured momentum one | Current-quarter breadth reaches ≥3:1 up over 30d, i.e. it stops being the cohort laggard | **2026-09-03** |

⚠ **No name was removed on narrative grounds while its measured flow still passed.** CTAS, CSX and PM
were dropped for **scope** (their sectors are not DEEP targets), which is not a rejection — **no ledger
row was filed for them**, and CSX is named above as the best un-owned read in the shortlist so it is
visible rather than buried. **EVENT_ALPHA Card 6 (civil nuclear) was RE-FILED, not rejected**, under a
new thesis line (*"the deal's beneficiary may not be listed in the US"*) with a dated re-check —
per the rule that a story going quiet while money still passes is a thesis rewrite, not a drop.

⚠ **Ledger state after this run**: 29 rows total, **22 legacy rows without a revival condition**
(all KR, owned by `industry_kr`), **4 new US rows all fully conditioned**. The measured base rate this
practice is fighting: **67% of rejections changed nothing**, and the loss tail ran **2.2× the gain
tail (+83.8pp vs −38.4pp)** — almost all of it from two condition-less rows on one name.

---

## EXIT CHECK

- [x] Every DEEP sector has a section (§ENRG · §FIN · §HLTH · §IT); cross-sector LIVE shortlist names
      are **included or explicitly dropped with a reason** (§X).
- [x] Numbers are pulled, not guessed; blanks left blank (RS60 absent for shortlist-only names is shown
      as `—`, not filled). Derived figures (crack, spreads, percentiles) carry their source stage.
- [x] Flow/positioning cross-read present per candidate; **one file**, `BET_SHEET.md`.
- [x] **Four set-aside names filed with a class AND a `--revives-if` AND a `--recheck-date`** — the
      first US rows the ledger has ever held (D27).
- [x] **No name removed on narrative grounds alone while its measured flow passed** — Card 6 re-filed,
      CTAS/CSX/PM dropped for scope with no ledger row.
- [x] Linter run on this file (see run log).
- [x] No position sizing, no buy/sell recommendation anywhere.

---

# §ALPHA — freshness gate (Stage 9/10)

> Separates "interesting" from "bettable NOW". Deterministic `theme-age` FIRST, then the tape.
> **🟢LIVE · 🟡PARTIAL (residual + a DATED re-check) · 🔴RESOLVED (dropped AND filed in the ledger).**
> ⚠ **A 🟡 is a dated appointment, not a shelf** — measured origin: 006360 carried an ALPHA tag with
> +64.4% consensus upside, its sector rested, nothing tracked it, and it ran **+12.3% over the next
> five sessions, unowned.**

## Theme novelty (deterministic, token-0, `--scope foreign`)

| Theme | Verdict | Age (d) | 7d avg | Accel | n |
|---|---|---|---|---|---|
| Bab el-Mandeb | 🟡ACCELERATING | 73 | 18.1 | **108.86×** | 148 |
| pharma tariff | 🟡ACCELERATING | 31 | 1.1 | 34.29× | **9 — no power (C4/S3)** |
| crack spread | 🟡ACCELERATING | 77 | 4.4 | 22.14× | 42 |
| bank credit | 🟡ACCELERATING | 57 | 3.4 | 14.69× | 42 |
| refining margin | 🟡ACCELERATING | 55 | 3.4 | 11.43× | 36 |
| AI security | 🟡ACCELERATING | 78 | 7.6 | 4.54× | 175 |
| hyperscaler capex | 🟡ACCELERATING | 57 | 6.4 | 4.19× | 178 |
| observability | 🟡ACCELERATING | ≥90 | 108.9 | 2.12× | 4,196 |
| defense backlog | 🟢FRESH | **3** | 0.4 | — | **3 — no power (C4/S3)** |

★ **Not one theme on this board is ⚪ECHO or 🔴FADING, and not one is 🟢FRESH with power.** Every
bettable theme is a **re-ignited old theme**, which is the 🟡 zone — it needs *stronger* live evidence
than a golden-zone 🟢FRESH would. **The two highest-acceleration readings are both n ≤ 9** and are
quoted with their denominators so they cannot be mistaken for signal.

## Tags

| Name | Tag | Evidence label + date | Residual / why | **Re-check date** |
|---|---|---|---|---|
| **XOM** | **🟢LIVE** | Only 🟢가속 + `new_green` in Energy; RS20 **+8.6 vs SPY**; crude KPI **accelerating** (WTI +5.2% on 07-23) | ⚠ own CQ revision breadth **0↑:4↓**; short-z **+4.46 = the board's extreme → hard-stop stamp** | 2026-07-24 (COT) |
| **VLO · MPC · PSX** | **🟡PARTIAL** | RS20 **+22 to +26 vs SPY** (A-grade), OBV agreeing; 🟡 is a `vol_surge` artifact (0.87–0.92), **not** weak flow | **Residual: the margin KPI moved against them.** Crack **−11.2%** on 07-23 — but **gasoline-led (−19.7%) not diesel (−3.6%)**, so the diesel bottleneck is intact. All three trade **above** consensus target on **+51–71%/90d** revisions = peak-denominator | **2026-07-24** (WTI COT, S8's own KPI) **and 2026-07-30** (VLO print) |
| **GS** | **🟢LIVE** | **8↑:0↓ / 9↑:0↓**, CY EPS **+19.5%/90d** — the board's best revision book — against flow −0.057 and **RS20 −1.5 vs SPY**; HY OAS 2.69% says it is not credit | ⚠ **Momentum-only flag INVERTED**: here the *fundamental* axis leads and the *tape* disagrees. That is a dislocation, not a tape trade | 2026-07-29 (FOMC) |
| **STT** | **🟢LIVE** | **4↑:0↓** both periods, PEG 0.78, short-z **−1.45 = low-short/covering**, the cleanest structure on the sheet | — | 2026-08-06 |
| **DDOG** | **🟢LIVE** | **37↑:0↓ / 36↑:0↓** revision breadth; RS20 **+9.5** / RS60 **+85.1 vs SPY**; OBV accumulating. 🟡 tag is `vol_surge` 0.70 (M25) | ⚠ carries open contradiction **C5** — strongest measured momentum × an unmeasured valuation axis (fwd 85.7×). **C5 is carried, not resolved** | 2026-08-06 (print) |
| **AAPL** | **🟢LIVE** | 🟢가속 · `new_green`, the only mega-cap positive on **both** RS20 **+8.8** and RS60 **+15.5 vs SPY**; short-z −0.43 | Belongs to neither the spender nor the supplier leg | 2026-08-06 |
| **AMAT** | 🟡PARTIAL | **25↑:0↓** CQ, NY EPS **+19.0%/90d**; **RS60 +28.1 vs SPY** — the strongest supplier book | **Residual: RS20 −7.3 vs SPY. Tonight's INTC print (S6) is the registered test.** ⚠ short-z +1.84 spike | **2026-07-24** |
| **LRCX · KLAC** | 🟡PARTIAL | RS60 **+14.5 / +6.3 vs SPY**, positive NY revisions | Same residual; **RS20 −15.9 / −14.1 vs SPY** | **2026-07-24** |
| **MU** | 🟡PARTIAL | RS60 **+88.5 vs SPY** — highest supplier read on the board | **Residual is the whole standing thesis**: GM **84.6% = 100th pct of 17y**, DRAM contract QoQ **+90~95 → +58~63 → +13~18%** (two consecutive rate declines). **A first downgrade in the 29↑:0↓ book is the trigger, not the 6.46× multiple.** short-z +1.62 | **~2026-09** (FQ4 print, S4) |
| **PANW** | 🟡PARTIAL | CQ **40↑:1↓**, RS60 **+83.1 vs SPY** | **Residual: NY EPS −15.1%/90d** — the far-book decay `STANDING_VIEW` flagged as a **suspected vendor artifact, still unresolved** | 2026-08-19 (print) |
| **FTNT** | 🟡PARTIAL | **38↑:0↓ / 39↑:0↓** — the cleanest revision book on the entire board; RS60 **+79.2 vs SPY** | **Residual: price is 16.3% ABOVE the mean target.** ★ Also: named Intel's first foundry customer (07-21/22) but on **Intel 4, not 18A** — a real Leg2↔Leg3 link that does **not** satisfy S6 | **2026-07-30** (print) |
| **MSFT** | 🟡PARTIAL | 🟢가속 · `new_green`, RS20 +2.5 vs SPY | **Residual: RS60 −12.8 vs SPY — the two windows disagree.** S13 is the test | **2026-07-29** |
| **META** | 🟡PARTIAL | 🟢가속 · `new_green`, RS20 **+9.7 vs SPY**, fwd 16.5 / PEG 0.94, FY breadth 3↑:0↓ | **Residual: RS60 −11.8 vs SPY — a 20-day inflection, not a trend (C4).** S16 is the test | **2026-07-29** |
| **JPM** | 🟡PARTIAL | Financials' only 🟢가속, RS20 +2.3 / RS60 +8.3 vs SPY | Residual: the steepener leg died 07-23; short-z **+1.89 spike → hard-stop stamp** | 2026-07-29 (FOMC) |
| **V** | 🟡PARTIAL | **5↑:0↓ / 7↑:0↓**, +15.2% to target | ⚡ **short-z +2.13 = crowded-short → turn-conditional squeeze fuel, NEVER a standalone reason. Hard-stop stamp.** Prints on FOMC day | **2026-07-29** |
| **MA** | 🟡PARTIAL | +22.5% to target, CY breadth 4↑:0↓ | **Residual: CQ breadth 0↑:1↓, and its estimates fall while V's rise** — the S14 pair test | **2026-07-30** |
| **USB · CB · TRV** | 🟡PARTIAL | 🟢 flow; TRV is the sector's top flow (+0.933, RS20 +15.5 vs SPY) | **Residual: S9 cuts BOTH ways** — the dovish branch (real 10y <2.20% with breakeven rising) hits the life/annuity leg directly and TRV/CB second-order; the hawkish branch arrives as **bear-flattening** and hits the *regional* leg instead. **Different names lose on each branch** | **2026-07-29** |
| **ABT · JNJ · ABBV · LLY · UNH** | 🟡PARTIAL | Sector wflow **#1 of 11**, best breadth 0.19, six 🟢 all OBV-accumulating and positive on both RS windows vs SPY | **Residual, stated up front: Δ −0.102 (one of only two negative deltas on the board), revision books flat (+0.5% to +1.4%/90d), and NO health-care thread exists in the 145 alive threads — money without narrative.** ⚠ JNJ short-z **+2.61 spike → hard-stop stamp**. UNH CQ breadth **2↑:3↓** | **2026-08-06** |
| ~~**MRK**~~ | **🔴RESOLVED — DROPPED** | CY EPS **−46.0%/90d** on **0↑:0↓** breadth while tagged 🟢 | Flow without a denominator | ledger `B.모멘텀only`, revives-if set, **2026-08-13** |
| ~~**HUM**~~ | **🔴RESOLVED — DROPPED** | RS60 **+80.0 vs SPY** but **11.5% above** target, and next-quarter EPS flipped to **−0.14 from +0.50 (−128.2%)** | Consensus models a loss the price has not taken | ledger `H.밸류소진`, revives-if set, **2026-07-31** |
| ~~**CRWD**~~ | **🔴RESOLVED — DROPPED** | CQ **29↑:11↓** vs 37–40↑:0–1↓ at the three cohort peers | ★ Dropped on the **measured** revision axis, **explicitly not on the 117× multiple** (C5) | ledger `B.모멘텀only`, revives-if set, **2026-09-03** |
| ~~**STNG**~~ | **🔴RESOLVED — DROPPED** | Thread BUILDING at **108.86×** acceleration; **RS20 −0.7 / RS60 −5.0 vs SPY** | The literal blockade beneficiary is not being bought | ledger `A.flow미도착`, revives-if set, **2026-08-06** |

## Momentum-only / positioning stamps

- **Hard-stop stamp (crowded-short = turn-conditional, never a standalone reason)**: **XOM (+4.46)** ·
  **JNJ (+2.61)** · **V (+2.13)** · **JPM (+1.89)** · **AMAT (+1.84)** · **MU (+1.62)**.
  ⚠ Read as **texture only** — rule **D2**: the FINRA proxy's sign was measured to **invert** through
  market-maker hedging, and "short building = bearish" is on the **rejected** list.
- **C-grade disagreements → 🟡, reported as disagreements, never converted into a verdict**: the whole
  semicap block (AMAT/LRCX/KLAC/MU/INTC) is 🔴 on the **C-grade** OBV tag while **positive on the
  A-grade RS60 vs SPY**. Per **D6** the C-grade tag **downgrades to 🟡 and is reported**; it does not
  make these tape trades, and it is **not** admissible as evidence that the equipment leg is broken.
- **No name on this sheet is momentum-only in the classic sense** (RS green, accumulation red) — every
  🟢LIVE row has OBV agreeing. The one genuine axis-disagreement runs the **other** way: **GS**, where
  the fundamental book (8↑:0↓) leads and the tape (−0.057, RS20 −1.5 vs SPY) lags.

## ★ Carry-forward list — tracked next run REGARDLESS of which sectors hold DEEP slots

`XOM · VLO · MPC · PSX · GS · STT · JPM · V · MA · USB · CB · TRV · ABT · JNJ · ABBV · LLY · UNH ·
AMAT · LRCX · KLAC · MU · DDOG · PANW · FTNT · MSFT · META · AAPL` — **27 names**, plus the four
🔴 ledger rows whose `--revives-if` conditions HANDOVER's `reject_ledger.py due` will re-examine
without anyone having to remember them.
**Nearest appointments: 2026-07-24** (WTI COT + the INTC read-through) · **2026-07-29** (FOMC, MSFT,
META, V) · **2026-07-30** (June PCE, MA, VLO, FTNT, STNG).

## EXIT CHECK — ALPHA

- [x] Every §B tag filled with an evidence label and a date; **four 🔴 dropped AND filed as ledger rows**
      with a reason class, a `--revives-if` and a `--recheck-date` (script-enforced, no bypass).
- [x] **Every 🟡PARTIAL carries an explicit re-check date**; the 27-name carry-forward list is written
      out **independently of next run's DEEP rotation** (the 006360 lesson).
- [x] Momentum-only and positioning stamps applied — including the one inverted case (GS).
- [x] `ACTION_TICKETS.md` written by `action_bracket.py`, **with an appended correction block** (D19).
- [x] No sizing language beyond the script's own DRY-RUN illustration; no buy/sell recommendation.
