# MACRO_REPORT — industry_US — 2026-07-21

> Stage 1/8 (MACRO) of protocol `industry_us`. English-pure runtime, `--market us`.
> Purpose: falsifiable macro propositions → **★sector transmission matrix** (ROTATION's input).
> Zero buy/sell. Primaries `[FRED]` > narrative `[news]`/`[web]`. Data asof stamped per line.

---

## §A · Regime primaries `[FRED]` (asof 2026-07-17 unless noted)

| Series | Latest | 1-mo Δ | Read | Freshness |
|---|---|---|---|---|
| Fed Funds eff (DFF) | **3.63%** | flat | Policy on hold; mkt prices ~1 cut into YE → ~3.4% | daily, fresh |
| 10y Treasury (DGS10) | **4.55%** | +0.12 | Long end drifting up despite disinflation | daily, fresh |
| 2y Treasury (DGS2) | **4.18%** | +0.13 | Front end sticky (cut priced but not imminent) | daily, fresh |
| **2s10s** | **+0.37** | steeper | Bull/bear-mixed steepening — term premium, not cut-euphoria | derived |
| Real 10y (DFII10) | **2.31%** | **+0.17** | ★ Real yields RISING = tightening financial conditions at the long end | daily, fresh |
| Core CPI YoY (CPILFESL) | **2.57%** | MoM −0.02% | Disinflation intact; core basically flat MoM | **monthly, asof Jun (1-mo lag)** |
| Headline CPI YoY (CPIAUCSL) | **3.46%** | MoM −0.42% | Sharp headline cool (energy/base effects) | **monthly, asof Jun (1-mo lag)** |
| Unemployment (UNRATE) | **4.2%** | +0.1 YoY | Labor loosening slowly, not cracking | monthly, asof Jun |
| DXY Broad (DTWEXBGS) | **120.53** | +1.28 | Dollar firming — headwind for EM/commodity-priced-in-USD & US multinationals' FX | daily, fresh |
| VIX (VIXCLS) | **18.65** | +1.87 | Moderate; 5-day [16.5→18.6] uptick into earnings/FOMC week | daily, asof Jul-20 |
| M2 (M2SL) | **$23.05T** | +5.1% YoY | Liquidity re-expanding (+5% YoY) — supportive backdrop | monthly, asof May |

**Corroboration `[web]`**: June CPI headline 3.5% / core 2.6% (my FRED calc 3.46%/2.57% — matches).
July FOMC 28–29; hike odds ~10%; median dot = 1 more 25bp cut in 2026 to ~3.4%. Gov. Waller (Jul-16):
needs "several months" of cooler data before confident. `[web: CNBC/FactSet/Fool 2026-07-13..20]`

**★The regime tension of this run:** headline disinflation (3.5%, MoM −0.42%) is being celebrated by
equities, **but the long-end real yield is climbing (+0.17 to 2.31%)** — the discount rate on long-duration
assets is going UP even as the Fed sits still. That wedge is the single most important cross-current: it
rewards *earnings-now* over *duration-of-growth-later*.

---

## §B · Positioning `[COT, CFTC]` (Tue-close, 3–4d lag → context, NOT trigger)

| Instrument | Net-spec | 1yr %ile | Signal |
|---|---|---|---|
| Nasdaq-100 | −10,313 | **4%ile** | 🔴 Crowded-SHORT → rebound ammo for mega-cap tech |
| S&P500 e-mini | −38,938 | 78%ile | 🟡 neutral-ish (spec short but rich percentile) |
| Russell 2000 | +103 | 67%ile | 🟡 neutral |
| UST 10Y | −831k | 22%ile | 🟡 spec short but light percentile |
| USD Index | +13,173 | 58%ile | 🟡 neutral (dollar bid not yet crowded) |
| WTI Crude | +19,783 | **10%ile** | 🔴 Crowded-SHORT → energy rebound ammo |
| Nat Gas | −178,612 | **6%ile** | 🔴 Crowded-SHORT → energy rebound ammo |
| Gold | +186,682 | 23%ile | 🟡 long but not extended |
| **Copper** | +64,385 | **95%ile** | 🟢 Crowded-LONG → materials/copper overheated, unwind risk |
| Silver | +25,074 | 40%ile | 🟡 neutral |

**Positioning tells:** (1) tech is *under*-owned by fast money (4%ile) — pain trade is UP, cushions the
"AI capex doubt" narrative; (2) energy (WTI 10%ile, NatGas 6%ile) is *under*-owned into an oil binary
(Hormuz) — asymmetric rebound fuel; (3) copper at 95%ile is the crowded-long to fade — materials strength
is late-stage. ⚠ US has NO investor-type actuals (no KR-style foreign/institution feed); this is
positioning context only, never a standalone trigger.

---

## §C · Narrative axis (⚠ news-DB axis DOWN this run)

⚠ **P4 disclosure:** the DeGaJa news event/term axis (`brief` / `fts` / `blindspot`) was **unavailable**
this run — the news API (`DEGAJA_NEWS_API`) returned **401 Unauthorized** (Basic-auth creds not present in
this sandbox), and the GPU event axis is client-only. Per the protocol's "know before you speak", the
narrative below is sourced from **live WebSearch** as the substitute, and I do **not** claim an event
denominator I cannot measure. Any "quiet in bucket X" claim is therefore withheld, not fabricated.

- **Rotation tape `[web, Jul 2026]`:** Energy (XLE) is the sharpest upside rotation and holds the top
  weekly rank; Financials (XLF) has confirmed leadership on both horizons; Real Estate/Staples/Health Care
  rotated up into Leading; **Technology (XLK) finished last** after a 5-session deterioration (AI-capex
  payoff doubts); Industrials (XLI) led the downside rotation.
- **Earnings `[FactSet, Jul-17]`:** Q2 blended EPS growth **+24.7% YoY** (revised UP through the quarter,
  vs the usual down-drift); 88% of the 10% reported beat, by 16.4%. Mag7 ~+28%. Semis (AVGO +92%, AMD
  +236%) and energy majors (XOM +122%, CVX +195%) are the outsized contributors. **Health Care is the
  ONLY sector expected to post a YoY earnings decline (−9%).**
- **Binary catalysts in window `[CATALYST_WATCH.json]`:** SCHW (D-0, 7/21), **TSLA (D-1, 7/22)**,
  RTX + LMT (D-2, 7/23), plus an undated Iran/Hormuz oil-axis statement (TACO trigger). **TSLA ≤48h is a
  binary → PREMORTEM must bracket it both ways** (one-way tilt into a known binary = protocol violation).

---

## §D · Macro propositions (falsifiable; both branches; anti-signal; KPI; catalyst)

**P1 — Disinflation lets equities hold, but the LEADERSHIP is earnings-now, not duration.**
- Anchor: headline CPI 3.46% (MoM −0.42%), core 2.57% flat `[FRED]`; real 10y +0.17 → 2.31% `[FRED]`.
- Direction: risk-on breadth persists **while** long real yields cap long-duration multiples.
- **Anti-signal (kills P1):** real 10y breaks **>2.55%** on a hot re-acceleration print → duration/growth
  de-rates and the "hold" fails; OR VIX >24 sustained.
- KPI: DFII10 daily; next CPI (Aug); 10y level. Catalyst: **FOMC 7/28–29**, Aug CPI.

**P2 — Energy is the asymmetric long: crowded-short positioning + earnings surge + an open oil binary.**
- Anchor: WTI COT 10%ile, NatGas 6%ile (🔴 crowded-short) `[COT]`; XOM +122%/CVX +195% Q2 EPS `[FactSet]`;
  XLE top weekly rotation rank `[web]`; Hormuz statement pending `[catalyst]`.
- Direction: OW energy. **Both branches (mandatory — oscillating war-premium):** (a) Hormuz escalation →
  oil spike, shorts covered, XLE rips; (b) "Strait open / TACO" de-escalation → oil gives back premium,
  but crowded-short means downside is cushioned and the earnings/dividend floor holds. Net skew = up.
- **Anti-signal:** WTI COT normalizes back above 40%ile AND crude rolls under recent range low on
  de-escalation with no demand offset → thesis is just a squeeze, fade it.
- KPI: WTI, XLE rel-strength, COT %ile weekly. Catalyst: Hormuz headline; XOM/CVX earnings (early Aug).

**P3 — Tech is under-owned (pain-trade up) but capped by real yields — a tactical, not structural, OW.**
- Anchor: Nasdaq-100 COT **4%ile** (🔴 crowded-short = rebound ammo) `[COT]`; Mag7 Q2 +28%, AVGO +92%/AMD
  +236% `[FactSet]`; BUT XLK last in rotation & real 10y rising `[FRED/web]`.
- Direction: neutral-to-slight-OW (semis > software), because positioning + earnings are a floor but the
  rising real-yield discount is a ceiling.
- **Anti-signal:** real 10y >2.55% OR a Mag7 guidance miss (TSLA 7/22 is the first live test) → the
  under-ownership cushion is spent; drop to UW.
- KPI: SOX rel SPX; Nasdaq COT %ile; TSLA/AVGO guidance. Catalyst: **TSLA 7/22**, AVGO/NVDA later.

**P4 — Financials are the quiet leadership: steep-ish curve + confirmed rotation, no crowding.**
- Anchor: 2s10s +0.37 (steeper) `[FRED]`; XLF confirmed leadership both horizons `[web]`; no COT crowding flag.
- Direction: OW financials (banks/capital-markets benefit from steepening + IB/trading revenue + light
  positioning).
- **Anti-signal:** 2s10s re-inverts (<0) on a growth scare, OR bank earnings show credit-cost jumps.
- KPI: 2s10s; XLF rel SPX; bank NII/credit commentary. Catalyst: bank earnings (largely reported), FOMC.

**P5 — Copper/materials strength is late-stage and crowded; do NOT chase.**
- Anchor: Copper COT **95%ile** (🟢 crowded-long) `[COT]`; DXY +1.28 firming (USD headwind for metals) `[FRED]`.
- Direction: UW/avoid materials as a *new* long; the easy money is made.
- **Anti-signal (would flip to neutral):** a genuine China-stimulus / supply-shock catalyst with COT
  resetting below 70%ile — then it's demand, not positioning froth.
- KPI: Copper COT %ile; DXY; LME inventory. Catalyst: China data, DXY direction.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> Wind direction only (NOT equal-weight analysis of 11 sectors). One line each, driving proposition ID.

| # | GICS Sector | Tilt | Driving proposition(s) | One-line why |
|---|---|---|---|---|
| 1 | **Energy** | **OW+** | P2 | Crowded-short + earnings surge + open oil binary = asymmetric up |
| 2 | **Financials** | **OW** | P4, P1 | Curve steepening + confirmed rotation + no crowding + earnings-now regime |
| 3 | **Info Tech** | **OW-/N** | P3, P1 | Under-owned (4%ile) & earnings-strong, but real-yield ceiling → semis>software, tactical |
| 4 | **Comm Services** | **N+** | P1, P3 | Mag7 earnings tailwind; ad/streaming cash-flow-now fits regime; watch real yields |
| 5 | **Industrials** | **N-** | P1 | Earnings-now ok but XLI led the DOWNSIDE rotation; defense binary (RTX/LMT 7/23) is a swing |
| 6 | **Health Care** | **UW** | narrative | ONLY sector with negative Q2 EPS (−9%); rotated up on defensive bid, not fundamentals |
| 7 | **Financials-adj REITs / Real Estate** | **N-** | P1 | Rotated into Leading on rate-cut hope, but rising REAL 10y is a direct headwind — conflicted |
| 8 | **Materials** | **UW** | P5 | Copper 95%ile crowded-long + firm DXY = late-stage, don't chase |
| 9 | **Cons. Discretionary** | **N** | P3 | TSLA 7/22 binary dominates the tape; ex-autos, real-yield-sensitive big-ticket demand soft |
| 10 | **Cons. Staples** | **N+** | P1 | Defensive rotation-up bid; ballast if VIX>24 anti-signal trips; no alpha, just insurance |
| 11 | **Utilities** | **N-** | P1 | Bond-proxy — rising real 10y (+0.17) is a headwind; AI-power-demand story is the only offset |

**Wind summary:** OW cyclicals-with-earnings-and-cheap-positioning (**Energy, Financials**), tactical
OW **Tech (semis)**, UW rate-sensitive/late-crowded/no-earnings (**Materials, Health Care, Utilities/REITs**).
The 4 DEEP candidates that ROTATION should carry: **Energy, Financials, Info Tech, Comm Services** — with
**Industrials** flagged as the pre-mortem swing (defense-earnings binary could promote it).

---

## §F · Self-backtest (running hit-rate)

⚠ **This is the FIRST `industry_US` run in `llm_outputs/`** (prior folders 2026-07-15/16 contain only
`real_alpha_kr` and `미러링`, no US MACRO_REPORT). There is **no prior US proposition set to score** —
hit-rate baseline starts here. Next run scores P1–P5 above at +7/+14/+30d.

**Recurring failure class to watch (carried from protocol note):** banking a one-sided read of an
*oscillating* variable. P2 (oil war-premium) is explicitly written with BOTH branches for exactly this
reason; P1/P3 carry the real-yield anti-signal as the kill line.

---

## §5 · DRIFT ADDENDUM

> **APPEND-ONLY** (Stage 8/8). The original §A–§F call above is NOT edited — the correction sits next
> to it so the self-backtest can score the asymmetry. ⚠ Deterministic burst detector (`drift_watch.py`)
> could NOT run (local `news_fts.db` absent; news API 401). Substitute = live WebSearch cross-check of
> the report's oscillating kill-switch variables, 2026-07-21.

### 🚨 ADDENDUM 2026-07-21 — Hormuz is ACTIVE and oscillating, not a "pending undated statement"

The report's §C/§D treated the Iran/Hormuz oil binary as an **undated pending statement**. The live tape
says it is an **active, escalating crisis that is whipsawing intraday** — exactly the oscillating-variable
regime P2 was bracketed for, but hotter than the baseline captured:
- **State (was mis-stated as "pending"):** the interim US-Iran truce broke down **7/8**; Iran struck
  commercial ships in the Strait; the US has bombed Iran **9 consecutive nights**; the Houthis declared a
  maritime embargo on Saudi; Trump (7/20) said Iran "would pay" for 3 US service members' deaths. `[Al Jazeera, CNBC 2026-07-20]`
- **Oil is oscillating HARD:** Brent closed **$89.22 Mon** (escalation) → crude fell toward **~$82 Tue 7/21**
  on renewed peace-talk hopes. Analysts flag a Hormuz-slowdown + depleted inventories could push **>$100**. `[TradingEconomics/Al Jazeera 2026-07-21]`
- **This is the T3 AGAINST-US branch PARTIALLY FIRING right now:** the war premium is *currently deflating*
  on peace hopes ($89→$82). Per the ticket, **do NOT press an energy short** — WTI COT 10%ile crowded-short
  means this is precisely where a peace-hope dip and an escalation-spike both live. The bracket holds; the
  *state pointer* moves to "de-escalation attempt in progress, unresolved."

### Minor drifts (no kill-switch flip)
- **VIX eased to 17.58** on 7/21 (−5.7%), *below* the report's 18.65 (asof 7/20) — intraday risk-on on
  peace hopes, NOT the VIX>24 anti-signal. `[market data 2026-07-21]`
- **10y eased to ~4.52%** (report had 4.55% asof 7/17) on cooler inflation — a small move toward, not
  through, any tripwire; real-yield duration anti-signal (>2.55%) remains un-tripped.
- Chips up early 7/21 on peace-talk hopes (corroborates the Info Tech 🟢LIVE re-entry read); indices modestly
  lower (S&P −0.19%). `[Schwab 2026-07-21]`

**Net:** the base-case tilt is intact; the single change is that **Energy's key oscillating catalyst is LIVE
and mid-swing (de-escalation attempt)**, which raises the weight on the T3 bracket and the stacked
Energy/FOMC tail — watch Brent's war-premium floor and WTI COT into the 7/28-29 FOMC.

*Sources: [Al Jazeera Hormuz](https://www.aljazeera.com/news/2026/7/8/oil-prices-surge-as-us-strikes-iran-reversing-fall-to-pre-war-levels) · [CNBC oil 2026-07-20](https://www.cnbc.com/2026/07/20/oil-prices-today-brent-wti-crude-us-iran-centcom-hormuz.html) · [TradingEconomics crude](https://tradingeconomics.com/commodity/crude-oil) · [Schwab market update](https://www.schwab.com/learn/story/stock-market-update-open).*

---
*Sources for narrative §C: [CNBC 2026-07-13](https://www.cnbc.com/2026/07/13/stock-market-today-live-updates.html) · [FactSet Earnings 2026-07-17](https://insight.factset.com/sp-500-earnings-season-update-july-17-2026) · [Motley Fool 2026-07-20](https://www.fool.com/investing/2026/07/20/federal-reserve-july-inflation-forecast-red-flag/) · [Investing.com sector rotation](https://www.investing.com/analysis/sector-rotation-a-guide-to-the-sp-500-momentum-status-200675903). Primaries: FRED. Positioning: CFTC COT via `scripts/us_flow.py`.*
