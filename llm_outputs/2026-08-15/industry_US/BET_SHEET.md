# BET_SHEET — industry_US · 2026-08-15 · Stage 9/11 (L1·BET)

> ONE file, per-sector sections (downstream desks glob this exact filename — never split it).
> Prices settled **2026-08-14**, benchmark **`SPY`** named inline. `flow_score` is **3-axis**.
> **Zero buy/sell recommendations.** Any size language is illustration only (P4).

## §0 · The constraints this sheet is written under

| Constraint | Source | Effect on every number below |
|---|---|---|
| `flow_score` is **3-axis**; the 🟢 tag is **4-axis** | `D261`, replicated & worse today | **6 of 11 🟢 are velocity-lit and excluded**: `NFLX` `NVDA` `CVX` `MRVL` `CSCO` `BAC`. **Admissible greens = 5** |
| `vol_surge` blocks **100 of 110** accumulating names, **100.0% of them alone** | `D270` (new) | **A 🟡 is not evidence against a name this week.** Every 🟡 below is annotated with its surge |
| Concentration guard has **no single number** | PREFLIGHT G4 FAIL (250d **11** units · 500d **10** · 750d **10**) | **No concentration statement is made** without its `--days` on the same line |
| `kelly_size --ic` is not evidence-backed | PREFLIGHT G6 FAIL (accrual 2.4× slow) | Any size referenced is **"mechanical ¼"** |
| Caps are **31 days stale** | PREFLIGHT G5 FAIL | `wflow`/`top1_w` are **not** current-cap weights; this sheet uses `eqflow`/RS/OBV instead |

---

## §I · ENERGY (OW — promoted this run) · DEEP continuous 1

### §A · Numbers (`module_fundamentals_us --json`, settled 08-14)

| | `MPC` *(held)* | `PSX` *(held)* | `VLO` *(not held)* |
|---|---|---|---|
| Price | **$355.42** | **$233.61** | **$341.67** |
| 52-week high | 360.10 (**−1.3%** from it) | 236.14 (**−1.1%**) | 346.09 (**−1.3%**) |
| Forward P/E · trailing | **11.04** · 12.36 | **11.11** · 13.33 | **12.09** · 14.24 |
| PEG · P/B | 1.59 · 5.27 | 1.25 · 3.28 | 4.08 · 4.25 |
| Consensus target mean | $317.72 | $217.11 | $315.26 |
| **Price vs target** | 🚨 **+11.9% ABOVE** | 🚨 **+7.6% ABOVE** | 🚨 **+8.4% ABOVE** |
| **FY2025 gross margin vs own median** | **10.0% vs 10.5% — BELOW** | **12.3% vs 12.1% — AT** | 🚨 **UNKNOWN (C3)** |

**Cross-check (`math_check` class)**: price ÷ target − 1 → MPC 355.42/317.72 = **+11.87%**;
PSX 233.61/217.11 = **+7.60%**; VLO 341.67/315.26 = **+8.38%**. Forward EPS × forward P/E reconciles
to price within rounding on all three. **Blanks are blanks**: `VLO`'s margin percentile is left empty,
not estimated.

★ **All three trade 7–12% ABOVE consensus and 1.1–1.3% BELOW their own 52-week highs, while their last
reported annual margins sit AT or BELOW their own medians.** Both halves stated (**C2**): the price is
extended against analysts and the earnings denominator is **not** peaking on trailing data. ⚠ The
**forward** denominator is unmeasured — FY2025 predates the entire crack move.

### §B · Thesis · freshness `[ALPHA fills]`
The Energy OW is **the refining node**, not the sector: refiner median RS60 vs `SPY` **+24.3** against
integrateds **−5.9**, a **30.2pp** spread; the binding constraint is **middle-distillate refining
capacity**, being physically destroyed (Salavat **200,000 bpd** struck 08-13; a fuel terminal 08-14;
Russia's diesel exports at a **multiyear low**). `HO=F` **+5.37% / 20d** while `CL=F` is **−0.11%**.

### §C · Flow / positioning
`MPC` **🟢 admissible** · OBV 매집 +0.220 · RS20 +9.3 · RS60 **+29.3** · surge 1.25 · FINRA short z
**−0.71 = ✅clean-rise** · short **2.8% float, covering, DTC 3.4** · option P/C 0.75, skew +61.9 ·
**implied ±4.4% to 08-21 (D6)**.
`PSX` 🟡 **on surge 1.01 alone** · OBV 매집 · RS60 +22.3. `VLO` 🟡 **on surge 0.84 alone** · OBV 매집 ·
RS60 +24.3 · **the most based runner on the board** (last-20 share of 60d excess = **24%**).
**WTI spec at the 18th percentile SHORT** (COT 08-11) — the board's most asymmetric positioning cell.

### §D · Competition / peers
Within the node the differentiator is **distillate yield**; `MPC` and `PSX` are held, `VLO` is not.
Integrateds (`XOM` `CVX` `COP` `OXY`) are **not** peers for this thesis — every one has a negative
RS60 and `XOM` alone contributes ~110% of the sector's Δ decay.

### §E · Refutation + dated catalyst
🚨 **`S88` (08-21)** — `EW{MPC,VLO,PSX}` exc5 vs `SPY` stood at **+15.698 = the 100th percentile of two
years** when the OW was granted. **A ≤ +0.061 falsifies the promotion.**
⚠ **`S84` (08-21) cannot falsify this thesis** — it tests Hormuz transit only, while the mechanism here
is Russian capacity destruction, killed by a **ceasefire**, not by the Strait reopening.
**`P62` KPI: `HO=F` 20d − `CL=F` 20d = +5.48pp; direction A holds above +4pp.**

### ★ EPICENTER-STARTER MODULE (a cycle GAP was flagged — required by the stage)
`CYCLE_EXPOSURE`: **rank-2 cycle "Energy / oil-refining", epicenter 7.10% vs 8.0% required,
margin −0.898pp.** The rule: **a partial core in a top-rank cycle's epicenter exists on the sheet
regardless of tape; the tape gates only the remainder.**
**Cleanest epicenter expressions, named and ranked by structure** (P4 — naming, not recommending):
1. **`MPC`** — held; the sector's only admissible 🟢; ✅clean-rise short profile; margin **below** median.
2. **`PSX`** — held; RS60 +22.3; margin **at** median; blocked from the shortlist by surge 1.01 only.
3. **`VLO`** — **not held**; best-based momentum (24% share); RS60 +24.3; ⚠ **margin percentile
   UNKNOWN (C3)** and the analyst book is **hold-majority (3/7/8/1/1)**.
⚠ **The desk holds two of the three, and the un-held one is the most based and the least measurable.**

---

## §II · INDUSTRIALS (OW−) · DEEP continuous 2

### §A · Numbers

| | `RTX` *(held)* | `GD` |
|---|---|---|
| Price | **$222.97** | **$395.78** |
| 52-week high | 226.88 (**−1.7%**) | 400.00 (**−1.1%**) |
| Forward P/E · trailing | **28.39** · 39.19 | **21.34** · 24.15 |
| PEG · P/B | 2.79 · 4.53 | 2.74 · 3.99 |
| Target mean | $232.27 | **$420.02** |
| **Price vs target** | **−4.0% BELOW** | **−5.8% BELOW** |
| Analyst book | — | 3 SB · 10 B · **10 H** · 1 S |

★ **Both trade BELOW consensus** — the opposite of the Energy node, and the only sector on this sheet
where that is true.

### §B · Thesis · freshness `[ALPHA fills]`
🚨 **`D249` is answered**: the OW− is on **defense + electricals**, not on `XLI`.
Defense `eqflow` **+0.331** / exc20 vs `SPY` **+7.60** / exc60 **+12.79**; electricals `eqflow`
**+0.221** / exc60 **+19.01**; transport `eqflow` **−0.335** / exc20 **−6.41**. **`XLI` sits at
exc20 −0.49 — between them.**

### §C · Flow / positioning
`RTX` OBV **+0.381 매집**, RS20 +10.8, RS60 **+22.0**, surge **0.64** ⇒ 🟡 **for volume only**.
`GD` OBV **+0.448** (the node's strongest), RS20 +2.9, RS60 +10.6, surge **0.52**.
`LMT` OBV +0.467, RS20 **+15.2**, surge 0.78, **implied ±3.0% to 08-21**.
**25 of 50 Industrials names pass `OBV 매집 ∧ RS20>0` and every one is blocked on `vol_surge` alone.**

### §D · Competition / peers
`HII` — **the pure-play US Navy shipbuilder — is NOT in `us_top300`**, so the most exposed listed name
to the 08-14/08-15 shipbuilding policy has **no reading on this desk** (`D274`). `NOC` exited
shipbuilding in 2011 and is therefore **not** exposure. Foreign beneficiaries (Hanwha, Fincantieri)
are outside the universe by construction.

### §E · Refutation + dated catalyst
🚨 **PREMORTEM Lens 3 tags `LMT` EXHAUSTED** — exc60 **+9.77** of which the last 20 sessions supplied
**+15.19**, i.e. days 21–60 were **−5.42** (share +155%) — **while `RTX` (share 49%) and `GD` (28%) are
based.** The node is not one shape; a node-level verdict would have been wrong in both directions.
⚠ **`cycle_exposure` cannot arbitrate**: the rank-3 "missile-defense" cycle has **no floor set**, so
its ⚪ means *unmeasured*, not *fine* (`D271`).
**Dated**: `GD` RS20 vs `SPY` **+2.9**, re-check **08-21**; kill if **< −3.0** while the shipbuilding
thread still builds.

---

## §III · CONSUMER DISCRETIONARY (N−) · DEEP rotating 1

### §A · Numbers — `ABNB`

| | `ABNB` |
|---|---|
| Price | **$184.06** · 52w high 187.12 (**−1.6%**) · 52w low 110.81 |
| Forward P/E · trailing | **29.98** · 42.22 · **PEG 1.93** |
| P/S · P/B | 8.38 · **13.92** |
| Target mean / median | **$174.73** / $175.00 |
| **Price vs target** | 🚨 **+5.3% ABOVE** |
| Analyst book | 4 SB · 20 B · **18 H** · 2 S · 1 SS |

### §B · Thesis · freshness `[ALPHA fills]`
The sector is **two businesses 21.5pp apart**: services `EW{ABNB,DASH,BKNG}` exc20 vs `SPY` **+15.77**
(exc60 **+33.49**) against goods `EW{AMZN,HD,TSLA}` **−5.74** (exc60 −6.47), with `XLY` at **−2.06**
between them. **The N− is a goods call.** The 08-14 consumer prints (5 outlets) hit the goods side —
`XLY` posted the **worst exc5 of eleven** while services was **+0.47**.

### §C · Flow / positioning
`ABNB` **🟢 and NOT velocity-lit** — it clears on `OBV 매집 +0.116 ∧ RS20 +21.6 ∧ vol_surge 1.55`
outright, the only DISC name to do so. RS60 **+34.5** (tied best in sector). FINRA short z **−0.94 =
✅clean-rise**. ⚠ Momentum shape **LATE-BUT-LIVE**: **63%** of its 60-day excess was earned in the last
20 sessions.
`ROST` OBV **+0.300 매집** — the only goods sub-node accumulating (a trade-down tell).

### §D · Competition / peers
Inside experiences the split is **asset-light vs owned-asset**: `ABNB` +34.5 and `BKNG` +31.4 against
`MAR` −6.4 🔴 and `HLT` −2.1 🔴. **The working leg is the one with no capex.**

### §E · Refutation + dated catalyst
⚠ **`ABNB` trades 5.3% above a hold-majority consensus at P/B 13.9**, and its move is **63% new**.
⚠ **The cohort split is n=3 per side and hand-picked (C5)** — real for those six names, **not** a
measured property of all 28 (`D275` registers the full-partition test).
**Dated: `S91` (08-21)** — `XLY` exc5 vs `SPY`, state **−1.783 (14th %ile)**, **A ≤ −2.467 ·
B ≥ +1.553**; `sd 1.639` is the narrowest estimator on the board ⇒ **both branches reachable**.

---

## §IV · REAL ESTATE (UW) · DEEP rotating 2

### §A · Numbers

| | `EQIX` | `DLR` | `CBRE` |
|---|---|---|---|
| Price | **$1,102.10** | **$200.15** | **$152.86** |
| 52-week high | 1,128.68 (−2.4%) | 208.14 (−3.8%) | 174.27 (**−12.3%**) |
| Forward P/E (**GAAP**) | 58.37 | **69.22** | **16.83** |
| PEG · P/B | 3.44 · 7.56 | **14.27** · 2.77 | **0.97** · 5.28 |
| Target mean | $1,225.76 (**+11.2% upside**) | $222.03 (**+10.9%**) | **$181.25 (+18.6%)** |
| Analyst book | — | — | **5 SB · 7 B · 1 H · 0 S** |

🚨 **GAAP-vs-FFO trap (`M151`), flagged explicitly**: `DLR`'s **69.22×** and `EQIX`'s **58.37×** are
**GAAP earnings multiples on REITs** and are **not comparable to a P/E**. `M151` already measured
`DLR`'s AFFO multiple at **≈24.4×** on a prior date. **Do not read 69× as expensive on this line** —
and this desk has made that exact error before, which is why the row is annotated rather than dropped.
✅ **`CBRE` is not a REIT** (it is a services company), so its **16.83× forward and PEG 0.97 are
directly readable** — the only clean multiple in this section.

### §B · Thesis · freshness `[ALPHA fills]`
RE's UW is **not** a duration call and **not** uniform. Data-centre node `EW{EQIX,DLR,CBRE,IRM}` is
**positive on all three windows** (exc5 **+4.35** / exc20 **+4.59** / exc60 **+3.35**) inside a sector
whose ETF is **−4.78 on 20 days**; towers are **−16.69 on 60** and health-care REITs **−8.42 on 20**.
**The UW is a towers + health-care call wearing a sector label.**

### §C · Flow / positioning
**4 of 12 accumulating — and they are the top four by flow score**: `EQIX` (+0.444, surge 0.93),
`DLR` (+0.439, OBV **+0.346**, RS20 **+10.7**, surge **0.59**), `CBRE` (+0.322, RS60 **+13.5**),
`IRM` (+0.182). **All four 🟡 on `vol_surge` alone.**
The eight below them contain **every 🔴**: `SPG` OBV **−0.466**, `O` **−0.298**, `WELL` `VTR` 분산.

### §D · Competition / peers
`CCI` **cannot compete for the data-centre demand** — post-divestiture (Fiber/Small Cells sold
2026-05-01) it has **zero AI exposure**, and its RS60 **−23.5** is the sector's worst. `AMT` sits with
duration (`M131`). ⇒ **The tower node is not a cheap version of the data-centre node; it is a
different business.**

### §E · Refutation + dated catalyst
🚨 **`DLR`, the node's loudest name, is the least based**: exc60 **+1.64** with days 21–60 **−9.02**.
✅ **But the node is not one shape** — `CBRE` exc60 **+13.51** with days 21–60 **+9.49** is genuinely
based, and `EQIX` is a **turn inside a drawdown** (exc60 −0.69, exc20 +3.60).
**Binding constraint = cost of capital**, and it is **not currently binding**: `HY OAS` **2.71% flat,
8bp off a 365-day low** `[FRED]` 08-13. **Kill line: HY OAS > 3.20%.**
**Dated: `S90` (08-21)** — `DLR` exc5 vs `SPY`, state **+2.878 (84th %ile)**, **A ≤ −3.199 ·
B ≥ +5.223**. ⚠ **No implied-move check was pulled for this row** and the gap is stated.

---

## §V · CROSS-SECTOR LIVE SHORTLIST — names from outside the DEEP sectors

`US_LIVE_SHORTLIST.json`, 11 names ⇒ **5 admissible** after the `D261` adjustment.
Two are already covered above (`MPC` §I, `ABNB` §III). The remaining three:

| Ticker | Sector | flow | Short z | Numbers | Disposition |
|---|---|---|---|---|---|
| **`KKR`** | Financials | **+0.939** · OBV 매집 · RS20 +8.5 · RS60 **+16.9** · surge **1.49** | **+1.62 = ⚡crowded-short** | px **$114.01** · fwd P/E **15.43** · **PEG 0.57** · P/B 3.63 · target **$126.53 = +11.0% upside** · book **7 SB · 12 B · 3 H · 0 S** · 52w high 152.10 (**−25.0% below**) | **INCLUDED.** `M669`'s relocated-breadth node, confirmed on a 2nd date — the only admissible 🟢 in a sector rated N−. ⚠ **crowded-short is squeeze fuel, NOT a demand axis (D6)** |
| **`COHR`** | Info Tech | **+0.990 — the maximum on a 299-name board** · OBV 매집 · RS20 +12.9 · **RS60 −13.7** · surge 1.67 | −0.17 △normal | px **$325.83** · fwd P/E 23.38 · trailing **79.28** · **PEG 0.92** · target **$394.62 = +21.1% upside** · 52w high 440.00 (**−26.0% below**) | ⚠ **INCLUDED WITH A LATE-MONEY TAG.** EVENT_ALPHA Card 2 dates its 1.67 surge to its **own 08-11/08-12 earnings print** ⇒ **reaction volume, not accumulation**. RS60 still **negative** |
| **`LITE`** | Info Tech | +0.817 · OBV 매집 +0.275 · RS20 **+21.9** · RS60 −1.8 · surge 1.27 | +0.38 △normal | *(not pulled — see §VI)* | ⚠ **INCLUDED WITH THE SAME TAG.** *"Lumentum sees sales more than double"* [`marketwatch` 08-11]; *"Earnings Top Estimates"* [`yahoo_finance` 08-12] |

**Explicitly DROPPED from this sheet, with reason** — the six velocity-lit greens
(`NFLX` `NVDA` `CVX` `MRVL` `CSCO` `BAC`): **their 🟢 can only be produced by the revoked news axis**
(`D261`), and `CSCO`'s RS20 is **−4.7, negative**. **Dropped as INADMISSIBLE INPUTS, not as rejected
names** — no rejection-ledger row is filed for them, because the desk is not rejecting the businesses;
**it cannot measure their tag today.** ⚠ Four of them (`NVDA` `CVX` `BAC` `MRVL`) remain measurable on
OBV/RS and appear in §I/§IV analysis where relevant.

★ **The 🟢 policy layer this run**: an FCC proposal to **ban Chinese optical transceiver imports**
(China holds **56%** of that market) [`tomshardware` 08-11] is a forward, un-priced leg for `COHR`/
`LITE` that the earnings print does **not** contain. **Dated by `S86` (08-21)**, already armed.

---

## §VI · Ledger writebacks

### §VI-a · Rejections filed at BET (`reject_ledger`) — class + `--revives-if` + `--recheck-date`
**None filed at this stage.** Every name considered here either (i) reached the sheet, or (ii) was
dropped as an **inadmissible instrument reading** rather than as a judgement on the name (§V) — and a
rejection ledger is for judgements. ⚠ **Stated explicitly rather than left as a silent zero**: filing
`NVDA` as "rejected" today would record a decision the desk did not make.

### §VI-b · Misses filed at BET (`missed_ledger`)

| Ticker | Class | Why it is a miss | `--enters-if` | recheck |
|---|---|---|---|---|
| **`VLO`** | `R.타이밍대기` | **The epicenter-starter module named it #3 and the desk does not hold it**, while `CYCLE_EXPOSURE` flags a **−0.898pp** shortfall on that exact cycle. It is the node's **most based** runner (24% last-20 share) with the **2nd-best RS60**. Not on the sheet as a holding — filed so the opportunity cost lands somewhere | `S88` settles **C or B** (i.e. the node does not mean-revert to its 2-year median) **AND** a `VLO` margin percentile becomes measurable | 2026-08-22 |
| **`CBRE`** | `Q.확신부족` | The **only clean, non-REIT multiple** in the RE data-centre node (fwd **16.83×**, **PEG 0.97**, **5 SB / 7 B / 1 H**), **+18.6% to target**, RS60 **+13.5**, and the node's only **genuinely based** momentum shape (days 21–60 **+9.49**). It did not get its own §A row treatment because the DEEP focused on `DLR`'s exhaustion question | `S90` settles **B**, or `CBRE` enters the 🟢 set on an admissible axis | 2026-08-22 |
| **`HII`** | `N.유니버스부재` | **The single most exposed listed US name to a dated policy change** (Navy shipbuilding opened to foreign yards, 08-14/08-15) and it is **outside `us_top300`** — so it has no flow, RS, OBV or short reading on this desk at all. **This is an instrument gap, filed as a miss so it is scored rather than forgotten** | `HII` enters the universe (a `build_us_universe.py --include` run), at which point it becomes measurable and can be judged | 2026-08-29 |

⚠ **Boundary respected**: none of the three was "considered and set aside on its merits" — `VLO` is a
timing/holdings gap, `CBRE` is insufficient work, `HII` is an instrument absence. **All three belong
in `missed_ledger`, not `reject_ledger`**, and the script enforces the boundary.

---

## ✅ EXIT CHECK
- [x] **Every DEEP sector has a section** — §I ENRG · §II INDU · §III DISC · §IV RE — each with
      §A numbers · §B thesis+freshness placeholder · §C flow/positioning · §D peers · §E refutation
      with a dated catalyst.
- [x] **Cross-sector LIVE shortlist names included or explicitly dropped with reason** (§V) — 5
      admissible names disposed of individually; the **6 velocity-lit greens dropped as inadmissible
      inputs**, with the reason distinguished from a rejection.
- [x] **Numbers cross-checked; blanks are blanks** — price÷target reconciled for all three refiners;
      **`VLO`'s margin percentile and `LITE`'s multiples are left EMPTY**, not estimated.
- [x] **Flow/positioning cross-read present per candidate**, including FINRA short z and — for the
      finalists — the **implied move** (`MPC` ±4.4%, `LMT` ±3.0%, both D6 to 08-21).
- [x] **BET_SHEET.md written as ONE file.**
- [x] **No name was removed on narrative grounds while its measured flow still passed** — the
      LATE-MONEY tag on `COHR`/`LITE` **lowers conviction and restates the thesis; it does not remove
      them** (the 475150 precedent, −41.2pp / −26.9pp, applied).
- [x] **Set-aside names are in a ledger with a class AND both required fields** — three
      `missed_ledger` rows (§VI-b); **zero rejection rows, with the reason for the zero stated**.
- [x] **Epicenter-starter module present** because a cycle GAP was flagged (§I) — a partial core in
      the rank-2 cycle's epicenter is on the sheet **regardless of tape**, with the three expressions
      named and ranked by structure.
- [x] **Zero buy/sell recommendations.** Size is referenced once, as **"mechanical ¼"**, per G6.

---

# §B-FRESHNESS — filled by Stage 10 (L1·ALPHA), 2026-08-15

> ALPHA tags follow the **name**, not its sector's turn in the rotation. Every 🟡 carries a **dated
> re-check** and is handed to `carryover` so the next run re-reads it. Zero buy/sell language (P4).

## §B-0 · 🚨 The instrument question ALPHA is required to answer FIRST

**PREFLIGHT G1 = FAIL, so this stage may not issue a `theme_age`-derived freshness verdict.**
The falsification probe the stage mandates was run, twice, and the result is **not** the usual one:

| Probe | Result |
|---|---|
| `fts search Nvidia --days 7 --count --scope foreign` @ **22:14** | ❌ 5/5 `URLError` |
| **the identical command** @ **23:1x** | ✅ **3,729 hits** — *(via NEWS API)* |
| library path, same moment | ✅ **3,729** — the two agree exactly |

⇒ **The zero is NOT the market and it is NOT the pipe.** The tunnel flapped and recovered, reproducing
`P60` for a **second consecutive run** (08-14: 5/5 fail 22:15 → 3/3 success 22:34–22:55).
🚨 **But the `theme_age` revocation SURVIVES on a different and stronger ground — `D260`: its
acceleration denominator tracks the CORPUS, not the theme.** So this stage records `theme_age`'s
output and **does not cite it**:

`diesel crack` 🟡ACCEL age **27d** accel 6.12× (17 articles) · `Navy shipbuilding` 🟡ACCEL age **69d**
accel 5.36× (11) · `optical transceiver` ⚪ECHO age **80d** accel 1.22× (123).

★ **F1 — "🟢FRESH fired 0 times" — is recorded again, and this run can finally say WHICH of the two
legs causes it.** The gate is `age ≤14d AND accel ≥2×`. **Two of the three themes clear the
acceleration leg outright (6.12×, 5.36×) and BOTH fail on age (27d, 69d).** On a 90-day corpus,
"first appearance ≤14 days ago" selects only **newly coined words**, which is a statement about this
desk's strategy, not about the market (`D254` · `D250-KR`, now independently reproduced on the US
side). **The zero is arithmetic — and the arithmetic is the age leg, not the news.**

**Substitute actually used for the tags below** (declared): per-name **pool-normalised** article
velocity — d1 vs the d7 daily average, divided by the day's own pool ratio **1.782×** (`D255`).
Foreign pool **d1 9,705 / d7 38,115**. This is a count, not content; it says attention moved, never why.

## §B-1 · The tags

| Name | Freshness | pool-norm velocity (d1 / d7) | Residual & **dated re-check** |
|---|---|---|---|
| **`MPC`** *(held, §I)* | 🟡 **PARTIAL** | **0.82×** (10 / 48) | The **name** is quiet while its **theme** is the loudest thing on the board — **`diesel crack` 2.75×, the highest pool-normalised reading of any term measured this run**. ⚠ Residual: `MPC` trades **+11.9% above consensus**, **−1.3%** from its 52-week high, and `S88` says the node entered at the **100th percentile of two years**. **Re-check 2026-08-21 (`S88` · `S84` · `P62` all settle).** |
| **`PSX`** *(held, §I)* | 🟢 **LIVE** | **1.11×** (11 / 39) | The only refiner whose **own name** is accelerating, and the one `action_bracket` selected as the tape-independent CORE-STARTER against a **−0.898pp** rank-2 cycle GAP. Blocked from the 🟢 shortlist by `vol_surge` **1.01** alone. **No residual gate; re-check 08-21.** |
| **`VLO`** *(not held, §I)* | 🟡 **PARTIAL** | **1.06×** (7 / 26) | Residual is **measurement, not price**: its gross-margin percentile is **UNKNOWN (C3)** for a 3rd run (`D272`), and the analyst book is **hold-majority**. **Filed to `missed_ledger` (`R.타이밍대기`); re-check 2026-08-22.** |
| **`GD`** (§II) | 🔴 **RESOLVED → dropped from the bettable list** | **0.58×** (4 / 27) | 🚨 The **story** is 24 hours old and loud (Navy shipbuilding opened to foreign yards, `reuters` 08-15) **while the name's own coverage is DECELERATING at 0.58×** and its `vol_surge` is **0.52**. **The named beneficiaries were foreign-listed, not `GD`.** PREMORTEM already **dropped** the bracket for the same reason. ⚠ **Dropped as NOT-YET-BETTABLE, and it is NOT filed as a rejection** — see §B-2 |
| **`RTX`** *(held, §II)* | 🟡 **PARTIAL** | **0.71×** (2 / 11) | n=2 articles/day — **too thin to read in either direction (C3)**. The name is carried on **flow, not story**: OBV +0.381 매집, RS60 **+22.0**, momentum **BASED** (49% share). **Re-check 08-21 with the `GD` watch KPI.** |
| **`ABNB`** (§III) | 🟡 **PARTIAL** | **0.65×** (22 / 133) | Coverage **decelerating** while the price sits **−1.6%** from its 52-week high and **+5.3% above** a hold-majority consensus, with **63%** of its 60-day excess earned in the last 20 sessions. ⚠ **Momentum-only flag does NOT apply**: the accumulation axis **agrees** (OBV 매집), so this is not a tape trade. **Re-check 2026-08-21 (`S91`).** |
| **`KKR`** (§V) | 🟡 **PARTIAL** | **0.78×** (37 / 187) | Residual is **positioning**: FINRA short z **+1.62 = ⚡crowded-short**, which is **squeeze fuel, not a demand axis (D6)**. ⚠ **Hard-stop language required** if it is ever expressed. **Re-check 2026-08-22.** |
| **`COHR`** (§V) | 🔴 **RESOLVED → dropped from the bettable list** | **0.98×** (42 / 168) | 🚨 **The catalyst already fired.** Its `vol_surge` 1.67 — the reason it is the board's #1 flow score — **is its own 08-11/08-12 earnings print** (`yahoo_finance`: "Cisco, Coherent Are Earnings Movers Late"), and coverage has already flattened to **0.98×**. RS60 is still **−13.7**. **This is the exact "catalyst fired before thesis time" case ALPHA exists to catch.** ⚠ **One un-priced leg survives** — the FCC proposal to ban Chinese optical transceiver imports (China 56% share) — **and it is already bracketed by `S86` (08-21)** |
| **`LITE`** (§V) | 🔴 **RESOLVED → dropped** | **0.76×** (25 / 130) | Same mechanism, same dates: "Lumentum sees sales more than double" [`marketwatch` **08-11**], "Earnings Top Estimates" [`yahoo_finance` 08-12]. Coverage decelerating. **Carried by `S86`, not by this sheet** |
| **`EQIX`** (§IV) | 🟡 **PARTIAL** | **0.86×** (7 / 32) | Momentum is a **turn inside a drawdown** (exc60 −0.69, exc20 +3.60), not exhaustion. **Re-check 2026-08-21 (`S90`).** |
| **`DLR`** (§IV) | 🔴 **RESOLVED → dropped** | 🚨 **0.25×** (**1** / 16) | **One article in the last day.** The node's loudest *price* is its quietest *story*, and PREMORTEM measured its geometry as **exhaustion** (exc60 +1.64 with days 21–60 **−9.02**). **Price without narrative and without a base is the definition of a resolved move.** `S90` settles 08-21 |
| **`CBRE`** (§IV) | 🟡 **PARTIAL** | *(not measured)* | ⚠ **No velocity pulled** — stated rather than assumed. Carried on numbers (fwd **16.83×**, **PEG 0.97**, **+18.6%** to target) and on the node's only **based** momentum (days 21–60 **+9.49**). **Filed to `missed_ledger` (`Q.확신부족`); re-check 2026-08-22.** |

**Tally: 🟢LIVE 1 · 🟡PARTIAL 7 · 🔴RESOLVED 4.**
★★ **`🟢LIVE` fired — and the honest reason is that the gate CHANGED, not that the board got fresher.**
The `theme_age`-based 🟢FRESH gate returned **0 again** (§B-0); the one 🟢 above comes from the
**pool-normalised substitute**. **A gate that fires because it was replaced is not evidence of a
fresher market**, and the 08-14 run flagged exactly this trap about itself. Recorded so the streak is
not silently declared broken.

## §B-2 · Ledger discipline on the four 🔴 — and why only ONE becomes a rejection

The stage requires a 🔴 to be logged as a ledger row, **not prose**. Applying the rule honestly splits
them:

| 🔴 | Ledger | Reason |
|---|---|---|
| **`GD`** | **NEITHER — carried as an armed watch** | ⚠ **Its measured flow still passes** (OBV **+0.448**, the node's strongest; RS20 +2.9; RS60 +10.6). The stage's own rule: *when the flow gate still passes and only the story broke, RE-FILE — do not remove.* Removing it would repeat the **475150** error (**−41.2pp / −26.9pp** across two narrative-only rejections). **Restated thesis + dated re-check 08-21 on `GD` RS20 vs `SPY`, currently +2.9.** |
| **`COHR`** · **`LITE`** | **NEITHER — carried by `S86`** | Their flow also still passes (both OBV 매집, RS20 +12.9 / +21.9). They are **not** rejected; they are **priced by a print that already happened**, with one un-priced policy leg already bracketed. **Conviction lowered, names kept.** |
| **`DLR`** | ✅ **`reject_ledger` — filed** | This is the one where the **measured axes**, not the story, reject it: the price move is **20 sessions old on a negative 60-day base** (days 21–60 −9.02) and the narrative is **0.25×, one article**. Class **`B.모멘텀only`**, `--revives-if` **"S90 settles branch B, or days-21-to-60 excess turns positive"**, `--recheck-date` **2026-08-22** |

⚠ **Three of four 🔴 produce no rejection row, and that is the discipline working, not a gap** — the
ledger is for names the **measured** axes reject. Each of the three instead carries a restated thesis
and a dated re-check, per the rule that produced this stage's most expensive lesson.

## §B-3 · ✅ ALPHA EXIT CHECK
- [x] **Falsification probe run BEFORE any freshness verdict** (§B-0) — and it **refuted** the
      transport half of G1's revocation while the `D260` half **survives**, so `theme_age` output is
      **recorded and not cited**.
- [x] **F1's zero explained rather than re-counted** — the age leg fails at 27d/69d while the
      acceleration leg **passes** at 6.12×/5.36×.
- [x] **Every bet tagged** 🟢/🟡/🔴; **every 🟡 carries a dated re-check** handed to `carryover`.
- [x] **Every 🔴 is dropped from the bettable list** and dispositioned in a ledger **or** explicitly
      re-filed with a restated thesis under the flow-still-passes rule (§B-2). **One rejection row
      filed (`DLR`); three deliberate non-filings with reasons.**
- [x] **Momentum-only flag applied by grade (D6)** — `ABNB` checked and **cleared** (accumulation
      agrees, so not a tape trade); `KKR`'s residual is stamped as **positioning, not demand**.
- [x] **Names whose sector rotated out are still tagged** — `KKR` (FIN, no DEEP slot) and `COHR`/
      `LITE` (IT, no DEEP slot) all carry tags, per "tags follow the name".
- [x] **`ACTION_TICKETS.md` written**, and the mandatory undated Hormuz both-sides bracket was
      **hand-written into it** because `action_bracket` dropped it for the **2nd consecutive run**
      (`D263`).
