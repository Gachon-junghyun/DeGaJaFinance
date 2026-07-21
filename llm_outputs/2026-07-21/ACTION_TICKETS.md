# ACTION_BRACKET — 2026-07-21  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 11,314,206원 · fx 1482 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** SCHW earnings (D-0, axis=earnings) — both-sides armed below.

### CORE-STARTER (tape-independent) — NVDA  (BUY)
- **condition:** establish NOW regardless of tape — closes AI-compute / semiconductors epicenter GAP (12.0% < 12.0%)
- **size:** 4 sh @ ~$203.28 (≈$813.12 notional, risk $61.08 = 0.8% )
- **stop:** $189.05 (−7.0%) · exch NASD
- **why core:** real-alpha REAL/not-priced, flow 🟡중립=non-chase entry, epicenter bottleneck, fwd PE 16.5 < AVGO 20.1

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (0.0% < 8.0%)
- **size:** 4 sh @ ~$208.8 (≈$835.2 notional, risk $61.08 = 0.8% )
- **stop:** $194.18 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---
---

# ★ ALPHA FRESHNESS GATE — appended 2026-07-21 (Stage 8 / L1·ALPHA), append-only
> Everything above this line is `action_bracket.py`'s deterministic output, **unedited**. Everything
> below is the ALPHA stage's freshness gate over it. The script reads the cycle registry verbatim;
> **two of its "why core" lines rest on numbers that have since changed sign, and one binary set it
> announced was never emitted.** Both are corrected here rather than silently accepted.

## 🚨 GATE 1 — the PSX ticket's stated rationale has REVERSED SIGN. **Ticket tagged 🔴 STALE-RATIONALE.**
The generated line reads: *"the only Energy name with **shorts actively exiting (FINRA short-vol
z −1.43, 5v5 −16.6▼)** = clean structural entry."*
**Measured 2026-07-20, independently, twice this run** (DEEP·ENRG §6 Q2 and PREMORTEM Lens 4):
```
PSX  short% 57.0%  base20 39.1%  z +2.01  5v5 −8.7▼   🔴 공매도급증(자기베이스대비 극단)
```
**z −1.43 → +2.01. The load-bearing premise of the ticket is now the opposite of what it says.**
- **What survives:** the valuation leg (**fwd PE 11.39, PEG 1.20** — cheapest large refiner,
  re-verified in `BET_SHEET.md` §1A) and the non-crack-segment business-mix leg. Both untouched.
- **What does not:** "clean structural entry" is no longer an accurate description of PSX's positioning.
- ⚠ **`core_pick` is a HUMAN-LOCKED registry field (`_note`: "Human-locked 2026-07-17"). This stage
  has no authority to change it and does not.** The ticket is **flagged, not rewritten** — a human
  must re-verify before it is treated as current.
- **ALPHA's own read, offered as an alternative and not substituted into the ticket:** by the measured
  tape the cleanest epicenter expression is **XOM** (OBV 매집, RS20 +8.3%, FINRA z **−0.77**, short
  **1.0% float covering, DTC 2.1**, and the only name in the refining complex with positive implied
  upside, **+13.2%** vs a median target, at **−15.9%** off its high). Three stages converged on XOM
  independently (EVENT_ALPHA CARD 1, PREMORTEM Lens 4, DEEP·ENRG §6 Q1).

## 🚨 GATE 2 — the NVDA ticket's flow line is stale too, and the GAP it closes is a rounding artifact
- The ticket says *"flow 🟡중립 = non-chase entry."* **Measured today: NVDA is 🔴분산 (distributing),
  RS20 −2.9%, RS60 −4.0%, vol 0.77×.** The "non-chase" description no longer matches the tape.
- **The GAP itself is −0.001pp** (epicenter 12.0% vs 12.0% required). PREMORTEM Lens 4 and SWEEP §3
  both triaged this as a **rounding artifact, effectively MET** — not comparable to the Energy hole's
  −8.00pp. **Treating it as an equal-severity 🚨 flattens a real finding.**
- ★ **The deeper problem the ticket cannot see: the book's 12.0% is the WRONG 12.0%.** All three held
  epicenter names are distributing (**AVGO RS20 −7.4%/RS60 −14.9% with no live narrative at all;
  TSM −12.3% on 1.24× volume — the steepest OBV distribution slope measured this run, −133%/20d;
  NVDA as above**), and **two of the three ride news threads that have ENDED.**
- **ALPHA verdict: 🟡 PARTIAL — the gap does not need closing; the QUALITY of the existing 12.0% is
  the real finding, and it belongs to the book desk, not to a new add.**

## 🚨 GATE 3 — the script announced both-sides brackets and emitted none
Line 7 reads *"**Nearest binary:** SCHW earnings (D-0) — **both-sides armed below**"* — **and no
bracket section follows.** The L1 requires the pre-mortem's both-sides brackets per binary to reach
this file. **Filed as a script defect and supplied manually below**, from `BLINDSPOT_PREMORTEM.md`
B1–B6. ⚠ **`--fx 1482` here vs `fx 1380` in `CYCLE_EXPOSURE.md` — the two script-owned artifacts
disagree on the same-day FX by 7.4%. Notional/size figures across the two files are not comparable.
Filed, not reconciled (both are script-owned).**

### Both-sides brackets — pre-committed conditionals (analysis→ticket; a human executes, never the desk)

| # | Binary | Date | **Branch A (with the desk)** | **Branch B (AGAINST the desk)** | Invalidation |
|---|---|---|---|---|---|
| **B1** ★ | **Iran 10-day ceasefire** | undated, **LIVE** | Rejected / Bab el-Mandeb enforced → ENRG OW holds; watch **DINO** (🟢가속, RS20 +40.8%, vol **1.29×**, short **5.2% float BUILDING, DTC 3.6** = squeeze fuel) | **Ceasefire lands** → crude gaps down; refiners **+25–31%/1m with vol <1.3× everywhere** give back; **XLE–XLY corr −0.63** means the DISC UW relieves simultaneously. **The $550B/−0.35% move on the mere proposal is the precedent** | An actual tanker turned away at Bab el-Mandeb (declared ≠ enforced) floors the leg even if Iran signs |
| **B2** | **SCHW earnings** | **07-21 (today)** | Beat **AND** NIM expansion guided despite a flat curve → first evidence FIN survives without the steepener | Miss / NIM guided down → XLF's **1.10× surge** (the board's only one) evaporates | ★ **Pre-commitment, binding: a clean print is NAME-LEVEL NOISE, not sector confirmation.** BMO cut SCHW to Market Perform on **07-20**, one session before |
| **B2b** ★ | **CB earnings** | ★ **07-22 (tomorrow)** | Beat → the **only** FIN sub-leg still alive is confirmed; CB is **🟢가속, OBV 매집, vol 1.20×, RS20 +9.6%** | Miss → the insurance relocation dies and **LATE MONEY becomes unqualified** | ⚠ **Found at the BET stage from `next_earnings_date`; NO upstream stage flagged it — the 3rd calendar gap this run** |
| **B3** | **TSLA / GOOGL** | 07-22 | Both miss and IT green-count stays **0/56** → IT UW confirmed, MU's reclaim books as relief beta | GOOGL beats with capex **rewarded on the capex line** → squeezes the triple-confirmed crowded short (COT 4%ile + record equity shorts + record hedge-fund tech selling) | GOOGL is 🔴분산, RS20 −3.7%, **FINRA z +1.45** going in |
| **B4** | **RTX / LMT** | 07-23 | Sub-1.3× volume → **P4 retired a 6th run**; RTX's accumulation rebooks as pre-earnings positioning | **>1.3× volume on an order/appropriations beat** → double-barrelled: earnings **plus** an unwind of **RTX z +1.64** and **GE 5v5 +14.6▲** | ★ **The revival bar stays >1.3×. It was NOT relaxed to fit an attractive setup** |
| **B5** | **INTC** | 07-23 | Breadth stays **0 green/56** → the de-rate holds | A foundry/AI-capex beat = the **2nd** falsifying observable in one week; **z −0.81 = no crowding to unwind, so a beat moves on fundamentals not squeeze** | KPI: SMH RS20 **> −8%** (now −14.7%) **AND** two of {MU,TSM,AVGO} flip OBV to 매집 (now **0 of 3**) |
| **B6** | **50% Canada tariff** | landed 07-20 | Canada retaliates → MATR UW deepens; **F's z +2.27** short build was right | Carve-out/negotiated down (**this administration's pattern**) → **F squeezes**, and **UNP/CSX (매집, RS20 +15.9%/+10.4%, vol >1.0×) accumulating INTO the tariff** prove early, not wrong | No formal Canadian counter-tariff has landed — only a premier's statement |

## Freshness tags on the tickets above (🟢LIVE / 🟡PARTIAL / 🔴RESOLVED)
| Ticket | Tag | Evidence label + date |
|---|---|---|
| **PSX core-starter** | 🔴 **STALE-RATIONALE** *(not dropped — the GAP is real; the stated REASON is dead)* | FINRA z −1.43 → **+2.01**, 07-20 · crack-detachment **Day 2 fired** (90.34→88.22→85.31, 07-16/17/20) |
| **NVDA core-starter** | 🟡 **PARTIAL** | GAP is **−0.001pp** (artifact) · flow line stale: 🟡중립 → **🔴분산**, 07-20 |
| **B1 ENRG (Bab el-Mandeb leg)** | 🟢 **LIVE** | ★ `theme-age "Bab el-Mandeb"` = **🟡ACCELERATING, 188.57× acceleration, 61 hits** — *the largest acceleration measured anywhere in this run* |
| B1 ENRG (crack leg) | 🟡 **PARTIAL** | `refining margin` 🟡ACCEL **4.76×**, `crack spread` 🟡ACCEL **12.86×** — **attention up while the actual crack fell 2 sessions.** Residual: the mechanism, not the margin |
| B1 ceasefire (the anti-branch) | ⚪ **ECHO** | `theme-age "ceasefire"` = ⚪**ECHO**, ≥90d, **31.4% share, only 1.87× accel, 1,762 hits** — loud but consumed. ⚠ **ECHO ≠ resolved: the binary is live and undated; an ECHO theme simply needs stronger live evidence to move a tilt** |
| **B2b CB (insurance leg)** | 🟡 **PARTIAL** | Flow 🟢가속/매집 vol 1.20× **but** `theme-age "insurance earnings"` = 🔴**FADING, 0.0× accel, ONE hit in 28 days.** ★ **A flow-only leg with essentially zero news denominator** — and DEEP·FIN's reinsurance KPI is unrefreshed |
| **B5 SEMI (AMD/Helios leg)** | 🟡 **PARTIAL** | `theme-age "Helios"` 🟡ACCEL **6.43×**, 107 hits — real. ⚠ **But `theme-age "Advancing AI"` = ⚪ECHO (79d, 16.3% share, 610 hits, only 1.88×)**: the *event date* was a genuine calendar gap; **the *theme* is already consumed.** Residual: AMD's OBV (**distributing −58%/20d**) must turn |
| B3 / B4 / B6 | 🟡 **PARTIAL** | All resolve on dated prints inside 48h; **none is bettable before its print, and this file says so rather than pre-judging** |

## Momentum-only + positioning stamps (`module_flow --positioning`, finalists only)
| Name | Flow | Short (%float / dir / DTC) | Options P/C · skew | Stamp |
|---|---|---|---|---|
| **DINO** | 🟢가속, OBV **매집**, RS20 +40.8%, vol **1.29×** | 5.2% **BUILDING**, DTC 3.6 | 0.11 · **+8.9** | ⚡ **Shorts building into an accumulating tape = squeeze fuel. Turn-conditional, NEVER a standalone buy — HARD STOP REQUIRED** |
| **CB** | 🟢가속, OBV **매집**, vol 1.20× | 1.2% building, DTC 2.7 | 0.38 · +18.8 | 🟢 Clean; prints **tomorrow** — **HARD STOP REQUIRED into a binary** |
| **XOM** | 🟡중립, OBV **매집** | 1.0% **covering**, DTC 2.1 | 0.43 · **−4.9** | 🟢 Cleanest crowding profile on the sheet. ⚠ Complacent options = **little squeeze fuel**: this is a *structural* expression, not a *momentum* one |
| **HUM** | 🟡중립, OBV 매집, RS60 **+78.8%** | 4.1% **covering**, DTC 2.8 | **1.13** · +13.5 → **hedge/fear** | ⚠⚠ **Two positioning instruments DISAGREE: FINRA daily short-vol z = +1.97 (극단) while settlement short interest is COVERING.** Recorded unresolved. **HARD STOP REQUIRED**; prints 07-29 |
| **AMD** | 🟡중립, **OBV 중립→distributing (−58%/20d on the chart tool)** | 2.6% covering, DTC 1.3 | **1.03** · ★ **+43.1** → **hedge/fear** | ⚠ **The steepest downside skew on the sheet — the options market is paying up hard for protection into the 07-22 event.** Momentum-only risk: **RS60 +61.6% with OBV not confirming → tape trade, HARD STOP REQUIRED** |

⚠ **US has no investor-type feed** (no KR-style foreign/institution actuals). Every "who is buying"
statement above is a **FINRA short-vol / short-interest / options proxy** — positioning context, and
per the desk's own failure-class-2 rule it may only **amplify** a proposition that already has its
own catalyst. **It is never a standalone trigger.**

---
**ALPHA EXIT CHECK:** ✅ `theme_age` run **first**, token-0, on every bet theme — and it **changed two
verdicts** (`insurance earnings` 🔴FADING with **1 hit/28d** demoted the FIN leg to PARTIAL;
`Advancing AI` ⚪ECHO qualified the AMD "missed catalyst" from fresh to consumed) · ✅ every §B tag
filled with an evidence label + date (mirrored into `BET_SHEET.md` §B) · ✅ **🔴 items logged with WHY,
so "it's cheap" cannot resurface next run** — the PSX ticket's *rationale* is 🔴 while its *gap* stays
open, and the distinction is stated so neither half is lost · ✅ **momentum-only stamps applied** (AMD,
DINO) and **hard-stop stamps applied to every ⚡crowded-short / binary-facing name** · ✅ positioning
gate applied US-style (crowded-short = turn-conditional squeeze fuel, never a standalone buy) ·
✅ `ACTION_TICKETS.md` written with **both-sides brackets B1–B6 + B2b, plus the cycle-GAP core-starters**
· ★ **three script-level defects caught rather than accepted: a sign-reversed PSX rationale, a stale
NVDA flow line, and announced-but-missing brackets — plus an FX disagreement (1482 vs 1380) between two
script-owned artifacts of the same day.**
**→ proceed to DRIFT.**