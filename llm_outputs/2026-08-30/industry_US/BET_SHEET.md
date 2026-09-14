# BET_SHEET — industry_US · 2026-08-30 (Stage 9 / L1·BET)

> ONE file, per-sector sections §A–§E. Downstream desks read this exact filename.
> **Zero buy/sell recommendations. Zero position sizing.** Any weight language below is
> *influence illustration* only (P4).
> All prices are the **2026-08-28 5m-proxy close**, validated at **0.0225% mean / 0.038% max vs the
> KIS broker feed (n=9)** and at **2.6 bp vs FRED's `SP500`** at index level. Stated once, here.
> Every relative-performance figure names its benchmark inline (`C1`).

## §0 · Gates read before anything was derived

**Company scoreboard** (`REPORT/COMPANY_SCOREBOARD.md`, `company_batch` run 1, **2026-08-21 = 9 days**):
**5 rows, all Korean** (`036460` · `011200` · `316140` · `028050` · `000660`). **Zero US names.**
⇒ **No candidate on this sheet carries a scoreboard row, so nothing is CONFIRMED and everything is
re-dug.** That is stated rather than left implicit, and it is the honest reading — not a failure of the
age test, but an absence of coverage. ⚠ The scoreboard's own two rules are respected: its top row is a
`PASS`, and a score is research quality, not an action.
⚠ `module_report_tags ticker <T>` was consulted before calling any name un-researched (§F).

**Rights removed (from `PREFLIGHT` / `HANDOVER §0`, binding on every line below):**
🚫 no sweep-sourced news velocity or theme freshness · 🚫 no Δflow · 🚫 no `wflow` promotion on a
flipper bucket · 🚫 **no US chart-shape claim** (`module_chart` renders 0/3) · 🚫 no bare concentration
number · 🚫 `kelly_size --ic` is "mechanical 1/4", never evidenced.

🚨 **Two data caveats that bind this sheet specifically:**
1. **`us_setup_screener` numbers are D-1.** Its loader calls `dropna(subset=["close"])`, which discards
   the void 08-28 bar ⇒ **every RSI and px/200DMA it printed is computed to 2026-08-27 and excludes
   the Warsh session.** Cited with that label wherever used.
2. **The dividend-yield field is already in percent**; an earlier working table of mine multiplied it
   by 100 and read `FCX 77%`. Corrected — **FCX 0.77%**. Cross-checked against
   `trailingAnnualDividendYield` on three names (`T` 4.27 vs 0.0436 · `FCX` 0.77 vs 0.00765 ·
   `CMCSA` 4.88 vs 0.0500). **My arithmetic error, caught before it reached a line here.**

## §0b · 🚨 A dated-catalyst defect found while pulling §A, and it touches a LIVE row

`module_fundamentals_us` and `yfinance`'s own calendar **both** put **`AVGO`'s next earnings at
2026-09-03**, not 09-02. `catalyst_calendar` carries **09-02**, and **`S132`** (registered 08-29,
ARMED) observes *"`AVGO` 1-session excess vs `SPY`"* **settling 2026-09-03** — a date derived from a
09-02 print.
⇒ **If the print is 09-03, `S132`'s settle date lands on the print day rather than the reaction day**,
and its observable measures the session *before* the information. **`HPE` reads 09-03 on both sources**,
consistent with the calendar's 09-03.
🚫 **No threshold is touched and the row is not re-frozen** (`D242`). **Filed as `D420`** and handed to
HANDOVER: *a settle date derived from a catalyst date must be re-checked against the issuer's own
calendar before the row arms.* ⚠ This is the **`R106` class** — the desk retracted "July PCE prints
08-28" on exactly this failure eight days ago.

---

## §A · Numbers — one table, all sections draw from it

Forward/trailing P/E, P/S, P/B, consensus mean target and upside, dividend yield, beta, next earnings.
Source `module_fundamentals_us --json` (XBRL primary + yfinance), pulled 2026-08-30. **Blanks are
blanks.** Upside = mean target ÷ 08-28 proxy close − 1.

| ticker | fwd P/E | trail P/E | P/S | P/B | mean tgt | upside % | div % | beta | next earn |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| **FCX** | 18.5 | 37.5 | 4.2 | 5.5 | 72.05 | **−5.8** | 0.77 | 1.38 | 10-22 |
| **NEM** | 12.7 | 16.1 | 5.2 | 3.8 | 132.87 | +3.8 | 0.79 | 0.50 | 10-23 |
| **A** | 22.8 | 30.3 | 5.9 | 5.9 | 174.40 | +13.4 | 0.65 | 1.23 | 11-26 |
| **MRK** | 15.5 | 118.7 | 5.5 | 8.7 | 148.73 | **+0.3** | 2.27 | 0.21 | 10-29 |
| **UNH** | 17.5 | 25.3 | 0.8 | 3.6 | 475.23 | **+20.9** | 2.35 | 0.63 | 10-27 |
| **CVS** | 10.9 | 24.6 | 0.3 | 1.5 | 116.08 | **+24.7** | 2.86 | 0.60 | 10-28 |
| **T** | **10.1** | **8.6** | 1.4 | 1.6 | 28.71 | +10.4 | **4.27** | **0.42** | 10-21 |
| **CMCSA** | **7.5** | **8.7** | 0.8 | 1.1 | 30.08 | +11.2 | **4.88** | 0.65 | 10-29 |
| **DIS** | 14.5 | 22.0 | 1.9 | 1.7 | 127.84 | +18.3 | 1.40 | 1.40 | 11-12 |
| **NFLX** | 21.4 | 25.7 | 7.0 | 11.3 | 93.66 | +14.6 | — | 1.51 | 10-21 |
| **WBD** | **411.0** | — | 2.0 | 2.2 | 29.82 | +3.6 | — | 1.56 | 11-05 |
| **CRM** | 16.2 | 23.4 | 4.8 | 5.5 | 262.54 | **+2.6** | 0.70 | 1.15 | **08-27 (past)** |
| **NOW** | 28.9 | 89.9 | 10.2 | 12.0 | 142.23 | **−1.7** | — | 0.93 | 10-29 |
| **PLTR** | **80.5** | 159.2 | **72.7** | 45.8 | 191.68 | +2.9 | — | 1.56 | 11-03 |
| **MU** | **6.0** | 21.1 | 11.7 | 10.5 | 1513.41 | **+62.2** | 0.06 | **2.21** | 10-01 |
| **SNDK** | **5.6** | 20.1 | 10.7 | 14.1 | 2125.09 | **+43.1** | — | — | 11-07 |
| **LITE** | 27.1 | — | **26.6** | 17.1 | 1148.30 | +28.3 | — | 1.51 | 11-06 |
| **COHR** | 20.0 | 67.6 | 7.7 | 5.0 | 416.09 | **+49.0** | — | 2.11 | 11-05 |
| **AVGO** | 18.9 | 61.4 | 23.2 | 20.0 | 525.97 | **+42.6** | 0.70 | 1.47 | **09-03** ⚠§0b |
| **HPE** | 12.8 | 50.8 | 1.8 | 2.7 | 65.35 | +24.9 | 1.05 | 1.44 | **09-03** |
| **ANET** | 37.9 | 61.6 | 23.4 | 16.7 | 241.82 | +23.8 | — | 1.61 | 11-04 |
| **COIN** | 63.2 | — | 7.8 | 3.6 | 197.59 | +10.6 | — | **3.36** | 10-30 |
| **HOOD** | 31.8 | 46.1 | 19.0 | 9.9 | 121.51 | +16.5 | — | 2.32 | 11-05 |
| **SCHW** | 14.1 | 20.1 | 7.3 | 4.3 | 124.95 | +13.4 | 1.16 | 0.75 | 10-15 |
| **BX** | 19.0 | 31.9 | 11.0 | 12.6 | 144.05 | +1.2 | 3.64 | 1.55 | 10-22 |
| **AJG** | 18.0 | 44.4 | 4.5 | 2.9 | 291.56 | +9.0 | 1.08 | 0.50 | 10-30 |
| **JPM** | 14.3 | 15.3 | 5.1 | 2.7 | 374.57 | +4.7 | 1.69 | 0.98 | 10-13 |
| **BAC** | 11.8 | 14.4 | 3.8 | 1.6 | 68.77 | +10.4 | 2.09 | 1.17 | 10-14 |

**Structural position, computed on the repaired series** (08-28 proxy close vs its own history):

| ticker | vs 200DMA | vs 50DMA | vs 52w high | vs 52w low |
|---|---:|---:|---:|---:|
| `MPC` | +55.6% | +19.6% | **0.0%** | +126.8% |
| `PSX` | +43.9% | +18.5% | **0.0%** | +92.5% |
| `MU` | +58.5% | −2.3% | −23.1% | **+687%** |
| `SNDK` | +53.0% | −7.4% | −36.4% | **+2,820%** |
| `LITE` | +33.7% | +9.9% | −15.0% | **+575%** |
| `COHR` | +2.1% | −12.7% | −34.6% | +218% |
| `HPE` | +60.8% | +5.5% | −12.6% | +161% |
| `CRM` | +27.9% | **+41.7%** | −3.8% | +70.7% |
| `AVGO` | **−0.2%** | −4.5% | **−23.4%** | +25.7% |
| `ANET` | +29.8% | +8.2% | −7.2% | +68.2% |
| `NVDA` | +11.1% | +4.4% | −7.7% | +31.7% |
| `T` | +3.4% | +12.2% | −12.2% | +27.0% |
| `FCX` | +27.2% | +16.5% | −4.3% | +116% |
| `NEM` | +18.9% | +22.6% | −5.3% | +75.3% |

⚠ **`module_math_check` note**: every upside figure above is `target_mean / close − 1` on the same
proxy close used everywhere in this run; the two independent price sources agree to ≤0.04%, so the
upside column carries no more than ~4 bp of price error. **The consensus target itself carries far
more uncertainty than that**, and none of these figures is treated as precise.

---

## §B · Per-sector sections

### §B-1 · MATERIALS (OW · DEEP continuous C1)

**Thesis (from `SECTOR_DEEP_MATR.md`)**: the OW is **not a Materials call** — `FCX` + `NEM` supply
**1.411 of the 1.967 net sum** of all 12 flow scores; ex-those-two, `eqflow` collapses **+0.164 →
+0.056**, flat. **Independently re-derived: +0.0556.**
**Freshness tag: `UNMEASURED (G1 FAIL)`** — the sweep's news axis is dead and no freshness claim is
admissible. *(ALPHA fills §B freshness.)*

| name | §C flow / positioning (asof 08-28, repaired) | §D peers | §E refutation + dated catalyst |
|---|---|---|---|
| **`FCX`** | flow **+0.767** 🟡 · OBV +0.276 매집 · rs20 **+19.1** · rs60 +6.2 vs `SPY` · `vol_surge` 1.18 | best flow in MATR; `NEM` +0.644 the only comparable | 🚨 **The strongest refutation on this sheet, and it is not a flow number: `FCX`'s mean target is BELOW its price — upside −5.8%, the only negative on §A.** And its input sits at **COT copper 100th percentile**, the board's only crowded long at its maximum. ★ **The DEEP read FCX's FY2025 10-K: US cathode/rod prices off "COMEX monthly average settlement… plus a premium"; South America off LME monthly averages 1–4 months forward. NO floor, NO ceiling — index-linked pass-through**, the structural opposite of `LIN`'s take-or-pay. ⇒ **revenue amplitude tracks the LME/COMEX cycle almost unsmoothed**, and no contractual ceiling can explain a future deceleration. **Catalyst: earnings 10-22.** |
| **`NEM`** | flow **+0.644** 🟡 · OBV **+0.506 매집** · rs20 **+33.5** · rs60 +17.0 vs `SPY` | MATR #2 | 🚨 **Estimates are being cut hard while price leads.** §A revision table: 0q EPS **2.577 (90d ago) → 1.916 now = −25.7%**, on **0 up : 7 down in 30 days**. The DEEP measured two consecutive QoQ revenue decelerations, the second an outright **−16.3%** contraction. ⇒ **price/flow is not confirming the fundamental second derivative** — the `L1` lens applied and failing. ⚠ Gold COT is **66th percentile, NOT crowded**, so `NEM` does not inherit copper's positioning risk — the two must not be netted. **Gold offtake structure remains `unknown` (`C3`) — not checked this run.** **Catalyst: earnings 10-23.** |
| **`STLD`** (contrast, not a candidate) | flow −0.187 🟡 · OBV +0.089 매집 · rs20 −9.6 · rs60 **−16.7** vs `SPY` | steel | **The mirror image of `NEM` and it is the sheet's cleanest open question**: accelerating revenue (+17% QoQ) and rising EPS estimates against negative flow and a −16.7 `rs60`. **Fundamentals up, money out — the exact inverse of `NEM`.** Neither is resolved; both are recorded. |

### §B-2 · HEALTH CARE (OW · DEEP continuous C2)

**Thesis (from `SECTOR_DEEP_HLTH.md`)**: the `eqflow` +0.135 vs `XLV` `exc5` −2.46pp vs `SPY` split is
a **cap-weight artifact, not a paradox** — split by value-chain position, **upstream +0.129** (23 names,
80.9% of cap) vs **downstream −0.439** (9 names, 19.1%). `wflow` is dragged because 3 of the 4 largest
names by cap (`LLY` $980B, `ABBV` $382B, `UNH` $364B) are all flow-negative.
**Freshness tag: `UNMEASURED (G1 FAIL)`.**

| name | §C flow / positioning | §D peers | §E refutation + dated catalyst |
|---|---|---|---|
| **`A`** (Agilent) | flow **+0.906 🟢가속** — the sector's **only** green and one of four in the whole 299-name universe · OBV +0.330 매집 · rs20 +8.1 · rs60 +9.9 vs `SPY` · **`vol_surge` 1.43** | life-science tools: `TMO` +0.392, `DHR` +0.397, `WAT` +0.426 — **the whole sub-industry is positive**, so `A` is not a lone spike | fwd P/E **22.8** vs trailing 30.3, **+13.4% upside**. ⚠ **It is the sector's only 🟢 and it is a $36B name in a bucket whose $980B name is distributing** — a breadth signal, not a weight signal. **Catalyst: earnings 11-26 — nothing dated inside 90 days**, which is itself the weakness. |
| **`MRK`** | flow +0.678 🟡 · OBV +0.249 매집 · rs20 +10.9 · rs60 **+27.3** vs `SPY` · `vol_surge` 1.02 | pharma: `AMGN` +0.556, `GILD` +0.506, `PFE` +0.489, `VRTX` +0.406 — again broad | 🚨 **`L2` peak-margin lens fires and is NOT waived: upside to mean target is +0.3%** — i.e. `MRK` trades **at** consensus. Trailing P/E **118.7** against forward **15.5** — a 7.7× compression that says the trailing denominator is depressed, not that the stock is cheap. **A multiple without its margin percentile is not a valuation**, and that percentile was not established this run (`C3`). **Catalyst: 10-29.** |
| **`UNH` · `CVS`** (the negative side, carried deliberately) | `UNH` **−0.765 🔴분산** (rs20 −8.2) · `CVS` **−0.828 🔴분산** (rs20 −13.9) — **the sector's only two reds, both managed care** | HC Services mean −0.466; Managed Care −0.104 | 🚨 **These two carry the largest consensus upside on the entire sheet — `CVS` +24.7%, `UNH` +20.9% — against the two worst flow scores in their sector.** That is the value-trap shape stated explicitly. ★ **The DEEP tested the desk's regulated-return frame here and it FAILS to transfer**: `UNH`'s own 10-K MD&A says Medicare Advantage rates have run *"well below the industry forward medical cost trend"*, and MLR floors **cap** insurer margin rather than guaranteeing it — **a ceiling with a cost headwind, not a floor.** **Catalysts: 10-27 / 10-28.** |
| **`MCK`** (divergence, recorded) | flow −0.342 on three axes: OBV −0.136 분산 · rs20 **+1.4** (flat) · `vol_surge` 0.79 — against `rs60` **+18.9** vs `SPY` | distributors −0.214 | **Guidance UP, flow DOWN**: raised FY27 guidance 08-24 on oncology/GLP-1 volume, yet a 60-day winner whose 20-day relative strength has gone flat on below-normal volume while OBV distributes. ⚠ **OBV is a C-grade signal and does not carry this alone** — the claim rests on the three-axis conjunction. **Read as a policy-risk de-rate, not a demand problem.** |

### §B-3 · FINANCIALS (OW− · DEEP rotating R1) — **the mandate was EARLY vs TRAP; the answer is neither**

**Thesis (from `SECTOR_DEEP_FIN.md`)**: 🚨 **"Financials" is the wrong analytical unit.**
Sub-industry dispersion is **0.72** (Investment Banking/Brokerage **+0.210** vs P&C Insurance
**−0.512**) — **8× the sector's own −0.090 average.** Three incompatible stories are netted into one
number: **brokers/exchanges/asset managers are genuinely EARLY**, **insurance is an outright TRAP**
(3 of the sector's 5 reds), and the **Diversified Banks core sits in the literal third state**
EVENT_ALPHA named — 6 of 7 majors OBV-accumulating while `rs20` stalls negative.
**Freshness tag: `UNMEASURED (G1 FAIL)`.**

| name | §C flow / positioning | §D peers | §E refutation + dated catalyst |
|---|---|---|---|
| **`AJG`** | flow +0.446 🟡 · OBV +0.251 매집 · rs20 **+4.3** · rs60 **+30.1** vs `SPY` | insurance brokers ≠ P&C underwriters — the DEEP's split puts these on opposite sides | **Momentum is fading fast: `rs60` +30.1 → `rs20` +4.3.** LENS 3 tagged it EXTENDED-BUT-LIVE with the flip at `rs20 < 0`. fwd P/E 18.0 vs trailing 44.4, upside +9.0%. **Catalyst: 10-30.** |
| **`SCHW` · `BX` · `COIN` · `HOOD`** | `SCHW` +0.376 (rs60 +25.2, `vol_surge` 1.11) · `BX` +0.422 (rs60 +27.0) · **`COIN` +0.750** (rs20 **+19.2**, `vol_surge` 1.15) · **`HOOD` +0.561** (rs20 +17.5, rs60 +23.8) | **the two best flow scores in a 47-name sector are crypto/retail brokerage, not banks** | 🚨 **"Financials is working" is, on this axis, "the brokers are working".** ⚠ `COIN` beta **3.36** and `HOOD` **2.32** — this leg is a high-beta expression of the same tape, not a diversifier. **`COIN` carries the desk's standing denominator caveat** (worst revision book on the board) and is **carried only with it attached**. |
| **`JPM` · `BAC` · `C` · `WFC` · `MS` · `GS`** | **6 of 7 majors OBV 매집 with `rs20` flat-to-negative**: `JPM` +0.176/−1.4 · `C` **+0.377**/−2.7 · `BAC` +0.125/−2.4 · `WFC` +0.113/−2.7 · `MS` +0.089/−0.9 · `GS` +0.030/−1.5 | `PNC` is the clean outlier (neutral OBV, worst `rs20`) | ★★ **The sharpest primary-source finding of the run's DEEP set. `PNC`'s 10-K (filed 2026-02-20) answers "is NIM mean-reverting on demand or on mechanics": FY2025 NIM rose to 2.83% from 2.66%, attributed by its own MD&A to "lower funding costs" and "the continued benefit of fixed rate asset repricing" — while loan growth was only +1%.** ⇒ **the NIM tailwind is a finite, mechanical back-book effect, not demand recovery.** That is exactly why money can accumulate on a real tailwind while price has not confirmed: **2s10s at the 20.5th percentile and 10s30s at the 16.5th cap how far it can run.** ⚠ **`XLF` `exc20` is −0.97pp vs `SPY` while `exc60` is +12.19pp — the middle window disagrees with the quarter.** **Catalysts: `JPM` 10-13, `BAC` 10-14.** |
| **insurance (not a candidate)** | P&C sub-industry mean **−0.512**, OBV distributing sector-wide, 3 of 5 sector reds | — | **Named as the TRAP leg so the sector's positive 60-day tape is not read across it.** |

### §B-4 · COMMUNICATION SERVICES (OW · DEEP rotating R2)

**Thesis (from `SECTOR_DEEP_COMM.md`)**: breadth is **real** — **8 of 12** scored constituents
(`DIS`, `WBD`, `NFLX`, `CMCSA`, `META`, `T`, `VZ`, `LYV`) are **OBV 매집 with positive `rs20`**,
spanning telecom, cable, media-streaming and one mega-cap. The **negative `wflow` (−0.424) is the
ad-tech complex alone**: `GOOGL` −0.558 and `GOOG` −0.737 at ~85% of the bucket's cap weight.
⇒ **`eqflow` +0.079 is not an artifact; `wflow` is the artifact.**
**Freshness tag: `UNMEASURED (G1 FAIL)`.**

| name | §C flow / positioning | §D peers | §E refutation + dated catalyst |
|---|---|---|---|
| 🚨 **`T`** — **held in the REAL account, 27 shares, $702 ≈ 13.6% of invested capital, and owned by NO thesis until this run** | flow **+0.333** 🟡 · **OBV +0.393 매집** · rs20 **+8.8** · rs60 **+8.4** vs `SPY` · `vol_surge` **0.40** · FINRA short z **+0.33** (normal) · **+2.508pp on the hawkish 08-28 session** | ranks **5th–6th of 12**, tied with `META` — ⚠ **corrected from my own PREMORTEM claim of "2nd", caught by the DEEP agent** | fwd P/E **10.1** · trailing **8.6** · P/B 1.6 · **div 4.27%** · **beta 0.42** · +10.4% upside. ⚠ **Estimates are being cut on the near quarter**: +1q EPS **0.5466 (90d) → 0.5251 = −3.9%**, on **2 up : 13 down in 30 days**. ★ **The DEEP computed dividend coverage at ≈39% of FCF from the 10-K's own figures**, which does **not** confirm a live anti-signal headline questioning the payout. ⚠ **Why it rose on a hawkish day**: a 93rd-percentile 10y is a headwind for a leveraged high-yield telco, but **HY OAS at the 0.0th percentile is the offsetting tailwind** — the credit side won. **That is a conditional explanation, not a thesis, and it inverts if `P116` fires branch B.** **Catalyst: earnings 10-21.** |
| **`CMCSA`** | flow +0.422 🟡 · OBV +0.377 매집 · rs20 +9.9 · rs60 **+13.0** vs `SPY` | cable | **Cheapest name on the entire sheet**: fwd P/E **7.5**, trailing 8.7, P/B **1.1**, div **4.88%**, +11.2% upside. ⚠ **Cheap and accumulating is the shape that has been a value trap in this sector for years** — the refutation is that no catalyst is dated inside 60 days. **Catalyst: 10-29.** |
| **`DIS` · `WBD` · `NFLX`** | `DIS` **+0.539** (best in sector, OBV **+0.577 매집**, rs20 +9.4) · `WBD` +0.461 (OBV +0.475) · `NFLX` +0.444 (rs20 **+11.0**, rs60 −1.7) | media/streaming — the sub-industry carrying the breadth | **`WBD` fwd P/E 411.0 and no trailing** — the multiple is meaningless and is **not** used to call it anything. `DIS` +18.3% upside at fwd 14.5. ⚠ **`XLC` was the best sector on 08-28 (+1.63pp vs `SPY`) and the Meta $18bn settlement is the obvious candidate cause — but `META`'s own flow is only +0.333 and its `rs60` is −9.2**, so the sector's strength is **not** Meta-led. **Tested, not assumed.** |

### §B-5 · INFORMATION TECHNOLOGY (N · ★PREMORTEM-PROMOTED 5th DEEP)

**Thesis (from `SECTOR_DEEP_IT.md`)**: **IT is two sectors.** Software `rs60` mean **+4.39** vs
hardware **−17.44** vs `SPY` — but **intra-cohort ranges (65–80pp) dwarf the 21.8pp between-cohort
gap**, so the two-sector read is real but approximate, and the file says so.
**Freshness tag: `UNMEASURED (G1 FAIL)`.**

| name | §C flow / positioning | §D peers | §E refutation + dated catalyst |
|---|---|---|---|
| **`CRM`** | flow **+1.000** (the cap) 🟢가속 · OBV +0.305 매집 · rs20 **+36.3** · rs60 **+32.4** vs `SPY` · **`vol_surge` 1.64 — the only volume-confirmed green on the board** · FINRA short z **−0.76**, 5v5 **−12.5▼** (shorts leaving) | software greens `INTU` +0.850, `MSTR` +0.883; `NOW` +0.572, `PLTR` +0.506, `SHOP` +0.456 all positive | **It already printed — 2026-08-27 — so this is post-earnings drift, not pre-print speculation.** fwd P/E 16.2 vs trailing 23.4; **upside only +2.6%**, i.e. it has run to consensus. ⚠ **+41.7% above its 50DMA** — extended by any measure. **No dated catalyst inside 60 days**, which is the honest weakness. |
| **`AVGO`** (paper-book) | flow **−0.717 🔴분산** · OBV −0.147 · rs20 −8.3 · **rs60 −25.1** vs `SPY` · FINRA z +0.26, 5v5 −5.7▼ | worst flow of any book name | 🚨 **Distributing INTO its print.** **−23.4% off its 52-week high and −0.2% from its 200DMA** — sitting exactly on the line. **+42.6% consensus upside** against 🔴분산 flow. **Implied move ±8.09%** (09-04 expiry, K=367.5, OI 645c/354p) vs **6.21%** realised ⇒ a move inside ±8.09% is **pre-declared no-information**. Revisions: 0q **+1.6% in 90d**, 25 up : 9 down. **Catalyst: 09-03 (⚠ §0b — the calendar says 09-02 and `S132` settles 09-03).** |
| **`HPE`** (held in BOTH books) | flow +0.275 🟡 · OBV +0.096 매집 · rs20 +6.2 · **rs60 −7.2** vs `SPY` · FINRA z −1.44 | — | ★ **New primary-source anti-signal from the DEEP**: the 10-K discloses the **Server reporting unit's goodwill fair-value cushion is only 11% on a $10.2bn goodwill balance**, and MD&A calls AI-server margins *"very competitive… limited"* despite backlog growth. **Implied ±11.23%** (P/C OI **2.19×**) vs **7.21%** realised — the option book is positioned for downside while OBV accumulates. **Two-sided by construction. Catalyst: 09-03.** |
| **`MU` · `SNDK`** (memory producers) | `MU` +0.346 OBV +0.126 매집, rs20 +10.3, **rs60 −15.6** · `SNDK` +0.358 OBV +0.100 매집, rs20 **+19.3**, **rs60 −20.9** · `MU` FINRA z **−1.67**, 5v5 **−16.9▼** — the board's largest short exodus | equipment is the mirror: `AMAT` **−0.839 🔴**, `KLAC` −0.647, `LRCX` −0.022 | 🚨🚨 **The peak-margin trap in its purest form. `MU` fwd P/E 6.0 with +62.2% upside; `SNDK` fwd 5.6 with +43.1%. And the denominator is being chased: `MU`'s 0q EPS ran 22.66 → 31.28 in 90 days = +38.0%, on 26 up : 0 down in 30 days.** ⇒ **a low multiple whose estimates are revised up that steeply is consensus chasing, not cheapness** — and the revision table is **not** a leading indicator and carries **no independent weight on an IT name**. ⚠ The DEEP measured `WDC` 48.9% and `SNDK` 71.5% **all-time-high** trailing gross margins against `rs60` of −24.6/−20.9 vs `SPY`. ⚠⚠ **And its contract-terms conclusion was OVERTURNED** (superseded 10-K; the FY26Q3 10-Q discloses take-or-pay with a floor/ceiling band) ⇒ **a decelerating contract-price rate may be arithmetic hitting a cap, not demand.** **Withheld from candidacy: these are `P111`'s registered observable (`S4`, out-of-sample).** |
| **`LITE` · `COHR`** (optical) | `LITE` +0.550 OBV +0.287 매집, **rs20 +22.3**, rs60 −6.6 · `COHR` +0.324 OBV +0.121 매집, rs20 +3.2, **rs60 −35.2** vs `SPY` · `LITE` FINRA z −1.04, 5v5 −10.5▼ | new chain-hop candidate from the DEEP: **`AAOI`** ($9.0bn), whose 08-24 equity raise produced a body-proximate sympathy sell-off in both | 🚨 **`D250`, 15th run: neither has a row in `cycle_registry.json`** — the AI-compute epicenter list carries `ANET` (the switch) but not the optical module layer inside it. ⇒ **exposure is UNMEASURABLE, not zero, and a cycle with no row cannot produce a GAP flag by construction.** ★ **`LITE`'s `rs20` +22.3 is the strongest 20-day number in this run's whole candidate set — against `ANET`'s +5.3.** ⚠ **But `LITE` is +575% off its 52-week low at P/S 26.6 and P/B 17.1** — the entry question is timing, and this sheet does not answer it. **No dated catalyst before 11-06.** |

### §B-6 · Cross-sector LIVE_SHORTLIST names (outside the DEEP sectors)

`US_LIVE_SHORTLIST.json` passed **4**: `CRM`, `A`, `MSTR`, `INTU` — **all already covered above**
(`CRM`/`INTU`/`MSTR` in §B-5, `A` in §B-2). **No cross-sector name is dropped**, because none exists
outside the DEEP set. ⚠ **The shortlist's own absences are the finding and were diagnosed in
`SWEEP_READ §4`**: 9 of 11 sectors produced zero names because the universe holds **4 greens against
73 reds**, and Energy's zero is a **🟢-tag filter artifact** (`MPC` +0.650 and `PSX` +0.388 are both
OBV-accumulating but tagged 🟡).

### §B-7 · Epicenter-starter module — **not required this run**

`CYCLE_EXPOSURE` reports **no GAP**: AI-compute epicenter **16.93%** (need ≥12.0%) · Energy/refining
**9.97%** (need ≥8.0%) · missile-defense 3.83% (**threshold unset — the guard is disarmed, not
passing**). ⇒ **no starter basket is owed.** 🚨 **But the audit is of the REAL account, and the
paper book differs on 6 of 13 names** (`HANDOVER`/`PREMORTEM §0a`) — **the GAP verdict therefore
applies to one book and not the other, and neither stage checked which.**

---

## §F · Ledger — every set-aside and every miss

**Written this stage** (all with class + condition + recheck date, script-enforced):

| ledger | ticker | class | condition | recheck |
|---|---|---|---|---|
| reject | `FCX` | `H.밸류소진` | revives if the mean target moves back **above** the price (upside > 0) **while** copper COT drops below the 85th percentile | 2026-09-22 |
| reject | `NEM` | `I.테제반증` | revives if 0q consensus EPS **stops falling** (two consecutive weeks with `downLast7Days` = 0) **and** QoQ revenue re-accelerates | 2026-09-22 |
| reject | `MRK` | `H.밸류소진` | revives if upside to mean target exceeds **+8%** on an unchanged flow score | 2026-09-22 |
| reject | `UNH` · `CVS` | `A.flow미도착` | revives if `obv_state` turns 매집 **and** `rs20` turns positive vs `SPY` | 2026-09-22 |
| missed | `T` | `U.발굴부재` | enters if it acquires a standing thesis row **and** the two books are reconciled | 2026-09-08 |
| missed | `CMCSA` | `R.타이밍대기` | enters if a dated catalyst lands inside 60 days while flow ≥ +0.30 | 2026-09-22 |
| missed | `LITE` | `Q.확신부족` | enters if `rs60` turns positive vs `SPY` while OBV stays 매집 | 2026-09-22 |
| missed | `DIS` | `M.숏리스트탈락` | enters if it turns 🟢 in a sweep with `vel_coverage` ≥ 80% | 2026-09-22 |

**Carried from earlier stages, not re-filed**: `SLB` (`M.숏리스트탈락`) and `CRM` (`Q.확신부족`)
from EVENT_ALPHA; the two thread kills (`NVDA`, `MU` — `K.본문반증`) from EVENT_ALPHA.
**Re-filed rather than removed**: none this run — **no name was set aside on narrative grounds while
its measured flow still passed.** `MU`/`SNDK` are **withheld, not rejected** (`P111` out-of-sample).

⚠ **`module_report_tags ticker` consulted before calling `T` un-researched** — it returns no US
per-name row for `T` in any report, which is what makes `U.발굴부재` the correct class rather than
`Q.확신부족`.

---

## §G · Exposure consistency (from `HANDOVER §4`)

Rule state **정상** · target invested **95%** · current **85.5%** · band gap **−9.5pp** ·
cumulative excess **−11.68pp = cash −5.94 + selection −5.74, n=16 (third run unmoved)**.
⇒ **The state is `정상`, not `복귀`, so this sheet is not required to supply candidates to close a
gap.** It supplies **zero ENTER language of any kind** (P4), and the −9.5pp band gap is carried as
context for the human, not acted on here.
🚨 **Standing alarm reported, not cleared**: `ARMED (TIMEFOLIO_EXECUTE=1)` on every ledger row —
the instrument's own output, not this desk's to change (P4/P6).

---

## ✅ EXIT CHECK
- [x] **Company scoreboard consulted first** (§0) — **zero US rows**, so every name is RE-DUG and that is stated, with the scoreboard's own two reading-rules respected. No matured observation point existed to grade.
- [x] Every DEEP sector has a section (§B-1…§B-5); **cross-sector LIVE shortlist names accounted for** (§B-6 — all four already covered, none silently dropped), and the shortlist's **absences diagnosed** rather than cited.
- [x] Numbers cross-checked — two independent price providers agree to ≤0.04%; **blanks are blanks** (`WBD` trailing P/E, several dividend fields, `SNDK` beta); ⚠ **one arithmetic error of my own found and corrected before it reached a line** (§0, the ×100 dividend bug).
- [x] **Flow/positioning cross-read present per candidate** (FINRA short-vol z on 14 names, dated 2026-08-28 — unaffected by the ghost bar); **BET_SHEET.md written as ONE file**.
- [x] **Every set-aside name is in the ledger with a class AND a `--revives-if`** (§F). No permanent bans filed.
- [x] **No name removed on narrative grounds alone while its measured flow still passed** — none this run; `MU`/`SNDK` are **withheld for out-of-sample integrity**, which is recorded as a withholding, not a rejection.
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** with `--enters-if` (§F, 4 rows). The funnel is scored on both sides.
- [x] **Sizing language consistent with the exposure state** (§G): state is `정상`, no target to fill, **zero sizing language anywhere**.
- [x] **Linter run on this stage's own output** — `report_lint.py BET_SHEET.md` ⇒ **0 findings** (C1/C2/S6/D6). ⚠ Form only; a clean run is not a correct report. The substantive errors this stage found are in §0 (my own ×100 dividend bug) and §0b (`D420`, the `AVGO` settle-date defect on a live row).


---

# §B FRESHNESS TAGS — filled by ALPHA (Stage 10 / L1·ALPHA), 2026-08-30

> Each `§B` section above carried `Freshness tag: UNMEASURED (G1 FAIL)` as a placeholder. **ALPHA
> replaces it here**, and the replacement is possible for a reason this run had to establish first.

## §α-0 · 🚨 The gate this stage is told not to walk through blind — and what the probe returned

The L1 says plainly: **when `G1` FAILs, ALPHA may not issue a freshness verdict at all**, because
*"a dead pipe and a quiet theme return the identical value."* `G1` **did** FAIL (`vel_coverage`
17.06%). So the falsification probe was run **before** any tag below was written:

| probe | result |
|---|---|
| `fts search` ×6, pre-sweep (`--scope foreign`, 7d counts) | **6/6 alive**, differentiated: 1237 / 5251 / 2022 / 55 / 1044 / 2467 |
| `fts search` ×4, post-sweep | **4/4 alive**, identical values |
| ★ 5 names the sweep recorded as `velocity: null`, re-queried directly | **5/5 answered normally** — QCOM 0.98 · DIS 0.70 · ADBE 1.03 · PFE 0.74 · T 0.75 |
| `theme-age` ×6 this stage | **6/6 returned differentiated, non-zero verdicts** (below) |

⇒ **The pipe is alive and the failure is confined to the sweep's own 300-query burst.** ★ **And
`theme-age` is on the healthy path by construction**: `module_news_data/__main__.py:50` routes it
through `DB_READ_CMDS` to the **remote server index**, so it never touched the stale client mirror
that broke `brief`/`thread` earlier in this run.
⇒ **ALPHA issues freshness verdicts, and states exactly which instrument each one came from.**
🚫 **Still barred: any freshness number sourced from `SECTOR_FLOW`'s velocity axis.** The two are
different instruments and only one of them failed.

## §α-1 · `theme_age` — deterministic novelty, 90d window, `--scope foreign`

| theme | verdict | age | 7d mean | **accel** | total |
|---|---|---|---:|---:|---:|
| **Jackson Hole** | 🟡 **ACCELERATING** | ≥90d | 167.0 | **27.23×** | 1,359 |
| **Warsh** | 🟡 **ACCELERATING** | ≥90d | 180.9 | **3.20×** | 4,719 |
| optical | ⚪ ECHO | ≥90d | 61.9 | 1.53× | 2,394 |
| memory | ⚪ ECHO | ≥90d | 216.7 | 1.11× | 11,211 |
| data center | ⚪ ECHO | ≥90d | 331.0 | 1.03× | 18,317 |
| rate hike | ⚪ ECHO | ≥90d | 100.4 | 0.93× | 6,591 |
| **Hormuz** | ⚪ **ECHO** | ≥90d | 133.0 | **0.79×** | 9,660 |

★★ **`M1106` `[measured]` — this table closes the loop on my own error, and it closes it against me.**
`MACRO §B-3` computed Hormuz velocity two ways: **naive 0.80** and a "dark-day-corrected" **1.04**.
I withdrew the correction an hour ago when the stale-mirror mechanism was found. **`theme_age`, a
third and independent instrument on the remote index, returns Hormuz accel `0.79×`** — i.e. it agrees
with the **naive** figure to 1 bp and refutes the "correction" outright. **Three instruments, one
answer: Hormuz is decaying, not flat.**

★ **`M1107` `[measured]` — `F1` reproduces, and for the first time on a VERIFIED pipe.**
**No theme scores 🟢FRESH.** The desk has recorded that zero for many runs and the standing warning is
that *"eighteen identical observations are not eighteen observations if one wire is loose."* This run
ran the probe four separate ways and all four came back alive, and `theme_age` returned six
differentiated verdicts spanning 0.79× to 27.23×. ⇒ **This zero is arithmetic, not instrument** —
and that is a statement no prior run was in a position to make.

## §α-2 · Tags — per §B section

| § | name | **tag** | evidence label + date | residual / re-check |
|---|---|---|---|---|
| B-1 | `FCX` | 🔴 **RESOLVED** | Theme `data center`/copper ⚪ECHO 1.03×; **consensus target is BELOW price (−5.8%)** and copper COT is at its **100th percentile** — the move is priced and the positioning is maxed | **dropped from the bettable list**, ledger `H.밸류소진`, revives-if upside > 0 while COT < 85th pctile, recheck **2026-09-22** |
| B-1 | `NEM` | 🔴 **RESOLVED** | 0q consensus EPS **−25.7% in 90d** on **0 up : 7 down**; two consecutive QoQ revenue decelerations | dropped, ledger `I.테제반증`, recheck **2026-09-22** |
| B-2 | **`A`** | 🟡 **PARTIAL** | The universe's only HLTH 🟢 (flow +0.906, `vol_surge` 1.43) and its whole sub-industry is positive — **but no theme it rides scores FRESH, and its next catalyst is 11-26** | **Residual: a dated catalyst inside 60 days.** Re-check **2026-09-22**. ⚠ **Carried forward independently of whether HLTH keeps a DEEP slot** |
| B-2 | `MRK` | 🔴 **RESOLVED** | `L2` fires: **+0.3% upside = trades at consensus**; trailing/forward 118.7→15.5 | dropped, ledger `H.밸류소진`, recheck **2026-09-22** |
| B-2 | `UNH` · `CVS` | 🔴 **RESOLVED** | Largest upside on the sheet against the two worst flows in the sector; the regulated-return frame **fails to transfer** (10-K MD&A) | dropped, ledger `A.flow미도착`, recheck **2026-09-22** |
| B-3 | banks (`JPM`·`BAC`·`C`·`WFC`·`MS`·`GS`) | 🟡 **PARTIAL** · ⚠ **positioning flag** | `rate hike` theme ⚪ECHO **0.93×** — the driver is *decaying* even as `Warsh` accelerates 3.20×. OBV accumulating, `rs20` flat-negative | **Residual: `rs20` turning positive vs `SPY` on any of the six.** Re-check **2026-09-08** (`S134` settles 09-04). ⚠ **`PNC`'s 10-K says the NIM tailwind is fixed-rate-asset repricing — a finite back-book effect**, so the residual has a clock on it |
| B-3 | `COIN` · `HOOD` | 🟡 **PARTIAL** · 🚨 **momentum-only, hard-stop required** | Best two flow scores in FIN, **but betas 3.36 / 2.32** and the accumulation axis is **OBV only = C-grade** (r≈0.49, no lead, t=1.00) | ⚠ **Per rule `D6` a C-grade disagreement downgrades to 🟡 and is reported as a disagreement — it does not by itself make this a tape trade.** `COIN` carried **only with its denominator** (worst revision book on the board). Re-check **2026-09-22** |
| B-3 | `AJG` | 🟡 **PARTIAL** | `rs60` +30.1 decaying to `rs20` +4.3 vs `SPY` | **Residual: `rs20` < 0 flips it to EXHAUSTED.** Re-check **2026-09-18** |
| B-4 | 🚨 **`T`** | 🟡 **PARTIAL** — **and this is a reconciliation item before it is a bet** | Flow +0.333, **OBV +0.393 매집**, `rs20` +8.8 vs `SPY`, **+2.508pp on the hawkish session**, FINRA z +0.33 normal. fwd P/E 10.1, div 4.27%, beta 0.42 | **Residual is NOT a price condition — it is that the desk owns 13.6% of invested capital in a name with no thesis.** Handed to HANDOVER as `D415`. `missed_ledger` `U.발굴부재`, enters-if it acquires a thesis row **and** the two books are reconciled, recheck **2026-09-08**. ⚠ **Estimates being cut: +1q EPS −3.9% in 90d on 2 up : 13 down** |
| B-4 | `DIS` · `CMCSA` | 🟡 **PARTIAL** | Best COMM flow (`DIS` +0.539, OBV +0.577) and the cheapest name on the sheet (`CMCSA` fwd 7.5, div 4.88%) | **Residual: no dated catalyst inside 60 days** on either. `missed_ledger` rows filed. Re-check **2026-09-22** |
| B-5 | `CRM` | 🟡 **PARTIAL** · ⚠ **extended** | **Its print already fired — 2026-08-27** ⇒ this is post-earnings drift, and the theme it rides is not FRESH. **+41.7% above its 50DMA**, upside only **+2.6%** | **Residual: the catalyst is spent.** `missed_ledger` `Q.확신부족` (filed at EVENT_ALPHA). Re-check **2026-09-12** |
| B-5 | `AVGO` | 🟡 **PARTIAL** · ⚠ **binary in 3 sessions** | 🔴분산 flow into its own print; **−23.4% off its 52w high, −0.2% from its 200DMA** | **Residual: the 09-03 print.** ⚠ **`S132` and `S127` are armed on it — ALPHA adds nothing and re-freezes nothing.** ⚠ **`D420`: the settle date may be one session early** (§0b) |
| B-5 | `HPE` | 🟡 **PARTIAL** · ⚠ **binary in 4 sessions** | OBV 매집 + `rs20` +6.2 against `rs60` −7.2 vs `SPY`; option book **2.19× put-heavy**; **11% goodwill cushion** on the Server unit (10-K) | **Residual: the 09-03 print.** Deliberately unbracketed — deferred to the IT DEEP by the 08-29 precedent, renewed today |
| B-5 | `LITE` · `COHR` | 🟡 **PARTIAL** | `optical` is the **highest-accelerating ECHO on the board (1.53×)** and `LITE`'s `rs20` **+22.3 vs `SPY`** is the strongest 20-day figure in the candidate set | **Residual: `rs60` still negative (−6.6 / −35.2).** ⚠ **`D250`, 15th run — no cycle-registry row, so exposure is unmeasurable, not zero.** `missed_ledger` `Q.확신부족`, recheck **2026-09-22** |
| B-5 | `MU` · `SNDK` | ⛔ **NO TAG — withheld, and that is not a 🔴** | They are **`P111`'s registered observable** (settles 2026-09-14) | **Withheld to keep the test out-of-sample (`S4`).** Recorded here so the absence of a tag is legible and is **not** read as a rejection |

**Tag census: 🟢LIVE 0 · 🟡PARTIAL 10 · 🔴RESOLVED 5 · withheld 2.**
**Every 🔴 is in `reject_ledger` with a class, a `--revives-if` and a `--recheck-date`** (§F above).
**Every 🟡 carries an explicit re-check date**, and **all of them are listed for carry-forward
regardless of whether their sector holds a DEEP slot next run** — the `006360` failure (`+12.3%`
unowned over five sessions after its sector rested) is the reason that sentence exists.
