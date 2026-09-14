# SECTOR_DEEP_IT — Information Technology · industry_US · 2026-08-30 (Stage 8 / L1·DEEP)

> **PREMORTEM-PROMOTED 5th SLOT.** ROTATION left IT at **Neutral** and routed it here rather than a
> normal DEEP slot; PREMORTEM Lens 1 promoted it. Prior DEEP: `llm_outputs/2026-08-29/industry_US/
> SECTOR_DEEP_IT.md` — read first, not re-printed. That file's structure (7-node value chain,
> horizon-dependent split, `M1079`–`M1081`, §3 held-name brackets) is carried by reference; this file
> spends its length on the **delta** and on **whether the sector label survives a second session.** P4.

## §0 · Mandate, answered in one line: **it is two sectors, and the split got sharper overnight**

> *"Is IT one sector or two?"* — **Two.** `wflow` **+0.034** flips sign the moment `NVDA`'s 19.4%
> weight is stripped (`wflow_ex_top1` **−0.015**); `eqflow` **−0.033** (rank 5/11, negative); breadth
> **0.05** (3 greens of 56) and **all three greens are software** (`CRM` `INTU` `MSTR`); `SMH` `exc60`
> **−15.31pp** vs `SPY` is the single worst 60-day ETF leg on this desk against `XLK` **−7.38pp**.
> Grouping by GICS sub-industry (n=19 software, n=37 semis/hardware) confirms it on means: `rs60`
> software **+4.39** vs hardware **−17.44** (**21.8pp** cohort gap, benchmark **`SPY`**). ⚠ **But the
> gap is an approximation, not a clean cut** — intra-cohort range is **79.7pp** in software (`SHOP`
> +33.4 to `APP` −46.3) and **64.8pp** in hardware (`MSI` +17.0 to `ON` −47.8), both **3–4× the
> between-cohort gap**. §1 carries this forward as a continuation of `M1081`'s horizon test.

## §1 · Delta vs 08-29 — the equal-weighted signal flipped sign in one session

| metric | 08-27 settle (yesterday's file) | 08-28 settle (this file) | delta |
|---|---|---|---|
| `wflow` | +0.008 | **+0.034** | +0.026, still `NVDA`-sized |
| `wflow_ex_top1` | −0.121 | **−0.015** | **+0.106 — improved** |
| `eqflow` | +0.060 | **−0.033** | **−0.093 — flipped sign** |
| breadth | 0.07 (~4 green) | **0.05 (3 green)** | narrowed by one name |
| `top1_flips_sign` | True | True | unchanged, still `NVDA` |

★★ **`eqflow` flipping from clearly positive to negative while `wflow_ex_top1` improved is the
session's real signal, not a matched pair — it says the mega/large-caps (ex-`NVDA`) that dominate cap
weight held up better than the median name.** 08-28 was the **Warsh Jackson Hole hawkish session**
(context: `NVDA` −4.58%, `HPE` −3.90%, `ANET` −2.87%, all 5m-proxy closes) — a **duration** sell-off
that hit both cohorts, which is consistent with a median-name eqflow flip **without** a software/semis
reversal: greens stayed 100% software (`CRM` `INTU` `MSTR`), and the losers span both cohorts
(`AVGO` 🔴, `WDC` 🔴, `AMAT` 🔴 in hardware; no software name is 🔴 today).

⇒ **The horizon test from `M1081` (yesterday's KPI #4) reads on a second session as: intra-cohort
dispersion still exceeds inter-cohort dispersion (§0), so "software vs semis" remains a real but
noisy axis — not resolved to a clean binary, and not falsified either.** A genuine 1-day intra- vs
inter-node re-test (the `exc1`-level test yesterday ran) needs per-name single-session excess, which
this run's data pull does not carry — flagged, not fabricated.

## §2 · Players ∪ thematic (mcap ≥ ~$2B) — unchanged map, changed color

Full 56-name map and the 7-node value chain are carried from 08-29 unmodified; only the standouts:

- **Software — 3 greens, all `Application Software`**: `CRM` **+1.000** (`rs20` +36.3, `rs60` +32.4,
  `OBV` +0.305 매집, **`vol_surge` 1.64 — the only volume-confirmed green on the whole board**) ·
  `MSTR` +0.883 (`rs20` +33.5 but `rs60` **−1.4** — a 60-day laggard riding a 20-day pop) · `INTU`
  +0.850 (`rs20` +10.3, `rs60` +13.0). `NOW` +0.572, `SHOP` +0.456 and `PLTR` +0.506 (`rs20` **+48.4**,
  the widest 20-day excess in the sector) sit just under the green line at 🟡.
- **Semis/equipment — the 🔴 cluster**: `AVGO` **−0.717**, `AMAT` **−0.839**, `WDC` **−0.839**, `KLAC`
  −0.647, `MCHP` −0.667, `NXPI` −0.769, `TXN` −0.825, `CSCO` −0.922 (worst score on the board). All
  carry `OBV 분산` — this is not a flow-score artifact, the distribution is visible in accumulation
  terms too.
- **Memory — internally split**: `MU` +0.346 (`OBV` +0.126 매집) and `SNDK` +0.358 (`OBV` +0.100 매집,
  `rs20` **+19.3**) both accumulating on a falling `rs60` (−15.6 / −20.9); `WDC` **−0.839 🔴분산**
  is the outlier — same commodity, opposite flow signature. §6 below resolves the tension with
  fundamentals, not sentiment.
- **Optical — accumulating, unmeasured by the registry**: `LITE` +0.550 (`OBV` +0.287 매집, `rs20`
  **+22.3**) and `COHR` +0.324 (`OBV` +0.121 매집, `rs20` +3.2 but `rs60` **−35.2**, the widest
  OBV/RS divergence in the sector). §10 addresses this directly — it is this file's mandated item.

## §3 · IR anchors — three names read from primary filings, Item 1A used for anti-signals

### `MU` — 10-K (FY2025, filed 2025-10-03, period 2025-08-28)

Risk bullets (Item 1A, verbatim top 3 of 10): *"volatility in average selling prices of our
products"* · *"a range of factors that may adversely affect our gross margins"* · *"realizing expected
returns from capacity expansions."* **These are the company's own words for the price-cycle risk this
file is required to test (§6/§7).**

★★★ Item 1 (primary, verbatim): *"Due to volatile industry conditions, our customers are generally
reluctant to enter into long-term, fixed-price purchase contracts. We typically enter into long-term
agreements with our customers with acknowledgment that pricing, quantity, and other terms will be
periodically negotiated to reflect market conditions."* **This is §7's answer, sourced, not inferred.**
Also: top-10 customers ≈ **half of total revenue** in each of the last 3 years — concentrated, but not
contractually locked.

### `HPE` — 10-K (FY2025, filed 2025-12-18, period 2025-10-31) — the fresher of the three filings

Risk bullets (Item 1A, top 5 of 10): go-to-market/as-a-Service execution · **dependence on third-party
suppliers, contract manufacturers, and single/limited-source suppliers** · cybersecurity · competitive
intensity · **Juniper Networks merger integration.** ★ Item 7 MD&A, verbatim: *"the AI servers business
is growing at a faster pace, [but] because graphics processing units represent a large portion of the
solutions, the pricing is very competitive and margins are limited."* **This is a primary-source
anti-signal that directly contradicts a naive "AI server growth = margin tailwind" read on `HPE` — the
growth is real, the margin capture is explicitly disclaimed by the company.**
🚨 ★★ Goodwill test, verbatim: *"The excess of fair value over carrying amount for the Server reporting
unit was 11%. The Server reporting unit has a goodwill balance of $10.2 billion."* **An 11% cushion is
thin — a modest downward revision to Server-unit projections (which the same paragraph ties explicitly
to "a significant or sustained decline in our stock price") risks a goodwill impairment.** This is a
dated, quantified anti-signal ahead of the **09-03** print that neither book's holding thesis carries.
Also: *"AI systems demand in the midst of persisting data center space availability constraints
continued to drive significant AI backlog"* — **the disclosed bottleneck is DATA CENTER SPACE, not
chip supply** — ties directly into §9's Australia item.

### `AVGO` — 10-K (FY2025, filed 2025-12-18, period 2025-11-02)

Risk bullets (top 5 of 10): highly cyclical semis industry *"undergoing profound change due to AI"* ·
**"a significant reduction in demand or loss of one or more of our significant customers"** ·
dependence on a limited number of contract manufacturers · **"our ability to maintain or improve gross
margin."** Item 1, verbatim: *"Sales to distributors accounted for 48% of our net revenue... aggregate
sales to our top five end customers, through all channels, accounted for approximately 40% of our net
revenue"* for FY2025 **and** FY2024 — unchanged concentration, and the company states plainly it
*"expect[s] to continue to experience significant customer concentration."* **This is the primary-source
number behind `W4`: the Alphabet custom-ASIC relationship and the `MRVL` dual-source thread (`S116`,
carried) sit inside a ~40%-of-revenue top-five bucket that `AVGO` itself flags as a named risk, not
this desk's inference.**

## §4 · Value chain — 7 nodes (carried structure), bottleneck confirmed, cross-sector chains marked

`EDA/IP → foundry → merchant silicon → custom ASIC → networking/optics → system OEM → software/workload`

**Binding constraint = node 5, networking/optics — unchanged from 08-29.** Confirming evidence this
run: node 5's `ANET` is `OBV` 매집 with `rs20` +5.3 (positive, if modest) while node 3 (`NVDA`) is
`OBV 분산`; node 5's `LITE`/`COHR` show the sector's sharpest OBV-vs-RS60 divergence (§2). The scarce
input in this buildout is still the interconnect layer, not the GPU itself.

★ **Cross-sector chain 1 (marked per protocol)**: node 5/6 → **power → transformers → copper** — `VRT`
and `ETN` (both held, both 매집 per `EVENT_ALPHA` Card 6, carried) sit downstream of the same buildout
demand as node 5.
★ **Cross-sector chain 2 (marked per protocol)**: **switch → optical module → laser** — `ANET` (switch
layer, node 5, `rs20` +5.3) → `LITE`/`COHR` (module layer, node 5, `rs20` **+22.3** / +3.2) → laser
diode / component suppliers, which this desk's `us_top300` universe does not currently price
(§10 — the registry gap and the universe gap are the same gap, described from two angles).

## §5 · Chain-hop candidate — body-proximate, flow cross-checked, passes the mcap floor

**`AAOI` (Applied Optoelectronics, mcap ≈ $9.0bn)** — not in the desk's 56-name IT universe, not
headline-named in any tracked bracket. Body-proximate co-mention, 08-24: *"Applied Optoelectronics
Sinks 12% on $600M Equity Offering, **Lumentum and Coherent Drop 5%**"* (`yahoo_finance`) — a dilutive
equity raise at `AAOI` produced a **sympathy sell-off in both `LITE` and `COHR`**, i.e. part of the
optical cohort's weak `rs60` (§2) is traceable to a name-specific financing event one node over, not a
sector-wide demand read. **Flow cross-check**: FINRA short-vol `AAOI` 50.2% vs its own 20-day base
56.1% (z **−0.98**, i.e. below its own norm) with a **+2.5▲** 5-day trend — short pressure easing from
an elevated base but rising again over the last week. ⇒ **Candidate registered, not promoted**: it
explains an anti-signal (why `LITE`/`COHR` fell on 08-24 despite accumulating `OBV`) rather than
proposing a new long idea, consistent with `W4`'s customer/co-mention discipline (§0 rule 5).

## §6 · 🚨 Price-cycle rule — the second derivative, read on revenue (labelled honestly) and on margin

No DRAM/NAND spot-price index tool exists in this build; the QoQ rate series below is **quarterly
revenue growth**, i.e. **price × volume blended**, not a pure ASP series — stated as a limitation, not
disguised as one.

**`MU` quarterly revenue and its own rate of change** (SEC XBRL, `module_fundamentals_us`):

| quarter end | revenue ($bn) | QoQ growth | Δ QoQ (2nd derivative) |
|---|---|---|---|
| 2025-08-31 | 11.32 | +21.7% | — |
| 2025-11-30 | 13.64 | +20.6% | **−1.1pp** (mild deceleration) |
| 2026-02-28 | 23.86 | **+74.9%** | **+54.3pp** (step-change acceleration, HBM ramp) |
| 2026-05-31 | 41.46 | +73.7% | **−1.2pp** (near-flat, marginal deceleration) |

**Reading**: the series is dominated by a discontinuous step-change (HBM mix shift into the
data-center segment, per the 10-K's own MD&A language, §3), not a smooth cycle. The most recent
quarter shows the rate barely decelerating (−1.2pp off a 74.9% base) — **one soft data point, not the
"two consecutive declines" the rule requires to call a turn.** The regime call is not confirmed or
denied by this series; it is **inconclusive on the current print count**, stated as such.

**Margin-history percentile (`scripts/margin_history.py`, own-history, annual FY)**:

| ticker | current FY | gross margin | own-history percentile | vs own peak |
|---|---|---|---|---|
| `MU` | FY2025 | 39.8% | **71st** | **−19.1pp** (peak 58.9%, FY2018) |
| `WDC` | FY2026 (ended ~Jun-26) | **48.9%** | **100th — all-time high** | 0.0pp |
| `SNDK` | FY2026 | **71.5%** | **100th — all-time high** (4-yr series) | 0.0pp |
| `AVGO` | FY2025 | 67.8% | ~90th | −1.1pp (peak 68.9%, FY2023) |
| `HPE` | data stale — SEC XBRL series stops at FY2018 | — | **unmeasurable, `C3`** | — |

★★★ **The tension the mandate is pointing at**: `WDC` and `SNDK` are printing **fresh all-time-high
gross margins** on a FY basis (48.9% / 71.5%) while their `rs60` sits at **−24.6 / −20.9** (benchmark
`SPY`) and `WDC` carries a `🔴분산` flow tag. **Margins are not decelerating at the fundamental level
— the stock is pricing a FUTURE rollover that the trailing-FY accounting data does not yet show.**
That is a forward-looking price call, not a confirmed second-derivative signal, and it should be
named as such rather than backed into as if the fundamentals already turned.

## §7 · 🚨 Contract-terms rule — read from the filing, answered, not asserted

> 🚨🚨 **ORCHESTRATOR CORRECTION — the section below reads the SUPERSEDED filing and its conclusion is
> OVERTURNED. The text is left standing (`D48`: append what broke it, do not edit it away).**
>
> The section quotes **`MU`'s FY2025 10-K, period 2025-08-28, filed 2025-10-03**. `handoff/RESEARCH.md`
> already records that **the FY26Q3 10-Q, nine months later, says the OPPOSITE**, and it records the
> reversal explicitly: strategic customer agreements are **take-or-pay with binding multi-year
> volumes**, carry a **ceiling at ~the 2Q CY2026 market price and a floor for the term**, and
> management states that at **floor** pricing gross margin runs *above any prior cycle's peak*.
> The desk's own note names the FY2025 10-K by name as the document that said *"customers reluctant to
> enter fixed-price contracts; terms periodically renegotiated"* — **which is verbatim what §7 below
> quotes.** `module_disclosure_us MU` confirms a **10-Q inside the last 90 days** (1 of 28 filings).
> ⇒ **The contracting regime CHANGED between the two filings.** The desk logged that change as the
> thing no file had noticed; this run's DEEP then re-derived the pre-change state from the older
> document and reported it as new.
>
> **Three consequences, all binding on BET and ALPHA:**
> 1. 🚫 **§7's conclusion "no floor/ceiling, no take-or-pay" is WITHDRAWN.** The current disclosed
>    structure is take-or-pay with a floor/ceiling band.
> 2. 🚫 **§8's "checked, does not apply" is WITHDRAWN and REVERSES.** The take-or-pay/RPO frame the
>    desk applies to `KMI`, `LNG` and `VST` **does** apply to memory — which is exactly the
>    frame-transfer the desk had never made in 21 files.
> 3. ⚠⚠ **§6's QoQ rate series may NOT be read as a clean demand signal.** With a ceiling pinned to a
>    dated market price, a decelerating contract-price rate is **arithmetic hitting a cap**, not
>    demand weakening — and that is the precise warning `RESEARCH.md` attaches to the desk's evidence
>    #1 for its standing regime call. **`P111` is unaffected as a registered row** (its observable is
>    an equity excess return, not a price series), but any narrative reading of §6 is.
>
> ★ **The lesson is the transferable part and it is filed as `D417`**: *a filing-read that CONTRADICTS
> a recorded desk finding must name the filing's period and check whether a later filing supersedes
> it, before the contradiction is reported as a discovery.* The agent did quote its source and date
> honestly, which is the only reason this was catchable in one grep.



**`MU`'s own 10-K (§3, quoted verbatim) states customers are "generally reluctant to enter into
long-term, fixed-price purchase contracts"** and that pricing/quantity terms are **periodically
renegotiated to market**. There is **no disclosed floor/ceiling band and no take-or-pay structure** —
the opposite of `KMI`'s RPO or `LNG`'s tolling. ⇒ **§8's frame-transfer question is answered directly
by the filing: a contractual ceiling is NOT producing the QoQ pattern in §6, because no such ceiling
is disclosed.** Whatever deceleration eventually shows up in the rate series will be a **demand/supply
signal, not arithmetic hitting a cap** — the opposite conclusion from 08-29's `D408`, which had marked
this `unknown` for lack of a filing read. **This run closes that gap for `MU`.** `WDC`/`SNDK` were not
independently filed-checked this run (same competitive-market structure is a reasonable prior given
they sell into the same customer base, but is not verified from their own text — marked `C3`).

## §8 · Frame-transfer — applied to memory, for the first time on this desk

The desk applies take-or-pay/RPO lock-in reasoning to `KMI`'s RPO, `LNG`'s tolling and `VST`'s 20-year
PPA floor across 21 files. **Checked here and it does not apply to `MU`** (§7) — memory sells on
periodically-renegotiated market terms, not multi-year fixed contracts. **This is a pass, not a gap**:
the frame was tested and correctly rejected for this sub-sector, rather than silently never asked.

## §9 · Customers named, spend checked — and the national-statistic denominator weighed

**`NVDA`'s disclosed supplier commitments — $279bn total, ~$160bn memory** (5 outlets, carried from
08-27→08-29) — is the demand-side, issuer-sourced **numerator** for `MU`/`WDC`/`SNDK`. Against it:
*"Australia's Capex Drops as Data Center Spending Hits Air Pocket"* (bloomberg, 08-28) is an
issuer-agnostic **national-statistic denominator** on the same broad AI-buildout demand thesis.
★ **Per the rule, the national statistic cannot on its own falsify the issuer-sourced commitment** —
Australia is one country's data-center capex, not global hyperscaler capex, and `NVDA`'s number is a
direct supplier commitment, not a survey estimate. **Weighed, not dismissed**: it is a legitimate
one-country data point suggesting buildout breadth is uneven, consistent with `HPE`'s own MD&A
language (§3) that the AI backlog constraint is **data-center space, not chip supply** — a
geographically-uneven capacity constraint is exactly what a one-country capex air-pocket would look
like if the true bottleneck is power/space siting rather than global demand. **Both facts point the
same direction (site/power scarcity), which is a materially different read than "AI demand is
slowing."**

## §10 · 🚨 The optical gap (`D250`), addressed directly with numbers

`data/cycles/cycle_registry.json`'s only relevant cycle (**"AI-compute / semiconductors"**) lists
epicenter `{NVDA, AVGO, AMD, MU, TSM, ASML, AMAT, LRCX, KLAC, MRVL, ANET, SKHY, SMCI, SMH}` and
adjacent `{CEG, VST, NRG, TLN, GEV, ETR, NEE, BWXT, ETN, VRT, PWR}` — **confirmed by direct read this
run: `LITE`, `COHR` and `AAOI` appear in neither list.** `ANET` (switch layer) is in the epicenter;
the optical-module/laser layer one node downstream (§4, chain 2) is not — **verified absent, not
merely reported absent.** What that hides: `LITE` `OBV` +0.287 매집 with `rs20` **+22.3** (the
sector's 3rd-widest 20-day excess) and `COHR` `OBV` +0.121 매집 on `rs20` +3.2 but `rs60` **−35.2**
— both look like accumulation-under-a-broken-60-day setups, structurally identical to the `VRT`/`ETN`
pattern the registry DOES track (§4). Because they carry no epicenter/adjacent tag, no cycle-level
sizing, thesis-continuity, or `find-cycle` sweep currently touches them. **This is the 15th
consecutive run with this gap; it is a registry-construction issue, not a data-availability one — the
flow and OBV data exist and are used in this file.**

## §11 · Estimate momentum — description only, confound stated, no signal used

The desk's own measured result (carried, not re-derived): same-quarter revision `+0.403` vs 90-day-back
`−0.299`, both above the IC noise floor but **pointing opposite ways**; ex-IT control spread `+9.4pp
→ −1.1pp` ⇒ **the effect is an IT-sector loading, not an independent revision axis, and this caveat
binds hardest in an IT file.** `HPE`'s own EPS trend shows a large upward move over 90 days (0q
estimate 0.579 → 0.932; +1y estimate 2.736 → 4.083) and `MU`'s similarly (0q 22.66 → 31.28). **Stated
as description of what analysts did, not cited as a leading signal on either name** — per the rule, it
carries zero independent weight here.

## §12 · Track KPIs and anti-signals — dated observables

| # | KPI / anti-signal | observable | kills what |
|---|---|---|---|
| 1 | **`AVGO` 09-02 print** | implied move **±8.09%** (09-04 exp, K=367.5, straddle 29.83); customer concentration ~40% top-5 (§3, primary) | the `S116`/`S132` dual-source-discount thesis |
| 2 | **`HPE` 09-03 print** | implied move **±11.23%** (09-04 exp, K=52.00, straddle 5.87); P/C OI **2.19×**; **11% goodwill cushion on a $10.2bn Server-unit balance** (§3, primary — new this run) | any "AI server backlog = clean upside" read |
| 3 | 🚨 **`HPE` still absent from `catalyst_calendar --days 14`** | re-checked this run, still only `AVGO` D-3 appears | the desk's own coverage of its book — 2nd consecutive run confirmed missing |
| 4 | `P111` | `EW{MU,SNDK,WDC}` exc10 vs `SPY`, 08-28→09-14, A ≤−3.00pp / B ≥+5.00pp — **not re-frozen** | the `[inferred]` regime call, resolved neither way by §6 |
| 5 | `P113` | \|`XLK` 5d − `XLU` 5d\| through 09-08 — **not re-frozen** | concentration-call vs macro-call framing |
| 6 | `eqflow` sign | next settle: does eqflow re-cross to positive, or does the 08-28 flip persist ≥2 sessions | §1's "median-name risk-off, not cohort reversal" read |
| 7 | `AAOI` | next print/filing — does the $600M raise fully clear, or is there a follow-on | whether §5's sympathy-sell explanation for `LITE`/`COHR`'s 08-24 leg holds |
| 8 | node 5 registry | `LITE`/`COHR`/`AAOI` added to `cycle_registry.json` epicenter/adjacent, or explicit reason given for exclusion | §10's "construction issue" reading |

## §13 · What this file does NOT claim

- 🚫 **No sector verdict change** — ROTATION's `N` stands; §0/§1 sharpen the two-way split, they do
  not overturn it, and no bracket here is re-frozen.
- 🚫 **No margin-collapse call on memory** — §6/§7 read the filing and the fundamentals; the QoQ
  series shows one soft data point, not a confirmed turn, and no ceiling-arithmetic story applies
  (contract terms checked, absent).
- 🚫 **No revision-momentum signal used as evidence** anywhere above (§11) — description only.
- ⚠ **`TSM` (foundry, node 2) remains outside `us_top300`** — unmeasurable, not absent, carried from
  08-29 unchanged.
- ⚠ **`WDC`/`SNDK` contract-terms not independently filed-checked** — `C3`, same competitive-market
  prior as `MU` assumed but not verified from their own text.
- ⚠ **`HPE` SEC-XBRL margin series stops at FY2018** — trailing margin percentile for `HPE`
  unmeasurable by this tool; the goodwill-cushion figure (§3) is used instead as the dated anti-signal.

## ✅ EXIT CHECK (this file)

- [x] Mandate answered in one line (§0, two sectors, caveat quantified) → **delta-led** flow read vs
  08-29 (§1, `eqflow` sign flip) → players ∪ thematic mcap ≥$2B (§2, + `AAOI` §5) → **3 primary
  filings** (`MU`/`HPE`/`AVGO`, Item 1A anti-signals used, §3) → 7-node chain, bottleneck + both
  cross-sector chains marked (§4) → chain-hop candidate, flow cross-checked (§5) → KPIs (§12).
- [x] Sub-sector dispersion stated both directions (§0/§1: 21.8pp cohort gap vs 65–80pp intra-cohort).
- [x] Price-cycle QoQ rate series tabulated, labelled revenue not pure ASP (§6); contract-terms rule
  read from `MU`'s own 10-K and quoted, frame-transfer question answered "checked, does not apply"
  (§7/§8).
- [x] Customers named, spend checked; national-statistic denominator weighed, not dismissed (§9).
- [x] Optical gap (`D250`, 15th run) addressed with numbers, registry read directly, confirmed absent
  (§10).
- [x] EDA lead/lag **not** re-inherited (no such claim made). Estimate revision used as description
  only, IT-confound caveat repeated (§11). KPIs dated, both `AVGO` 09-02 and `HPE` 09-03 (§12).
