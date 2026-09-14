# MACRO_REPORT — industry_US — 2026-07-24 (Fri)

> Stage 2/10 (MACRO) of protocol `industry_us`. English-pure runtime, `--market us`, news `--scope foreign`.
> Purpose: falsifiable macro propositions → **★sector transmission matrix** (ROTATION's input).
> Zero buy/sell. Primaries `[FRED]` > narrative `[news]`. Every line carries its `asof`.
> **Run clock: 2026-07-24 22:09 KST = 09:09 ET — the US 07-24 regular session has NOT opened.**
> Continuity anchor: `llm_outputs/2026-07-23/industry_US/MACRO_REPORT.md` + today's `HANDOVER.md`.

★ **What makes this run different from the last two.** Both prior US runs fired at ~09:1x ET and
therefore wrote on a stale close. **Today the 2026-07-23 session has settled**, and it is the most
informative session on the board — the one the 07-23 US run predicted and could not see, and the one
the 07-24 KR run saw only through a KR lens. **Reading it settles two registered scenarios' direction
and retracts one of yesterday's own headline measurements.**

---

## §0 · Catalyst injection `[catalyst_calendar --days 10]`

Pulled at **10 days, not the default 5** (dig D26's standing correction — `SCENARIOS.md` names 07-29,
07-30 and 07-31, all unreachable from 07-24 at `--days 5`). **10 binary catalysts in window.**
Saved to `llm_outputs/2026-07-24/CATALYST_WATCH.json`.

| When | Event | Axis |
|---|---|---|
| **D-5 2026-07-29** | **FOMC decision (Warsh, no SEP)** | rates 🔀 |
| D-5 2026-07-29 | META earnings · SK hynix ADR share-registration · KR financial-holdco governance reform | AI capex / KR |
| **D-6 2026-07-30** | **June PCE** · VLO earnings · STNG earnings · MA earnings | inflation / Energy / Financials 🔀 |
| D-7 2026-07-31 | SK이터닉스 KKR SPA closing | KR |
| undated | Iran "Strait of Hormuz open" statement | oil 🔀 `[blank — not guessed]` |

### ⚠ D18 fires a **FIFTH** consecutive time — and this time it is the largest print of the week

| Absent from `CATALYST_WATCH.json` | Why it is a binary | Independent evidence it is real |
|---|---|---|
| ★ **MSFT earnings (2026-07-29 or 07-30)** | **Half of `S13`'s cross-condition** — the desk's own highest-information registered bracket — and the largest-cap print of the window | Feed 07-23: *"Microsoft expands Mistral partnership with multibillion…"* thread live 7 days; `yfinance.calendar` returns **2026-07-30** |
| **AMZN (07-30)** | `S2` explicitly says *"Partial; wait for AMZN + AAPL (07-30)"* | Feed: *"With Amazon scheduled to report earnings on **July 30**…"* [fool + yahoo_finance, 07-23]; *"Alphabet Just Tied Amazon's $200 Billion Capex Guidance. Could Amazon Raise the Bar Even Higher on **July 30**?"* |
| **AAPL (07-30/31)** | ditto | `yfinance.calendar` **2026-07-31** |
| **UPS (2026-07-28)** | **Dig D23's last unread refiner customer** — the W4 test the desk has left open two runs | `yfinance.calendar` **2026-07-28** |

★ **The escalation is qualitative, not just another tally.** 07-22 missed GOOGL; 07-23 missed INTC and
the ECB; **today it misses the single largest earnings print in the window, which is also a named leg
of a registered scenario.** A `--days 10` pull was used (D26's fix) and did not help — consistent with
the 07-23 diagnosis that the defect is **source coverage of single-name earnings**, not window length.
⇒ **All four handed to PREMORTEM as mandatory both-sides brackets.**

### ⚠ Provider disagreement on the earnings dates themselves — declared, not silently resolved (rule D5)

| Source | META | MSFT | AMZN | AAPL |
|---|---|---|---|---|
| `catalyst_calendar` | **07-29** | *(absent)* | *(absent)* | *(absent)* |
| News bodies (`--scope foreign`) | **07-29** (*"an Announcement on July 29"*, fool/yahoo 07-21) | — | **07-30** (2 outlets, 07-23) | — |
| `yfinance.calendar` | **07-30** | **07-30** | **07-31** | **07-31** |

Two independent sources say META 07-29 and AMZN 07-30; `yfinance` sits **one day later on all four**,
i.e. it is the outlier and looks systematically offset. **The registered scenario dates (S2/S13/S16 =
07-29) are NOT rewritten on a single disagreeing provider.** Logged as a new dig (**D47**) because the
"six triggers stacked on 07-29" framing depends on it: if the mega-cap prints are actually 07-30, the
stack **splits across two days** and 07-30 (PCE + MSFT + META + MA + VLO) becomes at least as loaded.

---

## §A · Regime primaries `[FRED]` — 120-day window, pulled this run

| Series (FRED id) | Latest | Δ prev obs | Δ ~20 obs | Read | Freshness |
|---|---|---|---|---|---|
| Fed Funds eff (DFF) | **3.63%** | flat | flat | Policy on hold — into a meeting the market no longer reads as "hold" (§C-1) | daily, asof **07-22** |
| **10y Treasury (DGS10)** | **4.67%** | **+4bp** | **+21bp** (4.46) | ★ **120-day HIGH** (window max = 4.67) | daily, asof **07-22** |
| **2y Treasury (DGS2)** | **4.31%** | **+5bp** | +8bp | ★ **120-day HIGH** (window max = 4.31), second consecutive session at a new high | daily, asof **07-22** |
| **2s10s** (derived) | **+0.36** | **−1bp** | +13bp | ★ **Flattening continues** — a second consecutive session. R11 stays dead | derived |
| **Real 10y (DFII10)** | **2.39%** | **+2bp** | +18bp (2.21) | ★ **120-day HIGH** (window max = 2.39). **16bp below P1's 2.55% kill line** | daily, asof **07-22** |
| **10y breakeven (T10YIE)** | **2.28%** | flat | +5bp (2.23) | 120-day range [2.18, 2.50] — **still nowhere near the top** | daily, asof **07-23** |
| Core CPI (CPILFESL) | **YoY +2.57%** · **MoM −0.02%** | — | — | Both halves quoted (**C2**) | monthly, asof **Jun — 1-month lag** |
| Headline CPI (CPIAUCSL) | **YoY +3.46%** · **MoM −0.42%** | — | — | Both halves quoted (**C2**) | monthly, asof **Jun — 1-month lag** |
| Unemployment (UNRATE) | **4.2%** | −0.1 MoM | — | 120d range [4.1, 4.5]. Not cracking | monthly, asof Jun |
| DXY Broad (DTWEXBGS) | **120.5315** | **unchanged since 07-17** | +1.14 | Upper half of [117.44, 121.41] | daily, asof **07-17 — 5 business days stale, see §A-3** |
| VIX (VIXCLS) | **16.64** | −0.41 | −1.72 | ⚠ **Superseded by the tape** — `^VIX` settled **18.70** on 07-23 and **18.94** pre-open today | daily, asof **07-22** |
| **HY OAS (BAMLH0A0HYM2)** | **2.68%** | **−1bp** | −1bp | **5bp off the 365-day low (2.63)**; 120d max 3.46. **A new post-window low tick** | daily, asof **07-22** |
| **IG OAS (BAMLC0A0CM)** | **0.78%** | flat | flat | 120d range [0.73, 0.94]. No stress at investment grade either | daily, asof **07-22** |
| **NFCI (Chicago Fed)** | **−0.552** | −0.013 | −0.041 | **Loosening a 5th straight week**, 1.2bp off its 120-day loosest (−0.564) | weekly, asof **07-17** |
| M2 (M2SL) | **$23.05T** | +1.09% MoM | +5.1% YoY | Both halves quoted (C2) | monthly, asof May |

⚠ **Freshness (P4)**: FRED daily series stop at **07-22** (breakeven alone has 07-23). **Nothing in the
FRED column reflects the 07-23 close or today's pre-open.**

### §A-1 · The tape moved past FRED again, and in the same direction

`^TNX` (yfinance, settled): **07-22 4.657 → 07-23 4.703 → 07-24 pre-open 4.683.**
⇒ The 10y made **another new high on 07-23**, one FRED has not yet published. Nothing in §A is
directionally contradicted by the tape this run — unlike 07-23, when it was.

**The decomposition, both horizons quoted so the window is visible in the number** (the fix logged as
failure class 3 by the previous run):

```
20-session : 10y +21bp   breakeven +5bp   real +18bp   →  ~86% real-rate driven
last obs   : 10y  +4bp   breakeven  0bp   real  +2bp   →  ~100% real / term, zero inflation-expectation
front end  : 2y  +5bp = 120-DAY HIGH, again outpacing the 10y  →  2s10s flattened a 2nd session
```

★ **Read this next to §C-1.** A front end at a 120-day high with breakeven *flat* is not the market
pricing more inflation — it is the market pricing a **more hawkish reaction function**. That was P1's
claim on 07-23 and it survives on today's numbers. **But §C-1 supplies a third reading that neither
R11 nor P1 contained, and it has a named primary-dealer source.**

### §A-2 · Credit: not merely unstressed — it made a new low tick into all of it

HY OAS **2.68%, −1bp**, on a session (07-22) followed by an equity day of **S&P −1.21% / Nasdaq
−2.15%**. IG flat at 0.78%. NFCI loosening a 5th week. **This is the fifth consecutive run in which
every credit series refuses to confirm any of the risk narratives running above it.**
⚠ The pre-registered second-order test from 07-23 — *"if HY OAS is still ~2.69% after a 15% VIX day,
that is equity-only stress, a dispersion event not a credit event"* — **has now been half-answered**:
VIX settled 18.70 (from 16.64) and HY **fell** a basis point. The other half (HY's 07-23 print) is not
yet published; **score it next run rather than declaring it now.**

### §A-3 · DXY has not printed for five business days — and that is a scenario problem, not a data note

`DTWEXBGS` reads **120.5315 asof 2026-07-17**, byte-identical to its value when **S12** was registered
on 07-23. The 120-day range is confirmed unchanged at **[117.4396, 121.412]**.
⇒ S12 remains **PENDING**, re-check deadline **07-28**, and its construction defect is now registered
as **D46** (a 3-session invalidation window written on a series with a ~5-business-day lag).
**No proxy is substituted** (rule D5 / L3's own rule). The narrative that *would* move it is visible
and was found only in the withheld single-source tier: *"US Dollar Index: Higher yields and FOMC focus
lift DXY"* [fxstreet, 1 outlet] — i.e. **directionally toward branch B, unscoreable, and stated as such.**

---

## §B · Positioning `[COT, CFTC]` — the 07-24 print, which is S8's own registered cross-check

| Instrument | Net-spec | Wk Δ | 1yr %ile | Tag |
|---|---|---|---|---|
| **WTI Crude** | +19,783 | −1,139 ▼ | **10%ile** | 🔴 crowded-**short** |
| Nat Gas | −178,612 | −13,305 ▼ | **6%ile** | 🔴 crowded-short |
| **Nasdaq-100** | −10,313 | −1,572 ▼ | **4%ile** | 🔴 crowded-short |
| **Copper** | +64,385 | +113 ▲ | **95%ile** | 🟢 crowded-long |
| S&P 500 e-mini | −38,938 | +3,953 ▲ | 78%ile | neutral |
| UST 10Y | −831,675 | −17,413 ▼ | 22%ile | neutral |
| UST 2Y | −1,157,477 | +103,531 ▲ | 52%ile | neutral |
| USD Index | +13,173 | −96 ▼ | 58%ile | neutral |
| Gold | +186,682 | −7,564 ▼ | 23%ile | neutral |

★ **S8's registered cross-check ("WTI COT %ile, next print 2026-07-24") is delivered: 10%ile, and it
did not move** — speculators got **shorter** (−1,139) into a week in which Brent settled through $100.
⚠ **Context only, never a trigger.** "COT crowded-long contrarian" sits on this repo's **REJECTED**
signal list; the percentile is squeeze *fuel conditional on a turn being visible*, not a direction.
⚠ Tuesday close, 3–4 day lag.

---

## §C · Narrative axis `[news, --scope foreign]`

**Denominator, corrected and quoted in full (P4).** `brief --body 2 --scope foreign`, 2026-07-24:
**2,176 articles → 731 clusters → 350 events (all 350 classed market)**, head **37** / body **313** /
tail **0** · **subevents recovered 71** · `excluded_not_news` **{} (empty — the furniture detector is
domestic-only)**.
⚠ **`tail = 0` is NOT the coverage claim.** `single_source_clusters` = **381, of which 15 shown ⇒ 366
withheld**, and on `--scope foreign` those rows are **scoreless** (`nb: null` — the classifier is
Korean-only), so their absence is *not measured*, it is *not measurable*. `excluded_nonmarket` = 0/0.
**Every "quiet in bucket X" claim below is therefore stated against 366 unscoreable withheld rows.**
⚠ Today's article count (2,176) is a **partial day** — 07-21/22/23 ran 948/812/840 *events*; today's
per-day event count in the thread view is **350 vs 840 yesterday**. **This mechanically inflates
FADING**, and that warning is applied literally below rather than quoted and ignored.

### §C-1 ★★ The day's regime item: the bond market flipped to pricing a **HIKE** — and no registered scenario brackets that

Head tier, [8 articles / 7 outlets]: *"The Probability of a July Fed Rate Hike Has Tripled Over the
Last Week"*, with a `└` sub-event *"Bond Market Just Flipped to 'Rate Hike in July' as 2-Month…"*.
Thread status **REIGNITED, 4→7 outlets.**

**Body-drilled numbers** (`fts … --full`; CME FedWatch, quoted inside the body):

| Date | Implied probability of a **hike** at the 2026-07-29 FOMC |
|---|---|
| 2026-07-15 | **10.7%** |
| 2026-07-22 | **34.7%** (a second line in the same body gives 31.5%) |

The same body independently confirms the 07-23 US close — **Dow −0.97% · S&P 500 −1.21% · Nasdaq
Composite −2.15%** — which matches this run's own yfinance pull exactly, so the source is not a
recycled template (the **D29** check applied and passed).

★ **The named driver is OIL, not core inflation** — TD Securities, 07-23, body-read:
> *"Pricing for rate hikes moved alongside oil heading into the June CPI report… the longer energy
> shocks persist, the more markets will become worried about the Fed reacting."*

and, on the size of the dislocation:
> *"If current pricing persists into next week's FOMC decision, it would be the **second-largest
> deviation between market pricing and actual Fed action in the past decade**… we believe the pricing
> for July remains excessive and maintain a receive July OIS position."*

Corroborated from a second desk — Deutsche Bank via fxstreet, 07-22: *"despite higher US Treasury
yields and renewed speculation about a July Fed rate hike, US equities advanced, led by a strong
recovery in chip stocks. The Philly Semiconductor Index posted its best daily performance in a month…
markets simultaneously priced a more hawkish Fed path as real yields hit multi-year highs."*

⚠⚠ **This is a scenario-coverage failure, and it is the same class as D35.** `S9`'s grid runs
real 10y **>2.55% (hawkish)** / **<2.20% (dovish)**; `S2` branch C says *"either cuts, or real 10Y
closes >2.55%"*. **An actual rate HIKE — now a ~1-in-3 market-priced outcome five days out — appears
in no branch of any registered scenario.** Handed to PREMORTEM as the run's first mandatory bracket.

### §C-2 ★★ C6 re-measured: the branch is still un-named, but it has acquired a **vocabulary**, and it is not the desk's

Same query form as M46, `--scope foreign`, pool-normalized (pool d1 = 9,504 vs d7/7 = 3,898 ⇒ the
pool itself runs **2.44×** today, so raw velocities are divided by 2.44 before they mean anything):

| Term | d1 | d7 | raw | **pool-normalized** |
|---|---|---|---|---|
| **`free cash flow`** | 558 | 1,138 | 3.43× | **1.41× ★ fastest on the board** |
| **`capex`** | 416 | 853 | 3.41× | **1.40× ★** |
| `backlog` | 341 | 735 | 3.25× | **1.33×** |
| `tariff` | 647 | 1,479 | 3.06× | 1.26× |
| `earnings` | 3,680 | 8,804 | 2.93× | 1.20× |
| `rate hike` | 275 | 681 | 2.83× | 1.16× |
| `credit` | 818 | 2,288 | 2.50× | 1.03× |
| `hyperscaler` | 360 | 1,004 | 2.51× | 1.03× |
| `inflation` | 851 | 2,423 | 2.46× | 1.01× |
| `Iran` | 961 | 2,937 | 2.29× | 0.94× |
| `Fed` | 356 | 1,114 | 2.24× | 0.92× |
| `memory` | 420 | 1,330 | 2.21× | 0.91× |
| `semiconductor` | 542 | 1,750 | 2.17× | 0.89× |
| `recession` | 95 | 326 | 2.04× | 0.84× |
| **`capex cut`** | **0** | **1** | — | **0.00×** |
| **`margin drag`** | **0** | **1** | — | **0.00×** |

★ **The finding, and it is a refinement of C6 rather than a third repetition of it.** `capex cut`
remains literally zero for a **third consecutive measurement** — but the **two fastest terms in the
entire sweep are `free cash flow` and `capex`**, and the head/thread tiers name exactly what they are
being used to say:

- *"Google's profits are outrunning its AI spending boom"* — peaked **16 outlets**, thread 2→4→12→16→14→2
- *"Alphabet's cash burn raises alarm for Big Tech as AI s[pending]…"* [5→2→6→3]
- *"CapEx Is Exploding as Alphabet Goes On a Spending Spree"* [4→3]
- *"Analysis: AI investment boom puts Big Tech's free cash [flow under pressure]"* — **REIGNITED 3→6→3**
- *"Japan's Nikkei falls more than 2% on **AI spending worries**"* [4/4] · *"FTSE 100 Live: London stocks
  called lower as **Big Tech burn**…"* [2/2] · *"Why Most AI Projects Will Fail"* [11 art/**8 outlets**]

⇒ **The market is narrating capex-as-cash-consumption, not capex-as-cut.** That is precisely S13's
branch-A/B distinction, arriving *before* the 07-29 event. **Operational consequence: tracking this
branch on the frozen phrase `"capex cut"` measures the wrong thing.** The economic content lives in
`free cash flow` / `cash burn` / `AI spending worries`. **C6's original logging is vindicated — absence
of the phrase was never absence of the branch — and the tracking term is corrected here.**

### §C-3 · The rest of the day, by tier (every head line read, not the top of it)

**Head (37 events, ≥5 outlets)** — the ones that transmit:

| Event | Outlets | Transmits to |
|---|---|---|
| *Oil set for weekly rise amid Red Sea shipping attacks, Kazakh[stan]* | **11** | Energy — the day's #1 |
| *China slaps export controls on 14 EU entities in retaliation* | 9 | Materials, IT supply chain |
| *Trump's latest tariff tantrum unlikely to end well* / *US imposes new tariffs on dozens of trade partners over 'forced labor'* (60 countries; Singapore 12.5%) | 9 / 7 | Cross-sector — **S10's US-side print** |
| *Trump weighs 'massive attack' on Iran as Tehran's chokehold…* + *US launches new strikes on Iran over shipping routes* | 9 / 6 | Energy 🔀 |
| ★ *Big Banks Are Wading Back Into Commercial Real-Estate Lending* | **9** | **Financials + Real Estate** — thread **BUILDING 5 days** (5→7→3→5→9) |
| *Oil Tops $100 as Supply Crisis Deepens* / *Iran war pushes Brent to $100* | 7 | Energy — **confirmed on the settled tape, §D-P4** |
| ★ *The Probability of a July Fed Rate Hike Has Tripled* | 7 | **Everything** — §C-1 |
| ★ *Intel rises as strong forecasts signal AI boost for turnaround* + `└` ***"AMSL, AMAT, KLAC, LRCX: Chipmaking Equipment Stocks Rise"*** | 6 | **Info Tech — S6's transmission, §D-P3** |
| *ECB officials confirm: Eurozone inflation to stay above target* + `└` *"Still see probability of rate hike higher than hold"* | 7 | **S12** — the ECB held **hawkish**, feeding D35 |
| *Stocks suffer fresh blow as markets hit by perfect storm* / *Asian stocks fall on tech selloff* / *Japan's Nikkei falls >2% on AI spending worries* | 6 / 4 / 4 | Global risk |
| *Latest News In AI Chips — AMD and Cerebras Team Up* · *AMD reveals CPU roadmap through 2028* | 8 / 4 | IT |
| *Why Tesla Stock Crashed Today* + *Tesla's Operating Margin Just Fell to 1.4% and FCF…* | 5 / 4 | Cons. Discretionary |
| *TikTok charged with breaching EU rules on online safety* | 6 | **Comm Services — P7's axis, a second constituent** |
| *Japan inflation rises to 1.6% in June: Why the weak yen coul[d]…* | 5 | **P6 / dig D22** |
| ★ *Stripe Plans to Acquire PayPal for $53 Billion* + *Berkshire Hathaway Sold Mastercard Stock* | 4 / 3 | **Financials — S14's exact node** |
| *US Investors Are Doing Something They've Never Done Before* / *The bond market is telling investors it's time to start…* / *Investors fear Japanese bond bets risk becoming new 'widowmaker'* | thread **BUILDING 4 days** | Rates |

**Withheld single-source tier (366 rows unshown, scoreless)** — the 15 sampled included
*"ORCL Stock Rises After-Hours On Pentagon Deal Worth Up To…"* [yahoo_finance] and
*"US Dollar Index: Higher yields and FOMC focus lift DXY"* [fxstreet]. **Both are transmission-grade
and neither appeared in any other tier** — the L3's own warning about where rates/FX/defence primaries
hide, reproduced verbatim on the US feed.

**Blind-spot pass** (`blindspot --sample-pct 25 --days 3 --scope foreign`, 23,484-article blind pool,
5,871 sampled). Token-0 emergent list is dominated by structural furniture (`Earnings` 2,212, `AI`
1,924, `Results` 737). **Two raw sample rows are new transmission terms and are folded into the term
table below**:
- ★ *"Treasury market signals that **7% rate on 30-year mortgage** could be next"* [marketwatch, 07-23] —
  a rates→housing→consumer channel **no proposition in this file has carried**.
- *"House passes stopgap bill to fund the govt through early December"* [investing_en, 07-22] — removes
  a shutdown tail through December; also **absent from every scenario**.

**Living term table, terms added this run**: `free cash flow` · `cash burn` · `AI spending` ·
`rate hike` · `30-year mortgage` · `stopgap`. **Term removed as a tracking proxy**: `capex cut`
(kept as a *falsifier* for the anti-signal, dropped as a *tracking* term — §C-2).

---

## §D · Macro propositions — falsifiable · both branches · anti-signal · KPI · dated catalyst

**P1 — The front-end repricing is a reaction-function trade whose *trigger* is oil, not core inflation.**
*(carried from 07-23, and materially sharpened — this is a third framing, not a restatement)*
- Anchor `[FRED, 07-22]`: **2y 4.31% = 120-day high** (+5bp) outpacing 10y **4.67%** (+4bp) ⇒ **2s10s
  +0.36, flattening a second consecutive session**; **real 10y 2.39% = 120-day high**; **breakeven
  2.28%, flat**. Against **core CPI −0.02% MoM / +2.57% YoY** and **headline −0.42% MoM / +3.46% YoY**
  (both halves, **C2**), unemployment 4.2%. Tape confirms and extends: `^TNX` **4.703 on 07-23**.
- Anchor `[news, body-drilled]`: CME FedWatch hike odds **10.7% (07-15) → 34.7% (07-22)**; TD Securities
  names the mechanism — *"pricing for rate hikes moved alongside oil"* — and calls July pricing
  **excessive**, *"the second-largest deviation between market pricing and actual Fed action in the
  past decade."* Thread **REIGNITED 4→7**.
- ★ **What is new versus 07-23**: P1 said "reaction function, **not** an inflation trade." Today's
  primary-dealer evidence says it is a reaction function **to an inflation impulse the printed data
  does not yet contain** — an oil pass-through fear. **Both prior framings were incomplete**: R11's
  term-premium read is dead (2s10s flattened twice), and P1's clean "not inflation" is now
  **half-right** — the *expectation* series (breakeven, flat at 2.28%) supports it, the *narrated
  cause* (oil) does not.
- Direction: **fewer-cuts-or-a-hike pricing taxes long-duration multiples and the rate-sensitive
  consumer; it pays the front-book earners** — but the trigger being oil means **the same shock that
  drives it also drives the Energy OW**, which is a correlation the book has not priced.
- **Both branches (mandatory — oscillating variable):** (a) FOMC 07-29 holds and TD is right that
  pricing is excessive → the 2y falls back and this was positioning into an event; (b) **the FOMC
  hikes, or the 2y closes >4.45% / real 10y >2.55%** → duration de-rate becomes a regime call.
- **Anti-signal (kills P1):** the 2y falls **<4.15%**, **or** the decomposition flips to real-10y-down
  with breakeven-up (an outright oil-inflation trade). ⚠ 07-23's version of this anti-signal
  ("unmeasurable at run clock") **is now measurable and did NOT fire**: breakeven was flat at 2.28% on
  07-23 while the nominal rose.
- KPI: **DGS2 daily** · DFII10 quoted **with** T10YIE · 2s10s · **CME hike odds**.
- Catalyst: **FOMC 2026-07-29** (D-5) · **June PCE 2026-07-30** (D-6, = scenario **S15**).

**P2 — Credit is still the loudest narrative and the quietest market.** *(carried, 5th run)*
- Anchor `[FRED]`: HY OAS **2.68% (−1bp, a new low tick), 5bp off the 365-day low**; IG **0.78%**;
  **NFCI −0.552, loosening a 5th straight week** — against `credit` term velocity of **1.03×
  pool-normalized, i.e. exactly average**, and a head event (*Big Banks Wading Back Into CRE Lending*,
  **9 outlets, BUILDING 5 days**) that is credit **expansion**, not stress.
- Direction: **no risk-off discount is warranted by the credit market.** Any credit-stress claim in
  this run is **narrative-only** unless it cites HY OAS or NFCI.
- **Both branches:** (a) spreads hold <3.00% → cyclicals and financials keep the benefit of the doubt;
  (b) **HY OAS >3.10%** → the narrative was early and the earnings-now tilt is re-cut.
- **Anti-signal:** HY OAS >3.10% on a close, **or** NFCI rising two consecutive weeks.
- KPI: HY OAS daily · NFCI weekly. Catalyst: FOMC 07-29 · PCE 07-30.
- ⚠ **The 07-23 pre-registered dispersion test is half-scored**: VIX 16.64 → **18.70 settled**
  (+12.4%) while HY *fell* 1bp. **Equity-only stress so far.** HY's 07-23 print is unpublished; score
  the other half next run rather than closing it now (**C3** — this is `unknown`, not `resolved`).

**P3 — ★ The AI complex has SPLIT on the tape: the spenders were sold and the suppliers were bought, in the same session.**
*(P3 rewritten — the 07-23 version asked "is it a margin question?"; the settled tape answers it)*
- Anchor `[measured, own calc, settled 2026-07-23 closes vs 07-22, benchmark **SPY −1.23%** named
  inline per **C1**]`:

| Leg | Names | Session return | Excess vs **SPY** |
|---|---|---|---|
| **Suppliers** | MU **+3.20%** · KLAC **+1.88%** · AMAT **+1.60%** · LRCX **+0.15%** | all positive | **median +2.98pp** |
| **Spenders** | GOOGL **−7.13%** · AMZN **−4.57%** · META **−3.36%** · MSFT **−2.24%** | all negative | **mean −3.09pp** |
| **Spread** | | | **6.07pp in one session** |

- Corroboration `[news]`: *"Intel rises as strong forecasts signal AI boost"* with a `└` sub-event
  naming **"ASML, AMAT, KLAC, LRCX: Chipmaking Equipment Stocks Rise"**, plus INTC **+10~11% after
  hours** on the print that scored **S6 FIRED-A**. And the spender side is narrated by the fastest
  terms in the entire sweep (**`free cash flow` 1.41×, `capex` 1.40×**, §C-2).
- Direction: **Info Tech's single label is being falsified on both halves at once** — which is exactly
  **S13 branch A**, observed six days *before* S13's event. It is also the third instance of the shape
  the desk has already measured twice (**R7**: duration REITs vs digital infra, 18.2pp, replicated;
  **M26/M36**: primes vs capital goods, 0.705 → 0.285).
- ⚠⚠ **This is `n ≈ 1` (rule S1) — one date, eight names, one shared driver.** It is **not** a verdict
  and **must not** be written as one. S13's own observable runs **10 sessions after 07-29**; this is a
  pre-observation that raises the prior, nothing more. **C4 wording applies: `indistinguishable`
  between "the split is structural" and "one session's rotation on an INTC print."**
- **Both branches:** (a) MSFT/META raise capex on 07-29 and the spender multiple compresses again
  while suppliers hold → **S13 branch A confirmed, IT must be split**; (b) the spenders re-rate on the
  same raise → the 07-23 session was an INTC-driven rotation and the single label survives.
- **Anti-signal (kills P3):** a capex **cut** at MSFT or META — which breaks the volume leg *and* the
  price leg together (STANDING_VIEW §4) and would hit suppliers *harder* than spenders, inverting the
  split. ⚠ Its narrative frequency remains **zero** (`capex cut` d1 = 0), so this anti-signal is
  **un-narrated by construction** and must be watched on the line item, not the feed (**C6**).
- KPI: **the supplier-minus-spender excess-vs-SPY spread**, tracked daily · MSFT + META capex lines.
- Catalyst: **MSFT + META 2026-07-29** (⚠ date disputed, §0) · AMZN/AAPL 07-30/31.

**P4 — ★★ RETRACTION-BEARING: the refining margin did NOT collapse on 07-23. Yesterday's headline number was an incomplete-bar artifact.**
- **What was carried** (M32, 07-23 report, explicitly tagged *intraday, incomplete bar*): *"the 3-2-1
  crack fell 66.86 → 59.36 = **−11.2%**… gasoline −19.7% vs distillate −3.6%, gap 30.3 → 38.5."*
- **What the settled 07-23 closes say** `[measured, own calc, yfinance CL/RB/HO continuous]`:

```
              WTI      RBOB     HO      3-2-1 crack   gasoline crack   distillate crack   gap
2026-07-22    86.83    3.415    4.149      66.87           56.59            87.42        30.83
2026-07-23    92.19    3.496    4.342      66.49           54.66            90.16        35.50
   change    +6.17%   +2.37%   +4.65%     −0.56%          −3.41%           +3.13%        +4.67
```

⇒ **The crack fell 0.56%, not 11.2%. It sits at the 89th percentile of 90 days** (90d range
41.14–69.45). **R17 is filed** (§G). ★ **The decomposition's *direction* survives and is in fact
stronger than reported**: distillate cracks **rose 3.1%** while gasoline fell 3.4%, widening the
diesel-minus-gasoline gap to **35.50** — the Atlantic-basin middle-distillate bottleneck is not just
intact, it **tightened** on the day crude rose 6.2%.
- ⚠⚠ **The identical artifact is live right now and is refused**: today's **incomplete** 07-24 bar
  (09:09 ET, pre-open) computes a crack of **58.58 = −11.9%** — numerically almost the same false
  reading as yesterday's, and possibly compounded by an **RBOB August-contract roll** (RB=F −7.3% in
  one pre-open print). **This run does not cite it.** The operative reading is the **settled 07-23
  crack, 66.49.**
- **D30 does not reproduce this run**: `BZ=F` settled **100.69** against WTI **92.19** ⇒ Brent−WTI
  **+$8.50**, a coherent spread, and Brent through $100 is independently carried by 7 outlets. The
  07-23 column/roll artifact was real then and is absent now — logged, not generalised.
- Anchor `[news]`: Red Sea attacks are the **#1 event of the day (11 outlets)**; *Trump weighs "massive
  attack" on Iran* [9]; a 12th-plus US strike wave; *Tanker Exits Red Sea Dark as Another China Ship
  Heads to Strait* [4]. `Iran` term velocity **0.94× pool-normalized = below the pool** — the story is
  huge in *events* and unremarkable in *term share*, exactly the divergence the news L2 warns about.
- **Anchor that cuts against the equity leg** `[measured, 07-23 session, benchmark SPY −1.23%]`:
  **XOM +1.58% (+2.81pp) · CVX +0.75% (+1.98pp)** against **VLO −1.82% (−0.59pp) · MPC −1.12%
  (+0.11pp) · PSX −2.10% (−0.86pp)**. **The crude leg was bought and the refining leg was sold, on a
  day the refining margin held flat.**
- Direction: **the crude/integrated leg and the refining leg are separate positions and separated
  again** — third independent session. ★ And the **C4 detachment counter must be re-read, not
  incremented**: the counter's premise was "the crack falls while refiners rise." On 07-23 **the crack
  was flat and the refiners fell** — a *third* pattern, in neither the confirming nor the breaking
  bucket. **Corrected tally: 3 confirmed (07-17/20/21) · 1 broken (07-22) · 1 neither (07-23).**
- **Both branches:** (a) cracks hold ≥65 while crude holds >$90 → the margin thesis is intact and the
  refiner selling was positioning ahead of VLO's 07-30 print; (b) **cracks break <60 on settled
  closes** → the margin engine is going, and the OW must sit on crude/integrated alone.
- **Anti-signal (kills P4):** a Hormuz "open" statement collapsing crude and cracks together (**S8**),
  **or** a settled crack below 60 with crude above $90.
- KPI: **3-2-1 crack on SETTLED closes only** (this is now a rule, not a preference) · diesel-minus-
  gasoline gap · WTI COT %ile.
- Catalyst: **VLO earnings 2026-07-30** (D-6) · **STNG 2026-07-30** · Hormuz statement `[blank]`.

**P5 — The tariff axis went from threat to enacted, and it is now a 60-country cross-sector tax.**
*(upgraded from "unconfirmed" — the event printed)*
- Anchor `[news, 07-24]`: *"US imposes new tariffs on dozens of trade partners over 'forced labor'"*
  [19 art/7 outlets] · *"Trump reimposes tariffs on 60 countries using forced-labor [rationale]"* ·
  *"Trump imposes new **12.5%** tariff on **Singapore**"* [6/5] · Australia named separately. Thread
  **BUILDING 4 days (6→3→8→9)**; `tariff` velocity **1.26× pool-normalized, 4th fastest**.
  Cross-desk: the KR run scored **S10 FIRED-B** on the same print (Korea **12.5%**).
- ⚠ **C3 applies to the sector attribution, not to the event**: the event is confirmed; *which* US
  sectors carry the cost is **not** in today's tiers, and 366 single-source rows are withheld and
  unscoreable. **"Unknown", not "absent".**
- Direction: a broad, rate-flat import tax is a **margin** event for import-intensive Consumer
  Discretionary and Staples and a **retaliation-risk** event for Materials (China's 14-entity EU
  export-control retaliation, 9 outlets, is the live template).
- **Both branches:** (a) carve-outs/negotiated reductions follow within weeks — the repeated pattern,
  and Korea's own 12.5% **landed below the 15% cap its government was defending**; (b) retaliation
  escalates (China's export controls are already branch b in miniature).
- **Anti-signal:** a formal carve-out list that exempts the large import-intensive US retailers.
- KPI: the **published country/product schedule** · China retaliation headlines · retailer guidance.
- Catalyst: `[blank — no implementation date in the calendar; not guessed]`.

**P6 — Japan is still the un-priced global-duration channel.** *(carried, unchanged in status)*
- Anchor `[news, 07-24]`: *"Japan inflation rises to **1.6%** in June: Why the weak yen coul[d]…"*
  [5 outlets] · *"Japanese Yen remains pinned near a 40-year low as Fed-BoJ [divergence]"* REIGNITED
  2→3 · *"Investors fear Japanese bond bets risk becoming new 'widowmaker'"* inside a **4-day BUILDING**
  bond thread · *"Japan's Katayama says will take necessary steps on for[ex]"*.
- ⚠⚠ **Still tagged `[unverified]` under rule W2 and therefore NOT admissible as evidence.** The claim
  *"BOJ tightening leads US long-end yields"* has **no lag table in this repo** (dig **D22**, open).
  DEEP and BET may not cite it. It is carried as a channel to watch, at the same status as last run —
  **flat for a second consecutive run, which is itself the argument for closing D22.**
- **Both branches:** (a) the BOJ accelerates → global long end sells off, compounding P1 branch (b);
  (b) the MoF intervenes on the currency instead → the yen snaps and the carry-funded **equity** leg
  is hit before the rate leg.
- **Anti-signal:** the yen retraces with no policy change → it was positioning, not policy.
- KPI: USD/JPY · JGB 10y · DFII10 co-movement. Catalyst: next BOJ meeting `[blank]`.

**P7 — The regulatory tax on Big Tech is a separate axis, and it broadened to a second constituent.**
*(carried, one new data point)*
- Anchor `[news, 07-24]`: **TikTok charged with breaching EU rules on online safety** [6 art/6 outlets]
  — the axis moves off Alphabet for the first time. Alongside: *OpenAI's president suggests AI labs are
  struggling to control [models]* [6/5]; *Lawmakers push for AI 'kill switch' after OpenAI goes [rogue]*
  [8→5]; the OpenAI containment thread **FADING 5→13→18→20→24→14→8** off a 24-outlet peak.
- ⚠ The FADING tag sits on a **partial-day window (350 events vs 840 yesterday)** and the L3 says
  explicitly that this inflates FADING. **Read as "not confirmed today", not "over."**
- Direction: Comm Services and mega-cap IT carry a policy cost that is neither a rate story nor a
  capex story.
- **Both branches:** (a) fines remain one-off cash items → noise; (b) conduct remedies arrive → a
  structural take-rate question, i.e. a multiple event.
- **Anti-signal:** decisions appealed and stayed with no conduct remedy.
- KPI: the **remedy text**, not the fine size. Catalyst: `[blank]`.
- ⚠ Carried partly because the **cycle registry still has no AI-security / regulatory row** (dig D20,
  registry `updated: 2026-07-17`, now 7 days stale), so **no GAP guard can fire against 0% exposure.**

**P8 — ★NEW · The rate shock has a housing/consumer transmission the desk has never carried, and it surfaced only in the blind-spot pass.**
- Anchor `[news, blind-pool sample]`: *"Treasury market signals that a **7% rate on a 30-year mortgage**
  could be next"* [marketwatch, 07-23] — found in the random blind sample, present in **no** head, body
  or thread tier. Mechanically consistent with §A: 10y at a 120-day high (4.67% FRED / 4.703% tape).
- ⚠ **`[news]`-only and single-outlet. It is registered as a channel to test, not as evidence** — the
  desk has no mortgage-rate series wired, which is the point of registering it.
- Direction: a 7-handle 30-year mortgage taxes housing-linked Consumer Discretionary and the classic
  duration REIT complex — **the same duration REITs that R7 measured as *bid* (WELL/VTR)**. If the
  channel is real, R7's surviving finding gets a live test.
- **Both branches:** (a) the 30-year prints ≥7% and housing-linked names de-rate → Cons. Disc. and
  duration RE lose their bid; (b) it stays <7% or the 10y retraces → the item was a headline.
- **Anti-signal:** the 10y closing back below 4.45% (the level from which this 20-session move began).
- KPI: **wire a 30-year mortgage series (FRED `MORTGAGE30US`, weekly) — not currently in
  `module_macro_us`'s catalog** · housing-linked RS vs **XLY** and vs **SPY** (benchmarks named, C1).
- Catalyst: weekly Freddie Mac print `[blank — day not wired]`.

---

## §E · ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)

> Wind direction only, one line per GICS sector. **Not** an equal-weight analysis of 11 sectors.
> Every relative claim names its benchmark inline (**C1**). Flow tags are deliberately absent —
> they are SWEEP's job and they are C-grade (**D6**).
> ⚠ All session numbers below are the **settled 2026-07-23** close vs 07-22, benchmark **SPY −1.23%**.

| # | GICS Sector | Tilt | Δ vs 07-23 | Driving prop. | One-line why |
|---|---|---|---|---|---|
| 1 | **Energy** | **OW** | OW → **OW** | P4 | Brent settled **through $100 (100.69)**, WTI +6.17%, COT still 10%ile — and **the crack did NOT collapse** (settled −0.56%, 89th pctile of 90d; yesterday's −11.2% was an incomplete-bar artifact, R17). But the OW remains on the **crude/integrated** leg: **XOM +2.81pp vs SPY while VLO −0.59 / PSX −0.86** on the same day |
| 2 | **Info Tech** | **N → split-pending** | N → **N (SPLIT FLAGGED)** | **P3** | ★ The single label was falsified on **both halves in one session**: suppliers **median +2.98pp vs SPY**, spenders **mean −3.09pp**, spread **6.07pp**, with INTC's print (**S6 FIRED-A**) as the named cause. ⚠ **n≈1 (S1)** — the tilt is held at N and the **split is handed to ROTATION as a mandate**, not taken as a verdict |
| 3 | **Financials** | **OW−** | OW− → **OW−** | P1, P2 | Credit refuses stress for a 5th run (HY **2.68%, a new low tick**; NFCI loosening) and a front book paid by a 120-day-high 2y — but 2s10s **flattened a second session**, so the steepener leg stays dead (R11). ★ New: **credit is EXPANDING** (*Big Banks Wading Back Into CRE*, 9 outlets, BUILDING 5 days), and **payments beat money-centers on 07-23** (PYPL +2.12pp, MA +0.92, V +0.72 vs **GS −0.90, MS −0.28**) — S14's question got a live pre-read |
| 4 | **Industrials** | **N+ → OW−** | **N+ → OW−** | P4, S7 | ★ **Upgraded on the settled tape, not on narrative.** **LMT +10.54% (+11.78pp vs SPY) and RTX +7.33% (+8.56pp) on a −1.23% day** — both outside their implied bands, completing **S7 branch A**; NOC +2.80pp corroborates a third name. ⚠ Held below full OW because **M36 measured the intra-sector spread decaying 0.705 → 0.285** and W5 forbids one label over two opposite things |
| 5 | **Health Care** | **N−** | N− → **N−** | P5, C7 | ★ **A third independent observation the desk keeps not acting on**: XLV **+1.26% (+2.50pp vs SPY)** — the best sector on 07-23 — with **LLY +3.20pp, ABBV +2.66, JNJ +2.66**; only UNH negative. Against **flat revision books** and a **Δ −0.102**. **C7 stays `indistinguishable` (C4)**, but the tilt is now the desk's largest belief-vs-money gap for a 3rd run |
| 6 | **Comm Services** | **N−** | N− → **N−** | P7, P3 | GOOGL **−7.13% (−5.90pp vs SPY)** — the worst mega-cap on the board — and the regulatory axis broadened to **TikTok/EU**. But **META −2.12pp** moved *with* GOOGL this session, which is evidence **against** S16's branch A. Held N− with S16 explicitly unsettled |
| 7 | **Utilities** | **N−** | N− → **N−** | P1 | Bond proxy into a 120-day-high real yield **and** a 2y at a 120-day high. ⚠ Counter-evidence logged, not suppressed: **VST +2.58pp and CEG +1.49pp vs SPY** on 07-23 — the AI-power leg outperformed while the regulated leg did not, i.e. **the same two-legs problem as IT** |
| 8 | **Real Estate** | **N−** | N− → **N−** | P1, R7, **P8** | R7's finding replicated a **third** time on an independent date: **WELL +2.06pp vs SPY** against digital infra **DLR +1.76 / EQIX +1.70 / AMT +0.39** — ⚠ **the spread NARROWED to ~0.6pp this session** (from 18.2pp on RS20), so R7's *direction* holds and its *magnitude* is not a daily phenomenon. **P8's 7%-mortgage channel is the live test** |
| 9 | **Materials** | **UW** | UW → **UW** | P1, P5 | Copper **95%ile crowded-long** (context, not a trigger — REJECTED ledger) + DXY in the upper half of its range + **China's 14-entity EU export-control retaliation** [9 outlets] on top of a 60-country US tariff |
| 10 | **Cons. Discretionary** | **N−** | N− → **N−** | P1, **P8**, P5 | The most rate-sensitive consumption there is, into a 2y at a 120-day high and a possible 7-handle mortgage. Bottom-up: **TSLA −14.52% (−13.29pp vs SPY)**, operating margin to **1.4%** |
| 11 | **Cons. Staples** | **N** | N → **N** | P1, P5 | Bond-proxy-adjacent multiple into rising real yields, now with an import-tax overlay (P5). Ballast only if P1 branch (b) trips |

**Wind summary.** One clean **OW (Energy**, crude leg, with its margin KPI **corrected upward** by
R17). One **upgrade to OW− (Industrials)**, earned on the settled tape rather than on narrative.
**Financials OW− carried by credit alone.** One clean **UW (Materials)**. **Info Tech is the run's
open question**: its single N label was falsified on both halves in one session, and the tilt is held
only because **n≈1**. Three sectors (**IT, Utilities, Real Estate**) now each carry a **measured
two-legs problem** — which is the same finding R7 and M26 produced, appearing a third and fourth time.

**DEEP candidates handed to ROTATION** (ROTATION owns the final pick):
**① Info Tech — the supplier/spender split** (P3; S13's branch A observed six days early; the only
sector whose label was falsified on both halves at once).
**② Energy — the crude/refining separation** (P4, with R17 correcting the margin number the last run
got wrong; VLO prints 07-30).
**③ Industrials — defense** (S7 branch A complete on the band leg; LMT/RTX/NOC all outside; but M36's
decayed intra-sector spread means W5 is pre-armed).
**④ Health Care** — the desk's largest belief-vs-money gap, now on a **third** independent date (C7).
**Financials** is flagged as the pre-mortem swing (payments beat money-centers; S14 lands 07-30).

---

## §F · Self-backtest

**Running hit-rate: 0 scored / 0 scoreable at a registered horizon.** The first US propositions were
registered **2026-07-21**; the **+7d window opens 2026-07-28**, +14d 08-04, +30d 08-20. Nothing is
scored at a horizon today, and no horizon is manufactured to create one (**P4**).

### +1d kill-line audit of the 07-23 propositions (a state check, not a score)

| 07-23 prop | Kill line | State on the settled 07-23 tape | Status |
|---|---|---|---|
| **P1** front-end reaction-function trade | 2y **<4.15%** or real 10y **>2.55%** | 2y **4.31% = 120d high**; real **2.39% = 120d high, 16bp of room**; breakeven **flat** | **Un-tripped, and its stated anti-signal explicitly did NOT fire** (the 07-23 "unmeasurable" caveat is now measured: breakeven flat while nominal rose). **Sharpened, not corrected** — §D-P1 adds the oil trigger |
| **P2** credit narrative ≠ credit market | HY OAS **>3.10%** | **2.68%, a new low tick**, NFCI loosening a 5th week, credit velocity exactly 1.00× pool | **Un-tripped. Still the strongest-standing proposition on the board (5 runs).** |
| **P3** capex is now a margin question | capex **cut** at MSFT/META | `capex cut` **d1 = 0** for a 3rd measurement; but **`free cash flow` and `capex` are the two fastest terms on the board** and the tape split spenders from suppliers by **6.07pp** | ★ **Un-tripped and materially advanced.** The branch it flagged as "the one nothing in the book brackets" is now **narrated** (in different words) and **partially observed** |
| **P4** the war premium is HOSTILE to refining margin | crack recovers >$68 with crude >$90 | ⚠ **The proposition's own anchor was wrong.** Settled crack **66.49, −0.56%** — not −11.2%. Crude **$92.19** | ★★ **PARTIALLY RETRACTED (R17).** The direction (crude/refining separation) survives on equity prices; **the magnitude claim is withdrawn.** The anti-signal is within **$1.51** of firing, which the run would never have known on the bad number |
| **P5** tariffs are a sector-specific tax | pharma carve-out/delay | **The event printed** — 60 countries, forced-labor rationale, Singapore 12.5%, Korea 12.5% (S10 FIRED-B) | **Upgraded from "unconfirmed" to enacted.** The sector attribution remains `unknown` (C3) |
| **P6** Japan duration channel | yen retraces with no policy change | Japan CPI **1.6%**, yen still near a 40-year low, JGB "widowmaker" thread BUILDING | **Un-tripped and unchanged for a second run** — which is itself the argument for closing dig **D22** |
| **P7** regulatory tax on Big Tech | appealed and stayed, no remedy | **TikTok/EU charge** — the axis broadened to a second constituent | **Un-tripped, broadened** |

### Failure classes logged this run

1. ★★ **An incomplete-bar number survived one full run and became a `[measured]` fact.** M32's −11.2%
   crack collapse was **correctly labelled "intraday, incomplete bar"** in the source table — and then
   quoted **six times** across STANDING_VIEW, P4, C4 and the DEEP mandate as if settled. **A caveat on
   the row does not travel with the number.** ⇒ **New rule proposed to RESEARCH: a number from an
   unsettled bar is not written into `handoff/*.md` at all; it is written as `[pending settle]` with
   the date it settles.** Registered as dig **D48**.
2. **The same artifact is reproducible, which makes it a defect rather than an accident.** The 07-24
   pre-open bar computes a crack of **58.58** — within 1.3% of yesterday's false 59.36 — so the
   pre-open read is **systematically ~11% below settle** on this composite. Refused explicitly in §D-P4.
3. **The calendar's misses have escalated from obscure to central** (D18, 5th run): today it omits
   **MSFT**, a named leg of the desk's own highest-information scenario.
4. **A frozen tracking term can measure the wrong thing while remaining literally true.** `capex cut`
   = 0 for three measurements, while the branch it tracks is being narrated at **1.41× pool-normalized**
   under `free cash flow`. **Track the economic content, not the phrase** (§C-2).

---

## §G · Retraction filed by this stage (append-only, to `handoff/STANDING_VIEW.md` §5 at run end)

| # | Claim | Killed by | Date |
|---|---|---|---|
| **R17** | **"On 2026-07-23 the 3-2-1 crack fell 66.86 → 59.36 = −11.2%, decomposing as gasoline −19.7% vs distillate −3.6%, with the diesel-gasoline gap widening 30.3 → 38.5"** — M32, and the P4 anchor built on it | **The settled 07-23 closes, pulled today**: crack **66.865 → 66.492 = −0.56%**; gasoline crack −3.41%; **distillate crack +3.13%**; gap 30.83 → **35.50**. The crack sits at the **89th percentile of 90 days**, not out of its high zone. M32 carried its own *"intraday, incomplete bar"* caveat and the caveat did not travel with the number. ★ **What survives, and is strengthened**: the *direction* of the decomposition — distillate outperformed gasoline by **6.5pp** in one session, so the middle-distillate bottleneck **tightened**. ★ **What is withdrawn**: the magnitude, the "war premium is measurably hostile to refining margin" strength claim, and any use of −11.2% as evidence | 2026-07-24 |

---

## §H · Rule-linter result

`report_lint.py` on this file: **✅ 0 findings** across rules **C1 · C2 · S6 · D6** (1 file scanned).
⚠ The linter checks **form only** (C1 benchmark · C2 both halves · S6 future label · D6 OBV-alone).
A clean run is not a correct report.

## §I · New digs registered by this stage

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D47** | **Three sources disagree on the mega-cap earnings dates** (`catalyst_calendar` META 07-29 · news bodies META 07-29 / AMZN 07-30 · `yfinance.calendar` META 07-30 / MSFT 07-30 / AMZN 07-31 / AAPL 07-31, i.e. uniformly +1 day) | The desk's headline framing — *"six triggers stacked on 2026-07-29"* — depends on which is right. If the mega-caps print 07-30, the stack **splits** and **07-30 (PCE + MSFT + META + MA + VLO) is at least as loaded**. Registered dates are **not** rewritten on one disagreeing provider (D5) | MACRO / human to pick a primary |
| **D48** ★ | **A number from an unsettled bar entered `handoff/STANDING_VIEW.md` as `[measured]` and survived a full run** (M32 → R17). The row carried the caveat; the six downstream quotations did not | This is the mechanism by which a labelled uncertainty becomes an unlabelled fact. **Proposed rule: an unsettled-bar figure is written as `[pending settle — settles YYYY-MM-DD]`, never as a plain number, and no proposition anchor may rest on one** | RESEARCH / any stage writing the carry |
| **D49** | **`module_macro_us` has no mortgage-rate series** (`MORTGAGE30US`, weekly, free on FRED) | P8's channel — the rate shock's transmission into housing-linked Consumer Discretionary and the duration REITs R7 measured as *bid* — **cannot be measured with the current catalog**, only narrated | `module_macro_us` / human |

---

## §5 · DRIFT ADDENDUM — appended 2026-07-24 by stage 10 (append-only; nothing above is rewritten)

⚠ **`scripts/drift_watch.py` is STILL unrunnable — dig D17, third consecutive run.**
`drift_watch.py --report llm_outputs/2026-07-24/industry_US/MACRO_REPORT.md` returns
`'drift' 는 원격 실행 불가(조회 전용). 허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']`.
**The client-side `DB_READ_CMDS` edit was never deployed to the running server.** Per **P6** this needs a
server `git pull` + API restart — a one-command fix for a human, not a code change.
**The measured substitute is used and is now effectively the permanent path**: pool-normalized
`fts --count` over this run's own registered anti-signal terms.

**Pool baseline at run end**: d1 **9,796** vs d7/7 **3,939 ⇒ the pool itself is running 2.487×.**
Every ratio below is divided by that before it means anything.

| Anti-signal term (from this run's own propositions) | d1 | d7 | raw | **pool-normalized** | Read |
|---|---|---|---|---|---|
| **`guidance cut`** | 12 | 21 | 4.00× | ★ **1.61× — the run's only burst** | body-read below |
| `rate cut` | 83 | 202 | 2.88× | 1.16× | mildly above pool, and pointing the *opposite* way to §C-1's hike pricing |
| `recession` | 96 | 327 | 2.06× | 0.83× | below pool |
| `OPEC` | 42 | 162 | 1.82× | 0.73× | below pool |
| `diesel export ban` | 1 | 4 | 1.75× | 0.70× | ⚠ n=1/4 — unusable as a ratio |
| `credit stress` | 4 | 19 | 1.47× | 0.59× | below pool — **P2 untouched for a 5th run** |
| `ceasefire` | 97 | 498 | 1.36× | **0.55×** | **decelerating — the de-escalation branch is quieter, not louder** |
| **`capex cut`** | **0** | **1** | — | **0.00×** | **zero for a third consecutive measurement (C6)** |

### The one burst, body-read rather than counted

**`guidance cut` 1.61× is Walmart de México, plus legal boilerplate.** The 12 d1 hits resolve to
*"Walmex Q2 2026 slides: revenue beats but **guidance cut on weak demand**"* and *"Walmart de México
Q2 2026: modest beat, guidance cut"* [investing_en, 2026-07-24], plus a securities-class-action press
release on **GPGI** [prnewswire] whose "guidance cuts" reference is to **May 2026** — a
**recycled-date artifact of exactly the D29 class**, and it is discarded.

⇒ **No kill-switch fired against any call in this report.** The Walmex item is a **demand**-driven
guidance cut at a large-format retailer, which is mild *corroboration* of two calls this run already
made — **Cons. Discretionary N− → UW** (eqflow −0.281, 0🟢/11🔴, Δ −0.136 worst on the board) and
**Cons. Staples N → N−** — not a contradiction of either. **It is a Mexican retailer, so it is
read as a demand datapoint and not as a US regime signal.**
⚠ **It does sit on S20's branch-C axis** (a guidance cut attributed to **volume** rather than fuel).
Registered here **before** UPS prints on 2026-07-28 so it cannot be recruited afterwards as
confirmation of whichever branch fires.

### ★ The oil axis moved AFTER this report's baseline, and it moved AWAY from our anti-signal

`fts search "Strait of Hormuz" --scope foreign --days 1` returns **410 items**. Direction, body-read:

- ★ *"Oil prices touch six week high as **Strait of Hormuz is 'completely closed'**"* [toi, 07-23] —
  the IRGC claims the Strait is under its control.
- *"**Iran Apparently Seizes** Greek Billionaire's Shipping Tanker In Strait Of Hormuz"* [forbes, 07-22]
- *"Oil extends gains as **Trump threatens strikes on critical Iranian infrastructure**"* [cnbc, 07-23]
- *"Crude crosses $95 as US strikes enter their **12th day**. Why **Goldman says $120 is possible**"* [economictimes]
- ★ **The contested counter, and it is why "completely closed" is not taken at face value**:
  *"**Three Crude Supertankers Slip Out Through the Strait of Hormuz**"* [bloomberg, 07-23].
  **The closure is an IRGC claim that a same-day Bloomberg report partially contradicts.** Stated as
  contested, not adopted.
- Structural, and new: *"**DP World plans two ports in Fujairah** … to circumvent the Strait of Hormuz
  **permanently**"* [semafor, 07-23].

⇒ **`S8`'s branch A (a "Strait open" statement) moved FURTHER AWAY, not closer** — and the earlier
phrase-count of `"Strait of Hormuz open"` = 1 was a **false positive on the phrase**, not a signal.
**S8 stays undated `[blank]`; no date is guessed.**
⚠ **This does NOT strengthen the Energy OW's margin case, and the distinction matters**: DEEP-ENRG
concluded the margin is real on **three legs that are not the futures strip** (TotalEnergies' realized
$12.4/bbl marker, EIA utilization 96.2%, and the settled weekly distillate crack). **More war is more
war premium — it is the thing the margin case was constructed to be independent of.** The dated
observable that actually governs the distillate leg is unchanged and is **the Russian export ban's
expiry on 2026-07-31**.

### Verdict

**No 🚨. No §D proposition is flipped, and none is rewritten.** One benign burst (`guidance cut`,
body-read to a Mexican retailer and a stale-dated legal notice), one axis that escalated **in the
direction this report already leaned** while its own anti-signal grew quieter (`ceasefire` **0.55×**),
and **`capex cut` at zero for a third straight measurement** — which is the C6 finding, not an absence
of the branch: the branch is being narrated as **`free cash flow` 1.41× and `capex` 1.40×**, the two
fastest terms on the board.

