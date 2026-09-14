# MACRO_REPORT — industry_US · 2026-08-29 (Stage 3 / L1·MACRO)

> Run fires **Sat 09:1x ET**. The **2026-08-28 US session is fully settled** — the first US run in
> four whose own headline date is behind it rather than ahead of it. Every price below is a settled
> close unless labelled otherwise.
> ★ **Warsh delivered his first Jackson Hole speech as Chair on 08-28 and it was hawkish.** That is
> the single event this report is organised around.

---

## §0 · Rights removed before any number below is read

From `preflight/PREFLIGHT.md` (Stage −1) and `HANDOVER.md` (Stage 2). These bind every line:

1. **No news-velocity or theme-freshness citation, and no "quiet"/"no news" verdict** on any name or
   sector (G1 FAIL, `vel_coverage` 16.72%). Bucket denominators below are **counts**, never freshness.
2. **No cross-sectional use of the partial velocity subset** — it is a market-cap rank prefix (1–50).
3. **No bare concentration number** — every unit count carries its `--days` (G4 FAIL).
4. **`wflow` is not a current weighting** — 45-day-old caps (G5 FAIL). Prefer `eqflow`; tag `wflow`.
5. **Information Technology and Health Care may not be promoted/demoted on the weighted-flow bucket**
   (G3 flippers: IT/`NVDA`, HLTH/`LLY`).
6. **No IC-backed sizing language** (G6 FAIL).
7. 🚨 **`R108` (filed 2026-08-29 by `industry_kr`)**: the flipper/rank output of `sector_flow` may be
   used to **withhold** a promotion but **not** as evidence that the non-flippers are clean.
8. 🚨 **`D401` (registered this run)**: **no `SECTOR_FLOW_US.json` figure may be described as a
   settled reading** — its terminal bar is an intraday print (HANDOVER §11a). **This report therefore
   builds its tape section from settled ETF closes, not from the sweep file.**
9. 🚨 **`D402`**: `repair=True` output is not a settled price. All 08-28 closes below come from
   `fast_info.last_price`, corroborated in HANDOVER §2e.

---

## §A · Instruments

### A-1 · FRED primaries `[FRED]` — with each series' staleness stated

| series | last obs | value | 365d min–max | %ile | 5-obs change | staleness |
|---|---|---|---|---|---|---|
| `DGS10` | 2026-08-27 | **4.67** | 3.97–4.75 | **94.0** | −0.02 | 1 business day |
| `DGS2` | 2026-08-27 | **4.20** | 3.38–4.37 | **92.0** | +0.01 | 1 bd — 🚫 **08-28 bar not published** |
| `DGS30` | 2026-08-27 | **5.19** | 4.54–5.31 | **94.0** | −0.04 | 1 bd — 🚫 **08-28 bar not published** |
| `DGS5` | 2026-08-27 | 4.38 | 3.51–4.46 | **95.2** | −0.01 | 1 bd |
| `T10YIE` (breakeven) | **2026-08-28** | **2.31** | 2.18–2.50 | **53.6** | −0.03 | **current** |
| `DFII10` (real 10y) | 2026-08-27 | **2.34** | 1.67–2.47 | **88.8** | −0.01 | 1 bd |
| `VIXCLS` | 2026-08-27 | **14.51** | 13.47–31.05 | **3.9** | −1.50 | 1 bd |
| `DTWEXBGS` (broad USD) | 2026-08-21 | 118.06 | 117.44–121.92 | 9.4 | −0.84 | 🚨 **8 days** |
| `FEDFUNDS`/`SOFR` | 2026-08-27 | 3.63 / 3.64 | — | 31.0 / 38.3 | 0.00 / +0.01 | 1 bd |
| `UNRATE` | 2026-07-01 | 4.10 | 4.10–4.50 | 8.3 | −0.30 | **~2 months** |
| `CPIAUCSL` / `CPILFESL` | 2026-07-01 | 332.813 / 336.789 | — | — | +5.35 / +3.28 | **~1 month** |
| `M2SL` | 2026-07-01 | 23,218 | 22,025–23,218 | — | +619.1 | **~1 month** |
| `RRPONTSYD` | **2026-08-28** | 0.175 | 0.03–105.99 | 4.4 | −0.025 | current |
| `WALCL` (Fed assets) | 2026-08-26 | 6,730,912 | 6.54m–6.76m | 82.7 | −16,466 | 3 days |

★ **`M1046`** `[measured]` **The long end is at the top of its year and it is a REAL-rate level, not
an inflation-expectations level.** `DFII10` **2.34 = 88.8th percentile** against `T10YIE`
**2.31 = 53.6th percentile** — the required pairing, and it separates cleanly. A 30-year yield at the
94th percentile with breakevens at the median is a **term-premium / real-rate** condition. 🚫 Any
"the long end is inflation" reading is refused by this pair. (This is the exact separation `S120`
brackets, and `S120` cannot settle because `DGS30`'s 08-28 bar has not published.)

⚠ **`M1047`** `[measured]` **The dollar series is stale in the direction that matters.** `DTWEXBGS`
last prints **08-21 at 118.06 (9.4th percentile — near its year LOW)**, while the 08-28 tape carries
*"Dollar Rallies and Gold Falls on Hawkish Fed Chair Warsh"* and *"Dollar jumps after Warsh comments,
set for weekly gain"* (`brief` head + body, 08-28). ⇒ **the instrument says weak-dollar-near-lows and
the tape says the dollar just rallied.** 🚫 **No dollar-level claim is made in this report**, and
**`P97`'s dollar leg remains unreadable for an 11th run** (`D333`).

⚠ Monthly series (CPI, core CPI, M2, UNRATE) lag ~1–2 months and are **not** used as current-state
evidence. `CPILFESL` sitting at its 365-day maximum is arithmetically trivial for a price **index**
and is not read as a signal.

### A-2 · Credit — the axis the desk is required to cite, and it refuses the stress story harder than yesterday

| | value | 365d %ile | 5-obs change |
|---|---|---|---|
| **`BAMLH0A0HYM2` (HY OAS)** | **2.63%** (08-27) | **0.8th** | **−12bp** |
| `BAMLC0A0CM` (IG OAS) | 0.79% (08-27) | 57.4th | −3bp |
| `NFCI` | **−0.566** (08-21) | **3.8th** | −0.035 |

★ **`M1048`** `[measured]` **HY OAS is at its 365-day LOW (2.63 = 0.8th percentile) and NFCI is at its
loosest of the year (−0.566 = 3.8th percentile), on the same week a Fed Chair told the market rate
hikes may be needed.** Both tightened/loosened *further into risk* over the last five observations.
⇒ **any "credit stress" or "risk-off" claim in this run is labelled narrative-only.** There is none
in the instrument.
⚠ This is the pair `P108` brackets (settle 09-11, A ≤ 2.60 / B ≥ 2.95). Current 2.63 is **3bp above
branch A** — disclosed as a pre-settle read, **not scored** (`D242`).
🚫 Standing caveat carried, not solved (`M783`): the AI-capex credit move sits in **tech IG issuance**,
which neither `HY OAS` nor `IG OAS` reaches. This pair measures the **general** funding environment.

### A-3 · Positioning — `us_flow --cot`, CFTC speculative net, 1-year percentile

⚠ Tuesday-close data, Friday release ⇒ **3–4 day lag. Context, not a trigger** — and specifically
**it does not contain Warsh's Friday speech.**

| instrument | net spec | wk Δ | 1y %ile | read |
|---|---|---|---|---|
| **Copper** (MATR) | +85,266 | +5,518▲ | **100%** | 🟢 **crowded LONG — the board's only one, at the maximum** |
| **Nat Gas** (ENRG) | −197,932 | +5,571▲ | **2%** | 🔴 crowded short |
| **Russell 2000** | −16,118 | −412▼ | **15%** | 🔴 crowded short |
| UST 10Y | −838,975 | +107,986▲ | 22% | 🟡 neutral, covering hard |
| Nasdaq-100 | +11,127 | +23,193▲ | 59% | 🟡 flipped net long on the week |
| S&P500 e-mini | −67,994 | **−57,434▼** | 65% | 🟡 large net-short build |
| USD Index | +18,682 | −397▼ | 74% | 🟡 |
| Gold | +243,334 | +21,145▲ | 66% | 🟡 |
| WTI | +31,099 | +1,935▲ | 43% | 🟡 |
| Silver | +25,261 | +1,636▲ | 41% | 🟡 |

★ **`M1049`** `[measured]` **The two equity books moved in opposite directions in the same week**:
Nasdaq-100 spec flipped to **+11,127 (+23,193 on the week)** while S&P500 e-mini added **−57,434** to
a net short. ⇒ **speculative positioning got longer the concentrated index and shorter the broad one**
in the week before the epicenter printed. Context only; it is not a direction.
⚠ **Copper at the 100th percentile is the single most extreme reading on the board** and it sits under
the Materials sector. Read as **contrarian ammunition, not confirmation** (the tool's own caveat).

### A-4 · The tape, settled 2026-08-28 — ★★ the most informative table in this report

All closes settled; 08-28 from `fast_info.last_price` per §0.9. **Benchmark named inline: `SPY`.**
`SPY` **771.10 → 769.35 = −0.227%** on the day; **765.72 → 769.35 = +0.474%** over five sessions.

| sector | ETF | 1d % | **exc1 vs SPY** | 5d % | **exc5 vs SPY** |
|---|---|---|---|---|---|
| Comm Svcs | `XLC` | +1.418 | **+1.645** | +1.427 | **+0.953** |
| Cons Disc | `XLY` | +1.148 | +1.375 | −0.686 | −1.160 |
| Energy | `XLE` | +0.626 | +0.853 | −1.508 | −1.983 |
| Cons Staples | `XLP` | +0.435 | +0.662 | −0.628 | −1.102 |
| Financials | `XLF` | +0.380 | +0.607 | +1.079 | **+0.605** |
| Materials | `XLB` | −0.094 | +0.133 | −0.672 | −1.146 |
| Health Care | `XLV` | −0.245 | −0.018 | −1.981 | **−2.456** |
| **EW S&P** | `RSP` | −0.343 | **−0.116** | −0.442 | **−0.916** |
| Real Estate | `XLRE` | −0.403 | −0.176 | −1.331 | −1.805 |
| Industrials | `XLI` | −0.928 | −0.701 | −1.725 | −2.199 |
| Utilities | `XLU` | −1.042 | −0.815 | −0.094 | −0.568 |
| **Info Tech** | `XLK` | **−1.548** | **−1.321** | +1.298 | **+0.824** |

★★★ **`M1050`** `[measured]` **On the hawkish-Warsh session, Information Technology was the worst of
eleven sectors (`exc1` −1.321pp) and it is simultaneously the best over five (`exc5` +0.824pp).**
`XLK` is the only sector that owns both extremes. The **8 of 11 sectors that beat `SPY` on 08-28** did
so while the index fell — i.e. **the day was a rotation out of one sector, not a risk-off.**

★★ **`M1051`** `[measured]` **Sector breadth and stock breadth disagreed, and the disagreement is the
finding.** 8 of 11 GICS sectors beat `SPY` on 08-28, yet **`RSP` (equal-weight stocks) still lost to
`SPY` by 0.116pp**, and over five sessions `RSP` **exc5 −0.916pp**. ⇒ **the median stock did not
participate in the sector-level rotation.** Sector-count breadth is not stock breadth, and quoting
either alone misdescribes the tape.

⚠ **`M1052`** `[measured]` **The three duration underweights did not move as one, again.** On a
session that repriced rate expectations hawkishly, `XLU` **−0.815pp** and `XLRE` **−0.176pp** were
negative while `XLP` was **+0.662pp** — a **1.48pp spread** across the "one duration bet" grouping.
This reproduces `S108`'s inverted result (three legs 2.46pp apart on 08-25) for a **second**
observation. 🚫 **UTIL/RE/STPL may not be written as one trade in this run.**

---

## §B · Narrative — events, trajectories, buckets, blind spot

### B-1 · Events, `brief --date 2026-08-28 --body 2 --scope foreign`

**Corrected denominator, quoted as the stage requires**: **4,490 articles → 685 events → 685 market
(0 non-market)**.
⚠ **The "0 non-market" is NOT a measurement.** The tool's own note: the classifier is **Korean-only**,
so on `--scope foreign` it scores nothing — `비시장 경계선 0개 / 전체 0개` and **624 of the
single-source events "have no score at all — not low, unmeasured."** ⇒ **`excluded_nonmarket` is
unavailable to this desk by construction**, and I record that rather than reading 0 as clean.

**Coverage actually achieved, stated as a subtraction, not as `tail = 0`:**

| tier | total | shown | **withheld** |
|---|---|---|---|
| head (≥5 outlets) | 95 | 95 | 0 |
| body (2–4 outlets) | 590 | 30 | **560** |
| tail (2 outlets) | 0 | 0 (sample only) | — |
| single-source | **624** | 15 (random) | **609** |
| non-market boundary | 0 / 0 | — | **unmeasurable (Korean-only classifier)** |
| subevents recovered (`└`) | **224** | — | — |

⇒ **1,169 of the day's body/single-source events were not seen.** 🚫 **No claim of the form "nothing
happened in X" appears below**, and none could be supported from this read.

**What the head layer holds (95 events, all read):**

| event | outlets / articles | note |
|---|---|---|
| **Warsh's Jackson Hole speech** | **21 outlets / 70 articles** | *"Key Takeaways From Fed Chairman Warsh's Jackson Hole Speech"* |
| **Warsh: Fed has "work to do" if above-target inflation persists** | **19 / 76** | subevents: *"signals rate hikes may be needed"* · *"Fed's Hammack Backs Rate Hike"* · *"Dollar Rallies and Gold Falls on Hawkish Fed Chair Warsh"* · *"rejects Fed forward guidance"* |
| Pentagon blacklisting of **Anthropic** ruled unlawful | 21 / 26 | |
| **Iran war at six months; Trump "not in a hurry"** | 16 / 25 | subevent: *"Hormuz deal presses pause on Iran conflict, but fears of…"* |
| **Venezuela weighs OPEC exit; US discusses stake in oil** | 14 / 29 | *"Trump says US has deal with Venezuela for control of 65 bi[llion barrels]"* · *"Chevron said to be in talks to expand in Venezuela"* (7/6) |
| Oil heads for **weekly losses** as Hormuz flows recover | 14 / 22 | |
| US stocks end **lower** as Warsh keeps inflation focus | 11 / 22 | *"U.S. Stocks Fall After Warsh Speech Boosts Bond Yields"* |
| **Qatar extends LNG force majeure** as Hormuz traffic stays halved | 6 / 11 | ⚠ **directly contradicts the "flows recover" head above** |
| **US Job Growth Marked Down 79,000** in preliminary estimate | 5 / 5 | ⚠ a labour revision, at the bottom of the head layer |
| **Advent/Stripe consortium drops pursuit of PayPal** | 7 / 8 | see B-4 — the burst pass ranks this #1 on the day |
| `NVDA` *"Just Did Something It's Never Done Before"* / pulls back a financing program | 5 / 26 | |
| FDA approves `LLY`'s Mounjaro for CV risk reduction | 7 / 16 | Health Care's one head-layer positive |
| Marvell slides 10% on softer [guidance] | inside *"Stock Market News for Aug 28"* (9 / 42) | the `S116` event |

⚠ **Two head-layer items point opposite ways on the same object** — *"Crude heads for weekly losses
as Hormuz fl[ows recover]"* (14 outlets) versus *"**Qatar Extends LNG Force Majeure** as Hormuz
Traffic Remains Ha[lved]"* + *"Hormuz Tanker Traffic Drops Despite Recovery in Oil Flows"* (6
outlets). **Both are carried; neither is resolved here.** This is `P112`'s reason to exist.

### B-2 · Trajectories, `thread --date 2026-08-28 --days 7 --scope foreign`

Daily event counts: 08-22 **288** · 08-23 **323** · 08-24 **792** · 08-25 **832** · 08-26 **831** ·
08-27 **840** · 08-28 **685**. ⚠ **The 08-22/23 weekend denominators are ~2.6× smaller** — any
"acceleration" measured across them is partly a calendar artifact. Stated before any curve is read.
3,483 threads, **596 multi-day, 217 alive**.

| thread | tag | outlet curve | total |
|---|---|---|---|
| **Warsh → Jackson Hole** | **BUILDING**, 6 days | 6→3→5→7→13→**21** | 157 |
| **Fed / above-target inflation** | **BUILDING**, 6 days | 2→6→8→11→6→**19** | 185 |
| **Iran war six months / Hormuz** | **BUILDING**, 6 days | 3→3→4→5→5→**16** | 60 |
| AI-bubble debate | BUILDING, 4 days | 4→6→7→**13** | 44 |
| *"stock market is overvalued / bond sell-off"* | BUILDING, 6 days | 4→5→6→5→4→**6** | 69 |
| Amazon (pricing engine / custom chips) | BUILDING, 7 days | 6→5→8→6→8→4→**9** | 171 |

★ **`M1053`** `[measured]` **The two loudest threads are one object read twice.** *"Warsh at Jackson
Hole"* (21 outlets) and *"Fed has work to do on above-target inflation"* (19 outlets) both peak on
08-28 and both are the same speech. ⇒ **they are not two independent confirmations** (`D343`), and
the combined 40-outlet figure that a naive sum would produce is not used anywhere below.
⚠ **Every proposition in §C names its thread's tag and curve**, per the stage rule. 🚫 No proposition
below calls any thread "quiet" (G1).
⚠ **No ENDED thread sits under an inherited proposition** in this window's top 14.

### B-3 · Seven-bucket sweep — 🚨🚨 and the sweep found a defect in the sweep

Terms passed as **separate argv** (never one quoted string), `--scope foreign --days 3 --syn`.
**Run in BOTH `--mode` settings, because reading the tool's own output line revealed which one it had
been using.**

| bucket | terms (separate argv) | **`--mode and` (the default, and what this desk has always run)** | **`--mode or` (what the L2 spec calls for)** | rank AND → OR |
|---|---|---|---|---|
| AI capex | `data center` `AI capex` `accelerator` | 589 | **2,921** | 1 → **1** |
| **rates** | `Treasury` `yield` `bond market` | 165 | **2,465** | 5 → **2** |
| **oil** | `Hormuz` `OPEC` `crude` `refinery` | **76** | **2,211** | 6 → **3** |
| inflation | `PCE` `inflation` `price index` | 286 | 2,017 | 4 → 4 |
| **Fed** | `Warsh` `Jackson Hole` `FOMC` | 586 | 1,944 | 2 → **5** |
| **trade** | `tariff` `Canada` `trade war` | 324 | 1,782 | 3 → **6** |
| credit | `credit spread` `high yield` `default` | 10 | 459 | 7 → 7 |
| memory *(added 08-28)* | `NAND` `DRAM` `HBM` `memory capacity` | **5** | **272** | 8 → 8 |

🚨🚨 **`M1054`** `[measured]` **`fts search` defaults to `--mode and`, so every seven-bucket sweep this
desk has run has been scoring a CONJUNCTION, not a bucket.** The tool prints its own query and it
reads `MATCH: ("NAND") AND ("DRAM") AND ("HBM") AND ("memory capacity")` — four terms that must
co-occur in one article. `module_news_data/_fts.py:205` is `--mode {and,or}, default="and"`; line 117
joins the groups with `" AND "` unless told otherwise. **The L2 spec for this stage says "OR-mode per
bucket."**
★ **And it is not a rescaling — it reorders the table.** `oil` moves from **6th (76)** to **3rd
(2,211)**, a **29.1× difference**; `rates` from 5th to 2nd; `Fed` **falls** from 2nd to 5th and
`trade` from 3rd to 6th. ⇒ **the bucket ordering that has been feeding the transmission matrix was an
ordering of conjunction rarity, not of attention.** Registered as **`D403`**.
⚠ **This compounds `D396`** (the `--syn` flag, measured 08-28 at up to 49.5×). Two undocumented CLI
settings, each of which reorders the same table. **`M1014`'s 49.5× finding stands; its bucket LEVELS
were conjunctions.**
🚫 **This report uses the `--mode or` column and says so.** The AND column is printed beside it so the
gap is legible, and **no day-over-day bucket comparison is made** — yesterday has no OR column.
🚫 **No bucket is called quiet.** The thinnest under OR is **memory at 272 (3 days)**. Under AND it
read **5**, which is what "the desk's own regime-defining subject looks silent" would have been built
on. **The instrument would have manufactured that silence.**

### B-4 · Blind-spot pass — `burst --date 2026-08-28 --scope foreign` (denominator 4,660; baseline 30 days)

| word | z / articles | outlets | market % | dispersion |
|---|---|---|---|---|
| **`PAYPAL`** | **z 17.6** / 38 | **13** | **100%** | 0.79 |
| **`AFFIRM`** | z 11.0 / 14 | 5 | 43% | 0.79 |
| **`STRIPE`** | z 4.3 / 20 | **11** | **100%** | 0.91 |
| **`ADVENT`** | (new) 19 | **11** | **95%** | 0.92 |
| `ABANDON` / `PURSUIT` | (new) 12 / 7 | 9 / 6 | 92% / 100% | 0.95 / 0.98 |
| `MARVELL` / `MRVL` | z 3.7 / 4.5 | 10 / 4 | 70% / 100% | 0.81 |
| `NVDA` | z 3.6 / 28 | **3** | 100% | **0.28** |
| `COMMITMENTS` | z 6.2 / 6 | 6 | **100%** | **1.00** |
| `LIABILITY` | z 7.0 / 7 | 5 | 71% | 0.96 |
| `XLF` / `KRE` | (new) 4 / 4 | 3 / 3 | 100% | 0.95 |
| `GEFORCE` / `GIGABYTE` / `RESONANT` | (new) 5 each | 2 each | 100% | 0.72 |

**Two body-read rather than classified from the token:**

★★ **`M1055`** `[measured]` **The day's largest burst is a collapsed fintech take-private, and it is
not in any of the eight buckets.** `PAYPAL` z **17.6** across **13 outlets at 100% market relevance**
— the highest z on the board by 60% — with `STRIPE` (11 outlets), `ADVENT` (11), `ABANDON` (9),
`PURSUIT` (6) forming one cluster. Body: *"Advent, Stripe consortium is said to drop pursuit of
PayPal"* and *"PayPal shares sink on reports Advent-Stripe consortium walked away"* (`brief` head,
7 outlets). ⇒ **a large-cap take-private died on the same session as the Fed speech**, and the
seven-bucket table has no term that reaches deal flow. **`KKR` was flagged the same way on 08-27 and
was also left unattached.** ⇒ **term added to the living table: `take-private` · `consortium`**, and
the gap handed to EVENT_ALPHA. 🚫 No freshness score attached (G1).

★★★ **`M1056`** `[measured]` **`COMMITMENTS` (z 6.2, 6 outlets, 100% market, dispersion 1.00) is the
token for the largest memory fact of the week, and the memory bucket at AND-mode returned 5.** Bodies:
*"**Nvidia revenue tops $96 billion as memory commitments soar to $160 billion**"* (`tomshardware`
08-27) · *"Nvidia's **$279 billion** memory commitment reshapes the semiconductor competitive
landscape"* (`investing_en` 08-27) · *"Nvidia's $279 Billion Supply-Chain Gamble"* (`wsj` 08-27) ·
*"Trump Calls Micron One of the World's 'Hottest' Companies a Day After Nvidia Disclosed $279 Billion
in Supplier Commitments"* (`yahoo_finance` 08-28) · *"Nvidia Just Locked In a $279 Billion Bet on
Memory Chips"* (`fool`/`yahoo_finance` 08-29). **Five distinct outlets** (`wsj` `tomshardware`
`investing_en` `yahoo_finance` `fool`).
🚨 **And the memory equities did not take it.** *"**Micron Lags Despite NVIDIA's $279B Memory
Commitment; Western Digital Drops 4%**, SK Hynix Ticks Up"* (`yahoo_finance` 08-27) — which is the
same object `S118` measured numerically: `EW{MU,SNDK,WDC}` **−1.187%** against `NVDA` **+3.763%** over
08-26→08-28 (HANDOVER §2c). **This is `P111`.**

⚠ `GEFORCE`/`GIGABYTE`/`RESONANT` (2 outlets, dispersion 0.72) read as product news; recorded, not
promoted. `XLF`/`KRE` appearing as burst tokens is **ETF-ticker chatter, not a bank event** — flagged
and not built on.

---

## §C · Propositions — falsifiable, both branches, mandatory anti-signal

> **ID 3-grep at write time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**` (excluding this
> run's own files): `P111`–`P114` · `M1046`–`M1058` · `D403`–`D404` → **0 hits**. IDs issued by
> `module_evidence next-id` (highest before this run: `P110` · `M1038` · `D399`), **not hand-grepped**.
> All prices settled, one provider (`yfinance`, `auto_adjust=False`), benchmark named inline (`C1`).

### `P111` — ★★★ The memory equities refused the largest memory commitment ever disclosed (the run's central question)

**Claim to falsify**: *`NVDA`'s **$279bn supplier / $160bn memory** commitment is a **level** fact
that the memory equities are correctly ignoring, because the equity tracks the **second derivative**
of memory pricing — i.e. the standing regime call is right and the non-reaction is its confirmation.*

**Anchors**: `[news]` `M1056`, 5 outlets. `[measured]` `EW{MU,SNDK,WDC}` **−1.187%** vs `NVDA`
**+3.763%**, 08-26 → 08-28 settled (`S118`, `FIRED-C` at −4.950pp, **76% of the way to branch B**).
**Thread**: no dedicated thread; the parent AI-capex thread is **BUILDING 4→6→7→13**.
⚠ The regime call it tests is `[inferred]` and **is not used as evidence** — it is the thing under test.

**Frozen observable**: **`EW{MU, SNDK, WDC}` 10-session excess return vs `SPY`**, settled closes,
**2026-08-28 → 2026-09-14**, `yfinance`, `auto_adjust=False`. Benchmark `SPY`, named inline.

| branch | threshold | meaning |
|---|---|---|
| **A (the commitment is a level fact the tape ignores — regime call SURVIVES)** | `EW{MU,SNDK,WDC}` exc10 **≤ −3.00pp** | a locked-in $160bn buyer commitment produced no re-rate ⇒ the second-derivative framing is doing real work |
| **B (the tape was slow, not indifferent — regime call WEAKENS)** | exc10 **≥ +5.00pp** | the commitment re-rates the producers with a lag ⇒ "level stays tight" is tradeable after all and the deceleration leg is over-weighted |
| **C** | between | **disclosed as the favourite** |

- **`D93` executed BEFORE the bands were written** (§C-annex).
- ⚠ **Anti-signal (VOID)**: **`MU` prints its FQ4 on 2026-09-30** — *outside* the window by design, so
  it cannot void it. What **does** void: a **producer-specific dated announcement** (guidance
  revision, pre-announcement, or M&A) at any of `MU`/`SNDK`/`WDC` inside 08-28 → 09-14.
  ⚠ **Base rate checked and it is not remote** — `SNDK` is up *"3,110%"* by one outlet's count and
  `WDC` *"dropped 13% in a month"*; both are in an active re-rating, which is where corporate actions
  cluster. **Disclosed as live rather than assumed away.**
- **Information content (L3)**: **HIGH on both.** A and B change the standing regime call in opposite
  directions, and that call is the desk's oldest carried `[inferred]` claim.
- ⚠ **Non-redundancy (`D343`)**: `S118` measured a **2-session** window ending 08-28 and is closed.
  This row starts **where `S118` ends** and runs 10 sessions on a **different benchmark** (`SPY`, not
  `NVDA`). It is deliberately not a fifth reading of the 08-26 print.

### `P112` — ★★★ Hormuz: two head-layer items say opposite things about the same strait

**Claim to falsify**: *the oil complex is pricing a Hormuz **reopening** that the shipping data does
not show.*
**Anchors `[news]`, both 08-28, both in the head layer**: *"Oil prices today: Crude heads for weekly
losses as **Hormuz fl[ows recover]**"* [14 outlets] **against** *"**Qatar Extends LNG Force Majeure**
as Hormuz Traffic Remains Ha[lved]"* and *"**Hormuz Tanker Traffic Drops** Despite Recovery in Oil
Flows"* [6 outlets]. `[measured]` Brent `BZ=F` **94.39 (08-21) → 88.10 (08-28) = −6.66%** over five
settled sessions; **89.70 → 88.10 = −1.78%** on 08-28 alone.
**Thread**: Iran/Hormuz **BUILDING**, 3→3→4→5→5→**16**.

| branch | threshold | meaning |
|---|---|---|
| **A (the price is right, the shipping story is a lagging artifact)** | Brent settled close **≤ 84.00** on any settled bar through **2026-09-11** | the war premium is out ⇒ Energy must stand on refining margin alone — **and `P83`/`R89` say the desk has no instrument that separates that margin from the barrel** |
| **B (the shipping story is right, the price is early)** | Brent settled close **≥ 94.50** on any settled bar through **2026-09-11** | force majeure and halved transits reassert ⇒ the 08-26 Iran–Oman deal was a headline, not a transit change |
| **C** | neither touched by 09-11 | the contest stays unresolved; **disclosed as a real possibility, not a residual** |

- ⚠ **This deliberately narrows `P107`'s bands** (≤84.00 / ≥96.00 through 09-08). **`P107` is NOT
  re-frozen and stays ARMED on its own thresholds** (`D242`); this row runs beside it with a tighter
  upper leg and a later date, and **if the two disagree, the disagreement is the finding**
  (the `S14-ANNEX` precedent). Registered as a deliberate near-duplicate, **not** discovered as one.
- ⚠ **Anti-signal (VOID)**: **a Venezuela supply event** — *"Venezuela weighs OPEC exit"* [14 outlets],
  *"Trump says US has deal with Venezuela for control of 65 billion barrels"*, *"Chevron in talks to
  expand in Venezuela"* [7 outlets] — inside the window. **A barrel shock from the western hemisphere
  moves Brent for a reason that has nothing to do with Hormuz.** ⚠ **Base rate checked and NOT
  remote**: this cluster was 14 outlets on 08-28 alone. **Disclosed as live.**
- **Information content**: HIGH on B, MEDIUM on A (A is the direction the price is already travelling).

### `P113` — ★★ Hawkish Warsh: was the IT drawdown a rate event or a rotation?

**Claim to falsify**: *`XLK`'s −1.321pp on 08-28 was a **duration** repricing (a rate event), not a
sector rotation.*
**Anchors `[measured]`**: `M1050` (`XLK` worst of 11 on `exc1`, best of 11 on `exc5`), `M1052` (the
three duration legs **1.48pp apart** on the same session — `XLU` −0.815, `XLRE` −0.176, `XLP` +0.662),
`M1046` (`DFII10` 88.8th %ile vs `T10YIE` 53.6th %ile). `[news]` *"U.S. Stocks Fall After Warsh Speech
Boosts Bond Yields"*, *"Treasury Yields Rise as Warsh Vows to Pull Down Inflation"* [08-28].
**Thread**: Warsh/Jackson Hole **BUILDING** 6→3→5→7→13→**21** — i.e. **at its peak**, which is a
crowding flag, not a freshness flag (G1 bars the freshness reading).

**Frozen observable**: **`XLK` − `XLU` 5-session excess spread vs each other**, settled closes,
**2026-08-28 → 2026-09-08**. (If it is a rate event, the two rate-sensitive legs move **together**;
if it is a rotation, they diverge.)

| branch | threshold | meaning |
|---|---|---|
| **A (rotation, not a rate event)** | \|`XLK` 5d − `XLU` 5d\| **≥ 4.00pp** | the two duration-sensitive legs decouple ⇒ 08-28 was money leaving one sector, and an IT call is a **concentration** call, not a macro call |
| **B (a genuine rate event)** | \|`XLK` 5d − `XLU` 5d\| **≤ 1.00pp** | they move as one ⇒ the drawdown is duration and the `UTIL`/`RE` underweights and any IT view are **the same bet**, which the desk currently books as two |
| **C** | between | disclosed favourite |

- ⚠ **Anti-signal (VOID)**: **Aug NFP prints 2026-09-04, inside this window.** A payroll surprise
  moves both legs for a third reason. ⇒ **if `XLI` (the NFP-sensitive leg, and `S126`'s observable)
  moves ≥3.0pp on 09-04 alone, this row is AMBIGUOUS**, not scored. **Written in at registration.**
- **Information content**: **B is the informative branch and it is the rarer one** — the desk currently
  books IT and UTIL/RE as independent decisions, and B says they are one. **Stated at registration.**
- ⚠ **`M1052` already gives partial evidence against a clean rate reading** (the three duration legs
  did not move together on 08-28). That is disclosed as prior, not smuggled in as the result.

### `P114` — ★★ The labour revision nobody ranked

**Claim to falsify**: *the **−79,000** preliminary payroll markdown is the week's under-priced macro
item, and the market read the Fed speech instead.*
**Anchors `[news]`**: *"US Job Growth Marked Down 79,000 in Preliminary Estimate"* — **5 outlets, at
the very bottom of the head layer**, on a day the speech carried 21. `[measured]` `UNRATE` **4.10 =
8.3rd percentile** of its year, but **~2 months stale** (July). **Thread**: none — **no labour thread
appears in the 7-day top 14**, stated as an absence in the trajectory read, not as quiet (G1).

**Frozen observable**: **`XLI` 5-session excess vs `SPY`**, settled closes, **2026-09-04 → 2026-09-11**
— i.e. the five sessions **after** the August NFP print, not before it.

| branch | threshold | meaning |
|---|---|---|
| **A (the labour channel is live)** | `XLI` exc5 **≤ −2.50pp** | industrial weakness follows the labour data ⇒ the `INDU` underweight is a **cycle** call |
| **B (the labour channel is not the driver)** | `XLI` exc5 **≥ +1.50pp** | ⇒ `INDU`'s weakness is the **tariff** attribution the desk has claimed, or something else |
| **C** | between | disclosed favourite |

- ⚠ **Deliberate non-redundancy with `S126`** (`XLI` exc5 vs `SPY` settling **ON** 09-04): `S126`
  measures the five sessions **into** the print; this measures the five **out of** it. **Same
  instrument, disjoint windows, opposite sides of one event** — registered explicitly so that if both
  fire the same way it is read as one object, not two (`D343`).
- ⚠ **Anti-signal (VOID)**: a **BLS delay or cancellation** of the August report, or **Canada's
  2026-09-08 tariff effective date being moved** — that date falls **inside** this window and is the
  competing explanation the row exists to separate. ⚠ **Base rate: the tariff thread is live**
  (`trade` bucket **1,782** under OR-mode, 6th of 8). Disclosed.
- **Information content**: MEDIUM-HIGH. **B does not confirm the tariff story** — it only removes the
  labour explanation — **and that asymmetry is stated, not glossed.**

### §C-annex · `D93` baselines, executed BEFORE the bands were written

| row | observable | trailing-252 distribution | state at registration | implied branch probabilities |
|---|---|---|---|---|
| `P111` | `EW{MU,SNDK,WDC}` exc10 vs `SPY` | **not computable at this stage without a fresh 252-session pull on three names whose 08-28 close came from a degraded surface (§0.9)** ⇒ **bands set from the observable's own 2-session realised value (−4.95pp over 2 sessions) scaled to 10 sessions under a √t assumption, and that assumption is DISCLOSED, not hidden** | −4.950pp / 2 sessions | ⚠ **A ≈ favourite-adjacent; C disclosed as the modal outcome.** 🚨 **This is a weaker baseline than `D93` requires and it is labelled as such rather than dressed up** — the row is registered with a stated construction deficiency (`C5`), because deferring it would leave the run's central question unbracketed |
| `P112` | Brent touch, ≤84.00 / ≥94.50 | 5-session realised −6.66%; 08-28 alone −1.78% | **88.10** | A needs **−4.65%** more, B needs **+7.26%** ⇒ **A materially likelier than B, and that asymmetry is disclosed rather than corrected by moving a band** |
| `P113` | \|`XLK` 5d − `XLU` 5d\| | realised 5d spread to 08-28: `XLK` +1.298% vs `XLU` −0.094% ⇒ **1.39pp** | **1.39pp** | **the state sits inside C, 0.39pp above branch B** ⇒ **B is the near branch and the informative one; A needs a 2.9× widening.** Stated at registration (B4) |
| `P114` | `XLI` exc5 vs `SPY` | prior run's measured trailing-252: mean +0.012 · sd 1.619 · p05 **−2.500** · p50 −0.087 · p95 +3.121 (`S126`'s annex, same observable) | **−2.199pp** (08-28) = ~7th percentile | **A ≈5% · B ≈35% · C ≈60%.** ⚠ **The state is already near A's region** ⇒ **A is the LOW-information branch and B is the informative one**, stated at registration, not discovered at scoring |

---

## §D · ★ SECTOR TRANSMISSION MATRIX — wind direction only (ROTATION's input)

> **This is not an eleven-sector analysis** — it sets wind direction and names the driving
> proposition. ROTATION owns the ranking and the DEEP picks.
> 🚫 **Two entries carry a G3 restriction**: IT and Health Care **may not be moved on `wflow`**.
> Their lines below are built on **settled ETF excess returns vs `SPY` and `eqflow`**, and say so.
> **RULE C1 — benchmark declared once for this whole table**: every `exc1`/`exc5` figure below is the
> sector ETF's settled excess return **vs `SPY`**, carried from §A-4 where `SPY`'s own moves
> (−0.227% 1d, +0.474% 5d) are printed. No unlabelled excess figure appears in the rows.

| # | GICS sector | direction | driving proposition / evidence | instrument caveat |
|---|---|---|---|---|
| 1 | **Communication Services** | **OW** | The **only** sector positive on both windows: `exc1` **+1.645pp** (best of 11), `exc5` **+0.953pp**. `M1050`/`M1051` | `eqflow` −0.056 vs `wflow` −0.601 — the sweep disagrees with the settled tape; **`D401` says the sweep's bar is intraday, so the tape wins here** |
| 2 | **Financials** | **OW−** | Positive on both windows (`exc1` +0.607, `exc5` **+0.605**) into a **real-rate-driven** long end (`M1046`). `P113` | ⚠ `XLF`/`KRE` appeared as burst tokens (B-4) with **no event attached** — flagged, not built on |
| 3 | **Information Technology** | **N** *(from the inherited lean)* | **`M1050`: worst of 11 on 08-28 (`exc1` −1.321pp) AND best of 11 over 5 (`exc5` +0.824pp).** The sector owns both extremes; a direction taken today is a direction taken on which window you pick. `P113` decides it | 🚫 **G3 flipper (`NVDA`) — not moved on `wflow`.** Ranked here on settled ETF excess + `eqflow` **−0.029** (negative), stated inline. `R108` bars using the non-flipper list as evidence of cleanliness |
| 4 | **Energy** | **N** | `exc1` +0.853 / `exc5` −1.983. `P112` is unresolved **by construction** — two head-layer items contradict each other on Hormuz | 🚨 **`R89` + `P83` (`FIRED-B`): the desk has NO surviving instrument separating refining margin from the barrel.** No separation claim is made. Nat-gas COT at the **2nd percentile** = crowded short |
| 5 | **Health Care** | **N** | Worst `exc5` on the board (**−2.456pp**), against the one head-layer positive (`LLY` Mounjaro CV approval, 7 outlets) | 🚫 **G3 flipper (`LLY`) — not moved on `wflow` (−0.046).** Its **`eqflow` +0.057 is the table's largest positive**; the two instruments point opposite ways and **neither is used to move the sector** |
| 6 | **Consumer Discretionary** | **N** | `exc1` +1.375 (2nd best) but `exc5` −1.160. A one-session reversal inside a negative week | `wflow` −0.424 / `eqflow` −0.377 agree (both negative), so no flipper issue |
| 7 | **Materials** | **UW** | `exc5` −1.146. **Copper speculative net at the 100th percentile of one year** (`M1049`) — the board's only crowded long, at its maximum | ⚠ COT is **3–4 days lagged and predates the speech**. Contrarian ammunition, not a direction |
| 8 | **Consumer Staples** | **UW** | `exc5` −1.102, and its `exc1` **+0.662** is a defensive bid on a hawkish session, not a thesis | 🚫 **`M1052`: may NOT be written as one trade with UTIL/RE** — the three legs were **1.48pp apart** on 08-28 |
| 9 | **Real Estate** | **UW** | `exc5` −1.805 into a **94th-percentile 30-year** (`M1046`) | same `M1052` restriction |
| 10 | **Utilities** | **UW** | `exc5` −0.568 and `exc1` **−0.815** on the hawkish session — the cleanest duration response of the three | same `M1052` restriction; the AI-power leg is a **separate** driver and is not netted against the rate leg here |
| 11 | **Industrials** | **UW−** | Second-worst `exc5` (**−2.199pp**), sitting at ~the 7th percentile of its own trailing 252. **Two dated catalysts inside three weeks**: Aug NFP **09-04** and Canada's tariffs effective **09-08**. `P114` + `S126` | ⚠ The two catalysts are **not separated by any existing row that settles between them** — that gap is exactly why `P114` starts on 09-04 |

**Wind, in one line**: a **real-rate-led** long end at the top of its year, **credit at its year low**,
**VIX at the 4th percentile**, and a session that rotated **out of the one sector carrying the week**
— which makes the live question *"is IT a concentration or a market call"* (`P113`), not *"is the
market risk-on."*

---

## §E · Self-backtest — this desk's own hit rate

### E-1 · The five rows this desk had live, scored or explicitly deferred

| row | status at this run | note |
|---|---|---|
| **`P106`** (RSP exc5 vs SPY, 08-27→09-04) | ⏳ **not due** | 1-session preview: `RSP` −0.343% vs `SPY` −0.227% ⇒ **−0.116pp** of the way. **Explicitly not a score** |
| **`P107`** (Brent touch ≤84.00 / ≥96.00 through 09-08) | ⏳ **ARMED, neither leg touched** | Brent settled **88.10** on 08-28 — **4.10 above A, 7.90 below B.** Checked on every settled bar in the window, as the row's "any settled bar" wording requires |
| **`P108`** (HY OAS at first close covering 09-11) | ⏳ **not due** | HY OAS **2.63** = **3bp above branch A (≤2.60)**. Pre-settle read disclosed, **not scored** |
| **`P109`** (a 2nd ≥$10bn memory-**capacity** commitment, ≥3 outlets, by 09-30) | ⏳ **ARMED — and a candidate was found and REJECTED on the row's own words** | See E-2 |
| **`P110`** (`DGS2` at first `[FRED]` close covering 08-28) | ⏸ **DEFERRED, exactly as pre-declared** | ✅ The row wrote *"if the 08-28 bar has not published at the next run, this row is deferred and named, not expired"* (`D333`). **`DGS2` ends 08-27 at 4.20.** Branch A ≥4.30 / B ≤4.08 ⇒ 4.20 is mid-C. **The pre-declaration worked — this is the second row this week (`S120` the other) whose lag clause converted a discovery into a deferral** |

### E-2 · ★★ The one candidate that could have been scored wrongly, and was not

**`P109` branch A** requires *"a second, separately-sourced **≥$10bn memory-capacity commitment**
(any of DRAM/NAND/HBM, **any producer**) reported by ≥3 outlets."*
**Found**: `NVDA` disclosed **$279bn of supplier commitments, of which ~$160bn is memory**, across
**5 distinct outlets** (`wsj` · `tomshardware` · `investing_en` · `yahoo_finance` · `fool`, 08-27→08-29).
Dollar figure ✅ ≥$10bn. Outlets ✅ ≥3. Different from Kioxia/SanDisk ✅.

🚫 **It does not fire branch A, and the reason is the row's own word: `producer`.** `NVDA` is the
**buyer**. A purchase commitment is a **demand** fact; the row brackets a **capacity/supply** response.
⇒ **`P109` stays ARMED**, the candidate is recorded with its sources so a later run can revisit it on
evidence, and **`D404` is registered**: *a row whose observable names an actor class ("producer") must
say whether the counterparty side counts — because the largest instance will often come from the
other side of the transaction.* **No threshold was improvised** (`D242`).
★ **And the fact is too important to leave inside a rejected anti-signal check** — it is the anchor of
**`P111`**, where it is bracketed on its own terms.

### E-3 · Running hit-rate and the pattern in the misses

Scored rows available to this desk over the last four settle dates (from `SCENARIOS.md`, including
the five recovered this run): `S101` C · `P78` B · `P80` C · `S115` A · `P90` A · `S117` B · `P77` A ·
`S79` A/U-MIXED · `S81` C(ambiguous) · `P83` B · `P96` B · `S119` C · `S116` C · `S118` C.
**14 verdicts: A ×4 · B ×4 · C ×5 · 1 mixed.**

★ **`M1057`** `[measured]` **The desk's "C is the modal outcome" claim survives at 5/14 = 36%, but the
more useful pattern is that the pre-settle read has now pointed the WRONG WAY three times.** `S101`
(pre-settle +1.616 → final −0.744), `P78` (pre-settle **above branch A** → **branch B**), `P96`
(live **−8.584, deep in A** → settled **+4.874, B**). ⇒ **a pre-settle read is not a weak verdict on
this desk's record; it has been an inverted one.** Every deferred row in §E-1 therefore carries its
pre-settle number **with this warning attached**, not alone.

⚠ **`M1058`** `[measured]` **Two of the four B-branch verdicts killed an instrument rather than
confirming a direction** (`P83`: the refining separator collapsed; `P96`: the crack rate flipped
branch between a live and a settled bar). **The desk's scoreboard is currently doing more instrument
testing than direction testing**, which is worth stating because it means the hit-rate above is not a
measure of forecasting skill.

---

## ✅ EXIT CHECK
- [x] Catalysts injected (HANDOVER §10, `catalyst_calendar --days 14` — beyond the 5-day default per `D26`, because `SCENARIOS.md` names 09-08/09-11 dates); narrative (**events + trajectories + 7-bucket + blindspot**) and indicators (FRED primaries + COT positioning) read; **previous run's `MACRO_REPORT.md` read as the continuity anchor** (§E-1 scores its five propositions).
- [x] Events read via `brief --body 2` — **head layer read in full (95/95)**.
- [x] **`tail = 0` is NOT quoted as the coverage claim.** The three recovery tiers are quoted as subtractions: body **560 withheld**, single-source **609 withheld**, non-market **unmeasurable by construction (Korean-only classifier on `--scope foreign`)**, subevents **224 recovered**. Total unseen **1,169**. No "quiet"/"nothing happened" claim appears anywhere.
- [x] **Denominator is the corrected one** — 4,490 articles → 685 events → 685 market — and the reason `비시장 = 0` is **not** evidence of a clean pool is stated.
- [x] Trajectories read (`thread --days 7`): every proposition names its thread's tag + curve, or states the absence explicitly (`P114`: no labour thread in the top 14). Weekend denominator artifact declared before any curve was read. **No ENDED thread sits under an inherited proposition.**
- [x] Every "nothing in bucket X" claim carries its denominator — **there are none**, by design (G1).
- [x] **No bucket's count is trusted from a single CLI setting.** Terms passed as **separate argv**; the sweep was run in **both `--mode` settings** and the default was found to be `and` against an L2 spec of OR ⇒ **`D403`**, table reordered, `oil` 6th→3rd at 29.1×.
- [x] **Both halves of every headline print cited.** `NVDA`: $279bn total **and** $160bn memory. `XLK`: worst 1-day **and** best 5-day. Payrolls: `UNRATE` 4.10 (8.3rd %ile) **and** the −79,000 preliminary markdown. Hormuz: "flows recover" **and** "traffic remains halved".
- [x] **Every relative-performance number names its benchmark inline** (`SPY` throughout §A-4 and §C; `XLU` named as `P113`'s counter-leg). **No statistical result carried across markets** — the `vol_surge` IC cell stays KR-labelled (HANDOVER §5, `W1`).
- [x] **Credit axis read and cited**: `hy_oas` **2.63 (0.8th %ile)** + `nfci` **−0.566 (3.8th %ile)**. There is no credit-stress claim in this report; if there were, it would be labelled narrative-only.
- [x] **`real_10y` quoted with `breakeven_10y`** — 2.34 (88.8th) vs 2.31 (53.6th), and the growth-vs-inflation split is drawn from the pair, not from either alone (`M1046`).
- [x] Transmission matrix produced — **all 11 sectors, one line each**, with the two G3-restricted sectors flagged inline.
- [x] Self-backtest appended with a running hit-rate (14 verdicts, A4/B4/C5/1 mixed) **and the pattern in the misses named** (`M1057`, `M1058`).
- [x] New blind-spot terms folded back into the living table: **`take-private` · `consortium`** (`M1055`); the 08-28 additions `NAND`/`DRAM`/`HBM`/`memory capacity` got their first reading and it exposed `D403`.
- [ ] **Linter** — see ADDENDUM below.

---

## ADDENDUM — linter

`python -X utf8 scripts/report_lint.py llm_outputs/2026-08-29/industry_US/MACRO_REPORT.md`

- **First pass: 1 finding.** `L449 [C1]` — the §D header sentence used the words *"excess return"*
  without a benchmark on the same line. **Fixed, not exempted**: the §D header now declares `SPY`
  once for the whole table and points at §A-4, where `SPY`'s own 1-day and 5-day moves are printed.
- **Second pass: 0 findings.**
- ⚠ **A clean lint is not a correct report.** It checks four forms (C1 benchmark · C2 both halves ·
  S6 future label · D6 OBV-alone). The substantive constraints on this report are the ones the
  linter cannot see: `D401` (no `SECTOR_FLOW_US.json` figure described as settled), `D403` (bucket
  counts are OR-mode and stated as such), `R108` (flipper output may withhold, not clear), and the
  `P111` annex's **declared** `D93` deficiency.


---

## §5 · ADDENDUM — DRIFT WATCH (Stage 11, post-run) · appended 2026-08-29, never clobbered

`python -X utf8 scripts/drift_watch.py --report llm_outputs/2026-08-29/industry_US/MACRO_REPORT.md`

**Result: ✅ no kill-switch burst. No stale-report signal.**
Non-burst activity in the window: `Strait of Hormuz` **5** · `default` **3** · `bankruptcy` 1 ·
`ceasefire` 1 · `invasion` 1 · `rate hike` 1.

### ⚠ The finding that matters here is the window, not the verdict

**`M1089`** `[measured]` **The watch covered 0.7 hours, and the stage specifies +3–6h.**
`MACRO_REPORT.md` completed **22:45 KST** and `drift_watch` ran at **~23:26 KST** — a **0.7h** window
against a **3–6h** design. ⇒ **"no burst" over 0.7h is a much weaker statement than the stage's clean
✅ implies**, and it is written that way rather than as a pass.
- **Why the window is short and not extendable here**: this is an unattended scheduled run that must
  complete in one pass. A 3–6h wait is not available to it, and **US markets are closed** (Saturday),
  so the price side of any drift could not move regardless — but the **news** side could, and that is
  precisely the leg this watch is for.
- ⇒ **The honest carry**: this report is **unwatched from ~23:26 KST 2026-08-29 through the next
  run.** The Sunday-into-Monday window contains the **MSCI quarterly review (2026-08-31)** and the
  run-up to **`AVGO`'s 09-02 print**, and it is uncovered by any drift instrument.
- 🚫 **Right removed**: no downstream stage may cite this ✅ as evidence that the 08-29 report survived
  the weekend. It survived **42 minutes**.

### What the non-burst counts do and do not say

`Strait of Hormuz` at **5** is the largest non-burst count, and this run's `P112` is registered
precisely on that contest (Brent ≤84.00 / ≥94.50 through 09-11, settled 08-28 = **88.10**).
🚫 **The 5 is a count, not a direction** — and G1's removed rights bar any freshness or velocity
reading of it (`vel_coverage` 0.0% this run). **No branch of `P112` is moved by it, and none of the
report's propositions is amended.**

### Anti-signals the tool echoed back for human cross-check (unchanged, none fired)

`P111`'s VOID (`MU` prints **09-30**, deliberately outside its window; producer-specific dated
announcement at `MU`/`SNDK`/`WDC` inside 08-28→09-14) · `P112`'s VOID (**a Venezuela supply event**,
live at 14 outlets on 08-28) · `P113`'s VOID (**Aug NFP 09-04, inside the window**) · `P114`'s VOID
(a BLS delay, or Canada's 09-08 tariff date moving). **None fired inside the 0.7h window** — which,
per the caveat above, is close to no information about any of them.

**Original §C propositions and §D matrix are left standing and unedited** (append-only rule): the
call and its correction stay visible side by side, which is what the self-backtest reads.
