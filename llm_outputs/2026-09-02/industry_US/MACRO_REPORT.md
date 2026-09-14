# MACRO_REPORT — industry_US · 2026-09-02 (Wed) · Stage 3 / L1·MACRO

> Run clock **KST 22:09 → 23:0x = 09:09 → 10:0x ET**. **The NYSE had not opened.** Last settled US
> session **2026-09-01**. Every price statement below is about **09-01 or earlier** unless it carries
> the word LIVE, and no LIVE number is used as evidence (`D304`).
> English-pure runtime. Analytical output only — **zero buy/sell recommendations (P4)**.

## §0 · 🚨 Instrument state governing every line below (from `preflight/PREFLIGHT.md`)

| revoked today | substitute used here |
|---|---|
| primary `SECTOR_FLOW_US.json` OBV / flow / Δ | **`SECTOR_FLOW_US_REPAIRED.json`** (298 scored, 3-axis `nonews`, asof 09-01, 258 names patched at 08-28) |
| Δflow as a **magnitude** | Δ is cited as **direction only** — the 08-31 baseline is yesterday's holed-OBV primary snapshot |
| `wflow` verdicts on **Cons. Disc.** / **Cons. Staples** / **Comm. Services** | `eqflow`, breadth, the settled tape, FRED, COT/FINRA — each named on the same line |
| theme-freshness or "quiet" **sourced from the sweep** (`vel_coverage` 17.11%) | **direct** `fts` / `theme-age` / `news_velocity` calls at **≥9s spacing** |
| 08-28 daily closes for 259 of 301 names · any 08-28 volume claim · the 09-02 tape · `EA` / `APH` | the 5m-proxy tape, labelled; and 09-01 settled closes |
| cap-weight as "current size" (universe **49 days** stale) · single-number concentration (`--days` differs) | stated inline wherever it matters |

---

## §A · Indicators — `[FRED]` primaries, and the decomposition the frame turns on

### A-1 · The rate complex, both halves (`C2`) — and the leg **flipped on the last session**

`[FRED]`, all series at the **2026-08-31** close except where noted:

| series | 08-31 | Δ1 obs | Δ5 obs | Δ21 obs |
|---|---:|---:|---:|---:|
| `us_2y` (DGS2) | **4.34** | +0.00 | **+0.10** | +0.06 |
| `us_10y` (DGS10) | **4.75** | +0.02 | +0.05 | 0.00 |
| `us_30y` (DGS30) | **5.25** | +0.03 | +0.06 | — |
| `real_10y` (DFII10) | **2.44** | +0.02 | **+0.06** | **−0.03** |
| `breakeven_10y` (T10YIE) | 2.31 → **2.35 (09-01)** | **+0.04** | +0.03 | +0.08 |
| `fed_funds` (DFF) | 3.63 | 0.00 | 0.00 | 0.00 |
| `vix` | 14.92 | +0.49 | −0.93 | −1.07 |
| `nfci` (08-28) | **−0.558** | −0.002 | −0.020 | **−0.093** |

★ **`M1234` [measured] — through 08-31 the repricing was a REAL-rate repricing, and the measurement is
unambiguous.** The trailing-252 distribution of the **3-session (Δ`breakeven_10y` − Δ`real_10y`)**
spread puts the 08-31 reading at **−11.0 bp = the 5.2nd percentile of a year** (mean −0.79, sd 5.94,
p05 −11.0, p15 −6.0, p50 0.0, p85 +5.0, p95 +9.0). ⇒ **`P121`'s inherited claim — "the repricing is
the policy path, not inflation" — is not merely supported, it is at a one-year extreme.**

⚠ **And the very next observation points the other way.** `T10YIE` prints **2.35 on 09-01**, up
**+4 bp**, while `DGS10`/`DFII10`/`DGS30`/`DGS2` **all stop at 08-31**. Cross-provider (`D5`, stated):
CBOE `^TNX` moved **4.758 → 4.796 = +3.8 bp** on 09-01, so a **+4 bp** breakeven against a **+3.8 bp**
nominal implies a **real yield essentially FLAT (≈ −0.2 bp)** on that session — the exact inverse of
08-28, when the entire +14 bp `DGS2` / +6 bp `DGS10` move was real and breakevens were flat.
🚫 **This is stated as an inference across two providers, not as a `[FRED]` decomposition** — the
`[FRED]` decomposition for 09-01 **does not exist yet** (`C3`: the column is unknown, not zero).
⇒ registered as **`P125`** (§D) rather than concluded.

⚠ **`D427` reproduces for a third consecutive run**: `T10YIE` carries **09-01** while the two series
it is computed from stop at **08-31**. Every row that needs both is written to settle on the **joint**
date.

### A-2 · The curve's SHAPE says policy path even while the headlines say fiscal

The narrative on 09-01 was explicitly a global/fiscal one (§B-2: European yields at 15-year highs, JGB
10y at 3% for the first time since 1996, "Governments should heed the bond market's warning"). **The
US curve moved the other way round from a term-premium event.** CBOE settled closes, 08-31 → 09-01:

| tenor | 08-31 | 09-01 | Δ |
|---|---:|---:|---:|
| `^FVX` (5y) | 4.507 | 4.557 | **+5.0 bp** |
| `^TNX` (10y) | 4.758 | 4.796 | +3.8 bp |
| `^TYX` (30y) | 5.249 | 5.268 | **+1.9 bp** |

★ **`M1235` [measured] — the belly led and the long end lagged: 5y > 10y > 30y.** A term-premium /
fiscal-supply event steepens the back end; this **bear-flattened** it. ⇒ **on the US curve, 09-01 was a
rate-HIKE-expectation session**, which is corroborated by a dated, multi-outlet news fact rather than
by feel: *"The Odds of a September Rate Hike Have Nearly Doubled, Courtesy of Fed Chair Kevin Warsh"*
[4 outlets, 09-01] and *"Fed's Barr: If inflation doesn't moderate, the central bank should raise
rates"* [**8 outlets**, 09-01].

⚠ **Both halves (`C2`)**: the level statement (US 10y through 4.75%, "market watches 5%") and the shape
statement (30y the *smallest* mover) point in opposite interpretive directions and **both are printed
here**. This is exactly the oscillating-variable failure class this stage warns about, which is why
`P125` carries both branches.

### A-3 · Credit refuses to join — and it is at a one-year TIGHT, not merely "calm"

`[FRED]` 08-31: **`hy_oas` 2.63** · **`ig_oas` 0.80** · **`NFCI` −0.558 (08-28)**.

★ **`M1236` [measured] — `hy_oas` 2.63 sits at the 0.4th percentile of its trailing 252** (p05 2.67 ·
p15 2.71 · p50 2.83 · p85 3.07 · p95 3.19). Its 5-session change is **−6 bp**. **`ig_oas` 0.80** is at
the 57.9th percentile, i.e. dead middle, 5-session change **−1 bp**. `NFCI` has **eased 9.3 bp over 21
observations**.
⇒ **On the day the global bond market printed multi-decade-high yields, US credit spreads were at a
one-year low and financial conditions were still easing.** No credit-stress claim appears anywhere in
this report; the opposite is measured and labelled. **`P67`'s 2.85 trigger is now 22 bp further away
than at registration**, and `S111` already scored **C** on the IG leg.
⇒ registered as **`P128`** (§D).

### A-4 · Per-name short pressure `[FINRA Reg SHO daily, dated 2026-09-01 — matches the settled bar]`

| 🔴 pressure building | z | 🟢 pressure leaving | z |
|---|---:|---|---:|
| **ANET** (held) | **+2.25** | **NEM** | **−3.14** |
| **NVDA** (held) | **+2.18** | **WMB** | **−3.08** |
| **NUE** (held) | **+1.95** | **ETN** (held) | **−1.72** |
| MPC (held) | +1.49 | NDAQ (held) | −0.97 |
| RTX (held) | +1.21 | MET (held) | −0.16 |
| CRM | +1.05 | | |
| AVGO (held) | +0.79 | | |
| PSX (held) | +0.59 · SLB +0.47 · XOM +0.47 · HPE +0.22 | | |

★ **`M1237` [measured] — short pressure moved in the same direction as the tape, name by name.** The
three 🔴 extremes are **AI-compute and steel**, on sessions where `ANET` fell **−3.29%**, `NVDA`
**−1.51%** and `SMH` **−2.05%**; the three 🟢 extremes are **gold, midstream and electrical**, of which
`NEM` and `WMB` are two of the run's **six** green flow tags. ⚠ **`ETN` is the divergence worth
naming**: shorts left (**z −1.72**, 5v5 **−5.0**) on a **−2.78%** session — pressure exiting a falling
name is not the same object as pressure exiting a rising one, and this report does not read it as one.
⚠ `[FINRA]` short-volume includes market-maker hedging; it is an order-flow tell, **not** a directional
signal (`D6`).

---

## §B · News — `--scope foreign` on every call, and coverage is stated before anything is concluded

### B-1 · Coverage accounting, because `tail = 0` is **not** a coverage claim

`brief --date 2026-09-01 --scope foreign --body 2` (client-side, GPU; `embed sync` run first —
**6,222 fetched · 6,207 newly embedded · 562,149 cumulative vectors**):

| layer | count |
|---|---:|
| articles (denominator, `excluded_not_news = {}` — stated, not assumed) | **5,212** |
| clusters | **1,473** |
| events ≥2 sources (= market events) | **830** |
| head (≥5 sources) / body (≥2) / **tail** | 102 / 728 / **0** |
| `subevents_recovered` | **232** |
| `single_source` clusters | **643**, of which **15 shown** |
| `excluded_nonmarket` | **0 / 0** |

★ **`M1238` [measured] — the honest coverage number is 57.4%, not "tail = 0".** 830 multi-source events
+ 15 single-source rows = **845 of 1,473 clusters seen**; **628 single-source clusters were never
displayed.** And they are not merely truncated: the `single_source` tier reports
**`scored 0 · scorable 0 · unscored 643`** — the market/non-market classifier is **Korean-only**, so on
`--scope foreign` the 15 rows shown are a **random sample**, not the top-ranked. ⇒ **on this desk's
foreign runtime the single-source recovery tier is a random 2.3% sample, not a recovery mechanism.**
🚫 **No "quiet bucket", "nothing happened in X", or "the market ignored Y" claim appears anywhere in
this report**, and this measurement is the reason.

### B-2 · Events — the head, with denominators. **One story owns the day.**

The 09-01 head is dominated by a single, coherent macro complex, and it arrives from three independent
directions at once:

**(i) The escalation** — *"Oil prices rise as latest fighting resurrects Middle East supply disruption
risks"* [**17 outlets / 99 articles**] · *"US launches new strikes against Iran as war escalates"*
[16] · *"Two More Oil Tankers Are Attacked in the Strait of Hormuz"* [12] · *"U.S. military conducting
fresh strikes in the Strait of Hormuz"* [5] · *"Opposition to oil deal with U.S. grows in Venezuela"*
[22] · *"Asia Spot LNG Prices Hit 5-Month High as Hormuz Blockage Drags On"* [4] · *"Qatar Extends LNG
Force Majeure as Hormuz Traffic Remains…"* [thread 3→6→6→4→2].

**(ii) The bond market** — *"Japanese Yen weakens as 10-year bond yield hits 3% for first time since
1996"* [12] · *"Eurozone inflation jumps to 3.3% in August as energy prices surge"* [8] · *"European
government bond yields surge to 15-year highs as sell-off deepens"* [4] · *"Bond Yields Around the
World Soar in Challenge to Government Borrowing"* [WSJ, 4] · *"Global bond yields soar to multi-decade
highs as Middle East turmoil reignites inflation fears"* [CNBC, 3] · *"Governments should heed the bond
market's warning"* [FT, 3] · *"Bessent's Bond Gains Wiped Out as 30-Year Yields Jump Once Again"* [2].

**(iii) The policy reaction function** — *"Fed's Barr: If inflation doesn't moderate, the central bank
should raise rates"* [**8**] · *"The Odds of a September Rate Hike Have Nearly Doubled, Courtesy of Fed
Chair Kevin Warsh"* [4] · *"'This Is an Inflation First Fed Right Now,' Evercore's Guha Says"* [2] ·
*"Analysis: Japan faces day of policy reckoning as Bessent calls time on big stimulus"* [5] ·
*"Bessent meets BOJ's Ueda, calls for sound policy to avoid currency volatility"* [5].

**Named, dated sector causes in the same head** (each carried into §E rather than into a proposition):
- **Cons. Disc.** — *"FTC, states sue Amazon over alleged manipulation of advertising auctions"* [13].
- **Utilities / AI-power** — *"Analysis: Texas' halt on powering data centers reflects US reckoning
  over 'ghost' demand"* [**6 outlets**, up from 3 on 08-31] · *"California Wildfire Legislation
  Postponed, Utility Stocks Bounce"* [6] · *"Google Just Locked Up the Largest Geothermal Power Deal
  Ever Made"* [6] · *"Major U.S. Oil Port Selected for Nuclear Power Project"* [5] · *"The U.S. Army
  Will Spend $2.2 Billion on Micro Nuclear Reactors"* [4].
- **Health Care** — *"Trump's MFN Push Goes Beyond Big Pharma, Adds 9 Mid-Sized Drugmakers"* [5] ·
  *"Novartis pauses trials of experimental cell therapy after three deaths"* [7].
- **Materials** — *"Copper price stalls short of record as Chile's storm-hit output slumps to 2011
  low"* [5] · *"Gold Holds Drop as Higher Oil, Bond Selloff Raise Rate-Hike Bets"* [4].
- **IT** — *"Nvidia pours $3.5 billion into MediaTek — company will adopt NVLink Fusion"* [6] ·
  *"Anthropic signs $35 billion cloud deal with Nvidia-backed Lambda"* [5] · *"Broadcom Faces Crucial
  Earnings Test After AI Chip Sales Surge 143%"* [3] · *"Palo Alto Networks beats… acquires Console"*
  [11] · *"Dell Technologies Q2 2027 Earnings"* [11].
- **Labour** — *"US job openings rise in July after sharp downward revision in prior month"* [6].

★ **`M1239` [measured] — the tape agrees with the head, and the agreement is the finding.** Sector ETF
excess vs **`SPY`** (named inline, `C1`), settled closes ending **09-01**:

| ETF | exc1 | exc2 | exc5 | exc20 |
|---|---:|---:|---:|---:|
| **XLE** | **+1.95** | **+4.32** | **+4.91** | **+11.92** |
| XLK | −0.85 | −1.65 | +1.58 | −0.51 |
| XLP | +1.00 | +1.18 | −0.93 | +1.10 |
| XLU | +1.47 | −0.45 | −1.19 | −2.28 |
| RSP | −0.13 | −0.76 | −1.35 | +0.04 |
| XLF | −0.20 | −0.57 | −1.36 | +0.06 |
| SMH | −1.36 | **−3.86** | −1.37 | **−4.06** |
| XLC | +0.17 | +0.51 | −1.49 | +0.20 |
| XLV | +1.35 | +1.28 | −1.53 | **+7.14** |
| XLB | −0.49 | −1.20 | −2.28 | +1.37 |
| XLY | −1.03 | −0.13 | −2.31 | −1.89 |
| XLRE | +0.53 | −0.01 | −2.37 | −1.26 |
| **XLI** | −0.68 | **−2.41** | **−2.64** | **−6.10** |

⚠ **`XLK` and `SMH` disagree by 2.95pp on exc5** (+1.58 vs −1.37) and by 3.55pp on exc20 — **the IT
label is not one bet**, and §E does not treat it as one (`W5`).

### B-3 · Trajectories (`thread --days 7 --scope foreign`)

Per-day denominators first (the stage's own requirement): **08-27 856 · 08-28 735 · 08-29 307 ·
08-30 293 · 08-31 745 · 09-01 830 · 09-02 421**.
⚠ **09-02 is a PARTIAL day** (421 vs 745–856 on full sessions) because this run fires at 09:09 ET.
**Every FADING tag at the window end is therefore inflated and none is read as attention decay.**
Totals: daily events 4,187 → threads 3,228 (multi-day **503**, alive **138**, one-day 2,725).

| thread | tag | curve | used by |
|---|---|---|---|
| *"Markets slide as inflation fears trigger global bond selloff"* | **BUILDING** | 4→4→**7** (08-31→09-02) | `P125` |
| *"Euro area: Inflation jump supports ECB hike"* | **BUILDING** | 5→2→2→4→**6** (5 days) | `P125` |
| *"How Japan's bond rout is turning the tide of global capital"* | **BUILDING** | 4→**5** | `P125` |
| *"Global Bond Selloff Weighs on Stocks"* | **BUILDING** | 2→**4** | `P125` |
| *"Bessent Says Hormuz Will Soon Be 'Worthless' as Oil…"* | **BUILDING** | 2→2 | `P126` |
| *"Commodities: Middle East Escalation Pushes Energy Prices…"* | **REIGNITED** | 2→**4** | `P126` |
| *"Gas Turbine Prices Are on Track to Nearly Triple"* | **REIGNITED** | 5→3→**8** | `P127` |
| *"Prediction: Bloom Energy's Backlog Will Top $50 Billion"* | **REIGNITED** | 6→4→6→4 | `P127` |
| *"BOJ's Takata urges nimble rate hikes"* · *"BOJ's Himino Vows Inflation Vigilance"* | **REIGNITED** | 4→2→6 · 6→4 | `P125` |
| *"Dollar near two-week high as Warsh boosts rate-hike bets"* | **REIGNITED** | 4→3 | `P125` |
| *"U.S. strikes on Iran send oil prices higher"* | FADING | 16→17→16→19→22→22→**11** | `P126` ⚠ **partial-day tag** |
| *"Qatar Extends LNG Force Majeure as Hormuz Traffic Remains…"* | FADING | 3→6→6→4→2 | `P126` ⚠ same |
| *"Two More Oil Tankers Are Attacked in the Strait"* | **ENDED** | 3→2→**12** (peak on the final day) | ⚠ **an "ENDED" thread whose last observation is its peak** — that is the partial-day artifact in its purest form, and it is flagged, not used |
| *"5 Reasons to Buy Broadcom Stock Before Its Sept. 2 Earnings"* | FADING | 3→3→2 | `S138` context |

⚠ **ENDED threads under still-open rows**: `S130`'s Hugging Face thread is **REIGNITED** (15→2→4) after
two runs of being flagged ENDED — recorded as a status change, not acted on (the row settles 09-10 and
is already noted as a dead thread in the carry).

### B-4 · Term sweep — and a **convention defect in this table itself**, found this run

🚨 **`M1240` [measured] — the same term, on the same day, returns two different counts depending on how
it is passed, and the difference reaches 8× in the Δ.** `module_news_data/_fts.py:205` defaults
`--mode and`, so an unquoted multi-word term becomes an **AND of separate argv** (`D324`'s prescription)
while a quoted one becomes a **single phrase**. Both were run today, 7-day window, `--scope foreign`:

| term | **phrase** (quoted) | **argv AND** (unquoted) | 09-01 report | Δ on the phrase read |
|---|---:|---:|---:|---:|
| `inflation` | **3,481** | 3,481 | 3,339 | +4.3% |
| `data center` | **2,730** | 3,455 | 2,691 | +1.4% |
| `tariff` | **1,966** | 1,966 | 2,025 | −2.9% |
| `Federal Reserve` | **1,530** | 1,718 | 1,485 | +3.0% |
| `rate hike` | **1,223** | 1,582 | 1,023 | **+19.6%** |
| `Strait of Hormuz` | **1,113** | 1,123 | 1,021 | +9.0% |
| `crude oil` | **993** | 1,475 | 955 | +4.0% |
| `Treasury yield` | **687** | 1,251 | 613 | **+12.1%** |
| `payrolls` | **338** | 338 | 280 | **+20.7%** |
| `refinery` | **277** | 277 | 275 | **+0.7%** |
| `AI capex` | **116** | 470 | 107 | +8.4% |
| `credit spread` | **104** | 392 | 95 | +9.5% |
| `bond selloff` (new) | — | **205** | — | new term |
| `gas turbine` (new) | — | **116** | — | new term |

★ **Why this matters and is not pedantry**: read in the argv column, `Treasury yield` is **+104%** and
`rate hike` **+55%** over one day — a regime-flip headline. Read in the phrase column, the same terms
are **+12.1%** and **+19.6%** — a normal escalation. **The 09-01 report's EXIT CHECK asserts that its
B-4 terms were passed as separate argv, yet its `Federal Reserve` count (1,485) equals its own
phrase-mode G1 probe** — so the convention that produced that table cannot be recovered from the file.
⇒ **The Δ column above is computed on the phrase read and labelled convention-ambiguous**, and the
argv column is printed beside it rather than chosen between. Registered as **`D473`** (§D-5).

**What survives either convention:** `refinery` is **flat (+0.7%)** while `Strait of Hormuz` is
**+9.0%** and `crude oil` **+4.0%**. The refiner leg is still not the crowded story — a **second
consecutive run** of the same ordering.

### B-5 · Novelty (`theme-age`, 90d, `--scope foreign`)

| theme | verdict | age | 7d avg | **accel** | base |
|---|---|---:|---:|---:|---:|
| **`Larak`** | 🟡ACCELERATING | 37 | 26.6 | **72.47×** | 198 |
| **`bond selloff`** | 🟡ACCELERATING | ≥90 | 12.7 | **3.81×** | **196** |
| `rate hike` | ⚪ECHO | ≥90 | 155.9 | 1.43× | 7,121 |
| `gas turbine` | ⚪ECHO | ≥90 | 11.3 | 1.42× | 476 |
| `data center` | ⚪ECHO | ≥90 | 334.4 | 1.02× | 18,967 |
| **`refining margin`** | ⚪ECHO | 76 | 4.4 | **0.66×** | 302 |
| **`ghost demand`** | 🟢FRESH | **1** | 0.4 | — | **3** |

★ **`M1241` [measured] — the two axes the tape moved on are at opposite ends of the novelty scale.**
`bond selloff` accelerates **3.81× on a base of 196** — it is the newest *macro* axis on the board —
while `rate hike` runs **1.43× on 7,121**, i.e. loud but not new. **`Larak` at 72.47×** (up from 58.21×
on 09-01) remains the fastest term this desk has measured. And **`refining margin` decelerates at
0.66×** for a second run, on the same day `XLE` posts **exc5 +4.91 vs `SPY`**.
⚠ **`ghost demand` is 🟢FRESH on n = 3** ⇒ **FRESH-but-thin** and **excluded from the freshness gate**
per `D461`, even though its event count rose from 3 outlets (08-31) to **6** (09-01).

### B-6 · Blind-spot pass (`blindspot --scope foreign --days 3`)

Top token-0 emergent terms are dominated by the fixed set (`AI` 1,241 · `Earnings` 590 · `Iran` 474 ·
`Trump` 451 · `China` 400 · `Oil` 355 · `Nvidia` 339 · `Fed` 279 · `Japan` 278 · `Energy` 263).
**Two terms outside the fixed table clear 180**: **`Bessent` 207** and **`Bond` 188**.

★ **`M1242` [measured] — `Bessent` is the only person-name in the top-30 that the term table does not
carry, and he is the connective tissue of §B-2's three legs**: *"Bessent's Bond Gains Wiped Out as
30-Year Yields Jump"*, *"Bessent calls time on big stimulus"* (Japan), *"Bessent meets BOJ's Ueda"*,
and *"Bessent Says Hormuz Will Soon Be 'Worthless'"* — rates, FX and oil in one actor.
⇒ **Two terms folded into the living table this run: `bond selloff` and `Bessent`.** (`gas turbine` was
also tested and is **not** folded in — ⚪ECHO at 1.42×, i.e. its REIGNITED thread is a curve shape, not
novelty.)

---

## §C · Positioning — `[COT 2026-08-25 Tue-close, 3–4 d lag]` + `[FINRA 2026-09-01]`. Context, never a trigger.

| instrument | net spec | wk Δ | 1y %ile | verdict |
|---|---:|---:|---:|---|
| **Copper** | +85,266 | +5,518 | **100%** | 🟢 crowded-long |
| USD Index | +18,682 | −397 | 74% | 🟡 |
| UST 2Y | −861,296 | +66,041 | 72% | 🟡 |
| Gold | +243,334 | +21,145 | 66% | 🟡 |
| S&P500 e-mini | **−67,994** | **−57,434 ▼** | 65% | 🟡 |
| Nasdaq-100 | +11,127 | **+23,193 ▲** | 59% | 🟡 |
| **WTI Crude** | **+31,099** | +1,935 | **43%** | 🟡 — **NOT crowded** |
| Silver | +25,261 | +1,636 | 41% | 🟡 |
| UST 10Y | −838,975 | +107,986 | 22% | 🟡 |
| Russell 2000 | −16,118 | −412 | **15%** | 🔴 crowded-short |
| Nat Gas | −197,932 | +5,571 | **2%** | 🔴 crowded-short |

★ **`M1243` [measured] — the oil move is still not a positioning chase, and the gap widened.** WTI spec
sits at the **43rd percentile** with a **+1,935** weekly change, while `CL=F` ran **83.40 (08-28) →
85.76 (08-31) → 90.22 (09-01, +5.20% in one settled session)** and `BZ=F` **89.31 → 90.49 → 94.65**.
⇒ **Speculative length is mid-range into a third week of multi-state military escalation.** This is
`P122`'s premise, re-measured on a bigger price move, and it is **context, not a trigger** — `[COT]` is
3–4 days stale by construction and cannot see 08-31 or 09-01.
⚠ **`C24` reproduces a fourth time**: copper spec at the **100th percentile** against a Materials
bucket whose repaired flow Δ is **−0.208, the board's second-worst**, on the same day *"Copper price
stalls short of record as Chile's storm-hit output slumps to 2011 low"* [5 outlets] printed. **Carried,
not resolved.**
⚠ **Nat Gas at the 2nd percentile** is the board's most crowded short and sits directly beneath a
5-outlet *"European Natural Gas Extends Climb on Supply Tightness"* and a 4-outlet *"Asia Spot LNG
Prices Hit 5-Month High as Hormuz Blockage Drags On"* — **named, not converted into a proposition**,
because the desk has no clean US vehicle for it (`L.vehicle없음`, `D456`).

---

## §D · Propositions registered this run — `P125` · `P126` · `P127` · `P128`

> IDs issued by `module_evidence next-id` (live scan of `handoff/*.md` · `llm_outputs/**` · `REPORT/**`),
> **not hand-grepped**: highest existing at write time **`M1233` · `P124` · `S140` · `D472` · `R124` ·
> `C26`**. This run takes `M1234–` · `P125–P128` · `D473–` .

### `P125` — ★★★ Is the repricing's leg flipping from REAL to INFLATION? (`P121`'s own falsifier)

**Claim.** `P121` says the repricing is the **policy path**, and through **08-31** that is measured at a
one-year extreme (**`M1234`**: 3-session Δbreakeven − Δreal = **−11.0 bp = the 5.2nd percentile**).
**On 09-01 the only observable that published moved the other way** (`T10YIE` +4 bp against a `^TNX`
+3.8 bp ⇒ real ≈ flat), and the news axis flipped with it (`bond selloff` 🟡ACCEL **3.81×**; Eurozone
CPI **3.3%**; *"Middle East turmoil reignites inflation fears"*). **Either the 09-01 print is one
session of noise inside a real-rate regime, or the leg has changed — and the desk has been carrying
the first reading for four runs.**

| | |
|---|---|
| **Frozen observable** | [3-session change in `breakeven_10y`] **minus** [3-session change in `real_10y`], both `[FRED]`, in **basis points**, at the first observation where **BOTH** series carry **2026-09-04** (`D427` — written to settle on the joint date, not on a calendar date) |
| **Branch A (the inflation leg has taken over)** | **≥ +5.0 bp** (trailing-252 **p85**) — `P121`'s frame is superseded and `S139`'s correlated-underweight logic changes character |
| **Branch B (the policy-path leg persists)** | **≤ −6.0 bp** (trailing-252 **p15**) — `P121` survives its own test |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the same 3-session spread: mean **−0.79** · sd **5.94** · p05 **−11.0** · p15 **−6.0** · p50 **0.0** · p85 **+5.0** · p95 **+9.0** ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−11.0 bp = the 5.2nd percentile** (08-31, the last joint date). ⚠ **DISCLOSED: the state is already at branch B's outer edge, so B is the WEAK-information branch and A is the informative one.** A B print changes nothing; an A print reverses a four-run carry |
| **Anti-signal (VOID)** | a FRED methodology change or a data revision notice on `DFII10`/`T10YIE`, **or** an unscheduled Federal Reserve action, inside 09-01 → 09-04. ⚠ **Base rate checked**: no FOMC meeting falls in the window |
| **Track KPI** | if **A** fires, `^TYX − ^FVX` should **steepen**; if **B** fires it should **flatten further**. The 09-01 session flattened (**+1.9 bp vs +5.0 bp**), which is B's shape ⇒ **the KPI and the level currently disagree, and that disagreement is registered now rather than discovered at scoring** (`D450`) |
| **Dated catalyst** | **August payrolls, 2026-09-04** [`catalyst_calendar` D-2, `bls≈`, 🔀binary] |
| **Thread** | BUILDING *"Markets slide as inflation fears trigger global bond selloff"* **4→4→7**; BUILDING *"Euro area: Inflation jump supports ECB hike"* **5→2→2→4→6** ⚠ the 09-02 leg of both curves sits on a **partial day** |
| **Non-redundancy (`D343`)** | `S126`/`S134`/`S139`/`P114` all settle 09-04 on **equity** observables; `P121` is a **level** claim about the policy path. **No existing row measures which LEG of the nominal yield is moving**, which is the question `P86`'s dissenting KPI (`M1166`) left open |
| **Owner** | `industry_US` |

### `P126` — ★★★ Is the escalation finally paying the BARREL, or still only the CHAIN?

**Claim.** `M1201`/`M1202` established that Energy's OW was a **chain-position** bet: ex-`XOM` flow
**+0.471** vs headline +0.302, `XOM` the sector's only negative row, and the universe's only two
ignitions (`SLB`, `WMB`) neither of them a barrel. **That was measured before `CL=F` rose 5.20% in one
settled session.** Today the barrel names are at the **75.4th percentile** vs `SPY` on five sessions —
and the refiner names, whose 20-session leadership just fired `P100`-A at **+21.963pp**, are *still*
ahead of them. **Both legs are strong at once, which is exactly the state `M1201` said did not exist.**

| | |
|---|---|
| **Frozen observable** | `EW{XOM, CVX, EOG, FANG}` **minus** `EW{MPC, VLO, PSX}`, **5-session** returns, settled closes, `auto_adjust=False`, at the **2026-09-09** close |
| **Branch A (the barrel leg is finally paid)** | **≥ +2.312** (trailing-252 **p85**) — the chain-position reading is superseded and the OW's centre of gravity moves upstream |
| **Branch B (chain position persists)** | **≤ −4.443** (trailing-252 **p15**) — `M1201`/`M1202` replicate through a 5% barrel move, which would be strong evidence the refiner leg is a margin story and not an oil story |
| **Branch C** | between = the disclosed favourite |
| **`D93` executed BEFORE freezing** | trailing 252: mean **−0.987** · sd **3.503** · p05 −7.269 · **p15 −4.443** · p50 −0.637 · **p85 +2.312** · p95 +4.369 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−4.210 = the 17.5th percentile** (09-01 settled) — **just outside B**, so B is near and A is far. **Both branches are reachable; the asymmetry is disclosed, not hidden** |
| **Anti-signal (VOID)** | an **OPEC+ emergency production decision**, a **US SPR action**, or **announced M&A involving any of the seven names**, inside 09-02 → 09-09. ⚠ **Base rate checked** (`D300-KR`): the 8-day `fts` window returns **220 `OPEC` hits with no production decision** — the OPEC-adjacent story is *Venezuela weighing an OPEC exit* [bloomberg/investing_en, 08-27/28], which is **structural, not a production decision**, and therefore explicitly **not** a voider. **The Hormuz escalation is NOT an anti-signal — it is the event** |
| **Track KPI** | if **A**, `CL=F` should hold above **$88**; if **B**, the 3-2-1 crack should widen while `CL=F` is flat-to-down |
| **Dated catalyst** | the Hormuz axis's **undated** binary (*"Iran 'Strait of Hormuz open' statement"*, `catalyst_calendar` `[news👁]`) + weekly EIA prints. ⚠ **No date is invented for the undated one** |
| **Thread** | REIGNITED *"Commodities: Middle East Escalation Pushes Energy Prices…"* 2→4; BUILDING *"Bessent Says Hormuz Will Soon Be 'Worthless'"* 2→2; ⚠ FADING *"U.S. strikes on Iran send oil prices higher"* 16→…→22→**11** on a **partial day** — not read as decay |
| **Non-redundancy (`D343`)** | `S136` (09-09) asks whether the Energy escalation is a **barrel or chain-position** event through a *different* observable; `P122` (09-08) is a **positioning** claim. **`P126` is the direct pair spread and can disagree with both** — and if it does, the disagreement is the finding (`S14-ANNEX` precedent) |
| **Owner** | `industry_US` |

### `P127` — ★★ Did the AI marginal dollar go to POWER, or come back to COMPUTE?

**Claim.** `P123` (09-08) says the AI trade's marginal dollar moved from compute to power. The board
now carries a **dated falsifier and a dated confirmer on the same day**: Texas halted data-center power
over *"ghost demand"* [**6 outlets**, up from 3] against *"Gas Turbine Prices Are on Track to Nearly
Triple"* [REIGNITED **5→3→8**], *"Google Just Locked Up the Largest Geothermal Power Deal Ever Made"*
[6] and *"The U.S. Army Will Spend $2.2 Billion on Micro Nuclear Reactors"* [4]. **The tape is not
resolving it**: AI-power EW is **−1.524 vs `SPY` (34.5th %ile)** while AI-compute EW is **+0.890
(54.0th %ile)**, and the pair spread sits at the **25.4th percentile**.

| | |
|---|---|
| **Frozen observable** | `EW{VST, CEG, TLN, NRG, GEV, ETN, PWR}` **minus** `EW{NVDA, AVGO, ANET}`, **5-session** returns, settled closes, window **2026-09-03 close → 2026-09-10 close** |
| **Branch A (power wins the marginal dollar)** | **≥ +4.555** (trailing-252 **p85**) — `P123` confirmed on a pair spread rather than on a level |
| **Branch B (compute takes it back)** | **≤ −5.790** (trailing-252 **p15**) — `P123` falsified; the AI trade re-concentrates in the epicenter the book already holds |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252: mean **−0.524** · sd **4.957** · p05 −9.201 · **p15 −5.790** · p50 −0.231 · **p85 +4.555** · p95 +7.585 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | **−3.666 = the 25.4th percentile** (09-01 settled) — inside C, leaning B |
| **⚠ Window chosen to EXCLUDE a known contaminant** | `AVGO` prints **tonight (09-02 after close)**. A 5-session window ending 09-09 would start on **09-02** and put the print reaction inside the compute leg. **The window therefore starts at the 09-03 close** — the print day becomes the *base*, not a return inside the window. **This is the D-0 binary being designed around rather than voided on** |
| **Anti-signal (VOID)** | a **dated federal or ERCOT-wide action on data-center power siting**, or an **`NVDA`-specific guidance event**, inside 09-03 → 09-10 |
| **Track KPI** | if **A**, `gas turbine` theme-age should leave ⚪ECHO (currently **1.42× on 476**); if **B**, `ANET`'s `[FINRA]` z should retreat from **+2.25** |
| **Dated catalyst** | `AVGO` **09-02** (the base, not the window) · `P123`/`S140` settle **09-08** |
| **Thread** | REIGNITED *"Gas Turbine Prices…Nearly Triple"* **5→3→8**; REIGNITED *"Bloom Energy's Backlog Will Top $50 Billion"* 6→4→6→4; the falsifier *"Texas' halt… 'ghost' demand"* is 🟢FRESH **but n = 3 ⇒ FRESH-but-thin, excluded from the gate** (`D461`) |
| **Non-redundancy (`D343`)** | `P123` is a **level** claim; `S140` measures IT **breadth**; `S137` measures optical vs `SMH`. **None is a power-vs-compute pair spread**, and `D416` has carried "the AI-power cycle has no registry row" for five runs |
| **Owner** | `industry_US` |

### `P128` — ★★ Does the global bond selloff reach US CREDIT, or is it a rates-only event?

**Claim.** The loudest macro story of the week is a bond selloff, and **US high-yield credit is at the
0.4th percentile of its trailing year** (`M1236`). Two of this desk's credit instruments have now
declined to confirm the AI-capex-to-debt thesis (`S111` C at `ig_oas` 0.79; `P67` ARMED with `hy_oas`
25 bp further from its trigger than at registration). **Either credit is the last domino and it falls
next, or this is a rates-and-FX event that never touches spreads — and those two produce opposite
sector conclusions for Financials and Real Estate.**

| | |
|---|---|
| **Frozen observable** | `hy_oas` `[FRED]` **5-session change in basis points**, at the first `[FRED]` close covering **2026-09-08** |
| **Branch A (credit joins)** | **≥ +10.3 bp** (trailing-252 **p85**) — the rates event transmits to spreads; `P67`'s mechanism gains its first supporting instrument |
| **Branch B (credit keeps decoupling)** | **≤ −9.0 bp** (trailing-252 **p15**) — HY tightens *further* from a one-year low into a multi-decade-high yield print, which would make the "credit stress" reading unusable for the rest of the quarter |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of `hy_oas` 5-session change (bp): p05 **−17.0** · **p15 −9.0** · p50 **−1.0** · **p85 +10.3** · p95 +18.0 ⇒ **A ≈15% · B ≈15% · C ≈70%** |
| **State at registration** | 5-session change **−6 bp**; level **2.63 = the 0.4th percentile of 252** (levels: p05 2.67 · p50 2.83 · p95 3.19). ⚠ **The LEVEL is at an extreme while the CHANGE is mid-pack — those are different objects and the row is written on the change** (`D3`) |
| **Anti-signal (VOID)** | an idiosyncratic HY default or distressed exchange above **$5bn**, or an ICE index-methodology/rebalance notice, inside the window |
| **Track KPI** | `ig_oas` should move **with** `hy_oas` if A is a genuine credit event; if `ig_oas` stays inside 0.79–0.81 while `hy_oas` widens, the move is **idiosyncratic HY supply**, not credit stress |
| **Dated catalyst** | August NFP **09-04** · `P122`/`P123`/`S127`/`S140` settle **09-08** |
| **Thread** | *no matching thread* — **stated explicitly**. `credit spread` runs **104** hits (phrase, 7d), the smallest bucket on the board. **A macro axis with no narrative is exactly where an unpriced move can start**, and it is registered on that basis, not on a story |
| **Non-redundancy (`D343`)** | `P67` is a **level** trigger at 2.85 and has been un-fired for weeks; `S111` measured **IG** and scored C. **`P128` is the first row on the HY rate-of-change**, which is the quantity that moves before a level trigger is reached |
| **Owner** | `industry_US` |

### D-5 · Digs registered by this stage

- **`D473`** ★★★ — *A term-sweep table records the **exact CLI invocation** beside its counts, and a
  Δ is computed only against a prior run whose invocation is recorded.* **Measured origin `M1240`**:
  the same term on the same day returns **1,530 (phrase)** vs **1,718 (argv AND)**; on `Treasury
  yield` the two conventions give a one-day Δ of **+12.1%** and **+104%** respectively. The 09-01
  report asserts argv in its EXIT CHECK while its numbers match phrase, so **its convention is not
  recoverable from the file** and every Δ across the two runs is ambiguous.
- **`D474`** ★★ — *On `--scope foreign`, the `single_source` tier is reported as a **random sample of
  n**, never as a recovery.* **Measured origin `M1238`**: `scored 0 / scorable 0 / unscored 643` —
  the classifier is Korean-only, so 15 of 643 are shown at random and **628 clusters (42.6% of the
  day's clusters) are unseen**. The tier's own note says it "carries FX and rates single-articles",
  which is true on the KR runtime and **structurally false on this one**.
- **`D475`** ★ — *A `thread` window ending on a partial collection day marks every window-end tag as
  **provisional**, and an ENDED thread whose final observation is its **peak** is reported as an
  artifact rather than as a death.* **Measured origin**: 09-02 carries **421** articles against
  745–856 on full days, and *"Two More Oil Tankers Are Attacked in the Strait"* is tagged **ENDED**
  with a curve of **3→2→12**.

---

## §E · ★ Sector transmission matrix — the deliverable, and ROTATION's input

> Wind direction only; **ROTATION** issues verdicts. Excess returns vs **`SPY`** (named inline, `C1`),
> settled closes ending **2026-09-01**. Flow from **`SECTOR_FLOW_US_REPAIRED.json`** (asof 09-01,
> 3-axis `nonews`); **Δ is direction only** (§0).

| # | Sector | wind | driving prop. | flow `eqflow` / Δ | exc1 / exc5 / exc20 | note |
|---|---|---|---|---|---|---|
| 1 | **Energy** | **OW** | **`P126`** · `P122` | **+0.551** / **+0.295** | **+1.95 / +4.91 / +11.92** | The board's only sector strong on *every* window and on flow Δ. ★ `P100` **FIRED-A** on the refiner leg (+21.963pp vs ≥+13.478) and the barrel leg is now at the **75.4th %ile** — **both legs strong at once**, which `P126` exists to resolve. `refining margin` still ⚪ECHO **0.66×** |
| 2 | **Health Care** | **OW−** | `P125` (a duration-sensitive bucket) | **+0.265** / **+0.214** | +1.35 / −1.53 / **+7.14** | The 20-session leader ex-Energy, and flow Δ agrees. ⚠ A **named, dated negative**: MFN pricing extended to 9 mid-sized drugmakers [5 outlets] + *"Novartis pauses trials after three deaths"* [7]. `S133` settles 09-14 |
| 3 | **Materials** | **N, contested** | — (no proposition drives it — **that absence is the finding, 2nd run**) | −0.076 / **−0.208** | −0.49 / −2.28 / +1.37 | ⚠ **`C24` 4th reproduction**: copper spec **100th %ile** `[COT]` against the board's 2nd-worst flow Δ. `NEM` turned 🟢 by crossing a `vol_surge` gate it missed **by 0.01** yesterday (`C5`) and carries `[FINRA]` z **−3.14**, the board's most extreme short exit |
| 4 | **Information Technology** | **N** | `P127` · `S140` | −0.252 / −0.173 | −0.85 / **+1.58** / −0.51 | ⚠ **`XLK` +1.58 vs `SMH` −1.37 on exc5 — the label is two bets** (`W5`). `AVGO` prints **tonight**; `S138` (±11.00pp, outside the measured ±9.6% implied move) is the informative bracket, `S132` (±9.00pp) is **pre-declared NO-INFORMATION** (`M1197`). Shorts pressed the epicenter: `ANET` z **+2.25**, `NVDA` **+2.18** |
| 5 | **Consumer Staples** | **N** | `P125` | −0.086 / +0.060 | +1.00 / −0.93 / +1.10 | 🚫 **No `wflow` verdict permitted** — the primary and repaired sweeps disagree about whether `WMT` (28.9%) owns the sign (PREFLIGHT G3) |
| 6 | **Utilities** | **UW, under live challenge** | **`P127`** · `P125` | −0.223 / **+0.267** | **+1.47** / −1.19 / −2.28 | ★ The clearest tension on the board: the **best flow Δ but one** and the **best exc1**, against the worst exc20. Two dated causes on opposite sides — the Texas "ghost demand" halt [6] and the California wildfire-bill postponement [6, utilities bounced]. `S135` settles 09-11 |
| 7 | **Real Estate** | **UW** | `P125` · `P128` | −0.194 / +0.178 | +0.53 / −2.37 / −1.26 | A duration proxy under a front-end repricing. If `P125`-A fires, this reads differently — **stated now, not at scoring** |
| 8 | **Financials** | **N** | **`P128`** | −0.220 / **−0.220** | −0.20 / −1.36 / +0.06 | The verdict moved `OW− → N` on 09-01. `hy_oas` at the **0.4th %ile** is the strongest thing that could be said *for* the bucket, and `P128` is the row that tests whether it survives the week |
| 9 | **Consumer Discretionary** | **UW** | `P125` | −0.232 / −0.004 | −1.03 / −2.31 / −1.89 | ⚠ **PREFLIGHT G3 bars a `wflow` verdict change** (`AMZN` 40.2%, and the weight is 49 days stale). A named dated negative — the FTC/state ad-auction suit [13 outlets] — landed on that same 40.2% name |
| 10 | **Industrials** | **UW** | `P125` · `S126`(09-04) | −0.447 / **−0.222** | −0.68 / **−2.64** / **−6.10** | **The worst sector on 5 and 20 sessions and the 3rd-worst flow Δ** — the most internally consistent negative on the board. `S126`/`P114` settle at the **NFP on 09-04** |
| 11 | **Communication Services** | **no verdict issued** | — | **−0.013** / +0.029 | +0.17 / −1.49 / +0.20 | 🚫 **`wflow` barred entirely**: Alphabet is **76.6%** of the bucket under **two** tickers and `top1_flips_sign` prints **False** while ex-both-classes `wflow` is **+0.257** (swing **0.763**, `D459` 2nd reproduction). `eqflow` **−0.013** is the only citable aggregate and it is flat |

★ **The one-line wind reading:** **the escalation is paying Energy on every window, the rate complex is
draining Industrials and the duration proxies, and the AI label has split into a compute leg the shorts
are pressing and a power leg with a live dated falsifier.** The single number that could change all of
it is `P125`'s, and it settles **2026-09-04**.

---

## §F · Self-backtest — this desk's own hit rate

### F-1 · Rows settled this run: **0** — and the reason is structural, not an absence of due rows
`S109` (`FRO`) is due **today** and its observable is **tonight's close**; this desk fires at 09:09 ET.
**`D426`, third consecutive run.** Reference pre-settle (**explicitly not a score**, `D242`): window
08-26 → 09-01 gives `FRO` **+7.5728%** vs `SPY` **−0.5613%** ⇒ excess **+8.134pp**, **0.091pp above
branch A's +8.043**, with one session left. **0 `EXPIRED` · 0 silent skips · 1 unscoreable (`S8`, 35th
run).** Full accounting in `HANDOVER §2`.

### F-2 · ★ A MACRO proposition settled and **nobody had scored it** — `P100`, `FIRED-A`

`P100` was registered by the 2026-08-26 MACRO stage with a frozen observable at the **2026-09-01**
close. **It appears nowhere in `SCENARIOS.md`'s master index or scoring log** — it lived only in a run
report, which is precisely the failure `D449` names. Scored here:

| | |
|---|---|
| **Observable** | `EW{MPC, VLO, PSX}` 20-session excess vs **`SPY`**, settled closes, `auto_adjust=False`, window **2026-08-04 → 2026-09-01** |
| **Result** | `MPC` **+22.517%** · `VLO` **+17.251%** · `PSX` **+22.405%** ⇒ EW **+20.724%**; `SPY` **−1.238%** ⇒ **excess +21.963pp** |
| **Branches** | A ≥ **+13.478** ✅ · B ≤ −4.731 ❌ ⇒ **`FIRED-A`** |
| **Registration state** | **+11.597 = 77.4th percentile** (inside C, leaning A). The settle sits at the **~94.9th percentile**, just below the p95 of +22.084 |
| **Anti-signal (VOID) checked** | no OPEC+ emergency production decision, no US SPR action, no M&A involving the three names. `fts search OPEC --days 8 --scope foreign` returns **220 hits**; the OPEC-adjacent story is *Venezuela weighing an OPEC exit* [bloomberg 08-27/28, investing_en 08-28] — **structural, not a production decision** ⇒ **VOID does not fire** |
| ⚠ **What weakens the win** | `P100` was designed as *"was it the margin story or the barrel?"* and its discriminator was a **barrel break**. **The barrel broke and then reversed inside the same window** — `CL=F` fell to **82.23 (08-26)** and rose to **90.22 (09-01)**. ⇒ **A fired, and the mechanism it was built to separate did not stay separated.** Recorded beside the verdict rather than used to re-band (`D242`/`D445`), and it is the direct reason `P126` exists |

### F-3 · The pattern in the misses, carried and now with a **counter-instance**
The standing record is that **a pre-settle read on this desk has never yet been right** — wrong in sign
three times (`S101`, `P78`, `P96`) and wrong in magnitude a fourth (`S103`, 2.1×). ★ **`M1244`
[measured] — `P100` is the first counter-instance.** Its 08-26 registration state (+11.597, inside C
leaning A) pointed at the branch that fired, and the 09-01 settle exceeded it. ⇒ **the rule is amended,
not repeated: pre-settle *reads* have been unreliable; a *registration state* leaning toward the branch
that fired is a different and, on this one sample, better-behaved object.** `n = 1` (`S5`).

### F-4 · 🚨 What this stage asserted and then refuted, in the same run (`§4c` / `D48`)
★ **One, and it is the run's largest number.** The first pass of §B-4 was written from the **unquoted
argv** sweep and carried *"`Treasury yield` **+104%** and `rate hike` **+55%** in a single day"* as
evidence that the narrative had flipped regime. **Re-running the identical terms in the phrase
convention the prior run's numbers actually match gives +12.1% and +19.6%** — **the claim was an
artifact of how the CLI was called, and it was eight times too large.** The sentence is recorded here
rather than deleted, and `D473` is its dig.
⚠ **Zero self-refutations would itself be worth a line.** This stage has one; `HANDOVER §8` has two
more (the repair's "0/42 label flips" and the "08-28 will backfill" framing).

---

## ✅ EXIT CHECK

- [x] **Catalysts injected** — `catalyst_calendar --days 10` (not `--days 5`: `S138`'s `AVGO` print and
      `P122`/`P123`/`S127`/`S140` on 09-08 sit at or beyond the default edge). **5 binaries in window**:
      `AVGO` **D-0 (today)** · NFP **09-04** · PPI 09-10 · CPI 09-11 · the undated Hormuz statement.
      ⇒ **PREMORTEM must produce a both-sides bracket for the two ≤48h binaries**; standing both-sided
      rows already exist (`S138`/`S127`/`S132` for `AVGO`; `S126`/`S134`/`S139`/`P114`/`P121` for NFP)
      and PREMORTEM's job is to verify their reachability, not to re-register them. Saved to the
      day-folder root as `CATALYST_WATCH.json`.
- [x] **Narrative read**: events (`brief --body 2`) + trajectories (`thread --days 7`) + term sweep
      (14 terms, **both conventions**) + `theme-age` (7 themes) + blindspot. **Indicators read**: FRED
      14 series `--json`, COT 11 instruments, FINRA 16 names. **Daily anchor read** =
      `llm_outputs/2026-09-01/industry_US/MACRO_REPORT.md` + `module_report_tags show`.
- [x] Events read via `--body 2`; **tail = 0**.
- [x] **`tail = 0` is NOT treated as the coverage claim** (§B-1): `single_source` **643 counted / 15
      shown ⇒ 628 withheld, all `unscored`**; `excluded_nonmarket` **0/0**; `subevents_recovered`
      **232**. Stated coverage: **845 of 1,473 clusters = 57.4%**. **No "quiet bucket" claim appears
      anywhere in this report.**
- [x] **Denominator is the corrected one** — **5,212 articles**, with `excluded_not_news = {}` printed
      and stated rather than assumed.
- [x] **Trajectories read; every proposition carries a thread tag + curve** — `P125` BUILDING 4→4→7 and
      5→2→2→4→6 · `P126` REIGNITED 2→4 + BUILDING 2→2 · `P127` REIGNITED 5→3→8 · **`P128` explicitly
      "no thread", and the absence is used as part of its rationale.** The partial-day caveat is
      attached to every window-end tag (`D475`).
- [x] Every "nothing happened" claim carries its denominator — **none is made**.
- [x] **No bucket count is trusted from a single convention** — both conventions are printed and the
      ambiguity is registered as `D473` rather than resolved silently.
- [x] **Both halves cited** (`C2`): the rate move (level **up** and curve **flattened**); the leg
      decomposition (real-led through 08-31 **and** breakeven-led on 09-01); `hy_oas` (level at a
      one-year **tight** and 5-session change **mid-pack**); `XLK` **vs** `SMH`; monthly FRED series
      (`core_cpi`/`cpi`/`m2`/`unemployment`, all dated **2026-07-01**) flagged as ~1 month lagged and
      **not used in any proposition**.
- [x] **Every relative-performance number names `SPY` inline.** No statistical result carried across
      markets — the `vol_surge` IC result is `market=kr` and is **not** used (`W1`), and the KR desk's
      `rs20` bench defect (`R122`) was **re-checked on `SPY` rather than imported** (`SPY` has 0
      missing bars in the 20-session window).
- [x] **Credit axis read and cited** — `hy_oas` **2.63 (0.4th %ile)** · `ig_oas` **0.80** · `NFCI`
      **−0.558**. **No credit-stress claim is made; §A-3 measures the opposite and labels it.**
- [x] **`real_10y` quoted with `breakeven_10y`** — §A-1 is built on exactly that pair, and the one
      session where the pair is unavailable is marked `C3` (unknown column) rather than filled in.
- [x] **Linter run on this stage's own output** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-09-02/industry_US/MACRO_REPORT.md` ⇒ **0 findings** (rules C1·C2·S6·D6). ⚠ It checks form only; a clean run is not a correct report.
- [x] **Transmission matrix produced, all 11 sectors, one line each** (§E), with three sectors
      explicitly barred from a `wflow` verdict by PREFLIGHT G3.
- [x] **Self-backtest appended** (§F) — 0 rows settled with the structural reason; **`P100` scored
      `FIRED-A` after being found unregistered**; the pre-settle pattern amended with its first
      counter-instance; one in-run self-refutation recorded.
- [x] **New blind-spot terms folded into the living table**: **`bond selloff`** and **`Bessent`**
      (`gas turbine` tested and **not** folded, with the reason stated).

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **SWEEP** (Stage 4).
> ⚠ SWEEP inherits: cite `SECTOR_FLOW_US_REPAIRED.json` only; Δflow is a **one-session** (08-31 → 09-01)
> quantity and is **direction-only**; and §E's tape leaves it one arbitration — **`XLK` +1.58 vs `SMH`
> −1.37 on exc5**, i.e. whether the IT label is one bucket or two.

---

# §5 · DRIFT ADDENDUM — appended 2026-09-02 23:25 KST (Stage 11 / L1·DRIFT)

> **Append-only.** Nothing above this line is rewritten. The original call stays visible beside its
> challenge — that asymmetry is the self-backtest's food (`D48`).

## 5.0 · Spec compliance, stated first
🚨 **`D282` reproduces for a 7th consecutive run.** `drift_watch` ran at **+0.6h** after the report's
baseline (`MACRO_REPORT.md` completion **2026-09-02T22:47**, watch **23:24 KST**) against the stage's
**3–6h** spec. The run's clock is a scheduler property, not a choice available inside the run;
**the fix is scheduling and is a human item (P5).** ⚠ A +0.6h window sees a smaller post-run sample,
so **a quiet drift check at this lag is weak evidence of quiet**, and this addendum does not read it
as such.
⚠ **Clock note**: at write time it is **10:2x ET and the NYSE is open**. **No claim about the 09-02
tape appears anywhere in this addendum** — PREFLIGHT's revocation stands, and `AVGO` prints **after
today's close**, so nothing below is post-print.

## 5.1 · Four 🚨 bursts fired. **One is real; three are term-matching artifacts, and they are named.**

| burst | multiple | body-read verdict |
|---|---:|---|
| **`rate hike`** | **4.6× on 19 articles** | ✅ **REAL and on this report's own spine** — §5.2 |
| `strikes on Iran` | 5.6× on **3** | 🚫 **artifact** — 2 of the 3 sampled titles are substring false positives: *"**CrowdStrike** and federal authorities dismantle Russian malware…"* matches on `strike`, and *"The token supercycle"* has no Iran content. Only *"What is Iran's Castle Breaker missile, used against US bases?"* is on-axis, and it is an explainer, not an event |
| `invasion` | 3.3× on **3** | 🚫 **artifact** — *"FBI investigating 153 million driver's licenses leaked on a Russian cybercrime forum"* and *"Citibank's London unit fined £4.7m for breaching Russia sanctions"* are Russia-keyword matches with **no market-regime content**. *"Putin and Zelenskyy issue threats"* is on-axis but continues a thread already carried |
| `downgrade` | 3.2× on **3** | 🚫 **`D462` reproduces, 2nd time** — all three are **single-name analyst-action items**: *"Dell's Insane Numbers Terrified Me — In The Best Way Possible (**Downgrade**)"* (a title whose own body is bullish), *"Broadstone Net Lease (Rating Downgrade)"*, *"J.P. Morgan cuts NIO to Neutral"*. **No regime content.** The dig's prescription — *exclude single-name analyst roundups from the `downgrade` term set, or retire the term* — remains **unimplemented** (human item) |

★ **Three of four 🚨 are noise, and naming which three is the useful output.** A drift watch that
reports four alarms and lets the reader assume four events is worse than one that reports one.

## 5.2 · The real burst — and it **corroborates** §A-2 with a source the report did not have

**19 articles at 4.6× on `rate hike`**, body-read (`--scope foreign`, ≥9s spacing):

| dated fact | source |
|---|---|
| *"Fed Chair Kevin Warsh Pushed September **Rate Hike Odds Past 50%**. But 1 Investor Says the Market Has It Wrong"* | yahoo_finance, **09-01** |
| *"Markets see Warsh endorsing a rate hike in September. **Not everyone is convinced**"* | cnbc, 08-31 |
| *"**Jobs Data Could Complicate the Fed's Rate Hike Plans**"* | yahoo_finance, **09-02** |
| *"Fed's **Barr** warns on sticky inflation, keeps rate hike…"* | fxstreet, 09-02 |
| *"US Dollar: **Fed hike risk and yields back in focus**"* | MUFG via fxstreet, 09-02 |
| ★ *"Fed Chairman Kevin Warsh warned about inflation — **but that's not why long-term rates are surging**: Chart of the Day"* | yahoo_finance, 08-31 |

★★ **`M1261` [measured] — the last row is an independent source arguing exactly what §A-2 measured
from the curve, and the report did not have it when §A-2 was written.** §A-2's claim was built only
on the shape (`^FVX` **+5.0 bp** > `^TNX` +3.8 bp > `^TYX` **+1.9 bp** on 09-01 = bear-flattening,
i.e. policy path rather than term premium). A named outlet now makes the same separation in prose.
⇒ **§A-2 is CORROBORATED, not corrected.** ⚠ **This is corroboration, not confirmation of `P121`** —
it addresses the *long end vs policy path* axis, while `P125`'s question is *real vs breakeven*, and
those are different decompositions (`C3`: do not let one stand in for the other).

★ **And the burst hands `P125` its own timing**: *"Jobs Data Could Complicate the Fed's Rate Hike
Plans"* is dated **09-02** and points at the **09-04 NFP — the exact date `P125` settles on.**
Both sides are present in the corpus (**"odds past 50%"** vs **"not everyone is convinced"** vs
**"1 investor says the market has it wrong"**), which is what a genuinely two-sided binary looks like.

## 5.3 · What changes, and what does not

**Changes: nothing.** No verdict, no threshold, no branch.
- 🚫 **`P125` is NOT re-banded** (`D242`). Its observable is frozen `[FRED]` and its settle date is
  the joint 09-04 observation. A news burst is not the observable.
- 🚫 **`S141` and `S142` are NOT re-banded.** Both were registered hours ago with 252-obs percentiles
  and both are labelled `implied-move UNCHECKED`; the burst does not touch either.
- 🚫 **No ALPHA tag is upgraded.** `bond selloff` remains 🟡ACCELERATING at 3.81× and `rate hike`
  remains ⚪ECHO at 1.43× **on a base of 7,121** — a 4.6× *post-run* burst on a huge base is a
  **within-day** spike, not a change of theme age, and the two instruments are not conflated.

**Stands, with its confidence raised by one independent source:** §A-2's *"the curve's SHAPE says
policy path even while the headlines say fiscal"*.

**Stands, unchanged and unresolved:** §A-1's flag that the **09-01 leg cannot be decomposed** because
`DFII10`/`DGS10` stop at 08-31 while `T10YIE` carries 09-01 (`D427`, 3rd run). **The burst does not
supply the missing column** and no substitute is invented.

## 5.4 · Anti-signals re-checked against the burst (the report's own VOID clauses)
| row | VOID clause | fired? |
|---|---|---|
| `P125` | FRED methodology/revision notice on `DFII10`/`T10YIE`, or an **unscheduled** Fed action | ❌ — Warsh's speech was **scheduled** (Jackson Hole, 08-28) and Barr's remarks are commentary, not action |
| `P126` | OPEC+ emergency production decision · US SPR action · M&A among the seven | ❌ (`Strait of Hormuz` shows **7 non-burst** hits, below threshold) |
| `P127` | dated federal/ERCOT-wide action on data-center power siting · `NVDA`-specific guidance event | ❌ |
| `P128` | HY default/distressed exchange > $5bn · ICE index-methodology notice | ❌ (`default` 3 hits, `bankruptcy` 1 — both **non-burst**) |
| `S141` | market-wide halt · **dated** US export-control action on advanced semis | ❌ (`circuit breaker` 2 hits, non-burst) |

**Zero VOID clauses fired.** ✅

---
> Watch window **2026-09-02 22:47 → 23:24 KST (+0.6h)** · `drift_watch.py --report
> llm_outputs/2026-09-02/industry_US/MACRO_REPORT.md` · 4 bursts, **1 real / 3 artifacts** ·
> **0 verdicts changed · 0 thresholds moved · 0 VOID clauses fired · 1 claim corroborated.**
