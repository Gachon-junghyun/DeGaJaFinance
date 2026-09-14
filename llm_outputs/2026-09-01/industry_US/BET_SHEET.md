# BET_SHEET — industry_US · 2026-09-01 (Tue) · Stage 9 / L1·BET
### ONE file, per-sector sections (§A–§E each). Downstream desks glob this exact filename.

> **Analytical output only. Zero buy/sell recommendation. No sizing.** (P4 · the run's standing mandate.)
> Flow: `SECTOR_FLOW_US_REPAIRED.json`, 3-axis `nonews`, **asof 2026-08-31**. Benchmark `SPY` inline (`C1`).
> ⚠ **Prices, multiples and analyst targets below are `[live]`** — `module_fundamentals_us` was run
> with the NYSE open (~11:xx ET), so every price is a **partial bar**. Flow/RS/OBV are settled 08-31.
> ⚠ **`vol_surge`-derived tags carry the SWEEP §3 caveat**: 88 names are accumulating and beating
> `SPY` over 20 sessions; only 6 carry 🟢, and the whole difference is 0.2 of surge.

---

## §0 · Company scoreboard consulted BEFORE any re-derivation — and it covers none of this sheet

`REPORT/COMPANY_SCOREBOARD.md` (2026-08-21, `company_batch` run 1) holds **5 rows, all KR**
(`036460` `PASS` 92.5 · `011200` `PASS` 79.5 · `316140` `HOLD` 76.2 · `028050` `HOLD` 64.7 ·
`000660` `PASS` 58.8; ENTER/ADD **0**).
⇒ **No US candidate on this sheet carries a scoreboard row**, so every US name below is **RE-DERIVED,
and the failing confirmation test is "no row exists"** — not a silent skip.
⚠ **"No row ≠ no coverage"**, so `module_report_tags ticker` was run before concluding: `AVGO` has a
dedicated `REPORT/company_AVGO` folder plus 2026-08-14 industry coverage; `MU` carries 2026-08-14
BLINDSPOT/EVENT_ALPHA/MACRO/DEEP_COMM coverage; `SLB` carries **08-31** ROTATION · EVENT_ALPHA ·
ACTION_TICKETS · DEEP_ENRG coverage. **All three are covered by industry files, none by a scoreboard
row** — the distinction is stated rather than collapsed.
⚠ **The scoreboard's own two rules are honoured**: the score is *research quality*, not expected
return, and **its #1 row is a `PASS`.** Nothing on this sheet is promoted by scoreboard rank.

## §0b · Candidate set — wide net, and where each name came from
**(DEEP thesis leaders) ∪ (`us_setup_screener` setups) ∪ (`US_LIVE_SHORTLIST`)**, per the rule.

- **DEEP leaders**: `MU` `SNDK` `LITE` (IT) · `SLB` `WMB` (ENRG) · `A` (HLTH) · `NEM` `FCX` (MATR,
  LATE-MONEY) · `WBD` `DIS` `T` (COMM).
- **`US_LIVE_SHORTLIST` (6 names, all included)**: `CRM` `INTU` `SLB` `A` `MSTR` `WMB`.
  ⇒ **`MSTR` is the only cross-sector shortlist name outside the DEEP set** — it gets its own row (§F).
- **`us_setup_screener --limit 300`**: 21 new names across 3 buckets.
  🚨 **`D304`-class caveat, stated up front**: the screener ran **on the 2026-09-01 LIVE partial bar**
  (`가격 확보 299/300`, header date 09-01, NYSE open). ⇒ **its RSI and `px/200` levels are NOT usable
  as levels**; it is used **only as a name list**. Two book names surfaced: **`HPE`** (bucket A,
  RSI 26.0, +55% vs 200DMA) and **`NUE`** (bucket A, RSI 31.3) — both **held**, both flagged, neither
  acted on.

---

## §A · INFORMATION TECHNOLOGY — memory suppliers + optical, from DEEP §9

### A-1 Numbers `[live]` (XBRL↔yfinance cross-checked 4/4 within 5% on every name below)

| | **`MU`** | **`SNDK`** | **`LITE`** | **`CRM`** | **`INTU`** | `AVGO` (held) |
|---|---|---|---|---|---|---|
| price / mcap | — / $1,279B | $1,532.37 / $224B | $862.98 / $77B | $259.22 / $213B | $352.42 / $96B | — / $1,957B |
| 52w range | — | **$50.07 – $2,354.39** | **$125.00 – $1,085.68** | $146.32 – $269.11 | **$252.84 – $705.08** | — |
| Trailing / **Fwd P/E** | 21.27 / **6.06** | 20.77 / **5.79** | — / **26.14** | 23.74 / **16.28** | 21.32 / **12.89** | 60.65 / **18.59** |
| PEG | **0.14** | — (blank, not guessed) | 0.63 | 1.05 | 1.10 | 0.42 |
| Price/Sales | 11.76 | 11.08 | **25.68** | 4.86 | 4.49 | 22.94 |
| **est. momentum, next-yr, 90d** | ★ **+50.9%** | ★ **+44.7%** | +17.4% | +2.2% | 🚨 **−11.3%** | +6.0% |
| est. momentum, current-yr | +25.9% | +22.1% | +19.5% | +14.0% | 🚨 **−10.8%** | +2.7% |
| target mean vs price | **+61.0%** | **+38.7%** | **+33.1%** | ⚠ **+1.3%** | +20.2% | +44.5% |

⚠ **`SNDK`'s PEG is blank in the source and is left blank** (`C3`). ⚠ **`LITE` has no trailing P/E** —
left blank, not imputed.

### A-2 The valuation discipline the desk's own rule demands (lens **B2**)
🚨 **`M1212` [measured] — `MU` (6.06×) and `SNDK` (5.79×) are the two lowest forward multiples on this
sheet AND the two steepest estimate revisions on it (+50.9% / +44.7% next-year, 90 days).**
That is the **peak-margin / low-multiple trap shape by definition** — a low multiple whose denominator
is being revised up that steeply is **consensus chasing**, not cheapness.
⚠ **The margin percentile for both is `unknown` (`C3`)** — no US gross-margin history is wired
(`scripts/margin_history.py` exits 1, PREFLIGHT G7). **Neither is called cheap on this sheet.**
★ **But the escape hatch was checked and it exists for `MU`** (§A-4), which is the whole reason the
name is here rather than in the reject ledger.
⚠ **The revision table is used ONLY as a description of the denominator's direction.** The desk's own
measurement (`measure_ic.py`, 2026-08-09) showed the "revisions lead price" claim **failed** and that
the effect is an **Information-Technology loading** — ex-IT Q5−Q1 **−1.1pp**. ⇒ **it carries zero
independent weight on any name in this section.** Stated because every name here is IT.

### A-3 Flow / positioning cross-read (settled 08-31)
| | flow | tag | OBV | `rs20` / `rs60` vs `SPY` | surge | Δ (08-27→08-31) |
|---|---:|---|---:|---:|---:|---:|
| `MU` | +0.270 | 🟡 | +0.095 | **+14.3** / −5.1 | 0.53 | **+0.255** |
| `SNDK` | +0.481 | 🟡 | +0.127 | **+20.4** / −12.3 | 0.79 | **+0.343** |
| `LITE` | +0.533 | 🟡 | **+0.284 매집** | **+16.1** / −4.5 | 0.76 | −0.017 |
| **`CRM`** | **+1.000** | **🟢** | +0.326 | **+37.3** / +35.1 | ★ **1.90** | — |
| **`INTU`** | **+0.831** | **🟢** | +0.148 | +11.6 / +17.7 | **1.34** | — |
| `AVGO` (held) | **−0.616** | 🔴 | −0.133 | −6.8 / **−12.9** | 0.90 | −0.099 |

`[FINRA 08-31]` `AVGO` short-vol **34.3%, z +0.02** (5v5 −4.1▼) — **no short pressure either way**;
`NVDA` 38.1% z +0.40. ⚠ **`[FINRA]` was NOT pulled for `MU`/`SNDK`/`LITE`/`CRM`/`INTU`** — stated as a gap.
`module_flow AVGO --positioning` **[live]**: P/C **1.73**, IV skew **−3.3**, short 1.2% float
**covering**, DTC 3.0, implied move **±9.6% (D1)**.

### A-4 Contract terms — read from the filing, per the desk's hard rule
- **`MU`: checked, and the band EXISTS.** `R111` established from the **FY26Q3 10-Q** that strategic
  customer agreements are **take-or-pay with binding multi-year volumes, a ceiling at ~the 2Q CY2026
  market price, and a floor for the term**, with management stating that at *floor* pricing gross
  margin runs above any prior cycle's peak. ⇒ ⚠ **the contract-price QoQ deceleration
  (+90~95% → +58~63% → +13~18%) is arithmetic hitting a cap, not demand weakening** — the desk's rule
  is to check for a band *before* reading a second derivative as demand, and the band is there.
- **`AVGO`: `unknown` (`C3`).** ⚠ `module_disclosure_us AVGO` was **not** called this run (the filing
  budget went to `SLB`). ⇒ **no "the margin must mean-revert" claim is made about `AVGO`**, and this
  is named as the single most valuable unopened document with a print in ≤48h.
- **`SNDK` / `LITE` / `CRM` / `INTU`: not read.** Marked `unknown`, and no mean-reversion claim is made.

### A-5 Refutation + dated catalyst
| name | what kills it | dated catalyst |
|---|---|---|
| `MU` | OBV turns 분산 **or** `rs20 < 0 vs SPY` on a settled close | **`MU` FQ4 print 2026-09-24**; `P111` settles 09-14 |
| `SNDK` | same as `MU`; and it is the **higher-beta expression** of one thesis — 52w range **$50 → $2,354** is the single widest on this sheet | — (no dated print found this run; **stated as a gap**) |
| `LITE` | OBV turns 분산 before 09-09 ⇒ `S137`-B, and `D250` should be **closed as not-a-gap** | **`S137` settles 2026-09-09** |
| `CRM` | ⚠ **consensus target is +1.3% above the live price** — the name has arrived where the analyst set is. `vol_surge` **1.90** is the board's highest = top-risk | — |
| **`INTU`** | 🚨 **it already is refuted on one axis**: estimates **−10.8% / −11.3%** over 90 days, and the stock is **−50% from its 52w high**. Its 🟢 sits on a **cut** estimate line | — |
| `AVGO` (held) | **`S138` ±11.00pp**, outside the ±9.6% priced move | **print 2026-09-02 or 09-03** ⚠ `D420` unresolved |

★ **`M1213` [measured] — the two 🟢 names on this sheet have the two weakest fundamental setups on
it.** `CRM`'s consensus target is **+1.3%** away and `INTU`'s estimates are being **cut double digits**,
while `MU`/`SNDK`/`LITE` — all 🟡 — carry **+61% / +38.7% / +33.1%** target upside and rising estimates.
⇒ **the 🟢 tag and the fundamental setup point opposite ways on this sheet**, which is what SWEEP §3
predicted mechanically: the tag is a `vol_surge` filter, and `vol_surge` is the axis this desk's own
IC ledger scores **negatively** (t(NW) −3.51, `market=kr`, `W1`-barred from acting on).

---

## §B · ENERGY — the chain-position leg, from DEEP §11

### B-1 Numbers `[live]`
| | **`SLB`** | **`WMB`** | `MPC` (held) | `PSX` (held) |
|---|---|---|---|---|
| price / mcap | $58.97 / $88B | $74.81 / $92B | $377.06 / $106B | — / $67B |
| 52w range | $31.64 – **$60.46** (within 2.5% of the high) | $56.09 – $80.08 | **$161.93 – $381.15** (within 1.1% of the high) | — |
| Trailing / **Fwd P/E** | 28.76 / **18.22** | 29.80 / **28.54** | 13.07 / **11.71** | — |
| PEG · P/S | 1.88 · 2.41 | 2.48 · **7.43** | 1.80 · 0.71 | — |
| Beta | — | — | **0.51** | — |
| **est. momentum, next-yr, 90d** | 🚨 **−3.5%** | +1.9% | ★ **+44.4%** | — |
| est. momentum, current-yr | 🚨 **−4.3%** | +1.7% | ★ **+81.9%** | — |
| target mean vs price | ⚠ **+5.0%** | +14.0% | 🚨 **−13.9% (BELOW)** | — |

### B-2 The two findings that cut against the sector's own best names
🚨 **`M1214` [measured] — `SLB` is the board's #3 flow name and one of only two `new_green` ignitions,
and its estimates are being CUT.** Current-year **−4.3%**, next-year **−3.5%** over 90 days, with the
consensus target only **+5.0%** above a price sitting **2.5% below its 52-week high**. ⇒ **the $3.4bn
AI-data-center bet (Kelvion, 08-31) is a story the estimate line has not yet accepted.**
🚨 And the **primary-source counterweight from DEEP §4**: `SLB` filed **three Rule 144 proposed-sale
notices and three Form 4s on 08-26 / 08-27 / 08-31** — the exact window it ignited. ⚠ Rule 144 is a
notice of intent and share counts were not read.

🚨 **`M1215` [measured] — `MPC` is the sheet's clearest peak-margin/low-multiple case and its
consensus target is BELOW its price.** Forward **11.71×** on a current-year estimate revised **+81.9%
in ninety days (12↑ / 0↓)**, price within **1.1%** of a 52-week high, target mean **−13.9% below**.
⚠ Margin percentile `unknown` (`C3`) ⇒ **not called cheap.** And **`M831` already established from the
10-Q that refining has NO take-or-pay** — the contractual escape hatch that saves `MU` does **not**
exist here (lens **B2** applies in full).

### B-3 Flow / positioning (settled 08-31)
`SLB` **+0.822 🟢** OBV **+0.498** (sector-high) · `rs20` **+20.6 vs `SPY`** · surge **1.28** · Δ +0.25 ·
★`new_green` — `[FINRA]` short-vol **62.1%, z +1.13, 5v5 +8.7▲**.
`WMB` **+0.710 🟢** OBV +0.219 · `rs20` +5.3 · surge **1.28** · **Δ +0.46** · ★`new_green`.
`MPC` +0.711 🟡 OBV **+0.427** · **+20.4 / +38.5** — `[FINRA]` **74.5%, z +2.90 🔴** (shorts pressing in).
`PSX` +0.617 🟡 OBV +0.183 · +18.4 / **+32.6** — `[FINRA]` 59.1%, z +0.87.
⚠ **`SLB` chart (`module_chart`, restored today)**: **RSI in the >70 overbought band** while OBV-20d
has just turned positive — extended-but-live, with overbought as the near-term caution.

### B-4 Competition / peers
`SLB` vs `BKR` (+0.251 🟡, `rs60` −5.2 vs `SPY`) — **`SLB` is winning the services node outright.**
`WMB` vs `OKE` (+0.522, Δ +0.46) vs `KMI` (+0.322, surge 1.11) vs `TRGP` (+0.154, OBV −0.046) —
**midstream is broadly positive with `WMB` the only 🟢**; `KMI`'s **$35.67B RPO** is the desk's own
benchmark for a contracted floor.
`MPC` vs `PSX` vs `VLO` (+0.550, `rs60` **+37.3**) — **the three refiners are one trade**, `rs60`
+38.5 / +32.6 / +37.3, spread only 5.9pp.

### B-5 Refutation + dated catalyst
| name | what kills it | dated catalyst |
|---|---|---|
| `SLB` | estimates keep falling while flow holds ⇒ the ignition is positioning, not earnings. **Or** `P122`-B (`CL=F` ≤ 80.00) | **`P122` settles 2026-09-08** · `S136` 09-09 |
| `WMB` | forward **28.54×** on **+1.9%** estimate growth is the sheet's weakest growth-vs-multiple pair — a de-rating needs no bad news | `S136` 09-09 |
| `MPC` · `PSX` (held) | `P122`-B, or `S136`-B (`≤ −3.90pp`) which would say the chain-position split was a pre-event artifact | **`S136` settles 2026-09-09**; `MPC` next print **2026-11-03** |

---

## §C · HEALTH CARE — one name, from DEEP §8

**`A` (Agilent)** — the sector's **only 🟢**, and the shortlist's only HLTH row.
**Numbers `[live]`**: price **$151.98** (52w 108.35–163.75) / $43B · Trailing 29.98 / **Fwd 22.47** ·
PEG 1.41 · P/S 5.81 · **estimates +2.6% current-yr / +2.3% next-yr** (flat, neither chasing nor cut) ·
target mean **+14.8%**.
**Flow (08-31)**: +0.817 🟢 · OBV **+0.240** with `rs20` **+8.6 vs `SPY`** (RULE D6 — paired) ·
`rs60` +9.7 · surge **1.27**.
**§D peers**: `WAT` +0.478 (OBV +0.339) · `TMO` +0.424 (`rs60` **+26.7**) · `DHR` +0.376 — ★ **the
whole life-science-tools node is positive**, and DEEP §5 measured that its *customers* (the biotech
node) are uniformly accumulating. **This is the only name on the sheet where node and customer flow
were both measured and agreed.**
**§E refutation**: `A`'s surge falling below 1.0 ⇒ the sector loses its only ignition. **Contract
terms `unknown` (`C3`)** — no filing opened; no mean-reversion claim made. ⚠ `[FINRA]` short-z not
pulled. **Dated catalyst**: none found this run — **stated as a gap**, not invented (`D2`).

---

## §D · MATERIALS — LATE-MONEY, nothing handed forward

**`NEM`** (+0.772, rank 6 of 299) and **`FCX`** (+0.700) are the sector's only positive leg.
**Not handed to any candidate list**, for reasons DEEP measured, not asserted:
1. **`NEM`'s revenue QoQ rate decelerated twice then went negative** (+23.6% → +7.2% → **−16.3%**),
   which is lens **B1**'s signal (`C2`: the same quarter is **+15.06% YoY**).
2. **Copper spec positioning is at the 100th percentile of its year** `[COT 08-25]` — the most crowded
   reading on the board.
3. `NEM`'s consensus target is only **+7.2%** above the price; forward 12.29× with margin percentile
   **`unknown` (`C3`)** ⇒ not called cheap.
4. **Neither carries 🟢** — both missed the tag by **0.01–0.14 of `vol_surge`**, and `NEM` is **already
   filed to `missed_ledger`** (`M.숏리스트탈락`, enters-if surge ≥1.20 with 매집 and `rs20` > 0 vs
   `SPY`, recheck **2026-09-08**).
⚠ **`NUE` (held)** is the book's only Materials exposure and reads **−0.482 🟡, Δ −0.452**, i.e. the
sector's 2nd-worst row. It also appeared in the screener's leader-pullback bucket (RSI 31.3 `[live]`).
**Flagged; no action language** (P4).

---

## §E · COMMUNICATION SERVICES — the correction, and why nothing is handed forward

★ **DEEP measured that Alphabet occupies 76.6% of this bucket under TWO tickers** (`GOOGL` 38.3% +
`GOOG` 38.3%), that the one-name guard removes only one class, and that **ex-Alphabet the sector's
`wflow` is +0.144, not −0.547** (`M1206` / `D459`).
⇒ **The sector reads positive underneath its headline**, and its two best rows are **`WBD` +0.539
(OBV +0.444, `rs20` +8.1 vs `SPY`)** and **`DIS` +0.500 (OBV +0.476, `rs20` +8.4)** — the two highest
OBV readings in the bucket.
**Neither is handed forward**: both are 🟡, neither cleared the shortlist, and **no fundamentals were
pulled for either this run** (stated as a gap, not covered with a narrative).
⚠ **`T`** — carried in `C23`/`M1130` as **~13.6% of real invested capital with no thesis attached** —
is this sector's **4th-best flow row** (+0.350, OBV +0.269, `rs60` **+12.4 vs `SPY`**) and sits in its
**only contractually-protected node**. **The gap now has a candidate thesis; assigning one is a human
call (P5).**

---

## §F · CROSS-SECTOR LIVE SHORTLIST — the one name outside the DEEP set

**`MSTR` (MicroStrategy, Financials)** — `US_LIVE_SHORTLIST` row, **+0.811 🟢**, OBV **+0.482**,
`rs20` **+38.9 vs `SPY`** (the 2nd-highest 20-day in the universe), surge 1.26,
`[FINRA]` verdict **✅ low-short / short-covering (clean rise)**.
🚫 **Set aside, and filed to the rejection ledger with a class and both required fields** (§H).
**Reason**: it is a **bitcoin-beta vehicle**, not a Financials thesis — the desk carries **no crypto
proposition**, its flow is a **derivative of an asset the desk does not model**, and DEEP measured that
`Financials`' only green of 47 is *"bitcoin beta"* (the 08-22 `M805` observation, reproduced).
⚠ **This is a rejection, not a miss** — a reason was stated and the name was set aside.

---

## §G · Epicenter-starter module — NOT required this run
`cycle_exposure` reports **no top-rank cycle GAP** (AI-compute epicenter **16.85%** vs need ≥12.0;
Energy/refining **10.28%** vs ≥8.0). ⇒ **no epicenter-starter is owed.**
⚠ But **two cycles cannot be measured at all** — AI-power/grid (`D416`) and optical (`D250`, 17th run)
have **no ranked registry row**, so *"the book holds 0% of those layers"* is **unstatable, not zero**.
★ This run bracketed both directly instead of waiting for the registry: **`P123`** (power, settles
09-08) and **`S137`** (optical, 09-09).

## §H · Ledger discipline — what this sheet set aside, and what it never reached

**Rejections filed this run** (`reject_ledger.py add`, both `--revives-if` and `--recheck-date` set):
| ticker | class | why | revives-if | recheck |
|---|---|---|---|---|
| `RTX` (Driscoll thread) | `K.본문반증` | body-read named no program/budget change (EVENT_ALPHA §9) | a named US Army program cancellation/restructuring reported by ≥2 independent foreign outlets | 2026-09-15 |
| **`MSTR`** | `L.vehicle없음` | 🟢 flow is bitcoin beta; the desk carries no crypto proposition and does not model the underlying | the desk registers a crypto/digital-asset proposition, **or** `MSTR` shows `rs20` > 0 vs `SPY` **while** BTC is flat-to-down over the same 20 sessions (i.e. the beta detaches) | 2026-09-22 |

**Missed entries filed this run** (`missed_ledger.py add`, `--enters-if` + `--recheck-date`, `--sample prospective`):
`NEM` (`M.숏리스트탈락`, surge 1.19 vs a 1.20 bar) · `MPC` (`M.숏리스트탈락`, surge 1.08; the
2026-07-21 refiner tag artifact reproducing) — both recheck **2026-09-08**.

⚠ **No name was removed on narrative grounds while its measured flow still passed.** The one candidate
that fits that description — **`MRVL`** (`vol_surge` 1.11, `rs20` +8.0 vs `SPY`, but the **worst
5-session performer of the 56** and OBV **−0.013 = flat**) — is **not removed**: it is carried in
`SECTOR_DEEP_IT §3b` with its own thesis line (*"volume arriving into the deepest-discounted large-cap
semi four sessions before `AVGO` prints"*) and a dated re-check at the `AVGO` print. **It fails the
🟢 gate's conviction leg (OBV flat), so it is not a candidate — and it is not deleted either.**

⚠ **The screener's 21 new names were NOT individually ledgered.** Reason, stated rather than skipped:
the screener ran on a **live partial bar** (`D304`), so its levels are unusable, and filing 21 rows
whose triggering numbers are known-bad would pollute the ledger. ⇒ **the list is recorded here in
full** — `MMM ITW HPE PNC ROST D NUE STLD APP NKE PDD VST IBM TJX CARR RCL FER TTWO SHW HBAN PCG` —
**and re-running the screener on a settled bar is a dig for the next run.**

## §I · Sizing language vs the exposure state
`exposure_rule state` = **정상 (normal)**; target invested **95%**, actual **85.2%**, band gap
**−9.8pp**, **13th consecutive session outside the band**.
🚨 **The state is `정상`, not `복귀`**, so this sheet is not required to supply enough candidates to
close the gap — **and it could not**: the sheet carries **6 candidate rows** against a −9.8pp shortfall.
⚠⚠ **And the two numbers are about different books** (`C23`/`M1169`): `exposure_rule` reads the **KR
contest/timefolio** book at 85.2%, while `cycle_exposure` reads the **real KIS** account at
**53.0% cash** ($5,841 of $11,012). **Any sizing sentence downstream must name its book on the same
line.** **This sheet issues no sizing** (P4).

## ✅ EXIT CHECK
- [x] **Company scoreboard consulted before any re-derivation** (§0) — 5 rows, all KR, **zero US**;
      every US name marked RE-DERIVED with the failing test named ("no row exists"), and
      `module_report_tags ticker` run before calling anything un-researched. **No matured observation
      point on any cited row** (all 5 KR rows belong to the KR desk).
- [x] Every DEEP sector has a section (§A IT · §B ENRG · §C HLTH · §D MATR · §E COMM); the
      cross-sector LIVE shortlist name (`MSTR`) is **included and explicitly rejected with a reason**
      (§F/§H).
- [x] Numbers cross-checked (XBRL↔yfinance 4/4 within 5% on every name pulled); **blanks are blanks**
      (`SNDK` PEG, `LITE` trailing P/E, `PSX` fundamentals not pulled) — none guessed.
- [x] Flow/positioning cross-read present per candidate; **written as ONE file**.
- [x] **Every set-aside name is in the rejection ledger with a class AND a `--revives-if` AND a
      `--recheck-date`** (§H, 2 rows). No permanent bans filed.
- [x] **No name removed on narrative grounds while its measured flow passed** — `MRVL` is re-filed
      with a new thesis line and a dated re-check rather than deleted (§H).
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** (§H, 2
      rows, `--sample prospective`). The 21 screener names are **not** filed, **with the reason stated**.
- [x] **Sizing language consistent with the exposure state** (§I) — state is `정상`, the sheet states
      plainly that it **cannot** fill a −9.8pp gap with 6 rows, and names the two-book problem.
- [x] **Linter run on this stage's own output** — `report_lint.py .../BET_SHEET.md` ⇒ **0 findings** (C1·C2·S6·D6), and `module_math_check` ⇒ **ALL MATH CHECKS PASSED**. ⚠ Form only; a clean run is not a correct sheet.

---
> Next: `python pipeline/run_protocol.py industry_us --next` → **ALPHA** (Stage 10).
> ⚠ ALPHA inherits: `M1213` (the two 🟢 names have the weakest fundamentals on the sheet) and `M1214`
> (`SLB`'s estimates are being cut while its flow ignites) — both are **freshness/quality** questions,
> which is §B's job.


---

# §B · ALPHA FRESHNESS TAGS — written by Stage 10 (L1·ALPHA), 2026-09-01

> Freshness is `theme_age --scope foreign` (deterministic, token-0) **first**, then the live
> cross-read. 🟢LIVE = FRESH theme (≤14d **and** accel ≥2×) with money already arriving ·
> 🟡PARTIAL = a dated appointment with a stated residual · 🔴RESOLVED = dropped **and ledgered**.

## §B-0 🚨 The G1 check, run BEFORE any freshness verdict — and it PASSES

The protocol bars this stage from issuing a freshness verdict at all when PREFLIGHT **G1** fails,
because *"a dead pipe and a quiet theme return the identical value."* **The pipe was probed, not
assumed:** 6/6 pre-sweep counts, 4/4 post-sweep, **10/10** direct `news_velocity` falsification
including the universe's two lowest-ranked names (`PCAR` 1.29, `JCI` 1.07) and one at **3.07** (`AON`),
with every headline count **above** yesterday's.

★★ **`M1216` [measured] — and this run can do better than a liveness probe: it produced TWO 🟢FRESH
readings on the same board.**

| theme | verdict | age | 7d avg | accel | base |
|---|---|---:|---:|---:|---:|
| **`ghost demand`** | ★ **🟢FRESH** | **0** | 0.4 | — | **3** |
| **`Kelvion`** | ★ **🟢FRESH** | **1** | 1.7 | — | **12** |
| `Larak Island` | 🟡ACCELERATING | 36 | 22.6 | ★ **61.56×** | 169 |
| `Lambda` | 🟡ACCELERATING | ≥90 | 4.3 | 4.29× | 78 |
| `Ternus` | 🟡ACCELERATING | ≥90 | 28.0 | 4.14× | 474 |

⇒ **`F1` is arithmetic on this board, and it is now DEMONSTRATED rather than inferred.** The gate can
fire; the desk's bet themes simply are not fresh. This closes, for the US side, the doubt the protocol
raised about eighteen KR observations taken on an uninterrogated counter.

⚠⚠ **Two honest caveats on the demonstration itself:**
1. **Both 🟢FRESH terms have bases of 3 and 12 articles.** A freshness gate that fires at **n=3** can
   fire on noise. **Neither is treated as a tradeable theme**, and `Kelvion` is a deal name, not a theme.
   ⇒ **`D461`**: *`theme_age` reports a minimum base alongside its verdict; a 🟢FRESH on n<25 is
   labelled `FRESH-but-thin` rather than entering the freshness gate.*
2. ★ **The one genuinely new thing on this board is a FALSIFIER, not a thesis.** `ghost demand` is the
   Texas data-center-power halt (EVENT_ALPHA Card 5) — it argues **against** the AI-power leg and
   against `P123`-A. **The freshest information in the corpus is bearish for the story the desk was
   closest to adopting**, and that is recorded here rather than left in a card.

## §B-1 The bet themes — every one is ⚪ECHO

| theme | verdict | age | 7d avg | accel | base | rides |
|---|---|---:|---:|---:|---:|---|
| `memory chip shortage` | ⚪ECHO | ≥90 | 4.6 | 1.32× | 229 | `MU` · `SNDK` |
| `optical transceiver` | ⚪ECHO | ≥90 | 2.3 | **0.67× (decelerating)** | 155 | `LITE` |
| `AI data center` | ⚪ECHO | ≥90 | 92.1 | 1.03× | **5,337** | `SLB` |
| `refining margin` | ⚪ECHO | 75 | 4.9 | **0.72× (decelerating)** | 297 | `MPC` · `PSX` (held) |
| `gold price` | ⚪ECHO | ≥90 | 29.3 | 0.91× | 1,852 | `NEM` |

⇒ **ZERO 🟢LIVE — the 11th consecutive US run.** ⚠ **ECHO/FADING theses need *stronger* live evidence
to survive**, and that requirement is applied name by name below.

## §B-2 Tags

| name | tag | evidence label + date | residual | **re-check date** |
|---|---|---|---|---|
| **`MU`** | **🟡PARTIAL** | theme ⚪ECHO 1.32× — **but the corroborator is one day old and from the BUYER side**: *"Tim Cook's last warning as Apple CEO was that memory chip shortages won't improve any time soon"* [nasdaq · yahoo_finance · fool, **2026-09-01**], thread **BUILDING 7→8→6→4→3→14→21**. Flow 08-31: OBV **+0.095 매집** with `rs20` **+14.3 vs `SPY`**, **Δ +0.255** | the theme is consumed while the evidence is new; needs the supplier leg to be **paid**, not just corroborated | **2026-09-14** (`P111`) → **2026-09-24** (`MU` FQ4) |
| **`SNDK`** | **🟡PARTIAL** | same theme, same date. Flow: OBV **+0.127 매집**, `rs20` **+20.4 vs `SPY`**, **Δ +0.343** | **no dated catalyst of its own was found** (stated as a gap, not invented). It is the higher-beta expression of one thesis — 52w range **$50.07 → $2,354.39** | **2026-09-24** (rides `MU`'s print) |
| **`LITE`** | **🟡PARTIAL** | theme ⚪ECHO and **DECELERATING (0.67×)** — the weakest freshness on the sheet. Flow 08-31: OBV **+0.284 매집** (sector-high) with `rs20` **+16.1 vs `SPY`** | ⚠ **a decelerating theme demands stronger live evidence**, and the live evidence is the *partner leg collapsing*: `COHR` Δ **−0.805**, the worst in the 299-name universe | **2026-09-09** (`S137`) |
| **`SLB`** | **🟡PARTIAL** | theme ⚪ECHO 1.03× on a **5,337-article base** = maximally consumed. `Kelvion` 🟢FRESH but **n=12 and it is a deal name**. Flow 08-31: **+0.822 🟢**, OBV **+0.498** with `rs20` **+20.6 vs `SPY`**, ★`new_green` | ⚠ **three named residuals**: estimates are being **CUT** (−4.3% / −3.5%, 90d); consensus target only **+5.0%**; **three Rule 144 proposed-sale notices + three Form 4s on 08-26/27/31**. ⚠ **RSI >70 overbought** on the restored chart | **2026-09-08** (`P122` · `P123`) |
| **`WMB`** | **🟡PARTIAL** | no theme carries it (stated). Flow 08-31: **+0.710 🟢**, surge **1.28**, **Δ +0.46**, ★`new_green` | forward **28.54×** against **+1.9%** estimate growth is the weakest growth-vs-multiple pair on the sheet — a de-rating needs no bad news | **2026-09-09** (`S136`) |
| **`CRM`** | **🟡PARTIAL** | no theme pulled. Flow 08-31: **+1.000 🟢**, OBV **+0.326** with `rs20` **+37.3 vs `SPY`**, surge **1.90 — the board's highest** | ⚠ **the consensus target is +1.3% above the live price** — the name has arrived where the analyst set is | **2026-09-08** (`S140`) |
| **`INTU`** | **🟡PARTIAL** ⚠ **downgraded from its 🟢 flow tag** | Flow 08-31: **+0.831 🟢**, surge 1.34. **But its accumulation axis is C-grade OBV only (+0.148)** and the fundamental axis points the other way: estimates **−10.8% current-yr / −11.3% next-yr** over 90 days, and the stock is **−50% from its 52w high ($705.08 → $352.42)** | 🚨 **the 🟢 sits on a CUT estimate line.** Per the D6 grading rule a C-grade disagreement downgrades to 🟡 and is **reported as a disagreement**, not converted into a tape trade | **2026-09-15** — residual: estimate revisions must stop falling |
| **`A`** | **🟡PARTIAL** | no theme; no dated catalyst found (**stated as a gap**). Flow 08-31: **+0.817 🟢**, OBV **+0.240** with `rs20` **+8.6 vs `SPY`**, surge **1.27**. ★ Its customer node (biotech) is uniformly accumulating | ⚠ `[FINRA]` short-z **not pulled**; contract terms `unknown` (`C3`) | **2026-09-14** (`S133`) |
| `AVGO` **(held)** | **🟡PARTIAL — held-name watch, not a bet** | Flow 08-31 **−0.616 🔴**, OBV −0.133, `rs60` **−12.9 vs `SPY`**; estimates **flat** (+2.7% current-yr) ⇒ a **multiple de-rating, not a downgrade cycle** | prints in ≤48h; **`S138` ±11.00pp is the informative row and `S132` ±9.00pp is NOT** (inside the ±9.6% priced move) | **first settled close after the print** |

**🔴RESOLVED this run: none.** No bet's catalyst has fired and no thesis went to consensus.

## §B-3 Momentum-only and positioning stamps
- **Momentum-only flag: NOT triggered on any tagged name.** Every 🟡 above has OBV ≥ 0 **and**
  `rs20` > 0 vs `SPY` — the accumulation axis agrees with the tape in all eight cases. ⚠ Where a
  disagreement exists it is **fundamental**, not accumulation (`INTU`, `SLB`, `CRM`), and each is
  reported as a disagreement rather than converted into a trade.
- **D6 grading applied explicitly**: every accumulation read on this sheet is **C-grade (OBV only)** —
  the US has **no investor-type feed** (no KR-KIS equivalent), so no A-grade read exists for any US
  name by construction. ⇒ **no bet is upgraded on accumulation alone anywhere on this sheet.**
- **Positioning gate (US)**: no ⚡crowded-short name is tagged. `MSTR` carried the sheet's only
  ✅low-short/short-covering verdict and was **rejected at BET** on vehicle grounds (§F/§H).
  ⚠ **`MPC` (held) is the inverse case** — `[FINRA]` short-vol **z +2.90 🔴**, shorts pressing into a
  +2.69% session. **Stamped: hard-stop required if this is ever expressed as an add** (P4 — no sizing here).

## §B-4 Carry-forward list — tags follow the NAME, not the sector's turn
Per the 006360 precedent, these are carried into the next run's inheritance packet **regardless of
whether their sector holds a DEEP slot**:
**`MU` · `SNDK` · `LITE` · `SLB` · `WMB` · `CRM` · `INTU` · `A`** (8 tagged) **+ `AVGO`** (held-name watch).
⚠ **`IT` and `ENRG` may both lose their slots next run** (`ENRG` is already at a 0-run recency
violation) — **the tags do not lapse with them.**

## §B-5 Names carried into ALPHA that received NO tag — ledgered, not dropped
| name | why no tag | ledger row |
|---|---|---|
| `DIS` | COMM: OBV **+0.476** with `rs20` +8.4 vs `SPY`, 2nd-highest OBV in the sector — but **no fundamentals pulled and no dated catalyst** this run | ✅ `missed_ledger` `Q.확신부족`, enters-if *"COMM read ex-Alphabet (`D459`) AND `DIS` holds 매집 with `rs20` > 0"*, recheck **2026-09-15** |
| `WBD` | COMM: OBV **+0.444** (sector-high), `rs20` +8.1 — same reason | ✅ `missed_ledger` `Q.확신부족`, same enters-if, recheck **2026-09-15** |
| `FCX` | MATR: +0.700, OBV +0.202 매집, `rs20` +17.8 — **avoided on the THEME's crowding (copper spec 100th %ile), not on the name** | ✅ `missed_ledger` **`S.테마회피`**, enters-if *"copper spec 1-yr %ile < 80 while `FCX` holds 매집 and `rs20` > 0"*, recheck **2026-09-15** |
| `NEM` | filed at EVENT_ALPHA (surge 1.19 vs a 1.20 bar) | ✅ `missed_ledger` `M.숏리스트탈락`, recheck **2026-09-08** |
| `MPC` | filed at EVENT_ALPHA (surge 1.08; the 2026-07-21 refiner tag artifact) | ✅ `missed_ledger` `M.숏리스트탈락`, recheck **2026-09-08** |
| `T` | ⚠ **not ledgered, and the reason is that it is HELD with no thesis** (`C23`/`M1169`, ~13.6% of real invested capital). A missed-entry row would mis-file a position the desk already owns. **Named here instead, and handed to the human decision `C23` already carries.** | — |

**Total this run: 2 rejections (`RTX`-thread, `MSTR`) · 5 missed entries (`NEM` `MPC` `DIS` `WBD` `FCX`).**
The funnel is scored on both sides.

## §B-6 🚨 SELF-REFUTATION — two tags above are WITHDRAWN, and the earlier rows are left standing

> Appended at the run-end handoff step, after `reject_ledger.py list` was read directly.
> **The §B-2 rows are NOT edited away** (`D48` / §4c) — the mistake stays visible beside its correction.

**`M1219` [measured] — this run tagged two names that were already carrying STANDING rejections from
its own previous run, and nothing in the pipeline stopped it.**

| name | standing rejection | revival condition | today's check | verdict |
|---|---|---|---|---|
| **`CRM`** | **2026-08-31 · `B.모멘텀only`** — *"flow at the +1.000 score cap but its catalyst already fired 2026-08-27; +1q EPS −2.3%, upside +1.9%, +41.7% above its 50DMA"* · recheck **2026-09-30** | *"`rs20` > +20 vs `SPY` **AND** a new dated catalyst inside 30 days"* | `rs20` **+37.3 vs `SPY`** ✅ clears the first conjunct — but **§B-2's own row says "no theme pulled" and lists NO dated catalyst** ❌ | 🚫 **Revival condition NOT met (1 of 2 conjuncts). The 🟡PARTIAL tag is WITHDRAWN; `CRM` remains 🔴 rejected until 09-30.** ★ And the un-met conjunct is the *same* objection: consensus target **+1.3%** away, i.e. the 08-31 row was right and this run re-discovered its evidence without recognising it |
| **`INTU`** | **2026-08-31 · `G.섹터중립`** — *"🟢가속 but no sector mandate reaches it (IT is N and routed to PREMORTEM), and it is the only shortlist name without short-side confirmation (FINRA z +0.20)"* · recheck **2026-09-30** | *"`IT` returns to **OW** OR short-vol z < −1.0"* | **`IT` was NOT promoted** — ROTATION declined `IT N → OW` on `eqflow` −0.014 and routed it to PREMORTEM for a **3rd** run ❌ · **`[FINRA]` z was not pulled for `INTU` this run** (stated as a gap in §A-3) ❌ | 🚫 **Revival condition NOT met on either leg. The 🟡PARTIAL tag is WITHDRAWN; `INTU` remains rejected until 09-30.** ★ And this run independently found a *third* reason (estimates **−10.8% / −11.3%**) that the 08-31 row did not have |
| **`MSTR`** | rejected **three times already** — 08-24 `C.차트붕괴` · 08-26 `H.밸류소진` · 08-31 `L.vehicle없음` | — | this run filed a **fourth** row (09-01 `L.vehicle없음`) | ⚠ **Duplicate filing.** The decision was correct and the reason is the same as 08-31's; the row is redundant, is left in place (the ledger is append-only), and is named here rather than quietly tolerated |
| `LITE` | 08-31 → **`missed_ledger` `Q.확신부족`** (not a rejection) | — | — | ✅ **A miss row is not a ban.** `LITE`'s 🟡PARTIAL tag **stands** |

### What let this through — and it is a real gap, not carelessness
`reject_ledger.py due` ran at HANDOVER and returned **0 rows / 0 legacy**, correctly: `due` surfaces
rows whose **recheck date has passed**. Both `CRM` and `INTU` recheck on **2026-09-30**, so `due` was
silent — **and silence from `due` reads identically to "this name is clear."**
⇒ **`D463`**: *before ALPHA issues a freshness tag, each candidate is checked against the ledger's
**standing** rejections (`reject_ledger list`), not only against `due`. `due` answers "what is owed a
re-check"; it does not answer "is this name currently rejected."*
★ This is the same failure shape the desk logged for `F1` and for `D16`: **an instrument's zero was
read as evidence about the world instead of as a property of the question it answers.**

### Corrected tag summary
**🟡PARTIAL: 6** — `MU` · `SNDK` · `LITE` · `SLB` · `WMB` · `A` (+`AVGO` as a held-name watch).
**🔴 standing-rejected, tags withdrawn: 2** — `CRM` · `INTU`, both revive **2026-09-30**.
**🟢LIVE: 0** — the 11th consecutive US run, and §B-0 demonstrates that zero is arithmetic.
⚠ **§B-4's carry-forward list is corrected to 6 names + `AVGO`**; `CRM` and `INTU` carry forward as
**rejections with dates**, not as tags.
