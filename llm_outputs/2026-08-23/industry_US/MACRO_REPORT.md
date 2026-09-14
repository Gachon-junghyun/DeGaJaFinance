# MACRO_REPORT — industry_US · 2026-08-23 (Sun) · Stage 3 / L1·MACRO

> Run clock **KST 22:2x–23:0x = ET 09:2x–10:0x, SUNDAY — US cash CLOSED all weekend.**
> Terminal settled bar **2026-08-21 (Friday)**. **`n_new_sessions_since_prior_run = 0`.**
> Instrument rights: `llm_outputs/2026-08-23/preflight/PREFLIGHT_US.md` (**PASS 3 / FAIL 5**).
> All news calls `--scope foreign`, all made **outside a sweep window** (the sweep ran 22:09–22:13
> and every news figure below was pulled after 22:16).

---

## ★★★ The one thing this report exists to say today

**The desk's own regime call arrived as a price, on a weekend, in someone else's income statement.**

The spine has carried, `[inferred]`, for weeks: *memory is a price-cycle industry in rate-of-change
deceleration **while its level stays tight***. The "level stays tight" half has never had a
`[measured]` corroboration from the **buy** side of the chain. It has one now, and it is four days old:

> **`yahoo_finance`, 2026-08-22 — "Nvidia customers face over 15% server price hikes *as memory costs
> soar*"** · the same Bloomberg-sourced story carried by **8 outlets** (`fortune` · `scmp` · `cnbc` ·
> `cna` ×2 · `straitstimes` · `yahoo_finance` · `investing_en` · `google_en`/Reuters), the **most recent
> dated Sun 2026-08-23** — i.e. it is still spreading as this report is written. `[news, 8 outlets]`

**`M818`.** Two facts make this more than a headline:

1. **The mechanism is named in the title, and it is COST, not demand.** *"as memory costs soar."* A
   >15% price increase notified to customers is normally read as pricing power. **This one is
   explicitly a pass-through.** The distinction is the whole of `L2` (the peak-margin lens): a
   demand-led increase widens the margin; a cost-led one **defends** it.
2. **It is a chain event, not a name event.** `tomshardware`, **2026-08-19**: *"Samsung raises advanced
   foundry prices by up to **15%** as AI demand fills its 4nm lines."* **Two ~15% price increases at
   two different layers of the same chain inside four days** — foundry and accelerator. One is a
   supplier decision; two is a cost curve.

★★★ **And the timing is the part a Sunday desk can uniquely deliver.** `NVDA` reports **2026-08-26
(D-3)**. There is no tape to price this in — Friday closed before the story ran, and Monday is the
first session that can react. **This desk has no new price information today (§0) and it has a new
fact.** The two are not the same thing, and a run that only reads the tape would have found nothing.

⚠ **What this does NOT say.** It does not say `NVDA` beats or misses; it does not say the margin
falls. It says the **question at the print has changed shape**: not *"how big is demand"* but
*"how much of a >15% input-cost increase is being absorbed and how much is being passed on."*
That question is registered both ways as **`P90`** (§D) and is falsifiable at the 08-26 print.

---

## §0 · What this report may not claim, stated before the numbers

`PREFLIGHT_US.md` **PASS 3 / FAIL 5**, binding:

- 🚫 **No sentence of the form "since our last run, X moved."** Zero new sessions. **All 299
  `flow_score`s, all 299 tags and all 11 sector `wflow` values are identical to the 08-22 file.**
  Every price statistic below is the **2026-08-21 settle**, i.e. the same settle the prior report
  used, and is labelled as such rather than re-presented as fresh.
- 🚫 The sweep's **news-velocity axis** (`vel_coverage` = **0.0**, exactly zero) · any *"it went
  quiet"* claim from sweep silence (falsified **40/40** today, **360/360** cumulative).
- 🚫 The **Consumer Staples `wflow` sign** — `WMT` at **28.9%** flips it (−0.013 → **+0.116** ex-`WMT`).
- 🚫 Cap-weighted (`wflow`) statements as *current* — the universe's weights are **39 days** old.
- 🚫 Any flow/RS/OBV/short call on **`EA`** — unmeasured, not quiet (11th run).
- 🚫 **Any breadth number from a partial-coverage sweep, in either direction** (`R96`, new today).
- ✅ **Granted:** the 08-21 settled frame · `eqflow` for all 11 sectors · `wflow` signs for the ten
  non-flippers · today's tag layer as **3-axis unanimity** (all 299 velocities null ⇒ provably
  velocity-free) · FRED · COT · FINRA · **direct news calls outside a sweep window** (today 43/43,
  plus every query in §B).

---

## §A · Primary indicators — `[FRED]`, with percentiles and both halves

### A-1 · The shape: the policy rate at its yearly LOW, the long end at its yearly HIGH

All daily Treasury series `[FRED]` end **2026-08-20** — the **fifth** consecutive replication of
`D309` (FRED daily series do not publish on weekends; a Friday-dated FRED observable cannot be read by
a weekend desk). **08-20 values are not substituted for 08-21 anywhere below** — they are labelled
08-20 and used as 08-20.

| Series | Last | Date | 365d %ile | 365d range | 20-obs Δ | 60-obs Δ |
|---|---:|---|---:|---|---:|---:|
| `DFF` fed funds | **3.63** | 08-20 | **9.1** | 3.62 – 4.33 | 0.00 | — |
| `DGS2` | **4.19** | 08-20 | 88.7 | 3.38 – 4.37 | **−0.18** | +0.18 |
| `DGS10` | **4.69** | 08-20 | **96.0** | 3.97 – 4.75 | −0.02 | +0.19 |
| `DGS30` | **5.23** | 08-20 | **96.4** | 4.54 – 5.31 | **+0.06** | +0.20 |
| `DFII10` real 10y | **2.35** | 08-20 | 89.5 | 1.67 – 2.47 | −0.08 | **+0.25** |
| `T10YIE` breakeven | **2.34** | **08-21** | 59.0 | 2.18 – 2.50 | +0.08 | **−0.05** |

★ **`M819` — the policy rate sits at the 9th percentile of its own year while the 30y sits at the
96th.** That is not a curve *shape* statement, it is a **level** statement, and it is the cleanest
one-line summary of this regime: **the front end has been cut to the bottom of its range and the long
end has not followed.**

**Curve spreads, and they say something the levels do not:**

| Spread | Today (08-20) | 365d %ile | 365d median | 365d range | 20-obs Δ |
|---|---:|---:|---:|---|---:|
| `30y−10y` | **0.54** | **22.6** | 0.59 | 0.44 – 0.69 | **+0.08** |
| `10y−2y` | **0.50** | 30.2 | 0.53 | 0.27 – 0.74 | **+0.16** |
| `30y−2y` | **1.04** | — | — | — | **+0.24** |

★★ **`M820` — the 24bp steepening the prior run recorded (`M798`) decomposes almost entirely into a
FRONT-END RALLY, not a long-end selloff.** Over 20 observations `DGS2` fell **18bp** while `DGS30`
rose **6bp**. The steepener is three-quarters a 2-year move.
⚠ **This is stated as a decomposition, not as a revival of `P65`.** `R90` retracted `P65`'s
bull-steepener framing on a MISS of both frozen legs, and **both legs still fail today**: `30y−10y`
**0.54 < 0.58** and `DGS2` **4.19 > 4.15**. The direction `P65` anticipated is visible in the 2-year
and **has not reached the thresholds `P65` froze**. Recording the decomposition is not re-arguing the
retracted claim; asserting `P65` was right would be, and this report does not.

### A-2 · Real versus breakeven — the long-end move is REAL, and the 60-day window makes it unambiguous

| Horizon | `DFII10` real | `T10YIE` breakeven | `DGS10` nominal |
|---|---:|---:|---:|
| **60-obs Δ** | **+0.25** | **−0.05** | +0.19 |
| 20-obs Δ | −0.08 | +0.08 | −0.02 |
| Percentile | **89.5** | **59.0** | 96.0 |

★ **`M821` — over 60 observations the entire nominal rise is real yield, and the breakeven FELL.** The
market is not repricing inflation; it is repricing the real required return. ⚠ **Both halves quoted
(`C2`)**: at the 20-observation horizon the composition inverts (real −0.08, breakeven +0.08), so the
statement is **horizon-dependent and is labelled with its horizon rather than asserted flat.**

### A-3 · Inflation — the wedge, in both halves, **and a data hole that would have overstated it**

| Series | YoY (**date-matched**) | prior month YoY | MoM | MoM annualised | **3m annualised** |
|---|---:|---:|---:|---:|---:|
| Headline CPI (Jul) | **+3.304%** | +3.464% | +0.074% | +0.89% | **+0.49%** |
| Core CPI (Jul) | **+2.467%** | +2.566% | +0.215% | +2.62% | **+1.64%** |
| M2 (Jun) | +5.526% | +5.584% | +0.432% | +5.31% | +8.72% |
| Unemployment (Jul) | **−0.2pp** (4.3 → 4.1) | — | **−0.1pp** | — | — |

★ **`M822` — the wedge is entirely in HEADLINE, and it is enormous.** Headline runs **+3.30% YoY**
against **+0.49% 3-month annualised** — a **2.8pp** gap. Core runs **+2.47% YoY** against **+1.64%
3m-annualised** — a **0.8pp** gap. **The disinflation is not a core story.** A Fed chair debuting at
Jackson Hole on 08-27 can quote either number and be telling the truth.

🚨 **`M823` — an instrument defect this run walked into and caught, recorded rather than edited away
(`D48`).** This report's first pass computed YoY **positionally** (`obs[-13]`) and got **+3.54%
headline / +2.79% core** — **0.24pp and 0.32pp too high**. The cause: **`CPIAUCSL` and `CPILFESL` are
MISSING the 2025-10-01 observation** (the series jumps 2025-09-01 → 2025-11-01), so the thirteenth
element back is **August 2025, not July 2025**. The error was caught only because the prior run's
report carried +3.30%/+2.47% and the two disagreed.
⇒ **A positional YoY on any FRED monthly series is unsafe, and this one is unsafe in the direction
that makes inflation look worse.** Every figure in the table above is **date-matched**. Registered as
a dig in §F. ⚠ **`UNRATE` carries the same 2025-10 hole**; `M2` does not.

### A-4 · Credit and conditions — the divergence is still the finding, and it is not a stress signal

| Series | Last | Date | 365d %ile | 365d range | 20-obs Δ |
|---|---:|---|---:|---|---:|
| `HY OAS` | **2.75** | 08-20 | **23.3** | 2.63 – 3.46 | −0.02 |
| `IG OAS` | **0.82** | 08-20 | **77.9** | 0.73 – 0.94 | +0.03 |
| `NFCI` | **−0.559** | 08-14 | **7.8** (of 51 weekly obs) | −0.571 – −0.460 | — |
| `VIX` | **16.01** | 08-20 | 25.0 | 13.47 – 31.05 | **−2.69** |

★ **`M824` — IG at the 78th percentile with HY at the 23rd, and `NFCI` at the 8th (near its loosest of
the year).** Financial conditions are **easy** while investment-grade spread is **wide**. That
combination is not default risk — **default risk shows up in HY first, and HY is 12bp off its yearly
low.** It is duration and issuance, which is `P88`'s registered claim (settles 08-28).
⚠ **`C1`/`C3`**: the prior run quoted IG at the **85th** percentile and HY at the **25th** on a
different lookback. Today's numbers are 365-day percentiles computed here (n=262 for both OAS series).
**The lookback is stated because the percentile moves with it**; the *ordering* — IG high, HY low — is
what both readings agree on and is the citable half.

### A-5 · Positioning — `[COT, Tuesday 2026-08-18 close, published Friday]` ⇒ context, not a trigger

| Instrument | Net spec | Wk Δ | % OI | **1yr %ile** | Tool label |
|---|---:|---:|---:|---:|---|
| **Copper** | +79,748 | −640 | 28.3% | **100** | 🟢 crowded long |
| S&P 500 e-mini | **−10,560** | −21,840 | −0.5% | **84** | 🟢 "crowded long" ⚠ see below |
| USD Index | +19,079 | −2,330 | 39.8% | 76 | 🟡 |
| UST 2Y | −927,337 | +93,706 | −20.9% | 70 | 🟡 |
| Gold | +222,189 | +4,249 | 54.7% | 48 | 🟡 |
| WTI | +29,164 | +5,938 | 14.4% | 36 | 🟡 |
| Silver | +23,625 | −21 | 19.7% | 33 | 🟡 |
| Russell 2000 | −15,706 | −1,763 | −52.2% | **15** | 🔴 crowded short |
| **UST 10Y** | **−946,961** | −31,908 | −16.9% | **5** | 🔴 crowded short |
| Nasdaq-100 | −12,067 | **+30,838** | −3.8% | **4** | 🔴 crowded short |
| **Nat Gas** | −203,503 | −6,368 | −11.8% | **0** | 🔴 crowded short |

★ **`M825` — the speculative complex is short duration at the 5th percentile and short growth equity
at the 4th, while holding copper at the 100th.** Read as contrarian ammunition, not direction (`D6`):
a 10-year that is this heavily short is **fuel for a rally**, and copper at a 1-year maximum is fuel
for the reverse.

🚨 **`M826` — an instrument-label defect, first recorded here.** The S&P 500 e-mini row prints
**🟢 크라우디드-롱 (crowded long)** on a net-spec of **−10,560, which is net SHORT.** The percentile is
computed on the *level within its own 1-year range*, and if that range is entirely negative then the
84th percentile means **"least short of the year"**, not "long". **The label crosses zero and the
statistic does not.** This is the `D3` class (signed vs unsigned) and it matters because a reader
taking the label at face value would invert the position. ⇒ **Every COT citation in this run states
the net level and the percentile together; the label alone is not used.** Registered in §F.

---

## §B · Narrative — events, trajectories, and the weekend's distortion of both

### B-1 · Denominator, stated before any "quiet" claim (P4)

`brief --date 2026-08-22 --scope foreign --body 2`:
**1,684 articles → 280 events → 280 market events (0 non-market).**
- **Head (≥5 outlets): 27** · **Body (2–4 outlets): 253** · **Tail (2 outlets): 0**
- **`single_source`: 15 shown of 317** · **`excluded_nonmarket`: 0 of 0** · **`subevents` recovered: 80**

🚨 **`tail = 0` is NOT the coverage claim, and today the gap is bigger than the tail.** The module
states it outright: **302 of the 317 single-source items carry no classifier score at all**, because
the classifier is Korean-only and this is a foreign-scope day. ⇒ **~18% of the day's events are
unscored and only 15 were sampled.** Any "quiet" claim in this report is bounded by that, and none is
made without a denominator beside it.

⚠ **And the denominator itself is the weekend's:** per-day article counts across the thread window are
**08-17 756 · 08-18 824 · 08-19 825 · 08-20 824 · 08-21 766 · 08-22 280 · 08-23 142.**
**Saturday is 34% of a weekday and Sunday is 17%.**

### B-2 · What the head actually carried, 2026-08-22

| Cluster | Articles / outlets | Read |
|---|---|---|
| 🚨 **Canada retaliatory tariffs after US imposes 50% on some Canadian products** | **60 / 24** — the day's largest by a factor of three | The trade-war re-escalation the 08-22 `drift_watch` could not see (`D316`: the kill-switch term set contains no trade or tariff term). **It did not fade — it escalated to a named 50% rate and a named retaliation** |
| "The AI Spending Boom Is Outrunning Wall Street Estimates" | 11 / 7 | capex |
| **"Nvidia customers notified about AI-related price hikes above 15%"** | 10 / 7 (→ 8 outlets incl. 08-23) | **§0 headline** |
| "Amazon's Custom Chip Business Crossed a $25 Billion Run Rate" | 15 / 6 | merchant-silicon scale — ambiguous for `NVDA`, supportive for `AVGO` |
| "The U.S. Treasury's Bond Market Intervention Is a Nightmare…" + "The Real Cost Of $40 Trillion In Debt" | 7/6 + 5/5 | the `M797`/`M798` thread |
| "Iran says new US sanctions violate sovereignty of other states" | 8 / 6 | the oil axis |
| "Israel's Syria strike may have been bid to provoke Turkey" | 9 / 6 | geopolitical tail |
| Consumer-staples / real-estate / bond ETF selection cluster | 40 / 5 | retail allocation chatter, low information |

**Body-tier items that touch held names or registered propositions:**
`RTX`'s **$289 Billion Backlog, Explained** (8/4) · *"Marvell Targets a Huge AI Memory Bottleneck"* and
*"Google Is Getting Paid in Marvell Stock Warrants"* (6/4) · *"Data Centers Don't Just Need Power —
They Need Cooling"* (5/4) · *"GE Vernova's Backlog Is Bigger Than Some Countries' GDP"* (5/4) ·
*"Why Shell and the Other Oil Majors Aren't Price Gouging"* (9/4) · *"Oppenheimer has a blunt Nvidia
stock message ahead of earnings"* (5/4).

★ **`M827` — the single-source tier again carried a proposition-relevant primary.** `bloomberg`,
08-22, 1 outlet: **"Ukraine Drones Strike Samara Oil Refinery, E-Commerce Warehouse."** That is
`P66`'s Russian refinery-destruction leg, and it sat where the protocol says such things sit — in the
1-outlet tier, invisible to any outlet-count ranking. **`P66` continues to hold on fresh evidence.**

### B-3 · Trajectories — `thread --days 7 --scope foreign`, and every FADING label is suspect today

**4,417 daily events → 3,391 threads (536 multi-day, 49 live, 2,855 one-day, 92 new today).**

| Thread | Outlet curve 08-17 → 08-23 | Label | Read |
|---|---|---|---|
| **`NVDA` earnings** | 3 → 5 → 5 → 5 → 6 → 4 → **7** · 103 articles | **BUILDING** | ★ **peaks TODAY at 7 outlets, on a 142-article Sunday.** The print is 08-26. The story is accelerating into the print |
| Canada tariffs | 7 → 19 → 23 → 9 → 11 → **24** → 11 | *labelled* FADING | 🚨 **The label is a weekend artifact** — it went 11 → **24** → 11, and the final 11 is a Sunday with 17% of a weekday's volume |
| US debt > $40tn | 6 → 18 → 19 → 4 → 5 → 3 | *labelled* FADING | same caveat, weaker curve |
| Trump "economic warfare" on Iran-helpers | 18/11 → 18/12 → 6/6 → 23/17 → … → 2/2 | REIGNITED | the oil axis's political leg |

★★ **`M828` — a methodological correction that applies to every FADING/ENDED label in this run.** The
protocol warns that *"a holiday window-end inflates FADING; read the per-day denominator first."*
Today the window ends on **two** low-volume days: **08-22 at 34% and 08-23 at 17% of a weekday.**
⇒ **This report makes no "fading" or "ended" claim from the thread tool.** The 487 ENDED threads are
counted as a denominator, not read as an outcome.
⚠ **One ENDED thread is nonetheless a substantive input because its peak is inside the window, not at
its edge:** *"'Many' Fed officials think higher rates will be [needed]"* — **peak 18 outlets, 08-17 →
08-21**, i.e. the 08-19 FOMC minutes. **A hawkish minutes reading is the standing frame Warsh debuts
into on 08-27.** Likewise *"Walmart shares tumble as sales growth slows"* — **peak 19 outlets,
08-19 → 08-22** — which is a **named, dated cause** for `WMT`'s flow (−0.333, OBV 분산) rather than a
flow reading in search of a story.

### B-4 · Theme age — the sharpest instrument contrast of the run

All `theme-age … --scope foreign`, direct calls outside a sweep window:

| Theme | Verdict | Age | Velocity | Base articles |
|---|---|---:|---:|---:|
| **`Jackson Hole`** | 🟡 **ACCELERATING** | ≥90 | **10.67×** | 190 |
| **`Treasury buyback`** | 🟢 **FRESH** | **4 days** | — | 178 |
| `refinery` | ⚪ ECHO | ≥90 | 0.90× | 1,624 |
| `AI capex` | ⚪ ECHO | ≥90 | 0.68× | 1,149 |
| `Strait of Hormuz` | ⚪ ECHO | ≥90 | 0.79× | 8,041 |
| `tariff` | ⚪ ECHO | ≥90 | **1.11×** | **9,712** |
| `PCE inflation` | 🔴 FADING | ≥90 | **0.45×** | 391 |

★★★ **`M829` — the desk's news instrument reads `Jackson Hole` at 10.67×, the highest acceleration on
the board, while the desk's own `catalyst_calendar` carries ZERO rows for it.** `catalyst_calendar.py
--days 10`, run today, prints five binaries — `NVDA` 08-26 (D-3) · July PCE 08-28 (D-5) · `FRO` 08-28 ·
`AVGO` 09-02 · `S8` undated — **and nothing for 08-27 → 08-29.** `D18` reproduces for a third
consecutive run, and today it reproduces *against* a 10.67× reading from a sibling tool. **The event is
covered by `S112` (registered 08-22, settles 08-31); the calendar gap is a tool defect with a different
owner.**

🚨 **`M830` — `tariff` at 1.11× is a base-rate artifact, and it is the mirror image of `D316`.** A
60-article / **24-outlet** cluster — the largest single event of the day — registers as **ECHO** because
the term's 90-day base is **9,712 articles**. ⇒ **A velocity ratio is uninformative on a term whose base
is in the thousands**; the outlet-count cluster is the correct instrument there. **The desk therefore has
two independent ways to miss the same event**: `drift_watch`'s term set cannot see it (`D316`), and
`theme-age`'s ratio dilutes it (`M830`). Registered in §F.

★ **`Treasury buyback` is the board's only 🟢FRESH theme, at 4 days old with 178 articles.** `P85`'s KPI
is `theme-age Bessent`, which the prior run measured at 3.01×; the *operation* now has its own
freshly-born term. That is corroboration for `P85`'s framing, not a score.

⚠ **`PCE inflation` 🔴FADING at 0.45× with the print five days away** — an under-anticipated scheduled
binary. Recorded, not traded (P4).

### B-5 · Blind-spot pass — the term nobody would have thought to search

`burst --date 2026-08-22 --scope foreign`, ② "words that do not normally appear":

| Word | Articles | Share | Baseline appearance | Market % | Outlets |
|---|---:|---:|---:|---:|---:|
| **`NOTIFIED`** | 7 | 0.416% | **3%** | **100%** | **6** |
| `HOLE` (→ Jackson Hole) | 9 | 0.534% | 30% | 56% | 5 |
| `TEPPER` | 7 | 0.416% | 33% | 43% | 3 |
| `TJX` | 4 | 0.237% | 37% | 100% | 3 |

★ **`NOTIFIED` — 3% baseline, 100% market relevance, 6 outlets — is the run's headline story, and no
fixed term set contains it.** ⇒ **The blind-spot pass earned its keep today**, and this is recorded as
evidence for keeping it rather than as a general claim about the method. `JACKSON`/`HOLE` also surfaced
here at **z 5.5**, independently of the theme-age read.

---

## §C · Self-backtest — the exhaustive table, because "nothing was due" and "nobody checked" look alike

**Every registered proposition with a settle date, checked against 2026-08-23:**

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `P65` · `P66` · `P69` · `P70` · `P75` | **ALL settled by the 08-22 run** — `P65` MISS both legs (already `R90`) · `P66` HOLDS · `P69` FIRED-A · `P70` MISS on its control leg · `P75` CLOSED as unscoreable-by-construction |
| **2026-08-22** | **none** | — |
| **2026-08-23 (today)** | **none** | — |
| 2026-08-25 | `P79` | armed |
| 2026-08-26 | `P77` · `P78` · `P80` | armed (`NVDA` print) |
| 2026-08-27 | `P83` | armed (Jackson Hole opens) |
| 2026-08-28 | `P67` · `P81` · **`P85` · `P86` · `P87` · `P88` · `P89`** | armed (July PCE) |
| 2026-09-03 | `P84` | armed |

⇒ **0 propositions due today, and the table is the evidence the question was asked.**
**Hit-rate ledger, unchanged from the 08-22 run** (no new settlements): the running record is carried,
not recomputed, because recomputing an unchanged ledger under a new date is the same manufacturing
error §0 forbids on prices.

★ **One substantive pre-settle observation, offered as a reading and not as a score.** `P66`'s Russian
supply-destruction leg received **fresh corroboration inside the window** (`M827`, `bloomberg` 08-22,
Samara refinery). `P89`'s anti-signal (*a US refinery outage or PADD3 hurricane landfall*) has **still
not fired** — today's `refinery` theme reads ⚪ECHO 0.90× on 1,624 articles with no US-outage cluster
in the 08-22 head or body tiers. **Both are pre-settle context for 08-28, not verdicts.**

---

## §D · Propositions registered this run — both-sided, anti-signals base-rate-checked

> ⚠ **`D300-KR` applied to every clause.** Each anti-signal is keyed to a **magnitude** or to a
> **specific dated publication**, never to "an event occurring" in an 8-day US window.
> ⚠ **`D311` applied**: every date below comes from a body or an official schedule, not a headline.
> ⚠ **ID grep at write time**: `P90` `P91` `P92` returned **0 hits** across `handoff/*.md`,
> `llm_outputs/**`, `REPORT/**`. (`P90` matches only inside binary `.pkl` price caches — not IDs.)

### `P90` — ★★★ Is the >15% price increase a MARGIN EXPANSION or a COST PASS-THROUGH?
- **Claim.** `M818`: `NVDA` notified customers of **>15%** server price increases, and the reporting
  names the cause as **memory costs** (`yahoo_finance` 08-22, title verbatim). The desk's regime call
  says memory's **level** is tight while its **rate** decelerates — which predicts pass-through, not
  pricing power. `[news, 8 outlets]` + `[inferred]` chain link.
- **A (pass-through — the cost curve is binding).** At the **2026-08-26** print: `NVDA` guides
  **next-quarter gross margin ≤ its reported FQ-just-ended gross margin** (i.e. flat-to-down), **AND**
  the reported quarter's gross margin does not exceed the prior quarter's by more than **50bp**.
- **B (pricing power — demand is binding).** Guided next-quarter gross margin **≥ +100bp** above the
  reported quarter.
- **C** between — **disclosed as the favourite** (`L3`): a >15% list-price move announced days before a
  print most often lands as a partial pass-through.
- **Anti-signal (VOID).** **`NVDA` does not report on 2026-08-26** (delay/restatement), **or** the
  company explicitly declines to guide gross margin. ⚠ **Base rate: low** — a scheduled quarterly
  release with a fixed date and a company that has guided GM every quarter in the desk's series.
  **Keyed to a publication failure, not to an event occurring.**
- **Information grade.** **High.** Both A and B are reachable from the same document, and the two
  branches carry opposite implications for `AVGO` (09-02) and for the memory names.
- **KPI:** `theme-age "memory prices"` and whether the 8-outlet cluster survives Monday's session.

### `P91` — ★★ Does the front-end rally, or the long end, own the next leg of the curve?
- **Claim.** `M820`: over 20 observations `DGS2` **−0.18** vs `DGS30` **+0.06** with `DFF` unchanged —
  the steepening is three-quarters a 2-year move. `[FRED 08-20]`
- **A (front end owns it — the market is pricing cuts, not term premium).** At the first `[FRED]`
  close covering **2026-08-28**: `DGS2` ≤ **4.08** **AND** `DGS30` ≤ **5.28**.
- **B (long end owns it — term premium/issuance).** `DGS30` ≥ **5.36** (above its 248-obs max of 5.31)
  **OR** `30y−2y` ≥ **1.18**.
- **C** between — the favourite.
- **Anti-signal (VOID).** An **inter-meeting Fed action or an unscheduled FOMC statement** inside
  08-24 → 08-28. ⚠ **Base rate: very low** — none in the desk's series; keyed to a specific dated
  action, not to commentary. ⚠ **Jackson Hole speech content is deliberately NOT a void condition** —
  the speech is the mechanism the row is testing, and voiding on it would make the row unscoreable.
- ⚠ **`D309` applied at registration**: the settle is *the first `[FRED]` close covering 08-28*, which
  a weekend desk cannot read. **This row is explicitly assigned to the first BUSINESS-DAY run on or
  after 2026-08-31.**
- **Why registered:** it separates the two readings that `A-1` cannot separate, without reviving
  `P65`'s retracted framing (its thresholds are new, and `P65`'s frozen legs are not reused).

### `P92` — ★ Is the trade-war re-escalation a macro object or a headline?
- **Claim.** The 08-22 head carried **60 articles / 24 outlets** on US 50% tariffs and Canadian
  retaliation — the day's largest cluster by 3× — while `theme-age tariff` reads **⚪ECHO 1.11×** on a
  **9,712-article** base (`M830`). **Two of the desk's instruments disagree about whether this
  happened**, and one of them (`drift_watch`) cannot see it at all (`D316`).
- **A (macro object — it prices).** Over **2026-08-21 close → 2026-08-28 close**, `XLI` 5-session
  excess vs **`SPY`** ≤ **−2.50pp** (its 08-21 reading was **−1.988**) **OR** `XLB` excess ≤ **−1.00pp**
  (08-21: **+3.271**).
- **B (headline — it does not price).** **Both** `XLI` ≥ **−0.50pp** and `XLB` ≥ **+2.00pp** over the
  same window.
- **C** between — the favourite (`L3`, disclosed).
- **Anti-signal (VOID).** A **US–Canada agreement announced with a named effective date** inside the
  window ⇒ the object is resolved, not measured. ⚠ **Base rate checked**: the 08-22 cluster itself
  carries *"Canada says more work needed as US trade deal deadline looms"* (2 outlets), so a deal is
  live but not scheduled — **keyed to a named effective date, not to "talks occur"**, which is what
  keeps it from being near-certain.
- **Information grade.** **Medium-low, and disclosed as such.** Both A and B require a sector to move
  ~2.5pp on one axis in five sessions, and C is the heavy favourite. **Registered anyway** because the
  desk currently has **no** row keyed to the trade axis at all, and an axis with zero coverage cannot
  produce a surprise it can learn from.

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each

> **This is ROTATION's input and the deliverable of this stage. It sets wind direction only.**
> `exc5` / `exc20` / `exc60` = excess return vs **`SPY`** (named inline, `C1`), settled closes ending
> **2026-08-21**; `SPY` itself **5d −1.368% · 20d +3.626% · 60d +2.033%**, last **765.72**.
> ⚠ **These are the SAME windows the 08-22 report used** — there has been no session since. They are
> re-stated as inheritance, not as movement.
> `eqflow` / breadth from `SECTOR_FLOW_US.json` (`asof` 2026-08-21, `vel_coverage` 0.0).
> ⚠ `wflow` inherits **39-day-old cap weights** and decides **no** line below.
> ⚠ Breadth is read as **3-axis unanimity**, never as news-confirmed, and is **never compared to a
> pre-08-22 run's breadth** (`R96`).

| # | Sector | Wind | Evidence — both axes, and what disagrees | Driving proposition |
|---|---|---|---|---|
| 1 | **Health Care** | **OW** | `exc5` **+5.700** (rank 1) · `exc20` +3.787 · `exc60` **+15.327** (rank 1) · `eqflow` **+0.229** (rank 1) · 🟢1 : 🔴2 · breadth +0.030 · no flipper. **Leader on both the price axis and the flow axis, at both horizons.** ⚠ `LLY` is 19.4% of the cap weight but `wflow` +0.196 vs ex-top1 **+0.205** — the sector does **not** depend on it | none directly — the standing OW |
| 2 | **Energy** | **OW** | `exc5` **+4.162** (rank 2) · `exc60` +9.635 · `eqflow` **+0.102** (rank 2) · breadth +0.000 · 🟢0 : 🔴2 · no flipper. **`P66` corroborated inside the window** (`M827`, Samara refinery, 1 outlet). ⚠ `delta −0.093` is the second-most negative on the board — **price leads, flow does not confirm** | `P89` (settles 08-28) · `P66` |
| 3 | **Materials** | **OW−** | `exc5` **+3.271** (rank 3) · `exc20` +0.822 · `exc60` +2.578 · `eqflow` +0.046 · breadth **+0.080** (rank 1) · 🟢1 : 🔴1. 🚨 **Copper COT at the 100th percentile** (`M825`) and **`NEM` fired `S89`-B on exhaustion geometry** (`M779`: 246% of its rs60 in the last 20 sessions). **Price yes, positioning maximally crowded** | `P87` (gold, settles 08-28) · `P92` (`XLB` leg) |
| 4 | **Consumer Discretionary** | **N+** | `exc5` +1.216 · `exc20` **+4.244** (rank 1) · `exc60` **−4.938** (rank 10) · `eqflow` +0.103 · breadth **0.000** · 🟢0 : 🔴5. **The 20-day leader and the 60-day laggard — a reversal, and breadth is empty underneath it** | `S91` VOIDed; no live row |
| 5 | **Consumer Staples** | **N** *(no verdict on `wflow`)* | `exc5` +1.252 · `exc20` −1.415 · `eqflow` **+0.048** · breadth +0.050 · 🟢1 : 🔴2. 🚫 **`wflow` −0.013 is UNUSABLE — `WMT` at 28.9% flips the sign to +0.116 ex-`WMT`** (`R82`, G3). ★ **`WMT`'s weakness has a named dated cause**: *"Walmart shares tumble as sales growth slows"*, **peak 19 outlets 08-19→08-22**. ⚠ **`WMT` is also one of the six `R96` tag-contaminated names** — sign-owner and tag-mover at once. **FINRA: `WMT` 5v5 +12.1▲, the largest short-pressure build on the carried set** | `R82` blocks a verdict |
| 6 | **Financials** | **N** | `exc5` +0.199 · `exc20` −1.548 · `exc60` **+9.752** (rank 2) · `eqflow` **−0.034** · breadth +0.020 · 🟢1 : 🔴9. ★ **`M805` stands: six of six large banks share one shape** (`obv_norm` ≥0 ∧ rs20 <0 ∧ rs60 >0) and **five of nine reds are insurers**. ⚠ **Two of the six `R96` contaminated names are here** (`MS`, `JPM`) — a partial-coverage run would have printed them 🔴 | `P88` (credit, settles 08-28) |
| 7 | **Communication Services** | **N−** | `exc5` −0.004 · `exc20` +1.172 · `exc60` **−6.214** (rank 11) · `eqflow` +0.095 · breadth 0.000 · 🟢0 : 🔴1 (n=12). 🚨 **`D297` unfixed**: `GOOG` is a second 38.3% row, so the Alphabet complex is **76.6%** of the sector while `top1_w` reports 38.3%. **The flipper guard is structurally blind here** | none live |
| 8 | **Real Estate** | **UW** | `exc5` +0.948 · `exc20` **−5.519** (rank 10) · `eqflow` **−0.446** · breadth 0.000 · 🟢0 : 🔴6. **`S90` settled FIRED-A** — the 08-21 promotion was late, and the desk recorded that against itself. The digital-infrastructure node (`DLR`/`EQIX`/`IRM`) moved as a node, not a name | `S90` settled A |
| 9 | **Industrials** | **UW** | `exc5` **−1.988** · `exc20` **−4.945** · `exc60` +1.380 · `eqflow` **−0.231** · breadth 0.000 · 🟢0 : **🔴15**. **`M803`: `M704` ex-`LHX` is −4.162 vs −4.775 ⇒ succession explains 13%, every other prime explains 87%.** ⚠ `RTX` FINRA **z −2.15 covering INTO a −0.304 delta** — the second instance of the `M804` shape (shorts covering into decline) | `P92` (`XLI` leg) |
| 10 | **Information Technology** | **UW−** | `exc5` **−2.158** (rank 11) · `exc20` +0.599 · `exc60` −2.641 · `eqflow` **−0.102** · breadth +0.040 · 🟢2 : **🔴15**. ★★ **And this is the line `P90` puts under review**: the sector is the week's worst on price while its epicenter is announcing a **>15% price increase** three days before its print. ⚠ **`SECTOR_DEEP_SEMI.md` is 39 days old** and 4 of 11 book names live here | **`P90`** (settles 08-26) · `S113` (09-01) |
| 11 | **Utilities** | **UW** | `exc5` **−2.108** · `exc20` **−11.230** (rank 11, by 5.7pp) · `exc60` −7.284 · `eqflow` **−0.621** · breadth 0.000 · 🟢0 : **🔴13 of 15**. ★★ **`M802`'s open contradiction stands**: `NVDA` guarantees up to **$105bn** of OpenAI's Ohio leases while **every measurable power-layer name is 🔴**. The capital is going to power and the power tape is the worst on the board | `M802` unresolved |

**Wind summary — OW: Health Care, Energy · OW−: Materials · N+: Consumer Discretionary ·
N: Consumer Staples (verdict blocked), Financials · N−: Communication Services ·
UW−: Information Technology · UW: Real Estate, Industrials, Utilities.**

⚠ **Unchanged from the 08-22 matrix, because the inputs are unchanged.** The one line that has moved in
*meaning* rather than in *number* is **Information Technology**, and it moved on `M818` — a news fact,
not a price.

---

## §F · Instrument observations from this stage (dig candidates for `RESEARCH.md` Part C at run end)

| Candidate | What was measured |
|---|---|
| **A FRED monthly series has a hole, and positional YoY silently overstates inflation** | `CPIAUCSL`/`CPILFESL`/`UNRATE` are **missing 2025-10-01**. A positional `obs[-13]` YoY returns **+3.54% / +2.79%** where the date-matched values are **+3.30% / +2.47%** — **+0.24pp / +0.32pp too high, in the hawkish direction.** Caught only by disagreement with the prior run's number. **Positive-form remedy: match the date 12 months back; if that month is absent, state the gap and name the substitute base.** (`M823`) |
| **A COT label crosses zero while its statistic does not** | S&P 500 e-mini prints **🟢 crowded-long at net −10,560** because the 84th percentile is computed on a range that is entirely negative. **Positive-form remedy: print the net level beside the percentile, and suppress the long/short label when the 1-year range does not straddle zero.** (`M826`, `D3` class) |
| **A theme-age ratio is uninformative on a term with a four-figure base** | `tariff` reads **⚪ECHO 1.11×** on a 9,712-article base on the day its cluster ran **60 articles / 24 outlets** — the day's largest. Combined with `D316` (the drift term set has no trade term), **the desk has two independent ways to miss the same event.** **Positive-form remedy: report the outlet-count cluster beside the velocity ratio whenever the base exceeds ~2,000, and treat the ratio as unusable there.** (`M830`) |
| **Weekend window-ends make every FADING/ENDED label unreadable** | Per-day article counts **08-21 766 → 08-22 280 → 08-23 142** (34% and 17% of a weekday). The Canada thread reads FADING on a curve of **11 → 24 → 11**. **Positive-form remedy: `thread` should print the per-day denominator ratio beside each label and suppress FADING when the terminal day is below ~50% of the window median.** (`M828`) |

---

## §G · What this report may not say, restated at the end so it binds

1. **No claim of movement since the last run.** Zero sessions. Every price statistic here is the
   **2026-08-21 settle**, identical to the prior report's, and is stated as inheritance.
2. **No verdict on Consumer Staples from `wflow`** — `WMT` at 28.9% owns the sign (`R82`, G3).
3. **No breadth number compared to a pre-08-22 run**, and none taken from a partial-coverage sweep in
   either direction (`R96`).
4. **No cap-weighted claim treated as current** — the universe is 39 days stale.
5. **No "quiet" claim without its denominator**, and the denominator today is bounded by **302
   unscored single-source items** and a weekend article count at **17–34%** of a weekday's.
6. **No COT label used without its net level** (`M826`).
7. **No FADING/ENDED verdict from the thread tool this run** (`M828`).
8. **No inflation YoY quoted positionally** — all date-matched (`M823`).
9. `P90`–`P92` are **registered, not scored.** `P90` settles **08-26**, `P92` **08-28**, and `P91` is
   explicitly assigned to the first **business-day** run on or after **08-31** (`D309`).

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** — `catalyst_calendar.py --days 10` run (beyond the `--days 5` default,
      because `SCENARIOS_US.md` holds ARMED rows out to 09-03). **5 binaries**: `NVDA` 08-26 (D-3) ·
      July PCE 08-28 · `FRO` 08-28 · `AVGO` 09-02 · `S8` undated. **No binary ≤48h today** — the
      nearest is D-3, and this is the last run before that stops being true.
- [x] **Narrative read** — events (`brief --body 2`, **tail = 0**), trajectories (`thread --days 7`),
      theme-age on 7 buckets, blind-spot (`burst`). All `--scope foreign`, all outside sweep windows.
- [x] **`tail = 0` is NOT quoted as coverage.** `single_source` **15 shown / 317**, of which **302 are
      unscored** (Korean-only classifier on a foreign day) · `excluded_nonmarket` **0 / 0** ·
      `subevents` **80 recovered**. The coverage bound is stated in §B-1 and again in §G.
- [x] **Denominator quoted after non-news removal** — **1,684 articles → 280 events, 0 non-market.**
- [x] **Trajectories read; every proposition carries its thread's tag+curve or states "no thread"** —
      and **every FADING/ENDED label is explicitly refused this run** with the per-day denominators
      that make it unreadable (`M828`).
- [x] **Every "nothing happened" claim carries its denominator** (§B-1, §C, §G).
- [x] **No bucket's low hit-count trusted from a mis-passed CLI** — each theme-age term was passed as a
      single quoted argument and returned a non-zero base (190 … 9,712); the two FTS queries that
      failed did so **loudly** (`fts5: syntax error near "%"`) and were **not** read as zero.
- [x] **Both halves on every headline print** — CPI, core CPI, M2, unemployment all carry YoY **and**
      MoM **and** 3m-annualised, date-matched, with the 2025-10 hole disclosed.
- [x] **Every relative-performance number names its benchmark inline** (`SPY`, with its own return).
- [x] **Credit axis read and cited** — `HY OAS` 2.75 (23.3 %ile) · `IG OAS` 0.82 (77.9) · `NFCI`
      −0.559 (7.8). No credit-stress claim is made; the divergence is labelled duration/issuance.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.35 (89.5 %ile) vs 2.34 (59.0), with both horizons.
- [x] **Transmission matrix produced — all 11 sectors, one line each** (§E).
- [x] **Self-backtest** — exhaustive settle table; **0 propositions due**; hit-rate carried unchanged
      rather than recomputed on an unchanged ledger.
- [x] **New blind-spot terms folded back** — `NOTIFIED` promoted from the burst pass into `P90`'s KPI.
- [x] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-23/industry_US/MACRO_REPORT.md` → **0 findings** (rules C1, C2, S6, D6). ⚠ A clean lint is a form check, not a correctness check — it does not see `M823`, which was a content error caught by cross-run comparison, not by form.


---

# §5 ADDENDUM — appended by Stage 11 / L1·DRIFT, 2026-08-23

> **Append-only. Nothing above this line is edited.** The original call stays visible beside its
> correction — that asymmetry is what the self-backtest eats.

## §5-0 · `drift_watch` verdict, and its two standing defects

`scripts/drift_watch.py --report llm_outputs/2026-08-23/industry_US/MACRO_REPORT.md`:
**✅ no kill-switch burst.** Non-burst activity: `Strait of Hormuz` **2**.

⚠ **Two defects travel with that verdict and are logged, not waved through:**
1. **It ran at +0.6h against a 3–6h spec — 5th consecutive run at the wrong lag.**
2. **`D316` is unfixed**: the kill-switch term set contains **no trade or tariff term**, which is
   exactly why the 08-22 run's `drift_watch` returned "no burst" on that day's largest story
   (a 60-article / 24-outlet US–Canada escalation).
⇒ **A hand `brief --date 2026-08-23 --scope foreign --body 2` was run beside it.** Denominator:
**700 articles → 142 events → 142 market events (0 non-market)** — a Sunday at **17%** of a weekday's
volume. **Three items landed after the report's baseline. One of them corrects this run's own reading.**

## §5-1 · ★★★ A CORRECTION TO THIS RUN'S OWN `EVENT_ALPHA` CARD 2 — the "bad level" was the wrong level

**What the run wrote** (EVENT_ALPHA Card 2, unchanged above): *"their LEVELS are all negative …
⇒ **This is a rate-of-change inflection off a bad level, not accumulation.**"*

**What triggered the re-check**: today's head tier carried *"**Micron Stock Is Up 30% From Its Recent
Low.** Here's How Much…"* (**6 articles / 6 outlets**, 08-23) — an item that flatly contradicts
"bad level" as a price statement.

**Measured, settled closes through 2026-08-21 (`yfinance`, `auto_adjust=False`):**

| | last (08-21) | 90-day low | **off the low** | 90-day high | **from the high** |
|---|---:|---:|---:|---:|---:|
| **`MU`** | 966.78 | 448.42 (**2026-04-20**) | **+115.6%** | 1,213.56 | **−20.3%** |
| **`SNDK`** | 1,596.08 | 891.72 (2026-04-15) | **+79.0%** | 2,335.00 | **−31.6%** |
| **`LRCX`** | 314.00 | 248.75 (2026-04-29) | **+26.2%** | 433.33 | **−27.5%** |
| `NVDA` | 214.72 | 190.01 (2026-07-29) | +13.0% | 235.74 | −8.9% |

★★★ **The correction, stated plainly.** *"Bad level"* was true of the **relative-flow score**
(`MU` −0.278, `LRCX` −0.294) and **false of the price**. `MU` has **more than doubled off an April
low** and sits **20.3% below its own high**; `SNDK` is **+79.0% / −31.6%**. ⇒ **The memory complex is
not a base forming after a decline. It is a 20–32% drawdown inside a very large uptrend.**

**Why this matters rather than being a nicety:** those are two different objects with opposite
implications for `L2` (the peak-margin lens).
- The reading Card 2 implied — *inflection off a bad level* — invites "the cycle is turning up."
- The reading the price gives — *deep pullback from a high, after a 79–116% run* — is
  **EXTENDED-AND-IN-DRAWDOWN**, and `L2`'s peak-margin caution applies **more**, not less.

⚠ **What survives unchanged**: the one-session flow-delta ranking (**`SNDK` #7 · `LRCX` #10 ·
`MU` #16 · `ADI` #18 · `TER` #36 · `STX` #42 · `AVGO` #43 · `INTC` #45** of 299, universe median
**+0.011**) is arithmetic and is not affected. **Card 2's cell verdict (STORY-ONLY, not handed to
BET) is also unchanged** — if anything this correction supports it. **The four miss-ledger rows filed
for `MU`/`SNDK`/`LRCX`/`STX` stand, with their `--enters-if` conditions unaltered** (`D242` — a
condition is not re-written after the fact).
⚠ **And `S117` is unaffected**: it is a *relative* bracket (`MU` − `NVDA` on one session) and does not
depend on where either name sits in its own range.

## §5-2 · The trade-war object moved AWAY from its own anti-signal

Today's largest cluster: **"Canada's Carney refuses to take Trump's 'bait'"** (**13 articles /
11 outlets**), with the sub-event **"'No more!!!': Trump lashes out after US-Canada talks devolv[ed]"**
(2 outlets).

**`P92`'s registered anti-signal reads: *"a US–Canada agreement announced with a named effective
date"*.** Today's news says the talks **broke down**. ⇒ **The void condition moved further from
firing, not closer.** `P92` settles **2026-08-28** with its thresholds untouched (`XLI` ≤ −2.50pp
**or** `XLB` ≤ −1.00pp / both `XLI` ≥ −0.50pp and `XLB` ≥ +2.00pp).
★ **This is a pre-settle observation, not a score**, and it is recorded because a base-rate check made
at registration deserves a follow-up when the base rate visibly changes.

## §5-3 · A new item on the oil axis that no instrument in this run priced

Head tier, 08-23: **"Iran warns countries against joining US 'economic war'"** (6/5) and — the one
that is genuinely new — **"Small UK power plant shut down after cyberattack linked to I[ran]"**
(**5 articles / 5 outlets**).

⚠ **Stated at exactly the confidence it deserves**: this is a **headline-tier read, not a body read**,
and per `D311` no dated catalyst is registered from a headline. **What it changes: nothing yet.**
**What it flags: the energy-security channel has moved from "shipping-lane risk" to "infrastructure
attack", and the desk has no instrument pointed at that at all** — `theme-age "Strait of Hormuz"`
reads ⚪ECHO **0.79×** on 8,041 articles, which is the wrong term for this event, and `S8` (the
undated Hormuz binary) is unscoreable for a **22nd** run.
⇒ **Handed to the 08-24 run as a body-read obligation**, not resolved here.

## §5-4 · Two more items, logged for the next run rather than acted on

- **`BABA` announces a $10.2bn share placement** (7/6) — extends EVENT_ALPHA **Card 7**'s
  equity-**supply** thread beyond the private AI pipeline into listed China tech. Card 7's horizon is
  **2026-09-30**; this is corroboration, not a settle.
- **`MRVL` head-tier item: *"Forget Broadcom: Nvidia (NVDA) Is Still the Top Semiconduc[tor]…"*** (3/3,
  nested under the `NVDA` $6tn cluster) — the first item in the window arguing the **other side** of
  EVENT_ALPHA Card 3. **Recorded because it is the counter-case**, and `S116` is what settles it on
  **08-28**.

## §5-5 · What this ADDENDUM does NOT claim

- **It does not claim the report is stale.** `drift_watch` found no burst and the hand read found no
  regime flip. **One reading inside the report is corrected; none is reversed.**
- **It does not re-band, re-date or re-write any registered scenario** (`D242`). `P90`–`P92`,
  `S115`–`S117` settle exactly as registered.
- **It does not convert any headline into a dated catalyst** (`D311`).
