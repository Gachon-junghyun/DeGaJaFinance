# SECTOR DEEP — Information Technology / Semiconductors (US) · DELTA

**Date:** 2026-07-13 · **Desk:** US industry deep-sector analyst · **Track:** CONTINUOUS (deep-dived 2026-07-12) · **Method:** delta over prior file, structure carried by reference · **Calls:** ZERO buy/sell (analysis only)

**Prior full map:** `llm_outputs/2026-07-12/industry_US/SECTOR_DEEP_IT.md` — value-chain nodes, player roster (56 IT names in top300), and node-by-node mapping are **UNCHANGED and carried by reference.** This file spends budget only on **what moved.**

Sources: `[FINRA]` Reg SHO daily · `[flow]` sector_flow sweep asof 07-10 · `[WebSearch]` fresh web 07-13 · `[macro]` today's MACRO · `[SEC]` EDGAR. Blanks stated as blanks.

---

## 0. DELTA HEADLINE — the thesis got CONFIRMED with hard numbers, not revised

The M-02/M-10 spine (**value migrates DOWN the stack: memory + custom-ASIC + semicap capture UP on a physical shortage; GPU-premium erodes**) is **the same thesis, now quantitatively corroborated** by three fresh 07-13 datapoints that were qualitative yesterday:

1. **Custom-ASIC out-grows the GPU it feeds:** Bloomberg Intelligence forecasts **27% CAGR for custom ASICs through 2033 vs 16% for merchant AI accelerators** `[WebSearch]`. AVGO guided **Q3 AI-semi revenue to $16.0B, +200% YoY** `[WebSearch]`. The value-capture migration is now a numbered spread (27 > 16), not a narrative.
2. **NVDA is the "black sheep" of its own rally:** Nvidia is **up just ~3.2% YTD** while money floods everything else in the chip complex `[WebSearch]`. The GPU-premium fade (UW leg of the thesis) is confirmed by relative-performance, not just the DeepSeek/Etched headlines.
3. **Memory shortage is structural + sold-out, not cyclical:** **DRAM +50–55% QoQ**, suppliers guiding **+10–20%/month through end-2026**; **HBM effectively sold out for 2026** under multi-year contracts; HBM revenue/wafer **3–5× DDR5**; tight into 2027–2028 `[WebSearch]`. "Chipflation" is now a dated, quantified price path — and it is exactly the **AI-capex→inflation channel** the macro flags (CIBC ~0.4pp) `[macro]`.

**Net:** no structural rewrite. The delta is that the bull spine hardened into numbers, while **two NEW frictions appeared** (a memory antitrust suit, §3; and the reflexive capex→inflation→de-rate loop, §1).

---

## 1. MACRO OVERLAY — the reflexive twist (NEW today)

- **AI-capex is now itself an inflation channel** (~0.4pp to 2026 inflation) `[macro]`. This creates a **reflexive de-rate loop unique to this sector:** the memory/ASIC buildout that IS the bull thesis feeds the CPI print → feeds the hawkish-Warsh rate path (real-10y 2.31% rising) → de-rates the high-multiple names the thesis is long. The sector is now partly short its own success. **CPI prints THIS WEEK** (headline ~4.2% / core ~2.8%) — the near-term swing variable is a macro print, not a chip datapoint.
- **Positioning cuts the other way:** **Nasdaq-100 COT is crowded-SHORT (4th %ile)** `[macro]`. The AI wobble is already priced bearish → this is **reflexive rebound ammo, not a top warning.** Combined with VIX 15.8 (calm), the setup is a coiled-short, not an exhausted-long.
- **Reconciliation:** these two macro forces bracket the sector — capex→inflation is the slow de-rate headwind (hits NVDA/ANET/CRDO multiples), crowded-short is the fast rebound tailwind. Neither changes the *relative* call (funded memory/ASIC layer OW vs GPU-premium fade); both raise index-level volatility around it.

---

## 2. FLOW — breadth is the story; the print itself is STALE

**⚠️ No new tape.** FINRA Reg SHO is the **same 2026-07-10 snapshot** as yesterday; the sector_flow sweep is **asof 07-10**; the news_alert pool tops out 07-08. **Bottom-up flow has NOT advanced since yesterday's deep** — do not re-read the same short-vol z-scores as fresh confirmation.

### 2a. The breadth split, made concrete `[flow]`
IT ranks **#2** but on a **mega-cap-narrow** signal: **wflow +0.159 vs eqflow −0.033**, only **9 green / 17 red**. Cap-weighted strength (a handful of trillion-$ names) masks a majority of red constituents. This is the tape-level proof of M-09/M-10 concentration: **the sector's "strength" is 5–6 names, not the sector.** Read directly onto the roster:
- **The green (cap-weighted lift):** the mega semis — NVDA/AVGO/MU-tier — carry wflow.
- **The red 17 (equal-weight drag):** the long tail — mid-cap semis, the software/app-software cluster (CRM/ADBE/NOW/DDOG/SHOP), hardware/EMS (DELL/HPE/JBL) — is being sold or ignored.
- **The LIVE 🟢 accel IT names are PANW + ANET (security / networking) — NOT the mega semis** `[flow]`. Another breadth tell: the *accelerating* money is in the **enterprise-networking/security layer**, distinct from the cap-weighted-semis layer. Two different IT trades are running under one label.

### 2b. FINRA short-vol — carried unchanged (07-10) `[FINRA]`
| Ticker | Z | Read (unchanged from 07-12) |
|---|---|---|
| **AVGO** | **+2.15** 🔴 | Short-vol SPIKE still diverging from the bullish Apple-$30B/ASIC story. **Tape/story divergence UNRESOLVED** — carry into any AVGO sizing. |
| MU | −1.05 | Short-vol falling = covering into the memory rip (constructive). |
| AMD | +1.28 🟡 | Elevated, within range. |
| ANET / PANW | +0.71 / −0.34 🟡 | Both normal-range; PANW short-vol easing (−10.5 trend) into its LIVE-accelerating status — mildly constructive for the breadth name. |
| NVDA / MRVL / LRCX / AMAT | −1.05…+0.87 | 🟡 all normal range, no divergence. |

---

## 3. IR / anti-signal DELTA — one NEW regulatory tail on the memory node

- **NEW anti-signal — DRAM price-fixing litigation:** Samsung, SK Hynix, and **Micron (MU)** were sued **June 25 (N.D. Cal.), 17 plaintiffs**, alleging coordinated supply restriction; complaint cites **~700% price rise over 4 years**; a July-08 TrendForce piece frames it as testing "whether HBM expansion can prove collusion" `[WebSearch]`. This is a **new overhang specific to the memory pass-through node** — the exact mechanism (reallocating capacity to HBM, curtailing commodity DRAM/DDR4) that drives MU's pricing is now the thing being litigated. Not a thesis-killer (demand/shortage is real), but a **legal/headline tail that did not exist in yesterday's map.** Adds to MU's own filed kill-switch ("realizing returns from capacity expansions").
- **AVGO IR quantified:** the Apple deal (surfaced via news, not an 8-K) now sits alongside a hard guide — **Q3 AI-semi rev $16.0B (+200% YoY)**, custom-ASIC clients now explicitly **Google, Meta, OpenAI, Anthropic** `[WebSearch]`. Street: Strong Buy 48/50, median PT $458 (~37% over $400) — noted as context, NOT a call.
- **MU 10-K (FY-Aug'25, filed 2025-10-03)** re-pulled: "AI-driven demand … outpacing industry supply," DRAM mix shifted to HBM/data-center `[SEC]`. Unchanged from yesterday. **Caveat carried:** MU is only **~5–10% of HBM share** (SK Hynix 50–55%, Samsung 35–40%) `[WebSearch]` — the purest *US-listed* memory expression, but the smallest HBM incumbent; its beta is to DRAM contract price, not HBM allocation dominance.

---

## 4. VALUE-CHAIN MAP — carried by reference (no node change)

The 8-node left→right map (EDA/IP → foundry+equip → memory/HBM → custom-ASIC → advanced-packaging/CoWoS → GPU → networking/interconnect → hyperscaler) and every mapped name are **UNCHANGED** — see prior file §4. Cross-sector chains **→ UTIL (power: VRT, MPWR; NVDA's own filing pins energy as binding)** and **→ INDU (APH/GLW/TEL; CLS/JBL)** also unchanged.

**Only delta to the map's *emphasis*:** the flow sweep says the **networking/interconnect node (ANET, + security-adjacent PANW) is where LIVE money is accelerating** — that node moves from "carried" to "actively bid" this session. The custom-ASIC node's value-capture lead is now quantified (27% vs 16% CAGR).

---

## 5. BOTTLENECK / KPI / ANTI-SIGNAL — deltas only

- **Binding constraint — UNCHANGED:** advanced-packaging (CoWoS) + HBM capacity; energy/power second. Fresh corroboration: **HBM sold out 2026, DRAM +50–55% QoQ, tight into 2027–2028** `[WebSearch]` = the physical-rigidity of supply is now dated and quantified.
- **KPI dashboard — moved readings:**
  - DRAM contract price: **+50–55% QoQ, +10–20%/mo guided through end-2026** (was "elevated/rising") — sharply up.
  - HBM allocation: **sold out 2026, multi-year locked** (was "slow to add") — confirmed binding.
  - Custom-ASIC growth: **27% CAGR '33 vs 16% accelerators; AVGO Q3 AI $16B +200%** (NEW quantification).
  - NVDA relative: **+3.2% YTD, sector laggard** (NEW — the GPU-premium-fade KPI).
  - Breadth: **9 green / 17 red, wflow +0.159 vs eqflow −0.033** (NEW breadth KPI to track — narrowing = late-stage concentration).
- **What KILLS each layer (delta):**
  - **NEW kill-vector on memory:** antitrust remedy / price-fixing judgment forcing supply normalization (§3) — cuts the pass-through pricing pen legally rather than by oversupply.
  - **NEW kill-vector on the whole sector:** a **hot CPI print this week** → hawkish-Warsh confirmation → high-multiple de-rate (the reflexive capex→inflation loop, §1). Hits NVDA/ANET/CRDO/ALAB multiples hardest.
  - Unchanged: memory capacity-add flush; hyperscaler capex air-pocket; a **Nvidia blowout re-widening the GPU moat** (would invalidate the "value migrates down-stack" UW leg — watch NVDA next print as the single cleanest anti-signal to the whole thesis).

---

## 6. SUMMARY → BET SHEET HANDOFF

1. **Delta:** thesis unchanged but **hardened into numbers** (ASIC 27% > accelerator 16% CAGR; DRAM +50–55% QoQ, HBM sold out; NVDA +3.2% YTD "black sheep"), while two NEW frictions appeared — a **memory price-fixing suit** (MU node) and the **reflexive AI-capex→CPI→de-rate loop** (CPI prints this week). Flow is **stale (07-10) and mega-cap-NARROW** (9 green/17 red); the LIVE-accelerating names are **PANW/ANET**, not the mega semis.
2. **Cleanest OW layer = CUSTOM-ASIC / semicap** — it now has the quantified value-capture lead (27>16 CAGR, $16B/+200% AVGO guide) AND is the layer in-house silicon (DeepSeek/OpenAI/Anthropic) still must buy. Memory (MU) is the runner-up funded layer but now carries the litigation tail + smallest-HBM-share caveat.
3. **Top names for the bet sheet:**
   - **AVGO** — custom-ASIC pricing node; Q3 AI $16B (+200%), 27% ASIC CAGR, Apple $30B/2031, clients Google/Meta/OpenAI/Anthropic. **Caveat unresolved: FINRA short-vol z=+2.15 (tape fading the story) — size against that divergence.**
   - **MU** — purest US memory pass-through; DRAM +50–55% QoQ, short-vol covering (constructive). **New tail: price-fixing suit; only ~5–10% HBM share.**
   - **ANET (+ PANW watch)** — the LIVE 🟢 accel breadth names (networking/security); the actual *accelerating* layer per the flow sweep, and a **breadth hedge** against the mega-cap-narrow concentration that defines the sector's "strength."

*File: `llm_outputs/2026-07-13/industry_US/SECTOR_DEEP_IT.md` · continuous-track delta over 2026-07-12*
