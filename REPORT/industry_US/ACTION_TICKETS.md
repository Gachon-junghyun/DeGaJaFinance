# ACTION_BRACKET — 2026-09-14  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,136,443원 · fx 1346 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** FOMC decision (SEP/dot plot) (D-2, axis=rates) — both-sides armed below.

### BRACKET::A_cool  ★asym-hedge — NVDA  (BUY)
- **condition:** IF FOMC decision (SEP/dot plot) (D-2) prints toward cool
- **size:** 5 sh @ ~$218.29 (≈$1,091.45 notional, risk $89.94 = 0.8% )
- **stop:** $203.01 (−7.0%) · exch NASD

### BRACKET::B_hot — XLE  (BUY)
- **condition:** IF FOMC decision (SEP/dot plot) (D-2) prints toward hot
- **size:** 36 sh @ ~$65.14 (≈$2,345.04 notional, risk $168.63 = 1.5% )
- **stop:** $60.58 (−7.0%) · exch AMEX

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---
## ADDENDUM — industry_US BET/ALPHA stage (14:3x KST, append-only; the script block above is unchanged)

> Conditional, **unsized** pre-commitments from this run's brackets. The script armed the calendar's nearest
> binary only (FOMC). Everything below is an analytical observable with both branches; a human executes
> separately, never the desk. No buy/sell advice.

| bracket | observable (frozen) | window | A | B | pre-declared informative branch |
|---|---|---|---|---|---|
| `P151` | `SHY` 1-session % | 09-15 → 09-16 close | ≤ −0.236% (hawkish) | ≥ +0.134% (dovish) | B (falsifies five legs: UTIL/RE/STPL UW, FIN N−, `MET`) |
| `P148` | `IEF − SHY` 2-session | → 09-17 | slope steepens | flattens | already inside A at registration |
| `S156` | distillate crack `HO×42−CL` 5-session Δ | 09-11 (108.24) → 09-18 | ≤ −4.25 (collapse) | ≥ +8.70 | A (against the held crack leg; live −6.6 unsettled) |
| `P149` | `XLE` 5s − `CL=F` 5s (pp) | 09-11 → 09-18 | ≥ +4.69 | ≤ −5.17 | read with `P156` (sign) |
| `P152` | `EW{FRO,DHT,INSW,STNG,TNK}` − `SPY` 5s | 09-14 → 09-21 | ≥ +6.240 | ≤ −4.308 | B (state already above A) |
| `P153` | `FXY` 5-session % | 09-14 → 09-21 (BoJ Fri 09-18 JST inside) | ≥ +0.855% | ≤ −1.059% | B |
| `P154` | `QQQ − SPY` 2-session (pp) | 09-17 → 09-21 | ≤ −0.632 (carry unwind reaches NDX) | ≥ +0.772 | A |
| `P155` | `EW{NVDA,AVGO} − SPY` 1-session (pp) | 09-17 → 09-18 (NDX rebalance funding) | ≤ −1.932 | ≥ +1.584 | A-without-09-21-reversal, or B |
| `P156` | `CL=F` 5-session % | 09-14 → 09-21 | ≥ +8.764% | ≤ −5.734% (de-escalation) | B |

**Epicenter-map statement (PREMORTEM Lens 4 / BET §S):** rank-2 Energy is held 100% on the crack leg
(`MPC`+`PSX`, one unit) with **0% barrel and 0% freight** while the crack KPI moves against it live; the module's
rule is that a 🔴/unsettled tape gates *timing*, never justifies 0% core in a top-2 cycle. Cleanest barrel
expressions on the sweep: `COP` / `XOM`; freight is unmeasurable by the universe (`P152` is the instrument).
Rank-1 AI-compute: no gap; the four held names are **two** risk units and all read EXHAUSTED (Lens 3).
