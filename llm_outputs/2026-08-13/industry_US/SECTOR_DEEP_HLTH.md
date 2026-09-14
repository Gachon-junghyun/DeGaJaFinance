# SECTOR DEEP — HEALTH CARE (HLTH) · 2026-08-13
### TRACK = ROTATING · **promoted by PREMORTEM as the 5th DEEP** (protocol budget N=4; a pre-mortem-promoted 5th is permitted) ⇒ **FULL FRESH MAP**

**Benchmark declared for the whole file: `SPY`.** Every excess/relative figure below is measured
against `SPY` unless another benchmark is named in the same line.
**All prices are SETTLED closes to 2026-08-12.** No 2026-08-13 bar is used anywhere.
**Analytical only. ZERO buy/sell. No sizing (P4).**

**Data provenance.** yfinance `auto_adjust=False`, 550 settled rows 2024-06 → 2026-08-12, last bar
verified `2026-08-12`. Sweep figures re-read from `llm_outputs/2026-08-13/industry_US/SECTOR_FLOW_US.json`
(`asof 2026-08-12`). FINRA from `scripts/us_flow.py` (date stamp `2026-08-12` on every row).
**PREFLIGHT G1 honoured**: the sweep's news-velocity column is NOT cited anywhere in this file; every
news claim below quotes my own `fts search` / `chain-hop` call with its output.

---

## §0 — THE ASSIGNED QUESTION, ANSWERED FIRST

> **Is Health Care an idiosyncratic med-tech / life-science-tools leg, or the FOURTH LEG of the
> duration complex this desk is UNDERWEIGHT on three legs of?**

### VERDICT: **Neither lens as written. `XLV`-the-index IS a duration proxy; the HLTH leg that is
### actually moving is NOT. Lens 2's correlation is correct, replicates to the third decimal, and
### does not support the conclusion Lens 2 drew from it.**

I accept Lens 2's evidentiary prohibition in full and argue **without** the forbidden number. `XLV`
exc60 is not cited as evidence for the N+ anywhere in this file. The case is made from a quantity
that is **orthogonal to the duration factor by construction** — the regression residual.

**Three measurements carry it.**

**(1) The correlation is real, and it is a CAP-WEIGHT artifact of mega-pharma.**
Replication first — Lens 2 said 0.67 (252d) / 0.81 (60d) vs EW{`XLU`,`XLRE`,`XLP`}, and 0.48/0.64 vs
`TLT`. I measure **0.669 / 0.809** and **0.480 / 0.638**. Lens 2's arithmetic is sound; nothing here
disputes it. But decomposing the same regression by sub-node breaks it apart:

| basket (excess vs `SPY`) | corr w/ EW-DUR 60d | 252d | beta 60d | corr w/ `TLT` 60d |
|---|---|---|---|---|
| MEGA-PHARMA (JNJ MRK PFE BMY LLY ABBV AMGN GILD) | **0.785** | **0.646** | 0.990 | 0.609 |
| DEVICES (ABT BDX MDT SYK BSX ISRG) | 0.678 | 0.546 | 1.031 | 0.415 |
| MANAGED CARE (UNH CI ELV HCA) | 0.663 | 0.455 | 0.858 | 0.433 |
| BIOTECH (VRTX REGN MRNA BIIB INCY) | 0.419 | 0.268 | 0.605 | 0.436 |
| **TOOLS (TMO DHR A WAT MTD)** | **0.346** | **0.196** | 0.483 | 0.396 |
| `XBI` (biotech ETF) | **0.096** | **0.046** | 0.124 | 0.248 |
| `XLV` (the index) | 0.809 | 0.669 | 0.927 | 0.638 |

`XLV` sits at the **top** of its own constituent range, above every sub-basket inside it. An index
cannot be more factor-loaded than all its parts unless the loading is concentrated in its heaviest
weights — and the sweep confirms the weight: `top1 = LLY at 19.4%` of sector cap. **The duration
signature lives in mega-pharma. Tools carry a quarter of it; `XBI` carries none.**

**(2) Correlation of daily excess is not shared drift — and the drift runs the OPPOSITE way.**
Over the identical 60 settled sessions, **every member of the duration complex is NEGATIVE against
`SPY`**: `XLU` **−4.21pp**, `XLRE` **−0.96pp**, `XLP` **−3.56pp**, `TLT` **−5.48pp**, `IEF`
**−4.36pp**, `LQD` **−5.24pp**. Health care is positive over the same window. **A fourth leg of a
complex does not beat the other three by ~15pp in 60 sessions.**

Made precise by regressing each excess series on EW-DUR excess and cumulating the residual:

| series | window | beta to DUR | cumulative excess vs `SPY` | **cumulative RESIDUAL alpha (orthogonal to DUR)** |
|---|---|---|---|---|
| **TOOLS basket** | 60d | 0.483 | +26.86pp | **+26.24pp** |
| DEVICES basket | 60d | 1.031 | +8.71pp | +12.48pp |
| MEGA-PHARMA | 60d | 0.990 | +10.32pp | +13.44pp |
| `XBI` | 60d | 0.124 | +16.39pp | +16.49pp |
| `XLV` | 60d | 0.927 | (not cited — Lens 2 prohibition) | +13.41pp |

The duration factor's contribution to health care over 60 sessions is **negative**. The move is
residual. **The TOOLS basket's +26.24pp of 60-day residual alpha is, by construction, the part of the
return the duration factor cannot explain** — that, not any `XLV` tape figure, is the admissible
evidence for a distinct leg.

**(3) There is no shared MECHANISM, and that is checkable from a filing.** What makes `XLU`/`XLRE`/
`XLP` bond-like is contracted or regulated cash flow with low real volume growth — a regulated return
base, a lease, a staples annuity. Tools and devices have the opposite cash-flow shape: **`TMO` +10.5%
YoY revenue with +9.0% QoQ sequential; `A` +10.0% YoY with +2.1% QoQ; `ABT` +7.8% YoY with −2.6% QoQ;
`BDX` +5.4% YoY with +5.7% QoQ; `MTD` +4.5% YoY with +8.5% QoQ.** These are volume-growth P&Ls, not
annuities. Correlation without a shared cash-flow driver is a **positioning coincidence**, not factor
membership. (Mechanism check for the mega-pharma node is the opposite and is §5.)

### BUT — the half of Lens 2 that survives, and must be carried

**The coupling is at a 12-month extreme right now.** Rolling 60-day corr(`XLV` excess, EW-DUR excess)
is **0.809 today vs a trailing-252 mean of 0.580, min 0.388, max 0.832 — the 92.9th percentile.**
Tools are worse in relative terms: `TMO`'s 60d duration correlation is **0.410 against a 0.094 mean**,
roughly **4x its own norm**. So the historical decomposition supports Lens 1 while the *current*
loading supports Lens 2's risk. **The leg has been idiosyncratic and is presently trading more
duration-coupled than at almost any point in the past year.** A rates move transmits today at a beta
that the 252d history would not predict. `S82` branch B is live on that channel alone.

### And the unit is wrong (see §9)
Intra-sector exc60 dispersion is **44.15pp** (`MTD` +34.66 to `ISRG` −9.49) against the sector's own
+11.82pp move — **3.7x**. On a 252d window `IHI` is **−25.62pp** while `XBI` is **+53.19pp**, a
78.8pp gap inside one sector label. **"HLTH" is not a decision unit at this dispersion.**

---

## §1 — FULL FRESH CHAIN MAP (7 nodes, left → right)

```
 [1] REAL RATES        [2] PAYER            [3] HOSPITAL & LAB      [4] DEVICE OEM
 discount rate    →    reimbursement   →    CAPITAL BUDGETS    →    order books
 10y real / TLT        + MLR floors         ★★ BINDING ★★           ABT BDX MDT SYK BSX ISRG
                       UNH ELV CI HCA       capex/rev, MEASURED
       │                                          │
       │                                          ▼
       └──────────────→ [5] PHARMA & BIOTECH  →  [6] LIFE-SCIENCE TOOLS  →  [7] EQUITY
                            R&D BUDGETS            TMO DHR A WAT MTD          POSITIONING
                            (funding cost)         ★★ CO-BINDING ★★          OBV · FINRA short
                                                                              · index/factor flow
```

### ★ THE BINDING CONSTRAINT IS NODE 3 (and node 5 for tools). **It is NOT demand.**

Procedure volume, diagnosis rates and installed-base ageing are all *strong* and none of them is a
bottleneck — a bottleneck is the thing that caps throughput when everything upstream is willing.
Here the cap is the **customer's capital budget**, and it is measurably tightening (§7). Node 7 is a
*consequence* node, not a driver — it is where the duration factor of §0 actually enters, via index
and factor allocation, which is exactly why the correlation exists without a cash-flow mechanism.

**Where the desk's three existing UWs sit on this map**: `XLU`/`XLRE`/`XLP` attach at node 1 only.
They share node 1 with health care and share nothing else. That is the structural statement behind
the §0 measurement.

---

## §2 — RATE-OF-CHANGE SERIES ON THE PRICE-CYCLE NODES (QoQ, per requirement 3)

There is no commodity node in this chain. The price-cycle analogue is the **instrument/consumable
replacement cycle** at node 6 and the **capital budget** at node 3. Both are given as QoQ
rate-of-change, with gross-margin change in pp. Fiscal quarters, so QoQ carries seasonality — the
Q1 trough is structural in this sector and is not a signal.

**Node 6 — life-science tools, QoQ revenue and GM (yfinance quarterly statements):**

| name | quarter ends | rev $B | **QoQ %** | YoY % | GM % | GM chg pp |
|---|---|---|---|---|---|---|
| TMO | 2025-09-30 | 11.122 | +2.5 | — | 41.2 | +0.59 |
| TMO | 2025-12-31 | 12.215 | +9.8 | — | 41.0 | −0.18 |
| TMO | 2026-03-31 | 11.005 | −9.9 | — | 40.3 | −0.77 |
| **TMO** | **2026-06-30** | **11.994** | **+9.0** | **+10.5** | 40.7 | +0.45 |
| DHR | 2026-03-31 | 5.951 | −13.0 | — | 60.3 | +2.34 |
| **DHR** | **2026-06-30** | **6.265** | **+5.3** | **+5.5** | 57.6 | **−2.71** |
| A | 2026-01-31 | 1.798 | −3.4 | — | 52.6 | −0.58 |
| **A** | **2026-04-30** | **1.835** | **+2.1** | **+10.0** | 54.0 | +1.34 |
| MTD | 2026-03-31 | 0.947 | −16.2 | — | 58.7 | −1.10 |
| **MTD** | **2026-06-30** | **1.027** | **+8.5** | **+4.5** | 63.3 | **+4.61** |
| WAT | 2025-12-31 | 0.932 | +16.6 | — | 61.1 | +2.06 |
| **WAT** | **2026-03-31** | **1.267** | **+35.9** | **+91.4** | **46.4** | **−14.67** |

⚠⚠ **`WAT` is not organic and must be excluded from any demand read.** +35.9% QoQ / +91.4% YoY with
a **−14.67pp gross-margin step** in one quarter is a combination close, not a demand cycle. Any
citation of `WAT` strength (exc60 +21.63pp vs `SPY`, exc120 +13.16pp vs `SPY`) as evidence of tools
demand is a **category error**, and `WAT` is dropped from the demand inference below. It stays in the
correlation baskets of §0 because a merger does not bias a *factor loading* the way it biases a
growth rate.

**Read:** ex-`WAT`, node 6 sequential is **positive and re-accelerating off the fiscal-Q1 trough**
(TMO −9.9 → +9.0; MTD −16.2 → +8.5; DHR −13.0 → +5.3; A −3.4 → +2.1), but **gross margin is not
confirming**: DHR −2.71pp QoQ, TMO +0.45pp QoQ off a −0.77pp prior quarter. Only MTD (+4.61pp QoQ)
shows margin expanding with volume. **Volume is recovering; price/mix is not, at 3 of 4.**

**Node 3 — hospital capital budgets, QoQ (this is the constraint; series in §7).**

---

## §3 — DISPERSION: DEVICES vs TOOLS vs PHARMA vs BIOTECH vs MANAGED CARE (requirement 9)

Cumulative excess vs `SPY`, settled to 2026-08-12:

| unit | exc5 | exc20 | exc60 | exc120 |
|---|---|---|---|---|
| `IHI` med-devices | +4.04 | **+10.13** | +11.12 | **−18.38** |
| `XBI` biotech | +3.82 | **−0.31** | **+17.30** | **+12.43** |
| `XPH` pharma | −0.65 | +0.38 | +18.18 | +8.34 |
| `IHF` providers | +0.59 | −1.35 | +7.45 | +10.49 |
| `XLV` sector | +2.26 | +4.07 | +11.82 | −5.43 |

**The handed sub-leg claim VERIFIED, and then BROKEN by the window (C5).**
`IHI` exc20 **+10.13** and `XBI` exc20 **−0.31** reproduce the handed figures exactly — on the 20-day
window the leg is devices+tools and biotech is not in it. **On the 60-day window the claim inverts:
`XBI` +17.30 EXCEEDS `IHI` +11.12 and exceeds the sector.** On 252d the two are 78.8pp apart in the
*other* direction (`IHI` −25.62, `XBI` +53.19). ⇒ **"devices+tools, not biotech" is a 20-day
statement and it does not survive a window change.** C5 is not a hypothetical here; it is realised.

**Name-level exc60 range (vs `SPY`)**: `MTD` +34.66 · `TMO` +32.93 · `A` +28.19 · `ABT` +27.46 ·
`BDX` +24.08 · `AMGN` +22.76 · `DHR` +22.59 · `WAT` +21.63 (M&A, §2) … `ZTS` −5.00 · `HCA` −6.57 ·
`CI` −6.97 · `BSX` −7.17 · `ISRG` −9.49.

**Spread 44.15pp vs the sector's own +11.82pp move = 3.7x.**
⇒ **SAY IT PLAINLY: the sector label is the wrong unit.** A sector-level N+ on HLTH prices a
+11.82pp object that no constituent actually is. The measured objects are (a) a tools/instruments
node, (b) a large-cap device node, (c) a bounced-broken-device node with the opposite flow signature
(§6), (d) a managed-care node that is *negative on every window*, and (e) mega-pharma, which is the
duration exposure of §0. These are five different bets wearing one ticker prefix.

---

## §4 — VALUATION, OWN-HISTORY MARGIN POSITION, AND REVISION BREADTH (requirement 4)

Every "cheap on forward multiple" claim below states where margin sits in that name's **own** history
(`scripts/margin_history.py`) **and** its estimate-revision trend (`-m module_fundamentals_us`,
sections 추정치 모멘텀 / 리비전 브레드스). No multiple is quoted without both.

### BDX — the only genuinely cheap name in the leg
- **Forward P/E 13.87** (trailing 31.97, PEG 1.11, P/B 2.06). Price $184.80 vs 52w high $187.35.
- **Own-history margin**: latest quarterly GM **46.5%**. 19-year XBRL history — **median 48.0%, high
  52.6% (FY2009), low 42.2% (FY2023)**, FY2025 45.4%. ⇒ **BDX sits 1.5pp BELOW its own 19-year median
  and 6.1pp below its own high. This is NOT a peak-margin / low-multiple trap.** The cheap multiple
  is not being paid on a cyclical margin peak.
- **Revision trend — and this is the offset**: next-quarter EPS **−4.6% over 90 days** (2.86 → 2.73),
  next-year **−0.9%**, current-quarter **−0.7%**. 30-day breadth: current-Q **0↑/1↓**, FY **1↑/1↓**,
  next-year 2↑/0↓, next-Q 1↑/0↓ — **thin coverage and near-term negative.**
- **Honest read: BDX is cheap on a below-median margin with deteriorating near-quarter estimates.**
  Those two facts point opposite ways and the file does not resolve them.

### ABT — the cleanest fundamental profile in the leg
- Forward P/E **18.50** (trailing 36.31). Beta 0.58.
- **Own-history margin**: latest quarterly GM **56.2%**; 19-year median **56.4%**, high 58.5%
  (FY2019), low 53.2% (FY2011). ⇒ **at its own median — mid-history, not peak.**
- **Revision trend**: FY **+0.6% / 90d** with 30-day breadth **19↑ / 2↓**; next-quarter **+1.1%** with
  breadth **14↑ / 0↓** (30d). ⇒ **positive and broad.** Next-year is flat (−0.0%, 11↑/5↓) — the
  upgrade is near-dated, not structural.

### TMO
- Forward P/E **21.92** (trailing 32.47, PEG 1.96). Not cheap; no cheapness claim is made.
- ⚠ **TOOL DATA GAP, disclosed (C3)**: `scripts/margin_history.py TMO` returns only **FY2007–FY2017**
  (11 years, ending 57.1%). **There is no recent annual XBRL margin series for TMO from this tool**,
  so I cannot place current margin in its own long history. Substituting the yfinance quarterly GM:
  40.6 → 41.2 → 41.0 → 40.3 → **40.7%** — flat within 0.9pp over five quarters. **The 40.7% quarterly
  and the 57.1% FY2017 XBRL figure are different definitions and are NOT compared.** Margin position
  in own history for TMO = **`unknown`**.
- **Revision trend, and it is split**: FY **+1.0% / 90d**, breadth **18↑ / 0↓ (30d)** and next-year
  **16↑ / 2↓** — near-unanimous upgrades. But **next-quarter is −1.1% / 90d with breadth 5↑ / 10↓**.
  ⇒ **the annual is being marked up while the very next print is being marked down.** That is the
  shape of a back-half-weighted guide, and it puts the risk on one date (§10).

---

## §5 — CONTRACT TERMS READ FROM FILINGS (requirement 5)

No "margin must mean-revert" claim is made in this file without a filing behind it, or an explicit
`unknown` mark.

### DEVICES — the GPO / hospital-contracting question · `-m module_disclosure_us BDX`
`BDX` filed a **10-Q on 2026-08-06** (period 2026-06-30). Read from the filing body:

- **Variable consideration, quantified**: *"The Company's gross revenues are subject to a variety of
  deductions… Such variable consideration includes rebates, sales discounts and sales returns. The
  Company's rebate liabilities… were $860 million and $817 million as of June 30, 2026 and
  September 30, 2025."*
  ⇒ **rebate liability +5.3% over three quarters against revenue +5.4% YoY (+5.7% QoQ sequential).
  Rebate intensity is FLAT, not deteriorating** (~3.9% of LTM revenue). This is the measurable GPO/
  distributor channel and it is **not currently compressing margin**. It is also the *reverse* of a
  take-or-pay floor — see §6.
- **Named margin risks, from the filing's own risk language**: *"increased pricing pressure due to the
  impact of low-cost manufacturers, patents attained by competitors (particularly as patents on our
  products expire)"*, and consolidation *"among healthcare companies, distributors and/or payers"*.
- **Live cost headwind, disclosed**: *"Tariffs have adversely impacted our third quarter fiscal year
  2026 operating expense and we continue to monitor international trade pol[icy]"*. ⇒ **an
  acknowledged, already-realised opex hit** — relevant because BDX's GM is already 1.5pp below its own
  19-year median (§4).
- ⚠ **`unknown` (C3)**: the 10-Q does **not** disclose the share of revenue under GPO contracts, nor
  contract tenor, nor repricing dates. **The GPO-covered share of BDX revenue is `unknown` and no
  mean-reversion claim rests on it.**

### PHARMA — the LOE / patent-cliff and IRA-negotiation question
This is the node that IS the duration exposure (§0), so its contract terms matter to the desk's
factor question, not to a tools thesis. **`-m module_disclosure_us TMO/BDX` covers my two deep names;
I did not pull LOE schedules for the eight mega-pharma names, and I will not assert an LOE or
IRA-negotiation position I have not read.** ⇒ **mega-pharma LOE/IRA exposure = `unknown` in this file
(C3).** What *is* measured about that node here is only its factor loading (0.785 / 0.646) and the
`BDX` filing's generic patent-expiry language quoted above. The one policy datum I did verify is in
§8 and it is a **risk** to this node, not a driver.

---

## §6 — FRAME TRANSFER (requirement 6): does a frame the desk trusts elsewhere apply here?

**Frame tested: take-or-pay floors / RPO lock-in / regulated return** — the three contracted-revenue
frames this desk relies on in energy midstream, AI-compute backlog, and utilities respectively.

| frame | applies to HLTH devices/tools? | evidence |
|---|---|---|
| **Take-or-pay floor** | ❌ **Checked, does not apply — and it inverts.** | The `BDX` 10-Q discloses the *opposite* structure: revenue is subject to **deductions** (rebates $860M, discounts, returns), i.e. contracted variable consideration that reduces realised price. There is no minimum-volume floor. A device OEM's contract risk runs down, not up. |
| **RPO / backlog lock-in** | ❌ **Does not apply.** | Instrument sales are point-in-time; the closest analogue is the consumables razor-blade, which is **usage-based, not a contracted minimum** — it converts a customer's *actual* throughput into revenue and provides no floor if throughput falls. **The exact recurring/consumable share is `unknown` (C3)** — neither the TMO nor BDX filing set I pulled reports an RPO figure. |
| **Regulated return** | ❌ **Does not apply to devices/tools; it applies to the node NEXT DOOR.** | MLR floors are a regulated-return frame — but they bind on **payers** (node 2), not on device or tools vendors. |

**★ This is the frame-transfer result that answers §0 structurally.** The regulated-return frame is
precisely what makes `XLU` a bond proxy, and it is the desk's own reason for holding the utilities UW.
**That frame is absent at nodes 4 and 6 and present at node 2.** So the sub-sectors with a
utility-like *mechanism* (payers, and by cash-flow shape mega-pharma) are the ones that measure as
duration-correlated (managed care 0.663/0.455; mega-pharma 0.785/0.646), and the ones without it
measure as uncorrelated (tools 0.346/0.196; `XBI` 0.096/0.046). **The mechanism and the correlation
agree. That agreement is the strongest single argument that the tools/devices leg is not the fourth
leg of the duration complex.**

---

## §7 — THE NODE'S CUSTOMERS (requirement 7), AND THE BINDING CONSTRAINT MEASURED

Node 4 and node 6 sell to three customers: **hospital systems**, **payers**, and **pharma/biotech R&D
budgets**. Their disclosed spend is the constraint.

### Hospital systems — capital expenditure as % of revenue, QoQ (yfinance quarterly cash flow)

| operator | 2025-09-30 | 2025-12-31 | 2026-03-31 | 2026-06-30 | peak → latest |
|---|---|---|---|---|---|
| **HCA** | 6.72% | **7.63%** | 5.86% | 6.09% | **−1.54pp** |
| **THC** (Tenet) | 5.29% | **6.59%** | 3.11% | 2.78% | **−3.81pp (−58%)** |
| **UHS** | 5.52% | **6.40%** | 4.94% | 5.02% | **−1.38pp** |
| **CYH** | 2.11% | **3.03%** | 2.56% | 2.69% | −0.34pp |

QoQ on the capex dollar itself, latest quarter: HCA **+10.0%**, UHS **+5.0%**, CYH **0.0%**, THC
**−6.7%**. Absolute dollars bounced off the fiscal-Q1 trough at three of four — **but all four are
still below their Q4-2025 capex/revenue peak, and Tenet's has more than halved.**

**★ THIS IS THE BINDING CONSTRAINT, MEASURED, AND IT IS THE STRONGEST ANTI-SIGNAL IN THE FILE.**
The customers' disclosed capital intensity is **flat-to-down**, while their vendors carry **+24pp to
+33pp of 60-day excess return vs `SPY`** (BDX +24.08, ABT +27.46, A +28.19, TMO +32.93, MTD +34.66).
**The vendor tape has moved without the customer's budget moving.** Either the budget follows, or the
tape is discounting an order recovery the customers have not yet funded. Nothing in this file resolves
which — and, decisively, **nothing will resolve it inside either bracket window** (below).

### Payers
The payer node is **negative on every window vs `SPY`**: `UNH` exc5 −2.09 / exc20 −5.43 / exc60 −1.21,
`CI` exc20 −9.19 / exc60 −6.97, `ELV` exc60 −2.72. Sweep flow agrees — `UNH` flow −0.137 with
**rs20 −5.4 and rs60 −1.5**, `CI` −0.594 with **rs20 −9.2, rs60 −7.3**, `CVS` −0.611 with **rs20
−12.9**. `UNH` sequential revenue is **−1.3% QoQ against +2.0% YoY** — the slowest growth in the
chain, decelerating sequentially. **The reimbursement node is not funding the leg.**

### Pharma / biotech R&D budgets (the tools customer)
Directly measurable only through the customer equities. `XPH` exc60 +18.18 vs `SPY` and `XBI` exc60
+17.30 vs `SPY` — the funding node is **healthy on 60d**, which is the one customer-side reading that
supports node 6. ⚠ But note this is the same `XBI` that is **−0.31 on exc20** (§3): the funding read
is as window-dependent as the leg it is supposed to explain.

### ★ PRINT DATES — and the finding that matters most for both live brackets
| name | next earnings | inside `S76` (08-19) or `S82` (08-20)? |
|---|---|---|
| A (Agilent) | **2026-08-27** | ❌ outside |
| MDT | 2026-09-01 | ❌ outside |
| ABT | 2026-10-14 | ❌ outside |
| DHR / ISRG / TMO | 2026-10-20 / 10-21 / 10-21 | ❌ outside |
| ELV / HCA | 2026-10-21 / 10-23 | ❌ outside |
| UNH / BSX / WAT / BDX | 10-27 / 10-28 / 10-30 / 11-05 | ❌ outside |

**⚠⚠ NOT ONE health care print lands inside either bracket window.** `S76` settles 2026-08-19 and
`S82` settles 2026-08-20; the earliest relevant print is `A` on **2026-08-27**, seven days after the
later settle. **Both brackets will settle on pure tape with zero fundamental information arriving.**
For `S82` in particular — a spread between two ETF baskets over five sessions with no earnings in it —
**the observable measures factor rotation and nothing else.** That is not a defect of the bracket
(it was designed to measure exactly that), but a scorer must not read either outcome as a statement
about health care fundamentals. **It is a statement about factor flow only.**

---

## §8 — LEAD/LAG, MEASURED THIS RUN (requirement 8)

Cross-correlation of daily excess-vs-`SPY` series at lags −5 … +5 sessions, 252d window. `L>0` means
the second series leads.

| pair | L−5 | L−1 | **L0** | L+1 | L+3 | L+5 |
|---|---|---|---|---|---|---|
| `XLV` vs EW-DUR | −0.117 | +0.019 | **+0.669** | +0.011 | +0.092 | −0.079 |
| `XLV` vs `TLT` | −0.055 | +0.062 | **+0.480** | +0.023 | +0.053 | −0.036 |
| `IHI` vs EW-DUR | −0.101 | +0.027 | **+0.511** | −0.044 | +0.065 | −0.081 |
| `XBI` vs EW-DUR | −0.007 | −0.040 | **+0.046** | +0.098 | +0.021 | +0.018 |
| TOOLS vs EW-DUR | −0.046 | −0.041 | **+0.193** | −0.018 | +0.053 | +0.062 |
| DEVICES vs `HCA` | −0.001 | −0.085 | **+0.467** | +0.045 | −0.174 | −0.073 |
| TOOLS vs `HCA` | −0.037 | +0.060 | **+0.149** | −0.044 | −0.051 | −0.005 |
| DEVICES vs PAYERS | −0.200 | −0.010 | **+0.298** | −0.024 | +0.000 | −0.151 |

**Result: every relationship in this chain is CONTEMPORANEOUS. No lead/lag exists at any tested
horizon** — all off-zero lags are |r| < 0.2 and unstable in sign, which is noise at n=252.

Two consequences, both binding on how this file may be used:
1. **The duration complex does not LEAD health care.** It cannot be used as an early-warning
   instrument for `XLV`, and `XLV` cannot be said to "follow rates". The exposure is same-day
   co-movement — consistent with a **shared factor allocation** (node 7), not a transmitted
   cash-flow effect. This independently supports §0's mechanism argument.
2. **The customer does not lead the vendor either** (DEVICES vs `HCA` L+1 +0.045, L+3 −0.174). So the
   §7 capex constraint is **a fundamental anti-signal, not a timing instrument** — one cannot infer
   from hospital capex when the vendor tape turns. Any claim that it does would be **[unverified]**.

**Every lead/lag claim in this file is measured above. No unmeasured lead/lag claim is made.**

---

## §9 — FLOW, THE BREADTH ARTIFACT, AND THE SHORT-FUEL TRAP

### The 0.00 breadth is an artifact — re-verified independently this run
From `SECTOR_FLOW_US.json` (`asof 2026-08-12`), computed directly: **max `vol_surge` across all 32
HLTH names = 1.29, and that name is `COR`, whose OBV state is 분산 (distributing) with rs20 only
+3.6.** HLTH median `vol_surge` **0.83**; universe median **0.760**; only **20 of 300** names clear
1.2. ⇒ **HLTH structurally cannot produce a green tag on this tape.** Confirmed: **0 green / 2 red of
32, breadth 0.00**, and **no 0-green or 0-shortlist reading is treated as evidence anywhere in this
file.**

### `S76` leg 2 recomputed from source
Names satisfying **OBV 매집 ∧ rs20 > 0**: I count **19 of 32** (21 at OBV 매집; `ELV` rs20 −0.1 and
`UNH` rs20 −5.4 fail the RS leg). **This reproduces the handed count of 19 exactly**, against a
registration anchor of 18, branch A ≤ 10 and branch B ≥ 22.
Sector row re-read: **wflow 0.216 · eqflow 0.205 · gap 0.011 · delta −0.014 · top1 `LLY` 19.4% ·
wflow_ex_top1 0.194 · top1_flips_sign False.** No single-name dependence. Verified.

### ⚠⚠ THE SHORT-FUEL TRAP — STATED EXPLICITLY, AND IT IS WIDER THAN HANDED
`scripts/us_flow.py`, FINRA Reg SHO daily, every row stamped **2026-08-12**:

| name | short% | base20 | **z** | 5v5 trend | verdict |
|---|---|---|---|---|---|
| **BSX** | 63.3% | 38.8% | **+3.95** | **+11.7 ▲** | 🔴 extreme |
| **ISRG** | 48.9% | 30.4% | **+2.41** | **+9.8 ▲** | 🔴 extreme — **NOT in the handed set** |
| MDT | 41.4% | 30.6% | +1.51 | +2.7 ▲ | 🔴 elevated |
| TMO | 53.5% | 45.1% | +1.34 | +0.8 ▲ | 🟡 |
| ABT | 52.7% | 46.1% | +0.91 | −0.1 · | 🟡 |
| XLV | 65.7% | 62.2% | +0.39 | −1.4 ▼ | 🟡 neutral |
| WAT | 55.0% | 58.6% | −0.36 | −0.3 ▼ | 🟡 |
| BDX | 55.4% | 68.9% | −1.50 | −1.9 ▼ | 🟢 covering |
| DHR | 32.3% | 48.8% | −1.61 | −6.2 ▼ | 🟢 covering |
| BMY | 31.0% | 49.3% | **−2.61** | +0.3 · | 🟢 shorts exiting |
| **A** | 34.3% | 59.5% | **−3.52** | **−5.9 ▼** | 🟢 **strongest covering in the set — NOT handed** |

**`BSX` is the trap and it must be named.** It has the leg's best exc5 (**+7.36pp vs `SPY`**) and an
un-crowded exc60 (**−7.17pp vs `SPY`**) — exactly the profile a deep-dive is built to select. But its
FINRA z is **+3.95 with a 5v5 trend of +11.7 and RISING**, the most extreme reading in the set.
`module_chart BSX --read` this run: **RSI 86.7, upper Bollinger band, +18.2% 20d momentum, OBV
누적 with a +123% 20d slope — but that OBV is a grade-C axis and its supporting RS is rs20 +17.1
against rs60 −6.9**, i.e. RS is positive only on the short window. **The rise is SHORT FUEL, not
demand.** Corroborating from my own news call (below): the buying that is visible is **insider**, not
institutional — after a **54% decline**. `BSX` exc120 is **−45.55pp vs `SPY`**. **A 54%-broken name
bouncing on a squeeze is not the same object as the tools node** and must not be filed under it.
**`ISRG` carries the identical shape** (z +2.41, 5v5 +9.8 ▲, exc5 +6.60 vs `SPY` against exc60 −9.49
vs `SPY`, rs60 −9.2) and is the second instance of the same trap.

**★ The flow separates cleanly along the same seam as the duration decomposition.** The **tools** node
has shorts *leaving* (`A` −3.52, `DHR` −1.61, `WAT` −0.36) while the **bounced-broken devices** have
shorts *piling in* (`BSX` +3.95, `ISRG` +2.41, `MDT` +1.51). The names with real residual alpha (§0)
and the names with short fuel are **disjoint sets**. That is an independent confirmation that "HLTH"
contains at least two mechanically different objects (§3).

⚠ **Conflicts I am not resolving, disclosed rather than smoothed:**
- `module_chart TMO --read` reports **OBV 중립 with a 20d slope of −6%** while the sweep records TMO
  at OBV 매집 +0.180. **Two tools disagree on the same name on the same settled date.** TMO's
  supporting RS is unambiguous (rs20 +10.3, rs60 +33.1) and MA stack is 강세 (5>20>60>120, RSI 71.3),
  so the *direction* is not in doubt — but the OBV axis is a grade-C axis (D6) and it is not
  corroborated here, so it carries no weight in this file.
- `DHR` is **OBV 분산 (distributing) with rs60 +22.6** in the sweep while FINRA shows shorts covering
  (z −1.61, 5v5 −6.2 ▼). **The tools node is not uniformly accumulating** — TMO/WAT 매집, `A` 중립,
  `DHR` 분산. Any "the tools node is being accumulated" claim would overstate the sweep.
- `MTD`, the single best exc60 name in health care (+34.66 vs `SPY`), **is not in the `us_top300` HLTH
  set at all** and therefore appears in no sweep column. The deterministic screen cannot see the
  leg's best performer.

---

## §10 — NEWS: VERIFIED WITH MY OWN CALLS (PREFLIGHT G1)

All four calls run this session, 2026-08-13, against the news API at `impolite-coherent-props.ngrok-free.dev`.
The sweep's news-velocity column is **not** used.

**Call 1 — `-m module_news_data chain-hop "medical device hospital capital spending" --days 7`**
Output verbatim: *"기사 0건 스캔"*, **HEADLINE-NAMED top 0**, **CHAIN-HOP 후보 0**.

**Call 2 — `chain-hop "life science tools bioprocessing demand" --days 7`**
Output verbatim: *"기사 0건 스캔"*, **0 headline-named, 0 chain-hop candidates.**

**Call 3 — `fts search "pharmaceutical research spending" --days 10`** → **매칭 0건.**

**Call 4 — `fts search "Medicare drug price negotiation" --days 10`** → **매칭 2건**, and one is a
false positive (`NextPlat` quarterly results, unrelated). The single real hit is
**`2026-08-12 [yahoo_finance] "AARP issues urgent call on Medicare drug costs"`**.

**⇒ Lens 4's falsifier premise VERIFIED by my own calls: there is no clean HLTH catalyst thread, and
the only policy thread that exists (Medicare drug pricing) is a RISK to the pharma node — which is
the duration-correlated node of §0 — not a driver of the tools/devices node.** The 60-day move at
nodes 4 and 6 has **no news thread underneath it at all**. That is a genuine negative: a +26pp
residual with zero narrative is either early, or it is flow.

**Call 5 — `fts search "medical device" --days 7`** → **171 matches.** Coverage exists; it is simply
not about capital spending. Two hits are load-bearing for §9 and are quoted because they are the only
`BSX`-specific evidence in the corpus:
- **`2026-08-10 [fool/yahoo_finance] "Boston Scientific Director Habiger Buys $100k of Shares Amid 54% Decline"`**
- **`2026-08-10 [fool] "Boston Scientific CEO Mahoney Buys More Than 200k Shares for $10 Million"`**
⇒ The visible `BSX` bid is **insider**, into a **54% decline**, alongside a **+3.95 FINRA z with a
rising 5v5 trend**. This corroborates the §9 trap read rather than contradicting it: insider buying
and short-covering fuel can co-exist, and neither is customer demand.

---

## §11 — TRACK KPIs AND ANTI-SIGNALS, AS DATED OBSERVABLES (requirement 10)

Every line is a settled, checkable quantity with a date. No line is a price target and none implies an
action.

### KPIs — what would confirm the leg is real
| # | dated observable | measured today | check on |
|---|---|---|---|
| K1 | Hospital capex / revenue at HCA, THC, UHS regains its **Q4-2025 peak** (7.63 / 6.59 / 6.40%) | 6.09 / 2.78 / 5.02% | **HCA 2026-10-23**, UHS + THC late Oct |
| K2 | `A` (Agilent) print — first tools datum after the window | rev +2.1% QoQ, +10.0% YoY; GM +1.34pp QoQ | **2026-08-27** |
| K3 | `TMO` next-quarter consensus stops falling (breadth 5↑/10↓ turns ≥ 1:1) | −1.1% / 90d | daily; print **2026-10-21** |
| K4 | `BDX` next-quarter estimate stops the −4.6%/90d slide, GM ≥ 48.0% own-history median | 2.73 EPS; GM 46.5% | **2026-11-05** |
| K5 | `S76` leg 2 count holds ≥ 18 of 32 on the next full `sector_flow --market us` sweep | **19** | next sweep, by **2026-08-19** |
| K6 | Tools node residual alpha stays positive when re-regressed on EW-DUR | +26.24pp / 60d | weekly |
| K7 | A HLTH catalyst thread appears at all in `chain-hop` (currently 0 of 2 themes) | **0 candidates** | weekly |

### ANTI-SIGNALS — dated, and each one is already partly firing
| # | dated observable | status today |
|---|---|---|
| **A1** | **Customer capex/rev falls further below the Q4-2025 peak at ≥3 of 4 operators** | **⚠ ALREADY TRUE — 4 of 4 are below peak; THC −58%** |
| **A2** | **Lens 4's own falsifier, carried verbatim**: on the next three settled closes `XLV` exc20 stays **< +5.0** vs `SPY` **while ≥ 8 of the 21 accumulating HLTH names flip OBV to distribution** ⇒ idiosyncratic single-name strength inside a flat sector = stock picking, not a cycle | exc20 **+4.07 — ALREADY BELOW +5.0**; 21 accumulating, **0 flipped so far**. The OBV leg is a grade-C axis and must be read with RS20 (§9) and the FINRA table, not alone |
| A3 | `BSX` / `ISRG` FINRA z stays > +2 with a rising 5v5 while exc5 stays positive | **⚠ TRUE for both** (+3.95 / +2.41) |
| A4 | Rolling 60d corr(`XLV`, EW-DUR) stays above its 252d p85 | **⚠ TRUE — 0.809 at the 92.9th pctile** |
| A5 | `WAT` cited as organic tools demand anywhere downstream | ⚠ M&A distortion flagged (§2); GM −14.67pp in one quarter |
| A6 | Payer node stays negative on exc20 vs `SPY` (`UNH` −5.43, `CI` −9.19) | **⚠ TRUE** |
| A7 | Sector-level dispersion stays > 2x the sector's own move | **⚠ TRUE at 3.7x** |
| A8 | A device or tools name is filed under the leg on exc5 alone without a FINRA z check | procedural — §9 is the guard |

### `S82` observable, recomputed from source
[`XLV` exc5 vs `SPY`] − [EW{`XLU`,`XLRE`,`XLP`} exc5 vs `SPY`] = **+2.26 − (−0.833) = +3.093pp**,
reproducing the registered state of **+3.091pp** to 0.002pp. **Already above branch A (+2.45)**, as
disclosed at registration. Branch B (≤ −1.62) is the adversarial ask.
⚠ **Carry the registered correlated-tail flag**: `S82`-B and `S80`-A are the same underlying event
(the duration complex rallying and dragging `XLV`). **If both fire that is ONE regime read, not two.**

⚠ **Methodology disclosure**: my compounded-product excess for `XLV` exc60 is **+11.82pp** vs the
sweep's **+11.58pp** — a 0.24pp gap from differencing cumulative products rather than compounding
daily excess. Immaterial to sign; disclosed rather than silently reconciled. The regression tables in
§0 use compounded daily excess throughout (which is why `XLV` shows +10.65 there and +11.82 in §3 —
same data, two conventions, both stated).

---

## §12 — WHAT THIS FILE DOES NOT RESOLVE

1. **Mega-pharma LOE / IRA-negotiation exposure is `unknown` (C3).** I did not read LOE schedules for
   the eight names, so the §0 finding that mega-pharma carries the duration loading is a **statistical**
   result whose cash-flow explanation is asserted from filing risk-language, not from a negotiation list.
2. **`TMO` margin position in its own history is `unknown` (C3)** — the tool's XBRL series ends FY2017.
3. **GPO-covered revenue share and recurring/consumable share are `unknown` (C3)** for every device and
   tools name; no mean-reversion claim rests on either.
4. **The §7 contradiction is unresolved by design**: vendor tape +24 to +33pp of 60-day excess vs `SPY`
   against customer capital intensity below its own Q4-2025 peak at 4 of 4 operators. **No print lands
   inside either bracket window to settle it.**
5. **The 60d vs 252d window flips the biotech read** (§3) and the prompt's C5 warning is realised, not
   hypothetical. Both windows are reported; neither is privileged.

---

### ONE-LINE ANSWER
**The tools/devices leg is not the fourth leg of the duration complex — the duration factor was
*negative* across the same 60 sessions and the leg's return is +26.24pp of residual alpha orthogonal
to it, with no shared cash-flow mechanism (§6) and no lead/lag transmission (§8) — but `XLV`-the-index
IS a duration proxy through mega-pharma, its coupling sits at the 92.9th percentile of its own year,
the customers' capital budgets are below peak at 4 of 4, and the dispersion is 3.7x the sector's own
move, so "HLTH" is the wrong unit for any conclusion in either direction.**
