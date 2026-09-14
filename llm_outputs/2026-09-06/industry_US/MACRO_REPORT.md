# MACRO_REPORT — industry_US · 2026-09-06 (Sun) · Stage 3 / L1·MACRO

> Runtime `--market us`. **All news calls `--scope foreign`, without exception.**
> IDs from `module_evidence next-id` (live scan of `handoff/` + `llm_outputs/` + `REPORT/`), not
> hand-grepped: highest existing at write time **`M1358`** (this run's HANDOVER) · **`P138`** ·
> **`S147`** · **`D533`** (this run's HANDOVER) · `R133` · `C29`. This run takes **`M1359–`** ·
> **`P139`–`P141`** · **`D534–`**.
> **Daily anchor read**: `llm_outputs/2026-09-05/industry_US/MACRO_REPORT.md` in full (§A–§F), plus
> `module_report_tags show` (81 reports · 303 names · 12 sectors).

---

## §0 · 🚨 Instrument state governing every line below (from `preflight/PREFLIGHT.md`)

| gate | verdict | binding effect on this report |
|---|---|---|
| **G0** ✅ | 1/301 NaN on all 14 sessions (`EA` only), **0 partial-NaN names** | flow/OBV citable from the primary file; **`EA` gets no verdict** |
| **G1** 🔴 | sweep news axis **16.72%** (50/299); direct path **6/6** | **no velocity or theme-freshness from `SECTOR_FLOW_US.json`**; every news number below comes from a **direct** `module_news_data` call made ≥60s outside a sweep burst |
| **G2** 🟡 | scale continuous; **`asof` 2026-09-04 == the 09-05 run's `asof`** | **every Δ in this report is dated `09-03 → 09-04` and is NOT presented as today's move** |
| **G3** ✅ | 1 flipper by flag, **2 by issuer** | **no `wflow` verdict on Cons. Disc. or Comm. Services**; `eqflow`/breadth instead, named on the line |
| **G4** 🔴 | 12 / 11 / 10 units at 250/500/750d | no single-number concentration claim (none appears here) |
| **G5** 🔴 | universe **53 days** stale, cover 11/11 | **no cap weight or sector cap share cited as current**; where the two cuts disagree, **`eqflow` is the citable one** |
| **G6** 🔴 | accrual 0.55/day | no IC-backed sizing anywhere (none appears; P4) |
| **G7** 🟡 | 45/47 `--help` clean; chart live 3/3 | no `margin_history` |

★ **The governing fact of this stage, stated once and then obeyed.** The price tape has **no new
session** — Friday 2026-09-04 is the last settled close and **Monday 2026-09-07 is Labor Day**, so
the next one is **Tuesday 09-08**. Every price, flow and positioning number below is Friday's and
reproduces the 09-05 run's to the decimal. **Everything genuinely new in this report is therefore
non-price: news, and the FRED publication clock.** That is not a limitation of the run; it is the
condition the run has to reason inside, and §B is where the new information is.

---

## §A · Indicators — `[FRED]` primaries, and the publication clock is now the story

### A-1 · The split publication reproduces a **7th** time, and it now has a floor

`module_macro_us --days 400 --json`, pulled fresh this run:

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `T10YIE` **2.35** · `RRPONTSYD` 0.675 | `DGS2` **4.34** · `DGS10` **4.77** · `DGS5` **4.52** · `DGS30` **5.25** · **`DFII10` 2.42** · `hy_oas` **2.65** · `ig_oas` **0.81** · `VIXCLS` 14.32 · `SOFR` 3.66 | `WALCL` 09-02 · **`DTWEXBGS` 08-28** · `NFCI` 08-28 (weekly by construction) |

⇒ **`D427`, 7th reproduction.** `P121`·`P114`·`P125` stay blocked. ★ **New this run**: the block has a
**calendar floor** — H.15 does not publish on **Labor Day 2026-09-07**, so these three rows cannot
settle before **09-08**, a fourth consecutive blocked run, **known in advance rather than discovered**
(**`M1356`**, HANDOVER §3c).

### A-2 · The repricing's leg — recomputed from source, and the flip holds

3-session (Δ`breakeven_10y` − Δ`real_10y`), basis points, both `[FRED]`, joint dates only:

| joint date | 08-25 | 08-26 | 08-27 | 08-28 | 08-31 | 09-01 | 09-02 | **09-03** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| spread (bp) | +1.0 | +4.0 | +5.0 | **−11.0** | **−11.0** | −8.0 | −0.0 | ★ **+6.0** |

Trailing 252 of the same spread: mean −0.79 · p05 **−11.0** · p15 **−6.0** · p50 **0.0** · p85 **+5.0**
· p95 +9.0. **+6.0 bp = the 88.1st percentile**, i.e. **above `P125`'s branch-A line of +5.0**.

⚠⚠ **This is a REFERENCE STATE, not a score** (`D242`) — `P125` settles only when **both** series
carry 09-04, and `DFII10` stops at 09-03. **`M1283` reproduced exactly on an independent pull.**
★ **And that exactness is weaker evidence than it looks** (`S2`/`C1`): the underlying series has
published **no new observation**, so this is the same measurement made twice, not a replication.
Stated because "re-measured and confirmed" is precisely the sentence that would launder a null into
evidence on a weekend run. Filed as **`M1359`**.

### A-3 · The three one-year extremes, still pointing opposite ways

| instrument | level | percentile of trailing 252 | asof |
|---|--:|--:|---|
| `DGS30` | **5.25%** | 96th–99th band (nominal complex) | 09-03 |
| **`hy_oas`** | **2.65** | ★ **2.0th** | 09-03 |
| **`^VIX`** | **14.53** | ★ **4.8th** | **09-04** (CBOE) |
| `^TYX − ^FVX` | **69.6 bp** | ★ **2.0th** (flattest in a year) | 09-04 |
| `CL=F` | **$91.48** | **79.0th** | 09-04 |
| `JPY=X` | **156.22** | 34.1st (yen **strengthening**, −1.95% / 5 sessions) | 09-04 |

`M1286` reproduces: **rates price the most stress in a year while credit and volatility price the
least.** `hy_oas`'s 5-session change is **+2 bp** (mid-pack) against a **2.0th-percentile level** —
`D3`, and it is exactly why **`P128` (settles 09-08) is written on the CHANGE, not the level.**

### A-4 · 🚨 A carried number does NOT reproduce, and it is load-bearing

The 09-05 run wrote *"the week WTI printed **$96** with a 7% weekly surge"* and `M1297` recorded
*"5 sessions into 09-04: WTI **+8.08**"*. Measured directly from the settled `CL=F` series this run:

| session | 08-28 | 08-31 | 09-01 | 09-02 | 09-03 | **09-04** |
|---|--:|--:|--:|--:|--:|--:|
| close | 83.40 | 85.76 | 90.22 | 91.01 | 91.30 | **91.48** |
| high | 83.78 | 86.79 | 90.97 | 92.29 | **93.14** | 92.17 |

⇒ **The window's highest print of any kind is `$93.14` (09-03 intraday). No `$96` exists in the
series, on any bar, at any point in the window.** The 5-session change 08-28 → 09-04 is **+9.69%**,
not +8.08%. ★ **The DIRECTION of the carried thesis is confirmed and two of its numbers are not.**
The barrel did surge hard; the level cited was wrong by ~5% and the rate by ~1.6pp.
⇒ **`M1360`** [measured], and **`D534`**: *a price level quoted inside a narrative sentence is
re-pulled from the series before it is carried a second time — a direction that survives does not
certify the number attached to it.* ⚠ This corrects an inherited number; it does **not** retract
`M1297`'s crack figures, which **do** reproduce exactly (A-5).

### A-5 · The crack complex reproduces exactly — and its RATE is at a 1-year extreme nobody has stated

Computed from settled `CL=F` / `RB=F` / `HO=F` (products ×42 to $/bbl), 09-04 close:

| series | level | 252d percentile | 5-session change | **3-session change** | **3-sess percentile** |
|---|--:|--:|--:|--:|--:|
| **distillate crack** | **99.21** | **95.6th** | −0.37 | ★★ **−7.02** | ★★ **6.0th** |
| gasoline crack | 43.53 | 68.7th | **−19.64** | — | — |
| blended 3-2-1 | 62.09 | 86.1th | **−13.22** | — | — |
| **distillate − gasoline** | **55.68** | ★ **98.4th** | **+19.27** | — | — |

`M1297`/`M1311`'s figures reproduce to the decimal. ★★ **What no prior run has stated is the shape
inside the window**: the distillate crack **peaked at 106.23 on 09-01 and has printed three
consecutive lower closes** — 105.64 → 101.63 → **99.21** — and that 3-session decline of **−$7.02/bbl
is the 6.0th percentile of its trailing year.**

⇒ ★★★ **The desk's own regime call, applied to its own OW sector, splits.** §1 of `STANDING_VIEW`
says *"in a commodity-cycle industry the equity tracks the second derivative of price, not the
level."* The distillate crack's **level is the 95.6th percentile and its rate of change is the 6.0th.**
**`M1361`** [measured]. This is the row `P140` (§D) is written on, and it is a `L1`/`D3` split, not a
new fact — the same numbers the 09-05 run held, read on the derivative it says to read.
⚠ `M1311`'s "neither series has printed two consecutive declines" was about the **quarterly** rate and
is **not** contradicted by a daily series; two different objects, stated so they are not conflated.

### A-6 · Monthly series, lag stated rather than hidden
`CPIAUCSL` **332.813** and `CPILFESL` **336.789** carry **2026-07-01**; `UNRATE` **4.1%** carries
**2026-08-01**; `M2SL` carries 2026-07-01. **The August CPI is unpublished — it prints 2026-09-11.**
No inflation claim below is anchored on a `[FRED]` CPI observation.

---

## §B · News — `--scope foreign` on every call. Coverage is stated before anything is concluded.

### B-0 · Coverage, stated first (EXIT CHECK: the tail is not the coverage claim)

| day | articles | clusters | 2-src+ events | single-source clusters | shown of those | tail | nonmarket |
|---|--:|--:|--:|--:|--:|--:|--:|
| **2026-09-05** (Sat) | **1,665** | **621** | **281** (head 21 + body 260) | **340** | **15** (random) | **0** | **0** |
| **2026-09-06** (Sun, partial to 21:43 KST) | **557** | **280** | **104** (head 7 + body 97) | **176** | **15** (random) | **0** | **0** |

⇒ **09-05 visibility = 281 + 15 = 296 of 621 clusters = 47.7%. 325 clusters (52.3%) exist only as a
count.** `subevents_recovered` **66**. `excluded_not_news` returned **`{}`** — no correction was
available, so the denominator above is the raw one and is labelled as such.

🚨 **`D474`/`D506` reproduce, 13th measurement.** All 340 single-source clusters return `nb: null`
(`scored 0 / scorable 0 / unscored 340`) because the classifier is Korean-only, so the tier is a
**random 15-of-340**, not a recovery; and `excluded_nonmarket` returns **count 0 by construction**,
not by observation. **Two of the three mandated recovery tiers are structurally unavailable on this
runtime.** Every "quiet"/"nothing in bucket X" claim below therefore carries this number, and there
is exactly one such claim in this report (B-4) — it is made about a *measured* denominator, not about
an absence.

### B-1 · ★★★ The run's central event, and it is entirely outside the price frame

**Head of 2026-09-05, by outlet count:**

| outlets | articles | event |
|--:|--:|---|
| **16** | 21 | ★★★ **"U.S. hits three Iranian oil tankers after missiles target American warships"** |
| 14 | 25 | "Russia's Putin meets US envoys to discuss Trump proposal to end Ukraine war" |
| **13** | 15 | ★★ **"Trump Oil Deal Blindsides US Energy Companies"** |
| 7 | 15 | "History Says That Bitcoin Is an Unbelievable Bargain Right Now" |
| 7 | 11 | "Anthropic IPO launch shifts toward mid-October, sources say" |
| 7 | 10 | "OpenAI acknowledges 'wiki incident'…" |
| 6 | 9 | "Fed Chair Kevin Warsh Just Shifted the Central Bank's Entire Focus on Inflation in One Sentence" |
| 6 | 7 | "US peace envoys Witkoff and Kushner to visit Kyiv and Moscow…" |
| 5 | 8 | "Nvidia-backed AI company reveals staggering $103 billion number" |
| **5** | 7 | ★ **"Spot Memory Prices Are Running 4 Times Contract Prices. That Is Not What a Cycle Peak Looks Like."** |
| 5 | 6 | "The woman at the center of Japan's currency fight" |

**Head of 2026-09-06 (partial):** `Indonesia/Krakatau` 9 · `German state election` 7 · ★ **`"OPEC+ set
to keep oil output policy unchanged on Sept 6"` 7** · `China population` 6 · ★ **`"Iran Says It
Targeted Oil Tankers in Response to US Strikes"` 5**.

**Body-read of the escalation** (`fts search "oil tankers" --days 2 --scope foreign`, 46 matches):

- 09-05 — US strikes **three Iranian oil tankers**, framed by CENTCOM as targeting the financing of
  *"regional proxies"* [aljazeera, bbc, cnbc, ft, bloomberg, axios, scmp, seekingalpha, dw, politico,
  euronews, google_en/AP, fortune, wsj, forbes, guardian = 16 outlets]. One strike is reported **near
  Kharg Island** [euronews] — Iran's principal export terminal.
- 09-06 — **Iran targets a US naval drone attempting to enter the Strait of Hormuz** [euronews, scmp];
  IRGC **claims new attacks on US warships over a naval blockade** [aljazeera]; Iran warns of a
  *"more painful"* response [cnbc].
- 09-04, the workaround leg — **"Iraq Is in Process of Seeking Oil Tankers for Hormuz Strait Runs"**
  [bloomberg].

★★★ **`M1362`** [measured] — **a two-way military escalation around oil export infrastructure
occurred on 2026-09-05 and 09-06, after the last settled close and before the next one.** The desk's
entire price, flow and positioning apparatus is frozen at Friday; its news apparatus runs through
Sunday. **The asymmetry is not a defect this run can fix; it is the condition that makes this run's
propositions forward-looking rather than descriptive.** The first settled test is **2026-09-08**.

### B-2 · ⚠ The other side, read BEFORE any conclusion (`C2`, and the direct lesson of `M1327`)

The 09-05 run's DRIFT probe caught that run reading only one side of the Russian-refinery story. The
same corpus, same days, carries a **de-escalation and supply-expansion side** and it is larger, not
smaller, than the escalation side:

| date | outlets | item |
|---|--:|---|
| 09-05 | 2 | ★★ **"Bessent predicts $40 crude oil and lower yields after Iran war"** — the **US Treasury Secretary** forecasting the reversal of **both** of this desk's live macro legs [economictimes, seekingalpha] |
| 09-06 | — | "US Iran Fight Shifts to Economic Endurance" [bloomberg] — attrition, not shock |
| 09-06 | 7 | ★ **"OPEC+ set to keep oil output policy unchanged on Sept 6"** — a **scheduled** meeting with **no change** |
| 09-05 | 3 | "Trump calls Iran conflict **'small potatoes,'** as he plays down war" |
| 09-04 | — | "European Union joins U.S.-led 'Operation Economic Outcast'" [cnbc] — the sanctions axis widening |
| 09-06 | — | "US, Iran engaged in tanker war: Where is the months-long conflict headed?" [aljazeera] |

⚠⚠ **`P126`'s VOID clause names "an OPEC+ emergency production decision."** The 09-06 meeting is a
**scheduled** meeting that kept policy **unchanged**. ⇒ **It is NOT a voider**, and that is recorded
**now, at D-3, rather than argued at scoring** (`D450`). Filed as **`M1363`**.

### B-3 · ★★★ The blind spot this stage exists to find: **Venezuela**

**`Venezuela` is not in this desk's term table, is not in any carried proposition, is not in the
transmission matrix, and is not in `SCENARIOS_US.md`.** It is also the largest and fastest-moving
supply story on this desk's single OW sector.

| measure | value |
|---|---|
| `fts` foreign hits, 7d (phrase) | **487** — would rank **9th of 18** on the term table, above `refinery` (275), `diesel` (280), `rare earth` (176), `AI capex` (102), `gas turbine` (84), `credit spread` (65) |
| 14d | 670 ⇒ **the last 7 days carry 72.7%** of the fortnight |
| 3d | 207 ⇒ **the last 3 days carry 42.5%** of the week |
| **`theme-age`** | 🟡 **ACCELERATING · 2.95× · base 1,562 · age ≥90** |

★★★ **2.95× is the ONLY theme measured this run that clears the 2× acceleration bar, and it is
1.6× the next-highest** (`payrolls` 1.89×). It is not 🟢FRESH only because the *word* Venezuela is
old; the **deal** is 8 days old.

**Body-confirmed chain, multi-outlet, dated:**

| date | outlets/source | fact |
|---|---|---|
| 08-29/30 | axios, semafor, toi | Trump hails *"biggest oil deal in world history"*; **US strikes a deal for 65 billion barrels of Venezuelan reserves** |
| 08-30 | aljazeera | **Trump says the US will refill the SPR using Venezuelan oil** |
| 08-30/31 | euronews, hellenicshipping | Venezuela says it retains *"sovereignty"* over its reserves despite the deal |
| 08-31 | yahoo_finance | **Trump says `XOM` will enter Venezuela** |
| 08-31 | oilprice, yahoo | **`CVX`, `HAL`, `ONGC`, `GEV` near final deals**; *"`SLB`'s Venezuela bet: massive opportunity or risky gamble?"* |
| 09-01 | aljazeera, scmp | White House details the deal; **China demands a rights guarantee** as a US firm secures a 100-year concession |
| 09-02 | scmp, france24, economictimes, aljazeera | ★ **`CVX` $7bn plan to DOUBLE Venezuelan output in five years**; US energy secretary *"vows output will double"* |
| 09-03 | aljazeera, euronews | US and Eni expand projects; *"US energy firms significantly expand operations"* |
| **09-04/09-05** | **bloomberg ×2, japantimes** | ★★ **the turn: "Trump's Big Venezuela Deal Leaves US Oil Industry BLINDSIDED" — 13 outlets on 09-05** |

⚠⚠ **The body of the "blindsided" leg is UNREADABLE and this report does not guess at it.**
`search --field any` returns `[no body]` for both Bloomberg items and `[error]` for the Japan Times
one — Bloomberg is on the scraper's blocked list and this is a **`D10`-class** gap. ⇒ **The desk has
the SUBJECT from three outlets across two days and not the MECHANISM.** Recorded as an explicit hole,
because the difference between *"the deal is bad for US producers"* and *"the deal was announced
without consulting them"* is the difference between a thesis and a headline. **`D535`**: *the
third-largest event of the day on the desk's own OW sector was title-only across every outlet that
carried it, and no fallback venue was tried.*

**Why this matters to the standing view, stated as a question and not as an answer:**
Venezuelan crude is **heavy sour**, which is the design feed of the US Gulf Coast refining complex.
A structural increase in heavy-sour supply is **bullish the refining margin** (wider heavy–light
differentials) and **bearish the barrel**. Simultaneously, the named upstream/service beneficiaries
are `XOM`, `CVX`, `SLB`, `HAL`, `GEV`. ⇒ **The Venezuela axis and the Iran axis push the same sector
in opposite directions on the barrel and possibly the same direction on the crack.** No existing row
measures this. **`P139`** (§D) does.

★ **And it lands on the sector's own internal split, which is measurable today:**

| ticker | node | flow | OBV | rs20 | rs60 | Venezuela-named? |
|---|---|--:|--:|--:|--:|:--:|
| **`SLB`** | Equipment & Services | ★ **0.883** (sector #1) | +0.439 매집 | +14.2 | **−2.6** | ✅ |
| `WMB` | Storage & Transport | 0.769 | +0.151 | +5.7 | −3.6 | — |
| `PSX` | Refining | 0.750 | +0.434 | +25.5 | +34.2 | (feed side) |
| `VLO` | Refining | 0.700 | +0.482 | +24.7 | +37.5 | (feed side) |
| `MPC` | Refining | 0.694 | **+0.621** | **+30.8** | **+41.5** | (feed side) |
| **`CVX`** | Integrated | 0.661 | +0.371 매집 | +12.2 | +3.7 | ✅ **$7bn / double output** |
| `COP`·`EOG`·`DVN`·`OXY` | E&P | 0.64→0.55 | +0.13→+0.25 | +8 → +15 | −3 → +6 | — |
| **`XOM`** | Integrated | 🚨 **0.027 (sector last)** | **−0.071 중립** | +4.6 | −0.3 | ✅ **named by Trump** |

★★ **The two Venezuela-named names the desk can measure sit at ranks 1 and 7 of 16; the third sits
DEAD LAST.** `SLB`'s +14.2 rs20 against a **negative** rs60 is the signature of a *new* catalyst, not
a continuing trend. ⚠ `SLB` and `BKR` (0.308, rank 14) are the only two services names and are 0.575
flow points apart — **"services" is not a node on n=2 with that dispersion** (`W5`, and `D530`'s
residual-correlation test has not been run on it).

### B-4 · Term sweep — and the honest finding is that **this window carries no rotation signal**

`fts search --days 7 --scope foreign --count`, **both conventions printed** (`D473`). Exact
invocations recorded: phrase = `fts search "<term>" --days 7 --scope foreign --count`; argv =
`fts search <term1> <term2> --days 7 --scope foreign --count`.

**⚠ The window is NOT like-for-like with the 09-05 run's and this is measured, not assumed.**
Per-day foreign article denominators (`brief`, one call per day):

| day | 08-30 | 08-31 | 09-01 | 09-02 | 09-03 | 09-04 | 09-05 | **09-06** |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| articles | **1,711** | 4,958 | 5,465 | 5,812 | 5,376 | 4,704 | 1,665 | ★ **557** |

09-05 run's window (08-30→09-05) = **29,691** articles. This run's window (08-31→09-06) = **28,537**.
⇒ **The window swapped a full 1,711-article Sunday for a 557-article PARTIAL Sunday: −1,154 articles
= −3.89%.**

| term | phrase now | argv now | 09-05 phrase | raw Δ | ★ **share Δ** (denominator-corrected) |
|---|--:|--:|--:|--:|--:|
| `bond selloff` | 134 | 264 | 135 | −0.7% | **+3.3%** |
| `payrolls` | 599 | 599 | 613 | −2.3% | +1.7% |
| `Strait of Hormuz` | 970 | 980 | 997 | −2.7% | +1.2% |
| `AI capex` | 102 | 392 | 105 | −2.9% | +1.1% |
| `diesel` | 280 | 280 | 293 | −4.4% | −0.6% |
| `Treasury yield` | 743 | 1,172 | 778 | −4.5% | −0.6% |
| `gas turbine` | 84 | 112 | 88 | −4.5% | −0.7% |
| `refinery` | 275 | 275 | 290 | −5.2% | −1.3% |
| `yen` | 812 | 812 | 857 | −5.3% | −1.4% |
| `data center` | 2,378 | 3,066 | 2,519 | −5.6% | −1.8% |
| `rate hike` | 1,291 | 1,628 | 1,380 | −6.4% | −2.7% |
| `crude oil` | 790 | 1,273 | 847 | −6.7% | −3.0% |
| `tariff` | 1,715 | 1,715 | 1,846 | −7.1% | −3.3% |
| `inflation` | 2,887 | 2,887 | 3,149 | −8.3% | −4.6% |
| `Federal Reserve` | 1,324 | 1,496 | 1,451 | −8.8% | −5.1% |
| `rare earth` | 176 | 236 | 194 | −9.3% | −5.6% |
| `credit spread` | 65 | 326 | 76 | −14.5% | **−11.0%** |
| 🆕 **`Venezuela`** | ★ **487** | 487 | *(not carried)* | — | **new term, added to the table** |

★★★ **`M1364`** [measured] — **17 of 17 carried terms fell on raw counts (median −5.3%) against a
measured window denominator of −3.89%. Share-normalized the entire board collapses to ±5% flat, with
a median of −1.4% and 13 of 17 inside ±5%.** ⇒ **This sweep contains no rotation signal. The raw
table is a denominator artifact and would have read as "attention drained from everything," which is
not a thing that happens.**

⚠ **This does NOT retract the 09-05 run's `M1291`** ("attention CONCENTRATED"). That table had
`payrolls` **+81.4%** against a −5% to −27% field — a **~100pp dispersion** that no ±4% denominator
can manufacture. **Today's table has no dispersion at all**, and that difference is the whole point:
`M1291` had a signal, this one has a shorter window. Stated so the two are not read as a trend.
⚠ `C5`/`D473`: the conventions still disagree by up to **5.0×** (`credit spread` 65 vs 326). Every Δ
above is the **phrase** read, matching the convention the 09-05 table's numbers match.

### B-5 · Novelty (`theme-age`, 90d, `--scope foreign`) — a 13th zero, and now **doubly** arithmetic

| theme | verdict | age | 7d avg | **accel** | base |
|---|---|--:|--:|--:|--:|
| ★ **`Venezuela`** | 🟡 **ACCELERATING** | ≥90 | 63.9 | ★★ **2.95×** | 1,562 |
| `payrolls` | ⚪ECHO | ≥90 | 82.7 | **1.89×** | 2,600 |
| `rate hike` | ⚪ECHO | ≥90 | 178.9 | **1.74×** | 7,570 |
| `heavy crude` | ⚪ECHO | ≥90 | 4.7 | 1.55× | 140 |
| `gas turbine` | ⚪ECHO | ≥90 | 11.0 | 1.39× | 498 |
| `OPEC` | ⚪ECHO | ≥90 | 25.3 | 1.27× | 1,322 |
| `oil tanker` | ⚪ECHO | ≥90 | 16.0 | 1.20× | 1,168 |
| `Iran` | ⚪ECHO | ≥90 | 331.7 | 1.09× | 21,747 |
| `data center` | ⚪ECHO | ≥90 | 311.9 | 0.99× | 19,799 |
| `Strait of Hormuz` | ⚪ECHO | ≥90 | 133.1 | 0.94× | 9,118 |
| `credit spread` | ⚪ECHO | ≥90 | 7.9 | **0.74×** | 753 |
| **`refining margin`** | ⚪ECHO | **80** | 4.0 | ★ **0.65×** | 315 |
| **`distillate`** | ⚪ECHO | ≥90 | 17.0 | ★ **0.64×** | 1,346 |

★ **`M1365`** — **zero 🟢FRESH for a 13th consecutive foreign-feed measurement, and this run can say
the zero is arithmetic on BOTH legs, not one.** The gate needs age ≤14d **and** accel ≥2×. The
youngest theme measured is **80 days** (`refining margin`), *and* only **one of thirteen** clears 2×.
The 09-05 run could only rule out the age leg; **both legs are now independently measured to fail**,
so the zero is a property of the gate's definition against a mature-vocabulary feed, not an outage
(the pipe was falsified live, 6/6, before any of these calls).

★★ **The divergence that matters is inside the oil complex**: the **shipping/supply** legs are
accelerating (`oil tanker` 1.20× · `OPEC` 1.27× · `heavy crude` 1.55× · `Venezuela` 2.95×) while the
**label** is flat (`Strait of Hormuz` 0.94×) and the **refined-product margin** legs are decelerating
for a **4th consecutive run** (`distillate` 0.64× · `refining margin` 0.65×). ⇒ **The escalation is
being narrated as a supply-and-shipping event, not as a refining-margin event — and the refining
margin is the node this book holds.** **`M1366`**.

### B-6 · Trajectories (`thread --days 7`) — and the weekend inflates every FADING tag

**Per-day denominator, printed first as the stage's own spec requires:**
`08-31 755 · 09-01 858 · 09-02 944 · 09-03 877 · 09-04 727 · 09-05 281 · 09-06 104` events.
**The window ends on two low-volume days, one of them truncated.** `D508`/`R129` bind directly.

| thread | tag | curve | read **after** removing the weekend legs |
|---|---|---|---|
| *"U.S. strikes on Iran send oil prices higher"* | 🔴FADING | 22→22→19→14→21→**13→7** | **weekday legs 22→22→19→14→21 = flat-to-oscillating, NOT fading** |
| *"US launches new strikes against Iran as war escalates"* | 🔴FADING | 12→16→9→5→10→**16→5** | **weekday legs end 10→16, RISING into Friday** |
| *"Iraq projects → Two More Oil Tankers Attacked → …"* Hormuz chain | 🟡REIGNITED | 2→10→7→3→**4** | 4 outlets on a **104-event Sunday** = a high per-day share |
| *"Germany says Russia preparing 'hybrid' attacks"* | 🔴FADING | 13→18→20→11→14→14→4 | weekday legs flat at 14 |
| *"Nvidia to Acquire Hugging Face for $12.9bn"* | ⚫ENDED | 4→28→9, peak 28 | `R129`: the ENDED tag is a **curve shape**, not a death. `S130` settles **09-10** |

⇒ **`M1367`** — **every 🔴FADING tag in this window is weekend-inflated, and the two Iran threads
read flat-to-RISING once the two low-volume days are removed.** The 09-05 run made exactly this error
in its first pass and caught it (`D508`); this run applies the correction **before** writing, which
is what a registered defect is for.

### B-7 · Blind-spot / burst pass

`blindspot --scope foreign` ran over the **full corpus (324,584 articles)**, not a 7-day window, so
its top-30 is a long-run frequency table and not an emergent vocabulary — **`D536`**: *the blindspot
pass has no window argument on this runtime, so it cannot answer "what is new today."* Useful output:
`SpaceX` **4,958** and `Dollar` **4,570** rank in the top-10 of tokens absent from the fixed set;
`SpaceX`'s share unlock is **09-09** (`M1303`, carried).

`burst --scope foreign` on **today's 557-article partial day** — ⚠ every z below is computed against
a 30-day baseline that is mostly full weekdays, so **a 3-article word scores a large z by
construction**. Reported as a pattern, not as magnitudes:
**`HYPERSCALERS`** z 17.9 (6 art, 1.077% vs 0.050% usual) · **`TURBINES`** (new word, 3 art, 100%
market) · **`FOUNDRY`** z 8.1 · **`ORACLE`** z 7.6 · `DIMON`/`JAMIE` (JPM near $1tn) · `BURRY`
(Palantir accounting). ⇒ the coherent cluster is **AI-power hardware** — *"Elon Musk Says His New
Foundry Can Get **Gas Turbines** Online 18 Months Faster"* [3 outlets] against *"6 Hyperscalers…
$1.3 Trillion Capex in 2027"* [4 outlets]. **`P127`'s window closes 09-10 and this is inside it.**

⚠ **Unregistered dated catalyst surfaced by the 09-06 brief**: *"What to Expect in Markets This Week:
Fresh Inflation Data; Apple's Fall Launch Event and **Oracle Earnings**"* [2 outlets]. **`ORCL` is not
in any carried row and is not on `catalyst_calendar`.** Handed to PREMORTEM.

---

## §C · Positioning — `[COT report date 2026-09-01, Tue-close, released Fri 09-04]` + `[FINRA 09-04]`

⚠ **No new COT release exists.** The CFTC publishes Friday for Tuesday data; the 09-04 release
covering 09-01 is the same one the 09-05 run read. **Next release: Friday 2026-09-11.**

| instrument | net spec | wk Δ | 1y %ile | read |
|---|--:|--:|--:|---|
| **Copper** | +80,869 | −4,397 | ★ **100th** | 🟢 crowded-long — **6th consecutive run at the 100th percentile** (`C24`) |
| **Nasdaq-100** | +27,077 | **+15,951** | **82nd** | 🟢 crowded-long |
| **UST 10Y** | −909,275 | **−70,300** | ★ **9th** | 🔴 crowded-short — the largest weekly change on the board |
| **Nat Gas** | −208,911 | −10,979 | ★ **0th** | 🔴 crowded-short |
| Russell 2000 | −14,741 | +1,377 | 17th | 🔴 crowded-short |
| WTI Crude | +35,574 | **+4,475** | 70th | 🟡 neutral — ⚠ **NOT crowded**, on the week the barrel rose 9.7% |
| S&P 500 | −75,941 | −7,947 | 63rd | 🟡 |
| USD Index | +17,025 | −1,657 | 70th | 🟡 |
| Gold | +228,124 | −15,210 | 50th | 🟡 |
| UST 2Y | −882,518 | −21,222 | 71st | 🟡 |
| Silver | +26,739 | +1,478 | 44th | 🟡 |

★ **`M1368`** — **speculators are only 70th-percentile long WTI after a +9.69% five-session move and
a two-way military escalation.** Against a copper book at the **100th** and a 10Y short at the
**9th**, the barrel is the least crowded of the three extremes on the board. **Ammunition, not a
direction** (`D6`) — and the COT data is 3 days stale *and* pre-dates the tanker strikes entirely.

`[FINRA 09-04]` short-volume ratio vs each name's own 20-day base:

| ticker | short% | base20 | z | 5v5 trend | read |
|---|--:|--:|--:|--:|---|
| **`SMH`** | 71.6% | 54.5% | ★ **+2.99** | +2.7▲ | 🔴 on a session it printed **+2.61%** |
| **`ETN`** | 72.6% | 52.5% | ★ **+2.16** | −4.6▼ | 🔴 on a session it printed **+3.46%** |
| `VLO` | 62.5% | 57.8% | +0.52 | +4.0▲ | 🟡 |
| `STX` | 44.0% | 40.0% | +0.45 | −1.4▼ | 🟡 |
| `MPC` | 62.3% | 58.8% | +0.43 | ★ **+8.9▲** | 🟡 level, **but the largest 5v5 build on the sheet** |
| `PSX` | 51.9% | 54.3% | −0.36 | +0.8▲ | 🟡 |
| `SPY` | 58.0% | 60.7% | −0.38 | −4.9▼ | 🟡 |
| `XLE` | 53.7% | 57.9% | −0.49 | +0.9▲ | 🟡 |
| `NVDA` | 35.3% | 37.5% | −0.51 | −1.1▼ | 🟡 |

`M1287` reproduces: the two 🔴 extremes are **names that rose hard**, which `[FINRA]` cannot
separate from market-maker hedging (`D6`) — that ambiguity is what **`P137`** (settles 09-11) is for.
★ New: **`MPC` carries the sheet's largest 5-vs-5 short build (+8.9) at an unremarkable z**, i.e. the
building is recent and has not yet moved the level. On the book's largest-conviction refiner, that is
worth carrying into DEEP.

---

## §D · Propositions registered this run — `P139` · `P140` · `P141`

### `P139` — ★★★ The blind spot: does the VENEZUELA supply deal pay the upstream/service leg, or the REFINING leg?

**Claim.** The desk's single OW sector has a second, larger, faster-accelerating supply story than the
one it is carrying, and it is **not in the term table, not in any proposition, and not in the matrix**
(B-3). `Venezuela` runs **487 hits in 7 days at `theme-age` 2.95×** — the only theme this run
measured that clears the 2× bar and **1.6× the next-highest**. The deal is body-confirmed across
~15 outlets over 8 days: **65bn barrels opened, `CVX` $7bn to double output in five years, `XOM`
named by Trump, `SLB`/`HAL`/`GEV` near deals, SPR refill from Venezuelan crude** — and then, on
09-04/09-05, a **13-outlet turn** saying the US industry was **"blindsided"**, whose body this desk
cannot read (`D535`).

Venezuelan crude is **heavy sour**, the design feed of the US Gulf Coast complex. ⇒ **the same event
is bearish the barrel and plausibly bullish the crack** — the two halves of an Energy OW that this
desk has already re-specified as a *chain-position* bet. **Nothing on the board measures the split.**

| | |
|---|---|
| **Frozen observable** | `EW{XOM, CVX, SLB}` **minus** `EW{MPC, PSX, VLO}`, **5-session** returns, settled closes, `auto_adjust=False`, window **2026-09-04 close → 2026-09-14 close** (the 5 settled sessions 09-08, 09-09, 09-10, 09-11, 09-14 — Labor Day 09-07 excluded by construction) |
| **Branch A (the Venezuela leg is paid upstream)** | **≥ +2.719** (trailing-252 **p85**) — the deal re-rates integrateds/services and the OW's centre of gravity moves **upstream**, reversing `M1245`/`M1246`'s chain-position finding |
| **Branch B (it is a REFINER story, or nothing)** | **≤ −4.689** (trailing-252 **p15**) — heavy-sour feed, or the market ignores it; the chain-position bet replicates through a second supply shock |
| **Branch C** | between = the disclosed favourite |
| **`D93` executed BEFORE freezing** | trailing 252 of the same 5-session spread: p05 **−7.566** · **p15 −4.689** · p50 **−0.399** · **p85 +2.719** · p95 +4.860 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−3.260 = the 22.6th percentile** (09-04 settled) — **inside C, leaning B**. ⚠ **Disclosed**: B is the near branch and A is the far one; an A print is the informative one |
| **Anti-signal (VOID)** | a **reversal or suspension of the US–Venezuela arrangement**, a **US or Venezuelan sanctions action** that re-closes it, or **announced M&A involving any of the six names**, inside 09-08 → 09-14. ⚠ **Base rate checked**: the 7d `Venezuela` window returns 487 hits with **no** reversal item — the closest is Caracas asserting "sovereignty" [euronews 08-30], which is **rhetorical, not a suspension**, and therefore explicitly **not** a voider. ⚠ **The Iran escalation is NOT an anti-signal** — it is the competing driver the row is designed to sit against |
| **Track KPI** | if **A**, `heavy crude` theme-age should leave ⚪ECHO (currently **1.55× on 140**); if **B**, the distillate−gasoline spread should hold above the 90th percentile (currently 98.4th) |
| **Dated catalyst** | none dated — this is a **rolling** structural story, which is stated rather than invented. The two dated binaries inside the window (PPI 09-10, CPI 09-11) affect **both** legs and are not the driver |
| **Thread** | ⚠ **no matching thread** — stated explicitly. `Venezuela` does not appear as a multi-day thread in `thread --days 7` despite 487 hits, because the cluster titles differ every day. **A 2.95×-accelerating theme with no thread is exactly where an unpriced move can start**, and the row is registered on the *term and theme-age* instruments, not on a story |
| **Non-redundancy (`D343`)** | `P126` (09-09) is `EW{XOM,CVX,EOG,FANG}` − `EW{MPC,VLO,PSX}` — **barrel-vs-chain on E&P**, and it excludes `SLB`, the sector's #1 flow and a named beneficiary, while including two E&P names with no Venezuela exposure. `S147` (09-14) is refiners vs `SPY` — one leg only. `P136` (09-14) is the 16-name sector vs its narrative. **None is an upstream/service-vs-refining pair spread, and `P139` can disagree with all three — if it does, the disagreement is the finding** (`S14-ANNEX` precedent) |
| **Owner** | `industry_US` |

### `P140` — ★★★ The crack's LEVEL is the 95.6th percentile and its RATE is the 6.0th. Which does the desk's own regime call say to read?

**Claim.** `STANDING_VIEW` §1 asserts that *"in a commodity-cycle industry the equity tracks the
second derivative of price, not the level."* Applied to this desk's own OW sector, that assertion now
**splits its own evidence**: the distillate crack sits at **99.21 = the 95.6th percentile** while its
**3-session change is −$7.02/bbl = the 6.0th percentile** — it peaked at **106.23 on 09-01** and has
printed **three consecutive lower closes** (A-5). ⚠ The carried thesis has been written on the level
and the percentile every run.

| | |
|---|---|
| **Frozen observable** | The **distillate crack** = `HO=F` × 42 − `CL=F`, both settled closes, **5-session change in $/bbl**, at the **2026-09-11** settled close |
| **Branch A (the rate is the signal — compression continues)** | **≤ −4.209** (trailing-252 **p15**) — the margin story is rolling over while its level is still extreme, and the refiner sub-node's `L2` peak-margin trap (`M1313`) is loaded |
| **Branch B (the 3-session drop was an air pocket — the level reasserts)** | **≥ +8.699** (trailing-252 **p85**) — the escalation transmits to product and the level-based carry is vindicated |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the 5-session distillate-crack change: p05 **−8.942** · **p15 −4.209** · p50 **+0.248** · **p85 +8.699** · p95 +12.767 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−0.373 = the 45.6th percentile** (09-04) — **mid-pack, and deliberately so.** The extreme is in the *3-session* window (6.0th pctile); the row is written on the **5-session** change precisely so that its own registration state is **not** already at a branch (`B4`). **Both branches are genuinely reachable** |
| **Anti-signal (VOID)** | a **US SPR release or refill announcement executing inside the window**, an **NYMEX/ICE contract-specification or roll change** on `HO`/`CL`, or a **hurricane-driven Gulf Coast refinery outage ≥500kbd**, inside 09-08 → 09-11. ⚠ Base rate checked: the SPR item is live in the corpus (*"Trump says US will refill its petroleum reserves using Venezuelan oil"*, aljazeera 08-30) as a **stated intention with no date** — an actual dated execution inside the window **would** void |
| **Track KPI** | if **A**, `MPC`/`PSX`/`VLO`'s `rs20` (currently +30.8 / +25.5 / +24.7) should compress; if **B**, the distillate−gasoline spread should stay above the 95th percentile |
| **Dated catalyst** | weekly EIA product-stock print (Wed **09-09**) · US August CPI **09-11**, whose energy component is the same physical object |
| **Thread** | 🔴 the refined-product narrative instruments are **decelerating for a 4th consecutive run** — `distillate` **0.64×**, `refining margin` **0.65×** (base 315, age 80) — against a level at the 95.6th percentile. **The narrative and the physical print have disagreed for four runs and the RATE has now joined the narrative's side.** That is the change this row exists to measure |
| **Non-redundancy (`D343`)** | `S147`/`P136` measure the **equities**; `P126`/`P139` measure **relative** equity legs. **`P140` is the only row on the driver itself**, and the desk's whole `L1` lens says the driver's second derivative is the object |
| **Owner** | `industry_US` |

### `P141` — ★★ An INSTRUMENT proposition, registered here so it is not a `D504` orphan

**Claim.** *A 7-day term sweep whose window ends on a partial collection day cannot be differenced
against a prior run's sweep without denominator normalization, and the un-normalized difference will
read as a uniform decline across every term.*

**Measured origin** (B-4): 17 of 17 carried terms fell, median **−5.3%**, against a measured window
denominator change of **−3.89%**; share-normalized, the median move is **−1.4%** and 13 of 17 sit
inside ±5%. **Falsifier**: re-run the identical 17 terms on a window ending on a **full weekday**
(next opportunity **2026-09-08**) and compare share-normalized deltas against raw deltas. If the raw
and share readings agree there, the artifact is specific to truncated windows; if they disagree
again, the sweep needs a permanent denominator column.

⚠ **This row has an anti-signal and a horizon but NO PRICE OBSERVABLE, so it is not a bracket and it
is not written into `SCENARIOS.md`'s index.** It is recorded here and named in the writeback,
following the 09-06 KR run's precedent for `M-132`/`M-133` — **stating the absence is what keeps
`D504` from reproducing.**

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each. **This is ROTATION's input.**

> **Wind direction only, not a ranking.** `exc1`/`exc5`/`exc20` are **equal-weight `us_top300`
> constituent baskets, excess vs `SPY`**, recomputed this run from this run's own price frame on the
> **2026-09-04 SETTLED close**. `SPY` itself: **−0.385% (1) · +0.109% (5) · −0.397% (20)**.
> ★ **They reproduce the 09-05 run's table to the decimal on a second, independent computation
> (price frame vs. flow file) — which is `G2`'s null-novelty finding confirmed on a different
> instrument, not a new measurement** (`M1353`).
> 🚫 **`wflow` is barred as a verdict basis for Consumer Discretionary and Communication Services**
> (G3); every weighted number rests on a **53-day-old cap vector** (G5) — where the cuts disagree,
> **`eqflow` is the citable one and is named on the line.**
> **Every Δflow below is the `09-03 → 09-04` change** (G2). None is today's move.

| # | GICS sector | Wind | Driving prop. | eqflow / wflow | Δflow (09-03→09-04) | exc1 | exc5 mean / med | neg5/n | exc20 mean / med | One line |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | **Energy** | **OW** | ★★ **`P139`** · **`P140`** · `P136`·`P126` | **+0.562** / +0.440 | **+0.054** | −0.27 | **+1.89 / +1.44** | ★ **1/16** | ★ **+12.29 / +11.52** | ★★★ **The only sector positive on flow level, flow Δ, breadth and both price windows**, median ≈ mean ⇒ not a two-name artifact (`W5`). ⚠⚠ **And it is now the sector carrying THREE live, opposed supply drivers at once**: a two-way military escalation around export infrastructure (09-05/06, **outside the price frame**), a 2.95×-accelerating Venezuela supply deal **the desk was not carrying** (`P139`), and a crack whose **level is the 95.6th percentile while its 3-session rate is the 6.0th** (`P140`). Its narrative instruments decelerate for a 4th run (`distillate` 0.64×, `refining margin` 0.65×). **The OW's LEVEL evidence is unanimous and its DRIVER evidence has fractured.** ROTATION owns the verdict, not this stage |
| 2 | **Health Care** | **OW−** | `S133` (09-14) | **+0.190** / +0.098 | −0.043 | −0.44 | **+0.63 / +0.98** | 12/32 | **+3.63 / +3.74** | Positive on **both** windows with **median ≥ mean** on each — the board's second-broadest. Flow Δ mildly negative. The sector's `top1` (`LLY`, 19.4%) is **🔴분산 −0.462 and holds it DOWN** (`wflow` +0.098 → ex-top1 +0.232). `S133` settles 09-14. **No new information this run — nothing in the 09-05/09-06 feed touched it** (denominator: 385 market events read across the two days) |
| 3 | **Information Technology** | **N** ⚠ | `P137`(09-11) · `S140`(09-08) · `S145`(09-11) | −0.195 / −0.090 | −0.010 | ★ **+1.52** | −0.27 / **+0.27** | 26/56 | −0.99 / −1.82 | 🚨 **The board's best `exc1` is ONE SESSION** (`SMH` +2.61% vs `SPY` −0.39% on the payroll print) against `exc5` −0.27 and `exc20` −0.99. `P101` `FIRED-C` inverted the carried split: the 5-session drag is **EDA + security software**, not semicap (`M1315`). ★ New this run: *"Spot Memory Prices Are Running **4× Contract Prices**. That Is Not What a Cycle Peak Looks Like."* [**5 outlets**, 09-05] — a direct, multi-outlet challenge to the `MU` second-derivative carry, and **`MU`'s contracted-volume share is still `unknown` (`C3`)**, so it stays inadmissible |
| 4 | **Financials** | **N** | **`P128`(09-08)** · `S142`(09-11) | **−0.023** / −0.118 | −0.004 | −0.58 | −0.07 / **+0.10** | 21/47 | **+1.92 / +1.04** | Flat on flow, **positive on 20 sessions with median > 0**; `hy_oas` at the **2.0th percentile** remains the strongest fact standing *for* the bucket. `eqflow` −0.023 vs `wflow` −0.118 ⇒ the negative sign is weighted, not broad; **`eqflow` is the citable cut** (G5). ★ **`P128` settles 09-08 and is now in the master index** (HANDOVER §3e) — ⚠ its own settle depends on `hy_oas`, which currently stops at 09-03, so `D427` may reach it |
| 5 | **Utilities** | **N** | `P123`(09-08) · `P127`(09-10) · `S135`(09-11) · `S146`(09-14) | **+0.050** / +0.071 | −0.037 | +0.43 | **+0.35** / −0.13 | 8/15 | −1.36 / −1.17 | Positive on both flow cuts but breadth **0.00** and mean > median on `exc5` ⇒ **a few names, not a sector** — and `M1316` splits it into merchant (`CEG`,`VST`, the only positive-`rs20` pair) vs regulated (`rs60` −6.5 to −20.6). ⚠⚠ **That split has NOT been residual-correlation tested** (`D530`, opened this run from the KR desk's `R130`). ★ New: **`TURBINES` is a burst word today** and *"Musk's new foundry can get gas turbines online 18 months faster"* [3 outlets] lands **inside `P127`'s window** |
| 6 | **Materials** | **N−** ⚠ | `P102`(09-09) | −0.107 / −0.025 | −0.037 | +0.26 | −1.13 / **−2.44** | 9/12 | −0.85 / **−2.99** | Negative on **both** cuts, median far below mean on both windows ⇒ **two names still carrying the label** (`C24`, **7th run**). **Copper COT at the 100th percentile for a 6th consecutive run.** `rare earth` decelerates to **0.88× → this run 176 hits, −5.6% share**. **`P102` settles the two-name question 09-09** and this stage does not pre-empt it (`D343`) |
| 7 | **Real Estate** | **UW−** | `S135`(09-11) | −0.124 / −0.116 | −0.020 | −0.43 | −1.31 / −1.10 | **11/12** | −1.83 / −1.62 | Negative on every cut and every window, **11 of 12 negative on 5 sessions** — the board's most internally consistent bucket, and consistently bad. Rates at the 96th–99th percentile is the mechanism. ⚠ `D512`: `RE`+`STPL`+`UTIL` may be **one duration bet under three labels** — all three carry breadth 0.00 |
| 8 | **Consumer Staples** | **UW−** | `S135`(09-11) | −0.098 / −0.182 | −0.018 | −0.66 | −1.39 / **−2.29** | 12/19 | +0.03 / −1.94 | Negative on 5 sessions with median below mean; the 20-session mean ≈ 0 against a median of **−1.94** ⇒ the flat aggregate is one or two names. No defensive bid despite the rate move |
| 9 | **Consumer Discretionary** | **UW** | — | **−0.280** / −0.255 ⚠ | −0.004 | −0.25 | −2.38 / **−2.95** | ★ **21/28** | **−4.11 / −5.27** | 🚫 **`wflow` barred** (AMZN 40.2%, flips −0.255 → **+0.068** ex-top1). **`eqflow` −0.280 agrees with the sign, so the verdict stands on `eqflow` and says so.** Second-worst 20-session mean on the board with **21 of 28** negative — this one is **broad**, not weighted. The Cybercab→NHTSA probe sits inside the window and `TSLA` carries a standing `K.본문반증` rejection |
| 10 | **Communication Services** | **no verdict issued** | — | **−0.035** / −0.389 🚫 | +0.007 | −1.09 | −2.02 / −2.27 | **11/12** | **+1.27 / +3.70** | 🚫 **`wflow` barred entirely** — Alphabet is **76.6%** of the bucket under two tickers; ex-both-classes `wflow` **+0.272**, swing **0.661** (`D459`, **12th run**). `eqflow` **−0.035** is the only citable aggregate and it is **flat**. `exc20` median **+3.70** vs mean **+1.27** — the same one company dragging the mean. **A sector this desk cannot aggregate is a sector this desk does not rank** |
| 11 | **Industrials** | **UW** | `S126` (settled C) | −0.354 / −0.379 | ★ **+0.082** | +0.57 | −1.34 / −1.67 | ★ **33/50** | ★ **−5.04 / −5.90** | **The board's worst level and its LARGEST positive Δflow.** Worst `exc20` with **33 of 50** negative ⇒ the weakness is **broad**, not weighted. `S126` settled **`FIRED-C`** at −1.165pp. ⚠ `ETN`'s +3.46% and its `[FINRA]` z **+2.16** sit inside this label while the AI-power lane it belongs to spans two others (`D416`, `S146` 09-14) |

★★ **Three tensions handed to ROTATION unresolved (P4). All three are new or newly sharpened:**
1. ★★★ **Energy's level evidence is unanimous and its driver evidence has fractured into three
   opposed stories** — escalation (bullish barrel), Venezuela (bearish barrel, ambiguous crack), and
   a crack whose rate is at the 6th percentile while its level is at the 96th. **Two of the three are
   outside the price frame entirely.** ROTATION must decide whether an `OW` earned on Friday's tape
   survives Sunday's news, or whether the correct move is to wait for **09-08**. This stage does not
   say which.
2. **Industrials is the worst sector on level and the best on Δ** — carried from 09-05, unresolved,
   and **unchanged because no new session exists to resolve it.** ⚠ Repeating it is not new evidence.
3. 🆕 **Utilities' merchant-vs-regulated split and IT's software-vs-hardware split are both
   "a level difference between two nodes" — the exact object the KR desk's `R130` dissolved this
   morning under residual correlation.** Neither has been tested. `D530`.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 · Rows settled this run: **0 newly scored, 10 folded into the master log, 3 blocked, 3 `EXPIRED-UNSCORED`**
Full accounting in `HANDOVER §3`. **0 rows were due** — verified against the settle queue **and** an
exhaustive 152-block back-scan of `SCENARIOS_US.md`. **0 silent skips.**

### F-2 · ★★ The back-scan found what four runs of queue-reading could not
`S16` (07-29), `S24` (07-29) and `S42` (08-12) are **39/39/25 days past settle with no verdict
anywhere**, and all three share one signature: their last recorded state is an **interim "tracking"
line written 2026-07-30**, which contains the row id and a branch name and therefore **matches a
later run's verdict scan**. ⇒ **`D531`** — *an interim tracking line takes a token no verdict scan
will match.* They are marked **`EXPIRED-UNSCORED`**, not scored: reconstructing a 39-day-old capex
threshold is what `D242` forbids (**P5** — a human may re-register them).
★ **And `S25` (08-08) was scored correctly on 08-02 into the WRONG FILE** — its verdict lives in
`SCENARIOS_US.md`, never in the shared master log. Three distinct failure modes, one scan.

### F-3 · The pattern in registration states — n=2 and it stays withdrawn
`M1244`'s rule (*"a registration state leaning toward the branch that fired is a better-behaved
object"*) was built on `n=1` (`P100`) and contradicted by `P101` (registration **89.7th percentile
leaning A**, settle **−6.511, stopping 1.40pp short of B**). **It stays WITHDRAWN to "unmeasured."**
⚠ **`P139` and `P140` are both registered inside branch C leaning toward a named branch** (22.6th
and 45.6th percentiles) and both **disclose which branch is near** — so they will add samples 3 and 4
to this question rather than assuming its answer.

### F-4 · 🚨 What this stage asserted and then refuted, in the same run (`§4c` / `D48`)

1. ★★★ **This stage's first draft of B-4 read "every term on the board is down 5–27% — attention is
   draining from the whole complex."** That sentence was written, and then the stage measured its own
   denominator: **the window swapped a 1,711-article Sunday for a 557-article partial Sunday, −3.89%**,
   and share-normalized the median move is **−1.4%**. ⇒ **There is no draining; there is a shorter
   window.** The earlier sentence is not in the report; **the fact that it was written is** — because
   it is the identical error class the 09-05 run made on the oil thread's FADING tag (`D508`) and it
   arrived from the *other* instrument this time.
2. ★★ **An inherited number that carries a live thesis does not reproduce.** *"WTI printed $96"* is
   nowhere in the settled series — the window's highest print of any kind is **$93.14** (A-4). The
   **direction** survives (+9.69% over five sessions); the **level** and the **rate** as carried do
   not. ⇒ **`D534`**. ⚠ Recorded rather than quietly corrected, and scoped: `M1297`'s **crack**
   figures reproduce exactly, so this is one number, not a pattern.
3. ★ **This stage confirmed an inherited measurement and then discounted its own confirmation.**
   A-2's `+6.0 bp = 88.1st percentile` reproduces `M1283` exactly — **and the series published no new
   observation**, so it is the same measurement twice, not a replication (`M1359`). Recorded because
   an exact match on a weekend is the most inviting way to launder a null into evidence.
4. **Zero self-refutations would itself be a finding.** Three here; four more in `HANDOVER §9`.
   All three came from **running a measurement after the sentence was drafted**.

### F-5 · Digs registered by this stage
- **`D534`** — *A price LEVEL quoted inside a narrative sentence is re-pulled from the settled series
  before it is carried a second time; a direction that survives does not certify the number attached
  to it.* Origin: `M1360` (A-4).
- **`D535`** — *When the day's largest event on an OW sector is title-only across every outlet that
  carried it, the report records the SUBJECT and the ABSENCE of the mechanism, and names the venues
  tried.* Origin: the 13-outlet "Venezuela deal blindsides US energy" cluster — Bloomberg `[no body]`
  ×2, Japan Times `[error]`, `search --field any` and `fts` both exhausted (`D10` class).
- **`D536`** — *`blindspot` has no window argument on this runtime*, so it answers "what is
  historically frequent outside the fixed set," never "what is new today." Origin: it ran over
  324,584 articles (the full corpus) when a 7-day view was wanted.

---

## ✅ EXIT CHECK — MACRO

- [x] **Catalysts injected** — `catalyst_calendar --days 12` (beyond the default, because `SCENARIOS`
      carries armed dates to 09-18): **4 binaries in window — PPI 09-10 ✓ · CPI 09-11 ~est · FOMC
      09-16 ✓ · undated Hormuz-open statement 👁**, plus S&P quarterly rebalance/quad witching 09-18.
      ⚠ **None is ≤48h** (nearest is D-4), so PREMORTEM's mandatory ≤48h bracket **does not trigger on
      a date**. 🚨 **The calendar still carries no market-holiday row and so misses Labor Day 09-07**
      (`D532`, opened at HANDOVER), which governs three blocked scenario rows and every window count
      in this report. 🚨 **`ORCL` earnings this week is on no calendar and in no row** — handed to
      PREMORTEM. 🚨 **09-10 carries US PPI ∧ KOSPI200 quad witching and is unbracketed** (`D533`).
- [x] **Events read via `--body 2`** for **two** days (09-05 and 09-06), tail **0** on both.
- [x] **`tail = 0` is NOT the coverage claim** (§B-0): `single_source` **340 / 15 shown / min_nb 10.0 /
      scored 0 / scorable 0 / unscored 340**; `excluded_nonmarket` **count 0 by construction**;
      `subevents_recovered` **66**. **Visibility 296 of 621 clusters = 47.7%; 325 clusters exist only
      as a count.** The one "no new information" claim in this report (HLTH, §E row 2) cites the
      denominator that backs it.
- [x] **Denominator stated as the raw one**, because `excluded_not_news` returned **`{}`** and no
      correction was available — said so rather than implying a corrected figure.
- [x] **Trajectories read** (`thread --days 7`): per-day denominator printed **first**; every FADING
      tag in the window is shown to be **weekend-inflated**, and the two Iran threads read
      flat-to-RISING on weekday legs alone (`M1367`, §B-6). Every proposition names its thread's tag
      and curve, or states **"no thread"** explicitly — **`P139` does exactly that.**
- [x] **No bucket's low count is trusted from a quoted multi-word term** — all 18 terms were run in
      **both** conventions and both columns are printed, with the exact invocations recorded (`D473`).
- [x] **Both halves of every print cited.** The escalation carries its de-escalation side in §B-2
      (Bessent $40, OPEC+ unchanged, "small potatoes", economic-endurance framing) **before** any
      conclusion — the direct repair of `M1327`. `hy_oas` carries **level (2.0th pctile) and change
      (+2bp)** as separate objects (`D3`). The crack carries **level (95.6th) and rate (6.0th)**.
- [x] **Every relative-performance number names its benchmark inline** (`vs SPY`, equal-weight
      `us_top300` baskets, stated in the §E header). No statistical result is carried across markets:
      the KR desk's `ic_ledger`, `R130`–`R133`, and the KR news constant (58) are **named and not
      imported** (`W1`).
- [x] **Credit axis read and cited**: `hy_oas` **2.65 (2.0th pctile, 09-03)**, `ig_oas` **0.81**,
      `NFCI` **−0.558 (08-28, weekly)**. No credit-stress claim is made; the report states the
      opposite and cites the number.
- [x] **`real_10y` quoted with `breakeven_10y`** — §A-2 is built on exactly that pair, as a spread.
- [x] **Linter run on this file** — see the note appended below the check.
- [x] **Transmission matrix produced, all 11 sectors, one line each** (§E), with the G3/G5 bars applied
      per line and every Δ dated `09-03 → 09-04`.
- [x] **`MACRO_REPORT.md` written** with primary numbers explicit; **self-backtest appended** (§F);
      **new blind-spot term `Venezuela` folded into the term table** (§B-4) with its measurement.

---

## 📋 Stage run log — open decisions resolved without a human

1. **Whether an OW sector's verdict can be revised on news that post-dates the price frame** —
   resolved as **NO at this stage**: MACRO sets wind direction and hands the tension to ROTATION
   (P4). The escalation and the Venezuela axis are written as **propositions with settled-close
   observables**, not as matrix revisions.
2. **Whether OPEC+'s 09-06 "no change" voids `P126`** — resolved as **NOT a voider** (the clause names
   an *emergency production decision*; this was a scheduled meeting with no change), recorded at D-3
   rather than argued at scoring (`D450`).
3. **Whether to guess the mechanism of the unreadable 13-outlet Venezuela story** — resolved as
   **record the subject and the hole** (`D535`). The subject is confirmed across three outlets; the
   mechanism is not, and `P139` is written so that **either** mechanism is scoreable.
4. **Whether `Venezuela` enters the term table** — resolved as **yes**, on 487 hits and 2.95×
   acceleration; it would rank 9th of 18 and was absent, which is the blind-spot pass working.

---

> **Linter result** (`scripts/report_lint.py`, rules C1·C2·S6·D6): **0 findings.**
> ⚠ As the tool itself states, this is a **form** check — it does not judge whether the content is
> right. A clean lint is not a correct report, and this line exists so the clean result is not read
> as one.

---

# §5 · ADDENDUM — appended by DRIFT, 2026-09-06 (append-only; nothing above is rewritten)

## 5a · `drift_watch` result: NULL — and the null is weak, for a stated reason

`drift_watch --report llm_outputs/2026-09-06/industry_US/MACRO_REPORT.md`
⇒ **✅ no kill-switch term burst since the report's baseline. No staleness signal.**

⚠⚠ **`D282` reproduces for a 9th consecutive run and it governs how much this null is worth.**
The stage's spec is **+3–6h after the report completes**; this fired at **+0.7h**. A 42-minute
window on a **Sunday** — the lowest-volume day of the week, **557 foreign articles against a
4,700–5,800 weekday run** — cannot produce a burst on almost any term. ⇒ **the null is close to
uninformative and is reported as such rather than as reassurance.** The fix is scheduling, i.e.
human (**P5**).

★ The tool did correctly surface this report's own three anti-signal clauses for human cross-reading
(`P139`'s Venezuela-reversal clause, `P140`'s SPR/contract clause, and `P141`'s declared absence of a
price observable). **None of the three has fired.**

## 5b · ★★★ A correction the DRIFT window did NOT produce — it came from a later stage of this run

**This is the entry that matters, and `drift_watch` could not have found it**, because it is not a
term burst — it is a body-read of an article that was already in the corpus when MACRO ran.

**§B-3 of this report asserted a mechanism:** *"Venezuelan crude is heavy sour — the design feed of
the US Gulf Coast complex. A structural rise in heavy-sour supply is bearish the barrel and bullish
the heavy–light differential, i.e. bullish the refining margin."*

**`SECTOR_DEEP_ENRG §2` read the body four stages later and the mechanism does not survive intact:**

| what the body says | source |
|---|---|
| **Rystad: full production from EXISTING fields may not arrive until the mid-2030s**; CFR: **$10–20bn** to repair infrastructure, **≥$100bn and >a decade** for new fields; Venezuela currently produces **~1% of global output** | yahoo_finance, 2026-09-01, 9,736-char body |
| 🚨 **The binding constraint is REFINING, not crude.** **`VLO` told analysts on 2026-07-30 that it has been *"the largest U.S. consumer of Venezuelan crude over the last several years"* and expects processing rates to EXCEED its historical maximum** | same |
| `VLO` also flagged **~5 million b/d of global refining capacity OFFLINE** and **light-product inventories ~130 million barrels below normal seasonal levels** | same |
| Structure: **100-year concessions on 17 fields**, JV with **NABEP**, **the Pentagon's Office of Strategic Capital takes a 35% equity stake** in its parent, US takes **20% of production at cost** | same |

⇒ ★★ **The "cheaper heavy feed widens the incumbent's margin" reading is INVERTED**: an incumbent
already running **above its historical maximum** does not gain from more feed — **the scarce asset is
the coker, not the barrel.** ★ **What survives, and is strengthened**: the Energy OW's
**chain-position** specification (`M1245`/`M1246`), now on a **capacity-scarcity** mechanism rather
than a spread mechanism.

⚠ **`P139` is NOT re-thresholded** (`D242`). Its observable and both branch lines stand exactly as
registered. **What is corrected is this report's stated grading of which branch is informative**: §D
called branch A (upstream pays) the informative one; **the body puts the upstream payoff in the
mid-2030s, which makes A mechanically unlikely inside a 5-session window and lowers the row's
information content below what §D claimed.** Filed as **`M1380`**.

## 5c · Two instrument findings that arrived after §A/§B were written

1. ★★★ **`D541` — `fts search --full` / `--snippet` print stored article bodies, and this desk has
   invoked them ZERO times across six runs.** They are documented in
   `pipeline/L3_functions/drill_detail.md` and `pipeline/L2_modules/news.md` — the exact L3 this
   report's §B is told to call for the direction body-read. ⇒ **`D535`, registered in §F-5 of THIS
   report, is partly wrong**: the Bloomberg half stands (`[no body]`, blocked scraper), but the
   cluster's mechanism was readable all along from a different outlet whose body **is** stored, and
   `search` was **printing the body length (`body=9736자`) in the same line the desk read as evidence
   of absence.** `D535` is left standing and `D541` is appended beside it (append, not edit).
2. ★★ **`D543` — `theme-age`'s AGE leg measures the age of the WORD, not the age of the EVENT.**
   `Venezuela` scored **age ≥90 / accel 2.95×** — the **first** theme in 13 foreign measurements to
   clear the 2× acceleration leg (prior max 1.95×) — **while the deal driving it is eight days old.**
   ⇒ the 🟢FRESH gate **cannot by construction** mark a new event on an old proper noun as fresh,
   which covers most macro supply shocks. **This is a better explanation of 13 consecutive `F1`
   zeros than "no fresh themes exist,"** and it is a fixable defect rather than a market fact.

## 5d · What DID move in the tape after this report's baseline: nothing, and it cannot

**2026-09-07 is Labor Day.** NYSE is closed Saturday, Sunday **and Monday**. ⇒ **no settled price
observation can exist between this report and 2026-09-08**, so the entire class of drift this stage
exists to catch — a price/regime flip after the desk closes — **is structurally impossible for the
next ~33 hours.** ⚠ **The offsetting risk is the opposite one and it is real**: **news continues
through a market that cannot reprice**, and this run already carries a two-way military escalation
(09-05/06) that **no tape has seen.** ⇒ **the first settled close on 09-08 is doing three days of
repricing at once**, and every bracket registered today settles on the far side of it.
