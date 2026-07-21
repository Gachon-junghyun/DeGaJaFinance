# SECTOR DEEP — UTIL (Utilities / AI-Power & Data-Center Infrastructure)

**Desk:** US Industry — DEEP sector analyst
**Date:** 2026-07-12
**Scope:** AI-funded electricity load → IPP/utility offtake → firm-power delivery. One pass, SEC-anchored.
**Cross-chain out of scope (belongs to INDU deep):** electrical equipment GEV / ETN / VRT; copper/transformers → MATR.

---

## 0. THESIS HINGE (one line)

The AI-power trade has split into two confirmed regimes: **funded/deliverable firm power** (nuclear + gas IPPs with signed, IG-counterparty, multi-GW PPAs — some already *operating*) is a real underwritten cash-flow story; **pre-revenue optionality** (SMR/fusion/early geothermal) is a de-rating duration bet. The binding question `[daily-US][MACRO]`: even for the funded names, is the multiple still set by the Fed (real-10y 2.31%, hawkish Warsh, this-week CPI) rather than by the offtake? The anti-signal below says **partly yes**.

---

## 1. FLOW — short-pressure overlay + foreign news velocity

### 1.1 FINRA Reg SHO daily short-vol (2026-07-10) `[FINRA]`
`python -X utf8 scripts/us_flow.py VST CEG NEE TLN OKLO SMR RUN BE NNE`

| Ticker | Short% | Base20 | z | 5v5 trend | Read |
|---|---|---|---|---|---|
| **VST** | 27.8% | 42.8% | **−2.27** | −1.3 ▼ | 🟢 short cover / pressure exit |
| **CEG** | 34.4% | 49.7% | **−1.92** | −10.4 ▼ | 🟢 short cover / pressure exit |
| NEE | 55.4% | 46.1% | +0.91 | +3.5 ▲ | 🟡 normal |
| **TLN** | 77.2% | 55.3% | **+2.14** | +15.9 ▲ | 🔴 short spike (extreme vs own base) |
| OKLO | 55.5% | 49.4% | +1.04 | +0.7 ▲ | 🟡 normal |
| **SMR** | 47.4% | 35.7% | **+3.56** | +1.0 ▲ | 🔴 short spike (extreme) |
| RUN | 48.1% | 52.9% | −0.51 | +3.8 ▲ | 🟡 normal |
| BE | 27.1% | 44.7% | −1.37 | +0.6 ▲ | 🟡 normal (mild cover) |
| **NNE** | 65.2% | 51.3% | +1.56 | +8.1 ▲ | 🔴 short spike |

**Narrative-vs-tape divergences flagged:**
- **VST / CEG 🟢 (z ≤ −1.9)** — shorts covering *into* the funded-offtake narrative. Tape CONFIRMS the funded-IPP bull d/d. Cleanest alignment of flow + fundamentals in the sector.
- **TLN 🔴 (z +2.14, trend +15.9)** — short pressure *spiking* despite a genuine AWS 1,920 MW deal. **Divergence:** either shorts are pressing the pending-acquisition execution/leverage risk (Cornerstone, Freedom/Guernsey integration), or hedging around the co-location/ISA regulatory tail. Flow does NOT confirm TLN as cleanly as VST/CEG. `[FINRA]`
- **SMR z +3.56 / NNE z +1.56 🔴** — short spikes CONFIRM the pre-revenue SMR bear (F44) d/d; tape agrees with "value-trap." OKLO 🟡 only (already deeply de-rated: −27% H1 / −71% from 2025 highs `[MACRO]`, so less fresh short fuel).
- **RUN 🟡** — short-vol *normal* even after the +26–30% VPP pop; the Tesla/Renew Home 16 GW VPP move was a price event, not (yet) a short-squeeze structure. `[news]`

### 1.2 Foreign news velocity (14–30d) `[news]`
`scripts/search_news_alert.py --field any --scope foreign` (OR-mode; fuzzy semantic matches, treat counts as directional not exact)
- "Constellation" 136 hits, "data center power" 59, "Vistra" 19, "geothermal" 15 → power-demand theme is **high-velocity and broadening**, not fading.
- Confirmed live catalysts in the tape: *"Sunrun Surges 26% on 16-Gigawatt Virtual Power Plant Deal With Tesla and Renew Home"*; *"Bloom Energy (BE) Faces Fresh AI Data Center Power Competition From Gas And Nuclear"* (BE competitive-pressure headline = margin risk); *"Fervo Energy: Nvidia Can't Fix What's Missing Here"* (geothermal bull questioned); *"$17.5B US gov nuclear loans"*; Arizton — US hyperscale DC investment >$697B by 2031 / +12,144 MW by 2029.
- Bearish/valuation counter-tape: *"Vistra: A Solid Utility Story With Limited Margin For Error"*; *"CEG Seen as High-Quality Power Demand Play, but Goldman Flags Valuation"*; *"The AI Boom Could Be a Bad Reason to Buy Utility Stocks."* → the **duration/multiple** worry is explicitly in the foreign coverage.

---

## 2. PLAYERS — FUNDED/deliverable vs PROMISED/pre-revenue

Source: `module_business_us <T> --full --json` — SEC 10-K Item 1 / 1A / 7. English only. FY2025 filings (filed Feb 2026).

### 2.1 FUNDED — contracted MW with IG counterparties `[SEC]`

**VST — Vistra Corp.** (10-K 2026-02-27, FY2025) — *integrated retail + generation, ~44,000 MW fleet (gas/nuclear/coal/solar/storage), ~5M retail customers, 18 states.*
- **Sep 2025:** 20-yr PPA (+20-yr extension option) with **AWS** — **1,200 MW carbon-free from Comanche Peak Nuclear**; capacity building toward 2032.
- **Jan 2026:** 20-yr PPAs with **Meta** — **2,609 MW carbon-free from PJM nuclear plants, of which 2,176 MW ALREADY OPERATING.** ← *delivered MW, not just signed.*
- Integrated model = wholesale generation self-supplies retail load → structurally cash-generative *before* the AI offtake. MD&A: large-load offtake "underwrite[s] higher base profitability."
- FERC co-location rules noted as "remov[ing] regulatory uncertainty for co-location arrangements" → a tail risk retiring, not opening. `[SEC]`
- Overlay `[MACRO]`: Helix/KKR–Nvidia $10B mandate; Wells Fargo PT $259.

**CEG — Constellation Energy** (10-K 2026-02-24, FY2025) — *largest US nuclear operator; **55 GW post-Calpine**.*
- **Sep 2024:** 20-yr PPA with **Microsoft** — Three Mile Island Unit 1 restart ("Crane Clean Energy Center," ~835 MW), restart in progress.
- **Jun 2025:** 20-yr PPA with **Meta** — full output of **Clinton Clean Energy Center**.
- **Jan 7, 2026:** closed **Calpine acquisition — +~23 GW across 72 gas + geothermal + storage assets** (nation's largest gas & geothermal generator; TX/CA/NE footprint). Adds *dispatchable firm* to a nuclear base.
- Overlay `[MACRO]`: added **Walmart 20-yr** deal on top of Meta; **P/E compressed 50x → 21x even as offtake landed** — see §5 anti-signal.

**TLN — Talen Energy** (10-K 2026-02-26, FY2025) — *IPP, 13.1 GW; 2.2 GW nuclear (Susquehanna 2.5 GW, 90% interest, 17 TWh @ ~$27/MWh all-in).*
- **Jun 2025:** *expanded* PPA with **AWS** — fixed-price supply of **up to 1,920 MW annually from Susquehanna to the ADJACENT AWS data-center campus through 2042** (behind-the-meter / co-located). Susquehanna **ISA Amendment** (FERC co-location dispute) resolved `[SEC]`.
- Fleet build-out: **Freedom + Guernsey +2.8 GW** H-class combined-cycle gas (acquired); **Cornerstone Acquisition pending** — Lawrenceburg + Waterford **+2.0 GW gas** (IN/OH). "Large-load contracting strategy" backstopped by gas.
- Read: real, largest single behind-the-meter nuclear-to-hyperscaler deal — **but** FINRA short spike (§1.1) + pending-acquisition leverage/integration = execution overhang.

**NEE — NextEra** (candidate; not deep-pulled this pass) — regulated utility + world's largest renewables/storage developer; FINRA 🟡 neutral, z +0.91. Belongs to the *rate-sensitive regulated* bucket (duration-heavy), not the merchant-offtake bucket. Carry as watch, not lead.

### 2.2 PROMISED / pre-revenue — signed deals, no (or minimal) delivered MW
- **OKLO (Oklo)** — SMR/fast-reactor, pre-revenue. −27% H1 / −71% from 2025 highs `[MACRO]`. FINRA 🟡 (already crushed). Signed interest ≠ delivered MW.
- **SMR (NuScale)** — "value-trap <$10" `[MACRO]`; **FINRA short spike z +3.56** = tape confirms pre-rev bear. GEV: "not a golden buying opportunity yet."
- **NNE (NANO Nuclear)** — early-stage; **short spike z +1.56**. Pre-revenue.
- **BE (Bloom Energy)** — fuel cells; +1,410% cited in tape but *"Faces Fresh AI Data Center Power Competition From Gas And Nuclear"* `[news]` = competitive-margin anti-signal. FINRA mild cover 🟡.
- **RUN (Sunrun)** — Tesla + Renew Home **16 GW VPP** distributed solar+storage; +26–30% pop `[news]`. Semi-funded (distributed, aggregated), NOT firm baseload for hyperscaler co-location. FINRA 🟡.
- **Geothermal / fusion (next-gen firm entering public markets)** `[MACRO][news]` — Fervo–Nvidia EGS-Twin partnership (private; *"Nvidia Can't Fix What's Missing Here"*); Ormat (ORA) *"better business, not a better buy"*; a 20-yr fusion bet closing its SPAC. All pre-revenue optionality; **Calpine-inside-CEG is the only *funded* geothermal exposure** on public markets today.

---

## 3. VALUE-CHAIN DENSITY MAP (built manually — `module_industry_map` returns empty `[tool-gap]`)

```
 FUEL / INPUT            GENERATION (firm vs optional)        GRID / INTERCONNECT        BEHIND-THE-METER PPA        HYPERSCALER LOAD
 ───────────            ──────────────────────────────       ───────────────────       ───────────────────         ─────────────────
 Nat-gas supply    →    Nuclear IPP:  CEG, VST, TLN      →   PJM / ERCOT / ISO-NE   →   Co-location / 20-yr PPA  →  AWS   (VST 1.2GW, TLN 1.92GW)
 (Permian assoc.)       Gas (firm):   CEG/Calpine,           interconnect QUEUE          IG-counterparty offtake     Meta  (VST 2.6GW*, CEG Clinton)
                        TLN Freedom/Guernsey/Cornerstone     = THE BOTTLENECK                                        Microsoft (CEG TMI 0.83GW)
                        Geothermal:   CEG/Calpine (funded),   DOE PJM emergency order                                Walmart (CEG)
                        Fervo/ORA (pre-rev)                   FERC co-location rules /                               *2,176MW already operating
                        Solar+storage/VPP: RUN+Tesla 16GW     Susquehanna ISA amend.
                        SMR-option:   OKLO/SMR/NNE (pre-rev)
                        Fuel cell:    BE (competition risk)
```
**Cross-chains (out of this deep):** Generation ↔ **electrical equipment GEV/ETN/VRT (INDU)** (turbines, switchgear, cooling) — GEV: SMR "not a golden buying opportunity yet." Grid ↔ **transformers/copper → MATR**. Heatwave (Europe 1,300 deaths, Germany 41.7°C) + **DOE emergency order on PJM** made grid constraint a *federal* matter `[MACRO]`.

---

## 4. BOTTLENECK · KPI · ANTI-SIGNAL

### 4.1 Binding constraint
**Interconnect-queue + deliverable/firm-MW availability — NOT signed-deal count.** Signed 20-yr PPAs are abundant; what is scarce is (a) MW that can actually flow now (VST's 2,176 MW *operating* Meta block is the scarce asset; a restart like CEG-TMI or a 2032 ramp is not), (b) FERC/PJM approval for co-location (Susquehanna ISA amendment was the live test — resolved for TLN), and (c) queue position. The heatwave + DOE emergency order raise the political premium on *firm, dispatchable, deliverable-now* capacity.

### 4.2 KPIs to track (Phase 3)
1. **Signed IG PPAs vs DELIVERED MW** — VST 2,176 MW operating (Meta) is the benchmark; watch CEG TMI restart date and VST/AWS 2032 ramp convert to online MW.
2. **VST / CEG forward P/E vs real-10y** — if multiple keeps compressing while offtake lands, it stays a duration story (see 4.3).
3. **FINRA short-vol z** — VST/CEG 🟢 cover vs TLN/SMR/NNE 🔴 spike; watch for TLN z to normalize (would clear the execution overhang) or SMR z to fall on a delivered-revenue print.
4. **FERC co-location / PJM queue rulings** — binary de-risk events.

### 4.3 ANTI-SIGNAL (what would break the funded-bull read)
- **PRIMARY, currently PARTLY TRIGGERED:** *offtake headlines keep landing while P/E keeps FALLING with rates.* **CEG P/E 50x → 21x even as Meta + Walmart + Calpine landed** `[MACRO]` → proves the multiple is still substantially a **duration/Fed** variable, not fully a de-risked cash-flow variable. This week's CPI + hawkish Warsh are the live governor. The funded-bull is real on *cash flow*; it is NOT yet insulated on *multiple*.
- **SECONDARY, NOT triggered (would flip pre-rev read):** an SMR name converting a *signed* deal into *delivered* revenue. No sign of it — SMR/NNE short spikes (z +3.56 / +1.56) say the market is pressing the opposite.
- **TLN-specific:** the 🔴 short spike against a genuine AWS deal — if it resolves *down* (shorts right), it flags co-location/leverage risk the narrative is ignoring.

---

## 5. SUMMARY (carry to Phase 3)

- **Binding bottleneck:** deliverable/firm-MW + interconnect-queue/FERC co-location approval — NOT signed-PPA count. The scarce, value-bearing asset is MW that flows *now* (VST's 2,176 MW operating Meta block), backed by the DOE-PJM emergency order and heatwave making firm dispatchable power a federal priority.
- **Single funded name with cleanest exposure:** **VST (Vistra)** — has *delivered/operating* nuclear MW (2,176 MW Meta live), integrated retail cash flow that pays before the AI offtake, dual IG counterparties (AWS 1.2 GW + Meta 2.6 GW), FERC co-location tail retiring, **plus** the only 🟢 short-cover flow (z −2.27) fully aligned with the fundamentals and the Helix/KKR–Nvidia $10B mandate. CEG is a close second on offtake quality but carries the visible P/E-compression (duration) scar; TLN has the biggest single behind-the-meter deal but a 🔴 short spike + pending-acquisition execution overhang.
- **Live governor / anti-signal:** the trade is de-risked on *cash flow* but still a *duration* story on *multiple* — CEG's 50x→21x compression while offtake landed is the proof. Watch this-week CPI + real-10y (2.31%). SMR/fusion/early-geothermal remain confirmed pre-revenue (short spikes); the only *funded* geothermal is Calpine-inside-CEG.

---
*Sources: `[SEC]` 10-K FY2025 (VST/CEG/TLN Item 1/1A/7), `[FINRA]` Reg SHO daily 2026-07-10 via us_flow.py, `[news]` news_alert foreign 14–30d, `[MACRO]` MACRO_REPORT 2026-07-12, `[daily-US]`. `module_industry_map` empty → value chain built manually. ZERO buy/sell calls.*
