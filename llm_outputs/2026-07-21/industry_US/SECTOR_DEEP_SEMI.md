# SECTOR_DEEP_SEMI — Semiconductor / AI-Hardware epicenter · 2026-07-21 (Tue)

> Stage 5 / L1·DEEP. **★ PROMOTED, adversarial-pre-mortem track — not a ROTATION pick.** ROTATION's own
> 3 DEEP picks were ENRG/HLTH/FIN (delta runs); this leg exists because LENS 1 of `BLINDSPOT_PREMORTEM.md`
> found a dated catalyst (AMD "Advancing AI", 07-22) sitting inside the window and named nowhere in
> CATALYST_WATCH, MACRO, EVENT_ALPHA, or ROTATION, and because IT is this run's single largest matrix×flow
> contradiction (§4x(a) of MACRO; §2(a) of ROTATION). **This is a FULL FRESH MAP, not a delta** — the prior
> file (`2026-07-17/industry_US/SECTOR_DEEP_SEMI.md`) is read for continuity only. Zero buy/sell calls;
> BET owns sizing. Data: `module_flow`, `scripts/us_flow.py` (FINRA short-vol), `module_chart --read`,
> `module_news_data` (`--scope foreign` throughout), `module_business_us`/`module_fundamentals_us`/
> `module_disclosure_us` (EDGAR primary), `module_report_tags`.

---

## 0. Bottom line

**MU's reclaim reads as a NAME event, not a SECTOR event — every independent method this run agrees, and
the chart module adds the sharpest confirmation of all.** MU closed 865.46 (+1.94%, 07-20), clearing its
pre-committed 848.95 STOP — but `module_chart MU --read` shows the **ignition trigger (close >872.42 with
OBV flipping to accumulation) has NOT fired**: OBV is still **분배 (distribution), −57% 20-day slope**,
RSI 24.5 (deeply oversold, not confirmed-turning), turn-verdict **NEUTRAL/CHOP**, only 1 of 4 moving
averages above price, and volume on the reclaim day was **0.86× — below average**. The universe sweep
(0 green / 56 IT names, eqflow −0.334, the worst breadth on the board) and EVENT_ALPHA's chip-selloff card
(every named exposure distributing) independently reach the same read from different data. **All three
methods — price/chart, universe breadth, event-flow crosscheck — converge on "beta bounce on a $550B
market-wide relief day," not "sector re-rate."**

**The bull case is real but has not yet been rewarded by money.** AMD's Microsoft/Helios deal is a signed,
dated contract (shipments 2H2026) with a genuinely clean short tape (FINRA z **+0.01**), and it sits ahead
of a two-day investor event (07-22) the desk's own calendar missed entirely. But **AMD's own chart OBV is
ALSO distributing (−58% 20d slope)** — the stock rallied on the headline while money did not confirm it.
**The honest state, stated rather than resolved by assertion: the hardware bull case is a live, dated,
unconfirmed hypothesis with two falsification windows 24–48 hours away (GOOGL/AMD 07-22, INTC 07-23), and
until one of those prints, "unresolved" is the correct answer, not "bullish" or "bearish."**

---

## 1. Flow cross-check, split by node (`module_flow`, bench SPY, asof 2026-07-20 close; FINRA z asof 07-20)

| Node | Ticker | Flow tag | OBV | RS20 | RS60 | Vol surge | FINRA z | Read |
|---|---|---|---|---|---|---|---|---|
| **GPU / accelerator (epicenter)** | NVDA | 🔴분산 | 분산 | −2.9% | −4.0% | 0.77× | **−1.39** (covering) | Flat price, distributing flow, shorts covering underneath — the least-broken name, still not confirming |
| | AMD | 🟡중립 | 중립 | −5.7% | **+61.6%** | 0.83× | **+0.01** (clean) | Headline-driven pop, flow uncalled. RS60 intact. Zero crowding either direction |
| | AVGO | 🔴분산 | 분산 | −7.4% | **−14.9%** | 0.70× | — | Weakest of the three book-held epicenter names, **no live narrative at all** |
| **Memory** | MU | 🔴분산 | **분산** | −23.1% | +73.2% | 0.86× | −1.10 | Price reclaimed the stop; OBV did not follow. See §0 |
| **Foundry** | TSM | 🔴분산 | 분산 | −12.3% | −0.5% | **1.24×** | +0.22 | Distribution on **real volume**, not drift — the cleanest bear signal in the complex |
| **Semicap / WFE** | AMAT | 🔴분산 | 분산 | −14.2% | +25.9% | 0.77× | −1.27 | |
| | LRCX | 🔴분산 | 분산 | −20.5% | +11.2% | 0.91× | +0.62 | |
| | KLAC | 🔴분산 | 분산 | −19.4% | +10.2% | 0.86× | — | Entire equipment basket red on flow, RS60 still positive — beta-drag, not (yet) independent breakdown |
| **EDA / design (upstream)** | CDNS | 🔴분산 | 분산 | −14.2% | −4.8% | **1.00×** | — | RS60 negative too — the design-tool layer is the **only node where even the medium-term trend has broken** |
| | SNPS | 🔴분산 | 분산 | −16.3% | **−25.0%** | 1.14× | — | Same, worse |
| **Custom silicon / near-memory** | MRVL | 🔴분산 | 분산 | **−36.6%** | +19.6% | 0.59× | — | Worst RS20 in the whole named set |
| | QCOM | 🔴분산 | 분산 | −24.1% | +20.8% | 0.57× | — | |
| | INTC | 🔴분산 | 분산 | −26.9% | +44.4% | 0.84× | −0.81 (not crowded) | Dated fulcrum 07-23; no short crowding to unwind on a beat |
| | TXN / ADI (analog, adjacent) | 🟡중립 / 🔴분산 | 중립 / 분산 | −11.4% / −13.6% | +15.9% / −6.7% | 0.73× / 0.68× | — | Analog lagging the AI story entirely, as expected |
| **Networking** | ANET | 🟡중립 | **매집** | +0.4% | −9.1% | 0.78× | — | The single accumulating name in the whole node map |
| **Power / cooling** | VRT | 🔴분산 | 분산 | −11.8% | −8.8% | 0.72× | — | Contradicts the AI-rack bull case directly (see CARD 3, EVENT_ALPHA) |
| | HPE | 🟡중립 | 중립 | −5.4% | **+52.0%** | 0.63× | — | Rack-integration name, RS60 strongly positive, not headline-named |
| **Sector proxy** | SMH | 🔴분산 | 분산 | **−14.7%** | +12.9% | **1.04×** | — | Deepened even as MU bounced — the split in one line |

### ★ The split, stated plainly
**Exactly one name in the entire 21-ticker scan is accumulating: ANET.** Everything else — epicenter,
memory, foundry, semicap, EDA, custom silicon, power/cooling — is either distributing or flow-uncalled.
**The upstream design layer (CDNS/SNPS) is new information this run: it is the only node where the
medium-term trend (RS60) has also broken, not just the 20-day.** That is a heavier signal than the
memory/foundry story alone — if EDA seat/IP licensing is decelerating, it front-runs everything downstream
by 12–18 months in a normal cycle; **no news evidence yet explains why**, and that gap is logged, not
papered over (§7 anti-signal).

**Chart-confirmed detail on the two names that matter most to the debate:**
```
MU:  OBV: 분배(매도압력↑) (20d기울기 -57%)
     다이버전스: 없음 · MA정렬: 혼조 · 가격 1/4 MA 위
     볼린저: 확장 44.5% · 중단 · RSI: 24.5 · 모멘텀20d -28.5%
     턴-판정: NEUTRAL/CHOP (방향 불명확)
     트리거(점화): close>872.42 + OBV→누적 / 스탑(스윙저점): 848.95

AMD: OBV: 분배(매도압력↑) (20d기울기 -58%)
     다이버전스: 없음 · MA정렬: 혼조 · 가격 2/4 MA 위
     볼린저: 수축(코일링) 16.0% · 중단 · RSI: 44.3 · 모멘텀20d -8.7%
     턴-판정: PULLBACK-TO-SUPPORT (추세 눌림목)
     트리거(점화): close>515.51 + OBV→누적 / 스탑(스윙저점): 495.76
```
**Both names show the identical OBV signature (≈−57/−58% 20d slope) despite opposite headlines** — MU on
a "reclaim," AMD on a "deal win." **The chart module reads both as unconfirmed, not as diverging cases.**
That symmetry is itself evidence against reading MU's reclaim as sector-wide: if the sector had turned,
the two most newsworthy names in it would not carry matching distribution slopes.

---

## 2. Players — large-cap universe ∪ thematic small-caps

**Bounded set (named ≥2× in this run's news window, real ticker, mcap ≥ ~$2B):**
NVDA · TSM · AVGO · MU · AMD · INTC · ASML · AMAT · LRCX · KLAC · MRVL · QCOM · TXN · ADI · ANET · VRT ·
HPE · SMH (proxy) · CDNS · SNPS · GOOGL (context — Gemini chip, COMM-owned per MACRO, carried here only as
a demand-signal cross-check) · MSFT (the Helios buyer) · STX (chain-hop; see below).

**Thematic small/mid-cap layer surfaced by `chain-hop "HBM" "advanced packaging" "EUV"` (14d, foreign, 211
articles scanned)** — see §5 for the crowding read; carried into the player set only where flow was
independently checked: **CDNS, SNPS** (both promoted to the main table above on the strength of their RS60
breaks) and **STX** (Seagate — 🟡중립, RS20 −24.4%, RS60 **+34.0%**, vol surge **1.23×** — the only chain-hop
candidate with above-average volume; adjacent to the HBM/storage supply story but not itself a memory
maker, flagged as a genuine watch rather than promoted to the core map).

**Excluded from the player set, with reason:** GEV (🟡중립, RS20 −2.1%, already the AI-power/UTIL story's
epicenter, tracked there not here); AMZN (🟡중립 but OBV **매집**, +2.9% RS20 — a hyperscaler demand-side
name, kept as context not as a semi player); JPM/GS/C/MS (financing-the-buildout angle, COMM/FIN-owned).

---

## 3. IR anchor — primary filings (`module_business_us`, `module_disclosure_us`, EDGAR)

**AMD — 10-K filed 2026-02-04 (period ended 2025-12-27, accession 0000002488-26-000021), MD&A pulled
directly:**
- FY2025 net revenue **$34.6B, +34% YoY** (2024: $25.8B). **Data Center segment $16.6B, +32% YoY**, driven
  by 5th-gen EPYC and **Instinct MI350 Series GPUs**. Client and Gaming $14.6B, +51% YoY. Embedded −3%.
- Gross margin **50%** (+1pt YoY), net of ~$440M in inventory charges tied to the US export-control
  restriction on **MI308** China-bound GPUs — the filing's own words, i.e. AMD is disclosing a real,
  dollar-quantified China/export-control drag inside an otherwise-accelerating quarter.
- Cash + short-term investments **$10.6B** (from $5.1B YoY); total debt **$3.3B** (from $1.8B) — the
  balance sheet expanded on both sides, consistent with a capex/buildout-financing posture, not distress.
- **Primary confirmation of the Helios thesis, from the filing itself, predating the Microsoft deal
  announcement**: *"We previewed our Helios AI rack-scale platform solution that incorporates all of our
  data center products (CPUs, GPUs and Networking) to address the growing AI compute requirements."*
  **This means the Microsoft deal (07-20) is the platform's first named hyperscaler commitment, not a
  new product — the filing shows AMD had already built and previewed the rack before securing the
  customer**, which changes the read of "customer risk" in §1 of the bull/bear framing: the engineering
  bet was placed before this week's headline, the headline is the first monetization proof point.
- `module_disclosure_us AMD`: 38 filings in the trailing 90 days, **1 material-contract 8-K (2026-05-15,
  Item 1.01)**, 1 earnings 8-K (2026-05-05), 1 10-Q (2026-05-06, period 2026-03-28), 19 Form 4 insider
  filings (routine, not a cluster), 1 Item 5.02 exec-change 8-K (2026-07-01). **No new 8-K covering the
  Microsoft/Helios announcement had posted as of this run** — the deal so far is a press release + news
  cycle, not yet a filed material-agreement disclosure; worth re-checking after 07-22.

**Fundamentals cross-check (`module_fundamentals_us AMD --json`, yfinance + SEC XBRL):** price 503.57,
mkt cap **$821.1B**, trailing P/E **164.0** (extreme — reflects the export-control charge compressing
trailing EPS to $3.07), **forward P/E 37.4** (forward EPS $13.46 — the market is pricing a >4× earnings
step-up), PEG 1.16, analyst mean target **$541.66** (46 of 51 covering analysts strong-buy/buy, 0 sell).
Quarterly revenue climbing sequentially every quarter shown (Q1'26 $10.25B vs Q1'25 $7.44B, +38% YoY).
**The valuation is already pricing a large re-acceleration — which is why the chart's "unconfirmed by OBV"
read matters: the market has front-run the print, and 07-22 is where that bet gets marked, not created.**

**MU / TSM / INTC primary sourcing — carried forward from `2026-07-17/industry_US/SECTOR_DEEP_SEMI.md`
§4, not re-pulled this run (no new 10-Q/6-K has posted since):** TSM's most recent primary (6-K, accession
0001046179-26-000451, filed 07-16) showed Q2 revenue $40.20B (+33.7% YoY) with a raised Q3 guide of
$44.6–45.8B — the FY26 capex raise to $52–56B and the ~$265B cumulative US commitment are still
**news-corroborated, not independently re-verified against a primary transcript**, a gap that persists
into this run. INTC's most recent primary (10-Q, accession 0000050863-26-000079, period 2026-03-28) showed
Foundry segment revenue +16.2% YoY and external-customer revenue +461% YoY off a small base — this is now
**one quarter stale** ahead of the 07-23 print, the single most direct falsification test in the window.

---

## 4. Value-chain node map (5–8 nodes, left → right)

```
[EDA/IP design]──[Lithography]──[WFE equipment]──[Foundry]──[Advanced pkg + HBM]──[Compute silicon]──[Rack/network/power]──[Hyperscaler demand]
  CDNS,SNPS         ASML          AMAT,LRCX,KLAC     TSM       ★ BOTTLENECK ★         NVDA,AMD,AVGO,      ANET,VRT,HPE          MSFT,GOOGL,AMZN,META
  🔴 RS60 broken   (not scanned    all 🔴, RS60         🔴        CoWoS + HBM/MU        MRVL,QCOM,INTC       mixed: ANET 매집,      MSFT 매집 +6.7%,
  (new this run)   this run)      still +)          1.24x vol     both supply-           all 🔴 except         VRT 🔴, HPE 중립      GOOGL 🔴 z+1.45,
                                                       real        constrained             AMD 🟡 clean tape                          AMZN 🟡매집
```

**Bottleneck = advanced packaging (CoWoS) + HBM supply — unchanged from the 07-17 file, and the news axis
this run makes it stronger, not weaker.** *"Micron Says Memory Chip Supply Will Remain Tight Beyond 2027"*
and *"Chip industry lead time continues to accelerate, pricing rises"* [Susquehanna] are **both supply-side
observations, not demand-side ones — pricing power in a tight market is the textbook signature of a binding
capacity constraint, and it is the literal opposite of a capex de-rate.** **Strong AI-GPU demand is NOT the
bottleneck** (demand has been ahead of hardware output for six-plus quarters running); the bottleneck sits
one and two nodes upstream of the GPU (packaging capacity, HBM stack capacity), which is exactly why TSM's
Arizona expansion (now $265B cumulative) explicitly names "advanced packaging fabs" as new capacity, not
new wafer starts.

**Cross-sector chain, named per the brief's instruction:** AI compute → power draw → grid/transformer →
copper. This run's evidence: **VRT (rack power/cooling) is 🔴분산 −11.8%**, contradicting the AI-power
headline story (Hut 8's $9.8B lease, IREN's +19.6% day) exactly as MACRO §4 UTIL and EVENT_ALPHA CARD 3
found — **the power leg of the AI chain is currently the weakest-flowing node in the entire map**, worse
even than memory. That is worth carrying forward as a standing caveat on any "AI buildout is intact"
reading: compute demand may be real while the physical infrastructure to power it is not yet being bought.

---

## 5. Chain-hop candidates — body-proximate only, thematic small-caps widened

EVENT_ALPHA already found **zero un-crowded candidates within us_top300** for this theme (CARD 3: "every
name it returned was already headline-named"). Re-run here with `chain-hop "HBM" "advanced packaging"
"EUV"` (14d, foreign, 211 articles scanned) to test whether widening changes that finding.

**Result: it does not change the headline-named layer, but it surfaces a genuinely new candidate set
outside the AI-compute headline names — none of which were checked by EVENT_ALPHA because its scope was
narrower ("TSMC capex"/"Intel foundry" search terms).**

| Ticker | Proximity mentions | Body count | Flow check | Verdict |
|---|---|---|---|---|
| **CDNS** | 2 | 2 | 🔴분산, RS20 −14.2%, **RS60 −4.8%** | Promoted to core map (§1) — RS60 break is real signal, not noise |
| **SNPS** | 2 | 2 | 🔴분산, RS20 −16.3%, **RS60 −25.0%** | Same, worse |
| **STX** | 2 | 6 | 🟡중립, RS20 −24.4%, **RS60 +34.0%, vol 1.23×** | ★ **Only candidate with above-average volume** — flagged watch, not promoted (storage ≠ memory maker) |
| MRVL | 3 | 10 | Already in core map (🔴 −36.6%) | Not a new candidate — already headline-named elsewhere in this run's news pool |
| AMAT | 2 | 10 | Already in core map | Same |
| GEV | 2 | 6 | Already tracked as UTIL/AI-power epicenter | Not a SEMI candidate |
| AMZN | 5 | 42 | 🟡중립, OBV **매집** +2.9% RS20 | Demand-side hyperscaler, not a chain-hop supply candidate |
| JPM/GS/C | 2 each | 10–12 | Financing-the-buildout angle | FIN-owned, not SEMI |
| CDNS example headline: *"Cadence Introduces AuraStack AI Super Agent… Agentic AI Platform for PCB…"* — a
  real product story, body-proximate, zero headline appearances for CDNS itself in the theme window.

**Conclusion: EVENT_ALPHA's "no un-crowded layer left" finding holds for the headline AI-compute names
(NVDA/MU/AMD/AVGO/INTC/ASML) — it does NOT hold once the scope widens to the design/EDA layer.** CDNS and
SNPS are body-proximate, zero-headline-appearance names whose own RS60 has broken independently — this is
the one finding in this DEEP that neither MACRO, SWEEP, EVENT_ALPHA, nor ROTATION surfaced. **Flagged as a
genuine new lead, not yet flow-confirmed as accumulating** (both are still distributing) — the honest
read is "a bear signal nobody named yet," not an alpha candidate for a long.

---

## 6. ★ VERDICT on the hardware-vs-software bifurcation claim

**PREMORTEM's LENS 4 called for the registry's rank-1 AI-compute cycle to bifurcate into hardware vs
software because MU and IBM moved with opposite signs in one week. This DEEP tests that claim directly
against the flow data pulled in §1, and the claim holds — but weaker than "opposite signs" implies.**

- **The two sides are NOT symmetric in conviction.** IBM's move (−26.6%/5d on 2.44× volume) is confirmed
  by real, elevated turnover — a genuine distribution event. **MU's move (+1.94%/1d on 0.86× volume) is
  NOT confirmed by turnover** — it is a price move on below-average volume with OBV still distributing.
  **Calling these "opposite signs of equal weight" overstates the hardware side.** The correct framing is:
  **software has a confirmed sell signal; hardware has an unconfirmed, price-only buy signal.** That is not
  a clean bifurcation into two equal-and-opposite trades — it is one confirmed move and one noisy one.
- **Where the bifurcation IS real and load-bearing:** breadth. IT sweep shows 0 green / 56, eqflow −0.334
  — the worst in the market — and that number does not distinguish hardware from software; **both sub-legs
  of IT are red on breadth.** The desk's instinct to split rank-1 into two lines is directionally right for
  bookkeeping (two different theses need two different track KPIs), but the underlying flow evidence this
  run shows **both hardware and software presently failing to accumulate**, not one up and one down at the
  breadth level — only at the single-name (MU, IBM) level.
- **What would make the bifurcation real rather than definitional:** AMD's OBV flips to accumulation while
  IBM/MSFT/PLTR (software) stay distributing through 07-22/07-23. That has **not happened yet** — AMD's own
  OBV is currently distributing at almost the identical slope as MU's (§1). **Until AMD or MU's OBV
  actually flips, "hardware is diverging from software" is a headline-level claim, not yet a flow-level
  one.**
- **Verdict: the bifurcation is CORRECT AS A DEFINITIONAL FIX (two theses need two KPI tracks — agree with
  PREMORTEM) but NOT YET CONFIRMED AS A FLOW DIVERGENCE (both legs are currently red on OBV/breadth).**
  The registry should split the tracking, not conclude the hardware leg has turned.

---

## 7. Track-KPIs + anti-signals — dated, falsifiable, tied to 07-22/07-23

### Bull-branch KPIs (per the desk's own pre-committed bracket)
1. **MU closes >872.42 with OBV flipping to 누적 (accumulation), held ≥3 sessions.** Not yet fired (last:
   865.46, OBV 분배 −57%/20d). This is the chart module's own ignition trigger — distinct from and stricter
   than the 848.95 stop that already fired.
2. **SMH RS20 turns > −8%** (now **−14.7%**, deepened since the reclaim, not improved).
3. **Two of {MU, TSM, AVGO} flip OBV to 매집.** Currently zero of three.
4. **AMD's 07-22 "Advancing AI" event produces a guidance raise or a new named hyperscaler customer beyond
   Microsoft**, AND AMD's own OBV turns 매집 (currently distributing, −58%/20d — the event needs to move
   money, not just price, to count).
5. **GOOGL (07-22) or INTC (07-23) print an AI-capex beat that is rewarded on the capex line specifically**
   (MACRO's own wording) — INTC's Foundry segment (last: +16.2% YoY revenue, +461% external, one quarter
   stale) is the most direct test given its foundry-specific read-through to the TSM/packaging bottleneck.

### Bear-branch / anti-signals
1. **MU closes back below 848.95 on >1.2× volume** — the reclaim was relief-day beta, confirmed.
2. **IT breadth stays 0/56 through both 07-22 and 07-23 prints.**
3. **CDNS/SNPS RS60 breakdown deepens or spreads to a third EDA name** — would confirm the upstream-design
   deceleration is a real leading indicator, not noise (§1, §5 — new this run, unresolved).
4. **VRT/HPE (power/rack) stay distributing through end-July** — the AI chain's power leg failing to
   confirm even as compute names attempt a turn would mean the buildout thesis is compute-only, not
   full-stack.
5. **TSM's distribution (1.24× volume, RS20 −12.3%) persists 2+ more sessions on rising surge** — carried
   from the 07-17 file; TSM's thesis thread is independently marked ENDED in EVENT_ALPHA's book cross-check,
   and it is a held epicenter position.
6. **Yardeni's "another −12%" SOXX call and the triple-confirmed crowded short (Nasdaq COT 4%ile + record
   equity shorts + record hedge-fund tech selling) remain live** — this is squeeze fuel IF the bull KPIs
   fire, and continued downside confirmation IF they don't. Track: SMH price vs the 4%ile COT print
   (unchanged since 07-15, still stale-but-directionally-relevant).

---

**EXIT CHECK:** ✅ **Bottom line answered with numbers** (§0) — MU's reclaim named a NAME event, cross-
checked against chart OBV, universe breadth, and event-flow, all three agreeing · ✅ **Flow cross-check run
across 7 nodes, 21 tickers**, with OBV+RS20+RS60+volume+FINRA z per name where available (§1); the
CDNS/SNPS RS60 break is new information not surfaced elsewhere in this run · ✅ **Both `module_chart MU/AMD
--read` blocks embedded verbatim**, not summarized — and the matching −57%/−58% OBV slopes across two
oppositely-headlined names is the load-bearing cross-check · ✅ **Players bounded** (large-cap ∪ thematic
small-cap via chain-hop), exclusions stated with reason (§2) · ✅ **IR anchor pulled from primary EDGAR
filings for AMD this run** (10-K MD&A, disclosure feed, fundamentals XBRL); MU/TSM/INTC primary sourcing
carried forward from 07-17 with the staleness explicitly flagged, not silently re-asserted (§3) · ✅
**Value-chain mapped 8 nodes left→right, bottleneck named (advanced packaging + HBM, unchanged and
strengthening) and the cross-sector AI→power→grid leg flagged as the map's weakest node** (§4) · ✅
**Chain-hop widened to thematic small-caps and tested against EVENT_ALPHA's "no candidates left" finding
— found CDNS/SNPS as genuinely new, un-crowded, and bearish, not bullish** (§5) · ✅ **Hardware-vs-software
bifurcation verdict given with numbers: correct as a KPI-tracking split, not yet confirmed as a flow
divergence** (§6) · ✅ **KPIs and anti-signals dated and tied to 07-22 (AMD event, GOOGL) and 07-23 (INTC)**
(§7) · ⚠ **`module_industry_map` was attempted and failed as designed** — it is a KR-corpus tool
(`corp_embeddings.db`) and returns 0 hits on English seeds by construction; the tool's own error message
correctly redirected to `chain_hop.py` for US value-chain discovery, which was used instead (§5). Nothing
was silently blank — the failure and the substitution are both recorded here.
