# BET_SHEET — industry_US · 2026-09-07 (Mon, US Labor Day) · Stage 9 / L1·BET

> **ONE file, per-sector sections.** Downstream desks read this exact filename.
> **P4 — zero buy/sell recommendations.** Any sizing language is *influence illustration* only.
> ⚠ **Every flow/price number is `asof` 2026-09-04** — the third consecutive run on one settled
> session. **Nothing on this sheet is a fresh tape reading**, and the sheet says so on every line.

---

## §0 · Gates read before anything was derived

| gate | state | effect on this sheet |
|---|---|---|
| **Thesis-confirmation (`COMPANY_SCOREBOARD.md`)** | Exists, dated **2026-08-21**, **5 rows, all KR** (`036460` `011200` `316140` `028050` `000660`) | 🚫 **No US candidate on this sheet has a scoreboard row**, so the confirmation gate cannot fire and **every US name below is derived, not confirmed.** ⚠ The scoreboard is also **17 days old** — past the 10-settled-session **age** test — so even its two book-relevant KR rows (`316140` HOLD, `028050` HOLD) would need a re-dig before being cited as current. **Stated, not worked around.** |
| **`module_report_tags`** | queried — the US industry reports are indexed; no per-name US company report exists for any new candidate | *"no row ≠ no coverage"* checked, and the answer is genuinely **no coverage** |
| **Exposure state** | `exposure_rule show` = **live / 정상**, stored invested **85.2% (asof 09-04)**, **current field BLANK** (account query failed), band **−9.8pp**, n=18 | 🚫 **No sizing may be quoted from this.** The 85.2% may be cited **only** as a stored 09-04 value |
| **Cycle GAP** | `cycle_exposure` = **no top-rank GAP** (AI-compute 17.51% ≥ 12.0; Energy/refining 10.49% ≥ 8.0) | ⇒ **the epicenter-starter module is NOT triggered** and no starter appears on this sheet. **Rank-3 (defense) has no bar set**, so the check is silent there, not passing |
| **`kelly_size --ic`** | 🚫 **barred** — instrumentation accrual **0.56/day = 1.8× slow** (G6). If size appears anywhere downstream it is **"mechanical 1/4"**, with no IC claim |
| **Concentration** | `risk_units --book`: **12 units at 250d / 11 at 500d / 10 at 750d** — quoted here **with the window**, as G4 requires, and never as one number |

---

## §ENERGY — the refining node, and the un-held leg

**Candidate set** = DEEP-ENRG thesis leaders ∪ sector screener ∪ LIVE shortlist.
Screener (`us_setup_screener --sector Energy`, 16 names): **A. leader-pullback `FANG` `KMI`** ·
B/C empty. LIVE shortlist: **`SLB` `WMB` `CVX`**.

### §A · Numbers — the two refiners side by side (the point of the section)

| | **`MPC` (held)** | **`VLO` (not held)** |
|---|--:|--:|
| price / 52w | **$388.90** (high $398.52 ⇒ **−2.4% from the high**) | **$370.72** (high $375.11 ⇒ **−1.2% from the high**) |
| mcap · beta | $109B · 0.53 | $107B · 0.57 |
| **forward P/E** | **12.24** (trailing 13.48) | **11.88** (trailing 15.45) |
| P/B · P/S | 5.77 · 0.74 | 4.27 · 0.81 |
| PEG | 1.89 | **4.08** |
| **est. Δ90d, current year** | **+74.5%** (29.20 → 50.95) | **+49.4%** (29.33 → 43.83) |
| est. Δ90d, current quarter | **+120.8%** | **+87.2%** |
| **revision breadth 30d (curr. qtr)** | **15↑ / 0↓** | (not printed in the 30d cut this run — **blank stated as blank**) |
| analyst mean target | **$333.39 ⇒ −14.3%** | **$325.21 ⇒ −12.3%** |
| recommendations | 4 SB / 6 B / **8 H** / 1 S | 3 SB / 7 B / **8 H** / **2 S** |
| dividend yield | 1.03% | 1.29% |

★★ **Both names are within 2.4% of their 52-week high, on forward multiples near 12×, with estimates
up 49–120% in ninety days, trading ABOVE consensus mean targets, with `Hold` as the modal
recommendation and `VLO` carrying two `Sell`s.** That is the **peak-margin / low-multiple trap** with
every one of its markers present at once. **The low multiple is the denominator running, not a
discount** — and `SECTOR_DEEP_ENRG.md §3` establishes there is **no external take-or-pay floor** under
`MPC`'s consolidated margin (the MPLX minimum-volume commitments are **intercompany**, and the 10-K
says they *"will negatively impact segment adjusted EBITDA in periods when throughput or sales are
lower or refineries are idled"*).

### §B · Thesis + freshness *(ALPHA fills the freshness tags)*

> **The Energy OW is a chain-position bet on destroyed refining capacity, not a barrel bet.**
> Body-confirmed this run: **IEA ~9.6 mb/d = a fifth of Middle East refining capacity knocked out**;
> **Russia has banned diesel exports**; **record-low gasoline and diesel inventories**; a bunker-fuel
> shortage of **218 kb/d** vs 6 kb/d in 2025. The node's flow is the chain's best on every axis
> (`eqflow` **+0.715**, **3/3 accumulating**, `rs20` +27.0, `rs60` +37.7).
> ⚠ **The counter-evidence, carried in the same paragraph** (`C2`): the crack's **monthly** rate has
> now printed **two consecutive declines (+37.6% → +13.0% → +8.6%)** — which is verbatim the signal
> `RESEARCH.md` B1 defines — while its **quarterly** rate is at a two-year maximum (+40.5%).
> **The sign depends on the window** (`D565`), and `P140` settles the 5-session version on **09-11**.

- **`[freshness]` 🟡PARTIAL** — filled by ALPHA (see **§ALPHA A-1**). Re-check **2026-09-11** (`P140`). 🚫 Cannot be 🟢LIVE: the FRESH gate's **age leg** admits nothing on this board — see §ALPHA A-0.

### §C · Flow / positioning cross-read (`asof 2026-09-04`)

| name | flow | OBV | rs20 | rs60 | surge | tag | `[FINRA]` short | chart (`--read`) |
|---|--:|--:|--:|--:|--:|---|---|---|
| **`SLB`** | **+0.883** | +0.439 매집 | +14.2 | −2.6 | 1.39 | 🟢 | **z −1.21 ✅ low-short / covering** | **CONFIRMED-TURN**, OBV +87%, **no divergence**, 3/4 MA, trigger `close>57.94`, swing-low stop 51.79 |
| `MPC` (held) | +0.694 | **+0.621 매집** | **+30.8** | **+41.5** | 1.05 | 🟡 | z +0.43, but **the sheet's largest 5v5 short build (+8.9)** | CONFIRMED-TURN, OBV +52%, **no divergence**, RSI 76.0, 4/4 MA, stop 319.45 |
| `PSX` (held) | +0.750 | +0.434 매집 | +25.5 | +34.2 | 1.15 | 🟡 | covering, skew +0.1 | CONFIRMED-TURN, OBV +58%, 🚨 **BEARISH DIVERGENCE**, RSI 68.6, stop 214.38 |
| **`VLO`** | +0.700 | +0.482 매집 | +24.7 | — | 1.06 | 🟡 | — | not rendered this run — **blank stated as blank** |
| `COP` | +0.639 | +0.222 매집 | +14.6 | +5.8 | 0.95 | 🟡 | — | — |
| `WMB` | +0.769 | +0.151 매집 | +5.7 | — | 1.39 | 🟢 | **z −1.16 ✅** | — |
| `CVX` | +0.661 | +0.371 매집 | +12.2 | — | **0.99** | 🟢⚠ | z +0.78 △ | — |
| `XOM` | **+0.027** | −0.071 중립 | +4.6 | −0.3 | 0.97 | 🟡 | — | — |

⚠ **`CVX`'s 🟢 is not citable** — `vol_surge` **0.99** is below the gate; it is tagged only because
universe rank 35 grants it a `velocity`, an axis `scoring.vel_axis` declares **false** (`D561`).
⚠ **`MPC`/`PSX`/`VLO` are 🟡 by 0.05–0.15 of `vol_surge`** while carrying the board's strongest accumulation on the OBV axis, alongside `rs20` **+30.8 / +25.5 / +24.7** and `rs60` **+41.5 / +34.2** — **RULE D6 exempt: the OBV reading is quoted with two RS axes and the composite `flow_score`, never alone.**
**Their absence from `US_LIVE_SHORTLIST.json` is a filter artifact, not evidence.**
⚠ **US has no investor-type feed** — `[FINRA]` short pressure is a *proxy*, context never trigger.

### §D · Competition / peers

The refining node is **three names inside the universe** (`MPC` `PSX` `VLO`) and the desk holds two.
🚨 **The peer set cannot be completed**: `DINO`, `PBF`, `DK` are **not in `us_top300.csv`** (`D563`),
so relative-multiple work against the mid-cap refiners is **not possible on this desk's instruments**.
Upstream peers `HAL`, `FTI` likewise absent; `SLB` and `BKR` are the only services names available.

### §E · Refutation + dated catalyst

| | |
|---|---|
| **What kills it** | The crack's **monthly** rate printing a **third** consecutive decline or a negative month · an **IEA revision** cutting the 9.6 mb/d outage · **`MPC`'s first estimate downgrade** against a 15↑/0↓ breadth · a **Hormuz reopening statement** (undated, `[news👁]` in `CATALYST_WATCH`) · a **US SPR release/refill**, an **`HO`/`CL` contract-spec change**, or a **Gulf hurricane outage ≥500 kb/d** (all three are `P140`'s registered VOIDs) |
| **Dated catalysts** | **`P126` 2026-09-09** (barrel vs chain) · **`P140` 2026-09-11** (the crack's rate vs its level) · **`P139` 2026-09-14** (Venezuela: upstream leg vs refining leg) · **`P136` 2026-09-14** |
| **Momentum re-tag** (PREMORTEM Lens 3, volatility-normalized) | `MPC` **+3.27 z** — the board's true outlier — **EXTENDED-BUT-LIVE**, no divergence, OBV accumulating on both instruments · `PSX` **+3.08 z** — EXTENDED-BUT-LIVE **with a bearish divergence its twin does not have** · `SLB` +1.29 z EXTENDED-BUT-LIVE |
| 🚨 **Construction note on a live row** | `P139`'s branch-A basket is `EW{XOM, CVX, SLB}`. This run's body read `[yahoo_finance 09-06]` records **`XOM`'s own CEO called Venezuela "uninvestable" in January** and that `XOM` is *"far behind"* `CVX`, which has just signed the deal. **Thresholds and basket UNCHANGED (`D242`)** — the reading is recorded, not the row edited |

---

## §HEALTH CARE — the node that is accumulating on a falling denominator

Screener (32 names): **A. `EW` `LLY` `ABT`** · **B. de-rate snapback `ISRG`** (RSI 33.6, px/200 −21%)
· C empty. LIVE shortlist: **`MDT`**.

### §A · Numbers — `ALNY`, and the cross-sector comparison that is the section's point

| | **`ALNY`** (biotech node leader) | *(for contrast)* **`MPC`** |
|---|--:|--:|
| price / 52w | **$266.11** (high $495.55 ⇒ **−46% from the high**) | −2.4% from the high |
| mcap · beta | $36B · **0.30** | $109B · 0.53 |
| forward P/E | **21.14** (trailing 46.28) | 12.24 |
| PEG · P/S · P/B | 0.34 · 7.41 · 26.28 | 1.89 · 0.74 · 5.77 |
| **est. Δ90d, next year** | **−9.4%** (13.90 → 12.59) | **+33.6%** |
| **revision breadth 30d** | **2↑ / 11↓** | **15↑ / 0↓** |
| analyst mean target | **$370.20 ⇒ +39.1%** | $333.39 ⇒ −14.3% |
| recommendations | **6 SB / 16 B / 7 H / 0 S** | 4 SB / 6 B / 8 H / 1 S |

★★ **The desk's two OW sectors fail the valuation test from opposite directions.** Energy is
**accumulation into a rising denominator at a cycle high**; Health Care/biotech is **accumulation into
a falling denominator 46% below the high**. **Neither is "cheap."** ⚠ The revision table is used as
**direction only** (`measure_ic` 2026-08-09: two windows, opposite signs, and the effect is an **IT
loading** — ex-IT Q5−Q1 **−1.1pp**); on a non-IT name the confound is weaker but the **leading claim
is still barred**.

### §B · Thesis + freshness

> **Health Care's "one-name breadth" reading is retired this run.** The carried `breadth 0.03`
> (1 🟢 of 32) is a `vol_surge` artifact: **only one name in the whole sector clears the ~1.2 gate**
> (`MDT` 1.47). Against that, **OBV-accumulation breadth is 23/32 = 72%**, positive `flow_score`
> 24/32, positive `rs60` 21/32. **Nine names clear flow > +0.5 ∧ OBV > +0.15 ∧ `rs20` > 0 and are
> excluded from 🟢 by turnover alone**: `ALNY` `MRK` `GILD` `PFE` `A` `AMGN` `JNJ` `REGN` `VRTX`.
> ⚠ **Counter-evidence in the same paragraph** (`C2`): the sector's binding constraint is the **payor**
> node (`rs60` **−3.4**, `UNH` OBV 분산) and the **facilities** node (`HCA` **−0.472**) — i.e. the money
> is at the front of the chain and the weakness is at the point of payment. **A pipeline that cannot
> be reimbursed is not a revenue node.**

- **`[freshness]` 🟡PARTIAL** — filled by ALPHA (see **§ALPHA A-1**). Re-check **2026-09-14** (`S133`). 🚫 Cannot be 🟢LIVE: the FRESH gate's **age leg** admits nothing on this board — see §ALPHA A-0.

### §C · Flow / positioning (`asof 2026-09-04`)

| name | flow | OBV | rs20 | rs60 | surge | tag | note |
|---|--:|--:|--:|--:|--:|---|---|
| `MDT` | **+0.928** | +0.327 매집 | +8.4 | +11.2 | **1.47** | 🟢 | 🚨 the sector's **only** 🟢, and it sits in the **weakest node** (Equipment, `eqflow` −0.044, 2/8) |
| `ALNY` | +0.683 | +0.359 매집 | **+21.8** | **−14.8** | 1.03 | 🟡 | ⚠ **`rs20` and `rs60` disagree in sign** — a 20-day turn inside a 60-day downtrend |
| `GILD` | +0.561 | +0.361 매집 | +13.8 | +18.1 | 0.81 | 🟡 | both RS positive — the node's most internally consistent name |
| `VRTX` | +0.506 | +0.338 매집 | +10.5 | +19.2 | 0.71 | 🟡 | same shape |
| `MRK` | +0.567 | +0.185 매집 | +17.3 | +20.1 | 0.82 | 🟡 | pharma node's leader |
| `LLY` | **−0.462** | −0.149 분산 | −2.7 | −5.0 | 0.93 | 🔴 | 🚫 **standing REJECTED `B.모멘텀only`**, recheck **09-14**, revives if `flow_score` > 0 **AND** OBV turns 매집 — **neither condition is met**, so the rejection **stands** |
| `ISRG` | −0.226 | +0.049 중립 | −2.8 | **−17.2** | 0.62 | 🟡 | screener bucket B; the sector's worst `rs60` |

⚠ **`LLY` and `ISRG` both appear on the screener and both are refused here on their own axes** —
the screener finds *setups*, not *flow*, and this is the disagreement stated rather than resolved by
picking the friendlier instrument.

### §D · Competition / peers

The biotech node's real peer set is **mid-cap biotech**, which sits almost entirely **below the
universe's $10B floor** ⇒ **the peer comparison cannot be built** (`D563`, third instance in one run).
Within the universe, `ALNY` `GILD` `AMGN` `REGN` `VRTX` `ABBV` are the complete set and **all six are
accumulating**, which is the node's whole case and also its whole sample.

### §E · Refutation + dated catalyst

| | |
|---|---|
| **What kills it** | Any biotech-node name losing OBV accumulation (**6/6 is the case; 5/6 weakens it materially**) · the Tools node staying **0/4 accumulating** through another run ⇒ the front of the chain is unfunded · payor node `rs60` deepening past −10 · a **US drug-pricing action** · **`hy_oas` ≥ 3.10%** (re-prices unprofitable biotech first) |
| **Dated catalysts** | **`S133` 2026-09-14** (is Health Care its constituents or its ETF?). 🚨 **Nothing else is dated** — and `catalyst_calendar`'s EARNINGS block reads *"(none in window / yfinance unavailable)"*, an **unavailability rendered as an absence** (`D560`), so **"no catalyst" is not verified** |

---

## §UTILITIES / AI-POWER — where the sheet's one genuinely differentiated name sits

Screener (15 names): **A. `ED` `ETR`** · **B. `PCG`** (RSI 33.2, px/200 −15%) · **C. washout `SO`**
(RSI **24.8**, 5% off its 52-week low). **LIVE shortlist: none** — and §SWEEP_READ diagnoses that
absence as a filter artifact, not evidence.

### §A · Numbers

| | **`CEG`** | *(context)* `MPC` | *(context)* `ALNY` |
|---|--:|--:|--:|
| price / 52w | **$298.96** (high $412.70 ⇒ **−27.6% from the high**) | −2.4% | −46% |
| mcap · **beta** | $106B · **1.12** ⚠ | $109B · 0.53 | $36B · 0.30 |
| forward P/E | **22.41** (trailing 29.25) | 12.24 | 21.14 |
| PEG · P/S · P/B | 3.74 · 3.39 · 3.32 | 1.89 · 0.74 · 5.77 | 0.34 · 7.41 · 26.28 |
| **est. Δ90d** | current qtr **+2.3%** · next qtr **+7.9%** | +120.8% · +85.6% | −5.9% · −3.8% |
| analyst mean target | **$348.30 ⇒ +16.5%** | −14.3% | +39.1% |
| recommendations | **6 SB / 13 B / 3 H / 0 S** — the sheet's most positive distribution | 4/6/8/1 | 6/16/7/0 |

★ **`CEG` is the one name on this sheet that is not caught by either failure mode.** Its multiple is
**not** artificially low (22.41× with estimates up only 2–8%, so the denominator is not sprinting),
its price is **27.6% below its high** (not a chase), and consensus sits **above** the price. ⚠ **And
its beta is 1.12** — it is **not** a bond proxy, which is exactly why it does not belong in the same
bucket as the sector's other 13 names.
⚠ **`P/B −236.95` on `DELL`** and **`PEG 4.08` on `VLO`** are the two figures on this sheet that
should not be used at all; both are noted where they appear rather than quietly dropped.

### §B · Thesis + freshness

> **"Utilities" is not one object.** `CEG`+`VST` run `eqflow` **+0.632**, **2/2 accumulating**,
> `rs60` **+9.4**; the other **13** run **−0.039** with `rs60` **−10.7** and **2/13 accumulating**.
> **Sub-node dispersion 1.157 against a sector move of 0.050 — roughly 23×.** `rs60` is positive for
> **exactly 2 of 15 names**. The bucket is a duration short with a growth story stapled to it.
> ⚠ **Counter-evidence, same paragraph** (`C2`): the **filing** says the AI-power floor is
> **1,200 MW of a ~44,000 MW fleet = 2.7%**, with **no revenue before Q4 2027**, ramping to full
> capacity **by 2032** — and the same 10-K discloses an **ERCOT price CEILING** (peaker-net-margin at
> 3× CONE ⇒ a **$2,000/MWh** system-wide cap for the rest of the year, plus the PUCT Emergency Pricing
> Program). **The desk had carried the floor and never the ceiling** (`D516` closed).

- **`[freshness]` 🟡PARTIAL** — filled by ALPHA (see **§ALPHA A-1**). Re-check **2026-09-10** (`P127`). 🚫 Cannot be 🟢LIVE: the FRESH gate's **age leg** admits nothing on this board — see §ALPHA A-0.

### §C · Flow / positioning (`asof 2026-09-04`)

| name | flow | OBV | rs20 | rs60 | surge | tag |
|---|--:|--:|--:|--:|--:|---|
| `CEG` | **+0.644** | +0.188 매집 | **+11.2** | **+17.2** | **0.96** | 🟡 ⚠ blocked by the gate alone |
| `VST` | +0.619 | +0.207 매집 | +6.6 | +1.6 | **1.02** | 🟡 ⚠ same; **Δ +0.491 = the board's largest** |
| `NEE` | +0.353 | +0.190 매집 | −1.0 | −8.2 | 1.11 | 🟡 |
| `GEV` | **−0.186** | +0.022 중립 | −4.5 | +2.5 | 0.92 | 🟡 |
| `ETN` (held) | **−0.662** | −0.115 분산 | −8.0 | +3.3 | 0.84 | 🔴 |
| `SO` | −0.443 | −0.163 분산 | −4.5 | −12.5 | 1.14 | 🔴 |
| `DUK` | **−0.513** | −0.143 분산 | −3.3 | −10.0 | 0.86 | 🔴 |
| `PCG` | −0.123 | −0.059 중립 | **−17.7** | **−20.6** | 🚨 **3.32** | 🟡 |

🚨 **`PCG` carries the board's highest `vol_surge` (3.32) on the sector's worst RS pair (−17.7 /
−20.6)** — volume arriving into a collapse, which is the opposite of the accumulation shape the
screener's bucket-B label implies. **Named so the screener hit is not mistaken for a setup.**

### §D · Competition / peers

🚨 **The AI-power peer set cannot be completed**: **`TLN` and `NRG` are not in `us_top300.csv`** —
and **`P127`, a LIVE row settling 2026-09-10, contains both in its basket.** ⇒ **a scored row will
settle on names this desk cannot flow-tag** (`D563`, and this instance is a *scoring* exposure, not
merely a measurement one). Transmission/EPC peers likewise absent.

### §E · Refutation + dated catalyst

| | |
|---|---|
| **What kills it** | `CEG` or `VST` `rs60` turning negative ⇒ the lane is not a separate object · the equipment node (`GEV` −0.186, `ETN` −0.662 🔴) **staying** negative ⇒ the lane is two names, not a chain · **ERCOT peaker-net-margin breach** or **PUCT Emergency Pricing** activation ⇒ the statutory ceiling binds · a **hyperscaler capex guide-down** (the counterparties are **named in the filing**: AWS, Meta) · **`hy_oas` ≥ 3.10%** (merchant power is a levered credit) · a **Comanche Peak nuclear outage** (the PPA's physical asset) |
| **Dated catalysts** | **`P123` 2026-09-08** · **`P127` 2026-09-10** · **`S146` 2026-09-14** · and **`S152` 2026-09-14** (the ECB/long-end bracket registered today) is the row that most directly moves the other 13 names |

---

## §INFORMATION TECHNOLOGY — no sector-level bet is available, and that is the finding

Screener (56 names): **A. `ASML`** (RSI 27.7) · **`KEYS`** (30.2) · **`STX`** (31.2, px/200 **+43%**)
· **`HPE`** (35.6, px/200 **+56%**) · B and C empty. LIVE shortlist: **`DELL`**.

### §A · Numbers — `DELL`, and the two figures that must not be used

| | **`DELL`** |
|---|--:|
| price / 52w | **$524.14** (high $534.99 / low $110.22) ⇒ **−2.0% from the high**, and the 52-week range is **4.85×** |
| mcap · beta | $339B · **1.41** |
| forward P/E | **18.32** (trailing 30.49) · PEG 0.62 · P/S 2.24 |
| **P/B** | 🚫 **−236.95 — negative book equity. NOT USABLE**, stated rather than quietly dropped |
| **est. Δ, next quarter** | 🚨 **+78.7% in SEVEN DAYS** (4.05 → 6.87); current quarter only **+0.8%** in 90 days |
| analyst mean target | **$564.46 ⇒ +7.7%**; 5 SB / 14 B / 9 H / 0 S |

⚠ **The next-quarter estimate moved +78.7% in one week while the current quarter moved +0.8% in
ninety days.** That is a **post-print step-change**, not a trend, and it means the forward P/E of
18.32 is computed off a number that was 43% lower seven days ago. **Any "cheap on forward" reading of
`DELL` is a reading of a one-week-old revision.**

### §B · Thesis + freshness

> **There is no IT sector bet on this sheet, deliberately.** Sub-node dispersion is
> **+0.356 (Tech Hardware/Storage) to −0.538 (Semicap) = 0.894, against a sector `eqflow` of −0.195 —
> 4.6×**; on `rs60` it is **Systems Software +19.8 vs Semiconductors −14.9 = 34.7pp**. Per `W5` the
> sector label is the wrong unit and `SECTOR_DEEP_IT.md` says so. **The deliverable is a node board.**
> ★ `P101`'s SW/HW inversion was **recomputed independently this run and replicates to three
> significant figures** (SW **−4.46% / 4-of-19**; HW **+2.05% / 27-of-37**) — and the decomposition
> shows it was **a 5-session mean-reversion inside opposite 60-session trends**, not a regime change.
> ⚠ **Counter-evidence, same paragraph** (`C2`): the binding constraint has moved **out** of the
> sector — semicap, the classic bottleneck, is the worst node with **0/6 accumulating**, while the
> constraint that binds AI compute is **power and interconnection**, whose two measurable names
> (`GEV` −0.186, `ETN` −0.662) are both negative and whose middle (transmission, queue length) is
> **uninstrumented**.

- **`[freshness]` 🟡PARTIAL** — filled by ALPHA (see **§ALPHA A-1**). Re-check **2026-09-08** (`S127`/`S140`). 🚫 Cannot be 🟢LIVE: the FRESH gate's **age leg** admits nothing on this board — see §ALPHA A-0.

### §C · Flow / positioning (`asof 2026-09-04`)

| name | flow | OBV | rs20 | rs60 | surge | tag | note |
|---|--:|--:|--:|--:|--:|---|---|
| `DELL` | **+1.000** | +0.252 매집 | +15.9 | **+35.6** | **2.48** | 🟢 | ⚠ **momentum z only +0.70** — the *least* exceptional runner once normalized by its own 4.96% daily σ; chart shows a **bearish divergence** at RSI 59.0 |
| `HPE` (held) | +0.379 | +0.060 중립 | −1.9 | +8.1 | **2.18** | 🟡 | **Δ −0.421**, the board's largest negative; screener bucket A |
| `NVDA` (held) | −0.032 | −0.084 분산 | +3.3 | +8.8 | 1.01 | 🟡 | the Semis node's best `rs60` |
| **`AVGO`** (held) | **−0.356** | **−0.454 분산** | **−15.9** | −10.0 | 1.56 | 🟡 | 🚨 **the book's weakest holding on every axis.** `S127` settles **09-08** |
| `ANET` (held) | +0.047 | +0.067 중립 | +3.1 | **+21.5** | 0.60 | 🟡 | its node (Comms Equip) is **0/5 accumulating** |
| `ASML` | — | — | — | — | — | 🟡 | screener A at **RSI 27.7**; sits in the **worst node** (Semicap, 0/6 accumulating) |
| `ORCL` | — | 매집 | +8.4 | **−27.3** | 0.72 | 🟡 | prints **09-10**; implied **±11.8%**; short 2.8% float **covering** |
| `ADBE` | — | 중립 | +0.9 | +8.0 | 0.91 | 🟡 | prints **09-10**; implied **±8.1%**; short **5.1% float** covering, P/C **1.2 = hedged/fearful** |

⚠ **`ORCL` and `ADBE` are on the sheet as dated events, not as candidates.** Both implied moves sit
**outside** any threshold this desk could write (`D93` p85/p15 vs `SMH` = +3.15 / −3.66) ⇒
**pre-declared no-information**, which is why PREMORTEM did not bracket them.

### §D · Competition / peers

The node peer sets **are** complete inside the universe for Semis (14), Semicap (6) and Application
Software (12) — the one sector on this sheet where the peer work is possible. **What is missing is
the layer below**: neoclouds and optical component makers under the $10B floor.

### §E · Refutation + dated catalyst

| | |
|---|---|
| **What kills it** | A **hyperscaler capex guide-down** — the single event that breaks both the volume and the price leg (per `B4`, a **raise** confirms volume only and **cannot un-measure** the contract-price series, because the same buyers signed the caps) · **`hy_oas` ≥ 3.10%** — new this run, because the customers are now **debt-funded** (*"Big Tech's AI Debt Boom 'Driving' Treasury Yields Higher"*, 4 outlets, 09-07) · a **GICS reclassification** moving ≥3 of 56 names (`P101`'s own VOID) · `Systems Software` `rs60` (+19.8) turning negative ⇒ the inversion **was** a regime change |
| **Dated catalysts** | **`S127` 2026-09-08** (`AVGO`) · **`S140` 2026-09-08** (IT breadth) · **`ORCL`+`ADBE` print 2026-09-10** · **`S148` 2026-09-14** (does `P101`'s inversion survive its own two biggest prints?) |

---

## §CROSS-SECTOR LIVE — shortlist names outside the four DEEP sectors

`US_LIVE_SHORTLIST.json` (11 names, $10B floor, 🟢 filter). Six sit outside the DEEP sectors:

| name | sector | flow | OBV | rs20 | surge | `[FINRA]` | disposition |
|---|---|--:|--:|--:|--:|---|---|
| `DE` | Industrials | +0.911 | +0.18 매집 | +12.1 | 1.44 | −0.47 △ | ⚠ sits in the board's **worst 20-session sector** (`exc20` −5.04/−5.90). **Named, not carried** |
| `CTVA` | Materials | +0.861 | +0.27 매집 | +14.8 | 1.35 | −0.23 △ | ⚠ **`P102` settles Materials' two-name question on 09-09** — filing a view now pre-empts a live row (`D343`) |
| `TSLA` | Cons. Disc. | +0.828 | +0.17 | +8.2 | 1.29 | +1.19 △ | sector's `wflow` is **barred** (`AMZN` 40.2% flipper); `eqflow` −0.280 |
| `HOOD` | Financials | +0.783 | +0.21 매집 | **+31.3** | 1.21 | **−0.64 ✅** | momentum z **+1.28**; chart CONFIRMED-TURN with a **bearish divergence** and an **expanding** band |
| `RSG` | Industrials | +0.631 | +0.16 매집 | +4.2 | 1.22 | 🚨 **z +2.61 ⚡crowded-short** | **squeeze fuel, turn-conditional — explicitly NOT a candidate on its own** |
| `PG` | Cons. Staples | **+0.231** | +0.12 | +0.8 | **0.89** | −0.55 ✅ | 🚫 **TAG NOT CITABLE** — 🟢 on `velocity` alone at a below-gate surge (`D561`). **Carried as an instrument example, not as a name** |

---

## §F · Names set aside — ledger writes performed by this stage

**Rejections** (`reject_ledger add`, both `--revives-if` and `--recheck-date` supplied — the script
refuses without them):

| ticker | class | why (one line) | revives if | recheck |
|---|---|---|---|---|
| `XOM` | `I.테제반증` | Dead last of 16 in Energy on flow (**+0.027**, OBV −0.071 중립, `rs60` −0.3) **while carrying a velocity** (rank 19, inside the news wall) ⇒ the weakness is **measured, not filtered**; and the body read says its own CEO called Venezuela *"uninvestable"* in January, so the beneficiary story rests on a presidential remark | `flow_score` > +0.30 **AND** OBV turns 매집 | **2026-09-14** (`P139`'s settle) |
| `PCG` | `C.차트붕괴` | Board's highest `vol_surge` **3.32** on the sector's worst RS pair (**rs20 −17.7 / rs60 −20.6**) — volume into a collapse, the opposite of the screener bucket's implied shape | `rs20` > 0 **AND** `vol_surge` < 2.0 | **2026-09-21** |
| `RSG` | `D.약한손` | `[FINRA]` short z **+2.61 = crowded-short**. Squeeze fuel is turn-conditional and is not a thesis; `rs20` +4.2 is the board's weakest among the 🟢 set | a confirmed turn on `module_chart --read` **AND** short z falls below +1.5 | **2026-09-21** |

⚠ **`LLY`'s existing rejection is NOT re-filed** — it is a standing row with recheck **09-14** and
its revival condition (`flow_score` > 0 **AND** an OBV turn to 매집) is **unmet on both legs** (`flow_score` **−0.462**, `rs20` −2.7, `rs60` −5.0; the OBV leg reads 분산 — **RULE D6 exempt: this restates a pre-registered two-leg condition and the composite leg fails on its own**). **Re-filing a
live rejection would double-count it.**

**Missed** (`missed_ledger add`, filed at EVENT_ALPHA, listed here for the sheet's completeness):
`LNG` (`N.유니버스부재`, recheck 09-14) · `CEG` (`M.숏리스트탈락`, 09-14) · `VLO` (`M.숏리스트탈락`,
**09-11**, tied to `P140`'s settle).

⚠ **Boundary respected**: `CEG` and `VLO` went to the **missed** ledger because they were **excluded
by an instrument gate**, not set aside on a stated reason; `XOM`, `PCG` and `RSG` went to the
**rejection** ledger because a reason was stated. The script enforces the boundary (a ticker×date in
the rejection ledger is refused by `missed_ledger add`).

**Re-filed rather than removed** (the flow gate still passes, only the story broke):
- **`NVDA`** — thread 🔴FADING (Hugging Face 4→28→9→2→2) but the money verdict is **🟡 with OBV −0.084
  중립-to-분산, `rs60` +8.8** ⇒ **not a 🔴, so not DEAD.** New thesis line: *"an epicenter holding with
  a decayed catalyst and a flat tape."* Dated re-check **2026-09-10** (`S130`).
- **`XOM`** — its thesis line is rewritten from *"named Venezuela beneficiary"* to *"an integrated
  with the sector's worst flow and no operational Venezuela leg"*, **and then rejected on the new
  line** (above). The rewrite is recorded so the rejection is scored against the right claim.

---

## ✅ EXIT CHECK — BET

- [x] **ONE file, per-sector §A–§E sections.** Filename unchanged.
- [x] **Thesis-confirmation gate read FIRST** — `COMPANY_SCOREBOARD.md` exists but is **all-KR and 17 days old**, so **no US name is "confirmed"**; every US name is derived and that is stated. `module_report_tags` checked before concluding no coverage.
- [x] **Candidate set is a wide net**: DEEP thesis leaders ∪ **four sector screener runs** (Energy 2, Health Care 4, Utilities 4, IT 4 new names) ∪ **LIVE shortlist**, with the six cross-sector LIVE names given their own section.
- [x] **§A numbers cross-checked** (`module_fundamentals_us`: yfinance↔SEC XBRL **4/4 quarters within 5%** on `MPC`), **blanks stated as blanks** (`VLO` 30d breadth, `VLO` chart), and **two unusable figures named rather than dropped** (`DELL` P/B −236.95, `VLO` PEG 4.08).
- [x] **Every "cheap on forward multiple" claim carries its margin/denominator context** — `MPC`/`VLO` fwd ~12× placed against **estimates +49–120% in 90 days** and a crack level at the **95.6th percentile**; `DELL` 18.32× placed against a **+78.7% one-week** revision.
- [x] **§C flow/positioning read per candidate**, with **`asof` on every number** and **two tags declared non-citable** (`CVX`, `PG`) under `D561`.
- [x] **§E refutation + dated catalyst for every section**, and the one section with **no dated catalyst (Health Care) says so and flags `D560`** rather than reading the calendar's silence as absence.
- [x] **Epicenter-starter module NOT included, with the reason** — `cycle_exposure` reports **no top-rank GAP**; the rank-3 silence is named as a silence, not a pass.
- [x] **Sizing language: none.** Exposure state is quoted only as a **stored 09-04 value with its blank current field**; `kelly_size --ic` is barred (G6); concentration is quoted **12/11/10 with its `--days`**.
- [x] **Every name set aside is a scored record** — 3 rejections filed with **both** `--revives-if` and `--recheck-date`; 3 missed-ledger rows filed; the rejection/missed boundary respected and machine-enforced; **`LLY` not double-filed**; **two names re-filed rather than removed.**
- [x] **Linter run on this stage's own output** — see run log.

---

> P4 — analytical only. Zero buy/sell recommendations. Names are measurement subjects.

---

# §ALPHA — freshness gate (Stage 10 / L1·ALPHA, appended to this file per the protocol)

> **Separates "interesting" from "bettable NOW."** `theme-age` deterministic novelty ran **first**
> (token-0), `--scope foreign` on every call. **P4: no sizing, no buy/sell language.**

## A-0 · 🚨 The pipe was checked BEFORE the zero was read — and this run RESOLVES the F1 question

The stage's own warning: *"a gate that never fires looks identical to a universe with nothing in it."*
**PREFLIGHT G1's falsification probe ran and the pipe is alive**: 6/6 named probes immediately before
the sweep, with counts **moving** vs yesterday (NVIDIA 3,841→**3,761**, samsung 1,590→**1,471**,
Apple 1,267→**1,282**). A frozen collector returns frozen counts; this one does not.
⇒ **the zero below is admissible as a measurement, not as an outage.**

**And this run can say something the previous eighteen could not: the zero is a property of ONE LEG,
and it is measured.** 🟢FRESH requires **age ≤14 days AND acceleration ≥2×**. Across **22 themes**
measured this run:

| leg | themes clearing it | which |
|---|--:|---|
| **acceleration ≥ 2×** | **3** | `bond selloff` **5.93×** (base 247) · `Venezuela` 2.47× · `Fed hike` 2.06× |
| **age ≤ 14 days** | ★ **0** | the **minimum age measured all run is 47** (`Treasury selling`); next lowest **55** (`bunker fuel`), **81** (`refining margin`) |
| **both** | **0** ⇒ 🟢FRESH = **0, for a 14th consecutive foreign measurement** |

★★★ **The two legs have never been satisfied by the same theme, and the reason is now explicit: the
age leg measures the age of the WORD, not of the event** (`D543`, and `D559` registered this run).
`bond selloff` is the fastest-accelerating object this desk has ever measured on a foreign feed —
**and its word is ≥90 days old**, so the gate can never pass it. ⇒ **F1's zero is neither the market
nor a broken pipe. It is a gate specification that cannot fire on a mature vocabulary**, and it
should be read that way until a human changes the gate (**P5**).
⇒ **Consequence for this run: no bet may be tagged 🟢LIVE**, and that is a *gate* statement, not a
verdict about any name. Every tag below is 🟡 or 🔴 **for that structural reason first**, and then on
its own evidence.

## A-1 · Tags

| bet | theme read (`theme-age`, foreign) | live-evidence check | **tag** | residual / why | **re-check date** |
|---|---|---|:--:|---|---|
| **Energy — refining node** (`MPC` held · `PSX` held · `VLO` not held) | `refining margin` ⚪**ECHO 0.68×, age 81** (5th consecutive decelerating run) · `diesel` ⚪ECHO 1.04× · `fuel oil` ⚪ECHO 1.17× (base 203) · `bunker fuel` ⚪ECHO **age 55**, 0.86× | ★ **ECHO themes need STRONGER live evidence to survive, and here it exists and is one day old**: IEA **~9.6 mb/d** of Middle East refining capacity destroyed, a **Russian diesel export ban**, **record-low product inventories**, a **218 kb/d** bunker shortage vs 6 kb/d in 2025. ⚠ But `IEA refining capacity` as a *term* reads **⚫SILENT (0 hits)** — the fact is in bodies the term axis cannot see (`D10` class) | **🟡PARTIAL** | The **narrative axis and the physical axis point opposite ways**, and the desk's own B1 signal (two consecutive monthly rate declines: +37.6 → +13.0 → **+8.6%**) has **half-fired** against a quarterly rate at a 2-year max (+40.5%) | **2026-09-11** (`P140`) |
| **Energy — `SLB`** | `Venezuela` 🟡**ACCELERATING 2.47×** (down from 2.95× on 09-06), raw count **−5.3%** | Flow **+0.883** (sector #1), OBV +0.439 매집, `rs20` +14.2, `[FINRA]` z **−1.21 ✅ low-short/covering**, chart **CONFIRMED-TURN, OBV +87%, no divergence**, trigger `close>57.94`, swing-low stop **51.79**. Named in the body read as a near-deal party | **🟡PARTIAL** | 🚫 **Cannot be 🟢LIVE — blocked by the age leg (A-0), not by its evidence.** ⚠ `rs60` **−2.6** against `rs20` +14.2 = a 20-day turn inside a flat 60-day base — the residual is whether the turn holds | **2026-09-14** (`P139`) |
| **Energy — `COP`** | same `Venezuela` thread; the 09-06 run's only valid `chain-hop` in three runs (23 proximity / 24 body, **title 0**) | Flow +0.639, OBV +0.222 매집, `rs20` **+14.6**, `rs60` +5.8 — both RS positive. ⚠ Excluded from the shortlist by `vol_surge` **0.95** alone | **🟡PARTIAL** | Residual is the instrument, not the name: it enters on a surge ≥1.2 **or** on `P139` settling A | **2026-09-14** |
| **Health Care — biotech node** (`ALNY` `GILD` `VRTX` `AMGN` `REGN` `ABBV`) | 🚫 **No thread and no theme measured** — the sector produced **no BUILDING/REIGNITED thread** among the 99 alive, and `theme-age` was not run on a biotech term | **6/6 accumulating**, node `eqflow` +0.519, `rs60` +14.2 — the strongest node on the board by breadth. ⚠ **Against a falling denominator**: `ALNY` estimates **−9.4% (next year)**, revision breadth **2↑ / 11↓** | **🟡PARTIAL** | ⚠ **This 🟡 is weaker than the others and the file says so**: it has flow evidence and **zero narrative evidence**, and the desk **may not call that "quiet"** (247 of 299 names unmeasured; HLTH measured 5 of 32) | **2026-09-14** (`S133`) |
| **Health Care — `MDT`** | not measured | The sector's **only** 🟢, `vol_surge` **1.47** — the only name in 32 above the gate — but it sits in the sector's **weakest node** (Equipment, `eqflow` −0.044, 2/8 accumulating) | **🟡PARTIAL** | The tag is real (it clears the gate on merit) but **the node does not support it**. Residual: does Equipment's `eqflow` turn positive? | **2026-09-14** |
| **Utilities — `CEG` · `VST`** | `interconnection queue` 🔴**FADING 0.4×** · `Comanche Peak` ⚪ECHO 0.86× (base **26**) · `data center` ⚪ECHO **0.97×**, base 19,880 | Flow **+0.644 / +0.619**, **2/2 accumulating**, `rs60` **+17.2 / +1.6** — the only positive `rs60` pair in a 15-name sector. `CEG` fwd P/E 22.41 with estimates up only **+2.3%/+7.9%**, price **−27.6% from its high**, consensus **+16.5%**, beta **1.12** | **🟡PARTIAL** | 🚨 **The narrative axis actively contradicts the bet**: `interconnection queue` is the only **🔴FADING** read of the run, and it is the node the DEEP file names as the **binding constraint**. ⚠ Filing check: the PPA floor is **1,200 MW of ~44,000 = 2.7%, no revenue before Q4 2027**, and an **ERCOT ceiling** exists | **2026-09-10** (`P127`) |
| **IT — node board** (no sector bet issued) | `data center` ⚪ECHO **0.97×** · `AI capex` raw **−1.0%** · `AI debt` ⚪ECHO **0.52×** | Sub-node dispersion **0.894 vs a 0.195 sector move (4.6×)**; `P101`'s inversion replicated and re-read as a **5-session mean-reversion inside opposite 60-session trends** | **🟡PARTIAL** | ⚠ **No thread is building under the book's largest theme.** Residual is dated four ways: `S127` 09-08 · `S140` 09-08 · `ORCL`+`ADBE` print 09-10 · `S148` 09-14 | **2026-09-08** |
| **IT — `AVGO`** (held) | as above | **−0.356 flow, OBV −0.454 분산, `rs20` −15.9, `rs60` −10.0** — negative on every axis, the book's weakest holding | 🔴 **RESOLVED-adjacent, and deliberately NOT dropped** | ⚠ **`S127` settles it on 2026-09-08 — in one session.** Dropping a name the day before its own pre-registered row settles would destroy the observation (`D343`). **Held for the settle**, not on conviction | **2026-09-08** (`S127`) |
| **`NVDA`** (held) | Hugging Face thread 🔴**FADING 4→28→9→2→2** — and **not** a weekend artifact (the 28→9 collapse is inside the weekday block) | 🟡 tag, `flow_score` −0.032, `rs20` +3.3, **`rs60` +8.8**, `vol_surge` 1.01, OBV −0.084 | **🟡PARTIAL** | ⚠ **DEAD requires BOTH axes.** The story is fading; the money verdict is **not 🔴** (`rs60` positive, surge at 1.0, composite ~flat) ⇒ **re-filed with a new thesis line**, not dropped | **2026-09-10** (`S130`) |
| **`PG`** (Staples) | — | 🚫 **TAG REVOKED — instrument artifact.** 🟢 at `flow_score` **+0.231** and `vol_surge` **0.89** solely because universe rank 34 grants it a `velocity`, on a run whose `scoring.vel_axis` is **false** | 🔴 **REVOKED — and deliberately NOT ledgered in either direction** | **A rejection implies a judgement about the name; there is no judgement here, only a broken tag.** Writing it to either ledger would corrupt both scoreboards (`D561`) | n/a |
| **`RSG`** | — | `[FINRA]` z **+2.61 ⚡crowded-short** | 🔴 **DROPPED** | **Positioning gate: crowded-short is turn-conditional squeeze fuel, never a standalone bet.** ✅ **Logged as a ledger row** — `reject_ledger` `D.약한손`, revives on a CONFIRMED-TURN **and** short z < +1.5 | **2026-09-21** |
| **`XOM`** | `Venezuela` 🟡2.47× | Dead last of 16 on flow (+0.027) **while carrying a velocity** ⇒ measured, not filtered; the beneficiary story is a presidential remark against its own CEO's *"uninvestable"* | 🔴 **DROPPED** | ✅ **Logged** — `reject_ledger` `I.테제반증`, revives on `flow_score` > +0.30 **AND** an OBV turn | **2026-09-14** |
| **`PCG`** | — | `vol_surge` **3.32** (board high) on `rs20` **−17.7** / `rs60` **−20.6** | 🔴 **DROPPED** | ✅ **Logged** — `reject_ledger` `C.차트붕괴`, revives on `rs20` > 0 **AND** surge < 2.0 | **2026-09-21** |

## A-2 · Momentum-only and positioning stamps

| name | stamp | basis |
|---|---|---|
| `MPC` | ★ **NOT momentum-only** | The accumulation axis **agrees** on both instruments (sweep OBV +0.621 매집; chart OBV 20d slope **+52%**, no divergence) and the move is **+3.27 z** on its own 20-day σ — the board's genuine outlier |
| `PSX` | ⚠ **momentum-with-a-divergence** | Same accumulation agreement, **but the chart carries a bearish RSI divergence `MPC` does not**. Downgraded within 🟡 and reported as a disagreement, **not** converted to a tape trade |
| `MSTR` | 🚨 **MOMENTUM-ONLY** | Largest raw 20-day move (**+42.8%**) but **only +1.53 z** normalized, chart OBV **중립 +2%**, Bollinger **expanding 60.9%**, turn NEUTRAL/CHOP. `C25` **partial** disagreement (sweep 매집 +0.326) |
| `NEM` | 🚨 **NO TAG ISSUED — `C25` OUTRIGHT DISAGREEMENT** | Sweep OBV **+0.144 매집** vs chart **분배, 20d slope −58%**, with a bearish divergence. **A C-grade disagreement downgrades and is REPORTED as a disagreement** (`D6`); here the two instruments contradict outright, so **"unresolved" is the honest state, not "neutral"** |
| `DELL` | ⚠ **flow rank-1 overstates it** | Board-top `flow_score` **+1.000** but momentum z only **+0.70** — the least exceptional runner once normalized — plus a chart bearish divergence and a **+78.7% one-week** estimate step-change |
| `HOOD` | ⚠ momentum, low conviction | z +1.28, chart CONFIRMED-TURN with a bearish divergence and an **expanding** band |
| `RSG` | 🚨 **positioning gate — crowded-short** | z +2.61 ⇒ hard-stop stamp mandatory if it ever re-enters; not a standalone bet |
| `CVX` · `PG` | 🚫 **tags not citable** | `D561` — 🟢 on `velocity` at below-gate `vol_surge` |

## A-3 · Carry-forward list — tags follow the NAME, not the sector's turn

Handed to the next run's inheritance packet **regardless of whether their sector holds a DEEP slot**
(measured origin: `006360` carried an ALPHA tag, its sector rested, and **+12.3% over five sessions
went unowned**):

`MPC`(09-11) · `PSX`(09-11) · `VLO`(09-11) · `SLB`(09-14) · `COP`(09-14) · `ALNY`+biotech node(09-14) ·
`MDT`(09-14) · `CEG`(09-10) · `VST`(09-10) · `NVDA`(09-10) · `AVGO`(**09-08**) · IT node board(09-08).

⚠ **Every 🟡 above carries an explicit re-check date and every date is tied to a pre-registered row**
— none is "revisit later."

## A-4 · Action tickets — written, and the gap in them named

`action_bracket.py` wrote `llm_outputs/2026-09-07/ACTION_TICKETS.md` (day-folder root, script-owned):

| ticket | condition | name | DRY-RUN size | stop |
|---|---|---|---|---|
| `BRACKET::A_cool` | IF **Aug PPI (D−3)** prints toward cool | `NVDA` | 10 sh @ ~$230.36 (risk 1.5%) | $214.23 (−7.0%) |
| `BRACKET::B_hot` ★asym-hedge | IF **Aug PPI (D−3)** prints toward hot | `MPC` | 3 sh @ ~$388.90 (core risk 0.8%) | $361.68 (−7.0%) |

**Both sides armed — no one-way ticket.** ⚠ Sizes are **illustrative DRY-RUN**; a human executes
separately and this desk never sends an order.

🚨 **Two gaps in the ticket file, named rather than left:**
1. **The ECB decision (2026-09-10) is not in it**, because `action_bracket` reads
   `CATALYST_WATCH.json` and **`catalyst_calendar` carries no foreign central-bank dates** (`D562`).
   **This run's own mandatory both-sides bracket for it is `S152`** (`TLT` 3-session, A ≥ +0.913% /
   B ≤ −1.124%, settle **09-14**) and it lives in `handoff/SCENARIOS_US.md`, **not** in the ticket
   file. ⇒ **the two artifacts disagree about what the week's binaries are.**
2. **`D518` reproduces**: `action_bracket` selects on **date proximity** (nearest binary = PPI) while
   PREMORTEM selects on **information content** (which is why PPI was *not* separately bracketed —
   it already sits inside `S148`/`S149`). **Nothing says which governs**, and this run does not
   invent an answer (**P5**).

## ✅ EXIT CHECK — ALPHA

- [x] **Every §B tag filled with an evidence label and a date.** Four 🔴 issued: **three logged as ledger rows** with class + `--revives-if` + `--recheck-date` (`XOM` `I.테제반증` 09-14 · `PCG` `C.차트붕괴` 09-21 · `RSG` `D.약한손` 09-21), and **one deliberately NOT ledgered** (`PG`) with the reason stated — a revoked instrument tag is not a judgement about a name.
- [x] **Every 🟡PARTIAL carries an explicit re-check date**, and every date is tied to a pre-registered row rather than to a feeling.
- [x] **Every ALPHA-tagged name is on the carry-forward list independently of its sector's DEEP slot** (A-3).
- [x] **Momentum-only and positioning flags stamped** (A-2), including one name (`NEM`) where **no tag was issued at all** because the two instruments disagree outright.
- [x] **(US) `ACTION_TICKETS.md` written** — both-sides brackets present; **no cycle-GAP core-starter, because `cycle_exposure` reports no top-rank GAP**; and the ticket file's two structural gaps are named.
- [x] 🚨 **The pipe was probed before the zero was read** (G1: 6/6 alive, counts moving) **and the F1 zero is resolved as a gate-specification property**, with the numbers: 3 themes clear the 2× acceleration leg, **0** clear the ≤14-day age leg, minimum measured age **47**.
