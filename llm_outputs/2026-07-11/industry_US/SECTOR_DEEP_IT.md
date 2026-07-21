# SECTOR DEEP — Information Technology (IT)
**Phase-2 DEEP agent | US industry desk | 2026-07-11**
Analytical only. Zero buy/sell recommendations. Sizing language = relative conviction, not advice.

Macro drivers in play (Phase 0): **M-07** AI datacenter capex now a *named inflation input* (market pays for contracted physical backlog — Apple/Broadcom $30B captive silicon through 2031); **M-10** memory/HBM shortage, +55–60% DRAM contract prices, memory re-rating (UBS: memory out-earns hyperscalers); **M-08** concentration (semis ~19.7% of S&P); **M-12** DeepSeek own-chip + China H200 greenlight = marginal moat erosion. Backdrop: hawkish-of-neutral Fed, AI mega-cap de-rate is **rotation not rupture** ($1T off Nvidia), Nasdaq-100 COT at 1%ile crowded-short = rebound ammo.

---

## 1. FLOW — where is IT heading?

**News intensity (30–45d, foreign tape).** Broad IT-term sweep (HBM/custom silicon/AI chip/foundry/GPU/accelerator/CoWoS/DRAM) returns **2,522 matches/30d** — the tape is saturated with semis. The signal is not volume but *rotation within the complex*. [news]

**Latest US daily cards — AI Compute & Semiconductors (07-09 desk):** three live threads. [news]
1. **AVGO–Apple $30B+ custom-silicon + wireless pact through 2031**, Apple investing $1.5B into Broadcom's Fort Collins fab. AVGO +5–6%, AAPL flat. The asset that expanded is Broadcom's **captive, non-cancellable custom-silicon backlog locked to 2031** — merchant-silicon supplier captures the durable value, not the OEM. Framed as reshoring optics; substance is multi-generation revenue visibility.
2. **NVDA −16% / ~$1T off (May-14 high) to ~16–18x fwd** — cheapest since 2019, *below* the S&P. Street kept **raising** NVDA estimates as the stock fell → "rotation not correction." Money rotated into **MU/AMD/INTC**. China signaled Alibaba own-chip (M-12 moat erosion).
3. **Memory bear market**: MU −22%, SNDK −30% off late-June highs (after MU ~3x, SNDK +489% YTD). Bear = memory costs crimp phone/PC/console demand; bull = demand has **decoupled** from consumer devices, priced by capacity rigidity. Micron flagged **HBM TAM crossing $100B in 2027**, lifted FY26 capex to ~$27B. [SEC/news] Kill-line = contract prices bending.

**FINRA daily short-vol z-scores (2026-07-09 tape) — divergences flagged:** [FINRA]

| Ticker | Short% | z vs 20d | 5v5 trend | Read |
|---|---|---|---|---|
| **AEHR** | 60.9% | **+3.68** 🔴 | +6.9▲ | EXTREME short surge — skeptics leaning hard against the HBM/SiC burn-in-test thesis |
| **AMKR** | 63.7% | **+1.50** 🔴 | +14.9▲ | Short surge on OSAT/advanced-packaging — bears fading the CoWoS bottleneck story |
| LITE | 56.8% | +1.72 🔴 | −10.1▼ | Short surge *into* a falling tape (optical) — momentum-negative |
| PLTR | 59.7% | +1.71 🔴 | +21.8▲ | Crowded-short software; rebound fuel if narrative holds |
| AVGO | 49.3% | +1.34 🟡 | +6.5▲ | Elevated hedges after the Apple-deal pop (profit-taking), still normal band |
| **AMD** | 40.7% | **−2.01** 🟢 | −6.5▼ | Short-cover / pressure exit — **confirms AMD as the rotation destination** off NVDA |
| **COHR** | 40.1% | **−1.80** 🟢 | −6.3▼ | Short-cover on optical/networking — positive divergence vs quiet narrative |
| KLAC | 31.6% | −0.56 | −19.2▼ | Sharp short de-escalation into WFE |

*Interpretation:* the **narrative-confirming** flow is AMD short-covering (rotation destination) and NVDA short-vol *normalizing* (34.9%, z−0.15) despite the −16% drawdown — sellers are not pressing. The **contra-narrative** flow sits at the packaging/test node: AEHR (+3.68) and AMKR (+1.50) shorts are *fading* the CoWoS/HBM-test bottleneck bull case even as advanced-packaging news runs hot (100 mentions/45d). That skepticism is the crowded trade to watch — a squeeze setup if capacity data confirms.

---

## 2. PLAYERS

**(a) Top300 IT members — 56 names** [yfinance/us_top300.csv]. By node concentration:
- **GPU/accelerator:** NVDA (5.10T), AMD (876B)
- **Custom silicon / ASIC / merchant:** AVGO (1.96T), MRVL (272B), QCOM (238B)
- **Memory / storage:** MU (1.28T DRAM/HBM/NAND), SNDK (324B NAND), WDC (257B), STX (242B)
- **EDA/IP:** CDNS (107B), SNPS (87B), ARM (468B — files 20-F, no 10-K)
- **Foundry/WFE:** ASML (744B), AMAT (490B), LRCX (487B), KLAC (339B), TER (69B), Q/Qorvo? (35B)
- **Networking / connectivity / optical:** ANET (214B), CSCO (471B), CIEN (61B), LITE (66B), COHR (76B optical)
- **Analog/other semi:** TXN (294B), ADI (212B), NXPI (79B), MPWR (77B), MCHP (54B), ON (47B)
- **Systems/software (non-core to thesis):** MSFT, ORCL, PLTR, CRM, NOW, PANW, CRWD, FTNT, ADBE, INTU, DDOG, APP, SHOP, IBM, ACN, ADSK, MSTR
- **Hardware/EMS:** AAPL (4.38T), DELL (265B), HPE (63B), APH (202B), GLW (168B), TEL (64B), JBL (39B)
- Note: **TSM absent** from the US universe file (Taiwan ADR) — the foundry node's prime name is off-sheet; treat as external dependency.

**(b) UNION — thematic small/mid-caps below the top300 cutoff (~$35B)** qualifying at ≥2x news + real US ticker + mcap ≥$2B: [yfinance/news]
- **CRDO / Credo** — $48.6B, Tech/Semis. AEC copper active-cable connectivity for AI racks. **69 news mentions/45d.** (Big enough for top300 but absent from CSV — genuine below-radar leak.)
- **ALAB / Astera Labs** — $71.9B, Tech/Semis. PCIe/CXL retimers, connectivity fabric. **44 mentions.**
- **AMKR / Amkor** — $17.7B, Semi Equip & Materials. OSAT advanced packaging (CoWoS-adjacent). **20 mentions.** FINRA short-surge (z+1.50).
- **ONTO / Onto Innovation** ($16.0B), **NVMI / Nova** ($15.2B) — packaging/metrology inspection (HBM stacking yield).
- **CAMT / Camtek** — $6.8B, packaging inspection.
- **SMCI / Super Micro** — $18.6B, AI server integration.
- **AEHR / Aehr Test Systems** — $2.3B, HBM/SiC burn-in test. FINRA **extreme** short (z+3.68).
- Cross-sector flags: **VRT / Vertiv** ($124B, *Industrials* — datacenter power/thermal, IT→INDU), not an IT member but the physical enabler of M-07. Photomask (PLAB $1.7B) **dropped** — sub-$2B and only 1 mention.

---

## 3. IR / WHO-DOES-WHAT (10-K Item 1 / 1A / 7 — English SEC text) [SEC]

**NVDA** (10-K 2026-02-25, FY-end 2026-01-25). "Data-center-scale AI infrastructure company"; moat = **CUDA** full-stack (libraries/SDKs/APIs on all GPUs) + unified programmable architecture across multi-$B end markets. FY26 revenue driven by **Blackwell** (majority of Data Center rev) + networking. **Item 1A anti-signals:** long mfg lead times + uncertain supply/capacity → supply-demand mismatch (has already occurred); third-party foundry/packaging dependency (TSMC/CoWoS) reduces control of yield & schedule; competition to market share. MD&A flags **energy/datacenter/capital availability** for customer buildout as crucial — a multi-year regulatory-heavy constraint (ties to M-07 power bottleneck).

**AVGO** (10-K, FY-end 2025-11-02). Semis + infrastructure software (VMware/CA/Symantec). Strategy = "category-leading" custom + merchant silicon. The Apple 2031 pact makes the **captive custom-ASIC backlog** the durable asset. Item 1A: acquisition-integration risk (VMware), customer concentration.

**MU** (10-K 2025-10-03, FY-end 2025-08-28). DRAM/NAND/NOR + HBM; Micron/Crucial brands. MD&A **Industry Conditions: "AI-driven demand is accelerating and is outpacing industry [supply]."** **Item 1A anti-signals (the thesis kill-list itself):** volatility in ASPs; gross-margin factors; **realizing expected returns from capacity expansions** (over-build risk); highly competitive. This is the M-10 barometer — ASP volatility is *the* variable.

**MRVL** (10-K 2026-03-11, FY-end 2026-01-31). Fabless data-infrastructure SoC (data-center-core to network-edge), custom ASIC + electro-optics + interconnect. **Item 1A anti-signal:** *"dependence on a few customers for a significant portion of revenue… as our major customers comprise an increasing percentage"* — the custom-silicon model's structural fragility (hyperscaler concentration cuts both ways vs AVGO). Also names AI-model impact on its own business as a risk.

---

## 4. VALUE-CHAIN DENSITY MAP (left → right dependency)

```
[1] EDA/IP ───▶ [2] Foundry ───▶ [3] Memory/HBM ───▶ [4] Advanced Packaging ───▶ [5] GPU/Accel ───▶ [6] Custom Si/ASIC ───▶ [7] Networking/Optical ───▶ [8] Hyperscaler/Deploy
  CDNS SNPS      TSM(ext)         MU SNDK WDC STX       AMKR ONTO NVMI          NVDA AMD          AVGO MRVL QCOM        ANET CRDO ALAB          MSFT ORCL PLTR
  ARM            ASML AMAT         [+HBM test: AEHR      CAMT [CoWoS]                                                    CIEN LITE COHR CSCO      (+SMCI DELL HPE
                 LRCX KLAC TER      TER]                 <<BELOW-RADAR>>                          <<AVGO=captive        <<BELOW-RADAR:            servers)
                                   <<M-10 RE-RATE>>                                                 2031 backlog>>        CRDO/ALAB>>
```

**Cross-sector chains (flagged):**
- **IT → UTIL (power):** NVDA MD&A names *energy availability* as the binding buildout constraint → UTIL power/grid (CEG/VST/TLN/GEV territory). M-07's inflation channel runs through the power node.
- **IT → INDU (electrical/thermal):** VRT (Vertiv, power/cooling), APH/TEL (connectors/cabling), electrical equipment — the physical datacenter shell.

**BELOW-RADAR layer (do NOT converge on Nvidia):**
1. **Advanced packaging / CoWoS (node 4)** — AMKR, ONTO, NVMI, CAMT, AEHR. The physical bottleneck for accelerator output; *contra-narrative shorts are stacking here* (AEHR z+3.68, AMKR z+1.50) → highest-tension, least-crowded-long node.
2. **AI networking/connectivity (node 7)** — CRDO, ALAB, COHR. Every GPU added multiplies interconnect; CRDO 69 mentions but off the top300 sheet. COHR short-covering (z−1.80) is a quiet positive divergence.
3. **Memory re-rate (node 3)** — MU/SNDK/WDC/STX all *in* top300 but freshly drawn-down 22–30%; the re-rate is the crowded-but-corrected trade, priced on ASP rigidity not device volumes.

---

## 5. BOTTLENECK + KPI + ANTI-SIGNAL

**Binding constraints (strong demand ≠ bottleneck):**
- **HBM/advanced-packaging (CoWoS) capacity** — the true throughput cap on accelerators. KPI: TSMC CoWoS wafer allocation, AMKR/OSAT utilization, ONTO/NVMI/AEHR order flow.
- **Foundry advanced-node (N3/N2)** — TSM external, ASML EUV shipment cadence.
- **Datacenter energy/interconnect** — power availability (NVDA-named), rack-level optical/copper (CRDO/ALAB/COHR).
- **NOT bottlenecks:** GPU demand (abundant), DRAM *demand* (abundant — the constraint is capacity/ASP, not appetite).

**Current KPI readings:** [SEC/news]
- DRAM contract prices **+55–60%** (M-10); Micron: *demand outpacing supply*, HBM TAM **>$100B by 2027**, FY26 capex ~$27B. 🟢
- NVDA fwd multiple ~16–18x (below S&P) with **rising** Street estimates → valuation-reset not demand-reset. 🟢
- AVGO custom backlog contracted to **2031** (non-cancellable). 🟢
- FINRA: AMD short-cover (rotation confirmed); AEHR/AMKR short-surge (packaging skepticism — watch for squeeze or capacity disappointment). 🟡

**What KILLS the thesis (anti-signals):**
1. **A hyperscaler capex-DOWN guide** (MSFT/GOOGL/META/AMZN) — collapses M-07 the moment contracted backlog stops compounding. Single highest-impact kill-switch.
2. **DRAM/HBM capacity flood** — MU's own Item 1A "returns from capacity expansions" + inventory build → **contract prices bend** → memory re-rate reverses (SNDK/MU/WDC/STX unwind). The 07-09 card's explicit bear_trigger.
3. **OEM pass-through breaks consumer demand** — proves the supercycle rode phone/PC volumes after all (memory decoupling thesis fails).
4. **M-12 acceleration** — China H200 greenlight + DeepSeek/Alibaba own-chip erodes NVDA/AVGO marginal moat and merchant-silicon pricing.
5. **CoWoS capacity disappointment** — validates the AEHR/AMKR shorts; caps accelerator output *and* removes the packaging-node long.

---

## SHORTLIST (ranked — for Phase-3 bet sheet)

| # | Ticker | One-line thesis | Chain node | Freshness |
|---|--------|-----------------|------------|-----------|
| 1 | **AVGO** | Captive non-cancellable custom-ASIC backlog locked to **2031** (Apple $30B+); merchant-silicon premium compounds — the durable-visibility play. | [6] Custom Si/ASIC | 07-09 card, live; FINRA hedges elevated post-pop (z+1.34) |
| 2 | **MU** | M-10 memory re-rate; ASP rigidity decoupled from devices, HBM TAM >$100B by 2027; −22% drawdown = corrected entry if contract prices hold. | [3] Memory/HBM | 07-09 card; ASP = the KPI to watch |
| 3 | **AMD** | Prime **rotation destination** off NVDA — FINRA short-cover (z−2.01) confirms flow, cheaper accelerator alt. | [5] GPU/Accel | FINRA 07-09, freshest confirming signal |
| 4 | **CRDO** | Below-radar AI-networking (AEC copper); interconnect multiplies per-GPU; 69 news mentions yet off top300 sheet. | [7] Networking | Below-radar leak; FINRA neutral (z−0.04) |
| 5 | **NVDA** | Rotation-not-rupture; ~16–18x (below S&P) with rising estimates, short-vol normalized despite −16% — reset not deterioration. | [5] GPU/Accel | 07-09 card; COT 1%ile crowded-short = rebound ammo |
| 6 | **MRVL** | Custom-silicon + electro-optics #2; hyperscaler-concentration risk cuts both ways vs AVGO. | [6] Custom Si / [7] optics | 10-K Item 1A concentration flag |
| 7 | **AMKR** | CoWoS/advanced-packaging bottleneck proxy; **contra-narrative short-surge (z+1.50)** = squeeze setup if capacity confirms. | [4] Packaging | FINRA 07-09 tension; highest-risk |
| 8 | **COHR** | Optical/networking short-cover (z−1.80) — quiet positive divergence vs narrative. | [7] Optical | FINRA 07-09 |
| 9 | **ALAB** | PCIe/CXL connectivity fabric; below-radar node-7 alpha (44 mentions). | [7] Connectivity | Below-radar |
| 10 | **SNDK** | NAND leg of M-10 (+489% YTD then −30%); high-beta memory re-rate expression. | [3] Memory | 07-09 card; volatile |

Watch-only cross-sector: **VRT** (IT→INDU power/thermal), **CEG/VST/GEV** (IT→UTIL power) — physical enablers of M-07.

---
*Sources: [FRED] Phase-0 macro; [SEC] 10-K Item 1/1A/7 via module_business_us; [news] search_news_alert.py + insight_corpus daily cards; [FINRA] us_flow.py Reg SHO 2026-07-09; [yfinance] us_top300.csv + sector/mcap. ARM files 20-F (no 10-K). TSM outside US universe (external foundry dependency).*
