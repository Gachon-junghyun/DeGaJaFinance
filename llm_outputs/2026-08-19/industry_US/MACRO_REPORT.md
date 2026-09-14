# MACRO_REPORT — industry_US · 2026-08-19 (Wed) · Stage 3/11 (L1·MACRO)

## ★★★ The one thing this report exists to say today

**Four sectors' excess returns vs `SPY` all turned positive together, and once beta vs `SPY` is
removed the agreement disappears — two positive, two negative. `S98` settles on the unadjusted sign
tomorrow.**

`S98` (registered 08-17, settles **08-20**) asks whether UW-Utilities + UW-Real-Estate + UW−-Staples
+ Health Care are **four legs of one duration bet**. Its frozen observable is the **sign of the
5-session excess vs `SPY`** for `XLU`/`XLRE`/`XLP`/`XLV`: **A = all four agree · B = they split.**

Measured at the 08-18 settled close, over 08-13 → 08-18 (`SPY` **−1.341%**):

| ETF | raw return | **excess vs SPY** | β (252d) | **β-adjusted excess** |
|---|---|---|---|---|
| `XLU` | −0.045% | **+1.295** | 0.15 | **+0.150** |
| `XLRE` | −1.086% | **+0.255** | 0.27 | **−0.719** |
| `XLP` | −0.488% | **+0.852** | −0.08 | **−0.592** |
| `XLV` | +0.802% | **+2.143** | 0.27 | **+1.158** |

**Raw excess vs `SPY`: four positives inside a 1.9pp spread — branch A.** **β-adjusted: +0.150 / −0.719 / −0.592 /
+1.158 — two up, two down, a 1.88pp spread — branch B.** The four sectors carry betas of 0.15, 0.27,
−0.08 and 0.27; in a **−1.34% `SPY` tape** a low-beta sector outperforms `SPY` **by construction**, whatever the
rate is doing.

⇒ **`S98` is on track to fire branch A on a beta artifact, and branch A's registered consequence is to
retire a four-sector tilt.** The thresholds are **frozen and are not changed here** (that would be the
improvisation the protocol forbids). What is done instead is what §4c requires: **the construction
defect is written down BEFORE the settle, not after it.** The same defect binds `S80`, settling
tonight: its EW{`XLU`,`XLRE`,`XLP`} cumulative excess reads **+0.801 raw** and **−0.387 β-adjusted**.

★ The one sector whose lead survives the adjustment is **Energy**: `XLE` excess **+5.632**, β **−0.28**,
β-adjusted **+3.919**. Energy is the only sector on the board that outperformed because it went **up**
(+4.291% raw) rather than because it fell less.

---

## §0 · Instrument state — read FIRST, because it decides what this stage may do

`PREFLIGHT_US.md` **PASS 3 / FAIL 5**. Binding here:

- 🟢 **G0 PASS (first ever).** The 08-17 phantom bar was backfilled upstream; 08-18 settled.
  **The tape is readable for the first time in six runs and it advanced TWO sessions (08-14 → 08-18).**
- 🚫 **G1 FAIL (7th run).** The sweep's `velocity` field, its 51 survivors, `breadth` as a
  news-independent statistic, and any "went quiet / heating up" claim **from the sweep** are all
  revoked. **Retained and used below: article counts from the CLI path, each with its clock time.**
- 🚫 **G2:** every Δ in this run is **08-14 → 08-18, TWO sessions.** No Δ is called "today's".
- 🚫 **G3:** Financials · Industrials · Materials may not be moved on weighted `wflow`.
- 🚫 **G5:** sector market-cap weights are **35 days stale**; `EA` is not measurable.

⚠ **Three `[FRED]` series returned HTTP 502 on the first pull** (`DGS30`, `CPILFESL`, `NFCI`).
Per the unattended rule they were retried once and **all three returned on the retry** — values below
carry the retry, and the failure is logged rather than hidden.

⚠ **`brief --scope foreign` returned `기사 0건 → 사건 0개` on the first call.** This is `D276-KR`
reproduced on the US desk: the corpus was full (`fts search Nvidia --days 1 --count` = **1033** at
21:5x KST) while `brief` read empty, because the embedding cursor had not been advanced. After
`embed sync` (**5,714 new articles pulled, 5,699 embedded**, cursor → 21:45), the identical call
returned **2,282 articles → 379 events**. **A pipe failure and a quiet day are still indistinguishable
in this tool's output** — the only reason it was caught is that the count was *exactly* zero.

---

## §A · Primaries — `[FRED]`, and the level clause R73 retracted has re-fired on the new sessions

| Series | 08-13 | 08-14 | **08-17** | Δ 08-13→08-17 |
|---|---|---|---|---|
| `DGS2` | 4.15 | 4.17 | **4.19** | **+4 bp** |
| `DGS5` | 4.32 | 4.36 | **4.38** | +6 bp |
| `DGS10` | 4.63 | 4.68 | **4.72** | **+9 bp** |
| `DGS30` | 5.21 | 5.25 | **5.31** | **+10 bp** |
| `DFII10` (real 10y) | 2.39 | 2.41 | **2.44** | **+5 bp** |
| 10y breakeven | 2.24 | 2.27 | 2.28 *(2.30 @08-18)* | +4 bp |
| **30y − 10y** | 0.58 | 0.57 | **0.59** | — |
| **10y − 2y** | 0.48 | 0.51 | **0.53** | — |

Other primaries `[FRED]`: `HY OAS` **2.70** (08-17, 2.71 → 2.67 → 2.70, flat within noise) ·
`IG OAS` **0.81** (08-17, up from 0.78 on 08-05 — **the widest reading of the window**) ·
`NFCI` **−0.559** (08-14, from −0.528 and −0.46 — **easing, and the loosest of the window**) ·
`VIX` **15.19** (08-17, from 18.65 a month ago) · `SOFR` **3.65** vs `EFFR` **3.63** ·
`RRP` **0.155** (08-18) from **1.25** five observations earlier · Fed assets **6,759,955** (08-12,
from 6,657,161 twenty weeks ago) · Broad dollar **118.90** (08-14, from 120.53).

⚠ **Monthly series lag ~1 month and are labelled as such**: `CPI` **332.813 (July)** ·
`CPILFESL` **336.789 (July)** · `M2` **23,155.2 (June)** · `U-3` **4.1% (July)**. None is a
this-week observation and none is used as one.

### ★ A-1 · `R73` was retracted on a window that ended 08-13. The two sessions this desk just gained reverse its refuting half.

`R73` (registered 08-16) withdrew the **level** clause of `P56`/`M653` — *"30y−10y widened with `DGS2`
unchanged"* — because on the window **08-06 → 08-13** `DGS30` **fell** 5.22 → 5.21 and `DGS2` **fell**
10bp. That measurement was correct and is not disputed.

**On 08-13 → 08-17 — data that did not exist when `R73` was written — all four tenors rose, and the
long end rose most: `DGS30` +10bp · `DGS10` +9bp · `DGS5` +6bp · `DGS2` +4bp.** `DGS30` at **5.31** is
now above the 5.22 that opened `R73`'s window, and the news tape independently describes *"Treasury
yields ease from **19-year highs**"* [`nasdaq`, 08-19] — i.e. the long end printed a generational high
inside this window and is coming off it.

⇒ **This is a BEAR steepener, not a bull steepener.** `R73` is **not** re-retracted — its window is
what it is — but **the mechanism it installed (`P65`: a bull steepener is a tailwind for the duration
UWs) is contradicted by the newer window**, and `P65`'s own KPI now half-fails: it required
`30y−10y ≥ 0.58` **and** `DGS2 ≤ 4.15` at the 08-21 settle. **The spread half holds (0.59); the front-end
half has broken (4.19 > 4.15).** Scored in §F.

★ **This is rule `C1` again, and this time it cuts the other way**: `R73` was itself found by
re-measuring a carried window (C1's correct use). Today the *retraction* is the carried claim, and the
new window is what re-measures it. **A retraction has an `asof` too.**

### A-2 · The decomposition, because the direction alone is not the finding

Of `DGS10`'s +9bp over 08-13→08-17, **+5bp is real (`DFII10` 2.39 → 2.44) and +4bp is breakeven**
(2.24 → 2.28). The rise is **majority-real and roughly balanced** — it is neither a pure inflation
repricing nor a pure real-rate shock, and no proposition below claims it is either.

⚠ **`DFII10` 2.44 is the highest reading of the window** and sits 1bp under `P51-A`'s registered
pressure level (2.43). The transmission `P51-A` asserted — high real yields press the duration UWs —
is **testable right now and it failed**: over the same days, `XLU`/`XLRE`/`XLP`/`XLV` all produced
positive raw excess. §Headline shows why that is a beta reading, not a refutation of the mechanism —
**and that "why" is the point: neither the mechanism nor its refutation is measurable on the
unadjusted sign.**

### A-3 · The credit axis, cited because a risk-off claim without it is narrative-only

`HY OAS` **2.70%** — 2.75 → 2.71 → 2.70 → 2.70 → 2.71 → 2.71 → 2.67 → **2.70** across 08-05→08-17.
**Range 8bp over nine observations.** `IG OAS` **0.81%**, a 3bp widening from 0.78, which is the only
credit series that moved at all. `NFCI` **−0.559** and **easing**.
⇒ **There is no credit stress in the primaries.** Any risk-off framing in this report is labelled
**narrative-only** where it appears. `P67`'s AI-capex-credit thesis remains branch-B tracking.

---

## §B · Positioning — CFTC COT, and this time it is NOT a replay

Tuesday-close data, 3–4 day lag ⇒ **context, not a trigger** (the US desk has no investor-type feed;
this and FINRA short pressure are the substitutes).

| Instrument | net spec | wk Δ | %OI | 1y %ile | Read |
|---|---|---|---|---|---|
| S&P500 E-mini | +11,280 | **+38,538** ▲ | 0.5% | **88** | 🟢 crowded long |
| Nasdaq-100 | −42,905 | −7,899 ▼ | −14.2% | **0** | 🔴 crowded short |
| Russell 2000 | −13,943 | −5,044 ▼ | −49.5% | 18 | 🔴 crowded short |
| UST 10Y | −915,053 | +64,190 ▲ | −16.8% | **7** | 🔴 crowded short |
| UST 2Y | −1,021,043 | −16,815 ▼ | −23.3% | 63 | 🟡 neutral |
| USD Index | +21,409 | −1,090 ▼ | 43.2% | **80** | 🟢 crowded long |
| WTI Crude | +23,226 | +193 ▲ | 12.0% | 18 | 🔴 crowded short |
| Nat Gas | −197,135 | +411 ▲ | −11.6% | **2** | 🔴 crowded short |
| Gold | +217,940 | +20,306 ▲ | 54.4% | 49 | 🟡 |
| **Copper** | +80,388 | +3,265 ▲ | 27.1% | **100** | 🟢 crowded long |
| Silver | +23,646 | +1,366 ▲ | 20.5% | 33 | 🟡 |

★ **The one structural read**: **S&P500 spec net flipped positive on a +38,538 weekly swing into the
88th percentile, while Nasdaq-100 sits at the 0th percentile and UST-10Y at the 7th.** Speculators are
long the index, short the tech sub-index, and short duration — three positions that cannot all be
comfortable in the same week. **`Copper` at the 100th percentile** is the single most extreme reading
on the board and it sits under a Materials sector this desk holds at N−.

⚠ Extremes are **contrarian ammunition, not direction** (the desk's own standing caveat). ⚠ These
percentiles are a **1-year** lookback: `C5` — the window is a choice, and a 3-year lookback would put
different names in the extreme buckets.

---

## §C · The tape — settled through 2026-08-18, and it moved

`SPY` **777.88 (08-13) → 776.34 → 772.67 → 767.45 (08-18) = −1.341%** over three sessions.
Sector excess vs `SPY`, same window, with beta from 252 daily returns:

| Sector ETF | raw | excess | β | β-adj excess |
|---|---|---|---|---|
| `XLE` | **+4.291** | **+5.632** | −0.28 | **+3.919** |
| `XLV` | +0.802 | +2.143 | 0.27 | **+1.158** |
| `XLU` | −0.045 | +1.295 | 0.15 | +0.150 |
| `XLF` | −0.721 | +0.620 | 0.61 | +0.100 |
| `XLI` | −1.195 | +0.146 | 0.95 | +0.085 |
| `XLB` | −1.013 | +0.328 | 0.74 | −0.022 |
| `XLP` | −0.488 | +0.852 | −0.08 | **−0.592** |
| `XLY` | −1.764 | −0.424 | 1.18 | −0.188 |
| `XLK` | **−2.700** | **−1.359** | 1.74 | −0.370 |
| `XLRE` | −1.086 | +0.255 | 0.27 | **−0.719** |
| `XLC` | −1.839 | −0.498 | 0.68 | **−0.930** |

★ **Read the two columns against each other and the week has one story, not eleven**: on the raw
excess column **8 of 11 sectors "outperformed"** — an arithmetic impossibility of interpretation in a
−1.34% tape, and a direct measurement of how much of "excess" is just beta. **On the β-adjusted column
only `XLE` and `XLV` clear +1pp, and `XLC`, `XLRE`, `XLP` are the genuine laggards.**

Sweep-level (`SECTOR_FLOW_US.json`, `asof` **2026-08-18**, 3 axes, 299 names): universe `wflow`
**−0.170**, **8 🟢 / 63 🔴**. ⚠ Per `M25`, the 🟢 count is a **`vol_surge` count, not a flow count**.

---

## §D · News — `--scope foreign`, and the coverage is stated before anything is concluded

### D-0 · Coverage accounting, because `tail = 0` is not a coverage claim

`brief --scope foreign --body 2`, run **after** `embed sync`:
**denominator 2,282 articles → 379 events → 379 market · 0 non-market.**

| Section | shown | total | withheld |
|---|---|---|---|
| head (≥5 outlets) | 35 | 35 | 0 |
| body (2–4 outlets) | 31 | **344** | **313** |
| tail (2 outlets) | 0 | 0 | 0 |
| **single-source** | 15 | **435** | **420** |
| excluded non-market (nb > −3.0) | 0 | **0** | 0 |
| subevents recovered (`└`) | — | **60** | — |

🚨 **Two US-specific coverage holes, both structural:**
1. **The non-market band is empty by construction on this desk** — the classifier is Korean-only, so
   `--scope foreign` can never populate `excluded_nonmarket`. **The US desk's coverage claim can never
   rest on that section**, and the KR desk's practice of reading it does not transfer (`W1`).
2. **435 single-source items are UNSCORED, not low-scored** — the tool says so explicitly. 15 were
   sampled at random; **420 were never seen by anything.**

⇒ **No "quiet in bucket X" claim appears anywhere in this report**, because **313 body events + 420
single-source items are unread** and the desk cannot honestly assert absence at that denominator.

★ Even the 15-item random sample paid: **`[seekingalpha] "Valero: Downgrading To Hold, Unsustainable
Crack Spreads…"`** is a single-source item that speaks directly to `P70`, to the book's `MPC`/`PSX`,
and to `VLO`'s rows in **both** ledgers — and it would have been invisible at any outlet-count filter.
So would **`[bloomberg] "Saudis Give Full Oil Allocations to at Least Three Europe…"`**.

### D-1 · Events — the head, with denominators

| Event | articles / outlets |
|---|---|
| **Trump pauses 50% tariffs on Canada, claims trade deal is close** | **23 / 18** |
| Chinese humanoid-robot maker **Unitree** soars in Shanghai IPO debut (+460% → +629%, ~$66bn) | **33 / 17** |
| **Oil edges up on uncertainty over exports through Hormuz** | **23 / 13** |
| US–South Korea scale back joint military drills | 18 / 13 |
| Ukraine's ousted defence minister calls for elections; anti-corruption raids | 15 / 11 |
| **Fed Chair Kevin Warsh testified to Congress** + *"Global bond yields stabilize ahead of Fed minutes"* | 10 / 6 |
| **UAE imposes indefinite trade embargo on Iran** | 10 / 6 |
| Nvidia H200 chips reach China as imports remain limited | 6 / 6 |
| UK inflation rises to **2.9%** | 6 / 6 |
| SK Hynix launches **$28.6bn** buyback and cancellation | 8 / 5 |
| Analog Devices profit/revenue up on surging AI data-centre demand | 6 / 5 |
| Moderna stock doubles on cancer-vaccine results | 5 / 5 |

Body tier, macro-bearing: *"Dollar drifts near multi-month lows as Treasury yields ease"* (17/4) ·
*"US Equity Futures Mostly Flat Pre-Bell as Traders Await Fed Po[licy minutes]"* (5/4) ·
*"Gold edges higher as yields ease, markets await fed minutes"* (5/4) ·
*"Asian stocks tumble as chip rout, bond yields hammer South Korea"* (4/4) ·
*"Stock futures flat as Treasury yields ease from **19-year highs**"* (2/2, a `└` subevent).

### D-2 · 🚨 The catalyst instrument missed a ≤48h binary that the news tape carries in four places

`catalyst_calendar --days 5` returned **exactly one** item — the **undated** Hormuz statement — and
**zero** earnings (*"yfinance unavailable"*). But four separate news items above are keyed to
**FOMC minutes releasing today (2026-08-19)**, and one to **Fed Chair Warsh testifying to Congress**.

⇒ **A dated ≤48h macro binary is live and the desk's own catalyst instrument does not carry it.**
Injected here by hand so PREMORTEM's mandatory both-sides rule fires on it (`P73` below).
This is the same class as `S8`'s undated row and is registered as a dig.

### D-3 · Trajectories (`thread --days 7`, foreign) — 25 BUILDING · 1 FADING · 1 ENDED/REIGNITED

Daily denominators: 08-13 **808** · 08-14 743 · 08-15 282 · 08-16 293 · 08-17 754 · 08-18 797 ·
08-19 **379** (partial day — the US session has not opened). 4,056 daily events → 3,150 threads
(490 multi-day, **144 alive**, 227 new today).

| Thread | Days | Outlet curve | Read |
|---|---|---|---|
| **Canada 50% tariffs → paused** | 5 | 5→6→6→**17→18** | ★ **Peaked today ON the resolution.** A tariff escalation that ran five days and ended in a pause |
| **Unitree / China humanoid robotics** | 3 | 2→5→**17** | ★ **The fastest-accelerating thread on the board**, 2 → 17 outlets in 48h |
| **UAE ↔ Iran** | 2 | 4→6 | ★ Escalating: missiles fired at UAE (08-18) → **indefinite trade embargo** (08-19) |
| **NVDA into 08-26 earnings** | 7 | 5→2→3→3→3→5→5 | Flat-to-rising, **not yet crowded** — 7 days of runway. `S79` owns it |
| Robotics (2nd thread: Serve/Duke/Unitree STAR) | 4 | 5→5→3→5 | Corroborates the Unitree thread from a different cluster |
| SpaceX / space services | 3 | 5→4→5 | steady |

⚠ **The 08-15/08-16 denominators (282, 293) are a weekend**, which mechanically inflates any FADING
read across that boundary — one reason only **one** FADING thread appears and it is not used below.
⚠ Curve shape is not importance (P4).

### D-4 · Bucket sweep — terms passed as **separate argv**, CLI path, clocked 21:5x–22:0x KST

| Term | 7d | 30d | velocity |
|---|---|---|---|
| **utility** | 1,996 | 6,993 | **1.22×** |
| **minutes** (FOMC) | 1,840 | 6,458 | **1.22×** |
| **inflation** | 3,335 | 11,846 | **1.21×** |
| **HBM** | 226 | 820 | **1.18×** |
| yields | 3,824 | 14,490 | 1.13× |
| power | 6,406 | 24,302 | 1.13× |
| Treasury | 1,499 | 5,747 | 1.12× |
| tariff | 1,694 | 6,457 | 1.12× |
| refinery | 323 | 1,234 | 1.12× |
| crack | 587 | 2,289 | 1.10× |
| robotics | 826 | 3,278 | 1.08× |
| FOMC | 296 | 1,189 | 1.07× |
| Fed | 1,624 | 6,641 | 1.05× |
| Hormuz | 1,395 | 5,727 | 1.04× |
| capex | 962 | 4,056 | 1.02× |
| memory | 1,485 | 6,288 | 1.01× |
| semiconductor | 1,615 | 7,010 | 0.99× |
| **Iran** | 2,406 | 11,292 | **0.91×** |
| datacenter | 72 | 365 | 0.85× |

⚠ **These are corpus-wide article counts from the hand-run CLI path with a clock time — the axis
PREFLIGHT retained. They are NOT the sweep's per-name `velocity`, which is revoked**, and they are not
used to call any theme "fresh" or "quiet."
★ The one internally contradictory pair: **`Hormuz` 1.04× while `Iran` 0.91×** — the chokepoint term is
holding while the country term decays. `D279`'s standing constraint applies: **a low reading on a story
that never left is not evidence the risk receded**, and no proposition below reads it as one.

### D-5 · Blind-spot pass — `sample[]` read raw, 3 days

Top token-0 emerging terms are dominated by generic English (`AI` 1183, `Earnings` 970, `Trump` 450,
`China` 351, `Iran` 308) — **the tokenizer is Korean-tuned and English single-word frequency is close to
uninformative here**, which is itself the finding and limits what this pass can do on the US desk.
Two names cleared the noise floor and are worth naming: **`Micron` 165** (the regime call's own subject)
and **`SpaceX` 173**. Random sample of 8 read raw; nothing in it changed a proposition.

---

## §E · Propositions — falsifiable, both directions, mandatory anti-signal

### P73 — ★★★ MANDATORY both-sides bracket on today's ≤48h binary: **FOMC minutes, and whether the front end is what moves**

**Claim.** The FOMC minutes release **today, 2026-08-19**, into a curve that has just bear-steepened
(§A-1) with `DGS2` **4.19** and spec positioning at the **7th percentile short** in UST-10Y and
**neutral (63rd)** in UST-2Y (§B). The interesting question is not the direction but **which tenor
carries it** — `R73`/`P65` bet the front end was pinned; §A-1 shows it is not.

- **Direction A (front-end repricing):** `DGS2` at the first `[FRED]` close covering **2026-08-21**
  is **≥ 4.30** — the minutes read hawkish and the 2y carries it ⇒ **the bear steepener becomes a bear
  flattener, and every duration-UW argument on this desk changes sign again.**
- **Direction B (long-end-only):** `DGS2` **≤ 4.08** while `30y−10y` **≥ 0.59** — the minutes leave the
  front end alone and the term-premium story owns the move ⇒ `P65`'s spread half survives, its
  front-end half stays dead.
- **Between (4.08 – 4.30) = C, no information — and C is the favourite**, disclosed at registration:
  `DGS2`'s realised 9-observation range in §A is **4.15 – 4.25**, entirely inside C.
- **🚨 Mandatory anti-signal:** an **intermeeting Fed communication, a Warsh testimony headline that
  moves ≥3 outlets, or a Treasury refunding announcement** inside the window ⇒ the move is not the
  minutes and this row is **`VOID`**, not scored. (Warsh testified today at 10/6 outlets — **this
  anti-signal is already live and is reachability-checked, not decorative.**)
- **Thread:** `minutes` **1.22×** velocity, four separate body-tier items today; **no `thread` tag** —
  it is a one-day event cluster, and that is stated rather than dressed as a trajectory.

### P74 — ★★★ The duration complex is not measurable on an unadjusted sign, and this says so with a number

**Claim.** `S80` (tonight) and `S98` (08-20) both score the **sign of a raw excess return vs `SPY`**
on low-beta sectors. In a down tape the sign is dominated by beta (§Headline). **The claim is that the
beta correction, not the rate, decides both rows.**

- **Direction A (it is beta):** at the 08-21 settle, `XLU`/`XLRE`/`XLP`/`XLV` raw 5-session excess
  **all four share a sign** *while* the β-adjusted excess **splits (≥1 of each sign)** — reproducing
  today's 4-0 vs 2-2 split a second time ⇒ **`S98`'s observable cannot see the object it names**, and
  the row settles on a fact about `SPY`'s direction rather than about duration.
- **Direction B (it is duration):** raw and β-adjusted **agree on the split** at the 08-21 settle ⇒
  the unadjusted sign test was adequate and this proposition is wrong.
- **Between = C** (one of the four flips sign under adjustment but the majority reading survives).
- **🚨 Mandatory anti-signal:** if `SPY`'s own 5-session return is **within ±0.5%** over the settle
  window, the beta channel is too small to drive the result and this row is **`VOID`** — the effect
  requires a directional tape to exist at all. (`SPY` 08-13→08-18 was **−1.341%**, so the window this
  is registered against does have one.)
- ⚠ **C5**: β is measured on **252 daily returns** and that is a choice; a 60-day β would move `XLP`'s
  −0.08 materially. The window is on the same line as the conclusion.
- ⚠ **S3 power**: n = 4 sectors, one window. **This is a construction claim, not a statistical one.**

### P75 — ★★ The refining leg is being decided by 0.37pp on its own control variable

**Claim.** `P70` (08-17) built a discriminating test: refiners pay **without** the barrel ⇒ capacity
thesis. At the 08-18 close **`EW{MPC,PSX,VLO}` 5-session excess vs `SPY` = +8.886pp** (`MPC` +9.26 ·
`PSX` +8.93 · `VLO` +8.47) — **4.4× branch A's +2.0 bar** — but branch A also requires `BZ=F`'s
5-session return **≤ +2.0%**, and it is **+2.37%**. **The conjunction fails by 0.37pp on the control
leg**, so the row currently reads **C** while its signal leg is in a landslide.

Meanwhile the **physical** driver is unambiguous: the distillate crack (`HO=F`×42 − `CL=F`) went
**88.41 → 101.96 $/bbl over 20 sessions, +13.56**. Brent **91.02**, WTI **84.94**.

- **Direction A (capacity/crack, not crude):** at the **2026-08-21** settle the crack is **≥ 95**
  *and* `EW{MPC,PSX,VLO}` 5-session excess is **≥ +2.0pp** ⇒ the refining leg is a **margin** trade and
  `P70`'s branch A should be read as having been blocked by a threshold that measured the wrong control.
- **Direction B (crude after all):** crack **≤ 88** *and* the EW excess **≤ 0** ⇒ the +8.9pp was the
  barrel and the capacity thesis loses its best week.
- **Between = C.**
- **🚨 Mandatory anti-signal:** an **issuer event** at any of the three (guidance, unplanned outage,
  M&A) or a **PADD3 hurricane landfall** inside the window ⇒ `VOID`. ⚠ Reachability-checked: a
  single-source `[seekingalpha]` downgrade of `VLO` on *"unsustainable crack spreads"* printed **today**
  — that is an analyst opinion, **not** an issuer event, so it does **not** fire the anti-signal, and
  saying so now prevents it being used as an escape hatch later.
- **Thread/velocity:** `refinery` **1.12×**, `crack` **1.10×** (CLI counts, 22:0x KST).

### P76 — ★★ A new BUILDING cycle reached 17 outlets in 48 hours and this desk has no instrument pointed at it

**Claim.** The **Unitree / China humanoid-robotics** thread ran **2 → 5 → 17 outlets in three days**
(33 articles today) on a Shanghai STAR IPO that opened **+460% to +629%** at roughly **$66bn**, with a
second independent robotics thread (Serve/Grubhub, Duke Robotics, Primax Tymphany) BUILDING alongside
it at 5→5→3→5. `robotics` CLI velocity **1.08×**. **The claim is that this is a cycle the desk's
`cycle_registry` does not carry** — the same defect `S94` registered for optical/interconnect.

- **Direction A (real cycle):** by **2026-09-02**, the robotics thread is still alive at **≥5 outlets
  on ≥3 separate days** *and* at least **one `us_top300` name** is publicly named as a supplier or
  competitor in a ≥3-outlet story ⇒ the registry gap is a **discovery** failure, not a taxonomy one.
- **Direction B (IPO-day artifact):** the thread is **ENDED or ≤2 outlets** by 09-02 ⇒ it was a listing
  event, and the desk correctly ignored it.
- **Between = C.**
- **🚨 Mandatory anti-signal:** a **second China A-share tech IPO of comparable size** inside the window
  ⇒ the outlet count is measuring the IPO channel, not the theme, and this row is **`VOID`**.
- ⚠ **This proposition claims no US exposure and names no ticker** (P4). It claims an **instrument gap**.

---

## §F · Self-backtest — the first run in six that can score anything

| ID | Claim | Registered KPI | Settle | Observed @ 08-18/08-17 | Verdict |
|---|---|---|---|---|---|
| **P65** (08-16) | Long end is a **bull** steepener; `DGS2` **not pinned** | `30y−10y` ≥0.58 **AND** `DGS2` ≤4.15 at the 08-21 `[FRED]` settle | 08-21 | `30y−10y` **0.59** ✅ · `DGS2` **4.19** ❌ | ★ **HALF-BROKEN, and on new data.** The conjunction now fails. Not scored (settle is 08-21) but the trajectory **inverted** — §A-1 |
| **P66** (08-16) | Distillate bid has a **physical** driver | `HO=F`−`CL=F` 20d gap at 08-21 + a further dated strike | 08-21 | **crack 88.41 → 101.96, +13.56 $/bbl** | ★ **HIT-tracking, hard.** The physical half is now the largest move on the board. Political off-switch: **not** triggered (UAE embargo is escalation, not a halt) |
| **P67** (08-16) | AI capex bill migrating to debt; credit does not see it | `HY OAS` ≥2.85% at first close covering 08-28 | 08-28 | `HY OAS` **2.70%**, 8bp range over 9 obs | **CARRIED, branch B tracking.** Still **narrative-only** |
| **P61** (08-15) | Fed-hike premium detached from oil; driver is **demand** | `DGS2` at 08-21 vs 4.05 / 4.30 | 08-21 | `DGS2` **4.19** | **C (mid-band).** ⚠ But `DGS2` rose 4bp **while crude rose 2.37%** — the two moved **together** this window, which is the coupling `R70` said had separated. Flagged, not scored |
| **P69** (08-17) | Does a Hormuz shutdown reprice crude at all? | `BZ=F` at 08-21: A ≥93.00 · B ≤86.50 | 08-21 | **`BZ=F` 91.02**, +2.37% over 5 sessions | **C, as pre-registered as the favourite.** ⚠ Moving **toward A** (was 87.07–88.98 at registration) |
| **P70** (08-17) | Refiners pay **without** the barrel ⇒ capacity thesis | `EW{MPC,PSX,VLO}` exc5 ≥+2.0 **while** `BZ=F` 5d ≤+2.0% | 08-21 | EW **+8.886** ✅ · `BZ=F` **+2.37%** ❌ (by **0.37pp**) | ★ **C — blocked by its own control leg by 0.37pp.** `P75` registers the replacement discriminator |
| **P52** (08-13) | In-line print sent money to growth, not defensives | `XLK` exc5 ≤0 **∧** `XLU` exc5 >0 ⇒ A refuted | **08-19 (tonight)** | `XLK` exc5 **+0.151** ❌ · `XLU` exc5 **+1.297** ✅ | **A NOT refuted** — the refuting conjunction fails on the `XLK` leg. Settles tonight |
| **P53** (08-13) | Materials' broad leg lasted two sessions | ex-`NEM` EW exc5 **positive** ⇒ A wrong | **08-19 (tonight)** (`S77`) | **−3.231**, 10 of 11 names negative | ★ **A is NOT wrong — supported, and now on fresh closes.** Was −2.097 on the frozen tape |
| **P68** (08-16) | Two instruments cannot distinguish "no change" from "no observation" | next non-session run reproduces the 3-way identity | — | ★ **Cannot recur this run: the tape advanced 2 sessions, 298/299 scores moved, `[FRED]` gained 4 observations** | **RETIRED by circumstance**, not by refutation. Recorded so it is not silently dropped |

**Running hit-rate this run: 0 HIT · 2 HALF (P65 broken-half, P70 blocked-half) · 0 MISS ·
4 CARRIED · 1 RETIRED · 2 settling tonight.**

★ **And the honest headline on this table: for five runs it read "UNSCOREABLE — the window did not
advance." Today six of nine rows moved against real data, and the two that moved most (`P65`, `P70`)
both moved AGAINST the proposition that registered them.** A scoreboard that only advances when the
desk is right is not a scoreboard.

---

## §G · ★ SECTOR TRANSMISSION MATRIX — wind direction only, all 11 GICS

⚠ **Unlike the last four runs, this matrix is NOT a re-print** — the tape advanced two sessions, the
curve moved, and COT swung 38.5k contracts. Every cell below is re-derived. Δ is vs **08-17**.

| # | GICS sector | Wind | Driving proposition | Δ vs 08-17 |
|---|---|---|---|---|
| 1 | **Energy** | **OW** | `P66` (crack **+13.56 $/bbl**, the board's largest physical move) + `P75`. **The only sector whose lead survives β-adjustment (+3.919)** | ★ **strengthened — mechanism now physical, not premium** |
| 2 | **Industrials** | **OW−** | `M704`/`M719` defense-vs-`XLI`; `S97` (`LHX` succession, exc5 **−1.862**). β-adj excess **+0.085** = flat | — direction held, no new driver |
| 3 | **Information Technology** | **N+ → N (watch)** | **`XLK` is the week's worst raw sector (−2.700) and its β 1.74 explains most of it** (β-adj −0.370). `S85`/`S96` settle 08-21. **`HBM` 1.18× is the only semis-adjacent term above 1.1×** | ★ **changed — the drawdown is mostly beta, so the sector is weaker in price than in evidence** |
| 4 | **Health Care** | **N** | `S76` settles tonight: leg 1 `XLV` exc5 **+1.427** (mid-band), **leg 2 = 17 of 32** (mid-band). **β-adj +1.158 — the 2nd-best sector on the board** | ★ **changed — first genuinely positive β-adjusted read** |
| 5 | **Financials** | **N−** | `S78` settles tonight: median RS20 {JPM,BAC,WFC,BRK-B} **+1.256**, mid-band. β-adj **+0.100** = flat. `R69` stands | — held |
| 6 | **Materials** | **N−** | `S77` settles tonight at **−3.231, 10 of 11 negative** ⇒ heading to its **first NEM-free confirmation**. ⚠ **`Copper` COT 100th %ile** cuts the other way | ★ **strengthened, with one contrary instrument named** |
| 7 | **Consumer Discretionary** | **N−** | `S93` (08-21). β-adj **−0.188**. `XLY` β **1.18** — its underperformance is beta, not evidence | — held |
| 8 | **Communication Services** | **UW** | **β-adj −0.930, the board's worst** — the only sector that is worse after adjustment than before | ★ **strengthened on a new axis** |
| 9 | **Consumer Staples** | **UW−** | β-adj **−0.592** (raw excess was **+0.852** — the sign flips). `S80`/`S98` legs | ★ **strengthened; the raw print was misleading** |
| 10 | **Utilities** | **UW** | β-adj **+0.150** ≈ flat; `utility` CLI velocity **1.22× = the board's highest**. §A-1 turns the rate leg back into a **headwind** (bear steepener), reversing `P65`'s tailwind | ★ **changed — rate mechanism re-inverted, contradiction now resolved AGAINST the tailwind reading** |
| 11 | **Real Estate** | **UW** | **β-adj −0.719** (raw excess **+0.255** — sign flips). `S90` (08-21) | ★ **strengthened; the raw print was misleading** |

🚫 **ROTATION binding, carried from PREFLIGHT**: **Financials · Industrials · Materials** may **not**
be promoted or demoted on weighted `wflow` (G3 flippers: `BRK-B` 13.9% · `CAT` 8.7% · `LIN` 24.7%).
**No sector may be moved on a `breadth` change** (news-contaminated, G1). Sector weights are **35 days
stale** (G5). **`EA` is not measurable** and Communication Services' composition inherits that.
★ **New binding this run: no sector may be promoted or demoted on a RAW excess return alone.** §C shows
8 of 11 "outperformed" in a −1.34% week; three sectors change sign under β-adjustment (`XLP`, `XLRE`,
`XLB`). ROTATION must quote both columns or neither.

---

## §H · §4c — claims this stage asserted and then refuted, in this run

1. **This stage's own first `brief` call returned "0 articles" and that was nearly written as a quiet
   day.** It was a stale embedding cursor. The corrected read is **2,282 articles / 379 events.**
   The earlier reading is left here rather than edited away.
2. **The `S98` headline was initially framed as "all four duration legs agree, so the tilt is one
   bet."** The β decomposition run immediately afterward **split them 2-2**. The first framing is
   wrong and is recorded as wrong.
3. **`P70` was carried into this stage as "tracking branch A" on the strength of +8.9pp.** Checking the
   control leg showed the conjunction **fails** by 0.37pp. The optimistic read did not survive its own
   next command.

## §I · Failed lookups this run

| Lookup | Failure | Resolution |
|---|---|---|
| `[FRED]` `DGS30`, `CPILFESL`, `NFCI` | HTTP **502 Bad Gateway** on first pull | **Retried once — all three returned.** Values above are from the retry |
| `brief --scope foreign` | returned 0 articles / 0 events | `embed sync` (5,714 pulled), re-run returned 2,282 / 379 |
| `catalyst_calendar` earnings block | *"yfinance unavailable"* — 0 earnings in a 5-day window | **Not resolved.** FOMC minutes injected by hand (`D-2`); the earnings gap is logged |
| news bridge (G1) | 0/40 · 0/5 at 21:53–21:54 (TLS handshake dropped) | recovered by 21:55; all citations carry clock times |

## ✅ EXIT CHECK
- [x] Catalysts injected — **including one the instrument missed** (FOMC minutes, §D-2), bracketed
      both ways by `P73`.
- [x] Events read via `--body 2` with tail = 0, **and `tail = 0` explicitly rejected as a coverage
      claim** — 313 body + 420 single-source items named as withheld (§D-0).
- [x] Corrected denominator quoted: **2,282 articles → 379 events**, after `embed sync`.
- [x] Trajectories read (`thread --days 7`); every proposition carries a thread tag/curve or states
      "no thread" (`P73` does).
- [x] **No "nothing happened in bucket X" claim appears** — the denominator does not support one.
- [x] Bucket terms passed as **separate argv** (19 terms, §D-4), never as a quoted multi-word string.
- [x] Monthly prints labelled with their lag; no half-quoted headline used as an anchor.
- [x] **Every relative-performance number names `SPY` inline**, and β-adjusted figures carry their
      252-day window.
- [x] **Credit axis cited**: `HY OAS` 2.70 · `IG OAS` 0.81 · `NFCI` −0.559. No risk-off claim is made
      without them; where narrative outran credit it is labelled **narrative-only**.
- [x] Self-backtest scored (§F) with the running tally, including two rows that moved **against** the
      desk.
- [x] Transmission matrix covers all 11 GICS with driving proposition IDs and ROTATION bindings.


---

# 🚨 DRIFT ADDENDUM — appended 2026-08-20 KST 00:2x (Stage 11/11 · L1·DRIFT) · APPEND-ONLY

> ⚠ **Naming deviation, logged**: the protocol says *"append a §5 ADDENDUM."* This report is lettered
> **§0 · §A–§I**, with no §5, so the addendum is appended here as a terminal block rather than invented
> as a section number that does not exist. **Nothing above this line was edited** — the original call
> stays visible next to its correction, which is what the self-backtest eats.

**Baseline**: report completed **2026-08-19T22:21 KST**; `drift_watch.py` ran **+1.6h** later.

## 1 · The one burst, and it was body-read rather than counted

| term set | post-completion count | vs normal | verdict |
|---|---|---|---|
| **`bankruptcy`** | **5** | **4.7×** | 🚨 flagged ⇒ body-read below |
| `rate hike` 7 · `invasion` 5 · `downgrade` 5 · `default` 4 · `rate cut` 2 · `circuit breaker` 1 · `strikes on Iran` 1 · `new tariff` 1 | — | below 3.0× | no flag |

**Body-read, `fts search bankruptcy --days 1 --scope foreign` — 39 matches, decomposed:**

| what it actually is | items | reaches this desk's frame? |
|---|---|---|
| **Foreign idiosyncratic filings** — Casas Bahia (Brazil), Braskem Idesa (Mexico, Ch. 11, a *consensual* restructuring cutting debt **> $920M**) | 3 | ❌ no US sector in this report |
| **The Spirit Airlines estate data sale to Google ($10M)** — one story carried by 4 outlets | 4 | ❌ a bankruptcy-**court asset sale**, not a new distress event |
| **Legacy estates** — FTX hearing, Knaken, PCH | 3 | ❌ 2022–2025 vintage |
| **Structuring vocabulary, not distress** — Ethena's *"`bankruptcy`-remote SPV"* with FalconX | 1 | ❌ the word is a legal structure |
| **Risk-factor boilerplate** — e.g. Realty Income's dividend PR listing *"bankruptcies"* among standard risks | several | ❌ template language |
| **Genuine new US corporate distress** — *Freight Distress Report: >7,000 jobs cut*, incl. a boating supplier in Ch. 11 | **1** | ⚠ **freight / consumer-marine — not ENRG, INDU, MATR, COMM or STPL** |

⇒ **The burst is real as a word count and is not a credit-regime event.** One of ~39 items is a new US
distress datapoint, and it lands outside every sector this run took a view on.

## 2 · The credit instruments, because this desk's own rule requires them

**Rule (carry): any proposition about credit stress, risk-off or financial conditions cites `HY OAS` or
`NFCI`, or is labelled narrative-only.** Re-pulled `[FRED]` at 00:2x KST:

| series | latest | 365-day range | 90 days ago | read |
|---|---|---|---|---|
| **`HY OAS`** | **2.75** (2026-08-18) | **2.63 – 3.46** | 2.86 | **12bp off the 365-day LOW; 11bp TIGHTER over 90 days** |
| `IG OAS` | 0.82 (08-18) | 0.73 – 0.94 | 0.81 | mid-range, unchanged over 90 days |
| `NFCI` | **−0.559** (08-14) | **−0.571 – −0.460** | −0.527 | **within 1.2bp of the loosest reading of the year** |

⇒ **The daily credit market flatly refuses the burst.** This is the same shape as the measured
2026-07-21 failure, where the desk assembled a "credit surprise stack" from narrative while `HY OAS`
sat 6bp off its low — **and the instrument that closed that gap is doing its job here.**

## 3 · What changes in the report above — **nothing, and that is the finding**

- **No proposition is amended.** No §E row keyed on credit, and none of the anti-signals listed by
  `drift_watch` (Fed intermeeting / Warsh headline / `SPY` ±0.5% / issuer events / a second China
  A-share tech IPO) fired in the window.
- **No sector verdict moves.** The single genuine distress item is in freight; **Transport was already
  named as the INDU node with 0 of 9 accumulating** (`SECTOR_DEEP_INDU §1d`), and `DAL`/`UAL` were
  filed to `missed_ledger` at the BET stage with node-conditional entry conditions. ⇒ the drift item
  **corroborates a position the run already took**, which is not a reason to move anything.
- ⚠ **Recorded for the next run, not acted on**: if `bankruptcy` stays ≥3× for a **second** consecutive
  post-run window **while `HY OAS` widens ≥15bp from 2.75**, that is the pair that would matter. Neither
  leg is true tonight. **One leg alone is a word count.**

## 4 · Honest limits of this check

- The window is **1.6h**, not the protocol's 3–6h — the run finished late and DRIFT ran immediately
  after ALPHA rather than after a gap. **A 1.6h window sees less than a 6h one**; the 🚨 that fired did
  so inside it, but an absence in the other eight term sets is a **shorter-window absence** and is not
  claimed as a clean overnight all-clear.
- **PREFLIGHT G1 is still FAILED for the sweep axis.** These counts come from `drift_watch`'s own
  direct queries, which answered (39 matches on the body-read probe), and are reported as **counts with
  their clock**, never as a freshness verdict.
- `NFCI` is **weekly and 5 days stale** (08-14); `HY OAS` and `IG OAS` are daily through **08-18**.
  None of the three covers today's session — **the credit read is one settled session behind the burst
  it is being used to test**, and that is stated rather than hidden.
