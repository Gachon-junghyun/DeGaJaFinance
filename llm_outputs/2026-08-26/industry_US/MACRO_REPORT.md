# MACRO_REPORT — industry_US · 2026-08-26 (Stage 1 / L1·MACRO)

> Wind direction only. **Zero buy/sell recommendations, zero sizing (P4).**
> Run clock **2026-08-26 22:1x KST = 09:1x ET, Wednesday US PRE-MARKET**.
> **Terminal SETTLED equity bar = 2026-08-25 (Tuesday).** `n_new_sessions_since_prior_run = 1`.
> **Terminal joint `[FRED]` rates observation = 2026-08-24** (`D333`, 8th reproduction — see §A-0).

---

## ★★★ The one thing this report exists to say today

**The rotation the last run called its governing fact gave back more than half of itself in the very
next session — and the desk's own second extreme did the same thing 24 hours earlier.**

`EW{Staples+HealthCare} − EW{IT}` 5-session went **+9.336 (97.6th %ile of 252, 08-24) → +3.905
(85.7th %ile, 08-25)**: **−5.43pp in one session, 58% of the distance from p97.6 back to the p50
median, on `n=1`.** In the same 24 hours **`P79` rolled +7.9pp** (−10.852 → −2.977) and was scored
`FIRED-C`. ⇒ **Two consecutive percentile-extreme readings, both called load-bearing by the run that
took them, were substantially erased by the next single close.** That is a statement about **this
desk's 5-session estimator**, not about the market: at a 20-session sd of ~4.7pp, a 5-session window
sheds one-fifth of its content every day, so a p97 reading is a **claim with a one-day half-life**.

Underneath it, **the composition changed and it changed in the two places the desk is most committed**:

- **Information Technology `exc1 +0.884` = the board's BEST single session**, and the bounce is
  **concentrated in exactly the hardware nodes that were sold** (Comms Equipment +2.48 · Electronic
  Equipment +2.73 · Electronic Components +2.27 · Tech Hardware +1.70 · Semis +1.11 vs Systems
  Software **−1.27**). `exc5` improved **−4.761 → −1.449** and negative breadth improved **43/56 → 36/56**.
  🚫 **This is not called a turn** — `exc5` is still negative, and the software−hardware gap
  **survives at 10.36pp** (Application Software **+4.75 at 91.7% participation** vs Tech Hardware
  **−5.61 at 16.7%**), so the 08-25 desk's *"a HARDWARE de-rate, not one trade"* **replicates on a
  second frame** (`M935`).
- **Energy `exc1 −1.991` = the board's WORST single session**, `exc5 −2.763` with **14 of 16 negative**
  and **0% participation in refining**. **The refiner kill the last run said was one session from
  firing HAS FIRED on settled bars**: the 5-session 3-2-1 crack rate printed **−2.862 (08-24) then
  −1.675 (08-25) = two consecutive negatives** (`M936`). ⚠ **And the kill remains a weak
  discriminator**: re-measured today, two consecutive negatives occur on **36.1%** of the trailing 252
  sessions (`D352`, 08-25 measured 35.5%) — **the desk's regime marker fires better than one day in
  three by chance.**

**The cause is dated, primary-sourced and de-escalatory, not demand-side**: `brief` 08-25 carries
*"Oil Prices Fall as **Iran Negotiation Hopes Return**"*, *"**Iran, Oman Push Talks for 'Interim'
Reopening of Hormuz Strait**"* [9 art / 8 outlets], against *"New Tanker Strike in Hormuz as Iran
Vows Retaliation"* in the same cluster. The sibling KR desk measured the same instrument independently
this morning (`M934`: Brent −2.35% then −3.89%, below $90, on *"eased fears over Iran sanctions"*).
⚠ **Same 24 hours, opposite bodies** — this is an oscillating regime variable and every proposition
below carries both branches (the recurring failure class this stage is told to watch).

---

## §0 · What this report may NOT claim, stated before the numbers

Inherited verbatim from `preflight/PREFLIGHT.md` (3 PASS / 4 FAIL) via `HANDOVER.md §0`:

1. 🚫 **No news-velocity or theme-freshness citation as a cross-sectional ranking**, and **no
   "quiet"/"no news" verdict on any name or sector** (G1, `vel_coverage` 17.06% vs an 80% bar).
   Hand-run single-term lookups remain legal — they are the probe that passed — and are used in §B-3
   **with their base counts printed**, never as a ranking.
2. 🚫 **No bare concentration number** — any unit count carries its `--days` on the same line
   (G4: 250d → 11 units · 500d → 10 · 750d → 10, groupings differ).
3. 🚫 **`wflow` is not a current weighting** — `us_top300.csv` is **42 days old** (G5). Where `wflow`
   and `eqflow` disagree, **`eqflow` is the citable one**. ★ **This run has a priced casualty of that
   staleness, see `M937`.** ⚠ **The 08-21 sweep's `eqflow` column is itself 4 days old and is stamped
   as such wherever it appears; today's SWEEP has not run yet.**
4. 🚫 **Health Care may not be promoted/demoted on the weighted-flow bucket** — `LLY` owns the sign
   (G3). HLTH is ranked below on **price and `eqflow` only**, stated inline.
   ★ **And the flipper MOVED**: 08-25's restriction was on Consumer Staples/`WMT` and is **LIFTED**.
   PREFLIGHT now carries a `vs-yesterday` DIFF column implementing `D358-KR` the morning it was filed.
5. 🚫 **No IC-backed sizing language** anywhere (G6, 0.50/day accrual = 2.0× slow). No sizing at all
   in this stage regardless (P4).
6. ⚠ **`n=1` new settled session.** `S5` binds every claim below: one close does not test a regime.
   The regime call (§1 of `STANDING_VIEW`) is **carried unchanged and stays `[inferred]`**.

---

## §A · Primary indicators — `[FRED]`, both halves, percentiles inside their own pull windows

### A-0 · 🚨 `D333`, 8th reproduction — and it is designed around, not discovered at scoring
`DGS10` · `DGS2` · `DFII10` all terminate **2026-08-24**; `T10YIE` carries **2026-08-25**;
`DTWEXBGS` **2026-08-21**; `NFCI` **2026-08-21**. ⇒ **The last date on which all four rate legs are
jointly observable is 2026-08-24** — one session behind the equity tape. Every rates claim below is
stated on the **joint 08-24 frame**, and `P101`/`P102` settle on **joint** dates by construction.

### A-1 · The rate move over the last week is a FLATTENING, and its composition rotated from real to inflation

| Date | `DGS10` | `DGS2` | 2s10s | real 10y (`DFII10`) | 10y breakeven (`T10YIE`) |
|---|---:|---:|---:|---:|---:|
| 08-17 | 4.72 | 4.19 | **+53bp** | 2.44 | 2.28 |
| 08-19 | 4.65 | 4.19 | +46bp | 2.35 | 2.30 |
| 08-21 | 4.74 | 4.24 | +50bp | 2.40 | 2.34 |
| **08-24** | **4.70** | **4.24** | **+46bp** | **2.38** | **2.32** |
| Δ over the week | **−2bp** | **+5bp** | **−7bp** | **−6bp** | **+4bp** |

**Both halves, `C2`**: the **level** barely moved (10y −2bp) while the **shape** and the **composition**
both did — the curve flattened 7bp because the 2y rose 5bp against a 10y that fell, and inside the 10y
the **real yield fell 6bp while the breakeven rose 4bp.**
⇒ ★ **This INVERTS the "front-end-led REAL-rate rise" the desk has carried since July, and it inverts
`P97`'s own registration reading** (08-21: *"real 10y 2.40 **+5bp** with the breakeven **FALLING** to
2.32 ⇒ the nominal rise is **entirely real**"*). **On the 08-24 joint frame the signs are reversed on
both legs.** ⚠ The magnitudes are 4–6bp on a 137-observation window — this is a **composition note,
not a regime call** (`C4`), and `P97` is **not** re-banded (`D242`); it settles as registered.
Window percentiles (137-obs pull, stated as such, **not** as 365-day figures): `DGS10` **96th** ·
`DGS2` **92nd** · real 10y **85th** · breakeven **52nd**. (`M938`)

### A-2 · Credit and financial conditions — the axis that forbids a stress narrative, 3rd consecutive run

| Series | Level | Date | Percentile *in this 120-day pull* |
|---|---:|---|---:|
| **HY OAS** (`BAMLH0A0HYM2`) | **2.69%** | 08-24 | **9th** — 6bp off the pull's low (2.63) |
| IG OAS (`BAMLC0A0CM`) | 0.81% | 08-24 | 75th |
| **NFCI** (Chicago Fed) | **−0.566** | 08-21 | **4th — the LOOSEST reading in the entire 28-week pull** |
| VIX | 15.85 | 08-24 | 16th (was 18.67 twenty obs ago) |

⇒ **Any claim of credit stress or risk-off this run is `[narrative-only]` and must be labelled so.**
Both the daily spread axis and the weekly conditions axis say **easing, at their own extremes**.
⚠ **One genuine internal disagreement, stated rather than smoothed**: HY sits at its pull's **9th**
percentile while IG sits at its **75th** — the investment-grade spread is relatively the wider of the
two. On a 143-observation window with an 8bp IG range that is **indistinguishable from noise (`C4`)**
and is logged, not interpreted.

### A-3 · Positioning — `[COT, Tue-close, 3–4 day lag ⇒ CONTEXT, not a trigger]`

| Instrument | Net spec | Weekly Δ | 1y %ile | Read |
|---|---:|---:|---:|---|
| **Nasdaq-100** | −12,067 | **+30,838 ▲** | **4th** | ★★ **Board's largest weekly swing, and it is a short cover** — specs remain crowded-short at the 4th percentile |
| S&P 500 (E-mini) | **−10,560** | −21,840 ▼ | 84th | 🚨 **`D327`, 5th run: the row prints 🟢 "crowded-long" on a NET SHORT position.** **Label unused.** The *number* (largest negative weekly swing on the board) is used; the tag is not |
| **Copper** | +79,748 | −640 ▼ | **100th** | 🚨 **The board's only 100th-percentile reading, 4th consecutive run** — and Materials' entire 5-session excess is `FCX`+`NEM` (§E) |
| UST 10Y | −946,961 | −31,908 ▼ | 5th | Crowded-short, and getting shorter |
| Nat Gas | −203,503 | −6,368 ▼ | 0th | Crowded-short at the floor |
| UST 2Y · USD · WTI · Gold · Silver · Russell | — | — | 15–76th | Neutral-to-crowded-short; no extreme |

★ **The positioning tape and the price tape disagree about IT, and the disagreement is the useful
part**: NDX specs are at the **4th percentile short** *after* a 5-session hardware de-rate, into the
epicenter's own print tonight. **That is contrarian ammunition, not a direction** (P4).

### A-4 · Per-name short pressure — `[FINRA Reg SHO daily, dated 2026-08-25, matches the settled bar]`
Legal under G5 (all 11 book names are inside the universe; the coverage leg passed).

| Name | short% | 20d base | z | 5v5 | Read |
|---|---:|---:|---:|---:|---|
| **ANET** | 57.8% | 44.4% | **+2.06** | **+6.7 ▲** | 🔴 **Board's highest** |
| **NVDA** | 42.6% | 35.6% | **+1.78** | +2.4 ▲ | 🔴 **Short surge into its own D-0 print** |
| **AVGO** | 20.7% | 36.3% | **−2.17** | **−10.4 ▼** | 🟢 **Board's largest short EXIT**, into its own 09-02 print |
| **HPE** | 28.3% | 47.6% | −1.73 | −13.2 ▼ | 🟢 Second-largest exit |
| MPC · PSX · XOM · FCX · NEM · LLY · WMT · ETN · NUE · RTX · MET · NDAQ | — | — | −1.29…+1.12 | — | 🟡 all inside ±1.5 |

★★ **Inside one AI-compute complex the short book is SPLITTING, not moving as a bloc**: pressure onto
`NVDA`/`ANET`, off `AVGO`/`HPE`, spread **4.23 z-units** on the same day. (`M939`)
⚠ `D6`: this is a **B-grade** order-flow axis (an actual reported print, not a derived tag), and it is
the only per-name flow axis this stage cites — the sweep has not run yet.

### A-5 · The last monthly prints, both halves (`C2`) — and they lag a month, said plainly
- **CPI, July 2026 (published mid-August)**: **+3.30% YoY** *and* **+0.07% MoM**. A 3.3% annual print
  and an essentially flat month are the same release.
- **Core CPI, July 2026**: **+2.47% YoY** *and* **+0.22% MoM**. Last four monthly cores:
  **+0.38 · +0.21 · −0.02 · +0.22** — no trend in either direction on n=4 (`S5`).
- **Unemployment, July 2026: 4.1%** — the **lowest of the 12-month pull** (range 4.1–4.5).
- ⚠ **All three are ~8 weeks stale relative to tonight's tape.** The next reads are **July PCE 08-28**
  and **August payrolls 09-04**, both `🔀binary` on `CATALYST_WATCH`.

### A-6 · Oil and the crack — the settled frame, and the live frame separated

| Bar | 3-2-1 crack | 5-session rate | Note |
|---|---:|---:|---|
| 08-21 | 69.608 | +2.893 | |
| **08-24** | 66.320 | **−2.862** | 1st negative (15.5th %ile) |
| **08-25 · SETTLED, terminal** | **68.134** | **−1.675** | **2nd consecutive negative ⇒ THE REGISTERED KILL HAS FIRED** |
| 08-26 · **LIVE, partial (CL volume 45% of prior)** | 57.824 | **−9.821** (2.0th %ile) | 🚫 **not a settle** |

- **Base rate, re-measured today**: two consecutive negative 5-session rates occur on **36.1%** of the
  trailing 252 sessions. **The kill fires better than one day in three by chance** (`D352`; the 08-25
  desk measured 35.5% — the two agree). **It is a weak discriminator and this report says so on the
  same line as the firing.**
- 🚨 **`M926`'s futures stub bar has RESOLVED, and the resolution is checkable** (`M940`). The KR desk
  measured `BZ=F` 08-25 this morning as a **137-contract, $0.34-range stub implying −6.81%**, against
  four outlets printing **−3.89% / "Brent below $90"**. This run's pull carries `BZ=F` 08-25 at
  **volume 18,474, close 88.58** — and **92.17 × (1 − 0.0389) = 88.58 exactly.** ⇒ **the provisional
  bar was replaced and now agrees with the outlets.** ⚠ **But the volume field is still wrong**:
  `BZ=F` 08-24 and 08-25 both read **18,474**, and `CL=F` both read **219,422** — a **duplicated
  volume field on two consecutive days**, exactly as the KR desk found. **Price leg: trustworthy.
  Volume leg: not.** No `vol_surge`-style claim is made on the futures complex this run.
- **Brent settles**: −2.35% (08-24) then **−3.89% (08-25)**, i.e. **−6.1% over two sessions, below $90**
  (`M934`, KR desk, same instrument — this is one global contract observed twice, **not** a `W1`
  cross-market transfer of a statistical result).

---

## §B · Narrative — events, trajectories, terms, blind spot. Denominators first.

### B-0 · 🚨 The event pipe returned ZERO for today's market day, and that is a FAILURE, not a quiet day

```
brief --date 2026-08-26 --scope foreign  →  기사 0건 → 사건 0개 → 시장 0개
brief --date 2026-08-25 --scope foreign  →  기사 4,663건 → 사건 757개
brief --date 2026-08-24 --scope foreign  →  기사 4,762건 → 사건 779개
fts search "Nvidia" --days 1 --count --scope foreign → 1,562     ("Fed" 437 · "tariff" 588)
```
**The rolling 1-day FTS index answers with three-figure counts while `market_day = 2026-08-26` holds
zero rows.** ⇒ the foreign feed has **not yet been assigned to today's market day**; the pipe is alive
and the denominator is empty. **No "quiet"/"nothing happened" claim is made anywhere in this report**
(G1's removed right, independently re-earned here).
⇒ **Remedy applied and stated: the entire event and trajectory pass is run on `--date 2026-08-25`**,
which is also this run's terminal settled equity bar — so the narrative frame and the price frame are
**aligned on the same day by construction**, which is better practice than the mismatch it replaces.

### B-1 · Event pass · `brief --date 2026-08-25 --body 2 --scope foreign` · coverage stated in full

**Denominator: 4,663 articles → 757 events → 757 market-relevant (non-market 0).**

| Layer | Shown | Total | **Unseen** |
|---|---:|---:|---:|
| Head (≥5 outlets) | 89 | 89 | 0 |
| Body (2–4 outlets) | 31 | **668** | **637** |
| Tail (exactly 2) | 0 | 0 | 0 |
| **Single-outlet** | **15 (random)** | **622** | **607 = 97.6%** |
| Non-market boundary (nb > −3.0) | 0 | 0 | 0 |
| Sub-events recovered (`└`) | — | **200** | — |

🚨 **`D339` reproduces and is quantified: 607 of 622 single-outlet items (97.6%) went unseen**, and the
tool states why — **622 of them carry NO classifier score at all because the classifier is
Korean-only.** Against 08-25's 96.25% this is **worse**, on a fuller denominator.
⇒ **Total displayed: 120 of 757 events = 15.9%.** Any statement below about what the day contained is
a statement about **the 15.9% that was rendered**, and is written that way.

**What the head layer actually held (`[news]`-grade, outlet counts inline):**

| Cluster | art/outlets | Why it is here |
|---|---:|---|
| **Canada set to announce retaliatory tariffs against US** | **80 / 29** | ★★★ **The day's #1 by a wide margin.** Carney matching Trump with a **50% tax on US goods**; **Section 338** tariffs; *"US unlikely to win its 'dumb trade war'"*. Effective date **09-08** |
| Oil steady/falling on expanded US sanctions | 48 / 15 | *"Oil Prices **Fall** as **Iran Negotiation Hopes Return**"* · *"Crude Sharply Lower as Middle East Hostilities…"* |
| **Iran–Oman push for an 'interim' Hormuz reopening** | **9 / 8** | 🚨 **This is `S8`'s object and `CATALYST_WATCH`'s undated *"Strait of Hormuz open" TACO trigger*** — and it is still **undated** for a 27th run |
| Bessent's "D-Day" Iran sanctions · China angered | 23/14 + 22/10 | `S119` settles on this, **08-27** |
| **Fed May Need to Tighten Soon Without Progress on Inflation** | **29 / 7** | 🚨 *"US rates need to rise soon absent evidence of ongoing drop"* — a **hike** framing, against `DGS2` at the 92nd percentile of its pull |
| Nvidia earnings preview | 45 / 11 | *"History Says Nvidia Is Likely To Fall on Wednesday"* · *"Nvidia Has Become a Banker to the AI Boom"* |
| Bitcoin crosses $80,000 | 60 / 14 | The 08-22 body ties it to *"a **Treasury buyback tweak**"* — `S102`'s object, still running |
| **Druckenmiller calls Bessent's bond buys a mistake** | 11 / 9 | The long-end-cap thread `P77` brackets |
| Russia extends diesel export ban through September | 2 / 2 (sub) | 🚨 **`M93`'s object.** Paired with *"Ukraine Hits Another Russian Refinery as Fuel Crunch Worsens"* |
| US consumer confidence falls in August (Conference Board) | 10 / 7 | The only US macro print inside the day |
| Dick's Sporting Goods crashes on weak sneaker demand | 29 / 11 | Consumer discretionary, single-name |
| Apple unveils Mac mini / Mac Studio | 39 / 15 | IT hardware, product cycle |
| SpaceX Starship complex, Louisiana · *"SpaceX's power needs will make it Oklo's biggest customer"* | 15/11 + 14/7 | 🚨 `OKLO` is **outside `us_top300`** (`D341`) — untaggable |

⚠ **Read from the single-outlet random 15, not from the head** — the tier the L2 says rates and FX live
in: **`[bloomberg] "How the World Adapted to the Strait of Hormuz Crisis"`** ·
**`[yahoo_finance] "Nvidia Customers Face a 15% Price Hike"`** · `[wsj] "The Metals Lobby's Big Steal"`.
The `NVDA` pricing item is materially relevant to tonight's print and sat at **one outlet**.

### B-2 · Trajectories · `thread --days 7 --scope foreign`

🚨 **The default call is UNUSABLE and was replaced, not quoted.** `thread --days 7` with today's
window end returned **471 threads, ALL tagged `ENDED`, "살아있는 0"** — because the window's terminal
day (**08-26**) carries **0 articles** (§B-0). The tool's own warning names this failure
(*"a holiday/low-volume window end inflates FADING — read the per-day denominator first"*), and the
per-day line printed `08-26 0건`. **A run that quoted "471 threads ended" would have written a
fabricated regime read out of an empty denominator.**
⇒ **Re-run as `thread --date 2026-08-25 --days 7`** (window 08-19 → 08-25):
**4,571 daily events → 3,481 threads · 589 multi-day · 261 ALIVE · 481 new.**

| Tag | Curve (outlets/day, 08-19 → 08-25) | Thread | Total |
|---|---|---|---:|
| **BUILDING** | **23 → 9 → 11 → 24 → 20 → 21 → 29** | ★★★ **US–Canada trade war** | 370 |
| **BUILDING** | 16 → 10 → 7 → 13 → 12 → 18 | AI governance / training-data disclosure | 260 |
| **BUILDING** | 6 → 13 → 14 → 6 → 8 → 12 → 15 | Russia/Ukraine + **Russian fuel crisis** | 143 |
| **BUILDING** | 7 → 12 → 13 → 4 → 3 → 9 → 14 | Bitcoin (08-22 body: *"a Treasury buyback tweak"*) | 292 |
| **BUILDING** | 11 → 10 → 11 → 5 → 4 → 9 → 12 | ETF flows | **447** |
| **BUILDING** | 6 → 4 → 8 → 4 → 6 → 15 | Apple product cycle | 123 |

★★★ **The Canada thread's SHAPE is the finding, not its size.** Read its titles in order:
**08-19 *"Trump PAUSES tariffs on Canada after last-minute deal"* (23 outlets) → 08-20 *"US set to CUT
tariffs on Canada metals, autos"* → 08-21 *"Canada, US inch closer to trade deal"* → 08-22 *"Canada
announces RETALIATORY tariffs"* (24) → 08-25 *"Canada set to announce retaliatory tariffs"* (29).**
⇒ **A deal narrative inverted into a retaliation narrative inside six days, and ended at its widest
outlet count.** This is the transmission channel for the Industrials underweight, and it is **dated**:
**tariffs effective 2026-09-08**. (`M941`)

### B-3 · Term sweep — **counts and bases printed; `D340`'s readable band ~60–2,000 applied**
Terms passed as **single quoted phrases**, never multi-word AND (the silent-zero trap).

| Term | Base (90d) | Printed verdict | 7d avg | Accel | Readable? | vs 08-25 |
|---|---:|---|---:|---:|---|---|
| **`Jackson Hole`** | 633 | 🟡ACCEL | 77.0 | **26.25×** | ✅ | **↑ from 23.17×** |
| **`Iran sanctions`** | 212 | 🟡ACCEL | 22.9 | **22.12×** | ✅ | **↑ from 16.86×** |
| `national debt` | 321 | 🟡ACCEL | 26.6 | 8.13× | ✅ | ↓ from 8.57× |
| `Treasury buyback` | 259 | 🟢FRESH age 7 | 36.4 | (273.21×) | ✅ base | ⚠ **ratio degenerate** — see note |
| **`Canada tariff`** | 94 | 🟡ACCEL | 7.1 | **5.10×** | ✅ | 🚨 **↓ from 10.99×** |
| `drug pricing` | 166 | ⚪ECHO | 6.0 | 1.76× | ✅ | ↓ from 2.19× |
| `consumer confidence` | 624 | ⚪ECHO | 17.0 | 1.46× | ✅ | new |
| **`AI capex`** | **1,189** | **⚪ECHO** | 15.6 | **0.66×** | ✅ | **0.62× → 0.66×, 2nd run decelerating** |
| **`HBM`** | 1,336 | ⚪ECHO | 23.3 | **0.88×** | ✅ | new — in band |
| **`memory prices`** | 970 | ⚪ECHO | 16.9 | **0.80×** | ✅ | new — in band |
| `Rubin` | 1,374 | ⚪ECHO | 38.9 | 1.76× | ⚠ in band, **precision suspect** | see note |
| `refining margin` | 273 | ⚪ECHO | 5.6 | 0.78× | ✅ | 3rd run negative |
| **`diesel export`** | 195 | ⚪ECHO | 2.9 | **0.54×** | ✅ | new |
| `Strait of Hormuz` | **8,224** | (⚪ printed) | 104.6 | (0.66×) | 🚫 **above band — label only** | |

★★★ **The load-bearing row is the AI cluster, and all three legs agree**: `AI capex` **0.66×**,
`memory prices` **0.80×**, `HBM` **0.88×** — **every one inside `D340`'s readable band and every one
below 1.0, on the eve of the epicenter's own print.** ⇒ **the AI-compute de-rate arrives while its own
narrative decelerates on three independent terms.** (`M942`) `AI capex` is now the **second
consecutive** run at ⚪.

🚨 **`Canada tariff` accel FELL 10.99× → 5.10× while its event thread BUILT from 21 to 29 outlets and
80 articles.** The instrument and the event moved in **opposite directions on the same day**. This is
`D345`'s class — the trade slot's term is too narrow to catch *"retaliatory tariffs"*, *"Section 338"*,
*"Carney"* — but `D345` was logged on a **falling** event; **this is the first time it has been
measured on a RISING one**, which is the more dangerous direction because it **reads as calm.**
⇒ registered as **`D362`**.

⚠ **`Treasury buyback`'s 273.21× is a degenerate ratio, not a signal** — a 7-day average of 36.4
against a near-zero 90-day baseline. **Its `🟢FRESH` tag is age-driven (age 7) and the base (259) is in
band, so the AGE is readable and the ACCELERATION is not.** Stated rather than quoted as 273×.
⚠ **`Rubin` at base 1,374 is inside the band arithmetically but is a PRECISION risk** — the token
matches the Vera Rubin Observatory and personal names. Yesterday's blind-spot pass measured
`RUBIN` at **8 articles / 5 outlets** in titles; a 1,374 90-day base cannot be the same object.
**The ratio is not used.** (`D363` candidate — see §F.)

### B-4 · Blind-spot pass · `burst --date 2026-08-25 --scope foreign` · rows read raw
**Denominator 4,973 · 30-day baseline · market-relevance ≥40% · 665-company universe · field = title.**

- **① spiked (z-order):** `STUDIO` **12.7** (15 art/11 outlets/80% mkt) · `MAC` **12.0** (31/13/87%) ·
  `MINI` **11.1** — all one object, **Apple's Mac Studio/mini launch**. Then `CRM` 6.9 (12/4/100%) ·
  `EMISSIONS` 5.1 · **`INTUIT` 4.7 (12/8/92%)** 🆕 · `LINUX` 4.7 · **`CPUS` 4.2 (6/6/100%)** ·
  **`NORTHROP` 4.0 (5/2/40%)** 🆕 · `STREAK` 3.6 (21/10/71%) · `RECOVER` 3.4 (9/6/78%) ·
  **`RUBIN` 3.3 (8/5/75%)** · `SMUGGLING` 3.2 · `CHIPS` 2.8 (32/9/75%).
- **② new words:** `CYBERTRUCK` 11 (100% mkt, 3 outlets) · `VAULT` 10 · `PELOSI` 9 · `VEEVA` 9 (100%) ·
  **`WORKLOADS` 7 (5 outlets, 86% mkt)** 🆕 · `DISPOSITION` 7 · `NKE` 4.

★★★ **The pass refuted its own prior run's headline number, and the refutation is arithmetic (`M943`).**
The 08-25 run recorded **`RUBIN` at z 8.4** and built `D354` on it. **Today the identical 8 articles /
5 outlets / 75% market relevance measure `z 3.3` — a 61% fall with ZERO change in the underlying
counts.** The only differing variable is the denominator: **2,102 (partial day, run at 09:1x ET) vs
4,973 (complete day).** ⇒ **A `burst` z computed on a partial-day denominator is systematically
overstated, and this desk runs pre-market EVERY day.** `D354`'s *observation* (the term table has no
product-generation slot) survives; **its z is withdrawn as an artifact, not contradicted.**
⇒ registered as **`D364`**, and it is a sibling of `D355` (both are "this desk runs before the day is
finished, and its instruments do not know that").

⚠ `STREAK` (21 articles / 10 outlets) is literally *"Nvidia Notches Longest Losing Streak Since 2022"*
and `RECOVER` is *"Memory Stocks Recover"* — **the blind-spot pass found the tape's own two-sided
sentiment into tonight's print** before any price axis was consulted. Logged; not interpreted (P4).
⚠ `EMISSIONS`, `VEEVA`, `CYBERTRUCK`, `PELOSI` are 2–3-outlet spikes with no desk object attached —
logged, not interpreted.
⇒ **Terms folded into the living table this run: `WORKLOADS` · `Diamond Rapids` (carried) · `Section 338`
· `retaliatory tariffs`** (the last two seeded specifically to close `D362`). All four are below the
readable base band and are registered as **terms to accrue**, not ratios to read.

---

## §C · Self-backtest — the exhaustive settle table, because "nothing was due" and "nobody checked" look alike

### C-1 · Settled and scored this run: **0.** The two rows dated 08-25 were scored this morning by the sibling `industry_kr` desk.
`P79` → **`FIRED-C`** (−2.977pp) · `S108` → **`FIRED-C` by the letter**, VOID question referred to this
desk. **This desk issued the ruling in `HANDOVER §2b`: NO VOID, row stands, re-labelled
`LOW-INFORMATION-BY-CONSTRUCTION`** (its window contained no event — `R93` moved Warsh's speech to
08-27~29 after the window was frozen). ⇒ new dig **`D365`**, §F.

### C-2 · ⏳ Pre-settle readings — offered as readings, explicitly **NOT** as scores
All computed on the **08-25 settled** frame, i.e. **one session early**. `P79` has just demonstrated
that one session can move a trailing-5 spread by **7.9pp**, so none of these is a verdict.

| ID | Settles | Observable | **Pre-settle reading** | Branches | Standing |
|---|---|---|---|---|---|
| **`P78`** | 08-26 close | range of `exc5` vs `SPY` across {`XLU`,`XLRE`,`XLP`,`XLV`} | 🚨 **4.889pp** — `XLV` **+3.476** · `XLRE` +1.836 · `XLP` +1.299 · `XLU` **−1.412** | A ≥ **4.71** (disperse) · B ≤ 1.69 (one object) · C between = favourite | **ABOVE branch A's line.** If it holds one session, the *"duration complex is one bet"* framing is falsified on the desk's own registered observable |
| **`P80`** | 08-26 close | crack **and** `EW{MPC,VLO,PSX}` exc5 | crack **68.134**; EW **−2.651** (`MPC −2.893` · `VLO −2.553` · `PSX −2.506`) | B needs crack ≤ 58 **AND** EW ≤ −3.740 | **Inside C on both legs**, and the three legs are within 0.39pp of each other — the refiners moved as one unit |
| **`P77`** | first `[FRED]` close covering 08-26 | `DGS30` | **5.23 @ 08-24** (the series has no 08-25 or 08-26 bar yet) | A ≤ 5.18 · B ≥ 5.38 · C between = favourite | **Inside C**, and ⚠ **`D333` means this row cannot be read before 08-27 at the earliest** |
| **`P90`** | 08-26 close | `NVDA` print: margin expansion vs cost pass-through | **Not readable pre-print.** Implied move **±6.0% (expiry 08-28, D2)** correctly spans the event | — | Scored jointly with `S115` per its own registration |
| **`P96`** | 08-27 close | settled 5-session crack rate | **−1.675 @ 08-25** | A ≤ −2.887 · B ≥ +0.468 · C between | **Inside C**, having been **−2.862 (inside A) one session earlier.** ★ The *kill counter* fired (2 consecutive negatives) while the *bracket* did not — **the two are different instruments and this run keeps them apart** |
| **`P97`** | first JOINT date ≥ 08-28 | broad dollar **∧** `DGS10` | dollar **118.063 @08-21** · `DGS10` **4.70 @08-24** | A: dollar ≤117.44 **∧** `DGS10` ≥4.75 · B: ≥118.60 **∧** ≤4.65 | **Inside C on both legs**, neither at an extreme. ⚠ §A-1 shows the row's own compositional premise inverted; **it is NOT re-banded** (`D242`) |
| **`P98`** | 09-03 close | `EW{STPL+HLTH} − EW{IT}` 5-session | **+3.905 = 85.7th %ile** (was **+9.336 = 97.6th** at registration) | A ≥ +3.339 · B ≤ −1.347 · C | 🚨 **−5.43pp in ONE session — 58% of the way from p97.6 to the p50 median.** Barely still above A's line. **B was the disclosed ~50% favourite and it is being paid** |
| **`S101`** | 08-26 close | excluded-vs-admitted `vol_surge` baskets | **+1.616pp** (carried from `HANDOVER §2c`) | A ≥ +4.45 · B ≤ −3.88 · C | Inside C, leaning A. 🚨 **This is `C15`'s US-side settle** |
| **`S103`** | 08-25→08-29 | `NVDA` exc5 vs `SPY` | Window open; `NVDA` `rs20 +6.2` / `rs60 −6.8` | ±5.0pp hand-set | ⚠ **LOW-RESOLUTION by its own registration** — the ±5.0 bands sit inside the ±6.0% implied move ⇒ **pre-declared no-information**. Per `D242` it is not re-banded |

### C-3 · Not yet arrived, named so they cannot be skipped
**Tonight (08-26 close):** `P77` `P78` `P80` `P90` `S101` — **five rows on one date.**
**08-27:** `P96` `P83` `P91` · `S79` `S81` `S115` `S117` · **`S119` settles** · `MRVL` print · Jackson Hole opens.
**08-28:** 🚨 **NINE rows (`D343`)** — July PCE · `S116` `S118` `S120` `S111` · `P67` `P81` `P85`–`P89` `P92` `P93` · `FRO` print.
**08-31:** `S104` `S112` `S124` · MSCI quarterly review. **09-01:** `S113`. **09-02:** 🚨 **`AVGO` print — HELD, and `HANDOVER` records the registration obligation is still open.**
**09-03:** `P84` `P98` `S107` `S110` `S114`. **09-04:** `S126` · Aug NFP.

### C-4 · 🚨 `S8` — undated and unscoreable for the **27th** consecutive run
And this run has the strongest evidence yet that the cost is real: **its object appeared in today's
head layer** (*"Iran, Oman Push Talks for 'Interim' Reopening of Hormuz Strait"*, 9 art / 8 outlets)
and in `CATALYST_WATCH` as an explicitly **undated** `🔀binary`. **A human must `VOID` it or
re-register it with a date (P5).**

### C-5 · Running hit-rate — stated, with its own health warning
Across all rows this desk has scored to date the branch distribution remains **C-dominant by
construction** (most rows disclose C as the favourite at registration, and the `D93` baselines put C
at 35–70%). ⚠ **A high C-rate is not accuracy** — it is a property of tail-set thresholds. The
informative counter is elsewhere and is reported instead: **of the last 4 registered P-rows whose
state was disclosed at a percentile extreme (`P79`, `P98`, and the two `S`-rows `S100`/`S108`),
3 have moved sharply back toward the median before or at settlement.** That is the `M944` finding
below, and it is a criticism of the estimator this desk keeps choosing.

---

## §D · Propositions registered this run — `P100` · `P101` · `P102`

> ⚠ **ID 3-grep executed at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`.
> 🚨 **IT CAUGHT A COLLISION, for the 3rd time in 3 days: `M927`–`M934` were ALREADY TAKEN** by this
> morning's `industry_kr` run (`STANDING_VIEW_KR.md` §2). This run therefore starts at **`M935`**.
> **`P99` is deliberately skipped** — the 08-25 run reserved it because its only greps are
> *"99th percentile"* prose; that decision is honoured rather than reversed. This run takes **`P100`–`P102`**.
> `D362`–`D365` → 0 hits outside this run's own files. Current highest before this append:
> **`M934` · `P98` · `D361-KR` · `R102` · `S126` · `C17`**.
> ⚠ **Language: English** — the US desk's documented practice.

### `P100` — ★★★ The refiner kill fired. Does the 20-day refining leadership survive the commodity break?

**Claim.** The kill counter reached **two consecutive negative 5-session crack rates on settled bars
(08-24 −2.862, 08-25 −1.675)** while the Energy equity leg posted the board's **worst** single session
(`exc1 −1.991`) and **0% refining participation on five sessions**. **Yet `EW{MPC,VLO,PSX}` `exc20`
vs `SPY` is +11.597 = the 77.4th percentile of 252** — the 20-day leadership is fully intact.
`M879`'s ordering replicates a **5th** time on `exc20`: **refining +11.60 > E&P +5.42 > midstream −0.35**.
⇒ **The question is not whether the commodity broke. It is whether twenty days of equity leadership
was the margin story or the barrel.**

| | |
|---|---|
| **Frozen observable** | `EW{MPC, VLO, PSX}` **20-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, at the **2026-09-01** close |
| **Branch A (the margin story survives the barrel)** | **≥ +13.478** (its own trailing-252 **p85**) — leadership *extends* through a two-session −6.1% Brent break |
| **Branch B (it was the barrel)** | **≤ −4.731** (trailing-252 **p15**) — the whole 20-day excess unwinds |
| **Branch C** | between = **the favourite, disclosed** |
| **`D93` executed BEFORE freezing** | `EW{MPC,VLO,PSX}` exc20 vs `SPY`, trailing 252: mean **+4.727** · sd **9.725** · p05 −10.488 · **p15 −4.731** · p50 +4.969 · **p85 +13.478** · p95 +22.084 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **+11.597 = 77.4th percentile** — inside C but already leaning A, disclosed now rather than discovered at scoring |
| **⚠ Base-rate disclosure on the desk's own kill** | **two consecutive negative 5-session crack rates occur on 36.1% of the trailing 252.** The condition that just fired is a **one-in-three** event. This row exists partly *because* the kill is too weak to conclude from (`D352`) |
| **Anti-signal (VOID)** | an **OPEC+ emergency production decision**, a **US SPR action**, or **an announced M&A involving any of the three names** inside 08-26 → 09-01. ⚠ **Base rate checked (`D300-KR`)**: no OPEC+ ministerial is scheduled inside the window. **The Iran/Hormuz de-escalation is deliberately NOT an anti-signal — it is the event**, and voiding on it would be the designed-to-void defect that killed `S91`/`S93` |
| **Information content (`L3`/`B4`)** | **A falsifies** the reading this report just built (that the commodity break is repricing the margin story) and confirms `L2`'s peak-margin trap is **not** loading yet. **B falsifies** `M879`'s five-run refining-over-E&P ordering as a barrel artifact. **Neither branch merely confirms** |
| **Non-redundancy (`D343`)** | 09-01 carries only **`S113`** (the semis chain into `NVDA`). `P96` (08-27) measures the **COMMODITY**; `P80` (08-26) measures a **5-session** equity window with a crack conjunction; **`P100` measures the 20-SESSION equity window alone.** All three can disagree and the disagreement is the point |
| **Owner** | `industry_US` |

### `P101` — ★★ The IT de-rate is a hardware de-rate. Does the software−hardware gap close on the AVGO print?

**Claim.** The 08-25 desk's *"hardware, not one trade"* finding **replicates on a second frame**:
`EW{IT software+consulting, n=19} − EW{IT hardware+semis+semicap, n=37}` 5-session = **+6.228 = the
89.7th percentile of 252**, against a two-year mean of **−1.936** (i.e. the *normal* state is hardware
beating software). Participation confirms it is not a mega-cap artifact (`W5`): **Application Software
91.7% positive on five sessions vs Tech Hardware 16.7%, Semicap 0.0%, EMS 0.0%.**
★ **But the 08-25 session bounced the hardware side specifically** (Comms Equipment `exc1` +2.48,
Electronic Equipment +2.73, Electronic Components +2.27 vs Systems Software **−1.27**), and the gap
narrowed **14.21pp → 10.36pp**. **`AVGO` prints 09-02, inside the window.**

| | |
|---|---|
| **Frozen observable** | `EW{Application Software, Systems Software, IT Consulting; n=19}` **minus** `EW{Semiconductors, Semiconductor Materials & Equipment, Technology Hardware/Storage, Electronic Components, Electronic Equipment, EMS, Communications Equipment; n=37}`, **5-session returns**, `us_top300` constituents, settled closes, at the **2026-09-04** close |
| **Branch A (software keeps winning through both prints)** | **≥ +3.196** (trailing-252 **p85**) |
| **Branch B (hardware repairs)** | **≤ −7.906** (trailing-252 **p15**) |
| **Branch C** | between = **the favourite, disclosed** |
| **`D93` executed BEFORE freezing** | trailing 252: mean **−1.936** · sd **6.279** · p05 −12.282 · **p15 −7.906** · p50 −2.310 · **p85 +3.196** · p95 +10.369 ⇒ **A ≈15% · B ≈15% · C ≈70%.** ★ **The centre is NEGATIVE (−1.936), so "software beats hardware" is the ABNORMAL state** — the row is written knowing its own baseline is asymmetric (`D93`, and `P78`'s lesson that an estimator's centre is not zero) |
| **State at registration** | **+6.228 = 89.7th percentile.** On the 10-day version: +3.270 = 84.5th |
| **⚠ Event contamination — OWNED, not voided** | the window **08-27 → 09-04 contains the `NVDA` post-print sessions, `MRVL` 08-27, Jackson Hole, July PCE 08-28, `AVGO` 09-02 and Aug NFP 09-04.** **There is no clean 5-session window in the next fortnight.** Making any of them an anti-signal would be the designed-to-void defect. **The row deliberately measures the gap THROUGH the cluster** |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 of the 56 IT constituents between the two legs**, or a **trading halt ≥1 full session** in `NVDA` or `AVGO`. ⚠ **Base rate checked**: MSCI's 08-31 review does **not** change GICS assignment and is explicitly **not** a voider |
| **Information content (`B4`)** | **A** says the desk's `IT UW` is aimed at the wrong half of its own sector — the UW is arithmetically short a node running at 91.7% participation. **B** says the de-rate was a hardware air-pocket that repaired inside two prints, which retires the whole "hardware epicenter" framing. **Neither branch merely confirms** |
| **Non-redundancy (`D343`)** | 09-04 carries **`S126`** (Aug payrolls → Industrials) — a labour/cycle row on a different sector. **`S124`** (08-31) asks whether IT *breadth* repairs through its two prints; **`P101` asks WHICH HALF of IT does the repairing.** They can both fire and say different things |
| **⚠ `W3`** | this measures whether a spread persists, **not** whether any position was right. No sizing (P4) |
| **Owner** | `industry_US` |

### `P102` — ★★ Materials has no sector trade — it has two names, both at extremes, with COT copper at the 100th percentile

**Claim.** Materials prints the board's best `exc5` (**+3.740**) and it is **two names**: `FCX`
(Copper) **exc5 +20.69 / exc20 +26.26** and `NEM` (Gold) **+16.72 / +44.28**. The other ten names
carry `exc20` **−0.686 mean / −8.211 median with 9 of 12 negative**, and **Steel is −6.70**.
`EW{FCX,NEM} − EW{other 10 MATR}` 10-session = **+18.731 = the 98.8th percentile of 252.**
Against that: **CFTC copper spec positioning sits at the 100th percentile of one year, 4th consecutive
run**, and the 08-25 desk recorded both names *"at or above consensus mean targets within 3.5% of
their 52-week highs, `NEM` with current-year revisions 1↑/11↓ on a −9.6%/90d cut."*
⇒ **A sector verdict on Materials is a two-name momentum bet wearing a sector label** (`W5`).

| | |
|---|---|
| **Frozen observable** | `EW{FCX, NEM}` **minus** `EW{LIN, SHW, ECL, CRH, APD, NUE, CTVA, VMC, MLM, STLD}`, **10-session returns**, settled closes, at the **2026-09-09** close |
| **Branch A (the two-name concentration extends)** | **≥ +13.450** (trailing-252 **p95**) — a 98.8th-percentile state goes further |
| **Branch B (mean reversion)** | **≤ +2.505** (trailing-252 **p50**) — the spread returns to its own median |
| **Branch C** | between (**+2.505 → +13.450**) |
| **`D93` executed BEFORE freezing** | trailing 252: mean **+2.093** · sd **7.599** · p05 −10.158 · p15 −6.890 · **p50 +2.505** · p85 +9.928 · **p95 +13.450** ⇒ **A ≈5% · B ≈50% · C ≈45%. B is the favourite and is disclosed** — from the 98.8th percentile, reversion is the base case and this row says so before the fact |
| **⚠ Asymmetric branch design, declared** | A is deliberately set at **p95, not p85**, because the state is already at p98.8; using p85 would make A near-certain and therefore uninformative (`B4`) |
| **State at registration** | **+18.731 = 98.8th percentile**, above p95 |
| **Anti-signal (VOID)** | an **announced acquisition of `FCX` or `NEM`**, or a **US tariff action naming copper or gold specifically** inside 08-26 → 09-09. ⚠ **Base rate checked**: **Canada's retaliatory tariffs take effect 09-08, INSIDE the window**, and metals are named in the 08-20 cluster (*"US Set to Cut Tariffs on Canada Metals, Autos"*). **This is disclosed as a KNOWN in-window event that is NOT a voider** unless it names copper or gold specifically — a broad tariff action is exactly the mechanism the row should be exposed to |
| **Information content (`L3`)** | **A** says the desk's `MATR N+` is a defensible sector call only if it is written as a two-name call, and the 100th-percentile COT is not yet binding. **B** says every Materials sector verdict since 08-21 was a momentum artifact and the sector's real state is the other ten names (`exc20 −0.686`). **Neither branch merely confirms** |
| **Non-redundancy (`D343`)** | 09-09 carries only `S58-KR` (KR-owned) and three rejection rechecks. `S122` (09-30) brackets **Shell's chemicals sale and `XOM`'s control role** — a different object in a different sector |
| **Owner** | `industry_US` |

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each

> **This is ROTATION's input. It sets wind direction only** — not a ranking.
> **`exc1`/`exc5`/`exc20` are equal-weight `us_top300` constituent baskets, excess vs `SPY` (named
> inline), computed from this run's own price frame on the 2026-08-25 SETTLED close** — the unsettled
> 08-26 pre-market bar was **explicitly dropped** (`D355`, see §F).
> `SPY` itself: **+0.320% (1 session) · −0.201% (5) · +3.381% (20).**
> 🚫 **No flow column appears in this table.** Today's SWEEP has not run; the last `eqflow` is the
> 08-21 snapshot and is 4 days old on top of 42-day-old caps. **ROTATION reads flow from its own
> stage, not from here.**

| GICS sector | Wind | Driving prop. | exc1 | exc5 (mean / med) | neg5/n | exc20 (mean / med) | One line |
|---|---|---|---:|---:|---:|---:|---|
| **Materials** | **N+** ⚠ | ★ **`P102`** | +0.313 | **+3.740 / +1.941** | **2/12** | −0.686 / **−8.211** | 🚨 **Board's best 5-session and it is TWO NAMES**: `FCX` +20.69 · `NEM` +16.72; the other ten carry `exc20` median **−8.211** with 9/12 negative. **Mean 1.9× median.** Copper COT **100th %ile, 4th run.** ⇒ **`P102` brackets it. The `N+` is carried but is explicitly a two-name call, not a sector call** (`W5`) |
| **Health Care** | **OW** | `P98` | +0.167 | **+2.837 / +3.055** | 6/32 | **+0.986 / +0.774** | ★ **The only sector positive on BOTH windows with median ≥ mean.** 🚫 Ranked on **price and `eqflow` only** — `LLY` owns the `wflow` sign (G3). ★★ **The 08-25 payer overhang has largely CLOSED**: Distributors `exc5` **+3.25 at 100% participation** (`exc1 +2.11`, the sector's best) and Managed Care **+1.15 at 100%**, against the 08-25 reading of *"participation 11.1%, all five 🔴 sit there."* **The weak node is now Health Care EQUIPMENT (+0.19, 37.5%)** — a different node from the one the desk has been carrying (`M945`) |
| **Communication Services** | **N** | `P97` | +0.183 | **+2.558 / +3.636** | 2/13 | +1.611 / +0.741 | Median > mean and 11/13 positive. ⚠ **`D297`, 7th run**: `GOOGL` + `GOOG` ≈ 76.6% of a 13-name bucket while `top1_flips_sign` prints **false** — **no `wflow` claim is made on this sector at any cut.** 🚨 **And its `exc20` sample is n=12, not 13 — see `M937`** |
| **Consumer Discretionary** | **N** | `P93` | −0.372 | +2.348 / **+0.715** | **9/28** | −1.360 / −3.966 | ⚠ **Mean 3.3× median with 9/28 negative** — a top-heavy bounce, not breadth. `AMZN` is why the equal-weight cut is the one used. `exc20` is negative on both statistics with **18/28 negative** |
| **Financials** | **N** | `P97` | −0.096 | +1.842 / **+0.542** | **20/47** | −2.068 / −2.210 | ⚠ **Mean 3.4× median and 20/47 negative** — the mean/median agreement the 08-25 run recorded as "CLOSED" has **RE-OPENED** on the new bar (`M946`). `exc20` negative with 31/47 negative. Credit axis says **no stress** (HY OAS 9th %ile) — so this is positioning, not fundamentals |
| **Consumer Staples** | **N** | `P98` | **−1.233** | +1.817 / **+2.387** | **2/19** | **−6.739 / −4.891** | 🚨 **Board's WORST single session (−1.233) — the defensive bid unwound in one close.** `exc5` fell **+5.048 → +1.817** in that session. **17 of 19 negative on twenty sessions.** ✅ **The G3 restriction on this sector is LIFTED this run** (the flipper moved to HLTH) — it is normally rankable, and on price it is a one-week bounce inside a bad month |
| **Real Estate** | **N−** | `P97` | −0.142 | +1.064 / **+1.881** | 4/12 | −4.608 / −5.058 | Median 1.8× mean — better than its aggregate, as on 08-25. 🚨 **`P78`'s pre-settle range 4.889pp is ABOVE branch A**, and `XLRE` (+1.836) is 3.2pp from `XLU` (−1.412) ⇒ **the "duration complex" is dispersing, and this sector's underweight can no longer inherit `XLU`'s evidence** |
| **Utilities** | **UW−** | `P97` | −0.034 | **−1.428 / −2.080** | **13/15** | **−7.923 / −9.300** | **Board's worst 20-session excess with 14/15 negative.** ⚠ **Unlike 08-25 it no longer has a single-session bounce to disclaim** (`exc1 −0.034` ≈ flat) — the read is now internally consistent across all three windows. Weakest sector on the board |
| **Information Technology** | **UW** | ★★★ **`P101` · `P98` · `P90`** | **+0.884** | **−1.449 / −1.757** | **36/56** | **+4.230 / +3.147** | ★★★ **Board's BEST single session, and the bounce is hardware-specific** (Comms Equip +2.48 · Elec Equip +2.73 · Elec Components +2.27 · Tech Hardware +1.70 · Semis +1.11 vs Systems Software −1.27). `exc5` improved −4.761 → −1.449, breadth 43/56 → 36/56. 🚫 **NOT called a turn** — `exc5` still negative, and the **software−hardware gap survives at 10.36pp** (App Software +4.75 @ 91.7% participation vs Tech Hardware −5.61 @ 16.7%). **`AI capex` 0.66× · `memory prices` 0.80× · `HBM` 0.88× — the narrative is decelerating on all three readable terms.** ⚠ **The UW is a CONSENSUS position as of 08-24/25** (5 outlets, `HANDOVER §1b`) |
| **Industrials** | **UW−** | ★ **`P93` · `S123`** | −0.823 | **−2.220 / −1.949** | **36/50** | **−5.183 / −6.401** | ★ **The run's live transmission channel, and it is the only sector negative on all three windows with 40/50 negative on twenty.** Mechanism is dated and `[news]`-grade: **the Canada thread built 21 → 29 outlets and inverted from "deal" to "retaliation" in six days**, tariffs **effective 09-08**. ⚠ **`P93` settles 08-28, ELEVEN DAYS BEFORE the effective date** (`D342`) — which is exactly why `S123` (09-12) exists |
| **Energy** | **OW** ⚠ | ★★ **`P100` · `P96` · `S119`** | **−1.991** | **−2.763 / −2.707** | **14/16** | **+4.428 / +3.211** | 🚨 **Board's WORST single session and worst `exc5`, with 14/16 negative and 0% refining participation** — while **`exc20 +4.428` is the board's second best with only 3/16 negative.** ★ **The registered kill FIRED on settled bars** (2 consecutive negative crack rates) on a **36.1% base rate**. **`M879` replicates a 5th time on exc20**: refining **+11.60** > E&P **+5.42** > midstream **−0.35**. ⇒ **The `OW` is carried on the 20-day evidence and is now explicitly bracketed both ways by `P100`** rather than defended |

### ★ Matrix-level notes, all measured this run

1. **The monotone defensive→cyclical→AI ordering the 08-25 run found has BROKEN.** Rank by `exc5`
   today and the order is **Materials → Health Care → Comm Svcs → Cons Disc → Financials → Staples →
   Real Estate → Utilities → IT → Industrials → Energy.** **Staples has fallen to 6th from 1st and
   Energy to 11th from 7th, while IT rose off the bottom.** ⇒ **the "one axis, not eleven" framing was
   a one-session property, not a regime.** Written down rather than carried (`D48`).
2. **Mean-vs-median divergence is the run's most common shape and it points one way**: Cons Disc
   (3.3×), Financials (3.4×), Materials (1.9×) all have **mean ≫ median** ⇒ **top-heavy bounces**.
   Health Care, Comm Svcs, Staples and Real Estate have **median ≥ mean** ⇒ broad. **The four broad
   sectors are the four the desk is underweight or neutral in.** Stated as an observation, not a call.
3. **No sector verdict this run rests on a `wflow` number, a news-velocity number, or a 🟢/🟡/🔴 tag.**
   Every line above is price + participation, plus `[FRED]`, `[COT]`, `[FINRA]` and `[news]` where named.
4. **Two sector verdicts changed and both are downgrades of CONFIDENCE, not of direction**: Staples
   `N+ → N` (its 5-session lead more than halved in one close and it is 17/19 negative on twenty), and
   Materials keeps `N+` **only as an explicitly two-name call**. ⚠ **Both are `n=1`-session changes
   (`S5`)** and are flagged as such for ROTATION rather than presented as settled.
5. **`IT` is held at `UW` and NOT moved on the bounce.** One session of hardware mean-reversion inside
   a still-negative five is not evidence, and §5 of `HANDOVER` records that **`rs60` h=5 is this
   desk's most strongly negative IC cell (`t(NW) −5.46`, Bonferroni-passing)** — so a promotion on
   relative strength would be the *unsupported* direction. ⚠ **And the UW is now a consensus position**,
   which is recorded on the against-us side.

---

## §F · Instrument observations — dig candidates for `RESEARCH.md` Part C

> **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `M935`–`M946` and `D362`–`D365` → **0 hits outside this run's own files.**
> 🚨 **`M927`–`M934` were ALREADY TAKEN** by this morning's `industry_kr` run — **the `D76` collision
> class fired and was PREVENTED by this grep, for the 3rd time in 3 days.**

### 🚨 What this stage asserted and then refuted, in itself (`D48`)

1. **This stage's first price frame was built on the 2026-08-26 bar and every sector number in it was
   wrong.** The frame reported **Energy `exc5` −2.412 / IT `exc5` +0.217 / Staples +1.358**. On the
   settled 08-25 close the same computation gives **−2.763 / −1.449 / +1.817**. The draft is left on
   the record; the frame was rebuilt with the 08-26 bar dropped. **The differing variable was measured,
   not assumed** (see `D355` below).
2. **This stage drafted the crack-kill status from the inherited sentence *"1 of 2, one session from
   firing"* and the next command refuted it.** On settled bars the counter is **2 of 2 — the kill has
   already fired** (08-24 −2.862, 08-25 −1.675). **The inherited sentence was one session old and this
   run nearly carried it forward**, which is precisely `D358-KR`'s failure mode on a non-PREFLIGHT object.
3. **This stage drafted `P96` as "inside branch A" from the same inherited number.** `P96`'s branch A
   is ≤ **−2.887** and the current settled rate is **−1.675 ⇒ inside C.** ★ **The kill counter fired
   while the bracket did not.** They are different instruments with different thresholds and this
   report keeps them apart rather than letting the louder one speak for both.

### New digs

| # | Finding | Positive-form remedy |
|---|---|---|
| **`D362`** | 🚨 **A bucket term can DECELERATE while its own event ACCELERATES, and the desk reads the term.** Measured today: **`Canada tariff` accel fell 10.99× → 5.10× (base 94)** on the same day its `thread` built **21 → 29 outlets / 80 articles** and became the day's #1 head cluster. `D345` logged this class on a *falling* event; **this is the first measurement on a RISING one**, which is strictly more dangerous because a decelerating term **reads as calm** on a sector this desk is underweight | **Every bucket term is validated against its own `thread` outlet curve once per run, and a term whose accel moves OPPOSITE to its thread is flagged and widened on the spot.** Seeded this run: `Section 338`, `retaliatory tariffs`. Cost ≈ one `thread` cross-reference the stage already runs |
| **`D363`** | ⚠ **`D340`'s base band gates WIDTH but not PRECISION, and a term can be in-band for the wrong reason.** `Rubin` returns **base 1,374 — comfortably inside the ~60–2,000 band** — while the object the desk means (`NVDA`'s Rubin platform) measured **8 articles / 5 outlets** in the same 24 hours. The band admitted it; the token matches the Vera Rubin Observatory and personal names. **A band that only checks count will license a homonym** | **Any term entering the living table carries a one-time precision check (body-read `n=3` at entry) and its market-relevance %, exactly as `burst` already prints.** A term that fails the check is registered with its disambiguating phrase (`Rubin platform`, `Rubin NVL72`), never the bare token |
| **`D364`** | 🚨🚨 **A `burst` z computed on a PARTIAL-DAY denominator is systematically overstated, and this desk runs pre-market every day.** Measured: `RUBIN` read **z 8.4 on 08-25** (denominator **2,102**, run at 09:1x ET) and reads **z 3.3 today** (denominator **4,973**, complete day) on the **identical 8 articles / 5 outlets / 75% market relevance**. **A 61% fall in the statistic with zero change in the data.** `D354` was built on the 8.4. ⇒ **the observation survives; the number is withdrawn as an artifact** | **`burst` prints its denominator as a % of that weekday's trailing-4-week median and REFUSES to emit z below ~60%**, or emits it explicitly labelled `PARTIAL-DAY`. Sibling of `D355` — same root cause (the desk runs before the day is finished, and its instruments do not know that) |
| **`D365`** | ⚠ **A bracket anchored on an event DATE must verify that date from a primary source at registration.** `S108` froze its window around *"Warsh's Jackson Hole **D-0, 2026-08-21**"*; **`R93` (08-22) established the speech is 08-27~29** ⇒ **the window contained no event.** This desk ruled **NO VOID** (letter of the clause, `D242`, and consistency with the `S102` ruling 24 hours earlier) and re-labelled the row `LOW-INFORMATION-BY-CONSTRUCTION`. **It is the SECOND row in four days litigated at settle over what its clause meant** (`S102` → `D356`) | **`PREMORTEM` prints the event date AND the source it was taken from beside every frozen window, and the `D93` baseline table gains an `event_in_window` boolean.** A row whose boolean is false is scored but tagged non-informative automatically, rather than by argument after the fact. Cost ≈ one line per registration |

### Reproduced this run without new numbers (counts incremented, no new dig)

- **`D355` — 2nd run, and WORSE.** The 08-26 bar carries **median 2.48% of the prior session's volume**
  (mean 3.73%, p90 6.75%, max 47.77%, **0 of 299 names above 50%**) vs 08-25's 3.18%/4.08%/7.44%.
  ⇒ **the whole matrix in §E was rebuilt on settled bars with this bar dropped**, which is the remedy
  `D355` asked for, applied by hand one run after registration.
- **`D333` — 8th reproduction.** `DGS*`/`DFII10` end 08-24 · `T10YIE` 08-25 · `DTWEXBGS` 08-21 ·
  `NFCI` 08-21. Last joint rate date **08-24**. **`P77` cannot be read before 08-27 at the earliest.**
- **`D339` — worse again**: single-outlet layer **607 of 622 unseen = 97.6%** (08-25: 96.25%), still a
  random 15 because the classifier is Korean-only.
- **`D340` — paid in both directions again**: it kept `Strait of Hormuz` (8,224) out as a label-only
  row while licensing `AI capex` (1,189), `HBM` (1,336) and `memory prices` (970) — **the three rows
  that carry this report's most load-bearing narrative reading.** And **`D363` above is the first case
  where the band admitted a term it should have excluded.**
- **`D327` — 5th run**: the S&P 500 COT row prints **🟢 crowded-long on a net spec of −10,560** (net
  SHORT) while carrying the board's largest weekly swing (−21,840). **Label unused; number used.**
- **`D297` — 7th run**: `GOOGL`+`GOOG` ≈ 76.6% of a 13-name Comm Svcs bucket with
  `top1_flips_sign: false`. **No `wflow` claim made on COMM at any cut.**
- **`D352` — the base rate was re-measured, not inherited**: **36.1%** today vs 35.5% on 08-25. **The
  two agree**, and the condition fired this run, so the disclosure is now load-bearing rather than
  precautionary. **`P100` carries it in its own registration table.**
- **`D341`** — `OKLO` (today's head layer, *"SpaceX's power needs will make it Oklo's biggest
  customer"*, 14 art / 7 outlets), `LYB`, `DOW`, `FRO`, `X`, `AA` remain **outside `us_top300`**.
  **`S109` is armed on `FRO`, which prints 08-28 and which this desk cannot flow-tag.**
- **`D343` — 08-28 now carries NINE rows.** All three registrations this run deliberately avoided it
  (`P100` → 09-01, `P101` → 09-04, `P102` → 09-09), each naming its non-redundancy.
- **`D294`** — `action_bracket` is ALPHA's stage, not this one; the count will be taken there.
- **`D76` — the collision class fired and was PREVENTED for a 3rd time in 3 days** (`M927`–`M934`
  already held by this morning's `industry_kr` run). Caught by the write-time 3-grep, not by a reader.

### New measured rows registered this run — `M935` – `M946`

| id | Fact | Tag |
|---|---|---|
| **`M935`** | **The "hardware de-rate, not one trade" finding replicates on a second frame.** Settled 08-25, `us_top300`, excess vs `SPY`: Application Software `exc5` **+4.75 at 91.7% participation** · IT Consulting +4.58 at 100% vs Tech Hardware/Storage **−5.61 at 16.7%** · Semicap **−5.54 at 0%** · EMS **−5.09 at 0%** · Electronic Components **−4.61 at 0%** · Semis −2.48 at 14.3%. **Software−hardware gap 10.36pp** (was 14.21pp on the 08-24 frame) | `[measured]` |
| **`M936`** | **The registered refiner kill FIRED on settled bars.** 5-session 3-2-1 crack rate: **−2.862 (08-24) then −1.675 (08-25) = two consecutive negatives.** Crack levels 66.320 → 68.134. ⚠ **Unconditional base rate of two consecutive negatives, trailing 252: 36.1%** | `[measured]` |
| **`M937`** | 🚨 **The 42-day-old universe has a PRICED casualty, and it silently shrank a sector sample.** `EA` (Electronic Arts, rank 235, **$50.69B**, Communication Services) has **6 price observations in a 90-day frame, last bar 2026-08-10** — it has stopped trading. Consequence: **Comm Svcs `exc20` was computed on n=12, not n=13** (7.7% of the sector's names) **with no warning emitted anywhere.** G5's staleness leg is no longer abstract | `[measured]` |
| **`M938`** | **The rate move inverted its own composition over the week, on the joint 08-24 frame.** 08-17 → 08-24: `DGS10` **−2bp** · `DGS2` **+5bp** · 2s10s **+53 → +46bp** · real 10y **−6bp** · breakeven **+4bp.** ⇒ **a flattening whose 10y composition rotated from real to inflation** — the reverse of `P97`'s registration reading (08-21: real +5bp, breakeven falling). ⚠ 4–6bp on a 137-obs pull ⇒ composition note, not a regime call (`C4`) | `[measured]` |
| **`M939`** | **The AI-compute short book is splitting, not moving as a bloc.** FINRA Reg SHO, dated 08-25: `ANET` **z +2.06 / 5v5 +6.7▲** · `NVDA` **+1.78 / +2.4▲** vs `AVGO` **−2.17 / −10.4▼** · `HPE` **−1.73 / −13.2▼**. **Spread 4.23 z-units inside one complex on one day**; all four are book holdings and all four are inside the universe (G5 coverage leg) | `[measured]` B-grade |
| **`M940`** | **`M926`'s futures stub bar has RESOLVED and the resolution agrees with the outlets.** `BZ=F` 08-25 now reads **volume 18,474, close 88.58**, against the KR desk's same-morning read of a **137-contract, $0.34-range stub implying −6.81%**. **92.17 × (1 − 0.0389) = 88.58**, matching four outlets' *"Brent −3.89% / below $90"*. ⚠ **The volume field is still defective**: `BZ=F` 08-24 and 08-25 both read 18,474 and `CL=F` both read 219,422 — **a duplicated field on two consecutive days.** ⇒ **price leg trustworthy, volume leg not** | `[measured]` |
| **`M941`** | **A deal narrative inverted into a retaliation narrative inside six days and ended at its widest outlet count.** `thread --date 2026-08-25 --days 7`: **23 → 9 → 11 → 24 → 20 → 21 → 29 outlets, 370 articles, BUILDING.** Titles in order: *"Trump PAUSES tariffs on Canada after last-minute deal"* (08-19, 23 outlets) → *"US set to CUT tariffs on Canada metals, autos"* → *"inch closer to trade deal"* → *"Canada announces RETALIATORY tariffs"* (08-22, 24) → *"Canada set to announce retaliatory tariffs"* (08-25, 29). **Effective date 2026-09-08** | `[measured]` curve · `[news]` content |
| **`M942`** | **The AI narrative is decelerating on three independent in-band terms into the epicenter's own print.** `theme-age --scope foreign`: **`AI capex` 0.66× (base 1,189, 2nd consecutive run below 1.0)** · **`memory prices` 0.80× (970)** · **`HBM` 0.88× (1,336)**. All three inside `D340`'s readable band on both sides | `[measured]` |
| **`M943`** | 🚨 **A `burst` z fell 61% with zero change in the underlying data, and the differing variable is the denominator.** `RUBIN`: **z 8.4 (08-25, denominator 2,102, partial day) → z 3.3 (today, denominator 4,973, complete day)** on the **identical 8 articles / 5 outlets / 75% market relevance.** `D354` was built on the 8.4 | `[measured]` |
| **`M944`** | **Two consecutive percentile-extreme readings this desk called load-bearing were substantially erased by the next single close.** `EW{STPL+HLTH} − EW{IT}` 5-session: **+9.336 = 97.6th %ile (08-24) → +3.905 = 85.7th %ile (08-25) = −5.43pp, 58% of the distance to the p50 median.** `P79`: **−10.852 (08-24) → −2.977 (08-25) = +7.9pp**, scored `FIRED-C`. ⇒ **at a 5-session sd of ~4.7pp the estimator sheds ~20% of its content per day; a p97 reading has a one-day half-life** | `[measured]` |
| **`M945`** | **Health Care's payer/distributor overhang has largely closed on price, and the weak node moved.** Settled 08-25, excess vs `SPY`, participation in parentheses: Life Sciences Tools **+5.80 (100%)** · Pharma **+5.16 (100%)** · Facilities +4.34 (100%) · Biotech +4.02 (100%) · **Distributors +3.25 (100%), `exc1` +2.11 = the sector's best single session** · **Managed Care +1.15 (100%)** vs **Health Care Equipment +0.19 (37.5%)** and Services −0.71 (50%). ⇒ against the 08-25 reading of *"payers/distributors/services participation 11.1%, all five sector 🔴 there"* | `[measured]` |
| **`M946`** | **The Financials mean/median sign agreement the 08-25 run recorded as CLOSED has RE-OPENED.** Settled 08-25: `exc5` **mean +1.842 vs median +0.542 = 3.4×**, with **20 of 47 negative**; `exc20` mean −2.068 / median −2.210 with **31 of 47 negative**. Same shape in Cons Disc (mean 3.3× median, 9/28 neg) and Materials (1.9×) ⇒ **three of the four "positive" cyclical sectors are top-heavy bounces** | `[measured]` |

---

## §5 · Post-run ADDENDUM (append-only — L1·DRIFT writes here at stage 11)

*(nothing yet — DRIFT has not run)*

### ADDENDUM — appended 2026-08-26 by L1·DRIFT (append-only; nothing above this line was rewritten)

**Run clock**: report completed **22:46 KST**, DRIFT at **23:2x KST = 10:2x ET** ⇒ **+0.7h**.
⚠⚠ **DECLARED DEVIATION, 8th consecutive run**: the protocol asks for **+3–6h**. Anything breaking
2–5 hours out is **outside this run**, and this file says so rather than implying a full window.

#### `drift_watch` — **✅ no kill-switch burst.** Zero terms spiked above baseline in the window.

#### Anti-signal sweep — every VOID clause registered today, checked, and **none fired**

| Clause | Probe (`--days 1 --scope foreign`) | Verdict |
|---|---:|---|
| `P100` — OPEC+ emergency production decision | `"OPEC emergency"` **0** | not fired |
| `P100` — **US SPR action** | `"strategic petroleum reserve"` **10** | 🚨 **body-read, and it does NOT fire — see below** |
| `P102` — tariff action naming copper or gold | `"copper tariff"` **0** | not fired |
| `P102` — acquisition of `FCX` or `NEM` | `"Freeport acquisition"` **0** · `"Newmont acquisition"` **0** | not fired |
| `S127` — acquisition of or by `AVGO` | `"Broadcom acquisition"` **0** | not fired |
| `P101` · `S128` — GICS reclassification | `"GICS reclassification"` **0** | not fired |

★ **The SPR hits were body-read rather than counted, and the distinction is the whole point.**
The ten articles are **commentary on the SPR's LEVEL, not a policy ACTION**: *"Oil stocks in US
Strategic Petroleum Reserve fall by 3.7 million barrels to **the lowest level since 1982**"* [reuters,
08-24] · *"America's Strategic Petroleum Reserve Is **Running on Fumes**"* [yahoo_finance] ·
*"**Less than 300 million barrels left**: the engineering limits threatening the American SPR"*
[fortune]. **`P100`'s clause says "a US SPR action" — a release or purchase decision. Reporting on
depletion is not one. THE CLAUSE DOES NOT FIRE.**
⚠ **But the content is materially relevant and is recorded rather than discarded**: a depleted SPR
**removes the policy tool that has historically capped an oil spike**, which is a structural
asymmetry on the Energy `OW`'s upside tail that no row on this board currently owns (`M957`).

#### 🚨🚨 What this stage found is a defect in THIS REPORT'S OWN §A-6, and it is written here, not edited above

**`MACRO_REPORT §A-6` printed a LIVE 08-26 crack of 57.824 with a 5-session rate of −9.821 = the 2.0th
percentile**, labelled *"not a settle"*. **That label was not strong enough. The number is probably
not even a price move.**

| Bar | `RB=F` | `HO=F` | `CL=F` |
|---|---:|---:|---:|
| 2026-08-21 | 3.3479 | 4.4948 | 87.06 |
| 2026-08-24 | 3.2708 | 4.2677 | 85.01 |
| 2026-08-25 | 3.2529 | 4.2438 | 82.36 |
| **2026-08-26 (live)** | **2.9495** | 4.1170 | 81.56 |
| **one-session change** | **−9.34% (a 30.3-cent gap)** | **−3.0%** | **−1.0%** |

**Decomposing the crack's fall: the `RB=F` leg alone contributes `2 × (3.2529 − 2.9495) × 42 ÷ 3 =
8.49` of the ~9.5-point drop — ≈ 89% of it.** A **30-cent single-session gap in RBOB** while the other
two legs move 1–3% is the signature of a **September → October RBOB contract roll** (the summer→winter
RVP spec discontinuity), not of a market repricing.
⚠ **And the same volume defect fires again**: `RB=F` reads **29,842 on BOTH 08-24 and 08-25** — the
identical duplicated-field pattern `M926` found on `BZ=F`/`CL=F` and `M940` confirmed today.
⇒ 🚫 **The live crack figure is NOT read, and `MACRO_REPORT §A-6`'s "LIVE, partial" row is downgraded
from "not a settle" to "probably a roll artifact."** Registered as **`M958`** and as dig **`D368`**.
✅ **What survives untouched**: the **settled** crack series (**−2.862 on 08-24, −1.675 on 08-25**),
which is what `M936`, `P96` and the kill-counter finding actually rest on. **The kill still fired.**

#### Live tape check at +0.7h — reported as UNSETTLED, and it points against two of this run's readings

| Object | Settled 08-25 | **Live 08-26 (10:2x ET)** | Reads against |
|---|---:|---:|---|
| `MPC` · `PSX` · `VLO` | — | **+0.93% · +1.18% · +0.59%** | ★ **the refiners are UP while their own crack prints down** — directly the question `P100` (09-01) exists to settle |
| `NVDA` · `AVGO` · `MRVL` | — | −1.27% · **−1.63%** · −0.56% | the AI complex is being sold **into** the D-0 print |
| `COIN` · `MSTR` · `HOOD` | — | **−2.15% · −2.52% · −1.96%** | ⚠ the three worst live moves of the names tracked — **directionally consistent with `BET §A`'s denominator finding on `COIN`/`MSTR`, but `n=1` and NOT read as confirmation** |
| `MRK` | — | −1.45% | the sector's only 🟢 giving back |
| **`P78`'s four legs** | `XLV +3.476` (best) … `XLU −1.412` (worst) | 🚨 **INVERTED: `XLU +0.857` (best) … `XLV −0.252` (worst)**, live 1-session range only **1.11pp** | **the leg ordering flipped intraday on the very day `P78` settles.** ⚠ `P78`'s observable is the **5-session** range, so the pre-settle **4.889pp** is what carries — but a one-day inversion moves it, and the row settles tonight |

#### One source disagreement, recorded and NOT resolved
`toi` 08-25: *"Brent crude **stays above $90** as Middle East standoff intensifies"* against this run's
own settle of **88.58** (which matches `yonhap`'s *"−3.89% / below $90"* to the cent) and `fxstreet`'s
*"WTI slides below $84.00"*. ⇒ **the `toi` headline is contradicted by the settle.** It may be
intraday-stamped; **no attempt is made to reconcile it here**, and the settle is the citable number.

#### What this ADDENDUM changes and does not change
- ✅ **No proposition is retracted.** `P96` `P97` `P98` `P100` `P101` `P102` and `S127` `S128` all stand
  as registered; **no threshold is moved** (`D242`).
- 🚫 **One number is withdrawn**: the live 08-26 crack (`57.824` / rate `−9.821`) is withdrawn as a
  probable roll artifact. **The settled series it was printed beside is unaffected.**
- ⚠ **`D294` (8th)** and **`D355` (2nd)** and **`D353` (reproduced on `AVGO`)** are all already logged
  in `§F` / `BLINDSPOT_PREMORTEM`; nothing new is added for them here.
- ⚠ **The window is +0.7h, not +3–6h.** A burst 2–5 hours out is outside this run, and **tonight's
  `NVDA` print — the run's D-0 binary — falls entirely outside it by construction.**
