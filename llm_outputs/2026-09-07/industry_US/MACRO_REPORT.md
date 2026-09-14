# MACRO_REPORT — industry_US · 2026-09-07 (Mon, **US Labor Day — NYSE closed**) · Stage 3 / L1·MACRO

> `--market us` · every news call `--scope foreign` (hard rule). All FRED values `[FRED]`.
> Daily anchor read: `llm_outputs/2026-09-06/industry_US/MACRO_REPORT.md` (§A–§F incl. `P139`·`P140`·`P141`)
> and the handoff ledger via `module_report_tags show`.

---

## §0 · 🚨 Instrument state governing every line below (from `preflight/PREFLIGHT.md`)

**Three axes are frozen and one is live. That fact organises this whole report.**

| axis | state | consequence for this report |
|---|---|---|
| **Price / flow** | 🔴 **frozen — 3rd consecutive run.** Sweep `asof` **2026-09-04**; all 11 sectors numerically identical to the 09-06 file on all 9 fields | §E's matrix is **recomputed from this run's own frame** and reproduces to the decimal. **Δflow may not be called "today's move"** — it is the **09-03 → 09-04** change |
| **Positioning (COT)** | 🔴 **frozen.** CFTC report date **2026-09-01** (Tue-close, released Fri 09-04). No new release exists | §C is a **restatement**, and says so on every line |
| **US macro releases** | 🔴 **none — federal holiday.** H.15 does not publish | `D427`'s block on `P121`/`P114`/`P125` has a **calendar floor**, confirmed (§A-1) |
| **News** | 🟢 **LIVE, and the only source of new information today** | §B carries the entire new content of this run. Direct `module_news_data` only — the **sweep's** news axis is dead (17.39%, ranks 1–52 only) and **may not be cited** |

**Claim-rights revoked for this report** (PREFLIGHT consolidated table): no theme-freshness/velocity
from `SECTOR_FLOW_US.json` · **no "sector X is quiet"** (247 of 299 unmeasured; **UTIL/MATR/RE at zero
measured names**) · no `wflow` verdict on **Cons. Disc.** or **Comm. Services** · no single-number
concentration claim · no cap-weight / `top1_w%` as current (54-day-old vector) · no verdict on `EA`.

---

## §A · Indicators — `[FRED]`, and the publication clock is again the first fact

### A-1 · `D427` reproduces an **8th** time, and the 09-06 run's pre-commitment HELD

`module_macro_us --days 400 --json`, pulled fresh this run:

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `T10YIE` **2.35** · `RRPONTSYD` 0.675 | `DGS2` **4.34** · `DGS10` **4.77** · `DGS5` 4.52 · `DGS30` **5.25** · `DFII10` **2.42** · `hy_oas` **2.65** · `ig_oas` **0.81** · `VIXCLS` **14.32** · `SOFR` 3.66 | `WALCL` 09-02 · `DTWEXBGS` **08-28** · `NFCI` **08-28** |

**Identical to the 09-06 split on every named value.** The 09-06 run wrote that Labor Day gives the
block a **calendar floor of 2026-09-08**; that prediction is now confirmed, not asserted. ⇒ `P121` ·
`P114` · `P125` **blocked for a 5th consecutive run**, and the block was **known in advance**
(`M1412`). ★ `P125`'s joint-date construction keeps it **unscoreable rather than mis-scoreable** — a
calendar-dated twin would have been scored branch A today on a `DFII10` value that does not exist.

### A-2 · The repricing's leg — recomputed from source, and it has not moved because nothing published

3-session (Δ`breakeven_10y` − Δ`real_10y`), recomputed from the raw series this run:

| 08-27 | 08-28 | 08-31 | 09-01 | 09-02 | **09-03** |
|--:|--:|--:|--:|--:|--:|
| +5.0 | −11.0 | −11.0 | −8.0 | −0.0 | ★ **+6.0 bp** |

**+6.0 bp = the 88.5th percentile** of trailing 252 (p05 −11.4 · **p15 −6.1** · p50 −0.0 · **p85 +5.0** ·
p95 +9.0). ⚠ **This is the same observation the 09-06 run reported, not a replication of it** — the
underlying series published nothing new. Stated because two runs printing the same number look like
confirmation and are not (`M1359`, carried).

### A-3 · The one-year extremes — the whole curve is pinned at the top while risk pricing is at the bottom

| series | last | asof | **pctile (252)** |
|---|--:|---|--:|
| `DGS10` | **4.77** | 09-03 | ★ **98.8** |
| `DGS2` | **4.34** | 09-03 | ★ **97.6** |
| `DGS30` | **5.25** | 09-03 | ★ **96.0** |
| `DFII10` (real 10y) | **2.42** | 09-03 | **94.0** |
| `T10YIE` (breakeven) | **2.35** | 09-04 | 66.7 |
| `ig_oas` | 0.81 | 09-03 | 65.9 |
| `SOFR` | 3.66 | 09-03 | 50.4 |
| `DTWEXBGS` | 118.75 | **08-28** | 21.0 |
| `NFCI` | **−0.558** | **08-28** | 8.9 *(n=56 weekly)* |
| `VIXCLS` | **14.32** | 09-03 | 🚨 **2.4** |
| `hy_oas` | **2.65** | 09-03 | 🚨 **2.0** |

★ **`real_10y` is quoted with `breakeven_10y` as the rule requires: 94.0th vs 66.7th percentile ⇒ the
nominal move is a REAL-rate move, not an inflation-expectation move** — which is `P121`'s standing
frame and it is intact on the last published observation.
★ **2s10s +0.43 (09-03) = the 17.5th percentile**, and it has been flat-to-marginally-steeper for six
sessions (0.47 · 0.47 · 0.47 · 0.39 · 0.41 · 0.40 · 0.40 · **0.43**).
🚨 **Credit axis, cited as required**: `hy_oas` **2.65 = the 2.0th percentile** and `VIXCLS`
**14.32 = the 2.4th**. **Any risk-off claim in this report that does not cite these two is labelled
narrative-only, and §B does so explicitly.** `NFCI` −0.558 at the 8.9th percentile says financial
conditions are *loose*, not tight — 10 days stale, stated.

### A-4 · The rate object that IS at a live extreme

`DGS2` **5-session change = +14.0 bp** (08-27 → 09-03) **= the 92.1st percentile** of trailing 252
(p05 −12.0 · p15 −7.0 · p50 +2.0 · **p85 +10.0** · p95 +15.7). The last five readings are
**+10 · +10 · +22 · +20 · +14 bp** — five consecutive prints at or above the p85 line.
⇒ **The front end has been repricing hard for a week, and that is the object §B's news axis is
independently screaming about.** This becomes `P142`.

### A-5 · Monthly series — lag stated, not hidden

`cpi` 332.813 and `core_cpi` 336.789 both **asof 2026-07-01** (~2-month lag; **August CPI prints
2026-09-11**). `unemployment` **4.1%** asof 2026-08-01. `m2` 23,218 asof 2026-07-01. **None of these
is current and none is used as a live anchor below.**

### A-6 · The crack complex — carried unchanged, because it cannot have moved

`M1361` (09-06): distillate crack peaked **106.23 on 09-01**, printed three lower closes to **99.21**,
3-session change **−$7.02/bbl = the 6.0th percentile** while the **level sits at the 95.6th**.
**No new session exists**, so this is carried verbatim rather than re-derived. `P140` (registered
09-06) is the row that settles it on **2026-09-11**.

---

## §B · News — the only live axis. **Coverage is stated before anything is concluded.**

### B-0 · Coverage, stated first (the tail is NOT the coverage claim)

`brief --scope foreign --body 2`, 2026-09-07:

| field | value |
|---|--:|
| **denominator.articles** | **1,720** ⚠ **PARTIAL DAY** — run at 22:2x KST = **09:2x ET**; the US day has barely begun |
| clusters | 644 |
| market events (≥2 src) | **279** |
| head (≥5 src) shown | **30** |
| body (2–4 src) shown | **249** |
| **tail** | **0** |
| `single_source` | **count 365 · shown 15 ⇒ 350 withheld** · `min_nb` 10.0 · **`scored` 0 / `unscored` 365** |
| `excluded_nonmarket` | **count 0 · shown 0**, band −3.0 |
| `subevents_recovered` | **44** |

🚨 **`tail = 0` buys almost nothing today, and the two recovery tiers are structurally broken in this
scope** (`D506`, reproduced): the non-market classifier is **Korean-only**, so in `--scope foreign`
`scored = 0` and the 15 single-source rows shown are a **random sample of 365**, not the top-`nb`
ones; and `excluded_nonmarket` is **empty by construction, not because nothing was excluded**.
⇒ **350 single-source clusters were not read and could not have been prioritised.** Every "quiet"
claim below carries that number.

⚠ **And the denominator itself is partial.** Today is a US holiday *and* the run fires early in the
ET day. **1,720 is not a day.** For reference, the same call re-run today for the settled days gives
**09-06 = 1,521** and **09-05 = 1,740** — against the 09-06 run's own same-day reading of
**557 for 09-06**. ⇒ ★★ **a same-day denominator understated its own day by 2.7×**, which matters
because the 09-06 run built its entire term-normalisation on that 557. See B-4.

### B-1 · ★★★ The run's central event: the rate-HIKE branch is being repriced, and it is dated

This is the one story that shows up on **every** live instrument at once — head, body, single-source,
threads, term counts and `theme-age` — while the price tape says nothing because it is closed.

**Head and body carriage** (`[news]`, outlet counts from `brief`):
- *"Bitcoin slips below $80k as **Fed hike bets**, oil surge weigh"* — Investing.com, inside the
  17-article/8-outlet Liquid Network cluster
- *"**Dollar barely gets lift** from boost in **Fed hike expectations**"* [4 outlets]
- *"As Wall Street shifts expectations towards a **Fed rate hike**, the White House turns up the
  pressure on **Warsh's** central bank"* [4 outlets]
- *"**Gold eases** as robust **US payrolls** boost **rate-hike bets**; inflation data in focus"* [3]
- *"**Copper Eases** on **Fed Rate Hike** Concerns"* [3]
- *"US Dollar: Volatility risks around Fed decision – Commerzbank"* [3]
- *"Here's Why **This Friday** Could Be One of the Most Critical Days for the Stock Market in
  September"* [3] — i.e. the **09-11 CPI**

**Thread carriage** (`thread --days 7 --scope foreign`):
- **REIGNITED, 5 days, outlets 4→6→2→9→5**: euro-area inflation → ECB hike → *"**Fed Rate Hike Impact
  on Markets and Bonds**"* [9 outlets, 09-04] → *"European markets edge lower, **ECB decision in
  focus**"* [5, today]
- **REIGNITED, 5 days, 3→5→7→4→8, 76 articles**: the **global bond selloff**
- **REIGNITED, 3→5**: *"10-Year Treasuries Yield About 4.8%…"*
- **REIGNITED, 4→3**: *"Gold Holds Drop as Higher Oil, Bond Selloff **Raise Rate**…"*

**`theme-age --scope foreign`**:

| theme | verdict | age | 7d avg | **accel** | base |
|---|---|--:|--:|--:|--:|
| ★★★ **`bond selloff`** | 🟡 **ACCELERATING** | ≥90 | 19.6 | ★★★ **5.93×** | **247** |
| ★ **`Fed hike`** | 🟡 **ACCELERATING** | ≥90 | 24.7 | **2.06×** | 942 |
| `Venezuela` | 🟡 ACCELERATING | ≥90 | 57.0 | 2.47× *(09-06: 2.95×)* | 1,570 |
| `payrolls` | ⚪ECHO | ≥90 | 84.4 | 1.88× | 2,625 |
| `rate hike` | ⚪ECHO | ≥90 | 174.0 | 1.64× | 7,630 |
| `Treasury yield` | ⚪ECHO | ≥90 | 103.3 | 1.51× | 3,917 |
| `ECB` | ⚪ECHO | ≥90 | 34.3 | 1.46× | 2,097 |
| `yen` · `LNG` | ⚪ECHO | ≥90 | 109.0 · 36.1 | 1.24× · 1.24× | 5,662 · 1,832 |
| `diesel` | ⚪ECHO | ≥90 | 37.4 | 1.04× | 2,036 |
| `data center` | ⚪ECHO | ≥90 | 303.1 | 0.97× | 19,880 |
| `Strait of Hormuz` | ⚪ECHO | ≥90 | 127.1 | 🔻 **0.88×** | 9,185 |
| `Hormuz blockade` | ⚪ECHO | ≥90 | 0.9 | 0.80× | 77 |
| `refining margin` | ⚪ECHO | **81** | 4.0 | 🔻 **0.68×** | 319 |
| `credit spread` | ⚪ECHO | ≥90 | 6.4 | 🔻 **0.61×** | 752 |

★★★ **`bond selloff` at 5.93× is the highest acceleration figure this desk has recorded on a foreign
measurement** — the prior maximum was `Venezuela` **2.95×** (09-06), itself the prior record.
⚠ **But it is on a base of 247**, i.e. ~2.4 articles/day baseline, so the multiple is fragile and the
absolute count (**137 in 7 days**) is small. **Both halves stated** (`C2`); the multiple is not quoted
without the base.
★ **Zero 🟢FRESH for a 14th consecutive foreign measurement** — but note the reason has now flipped:
`bond selloff` and `Fed hike` **clear the acceleration leg comfortably** and are blocked only by the
**age** leg (`≥90`), which measures the age of the *word*, not of the event (`D543`).

### B-2 · ⚠ The other side, read BEFORE any conclusion (`C2`)

The hike story is **not** one-sided in the tape, and three independent instruments say so:

1. **A FADING counter-thread with a longer history than the BUILDING one**: *"Fed's **Waller** says
   central bank's next rate move depends…"* — **8→11→16→9→6→7→4** over seven days, and a live
   REIGNITED sibling *"**Stocks, Bonds Rise as Fed-Hike Bets EASE on Waller**"* (6→3).
   ⇒ the same week carries *"hike bets rise"* and *"hike bets ease"* from the same official.
2. **The credit and vol tape refuses to confirm it**: `hy_oas` at the **2.0th percentile** and
   `VIXCLS` at the **2.4th** (§A-3). A repricing this violent at the front end with credit and vol at
   one-year lows is a **rates-only event on the last published data**, exactly `P128`'s question,
   which settles **09-08**.
3. **`credit spread` is the single most-decelerating theme on the board** — `theme-age` **0.61×**,
   raw count **−13.8%**, the only term of 18 that fell by double digits. ⇒ the narrative is *not*
   propagating to credit either.

⇒ **The honest reading is that this is a two-sided, dated object, not a trend to lean into.** That is
what `P142` brackets, both ways.

### B-3 · The escalation: the level is at an extreme and the NARRATIVE is decelerating

**Head #1**, 32 articles / **13 outlets**: *"Oil prices today: Crude rises as US-Iran strikes fuel
fears of prolonged Hormuz disruption"*, with sub-events *"Oil Rises as Escalating U.S.-Iran Conflict
Stokes Supply Disruption Fears"* [9 outlets] and *"Oil up, bitcoin down as U.S. strikes Iranian crude
carriers"* [3].

Corroborating rows, all `[news]`: *"**Iran, US Trade Tanker Attacks** as Conflict Escalates"* [6] ·
*"**India's Crude Oil Benchmark Tops $100** as Middle East War Escalates"* [6] · *"**Iran to announce
restricted zone outside Strait of Hormuz**"* [3] · *"Asia Spot **LNG** Prices Hit **5-Month High** as
Hormuz Blockade…"* (REIGNITED 5→3→2→3→2) · *"European **Gas** Climbs on **LNG** Supply Concerns Ahead
of Winter"* [3] · *"**Shipping Fuel Shortage Looms as Refiners Prioritize Diesel**"* [4].

🚨 **And the counter-evidence sits in the single-source tier, where it would have been missed**:
*"**WTI struggles to hold above $90** despite material supply risks"* — one outlet, in the random-15
sample. Against `M1360`'s settled figure (`CL=F` 09-04 close **$91.48**, window high $93.14), that is
the **consistent** reading: the escalation has been running for a week and WTI is at $91, not $120.

⇒ ★★ **Two instruments disagree with the headline and they agree with each other**:
`Strait of Hormuz` **theme-age 0.88×** (decelerating) and `Hormuz blockade` **0.80×** on a base of 77,
while the term's raw 7-day count is at the **top of the board (+7.2%)**. **A high level with a
decelerating rate** — the identical shape `P140` was written on for the crack, now visible on the
narrative instrument for the same complex. **Stated, not resolved.**

⚠ **`refining margin` decelerates for a 5th consecutive run (0.68×, age 81)** while the crack level
sits at the 95.6th percentile — `M1379` reproduces.

### B-4 · 🚨🚨 Term sweep — and the run's largest finding is that **the normalisation method is invalid**

`fts search --days 7 --scope foreign --count`, both conventions printed (`D473`).

| term | phrase | argv | 09-06 phrase | **raw Δ** |
|---|--:|--:|--:|--:|
| `rate hike` | **1,389** | 1,750 | 1,291 | ★ **+7.6%** |
| `Strait of Hormuz` | **1,040** | 1,050 | 970 | ★ **+7.2%** |
| `payrolls` | **640** | 640 | 599 | ★ **+6.8%** |
| `yen` | **859** | 859 | 812 | ★ **+5.8%** |
| `refinery` | 288 | 288 | 275 | +4.7% |
| `Treasury yield` | 775 | 1,220 | 743 | +4.3% |
| `Federal Reserve` | 1,377 | 1,544 | 1,324 | +4.0% |
| `diesel` | 291 | 291 | 280 | +3.9% |
| `crude oil` | 817 | 1,333 | 790 | +3.4% |
| `inflation` | 2,984 | 2,984 | 2,887 | +3.4% |
| `bond selloff` | 137 | 266 | 134 | +2.2% |
| `data center` | 2,387 | 3,053 | 2,378 | +0.4% |
| `AI capex` | 101 | 403 | 102 | −1.0% |
| `tariff` | 1,649 | 1,649 | 1,715 | −3.8% |
| `Venezuela` | 461 | 461 | 487 | −5.3% |
| `rare earth` | 166 | 224 | 176 | −5.7% |
| `gas turbine` | 78 | 103 | 84 | −7.1% |
| `credit spread` | **56** | 331 | 65 | 🔻 **−13.8%** |

**Raw dispersion 21.4pp, median +3.4%.** The ranking is coherent and matches §B-1/§B-3 independently:
**rates + Hormuz + payrolls + yen at the top; credit spread, gas turbine, rare earth and Venezuela at
the bottom.** `Venezuela` decelerating on both instruments (−5.3% raw, `theme-age` 2.95× → 2.47×)
is the notable reversal against the 09-06 run's headline finding.

#### 🚨🚨 **`D557` — the share-normalisation both this run and the 09-06 run used divides two different populations, and one measurement proves it**

This stage set out to repeat the 09-06 method (divide each term's count by the window's article
denominator). Before publishing the result it ran the control the method requires. **The control
falsified the method:**

| control term | `fts --days 1 --scope foreign --count` | `brief --date 2026-09-07 --scope foreign` `denominator.articles` |
|---|--:|--:|
| `company` | **1,741** | **1,720** |
| `market` | **1,952** | **1,720** |

**A single term cannot match more articles than the day contains.** ⇒ **`fts --days N --count` and
`brief`'s `denominator.articles` count different populations** (different date field, or pre- vs
post-dedup/cluster). Confirmed by a second signature: the per-lookback-slot increments of
`inflation` are **412 · 294 · 441 · 447 · 570 · 480 · 340** while the per-calendar-day article counts
swing **1,720 · 1,521 · 1,740 · 4,719 · 5,380 · 5,813 · 5,465** — a **3.8× denominator range against
a flat numerator**, and the ratio decays monotonically with lookback (1,012 → 225 per thousand),
which is what a **different timestamp field**, not a calendar window, produces.

**Consequences, stated in both directions:**
- ⚠ **This run does NOT publish a share-normalised column.** The raw table above is the citable object.
- 🚨 **`M1364`'s share leg is retracted** (its raw leg stands). *"Share-normalized the entire board
  collapses to ±5% flat, median −1.4%"* divided an `fts` count by a `brief` denominator, so its
  magnitude is not interpretable. The 09-06 run's raw observation — **17 of 17 terms fell** — remains
  a measurement; **the conclusion drawn from normalising it does not.** Filed as **`R139`**.
- 🚨 **`P141`'s premise is superseded before its own falsifier date.** `P141` (09-06) attributes the
  uniform decline to a **truncated final day** and proposes re-running on a full weekday (09-08).
  That test would not have found this: **the mismatch is present on every day, truncated or not.**
  `P141` is **not retracted** — its *observation* is intact and its falsifier is still worth running —
  but its **diagnosis is superseded** by `D557`, and this is recorded rather than quietly replaced.
- ✅ **What survives**: raw run-over-run Δ compared *between terms* (the window defect is common-mode
  for ranking), and the `theme-age` accelerations, which are computed inside one instrument.

⚠ **`C5`/`D473` unchanged**: the two conventions still disagree by up to **5.9×** (`credit spread`
56 vs 331). Every Δ above is the **phrase** read, matching the convention the 09-06 numbers used.

### B-5 · Trajectories — and the FADING tags are again denominator artifacts

Per-day event counts from `thread --days 7`: **09-01 858 · 09-02 944 · 09-03 879 · 09-04 732 ·
09-05 291 · 09-06 271 · 09-07 279.** ⇒ the last three days run at **~1/3** the weekday rate (weekend
plus a US holiday). **`M1367` reproduces**: every 🔴FADING tag whose curve crosses that boundary is
partly arithmetic. Read on weekday legs only:

- 🔴 **`Nvidia to Acquire Hugging Face for $12.9bn` — 4→28→9→2→2.** This one is **real fading**, not
  an artifact: the collapse from 28 to 9 happened **inside the weekday block** (09-02→09-03).
  ⇒ relevant to **`S130` (settles 09-10)**, and the deceleration is recorded now rather than argued
  at scoring (`D450`).
- 🔴 **`Opposition to oil deal with U.S. grows in Venezuela` — 22→19→14→21→13→9→13.** Tagged FADING,
  but today's **13 exceeds yesterday's 9 on a smaller denominator** ⇒ **the tag is not supported**;
  the thread is flat-to-firm. Directly relevant to **`P139`** (registered 09-06, settles 09-14).
- 🟢 **BUILDING, 3 days, 3→3→5**: *Druckenmiller on the 30-year* → *"US National Debt Surpasses $40
  Trillion"* → *"'Uncharted territory': …interest payments rise to $1.25 trillion a year"* [5 outlets].
  ⇒ **a fiscal/duration thread with no bracket on this desk.** Named for PREMORTEM.
- 🟢 **BUILDING, 2 days, 3→7**: *China injects **over €45bn** into state banks and insurers as growth
  slows* [7 outlets].
- 🟢 **REIGNITED, 2→6**: *Japan's August foreign reserves post **largest-ever drop** after record
  intervention*; plus *Yen at a **seven-month high***, *BoJ hawks raise hike risk*, and *Takaichi's
  reflationist aide **projects a BoJ hike in September***. ⇒ this becomes **`P143`**.

### B-6 · Blind-spot / burst pass — null, and the null is denominator-bound

`burst --scope foreign`, denominator **1,720** (partial holiday day). Top z-scores are
`TRENDING` 13.6 · `ATTENTION` 11.7 · `HELIOS` 10.3 · `XIAOMI` 10.0 — of which only **`HELIOS`**
(AMD's rack-scale system, from *"Data Center Passes 70% of AMD's Revenue in 2027, Before the Helios
Ramp Is Finished"* [5 outlets]) touches a market object, on **3 articles**. Tier ② (unseen words)
tops out at 9 articles.

⇒ **No new term is promoted to the table this run.** ⚠ And that null is **not** evidence of a quiet
tape: the burst denominator is a third of a weekday's and **350 single-source clusters were withheld
unranked** (B-0). Stated as a coverage limit, not a finding.

---

## §C · Positioning — `[COT report date 2026-09-01, Tue-close, released Fri 09-04]`

⚠ **No new COT release exists** — the CFTC publishes Friday for Tuesday data, and the next release is
**Friday 2026-09-11**. **Every row below is a restatement of the 09-06 report, verified identical.**

| instrument | net spec | wk Δ | **1y %ile** | read |
|---|--:|--:|--:|---|
| **Copper** | +80,869 | −4,397 | ★ **100th** | 🟢 crowded-long — **7th consecutive run at the 100th percentile** (`C24`) |
| **Nasdaq-100** | +27,077 | **+15,951** | **82nd** | 🟢 crowded-long |
| UST 2Y | −882,518 | −21,222 | 71st | 🟡 neutral |
| WTI Crude | +35,574 | +4,475 | 70th | 🟡 neutral |
| USD Index | +17,025 | −1,657 | 70th | 🟡 neutral |
| S&P 500 | −75,941 | −7,947 | 63rd | 🟡 neutral |
| Gold | +228,124 | −15,210 | 50th | 🟡 neutral |
| Silver | +26,739 | +1,478 | 44th | 🟡 neutral |
| Russell 2000 | −14,741 | +1,377 | **17th** | 🔴 crowded-short |
| **UST 10Y** | −909,275 | **−70,300** | 🚨 **9th** | 🔴 crowded-short |
| Nat Gas | −208,911 | −10,979 | 🚨 **0th** | 🔴 crowded-short |

⚠⚠ **The single most important limitation of this section, stated rather than buried**: the COT
snapshot is **Tuesday 09-01**, i.e. it **pre-dates the 09-05 US strikes on Iranian tankers, the whole
of §B-1's hike repricing, and the 09-04 payroll print.** It is **context, never a trigger** (`D6`),
and it is 6 days old on an axis that §B says moved hard inside those 6 days.
★ The one line worth carrying forward: **UST 10Y specs are crowded-SHORT at the 9th percentile and
got 70k more short in the week** — i.e. the bond selloff §B-1 is accelerating on is one the
speculative community was **already positioned for**, which is the opposite of an un-chased move.

---

## §D · Propositions registered this run — `P142` · `P143` · `P144`

> Registered deliberately **few**. With the price tape frozen for a third run, a row whose branch
> lines come from the same `D93` distribution the 09-05 run used is *width without information*
> (`D503`). All three below are anchored on the **live** axis (news + the last published FRED close),
> which is the only axis that produced anything new today.

### `P142` — ★★★ The front end has repriced five sessions running. Is this a HIKE path, or a term-premium/supply event?

**Claim.** `DGS2`'s 5-session change is **+14.0 bp = the 92.1st percentile**, the fifth consecutive
print at or above p85 (§A-4), and the news axis independently carries **`Fed hike` at `theme-age`
2.06×** with hike language in five separate outlets' framing (§B-1) — while **credit and vol sit at
the 2.0th and 2.4th percentiles** and the strongest counter-thread on the board is Waller **easing**
hike bets (§B-2). **The desk has no live row on the front end**: `S19` was the hike bracket and this
run just scored it **FIRED-M** on a July window; `P121` is a *level* claim and is blocked by `D427`.

| | |
|---|---|
| **Frozen observable** | **`DGS2` `[FRED]` 5-session change in basis points**, at the **first `[FRED]` close covering 2026-09-11** (the August CPI session) |
| **Branch A (the hike path is being priced)** | **≥ +10.0 bp** (trailing-252 **p85**) — the front end extends its repricing *through* the CPI print, and the FOMC on **09-16** becomes a live two-sided event for every duration-sensitive tilt on the board |
| **Branch B (it was a supply/term-premium event and it mean-reverts)** | **≤ −7.0 bp** (trailing-252 **p15**) — the move was the global bond selloff (§B-1, `bond selloff` 5.93×) reaching the US front end, and it unwinds once the auction/CPI calendar clears |
| **Branch C** | between −7.0 and +10.0 = the disclosed favourite |
| **`D93` executed BEFORE freezing** | trailing 252 of `DGS2` 5-session change, bp: p05 **−12.0** · **p15 −7.0** · p50 **+2.0** · **p85 +10.0** · p95 +15.7 ⇒ A ≈15% · B ≈15% · C ≈70% |
| **State at registration** | **+14.0 bp = the 92.1st percentile — already ABOVE branch A's line.** ⚠⚠ **Disclosed: A is therefore the LOW-information branch and B is the informative one.** A continuation prints A almost mechanically; only B tells the desk something it does not already believe (`L3`) |
| **Anti-signal (VOID)** | an **unscheduled FOMC action or emergency statement**, a **BLS delay/restatement of the August CPI release**, or **`hy_oas` ≥ 3.10% on a close** inside the window (then it is a credit event and the rate attribution is void — the same clause `S19`/`S41` used) |
| **Track KPI** | if **A**, `Fed hike` `theme-age` should hold above 2× and `credit spread` should stop decelerating; if **B**, `bond selloff` (5.93× on base 247) should fall back inside 2× |
| **Dated catalyst** | **US August CPI 2026-09-11** (`[bls~est]`), with **US August PPI 09-10** `[bls✓]` inside the window and **FOMC + SEP 09-16** just outside it |
| **Thread** | 🟡 ACCELERATING — `Fed hike` **2.06×** / `bond selloff` **5.93×** (base 247, stated); counter-thread `Waller` **FADING 8→11→16→9→6→7→4** with a live REIGNITED sibling *"Fed-Hike Bets Ease on Waller"* (6→3) |
| **Non-redundancy (`D343`)** | `P121` is a **level** claim (`DGS2` ≥ 4.50 / ≤ 4.18) and is **blocked by `D427`**; `P125` measures **which leg** of the nominal yield moves; `P128` measures **credit** (`hy_oas`). **No row measures the front end's RATE of change**, which is the object at the 92nd percentile |
| **⚠ `D427` exposure, declared at registration** | `DGS2` currently stops at **09-03**. If the H.15 lag persists, this row is **blocked, not mis-scored** — the observable names the *first close covering 09-11*, deliberately copying `P125`'s construction, which is the only thing that has protected a row from `D427` so far |
| **Owner** | `industry_US` |

### `P143` — ★★ The BoJ/yen carry channel: a global-duration binary that **no row on this desk brackets**

**Claim.** `FXY`'s 5-session change is **+2.48% = the 94.8th percentile** of trailing 252 — the yen at
a **seven-month high** — and the news axis carries the mechanism explicitly: *Japan's August foreign
reserves post their **largest-ever drop** after **record intervention*** [6 outlets], *Takaichi's
reflationist aide **projects a BoJ hike in September***, *BoJ hawks raise hike risk*, *traders spy a
sea-change*. **A BoJ hike is the classic transmission into US long duration** (carry unwind), and
`DGS10` sits at the **98.8th percentile** with specs **crowded-short at the 9th**. **This desk has
carried `yen` as a term for weeks (859 hits, 4th-largest raw gain) and has never bracketed it.**

| | |
|---|---|
| **Frozen observable** | **`FXY` 5-session % change**, settled closes, `auto_adjust=False`, window **2026-09-04 close → 2026-09-11 close** (5 settled sessions: 09-08, 09-09, 09-10, 09-11 — ⚠ **4 sessions, because 09-07 is a US holiday**; the window is defined as *the 5 settled closes following 09-04*, which is **09-08 → 09-14**) |
| **Branch A (the carry unwind is real and continues)** | **≥ +0.704%** (trailing-252 **p85**) — the yen extends; US long duration takes the second leg and the desk's rate-sensitive underweights face a driver that is **not** the Fed |
| **Branch B (intervention exhaustion — it reverses)** | **≤ −1.062%** (trailing-252 **p15**) — the record intervention was the move, not a policy turn, and the channel closes |
| **Branch C** | between = the disclosed favourite |
| **`D93` executed BEFORE freezing** | trailing 252 of `FXY` 5-session % change: p05 **−1.546** · **p15 −1.062** · p50 **−0.281** · **p85 +0.704** · p95 +2.486 ⇒ A ≈15% · B ≈15% · C ≈70% |
| **State at registration** | **+2.480% = the 94.8th percentile — above p95, i.e. above branch A's line already.** ⚠ **Disclosed: A is the low-information branch; B is the informative one**, and B is also the branch that would *close* a risk the desk has not been counting |
| **Anti-signal (VOID)** | a **further announced MoF/BoJ FX intervention** inside the window (then the observable measures policy, not positioning), or a **BoJ emergency meeting** |
| **Track KPI** | if **A**, `DGS30` (5.25, 96th pctile) should not retreat and `yen` raw count should hold above 850; if **B**, `yen` falls back with `bond selloff` |
| **Dated catalyst** | ⚠ **The BoJ's September meeting date is NOT in `catalyst_calendar`** (`--days 10` lists PPI, CPI, FOMC and nothing else) and this stage does **not** invent it. The window is set by the desk's own 5-session convention, not by the meeting — **stated rather than dressed up** |
| **Thread** | 🟢 REIGNITED **2→6** (FX reserves) + REIGNITED **5→6→7→3** (yen/BoJ rate bets) + **3→2** (Commerzbank JPY). `theme-age` `yen` ⚪ECHO **1.24×** — ⚠ **the theme instrument does NOT confirm the thread instrument**, which is `D508`'s exact class and is disclosed here rather than resolved |
| **Non-redundancy (`D343`)** | Nothing on the board contains a non-USD rate object. `P142` is the **US front end**; `P128` is **US credit**; `P124` is the **dollar** (`DTWEXBGS`, and 10 days stale). **`FXY` is a distinct instrument measuring a distinct policy** |
| **⚠ `W1` note** | This is a **US-desk row on a US-listed instrument** measuring a foreign policy's transmission into US duration. It is **not** an import of a KR/JP-measured result; no cross-market statistical transfer is made |
| **Owner** | `industry_US` |

### `P144` — ★★★ An INSTRUMENT proposition (no price observable, registered here so it is not a `D504` orphan)

**Claim.** *A term count from `fts search --days N --count` and an article denominator from
`brief --date` measure different populations, so their ratio is not a share and cannot be differenced
across runs. Any "attention share" conclusion built from that ratio is uninterpretable in magnitude,
in either direction.*

**Measured origin** (B-4), and the measurement is a single decisive inequality:
`fts search company --days 1 --scope foreign --count` = **1,741** against
`brief --date 2026-09-07 --scope foreign` `denominator.articles` = **1,720**. **A term matched more
articles than the day contains.** Second signature: `inflation` per-lookback-slot increments
**412·294·441·447·570·480·340** against calendar-day article counts **1,720·1,521·1,740·4,719·5,380·
5,813·5,465** — a 3.8× denominator range against a flat numerator, with the ratio decaying
monotonically by lookback slot.

**Falsifier** (what would show this is wrong): find any single day on which
`fts --days 1 --count` for a broad term is **≤** that day's `brief` denominator **and** the per-slot
increments track the per-day denominators within ±20%. One clean day of that would mean the two
tools do share a population and the 09-07 reading was a boundary effect.

**What this row does NOT claim**: it does not say the term counts are wrong, and it does not retract
the 09-06 run's raw observation that 17 of 17 terms fell. It says the **normalisation** is invalid.
The raw table and the `theme-age` accelerations (computed inside one instrument) are unaffected.

⚠ **No price observable ⇒ not a bracket, and NOT written into `SCENARIOS.md`'s index.** It is recorded
here and named in the writeback — following the 09-06 run's precedent for `P141`. **Stating the
absence is what keeps `D504` from reproducing.**

**Supersession, stated explicitly** (`D48`): `P141` (09-06) diagnosed the same symptom as *a truncated
final day*. `P144` shows the defect is present on **every** day. `P141` is **not retracted** — its
observation stands and its 09-08 falsifier is still worth running — but its **diagnosis is
superseded**, and the earlier sentence is left standing rather than edited.

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each. **This is ROTATION's input.**

> **Wind direction only, not a ranking.** `exc1/5/20` are **equal-weight `us_top300` constituent
> baskets, excess vs `SPY`** (benchmark named inline, `C1`), recomputed **this run from this run's own
> price frame**, all through the settled **2026-09-04** close. **`breadth5` = names with positive
> 5-session excess.** ⚠ **Flow columns are the 09-03 → 09-04 change** and may not be read as today's.

| # | sector | wind | driving row | eqflow / wflow | Δflow (09-03→09-04) | exc1 | exc5 mean/med | breadth5 | exc20 mean/med | note |
|---|---|---|---|---|--:|--:|---|--:|---|---|
| 1 | **Energy** | **OW** | **`P126`(09-09)** · `P139`(09-14) · **`P140`(09-11)** | **+0.562** / +0.440 | +0.054 | −0.27 | **+1.89 / +1.44** | ★ **15/16** | ★ **+12.29 / +11.52** | The board's only unambiguous OW and its **breadth is 15 of 16**. ⚠ **But its two narrative instruments both decelerate** — `Strait of Hormuz` **0.88×**, `refining margin` **0.68×** (5th run) — while crude sits at $91 and the crack level at the 95.6th percentile with its rate at the 6.0th. **Level-vs-rate split on three instruments at once** |
| 2 | **Health Care** | **N+** | `S133`(09-14) | **+0.190** / +0.098 | −0.043 | −0.44 | **+0.63 / +0.98** | 20/32 | **+3.63 / +3.74** | Positive on every cut, median above mean on both windows ⇒ **broad, not carried**. The only other bucket with a positive `eqflow` |
| 3 | **Information Technology** | **N** | `S140`(09-08) · `S148`(09-14) · **`P142`(09-11, new)** | −0.195 / −0.090 | −0.010 | **+1.52** | −0.27 / **+0.27** | 30/56 | −0.99 / −1.82 | ⚠ **The cuts disagree and that IS the reading**: `exc5` mean −0.27 but median **+0.27** with **30 of 56 positive** ⇒ a few large names dragging. `exc1` **+1.52 = the board's best single session**. `P101`'s SW-vs-HW inversion (settled `FIRED-C`, −6.511) is the live structure and **`S148` re-tests it 09-14 across `ORCL`+`ADBE` on 09-10** |
| 4 | **Financials** | **N** | **`P128`(09-08)** · `S142`(09-11) · **`P142`(new)** | **−0.023** / −0.118 | −0.004 | −0.58 | −0.07 / **+0.09** | 26/47 | **+1.92 / +1.04** | Flat on flow, **positive on 20 sessions with median > 0**. `eqflow` −0.023 is the citable cut (G5). ★ **`hy_oas` at the 2.0th percentile remains the strongest fact standing FOR the bucket** — and **`P128` settles it 09-08**, `D427` permitting |
| 5 | **Utilities** | **N−** | `S135`(09-11) · `S146`(09-14) | **+0.050** / +0.071 | −0.037 | +0.43 | +0.35 / **−0.13** | 7/15 | −1.36 / −1.17 | ⚠ **Positive flow, negative price, mean-vs-median disagreement, breadth 7/15** — the least internally consistent bucket on the board. 🚫 **`D537`: its sweep breadth 0.00 is a `vol_surge` filter artifact** (`M1372`), so breadth may not be used against it. ⚠ **`theme-age` measured 0 of its names — no "quiet" claim admissible** |
| 6 | **Materials** | **N−** | **`P102`(09-09)** | −0.107 / −0.025 | −0.037 | +0.26 | −1.13 / **−2.44** | **3/12** | −0.85 / **−2.99** | Negative on both cuts, **median far below mean on both windows** ⇒ two names carrying the label (`C24`, **8th run**). **Copper COT 100th percentile, 7th consecutive run** — but the COT is **09-01 data**. `rare earth` **−5.7% raw**. **`P102` settles the two-name question 09-09**; this stage does not pre-empt it (`D343`) |
| 7 | **Consumer Staples** | **UW** | `S135`(09-11) | −0.098 / −0.182 | −0.018 | −0.66 | −1.39 / **−2.29** | 7/19 | +0.03 / −1.94 | Negative on flow and on 5 sessions with median below mean; the 20-session mean is flat only because of a few names. `D512`: may be a **duration** leg, not a staples verdict |
| 8 | **Real Estate** | **UW−** | `S135`(09-11) | −0.124 / −0.116 | −0.020 | −0.43 | −1.31 / −1.10 | 🚨 **1/12** | −1.83 / −1.62 | Negative on **every** cut and **every** window; **1 of 12 positive on 5 sessions** — the board's most internally consistent bucket, and consistently bad. **`DGS10` at the 98.8th percentile is the mechanism**, and `P142` now brackets whether that rate keeps moving. ⚠ `D512` |
| 9 | **Industrials** | **UW−** | `S150`(09-14) | −0.354 / −0.379 | +0.082 | **+0.57** | −1.34 / −1.67 | 17/50 | 🚨 **−5.04 / −5.90** | **Worst 20-session basket on the board on both mean and median.** ⚠ **The largest Δflow on the board (+0.082) sits here** — but that is the 09-03→09-04 change, already reported twice, and is **not** evidence of a turn. `M1370`: Aerospace & Defense is **16th of 19 industries** at `eqflow` −0.622, `EW{RTX,LMT,NOC,GD,LHX}`−`SPY` at the **7.1st percentile** — bracketed by `S150` |
| 10 | **Consumer Discretionary** | **UW** | — | −0.280 / −0.255 🚫 | −0.004 | −0.25 | −2.38 / **−2.95** | 7/28 | 🚨 **−4.11 / −5.27** | 🚫 **`wflow` barred** (AMZN 40.2%, `top1_flips_sign` **True**). **`eqflow` −0.280 is the citable cut and it agrees with the sign** — the bucket is negative on every price window with median below mean. **This is the one barred-`wflow` sector where the equal-weight cut still supports a verdict**, and that is stated on the line as required |
| 11 | **Communication Services** | **no verdict issued** | — | **−0.035** / −0.389 🚫 | +0.007 | −0.97 | −1.85 / −2.22 | 🚨 **2/13** | **+1.27 / +3.70** | 🚫 **`wflow` barred entirely** — Alphabet is **76.6%** under two tickers; ex-both-classes `wflow` **+0.272**, swing **0.661** (`D459`, **13th run**). `eqflow` **−0.035 = flat**. `exc20` median **+3.70** vs mean **+1.27**, `exc5` **2 of 13** positive ⇒ **the cuts contradict each other across windows**. **A sector this desk cannot aggregate is a sector this desk does not rank** |

★ **The matrix carries the same wind as 09-06, because the price data is the same data.** What
changed is **which rows are live**: `P142` now points at IT · Financials · Real Estate · Utilities
through a single rate object, and `P143` points at Real Estate · Utilities · Financials through a
**second, non-Fed** duration driver the board has never carried.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 · Rows settled this run: **4 newly scored · 1 half-scored · 1 `EXPIRED-UNSCORED` (reassigned) · 3 blocked**

Full measurements in `HANDOVER.md` §3d and in `handoff/SCENARIOS.md`'s new master-log block.

| row | settle | verdict | for/against the desk |
|---|---|---|---|
| `S19` | 07-29 / 08-05 | **FIRED-M** | neutral — *"no conclusion changes"* |
| `S9` | 07-29 (no end date) | **FIRED-B** | **for** — but B was the disclosed **low-information** branch |
| `S41` | 08-12 | **FIRED-B** | ★★ **for** — the single-name AI CDS widening did **not** transmit to the index; `S26-A` held |
| `S46` | 08-13 | ★★ **FIRED-A** | 🚨 **AGAINST** — a ledger revival taken on a flow pull hours before an unbracketed binary was **wrong**, measured |
| `S14` | 08-06 | **A-partial** | branch B ruled out; A's fundamental leg unretrievable (`D556`) |

⇒ **The scoreboard this run is 1 clean against-us, 2 for-us (one of them low-information), 1 neutral,
1 half.** The against-us one lands on a **decision class**, not a name, which is the more useful kind.

### F-2 · ★★ The run's largest finding is an instrument finding, and it retracts one of this desk's own numbers

`D557`/`P144` (B-4) shows the term-share normalisation divides two populations. **`M1364`'s share leg
is retracted (`R139`)** — one run after it was written, by this desk, about this desk. That is the
correct latency for an error of this class and it is stated as such rather than presented as a
routine update.

### F-3 · Propositions carried, with their state

| row | settle | state today |
|---|---|---|
| `P121` · `P114` · `P125` | blocked | 🚨 **5th consecutive `D427` block**, floor confirmed at 09-08 |
| `P128` (credit) | **09-08** | reference only (`D242`): `hy_oas` 5-session change at 09-03 = **+2 bp**, inside C; **level 2.65 = the 2.0th percentile.** `D3` applies — the **level** is extreme, the **change** is mid-pack, and the row is written on the change. ⚠ `hy_oas` stops at 09-03 ⇒ `D427` may reach it |
| `P126` (barrel vs chain) | 09-09 | OPEC+ kept policy unchanged 09-06 ⇒ **NOT a voider** (`M1363`), recorded at D−2 not argued at scoring |
| `P127` (power vs compute) | 09-10 | window closes on US PPI; PPI is **not** in its anti-signal list ⇒ **not a voider**, recorded now (`D450`) |
| `P139` (Venezuela leg) | 09-14 | ⚠ its driver **decelerated** this run: `Venezuela` `theme-age` **2.95× → 2.47×**, raw **−5.3%**; but its thread is **flat-to-firm, not fading** (B-5). Both stated |
| `P140` (crack rate vs level) | 09-11 | `refining margin` **0.68×**, a 5th consecutive decelerating run, consistent with branch A's premise. **Not a score** |
| `P141` (instrument) | — | **diagnosis superseded by `P144`**, observation intact, **not retracted** |

### F-4 · 🚨 What this stage asserted and then refuted, inside the same stage (`D48`)

1. ★★★ **This stage computed and formatted a full share-normalised term table** — median **+11.9%**,
   16 of 18 terms up more than +5% — **and then deleted it**, because the control test showed the
   denominator is not the term counts' population. **The mirror image of the 09-06 run's
   "17/17 fell"** was sitting in this report's draft, and it would have read as *"attention flooded
   into everything"*, which is not a thing that happens either. The sentence is left here rather
   than removed.
2. ⚠ **A first attempt normalised yesterday's counts against a denominator re-pulled today**
   (09-06 = 1,521 rather than the 557 the 09-06 run saw). That is a **maturity mismatch** and it
   inflated every term; it was caught and discarded before it reached the second draft. Recorded
   because it is a distinct error from (1) and would recur.

### F-5 · Digs registered by this stage

| id | dig |
|---|---|
| **`D557`** ★★★ | *`fts search --days N --count` and `brief --date`'s `denominator.articles` count different populations — a term matched **1,741** articles on a **1,720**-article day. Never divide one by the other; publish raw counts and inter-term dispersion instead.* |
| **`D558`** | *A cross-run term comparison requires both legs measured at the same data maturity. Re-pulling the prior window's denominator today while using the prior run's counts inflates every term — measured: 09-06's own denominator grew **557 → 1,521 (2.7×)** after its run.* |
| **`D559`** | *`theme-age`'s zero-🟢FRESH streak (now 14) is no longer an acceleration failure: `bond selloff` **5.93×** and `Fed hike` **2.06×** both clear the acceleration leg and are blocked solely by the **age** leg, which measures the age of the word. `D543` now has US-native evidence.* |
| **`D560`** | *`catalyst_calendar` reports **"(none in window / yfinance unavailable)"** for EARNINGS while the desk's own 09-06 run has `ORCL` and `ADBE` both printing **09-10 16:00 ET** inside the window. The empty block reads as absence and is unavailability (`D540`, US instance).* |

---

## ✅ EXIT CHECK — MACRO

- [x] **Catalysts injected**: `catalyst_calendar --days 10` (not the 5-day default, because `SCENARIOS.md` names dates to 09-18) ⇒ **4 binaries in window**: PPI **09-10** `[bls✓]`, CPI **09-11** `[bls~est]`, **FOMC+SEP 09-16** `[fed✓]`, undated Hormuz-reopening statement `[news👁]`. `CATALYST_WATCH.json` saved at the day-folder root. ⚠ **`D507` reproduces — no US market-holiday row for today.**
- [x] **Events read via `--body 2`, tail = 0**, head 30 + body 249 read line by line.
- [x] **`tail = 0` is NOT presented as the coverage claim** — `single_source` **365 count / 15 shown / 350 withheld**, `scored 0` because the classifier is Korean-only; `excluded_nonmarket` **0/0, structurally empty**; `subevents_recovered` **44**. Every null in this report cites those numbers.
- [x] **Denominator quoted after correction** — `excluded_not_news` = `{}` (empty in foreign scope), articles **1,720**, and **flagged as a partial holiday day**, with the settled comparison days re-pulled (09-05 **1,740** · 09-06 **1,521**).
- [x] **Trajectories read** (`thread --days 7 --scope foreign`): every proposition carries its thread tag+curve or states "no thread"; the per-day event denominators are printed and the FADING tags are corrected against them (B-5). `P139`'s thread is re-read and its FADING tag is **not supported**.
- [x] **Every "nothing happened" claim carries its denominator** (B-6 burst null is explicitly bound to a 1,720 partial-day denominator and 350 unread single-source clusters).
- [x] **No bucket's count is trusted from a quoted multi-word term** — all 18 terms were run in **both** conventions and both columns are printed; the disagreement reaches **5.9×**.
- [x] **Both halves of every headline print cited** — `bond selloff` 5.93× is quoted **with its base of 247**; the crack's 95.6th-percentile level is quoted **with its 6.0th-percentile rate**; `hy_oas`'s 2.0th-percentile level is quoted **with its mid-pack change**.
- [x] **Every relative-performance number names its benchmark inline** (§E: equal-weight `us_top300` constituents, excess vs `SPY`). **No statistical result carried across markets** — the three KR retractions `R136`–`R138` were read and not used (`W1`).
- [x] **Credit axis read and cited**: `hy_oas` **2.65 = 2.0th pctile** + `nfci` **−0.558 = 8.9th** (10 days stale, stated). §B-2 labels the hike narrative **narrative-only** on the credit leg for exactly this reason.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.42 (94.0th) vs 2.35 (66.7th), with the conclusion that the move is real-rate, not inflation.
- [x] **Linter run on this stage's own output** — `report_lint.py` on this file: **0 findings** across C1/C2/S6/D6. ⚠ Form only; a clean run is not a correct report.
- [x] **Transmission matrix produced — all 11 sectors, one line each.**
- [x] **Self-backtest appended** (§F) with the 4 new verdicts and one **retraction of this desk's own number** (`R139`); new terms folded back: **none promoted**, with the denominator reason stated (B-6).

---

> P4 — no sizing, no buy/sell language. Propositions are falsifiable claims with pre-registered
> thresholds and anti-signals, not recommendations.


---

# §5 · DRIFT ADDENDUM — appended post-run by Stage 11 / L1·DRIFT (append-only; nothing above is rewritten)

> `drift_watch.py --report llm_outputs/2026-09-07/industry_US/MACRO_REPORT.md`, run **2026-09-07 23:25 KST**.
> Report completion baseline **2026-09-07T22:52** ⇒ monitored window **+0.6h**.

## D-0 · ⚠ The instrument fired early, so its null results carry little weight

`D282` reproduces for a **9th** time: DRIFT fired at **+0.6h** against its own **3–6h** specification.
⇒ **anything this pass did NOT find is weak evidence of absence**, and this addendum says so before
reporting anything it did find.

## D-1 · Four burst candidates, all four body-read, three are term artifacts

| term | post-completion count | vs baseline | body read | verdict |
|---|--:|--:|---|---|
| `rate cut` | 4 | **9.3×** | **The same article three times** — *"How Elastic Stock Bounced 48.3% Higher Last Month"*. The term matches on a phrase inside an equity-performance piece | ⚪ **artifact** (`D519`) |
| `ceasefire` | 3 | **7.0×** | Gaza/Yemen humanitarian items (*"Israeli attacks on Gaza kill five Palestinians"* · *"Yemen jab shortages"* · *"Nicaragua takes Germany to the ICJ"*) — no truce state changed | ⚪ **artifact** |
| `invasion` | 3 | 3.6× | The Iraq item below, plus *"Cold Plasma Market worth $3.03 billion by 2031"* (a press release) and a Societe Generale gold note | ⚪ **artifact**, except the Iraq leg |
| **`blockade`** | 4 | **6.5×** | ★ **one real item** — see D-2 | 🚨 **MATERIAL** |

Non-burst activity recorded for completeness: `rate hike` **11** · `Strait of Hormuz` **3** ·
`emergency meeting` 1 · `downgrade` 1 · `default` 1. ⚠ **`rate hike` at 11 mentions is the run's
largest post-completion count and it did NOT trip the burst threshold** — consistent with `P142`'s
object being live and already priced into the day's flow rather than newly igniting.

## D-2 · 🚨 The one material item: a **dated** escalation-risk event on the desk's only OW sector, 23 days out and in no register

`[news — aljazeera, 2026-09-07, body read in full]`:

> *"The United States-led international military coalition will conclude its mission in Iraq by the
> end of this month, the country's armed forces have confirmed… **September 30 is the date** for the
> end of the mission of the international coalition forces in Iraq."*
> *"Under a 2024 agreement between Baghdad and Washington, **the withdrawal includes the removal of
> US air defence systems stationed in Erbil**… **These platforms have been critical to the
> interception of Iranian ballistic missiles and drones targeting the region amid the US-Israel war
> on Iran.**"*
> *"**October 1 will mark a new day in the trajectory of the Iraqi state, as Iraq will be free of any
> foreign military presence**," the prime minister's office said.*

**Why this matters to this report and not to a general reader:**
1. **It is dated (2026-09-30) and it is structural** — the class `catalyst_calendar`'s STRUCTURAL
   block exists for and which has been **empty for every run this desk has logged** (`D510`).
2. **It removes an air-defence capability in a live shooting conflict** whose oil leg is this desk's
   **only OW sector**. §B-3 of this report records US strikes on Iranian tankers, an Iranian
   restricted zone outside Hormuz, and QatarEnergy's force majeure extended into November.
3. **No registered row contains it.** `P126` (09-09) · `P139` (09-14) · `P140` (09-11) all settle
   **before** it; `S37`/`S40`/`S48`/`S122` settle **on** 09-30 but none is scoped to it.
4. ⚠ **The counter-evidence is in the same body and is quoted rather than dropped** (`C2`): a
   University of Baghdad political scientist calls the withdrawal *"largely a formality… mostly
   symbolic, considering that the Americans have ended their military presence in many
   headquarters."* ⇒ **the event's magnitude is contested by the source that reports it.**

## D-3 · What this addendum does and does not change

- ❌ **It changes NO verdict, NO proposition threshold and NO sector wind above.** The event is
  **23 days out**, its magnitude is contested inside its own source, and this stage's job is to stop
  the report lying overnight — not to re-run it (`D242`).
- ✅ **It registers the gap**: a dated, structural, OW-sector-relevant catalyst that **the desk's
  calendar cannot see and no bracket owns**. Filed as **`D567`** — *the STRUCTURAL calendar's
  emptiness is not a reporting gap, it is a coverage gap: this run found a 09-30 event in a DRIFT
  burst that a 10-day catalyst pull three hours earlier could not have surfaced.*
- ✅ **It is handed forward by name**: the **2026-09-08 run** inherits it as a bracket candidate, on a
  settled tape and with the 09-11 COT available — the same run that already owes the FOMC bracket
  (`D564`). ⚠ **Registering it now would put its `D93` on the same frozen distribution the last three
  runs used** (`D503`), which is exactly why it is handed forward rather than armed here.
- ⚠ **And per D-0, the three "artifact" verdicts above are weak**: the window was **0.6h**, not 3–6h.
  A second pass at the correct offset is not scheduled by this protocol, and that is stated rather
  than assumed away.

## ✅ EXIT CHECK — DRIFT

- [x] **`drift_watch` run** against this report's own path; baseline and offset both printed.
- [x] **Every 🚨 item body-read, not counted** — four candidates, four bodies opened; three resolved as term artifacts with the matching article named, one resolved as material.
- [x] **§5 ADDENDUM appended, append-only** — nothing above this line is rewritten, and the addendum states explicitly that it changes no verdict.
- [x] **`D282` reproduction recorded (9th)** with its consequence for the null results, before the findings rather than after.
