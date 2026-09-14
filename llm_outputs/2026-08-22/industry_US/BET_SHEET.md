# BET_SHEET — industry_US · 2026-08-22 (Sat) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split.
> Flow `asof` **2026-08-21** settled; `exc5` vs **`SPY` (−1.368%)** named inline (`C1`).
> **Sizing language here is influence illustration only — zero buy/sell recommendation (P4).**
> DEEP set: `ENRG` · `HLTH` · `FIN` · `INDU` · `IT` (PREMORTEM-promoted 5th).

## §0 · Gates read before anything was derived

**Thesis-confirmation gate — no rows to confirm.** `REPORT/COMPANY_SCOREBOARD.md` (2026-08-21, run 1)
holds **5 names, all KR** (`036460` `011200` `316140` `028050` `000660`). **Zero US rows** ⇒ every US
candidate below is derived here, not confirmed. ⚠ **And its own two rules are respected**: the score
measures research quality, not action (its rank-1 is a `PASS`), and it is not quoted as expected return.

**Instrument rights (`PREFLIGHT_US`)** — no news velocity or theme freshness from the sweep; no
concentration figure without its `--days`, **and today not even as a single count** (`G4`: 250d **11**
units and 500d **11** units with *different membership*); no `EA` reading; **no 2026-08-22 price**.
Tags **are** citable (velocity `null` on all 299 ⇒ velocity-free) as **3-axis unanimity**.

⚠ **`us_setup_screener` note (`D304`, 3rd run).** It stamps its header **2026-08-22** while the
terminal bar is **2026-08-21**, and it still emits no `bar_settled` field. **Today that ambiguity is
harmless because the US market did not open — the bar it scanned IS settled.** ⚠ **On a weekday it
would not be, and the defect is unchanged.** Its 18 `🆕신규` names are used below as *raw setup
candidates*, never as promotions.

---

## §A · Numbers — the candidate set, one table (XBRL ↔ yfinance via `module_fundamentals_us --json`)

Blanks are printed as blanks. **Price column is the 2026-08-21 settled close.**

| Ticker | px | mcap | fwd P/E | trail P/E | PEG | P/S | P/B | fwd EPS | target mean | 52w high | px / 52wH | next ER |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| `MRK` | 152.55 | 376B | 15.99 | 122.04 | 14.56 | 5.65 | 8.98 | 9.54 | **146.54** | 154.49 | **98.7%** | 10-29 |
| `PFE` | 28.07 | 160B | **9.69** | 36.93 | 2.74 | 2.51 | 1.88 | 2.90 | 28.61 | 28.75 | **97.6%** | 11-03 |
| `TGT` | 165.44 | 75B | 17.44 | 16.41 | 2.95 | 0.70 | 4.58 | 9.49 | **160.32** | 165.48 | **100.0%** | 11-18 |
| `MSI` | 480.47 | 80B | 25.18 | 37.30 | 2.29 | 6.50 | 29.76 | 19.08 | 522.73 | 493.57 | 97.3% | 11-06 |
| `ECL` | 281.63 | 79B | 29.90 | 37.75 | 2.95 | 4.69 | 7.85 | 9.42 | **324.95** | 309.27 | 91.1% | 10-27 |
| `COIN` | 186.49 | 49B | 61.79 | — | 9.09 | 8.14 | 3.76 | 3.02 | 194.97 | 402.16 | **46.4%** | 10-30 |
| `MSTR` | 119.25 | 47B | **2.41** | — | 2.85 | **95.07** | 1.43 | 49.49 | 229.07 | 365.21 | **32.7%** | 10-30 |
| **`ORCL`** | 146.47 | 422B | **13.42** | 25.12 | **0.81** | 6.26 | 11.23 | 10.91 | **246.43** | 345.72 | **42.4%** | **09-11** |
| `TRI` | 105.53 | 46B | 20.76 | 27.84 | 1.59 | 5.84 | 4.11 | 5.08 | 122.29 | 180.00 | 58.6% | 11-03 |
| `HOOD` | 108.13 | 97B | 33.29 | 47.85 | 2.17 | **19.71** | 10.25 | 3.25 | 119.93 | 153.86 | 70.3% | 11-05 |
| `ANET` *(held)* | 188.65 | 238B | 36.56 | 59.51 | 1.76 | 22.57 | 16.08 | 5.16 | 241.82 | 214.89 | 87.8% | 11-04 |
| `VLO` | 348.86 | 100B | 11.43 | 14.55 | 4.08 | 0.76 | 4.02 | 30.52 | **312.53** | 352.70 | **98.9%** | — |

★ **Four names trade ABOVE their consensus mean target** — `MRK` (+4.1% over), `TGT` (+3.2%),
`VLO` (+11.6%), `PFE` (−1.9%, essentially at it). **Three of them are the sheet's strongest flow
names.** That is a valuation state, not a verdict (P4), and it is printed because it is the same
condition on all three.

### Revision breadth — read as the DENOMINATOR'S DIRECTION only, never as a lead indicator

🚫 **Standing constraint applied, not summarized.** `measure_ic`'s control arm settled this:
**ex-IT 120 names give +0.074 / −0.064 with a Q5−Q1 spread of +9.4pp → −1.1pp** ⇒ **the revision
effect is an Information-Technology loading, not a revision axis.** ⇒ **`ORCL` and `ANET`'s revision
lines below are exactly where the confound lives and are NOT independent evidence for them.**

| Ticker | 0q (30d) | +1q (30d) | Reading |
|---|---|---|---|
| `ANET` *(held, IT)* | **21↑ / 0↓** | **21↑ / 0↓** | perfect breadth — 🚫 **IT confound, not independent evidence** |
| **`ORCL`** *(IT)* | **19↑ / 6↓** | **20↑ / 5↓** | strongest ex-`ANET` breadth — 🚫 **same confound** |
| `MSI` | 5↑ / 3↓ | **11↑ / 0↓** | clean, and **not** an IT-confound name by business (comms equipment for public safety) |
| `TGT` | **7↑ / 0↓** | 6↑ / 2↓ | clean |
| `ECL` | 7↑ / 6↓ | 9↑ / 4↓ | mixed |
| `HOOD` | 11↑ / 4↓ | 9↑ / 5↓ | positive, noisy |
| `TRI` | **1↑ / 11↓** | **11↑ / 1↓** | 🚨 **inverted between horizons — the current quarter is being cut while next year is raised** |
| `PFE` | **1↑ / 14↓** | 11↑ / 4↓ | same inversion, sharper |
| `MRK` | **1↑ / 5↓** (7d: **2↑ / 10↓**) | 2↑ / 4↓ | 🚨 **the sheet's only 🟢 in Health Care has NEGATIVE revisions in both horizons** |
| `MSTR` | 3↑ / 0↓ | 3↑ / 0↓ | ⚠ meaningless — the denominator is a bitcoin mark |
| **`COIN`** | **0↑ / 17↓** | **0↑ / 17↓** | 🚨🚨 **the worst revision profile on the sheet, and it is the sector's only green** |

---

## §B · Per-sector sections — thesis, freshness placeholder (ALPHA fills), flow, competition, refutation

### §B-ENRG — Energy (OW) · continuous track

**Candidates**: `PSX`*(held)* · `MPC`*(held)* · `COP` · `VLO` — and `XOM` as the **control**.
**Screener contributed nothing in Energy** (0 of 18 `🆕신규` names are Energy).

| | |
|---|---|
| **Thesis** | Refining-**capacity** destruction. Three independent mechanisms now dated: Hormuz near-zero traffic, Russian refinery strikes (**Lukoil hit 08-21**), Aramco Jazan closed since end-July |
| **Freshness** | `[ALPHA]` |
| **§C Flow** | All four **OBV-accumulating with positive `rs20` vs `SPY`**, all four **blocked from 🟢 by `vol_surge` alone**. `PSX` +0.728 (rs60 +37.0) · `MPC` +0.700 (**rs60 +44.0**) · `COP` +0.694 · `VLO` +0.506 (rs60 +43.1). FINRA: all 🟡 normal; `PSX` 5v5 **+8.4▲**. **Control `XOM` −0.183 with OBV DISTRIBUTING** |
| **§D Competition** | `VLO` **fwd P/E 11.43** vs `MPC`/`PSX`; ★ **`VLO`'s gross-margin percentile is now measurable** (this run's ledger fix): **FY2025 4.43% = the 50th percentile of FY2016–FY2025**, median 4.60%, range −1.14% to 9.52%. **Dead median.** ⚠ And it trades at **98.9% of its 52-week high, 11.6% ABOVE consensus mean** |
| **§E Refutation + catalyst** | 🚨 **`P70` MISSED at settle** — the separation claim is gone (`R89`). `MPC` chart shows a **bearish RSI divergence at RSI 76.7**. `P89` settles **08-28** (kill: `BZ=F` ≤ 88.00 **or** distillate crack ≤ 90.0); `P83` **08-27**; `P80` **08-26**; `S92` **08-31**. 🚨 **The contract read that would settle margin durability is 3 runs unopened** |

### §B-HLTH — Health Care (OW) · continuous track

**Candidates**: `MRK` (the only 🟢) · `PFE` (sector's highest `obv_norm` +0.517) · `BDX` (highest
`rs20` +19.2) · `A` (rs60 +35.2, **delta +0.285**) · `TMO` (rs60 +35.9) · `AMGN`.
**Screener contributed `ISRG`** (bucket B de-rate snapback, RSI 51.9, px/200 **−20%**).

| | |
|---|---|
| **Thesis** | The sector decoupled **upward** out of the duration complex (`S82` FIRED-A) on a dated driver: the Moderna/Merck Phase-3 mRNA cancer-vaccine success, **2026-08-19**, `XLV` **+3.51%** that session |
| **Freshness** | `[ALPHA]` |
| **§C Flow** | **Nine of nine top names accumulate with positive `rs20` vs `SPY`; one clears the volume gate.** Breadth 0.03 is a gate artifact, not thin flow (`SECTOR_DEEP_HLTH §2`). FINRA: no 🔴 in the sector; `PFE` z +1.20 with **5v5 −8.7▼** |
| **§D Competition** | `PFE` **fwd P/E 9.69** vs `MRK` **15.99**; `MRK` P/B 8.98 vs `PFE` 1.88. **`MRK` trades at 98.7% of its 52w high and 4.1% above consensus mean; `PFE` at 97.6% and at consensus** |
| **§E Refutation + catalyst** | 🚨🚨 **The strongest refutation on this sheet: `MRK` — the sector's only 🟢, at RSI 86.7 on the upper band — carries 0q revisions of 1↑/5↓ over 30 days and 2↑/10↓ over 7 days.** Price and estimates are moving in opposite directions on the name that *is* the sector's breadth. ⚠ And `S82`'s driver and `MRK`'s flow are **the same trial** ⇒ `n≈1` (`B3`). Next ER **10-29** — no dated catalyst inside two weeks |

### §B-FIN — Financials (N−) · rotating track

**Candidates**: `JPM` `BAC` `C` (the uniform bank shape) · `HOOD` (**delta +1.230, largest of 299**) ·
`SCHW` (rs60 +29.1) · `ICE` (obv +0.411) · held `KKR` `NDAQ` `MET`.
**Screener contributed `HIG`** (leader pullback, RSI 30.4) and **`AFL`** (washout, **RSI 18.0**).

| | |
|---|---|
| **Thesis** | Not one thesis — **three businesses** (`SECTOR_DEEP_FIN`): six of six large banks accumulating into a 20-day de-rate on a curve that steepened **~24bp/20d** against the Treasury's own stated intention; five of nine reds are insurers; the only green is bitcoin beta |
| **Freshness** | `[ALPHA]` |
| **§C Flow** | Banks: `JPM` obv **+0.308** / rs20 −4.1 / rs60 +15.4 · `C` +0.297 / −4.0 / +3.0 · `BAC` +0.247 / −4.2 / +18.7 — **6 of 6 same sign pattern**. `NDAQ` FINRA **z −1.67 🟢 covering**; `MET` z +0.42 🟡; `SCHW` z **+1.15 with 5v5 +8.1▲** |
| **§D Competition** | `HOOD` **P/S 19.71, fwd P/E 33.29** against `SCHW`/`ICE` — the flow leader is the most expensive expression of it. `AFL` at **RSI 18.0** is the sector's washout candidate and is 🔴 on flow (−0.700, obv −0.252) — **washout ≠ turn**, and no turn is claimed |
| **§E Refutation + catalyst** | The bank case dies if **`HY OAS` ≥ 2.95** (`P88` branch B) — i.e. if this stops being a duration story and becomes a credit one. `S112` settles **08-31** (branch A = the duration complex rips ⇒ the steepener reverses). ⚠ **`MET` is `module_report_tags`-unindexable (`M152`)** — its coverage cannot be reconciled by that instrument at all |

### §B-INDU — Industrials (UW−) · rotating track

**Candidates**: `TRI` (sector's best flow +0.711) · `ADP` · `AXON` (**rs60 +58.4, sector's highest**) ·
held `RTX` · `ETN`.
**Screener contributed `LHX`** (de-rate snapback, RSI 40.6) and **`HON`** (washout, RSI 22.6).

| | |
|---|---|
| **Thesis** | 🚨 **The carried defense thesis is downgraded by this run's own measurement.** `M704` re-run: EW{LMT,NOC,GD,RTX,LHX} exc5 **−4.775** → ex-`LHX` **−4.162**, a change of **+0.614pp**. **`S97`'s discontinuity explains 13% of the weakness; the other 87% is every other prime.** All six legacy primes carry negative one-session deltas |
| **Freshness** | `[ALPHA]` |
| **§C Flow** | `RTX` obv **+0.023 — it has LEFT accumulation**, delta **−0.304** (book's largest). ⚠ **`C11`: the two OBV instruments disagree on `RTX`** — sweep level +0.023 neutral vs chart rate **분배 −71%** — which `HANDOVER §8` shows is the signature of a *decelerating* name. Short axis **fully inverted in one session**: `LHX` z **−2.99 🟢** (was +1.35 on 08-21), `RTX` **−2.15 🟢** ⇒ **shorts covered INTO the decline** |
| **§D Competition** | `AXON` is the sector's only positive-flow defense name (**+0.494**, rs60 +58.4) and it moves opposite to all five legacy primes. ⚠⚠ **`D305` binds: `module_fundamentals_us AXON` returns the WRONG company name (`Axovant Sciences`) with correct numbers — the name is not quoted from that tool.** Actual leadership is node ⑤: `TRI` +0.711, `ADP` +0.633, `PAYX` +0.450 — **payroll and information services, which no thesis on this board is about** |
| **§E Refutation + catalyst** | `RTX` chart: **Bollinger coiling at 7.9%, the tightest in this run's set**, RSI 41.5, at the lower band; **trigger close > 217.94 · swing-low stop 209.91**. ⚠ **`W4` unpaid — `RTX`'s customer is unmeasured for 205 days.** `TRI`'s revisions are **inverted** (0q 1↑/11↓ vs +1q 11↑/1↓) |

### §B-IT — Information Technology (UW) · PREMORTEM-promoted 5th

**Candidates**: **`ORCL` (the run's one admitted chain-hop name)** · `NOW` (obv +0.509) ·
`INTU` (+0.458) · `CRM` · `PLTR` (**rs20 +42.8, highest of 299**) · `LITE` (delta +0.236) · `MRVL` ·
held `ANET` `AVGO` `NVDA` `HPE`.
**Screener contributed `APP`** (washout, RSI 22.1, px/200 **−39%**).

| | |
|---|---|
| **Thesis** | The UW is priced at the mega-cap layer and unsupported at breadth: `eqflow` rank **8** vs price rank **11**, `eqflow − wflow` **+0.129**, the board's widest positive gap. **Software carries the sector's two highest `obv_norm`.** The sector enters `NVDA` **08-26** from the **12th %ile of 252** (`SMH` exc5 −3.293) with `Nasdaq-100` spec at the **4th %ile** — 🚫 positioning, **context not a trigger (`D6`)** |
| **Freshness** | `[ALPHA]` |
| **§C Flow** | 🚨 **`ANET` (held) is this run's ONLY 🔴 short axis of 25 probed: FINRA z +1.82, short% 51.9 vs base 42.2, 5v5 +3.9▲** — on the book name that improved most on flow (delta +0.384). **Flow improving and short pressure spiking on the same settled bar.** Counter-readings: `AVGO` z **−2.53 🟢**, `HPE` 5v5 **−14.8▼**, `NVDA` +0.41 🟡 |
| **§D Competition** | **`ORCL`: fwd P/E 13.42, PEG 0.81 — the lowest on this sheet — at 42.4% of its 52w high, with consensus mean 246.43 (+68% to spot).** OBV **+0.380 accumulating**, `rs20` **+23.8**, `rs60` **−25.3** ⇒ the exact *"OBV accumulating, RS not yet up"* shape `chain-hop` defines as its alpha. ⚠ `vol_surge` **0.60** ⇒ it can never be 🟢 under the current gate. 🚫 **Its 19↑/6↓ revision breadth is NOT independent evidence — it is an IT name and that is where `measure_ic`'s confound lives** |
| **§E Refutation + catalyst** | **`S113` settles 09-01** (branch A `SMH` exc5 ≥ +4.461 falsifies the UW; branch B pre-declared LOW-INFO). `P79` settles **08-25** at −5.609, having moved **away** from branch B. `S94` **08-31**. 🚨 **`D315`: `--positioning NVDA` returns the 08-24 D2 expiry for an 08-26 event ⇒ `S103`'s bands stay hand-set and are NOT re-frozen (`D242`)**. **`ORCL` next ER 09-11 — the only dated single-name catalyst on this sheet inside three weeks** |

### §B-CROSS — LIVE_SHORTLIST names outside the DEEP sectors

`TGT` (Consumer Staples) · `ECL` (Materials) · `MSI` (IT, already above) · `COIN` (FIN, above) ·
`MSTR` (IT, above) · `MRK` (HLTH, above).

| Name | §A / §C | §E refutation |
|---|---|---|
| **`TGT`** | 🟢 +0.950, obv +0.292, rs60 +26.9, surge 1.51; **at 100.0% of its 52w high**, 3.2% above consensus; revisions 0q **7↑/0↓** | 🚨 **`P84`: its Q2 beat contained $1.65 of $4.11 EPS = 40.1% tariff refund.** And **`S93` VOIDed on a tariff clause that named `WMT` and `TGT` by name.** `W5`: `TGT` +8.463 vs `WMT` −8.669 exc5 = **17.1pp intra-sector** |
| **`ECL`** | 🟢 +0.606, obv +0.169, rs20 **+1.2 (barely positive)**, surge 1.40; fwd P/E 29.90, consensus **+15.4% above spot** | **The weakest green on the board** — it clears `rs20` by 1.2 points. A single down session removes it from the green set. Revisions mixed (7↑/6↓) |
| **`MSI`** | 🟢 +0.806, obv +0.218, rs60 +15.5, surge 1.25; **+1q revisions 11↑/0↓, the cleanest on the sheet** and **not** an IT-confound business | fwd P/E 25.18 with **P/B 29.76**; consensus +8.8%. No dated catalyst before **11-06** |
| **`COIN` / `MSTR`** | ★ **ONE risk unit in two GICS labels** — both bitcoin beta (08-21 finding, reproduced). `COIN` obv +0.289 rs60 **+5.3**; `MSTR` obv +0.361 rs60 **−24.7**, short **8.9% float covering**, implied **±9.0% (D6)** | 🚨🚨 **`COIN`'s revisions are 0↑/17↓ in BOTH horizons over 30 days** — the worst on the sheet, on the board's joint-highest flow score. `MSTR`'s **fwd P/E 2.41 / P/S 95.07** is a bitcoin-mark artifact, not a valuation |

---

## §C · Epicenter-starter module — **no cycle GAP flagged, and the reason that matters more**

`CYCLE_EXPOSURE`: AI-compute rank 1 **16.52% ≥ 12.0% ✅** · Energy/refining rank 2 **9.84% ≥ 8.0% ✅** ·
missile-defense rank 3 **3.79%, ⚪ no floor set**. **No top-rank GAP ⇒ no starter module is required.**

🚨 **But `PREMORTEM §5` attacked that ✅ three ways and BET carries the result forward as a
MEASUREMENT gap, not a size:**
1. **Rank 3 has no floor, so it cannot fail** — and the one name there (`RTX`) was tagged
   **ROLLING OVER** by lens 3 this run. **An unset threshold is a silent pass.**
2. **`cycle_registry.json` has no optical/interconnect row for a 10th run** ⇒ that exposure is
   **unmeasurable, not zero**, on the week `Fabrinet` guided multi-year demand while `S86`/`S96` both
   settled branch B.
3. ★★ **The AI-compute ✅ is carried at the COMPUTE layer while the week's committed capital went to
   POWER** — `NVDA` guaranteeing **up to $105bn** of OpenAI's Ohio leases (8-GW campus) — and **every
   measurable power-layer name is 🔴**: `GEV` −0.741, `CEG` −0.625, `VRT` −0.539, `NEE` −0.600,
   `VST` −0.689. **`ETN` cannot be counted there** (`M778`: β`XLI` +1.402 t +6.12).
⇒ **The sheet's honest statement: the desk cannot currently measure whether it owns the layer where
the money was committed.** No size is proposed on that (P4).

⚠ **`G4` binds every concentration sentence on this sheet**: 250d gives **11** units and 500d gives
**11** units **with different membership**, 750d gives 10. **`MPC` + `PSX` is one unit in all three
windows** and is the only grouping quotable without a window caveat.

---

## §D · Names set aside — filed to the ledgers, both fields attached

**Rejections filed (`reject_ledger.py add`, `--stage BET`, each with `--revives-if` AND
`--recheck-date` — the script will not run without both). All four took class `A.flow미도착` from the
ledger's fixed enum: in every case a SETUP existed and the FLOW had not arrived, which is the same
defect and should be scored as one class rather than split by cosmetic wording:**

| Ticker | Class | Why (one line) | Revives if | Recheck |
|---|---|---|---|---|
| `AFL` | `A.flow미도착` | Screener washout at **RSI 18.0** but flow is 🔴 **−0.700** with `obv_norm` −0.252 — washout is not a turn | `obv_norm` turns ≥ 0 **AND** `rs20` vs `SPY` > 0 on a settled close | 2026-09-19 |
| `HON` | `A.flow미도착` | Screener washout RSI 22.6 but the sector's **worst flow** at −0.865, rs20 −14.8, rs60 −13.1 | `obv_norm` ≥ 0 on a settled close **AND** `rs60` vs `SPY` > −5 | 2026-09-19 |
| `NEE` | `A.flow미도착` | `chain-hop` candidate that **failed the flow cross-check**: 🔴 −0.600, `obv_norm` −0.205 distributing | `obv_norm` turns ≥ 0 **AND** it reappears as a `chain-hop` candidate on the AI-power theme | 2026-09-19 |
| `CEG` | `A.flow미도착` | Same — `chain-hop` candidate, flow 🔴 −0.625, `obv_norm` −0.268 | `obv_norm` ≥ 0 **AND** `EW{GEV,CEG,VRT}` exc5 vs `SPY` ≥ 0 | 2026-09-19 |

⚠ **`T25` honoured**: the rejection ledger's measured loss asymmetry is re-printed beside these —
**67% of past rejections changed nothing, and the loss tail ran 2.2× the gain tail (+83.8pp vs
−38.4pp)**, almost all of it from two rows filed without a revival condition. **All four rows above
carry both fields.**

**Misses filed (`missed_ledger.py add`) — names that surfaced upstream and did NOT make a section:**

| Ticker | Class | Enters if | Recheck |
|---|---|---|---|
| `APP` | `Q.확신부족` | `rs20` vs `SPY` > 0 **AND** `obv_norm` ≥ 0 on a settled close (washout RSI 22.1, px/200 −39%, IT) | 2026-09-19 |
| `ISRG` | `Q.확신부족` | `obv_norm` ≥ +0.15 **AND** `rs60` vs `SPY` > 0 (de-rate snapback, px/200 −20%) | 2026-09-19 |
| `HIG` | `U.발굴부재` | Financials takes a DEEP slot again **AND** `HIG` appears in the LIVE shortlist, **OR** `obv_norm` ≥ +0.15 with `rs20` > 0 | 2026-09-19 |

⚠ **`FRO`/`STNG`/`INSW` are deliberately NOT filed** — they are outside `us_top300`, so a row could
not resolve on any market outcome (the **`FSLR` defect**, P5). **Registered as universe dig `D314`
instead** (EVENT_ALPHA §4).

---

## §E · What this sheet does NOT say

- **No buy, no sell, no size.** Every number above is a state, not an instruction (P4).
- **No concentration figure as a single number, and today not as a single count** (`G4`).
- **No claim that any 🟢 is news-confirmed** — the velocity axis is `null` on all 299 names.
- **No `EA` reading** — unmeasurable for a 10th run.
- **No revision-momentum claim used as a leading indicator**, and none used as independent evidence on
  an IT name (`ORCL`, `ANET`) — that is precisely where `measure_ic`'s control located the confound.
- **No "peak margin must collapse" claim on `MPC`/`PSX`** — the escape-hatch rule makes that a
  contractual question and **the filing is 3 runs unread**.

---

## §F · ALPHA freshness gate — every §B `[ALPHA]` placeholder filled

> Written by Stage 10 (L1·ALPHA). `theme-age … --scope foreign`, hand-issued **22:5x KST**, vector
> index synced **2026-08-22 21:54**. ⚠ **Multi-word terms are excluded** — the tool splits them and
> measures only the last token (`M68`, 4 of 7 collapsed this run). **Only single-token readings below.**

### F-1 · 🚨 The pipe was checked BEFORE the zero was read (the mandatory `G1` probe)

The stage forbids writing *"F1 is arithmetic"* without falsifying the instrument first. **Done, twice:**
1. **`G1` falsification probe, 22:14 KST** — the 40 names the sweep marked silent returned
   **40 / 40 valid in 18.1 s**; the CLI answered **3536** before and after the sweeps.
2. ★ **A same-run positive control for the age readout**: `theme-age Cloverleaf` returns
   **age 60, 18.21×, n 22** — **an uncapped age below 90 and the run's highest acceleration.**
   ⇒ **The `>=90` readings below are real ages, not a ceiling.** (The 08-21 run produced the same
   control with `Treasury buybacks`, age 2; today's is independent.)

⇒ **F1 — zero 🟢LIVE for an 11th consecutive US run — is ARITHMETIC, and it is provable today.**
🟢FRESH needs **age ≤14d AND accel ≥2×**; **every theme this desk's bets ride is ≥90 days old.** The
conjunction, not the tool, is what fires zero.

### F-2 · Tags

| Bet / theme | `theme-age` | Tag | Evidence label + date | Residual / re-check |
|---|---|---|---|---|
| **HLTH — the mRNA/oncology decoupling** (`MRK`) | **`mRNA` 🟡ACCELERATING, 5.19×, 7d avg 26.3, n 422 — the highest acceleration of any bet theme this run** | **🟡 PARTIAL** | `S82` FIRED-A on a dated driver (`M776`, 08-19, `XLV` +3.51%); theme measured 22:5x KST 08-22 | 🚨 **Residual, and it is large: `MRK`'s own revisions are 1↑/5↓ (30d) and 2↑/10↓ (7d) while it trades at 98.7% of its 52w high, 4.1% above consensus, at RSI 86.7.** The theme accelerates and the estimates fall. **Re-check 2026-08-28** (`S112` window opens) |
| **ENRG — refining-capacity destruction** (`MPC` `PSX` `VLO` `COP`) | `refining` ⚪ECHO **0.98×**, 92.9/day, n 4,533 · `Hormuz` ⚪ECHO **0.80×**, 141.9/day, n 9,199 | **🟡 PARTIAL** | `P69`/`S95` FIRED-A (`BZ=F` 94.39); `P66` re-confirmed 08-21 (Lukoil strike) | ⚠ **ECHO/FADING theses need STRONGER live evidence to survive, and this one just LOST an instrument** (`P70` MISSED). **Residual = `P89` at the 08-28 close** (`BZ=F` ≥ 93.00 ∧ distillate crack ≥ 98.0). **Re-check 2026-08-28** |
| **FIN — the curve/credibility bid** (`JPM` `BAC` `C`) | `Bessent` **🟡ACCELERATING 3.01×**, 69.9/day, n 1,310 | **🟡 PARTIAL** | `[FRED 08-20]` 30y−2y widened ~24bp/20d; BBH body-read 08-20 12:11 GMT | Residual = **`P85` and `P88` at the 08-28 close**. ⚠ **Momentum-only flag does NOT apply** — the bank shape is `obv_norm` ≥0 with `rs20` <0, i.e. accumulation *without* momentum, the opposite pattern. ⚠ **`D6` grade C**: the accumulation read is OBV-only, so the six-name uniformity is the claim, not any single name. **Re-check 2026-08-28** |
| **IT — the chain-hop name** (`ORCL`) | `interconnect` ⚪ECHO **0.98×**, 28.7/day, n 1,481 | **🟡 PARTIAL** | `chain-hop "data center power"` 08-22: prox 3 / body 16, title-unnamed; **passed the flow cross-check** (obv **+0.380**, rs20 +23.8, rs60 −25.3) | Residual = its **09-11 earnings**, the only dated single-name catalyst on this sheet inside three weeks. ⚠ **Momentum-only flag: NO** — RS20 is green and OBV *agrees*, so this is not a tape trade. 🚫 Its 19↑/6↓ revisions are **not** independent evidence (IT confound). **Re-check 2026-09-11** |
| **IT — the optical node** (`LITE` `COHR` `CIEN`) | `interconnect` ⚪ECHO 0.98× | **🔴 RESOLVED on the money axis / re-filed on the story axis** | `S86` **FIRED-B** (−7.050) and `S96` **FIRED-B** (−7.412), both scored 08-22 | ⚠ **NOT dropped, and no rejection row is filed** — the stage's own rule makes DEAD a *both-axes* verdict, and `LITE`'s `obv_norm` is **+0.174 accumulating** with all three deltas positive. **Re-filed with a new thesis line in `EVENT_ALPHA` CARD 8. Re-check 2026-08-31 (`S94`)** |
| **MATR — gold** (`NEM`) | no admissible single-token theme; `GLD` 5d **+5.450 = 94th %ile** used instead | **🟡 PARTIAL** | `S89` **FIRED-B** (exc5 +13.104); gold spec **48th %ile** `[COT 08-18]` | 🚨 **Momentum-only flag: STAMPED.** `M779` puts **246.4% of `NEM`'s rs60 in the last 20 sessions** (days 21–60 negative) ⇒ RS/volume green on a losing base. **Hard stop required** if ever expressed. ⚠ Positioning gate: **P/C 0.17, skew +0.1 — nobody is hedged.** **Re-check 2026-08-28** (`P87`) |
| **CROSS — bitcoin beta** (`COIN` `MSTR`) | `bitcoin` ⚪ECHO **1.26×**, 165.3/day, n 6,187 | **🔴 RESOLVED for `COIN` on the estimate axis / 🟡 for `MSTR`** | 08-21 head cluster, 12 outlets, +20–25% weekly | 🚨🚨 **`COIN`: 0↑ / 17↓ revisions in BOTH horizons over 30 days**, on the joint-highest flow score of 299 names. **Positioning gate: `MSTR` short 8.9% float covering, DTC 1.8, implied ±9.0% (D6) ⇒ ⚡ squeeze fuel, never a standalone buy — hard-stop stamp.** ★ **They are ONE risk unit in two GICS labels.** **Re-check 2026-08-31** |
| **STPL — the big-box split** (`TGT`) | `tariff` ⚪ECHO 1.06×, 211.1/day, n 9,567 | **🟡 PARTIAL** | Revisions 7↑/0↓ (30d); flow +0.950, rs60 +26.9 | 🚨 **Residual is `P84`: $1.65 of $4.11 EPS = 40.1% tariff refund**, and **`S93` VOIDed on a tariff clause that named `WMT` and `TGT` by name.** At **100.0% of its 52w high**, 3.2% above consensus. **Re-check 2026-09-03** (`P84`) |
| **MATR — `ECL`** | `steel` ⚪ECHO 1.02×, n 2,420 *(nearest available single token; `ECL` is specialty chemicals, so this is context, not its theme)* | **🟡 PARTIAL** | 🟢 tag, +0.606, surge 1.40 | **The board's weakest green — `rs20` +1.2 vs `SPY`.** One down session removes it from the green set. **Re-check 2026-08-29** |
| **IT — `MSI`** | no admissible single-token theme | **🟡 PARTIAL** | 🟢 +0.806, surge 1.25, **+1q revisions 11↑/0↓ — the cleanest on the sheet and NOT an IT-confound business** | No dated catalyst before **11-06** — that IS the residual. **Re-check 2026-09-05** |

**Tag totals: 🟢LIVE 0 · 🟡PARTIAL 8 · 🔴RESOLVED 2** (`COIN` on the estimate axis; the optical node on
the money axis, **re-filed not dropped**).

### F-3 · 🔴 handling — and why **no** rejection row was filed from this stage

- **The optical node** is 🔴 on money and **alive on story** (`LITE` accumulating, three positive
  deltas, `Fabrinet` guiding multi-year demand). **The stage's own rule makes DEAD a both-axes
  verdict**, so it is **re-filed with a new thesis line and a dated re-check (08-31)**, not dropped.
- **`COIN`** is 🔴 on the **estimate** axis only; its flow is the joint-highest of 299 names.
  **A rejection row here would be a verdict this desk cannot support**, so the finding is written as
  a residual with a hard-stop stamp instead.

⇒ **The 4 rejection rows filed this run all come from BET §D, not from ALPHA.** **No 🔴 was dropped
without a row, because no 🔴 was dropped.**

### F-4 · Carry-forward list — **independent of whether the sector holds a DEEP slot next run**

`MRK` · `PFE` · `MPC` · `PSX` · `VLO` · `COP` · `XOM`(control) · `JPM` · `BAC` · `C` · `HOOD` ·
`ORCL` · `LITE` · `COHR` · `CIEN` · `NEM` · `COIN` · `MSTR` · `TGT` · `ECL` · `MSI` · `TRI` · `AXON` ·
`RTX` · `ANET` · `NUE` · `STLD`.

⚠ **Listed explicitly because several of these sectors will lose their DEEP slot under the recency
rule next run**, and the measured failure mode is precisely a name going untracked when its sector
rests (**+12.3% over five sessions, unowned**).

### F-5 · Obligations closed and opened by this stage

- ✅ **`APH` CLOSED — the pre-commitment held.** The 08-21 packet wrote that it *"must not cross a
  second HANDOVER unresolved"*; `missed_ledger.py resolve --outcome entered` was called this run.
  **OR-leg 1 met as written** (IT took a DEEP slot **and** `SECTOR_DEEP_IT.md` names the *interconnect*
  chain node), with the **honest caveat recorded rather than laundered**: the node named is populated
  by the optical names and **`APH` itself was not mapped into it**. OR-leg 2 fails cleanly
  (`vol_surge` 0.85 < 1.20). Corroboration only: `APH` delta **+0.435**, among the largest positive
  one-session flow moves of the 299.
- ⚠ **`009830` 한화솔루션 remains the ledger's one open past-due row** — KR-owned, and **the KR desk
  could not measure it either** this morning (`SECTOR_FLOW_KR.json` returned `scored: 0`). **Named,
  not dropped**; it belongs to `industry_kr`.
- 🚨 **`D295` is UNMET for a THIRD run — and this run converted it from a lapse into a diagnosed tool
  defect (`D315`)**: `--positioning NVDA` selects the **08-24 (D2)** expiry for an **08-26** event.
  `S103`'s bands stay hand-set and are **not** re-frozen (`D242`); **`S113` is the additive repair.**
- 🚨 **`D294` reproduced a FOURTH time** — `action_bracket` printed *"Nearest binary: NVDA earnings
  (D-4)"* and *"no dated binary in window"* in consecutive lines, and emitted **zero tickets** on a
  window holding **three** binaries. **`ACTION_TICKETS.md` was hand-built**; the raw output is
  preserved at `industry_US/_action_bracket_raw.md`.
