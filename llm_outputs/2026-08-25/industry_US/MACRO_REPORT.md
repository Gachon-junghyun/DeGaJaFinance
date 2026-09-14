# MACRO_REPORT — industry_US · 2026-08-25 (Tue) · Stage 3 / L1·MACRO

> Run clock **KST 22:1x–23:xx = ET 09:1x–xx, TUESDAY, PRE-MARKET** (US cash opens 09:30 ET).
> **Terminal settled equity bar 2026-08-24 (Monday) — ONE new settled session, the first in four runs.**
> All news calls `--scope foreign`. Futures carry a live 08-25 bar and every use of it is labelled **LIVE**.

## ★★★ The one thing this report exists to say today

**The tape moved, and it moved as one trade: an AI-compute de-rate paid for by defensives — and the
split is now at the 97.6th percentile of two years.**

Equal-weight, own price frame, benchmark **`SPY`** named inline, 5 settled sessions to 2026-08-24:
**Information Technology `−4.761` mean / `−6.279` median with 43 of 56 names negative**, against
**Consumer Staples `+5.048` / `+5.243` with only 2 of 19 negative** and **Health Care `+4.295` /
`+4.668` with 3 of 32 negative.** The spread `EW{Staples + Health Care} − EW{IT}` over 5 sessions reads
**+9.336 = the 97.6th percentile of the trailing 252**, against a two-year mean of **−1.064** (`M914`).

Three things make this different from the last four runs' "the numbers did not change":
1. **It is broad, not mega-cap.** IT's mean and median *agree in sign and magnitude*, and the negative
   count is 77% of the sector. This is not `NVDA` dragging an aggregate (`W5` checked, not assumed).
2. **It has no narrative behind it.** `theme-age "AI capex"` reads **⚪ECHO 0.62×** on a **1,176**-article
   base — inside `D340`'s usable band, therefore readable, and **decelerating** (`M915`). The de-rate is
   arriving while its own story is going quiet, which is the opposite configuration to a narrative-led move.
3. **It has erased twenty days in five.** IT `exc20` is **+0.189 ≈ zero** while `exc5` is −4.761.

⇒ **`P79` — the desk's own registered row on exactly this question — sits at `−10.852` at the 08-24
close, inside branch B, and settles at tonight's close, one session before the `NVDA` print by
construction.** The proposition the desk wrote five days ago to separate "positioning flush" from
"de-rate begins" is about to answer itself, and it is currently answering **de-rate**.

---

## §0 · What this report may NOT claim, stated before the numbers

Inherited from `preflight/PREFLIGHT.md` (PASS 3 / FAIL 4) and `HANDOVER.md §0`:

1. **No sweep news-velocity citation and no theme-freshness ranking built on it** — `vel_coverage`
   **0.0% (0/299)** while hand probes answer and discriminate across three orders of magnitude
   (Nvidia 4137 / Nucor 27 / Marathon Petroleum 25 / Nasdaq Inc 6, `--days 7 --scope foreign`).
   **No name or sector is called "quiet" anywhere below.**
   ↳ **Hand-run `theme-age` and `fts search` ARE used** and are declared a *different instrument* from
   the dead sweep axis: each carries its own article base, each was verified live this run, and **none
   is used to rank sectors cross-sectionally.**
2. **No bare concentration number** — every unit count carries its `--days` (250d → 11 units,
   500d → 10, 750d → 10, groupings disagree).
3. **`wflow` is not a current weighting** — `us_top300.csv` is **41 days old**. Where `wflow` and
   `eqflow` disagree, **`eqflow` is the citable one**, and every `wflow` figure below is stamped
   **`[08-21 sweep, 41-day-old caps]`**.
4. **No Consumer Staples promotion/demotion on the weighted-flow bucket** — `WMT` (28.9%) is the run's
   only flipper (1 of 11). §E ranks STPL on `eqflow` and on price excess, and says so inline.
5. **No IC-backed sizing language** — accrual is at **0.49/day = 2.1× slower** than ideal.
6. **Every FRED value below carries its own last-observation date**, and **no two FRED series are
   differenced across different dates** (`D333-KR`, reproduced again this run — §F).
7. **Every futures number from the 2026-08-25 bar is labelled LIVE** and is kept out of the settled
   frame. The settled frame's terminal bar is **2026-08-24**.

---

## §A · Primary indicators — `[FRED]`, with 365-day percentiles and both halves

Pulled via `module_macro_us --series … --days 365 --json`.

### A-1 · The shape: the long end at a one-year HIGH while the dollar sits at a one-year LOW

| Series | Value | Last obs | 365d %ile | 365d range | Prev obs |
|---|---:|---|---:|---|---:|
| effective fed funds | **3.63** | 2026-08-21 | 29.6% | 3.62 – 4.33 | 3.63 |
| **`DGS10`** | **4.74** | 2026-08-21 | **99.6%** | 3.97 – 4.75 | 4.69 |
| **`DGS2`** | **4.24** | 2026-08-21 | **95.6%** | 3.38 – 4.37 | 4.19 |
| **`DFII10`** real 10y | **2.40** | 2026-08-21 | **93.6%** | 1.67 – 2.47 | 2.35 |
| `T10YIE` 10y breakeven | **2.32** | **2026-08-24** | 56.0% | 2.18 – 2.50 | 2.34 |
| **broad dollar index** | **118.06** | 2026-08-21 | **9.2%** | 117.44 – 121.92 | 118.25 |
| `VIXCLS` | 15.13 | 2026-08-21 | 11.3% | 13.47 – 31.05 | 16.01 |

★ **The 10-year yield is at the 99.6th percentile of its own year — effectively a one-year high — and
the broad dollar is at the 9.2nd — effectively a one-year low.** In a growth-led rate move those two go
the *same* way. They are going opposite ways.

★★ **And the move is REAL, not inflation, on the desk's own required pairing (`real_10y` with
`breakeven_10y`):** real 10y **2.40 (93.6th %ile, +5bp on the session)** while the 10-year breakeven
**FELL to 2.32 (56.0th %ile, −2bp)**. Both halves cited: **the entire nominal rise is the real leg.**
⇒ this is a **term-premium / debasement** configuration, not a reflation one. Registered as **`P97`**.

⚠ **Staleness, stated rather than papered over.** Monthly series lag ~1 month and are **not** used as
current reads: core CPI index **336.789 @2026-07-01** (100th %ile of the 12 monthly obs — it is a level
index, so a percentile on it is near-meaningless and is quoted only for completeness), CPI **332.813
@2026-07-01**, unemployment **4.1% @2026-07-01 (down from 4.2%, the 8.3rd %ile = the year's low)**,
M2 **23,155.2 @2026-06-01**. **No proposition below rests on a monthly series.**

### A-2 · Credit and financial conditions — the axis that forbids a stress narrative

| Series | Value | Last obs | 365d %ile |
|---|---:|---|---:|
| **HY OAS** | **2.70** | 2026-08-21 | **9.9%** (365d low 2.63) |
| IG OAS | 0.81 | 2026-08-21 | 77.9% |
| `NFCI` | **−0.559** | 2026-08-14 | **11.8%** |

**Cited as the rule requires**: HY OAS is in its **tightest decile of the year** and `NFCI` is in its
**loosest**. ⇒ **any claim below that this week's equity move is credit-driven or risk-off would be
narrative-only, and none is made.** The IG/HY divergence (77.9th vs 9.9th) persists from `M860` and is
carried unresolved — it is a **composition** puzzle, not a stress signal.

### A-3 · Positioning — `[COT as of 2026-08-18, Tue-close, 3–4 day lag ⇒ CONTEXT, not a trigger]`

| Instrument | Net spec | Weekly Δ | 1yr %ile | Read |
|---|---:|---:|---:|---|
| **Nasdaq-100** | **−12,067** | **+30,838 ▲** | **4%** | **crowded-short — rebound ammunition** |
| Russell 2000 | −15,706 | −1,763 ▼ | 15% | crowded-short |
| **UST 10Y** | −946,961 | −31,908 ▼ | **5%** | crowded-short **while the 10y yield is at its 365d high** |
| UST 2Y | −927,337 | +93,706 ▲ | 70% | neutral |
| **Copper** | +79,748 | −640 ▼ | **100%** | **crowded-long — the standing MATR risk, 3rd run** |
| WTI Crude | +29,164 | +5,938 ▲ | 36% | neutral |
| Nat Gas | −203,503 | −6,368 ▼ | 0% | crowded-short |
| USD Index | +19,079 | −2,330 ▼ | 76% | neutral |
| Gold | +222,189 | +4,249 ▲ | 48% | neutral |

★ **The Nasdaq-100 line is the strongest counter-evidence to this report's headline.** Specs covered
**+30,838** into the drawdown and sit at the **4th percentile short** — i.e. the flush reading of `P79`
still has a live mechanism, and it is named here rather than omitted because it cuts against §0's lead.
🚫 **Contrarian COT is a REJECTED-grade signal (`D6`)** — this is ammunition, not a direction.

🚨 **`D327` reproduces, 4th run**: the S&P 500 row prints **🟢 crowded-long on a net spec of −10,560,
which is net SHORT**, while carrying the board's largest weekly swing (**−21,840**). A reader taking
the label at face value inverts both the level and the change. **The label is not used below.**

### A-4 · Oil, and the separation that matters — settled frame vs LIVE

**Settled (terminal bar 2026-08-24):** Brent **92.17** (−2.35% on the session, **+1.43% over 5**);
3-2-1 crack **66.32 = 93.2nd percentile of 252**. 5-session crack rate, most recent first:
**[−2.86, +2.89, +0.41, +2.36, +5.65]** ⇒ **ONE decline. The registered refiner kill counter stands at
1 of 2** (`M912`).

**LIVE 2026-08-25 futures print, 09:1x ET — NOT settled, NOT in the frame:** Brent **87.88, −4.65% on
the day**; WTI 82.34, −3.14%; 3-2-1 crack **58.11, −8.21 on the session**, which would put the
5-session rate at **−11.70** ⇒ **the second consecutive decline, i.e. the kill fires** (`M913`).

⇒ **This is the crude-and-crack co-fall that `M879` said would separate the war premium from the
capacity story, arriving live.** It is registered as **`P96`** rather than asserted, precisely because
it exists only on an unsettled bar.

★ **And a finding about the desk's own kill condition, measured before it is used**: over the trailing
252 sessions, **two consecutive negative 5-session crack rates occur 35.5% of the time** (`M916`).
⇒ **the registered "second consecutive decline" kill is a weak discriminator with a one-in-three
unconditional base rate.** It is not evidence of a regime break on its own. **New dig `D352`.**

---

## §B · Narrative — events first, then trajectories, then buckets, then the blind spot

### B-1 · Event pass · `brief --scope foreign --body 2` · denominator stated

**Corrected denominator: 2,102 articles → 369 events → 369 market-relevant, 0 excluded as non-market.**
Head (≥5 outlets) **31** · body (2–4) **338** · **tail (2 outlets) = 0**.

🚨 **`tail = 0` is NOT the coverage claim, and this run's uncovered fraction is WORSE than yesterday's.**
- `single_source`: **15 shown of 400** ⇒ **385 unseen = 96.25%** (yesterday 94.6%). The layer is
  **entirely unscored on the US path — the classifier is Korean-only** — so `--singles-nb` has nothing
  to threshold and the tool shows a **random 15**. `D339`, worse (`M917`).
- `excluded_nonmarket`: **0 of 0** shown, band `nb > −3.0`. Nothing withheld here.
- `subevents_recovered`: **61 sub-events** swallowed at the 0.65 threshold.
⇒ **Every coverage-shaped statement in this report is qualified by 385 unseen single-outlet events**,
and no "nothing in bucket X" claim is made anywhere below.

**The day's ranked objects (outlets in brackets):**
1. **[25 art / 16 outlets] US–Canada trade war** — *"Trump's latest Canada trade war threat: renaming
   Lake Ontario"*, with sub-clusters *"Canada set to announce retaliatory tariffs against US"* [4/4],
   *"Trump won't budge on Canada, beef despite Republican pushback"* [4/3], *"Trump's trade war with
   Canada could rattle economies in st…"* [3/3].
2. **[35 / 15] Oil and the Iran sanctions rollout** — *"Oil prices steady as investors weigh impact of
   expanded US s…"*, plus *"Commodities: Oil Shrugs Off Bessent's 'D-Day' Plan For Ira…"* [4/4] and
   *"Conflict-hit oil supply crisis deepens as nearly half of g…"* [2/2].
3. **[34 / 10] Bitcoin crosses $80,000** for the first time since May.
4. **[16 / 10] What the new US sanctions on Iran mean for European business**; **[13/6] Bessent's Iran
   D-Day Threat Hinges on Willingness to Hit Chi[na]**.
5. **[28 / 9] "The S&P 500's Biggest Stocks Keep Getting Bigger"** — a concentration story in the head
   tier on the day the concentration leg lagged **`SPY`** (RULE C1: benchmark named — IT equal-weight
   `exc5` **−4.761 vs `SPY`**, the figure this clause refers to).
6. **`NVDA` occupies four separate head clusters** [14/5], [12/5], [12/5], [7/5] — including
   *"Nvidia stock is on a 7-day losing streak ahead of its big [print]"* and *"Nvidia shares set for
   $280 billion price swing after earnings."*

★★ **The 08-24 session had a NAMED cause and it was not the macro object everyone was watching.**
Body reads, `--scope foreign`, `--days 2`: *"US Equity Indexes Mixed as Investors **Await** Iran
Sanctions **While Chipmakers Push Technology Lower**"* [yahoo_finance 08-24]; *"European shares slip
as **tech drags**; Iran sanctions in focus"* [investing_en]; *"Oil prices drop nearly 1% as U.S.
prepares more Iran sanctions"* [investing_en] (`M918`). ⇒ **the sanctions were an anticipation, the
chips were the move.** This is the corroboration `brief` alone cannot give: `brief` carries no prices.

### B-2 · Trajectories · `thread --days 7 --scope foreign`

**Per-day denominators: 08-19 826 · 08-20 828 · 08-21 771 · 08-22 288 · 08-23 323 · 08-24 765 ·
08-25 369.** ⚠ **08-25's 369 is a PARTIAL DAY** (the run is at 09:1x ET) — not a weekend trough. The
weekend distortion `D328(b)` flagged has **cleared**: 08-24 recovered to 765 = 93% of the weekday median.
**No thread below was selected or excluded by a FADING/ENDED label.**

Threads bearing on propositions:

| Object | Tag | Outlet curve | Read |
|---|---|---|---|
| **Bond market / Treasury buyback** | **BUILDING** 2d | 5→6 | *"Global Bond Markets Stabilize as Investors Mull U.S. Buyback"* — the `P97` axis is **still building**, not fading |
| **US rates / data wait** | **BUILDING** 3d | 4→3→4 | *"Treasury yields steady as traders await more economic data"* |
| **Jackson Hole / Warsh** | **BUILDING** 2d | 3→3 | *"Treasury yields fall as investors brace for Warsh's Jackson [Hole]"* — the `S108` event, 2 days out |
| **Bitcoin $80k** | **BUILDING** 4d | 2→7→7→10 | strongest curve on the board; **no desk position and no bracket** |
| **SpaceX / Oklo power** | **BUILDING** 4d | 7→4→4→7 | private-name object; **the optical/power chain the registry still cannot tag (`D250`, 11th run)** |
| **Micron / memory** | **BUILDING** 3d | 3→3→3 | *"Is It Too Late to Buy Micron Stock After Its 981% Surge?"* — memory narrative alive into `S118`'s window |
| **`US debt tops $40 trillion`** | **ENDED** 08-19→08-24 | 18→19→4→5→6→2, peak **19** | ⚠ **A staleness flag under a LIVE proposition.** `P97` rests on the debasement configuration; its loudest narrative leg has ENDED on outlet count while `theme-age "national debt"` still reads **🟡8.57×**. **The two instruments disagree and the disagreement is recorded, not resolved** |
| **`US treasury doubles debt buyback`** | **ENDED** 08-19→08-20 | 14→2, peak 14 | the *event* thread ended; the *theme* is 🟢FRESH (below). Same object, opposite tags — `D340`'s width law in a third instrument |
| **`U.S. Unveils 'Economic D-Day' Against Iran`** | **FADING** | 2→4→2 | the `S119` object's own thread is fading **while its execution is today's #2 head cluster** |
| **`Walmart shares tumble as sales growth slows`** | **ENDED** 08-19→08-22 | 5→19→3→2, peak 19 | the STPL flipper's own story has ended; **STPL is nonetheless the board's best 5-session sector (§E)** |

### B-3 · Term sweep — read with `D340`'s width band (usable ~60–2,000 articles)

Terms passed as **single quoted phrases**, never as multi-word AND (the silent-zero trap). Each row
carries its base so the ratio can be judged readable.

| Term | Base (90d) | Verdict | 7d avg | Accel | Readable? |
|---|---:|---|---:|---:|---|
| **`Jackson Hole`** | 448 | 🟡ACCELERATING | 53.3 | **23.17×** | ✅ in band — **up from 14.9× on 08-24** |
| **`Iran sanctions`** | 170 | 🟡ACCELERATING | 16.9 | **16.86×** | ✅ in band |
| **`Canada tariff`** | 85 | 🟡ACCELERATING | 8.4 | **10.99×** | ✅ in band — **up from 9.86× on 08-24** |
| **`national debt`** | 299 | 🟡ACCELERATING | 24.9 | 8.57× | ✅ in band — up from 7.82× |
| **`Treasury buyback`** | 239 | **🟢FRESH, age 6** | 34.1 | — | ✅ in band — **the board's only FRESH theme, base grew 201 → 239** |
| **`drug pricing`** | 166 | 🟡ACCELERATING | 7.1 | 2.19× | ✅ in band |
| **`AI capex`** | **1,176** | **⚪ECHO** | 14.9 | **0.62×** | ✅ **in band — and DECELERATING** |
| **`refining margin`** | 265 | ⚪ECHO | 5.7 | 0.81× | ✅ in band — a genuine negative, 2nd run |
| `server prices` | **38** | (🟡 printed) | 3.3 | (8.21×) | 🚫 **BELOW the band — degenerate, ratio NOT read** (`D340`) |
| `Strait of Hormuz` | **8,127** | (⚪ printed) | 106.6 | (0.67×) | 🚫 **ABOVE the band — category label only, ratio NOT read** |
| `data center` | **16,999** | (⚪ printed) | 296.4 | (0.87×) | 🚫 **ABOVE the band — category label only** |

★★ **The single most load-bearing row is `AI capex` ⚪0.62× on a 1,176 base.** It is **inside** the
usable band on both sides, so unlike `data center` and `Strait of Hormuz` its ratio *is* readable — and
it says the AI-capex narrative is **decelerating** while the AI-compute complex takes a 5-session
p05 drawdown. ⇒ **the de-rate is not narrative-led.** (`M915`)

★ **`server prices` is explicitly NOT read this run**, and that is a change from 08-24, which quoted it
at 6.79× on a base of 34. **`D340`'s own band excludes base < ~60.** The 08-24 citation is therefore
**withdrawn as unreadable, not contradicted** — recorded in §F, not edited away.

### B-4 · Blind-spot pass · `burst --scope foreign` · rows read raw

**Denominator 2,102 · 30-day baseline · market-relevance ≥40% · 665-company universe · field = title.**

Words that spiked (z-order): **`RUBIN` z 8.4** (8 articles, 5 outlets, 75% market) · `CRM` z 9.8
(Salesforce, 2 outlets) · `LINUX` 9.4 · `SELECTED` 7.2 · `SMUGGLING` z 5.7 (4/4 — *"Nvidia employee
charged with smuggling advanced chips into China"*) · `REGENERON` 5.6 · `CPUS` 5.0 (3/3, 100% market)
· `AGENTIC` 3.9 · `EMISSIONS` 5.2.
New words (never normally present): **`HBM`** (3 articles, 3 outlets, 67% market, appears 37% of days)
· `PDD` · `DISPOSITION` · `STAGGER`.

★ **The blind-spot pass found the epicenter's product name before the term table did.** `RUBIN` is
`NVDA`'s next-generation platform, and it enters at **z 8.4 across 5 outlets, one day before the
print**, alongside `HBM` and `CPUS` — while the desk's own bucket table has **no term for `Rubin`, no
term for `HBM`, and no term for the AI-server CPU competition** (`M919`). Corroborating body from the
event pass: *"Nvidia faces growth test as **Rubin debut** meets AI financing scr[utiny]"* [4 outlets],
*"Intel pitches **Diamond Rapids** at Hot Chips as server CPU competit[ion]"* [3 outlets], *"Applied
Materials executive says data centers set new AI c[apex]"* [2 outlets].
⇒ **New terms folded into the living table this run: `Rubin` · `HBM` · `Diamond Rapids` · `agentic`.**
⚠ Each is currently **below the readable base band**, so they are registered as *terms to accrue*,
not as ratios to read.

⚠ **`EMISSIONS` and `REGENERON` are single- or double-outlet spikes on 100%-market words with no desk
object attached.** They are logged, not interpreted (P4).

---

## §C · Self-backtest — the exhaustive table, because "nothing was due" and "nobody checked" look alike

**Every registered proposition with a settle date, checked against 2026-08-25:**

| Settle | Rows | Status |
|---|---|---|
| ≤ 2026-08-21 | `P65` `P66` `P69` `P70` `P75` | settled by the 08-22 run |
| 08-22 · 08-23 · 08-24 | none | — |
| **2026-08-25 (TODAY)** | **`P79`** | 🚨 **settles at TONIGHT'S close — cannot be scored by a pre-market run.** Pre-settle reading below. Past-due on arrival for the 08-26 run |
| 2026-08-26 | `P77` `P78` `P80` `P90` | armed (`NVDA` print) |
| 2026-08-27 | `P83` `P91` | armed (Jackson Hole opens) |
| **2026-08-28** | `P67` `P81` `P85`–`P89` `P92` `P93` | armed (July PCE) — **9 rows on one date, `D343`** |
| 2026-09-03 | `P84` | armed |
| 2026-09-05 | `P95` | armed |

⇒ **0 propositions scoreable today, exhaustively verified. 1 (`P79`) is due tonight and is named.
Hit-rate ledger carried unchanged, not recomputed** — recomputing an unchanged ledger under a new
date is manufacturing, not backtesting.

### ⏳ Pre-settle readings — offered as readings, explicitly NOT as scores

**1. `P79` (settles tonight). Frozen observable: `EW{AVGO, ANET, HPE, COHR, LITE}` trailing 5-session
excess vs `SPY`. A ≥ +8.02 (252d p85) · B ≤ −7.72 (252d p05) · C between.**
**Measured at the 2026-08-24 settled close: `−10.852`** — legs `COHR −20.371`, `LITE −13.128`,
`HPE −7.801`, `AVGO −7.389`, `ANET −5.573`. **Inside branch B**, i.e. a **second sub-p05 week**, which
is precisely what branch B was written to detect.
Trajectory across the runs that measured it: **−12.425 (registration 08-20) → −7.178 (08-21) →
−5.609 (08-22) → −10.852 (08-24).**
⚠ **Window discipline, and this stage got it wrong first.** The partial window 08-18→08-24 (4 sessions)
reads **−5.298**; the row freezes a **trailing 5-session** window, which at 08-24 is 08-17→08-24 =
**−10.852**. **Both numbers are written down** (§F carries the near-miss).
⚠ **Branch A retains a live mechanism** and it is stated: `Nasdaq-100` spec is at the **4th percentile
short** with **+30,838 of weekly covering** (§A-3).

**2. `S108` (settles tonight). `EW{XLU, XLRE, XLP}` 3-session excess vs `SPY`, 08-20 close → 08-25
close. A ≥ +1.68 · B ≤ −1.76 · C between (favourite, ≈70%, disclosed at registration).**
**Measured with 2 of 3 sessions elapsed: `+0.484`** — legs **`XLP +2.382`, `XLRE +0.440`,
`XLU −1.371`.** Inside C and **moving away from A** (state at registration was +1.432 = 78.6th %ile).
★ **The dispersion is the more informative number: the three legs span 3.75pp and one is negative.**
Whatever settles tonight, *"the three underweights rip together"* — the row's own premise — **is not
what the tape is doing.**

**3. `P92`/`P93` (settle 08-28, trade war).** `P92`'s anti-signal — a US–Canada agreement with a named
effective date — **has still not fired; the opposite continues** (retaliatory tariffs being announced,
16 outlets today). Mid-window: **Industrials EW `exc5 −1.881`, median −2.321, 30 of 50 negative** —
the second-worst sector, consistent with the transmission channel `P93` names. **Not a score.**

---

## §D · Propositions registered this run — `P96` · `P97` · `P98`

> **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `P96` `P97` `P98`
> → **0 markdown registrations** (`P96`'s single hit is a byte match inside a binary `.png`; `P99`'s
> hits are all *"99th percentile"* prose, so **`P99` is deliberately skipped** to keep the ID space
> unambiguous). Current highest registered proposition: **`P95`**.

### `P96` — ★★★ The refiner kill is one settled session from firing, and the kill itself is weak

**Claim.** The desk's registered refiner kill is *"a second consecutive 5-session crack-rate decline."*
`P80` recorded on 08-20 that the counter had **reset**. On settled bars through **08-24** it stands at
**1 of 2** (rate `−2.862`, the 15.5th percentile of 252). On the **LIVE 08-25 futures print** Brent is
**−4.65%** and the crack **−8.21 in one session**, which would take the 5-session rate to **−11.70** and
**complete the kill**. ⇒ the question is whether the live bar survives to settlement.

| | |
|---|---|
| **Frozen observable** | 3-2-1 crack (`2×RB=F×42 + HO=F×42 − 3×CL=F`, ÷3) **5-session rate, on SETTLED closes**, at the **2026-08-27** close |
| **Branch A (the kill fires and deepens)** | **≤ −2.887** (its own trailing-252 **p15**) — the capacity/margin story is being repriced, not just the war premium |
| **Branch B (the live print was noise)** | **≥ +0.468** (trailing-252 **p50**) — the counter resets a second time, as it did on 08-20 |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of the 5-session crack rate: mean **+0.798** · sd **4.561** · p05 **−5.998** · p15 **−2.887** · p50 **+0.468** · p85 **+5.095** · p95 **+8.928** ⇒ **A ≈15% · B ≈50% · C ≈35%. B is the favourite and is disclosed.** |
| **State at registration** | settled **−2.862 = 15.5th percentile**, i.e. **0.025 above branch A's line** — the narrowest starting state this desk has registered |
| **⚠ Base-rate disclosure on the desk's OWN kill** | **two consecutive negative 5-session rates occur 35.5% of the trailing 252 sessions.** The registered kill is a **one-in-three** event ⇒ **it is a weak discriminator and this row says so before it is used** (`D352`) |
| **Anti-signal (VOID)** | an **OPEC+ emergency production decision** or a **US SPR action** inside 08-25 → 08-27. ⚠ **Base rate checked (`D300-KR`)**: no OPEC+ ministerial is scheduled inside the window; an emergency call in three sessions is not the base case ⇒ **the clause is not near-certain to fire.** ⚠ **The Iran sanctions rollout is deliberately NOT an anti-signal — it is the event**, and voiding on it would be the designed-to-void defect that killed `S91`/`S93` |
| **Information content (`L3`)** | **A and B both change a conclusion.** A validates `L2`'s peak-margin trap on the exact node `M875` proved has no contractual hedge; B retires the kill-counter framing for the second time in six sessions, which would itself be evidence the counter is not a usable instrument |
| **Non-redundancy (`D343`)** | 08-27 carries `S119`, `P83`, `P91`. **`S119` measures the Energy EQUITY leg; `P96` measures the COMMODITY leg.** They can disagree, and the disagreement is the point |
| **Owner** | `industry_US` |

### `P97` — ★★★ Yields at a one-year high with the dollar at a one-year low: debasement, or a two-week artifact?

**Claim.** `DGS10` **4.74 @08-21 = 99.6th percentile of 365d** while the broad dollar index sits at
**118.06 = 9.2nd percentile**. In a growth-led rate move those go the same way. Both halves of the real
decomposition are cited: **real 10y 2.40 (+5bp, 93.6th %ile) with the 10y breakeven FALLING to 2.32
(−2bp, 56.0th %ile)** ⇒ the nominal rise is **entirely real**. The narrative legs corroborate and are
dated: **`Treasury buyback` 🟢FRESH age 6 (base 239, the board's only FRESH theme)** and
**`national debt` 🟡8.57× (base 299)**, both inside `D340`'s readable band. The counter-evidence is
also stated: the **`US debt tops $40 trillion` thread has ENDED** (peak 19 outlets → 2).

| | |
|---|---|
| **Frozen observable** | broad dollar index **and** `DGS10`, `[FRED]`, at the **first observation where BOTH carry the SAME date ≥ 2026-08-28** |
| **Branch A (debasement extends)** | dollar **≤ 117.44** (a new 365-day low) **∧** `DGS10` **≥ 4.75** (a new 365-day high) — both legs make new extremes together |
| **Branch B (it re-couples)** | dollar **≥ 118.60 ∧** `DGS10` **≤ 4.65** — the pair moves back the normal way |
| **Branch C** | between = **the favourite, disclosed** (both A and B require a conjunction) |
| **`D93` baseline** | 365-day ranges, both from this run's own pull: dollar **117.44 – 121.92** (current 9.2nd %ile) · `DGS10` **3.97 – 4.75** (current 99.6th %ile). ⚠ **Branch A asks each leg to exceed its own one-year extreme**, so A is deliberately the rare branch |
| **⚠ Observation-lag clause, written INTO the row** | `D333-KR`, reproduced for a **7th** time this run: `DGS*` end **08-21** while `T10YIE` carries **08-24**. **The row settles on a JOINT date, not on "the first close after 08-28"** — this is the exact defect that left `S102` unsettled for five runs, and it is designed out rather than discovered at scoring |
| **Anti-signal (VOID)** | an **intermeeting Fed policy action**, or an **executed** FX intervention confirmed by MoF/BoJ or the US Treasury in **≥2 outlet bodies**. ⚠ **Base rate disclosed and it is RAISED, not decorative**: `nikkei` 08-21 carries *"US Treasury buybacks put market on alert over more yen interventions."* The clause is narrowed to an **executed, confirmed** intervention precisely so that market chatter about one does not void the row |
| **Information content (`B4`)** | **A falsifies** the desk's four duration-underweight legs a fourth time — and per `S102`'s own regression those four legs have **no measurable rate beta** (`XLU +0.0049 · XLRE −0.0072 · XLP +0.0224 · XLV +0.0185` pp/bp) while **`XLE` has +0.1534**, so the desk's only rate-exposed tilt is its **overweight**, with a positive sign. **B falsifies** the debasement framing this report just built |
| **Non-redundancy (`D343`)** | `S120` (08-28) brackets **`DGS30` + `T10YIE`** — a rates-internal pair. **`P97` brackets a CURRENCY against a rate.** If both fire the same way that is two observations of one regime, and the correlation is named here in advance |
| **Owner** | `industry_US` |

### `P98` — ★★ The defensive-vs-AI split is at the 97.6th percentile of two years. Regime, or a week?

**Claim.** `EW{Consumer Staples + Health Care, n=51} − EW{Information Technology, n=56}`, 5-session
returns, settled to 08-24: **+9.336pp = the 97.6th percentile of the trailing 252**, against a two-year
mean of **−1.064** and sd **4.728**. This is a **self-benchmarking long-short**, so it does not inherit
the single-leg-vs-`SPY` bias `S101` located. Breadth confirms it is not a mega-cap artifact (`W5`):
**43 of 56 IT names negative; 2 of 19 Staples and 3 of 32 Health Care names negative.**

| | |
|---|---|
| **Frozen observable** | `EW{STPL+HLTH} − EW{IT}` **5-session return spread**, `us_top300` constituents, settled closes, at the **2026-09-03** close |
| **Branch A (the split persists through its own catalysts)** | **≥ +3.339** (trailing-252 **p85**) |
| **Branch B (full reversion)** | **≤ −1.347** (trailing-252 **p50**) |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252: mean **−1.064** · sd **4.728** · p05 **−8.026** · p15 **−5.997** · p50 **−1.347** · p85 **+3.339** · p95 **+7.375** ⇒ **A ≈15% · B ≈50% · C ≈35%. B is the favourite and is disclosed** — from a 97.6th-percentile state, reversion is the base case and the row says so |
| **State at registration** | **+9.336 = 97.6th percentile**, above p95 |
| **⚠ Event contamination — OWNED, not voided** | the window **08-27 → 09-03 contains the `NVDA` post-print sessions, Jackson Hole (08-27→29), July PCE (08-28) and the `AVGO` print (09-02)**. **There is no clean 5-session window in the next fortnight**, and making any of them an anti-signal would be the designed-to-void defect (`D300-KR`) that killed `S91` and `S93`. **The row deliberately measures the spread THROUGH the cluster** — the question *is* whether the split survives its own catalysts |
| **Anti-signal (VOID)** | an **intermeeting FOMC action**, or a **GICS reclassification moving ≥3 of the 107 constituents between the two legs** inside the window. ⚠ **Base rate checked**: MSCI's **08-31 quarterly review** falls inside the window but **does not change GICS assignment**, so it is explicitly **not** a voider; a GICS reclassification of that size inside seven sessions is not the base case |
| **Information content (`L3`)** | **A** says the desk's `IT = N` and its defensive underweights are **both** on the wrong side of a live factor rotation. **B** says this week was a flush and `P79`'s branch A reading was right. Neither branch merely confirms |
| **⚠ `W3`** | this measures whether a spread persists, **not** whether any position was right. No sizing (P4) |
| **Non-redundancy (`D343`)** | 09-03 carries `P84`, `S107`, `S110`, `S114`. **All four are single-name or single-pair rows; `P98` is the only cross-sector factor row on that date** |
| **Owner** | `industry_US` |

---

## §E · ★ Sector transmission matrix — all 11 GICS, one line each

> **This is ROTATION's input. It sets wind direction only** — not a ranking, and it does not analyse
> eleven sectors equally. **`exc5`/`exc20` are equal-weight `us_top300` constituent baskets, excess vs
> `SPY` (named inline), computed from this run's own price frame on the 2026-08-24 settled close.**
> `SPY` itself: **−0.294% (1 session) · −1.191% (5) · +3.299% (20).**
> **`flow`/`eqflow` are the 08-21 sweep and are stamped `[08-21, 41-day-old caps]`** — per §0.3 the
> `eqflow` column is the citable one.

| GICS sector | Wind | Driving prop. | exc5 (mean / median) | neg/n | exc20 | eqflow `[08-21]` | One line |
|---|---|---|---:|---:|---:|---:|---|
| **Consumer Staples** | **N+** | **`P98`** | **+5.048 / +5.243** | **2/19** | −3.580 | **+0.048** | 🚫 **`wflow −0.013` is unusable — `WMT` 28.9% owns the sign (G3, 4th run). Ranked here on `eqflow` and on price.** ★ **Board's best 5-session excess, and mean ≈ median with 89% of names positive ⇒ broad, not one name.** ⚠ Its 20-session excess is still **−3.580** — this is one week, not a trend |
| **Health Care** | **OW** | **`P98`** (first driver it has had) | **+4.295 / +4.668** | 3/32 | **+3.318** | **+0.229** | ★ **The only sector positive on BOTH windows with the board's best flow.** The 08-24 run recorded it as *"a coverage gap, not a conviction"* — **`P98` closes the gap**: it is now half of a registered factor row. `theme-age "drug pricing"` 🟡**2.19×** on a 166 base (in band) |
| **Communication Services** | **N** | `P95` | +3.478 / +3.263 | 2/13 | +3.302 | +0.095 | ⚠ **`D297`, 6th run**: `GOOGL` 38.3% **+ `GOOG` 38.3% = 76.6%** of the sector while `top1_w` reports half and `top1_flips_sign` prints **false** — a **demonstrated false negative** (`M877`). **No `wflow` claim is made on this sector at any cut** |
| **Consumer Discretionary** | **N** | `P93` | +3.091 / +2.431 | 4/28 | +1.235 | +0.103 | Mean > median but same sign and 86% positive — **no `W5` split flagged.** `AMZN` is 40.2% of the cap-weighted view, which is why the equal-weight cut is the one used |
| **Financials** | **N** | `P97` | +2.662 / +2.413 | 17/47 | −0.834 | −0.034 | ★ **The mean/median sign disagreement `M`-noted on 08-24 has CLOSED** — both +2.4 to +2.7 now. But **17 of 47 negative** is the board's third-worst breadth, and `eqflow` is still negative. Credit axis says **no stress** (HY OAS 9.9th %ile) |
| **Materials** | **N+** | `P97` · chemicals M&A (`S122`) | +2.621 / +1.949 | 2/12 | +0.625 | +0.046 | ★ **The 08-24 mean/median SIGN disagreement has also closed** (was +1.813 mean vs −0.315 median). 🚨 **Copper COT at the 100th percentile is the standing risk, 3rd run.** `S122` (Shell's $8bn chemicals sale) is armed to 09-30; 🚨 `LYB`/`DOW` remain **outside the universe** (`D341`) |
| **Energy** | **OW** | **`P96`** · `S119` | +1.620 / +2.284 | 4/16 | **+5.062** | +0.102 | ★ **Board's best 20-session excess and the only sector where the median beats the mean** ⇒ the strength is broad-based. 🚨 **But the commodity leg is breaking LIVE**: Brent −4.65%, crack −8.21 on the 08-25 intraday print, which would fire the refiner kill (`P96`). **`exc1` −0.522 is one of only two negative same-session reads** |
| **Real Estate** | **N−** | `P97` | +1.319 / **+2.782** | 3/12 | −4.230 | **−0.446** | ⚠ **Median 2.1× the mean** — the sector is better than its aggregate. Worst-but-one flow, yet **the duration-UW's measured rate beta is −0.0072 pp/bp ≈ zero** ⇒ **the underweight rests on flow, not on rates**, and `P97` therefore does **not** transmit here |
| **Utilities** | **UW−** | `P97` | −1.011 / −1.268 | **13/15** | **−8.401** | **−0.621** | **Board's worst flow, worst 20-session excess, and 87% of names negative.** ⚠ **Yet `exc1` is +1.426, the board's best single-session read** — a one-day bounce inside a broken 20-day trend. **Not called a turn** |
| **Industrials** | **UW−** | ★ **`P93`** | **−1.881 / −2.321** | **30/50** | −4.682 | −0.231 | ★ **The run's live transmission channel, unchanged.** `theme-age "Canada tariff"` **10.99× on an 85 base (in band), up from 9.86×**; retaliatory tariffs are today's **#1 head cluster (25 art / 16 outlets)**; **`P93` settles 08-28, ELEVEN DAYS BEFORE the 09-08 effective date** (`D342`), which is why `S123` exists |
| **Information Technology** | **UW** ⬇ *(from N)* | ★★★ **`P79` · `P98` · `P90`** | **−4.761 / −6.279** | **43/56** | **+0.189** | −0.102 | ★★★ **The board's worst on 5 sessions by 2.9pp, with mean and median AGREEING and 77% of names negative** ⇒ **broad de-rate, not a mega-cap artifact (`W5` checked).** `exc20 +0.189 ≈ zero` — twenty days erased in five. **`AI capex` narrative is ⚪0.62× = decelerating on a readable 1,176 base.** ⚠ **`NVDA` prints 08-26 (D-1); the sector's next two sessions are an earnings event, not a macro read** |

### ★ Matrix-level notes, all measured this run

1. **The wind is one axis, not eleven.** Rank the eleven by `exc5` and the ordering is
   *defensive → cyclical → AI-compute*, monotone. **`P98` brackets the two ends of that ordering as a
   single object** rather than writing eleven separate stories about it.
2. **IT is downgraded N → UW on price breadth, and the downgrade is deliberately NOT taken on flow.**
   `eqflow −0.102` ranks it 8th of 11, not last; the price evidence (43/56 negative, mean ≈ median) is
   what carries it, and per §5 of `HANDOVER` **`rs60` is the ledger's most strongly negative axis, so a
   promotion on relative strength would have been the unsupported direction — a demotion on breadth is
   not the same claim.** ⚠ **This is a one-session-old change on `n=1` new session (`S5`).**
3. **Two sign disagreements CLOSED this run** (Materials, Financials — both had mean and median of
   opposite sign on 08-24). **They closed because the tape moved, not because the cut changed.**
4. **Health Care finally has a driving proposition** after being the board's best sector with none.
5. 🚫 **No sector verdict rests on a `wflow` number**, on a news-velocity number, or on a 🟢/🟡/🔴 tag.

---

## §F · Instrument observations from this stage — dig candidates for `RESEARCH.md` Part C

> **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`: `M911`–`M919`
> and `D352`–`D354` → **0 hit**. Current highest **`M910`** / **`D351`** (both 2026-08-25 `industry_kr`,
> this morning). The US series resumes past both.

### 🚨 What this stage asserted and then refuted, in itself (`D48`)

**This stage drafted `P79`'s pre-settle reading as `−5.298`, "still outside branch B", before
re-opening the row's registration.** The row freezes a **trailing 5-session** window; −5.298 is the
partial 08-18→08-24 window (4 sessions). The correct reading is **−10.852, inside branch B.**
**The draft is not edited away** — both numbers appear in §C. This is `C1`'s own failure mode
(*measure the window yourself, including any baseline you were handed*), and it was caught by opening
the registration rather than by trusting three prior MACRO reports' running commentary.

**And one 08-24 citation is withdrawn as unreadable, not contradicted**: `server prices` **🟡6.79× on a
base of 34** was quoted by the 08-24 run. **`D340`'s own measured band excludes base < ~60.** Today the
base is 38 and the ratio is **not read**. The 08-24 sentence stands; the correction is appended beside it.

### New digs

| # | Finding | Positive-form remedy |
|---|---|---|
| **`D352`** | ⚠ **The desk's registered refiner kill has a 35.5% unconditional base rate.** Measured on the trailing 252 sessions, **two consecutive negative 5-session crack rates occur on 35.5% of days** (`M916`). The condition has been used as a regime marker (`P80` recorded it "resetting" as if a reset were informative) without anyone measuring how often it fires by chance | **Compute and print the unconditional base rate beside every registered kill/trigger condition, the way `D93` already requires a baseline beside a threshold.** A condition that fires one day in three is a weak discriminator and must be labelled one at registration. **Applied immediately: `P96` carries the 35.5% on its own face** |
| **`D353`** | 🚨 **`D315` "self-corrected" and it is not fixed — the calendar moved past it.** On 08-24 `module_flow NVDA --positioning` returned **±1.3% (expiry 08-24, D0)** two days before the print — 4.7× too small with a confident wrong adjective. Today the same call returns **±6.1% (expiry 2026-08-28, D3)**, correct. **Nothing changed in the code; the bad expiry expired** (`M920`). A defect that heals itself when the calendar rolls is a defect that will re-appear on the next same-day expiry, and the desk will have logged a "fix" | **Have `--positioning` refuse to quote an expiry with `D ≤ 1` when a scheduled earnings date sits beyond it, and print `D±n` next to the adjective it chooses.** ⚠ Until then, **every implied-move citation carries its expiry date on the same line** — done throughout this report |
| **`D354`** | ★★ **The blind-spot pass found the epicenter's product name a day before the print, and the term table has no row for it.** `RUBIN` entered at **z 8.4 / 5 outlets / 75% market relevance**, alongside new-word **`HBM`** (3 outlets) and **`CPUS`** (3/3, 100% market), corroborated by bodies on Rubin's debut and Intel's Diamond Rapids server-CPU push (`M919`). The desk's bucket table carries **no product-generation terms at all** — it has macro terms and theme terms, and a chip cycle turns on product names | **Add a PRODUCT-GENERATION slot to the living term table (`Rubin`, `HBM`, `Diamond Rapids`, `agentic` seeded this run) and let `burst`'s new-word section feed it automatically.** ⚠ All four are currently below `D340`'s readable base band ⇒ registered as **terms to accrue**, not ratios to read |

### Reproduced this run without new numbers (counts incremented, no new dig)

- **`D333-KR`** — **7th reproduction**: `DGS*` end **2026-08-21** while `T10YIE` carries **2026-08-24**.
  **Designed into `P97`'s settle clause** rather than logged again.
- **`D339`** — **worse**: single-outlet layer **385 of 400 unseen = 96.25%** (yesterday 94.6%), still a
  random 15 because the classifier is Korean-only.
- **`D327`** — **4th run**: S&P 500 COT prints 🟢 crowded-long on a **net-short** −10,560. Label unused.
- **`D340`** — **paid again, in both directions**: it forced `server prices` (base 38) and
  `Strait of Hormuz` (base 8,127) out of the readable set, and it licensed `AI capex` (base 1,176) —
  the run's most load-bearing narrative reading.
- **`D297`** — **6th run unfixed**, and PREFLIGHT's G3 PASS is only as good as a test that cannot see
  share-class pairs. COMM carries **no `wflow` claim** this run in consequence.
- **`D343`** — **08-28 now carries NINE rows** (`P67` `P81` `P85`–`P89` `P92` `P93`), up from seven.
  Both rows registered today deliberately avoid it (`P96` → 08-27, `P98` → 09-03), each naming its
  non-redundancy.
- **`D250`** — **11th run**: no optical/interconnect row in `cycle_registry.json`, on the day
  `COHR −20.37` and `LITE −13.13` are the board's worst five-session names and the largest single
  contributors to `P79` entering branch B.
- **`D328(b)`** — **cleared this run**: 08-24's denominator recovered to 765 (93% of the weekday
  median). Today's 369 is a **partial day**, not a trough, and is labelled one.
- **`D341`** — unchanged; `S109` remains armed on `FRO`, which this desk cannot flow-tag.

---

## §5 · Post-run ADDENDUM (append-only — DRIFT writes here at stage 11)

*(reserved — nothing appended yet this run)*


### ADDENDUM — appended 2026-08-25 by L1·DRIFT (append-only; nothing above this line was rewritten)

> ⚠⚠ **DRIFT ran at +0.5h**, not the +3–6h the stage specifies — **a 7th consecutive declared
> deviation**. Anything breaking 2–5 hours after this report closed is **outside this run**, and the
> 08-26 run inherits that gap. Stated, not glossed.
> Baseline: report completion **2026-08-25T22:36 KST**. `drift_watch.py --report MACRO_REPORT.md`.

**Two bursts ≥3.0×. Both body-read. One is real and confirms the report; one is a precision failure.**

#### 🚨 Burst 1 — `[default]` **7.9×** (8 articles post-completion): the street named this report's headline the same day, and that is a CROWDING signal, not a confirmation

Bodies read, `--scope foreign`:
- *"Wall Street is **rotating out of 2026's biggest winners**: Chart of the Day"* [`yahoo_finance` 08-24, body]
- *"Stock market sector rotation update: **Industrials join Technology in cooling off**"* [`google_en`/investingLive 08-24] — **this run's two `UW−`/`UW` sectors, named together, by an outside desk**
- *"**Nvidia and Warsh Will Test a Stock Market That's in Mid-Rotation**"* [`bloomberg` 08-24]
- *"Jim Cramer says **the data center trade is under attack**"* [`cnbc` 08-24, body]
- *"**“Give Me Anything But Tech”**: Jim Cramer's Bold Call on the Market's Next Big Rotation"* [`yahoo_finance` 08-25]
- *"JPMorgan stays constructive on stocks, expects a grind higher **with rotation**"* [2 outlets]
- *"Nvidia Makes Waves With Poolside Deal, AI Investments … investment in AI service provider Perplexity. **Nvidia stock fell Monday**"* [`yahoo_finance` 08-24, body]

★★★ **What this changes, and it is NOT a confirmation.** This report's §0 headline — an AI-compute
de-rate paid for by defensives — was **independently named by at least five outlets within hours of
the same close**, including the exact sector pair (`IT` + `INDU`) this run downgraded. ⇒ **the `IT UW`
taken today is a CONSENSUS position as of 2026-08-24/25, not a differentiated one.**
**That cuts against the desk, and it is written on the against side deliberately:**
- The `UW` was taken at **the 5.6th percentile of IT's own two-year breadth distribution** (13 of 56
  positive `exc5`; 252d median 30) — **and now the street is publishing the same call.**
- `Nasdaq-100` spec sits at the **4th percentile short with +30,838 of weekly covering** `[COT 08-18]`.
- **`S124` (settles 08-31) is exactly the row that tests this**, and its `D93` already put branch A
  (breadth repairs to ≥30) at **≈50%** against branch B (**≤13**) at **≈6%**. **The rare branch is the
  one that vindicates the desk, and the crowding evidence just arrived on the other side.**
🚫 **No verdict is moved on this.** A same-day narrative echo of a price move the desk measured itself
is **not a flow number**, and ROTATION barred narrative-only deltas this run. **It is recorded as
crowding context on a one-session-old call.**

#### ⚠ Burst 2 — `[invasion]` **3.8×** (3 articles): **0 of 3 on topic. `D346` reproduces, 2nd consecutive run, SAME term, same cause**

Bodies: *"Denmark bets on Ukraine wind farm with €100 million loan"* · *"Israel Cancer Research Fund
Announces $5.35 Million in New Cancer Research Grants"* · *"How Putin's War Shapes Ukraine 35 Years
After Independence"*. **None concerns an invasion.** The matches are the substring inside
**"invasive"/"non-invasive"** plus a Russia-adjacent item.
⇒ **`D346`'s prescription (whole-word matching, `\binvasion\b`, and a PRECISION-FAILURE stamp on any
burst with a 0% body hit rate) was filed 2026-08-24 and is unimplemented.** The same term fired the
same false positive on the next run. **A kill-switch set that cries wolf is one the desk stops
reading** — that is the failure mode, and its count is now **2**.

#### Anti-signal sweep — every VOID clause registered today, checked against the post-run window

| Row | Anti-signal | Fired? |
|---|---|---|
| `P96` | OPEC+ emergency production decision · US SPR action | **No** |
| `P97` | intermeeting Fed action · an **executed** MoF/BoJ/US Treasury FX intervention (≥2 bodies) | **No** |
| `P98` | intermeeting FOMC action · GICS reclassification moving ≥3 of 107 names | **No** |
| `S124` | GICS reclassification (≥3 IT names) · market-wide halt | **No** |
| `S125` | US–Canada agreement removing agricultural goods · `ADM` corporate action | **No** |
| `S126` | intermeeting FOMC action · BLS delay/cancellation of the August employment report | **No** |
| `P92` | a US–Canada agreement with a named effective date | **No — the opposite continues** |

**Non-burst activity, for the denominator**: `rate hike` 4 · `Strait of Hormuz` 4 · `new tariff` 2 ·
`ceasefire` 2 · `bankruptcy` 2 · `downgrade` 2 · `rate cut` 1 · `blockade` 1 — all below the 3.0× bar.
⚠ **`new tariff` logged 2 on the day the Canada retaliation cluster ran at 25 articles / 16 outlets**
⇒ **`D345` reproduces**: the trade slot's term is too narrow to fire and reads as calm.

**Nothing above this addendum was edited. The original §0 headline stands beside its crowding
correction — that asymmetry is the self-backtest's food.**
