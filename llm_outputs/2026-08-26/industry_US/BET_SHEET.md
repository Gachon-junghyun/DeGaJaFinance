# BET_SHEET — industry_US · 2026-08-26 (Stage 6 / L1·BET)

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split it.
> **Zero buy/sell recommendation, zero sizing (P4).** Any fraction that appears anywhere is
> **"mechanical 1/4 — IC not yet estimable (G6 FAIL)"**, never an evidence-backed size.
> Price: equal-weight `us_top300`, excess vs **`SPY`**, **settled 2026-08-25**.
> Flow: 2026-08-26 sweep ⚠ **pre-market bar — `vol_surge` structurally depressed on every row (`D355`)**.
> **`src=` provenance tag on every §B candidate** (convention registered by the sibling desk 2026-08-26;
> adopted here so *"how many DEEP observations did BET actually use?"* becomes one `grep`).

---

## §0 · Thesis-confirmation gate — the scoreboard was consulted FIRST, and it is empty for this desk

`REPORT/COMPANY_SCOREBOARD.md` (2026-08-21, `company_batch` run 1) holds **5 rows, all KR**
(`036460` `011200` `316140` `028050` `000660`). ⇒ **ZERO of this sheet's candidates carries a
scoreboard row.** Every name below is **RE-DERIVED**, and the failing confirmation test is the
trivial one — **no row exists**.
⚠ **"No row ≠ no coverage"**, so `module_report_tags ticker <T>` was run on all eight finalists:

| Name | Last report covering it | Age |
|---|---|---|
| `MRVL` · `KLAC` | `2026-07-15/industry_US/SECTOR_DEEP_SEMI.md` | **42 days** |
| `ORCL` | `2026-07-15/industry_US/SECTOR_DEEP_IT.md` | 42 days |
| `COIN` · `MRK` | `2026-07-17/industry_US/SECTOR_DEEP_{FIN,HLTH}.md` | 40 days |
| `HOOD` | `2026-07-12/industry_US/SECTOR_DEEP_FIN.md` | 45 days |
| `VLO` | `2026-07-15/ACTION_TICKETS.md` | 42 days |
| **`MSTR`** | 🚨 **no report has ever covered it** | — |

🚨 **The ledger index itself was last rebuilt 2026-07-21T18:58 — 36 days ago** (`HANDOVER §6a`), so
these ages are a **floor**, not a measurement: five weeks of desk output are absent from it.
**Every age above is therefore ≥ the number shown**, and the `MSTR` "never covered" line is the one
that most likely reflects the index rather than reality. **Stated rather than trusted.**

---

## §A · Numbers — cross-checked, blanks left blank

> Consensus/valuation from `module_fundamentals_us` (yfinance + SEC XBRL). Revision columns are a
> **description of the denominator's direction** (arithmetic, valid) and **NOT a leading indicator** —
> `measure_ic.py` found two non-overlapping windows disagreeing in sign, resolving to an
> **Information-Technology loading**. **They are never used here as a timing signal**, and on the IT
> names (`MRVL`, `ORCL`, `KLAC`, `MSTR`) they carry that confound explicitly.

| Name | Sector | Fwd P/E | PEG | Upside to mean tgt | **CY consensus, 90d** | **NY consensus, 90d** | Near-term breadth |
|---|---|---:|---:|---:|---:|---:|---|
| **`HOOD`** | FIN | 34.05 | 2.45 | **+8.5%** | 1.88 → **2.07 = +10.2%** | 2.50 → **2.70 = +8.2%** | positive all 4 periods |
| **`MRVL`** | IT | 38.12 | **1.40** | +10.6% | 3.83 → **4.06 = +5.9%** | 5.52 → **6.25 = +13.2%** | positive all 4 |
| **`KLAC`** | IT | 27.19 | 1.76 | **+27.7%** | 5.02 → **5.45 = +8.6%** | 5.91 → **6.60 = +11.7%** | positive all 4 |
| **`ORCL`** | IT | **13.63** | **0.83** | **+65.7%** | 8.03 → 8.05 = **+0.3%** | 10.71 → 10.91 = +1.9% | flat-positive |
| **`COP`** | ENRG | 13.88 | 1.07 | +9.9% | 9.82 → **10.44 = +6.3%** | 9.15 → 9.53 = +4.1% | positive all 4 |
| **`MRK`** | HLTH | 16.19 | 10.47 | 🚨 **−4.4% (ABOVE mean target)** | 2.74 → 2.75 = +0.4% | 9.52 → 9.54 = +0.2% | ⚠ current-qtr **−4.2%** |
| **`VLO`** | ENRG | **11.16** | 4.08 | 🚨 **−8.4% (ABOVE mean target)** | 28.14 → **43.60 = +54.9%** | 19.99 → **30.64 = +53.3%** | positive all 4 |
| **`COIN`** | FIN | **63.93** | **10.58** | +6.4% | 🚨 **+1.01 → −2.06 = −303.5%** | 4.91 → **2.89 = −41.1%** | 🚨 negative all 4 |
| **`MSTR`** | IT | 🚨 **2.52** | 2.85 | **+83.8%** | 🚨 **43.82 → −6.69 = −115.3%** | 14.27 → **3.97 = −72.2%** | 🚨 negative all 4 |
| `EQIX` | RE | 57.83¹ | — | +14.2% | 17.75 → 17.88 = +0.8% | 19.22 → 18.69 = −2.8% | **1↑/3↓** both periods |
| `DLR` | RE | 66.99¹ | — | +15.3% | 2.97 → **3.35 = +12.9%** | 2.86 → 2.89 = +0.9% | 0↑/1↓ both periods |
| `CCI` | RE | 26.48¹ | — | **+24.3%** | 2.39 → 2.31 = **−3.6%** | 2.95 → 2.89 = −2.3% | **1↑/3↓** both periods |
| `MPC` · `PSX` (held) | ENRG | — | — | — | — | — | carried from 08-25, not re-pulled |

<sub>¹ 🚨 **GAAP multiples on REITs are a category error and are printed for tool continuity ONLY.**
The desk has logged this exact trap twice (`DLR` GAAP 67.87 vs **24.4× on AFFO**; `VTR`'s "−33.3% cut"
that was **~1.6% of FFO**). **No REIT is called cheap or expensive on these numbers.**</sub>

### ★★★ The sheet's headline is an arithmetic asymmetry, and it runs THROUGH this run's own hand-offs
**Sort the sheet by the denominator's direction and the CONFIRMED-EARLY names split cleanly in two:**

| | Rising denominator | **Collapsing denominator** |
|---|---|---|
| Names | `HOOD` +10.2% · `MRVL` +5.9% · `KLAC` +8.6% · `COP` +6.3% · `VLO` +54.9% | **`COIN` −303.5%** · **`MSTR` −115.3%** |
| Their multiple | 27–38× (`VLO` 11.2×) | **`COIN` 63.9× · `MSTR` 2.52×** |
| Their flow rank | 2nd, 5th, 6th, — , — | **1st and 2nd on the entire 299-name board** |

🚨 **`M956`: the two names with the highest flow scores in the universe are the two names whose
consensus has been cut to a loss.** `COIN`'s current-year estimate went **+1.01 → −2.06** and
`MSTR`'s **+43.82 → −6.69** over ninety days.
🚨 **And `MSTR`'s 2.52× forward P/E is the `L2` peak-multiple trap in its purest form** — the multiple
is low **because the denominator is collapsing**, not because the price is. Put next to a **+83.8%**
consensus upside, that is a consensus that has not finished marking down.
⇒ **This refutes BOTH of `EVENT_ALPHA` Card 4's hand-offs**, two stages after they were made
(`SECTOR_DEEP_FIN §1` caught `COIN`; `MSTR` is caught here). **Written down, not edited away (`D48`).**

⚠ **The mirror case, stated so the rule is applied symmetrically**: **`VLO`'s 11.16× forward is the
SAME shape** — low because current-year consensus was revised **+54.9% in ninety days** — and it
trades **8.4% ABOVE its mean target**. **`VLO` is not cheap. It is a peak-denominator refiner**, and
`L2` applies to it exactly as it does to `MSTR`. **The two names differ in the SIGN of the revision,
not in the shape of the trap.**

---

## §B · Candidates by sector — thesis + `src=` provenance + freshness

> 🚫 **FRESHNESS: every row reads `UNMEASURED (G1 FAIL)`.** `vel_coverage` **17.06% vs an 80% bar**,
> and this run additionally established the cause is a **hard cap at `us_top300` ranks 1–51**, not a
> pipe drop (`M947`). **No row says `stale`, `cold`, or `quiet`** — those would claim a measurement
> that was not taken.

### §B-1 · Energy (DEEP, continuous)

| Name | `src=` | Thesis, one line | Freshness |
|---|---|---|---|
| **`VLO`** | `src=DEEP_ENRG` | The only pure refiner the book does not own: `rs60 +33.6`, `exc20 +10.51`, OBV 매집, and the **smallest** negative flow delta cohort in a sector where E&P deltas ran −0.52 to −0.57. ⚠ **But §A shows it is a peak-denominator name trading above target** | `UNMEASURED (G1 FAIL)` |
| **`COP`** | `src=DEEP_ENRG` | The sector's **#2 flow score (+0.519)** and the only E&P name reading OBV 매집; `exc20 +12.17` matches the refiners while its delta (−0.09) is an order of magnitude smaller than its four E&P peers | `UNMEASURED (G1 FAIL)` |
| `MPC` · `PSX` | `src=DEEP_ENRG` (**HELD**) | Highest and third-highest flow of all 11 holdings; **`exc20` +12.57 / +11.70**, `exc60` +41.41 / +33.45 | `UNMEASURED (G1 FAIL)` |

### §B-2 · Health Care (DEEP, continuous)

| Name | `src=` | Thesis | Freshness |
|---|---|---|---|
| **`MRK`** | `src=DEEP_HLTH` | The sector's **only 🟢**, first on all four price windows, and **one of only four names on the 299-name board with `vol_surge` > 1.15 on a 2.48%-volume bar**. ⚠ **The 08-25 carried claim is now RE-VERIFIED this run: −4.4% upside = it trades ABOVE its mean consensus target**, with current-quarter revisions **−4.2%** | `UNMEASURED (G1 FAIL)` |

### §B-3 · Real Estate (DEEP, rotating R1)

| Name | `src=` | Thesis | Freshness |
|---|---|---|---|
| `EQIX` · `DLR` | `src=DEEP_RE` | The sector's **two largest positive flow deltas (+0.28, +0.31)** and the only two names flat-to-positive on `exc60` — **against near-term revision breadth of 1↑/3↓ and 0↑/1↓.** Money in, estimates out | `UNMEASURED (G1 FAIL)` |
| `CCI` | `src=DEEP_RE` | The sector's **widest consensus upside (+24.3%)** against its **worst `exc60` (−17.87)** — and the only RE name whose multiple is not a GAAP category error. ⚠ Revisions −3.6% CY, 1↑/3↓ | `UNMEASURED (G1 FAIL)` |

### §B-4 · Financials (DEEP, rotating R2)

| Name | `src=` | Thesis | Freshness |
|---|---|---|---|
| **`HOOD`** | `src=DEEP_FIN` (**ADDED by DEEP**) | ★ **The clean expression of the sector's only agreeing node**: `exc5 +22.66` / `exc20 +17.46` / `exc60 +17.62` — **positive on all three, which `COIN` is not** — `vol_surge` **1.06**, `rs20 +17.5 / rs60 +20.3`, **positive revisions on all four periods**, with the C-grade OBV 매집 agreeing (**RULE D6** — four non-OBV axes carry this row), revenue **+32.25% YoY with SEC XBRL cross-checking yfinance at 0.0% difference on every comparable quarter** | `UNMEASURED (G1 FAIL)` |
| **`COIN`** | `src=EVENT_ALPHA` → **AMENDED by `DEEP_FIN`** | Board's #1 flow (+0.978) and #1 `vol_surge` (1.56). 🚨 **Carried ONLY with its denominator attached**: CY consensus **+1.01 → −2.06 (−303.5%)**, trailing EPS **−$3.87**, **63.9× forward / PEG 10.58**, and **`exc60 −2.24`** ⇒ **no 60-day trend under the 5-day move** | `UNMEASURED (G1 FAIL)` |

### §B-5 · Cross-sector LIVE shortlist names (outside the DEEP sectors)

| Name | `src=` | Thesis | Freshness |
|---|---|---|---|
| **`MRVL`** | `src=SWEEP` + `EVENT_ALPHA` | ★ **The only CONFIRMED-EARLY hand-off whose denominator is RISING** (+5.9% CY, **+13.2% NY**, positive all four). 🟢가속, OBV 매집, **`rs20 +41.7` = the board's best**, ✅ low-short/short-cover (FINRA `z −1.11`). **Prints TOMORROW 08-27**; `S116` brackets it at ±12.0pp against an implied **±10.3%** ⇒ thresholds outside the priced move | `UNMEASURED (G1 FAIL)` |
| **`ORCL`** | `src=SWEEP` | 🟢가속, OBV 매집, **the cheapest 🟢 on the board (13.63× fwd, PEG 0.83) with the widest upside (+65.7%)** — against **`rs60 −40.5`, the worst 60-day of any green**, and `vol_surge` **0.41**, the lowest of the six. ⚠ **PREMORTEM re-tagged it NOT-A-RUNNER: a reversal, not continuation** | `UNMEASURED (G1 FAIL)` |
| **`KLAC`** | `src=SWEEP` | 🟢가속, OBV 매집, revisions **positive on all four** (+8.6% CY, +11.7% NY), +27.7% upside. ⚠ **The run's single `new_green`, and its ignition is UNREADABLE** — `vol_surge` **0.56** on a bar carrying 2.48% of normal volume. **The 🟢 is carried; the "ignition" is not** | `UNMEASURED (G1 FAIL)` |
| **`MSTR`** | `src=EVENT_ALPHA` → **REJECTED here** | See §E and the ledger row below | `UNMEASURED (G1 FAIL)` |

**`src=` tally (the `grep` the convention exists for): `DEEP_ENRG` 4 · `DEEP_HLTH` 1 · `DEEP_RE` 3 ·
`DEEP_FIN` 2 · `SWEEP` 3 · `EVENT_ALPHA` 2 (both amended or rejected by a later stage).**
⇒ **10 of 15 candidate rows originate in a DEEP file.** The question *"how much of BET is DEEP?"*
now has an answer for the first time.

---

## §C · Flow / positioning cross-read (per candidate)

| Name | flow · tag · OBV | `rs20` / `rs60` | `vol_surge` | Δ | FINRA short-z (08-25) | Options |
|---|---|---:|---:|---:|---|---|
| `COIN` | **+0.978** 🟢 매집 | +9.9 / −0.2 | **1.56** | +0.11 | `+0.49` △ normal | — |
| `MSTR` | **+0.939** 🟢 매집 | **+28.9** / **−17.5** | **1.49** | −0.06 | `−0.60` ✅ cover | — |
| `MRK` | +0.767 🟢 매집 | +13.0 / +32.6 | **1.18** | −0.19 | — | — |
| `HOOD` | +0.594 🟡 매집 | +17.5 / +20.3 | **1.06** | +0.24 | — | — |
| `MRVL` | +0.444 🟢 매집 | **+41.7** / +8.2 | 0.60 | −0.08 | **`−1.11` ✅ cover** | 🚨 short **4.8% float BUILDING**, DTC 1.4, P/C 0.86, skew **+3.5**, implied **±10.3% (08-28, D2)** |
| `ORCL` | +0.339 🟢 매집 | +22.6 / **−40.5** | **0.41** | −0.03 | — | — |
| `KLAC` | +0.093 🟢 매집 | +1.7 / −7.4 | 0.56 | **+0.64** (the run's only `new_green`) | `−0.05` △ | — |
| `VLO` | +0.384 🟡 매집 | +7.7 / **+33.6** | 0.57 | −0.06 | — | — |
| `COP` | +0.519 🟡 매집 | +6.2 / +12.6 | 0.87 | −0.09 | — | — |
| `MPC` · `PSX` (held) | +0.572 / +0.505 🟡 매집 | +10.4/+36.8 · +9.9/+30.9 | 0.83 / 0.75 | −0.01 / −0.05 | `−0.60` / `+1.12` △ | — |
| `EQIX` · `DLR` · `CCI` | −0.053 / −0.159 / −0.475 🟡 | +2.1/+1.8 · −2.2/+3.6 · −8.2/−16.9 | 0.68/0.44/0.46 | **+0.28 / +0.31 / −0.41** | — | — |

🚨 **`MRVL` carries a two-instrument contradiction on its short book, one session before its print**:
`us_live_shortlist` calls it **✅ 저숏/숏커버 "clean rise"** from the FINRA daily z (**−1.11**), while
`module_flow --positioning` reads **short 4.8% of float and BUILDING**. **Two different windows and
two different data sources, and they disagree in direction.** ⇒ **Neither is used alone**, and the
disagreement is handed to `S116`'s settle rather than averaged away.
⚠ **`vol_surge` is unusable across the entire sheet except `COIN` (1.56), `MSTR` (1.49), `MRK` (1.18)
and `HOOD` (1.06)** — 11 of 15 rows sit below 0.90 on a 2.48%-volume bar (`D355`).

---

## §D · Competition / peers

- **`COIN` vs `HOOD` — the same node, opposite denominators.** Comparable price move (`exc5` +28.19 vs
  +22.66), comparable surge (1.56 vs 1.06), **opposite revision books** (−303.5% vs +10.2% CY) and
  opposite 60-day excess (−2.24 vs +17.62). ⇒ **the peer comparison IS the finding.**
- **`MRVL` vs `AVGO` (held).** `S116` measures exactly this spread on 08-28. `MRVL` `rs60 +8.2` vs
  `AVGO` **−24.1** = a **32.3pp** realised gap; `MRVL` revisions positive on all four, `AVGO`
  `exc5 −5.92 = the 9.9th percentile of 252` and now bracketed by **`S127`** (registered this run).
- **`VLO` vs `MPC`/`PSX`.** The three moved as **one unit**: `exc5` −2.55 / −2.89 / −2.51, a **0.38pp
  spread on five sessions** against 2.06pp on twenty. `risk_units` merges `{MPC, PSX}` at all three
  windows (250d / 500d / 750d). ⇒ **adding `VLO` to a book already holding `MPC`+`PSX` adds a name,
  not a risk unit.** Stated as a structural fact; **no sizing implication is drawn (P4).**
- **`EQIX` vs `DLR` vs `IRM`.** The carried registry grouping `{DLR, EQIX, IRM}` is **not observed on
  this frame** — `IRM` is negative on all three windows while `DLR`/`EQIX` carry the sector's two
  largest positive deltas (`M953`).
- **`ORCL` vs `KLAC` vs `MRVL`** — three IT 🟢s with three different shapes: `ORCL` cheap-and-broken
  (`rs60 −40.5`), `KLAC` mid-multiple with rising estimates, `MRVL` expensive with the fastest
  estimates and a print in one session.

---

## §E · Refutation + dated catalyst (per candidate)

| Name | What kills it | Dated observable |
|---|---|---|
| `VLO` `MPC` `PSX` | **`P100` branch B** (`EW{MPC,VLO,PSX}` `exc20` ≤ **−4.731**) ⇒ the 20-day leadership was the barrel, not the margin. ⚠ Independently: it trades **8.4% above target** on a **+54.9%** 90-day revision — `L2` | **2026-09-01** |
| `COP` | Sector-wide E&P delta contagion reaching it (its Δ is −0.09 vs peers' −0.52…−0.57) | **09-08** |
| `MRK` | It already trades **above** its mean target with **−4.2%** current-quarter revisions. Kill = price ≥ target **while** revisions keep falling ⇒ `L2` fires on the sector's only 🟢 | **09-08** |
| `EQIX` `DLR` | Their positive deltas turning negative, **or** the 1↑/3↓ near-term breadth spreading to the CY line | **09-08** |
| `CCI` | `exc60` staying ≤ −15 through the tower roll-off ⇒ the +24.3% upside is a value trap | **09-08** |
| `HOOD` | Its driver is the debasement thread, **not** lending. Kill = **`P97` branch B** (broad dollar ≥ 118.60 on a settled `[FRED]` close) | **08-28+** |
| **`COIN`** | **Already partly refuted by §A.** Kill = CY consensus staying below 0 while `exc60` stays negative ⇒ the flow bought a deteriorating denominator | **09-08** |
| `MRVL` | **`S116` branch B** (`MRVL − AVGO` ≤ −12.0pp on 08-28) | **2026-08-27 print → 08-28 settle** |
| `ORCL` | `rs60 −40.5` with `vol_surge` 0.41 — **PREMORTEM already re-tagged it a reversal, not a runner.** Kill = `rs20` crossing back below 0 while `rs60` stays ≤ −30 | **09-08** |
| `KLAC` | Its `new_green` is unreadable at `vol_surge` 0.56. Kill = failing to tag 🟢 on a **SETTLED-bar** sweep | first settled-bar sweep |
| **`MSTR`** | **REJECTED — see below** | — |

---

## §F · Epicenter-starter module — **NOT triggered, and the ✅ is qualified**

`cycle_exposure` reports **no GAP**: AI-compute epicenter **16.69%** (need ≥12.0) via `NVDA`/`ANET`;
Energy/refining **9.7%** (need ≥8.0) via `MPC`/`PSX`. ⇒ **no epicenter-starter is required by rule.**
🚨 **But PREMORTEM downgraded that ✅ to ⚠ UNDER-DETERMINED** (`D250`, **12th run**): `cycle_registry.json`
has **no optical/interconnect row**, on a run where `COHR` and `LITE` were `P79`'s largest contributors.
**An epicenter percentage computed against a registry missing a live chain layer cannot say "no gap"**,
so the module is **not** triggered and the reason is recorded rather than the ✅ being taken at face value.

---

## §G · Ledger writes from this stage

| Ledger | Row | Class | Condition | Recheck |
|---|---|---|---|---|
| **reject** | **`MSTR`** | **`H.밸류소진`** | CY consensus EPS turns positive **AND** `rs60` > 0 on a settled sweep | **2026-09-16** |
| **missed** | **`ORCL`** | **`Q.확신부족`** | `rs60` recovers above −15 while it holds 🟢 on a **settled-bar** sweep | **2026-09-16** |
| **missed** | **`KLAC`** | **`M.숏리스트탈락`** | tags 🟢 on a **SETTLED-bar** sweep with `vol_surge ≥ 1.2` | **2026-09-16** |
| *(EVENT_ALPHA, earlier this run)* | `XOM` reject · `AMD` miss · `AAPL` miss | — | — | 09-09 / 09-09 / 09-16 |

**`MSTR`'s rejection reasoning, written out because the ledger's cost is measured**: it is **not**
rejected on narrative. Its **measured** axes reject it — a **2.52× forward multiple produced by a
current-year consensus that fell 43.82 → −6.69 (−115.3%)** and a next-year book down **−72.2%**,
against `rs60 −17.5`. **PREMORTEM independently re-tagged it NOT-A-RUNNER.** ⚠ **The counter-case is
recorded**: its flow score (+0.939) and `vol_surge` (1.49) are 2nd on the entire board and its FINRA
z is **−0.60 (shorts leaving)**. **That is exactly why the `revives_if` is set on the denominator and
not on the story** — the "re-file, don't remove" rule applies to names removed on *narrative* grounds
while their measured flow passes; here the removal **is** on a measured axis, and the flow axis that
still passes is what the revival condition watches.

⚠ **`ORCL` is filed as a MISS, not a rejection**, and the boundary matters: it is not being *rejected*
on evidence — its estimates are mildly positive and its multiple is the cheapest on the board. It
simply **did not clear this sheet** on `rs60 −40.5` + `vol_surge` 0.41. `missed_ledger` is the right
ledger for that, and the script enforces the boundary (a ticker×date in the rejection ledger is refused).

---

## ✅ EXIT CHECK
- [x] **Company scoreboard consulted BEFORE any re-derivation** — 5 rows, all KR, **zero US
      candidates covered** ⇒ every name RE-DERIVED with the failing test named ("no row"), and
      `module_report_tags ticker` run on all eight finalists with **the index's own 36-day staleness
      stated** so the ages read as floors.
- [x] Every DEEP sector has a section (§B-1…§B-4); **cross-sector LIVE shortlist names included**
      (§B-5) — `MRVL` `ORCL` `KLAC` `MSTR` carried, `MSTR` explicitly rejected with a reason.
- [x] Numbers cross-checked: `HOOD` revenue verified **SEC XBRL ↔ yfinance at 0.0% on every
      comparable quarter**; every revision figure taken from the tool's own 90-day column;
      **blanks left blank** (`MPC`/`PSX` §A row, RE PEG column, most FINRA/options cells).
- [x] Flow/positioning cross-read present per candidate (§C), with the **`MRVL` two-instrument short
      contradiction** stated rather than averaged.
- [x] **BET_SHEET.md written as ONE file** with per-sector sections.
- [x] **Every set-aside name is in a ledger with a class AND a condition AND a recheck date** (§G) —
      `MSTR` (reject), `ORCL`/`KLAC` (missed), plus the three filed at EVENT_ALPHA.
- [x] **No name removed on narrative grounds while its measured flow still passed** — `MSTR`'s removal
      is on a **measured** axis (the revision book), its still-passing flow axis is exactly what the
      `revives_if` watches, and the counter-case is written out.
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** — `ORCL`,
      `KLAC` here; `AMD`, `AAPL` at EVENT_ALPHA. **Six ledger rows from one sheet.**
- [x] **Sizing language consistent with the exposure state**: state `정상`, target 95% vs accrued
      85.5%, gap **−9.5pp**, and 🚨 **`exposure_rule state` could NOT read the account
      (`투자비중미상`)** — the 85.5% is **stated from the accrued ledger row, not substituted**.
      The state is **not** `복귀`, so no fill-the-target obligation arises. **No fraction appears
      anywhere on this sheet**, and any that did would read "mechanical 1/4 — IC not yet estimable".
- [x] Linter run on this file.

---

## §H · ALPHA freshness gate (Stage 7 / L1·ALPHA) — **NO VERDICT ISSUED, BY RULE**

> This section is written by the ALPHA stage into the file the protocol assigns it (`BET_SHEET §B`
> tags + `ACTION_TICKETS.md`). **Every §B row above reads `UNMEASURED (G1 FAIL)` and none was changed.**

### H-1 · Why no verdict: G1 FAILED, and this run additionally identified the CAUSE
`vel_coverage` **17.06% against an 80% bar** ⇒ PREFLIGHT removed the theme-freshness citation right
for the whole run. **ALPHA therefore issues no 🟢LIVE / 🟡PARTIAL / 🔴RESOLVED verdict at all**, the
same ruling the 2026-08-25 run made.

🚨 **And `F1`'s counter is NOT incremented.** The desk's standing line — *"🟢LIVE has fired 0 times in
N consecutive runs"* — is **not advanced by this run**, because incrementing a count produced by a
loose instrument is `D16`'s error verbatim (the estimate daemon that reported *"35 days to go"* while
dying). **The count stays where it was.**

★ **What this run adds that no prior run had**: `M947` establishes the cause is **not** a dropping
tunnel. The 51 velocity-measured names are `us_top300` **ranks 1–51, contiguous, and byte-identical
to 08-25's set (overlap 51 of 51)**. **A load-dependent failure cannot produce a contiguous rank
prefix twice.** ⇒ **`vel_coverage` will read 17.06% on every run until the cap changes**, and because
the cap is a rank prefix of a **42-day-old** market-cap file, **G1 and G5 are the same defect.**

### H-2 · Falsification probes — **8 of 8 alive and discriminating** (run mid-stage, this stage)
`module_news_data fts search "<name>" --days 7 --count --scope foreign`:

| Nvidia | Oracle | Marvell | Merck | Robinhood | Coinbase Global | Valero | KLA Corporation |
|---:|---:|---:|---:|---:|---:|---:|---:|
| **4,520** | 515 | 417 | 290 | 258 | 151 | 38 | **12** |

**Two and a half orders of magnitude between the loudest and quietest probe** ⇒ the pipe is alive and
ordering correctly. 🚫 **`Valero` 38 and `KLA Corporation` 12 are NOT read as "quiet"** — G1's removed
right forbids exactly that verdict, and a low hand-probe count on a two-word company name is a
name-matching question, not a market one.

### H-3 · What the theme instrument printed, reported as a MEASUREMENT and not as a verdict
Under the sibling desk's **base ≥ 100 articles** filter (registered 2026-08-26 after `theme-age`
returned 🟢FRESH on `n=1`), the US board's readable terms are:

| Term | Age | Base | Accel | Would it clear a FRESH gate? |
|---|---:|---:|---:|---|
| **`Treasury buyback`** | **7** | **259** | (273.21×) | ⚠ **age clears; the accel is DEGENERATE** — a 7-day average of 36.4 against a near-zero 90-day baseline. **The age is readable; the ratio is not** |
| `Canada tariff` | 60 | 94 | 5.10× | no — age |
| `diesel export` | 63 | 195 | 0.54× | no — age and accel |
| `Jackson Hole` · `Iran sanctions` · `national debt` · `AI capex` · `HBM` · `memory prices` · `refining margin` · `drug pricing` · `consumer confidence` | ≥90 | 166–1,336 | 0.66×–26.25× | no — age |

⇒ **Had a verdict been permitted, `Treasury buyback` is the only US theme in the window that would
even reach the age gate — and its acceleration is unreadable, so it would not have cleared cleanly.**
**No verdict is issued. This is the instrument's printout, labelled as such.**

### H-4 · Carry-forward — every ALPHA-touched name, INDEPENDENT of its sector's DEEP slot
> The rule exists because `006360` carried an ALPHA tag with real flow, its sector rested, nothing
> tracked it, and it ran **+12.3% over five sessions, unowned.**

**Carried to the next run's inheritance packet regardless of rotation**: `MRVL` · `HOOD` · `COIN` ·
`MRK` · `VLO` · `COP` · `EQIX` · `DLR` · `CCI` · `MPC` · `PSX` (held) · plus the ledger rows
`MSTR` `ORCL` `KLAC` `XOM` `AMD` `AAPL`.
**Every one of the six ledger rows carries a class, a condition and a recheck date** (§G) — so none of
them depends on anyone remembering it.

### H-5 · 🟡PARTIAL re-check dates — **none issued, because no tag was issued**
The rule *"a 🟡PARTIAL is a dated appointment, not a shelf"* has **nothing to bind to this run**.
⚠ **The equivalent obligation was met a different way**: every candidate on this sheet carries a dated
observable in **§E**, and every set-aside name carries a `recheck_date` in **§G**. `ACTION_TICKETS.md
§3` lists all twelve appointments in one table. **No name on this sheet is on a shelf without a date.**

### H-6 · 🚨 `D294` reproduces — **8th** time, and `ACTION_TICKETS.md` is hand-built for a **4th** run
`action_bracket.py` printed *"**Nearest binary:** NVDA earnings (D-0, axis=earnings) — both-sides
armed below"* and, four lines later, *"No tickets — no cycle GAP and no dated binary in window"* — on
a window `CATALYST_WATCH` fills with **six** binaries plus two this desk added by hand.
⇒ `llm_outputs/2026-08-26/ACTION_TICKETS.md` was **written by hand**, with **DRY-RUN share counts
deliberately omitted** under the analytical-only mandate.

### ✅ ALPHA EXIT CHECK
- [x] Every §B tag filled with an evidence label and date — **all read `UNMEASURED (G1 FAIL)`**, and
      **no 🔴 was issued**, so no `reject_ledger` row is owed *by this stage*. (Three rejection/miss
      rows were nevertheless filed at BET and three at EVENT_ALPHA — six for the run.)
- [x] **No 🟡PARTIAL exists to date**, and the equivalent obligation is met through §E's dated
      observables and §G's recheck dates; **every ALPHA-touched name is listed for carry-forward
      independently of its sector's DEEP slot** (§H-4).
- [x] **Momentum-only and positioning flags stamped** — `MSTR` and `ORCL` momentum-only;
      the `MRVL`, `NVDA` and `ANET` two-instrument short disagreements reported rather than averaged;
      🚫 **no `⚡crowded-short` stamp issued anywhere, stated as a finding.**
- [x] **`ACTION_TICKETS.md` written** — both-sides brackets per binary (8 binaries, 8 audited,
      2 registered this run), **no core-starter** (the GAP gate is ⚠ UNDER-DETERMINED, not ✅).
- [x] **Falsification probe actually run mid-stage** (8 of 8 alive) **and `F1`'s counter NOT
      incremented** (`D16`).
