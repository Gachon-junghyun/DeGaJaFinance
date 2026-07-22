# L1 · DEEP — sector deep-dive (stage)

> Phase 2. One agent per DEEP sector (parallel fan-out, one message): flow → players → IR →
> value chain → bottleneck/refutation. Calls L2. Output: `SECTOR_DEEP_{code}.md` × N.

## L2 called
- [deepdive](../L2_modules/deepdive.md) — `module_industry_map` (player union + value chain) ·
  `module_business(_us)` (⚠ `--json` on US: default markdown carries KR headers) ·
  `module_disclosure(_us)` · `module_chart --read`.
- [news](../L2_modules/news.md) — (US) `chain-hop` under-named-beneficiary candidates.
- [indicators](../L2_modules/indicators.md) — `module_flow`/`us_flow` flow cross-check
  (short-z ≥+1.5 spike / ≤−1.5 exit divergence vs narrative = the order-flow tell news can't see).

## What this stage does
- **Macro gate**: only OW-designated sectors (plus any pre-mortem-promoted leg). No Neutral/UW padding.
- Per sector: player extraction (**large-cap universe ∪ thematic small-caps**, bounded: named ≥2×
  in the sector's news window AND a real ticker AND mcap ≥ ~$2B — this union is where alpha leaks) →
  IR anchor (who does what, from primary filings) → value-chain node map 5–8 nodes left→right
  (bottleneck = *binding constraint*, strong demand ≠ bottleneck; mark cross-sector chains,
  e.g. AI→power→transformers→copper) → chain-hop candidates (body-proximate only, never
  headline-named; a news co-mention alone is NOT a candidate — flow cross-check before it may
  reach BET) → track-KPIs + anti-signals (what kills the thesis, stated as observables).
- **Continuous-track vs rotating** (from ROTATION's picks):
  a continuous sector was deep-dived very recently → **lead with the DELTA** (new print/contract/
  guide, thesis confirm-or-crack, kill-switch proximity) and carry unchanged structure by reference
  to the prior file. A rotating sector gets a full fresh map. Daily tracking compounds signal;
  it does not re-print the same map.
- Fan out all sector agents **in one message** (parallel) — wall-clock stays near a single deep.

### Carry rules from `handoff/RESEARCH.md` (loaded by HANDOVER; binding here)
- ⚠ **Price-cycle sectors are read on the second derivative, not the level** (lens B1). For memory,
  steel, shipping, refining, chemicals — any commodity node — tabulate the **QoQ change series**.
  Level and rate routinely point opposite ways, which produces the apparent paradox "shortage
  persists but the equity struggles". Measured: server DRAM contract prices ran
  **+90~95% → +58~63% → +13~18% QoQ** across three quarters while physical supply stayed short into
  2027. Two consecutive declines in the *rate* is the signal; the level is the distraction.
- ⚠ **Peak-margin / low-multiple trap** (lens B2). A cyclical at its earnings peak prints its
  *lowest* forward multiple because the denominator is peaking. Measured: Micron forward P/E
  **6.31×** at gross margin **84.6%**, against a prior-cycle peak of 59% and an FY2023 margin of
  **−9.1%**. **Put the forward multiple next to where margin sits in its own history** before calling
  anything cheap — a multiple without a margin percentile is not a valuation.
  ★ **And read the estimate-momentum table with it** (`module_fundamentals_us` §추정치 모멘텀,
  added 2026-07-22). It shows where the denominator has been *going*: MU's +1y EPS ran
  **100.53 → 150.91 in 90 days (+50.1%)** on **30 upgrades : 0 downgrades**. A low multiple whose
  estimates are being revised up that steeply is consensus **chasing**, not cheapness. Revisions turn
  before price does — a first downgrade in a 30:0 name is a bigger event than the multiple.
- ⚠ **Name the node's customers and check their disclosed spend** (rule A6). A supply-chain verdict
  written without looking at the buyers' capex is missing the demand side of its own thesis. If their
  prints are pending, say so **with the date** rather than concluding around them.
- ⚠ **An inherited lead/lag claim is tested or tagged `[unverified]`** (rule A5). Measured: an
  uncited "EDA leads semis by 12–18 months" was carried between reports and repeated as fact; 199
  monthly observations (2010–2026) gave same-month **+0.63** vs lag-12 **+0.05** — coincident, not
  leading. Lead-lag is one correlation table to test and expensive to get wrong; it is the claim
  class most likely to be repeated on authority alone.
- ⚠ **State the dispersion inside the sector** (lens B5). Measured 2026-07-21: memory/storage
  +12~14% while GPU/ASIC managed +2.0~2.2% — a ~10pp spread inside "semiconductors" in one session.
  If the spread between sub-nodes exceeds the sector's own move, the sector label is the wrong unit
  of analysis and the file must say so.

## ✅ EXIT CHECK
- [ ] One `SECTOR_DEEP_{code}.md` per selected sector (incl. any promoted 5th), written via parallel agents.
- [ ] Each covers flow → players(∪ thematic) → IR → chain map(+chain-hop) → bottleneck/KPI/anti-signal.
- [ ] Continuous-track files LED with the delta; rotating files are full fresh.
- [ ] Any ROTATION-flagged matrix×flow divergence has an explicit resolution verdict in its sector file.
- [ ] **Commodity/price-cycle nodes carry a QoQ rate-of-change series, not just levels.**
- [ ] **Every "cheap on forward multiple" claim states where margin sits in that name's own history.**
- [ ] **The node's customers are named and their disclosed spend checked** (or their print dates given).
- [ ] **Every lead/lag claim is either measured this run or tagged `[unverified]`** — none inherited as fact.
- [ ] Sub-sector dispersion stated; if it exceeds the sector move, the file says the sector label is the wrong unit.
