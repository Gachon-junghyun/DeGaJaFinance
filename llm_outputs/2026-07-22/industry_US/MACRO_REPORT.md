# MACRO_REPORT — industry_US — 2026-07-22

> Stage 1/10 (MACRO) of protocol `industry_us`. English-pure runtime, `--market us`, news `--scope foreign`.
> Purpose: falsifiable macro propositions → **★sector transmission matrix** (ROTATION's input).
> Zero buy/sell. Primaries `[FRED]` > narrative `[news]`. Data asof stamped per line.
> Run clock: **2026-07-22 19:2x KST = 06:2x ET** — the US regular session has **not opened**.
> Continuity anchor: `llm_outputs/2026-07-21/US_2/MACRO_REPORT.md` + `HANDOVER.md` (this run, stage 0).

---

## §A · Regime primaries `[FRED]`

| Series | Latest | Δ vs prev obs | Δ vs ~20 obs ago | Read | Freshness |
|---|---|---|---|---|---|
| Fed Funds eff (DFF) | **3.63%** | flat | flat | Policy on hold | daily, asof **07-20** |
| 10y Treasury (DGS10) | **4.60%** | +5bp | **+14bp** (4.46) | Long end pushing to the top of the 120d range [3.97, 4.67] | daily, asof 07-20 |
| 2y Treasury (DGS2) | **4.21%** | +3bp | +2bp | Front end anchored — the move is at the long end | daily, asof 07-20 |
| **2s10s** (derived) | **+0.39** | +2bp | +12bp | **Bear-steepening** — term premium, not cut-pricing | derived |
| **Real 10y (DFII10)** | **2.35%** | **+4bp** | **+14bp** (2.21) | ★ **120-day HIGH** (window max 2.36). See the wedge below. | daily, asof 07-20 |
| **10y breakeven (T10YIE)** | **2.26%** | +1bp | **+3bp** (2.23) | Inflation expectations barely moved | daily, asof **07-21** |
| Core CPI (CPILFESL) | **YoY +2.57%** · **MoM −0.02%** | — | — | Both halves quoted (C2). Core flat sequentially | **monthly, asof Jun — 1-month lag** |
| Headline CPI (CPIAUCSL) | **YoY +3.46%** · **MoM −0.42%** | — | — | Both halves quoted (C2). Sharp sequential cool, energy-led | **monthly, asof Jun — 1-month lag** |
| Unemployment (UNRATE) | **4.2%** | −0.1 MoM | +0.1 vs Jun-25 | Loosening slowly, not cracking | monthly, asof Jun |
| DXY Broad (DTWEXBGS) | **120.53** | +0.20 | +1.14 | Near the top of the 120d range [117.44, 121.41] | daily, asof **07-17 (3 sessions stale)** |
| VIX (VIXCLS) | **18.65** | −0.12 | +1.37 | Moderate. **Far from the >24 anti-signal** | daily, asof 07-20 |
| **HY OAS (BAMLH0A0HYM2)** | **2.69%** | **−4bp** | +4bp | **6bp off the 365d low (2.63)**. No credit stress. | daily, asof 07-20 |
| **IG OAS (BAMLC0A0CM)** | **0.78%** | −1bp | +4bp | Same read at investment grade | daily, asof 07-20 |
| **NFCI (Chicago Fed)** | **−0.538** | −0.014 | −0.016 | **Loosening again** — 3 straight weekly declines (−0.510 → −0.524 → −0.538) | weekly, asof **07-10** |
| M2 (M2SL) | **$23.05T** | +1.09% MoM | +5.1% YoY | Liquidity re-expanding; both halves quoted (C2) | monthly, asof May |

⚠ **Freshness caveat (P4)**: FRED's daily series stop at **07-20** for most tapes (breakeven has 07-21).
Nothing here reflects the 07-21 US session or today's pre-open. DXY is 3 sessions stale.

### ★ The regime read of this run — the wedge is now measurable, not narrative

Yesterday's report called the wedge "headline disinflation vs rising real yields". Today the
**decomposition is explicit**: the 10y rose **+14bp** over ~20 sessions while the 10y **breakeven rose
only +3bp**. **~79% of the nominal move is real rate, not inflation expectation.** That is a
*discount-rate* event, not an *inflation* event, and it happened while:

- **Credit refused to confirm any stress** — HY OAS **2.69%** (−4bp on the day, 6bp off its 365-day
  low), IG **0.78%**, NFCI **−0.538 and loosening for 3 straight weeks**.
- **VIX 18.65**, nowhere near the 24 kill line.

**Rising real rates + tightening-free credit + loose financial conditions = growth/term-premium
repricing, not risk-off.** The consequence for leadership is the same as yesterday but sharper:
**this regime pays earnings-now and taxes duration-of-growth-later.** Bond proxies (Utilities, REITs,
Staples) carry a direct headwind; long-duration multiple expansion has a ceiling that is *still rising*.

⚠ **The kill line is closer than yesterday.** The prior run's P1/P3 anti-signal is `real 10y > 2.55%`.
It was **2.31% (asof 07-17)** and is now **2.35% (asof 07-20)** — **20bp of room**, at a 120-day high,
with the FOMC on 07-28~29. This is the single number to watch in this run.

---

## §B · Positioning `[COT, CFTC]` — ⚠ **the same weekly print as yesterday, zero new information**

| Instrument | Net-spec | Wk Δ | 1yr %ile | Signal |
|---|---|---|---|---|
| Nasdaq-100 | −10,313 | −1,572 | **4%ile** | 🔴 Crowded-SHORT → rebound ammo for mega-cap tech |
| S&P500 e-mini | −38,938 | +3,953 | 78%ile | 🟡 neutral |
| Russell 2000 | +103 | +990 | 67%ile | 🟡 neutral |
| UST 10Y | −831,675 | −17,413 | 22%ile | 🟡 spec short, light percentile |
| UST 2Y | −1,157,477 | +103,531 | 52%ile | 🟡 neutral |
| USD Index | +13,173 | −96 | 58%ile | 🟡 neutral |
| WTI Crude | +19,783 | −1,139 | **10%ile** | 🔴 Crowded-SHORT → rebound ammo |
| Nat Gas | −178,612 | −13,305 | **6%ile** | 🔴 Crowded-SHORT → rebound ammo |
| Gold | +186,682 | −7,564 | 23%ile | 🟡 long, not extended |
| **Copper** | +64,385 | +113 | **95%ile** | 🟢 Crowded-LONG → unwind risk |
| Silver | +25,074 | −2,941 | 40%ile | 🟡 neutral |

⚠ **P4 disclosure:** every figure above is **byte-identical to the 2026-07-21 report**. COT is
Tuesday-close, Friday-released — this is the *same* print, not a fresh confirmation. Treating it as
corroboration of a second day's tape would be double-counting one observation (rule **S1**: the
effective sample here is **one weekly date**, not two daily reads). Next new print: Friday 07-24.

⚠ **Rejected-ledger guard**: COT extremes are on the **REJECTED** list as a *contrarian trigger*
(`handoff/RESEARCH.md` D6). They are used below only as **ammunition/cushion context** attached to an
independent reason — never as the reason itself. US has **no** investor-type actuals (no KR/KIS
equivalent), so positioning is the whole flow axis here, which is exactly why it must not be promoted.

---

## §C · Narrative axis `[news, --scope foreign]` — event axis, trajectories, buckets, blind spot

**Denominator (measured, not asserted):** 07-22 foreign feed = **1,132 articles → 466 clusters → 206
events (206 market / 0 nonmarket)**; head 25 · body 181 · **tail 0** (`--body 2`, so nothing was
sampled away). 7-day pool **22,591 articles**; 30-day pool **55,091**.
⚠ **Body-blind rate 63.7%** on the 8-bucket term union (`coverage`: title+summary sees 3,120 of an
8,586 reachable union — recall **36.3%**, 🔴). Every "quiet" claim below is therefore withheld unless
the event denominator backs it.
⚠ **Today's day is incomplete** — 206 events vs 07-21's 924, because it is 06:2x ET. Per the unit's
own warning, **FADING tags dated 07-22 are mechanically inflated** and are read as such below.

### C-1 · The day's events (head, ≥5 outlets)

| Event | Coverage | Sector read |
|---|---|---|
| **Oil rises after US announces new round of strikes** | 11 art / **10 outlets** (#1 of the day) | Energy |
| **OpenAI: AI models autonomously hacked / escaped containment to hack Hugging Face** | 14/8 + 8/8 = **22 articles, 2 clusters** | IT / regulatory tail |
| **Pharma stocks bleed after Trump announces up to 200% tariff on [pharma]** | 11 / 7 | **Health Care — direct hit** |
| **Trump approves landmark civil-nuclear deal with Saudi Arabia** (body-confirmed: WSJ + Forbes, "with Saudi Arabia") | 7 / 7 | Utilities / Industrials (nuclear chain) |
| **EU bids to finalise new Russia sanctions** | 10 / 6 | Energy |
| **Analysis: AI investment boom puts Big Tech's free cash flow under pressure** | 8 / 5 | ★ **the S1 axis** |
| **Google Earnings Today: What to Expect as AI Spending Faces Scrutiny** | 6 / 5 | ★ **S1** |
| **Samsung in talks to invest in Mistral at €20B valuation** | 6 / 5 | IT |
| **Japan imports jump to record high on oil price surge** | 11 / 5 | Macro / FX |
| **UK headline CPI 2.6% in June** | 6 / 5 | Global rates |
| **House passes spending bill to head off government shutdown** | 6 / 6 | Macro tail removed |

### C-2 · Body tier, market-relevant (of 181 — the structural prints hide here)

- **WTI hits fresh six-week high $86.00 on supply concerns** [9/4] · **Brent back above US$92** [3/3] ·
  **US CENTCOM completes 11th night of strikes on Iran** [4/4] · **Iran's FM describes the attack that
  killed Khamenei** [3/3] · **Iran war has cost the US $37.5bn** [4/3] · **China's oil output hits a
  record high** [3/2] · **Equinor profit soars 93% on the oil & gas price spike** [4/3, REIGNITED].
- **BOJ said open to a faster rate-hike pace as the yen adds price risk** [9/4] · **yen at a 40-year
  low above 163** · **Japan ready for decisive currency action** [4/3] · **Japan's June trade deficit
  widens to ¥406.9B on a +25.4% import spike** [3/3].
- **AI Stock Rally Loses Steam Ahead of Key Big Tech Earnings** [4/4] · **Dow/S&P/Nasdaq futures slide
  with Alphabet and Tesla earnings on deck** [3/2] · **Tesla Q2: investors eye margins, AI roadmap** [3/2].
- **Micron, Western Digital and SanDisk just jumped 12–14%** [3/3] — the 07-21 memory session, recorded.
- **TSMC "100 billion reasons why the AI build-out will last several more [years]"** [4/3] ·
  **Nvidia supplier Wistron opens a $700M Texas site producing AI 'superchips'** [4/4] ·
  **Meta–Anthropic potential $10B compute lease** [4/3, REIGNITED] · **Why AMD stock jumped** [5/4].
- **SK Hynix dismisses the Intel Ohio buyout report: "no plans for an acquisition"** [3/2].
- **KeyCorp Q2 results** [**40 articles**/4 — the largest single body cluster of the day] ·
  **Santander**, **Danske**, **Bandhan Bank −15% on Q1** — bank prints are the day's earnings mass.
- **Cleveland Fed's Hammack "said the quiet part out loud about inflation"** [4/4] — hawkish-leaning Fed speak.
- **US targets China in a move to ban military-grade drone imports** [3/2] · **companies race to deliver
  autonomous uncrewed fighter jets** [3/3] — defense/industrial.
- **Anthropic to donate $20M to a US political group supporting AI regulation** [3/2].

### C-3 · Trajectories (`thread --days 7`) — what is building vs crowded

Per-day denominators: 07-16 **262** · 07-17 347 · 07-18 187 · 07-19 221 · 07-20 698 · 07-21 **924** ·
07-22 **206 (partial day)**. 2,845 daily events → 2,207 threads (360 multi-day, 77 alive).

| Thread | Curve | Tag | Read |
|---|---|---|---|
| **Slower-hyperscaler-capex positioning → "AI capex puts Big Tech FCF under pressure"** | 5→2→4→5→5 (5d) | **BUILDING** | ★ The bear case for tonight's print has had **5 days of runway** and is at a **flat, not accelerating**, outlet count. Not yet crowded, not new either. |
| **Big Tech earnings test / Alphabet Q2 preview** | 3→7→4→7 (4d) | **BUILDING** | The event is priced as an event. |
| **OpenAI containment breach / Hugging Face** | 4→8 (2d) | **BUILDING** | **Fastest accelerator on the board** (+100% outlets in one day) and brand new. Regulatory-tail candidate. |
| **Meta–Anthropic $10B compute lease** | 2→5→3 | REIGNITED | Demand-side capex datapoint, not supply. |
| **Nvidia (valuation debate)** | 2→5→3 | REIGNITED | Debate, not news. |
| **Equinor / Venture Global — energy windfall** | 3→3 | REIGNITED | Earnings confirmation of the oil move. |
| **Oil / US-Iran strike threads** | 5→12→5→6→17→18→**5** | FADING | ⚠ **Artifact.** The window ends on a 206-event partial day, and today's **#1 head event (10 outlets) is oil**, with WTI at a 6-week high and Brent >$92. **Do not read this FADING tag as attention leaving oil.** |
| **"Oil hits $90 as US-Iran war escalates" · "Iran strikes another tanker" · "Houthi maritime embargo"** | peaks 15 / 11 / 11 | **ENDED 07-21** | Attention rotated *within* the same story to a new thread, not away from it. |
| **Gold falls amid higher-for-longer rate expectations** | 3→3→4→3→3 | FADING | Independent corroboration of the real-rate read in §A. |
| **Euro-zone banks tighten credit standards** | 2→3→3→5→8→6 | FADING | ⚠ **Narrative-only** — see the credit guard below. |
| **Trump slaps more tariffs on Canada** | 9→24 (peak **24 outlets**) | ENDED 07-21 | The tariff wave's high-water mark this window. |

### C-4 · 7-bucket term sweep — normalized velocity (terms passed as separate argv)

Velocity = (7d hits / 30d hits) × 30/7, then divided by the **pool's own** ratio (22,591/55,091 ×
30/7 = **1.758**). >1.00 = the bucket is gaining share of the feed; ≈1.00 = moving with the pool.

| Bucket | Terms (separate argv) | 7d | 30d | Norm. velocity |
|---|---|---|---|---|
| **Credit** | credit · spreads · default · bankruptcy | 2,257 | 4,475 | **1.23 ★ fastest** |
| **Tariffs** | tariff · tariffs · trade war | 915 | 1,927 | **1.16** |
| **Energy** | Hormuz · OPEC · crude · Brent | 3,277 | 7,031 | **1.14** |
| **Defense/geo** | Iran · missile · defense | 3,062 | 6,782 | 1.10 |
| **AI capex** | capex · hyperscaler · datacenter | 2,001 | 4,494 | 1.09 |
| **Memory/semis** | DRAM · HBM · memory · semiconductor | 1,886 | 4,306 | 1.07 |
| **FX** | yen · BOJ · dollar | 2,820 | 6,895 | 1.00 |
| **Rates** | Treasury · yields · FOMC · Powell | 3,375 | 8,470 | **0.97 (slowest)** |

★ **The most useful line in this table is a disagreement.** Credit *talk* is the fastest-accelerating
bucket in the feed (1.23×) while the credit *market* sits 6bp off a 365-day low. **Per the measured
2026-07-21 failure, every credit-stress claim in this run is labelled `narrative-only` unless it cites
HY OAS or NFCI.** It does not, so it is.
⚠ C5 (arbitrary choice): "credit" is polysemous in an English feed (credit card, credit rating, tax
credit) — this bucket's absolute level is unreliable; only its *change* is used, and only as a flag.

★ **Second disagreement:** the **Rates** bucket is the *slowest* bucket in the feed (0.97) on the same
week the 10y real yield made a 120-day high. **Attention is not where the move is.** Under the desk's
own reasoning (a thread still at 2 outlets is where discovery lives, a 5th-day peak is crowded), the
under-covered axis is the rate axis, and the crowded axis is credit/tariff/oil.

### C-5 · Blind-spot pass (`blindspot --sample-pct 25 --days 7 --scope foreign`, sample 5,647 of 22,591)

Token-0 emergent terms read **raw**, not bucketed. Top of list is expected furniture (AI 2,062 ·
Earnings 1,282 · China 727 · Iran 646 · Trump 578). **Three rank-jumps that no fixed bucket queries:**

1. **SpaceX — 316 mentions**, above Nvidia (306) and Apple (258), with no US-listed-equity bucket
   containing it. Body rows: *"SpaceX is down 20%"*, *"down 36% from its post-IPO peak"*, *"sinks
   further below IPO price after Starship la[unch]"*, *"Musk says short sellers have a 'very low'
   survival probability"*. **This is a live sentiment gauge for the speculative-growth cohort** and it
   is bleeding while the memory cohort rips — a dispersion datapoint (W5), not a stock call.
2. **Japan — 253**, arriving through three separate doors (BOJ hike pace · yen 40-year low · record
   oil-driven import bill). The FX bucket scores a flat 1.00 because "yen/BOJ/dollar" splits the story.
3. **Bank — 334 / Fed — 325** in the same sample where the *Rates* bucket is the slowest. The bank
   earnings mass (KeyCorp's 40-article cluster, Santander, Danske) is being covered as *company* news,
   not as *rates* news — which is precisely why the rates bucket under-reads.

**New terms folded into the living table for the next run:** `SpaceX` · `BOJ` (promote out of the FX
bucket into its own global-duration line) · `Hammack` (Fed speakers by name) · `Saudi nuclear`.

---

## §D · Macro propositions (falsifiable · both branches · anti-signal · KPI · dated catalyst)

**P1 — The long-end repricing is REAL-rate, not inflation, and it is the ceiling on duration.**
- Anchor: 10y **4.60%** (+14bp/20 obs) vs breakeven **2.26%** (+3bp) → real 10y **2.35%**, a
  **120-day high**; 2s10s **+0.39** bear-steepening `[FRED, asof 07-20/21]`. Corroborated by an
  independent narrative thread (*"Gold falls amid higher-for-longer rate expectations"*, 5 days) `[news]`.
- Direction: **earnings-now over duration-of-growth-later**; bond proxies carry a direct headwind.
- **Both branches (mandatory — this is an oscillating variable):** (a) real 10y stalls ≤2.40% into the
  FOMC → the wedge is a term-premium blip and duration recovers; (b) real 10y breaks **>2.55%** → the
  duration de-rate is a regime call, not a tilt.
- **Anti-signal (kills P1):** real 10y falls back **<2.20%** *with* breakeven rising — that would make
  the move an inflation story after all, inverting the sector conclusion.
- KPI: **DFII10 daily** (the single most important number in this run) · T10YIE alongside it · 2s10s.
- Catalyst: **FOMC 2026-07-28~29** (dated) · Aug CPI.

**P2 — Credit is the loudest narrative and the quietest market; trade the market, not the narrative.**
- Anchor: HY OAS **2.69%** (−4bp d/d, 6bp off the 365d low), IG **0.78%**, NFCI **−0.538** loosening
  3 straight weeks `[FRED]` — against a credit term-bucket accelerating at **1.23× the pool** and a
  6-day *"euro-zone banks tighten credit standards"* thread `[news]`.
- Direction: **no risk-off discount** is warranted. Bank credit-cost fear is not priced by spreads.
- **Both branches:** (a) spreads stay <3.00% → the narrative is noise and financials/cyclicals keep
  the benefit of the doubt; (b) HY OAS widens **>3.10%** (its 120-day high is 3.46) → the narrative was
  early and the whole earnings-now tilt must be re-cut.
- **Anti-signal (kills P2):** HY OAS **>3.10%** on a close, or NFCI turning positive-ward two weeks running.
- KPI: HY OAS daily · NFCI weekly · bank credit-cost commentary in the Q2 calls now printing.
- Catalyst: **the S1 second-order test — if Alphabet cuts capex tonight, HY OAS the following session
  decides whether it is a regime event or a single-name repricing** (pre-registered, `handoff/SCENARIOS.md`).

**P3 — The AI-capex question is now a cash-flow question, and it resolves tonight — but only on the capex line.**
- Anchor: a **5-day BUILDING** thread moved from *"some investors position for slower hyperscaler
  capex"* to *"AI investment boom puts Big Tech's FCF under pressure"* (5→2→4→5→5 outlets) `[news]`;
  *"AI Stock Rally Loses Steam Ahead of Key Big Tech Earnings"*; futures slide into the print `[news]`.
  Counter-evidence in the same feed: **TSMC's build-out-lasts-years framing**, **Wistron's $700M Texas
  AI site**, **Meta–Anthropic $10B compute lease** `[news]`.
- Direction: **genuinely two-sided**; the desk holds a **frozen pre-commitment** from stage 0 —
  a move **inside GOOGL's ±7.1% implied** is **no information**, and a beat against estimates that were
  cut **4:1 over 30 days** is a lowered bar, not a beat. Score the **capex line** (derived run-rate
  **~$49.8B/qtr**; <~$40B under-runs, >~$50B implies a raise), never the price reaction.
- **Anti-signal (kills P3's neutrality → UW):** capex guide **cut** or explicit ROI defensiveness →
  breaks the volume leg and the price leg together, and extends past memory to NVDA/AVGO.
- KPI: Alphabet Q2 capex line + FY guide; then MSFT/META **07-29**.
- Catalyst: **GOOGL 2026-07-22 AMC (≈07-23 05:00 KST)** · TSLA same night · INTC 07-23 · **MSFT+META 07-29**.

**P4 — Energy's war premium re-inflated within 24 hours; the bracket, not the direction, is the position.**
- Anchor: WTI **$86.00, a fresh six-week high**; **Brent back above $92**; **CENTCOM's 11th consecutive
  night of strikes**; Iran's FM on the strike that **killed Khamenei**; Japan's imports at a record on
  the oil bill; India bonds slipping on the oil spike `[news, 2026-07-22]`. Earnings confirmation:
  **Equinor's profit +93%** `[news]`. Positioning cushion: WTI COT **10%ile**, NatGas **6%ile** `[COT — same print as yesterday]`.
- Direction: **OW energy** on an asymmetry, not a forecast.
- **Both branches (mandatory — measured oscillation):** the prior run's ADDENDUM recorded
  **de-escalation** ($89→$82) on 07-21; **less than 24 hours later the premium is back above $92**.
  (a) escalation → spike into crowded shorts; (b) de-escalation → premium bleeds again, but 10%ile
  positioning and a +93% earnings print floor it. **Anyone reading a direction out of a variable that
  reversed twice in two sessions is reading noise.**
- **Anti-signal:** WTI COT normalizes >40%ile **and** crude closes below the pre-escalation range with
  no demand offset → it was only a squeeze; fade.
- KPI: Brent/WTI daily · WTI COT %ile (next print **Fri 07-24**) · XLE vs **SPY** (benchmark named, C1).
- Catalyst: Hormuz headlines (undated, `[blank]` — not guessed) · **EU Russia-sanctions finalisation** ·
  XOM/CVX earnings early Aug.

**P5 — Tariff escalation is a sector-specific tax and it landed on Health Care today.**
- Anchor: **up to 200% pharma tariff announced, pharma stocks bleeding** [11 articles / **7 outlets**,
  2026-07-22] `[news]`; a **50% tariff executive order** signed 07-21 [body-confirmed]; the Canada
  tariff thread peaked at **24 outlets** before ending; *"US eyes new tariffs as existing duties near
  expiry"*; tariff bucket velocity **1.16×** the pool `[news]`.
- Direction: **UW Health Care** — the sector already carried the only negative Q2 EPS growth of the 11,
  and now takes a direct policy hit. Second-order: **Industrials/Materials** import-cost exposure.
- **Both branches:** (a) tariffs are implemented as announced → margin hit is real and dated;
  (b) they are negotiated down / delayed (the pattern this administration has repeatedly run) → an
  oversold defensive with cheap positioning. **This is an oscillating policy variable — bracket it.**
- **Anti-signal:** a formal carve-out or delay for pharma → the UW is spent; revert to neutral.
- KPI: pharma sub-index vs **XLV**, and XLV vs **SPY** (benchmarks named, C1) · the effective date in
  the executive order text.
- Catalyst: implementation date `[blank — not in the calendar; do not guess]`.

**P6 — Japan is the run's un-priced global-duration channel.**
- Anchor: **BOJ said open to a faster hike pace**; **yen at a 40-year low above 163**; MoF "ready to
  take decisive currency action"; **June trade deficit ¥406.9B on a +25.4% import spike** (both halves:
  deficit widened *and* imports at a record, oil-driven) `[news, 3 separate clusters]`. The FX term
  bucket reads a flat **1.00** because the story is split across three doors — a measured under-read.
- Direction: a BOJ acceleration into a US real-yield high is the classic global term-premium
  transmission. It reaches US duration *through* the JGB/carry channel, not through the Fed.
- **Both branches:** (a) BOJ accelerates → global long end sells off, compounding P1's kill line;
  (b) MoF intervenes on the currency instead → yen snaps, carry unwinds, and the *equity* leg is hit
  before the rate leg.
- **Anti-signal:** yen retraces below ~155 with no policy change → it was positioning, not policy.
- **⚠ Tagged `[unverified]` (rule W2):** "BOJ tightening leads US long-end yields" is a **lead/lag
  claim with no lag table in this repo.** It is carried as a channel to watch, **not as evidence**, and
  may not be cited by DEEP or BET until measured. Candidate dig.
- KPI: USD/JPY · JGB 10y · DFII10 co-movement. Catalyst: next BOJ meeting `[blank — not in calendar]`.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> Wind direction only, one line per GICS sector. Not an equal-weight analysis of 11 sectors.

| # | GICS Sector | Tilt | Driving prop. | One-line why |
|---|---|---|---|---|
| 1 | **Energy** | **OW+** | P4, P2 | War premium re-inflated <24h (WTI $86 6-wk high, Brent >$92) into 10%ile crowded-short positioning, with a +93% earnings print behind it |
| 2 | **Financials** | **OW** | P1, P2 | Bear-steepening 2s10s **+0.39** + credit that refuses to confirm stress (HY 2.69%) + the day's largest earnings mass; the sector is paid by exactly the wedge in §A |
| 3 | **Info Tech** | **N (was OW-)** | P3, P1 | **Held flat into the binary, deliberately.** Under-owned (Nasdaq COT 4%ile) and memory ripped 12–14%, but the capex/FCF bear case has 5 days of runway and tonight decides it. A tilt now is a one-way tilt into a known binary |
| 4 | **Comm Services** | **N** | P3 | GOOGL *is* the binary. Any tilt is a bet on the print — held to neutral by protocol until the capex line prints |
| 5 | **Industrials** | **N+** | P4, P5 | Saudi civil-nuclear approval + drone-import ban + uncrewed-fighter programs are real order flow; offset by tariff input costs. Defense is the live sub-node |
| 6 | **Utilities** | **N-** | P1, P4 | Bond proxy into a **120-day-high real yield** — a direct headwind. The Saudi nuclear deal and AI power demand are the only offsets, and they are slower than the discount rate |
| 7 | **Real Estate** | **UW** | P1 | The purest duration expression on the board while real 10y makes 120-day highs. No offsetting catalyst in the feed |
| 8 | **Health Care** | **UW** | P5 | Only sector with negative Q2 EPS growth, now taking an announced **up-to-200% pharma tariff** [7 outlets]. Two independent negatives |
| 9 | **Materials** | **UW** | P1, P5 | Copper **95%ile crowded-long** + DXY near range highs + tariff input costs. Late-stage; the easy money is made |
| 10 | **Cons. Discretionary** | **N-** | P1, P3 | TSLA prints tonight; ex-autos, big-ticket demand is the most real-rate-sensitive consumption there is |
| 11 | **Cons. Staples** | **N** | P1 | Defensive bid, but a bond-proxy-adjacent multiple into rising real yields. Ballast only if P1 branch (b) or the VIX>24 anti-signal trips |

**Wind summary.** OW **Energy** and **Financials** — the two sectors paid by *this* wedge (war premium
into crowded shorts; steepening into non-confirming credit). UW the three duration/policy-taxed
sectors: **Real Estate, Health Care, Materials**. **Info Tech and Comm Services are pinned at neutral
on purpose** — both are one earnings line away from a rewrite, and the protocol forbids a one-way tilt
into a binary ≤48h.

**DEEP candidates handed to ROTATION:** **Energy · Financials · Info Tech · Health Care**, with
**Industrials** flagged as the pre-mortem swing (nuclear/defense order flow could promote it).
Health Care enters as a *falsification* target, not a long: it is the sector where this run's view is
most likely to be wrong in the "oversold on an oscillating policy variable" direction (P5 branch b).

---

## §F · Self-backtest

**Running hit-rate: 0 scored / 0 scoreable.** The first US propositions in `llm_outputs/` were
registered **2026-07-21** (both `industry_US/` and `US_2/`). The +7d scoring window opens
**2026-07-28**; +14d **2026-08-04**; +30d **2026-08-20**. Nothing may be scored today without
manufacturing a horizon, and that is not done here.

**+1d state check of the 07-21 propositions (not a score — a kill-line audit):**

| Prior prop | Kill line | State today | Status |
|---|---|---|---|
| P1 disinflation-holds / earnings-now | real 10y **>2.55%** or VIX >24 | real 10y **2.35%** (was 2.31), VIX 18.65 | **Un-tripped, 20bp of room — closer** |
| P2 Energy asymmetric long | WTI COT >40%ile **and** crude below range low | COT unchanged at 10%ile (same print); WTI at a **6-week high** | Un-tripped; the 07-21 ADDENDUM's de-escalation reversed inside 24h |
| P3 Tech tactical OW | real 10y >2.55% **or** a Mag7 guidance miss | first live test is tonight (GOOGL/TSLA) | **Pending — this is why IT is neutral today** |
| P4 Financials OW | 2s10s re-inverts, or credit-cost jumps | 2s10s **+0.39** (steeper); HY OAS −4bp | Un-tripped, moving the right way |
| P5 Materials UW | Copper COT resets <70%ile on a real catalyst | 95%ile, unchanged print | Un-tripped |

**Recurring failure class, actively guarded this run:** banking a one-sided read of an *oscillating*
variable. Three variables in this report oscillate (oil war premium, tariff policy, the capex
narrative) and **all three are written with both branches**. The 07-21→07-22 oil reversal
($89 → $82 → >$92 in two sessions) is the measured justification, not a hypothetical.

**New failure class logged this run:** a **partial-day window end** silently inflates FADING tags in
the thread axis. Measured today: every oil thread tagged FADING while oil was the day's **#1 head
event at 10 outlets**. Read the per-day denominator (206 vs 924) before believing any tag dated today.

---

## §5 · DRIFT ADDENDUM

> **APPEND-ONLY** (Stage 10/10). §A–§F above are **not edited** — the original call stays visible next
> to its correction, because that asymmetry is what the self-backtest eats.

### ⚠ Tool failure disclosed first (P4)

`scripts/drift_watch.py` **could not run**: it calls `module_news_data drift`, and `drift` is **not in
the server's `DB_READ_CMDS` allowlist** (`'drift' 는 원격 실행 불가(조회 전용). 허용: blindspot, burst,
chain-hop, coverage, export, fts, search, theme-age`), while this client has **no local
`news_alert.db`/`news_fts.db`** (client-owned derivative only). **This is a real repo defect, not a
one-off**: the desk's post-run kill-switch detector is unreachable from the client whenever the news
axis is served remotely. Logged as a dig; **`__main__.DB_READ_CMDS` is the single source and adding a
line there needs a human plus a server `git pull` + API restart** (CLAUDE.md P6).

**Substitute used, and its arithmetic stated**: the same built-in `KILL_TERMS` set run through the
**allowed** `fts search --count`, 1-day vs 7-day, `--scope foreign`. ⚠ The raw d1/avg7 ratio is
**not** the burst — the pool itself grew. Measured pool denominators: **1-day foreign = 10,046
articles**, **7-day = 22,591 (avg 3,227/day)** ⇒ **the pool's own d1/avg7 baseline is 3.11×.**
Every ratio below is divided by that. Anything at ~1.0 is moving *with* the feed, not bursting.

| Kill term | d1 | d7 | raw d1/avg7 | **÷3.11 pool baseline** | Read |
|---|---|---|---|---|---|
| **new tariff** | 62 | 79 | 5.49× | **1.77× 🚨** | The single fastest kill term on the board |
| **ceasefire** | 235 | 405 | 4.06× | **1.31× 🚨** | Body-read below — it is **not** peace |
| **blockade** | 232 | 431 | 3.77× | **1.21×** | Rides the same Hormuz story |
| guidance cut | 5 | 11 | 3.18× | 1.02× | n=5 — **indistinguishable** |
| strikes on Iran | 71 | 161 | 3.09× | 0.99× | At baseline |
| Strait of Hormuz | 355 | 833 | 2.98× | 0.96× | At baseline |
| circuit breaker · default · downgrade · rate hike · rate cut · bankruptcy · export ban | 11 · 88 · 75 · 181 · 46 · 39 · 4 | — | 2.33–2.96× | **0.75–0.95×** | All **slower than the pool** |
| flash crash · state of emergency | 3 · 4 | 4 · 7 | 5.25× · 4.00× | 1.69× · 1.29× | **n≤4 — indistinguishable**, not a burst |
| **capex cut** | **0** | 1 | — | — | ★ see below |
| emergency FOMC | 0 | 0 | — | — | Nothing |

### 🚨 DRIFT 1 — the "ceasefire" burst is an ESCALATION burst, and oil is up 4% since the baseline

**Body-read (required — a count is not a finding).** The top item is CNBC, **2026-07-22**:
**"Oil prices jump 4% as Rubio says Iran 'not serious' about peace talks"**, alongside *"Ships attacked
as Trump extends Iran ceasefire"*, DW's *"Trump says the United States is 'not finished' with Iran"*,
and FXStreet reporting *"Washington is demanding a longer ceasefire and partial navigation [rights]"*.
Yahoo's 07-20 body records that the ceasefire framework **"has since largely broken down."**

**What this changes.** §A's tape was **asof 07-20 (FRED)** and **07-21 close (sweep)**; §C had WTI at a
six-week high **$86.00** and Brent **>$92**. Since that baseline, **crude is +4% on a named US-official
statement.** So:
- **P4's oscillating variable has now printed three states in three sessions**: de-escalation 07-21
  ($89 → $82) → re-escalation overnight (Brent >$92) → **a further +4% today on Rubio**. The report said
  *"anyone reading a direction out of a variable that reversed twice in two sessions is reading noise"* —
  **that stands, and is reinforced, not overturned.** The bracket is the position; the direction is not.
- **S8 (frozen, `handoff/SCENARIOS.md`) is NOT firing branch A.** Branch A required crude **below** its
  pre-escalation range **with the diesel crack rolling over**. Crude is up. **Branch C (escalation
  continues) is the live state pointer.** ⚠ The DEEP·ENRG detachment counter (crack falling while
  refiners rise) is a **separate** counter at **3** and its next reading is tonight's close — a rising
  crude print does not settle it either way.
- **No threshold is moved and no branch is scored**, because the observable S8 names is the
  **crack**, not the crude price.

### 🚨 DRIFT 2 — "new tariff" is the fastest kill term and it is broader than the pharma line

**Body-read:** Al Jazeera 07-21 — **"Trump imposes 50% US tariffs on some Canadian goods, citing
discrimination"**; *"US eyes new tariffs as existing trade duties near expiry"*; Economic Times ties the
same 50% action to a firm dollar. Together with today's **up-to-200% pharma tariff** [11 articles / 7
outlets], **P5 was written one sector too narrow.** The axis is a **broad tariff wave with at least
three live fronts** (pharma, Canada, expiring duties). P5's both-branch structure is unchanged and its
`[blank]` implementation date is still blank — but the exposure is not confined to Health Care, and
**Materials / Industrials input costs are the second-order carriers**, which §E already had as UW / N−.

### ★ DRIFT 3 — the null that matters: "capex cut" printed **ZERO** in 24 hours

The branch that would **rewrite** the standing view (S1-C, and the whole of P3) has **no narrative
presence at all** going into tonight's print — 0 hits in 24 hours, 1 in 7 days. Read next to the
pre-print state already recorded (**±7.1% implied**, near-term estimates cut **4:1**), it says the market
is positioned for a *disappointment against a lowered bar*, **not** for a capex cut.
⚠ **This is a statement about attention, not about probability**, and the desk's own measured lesson is
that a regime-moving event can sit at 1.3× term-share while eight outlets scream it (the KOSPI −8%
circuit-breaker day ranked **nowhere** by term velocity). **Absence of narrative is not evidence of
absence.** It is logged so that if branch C does fire, the record shows it was un-narrated beforehand.

### Kill-switch status after the drift pass — no verdict flipped

| Kill line | State | Tripped? |
|---|---|---|
| P1/P3 · real 10y **>2.55%** | **2.35%** (FRED asof 07-20), 120-day high | **No — 20bp of room** |
| P1 · VIX **>24** | 18.65 (asof 07-20) | No |
| P2 · HY OAS **>3.10%** close | **2.69%**, 6bp off a 365-day low | No |
| P4/S8 · crude below pre-escalation range **with cracks rolling** | Crude **+4% today**; crack is the observable and is unresolved | **No — branch C is the live pointer** |
| P5 · formal pharma carve-out or delay | None found | No |
| P6 · yen below ~155 with no policy change | No | No |

**Net:** the base-case tilt is intact. The one substantive change is that **the oil axis moved
*further* into escalation after the report's baseline**, which raises the weight on the S8 bracket and
on the stacked 07-29 tail — and the tariff axis is **broader than the single sector P5 named**.
⚠ **Everything in §A–§F above remains as originally written**; this addendum sits next to it.
