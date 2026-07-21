# SECTOR DEEP — Information Technology / Semiconductors (US)
**Date:** 2026-07-12 · **Desk:** US industry deep-sector analyst · **Scope:** IT (semis, memory, ASIC, packaging, equipment, networking) · **Method:** INDUSTRY_ANALYSIS_US.md §4 Phase 2 · **Calls:** ZERO buy/sell (analysis only; sizing is Phase 3)

Sources labeled inline: `[SEC]` EDGAR filings · `[news]` news_alert.db foreign pool · `[FINRA]` Reg SHO daily short-vol · `[WebSearch]` web · `[macro]` today's MACRO_REPORT. Blanks are stated as blanks.

---

## 0. One-paragraph thesis anchor (from MACRO M-07 / M-02)
Value is **physically migrating down the compute stack** — from GPU/hyperscaler buyers (whose FCF is compressing) to the component sellers that hold the pricing pen: **memory (DRAM/HBM), custom-silicon ASIC, advanced packaging, and power/interconnect** `[macro M-07]`. The sector's binding constraints are NOT demand (demand is abundant) but **supply chokepoints**: HBM/advanced-packaging capacity, leading-edge wafer allocation, and ASIC design+packaging slots. "Chipflation." Below Nvidia, a genuine **challenger compute layer** is now investable (custom ASIC via AVGO/MRVL, plus DeepSeek/Etched in-house silicon) `[macro]`. Two tail risks bracket the thesis: (a) AI-trade concentration wobble (Mag7 shed $2.3T in June) and (b) hawkish-Warsh Fed / real-10y 2.31% de-rating high-multiple names `[macro M-08/M-01]`.

---

## 1. FLOW — where the sector is heading

### 1a. News velocity (foreign pool, 14–60d) `[news]`
- **Memory is the loudest node.** "HBM + memory" = **103 foreign matches / 14d**. Dominant threads: MU raised guidance on surging memory prices; MU/SNDK +200% in 3 months; SK Hynix Nasdaq ADR listing (SKHL/SKUU/SKDD launching ~Jul 10–13); **Apple negotiating with (blacklisted) Chinese memory makers "not about lower prices — about surviving an AI-driven supply crunch"**; Samsung mass-producing storage for Nvidia's Vera Rubin. Two-sided tape: Michael Burry disclosed a short vs NVDA/MU/AMD, and MU had a sharp intraday crash mid-window — i.e. **crowded long meeting fresh shorts**, not a clean uptrend.
- **Custom ASIC is the second node.** "ASIC + custom" = 141 matches. Anchor event: **Apple extending Broadcom chip supply partnership through 2031 (~$30B, 15B+ ASIC chips + US packaging)** `[news, Mon 6 Jul]`. But the same window carries a divergence: **Marvell −22.6% after NVIDIA's $2B AI bet and an index exit** `[news]` — the ASIC #2 got repriced even as the theme ran ("Better Custom ASIC Stock: Marvell vs. Broadcom").
- **Packaging is the thin/under-covered node** (only 7 matches for "packaging+CoWoS") but structurally pivotal: **Mizuho lifted TSMC CoWoS capacity forecasts**; TSMC targeting 2029 panel-level CoPoS; Nova WMC expanding across advanced-packaging processes `[news]`. Low headline count ≠ low importance — this is the physical bottleneck (see §4/§5).
- **Challenger silicon / diversification below Nvidia:** DeepSeek developing an in-house AI chip (NVDA −2.2% on the report); "Nvidia is a victim of the compute marketplace it created"; OpenAI efficiency gains hammered SOX −5% one session `[news]`. Connectivity/optical sub-theme rising: **Credo (CRDO)** and **Astera Labs (ALAB)** each appear repeatedly (initiations, "AI connectivity winner," "$3,000-per-GPU memory arbitrage").

### 1b. Short-pressure overlay (FINRA Reg SHO daily, 2026-07-10) `[FINRA]`
| Ticker | Short% | Base20 | Z | 5v5 trend | Read |
|---|---|---|---|---|---|
| **AVGO** | 55.0% | 40.8% | **+2.15** 🔴 | +8.4▲ | **Short-vol SPIKE diverging from the bullish Apple-2031/ASIC narrative** — fresh sellers leaning into strength. Watch. |
| **VRT** (power/thermal) | 64.0% | 52.1% | **+1.52** 🔴 | +11.6▲ | Short-vol spike into the data-center-power run — cross-sector caution flag. |
| MU | 32.7% | 40.5% | −1.05 | −9.2▼ | Short-vol **falling** = covering into the memory rip (constructive, not divergent). |
| ANET / ALAB / TER | 56–60% | ~52% | +0.4–0.8 | mixed | Elevated but within own base (structurally high-short-vol names). |
| NVDA / AMD / MRVL / ARM / QCOM / WDC / STX / SNDK / INTC | 29–55% | — | −1.1…+1.3 | mixed | 🟡 all within normal range — no divergent signal. |
| ASML / AMAT / LRCX / KLAC | 34–40% | ~38–42% | −0.9…+0.2 | ▼ | Equipment names' short-vol easing. |

**Two divergences to carry:** (1) **AVGO** z=+2.15 — the freshest bullish narrative (Apple $30B/2031) is being met by the most extreme short-vol in the group; a name where the tape and the story disagree. (2) **VRT** z=+1.52 — the power/thermal cross-sector proxy is drawing shorts even as capex narrative persists. `[FINRA]`

---

## 2. PLAYERS — who does what (SEC 10-K Item 1 / 1A anti-signal) `[SEC]`

- **MU — Micron** (10-K filed 2025-12-25 period FY-Aug'25). "Industry leader in memory and storage … DRAM, NAND, NOR." MD&A: **"AI-driven demand is accelerating and is outpacing industry supply"**; shifted DRAM supply to data-center/hyperscale with **emphasis on HBM**, mix now weighted to higher-growth segments `[SEC Item 7]`. **Anti-signal (Item 1A):** volatility in average selling prices; factors pressuring gross margin; **"realizing expected returns from capacity expansions"**; highly competitive/cyclical industry `[SEC Item 1A]`. → MU is the purest US expression of the memory-crunch pass-through; its own risk factor names the kill switch (capacity-add returns).
- **AVGO — Broadcom** (10-K 2025-12-18). "Global technology leader … semiconductor + infrastructure software (VMware, CA, Symantec)." Strategy = tech leadership + strategic M&A. **Anti-signal:** "highly cyclical semiconductor industry undergoing profound change due to AI"; **"significant reduction in demand or loss of one or more significant customers"**; **"winning business is an unpredictable process"**; **dependence on a limited number of contract manufacturers / critical-material suppliers** `[SEC Item 1A]`. → The custom-ASIC pricing layer (Apple, Google TPU heritage); customer-concentration + foundry/packaging dependence is the exposure.
- **MRVL — Marvell** (10-K 2026-03-11). "Fabless supplier of data-infrastructure semiconductors, data-center core to network edge; complex SoC, analog/mixed-signal/DSP." **Anti-signal:** **"dependence on a few customers for a significant portion of revenue, particularly as major customers comprise an increasing percentage"**; risk from AI's impact on its business model; **"cancellations, rescheduling or deferrals of significant customer orders"** `[SEC Item 1A]`. → ASIC #2; customer concentration is exactly the vector that repriced it −22.6% this window `[news]`.
- **NVDA — Nvidia** (10-K 2026-02-25). "Data-center-scale AI infrastructure company … CUDA + full-stack." FY26 revenue driven by data-center compute+networking; **Blackwell = majority of DC revenue**. Outlook explicitly names a **physical constraint: "availability of data centers, energy, and capital … any shortage could impact future revenue; expanding energy capacity is a complex, multi-year process"** `[SEC Item 7]` — Nvidia itself points down-stack to power. **Anti-signal:** **"long manufacturing lead times and uncertain supply and capacity availability"**; **dependency on third-party suppliers to manufacture/assemble/test/package** (i.e. TSMC + CoWoS) `[SEC Item 1A]`. → The compute buyer whose own filing localizes value at packaging + power.
- **AMD** (10-K 2026-02-04). Challenger accelerator/CPU; MD&A frames 2025-vs-2024 DC growth `[SEC Item 7]`. Thematic role reinforced by news (self-driving customer win) `[news]`. Business-primary text did not parse cleanly this pass (blank) — flagged, not fabricated.
- **ARM** — files 20-F (foreign private issuer); no 10-K in EDGAR, module returned no body `[SEC blank]`. Role = IP/instruction-set layer (leftmost node); qualitative only this pass.

---

## 3. IR / filings (latest, 90d) `[SEC]`
- **AVGO** 8-K 2026-06-03 (Item 2.02 earnings). No **new order/M&A 8-K** in the 90-day window — the Apple $30B/2031 extension surfaced via **news, Mon 6 Jul** `[news]`, not a standalone contract 8-K (verify order economics before treating as filed).
- **MU** 8-K x2 (Item 2.02 earnings + Item 5.02 mgmt change). No order/contract 8-K in window `[SEC]`. Guidance raise on memory prices is via earnings + news `[news]`.
- Insider/Form-4 flow heavy on both (MU 16, AVGO 17) — normal for post-run names; not a directional signal here.

---

## 4. VALUE-CHAIN DENSITY MAP (left → right dependency; event labels = VERBS) `[news][SEC]`
Built manually — `module_industry_map` returns empty (tool regression) `[macro note]`.

```
[EDA/IP]        [Leading-edge      [Memory / HBM]     [Custom ASIC       [Advanced          [GPU/Accel]     [Networking/       [Hyperscaler/
 SNPS CDNS       foundry+wafer]      MU  (SNDK/WDC/     design]            packaging/CoWoS]    NVDA  AMD       interconnect]      System]
 ARM(IP)         ASML AMAT LRCX      STX = NAND/HDD)    AVGO  MRVL          (TSMC ext) ·        (Blackwell/    ANET  MRVL  CRDO    DELL HPE  +
                 KLAC TER Q          ARM-IP inside       ALAB(fabric)       ONTO FORM NVMI      Rubin)         ALAB  COHR LITE     hyperscalers
                 (metrology/test)                        (verify/test)      MPWR(power-IC)                     CIEN  QCOM
```

**Node-by-node, every candidate mapped:**
1. **EDA / IP (leftmost):** SNPS, CDNS (design tools); ARM (instruction-set IP embedded in nearly every accelerator/ASIC). *Verb: licenses, enables.*
2. **Leading-edge foundry + wafer equipment:** ASML (EUV litho — single-source chokepoint), AMAT, LRCX (deposition/etch), KLAC (process control), TER (test), Q/Qorvo-adjacent. *Verb: allocates wafer, expands capacity.* Short-vol easing here `[FINRA]`.
3. **Memory / HBM:** **MU** (DRAM/HBM — the pass-through node), SNDK + WDC + STX (NAND/HDD storage, Vera-Rubin storage demand). *Verb: raises contract price, shifts supply to HBM.* `[SEC MU MD&A]`
4. **Custom ASIC design:** **AVGO** (Apple $30B/2031, Google-TPU heritage), **MRVL** (#2, repriced −22.6%), **ALAB** (connectivity fabric adjacent). *Verb: wins socket, captures pricing pen.* `[news]`
5. **Advanced packaging (CoWoS / panel-level):** TSMC (foreign, off-list) is the physical chokepoint; US-listed exposure = **ONTO, FORM, NVMI, Nova** (packaging metrology/probe/inspection), plus AVGO's committed **US packaging**. *Verb: constrains throughput, adds capacity slowly.* `[news]`
6. **GPU / accelerator:** NVDA (Blackwell = majority DC rev), AMD (challenger + self-driving win). *Verb: buys the stack, compresses own FCF.* `[SEC][news]`
7. **Networking / interconnect / optical:** ANET, MRVL, **CRDO** (SerDes/AECs — "$3k-per-GPU arbitrage"), **ALAB**, COHR, LITE, CIEN, QCOM. *Verb: connects GPUs, scales the AI factory.* `[news]`
8. **Hyperscaler / system:** DELL, HPE (AI servers) + Mag7 buyers. *Verb: integrates, deploys.*

**Cross-sector chains (marked):**
- **→ UTIL (power):** NVDA's own 10-K makes **energy capacity a binding multi-year constraint** `[SEC]`; **VRT** (power/thermal, z=+1.52 short spike `[FINRA]`), **MPWR** (power-management IC) are the electrical-margin capture points. The AI-compute thesis leaks into the power grid.
- **→ INDU (electrical/copper/EMS):** APH, GLW, TEL (components/connectors), CLS/JBL (EMS assembly). Physical build-out layer.

---

## 5. BOTTLENECK + KPI + ANTI-SIGNAL

### Binding constraint (name ONE — demand is NOT it)
**Advanced-packaging + HBM capacity is the single binding bottleneck.** Demand is abundant; the pen is held by whoever controls the **slow-to-add physical steps: HBM stacking + CoWoS/advanced packaging + leading-edge wafer allocation.** Corroboration: Mizuho *lifting* CoWoS forecasts (capacity is the swing variable), MU MD&A "demand outpacing supply," Apple begging (even blacklisted) memory makers "to survive the crunch," and NVDA's own filing pinning risk on "uncertain supply/capacity" + third-party packaging `[news][SEC]`. Secondary binding layer: **energy/power capacity** (NVDA-stated) → cross-sector to UTIL.

### KPI dashboard (current readings) `[news][macro]`
- **DRAM/HBM contract price:** elevated / rising; MU raised guidance explicitly on surging memory prices `[news]`. HBM wafer+packaging capacity slow to add `[macro M-02]`.
- **CoWoS capacity:** forecasts revised **up** (Mizuho); panel-level CoPoS not until ~2029 → near-term capacity stays tight `[news]`.
- **Hyperscaler capex:** persists but buyer FCF compressing (value migrating down-stack) `[macro M-07]`; watch for an **air-pocket** print.
- **Semis weight in S&P 500:** record **19.7%** — concentration is itself a risk metric `[news]`.
- **Memory US-fab build:** Micron $250B US (→40% domestic DRAM); SK Hynix $29B US listing `[macro M-02]`.

### What KILLS the thesis (anti-signals to monitor)
1. **Capacity-add wave** — the exact risk MU names ("realizing expected returns from capacity expansions") `[SEC]`; a memory/packaging supply flush collapses the pass-through pricing.
2. **Hyperscaler capex air-pocket** — buyer FCF already compressing; a capex pause starves the whole right side of the chain `[macro]`.
3. **In-house silicon breaks pass-through** — DeepSeek/Etched/OpenAI-efficiency reduce merchant-GPU pull (NVDA −2.2% on DeepSeek; SOX −5% on OpenAI efficiency) `[news]`. Cuts both ways: bearish NVDA, but *bullish the ASIC/packaging node* that in-house chips still need.
4. **High-multiple de-rate under hawkish Warsh Fed** (real-10y 2.31%) — hits the richest names (NVDA, ANET, ALAB, CRDO) hardest `[macro M-01]`.
5. **Tape/story divergence** — **AVGO z=+2.15** and **VRT z=+1.52** short-vol spikes say fresh money is fading the two freshest bull narratives `[FINRA]`.

---

## 6. SUMMARY (3 lines → Phase 3 handoff)
1. **Binding bottleneck:** advanced-packaging (CoWoS) + HBM capacity — the physically slow-to-add steps that let memory (MU) and custom-ASIC (AVGO/MRVL) capture the price the compute buyers can't; energy/power (VRT, per NVDA's own filing) is the cross-sector second constraint.
2. **Freshest name to carry:** **AVGO** — the newest hard catalyst (Apple $30B / 15B-chip / US-packaging deal through 2031, surfaced 6 Jul) sits at the ASIC pricing node, BUT its FINRA short-vol just spiked to z=+2.15 (tape disagreeing with the story) — the highest-signal name to resolve in Phase 3.
3. **Runner-up fresh names:** **MU** (memory pass-through, short-vol covering = constructive) and the under-covered connectivity/packaging alpha (**CRDO, ALAB, ONTO/FORM/NVMI**) that sit in the chain layers the headlines under-weight.

*File: `llm_outputs/2026-07-12/industry_US/SECTOR_DEEP_IT.md`*
