# BET_SHEET — industry_US · 2026-09-02 (Wed) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks read this exact filename — never split it.
> DEEP set: **`ENRG` · `HLTH` (ROTATION) + `IT` · `UTIL` (PREMORTEM-promoted)**.
> Flow asof **2026-09-01** (`SECTOR_FLOW_US_REPAIRED.json`). Benchmark **`SPY`** named inline.
> **Sizing language is influence illustration only — ZERO buy/sell recommendation (P4).**

## §0 · Instrument state and exposure state, before any number

**Instrument (PREFLIGHT):** primary sweep's OBV/flow/Δ **revoked**; the repaired file is the citable
object; **Δ is direction-only**; **no `wflow` verdict on `DISC`/`STPL`/`COMM`**; **no theme-freshness
from the sweep**; universe cap-weights **49 days stale**; **nothing about the 09-02 tape** — the
market had not opened at run time.

**Exposure (HANDOVER §5) — and the sizing language below is consistent with it:**

| book | state | what it means for this sheet |
|---|---|---|
| **Real KIS** | **$5,154 invested of ≈$10,980 ⇒ 53.1% cash**; 9 US names | there is room; the sheet is not cash-constrained |
| KR contest / timefolio | **85.2% invested vs a 95% target, band gap −9.8pp, 14th session outside**, verdict **정상** | a different book (`C23`); **not merged here** |

⚠ The `exposure_rule` verdict is **정상**, **not `복귀`** — so this stage is **not** under an
obligation to supply enough candidates to close a gap, and no candidate below is manufactured to fill
one. ⚠ Both instruments print 🚨🚨**ARMED (`TIMEFOLIO_EXECUTE=1`)**; **this run issues no order.**

## §0b · 🚨 Thesis-confirmation gate — the company scoreboard, consulted FIRST

`REPORT/COMPANY_SCOREBOARD.md` (2026-08-21, `company_batch` run 1) holds **5 rows, all KR**:
`036460` PASS 92.5 · `011200` PASS 79.5 · `316140` HOLD 76.2 · `028050` HOLD 64.7 · `000660` PASS 58.8.
⇒ **Zero of this sheet's candidates carry a scoreboard row**, so nothing is CONFIRMED-by-citation and
everything below is a fresh derivation. **The age test would fail anyway** — the run is **12 settled
sessions old** against a 10-session bar.
⚠ **"No row ≠ no coverage"** — `module_report_tags show` was cross-queried at HANDOVER and returns
`industry_US` sector files only, no US company reports. **The US side has never been through
`company_batch`**, and that is stated as a coverage gap rather than read as "nothing to confirm".
⚠ **A high score is not a promotion** — the scoreboard's own #1 row is a `PASS`.

## §0c · 🚨 STANDING rejections audited BEFORE any candidate is written (`D463`)

`reject_ledger due` returned **0 rows** — correctly, because no recheck date has passed. **`due` does
not answer "is this name currently rejected."** `reject_ledger list` does, and it changes this sheet:

| ticker | filed | class | revival condition | **status today** |
|---|---|---|---|---|
| **`EOG`** | 08-31 | `A.flow미도착` | *OBV turns 매집 **while** `DCOILWTICO` `[FRED]` ≥ 88.00* | 🚫 **STAYS REJECTED** — OBV **매집 ✅** but **`DCOILWTICO` last prints 83.90 at 2026-08-25** (7 days stale) ⇒ **< 88.00 ❌** |
| **`FANG`** | 08-31 | `A.flow미도착` | same | 🚫 **STAYS REJECTED** — OBV **중립 ❌** *and* the `[FRED]` leg ❌ |
| `XOM` | 08-31 | `A.flow미도착` | *OBV 매집 **AND** `rs20` > 0 on two consecutive settled closes* | 🚫 stays — OBV **−0.001 = 중립 ❌** (`rs20` +8.1 ✅) |
| `KEYS` · `CIEN` | 08-31 | `I.테제반증` | *`LITE` confirms card-6 KPI **AND** own OBV 매집* | 🚫 stays — `KEYS` OBV −0.168 분산, `CIEN` −0.132 분산 |
| `AON` | 08-31 | `A.flow미도착` | *OBV 매집 within 10 sessions of deal close* | 🚫 stays — OBV −0.068 중립 |
| **`CRM`** | 08-31 | `B.모멘텀only` | *`rs20` > +20 **AND** a new dated catalyst inside 30 days* | 🚫 **stays — `rs20` +36.4 ✅, catalyst ❌.** ⚠ **`CRM` is this run's rank-1 flow name (+1.000) with `vol_surge` 2.00, the board's highest** — the pressure to tag it is maximal and it is **barred** |
| `INTU` | 08-31 | `G.섹터중립` | *IT returns to `OW`* OR *short-vol z < −1.0* | 🚫 stays — IT is **N** ❌; z not pulled this run ⇒ `unknown` (`C3`) |
| `MRK` | 08-31 | `I.테제반증` | *0q revision breadth flips net-up **while** `rs20` > 0* | 🚫 stays — `rs20` **+18.3 ✅**, breadth leg **not pulled** ⇒ `unknown` (`C3`), recheck 10-29 |
| **`MSTR`** | 08-31 **and** 09-01 | `L.vehicle없음` ×2 | 08-31: *crypto driver row registered* OR *`rs60` positive with OBV > +0.40* · 09-01: *crypto proposition registered* OR *`rs20` > 0 while **BTC flat-to-down** over the same 20 sessions* | ⚠ **THE TWO ROWS DISAGREE — see below** |
| `HWM` · `GEV` | **09-02, this run** | `I.테제반증` · `A.flow미도착` | §D | 🚫 filed today at EVENT_ALPHA |

### ⚠ `MSTR` — the two stored conditions give opposite answers, and neither is improvised away
- **08-31 row: MET, on margins of 0.4pp and 0.004.** `rs60` **+0.4 (positive)** and OBV **+0.404
  (> +0.40)**.
- **09-01 row: NOT MET, and it is the better-specified test.** It asks whether *the bitcoin beta
  detaches*: over the same 20 sessions (**2026-08-12 → 09-01**) **`BTC-USD` +22.08%** and `MSTR`
  **+31.69%** against `SPY` **−1.39%**. **BTC is not flat-to-down — the beta did not detach; it
  levered.**
⇒ **`MSTR` is NOT revived into §A/§B.** The literal trigger fired on two hair's-breadth margins while
the row written the next day *specifically to test the same question with a cleaner observable* says
no. 🚫 **No threshold is re-written and no row is deleted** (`D242`) — both stand, the measurement is
recorded here, and **`due` will surface them on 09-18 / 09-22 for a human resolve (P5).**

### 🚨 An error THIS RUN made, recorded rather than edited away (`D48`)
**EVENT_ALPHA §10 filed `EOG` and `FANG` to `missed_ledger` — and both were carrying STANDING
rejections from this desk's own 08-31 run.** A name set aside with a stated reason is a **rejection**,
not a **miss**. The machine guard did not stop it because **`missed_ledger add` refuses a duplicate on
`ticker × date`, and the dates differ (08-31 rejection vs 09-02 miss)**, so a standing rejection is
invisible to it.
⇒ **Both records stand (append-only).** Registered as **`D478`** — *the miss-ledger guard is keyed on
`ticker × date` and therefore cannot see a standing rejection from an earlier date; the standing list
must be read before filing a miss.* This is the **US analogue of `D471-KR`, filed by the sibling desk
this morning**, reproduced here within hours — which is itself the finding: **the same boundary error
occurred on two desks on the same day.**

---

## §A · Energy (`ENRG`) — OW · continuous track

### A-1 Numbers (`module_fundamentals_us`, 2026-09-02; XBRL↔yfinance cross-checked where available)

| | `SLB` | `WMB` | `MPC` (held) | `PSX` (held) | `XOM` |
|---|---:|---:|---:|---:|---:|
| price | $57.16 | $73.80 | **$386.86** | **$254.72** | $163.16 |
| vs 52w high | −5.5% | −7.8% | **−0.4%** | **−0.25%** | −7.5% |
| mcap | $85B | $90B | $109B | $102B | $671B |
| trailing / forward P/E | 27.91 / **17.70** | 29.38 / **28.14** | 13.41 / **11.93** | 14.21 / **12.31** | 21.00 / 15.33 |
| 90d estimate Δ (cur-yr / next-yr) | 🚨 **−4.2% / −3.4%** | +1.7% / +1.9% | **+81.9% / +44.4%** | **+48.2% / +25.1%** | +5.7% / +1.3% |
| revision breadth (30d, next-yr) | — | **6↑ / 2↓** | — | — | — |
| consensus target vs price | +8.5% | +15.5% | 🚨 **−16.1%** | 🚨 **−12.8%** | +4.0% |

### A-2 Thesis · freshness placeholder *(ALPHA fills the freshness tag)*
**The OW is chain-positioned on level and turning barrel-ward on Δ** (`SECTOR_DEEP_ENRG §1`): level
order refining > services > midstream > barrel; **Δ order exactly reversed**. `P126` (09-09) is the
row that settles which. **16 of 16 names positive, zero reds — the only sector on the board with no
red name.**
_freshness: [ALPHA]_

### A-3 Flow / positioning cross-read

| name | flow | tag | OBV | `rs20` / `rs60` vs `SPY` | surge | Δ | `[FINRA]` z (09-01) |
|---|---:|:--:|---:|---:|---:|---:|---:|
| **`SLB`** | +0.894 | 🟢 | +0.351 | +13.7 / +0.9 | **1.41** | +0.105 | +0.47 △ |
| **`WMB`** | +0.772 | 🟢 | +0.181 | +6.4 / +1.3 | 1.31 | +0.118 | **−3.08 ✅ clean rise** |
| `MPC` | +0.717 | 🟡 | **+0.425** | +23.8 / **+42.9** | 1.09 | −0.005 | +1.49, 5v5 **+8.6▲** |
| `PSX` | +0.661 | 🟡 | +0.301 | +23.6 / +34.4 | **0.99** | +0.089 | +0.59 |
| `XOM` | +0.287 | 🟡 | −0.001 | +8.1 / +6.5 | 0.92 | **+0.536** | +0.47, 5v5 **−11.3▼** |

★ **`SLB` chart (`module_chart --read`)**: **CONFIRMED-TURN**, OBV 20d slope **+103%**, RSI 65.9,
price above 4/4 MAs, stop-reference (swing low) **49.91**.
★ **`MPC` chart**: **CONFIRMED-TURN** but **RSI 77.5**, momentum20d **+29.8%**, Bollinger expanding
30.4% — extended, stop-reference **296.94**.
⚠ Both reads run on a window that spans **2026-08-28**; for names outside the 42 backfilled that bar
is a 5m proxy (close err ≤0.094%, volume −18% biased).

### A-4 Competition / peers
`us_setup_screener --sector Energy` returns **0 setups in all three buckets across 16 names** — no
leader pullback, no de-rate snapback, no washout. ⇒ **the whole sector is extended; there is no entry
setup in it today**, which is a finding, not an absence of coverage.

### A-5 Refutation + dated catalyst
- 🚨 **`MPC` and `PSX` are the sheet's clearest peak-margin cases and the gap WIDENED**: within
  **0.4%** of 52-week highs, estimates revised up **48–82% in 90 days**, and **consensus targets
  BELOW the live price** (−16.1% / −12.8%, from −13.9% on 09-01). **Refining has no take-or-pay
  (`M831`) ⇒ lens `B2` has no escape hatch here.**
- 🚨 **`SLB` is the board's #2 flow name on a CUT estimate line** (−4.2% / −3.4%) with only **+8.5%**
  consensus upside and **RSI 65.9** — the internal contradiction is stated, not resolved.
- **Dated catalysts**: `P126` · `S136` settle **09-09**; `S109` (`FRO`) settles **tonight**; the
  Hormuz "Strait open" statement is **undated** and **no date is invented**.
- **Anti-signal**: an OPEC+ emergency production decision or a US SPR action — **checked, neither
  fired** in the 8-day window (220 `OPEC` hits; the OPEC-adjacent story is Venezuela weighing an
  *exit*, which is structural and explicitly not a voider).

---

## §B · Health Care (`HLTH`) — OW (promoted today) · continuous track

### B-1 Numbers

| | `A` | `MDT` | `LLY` |
|---|---:|---:|---:|
| price / vs 52w high | $152.32 / −7.0% | $93.97 / −11.6% | $1,181.69 / −8.6% |
| forward P/E | 22.52 | **14.69** | 25.01 |
| 90d estimate Δ (cur-yr / next-yr) | **+2.6% / +2.3%** | 🚨 **−1.8% / −1.9%** | +1.5% / **+6.3%** |
| consensus target vs price | **+14.5%** | 🚨 **+5.2%** | +11.3% |

### B-2 Thesis · freshness placeholder
**The OW is three different stories, and the file says so**: pharma holds the level (EW +0.474,
`rs20` +11.22), **payers hold the change** (EW Δ **+0.247**, the sector's best, with `UNH` +0.310 ·
`CI` +0.359 · `CVS` +0.251), devices hold both greens **and the only negative Δ** (−0.137).
**Dispersion 1.583 vs a 7.14 sector move ⇒ `B5` fires: the sector label is the wrong unit.**
_freshness: [ALPHA]_

### B-3 Flow / positioning cross-read
`A` +0.828 🟢 · OBV +0.208 · `rs20` +8.9 · surge **1.29** · Δ −0.066 — chart **PULLBACK-TO-SUPPORT**,
OBV +59%, RSI 55.7, stop-reference **141.11**.
🚨 `MDT` +0.774 🟢 · OBV **+0.137 (sweep says 매집)** vs **`module_chart` OBV NEUTRAL, 20d slope −5%**
⇒ **`C25` reproduces on a US name; the accumulation leg is established by neither instrument.**
`MDT`'s 🟢 therefore rests on `rs20` +8.0 and `vol_surge` 1.28 alone.

### B-4 Competition / peers
`us_setup_screener --sector "Health Care"` → **4 new names**: `LLY` (leader pullback, RSI 42.1,
+10% vs 200DMA), `EW` (leader pullback, RSI 42.8), `ISRG` (de-rate snapback, RSI 37.0, **−19% vs
200DMA**), `SYK` (**washout, RSI 24.9**, −6% vs 200DMA). ⚠ **`D304`: the screener ran pre-open at
09:1x ET, so its bar may be partial.** The four are **recorded as a list only** and **none is
ledgered or promoted on it**.

### B-5 Refutation + dated catalyst
- 🚨 **`MDT` is downgraded to 🟡PARTIAL on this sheet**: a 🟢 on a **cut** estimate line with only
  **+5.2%** consensus upside, an **unconfirmed buyer side** (`HCA` −0.194, `MCK` −0.033), and a live
  instrument disagreement on its accumulation leg. **This is the same shape as the 08-31 `INTU` error
  (`M1219`) and it is caught BEFORE ALPHA tags it, not withdrawn after.**
- **`A` is the sheet's one clean Health Care candidate**: rising estimates, +14.5% consensus upside,
  buyer side confirmed by pharma's own rising estimate lines, chart in pullback rather than extended.
- **Dated negatives**: MFN pricing extended to 9 mid-sized drugmakers [5 outlets, 09-01] points at the
  node carrying the sector's level; **track KPI — pharma EW `rs20` falling below +5 within 5 settled
  sessions kills the level leg.** `S133` settles **09-14**.
- **Unknown, marked**: the payer node's contractual band (MLR rebate floor) was **not read from a
  filing** ⇒ `C3`, and it is this sector's top dig.

---

## §C · Information Technology (`IT`) — N · PREMORTEM-promoted

### C-1 Numbers

| | `NVDA` (real book **21.3%**) | `ANET` (**14.6%**) | `AVGO` (paper book) | `MU` |
|---|---:|---:|---:|---:|
| price / vs 52w high | $222.28 / −6.0% | $186.34 / −13.3% | $368.43 / **−25.6%** | $939.03 / −25.2% |
| forward P/E | **14.43** | 36.11 | **18.82** | **6.06** |
| 90d estimate Δ (cur-yr / next-yr) | +4.1% / **+22.2%** | **+13.3% / +16.0%** | +2.7% / **+6.0%** | +25.9% / **+50.9%** |
| revision breadth | — | — | **25↑ / 9↓ (30d)** | — |
| consensus target vs price | **+46.7%** | +29.8% | **+42.8%** | +61.1% |

★★ **The sheet's largest cross-sector fact**: in **Energy**, estimates revised up **48–82%** sit at
52-week highs with targets **BELOW** price; in **IT**, estimates revised up **6–51%** sit **6–26%
below** their highs with targets **30–61% ABOVE** price. **The same input is priced in opposite
directions in the two sectors this run deep-dived** — lens `B2` loads in Energy and does not load here.
⚠ **`D395`/`D428` bind**: the revision table is **a description of the denominator's direction only**,
is **not** a leading indicator, and carries **no independent weight on an IT name** (the 2026-08-09
control measured the whole effect as an IT loading, ex-IT Q5−Q1 **−1.1pp**).

### C-2 Thesis · freshness placeholder
**IT is two bets.** Software/services/security (n=21) reads **+0.092 flow · +0.042 OBV · +4.73 `rs20`
· 1 green**; semicap/test (n=6) reads **−0.759 · −0.221 · −9.82 · 0 greens**. **Gap 0.851.**
Dispersion **1.878 — the widest on the board**, decisively exceeding the sector's own move.
⇒ **the verdict unit for IT should be the sub-node, not the sector.**
_freshness: [ALPHA]_

### C-3 Flow / positioning cross-read — the two held names are being distributed AND shorted
`NVDA` +0.036 🟡 · OBV **−0.195** on `vol_surge` **1.38** · Δ −0.210 · `[FINRA]` z **+2.18 🔴** ·
chart **PULLBACK-TO-SUPPORT with a BEARISH DIVERGENCE** (price higher high, RSI lower high), OBV 20d
**−89%**, coiling 9.6%, stop-reference **208.48**.
`ANET` −0.029 🟡 · OBV +0.070 but `vol_surge` **0.64** · Δ **−0.494** · `[FINRA]` z **+2.25 — the
board's largest short build** ⇒ **PREMORTEM Lens 3 re-tagged it EXHAUSTED**: `rs60` +19.4 has decayed
to `rs20` **+0.6**.
`AVGO` −0.711 🔴 · OBV −0.264 · chart **FALLING-KNIFE (진입 금지)**, **RSI 24.5**, **0/4 MAs**, OBV 20d
**−84%**, stop-reference 355.59 · positioning short **1.2% float COVERING**, DTC 3.0, **P/C 1.62**,
**예상변동 ±9.5% (D0)**.

### C-4 Competition / peers
`us_setup_screener --sector "Information Technology"` → **4 new**: `HPE` (leader pullback, **RSI
20.8**, +53% vs 200DMA), `KEYS` (RSI 28.0 — ⚠ **standing rejection**, §0c), `DELL` (RSI 34.5, **+76%
vs 200DMA**), `IBM` (de-rate snapback, RSI 44.4). Existing: `ANET`, `CRWD`. ⚠ `D304` — pre-open bar;
**list only, nothing ledgered.**

### C-5 Refutation + dated catalyst
- 🚨 **`module_disclosure_us AVGO --days 45` returns 0 filings, 0 8-Ks.** The two-run-old gap
  *"contracted share unknown, module never opened"* is **opened and converts**: the share is `unknown`
  **because there is nothing filed**, not because nobody looked (`C3`). **Any claim about `AVGO`'s
  contracted AI revenue tonight is press-sourced.**
- **Dated catalyst: `AVGO` prints TONIGHT.** `S138` (±11.00pp) is **outside** the measured **±9.5%**
  implied move and is the informative row; **`S132` (±9.00pp) is INSIDE it and is restated as
  pre-declared NO-INFORMATION** (`D451`); `S141` (does the print move `SMH`) settles **09-03**;
  `S127` settles 09-08; `S140` (does IT's breadth hold) settles 09-08.
- **`MU`'s low multiple is checked against its contract band, not asserted**: the FY26Q3 10-Q
  establishes **take-or-pay volumes with a floor and a ceiling**, so the decelerating contract-price
  QoQ series (**+90~95% → +58~63% → +13~18%**) is **arithmetic hitting a cap, not demand weakening**.
  ⚠ **The contracted share itself is still `unknown`** (`C3`, carried).
- **Anti-signal, base rate pre-stated**: a dated US export-control action on advanced semiconductors
  would void `S141`; the recent **tungsten / battery black-mass** action and the **draft** rule
  reported by tomshardware are **different product classes and are NOT voiders**.

---

## §D · Utilities (`UTIL`) — UW · PREMORTEM-promoted · full fresh map

### D-1 Numbers

| | `VST` | `CEG` | `NEE` |
|---|---:|---:|---:|
| price / vs 52w high | $140.54 / **−36.1%** | $284.47 / **−31.1%** | $82.35 / −16.6% |
| forward P/E · PEG | **13.56** · **0.40** | 21.30 · 3.74 | 18.76 · 1.82 |
| 90d estimate Δ (cur-qtr / next-yr) | **+14.0% / −5.0%** | +2.3% / −1.8% | **−1.8% / −0.2%** (next-qtr **−11.2%**) |
| consensus target vs price | **+54.7%** | +22.4% | +19.5% |
| ratings | 19 buy / 0 hold / 1 strong sell | 19 / 3 / 0 | 12 / **7 hold / 1 sell** |

### D-2 Thesis · freshness placeholder
**It is an OFFTAKE story, not an equipment story** — and the offtake story's own **denominator** is
under a dated, **two-ISO** attack (ERCOT's halt **and** PJM pulling a Meta-backed 750MW project), with
a **$1.45bn** behind-the-meter bypass acquisition announced 09-02. **`VST`'s estimate term-structure
already carries it: near-term +14.0%, out-year −5.0%.**
**And the sector's one unique number: all 15 names carry a positive Δ — no other sector is unanimous.**
_freshness: [ALPHA]_

### D-3 Flow / positioning cross-read
`VST` 🟡 · OBV −0.070 (sweep) vs **chart OBV +93% accumulation** · Δ **+0.432** · coiling 10.5% ·
RSI 41.1 · bearish MA stack · stop-reference **135.66** · positioning: short **3.3% float covering**,
DTC 2.0, **P/C 22.65**, 예상변동 ±3.7% (D2).
`CEG` 🟡 · `rs20` +6.1 · chart OBV **+90%**, 4/4 MAs, **upper band**, coiling 9.1% · stop-reference
**260.70** · short 3.0% float covering, P/C 1.61.
`NEE` 🟡 · Δ **+0.481 (sector best)** · chart **BULLISH DIVERGENCE at the lower band**, coiling
**5.3%**, RSI 26.7 · stop-reference **82.34**.
⚠ **`D6`** — every OBV figure above is reported beside RSI, MA stack and Bollinger width; **no
candidate rests on OBV alone.**

### D-4 Competition / peers
`us_setup_screener --sector Utilities` → **3 new**: `ETR` (leader pullback, RSI 44.7), **`SO`
(washout, RSI 19.9)**, **`PCG` (washout, RSI 26.0, −24% vs 200DMA, −26% vs 50DMA, at its 52-week
low)**. ⚠ `D304` — pre-open bar; **list only**.
★ **`PCG` is the wildfire-legislation crater** and carries **`vol_surge` 3.18, the highest reading in
the 298-name universe** — a capitulation-and-bounce signature, **not** accumulation.

### D-5 Refutation + dated catalyst
- 🚨 **This sheet inherits a correction to its own run** (`SECTOR_DEEP_UTIL §1`): MACRO §E and
  EVENT_ALPHA Card 4 cited *"California Wildfire Legislation Postponed, Utility Stocks Bounce"*
  [6 outlets] as a **positive**. The body says utilities **plummeted on 08-28/08-31** when the
  legislation was announced, and the 09-01 item is the **bounce after a postponement**. ⇒ **`XLU`'s
  exc1 +1.47 — one of the two numbers that promoted this sector — is partly a legislative
  round-trip.** Registered `D477`.
- **The UW is NOT challenged by this sheet.** What is handed forward is a falsifiable test: **if the
  15/15 Δ unanimity repeats next run while `eqflow` stops falling, the axis disagreement resolves in
  Δ's favour.** ⚠ **One run of unanimity is n≈1** (`B3`).
- **Dated catalyst**: `S135` (are `UTIL`/`RE`/`STPL` three verdicts or one?) settles **09-11**;
  `P127` (power vs compute) settles **09-10**; `P123` settles 09-08.
- **Unknown, marked**: no US gas contract-price QoQ series is wired ⇒ `B1`'s second derivative is
  `unknown` (`C3`) for this sector, not substituted with the spot level.

---

## §E · Cross-sector LIVE shortlist + the epicenter/cycle module

### E-1 `US_LIVE_SHORTLIST.json` — 6 names, all inside the DEEP set, none dropped
`CRM` (IT) · `SLB` (ENRG) · `A` (HLTH) · **`NEM` (MATR)** · `MDT` (HLTH) · `WMB` (ENRG).
⇒ **Only `NEM` falls outside a DEEP sector**, and it gets its own row rather than being dropped:

🚨 **`NEM` — the shortlist's cleanest "clean rise" sits on the most-cut estimate line on this sheet.**

| | `NEM` |
|---|---|
| flow / tag | **+0.783 🟢** (a `new_green` this run) |
| OBV · `rs20` · `rs60` · surge | +0.270 · **+26.7** · +19.7 · **1.21** |
| `[FINRA]` z | **−3.14 ✅** — the board's most extreme short exit |
| forward P/E | 12.55 |
| **90d estimate Δ** | 🚨 **−12.1% cur-yr / −11.8% next-yr** |
| **revision breadth (30d)** | 🚨 **1↑ / 11↓** and **4↑ / 11↓** |
| consensus target vs price | 🚨 **+5.0%** ($126.53 vs $132.87 mean) |
| ⚠ | it crossed the `vol_surge` 1.0 gate it **missed by 0.01 yesterday** (`C5`) — the tag is a threshold event, not a regime event |

⇒ **`NEM` is handed to ALPHA as 🟡PARTIAL, not as a clean green.** Three names on this sheet now carry
the same shape — *a 🟢 or near-🟢 on a cut estimate line* (`MDT`, `NEM`, and the standing `INTU`) — and
naming the shape is more useful than naming the names.
⚠ Its sector (`MATR`) was **demoted to N today** and its `C24` contradiction (copper spec at the
**100th percentile** `[COT 08-25]`) is carried unresolved for a 4th run.

### E-2 Epicenter / cycle module — a GAP the instrument cannot raise
`cycle_exposure` prints **✅ no GAP** (AI-compute epicenter 16.8% ≥ 12.0%; Energy 10.3% ≥ 8.0%).
🚩 **Three things sit under that ✅, and they are handed to this sheet by PREMORTEM Lens 4:**
1. **The AI-power cycle has no registry row** (`D416`, 6th run), so no GAP can be computed for it.
   The book's only exposure is **`ETN` 7.5%**, tagged *adjacent*, and `ETN` is **🔴분산, Δ −0.633
   (4th-worst in the universe)**, `[FINRA]` z −1.72 (shorts leaving a **falling** name).
   ⇒ **manually flagged as a GAP the instrument is structurally unable to raise.**
2. **The rank-1 cycle's epicenter is half-exhausted**: `ANET` (14.6%) re-tagged **EXHAUSTED**; `NVDA`
   (21.3%) distributed on 1.38× volume with z +2.18. **A floor met by two distributed names is a
   floor met on paper.** ⚠ **This is a TIMING flag, never a weight cut** — the rule is explicit that
   a 🔴 tape gates ADD timing and never justifies zero core in a multi-year cycle, and **a partial
   core exists on this sheet regardless of tape.**
3. **16.6% of real invested capital carries no thesis**: `T` **13.8%** (OBV **+0.409 매집**, `rs60`
   +11.0 — 2nd run) and **`CBRE` 2.8%** (**🔴분산**, newly surfaced this run). **Assigning theses is a
   human call (P5).**

### E-3 Sizing language — illustration only
The real book is **53.1% cash** with the exposure verdict at **정상** (not `복귀`), so **no target
needs to be closed and nothing below is manufactured to close one.** Influence illustration: the
sheet's **one clean candidate** is `A` (rising estimates, +14.5% upside, pullback chart); `SLB` and
`WMB` are 🟢 with the body-read behind them but carry a cut estimate line and a 28× forward multiple
respectively; `MDT` and `NEM` are 🟡PARTIAL on cut estimate lines. **Zero buy/sell recommendation is
made (P4).**

---

## §F · Ledger writes this stage

**No new rejections and no new misses are filed at BET.** The reason is stated rather than left
implicit: **every name this stage set aside was already filed at EVENT_ALPHA** (`HWM`, `GEV`
rejected; `PSX`, `CVX`, `EOG`, `FANG`, `CEG`, `FRO`, `LNG` missed), and **the two names this stage
would otherwise have filed are already standing rejections** (`CRM`, `MSTR`) that it is **barred from
re-filing** — re-filing a standing rejection would double-count the same decision.
⚠ **This is not a zero-scored funnel**: 2 rejections + 7 misses were written this run, at the stage
that generated them. **The boundary error in that set (`EOG`/`FANG`) is recorded in §0c as `D478`.**

**Names re-filed rather than removed** (the flow gate still passes, only the story changed): none this
run — no candidate lost its story while its money kept arriving.

---

## ✅ EXIT CHECK
- [x] **Company scoreboard consulted before any re-derivation** (§0b): 5 rows, **all KR**, **zero
      overlap** with this sheet's candidates, and the **age test fails at 12 settled sessions vs a
      10-session bar** ⇒ nothing CONFIRMED-by-citation, and the US-side coverage gap is named rather
      than read as "nothing to confirm". No matured observation point to grade.
- [x] **Every DEEP sector has a section** (§A–§D); the cross-sector LIVE shortlist name outside the
      DEEP set (`NEM`) is **included with its own row**, not dropped.
- [x] Numbers cross-checked (`module_fundamentals_us` reports its own XBRL↔yfinance agreement:
      **4/4 quarters within 5%** for `AVGO`/`VST`/`CEG`, 2/2 for `MDT`, **0/0 for `NEE`** — the last
      is stated as a blank, not filled in). **Blanks are blanks**: `INTU` short z, `MRK` revision
      breadth, `MU` contracted share, `AVGO` contracted share, the US gas QoQ series — all `C3`.
- [x] Flow/positioning cross-read present per candidate; **BET_SHEET.md written as ONE file.**
- [x] **Every set-aside name is in a ledger with a class AND a `--revives-if`/`--enters-if` condition**
      (filed at EVENT_ALPHA §10, listed in §F). **Every name whose stored condition might have come
      true was checked against the pre-registered observable** (§0c) — `EOG`/`FANG` fail on
      `DCOILWTICO` **83.90 < 88.00**, `XOM` on OBV 중립, `MSTR` on the newer of its two rows
      (**BTC +22.08%**, the beta did not detach).
- [x] **No name was removed on narrative grounds alone while its measured flow still passed.**
      `HWM`/`GEV` were dropped on a **MONEY** verdict (both 🔴분산) as well as a story one.
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** with
      `--enters-if` (7 rows). ⚠ **Two of them (`EOG`, `FANG`) were mis-filed as misses when they were
      standing rejections** — both records stand and the defect is registered as **`D478`** (§0c).
- [x] **Sizing language is consistent with the carried exposure state** (§0, §E-3): the state is
      **정상**, not `복귀`, so no unfillable target is created and none is claimed to be closed.
- [x] **Linter run on this stage's own output** — `report_lint.py BET_SHEET.md` ⇒ **0 findings**
      (C1·C2·S6·D6); `module_math_check BET_SHEET.md` ⇒ **ALL MATH CHECKS PASSED**. ⚠ Both check form
      and arithmetic only; a clean run is not a correct sheet.

---

# ═══ §B · ALPHA FRESHNESS TAGS — appended 2026-09-02 by Stage 10 / L1·ALPHA ═══

> Fills the `_freshness: [ALPHA]_` placeholders left in §A–§E. **Append-only** — nothing above is
> rewritten. **Zero buy/sell recommendation (P4).**

## B-0 · 🚨 The pipe was checked BEFORE the freshness verdict was written

The stage's own rule: *"a dead pipe and a quiet theme return the identical value… when G1 FAILs,
ALPHA may not issue a freshness verdict at all."* **G1 FAILED on the sweep axis (`vel_coverage`
17.11%) and PASSED on the direct path**, and `theme_age` rides the **direct** path. The
falsification evidence, all from this run:

| probe | result |
|---|---|
| headline `fts` pre-sweep | **6/6** — Federal Reserve 1530 · Nvidia 5094 · tariff 1966 · jobs report 140 · oil prices 1456 · data center 2730 |
| headline `fts` post-sweep | **4/4**, identical counts |
| `news_velocity` falsification, **9s cadence** | **10/10 alive**, incl. universe-floor `PCAR` **1.29** and `JCI` **0.99** |
| ★ the controlled test | the **same 7 names** returned `None` at **1.5s** and real numbers at **9s** — the `None`s were **refusals**, not silence |

⇒ **The pipe is verified live and this stage MAY issue a freshness verdict.** Every `theme_age` call
below was fired at **≥9s spacing, outside the sweep window**.

## B-1 · Theme age — deterministic novelty, run BEFORE any live search

| theme (bet it serves) | verdict | age | 7d avg | accel | base |
|---|---|---:|---:|---:|---:|
| `refining margin` (`MPC`/`PSX`) | ⚪ECHO | 76 | 4.4 | **0.66×** | 302 |
| `oilfield services` (`SLB`) | ⚪ECHO | ≥90 | 3.0 | 0.98× | **165** |
| `LNG` (`WMB`) | ⚪ECHO | ≥90 | 38.3 | 1.26× | 1,697 |
| `gold price` (`NEM`) | ⚪ECHO | ≥90 | 28.7 | **0.87×** | 1,880 |
| `medical devices` (`MDT`) | ⚪ECHO | ≥90 | 14.3 | **0.76×** | 1,021 |
| `life sciences` (`A`) | ⚪ECHO | ≥90 | 20.1 | 0.91× | 1,308 |
| `data center` (`IT`/`UTIL`) | ⚪ECHO | ≥90 | 334.4 | 1.02× | 18,967 |
| `gas turbine` (`UTIL` equipment) | ⚪ECHO | ≥90 | 11.3 | 1.42× | 476 |
| **`bond selloff`** (macro, no vehicle) | 🟡ACCELERATING | ≥90 | 12.7 | **3.81×** | 196 |
| **`Larak`** (Hormuz) | 🟡ACCELERATING | 37 | 26.6 | **72.47×** | 198 |
| `ghost demand` (the `UTIL` falsifier) | 🟢FRESH | **1** | 0.4 | — | **3** |

★ **`F1` fires again: 0 🟢LIVE, a 9th consecutive US run — and this time the zero is arithmetic on a
VERIFIED pipe, not an untested one.** **Not one bet theme is FRESH.** The only 🟢FRESH reading on the
board is **`ghost demand` on a base of 3** ⇒ **FRESH-but-thin, excluded from the gate by `D461`** —
and it is a **falsifier**, not a thesis. The two accelerating themes (`bond selloff` 3.81×, `Larak`
72.47×) are **macro axes the desk has no clean vehicle for** (`L.vehicle없음`, `D456`).
⇒ **A board whose only novelty is a falsifier and two un-investable macro axes is the finding**, and
it is why every tag below is 🟡 or 🔴 rather than 🟢.

## B-2 · Tags

| name | tag | residual / reason | **dated re-check** |
|---|:--:|---|---|
| **`A`** (Agilent) | **🟡PARTIAL** | The sheet's cleanest candidate — rising estimates (+2.6%/+2.3%), **+14.5%** consensus upside, buyer side confirmed by pharma's own rising lines, chart **PULLBACK-TO-SUPPORT** (OBV +59%, RSI 55.7), stop-ref **141.11**. **Residual: its theme is ⚪ECHO at 0.91× on a base of 1,308** — there is no novelty carrying it, so the entry depends on the `vol_surge` 1.29 holding | **2026-09-09** |
| **`SLB`** | **🟡PARTIAL** | 🟢 on flow with a **CONFIRMED-TURN** chart (OBV +103%, RSI 65.9, 4/4 MAs) and a dated **8-K Item 7.01 guidance filing on 08-31**, the session it ignited. **Residual: estimates are being CUT −4.2%/−3.4% with only +8.5% consensus upside, and its theme is ⚪ECHO at 0.98× on a base of just 165.** Flow and the revision book point opposite ways | **2026-09-09** (with `P126`/`S136`) |
| **`WMB`** | **🟡PARTIAL** | 🟢 with the board's 2nd-most-extreme short exit (`[FINRA]` z **−3.08**), a fee-based/contracted revenue model (the take-or-pay frame **applies** here), and next-year revision breadth **6↑/2↓**. **Residual: forward P/E 28.14 is the richest multiple on the sheet, and the `LNG` theme is ⚪ECHO at 1.26×** | **2026-09-09** |
| **`NEM`** | **🟡PARTIAL** | ✅ "clean rise" on the shortlist (z **−3.14**, `rs20` +26.7). **Residual, and it is severe: estimates CUT −12.1%/−11.8% with 30-day breadth 1↑/11↓, consensus upside only +5.0%, `gold price` ⚪ECHO at 0.87×, and the 🟢 exists only because `vol_surge` crossed 1.0 after missing it BY 0.01 yesterday (`C5`).** Its sector was demoted to **N** today | **2026-09-09** |
| **`MDT`** | **🟡PARTIAL** | **Residual: a 🟢 on a CUT estimate line (−1.8%/−1.9%) with +5.2% consensus upside, an unconfirmed buyer side (`HCA` −0.194, `MCK` −0.033), a ⚪ECHO theme at 0.76×, AND a live instrument disagreement on its accumulation leg** — sweep says `obv_norm` +0.137 매집, `module_chart` says OBV **neutral, 20d slope −5%** (`C25` on a US name) | **2026-09-09** |
| **`CEG`** | **no tag — `missed_ledger`** | The cleanest AI-power offtake expression (chart OBV +90%, 4/4 MAs, `rs20` +6.1) inside a card filed STORY-ONLY. Filed `Q.확신부족`, enters if 🟢 **or** `P127` fires A | **2026-09-10** |
| **`CRM`** | 🚫 **BARRED, no tag issued** | Standing 08-31 rejection `B.모멘텀only`. Revival needs `rs20 > +20` ✅ **and a new dated catalyst inside 30 days ❌**. ★ **This is precisely the check the 08-31 run failed (`M1219`/`D463`) — it is applied here BEFORE the tag, not withdrawn after** | 2026-09-30 |
| **`MSTR`** | 🚫 **BARRED, no tag issued** | Two standing rejections; the better-specified one is unmet — **BTC +22.08% over the same 20 sessions, so the beta did not detach** (`BET_SHEET §0c`) | 2026-09-18 / 09-22 |
| **`HWM`** · **`GEV`** | 🔴 **RESOLVED → dropped, ledgered** | Filed at EVENT_ALPHA with `--revives-if` + `--recheck-date`. `HWM` `I.테제반증` (the thread's body says an entrant attacks its bottleneck and the tape already knocked it); `GEV` `A.flow미도착` | **2026-09-10** |

## B-3 · Momentum-only flags, graded before they are acted on (`D6`)

| name | flag | grade of the disagreement |
|---|---|---|
| **`NEM`** | RS/volume green (`rs20` +26.7, surge 1.21) vs **an estimate book at 1↑/11↓** | ⚠ **not an OBV disagreement** — OBV agrees (+0.270 매집). The disagreement is **flow vs fundamentals**, which the `D6` grading ladder does not cover ⇒ reported as a **𝗳𝘂𝗻𝗱𝗮𝗺𝗲𝗻𝘁𝗮𝗹 disagreement**, and it is why the tag is 🟡. **Hard stop required if ever acted on** |
| **`MDT`** | 🟢 tag vs **OBV neutral on the chart instrument** | **C-grade** (OBV-only, r≈0.49, no leading power) ⇒ **downgrades to 🟡 and is reported as a disagreement** — it does **not** by itself convert the bet into a tape trade |
| **`MPC`** (held) | `rs60` **+42.9** with **RSI 77.5** and shorts pressing (z +1.49, 5v5 **+8.6▲**) | **EXTENDED-BUT-LIVE** (PREMORTEM Lens 3). Hard-stop reference **296.94** |
| **`ANET`** (held) | `rs60` +19.4 decayed to `rs20` **+0.6** on `vol_surge` **0.64**, z **+2.25** | 🚩 **EXHAUSTED** — the only runner of nine re-tagged so, and it is **14.6% of real invested capital**. Flip condition: `rs20` > +8 **with** `vol_surge` > 1.0 |

## B-4 · Positioning gate (US)
**No ⚡crowded-short name is on the sheet.** The shortlist's short-pressure verdicts are **2 ✅
clean-rise** (`NEM` z −3.14, `WMB` z −3.08) and **4 △ normal** — **zero crowded-short**, so the
"squeeze fuel, never a standalone buy" stamp is not needed on any candidate this run.
⚠ Where crowded fear *does* sit is in the names the desk **holds**: `AVGO` P/C **1.62** and `NVDA`
P/C **2.16 with skew +26.1** into tonight's print. **That is squeeze fuel on a beat and it is stamped
hard-stop, not converted into an add** (`NVDA` swing-low **208.48**, `AVGO` **355.59**).

## B-5 · Tags that follow the NAME, not the sector — carried into the next run's inheritance packet
`A` · `SLB` · `WMB` · `NEM` · `MDT` (all 🟡PARTIAL, **all re-check 2026-09-09**) **plus** `CEG`
(`missed`, 09-10). ⚠ **`NEM`'s sector was demoted to `N` today and `MATR` holds no DEEP slot** — under
the measured `006360` failure (a tag carried, the sector rested, **+12.3% unowned over five
sessions**), **the tag follows the name and is carried anyway.**

## B-6 · Withdrawals this run
**None.** ★ **And that is the point worth recording**: the 09-01 run had to withdraw two tags
(`CRM`, `INTU`) *after* issuing them because it checked only `reject_ledger due`. This run read
`reject_ledger list` **before** tagging (`BET_SHEET §0c`) and **issued neither tag**. `D463`'s
prescription worked on its first application.

## B-7 · ACTION_TICKETS
Written to `llm_outputs/2026-09-02/ACTION_TICKETS.md` (day-folder root, script-owned).
🚨 **`action_bracket` emitted ZERO tickets while naming the nearest binary in the line above — `D294`,
7th reproduction, on a window holding FIVE binaries.** Per PREMORTEM's pre-commitment, **the tickets
are hand-written in an append-only ADDENDUM** to that file: both-sides brackets for `AVGO` (D-0) and
the NFP (D-2), plus the AI-power cycle flag the instrument could not raise. **DRY-RUN only; a human
executes separately and `--execute` is not used by this desk.**
