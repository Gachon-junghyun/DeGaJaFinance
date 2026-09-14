# MACRO_REPORT — industry_US · 2026-09-12 (Sat) · Stage 3 / L1·MACRO

> Written **22:20–22:50 KST, NYSE closed** — every price below is a **settled 2026-09-11 close**
> (no partial bar can enter; `D577` moot today). The 14:52 invocation stopped after HANDOVER; this
> stage inherits its PREFLIGHT/HANDOVER (plus the 22:10 addenda) and writes MACRO fresh.
> Sources this stage actually ran: `catalyst_calendar --days 10` (22:12) · `module_macro_us --json`
> (22:14, 17 series, `[FRED]`) · `us_flow --cot` + FINRA (15:07 file, `[COT 09-08 ref / FINRA 09-11]`)
> · `SECTOR_FLOW_US.json` (asof 09-11, 3-axis `nonews`) · a direct `yfinance` pull (39 ETFs/futures +
> the 300-name price frame) for the sector table and `D93` percentiles · `thread --days 7 --date
> 2026-09-08 --scope foreign` and `brief 09-08 --body 2` **from the local title derivative** ·
> **three `[WebSearch]` reads** (Yahoo/CNBC/The National/STAT) used **only** to attach a cause to
> the 09-09→09-11 sessions the desk's own feed cannot see.
> **Previous MACRO_REPORT read** (09-08, propositions §D, matrix §E, DRIFT addendum §5) — the
> continuity anchor. Ledger cross-read via HANDOVER (`module_report_tags show`, 85 reports).

---

## §0 · 🚨 Instrument state governing every line below (`preflight/PREFLIGHT.md` + 22:10 addendum)

| gate | verdict | consequence in THIS report |
|---|---|---|
| **G1 news** | 🔴 **FAIL — total, 7 h and counting** (ngrok 404 on every probe 14:52 / 15:15 / 22:10) | **No term sweep, no `theme-age`, no `blindspot`, no `chain-hop`** — §B-4/B-6 are recorded as **UNMEASURABLE**, not quiet. Narrative for 09-09/-10/-11 is **`[WebSearch]`** (3 reads) or `[inferred]`; only titles ≤ 09-08 are `[news_vectors.db]` |
| **G2 scale** | ✅ 3-axis continuous; `delta` = **09-04 → 09-11** (one week) | Δflow is quoted as a *weekly* change, never "today's" |
| **G3 sign owner** | STPL/WMT flips; **COMM/Alphabet flips at issuer level** | those two sectors get `eqflow`/breadth only |
| **G4 units** | 11 / 11 / 10 at 250/500/750d | any concentration line carries `--days` |
| **G5 universe** | 59 days stale | equal-weight columns govern; cap shares not quoted as current |
| **G0** | `EA` NaN | no `EA` verdict |
| **`[FRED]` clock** | `DGS2/5/10/30`, `DFII10`, `VIXCLS`, `hy_oas` end **09-10**; `T10YIE` ends **09-11**; `DXY` **09-04**; CPI/core Aug (published 09-11); NFCI 09-04 | the H.15 split reproduces a 4th time post-lift (`R147`: no forecast of the unblock). **09-11 rates are quoted from CBOE `^FVX/^TNX/^TYX` and named as such** |

**Three-line summary.**
> (1) **The week's macro fact is a Fed HIKE being priced into 09-16** — `[WebSearch]` CME FedWatch **87%**
> post-CPI (from 69%), first hike since July 2023, to 3.75–4.00% — and the tape agrees on the desk's own
> instruments: `[FRED]` `DGS2` **4.37 → 4.56 (+19 bp, 09-04→09-10)** with fed funds **3.63** (a **+93 bp**
> 2y-over-funds wedge), `DGS10` **4.78 → 4.95**, CBOE 10y **4.97 on 09-11** (highest since Oct-2023),
> the 30y−5y slope **69.6 → 56.3 bp = bear-flattening past a 2nd-percentile level** (`P138`-B).
> (2) **The move is REAL-yield-led over the week and INFLATION-flavoured on one session**: `DFII10`
> **2.43 → 2.55 (+12 bp)** vs `T10YIE` **2.35 → 2.40 → 2.36 (+1 bp net)**; the PPI session alone priced as
> inflation (`P147`-A, `TIP−IEF` +0.343%). Aug CPI `[FRED]`: headline **+0.40% MoM / +3.35% YoY**
> (July +3.30%), core **+0.29% MoM / +2.45% YoY** (July +2.47%) — headline accelerating on energy, core flat.
> **Credit did not move**: `hy_oas` **2.68 → 2.70**, `ig_oas` 0.81 → 0.80, NFCI −0.564 (7th straight easing).
> (3) **Oil is the other axis and it cleared $100**: WTI **91.48 → 100.05 (+9.4%)**, Brent 96.28 → 104.61,
> heating oil +9.2% (crack **108.24, new high**, `P140`-B); `[WebSearch]` Hormuz transits **7/day Thursday
> from 18 Tuesday**, Houthis seized **Mokha** near Bab al-Mandeb; Friday −1.8% on an Iran–Gulf meeting in
> Oman. **The equity leg did not follow**: `XLE` +1.7% on the week, EW Energy exc5 **+1.57pp vs SPY = 55th
> pctile** while the barrel sits at the **99th** — the barrel/equity 20-session gap is at its **9.9th pctile**.

---

## §A · Indicators — `[FRED]` first, publication clock stated

### A-1 · Rates: hikes are priced, the curve bear-flattened, and the front end led

| series `[FRED]` | 09-04 | 09-08 | 09-09 | 09-10 | Δ 09-04→09-10 | 09-11 (CBOE proxy) |
|---|--:|--:|--:|--:|--:|--:|
| `DFF` fed funds | 3.63 | 3.63 | 3.63 | 3.63 | 0 | — |
| `DGS2` | 4.37 | 4.39 | 4.43 | **4.56** | **+19 bp** | — |
| `DGS5` | 4.54 | 4.57 | 4.61 | **4.75** | **+21 bp** | `^FVX` **4.79** (+24 bp on 09-11 vs 09-04) |
| `DGS10` | 4.78 | 4.80 | 4.83 | **4.95** | **+17 bp** | `^TNX` **4.97** |
| `DGS30` | 5.24 | 5.25 | 5.28 | **5.37** | **+13 bp** | `^TYX` **5.35** |
| `DFII10` real 10y | 2.43 | 2.43 | 2.46 | **2.55** | **+12 bp** | — |
| `T10YIE` breakeven | 2.35 | 2.37 | 2.37 | 2.40 | +5 bp | **2.36** (−4 bp on CPI day; **+1 bp** net on the week) |
| `SOFR` | 3.65 | 3.64 | 3.64 | 3.62 | −3 bp | — |

- **2y − fed funds = +93 bp.** The front end is pricing a hiking cycle, not one hike. `[WebSearch]`
  (Yahoo 09-11): FedWatch **87%** for a 25 bp hike on 09-16, "the first since July 2023", Fed Chair
  **Warsh**'s inflation-fighting remarks referenced. **The desk's own `P138` settled B on 09-11** (30y−5y
  −13.3 bp) — *Fed path dominates the curve*; `P143`'s yen/term-premium channel did not own the US curve.
- **Real vs breakeven, both halves (`C2`-style pairing):** over the week **real +12 / breakeven +1** ⇒
  the repricing is a **real-rate / policy-path** move, **not** an inflation-expectations move — the
  opposite of the 09-08 report's read *for the PPI session*, which `P147`-A settled as inflation-flavoured
  (`TIP−IEF` +0.343% on 09-10). **Both are true at different windows** (`D531`) and are recorded as such.
- 🚨 **`P142` (`DGS2` level, settle "first `[FRED]` close covering 09-11") remains blocked** by the H.15
  split; bound: `DGS2` 09-10 **4.56 = +19 bp over the window**, past A's +10 bp — the low-information
  branch. Not scored until 09-11 prints (`R147`: no unblock forecast).

### A-2 · Credit: quiet on the instrument, and it stayed quiet through a hike repricing and $100 oil
`hy_oas` **2.65 (09-01) → 2.68 (09-04) → 2.71 (09-09) → 2.70 (09-10)** — +2 bp on the week, within
**~8 bp of its 365-day low**. `ig_oas` **0.81 → 0.80**. `nfci` **−0.564 (09-04)**, easing for a 7th
consecutive week. **`P128` settled C (+2 bp)** on exactly this. ⇒ Any "risk-off" sentence in this
report is **narrative-only** unless it cites these; none does. The one risk instrument that moved is
**`VIX` 14.53 → 17.84 (09-10) → 15.84 (09-11 CBOE)** — a rates/oil-vol spike that mean-reverted on the
CPI relief day, with credit spreads never joining.

### A-3 · Growth/inflation monthlies — lag stated
- **Aug CPI (published 09-11)**: headline index 334.131 = **+0.40% MoM · +3.35% YoY** (July +0.07% MoM
  / +3.30% YoY); core 337.765 = **+0.29% MoM · +2.45% YoY** (July +0.22% / +2.47%). `[WebSearch]` reads it
  as "matches expectations; core monthly 0.3% above the 0.2% forecast". **Headline accelerating on
  energy, core flat** — like-for-like MoM windows.
- Unemployment **4.1% (Aug)**, unchanged from July; M2 **23,218 (July, +0.4% MoM, +3.9% YoY)** — one to
  two months old, stated.
- `DXY` `[FRED]` ends **09-04 (118.07)**; `[yfinance]` `DX-Y.NYB` **99.16 → 99.12** on the week = flat
  (different index construction; both stated). `JPY=X` **155.66 → 153.55 (−1.35% = yen stronger)** —
  `P143`'s premise (yen at a 7-month high on BoJ-hike odds, thread 5→2→2→5 `[titles ≤09-08]`) is live
  into its 09-14 settle.

### A-4 · Oil and gas — the level, the product, the equity leg
| | 09-04 | 09-08 | 09-09 | 09-10 | 09-11 | week |
|---|--:|--:|--:|--:|--:|--:|
| `CL=F` WTI | 91.48 | 93.03 | 96.05 | **102.48** | 100.05 | **+9.4%** |
| `BZ=F` Brent | 96.28 | 97.92 | 101.21 | **107.63** | 104.61 | +8.7% |
| `HO=F` heating oil | 4.54 | 4.57 | 4.80 | **5.06** | 4.96 | +9.2% |
| `NG=F` Henry Hub | 2.97 | 2.92 | 2.82 | 2.83 | 2.83 | **−4.8%** |
| `XLE` | 64.06 | 64.77 | 65.31 | 64.93 | 65.14 | +1.7% |
| `LNG` / `GLNG` / `FLNG` | 292.00/52.12/31.51 | 276.02/51.46/30.98 | — | — | 278.34/52.89/31.70 | −4.7% / +1.5% / +0.6% |

- **Three settled verdicts today say the same thing** (`S149`-A barrel +9.4% · `P122`-A positioning
  followed to the 75th pctile · `P140`-B crack LEVEL to a new high **108.24**): the escalation is priced
  in the barrel and the product, and **the desk's `L1` (rate-over-level) lens lost on the crack**.
- **The equity leg lags by a percentile-extreme margin**: `XLE` 5-session return minus `CL=F` 5-session
  return = **−8.78 = 7.9th pctile** of the trailing 252; the 20-session gap **−16.46 = 9.9th pctile**
  (`CL` +23.1% / `XLE` +6.7% / `SPY` −1.75% over 20 sessions). Inside the sector the barrel names led
  (`VLO` +5.3, `DVN` +4.5, `XOM` +4.1) and services/midstream lagged (`BKR` −7.0, `SLB` −2.5, `WMB` −1.8).
  ⇒ **`P149` below brackets whether the equity leg closes the gap or keeps discounting $100 as transient.**
- **US gas is disconnected from the global scarcity**: `NG=F` −4.8% on the week with `[COT]` nat-gas
  spec at the **0th percentile (crowded short, −219,767, −10,856 WoW)** while `P145`'s premise (Asia LNG
  5-month high, European gas up) is a *foreign* gas story. **`D6`: COT-contrarian is REJECTED — the
  0th percentile is context, not a rebound call.** `P145`'s basket `EW{LNG,GLNG,FLNG}` sits at
  **−0.10pp vs `SPY` (09-04→09-11)** with one session to its 09-14 settle — leaning C, stated not scored.

---

## §B · News — the axis is DEAD; what is written here is titles ≤ 09-08 plus three web reads

### B-0 · Coverage stated first
- **Remote pipe: 0 of 8 probes answered (404), 14:52 → 22:10.** No term sweep, no `theme-age`, no
  `blindspot`, no `chain-hop` ran. **§B-4 and §B-6 are UNMEASURABLE**, and no "quiet" claim appears
  anywhere in this report (`C3`).
- **Local title derivative, `--scope foreign`, `brief --date 2026-09-08 --body 2`**: **4,811 articles →
  760 events**, head (≥5 outlets) **91**, non-market **0** (the classifier is Korean-only ⇒ nothing is
  filtered on the foreign path, `D578`; the single-source tier is unscored). 09-09 / 09-11 briefs:
  **0 rows** — the derivative never synced past 09-08. **The three sessions that moved (09-09 → 09-11)
  have zero desk-owned narrative coverage.**
- **`thread --days 7 --date 2026-09-08`**: 09-02 944 · 09-03 880 · 09-04 729 · 09-05 292 · 09-06 286 ·
  09-07 531 · 09-08 760 articles; 4,422 daily events → 3,424 threads (**239 living multi-day**, 506 new
  on 09-08). ⚠ The window ends 09-08 — the curve tags below are **four sessions stale** and say nothing
  about whether a thread survived the CPI/oil week.

### B-1 · What the 09-08 tape carried, and how each thread was moving `[news_vectors.db, titles only, asof 09-08]`
| thread (curve = outlets/day) | tag | 09-08 head | reads onto |
|---|---|---|---|
| Oil / Hormuz — *"Oil Nears $100 a Barrel as Fresh Attacks on Saudi Energy Ops"* **66 art / 20 outlets**, the day's #1 | Iran-war thread **BUILDING 9→5→10→9→7→10** (6 days) | US strikes Iranian tankers in Hormuz; Houthi attacks on southern Saudi; *"Goldman Sachs Warns Oil Could Hit $120 as Shipping Risks…"* (3→3) | §A-4; `S149`/`P122`/`P140` settled on it |
| Canada tariffs — *"Canada Imposes New Tariffs on U.S. Goods, as Trade War Intensifies"* **51 / 20** | **BUILDING 9→11→4→3→9→20** (6 days, the board's steepest last-day jump) | up to 50% on US goods; Trump threatens Bombardier | `S123` settled **C** today (EW INDU −0.96pp vs `SPY`, 09-04→09-11) — the implementation did **not** price as a sector event (`W5`: `HWM` −11.4 / `VRT` −8.4 vs `FIX` +5.0 / `PWR` +4.2) |
| Fed hike odds — *"Bitcoin Slides as Fed Hike Odds…"* 34 / 8; *"Gold: Fed inflation focus…"* 17 / 7 | crypto thread BUILDING 5→8→8→7→5→8 | hike odds already in the 09-08 tape, **before** PPI/CPI | §A-1; `P138`-B, `P148` (09-16) |
| Yen — *"Japanese Yen rises to seven-month high on BoJ rate hike…"* 26 / 5 | **BUILDING 5→2→2→5** | Japan GDP/wages support BoJ hike (6 outlets) | `P143` (09-14) live; `JPY=X` −1.35% on the week confirms direction, not magnitude |
| Copper record — *"Copper hits new peak of $14,533/t"* 7 / 5 and 6 / 5 | two BUILDING threads 2→5 | LME record on tariffs + supply | **`HG=F` fell −1.9% on the week from that print** while `[COT]` copper sits at the **100th pctile for a 6th run** (`C24`); `P102`-B settled the equity spread as a momentum artifact |
| Germany — *"Far right's rise in rapidly re-arming Germany…"* 18 / 10; *"Chancellor Merz: The sick man of Germany?"* 2→4 | BUILDING | German exports decline (first in 6 months); grid-sabotage arrest | `P146` (09-14): `EWG` **−2.32% vs `SPY` −0.77% = −1.55pp**, sitting **between A (−1.807) and C** with one session left — stated, not scored |
| AI capex — Qualcomm×Amazon custom silicon (32 / 7), *"Amazon's AI Buildout Is Starting to Show Up in Its Debt"*, Google/Blackstone data-center delays (3/3), NextEra/DOE $1.9bn nuclear loan (12 / 9) | mixed | | IT rip §C/§E; `P127` settled C (power beat compute +2.27pp, below A) |
| Intel — *"Why Intel Stock Rallied Tuesday Morning"* 22 / 9 | BUILDING 3→2→9 | | `[WebSearch]`: `INTC` −5.5% Thursday, +2.5% Friday — the thread reversed after the derivative stopped |
| Anthropic IPO / $15bn debt (30 / 7) · Mistral $24bn (11 / 8) | BUILDING 3→6→4→3→7→7 | | private-AI funding, no listed observable on this desk (`D563` class) |
| China exports accelerate, trade surplus widens (17 / 11) · *"China hits Japan with anti-dumping measures on chip chemicals"* (5 / 5) | BUILDING 3→4→11 | | Materials/IT supply chain — no row; noted for EVENT_ALPHA |

### B-2 · The sessions the desk could not see — `[WebSearch]`, three reads, causes attached with that tag only
- **09-10 (PPI + ECB + ORCL/ADBE)**: `SPY` −0.60%, WTI 102.48, `VIX` 17.84, `TIP−IEF` +0.343% (`P147`-A).
  `[WebSearch]` `ORCL` −2% "despite strong earnings"; the desk's own frame has **`ORCL` −5.4%, `ADBE` −5.4%,
  `NOW` −6.2%, `SHOP` −11.2%** on the week — **the software leg sold off into and after its prints**
  (`S148`, 09-14, is the row that owns this).
- **09-11 (CPI)**: `SPY` **+0.85%** (7,656.98), Dow +0.98%, Nasdaq +0.96%; **hike odds 69% → 87%**; 10y
  4.98% intraday; WTI −1.8% on the Oman talks headline; **`HPE` and `DELL` double-digit jumps** (frame:
  `HPE` **+19.4%** on the week, `DELL` +8.2%, `CIEN` +8.9%, `COHR` +8.3%, `AMD` +8.1%), `TMUS` +3.5%,
  `UNH` −3%. Sector leaders: Comm. Services, Cons. Discretionary, IT.
- **Health Care, the week's worst sector** (`XLV` −3.55%, EW exc5 **−3.18pp vs `SPY` = 7.5th pctile**,
  breadth **4/32 = 3.2nd pctile**): `[WebSearch]` names a **managed-care selloff on medical-cost pressure
  / Medicare Advantage margins** (STAT, ad-hoc-news) — **but the desk's own frame refutes that as the
  mechanism**: managed care and providers were the sector's *best* names (`HCA` +5.4, `ELV` +2.8,
  `HUM` +2.1) while **biotech/medtech carried the drawdown** (`AMGN` **−13.7**, `BSX` −10.1, `SYK` −9.1,
  `ALNY` −6.5, `EW` −6.2, `ABT` −5.9). The **cause of the medtech/biotech leg is UNKNOWN on this desk**
  (`C3`) — one web read attributes the *sector* to UNH, which the constituent tape contradicts.
  `AMGN` is **one of `S133`'s six names** (settle 09-14, vs `XLV`) — recorded at D−1, not argued.

### B-3 · Term sweep (7 buckets) — **UNMEASURABLE** (G1). Not run; nothing is "quiet".
### B-4 · Blind-spot pass — **UNMEASURABLE** (G1, and `D579`). Not run.
### B-5 · `[news_vectors.db]` ENDED threads under live propositions (staleness flags)
The 09-02→09-08 window shows **no ENDED thread under `P143` (yen), `P145` (LNG), `P146` (Germany),
`P148` (FOMC)** — all four are BUILDING or REIGNITED at the window's end. ⚠ **This is a 09-08 statement**;
whether any ended 09-09→09-11 is unmeasurable.

---

## §C · Positioning — `[COT report date 2026-09-08, Tue-close, released 09-11]` + `[FINRA 09-11]`

| market | net spec | WoW | 1-yr pctile | tag | read (context, not trigger — `D6`) |
|---|--:|--:|--:|---|---|
| **UST 2Y** | −929,107 | −46,589 | **80** | 🟢 crowded-long (on the short-in-contract convention the tool prints; 80th of its own history) | front-end positioning moved *with* the +19 bp — the crowd is on the hike side |
| UST 10Y | −834,783 | +74,492 | 27 | neutral | shorts covered into the selloff |
| USD Index | +17,604 | +579 | **84** | crowded-long | `DX-Y.NYB` flat on the week — a crowded long that did not pay |
| **WTI** | +35,358 | −216 | **75** | neutral | `P122`-A: positioning followed the barrel |
| **Nat gas** | −219,767 | −10,856 | **0** | crowded-short | context only (REJECTED contrarian) |
| **Copper** | +92,476 | +11,607 | **100** | crowded-long, **6th run** | `HG=F` −1.9% on the week; `P102`-B — `C24` sharpened |
| Gold | +231,960 | +3,836 | 60 | neutral | `GC=F` −1.4% |
| E-mini S&P | −76,036 | −95 | 66 | neutral | |
| Nasdaq-100 | +20,704 | −6,373 | 72 | neutral | longs trimmed into the IT rip |
| Russell 2000 | −8,865 | +5,876 | 28 | neutral | `IWM` −2.4% on the week |

**FINRA short-volume z (09-11)** on held names: `MET` **+1.95 🔴** (short ratio 67.9 vs base 48.0) ·
`ANET` **+1.50 🔴** (62.8 vs 52.1) · `RTX` +1.40 · `NDAQ` +1.21 (48.6 vs 34.1; the name fell −5.9% on
the week) · `NUE` +0.89 · `AVGO` +0.73 · `ETN` +0.59 · `HPE` +0.58 (**while +19.4%** — shorts leaning
into the rip, or hedged) · `SMH` +0.53 · `PSX` +0.21 · `MPC` +0.09 · `NVDA` −0.24 · `XLE` −0.49.
Context only; "short building = bearish" is a REJECTED read (`D6`).

---

## §D · Propositions registered this run — `P149` · `P150`

> Thresholds from **`D93` trailing-252 percentiles computed this stage** on settled closes to 09-11,
> `auto_adjust=False`, benchmark named inline (`C1`). IDs issued by `module_evidence next-id`
> (P: `P149`, `P150`). **Windows are registered as `base close → terminal close` dates, both verified
> trading days (`D588`)** — 09-11 (Fri) → 09-18 (Fri), five sessions 09-14…09-18, no US holiday.
> ⚠ **09-18 is quad witching / S&P rebalance (`P124`'s date)** — inside both windows, **named here as a
> known structural day, not a voider** (`D450`).

### `P149` — ★★★ The barrel cleared $100 and the equity leg did not follow: convergence or discount?

**Claim.** §A-4: `CL=F` +23.1% over 20 sessions vs `XLE` +6.7% (`SPY` −1.75%); the 20-session
`XLE−CL` gap is at the **9.9th pctile**, the 5-session gap at the **7.9th**. Three brackets settled today
say the escalation is priced in the barrel (`S149`-A), the positioning (`P122`-A) and the product
(`P140`-B) — **and the equity market is treating it as transient**, or is simply late. Which one is a
measurable question the board does not yet ask: `P126` (settled B) was chain-vs-barrel *inside* equities;
`P139` (09-14) is the Venezuela leg; `P145` (09-14) is gas. **None measures equity-vs-commodity.**

| field | value |
|---|---|
| **Frozen observable** | **`XLE` 5-session return minus `CL=F` 5-session return** (percentage points, benchmark = the front-month WTI future itself, named inline), settled closes, `auto_adjust=False`, **2026-09-11 close → 2026-09-18 close** |
| **A (convergence — the equity leg catches up and/or the barrel gives back)** | gap **≥ +4.69pp** (trailing-252 **p85**) |
| **B (the equity market keeps discounting $100 as transient — the gap widens from the 8th pctile)** | gap **≤ −5.17pp** (trailing-252 **p15**) |
| **C** | between — the disclosed favourite |
| **`D93` before freezing** | trailing 252 settled 5-session gaps to 2026-09-11: **p15 −5.17 · p85 +4.69**; current window **−8.78 = 7.9th pctile** ⇒ **the row enters INSIDE branch B's zone**, disclosed now. Mean reversion favours A/C mechanically (`S128`'s reversal factor held out of sample this week) — **which makes B the informative branch** (`L3`): B says a second week of divergence is not noise but a priced view that the Hormuz premium is temporary |
| **Both halves (`C2`)** | 20-session: `CL` +23.1% / `XLE` +6.7% / `SPY` −1.75%; 5-session: `CL` +9.4% / `XLE` +1.7% / `SPY` −0.77% |
| **Anti-signal (VOID)** | a **front-month roll inside the window** (October `CL` expires ~09-22 — outside; stated) · a **confirmed Hormuz reopening / ceasefire statement by ≥3 outlets** (the calendar's own undated 🔀binary — named, not improvised; ⚠ *"fully reopened Strait"* appears in one `[WebSearch]` read on 09-11 against transit counts of 7/day — **contradictory web reads are recorded, not resolved**) · an **`XLE` constituent M&A ≥ $10bn** inside the window |
| **Track KPI** | EW Energy breadth5 (12/16 today); `[COT]` WTI pctile (75 today) |
| **Implied move** | **UNCHECKED** — no straddle prices the spread (`C3`) |
| **Non-redundancy (`D343`)** | see claim; `P122` (positioning) and `S149` (barrel) are **settled** and cannot be re-armed; this is the equity-vs-commodity object neither measured |
| **Owner** | `industry_US` |

### `P150` — ★★★ Health Care's one-week, 4-of-32 drawdown: a shock that reverts, or the start of its own rotation?

**Claim.** §B-2: EW Health Care exc5 **−3.175pp vs `SPY` = 7.5th pctile**, breadth **4/32 = 3.2nd pctile
(= the p05 level)** — the sector moved as a *sector* (dispersion-to-move low, `D566` satisfied for once),
led by biotech/medtech, **with no measurable cause on this desk** (the web read that names UNH is refuted
by the constituent tape). The 09-08 matrix carried HLTH at **N+** on `eqflow` +0.190; today `eqflow` is
**−0.059** (Δ −0.250, the board's largest weekly flow drop). `S133` (09-14) measures constituents-vs-ETF,
**not** the sector-vs-market question; `S128`'s reversal factor just held (+6.76pp) and would mechanically
favour a bounce. **Which side is a fact only after next week.**

| field | value |
|---|---|
| **Frozen observable** | **equal-weight `us_top300` Health Care basket (32 names, enumerated in `SECTOR_FLOW_US.json` §names) 5-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, **2026-09-11 close → 2026-09-18 close** |
| **A (rotation — the sector keeps lagging)** | excess **≤ −2.594pp** (trailing-252 **p15**) ⇒ a two-week sector-level fact; HLTH is demoted on measurement, not on one week |
| **B (shock reverts — `S128`-class reversal)** | excess **≥ +2.422pp** (trailing-252 **p85**) ⇒ the week was a one-off and N+ was not wrong |
| **C** | between — the disclosed favourite |
| **`D93` before freezing** | trailing 252 settled 5-session windows to 2026-09-11: mean **−0.025** · sd **2.380** · p05 −3.391 · **p15 −2.594** · p50 −0.044 · **p85 +2.422** · p95 +4.067 ⇒ A ≈15% · B ≈15% · C ≈70%. Current (ending) window **−3.175 = 7.5th pctile**; the registered window starts fresh at 09-11 |
| **Information content (`B4`)** | **A is the informative branch**: it would be the first sector demotion this desk makes on a *measured two-week breadth fact* rather than on a flow score; B merely restores a verdict |
| **Anti-signal (VOID)** | **an FDA decision / trial readout with a named date at ≥3 of the 32 names**, or **a federal drug-pricing / Medicare rule with a named effective date**, inside 09-14 → 09-18. ⚠ **Both are unverifiable on this desk's feeds today (G1)** — at scoring they are checked by `[WebSearch]` and, if unavailable, recorded as **unknown (`C3`)**, not "did not fire". Earnings inside the window: `Ticker.earnings_dates` check to be run at PREMORTEM |
| **Track KPI** | HC breadth5 (4/32 today); `eqflow` HLTH (−0.059) |
| **Implied move** | `XLV` straddle not retrieved this stage — **UNCHECKED** (`C3`) |
| **Non-redundancy (`D343`)** | `S133` = six high-`rs60` names **vs `XLV`** (the split question); `S135` (settled A) was the UW trio; **no row measures Health Care vs the market** |
| **Owner** | `industry_US` |

### 🔀 Catalyst injection — `catalyst_calendar --days 10` (22:12; `CATALYST_WATCH.json` at the day-folder root)

| when | event | axis | source |
|---|---|---|---|
| **D−4 cal / 2 sessions · 2026-09-16 14:00 ET** | **FOMC decision + SEP / dot plot** | rates | `[fed✓]` — 🔀 binary |
| undated | Iran "Strait of Hormuz open" statement (TACO trigger) | oil | `[news👁]` — 🔀 binary, undated |
| D−6 · 2026-09-18 | S&P quarterly rebalance = quad witching | market | `[derived≈]` |
| — | EARNINGS block: *"none in window / yfinance unavailable"* | | `D560` reproduces |

🚨 **The FOMC is 2 trading sessions from Monday's open.** `P148` (registered 09-08, `IEF−SHY` 2-session
09-15→09-17) **spans it both ways** — PREMORTEM must confirm the bracket and the anti-signals still
stand after CPI (they do: `hy_oas` 2.70 < 3.10; no unscheduled action). **A hike is now the 87% base
case `[WebSearch]`** — PREMORTEM should consider whether `P148`'s slope observable still discriminates
when the *level* move is consensus, i.e. whether a **"hike delivered, dots hawkish vs dovish"** reading
needs a second observable (the `DGS2` level is blocked; an ETF proxy would be `SHY` 1-session).
⚠ `D507`: no US-holiday table — none inside the window this time (verified by hand: 09-14…09-18 are
all sessions). ⚠ `D562`: the calendar carries no ECB/BoJ dates; the BoJ's next decision date is
**`[blank]`** on this desk (not guessed).

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each. **This is ROTATION's input.**

> Wind direction only. `exc1/5/20` = **equal-weight `us_top300` constituent baskets, excess vs `SPY`**
> (benchmark inline, `C1`), settled to **09-11**; 5-session base **09-03** (sessions 09-04, 09-08…09-11),
> 20-session base 08-13. `breadth5` = names with positive 5-session excess. **`eqflow`/`wflow` from the
> 09-11 sweep; `Δflow` = the 09-04 → 09-11 weekly change** (G2). `SPY` itself: 1d +0.85% · 5d −1.15% ·
> 20d −1.75%. 🚫 G3: STPL and COMM on `eqflow`/breadth only.

| # | sector | wind | driving row | eqflow / wflow | Δflow (wk) | exc1 | exc5 mean / med | breadth5 | exc20 mean / med | note |
|---|---|---|---|---|--:|--:|---|--:|---|---|
| 1 | **Energy** | **OW** | ★`P149`(09-18, new) · `P145`(09-14) · `P139`(09-14) | **+0.431** / +0.470 | +0.030 | −0.59 | **+1.57 / +2.25** | **12/16** | ★ **+7.75 / +8.85** | The only bucket positive on flow and on both price windows; `exc20` median **+8.85**. **But the equity leg is at the 55th pctile while the barrel is at the 99th** (§A-4) — OW stands on *what the tape did*, and `P149` brackets *whether it continues*. Inside: barrel names led, services/midstream lagged (`W5`) |
| 2 | **Information Technology** | **N → N+ candidate, on breadth** | `S148`(09-14) · `S140` settled C at 09-08 | −0.207 / −0.102 | −0.012 | **+1.38** | ★ **+3.40 / +4.23** | ★ **40/56** | −1.05 / −1.90 | **The week's leader on price, on 40 of 56 names**, from `S140`'s 30/56 median at 09-08. Flow is still negative and flat — **the tape ran ahead of the flow axis**. Two-tier inside: hardware/optical/AI-infra (`HPE` +19.4, `CIEN` +8.9, `COHR` +8.3, `DELL` +8.2, `AMD` +8.1, `GLW` +7.8) vs software (`SHOP` −11.2, `NOW` −6.2, `ORCL`/`ADBE` −5.4). `D566`: the sector-level fact is the **breadth**, not the mean. 🚫 no news leg to say why |
| 3 | **Communication Services** | **no verdict issued** (G3) | — | **−0.054** / −0.148 🚫 | +0.241 | +0.11 | −0.24 / +0.03 | 6/12 | +1.16 / +0.92 | Alphabet 76.6% at issuer level flips the sign; `eqflow` flat; price flat vs `SPY` on every window. Unrankable, stated |
| 4 | **Utilities** | **N−** | `S146`(09-14) · `S135` settled **A** (one bet with RE/STPL) | −0.273 / −0.268 | **−0.340** | −1.19 | −0.31 / −0.48 | 5/15 | −2.61 / −2.56 | Largest weekly flow drop after HLTH; negative on every window; **`S135`-A says UTIL/RE/STPL moved as ONE duration object** in a +17 bp 10y week — the wind is the curve, not the sector |
| 5 | **Industrials** | **UW−** | `S150`(09-14) · `S123` settled **C** today | −0.470 / −0.505 | −0.125 | +0.32 | −0.38 / −0.43 | 21/50 | 🚨 **−5.88 / −6.00** | Worst 20-session basket on the board (both cuts); flow the most negative. `S123`-C: the Canada implementation was **not** a sector event (dispersion `HWM` −11.4 … `FIX` +5.0). ⚠ the two KR names' merge aside, `ANET+ETN` are one risk unit at 500/750d (G4) — the book's INDU exposure is AI-electrical, not the sector |
| 6 | **Consumer Staples** | **UW** (on `eqflow`/breadth — G3) | `S135` settled A | **−0.059** / −0.186 🚫 | −0.004 | −0.53 | −0.73 / −0.02 | 9/19 | −0.46 / +0.03 | Median ≈ 0 on both windows ⇒ the negative mean is a few names; `eqflow` flat. Held at UW **only as the third leg of the `S135` duration object**, and that is stated as the reason |
| 7 | **Real Estate** | **UW−** | 09-07 `TLT` row (09-14) · `S135` settled A | −0.351 / −0.319 | −0.203 | +0.25 | −0.82 / −1.05 | 4/12 | −2.33 / −2.46 | Negative on every cut; 10y 4.97 is the mechanism and it is a **real**-yield move (§A-1) — the worst version for duration equity |
| 8 | **Materials** | **N−** | `P102` settled **B** today | −0.200 / −0.085 | −0.060 | −0.06 | −1.48 / −1.59 | 🚨 **2/12** | −0.50 / −2.92 | `P102`-B: the FCX/NEM spread was a momentum artifact; **copper COT 100th pctile (6th run) while `HG=F` fell −1.9%** (`C24` sharpened). 2 of 12 positive; `exc20` median −2.92 ≪ mean. No promotion path on this evidence |
| 9 | **Financials** | **N → N− candidate** | `S142` settled C at 09-11 · `P124`(09-18) | −0.269 / −0.288 | −0.170 | −0.27 | **−2.18 / −1.45** | 11/47 | −0.87 / −0.81 | Second-worst 5-session basket after HLTH. **Curve bear-flattened (`P138`-B) and credit stayed shut (`P128`-C)** — the losers were exchanges/insurance brokers/alt managers (`AJG` −8.5, `HOOD` −7.8, `SPGI` −7.4, `AON` −6.3, `KKR` −6.2, **`NDAQ` −5.9 held**) while money-center banks were flat (`BAC` 0.0, `WFC` +0.4, `C` +0.8). A rates-sensitivity split inside the label, not a credit event (`hy_oas` 2.70) |
| 10 | **Consumer Discretionary** | **UW** (on `eqflow` — AMZN 40.2%) | — | **−0.338** / −0.240 | +0.015 | −0.32 | −2.49 / −1.92 | 5/28 | 🚨 **−4.60 / −5.18** | Negative on every window, breadth 5/28; `[WebSearch]` names it a Friday *leader* — one session against four. Unchanged |
| 11 | **Health Care** | **N+ → N, with ★`P150` armed** | ★`P150`(09-18, new) · `S133`(09-14) | −0.059 / −0.152 | 🚨 **−0.250** | −0.78 | 🚨 **−3.18 / −3.50** | 🚨 **4/32** | +0.10 / +1.48 | From the board's best `eqflow` (+0.190) to the week's worst basket in five sessions, on **28 of 32 names** — the one sector this week that moved *as a sector*. Cause **unknown on this desk** (§B-2). N+ is withdrawn because its evidence (flow) reversed; N (not UW) because one week at the 7.5th pctile is one draw (`S5`) — `P150` decides |

★ **What changed versus 09-08, on the instruments**: (i) the price tape is new for the first time in five
runs — **IT +3.40 / HLTH −3.18 is a 6.6pp one-week swap between the two largest buckets**, both on breadth
(40/56 vs 4/32), not on one name; (ii) the rates axis moved from "synchronized hiking repricing" (narrative)
to **a hike priced at 87% with the front end +19 bp and the curve bear-flattened past the 2nd pctile**
(measured); (iii) oil went through $100 **with the equity leg at a percentile-extreme lag**; (iv) credit
did nothing. **What did not change**: Energy OW, the duration trio UW (now one measured object, `S135`-A),
INDU UW−, MATR N−, COMM unrankable.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 · Rows settled this run (HANDOVER §3a + addendum) — 23 scored
| | count | rows |
|---|--:|---|
| **A** | 5 | `P122` · `S128` · `P147` · `S135` · `S149` |
| **B** | 4 | `P102` · `P126` · `P138` · `P140` |
| **C** | 12 | `S127` · `S140` · `P123` · `P128` · `S129` · `S137` · `S130` · `P127` · `S142` · `S145` · `P137` · `P114` · `P121` · `P125` · **`S123`** (addendum) — *15 including the three `[FRED]`-window rows and `S123`; 12 on the 09-08…09-11 price rows alone* |
| **AMBIGUOUS** | 1 | `S136` (`D588`) |
| **Blocked / unmeasurable** | 2 | `P142` (H.15 split) · `P141` (G1) |

**Base rate check**: with A ≈ B ≈ 15% by construction, 23 rows should give ~3.5 A and ~3.5 B; the week
gave **5 and 4** — **a regime-move week, not a well-calibrated-desk week** (`S5`: one week). **Where the
desk's *stated* side was right**: `P122`-A (supply bid extends), `S128`-A (its strongest measured cell,
out of sample), `S135`-A (the desk itself predicted the trio was one bet), `P126`-B (chain over barrel,
the desk's stated read). **Where it was wrong**: `P140`-B (the `L1` lens said crack *rate* would fade —
the level made a new high), `P147`-A (09-08 §A-2 called the PPI session "two-thirds real" — it priced as
inflation), `P138`-B (the yen/term-premium channel did not own the curve — the Fed path did), `P102`-B
(every Materials verdict since 08-21 rested on a two-name artifact). **Hit ledger for propositions the
desk took a side on: 4 right · 4 wrong · rest C.** Recorded, not smoothed.

### F-2 · Propositions carried, with their state at 09-11 (stated, not scored)
| row | settle | state |
|---|---|---|
| `P143` (yen) | 09-14 | `JPY=X` 155.66 → 153.55 (yen +1.35%) — direction consistent; magnitude vs its frozen line not computed here |
| `P145` (LNG chain) | 09-14 | `EW{LNG,GLNG,FLNG}` −0.10pp vs `SPY` (09-04→09-11); `LNG` −4.7% alone. Leaning C; A needs +3.4pp in one session |
| `P146` (Germany) | 09-14 | `EWG` **−1.55pp vs `SPY`**, between A (−1.807) and C; one session left |
| `S133` (HC constituents vs `XLV`) | 09-14 | ⚠ `AMGN` (a member) −13.7% on the week; `XLV` −3.55% — the six vs the ETF not computed here (D−1, `D242`) |
| `S146` · `S148` · `S150` · the `TLT` row · `P139` | 09-14 | not pre-empted; `S148`'s software leg fell 5–11% into its prints (§B-2) |
| **`P148`** (FOMC slope) | **09-17** | anti-signals intact (`hy_oas` 2.70); **the level move is now consensus (87%)** — PREMORTEM to consider a companion level row (§D) |
| `P124` (credit + dollar = policy event) | 09-18 | `hy_oas` +2 bp, `DXY` flat — tracking its own premise |
| `P142` | blocked | bound +19 bp (A side, low-information) |

### F-3 · 🚨 What this stage asserted and then refuted, inside the same stage (`D48`)
1. ⚠ **The first draft of §B-2 attributed the Health Care drawdown to managed care / Medicare Advantage**
   on the strength of the `[WebSearch]` reads (UNH −3%, "managed-care selloff"). **The constituent
   tape refuted it**: `HUM` +2.1, `ELV` +2.8, `HCA` +5.4 were the sector's *best* names; the drawdown was
   `AMGN`/`BSX`/`SYK`/`ALNY`/`EW`/`ABT`. The web read is kept in §B-2 as the refuted claim; the cause of
   the actual leg is **unknown** (`C3`). *A web headline about a sector is a claim about its ETF, not its
   constituents* — the `S133` question in miniature.
2. ⚠ **`S123` was first treated as "due today, terminal close 09-12"** — 09-12 is a Saturday, and so is
   the registered base date 09-05. Scored on the only admissible window (09-04→09-11) and logged as
   `D588`'s second instance (HANDOVER addendum).
3. ⚠ **A first pass at §A-1 read the week as "inflation-led" from `P147`-A alone.** The `[FRED]` weekly
   decomposition (real +12 / breakeven +1) says the *week* was real-led; `P147` is one session. Both kept.

### F-4 · Registered by this stage (transcribed to `handoff/` at run end — receipt = `grep 2026-09-12`)
| id | type | statement |
|---|---|---|
| **`M1475`** | measured | **A Fed hike is priced for 09-16**: `[FRED]` `DGS2` 4.37 → 4.56 (+19 bp, 09-04→09-10) over `DFF` 3.63 (**+93 bp wedge**); CBOE 10y 4.97 on 09-11; `[WebSearch]` FedWatch 87%. Week decomposition: **real +12 bp / breakeven +1 bp**; `hy_oas` 2.68 → 2.70; `VIX` 14.53 → 17.84 → 15.84 |
| **`M1476`** | measured | **Barrel/equity divergence at a percentile extreme**: `CL` +23.1% vs `XLE` +6.7% over 20 sessions (gap **9.9th pctile**); 5-session gap −8.78 (**7.9th**); EW Energy exc5 vs `SPY` +1.57 = 55th pctile |
| **`M1477`** | measured | **IT/HLTH one-week swap on breadth**: EW IT exc5 vs `SPY` **+3.40 (40/56, 79.8th pctile)** vs EW HLTH **−3.18 (4/32, 7.5th; breadth at the p05 level)**; HLTH `eqflow` +0.190 → −0.059 (Δ −0.250, largest on the board); the HLTH leg is biotech/medtech (`AMGN` −13.7, `BSX` −10.1, `SYK` −9.1), not managed care (`HCA` +5.4, `ELV` +2.8, `HUM` +2.1) |
| **`P149`** · **`P150`** | propositions | §D |

---

## ✅ EXIT CHECK — MACRO
- [x] Catalysts injected (`--days 10`; FOMC 09-16 inside 2 sessions, `P148` spans it; quad witching 09-18 inside both new windows, named). Indicators read: `[FRED]` 17 series with the publication clock stated; `[COT]`/`[FINRA]` read. Daily anchor = 09-08 MACRO_REPORT read.
- [x] Events: `brief --body 2` on the **local** derivative for 09-08 (4,811 → 760, head 91, tail 0); **09-09/-11 = 0 rows** — stated as zero coverage, not as a quiet day. Single-source tier unscored on the foreign path (`D578`), stated.
- [x] Trajectories: `thread --days 7` to 09-08; every proposition names its thread state **as of 09-08** or states `[WebSearch]`/unknown. No ENDED thread under a live row at 09-08.
- [x] **Term sweep and blind-spot: UNMEASURABLE (G1), not "quiet"** — no bucket carries a hit count and no bucket is called quiet.
- [x] Headline prints cited with both halves (CPI MoM + YoY, headline + core; real + breakeven; 5- and 20-session).
- [x] Every relative-performance number names its benchmark inline (`SPY`, `XLV`, `CL=F`); no cross-market statistical transfer (the KR IC ledger is not cited here).
- [x] Credit axis read and cited (`hy_oas`, `ig_oas`, `nfci`); no risk-off sentence without it.
- [x] `real_10y` quoted with `breakeven_10y`.
- [x] Linter run on this file — `report_lint.py` **0 findings** (C1·C2·S6·D6), 22:52 KST.
- [x] Transmission matrix produced, 11 sectors, one line each.
- [x] MACRO_REPORT written; self-backtest appended (23 rows; 4 right / 4 wrong on sided calls); no new blind-spot terms (pass unmeasurable — the term table is unchanged, stated).

> P4 — no market call, no sizing, no buy/sell language. Propositions are brackets; the matrix is wind
> direction for ROTATION.

---

# PREMORTEM ADDENDUM — appended 22:40 KST by Stage 7 (★ APPEND-ONLY — nothing above is rewritten)

- **§B-2 "cause of the medtech/biotech leg is UNKNOWN on this desk" is superseded** by the pre-mortem's
  `[WebSearch]` reads (BLINDSPOT_PREMORTEM Lens 1 / `M1478`): `AMGN` −10.1% on 09-08 = Novartis/Ionis
  pelacarsen Lp(a) Phase 3 miss (read-through to olpasiran) + Tavneos UK/EU suspension; `BSX` and `SYK` =
  two separate cyber attacks (BSX guide pulled). Three idiosyncratic breaks produced 4/32 breadth by
  sympathy. The earlier sentence is left standing (`D48`); **`P150`'s observable and thresholds are
  unchanged**, its branch-A reading is corrected in the pre-mortem §5.
- **§E IT line**: the 40/56 breadth is two headline days (`M1479`: 09-11 = 7 IT names z>2 on Oracle's
  $90–95bn capex guide); the sector-level fact is the AI-hardware/optics sub-basket — DEEP is scoped to it.
- **§F-3 gains a 4th self-refutation**: this stage wrote "cause unknown" at 22:35 and the pre-mortem read
  it 20 minutes later. The gap was the instrument, not the cause — a web read the MACRO stage chose not
  to spend was the whole answer.


---

# §5 · DRIFT ADDENDUM — appended 2026-09-12 23:10 KST by Stage 11 / L1·DRIFT (★ APPEND-ONLY — nothing above is rewritten)

## D-0 · The instrument could not run — recorded as *unable to measure*, not as "no drift"
`drift_watch.py --report MACRO_REPORT.md` → **`rc=2`, HTTPError 404 (ngrok offline)** at 23:02 and again
at 23:03 after a 15 s wait — the same total outage PREFLIGHT G1 measured at 14:52 / 15:15 / 22:10 (8+2
probes, 0 answers). **No kill-switch term burst can be counted tonight**; every regime-oscillating
variable this report leans on (Hormuz war-premium, the hike-vs-hold coin, the crack) is **unwatched by
the desk's own instrument until the server-side collector/API is restored (P5/P6 — human item).**

## D-1 · Manual substitute — one `[WebSearch]` read on the two regime variables, body-read, tagged
- **Hormuz — the undated 🔀 binary now has a date.** `[WebSearch]` (NPR 08-07 · Al Jazeera 08-05/08-08 ·
  ua.news 09-11): Iran's FM spokesman said 09-11 that **Oman hosts an eight-country ministerial on
  Monday 2026-09-14 in Muscat** to sign a **joint Iranian–Omani shipping-route agreement** for the
  Strait; Iran and Oman have "agreed the coordinates"; **Iran's version bans US and Israeli vessels
  and fines violators up to 20% of cargo value.** ⇒ **The signing falls INSIDE the `S156` / `P149`
  windows (09-14…18) and two sessions before the FOMC.**
- ★ **Pre-declared reading, so the anti-signal is not improvised at scoring (`D242`, `C5`)**: `P149`'s
  voider is *"a confirmed Hormuz **reopening** / ceasefire statement by ≥3 outlets"*. **A route
  agreement that excludes US/Israeli flags is NOT a reopening statement** — transit counts (7/day on
  09-10) are the observable that would show a reopening; a Muscat signing that leaves the US naval
  blockade and the US-flag ban in place is **a partial-corridor event, and `P149` stays ARMED unless ≥3
  outlets carry the words "reopened" / "open to all shipping" or transits recover past ~18/day** (the
  09-08 level). `S156` **does not void on any of this — it measures it** (registered for exactly this).
- **FOMC**: nothing new since MACRO §A/§D (87% hike odds; `P148`/`P151` armed). No unscheduled Fed
  action reported. `hy_oas` 2.70 (09-10) — voider (≥ 3.10) far.

## D-2 · What this addendum changes — and what it does not
- Changes: **the Hormuz binary is dated 09-14** for the next run's `catalyst_calendar` cross-check
  (`D562`-class gap: the calendar carries it undated); PREMORTEM §2b's "Hormuz-A" ticket has a date.
- Does not change: any verdict, any threshold, any tag. The report above stands with its G1 caveats.

## D-3 · Registered from this addendum (writeback at run end)
| id | type | statement |
|---|---|---|
| **`M1481`** | measured | **DRIFT unmeasurable 2026-09-12** — `drift_watch` rc=2 ×2 on a 404 pipe; the only drift read is one `[WebSearch]` pass. **Muscat route-agreement signing dated 2026-09-14** `[WebSearch]`; Iran's terms exclude US/Israeli vessels (fine ≤20% cargo) — pre-declared **not** a `P149` voider unless ≥3 outlets say "reopened"/"open to all" or transits recover past ~18/day |

## ✅ EXIT CHECK — DRIFT
- [x] `drift_watch` run (twice) — **failed on the instrument, logged (`_drift.log`)**; the 🚨 item that
      exists (Muscat 09-14) was body-read via `[WebSearch]` and its anti-signal reading pre-declared.
- [x] §5 ADDENDUM appended, append-only.
