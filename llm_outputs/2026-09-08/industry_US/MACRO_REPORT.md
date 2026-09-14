# MACRO_REPORT — industry_US · 2026-09-08 (Tue) · Stage 3 / L1·MACRO

> Runtime `--market us` · news `--scope foreign` on every call (hard rule).
> Daily anchor read: `llm_outputs/2026-09-07/industry_US/MACRO_REPORT.md` (§A–§F incl. `P142`·`P143`·`P144`)
> and this run's `HANDOVER.md` + `preflight/PREFLIGHT.md`. Ledger cross-queried (`module_report_tags show`).
> **Clock: this stage ran 09:2x–10:0x ET, i.e. it CROSSED the 09:30 ET open mid-stage.** See §0-b — that
> crossing is this run's first new instrument finding and it governs every price number below.

---

## §0 · 🚨 Instrument state governing every line below (from `preflight/PREFLIGHT.md`)

| gate | verdict | what it removes |
|---|---|---|
| G0 | ✅ PASS (1/301 NaN, `EA` only; partial-NaN 0; **no 09-08 bar at 09:10 ET**) | any verdict on `EA` |
| G1 | 🔴 sweep news axis 17.39% (52/299); direct path 8/8 pre-sweep, 0/4 post, 2/2 after idle | 🚫 no velocity/freshness **from the sweep**; 🚫 no "quiet" claim for **UTIL / MATR / RE** (0 names measured each) |
| G2 | 🟡 scale continuous, **novelty ZERO for a 4th run** (`asof` 2026-09-04; 11/11 sectors identical on 11/11 fields) | 🚫 Δflow may not be worded as today's move — it is **09-03→09-04** |
| G3 | ✅ list printed (1 flipper by flag, 2 by issuer) | 🚫 no `wflow` verdict on **Cons. Disc.** or **Comm. Services** |
| G4 | 🔴 12 / 11 / 10 units at 250/500/750d | 🚫 no single-number concentration claim |
| G5 | 🔴 universe **55 days** stale | 🚫 no cap weight / sector share / `top1_w%` as current |
| G6 | 🔴 accrual 0.57/day (1.75× slow) | `kelly_size --ic` = "mechanical 1/4" only |
| G7 | 🟡 51/53 `--help` clean; chart live 3/3 | 🚫 no `margin_history` output |

### §0-b · 🚨🚨 The instrument state CHANGED inside this stage, and PREFLIGHT could not have caught it

`PREFLIGHT` probed `yfinance` at **09:10 ET** and correctly recorded **no 2026-09-08 row** for
NVDA/SPY/AAPL/XOM. A second pull at **09:5x ET**, inside this stage, returns one:

| ticker | 2026-09-04 (settled) | **2026-09-08 (PARTIAL, intraday)** |
|---|--:|--:|
| SPY | 770.19 | **767.50** |
| LNG | 292.00 | **276.98** |
| EWG | 43.89 | **43.75** |

⇒ **This desk's run window straddles the US open.** Every tool called before ~09:30 ET sees a clean
settled frame; every tool called after it silently receives an **incomplete bar as the last row**, with
no error and no marker. `D74`'s intraday-truncation class is therefore not a property of *when the desk
chooses to look* — it is a property of **which stage you are in**. Registered as **`D577`**.

**Applied, not just noted:** every price computation in this report explicitly filters
`index <= 2026-09-04` before computing. The `D93` percentile tables in §D were computed under that
filter and the filter is stated on the same line as the numbers (`C5`).

⚠ **PREFLIGHT's G0 verdict is not wrong — it is TIME-LIMITED**, and nothing in the file said so.
That is the appendable half: a gate that asserts a property of a live feed needs the clock at which it
was true printed beside it. Handed back to `preflight` as part of `D577`.

---

## §A · Indicators — `[FRED]`, and the publication clock is again the first fact

### A-1 · 🚨🚨 `D427`'s stated cause is **REFUTED**, and the desk's own pre-commitment FAILED

The 09-06 and 09-07 runs both pre-committed that the H.15 block would hold through Labor Day **and lift
on the first business day after it**. `M1412` recorded the first half as a successful pre-commitment.
**Today is that first business day. The block did not lift.**

`module_macro_us --days 120 --json`, pulled fresh this run:

| carries **2026-09-04** | stops at **2026-09-03** | stops earlier |
|---|---|---|
| `breakeven_10y` (T10YIE) **2.35** | `us_2y` **4.34** · `us_10y` **4.77** · `real_10y` **2.42** · `fed_funds` 3.63 · `hy_oas` **2.65** · `ig_oas` **0.81** · `vix` **14.32** | `nfci` 08-28 · `dxy` 08-28 · `unemployment` 08-01 · `cpi`/`core_cpi`/`m2` 07-01 |

★ **And this run added the leg every prior run assumed rather than measured.** The module was
**bypassed entirely** and the FRED REST API queried directly for the raw series ids
(`observation_start=2026-08-28`, `observation_end=2026-09-09`):

| FRED series id | last observation |
|---|---|
| `DGS10` · `DGS2` · `DFII10` · `VIXCLS` · `BAMLH0A0HYM2` | **2026-09-03** |
| `T10YIE` | **2026-09-04** |

⇒ **The split is FRED-side, not a `module_macro_us` defect.** That leg has been assumed for nine
reproductions and is now measured. Filed as **`M1455`**.

**And the holiday explanation cannot survive the dates.** The block was **already present on
Saturday 2026-09-05** (the 09-05 run's own §A prints `DGS2` at 09-03 and `T10YIE` at 09-04) — a day
whose only intervening event was Friday's close. A federal holiday two days later cannot explain a
block that pre-dates it, and a full business morning has now failed to clear it.
⇒ **`D427`'s *observation* stands (nine reproductions); its *stated cause* is retracted.** Filed as
**`R147`**. The honest forward statement is that **this desk no longer has a working model of when
these three series unblock**, and must stop predicting it.

⇒ **`P121` · `P114` · `P125` are BLOCKED for a 6th consecutive run.** They settle at *"the first
`[FRED]` close covering 2026-09-04"*, and `DGS2`/`DGS10`/`DFII10` do not carry it. `HANDOVER §3e`
handed this stage an obligation to report **either way**; this is the report, and the answer is *still
blocked, and the reason we gave was wrong.*

⚠ **One caveat against over-reading `T10YIE`'s extra day.** `T10YIE` is defined as `DGS10 − DFII10`.
At 09-03 that is `4.77 − 2.42 = 2.35`, which is **exactly** the value stamped 09-04. So the extra day
may be a genuine 09-04 observation that happens to be unchanged, **or** a carried value under a new
date. **This stage cannot tell which**, and therefore does not treat `T10YIE`'s 09-04 stamp as one more
session of information (`C3` — the column is unknown, not zero).

### A-2 · The repricing's leg — recomputed from source, unchanged because nothing published

| series | `[FRED]` last | value | 5d | 20d | 1yr %ile |
|---|---|--:|--:|--:|--:|
| `us_2y` (DGS2) | 09-03 | **4.34** | +0.14 (08-27 4.20) | — | high end of the 120d frame |
| `us_10y` (DGS10) | 09-03 | **4.77** | +0.10 (08-27 4.67) | — | high end of the 120d frame |
| `real_10y` (DFII10) | 09-03 | **2.42** | +0.08 | — | — |
| `breakeven_10y` (T10YIE) | **09-04** | **2.35** | +0.04 | — | — |

★ **`real_10y` is quoted with `breakeven_10y` as required**: real **2.42** vs breakeven **2.35**. The
5-session move is **+0.08 real vs +0.04 breakeven** ⇒ **roughly two-thirds of the 10-year move is
REAL, not inflation compensation.** That is a growth/term-premium/supply signature, not an inflation
signature — and it is the same reading `P142` (front end, settles 09-11) and the 09-07 `TLT` row
(long end, settles 09-14) already bracket. **This stage does not re-bracket it** (`D343`).

### A-3 · Credit is quiet and it is quiet on the instrument, not on the narrative

| series | last | value | 5-session change |
|---|---|--:|--:|
| `hy_oas` (BAMLH0A0HYM2) | 09-03 | **2.65%** | 08-27 2.63 → **+2 bp** |
| `ig_oas` | 09-03 | **0.81%** | 08-27 0.79 → **+2 bp** |
| `nfci` | 08-28 | **−0.558** | six straight weekly readings easing: −0.538 → −0.544 → −0.549 → −0.553 → −0.556 → **−0.558** |

⇒ **Any risk-off claim in this run is cited against these three or labelled narrative-only.** All three
say the same thing: **financial conditions are still easing while the curve sells off.** ⚠ `D3`
applies — the **level** (`hy_oas` 2.65 near its 1-year low) and the **change** (+2 bp, mid-pack) are
different objects, and **`P128` is written on the change**, not the level.

### A-4 · Monthly series — lag stated, not hidden

`cpi` **332.813** and `core_cpi` **336.789** are the **July** prints (lag ~1 month; **August CPI does
not print until 09-11**). `unemployment` **4.1%** is August. `m2` **23,218.0** is July.
⚠ **`dxy` last carries 2026-08-28 — eleven days stale**, so no dollar claim in this report is made on
`[FRED]` `dxy`; the dollar reads below come from the news axis and are labelled `[news]`.

---

## §B · News — the only live axis. **Coverage is stated before anything is concluded.**

### B-0 · Coverage, stated first (the tail is NOT the coverage claim)

🚨 **`brief --date 2026-09-08 --scope foreign` returns `기사 0건 → 사건 0개`.** That is **not** a quiet
day — the foreign feed's 09-08 has barely begun at 09:2x ET. Reading it as silence would be exactly the
error `P4` forbids. **Every event read below is therefore taken from the last COMPLETE foreign day,
2026-09-07**, and is labelled as such.

`brief --date 2026-09-07 --scope foreign --body 2`:

| section | shown / total | what it means |
|---|---|---|
| `denominator.articles` | **1,720** → 279 events → **279 market / 0 non-market** | the corrected denominator (⚠ `D558`: the same day re-pulled later will read higher; this is today's maturity) |
| head (≥5 outlets) | 30 | |
| body (2–4 outlets) | **35 shown / 249** | **214 withheld** |
| tail (2 outlets) | **0 / 0** | genuinely empty |
| **single_source (1 outlet)** | 🚨 **15 shown / 365** | **350 withheld — and ALL 365 are UNSCORED** |
| excluded_nonmarket (nb > −3.0) | 0 / 0 | |
| subevents recovered (`└`) | **44** | |

🚨🚨 **A structural blind spot this desk has never written down.** The brief's own footnote reads:
*"1매체 중 365개는 **점수가 없다** (분류기는 한글 전용)"* — **the market/non-market classifier is
Korean-only, so on the US desk the entire single-source tier is unscored and only a random 15 of 365
are displayed.** That tier is, by this protocol's own L2, *"where FX, rates and bond primaries live"*.
⇒ **On the US runtime, 365 of 1,720 articles (21.2%) reach the desk as an unranked random sample of
15.** Any "nothing in bucket X" claim on this desk is bounded by that, and this report makes none
without the denominator attached. Registered as **`D578`**.

★ What the 15 visible singles did contain, which justifies the concern: *"WTI struggles to hold above
$90 despite material supply risk"* [fxstreet] · *"Is the ECB headed for a third hike?"* [hellenicsh] ·
*"Indian Shares Open Lower On US-Iran Tensions"* [nasdaq]. **Three macro primaries in a random 15.**

### B-1 · ★★★ The week's central event: a **synchronized** hiking repricing, and it is dated

This is not a Fed story with foreign decoration. Three central banks are in the same trade on the same
week, and the thread instrument shows it (`thread --days 7 --date 2026-09-07 --scope foreign`;
per-day denominators **09-01 858 · 09-02 944 · 09-03 879 · 09-04 732 · 09-05 291 · 09-06 271 · 09-07 279**):

| leg | thread tag + curve (outlets/day) | anchor lines |
|---|---|---|
| **ECB** | **REIGNITED**, 5 days, **4→6→2→9→5** | *"Euro area: Inflation jump supports ECB hike – Commerzbank"* (09-01) → *"Fed Rate Hike Impact on Markets and Bonds"* 22 articles/9 outlets (09-04) → *"European markets edge lower, **ECB decision in focus**"* 12/5 (09-07), with *"ECB rate decision: Five key questions for markets as energ…"* 5/3 beneath it |
| **Fed** | **living**, *"Dollar barely gets lift from boost in Fed hike expectations"* **2→2→4**; *"Stocks, Bonds Rise as **Fed-Hike Bets Ease on Waller**"* **6→3**; ENDED *"Fed's Waller says central bank's next rate move…"* peak 16 | ⚠ **both directions present in one week** (`C2`) — the hike bid and the Waller-driven fade |
| **BoJ / yen** | **REIGNITED**, 4 days, **9→3→5→5**; living *"Japanese Yen: BoJ hawks raise hike risk"* **3→5→2→2** | *"Japan's yen hits **strongest in seven months**"* (09-07) · *"Japan's August foreign reserves post **largest-ever drop** after…"* 7/6 · *"Japan PM Takaichi's reflationist aide projects Bank of Japan r…"* 5/4 |
| **the transmission** | **REIGNITED**, 5 days, **3→5→7→4→8** — *rising to its highest outlet count on the last day* | *"Global Bond Sell-Off Puts Investors on Edge"* [nytimes] → *"Why investors are getting worried about global bond markets"* → 11 articles/8 outlets (09-07) |

`theme-age --scope foreign`: **`Fed hike` 🟡ACCELERATING 2.09×** (7d avg 26.4, base 968) ·
**`bond selloff` 🟡ACCELERATING 4.18×** (7d avg 17.0, base 252) · `ECB` ⚪ECHO **1.38×** (base 2,128) ·
`yen` ⚪ECHO **1.23×** (base 5,807).

⇒ **[news]-grade proposition: the repricing is global and its fastest-accelerating expression is the
BOND SELLOFF term (4.18×), not the Fed term (2.09×).** That is consistent with §A-2's measurement that
two-thirds of the 10-year move is **real**, i.e. a supply/term-premium event rather than an inflation
event — and with `P143`'s carry-unwind channel.

### B-2 · ⚠ The other side, read BEFORE any conclusion (`C2`)

1. **Positioning is already maximally on the other side of this.** `[COT 2026-09-01]` **UST 10Y spec
   net −909,275 = the 9th percentile of its year** — the single most crowded-short reading on the
   board, and it got **more** short last week (−70,300 WoW). A bond selloff narrative accelerating at
   4.18× into a 9th-percentile short is the textbook squeeze setup, and this desk's rejected-signal
   table says **COT contrarian is REJECTED** — so this is recorded as **ammunition context, never as a
   direction** (`D6`).
2. **The Fed leg has a live counter-thread**: *"Stocks, Bonds Rise as Fed-Hike Bets Ease on Waller"*
   (6→3 outlets). The week contains both the hike bid and its fade.
3. **Credit refuses to confirm** (§A-3): `hy_oas` +2 bp over five sessions with `nfci` easing for six
   straight weeks. **A global rate shock that credit does not price is a rates event, not a risk
   event** — which is precisely the question `P124` was written to settle (09-18).

### B-3 · The oil complex: the **level** is escalating and the **US barrel is the laggard**

09-07 head, body-read where quoted:

| item | outlets | what it says |
|---|--:|---|
| *"Oil prices today: Crude rises as US-Iran strikes fuel fears"* | 32 articles / **13** | the day's largest cluster |
| └ *"Oil up, bitcoin down as **U.S. strikes Iranian crude carrier**"* | 3/3 | the dated cause |
| └ *"**OPEC+ keeps oil output targets unchanged for October**"* | 3/2 | ⚠ **not** a voider for `P126` (`M1363`), restated at D−1 |
| *"Iran, US Trade Tanker Attacks as Conflict Escalates"* | 9/6 | |
| *"**India's Crude Oil Benchmark Tops $100** as Middle East War Esc…"* | 6/6 | living thread **2→6** |
| *"**Asia Spot LNG Prices Hit 5-Month High as Hormuz Blockade…**"* | living **5→3→2→3→2** | |
| *"**European Gas Climbs on LNG Supply Concerns Ahead of Winter**"* | REIGNITED **9→3→2→3** | |
| *"**Shipping Fuel Shortage Looms as Refiners Prioritize Diesel**"* | 4/4 | the distillate leg, on the tape |
| *"South Korea, US agree on **more than $20 billion gas plant investment**"* | 5/5 | |
| **[single-source]** *"WTI struggles to hold above $90 despite material supply risk"* | 1 [fxstreet] | ★ the counter-observation, and it was **only** visible in the unscored tier |

**Settled prices** (`auto_adjust=False`, filtered to ≤ 2026-09-04): `CL=F` **91.48** (08-31 85.76 →
+6.67% in four sessions) · `BZ=F` **96.28**. `theme-age Hormuz` **⚪ECHO 0.78×** on a **10,568** base —
the term is saturated and decelerating for a 6th run **while the physical event escalates**.

⇒ **[news + price] reading: the scarcity is priced in the CHAIN — Indian benchmark >$100, Asia spot
LNG at a 5-month high, European gas climbing, diesel crowding out bunker fuel — while the US
benchmark, the thing every US E&P is levered to, "struggles above $90".** That is the surviving half
of `R135` (capacity scarcity, not feed-cost) expressed one link further down the chain, and it is what
`P145` below brackets. ⚠ `P126` (09-09) already brackets **barrel vs refining**; **nothing on this
board reaches gas / LNG**, and `D563` says the reason is that **not one of those names is in
`us_top300.csv`.**

### B-4 · ★★ Term sweep — and **`P141`'s falsifier ran and FALSIFIED it**

`fts search <term> --days 7 --scope foreign --count`, **phrase convention** (single unquoted argv —
this is the convention the 09-06/09-07 numbers used; the quoted/OR convention is printed beside it per
`D473`). **No share-normalised column is published** (`D557`/`R139`).

| term | **09-08 phrase** | 09-08 OR-convention | 09-07 phrase | **raw Δ** |
|---|--:|--:|--:|--:|
| `refinery` | **324** | 324 | 288 | ★ **+12.50%** |
| `yen` | **935** | 935 | 859 | ★ **+8.85%** |
| `tariff` | **1,757** | 1,757 | 1,649 | ★ **+6.55%** |
| `bond selloff` | 142 | 271 | 137 | **+3.65%** |
| `diesel` | 300 | 300 | 291 | **+3.09%** |
| `payrolls` | 651 | 651 | 640 | +1.72% |
| `inflation` | 2,980 | 2,980 | 2,984 | −0.13% |
| `rate hike` | 1,382 | 1,746 | 1,389 | −0.50% |
| `AI capex` | 100 | 420 | 101 | −0.99% |
| `data center` | 2,361 | 3,053 | 2,387 | −1.09% |
| `Treasury yield` | 763 | 1,199 | 775 | −1.55% |
| `crude oil` | 803 | 1,324 | 817 | −1.71% |
| `Strait of Hormuz` | 1,013 | 1,027 | 1,040 | −2.60% |
| `rare earth` | 159 | 214 | 166 | −4.22% |
| `Federal Reserve` | 1,315 | 1,474 | 1,377 | −4.50% |
| `Venezuela` | 420 | 420 | 461 | **−8.89%** |
| `credit spread` | 48 | 317 | 56 | 🔻 **−14.29%** |
| `gas turbine` | 64 | 97 | 78 | 🔻 **−17.95%** |

**Raw dispersion 30.45pp · median −1.04% · 7 of 18 UP, 11 down.**

🚨 **`P141` is scored, and it is falsified by its own test.** `P141` (registered 09-06) attributed the
09-06 run's *"17 of 17 terms fell"* to a **truncated final day** and pre-registered a re-run *"on a
window ending on a full weekday — next opportunity 2026-09-08"*. This run is that opportunity, and the
result is the opposite of the prediction **twice over**:
1. today's window ends on **09-08, a day with ZERO articles in the pool** — i.e. **maximally
   truncated**, more so than 09-06 — and the decline is **not uniform**: 7 terms rose, dispersion
   30.45pp, median −1.04%. A truncation artifact cannot produce `refinery +12.5%` and
   `gas turbine −18.0%` in the same window.
2. `D557`/`R139` had already superseded its **diagnosis** on independent grounds one run earlier.
⇒ **`P141` = `FIRED-against-its-own-hypothesis`.** The uniform 09-06 decline was **not** a truncation
artifact; whatever produced it, this test rules out the cause `P141` named. Filed as **`M1456`**.
⚠ Its **observation** (17/17 fell on 09-06) is still not explained, and this stage does not invent a
replacement cause.

★ **And the ranking is coherent with §B-1/§B-3 measured independently**: `refinery` · `diesel` at the
top with `Shipping Fuel Shortage` on the head tape; `yen` at +8.85% with the yen at a 7-month high;
`tariff` +6.55%; `Venezuela` **−8.89%, a second consecutive decelerating run** (`theme-age` 2.95× →
2.47× → and now raw −8.89%), which is a **carried warning against `P139`'s driver**, stated but not
scored (`D242`). `credit spread` **−14.3%** agrees with §A-3's instrument reading — this is the one
"quiet" claim in the report and it is made on **two independent instruments**, not on a sweep zero.

⚠ **`C5`/`D473` unchanged and now larger**: the two conventions disagree by up to **6.6×**
(`credit spread` 48 vs 317; `AI capex` 100 vs 420). Every Δ above is the **phrase** read.
⚠ **A method error this stage made and caught** — see §F-4.

### B-5 · Trajectories — and today the instrument is structurally unusable at this desk's clock

`thread --days 7 --scope foreign` **ending on today (the default)** returns:
**`다일 395 — 살아있는 0 · 원데이 2314, 그중 오늘 신규 0`.**
**Zero living threads, 395 ENDED.** The cause is mechanical: a thread counts as living only if it has
an article on the window's last day, and **the last day has 0 articles** (§B-0). ⇒ **every FADING/ENDED
tag the default invocation produced today is an artifact of the desk's pre-open clock, not of
attention.** This is `D572`'s (HANDOVER) second expression and it is filed together with it.

**Workaround applied and reported**: the window was shifted with `--date 2026-09-07`, which yields
**505 multi-day threads, 99 living, 177 new today** — a usable instrument. **All trajectory claims in
this report come from the shifted window and say so.** Any run that reads the default output at this
clock will conclude "the entire news board went quiet", which is false.

### B-6 · Blind-spot pass — run, and its null is denominator-bound

`blindspot --scope foreign` over the full pool (**331,582** articles, random sample 400).
Token-0 emergent words are all saturated generics (`AI` 25,250 · `Earnings` 23,274 · `Trump` 9,750 ·
`Iran` 9,132 · `China` 8,625 · `Fed` 7,348 · `Nvidia` 5,677 · `Oil` 5,373 · `SpaceX` 5,003).
⇒ **no new macro term is folded into the table from this pass** — the instrument is running against
*all time*, so a term that is hot **this week** cannot rank against a 90-day-plus base. **This is a
specification limit, not an absence** (`C3`), and it is the same shape as `D559`'s `theme-age` age-leg
finding. The one non-generic line worth carrying from the random sample:
*"NY Fed survey finds highest credit application rate in nearly five years"* [google_en/Reuters] —
which is **the exact narrative the 2026-07-21 run built a credit-stress stack on and `hy_oas` refuted**.
Recorded so it is not re-bought (`R`-ledger discipline); §A-3 governs.

### B-7 · What else the 09-07 tape carried that this desk had no row for

| item | outlets | why it is here |
|---|--:|---|
| **AfD wins a German state election** — *"Merz to respond as Germany's far-right AfD wins key state el…"* · *"AfD Win Spells Economic Disaster, **Germany's DIW** Says"* · *"'Turning point for our country'"* | 26 articles / **13** | **`theme-age AfD` = 🟡ACCELERATING **8.73×**, age 78 — the FASTEST-accelerating term this stage measured, by 2.1× over the next one.** Nothing on this desk brackets Europe |
| *"**German Industrial Production Contracts** on Auto Sector Woes"* + *"Volkswagen finds **defense role** for German factory as auto j…"* | 8/5 | the real-economy leg beneath it |
| *"Germany news: **Explosive devices found near power plant**"* + *"Germany says Russia preparing 'hybrid' attacks" (ENDED, peak 20)* | | the security leg |
| **`Thailand pauses ALL datacenter builds and approvals`** | REIGNITED | ★★ **the SECOND jurisdiction to halt data-center interconnects**, after Texas's "ghost demand" halt that `P123` disclosed as counter-evidence at registration. `P123` settles **today** |
| *"China injects over €45 billion into state banks and insurers"* | BUILDING **3→7** | |
| *"The Stock Market Has Not Been This Expensive Since the Dot-com…"* cluster (+ *"Flashing a Warning Seen Only 6 Times"*, *"A Once-in-a-Generation Market Warning Just Flashed"*) | 18 articles / 4, three sub-clusters | valuation-anxiety cluster, `[news]` grade only |
| *"AMD's Whole AI Story Has One Threat It Cannot Ignore: **Broadcom**"* | 7/3 | `AVGO`-relevant on the day `S127` settles |
| *"Nvidia to Acquire Hugging Face for $12.9 Billion"* | ENDED, **peak 28** | `S130`'s thread. The 09-07 run recorded it **REIGNITED 15→2→4**; on the shifted window it now reads **4→28→9→2→2 = ENDED**. Status change recorded, **row untouched** (`D242`); `S130` settles 09-10 |

---

## §C · Positioning — `[COT report date 2026-09-01, Tue-close, released Fri 09-04]` + `[FINRA 09-04]`

| instrument | net spec | WoW | 1yr %ile | read |
|---|--:|--:|--:|---|
| **UST 10Y** | **−909,275** | **−70,300▼** | 🔴 **9%** | the board's extreme. **Crowded-short into an accelerating selloff narrative** |
| UST 2Y | −882,518 | −21,222▼ | 71% | 🟡 |
| **Nasdaq-100** | **+27,077** | **+15,951▲** | 🟢 **82%** | **crowded-long, and it got there in one week** (the largest WoW build on the board) |
| S&P 500 | −75,941 | −7,947▼ | 63% | 🟡 |
| Russell 2000 | −14,741 | +1,377▲ | 🔴 17% | crowded-short |
| **Copper** | +80,869 | −4,397▼ | 🟢 **100%** | **`C24`, 11th consecutive run at the top of its year** |
| WTI | +35,574 | +4,475▲ | 🟡 **70%** | ⚠ **`P122`-A needs ≥65 at the 09-08 COT** — this is the **09-01** reference and it reads 70. **Context, not a score** |
| Nat Gas | −208,911 | −10,979▼ | 🔴 0% | maximally crowded-short **into** the Asia-LNG/European-gas squeeze of §B-3 |
| Gold / Silver / USD | +228,124 / +26,739 / +17,025 | | 50% / 44% / 70% | 🟡 |

★ **Two extremes point the same way and this desk may not trade either** (`D6`, COT contrarian is
REJECTED): **UST10Y at the 9th percentile** and **Nat Gas at the 0th** are both maximally short into
narratives that are accelerating against them. Recorded as **ammunition context**.

**`[FINRA]` daily short-volume z, the 11 US holdings, 2026-09-04:**

| name | short% | base20 | z | 5v5 |
|---|--:|--:|--:|--:|
| **NUE** | 74.9% | 50.3% | 🔴 **+2.70** | **+19.9▲** |
| **ETN** | 72.6% | 52.5% | 🔴 **+2.16** | −4.6▼ |
| HPE | 52.2% | 46.0% | +0.53 | **+21.3▲** |
| MET | 56.4% | 48.5% | +0.78 | +13.1▲ |
| AVGO | 26.8% | 33.4% | −0.84 | **+10.9▲** |
| MPC / NDAQ / ANET / RTX / PSX / NVDA | 62.3 / 45.7 / 53.5 / 38.8 / 51.9 / 35.3% | | +0.43 / +0.60 / +0.54 / −0.18 / −0.36 / −0.51 | all 🟡 |

⇒ **Two names at extreme short pressure, and they diverge**: `NUE` is z **+2.70 with the trend still
building (+19.9▲)**; `ETN` is z **+2.16 with the trend already easing (−4.6▼)**. Same headline colour,
opposite direction of travel — stated on the line so the two are not averaged.

---

## §D · Propositions registered this run — `P145` · `P146`

> Thresholds from **`D93` measured percentiles**, computed this run on a frame **filtered to
> `index <= 2026-09-04`** (§0-b), `auto_adjust=False`, benchmark named inline (`C1`).
> ⚠ **No implied move is available for either observable** — neither basket has a listed straddle
> covering the window. Labelled `implied-move UNCHECKED` rather than claimed as "outside the priced
> move" (`C3`, the `S141` precedent).

### `P145` — ★★★ The oil scarcity is in the GAS/LNG chain, and this desk cannot even see the names

**Claim.** §B-3: `CL=F` **91.48** *"struggles above $90"* [fxstreet, single-source] while **India's
crude benchmark tops $100** (living thread 2→6), **Asia spot LNG hits a 5-month high on the Hormuz
blockade** (living 5→3→2→3→2), **European gas climbs on LNG supply concerns ahead of winter**
(REIGNITED 9→3→2→3), and Korea and the US sign **>$20bn of gas-plant investment** (5 outlets).
`refinery` is the term sweep's **top riser (+12.5%)** and `diesel` is 5th (+3.1%).

| field | value |
|---|---|
| **Frozen observable** | **`EW{LNG, GLNG, FLNG}` 5-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, window **2026-09-04 close → 2026-09-14 close** (the 5 sessions 09-08, 09-09, 09-10, 09-11, 09-14) |
| **A (the chain is where the scarcity is priced)** | excess **≥ +3.423pp** (trailing-252 **p85**) |
| **B (it was a headline, and the US barrel was right to lag)** | excess **≤ −3.628pp** (trailing-252 **p15**) |
| **C** | between — **the disclosed favourite** |
| **`D93` before freezing** | trailing 252 settled 5-session windows to 2026-09-04: mean **+0.072** · sd **3.898** · p05 −5.441 · **p15 −3.628** · p50 +0.144 · **p85 +3.423** · p95 +5.512 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **+2.276 = the 74.2nd percentile** (20-session excess **+6.96**) — ★ **it enters leaning toward A, disclosed now rather than discovered at scoring.** ⇒ **B is the informative branch** (`L3`): B says the gas leg was a headline and the desk's Energy OW is correctly positioned in refining rather than gas |
| 🚨 **Why this row exists at all — it is `D563` made scoreable** | **Not one of `LNG`, `GLNG`, `FLNG` is in `data/us_universe/us_top300.csv`.** They carry **no flow score, no OBV, no RS, no velocity** in any sweep this desk runs. `D563` called this *"a scoring exposure, not only a measurement one"* — this row converts an unmeasurable cycle into a **settled-price** observable that needs no universe membership. **If it fires A, the universe defect has cost the desk a measured cycle** |
| **Anti-signal (VOID)** | an **announced acquisition of any of the three**, a **trading halt ≥1 full session** in any of them, or a **Strait-of-Hormuz reopening statement confirmed by ≥3 outlets** inside the window (the last is `catalyst_calendar`'s own undated 🔀binary, so it is named rather than improvised at scoring) |
| ⚠ **Post-registration evidence, disclosed and NOT used to re-band (`D242`)** | the **partial** 09-08 intraday bar (§0-b) has `LNG` at **276.98 vs 292.00** = **−5.1%**, i.e. day 1 opens **against** branch A. **This is an incomplete bar and is explicitly not a score**; it is recorded so it cannot be presented as foresight later |
| **Track KPI** | `theme-age LNG` **⚪ECHO 1.18×** today; under A it should clear 2× |
| **Non-redundancy (`D343`)** | `P126` (09-09) is **barrel vs refining** inside `us_top300`; `P139` (09-14) is the **Venezuela** leg; `P140` (09-11) is the **crack rate vs level**. **None reaches gas or LNG, and none can — the names are not in the universe** |
| **Implied move** | **UNCHECKED** — no straddle covering 09-14 was retrievable for a 3-name equal-weight basket |
| **Owner** | `industry_US` |

### `P146` — ★★ The German political shock: the board's fastest-accelerating term, and no row on this desk touches Europe

**Claim.** §B-7: the AfD wins a German state election (26 articles / 13 outlets), **DIW calls it an
economic disaster**, **German industrial production contracts**, explosive devices are found near a
power plant, and the ECB decides **09-10** with a *"third hike"* question live in the single-source
tier. **`theme-age AfD` = 🟡ACCELERATING 8.73×, age 78 — 2.1× faster than the next-fastest term this
stage measured (`bond selloff`, 4.18×).**

| field | value |
|---|---|
| **Frozen observable** | **`EWG` 5-session excess return vs `SPY`**, settled closes, `auto_adjust=False`, window **2026-09-04 close → 2026-09-14 close** (5 sessions; **the ECB decision 09-10 and the US CPI print 09-11 are both INSIDE the window**, deliberately) |
| **A (political risk is repriced in German equity)** | excess **≤ −1.807pp** (trailing-252 **p15**) |
| **B (an election headline the market ignores)** | excess **≥ +1.482pp** (trailing-252 **p85**) |
| **C** | between — the disclosed favourite |
| **`D93` before freezing** | trailing 252 settled 5-session windows to 2026-09-04: mean **−0.224** · sd **1.626** · p05 −2.891 · **p15 −1.807** · p50 −0.127 · **p85 +1.482** · p95 +2.196 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−1.679 = the 18.7th percentile** (20-session excess **+0.10 = flat**) — ★ **already just outside branch A.** Disclosed now, not at scoring. ⇒ **B is the informative branch** (`L3`): B says an 8.73×-accelerating political term produced **nothing** in the priced asset, which would be a direct measurement against this desk's habit of promoting narrative velocity |
| **Information content (`B4`)** | **A** gives the desk its first European risk row and makes the ECB decision a live input to the `RE`/`STPL`/`UTIL` duration cluster. **B** falsifies `theme-age` acceleration as a cross-asset signal at its most extreme reading on the board — **which is the more useful outcome**, because this desk has cited `theme-age` acceleration in support of propositions **for 15 consecutive runs without ever bracketing it** |
| **Anti-signal (VOID)** | an **unscheduled ECB action or emergency statement**, a **German federal government collapse or snap-election call**, or a **market-wide trading halt**, inside 09-04 → 09-14. ⚠ Base rate pre-stated: a *state* election result is **not** a voider — it is the event |
| **Track KPI** | `theme-age AfD` 8.73×; under B it falls back inside 3× while `EWG` is unmoved |
| **Non-redundancy (`D343`)** | the 09-14 cell carries `S133`, `S148`, `S146`, `S150`, `P139` and the 09-07 `TLT` row. **Every one of them is a US object.** `P146` is **the only non-US-equity row this desk has ever registered**, and the `TLT` row's ECB exposure is via the **US long end**, not via European equity |
| **Implied move** | **UNCHECKED** — `EWG`'s listed straddles do not cover the 09-14 window |
| **Owner** | `industry_US` |

### 🔀 Catalyst injection — **`catalyst_calendar --days 10`** (`CATALYST_WATCH.json` saved to the day-folder root)

| when | event | axis | source |
|---|---|---|---|
| **D−2 · 2026-09-10** | **US Aug PPI** | inflation | `[bls✓]` |
| **D−3 · 2026-09-11** | **US Aug CPI** | inflation | `[bls~est]` |
| **D−8 · 2026-09-16** | **FOMC decision + SEP / dot plot** | rates | `[fed✓]` |
| undated | Iran "Strait of Hormuz open" statement (TACO trigger) | oil | `[news👁]` |
| D−10 · 2026-09-18 | S&P quarterly rebalance = quadruple witching | market | `[derived≈]` |

🚨 **`PPI 2026-09-10 08:30 ET is now INSIDE 48 hours of this run** (which fired 09-08 09:1x ET).
Per the protocol's US runtime delta, **PREMORTEM must produce a both-sides bracket for it** — a one-way
tilt into a known binary is a protocol violation. ⚠ The desk has **dropped PPI on information grade
(`B4`) for four consecutive runs, BY DECISION**. That decision was taken when PPI sat **outside** the
48h rule. **This is the first run in which the mandatory rule and the standing decision collide, and
PREMORTEM must resolve it explicitly rather than inherit the drop.** Handed forward by name.

🚨 **`D562` reproduces**: the calendar names US PPI, US CPI and the FOMC and **omits the ECB decision
on 2026-09-10**, which §B-1 shows is the week's most-covered scheduled event in the foreign pool.
**`P146`'s window is built to contain it anyway.**

🚨 **`D560` reproduces**: the EARNINGS block prints *"(none in window / yfinance unavailable)"* while
`yfinance` queried directly in this stage returns **`ORCL` 2026-09-10 16:00 ET** and **`ADBE`
2026-09-10 16:00 ET** — both inside the window. ⇒ **2026-09-10 carries US PPI ∧ the ECB decision ∧ an
ORCL+ADBE double print.** Three binaries on one day, of which the desk's own calendar surfaces one.

⚠ **`D507`**: `catalyst_calendar` still has no US market-holiday table. **2026-09-07 was Labor Day**,
so every "D−n" above is a **calendar**-day count, not a session count. Corrected session counts from
09-08: PPI **+2 sessions**, CPI **+3**, FOMC **+6**, rebalance **+8**.

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each. **This is ROTATION's input.**

> **Wind direction only, not a ranking.** `exc1/5/20` are **equal-weight `us_top300` constituent
> baskets, excess vs `SPY`** (benchmark named inline, `C1`), **recomputed this run from this run's own
> price frame, filtered to `index <= 2026-09-04`** (§0-b). **`breadth5` = names with positive 5-session
> excess.** ⚠ **Flow columns are the 09-03 → 09-04 change** and may not be read as today's (G2).

| # | sector | wind | driving row | eqflow / wflow | Δflow (09-03→09-04) | exc1 | exc5 mean/med | breadth5 | exc20 mean/med | note |
|---|---|---|---|---|--:|--:|---|--:|---|---|
| 1 | **Energy** | **OW** | **`P126`(09-09)** · `P140`(09-11) · `P139`(09-14) · ★**`P145`(09-14, new)** | **+0.562** / +0.440 | +0.054 | −0.27 | **+1.89 / +1.44** | ★ **15/16** | ★ **+12.29 / +11.52** | Still the board's only unambiguous OW: positive on every cut, **breadth 15 of 16**, `exc20` median +11.52. ★ **New this run: the tape says the scarcity moved DOWN the chain** — Indian benchmark >$100, Asia LNG 5-month high, European gas climbing, `refinery` the term sweep's top riser **+12.5%** — while `CL=F` "struggles above $90". **`P145` brackets the leg the universe cannot see** |
| 2 | **Health Care** | **N+** | `S133`(09-14) | **+0.190** / +0.098 | −0.043 | −0.44 | **+0.63 / +0.98** | 20/32 | **+3.63 / +3.74** | Positive on every cut, **median above mean on both windows ⇒ broad, not carried**. The only other positive `eqflow`. Unchanged, because the price data is unchanged |
| 3 | **Information Technology** | **N** | `S140`(09-08) · `S148`(09-14) · `P142`(09-11) | −0.195 / −0.090 | −0.010 | **+1.52** | −0.27 / **+0.27** | 30/56 | −0.99 / −1.82 | ⚠ **The cuts disagree and that IS the reading**: `exc5` mean −0.27 vs median **+0.27**, 30/56 positive ⇒ a few large names dragging. **`D566`: dispersion/move = 4.6× ⇒ there is no sector-level fact here to attach a verdict to** — 8th consecutive run this bucket is left at N. `S140` settles the breadth question **at tonight's close** |
| 4 | **Financials** | **N** | **`P128`(09-08)** · `S142`(09-11) · `P142` | **−0.023** / −0.118 | −0.004 | −0.58 | −0.07 / **+0.09** | 26/47 | **+1.92 / +1.04** | Flat on flow, positive on 20 sessions with median > 0. `eqflow` −0.023 is the citable cut (G5). **`hy_oas` at 2.65 near its 1-year low with `nfci` easing six straight weeks remains the strongest fact FOR the bucket** — and `P128` settles on the **change** (+2 bp), not the level (`D3`). ⚠ `D427` blocks it a 6th time |
| 5 | **Utilities** | **N−** | `S135`(09-11) · `S146`(09-14) | **+0.050** / +0.071 | −0.037 | +0.43 | +0.35 / **−0.13** | 7/15 | −1.36 / −1.17 | ⚠ Positive flow, negative price, mean-vs-median disagreement — the least internally consistent bucket. 🚫 sweep breadth is a `vol_surge` artifact (`D537`→`D561`), **and `theme-age` measured 0 of its names ⇒ no "quiet" claim admissible.** ★ New tape input: **Thailand halts ALL data-center builds** — a **second** jurisdiction after Texas. `D566`: dispersion/move ≈ **23×** |
| 6 | **Materials** | **N−** | **`P102`(09-09)** | −0.107 / −0.025 | −0.037 | +0.26 | −1.13 / **−2.44** | **3/12** | −0.85 / **−2.99** | Negative on both cuts, **median far below mean** ⇒ two names carrying the label (`C24`, **9th run**). **Copper COT 100th pctile, 8th consecutive run** — but on **09-01** data. `rare earth` **−4.2% raw**. `P102` settles the two-name question 09-09; not pre-empted (`D343`) |
| 7 | **Consumer Staples** | **UW** | `S135`(09-11) | −0.098 / −0.182 | −0.018 | −0.66 | −1.39 / **−2.29** | 7/19 | +0.03 / −1.94 | Negative on flow and 5 sessions with median below mean. `D512`: likely a **duration** leg, not a staples verdict — and §A-2 says two-thirds of the 10y move is **real**, which is the duration mechanism |
| 8 | **Real Estate** | **UW−** | `S135`(09-11) · the 09-07 `TLT` row (09-14) | −0.124 / −0.116 | −0.020 | −0.43 | −1.31 / −1.10 | 🚨 **1/12** | −1.83 / −1.62 | Negative on **every** cut and **every** window; 1 of 12 positive on 5 sessions — the board's most internally consistent bucket, consistently bad. **`DGS10` 4.77 with two-thirds of the 5-session move REAL is the mechanism**, and the bond-selloff term is the fastest-accelerating rates term (4.18×) |
| 9 | **Industrials** | **UW−** | `S150`(09-14) | −0.354 / −0.379 | +0.082 | **+0.57** | −1.34 / −1.67 | 17/50 | 🚨 **−5.04 / −5.90** | **Worst 20-session basket on the board on both mean and median.** ⚠ The largest Δflow on the board (+0.082) sits here but it is the **09-03→09-04** change reported for the fourth time and is **not** evidence of a turn (G2). ★ New tape: *"Volkswagen finds **defense role** for German factory"* + *"Japanese banks in a bind over **defense investments**"* — the defense re-rating is happening **outside** the US names `S150` brackets |
| 10 | **Consumer Discretionary** | **UW** | — | −0.280 / −0.255 🚫 | −0.004 | −0.25 | −2.38 / **−2.95** | 7/28 | 🚨 **−4.11 / −5.27** | 🚫 **`wflow` barred** (AMZN 40.2%, flag `True`). **`eqflow` −0.280 is the citable cut and it agrees with the sign** — negative on every price window with median below mean. Stated on the line as required |
| 11 | **Communication Services** | **no verdict issued** | — | **−0.035** / −0.389 🚫 | +0.007 | −0.97 | −1.85 / −2.22 | 🚨 **2/13** | **+1.27 / +3.70** | 🚫 **`wflow` barred entirely** — Alphabet **76.6%** under two tickers, ex-issuer +0.272, swing 0.661 (`D459`, **14th run**). `eqflow` **−0.035 = flat**; `exc20` median +3.70 vs `exc5` 2/13 ⇒ **the cuts contradict each other across windows. A sector this desk cannot aggregate is a sector this desk does not rank** |

★ **The matrix carries the same wind as 09-07 because it is computed on the same settled close** (G2 —
this is stated rather than presented as confirmation). **What changed is entirely non-price**: a
synchronized hiking repricing with the bond-selloff term at 4.18× (§B-1), the oil scarcity visibly
migrating down-chain to gas/LNG (§B-3), a second data-center-interconnect halt (§B-7), and the
board's fastest term (`AfD` 8.73×) sitting on a continent this desk has no row for — now `P146`'s.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 · Rows settled or scored this run

| row | settle | verdict | for/against the desk |
|---|---|---|---|
| **`S13`** | 07-29 (+10 sessions to 08-12) | ★ **`A-RULED-OUT · B/C AMBIGUOUS`** (HANDOVER §3c) | **neutral-negative** — the row's high-information branch is dead, and **two of its three legs were unmeasurable at settle**. A registration failure, not a market failure |
| **`P141`** | 09-08 (its own pre-registered falsifier date) | ★★ **falsified by its own test** (§B-4) | ★ **for the process** — the desk wrote a falsifier, ran it on the date it named, and the falsifier killed the hypothesis. `M1456` |
| `P121` · `P114` · `P125` | *first `[FRED]` close covering 09-04* | 🚨 **6th consecutive block, and the CAUSE is now retracted** (`R147`) | **against** — a pre-commitment this desk logged as a success (`M1412`) rested on a mechanism the dates refute |
| `S127` · `S140` · `P122` · `P123` · `P128` | **09-08** | **structurally unscoreable at this clock** (`D572`) | — |

### F-2 · Propositions carried, with their state

| row | settle | state today |
|---|---|---|
| `P122` (oil supply vs positioning) | 09-08 | branch **B** requires a **−12.55% single-session close** on 09-08 ⇒ **arithmetically all-but-closed, formally open** (bound, not a score). Branch A's `[COT]` leg does not publish until ~09-11 (`D573`). Reference: WTI spec **70th pctile** on 09-01 data |
| `P123` (power vs compute) | 09-08 | ⚠ its disclosed counter-evidence **strengthened**: **Thailand halts all data-center builds**, a second jurisdiction after Texas. **Recorded at D−0, not argued at scoring** (`D242`) |
| `P126` (barrel vs chain) | 09-09 | OPEC+ kept October targets unchanged 09-06 ⇒ **NOT a voider** (`M1363`), restated at D−1. §B-3 says the chain is where the tape is |
| `P127` (power vs compute basket) | 09-10 | window closes on US PPI ∧ ECB ∧ ORCL+ADBE — **none is in its anti-signal list ⇒ not a voider**, recorded now (`D450`). ⚠ `D563`: **`TLN` and `NRG` are inside its basket and outside the universe** |
| `P128` (credit) | 09-08 | `hy_oas` 5-session change at 09-03 = **+2 bp**, inside C; level 2.65. **`D427` blocks the settle** |
| `P139` (Venezuela leg) | 09-14 | ⚠ its driver decelerated a **second** consecutive run: raw **−8.89%** (after −5.3%), `theme-age` 2.95× → 2.47×. Stated, not scored |
| `P140` (crack rate vs level) | 09-11 | consistent with branch A's premise: `refinery` is the term sweep's **top riser +12.5%** and `diesel` +3.1%, with *"Shipping Fuel Shortage Looms as Refiners Prioritize Diesel"* on the head tape. **Not a score** |
| `P142` (US front end) · `P143` (yen) · the 09-07 `TLT` row (long end) | 09-11 / 09-14 / 09-14 | all three point at §B-1's synchronized repricing. **`yen` is the term sweep's #2 riser (+8.85%)** and the yen is at a 7-month high — `P143`'s premise is live |
| `P144` (instrument) | — | **confirmed by this run's own method error** (§F-4) |

### F-3 · 🚨 What this stage asserted and then refuted, inside the same stage (`D48`)

1. ★★ **This stage's first term sweep ran all 18 terms in the wrong convention and would have
   published it as the phrase column.** The counts returned (`rate hike` 1,746 · `data center` 3,053 ·
   `credit spread` 317) are the **OR/argv** convention, and compared against the 09-07 **phrase**
   column they produce **`credit spread` +466%** and **`AI capex` +316%** — a fabricated "attention
   flooded into credit and AI capex" story. It was caught by a two-term control (`rate hike`
   unquoted = **1,382** vs quoted = **1,746**) before anything was written. **The wrong table is
   recorded here rather than deleted**, and the OR column is published beside the phrase column so
   the next run cannot repeat it. This is `D473`/`C5` reproducing **inside** the stage that cites it.
2. ⚠ **This stage's first thread read concluded from the default `thread --days 7` output that the
   news board had gone to zero living threads.** The shifted window (`--date 2026-09-07`) refuted it:
   **99 living threads, 177 new.** The zero was the desk's own pre-open clock (§B-5).
3. ⚠ **PREFLIGHT's G0 said "no 09-08 partial bar exists" and this stage found one 45 minutes later.**
   PREFLIGHT was not wrong; its verdict was **time-limited and did not say so** (§0-b, `D577`).

### F-4 · Digs registered by this stage

| id | dig |
|---|---|
| **`D577`** ★★★ | **A gate's verdict about a live feed is valid only at the clock it was measured.** This desk's run window **straddles the 09:30 ET open**: tools called before it see a settled frame, tools called after it silently receive a partial bar as the last row. **Prescription: PREFLIGHT prints the clock beside every feed verdict, and every price computation filters to the last settled session explicitly.** |
| **`D578`** ★★★ | **On the US runtime the entire single-source news tier is UNSCORED** — `brief`'s market/non-market classifier is Korean-only, so **365 of 1,720 foreign articles (21.2%) arrive as an unranked random sample of 15.** That tier is where FX/rates/bond primaries live (measured today: the WTI-vs-$90 counter-observation and the "ECB third hike?" line were both only there). |
| **`D579`** | **`blindspot` runs against the full pool (331,582 articles), so a term that is hot this week cannot rank against its own all-time base.** Its null is a specification limit, not an absence (`C3`) — same shape as `D559`. **Prescription: add a window argument, or read it only for structural gaps.** |
| **`R147`** (retraction) | **`D427`'s stated cause — "H.15 does not publish on a federal holiday" — is refuted.** The block was already present on **Saturday 09-05**, before the holiday, and survived the first post-holiday business morning. **The nine-reproduction observation stands; the mechanism does not, and the desk stops predicting the unblock date.** |
| **`M1455`** (measured) | **The FRED split is FRED-side, not a module defect** — proven by bypassing `module_macro_us` and querying the REST API for raw ids: `DGS10`/`DGS2`/`DFII10`/`VIXCLS`/`BAMLH0A0HYM2` all end **2026-09-03**, `T10YIE` ends **2026-09-04**. Assumed for nine reproductions, measured today. |
| **`M1456`** (measured) | **`P141`'s falsifier ran on the date it pre-registered and falsified it.** Window ending on a **0-article** day (maximally truncated) produced **7 of 18 terms UP, dispersion 30.45pp, median −1.04%** — not the uniform decline a truncation artifact predicts. |

---

## ✅ EXIT CHECK — MACRO

- [x] Catalysts injected (`--days 10`, because `SCENARIOS.md` carries ARMED dates to 09-30);
      `CATALYST_WATCH.json` saved to the day-folder root; **the ≤48h binary (PPI 09-10) is named and
      handed to PREMORTEM with the standing-drop collision stated explicitly.**
- [x] Narrative read in all four passes — **events** (`brief --body 2`, and the 09-08 zero identified
      as a clock artifact, so 09-07 was used), **trajectories** (`thread --days 7`, default output
      diagnosed as unusable and the window shifted), **18-term sweep** (both conventions), **blindspot**.
- [x] Indicators read: FRED primaries `--json` **plus an independent REST probe**, COT positioning,
      FINRA per-name short-vol. Daily anchor (09-07 MACRO) read.
- [x] **`tail = 0` is NOT treated as the coverage claim.** All three recovery sections quoted with
      shown/total: single_source **15/365** (🚨 and all 365 unscored — `D578`), excluded_nonmarket
      **0/0**, subevents **44**. The report's one "quiet" claim (`credit spread`) is made on **two**
      instruments, not on a zero.
- [x] **Denominator is the corrected one** (`1,720` after non-news exclusion) and its maturity caveat
      (`D558`) is stated.
- [x] Every proposition carries its thread's tag + curve; the `NVDA`/Hugging Face status change
      (REIGNITED → ENDED) is recorded with the row left untouched.
- [x] **No bucket's low count is trusted from a mis-passed CLI** — the convention error was caught by a
      control and both conventions are published (§B-4, §F-3).
- [x] **Both halves cited**: `real_10y` **2.42** with `breakeven_10y` **2.35** and the split of the
      5-session move (**+0.08 real vs +0.04 breakeven**); the oil complex cited with **both** the
      escalating chain prices **and** the lagging US benchmark.
- [x] **Every relative-performance number names its benchmark inline** (`SPY` throughout §D/§E).
- [x] **Credit axis read and cited**: `hy_oas` 2.65 · `ig_oas` 0.81 · `nfci` −0.558. No narrative
      risk-off claim is made without them.
- [x] Transmission matrix produced — **all 11 sectors, recomputed this run on a frame filtered to the
      last settled close**.
- [x] Self-backtest appended; two propositions scored (`S13` via HANDOVER, `P141` here); one
      retraction (`R147`) and three digs registered.
- [x] **`report_lint.py` run on this file — 0 findings** (rules C1, C2, S6, D6). ⚠ Form only; a clean run is not a correct report.

> P4 — this report sets **wind direction**. It issues no size, no order, and no buy/sell language.


---

# §5 · DRIFT ADDENDUM — appended 2026-09-08 by Stage 11 / L1·DRIFT (★ APPEND-ONLY — nothing above is rewritten)

> `scripts/drift_watch.py --report llm_outputs/2026-09-08/industry_US/MACRO_REPORT.md`, baseline
> **2026-09-08T22:47 KST**, +0.5h window. **5 burst candidates ≥3.0×. All five body-read, not counted.**

## D-0 · The instrument fired early, so its nulls carry little weight

The watch window is **0.5h**, not the 3–6h the stage specifies, because this run completed late in its
own slot. ⇒ a **quiet** reading here would prove nothing; the 🚨 readings still count, because a burst
that clears 3× inside half an hour is a burst.

## D-1 · Five bursts, body-read — **three are term artifacts, two are material**

| term | post-run count | vs normal | body-read verdict |
|---|--:|--:|---|
| `rate cut` | 10 | **21.8×** | ❌ **ARTIFACT.** Top hit is *"September Equity Style Box Returns"* [nasdaq/Zacks, 09-08 08:43 EDT] — a monthly style-box table. The other two are a Zacks screen and a single-name bull case. **No rate-cut news content.** |
| `default` | 8 | 9.2× | ❌ **ARTIFACT.** *"BigBear phishing crew nets thousands of Microsoft 365 credentials"* and *"Palo Alto vs. Zscaler"* — the term is matching **cybersecurity defaults**, not credit defaults |
| `downgrade` | 4 | 5.3× | ❌ **ARTIFACT.** *"SpaceX initiated, Intel upgraded: Wall Street's top analyst calls"* ×2 — a broker-call roundup |
| **`blockade`** | 3 | **4.2×** | ★ **MATERIAL** — see D-2 |
| **`Strait of Hormuz`** | 10 | 3.6× | ★ **MATERIAL** — see D-2 (its top hit is a Palantir headline, i.e. the term list is noisy, but hits 2 and 3 are the real ones) |

## ★ D-2 · The material finding: the disruption has a **SECOND chokepoint**, and this run's report did not have it

**Two articles, both body-read, both dated inside the watch window:**

**① *"Oil Tankers Flood Back Into Suez Canal As Red Sea Risk Grows"*** [oilprice, 2026-09-08]
- Suez Canal revenue **$505m in July, +42% YoY** (vs $355m July-2025, $438m June-2026); transits
  **1,340 vessels, +27% YoY**; **oil tankers 485 → 526** month on month.
- Mechanism, quoted: *"Saudi Arabia, which had **already re-routed most of its crude oil exports to the
  Western port of Yanbu on the Red Sea due to the Strait of Hormuz crisis**, had to **further detour**
  tankers north to the Suez Canal and a pipeline to… Sidi Kerir"* — after *"the Iran-aligned Houthis
  in Yemen announced **in July a blockade on Saudi shipments in the southern Red Sea and Bab
  el-Mandeb Strait**"*, with *"several **attacks** on Saudi tankers in the Red Sea"*.

**② *"Hormuz disruptions hitting small businesses hardest, UN trade agency warns"*** [Reuters/UNCTAD,
Geneva, 2026-09-08]
- 🚨 **"Brent crude prices were up more than 2% on Tuesday, above $99 a barrel."** This report's price
  frame ends at the settled **2026-09-04 `BZ=F` 96.28**; the live tape is **above $99**.
- *"After a month of calm in August, fighting in the Gulf resumed, with Iran and the U.S. exchanging
  fire, sending global oil prices back up to levels unseen since July."*
- ⚠ *"**Houthi attacks on southwestern Saudi Arabia** have the potential to deepen the economic impact
  of the conflict by disrupting Middle East energy supplies **beyond the blockaded Strait of Hormuz**."*

## D-3 · What this addendum changes, and what it explicitly does NOT

**CHANGES — one thing, and it is an anti-signal, not a threshold:**
🚨 **PREMORTEM §2a's correlated-hit trigger is now WRONG AS WRITTEN, and this is the correction.**
That section said a confirmed **Strait-of-Hormuz reopening** would take the gas leg, the refining
premium, the breakevens and the three duration underweights **at once**. The body-reads above show a
**second, independent chokepoint** — a Houthi blockade of the **southern Red Sea / Bab el-Mandeb**
with attacks on Saudi tankers and strikes on southwestern Saudi Arabia — which is **not cleared by a
Hormuz reopening**. Saudi crude is already routed *around* Hormuz via Yanbu and is being disrupted
*there*. ⇒ **the single-headline correlated hit is smaller than the desk wrote three stages ago**, and
`P145`'s VOID clause (*"a Strait-of-Hormuz reopening statement confirmed by ≥3 outlets"*) is now known
to be **a partial, not a complete, invalidation**.
★ This is recorded as a **stated weakening of an anti-signal**, exactly the class `M1363` established
with the OPEC+ non-voider — **and no threshold on any row is touched** (`D242`).

**DOES NOT CHANGE:**
- **No number in §A–§F is edited.** The settled frame is still **2026-09-04**; `BZ=F` **96.28** and
  `CL=F` **91.48** stay as written, and the ">$99 Brent" line above is labelled **live/intraday**, not
  substituted for them (`D577`).
- **No verdict moves.** `ENRG OW` stands where ROTATION put it; this addendum is evidence *for* the
  Energy chain thesis and ROTATION already declined to promote on news (macro re-argument).
- **No bracket is re-banded.** `P145` (09-14), `P122` (09-08), `P126` (09-09), `P140` (09-11) keep
  their registered thresholds.
- **`P122`'s branch-B bound is unaffected**: it needs a `CL=F` **close ≤ 80.00** on 09-08; Brent above
  $99 makes that arithmetically further away, not nearer, but the bound was already
  **−12.55% in one session** and remains formally open.

## D-4 · Registered from this addendum

| id | type | statement |
|---|---|---|
| **`M1457`** | measured | **The Middle East energy disruption has TWO chokepoints, not one.** Suez revenue **+42% YoY** with oil-tanker transits **485 → 526 MoM** because Saudi crude — *already* re-routed to Yanbu to avoid Hormuz — is being pushed further north by a **July Houthi blockade of the Red Sea / Bab el-Mandeb** and attacks on Saudi tankers. **A Hormuz reopening does not clear the second chokepoint** |
| **`D580`** | defect | **`drift_watch`'s term list produces a ~60% artifact rate at the 3× burst threshold** — measured today: `rate cut` **21.8×** was a Zacks style-box table, `default` **9.2×** was cybersecurity, `downgrade` **5.3×** was a broker-call roundup; **3 of 5 bursts had no relation to their term's intended meaning**, and the largest multiple was the emptiest. **Prescription: rank drift candidates by burst × body-read hit-rate, or narrow the terms (`credit default`, `rate cut expectations`) — a raw multiple on an ambiguous token is a false-alarm generator** |

## ✅ EXIT CHECK — DRIFT

- [x] `drift_watch` run against **this run's own** `MACRO_REPORT.md`.
- [x] **Every 🚨 item body-read, not counted** — 5 of 5, and the three artifacts are named with the
      article that produced them rather than dismissed as noise.
- [x] **§5 ADDENDUM appended, append-only.** Nothing above §5 is rewritten; the original call stands
      next to its correction, which is what the self-backtest eats.
- [x] The one thing that changed (**PREMORTEM §2a's correlated-hit trigger is incomplete**) is stated
      as a weakened **anti-signal**, with **no threshold on any registered row touched** (`D242`).
