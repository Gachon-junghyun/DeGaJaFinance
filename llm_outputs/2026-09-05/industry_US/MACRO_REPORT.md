# MACRO_REPORT — industry_US · 2026-09-05 (Sat) · Stage 3 / L1·MACRO

> `--market us` · every news call `--scope foreign` (hard rule). Primary macro = `[FRED]`.
> Run clock **KST 2026-09-05 22:2x → 23:5x = Sat 09:2x–10:5x ET. NYSE CLOSED.**
> Last settled US session **2026-09-04 (Fri, August payrolls)**, complete and settled.
> **Analytical output only — zero buy/sell recommendations (P4).**

## §0 · 🚨 Instrument state governing every line below (from `preflight/PREFLIGHT.md`)

| gate | what it grants / removes here |
|---|---|
| **G0** ✅ | OBV/flow citable from the **primary** `SECTOR_FLOW_US.json`; no `_REPAIRED` file exists. `EA` gets no verdict |
| **G1** 🔴 | 🚫 **no news-velocity or theme-freshness number from the sweep**, including its 49 scored names (they are the 49 largest caps). 🚫 **no "quiet sector" claim from sweep coverage.** ✅ direct `module_news_data` calls made outside a sweep burst ARE the required path and are what §B uses |
| **G2** ✅ | Δflow citable directly from the JSON — the 09-04 run's blanket revocation is lifted |
| **G3** ✅/⚠ | 🚫 no `wflow` verdict on **Cons. Disc.** or **Comm. Services** — `eqflow`/breadth only, named on the line |
| **G4** 🔴 | any concentration statement carries its `--days` and the 12/11/10 spread |
| **G5** 🔴 | 🚫 **no cap weight, sector cap share or `top1_w%` cited as current** (universe 52 days old). Where weighted and equal-weighted disagree, **equal-weighted is the citable one** |
| **G6** 🔴 | `kelly_size --ic` would be "mechanical 1/4"; not used in this stage |
| **G7** 🟡 | `module_chart` citable (live 3/3); `margin_history` not |

★ **One clock property removes a whole class of caveat.** Every run since 09-01 reasoned about
partial bars. **This one is a Saturday: 09-04 is settled and complete**, so `D74` intraday
contamination is structurally absent rather than merely checked.

---

## §A · Indicators — `[FRED]` primaries, and the leg the frame turns on has FLIPPED

### A-1 · The rate complex, both halves (`C2`)

`[FRED]`, all series at their **latest published** observation. ⚠ **They do not share one date.**

| series | latest | value | Δ1 obs | Δ5 obs | Δ21 obs | pctile of trailing 252 |
|---|---|---:|---:|---:|---:|---:|
| `us_2y` (DGS2) | **09-03** | **4.34** | −0.05 | **+0.14** | +0.16 | **97.6** |
| `us_10y` (DGS10) | **09-03** | **4.77** | −0.02 | +0.10 | +0.14 | **98.8** |
| `us_30y` (DGS30) | **09-03** | **5.25** | −0.02 | +0.06 | +0.08 | **96.0** |
| `real_10y` (DFII10) | **09-03** | **2.42** | −0.03 | +0.08 | +0.01 | **94.0** |
| `breakeven_10y` (T10YIE) | **09-04** | **2.35** | 0.00 | +0.04 | +0.09 | 66.7 |
| `fed_funds` (DFF) | 09-03 | 3.63 | 0.00 | 0.00 | 0.00 | — |
| `hy_oas` | 09-03 | **2.65** | −0.01 | +0.02 | −0.10 | **2.0** |
| `ig_oas` | 09-03 | 0.81 | 0.00 | +0.02 | +0.03 | 65.9 |
| `vix` (VIXCLS) | 09-03 | **14.32** | −0.88 | −0.19 | −1.49 | **2.4** |
| `nfci` (weekly) | 08-28 | **−0.558** | — | — | −0.093/21obs | — |
| `dxy` (DTWEXBGS) | **08-28** | 118.75 | — | — | — | ⚠ **7 days stale** |

★★★ **`M1283` [measured] — the leg of the repricing has FLIPPED from real to inflation, and it
crossed the distribution from one tail to the other in three observations.** The 3-session
(Δ`breakeven_10y` − Δ`real_10y`) spread, computed on the 274 joint dates:

| date | spread | percentile of trailing 252 |
|---|---:|---:|
| **2026-08-31** (the 09-02 run's `M1234`) | **−11.0 bp** | **5.2nd** |
| **2026-09-03** (latest joint date) | **+6.0 bp** | **88.5th** |

Trailing-252 reference (unchanged from `M1234`'s own computation, which reproduces exactly):
mean **−0.79** · sd **5.92** · p05 −11.0 · p15 −6.0 · p50 −0.0 · p85 **+5.0** · p95 +9.0.

🚨 **`+6.0 bp` is ABOVE `P125`'s branch-A line of +5.0 bp.** ⚠⚠ **`P125` IS NOT SCORED HERE.** Its
frozen observable is *"the first observation where **BOTH** series carry **2026-09-04**"*, and
`DFII10` stops at **09-03**. The number above is a **reference state, explicitly not a score**
(`D242`), and it is printed precisely so that the settle — whenever `DFII10` publishes — cannot be
influenced by having seen it. ★ **This is `P125`'s construction working as designed**: the row was
written knowing about `D427` and is therefore *unscoreable* rather than *mis-scoreable*.

⇒ **The carried frame — "the repricing is the POLICY PATH, not inflation" (`P121`, four runs) — is
now standing on the wrong side of its own falsifier's reference reading.** Nothing is retracted
(`P125` has not settled), but MACRO carries the frame forward **flagged**, not confirmed.

### A-2 · The curve's SHAPE on the payroll session says the OPPOSITE of the breakeven leg

`[FRED]` cannot answer this — `DGS*` stops at 09-03. Cross-provider (`D5`, stated as such):
**CBOE settled closes, 2026-09-03 → 2026-09-04 (the August payroll session).**

| tenor | 09-03 | 09-04 | Δ |
|---|---:|---:|---:|
| `^IRX` (13w) | 3.740 | 3.757 | +1.7 bp |
| **`^FVX` (5y)** | 4.509 | **4.550** | **+4.1 bp** |
| `^TNX` (10y) | 4.762 | 4.784 | +2.2 bp |
| `^TYX` (30y) | 5.243 | 5.246 | **+0.3 bp** |

★★ **`M1284` [measured] — the payroll session BEAR-FLATTENED, hard: 5y +4.1 > 10y +2.2 > 30y +0.3.**
That is `M1235`'s exact shape reproduced on the single most policy-relevant print of the month. A
term-premium / fiscal-supply event steepens the back end; this compressed it. **On the curve, 09-04
was a rate-HIKE-expectation session.**

★★ **`M1285` [measured] — and the curve is at its FLATTEST in a year.** `^TYX − ^FVX` = **69.6 bp**,
the **2.0th percentile of the trailing 252**. Its 4-session change is **−4.60 bp** (22.2nd
percentile), i.e. still flattening faster than typical.

⚠ **`C2`, and it is the run's central tension**: the **breakeven/real** decomposition (A-1) says the
marginal move is now **inflation**; the **curve shape** (A-2) says it is the **policy path**. Both
are printed. They are measured on different providers and different last dates (`[FRED]` 09-03 vs
CBOE 09-04) and **that alone could explain the disagreement** — which is why `P138` (§D) brackets the
shape leg on a forward window instead of adjudicating it here.

### A-3 · Credit still refuses to join — and it is now at the 2nd percentile

`[FRED]` 09-03: **`hy_oas` 2.65 = the 2.0th percentile** of trailing 252 · **`ig_oas` 0.81 = 65.9th**
· `NFCI` **−0.558** (08-28) and easing.

★ **`M1286` [measured] — three risk instruments are simultaneously at one-year extremes pointing in
opposite directions.** Nominal yields at the **96th–99th percentile**, `hy_oas` at the **2.0th**, and
`vix` at the **2.4th**. **Rates are pricing the most stress in a year; credit and volatility are
pricing the least.** ⇒ **Any risk-off claim in this run is barred from resting on narrative** —
`hy_oas` and `NFCI` both say the opposite, and this stage says so rather than hedging.
⚠ `P67`'s 2.85 `hy_oas` trigger sits **20 bp** away. `P128` (settles 09-08) is the row that tests
whether the global bond selloff reaches US credit; its reference state is **`hy_oas` +2 bp over five
observations**, i.e. the answer so far is *no*.

### A-4 · Per-name short pressure `[FINRA Reg SHO daily, dated 2026-09-04 — matches the settled bar]`

| 🔴 short-volume spike (z ≥ +1.5) | short% | base20 | z | 5v5 | that session's move |
|---|---:|---:|---:|---:|---|
| **`SMH`** | **71.6%** | 54.5% | **+2.99** | +2.7▲ | ★ **+2.61%** (a +3.00pp excess vs `SPY`) |
| **`NUE`** (held) | **74.9%** | 50.3% | **+2.70** | **+19.9▲** | −0.53% |
| **`ETN`** (held) | **72.6%** | 52.5% | **+2.16** | −4.6▼ | ★ **+3.46%**, the book's best name |

Others (🟡 normal): `MET` +0.78 · `NDAQ` +0.60 · `ANET` +0.54 · `HPE` +0.53 (5v5 **+21.3▲**) ·
`MPC` +0.43 · `RTX` −0.18 · `PSX` −0.36 · `XLE` −0.49 · `NVDA` −0.51 · `MU` −0.63 · `AVGO` −0.84.

★★ **`M1287` [measured] — the short-pressure sign INVERTED against the tape, which is the opposite of
what `M1237` measured three sessions ago.** On 09-01 the three 🔴 extremes were names that **fell**
(`ANET` −3.29%, `NVDA` −1.51%, `SMH` −2.05%) and the report read pressure as trend-confirming. On
09-04 **two of the three 🔴 extremes are names that ROSE hard** (`SMH` +2.61%, `ETN` +3.46%). Short
volume at 71.6% against a 54.5% base on a +2.61% session has two readings and this stage does not
choose between them: **(i) a squeeze** — shorts covering into strength inflates print-side short
volume little, so the elevated ratio is *new* shorting into the rally = distribution; **(ii) hedging**
— market-maker delta hedging against option flow, which `[FINRA]` cannot separate (`D6`).
⇒ **registered as `P137` (§D) rather than read.**
⚠ `NUE`'s **+19.9 5v5 trend on a 74.9% ratio** is the largest sustained build on the board and it is a
**held** name; recorded as a fact, resolved by ROTATION/DEEP, not here (P4).

---

## §B · News — `--scope foreign` on every call. Coverage is stated before anything is concluded.

### B-1 · Coverage accounting, because `tail = 0` is **not** a coverage claim

`brief --date 2026-09-04 --scope foreign --body 2`, corrected denominator:

| field | value |
|---|---:|
| `denominator.articles` | **4,531** |
| `clusters` | 1,323 |
| `events_2src_plus` (= `market_events`) | **705** |
| `excluded_not_news` | **{} — empty** |
| `head` (≥5 outlets) shown | **87** |
| `body` (≥2 outlets) shown | **618** |
| **`tail`** | **0** |
| `single_source` clusters | **618**, of which **shown 15** |
| `excluded_nonmarket` | **count 0** |
| `subevents_recovered` | **204** |

🚨 **`M1288` [measured] — two of the three mandated recovery tiers are STRUCTURALLY UNAVAILABLE in
the foreign scope, and the tool says so in its own note.** The `nb` classifier is **Korean-only**:
every one of the 618 `single_source` clusters returns `nb: None` (`scored: 0`, `scorable: 0`,
`unscored: 618`), so the foreign `single_source` tier is a **random 15-of-618 sample**, not the
"classifier top-scored" tier the EXIT CHECK is written for; and `excluded_nonmarket` returns
**count 0**, because nothing foreign is ever classified, so that tier is empty by construction rather
than because the day held no boundary-band events.
⇒ **Stated coverage: 87 + 618 + 15 + 204 = 924 of 1,323 clusters = 69.8%.** **603 single-source
clusters exist only as a count** and 0 of the non-market boundary band was reachable.
⇒ 🚫 **No "quiet bucket", "nothing happened in X", or "the market ignored Y" claim appears anywhere
in this report.** ★ Registered as **`D506`** (§D-5): *the domestic and foreign feeds do not have the
same recovery tiers, and a coverage claim written to the domestic spec overstates the foreign one.*

★ **And the random sample immediately paid for itself.** One of the 15 randomly surfaced
single-outlet clusters is
*"Micron, SanDisk Jump 4% Even as Hot Jobs Report Briefly Flips Fed Hike Odds Above 50%"* — a
**dated, quantified Fed-path fact at one outlet**, on the day the whole board turned on the Fed path.
It appears nowhere in head or body. (Others in the sample: *"Ex-RBA Official Expects September
Hike"*, *"Japan Has Not Done This Since 1990. If It Happens, the Cheap Money Propping Up US Stocks
Gets Expensive"* — **two more rate/carry items at one outlet each**.)

### B-2 · Events — the head, with denominators. **One print owns the day, and it is labour.**

| # | event | outlets | axis |
|---|---|---:|---|
| 1 | **US adds 162,000 jobs in August, beating expectations** (+ *"US jobs surge in August, putting rate hike firmly in play"*, *"Strong August jobs report sends yields higher"* [Reuters]) | **15 + 9 + 8** across three clusters | **rates/labour** |
| 2 | **The Commodities Feed: Oil maintains gains amid Persian Gulf escalation** (└ *"Oil set for steepest weekly gain since mid-July"*; └ *"Oil Price Today: Crude at **$96**, set for a **7% weekly surge** as Iran, US exchange attacks"*) | **21** | **oil** |
| 3 | **US diesel prices hit an all-time high** (└ *"Diesel price surges to all-time high, fueled by wars"*; └ *"...pushing up transportation costs for a long list of goods"*) | **10** | **refined product** |
| 4 | Russia hits Ukrainian security HQ in drone attack | 14 | geopolitics |
| 5 | Tesla launches steering-wheel-free Cybercab in Austin → *"US auto safety regulator evaluating"*, *"From Launch Party to Federal Probe in 24 Hours"* | 13 + 6 | CD/autos |
| 6 | **Nvidia's $13 Billion Hugging Face Deal Expands Open-Source AI** | **9** | AI/compute |
| 7 | *"Fed Rate Hike Impact on Markets and Bonds"* · *"German bond yields set for fourth weekly rise"* · *"The Bond Markets Are Pushing Up Rates. Will Central Banks Follow?"* | 9 | **rates/global** |
| 8 | **Trump says if the Fed doesn't cut rates, he'll stop trading with some nations** | 7 | policy/Fed |
| 9 | **China rare earth firms halt some US shipments over geopolitical worries** [Reuters] + **Pentagon rare earth push collides with China's grip** | 6 + 8 | materials/supply |
| 10 | **South Korea Paving Way to Send Troops to Hormuz** | 7 | oil/geopolitics |
| 11 | Volkswagen approves plan to cut another 50,000 jobs (└ 100,000 by end of decade) | 11 | CD/industrial |
| 12 | **US fuel production rose in August** | 7 | refining supply |
| 13 | Bloom Energy, Illumina, Everpure rise on **S&P 500 inclusion** | 5 | index/structural |
| 14 | **Japan warns against weak yen, stands ready to intervene** · **Japan's Katayama monitoring bond markets "with heightened urgency"** | 5 + 7 | **yen/JGB** |
| 15 | *"Yields, dollar rise, stocks ease after solid US jobs report"* · *"U.S. stocks down in final hour as jobs data raise chances of interest-rate hike"* | 5 + 5 | rates |

★ **`M1289` [measured] — the payroll print was a HIKE story in the wire copy, not a growth story.**
Of the three largest labour clusters, two carry rate-hike framing in their own headlines (*"putting
rate hike firmly in play"*, *"raise chances of interest-rate hike"*), and the single-source tier
carries the number: **Fed hike odds briefly above 50%.** ⚠ **Both halves (`C2`)**: the same day's
head also carries *"Labor Shock: 162,000 Jobs, But This Is No Hiring Boom"* and
*"The Nasdaq, S&P 500, and Dow All Fell Slightly Friday. The Jobs Report Wasn't Really Why."* — the
counter-reading is printed rather than dropped.
⚠ **What is NOT available**: the desk has no BLS release detail (revisions, participation, average
hourly earnings), so **only the headline 162k is cited and the sequential/revision half is
explicitly unread** (`C2` acknowledged as unmet, not faked).

### B-3 · Trajectories (`thread --days 7 --scope foreign`)

Per-day denominators: 08-30 **293** · 08-31 755 · 09-01 858 · 09-02 943 · 09-03 875 · 09-04 705 ·
**09-05 147**. 4,576 events → 3,525 threads (581 multi-day, 54 live).

⚠⚠ **The window ends on a SATURDAY with 147 articles against a 705–943 weekday run, and the tool's
own warning applies: every `FADING` tag in this table is inflated by that.** Every curve below is
therefore read **on its weekday legs**, with the Saturday bar named and discounted.

| thread | tag as printed | outlet curve | read on weekdays only |
|---|---|---|---|
| **Oil / Iran / Venezuela** (530 articles) | FADING | 19→22→22→19→13→**21**→4 | 🚨 **NOT fading — RISING into 09-04** (13 → **21**). The "4" is Saturday |
| **AI power demand / hyperscalers** (373) | FADING | 7→11→18→21→19→**13**→5 | genuinely decelerating on weekdays (21 → 13) |
| **Russia / Ukraine / Europe hybrid** (219) | FADING | 13→13→18→20→11→**14**→11 | flat-to-firm |
| **Trump "hit Iran hard" / US-Iran clashes** | REIGNITED | 5→2→9→3 | live |
| **US-Canada trade war** | REIGNITED | 3→8→2 | live, thin |
| **Asian refiners turn to Argentina as Iran war disrupts oil** | REIGNITED | 8→3 | ★ the *chain* leg of the oil story, alive separately from the barrel leg |
| **China grabbing memory market share** | REIGNITED | 2→3 | small, live |
| **Pentagon rare earth vs China's grip** | FADING | 3→8→2 | ⚠ 09-04 carried a **new** Reuters item (shipment halt) that has not yet joined the curve |
| **Tesla Cybercab → NHTSA probe** | REIGNITED | 2→2 | live |
| **Anthropic IPO shifts toward mid-October** | BUILDING | 2→6 | new, structural |

🚨 **`M1290` [measured] — an inherited "dead thread" label is wrong, and it sits under a live
bracket.** The 09-04 HANDOVER carries `S130` (`NVDA` / Hugging Face, settles 09-10) annotated
**"dead thread"**. The thread ran **4→28→9 with a peak of 28 outlets** (09-02→09-04) and is tagged
`ENDED` only because it compressed after the peak; the 09-04 head still carries it at **9 outlets**,
and `theme-age "Hugging Face"` reads **🟡ACCELERATING, 3.11×, base 1,022, age 74**. ⇒ **The "dead
thread" annotation is retracted (`R129`, §D-5). `S130` is a live row.**

### B-4 · Term sweep — **both conventions printed** (`D473`), 7d, `--scope foreign`

Windows are structurally comparable: this run's 08-30→09-05 and the 09-02 run's 08-27→09-02 each
contain exactly **two weekend days**.

| term | **phrase** | argv AND | 09-02 phrase | **Δ on the phrase read** |
|---|---:|---:|---:|---:|
| `inflation` | 3,149 | 3,149 | 3,481 | **−9.5%** |
| `data center` | 2,519 | 3,213 | 2,730 | −7.7% |
| `tariff` | 1,846 | 1,846 | 1,966 | −6.1% |
| `Federal Reserve` | 1,451 | 1,633 | 1,530 | −5.2% |
| **`rate hike`** | **1,380** | 1,751 | 1,223 | ★ **+12.8%** |
| `Strait of Hormuz` | 997 | 1,009 | 1,113 | **−10.4%** |
| `crude oil` | 847 | 1,352 | 993 | **−14.7%** |
| **`Treasury yield`** | **778** | 1,244 | 687 | ★ **+13.2%** |
| **`payrolls`** | **613** | 613 | 338 | ★★ **+81.4%** |
| `refinery` | 290 | 290 | 277 | +4.7% |
| `AI capex` | 105 | 431 | 116 | −9.5% |
| `credit spread` | 76 | 344 | 104 | **−26.9%** |
| `bond selloff` | 135 | 267 | (205 argv) | argv **+30.2%** |
| `gas turbine` | 88 | 118 | (116 argv) | argv +1.7% |
| 🆕 `rare earth` | 194 | 252 | — | new term |
| 🆕 `diesel` | 293 | 293 | — | new term |
| 🆕 **`yen`** | **857** | 857 | — | ★ new term, see B-6 |

★★ **`M1291` [measured] — the board's attention did not rotate, it CONCENTRATED.** Ten of the twelve
carried terms are **down 5–27%** week-over-week on the phrase convention, while `payrolls` is
**+81.4%**, `Treasury yield` **+13.2%** and `rate hike` **+12.8%**. The total foreign article count
was **higher** in this window than the last (4,576 events), so this is not a denominator effect: the
labour/rates axis took share from everything else.
★★★ **And the sharpest divergence on the board is oil.** `crude oil` **−14.7%** and
`Strait of Hormuz` **−10.4%** — **on the week WTI printed $96 with a 7% weekly surge, US diesel hit an
all-time high [10 outlets], and the oil thread's own weekday outlet count went 13 → 21.**
⇒ **The narrative is leaving the barrel while the physical print is going vertical.** This is the
proposition (`P136`, §D).
⚠ `C5`/`D473`: the two conventions disagree by up to **4.5×** (`credit spread` 76 vs 344). Every Δ
above is on the **phrase** read, which is the convention the 09-02 table's own numbers match; the
argv column is printed beside it rather than chosen between.

### B-5 · Novelty (`theme-age`, 90d, `--scope foreign`)

| theme | verdict | age | 7d avg | **accel** | base | vs 09-02 |
|---|---|---:|---:|---:|---:|---|
| **`Larak`** | 🟡ACCELERATING | 40 | 28.1 | **84.43×** | 210 | 72.47× → **84.43×** |
| **`bond selloff`** | 🟡ACCELERATING | ≥90 | 19.1 | **5.80×** | 243 | 3.81× → **5.80×** |
| **`Hugging Face`** | 🟡ACCELERATING | 74 | 43.7 | **3.11×** | 1,022 | not measured |
| `payrolls` | ⚪ECHO | ≥90 | 82.7 | 1.89× | 2,628 | new |
| `rate hike` | ⚪ECHO | ≥90 | 177.7 | 1.67× | 7,587 | 1.43× → 1.67× |
| `gas turbine` | ⚪ECHO | ≥90 | 11.3 | 1.40× | 493 | 1.42× → 1.40× |
| **`diesel`** | ⚪ECHO | ≥90 | 38.4 | **1.02×** | 2,003 | new |
| `data center` | ⚪ECHO | ≥90 | 317.9 | 0.98× | 19,718 | 1.02× → 0.98× |
| **`rare earth`** | ⚪ECHO | ≥90 | 23.7 | **0.88×** | 1,528 | new |
| **`refining margin`** | ⚪ECHO | 79 | 4.3 | **0.66×** | 313 | 0.66× → **0.66×** |

★★ **`M1292` [measured] — the three refined-product instruments all read flat-to-decelerating on the
day the physical print set an all-time high.** `diesel` **1.02×** (base 2,003), `refining margin`
**0.66×** for a **third consecutive run**, and `refinery` term count **+4.7%**, against a
**10-outlet** "US diesel prices hit an all-time high" cluster and a 7-outlet "US fuel production rose
in August". **The desk has now measured this same ordering — physical extreme, narrative flat — on
three separate runs and two separate instruments.**
★ **`rare earth` decelerates at 0.88×** on the day Reuters carried a **China shipment halt** [6] and
a Pentagon-vs-China piece [8] — a second instance of the same shape, in Materials.
⚠ `Larak` at **84.43×** is still the fastest term this desk has ever measured and is **still not
attached to any registered bracket** — carried, third run.

### B-6 · Blind-spot pass (`blindspot --scope foreign --days 3`; blind pool 21,356, sample 400)

Top token-0 terms are dominated by the fixed set (`AI` 1,719 · `Earnings` 955 · `Fed` 472 ·
`Trump` 439 · `Nvidia` 421 · `China` 403 · `Iran` 399 · `Oil` 354 · `Bitcoin` 321). **Three terms
outside the fixed table clear 220: `Yen` 257 · `Bond` 232 · `Dollar` 223.** (`Bessent`, the 09-02
run's find at 207, has dropped out of the top 30.)

★★★ **`M1293` [measured] — `yen` is a bucket-sized axis that the term table does not carry.**
Measured directly: **`yen` 857 hits (7d, phrase, foreign)** — **larger than `Treasury yield` (778),
`payrolls` (613), `refinery` (290) and `credit spread` (76)**, i.e. it would rank 8th of 17 in B-4 if
it were in the table. Supporting terms: `intervention` 553 · `Bank of Japan` 232 · `JGB` 51.
It has a **named, dated, multi-outlet mechanism** on 09-04:
*"Japan warns against weak yen, stands ready to intervene"* [5] · *"Japan's Katayama says will
closely monitor bond markets with heightened urgency"* [7] · *"Yen's changing fortunes might finally
be spooking the..."* [4→2] · and in the single-source tier *"Japan Has Not Done This Since 1990. If
It Happens, the Cheap Money Propping Up US Stocks Gets Expensive."*
⇒ **`yen` is folded into the term table from this run forward**, and the axis it implies — a
carry/term-premium channel into US duration — is bracketed as **`P138`** (§D), because it makes a
**testable, opposite** prediction to A-2's bear-flattening.
⚠ `carry trade` is **NOT** added: phrase **49** vs argv **1,797** — a 37× convention gap that makes
it uninterpretable as a bucket term (`D473`).

---

## §C · Positioning — `[COT report date 2026-09-01, Tue-close, released 09-04]` + `[FINRA 09-04]`

**⚠ This is a NEW COT release** (the 09-02 run read 08-25). It is Tuesday-dated, so **it does not
contain the 09-04 payroll reaction.** Context, never a trigger.

| instrument | net spec | wk Δ | 1y %ile | tag |
|---|---:|---:|---:|---|
| **Copper** | +80,869 | −4,397▼ | **100%** | 🟢 crowded long — **5th consecutive run at the 100th** |
| **Nasdaq-100** | +27,077 | **+15,951▲** | **82%** | 🟢 crowded long |
| USD Index | +17,025 | −1,657▼ | 70% | 🟡 |
| WTI Crude | +35,574 | +4,475▲ | 70% | 🟡 |
| UST 2Y | −882,518 | −21,222▼ | 71% | 🟡 |
| S&P500 e-mini | −75,941 | −7,947▼ | 63% | 🟡 |
| Gold | +228,124 | −15,210▼ | 50% | 🟡 |
| Silver | +26,739 | +1,478▲ | 44% | 🟡 |
| Russell 2000 | −14,741 | +1,377▲ | **17%** | 🔴 crowded short |
| **UST 10Y** | −909,275 | **−70,300▼** | **9%** | 🔴 crowded short |
| Nat Gas | −208,911 | −10,979▼ | **0%** | 🔴 crowded short |

★★ **`M1294` [measured] — the two largest weekly position changes point at the two axes this report
is about, and they disagree with the tape.** Speculators **added 15,951 Nasdaq-100 contracts in a
week to the 82nd percentile** while the equity tape's 5-session leadership was **Energy, not tech**
(§E); and they **sold 70,300 more UST 10Y contracts into a 9th-percentile short** — the single
largest weekly change on the board — **on the week the 30y−5y curve reached its flattest in a year
(`M1285`)**. A record-scale duration short built while the long end refuses to sell off is
**rebound ammunition**, not a direction (`D6`).
⚠ **`C24` reproduces a 5th run**: Copper at the **100th percentile** while Materials is
**−0.025 `wflow` / −0.107 `eqflow`** with Δ −0.037. `P102` settles that question **09-09**.

---

## §D · Propositions registered this run — `P136` · `P137` · `P138`

> All three have `D93` executed **before** freezing, thresholds taken from the observable's own
> measured trailing-252 distribution (`D503`, registered by this run's HANDOVER, applied immediately).
> ⚠ **`M1295` [measured] — 2026-09-07 is Labor Day and the NYSE is closed. `catalyst_calendar --days
> 10` does not carry it** (its window is described as "trading-ish days" and lists only PPI 09-10 and
> CPI 09-11). Every window below is counted in **settled sessions**, not calendar days, because of it.
> ⇒ registered as **`D507`** (§D-5).

### `P136` — ★★★ The narrative left the barrel while the physical print went vertical. Does the Energy tape follow the story or the barrel?

**Claim.** Three instruments say the oil *narrative* is draining and three say the oil *physical* is
at an extreme, in the same week. Narrative: `crude oil` **−14.7%**, `Strait of Hormuz` **−10.4%**,
`refining margin` **0.66×** (3rd run), `diesel` **1.02×** on a base of 2,003. Physical/price: WTI
**$96, +7% weekly, the steepest since mid-July** [21 outlets], **US diesel at an all-time high**
[10 outlets], and Energy is the board's only sector positive on **both** windows with near-unanimous
participation (`exc5` **+1.894 mean / +1.436 median, 1 of 16 negative**; `exc20` **+12.291 /
+11.517**). ⇒ **Either the tape is early and the narrative catches up, or the tape is late and the
5-session leadership decays into a decelerating story.**

| | |
|---|---|
| **Frozen observable** | `EW{XOM, CVX, COP, WMB, SLB, MPC, KMI, VLO, EOG, PSX, BKR, TRGP, OKE, FANG, OXY, DVN}` (the 16 `us_top300` Energy constituents) **minus `SPY`**, **5 settled-session** returns, `auto_adjust=False`, measured from the **2026-09-04** close to the **5th settled session after it = 2026-09-14** (09-07 is Labor Day) |
| **Branch A (the tape is early; leadership extends)** | **≥ +4.508** (trailing-252 **p85**) |
| **Branch B (the tape follows the decelerating story)** | **≤ −3.863** (trailing-252 **p15**) |
| **Branch C** | between = **the favourite, disclosed** |
| **`D93` executed BEFORE freezing** | trailing 252 of the same 5-session EW excess: mean **+0.520** · sd **3.922** · p05 −6.982 · **p15 −3.863** · p50 +0.907 · **p85 +4.508** · p95 +6.006 ⇒ **A ≈15% · B ≈15% · C ≈70%.** ★ **The centre is POSITIVE (+0.520) and the median is +0.907**, so "Energy beats SPY over 5 sessions" is the *normal* state — the row is written knowing its own baseline is asymmetric (`P78`/`D93`) |
| **State at registration** | **+1.894 = the 58.7th percentile.** ⚠ **Explicitly NOT an extreme** — the 20-session number (+12.291) is the extreme, the 5-session one is ordinary. Stated so the row is not read as a mean-reversion bet |
| **⚠ Event contamination — OWNED, not voided** | the window contains **August PPI (09-10)** and **August CPI (09-11)**, both 🔀binary, and the US-Iran exchange is live. There is no clean 5-session window; making these anti-signals would be the designed-to-void defect |
| **Anti-signal (VOID)** | an **OPEC+ emergency production decision**, a **US SPR release announcement**, or an **announced ceasefire/"Strait of Hormuz open" statement** (the `catalyst_calendar` TACO trigger) inside 09-05 → 09-14. ⚠ **Base rate checked**: no OPEC meeting is scheduled in the window; the Hormuz statement is an *undated* binary the calendar itself flags |
| **Information content (`L3`)** | **A** says a decelerating narrative is not a decaying trade and the desk's `refining margin 0.66×` reading has been a false negative for three runs. **B** says the 20-session Energy lead is a story-driven move now rolling over, and the `exc20 +12.291` is the thing to be short of, not long. **Neither branch merely confirms** |
| **Non-redundancy (`D343`)** | `P126` (09-09) asks *barrel vs chain* through a **pair spread**; `S136` (09-09) asks the same question through a different observable. **`P136` asks neither — it asks whether the SECTOR aggregate follows price or narrative**, and can fire opposite to both |
| **Track KPI** | if **A**, `refinery`/`diesel` term counts should turn up over the window; if **B**, they should keep decelerating. ⚠ The KPI and the level currently **disagree** (level positive, narrative decelerating) — registered now, not discovered at scoring (`D450`) |
| **Thread** | Oil/Iran, printed `FADING` but **rising on weekdays 13 → 21** (B-3); the chain leg (*Asian refiners turn to Argentina*) `REIGNITED` 8→3 |
| **⚠ `W3`** | this measures whether a spread persists, **not** whether any position was right. No sizing (P4) |
| **Owner** | `industry_US` |

### `P137` — ★★ A short-volume spike ON a +2.6% session: squeeze or distribution?

**Claim.** `SMH` printed **+2.61% against `SPY` −0.39% = +3.00pp excess** on the payroll session —
**1.7× branch A of `S141`, which had just measured "the `AVGO` print does not move the sector" at
−0.662pp one bar earlier** (`M1281`). On the same session `[FINRA]` short volume was **71.6% against
a 54.5% 20-day base, z = +2.99**, the board's largest. Short volume rising into a hard rally has two
incompatible readings and `[FINRA]` cannot separate them (`D6`): **new shorting into strength
(distribution)** or **market-maker hedging against option flow**.

| | |
|---|---|
| **Frozen observable** | `SMH` **minus `SPY`**, **4 settled-session** returns, `auto_adjust=False`, from the **2026-09-04** close to the **2026-09-11** close (09-08, 09-09, 09-10, 09-11; 09-07 is Labor Day) |
| **Branch A (the rip extends — the spike was hedging, or a squeeze that had further to run)** | **≥ +4.217** (trailing-252 **p85**) |
| **Branch B (the spike was distribution and it is paid)** | **≤ −2.886** (trailing-252 **p15**) |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of `SMH` 4-session excess vs `SPY`: mean **+0.851** · sd **3.420** · p05 −4.865 · **p15 −2.886** · p50 +1.230 · **p85 +4.217** · p95 +6.179 ⇒ **A ≈15% · B ≈15% · C ≈70%.** ★ centre **positive**, so "SMH beats SPY" is again the normal state and B is the harder branch |
| **State at registration** | **+1.455 = the 54.8th percentile** — dead middle. **The row starts from no edge in either direction, which is the point**: it is a test of the short-volume reading, not of momentum |
| **Anti-signal (VOID)** | a **semiconductor-specific US export-control ACTION** (a published rule, not a draft or a report of one) or an **`NVDA`/`AVGO`/`TSM` guidance withdrawal or M&A announcement** inside 09-05 → 09-11. ⚠ **Base rate checked**: the only export-control item in the last window was a **draft**-rules report, the class already pre-declared non-voiding by `S132`/`S138`/`S141` |
| **Information content (`L3`)** | **A** says a z ≈ +3 short-volume print on an up-session is hedging noise and this desk should stop reading `[FINRA]` z-extremes as pressure. **B** says it is the order-flow tell the L2 claims it is, and it caught a distribution the price did not show — which would be the **first** time this instrument has led. **Neither branch merely confirms**, and `M1237` vs `M1287` already show the sign inverting between runs |
| **Non-redundancy (`D343`)** | 09-11 carries `S125`, `S135` (UTIL/RE/STPL), `S142` (FIN UW on CPI) — three *sector-verdict* rows. **`P137` is an instrument row about `[FINRA]` short volume** and is orthogonal to all three. `S140` (IT breadth, 09-08) asks about **breadth**, not about a single index's reaction |
| **Track KPI** | if **A**, `SMH`'s short% should mean-revert toward its 54.5% base without the price giving back; if **B**, short% stays elevated *and* price falls |
| **⚠ `D6`** | `[FINRA]` short volume includes market-maker hedging. This row exists **because** the instrument cannot separate the two, not despite it |
| **Owner** | `industry_US` |

### `P138` — ★★★ Fed path or global term premium? The curve's own shape, and the blind-spot term that predicts the opposite

**Claim.** Two measurements this run point opposite ways about *what* is repricing.
**Fed path**: the payroll session bear-flattened **5y +4.1 > 10y +2.2 > 30y +0.3** (`M1284`), the
wires framed the print as a hike (`M1289`, hike odds *"briefly above 50%"*), and the 30y−5y slope is
at **69.6 bp = the 2.0th percentile of a year** (`M1285`) — the flattest in twelve months.
**Global term premium**: the run's top blind-spot term is **`yen` (857 hits, `M1293`)** with a dated
BoJ intervention warning [5] and a bond-market urgency statement [7]; `bond selloff` accelerates
**5.80×**; German yields set a fourth weekly rise. **A yen/JGB carry-unwind channel arriving in US
duration STEEPENS the curve. A Fed-hike repricing FLATTENS it. They cannot both be the driver.**

| | |
|---|---|
| **Frozen observable** | `^TYX − ^FVX` (CBOE settled closes, in **basis points**), **change over 4 settled sessions**, from the **2026-09-04** close (**69.6 bp**) to the **2026-09-11** close |
| **Branch A (global term premium arrives — the curve steepens)** | **≥ +4.40 bp** (trailing-252 **p85**) |
| **Branch B (Fed path dominates — it flattens further from a 2nd-percentile level)** | **≤ −5.97 bp** (trailing-252 **p15**) |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the same 4-session slope change: mean **−0.80** · sd **4.92** · p05 −9.63 · **p15 −5.97** · p50 −0.60 · **p85 +4.40** · p95 +6.60 ⇒ **A ≈15% · B ≈15% · C ≈70%.** ★ **The centre is NEGATIVE (−0.80)**, i.e. the trailing year's *normal* state is mild flattening — so branch A is the genuinely abnormal outcome and branch B is the continuation |
| **State at registration** | 4-session change **−4.60 bp = the 22.2nd percentile**, from a **level at the 2.0th percentile**. ⚠ **DISCLOSED: the level is already at a one-year extreme, so B requires flattening past an extreme and is mechanically harder than its 15% prior suggests.** A is the informative branch |
| **Dated catalysts inside the window** | **August PPI 2026-09-10** [`bls✓`, 🔀binary] and **August CPI 2026-09-11** [`bls~est`, 🔀binary] — both land inside, deliberately. A rate-path row that avoided the two inflation prints would be measuring nothing |
| **Anti-signal (VOID)** | an **unscheduled Federal Reserve action**, a **confirmed BoJ FX intervention or an unscheduled BoJ policy meeting**, or a **US Treasury refunding-size announcement** inside 09-05 → 09-11. ⚠ **Base rate checked**: no FOMC and no scheduled BoJ meeting fall in the window; quarterly refunding was announced in August |
| **Information content (`B4`)** | **A** says the axis this desk could not see until its own blind-spot pass surfaced it is the real driver, and `P121`'s four-run policy-path frame is aimed at the wrong mechanism. **B** says the Fed path owns the curve and the yen story is a foreign-market narrative with no US transmission, which retires `yen` from the term table as fast as it entered. **Neither branch merely confirms** |
| **Non-redundancy (`D343`)** | `P121` is a **level** claim (`DGS2` thresholds). `P125` is a **breakeven-vs-real leg** claim. `P128` is a **credit** claim. **None of the three measures curve SHAPE**, which is the only observable that separates a policy-path repricing from a term-premium one — the exact ambiguity `M1235` flagged on 09-02 and `M1284` reproduced today. `S142` (09-11) is a Financials sector row, not a rate row |
| **⚠ `D5`** | the observable is **CBOE**, not `[FRED]`, and that is deliberate: `DGS*` runs 1–2 days behind and `D427` has blocked three rows on it for two consecutive runs. The provider is named in the observable so the settle cannot drift between sources |
| **Owner** | `industry_US` |

### D-5 · Digs and one retraction registered by this stage

- **`R129`** — retracted: *"`S130` (`NVDA`/Hugging Face) is a **dead thread**"*, carried by the
  2026-09-04 HANDOVER §3c. **Killed by**: the thread's own curve **4→28→9 with a 28-outlet peak**
  (09-02→09-04), a **9-outlet** cluster in the 09-04 head, and `theme-age "Hugging Face"` =
  **🟡ACCELERATING, 3.11×, base 1,022**. `S130` settles **09-10** and is live. ⚠ What survives: the
  thread's `thread` **tag** is `ENDED`, which is a curve shape, not an importance judgement — the
  tool's own warning. **What is withdrawn**: the desk's reading of that tag as "dead".
- **`D506`** — *The `brief` recovery tiers are not symmetric across scopes: the `nb` classifier is
  Korean-only, so in `--scope foreign` the `single_source` tier is a **random sample** and
  `excluded_nonmarket` is **structurally empty**.* **Measured origin**: 618 single-source clusters,
  `scored: 0` / `scorable: 0` / `unscored: 618`, all `nb: None`, 15 shown at random;
  `excluded_nonmarket.count = 0`. A coverage claim written to the domestic spec **overstates** the
  foreign one, and this desk is foreign-only.
- **`D507`** — *`catalyst_calendar` does not carry US market holidays, so every N-session bracket
  written off its window is mis-dated.* **Measured origin**: **2026-09-07 is Labor Day**; the tool's
  `--days 10` output lists PPI (09-10) and CPI (09-11) and no holiday, while describing its window as
  "trading-ish days". A 5-session bracket written from the 09-04 close settles **09-14, not 09-11**.
  Same class as `D13`-STRUCTURAL (the KR quad-witching the calendar missed and the futures board
  carried).
- **`D508`** — *A `theme-age` reading and a `thread` tag can contradict each other, and the desk has
  been treating the tag as authoritative.* **Measured origin**: `Hugging Face` reads
  🟡ACCELERATING **3.11×** while its thread reads `ENDED`; `Oil/Iran` reads `FADING` while its
  weekday outlet curve **rises 13 → 21**. **Both contradictions resolve toward the numeric
  instrument, and both were caused by the tag being computed on a curve whose last bar is a
  weekend.** Prescription: **read every `thread` tag on weekday legs only, or read `theme-age`
  instead** (`R129` is this dig's first cost).

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each. **This is ROTATION's input.**

> **Wind direction only, not a ranking.** `exc1`/`exc5`/`exc20` are **equal-weight `us_top300`
> constituent baskets, excess vs `SPY`**, from this run's own price frame on the **2026-09-04 SETTLED
> close**. `SPY` itself: **−0.385% (1) · +0.109% (5) · −0.397% (20)**.
> Flow columns are this run's own `SECTOR_FLOW_US.json` (asof 09-04, 3-axis `nonews`, Δ citable).
> 🚫 **`wflow` is barred as a verdict basis for Consumer Discretionary and Communication Services**
> (G3) and every weighted number rests on a **52-day-old cap vector** (G5) — where the two cuts
> disagree, `eqflow` is the citable one and is named on the line.

| # | GICS sector | Wind | Driving prop. | eqflow / wflow | Δflow | exc1 | exc5 mean / med | neg5/n | exc20 mean / med | One line |
|---|---|---|---|---:|---:|---:|---:|---:|---:|---|
| 1 | **Energy** | **OW** | ★ **`P136`** | **+0.562** / +0.440 | **+0.054** | −0.27 | **+1.89 / +1.44** | **1/16** | **+12.29 / +11.52** | ★ **The only sector positive on flow level, flow Δ, breadth AND both price windows**, with **1 of 16** negative on 5 sessions and 3🟢/0🔴. Median ≈ mean ⇒ not a two-name artifact (`W5`). ⚠ **`P136` is registered precisely because its NARRATIVE is decelerating** (`crude oil` −14.7%, `refining margin` 0.66× for a 3rd run) while the physical print set an all-time high in diesel |
| 2 | **Health Care** | **OW−** | `S133` (09-14) | **+0.190** / +0.098 | −0.043 | −0.44 | **+0.63 / +0.98** | 12/32 | **+3.63 / +3.74** | Positive on **both** windows with **median ≥ mean** on each — the board's second-broadest. Flow Δ is mildly negative. `S133` (constituents vs ETF) settles 09-14 |
| 3 | **Information Technology** | **N** ⚠ | ★ **`P137`** · `S140`(09-08) | −0.195 / −0.090 | −0.010 | ★ **+1.52** | −0.27 / **+0.27** | 26/56 | −0.99 / −1.82 | 🚨 **The board's best `exc1` and it is ONE SESSION** — `SMH` +2.61% vs `SPY` −0.39% on the payroll print, against `exc5` −0.27 and `exc20` −0.99. ★★ **And `P101` settled today inverting the carried split**: software −4.46% vs hardware +2.05% over 5 sessions, participation **21.1% vs 73.0%** — the drag is **EDA and security software** (`ADSK` −16.4 · `CDNS` −14.0 · `SNPS` −11.0 · `PANW` −10.3 · `DDOG` −10.2), not semicap. **`M1251`'s "weak half = semicap" is dated** |
| 4 | **Financials** | **N** | `P128`(09-08) · `S142`(09-11) | **−0.023** / −0.118 | −0.004 | −0.58 | −0.07 / **+0.10** | 21/47 | **+1.92 / +1.04** | Flat on flow, **positive on 20 sessions with median > 0**, and `hy_oas` at the **2.0th percentile** is the strongest fact standing *for* the bucket. `eqflow` −0.023 vs `wflow` −0.118 ⇒ the negative sign is weighted, not broad; **`eqflow` is the citable cut** (G5) |
| 5 | **Utilities** | **N** | `P123`(09-08) · `S135`(09-11) | **+0.050** / +0.071 | −0.037 | +0.43 | **+0.35** / −0.13 | 8/15 | −1.36 / −1.17 | The only other sector with positive flow on both cuts, but breadth **0.00** and mean > median on `exc5` ⇒ **a few names, not a sector**. `ETN` (+3.46% on 09-04, `[FINRA]` z +2.16) is in Industrials, not here — the AI-power object still spans two labels (`D416`) |
| 6 | **Materials** | **N−** ⚠ | `P102`(09-09) | −0.107 / −0.025 | −0.037 | +0.26 | −1.13 / **−2.44** | 9/12 | −0.85 / **−2.99** | Negative on **both** cuts now, with median far below mean on both windows ⇒ **two names still carrying the label** (`C24`, 6th run). **Copper COT at the 100th percentile for a 5th run.** `rare earth` decelerates **0.88×** on the day of a China shipment halt. **`P102` settles the two-name question 09-09** |
| 7 | **Real Estate** | **UW−** | `S135`(09-11) | −0.124 / −0.116 | −0.020 | −0.43 | −1.31 / −1.10 | 11/12 | −1.83 / −1.62 | Negative on every cut and every window, **11 of 12 negative on 5 sessions** — the most internally consistent bucket on the board, and consistently bad. Rates at the 96th–99th percentile is the mechanism |
| 8 | **Consumer Staples** | **UW−** | `S135`(09-11) | −0.098 / −0.182 | −0.018 | −0.66 | −1.39 / **−2.29** | 12/19 | +0.03 / −1.94 | Negative on 5 sessions with median below mean; 20-session mean ≈ 0 but median **−1.94** ⇒ the flat aggregate is one or two names. No defensive bid despite the rate move |
| 9 | **Consumer Discretionary** | **UW** | — | **−0.251** / −0.255 ⚠ | −0.004 | −0.25 | −2.38 / **−2.95** | **21/28** | **−4.11 / −5.27** | 🚫 **`wflow` barred** (AMZN 40.2%, the board's only flipper: −0.255 → **+0.068** ex-top1). **`eqflow` −0.251 agrees with `wflow`, so the verdict stands on `eqflow` and says so.** Worst 20-session mean on the board after Industrials, **21 of 28 negative** — this one is broad. Tesla's Cybercab launch → NHTSA probe inside the window |
| 10 | **Communication Services** | **no verdict issued** | — | **−0.035** / −0.389 🚫 | +0.007 | −1.09 | −2.02 / −2.27 | **11/12** | **+1.27 / +3.70** | 🚫 **`wflow` barred entirely** — Alphabet is **76.6%** of the bucket under two tickers, ex-both-classes `wflow` **+0.272** (swing **0.661**, `D459` 11th run). `eqflow` **−0.035** is the only citable aggregate and it is **flat**. ⚠ `exc20` **median +3.70 vs mean +1.27** — the same one company dragging the mean. **A sector this desk cannot aggregate is a sector this desk does not rank** |
| 11 | **Industrials** | **UW** | `S126` (settled C) | −0.354 / −0.379 | ★ **+0.082** | +0.57 | −1.34 / −1.67 | **33/50** | **−5.04 / −5.90** | **The board's worst level and its LARGEST positive Δflow (+0.082)** — the run's second tension. Worst `exc20` on the board with **33 of 50** negative on 5 sessions, i.e. the weakness is broad, not weighted. `S126` settled **`FIRED-C`** at −1.165pp. ⚠ `ETN`'s +3.46% sits inside this label |

★ **Two tensions handed to ROTATION unresolved (P4):**
1. **Energy is unanimous on every instrument this desk owns and its narrative is decelerating on
   every news instrument this desk owns.** `P136` brackets it; ROTATION must decide whether to act
   before 09-14.
2. **Industrials is the worst sector on level and the best on Δ.** One of the two is the newer
   information and this stage does not say which.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 · Rows settled this run: **1 newly scored, 9 folded in, 3 read from the KR desk**
Full accounting in `HANDOVER §3`. **`P101` `FIRED-C`** is the only row this stage's desk scored
fresh; the nine from the unwritten 09-04 run were **transcribed, not re-derived** (`D242`), and
`S126`/`S134`/`S139` were scored by the KR desk this morning. **0 `EXPIRED` · 0 silent skips ·
3 blocked-and-named (`P121`·`P114`·`P125`, all on `D427`) · 1 unscoreable (`S8`, 38th run).**

### F-2 · ★ The `D449` class produced its second scored row, and the pattern is now visible
`P100` (09-02 run) and **`P101` (this run)** were both registered inside a `MACRO_REPORT §D`,
both absent from `SCENARIOS.md`'s master index, and both were reached **only because a later run went
looking**. `P101` sat unscored for **10 days past its settle**. ⇒ **`D504`** (registered at HANDOVER)
generalises `D449` from *propositions* to their *settlement path*, and **`P102`·`P126`·`P127`·`P128`
are in the same state right now**, with `P102` settling **09-09**. This stage's three new rows
(`P136`–`P138`) are written into this report **and named in the writeback pre-commitment** so they do
not join that set.

### F-3 · The pattern in the registration states — a second counter-instance, and a caveat
The standing record: pre-settle *reads* on this desk have been unreliable (wrong in sign three times,
in magnitude a fourth); `M1244` amended it to *"a **registration state** leaning toward the branch
that fired is a better-behaved object"* on `n = 1` (`P100`).
★ **`P101` is the second sample and it points the other way.** Its registration state was
**+6.228 = the 89.7th percentile**, leaning hard toward branch **A**, and the settle came in at
**−6.511**, a **−12.74pp** move that stopped 1.40pp short of the **opposite** branch. ⇒ **`n = 2`,
one for and one against. The amendment of `M1244` is withdrawn to "unmeasured" rather than carried as
a rule** (`C4`, `S5`). Recorded because carrying a rule built on `n = 1` after `n = 2` contradicts it
is precisely the failure this section exists to catch.

### F-4 · 🚨 What this stage asserted and then refuted, in the same run (`§4c` / `D48`)
1. ★★ **This stage's first pass read the oil thread's `FADING` tag as a fact and drafted "the oil
   narrative is fading on both the term sweep and the thread."** Re-reading the same curve with the
   per-day denominator line — which the stage's own spec puts *first* — shows the tag rests on a
   **Saturday bar of 147 articles against a 705–943 weekday run**, and the weekday legs go
   **13 → 21, rising**. **Only the term sweep says the narrative is draining; the thread does not.**
   The corrected form is what B-3 and `P136` carry; the error is recorded rather than deleted, and it
   is the direct cause of **`D508`**.
2. ★ **A carried label was refuted by measurement, not by re-reading** — `S130`'s "dead thread"
   (`R129`). It had been written into a HANDOVER and would have been inherited a third time.
3. ⚠ **Zero self-refutations would itself be a finding.** Two here; three more in `HANDOVER §9`.

---

## ✅ EXIT CHECK — MACRO

- [x] **Catalysts injected** — `catalyst_calendar --days 10` (beyond the default, because `SCENARIOS`
      carries armed dates to 09-18): **3 binaries in window — PPI 09-10 ✓, CPI 09-11 ~est, and an
      undated Hormuz-open statement.** ⚠ **None is ≤48h** (today is Saturday; the nearest is D-5), so
      PREMORTEM's mandatory ≤48h both-sides bracket **does not trigger on a date** — but both dated
      binaries sit inside `P136`/`P137`/`P138`'s windows and all three rows are written both ways.
      🚨 **The calendar missed Labor Day 09-07** (`D507`), and every window here is counted in
      settled sessions because of it.
- [x] **Narrative read**: events (`brief --body 2`, tail **0**), trajectories (`thread --days 7`),
      17-term sweep in **both conventions**, blind-spot pass. **Indicators**: `[FRED]` primaries at
      `--days 120` and `--days 400`, CBOE curve, `[COT 09-01]`, `[FINRA 09-04]`. **Daily anchor**:
      `llm_outputs/2026-09-02/industry_US/MACRO_REPORT.md` read in full; `module_report_tags show`
      cross-queried at HANDOVER.
- [x] **`tail = 0` is NOT treated as the coverage claim** (B-1): `single_source` **618 counted / 15
      shown (603 unseen)**, `excluded_nonmarket` **count 0 — structurally empty in this scope**,
      `subevents_recovered` **204**. Stated coverage **924 of 1,323 = 69.8%**. 🚨 The asymmetry is
      itself registered as **`D506`**. **No "quiet bucket" claim appears anywhere in this report.**
- [x] **Denominator is the corrected one**: `denominator.articles` **4,531** with
      `excluded_not_news` **empty ({})** — stated as empty rather than assumed applied.
- [x] **Trajectories read**; every proposition carries a thread tag + curve (`P136`: Oil/Iran
      `FADING`-as-printed but **13→21 on weekdays**; `P137`: no matching thread, stated explicitly —
      it is an instrument row; `P138`: `bond selloff` 🟡ACCEL **5.80×** + the `yen` cluster).
      **An inherited thread label was flagged AND retracted** (`S130`, `R129`).
- [x] **Every "nothing happened" claim carries its denominator** — there are none; the coverage
      accounting explicitly bars them this run.
- [x] **No bucket count trusted from a single convention** — both printed, gaps up to **4.5×**
      (`credit spread` 76 vs 344) and **37×** (`carry trade` 49 vs 1,797, which is why it was
      **rejected** as a bucket term).
- [x] **Both halves cited** (`C2`): the payroll print's hike framing **and** *"This Is No Hiring
      Boom"* / *"The Jobs Report Wasn't Really Why"*; the rate complex's **level** (96th–99th
      percentile) **and** its **shape** (2.0th-percentile slope); ⚠ **the BLS revision/AHE half is
      declared UNREAD rather than faked.**
- [x] **Every relative-performance number names its benchmark inline** (`vs SPY` throughout §E and
      §D; `vs its own 20-day base` for `[FINRA]`). **No statistical result carried across markets** —
      the KR `ic_ledger` cell is named in `HANDOVER §2`/`C29` and used nowhere here (`W1`).
- [x] **Credit axis read and cited**: `hy_oas` **2.65 = 2.0th percentile**, `ig_oas` 0.81, `NFCI`
      **−0.558** and easing. **No credit-stress or risk-off claim appears**; the opposite is measured
      and stated (`M1286`).
- [x] **`real_10y` quoted with `breakeven_10y`** — and their 3-session decomposition is the report's
      headline measurement (`M1283`), printed as a **reference state, not a score** (`P125`, `D427`).
- [x] Transmission matrix produced — **all 11 sectors, one line each**, with `eqflow` named as the
      citable cut wherever `wflow` is barred.
- [x] Self-backtest appended: 1 newly scored, 9 folded in, `n = 2` on the registration-state rule
      **with the rule withdrawn rather than carried**.
- [x] New blind-spot term **`yen` folded into the term table**; `carry trade` explicitly rejected
      with its measurement.
- [x] **Linter** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-09-05/industry_US/MACRO_REPORT.md` ⇒ **0 findings** across C1/C2/S6/D6. ⚠ It checks **form** only; a clean run is not a correct report, and §F-4 records two content errors this stage made and corrected that the linter cannot see.


---

# §5 · DRIFT ADDENDUM — appended 2026-09-05 by Stage 11 / L1·DRIFT (append-only)

> `scripts/drift_watch.py --report llm_outputs/2026-09-05/industry_US/MACRO_REPORT.md`, run at
> **completion + 0.7h**. ⚠ **`D282` reproduces for an 8th time**: the spec is **+3–6h** and this run
> fired at **+0.7h**, because the whole desk runs inside one session. The fix is scheduling, i.e.
> human. **The window this addendum can see is therefore ~42 minutes wide, and its null result on
> every other term set carries correspondingly little weight.**
> **Nothing above is rewritten. The original call stays visible next to its correction (P4).**

## 5.1 · One 🚨 burst, and it points straight at the run's headline thesis

| term set | post-completion count | vs baseline |
|---|---:|---:|
| **`ceasefire`** | **4** | **8.3×** |
| `Strait of Hormuz` | 5 | non-burst |
| `rate hike` | 4 | non-burst |
| `blockade` · `invasion` · `downgrade` | 2 each | non-burst |
| `guidance cut` · `bankruptcy` | 1 each | non-burst |

**Body-read (not counted) — the two items that carry the burst:**
- *"**Putin signs off on 72-hour ceasefire with Kyiv as US envoys visit**"* [politico, 2026-09-05]
- *"**US drafting post-war plan for the Middle East, report says**"* [euronews, 2026-09-05] —
  ⚠ **1 article, 1 outlet.**

## 5.2 · 🚨 The burst is a partial contaminant, and the contamination is measured, not assumed

Of the **8** highest-BM25 `ceasefire` matches in the last 2 days, **three are dated `Wed, 29 Apr`**
(`google_en` rows: *"Oil prices rise despite UAE exit from OPEC amid Iran ceasefire impasse"* ×3) and
**two are Gaza/Lebanon items unrelated to either war leg**. ⇒ **the 8.3× multiple is inflated by
stale-dated and off-topic rows**, and the count alone would have over-stated it.
★ **Registered as `D519`**: *`drift_watch`'s burst multiple is computed on a term count that includes
rows whose own dates are months old, so a burst must be body-read before it is sized — the counting
layer and the dating layer disagree.* This is the same class as `D508` (a tag computed on a curve
whose last bar is a weekend).
⇒ **The burst is downgraded from 8.3× to "two dated, on-topic articles, one of them single-outlet"**
— and it is **still worth this addendum**, for the reason in 5.3.

## 5.3 · What it does to the report's headline thesis — and what it does NOT do

**The mechanism is direct.** `MACRO §D`'s `P136` and `SECTOR_DEEP_ENRG` rest on a **distillate-crack
capacity event**, and the wires name **two** causes for it — *"Diesel hits record high as **Ukraine
and Iran wars** knock out refineries."* A Russia–Ukraine ceasefire, if it held, would pause the
**Ukrainian drone strikes on Russian refineries**, which is one of those two causes.
**And the tape already carries an independent, earlier signal in the same direction that this report
did NOT carry**, found by the body-read:

| dated item | date | source |
|---|---|---|
| *"Russia Says Oil Output Drop Is **Temporary** as Refineries **Restart**"* | 09-03 | oilprice |
| *"Ukraine's Refinery Strikes Force Russia to Process Oil Abroad"* | 09-02 | oilprice |
| *"Ukrainian drones start fire at Russian oil export port"* (Novatek terminal) | 09-03 | hellenicshipping |
| *"Russia's Oil Revenue Sinks as Urals Falls to $59"* | 09-03 | oilprice |

★ **`M1327` [measured] — the Russian-refinery leg was ALREADY two-sided in the corpus on 09-03 and
this report did not read it.** MACRO §B-2 carried only the destruction half; the **restart** half was
sitting in the same feed, same source, same day. **That is a coverage failure inside this run, not a
drift event** — the drift probe merely surfaced it.

⇒ **Two consequences, and the second is the one that matters:**
1. **`P136`'s VOID clause is NOT amended.** It names an OPEC+ emergency decision, a US SPR release,
   and a Hormuz-open statement. **A Russia–Ukraine ceasefire is none of those.** `D242` forbids
   moving a frozen clause after registration, and it is not moved. ⇒ **`P136` and `S147` settle
   2026-09-14 exactly as frozen**, and a ceasefire would show up **inside** the observable rather
   than voiding it — which is the correct behaviour for a thesis risk.
2. **The kill condition `SECTOR_DEEP_ENRG §Δ9` already names is the right one and it is now dated.**
   *"The distillate−gasoline spread falling below its 50th percentile"* (today **98.4th**). A
   ceasefire that restores Russian refining capacity would show there first. **Watch date: the first
   settled close after the 72-hour window expires, i.e. 2026-09-08.**

⚠ **What this addendum does NOT claim.** 72 hours is not a peace; *"US drafting a post-war plan"* is
**one outlet reporting a report**; and the same 2-day window carries *"At least 5 killed in Russian
attacks on Ukraine as US envoys visit"* [aljazeera 09-05] and *"No End in Sight for US-Iran
Conflict"* [bloomberg 09-03]. **The report's Energy call is left standing, flagged, not reversed.**

## 5.4 · The other anti-signals, re-checked against the burst — none fired

`drift_watch` printed this report's own VOID clauses for cross-checking. Checked, one by one:

| clause (row) | fired? |
|---|---|
| OPEC+ emergency production decision · US SPR release · Hormuz-open statement (`P136`) | ❌ none in the window |
| semiconductor-specific US export-control **ACTION**, published rule (`P137`, `S145`) | ❌ none |
| unscheduled Fed action · confirmed BoJ FX intervention · unscheduled BoJ meeting · Treasury refunding-size announcement (`P138`) | ❌ none. ⚠ `rate hike` ran **4** post-completion — **non-burst**, and no *action* item among them |
| earnings print at `STX`/`WDC`/`AMD` (`S145`) | ❌ none — next prints 10-27 / 11-05 / 11-03 (`earnings_dates`) |
| PJM/ERCOT capacity-auction result or emergency order (`S146`) | ❌ none |
| US federal policy action against refiner margins (`S147`) | ❌ none — the standing thread (*"Trump ramps up pressure on refiners"*, 09-01) did not advance to an action |
| acquisition of `FCX`/`NEM`, or a tariff action naming copper or gold (`P102`) | ❌ none |

⇒ **Zero registered VOID clauses fired.** Every bracket registered today stands armed as frozen.

## 5.5 · What this stage adds to the run's own error record (`D48`)

**One coverage failure found in this run's own MACRO stage** (`M1327`, §5.3): the Russian-refinery
story was **two-sided in the corpus on 09-03** and §B-2 carried only one side. The earlier text is
**not edited** — it stands above with its one-sided reading, and this addendum stands beside it.
★ **And the instrument that found it was a burst that turned out to be 60% artifact** (§5.2). **A
noisy probe still surfaced a real gap**, which is an argument for running it even at +0.7h where its
own null results are near-worthless.
