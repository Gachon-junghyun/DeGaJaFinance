# SECTOR DEEP-DIVE — Utilities (UTIL) — 2026-07-15 (Wed)

**Desk:** industry_US · **Status:** PROMOTED Neutral → OW (flow #1, wflow 0.415, broad-but-shallow) · **English-pure · Zero buy/sell calls — analytical map only.**

**CENTRAL QUESTION:** Is the flow-#1 UTIL bid an **AI-power load-growth thesis** or a **rate-relief bond-proxy bid**?

## VERDICT (up front)

**The flow-#1 UTIL bid is predominantly a RATE-RELIEF BOND-PROXY bid, not an early-cycle AI-power load-growth bid.** Four independent tells converge:

1. **The flow sits in regulated bond-proxies, not IPPs.** Accumulation (OBV 매집) is broad across the regulated T&D complex (PEG, NEE, SO, D, AEP, ETR, PCG) while the marquee AI-power/nuclear name **CEG ranks dead last** (flow 0.177, OBV neutral) and is being **shorted at an extreme** (short-vol Z +1.92, 🔴). [flow]
2. **Breadth is 0.0 — zero acceleration (🟢) names, one 🔴.** A flow that is #1 by weighted score yet has *no* momentum-green constituents is the fingerprint of a **defensive duration bid**, not a growth chase. [flow]
3. **The macro trigger is real-yield relief, dated to the day.** June CPI printed cool (−0.4% MoM, 3.5% YoY vs 3.8% exp, released 07-14); 10Y fell to 4.583%, 2Y to 4.185%. Regulated utilities are long-duration bond proxies — this is the mechanical bid. [WebSearch][MACRO_REPORT]
4. **The AI-power leg is being actively throttled and de-rated.** NY's first-in-nation moratorium (EO No. 62, 07-14) + a nationwide state-bill wave, plus >half of developers routing behind-the-meter, cut the *regulated* load-growth channel — which is exactly why CEG "behaves like a traditional utility" and lost ~35% of its value in H1 2026. [WebSearch]

**Regime implication:** UTIL here is a **rate trade, not a cycle.** It is early *only* in the sense that real-yield relief is early; it **reverses if inflation re-lifts** (the macro desk's P1 anti-signal — a hot PPI/oil spike pushing real-10Y >2.5%). The one genuine AI-power sub-leg still receiving flow is **VST (merchant/IPP)**, and even that is a *pullback-to-support* structure, not a breakout.

---

## 1. Flow cross-check — regulated (bond-proxy) or IPP (AI-power)?

`module_flow NEE SO D VST CEG PEG AEP --bench SPY --json` [flow]

| Ticker | Type | Flow tag | News vel | OBV | Vol surge |
|---|---|---|---|---|---|
| NEE | Regulated (FPL) + NEER renewables | 🟡 neutral | 1.37x | **매집 (accum)** | 0.86x |
| SO | Regulated | 🟡 neutral | 1.10x | **매집** | 0.59x |
| D | Regulated | 🟡 neutral | 1.07x | **매집** | 0.59x |
| PEG | Regulated (+ nuclear) | 🟡 neutral | 1.09x | **매집** | 0.88x |
| AEP | Regulated T&D | 🟡 neutral | 2.14x | **매집** | 0.76x |
| VST | **Merchant / IPP** | 🟡 neutral | 1.12x | **매집** | 0.76x |
| CEG | **IPP / nuclear-for-DC** | 🟡 neutral | 1.22x | **중립 (neutral)** | 0.70x |

Full-sector ranking (SECTOR_FLOW_US.json, Utilities constituents, sorted by flow_score) [flow]:

```
PEG 0.700  NEE 0.692  VST 0.639  ETR 0.613  SO 0.579  D 0.542
PCG 0.509  AEP 0.439  SRE 0.342  EXC 0.284  CEG 0.177  DUK 0.162
WEC 0.119  ED 0.096   XEL -0.248 (🔴 분산/distribution)
```

Short-pressure cross-check — `scripts/us_flow.py VST CEG NEE` (FINRA Reg SHO, asof 07-14) [flow]:

| Ticker | Short% | Base20 | Z | 5v5 trend | Verdict |
|---|---|---|---|---|---|
| VST | 40.3% | 41.6% | −0.16 | −11.0 ▼ | 🟡 normal |
| **CEG** | **64.7%** | 49.5% | **+1.92** | +1.8 ▲ | **🔴 short surge (extreme vs own base)** |
| NEE | 60.7% | 48.1% | +1.27 | +9.6 ▲ | 🟡 normal-high |

**Read:** The accumulation is concentrated in the **regulated bond-proxy complex** (top-8 flow all regulated except VST). The two pure AI-power/nuclear-IPP names split hard: **CEG is exhausting** — bottom of the flow ranking, OBV neutral (no accumulation), and an *extreme* short surge (Z +1.92) — while **VST is the lone IPP still accumulating** with normal short pressure. This directly answers the central question: **the bid is regulated (bond-proxy), not IPP (AI-power).**

---

## 2. Sub-leg split — three legs, three drivers

| Sub-leg | Names (flow leaders) | Primary driver | 07-15 flow read |
|---|---|---|---|
| **A. Regulated T&D** | NEE(FPL), SO, D, AEP, PEG, ETR, PCG | **Discount rate / rate-case allowed ROE** — long-duration bond proxy. Falls when real yields fall. | **Broad 매집.** This *is* the flow-#1 bid. Bond-proxy. |
| **B. Merchant / IPP** | **VST**, CEG, NRG | **Merchant power price + datacenter PPA/co-location.** AI-power growth beta. | **Bifurcated:** VST accum (best IPP), CEG exhausted + shorted. |
| **C. Renewables-yield** | NEE (NEER arm), PCG | Tax-credit/PPA economics + rate base growth; rate-sensitive on the yield leg. | Rides A via NEE; not a distinct flow signal. |

**Driver map:** Leg A is a **duration/rate trade** — its 2026 bid is the CPI-driven real-yield drop, full stop. Leg B is the only **genuine AI-power beta**, and the moratorium/behind-the-meter forces (§3) are precisely what fractured it (VST survives on secured PPAs; CEG's premium unwound). The flow being 7:1 skewed to Leg A over clean Leg B exposure is the core evidence for the bond-proxy verdict.

---

## 3. Moratorium impact — who loses the load-growth, who is pure-rate

**NY EO No. 62 (signed 07-14, Gov. Hochul):** first statewide moratorium on new hyperscale data centers ≥50 MW; pauses state environmental permits up to one year while a Generic Environmental Impact Statement / ratepayer-protection framework is built. **~12 GW of DC load sits in the NYISO interconnection queue** (>8 GW entered in 2025 alone) — that is the pipeline now frozen. [WebSearch]

**State-bill wave (the bifurcation, quantified):** >300 DC bills filed across 30+ states in 2026. **At least 18 states** have introduced bills creating **special rate classes for large loads** (forcing DCs to pay full interconnection cost / demand-response — anti-cost-shift). NY is the only *enacted* one-year moratorium; similar moratoria **failed** in MD, MN, NH, OK, SD, WI; Ohio's ≤25 MW ballot ban failed to qualify (retry 2027); Ohio & Utah governors **paused new DC tax exemptions**; Virginia added a **$0.011/kWh** DC energy tax (capped $600M/yr) while keeping its sales-tax exemption; Georgia's incentive-limit bill was vetoed. [WebSearch]

**Behind-the-meter bypass (who wins/loses):** **56% of developers** are exploring co-located/on-site generation (Foley 2026 survey — 3rd-most-common tactic after PPAs and grid interconnects); McKinsey forecasts **25–33% of new DCs to be BTM**; ~82 GW of BTM capacity announced since 2025 (though ~60% is still only announcements/early-stage, ~2 GW operating today). [WebSearch]

**FERC swing factor (matters for Leg B):** FERC **rejected** the Talen–Amazon Susquehanna co-location ISA (grid-reliability/cost-allocation), but its **later order creating pathways for DC-next-to-plant siting is a "major positive" for VST/Talen.** VST separately holds **20-yr PPAs for >2,600 MW of nuclear to Meta** (deliveries begin late-2026). [WebSearch]

**Bifurcation summary:**
- **Throttled (grid-interconnect / regulated load-growth at risk):** NY-exposed regulated utilities and the *regulated* AI-load-growth narrative broadly. This is why the flow rotated to *rate* names, not *growth* names.
- **Exhausted (AI-power premium de-rated):** **CEG** — Citi cut PT to $297 (Neutral) after the PJM meeting; stock hit a 52-wk low $228.63 and shed **~35% of market value in H1 2026**; now "valued more like a traditional utility." [WebSearch]
- **Still standing (secured merchant PPA):** **VST** — contracted nuclear-to-Meta + a favorable FERC co-location order; the one IPP with live flow.
- **NOTE FOR INDU DESK:** BTM self-sourcing = the value migrates from utilities to **on-site power equipment** (gas turbines, gensets, fuel cells, grid gear). Utilities lose the load; equipment OEMs win the capex. Flag for Industrials.

---

## 4. IR / filings — NEE 10-K (FY2025, filed 2026-02-13) [filing]

`module_business_us NEE --full --json`. Item 1A regulatory anti-signals confirm the **rate-case, not AI-PPA**, driver for the flow-leader regulated name:

- **"NEE's and FPL's business… may be materially adversely affected by the extensive regulation of their business."** FPL is subject to **FPSC jurisdiction over retail base rates and cost-recovery clauses** — earnings hinge on the regulator granting **"a reasonable return on invested capital through base rates."** This is a **rate-case/allowed-ROE engine**, not merchant power-price or datacenter-PPA upside. [filing]
- **Explicit rate-sensitivity anti-signal in the risk factors:** development of generation/storage is exposed to **"inflation, rising interest rates"** and supply-chain — i.e., the filing itself names rising rates as a headwind, the mirror image of the current falling-rate bid. [filing]
- Business mix: ~80 GW net capacity (gas, wind, solar, nuclear, storage); two arms — **FPL (largest US regulated electric utility)** + **NEER (renewables/merchant)**. The *regulated* FPL arm dominates the identity → confirms NEE trades as a rate-base/duration proxy, with NEER renewables-yield as the secondary, also-rate-sensitive leg. [filing]

**Anti-signal net:** NEE's own 10-K frames its earnings power around FPSC-approved ROE and flags rising rates as a risk — consistent with a bond-proxy, not an AI-growth, tape.

---

## 5. Value chain & bottleneck

```
FUEL/GEN                 TRANSPORT        DISTRIBUTION      MONETIZATION
gas / nuclear /   ──►  transmission  ──►  distribution  ──►  REGULATED: allowed ROE on rate base (FPSC/PUC)
renewables / storage      grid            (T&D)              MERCHANT: power price + datacenter PPA/co-lo
        │                    │                                       │
        └── BTM bypass ──────┴── routes AROUND the utility ──────────┘ (equipment OEMs capture capex → INDU)
```

**Bottleneck(s):**
1. **Interconnection queue** — 12 GW frozen in NYISO; the physical throttle on regulated load-growth. [WebSearch]
2. **Regulatory ROE / rate cases** — the earnings governor for Leg A; the value driver is the *discount rate applied to* that ROE, i.e., the 10Y real yield. [filing]
3. **The moratorium + FERC co-location rules** — the on/off switch for Leg B's AI-power PPA demand. [WebSearch]

The chain shows why flow chose Leg A: the *regulated* monetization node revalues on rates (a live, dated catalyst) while the *merchant* node is gated by regulatory bottlenecks that just tightened.

---

## 6. Chart read — regulated (NEE) vs IPP (VST) structure contrast

`module_chart NEE --read` (verbatim CHART_READ):

```
OBV: 분배(매도압력↑) (20d기울기 -29%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 0/4 MA 위
볼린저: 확장 nan% · 중단
RSI: nan · 모멘텀20d +nan%
턴-판정: NEUTRAL/CHOP (방향 불명확)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 85.73
```
*Gloss:* bullish MA stack but **OBV distributing (−29% 20d)** and price under all 4 MAs → NEUTRAL/CHOP. A **duration proxy drifting on rates**, not a trending growth name. (Note the divergence: the 30d flow module reads NEE OBV as 매집; the 20d chart reads distribution — the accumulation is a *slow bond-proxy bid*, not momentum.)

`module_chart VST --read` (verbatim CHART_READ):

```
OBV: 누적(매수압력↑) (20d기울기 +16%)
다이버전스: 강세(가격 저점↓ · RSI 저점↑)
MA정렬: 혼조 · 가격 3/4 MA 위
볼린저: 수축(코일링) 11.3% · 중단
RSI: 44.5 · 모멘텀20d +3.3%
턴-판정: PULLBACK-TO-SUPPORT (추세 눌림목)
트리거(점화): close>159.20 + OBV→누적 / 스탑(스윙저점): 151.05
```
*Gloss:* **OBV accumulating (+16%)**, bullish RSI divergence, Bollinger coiling (11.3%), price 3/4 MAs → **PULLBACK-TO-SUPPORT** with an ignition trigger at close >159.20. The lone IPP with genuine constructive structure — but a *pullback*, not a breakout.

**Contrast:** the regulated bellwether (NEE) is chop/duration-drift; the surviving IPP (VST) is a coiled pullback. Both consistent with the verdict — the *rate* leg is being bid quietly; the *AI-power* leg has one coiled survivor and one broken leader (CEG).

---

## 7. Track-KPIs & anti-signals

**KPIs (leading tells):**
| KPI | Why | Bond-proxy vs AI-power tell |
|---|---|---|
| **10Y real yield** (currently ~2.36% pre-CPI mark; 10Y 4.583% post-CPI) | The bond-proxy driver | Real yield ↓ = Leg A bid persists; ↑ = it unwinds. **THE top KPI.** |
| Datacenter PPA signings / FERC co-location orders | Leg B (IPP) demand | New secured PPAs (VST-type) = AI-power leg real; rejections (Talen-type) = gated |
| Moratorium spread to TX / VA | Load-growth contagion | Spread beyond NY = regulated load-growth throttle widens |
| Rate-case outcomes (FPSC/PUC allowed ROE) | Leg A earnings governor | Constructive ROE = rate-base story intact |
| IPP merchant power prices (PJM) | Leg B margin | Firming = VST leg supported; softening = de-rate continues |

**Anti-signals (kill switches):**
- **A1 — Inflation re-lift (kills the bond-proxy bid).** Hot PPI (today 08:30 ET print) or a Hormuz oil spike re-lifts breakevens, pushes **real-10Y >2.5%** → the rate-relief risk-on unwinds and long-duration defensives sell off. This is the MACRO desk's explicit P1 other-branch. **Primary anti-signal.** [MACRO_REPORT]
- **A2 — Moratorium contagion (kills the load-growth leg).** NY EO spreading to large-DC states (TX/VA) or more of the 18 special-rate-class bills enacting → regulated AI-load-growth narrative throttled further; would deepen the CEG-style de-rate across IPPs. [WebSearch]

---

## Sources
- [flow] `module_flow`, `scripts/us_flow.py`, `out/flow/2026-07-15.json`, `SECTOR_FLOW_US.json` (this run, asof 07-14)
- [filing] NEE 10-K FY2025 (filed 2026-02-13) via `module_business_us`
- [MACRO_REPORT] `llm_outputs/2026-07-15/industry_US/MACRO_REPORT.md`
- [WebSearch] NY Gov. Hochul EO No. 62 (governor.ny.gov, 07-14); Axios/NBC/Bloomberg 07-14; CNBC "Treasury yields slide after June CPI" 07-14; TheStreet/AOL CEG downgrade (Citi PT $297); MultiState / Good Jobs First / ArentFox state-bill trackers 2026; Foley 2026 Data Center Survey & McKinsey (behind-the-meter); PowerMag / Utility Dive / Bloomberg Law (Vistra PPAs, FERC co-location order)
