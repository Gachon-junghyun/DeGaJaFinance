# MACRO_REPORT — industry_US · 2026-08-13 · Stage 3/11 (L1·MACRO)

> Wind direction only. This stage does **not** change a sector verdict — ROTATION owns that.
> Analytical only, zero buy/sell (P4). Bench named inline on every relative number (C1).
> Run clock **KST 2026-08-13 22:10–23:20 = ET 09:10–10:20, Thursday**. Cash opened 09:30 ET **during
> this stage** ⇒ **every price below is the settled 2026-08-12 close. No 08-13 bar is used anywhere (D74).**

---

## §0 · 🚨 AMENDMENT TO PREFLIGHT G1 — written first, because it changes what the rest of this stage may cite

**PREFLIGHT G1 FAILed at 22:14 KST on a 5/5 probe failure and revoked the entire news axis.**
**That revocation was correct for the sweep and is WRONG for this stage, and the difference was
measured inside this run, six minutes apart.** Left visible rather than rewritten (**D48**).

| Path | 22:10–22:14 KST | 22:17–22:25 KST |
|---|---|---|
| `sector_flow` velocity column | **17.0% coverage (51/300)** — the sweep's own 🚨 line | *(not re-run)* |
| `fts search <name> --days 7 --count --scope foreign` | **5/5 `URLError`** | ✅ **`Nvidia` → 3,830** *(via NEWS API @ ngrok)* |
| `embed sync` (server pull, `_export.pull`) | — | ✅ **5,769 new articles pulled from the server** |
| `brief --scope foreign --body 2` | — | ✅ **2,435 foreign articles → 350 events** |
| `thread --days 7 --scope foreign` | — | ✅ **3,971 daily events → 3,098 threads, 124 live multi-day** |

⇒ **The news axis is not dead. The tunnel flaps on a minutes timescale**, and PREFLIGHT caught a
trough. Combined with the KR desk's 5/5 success at 08:40 KST and RUN-2's restoration at 22:45 KST on
08-12, this is now **three transitions in 26 hours on one tunnel** — registered as **`D245`** in
HANDOVER §7.

**What this amendment does and does not license:**
- ✅ **This stage MAY cite** the event pass, the 7-day trajectories, and **term counts it ran itself
  at 22:20–22:30 KST**, each with its own output quoted.
- ⛔ **It may NOT rehabilitate `SECTOR_FLOW_US.json`'s `velocity` column.** Those 51 names are a
  **survivor sample of a failing tunnel** — a different object from a clean query. **G1's revocation
  of the sweep's velocity axis STANDS**, and every flow number below is **3-axis**.
- ⛔ It does not restore `coverage` (**argv parse failure**, `--scope` unsupported on that subcommand)
  and it does not test `drift_watch` (**`D17`, 8th run**).

---

## §A · The rate/credit axis — `[FRED]`, this run's own pull

**Daily block publishes through 2026-08-11** (`T10YIE` through **08-12**). **1 session behind** — a
material improvement on the 3–4 sessions that blocked four consecutive runs, but **still enough to
leave `S73` Leg 1 unsettleable** (HANDOVER §2b).

| Series | Last | 30d ago | 120d ago | Read |
|---|---|---|---|---|
| `DFF` fed funds | **3.63%** (08-11) | 3.63 | 3.64 | Policy rate has not moved in four months |
| `DGS2` | **4.22%** (08-11) | 4.18 | 3.56 | **+66bp over 120d** |
| `DGS10` | **4.70%** (08-11) | 4.58 | 4.22 | **+48bp over 120d**; 365d high 4.75 |
| **derived 2s10s** | **+0.48** | +0.40 | +0.66 | **★ steepened 3 consecutive prints: +0.46 (08-07) → +0.47 (08-10) → +0.48 (08-11)** |
| `DFII10` real 10y | **2.43%** (08-11) | 2.33 | 1.90 | **365d high 2.47 — sitting 4bp off it** |
| `T10YIE` breakeven | **2.26%** (08-12) | 2.25 | 2.32 | **365d range 2.18–2.50 — in the bottom quartile** |
| `BAMLH0A0HYM2` HY OAS | **2.72%** (08-11) | 2.72 | 2.69 | **9bp off the 365d low (2.63)** |
| `BAMLC0A0CM` IG OAS | **0.79%** (08-11) | +0.02 30d | +0.03 90d | 365d low 0.73 |
| `NFCI` | **−0.549** (08-07) | −0.531 | −0.567 | **Loose. 365d range −0.46 / −0.57** |
| `VIXCLS` | **15.28** (08-11) | 16.5 | 16.15 | 365d low 14.90 |
| `DTWEXBGS` | **119.06** (08-07) | 120.47 | 118.05 | **−1.41 over 30d** |
| `UNRATE` | **4.1%** (July) | 4.1 | 4.3 | monthly, lags |

### A-1 · ★★★ The 10-year's move is almost entirely REAL, and that is the run's load-bearing decomposition

**Both halves quoted, on like-for-like windows (C2):**

| Window | `DGS10` | of which `DFII10` (real) | of which `T10YIE` (inflation) | real share |
|---|---|---|---|---|
| **30 days** | **+12bp** | **+10bp** | **+1bp** | **≈91%** |
| **120 days** | **+48bp** | **+53bp** | **−6bp** | **>100% — breakevens FELL** |

⇒ **The bond market has repriced growth and term premium, not inflation.** Over four months the 10y
rose 48bp **while inflation expectations declined 6bp.** ★★ **This is the single strongest reason to
distrust the "stagflation" framing that surfaced in today's tape** (§D-3): the market that prices
inflation directly has been moving the other way for four months, and it did not blink at a **+4.7%
12-month core PPI** (§A-3). **Quoting `real_10y` without `breakeven_10y` would have hidden this
entirely** — the rule that requires the pair is the reason this section exists.

### A-2 · Credit is not confirming anything, in either direction — and that is a citable fact, not an absence

**HY OAS 2.72%, 9bp off its 365-day low, flat over 30 days. IG OAS 0.79%, 6bp off its low.
`NFCI` −0.549, within 2bp of its loosest reading of the year.** ⇒ **any "credit stress" or "risk-off"
claim in this run is `narrative-only` and must be labelled so.** Through a negative payroll (08-07),
an in-line CPI (08-12) and a split PPI (08-13), **the credit channel has not moved.**

### A-3 · ★★★ The two prints, both halves each — and they disagree about which one matters

| | Headline | Core | Grade |
|---|---|---|---|
| **July CPI** (08-12 08:30 ET) | **+0.1% MoM · 3.4% YoY** (−0.1pp from June) | **+0.2% MoM · 2.5% YoY** (−0.1pp) | ✅ **`[FRED]`-CONFIRMED this stage.** `CPIAUCSL` 322.169 (2025-07) → **332.813** (2026-07) = **+3.30%**; `CPILFESL` 328.682 → **336.789** = **+2.47%**. SA-vs-NSA rounding explains the 0.1pp. **Upgraded from `[WebSearch]` to `[FRED]`** |
| **July PPI** (08-13 08:30 ET) | **UNCHANGED, 0.0% MoM.** Final-demand **goods −0.7%** (after −1.4% in June) · **services +0.2%** (after +0.5%) | ★ **ex food, energy, trade services: +0.4% MoM** (after **+0.1%** in June) · **+4.7% over 12 months** | ⚠ **`[WebSearch]` — the BLS primary returned HTTP 403** to a direct fetch. Two independent aggregations agreed. **Tagged `[inferred-source]`; FRED has no July PPI yet** |

★★ **The July CPI landed in P50's ~10% branch (IN-LINE), not in either 45% branch.** Recorded as a
calibration finding in §F, not softened.

★★★ **The PPI is not "hot" and it is not "cool" — it is SPLIT, and the split is directional:**
**goods deflation (energy) is holding the headline at zero while core services accelerated 4× MoM
(0.1 → 0.4).** Anyone reading only the headline sees disinflation; anyone reading only the core sees a
4.7% 12-month rate. **Both halves are quoted here precisely because the two halves support opposite
tilts** — and **`S71`, which settles on tonight's `XLU` bar, is the registered instrument for which
half the tape trades.** This stage does **not** pre-empt it.

---

## §B · Positioning — COT + FINRA. **Context, never a trigger.**

`scripts/us_flow.py --cot` (CFTC, Tuesday-close, 3–4d lag) · `scripts/us_flow.py <ETFs>` (FINRA Reg SHO daily, **2026-08-12**)

| Instrument | net-spec | wk Δ | 1yr %ile | Tag |
|---|---|---|---|---|
| **UST 10Y** | **−979,243** | **−103,124 ▼** | **3%ile** | 🔴 **crowded-SHORT — the most extreme reading on the board** |
| **Nasdaq-100** | −35,006 | −25,091 ▼ | **0%ile** | 🔴 **crowded-SHORT, at the floor of its own year** |
| **Nat Gas** | −197,546 | −6,747 ▼ | 1%ile | 🔴 crowded-short |
| **WTI Crude** | **+23,033** | +3,275 ▲ | **18%ile** | 🔴 crowded-short — **still, after a 5-day +10.7% rally** |
| **Copper** | +77,123 | +9,842 ▲ | **100%ile** | 🟢 **crowded-LONG, at the ceiling** |
| **USD Index** | +22,499 | +5,302 ▲ | 81%ile | 🟢 crowded-long — **added again** |
| **S&P500 E-mini** | **−27,258** | −10,062 ▼ | 80%ile | 🟢 tagged crowded-long |
| UST 2Y | −1,004,228 | +120,346 ▲ | 65%ile | 🟡 neutral |
| Russell 2000 | −8,899 | −7,520 ▼ | 26%ile | 🟡 neutral |
| Gold / Silver | +197,634 / +22,280 | ▲ / ▲ | 29% / 29% | 🟡 neutral |

⚠⚠ **D3 (signed vs unsigned) applied, because the S&P row is a trap**: the E-mini net-spec is
**NEGATIVE (−27,258)** and simultaneously at the **80th percentile**. Those are consistent — spec has
been *more* short for 80% of the past year — but **"crowded-long" is a percentile label, not a level
statement, and this report does not repeat it as one.** The correct sentence is:
***speculators are net short the S&P and less short than usual.***

★★ **The structural read**: the two most extreme percentiles on the board are **short bonds (3%ile)**
and **short Nasdaq-100 (0%ile)**, **against a long copper at the 100th percentile.** That is a
reflation-trade positioning stack. **It is squeeze fuel in both directions and it is context, not a
trigger** (Tuesday data, 3–4 days stale).

### B-1 · FINRA short pressure on the 08-12 settled session — a hedging signature

| ETF | short% | z vs own 20d | 5v5 trend | Tag |
|---|---|---|---|---|
| **SPY** | 69.6% | **+1.58** | **+12.9 ▲** | 🔴 **short pressure RISING on the index itself** |
| XLF | 41.7% | **−2.36** | −8.1 ▼ | 🟢 heaviest short covering of the 9 |
| XLRE | 50.1% | −1.94 | −9.8 ▼ | 🟢 covering |
| XLK | 37.1% | −1.91 | −1.9 ▼ | 🟢 covering |
| XLE | 44.3% | −1.72 | +1.3 ▲ | 🟢 covering |
| XLB | 67.5% | −0.46 | **+13.2 ▲** | 🟡 normal, **but the steepest rising trend of the nine** |
| XLC | 47.4% | −0.11 | +9.0 ▲ | 🟡 |
| XLI / XLU / XLV | 69.9 / 53.3 / 65.7% | +1.16 / +0.19 / +0.39 | +4.8 / +4.8 / −1.4 | 🟡 |

★ **The divergence is the finding: index-level short pressure is rising (+1.58z, +12.9 trend) while
every sector ETF except XLB is covering.** That is the shape of **macro hedges going on while
single-sector shorts come off** — consistent with an in-line print that removed a sector thesis
without removing macro risk. ⚠ **D6: this is a C-grade inference from a B-grade instrument.**

---

## §C · The tape — settled **2026-08-12**, bench **SPY** named inline (C1)

**SPY 1d +0.25% · 5d +0.35% · 20d +2.34%.**

| Sector ETF | exc1 | exc5 | exc20 | exc60 |
|---|---|---|---|---|
| **XLE** Energy | −0.09 | ★ **+6.14 (best of 11)** | ★ **+5.68 (best)** | −1.83 |
| **XLV** Health Care | +0.01 | +2.26 | +4.07 | ★ **+11.58 (best)** |
| **XLK** Info Tech | ★ **+1.24 (best on the day)** | +1.24 | +1.67 | +2.64 |
| **XLB** Materials | 🚨 **−1.49 (worst on the day)** | **−0.46** | +1.78 | +0.03 |
| XLI Industrials | −0.15 | −0.60 | +0.89 | +3.94 |
| XLF Financials | −0.04 | −0.49 | +0.06 | **+8.84** |
| XLU Utilities | +0.23 | +0.06 | **−5.39** | −4.58 |
| XLRE Real Estate | +0.68 | −1.92 | −2.50 | −1.59 |
| XLP Staples | +0.21 | −0.64 | −0.41 | −3.99 |
| XLY Discretionary | −1.38 | −0.98 | −1.58 | −3.34 |
| **XLC** Comm Svcs | −1.15 | −0.89 | **−5.09** | 🚨 **−9.51 (worst)** |

**Commodities (settled 08-12)**: `CL=F` **83.27** (1d +0.08% · **5d +10.70%** · 20d +4.61%) ·
`HO=F` **4.304** (5d **+13.38%**) · `NG=F` 2.804 (5d +4.32% · 20d −4.10%) · `HG=F` copper 6.597
(5d −1.58% · 20d +4.82%) · `GC=F` gold 4,408.9 (20d **+9.02%**) · `UUP` 28.20 (5d +0.39%).

### C-1 · ★★★ On CPI day the winner was Information Technology, which neither P50 branch predicted

**XLK +1.24 was the best sector on the 08-12 session; XLB −1.49 was the worst.** P50 mapped a HOT
branch (rips against UTIL/RE/MATR, for FIN) and a COOL branch (duration bid, metals extend). **Neither
describes a tape where tech leads, materials lose 1.5pp, and utilities/financials/energy all sit
inside ±0.25pp.** The in-line print **removed a macro constraint and the money went to duration-long
growth, not to duration-long defensives.** ⚠ **n = 1 session (S1).** It is registered as a
proposition (§E · P52), not carried as a conclusion.

### C-2 · ★★★ Materials reversed in ONE session and the sector is now a single name

| Close | `XLB` exc5 vs SPY |
|---|---|
| 08-05 | −3.789 |
| 08-06 | −2.596 |
| 08-07 | +1.307 |
| 08-10 | **+2.227** ← S57 branch A line (+1.9) crossed |
| 08-11 | **+2.484** ← crossed again |
| **08-12** | 🚨 **−0.465** |

**And the decomposition inverted with it**: on 08-10/08-11 the move was **broad** (ex-NEM cap-weighted
+1.203, equal-weighted +0.908, **8 of 12 names positive**, NEM only **11.6%** of sector cap — that is
what fired P44's anti-signal and scored **S57 FIRED-A**). **On 08-12, `NEM`'s own 5-session excess is
+12.642 while the sector's is −0.465** ⇒ **Materials is NEM and nothing else.** Corroborating and
independent: **XLB's FINRA 5v5 short trend is +13.2▲, the steepest of the nine ETFs measured.**
⚠ **Copper spec is at the 100th percentile** — the metals leg's positioning is at its ceiling while
its equity expression just gave back two sessions.

### C-3 · Energy: the price leg is intact and the *narrative* leg is decaying — they are not the same axis
`XLE` exc5 **+6.14** and exc20 **+5.68** are both the best on the board, crude ran **+10.7% in five
sessions**, distillate **+13.4%**, and WTI spec is **still at the 18th percentile.** Meanwhile the
Hormuz thread is **FADING** (§D-2) and today's largest cluster is titled *"Oil prices **cool** despite
US-Iran deadlock."* ⚠ **exc60 is −1.83** — the 60-day window has not turned. **A 5-day leader on a
negative 60-day window is a re-rating in progress, not an established trend** (M149's shape, inverted).

---

## §D · News — the axis this stage recovered (§0). **Denominators quoted; no "quiet" claim without one.**

### D-1 · Event pass — `brief --scope foreign --body 2`, run 22:22 KST
**Denominator: 2,435 foreign articles → 350 events → 350 market / 0 non-market.**
Head (≥5 outlets) **30** · body (2–4) **320** · **tail 0** · **1-outlet 15 shown of 407** ·
non-market boundary band **0 of 0** · **75 sub-events recovered** (`└`).

⚠⚠ **`tail = 0` is NOT the coverage claim, and this run states what remains withheld**: **392 of the
407 single-outlet events were not shown** (15 random samples only), and the module prints its own
warning that **those 407 carry no classifier score at all — the classifier is Korean-only**, so on a
`--scope foreign` run they are **unmeasured, not low**. **Any "nothing happened in bucket X" claim in
this report is therefore capped at 350 scored events out of 2,435 articles**, and none is made.

**The head, ranked by outlet count — the six that carry macro:**

| Cluster | Articles/outlets | Why it is here |
|---|---|---|
| ★ *"The Commodities Feed: Oil prices **cool** despite US-Iran deadlock"* | **36 / 14** | **The day's largest cluster.** Sub-events: *"OPEC cuts 2026 demand forecast; Iran wa…"* [6/3] · *"Crude oil dips below $90 despite…"* [2/2] · ★ ***"Iran war tensions over Hormuz FAIL TO LIFT oil prices"*** [2/2] |
| ★★ *"**Fed should raise rates** to restrain growth and inflation, Hammack"* | **16 / 7** | The terminal node of the week's #1 BUILDING thread (§D-2). Sub-events: *"Gold: Upside capped by **Fed hike risks**"* [2/2] · *"Dow futures rise as **cooling inflation reduces Fed rate** [hike] odds"* [2/2] |
| *"Major Russian grain export terminals hit in Ukraine Black Sea…"* | 12 / 10 | Agri/fertiliser supply |
| *"Asian stocks rise as US inflation data dents **September Fed hike** odds"* | 12 / 6 | The market's read of the CPI, stated as *hike* odds |
| *"Oil spill from tanker believed to be Russian reaches Oman's…"* | 9 / 8 | Tanker/freight — the S61/D168 object |
| *"SpaceX Is Back Above Its IPO Price"* | 10 / 7 | S56's subject, still live |

**Body tier (2–4 outlets), the five that are transmission-matrix input and would be invisible at the
default `--body`:** *"US and Iran duel over who controls Hormuz"* [4/4] · *"Strikes on Black Sea
ports threaten global grain supplies"* [4/4] · *"European stocks rise as **on-target U.S. CPI dampens
Fed hike expectations**"* [4/4] · *"**The Puzzle Pieces for Stagflation Are Beginning to Take
Shape**"* [4/4] · *"Maersk Q2 profit surges past forecasts, raises outlook"* [4/4].
Also: *"Lenovo's Revenue Beats Expectations on Robust AI Demand"* [4/4] · *"L&T secures order to build
AI factory"* [6/4] · *"Alphabet Just Revealed How Many SpaceX Shares It [owns]"* [4/4].

★ **The single most important framing fact in the whole pass**: **every rate headline in the feed is
about a HIKE, not a cut.** *"Fed should raise rates"* · *"reduces Fed rate hike odds"* · *"dents
September Fed hike odds"* · *"dampens Fed hike expectations"* · *"Gold upside capped by Fed hike
risks."* **The debate is hike-versus-hold**, and an in-line CPI is being read as *removing hike
urgency* — not as opening the door to easing.

### D-2 · Trajectories — `thread --days 7 --scope foreign`
**Daily denominators**: 08-07 **720** · 08-08 283 · 08-09 289 · 08-10 **785** · 08-11 **801** ·
08-12 **743** · 08-13 **350** (partial day). **3,971 daily events → 3,098 threads · 477 multi-day ·
124 live · 2,621 one-day (221 new today).**

| Thread | Tag | Curve (outlets) | Total |
|---|---|---|---|
| ★★★ **Fed inflation fight → rate path** | **BUILDING, 7 days** | **6 → 3 → 3 → 6 → 7 → 7 → 7** | **163 articles** |
| **Hormuz / Strait oil premium** | 🚨 **FADING** | **16 → 6 → 7 → 22 → 23 → 17 → 14** | — |
| Black Sea strikes → wheat/grain | **BUILDING** | 3 → 4 | 8 |
| SK Hynix $38B / $720B AI buildout | REIGNITED | 7 → 3 | 16 |
| NuScale / nuclear energy platform | REIGNITED | 2 → 3 → 6 | 14 |
| BOJ upside price risks / faster hikes | REIGNITED | 8 → 2 | 16 |
| SpaceX above IPO price | REIGNITED | 9 → 7 | 32 |
| *"Nvidia, Wall Street firms plan $500B AI infrastructure"* | FADING | 11 → 13 → 9 → 4 | — |
| *"Apple downgraded as **soaring memory costs** test…"* | FADING | 2→2→3→7→5→5→4 | — |
| *"US inflation falls to 3.4% in July"* | FADING | 2→9→6→11→3 | — |

★ **The week's dominant thread is not CPI and not Hormuz — it is the Fed's own hawkish argument**,
and it is the only 7-day BUILDING thread on the board, ending today at its widest outlet count.
Every proposition below that touches rates carries this curve.

⚠ **Staleness flag, as the L1 requires**: the **Hormuz** thread is **FADING from 23 outlets (08-11) to
14 (08-13)**. **`S74` is still ARMED to 08-24 on it.** An ENDED/FADING thread under an armed row is
a re-justification instruction — **and this run does NOT move S74's band** (`D239`/`D233` discipline).

### D-3 · Term sweep — **every term passed as a SINGLE argv**, never a quoted bigram

7-day vs 30-day counts, `--scope foreign`, run 22:28 KST, then **normalised by the pool** — measured
**(7d/7) ÷ (30d/30) = 1.120** on 57,469 / 219,901 articles, because the article pool itself is growing:

| Term | 7d | 30d | raw vel | **pool-normalised** |
|---|---|---|---|---|
| **refinery** | 406 | 1,060 | 1.64× | ★ **1.46× — the fastest term on the board** |
| **Hormuz** | 1,829 | 5,318 | 1.47× | **1.31×** |
| inflation | 3,369 | 10,851 | 1.33× | 1.19× |
| shortage | 858 | 2,801 | 1.31× | 1.17× |
| recession | 372 | 1,232 | 1.29× | 1.15× |
| tariff | 1,620 | 5,557 | 1.25× | 1.12× |
| hike | 1,565 | 5,447 | 1.23× | 1.10× |
| capex | 1,006 | 3,633 | 1.19× | 1.06× |
| memory | 1,574 | 5,732 | 1.18× | 1.05× |
| **stagflation** | **19** | 219 | 0.37× | 🚨 **0.33× — decelerating hard** |

★★ **Two findings the raw counts hide:**
1. **`stagflation` appeared in today's head-adjacent tier at 4 outlets and the WORD is collapsing —
   0.33× pool-normalised, 19 articles in seven days.** A single fresh article is not a theme.
   **This report does not adopt the stagflation frame**, and §A-1 gives the independent market reason.
2. **`Hormuz` term-share is RISING (1.31×) while its thread outlet-breadth is FALLING (23 → 14).**
   These are **different axes**, not a contradiction: more articles, written by fewer independent
   desks. ⚠ **A stage citing only one of them would report the opposite direction from a stage citing
   the other.** Both go on the record. **`refinery` at 1.46× is the fastest term and it is downstream
   of the same complex** — consistent with §C-3's split (price leg intact, narrative leg narrowing).

### D-4 · Blind-spot pass — run, and it returned **no macro-relevant emergent term**
`blindspot --scope foreign` sampled the un-queried pool; the returned rows are personal-finance and
single-name items (Wave Life Sciences, a Graham-value screen, two retirement-finance pieces). **No new
term is folded into the table this run.** ⚠ `coverage --scope foreign` **failed on argv parsing**
(*"인자 파싱 실패"*) — the subcommand does not accept `--scope`. **Logged, not worked around**; it
means **the coverage denominator for the fixed term set is unmeasured today** and no claim rests on it.

---

## §E · Propositions — falsifiable, both branches, mandatory anti-signal

### P51 — ★★★ The 10-year's repricing is REAL-rate, not inflation, and the PPI core did not change that

- **Claim** `[FRED]`: over 120 days `DGS10` **+48bp** decomposes into `DFII10` **+53bp** and
  `T10YIE` **−6bp**; over 30 days **+12bp = +10bp real + 1bp breakeven (91% real)**. **A +4.7%
  12-month core PPI printed on 08-13 and breakevens sat at 2.26, in the bottom quartile of a
  2.18–2.50 365-day range.**
- **Direction A (~60%)**: the real-rate regime holds ⇒ **duration-sensitive sectors (UTIL, RE) stay
  pressured on the LEVEL of real yields regardless of the CPI path**, and the "cool CPI relieves
  duration" reflex keeps failing. **Track KPI**: `DFII10` and `T10YIE` at the next three settled
  prints; `XLU`/`XLRE` exc20 vs SPY.
- **Direction B (~40%)**: the PPI core leaks into breakevens ⇒ `T10YIE` clears **2.35** within
  10 sessions and the decomposition flips to inflation-led, which would make UTIL/RE **worse**, not
  better, and would validate the stagflation frame this report declines.
- ⚠ **Mandatory anti-signal**: **if `DFII10` falls ≥15bp while `T10YIE` is flat and `XLU` does NOT
  outperform SPY over the following 5 sessions, direction A's transmission claim is wrong** — the
  real rate would have moved and the mechanism would not have paid.
- **Thread**: the Fed rate-path thread, **BUILDING 7 days, 6→3→3→6→7→7→7, 163 articles.**
- **Catalyst**: next `[FRED]` H.15 prints (daily) · **FOMC minutes** · August CPI **2026-09**.

### P52 — ★★ An in-line print sent money to GROWTH, not to defensives — and both P50 branches missed it

- **Claim** `[measured, n=1]`: on the 08-12 CPI session, **`XLK` +1.24 was the best sector excess vs
  SPY and `XLB` −1.49 the worst**, while XLU +0.23, XLF −0.04, XLE −0.09 and XLI −0.15 all sat inside
  ±0.25pp. **P50 assigned ~90% probability to two branches (HOT/COOL) that describe neither tape.**
- **Direction A (~55%)**: removing hike *urgency* is a **duration-long GROWTH** event, not a
  duration-long **defensive** event, because the constraint that was lifted was on the discount rate's
  *path*, not its level (P51). ⇒ **IT/growth absorbs relief; UTIL/RE do not.**
- **Direction B (~45%)**: the 08-12 tech bid is a one-session artifact of an expiry/flow event and
  **mean-reverts within 5 sessions**, in which case the correct reading of the print is P50's
  IN-LINE branch — *no information* — and this proposition is noise dressed as structure.
- ⚠ **Mandatory anti-signal**: **if `XLK`'s 5-session excess vs SPY is ≤ 0 at the 08-19 settle while
  `XLU`'s is > 0, direction A is refuted outright.** ⚠ **S1: this is ONE session.** It is registered
  so it can be scored, **not** carried as evidence for any tilt.
- **Thread**: *"Asian stocks rise as US inflation data dents September Fed hike odds"* [12/6],
  REIGNITED 5→6.
- **Catalyst**: the **08-19** settle.

### P53 — ★★★ Materials' broad leg lasted two sessions and the sector is now one name

- **Claim** `[measured]`: `XLB` exc5 vs SPY ran **+2.227 (08-10) → +2.484 (08-11) → −0.465 (08-12)**,
  while **`NEM`'s own exc5 is +12.642.** On 08-10/08-11 the move was broad (ex-NEM +1.203 cap-wtd,
  **8 of 12 positive**, NEM 11.6% of sector cap — the measurement that fired P44's anti-signal and
  scored **S57 FIRED-A**). **On 08-12 that breadth is gone.** Corroborating, independent: **XLB FINRA
  5v5 short trend +13.2▲, steepest of nine ETFs**; **copper spec at the 100th percentile.**
- **Direction A (~55%)**: the 08-10/11 broadening was a **dollar-driven two-session repricing**
  (`DTWEXBGS` 119.60 → 119.06) that has exhausted; Materials reverts to a **single-name gold story**
  and the sector aggregate carries no information. ⇒ **`S77`'s ex-NEM basket is the only admissible
  Materials instrument**, which is exactly why it was registered.
- **Direction B (~45%)**: the 08-12 reversal is the one-session artifact and the broad leg resumes ⇒
  **`S77` branch A (EW ex-NEM ≥ +2.03 by 08-19) fires** and the N− tilt must change.
- ⚠ **Mandatory anti-signal**: **if `S77`'s ex-NEM equal-weight 5-session excess is positive on ANY
  settled close through 08-19, direction A is wrong** — a genuinely broad sector cannot be described
  as one name. ⚠ **G3 binds**: `wflow` is inadmissible for Materials (flipper `LIN`, 24.7%).
- **Catalyst**: **S77 settles 2026-08-19.**

### P54 — ★★ Energy's price leg and its narrative leg have separated, and only one of them is decaying

- **Claim** `[measured + news]`: **price** — `XLE` exc5 **+6.14** and exc20 **+5.68**, both best of 11;
  crude 5d **+10.70%**, distillate 5d **+13.38%**; WTI spec **still 18th percentile**; XLE FINRA
  **z −1.72 🟢 covering**. **Narrative** — the Hormuz thread is **FADING 23 → 14 outlets**, today's
  largest cluster is *"Oil prices **cool** despite US-Iran deadlock"* [36/14] with the sub-event
  *"Iran war tensions over Hormuz **fail to lift** oil prices"* [2/2], and **OPEC cut its 2026 demand
  forecast.** ⚠ **`XLE` exc60 is −1.83 — the long window has not turned.**
- **Direction A (~55%)**: the move is **physical/refining-margin**, not war-premium — which is why it
  survives a fading Hormuz thread and why **`refinery` is the fastest term on the board (1.46×)**.
  ⇒ the ENRG strength should keep concentrating in **refiners** rather than integrateds.
- **Direction B (~45%)**: crude's +10.7% *was* the premium and its decay is now the dominant term ⇒
  **XLE gives back the 5-day lead within 10 sessions** and the exc60 −1.83 is the honest window.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if crude falls ≥5% while `XLE` exc5 stays positive,
  direction B is refuted; **(b)** if crude holds and `XLE` exc5 turns negative, direction A is refuted.
  ⚠⚠ **R47 binds: no stage may state "the distillate bottleneck released" as fact** — **S55 scored C**
  and the physical-vs-premium split is **still unseparated.** This proposition does **not** resolve it;
  it registers the separation as an observable.
- **Catalyst**: **S67 settles tonight (08-13)**; **S75 settles 08-19**.

### P55 — ★★ The desk's news instrument is intermittent, and "quiet" has been mis-measured at least three times this week

- **Claim** `[measured]`: the same tunnel returned **5/5 failures at 22:14 KST** and **3,830 hits for
  `Nvidia` at 22:20 KST**, six minutes apart; **`embed sync` pulled 5,769 articles from the same
  server** in between; the client store holds **51,718 articles for 08-06→08-13 including 476 `Nvidia`
  title hits.** **PREFLIGHT G1 recorded this as a dead axis and the sweep scored 300 names 3-axis on
  a 17.0% coverage reading.**
- **Direction A (~70%)**: the failures are a **transient availability window**, not an outage ⇒
  **any run that probes once and revokes is over-revoking**, and at least three recent "the news axis
  is dead / the theme went quiet" statements are **measurement artifacts, not observations.**
- **Direction B (~30%)**: the flap correlates with load or time-of-day in a way that makes the axis
  **unreliable at the exact hour this desk runs** ⇒ the revocation is right even if the diagnosis is
  wrong, and the fix is scheduling, not code.
- ⚠ **Mandatory anti-signal**: **if three timestamped probes spaced 10 minutes apart all fail on the
  next run, direction A is wrong** and the outage is real at this hour.
- **Registered as `D245`.** ⚠ **This proposition changes no tilt.** It is here because
  **`P49` (08-12) asserted the blindness and this run measured its cause** — the honest place for that
  is a scored proposition, not a footnote.

---

## §F · Self-backtest — **1 HIT-on-branch/MISS-on-calibration · 1 HALF · 1 MISS · 2 carried**

| Proposition | Registered condition | Settled outcome | Score |
|---|---|---|---|
| **P50** (08-12) — July CPI branch map: HOT ~45% · COOL ~45% · **IN-LINE ~10%** | Named `S73` (both legs) · `S71` · `S72` as the instruments | **The print was IN-LINE on every reading** (headline +0.1/3.4, core +0.2/2.5, all in line with consensus), **`[FRED]`-confirmed this stage.** ⇒ **the ~10% branch fired and the desk had 90% of its probability mass on the two branches that did not.** ★ Its stated consequence — *"S72's sign-pattern test becomes the informative object"* — **did NOT deliver: S72 scored AMBIGUOUS** with 3 of 5 legs flat | ★ **HIT on branch identification · MISS on calibration.** Recorded as a **calibration failure**, not rounded up to a hit. **A branch map whose modal 90% does not fire is a map that was not measuring the distribution** |
| **P48** (08-12) — Materials has a real sector leg and this desk's own anti-signal proved it | Track KPI = XLB's ex-NEM excess breadth | **The breadth survived exactly two sessions.** exc5 **+2.484 (08-11) → −0.465 (08-12)** with **NEM's own exc5 +12.642** (§C-2) | **HALF** — the 08-10/11 measurement was correct and is not withdrawn; **the inference that it was a durable "sector leg" is** |
| **P47** (08-12) — Energy's inversion is a whole-barrel move into a crowded short | Track KPI = crude/XLE vs the Hormuz narrative | **Price leg CONFIRMED** (XLE exc5 +6.14 best of 11, crude 5d +10.7%, WTI spec still 18th %ile, XLE FINRA covering). **Narrative leg REFUTED** — Hormuz thread FADING 23→14 and the day's biggest cluster says oil *cooled* despite the deadlock | **HALF** — one named leg confirmed, one refuted. Re-registered as **P54** with the separation as the observable |
| **P49** (08-12) — the desk is blind on the news axis and the correct output is to say so | — | ★ **The output was right and the diagnosis was wrong.** The axis was not blind; the tunnel was flapping (§0, §E·P55) | **HALF → the honest half is the process, not the fact.** Re-registered as **P55** |
| **P43** (08-10) — CXMT is an uncovered supply-side axis | Track KPI = an Apple/CXMT **filing**, MU revision breadth, whether it reaches HBM | ⚠ **Carried UNREFRESHED for a FOURTH run.** The news axis was available this run and **this stage did not check the filing** — that is a stage failure, not a data failure. Adjacent evidence exists and is **not** a substitute: *"Apple downgraded as **soaring memory costs** test…"* FADING 2→2→3→7→5→5→4; `memory` term **1.05×** pool-normalised = **flat** | **UNSCOREABLE — and named as this stage's own omission** |
| **P-R2-1** (08-12 RUN-2) — July's benign headline is a July-window artifact; **August** headline y/y stops falling | Falsifier: August headline ≤3.3% **with** non-positive energy contribution | Settles **2026-09**. ⚠ Partial counter-evidence today: **PPI final-demand goods −0.7%**, i.e. the goods/energy channel deflated *again* in July's producer data | **CARRIED — not yet scoreable** |

**Running line for this run: 1 HIT-on-branch/MISS-on-calibration · 3 HALF · 2 carried, one of them a
named stage omission.**

★★★ **The most valuable row is P50, and it is the calibration one.** The desk wrote a three-branch map,
put **90%** on two branches, and **the 10% branch fired.** This is the second consecutive run in which
a registered anti-signal or tail branch beat the desk's modal call (08-12: P44's anti-signal fired and
scored MISS). **Two data points is not a calibration study** (C4) — but it is enough to say that the
probabilities on these branch maps are **not** being generated by a measured distribution, and this
desk should stop writing them as though they were. Registered as dig **`D246`**.

---

## §G · ★ Sector transmission matrix — all 11 GICS. **This is ROTATION's input.**

**Inherited verdicts** (`2026-08-12/SECTOR_ROTATION.md §1` + its three deltas, verified on disk):
`INDU OW− · ENRG OW− · FIN N · IT N · HLTH N+ · DISC N · MATR N− · COMM UW · UTIL UW · STPL UW− · RE UW`

⚠ **Flow numbers are 3-axis** (`vel_coverage` 17.0% ⇒ velocity excluded, all 300 names scored alike) —
**stated on the same line as every conclusion, as G1 requires.**
✅ **Δ is a ONE-session change (08-11 → 08-12)** — PREFLIGHT G2 PASS, 300/300 names, the cleanest Δ in a week.
🚨 **G3 flippers — Industrials (`CAT` 8.7%) · Materials (`LIN` 24.7%) — may NOT be promoted or demoted
on `wflow`.** ✅ **Financials is OFF the flip list this run** (it was on it 08-12).

| # | Sector | Wind (this stage) | Driving prop | Numbers (settled 08-12 · bench SPY · flow 3-axis · Δ = 1 session) |
|---|---|---|---|---|
| 1 | **Energy** | **OW− held — price leg intact, narrative leg decaying; the two are now separate observables** | **P54** | exc5 **+6.14 (best of 11)** · exc20 **+5.68 (best)** · exc1 −0.09 · **exc60 −1.83 (not turned)**. Sweep **wflow +0.416 · eqflow +0.242 — rank 1 on both axes**, Δ **+0.056**, 2🟢/1🔴 of 16, **no flipper** (XOM 30.5%, ex-top1 +0.316). FINRA **z −1.72 🟢 covering**. WTI spec **18th %ile**. **S67 settles tonight** |
| 2 | **Health Care** | **N+ held — the board's best long window, and nothing this run touches it** | — | exc60 **+11.58 (best of 11)** · exc20 +4.07 · exc5 +2.26 · exc1 +0.01. FINRA z +0.39 🟡. **S76's two legs settle 08-19** |
| 3 | **Information Technology** | ★ **N → this stage hands ROTATION an argument for promotion it did not have yesterday** | **P52** | ★ **exc1 +1.24 = best sector on the CPI session** · exc5 +1.24 · exc20 +1.67 · exc60 +2.64 — **positive on all four windows, the only sector besides HLTH that is.** FINRA **z −1.91 🟢 covering**. ⚠⚠ **Counter, stated: Nasdaq-100 spec is at the 0th percentile short** — the bid may be a squeeze. ⚠ **P43's CXMT axis unrefreshed for a 4th run (§F)** |
| 4 | **Materials** | ★★ **N− → the case for holding it is STRONGER than yesterday, and for the opposite reason** | **P53** | exc1 **−1.49 (worst on the day)** · exc5 **−0.46** (from +2.484 on 08-11) · exc20 +1.78. **NEM's own exc5 +12.642 ⇒ the sector is one name.** FINRA 5v5 **+13.2▲, steepest of nine**. Copper spec **100th %ile**. 🚨 **G3 forbids a wflow call** (LIN 24.7%; wflow −0.106 vs ex-top1 **+0.115**) |
| 5 | **Financials** | **N held — mechanism intact, tape inert** | **P51** | exc60 **+8.84 (2nd best)** vs exc5 −0.49 · exc20 +0.06 · exc1 −0.04 — **M149's decaying-stock shape again**. ★ **2s10s steepened a 3rd consecutive print to +0.48** ⇒ S51's NIM mechanism is not just intact, it is extending. FINRA **z −2.36 🟢, the heaviest covering of the nine**. ✅ **No longer a G3 flipper.** **S78 settles 08-19** |
| 6 | **Industrials** | **OW− held — and it remains the weakest overweight on the board** | — | exc1 −0.15 · exc5 −0.60 · exc20 +0.89 · exc60 +3.94. FINRA z +1.16, 5v5 +4.8▲. 🚨 **G3 flipper (CAT)** ⇒ no wflow call. **Three sectors beat it on exc5 and exc20. S64 settles tonight** |
| 7 | **Utilities** | **UW held** | **P51** | exc20 **−5.39** · exc60 −4.58 vs exc1 +0.23 · exc5 +0.06. **P51 supplies the mechanism the UW previously argued from CPI**: the pressure is the LEVEL of `DFII10` (2.43, 4bp off a 365d high), not the CPI path. **S71 settles tonight on this ETF** |
| 8 | **Real Estate** | **UW held** | **P51** | exc5 **−1.92** · exc20 −2.50 · exc60 −1.59 · exc1 +0.68. FINRA **z −1.94 🟢 covering** — the one axis pointing the other way, and it is a positioning axis, not a demand axis (D6) |
| 9 | **Consumer Discretionary** | **N held** | — | exc1 **−1.38** · exc5 −0.98 · exc20 −1.58 · exc60 −3.34 — **negative on all four windows.** ⚠ Yesterday's C3 "cap and breadth disagree in sign" no longer applies to price: the price windows now agree with each other. **DISC has been uncovered for 7 runs** |
| 10 | **Consumer Staples** | **UW− held** | — | exc1 +0.21 · exc5 −0.64 · exc20 −0.41 · exc60 −3.99. The 20-day is nearly flat — **the demote has stopped deepening for a second run** |
| 11 | **Communication Services** | **UW held — the worst long windows on the board** | — | exc20 **−5.09** · exc60 **−9.51 (worst of 11)** · exc1 −1.15 · exc5 −0.89. ⚠⚠ **R56 binds: `EA` is in `us_top300.csv` on day 29 and NOW RETURNS A NULL 08-12 CLOSE** (PREFLIGHT G5) ⇒ **the aggregate breadth number is not merely stale, it is missing a constituent.** FINRA 5v5 +9.0▲ |

**Universe headline** (`SECTOR_FLOW_US.json`): **n=300 · wflow −0.193 · 🟢 16 · 🔴 76.**

⚠⚠ **What this stage claims and does not claim.** The price inputs are one genuinely new settled
session and **Δ is valid and one-session-clean**, so the arguments below are legitimate — but they are
**arguments, not verdicts**, and three carry instrument caveats:
- ★ **IT (N) now has a promotion argument** it did not have yesterday — positive on all four windows,
  best sector on the print day, short covering — **with the 0th-percentile Nasdaq short stated against it.**
- ★★ **MATR (N−) has a stronger hold argument** — the refuting breadth evaporated in one session.
- **ENRG / HLTH / FIN / UTIL / RE / INDU / DISC / STPL / COMM: no change argued.**
🚨 **G3 removes `wflow` as an admissible basis for INDU and MATR.** **ROTATION owns every decision.**

---

## §H · Catalysts injected at run start

`catalyst_calendar.py --days 14` → `llm_outputs/2026-08-13/CATALYST_WATCH.json`.
**⚠ 3 BINARY catalysts in window — both-sides brackets REQUIRED for each.**

| When | Event | Axis | Status |
|---|---|---|---|
| 🚨 **D-0 · 2026-08-13 08:30 ET** | **July PPI** `[bls✓ 🔀binary]` | inflation | ★ **ALREADY PRINTED, 40 minutes before this stage opened** (§A-3). **Its market settlement is TONIGHT'S CLOSE**, which is what PREMORTEM must bracket |
| **D-13 · 2026-08-26** | **NVDA earnings** `🔀binary` | AI-compute | Owned by **`S79`**, two independent legs |
| undated | Iran *"Strait of Hormuz open"* statement | oil | Owned by **`S74`** → 08-24. ⚠ Its thread is **FADING** (§D-2) and its branch enumeration is defective (`D239`) |

⚠ **`--days 14` was used, not the `--days 5` default**, because `SCENARIOS_US.md` carries ARMED dates
at 08-19 (S75–S78) and 08-27 (S79) beyond the default window (**D26**).
⚠ **`[STRUCTURAL]` block is EMPTY** — `data/catalysts/structural_schedule.json` is human-maintained
and has no entries in the window. **That is an un-maintained file, not an absence of lockups/rebalances.**

---

## §I · New facts registered by this stage (`M613`–`M621`) and two new digs

**ID hygiene, checked at WRITE time against all nine handoff files**: highest existing **M612** /
**D241 (US, unsuffixed)** — the 08-13 KR run explicitly reserved `D242~` unsuffixed for this desk.

| # | Fact | Source |
|---|---|---|
| **M613** | `DGS10` +48bp over 120d = `DFII10` **+53bp** + `T10YIE` **−6bp**; over 30d +12bp = +10bp real + 1bp breakeven (**91% real**) | `[FRED]` 2026-08-11/12 |
| **M614** | July CPI **`[FRED]`-confirmed**: `CPIAUCSL` 322.169→**332.813 = +3.30%**; `CPILFESL` 328.682→**336.789 = +2.47%** | `[FRED]` 2026-07-01 |
| **M615** | July PPI: final demand **0.0% MoM**, goods **−0.7%**, services **+0.2%**, **core ex-FET +0.4% MoM / +4.7% 12m** | `[WebSearch]` ⚠ `[inferred-source]`, BLS primary 403 |
| **M616** | On the 08-12 CPI close, `XLK` **+1.24** was the best sector excess vs SPY and `XLB` **−1.49** the worst; UTIL/FIN/ENRG/INDU all inside ±0.25pp | yfinance, settled |
| **M617** | `XLB` exc5 vs SPY **+2.227 → +2.484 → −0.465** (08-10/11/12) while `NEM` exc5 = **+12.642** | yfinance, settled |
| **M618** | COT: UST-10Y spec **3rd %ile**, Nasdaq-100 **0th %ile**, copper **100th %ile**, WTI **18th %ile**, USD **81st %ile** | `[CFTC]` via `us_flow --cot` |
| **M619** | FINRA 08-12: **SPY z +1.58 / 5v5 +12.9▲** while XLF −2.36, XLRE −1.94, XLK −1.91, XLE −1.72 all cover; **XLB 5v5 +13.2▲** steepest | `[FINRA]` Reg SHO |
| **M620** | Pool-normalised 7d term velocity (pool ratio **1.120**, n=57,469/219,901): **refinery 1.46× · Hormuz 1.31× · inflation 1.19× · memory 1.05× · stagflation 0.33×** | `module_news_data fts`, 22:28 KST |
| **M621** | Hormuz thread **outlet breadth FADING 16→6→7→22→23→17→14** while its term-share **rises** — two axes, opposite directions | `thread --days 7 --scope foreign` |

| # | Dig | Human needed? |
|---|---|---|
| **D246** | ★★★ **The desk's branch probabilities are written, not measured, and two consecutive runs have been beaten by their own tails.** 08-12: P44 carried ~60% and its registered anti-signal fired ⇒ MISS. 08-13: **P50 put 45/45 on HOT/COOL and the ~10% IN-LINE branch fired.** ⚠ **C4 — two points is not a calibration study**, and that is the point: **there is no instrument that scores branch-probability calibration at all**, so the desk cannot tell a well-calibrated map from a decorated guess. **Positive-form remedy: log every proposition's stated branch probabilities and the branch that fired to a small ledger, the way `ic_ledger` does for axes — then a Brier score becomes computable in ~20 observations** | **human (wire a `prop_ledger`) · MACRO (state probabilities as priors, not measurements, until it exists)** |
| **D247** | ★★ **`module_news_data coverage` does not accept `--scope`, so the US desk has never been able to measure its own fixed-term coverage.** Ran this run: *"인자 파싱 실패: coverage --scope foreign"*. ⇒ **the denominator behind every "the term set covers the day" claim is unmeasured on the US side**, while the KR side (which needs no scope flag) can measure it. **Positive-form remedy: add `--scope` to the `coverage` subparser, or document that coverage is KR-only and have the US desk cite the `brief` denominator instead** | **human (code) · MACRO (cite the `brief` denominator, as this run did)** |

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** (`--days 14`, not the 5-day default — §H) · **events + trajectories +
      term sweep + blindspot read** (§D) · **indicators**: FRED primaries (§A) + COT + FINRA (§B) ·
      **daily anchor read** = `2026-08-12/industry_US/MACRO_REPORT.md` incl. its RUN-2 addendum.
- [x] **Events read via `--body 2`; tail = 0.**
- [x] **`tail = 0` is NOT quoted as the coverage claim.** §D-1 states what was withheld: **392 of 407
      single-outlet events unshown**, and that all 407 are **unscored because the classifier is
      Korean-only** on a `--scope foreign` run. Non-market band **0 of 0**. **75 sub-events recovered.**
- [x] **Denominator quoted**: 2,435 articles → 350 events; daily thread denominators in §D-2.
- [x] **Trajectories read**; every rate proposition carries the BUILDING 7-day curve; **the FADING
      Hormuz thread under ARMED `S74` is flagged** (§D-2) and the band was **not** moved.
- [x] **No "nothing happened" claim is made anywhere**; where an axis is unmeasured (`coverage`,
      P43's filing) it is named as unmeasured.
- [x] **Every term passed as a SINGLE argv** — no quoted bigram anywhere (§D-3), and the counts are
      **pool-normalised** with the pool ratio stated.
- [x] **Both halves of every headline print** (§A-3): CPI headline **and** core, MoM **and** YoY;
      PPI headline **and** core, goods **and** services.
- [x] **Every relative-performance number names its benchmark inline** (SPY, or XLF for S59).
      **No statistical result carried across markets** — the KR IC ledger is explicitly barred (HANDOVER §3e).
- [x] **Credit axis read and cited**: `hy_oas` 2.72 · `ig_oas` 0.79 · `nfci` −0.549 (§A-2), and the
      report states there is **no credit confirmation in either direction**.
- [x] **`real_10y` quoted WITH `breakeven_10y`** — and the decomposition is §A-1, this run's spine.
- [ ] **Linter** — run below; findings resolved in the appended §J.
- [x] **Transmission matrix produced, all 11 sectors, one line each** (§G).
- [x] **`MACRO_REPORT.md` written; self-backtest appended (§F); no new blind-spot term qualified this
      run (§D-4), stated rather than omitted.**

---

## §J · Linter run on this stage's own output

`python -X utf8 scripts/report_lint.py llm_outputs/2026-08-13/industry_US/MACRO_REPORT.md`
→ **`✅ MACRO_REPORT.md` · 총 0건** (rules C1 · C2 · S6 · D6).

⚠ **A clean run is not a correct report.** The linter checks **form only** — that a benchmark is named
near a relative number, that a headline print carries both halves, that no future label leaks, and that
OBV is not cited alone. It cannot see whether **§A-1's decomposition is the right decomposition**, whether
**P52's n=1 session deserves a proposition**, or whether **§G's IT promotion argument survives the
0th-percentile Nasdaq short stated against it.** Those are the three places this stage would break first,
and they are named here rather than left for a reader to find.

---

# ═══ §5 ADDENDUM · DRIFT — appended 2026-08-13 23:50 KST by L1·DRIFT (Stage 11/11) ═══

> **APPEND-ONLY.** Nothing above is rewritten — the original call stays visible beside its correction,
> and that asymmetry is the self-backtest's food. Analytical only (P4).
> Baseline = `MACRO_REPORT.md` mtime **2026-08-13 22:39 KST**. Elapsed at this stage: **~1h10m**, and
> critically **the US cash session opened at 09:30 ET inside that window and is now ~1h15m old.**

## §K-1 · 🚨 The tool failed again — **EIGHTH consecutive run**, and the root cause is unchanged

```
python -X utf8 scripts/drift_watch.py --report llm_outputs/2026-08-13/industry_US/MACRO_REPORT.md --scope foreign
→ drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
   허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```
**`D17`**: `drift` is absent from `module_news_data/__main__.DB_READ_CMDS`, the single source
`Server/news_api.py` imports. **Server-side fix, human-gated (P6).** ⚠ **The local fallback is also
dead** — `DEGAJA_NEWS_API= … burst` raises `sqlite3.OperationalError: unable to open database file`
(the client does not own `news_alert.db`, by design).
⚠ **And `burst`, which IS on the allow-list, timed out 2/2 remotely** (`TimeoutError: read operation
timed out`) **in the same minutes that `fts search` returned 1,199 hits.** ⇒ **the failure is
query-cost, not availability** — see §K-4.

## §K-2 · Substitute drift check, executed with allowed commands only — and **normalised**

`fts search <term> --days 1 --count --scope foreign`, run 23:44–23:48 KST, against each term's own
7-day daily average.

🚨🚨 **The pool must be normalised FIRST, and this is the finding.** Measured on the client store:
**last-1d 14,674 articles vs a 7-day daily average of 8,210 ⇒ the pool itself is running at 1.79×.**
The rolling 24h window straddles **two US sessions plus a PPI print**.

| Term | 1d | 7d avg | raw ratio | ★ **pool-normalised (÷1.79)** | Burst? (3× threshold) |
|---|---|---|---|---|---|
| `OPEC` | 87 | 26.9 | 3.24× | **1.81×** | no |
| `inflation` | 1,288 | 481.3 | 2.68× | **1.50×** | no |
| `hike` | 534 | 223.6 | 2.39× | **1.34×** | no |
| `tariff` | 515 | 231.4 | 2.23× | **1.25×** | no |
| `Iran` | 755 | 377.0 | 2.00× | **1.12×** | no |
| `Hormuz` | 514 | 261.3 | 1.97× | **1.10×** | no |
| `Ukraine` | 189 | 96.3 | 1.96× | **1.10×** | no |
| `refinery` | 110 | 58.0 | 1.90× | **1.06×** | no |
| `recession` | 78 | 53.1 | 1.47× | **0.82×** | no |

⇒ **NO KILL-SWITCH BURST. The highest pool-normalised reading is `OPEC` at 1.81×, well under the 3×
threshold.**
★★ **And the methodological point, which is the real output of this section: the RAW ratios would have
flagged FIVE terms above 1.9× and TWO above 2.2×, and every one of those is pool inflation.** Without
the denominator this substitute check produces **five false bursts**. It is the same defect class
`MACRO §D-3` corrected with a 1.120 pool ratio six hours earlier — **the same error, a different
window, inside one run.** Registered as **`D255`**.

## §K-3 · 🚨🚨 THE TAPE DRIFTED, AND IT DRIFTED AGAINST THIS RUN'S OWN CALL

**Six registered brackets settle at tonight's close.** The session is open. **Every number below is an
UNSETTLED INTRADAY READ at ~10:45 ET and is BARRED from scoring anything** (`D74`) — it is reported
because a report that says nothing while its own subject moves is the failure this stage exists for.

**🚨 UNSETTLED intraday, 2026-08-13 ~10:45 ET · SPY +0.88% · excess vs SPY in pp:**

| | intraday excess | Reads against |
|---|---|---|
| ★★★ **`HPE`** | **+4.37pp** *(+5.25% absolute — the largest move on the board)* | 🚨 **ALPHA tagged HPE 🔴RESOLVED / EXHAUSTED hours ago** |
| **`ANET`** | **−1.69pp** | 🚨 ALPHA tagged ANET the **live** end of the same pair |
| **`NEM`** | **−3.73pp** | ✅ consistent — ALPHA tagged NEM 🔴RESOLVED |
| `XLK` | +0.61 | ✅ consistent with MACRO **P52-A** (relief goes to growth) |
| `XLRE` +0.55 · `XLP` +0.21 · **`XLU` −0.20** | mixed | ⚠ **the duration complex is NOT bid** ⇒ PREMORTEM §3a's against-us trigger (`XLU` ≥ +1.80 **and** XLRE, XLP both > 0) **is not firing** |
| `XLE` −1.22 · `XLB` −1.10 · `XLI` −0.99 | all negative | cyclicals lagging |
| `MPC` −0.15 · `VLO` −0.22 · `PSX` −0.05 | ≈flat | `S67` unmoved intraday |

### ★★★ The drift that matters: `S83` is running toward the branch that says this desk was wrong

**`S83`** (registered ~6 hours ago) scores **[`ANET` 5-session excess] MINUS [`HPE` 5-session excess]**,
**A ≥ +7.16pp · B ≤ −9.68pp**, state at registration **−3.781**.
**Intraday the pair spread moved ≈ −6.06pp in ONE session** (ANET −1.69 vs HPE +4.37).

⇒ **PREMORTEM Lens 3's central adversarial call — `HPE` EXHAUSTED, `ANET` live — is being contradicted
by the tape within hours of being written**, and **`S83` branch B (*"the split is backwards; HPE is
the live end"*) is the branch moving into range.**

⚠⚠ **This changes NOTHING that is scoreable and it is not treated as evidence.** Stated precisely:
1. **No bar has settled.** The 08-13 close is ~5 hours away and intraday reversals are routine.
2. **`S83`'s own registration disclosed sd = 8.417pp — the widest estimator on this board** — so a
   6pp single-session move **is inside 0.72σ** and is exactly the noise the row warned about when it
   pre-declared that **branch C is the heavy favourite.**
3. **The estimate measurement that produced the EXHAUSTED tag is unchanged**: HPE's consensus has not
   moved in 60 days (current-Q 0.92 → 0.93; FY 3.41 → 3.42; 30-day breadth **1↑/1↓** on three buckets).
   **A price move does not revise an estimate series.** ⚠ **Score the observable, not the price
   reaction** — the rule that exists for exactly this moment.
⇒ **The tag stands, the bracket is armed, and the desk's own adversarial call is now sitting in front
of a dated test it may lose.** ★ **That is the correct state.** It is written here so that **if `S83`
settles B, the next run finds the warning already on the record rather than discovering it.**

## §K-4 · What this stage measured about its own instruments

★★★ **`D245` is REFINED and its diagnosis changes.** This run observed **four transitions** on one
tunnel — 22:14 dead → 22:20 alive → 23:07 timeout → 23:09 alive — and the earlier reading was
*"the tunnel flaps."* **The sharper measurement is: `burst` fails 2/2 with a READ TIMEOUT while
`fts search` succeeds in the same minute.** ⇒ **the failures are per-query COST, not availability.**

★ **And that reframes PREFLIGHT G1's headline number.** The sweep issues **300 sequential
`news_velocity` calls**; a client-side read timeout under server load produces **exactly** a partial
failure like **17.0% coverage** — **not an outage.** ⇒ *"the news axis died"* is very likely
**"the client gave up on 249 of 300 slow queries."**
**Positive-form remedy**: raise the client read timeout, **or** batch the velocity lookup server-side
into one request instead of 300. **Registered as `D256`.**
⚠ **This does NOT retroactively license the sweep's velocity column** — those 51 names are still a
survivor sample of a failing transport, and G1's revocation of that column stands for this run.

## §K-5 · Kill-switch coverage after this run

| Object | Covered by | State |
|---|---|---|
| PPI/CPI wedge | `S71` (tonight) · `S80` (08-19) | armed — ⚠ S71 pre-graded **no-information** (`D248`) |
| Duration complex (UTIL/RE/STPL) | **`S80`** | armed 08-19 |
| HLTH = duration leg or its own object | **`S82`** | armed 08-20 |
| The book's AI-compute concentration | **`S81`** (08-27) · **`S83`** (08-20) | armed — **`S83` is drifting toward B tonight** |
| Hormuz | `S74` (08-24) | armed · ⚠ thread FADING, physical condition TIGHTENING (EVENT_ALPHA Card 3); branch enumeration defective (`D239`) |
| Materials ex-NEM | `S77` (08-19) | armed · **0.175pp from branch B** |
| INDU | `S64` (tonight) | ⚠ **measuring the wrong object** (`D249`) |
| ENRG | `S67` (tonight) · `S75` (08-19) | ⚠ S67 **near-mechanically determined** |
| NVDA 08-26 | `S79` · `S81` | armed |

**Uncovered**: the **July retail-sales print, 2026-08-14 08:30 ET**, which PREMORTEM Lens 1 named as
the dated catalyst for the HLTH promotion **and** which lands on the consumer axis this run just
demoted (**DISC N → N−**). **No bracket owns it.** ⚠ It sits **inside** `S80`/`S82`'s windows, so a
retail-sales shock **contaminates both** — flagged here, not silently inherited.

## ✅ DRIFT EXIT CHECK
- [x] `drift_watch` run — **failed, 8th consecutive run, root cause logged, NOT worked around silently.**
- [x] **Substitute executed with allow-listed commands only**, and **pool-normalised** — the raw
      ratios would have produced five false bursts (`D255`).
- [x] **No 🚨 term burst** ⇒ no burst body-read was owed. **The drift that DID occur is in the TAPE,
      not the terms**, and §K-3 body-reads it against this run's own calls.
- [x] **§5 ADDENDUM appended, append-only.** Nothing above was rewritten.
- [x] **Every intraday number is labelled UNSETTLED and barred from scoring** (`D74`).
