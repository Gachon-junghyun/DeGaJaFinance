# ACTION_BRACKET — 2026-07-14  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 11,011,585원 · fx 1492 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** June PPI (D-1, axis=inflation) — both-sides armed below.

### CORE-STARTER (tape-independent) — NVDA  (BUY)
- **condition:** establish NOW regardless of tape — closes AI-compute / semiconductors epicenter GAP (0.0% < 12.0%)
- **size:** 3 sh @ ~$211.62 (≈$634.86 notional, risk $59.04 = 0.8% )
- **stop:** $196.81 (−7.0%) · exch NASD
- **why core:** real-alpha REAL/not-priced, flow 🟡중립=non-chase entry, epicenter bottleneck, fwd PE 16.5 < AVGO 20.1

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF June PPI (D-1) prints toward cool
- **size:** 7 sh @ ~$211.62 (≈$1,481.34 notional, risk $110.69 = 1.5% )
- **stop:** $196.81 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF June PPI (D-1) prints toward hot
- **size:** 2 sh @ ~$303.896 (≈$607.79 notional, risk $59.04 = 0.8% )
- **stop:** $282.62 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*