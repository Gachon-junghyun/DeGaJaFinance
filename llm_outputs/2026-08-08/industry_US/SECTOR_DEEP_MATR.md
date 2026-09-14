# SECTOR_DEEP_MATR — Materials · 2026-08-08 (Sat) · settled 2026-08-07

> ROTATING track, first full map in six runs (last 2026-08-03). Zero buy/sell language, zero sizing (P4).
> Benchmark named inline on every relative number (C1). Both halves of every print (C2).

## §0 · VERDICT ON S57-ANNEX — the ex-NEM number, computed independently

**`S57`**: XLB 5-session excess vs **SPY** > +1.9pp fires branch A ("Materials outperforms because the
dollar leg flipped and the crowded-long leg didn't cap it"), any settled close through 08-12. Current
reading **+1.307**, **0.59pp from firing.**

**Recomputed from scratch** — SSGA's dated 08-06 XLB holdings file (25 names, weights) + yfinance
settled closes (`auto_adjust=False`), 07-31 close → 08-07 close:

| Quantity | 5-session excess vs **SPY** |
|---|---|
| **XLB, as reported** | **+1.307** (recompute matches the desk's number exactly — methodology cross-validated) |
| **XLB ex-NEM** (NEM weight 6.60%, removed and rest reweighted to 100%) | **+0.194** |
| **XLB ex-{NEM, ALB, FCX}** (weights 6.60% / 1.98% / 5.75%, combined 14.34% removed) | **−0.485** |

**Removing one name — 6.6% of the fund's weight — takes the sector's own falsifier from 0.59pp-short-
of-firing to 1.71pp-short-of-firing.** Removing three names flips the sign. **This is decisive: the
ex-NEM number does NOT clear +1.9 — it does not clear even +0.5.** The annex's W5 claim is CONFIRMED,
not weakened, by independent recomputation.

**And the three excluded names are not one story wearing three tickers — they are three unrelated
single-commodity trades stacked into one ETF number:**
1. **NEM** — gold spot +2.4% to a 7-week high on falling Fed-hike odds `[economictimes 08-07]`, while
   its **own** estimate revisions are cut 9-to-1 (§2.3) — a macro/rates trade, and PREMORTEM Lens 3
   independently flagged it exhausted on a non-price axis.
2. **ALB** — a **company-specific** Q2 beat (adj. EPS $3.75 vs $3.20 est.) on a **real lithium-price
   recovery** (benchmark lithium ~$21,000/t, ~2× year-ago) plus AI-data-centre **grid-storage** demand
   `[oilprice/yahoo_finance 08-05/06]` — nothing to do with gold, dollars, or copper.
3. **FCX** — copper, where the CFTC COT (Tue 08-04 close) shows spec net long at the **100th
   percentile of the trailing year, BUILDING (+9,842)** — the crowded-long leg S57 branch A explicitly
   says "did not cap it" is, on the freshest instrument, the single most crowded reading of the year.

⇒ **If S57 branch A fires, it fires on a rates trade in a single gold name, riding alongside an
unrelated lithium re-rating and a copper future at its own yearly-maximum long — not on Materials.**
And the **08-14 XLB option-implied move is ±2.1%** against a 0.59pp gap — the observable sits inside
its own noise band before any of the above is applied. **Verdict: S57-ANNEX holds. S57 is not
re-frozen; this section adds a SIXTH independent leg (decomposition-by-recomputation) to five already
on record (flow · dollar positioning · copper positioning · revision breadth · options-noise).**

---

## §1 · The value chain, node by node — binding constraints, not demand

Demand is not the constraint anywhere in this chain right now; every node below has a real, live
demand story. The binding constraint is elsewhere in each case.

1. **Precious-metals mining — NEM.** Demand/price: not binding (gold at a 7-week high). **Binding
   constraint: estimate credibility.** 30d revision breadth is **current-qtr 0↑/9↓ · FY 1↑/9↓ ·
   next-FY 2↑/13↓, FY estimate −8.9%/90d** — analysts are cutting the numbers while the tape rallies.
   `[measured]`
2. **Industrial-metals mining — FCX (copper).** **Binding constraint: positioning, not physical
   supply.** COT spec long **100th percentile, building**, while FCX's own OBV is **−0.071 (중립, NOT
   매집)** `[module_flow — D208, module named]` — the futures market is more committed to this trade
   than the equity tape is. `[measured]`
3. **Lithium/specialty — ALB.** **Binding constraint: durability of the price recovery**, not the Q2
   print (a clean beat). Lithium at ~$21,000/t is still **well below the ~$30,000 earlier-year peak**
   `[oilprice 08-06]` — the binding question is whether AI-driven grid-storage demand holds the floor
   as EV demand normalises. `[measured/inferred]`
4. **Steel — NUE, STLD, CLF.** ⚠⚠ **X (US Steel) sanity-checked and confirmed DELISTED** (no yfinance
   price data; Nippon Steel completed the take-private) — **excluded from this map; do not carry it on
   any screen.** **Binding constraint: NOT demand, NOT tariff policy — the desk's own detection gate.**
   See §2.1. `[measured]`
5. **Commodity chemicals — DOW, LYB, CE, EMN.** **Binding constraint: structural overcapacity.** A
   "global overbuild of base chemicals and plastics," bottoming in 2025 with the glut "not fully solved
   until 2030," being worked off via **plant closures in Europe/UK/Germany** faster than planned
   `[fortune 07-30]`. Layered on top: a short-term unwind of the Hormuz-driven North-American
   ethane-cost advantage that had briefly lifted margins (XLE exc5 **−6.95pp vs SPY**, same window).
6. **Fertilizer/ag — CF, MOS, CTVA.** **Binding constraint: feedstock-cost inflation vs
   priced-for-perfection expectations**, and it is **not the same constraint across the leg** — §2.2.
7. **Coatings & industrial gases — SHW, PPG, IFF, ECL, APD, LIN.** Internally split: **SHW/PPG are
   1-session leaders (+2.27 / +1.57pp vs SPY)**; **LIN is the flow board's worst Materials name
   (🔴분산 −0.683, rs20 vs SPY −9.9)** and **APD is flat-to-negative (rs20 −1.1)**. **Binding
   constraint for the gases pair: industrial/hydrogen capex-cycle exposure — LIN and APD are NOT
   participating in whatever is lifting the rest of the sector.** `[measured]`
8. **Packaging — BALL, PKG, IP, SW, AMCR.** Split the other way: **SW +2.27pp / IP +1.98pp** vs
   **BALL −5.75pp (5-session)**. **Binding constraint: beverage-can (BALL) vs containerboard/coated
   paper (SW, IP, PKG) input-cost and volume divergence** — aluminium vs pulp economics, not one story.

**Cross-sector chains flagged, both unconfirmed by flow (§3):** AI → power → transformers → **copper
(FCX)**; Texas data-centre build → **cement/aggregates (VMC, MLM)**.

---

## §2 · Assignments 3–5

### 2.1 · ★★ Steel divergence — resolved: real strength, wrong instrument catching it

**SLX exc20 vs SPY +8.57pp vs XLB exc20 +1.45pp — a 7.1pp lead, recomputed and confirmed.**
⚠ **SLX is not a clean US-steel proxy**: top holdings are **BHP 7.4% / RIO 7.0% / VALE 7.0% / NUE 6.6%
/ STLD 5.6% / Nippon Steel 5.5% / ArcelorMittal 5.4%** — a **global diversified-miner ETF**. But
decomposing 20-session excess vs **SPY** name by name: **NUE +17.48 · STLD +12.47 · RIO +9.24 ·
MT +8.49 · BHP +8.26 · VALE −0.70.** **NUE alone outruns every global miner in the fund** ⇒ SLX's
strength is a genuine blend of US-steel-specific and global-iron-ore strength, **not** a composition
artifact inflating a weak US story.

**Primary source — NUE 10-K (FY2025, filed 2026-02-25)**: *"Backlogs for the steel mills segment at
the end of 2025 were at historically high levels"* — **steel mills backlog $3.35bn vs $2.13bn at
end-2024 = +57% y/y** `[measured, SEC XBRL / 10-K text]`. Driver named explicitly: **"growing demand
from data center construction"**, alongside stabilised warehouse construction. **STLD's 10-K**: order
backlog *"maintaining solid levels and extending through the first half of 2026,"* demand *"largely
driven by the commercial, data center, manufacturing, warehouse, and healthcare sectors."*
**Section 232 tariffs** (up to 50% on imported steel) independently confirmed as a live pricing-power
mechanism `[yahoo_finance/barchart 08-02]`.
⇒ **Answer: BOTH — a genuine data-centre / non-residential construction demand pull, protected by an
active tariff regime that blocks import competition. Not a supply-side event; not a pure trade-policy
artifact.**

**Why NUE/STLD stay 🟡중립 — verified mechanically, not repeated.** `module_flow`'s gate
(`_synthesize.py`) needs **green ≥ 3 of 4** axes (OBV 매집 · rs20 > 0 · `vol_surge` ≥ **1.2** ·
velocity ≥ 1.2) plus conviction. **NUE clears 2 of 4** (OBV 매집, rs20 vs SPY +17.5) and fails 2
(`vol_surge` 0.95 < 1.2; velocity `None` → 0). **STLD: identical shape** (OBV 매집, rs20 +12.5;
`vol_surge` 0.90; velocity `None`). ⇒ **raising `vol_surge` alone to ≥1.2 — with velocity still
unmeasured — is sufficient to cross green ≥ 3 for both names.** **The "vol_surge alone blocks it"
claim is VERIFIED TRUE**, for the specific mechanical reason that only one of the two failing axes
needs to flip. **This is a detection-gate constraint on the desk's own instrument, not a fundamental
one** — the backlog, tariff and RS/OBV evidence is unambiguous; the 🟡 tag is a measurement artifact
of a `vol_surge` proxy that two large, low-beta, steadily-traded names structurally under-clear.

### 2.2 · ★★ Fertilizer/chemicals — collapsing on at least THREE different constraints, not one

**5-session excess vs SPY: CF −12.17 · LYB −7.52 · DOW −6.65 · CTVA −5.90 · BALL −5.75 · CE −5.37.**

- **CF — an earnings-quality miss, not a demand problem.** Pre-print coverage (08-04) was bullish
  (*"healthy nitrogen fertilizer demand… higher nitrogen prices"*). The print (after-close **08-05**)
  **missed both revenue and EPS, shares −6.2% in extended trading** `[seekingalpha 08-05]`, after a
  **51% YTD run into it**. Mechanism named in pre-print coverage: **average natural-gas cost
  $4.57/MMBtu vs $3.68 a year ago (+24% y/y)** — the key nitrogen feedstock — compressing margin even
  as volumes and prices both rose `[nasdaq/zacks 08-04]`. **CF's FY2025 gross margin sits at the
  78.9th percentile of its own 19-year history (§2.3)** ⇒ **a priced-for-perfection miss on cost, not
  a demand-side crack.**
- **DOW / LYB — structural overcapacity, compounded by an unrelated trade unwinding.** Dow's **most
  profitable quarter in four years** (net income $802mm, +20% sales) was itself powered by a
  **Hormuz-driven North-American ethane-cost advantage** — Asian/European crackers run naphtha
  (crude-linked, which spiked); US crackers run cheap domestic ethane `[fortune 07-30]`. As Hormuz
  de-escalation optimism entered the tape (**XLE exc5 −6.95pp vs SPY, same 5-session window**), part
  of that feedstock-advantage trade unwinds with it. **Separately and structurally**: both are
  **actively shuttering European capacity** into an unresolved global plastics glut (LYB divested
  "select European assets" this quarter). **Two mechanisms, one direction.**
- **CTVA — segment pricing pressure plus a spin-off overhang**, no feedstock analog: Crop Protection
  segment price **−2% y/y**, attributed to *"competitive market dynamics in Latin America and Asia
  Pacific"* `[nasdaq/zacks 07-29]`, under the company's **planned Q4 2026 separation (Vylor spin)**.

⇒ **Answer: NOT the same constraint. Three mechanisms wearing one "fertilizer/chemicals leg" label.**

### 2.3 · ★★ L2 — peak-margin / low-multiple, name by name

`scripts/margin_history.py` (SEC XBRL). ⚠ **NEM: `[unavailable]`** — the script returns "no annual
data" (its gross-margin tag mapping does not resolve for Newmont's XBRL structure). **Flagged as a
tooling gap, not skipped.**

| Ticker | Fwd P/E | EV/EBITDA | FY2025 gross margin | Percentile in own history | Read |
|---|---|---|---|---|---|
| **NEM** | 10.69 | 6.79 | `[unavailable]` | `[unavailable]` | Cheap on cash-flow proxies, but **the margin side of the pairing cannot be built ⇒ this is not a valuation (L2)** |
| **FCX** | 17.03 | 12.39 | 26.1% | **46.7%** (n=15) | Mid-range margin, elevated-for-FCX multiple — not a trap, not statistically cheap |
| **NUE** | 14.48 | 11.93 | 11.9% | **52.6%** (n=19) | Median margin, mid-teens multiple — the **+57% backlog build (§2.1)** is a forward bet the multiple has started to price and the current margin does not yet show |
| **STLD** | 13.91 | 15.48 | 13.2% | **42.1%** (n=19) | Below-median margin, richest EV/EBITDA of the group — multiple ahead of the current margin print |
| **DOW** | 15.91 | 9.56 | 6.3% | **12.5%** (n=8) — **TROUGH** | A **not-cheap** 15.9× forward multiple on the **lowest gross margin in Dow's own 8-year public history** — pricing a recovery that has not appeared |
| **LYB** | 9.24 | 8.70 | 8.5% | **6.7%** (n=15) — **TROUGH, literally the 15-year minimum** | The multiple **IS** cheap (9.2×) against a trough — the classic countercyclical setup, and a **different object from DOW's more expensive version of the same trough** |
| **CF** | 10.42 | 5.58 | 38.5% | **78.9%** (n=19) — **NEAR-PEAK** | ★★★ **The textbook L2 trap**: a cheap-looking multiple (10.4× fwd, 5.6× EV/EBITDA) on a margin in its own **top quintile**. **The 08-05 miss is the first data point consistent with the mean-reversion risk the multiple does not price** |

---

## §3 · Chain-hop candidates + flow cross-check

⚠⚠ **Tooling anomaly, logged not hidden**: `module_news_data chain-hop` was invoked twice with the
terms `copper grid transformer` — **both runs returned a different, unrelated theme** ("co-packaged
optics switch", then "optical interconnect datacenter" — matching today's separately-promoted DEEP-IT
node) instead of the requested terms, and both took >150s. **The tool did not answer the query asked**
⇒ treated as **non-responsive, not as evidence**, and not cited below. **Registered as a defect.**

Falling back to the flow-JSON cross-check (legitimate, self-computed) for the two named chains:

- **AI → power → transformers → copper (FCX).** FCX is **🟡중립, OBV −0.071** — **not accumulating**.
  This **directly contradicts** a "copper is where the AI-power chain money is" read: the futures
  market is maximally long (100th %ile COT) while the equity's own volume-flow signature is
  flat-to-distributive. **Real in positioning terms, unconfirmed at the single-name equity-flow level.**
- **Texas data-centre build → cement/aggregates (VMC, MLM).** **Both 🔴분산** — VMC (flow −0.599,
  rs20 vs SPY −6.0, OBV −0.149) and MLM (−0.668, rs20 −7.5, OBV −0.187) are **the two worst flow
  scores in the entire 12-name Materials universe**, worse than LIN. ⇒ **the aggregates leg of the
  data-centre-construction chain shows NO flow confirmation whatsoever** — consistent with PREMORTEM
  Lens 4's finding that the AI-power chain's named suppliers (GEV, CAT) are similarly red while the
  registry that should track exposure to it cannot see the chain at all (**D218**). ⇒ **the
  narrative-vs-money gap is not confined to Energy/Utilities — it reproduces inside Materials.**

**No Materials chain-hop candidate reached BET-eligibility this run.**

---

## §4 · Track-KPIs and anti-signals — dated observables

| # | Observable | Reads today | Falsifies / confirms |
|---|---|---|---|
| 1 | **S57 branch A**: XLB 5-session excess vs SPY > +1.9, ANY settled close through **08-12** | **+1.307; ex-NEM +0.194** | **If it fires, check the ex-NEM print (this file's methodology) BEFORE reading it as a Materials call** |
| 2 | **NEM 30d revision breadth turning net-positive**, or **gold giving back the week** | 0↑/9↓ current-qtr; gold +2.4%/wk | Either failing while price holds = the exhaustion case materialising |
| 3 | **Copper COT next Tuesday close (08-11, published 08-14)** | +77,123 net, **100th %ile**, +9,842 wk | A pullback from the yearly max = the first sign the crowded-long leg is capping, not confirming |
| 4 | **NUE / STLD `vol_surge` crossing 1.2** | 0.95 / 0.90 | A mechanical flip to 🟢 on an unchanged fundamental picture — **a detection-lag event, not new information** |
| 5 | **CF Q3 natural-gas cost per MMBtu** | Q2 ref $4.57 vs $3.68 y/y | A further sequential rise on flat/softer urea pricing repeats the margin-miss mechanism |
| 6 | **DOW/LYB vs XLE co-movement through the 08-12 CPI** | XLE exc5 −6.95 vs SPY, same window DOW/LYB lag | Re-coupling as XLE stabilises ⇒ the fading-Hormuz-cost-advantage read is confirmed; decoupling ⇒ overcapacity dominates |
| 7 | **CTVA Crop Protection segment pricing**, next print | −2% y/y, LatAm/APAC | A second consecutive negative print upgrades this from one segment/one region to a leg-wide constraint |
| 8 | ⚠⚠ **X (US Steel) is DELISTED** — confirmed via an empty yfinance response, no OHLC | — | **Anti-signal: any screen, watchlist or peer set still carrying `X` as live is stale and must be corrected on sight** |
| 9 | **VMC / MLM flow score** | −0.599 / −0.668, both 🔴 | A flip to 🟡/🟢 alongside continued Texas data-centre headlines = the first flow confirmation of the aggregates leg |
| 10 | **XLB D6 option-implied move, 08-14 expiry** | **±2.1%** | **Any branch-A fire inside this band should be read as LOW-INFORMATION** until a subsequent session extends beyond it |

**No position sizing and no buy/sell language appears anywhere in this file (P4).**
