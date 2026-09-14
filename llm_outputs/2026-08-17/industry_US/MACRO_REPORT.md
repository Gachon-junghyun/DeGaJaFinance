# MACRO_REPORT — industry_US · 2026-08-17 (Mon) · Stage 3/11 (L1·MACRO)

> Runtime `--market us`. All news calls `--scope foreign`. FRED values cited `[FRED]`.
> No sizing, no buy/sell language (P4).

## ★★★ The one thing this report exists to say today

**Three of this desk's four macro instruments returned values byte-identical to yesterday's. The fourth
— the news corpus — carried a dated, D-0 binary that none of the desk's instruments could see.**

Today, **2026-08-17**, the **60-day US–Iran ceasefire / Memorandum of Understanding EXPIRED**, with
Strait-of-Hormuz tanker traffic reported at or near **zero**. Corroborated across **five independent
outlets** on the day (`yahoo_finance` *"US Equity Futures Mixed Pre-Bell as 60-Day US-Iran Ceasefire
Expires"* · `aljazeera` *"US-Iran Memorandum of Understanding expires: How and why it fell apart"*,
9,981-char body · `bloomberg` *"Trump Issues Threat to Oman as US-Iran MOU Expires"* · `cnbc` *"Strait
of Hormuz shipping grinds to a halt ahead of U.S.-Iran ceasefire expiry"* · `oilprice` *"Hormuz Tanker
Traffic Slows to a Trickle"*), and pre-announced by `aljazeera` on 08-16 (*"US-Iran MoU is set to
expire: What to know"*, 7,592 chars).

**`CATALYST_WATCH.json`, pulled at 22:1x KST today, does not contain it.** The calendar returned exactly
two binaries: `NVDA` earnings (**08-26, D-9**) and the *undated* Hormuz statement that `S8` has carried
un-scoreable for **fifteen runs**. ⇒ **The desk went into a D-0 binary with no bracket, and the reason is
not that the news was quiet — it is that every instrument the desk owns is vocabulary-locked or
calendar-locked.** Measured below in §D-0. **PREMORTEM's mandatory both-sides bracket now fires.**

★ **And the second half is the part a one-way tilt would miss: the tape has not repriced any of it.**
Brent settled **88.91 (08-11) → 88.52 (08-14)** and prints **88.84** on a live 08-17 bar; WTI
**83.20 → 82.40 → 82.54**. Over the four *settled* sessions in which Hormuz attacks mounted and traffic
collapsed, **crude fell**. A report that led with the escalation and stopped there would be describing a
headline, not a market.

---

## §0 · Instrument state — read FIRST, because it decides what this stage may do

`llm_outputs/2026-08-17/preflight/PREFLIGHT_US.md` — **PASS 3 / FAIL 5.** Binding on this stage:

| 🚫 This stage may not | ✅ This stage may |
|---|---|
| cite the sweep's news-velocity axis or its **51 survivors** | cite **`[FRED]`** — but see §A, it has no new observation |
| call anything "today's change" on a price-derived number | cite **settled prices through 08-14** with fine-grain RS |
| read an **empty** `theme_age`/`burst` result as "cooled" or "quiet" | cite **per-name / per-term news probes I ran myself**, with the counts and the probe clock time on the same line |
| cite a **`breadth` change** between runs as a market change (news-contaminated, PREFLIGHT §G1(d)) | cite **`eqflow`** — protected by the axis-drop guard |
| describe this run as reflecting **Monday 08-17 trading** | cite `news_vectors.db` through **08-16** |

⚠ **Run clock 22:10–22:5x KST = 09:10–09:5x ET.** The sweep finished **20 minutes before the bell**.
Where this report quotes an **08-17** price it is a **live intraday bar pulled at 22:30:33 KST**, is
labelled as such, and is **never** compared to the sweep frame.

---

## §A · Primaries — `[FRED]`, and the finding is that there is no finding

`module_macro_us --series … --days 120 --json`, live pull 22:1x KST. **14 series.**

### ★ A-1 · Measured: `[FRED]` is byte-identical to the 08-16 pull. Zero new observations, zero revisions.

A key-by-key diff of today's pull against yesterday's `_macro_fred.json`: **new dates = 0 and revised
values = 0 in all fourteen series.** There is no cache in `module_macro_us` (no cache path in the
module; the fetch log shows live per-series observation counts), so this is a **live-pull identity**,
not a stale file.

⇒ **This matters because both the 08-16 HANDOVER and today's said `[FRED]` was "the one instrument that
could have moved."** It did not. The 08-16 run got `R73` out of a **re-measurement** of an existing
window; today there is neither new data nor an unexamined window left in this block. **The news corpus
is the only axis carrying information into this run** — and §D shows it carried a great deal.

| Series | Last obs | Value | Prior obs | Both halves / note |
|---|---|---|---|---|
| `DGS30 − DGS10` *(from the same block)* | 2026-08-13 | — | — | see `P65`; unchanged since 08-16 |
| `us_10y` (`DGS10`) | **2026-08-13** | **4.63%** | 08-12 4.68% | −5bp d/d |
| `us_2y` (`DGS2`) | **2026-08-13** | **4.15%** | 08-12 4.20% | −5bp d/d — the `P65` front-end leg |
| `real_10y` (`DFII10`) | 2026-08-13 | **2.39%** | 08-12 2.42% | ⚠ quoted **with** breakeven below (C2) |
| `breakeven_10y` (`T10YIE`) | **2026-08-14** | **2.27%** | 08-13 2.24% | +3bp. ⇒ the 08-13 10y fall is **real-yield-led**, not an inflation-expectation move |
| `fed_funds` (`DFF`) | 2026-08-13 | **3.63%** | 08-12 3.63% | flat |
| `vix` | 2026-08-13 | **14.63** | 08-12 14.55 | ⚠ **C3 — no measured cause** for a VIX this low into a D-0 geopolitical binary |
| `hy_oas` | 2026-08-13 | **2.71%** | 08-12 2.71% | flat, **6 sessions** |
| `ig_oas` | 2026-08-13 | **0.79%** | 08-12 0.79% | flat |
| `nfci` | 2026-08-07 | **−0.549** | 07-31 −0.546 | marginally looser |
| `dxy` | **2026-08-07** | 119.06 | 08-06 119.51 | ⚠ **10 days stale** — see §D-3, the news says the dollar fell to an early-June low on 08-17 and this series cannot see it |
| `cpi` / `core_cpi` | **2026-07-01** | 332.813 / 336.789 | 06-01 332.568 / 336.065 | monthly, ~1-month lag. Core MoM **+0.215%**, headline MoM **+0.074%** — ⚠ **both halves**: the *sequential* gap between core and headline is 14bp, the largest of the last three prints |
| `unemployment` | 2026-07-01 | **4.1%** | 06-01 4.2% | monthly; fell 0.1pp |
| `m2` | 2026-06-01 | 23,155.2 | 05-01 23,055.6 | monthly, ~2-month lag |

**A-2 · The tension the whole board sits inside, restated on unchanged numbers.**
Financial conditions are at their loosest of the year (`NFCI` 7.1st %ile · `HY OAS` 2.71% ≈ 10th %ile ·
`VIX` 14.63) while the long end sits near its highest and the 10y move decomposes **real, not
inflationary** (real 2.39% with breakeven only 2.27%). ⚠ **This is the same observation the 08-16 run
made and it is not re-counted as confirmation** (PREFLIGHT G2) — it is one reading, quoted twice.

---

## §B · Positioning — CFTC COT. **A REPLAY for the third run, and labelled as one.**

`scripts/us_flow.py --cot` · Tue **2026-08-11** close, released 08-14 · **identical to the 08-15 and
08-16 runs, instrument by instrument.** Context, never a trigger (D6).

| Instrument | Net spec | Weekly Δ | 1y %ile | Read |
|---|---|---|---|---|
| **S&P 500 (E-mini)** | +11,280 | +38,538 ▲ | **88th** | 🟢 crowded long |
| **Nasdaq-100** | −42,905 | −7,899 ▼ | **0th** | 🔴 crowded SHORT |
| Russell 2000 | −13,943 | −5,044 ▼ | 18th | 🔴 crowded short |
| **UST 10Y** | −915,053 | +64,190 ▲ | **7th** | 🔴 crowded short |
| UST 2Y | −1,021,043 | −16,815 ▼ | 63rd | 🟡 neutral |
| USD Index | +21,409 | −1,090 ▼ | 80th | 🟢 crowded long |
| **WTI Crude** | **+23,226** | +193 ▲ | **18th** | 🔴 **crowded short** |
| Nat Gas | −197,135 | +411 ▲ | 2nd | 🔴 crowded short |
| Gold | +217,940 | +20,306 ▲ | 49th | 🟡 neutral |
| **Copper** | +80,388 | +3,265 ▲ | **100th** | 🟢 crowded long |
| Silver | +23,646 | +1,366 ▲ | 33rd | 🟡 neutral |

🚫 **This table may not be cited as "positioning held" or "confirmed for a third run."** It is the same
Friday release read three times. The 88-percentile-point spread inside equities is **one** observation
dated 08-11.

★ **The `WTI` row is now the most information-bearing cell on the board, and it cuts both ways.**
Spec positioning is at the **18th percentile short**, snapshotted **2026-08-11**. In the six days since,
Hormuz went from "attacks mounting" to **traffic near zero** and the **MoU expired** (§D-1) — the entire
escalation is **outside** the snapshot.
⚠ **And the obvious inference is already refuted by price.** Crowded-short-into-an-escalation has had
four settled sessions to hurt and has not: Brent **88.91 → 88.52** and WTI **83.20 → 82.40** across
08-11 → 08-14. **The asymmetry is real; the payoff is not observed.** Both halves go into `P69`.
⚠ **USD Index 80th %ile crowded long** against §D-3's *"Dollar falls to lowest since early June"* — the
same frozen-snapshot-vs-live-tape shape, on a second instrument.

---

## §C · The tape — settled through 2026-08-14. Frozen for a **fourth** run.

`SPY` **776.34** (08-14), −0.20% from 08-13's 777.88. Median last-bar volume **0.649×** the trailing
20-day average, after 08-13's 0.732× — two consecutive sub-0.75 sessions. August monthly opex is
**08-21**, so this is not an expiry artifact.
Universe: **n=299 · `wflow` −0.132 · 9 🟢 / 60 🔴** — identical to the 08-16 run, and **all 299
`flow_score` values are identical name-by-name.**
⚠ **G3 flippers (3 of 11), binding on ROTATION**: Information Technology (`NVDA`, 19.4%) · Industrials
(`CAT`, 8.7%) · Materials (`LIN`, 24.7%) — `wflow` inadmissible for promotion or demotion.
⚠ Every cap weight above is computed from a **33-day-old** market-cap file.
⚠ **New this run**: two sector `breadth` values moved (`Financials` 0.04→0.06, `Communication Services`
0.08→0.00) **with zero price change**, because `tag` consumes raw velocity outside the axis-drop guard
(PREFLIGHT §G1(d) · `D261` · `M701` · `D263-KR`). **`breadth` deltas are not market information.**

**Live intraday context, pulled 22:30:33 KST = 09:30:33 ET, quoted separately and never mixed with the
frame above:** Brent `BZ=F` **88.84** · WTI `CL=F` **82.54** · `XLE` **62.12** · `XOP` **181.10** ·
`SPY` **776.65**. These are opening prints on a live bar. **[measured, intraday, incomplete]**

---

## §D · News — the only axis that moved, `--scope foreign`

`embed sync` at 22:0x KST pulled **+3,843 articles** (15 dropped for missing publish time); cursor
advanced `2026-08-17T09:23` → **`2026-08-17T22:05`**. Corpus **435,998** articles / vectors.

**Denominator (corrected).** `brief --scope foreign --body 2`: **1,965 articles → 347 events → 347
market / 0 non-market.**
**The three recovery sections, quoted rather than waved through** (the EXIT CHECK's own requirement):
- 꼬리 (2 outlets): **0 shown / 0 total** — genuinely empty this run, not truncated.
- 1-outlet tier: **15 shown / 384 total** ⇒ **369 single-source items were NOT shown.** ⚠ And the tool
  states why they cannot be ranked: the classifier is **Korean-only**, so all 384 are **unscored — not
  low-scored**. This is where FX and rates primaries live, and this desk cannot see 96% of that tier.
- 비시장 경계선 (nb > −3.0): **0 / 0** — the boundary band is empty because everything classified market.
- Sub-events recovered (`└`): **41** swallowed by a larger event at the 0.65 threshold.
⇒ **Any "quiet in bucket X" claim in this report would be unsupportable, and none is made.**

### ★ D-0 · The instrument finding: the day's biggest event is invisible to every term instrument

`theme-age --scope foreign`, **13 terms, all probed 22:30:56–22:31:20 KST, all answered (13/13)**:

| Term | Verdict | Accel | Term | Verdict | Accel |
|---|---|---|---|---|---|
| **`optical`** | ⚪ECHO | **1.74×** ← highest | `refining` | ⚪ECHO | 1.31× |
| `rate hike` | ⚪ECHO | 1.43× | `blockade` | ⚪ECHO | 1.28× |
| `inflation` | ⚪ECHO | 1.36× | `Hormuz` | ⚪ECHO | **1.17×** |
| `MoU` | ⚪ECHO | 1.34× | `Strait` | ⚪ECHO | 1.13× |
| `Nvidia` | ⚪ECHO | 1.30× | `memory` | ⚪ECHO | 1.01× |
| | | | `Oman` | ⚪ECHO | **0.96×** |
| | | | `tanker` | ⚪ECHO | **0.68×** |
| | | | **`ceasefire`** | ⚪ECHO | **0.81×** |

★★ **On the day a 60-day ceasefire expired, the term `ceasefire` reads 0.81× and `tanker` reads 0.68×.**
Five vocabulary variants were probed precisely to test the KR desk's 08-17 D-trigger (*a fixed-term
velocity probe returns the opposite of the truth when the story changes vocabulary*) — and **all five
fail together**: Hormuz 1.17, MoU 1.34, Strait 1.13, Oman 0.96, blockade 1.28. **None reaches the 2×
accel gate.** This replicates `F1`/`M709` (the 🟢FRESH gate is arithmetically unreachable — 13 of 13
ECHO today after 8 of 8 yesterday) and **extends it**: the gate is not merely unreachable, it is
unreachable *on the day's largest event*.

★★★ **And `burst` — which uses no fixed vocabulary at all — does not surface a single Iran / Hormuz /
oil / ceasefire token.** Its top-z words are `LG` 9.5 · `QUARTERS` 9.3 · `HARRIS` 7.7 · **`HBM` 7.2** ·
`CATALYSTS` 7.1 · `LICENSING` 6.8 · **`OPTOELECTRONICS` 5.7** · **`GPU` 5.2**; its new-word list is
`HIVE` · `EMCOR` · `DRUCKENMILLER` · `DUQUESNE` · **`KUBASIK`** (0% baseline). ⇒ **This is stronger than
the KR finding**, because vocabulary-locking cannot explain a vocabulary-free instrument's silence. The
mechanism is the **title-only field** (`field=title` in burst's own header) plus a 30-day baseline in
which "Iran" has been continuously present for weeks — **a story that never left cannot burst.**
🚫 **Consequence, stated as a binding: no stage may use a low `theme_age` or an absent `burst` token as
evidence that a risk has receded.** Registered as `D279`.

### D-1 · Middle East — the D-0 binary, and the price that refuses to confirm it

**Instrument answered**: `fts search "Hormuz" --days 2 --scope foreign` at **22:28:53 KST** → **283
matches**. Dated items, by outlet:

| Date | Outlet | Item |
|---|---|---|
| **08-17** | `yahoo_finance` | **"US Equity Futures Mixed Pre-Bell as 60-Day US-Iran Ceasefire Expires"** |
| **08-17** | `aljazeera` | **"US-Iran Memorandum of Understanding expires: How and why it fell apart"** (9,981-char body) |
| **08-17** | `bloomberg` | **"Trump Issues Threat to Oman as US-Iran MOU Expires"** |
| **08-17** | `cnbc` | **"Strait of Hormuz shipping grinds to a halt ahead of U.S.-Iran ceasefire expiry"** |
| **08-17** | `oilprice` | "Hormuz Tanker Traffic Slows to a Trickle" |
| **08-17** | `toi` | "Oil prices hold steady as Hormuz nears zero traffic while Iran-US talks on Strait opening stall" |
| **08-17** | `investing_en` | "European gas gains for **4th straight session** as Hormuz blockade risks escalate" |
| **08-17** | `yahoo_finance` | "Brent Crude Nears $89 As Hormuz Stays Disrupted – Exxon, Chevron And Shell Rack Up Record Cash Flow" |
| 08-16 | `bloomberg` | "Iran MOU Expires With Diplomacy Still in Play" · "Israel Strikes Lebanon as End of US-Iran Ceasefire Looms" |
| 08-16 | `fortune` | ★ **"Covert mideast oil flows are keeping global prices in check"** — the named counter-mechanism |
| 08-15 | `bloomberg` | "Iran, Oman Home In on Hormuz Strait Deal as Ship Attacks Mount" ← **the item yesterday's DRIFT fired on** |
| 08-15 | `investing_en` | "ADNOC vessel attacked in Hormuz" · `zerohedge` "Somali Piracy Surges Amid Hormuz Blockade" |
| 08-14/15 | `aljazeera`·`scmp`·`upi`·`dw`·`forbes` | Trump to declare the Strait **US territory**; Iran rejects it as *"delusions"* |
| 08-13 | `yahoo_finance` | "Hormuz Stalemate Raises Risk of **$120 Oil**" |

★ **The trajectory, from `thread --days 7`:** the Iran thread is **REIGNITED, 5 days, 5→10→10→9→6
outlets, 100 articles** — today's node is *"Iran's Secret Plan to Escalate the War"* (6 outlets). The
negotiation branch that DRIFT fired on yesterday is **explicitly stalled today** (`toi`: "talks on
Strait opening stall"; `economictimes`: "no breakthrough in Iran war talks"), and the US applied a
**threat to the mediator** (`bloomberg`: Trump threatens Oman).

★★ **The measured refutation of the obvious read.** Settled closes, benchmark named inline:

| | 08-11 | 08-14 | Δ (4 settled sessions) | vs `SPY` |
|---|---|---|---|---|
| Brent `BZ=F` | 88.91 | **88.52** | **−0.44%** | — |
| WTI `CL=F` | 83.20 | **82.40** | **−0.96%** | — |
| `XLE` | 60.93 | 61.91 | **+1.61%** | **+0.86pp** vs `SPY` +0.75% |
| `XOP` | 178.37 | 180.49 | +1.19% | +0.44pp |
| `SPY` | 770.56 | 776.34 | +0.75% | — |

⇒ **Hormuz traffic collapsed and crude went DOWN.** The `fortune` piece names the mechanism (covert
flows). ⇒ **"$90 oil" is a level the market has sat at since 08-11, not a repricing** — the headline
*"crude approaches $90 again"* is arithmetically true and informationally empty.
★★★ **This is the discriminating observation for the desk's own Energy thesis.** `STANDING_VIEW_US §3a`
holds `MPC`/`PSX`/`VLO` as **"refining-CAPACITY destruction, not a crude trade."** The 08-11→08-14 tape
is exactly what that thesis predicts and what a crude-premium thesis does not: **crude flat-to-down,
energy equities modestly up.** ⚠ **C4**: four sessions, one benchmark — this **narrows** the alternative,
it does not confirm the thesis. ⚠ And `M707`'s three refutations (no OBV confirmation on the +19% move,
bearish RSI divergence, no issuer event until 11-03) are **unchanged and not cancelled by this**.

### D-2 · Rates — the market is unwinding a HIKE premium, and `[FRED]` cannot see it

Thread: **REIGNITED, 5 days, 7→8→8→6→7 outlets, 165 articles — the largest thread on the board.**
Today's nodes: *"Fed rate hike bets retreat as markets await retail earnings"* (**7 outlets**) ·
*"Goldman Sachs: September Fed rate hike very unlikely as inflation…"* (5) · *"Goldman Says Markets Too
Hawkish on Betting Fed Will Hike"* (2) · *"Economists agree: Fed to leave interest rates unchanged"* (2)
· *"Dollar falls to lowest since early June as rate hike bets fade"* (4).
⚠ **Note the sign — the market has been pricing HIKES, not cuts**, which is the frame `P61`/`P65` sit in.
⚠ **`[FRED]`'s last `DGS2` is 08-13 and `dxy` is 08-07** ⇒ the instrument that would score this is
**3 to 10 days behind the story**. This is `D212` (H.15 publishes late) meeting a live repricing.
Counter-node in the same window: *"Headline Inflation Is Easing, but Trumpflation Isn't"* (4 outlets) ·
*"Japan's Bond Yields Climb on BOJ Hike Bets, Fiscal Concerns"* (3) · *"Global Bond Yields Climb Due to
Inflation Fears"* thread (8→3→3→3).

### D-3 · Growth — three Asian prints, all soft, all in one session

*"Japan stocks edge lower after GDP growth miss"* (**8 outlets**; Q2 **+1.1% annualized**, thread
BUILDING 3→8) · *"China's Economic Activity Weakened in July"* (4) · *"Thai Growth Slows to 1.9% as
Energy Prices Counter Stimulus"* (5, thread REIGNITED 2→3→3→3→7). Against it: *"Emerging markets march
out of 'valley of tears'"* (4) and *"Emerging Asian currencies rise as softer dollar…"* (4).
⚠ **Both halves**: Japan's print is a *miss* on the level and still **positive growth** — the outlets
split on which half leads (`bloomberg`-family: *"Japan's Economy Keeps Growing, But Weakness Could Vex
BOJ"*).

### D-4 · AI / memory / optical — three instruments converge on one node

- **Memory**: `HBM` bursts at **z = 7.2** (4 items, 2 outlets). *"Market Chatter: Apple May Buy Chinese
  Memory Chips Despite US…"* (4 outlets) · *"Chipmaker CXMT becomes China's most valuable company"*
  (REIGN 5→3) · *"Billionaire Stanley Druckenmiller Dumped Micron and Intel"* (4 outlets; `DRUCKENMILLER`
  and `DUQUESNE` both new words) · *"Stock Market Today: Dow Falls, Nasdaq Rises As Memory Chip Sto…"*.
  ⇒ **This is the desk's own regime call's subject matter arriving from three directions at once**, and
  `S37` (the CXMT branch in which a funded entrant is *bullish* for incumbents) settles 09-30.
- ★★ **Optical / interconnect — the convergence worth naming.** `theme_age optical` **1.74×, the highest
  accel of thirteen terms probed** · `OPTOELECTRONICS` bursts at **z = 5.7** · a **BUILDING** thread
  *"Lightmatter sets optical interconnect blueprint as AI hi…"* · and the same window carries
  *"Lumentum, CoreWeave, SMCI, and More Stocks That Explain…"* (REIGN 5→4→2→4). **Three independent
  instruments, one node**, on the layer `S86` describes as *"the desk's maximum flow score, with zero
  exposure"* and `D250` records as having **no row in the cycle registry**. ⚠ `COHR` round-tripped
  −14.06% (08-07→08-14) while `LITE` held +21.9pp exc20 — **`M-` says they are not one node**, so the
  layer may not be traded as one name.
- **AI capex/credit** (`P67`'s subject): *"What Nvidia's $500 billion Wall Street deal signals"* (REIGNITED
  13→9→6→4→6, 100 articles) · *"Nvidia Downsizes Plans for $250 Billion Guarantee"* (4→3) ·
  *"Hyperscaler AI borrowing binge shakes up foreign credit"* (3→2) · *"Big investors hunt for tomorrow's
  AI winners as capex…"* (4) · *"Alphabet's Reported $112 Billion Profit Included a $94 Billion…"* (4).
  ⚠ **Labelled narrative-only** — `HY OAS` is flat at 2.71% for a sixth session.
- **Defense**: **`KUBASIK` appears as a new word at a 0% baseline** (3 items, 3 outlets) — L3Harris's CEO.
  ⚠ `LHX` is the **only** name negative on both 20d and 60d inside `M704`'s defense EW. Handed to
  EVENT_ALPHA as a named, un-body-read lead; **no direction is claimed here** (P4).

### D-5 · What the desk cannot see, stated as a number
**369 of 384 single-outlet items were not shown, and all 384 are unscored because the classifier is
Korean-only.** ⚠ Any claim in this report about FX or the rates primaries is therefore **thread- and
headline-grade, never denominator-grade.** `D257-KR`'s "declare which index" rule has a US analogue
here: **declare which tier**.

---

## §E · Propositions — falsifiable, both directions, mandatory anti-signal

### P69 — ★★★ The MANDATORY both-sides bracket on today's D-0 binary: does a Hormuz shutdown reprice crude at all?
**Claim.** The 60-day US–Iran MoU expired **2026-08-17** with Hormuz traffic near zero (5 outlets,
§D-1), and **four settled sessions of escalation have produced a −0.44% Brent move.** Spec positioning
is **18th-percentile short**, snapshotted 08-11, i.e. **before** the escalation. `[news]` mechanism,
`[measured]` price. **This row exists because a one-way tilt into a known binary is a protocol
violation, and because the escalation half is the one the tape refuses to pay.**
**Direction A (the shutdown finally reprices):** at the **2026-08-21** settle, `BZ=F` **≥ 93.00**
(+5.1% from the 08-14 settle of 88.52) — a move outside the 88–89 band crude has held since 08-11.
**Direction B (covert flows / demand dominate — the `fortune` mechanism wins):** `BZ=F` **≤ 86.50** at
the same settle, i.e. crude *falls* through the escalation.
**Between (86.50 – 93.00) = C, no information** — and **C is the favourite on the base rate, disclosed
here at registration**: the realised 4-session range is 87.07–88.98, a 2.2% band.
**🚨 Mandatory anti-signal:** a **US refinery outage, PADD3 hurricane landfall, or an OPEC+ quota
decision** inside the window makes any crude move non-attributable to Hormuz ⇒ **VOID**, not scored.
**⚠ C4/S1:** four settled sessions is n=1 episode, not a base rate for "escalations don't move crude."

### P70 — ★★★ The refining thesis's discriminating test, now that crude has volunteered the control
**Claim.** `STANDING_VIEW_US §3a` holds `MPC`/`PSX`/`VLO` as **capacity destruction, not a crude
trade** — a claim that has never had a clean control because crude and cracks usually move together.
**08-11 → 08-14 supplied one**: Brent **−0.44%**, WTI **−0.96%**, `XLE` **+1.61%** and `XOP` **+1.19%**
vs `SPY` **+0.75%**. `[measured]`, benchmark named inline.
**Direction A (capacity thesis):** at the **2026-08-21** settle, `EW{MPC,PSX,VLO}` 5-session excess vs
**`SPY`** is **≥ +2.0pp** *while* `BZ=F` 5-session return is **≤ +2.0%** — the equities pay without the
barrel.
**Direction B (it was a crude trade after all):** `EW{MPC,PSX,VLO}` 5-session excess vs `SPY`
**≤ −2.0pp** *while* `BZ=F` is **≥ +2.0%** — the barrel pays and the equities do not.
**Between = C.**
**🚨 Mandatory anti-signal:** an **issuer event** (guidance, outage, M&A) at any of the three inside the
window ⇒ **VOID for that leg**; the desk's own §3a records **no scheduled issuer event until 11-03**,
so this anti-signal is reachability-checked at registration (`D272-KR`'s rule).
**⚠** This row does **not** re-litigate `M707`'s three refutations (no OBV confirmation, bearish RSI
divergence at the upper band). A confirmed branch A would strengthen the *mechanism*, not the *entry*.

### P71 — ★★ The desk's term instruments cannot see a story that never left — and this is testable, not merely observed
**Claim.** On the day of a D-0 geopolitical binary, **13 of 13 `theme_age` probes returned ⚪ECHO**
(max 1.74×, Hormuz **1.17×**, `ceasefire` **0.81×**, `tanker` **0.68×**) and **`burst` surfaced zero
Iran/Hormuz/oil tokens** despite being vocabulary-free. Mechanism named: burst's own header says
`field=title`, and its baseline is 30 days in which the term has been continuously present.
`[measured]`, probes timestamped 22:30:56–22:31:20 KST.
**Direction A (structural — the instruments cannot fire on continuing stories):** at the next run in
which the foreign corpus carries a ≥5-outlet dated Middle-East escalation, `theme_age Hormuz` again
reads **< 2.0×** **AND** `burst` again returns **zero** Iran/Hormuz/oil tokens in its top-25 z list.
**Direction B (it was today's particular shape):** either instrument fires on that day.
**🚨 Mandatory anti-signal:** if a human changes `burst`'s field to include bodies, or changes the
baseline window, inside the observation period ⇒ **VOID** (the instrument, not the world, changed).
**⚠ Process proposition, not a market one.** No §G verdict rests on it. It is registered because the
desk has repeatedly been told by its own rights table that *"an empty result is not 'cooled'"* — and
today is the first run with a **measured, dated counterexample large enough to settle the argument.**

### P72 — ★★ `[FRED]` went silent for a full run, and no artifact says so
**Claim.** All **14** FRED series returned **zero new observations and zero revisions** versus the
08-16 pull — a live-pull identity, with no cache in the module. Combined with an identical COT block
(3rd run) and 299/299 identical `flow_score`s (4th run), **three of four macro instruments carried no
information into this run and no artifact records that fact.** `[measured]`. This is `P68`'s claim
reproduced on a **weekday**, which its own registered window did not anticipate.
**Direction A (systemic):** the next run in which ≥1 US session settles still emits no
session/observation counter in `SECTOR_FLOW_US.json §scoring`, and `[FRED]` staleness is again
undeclared in any artifact header.
**Direction B (it self-corrects):** any artifact emits an observation counter or a per-series `asof`
staleness flag before then.
**🚨 Mandatory anti-signal:** a human promoting `us_all_v2_candidate.csv` or otherwise changing the
universe inside the window confounds the identity test ⇒ **VOID**.
**⚠** Registered as the **positive-form remedy** (`D280`): stamp `n_new_sessions_since_prior_run` and a
per-series `asof` age into the artifacts, so a consumer can weight a replay as zero.

---

## §F · Self-backtest — one row scores, and it scores against this desk

| Prop | Claim | Pre-registered KPI | Settle | Observed today | Verdict |
|---|---|---|---|---|---|
| **P65** (08-16) | Long end is a **bull steepener**; `DGS2` not pinned | `30y−10y` ≥0.58 **and** `DGS2` ≤4.15 at the 08-21 `[FRED]` settle | **08-21** | `DGS2` **4.15%**, still the **08-13** observation — **no new `[FRED]` data at all** | **UNSCOREABLE — the window has not advanced.** Not "carried favourably" |
| **P66** (08-16) | Distillate bid has a physical driver **and** a political off-switch | `HO=F`−`CL=F` 20d gap at 08-21 + a further dated strike | **08-21** | No new settled session for the gap. ⚠ **Branch-B watch**: the off-switch actor reappeared — `bloomberg` 08-17 *"Trump Issues Threat to Oman"* is pressure on the **mediator**, not a halt to strikes ⇒ does **not** meet B's ≥3-outlet "dated halt" test | **UNSCOREABLE.** Branch B **not** triggered |
| **P67** (08-16) | AI capex bill migrating to debt; credit does not see it | `HY OAS` ≥2.85% at the first close covering **08-28** | **08-28** | `HY OAS` **2.71%, unchanged for a 6th session**; the *story* spread further (§D-4: hyperscaler borrowing, `NVDA` $250bn guarantee downsized) | **CARRIED, branch B tracking.** Still labelled **narrative-only** |
| **P68** (08-16) | Two instruments cannot distinguish "no change" from "no observation" | next **non-session** run reproduces the 3-way identity **and** no artifact marks it | "the coming weekend" | ★ **Reproduced today — a WEEKDAY**: tape identical (299/299), `[FRED]` identical (14/14, zero new obs), COT identical (11/11), and **no artifact carries a marker** | **CONFIRMED-EARLY, and explicitly NOT counted as the registered settle** — the observable said *"non-session run (the coming weekend)"* and today is a session day that had not opened. **The construction was too narrow; that is a finding about the row, not the market** (`AMBIGUOUS`-class). Superseded by `P72` with a corrected observable |
| **P61** (08-15) | Fed-hike premium detached from oil; driver is DEMAND | `DGS2` at 08-21 vs 4.05 / 4.30 | **08-21** | `DGS2` 4.15%, **08-13** observation | **UNSCOREABLE.** ⚠ §D-2's *"rate hike bets retreat"* thread is **narrative-grade support only** and is not counted |
| **P52** (08-13) | In-line print sent money to growth, not defensives | `XLK` exc5 ≤0 **∧** `XLU` exc5 >0 ⇒ A refuted | 08-19 | Refuting conjunction still cannot fire — **same closes** | **CARRIED, not re-counted** |
| **P53** (08-13) | Materials' broad leg lasted two sessions | ex-`NEM` EW exc5 positive ⇒ A wrong | 08-19 (`S77`) | **−2.097, same closes** | **CARRIED, not re-scored** |

**Running hit-rate.** Scoreable rows this run: **0 of 7 on their registered observables.** Four
consecutive runs have now produced **zero** scoreable price-KPI settles, and the reason is mechanical
(no settled session advanced). ★ **The honest reading is not "the desk is patient" — it is that this
desk has registered seven rows whose common failure mode is that they all settle on the same two dates
(08-19 and 08-21).** That concentration is itself a construction flaw and is handed to PREMORTEM.
★ **The one row that did resolve resolved against the desk**: `P68` was right about the world and wrong
about its own window.

---

## §G · ★ SECTOR TRANSMISSION MATRIX — wind direction only, all 11 GICS

⚠ **This matrix is 90% a RE-PRINT and says so** (`D260-KR`'s gap, applied to this desk). With `[FRED]`,
COT and the tape all identical to 08-16, **only the rows whose driver is a NEWS proposition can have
moved**, and exactly those are marked ★ below. The rest are yesterday's cells re-rendered.

| # | GICS sector | Wind | Driving proposition | Δ vs 08-16 |
|---|---|---|---|---|
| 1 | **Energy** | **OW** | ★ `P69` + `P70` — mechanism upgraded from "five dated strikes" to **"a D-0 binary that the barrel refuses to pay"**. The *capacity* leg gains a control; the *crude-premium* leg loses one | ★ **changed — driver replaced, direction unchanged** |
| 2 | **Industrials** | **OW−** | `M704` (bracket/object mismatch **closed**), `M708` (three businesses, 10.6pp spread). ★ `KUBASIK` surfaces at 0% baseline — a named, un-read defense lead | ★ **watch item added, verdict unchanged** |
| 3 | **Information Technology** | **N+** | `P65`-adjacent duration leg + `S85` (settles 08-21, already at branch C). ★ §D-4: `HBM` z=7.2, `OPTOELECTRONICS` z=5.7, `optical` 1.74× — **the sector's live sub-node is optical/interconnect, which the desk does not own** | ★ **sub-node named; sector verdict unchanged** |
| 4 | **Health Care** | **N** | `S82` (08-20, already above branch A at +3.091). No new driver | — re-print |
| 5 | **Financials** | **N−** | `M40` inversion unrepaired; `R69` stands; `KKR` = `M669`'s relocated node. ⚠ Its `breadth` moved 0.04→0.06 **on instrument flicker only** (§C) — **not a signal** | — re-print, with a false-delta warning |
| 6 | **Materials** | **N−** | G3 flipper (`LIN` 24.7%) ⇒ `wflow` inadmissible. `Copper` COT **100th %ile** crowded long (08-11 snapshot, replay) | — re-print |
| 7 | **Consumer Discretionary** | **N−** | `S93` (08-21). ★ §D-2's *"Goldman Sachs warns of consumer spending slowdown as tax…"* (3 outlets, BUILDING 3→3) and *"Home Depot's Customer Transactions Have Fallen for 5 Str…"* (BUILDING) are **new, dated, and on the bear side** | ★ **changed — bear-side evidence added** |
| 8 | **Communication Services** | **UW** | Bucket membership changed (`EA`). ⚠ Its `breadth` moved 0.08→0.00 **on instrument flicker only** — **not a signal** | — re-print, with a false-delta warning |
| 9 | **Consumer Staples** | **UW−** | Board floor; `TGT` is the internal accumulation (33.6pp intra-sector spread), reports ~08-20 | — re-print |
| 10 | **Utilities** | **UW** | Only real flow absence (0/15 fail at OBV/RS, **before** `vol_surge`). ⚠ `P65`/`R73` make the rate leg a **tailwind**, and the bounce is in the **merchant** leg | — re-print, contradiction carried |
| 11 | **Real Estate** | **UW** | `S90` (08-21); 4 of 12 accumulate (`M131` data-centre unit) | — re-print |

🚫 **ROTATION binding**: IT · Industrials · Materials may **not** be promoted or demoted on `wflow`
(G3 flippers), and **no sector may be moved on a `breadth` change** (§C). `eqflow` or hold.

---

## §H · Linter

`python -X utf8 scripts/report_lint.py llm_outputs/2026-08-17/industry_US/MACRO_REPORT.md` — run below;
findings fixed or exempted with a stated reason. ⚠ It checks **form only** (C1 benchmark · C2 both
halves · S6 future label · D6 OBV-alone); a clean run is not a correct report.

---

## §I · §4c — claims this stage asserted and then refuted (D48 class)

**Count: 2.**

1. 🚨 **This stage drafted "the news axis shows the Hormuz story accelerating" and its own instrument
   refuted it.** `theme_age Hormuz` reads **1.17×** and `ceasefire` **0.81×**; `burst` returns nothing.
   The corrected statement is stronger and became `P71`: **the acceleration is real in the tape of
   events (5 outlets, D-0) and absent from every term instrument** — which is a fact about the
   instruments, not about the risk.
2. 🚨 **This stage drafted "crude is repricing the Hormuz shutdown" from the headline
   *"Crude oil approaches $90 again"* and its own price pull refuted it inside the same stage.**
   Brent was **88.91 on 08-11** and **88.52 on 08-14**: the "approach" is a level it never left. ⇒ The
   corrected reading (`P69`/`P70`) is that the escalation is **unpriced**, which is a materially
   different — and more useful — claim than "oil is rising on Hormuz."

⚠ Both refutations came from **running the control**, not from re-reading the narrative. On a run where
three of four instruments were frozen, the two contradictions the stage found both came from the one
axis that moved.

---

## ✅ EXIT CHECK

- [x] Catalysts injected (`catalyst_calendar --days 10`, saved to the day-folder root) — **2 binaries:
      `NVDA` 08-26 (D-9) and the undated Hormuz statement.** ★ **And the stage recorded that the
      calendar MISSED a D-0 binary** (§D-1) rather than accepting its output — `D259-KR` reproduced.
- [x] Narrative read: **events** (`brief --body 2`), **trajectories** (`thread --days 7`), **term sweep**
      (13 `theme_age` probes), **blindspot** and **burst**. Indicators: FRED primaries + COT positioning.
      Daily anchor = the 08-16 `MACRO_REPORT.md`, read (its `P65`–`P68` are scored in §F).
- [x] **`--body 2` used; tail = 0.**
- [x] **`tail = 0` is NOT the coverage claim** — the three recovery sections are quoted with counts in
      §D: single-outlet **15 shown / 384 total (369 withheld, all unscored — Korean-only classifier)**,
      boundary band **0/0**, sub-events **41**. **No "quiet bucket" claim is made anywhere in this report.**
- [x] **Denominator is the corrected one** — 1,965 articles → 347 events, 0 non-market excluded.
- [x] **Trajectories read**; every proposition names its thread's tag and curve (Iran REIGNITED
      5→10→10→9→6 · Fed REIGNITED 7→8→8→6→7 · optical BUILDING · Japan-GDP BUILDING 3→8).
- [x] **Every headline print cited with both halves** — CPI core MoM +0.215% vs headline +0.074% on
      like-for-like months; Japan Q2 "miss" quoted as *still positive growth*.
- [x] **Every relative-performance number names its benchmark inline** (`SPY` on every excess figure).
      No statistical result carried across markets — the IC ledger is KR and is **not** cited here (W1).
- [x] **Credit axis read and cited** — `hy_oas` **2.71%** and `nfci` **−0.549**; the AI-credit
      proposition (`P67`) is explicitly labelled **narrative-only** because the instrument is flat.
- [x] **`real_10y` quoted with `breakeven_10y`** (2.39% / 2.27%) and the decomposition stated.
- [x] Linter run (§H).
- [x] **Transmission matrix produced, all 11 sectors** (§G) — and marked **re-print vs changed**
      per row, which is `D260-KR`'s remedy applied to this desk.
- [x] MACRO_REPORT.md written; **self-backtest appended with an honest 0-of-7 scoreable count** and the
      one row that resolved resolving **against** the desk; new blind-spot terms (`optical`,
      `optoelectronics`, `HBM`, `MoU`, `blockade`, `Strait`, `Oman`) folded into the probe set.

---

# §5 · DRIFT ADDENDUM — appended 2026-08-17 23:07 KST (Stage 11/11 · L1·DRIFT) ★append-only

> The original report above is **not rewritten**. This section is appended beside it so the call and
> its correction stay visible together — that asymmetry is what the self-backtest eats.

## 5-0 · The instrument, reported FIRST (PREFLIGHT G1 binds this stage explicitly)

**`drift_watch.py --report …/MACRO_REPORT.md` ran at 23:07:18 KST and ANSWERED.**
Verdict: **✅ no kill-switch term burst.** Monitoring window as reported by the tool: **0.5h**
(report completed **22:37**, probe **23:07**).

🚫 **That verdict may not be read as "no drift", and PREFLIGHT says so in advance.** Two reasons, both
measured:
1. **The window is 0.5h against the stage's own specification of +3–6h.** A 30-minute window on a
   news corpus that ingests on a lag is close to no window at all.
2. **The desk measured 0 of 120 "silent" names as genuinely quiet across three runs.** An empty burst
   list from this corpus is not evidence of calm.
⇒ **The correct statement is: the instrument answered, it found nothing, and it was looking for 30
minutes at a corpus that cannot yet contain the session.**

## 5-1 · ★★ So this stage checked the one thing the corpus cannot see — the live tape

The US session opened at **22:30 KST**, i.e. **during this run**, and had been trading **~37 minutes**
when this addendum was written. The report above is built entirely on the **2026-08-14** settled close
(PREFLIGHT G0). ⇒ The sharpest available staleness test is not a term burst; it is **whether the
session that opened mid-run is moving the rows this run registered.**

**Live intraday prices, pulled 23:07:35 KST = 10:07 ET. 🚨 These are PARTIAL BARS ~37 minutes into a
6.5-hour session. They settle nothing, they are never mixed with the sweep frame, and every registered
row below settles on a SETTLED close on 08-19 / 08-20 / 08-21.**

| | 08-14 settled | 08-17 live 10:07 ET | Δ | vs `SPY` |
|---|---|---|---|---|
| `SPY` | 776.34 | 775.39 | **−0.12%** | — |
| **`LHX`** | 291.82 | **282.71** | **−3.12%** | **≈ −3.00pp** |
| **`COHR`** | 325.83 | **341.72** | **+4.88%** | **≈ +5.00pp** |
| `LITE` | 926.14 | 948.28 | +2.39% | ≈ +2.51pp |
| `PSX` | 233.61 | 238.37 | +2.04% | ≈ +2.16pp |
| `MPC` | 355.42 | 361.59 | +1.74% | ≈ +1.86pp |
| `VLO` | 341.67 | 347.24 | +1.63% | ≈ +1.75pp |
| `XLE` | 61.91 | 62.35 | +0.71% | ≈ +0.83pp |
| **`KKR`** | 114.01 | **110.84** | **−2.78%** | ≈ −2.66pp |
| `ABNB` | 184.06 | 182.10 | −1.06% | ≈ −0.94pp |
| `TGT` | 154.48 | 154.14 | −0.22% | ≈ −0.10pp |
| `NVDA` | 225.16 | 225.57 | +0.18% | ≈ +0.30pp |
| **Brent `BZ=F`** | 88.52 | **88.97** | **+0.51%** | — |
| WTI `CL=F` | 82.40 | 82.59 | +0.23% | — |

## 5-2 · 🚨 What this does to the rows this run registered — three are moving hard on day one

| Row | Threshold | Day-1 state (partial bar) | Read |
|---|---|---|---|
| **`S97`** `LHX` 5-session excess ≤ **−4.0pp** = branch A | −4.0pp over 5 sessions | **≈ −3.00pp in one session** | 🚨 **~75% of branch A on day one.** The CEO-exit read is confirming faster than the bracket assumed, and the **±3.7% implied move with skew +0.0** — the anomaly the row flagged at registration — is already breached intraday |
| **`S96`** `EW{COHR,LITE}` 5-session excess ≥ **+5.0pp** = branch A | +5.0pp over 5 sessions | **≈ +3.75pp in one session** | 🚨 **~75% of branch A on day one.** ★ And it lands on the leg the DEEP was *most* sceptical of: `COHR`, the name with rs60 **−13.7** that had round-tripped below its 332.48 trigger |
| **`P70`** refiners ≥ **+2.0pp** *while* Brent ≤ **+2.0%** | both, at the 08-21 settle | equities **+1.75 to +2.16pp**, Brent **+0.51%** | ✅ **Tracking branch A** — the capacity-not-crude reading, so far |
| **`S95`** Brent ≥93.00 = A · ≤86.50 = B | 08-21 settle | **88.97** | **Inside the declared NO-INFORMATION band**, exactly as registered. The 4-session 87.07–88.98 range is now a 5-session 87.07–88.98 range |
| `S78` `KKR` | 08-19 | ≈ −2.66pp | Moving against the name the sheet called Financials' only admissible 🟢 |

## 5-3 · ★ The correction this addendum owes the report above

**§D-1 and §2's headline reading was "the barrel refuses to pay".** One session later Brent is
**+0.51%** and the refiners are **+1.7 to +2.0%**. ⇒ **The claim is not refuted — it is sharpened:**
crude moved **half a percent** while the equities moved **four times that**, which is the *same*
divergence the report described, one notch wider. **`P70`'s conjunction was written for exactly this
shape and it is tracking branch A.**

⚠ **But the honest limit is larger than the finding.** Every number in §5-1 is a **37-minute partial
bar**. The desk has an explicit measured rule about this (`project_hyper_execute_intraday_close`-class
error: an unsettled bar read as a close). **Nothing here scores, confirms or falsifies any registered
row.** The rows settle on **08-19 (`S78`, `S75`–`S77`, `S80`)**, **08-20 (`S82`, `S83`, `S98`)** and
**08-21 (`S84`–`S91`, `S93`, `S95`–`S97`, `P65`–`P70`)**, on settled closes.

## 5-4 · What did NOT drift

- The **D-0 binary** (`MACRO_REPORT §D-1`) produced **no new dated Hormuz item** inside the 0.5h window.
  ⚠ Per §5-0 that is not evidence of quiet.
- `NVDA` **+0.18%** — the 08-26 print is still nine days out and nothing moved it.
- `TGT` **−0.22%** — the pre-print flow/positioning disagreement (`BET §C`) is unresolved and stays
  unresolved until its ~08-20 print.

## 5-5 · This addendum's own §4c line (D48 class)

🚨 **This stage drafted "no drift — the instrument returned a clean burst list" and then refuted its
own draft by looking somewhere else.** The burst list *was* clean; the tape was not. **Two of this
run's four new brackets moved ~75% of the way to a branch inside 37 minutes**, and a term-burst
instrument watching a lagging news corpus for 30 minutes had no chance of seeing it.
⇒ **The transferable finding, stated positively: DRIFT should read the live tape against the run's own
registered thresholds, not only the news corpus.** Registered as a new dig (`D282`) — the burst check
answers "did the story change", and this run needed "did the price already move on my own brackets".
