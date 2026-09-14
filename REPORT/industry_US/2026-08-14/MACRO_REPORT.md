# MACRO_REPORT — industry_US · 2026-08-14 · Stage 3/11 (L1·MACRO)

> Falsifiable propositions + the sector transmission matrix (ROTATION's input). Analytical only — no
> sizing, no buy/sell (P4). Prices **pinned to the 2026-08-13 settled close**; benchmark **`SPY` named
> inline on every relative number (C1)**. `[FRED]` values are this run's own pull.
> Run clock **KST 2026-08-14 22:35–23:2x = ET 09:35–10:2x, Friday — the US cash session IS OPEN.**

---

## §0 · 🚨 AMENDMENT TO PREFLIGHT G1 — written first, because it changes what the rest of this stage may cite

**PREFLIGHT G1 (22:15 KST) recorded the news axis DEAD on 5/5 `URLError`. At 22:34:57 KST the same
tunnel returned `Nvidia` = 3,835 hits.** Nineteen minutes. `chain-hop`, `fts search`, `theme-age` and
`blindspot` all ran normally afterwards and their output is used below.

**This is a SCOPE NARROWING, not a reversal. Three things stay revoked and one is restored:**

| Object | Status | Reason |
|---|---|---|
| `SECTOR_FLOW_US.json` **`vel_coverage` 17.0%** and its **51-name survivor sample** | 🚫 **STILL REVOKED** | The sweep scored at **22:12, inside the dead window.** The number is a property of the outage. Re-running the bridge afterwards does **not** retro-fix a written file |
| "This theme went quiet" / "the tape is silent" | 🚫 **STILL FORBIDDEN** | A single-probe silence is now measured to be a **19-minute artifact** at least once |
| **`theme-age` verdicts** | 🚫 **REVOKED ON A NEW, INDEPENDENT GROUND** — see §D-4 | 6 of 6 terms returned the identical `🟡ACCELERATING` at accel **4.03×–7.71×**, including `term premium` on a base of **14 articles**. An instrument that cannot separate 2,936 Hormuz articles from 14 is not discriminating **today** |
| **Direct `fts search` · `chain-hop` · `blindspot` · client-store `brief`/`thread`** | ✅ **RESTORED, with source+date on every cited line** | All ran successfully 22:34–22:52 |

⚠ **This is the second consecutive run in which G1's single probe over-revoked**, and the pattern is
now dated on both sides: **DEAD 08-13 22:14 → ALIVE 08-14 08:40 (KR desk) → DEAD 08-14 22:15 → ALIVE
08-14 22:35.** Registered **`D259`** (amended at `HANDOVER.md §10`): **G1 must probe three times spaced
≥10 minutes before revoking anything.** This stage ran that test — §E·P55.

⚠ **It also refuted this run's own HANDOVER §3a/§3b.** Corrected in `HANDOVER.md §10` by **append**, and
one ledger row changed outcome (`INSW` `reaffirmed` → **`entered`**). Not edited away.

---

## §A · The rate/credit axis — `[FRED]`, this run's own pull

| Series | asof | Value | 20-obs ago | Δ |
|---|---|---|---|---|
| `DGS10` | **2026-08-12** | **4.68** | 4.55 | **+13bp** |
| `DGS2` | 2026-08-12 | **4.20** | 4.13 | +7bp |
| `DGS30` | 2026-08-12 | **5.24** | 5.08 | **+16bp** |
| `DFII10` real 10y | 2026-08-12 | **2.42** | 2.32 | +10bp |
| `T10YIE` breakeven | **2026-08-13** | **2.24** | 2.22 | +2bp |
| `BAMLH0A0HYM2` HY OAS | 2026-08-12 | **2.71** | **2.71** | **0bp** |
| `BAMLC0A0CM` IG OAS | 2026-08-12 | 0.79 | 0.79 | 0bp |
| `NFCI` | 2026-08-07 | **−0.549** | −0.464 | **looser** |
| `DTWEXBGS` | 2026-08-07 | 119.065 | 120.505 | **−1.19%** |
| `UNRATE` | 2026-07 | **4.1%** | Apr 4.3 · May 4.3 · Jun 4.2 | **3rd consecutive fall** |
| `VIXCLS` | — | 🚨 **`[FRED]` 502 Bad Gateway, retried once, failed twice** | — | substituted `^VIX` **[yfinance]** 14.63 (08-13 settle) vs **18.77** 20 sessions ago |

### A-1 · ★★★ The load-bearing decomposition: this is TERM PREMIUM at the long end, and nothing else confirms stress

| Date | 10y | 2y | **2s10s** | 30y | **30y−10y** |
|---|---|---|---|---|---|
| 2026-07-28 | 4.61 | 4.26 | **+0.35** | 5.09 | +0.48 |
| 2026-08-05 | 4.63 | 4.18 | +0.45 | 5.17 | +0.54 |
| 2026-08-11 | 4.70 | 4.22 | +0.48 | 5.24 | +0.54 |
| **2026-08-12** | **4.68** | **4.20** | **+0.48** | **5.24** | **+0.56** |

**2s10s has steepened 13bp in eleven sessions and 30y−10y is at +0.56, the widest in the window** —
while the **2-year is unchanged** (4.26 → 4.20). The move is **entirely long-end.**

Now the four things that would normally accompany a long-end selloff, and **none of them is present**:
- **Inflation expectations**: `T10YIE` **2.24 on 08-13, DOWN 2bp from 2.26** and in the bottom
  quartile of a 2.18–2.50 365-day range. **The long end sold off while breakevens fell.**
- **Credit**: HY OAS **2.71 = exactly its own 20-obs-ago value**, 8bp off a 365-day low; IG **0.79**
  flat. **Zero credit confirmation, in either direction.**
- **Financial conditions**: `NFCI` **−0.549 and still loosening** (−0.464 twenty obs back).
- **Volatility**: `^VIX` **14.63** at the 08-13 settle vs **18.77** twenty sessions ago **[yfinance]**.

⇒ **Not inflation (breakevens down), not credit stress (OAS flat at the tights), not a growth scare
(VIX at 14.6, NFCI loosening). The residual is term premium / supply at the long end.**
⚠ **C3**: this desk has **no direct term-premium series** (no ACM/KW pull) — the reading is the
residual after excluding the three measured channels, not a measured decomposition. Labelled
`[inferred]` and it may not be cited downstream as evidence.
★ **And the tape has not named it**: `term premium` returns **0 title hits in 49,722 seven-day
articles** (§D-3). The single largest structural move on the board has **no narrative attached.**

### A-2 · ★★★ Both halves of the July CPI, `[FRED]`-confirmed — and "cool" is a sequential artifact

| | Jun index | **Jul index** | **MoM** | **YoY (12-obs)** |
|---|---|---|---|---|
| `CPIAUCSL` headline | 332.568 | **332.813** | **+0.074%** | **+3.30%** |
| `CPILFESL` core | 336.065 | **336.789** | **+0.215%** | **+2.47%** |

⚠ **C2, and it is decisive here.** The "cool CPI" reading is a **sequential** reading, and its
denominator is a June that was **outright negative**: May 333.979 → Jun 332.568 = **−0.42% MoM**.
Against that base, July's **+0.07%** is a *rebound*, not a disinflation.
★ **And the two halves point opposite ways**: headline MoM decelerating toward zero while **core MoM
ACCELERATED from −0.017% (June) to +0.215% (July)**. **YoY headline is 3.30%** — not a cool number.
- **PPI (2026-08-13 08:30 ET)** — the desk's inherited *"core +0.4% MoM / +4.7% 12m"* remains
  **`[inferred-source]`** (the BLS primary returned HTTP 403 on 08-13 and this stage did not re-pull
  it). What **is** citable today is the market's own reading: *"Wholesale prices flatten out in July
  and inflation eases. A Fed rate hike is in doubt."* [`MarketWatch` via google_en, 2026-08-13].
  🚫 **Neither PPI half may be quoted as a primary number by this desk until BLS or `[FRED]` returns it.**

### A-3 · The labour leg, which cuts the same way as the long end
`UNRATE` **4.3 → 4.3 → 4.2 → 4.1** over Apr→Jul. **Three consecutive monthly declines.** A tightening
labour market alongside a re-accelerating core is a **hike-side** input, and it is why §D-3's
`rate hike` acceleration is not merely a headline artifact.

---

## §B · Positioning — COT (Tue-close, 3–4d lag) + FINRA daily. **Context, never a trigger.**

### B-1 · CFTC COT — three crowded shorts sitting against the tape, and two crowded longs

| Instrument | Net spec | 1y %ile | Verdict | ⚠ What it sits against |
|---|---|---|---|---|
| **UST 10Y** | −979,243 (**−103,124 wk**) | **3%ile** | 🔴 crowded short | **the curve is steepening** — this is the squeeze fuel *against* the A-1 move |
| **Nasdaq-100** | −35,006 (**−25,091 wk**) | **0%ile** | 🔴 crowded short | `XLK` exc20 **+3.846 = best of 11** (§C) |
| **WTI Crude** | +23,033 | **18%ile** | 🔴 crowded short | crude **+5.12% over 5 sessions** to the 08-13 settle |
| **Nat Gas** | −197,546 | **1%ile** | 🔴 crowded short | — |
| **Copper** | +77,123 | **100%ile** | 🟢 crowded long | Materials ex-NEM EW exc5 **−1.893** (§C-2) |
| **USD Index** | +22,499 (**+5,302 wk**) | **81%ile** | 🟢 crowded long | `DTWEXBGS` **−1.19%** over 20 obs — **long and losing** |
| S&P 500 e-mini | −27,258 | 80%ile | 🟢 crowded long | — |
| Gold · Silver · Russell | — | 29 / 29 / 26%ile | 🟡 neutral | — |

★ **The single most striking cell is Nasdaq-100 at the 0th percentile of a year while `XLK` leads the
board on 20-session excess.** ⚠ **D6 / P4**: an extreme percentile is **ammunition, not direction.**
Registered as an observable in P57, not used as a tilt.

### B-2 · FINRA short pressure on the 2026-08-13 settled session

| ETF | short% | z vs own 20d | 5v5 trend | Verdict |
|---|---|---|---|---|
| **XLC** | 75.3% | **+2.15** | **+12.4▲** | 🔴 **short surge — the steepest of the eleven** |
| **XLV** | 77.6% | **+1.66** | −1.8▼ | 🔴 short surge |
| XLP | 74.5% | +1.39 | +8.4▲ | 🟡 |
| XLU | 62.8% | +1.32 | +9.0▲ | 🟡 |
| **SPY** | 67.8% | +1.18 | **+11.3▲** | 🟡 — index-level hedging is rising |
| XLB | 76.6% | +0.68 | +10.4▲ | 🟡 |
| XLE · XLI | 56.3 / 64.1% | +0.57 / +0.44 | +1.8▲ / +8.0▲ | 🟡 |
| XLK · XLF | 48.6 / 61.0% | −0.11 / −0.26 | −5.6▼ / −8.3▼ | 🟡 |
| **XLRE** | 52.5% | **−1.41** | −10.2▼ | 🟡 pressure leaving |
| **XLY** | 54.1% | **−1.61** | −9.3▼ | 🟢 **short covering** |

⚠ **D3/D6**: short-volume ratio includes market-maker hedging and is **unsigned as to intent**. The
readable object is the **z vs the ETF's own base**, not the level. **XLC's +2.15 with a +12.4 trend
and XLY's −1.61 with a −9.3 trend are the two extremes and they point opposite ways.**

---

## §C · The tape — settled **2026-08-13**, benchmark `SPY` inline (C1)

🚨 **A within-run catch, recorded rather than fixed silently (D74).** A pull made at ~22:33 KST
returned a **2026-08-14 bar** — the US session had opened between this stage's first and second pull.
Every number below was **re-pulled and pinned to `index <= 2026-08-13`**, and the difference is not
cosmetic: `XLE exc5` read **+5.936 on the live bar vs +3.774 pinned**, and `NEM exc5` **+3.484 vs
+7.096**. **The live bar would have moved two propositions.**

| ETF | exc5 | **exc20** | exc60 |
|---|---|---|---|
| **XLK** | +1.723 | **+3.846** ①| +4.101 |
| **XLE** | **+3.774** ①| **+3.467** ② | −4.519 |
| XLV | +1.177 | +0.449 | **+10.239** ① |
| XLI | −0.655 | −0.487 | +3.497 |
| XLB | −0.944 | −0.828 | −1.149 |
| XLF | −0.434 | −0.957 | **+7.290** ② |
| XLP | −0.167 | −3.396 | −5.195 |
| XLY | −0.916 | −2.672 | −3.480 |
| XLC | +0.020 | −3.707 | **−9.098** ⑪ |
| XLRE | −0.521 | −4.366 | −2.180 |
| **XLU** | +0.309 | **−6.763** ⑪ | −5.083 |

### C-1 · The 20-day and the 60-day windows disagree about four sectors, and the disagreement is the read
`XLV` is **11th-ish on 20d (+0.449) and 1st on 60d (+10.239)**; `XLF` is **−0.957 on 20d and +7.290 on
60d**; `XLE` is **+3.467 on 20d and −4.519 on 60d**; `XLK` is the **only sector positive on all three
windows**. ⚠ **C5 stated rather than smuggled**: which of these sectors "leads" is a **choice of
window**, and this report does not pick one — it names both, every time.

### C-2 · ★★★ Materials is one name, and the measurement is now unambiguous
`NEM` exc5 **+7.096** · exc20 **+22.101**. The **equal-weighted ex-NEM basket of 12** reads
**exc5 −1.893 with 1 of 12 positive** (only `DOW` +4.270; `FCX` −5.170 and `PPG` −5.015 the worst).
⇒ **the sector's aggregate carries no information about the sector.** This is `P53` direction A
confirmed, and it is `S77`'s registered instrument.
⚠ Independent and pointing the same way: **copper spec at the 100th percentile** (§B-1) with the
mining complex negative — positioning is long the commodity while the equities are not participating.

### C-3 · Energy: the crack, and it is the physical leg
| Contract, all settled 08-13 | 1d | 5d | 20d |
|---|---|---|---|
| `CL=F` crude | **−2.43%** | **+5.12%** | +2.91% |
| `HO=F` distillate | −1.24% | **+9.50%** | +5.46% |
| `RB=F` gasoline | −0.81% | +6.45% | −4.77% |

**3-2-1 crack: 59.34 (5 sessions ago) → 65.84 (08-13) = +6.50 crack points**, though still below
**69.45** twenty sessions back. **Products outran crude on the 5-day (HO +9.50 vs CL +5.12) ⇒ margin
expansion, not a barrel-price effect.** Refiners lead the board on RS20 vs SPY: **MPC +12.900 ·
PSX +11.925 · VLO +10.590**.
⚠ **And on 08-13 itself the barrel fell** (−2.43%) while the day's largest news cluster was
*"The Commodities Feed: Oil prices **cool** despite US-Iran deadlock"* [44 articles / 17 outlets] with
sub-events *"Crude oil dips below $90"* and *"OPEC cuts 2026 demand forecast"*.

---

## §D · News — the axis §0 restored. **Denominators quoted; no "quiet" claim without one.**

### D-1 · Event pass — `brief --date 2026-08-13 --body 2 --scope foreign`

**Corrected denominator: 5,205 articles → 725 events → 725 market / 0 non-market.**
**Coverage accounting, quoted rather than implied (the tail-0 trap):**

| Tier | Shown | Total | **Withheld** |
|---|---|---|---|
| Head (≥5 outlets) | **91** | 91 | 0 |
| Body (2–4 outlets) | ~26 | — | **604** |
| Tail (2 outlets) | 0 | 0 | 0 |
| **1-outlet** | **15 (random sample)** | **588** | **573** |
| Non-market boundary (nb > −3.0) | 0 | **0** | 0 |
| Sub-events recovered (`└`) | — | **195** | — |

🚨 **The coverage claim this run may NOT make.** `tail = 0` here is **not** evidence the day was seen:
**1,177 event-slots were withheld**, and — the harder limit — **all 588 single-outlet events are
UNSCORED because the classifier is Korean-only.** On the foreign feed the tier where *"환율·금리·채권
1차 재료가 여기 산다"* is **not ranked at all, only randomly sampled**. ⇒ **no "nothing happened in
bucket X" statement is available from this pass, for any bucket.** The 0/0 non-market line is the same
artifact, not a clean classification.

**The head, read in full. What it actually held:**
- **Oil cooled *despite* the deadlock** [44/17] — the day's largest event, and it is a *negative*
  print for the war-premium reading.
- **Rate path**: *"S&P 500 Hits Record as Cooling Inflation Boosts Rate-Cut Hopes"* [5/2] sitting in
  the same head as *"Update: US Equity Indexes Mixed as Soft Wholesale Inflation…"* [21/8] with the
  sub-line ★ *"Opinion | Bond Investors Want the Fed to **Raise** Rates"* [2/2]. **The head contains
  both directions of the Fed question on the same day.**
- **AI-power / AI-capex**: Microsoft Copilot super-app [37/9] with sub-events *"IREN Stock Jumps as
  **Microsoft and Nvidia** Back Its AI Cloud"* and ★ *"**SpaceX Has 1.4 Gigawatts of AI Capacity
  Online**"*; IBM×OpenAI [18/9]; *"Midstream Companies Expand Natural Gas Pipelines As LNG And AI…"* [6/4].
- **Physical power stress, Europe**: extreme-heat wave [17/12]; ★ *"Romania **shuts nuclear plant**,
  Hungary dams dry Danube River"* [8/8].
- **Refining supply**: *"Ukraine's drones hit a major Russian refinery 800 miles from…"* [2/2] inside
  the Ukraine cluster [32/15].
- **Intel raised $20bn** in an upsized share sale [7/4].

### D-2 · Trajectories — `thread --days 7 --scope foreign`
Per-day denominator first: **08-08 283 · 08-09 289 · 08-10 787 · 08-11 798 · 08-12 756 · 08-13 725 ·
08-14 0.** 3,638 daily events → 2,882 threads (439 multi-day).
🚫 **No `FADING` / `ENDED` verdict is quoted from this run.** **All 439 multi-day threads are tagged
`ENDED` and "살아있는 0"** — because the window's terminal day (08-14) has **zero articles at this
clock**. That is a window-end artifact; the tool warns about it itself.
**What IS readable — the outlet curves:**
- *"Oil prices hold near one-week high as Strait of…"* — **6→7→22→23→18→17**, peak 23 outlets.
- *"Iran says Hormuz deal close amid attack on UAE t…"* — **15→9→7→6→5→4**.
- *"Ukrainian drone strike on oil-refining city…"* — **12→11→16→13→16→15**, flat-to-rising.
⇒ **the Hormuz *deal* thread is decaying while the oil-price and refinery-strike threads are not.**
That is the same shape `R67` recorded ("attention rotated, the object did not") and it is **not**
re-asserted as decay of the premium itself.

### D-3 · Term sweep — pool-normalised, 7d (08-07…08-13) vs prior 7d, denominators **49,722 / 51,071**

| Term | 7d | prior | share | **ratio** |
|---|---|---|---|---|
| **CPI** | 308 | 10 | 0.619% | **31.64×** |
| ★ **rate hike** | **152** | **56** | 0.306% | **2.79×** |
| ★ **refinery** | 33 | 21 | 0.066% | **1.61×** |
| Taiwan | 88 | 55 | 0.177% | 1.64× |
| gold | 364 | 281 | 0.732% | 1.33× |
| dollar | 394 | 328 | 0.792% | 1.23× |
| power | 468 | 409 | 0.941% | 1.18× |
| PPI · tariff · Hormuz · copper | 231 · 141 · 327 · 50 | 212 · 131 · 315 · 47 | — | 1.12 · 1.11 · **1.07** · 1.09× |
| China · yield · credit · data center | 523 · 238 · 118 · 157 | 538 · 252 · 124 · 171 | — | 1.00 · 0.97 · 0.98 · 0.94× |
| memory · DRAM · Iran · CXMT | 146 · 26 · 520 · 39 | 185 · 34 · 693 · 57 | — | 0.81 · 0.79 · **0.77** · 0.70× |
| **HBM** · earnings beat · **AI capex** | 43 · 60 · 10 | 74 · 108 · 26 | — | **0.60** · 0.57 · **0.40×** |
| ★ **rate cut** | **2** | 3 | 0.004% | 0.68× |
| ★ **term premium** | **0** | 0 | **0.000%** | — |

★★★ **The board's loudest asymmetry: `rate hike` 152 hits and accelerating 2.79×, against `rate cut`
at TWO hits.** Body-verified with named sources rather than left as a count:
- *"Fed's Barkin: Still an 'open question' if **rate hike** will be needed to meet inflation target"*
  [Reuters via `google_en`, 2026-08-13]; **"Hammack backs increase on inflation concerns"**
  [`economictimes` 08-13].
- *"Goldman's Kaplan Backs 'Kick-the-Can' Fed Caution on Rate Hikes"* [`bloomberg` 08-13].
- ★ **the hinge**: *"**Traders Pare Bets on Fed Rate Hike This Year as Oil Prices Fall**"*
  [`bloomberg` 08-13] and *"Stocks rise as traders reduce rate hike bets, oil prices drop"*
  [`yahoo_finance` 08-13].
⚠ **C3 / query hygiene**: the 152 includes **BOJ, ECB and RBI** hits (`"Bank of Japan September Rate
Hike Locked In"`, `"ECB rate hike expectations strengthen"`, RBI at 5.25%). The **direction** claim
above rests on the four named US-Fed articles, not on the count.
★★ **`term premium` = 0 hits in 49,722 articles** while §A-1 measures the largest structural move on
the board. **The corpus is not writing about the thing the curve is doing.**
⚠ **AI-capex/memory decelerating on every term** (AI capex 0.40× · HBM 0.60× · DRAM 0.79× · memory
0.81×) while `data center` holds flat at 0.94× and `power` rises 1.18×. **The narrative is rotating
from the chips to the electricity**, which is the one place the AI thread is still accelerating.

### D-4 · 🚨 `theme-age` returned SIX identical verdicts and is therefore not citable today

| Term | verdict | 7d avg | accel | total |
|---|---|---|---|---|
| Hormuz | 🟡ACCELERATING | 203.3 | 4.03× | 2,936 |
| rate hike | 🟡ACCELERATING | 136.1 | **6.38×** | 1,593 |
| data center | 🟡ACCELERATING | 328.1 | 4.26× | 4,608 |
| refinery | 🟡ACCELERATING | 50.3 | 4.96× | 656 |
| CXMT | 🟡ACCELERATING | 11.9 | 4.23× | 167 |
| **term premium** | 🟡**ACCELERATING** | **1.3** | **7.71×** | **14** |

**6 of 6 identical, accel banded 4.03–7.71×, and the HIGHEST acceleration belongs to the term with
FOURTEEN total articles.** The tool's accel ratio is tracking the corpus's own weekday/weekend shape
(§D-2: weekend days 283/289 vs weekdays 787/798 — a **2.7× denominator swing** inside the window),
not theme-specific acceleration.
🚫 **No `theme-age` verdict is cited anywhere in this run.** The pool-normalised sweep in §D-3, which
divides by its own same-window denominator, **did** discriminate (0.40× to 31.64×) and is used instead.
⚠ **This does NOT resurrect `R31`** (the retracted six-run claim that `theme_age` produces zero
discrimination on the foreign feed, killed 2026-07-30 by a run that returned three distinct verdicts).
**One day of uniformity is not the general claim** — this is a dated measurement with a named
mechanism, and it is registered as `D260`, not as a revival of R31.

### D-5 · Blind-spot pass — run, and one emergent token is worth naming
Top emergent tokens are mostly generic calendar/market words (Energy 549 · July 537 · Oil 533 ·
Revenue 533 · Wall 521). Two are not: ★ **`SpaceX` 492** and `Bitcoin` 439, both above **`Nvidia` 489**
and **`Hormuz` 411**. SpaceX corroborates the head's *"SpaceX Has 1.4 Gigawatts of AI Capacity Online"*
⇒ **a private, un-listable name is one of the loudest AI-power entities on the board.** ⚠ It is
**not investable through this desk's universe** and is registered as context only — the same shape as
the 2026-06-28 SPCX blind-spot miss.
**No macro-relevant new term is folded into the living table this run** (the rest of the emergent list
is calendar noise) — stated as a null result of a check performed, not as a skip.

### D-6 · ★ `P43` (CXMT) — REFRESHED after five unrefreshed runs, and it cuts BOTH ways

| Evidence, foreign-scope sources only | Date |
|---|---|
| *"Chipmaker CXMT becomes China's most valuable company"* [`semafor`] · *"Memory maker CXMT overtakes Tencent … 17 days after its IPO"* [`tomshardware`] | 2026-08-13 |
| *"**Apple is testing Chinese DRAM even after CXMT refused to cut prices**"* [`yahoo_finance`] | 2026-08-12 |
| *"Apple's CXMT Bet Could Strengthen Its Memory Supply, But Risks Remain"* [`yahoo_finance`] | 2026-08-12 |
| *"Apple Tests China's CXMT Memory Chips **Amid AI-Driven Supply Shortage**"* [`nasdaq`] | 2026-08-11 |

⚠ **Out-of-scope sources excluded from the frame** (they surfaced because a direct SQL query bypassed
`--scope foreign`, disclosed rather than used): `chosun` · `mt` · `sedaily` · `google_kr` reporting
DDR5 yield >90% and mobile-DRAM entry. **KR-domestic sourcing may not rank the US frame.**
★★ **The read, and it is the S37 branch**: a funded entrant that **refuses to cut prices**, being
qualified by Apple **because of a shortage**, is a **price-discipline** datapoint, not a price-war one.
⇒ **`S37`'s registered branch ("a funded entrant is BULLISH for the incumbents") now has its first
direct evidence.** ⚠ **C4**: two outlets on one Apple test is not a supply-curve measurement. **`P43`
is refreshed, not resolved**, and CXMT's own term ratio is **0.70× — decelerating**, so this is a
*discrete event* inside a *decelerating* narrative.

---

## §E · Propositions — falsifiable, both branches, mandatory anti-signal

### P56 — ★★★ The long end is repricing TERM PREMIUM, and the three duration underweights are exposed to a channel none of them was written for

- **Claim** `[FRED, measured]`: 2s10s **+0.35 → +0.48** and 30y−10y **+0.48 → +0.56** over eleven
  sessions with **`DGS2` unchanged**, while `T10YIE` **fell to 2.24**, HY OAS is **flat at 2.71**,
  `NFCI` **loosened to −0.549** and `^VIX` sits at **14.63 [yfinance]**. The three named channels are
  all absent; the residual is term premium `[inferred]`.
- **Direction A (~60%)**: a long-end/supply repricing keeps **UTIL and RE** pressured *on the long
  end* regardless of the CPI path — which is why `XLU` exc20 **−6.763** and `XLRE` **−4.366** both
  deteriorated *through* a cool CPI. ⇒ the duration UWs are right **for a different reason than
  registered** (`S63`/`S80` were written on a *policy-rate* mechanism).
  **Track KPI**: `DGS30−DGS10` at the next three `[FRED]` settles; `XLU`/`XLRE` exc20 vs SPY.
- **Direction B (~40%)**: the steepening is the **UST-10Y crowded short (3rd %ile) being pressed**,
  not term premium — in which case it **reverses violently on any risk-off tick** and UTIL/RE get an
  unearned bid. **This is the branch the positioning data supports and the price data does not.**
- ⚠ **Mandatory anti-signal**: **if `DGS30−DGS10` narrows ≥8bp while `XLU` fails to outperform SPY
  over the following 5 settled sessions, direction A's transmission claim is wrong** — the channel
  would have moved and the mechanism would not have paid.
- **Thread**: ★ **none** — `term premium` has **0 title hits in 49,722 articles** (§D-3). A proposition
  with no thread is stated as such, not given a proxy.
- **Catalyst**: next `[FRED]` H.15 prints (daily) · **Jackson Hole** (`bloomberg` 08-13 names Warsh) ·
  August CPI **2026-09**.

### P57 — ★★★ The Fed-hike premium is an OIL function, and this is the SECOND independent measurement of that coupling

- **Claim** `[news, body-verified + measured]`: `rate hike` accelerated **2.79× (152 vs 56)** while
  `rate cut` sits at **2 hits**; Hammack **backs an increase**, Barkin calls it an **"open question"**
  [Reuters 08-13]. **And on 08-13 the coupling printed directly**: *"Traders Pare Bets on Fed Rate
  Hike This Year **as Oil Prices Fall**"* [`bloomberg` 08-13] on a session where `CL=F` fell **−2.43%**
  and the S&P made a record. ★ **`M69` measured this same coupling on 2026-07-24** (TD Securities:
  *"pricing for rate hikes moved alongside oil"*, hike odds 10.7% → 34.7%). **Three weeks apart, same
  mechanism, opposite direction — the coupling reproduced.**
- **Direction A (~60%)**: hike risk is **priced off the oil path, not off the labour or core-CPI
  path**. ⇒ **Energy and the rate-sensitive complex are ONE trade with opposite signs**, and a crude
  decline is simultaneously bearish ENRG and bullish UTIL/RE/growth. **Track KPI**: the sign of
  [Δ`CL=F`] × [Δ hike-odds proxy = `DGS2`] over the next 5 settled sessions.
- **Direction B (~40%)**: the coupling is **coincidental to a single news cycle**; the real driver is
  **core CPI +0.215% MoM with `UNRATE` at 4.1%** (§A-2/A-3), in which case hike risk persists **even
  if crude falls** and the "oil relief" trade is a trap.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if `CL=F` falls ≥5% over 5 sessions while `DGS2`
  **rises**, direction A is refuted; **(b)** if `CL=F` rises ≥5% while `DGS2` **falls**, direction A is
  refuted in the other direction. ⚠ **Both branches must be checked** — this is the oscillating-regime
  class the L1 names as the recurring failure mode.
- **Thread**: outlet curve on the oil-price thread **6→7→22→23→18→17** (peak 23); no `theme-age`
  verdict cited (§D-4).
- **Catalyst**: **Jackson Hole** · the next `[FRED]` `DGS2` prints · **OPEC** (it cut its 2026 demand
  forecast on 08-13).

### P58 — ★★ Energy's strength is the CRACK, and it survived the barrel falling — but only on the 5-day window

- **Claim** `[measured]`: 3-2-1 crack **59.34 → 65.84 = +6.50 points in 5 sessions**, with **products
  outrunning crude** (HO +9.50% vs CL +5.12%); refiners lead the board on RS20 vs SPY (**MPC +12.900 ·
  PSX +11.925 · VLO +10.590**); `XLE` exc5 **+3.774** held **while crude fell −2.43% on 08-13** and the
  day's biggest cluster was *"oil prices cool despite the deadlock"* with **OPEC cutting 2026 demand**.
  ⚠ **`XLE` exc60 is −4.519 and the crack is still BELOW its own 20-session level (69.45)** — the long
  windows have not turned.
- **Direction A (~55%)**: this is a **refining-margin** event (physical), not a war premium — which is
  why it survives a decaying Hormuz-*deal* thread, why `refinery` is the fastest non-CPI term on the
  board (**1.61×**), and why the Ukrainian-drone refinery-strike thread is **flat-to-rising (12→11→16→
  13→16→15)** while the deal thread decays 15→4.
- **Direction B (~45%)**: the +6.50 crack is the **tail of the same premium**; with **WTI spec at the
  18th percentile** nobody has chased it, and a resolution collapses products faster than crude ⇒
  `XLE` exc5 turns negative within 10 sessions and **exc60 −4.519 is the honest window**.
- ⚠ **Mandatory anti-signal, both sides**: **(a)** if crude falls ≥5% while the **crack holds ≥63**,
  direction B is refuted; **(b)** if crude holds ±3% while the **crack falls ≥5 points**, direction A
  is refuted. ⚠⚠ **`R47` binds**: **no stage may state "the distillate bottleneck released" as fact** —
  `S55` scored C and the physical-vs-premium split is **still unseparated.**
- **Catalyst**: **`S75` settles 2026-08-19** · OPEC monthly · the Hormuz binary (undated, §H).

### P59 — ★★ Materials is one name and the positioning is on the other side of it

- **Claim** `[measured]`: ex-NEM equal-weight **exc5 −1.893 with 1 of 12 positive** against **NEM
  exc5 +7.096 / exc20 +22.101**; sector `wflow −0.179` **flips to +0.016 without `LIN`** (G3 flipper,
  24.7% weight) and breadth is **0.00**; **copper spec at the 100th percentile** while `FCX` is the
  basket's **worst name at −5.170**.
- **Direction A (~65%)**: the sector aggregate carries **no information**; the only admissible
  Materials instrument is `S77`'s ex-NEM basket, and the gold leg is a **dollar/real-rate trade**
  (`DTWEXBGS` −1.19%) that belongs in the macro book, not the sector book.
- **Direction B (~35%)**: copper's 100th-percentile long is **early positioning ahead of a broadening**
  and the ex-NEM basket turns positive by the `S77` settle ⇒ the N− tilt must change.
- ⚠ **Mandatory anti-signal**: **if `S77`'s ex-NEM equal-weight 5-session excess is positive on ANY
  settled close through 08-19, direction A is wrong.** ⚠ **G3 binds: `wflow` is inadmissible for
  Materials this run.**
- **Catalyst**: **`S77` settles 2026-08-19.**

### P60 — ★★ The desk's news instrument has an availability window measured in MINUTES, and single-probe revocation is now a measured error

- **Claim** `[measured, this run]`: **5/5 `URLError` at 22:15 KST → 3,835 `Nvidia` hits at 22:34:57
  KST**, same tunnel, **19 minutes apart**, with `chain-hop` / `fts` / `blindspot` all functional
  afterwards. The single 22:15 probe **revoked citation rights that were available 19 minutes later**,
  and it **caused this run's own HANDOVER to mis-resolve a ledger row** (`INSW`, corrected in §10).
- **Direction A (~75%)**: the failures are a **short availability window**, so **any single-probe
  revocation over-revokes**; the correct instrument design is **three probes ≥10 minutes apart**.
- **Direction B (~25%)**: the flap correlates with the KST-evening hour this desk runs, so the
  revocation is **right in expectation even though the diagnosis is wrong**, and the fix is scheduling.
- ⚠ **Mandatory anti-signal**: **if all three of this run's pre-registered probes (22:35 / 22:45 /
  22:55) had failed, direction A would be wrong.** ⚠ **This proposition changes no tilt.**
- **Registered `D259` (amended) · `D260`** (§D-4, the `theme-age` uniformity).

---

## §F · Self-backtest — **2 HIT · 1 HIT(interim) · 1 CARRIED · 1 REFRESHED · 1 CARRIED-undated**

| Proposition | Track KPI it named | Measured now (08-13 settle unless stated) | Verdict |
|---|---|---|---|
| **P51** (08-13) — the 10y's repricing is REAL-rate, not inflation ⇒ UTIL/RE stay pressured | `DFII10` + `T10YIE`; `XLU`/`XLRE` exc20 vs SPY | `DFII10` **2.43 → 2.42 (flat)**, `T10YIE` **2.26 → 2.24 (fell)** ⇒ direction B's 2.35 trigger moved **further away**. `XLU` exc20 **−5.394 → −6.763**, `XLRE` **−2.499 → −4.366** — **both more pressured, through a cool CPI.** Anti-signal (DFII10 −15bp) did not fire | ★ **HIT** — but see P56: the **level** of real rates was flat this week while the **long end** moved, so the *mechanism* is now better described as term premium. **The call is right; its stated cause is being upgraded, not withdrawn.** ⚠ S1: one settled session |
| **P53** (08-13) — Materials' broad leg lasted two sessions; the sector is one name | ex-NEM EW 5-session excess positive on **any** close through 08-19 ⇒ A wrong | ex-NEM EW exc5 **−1.893**, **1 of 12 positive**; NEM exc5 **+7.096** | ★ **HIT (interim)** — anti-signal has not fired. `S77` settles 08-19 |
| **P54** (08-13) — Energy's price and narrative legs separated | (a) crude −5% & XLE exc5 >0 ⇒ B refuted · (b) crude holds & XLE exc5 <0 ⇒ A refuted | crude **+5.12% / 5d**, XLE exc5 **+3.774**; crack **+6.50 points**; `refinery` **1.61×**, the fastest non-CPI term | ★ **HIT on direction A** — neither anti-signal fired; the refining leg is now measured on the crack itself (P58). ⚠ **exc60 −4.519 unchanged** |
| **P52** (08-13) — the in-line print sent money to GROWTH, not defensives | `XLK` exc5 ≤0 at the 08-19 settle **while** `XLU` exc5 >0 ⇒ A refuted | `XLK` exc5 **+1.723** (and exc20 **+3.846 = best of 11**); `XLU` exc5 **+0.309** ⇒ the conjunction **cannot** fire on today's reading | **CARRIED, running in A's favour.** Settles 08-19 |
| **P55** (08-13) — the news instrument is intermittent and "quiet" was mis-measured | three probes ≥10 min apart all failing ⇒ A wrong | Probe 1 **22:34:57 SUCCEEDED (3,835 hits)** after 5/5 failures at 22:15 ⇒ **the anti-signal cannot fire** | ★ **HIT, and independently reproduced.** Re-registered as **P60** with the remedy attached |
| **P43** (08-10) — CXMT is an uncovered supply-side axis | an Apple/CXMT **filing**, MU revision breadth, whether it reaches HBM | ⚠ **No filing read** — but the axis is **refreshed on four foreign-scope articles** (§D-6): CXMT is now **China's most valuable company**, and **Apple is testing its DRAM after CXMT REFUSED to cut prices** | **REFRESHED after 5 runs, NOT resolved.** The filing leg is **still unread** and that remains this desk's omission, named again |
| **P-R2-1** (08-12 RUN-2) — July's benign headline is a window artifact; **August** headline y/y stops falling | August headline ≤3.3% **with** non-positive energy contribution | ⚠ **Now partially supported ahead of its settle**: July headline YoY is **+3.30%** and July MoM is **+0.074% off a June that FELL −0.42%** (§A-2) — i.e. the benign sequential number **is** a base artifact | **CARRIED — settles 2026-09** |

**Running hit-rate, propositions scored on a named KPI: 4 HIT (P51 · P53 · P54 · P55) · 0 HALF ·
0 MISS · 2 carried · 1 refreshed-unresolved.** ⚠ **S5/S1: three of the four HITs rest on ONE settled
session past registration.** They are recorded as tracked, not as validated.
⚠ **The honest counterweight**: yesterday's board carried **1 calibration MISS (P50, a 90%-mass branch
map whose modal branch did not fire)**. A run reporting 4/4 the day after a calibration failure should
be read as *"the KPIs were still running in the registered direction one session later"*, not as skill.

---

## §G · ★ Sector transmission matrix — all 11 GICS. **This is ROTATION's input.**

> Wind direction only. Sweep values are **3-axis** (`vel_coverage` 17.0%, velocity column revoked, §0)
> on **30-day-stale caps** (G5). ⚠ **G3 bars any `wflow`-based promotion/demotion for IT · HLTH · MATR.**

| # | Sector | Driving prop. | Wind | The one line |
|---|---|---|---|---|
| 1 | **Information Technology** | **P57-A** · P56-B | **OW-side wind** | Only sector positive on **all three** windows (exc5 +1.723 · exc20 **+3.846 best** · exc60 +4.101), and **NDX spec sits at the 0th percentile of a year**. ⚠⚠ **G3: `wflow +0.016` is `NVDA` alone — ex-top1 it is −0.078**, breadth 0.09 with **5🟢/10🔴 of 56**. *Cheap relief if oil keeps easing; the breadth does not support a broad call* |
| 2 | **Energy** | **P58** | **OW-side wind, 5-day only** | The board's **only positive `wflow` (+0.259)**, exc20 **+3.467**, crack **+6.50/5d**, WTI spec **18th %ile**. ⚠ **exc60 −4.519 and Δ −0.157 (2nd worst on the board)**. *The refiners are the expression; the integrateds are not* |
| 3 | **Health Care** | — (S82 open) | **neutral, unresolved** | **exc60 +10.239 = best of 11**, exc20 +0.449 — but **breadth 0.00**, **Δ −0.228 = worst on the board**, and **FINRA z +1.66 🔴 short surge**. ⚠ **G3 flipper (`LLY` 19.4%)**. *The 60-day leader and the 20-day laggard are the same sector — S82 (08-20) is the instrument* |
| 4 | **Financials** | **P56** | **neutral, steepener-levered** | exc60 **+7.290 (2nd best)** vs exc20 −0.957; `wflow −0.066` with `eqflow −0.144` (**breadth worse than the megacaps**); FINRA pressure **leaving** (z −0.26, −8.3▼). *A long-end steepener is a bank positive — but the 20-day says the market has not paid for it* |
| 5 | **Industrials** | P57-B | **neutral-to-UW wind** | exc20 −0.487 · exc60 +3.497; **0🟢 / 10🔴 of 50**. ⚠ **`D249`: the desk's live bracket measures `XLI` while the actual position is DEFENSE** (defense EW exc20 **+7.81** vs XLI **+0.89**). *The label and the position are different objects* |
| 6 | **Materials** | **P59** | **UW-side wind** | ex-NEM EW exc5 **−1.893, 1 of 12 positive**; NEM exc20 **+22.101**; **copper spec 100th %ile**. ⚠ **G3 flipper (`LIN` 24.7%)**. *One name, and the positioning is on the other side of the other eleven* |
| 7 | **Consumer Discretionary** | P57-A | **neutral** | exc20 −2.672, `wflow −0.416` (`AMZN` 40.2% of cap); **FINRA 🟢 the board's only short-covering signal (z −1.61, −9.3▼)**. *The only sector where pressure is actively leaving* |
| 8 | **Communication Services** | P56-A | **UW wind, but watch the tape** | exc60 **−9.098 = worst of 11**, `wflow −0.523` = worst, breadth 0.00 — **yet Δ +0.185 is the BEST on the board** and **FINRA z +2.15 / +12.4▲ is the steepest short surge**. *Maximum crowding against a sector whose flow just improved most — the two readings must be reconciled before any move* |
| 9 | **Consumer Staples** | P56-A | **UW− wind** | exc20 −3.396, `wflow −0.324`, breadth 0.00, FINRA +1.39/+8.4▲. ⚠ **`D249`: at 252 days STPL — not FIN — is the measured third leg of the duration complex.** *If P56-A is right this is a duration UW wearing a defensive label* |
| 10 | **Utilities** | **P56-A** | **UW wind, on a NEW mechanism** | exc20 **−6.763 = worst of 11**, `wflow −0.491`, **0🟢/9🔴 of 15**. ⚠ Two counterweights: **exc5 is +0.309 (positive)**, and the physical thread is live (*Romania shuts a nuclear plant; Danube dams dry; European heat wave* [8/8, 17/12]). *Pressured by the long end, not by the policy rate — the reason changed, the sign did not* |
| 11 | **Real Estate** | **P56-A** | **UW wind** | exc20 −4.366 (deteriorated from −2.499 through a cool CPI); `wflow −0.252`, breadth 0.00; **FINRA z −1.41, pressure leaving**. *The cleanest expression of P56-A: it got worse on the print that was supposed to help it* |

★ **The matrix's single organising claim**: **P56 (long-end term premium) and P57 (hike risk is an oil
function) are the two winds, and they point OPPOSITE ways for the same sectors.** A falling barrel
relieves UTIL/RE/IT through P57 and does nothing for them through P56. **ROTATION should treat any
UTIL/RE/STPL move this week as a test of which wind is real** — that is exactly what `S80` (08-19) was
registered to measure.

---

## §H · Catalysts injected at run start (`catalyst_calendar --days 5`, saved to `CATALYST_WATCH.json`)

| Type | Item | Axis | Note |
|---|---|---|---|
| 🔀 **BINARY** | **Iran "Strait of Hormuz open" statement (TACO trigger)** | oil | **undated** ⇒ **PREMORTEM (stage 7) MUST produce a both-sides bracket.** A one-way tilt into a known binary is a protocol violation |
| EARNINGS | **none in window** | — | ⚠ the calendar reports `yfinance unavailable` — this is **an instrument gap, not an empty calendar** |
| STRUCTURAL | **none in window** | — | `data/catalysts/structural_schedule.json` is human-maintained and was not updated |

⚠ **`S79`/`S81` name 2026-08-26 (NVDA) — beyond the 5-day window.** Per the L2's own D26 rule the
window was extended by reading `SCENARIOS.md` directly: the next settles are **08-19 (S75·S76·S77·S78·
S80) · 08-20 (S82·S83) · 08-24 (S74) · 08-26–27 (S79·S81)**. **No settle falls inside 08-14…08-18.**
⚠ **`D155`**: `action_bracket` returns a silent false negative on runs crossing local midnight. This
run started 22:10 KST and **may cross midnight before DRIFT** — flagged for stage 11.

---

## §I · New facts registered by this stage (`M653`–`M664`) and two new digs

| id | Fact | Source | asof |
|---|---|---|---|
| **M653** | 2s10s **+0.35 → +0.48** and 30y−10y **+0.48 → +0.56** over 11 sessions with `DGS2` **unchanged** | `[FRED]` | 2026-08-12 |
| **M654** | The long-end selloff carries **falling breakevens** (`T10YIE` 2.26 → **2.24**), **flat HY OAS (2.71 = 20-obs-ago)**, **loosening NFCI (−0.549)** and **`^VIX` 14.63 vs 18.77** | `[FRED]` + `[yfinance]` | 08-12/08-13 |
| **M655** | July CPI **MoM +0.074% / YoY +3.30%**; core **MoM +0.215% / YoY +2.47%** — and **June was −0.42% MoM**, so the benign sequential number is a base effect | `[FRED]` | 2026-07 |
| **M656** | `UNRATE` **4.3 → 4.3 → 4.2 → 4.1** Apr→Jul, three consecutive falls | `[FRED]` | 2026-07 |
| **M657** | `rate hike` **2.79× (152 vs 56)** vs `rate cut` **2 hits**, pool-normalised on 49,722/51,071 | client store, foreign scope | 08-07…08-13 |
| **M658** | ★ The hike-oil coupling **reproduced 3 weeks after M69**: *"Traders Pare Bets on Fed Rate Hike This Year as Oil Prices Fall"* [`bloomberg`] on a −2.43% crude session | `[news]` | 2026-08-13 |
| **M659** | `term premium` = **0 title hits in 49,722 articles** while the curve executes the largest structural move on the board | client store | 08-07…08-13 |
| **M660** | 3-2-1 crack **59.34 → 65.84 (+6.50 pts / 5 sessions)** with **HO +9.50% > CL +5.12%**; still below **69.45** twenty sessions back | `[yfinance]` settled | 2026-08-13 |
| **M661** | Materials ex-NEM EW **exc5 −1.893, 1 of 12 positive** vs **NEM +7.096**; copper spec **100th %ile** | own calc + COT | 2026-08-13 |
| **M662** | **UST-10Y spec 3rd %ile · NDX 0th %ile · WTI 18th %ile crowded short**; **copper 100th · USD 81st %ile crowded long** while `DTWEXBGS` fell 1.19% | CFTC COT | Tue close |
| **M663** | ★ **Apple is testing CXMT DRAM *after CXMT refused to cut prices*, amid an AI-driven shortage**; CXMT overtook Tencent as China's most valuable company 17 days post-IPO | `[news]` `yahoo_finance` · `nasdaq` · `semafor` · `tomshardware` | 08-11…08-13 |
| **M664** | 🚨 **D74 caught inside this stage**: a 22:33 pull returned a LIVE 08-14 bar; `XLE exc5` read **+5.936 live vs +3.774 pinned**, `NEM exc5` **+3.484 vs +7.096** | own measurement | 2026-08-14 |

**New digs**
- **`D259` (amended at `HANDOVER.md §10`)** — G1's single probe over-revokes; the availability window
  is **minutes**. Remedy: three probes ≥10 min apart before any revocation. **Human/idle_probe.**
- **`D260`** — `theme-age` returned **6/6 identical `🟡ACCELERATING`** with the highest acceleration on
  the term holding **14 articles**; its accel ratio tracks the corpus's **2.7× weekday/weekend
  denominator swing**, not the theme. Remedy: pool-normalise the accel denominator, as §D-3 does.
  ⚠ **Does not resurrect `R31`.**
- Carried: **`D243`** (no US IC ledger) · **`D249`** (S63's third leg / S64's XLI-vs-defense) ·
  **`D211`** (dig counter, human, 8th run) · **`D17`** (`drift` absent from `DB_READ_CMDS`, 9th run) ·
  🚨 **`S8` undated, 12th run.**

---

## ✅ EXIT CHECK

- [x] Catalysts injected (§H, `CATALYST_WATCH.json` written); **window extended past `--days 5` by
      reading `SCENARIOS.md`'s armed dates directly** (D26 rule).
- [x] Events read via `brief --body 2` — **tail count = 0**, head read **in full (91 events)**.
- [x] **`tail = 0` explicitly NOT used as the coverage claim** (§D-1): 604 body + 573 single-outlet
      withheld, **588 single-outlet events unscored because the classifier is Korean-only**, non-market
      band 0/0 for the same reason, **195 sub-events recovered**. ⇒ **no "quiet in bucket X" claim is
      made anywhere in this report.**
- [x] **Corrected denominator quoted**: 5,205 articles → 725 events → 725 market / 0 non-market.
- [x] Trajectories read (`thread --days 7`); **every proposition names its thread's curve or states
      "no thread" explicitly** (P56 has none, and says so). **No `FADING`/`ENDED` tag cited** — the
      window-end artifact is named instead.
- [x] Every "nothing happened" claim carries its denominator — **and the only such claim made is that
      no macro-relevant new blind-spot term emerged (§D-5), stated as a null result of a check run.**
- [x] **No bucket's low count is trusted from a quoted multi-word query**: `rate cut`'s 2 hits are
      reported with its own body-level counter-evidence (the hike articles), and the `Frontline` /
      `theme-age --days` query-form failures are documented at `HANDOVER.md §10` and §D-4.
- [x] **Both halves of every headline print** — §A-2 carries MoM **and** YoY **and** the negative June
      base for CPI; **PPI is explicitly NOT quoted as a primary number** (`[inferred-source]`).
- [x] **Every relative-performance number names `SPY` inline**; the KR-sourced CXMT articles are
      **excluded from the frame** rather than cross-market transferred (§D-6, W1).
- [x] **Credit axis read and cited**: HY OAS **2.71 flat**, IG **0.79 flat**, NFCI **−0.549**. ⇒ the
      report states **there is no credit confirmation in either direction** rather than asserting stress.
- [x] **`real_10y` quoted with `breakeven_10y`** (§A / §A-1) — and the decomposition is the load-bearing
      argument of P56.
- [x] Transmission matrix produced — **all 11 GICS, one line each** (§G).
- [x] `MACRO_REPORT.md` written; self-backtest hit-rate appended (§F); blind-spot terms folded back
      (§D-5 — **null result, stated**).
- [ ] **Linter** — run below (§J).

### 🚨 Failed lookups this stage, listed rather than absorbed
1. **`[FRED]` `VIXCLS` — HTTP 502 Bad Gateway, retried once, failed twice.** Substituted with `^VIX`
   **[yfinance]** and **tagged as a different provider (D5)**; no `[FRED]` claim is made on volatility.
2. **BLS PPI primary** — not re-pulled this stage; the 08-13 HTTP 403 stands. PPI remains
   **`[inferred-source]`** and is not used as a proposition anchor.
3. **`catalyst_calendar` earnings section** — `yfinance unavailable`; reported as an instrument gap.
4. **`module_news_data theme-age --days`** — operator error on this stage's part (the flag is
   `--window`); corrected and re-run. **Logged because a mis-passed CLI that returns nothing is the
   exact class this protocol calls a fabricated proposition.**

---

## §J · Linter run on this stage's own output

```
python -X utf8 scripts/report_lint.py llm_outputs/2026-08-14/industry_US/MACRO_REPORT.md
# REPORT_LINT — 1 file · rules C1,C2,S6,D6
  ✅ MACRO_REPORT.md
총 0건.
```
**0 findings, no exemptions claimed.** ⚠ The tool checks **form only** (C1 benchmark named · C2 both
halves · S6 future label · D6 OBV-alone). **A clean lint is not a correct report** — the substantive
weaknesses of this stage are stated in §F (three of four HITs rest on one settled session past
registration) and in the failed-lookup list.

## §K · P60's pre-registered probe test — result

| Probe | Clock (KST) | Result |
|---|---|---|
| PREFLIGHT G1 | 22:15 | ❌ **5/5 `URLError`** |
| **1** | **22:34:57** | ✅ **3,835 hits** |
| **2** | **22:44:59** | ✅ **3,835 hits** |
| **3** | **22:55:00** | ✅ **3,835 hits** |

⇒ **P55's anti-signal — "if three probes ≥10 minutes apart all fail, direction A is wrong" — CANNOT
fire.** **Three of three succeeded**, the full pre-registered test completed. **Direction A (a short availability window, not an outage) is confirmed
for a second consecutive run, now with timestamps on both the failure and the recovery.**
★ The identical count at **all three** probes (3,835) also rules out a partial/racing index as the cause — the
server's answer was **stable** the whole time the desk was calling it dead.

---

# §5 · DRIFT ADDENDUM — appended 2026-08-14 ~23:25 KST by stage 11 (L1·DRIFT)

> **APPEND-ONLY.** Nothing above is rewritten. The original calls stay visible beside their
> correction — that asymmetry is what the self-backtest eats.

## §5-0 · The tool failed again — `D17`, TENTH consecutive run

```
python -X utf8 scripts/drift_watch.py --report llm_outputs/2026-08-14/industry_US/MACRO_REPORT.md
drift 질의 실패 (rc=2): 'drift' 는 원격 실행 불가(조회 전용).
허용: ['blindspot','burst','chain-hop','coverage','export','fts','search','theme-age']
```
`drift` is **still absent from `__main__.DB_READ_CMDS`**, so it cannot run through the remote bridge.
Root cause unchanged; **human item (P6 — the allowlist is the server's single source).**

## §5-1 · 🚨🚨 The substitute check returned a FALSE ALL-CLEAR, and catching that is this section's main finding

Following `D255`, the substitute burst check was run **pool-normalised** against the client store:

| | Value |
|---|---|
| 08-14 articles in the client store | **487** |
| 7-day daily average (08-07…08-13) | **7,103.1** |
| **Pool ratio** | **0.069 — i.e. 6.9% of a normal day** |
| Terms returning **zero** 08-14 hits | `Hormuz` `Iran` `Strait` `OPEC` `oil` `refinery` `diesel` `rate hike` `Treasury` `yield` `copper` `gold` `tariff` `Microsoft` `memory` `tanker` |
| Only reading above 2× pool-normalised | `PPI` **2.21×** — on **5 raw articles** |

**Read naively this is "no drift". It is not — it is no data.** The client store's 08-14 row is a
**partial-day snapshot** (its mtime is 08:55 KST; this check ran at 23:2x). ⇒ **the check is broken in
BOTH directions at once**: with a 0.069 pool, a term averaging 46.7/day needs **~10 articles** to
register a 3× burst (under-powered), while a term averaging 4.7/day needs **~1** (over-sensitive).
**Registered `D264`**: *a pool-normalised burst check must also publish its pool ratio and refuse to
report an all-clear below a stated floor — `D255` made the ratio a divisor; it must also be a gate.*

## §5-2 · ★★★ And the tape DID drift — the live index found what the client store could not

Re-run through the **server FTS** (`fts search … --days 1 --scope foreign`, the path that was alive
from 22:34), every line **hand-cited with source and date**:

| Date | Source | Headline | Hits which proposition |
|---|---|---|---|
| **2026-08-14** | `aljazeera` | ★★★ ***"UAE accuses Iran of attacks on TWO ADNOC VESSELS in Strait of Hormuz"*** | **`S84` · P57 · P58** |
| **2026-08-14** | `bloomberg` | ★★ ***"Russian Regions Report NEW FUEL CRUNCH As Kyiv Hits Refineries"*** | **P58 direction A** |
| **2026-08-14** | `cnbc` | ★★ ***"Treasury yields RISE as U.S. threatens Iran with more economic sanctions"*** | **P56 · P57** |
| 2026-08-13 | `bloomberg` | *"Ukraine Says It Hit Oil Refinery in Russia's Urals Region"* | P58 |
| 2026-08-13 | `cnbc` | *"'Hormuz remains blocked': Iran disputes Trump claims as traffic sinks to near 3-month lows"* | `S84` |
| 2026-08-12 | `yahoo_finance` | *"Refinery Attacks Deepen **GLOBAL DIESEL** Supply Crunch"* | P58 |

### What it does to this run's calls — and it moves them, though not against them

1. **`P58` (Energy is refining margin, not war premium) — STRENGTHENED, and now with a second-order
   proof.** *"Russian Regions Report New Fuel Crunch"* is **the destroyed capacity showing up as a
   physical product shortage inside the producing country**, which is a strictly stronger observation
   than the strike reports the DEEP used. **The anti-signals are unchanged and neither fired.**
2. **`P57` (the hike premium is an oil function) — CONFIRMED IN THE OPPOSITE DIRECTION, 24 hours later.**
   On 08-13 the desk cited *"Traders Pare Bets on Fed Rate Hike **as Oil Prices Fall**"* [`bloomberg`].
   On 08-14 the tape prints *"**Treasury yields RISE** as U.S. threatens Iran with more economic
   sanctions"* [`cnbc`]. ⇒ **the coupling fired in both directions inside 48 hours on the same
   mechanism.** That is a far better test than either observation alone, and it was **not available
   when P57 was written.** ★ **This is the single most valuable line in the addendum.**
3. **`S84` — the live input lands on branch B (escalation), not branch A.** A **named-vessel attack**
   on 08-14 is the opposite of the reopening the bracket's against-us branch requires.
   🚫 **The band is NOT moved and the row is NOT re-dated.** It settles **2026-08-21** on its frozen
   text. Recording that the first post-registration news favours B is **tracking**, not scoring.
4. **`P56` (long-end term premium) — a competing explanation has appeared and it must be logged.**
   `cnbc` attributes the 08-14 yield rise to **Iran sanctions**, i.e. a **geopolitical/supply** driver,
   not the pure supply/term-premium residual §A-1 inferred. ⚠ **§A-1's `[inferred]` tag was already on
   that reading** and it now has a named alternative. **P56 is not withdrawn** — its KPI
   (`DGS30−DGS10`) is unchanged and its anti-signal has not fired — **but "the residual is term
   premium" is now one of two live explanations rather than the only one.** Stated here rather than
   quietly kept.

## §5-3 · What is NOT claimed

🚫 **No tilt is changed by this addendum**, and no bracket band is moved. The 08-14 tape is
**unsettled** (the US session is open as this is written) and **`D74` bars it from scoring anything.**
⚠ **`S71`'s anti-signal (a) is untouched** — both prints landed on schedule; nothing here re-opens it.
⚠ The 08-14 articles above are **narrative**, not price: this addendum makes **no** claim about what
`XLE`, `XLU` or the crack did on 08-14, because **that bar has not settled.**

## §5-4 · Drift verdict

**🚨 DRIFT DETECTED — three 08-14 items, all body-read rather than counted.** The direction is
**toward** this run's Energy and rate-coupling calls and **toward `S84` branch B**, with **one
competing explanation opened against `P56`'s inferred mechanism.**
★ **And the process finding outranks the market finding**: the desk's substitute drift check
**returned a clean all-clear on a 6.9%-of-a-day pool** while a named-vessel attack sat in the live
index. **An all-clear from an empty pool is the same failure class as PREFLIGHT G1's 17% coverage** —
`D264`.
