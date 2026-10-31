# L1 · COMPETITION — industry structure and competitive position (stage)

> Big stage (replaces DEEP, 2026-10-31). One agent per focus sector, all in **one message** (parallel).
> Order inside each agent: **players → value chain → share · price · capacity · customers → contract terms →
> bottleneck and kill conditions.** Flow is not read here — FLOW_CHECK does that afterwards.
> **Reads (primary sources)**: 10-K Item 1/1A/7 · 사업보고서 «II. 사업의 내용» · competitors' filings and IR ·
> customers' disclosed capex · industry price series · 수주 공시.
> **Output**: `SECTOR_DEEP_{code}.md` × N (filename kept — `module_report_tags` normalizes on it) — **cap 12 KB each**.
> **Next stages use**: BET takes §share/price/capacity/customers per name as its «competition» column and the
> lens `filing` rows; the kill conditions become BET §E and PREMORTEM/ALPHA observables.

## Calls (modules — direct, no flow tools)
- Players and chain: `python -X utf8 -m module_industry_map "<sector thesis terms>"` (5–8 nodes, sub-suppliers) ·
  L3 [competitors](../L3_functions/competitors.md) (chain position: bottleneck / beneficiary / bystander).
- Business text: US `module_business_us <TKR> --full --json` (Item 1A = anti-signal list) · KR `module_disclosure
  <6자리> --business-report`. 🚨 KR: never `module_business --include-dart` (it scrapes the DART frameset shell).
- Orders and contracts: `module_disclosure <6자리> --category contract --days 90` (`--guidance <조>` gives progress
  vs the annual order plan) · US contract text sits in the 10-Q exhibit index when the 8-K says «filed as exhibit».
- Anything a module cannot give (competitor IR deck, price series page, customer capex release):
  [web_errand](../L2_modules/web_errand.md).

## What this stage does — per sector
1. **Players**: large caps ∪ thematic names (bounded as in EARNINGS §1). Mark the headline layer — it is the
   crowded layer by construction.
2. **Value-chain map** left→right, 5–8 nodes; bottleneck = the *binding constraint*, not the strongest demand.
   Mark cross-sector chains (AI → power → transformers → copper).
3. **The competition table** — one row per node leader and its two nearest competitors:
   `revenue growth · operating margin (from EARNINGS) · share or rank (source) · price action (raised / held / cut,
   dated) · capacity added (dated, units) · top customers and their disclosed spend`.
   A cell nobody publishes is written `not disclosed` with the place looked; a cell not looked for is a fail.
4. **Contract terms before any mean-reversion call** — take-or-pay volumes, floor/ceiling bands, contracted share,
   read from the filing. Measured on MU FY26Q3 10-Q: take-or-pay with binding multi-year volume, a ceiling near
   the 2Q CY2026 market price and a floor for the term — while the FY2025 10-K said customers avoided fixed-price
   contracts. ⚠ A contractual ceiling flattens the QoQ price series: check for a band before reading a
   deceleration as demand weakening.
5. **Bottleneck, track KPIs and kill conditions** as dated observables (earnings or price-series observables
   first; a flow observable may be added, never alone).
6. **Continuous vs rotating sector** (MACRO's pick): continuous → lead with the delta since the prior file (new
   print, contract, guide, price move) and cite unchanged structure by path; rotating → full fresh map.

## Carry rules (from `handoff/RESEARCH.md`; binding here)
- **Price-cycle nodes are read on the second derivative** (lens L1): tabulate the QoQ change series. Measured:
  server DRAM contract prices +90~95% → +58~63% → +13~18% QoQ while supply stayed short.
- **Peak-margin / low-multiple trap** (lens L2) — multiple next to margin percentile, from EARNINGS.
- **Name the customers and check their disclosed spend** (W4) or give their print dates.
- **Inherited lead/lag claims are tested or tagged `[unverified]`** (W2 — archived in `handoff/_archive/2026-10-31/RESEARCH.md`, binding here). Measured: «EDA leads semis 12–18 months»
  gave same-month +0.63 vs lag-12 +0.05 on 199 months.
- **State sub-sector dispersion** (W5). Measured: memory +12~14% vs GPU/ASIC +2.0~2.2% in one session; if the
  spread exceeds the sector move, the sector label is the wrong unit.
- **Frame transfer**: name a frame trusted elsewhere (take-or-pay, RPO lock-in, regulated return) and say whether
  it applies here (take-or-pay was applied to KMI/LNG/VST in 21 files, to memory in 0).
- ⚠ Neither the estimate-revision axis (IT confound) nor the sweep flow axes (M224 noise band; lens 5/32) may carry
  a competition verdict.

## ✅ EXIT CHECK
- [ ] One `SECTOR_DEEP_{code}.md` per focus sector (incl. any PREMORTEM-promoted leg), written by parallel agents.
- [ ] **Competition table present**: per node leader + 2 competitors, the six columns filled from sources or
      `not disclosed (looked: <where>)`. Zero rows = failed stage.
- [ ] **Share or rank, price action and capacity each answered at least once per sector** with a dated source.
- [ ] **Customers named and their disclosed spend checked** (or print dates given).
- [ ] Every «margin must mean-revert» claim names the contract terms read from the filing; `unknown` only with
      the filing searched and cited; and blocks the mean-reversion verdict.
- [ ] Commodity nodes carry a QoQ rate-of-change series; ceiling check stated before reading it as demand.
- [ ] One frame-transfer question answered; lead/lag claims measured or `[unverified]`; dispersion stated.
- [ ] Continuous-track files lead with the delta; each file ≤ 12 KB; no MACRO/EARNINGS table restated.
- [ ] Linter run: `python -X utf8 scripts/report_lint.py <file>`.
