# SECTOR_DEEP_45 — Information Technology — 2026-07-21

> Scope: GICS 45 (Information Technology). Deep-dive for the US sector-rotation desk.
> Data asof: module pulls 2026-07-21 (yfinance/SEC), news via WebSearch (cited). Zero buy/sell recommendations — this file produces deterministic data + a divergence resolution rule only. Judgement calls (size, timing) are the desk's.

---

## 1. Flow read — the divergence, stated up front

Information Technology is the **#2 MATRIX×FLOW divergence** on the board and it carries the **CYCLE-#1 CORE discipline**. Three readings point in three directions at once:

- **MACRO matrix = tactical OW-/N.** Tech is under-owned and earnings-strong, but rising real yields are a valuation ceiling. Net: constructive, capped.
- **FLOW (SECTOR_FLOW) = one of the WORST on the board.** wflow **−0.215**, eqflow **−0.375**, **33 RED NAMES** — the worst breadth of any sector. On the tape, money is *leaving*.
- **COT = CROWDED-SHORT.** Nasdaq-100 leveraged/fast money at the **4th percentile**. Hedge funds "walked out of the Nasdaq" — from comfortably long in mid-June to nearly flat three weeks later, one of their smallest positions in three years, while pensions/insurers bought the −4% dip ([SmartFlow COT 2026-07-14](https://smartflow.trading/cftc-cot-report-analysis-july-14-2026/), [RogueQuant](https://roguequant.substack.com/p/the-market-doesnt-take-vacations)). Fast money under-owned = the pain trade is **UP** (squeeze risk).

The tape (worst breadth) and the positioning (4%ile crowded-short) are **the same fact seen from two sides**: everyone who was going to sell semis has largely sold. Hedge funds sold US semiconductors for four straight weeks into early July ([Bloomberg via cryptobriefing](https://cryptobriefing.com/tech-trade-2026-chip-stocks-software-decline/)). Red breadth is what a completed de-risking *looks like*.

**Split the sector — this is essential:**
- **SEMIS / AI-compute (the epicenter, CYCLE #1)** — corrected hard. PHLX SOX fell 10% on June 5 (worst day since March 2020), $1.3T wiped, triggered by Broadcom's Q3 AI-rev guide ($16B vs ~$17.2B expected) ([intellectia](https://intellectia.ai/blog/semiconductor-stocks-selloff-june-2026)). NVDA −12% on the month and sits ~26% below its 52-wk high. This is a **factor/positioning unwind on an accelerating demand base**, not a demand break (§3 confirms capex is *rising*).
- **SOFTWARE (not the epicenter)** — the *opposite* setup. Laggard on price (MSFT −18% YTD, NOW −28% YTD) but staging a relative-strength rally as investors broaden AI exposure from picks-and-shovels to monetization ([SeekingAlpha/XSW](https://seekingalpha.com/article/4920379-timing-the-next-market-rotation-semis-software-and-the-hyperscalers), [Benzinga](https://www.benzinga.com/etfs/sector-etfs/26/06/60139041/software-etfs-are-finally-catching-an-ai-tailwind)). Software's problem is a valuation discount without a near-term catalyst; semis' problem is a great business with a red tape.

The divergence to resolve (§8): **is the semis red tape early re-entry into CYCLE #1, or a falling knife?**

---

## 2. Players (bounded)

**Semis / AI-compute epicenter (CYCLE registry #1, min_epicenter 12%, core NVDA):**
NVDA, AVGO, AMD, MU, TSM, ASML, AMAT, LRCX, KLAC, MRVL, ANET, SMH (ETF proxy).

**Software (adjacent, NOT epicenter):**
MSFT, CRM, ORCL, NOW, PLTR.

**Hardware / systems:** DELL, SMCI, AAPL (systems demand, not core).

**Cross-sector chain (AI-power, §4 node 7):** VRT, ETN, GEV, CEG (Utilities/Industrials — flagged, not in-sector).

**Comm Services AI-adjacent catalyst (folded in, §3/§7):** GOOGL reports 7/22 after close.

---

## 3. IR anchor — AI-capex demand signal per layer (who is accelerating vs decelerating)

The demand base under the epicenter is **accelerating, not decelerating** — this is the load-bearing fact for the verdict.

**Hyperscaler capex 2026 (the demand):** The big four guide to **~$725B combined for 2026, up ~77% from 2025's ~$410B** ([valueaddvc](https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once), [CNBC](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html)):
- **Amazon** ~$200B — accelerating
- **Alphabet** ~$175–185B — accelerating (7/22 print is the near-term read; §7)
- **Microsoft** ~$120–145B (FY26 run-rate) — accelerating
- **Meta** ~$125–145B — accelerating (raised full-year)

**Read:** the $725B → the-Street's "~$1T next year" trajectory means the buyers of NVDA/AVGO silicon are **guiding spend UP**. The semis drawdown (§1) happened *while* the demand guide rose — the classic signature of a **positioning/factor unwind, not a demand break**. The one wobble was AVGO's Q3 AI-rev guide ($16B vs ~$17.2B), a single-quarter guide miss that detonated crowded positioning, not an order cancellation.

**Decelerating layer:** none on the compute side. The friction is *supply* (§4 bottleneck) and *valuation/rates*, not order flow.

---

## 4. Value-chain map (7 nodes) — bottleneck = binding constraint

| # | Node | Key names | Role | State |
|---|------|-----------|------|-------|
| 1 | EDA / IP | (CDNS, SNPS, ARM — adjacent) | Design tools, cores | Steady, toll-taker |
| 2 | Foundry | **TSM** | Fabs the leading-edge dies | Sold out leading-edge into 2026–27 |
| 3 | Equipment | **ASML, AMAT, LRCX, KLAC** | Litho / depo / etch / metrology | Capex-levered to foundry expansion |
| 4 | **Advanced packaging (BOTTLENECK)** | **TSM (CoWoS)**, HBM: MU / SK Hynix / Samsung | Interposer + HBM stack | **Oversubscribed through 2026, structural** |
| 5 | Compute / GPU + accelerators | **NVDA, AMD, AVGO (custom ASIC), MRVL** | The silicon | Corrected on tape, demand rising |
| 6 | Networking / interconnect | **AVGO, ANET, MRVL** | Rack/cluster fabric (scale-up/out) | AVGO custom silicon at ATH intra-correction |
| 7 | Hyperscaler / systems → **AI-power (cross-sector)** | MSFT/GOOGL/AMZN/META; DELL/SMCI; **VRT/ETN/GEV/CEG** | Buyers + power/cooling | Power = the *next* binding constraint |

**BINDING CONSTRAINT = advanced packaging + HBM (node 4), migrating to power (node 7).**
- **CoWoS packaging** is "the single tightest part of the AI semiconductor stack" — TSMC/NVIDIA/OSATs report it oversubscribed through at least 2026. HBM is *inseparable* from CoWoS (the stack sits on the interposer next to the GPU die).
- **HBM is sold out for 2026** across SK Hynix / Samsung / Micron; MU is ramping HBM4 to volume in 2026; Samsung repricing contracts up high-teens % ([fusionww](https://info.fusionww.com/blog/inside-the-ai-bottleneck-cowos-hbm-and-2-3nm-capacity-constraints-through-2027), [enkiai HBM](https://enkiai.com/ai-market-intelligence/ai-supply-chain-crisis-2026-the-new-hbm-bottleneck/)).
- CEOs of TSMC/SK Hynix/Micron/Intel/NVIDIA/Samsung all delivered the same message: demand for advanced nodes/packaging/HBM is rising **faster than capacity can be built** — a structural limit shaping pricing and lead times into 2027.
- **Downstream, the bottleneck shifts to power** (node 7): grid interconnect queues run 4–7 years in NoVA/Phoenix/Dallas; ~43 GW planned across 84 tracked US AI facilities ([spheron power](https://www.spheron.network/blog/ai-data-center-power-constraints-2026/), [siliconreport](https://siliconreport.com/ai-datacenter-power-crunch-electricity-bottleneck-31b33b49)).

A sold-out bottleneck is a *bull* fact for the constrained node's pricing power (MU HBM, TSM CoWoS) — it is the opposite of a demand-break narrative.

---

## 5. Chain-hop candidates (under-named beneficiaries — all "needs flow cross-check")

The epicenter names are crowded; the beneficiaries one hop away are less-owned. **None of these are buy calls — each is tagged "needs flow cross-check" before any action.**

| Candidate | Hop from | Thesis (1-line) | Tag |
|-----------|----------|-----------------|-----|
| **MU** | node 4 (HBM) | HBM sold out 2026, HBM4 ramp; sits *inside* the epicenter but under-owned vs NVDA | needs flow cross-check |
| **VRT** (Vertiv) | node 7 (power/cooling) | Data-center power+cooling; >$15B backlog end-2025; liquid cooling levered to rack density | needs flow cross-check |
| **ETN** (Eaton) | node 7 (electrical) | Grid-to-rack switchgear/UPS/transformers; ~$14.5B backlog; 800V DC architecture | needs flow cross-check |
| **GEV** (GE Vernova) | node 7 (generation) | Gas turbines / firm generation for the power gap | needs flow cross-check |
| **CEG** (Constellation) | node 7 (nuclear PPA) | TMI-1 restart 2027 (835 MW) under 20-yr MSFT PPA | needs flow cross-check |
| **ANET** (Arista) | node 6 (networking) | Cluster fabric scale-out; less crowded than GPU core | needs flow cross-check |

Sources: [Motley Fool VRT/ETN](https://www.fool.com/investing/2026/07/06/why-vertiv-eaton-ultimate-infrastructure-ai/), [cryptodaily GEV/VRT](https://cryptodaily.co.uk/2026/06/ge-vernova-vertiv-ai-power-bottleneck-trade), [S&P Global utilities](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/7/data-center-demand-has-investors-reevaluating-us-electric-utility-stocks-103396628). Note: node-7 names are **cross-sector** (Industrials/Utilities) — hand off to those sector agents; they belong here only as the AI-power chain terminus.

---

## 6. Deterministic data

### Valuation table (module_fundamentals_us, asof 2026-07-21; NVDA per desk pull)

| Ticker | Price | Trailing P/E | Fwd P/E | PEG | 52w High / Low | Target (mean / median) | Note |
|--------|-------|--------------|---------|-----|----------------|------------------------|------|
| **NVDA** | 205.32 | — | **15.99** | **0.56** | — | — | core; desk pull |
| **AVGO** | 385.27 | 64.10 | **19.84** | **0.42** | 495.00 / 273.00 | 524.51 / 525.00 | custom-ASIC + networking |
| **AMD** | 529.74 | **175.42** | 39.34 | 1.16 | 584.73 / 149.22 | 541.66 / 540.00 | EXTENDED-FLAG (~175x TTM) |
| **MU** | 937.85 | 21.20 | **6.21** | **0.12** | 1255.00 / 103.38 | 1491.95 / 1550.00 | HBM; cheapest fwd multiple |
| **MSFT** | 400.31 | 23.85 | 20.65 | 1.21 | 555.45 / 349.20 | 557.79 / 550.00 | software split reference |

Observations (data only, no recommendation): the epicenter names trade at **low-to-mid teens forward multiples with PEG < 0.6** (NVDA 0.56, AVGO 0.42, MU 0.12) — a valuation profile that argues the correction was multiple compression on rising forward EPS, *not* a bubble deflation. AMD is the outlier: fwd P/E 39 and TTM P/E 175 flag it as **EXTENDED-FLAG (size-down, not add)** per the premortem. MSFT (software) sits at fwd 20.6 / PEG 1.21 — a full multiple with a laggard tape, the mirror image of the semis setup.

### VERBATIM CHART_READ — epicenter names (module_chart --read)

**NVDA** (desk pull) — `PULLBACK-TO-SUPPORT`; ignition trigger **close > 206.27**, swing-low stop **192.53**. (English: trend pullback holding support; needs a >206.27 close + OBV accumulation to confirm the turn.)

**AVGO** (verbatim):
```
OBV: 중립 (20d기울기 +5%)
다이버전스: 없음
MA정렬: 혼조 · 가격 3/4 MA 위
볼린저: 수축(코일링) 11.5% · 중단
RSI: 52.9 · 모멘텀20d +1.3%
턴-판정: PULLBACK-TO-SUPPORT (추세 눌림목)
트리거(점화): close>403.56 + OBV→누적 / 스탑(스윙저점): 360.45
```
(English gloss: OBV neutral (+5% 20d slope); no divergence; MA mixed, price above 3/4 MAs; Bollinger coiling 11.5%; RSI 52.9, +1.3% 20d momentum. Verdict **PULLBACK-TO-SUPPORT**; ignition **close > 403.56** + OBV accumulation, stop **360.45**.)

**AMD** (verbatim):
```
OBV: 분배(매도압력↑) (20d기울기 -67%)
다이버전스: 없음
MA정렬: 혼조 · 가격 3/4 MA 위
볼린저: 수축(코일링) 15.7% · 중단
RSI: 41.5 · 모멘텀20d +1.9%
턴-판정: BASING (바닥 다지기 · 미확인 턴)
트리거(점화): close>530.24 + OBV→누적 / 스탑(스윙저점): 495.76
```
(English gloss: OBV in distribution (−67% 20d slope, sell pressure up); no divergence; MA mixed, price above 3/4 MAs; Bollinger coiling 15.7%; RSI 41.5. Verdict **BASING (unconfirmed turn)**; ignition **close > 530.24** + OBV accumulation, stop **495.76**.)

**MU** (verbatim):
```
OBV: 분배(매도압력↑) (20d기울기 -72%)
다이버전스: 없음
MA정렬: 혼조 · 가격 3/4 MA 위
볼린저: 확장 41.3% · 중단
RSI: 32.1 · 모멘텀20d -11.0%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>996.17 + OBV→누적 / 스탑(스윙저점): 848.95
```
(English gloss: OBV distribution (−72% 20d slope); no divergence; MA mixed, price above 3/4 MAs; Bollinger *expanding* 41.3%; RSI 32.1 (near-oversold), −11.0% 20d momentum. Verdict **NEUTRAL/CHOP (direction unclear)**; ignition **close > 996.17** + OBV accumulation, stop **848.95**.)

**Chart synthesis (data, not a call):** NVDA and AVGO read `PULLBACK-TO-SUPPORT` (constructive-but-unconfirmed); AMD `BASING`; MU `NEUTRAL/CHOP` with the weakest momentum (RSI 32, −11% 20d) — the tape confirms §1's "money is leaving" on the memory/laggard names while the leaders hold support. Every name shares the pattern: **price above most MAs, coiling/oversold, awaiting an ignition close** — i.e., de-risked and set, not broken.

---

## 7. Track-KPIs + anti-signals

**Confirming KPIs (thesis intact / re-accelerating):**
- **Hyperscaler capex guides** hold/raise the ~$725B → ~$1T path (next reads: GOOGL 7/22 after close; MSFT/META/AMZN on their July/Aug prints).
- **NVDA data-center revenue sequential** stays positive (next NVDA print is the definitive read).
- **Nasdaq COT %ile** — currently ~4%ile crowded-short; a *rise* off the floor = fear unwinding (fuel spent = squeeze delivered).
- **SOX relative strength** turns up vs SPX (leadership re-taken).
- **Ignition closes**: NVDA > 206.27, AVGO > 403.56, AMD > 530.24, MU > 996.17 (per §6).

**Anti-signals (EXTENDED-BUT-LIVE → EXHAUSTED flip):**
- **real10y > 2.55%** — the macro ceiling bites; multiple compression resumes regardless of earnings.
- **A hyperscaler capex GUIDE CUT** (not a beat/miss on current-q revenue) — this is the *only* clean demand-break signal. A capex *cut* flips "factor unwind" to "demand break."
- **NVDA DC revenue sequential goes flat/negative** — order-flow break at the core.
- **HBM/CoWoS shifts from sold-out to available** (lead times shorten) — bottleneck relief = demand caught up = pricing power fades.
- **AMD-type extension spreads to NVDA/AVGO** (fwd P/E re-expands toward AMD's 39x without EPS follow-through).

**Momentum tags (premortem):**
- **NVDA / AVGO = EXTENDED-BUT-LIVE** — capex accelerating $725B→~$1T; the semis dip is an **MTUM factor-unwind, not a demand break**. Live until a *capex guide cut* or *real10y > 2.55%* flips it to EXHAUSTED.
- **AMD = EXTENDED-FLAG** — ~175x TTM P/E; **size-down, not add**.

**The 7/22 catalyst pair (asymmetry):**
- **GOOGL** (Comm Services, AI-adjacent) reports **7/22 after close**: Street ~$2.88 EPS (+25%), rev ~$116.5B (+21%) ([MarketBeat](https://www.marketbeat.com/articles/alphabets-ai-spending-question-looms-over-q2-earnings/), [TipRanks](https://www.tipranks.com/news/tesla-tsla-or-alphabet-googl-buy-one-ai-tech-stock-avoid-the-other-says-wall-street-ahead-of-july-22-earnings)). A **beat + raised capex** firing into a **4%ile crowded-short Nasdaq = asymmetric squeeze** through the whole AI-compute complex.
- **TSLA** reports the same evening: Street ~$0.52 EPS, ~$26.0B rev. A **TSLA miss is the against-us** — it can drag SMH/NVDA by sentiment contagion even though Tesla is not in the compute chain. Watch which print sets the tape into 7/23.

---

## 8. ★ DIVERGENCE VERDICT (mandatory)

**Resolution: EARLY RE-ENTRY, not a falling knife — on the epicenter (semis / AI-compute). The red tape is a TAPE read, and it must NOT be allowed to masquerade as a CYCLE read.**

The evidence stack resolves the divergence one way:
1. **Demand is accelerating** — hyperscaler capex guides ~$725B → ~$1T, up 77% YoY (§3). The drawdown happened *while the demand guide rose*.
2. **The bottleneck is sold out** — CoWoS + HBM oversubscribed through 2026–27 (§4). Sold-out = pricing power, the opposite of demand-break.
3. **Valuation compressed, not inflated** — epicenter fwd P/E in the teens, PEG < 0.6 (NVDA 0.56, AVGO 0.42, MU 0.12) (§6).
4. **Positioning is washed out** — 33 red names + Nasdaq 4%ile crowded-short + hedge funds four weeks of selling = a *completed* de-risk (§1). At the 4%ile, the marginal seller is exhausted; the pain trade is UP.

The semis red is an **MTUM factor-unwind on an intact secular cycle**, not a break. That is the definition of early re-entry.

**★ ENCODED CORE-vs-ADD RULE (the discipline this file exists to carry):**

> The 2026-07-14 postmortem's named failure was letting a red tape drive the **#1-cycle epicenter core to 0%**. The rule that prevents the repeat:
>
> 1. **NVDA is a 12% CORE FLOOR (min_epicenter). It is held REGARDLESS OF TAPE.** Red flow, 33 red names, and the "crowded" tag **NEVER** take the core below 12%. Core sizing answers "is this CYCLE #1?" (yes) — it does not answer "how is the tape today?"
> 2. **Red flow / 33 red names / "crowded" GATE ADD *TIMING* ONLY.** They decide *when and how fast you add above the floor* — never whether the floor exists. A red tape is a reason to stage adds, not to breach the core.
> 3. **4%ile crowded-short = FADE-THE-FEAR ADD TRIGGER**, not a stay-away signal. Fast-money washout is the *setup* for the squeeze, so extreme crowded-short is a reason to lean toward adds (staged), not away.
> 4. **Add mechanics:** NVDA/AVGO EXTENDED-BUT-LIVE → stage adds above the floor on ignition closes (NVDA > 206.27, AVGO > 403.56). AMD EXTENDED-FLAG → **size-down, not add** (~175x TTM). MU HBM → chain-hop, needs flow cross-check.

**The observable that FLIPS the verdict (early re-entry → falling knife):** a **hyperscaler CAPEX GUIDE CUT** (demand break, not a single-quarter revenue miss) **OR real10y > 2.55%** (macro ceiling bites). Either one flips NVDA/AVGO from EXTENDED-BUT-LIVE to EXHAUSTED and turns the pullback into a knife. Absent both, red flow is timing information, and the 12% NVDA core floor stands.

**One-line verdict:** #1-cycle epicenter — hold the **12% NVDA core through the red tape**; let flow gate *add timing* only; treat **4%ile crowded-short as a fade-the-fear add trigger**; flip only on a hyperscaler capex-guide cut or real10y > 2.55%.

---

### Sources
- Hyperscaler capex: [valueaddvc $725B](https://valueaddvc.com/blog/ai-hyperscaler-capex-compared-why-microsoft-google-meta-and-amazon-are-all-spending-at-once), [CNBC ~$700B](https://www.cnbc.com/2026/02/06/google-microsoft-meta-amazon-ai-cash.html), [Yahoo/Futurum](https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/)
- Semis correction: [intellectia selloff](https://intellectia.ai/blog/semiconductor-stocks-selloff-june-2026), [intellectia rotation 7/12](https://intellectia.ai/blog/ai-semiconductor-stocks-july-2026-market-rotation-2026-07-12), [Motley Fool 20% drawdown](https://www.fool.com/investing/2026/07/18/history-buying-chip-stocks-20-drawdown-avgo/)
- Semis vs software: [SeekingAlpha XSW](https://seekingalpha.com/article/4920379-timing-the-next-market-rotation-semis-software-and-the-hyperscalers), [cryptobriefing](https://cryptobriefing.com/tech-trade-2026-chip-stocks-software-decline/), [Benzinga software ETFs](https://www.benzinga.com/etfs/sector-etfs/26/06/60139041/software-etfs-are-finally-catching-an-ai-tailwind)
- Bottleneck: [fusionww CoWoS/HBM](https://info.fusionww.com/blog/inside-the-ai-bottleneck-cowos-hbm-and-2-3nm-capacity-constraints-through-2027), [enkiai HBM](https://enkiai.com/ai-market-intelligence/ai-supply-chain-crisis-2026-the-new-hbm-bottleneck/), [oplexa TSMC packaging](https://oplexa.com/ai-chip-packaging-bottleneck-2026/)
- AI-power chain: [Motley Fool VRT/ETN](https://www.fool.com/investing/2026/07/06/why-vertiv-eaton-ultimate-infrastructure-ai/), [spheron power](https://www.spheron.network/blog/ai-data-center-power-constraints-2026/), [S&P Global utilities](https://www.spglobal.com/market-intelligence/en/news-insights/articles/2026/7/data-center-demand-has-investors-reevaluating-us-electric-utility-stocks-103396628)
- COT / positioning: [SmartFlow COT 7/14](https://smartflow.trading/cftc-cot-report-analysis-july-14-2026/), [RogueQuant](https://roguequant.substack.com/p/the-market-doesnt-take-vacations)
- 7/22 earnings: [MarketBeat GOOGL](https://www.marketbeat.com/articles/alphabets-ai-spending-question-looms-over-q2-earnings/), [TipRanks GOOGL/TSLA](https://www.tipranks.com/news/tesla-tsla-or-alphabet-googl-buy-one-ai-tech-stock-avoid-the-other-says-wall-street-ahead-of-july-22-earnings)
- Deterministic: module_fundamentals_us + module_chart, asof 2026-07-21
