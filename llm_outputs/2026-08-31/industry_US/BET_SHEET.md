# BET_SHEET — industry_US · 2026-08-31 (Mon) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks glob this exact filename — never split it.
> **Analytical only. Zero buy/sell recommendation.** Sizing language below is *influence
> illustration*, never an instruction.
> All flow `repaired sweep, asof 2026-08-28`; Δ = `08-27 → 08-28, 3-axis nonews`; 08-28 prices are
> **5m-proxy (err ≤0.05%)**; every relative figure names `SPY` inline (`C1`).

---

## §0 · Gates that bind this sheet

### 0a · Thesis-confirmation gate — the scoreboard was consulted first

`REPORT/COMPANY_SCOREBOARD.md` (2026-08-21, `company_batch` run 1) holds **5 rows, all KR**
(036460 · 011200 · 316140 · 028050 · 000660). **Zero US names.**
⇒ **No candidate on this sheet carries a scoreboard row**, so nothing here is a CONFIRM-by-citation
and nothing is a silent re-derivation. **The gate was run and returned empty; that is stated rather
than skipped.** ⚠ The scoreboard is also **10 calendar days old**, past the 10-settled-session
freshness bar, so even a matching row would have failed the **age** test.
⚠ **"No row ≠ no coverage"** — `module_report_tags ticker` was queried per candidate: `SLB`, `COP`,
`VLO`, `ETN`, `NUE`, `LIN` all carry prior desk coverage; **`A` (Agilent) returns
*"no report has covered it"*** and is flagged as such in §HLTH.

### 0b · Instrument revocations still binding (from `PREFLIGHT` + `SWEEP`)

🚫 Primary `SECTOR_FLOW_US.json` is empty · 🚫 no `wflow` promotion/demotion of IT, ENRG, DISC ·
🚫 no sweep-sourced velocity or "quiet" claim · 🚫 no 08-28 close from the daily endpoint/book/`pulse`
· 🚫 no US chart-shape verdict (`module_chart` 0/3) · 🚫 no 08-31 settled-tape claim.

### 0c · 🚨 A new instrument measurement made by THIS stage, before its own screener output is used

`us_setup_screener.py:105` runs `sub.dropna(subset=["close"])`. With the 08-28 Close still `NaN` for
301/301 tickers, that line **deletes the 08-28 bar entirely**; and the 13-month download now also
carries a **live, unsettled 08-31 bar**. Verified directly on two of its own outputs:

| ticker | last four bars the screener actually sees | closes |
|---|---|---|
| `NUE` | **2026-08-25 · 08-26 · 08-27 · 08-31** | 247.55 · 252.80 · 252.37 · **251.42 (live)** |
| `LLY` | **2026-08-25 · 08-26 · 08-27 · 08-31** | 1,233.66 · 1,189.41 · 1,176.10 · **1,154.29 (live)** |

⇒ 🚨 **Every RSI and every `px/200` in §MATR/§HLTH/§INDU below is computed on a GAPPED series that
omits 08-28 and TERMINATES ON AN UNSETTLED INTRADAY BAR.** This is worse than the 08-30
characterisation (`C21`: *"computed to 08-27"*) — it is 08-27 **plus a live bar with a hole between
them**. **The screener's rows are used only to widen the candidate net, never as a level or a
trigger**, and every one of them carries this label.
⇒ **`D438` registered**: *a screener whose loader drops NaN rows must report its own series'
last-bar date and gap count, because dropping a void bar and appending a live bar are two defects
that cancel in the row count and compound in the value.*

### 0d · 🚨 Which book — every sizing line must name it (`C23`, unresolved, human call)

| book | invested | cash | names |
|---|---|---|---|
| **REAL KIS account** | **$5,188.76 of $11,045.42** | **53.0%** | 8 US (`NVDA`·`ANET`·`ETN`·`MPC`·`PSX`·`RTX`·`CBRE`·`T`) |
| `module_paper_book` | — | — | 13 (11 US + 2 KR) |
| `exposure_rule` ledger (KR contest) | **85.3%** vs a **95% target** ⇒ **−9.7pp band gap** | — | — |

**Exposure state = `정상` (normal), rule fired nothing.** ⚠ It is **not** `복귀`, so this sheet is
**under no obligation to supply enough candidates to reach a target** — that clause does not bind
today, and saying so is the honest reading rather than manufacturing candidates to fill a gap.
⚠ `exposure_rule state` printed **"투자비중 미상"** while `show` carries 85.3% — the two lines
disagree about whether the weight is known; reported as read, not substituted (P5).

### 0e · Cycle-exposure / epicenter-starter module — **no GAP, so no starter is required**

`cycle_exposure.py` (REAL book): AI-compute epicenter **16.91%** vs a 12.0% floor · Energy/refining
**10.17%** vs 8.0% · missile-defence 3.82% (no floor). **No rank≤2 GAP ⇒ the epicenter-starter module
does not fire this run.** ⚠ Three stated weaknesses in that verdict (`BLINDSPOT_PREMORTEM` Lens 4):
AI-power and optical have **no registry row at all** (so 0% is unstatable, not measured); **`TSM` and
`SMCI` are outside the universe**; and the verdict covers **one of three books**.

---

## §ENRG — Energy (DEEP rotating R1)

### §A · Numbers

| | **SLB** | **COP** | **VLO** | **MPC** *(held)* | **PSX** *(held)* |
|---|---:|---:|---:|---:|---:|
| price | 60.14 | 132.94 | 358.39 | 372.94 | — |
| forward P/E | 18.61 | 13.95 | **11.70** | **11.58** | — |
| trailing P/E | 29.33 | — | 14.93 | 12.93 | — |
| P/B | 3.42 | 2.44 | 4.13 | 5.53 | — |
| beta | 0.749 | **0.123** | 0.554 | 0.508 | — |
| dividend yield | 2.06% | — | 1.36% | 1.08% | — |
| 52-week range | 31.64–**60.46** | 85.57–**135.88** | 151.25–**362.79** | 161.93–**376.05** | — |
| distance to 52w high | **−0.5%** | −2.2% | **−1.2%** | **−0.8%** | at the high |
| consensus upside | **+3.0%** | +9.3% | 🚨 **−11.3%** | 🚨 **−13.0%** | — |
| revenue QoQ series | −7.3·+0.7·+4.5·−2.3·**+2.9** | +26.7·−15.2·+7.3·+4.9·**+21.6** | +7.6·−5.6·+6.6·**+37.4** | −10.2·+7.2·+3.0·−1.7·**+52.0** | — |
| 0q EPS 90-day | 🚨 **0.691→0.621 = −10.1%** | 2.569→2.624 = +2.1% | **8.53→16.20 = +90%** | **8.59→19.49 = +127%** | — |
| 0q revision breadth | 🚨 **3 up : 14 down** | 5 up : 5 down | **15 up : 0 down** | **14 up : 0 down** | — |
| +1q revision breadth | 🚨 **1 up : 14 down** | **8 up : 2 down** | 13 up : 2 down | 13 up : 1 down | — |
| next print | 2026-10-23 | 2026-11-05 | 2026-10-22 | 2026-11-03 | — |

⚠ **Blanks are blanks** — `PSX`'s fundamentals were not pulled this run and are left empty rather
than inferred. ✅ Arithmetic: the two "upside" figures are `target_mean/price − 1` on the pulled
values (324.556/372.940 = **−12.98%**; 317.895/358.385 = **−11.30%**) — both **negative**, i.e. price
above consensus target.

### §B · Thesis + freshness placeholder *(ALPHA fills the freshness tag)*

**The chain-position thesis**: the escalation's beneficiary is the **midpoint of the chain**
(services + refining), not the integrated majors or E&P. Evidence: `SECTOR_ROTATION §2`'s split, the
two independent refining-capacity destruction legs (Iran + Russia/Ukraine), and `GS`'s $63/bbl diesel
call. **Bracketed by `S136`** (settles 09-09) and **`P118`** (spot WTI, 09-11).
★ **ALPHA freshness tag: 🟡PARTIAL.** `theme_age` reads **Hormuz ⚪ECHO, accel 0.83×** and
**Iran ⚪ECHO 0.94×** — i.e. the *stock* of attention is decaying — **while the same-day flow column
says the opposite**: Hormuz printed **201 articles = 1.30× its own 7-day average**, and the
escalation's proper noun **`Larak` printed 91 of its 100 thirty-day articles TODAY** (velocity 3.94,
same-day ratio **6.92**). ⇒ **the theme is old; the event is one day old.**
**Residual, stated:** *does the escalation reach the equities' flow at all?* The flow axis is
`asof 08-28` and the strikes were **08-30/31**, so **the money has not voted.**
**Dated re-check: 2026-09-09** (`S136`), with `P118` at **09-11** behind it.

### §C · Flow / positioning cross-read

| | flow (Δ) | OBV | `rs20`/`rs60` vs `SPY` | FINRA short-vol z (08-28) |
|---|---|---|---|---|
| **SLB** | **+0.661** (+0.09) | **+0.318 매집** | +12.6 / −1.2 | 🔴 **+2.40, 5v5 +9.0▲ — board's extreme spike** |
| COP | +0.324 (−0.05) | +0.097 | +5.2 / +7.5 | — |
| VLO | +0.349 (+0.01) | +0.090 | +9.6 / **+32.7** | — |
| MPC | +0.650 (−0.01) | +0.329 | +13.6 / **+36.0** | 🟢 −1.85 covering |
| PSX | +0.388 (−0.07) | +0.082 | +12.3 / +30.1 | +0.63 normal |
| XOM | −0.486 🔴 | −0.201 | −2.2 / +0.7 | 🟢 **−3.71** — board's extreme covering |

⚠ **`D6`**: OBV is a C-grade axis and carries none of these lines alone; each is quoted beside `rs20`
and the revision book.

### §D · Competition / peers

`SLB` vs `BKR` (−0.003): the two large service names diverge by **0.66** on flow — **`SLB` is not
"the services trade", it is a single name**. `MPC` / `PSX` / `VLO`: three refiners, **all within 1.2%
of 52-week highs**, `rs60` +36.0 / +30.1 / **+32.7** vs `SPY` — a **crowded cohort**, not a spread.
E&P: `COP` +0.324 against `EOG` −0.694 🔴 and `FANG` −0.622 🔴 — a **1.0 spread inside one
sub-industry**.

### §E · Refutation + dated catalyst

- 🚨 **`SLB`'s refutation is its own estimate book**: **3 up : 14 down (0q) and 1 up : 14 down (+1q)**,
  a **flat** revenue rate, and only **+3.0%** consensus upside at **−0.5%** from its 52-week high.
  **The money likes it; the analysts are cutting it.** ⇒ the accumulation is being driven by
  something other than earnings — the acquisition, the crowded short, or the barrel — and
  **`P118`-A (spot WTI ≥ 91.00) would make it the barrel**, which is written into `EVENT_ALPHA`
  card 8 as an explicit AMBIGUOUS clause.
- 🚨 **`MPC`/`VLO`'s refutation is `B2` in textbook form**: an 11.6× / 11.7× forward multiple on
  denominators revised **+127% / +90% in 90 days on 14:0 and 15:0 breadth**, **at** 52-week highs and
  **above** consensus target. ★ **And the frame that saved memory from this lens is unavailable
  here**: `module_disclosure_us MPC` shows **zero 수주/계약, zero 2.02, zero 7.01 filings in 90 days**
  — **a refining crack is a spot spread with no counterparty floor**, so there is no `R111`-style
  contractual band to flatten the fall. *"Checked, and it does not apply"* — a pass on the frame-
  transfer test with a bad answer for the position.
- ⚠ **`R89` + `P83` bar any refining-margin-vs-barrel separation claim** and none is made.
- **Dated catalysts**: `S136` **09-09** · `P118` **09-11** · `SLB` print **10-23** · `VLO` **10-22** ·
  `MPC` **11-03**. **Anti-signals live**: Venezuela supply event (printed today), OPEC+ quota, and any
  further M&A among `S136`'s eight constituents.

---

## §MATR — Materials (DEEP continuous C1)

### §A · Numbers

| | **LIN** | **FCX** | **NUE** *(held)* | **STLD** |
|---|---:|---:|---:|---:|
| price | 491.03 | 75.77 | 251.76 | 235.43 |
| forward P/E | 25.09 | 18.32 | **13.22** | **12.43** |
| trailing P/E | 31.64 | **37.14** | 20.09 | 21.36 |
| P/B | 5.79 | 5.41 | 2.58 | 3.59 |
| beta | **0.726** | 1.379 | **1.892** | 1.532 |
| 52-week range | 387.78–548.20 | 35.15–80.24 | 131.32–280.11 | 126.88–288.74 |
| distance to 52w high | −10.4% | −5.6% | −10.1% | **−18.5%** |
| consensus upside | +11.4% | 🚨 **−4.9%** | +12.3% | +15.2% |
| revenue QoQ series | −2.9·+4.7·+1.4·+1.9·**+5.8** | −15.6·+32.4·−8.0·−10.6·**+12.8** | +10.7·+8.0·+0.8·+11.4·**+9.5** | +0.6·+4.5·+5.8·+7.8·**+17.0** |
| 0q EPS 90-day | flat (data gap, see ⚠) | 0.741→**0.730 = −1.5%** | **4.111→5.886 = +43.2%** | **4.490→5.413 = +20.5%** |
| 0q revision breadth | 5 up : 7 down | 🚨 **3 up : 6 down** | **5 up : 1 down** | **5 up : 1 down** |
| +1q revision breadth | **1 up : 1 down (flat)** | 7 up : 1 down | **4 up : 1 down** | 2 up : 3 down |
| next print | **2026-10-30** | 2026-10-22 | 2026-10-27 | 2026-10-20 |

⚠ **`LIN`'s 0q EPS `current` field returns 0.0** in the pull (a provider data gap, not a zero
estimate) — **left as a blank, not imputed**; the +1q row (4.2358 → 4.2305, **1 up : 1 down**) is the
usable one and is what §E argues from.

### §B · Thesis + freshness placeholder

**The sector's board-leading Δ (+0.197) is NOT the metals.** Attribution: **`LIN` 51.4% · `CTVA`
21.4% · `CRH` 14.6% · `APD` 11.0% · `MLM` 9.1%**, with **`FCX` −3.4% and `NEM` −1.4% — negative.**
⇒ industrial gases + construction aggregates + ag-chem, i.e. **a low-beta rotation wearing a
Materials label**, not a commodity-cycle signal.
★ **ALPHA freshness tag: 🟡PARTIAL.** `theme_age` **copper ⚪ECHO 0.98×** — no acceleration
anywhere in this thesis, and **the Δ story has a mechanical rival**: **today is the MSCI
quarterly-review effective date** and `LIN` is a **24.7%-weight** constituent of its own sector.
**Residual, stated:** *is `LIN`'s +0.41 a rotation or a passive-flow artifact?* **`S131` (ARMED,
settles on the 08-31 close) separates them, and it is readable on the NEXT run.**
**Dated re-check: 2026-09-01** for `S131`, **2026-09-04** for the next COT print.

### §C · Flow / positioning cross-read

`LIN` +0.199 (Δ **+0.41**), OBV +0.258 매집, **`rs20` −0.7 / `rs60` −5.6 vs `SPY`**, `vol_surge`
**0.81** — accumulated on **below-average** volume with **negative** relative strength.
`FCX` +0.767, OBV +0.276, `rs20` +19.1 but **`rs60` only +6.2**, Δ **−0.08**.
`NEM` +0.644, OBV **+0.506**, `rs20` **+33.5**.
**Positioning**: **copper COT spec net at the 100th percentile of its year** (+85,266, +5,518▲);
**gold at the 66th — NOT crowded, and the two must not be netted.**

### §D · Competition / peers + screener widening

Screener (⚠ **gapped series, §0c**) adds: **leader-pullback `SHW` (RSI 28.1), `STLD` (26.5), `NUE`
(29.4)**; **de-rate snapback `CRH` (33.1, px/200 −16%), `MLM` (35.2, −13%)**. **5 new names, none
held.** ⚠ **Used only to widen the net** — RSI values sit on a series that omits 08-28 and ends on a
live bar, so **no level or trigger is taken from them**.

### §E · Refutation + dated catalyst

- 🚨 **The `LIN` reading's own falsifier is pre-declared**: **today is the MSCI quarterly-review
  effective date**, and `LIN` is a 24.7%-weight constituent. **A +0.41 one-day Δ on a low-beta index
  heavyweight, on a rebalance date, has a mechanical candidate cause.** `S131` (ARMED, settles on the
  08-31 close) is the row that separates rotation from passive flow — **registered before the score,
  not after** (`D242`).
- 🚨 **`FCX`**: price **above** consensus target (−4.9%), trailing P/E 37.1, **0q estimates being cut
  (3 up : 6 down)**, and a revenue rate that **oscillates without trend** (−15.6·+32.4·−8.0·−10.6·+12.8)
  ⇒ **`B1`'s rate series is uninformative here and this sheet says so** rather than reading noise as
  a signal. **Frame check**: the FY2025 10-K prices US cathode off *"COMEX monthly average settlement…
  plus a premium"* and South America off **LME monthly averages 1–4 months forward** — **no floor, no
  ceiling** ⇒ **no contractual cap can be producing that oscillation.**
- 🚨 **`NUE` (held) and `STLD`: fundamentals up, money out.** Revenue rates accelerating (`STLD`
  0.6→4.5→5.8→7.8→**17.0**), estimates up **+43.2% / +20.5%** on 5:1 breadth — against flow **−0.307 /
  −0.187** and `rs60` **−4.8 / −16.7 vs `SPY`**. ⚠ **Steel's contracted share is `unknown` (C3)**, so
  the accelerating rate is **not** read as demand — annual contract resets would produce the same
  series.
- ⚠ **`C24` stays OPEN** — narrowed to `FCX` specifically. The strongest new evidence against the
  copper long is **not positioning**: it is that **copper's grid-demand chain is being distributed in
  the sector next door** (`GEV` −0.640, `ROK` −0.850 🔴, `PWR` −0.622 🔴 — see §INDU).
- **Dated catalysts**: `S131` settle **08-31 close** (readable next run) · next COT print **09-04** ·
  `STLD` **10-20** · `FCX` **10-22** · `NUE` **10-27** · `LIN` **10-30**.

---

## §HLTH — Health Care (DEEP continuous C2)

### §A · Numbers

| | **A** (Agilent) | **LLY** | **MRK** |
|---|---:|---:|---:|
| price | 152.28 | 1,152.51 | 147.58 |
| forward P/E | 22.56 | 24.40 | **15.46** |
| trailing P/E | 29.98 | 38.62 | — |
| P/B | 5.83 | 🚨 **30.33** | 8.69 |
| beta | 1.229 | 0.506 | **0.211** |
| 52-week range | 108.35–163.75 | 712.05–1,292.65 | 77.58–156.92 |
| distance to 52w high | −7.0% | −10.8% | −6.0% |
| consensus upside | +14.5% | +14.1% | 🚨 **+0.8%** |
| revenue QoQ series | 🚨 **+6.5·−0.8·+4.2·+3.5·+2.1** | +11.3·+22.2·+13.1·+12.5·**+16.0** | −6.8·+1.8·+9.3·−5.7·**+2.0** |
| 0q EPS 90-day | 1.710→1.728 = +1.1% | 9.396→**9.871 = +5.1%** | 2.307→**2.210 = −4.2%** |
| 0q revision breadth | 1 up : 1 down | **13 up : 1 down** | 🚨 **1 up : 5 down** |
| **+1q revision breadth** | 🚨 **0 up : 2 down** | 🚨 **5 up : 10 down** | 🚨 **2 up : 4 down** |
| next print | 🚨 **2026-11-26** | 2026-10-29 | 2026-10-29 |

### §B · Thesis + freshness placeholder

**The breadth is real and is not an `LLY` artifact** — `eqflow` **+0.135 (rank 2/11)** is
equal-weighted by construction, **30 of 32 names are non-red**, and the coherent block is **Life
Sciences Tools, 4 of 4 positive** (`A` +0.906 · `WAT` +0.426 · `DHR` +0.397 · `TMO` +0.392).
The two reds are **managed care** (`UNH` −0.765, `CVS` −0.828), not the sector.
★ **ALPHA freshness tag: 🟡PARTIAL.** **No health-care theme registers acceleration on this
board**, and the sector's only 🟢 (`A`) has **no scheduled catalyst until 2026-11-26** — three months
in which its only observable is the flow axis being tested.
**Residual, stated:** *does the tools block hold as a unit?* `EW{A, TMO, DHR, WAT}` `rs20` vs `SPY`
all four positive keeps the breadth claim; two turning negative retires it.
**Dated re-check: 2026-09-14** (`S133`), with `LLY`'s +1q revision breadth graded **2026-10-29**.

### §C · Flow / positioning cross-read

`A`: **+0.906 🟢, OBV +0.330 매집, `vol_surge` 1.43** — the only green on the board with volume
confirmation. `LLY`: −0.288, OBV −0.082, `rs20` −0.8 vs `SPY` — **drags the LEVEL** while being
**27.9% of the sector's positive Δ**. `MRK`: +0.678, OBV +0.249, **`rs60` +27.3 vs `SPY`**.
`LLY` FINRA short-vol **z +0.54, normal**.

### §D · Competition / peers + screener widening

Screener (⚠ **gapped series, §0c**) adds **leader-pullback `LLY` (RSI 37.5), `EW` (44.3)** and
**de-rate snapback `ISRG` (33.0, px/200 −21%)** — **3 new names**.
Peers: within Life Sciences Tools, `A` leads `WAT`/`DHR`/`TMO` by 0.48–0.51 on flow — **a leader
inside a uniformly positive block**, which is the shape the desk calls breadth rather than a spike.

### §E · Refutation + dated catalyst

- 🚨 **`A`'s refutation is its own rate series**: **+4.2 → +3.5 → +2.1 is two consecutive declines in
  the RATE**, which is exactly `B1`'s signal, with the still-positive level as the distraction.
  **Contract check (`R111`'s lesson)**: `A` sells instruments and consumables on catalogue/spot
  pricing; **no floor/ceiling structure is disclosed in the sources read** ⇒ **the deceleration is
  not arithmetic hitting a cap.** Contracted share itself `unknown` (C3).
  🚨 **And it has no scheduled catalyst until 2026-11-26** — a 🟢 whose only observable for three
  months is the very axis being tested. ⚠ **`module_report_tags` returns NO prior desk report on
  `A`** — an un-covered name carrying the board's cleanest green.
- 🚨 **`LLY`'s refutation is a breadth flip one quarter out**: **0q is 13 up : 1 down while +1q is
  5 up : 10 DOWN**, at **P/B 30.3** — a multiple with no cushion if the forward book keeps turning.
  ⚠ The Merida acquisition is quoted as *"up to $2.875bn"*; **the upfront consideration is `unknown`
  (C3)** and no earnings impact is claimed.
- 🚨 **`MRK` is the sheet's cleanest "cheap and rolling over"**: forward P/E **15.5** with
  consensus upside **+0.8%** (price essentially AT target) against **0q 1 up : 5 down and +1q 2 up :
  4 down** — the flow (+0.678, `rs60` +27.3) and the revision book point opposite ways. **Recorded as
  an unresolved disagreement, not resolved by picking a side** (`C5`).
- **`UNH`/`CVS` stay rejected** on the frame that **inverts**: an MLR floor **caps** insurer margin
  rather than guaranteeing it — the board's two largest consensus upsides (+20.9% / +24.7%) have **no
  contractual protection**.
- **Dated catalysts**: `S133` **09-14** (⚠ this sheet deliberately does **not** pre-commit its
  answer) · `LLY`/`MRK` prints **10-29** · `A` **11-26**.

---

## §INDU — Industrials (DEEP, PREMORTEM-promoted)

### §A · Numbers

| | **ETN** *(held)* | **GEV** | **VRT** | **PWR** |
|---|---:|---:|---:|---:|
| price | 403.48 | 893.86 | 257.90 | 605.03 |
| forward P/E | 25.11 | **35.56** | 28.34 | **30.80** |
| trailing P/E | 41.05 | 25.66 | — | — |
| P/B | **7.74** | 🚨 **19.91** | 🚨 **20.87** | **9.43** |
| beta | 1.177 | 1.033 | 🚨 **2.077** | 1.219 |
| 52-week range | 311.92–478.00 | 530.16–**1,195.94** | 118.70–**379.94** | 363.01–**788.75** |
| distance to 52w high | −15.6% | 🚨 **−25.3%** | 🚨 **−32.1%** | 🚨 **−23.3%** |
| consensus upside | +17.9% | **+38.3%** | **+31.1%** | +27.3% |
| revenue QoQ series | +0.5·+10.2·−0.6·+6.6·**+14.5** | −9.9·+13.4·+9.4·−6.3·**+18.9** | −1.8·+29.6·+1.4·−1.0·**+23.6** | −4.9·+8.7·+12.7·+3.2·**+21.4** |
| 0q EPS 90-day | 3.5065→3.5266 (**flat**) | 4.347→**4.170 = −4.1%** | 1.783→1.822 = +2.2% | 4.239→**5.020 = +18.4%** |
| 0q revision breadth | 11 up : 6 down | 7 up : 5 down | **13 up : 4 down** | **16 up : 0 down** |
| **+1q revision breadth** | **15 up : 2 down** | **11 up : 1 down** | **15 up : 1 down** | **16 up : 0 down** |
| next print | 2026-11-03 | 2026-10-28 | 2026-10-21 | 2026-10-29 |

### §B · Thesis + freshness placeholder

**The `UW−` is right about the bucket and wrong as a unit.** Industrials is two sectors under one
label: a **positive services/payroll/rail block** (13 names, four with OBV > +0.28) and a **negative
short-cycle capex + construction + electrical block**. 🚨 **The AI-power/electrical sub-block is
27.4% of the sector's entire one-day deterioration** (`GEV` 11.7% + `ETN` 9.6% + `VRT` 6.1%) —
**and the desk is long it through `ETN`.**
★ **ALPHA freshness tag: 🟡PARTIAL.** `theme_age` **data center ⚪ECHO 1.03×** — the AI-power
narrative is **consumed, not fresh** — while the block's **forward estimates are being revised UP**
(`PWR` **16 up : 0 down**, `VRT` 15:1, `ETN` 15:2, `GEV` 11:1) and its flow is being distributed.
**Residual, stated:** *is `ETN`'s worst-of-book Δ a corporate-action mechanic or a thesis break?*
The `DAN` combination completes **Q1 2027**; the near-term tell is whether Δ recovers above 0 **while**
OBV stays 매집.
**Dated re-check: 2026-09-18**, with `S126`+`P114` on **NFP 09-04** in between.

### §C · Flow / positioning cross-read

| | flow (Δ) | OBV | `rs20`/`rs60` vs `SPY` | short-vol z |
|---|---|---|---|---|
| **ETN** *(held)* | −0.061 (**Δ −0.39 — worst of any held name**) | **+0.202 매집** | −6.0 / −6.4 | 🟢 **−1.98 covering** |
| GEV | −0.640 (−0.26) | −0.075 | −11.0 / −7.0 | — |
| VRT | +0.153 (**−0.32**) | +0.093 | +3.3 / **−24.5** | — |
| PWR | **−0.622 🔴** (−0.30) | −0.117 | −12.7 / −17.8 | — |
| ROK | **−0.850 🔴** | −0.229 | −13.2 / −8.7 | — |
| RTX *(held)* | −0.255 (−0.16) | +0.031 | −4.6 / **+20.7** | +0.75 normal |

★ **`ETN`'s three axes point three ways**: flow score **worst-of-book**, OBV **accumulating**, shorts
**covering**. That combination is what a **corporate action** produces — see §E.

### §D · Competition / peers + screener widening

Screener (⚠ **gapped series, §0c**) adds **leader-pullback `ITW` (RSI 19.7), `MMM` (24.5), `GD`
(24.9), `PH` (28.1)** and **washout `FER` (18.6), `HON` (21.7), `LHX` (22.4)** — **7 new names, the
largest new-name count of any sector this run**, consistent with 17 reds of 50.
Peers inside the AI-power block: `ETN` −0.061 vs `EMR` +0.208 vs `ROK` −0.850 — **a 1.06 spread among
three electrical names**, so "electrical equipment" is not a tradeable unit either.

### §E · Refutation + dated catalyst

- 🚨🚨 **The finding that changes how `ETN` should be read, and no prior desk file contains it.**
  `module_disclosure_us ETN` (90 days) returns **18 filings of which SIX are Form 425** — five on
  **2026-06-11** (two named `…-cfaqs` / `…-efaqs`) and one on **2026-07-31**, plus a **Form 3** on
  08-18. Primary source read:
  > *"Filed by Eaton Corporation plc … **Subject Company: Dana Incorporated** … CEO Paulo Ruiz
  > announced **Eaton's plans to combine Mobility Group and Dana Incorporated** … approximately
  > **$11B in revenues** … we expect to complete in **Q1 2027**."*
  **`D5` cross-provider: MET at name level** — `seekingalpha` 2026-08-06: *"Dana plans $200M 2026
  buybacks and targets **$14B–$15B sales by 2030 with Eaton Mobility**"*; plus `prnewswire` M&A
  class-action notices naming **DAN** (06-24, 06-25).
  ⇒ (i) **`ETN` is being narrowed toward a pure electrical/AI-power business**, which makes the
  desk's own thesis label *more* accurate after the deal; (ii) there is a **live corporate-action
  process with shareholder litigation noise**; (iii) it is a **plausible mechanical explanation** for
  the flow/OBV/short three-way split. ⚠ **Explicitly a hypothesis with an observable, not a
  mechanism** — the desk has no instrument attributing flow to corporate actions.
  🚨 **Process failure named**: the deal was announced **eleven weeks ago** on a name held in both
  books, and appears in **zero** desk artifacts. ⇒ **`D436`** (read a held name's filing list for
  **425 / S-4 / DEFM14A**, not only 8-K/10-Q — `ETN`'s 8-K categories 2.02/7.01/3.02/5.02 are all
  empty while six 425s sat beside them).
- 🚨 **The block-level refutation cuts the other way from the flow**: **forward estimates are being
  revised UP across the whole AI-power block** — `ETN` **15 up : 2 down**, `GEV` **11 up : 1 down**,
  `VRT` **15 up : 1 down**, `PWR` **16 up : 0 down** — while every one of them is **15–32% below its
  52-week high** and being distributed. ⚠ **Used only as a description of the denominator's
  direction**, never as a leading indicator (and none of these is an IT name, so the measured
  IT-loading confound does not apply).
- 🚨 **Valuation offers no cushion**: `GEV` **P/B 19.9**, `VRT` **P/B 20.9 at beta 2.08**. **`B2` does
  not apply** (there is no cheap multiple to be trapped by); **the opposite risk does.**
- ⚠ **Contracted backlog share is `unknown` (C3)** for `ETN` and `GEV` — neither 90-day filing list
  contains a 수주/계약 disclosure. **Any future "AI-power backlog protects the margin" claim must
  extract it first.**
- **Dated catalysts**: `S126` + `P114` on **NFP 09-04** · `VRT` **10-21** · `GEV` **10-28** ·
  `PWR` **10-29** · `ETN` **11-03** · the `DAN` combination **Q1 2027**.

---

## §LIVE — cross-sector shortlist names (outside the DEEP sectors)

`US_LIVE_SHORTLIST.json`: **4 names** clear mcap ≥ $10B + 🟢가속.

| | flow | OBV | `rs20`/`rs60` vs `SPY` | short-vol | verdict on this sheet |
|---|---:|---|---|---|---|
| **CRM** | **+1.000** (score cap) | +0.305 | **+36.3** / +32.4 | z −0.76 ✅ | ⚠ **its print already fired 2026-08-27** ⇒ post-earnings drift, **not a pending catalyst**. Forward P/E 16.29, **consensus upside +1.9%**, 0q 1 up : 0 down but **+1q 3.627 → 3.544 = −2.3%**. **+41.7% above its 50DMA.** ⇒ **not carried as a candidate; re-filed to watchlist** |
| **A** | +0.906 | +0.330 | +8.1 / +9.9 | z −0.92 ✅ | **carried in §HLTH** |
| **MSTR** | +0.883 | **+0.471** | **+33.5** / **−1.4** | z −1.41 ✅ | 🔄 **TURN shape, not continuation.** A bitcoin-treasury proxy; *"Strategy Buys $370M of Bitcoin in First Purchase Since June"* [5 outlets today]. **Dropped from this sheet — its driver is an asset price the desk does not model**, `L.vehicle없음`-adjacent |
| **INTU** | +0.850 | +0.165 | +10.3 / — | z +0.20 △ | **Dropped** — the only shortlist name without short-side confirmation, and no sector mandate reaches it |

⚠ **Every drop above is written to a ledger in §Ledger, not left as an absence.**

---

## §Ledger · what this sheet set aside, and what it never reached

**Rejections written this stage** (`reject_ledger.py add`, each with a class, a `--revives-if` and a
`--recheck-date` — the script refuses the row without both):

| ticker | class | why | revives if | recheck |
|---|---|---|---|---|
| **CRM** | `B.모멘텀only` | flow at the score cap but the catalyst **already fired 08-27**; +1q EPS −2.3%, consensus upside **+1.9%**, +41.7% above its 50DMA | `rs20` > +20 vs `SPY` **and** a new dated catalyst inside 30 days | 2026-09-30 |
| **INTU** | `G.섹터중립` | 🟢 but **no sector mandate reaches it** and it is the only shortlist name without short-side confirmation (z +0.20) | IT returns to `OW` **or** short-vol z < −1.0 | 2026-09-30 |
| **MSTR** | `L.vehicle없음` | its driver is the bitcoin price, which this desk does not model; the flow read is real but **un-attributable** | the desk registers a crypto driver row, **or** `MSTR` `rs60` turns positive with OBV > +0.40 | 2026-09-18 |
| **MRK** | `I.테제반증` | flow +0.678 and `rs60` +27.3 vs `SPY` against **0q 1 up : 5 down, +1q 2 up : 4 down** and consensus upside **+0.8%** — price at target with a turning book | 0q revision breadth flips net-up **while** `rs20` > 0 | 2026-10-29 |

**Misses written this stage** (`missed_ledger.py add`, `--sample prospective`):

| ticker | class | why | enters if | recheck |
|---|---|---|---|---|
| **PWR** | `Q.확신부족` | **16 up : 0 down on BOTH 0q and +1q**, revenue rate **+21.4% QoQ**, **−23.3% off its 52-week high** — the strongest revision book in this entire sheet, against flow −0.622 🔴 | OBV turns 매집 **and** `rs20` > 0 vs `SPY` on two consecutive settled closes | 2026-09-18 |
| **GEV** | `Q.확신부족` | consensus upside **+38.3%**, +1q **11 up : 1 down**, **−25.3% off its high**, and it is the AI-power cycle's generation node — which the registry cannot represent (`D416`) | `cycle_registry.json` gains an AI-power row **or** GEV OBV turns 매집 | 2026-09-18 |

★ Earlier stages already wrote **6 rejections** (`XOM`·`EOG`·`FANG`·`KEYS`·`CIEN`·`AON`) and **5
misses** (`VLO`·`COP`·`MSFT`·`LITE`·`SHOP`). **Run total: 10 rejections, 7 misses.**
⚠ **No name was removed on narrative grounds while its measured flow still passed.** The one name
that would have qualified — **`XOM`, dropped by money on the day its story was the board's loudest** —
was **re-filed with a new thesis line** (*"the escalation's beneficiary is the chain's midpoint, not
the integrated major"*) rather than deleted, per the 475150 precedent.
⚠ **Sign convention**: `missed_ledger`'s `excess` is inverted vs `reject_ledger`'s; **never summed
without aligning signs.**

---

## §Size · influence illustration only — and it names its book

**Zero buy/sell recommendation. Nothing below is an instruction.**
- The exposure rule reads **`정상`** — **no firing condition, and no `복귀` obligation to fill a
  target.** ⇒ **this sheet is under no pressure to manufacture candidates**, and it did not.
- **Whichever book is read, the cash question has two different answers and they are not
  reconcilable inside this run**: the **real KIS account is 53.0% cash**; the **KR-contest ledger is
  85.3% invested against a 95% target (−9.7pp)**. **`C23` is a human call (P5).**
- 🚫 **Concentration cannot be stated as a single number** (`G4`): risk units read **11 (250d) / 10
  (500d) / 10 (750d)** with **different membership** — the 250d window puts `ANET`, `AVGO`, `ETN`,
  `NVDA` in **four separate units** while 500d/750d merge them into **two**. **Whether the book's four
  AI names are one bet or four is unmeasured today.**
- 🚫 **`kelly_size --ic` may not be reported as an evidenced size** (`G6`: accrual 0.51/day = 2.0× the
  ideal). If used anywhere downstream it must be labelled **"mechanical 1/4"**.

## ✅ EXIT CHECK
- [x] **Company scoreboard consulted before any re-derivation** (§0a) — **zero US rows**, and the
      10-day age would have failed the freshness test anyway. `module_report_tags ticker` queried per
      candidate; **`A` flagged as having no prior desk report.**
- [x] Every DEEP sector has a section (**§ENRG · §MATR · §HLTH · §INDU**); cross-sector LIVE shortlist
      names are in **§LIVE**, and the three dropped ones each carry a ledger row.
- [x] Numbers cross-checked; the two negative-upside figures re-derived by hand
      (324.556/372.940 − 1 = −12.98%; 317.895/358.385 − 1 = −11.30%). **Blanks left blank** (`PSX`
      fundamentals; `LIN`'s 0q field; contracted shares marked `unknown`).
- [x] Flow/positioning cross-read present per candidate (§C in each section);
      **`BET_SHEET.md` written as ONE file.**
- [x] **Every set-aside name is in `reject_ledger` with a class AND a `--revives-if` AND a
      `--recheck-date`.** No permanent bans issued.
- [x] **No name removed on narrative grounds alone while its flow still passed** — `XOM` re-filed
      under a new thesis with a dated re-check rather than deleted.
- [x] **Names that surfaced upstream but never reached a rejection are in `missed_ledger`** with a
      class and an `--enters-if` (`PWR`, `GEV` here; `VLO`·`COP`·`MSFT`·`LITE`·`SHOP` upstream).
      **The funnel is scored in both directions: 10 rejections, 7 misses this run.**
- [x] **Sizing language consistent with the carried exposure state** (§Size) — state is `정상`, not
      `복귀`, so no target-filling obligation is asserted, and **every sizing line names its book.**
- [x] **Linter** — `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-31/industry_US/BET_SHEET.md` → **0 findings** on C1 / C2 / S6 / D6, no exemptions claimed. ⚠ Form only; the substantive risks are named in §0c (the gapped screener series) and §INDU §E (the `ETN` corporate action).

---

## §ALPHA · Freshness gate (Stage 10, appended — the sheet is not re-written)

### The `F1` line, and this is the SECOND run that may state it as arithmetic

`theme_age` on eleven terms, `--scope foreign`: **every term returns `age ≥ 90`.** The 🟢FRESH gate
requires **age ≤ 14 days AND accel ≥ 2×**, so **on this board it is arithmetically unreachable** —
**no bet can be tagged 🟢LIVE, and that is a property of the gate, not of the market.**

🚨 **And the zero was checked against the pipe before being written** (`G1`, the mandatory
falsification probe):
- `fts search --days 7 --count --scope foreign`: **6/6 pre-sweep** (Federal Reserve 1,365 · Nvidia
  5,292 · tariff 1,993 · jobs report 82 · oil prices 1,143 · data center 2,551) and **4/4 post-sweep**,
  identical values.
- Direct `news_velocity` on **8 names, 8/8 alive**, including the two **lowest-flow names in the whole
  299-name universe** (`GWW` 0.69 · `PCAR` 1.12).
⇒ **the pipe is verified live, so the `F1` zero is arithmetic.** ⚠ This is only the **second** run in
the desk's record able to say that (the first was 08-30, `M1107`); the KR side's equivalent count is
**19 consecutive runs** and was, until recently, never checked against the counter.

**Accel, read separately from age** (since the age leg cannot fire): **Warsh 🟡ACCELERATING 3.27× —
the only accelerating theme on the board** · optical 1.35× · tariff 1.28× · rate hike 1.07× ·
memory 1.05× · data center 1.03× · copper 0.98× · Iran 0.94× · refining margin 0.85× · Hormuz 0.83×.

★ **The instrument gap this run measured, and it is why every tag above is 🟡 rather than 🔴**:
**the whole `theme_age` family is a STOCK-of-attention measure over 7–90 day windows, and it is
structurally blind to a one-day binary on an old theme.** Today it returned *"Hormuz decaying"* on
the day the strait's escalation was the **#1 event of 344** with 16 outlets. **The same-day column
(`D411`'s prescription, executed this run) is the flow measure that sees it**, and it is adopted from
here on.

### Tags issued

| bet | tag | residual / reason | dated re-check |
|---|---|---|---|
| **ENRG chain-position thesis** (`SLB`·`COP`·`VLO` + held `MPC`/`PSX`) | **🟡PARTIAL** | the money has not voted — flow is `asof 08-28`, strikes were 08-30/31 | **2026-09-09** (`S136`) |
| **MATR `LIN`-led Δ** | **🟡PARTIAL** | rotation vs passive-flow artifact, unseparated until `S131` is readable | **2026-09-01** |
| **HLTH breadth** (tools block) | **🟡PARTIAL** | block cohesion untested; the only 🟢 has no catalyst for 3 months | **2026-09-14** (`S133`) |
| **INDU / AI-power block** (`ETN` held) | **🟡PARTIAL** | corporate-action mechanic vs thesis break, unresolved | **2026-09-18** |
| **`CRM`** | 🔴 **RESOLVED — dropped** | catalyst already fired **2026-08-27**; +1q EPS −2.3%, upside +1.9% | ledger, revives 2026-09-30 |
| **`INTU`** | 🔴 **RESOLVED — dropped** | no sector mandate reaches it; no short-side confirmation | ledger, revives 2026-09-30 |
| **`MSTR`** | 🔴 **RESOLVED — dropped** | driver is an asset price this desk does not model | ledger, revives 2026-09-18 |
| **`MRK`** | 🔴 **RESOLVED — dropped** | flow and revision book point opposite ways; price at target | ledger, revives 2026-10-29 |

⚠ **Every 🔴 is a ledger row with a `--revives-if`, not prose** — so a dropped name returns on
evidence rather than on someone remembering it. **Every 🟡 carries an explicit re-check date** and is
handed to `carryover`, because *"a 🟡PARTIAL is a dated appointment, not a shelf."*
⚠ **Tags follow the NAME, not the sector's turn in the rotation** — `SLB`, `COP`, `VLO`, `LIN`, `A`
and `ETN` stay tracked in the next run's inheritance packet even if their sector loses its DEEP slot.

### Momentum-only flags, graded before being acted on (`D6`)

| name | disagreement | grade | outcome |
|---|---|---|---|
| **`SLB`** | RS/volume positive, **estimate book 3 up : 14 down** | the disagreement is **fundamental vs price**, not OBV-vs-price | **🟡, hard-stop stamp required**; ⚡ crowded-short is **squeeze fuel, never a standalone entry** |
| **`NUE`** *(held)* · **`STLD`** | revenue rate and estimates **UP**, flow and `rs` **DOWN** | price axes vs fundamental axes | **reported as a disagreement**, not converted into a verdict |
| **`ETN`** *(held)* | flow **worst-of-book**, OBV **매집**, shorts **covering** | the accumulation leg here is **OBV only = C-grade** (r≈0.49 vs real flow, no leading power, t=1.00) | ⇒ **C-grade disagreement DOWNGRADES to 🟡 and is reported as a disagreement** — it does **not** by itself make this a tape trade |

### Positioning gate (US)

⚡ **`SLB` z +2.40 with 5v5 +9.0▲ = crowded short.** Turn-conditional squeeze fuel; **stamped
hard-stop-required and NOT ticketed.** 🟢 `XOM` **z −3.71** and `NDAQ` **−2.37**, `ETN` **−1.98**,
`MPC` **−1.85** = short exodus — context, not a trigger. ⚠ **The US desk has no investor-type feed**;
short-pressure + COT percentile is *positioning context*, never a standalone signal.

### `ACTION_TICKETS.md` — zero tickets, and the reason is not silence

`action_bracket.py` wrote **no tickets**, correctly: **no cycle GAP**, **every binary in the window
already bracketed both ways (6 of 6)**, and the exposure rule reads **`정상`** with no target-filling
obligation. 🚨 **But the script contradicted itself in one output for a THIRD consecutive run**
(`D421`): it printed *"Nearest binary: AVGO earnings (D-2) — both-sides armed below"* **and** *"no
dated binary in window"* four lines apart. **Named in the file's ADDENDUM, not worked around.**
