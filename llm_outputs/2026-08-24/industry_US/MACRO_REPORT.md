# MACRO_REPORT — industry_US · 2026-08-24 (Mon) · Stage 3 / L1·MACRO

> Run clock **KST 22:3x–23:2x = ET 09:3x–10:2x, MONDAY.** US cash **opened at 09:30 ET during this
> stage.** Terminal settled bar **2026-08-21 (Friday)** — the third consecutive run on one close.
> All news calls `--scope foreign`, all made **outside a sweep window**.

## ★★★ The one thing this report exists to say today

**The desk's largest macro object is one its own instruments ranked 21st, labelled FADING, and called
an echo — and today a single change of search width overturned all three readings at once.**
`theme-age tariff` on a **9,876**-article base reads **⚪ECHO 1.14×**. `theme-age "Canada tariff"` on a
**69**-article base reads **🟡ACCELERATING 9.86×**. Same event, same day, same tool: **8.7× difference
in the velocity ratio, produced entirely by the width of the term** (`M861`). Meanwhile `brief` ranked
US–Canada trade-talk collapse the **#1 event of 08-23 at 38 articles / 20 outlets**, and `thread`
placed it **outside its top-20**, one-lined in the tail, tagged **FADING** on a curve reading
**19→23→9→11→24→20→14** (`M862`).

⇒ This is not three instruments disagreeing about the world. **It is three instruments being asked
badly-scoped questions, and yesterday's `P92` explicitly recorded the disagreement as unresolved
(*"two of the desk's instruments disagree about whether this happened"*). It is resolved today, in
favour of "it happened," by a measurement rather than a judgement.**

---

## §0 · What this report may not claim, stated before the numbers

Inherited verbatim from `preflight/PREFLIGHT_US.md` (PASS 3 / FAIL 5) and `HANDOVER.md §0`:

1. ★ **No "since our last run" language on any price.** `n_new_sessions_since_prior_run = 0`, second
   run running; the persisted sweep is element-identical to 08-23's and 08-22's.
2. ★ **A post-09:30-ET quote is a LIVE INTRADAY PRINT and is labelled one.** Two are used below
   (Brent/WTI in §B-2, and `BABA` in §B-5) and both carry the label. Neither enters the
   `asof = 2026-08-21` frame.
3. **No sweep news-velocity citation** (`vel_coverage = 0.0`). **No "quiet / cooling" verdict from
   sweep silence** — 40/40 falsified today, 400/400 cumulative.
4. ★ **No description of the news-coverage defect as random.** The bucket is **universe ranks 0–48,
   contiguous, 49/49 identical across days, 16.4% by count and 69.0% by market cap.**
5. **No Consumer Staples promotion/demotion on `wflow`** (`WMT` 28.9% flips the sign) · **no bare
   concentration number** (`--days` on the same line) · **no cap-weighted claim on a 40-day-old
   universe** · **no flow/RS/OBV/short verdict on `EA`** · **no `--ic`-derived size as evidence.**
6. ★ **Every FRED number below carries its own last-observation date** (`D333-KR`), and **no two FRED
   series are added or differenced across different dates.**

---

## §A · Primary indicators — `[FRED]`, with 365-day percentiles and both halves

Pulled twice, by two independent paths (`module_macro_us --json`; a direct `api.stlouisfed.org` call).

### A-1 · The shape: the policy rate at its yearly LOW, the long end at its yearly HIGH

| Series | Value | Last obs | 365d percentile | Range |
|---|---:|---|---:|---|
| `DFF` effective fed funds | **3.63** | 2026-08-20 | **9.1%** | 3.62 – 4.33 |
| `SOFR` | 3.65 | **2026-08-21** | 37.5% | 3.50 – 4.51 |
| `DGS2` | **4.19** | 2026-08-20 | 88.7% | 3.38 – 4.37 |
| `DGS10` | **4.69** | 2026-08-20 | **96.0%** | 3.97 – 4.75 |
| `DGS30` | **5.23** | 2026-08-20 | **96.4%** | 4.54 – 5.31 |
| `DFII10` real 10y | **2.35** | 2026-08-20 | 89.5% | 1.67 – 2.47 |
| `T10YIE` 10y breakeven | **2.34** | **2026-08-21** | **59.0%** | 2.18 – 2.50 |

★ **`DGS2` has printed 4.19 on four consecutive sessions — 08-17, 08-18, 08-19, 08-20 — straight
through the 08-19 FOMC minutes** (`M859`). Its realised 12-observation range is **4.15–4.25**. The
front end did not move on the minutes at all; whatever repriced, repriced further out.
`30y−10y`: **0.59 (08-17) → 0.57 → 0.54 → 0.54 (08-20)** — the curve's long end *flattened* over the
same four sessions.

### A-2 · Real versus breakeven — the long-end level is REAL, and the percentile gap says so cleanly

**`DFII10` sits at the 89.5th percentile of its own year while `T10YIE` sits at the 59.0th.** Quoted
together, per the standing rule: a 10-year yield near its yearly high is being carried by the **real**
leg, not by inflation compensation. Breakeven is unremarkable; the real yield is nearly a yearly high.
⚠ **They are NOT summed here.** `DFII10` ends 08-20 and `T10YIE` ends 08-21 (`D333-KR`). On the
**common** date 08-20 the identity closes (2.35 + 2.34 = 4.69 = `DGS10`), and `D333-KR` already logged
that this closes **coincidentally** because breakeven printed 2.34 on both days.

### A-3 · Inflation — both halves, on a date-matched base (`D326` applied, not merely cited)

| | Level (2026-07) | **YoY, date-matched** | **MoM, sequential** |
|---|---:|---:|---:|
| `CPIAUCSL` headline | 332.813 | **+3.30%** | **+0.07%** |
| `CPILFESL` core | 336.789 | **+2.47%** | **+0.22%** |

⚠ **The base month is fetched by DATE (`2025-07-01`), not by position.** `D326` recorded that
`CPIAUCSL`/`CPILFESL` are **missing `2025-10-01`**, so `obs[-13]` overstates YoY by ~0.24pp headline
and ~0.32pp core, in the hawkish direction. The figures above are the date-matched ones and reproduce
the 08-23 run's corrected values exactly.
★ **Both halves disagree in direction and both are quoted**: headline YoY is elevated (+3.30%) while
its **sequential print is +0.07% — essentially flat**; core is the mirror, a lower YoY (+2.47%) on a
**firmer** monthly (+0.22%). ⚠ **These are July data released in August — one month stale, stated
rather than dressed as current.** **July PCE prints 2026-08-28 (D-4, `[bea~est]`, 🔀binary).**

### A-4 · Credit and conditions — the divergence persists, and it is still not a stress signal

| | Value | Last obs | 365d percentile |
|---|---:|---|---:|
| `BAMLH0A0HYM2` HY OAS | **2.75** | 2026-08-20 | **23.3%** |
| `BAMLC0A0CM` IG OAS | **0.82** | 2026-08-20 | **77.9%** |
| `NFCI` | **−0.559** | 2026-08-14 | **7.8%** — loosest of the year |
| `VIXCLS` | 16.01 | 2026-08-20 | 25.0% |
| `RRPONTSYD` | 0.200 | **2026-08-21** | 4.4% |
| `WALCL` Fed assets | 6,745,699 | 2026-08-19 | (−14.3bn w/w) |

★ **The divergence carried from 08-23 is intact and measured again: HY OAS near its yearly LOW (23rd
pctile) while IG OAS sits at the 78th** (`M860`). Two credit instruments, opposite percentiles.
🚫 **Any "credit stress" claim in this run is `narrative-only`** — the credit axis was read and it does
not support one. `NFCI` at the **7.8th percentile** says financial conditions are the loosest they have
been in a year; that is the opposite of stress.
⚠ **`NFCI` is weekly and ends 08-14 — ten days stale.** It is quoted as a slow-moving condition index,
not as a reaction to anything that happened last week.
★ **The narrative that fits this table is supply, not fear**: policy rate at a yearly low, long end at
a yearly high, real yields doing the work, credit calm, conditions loose, RRP drained to 0.200.
`theme-age "national debt"` reads **🟡ACCELERATING 7.82×** on a 278-article base, and `brief` carried
*"The U.S. National Debt Officially Surpassed $40 Trillion"* at 6 outlets — **the term-premium story
has a live narrative leg, which last week it did not** (`M863`).

### A-5 · Positioning — `[COT, Tuesday 2026-08-18 close, published Friday]` ⇒ context, not a trigger

| Instrument | Net spec | Wk Δ | 1y %ile | Tool label | **This desk's reading** |
|---|---:|---:|---:|---|---|
| S&P 500 e-mini | **−10,560** | −21,840 | 84% | 🟢 crowded-long | 🚨 **UNUSABLE — `D327`, 3rd run.** Net spec is **NEGATIVE**; "84th percentile" of an all-negative year means **least-short**, not long |
| Nasdaq-100 | −12,067 | +30,838 | **4%** | 🔴 crowded-short | usable — extreme short, and it **covered 30,838 into the week** |
| Russell 2000 | −15,706 | −1,763 | 15% | 🔴 crowded-short | usable |
| UST 10Y | **−946,961** | −31,908 | **5%** | 🔴 crowded-short | usable, and it is the board's largest short base — **added to, not covered** |
| UST 2Y | −927,337 | +93,706 | 70% | 🟡 neutral | covering |
| USD Index | +19,079 | −2,330 | 76% | 🟡 neutral | — |
| WTI | +29,164 | +5,938 | 36% | 🟡 neutral | length **added** into the Hormuz week |
| Nat Gas | −203,503 | −6,368 | **0%** | 🔴 crowded-short | usable — the board's only 0th percentile |
| **Copper** | +79,748 | −640 | **100%** | 🟢 crowded-long | ★ usable (range straddles zero) — **the board's only 100th-percentile long** |
| Gold | +222,189 | +4,249 | 48% | 🟡 neutral | — |

★ **The two extremes point opposite ways and both are legitimate**: `Copper` at the **100th** percentile
long, `Nat Gas` at the **0th** percentile short. **Extreme percentiles are contrarian ammunition, not
direction (P4)** — and the data is **3–4 days stale by construction**.
🚨 **`D327` reproduced a third time**, and today it is worse than a label problem: the S&P row *also*
shows the **largest weekly swing on the board (−21,840)** while the label stays 🟢. **A reader taking
the label at face value inverts both the level and the change.**

---

## §B · Narrative — events, trajectories, and the width problem underneath all of them

### B-1 · Denominator, stated before any "quiet" claim (P4)

`brief --date 2026-08-23 --scope foreign --body 2 --singles-nb 5`:
**1,634 articles → 303 events → 303 market / 0 non-market.**
Layers: **head 34** (≥5 outlets) · **body 269** (2–4) · **tail 0** · **single-outlet 15 shown of 280** ·
non-market boundary band **0 of 0**.

🚨 **`tail = 0` is emphatically NOT the coverage claim here, and on the US desk it cannot be.** The
tool prints the reason itself: *"280 of the single-outlet items **have no score** — the classifier is
Korean-only. Not low: unmeasured. A random 15 are shown."*
⇒ **`265 of 280 single-outlet foreign events were not seen, and the 15 that were are a random draw**
(`M864`). **`--singles-nb 5` did nothing on this desk** — there are no scores to threshold against.
★ **This retires, for the US desk, the KR remedy `D334-KR` prescribed** (*"lower `--singles-nb` to 5
and report the residual"*): lowering the cut cannot work where the field is null. ⇒ **`D339`.**
⚠ **And the layer demonstrably carries macro material**: even in a random 15, two macro items appeared
— *"US vows 'economic D-Day' as Iran threatens to halt all oil"* `[google_en]` and *"What's Pushing
Long-Term Bond Yields Higher?"* `[seekingalpha]` — the exact two axes §A-1 and §B-2 are about.
⇒ **Every "nothing in bucket X" sentence in this report is qualified by: 265 unseen single-outlet
events, drawn from at random.**
Also withheld: **61 sub-events** swallowed by larger clusters at the 0.65 threshold.

### B-2 · What the head actually carried, 2026-08-23 — and it is a trade war, not a chip cycle

| Cluster | Articles / outlets | Why it matters here |
|---|---|---|
| ★★★ **Canada — Carney refuses Trump's "bait"; US–Canada talks COLLAPSE over new tariffs** | **38 / 20** — the day's largest by **3.2×** | Sub-clusters name it plainly: *"US-Canada trade talks collapse over new tariffs"* `[朝日新聞]` · *"Trump Just Restarted the Trade War With Canada"* · *"Stock futures slip as U.S. and Canada appear headed for trade [war]"* · *"Canada Turned Down a US Tariff Deal"* |
| Zelenskyy rejects election call | 12 / 9 | — |
| Exxon: *"One of Exxon's Biggest Oil Fields Is Running Out of Room"* | 11 / 7 | Feeds §B-5 |
| **Alibaba $10bn Hong Kong placement to fund AI** | 10 / 7 | AI-capex financing migrating to HK equity |
| **IPO fever: OpenAI and Anthropic** | 12 / 6 | *"Anthropic's Investors Want a $2 Trillion IPO"* |
| Iran condemns new US sanctions | 7 / 6 | `S74` leg, §B-4 |
| *"What to Expect in Markets This Week: Nvidia Earnings"* | 10 / 5 | D-2 |
| **US national debt passes $40 trillion** | 6 / 5 | §A-4's term-premium leg |
| Amazon FCF **−$7.6bn** | 25 / 5 | AI-capex cash cost, printing at a hyperscaler |

⚠ **LIVE INTRADAY PRINT, not a settled bar:** Brent **−1.3% to $93.16**, WTI **−1.9% to $85.42**, quoted
at **04:32 ET 08-24** in a wire body, attributed to Iran granting transit permits to some Iraqi tankers.
**It is not in this run's `asof = 2026-08-21` frame.**

### B-3 · Trajectories — `thread --days 7 --scope foreign`, and every FADING label is unreadable today

Per-day denominators: **08-18 824 · 08-19 826 · 08-20 827 · 08-21 771 · 08-22 288 · 08-23 303 ·
08-24 336 (partial, 09:1x ET).**
⇒ The last three days run at **35% / 37% / 41%** of the weekday median (~824).
🚫 **Every `FADING` and `ENDED` label in this window is therefore unreadable, and no thread is included
or excluded by its label in this report** (`D328(b)`, reproduced on the US side).

**Threads read (top-20 of 129 alive ⇒ 109 seen only as one-liners):**
- **BUILDING 2→4→16**, `Shein` HK IPO — **$1.77bn sought at a $27bn valuation** (08-24, 22 articles /
  16 outlets). Paired with **Alibaba $10.2bn** (7→9 outlets) ⇒ **two large Hong Kong equity raises in
  48 hours**, both AI-adjacent in stated use of proceeds.
- **BUILDING 4→4→7→5→7**, the risk-appetite thread — *"Investors try to catch a falling knife"* →
  *"Investment market volatility is 'here to stay'"*.
- **REIGNITED 6→14→10→5**, Korea–US joint drills scaled back / **US cancelled joint marine drills**.
- **REIGNITED 14→2→2**, Hormuz — *"Hormuz Tanker Traffic Slumps as U.S. and Iran Trade Threats"* (08-24).
- One-liner tail, and this is the finding: `[FADIN] 19→23→9→11→24→20→14 Canada announces retaliatory
  tariffs on U.S. goods` — **the largest sustained outlet curve on the board, ranked 21st or worse and
  tagged FADING** (`M862`). ★ **This is `D335-KR` reproduced on the US desk, and it is the second
  consecutive day the same object slipped the same instrument.**

### B-4 · Theme age — ★★★ the run's central measurement: **the ratio is a function of term width**

All `theme-age … --scope foreign`, each term passed as **one quoted argv** (`D324` guard), all outside
a sweep window:

| Term | Verdict | Age | Ratio | Base (90d) |
|---|---|---:|---:|---:|
| `tariff` | ⚪ ECHO | ≥90 | **1.14×** | **9,876** |
| ★ **`Canada tariff`** | 🟡 **ACCELERATING** | ≥90 | ★ **9.86×** | **69** |
| ★ **`retaliatory tariffs`** | 🟡 **ACCELERATING** | 73 | **3.78×** | 101 |
| `sanctions` | ⚪ ECHO | ≥90 | 1.32× | 3,600 |
| ★ **`economic D-Day`** | 🟢 **FRESH** | **4 d** | — | 141 |
| `Strait of Hormuz` | ⚪ ECHO | ≥90 | 0.73× | 8,059 |
| ★ **`Iraqi tankers`** | 🟢 **FRESH** | **2 d** | — | **3** ⚠ too thin to rate |
| `Warsh` | ⚪ ECHO | ≥90 | 0.85× | 3,628 |
| ★ **`Jackson Hole`** | 🟡 **ACCELERATING** | ≥90 | ★ **14.9×** | 296 |
| **`Treasury buyback`** | 🟢 **FRESH** | **5 d** | — | 201 |
| ★ **`Nvidia earnings`** | 🟡 **ACCELERATING** | ≥90 | **14.11×** | 118 |
| ★ **`national debt`** | 🟡 **ACCELERATING** | ≥90 | **7.82×** | 278 |
| `AI capex` | ⚪ ECHO | ≥90 | 0.70× | 1,169 |
| `memory prices` | ⚪ ECHO | ≥90 | 0.72× | 927 |
| `refinery` | ⚪ ECHO | ≥90 | 0.85× | 1,647 |
| `bear market` | ⚪ ECHO | ≥90 | 0.91× | 1,384 |
| `gas turbine` | ⚪ ECHO | ≥90 | 0.93× | 396 |
| `Hong Kong IPO` | ⚪ ECHO | ≥90 | 1.28× | 134 |

★★★ **`M861` — the width law, measured three independent times in one session.** Every pair below is
the *same underlying event*, read at two term widths:

| Event | Broad term (base) | Narrow term (base) | Ratio change |
|---|---|---|---|
| US–Canada trade war | `tariff` ⚪1.14× (**9,876**) | `Canada tariff` 🟡**9.86×** (**69**) | **8.7×** |
| US sanctions escalation | `sanctions` ⚪1.32× (**3,600**) | `economic D-Day` 🟢**FRESH, 4d** (141) | ECHO → FRESH |
| Warsh at Jackson Hole | `Warsh` ⚪0.85× (**3,628**) | `Jackson Hole` 🟡**14.9×** (296) | **17.5×** |

⇒ **`D328(a)`'s remedy is correct but too weak.** It said: *report the outlet cluster beside the ratio
when the base exceeds ~2,000 and treat the ratio as unusable there.* **The stronger, positive form:
when the base exceeds ~2,000, do not read the ratio — narrow the term until the base falls under it,
and read the ratio then.** Every one of the three broad terms above is a *category*; every narrow one
names *an event*. ⇒ **`D340`.**
⚠ **The rule has a floor.** `Iraqi tankers` returns a 3-article base at age 2 — narrow enough to be
meaningless. **Usable band, as measured today: roughly 60–2,000 articles.** Below ~50 the ratio is a
count, not a velocity.

### B-5 · Blind-spot pass — `burst`, and it found a named $8bn transaction nobody searched for

`burst --scope foreign` (denominator **1,963** articles, 30-day baseline, universe 665 firms):

| Word | z | Articles | Outlets | Market-relevance |
|---|---:|---:|---:|---:|
| ★ **CHEMICALS** | **13.2** | 6 | 4 | **100%** |
| NAND | 8.5 | 3 | 3 | 100% |
| SEMICONDUCTORS | 8.1 | 6 | 5 | 50% |
| CHEMICAL | 7.0 | 5 | 4 | 60% |
| EXXON | 4.7 | **12** | 5 | 100% |
| *(new words)* PERPLEXITY | — | 9 | 4 | 100% |
| *(new words)* PCE · HBM | — | 5 · 4 | 4 · 2 | 60% · 75% |

★ **`CHEMICALS` carries the highest z on the board and 100% market relevance, and no bucket in this
desk's term table points at chemicals at all.** Body-read before classifying, per protocol:

**Shell is selling its US chemicals business — ~$8bn, four Louisiana sites — and the named interested
parties are `XOM`, LyondellBasell and Apollo** (FT, 08-24; corroborated in bodies at `yahoo_finance`,
`seekingalpha`, `oilprice`, `investing_en`, with a `bloomberg` title) (`M864` companion observation).
★ Note **`XOM` is carried in this desk's standing view as a 🔴RESOLVED *control*, not a thesis** — and
a control that is bidding $8bn for a downstream asset is doing something a control does not do. **This
is a dig, not a re-rating** (§F).
Alongside it, `brief`'s head carried *"One of Exxon's Biggest Oil Fields Is Running Out of Room"*
(11 / 7). ⚠ **LIVE INTRADAY PRINT:** `BABA` shares slid after the $10.2bn placement (08-24 wire).

**New terms folded into the living table:** `Canada tariff` · `retaliatory tariffs` · `economic D-Day` ·
`national debt` · `chemicals M&A`. Removed as unusable at their current base: none — `tariff`,
`sanctions`, `Warsh`, `Strait of Hormuz` are **kept and demoted to category labels**, never read as
ratios (`D340`).

---

## §C · Self-backtest — the exhaustive table, because "nothing was due" and "nobody checked" look alike

**Every registered proposition with a settle date, checked against 2026-08-24:**

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `P65` · `P66` · `P69` · `P70` · `P75` | **ALL settled by the 08-22 run** |
| 2026-08-22 · 2026-08-23 · **2026-08-24** | **none** | — |
| 2026-08-25 | `P79` | armed |
| 2026-08-26 | `P77` · `P78` · `P80` · **`P90`** | armed (`NVDA` print) |
| 2026-08-27 | `P83` · **`P91`** | armed (Jackson Hole opens) |
| **2026-08-28** | `P67` · `P81` · `P85`–`P89` · **`P92`** | armed (July PCE) |
| 2026-09-03 | `P84` | armed |

⇒ **0 propositions due today, exhaustively verified. Hit-rate ledger carried unchanged**, not
recomputed — recomputing an unchanged ledger under a new date is the manufacturing error §0 forbids.

★ **Three pre-settle readings, offered as readings and explicitly NOT as scores:**
1. **`P92` (trade war, settles 08-28).** Its anti-signal — *a US–Canada agreement with a named
   effective date* — **has not fired; the opposite occurred** (talks collapsed, 08-23, 20 outlets).
   Mid-window measurement on the sweep's own equal-weight sector baskets: **Industrials 5-session
   excess vs `SPY` = −1.736pp** against a trailing-60 mean of **+0.437** and sd **1.681** ⇒ **−1.29σ**.
   `P92`'s branch A needs `XLI ≤ −2.50pp`. **Not there; moving toward it.** ⚠ Benchmark named inline:
   `SPY`, whose own 5-session return is **−1.368%**. ⚠ Equal-weight sector baskets are **not** `XLI`/`XLB`
   and are not substituted for them at settle.
2. **`P92`'s framing defect is closed.** It said *"two of the desk's instruments disagree about whether
   this happened."* §B-4 shows they never disagreed — one was asked a category-width question.
3. **`P91` (front end vs long end, settles 08-27).** `DGS2` printed **4.19 four sessions running through
   the FOMC minutes** while `30y−10y` fell **0.59 → 0.54**. Pre-settle, this leans against a front-end
   story. **No score; the observable settles on 08-27.**

---

## §D · Propositions registered this run — both-sided, anti-signals base-rate-checked

> ID check at WRITE time, 3-grep across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `P93`–`P95` **0 hit** in all three. Current highest **`P92`** (2026-08-23 `industry_US`).
> ⚠ `D300-KR` applied: every anti-signal is keyed to a **magnitude** or a **named, dated event**,
> never to "something happens."

### `P93` — ★★★ Is the trade-war escalation carried by the INDUSTRIAL channel, or is it an index-level risk premium?

- **Claim.** `M862`/`M861` establish the object is real and accelerating. **They do not establish where
  it lands.** Industrials is the desk's textbook transmission sector and it is already **−1.29σ** on a
  5-session basis; but the same week's `SPY` fell 1.368% outright, so an index-level de-rating would
  produce a similar-looking sector number.
- **A (industrial channel).** Over **2026-08-21 close → 2026-08-28 close**, the equal-weight
  **Industrials** basket's 5-session excess vs **`SPY`** ≤ **−3.10pp** (= −2.0σ on the trailing-60
  mean +0.437 / sd 1.681; its 08-21 reading is **−1.736**).
- **B (index-level, not sectoral).** Industrials excess **≥ −0.50pp** vs `SPY` **AND** `SPY`'s own
  5-session return over the same window **≤ −1.00%** — i.e. the tape falls and Industrials does not
  underperform it.
- **C** between — **the favourite, disclosed** (`L3`): C spans −0.50 to −3.10pp, ~1.6σ wide.
- **Anti-signal (VOID).** A **US–Canada agreement announced with a named effective date**, or a
  **US tariff proclamation with a named effective date that excludes Canada**, inside the window.
  ⚠ **Base rate checked**: the 08-23 head carries *"Canada Turned Down a US Tariff Deal"* — a deal was
  live and was **refused**, so a dated agreement inside five sessions is well below even odds.
- **Information grade.** **A falsifies** the desk's standing INDU underweight rationale if it fires for
  the wrong reason (index beta, caught by B). **B falsifies** the sector-transmission story entirely.
  Neither branch merely confirms.
- **KPI:** `theme-age "Canada tariff"` (today **9.86×**) and the thread's outlet curve.

### `P94` — ★★ Does the term-premium story have a real leg, or is $40 trillion a headline?

- **Claim.** §A-1 shows the long end at the **96th percentile** with the real leg at **89.5** and
  breakeven at only **59** — a supply/term-premium shape, not an inflation shape. §A-4 shows the
  narrative leg arriving late: `national debt` **7.82× ACCELERATING** on a 278 base, and
  `Treasury buyback` **🟢FRESH at 5 days**. **Two of the three cheapest explanations (fear, inflation)
  are already ruled out by percentile; the question is whether supply is the third.**
- **A (real supply leg).** At the **first close covering 2026-08-27** `[FRED]`: `DGS30` ≥ **5.31**
  (its 365-day maximum) **AND** `T10YIE` ≤ **2.38** — the long end makes a new yearly high **without**
  breakeven confirming.
- **B (it retraces — headline only).** `DGS30` ≤ **5.10** at the same observation **AND** `T10YIE`
  within 2.28–2.40.
- **C** between — the favourite, disclosed. `DGS30`'s realised 8-observation range is 5.19–5.31.
- **Anti-signal (VOID).** A **Treasury refunding announcement or an announced buyback-size change**
  inside the window, or an **intermeeting Fed action**. ⚠ **Base rate checked and this one is NOT
  remote**: `Treasury buyback` is the board's only 🟢FRESH theme (age 5, 201 articles) and `brief`
  carried *"Treasury may tap $1 trillion cash account for bond buy[backs]"* — **the VOID leg is live,
  and it is disclosed as live rather than assumed away.**
- ⚠ **Observation-lag clause, written into the row per `D333-KR`**: `DGS30` and `T10YIE` publish on
  **different lags** (H.15 ~1 business day behind). **This row settles on the first observation where
  BOTH carry 08-27**, and that date is named in the row rather than discovered at settle — which is
  the defect that has left `S102` unsettled for five runs.
- **Information grade.** **A falsifies** any remaining "the long end is inflation" reading. **B
  falsifies** the supply framing this report just built. Neither confirms.

### `P95` — ★ Is the Hong Kong equity-raise cluster an AI-capex financing rotation or a China-local event?

- **Claim.** Two large HK raises in 48 hours — **Alibaba $10.2bn** (7→9 outlets) and **Shein $1.77bn at
  a $27bn valuation** (2→4→16 outlets, BUILDING) — with `Hong Kong IPO` reading only **1.28×** on a
  134 base, i.e. **the instrument does not see a cluster the event tier plainly shows**. If AI capex is
  migrating to HK equity funding, that is a financing-channel fact with US semis on the other side.
- **A (AI-financing rotation).** By **2026-09-05**, **≥2 additional** HK listings or placements
  ≥ **$1bn** whose reported use of proceeds names AI/data-centre/compute, in **≥2 outlet bodies each**.
- **B (China-local).** Zero such additional raises by 2026-09-05, **and** `theme-age "Hong Kong IPO"`
  ≤ 1.5× on that date.
- **C** between (exactly one qualifying raise) — disclosed as a live outcome, not a dodge.
- **Anti-signal (VOID).** A **HKEX listing-rule change or a PBoC/CSRC announcement with a named
  effective date** inside the window that mechanically changes issuance volume.
- **Information grade.** **Low-to-medium, disclosed.** Registered because the desk has **zero** rows on
  the AI-capex *financing* channel while carrying multiple rows on its demand channel — an axis with no
  coverage cannot produce a surprise it can learn from.
- ⚠ **Grade `[news]`, not `[measured]`.** No price threshold; it settles on issuance facts.

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each

> **This is ROTATION's input. It sets wind direction only** — it is not a ranking and it does not
> analyse eleven sectors equally. `flow`/`eqflow` figures are the **08-21 settled** sweep, unchanged
> for three runs. `exc5` = equal-weight basket 5-session excess vs **`SPY`** (named inline), computed
> from this run's own price frame; `SPY` 5-session **−1.368%**.

| GICS sector | Wind | Driving proposition | exc5 vs SPY | flow / eqflow | One line |
|---|---|---|---:|---|---|
| **Energy** | **OW** | `P66` · `P89` · `S74`(`FIRED-C`) | **+3.519** | +0.076 / +0.102 | Hormuz risk **hardened** (fatal strike, seizure) while a *partial* reopening ran on a channel no bracket covered. Crude's live print fell on it — **oil is now two-sided, not one-way** |
| **Health Care** | **OW** | inherited | **+3.889** | **+0.196 / +0.229** | Board's best flow **and** best exc5; the only sector where both instruments agree, and no macro proposition drives it — a **coverage gap, not a conviction** |
| **Materials** | **N+** | `P94` (real rates) · **NEW: chemicals M&A** | +1.813 (median **−0.315**) | +0.064 / +0.046 | 🚨 **Mean and median disagree in SIGN** (`W5`): the +1.813 is carried by a minority. **Copper COT at the 100th percentile** is the standing risk. **Shell's $8bn US chemicals sale with `XOM` bidding** is new and unmodelled |
| **Consumer Staples** | **N** | — | +1.814 | −0.013 / **+0.048** | 🚫 **`wflow` sign unusable — `WMT` 28.9% owns it (G3, 3rd run).** Use `eqflow` **+0.048**. `TGT` +0.950 🟢 vs `WMT` −0.333 🔴 = **17.1pp intra-sector** |
| **Communication Services** | **N** | `P95` | +1.118 | +0.108 / +0.095 | ⚠ **`D297`**: `GOOGL` 38.3% + `GOOG` 38.3% = **76.6%** of the sector while `top1_w` reports half — the flipper test is structurally halved here |
| **Consumer Discretionary** | **N** | `P93` (tariff pass-through) | +0.975 | +0.122 / +0.103 | `AMZN` **40.2%**; ex-top1 flow is **+0.254** vs +0.122 ⇒ the sector is better than its own aggregate |
| **Financials** | **N** | `P94` | +0.877 (median **−0.086**) | +0.003 / −0.034 | Mean/median disagree in sign again (`W5`). Credit axis (§A-4) says **no stress**: HY OAS 23rd pctile |
| **Real Estate** | **N−** | `P94` | +0.295 | **−0.543 / −0.446** | Worst flow but **not** the worst exc5 — the duration underweight's rate beta was measured at **−0.0072** (`S102` note), i.e. ~zero. **The UW rests on flow, not on rates** |
| **Industrials** | **UW−** | ★ **`P93`** | **−1.736** (−1.29σ) | −0.259 / −0.231 | ★ **The run's live transmission channel.** Trade-war object is real and accelerating (§B-4); INDU is the sector that should carry it, and it is 1.29σ down with `P93` armed to settle whether that is the channel or the index |
| **Utilities** | **UW−** | `P94` | **−2.373** · **exc20 −11.469** | **−0.648 / −0.621** | Board's worst on flow **and** on 20-session excess. `gas turbine` reads ⚪0.93× on a 396 base — **no narrative leg is arriving** |
| **Information Technology** | **N** | `P90` · `S115`–`S117` | **−2.655** (worst exc5) | −0.231 / −0.102 | 🚨 **exc5 worst on the board, exc20 +1.992 — the two windows disagree in sign.** **`NVDA` prints 08-26 (D-2, `theme-age` 14.11×)**; `MRVL` 08-27; `AVGO` 09-02. **The sector's next two sessions are an earnings event, not a macro read** |

★ **Two matrix-level cautions, both measured this run:**
1. **`Health Care` is the board's best sector on two independent instruments and has NO driving
   proposition.** That is the matrix's largest hole and it is stated rather than filled with a
   backfilled rationale (P4).
2. **`Materials` and `Financials` both have mean and median excess of opposite sign** — `W5` binds any
   DEEP written on either.

---

## §F · Instrument observations from this stage (dig candidates for `RESEARCH.md` Part C at run end)

> 3-grep at WRITE time across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `D339`, `D340` **0 hit**;
> `M859`–`M864` **0 hit**. Current highest `D329` (US) / `D335-KR` (KR) / `M852`.

| id | Finding | Positive-form remedy |
|---|---|---|
| **`D339`** | 🚨 **On the US desk, `brief`'s single-outlet layer is entirely unscored — the classifier is Korean-only — so `--singles-nb` has nothing to threshold and the tool shows a RANDOM 15 of 280.** Measured today: **265 of 280 single-outlet foreign events unseen (94.6%)**, and even the random 15 contained two macro items on the run's two live axes (*"US vows 'economic D-Day'"*, *"What's Pushing Long-Term Bond Yields Higher?"*). ⚠ **`D334-KR`'s remedy (lower `--singles-nb` to 5) CANNOT work here** — this is the `D331-KR` class again: a KR instrument prescription that does not cross the market | **① Rank the US single-outlet layer by an available English signal instead of `nb` — outlet tier, or title-embedding distance to the day's head clusters — and show the top N by that. ② Until then, have `brief` print `shown / total / UNSCORED` explicitly on the US path so the 94.6% is a number in the report, not a footnote. ③ Every "quiet bucket" claim on this desk carries the unseen count** |
| **`D340`** | ★★★ **`theme-age`'s velocity ratio is a function of TERM WIDTH, and the effect is larger than the signal it is meant to detect.** Three same-event pairs measured in one session: `tariff` ⚪1.14× (base 9,876) vs **`Canada tariff` 🟡9.86×** (69) = **8.7×**; `sanctions` ⚪1.32× (3,600) vs **`economic D-Day` 🟢FRESH** (141); `Warsh` ⚪0.85× (3,628) vs **`Jackson Hole` 🟡14.9×** (296) = **17.5×**. **`D328(a)` prescribed reporting the outlet cluster beside the ratio; that is treatment, not repair** | **Narrow the term until the 90-day base falls inside the usable band and read the ratio there. Band measured today: ~60–2,000 articles** (below ~50 the ratio degenerates — `Iraqi tankers` returned a 3-article base at age 2). **Add the base-width band to the tool's own output line, and keep broad terms in the table as CATEGORY labels that are never read as ratios** |

**Also reproduced this run, no new number needed:** `D327` (COT label inverts, 3rd run — and today the
mislabelled row also carries the board's largest weekly swing) · `D328(b)` (weekend denominators make
every FADING label unreadable — 08-22/23/24 at 35/37/41% of the weekday median) · `D335-KR` (`thread`
top-N hides the day's largest object; **2nd consecutive day, same object**) · `D316` (no trade term in
the `drift_watch` kill-switch set — **and the trade object is now the run's #1**).

---

## §G · What this report may not say, restated at the end so it binds

1. **No price moved.** Every price statistic here is the **2026-08-21** settle, for a third run.
   The two intraday quotes are labelled **LIVE INTRADAY PRINT** and are not in the frame.
2. **No sector was promoted or demoted by this stage.** §E sets wind direction; ROTATION grades.
3. **Consumer Staples' `wflow` sign is unusable** (`WMT` 28.9%). **`EA` is unmeasured, not quiet.**
   **The S&P 500 COT row is unusable** (`D327`).
4. **No "quiet bucket" claim is unqualified**: **265 single-outlet events (94.6% of that layer) and 61
   sub-events went unseen**, and the seen fraction is a random draw.
5. **No `theme-age` ratio on a base above ~2,000 is read as a velocity** in this report — `tariff`,
   `sanctions`, `Warsh`, `Strait of Hormuz`, `bear market` and `refinery` appear as **category labels
   only**.
6. **The credit axis was read and does not support a stress claim** — HY OAS **23.3rd** percentile,
   `NFCI` **7.8th** (loosest of the year). Any risk-off language elsewhere in this run is
   **narrative-only** and must say so.
7. **Health Care is the board's best sector and has no proposition behind it.** Stated as a hole.
8. **`S74` settled `FIRED-C` and its own anti-signal partially fired** (HANDOVER §2b) — the Energy line
   in §E carries that, and it is why ENRG reads two-sided rather than one-way.

---

*Analytical output only. No buy/sell recommendation, no position sizing, no grade change (P4).*

---
---

# §5 · POST-RUN ADDENDUM — appended 2026-08-24 by L1·DRIFT (append-only; nothing above is rewritten)

> `drift_watch.py --report MACRO_REPORT.md`, run at **completion +0.5h**. ⚠ **The spec calls for
> +3–6h; this ran at +0.5h — a declared deviation, 6th consecutive run**, because the scheduled window
> ends after the desk's session. **Cost of the deviation is real and is stated: a burst that begins
> 2–5 hours from now will not be seen by this run.**
> **3 burst candidates (≥3.0×). Two are real and one is a false positive; all three were body-read,
> not merely counted.**

## §5-0 · 🚨🚨 THE ONE THAT MATTERS — a FOURTH Hormuz channel opened after the report closed (`M883`)

**`[ceasefire]` burst 4.0× · `[blockade]` burst 3.0×**, and inside them:

> **"China and Jordan call for Strait of Hormuz to get back to normal after US-Iran conflict"**
> `[scmp` body, published **21:48 HKT 24 Aug**, updated 21:50`]`

**Body, verbatim in substance:** *China and Jordan have called for the **reopening of the Strait of
Hormuz to shipping** and for the **US–Iran ceasefire to be maintained**, in a **joint statement issued
during King Abdullah's visit to Beijing**, alongside criticism of Israel's "dangerous escalatory
actions."* Principals named: **King Abdullah and Xi Jinping.**

★★★ **Why this changes the shape of today's Energy section rather than merely adding to it.**
`S74` settled **`FIRED-C`** this morning with its anti-signal (a) partially fired, because a partial
reopening ran through **bilateral exception-granting** — a *third* channel neither the retired Oman
track nor the IRGC's two named conditions covers (`D338`). **Tonight a FOURTH channel opened:
third-party great-power diplomacy.** Neither named condition appears in it either.
⇒ **The desk now has four distinct mechanisms by which the Strait could reopen and its only remaining
Hormuz bracket for the general fleet is `S8`, which has been undated and unscoreable for 23 runs.**

★ **And the scale is not incidental.** `hellenicshipping` 08-24 body: **China buys ~80% of Iran's
shipped oil**, and COSCO Shipping Energy and China Merchants Energy — together **>100 VLCCs, roughly
half of China's pre-war Middle-East crude imports** — have been keeping their fleets out of Hormuz on
Beijing's guidance. **The party with the largest commercial stake in the closure has now publicly
asked for it to end.**

🚫 **What this ADDENDUM does NOT do:** it does not re-grade Energy, does not move `S119`'s thresholds
(frozen at registration this morning), and does not settle `S74` differently. `S74` fired C on the
observable as written, **before** this statement existed. **The original call stays visible next to
its correction — that asymmetry is the self-backtest's food.**
⇒ **`S119`'s branch B (Energy 3-session excess vs `SPY` ≤ −2.60pp by 08-27) now has one more live
mechanism behind it than it did at registration.** That is the honest statement.

## §5-1 · The second real burst — escalation in the opposite direction, same night

`[blockade]` 3.0× also carried, in **four outlets**:
- *"Iran's currency **rial** hits record low as US plans more sanctions"* `[economictimes` body`]`
- *"No relief for Rial: Iranian currency sinks to record low as US works on new sanctions"* `[toi` body`]`
- *"US Set to Unveil Fresh Iran Sanctions as Rial Hits Record Low"* `[bloomberg` title`]`
- *"Iran's rial currency hits new record low as US prepares to announce more sanctions"* `[google_en/AP` title`]`
- *"Iran calls U.S. sanctions support **'act of war'** as its currency crumbles"*

⇒ **The two bursts point opposite ways on the same axis, in the same hour.** ★ **That is not noise —
it is the run's Energy framing (§E: "oil is now two-sided, not one-way") confirming itself within
hours of being written**, and it is why `S119` was registered both-sided this morning rather than as
a tilt. **A one-way tilt written today would already be half-wrong.**
⚠ **`Strait of Hormuz` itself logged 7 articles as NON-burst activity** — consistent with §B-4's
finding that a term on an 8,059-article base cannot register a burst (`D340`). **The tool caught this
event on `ceasefire`/`blockade`, not on the term the event is actually about.**

## §5-2 · The third burst is a FALSE POSITIVE, and it is logged as one (`M884`)

`[invasion]` fired at **3.6×** on three articles:
*"Roche and Eli Lilly Win FDA Clearance for Alzheimer's Blood Test"* · *"Equinor and Aker BP Make New
North Sea Gas Discovery"* · *"EFL and Scottish league pushing to stop illegal broadcast of matches in
Russia"*.
⇒ **Zero of three concern an invasion.** The term is matching *"invasive"*, *"non-invasive"* and a
Russia-adjacent sports-piracy story. **A 3.6× burst on a kill-switch term with a 0/3 body hit rate is
a precision failure, and it is recorded rather than quietly dropped** — a kill-switch set that cries
wolf is one the desk stops reading.
★ **Amusing but load-bearing detail**: the false positive's top article is an **Eli Lilly** FDA
clearance — **a genuine Health Care catalyst, on the sector this run twice declared to have zero
narrative coverage.** It arrived through the drift monitor's *wrong* term. (BET §I-0 already filed the
self-correction on that claim via `theme-age "drug pricing"` 🟡2.12×.)

## §5-3 · `D316` is REFINED, not merely reproduced (`D345`)

The standing dig says *"no trade/tariff term in the `drift_watch` kill-switch set."* **Today's output
shows the set DOES contain `new tariff` — and it logged exactly ONE article** on the day whose #1
event, by `brief`'s own ranking, was **US–Canada trade-talk collapse at 38 articles / 20 outlets**.
⇒ **The defect is not a missing term; it is a term too narrow to fire.** `new tariff` is a phrase that
the day's actual headlines (*"Canada announces retaliatory tariffs"*, *"US imposes 50 percent tariffs
on $20bn in Canadian goods"*) do not contain.
**Positive-form remedy: widen the trade slot to a term SET — `retaliatory tariff` · `trade talks` ·
`tariff deal` · `trade war` — and have `drift_watch` print each term's article count beside its
multiple, so a term that never fires is visible as a term that never fires rather than as calm.**
⚠ **This is `D340`'s width law appearing in a third instrument today** (after `theme-age` and
`brief`). **Three separate tools, one failure mode: the question's width decides the answer.**

## §5-4 · What this ADDENDUM does NOT claim

- **No price moved.** The report's frame remains `asof = 2026-08-21`; the two intraday quotes it
  carries are labelled **LIVE INTRADAY**, and this ADDENDUM adds none.
- **No sector was re-graded**, no bracket threshold was moved, and `S74`'s `FIRED-C` stands.
- **No claim that the Strait will reopen.** Four channels now exist as *mechanisms*; **zero of them
  has produced a general reopening**, and the hardening evidence (a fatal strike in transit, a
  seizure, strictest-ever sanctions, a record-low rial, an "act of war" statement) is simultaneous.
- ⚠ **The +0.5h window means this ADDENDUM is itself provisional.** Anything breaking 2–5 hours from
  now is outside it, and the next run inherits that gap rather than a clean sheet.

