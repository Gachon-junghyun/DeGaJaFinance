# ACTION_BRACKET — 2026-07-29  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,946,407원 · fx 1466 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** FOMC decision (Warsh, no SEP) (D-0, axis=rates) — both-sides armed below.

### CORE-STARTER (tape-independent) — NVDA  (BUY)
- **condition:** establish NOW regardless of tape — closes AI-compute / semiconductors epicenter GAP (8.32% < 12.0%)
- **size:** 6 sh @ ~$192.36 (≈$1,154.16 notional, risk $87.01 = 0.8% )
- **stop:** $178.89 (−7.0%) · exch NASD
- **why core:** real-alpha REAL/not-priced, flow 🟡중립=non-chase entry, epicenter bottleneck, fwd PE 16.5 < AVGO 20.1

### CORE-STARTER (tape-independent) — PSX  (BUY)
- **condition:** establish NOW regardless of tape — closes Energy / oil-refining (Hormuz + Russia crack) epicenter GAP (7.72% < 8.0%)
- **size:** 5 sh @ ~$209.32 (≈$1,046.6 notional, risk $87.01 = 0.8% )
- **stop:** $194.67 (−7.0%) · exch NYSE
- **why core:** cheapest large refiner on forward (11.2, PEG 1.17) + the only Energy name with shorts actively exiting (FINRA short-vol z -1.43, 5v5 -16.6▼) = clean structural entry, not an extended one (cf. MPC RSI 85.7). Crack-spread leverage, not crude beta. Human-locked 2026-07-17; evidence: llm_outputs/2026-07-17/industry_US/SECTOR_DEEP_ENRG.md

### BRACKET::A_cool  ★asym-hedge — NVDA  (BUY)
- **condition:** IF FOMC decision (Warsh, no SEP) (D-0) prints toward cool
- **size:** 6 sh @ ~$192.3101 (≈$1,153.86 notional, risk $87.01 = 0.8% )
- **stop:** $178.85 (−7.0%) · exch NASD

### BRACKET::B_hot — XLE  (BUY)
- **condition:** IF FOMC decision (Warsh, no SEP) (D-0) prints toward hot
- **size:** 39 sh @ ~$58.96 (≈$2,299.44 notional, risk $163.14 = 1.5% )
- **stop:** $54.83 (−7.0%) · exch AMEX

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*