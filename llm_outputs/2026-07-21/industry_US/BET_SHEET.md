# BET_SHEET — industry_US · 2026-07-21 (Tue)

> Stage 7 / L1·BET. **ONE file, per-sector sections** (§A numbers · §B thesis+freshness · §C flow ·
> §D peers · §E refutation+dated catalyst). Downstream desks glob this exact filename — never split it.
> Candidate set per DEEP sector = **(deep-agent thesis leaders) ∪ (sector screener setups) ∪
> (LIVE_SHORTLIST names)** — the last drags in cross-sector names beyond the DEEP sectors, which get
> their own section (§X).
> **Prices/flow asof the 2026-07-20 close. Fundamentals pulled live 2026-07-21** (`module_fundamentals_us
> --json`, XBRL/yfinance). **Sizing language is illustration only — ZERO buy/sell recommendation.**

## ⚠ Data-quality flags recorded BEFORE any table is read (blanks are blanks, not guesses)
1. **`module_fundamentals_us` does not expose ROE, operating margin, revenue growth or debt/equity.**
   Its key set is price/mcap/PE/forward PE/PEG/PS/PB/EPS/52w/beta/targets/next_earnings/quarterly_revenue.
   **Those four columns are therefore absent from §A everywhere — not estimated, not filled from memory.**
2. **HPE's `next_earnings_date` returns 2026-06-02 — a date in the past.** The field is stale for that
   name; its "+50.4% to target" is computed off a target of the same vintage. **HPE's §A is flagged
   unreliable rather than used.**
3. **TRI shows a 52-week high of 209.90 against a 95.43 price (−54.5%).** That is almost certainly a
   split/adjustment artifact, not a drawdown. **Flagged suspect; not used in any judgement.**
4. **PGR's PEG reads 31.72** — a degenerate ratio (near-zero growth denominator). **Shown, marked, not used.**
5. ★ **Two dated catalysts this run's earlier stages never found, surfaced here by `next_earnings_date`:
   CB prints 2026-07-22 (tomorrow) and T prints 2026-07-22.** CB is the FIN insurance leg's own test —
   **the leg DEEP·FIN just relocated its verdict onto — and no upstream stage flagged it.** Added below
   and handed to ALPHA. *(This is the third calendar gap found in one run: AMD's 07-22 event by
   PREMORTEM, GOOGL/INTC by the 07-19 DRIFT, CB/T here.)*

---

# §0 ★ EPICENTER-STARTER MODULE — required on the sheet regardless of tape

**The GAP (from `CYCLE_EXPOSURE.md`, 4th consecutive flag):** rank-2 cycle *"Energy / oil-refining
(Hormuz + Russia crack)"* — **epicenter exposure 0.0% vs 8.0% required, margin −8.00pp.** The book
holds only KMI and LNG — **adjacent/fuel, beta to the consequence, none to the engine.**

**The governing rule, unchanged and applied literally: a 🔴/crowded tape gates the ADD *timing*; it
never justifies a 0% core in a rank≤2 cycle. A partial core therefore exists on this sheet regardless
of the tape — and the tape gates only the remainder.**

⚠ **Two independent gates argue for caution on ENTRY TIMING — and neither changes which name is
cleanest** (DEEP·ENRG §6 Q1 kept these strictly separate, and so does this sheet):
- **Gate 1 — the live 10-day Iran ceasefire proposal** (undated, rejected so far).
- ★ **Gate 2 — NEW and more damaging, from DEEP·ENRG §0 D1: the prior run's OWN falsifier fired.**
  Self-computed distillate crack (`HO=F×42 − CL=F`, one continuous pull): **90.34 → 88.22 → 85.31**
  across 07-16/17/20 — **down two consecutive sessions while VLO, PBF, MPC and PSX rose on both.**
  The 07-19 file pre-committed: *"2 consecutive sessions where the crack falls and PBF/VLO still rise →
  Day 2 → treat as narrative-priced."* **Day 2 fired.**
- ★★ **And DEEP·ENRG separated a conflation the earlier stages made:** MACRO and EVENT_ALPHA both
  celebrated *"VLO +1.18% on the day crude fell −0.35% — the decoupling test passed."* On 07-20
  **product fell MORE than crude** (`HO=F` −1.83% vs `CL=F` −0.27%). **The refiners did not decouple
  from crude; they decoupled from their own margin.** *"Anti-fragile to a crude selloff"* and *"rising
  while the margin shrinks"* are **not the same sentence**, and only the second one is what happened.

**Consequence for this sheet: the epicenter core is placed on the CLEANEST name, not the strongest
runner.** The strongest runners are precisely the ones the falsifier caught.

---

# §1 ENERGY (ENRG) — OW #1
*Sources: `SECTOR_DEEP_ENRG.md` §1/§6, `EVENT_ALPHA.md` CARD 1, `BLINDSPOT_PREMORTEM.md` Lens 3/Lens 4.*

## §A Numbers [`module_fundamentals_us --json`, pulled 2026-07-21]
| Ticker | Price | Mcap $B | Trail PE | Fwd PE | PEG | P/S | P/B | Div % | 52wL–52wH | % off high | Beta | Next ER | Tgt median | vs price |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **XOM** | 148.36 | **614.9** | 24.81 | **13.92** | 1.25 | 1.89 | 2.42 | **2.80** | 105.53–176.41 | **−15.9%** | **0.16** | 2026-07-31 | 168.00 | ★ **+13.2%** |
| **DINO** | 90.41 | 16.3 | **13.30** | **10.65** | 1.33 | **0.59** | 1.70 | 2.26 | 42.16–91.45 | **−1.1%** | 0.71 | 2026-07-28 | 80.00 | ⚠ **−11.5%** |
| VLO | 313.31 | 93.0 | 22.89 | 13.73 | ⚠ **4.08** | 0.79 | 3.90 | 1.55 | 130.78–316.57 | **−1.0%** | 0.55 | 2026-07-30 | 287.50 | ⚠ **−8.2%** |
| MPC | 315.31 | 92.1 | 20.58 | 11.72 | 1.55 | 0.68 | **5.51** | 1.25 | 158.00–319.36 | **−1.3%** | 0.52 | 2026-08-04 | 300.00 | ⚠ −4.9% |
| PSX | 208.80 | 83.7 | 20.45 | **11.39** | **1.20** | 0.62 | 2.93 | 2.46 | 118.07–211.04 | **−1.1%** | 0.68 | 2026-08-05 | 203.00 | ⚠ −2.8% |

★★ **The single most important line in this section, and it is arithmetic, not opinion: FOUR of the
five refiners trade ABOVE the sell-side median target, and all four sit within 1.3% of their 52-week
high.** DINO −11.5%, VLO −8.2%, MPC −4.9%, PSX −2.8%. **XOM is the only name in the complex with
positive implied upside (+13.2%) and the only one meaningfully off its high (−15.9%).**
*(Targets are consensus, a lagging and herding input — cited as a crowding measure, not a valuation view.)*

## §B Thesis + freshness — ★ **ALPHA-FILLED 2026-07-21**
> **Bab el-Mandeb leg 🟢 LIVE** — `theme-age` **🟡ACCELERATING, ★188.57× acceleration, 61 hits** (the
> largest acceleration measured anywhere in this run). **Crack leg 🟡 PARTIAL** — `refining margin`
> **4.76×**, `crack spread` **12.86×** acceleration, i.e. **attention up while the actual crack fell two
> sessions**; residual = the mechanism, not the margin. **Ceasefire anti-branch ⚪ECHO** (≥90d,
> 31.4% share, only 1.87× accel, 1,762 hits — loud but consumed; ECHO ≠ resolved, the binary is live).
> **Positioning:** DINO ⚡ shorts **5.2% float BUILDING** into an accumulating tape = squeeze fuel,
> **turn-conditional, HARD STOP REQUIRED** · XOM shorts **1.0% covering**, P/C 0.43, skew **−4.9** =
> complacent, little squeeze fuel — **a structural expression, not a momentum one.**

- **P3′ — the durable ENRG leg is refining, not the crude premium.** Mechanism: physical conversion
  capacity destroyed (**"at least 24 of Russia's 34 largest refineries" damaged; "over 40% of Russia's
  refining capacity" disabled**) + two independent chokepoints (Hormuz **and** Bab el-Mandeb).
- ⚠ **Freshness caveat that must travel with the thesis: the MECHANISM is intact and the KPI is not.**
  `refining margin` 30→**76** hits/7d and `crack spread` 14→**32** — attention doubled — while the
  **actual crack fell two straight sessions.** *Attention up, margin down, price up* is the narrative-
  priced signature, not the confirmation it looks like at first glance.
- Freshness tag: `[ALPHA fills]`

## §C Flow / positioning cross-read [07-20 close; FINRA z 07-20]
| Ticker | OBV | RS20 | RS60 | Vol surge | FINRA z / 5v5 | Read |
|---|---|---|---|---|---|---|
| **XOM** | **매집** | +8.3% | −5.1% | 0.83× | **−0.77** / +2.2▲ | ★ **No crowding in either direction — the un-crowded layer.** Not headline-named anywhere in this run |
| **DINO** | 🟢가속 | **+40.8%** | — | ★ **1.29×** | — | ★ **The ONLY name in the whole complex with an active-ignition tag AND real volume** |
| VLO | 매집 | **+33.2%** | +29.3% | 1.06× | +0.31 / −5.7▼ | Strongest RS; volume not confirming fresh buying |
| MPC | 매집 | +30.4% | +37.6% | **0.86×** | −0.94 / +2.4▲ | ⚠ RSI **86.4** — most extended, thinnest volume |
| **PSX** | 매집 | +26.3% | +25.6% | 0.96× | ★★ **+2.01 🔴 극단** / −8.7▼ | ★★ **Short-vol z REVERSED SIGN vs the registry's locked rationale (−1.43)** |
| CVI *(small-cap)* | — | — | — | — | ★ **−2.20 🟢 sharp cover** | ★ Two refiners, **opposite** positioning signals, same week |

## §D Competition / peers
Refining is a spread business, not a share business — peers compete for **crude slate and conversion
complexity**, not customers. **Bottleneck = conversion capacity** (carried by reference from
07-17/07-19 §4; strong demand is *not* a bottleneck). Small-cap independents kept accelerating past
the majors: **PBF RS20 +65.8%→+71.8% · DK +49.1%→+56.5% · PARR +49.6%→+53.0% · DINO +34.1%→+40.8%**.
**XOM/CVX/EOG are `counter_sign` to the crack, not peers to it** — they are integrated, so a widening
crack helps their downstream and a falling crude hurts their upstream.

## §E Refutation + dated catalyst
- **Kill (mechanism):** Russian/Ukrainian refining capacity comes back online (Afipsky, Syzran), or a
  lifted diesel export ban. **NOT a Hormuz headline** — that is the wrong kill-switch for this leg.
- **Kill (already firing, this is the live one):** ★ **crack detachment Day 2 fired.** Escalation
  observable: **a third consecutive session of crack down with refiners up** → the leg is priced on
  narrative, and the sheet's own §0 gate tightens further.
- **Kill (positioning):** PSX **OBV flips to 분산 while z stays >+2.0** → PSX's own kill condition.
- **Dated catalysts:** **DINO 07-28 · VLO 07-30 · XOM 07-31 · MPC 08-04 · PSX 08-05.** Undated but
  live: the 10-day Iran ceasefire; Bab el-Mandeb enforcement (declared, **not yet observed as an
  actual tanker turned away** — that is the specific observable PREMORTEM B1 named).
- ★ **Registry defect handed to a human, not overridden:** the human-locked `core_pick: PSX` rationale
  reads *"the only Energy name with shorts actively exiting (z −1.43)"*. **Measured today: z +2.01.**
  The valuation leg (fwd 11.39, PEG 1.20 — cheapest large refiner, confirmed in §A) and the
  non-crack-segment leg are **untouched**; only the stated positioning premise reversed. **Re-verify
  before treating the lock as current.**

---

# §2 HEALTH CARE (HLTH) — OW #2 (hedge role)
*Sources: `SECTOR_DEEP_HLTH.md` §6-Q1/§6-Q2, `BLINDSPOT_PREMORTEM.md` FINDING 0.*

## §A Numbers
| Ticker | Price | Mcap $B | Trail PE | Fwd PE | PEG | P/S | P/B | Div % | % off 52wH | Beta | Next ER | Tgt median | vs price |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **ABT** | 101.66 | 177.1 | 28.16 | 16.76 | 1.50 | 3.80 | 3.40 | 2.50 | ★ **−26.1%** | 0.61 | 2026-10-14 | 119.00 | ★ **+17.1%** |
| **UNH** | 421.55 | **382.8** | 32.06 | 18.85 | 1.42 | 0.85 | 3.91 | 2.18 | −8.7% | 0.63 | **2026-07-16 (passed)** | 479.00 | +13.6% |
| CVS | 107.61 | 137.3 | 47.20 | **12.79** | ★ **0.30** | **0.34** | 1.77 | 2.48 | **−1.2%** | 0.60 | 2026-08-05 | 111.00 | +3.2% |
| **HUM** | 398.20 | 47.8 | 42.73 | 24.84 | 2.27 | 0.35 | 2.57 | 0.89 | −7.2% | 0.72 | **2026-07-29** | 342.00 | ⚠ **−14.1%** |

## §B Thesis + freshness — ★ **ALPHA-FILLED 2026-07-21**
> **🟡 PARTIAL.** `theme-age "managed care"` = **🟡ACCELERATING, 55d, 2.86× accel, 37 hits** — a real
> but modest denominator; the sector still has **zero multi-day threads in five runs**.
> **Positioning (HUM):** ⚠⚠ **two instruments disagree — FINRA daily short-vol z +1.97 (극단) against
> settlement short interest of 4.1% float COVERING, DTC 2.8**, with options **P/C 1.13, skew +13.5
> (hedge/fear)**. **Recorded unresolved rather than picking the convenient one. HARD STOP REQUIRED**;
> HUM prints 07-29. **Residual for the whole sector: it is tagged PARTIAL, not LIVE, because the
> correlation constraint below means the position is a sleeve, not a sector.**

- **P7 — HLTH as a rotation destination is FALSIFIED; HLTH as a hedge is CONFIRMED.** DEEP·HLTH
  recomputed **XLV's beta to SPY at −0.86 over 20 days** (vs −0.17 at 60d) — **the hedge behavior is
  intensifying in the freshest data, not fading.** Live confirmation: XLV was the **worst** sector
  (−1.14%) on the +$550B risk-on day while its own flow tag stayed 매집.
- ★ **Five runs, zero multi-day news threads.** Sustained accumulation with no story is what a
  **portfolio-construction** trade looks like from outside — a destination generates coverage.
- **DEEP's named split:** **HEDGE = XLV, WELL, VTR, and now UNH** (reclassified) · **DESTINATION =
  ABT** (clean; CONFIRMED-TURN on the chart tool) · **CVS** (confirmed but at its exact YTD high) ·
  **HUM** (the cycle's real vehicle — but no longer clean).

## §C Flow / positioning cross-read
| Ticker | OBV | RS20 | Vol | FINRA z | Read |
|---|---|---|---|---|---|
| **HUM** | — | — | — | ★★ **+1.97 극단** *(was −0.60 on 07-19)* | ★★ **The largest single measured change in the whole run.** 07-19's diversifier case rested on HUM being orthogonal **AND** uncrowded. **The uncrowded leg broke in two sessions** |
| **UNH** | 매집 *(module_flow)* | +5.8% | 1.20× | +0.83 | ⚠ **Two methods disagree: `module_chart` reads OBV 분배, −19%/20d, bearish divergence, PULLBACK-not-CONFIRMED-TURN.** Reported unresolved, not smoothed |
| ABT | 매집 | +15.6% | — | +0.70 | CONFIRMED-TURN; a broken-name rebound, unrelated to the MLR cycle |
| CVS | — | — | — | +1.34 | CONFIRMED-TURN but at its YTD high with elevated short — a destination already being fought over |
| WELL | 매집 | **+19.1%** | — | **+1.34** *(was +0.08)* | ⚠ **Crowding is now building on the hedge leg too** |

## §D Competition / peers — screener additions (raw candidates, flow-vetted here before use)
`us_setup_screener --sector "Health Care"` returned **8 new names**. **Flow-checked before promotion —
and most fail:**
| Ticker | Screener basket | RSI | Flow | OBV | RS20 | RS60 | Vol | Verdict |
|---|---|---|---|---|---|---|---|---|
| **MRK** | leader pullback | 42.3 | 🟡 | **매집** | **+9.9%** | +5.9% | 1.01× | ★ **The only screener name with accumulation AND positive RS on both horizons** |
| **LLY** | leader pullback | 33.6 | 🟡 | **매집** | +5.0% | **+20.1%** | 0.81× | ★ Accumulating, deeply oversold RSI |
| EW | leader pullback | 33.3 | 🟡 | 중립 | −2.1% | −0.1% | 1.12× | No flow — drop |
| WAT | leader pullback | 41.0 | 🟡 | 중립 | +1.2% | +2.6% | 0.67× | No flow — drop |
| BSX | de-rate snapback | 51.4 | 🔴 | 분산 | −2.7% | **−36.9%** | 0.77× | Distributing — drop |
| **ISRG** | de-rate snapback | 35.7 | 🟡 | 중립 | **−12.6%** | **−31.3%** | ★ **2.27×** | ⚠ **The 07-17 DRIFT built part of the HLTH case on ISRG. It is now 2.27× volume, RS60 −31.3%, OBV neutral — that leg is dead, confirmed a second time** |
| ALNY | de-rate snapback | 39.5 | 🟡 | 분산 | −1.3% | −16.5% | 1.01× | Distributing — drop |
| HCA | de-rate snapback | 41.7 | 🟡 | 중립 | −0.6% | −25.8% | 1.29× | No flow — drop |
**6 of 8 screener names dropped on flow. MRK and LLY carried forward as fresh, un-crowded candidates.**

## §E Refutation + dated catalyst
- ★★ **BINDING CONSTRAINT (PREMORTEM FINDING 0, re-verified and WORSE):** XLV·XLRE·XLU·XLP are one
  duration sleeve. **90d pairwise ≈0.57–0.66; the 20d window reads 0.67–0.80** (XLV–XLRE **0.801**).
  **HLTH may not be counted as diversification against RE/UTIL/STPL.** **Shared kill-switch:
  real 10Y > 2.50% (now 2.31%) or 2s10s < +30bp (now +37bp — 7bp away).** One number invalidates the
  whole sleeve, and this sheet flags it as a **concentration** item, not four positions.
- ★ **HUM's correlation leg survives, its crowding leg does not.** DEEP computed **HUM as the only one
  of 11 HLTH names with NEGATIVE correlation to XLRE (−0.13/−0.33)** — genuinely the sleeve-breaker —
  **but z +1.97 means "quiet, uncrowded accumulation" is a dead description.** Any downstream stage
  citing 07-19's *"shorts have simply abandoned it"* is citing a dead number.
- **Kill:** XLV OBV flips to 분산, **or** XLV *outperforms* on an up day (which would restore the
  destination read and falsify the hedge read — stated both ways on purpose).
- **Dated catalysts: HUM 2026-07-29 · CVS 2026-08-05 · ABT 2026-10-14.** ⚠ **UNH's print (07-16) has
  already passed** — its flow is post-event, not pre-event.

---

# §3 FINANCIALS (FIN) — OW #3, on flow only
*Sources: `SECTOR_DEEP_FIN.md` §0/§2/§3/§4.*

## §A Numbers
| Ticker | Price | Mcap $B | Trail PE | Fwd PE | PEG | P/S | P/B | Div % | % off 52wH | Beta | Next ER | Tgt median | vs price |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **SCHW** | 102.54 | 178.3 | 20.39 | 13.63 | 1.21 | 7.19 | 4.20 | 1.26 | −4.6% | 0.76 | ★ **2026-07-21 (TODAY)** | 122.00 | ★ **+19.0%** |
| **CB** | 352.53 | 136.7 | **12.45** | 12.07 | 3.10 | 2.24 | 1.86 | 1.16 | −3.5% | **0.41** | ★★ **2026-07-22 (TOMORROW)** | 373.00 | +5.8% |
| PGR | 212.23 | 123.4 | **10.44** | 13.07 | ⚠ 31.72 | 1.36 | 3.59 | ★ **6.68** | −16.7% | **0.25** | 2026-10-14 | 230.00 | +8.4% |
| TRV | 368.50 | 78.4 | **9.91** | 12.54 | 2.36 | 1.60 | 2.32 | 1.36 | −0.9% | 0.47 | 2026-10-15 | 340.00 | ⚠ −7.7% |
| STT | 182.58 | 50.2 | 16.10 | 12.02 | **0.94** | 3.34 | 2.10 | 2.02 | −5.2% | **1.43** | 2026-10-16 | 197.00 | +7.9% |
| **PYPL** | **56.82** | 50.1 | **10.62** | **9.88** | 1.02 | 1.49 | 2.53 | 0.99 | ★ **−28.5%** | 1.33 | 2026-07-28 | ⚠ **48.00** | ⚠ **−15.5%** |

## §B Thesis + freshness — ★ **ALPHA-FILLED 2026-07-21**
> **🟡 PARTIAL, and the gate nearly demoted it further.** ★ `theme-age "insurance earnings"` =
> **🔴 FADING — 0.0× acceleration, ONE hit in 28 days.** **The sub-leg DEEP·FIN just relocated the
> whole verdict onto has essentially NO news denominator** — it is a flow-only phenomenon, and
> DEEP·FIN's own reinsurance-pricing KPI is **unrefreshed for 5 days**. It survives as PARTIAL rather
> than RESOLVED only because **CB's flow is genuinely 🟢가속/매집 on 1.20× volume and it prints
> tomorrow** — i.e. the residual is a dated test, not a hope. **Bank leg: 🔴 RESOLVED and DROPPED** —
> zero green banks, 2s10s +42→+41→**+37bp**; **logged with the reason so "banks are cheap" cannot
> resurface next run.** **Positioning:** CB shorts 1.2% building, DTC 2.7 — **HARD STOP REQUIRED into
> a binary.** STT ⚡crowded-short (z +1.50) = **turn-conditional, never a standalone buy.**

- **The verdict RELOCATED, it did not overturn.** DEEP·FIN: LATE MONEY is now *"late on **banks**,
  unresolved on **insurance**, plus a special situation (PYPL) and a squeeze setup (STT) that say
  nothing about the sector either way."*
- **The decomposition of XLF's 1.10× surge — the only volume surge on the sector board — is the point:
  5 green names = 3 insurance (TRV/CB/PGR) + 1 crowded-short custody (STT) + 1 M&A arb (PYPL).
  ZERO green banks.** No component of that is *"a hike regime helps banks."*
- **The curve got 6bp deader** (2s10s +41→+37bp). **Nothing revives the original macro driver.**

## §C Flow / positioning cross-read
| Ticker | OBV | RS20 (Δ vs 07-19) | RS60 (Δ) | Vol | FINRA z | Read |
|---|---|---|---|---|---|---|
| **CB** | 매집 | 7.1%→**9.6%** | 1.4%→**4.0%** | — | — | ★ **Genuine second leg (+2.5pp/+2.6pp) — not a spent earnings gap** |
| **PGR** | 매집 | 1.4%→**4.2%** | −5.4%→**+0.4%** | — | — | ★ **+2.8pp/+5.8pp — the short-cover bounce is becoming an actual move** |
| TRV | 매집 | 20.2%→**20.3%** | — | — | +0.26 | ⚠ **Flat — no second leg. 07-19's "catalyst-spent" finding now applies to THIS name only** |
| SCHW | 매집 | 7.1%→**12.4%** | 4.9%→**7.5%** | **0.85×** | **+0.07** | ★ Strongest reading in the complex — **and still sub-1.0× volume: nobody is positioned ahead of a same-day binary** |
| **GS** | — | — | — | — | ★ **+1.59 🔴** | ★ **The narrative-vs-money gap MOVED names**: JPM's +1.68 resolved to +0.45; GS is now the crowded short, against its own record-revenue headline |
| JPM | 매집 | +4.8% | +3.9% | 1.07× | +0.45 정상 | Divergence resolved; RS still tepid |
| STT | +0.14 | +9.1% | — | — | **+1.50 ⚡** | Squeeze-conditional. **Not a buy on its own** |

## §D Competition / peers — screener additions
`us_setup_screener --sector Financials` → **2 names: C (RSI 28.4, leader pullback, +41% off its 52w
low) and BRK-B (RSI 45.0).** Both are **banks/conglomerate** — i.e. **the sub-leg DEEP just found has
zero green names.** **Logged, not promoted:** a screener setup inside a sub-leg with no flow is a
chart pattern, not a candidate.

## §E Refutation + dated catalyst
- ★ **PYPL — resolved from primary sources, and the resolution kills the "the desk is wrong to avoid
  it" framing rather than confirming it.** PREMORTEM Lens 3 called PYPL *"the name the desk is most
  wrong to avoid"* on a chart CONFIRMED-TURN + OBV +42%/20d + z −1.55. **DEEP·FIN then found the
  cause: a reported Stripe + Advent $53B (~$60.50/share) bid that PayPal's board called
  "inadequate"** (Reuters 07-17), with PayPal cast as an *"unwilling merger target"*.
  **The arithmetic makes the structure unmistakable: price 56.82 · reported bid 60.50 (a +6.48%
  spread) · sell-side median target 48.00 (−15.5% BELOW the market).** ★ **This is a merger-arbitrage
  payoff, not a payments-sector signal — the flow score that topped the entire 300-name sweep is deal
  spread, not accumulation.** ⚠ **Anti-signal from PYPL's own 10-K: TPV +7% YoY but transaction count
  −4% YoY.** **Carried out of the FIN thesis and logged as an orphan special situation.**
- ★★ **CB prints 2026-07-22 — TOMORROW — and no upstream stage flagged it.** It is the dated test of
  the exact sub-leg DEEP·FIN relocated the verdict onto. **Handed to ALPHA.**
- **SCHW status: PENDING, verified not assumed.** `fts search SCHW Schwab --days 1` → 40 matches,
  **all previews, zero results.** New pre-print fact: **BMO downgraded SCHW to Market Perform on
  07-20**, one session before the binary.
- ★ **Pre-commitment adopted (PREMORTEM B2), stated so it cannot be walked back: a clean SCHW print is
  NAME-LEVEL NOISE, not sector confirmation.** The steepener is dead regardless of what SCHW reports.
  **Reading a good SCHW number as validating the FIN OW would be the MU-reclaim error in reverse.**
- **Kill:** the insurance second leg stalls (CB/PGR RS20 flat next read) · a credit-cost surprise —
  the stack is **NY Fed record credit-application rate [7a/5s], student-loan defaults, Dimon
  "wouldn't buy stocks or Treasurys", "$1.5T leverage peaking", W.R. Berkley revenue miss.**
  ⚠ **The insurance leg's own bottleneck KPI (reinsurance-pricing softening) is UNREFRESHED — no
  confirming or falsifying item in 5 days. Recorded rather than silently dropped.**

---

# §4 SEMICONDUCTORS / AI-HARDWARE (SEMI) — promoted leg, verdict UNRESOLVED
*Sources: `SECTOR_DEEP_SEMI.md` §0/§1/§6/§7.*

## §A Numbers
| Ticker | Price | Mcap $B | Trail PE | Fwd PE | PEG | P/S | P/B | % off 52wH | Beta | Next ER | Tgt median | vs price |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AMD** | 503.57 | **821.1** | ⚠ **164.03** | 37.40 | **1.16** | ⚠ **21.92** | 12.73 | −13.9% | ★ **2.47** | 2026-08-05 | 540.00 | +7.2% |
| **ANET** | 169.35 | 213.2 | 57.80 | 37.91 | 2.15 | 21.96 | 15.81 | −10.8% | 1.60 | 2026-08-05 | 190.00 | +12.2% |
| HPE | 44.56 | 59.0 | 41.64 | **11.14** | **0.85** | 1.52 | 2.33 | −30.6% | 1.44 | ⚠ **2026-06-02 (STALE)** | ⚠ 67.00 | ⚠ +50.4% (stale) |

⚠ **AMD's beta is 2.47 — by far the highest on this sheet.** Any illustration of influence must
account for the fact that one unit of AMD carries roughly **5–15× the index sensitivity** of the
insurance and refining names above (CB 0.41, PGR 0.25, XOM 0.16).

## §B Thesis + freshness — ★ **ALPHA-FILLED 2026-07-21**
> **🟡 PARTIAL — and the freshness gate materially qualifies PREMORTEM's "missed catalyst" framing.**
> `theme-age "Helios"` = **🟡ACCELERATING, 6.43× accel, 107 hits** — the deal narrative is real and
> young. **But `theme-age "Advancing AI"` = ⚪ECHO (79d, 16.3% share, 610 hits, only 1.88× accel).**
> ★ **The EVENT DATE was a genuine calendar gap; the THEME is already consumed.** Per the L1 rule an
> ECHO thesis needs *stronger* live evidence to survive — and here the live evidence is **absent**:
> **AMD's own OBV is distributing at −58%/20d.** **Residual, stated as one observable: AMD's OBV must
> turn 매집.** **Positioning:** AMD shorts 2.6% covering, DTC 1.3, options **P/C 1.03 with skew
> ★+43.1 — the steepest downside skew on the entire sheet**; the options market is paying up hard for
> protection into 07-22. ⚠ **MOMENTUM-ONLY STAMP: RS60 +61.6% with OBV not confirming = tape trade —
> HARD STOP REQUIRED.**

- ★ **MU's kill-line reclaim is a NAME event, not a SECTOR event — four independent methods agree.**
  Chart (`module_chart MU --read`): the reclaim cleared only the **STOP (848.95)**; the chart's own
  **ignition trigger — close >872.42 with OBV flipping to accumulation — has NOT fired.** OBV **분배
  −57%/20d**, RSI 24.5, turn-verdict **NEUTRAL/CHOP**, 1 of 4 MAs above, reclaim-day volume **0.86×**.
  Plus the universe sweep (**0 green/56, eqflow −0.334**) and EVENT_ALPHA CARD 8 (all names distributing).
- ★★ **DEEP·SEMI's sharpest new finding: AMD's own OBV is distributing at −58%/20d — almost identical
  to MU's −57% — despite the bullish Helios headline. The rally moved PRICE, not MONEY,** on a
  genuinely clean short tape (z +0.01).
- ★ **IR anchor from EDGAR primary (accession 0000002488-26-000021): AMD's Helios rack platform was
  previewed BEFORE the Microsoft deal.** So the 07-20 announcement is a **monetization proof point on
  an existing engineering bet, not a new product** — materially less of a surprise than the headline reads.
- **Honest state: a live, dated, UNCONFIRMED hypothesis with two falsification windows 24–48h away.
  "Unresolved" is the correct answer, not "bullish" or "bearish."**

## §C Flow / positioning cross-read [every epicenter name is red]
NVDA 🔴분산 RS20 −2.9% (z **−1.39** covering) · **AMD 🟡중립** RS20 −5.7%/**RS60 +61.6%**, z **+0.01** ·
AVGO 🔴분산 −7.4%/**−14.9%**, **no live narrative at all** · MU 🔴분산 −23.1% vol 0.86× ·
**TSM 🔴분산 −12.3% on 1.24× volume — distribution on REAL volume, the cleanest bear signal** ·
AMAT/LRCX/KLAC all 🔴 · MRVL **−36.6%** · INTC −26.9% (z −0.81, **no crowding to unwind on a beat**) ·
**ANET 🟡중립 but OBV 매집 — the single accumulating name in the entire node map** ·
HPE 🟡중립 RS20 −5.4%/**RS60 +52.0%**, not headline-named · VRT 🔴분산 −11.8% ·
**SMH 🔴분산 RS20 −14.7% on 1.04× — deepened even as MU bounced.**

## §D Competition / peers — ★ the chain-hop finding nobody else produced
EVENT_ALPHA found **no un-crowded hop left in AI-compute within us_top300**. DEEP·SEMI widened past
that boundary and found two: **CDNS and SNPS (the EDA / design-tool layer)** — genuinely un-crowded and
body-proximate. ★ **But they point the WRONG way: CDNS RS20 −14.2%/RS60 −4.8%, SNPS −16.3%/RS60 −25.0%,
both distributing. The design-tool layer is the ONLY node where even the medium-term trend has
broken** — and design tools lead silicon by quarters. **A bearish leading indicator, surfaced only
because the widened search was run. Logged as a candidate for the SHORT side of the ledger, which this
desk does not express — so it is carried as a KPI, not a name.**

## §E Refutation + dated catalyst
- ★ **Bifurcation verdict (testing PREMORTEM Lens 4's claim rather than accepting it): CORRECT as a
  definitional fix, NOT YET CONFIRMED as a flow divergence.** The two sides are **not symmetric**:
  IBM's −26.6%/5d on **2.44× volume** is a confirmed distribution event; MU's +1.94% on **0.86×** is
  not confirmed by turnover. **Software has a confirmed sell signal; hardware has an unconfirmed,
  price-only buy signal.** At the breadth level **both legs are red.** The registry should **split the
  tracking, not conclude the hardware leg has turned.**
- **Bull-branch KPIs (pre-committed, unchanged, deliberately made harder rather than softer):**
  ① **MU >872.42 with OBV→누적, held ≥3 sessions** (not the 848.95 stop that already fired) ·
  ② **SMH RS20 > −8%** (now −14.7%, *deepened*) · ③ **two of {MU, TSM, AVGO} flip OBV to 매집**
  (currently **zero of three**) · ④ **AMD's 07-22 event delivers a guidance raise or a new named
  hyperscaler beyond Microsoft AND AMD's OBV turns 매집** — *the event must move money, not just price* ·
  ⑤ **GOOGL 07-22 or INTC 07-23 print a capex beat that is rewarded ON THE CAPEX LINE.**
- **Dated catalysts: AMD "Advancing AI" 07-22 (two days) · GOOGL 07-22 · INTC 07-23 · AMD ER 08-05 ·
  ANET ER 08-05.**
- **Kill:** breadth stays **0 green/56** through the 07-23 prints → IT returns to a clean UW and MU's
  reclaim books as relief-day beta.

---

# §X CROSS-SECTOR LIVE_SHORTLIST names (outside the DEEP sectors) — included or dropped with reason
The shortlist's 12 names span sectors the DEEP set does not cover. **Per the L1 rule they are carried
here rather than silently lost.**

| Ticker | Sector | Flow | OBV | RS20 | FINRA z | Verdict | Fwd PE / Beta / Next ER | Disposition |
|---|---|---|---|---|---|---|---|---|
| **CTAS** | Industrials | +0.95 | +0.22 | +18.7 | −0.29 | △ normal short | 33.16 / 0.93 / 2026-09-23 | **CARRIED** — defensive-quality; but INDU is Neutral-lean-down and its ER is 2 months out. No near catalyst |
| **TRI** | Industrials | +0.80 | +0.17 | +22.1 | −0.51 | ✅ clean rise | 18.91 / **0.17** / 2026-08-05 | **CARRIED w/ DATA FLAG** — the 52wH 209.90 vs px 95.43 is a split artifact; valuation read unreliable |
| **EA** | Comm Services | +0.71 | ★ **+0.52** | +4.2 | −1.01 | ✅ clean rise | 21.74 / 0.64 / **2026-07-29** | **CARRIED** — highest OBV on the shortlist, in a **UW** sector. ⚠ **price 209.29 vs 52wH 209.32 — at its exact high**, and the target median (210.00) is +0.3%. Fully valued on consensus |
| **GRMN** | Cons Disc / IT | +0.67 | +0.20 | +5.1 | +0.37 | △ normal | 23.71 / 0.91 / **2026-07-29** | **DROPPED** — sits in a UW sector with no thesis support and only +1.7% implied upside |
| **T** | Comm Services | +0.50 | +0.18 | +0.4 | +0.98 | △ normal | 8.60 / **0.42** / ★ **2026-07-22** | **CARRIED** — ★ **prints TOMORROW (calendar gap #3)**; div **5.09%**, −26.3% off its high, **+33.3% to target median** — the widest implied upside on the entire sheet |
| PYPL · STT · ABT · TRV · CB · UNH · PGR | — | — | — | — | — | — | — | **Already covered in §2/§3** — not double-counted |

⚠ **Composition read, restated because it is itself evidence:** the shortlist is **4 insurance ·
2 health care · 4 defensive-quality services · 1 payments-M&A · 1 custody**. **Zero IT. Zero Energy.
Zero defense.** ★ **The ENRG absence is a 🟢-tag FILTER ARTIFACT, not a signal** (ENRG has 0 green
names while its OBV accumulates) — flagged in SWEEP §2(g) and repeated here so no reader mistakes it.

---

# §Z Illustration of influence ONLY (not a recommendation, not a size)
Purely to show **how the constraints above interact** — no instruction to buy or sell anything:
- The **epicenter-starter** (§0) is the only item on this sheet that exists **independent of tape**,
  because a rank-2 cycle at 0.0% is a structural hole, not a timing view. **Cleanest expression = XOM**
  (un-crowded, z −0.77, the only refining-complex name with positive implied upside and −15.9% off its
  high). **Timing is gated twice** — the ceasefire binary and crack-detachment Day 2.
- **HLTH·RE·UTIL·STPL count as ONE sleeve** (§2 §E) with a single kill-switch at real 10Y >2.50% /
  2s10s <+30bp. **Four labels, one exposure.**
- **SEMI is unresolved by design**, with five pre-committed KPIs and two prints inside 48 hours.
  **Nothing here is actionable before 07-23**, and the sheet says so rather than manufacturing conviction.
- **PYPL and STT are orphan special situations** that happen to sit in the FIN bucket. **They must not
  be counted as sector exposure.**

---
**EXIT CHECK:** ✅ **Every DEEP sector has a section** (§1 ENRG · §2 HLTH · §3 FIN · §4 SEMI), each with
§A numbers / §B thesis+freshness placeholder / §C flow / §D peers / §E refutation+dated catalyst ·
✅ **cross-sector LIVE_SHORTLIST names carried in §X, each explicitly CARRIED or DROPPED with a reason**
(GRMN dropped; TRI carried with a data flag) · ✅ **screener setups unioned in and flow-vetted before
use — 6 of 8 HLTH names dropped on flow, and both FIN names logged-not-promoted because they sit in the
zero-green bank sub-leg** · ✅ **numbers pulled live and BLANKS LEFT AS BLANKS** — ROE / operating margin
/ revenue growth / debt-equity are **absent from `module_fundamentals_us` and are therefore absent here,
not estimated** — with four further data-quality defects flagged up front (HPE stale ER, TRI split
artifact, PGR degenerate PEG, absent ratio fields) · ✅ **flow/positioning cross-read present for every
candidate**, FINRA z included wherever the tool returned it · ✅ **the pre-mortem's epicenter-starter
module is present (§0) and placed on the CLEANEST name rather than the strongest runner**, because the
prior run's own falsifier fired against the runners · ✅ **written as ONE file, `BET_SHEET.md`** ·
★ **three findings here contradict upstream stages and are stated rather than smoothed: PYPL is an M&A
spread and not the "wrongly avoided" name PREMORTEM called it; the refiners' "decoupling" was from
their own margin, not from crude; and CB — the dated test of the only FIN sub-leg still alive — prints
TOMORROW and no upstream stage found it.**
**→ proceed to ALPHA.**
