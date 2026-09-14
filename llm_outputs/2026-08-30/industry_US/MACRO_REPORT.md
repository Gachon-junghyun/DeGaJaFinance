# MACRO_REPORT — industry_US · 2026-08-30 (Stage 3 / L1·MACRO)

> Sunday 09:1x ET. **No US session has occurred since 2026-08-28.** The macro axis therefore has
> exactly one new thing to say versus the 08-29 run — and it turns out to be a large one, because the
> 08-28 session that run could only read through `fast_info` on eight names is now readable **across
> the whole universe and across two independent providers** (§A-0).
> Zero buy/sell recommendations. Every relative number names its benchmark inline (`C1`).

---

## §0 · Rights removed before any number below is read

From `preflight/PREFLIGHT.md` (6 FAIL) and `HANDOVER.md §0`:

1. 🚫 **`SECTOR_FLOW_US.json` is empty** (`scored=0/299`). No flow score, no Δflow, no 🟢/🔴, no
   breadth, no flipper list, **no sector promotion or demotion on `wflow`/`eqflow`.** Every sector
   statement in §D is built from **ETF excess returns, FRED, COT and the news denominator**, and says so.
2. 🚫 **No news-velocity or theme-freshness claim sourced from the sweep** (17.06% coverage). Direct
   queries are live and are labelled *"direct query, outside the sweep window"* wherever used.
3. 🚫 **No 08-28 price from the daily endpoint, the book, `status` or `pulse`** — those show **08-27**.
   ✅ 08-28 is cited from the **5m proxy**, always with that label.
4. 🚫 **No US chart-shape verdict** (`module_chart` renders 0/3).
5. 🚫 **No bare concentration number** and **no `kelly_size --ic` as evidenced**.

★ **And one right this stage removes that PREFLIGHT did not**: **`M1090`** `[measured]` — **the foreign
news ingest has been dark for two days.** Article counts, `--scope foreign`: 08-26 **5,310** · 08-27
**5,263** · 08-28 **4,490** · **08-29 = 3** · **08-30 = 0**.
⇒ 🚫 **No "as of today" news claim anywhere in this run. The newest news observation this desk holds
is 2026-08-28.** ⚠ And **`fts search --days 7` cannot detect this** — a 7-day count is dominated by the
five populated days, which is exactly why PREFLIGHT G1's healthy probe counts (1237/5251/2022/…) are
true and yet do not license a freshness claim. Registered as **`D411`**. See §E-4 for the self-refutation.

---

## §A · Instruments

### A-0 · ★★ The 08-28 session, corroborated across **two providers** — `D5` satisfied for the first time in this window

The 08-29 run tried Stooq as its second provider and got **HTTP 404**; today Stooq answers with a
**JavaScript proof-of-work challenge**, which this desk does not solve. So I used a provider the desk
already holds credentials for and had never pointed at prices: **FRED**, whose `SP500` and
`NASDAQCOM` series come from **S&P Dow Jones Indices / Nasdaq via the St. Louis Fed** — a genuinely
different pipeline from `yfinance`.

| index / proxy | provider A — FRED `[FRED]` | provider B — 5m proxy (yfinance) | agreement |
|---|---|---|---|
| S&P 500 · 08-27 → 08-28 | `SP500` **7,730.99 → 7,711.76** = **−0.2487%** | `SPY` **771.10 → 769.38** = **−0.2231%** | **2.6 bp apart** |
| Nasdaq · 08-27 → 08-28 | `NASDAQCOM` **26,541.35 → 26,402.42** = **−0.5235%** | `QQQ` 721.11 → 716.45 = **−0.6462%** | 12 bp apart (Composite vs NDX-100 — different baskets) |

⇒ **`M1091`** `[measured]` **The 2026-08-28 US session is confirmed by an independent provider.** The
residual differences are the expected ETF-vs-index and Composite-vs-100 tracking gaps, not instrument
disagreement. **`D5` is met for the index level** — the first time in this window. ⚠ It is **not** met
at the single-name level (FRED carries no single equities); name-level 08-28 prices remain
one-provider, three-surface (`HANDOVER §11a`).

### A-1 · FRED primaries `[FRED]` — with each series' staleness stated

| series | id | last obs | value | 1y %ile | 21-obs ago | staleness |
|---|---|---|---|---:|---:|---|
| Fed funds | `DFF` | 2026-08-27 | **3.63** | **8.3** | 3.63 | 1 business day |
| 2y | `DGS2` | 2026-08-27 | **4.20** | **91.2** | 4.22 | 1 bd |
| 5y | `DGS5` | 2026-08-27 | **4.38** | **94.1** | 4.37 | 1 bd |
| 10y | `DGS10` | 2026-08-27 | **4.67** | **93.0** | 4.67 | 1 bd |
| 30y | `DGS30` | 2026-08-27 | **5.19** | **93.4** | 5.20 | 1 bd |
| real 10y | `DFII10` | 2026-08-27 | **2.34** | **89.0** | 2.41 | 1 bd |
| 10y breakeven | `T10YIE` | **2026-08-28** | **2.31** | **45.6** | 2.27 | current |
| VIX | `VIXCLS` | 2026-08-27 | **14.51** | **3.9** | 20.66 | 1 bd |
| HY OAS | `BAMLH0A0HYM2` | 2026-08-27 | **2.63** | **0.0** | 2.87 | 1 bd |
| IG OAS | `BAMLC0A0CM` | 2026-08-27 | **0.79** | 45.3 | 0.81 | 1 bd |
| NFCI | `NFCI` | 2026-08-21 | **−0.566** | **0.0** | −0.459 | **9 days** |
| broad USD | `DTWEXBGS` | **2026-08-21** | 118.06 | 8.2 | 120.91 | 🚨 **9 days — `D333`, 12th reproduction** |
| CPI | `CPIAUCSL` | 2026-07-01 | 332.813 | — | — | **~2 months** |
| core CPI | `CPILFESL` | 2026-07-01 | 336.789 | — | — | ~2 months |
| unemployment | `UNRATE` | 2026-07-01 | **4.10** | **0.0** | — | ~2 months |
| M2 | `M2SL` | 2026-07-01 | 23,218.0 | 92.3 | — | ~2 months |
| Fed assets | `WALCL` | 2026-08-26 | 6,730,912 | 82.5 | 6,675,344 | 4 days |
| RRP | `RRPONTSYD` | **2026-08-28** | 0.175 | 3.7 | 1.076 | current |
| SOFR | `SOFR` | 2026-08-27 | 3.64 | 26.1 | 3.65 | 1 bd |

**Both halves of every headline print** (`C2`), like-for-like windows:
- **Headline CPI**: **+3.30% YoY** (Jul-25 → Jul-26) and **+0.07% MoM**. Both cited.
- **Core CPI**: **+2.47% YoY** and **+0.22% MoM**. Both cited.
- ⇒ **`M1092`** `[measured]` **headline runs 83 bp ABOVE core** on the same July print — the wedge is
  in the non-core components, and it is the *headline* number a hawkish speech gets asked about.
  ⚠ `handoff/RESEARCH.md` flags the headline-CPI wedge as an **oscillating** variable; any proposition
  on it carries both branches, and §C-`P115` does.
- **M2**: **+5.41% YoY**, **+0.44% MoM**.
- **`real_10y` quoted with `breakeven_10y`** (required): **DFII10 2.34 at the 89.0th %ile** against
  **T10YIE 2.31 at the 45.6th %ile**. ⇒ **`M1093`** `[measured]` **the yield level is a REAL-rate
  phenomenon, not an inflation-expectation one** — and Bloomberg's own 08-28 headline says the same
  thing independently (*"Warsh's Hawkish Message Lands as Real Yields Lead Bond Moves"*, §B-1).

**The curve, and the number that organises this whole report:**

| spread | last (08-27) | 1y %ile | 21 obs ago |
|---|---:|---:|---:|
| 2s10s | **+0.47** | 20.5 | +0.45 |
| 10s30s | **+0.52** | 16.5 | +0.53 |
| **10y − Fed funds** | **+1.04** | **93.0** | (63 obs ago **+0.83**) |

⇒ **`M1094`** `[measured]` **The Fed has cut 70 bp over the year (DFF 4.33 → 3.63, an 8.3rd-percentile
policy rate) while the entire 2y–30y curve sits at 91st–94th percentiles.** Internal slope is *flat*
by its own history (2s10s at the 20th %ile, 10s30s at the 16th) ⇒ **this is a level/term-premium
repricing against policy, not a steepening.** ★ **The market has spent the year refusing the Fed's
easing, and on 08-28 the Fed came round to the market.**

### A-2 · Credit — the axis this stage is required to cite, and it still refuses the stress story

- **HY OAS 2.63 = the 0.0th percentile of its own year** (365-day low; 2.87 twenty-one observations ago,
  i.e. **−24 bp in a month**).
- **IG OAS 0.79**, 45.3rd %ile — mid-range, unmoved (0.81 a month ago).
- **NFCI −0.566 = the 0.0th percentile**, i.e. **the loosest financial conditions of the year**, and
  loosening monotonically (−0.459 → −0.531 → −0.566).
- **VIX 14.51 = 3.9th %ile.**

⇒ **`M1095`** `[measured]` **On the day the Fed chair signalled possible rate hikes, three separate
funding/risk instruments sat at or within 4 percentiles of their yearly extremes of EASE.** Any claim
of credit stress in this run would be **narrative-only** and is labelled as such wherever it appears.
★ The interesting tension is not "credit is calm" but **the joint state**: real yields at the 89th
percentile *and* credit spreads at the 0th. That pair is what `P116` brackets.

### A-3 · Positioning — `us_flow --cot`, CFTC speculative net, 1-year percentile

| instrument | net spec | weekly Δ | %OI | 1y %ile | tag |
|---|---:|---:|---:|---:|---|
| S&P 500 (E-mini) | −67,994 | **−57,434 ▼** | −3.3% | 65 | 🟡 neutral |
| Nasdaq-100 | +11,127 | **+23,193 ▲** | +3.5% | 59 | 🟡 neutral |
| **Russell 2000** | −16,118 | −412 ▼ | −50.9% | **15** | 🔴 **crowded short** |
| UST 10Y | −838,975 | +107,986 ▲ | −13.5% | 22 | 🟡 |
| UST 2Y | −861,296 | +66,041 ▲ | −18.4% | 72 | 🟡 |
| USD Index | +18,682 | −397 ▼ | +39.0% | 74 | 🟡 |
| WTI | +31,099 | +1,935 ▲ | +15.0% | 43 | 🟡 |
| **Nat Gas** | −197,932 | +5,571 ▲ | −11.3% | **2** | 🔴 **crowded short** |
| Gold | +243,334 | +21,145 ▲ | +56.9% | 66 | 🟡 |
| **Copper** | +85,266 | +5,518 ▲ | +30.1% | **100** | 🟢 **crowded long** |
| Silver | +25,261 | +1,636 ▲ | +22.2% | 41 | 🟡 |

⚠ **Tuesday close, 3–4 day lag ⇒ this is context, not a trigger** (the desk's own rule; the tape it
describes ends 08-25, before the speech).
- ★ **`M1096`** `[measured]` **The two equity legs moved in opposite directions in the same week**:
  S&P 500 spec net **−57.4k** while Nasdaq-100 spec net **+23.2k**. **Speculators added tech and cut
  broad index in the same week.** ⚠ Both land at 59–65th %ile, i.e. **neither is extreme**; the
  *direction* is the observation, and it is a pre-speech observation.
- **Copper at the 100th percentile** is the board's only crowded-long, and it is a `MATR` input.
- **Nat gas at the 2nd percentile** is the board's most crowded short, on a week when **Qatar extended
  its LNG force majeure** (§B-1). Named as a positioning/news conjunction, **not** as a direction.
- **Russell 2000 at the 15th percentile** with `IWM` exc5 **−1.88pp vs SPY** — crowded short *and*
  underperforming, i.e. the short is currently working.

### A-4 · The tape, settled 2026-08-28 — ★ the most informative table in this report

All closes are **5m-proxy (err ≤0.05%, n=324 · mean 0.022% · 319 of 324 inside 0.1%)**; benchmark
**SPY**, named inline. The daily endpoint has none of these.

**Sector ETFs, excess vs SPY (pp):**

| ETF | GICS | exc1 (08-28) | exc5 | exc20 | exc60 |
|---|---|---:|---:|---:|---:|
| XLC | Communication Services | **+1.63** | **+0.94** | +1.38 | −1.21 |
| XLK | Information Technology | **−1.33** | **+0.81** | **+2.90** | **−7.38** |
| XLF | Financials | +0.59 | +0.58 | −0.97 | **+12.19** |
| XLU | Utilities | −0.87 | −0.62 | **−6.69** | −4.30 |
| XLP | Consumer Staples | +0.63 | −1.14 | −2.55 | +1.97 |
| XLY | Consumer Discretionary | **+1.37** | −1.16 | −2.03 | −1.60 |
| XLB | Materials | +0.11 | −1.17 | +2.44 | +0.98 |
| XLRE | Real Estate | −0.22 | −1.85 | −4.35 | +0.18 |
| XLE | Energy | +0.82 | **−2.02** | +2.23 | +4.72 |
| XLI | Industrials | −0.73 | **−2.23** | **−4.52** | −0.26 |
| XLV | Health Care | −0.02 | **−2.46** | +2.30 | **+13.99** |

**Non-GICS reads, same benchmark:** `SMH` **−3.26 / −1.79 / −0.67 / −15.31** · `XBI` −3.25 / −2.49 /
**+7.47 / +23.07** · `KRE` +0.17 / −1.21 / −5.29 / **+7.47** · `ITA` −0.42 / −2.41 / −5.88 / +1.49 ·
`IWM` −1.13 / −1.88 / −1.43 / +0.80 · `RSP` −0.13 / −0.93 / −0.36 / +3.45 · `QQQ` −0.42 / −0.06 / +1.14 / −5.74.
**SPY itself: 769.38 · +0.48% 5d · +2.99% 20d · +2.01% 60d.**

★ **`M1097`** `[measured]` **The single most important thing in this table is a sign flip inside one
column pair: `XLK` is the WORST of eleven on `exc1` (−1.33) and the BEST of eleven on `exc20` (+2.90).**
⇒ **the Warsh session was a one-day duration hit inside a still-leading 20-day IT run**, and a stage
that reads only the day would call IT broken while a stage that reads only the month would call it
unscathed. **Both readings are in this report and neither is allowed alone.**
- **The duration legs did NOT move together on 08-28**: `XLK` −1.33 · `XLU` −0.87 · `XLRE` −0.22 —
  **1.11 pp apart** on a single session. That is evidence *against* a clean rate-event reading and is
  the prior `P113` was registered on; **it is disclosed as a prior, not smuggled in as a result.**
- **`SMH` −15.31 on `exc60` against `XLK` −7.38** ⇒ semis are dragging IT over the quarter while IT
  leads over the month. **The AI-compute epicenter is the 60-day loser of this board.**
- **`XLV` +13.99 and `XLF` +12.19 on `exc60`** are the two 60-day winners — and **both are among the
  worst three on `exc5`** (`XLV` −2.46) or flat (`XLF` +0.58). Momentum and the last week disagree.
- **`XLU` −6.69 on `exc20`** is the worst 20-day leg on the board.

**Book names on 08-28 (5m proxy):** `HPE` **−3.90%** · `ETN` **−3.21%** · `ANET` **−2.87%** ·
`NVDA` **−4.58%** · `AVGO` −0.77% · `NUE` −0.74% · `RTX` −0.17% · `NDAQ` −0.04% · `MET` +0.26% ·
`MPC` **+1.47%** · `PSX` **+1.76%**.
⚠ Stated once so no stage double-counts it (`D343`): **the four worst are the AI-compute/AI-power
cluster and the two best are the two refiners.** `NVDA`'s −4.58% is already inside `S116` and `S118`;
**it is one price path read at several points, not several confirmations.**

---

## §B · Narrative — events, trajectories, buckets, blind spot

### B-1 · Events — `brief --date 2026-08-28 --body 2 --scope foreign`

**Denominator, corrected**: **4,490 articles** → 1,309 clusters → **685 market events (2+ outlets)** ·
**224 subevents recovered** · **624 single-source clusters** · `excluded_not_news` **{} (empty this run)**.
Head 95 · body 590 · **tail 0**.
⚠ **`tail = 0` is not the coverage claim.** What was still withheld:
**`single_source` shown 15 of 624 ⇒ 609 clusters unseen** (`min_nb` 10.0) · `excluded_nonmarket`
**shown 0 of 0** (the classifier put nothing in the non-market band this run). ⇒ **the honest coverage
statement is: every 2+-outlet market event was read; 609 one-outlet clusters were not.**

**★ The day's macro event, and it is unambiguous — 3 of the top 10 clusters are the same speech:**

| cluster | outlets / articles | primary evidence |
|---|---:|---|
| *"Key Takeaways From Fed Chairman **Warsh**'s Jackson Hole Speech"* | **21 / 70** | `bloomberg` · `google_en`/qz · subevents: *"'We Have Work to Do'…"*, *"Warsh's First Jackson Hole Speech"* |
| *"**Warsh says Fed has 'work to do'** if above-target inflation persists"* | **19 / 76** | `yahoo_finance` · subevents: *"Fed Chair Warsh **signals rate hikes may be needed**"* (AP), *"Fed's Warsh Cites 'Readiness to Act'… **Markets See a September Rate Hike**"* (Barron's) |
| *"US stocks end lower as Warsh keeps inflation fight front and centre"* | **11 / 22** | `economictimes` · `straitstimes` · `yahoo_finance` *"Stocks Lower as Fed's Warsh Comments Boost Rate-Hike Bets"* |
| *"Analysis: Warsh sharpens inflation warning… signaling possible rate hike"* | 6 / 12 | `cnbc`; subevent *"Treasury Yields Rise as Warsh Vows to Pull Down Inflation"* |
| *"Warsh Speaks and **Rate-Hike Odds Rise**"* | 6 / 10 | `wsj` · Reuters VIEW |
| *"**Warsh, In Our Time**"* | 6 / 7 | 🟢 **`federalreserve` — the primary source itself**; `bloomberg`: *"Warsh's Hawkish Message Lands as **Real Yields Lead Bond Moves**"* |
| *"**Dollar jumps** after Warsh comments, set for weekly gain"* | 5 / 12 | `cna` ×3 |

⇒ **`M1090`-adjacent, `[measured]` + `[news]`**: the 08-28 macro event is a **hawkish Fed-chair speech
that moved rate-hike odds, yields, the dollar and equities in one session.** The primary source is in
the evidence list (`federalreserve`), so this is not a second-hand read.
★ **And it explains the tape without needing a sector story**: duration down (`XLK` −1.33, `XLU` −0.87),
banks up (`XLF` +0.59, `KRE` +0.17), dollar up, `SMH` −3.26.
🚨 **The dollar item is the one that indicts an instrument**: *"Dollar jumps… set for weekly gain"*
[5 outlets] while **`DTWEXBGS` last prints 2026-08-21**. ⇒ **the desk's only FX series is nine days
behind a move the news layer can see.** `D333`, 12th reproduction, and this is the first run where the
lag is demonstrably hiding a *direction*, not just a level.

**Other head-layer items that are macro or sector input (not ranked by importance — `P4`):**

| item | outlets | why it is here |
|---|---:|---|
| **"US Job Growth Marked Down 79,000 in Preliminary Estimate"** | 5 / 5 | the labour benchmark revision — **bottom of the head layer on a day the speech carried 21** |
| **"US Consumer Sentiment Drops, Year-Ahead Inflation Views Improve"** | 5 / ~6 | **both halves point opposite ways in one release** (`C2` is the reason this is quoted whole) |
| **"Qatar Extends LNG Force Majeure as Hormuz Traffic Remains Halted"** | **6 / 11** | `bloomberg` · `oilprice`; subevent *"**Hormuz Tanker Traffic Drops** Despite Recovery in Oil Flows"* |
| **"Oil… Crude heads for weekly losses as Hormuz flows remain choppy"** | **14 / 22** | `toi` · `nasdaq` *"Crude Prices Slip as **More Oil Flows Through** the Strait"* · `oilprice` *"…Despite Escalating Iran Tensions"* |
| **"Venezuela weighs exit from OPEC as US discusses stake in oil fields"** | **14 / 29** | `aljazeera` · `scmp` *"Trump says US has deal with Venezuela for control of 65 billion barrels"* |
| **"Chevron… in Talks to Expand in Venezuela"** | 6 / 7 | `nyt` · `wsj` *"Chevron, Other U.S. Firms Near Deal to Invest Billions"* |
| **"Nvidia pauses revenue-sharing deals with AI cloud companies"** | 5 / 6 | AI-compute chain |
| **"Marvell selloff deepens as investors seek clarity on Google AI deal payoff"** | 5 / 6 | corroborates `S116`'s `FIRED-C`-leaning-B |
| **"SK Hynix starts construction of $5 billion memory hub in Indiana"** | 5 / 6 | memory **capacity** — `P109`'s object class |
| **"Micron's Chinese rival just reported its first earnings — sales booming"** | 1 (single-source layer) | CXMT; the memory-supply competitor |
| **"Blue Owl funds lead $2.4B compute equipment financing for IREN"** · **"IREN Falls 6% as $639M Mining Rig Writedown…"** | 5 / 6 · single-source | AI-compute financing, both directions |
| **"ECB's Kocher: Europe's Economy Is Gaining More Momentum"** · **"Eurozone Economic Sentiment Beats Forecasts"** · **"Canada's Economy Grows 3.3% in Q2"** | 5 each | non-US growth, all positive |
| **"Japan spent record $96.5 billion to support yen over past month"** | 5 / ~6 | FX intervention, a dollar-side fact |
| **"US judge rules Pentagon's blacklisting of Anthropic unlawful"** | high | AI/defence-procurement |
| **"Meta's $18 Billion Settlement Could Reshape Social Media Stocks"** | 5 / 6 | `XLC` is the day's best sector (+1.63) — named as a coincidence to check, **not** as a cause |

### B-2 · Trajectories — `thread --days 7 --scope foreign`

🚨 **Read the denominator line first, because it changes every tag on the list**:
**08-24 792 · 08-25 832 · 08-26 831 · 08-27 840 · 08-28 685 · 08-29 0 · 08-30 0.**
The tool reports **525 ENDED threads and 0 alive**. ⇒ **Every thread reads ENDED because the window's
last two days are empty** (`M1090`), not because attention rotated. The stage's own warning — *"a
holiday/low-volume window end inflates FADING"* — is firing **literally**, and this is the strongest
form of it the desk has recorded.

Curves through **08-28**, which is the last day that carries information:

| thread | curve 08-24→08-28 | peak | reading |
|---|---|---:|---|
| **Warsh / Jackson Hole takeaways** | **5→7→13→21** | 21 | **BUILDING, and still climbing when the data stops.** The tool calls it ENDED; the data says the opposite |
| **Warsh "work to do"** | 6→8→11→6→**19** | 19 | spike on the speech day |
| Canada retaliatory tariffs | 21→29→15→9→**3** | 29 | genuinely **FADING** (populated days only) |
| *"U.S. Stocks Rise as Oil, Inflation Fears Retreat"* | 16→20→15→16→14 | 20 | flat — and **its premise was reversed on 08-28** |
| *"Top analyst resets Nvidia price target"* | 4→14→18→4 | 18 | peaked 08-26/27, off before the 08-28 drop |
| **US threatens toughest sanctions yet against Iran** | 17→14→4→6→**2** | 17 | FADING on populated days |
| Meta settlement ($16.7bn / $18bn, two clusters) | 19→4 · 18→7→5 | 19 | one-day events |
| Government urges AI firms to disclose learning data | 13→20→15→19→14 | 20 | persistent |

⇒ **Every proposition in §C names its thread's tag and curve, and where the tag is an artifact of the
dark window, the curve is quoted instead of the tag.**
⚠ **Curve shape is not importance** (`P4`) — the Canada-tariff thread has the highest peak on the board
and the smallest market footprint in §A-4.

### B-3 · Term sweep — and the correction that changes every number in it

Terms passed as **separate argv**, `--scope foreign`, direct queries (outside the sweep window):

| term | 7d | 30d | naive velocity | **dark-day-corrected velocity** |
|---|---:|---:|---:|---:|
| **Jackson Hole** | 1,187 | 1,348 | 3.77 | **4.93** |
| tariff | 2,029 | 6,747 | 1.29 | **1.68** |
| inflation | 3,002 | 11,708 | 1.10 | **1.44** |
| recession | 324 | 1,258 | 1.10 | **1.44** |
| credit spread | 76 | 337 | 0.97 | **1.26** |
| rate hike | 715 | 3,227 | 0.95 | **1.24** |
| layoffs | 106 | 539 | 0.84 | **1.10** |
| **Hormuz** | 956 | 5,132 | **0.80** | **1.04** |
| data center capex | 6 | 35 | 0.73 | 0.96 ⚠ n too small to read |
| payrolls | 195 | 1,330 | 0.63 | **0.82** |

🚨 **`D411` in action.** The naive velocity divides by **7** days when only **5** carried articles, and
the 30-day base also contains those 2 dark days (28 populated). Corrected velocity =
`count7 × 28 / (5 × count30)`.
⇒ **The uncorrected column reads "everything is quieting" — nine of ten terms below 1.30 and Hormuz at
0.80 = "fading". The corrected column says Hormuz is FLAT (1.04) and tariff is genuinely accelerating
(1.68).** **A run that had not measured the ingest gap would have written a systematically calmer
macro than the data supports**, and would have called the Hormuz thread dead on a day Qatar extended
a force majeure.
⚠ **Even corrected, none of these is a freshness claim about today** — the newest article is 08-28.
⚠ `data center capex` at n=6/35 is **not** read as quiet (`G1` bars that anyway); it is read as a
**mis-specified multi-word term**, the exact failure the EXIT CHECK names.

### B-4 · Blind-spot pass — `blindspot --days 7 --scope foreign`

Top zero-token emerging terms (title frequency in the pool the fixed term set never sees):
**AI 2,622 · Earnings 1,839 · Nvidia 1,496 · Trump 899 · China 753 · Iran 730 · Bitcoin 623 · Fed 602
· **Warsh 545** · Billion 558 · Canada 451 · Oil 431 · Dollar 422 · Energy 382 · Meta 353 · Japan 348
· **Jackson 346 · Hole 340**.**

⇒ **The blind-spot pass and the event pass agree**: `Warsh` + `Jackson` + `Hole` is the largest
un-tabled cluster in the pool. **New macro terms folded into the living table this run:
`Warsh` · `Jackson Hole` · `rate hike odds` · `force majeure` · `benchmark revision`.**
⚠ **`Dollar` at 422 with `DTWEXBGS` nine days stale** is the same defect from a second direction.
Random-sample rows read raw (8 shown): `TotalEnergies` Q4, `Waymo` to Germany, China–Nepal landslide,
`OpenAI`/"Netscape moment", `Honda` US factory, an 8-K filer, a Walmart retail item — **no rank-jump
of a single name**, so nothing promoted from the sample.

---

## §C · Propositions — falsifiable, both branches, mandatory anti-signal

> **ID 3-grep at write time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `P115`–`P117` ·
> `M1090`–`M1097` · `D411`–`D413` → **0 hits**. IDs issued by `module_evidence next-id` (highest
> before this run: `P114` · `M1089` · `D410` · `S134`), **not hand-grepped**.
> All 08-28 prices are **5m-proxy**, labelled; benchmark named inline (`C1`).
> ⚠ **All three rows below are deliberately keyed to observables the 08-28 ghost bar does not touch**
> (forward windows starting 08-31), so a repeat of today's instrument failure cannot make them
> unscoreable in the way it made the sweep unscoreable.

### `P115` — ★★★ Was 08-28 a repricing of the POLICY PATH, or of one speech?

**Claim to falsify**: *the Warsh speech moved the **level** of expected policy, so the front end must
follow it and stay followed — it was not a one-session sentiment event.*

**Anchors**: `[news]` §B-1 — 7 clusters, 21/19/11/6/6/6/5 outlets, **primary source `federalreserve`
in the evidence list**; Barron's subevent *"Markets See a September Rate Hike"*; Reuters VIEW
*"Rate-hike expectations rise."* `[FRED]` `DGS2` **4.20** (91.2nd %ile) at 08-27, i.e. **before** the
speech. `[measured]` `XLF` **+0.59pp** vs `SPY` on 08-28 while `XLK` −1.33pp.
**Thread**: Warsh/Jackson Hole **5→7→13→21, still climbing at the data's edge** (§B-2 — the ENDED tag
is a dark-window artifact and the curve is quoted instead).

**Frozen observable**: **`DGS2`, first `[FRED]` observation covering 2026-09-04 or later**, `[FRED]`,
compared against its **2026-08-27 value of 4.20**.

| branch | threshold | meaning |
|---|---|---|
| **A (the policy path repriced)** | `DGS2` **≥ 4.32** | +12 bp held for a week ⇒ a hike is genuinely in the curve; the desk's duration-sensitive underweights (`UTIL`, `RE`) are a **macro** call, and the IT drawdown has a macro cause |
| **B (one speech, retraced)** | `DGS2` **≤ 4.12** | the front end gave it back ⇒ 08-28 was positioning, and `XLK`'s −1.33 belongs to the **concentration** story (`SMH` −15.31 exc60), not the rate story |
| **C** | between | disclosed as the modal outcome |

- **Band derivation, stated (`C5`)**: `DGS2`'s realised 21-observation range this month is 4.19–4.22
  (3 bp). ±12/8 bp is **4×** that range — deliberately wide, because a 3 bp band would fire on noise.
  ⚠ **Asymmetric and disclosed**: A is +12, B is −8, because 4.20 sits at the 91st percentile already
  and the room above is mechanically thinner.
- ⚠ **Anti-signal (AMBIGUOUS)**: **Aug NFP prints 2026-09-04, inside the window.** A payroll surprise
  moves `DGS2` for a different reason. ⇒ **if the Aug NFP headline misses consensus by ≥100k in either
  direction, this row is AMBIGUOUS, not scored.** ⚠ **Base rate checked and NOT remote** — the
  preliminary benchmark revision just marked job growth **down 79,000** (§B-1), i.e. the labour data
  is actively being restated. **Disclosed as live.**
- ⚠ **`D333` pre-declaration, written in at registration**: `DGS2` publishes one business day in
  arrears. **If the 09-04 bar has not published at the next run, this row is DEFERRED and named, not
  `EXPIRED`.** (This clause is what saved `P110` and `S120`; it is standard here by design.)
- **Information content (`L3`)**: **HIGH on B.** B says two of this desk's underweights are one bet,
  not two — a claim about its own book structure, which is the class of finding `G4` keeps failing to
  settle. A is the direction the tape already travelled and is therefore worth less.
- ⚠ **Non-redundancy (`D343`)**: `P113` (registered 08-29) measures `XLK − XLU` **equity** spread over
  08-28→09-08. This measures the **rate** itself over a later window. They can disagree, and if they
  do, **the disagreement is the finding**.

### `P116` — ★★★ Real yields at the 89th percentile against credit spreads at the 0th — which one is wrong?

**Claim to falsify**: *the joint state (`DFII10` 2.34 = 89th %ile · `HY OAS` 2.63 = 0th %ile ·
`NFCI` −0.566 = 0th %ile · `VIX` 14.51 = 4th %ile) is **stable**, i.e. high real rates are being
absorbed by an economy that can pay them — not a mispricing that resolves toward stress.*

**Anchors `[FRED]`**: all four above, 08-27 (08-21 for `NFCI`), with `T10YIE` **2.31 = 45.6th %ile**
establishing the rise is real, not inflationary (`M1093`). `[news]` `bloomberg` 08-28 *"Warsh's
Hawkish Message Lands as **Real Yields Lead Bond Moves**"* — an independent statement of the same
decomposition. **Thread**: credit has **no thread** in the 7-day top list — **stated as an absence in
the trajectory read, not as quiet** (`G1`).

**Frozen observable**: **`BAMLH0A0HYM2` (HY OAS), first `[FRED]` observation covering 2026-09-18 or
later**, `[FRED]`, against its 08-27 value of **2.63**.

| branch | threshold | meaning |
|---|---|---|
| **A (credit was right; the joint state is stable)** | HY OAS **≤ 2.62** | spreads make a new low *after* a hawkish repricing ⇒ high real yields are not a funding problem, and any "rates are breaking something" sector call is narrative-only |
| **B (credit was late)** | HY OAS **≥ 3.00** | +37 bp ⇒ the real-rate level does bite; the `XLU`/`XLRE`/`XLI` weakness gets a funding cause and the AI-capex financing chain (`IREN`'s $2.4bn, §B-1) is the place to look |
| **C** | between | disclosed favourite |

- **Band derivation, stated (`C5`)**: current 2.63, 365-day low = 2.63, 365-day high = 3.46. A is
  **−1 bp** (a new low, mechanically hard) and B is **+37 bp** (45% of the way to the yearly high).
  ⚠ **Deliberately asymmetric and disclosed**: a symmetric band around a series sitting *exactly at*
  its yearly low would make one branch near-certain — the `S61` failure this desk has logged.
- ⚠ **Deliberate relationship to `P108`** (registered 08-28: HY OAS ≤2.60 / ≥2.95 at the first close
  covering **09-11**). **`P108` is NOT re-frozen and stays ARMED on its own thresholds** (`D242`).
  This row runs **one week later with a wider upper leg**; if the two disagree, the disagreement is
  the finding (the `S14-ANNEX` precedent). **Registered as a deliberate near-duplicate, not
  discovered as one.**
- ⚠ **Anti-signal (AMBIGUOUS)**: a **single-issuer default or large idiosyncratic HY event** in the
  window ⇒ widening that is not a macro repricing. ⚠ Second anti-signal: **an index-composition change
  in `BAMLH0A0HYM2`** would move the level without a market event.
- **Information content**: **HIGH on B, MEDIUM on A.** A is the continuation of a state already at an
  extreme; B would be the first funding-side confirmation of a story the equity tape has been telling
  alone for three weeks.

### `P117` — ★★ Hormuz: the two providers disagree about the barrel, and one live row's verdict depends on which you ask

**Claim to falsify**: *the oil complex is pricing a Hormuz reopening that the shipping data does not
show* — the same contest `P107`/`P112` carry, but this row's object is **the instrument**, because
today produced a measurement the earlier rows could not have.

**Anchors.** `[news]` 08-28, both in the head layer, **saying opposite things about the same strait**:
*"Crude heads for weekly losses as **Hormuz flows remain choppy**"* / `nasdaq` *"Crude Prices Slip as
**More Oil Flows Through** the Strait"* [**14 outlets / 22 articles**] **against** `bloomberg`
*"**Qatar Extends LNG Force Majeure** as Hormuz Traffic Remains **Halted**"* + subevent *"**Hormuz
Tanker Traffic Drops** Despite Recovery in Oil Flows"* [**6 / 11**].
`[measured]`, **and this is the new part** — the same barrel, two providers:

| date | `BZ=F` (yfinance) | `DCOILBRENTEU` `[FRED]` | gap |
|---|---:|---:|---:|
| 2026-08-20 | 93.78 | 94.00 | 0.22 |
| **2026-08-21** | **94.39** | **96.92** | **2.53** |
| 2026-08-24 | 92.17 | 92.71 | 0.54 |
| 2026-08-25 | 88.58 | 88.24 | 0.34 |
| 2026-08-28 | **88.10** | *(not published — 3-day lag)* | — |

🚨 **`M1091`-sibling, `[measured]`: `P107`'s branch B is "Brent settled close ≥ 96.00 on any settled
bar through 2026-09-08." On FRED's Brent series that line was TOUCHED on 2026-08-21 at 96.92. On
`BZ=F` it was not (94.39).** ⇒ **`P107` remains ARMED and unfired**, because its registration names
**`BZ=F`** explicitly — **one word in the registration is the entire difference between "neither leg
touched" and "branch B fired."** 🚫 **This is recorded as an instrument finding and is NOT a score**
(`D242` — no threshold improvised, no source substituted). Registered as **`D413`**: *a row whose
threshold sits inside the cross-provider spread of its own observable must say so at registration and
state the tie-break rule.*

**Frozen observable**: **`BZ=F` settled close, any settled bar 2026-08-31 → 2026-09-18**, `yfinance`,
`auto_adjust=False` — **and `DCOILBRENTEU` `[FRED]` read alongside on the same dates**.

| branch | threshold | meaning |
|---|---|---|
| **A (reopening prices through)** | `BZ=F` **≤ 85.00** on any settled bar | the war premium is out ⇒ Energy stands on refining margin alone, **and `R89`/`P83` say the desk has no instrument that separates that margin from the barrel** |
| **B (the shipping story is right)** | `BZ=F` **≥ 95.00** on any settled bar | force majeure and halted transits reassert ⇒ the 08-26 Iran–Oman deal was a headline, not a transit change |
| **C** | neither touched by 09-18 | contested state persists |
| **★ cross-provider leg (scored separately, always)** | does `DCOILBRENTEU` fire a **different** branch than `BZ=F` over the same window? | if yes, **every Brent-keyed row this desk holds is provider-dependent** and `D413` escalates from a note to a blocking rule |

- **Band derivation, stated (`C5`)**: 88.10 ± ~7.8%, set from the realised range the tape traversed
  this month (87.84 low → 94.39 high on `BZ=F` = 7.4% wide) ⇒ reachable in both directions by
  construction (`D216`). ⚠ **The bands are deliberately NOT `P107`'s or `P112`'s** — those stay armed
  on their own thresholds; this one is set on a later window so a three-way disagreement is readable.
- ⚠ **Anti-signal (AMBIGUOUS, both sides)**: **a Venezuela supply event.** *"Venezuela weighs OPEC
  exit"* [**14 outlets / 29 articles**], *"Trump says US has deal for control of 65 billion barrels"*,
  *"Chevron… near deal to invest billions"* [6/7]. **A western-hemisphere barrel shock moves Brent for
  a reason that has nothing to do with Hormuz.** ⚠ **Base rate checked and NOT remote — this cluster
  was 14 outlets on 08-28 alone.** Second anti-signal: an **OPEC+ quota decision** in the window.
- **Information content**: **HIGH on the cross-provider leg** (it is about every future row), MEDIUM
  on A/B (A is the direction the price is already travelling).

---

## §D · ★ SECTOR TRANSMISSION MATRIX — wind direction only (ROTATION's input)

> 🚨 **Built WITHOUT the sweep.** `SECTOR_FLOW_US.json` is empty (`G3`), so there is **no `wflow`, no
> `eqflow`, no breadth and no flipper list** behind any line below. Each row states the axes it *does*
> stand on: **ETF excess vs `SPY` (5m-proxy 08-28)** · **`[FRED]`** · **COT** · **the 08-28 news
> denominator**. ⚠ This is a weaker basis than a normal run's and is labelled as such, not dressed up.
> Wind direction only — ROTATION decides ranks and DEEP slots.

| # | GICS sector | direction | driving prop. | axes it stands on (no sweep) | note |
|---|---|---|---|---|---|
| 1 | **Financials** | **OW** | `P115`(A) · `P116`(A) | `exc60` **+12.19** (2nd best) · `exc1` **+0.59** on the hawkish day · `KRE` exc60 +7.47 · HY OAS 0th %ile | **The only sector whose 60-day leadership and its hawkish-day behaviour point the same way.** ⚠ `exc20` **−0.97** — the month is flat; this is a quarter-and-a-day call, and the middle disagrees |
| 2 | **Health Care** | **OW** | — (no macro prop; `L2` flag) | `exc60` **+13.99** (best) · `XBI` exc60 **+23.07**, exc20 +7.47 · `exc5` **−2.46 (worst)** | **Rate-insensitive leadership** — the one OW that does not depend on which way `P115` resolves. ⚠ **`MRK`, the carried §3a name, trades ABOVE its mean target (upside −4.4%) ⇒ `L2` peak-margin lens binds** |
| 3 | **Information Technology** | **N** (from a carried OW) | `P113` · `P115`(B) | `exc20` **+2.90 (best)** vs `exc1` **−1.33 (worst)** · `SMH` exc60 **−15.31** vs `XLK` −7.38 | 🚨 **The sign flip is the call** (`M1097`). Cut to **N** not because the month broke but because **the quarter is already broken underneath it** (`SMH`) and one speech took the top off in a session. **A single number cannot rank this sector today** |
| 4 | **Communication Services** | **N→OW-lean** | — | `exc1` **+1.63 (best)** · `exc5` **+0.94 (best)** · `exc20` +1.38 | **The only sector positive on all three short windows.** ⚠ `exc60` −1.21 and a possible one-name driver (**Meta's $18bn settlement**, 5 outlets, 08-28) — **G3 is dead, so I cannot test top-1 dependence.** ⇒ held at **N with an OW lean**, and the untestable concentration is the reason it is not a clean OW |
| 5 | **Materials** | **N** | — | `exc20` **+2.44** (2nd) · `exc5` −1.17 · **Copper COT 100th %ile 🟢 crowded-long** | ⚠ **The crowded-long is the whole caution**: the sector's best axis and its most extreme positioning are the same metal. Contrarian ammunition points **down** here |
| 6 | **Energy** | **N** | `P117` · `P107` · `P112` | `exc60` +4.72 · `exc20` +2.23 · `exc5` **−2.02** · `exc1` +0.82 · WTI COT 43rd %ile · **NatGas COT 2nd %ile 🔴** | 🚨 **Held at N, and the reason is instrumental**: `R89`+`P83` mean **no surviving instrument separates refining margin from the barrel**, and `P117` shows **the barrel itself is provider-dependent**. The refiners were the book's two best 08-28 names (`PSX` +1.76, `MPC` +1.47) — **which is exactly the observation the desk is barred from converting into a separation claim** |
| 7 | **Consumer Discretionary** | **N** | — | `exc1` **+1.37** (2nd) · `exc5` −1.16 · `exc20` −2.03 · `exc60` −1.60 | one good session inside a negative month and quarter. **The 08-28 strength is the anomaly, not the trend** |
| 8 | **Consumer Staples** | **N** | `P115`(A) | `exc1` +0.63 · `exc60` +1.97 · `exc5` −1.14 · `exc20` −2.55 | defensive bid on the hawkish day only; no trend |
| 9 | **Industrials** | **UW** | `P114` (registered 08-29) | `exc5` **−2.23** · `exc20` **−4.52** · `ITA` exc20 **−5.88** · `exc1` −0.73 | **Negative on every short window.** ⚠ The competing explanations — **labour** (`−79k` benchmark revision) vs **tariff** (Canada thread peaked at 29 outlets) — are exactly what `P114` was registered to separate, and it is **not** resolved here |
| 10 | **Real Estate** | **UW** | `P115` · `P116`(B) | `exc5` −1.85 · `exc20` **−4.35** · `exc60` +0.18 | rate-sensitive and losing on the month. ⚠ **`XLRE` fell only −0.22 on the hawkish session** — **weaker than `XLK`** — which is evidence *against* reading this as a pure duration trade |
| 11 | **Utilities** | **UW** | `P113` · `P115` | `exc20` **−6.69 (worst on the board)** · `exc60` −4.30 · `exc1` −0.87 | **The clearest UW on the board.** ⚠ And the one whose thesis is entangled with the book: `ETN` (AI-power) fell **−3.21%** on 08-28. **Whether `XLU` and the AI-power leg are one bet is `P113`'s question and is unmeasured** (`G4` gives 11 units at 250d and 10 at 500/750d, with different memberships) |

**Wind direction, one sentence**: **a hawkish policy repricing at 91st–94th-percentile yields with
0th-percentile credit spreads favours the sectors that get paid by rates (`FIN`) or ignore them
(`HLTH`), and penalises the ones that pay them (`UTIL`, `RE`, `INDU`) — with `IT` genuinely
two-sided** because its month is the board's best and its quarter (via `SMH`) the board's worst.

---

## §E · Self-backtest — this desk's own hit rate

### E-1 · Live rows — status, with every deferral named

| row | status | note |
|---|---|---|
| **`P106`** (`RSP` exc5 vs `SPY`, 08-27→09-04) | ⏳ **not due** | 1-session preview `RSP` −0.13pp. **Explicitly not a score** |
| **`P107`** (Brent `BZ=F` ≤84.00 / ≥96.00 through 09-08) | ⏳ **ARMED, neither leg touched on its named instrument** | `BZ=F` 88.10 (08-28) — 4.10 above A, 7.90 below B. 🚨 **On FRED's Brent, B was touched at 96.92 on 08-21** — see `P117`/`D413`. **Not scored; the row names `BZ=F`** |
| **`P108`** (HY OAS at first close covering 09-11) | ⏳ **not due** | HY OAS **2.63** = 3 bp above branch A (≤2.60). Pre-settle read disclosed, **not scored** |
| **`P109`** (2nd ≥$10bn memory-**capacity** commitment, ≥3 outlets, by 09-30) | ⏳ **ARMED — and a 2nd candidate appeared today and is REJECTED on the row's own words** | See E-2 |
| **`P110`** (`DGS2` at first `[FRED]` close covering 08-28) | ⏸ **DEFERRED for a 2nd run, exactly as pre-declared** | `DGS2` still ends **08-27 at 4.20**; A ≥4.30 / B ≤4.08 ⇒ mid-C. ✅ **The lag clause is now 2-for-2** |
| **`P111`–`P114`** (registered 08-29; settle 09-04 → 09-14) | ⏳ **not due** | ⚠ `P111`'s window opened 08-28: `EW{MU,SNDK,WDC}` is **1 of 10 sessions in**. Not previewed — see `M1057` |
| **`P115`–`P117`** | 🆕 registered this run | settle 09-04+ / 09-18 / 09-18 |

### E-2 · ★ The second candidate that could have been scored wrongly, and was not

**`P109` branch A** requires *"a second, separately-sourced **≥$10bn memory-capacity commitment**
(any of DRAM/NAND/HBM, **any producer**) reported by ≥3 outlets."*
**Found on 08-28**: ***"SK Hynix starts construction of $5 billion memory hub in Indiana"*** — **5
outlets / 6 articles**. Producer ✅ (SK Hynix is a producer, unlike the `NVDA` case the 08-29 run
rejected on exactly that word). Capacity ✅ (construction of a memory hub). Outlets ✅ ≥3.
🚫 **It does not fire branch A: $5bn < $10bn.** ⇒ **`P109` stays ARMED**, and the candidate is recorded
with its sources so a later run can revisit on evidence.
★ **The pattern across the two rejections is worth more than either**: `NVDA`'s $279bn/$160bn failed on
**actor class** (buyer, not producer) and SK Hynix's $5bn fails on **magnitude** — i.e. **the row's two
qualifying conditions have each been the binding one once, and never together.** That is evidence the
row is *well* specified, not evidence it is unreachable. **No threshold improvised** (`D242`).

### E-3 · Running hit-rate and the pattern in the misses

**No verdict was added since the 08-29 run** (no session, no `[FRED]` maturation). The standing record
is carried unchanged and **is not restated as if it were new**:
`S101` C · `P78` B · `P80` C · `S115` A · `P90` A · `S117` B · `P77` A · `S79` A/U-MIXED ·
`S81` C(ambiguous) · `P83` B · `P96` B · `S119` C · `S116` C · `S118` C ⇒ **14 verdicts: A×4 · B×4 ·
C×5 · 1 mixed. C = 5/14 = 36%.**
- **`M1057` (carried)**: the pre-settle read has pointed **the wrong way three times** (`S101`, `P78`,
  `P96`). ⇒ every pre-settle number in §E-1 carries that warning; none is treated as a weak verdict.
- **`M1058` (carried)**: **two of four B-verdicts killed an instrument rather than confirming a
  direction.** ★ **This run adds a third data point to that pattern without a new verdict**: `P117`
  shows a *live* row (`P107`) whose branch depends on the provider. ⇒ **the desk's scoreboard is still
  doing more instrument testing than direction testing**, and `D413` is the attempt to convert that
  from a recurring surprise into a registration-time question.

### E-4 · 🚨 What this stage asserted and then refuted (`§4c` / `D48`)

**PREFLIGHT G1 (mine, ~90 minutes earlier) wrote: *"✅ Live authority: direct queries at every entry
point — 6/6 pre-sweep and 4/4 post-sweep."* That sentence is true and its implication is false.**

Both probes ran `--days 7`. A 7-day count is dominated by 08-23→08-28 and **cannot see that 08-29
returned 3 articles and 08-30 returned 0.** I found it only because `thread --days 7` printed a
per-day denominator line and every thread came back ENDED. ⇒ **the news *index* is queryable and the
news *ingest* is two days dark, and my own gate could not distinguish them** — the exact
"instrument returns a plausible number" class this desk's PREFLIGHT exists to catch, reproduced **by
PREFLIGHT itself.**
- **The PREFLIGHT text is not edited.** The additional removed right is in §0 of this file and the dig
  is **`D411`**: *G1's liveness probe must include a **same-day** count, not only a 7-day count.*
- ✅ **What survives unchanged**: the *permission*. Direct queries do work; 5/5 sweep-failed names
  answered. **What dies is the freshness implication**, and every velocity number in §B-3 is corrected
  for it rather than being quietly used.

⚠ **The adversarial checks that survived, reported because zero self-refutations usually means the
controls were not adversarial**: (i) the two-provider index reconciliation (§A-0, 2.6 bp), (ii) the
`BZ=F`-vs-FRED Brent comparison, which was run *hoping* to confirm `P107` and instead found a
threshold-crossing disagreement, and (iii) the naive-vs-corrected velocity table, which was computed
both ways specifically so the correction could be seen to matter (Hormuz 0.80 → 1.04).

---

## ✅ EXIT CHECK
- [x] Catalysts injected (`catalyst_calendar --days 14`, §10 of `HANDOVER.md`: **5 binaries**, MSCI review **D-1 inside 48h**); narrative read (**events + trajectories + 7-bucket + blind spot**); indicators read (**FRED primaries + COT positioning**); **daily anchor** = the 08-29 `MACRO_REPORT.md` read in full (its `P111`–`P114` carried in §E-1, its `M1057`/`M1058` carried in §E-3).
- [x] Events read via `--body 2`; **tail = 0**.
- [x] **`tail = 0` is NOT treated as the coverage claim** — `single_source` **15 shown / 624 total ⇒ 609 withheld** (`min_nb` 10.0); `excluded_nonmarket` **0 / 0**; `subevents_recovered` **224**. Every "the day held X" statement in §B-1 is scoped to the **2+-outlet** layer and says so.
- [x] **Denominator is the corrected one**: **4,490 articles** after `excluded_not_news` (**empty this run**, stated rather than assumed).
- [x] Trajectories read (`thread --days 7`): every proposition names its thread's tag **and curve**. 🚨 **The ENDED tags are a dark-window artifact** (`M1090`) and the curves are quoted in their place — stated in §B-2, not silently worked around.
- [x] **Every "nothing happened in bucket X" claim carries its denominator** — and in fact **no such claim is made**, because `G1` bars it and `D411` shows why the 7-day counts could not support one.
- [x] **No bucket's low count is trusted**: `data center capex` (6/35) is read as a **mis-specified multi-word term**, not as quiet. All terms passed as separate argv.
- [x] **Both halves of every headline print**: CPI **+3.30% YoY / +0.07% MoM**, core CPI **+2.47% YoY / +0.22% MoM**, M2 **+5.41% YoY / +0.44% MoM**, consumer sentiment (**down** on level, **improving** on year-ahead inflation views) — like-for-like windows.
- [x] **Every relative-performance number names `SPY` inline**; no statistical result carried across markets (the `vol_surge` IC stays `market=kr`, `W1`, `HANDOVER §5`).
- [x] **Credit axis read and cited**: `hy_oas` **2.63 = 0.0th %ile** + `nfci` **−0.566 = 0.0th %ile** + `ig_oas` 0.79. No stress claim is made anywhere; where one might be implied it is labelled **narrative-only** (§A-2, §D-6).
- [x] **`real_10y` quoted with `breakeven_10y`**: **2.34 (89.0th %ile) vs 2.31 (45.6th %ile)** ⇒ the move is real, not inflationary (`M1093`), corroborated independently by `bloomberg` 08-28.
- [x] **Linter run on this stage's own output** — `report_lint.py MACRO_REPORT.md` ⇒ **0 findings** across C1/C2/S6/D6. ⚠ It checks **form only**; a clean run is not a correct report, and §E-4 is the substantive error this run found in itself.
- [x] **Transmission matrix produced, all 11 GICS sectors, one line each** (§D) — 🚨 with the sweep-free basis stated on every row.
- [x] `MACRO_REPORT.md` written with primary numbers explicit; **self-backtest carried and explicitly not restated as new** (§E-3); **new blind-spot terms folded into the living table** (`Warsh` · `Jackson Hole` · `rate hike odds` · `force majeure` · `benchmark revision`).

---

## 🚨🚨 POST-HOC CORRECTION — `M1090` / `D411` are REFUTED. Appended 2026-08-30 23:3x KST, not edited away (`D48`)

**What this report claimed (§0, §B-2, §B-3, §E-4):** *"the foreign news ingest has been dark for two
days — 08-29 = 3 articles, 08-30 = 0"*, and every velocity in §B-3 was "corrected" for those two dark
days.

**What refuted it.** The `SECTOR_DEEP_HLTH` agent reported that a live query returned foreign articles
dated 08-29 and 08-30, and **wrote the contradiction down instead of resolving it silently**. I checked
it and the agent was right.

**The mechanism, read from source — this is not an outage, it is a mirror I failed to sync:**
`module_news_data/__main__.py:50` defines
`DB_READ_CMDS = {search, fts, coverage, blindspot, theme-age, chain-hop, burst, export, drift}` —
these route to the **remote server index**. The comment two lines above states that `embed`, `cluster`,
**`brief`** and **`thread`** are *deliberately excluded* because they read a **client-side**
`data/news_vectors.db`. `embed status` showed that mirror's cursor at **2026-08-29T09:04:46** — the
moment the KR desk last synced it.
⇒ **The server index was current the whole time. The client mirror was 38 hours stale.**
⇒ 🚨 **And the MACRO L2 spec says, in its own words, *"Events (`brief --body 2`, run `embed sync`
first)"*. I did not run it.** This was a procedural miss by this run, not a pipeline defect.

**Measured after running `embed sync`** (6,405 new articles embedded, cursor → 2026-08-30T22:26):

| `--scope foreign` | before sync | **after sync** |
|---|---:|---:|
| 2026-08-28 articles | 4,490 | **4,895** |
| 2026-08-29 articles | **3** | **1,676** (295 market events) |
| 2026-08-30 articles | **0** | **702** (123 market events) |

⇒ The weekend is genuinely **lighter** (295 and 123 market events against ~800 on a weekday) but it is
**not dark**, and "dark" was the word this report built on.

### What is WITHDRAWN

1. 🚫 **`M1090` is withdrawn.** Replacement, `M1104` `[measured]`: *the client-side `brief`/`thread`
   mirror was 38 hours stale because `embed sync` was not run; the remote index was current.*
2. 🚫 **§B-3's "dark-day-corrected velocity" column is withdrawn in full.** `fts search` is a **remote**
   call, so its 7-day and 30-day counts **already contained** 08-29 and 08-30. The correction divided
   by a denominator that was never missing. **The NAIVE column was the correct one**, and the
   conclusions flip back with it — most consequentially **Hormuz reads 0.80 (fading), not 1.04
   (flat)**, and `tariff` reads 1.29, not 1.68. ⚠ **The paragraph that said an uncorrected reading
   "would have written a systematically calmer macro than the data supports" is exactly backwards:
   the correction wrote a systematically LOUDER one.**
3. ⚠ **§B-2's ENDED-tag observation SURVIVES as an observation but its cause changes.** Every thread
   did read ENDED on the default window — because `thread` reads the stale mirror. The fix is
   `embed sync`, not a window shift. Re-run after syncing: **50 alive threads** on the 08-24→08-30
   window, per-day 791 / 832 / 832 / 854 / 733 / **295** / **123**.
4. ✅ **§B-1's event read SURVIVES.** It was taken from the 08-28 brief, which the mirror covered.
   The denominator is restated as **4,895 articles** (from 4,490); the head-layer clusters and the
   Warsh evidence are unchanged.
5. ⚠ **`D411`'s prescription is REPLACED.** Old: *"G1's liveness probe must include a same-day count."*
   That would NOT have caught this — a same-day `fts` count is a **remote** call and would have looked
   healthy. New (**`D418`**): *G1 compares the CLIENT mirror's cursor (`embed status`) against the
   REMOTE index's newest article date, and the run does not read `brief`/`thread` until the gap is
   closed.* **The defect was invisible to every probe I ran because all of them queried the healthy
   side.**

### What the corrected weekend actually holds (new, and it was unavailable before the sync)

`brief --date 2026-08-30 --scope foreign` — **702 articles / 317 clusters / 123 market events**, head
layer of 6: **"Furore grows as Venezuela defends US oil deal with Trump"** [**9 outlets / 13 articles**]
· "Iceland Set to Reject EU Entry Talks in Tight Referendum" [12/19] · "Death toll rises to 38 from
Russia's deadliest attack on Ukraine this year" [10/11].
★ **The Venezuela item is directly on `P117`'s registered anti-signal** — the row VOIDs on *"a Venezuela
supply event"*, and the cluster grew from 14 outlets on 08-28 to a 9-outlet head item on 08-30 while
this desk was reading a mirror that could not see it. **The anti-signal is live and this is recorded on
the row's own terms, not scored.**
And a new BUILDING thread on the same axis: *"New U.S. sanctions will hit ordinary Iranians hard"* →
*"Iran war live: Tehran stands firm over US sanctions"* (3→3 outlets, 08-29→08-30).

### The two-level lesson, stated because it is the useful part

§E-4 recorded a self-refutation: PREFLIGHT G1 wrote *"direct queries live"* and this stage refuted its
freshness implication. **That refutation has now itself been refuted** — G1's original sentence was
true *and* its implication was fine; what was broken was a third thing neither had measured. ⇒ **Two
levels of correction on one axis in one run, and the thing that finally caught it was a subagent
disagreeing with its own brief and saying so.** `M1105`.


---

# §5 · ADDENDUM — DRIFT WATCH (Stage 11, post-run) · appended 2026-08-30, never clobbered

`drift_watch.py --report MACRO_REPORT.md` → **✅ no kill-switch burst.**

⚠ **And that verdict is nearly uninformative, which the tool says itself**: it watched
**0.4 hours** after the report's completion stamp (2026-08-30T23:32). The stage's design intent is
**+3–6h**; this run finished at 23:32 KST on a Sunday, so the watch window is a fifth of the shortest
intended one. **A clean burst check over 24 minutes is not evidence the report is not stale.**
Stated rather than reported as a pass.

## 🚨 The drift the burst-counter structurally could not see — and it is on a registered anti-signal

`drift_watch`'s window opens at report-completion time, so it can only see news published **after
23:32 KST**. The material development landed **during the 08-30 session**, hours before the window
opened, and it was found instead by re-reading the day's brief after the client mirror was synced
(see the POST-HOC CORRECTION above).

**`M1108` `[measured]` — the Venezuela cluster changed STATE between 08-28 and 08-30:**

| date | framing | outlets / articles |
|---|---|---:|
| **08-28** | *"Venezuela **weighs** exit from OPEC as US **discusses** stake in oil fields"* · *"Chevron… **in talks** to expand"* · *"US **nears** deal to secure stake"* | 14 / 29 |
| **08-30** | *"Furore grows as Venezuela **defends US oil deal** with Trump"* (`scmp`) · *"Delcy Rodríguez says Venezuela **'retains sovereignty' despite US oil deal**"* (`aljazeera`) · *"**Trump's oil deal** riles both sides of Venezuelan political divide"* (`japantimes`) | **9 / 13** |

⇒ **The verbs moved from "weighs / discusses / nears / in talks" to "defends the deal" and "despite
the deal".** Fewer outlets, but the framing across all three is a **concluded** arrangement being
politically defended, not a negotiation being reported.

**Why this matters to a live row, stated precisely and NOT scored:**
- **`P117`** (registered this run, settles 2026-09-18) carries the VOID condition *"a **Venezuela
  supply event** — a western-hemisphere barrel shock moves Brent for a reason that has nothing to do
  with Hormuz"*, and the row's own text says **"base rate checked and NOT remote."**
- **`P107`** (≤84.00 / ≥96.00 through 09-08) and **`P112`** (through 09-11) are exposed to the same
  confound.
- 🚫 **No branch is scored, no threshold is touched, and the anti-signal is NOT declared fired** —
  "a deal is being politically defended" is not yet "barrels moved". **What is recorded is that the
  condition advanced a step**, on 9 independent outlets, inside the window the rows are live in.
  ⇒ **The next run inherits this as a dated observation to check first**, not as a verdict.

**A second, smaller item on the same axis**: a BUILDING thread *"New U.S. sanctions will hit ordinary
Iranians hard"* → *"Iran war live: Tehran stands firm over US sanctions"* (3→3 outlets, 08-29→08-30),
plus *"Investors prosper and consumers pay as the Iran war exacts an uneven economic toll 6 months
in"* (AP). **Sanctions tightening and a western-hemisphere supply deal are opposite-signed for
Brent** — which is exactly why `P117` was registered two-sided.

## What this stage adds to the desk's own instrument record

★ **`D422`** — *`drift_watch`'s window is anchored to the report's completion time, so a same-day
development that precedes completion is invisible to it by construction.* On a run that finishes near
midnight local time, that excludes **the entire session the report is about**. **Positive form**: the
drift check runs against **the later of (report completion − 24h, the last populated news day)**, not
against completion alone. ⚠ This is the second window-definition defect this run found in a
timing-sensitive instrument (the first was the client mirror's cursor, `D418`), and both share a
shape: **the tool measured from the wrong end of the window and returned a confident, clean number.**

✅ **Anti-signals the tool echoed back for human cross-check** (unchanged, none independently fired):
Aug NFP 09-04 inside `P115`'s window · a single-issuer HY default or index-composition change inside
`P116`'s window · **a Venezuela supply event or an OPEC+ quota decision inside `P117`'s window — the
one above.**
