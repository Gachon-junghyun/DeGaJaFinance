# SECTOR_DEEP_STPL — Consumer Staples · 2026-08-10 (Mon) · settled 2026-08-07

> ROTATING track — **first full map this sector has ever received** in the desk's recorded DEEP_LOG
> history, honouring the 2026-08-08 pre-commitment ("STPL — ★next run's first rotating pick"). No
> lead-from-delta exists; this is a fresh map. Bench **SPY** named on every relative print (C1). Both
> halves on every YoY (C2). OBV never carries a proposition alone — paired with RS20/RS60 (D6).
> Zero buy/sell language, zero sizing (P4). `n_axes 3 · vel_coverage 0.0` this run — no news-velocity
> or theme-freshness claim appears anywhere below, and **this sector is never called "quiet"**: 431
> single-outlet foreign clusters went unopened today and that tier is UNSCORED, not low-scored
> (`MACRO_REPORT.md §D-1`).

## §0 · Inherited state and what this file answers

**MACRO/ROTATION hold STPL at UW−**, demoted 08-08 on the worst eqflow and the worst Δ on the board.
Today (`SECTOR_FLOW_US.json`, asof settled **2026-08-07**): **worst of 11 sectors on both wflow
(−0.220) and eqflow (−0.184)**, **0🟢 of 18**, XLP exc5 **−3.43** vs **SPY** / exc20 **−1.24**
(`MACRO_REPORT.md §C`, settled 08-07). ⚠ **Δ and "new 🟢" are disqualified this run** (`D232` — the
only same-mode baseline is 2026-07-20 and holds 5 tickers) — nothing below cites either.

Four questions drive this file: **(1)** sector-wide or name-narrow? **(2)** the n=19→18 composition
anomaly ROTATION flagged and could not explain. **(3)** would a hot-CPI risk-off tape actually bid
Staples here, on fundamentals rather than reflex? **(4)** are the two missed-ledger rechecks (ADM,
CTAS) approaching their entry conditions?

---

## §1 · Q1 — sector label vs sub-node: the spread test

`SECTOR_FLOW_US.json` decomposed into five sub-nodes (own calc from the 18 names' `flow_score` and
`mcap`; reproduces the file's sector total exactly — wflow −0.220, eqflow −0.184 — as a methodology
check):

| Sub-node | n | tickers | eqflow | wflow (cap-w) | mcap |
|---|---|---|---|---|---|
| **Staples food** | 3 | MDLZ, HSY, ADM | **+0.005** | **+0.077** | $148.4B |
| Tobacco | 2 | PM, MO | −0.085 | −0.082 | $393.5B |
| Household & personal care | 4 | PG, CL, KMB, KVUE | −0.098 | −0.059 | $490.6B |
| Beverages | 4 | KO, PEP, CCEP, KDP | −0.293 | −0.146 | $620.5B |
| **Staples retail** | 5 | WMT, COST, TGT, KR, SYY | **−0.318** | **−0.371** | $1,486.2B |
| **Sector total** | **18** | — | **−0.184** | **−0.220** | $3,139.2B |

**The spread test, stated per the stage rule**: sub-node eqflow spans +0.005 to −0.318 = **0.323pp
spread**; wflow spans +0.077 to −0.371 = **0.448pp spread**. **Both exceed the sector's own move
(0.184 / 0.220 in magnitude).** ⇒ **The sector label is the wrong unit of analysis this run, and the
UW− is not one reading — it is at minimum two: a genuinely negative retail/beverage core and a
flat-to-positive food/confectionery fringe.**

**Is retail's −0.318 just WMT (top1, 29.7% of the *sector's* cap)?** No — recomputed ex-WMT within the
retail node alone: **eqflow −0.302, wflow −0.353** (barely different from −0.318/−0.371 with WMT in).
**COST is independently at −0.396 and KR at −0.789**; only TGT (−0.015) and SYY (−0.008) sit near
flat. **The retail node's weakness is broad within the node, not a WMT artifact** — three of five
retail names are deeply red on their own. (Sector-level ex-top1: `wflow_ex_top1 = −0.152`, matching
`SECTOR_FLOW_US.json` directly.)

---

## §2 · Q2 — the MNST arithmetic: composition improved the number; scoring mode overwhelmed it

ROTATION flagged that STPL's n fell 19→18 (MNST the sole `dropped_missing_axis` name), that MNST
scored **−0.60** on 08-08, and that removing a negative name should have made eqflow *less* negative —
**yet it got worse (−0.165 → −0.184).** Decomposed against the archived **08-08** `SECTOR_FLOW_US.json`
(4-axis, same 08-07 settled bar):

| Step | eqflow | Δ | Mechanism |
|---|---|---|---|
| 08-08, n=19 (incl. MNST −0.600) | **−0.1653** | — | baseline |
| Hypothetical: drop MNST only, hold the other 18 names' 08-08 scores | **−0.1412** | **+0.024** | **composition alone IMPROVES eqflow**, exactly as arithmetic requires when a below-average name (−0.60 vs mean −0.165) is removed |
| 08-10 actual, n=18, 3-axis (velocity dead) | **−0.1838** | **−0.043** vs the hypothetical | **scoring-mode shift on the remaining 18 names**, net |

**Net change 08-08→08-10: −0.019** (= +0.024 composition − 0.043 scoring-mode). ⇒ **the deterioration
is scoring-mode, not composition — composition alone would have improved the number.**

The scoring-mode shift is not diffuse. Per-name 08-08→08-10 delta, all 18 common names:

| Name | 08-08 flow (velocity) | 08-10 flow (no velocity) | Δ |
|---|---|---|---|
| WMT | −0.067 (vel 1.35) | −0.381 | **−0.314** |
| COST | −0.047 (vel 1.45) | −0.396 | **−0.349** |
| KO | +0.343 (vel 3.57) | +0.124 | **−0.219** |
| PG | +0.003 (vel 1.08) | −0.063 | −0.066 |
| PM | −0.257 (vel 0.68) | −0.076 | **+0.181** |
| *(13 other names, all `velocity=None` on 08-08)* | — | — | **0.000, every one** |

**Sum of the 18 deltas = −0.767 → −0.0426 per name** — matches the residual to three decimals
(−0.1412 − 0.0426 = −0.1838 ≈ actual −0.184). **The mechanism is exactly SWEEP §2's**: STPL has **5
names inside the market-cap top-50** (WMT, COST, PG, KO, PM — precisely the five with non-null
`velocity` on 08-08), and those are the only five whose score moved at all; the other 13 are
byte-identical between runs, same as the three zero-top-50 sectors SWEEP found frozen. **Four of the
five top-50 names got *more* negative when velocity was removed (WMT/COST especially); only PM
improved.** ⇒ **STPL is the ninth sector (of eight named in `SWEEP_READ.md §2a`) whose flow number
moved on the identical price bar purely because it holds top-50 names — this file adds the STPL
instance SWEEP's table left implicit.**

---

## §3 · Flow → players → IR anchor

**Players** (mcap ≥ $2B floor cleared by all 18; news-window check run — a single OR-mode pull across
the nine smaller names returned 431 hits/7d with ≥2 hits each, `[measured]`): all 18 sector names
qualify. Ranked by mcap: **WMT $932.5B · COST $421.9B · KO $374B[live] · PG $337B[live] · PM $290B[live]
· PEP $194.1B · MO $115.4B · MDLZ $77.2B · CL $71.6B · TGT $59.4B · CCEP $42.9B · KDP $41.9B · SYY
$37.6B · ADM $36.2B · HSY $35.0B · KVUE $34.8B · KR $34.7B · KMB $34.0B** (settled-08-07 mcaps from
`SECTOR_FLOW_US.json`; the three `[live]`-tagged figures are today's `module_fundamentals_us` pull and
differ slightly from the settled bar — flagged per the price-filter rule).

**IR anchor, primary filings** (`module_business_us`, `module_disclosure_us`):
- **WMT 10-K** (filed 2026-03-13): ~280M weekly customers, 10,900+ stores/19 countries, strategy keyed
  to **EDLP** (everyday-low-price) — a structural commitment to price leadership that caps unit-margin
  expansion by design. `[measured, SEC XBRL]`
- **PG 10-K** (filed **2026-08-04**, five days old): **Sales to Walmart and affiliates = ~16% of total
  net sales in 2026, 2025 and 2024 — no other single customer above 10%. Top ten customers = ~43% of
  net sales (2026, 2025), 42% (2024).** `[measured, SEC XBRL]` ⇒ **the retail node is not just a
  sub-sector — WMT is also PG's largest customer**, concentrating channel bargaining power on the same
  name that anchors the retail node's flow weakness. PG's 10-K separately discloses **"some single-
  source suppliers"** for raw/packaging materials.
- **PG, KMB, KVUE** all filed Q2 earnings 8-Ks inside the last 10 days (07-29, 08-04, 08-06
  respectively; Item 2.02, `module_disclosure_us`) — the sub-sector's information flow is current, not
  stale.

---

## §4 · Value chain — nodes and the binding constraint

Demand is not absent anywhere in this chain — every node moves real, recurring consumer spend. The
binding constraint is **volume/pricing power on the demand side**, not production capacity, and it is
the same constraint recurring across nodes rather than seven unrelated stories:

1. **Agricultural inputs — ADM.** Binding constraint: **not feedstock availability** — ADM **raised
   its FY26 profit outlook twice** (08-04, biofuels-policy tailwind) `[bloomberg/wsj/nasdaq 08-04]`, an
   improving fundamental. **Binding constraint is price/flow credibility**: settled flow is **−0.517,
   🔴분산**, RS20 **−7.2**, RS60 **−9.9** — the tape has not followed the guidance raise
   (`[measured, SECTOR_FLOW_US.json]`, D6-paired). One outlet asked the same question directly:
   *"Is ADM's Rally Getting Ahead of Its Policy Tailwind?"* `[nasdaq 08-05]`.
2. **Branded food/confectionery manufacturers — MDLZ, HSY.** The sector's only accumulating names:
   MDLZ OBV **매집 +0.086**, RS20 **+4.0**; HSY OBV **매집 +0.258**, RS20 **+2.6**
   (`[measured, SECTOR_FLOW_US.json]`, D6-paired). Binding constraint: **input-cost volatility** —
   cocoa prices swung on both sides of the 7-day window (*"Ghana Cocoa Production Concerns Boost
   Cocoa Prices"* 08-03 → *"Larger Ghana Cocoa Supplies Weigh on Prices"* 08-05 → *"Cocoa Prices Slip
   as Overbought Conditions Spur Technical Selling"* 08-04) `[nasdaq body, 7d window]` — not a demand
   problem.
3. **Beverages — KO, PEP, CCEP, KDP.** The weakest branded node (eqflow −0.293). Binding constraint:
   **GLP-1-linked calorie-demand headwind**, live and named in the feed but **already headline-crowded**
   (§5) — not a hidden mechanism.
4. **Household & personal care — PG, CL, KMB, KVUE.** Binding constraint: **retail-channel
   concentration**, disclosed above (§3) — PG derives ~16% of sales from one customer and 43% from ten.
   Margins are not the constraint here (§6): KMB gross margin sits at its **90th-plus percentile** of
   its own 13-year history.
5. **Tobacco — PM, MO.** Binding constraint: **regulatory/volume, not margin** — PM's post-2016
   (excise-tax-accounting-consistent) gross margin is at its **90th percentile of 10 years** (§6); the
   constraint is unit-volume decline structurally offset by pricing, a mature-market dynamic rather
   than a live catalyst.
6. **Food distribution — SYY.** Binding constraint: **restaurant/food-service volume pass-through**
   — flow near flat (−0.008) with **vol_surge 1.69, the highest in the sector**
   (`[measured, SECTOR_FLOW_US.json]`), a genuine activity signal without a directional OBV read
   (분산) to confirm it either way.
7. **Staples retail / mass merchandise — WMT, COST, TGT, KR.** Binding constraint: **traffic/basket
   growth in a trade-down environment** — this is the node carrying the sector's worst numbers (§1),
   broad-based, not WMT-concentrated.
8. **End consumer / household demand.** The node every above node is priced against. Two
   simultaneous, body-sourced pressures this window: **GLP-1-driven appetite suppression** compressing
   snack/beverage calorie volumes (§5), and **grocery trade-down/private-label** dynamics (*"Kroger
   makes a pricing move Costco and Walmart will love"* 08-07, *"Publix struggles to reverse concerning
   customer behavior"* 08-08) `[nasdaq/yahoo_finance bodies]`. **Tariff refund checks are arriving**
   (*"Trump Tariff Refunds Just Topped $100 Billion"*, 08-07, multi-outlet) but a companion piece
   frames the net effect as underwhelming for consumers (*"'Your refund: $0': Companies claim billions
   in tariff refunds, months after Trump floated $2,000 checks"*, `[yahoo_finance 08-07]`) — a mixed,
   not clearly stimulative, signal for the end node.

**Answer to the node-level binding-constraint question**: strong demand is not the constraint at any
single node; **unit-volume growth against two structural headwinds (GLP-1 appetite suppression,
trade-down) is the constraint that recurs across nodes 3, 7 and 8**, while nodes 4 and 5 face a
channel-concentration / regulatory constraint that is largely priced and margin-neutral.

---

## §5 · Chain-hop candidates — none cleared the body-proximate bar for STPL

`module_news_data chain-hop GLP-1 weight-loss --days 7 --scope foreign --mode or` (168 articles
scanned, ±300-char proximity window):

- **HEADLINE-NAMED (already crowded, not a chain-hop)**: **COST** 1 headline/7 body · **KO** 4/4 ·
  **CCEP** 4/4 · **WMT** 3/3 · **MDLZ** 1/0. The GLP-1↔Staples link is a **named** theme in the desk's
  own feed, not a hidden co-mention.
- **★ CHAIN-HOP CANDIDATES** (title 0 + ≥2 body-proximate co-mentions): **NVDA, JPM, ABBV, GS, AAPL,
  MSFT, MRK, JNJ, UNH, BMY, MMM** — **zero of these are Consumer Staples names.** ⇒ **no legitimate
  STPL chain-hop candidate exists this run under the body-proximate rule; a co-mention alone (e.g. any
  Staples ticker appearing near "GLP-1" in a headline) is explicitly not a candidate per this file's
  own instruction, and none of the eleven qualifying names sit in this sector.**
- A second attempt (`tariff refund consumer`, same parameters) returned no output inside the tool's
  120s window and is **logged as non-responsive, not cited as evidence** — consistent with the
  chain-hop tooling anomaly `DEEP_MATR §3` already logged on 08-08.

---

## §6 · Q3 — would a hot-CPI risk-off tape actually bid Staples here?

**The setup PREMORTEM handed this file**: `S73` branch H (hot/hawkish 2026-08-12 CPI: ΔDGS2 ≥ +0.15 ∧
ΔHY OAS ≥ +0.10) is registered against INDU/FIN/STPL — but **its equity leg is keyed to
median{JPM,BAC,XLI} ≤ −1.50pp, and the desk has no Staples observable registered for either branch of
S73 at all** (`BLINDSPOT_PREMORTEM.md §2a`). The reflex says a hawkish/hot print triggers a defensive
rotation into Staples — the opposite of the sector's current UW−. **Bracket registration is
PREMORTEM's stage (P4/ownership); this file only assesses the fundamentals question and hands the
observation upstream.**

**Beta**: WMT 0.60 · COST 0.86 · PG 0.38 · KO 0.34 · PM 0.40 · PEP 0.36 `[measured, module_fundamentals_us,
live pull 08-10]`. **All classically low-beta.** Mechanically, a broad equity selloff on hot CPI would
see these names decline **less** than SPY in points — which registers as a positive excess return **vs
SPY** by construction (C1), independent of any fresh capital rotating in.

**Revision breadth, 90-day EPS-estimate momentum** (`module_fundamentals_us`, current + next quarter):
**WMT −0.7% / −0.6% · PG −4.3% / −0.9% · KO ~0.0% / −0.1% · PM −7.3% / −0.2% · PEP −5.9% / +0.9% ·
COST +0.9% / +1.1% (the lone improver)**. ⇒ **Four of the six mega-cap names are being cut on
estimates right now, independent of Tuesday's CPI print.** This is the opposite of what a "safe,
predictable earnings" defensive thesis requires.

**Margin history** (`scripts/margin_history.py`, SEC XBRL annuals, own-history percentile):

| Name | Latest FY gross margin | Own-history percentile | Read |
|---|---|---|---|
| WMT | 24.2% (FY26) | **26.3%** (n=19) | below-median, recovering off FY2023's 23.5% trough |
| PG | 50.2% (FY26) | **57.9%** (n=19, ex the FY2012 accounting-break outlier) | above-median |
| KO | 61.6% (FY25) | **80.0%** (n=10) | near-peak |
| PEP | 54.1% (FY25) | **52.6%** (n=19) | at-median |
| PM | 67.1% (FY25) | **90.0%** (n=10, post-2016 excise-tax-accounting break — pre-2016 figures are a different accounting object and excluded) | near-peak |
| KMB | 36.0% (FY25) | **76.9%** (n=13) | near-peak |

**No margin-erosion story exists across the six largest names measured.** ⇒ **the risk to the sector's
current UW− is not a cost-structure crisis — it is top-line/volume, sitting on GLP-1 and trade-down
pressure (§4) even as gross margins hold at or above their own medians.**

**Pre-positioning check — is the tape already staged for a defensive rotation ahead of CPI?** OBV state
across all 18 names, D6-paired with RS20: **9 of 18 in 분산 (distribution)** — WMT (−4.2), COST (+1.0),
PEP (−1.2), TGT (+8.3), KDP (−7.7), SYY (−1.9), ADM (−7.2), KVUE (−3.7), KR (−8.7) — **7 in 중립**, and
**only 2 in 매집 (MDLZ +4.0, HSY +2.6) — neither a mega-cap "flight to quality" name.** None of WMT,
PG, KO, PM show accumulation. `[measured, SECTOR_FLOW_US.json §names]`

**Answer, stated with its hedge**: mechanically, low beta means a hot-CPI equity selloff would likely
see Staples **fall less than SPY** (a positive excess return by definition, not new buying) — a
different, narrower claim than "the market is rotating in." The flow evidence shows **no current
pre-positioning** for a genuine defensive rotation (worst breadth and worst two flow axes on the board,
distribution outweighing accumulation 9:2, zero mega-cap accumulation), and the revision-breadth
deterioration on four of six mega-caps argues against the earnings-safety premise that would justify a
durable bid even if branch H fires. **Margins are the one leg of the classic defensive thesis that
genuinely holds up on the primary data — the case's weak leg is estimates and volume, not cost
structure.**

---

## §7 · Q4 — missed-ledger rechecks: ADM and CTAS, due 2026-08-16

`out/missed_ledger.jsonl`, both filed 2026-08-02, both `--sample prospective`, both due **2026-08-16**:

⚠ **CTAS is Industrials (`Diversified Support Services`), not Consumer Staples** —
`SECTOR_FLOW_US.json §names` confirms it directly. The two rows share a due-date and were filed the
same day, which is presumably why they travel together in `STANDING_VIEW.md`, but **CTAS does not
belong in a Staples deep-dive on sector grounds** and is covered here only because this file was
handed the recheck.

| Name | `enters_if` (registered 08-02) | Current reading (08-10) | Verdict |
|---|---|---|---|
| **ADM** | *"Staples is promoted above N by ROTATION on a flow number, OR ADM rs60 vs SPY turns positive while the green tag holds"* | Staples is **UW−**, one notch **below** where it stood 08-02 (not promoted) · ADM rs60 vs SPY **−9.9** (was −3.1 on 08-02 — moved further negative) · tag **🔴분산**, not green | **Not approaching on either leg — both moved away.** ADM's own fundamentals improved in the interim (FY26 profit outlook raised twice, 08-04) without the price/flow condition following (§4 node 1) |
| **CTAS** *(Industrials, mis-filed here)* | *"a 4Phase company analysis is produced, OR it clears the green gate while rs60 vs SPY holds above +15"* | rs60 vs SPY **+18.0** (was +17.7 on 08-02 — **now clears the +15 threshold**) · tag still **🟡중립** (`vol_surge` 0.86, the same gate the 08-02 filing named as the sole blocker) · no 4Phase found in this run's file set | **One leg of the OR-condition is now met (rs60 +18.0 > +15) but the compound condition requires BOTH clearing the green gate AND rs60 above +15 — vol_surge still blocks the green tag, so the entry condition as registered is not satisfied.** This is the closer of the two rechecks |

---

## §8 · Track-KPIs and anti-signals — dated observables

| # | Observable | Reads today | Falsifies / confirms |
|---|---|---|---|
| 1 | Sub-node spread (eqflow, §1) | food +0.005 vs retail −0.318 = 0.323pp spread vs sector −0.184 | Spread compressing below the sector's own move = the "one sector, one reading" framing becomes valid again |
| 2 | Retail node ex-WMT (§1) | eqflow −0.302 vs −0.318 with WMT | A widening gap (ex-WMT much less negative) would mean the retail weakness IS concentrating into WMT; today it is not |
| 3 | STPL top-50 names (WMT/COST/PG/KO/PM) vs the other 13, on velocity's return (§2) | 5 moved this run, 13 frozen | If `vel_coverage` recovers >0%, re-test whether the same 5 names revert toward their 08-08 levels — confirms the scoring-mode mechanism rather than a new one |
| 4 | ADM rs60 vs SPY (§7) | **−9.9** | Crossing to positive while the 🔴 tag lifts = ADM's `enters_if` fires |
| 5 | STPL ROTATION verdict (§7) | UW− | Any promotion above N fires ADM's other `enters_if` leg |
| 6 | CTAS `vol_surge` (§7) | **0.86** | Crossing ≥1.2 with OBV 매집 and rs20 positive intact clears the green gate and fires CTAS's `enters_if` |
| 7 | S73 branch H macro leg (CPI 2026-08-12) | ΔDGS2 ≥ +0.15 ∧ ΔHY OAS ≥ +0.10, un-fired | No Staples equity leg exists in the current registration (§6) — if PREMORTEM adds one, the pre-positioning evidence here (9 분산 / 2 매집, 0🟢/18) is the baseline to test it against |
| 8 | WMT next earnings | **2026-08-20** `[measured, module_fundamentals_us]` | First live test of whether the −0.7%/−0.6% 90d revision drift (§6) resolves before or after the print |
| 9 | Mega-cap revision breadth (WMT/PG/KO/PM/PEP) | 4 of 5 negative on 90d EPS momentum (§6) | A shift to net-positive across ≥3 of 5 would be the first fundamental leg supporting a genuine (not just low-beta-mechanical) defensive case |
| 10 | Cocoa price direction (input to MDLZ/HSY, §4 node 2) | swung both directions inside the 7-day window | A sustained rise would test whether the sector's only two accumulating names (MDLZ, HSY) hold their OBV 매집 state |

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
