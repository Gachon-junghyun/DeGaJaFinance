# MACRO_REPORT — industry_US · 2026-08-16 (Sun) · Stage 3/11 (L1·MACRO)

> Wind direction only. No sizing, no buy/sell language (P4). `--market us` · news `--scope foreign`.
> Every relative-performance number names its benchmark inline (**C1**). Every print carries both its
> YoY and its sequential half (**C2**). Unknown columns are written `unknown`, not filled (**C3**).

---

## §0 · Instrument state — read FIRST, because it decides what this stage is allowed to do

`llm_outputs/2026-08-16/preflight/PREFLIGHT_US.md` — **PASS 3 / FAIL 5**. The binding table is
`HANDOVER.md §6`. The two constraints that bite hardest on this stage:

1. 🚫 **No Δ may be written as "today", "the latest session", or "now accelerating".** **Zero sessions
   settled** since the prior `industry_US` run.
2. 🚫 **No citation of the sweep's news-velocity axis** (coverage **16.7%**, survivor set monotone-nesting).
   Per-name velocity may be hand-probed **with its 7d/30d counts and probe clock time on the same line**.

### ★ The measurement that defines this run — THREE of the desk's four macro instruments are frozen, and it is not the same as being blind

| Axis | Last observation | vs the 08-15 run | Could it have moved? |
|---|---|---|---|
| **Equity tape** | 2026-08-14 close | **identical** — `SPY` 776.34, 11-sector table identical to 3dp, median `vol_surge` 0.649 | ❌ Sat + Sun |
| **`[FRED]` primaries** | **2026-08-13** (H.15) · 08-14 (T10YIE, RRP) | **identical, series by series** — `DGS10` 4.63 · `DGS2` 4.15 · `DFII10` 2.39 · `BAMLH0A0HYM2` 2.71 · `NFCI` −0.549 · `VIXCLS` 14.63 | ❌ publication lag (`D212`) + weekend |
| **CFTC COT** | **Tue 2026-08-11 close**, released 08-14 | **identical, instrument by instrument** | ❌ weekly, Friday release |
| ★ **News corpus** | **live** | **+1,855 new articles ingested this run** (`embed sync`, cursor `2026-08-16T21:44`) | ✅ **the only axis that moved** |

⇒ **This stage's budget goes to §D.** A proposition built on §A/§B/§C today is a proposition built on
the same bytes the last run already read. ⚠ **And the inverse is equally forbidden**: "the macro did
not move" is **false**. The macro *observation* did not move. Those are different statements, and the
distinction is exactly what `S1` (date-fold) exists to protect.

★ **One thing frozen data still permits: re-measuring the window.** `C1` says measure the baseline
yourself. §A below does that, and it **breaks a carried premise without a single new datapoint.**

---

## §A · Primaries — `[FRED]`, with both halves of every print

All values `[FRED]`. Percentiles are over the **138-observation** pull (≈ 2026-01-28 → 2026-08-13/14).

| Series | Latest | Date | Δ 1 obs | Δ 5 obs | Percentile of the pull |
|---|---|---|---|---|---|
| `DGS30` 30y | **5.21%** | 08-13 | −0.03 | **−0.01** | **94.2nd** |
| `DGS10` 10y | **4.63%** | 08-13 | −0.05 | **−0.06** | 87.0th |
| `DGS5` 5y | 4.32% | 08-13 | −0.06 | **−0.08** | 84.8th |
| `DGS2` 2y | **4.15%** | 08-13 | −0.05 | **−0.10** | 75.4th |
| `DFII10` real 10y | **2.39%** | 08-13 | −0.03 | −0.04 | 87.7th |
| `T10YIE` breakeven 10y | **2.27%** | 08-14 | +0.03 | +0.02 | **26.6th** |
| `BAMLH0A0HYM2` HY OAS | **2.71%** | 08-13 | 0.00 | 0.00 | **10.3rd** |
| `BAMLC0A0CM` IG OAS | 0.79% | 08-13 | 0.00 | +0.01 | 50.3rd |
| `NFCI` | **−0.549** | 08-07 | −0.003 | −0.025 | **7.1st (loosest)** |
| `VIXCLS` | **14.63** | 08-13 | +0.08 | −0.52 | **0.7th** |
| `DTWEXBGS` dollar | 119.06 | **08-07** | −0.45 | −0.64 | 40.3rd |
| `SOFR` | 3.62% | 08-13 | 0.00 | −0.03 | 20.4th |
| `RRPONTSYD` | **0.25 $bn** | 08-14 | −0.20 | −1.20 | 9.4th |
| `CPIAUCSL` | 332.813 | **2026-07-01** | +0.245 MoM | — | monthly, lags ~1 month |
| `UNRATE` | 4.1% | **2026-07-01** | −0.1 MoM | −0.3 (5 mo) | monthly |

⚠ **Freshness stated rather than implied**: the H.15 block ends **2026-08-13**, i.e. **one session
BEHIND the equity tape's 08-14**. `DTWEXBGS` is **9 days stale (08-07)** — the same `S12` staleness the
desk has logged since July. Monthly series (CPI, M2, UNRATE) carry a **~1-month** lag and are quoted as
July data, not as current.

### ★ A-1 · The re-measurement: `P56`'s stated premise does not survive the current window

`M653` / `P56` carry the mechanism as *"30y−10y widened +0.48 → +0.56 **with `DGS2` unchanged**"* ⇒
term premium, not a policy-rate move. Measured on the pull above, over the **08-06 → 08-13** window:

| | 08-06 | 08-07 | 08-10 | 08-11 | 08-12 | **08-13** |
|---|---|---|---|---|---|---|
| **30y − 10y** | 0.53 | 0.54 | 0.53 | 0.54 | 0.56 | **0.58** |
| **10y − 2y** | 0.44 | 0.46 | 0.47 | 0.48 | 0.48 | **0.48** |
| `DGS30` | 5.22 | 5.19 | 5.25 | 5.24 | 5.24 | **5.21** |
| `DGS2` | **4.25** | — | — | — | — | **4.15** |

**Both halves (C2).** The **spread half survives and extended**: 30y−10y **0.53 → 0.58 = +5bp**, a
fifth consecutive widening. **The level half is refuted**: `DGS30` **fell** 5.22 → 5.21, `DGS10` fell
9bp over the same window (4.72 → 4.63 on the real+breakeven decomposition), and **`DGS2` fell 10bp —
it is not "unchanged."**

⇒ **This is a BULL steepener at the long end, not a term-premium level rise.** Yields fell across the
curve and the 30y simply fell **less**. ★ **No new data was required to find this** — the prior run's
own pull contained it; the carried sentence was measured on an earlier window and never re-measured
(**C1's own failure mode, and the third time this desk has logged it**).
⚠ **Scope discipline (C4)**: this does **not** assert term premium is absent. It withdraws
*"with `DGS2` unchanged"* as a supporting clause. **What `P56` still owns is the spread; what it no
longer owns is the front end.** Registered as a retraction candidate — see §F and the run-end writeback.

### A-2 · The tension the whole board sits inside, in one line

**Financial conditions are at their loosest reading of the year while the long end sits near its
highest.** `NFCI` **7.1st percentile** · `HY OAS` **10.3rd** · `VIX` **0.7th** — against `DGS30` at the
**94.2nd**. And the breakeven at the **26.6th percentile** says the long end is **not** an inflation
expectation: real 10y **87.7th** vs breakeven **26.6th**.
⚠ **C3**: the desk does **not** have a measured cause for a 0.7th-percentile VIX. `unknown`, not "complacency".

---

## §B · Positioning — CFTC COT. **A REPLAY, and it is labelled as one.**

`scripts/us_flow.py --cot` · Tue **2026-08-11** close, released 08-14 · **identical to the 08-15 run,
instrument by instrument.** Context, never a trigger (D6).

| Instrument | Net spec | Weekly Δ | 1y %ile | Read |
|---|---|---|---|---|
| **S&P 500 (E-mini)** | +11,280 | **+38,538 ▲** | **88th** | 🟢 crowded long |
| **Nasdaq-100** | −42,905 | −7,899 ▼ | **0th** | 🔴 crowded SHORT |
| Russell 2000 | −13,943 | −5,044 ▼ | 18th | 🔴 crowded short |
| **UST 10Y** | −915,053 | +64,190 ▲ | **7th** | 🔴 crowded short |
| UST 2Y | −1,021,043 | −16,815 ▼ | 63rd | 🟡 neutral |
| USD Index | +21,409 | −1,090 ▼ | 80th | 🟢 crowded long |
| **WTI Crude** | +23,226 | +193 ▲ | **18th** | 🔴 crowded short |
| Nat Gas | −197,135 | +411 ▲ | 2nd | 🔴 crowded short |
| Gold | +217,940 | +20,306 ▲ | 49th | 🟡 neutral |
| **Copper** | +80,388 | +3,265 ▲ | **100th** | 🟢 crowded long |
| Silver | +23,646 | +1,366 ▲ | 33rd | 🟡 neutral |

🚫 **This table may not be cited as "positioning held" or "confirmed for a second run."** It is the
same Friday release read twice. The **88-percentile-point spread** inside equities (S&P 88th vs
NDX 0th) is one observation dated **08-11**, not two.
★ **The one row that has acquired new outside information since it was measured is `WTI` at the 18th
percentile short** — §D shows the Hormuz axis escalated on **08-14/08-15**, i.e. **after** the COT
snapshot. That asymmetry (short positioning frozen before an escalation) is the input to `P66`.

---

## §C · The tape — settled through 2026-08-14. **Frozen; stated, not re-read.**

`SPY` **776.34** (08-14), −0.20% from 08-13's 777.88. Median last-bar volume **0.649×** the trailing
20-day average, after 08-13's 0.732× — **two consecutive sub-0.75 sessions**, and August monthly opex
is **08-21**, so this is not an expiry artifact.
Universe: n=299 · `wflow` **−0.132** · **9 🟢 / 60 🔴**.
11-sector table lives in `SECTOR_FLOW_US.json §sector_rotation` and is **not reprinted here** — it is
identical to the 08-15 run to three decimals.
⚠ **G3 flippers (3 of 11), binding on ROTATION**: Information Technology (`NVDA`, 19.4%) ·
Industrials (`CAT`, 8.7%) · Materials (`LIN`, 24.7%) — `wflow` inadmissible for promotion or demotion.
⚠ Every cap weight above is computed from a **32-day-old** market-cap file.

---

## §D · News — **the only axis that moved**, `--scope foreign`

### D-0 · The denominator, and what could NOT be read

| | |
|---|---|
| Daily event counts, 08-10 → 08-16 | 789 · 798 · 781 · 801 · **736** · **269** · **112** |
| 08-16 brief | **624 articles → 297 clusters → 112 events** (2+ outlets) · market 112 / non-market **0** |
| Recovery sections actually read | `single_source` **15 shown / 185 total** · `excluded_nonmarket` **0 / 0** (band nb>−3.0) · `subevents` **15 recovered** at threshold 0.65 |
| Tail (2 outlets) | **0** |
| ⚠ Body-blindness, measured this run | `coverage Iran Hormuz --days 7` → pool **35,627**; title+summary recall **39.1%**; **60.9% of body-matching articles are invisible to a title search** — 🔴 |

🚨 **"Quiet" is inadmissible today, and the reason is a calendar, not a market.** The corpus runs
**736 → 269 → 112** across Fri → Sat → Sun — a **6.6× collapse** that is a weekend property of the
feed. Any bucket reading low over a window containing 08-15/08-16 is reading the publication schedule.
🚨 **And 170 of the 185 single-outlet items were not shown** — the tier where FX, rates and oil primary
material lives. **The `min_nb` gate cannot score them at all** (the classifier is Korean-only), so they
are **unmeasured, not low**.

### D-1 · Term sweep — separate argv (never a quoted bigram), 7d vs 30d

| Term | 7d | 30d | raw velocity ×4.286 | Read |
|---|---|---|---|---|
| `refinery` | 354 | 1,140 | **1.33×** | ★ fastest of the sweep |
| **`shadow` AND `credit`** | 28 | 93 | **1.29×** | ★ **new object, §D-3** |
| `rate` AND `cut` | 1,637 | 5,889 | 1.19× | |
| `OPEC` | 177 | 639 | 1.19× | |
| `Hormuz` | 1,442 | 5,367 | **1.15×** | escalating, §D-2 |
| `tariff` | 1,577 | 6,057 | 1.12× | |
| `data` AND `center` | 3,269 | 12,810 | 1.09× | largest absolute pool |
| `credit` AND `spread` | 418 | 1,651 | 1.09× | |
| `diesel` | 269 | 1,076 | 1.07× | |
| `recession` | 316 | 1,269 | 1.07× | |
| `capex` | 921 | 3,871 | 1.02× | |
| `Fed` | 1,455 | 6,309 | 0.99× | |
| `DRAM` | 232 | 1,006 | 0.99× | |
| `memory` | 1,344 | 5,923 | 0.97× | |
| `Iran` | 2,185 | 10,622 | **0.88×** | ⚠ decelerating |
| `layoffs` | 132 | 678 | 0.83× | |

⚠ **These are RAW ratios and are biased LOW by roughly the weekend effect** — the 7-day window
contains two collapsed days, the 30-day window contains eight. **No term is called "fading" on this
table**, and the ordering (not the level) is what is used below.
★ **`Iran` 0.88× while `Hormuz` 1.15× and `refinery` 1.33×** is the sweep's most informative pair: the
*country* story is decelerating while the *chokepoint* and the *physical asset* stories accelerate.
The narrative has moved from politics to plumbing.

### D-2 · ★★ The oil axis — a dated escalation on ONE side and a dated de-escalation on the OTHER

**Escalation, all body-read:**
- **2026-08-14 — *"Trump threatens to declare strait of Hormuz 'territory of the United States'"*** [`guardian`].
  This is the **exact object `CATALYST_WATCH` carries as an undated 🔀binary** and that `S8` has failed
  to date for **14 runs**.
- 2026-08-15 — *"Trump asks Americans to accept high pump prices as Iran standoff drags on"* [`seekingalpha`, **1 outlet**].
- 2026-08-14 — *"CNBC Daily Open: Washington tightens squeeze on the Iranian economy"* [`cnbc`].
- **2026-08-15 — *"Depleted strategic oil reserve nears level that raises concerns about damage to caverns, operations"*** [`cnbc`]. ★ A **physical** constraint on the US's own shock absorber.
- Ukraine → Russian refining, five dated strikes in six days: **08-10** refinery deep inside Russia (13 killed) [`guardian`] · **08-11** major refinery [`oilprice`] · **08-13 Gazprom's Salavat, 200,000 bpd, Urals** [`oilprice`+`bloomberg`] · **08-14** fuel-terminal blaze [`oilprice`] · **08-14 *"Russia admits new petrol shortages"*** [`euronews`].
- **08-12 — *"Russia Imports Indian Fuel as Refinery Crisis Deepens"*** [`oilprice`] · **08-13 — *"Russia's Diesel Exports Crash to Multiyear-Low amid Tight Global Market"*** [`yahoo_finance`].

**De-escalation, and it is NOT buried (C2 — both halves):**
- **2026-08-12 — *"Kyiv stops strikes on Russian port after request from JD Vance"*** [`semafor`].
  ⇒ **A named US actor is already applying the brake to the exact mechanism.**
- 2026-08-13 — *"Crude Prices Undercut as Persian Gulf Tensions Ease Slightly"* [`nasdaq`] and
  *"Oil falls on weaker demand outlook and higher US stocks"* [`yahoo_finance`].

⇒ **The distillate story has a named physical driver AND a named political off-switch, both dated
inside the same week.** That is the `L3` shape (a branch that carries information), and it is why
`P66` below is registered as a **bracket**, not a tilt.

### D-3 · ★★★ A genuinely NEW macro object: **$70bn of "shadow credit" backstops for AI companies**

| Date | Outlet | Item |
|---|---|---|
| **08-15** | `bloomberg` | *"Bond Traders Agonize Over AI Companies' $70 Billion of Shadow Credit Backstops"* |
| 08-15 | `yahoo_finance` | same story, **body available** |
| **08-16** | `google_en` ×2 (The Edge Singapore · The Business Times) | syndicated — the story is **spreading on a Sunday**, which is unusual |
| 08-11 | `wsj` | *"Private-Credit Firms Clamp Down on Loan Sweeteners in Fear of 'Shadow Defaults'"* |

**Why this matters to this desk specifically, and it is not a new idea — it is an old one acquiring a
number.** `M134` established that **the data-centre node's live variable is cost of capital, not the AI
narrative** (`GOOGL` Q2 FCF **−$5.86bn**, funded by a **$49.6bn** equity raise). This week supplies the
debt-side instance: **`AMD` borrowed $4.75bn, more than triple its prior bond sale** [`fool`/`nasdaq`/
`yahoo_finance` 08-15/16], and the stock **rose 5.6% on the day the deal landed** [`yahoo_finance` 08-14].
⇒ **AI capex is migrating onto balance sheets and into structures bond desks are calling shadow.**

⚠ **And the credit instrument says nothing yet**: `HY OAS` **2.71% = 10.3rd percentile, unchanged for
5 sessions**; `IG OAS` 0.79 flat; `NFCI` at its loosest of the year. ⇒ **Narrative-only, and labelled
as such.** This is the exact failure the desk logged on 2026-07-21 (*"a whole credit-stress stack built
from narrative while HY OAS sat 6bp off its 365-day low"*). **`P67` registers it as a bracket rather
than promoting it.**

### D-4 · Two dated items the catalyst instrument MISSED

1. ★ **`Reddit` joins the S&P 500 on 2026-08-18** [`yahoo_finance` 08-14]. `catalyst_calendar --days 5`
   printed **`[STRUCTURAL] (none in window)`** — an index rebalance **two sessions out** is precisely
   what that block exists to carry, and `data/catalysts/structural_schedule.json` is human-maintained
   (P5). **Named, not fixed.**
2. **Earnings week ahead: `WMT` · `BABA` · `HD` · `TGT`** [`seekingalpha` 08-15]. The `[EARNINGS]` block
   printed *"(none in window / yfinance unavailable)"*. ⇒ **`CATALYST_WATCH.json` under-reports this
   week by at least six dated events.** The consumer complex reports into a tape where `XLY`'s exc5 was
   the worst of eleven — that is a DISC input, and the calendar did not carry it.

### D-5 · Instrument defect found in `thread` this run

`thread --days 7 --scope foreign` returns its longest `BUILDING` chains as **syndicated evergreen
templates**, not stories: *"Airbnb vs. McDonald's → Booking vs. Celsius → Adobe vs. AppLovin →
Amazon vs. Comcast → Arista vs. Intel → Reddit vs. Snowflake"* — **6 days, 89 articles, tagged
BUILDING**, and it is one publisher's recurring column format. The same shape appears three more times.
⇒ **On a weekend-heavy window the trajectory tool's BUILDING tag is contaminated by publication
templates.** Registered as a dig; **no proposition below cites a `thread` tag.**

---

## §E · Propositions — falsifiable, both directions, mandatory anti-signal

> ID 3-grep at write time (`handoff/` · `llm_outputs/` · `REPORT/`): highest existing **P64** ⇒ this
> run takes **P65–P68**.
> ⚠ **Every observable below settles on a FUTURE session.** Nothing registered here can be scored by
> re-reading 08-14, which is the point.

### P65 — ★★★ `P56`'s mechanism is half wrong, and the half that is wrong is the FRONT END
**Claim.** The long-end move is a **bull steepener**, not a term-premium level rise. Over 08-06 → 08-13
`30y−10y` widened **0.53 → 0.58 (+5bp)** *while* `DGS30` **fell** (5.22 → 5.21), `DGS10` fell 9bp and
**`DGS2` fell 10bp (4.25 → 4.15)**. `P56`/`M653`'s supporting clause *"with `DGS2` unchanged"* is
refuted on the current window. `[measured]` `[FRED]`.
**Direction A (bull steepener, real):** at the **2026-08-21** `[FRED]` settle, `30y−10y` **≥ 0.58**
**AND** `DGS2` **≤ 4.15%** — the spread holds or widens while the front end does not rise.
**Direction B (term premium reasserts as a level move):** `30y−10y` **≥ 0.58** **AND** `DGS2`
**≥ 4.30%**.
**Between = C, no information.**
**🚨 Mandatory anti-signal:** a **September FOMC-dated** communication or an inflation print inside the
window confounds the front-end leg ⇒ the row is **VOID**, not scored favourably.
**⚠ D212:** the `[FRED]` H.15 block publishes **3–4 sessions late**; the 08-21 read may land 08-25.
The row settles on **the first published close covering 08-21**, stated at registration.

### P66 — ★★★ The distillate bid has a named physical driver AND a named political off-switch — this is a BRACKET, not a tilt
**Claim.** The crack's middle-distillate leg (`P62`, `M127`) acquired **five dated Russian refining
strikes in six days** (08-10 · 08-11 · **08-13 Salavat 200kbpd** · 08-14 terminal · 08-14 Russia admits
petrol shortages) plus **Russian diesel exports at a multiyear low** (08-13) and **Russia importing
Indian fuel** (08-12). **And in the same window a named US actor applied the brake**: *"Kyiv stops
strikes on Russian port after request from JD Vance"* [`semafor` 08-12]. `[news]`-grade both sides.
**Direction A (supply destruction dominates):** at the **2026-08-21** settle, `HO=F` 20-day return
exceeds `CL=F` 20-day by **> +4pp** (`P62`'s branch A) **AND** at least one further **dated** strike on
Russian refining capacity appears in the foreign corpus inside the window.
**Direction B (the off-switch dominates):** the `HO=F` − `CL=F` 20-day gap closes to **≤ 0pp** **OR** a
dated US-brokered halt to strikes on Russian energy infrastructure is reported by **≥3 independent
outlets**.
**Between = C.**
**🚨 Mandatory anti-signal:** a **US refinery outage** or a **PADD3 hurricane landfall** inside the
window makes distillate strength a domestic-supply artifact ⇒ **VOID** (inherited from `P62`).
**⚠ C4:** this row does **not** claim to know which side wins. Its information content is that **both
branches are now dated and observable**, which they were not on 08-15.

### P67 — ★★ The AI capex bill is migrating to the debt market, and the credit instrument does not see it yet
**Claim.** Two dated instances one week apart — **`AMD` borrowing $4.75bn, >3× its prior bond sale**
(08-14, stock **+5.6%** the same session) and **$70bn of "shadow credit" backstops for AI companies**
now being priced by bond desks (`bloomberg` 08-15, syndicated to 2 further outlets 08-16) — against a
credit tape that is **flat at its loosest of the year** (`HY OAS` **2.71% = 10.3rd percentile,
unchanged 5 sessions**; `NFCI` **7.1st percentile**). This connects the debt side to `M134`'s equity
side (`GOOGL` FCF **−$5.86bn**, **$49.6bn** raise).
**Direction A (the instrument catches up):** `BAMLH0A0HYM2` **≥ 2.85%** (+14bp) at the first `[FRED]`
close covering **2026-08-28**.
**Direction B (it stays narrative):** `BAMLH0A0HYM2` **≤ 2.71%** at the same settle — i.e. no widening
at all despite the story spreading.
**Between = C.**
**🚨 Mandatory anti-signal:** a **macro** credit event unrelated to AI financing (sovereign, bank,
non-AI HY default wave) inside the window makes any widening non-attributable ⇒ **VOID**.
**⚠ Labelled `narrative-only` in the text per the MACRO EXIT CHECK** — no sector verdict in §G rests on
this row. It is registered **because** the desk has previously built a credit-stress stack out of
narrative and paid for it (2026-07-21).

### P68 — ★★ Two of this desk's four macro instruments cannot distinguish "no change" from "no observation"
**Claim.** On 2026-08-16 the equity tape, the `[FRED]` block and the COT block all returned **values
identical to the prior run**, and **nothing in any artifact says so**. `SECTOR_FLOW_US.json`'s
`§scoring` carries `n_axes`/`vel_coverage`/`scored` but no session counter; `history.json` was
**overwritten at the same key `2026-08-14` by two consecutive runs**. `[measured]`.
**Direction A (this is a systemic reporting gap):** the **next** non-session run (the coming weekend)
reproduces the same three-way identity **and** the artifacts again carry no marker.
**Direction B (it self-corrects):** any of the three artifacts emits a session/observation counter
before then.
**🚨 Mandatory anti-signal:** if a human promotes `us_all_v2_candidate.csv` or otherwise changes the
universe inside the window, the identity test is confounded ⇒ **VOID**.
**⚠ This is a process proposition, not a market one.** It is registered here because §F below cannot
score a single price-KPI row today, and the reason is exactly this.

---

## §F · Self-backtest — and the honest result is that nothing could be scored

| # | Registered claim | KPI | Settles | Measured today | Verdict |
|---|---|---|---|---|---|
| **P61** (08-15) | Fed-hike premium detached from oil; driver is DEMAND | `DGS2` at 08-21 vs 4.05 / 4.30 | **08-21** | `DGS2` **4.15%**, unchanged observation (08-13) | **UNSCOREABLE — window has not advanced.** Not "carried favourably" |
| **P62** (08-15) | Energy's strength is DISTILLATE | `HO=F` − `CL=F` 20d gap at 08-21 | **08-21** | No settled session | **UNSCOREABLE.** ★ But its *narrative* leg strengthened materially — §D-2, five dated strikes ⇒ folded into `P66` |
| **P63** (08-15) | 88-point percentile spread inside equities | `RSPT−XLK`, `XLK−SPY` at 08-21 | **08-21** | COT identical (Tue 08-11) | **UNSCOREABLE** |
| **P64** (08-15) | Two record-adjacent sessions on ⅔ volume | median `vol_surge` + `SPY` vs 777.88 at **08-20** | **08-20** | 0.649× / 776.34 — **the same two sessions**, not a third | **UNSCOREABLE.** n is still 2 |
| **P52** (08-13) | In-line print sent money to growth, not defensives | `XLK` exc5 ≤0 **∧** `XLU` exc5 >0 ⇒ A refuted | 08-19 | Refuting conjunction still cannot fire (`XLK` +0.687, `XLU` +1.207 — **same closes**) | **CARRIED. Not re-counted as a second confirmation** |
| **P53** (08-13) | Materials' broad leg lasted two sessions | ex-`NEM` EW exc5 positive ⇒ A wrong | 08-19 (`S77`) | **−2.097, same closes** | **CARRIED, not re-scored** |
| **P56** (08-14) | Long end = term premium, `DGS2` pinned | curve shape | — | ★ **§A-1: the `DGS2`-pinned clause is REFUTED on the current window** | ⚠ **PARTIAL RETRACTION — spread survives, front-end clause withdrawn.** See `P65` |

**Running hit-rate this run: 0 HIT · 0 HALF · 0 MISS · 5 UNSCOREABLE · 1 PARTIAL RETRACTION.**

🚨 **A zero-scored backtest is a finding, not a blank.** Every price-anchored KPI this desk registered
settles on a future session, and **no session settled.** The desk ran a full macro stage and could not
move a single scoreboard row — which is the strongest available argument that **a second consecutive
non-session run has low marginal value on the price axes and should be spent on news, filings and
re-measurement**, which is what §A-1 and §D did.
★ And the one thing that *did* change came from **re-measuring data the desk already had** (`P56`),
not from waiting for new data.

---

## §G · ★ SECTOR TRANSMISSION MATRIX — wind direction only, all 11 GICS

> ROTATION's input. **This is a wind reading, not a verdict.** ⚠ Every flow number below is the
> **08-14** observation, unchanged since the prior run — a matrix row that agrees with yesterday's is
> agreeing with itself.

| # | Sector | Driving prop. | Wind | Evidence, benchmark named inline |
|---|---|---|---|---|
| **1** | **Energy** | **P66** · P62 | ★ **OW-side, and the NARRATIVE leg strengthened while the price leg stood still** | Board's **only positive `wflow` +0.217** and **not a flipper** (ex-`XOM` +0.205 at a 30.5% weight) · `eqflow` **+0.102** and `breadth` **0.12**, both the highest of eleven. ★ New this run: **five dated Russian refining strikes in six days** + Russia at a **multiyear-low diesel export** + **SPR near a cavern-damage threshold**. ⚠ **Both halves**: a **named political off-switch** exists (JD Vance / Kyiv port halt, 08-12) and `WTI` spec sits at the **18th percentile SHORT** — dated 08-11, *before* the escalation |
| **2** | **Information Technology** | P63 · P65 | **OW-side wind, on BREADTH — and its cap-weight leg is one name** | `eqflow +0.044 > wflow +0.023`; `RSPT` beat `XLK` on all three windows vs **`SPY`** at the last settle. **NDX spec 0th percentile short.** ⚠⚠ **G3 flipper**: ex-`NVDA` `wflow` is **−0.082**; breadth 0.05 (5🟢/6🔴 of 56). ⚠ `S85` (its own falsifier, settle 08-21) reads **+1.343 = branch C** |
| **3** | **Industrials** | — | **OW-side wind, on an object the bracket does not measure** | ⚠⚠ **`D249`, 5th run**: the falsifier measures `XLI`, the position is **defense**. G3 flipper (`CAT`, 8.7%) ⇒ `wflow` inadmissible; `eqflow −0.007`, breadth 0.00. **No new information this run** |
| **4** | **Health Care** | — | **Neutral** | `eqflow +0.027` positive and `XLV` exc60 **+7.803 vs `SPY`, 2nd best of eleven**, against **Δ −0.103 = the worst of eleven and a 4th consecutive negative**. `S76` 08-19 · `S82` 08-20 (already **+3.091**, above its branch A) |
| **5** | **Financials** | P65 | **Neutral−, and `P65` weakens its remaining macro leg** | `eqflow −0.126` still **below** `wflow −0.031` ⇒ `M40`'s inversion unrepaired (`R69` stands). ★ **A steepener argument is now available on the 30y−10y leg (+5bp) — and `P65` shows it is a BULL steepener with the front end FALLING**, which is not the NII geometry `M138` describes. **The steepener does not rescue FIN** |
| **6** | **Materials** | P59 | **UW-side wind** | G3 flipper (`LIN` 24.7%) ⇒ `wflow` inadmissible; `eqflow −0.114`, breadth 0.00. **Copper spec at the 100th percentile long** while `FCX` was the basket's worst name vs **`SPY`**. `S77` 08-19 |
| **7** | **Consumer Discretionary** | — | **UW-side wind, and the calendar instrument failed it** | `eqflow −0.123`; `XLY` exc5 was the worst of eleven vs **`SPY`**. ★ **New**: **`WMT` · `HD` · `TGT` all report this week** and `CATALYST_WATCH` carried **zero earnings** (§D-4); *"US retail sales post first decline in nine months in July"* [08-14]. ⚠ **Δ +0.038 is positive** — the demote was declined on that and nothing has changed it |
| **8** | **Communication Services** | — | **UW, both directions blocked** | Δ +0.092 (best of eleven) vs `XLC` exc60 **−8.311 vs `SPY`** (worst of eleven) ⇒ **C3**. ⚠ **The bucket changed membership** (`EA` left the scored set) — its numbers moved by composition |
| **9** | **Consumer Staples** | — | **UW−, floor of this board** | Δ **+0.081, positive**; nothing pushes. Last DEEP **08-10 = 6 runs, the longest gap on the board** |
| **10** | **Utilities** | P65 | **UW — and `P65` changes the mechanism under it a SECOND time** | ★ The board's **only real (non-`vol_surge`-artifact) flow absence**: **0 of 15** pass `OBV 매집 ∧ RS20>0`; `eqflow −0.433` worst of eleven. ⚠ Against: `XLU` exc5 **+1.207 vs `SPY`, 2nd best of eleven**, and Δ +0.045. ★ **A bull steepener with `DGS2` FALLING is a friendlier rate backdrop for regulated utilities than the term-premium story the UW was written under.** The sign is unchanged; **its justification is now contested twice** |
| **11** | **Real Estate** | P65 · **P67** | **UW — the most internally consistent verdict, and now the most interesting contradiction** | Every aggregate axis agrees (`wflow −0.280` · `eqflow −0.244` · breadth 0.00 · exc20 −4.777 vs **`SPY`**, deteriorating). ⚠ **Yet 4 of 12 names accumulate — `EQIX` `DLR` `CBRE` `IRM` = `M131`'s measured data-centre unit.** ★ **`P67` supplies the variable that should decide it**: if AI capex is migrating into shadow-credit structures, the data-centre node's live sensitivity is **cost of capital** (`M134`), not the AI narrative — and `HY OAS` at the **10.3rd percentile** currently argues the *opposite* of the UW |

**Wind summary.** OW-side: **Energy** (strongest, and the only one whose evidence grew this run) ·
**IT** (breadth leg only) · **Industrials** (on an unverified object). UW-side: **RE · UTIL · COMM ·
STPL · MATR**. Neutral: **HLTH · FIN · DISC**.
⚠ **ROTATION must read `HANDOVER §2`'s warning before acting**: with zero new sessions, **every flow
input to a verdict change is byte-identical to the one that produced yesterday's verdicts.** A verdict
delta today has to be carried by something that actually moved — **§D news, §A-1's re-measurement, or
an error found in yesterday's reasoning** — and it must say which.

---

## §H · Linter

`python -X utf8 scripts/report_lint.py llm_outputs/2026-08-16/industry_US/MACRO_REPORT.md` — result
recorded in the run log below. ⚠ **It checks form only** (C1 benchmark · C2 both halves · S6 future
label · D6 OBV-alone); a clean run is not a correct report.

---

## §I · §4c — claims this stage asserted and then refuted (D48 class)

**This stage's own count: 1.**

🚨 **This stage drafted §D-1 with the sentence "`Iran` is FADING at 0.88×" and its own denominator
refuted it.** The 7-day window contains **two weekend days at 269 and 112 events against a weekday norm
near 780** — a **6.6× collapse** that biases *every* 7d/30d ratio downward. The corrected statement is
that the sweep's **ordering** is usable (`refinery` 1.33× > `Hormuz` 1.15× > `Iran` 0.88×) and its
**levels are not**, and that **no term may be called fading on this table today**. Left in place per
§4c rather than edited away.

⚠ **One self-refutation in a stage that ran four independent instruments is a LOW count**, and this
stage says so: three of those four instruments returned frozen data, so they could not contradict
anything. **The controls were weak by construction today.**

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** — `catalyst_calendar --days 5` → `llm_outputs/2026-08-16/CATALYST_WATCH.json`.
      **1 🔀binary in window** (the undated Hormuz statement) ⇒ **PREMORTEM must produce a both-sides
      bracket.** ⚠ Two dated catalysts the tool MISSED are named in §D-4 (`Reddit` S&P 500 inclusion
      **08-18**; `WMT`/`BABA`/`HD`/`TGT` earnings this week).
- [x] **Events read via `brief --body 2`** after `embed sync` (1,855 new articles) — **tail = 0**.
- [x] **`tail = 0` is NOT the coverage claim.** The three recovery sections were read and counted:
      `single_source` **15 shown / 185 total** (⚠ **170 withheld, and the classifier cannot score any of
      them — Korean-only**), `excluded_nonmarket` **0 / 0** at band nb>−3.0, `subevents_recovered` **15**.
- [x] **Denominator quoted after non-news removal** — 08-16: **624 articles → 297 clusters → 112
      events**, non-market 0. Weekly event counts printed in §D-0.
- [x] **Trajectories read** (`thread --days 7`) — ★ **and a defect was found and reported (§D-5): the
      longest BUILDING chains are syndicated evergreen templates, not stories.** **No proposition cites
      a `thread` tag**, and that exemption is stated rather than silent.
- [x] **Every "nothing happened in bucket X" claim carries its denominator** — and §D-0 forbids "quiet"
      outright today, because the corpus collapses **736 → 269 → 112** across the window.
- [x] **No bucket's hit count came from a quoted multi-word term** — every term in §D-1 was passed as
      **separate argv** (`shadow credit` → `("shadow") AND ("credit")`, verified in the tool echo).
- [x] **Every headline print cited with both halves** — §A-1 gives the spread half **and** the level
      half of `P56` and reaches opposite verdicts on them; §A gives Δ1 and Δ5 for every daily series.
- [x] **Every relative-performance number names its benchmark inline** (`SPY` throughout §G); **no
      statistical result carried across markets** — the `vol_surge` IC finding is **KR-measured** and is
      reported in `HANDOVER §8` as a **dig, not a gate flip** (`W1`).
- [x] **Credit axis read and cited** — `hy_oas` **2.71% (10.3rd pctile)** and `nfci` **−0.549 (7.1st)**.
      ★ The one credit *story* this run found (`P67`) is explicitly labelled **narrative-only** because
      neither series moved.
- [x] **`real_10y` quoted with `breakeven_10y`** — **2.39% (87.7th) vs 2.27% (26.6th)** ⇒ the long end
      is a **real** phenomenon, not an inflation-expectation one.
- [x] **Transmission matrix produced — all 11 sectors, one line each** (§G), with the driving
      proposition ID and the benchmark named.
- [x] **Self-backtest appended with a running hit-rate** (§F) — **0 HIT / 0 HALF / 0 MISS / 5
      UNSCOREABLE / 1 PARTIAL RETRACTION**, and the zero is reported as a finding rather than hidden.
- [x] **New blind-spot terms folded into the term table** — `shadow`+`credit` added this run (1.29×,
      the sweep's #2) after appearing in the single-outlet tier.
- [x] **Linter run on this stage's own output** — `report_lint.py` on this file: **0 findings** across
      C1 · C2 · S6 · D6. ⚠ Restated so it is not over-read: **a clean lint is a form check, not a
      correctness check** — it cannot see that three of this stage's four instruments returned frozen
      data, which is the report's most important content.

---

# §5 · ADDENDUM — post-run DRIFT (appended 2026-08-16 ~23:35 KST · APPEND-ONLY, nothing above is rewritten)

> Written by stage 11 (L1·DRIFT). **The original call above stays visible next to its correction** —
> that asymmetry is what feeds the self-backtest. 🚨 **DRIFT FIRED.**

## 5-0 · The instrument, reported FIRST (PREFLIGHT G1 binds this stage explicitly)

**`drift_watch.py` FAILED, twice, and it is the same failure as every prior run:**
`drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용)` — `drift` is **not on the remote news
API's allow-list** (`['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']`).
Retried once per the unattended-run rule; failed identically. **`D17`, logged unrepaired again.**
⇒ **This stage ran on its documented substitutes**: `burst --date 2026-08-16 --scope foreign` and a
12-term kill-switch `fts` sweep with the **pool ratio as a gate** (`D264`).
⚠ **Window caveat, stated rather than hidden**: DRIFT is specified as a **+3–6h** post-run check. This
run's MACRO baseline was ~22:2x KST and this addendum is ~23:3x — **≈1 hour, not 3–6.** What follows is
therefore *"does the corpus already contradict the report"*, **not** a full drift window.

## 5-1 · Pool-normalised kill-switch sweep — anchored on a MEASURED denominator, not an assumed one

Pools measured, not assumed: **d1 = 5,514 docs · d7 = 35,627 docs** ⇒ a term with **no** change reads
`d1/d7 = 0.1548`. Everything below is divided by that.

| Kill term (separate argv) | d1 | d7 | **pool-normalised** | Read |
|---|---|---|---|---|
| **`truce`** | **16** | 62 | **★ 1.67×** | **the only term meaningfully above pool — body-read below** |
| `default` | 59 | 333 | 1.14× | at pool |
| `tariff`+`consumer` | 89 | 505 | 1.14× | at pool |
| `strikes`+`halt` | 11 | 64 | 1.11× | at pool |
| `hurricane` | 10 | 58 | 1.11× | at pool |
| `guidance`+`cut` | 155 | 949 | 1.06× | at pool |
| `ceasefire` | 27 | 204 | 0.86× | below pool |
| `capex`+`cut` | 34 | 262 | 0.84× | below pool |
| `credit`+`stress` | 17 | 130 | 0.84× | below pool |
| `sanctions`+`lifted` | 11 | 114 | 0.62× | below pool |
| **`Hormuz`+`open`** | 35 | 435 | **0.52×** | **decelerating** |
| ✅ **`refinery`+`outage`** | **0** | 17 | **0.00×** | **`P62`/`P66`'s VOID condition has NOT fired** |

⚠ **`burst` was run and is reported as UNUSABLE on this date, not as a clean all-clear** (`D264`). Its
76 "spikes" are computed against a **730-doc Sunday denominator**, so `z = 24.93` sits on **n = 3**.
The only entries with real n corroborate the report rather than contradicting it: **`WALMART` n=13
(z 15.63, mkt 100%)** ← the `S93` consumer complex · **`AMD` n=13 + `BORROWED` n=3 + `TRIPLE` n=3** ←
Card 4 / `P67`'s $4.75bn bond · `MSTR` n=5 ← the `missed_ledger` row filed this run.
**No kill-switch term appears anywhere in the spike list.**

## 5-2 · 🚨 What DRIFT actually found — and it CORRECTS this report's own oil read

Body-read of the `truce` hits (most are Lebanon/Israel and Yemen — stated so the count is not
over-read). **Two are directly on this desk's #1 OW axis, and neither is in §D above:**

| Date | Outlet | Item |
|---|---|---|
| ★★ **2026-08-15** | **`fortune`** | ***"Iran, Oman home in on Hormuz Strait deal as ship attacks mount"*** |
| ★ **2026-08-16** | `aljazeera` | *"Iran war live: **Talks on Hormuz Strait continue**; Israel kills 11 in Lebanon"* |

### What this corrects

**§D-2 above read the Hormuz axis as escalating** — anchored on *"Trump threatens to declare strait of
Hormuz 'territory of the United States'"* (`guardian` 08-14) and *"Trump asks Americans to accept high
pump prices"* (`seekingalpha` 08-15) — and carried de-escalation only as a **generic** counterweight
(*"tensions ease slightly"*, `nasdaq` 08-13).
⇒ **That was incomplete.** There is a **named mediator (Oman), a named negotiation (a Strait deal), and
it is live TODAY.** A negotiated Hormuz settlement is a materially different object from "tensions
easing" — it is `S92`'s **branch B** acquiring a mechanism and a counterparty.

**What survives, and what does not:**
- ✅ **`P66` / `SECTOR_DEEP_ENRG` are UNAFFECTED on their stated mechanism.** That thesis rests on
  **Russian refining capacity destruction** (Salavat 200kbpd, Russia importing Indian fuel, diesel
  exports at a multiyear low) — **not** on the Strait. **PREMORTEM §2b pre-registered exactly this
  asymmetry**, which is why `S92` carries a **branch C** (a US-brokered halt to Ukrainian strikes) as
  the only branch that can falsify the Energy OW. **`refinery outage` at 0.00× confirms the VOID
  condition has not fired.** The bracket did its job before the news arrived.
- ⚠ **What IS weakened is §D-2's framing**, `S92` **branch A's** likelihood, and any reading of `WTI`'s
  18th-percentile short as "positioned against an escalation the market has not seen." **The market may
  be positioned for a deal that is actually being negotiated.**
- ⚠ **`Hormuz open` reads 0.52× — BELOW pool.** ⚠ **This may NOT be read as "the theme is cooling"**
  (PREFLIGHT G1 forbids it, and the body-read directly contradicts it: talks are *ongoing*). It is the
  standard failure of a fixed two-word probe against a story whose vocabulary shifted to **"deal"** and
  **"talks"**. **The fixed term missed the event; the body-read caught it.**

### Registered rather than argued
**No threshold on `S92` is moved** — a bracket whose threshold moves after the news is a description
wearing a forecast's clothes. `S92` branch B stands as frozen: `CL=F` **< 78.00** through **2026-08-31**
with no dated US action. **This addendum records that branch B now has a named mechanism**, which is
information about its *probability*, not about its threshold.

## 5-3 · What did NOT drift

- **`[FRED]`**: nothing published since §A was written; the H.15 block still ends **2026-08-13**.
- **The tape**: still **2026-08-14**. Zero sessions settled during this run.
- **Credit**: `credit stress` **0.84× — below pool**, consistent with §A's `HY OAS` **2.71% (10.3rd
  percentile), unchanged 5 sessions**. **`P67` stays `narrative-only`; the drift check did not
  upgrade it.**
- **`capex cut` 0.84×** — the §4 asymmetry's trigger (*a hyperscaler capex CUT changes the thesis*) is
  **not firing**.
- **`tariff consumer` 1.14×, at pool** — `S93`'s VOID condition has not fired.

## 5-4 · This addendum's own D48 line

⚠ **This stage's substitute sweep initially read `Hormuz open` at 0.52× and drafted "the Hormuz axis is
decelerating post-report."** The body-read of a *different* term (`truce`) refuted it within the same
stage — **talks are live and a deal is being negotiated.** ⇒ **A fixed-term velocity probe returned the
opposite of the truth because the story changed vocabulary.** Left visible rather than edited away;
this is the **second** independent instance this run of a term-frequency instrument disagreeing with the
world it is measuring (§I was the first).

**✅ DRIFT EXIT CHECK** — `drift_watch` run (failed ×2, `D17`, substitutes used and named) · the 🚨 item
was **body-read, not merely counted** · **§5 ADDENDUM appended, append-only, nothing above rewritten**.
