# MACRO_REPORT — industry_US — 2026-07-23

> Stage 2/10 (MACRO) of protocol `industry_us`. English-pure runtime, `--market us`, news `--scope foreign`.
> Purpose: falsifiable macro propositions → **★sector transmission matrix** (ROTATION's input).
> Zero buy/sell. Primaries `[FRED]` > narrative `[news]`. Data asof stamped per line.
> **Run clock: 2026-07-23 22:1x KST = 09:1x ET — the US regular session has NOT opened.**
> Continuity anchor: `llm_outputs/2026-07-22/industry_US/MACRO_REPORT.md` + this run's `HANDOVER.md`.

---

## §0 · Catalyst injection `[catalyst_calendar --days 10]`

Pulled at **10 days, not the default 5** — the HANDOVER ranked dig **D26** first precisely because
`SCENARIOS.md` already names 07-29 and 07-30, both unreachable at `--days 5` from 07-23.
**12 binary catalysts in window.** Saved to `llm_outputs/2026-07-23/CATALYST_WATCH.json`.

| When | Event | Axis |
|---|---|---|
| **D-0 2026-07-23** | **RTX earnings** · **LMT earnings** | Industrials — **already printed pre-market, see §F** |
| D-6 2026-07-29 | **FOMC decision (Warsh, no SEP)** | rates 🔀 |
| D-6 2026-07-29 | META earnings · SK hynix ADR↔ordinary conversion opens · KR financial-holdco governance reform | AI capex / KR |
| D-7 2026-07-30 | **June PCE** · VLO earnings · STNG earnings · MA earnings | inflation / Energy |
| D-8 2026-07-31 | SK이터닉스 KKR SPA closing | KR |
| undated | Iran "Strait of Hormuz open" statement | oil 🔀 `[blank]` |

### ⚠ The calendar missed **two** D-0 binaries — third consecutive occurrence of dig D18

| Missing from `CATALYST_WATCH.json` | Why it is a binary | Evidence it is real |
|---|---|---|
| **INTC FQ2, tonight AMC (2026-07-23)** | It is the *only* registered scenario keyed to today's date (**S6**, `handoff/SCENARIOS.md`), and its branch A explicitly reads *"the industry_US IT underweight is short the wrong thing."* | Feed: *"Intel earnings loom as investors watch jobs data and corporate results"* [yahoo_finance, 07-22] |
| **ECB rate decision, today (2026-07-23)** | A G3 central-bank decision, D-0, with a live FX thread building into it | `ECB` term hits: **104 in 1 day vs a 41/day 7-day average = 2.5×.** Thread BUILDING 6 days (3→3→5→8→3→8 outlets), today's item *"Euro rallies against the Pound as markets brace for ECB's monetary policy decision"* [20 art / 8 outlets]; fxstreet: *"European Central Bank set to hold interest rates amid cooling inflation and weaker growth"* |

**The pattern is now measured three runs deep**: 07-22 missed GOOGL (±7.1% implied, the event the
whole run was organised around); 07-23 misses **INTC and the ECB**. The calendar reliably carries the
*second-tier* names (RTX/LMT/STNG/MA) and drops the largest binary of the day. Anti-tunnel discipline
is therefore depending on a human remembering, which is the exact failure D18 names.
⇒ **Both are handed to PREMORTEM as mandatory both-sides brackets.**

---

## §A · Regime primaries `[FRED]` — 120-day window

| Series (FRED id) | Latest | Δ prev obs | Δ ~20 obs | Read | Freshness |
|---|---|---|---|---|---|
| Fed Funds eff (DFF) | **3.63%** | flat | flat | Policy on hold | daily, asof 07-21 |
| 10y Treasury (DGS10) | **4.63%** | +3bp | **+17bp** (4.46) | 120d range [3.97, 4.67] — near the top | daily, asof 07-21 |
| **2y Treasury (DGS2)** | **4.26%** | **+5bp** | +5bp | ★ **120-day HIGH** (window max = 4.26) | daily, asof 07-21 |
| **2s10s** (derived) | **+0.37** | **−2bp** | +12bp | ★ **Bear-FLATTENING today** — reverses the 07-22 report's bear-steepening read | derived |
| **Real 10y (DFII10)** | **2.37%** | +2bp | +16bp (2.21) | ★ **120-day HIGH** (window max = 2.37) | daily, asof 07-21 |
| **10y breakeven (T10YIE)** | **2.28%** | +2bp | +5bp (2.23) | Inflation expectations still barely moved | daily, asof **07-22** |
| Core CPI (CPILFESL) | **YoY +2.57%** · **MoM −0.02%** | — | — | Both halves quoted (**C2**) | monthly, asof **Jun — 1-month lag** |
| Headline CPI (CPIAUCSL) | **YoY +3.46%** · **MoM −0.42%** | — | — | Both halves quoted (**C2**). Sharp sequential cool | monthly, asof **Jun — 1-month lag** |
| Unemployment (UNRATE) | **4.2%** | −0.1 MoM | — | 120d range [4.1, 4.5]. Not cracking | monthly, asof Jun |
| DXY Broad (DTWEXBGS) | **120.53** | +0.20 | +1.14 | Near the top of [117.44, 121.41] | daily, asof **07-17 — 4 sessions stale** |
| VIX (VIXCLS) | **17.05** | **−1.60** | −1.72 | Far from the >24 anti-signal *on FRED's tape* — but see §A-2 | daily, asof 07-21 |
| **HY OAS (BAMLH0A0HYM2)** | **2.69%** | flat | flat | **6bp off the 365d low (2.63)**; 120d max 3.46. No credit stress | daily, asof 07-21 |
| **IG OAS (BAMLC0A0CM)** | **0.78%** | flat | flat | Same read at investment grade; 120d range [0.73, 0.94] | daily, asof 07-21 |
| **NFCI (Chicago Fed)** | **−0.552** | −0.013 | −0.041 | **Loosening for a 5th straight week**, now 1.2bp off its 120d loosest (−0.564) | weekly, asof **07-17** |
| M2 (M2SL) | **$23.05T** | +1.09% MoM | +5.1% YoY | Both halves quoted (C2). Liquidity re-expanding | monthly, asof May |

⚠ **Freshness (P4)**: FRED daily series stop at **07-21** (breakeven has 07-22). **Nothing in this
table reflects the 07-22 US close or today's pre-open.** DXY is 4 sessions stale.

### §A-1 · What changed vs the carry — and it is not what the carry said

`STANDING_VIEW` M20 (asof 07-20/21) reads: *"~79% of the nominal move is real."* That is still true
**of the 20-session move**. But the **composition of the last two sessions inverted**:

```
20-session move :  10y +17bp   breakeven  +5bp   real +16bp   →  real-rate driven  (M20 holds)
last obs (d/d)  :  10y  +3bp   breakeven  +2bp   real  +2bp   →  split roughly evenly
front end       :  2y   +5bp  = 120-DAY HIGH,  outpacing the 10y  →  2s10s FLATTENED −2bp
```

★ **The front end is now leading, and that is a different regime statement.** A 2y at a 120-day high
into a **D-6 FOMC** is the market pricing *fewer cuts*, not more term premium. The 07-22 report called
this "bear-steepening — term premium, not cut-pricing." **On today's data that reverses: 2s10s
flattened.** The named cause is in the feed, not inferred:

- **"Warsh Confuses Traders, Makes Them Guess Next Week's Rate Move"** [bloomberg, 07-22] ·
  **"Fed Chair Kevin Warsh Just Threw Cold Water on Investors Who Thought the Worst of Inflation Was
  Over"** [yahoo_finance, **7 art / 5 outlets, 07-23**] · *"Kevin Warsh has homed in on three key
  phrases. How Fed watchers interpret them"* [cnbc] · *"A quieter Fed chief means others narrate the
  story"* [axios]. `[news, --scope foreign]`

⚠ **C2 discipline on the CPI line, because it cuts against the above**: headline CPI is **−0.42% MoM**
and core **−0.02% MoM** — sequentially the softest inflation data on the table — while the 2y makes a
120-day high and unemployment *fell* to 4.2%. **The front end is not repricing inflation; it is
repricing the reaction function and the labour side.** Quoting only the YoY (+3.46%) would have made
today's 2y look like a straightforward inflation trade. It is not.

### §A-2 · ⚠ The tape moved after FRED's last observation, and the direction is against §A

FRED cannot see today. A second provider can, so it is quoted **as a second provider with its own
caveats** (rule **D5** — and it disagreed with itself on one series, see the ⚠ below).

| Series `[yfinance, intraday 09:1x ET — INCOMPLETE BAR]` | 07-22 close | **07-23 (partial)** | Move |
|---|---|---|---|
| **^TNX (10y)** | 4.66 | **4.71%** | **+5bp — a 6-month high** (6mo max = 4.71) |
| **^VIX** | 16.64 | **19.13** | **+2.49 (+15%)** |
| **CL=F (WTI)** | 86.83 | **91.37** | **+$4.54 = +5.2%** |
| **3-2-1 crack** (own calc, 2×RB+HO−3×CL /3) | 66.86 | **59.36** | **−$7.50 = −11.2%** |

⚠ **Three caveats, none of them optional.**
1. **Every 07-23 figure is an unfinished bar.** The session opens at 09:30 ET. These are pre-open
   futures/quotes and will move. No stage may treat them as a close (this desk's own logged failure).
2. **A provider disagreement, unresolved**: `BZ=F` (Brent) prints **86.72 — below WTI's 91.37**, which
   is not a possible spread. The 07-23 Brent value also equals WTI's *07-22* value exactly, i.e. a
   column/roll artifact. **Brent is therefore NOT cited from yfinance today.** The feed's number is
   **$97** (*"Oil jumps to $97 after Houthis attack two Saudi Arabian oil tankers"*, 7 art/5 outlets)
   and it is tagged `[news]`, not `[measured]`. Logged as a new dig (**D30**).
3. **The 10y decomposition for 07-23 does not exist yet.** DFII10/T10YIE stop at 07-21/07-22. So
   whether today's +5bp on the 10y is *real* or *breakeven* is **unmeasurable at run time** — and the
   feed says it is inflation (*"Global Bond Yields Jump as Oil Prices Surge, Inflation Fears"*,
   3 art/3 outlets). **That is the shape of P1's own anti-signal**, so it is flagged, not resolved.
   **First scoreable at the next run, on FRED.**

★ **The single most important number this run is the crack, not the crude.** Crude **+5.2%** and the
3-2-1 crack **−11.2%** in the same session: the refining *margin engine* moved hard **against** the
oil price. This is the third independent observation of the same split (KR desk 07-21→07-22: crack
−10.2% on Brent +5.1%; US 07-22: crack 68.23→66.86 while crude rose). See §D-P4 and the C4 counter.

---

## §B · Positioning `[COT, CFTC]` — ⚠ still the same weekly print

| Instrument | Net-spec | Wk Δ | 1yr %ile | Tag |
|---|---|---|---|---|
| **Nasdaq-100** | −10,313 | −1,572 | **4%ile** | Crowded-SHORT |
| S&P500 e-mini | −38,938 | +3,953 | 78%ile | neutral |
| Russell 2000 | +103 | +990 | 67%ile | neutral |
| UST 10Y | −831,675 | −17,413 | 22%ile | spec short, light |
| UST 2Y | −1,157,477 | **+103,531** | 52%ile | neutral — but the largest weekly Δ on the board |
| USD Index | +13,173 | −96 | 58%ile | neutral |
| **WTI Crude** | +19,783 | −1,139 | **10%ile** | Crowded-SHORT |
| **Nat Gas** | −178,612 | −13,305 | **6%ile** | Crowded-SHORT |
| Gold | +186,682 | −7,564 | 23%ile | long, not extended |
| **Copper** | +64,385 | +113 | **95%ile** | Crowded-LONG |
| Silver | +25,074 | −2,941 | 40%ile | neutral |

⚠ **P4 disclosure**: byte-identical to the 07-21 **and** 07-22 reports. COT is Tuesday-close /
Friday-released — this is the **same single weekly observation read for a third day.** Per rule **S1**
the effective sample is **one date**, not three. **Next new print: Friday 2026-07-24** — which is also
S8's registered cross-check KPI.

⚠ **Rejected-ledger guard (`RESEARCH.md` D6)**: COT extremes are on the **REJECTED** list *as a
contrarian trigger*. Nothing below uses "crowded short ⇒ bounce" as a reason. They appear only as
**cushion/ammunition context attached to an independent reason**. The US has no investor-type actuals,
so positioning is the entire flow axis here — which is exactly why it must not be promoted.

---

## §C · Narrative axis `[news, --scope foreign]`

### C-0 · Denominator, stated before any claim (P4)

`brief --date 2026-07-23 --scope foreign --body 2`:

```
articles 2,137 → clusters 728 → market events (≥2 outlets) 361 → head 28 · body 333 · tail 0
subevents recovered 68 · single-source clusters 367 (15 shown) · nonmarket 0 · excluded_not_news {}
```

⚠ **`tail = 0` is NOT the coverage claim.** The honest statement:
- **Seen: 361 of 361** multi-outlet events (tail empty, nothing sampled away) **+ 15 of 367**
  single-source clusters = **376 of 728 clusters**.
- **Withheld: 352 single-source clusters = 48.4% of the day's clusters.** On `--scope foreign` the
  1-outlet tier is **scoreless** — the classifier is Korean-only — so those 352 are not "low-ranked",
  they are **unmeasured**. Every "quiet in bucket X" claim below is conditional on that.
- `excluded_nonmarket` is **0/0** and `excluded_not_news` is **empty** — both filters are
  domestic-specific and do no work on the foreign feed. Not a clean day; an unfiltered one.
- **Body-blind rate 68.8%** (`coverage`, 8 terms, 7d): title+summary sees 2,216 of a 7,092 reachable
  union ⇒ **recall 31.2%, 🔴**. Body-inclusive search was used for every drill below.
- ⚠ **Today is a partial day**: 361 events vs 07-21's 947 and 07-22's 785, because it is 09:1x ET.
  **FADING tags dated 07-23 are mechanically inflated** and are read as such.

### C-1 · The day's events — head tier (≥5 outlets), all 28 read

| Event | Coverage | Sector read |
|---|---|---|
| **EU hits Google with $1B fine over Play store** (+ €890m over search) | **39 art / 19 outlets — #1** | Comm Services — policy |
| ⤷ subevent: *"Google's extreme AI capex spending plans trigger a technical [selloff]"* | 4/2 | ★ the S1 read-through |
| **Oil rises to six-week high as US-Iran tensions escalate** | 29 / 16 | **Energy** |
| ⤷ *"Global Bond Yields Jump as Oil Prices Surge, Inflation Fears"* | 3/3 | ★ **rates ← oil** |
| **Houthis claim strikes on two Saudi oil tankers in the Red Sea** | 17 / 12 | **Energy — physical** |
| ⤷ *"Oil jumps to $97 after Houthis attack two Saudi Arabian oil tankers"* | 7/5 | Energy |
| **AI will not trigger employment collapse — Adecco** | 16 / 10 | Labour / IT sentiment |
| **China warns Philippines after latest clash at sea** | 10 / 10 | Geo tail |
| **Euro rallies vs Pound as markets brace for the ECB decision** | 20 / 8 | ★ **the missed D-0** |
| **Nokia Q2 profit beats on strong AI** demand | 7 / 7 | IT — networking |
| **UniCredit raises profit targets** | 9 / 6 | Financials — Europe |
| **IBM buys HRL Laboratories in a two-track quantum shift** | 8 / 6 | IT |
| **China's Moonshot AI stole from Anthropic — Trump tech adviser** | 6 / 6 | IT / policy |
| **BOJ to raise rates again by December as a weak yen revives inflation** | 9 / 5 | ★ **P6 channel** |
| **SK hynix denies the Intel Ohio fab deal — "but the market didn't care"** | 8 / 5 | Semis — ★ **S6-adjacent** |
| **US signs a landmark nuclear deal with Saudi Arabia** | 7 / 5 | Utilities / Industrials |
| **EU agrees a new round of sanctions against Russia** | 8 / 5 | Energy |
| **Fed Chair Warsh throws cold water on inflation optimists** | 7 / 5 | ★ **rates — §A-1's cause** |
| **Are SpaceX bulls deluding themselves?** | 10 / 6 | Spec-growth sentiment |
| **Amazon: Jassy announcement prediction** · **T. Rowe 40y dividend** · **Coinbase/BTC bottom** · **European car sales surge on Chinese EVs** · Europe wildfires · Russia/Ukraine · India protests · UK business rates · Malaysia-HK dual listing · midday bulletin | 5–13 outlets each | Read; no US sector transmission |

### C-2 · Body tier (333 events) — the market-structural rows

- **Energy, physical**: *"Gulf oil producers race to build alternative routes to the Strait"* [5/4] ·
  *"US-Iran tensions underpin dollar as yen nears 40-year low"* [7/4] · **TotalEnergies profit +68%
  on the oil price surge** · *"War risk insurance under pressure as volatility reshapes [shipping]"* ·
  **body-drill (oilprice, 07-23)**: the US ran its **12th consecutive wave** of strikes; the IRGC
  claims a tanker caught fire **in the Strait of Hormuz**; the Houthis declared a **naval blockade of
  Saudi Arabia at Bab el-Mandeb** and claim **nine ships turned back**; two named Saudi tankers
  (Encelia, Layla) struck. Two Cosco tankers with Saudi crude are transiting anyway.
- **AI capex**: **Tesla Q2 — capex guided >$25B**, Musk *"Tesla should be spending on AI as fast as we
  can"* [5/4] · *"Tesla's once-bullish tone on robotaxis shifts"* [4/4] · *"OpenAI to spend more on
  data centers"* [3/2] · *"TSMC just announced incredible news for Nvidia and Broadcom"* [8/4] ·
  *"Democrats try to harness data-center backlash"* [1 outlet — the political tail of the capex trade].
- **Rates/FX**: *"US Stock Market Today: S&P 500 futures slip as rate and jobs worries [mount]"* [7/4] ·
  *"Gold off a two-week peak as oil advances, Fed meeting eyed"* [4/4] · *"Japan's Katayama says will
  take necessary steps on for[ex]"*.
- **Real Estate / digital infra**: **Crown Castle signals $2.1B AFFO midpoint through H1 2027** [1 outlet]
  — a duration-REIT datapoint sitting in the unscoreable single-source tier. Directly relevant to R7.
- **Industrials/defense**: **Thales books strong orders as defense & aerospace [grow]** [wsj, 1 outlet] ·
  *"Nuclear Energy Revival Puts Westinghouse in Prime Position"* [4/4].
- **Health Care**: *"AstraZeneca secures EU nod for Etcamah"* · *"FDA reviews peptide injections"* ·
  *"Concentrated pharma exposure or broader global healthcare? PPH [vs…]"* [4/4]. ⚠ **The 07-22
  200%-pharma-tariff event does not appear anywhere in today's head or body tier.** Given a 48.4%
  withheld single-source tier, that is **an absence of evidence, not evidence of absence** (C3).
- **Consumer**: **Albertsons cuts annual sales and profit forecasts, shares −20%** [1 outlet] ·
  *"These consumer discretionary stocks flash overbought s[ignals]"* [4/2].

### C-3 · Trajectories `[thread --days 7, --scope foreign]`

Per-day denominators: 07-17 **347** · 07-18 187 · 07-19 221 · 07-20 701 · 07-21 **947** · 07-22 785 ·
07-23 **361 (partial)**. 3,549 daily events → 2,696 threads (467 multi-day, 145 alive).

| Thread | Curve (outlets/day) | Tag | Read |
|---|---|---|---|
| **Google: EU antitrust + the capex debate** | 5→2→4→12→18→**19** | **BUILDING** | ★ **The fastest-accelerating thread on the board, 6 days.** 07-22 was *"Google's profits are outrunning its AI spending boom"* [53 art/18]; 07-23 is the **$1B EU fine** [39/19]. The narrative rotated from *capex-as-drag* to *regulatory tax* **without the capex question being settled** |
| **Houthi maritime blockade → strikes on Saudi tankers** | 11→9→9→**12** | **BUILDING** | ★ **Building INTO a partial day** — it gained outlets while the day's denominator fell 785→361. That is the strongest form of this signal |
| **Oil / US-Iran strikes** (the older thread) | 12→5→6→17→18→14→16 | FADING | ⚠ **Artifact + rotation.** The window ends on a partial day, *and* attention migrated to the Houthi thread above. **Do not read FADING as attention leaving oil** — oil is the #2 head event at 16 outlets |
| **ECB / Euro-zone rates** | 3→3→5→8→3→**8** | **BUILDING** | The D-0 the calendar missed |
| **Gold above $4,000–4,100** | 5→4→6→5→6 | BUILDING | Independent corroboration of the rate/inflation stress |
| **Crypto / Bitcoin** | 2→3→3→5→5→6 | BUILDING | No US sector transmission |
| **"AI investment boom puts Big Tech's FCF under pressure"** | 5→2→6→3 | **FADING** | ★ **The bear thread P3 was built on has lost steam** — and GOOGL's actual print resolved it toward *"profits outrunning the spending boom"* [53 art/18 outlets] |
| **OpenAI rogue-model / containment breach** | 8→5→13→18→20→23→10 | FADING | Peaked at 23 outlets on 07-22. Regulatory tail; the AI-security theme the cycle registry still has **no row for** (D20) |
| **SpaceX below IPO price** | 8→4→3→7→8→5→6 | FADING | Spec-growth sentiment gauge, second run in a row |
| **Cleveland Fed's Hammack** | 5→2→5→5→5→9→5 | FADING | Superseded by Warsh (§A-1) |
| **IBM lowers full-year forecast** | 3→3→3→5→4→9→6 | FADING | IT dispersion datapoint (W5) |
| **Trump 50% Canada tariffs** | 9→25→8 | **ENDED 07-22** | The tariff wave's high-water mark. ⚠ An ENDED thread under an inherited proposition = staleness flag → **P5 is re-justified below, not carried** |
| *"Oil hits $90 as US-Iran war escalates"* · *"Iran strikes another tanker"* | peaks 15 / 11 | ENDED 07-22 | Rotation within the story, not away from it |

### C-4 · 7-bucket term sweep — normalized velocity (terms as separate argv, OR-mode, body-inclusive)

Pool: **7d = 26,437** · **30d = 58,727** ⇒ the pool's own ratio (7d/30d × 30/7) = **1.929**.
Normalized velocity = bucket ratio ÷ 1.929. **>1.00 = gaining share of the feed.**

| Bucket | Terms (separate argv) | 7d | 30d | Norm. vel. | vs 07-22 |
|---|---|---|---|---|---|
| **Credit** | credit · spreads · default · bankruptcy | 2,874 | 5,132 | **1.24 ★ fastest** | 1.23 → flat |
| **AI capex** | capex · hyperscaler · datacenter | 1,348 | 2,459 | **1.22** | **1.09 → 1.22 ▲▲** |
| **Tariffs** | tariff · tariffs · "trade war" | 1,108 | 2,039 | **1.21** | 1.16 → ▲ |
| **Energy** | Hormuz · OPEC · crude · Brent | 1,922 | 3,591 | **1.19** | 1.14 → ▲ |
| **Defense/geo** | Iran · missile · defense | 3,609 | 7,038 | 1.14 | 1.10 → ▲ |
| **Rates** | Treasury · yields · FOMC · Powell | 3,145 | 6,193 | **1.13** | ★ **0.97 → 1.13 ▲▲** |
| **Memory/semis** | DRAM · HBM · memory · semiconductor | 2,280 | 4,732 | **1.07** | 1.07 → flat |
| **FX** | yen · BOJ · dollar | 2,968 | 6,462 | **1.02 (slowest)** | 1.00 → flat |

★ **The headline change is Rates: 0.97 (slowest bucket) → 1.13.** The 07-22 report's finding was
*"attention is not where the move is."* **Attention has now arrived** — coincident with the 2y making
a 120-day high and Warsh going 7-article/5-outlet. That is a discovery window closing, not opening.
★ **AI capex 1.09 → 1.22** — second-fastest, and it accelerated *through* a print that beat. The
question migrated from "will they spend" to "what does spending cost the multiple."
⚠ **C5 (arbitrary choice)**: "credit" is polysemous in an English feed (credit card / rating / tax
credit), so this bucket's **absolute level is unreliable — only its change is used, and only as a
flag.** ⚠ Verified the multi-word term did not silently zero: `"trade war"` as a phrase = **63 hits**,
`tariff` alone = 1,090 — the bucket is genuinely carried by the single words, as intended.

### C-5 · Blind-spot pass `[blindspot --days 7 --scope foreign --sample-pct 25]`

Blind pool 28,924 · random sample 7,231. Token-0 emergent terms read **raw**:

1. **SpaceX — 394 mentions, still above Nvidia (372)** and Alphabet (328), with **no US-listed-equity
   bucket containing it.** This is the **second consecutive run** it ranks there (316 on 07-22), and
   the thread is *"sinks further below IPO price"*. A persistent, un-bucketed sentiment gauge for the
   speculative-growth cohort — a **dispersion datapoint (W5)**, not a name call.
2. **Earnings 1,978 / Results 695 / Quarter 445 / Second 410** — the sample is ~40% an earnings-season
   artifact. Stated so the next reader does not mistake volume for signal.
3. **Oil 530 · Energy 383 · Iran 755** together outrank every equity term except AI — consistent with
   §C-3's BUILDING energy threads and inconsistent with the FADING tag on the older oil thread.

**New terms folded into the living table**: `Houthi` · `Bab el-Mandeb` · `ECB` (promote out of the FX
bucket — it is a rates event, and FX scores 1.02 partly because the story splits) · `Warsh` (replaces
`Hammack` as the named Fed speaker) · `SpaceX` (carried, still unbucketed).

---

## §D · Macro propositions — falsifiable · both branches · anti-signal · KPI · dated catalyst

**P1 — The rate repricing moved to the FRONT end, and it is a reaction-function trade, not an inflation trade.**
- Anchor: 2y **4.26% = 120-day high** (+5bp) outpacing 10y **4.63%** (+3bp) ⇒ **2s10s +0.37, flattening
  −2bp**; real 10y **2.37% = 120-day high**; breakeven **2.28%** `[FRED, asof 07-21/22]`. Against
  **core CPI −0.02% MoM and headline −0.42% MoM** (both halves, C2) and unemployment **4.2%**, −0.1.
  Named cause `[news]`: Warsh — *"threw cold water on investors who thought the worst of inflation was
  over"* [7/5], *"confuses traders, makes them guess next week's rate move"* [bloomberg].
  Thread: **Rates bucket 0.97 → 1.13**, i.e. attention arrived (C-4).
- Direction: **fewer-cuts pricing taxes long-duration multiples and the rate-sensitive consumer;
  it pays the front-book earners.**
- **Both branches (mandatory — oscillating variable):** (a) FOMC 07-29 is read as "hold with optionality"
  → the 2y stalls ≤4.30% and this is positioning into an event; (b) **2y >4.40% or real 10y >2.55%** →
  the de-rate becomes a regime call, not a tilt.
- **Anti-signal (kills P1):** the 2y falls back <4.15% **or** the decomposition flips — real 10y falling
  **with** breakeven rising, which would make this an oil-inflation story after all.
  ⚠ **That anti-signal may already be firing and is unmeasurable at run clock**: ^TNX is **4.71%
  intraday, a 6-month high** on the day crude jumped 5.2%, and the feed headline is *"Global Bond
  Yields Jump as Oil Prices Surge, Inflation Fears."* **DFII10/T10YIE do not cover 07-23.** First
  scoreable next run, on FRED. Stated, not resolved.
- KPI: **DGS2 daily** (promoted above DFII10 this run) · DFII10 with T10YIE alongside · 2s10s.
- Catalyst: **FOMC 2026-07-29** (D-6, dated) · **June PCE 2026-07-30** (D-7, dated) · **ECB today**.

**P2 — Credit is still the loudest narrative and the quietest market.** *(carried, re-anchored)*
- Anchor: HY OAS **2.69%** (flat, **6bp off the 365-day low**), IG **0.78%**, NFCI **−0.552 loosening a
  5th straight week** and 1.2bp off its 120-day loosest `[FRED, 07-21/07-17]` — against a credit term
  bucket that is **still the fastest in the feed at 1.24×**.
- Direction: **no risk-off discount is warranted by the credit market.** Any credit-stress claim in
  this run is labelled **narrative-only** unless it cites HY OAS or NFCI. None does, so it is.
- **Both branches:** (a) spreads hold <3.00% → cyclicals and financials keep the benefit of the doubt;
  (b) **HY OAS >3.10%** (120d high 3.46) → the narrative was early and the whole earnings-now tilt is re-cut.
- **Anti-signal (kills P2):** HY OAS >3.10% on a close, **or** NFCI rising two consecutive weeks.
- KPI: HY OAS daily · NFCI weekly. Catalyst: FOMC 07-29 · PCE 07-30.
- ⚠ **New second-order test**: VIX went **16.64 → 19.13 (+15%)** intraday today while HY OAS's last
  print was flat. If tomorrow's HY OAS is still ~2.69% after a 15% VIX day, that is equity-only stress
  — a **dispersion event, not a credit event.** Pre-registered here so it cannot be re-read later.

**P3 — The AI-capex question resolved on volume and re-opened on price. It is now a MARGIN question.**
- Anchor: **GOOGL FY26 capex $195–205B, raised from $180–190B; Q2 capex $44.9B, +100% YoY**; management
  language *"supply-constrained environment"* `[M29, company]`. The market's reading is in the feed:
  *"Google's extreme AI capex spending plans trigger a technical [selloff]"* [4/2] and the 07-22
  cluster *"Google's profits are outrunning its AI spending boom"* [53 art / **18 outlets**].
  **Tesla guided capex >$25B** with Musk *"we should be spending on AI as fast as we can"* [5/4].
  Meanwhile the bear thread — *"AI investment boom puts Big Tech's FCF under pressure"* — is **FADING
  (5→2→6→3)** while the **AI-capex term bucket accelerated 1.09 → 1.22**. `[news]`
- Direction: **the volume leg is confirmed and is no longer the contested variable** (this is exactly
  what `STANDING_VIEW` §4 pre-registered: *a raise only moves the timing*). The contested variable is
  **whether the market pays for capex-funded growth**, which is a multiple question, not a demand one.
- **Both branches:** (a) MSFT+META raise on 07-29 and the complex holds its multiple → the spend is
  read as demand; (b) **they raise and the multiple compresses anyway** → capex is being priced as a
  margin drag, and the *suppliers* (memory, semicap, power) decouple from the *spenders*.
  ⚠ **Branch (b) is the one nothing in the book brackets** — it is the branch where a capex RAISE is
  bearish for the spenders and neutral-to-good for the chain. Handed to PREMORTEM.
- **Anti-signal:** a capex **cut** at MSFT or META → breaks the volume leg and the price leg together
  (the `STANDING_VIEW` §4 asymmetry), and extends past memory to NVDA/AVGO.
- KPI: MSFT + META capex lines **07-29**; then AMZN/AAPL 07-30.
- Catalyst: **INTC tonight (07-23 AMC — the equipment-leg test, S6)** · **MSFT + META 2026-07-29**.

**P4 — Energy escalated to PHYSICAL, and the war premium is now measurably HOSTILE to refining margin.**
- Anchor `[news, body-drilled]`: Houthis struck two named Saudi tankers (Encelia, Layla) and declared a
  **naval blockade at Bab el-Mandeb**, claiming **9 ships turned back**; the US ran its **12th
  consecutive** strike wave; the IRGC claims a tanker on fire **in Hormuz**; *Gulf producers race to
  build alternative routes* [5/4]; **EU agrees new Russia sanctions** [8/5]. Thread **BUILDING 11→9→9→12
  outlets into a partial day.** Earnings confirmation: **TotalEnergies +68%**, Equinor +93% (07-22).
- **Anchor `[measured, own calc]` — the part that cuts against the naive long:** WTI **+5.2%** (86.83 →
  91.37) while the **3-2-1 crack fell −11.2%** (66.86 → **59.36**) in the same session. The crack has
  now fallen **−$10.0 from its 07-16 peak of 69.45**, i.e. out of the 99.5th-percentile zone M22
  recorded. ⚠ 07-23 is an **incomplete bar**.
- Direction: **the crude leg and the refining leg have separated, and they are different positions.**
  A war premium raises the *input cost* of a refiner; it does not raise the *product* crack unless
  product supply is also hit. Three independent observations now (KR 07-22, US 07-22, US 07-23).
- **Both branches:** (a) the blockade holds and product supply is disrupted too → cracks re-widen and
  crude and refining re-converge; (b) **crude holds high while cracks keep compressing** → the refining
  node is a war-premium position wearing a crack-spread label, which is **exactly S8's registered
  distinction**, now with the evidence pointing at branch A of S8 (*against* us) rather than branch B.
- **Anti-signal:** the crack recovers >$68 while crude holds >$90 → the two legs re-couple and the
  margin thesis is intact; alternatively a Hormuz "open" statement collapses both at once.
- KPI: **3-2-1 crack daily (promoted to the primary KPI over crude)** · WTI COT %ile — **next print
  Friday 2026-07-24, S8's own registered cross-check** · XLE vs **SPY** (benchmark named, C1).
- Catalyst: **VLO earnings 2026-07-30** (D-7, dated — the refining read-through) · Hormuz statement `[blank]`.
- ⚠ **This proposition materially updates the desk's open contradiction C4.** The detachment counter
  was at 3; today adds a 4th and largest observation. **At 5 the equity is priced off something other
  than its KPI.** Not resolved here — counted.

**P5 — Tariff escalation: the thread ENDED and the pharma hit is UNCONFIRMED today. Re-justified, not carried.**
- Anchor: the tariff **term bucket is still fast (1.21×, 3rd)** — but the two threads that carried the
  07-22 read are both **ENDED**: *"Trump defends 50% tariffs on Canada"* peaked at **25 outlets** on
  07-21 and ended 07-22. **The 200% pharma-tariff event does not appear in today's head or body tier
  at all.** `[news]`
- ⚠ **C3 — this is a genuine "unknown", not an "absent".** 48.4% of today's clusters are in the
  unscoreable single-source tier, and the day is partial (361 vs 785 events). **The correct statement
  is "not confirmed today", not "faded".** The desk's own measured failure is a thread tag on a
  partial-day window.
- Direction: **Health Care carries a policy overhang that is dated-unknown**, plus the standing fact
  that it had the only negative Q2 EPS growth of the 11 sectors.
- **Both branches:** (a) implementation confirms → dated margin hit; (b) negotiated down or delayed
  (the repeated pattern) → an oversold defensive. **This is an oscillating policy variable; it is
  bracketed, and this run down-weights it because its threads ENDED.**
- **Anti-signal:** a formal pharma carve-out or delay → the UW is spent, revert to neutral.
- KPI: pharma sub-index vs **XLV**, XLV vs **SPY** (benchmarks named, C1) · the executive-order
  effective date. Catalyst: `[blank — not in the calendar; not guessed]`.

**P6 — Japan is still the un-priced global-duration channel, and it now has a DATE.** *(carried, upgraded)*
- Anchor: **"BOJ to raise rates again by December as a weak yen revives inflation"** [9 art/5 outlets,
  07-23] · *"Half of economists still see the BOJ waiting until December"* [2/2] · yen **near a 40-year
  low**, *"US-Iran tensions underpin dollar as yen nears 40-year low"* [7/4] · *"Japan's Katayama says
  will take necessary steps on for[ex]"* `[news]`. **The FX bucket reads 1.02 — the slowest on the
  board — because the story splits across three doors.** A measured under-read, second run running.
- Direction: a BOJ acceleration into a US real-yield 120-day high is the classic global term-premium
  transmission — through the JGB/carry channel, not the Fed.
- **Both branches:** (a) the BOJ accelerates → global long end sells off, compounding P1 branch (b);
  (b) the MoF intervenes on the currency instead → yen snaps, carry unwinds, and the **equity** leg is
  hit before the rate leg.
- **Anti-signal:** yen retraces below ~155 with no policy change → it was positioning, not policy.
- ⚠ **Still tagged `[unverified]` under rule W2** — *"BOJ tightening leads US long-end yields"* has **no
  lag table in this repo** (open dig **D22**). It is a channel to watch, **not evidence**, and DEEP/BET
  may not cite it. **Upgrade this run: the claim now has a testable date ("by December"), which is
  what W2 asks for** — but the lag table still does not exist, so the tag stands.
- KPI: USD/JPY · JGB 10y · DFII10 co-movement. Catalyst: next BOJ meeting `[blank]`.

**P7 — ★NEW · The regulatory tax on Big Tech is a separate, accelerating axis from the capex debate.**
- Anchor: **EU fines Google $1B over Play + €890m over search — 39 articles / 19 outlets, the #1 event
  of the day**, on a thread that has been the **fastest accelerator on the board for six days**
  (5→2→4→12→18→19). Alongside: *"China's Moonshot AI stole from Anthropic"* [6/6] · *"Democrats try to
  harness data-center backlash"* · the **OpenAI containment-breach thread peaking at 23 outlets** ·
  *"Anthropic to donate $20M to a US political group supporting AI regulation"* (07-22). `[news]`
- Direction: Comm Services and mega-cap IT carry a **policy cost that is not a rate story and not a
  capex story** — it is a third, independent channel, and it is the one currently getting the most
  editorial attention of anything on the board.
- **Both branches:** (a) fines stay one-off cash items → noise, and the multiple ignores them;
  (b) they arrive with **conduct remedies** (data sharing, store-rule changes) → a structural
  take-rate question, which is a multiple event rather than an earnings event.
- **Anti-signal:** the EU decisions are appealed and stayed with no conduct remedy → the axis reverts
  to a cash-item story.
- KPI: the **remedy text**, not the fine size · GOOGL/META regulatory disclosures · the AI-security
  thread's outlet curve.
- Catalyst: `[blank — appeal/remedy timetable not in the calendar; not guessed]`.
- ⚠ Registered partly because the desk's **cycle registry has no AI-security / regulatory row at all**
  (open dig **D20**), so **no GAP guard can fire against 0% exposure to it.** Flagged to PREMORTEM.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> Wind direction only, one line per GICS sector. **Not** an equal-weight analysis of 11 sectors.
> Every relative claim names its benchmark inline (**C1**). Flow tags are deliberately absent here —
> they are SWEEP's job and they are C-grade (**D6**).

| # | GICS Sector | Tilt | Δ vs 07-22 | Driving prop. | One-line why |
|---|---|---|---|---|---|
| 1 | **Energy** | **OW** | OW+ → **OW** | P4 | Escalation went **physical** (named tankers, Bab el-Mandeb blockade, 12th strike wave) into 10%ile COT — **but the 3-2-1 crack fell 11.2% the same session**, so the OW is on the **crude/integrated** leg, not automatically the refining leg. Downgraded a notch because its own margin KPI moved against it |
| 2 | **Financials** | **OW−** | OW → **OW−** | P1, P2 | Credit still refuses to confirm stress (HY 2.69%, NFCI loosening 5 weeks) and the front book is paid by a 120-day-high 2y — **but 2s10s FLATTENED today**, which removes the steepener leg the 07-22 OW rested on. Half the original reason is gone; the credit half is intact |
| 3 | **Info Tech** | **N** | N → **N** | P3, P7, P1 | Held flat a second run, now for a *different* reason: the binary that pinned it (GOOGL) resolved, and two new ones replaced it (**INTC tonight**, MSFT/META 07-29). Nasdaq COT 4%ile is cushion, not a reason (rejected-ledger guard) |
| 4 | **Comm Services** | **N−** | N → **N−** | **P7**, P3 | The **#1 event of the day is a $1.9B regulatory hit to the sector's largest constituent**, on the fastest-accelerating thread on the board — and the capex-as-margin-drag question is unsettled, not answered |
| 5 | **Industrials** | **N+** | N+ → **N+** | P4, S7 | **RTX backlog $289B (from $271B) and LMT a record $230.4B on $65B of quarterly orders (b:b ≈3.2×), both raising FY guidance** (§F). Saudi civil-nuclear + Westinghouse + Thales corroborate. Held at N+ not OW because M26 measured the sector as **two opposite things** (primes +0.250 flow vs capital goods −0.455) — W5 forbids one label |
| 6 | **Utilities** | **N−** | N− → **N−** | P1 | Bond proxy into a 120-day-high real yield *and* a 120-day-high 2y. Offsets (Saudi nuclear, AI power demand) are slower than the discount rate |
| 7 | **Real Estate** | **N−** | **UW → N−** | P1, R7 | ★ **Upgraded on a retraction, not on news.** R7 killed *"RE is the purest duration expression"*: the sector's RS20 leaders vs **SPY** are the classic-duration REITs (WELL +16.0, VTR +17.0) while the reds are **digital infrastructure**. A blanket UW is a third copy of an AI-datacenter short (M24 weak form). ROTATION must split the sector, not tilt it |
| 8 | **Health Care** | **N−** | **UW → N−** | P5 | ★ **Upgraded because the evidence weakened, not because the sector improved.** Both tariff threads **ENDED**; the 200% pharma event is **absent from today's tier** — and with 48.4% of clusters withheld that is an *unknown* (C3), not a fade. The standing negative-EPS-growth fact survives; the policy hit is unconfirmed |
| 9 | **Materials** | **UW** | UW → **UW** | P1, P5 | Copper **95%ile crowded-long** + DXY near range highs + a flattening front end. Unchanged |
| 10 | **Cons. Discretionary** | **N−** | N− → **N−** | P1 | The most rate-sensitive consumption there is, into a 2y at a 120-day high. Corroborated bottom-up: **Albertsons −20% on cut forecasts**, *"consumer discretionary stocks flash overbought"*, Tesla's robotaxi tone shift |
| 11 | **Cons. Staples** | **N** | N → **N** | P1 | Bond-proxy-adjacent multiple into rising real yields; ballast only if P1 branch (b) or VIX >24 trips. **VIX 19.13 intraday is the closest it has been** |

**Wind summary.** One clean OW (**Energy**, on the crude leg, with its own margin KPI flagged as
moving against it) and one softened OW (**Financials**, now carried by credit alone after the
steepener leg inverted). One clean UW (**Materials**). **Info Tech and Comm Services are pinned at
N / N−** — one earnings line (INTC tonight, MSFT/META 07-29) and one remedy text away from a rewrite.
**Two former underweights were upgraded to N− by this stage's own retracted ledger and denominator
discipline**, which is the intended behaviour of the HANDOVER stage and is recorded as such.

**DEEP candidates handed to ROTATION** (ROTATION owns the final pick):
**① Energy** — the crude/refining separation is the run's sharpest measured split (C4 counter now 4).
**② Industrials** — a same-day primes backlog record against a measured 0.705-point intra-sector flow
spread; W5 is pre-armed.
**③ Info Tech**, specifically the **semicap node (AMAT/LRCX/KLAC)** — §7 of HANDOVER found it has four
reports each and **no standing thesis**, and tonight's INTC print is its registered test (S6).
**④ Comm Services / mega-cap IT under P7** — the fastest thread on the board with no cycle-registry row.
**Financials** is flagged as the pre-mortem swing (the steepener leg just inverted under it).

---

## §F · Same-day earnings already printed (pre-market 07-23) — the S7 observable

Recorded here because MACRO ran after the prints and before the open; scored in `HANDOVER.md` §3.

| Name | Backlog | Orders | Guidance | Q2 |
|---|---|---|---|---|
| **RTX** | **$289B** (commercial $170B / defense $119B), from **$271B** | — | **Raised**: FY26 adj. revenue **$95–96B** (prior ceiling $93.5B) | Sales **$24.7B, +14% YoY**; non-GAAP EPS **$1.89** (+$0.23 vs street) |
| **LMT** | **$230.4B — a record** | **$65B new orders** on $20.1B sales ⇒ b:b ≈ **3.2×** | **Raised**: FY26 sales **$79.75–81.75B** (prior $77.5–80.0B); FCF >$7B | Sales **$20.1B, +11% YoY**; **Missiles & Fire Control +19%** (PAC-3/THAAD/PrSM) |

⚠ **Data trap logged (new dig D29)**: a nasdaq/Zacks item dated **today** reports RTX at *"$1.41 EPS,
quarter ended June 2024, revenues $19.72 billion"* — a **recycled 2024 template under a 2026 date**,
contradicting the actual print. Any stage quoting a Zacks-syndicated earnings body must check the
quarter label **inside** the text.

---

## §G · Self-backtest

**Running hit-rate: 0 scored / 0 scoreable.** The first US propositions were registered **2026-07-21**;
the +7d window opens **2026-07-28**, +14d **2026-08-04**, +30d **2026-08-20**. Nothing is scored today
without manufacturing a horizon, and that is not done here (P4).

### +1d kill-line audit of the 07-22 propositions (a state check, not a score)

| 07-22 prop | Kill line | State 07-23 | Status |
|---|---|---|---|
| **P1** long-end move is real-rate | real 10y **>2.55%** | real **2.37%** (was 2.35) = 120d high; **18bp of room** | Un-tripped — **but its *composition* claim partly reversed**: 2s10s flattened and the 2y made a 120d high. The 07-22 text said "bear-steepening, term premium, not cut-pricing." **On today's tape that is wrong.** Corrected in this run's P1, and logged as the first substantive prop correction the desk has made on its own tape |
| **P2** credit narrative ≠ credit market | HY OAS **>3.10%** | **2.69%**, flat, NFCI loosening a 5th week | Un-tripped, moving the same way. **The strongest-standing proposition on the board** |
| **P3** AI capex resolves on the capex line | capex **cut** | **GOOGL raised to $195–205B**; TSLA guided **>$25B** | ★ **Resolved on the pre-registered line item, in the pre-registered direction.** And the pre-commitment held in the wild: the stock reportedly *fell* on the raise. The prop's own rule — score the observable, not the reaction — is what let it be scored cleanly |
| **P4** energy war premium, bracketed | WTI COT >40%ile **and** crude below range | COT unchanged 10%ile (same print); WTI **+5.2%**, physical escalation | Un-tripped on its stated line — **but its unstated assumption broke**: the crack fell 11.2% the same session. **P4 is rewritten this run to make the crack the KPI instead of crude.** This is the recurring failure class the stage is told to guard: a one-sided read of an oscillating variable, where the oscillation was in the *margin*, not the *price* |
| **P5** tariffs are a sector-specific tax | pharma carve-out/delay | Both threads **ENDED**; the pharma event absent from today's tiers | **Weakened, and down-weighted rather than carried.** ⚠ Absence under a 48.4%-withheld tier is `unknown`, not `resolved` (C3) |

### Failure classes logged this run

1. **A one-sided read of an oscillating variable — caught again, in a new place.** P4 bracketed the
   *crude price* both ways and left the *refining margin* unbracketed. The oscillation happened in the
   unbracketed variable. **Bracket the KPI, not just the headline price.**
2. **Partial-day windows inflate FADING** — carried from 07-22 and it fired again: every oil thread
   tags FADING on a 361-event day while oil is the #2 head event at 16 outlets and the Houthi
   successor thread is **BUILDING into the same partial day**.
3. **NEW — a `[measured]` claim can decay into a `[stale]` one inside 48 hours without changing its
   text.** M20's "79% of the move is real" was true of the 20-session window and is being read as a
   statement about *now*. The fix used here: quote the **20-session** and **last-observation**
   decompositions as separate rows (§A-1), so the horizon is visible in the number.
4. **NEW — provider disagreement on a price series** (`BZ=F` printing below WTI). Registered as **D30**.

---

## §H · Rule-linter result

`python -X utf8 scripts/report_lint.py llm_outputs/2026-07-23/industry_US/MACRO_REPORT.md` — see the
run log. ⚠ The linter checks **form only** (C1 benchmark presence · C2 both halves · S6 future labels ·
D6 OBV-alone). **A clean run is not a correct report**, and it is not treated as one here.

---

## §5 · DRIFT ADDENDUM

> **APPEND-ONLY** (Stage 10/10). §0–§H above are **not edited** — the original call stays visible next
> to its correction, because that asymmetry is what the self-backtest eats.

### Run clock of this addendum: 2026-07-24 00:1x KST = 2026-07-23 11:1x ET

The US regular session **has now opened** (baseline §A–§H was written pre-open). ⚠ This addendum still
does not use intraday prices as closes — it reads the **narrative** axis only, which is what the stage
is for.

### ⚠ Tool failure disclosed first (P4) — and the HANDOVER's own caveat is what caught it

`scripts/drift_watch.py` **could not run**:

```
drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```

★ **This is a sharper diagnosis than dig D17 currently carries, and it reverses a provisional call
made earlier in this same run.** HANDOVER §8 recorded *"D17 appears CLOSED — `drift` is now present in
`module_news_data.__main__.DB_READ_CMDS`; DRIFT must verify it actually executes remotely before the
fix is declared."* **That verification just failed.** The local file does list `drift`; the **server's
copy does not**, because per CLAUDE.md **P6** a change to `DB_READ_CMDS` needs the server to `git pull`
and restart its API, and that has not happened. **The fix was made client-side and never propagated.**

⇒ **D17 is NOT closed.** Its correct statement is now: *"`drift` is in the client's allowlist and
absent from the running server's — the client-side edit was never deployed."* That is a one-command
fix for a human (server `git pull` + API restart), not a code change.

### Substitute used, with its arithmetic stated

The module's own **20 `KILL_TERMS`** (`module_news_data/_drift.py:38`) run through the **allowed**
`fts search --count`, 1-day vs 7-day, `--scope foreign`. ⚠ The raw d1/avg7 ratio is **not** the burst —
the pool itself grew. Measured pool denominators: **1-day foreign = 10,488 articles**, **7-day =
26,437 (avg 3,776.7/day)** ⇒ **the pool's own d1/avg7 baseline is 2.777×.** Every ratio below is
divided by that. Anything near 1.0 is moving **with** the feed, not bursting.

⚠ **A methodology correction that matters for comparing to yesterday.** Run first in `--mode and`
(each word matched anywhere in the body) the counts came out 40× larger than the 07-22 table's — which
would have read as an enormous burst and would have been **an artifact of the query, not the news.**
Re-run in **phrase mode**, which is what the 07-22 run used, the numbers are directly comparable. **The
phrase-mode figures are the ones reported.** Logged as a lesson: a drift substitute must replicate the
*query form* of the baseline it is compared against, or it manufactures its own alarm.

### Result: ✅ **NO DRIFT.** Both of yesterday's 🚨 flags have decayed.

| Kill term (phrase mode) | d1 | d7 | raw d1/avg7 | **÷ 2.777 pool baseline** | vs 2026-07-22 |
|---|---|---|---|---|---|
| **new tariff** | 43 | 102 | 2.95× | **1.06×** | ★ **1.77× 🚨 → 1.06×** — the burst decayed |
| **ceasefire** | 137 | 446 | 2.15× | **0.77×** | ★ **1.31× 🚨 → 0.77×** — now the *slowest* major term |
| Strait of Hormuz | 425 | 1,028 | 2.89× | **1.04×** | 0.96× → 1.04×, flat |
| guidance cut | 8 | 14 | 4.00× | 1.44× | ⚠ **n = 8 — indistinguishable (C4/S3)**, not a burst |
| **capex cut** | **0** | **1** | — | — | ★ **0 → 0. See below.** |
| emergency FOMC · circuit breaker · flash crash | 11 · 9 · 9 (AND-mode) | — | — | — | **n ≤ 11 — indistinguishable** |
| blockade · invasion · state of emergency · rate hike · rate cut · default · downgrade · bankruptcy · export ban · strikes on Iran · emergency meeting · Hormuz closed | — | — | 2.7–3.4× (AND-mode) | **0.98–1.12×** | All **at or below** the pool |

**Nothing crosses the 1.3 flag on a sample large enough to read.** The report does not go stale
overnight on the narrative axis.

★ **The decay of "ceasefire" is itself informative and cuts the same way §D-P4 already reads.**
On 07-22 the "ceasefire" burst was body-read and found to be an **escalation** burst wearing a peace
word. Today it is the slowest term on the board — because the story has stopped being *about* a
ceasefire at all. §C-3's Houthi/Bab el-Mandeb thread is **BUILDING (11→9→9→12 outlets) into a partial
day**, and the physical facts (two named tankers struck, a declared naval blockade, nine ships turned
back, a 12th consecutive strike wave) have replaced the negotiation frame entirely. **Attention
rotated within the story, not away from it** — the same pattern §C-3 flagged on the older oil thread.

### ★ The finding that matters most: **open contradiction C6 still stands, one day later**

`handoff/STANDING_VIEW.md` **C6 — "the un-narrated branch"** was logged on 07-22 because
**`"capex cut"` had 0 mentions in 24 hours** across the foreign feed while the market priced a ±7.1%
move into GOOGL and cut near-term estimates 4:1.

**Measured again today, same query form: `"capex cut"` d1 = 0, d7 = 1.** Alphabet then **raised** capex
to $195–205B (**S1 FIRED-A**) and **the stock fell**. So:

> **The market has now demonstrably priced capex-as-margin-drag — while the phrase for that branch
> has appeared zero times in 24 hours and once in 7 days across the entire foreign feed.**

**Absence of narrative is not evidence of absence** — the desk's own measured precedent is the KOSPI
−8% circuit-breaker day, which ranked **nowhere** on term velocity. C6 was logged precisely so that if
this branch fired, the record would show it was un-narrated beforehand. **It fired, and the record
shows exactly that.** This is now the direct empirical justification for **S13** (registered this run,
2026-07-29): a capex **raise** priced as a margin drag is the branch nothing in the book bracketed, and
the news feed cannot see it coming — so it must be bracketed on **observables**, never on narrative.

### What is NOT covered by this addendum

- **Price drift.** The US session opened at 09:30 ET; §A's FRED tape stops at 07-21 and §A-2's
  intraday quotes were unfinished bars. **Whether today's 10y move (nominal 4.71%, a 6-month high on
  a +5.2% crude day) was real-rate or breakeven remains unmeasurable** until FRED publishes — stated
  in §A-2 and still true. **First scoreable next run.**
- **The 48.4% withheld single-source tier** (352 of 728 clusters) is unscoreable on `--scope foreign`
  because the classifier is Korean-only. A drift term sitting only in that tier would not be seen by
  this sweep either.
- **INTC prints after today's close and the ECB decision lands today** — both after this addendum's
  clock. They are bracketed (**S6**, **S12**) rather than watched.
