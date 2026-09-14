# BET_SHEET — industry_US — 2026-07-30 (Thu)

> **ONE file, per-sector sections §A–§E** (downstream desks glob this exact filename — never split).
> Benchmark **SPY** inline (C1). Flow/RS asof **2026-07-29 settled**; fundamentals pulled live
> 2026-07-30. **Sizing language is influence illustration only — zero buy/sell recommendation (P4).**

## ⚠ 0 · Four instrument caveats binding on every number below

1. **L2 is unrunnable on the majority of this sheet.** `margin_history.py` returns
   **`연간 데이터 없음` on VLO (6th run), XOM (2nd), PLD**, and **no health-care or REIT name has ever
   produced a usable percentile in this repo.** ⇒ **NO name in this file is called cheap or expensive
   (C3).** A forward multiple without a margin percentile is not a valuation.
2. **The 🟢 tag's arity changed between runs.** `velocity` is non-null on **50/300** today against
   **0/300** on 07-28 ⇒ **13 of 41 greens cleared on a velocity path with `vol_surge` below the gate.**
   Any green marked **(vel)** below would not have been green yesterday (D75).
3. **Today's US bar is unsettled** and **FRED's daily curve stops at 07-28** — the entire post-FOMC
   rate move is unmeasured. **No rate-driven number here is current.**
4. **27% of the real US book is untaggable**: **TSM ($382) and LNG ($780) sit outside `us_top300`**
   (M252) ⇒ any exposure percentage carries an unstated error bar.

---

# §A · ENERGY (OW−, continuous DEEP ①)

### Numbers

| Name | Trailing P/E | Forward P/E | Fwd EPS | Mean target | Margin percentile | flow | RS20 | RS60 | **days 21–60** |
|---|---|---|---|---|---|---|---|---|---|
| **MPC** | 20.63 | **11.28** | $27.77 | $303.89 | **~37.5th** (FY25 GM 10.0%, 8y median 10.5) | +0.60 🟡 | +23.1 | +24.2 | **+1.1** |
| **VLO** | 22.57 | **12.30** | $25.11 | $289.63 | ⚠ **BLANK, 6th run (D56)** | +0.50 🟡 | +18.0 | +20.8 | **+2.8** |
| **PSX** | — | — | — | — | ~55–60th | +0.62 🟡 | +24.7 | +16.2 | **−8.5** |
| **XOM** | 26.11 | 14.43 | $10.75 | $167.23 | ⚠ **BLANK (M233)** | +0.70 🟢 (vel) | **+17.0** | +1.4 | **−15.6** |

**Arithmetic cross-check**: forward EPS ÷ trailing EPS = **MPC 27.77/15.19 = 1.828 (+82.8%)**,
**VLO 25.11/13.68 = 1.836 (+83.6%)** — reproduces M234's *"forward EPS +83–87% above trailing"*
independently. ✅

### §B Thesis (freshness tag ← ALPHA)
**Refining margin, read on the second derivative, not the level.** The settled **distillate crack made
a window high 99.084 on 07-29 while crude rose +6.6%** and the **gasoline crack fell −2.541** — the
composite 3-2-1 turned down (−0.359) only because it averages two opposite legs. **The leg the thesis
rests on is still accelerating.** `[measured]`

### §C Flow / positioning
Sector is **#1 on both wflow (+0.558) and eqflow (+0.477)**, breadth 0.190, 3🟢/1🔴, and **XLE was the
only green sector on 07-29 (+1.88% vs SPY −1.54%)** with the **best 20-day excess on the board
(+12.75pp)**. FINRA 07-29: **XOM z −1.04 (5v5 −0.2·)**, **MPC z +0.93 (−6.1▼)**, **VLO z +0.88 (+3.4▲)**.
Implied moves: **MPC ±9.4% (expiry 08-21, D22 — COVERS its 08-04 print, usable)**;
**PSX ±2.7% (expiry 07-31 — EXPIRES BEFORE its 08-05 print, not event-priced)**.

### §D Competition / peers
One risk unit (**ρ +0.878, M147**) — MPC/VLO/PSX may not be counted as three positions.
**XOM is a separate expression with 0% refining** and is the *control*, not a peer.

### §E Refutation + dated catalyst
- ⚠⚠ **The composition is drifting toward the weakest bases.** **PSX — the human-locked `core_pick` —
  has a negative days-21-60 for a 3rd consecutive run (+1.6 → −5.91 → −8.5)**, while **MPC (+1.1) and
  VLO (+2.8) hold the only positive bases in a 16-name sector.**
- ⚠ **XOM is 927%-concentrated in its last 20 sessions** ⇒ **S31 branch A is tracking against us**, and
  **XOM prints 07-31 inside that window.**
- **Dated**: **Russian diesel-ban expiry 07-31** · **XOM 07-31** · **MPC 08-04** · **PSX 08-05** ·
  **S49 settles 08-06.**
- **Kill (frozen, S49)**: the **5-session change in the settled distillate crack ≤ −5.0 points by
  08-06** (now **+9.007**). ⚠ **Not a level — R30/D95 withdrew levels on this series.**

### ★ Epicenter-starter module (cycle GAP flagged this run)
`cycle_exposure`: **Energy (rank 2) epicenter 6.88% vs a required 8.0% ⇒ 🚨 GAP −1.119pp**, held
epicenter **{MPC, PSX}**, and the book touches the cycle otherwise only through **LNG — beta to the
consequence, not the engine**. ⚠⚠ **The flag's movement is denominator drift, not information**
(9th consecutive mark-to-market reading; the book fell $11,575 → $10,654). **The cleanest measured
epicenter expression on today's data is MPC** — the only refiner with a positive base *and* an
event-covering straddle. **Recorded as an exposure observation; this stage does not size (P4).**

---

# §B · FINANCIALS (OW−, continuous DEEP ②)

### Numbers

| Name | Trailing P/E | Forward P/E | Fwd EPS | Mean target | flow | RS20 | RS60 | **days 21–60** |
|---|---|---|---|---|---|---|---|---|
| **TRV** | 10.00 | **12.34** | $30.16 | $357.83 | +0.80 🟢 | **+20.2** | **+26.4** | **+6.2** |
| **BX** | 28.39 | 16.94 | $7.47 | $141.95 | **+0.83 🟢** (sector #1) | +12.3 | +1.2 | −11.1 |
| **MET** | — | — | — | — | +0.79 🟢 | +17.0 | +19.7 | **+2.7** |
| **MRSH** | — | — | — | — | +0.79 🟢 | +20.9 | +17.7 | −3.2 |
| **MA · V** | — | — | — | — | +0.65 / +0.70 🟢 (vel) | +12.0 / +9.8 | +12.5 / +11.2 | +0.5 / +1.4 |

⚠ **TRV's forward P/E (12.34) EXCEEDS its trailing (10.00)** ⇒ **forward EPS is BELOW trailing** —
the opposite of the refiners. Stated as a fact; **not** called expensive (§0-1).

### §B Thesis
⛔ **RESTATED THIS RUN, because the old one broke.** The OW was written on **breadth (eqflow > wflow)**.
**Re-derived and verified by direct recomputation: all-47 gap +0.0214; ex-BRK-B gap −0.0166.**
**BRK-B is 13.94% of sector cap at a flow score of +0.11, and removing that one row flips the sign.**
⇒ **the surviving carrier is not breadth — it is a 12-name INSURANCE node at eq-mean +0.603 = 1.48×
the sector, holding 3 of 8 greens.** `[measured]`

### §C Flow / positioning
8🟢 / 1🔴 of 47; **32 names pass the accumulation pre-condition and 24 are blocked by `vol_surge`
alone — the deepest base of any sector.** ⚠ **5 of the 8 greens are velocity-path (D75)**: at
yesterday's arity this sector shows **4**. FINRA 07-29: **JPM z +0.40, MA +0.95, TRV +0.55 (5v5 +5.4▲)**
— all inside normal range.

### §D Competition / peers
**{JPM, XLF} / {MA, V} / {CB, TRV} are three distinct residual units at ≤0.55 (M147)** — genuinely
three risk units, unlike Energy. ⚠ **But all three share a beta (JPM 0.932)**, so an IG-OAS event
hits them together (**S41**).

### §E Refutation + dated catalyst
- ⚠⚠ **Two of the OW's three stated legs are now dead or reversed** — the steepener (**R11**) and the
  breadth claim (§B above) — leaving **NII migration**, which nobody has measured.
- ⚠ **The exchanges node is the concentration problem**: **CME −32.0 · COIN −29.3 · ICE −29.1 ·
  PYPL −22.9 · NDAQ −20.1 days-21-60** ⇒ their entire 60-day relative move is a last-20 event, and
  **M135's registered RS60 test is BROKEN** (on frozen prices it can only report CONFIRM).
- ⚠ **PYPL's RS20 +37.4 is the sector's highest and it is a merger-arb spread**, pre-registered in
  **S14-ANNEX**; its days-21-60 is **−22.9**, which is that spread's signature.
- **Dated**: **S23/S19 windows close 08-05** · **S14 settles 08-06 (both readings recorded)** ·
  **the exchanges' replacement observable 08-07 (4 of 7 do not print inside it)** · **JPM 08-08**.
- **Kill**: **derived 2s10s ≤ +0.20 on a settled close by 08-05** (now **+0.35**, and it moved 1bp
  AWAY on the last settled print) **or HY OAS ≥ 3.10%** (now 2.84%, six consecutive widening prints).

---

# §C · HEALTH CARE (N → OW− this run, rotating DEEP ③)

### Numbers

| Name | Trailing P/E | Forward P/E | Fwd EPS | Mean target | flow | RS20 | RS60 | **days 21–60** |
|---|---|---|---|---|---|---|---|---|
| **TMO** | 30.28 | 20.45 | $27.49 | $627.62 | **+0.88 🟢** (sector #1) | +17.3 | +21.6 | **+4.3** |
| **HCA** | **13.32** | **12.35** | $32.18 | $452.81 | +0.61 🟢 `new` | +7.0 | −7.0 | **−14.0** |
| **ABT** | — | — | — | — | +0.59 🟡 | **+21.3** | +19.5 | −1.8 |
| **HUM** *(watch, not candidate)* | — | — | — | — | **−0.21 🟡** | −5.7 | **+55.2** | **+60.9** |

⚠ **HCA's forward P/E (12.35) is barely below trailing (13.32)** — a flat-EPS profile, **not** a
cyclical trough. And per §0-1, **no percentile exists for any of these names**, so **none is called
cheap.**

### §B Thesis
**C7's resolving observable fired for the first time in four runs** — **HCA is a 🟢 unambiguously
outside the Health Care top-6 by cap (13th, $83.2bn)**, with **TMO borderline (7th, $172.7bn against
AMGN's $182.2bn = a 5.2% gap)**. **XLV is the board's best 5-day sector (+6.67pp excess vs SPY).**
`[measured]`

### §C Flow / positioning
wflow +0.360 / eqflow +0.300, 4🟢/2🔴 of 32, breadth 0.120; **15 of 32 pass the accumulation
pre-condition, 11 blocked by `vol_surge` alone.** FINRA 07-29: ⚠ **ABT z +0.78 with 5v5 +10.2▲** —
**short pressure BUILDING on the sector's best A-grade name.**

### §D Competition / peers
Node spread **tools +0.49 vs biotech +0.07 = 0.42 flow points against a sector eqflow of +0.300**
⇒ **the spread is 140% of the level — the sector label is the wrong unit (W5).**

### §E Refutation + dated catalyst
- ⚠⚠ **C7 is NOT resolved and this sheet must not inherit a resolution.** The "top-6" was never
  defined; **the desk's own named block contains TMO and not AMGN**, so the observable returns **1 or
  2 depending on an undocumented choice (C5)**.
- ⚠ **The two names that answer it have opposite geometry**: **TMO's base is +4.3; HCA's is −14.0**,
  i.e. **the cleaner definitional answer is the weaker structural one.**
- ⚠ **A-grade and B-grade disagree on ABT** (price best in sector, short pressure building) ⇒
  **`indistinguishable` (C4)**, reported rather than resolved.
- **Dated**: **HUM ledger recheck 07-31** · **MRK 10-Q 08-04** (promotes or retracts the IPR&D-charge
  reading) · **C7 second read 08-06.**
- **Kill**: the outside-top-6 green count returning to **0** on the 08-06 read, **or** XLV's 5-day
  excess turning negative while SPY rises (= defensive rotation, not sector demand).

---

# §D · REAL ESTATE (N → OW− this run, rotating DEEP ④)

### Numbers

| Name | Trailing P/E | Forward P/E | Fwd EPS | Mean target | flow | RS20 | RS60 | **days 21–60** |
|---|---|---|---|---|---|---|---|---|
| **PLD** | — | **42.49** (fwd **>** trailing 32.20) | — | — | +0.86 🟢 | +9.7 | +1.6 | −8.1 |
| **AMT** | 28.02 | 25.00 | $6.95 | $214.74 | +0.73 🟢 `new` | **+11.9** | −2.5 | **−14.4** |
| **DLR** | — | ⚠ GAAP 67.87 is a **category error**; on AFFO **24.4×** (M151) | — | — | +0.73 🟢 `new` | +7.1 | −7.5 | −14.6 |
| **CCI** | — | **16.3× AFFO**, +28.0% to target | — | — | +0.69 🟢 `new` | +6.8 | −12.6 | **−19.4** |
| **SPG** *(unowned, no thesis)* | 63.88 | 34.12 | $6.74 | $227.95 | **+0.05 🟡** | +7.7 | **+15.2** | **+7.5** |

### §B Thesis
**The board's best breadth (0.330) and its ONLY zero-red sector**, with **three names igniting in one
session (AMT Δ+0.70 · CCI Δ+0.82 · DLR Δ+0.50 — the board's three largest deltas).** `[measured]`

### §C Flow / positioning
4🟢 / 0🔴 of 12. ★ **None of the four cleared on the velocity path** (`vol_surge` all ≥1.21) ⇒
**unlike Financials, this green count is comparable across runs.** **XLRE fell only −0.11% on a
−1.54% SPY session.**

### §D Competition / peers
Grouped by **M131's measured units, not GICS**: {AMT, CCI} duration · {DLR, EQIX, IRM} data-centre ·
{PLD} logistics · {WELL, VTR} health · {SPG, O, PSA, CBRE} retail/storage. ⚠ **The data-centre unit is
internally split by 1.09 flow points (DLR +0.73 vs EQIX −0.36).**

### §E Refutation + dated catalyst
- ⚠⚠ **Every one of the four greens has a NEGATIVE 60-day base**, and **the deepest base in the sector
  (SPG, +7.5, RS60 +15.2) is 🟡 with the second-worst flow score and carries no thesis anywhere.**
  ⇒ **this promote rests on 20-day money, not 60-day structure.**
- ⚠⚠ **The binding constraint is credit, not AI (M134)** — and it is moving **against** the sector:
  **HY OAS 2.84% on six consecutive widening prints; IG OAS 0.81%, 9bp from S41's line.**
  **That is the strongest argument against this run's own promote, and it is not a real-estate
  argument.**
- ⚠ **Three names that M131 measured into different units ignited on the same day** — **n=1 (S1)**;
  **no re-clustering is run on one day's data**, and **S25 settles it 08-08.**
- **Dated**: **EQIX printed 07-30 (S25's second settling point, NOT read at this run clock)** ·
  **S25 08-08** · **S41 08-12** · **K8 ≈08-21.**
- **Kill**: **IG OAS ≥ 0.90% on a close**, or all four greens losing the tag on the next settled sweep.

---

# §E · CROSS-SECTOR LIVE SHORTLIST (names outside the four DEEP sectors)

From `US_LIVE_SHORTLIST.json` (mcap ≥$10B, 🟢, top-15 by flow) plus EVENT_ALPHA's one CONFIRMED-EARLY.

| Name | Sector | flow | RS20 | RS60 | **days 21–60** | Short (FINRA 07-29) | Status |
|---|---|---|---|---|---|---|---|
| **AAPL** | IT | +0.70 🟢 (vel) | **+19.2** | **+19.5** | **+0.2** | 1.0% float building, P/C 0.62 | ★ **CONFIRMED-EARLY (EVENT_ALPHA Card 5) — and it PRINTS TONIGHT.** Fwd P/E 34.39, mean target $319.72. ⚠⚠ **Revived on the ledger this morning; base is arithmetically ZERO; bracketed by S46** |
| **GRMN** | DISC | **+1.00** (board #1) | +26.4 | +20.4 | **−6.0** | **z −2.09 ✅ clean rise** | ⚠ **129% last-20 concentration and NO thesis anywhere.** Carried as a coverage gap, not a candidate |
| **RTX** | INDU | +0.94 | +15.8 | +22.5 | **+6.7** | z +0.52 △ | **Held name.** The one prime whose W4 is closed from primary filings |
| **UNP · NSC · CSX** | INDU | +0.91 / +0.81 / +0.78 | +9.7 / +9.0 / +9.1 | +8.5 / +5.1 / +11.3 | −1.2 / −3.9 / +2.2 | NSC z −0.88 ✅ | ⚠⚠ **~8 of UNP's 12 revenue growth points are fuel surcharge (M91) — this is the ENERGY bet again, not a diversifier.** **S49 branch B hits it and §A on one tick** |
| **GD** | INDU | +0.84 `new` | +9.9 | +8.9 | −1.0 | **z −1.42 ✅ clean rise** | Printed 07-29 with no bracket (dropped: neither branch changed a conclusion) |
| **TRI** | INDU | +0.83 `new` | **+32.5** | +13.8 | **−18.8** | z +0.65, ⚠ base20 74.3% **out of band ⇒ verdict SUPPRESSED (D52/D73)** | ⚠ **236% concentration, no thesis, and silently unindexable by the ledger (D101)** |
| **ITW · MMM · WAB · PCAR** | INDU | +0.83 / +0.79 / +0.77 / — | +10.4 / +12.2 / +10.5 / +13.8 | +13.3 / +23.7 / +8.9 / +14.2 | +2.9 / +11.5 / −1.6 / +0.4 | — | **S42's basket, median RS20 +11.38, control CAT at −24.04 and diverging** |
| **PCG** | UTIL | +0.90 | +7.6 | +6.4 | −1.2 | z +0.01 △ | **Utilities' only 🟢, 3rd run.** ⚠ **Does not report until 2026-10-22 ⇒ it cannot be what the sector is trading this week** |
| **MDLZ** | STPL | +0.87 `new` | +14.7 | +4.7 | −10.0 | **z −0.77 ✅ clean rise** | ⚠ **Staples is the board's 2nd-best 5-day sector and NO proposition claims it — 2nd run** |
| **BKR** | ENRG | **+0.93 `new`** | +8.1 | −16.3 | **−24.4** | z +1.16 △ | ⚠⚠ **ON THE REJECT LEDGER** (`A.flow미도착`, recheck **08-14**) on a basis (*"the only negative flow score of 11"*) **that is now false** — ★ **not resolved early (S1); named so the 08-14 audit cannot call it unforeseen** |

**Clean-rise set (🟢 ∧ low-short/covering)**: **GRMN · MDLZ · PLD · GD · NSC.**

---

## §F · Ledger actions this run

**Filed at EVENT_ALPHA (both required fields, script-enforced):**
- **QCOM** `K.본문반증` — revives-if *"RS20 vs SPY turns positive AND the Apple-content leg is replaced
  by a named design win"*, recheck **2026-08-13**.
- **CIEN** `C.차트붕괴` — revives-if *"RS20 vs SPY recovers above −10 AND the optical median turns
  positive"*, recheck **2026-09-30**.

**Resolved at HANDOVER**: **AAPL → `revived`** (S13's categorical condition met; 🟢 on both RS windows)
· **000810 → `reaffirmed`** on a fresh full-axis pull.

**⚠ Set aside WITHOUT filing, and the reason is a rule, not an oversight** — **no name was removed on
narrative grounds while its measured flow still passed**:
- **GEV · VRT · ETN · PWR · VST** — all 🔴 today, **but they are the exposure map of an armed bracket
  (S24, → 08-12)**. Filing them converts a bracket into a rejection and destroys its scoring.
- **SPG · GRMN · TRI · CTAS · MDLZ** — **measured flow passes on every one**; what is missing is a
  **thesis**, and *"we have not written a thesis"* is not a rejection reason. **Re-filed as coverage
  gaps with dated re-checks (08-12/08-13) rather than dropped** — the 475150 precedent applied
  forward rather than re-learned.
- **HUM** — flow −0.21 fails, **but its ledger recheck is 07-31 (tomorrow)** and it carries the
  **deepest 60-day base measured anywhere this run (+60.9)**. **Not pre-empted (S1).**

## ✅ EXIT CHECK

- [x] **Every DEEP sector has a section** (§A ENRG · §B FIN · §C HLTH · §D RE); **cross-sector LIVE
      shortlist names are in §E**, with the two that were not carried forward (**GRMN, TRI**)
      **explicitly labelled coverage gaps with their reason**, not dropped.
- [x] **Numbers cross-checked**: the ex-BRK-B breadth reversal was **recomputed directly from all 47
      rows (+0.0214 → −0.0166)**, and the refiners' forward/trailing EPS ratio **independently
      reproduces M234 (+82.8% / +83.6%)**. **Blanks are stated as blanks** — VLO's and XOM's margin
      percentiles, every REIT's and health-care name's, PSX's live multiples.
- [x] **Flow/positioning cross-read present per candidate** (flow tag · RS20 · RS60 · days-21-60 ·
      FINRA z with its baseline where in-band). **BET_SHEET.md written as ONE file.**
- [x] **Every set-aside name is either in the ledger with a class AND a `--revives-if`, or is
      explicitly re-filed as a coverage gap with a dated re-check** (§F). **No permanent bans written
      this run.**
- [x] **No name was removed on narrative grounds while its measured flow still passed** — five such
      names are re-filed under coverage-gap status, and **BKR's now-false rejection basis is named
      without pulling its recheck date forward.**
- [x] Linter — see below.

## §B-FRESHNESS · ALPHA gate (appended by stage 9 — tags, evidence label, date)

### The deterministic gate first, and it CHANGED STATE this run

`theme-age`, ten probes, `--scope foreign`, 90d window:

| Theme | verdict | age | 7d mean | accel | n |
|---|---|---|---|---|---|
| **CXMT** | 🟡ACCELERATING | 78d | 38.3 | **17.14×** | 351 |
| capex guidance | 🟡ACCELERATING | 65d | 16.3 | 4.29× | 300 |
| **tower REIT** | 🟡ACCELERATING | 63d | 0.6 | 3.43× | ⚠ **11 — UNUSABLE at this n** |
| refining margin | 🟡ACCELERATING | 63d | 5.4 | 3.26× | 92 |
| optical transceiver | 🟡ACCELERATING | 65d | 2.1 | 2.30× | 63 |
| insurance | 🟡ACCELERATING | ≥90d | 119.1 | 2.11× | 3,525 |
| **rate hike** | **⚪ECHO** | ≥90d | 101.1 | 1.83× | 4,081 |
| **data center power** | **⚪ECHO** | 69d | 9.6 | 1.54× | 358 |
| **life sciences** | **⚪ECHO** | ≥90d | 16.4 | 1.34× | 667 |
| **distillate crack** | **🔴FADING** | 15d | **0.0** | **0.00×** | ⚠⚠ **2 in 90 days** |

★★ **M112 / M154 / M180 / M210 / M243's "zero discrimination" is BROKEN this run — and that is the
first change in seven measurements.** Six prior foreign-feed runs returned **all-🟡, zero FRESH, zero
FADING**. Today the instrument returns **three distinct verdicts (6 🟡 · 3 ⚪ECHO · 1 🔴FADING)**.
**The tool discriminates; it just has not had anything to discriminate before.**

⚠ **Still ZERO 🟢FRESH** ⇒ **this run issues ZERO 🟢LIVE tags — a 7th consecutive foreign-feed
measurement.** The gate is deterministic and is not overridden.

★★★ **Three cross-axis disagreements that this gate exposes, none of them resolved here (C4):**
1. **`rate hike` reads ⚪ECHO (1.83×) while the SAME window's thread axis has the Fed/Warsh saga
   BUILDING at 6→6→5→7→9→12 outlets over six days.** ⇒ **the term axis and the event axis disagree
   about the board's loudest story.** M186's *"a term spikes when it is new; an event ranks when it is
   big"* — measured again, now with the term explicitly stale.
2. **`distillate crack` returns 2 articles in 90 days and 0.0 in the last 7.** ⇒ **the desk's single
   most load-bearing KPI — the observable S49 was just frozen on — has essentially NO narrative
   coverage at all.** That is **not** a defect in the observable (a price is a price), but it means
   **the news axis can neither corroborate nor contradict §A**, and every ENRG claim rests on the
   price series alone. **Stated so no later stage mistakes narrative silence for confirmation (C6).**
3. **`life sciences` reads ⚪ECHO while Health Care is the board's best 5-day sector.** ⇒ **C7's
   original "money without narrative" finding replicates a 6th time**, now from the term axis rather
   than from the thread count.

### Tags

| Name | Tag | Evidence label · date | Residual / re-check |
|---|---|---|---|
| **MPC** | 🟡PARTIAL | `[measured]` distillate crack at a window high 99.084, only refiner with a positive base **and** an event-covering straddle (±9.4%, D22) · 2026-07-29 | **Residual: its own print.** Re-check **2026-08-04** |
| **VLO** | 🟡PARTIAL | `[measured]` days-21-60 **+2.8**, the sector's best base · 2026-07-29 | **Residual: the margin percentile is a 6-run structural blank (D56) ⇒ no cheapness claim is available.** Re-check **2026-08-06** (S49) |
| **PSX** | 🟡PARTIAL, **downgraded** | `[measured]` days-21-60 **−8.5**, negative and deteriorating a 3rd run · 2026-07-29 | ⚠ **Residual: it is the human-locked `core_pick` and the degrading leg.** Re-check **2026-08-05** |
| **XOM** | 🟡PARTIAL, **momentum-only** | `[measured]` RS20 +17.0 / RS60 +1.4 ⇒ **927% last-20 concentration** · 2026-07-29 | ⚠ **HARD-STOP STAMP.** Residual: **S31 settles 2026-08-05** and it prints **07-31 inside the window** |
| **TRV** | 🟡PARTIAL | `[measured]` 🟢 with days-21-60 **+6.2** — a real base, improved from M150's 98.6% to 76% last-20 share · 2026-07-29 | Re-check **2026-08-06** |
| **MET · MRSH · BX** | 🟡PARTIAL | `[measured]` 🟢 volume-path; MET base **+2.7**, MRSH −3.2, **BX −11.1** · 2026-07-29 | ⚠ **BX's base is the weakest of the three and it is the sector's #1 flow score.** Re-check **2026-08-08** |
| **MA · V · JPM · BAC** | 🟡PARTIAL, **instrument-flagged** | `[measured]` 🟢 **on the velocity path only** (`vol_surge` 0.75–0.88, below the 1.20 gate) · 2026-07-29 | ⚠⚠ **At yesterday's gate arity these four are NOT green (D75).** MA's beat landed **inside its own pre-declared ±3.9% no-information band.** Re-check **2026-08-06** |
| **TMO** | 🟡PARTIAL | `[measured]` sector #1 flow, base **+4.3**, the only HLTH node where flow and base agree on all constituents · 2026-07-29 | Re-check **2026-08-06** |
| **HCA** | 🟡PARTIAL, **momentum-only** | `[measured]` 🟢 `new_green` and the unambiguous answer to C7, but days-21-60 **−14.0** · 2026-07-29 | ⚠ **HARD-STOP STAMP.** Re-check **2026-08-06** |
| **ABT** | 🟡PARTIAL, **A-vs-B disagreement** | `[measured]` RS20 +21.3 / RS60 +19.5 (A-grade, best in sector) against **FINRA 5v5 +10.2▲** (B-grade, short pressure building) · 2026-07-29 | ⚠ **Reported as a disagreement, NOT resolved by picking the louder axis (D6/C4).** Re-check **2026-08-06** |
| **PLD · AMT · DLR · CCI** | 🟡PARTIAL, **momentum-only, all four** | `[measured]` 🟢 volume-path with **every base negative** (−8.1 / −14.4 / −14.6 / −19.4) · 2026-07-29 | ⚠⚠ **HARD-STOP STAMP on all four.** Residual: **the binding constraint (IG OAS) is 9bp from S41's line.** Re-check **2026-08-08** (S25) |
| **AAPL** | 🟡PARTIAL, **binary-pending** | `[measured]` 🟢 (vel), RS20 +19.2 / RS60 +19.5, but days-21-60 **+0.2 = an arithmetically zero base** · 2026-07-29 | ⚠⚠ **PRINTS TONIGHT. Bracketed by S46.** Re-check **2026-08-13** |
| **SPG** | 🟡PARTIAL, **unowned** | `[measured]` the sector's deepest base (+7.5, RS60 +15.2) with flow +0.05 and `vol_surge` 0.61 · 2026-07-29 | **Residual: no thesis exists anywhere.** Re-check **2026-08-12** |
| **GRMN · TRI · CTAS · MDLZ · PCG** | 🟡PARTIAL, **coverage gaps** | `[measured]` flow passes on all five; **no thesis on any** · 2026-07-29 | Re-check **2026-08-12/13**. ⚠ **PCG does not report until 2026-10-22 ⇒ it cannot be what its sector is trading this week** |
| **QCOM** | 🔴RESOLVED → **DROPPED and LEDGERED** | `[measured]` 🔴분산 −0.83, **RS20 −13.4 AND RS60 −13.3 — negative on both windows**; guided weak on cost inflation + loss of Apple modem content · 2026-07-30 | **Ledger row filed** `K.본문반증`, revives-if *"RS20 vs SPY turns positive AND the Apple-content leg is replaced by a named design win"*, **recheck 2026-08-13** |
| **CIEN** | 🔴RESOLVED → **DROPPED and LEDGERED** | `[measured]` RS20 −30.3 / RS60 −39.5, 🔴, into a newly funded $6.8bn direct competitor · 2026-07-30 | **Ledger row filed** `C.차트붕괴`, revives-if *"RS20 recovers above −10 AND the optical median turns positive"*, **recheck 2026-09-30** |

★ **Carry-forward rule executed, not logged**: **all 24 tagged names above carry an explicit re-check
date and are handed to the next run's inheritance packet INDEPENDENTLY of whether their sector holds
a DEEP slot** — the 006360 lesson (an ALPHA-tagged name with +64.4% consensus upside went unowned for
five sessions because its sector rested).

## §G · Rule-linter result

`python -X utf8 scripts/report_lint.py "llm_outputs/2026-07-30/industry_US/BET_SHEET.md"` →
**✅ 0 findings** across **C1 · C2 · S6 · D6**. No exemptions claimed. ⚠ Form only (C1 · C2 · S6 · D6); a clean run is not a correct report, and in this file
the thing it cannot see is **§0-1: most of these multiples have no margin percentile beside them, so
none of them is a valuation.**
