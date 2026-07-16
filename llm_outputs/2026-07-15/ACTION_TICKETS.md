# ACTION_BRACKET — 2026-07-15  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 11,026,016원 · fx 1492 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** June PPI (D-0, axis=inflation) — both-sides armed below.

### CORE-STARTER (tape-independent) — NVDA  (BUY)
- **condition:** establish NOW regardless of tape — closes AI-compute / semiconductors epicenter GAP (0.0% < 12.0%)
- **size:** 3 sh @ ~$211.74 (≈$635.22 notional, risk $59.11 = 0.8% )
- **stop:** $196.92 (−7.0%) · exch NASD
- **why core:** real-alpha REAL/not-priced, flow 🟡중립=non-chase entry, epicenter bottleneck, fwd PE 16.5 < AVGO 20.1

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF June PPI (D-0) prints toward cool
- **size:** 7 sh @ ~$211.74 (≈$1,482.18 notional, risk $110.84 = 1.5% )
- **stop:** $196.92 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF June PPI (D-0) prints toward hot
- **size:** 2 sh @ ~$300.27 (≈$600.54 notional, risk $59.11 = 0.8% )
- **stop:** $279.25 (−7.0%) · exch NYSE

---

## ALPHA ENRICHMENT (07-15, analyst layer over the deterministic base above)

> The script armed the *nearest* binary (PPI) + one core name (NVDA). Below extends it with the premortem's
> full bracket set, the realized-PPI update, and the epicenter-core refinement. All DRY-RUN, illustrative sizing.

### ⚡ PPI binary RESOLVED — the A_cool branch is the realized one
June PPI printed **−0.3% m/m vs +0.0% exp (COOL)** [BLS 07-15]. → **BRACKET::A_cool is the live branch; B_hot (MPC) stands down for today** but is RETAINED as the *forward re-arm trigger*: re-arm the hot-branch (MPC/XLE/KRE, short-duration) IF **core PPI ≥+0.5% next print OR 10Y >4.75%** (the term-premium bid is still live even after a cool print).

### Epicenter core refinement (premortem Lens 4)
The script defaulted the core to **NVDA**, but NVDA is the *crowded-short* epicenter (4%ile). Refine:
- **Tape-INDEPENDENT monopoly core first: TSM + AVGO** (+ ASML small, at-target) — least squeeze-exposed; TSM actively short-covering (z −1.23). Establish regardless of tape toward the ≥12% floor.
- **NVDA + MU = squeeze-GATED adds** — the crowd gates *these*, not the monopoly core. NVDA ticket above is valid but tag it hard-stop / gated (add on the dip, stop 196.92), not the first tranche.

### Hormuz both-sides bracket (premortem Lens 2 — the open binary) ⚠ narrative 🔴FADING
Theme "Hormuz oil" is 🔴FADING (news accel 0.39x) even as the physical blockade persists → de-escalation is being *priced*, which raises the TACO-down risk. Both branches stay conditional (hard-stop, turn-confirmation required — a crowded-short is not a standalone buy):
- **2a ESCALATION-UP:** IF WTI holds **>$88–90** / confirmed strait closure → energy squeeze: VLO/MPC (refiner crack), XLE, FANG/OXY. *Invalidation:* WTI <$76 / ceasefire. ⚠ also second-order PPI-hot → hits UTIL + long-duration IT/SEMI.
- **2b TACO-DOWN:** IF ceasefire re-declared / transits >30/day / WTI **<$74** → pare any energy-positioning into the gap; the relief bid activates the SEMI/IT core (own-side good tail). Watch UW Consumer-Disc squeeze (XLY/JETS).

### Defense un-gated starter (premortem Lens 4 — NOT crowded, no squeeze excuse)
- **RTX or LMT** small multi-year core — rank-3 cycle held 0% at all layers; defense is un-crowded (NOC −12% YTD). RTX is the flow-confirmed expression (CONFIRMED-TURN, stop 181.83); LMT/NOC are the deeper-value re-rate options gated to late-July Q2 prints.

### Bettable-now set (post-freshness-gate) — for the watchlist, DRY-RUN only
🟢 LIVE: **SEMI monopoly core (TSM/AVGO)** · **FIN regionals/broker (PNC/HBAN/SCHW)** · **VST** · **RTX** · **META**.
🟡 PARTIAL (residual stated, hard-stop): IT cyber (PANW/CRWD/FTNT — above target) · NEE (bond-proxy, distribution) · NOC/LMT/ETN/GEV · HCA (no catalyst this week).
🔴 RESOLVED-priced & DROPPED (logged so "it's cheap" can't resurface): **GS/MS/JPM money-center capital-markets** (pop spent, at/above target).

### Risk-unit reminder (premortem Lens 2)
UTIL(bond-proxy) + UW RE/Disc + long-duration IT/SEMI are correlated on the **10Y real-yield axis** — a rate re-lift is the single kill across UTIL + IT + SEMI at once. Size the long-duration complex as ONE unit; today's cool CPI+PPI landed on its favorable side, but the term-premium bid keeps the other branch alive.

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; a human executes separately via `module_KIS ... --execute`. No order is sent by this desk.*