# ACTION_BRACKET — 2026-09-07  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,184,840원 · fx 1355 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** Aug PPI (D-3, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF Aug PPI (D-3) prints toward cool
- **size:** 10 sh @ ~$230.36 (≈$2,303.6 notional, risk $168.07 = 1.5% )
- **stop:** $214.23 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF Aug PPI (D-3) prints toward hot
- **size:** 3 sh @ ~$388.9 (≈$1,166.7 notional, risk $89.64 = 0.8% )
- **stop:** $361.68 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*