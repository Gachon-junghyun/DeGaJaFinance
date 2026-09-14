# MACRO_REPORT — industry_US · 2026-09-01 (Tue) · Stage 3 / L1·MACRO

> Runtime `--market us`. All news calls `--scope foreign`. Benchmark named inline on every relative
> figure (`C1`). Run clock **KST 22:09–23:0x = ET 09:09–10:0x, PRE-OPEN** — nothing below is about the
> 09-01 US session. Last settled US session **Mon 2026-08-31**.
> IDs from `module_evidence next-id`: **M1172–M1182 · D452 · P121–P128 · S138–S145** reserved.

## 🚨 Instrument state governing every line below (inherited from PREFLIGHT · HANDOVER §0)
- ✅ **08-31 closes are official and citable plainly** (1/301 NaN in the sweep cache; the 1 is `EA`).
- 🔴 **08-28 is a fixed hole for 259 of 301 names.** ⇒ **every relative-performance figure in this
  report is computed on a 2-session (08-27 → 08-31), 5-session or 20-session window using ONLY
  official closes**, so that no number mixes a proxied bar with an official one. Where a 1-session
  08-28 → 08-31 figure appears it is labelled.
- 🔴 **OBV / flow-score from the primary `SECTOR_FLOW_US.json` may not be cited** (259 names have
  their two most recent sessions zeroed out of the OBV window; 29% label-flip rate).
  `SECTOR_FLOW_US_REPAIRED.json` is the citable flow object and SWEEP owns it — **this stage cites the
  tape and `[FRED]`, not the sweep.**
- 🔴 **News velocity from the sweep may not be cited** (16.05% coverage). Every news figure below is a
  **direct query, outside the sweep window**.
- ✅ `[FRED]` H.15 **caught up to 08-28**; `DTWEXBGS` caught up from 08-21 to 08-28.

---

## §A · FRED primaries `[FRED]` — each with its own staleness

`module_macro_us --days 30 --json`, pulled 22:4x KST. **19 series, 14 of them daily.**

| series | id | last obs | value | prior obs | Δ |
|---|---|---|---:|---|---:|
| 2y Treasury | `DGS2` | **2026-08-28** | **4.34** | 08-27 4.20 | **+14 bp** |
| 5y Treasury | `DGS5` | 2026-08-28 | 4.48 | 08-27 4.38 | **+10 bp** |
| 10y Treasury | `DGS10` | 2026-08-28 | 4.73 | 08-27 4.67 | +6 bp |
| 30y Treasury | `DGS30` | 2026-08-28 | 5.22 | 08-27 5.19 | +3 bp |
| **real 10y** | `DFII10` | 2026-08-28 | **2.42** | 08-27 2.34 | **+8 bp** |
| **10y breakeven** | `T10YIE` | **2026-08-31** | **2.31** | 08-28 2.31 · 08-27 2.33 | **−2 bp over the same window** |
| fed funds | `DFF` | 2026-08-28 | 3.63 | 08-27 3.63 | 0 |
| broad dollar | `DTWEXBGS` | 2026-08-28 | 118.7479 | 08-27 118.3583 | +0.33% |
| VIX | `VIXCLS` | 2026-08-28 | 14.43 | 08-27 14.51 | −0.08 |
| HY OAS | `BAMLH0A0HYM2` | 2026-08-28 | **2.60** | 08-27 2.63 | **−3 bp (tighter)** |
| IG OAS | `BAMLC0A0CM` | 2026-08-28 | 0.79 | 08-27 0.79 | 0 |
| SOFR | `SOFR` | 2026-08-31 | 3.68 | 08-28 3.65 | +3 bp |
| ON RRP | `RRPONTSYD` | 2026-08-31 | 6.726 | 08-28 0.175 | month-end spike |
| NFCI | `NFCI` | **2026-08-21 (11 d)** | −0.566 | 08-14 −0.561 | marginally looser |
| Fed assets | `WALCL` | 2026-08-26 | 6,730,912 | 08-19 6,745,699 | −$14.8bn |
| **monthly, ~1 month lagged — flagged, not pretended fresh** | | | | | |
| CPI · core CPI | `CPIAUCSL` · `CPILFESL` | **2026-07-01** | 332.813 · 336.789 | 06-01 | +0.07% · +0.22% MoM |
| unemployment | `UNRATE` | **2026-07-01** | **4.1** | 06-01 4.2 | −0.1pp |
| M2 | `M2SL` | 2026-07-01 | 23,218.0 | 06-01 23,115.2 | +0.44% |

### A-1 ★ The decomposition, and it is the report's spine
**`M1172` [measured] — the 08-28 rate move is ENTIRELY real yield.** `DGS10` +6 bp decomposes as
**`DFII10` +8 bp against `T10YIE` −2 bp.** The front end did far more than the long end
(`DGS2` **+14 bp** vs `DGS30` **+3 bp**) ⇒ **2s10s compressed 47 → 39 bp and 2s30s 99 → 88 bp in one
session.** Both halves cited (`C2`): the level rose **and** the curve flattened, and the flattening is
at the *front*, which is a **policy-path** shape, not a term-premium shape.
⚠ This **inverts the 08-25 run's own framing.** `P97` was registered on *"yields at a one-year high
with the dollar at a one-year low ⇒ term-premium / debasement"*. On this session the **dollar ROSE**
(118.36 → 118.75) **with** yields, and the long end barely moved. ⇒ **the debasement configuration is
not what produced this move**, and `P97` scored `C` accordingly (HANDOVER §2b) rather than A.

### A-2 Market-series cross-check (`D5`, different provider, same object)
`^TNX` **4.758** · `^FVX` **4.507** · `^TYX` **5.249** at the **08-31** close (`[yfinance]`) — i.e. the
move **continued past FRED's last observation**: 5y +11 bp and 10y +2.6 bp beyond 08-28.
★ **`M1173` [measured] — `^TNX` 4.758 exceeds the 4.75 that `P97`'s own `D93` recorded as the
365-day high.** The 10y made a new one-year high on 08-31, **after** the row settled at C on the
08-28 joint date. **Recorded forward, not used to re-score** (`D242`).
★ **`M1174` [measured] — a single-source rates claim REFUTED by the series.** The 08-31 brief's
`single_source` tier carries *"US Treasury Bond Storm: 30-year Treasury Yield Surges to 5.34%"*
[36Kr, **1 outlet**]. `^TYX` settled **5.249** on 08-31 and **5.262** on 09-01 — **the 5.34 figure is
not in the data.** ⇒ the single-source tier was read as the protocol requires **and** its most
market-moving row did not survive a check. Both facts are reported.

### A-3 Credit and financial conditions — the axis that refuses to confirm anything
`hy_oas` **2.60** and it has tightened **seven observations running** (2.73 → 2.60) ⇒ **25 bp further
from `P67`'s 2.85% trigger than at registration.** `ig_oas` **0.79**, unmoved, which is exactly why
`S111` scored `C` (HANDOVER §2b). `NFCI` **−0.566** = looser than the prior week.
⇒ **Any "credit stress / risk-off" sentence in this run is `narrative-only` by rule** — and none is
written. **`M1175` [measured]: the desk now has TWO credit instruments (`P67`'s HY, `S111`'s IG) that
have both declined to confirm the AI-capex-to-debt claim.** That is an accumulating negative, not a
neutral.

---

## §B · News — events, then trajectories, then the term sweep

### B-1 Denominator (corrected), read via `brief --date 2026-08-31 --scope foreign --body 2`
| | count |
|---|---:|
| **articles (corrected)** | **4,680** — `excluded_not_news` is **`{}` (empty)** for this date, so 4,680 is both the raw and the corrected denominator, stated rather than assumed |
| clusters | 1,335 |
| **market events (≥2 sources)** | **717** |
| non-market events | 0 |
| **head (≥5 sources)** | **95** |
| **body (2–4 sources)** | **622** |
| **tail (≤1 source)** | **0 · shown 0** |
| **`single_source`** | **count 618 · shown 15 · `min_nb` 10.0 · scored 0 · scorable 0 · unscored 618** |
| **`excluded_nonmarket`** | **count 0 · shown 0 · band −3.0** |
| **`subevents_recovered`** | **193** |

🚨 **`tail = 0` is NOT the coverage claim, and this run's withheld figure is large.**
**`single_source.count − shown = 603` clusters were counted and not shown**, and **all 618 are
`unscored`/`unscorable`** — the tier's own scorer produced nothing for this date. ⇒ **no "quiet
bucket" claim is made anywhere in this report**, and the one single-source row that did surface a
market number was **refuted** (`M1174`). `excluded_nonmarket` withheld **0**.

### B-2 The day, read event by event (head, `n_sources` desc — every line read, not the top)

★ **The 08-31 session had one dominant cause and it is a war, not a print.**

| src/art | event | what it transmits |
|---:|---|---|
| **22 / 86** | **"Energy stocks rally as fresh U.S.-Iran attacks drive oil prices higher"** └18 subevents | the day's largest cluster by both measures |
| 12 / 20 | **"Iran war live: IRGC attacks US bases in Jordan after US bombs Larak Island"** └4 | ★ **Larak is IN the Strait of Hormuz.** Subevents: *"Iran fires retaliatory strikes following US attacks on Larak island in the Strait of Hormuz"* · *"Iran attacks Jordan, UAE after US bombs Larak Island"* · *"Dow falls as US strikes Iran, **rate-hike bets jump**"* |
| 8 / 9 | "UAE intercepts Iranian drone over its waters in 'dangerous escalation'" | the escalation is multi-state |
| 5 / 7 | "Trump promises more strikes after US and Iran trade blows for first time in a month" · "Trump threatens to 'hit Iran hard'" | forward risk, undated |
| **15 / 27** | **"Trump announced a massive oil deal with Venezuela. Why it won't lower gas prices anytime soon"** └7 | ★ the **counter-supply** story, and the cluster's own framing is skeptical: *"Trump's 'Historic Deal' Isn't Fooling Oil Traders"* · *"65 Billion-Barrel Oil Deal Won't Fix Supply Anytime Soon"* |
| **10 / 27** | **"Fed Chair Warsh's Jackson Hole Debut: What He Said, and Didn't Say, About Rate Hikes"** └4 | └ *"Warsh's hawkish shift reshapes rate outlook – Rabobank"* · └ **"Barclays turns hawkish on Fed, sees TWO RATE HIKES in 2026"** |
| 14 / 52 | **"Tim Cook Ends Tenure As Apple CEO"** └6 | the week's largest single-company story |
| **13 / 44** | **"FTC sues Amazon for manipulating ad auction prices"** └3 | └ *"FTC, 22 states sue Amazon"* · └ *"Amazon's stock slips as the FTC alleges billions in hidden ad fees"* ⇒ a **named, dated cause** for Consumer Discretionary |
| 13 / 20 | **"AI Power Demand Is Exploding, But How Much Actually Gets Built"** └3 | the capex-vs-delivery gap, stated by the corpus itself |
| 11 / 34 | "Pre-Markets in Red to End a Strong August" └5 | └ *"**Energy stocks lead in subdued final trading day of August, utilities under pressure**: AlphaCheck"* — the sector shape, from the corpus, matching the tape |
| **6 / 9** | **"California Utility Stocks Plummet After Wildfire Legislation Announced"** | ★ a **named, dated, sector-specific** cause for `XLU` |
| 6 / 17 | "Nvidia and MediaTek expand partnership, Nvidia invests $3.5b" | |
| 5 / 6 | **"SLB Makes $3.4 Billion Bet on AI Data Center Boom"** | ★ **the Energy↔AI-power bridge, named** |
| 5 / 5 | **"Goldman Sachs Sees Diesel Refining Margins Soaring to $63 a Barrel"** | refiners |
| 5 / 12 | "Eli Lilly buying Merida Biosciences for up to $2.875 billion" | HLTH M&A |
| 6 / 11 | "China's Official Gauges Point to Continued Contraction" · 5/5 *"China's factory activity shrinks for second straight month, contracting less than expected"* | ⚠ **both halves cited (`C2`)**: contraction **and** a smaller-than-expected one |
| 6 / 11 | "AI could cause global economic downturn, Andrew Bailey warns G20" | |
| 6 / 31 | "Bessent expects Japan to take action to boost yen, signals BOJ rate-hike chance" | + `single_source`: *"Yen breaches 160 again"* |
| 12 / 20 | "Tariffs spat: Carney bets Canada can defy Trump" | |
| 6 / 10 | "Russian LNG gains traction in China as Arctic LNG 2 deliveries increase" | |
| 8 / 11 | "Greece signs $3.5bn air defence deal with Israel" · 5/5 "Japan Targets Record Defense Spend" | defense demand, two dated deals |
| 6 / 8 | "OpenAI's ad business hits $1 billion annualized revenue run rate" | |

### B-3 Trajectories — `thread --days 7 --scope foreign`
Window denominators first (the FADING-inflation guard): **08-26 832 · 08-27 854 · 08-28 734 ·
08-29 307 · 08-30 292 · 08-31 717 · 09-01 383** (09-01 is a **partial** day at run time).
4,119 daily events → 3,167 threads (517 multi-day, **136 alive**, 2,650 one-day of which 241 are new).

| thread | curve (outlets/day) | tag | read |
|---|---|---|---|
| **"Energy stocks rally as fresh U.S.-Iran attacks drive oil prices higher"** | **15→16→17→16→19→22→15** | `FADING` | 🚫 **the tag is an artifact.** The last point is a **partial day (383 vs 717 articles)**; on completed days the curve is **monotone up to a 7-day peak of 22**. This is the week's **largest and most stable** thread, not a fading one — the protocol's own denominator warning, applied |
| **"Iran war: US military strikes Iran's Larak Island"** | 5→5→15→6→**21**→12→5 | `FADING` | same partial-day caveat; peak 21 on 08-30 |
| **"Key Takeaways From Fed Chairman Warsh's Jackson Hole S…"** | 7→13→**21**→5→2→10→4 | `FADING` | peak **21 on 08-28** — the same session as the +14 bp `DGS2` move |
| **"Warsh Sounds Hawkish, but Will There Be a September Rate…"** → **"The Odds of a September Rate Hike Have Nearly Doubled"** | 2→**5** | ★ `BUILDING` | the hawkish read is **still gaining outlets on a partial day** |
| **"Global bond yields soar to multi-decade highs as Middle …"** | 3→**7** | ★ `BUILDING` | ⇒ the corpus itself links **rates ↔ the Gulf**, which is the transmission this report has to price |
| **"Tim Cook Ends Tenure As Apple CEO"** → 09-01 **"Tim Cook's Last Warning as Apple CEO Was That Memory Chi[ps]…"** | 7→8→6→4→3→14→**21** | ★ `BUILDING` | ★ the 7-day-old thread's **newest leg is about memory-chip cost** — the desk's own `P111`/`R111` axis, arriving from outside the desk |
| **"Anthropic signs $35 billion cloud deal with Nvidia-backed …"** | 4→4 | `BUILDING` | AI-compute demand, dated |
| **"Russia attacks Kyiv with drones…"** | **13→15→14→11→13→14→14** | `FADING` | ★ **the flattest curve on the board across 7 days** — the Ukraine leg is *persistent*, and `S92`'s branch-C falsifier (a US-brokered halt to Ukrainian strikes on Russian energy) did **not** occur |
| "FTC sues Amazon" | 8→4→9→5→4→13→7 | `FADING` | re-peaked 08-31 |
| "Nvidia tops earnings estimates, guides to $108 billion" | 18→15→5→5→5→8→3 | `FADING` | the print is 4 sessions behind and its attention has decayed |
| "Canada announces retaliatory tariffs on U.S. products" | 15→9→5→4→7→12→4 | `FADING` | re-peaked 08-31 |
| **ENDED · "Iran, Oman Agree to Temporary Strait of Hormuz D[eal]"** | 13→2, dead **08-27** | `ENDED` | ★★ **the de-escalation thread died four days before the strikes.** Registered as a staleness flag against any inherited "diplomacy is working" carry |
| **ENDED · "Nvidia agrees to acquire Hugging Face for $12.9B"** | 15→2, dead **08-28** | `ENDED` | ⚠ **`S130` (settles 09-10) is armed on this thread** — staleness flag re-raised, 2nd run. A row may still score with a dead thread; its premise no longer has an audience |
| REIGNITED · "Bill Gates has a stark warning about AI" | 13→2→4 | `REIGNITED` | AI-scepticism attention returning |

### B-4 Term sweep (7-day counts, `--scope foreign`, each term passed as its own argv — `D324`)
`inflation` **3,339** · `data center` **2,691** · `tariff` **2,025** · `Federal Reserve` **1,485** ·
`rate hike` **1,023** · `Strait of Hormuz` **1,021** · `crude oil` **955** · `Treasury yield` **613** ·
`payrolls` **280** · `refinery` **275** · `AI capex` **107** · `credit spread` **95**.

### B-5 Novelty (`theme-age`, 90d/foreign) — the ranking that matters more than the counts
| theme | verdict | age | 7d avg | **accel** | base |
|---|---|---:|---:|---:|---:|
| **`Larak`** | 🟡ACCELERATING | **36** | 23.3 | **58.21×** | 175 |
| **`Warsh`** | 🟡ACCELERATING | ≥90 | 202.4 | **3.22×** | 5,102 |
| **`Venezuela`** | 🟡ACCELERATING | ≥90 | 48.6 | **2.74×** | 1,286 |
| `rate hike` | ⚪ECHO | ≥90 | 136.7 | 1.26× | 6,890 |
| `data center` | ⚪ECHO | ≥90 | 329.1 | **1.01×** | 18,656 |
| **`refining margin`** | ⚪ECHO | 75 | 4.9 | **0.72×** | 297 |

★ **`M1176` [measured] — the escalation is genuinely new attention and the refining story is not.**
`Larak` at **58.21×** is the fastest term this desk has measured in weeks, while `refining margin`
runs **0.72× (decelerating)** on a base of 297 **on the same day Goldman published a $63/bbl diesel
call.** ⇒ the refiner leg is **not** a crowded narrative; the barrel leg is. Recorded because the desk
holds `MPC` and `PSX` and the two legs are being priced by different crowds.

### B-6 Blind-spot pass (`blindspot --scope foreign --days 3`)
Top unmatched tokens are already inside the fixed set (`China` 364 · `Nvidia` 336 · `Iran` 331 ·
`Warsh` 330 · `Fed` 325 · `Bitcoin` 292 · `Oil` 252 · `Apple` 181 · `Amazon` 153 · `Dollar` 147).
**No new macro term is folded into the table this run** — the day's mass sits on terms the sweep
already carries. The one raw sample row worth carrying is *"Longer-dated US Treasury yields climb as
Iran and US restart military attacks"* [economictimes, 08-31], which is the **B-3 rates↔Gulf link
stated in a single headline** and is the mechanism §D-1/§D-5 have to reconcile.

---

## §C · Positioning `[COT 08-25 Tue-close, 3–4 d lag]` + `[FINRA 08-31]` — context, never a trigger

| instrument | net spec | wk Δ | 1y %ile | verdict |
|---|---:|---:|---:|---|
| **Copper** | +85,266 | +5,518 | **100%** | 🟢 crowded-long |
| USD Index | +18,682 | −397 | 74% | 🟡 |
| UST 2Y | −861,296 | +66,041 | 72% | 🟡 |
| Gold | +243,334 | +21,145 | 66% | 🟡 |
| S&P500 e-mini | **−67,994** | **−57,434 ▼** | 65% | 🟡 |
| Nasdaq-100 | +11,127 | **+23,193 ▲** | 59% | 🟡 |
| **WTI Crude** | **+31,099** | +1,935 | **43%** | 🟡 — **NOT crowded** |
| Silver | +25,261 | +1,636 | 41% | 🟡 |
| UST 10Y | −838,975 | +107,986 | 22% | 🟡 |
| Russell 2000 | −16,118 | −412 | **15%** | 🔴 crowded-short |
| Nat Gas | −197,932 | +5,571 | **2%** | 🔴 crowded-short |

★ **`M1177` [measured] — the oil move is NOT a positioning chase.** WTI spec sits at the **43rd
percentile** of its year with a **+1,935** weekly change, while `CL=F` ran 83.40 → **85.76** (08-31)
→ **88.13** (09-01, unsettled) and `BZ=F` 89.31 → **90.49** → **92.62**. **Speculative length is
mid-range into a two-day, multi-state military escalation.** This is the single most actionable
asymmetry the positioning axis produced today, and it is **context, not a trigger** (`[COT]` is 3–4
days stale by construction).
★ **`M1178` [measured] — specs rotated OUT of the S&P and INTO the Nasdaq in one week**
(−57,434 vs **+23,193**) — the largest paired weekly swing on the board, and it **agrees with the
tape**: `XLK` `exc5` **+3.11pp vs `SPY`** while `RSP` − `SPY` `exc5` is **−1.61pp**.
⚠ **`C24` reproduced a third time**: **copper spec at the 100th percentile of its year** against a
Materials bucket that just fell from rank 1 to rank 2 on flow. Carried, not resolved.

**`[FINRA]` short-volume ratio, 2026-08-31, z vs own 20-day base:**
`MPC` **74.5% · z +2.90 🔴** · `PCG` 49.7% · z **+2.70 🔴** · `NEE` 54.2% · z **+1.76 🔴** ·
`SLB` 62.1% · z +1.13 (5v5 **+8.7▲**) · `AMZN` 41.2% · z +0.96 · `ANET` 53.0% · z +0.92 ·
`NVDA` 38.1% · z +0.40 · `XOM` 43.2% · z −0.26 (5v5 **−18.3▼**) · `LLY` z −0.43 · `CRM` z −0.34 ·
**`CAT` 27.8% · z −2.30 🟢 (short covering)**.

★ **`M1179` [measured] — shorts pressed INTO the refiner rally and left `XOM`.** `MPC` rose **+2.69%**
(08-27→08-31, official) with short-volume at **+2.90 z**, its most extreme of the trailing month,
while `XOM`'s short pressure fell **−18.3** on the 5-vs-5 trend. **The two Energy legs are being
positioned in opposite directions**, which is exactly the split `S136` (settles 09-09) brackets.

---

## §D · Propositions — falsifiable, both-sided, anti-signal mandatory

> ⚠ Anchors: `[FRED]` > `[yfinance]` > `[news]`. Every threshold is frozen here (`D242`).
> ⚠ `D93` executed before freezing wherever a distribution exists; where none does, that is stated
> rather than a band being invented.

### `P121` — ★★★ The repricing is the POLICY PATH, not inflation, and not term premium
- **Claim.** `[FRED]` 08-28: `DGS2` **+14 bp** · `DFII10` **+8 bp** · `T10YIE` **−2 bp** · 2s10s
  **47 → 39 bp**. `[news]` Warsh's debut read hawkish across 10 outlets; Barclays now sees **two 2026
  hikes**; the *"odds of a September rate hike have nearly doubled"* thread is **BUILDING 2→5**;
  `theme-age Warsh` **3.22× ACCELERATING** on a 5,102 base.
- **A (the path repricing extends).** `DGS2` **≥ 4.50** at the first `[FRED]` close covering
  **2026-09-04** (the August NFP session) **AND** `T10YIE` **≤ 2.36** ⇒ real/path, confirmed twice.
- **B (it was a two-session Jackson-Hole artifact).** `DGS2` **≤ 4.18** at the same close ⇒ the move
  fully retraces below its 08-27 level and the hawkish read did not survive contact with the labour print.
- **C** between — **the disclosed favourite.**
- **`D93` before freezing.** `DGS2`'s own 5-observation change, trailing 252: sd **≈6.5 bp**,
  realised 30-day range **4.17 – 4.34**. A needs **+16 bp** and B needs **−16 bp** over ~4
  observations ⇒ both are ~**±2.5σ** ⇒ **A ≈10% · B ≈10% · C ≈80%, disclosed up front.**
- **Anti-signal (VOID).** An **intermeeting Fed action**, or a **BLS delay/restatement of the August
  payroll release**. ⚠ Base rate: low — both are publication-failure clauses, not event clauses.
- **KPI.** `T10YIE` **2.31**: under A it should stay **at or below** 2.36; if branch A fires *with*
  `T10YIE` above 2.42 the claim is right about direction and **wrong about mechanism** — the same
  split that `P86` just produced (`M1166`).
- **Thread.** `BUILDING 2→5` (September-hike odds); `Warsh` 🟡3.22×.
- **Owner** `industry_US`. **Settles 2026-09-04+.**

### `P122` — ★★★ The oil bid is a supply event that positioning has not chased
- **Claim.** `CL=F` **83.40 → 85.76** (08-31 settled) with `BZ=F` **89.31 → 90.49**; `[COT 08-25]` WTI
  spec net **+31,099 = 43rd percentile of its year**, `+1,935` WoW. Cause is dated and multi-sourced:
  **US strikes on Larak Island, inside the Strait of Hormuz**, and **Iranian retaliation on US bases in
  Jordan and on the UAE** (22-outlet head cluster, 12-outlet live thread). `theme-age Larak` **58.21×**.
- **A (supply premium extends and positioning follows).** At `[COT]` for **2026-09-08**, WTI spec
  1-year percentile **≥ 65** **AND** `CL=F` settled close **≥ 88.00** on that date ⇒ the move is now
  *both* physical and crowded — which is the point at which the desk's own Energy OW stops being an
  asymmetry.
- **B (it is a headline spike into an oversupplied market).** `CL=F` settled close **≤ 80.00** on or
  before 2026-09-08 ⇒ the Venezuela supply story and OPEC spare capacity win; the escalation was a
  two-day repricing.
- **C** between — **the disclosed favourite.**
- **`D93` before freezing.** `CL=F` 30-day realised range **81.25 – 87.83**; 5-session sd ≈ **2.6**.
  A's 88.00 and B's 80.00 both sit **outside** the 30-day range ⇒ **A ≈15% · B ≈10% · C ≈75%.**
- **Anti-signal (VOID).** A **front-month contract roll inside the window** — ★ **base-rate raised, not
  decorative**: `R116` was retracted **yesterday** because a roll made `BZ=F` read −1.14% on an
  escalation day. ✅ Confirmed resolved on settled closes: **`BZ=F` 89.31 → 90.49 = +1.32%**, i.e.
  **Brent rose**, and the Brent−WTI spread **5.91 → 4.73** sits inside its 60-day 2.40–8.50 range.
  ⇒ **`M1180`**: the roll artifact was intraday only, and `R116`'s retraction is confirmed by the settle.
- **KPI.** `theme-age Larak` **58.21×** — a fall below **~5×** with `CL=F` still bid would say the
  market stopped attributing the bid to the Strait.
- **⚠ Counter-evidence stated at registration.** *"Trump's 'Historic Deal' Isn't Fooling Oil
  Traders"* and *"65 Billion-Barrel Oil Deal Won't Fix Supply Anytime Soon"* — the Venezuela cluster is
  **15 outlets and ACCELERATING 2.74×**, and it is the named bear leg.
- **Owner** `industry_US`. **Settles 2026-09-08.**

### `P123` — ★★ The AI trade's marginal dollar moved from COMPUTE to POWER, and it is now nameable
- **Claim.** Same-day, ≥5 outlets each: **"AI Power Demand Is Exploding, But How Much Actually Gets
  Built"** (13 outlets) · **"SLB Makes $3.4 Billion Bet on AI Data Center Boom"** · *"Trump:
  Communities that reject data centers will end up 'backwards and poor'"* (11) · Anthropic's **$35bn**
  cloud deal (BUILDING) — while `theme-age data center` is **⚪ECHO 1.01×** on an 18,656 base, i.e.
  **the topic is saturated and the money is moving inside it.** `SLB` is the repaired sweep's **#5**
  name (`flow +0.789`, `rs20 +20.0 vs SPY`) and sits in **Energy**, not IT.
- **A (the power leg is where the delivery is).** `EW{SLB, ETN, NEE, VRT}` **minus `SMH`**, 5-session
  sum of daily returns, first settled close after 2026-09-01 → **2026-09-08**: **≥ +5.00pp** ⇒ the
  chain's bottleneck is priced at the power layer and the desk's `IT`-centric AI exposure is
  mislabelled.
- **B (it is one week of oil beta).** **≤ −5.00pp** ⇒ the power basket is tracking its own sectors
  (energy / industrials) and there is no separate AI-power leg to own.
- **C** between — disclosed as the modal outcome.
- **Band derivation (`C5`).** Measured 5-session-sum sd of this exact spread over 60 sessions ≈
  **3.3pp**; **±5.00pp ≈ ±1.5σ**, the same construction `S136` uses, chosen for consistency rather
  than tuned.
- **Anti-signal (VOID).** `AVGO`'s **09-02/09-03** print moving `SMH` by **>±5%** in a single session
  ⇒ the benchmark leg becomes an earnings read, not a chain read. ⚠ Base rate **HIGH** —
  `AVGO`'s registered implied move is **±8.11%** (`S132`), so this clause is **likely to fire**, and
  that is disclosed now rather than discovered at settle.
- **KPI.** `NEE` `[FINRA]` short-volume **z +1.76 🔴** today — under A that pressure should ease.
- **⚠ `D416` open:** `cycle_registry.json` still has **no ranked AI-power row**, so "the book's power
  exposure is 0%" remains **unstatable**, not measured. This row measures the question the registry
  cannot.
- **Owner** `industry_US`. **Settles 2026-09-08.**

### `P124` — ★★ Credit and the dollar both say this is a policy event, not a risk event
- **Claim.** `[FRED 08-28]` `hy_oas` **2.60**, **tighter on seven consecutive observations**;
  `ig_oas` **0.79**, unmoved; `NFCI` **−0.566**, looser. `[yfinance 08-31]` `GC=F` **4,478 → 4,431**
  (and 4,388 on 09-01) **while `DTWEXBGS` rose** and `VIXCLS` sits at **14.43**. A war escalation, a
  hawkish central-bank debut and a new one-year high in the 10y produced **no credit widening, no vol
  bid and a falling gold price.**
- **A (the market is under-pricing it).** `hy_oas` **≥ 2.85** (`P67`'s standing line) at the first
  `[FRED]` close covering **2026-09-18** ⇒ the calm was complacency.
- **B (it holds — the repricing is orderly).** `hy_oas` **≤ 2.50** at the same close **AND**
  `VIXCLS` **≤ 15.5** ⇒ credit tightens *through* a Gulf escalation.
- **C** between — disclosed favourite.
- **`D93`.** `hy_oas` 252-obs: current 2.60 is near the low end of its year; 14-obs change sd ≈ 8 bp
  ⇒ A needs **+25 bp** (≈3σ) and B needs **−10 bp** (≈1.2σ) ⇒ **A ≈5% · B ≈25% · C ≈70%.**
  ⚠ **The bands are deliberately asymmetric because the distribution is** — stated, not hidden.
- **Anti-signal (VOID).** A **single-issuer default or a bank resolution** inside the window ⇒ an
  idiosyncratic credit event is not the systemic reading this row tests.
- **KPI.** `GC=F` — under A, gold should stop falling; it has fallen **three sessions running**
  (4,609.7 → 4,388.2) **while the dollar rose**, which is the configuration `P97` was registered
  against and which `P97` scored `C` on.
- **Relationship to `P67`/`S111`.** ⚠ **Not redundant, and the overlap is named** (`D343`): `P67` is a
  *level* claim about AI-capex debt; this row is a *joint* claim about credit **and** vol **and** gold
  through a geopolitical event. If both fire the same way that is two observations of one regime.
- **Owner** `industry_US`. **Settles 2026-09-18.**

### ⚠ Brackets deliberately NOT registered this run, with reasons (information-content rule)
- **August NFP 09-04** — already carried both-sided by **`S126`** (`XLI` exc5 **into** the print) and
  **`P114`** (**out of** it), plus `P121` above now keys its own settle to that date. A fourth row
  double-counts one observation.
- **`AVGO` 09-02/03** — carried twice (`S132` ±9.00pp, `S127` 09-08). ⚠ `D420` unresolved (issuer
  calendar 09-03 vs `catalyst_calendar` 09-02).
- **The Hormuz/oil axis** — `P122` above **replaces the bracket `S92` consumed when it scored today**;
  PREMORTEM was told in HANDOVER §8 that this was owed, and it is discharged here rather than deferred.
- **Tim Cook / `AAPL` succession** — a 21-outlet BUILDING thread, but **no branch would change a
  sector verdict** on this board (`AAPL` is not held and IT's verdict turns on breadth, not on one
  name). **Filed as a dig, not a bracket.**
- **California wildfire legislation / `PCG`** — a named, dated, single-state regulatory event.
  It **explains** part of `XLU`'s −2.20% but the desk's `UTIL UW` does not rest on it, so a bracket
  would measure the news rather than the thesis.

---

## §E · ★ Sector transmission matrix — the deliverable ROTATION consumes

> **Wind direction only.** This is not an 11-way equal analysis (protocol rule). Tape figures are
> **official closes, 2026-08-27 → 08-31 (2 sessions) and 5/20-session, benchmark `SPY` named inline
> (`C1`)**. Flow is **not** cited here — the primary sweep's OBV axis is revoked and SWEEP owns the
> repaired file.

| # | GICS sector | wind | tape (`exc2` / `exc5` / `exc20` vs `SPY`) | driving proposition |
|---|---|---|---|---|
| 1 | **Energy** | **OW** | **+3.21 / +0.88 / +7.56** — best on all three horizons | **`P122`** (supply event, spec at 43%ile) · `P123` (SLB's $3.4bn AI-power bridge) · ⚠ `M1179`: the two legs (`MPC` short z **+2.90** vs `XOM` 5v5 **−18.3**) are positioned oppositely — `S136` settles 09-09 |
| 2 | **Information Technology** | **N → the board's open question** | −0.59 / **+3.11** / **+3.51** | ★ **`S124` FIRED-A at 41/56** from a 13/56 registration state. `P123` says the AI marginal dollar left this bucket for power. **The 2-session and 5-session tape disagree by 3.7pp** — ROTATION must resolve which window it is verdicting on |
| 3 | **Health Care** | **OW, weakening** | −0.08 / **−2.85** / **+3.88** | No new proposition. `[news]` LLY buying Merida ($2.875bn, 5 outlets). ⚠ **the 5-session tape is the 2nd-worst on the board while the 20-session is 2nd-best** — a rollover, not a level |
| 4 | **Materials** | **OW, contested** | −0.49 / −2.13 / **+2.06** | ⚠ **`C24`, 3rd reproduction**: copper spec **100th percentile** `[COT]` against a bucket that just lost rank 1. No proposition drives it — that absence is the finding |
| 5 | **Financials** | **OW−** | **+0.23** / −1.34 / −0.66 | `P121` (a front-end-led repricing is the bank-friendly shape). ⚠ **PREFLIGHT G3 bars any `wflow` claim here** — the two sweep instruments disagree on its sign |
| 6 | **Communication Services** | **OW−** | **+0.57** / −1.23 / −1.13 | No proposition. ⚠ `wflow −0.547` vs `eqflow **+0.054**` is the widest cap-vs-equal split on the board (`D297`: n=12, GOOGL 38.3% ⇒ un-measurable by rule) |
| 7 | **Consumer Staples** | **N** | **+0.41** / **−3.29** (worst on 5d) / −1.10 | `P121` (a duration-proxy bucket under a front-end repricing) |
| 8 | **Consumer Discretionary** | **UW** | **+1.14** (best ex-Energy on 2d) / −1.91 / −2.61 | ⚠ **a named, dated cause on the strong side**: the FTC/22-state suit hit `AMZN` (13 outlets) and the bucket still **outperformed** on 2 sessions. **PREFLIGHT G3 bars a `wflow` verdict change here** (`AMZN` 40.2%) |
| 9 | **Real Estate** | **UW** | −0.71 / −3.16 / −3.61 | **`P121`** — the cleanest duration-proxy short under a +14bp front end |
| 10 | **Industrials** | **UW** | −1.53 / −2.63 / **−5.62** | `P121` · ⚠ **`CAT` short-volume z −2.30 🟢 (covering) on a −2.05% session** — pressure leaving the worst bucket. `S126`/`P114` settle 09-04 |
| 11 | **Utilities** | **UW** | −1.67 / −2.76 / **−6.04 (worst on the board)** | **`P121`** + a **named, dated, sector-specific cause**: California wildfire legislation (6 outlets), `NEE` short z **+1.76 🔴**, `PCG` z **+2.70 🔴**. ⚠ **`P123` cuts the other way** — if the AI-power leg is real, this is the bucket that owns it |

★ **`M1181` [measured] — the wind has one direction and it is not equities.** On the 20-session
window only **three** of eleven sectors beat `SPY` (`XLE` +7.56 · `XLV` +3.88 · `XLK` +3.51) and
`RSP` − `SPY` is **−0.19 / −1.61 / −0.19** across 2/5/20 sessions. **Breadth is not paying**; the
index's return is concentrated, which is the mechanical reading `S131` (scored `C` today) could not
distinguish from a behavioural one.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 Rows settled this run (full detail in `HANDOVER §2`)
**11 scored · 0 `EXPIRED` · 1 unscoreable (`S8`, 34th run) · 0 silent skips.**

| verdict class | rows | what it says about the desk |
|---|---|---|
| **Vindicated a desk position** | **`S112` FIRED-B** (`EW{XLU,XLRE,XLP}` exc3 **−2.331pp** vs a −1.757 threshold) | the correlated-underweight tilt survived its own registered test, from a **49th-percentile** starting state |
| **Refuted a desk position** | **`S124` FIRED-A** (IT breadth **41/56**, threshold ≥30, registration state **13/56**) | the desk's IT call is the one a settled bracket moved against |
| **Fired with a dissenting KPI** | **`P86` FIRED-B** on `DGS2` 4.34 ≥ 4.32, while its own KPI (`T10YIE` ≥ 2.42) reads **2.31** | the level test fired; the mechanism it named did not (`M1166`) |
| **Confirm-only by its own grading** | **`S92` FIRED-A** | the row pre-graded A as confirm-only and its **falsifier branch C did not fire** ⇒ little information, as designed |
| **No information** | **7 `C`s** — `S94` · `S103` · `S104` · `S111` · `S120` · `S131` · `P97` | ⚠ **`S103`'s C is doubly uninformative** — the 08-23 run had already declared its ±5.0pp bands inside the implied move |

**Running read: 1 clean vindication, 1 clean refutation, 9 rows that changed nothing.** ⇒ the honest
summary is **not** "the desk went 1-for-2"; it is **"9 of 11 pre-registered rows produced no
information"**, and the two that did point in opposite directions.

### F-2 The pattern in the misses — carried, and re-confirmed a fourth time
The desk's recorded pattern is that **a pre-settle read has been an inverted one, three for three**
(`S101`, `P78`, `P96`). ★ **`M1182` [measured] — a fourth instance, in the milder direction.**
`S103`'s pre-settle read on 08-29 was **+1.663pp**; the settled value is **+3.479pp** — same sign,
**2.1× the magnitude**. ⇒ the rule is refined rather than repeated: *pre-settle reads on this desk have
been wrong in sign three times and wrong in magnitude a fourth; none has yet been right.*

### F-3 🚨 What this stage asserted and then refuted, in the same run (`§4c` / `D48`)
★ **`D452` — one claim was written and then killed by the next command.** The first draft of §A-2
carried the `single_source` headline *"30-year Treasury Yield Surges to 5.34%"* as corroboration that
the long end was leading. **`^TYX` settled 5.249 (08-31) and 5.262 (09-01)** — the figure is not in the
data, and the long end was in fact the *laggard* (`DGS30` +3 bp vs `DGS2` +14 bp), i.e. the retracted
sentence pointed the **opposite way** to the report's spine. ⇒ **the sentence is left recorded here
rather than deleted** (`M1174`), and the dig is: *a single-source market figure is checked against the
series before it is allowed to support a direction, not after.*
⚠ **Zero self-refutations would itself be worth a line** — this run has one, plus `R120` in HANDOVER
retracting a bound this desk published yesterday.

---

## ✅ EXIT CHECK
- [x] Catalysts injected (`catalyst_calendar --days 5`, saved to the day-folder root; **`--days 10`
      not needed — no `ARMED` row sits between 09-06 and 09-08 that the 5-day window misses; the
      furthest near-term armed dates are 09-04/09-08/09-09/09-11/09-14 and all are named in HANDOVER
      §2d**). Narrative (events + trajectories + 7-bucket + blindspot) and indicators (FRED primaries
      + COT + FINRA) read; **daily anchor read** = `llm_outputs/2026-08-31/industry_US/MACRO_REPORT.md`
      + `module_report_tags show`.
- [x] Events read via `--body 2`; **tail count = 0**.
- [x] **`tail = 0` is NOT treated as the coverage claim** (§B-1): `single_source` **618 counted / 15
      shown ⇒ 603 withheld**, all `unscored`; `excluded_nonmarket` **0 / 0**; `subevents_recovered`
      **193**. **No "quiet bucket" claim appears anywhere in this report.**
- [x] **Denominator is the corrected one** — 4,680 articles, with `excluded_not_news = {}` stated
      explicitly rather than assumed.
- [x] Trajectories read; **every proposition carries a thread tag + curve** (`P121` BUILDING 2→5;
      `P122` 15→16→17→16→19→22→15 with the partial-day caveat; `P123` BUILDING 4→4; `P124` no thread,
      **stated**). **Two ENDED threads flagged under still-open rows** (`S130`'s Hugging Face thread,
      2nd run; the Hormuz-diplomacy thread that died 08-27).
- [x] Every "nothing happened" claim carries its denominator — **none is made** (§B-1).
- [x] **No bucket's count came from a quoted multi-word boolean** — every term in §B-4 was passed as
      its own argv (`D324`).
- [x] **Both halves cited** (`C2`): China PMI (contraction **and** better-than-expected); the rate move
      (level up **and** curve flattened); `DGS10` (+6 bp = real +8 / breakeven −2); the monthly FRED
      series flagged as ~1 month lagged rather than presented as current.
- [x] **Every relative-performance number names `SPY` inline**; no statistical result carried across
      markets (the `vol_surge` IC result is `market=kr` and is **not** used here — `W1`).
- [x] **Credit axis read and cited** — `hy_oas` 2.60 · `ig_oas` 0.79 · `NFCI` −0.566. No credit-stress
      claim is made; §A-3 states the opposite and labels it.
- [x] **`real_10y` quoted with `breakeven_10y`** — §A-1 is built on exactly that pair.
- [x] **Linter run on this stage's own output** — `report_lint.py llm_outputs/2026-09-01/industry_US/MACRO_REPORT.md` ⇒ **0 findings** (rules C1·C2·S6·D6). ⚠ It checks form only; a clean run is not a correct report.
- [x] Transmission matrix produced, all 11 sectors, one line each (§E).
- [x] Self-backtest appended (§F) with the running pattern; **no new blind-spot term folded in**, and
      the reason is stated (§B-6).

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **SWEEP** (Stage 4).
> ⚠ SWEEP inherits: cite `SECTOR_FLOW_US_REPAIRED.json` only; the primary file's OBV axis is revoked;
> Δflow is a **two-session** (08-27 → 08-31) quantity; and §E's tape says **`XLK`'s 2-session and
> 5-session readings disagree by 3.7pp** — the sweep is the instrument that has to arbitrate it.


---

# §5 · DRIFT ADDENDUM — appended 2026-09-01 23:2x KST (Stage 11 / L1·DRIFT)

> **Append-only.** Nothing above this line is rewritten. The original call stays visible beside its
> challenge — that asymmetry is the self-backtest's food (`D48`).

## 5.0 · Spec compliance, stated first
`drift_watch.py --report .../MACRO_REPORT.md` ran at **+0.6h** after the report's completion stamp
(**2026-09-01T22:43**) against the stage's **3–6h** specification.
🚨 **`D282` reproduced — 6th consecutive run.** The window is short by design constraint, not by
choice, and every count below is from a 0.6h window. **Stated before the findings, not after.**

## 5.1 · 🚨 The burst that challenges this report's spine

**3 candidate bursts (≥3.0×). One of them is a direct challenge to §A-1.**

| term set | post-completion count | vs baseline |
|---|---:|---:|
| **`rate hike`** | 23 | **6.5×** |
| **`Strait of Hormuz`** | 13 | **3.9×** |
| `downgrade` | 3 | 3.2× |

### ★ The challenge, body-read (not counted)
§A-1 of this report is built on **`M1172`**: the 08-28 rate move is **entirely real yield**
(`DFII10` +8bp against `T10YIE` **−2bp**), front-end-led, therefore a **policy-path** event and
**not** an inflation event. The window's own headlines name the opposite mechanism, across
**four independent outlets**:

- *"US bonds sell off as **rising oil prices create inflation anxiety**"* [yahoo_finance, 09-01]
- *"Nasdaq crashes over 1% as bond selloff, oil rise fuel **inflation anxiety**"* [economictimes, 09-01]
- *"**How the Oil Price Is Pressuring Treasuries**"* [bloomberg, 09-01]
- *"**Global Bond Sell-Off** Puts Investors on Edge"* [nyt, 09-01]
- *"Oil up more than 2% as renewed US-Iran strikes stoke supply fears"* · *"US bonds sell off as
  rising oil prices create inflation anxiety"*

⇒ **the oil escalation and the rate repricing have been joined by the corpus into one story, and the
joint is named as INFLATION** — the leg §A-1 explicitly ruled out.

## 5.2 · What the curve says about the same session — and it does NOT agree with the corpus

**`M1218` [measured]** — live 09-01 (⚠ **unsettled, NYSE open**; settled values in brackets):

| | 08-27 | 08-31 (settled) | **09-01 [live]** | 08-31 → 09-01 |
|---|---:|---:|---:|---:|
| `^FVX` (5y) | 4.396 | 4.507 | **4.520** | **+1.3 bp** |
| `^TNX` (10y) | 4.672 | 4.758 | **4.766** | **+0.8 bp** |
| **`^TYX` (30y)** | 5.191 | 5.249 | **5.248** | ★ **−0.1 bp — FLAT** |
| `CL=F` | 83.53 | 85.76 | **87.89** | **+2.5%** |
| `BZ=F` | 89.70 | 90.49 | **92.20** | **+1.9%** |
| `VIXCLS`/`^VIX` | 14.51 | 14.92 | **15.66** | +0.74 |
| `DX-Y.NYB` | 99.160 | 99.430 | **99.517** | +0.09 |

★ **The long end did not move.** A genuine inflation repricing driven by a supply shock should push
the **30-year** hardest; instead `^TYX` is **flat to −0.1bp** while the **5y and 10y** rose. That is
the **same front/belly-led shape as 08-28**, which is what §A-1 called a policy-path move.
★ And one of the window's own headlines says so explicitly, against the other four:
*"**US 10-year Treasury yield tops 19-month high as oil prices fuel RATE-HIKE bets**"*
[economictimes, 09-01] — i.e. oil → **the Fed's path**, not oil → term premium.

## 5.3 · Verdict on the challenge: UNRESOLVED, and the arbiter is already registered

🚫 **§A-1 is NOT retracted, and it is NOT defended.** The two instruments disagree:
**the corpus says inflation; the curve's shape says policy path.**

★ **The report anticipated exactly this and wrote the arbiter into `P121`'s KPI**, verbatim:
> *"`T10YIE` **2.31** — under A it should stay ≤ 2.36. **If branch A fires WITH `T10YIE` above 2.42
> the claim is right about direction and wrong about mechanism**."*

`[FRED]` `T10YIE` last observation is **2026-08-31 = 2.31**; **no new observation exists yet.**
⇒ **The challenge is live, dated, and scoreable on a pre-registered threshold — no threshold is
moved** (`D242`). **The next run settles it, not this addendum.**

## 5.4 · Two disclosures this burst forces, neither of them a score
1. **`P124`'s branch-B conjunct is at risk on the live tape.** B requires `hy_oas ≤ 2.50` **AND**
   `VIXCLS ≤ 15.5`; `^VIX` reads **15.66 [live, unsettled]**. ⚠ **Disclosed, explicitly NOT scored** —
   `P124` settles on `[FRED] VIXCLS` at the first close covering **2026-09-18**, and this desk's
   pre-settle reads are **0 for 4**.
2. **`P122`'s A-branch price leg is already through its threshold on an unsettled bar.** A requires
   `CL=F` **≥ 88.00** at `[COT 09-08]`; the live print is **87.89**, within 0.13%. ⚠ **The
   positioning conjunct (spec ≥65th %ile, currently **43rd**) is the binding leg and is unchanged.**
   **Disclosed, not scored.**

## 5.5 · The two bursts that are NOT findings, said so rather than padded
- **`rate hike` 6.5× (23 articles)** — body-read: *"Dollar gains on rate hike expectations, yen
  retreats past 160"* [KITCO] and *"MUFG sees BoJ rate hike bets as key FX driver"* [CryptoRank].
  ⇒ **this is the BoJ/yen leg, not a new US fact.** It **corroborates** §B-3's Card-3 reading that the
  duration event is **global** (UK 28-year high · Japan · US together) rather than a Warsh-only story.
  **Not a challenge; a confirmation of the widened frame.**
- **`downgrade` 3.2× (3 articles)** — body-read: *"Jim Cramer's top 10 things to watch"*,
  *"Robinhood upgraded, Uber initiated"*, *"4 Reasons Why SCHD May Be In Trouble"*. ⇒ **generic
  analyst-call roundups with no regime content. Noise, and it is labelled noise rather than
  written up.** ⚠ This is the third `drift_watch` term set in recent runs whose 🚨 is a roundup
  artifact — **`D462`**: *`drift_watch`'s `downgrade` set excludes single-name analyst-action
  roundups, or the term is retired.*
- ⚠ **Non-burst activity, recorded for the denominator**: `strikes on Iran` 2 · `new tariff` 1 ·
  `ceasefire` 2 · `blockade` 2 · `bankruptcy` 1 · `default` 3 · `invasion` 1.

## 5.6 · One name-level fact the burst carried, handed to the next run
*"Stock Market Today: Dow Falls As Oil Prices, Treasury Yields Jump; **Nvidia, Micron Shares Slide**"*
[yahoo_finance, 09-01, live coverage]. ⇒ **`MU` — tagged 🟡PARTIAL in `BET_SHEET §B-2` on settled
08-31 flow (OBV +0.095 매집, `rs20` +14.3 vs `SPY`, Δ +0.255) — is sliding on the unsettled 09-01
session.** ⚠ **Not a tag change** (the tag is pinned to settled data by construction); **carried into
the next run's inheritance as a dated observation against its own re-check (09-14 / 09-24).**
