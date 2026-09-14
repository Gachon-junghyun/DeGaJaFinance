# ACTION_BRACKET — 2026-09-08  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,157,912원 · fx 1343 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** Aug PPI (D-2, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF Aug PPI (D-2) prints toward cool
- **size:** 10 sh @ ~$227.99 (≈$2,279.9 notional, risk $169.35 = 1.5% )
- **stop:** $212.03 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF Aug PPI (D-2) prints toward hot
- **size:** 3 sh @ ~$396.92 (≈$1,190.76 notional, risk $90.32 = 0.8% )
- **stop:** $369.14 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---

## ALPHA addendum — 2026-09-08 (Stage 10 / L1·ALPHA)

🚨 **Price caveat on the two tickets above.** `action_bracket` ran **after 09:30 ET**, so the quotes it
sized on (`NVDA` ~$227.99, `MPC` ~$396.92) are the **PARTIAL 2026-09-08 intraday bar**, not a settled
close (`D577`). The settled 09-04 closes are `NVDA` **230.36** and `MPC` **388.90**. **The share counts
and stops above are therefore illustrative twice over** — once because they are DRY-RUN, and once
because their reference price is an incomplete bar. **A human re-prices before anything is executed.**

### Both-sides coverage of the nearest binary — **US Aug PPI, 2026-09-10, D−2**

The two tickets are the tape expression. The **analytical** bracket registered for the same binary is
**`P147`** (`TIP` − `IEF` 1-session excess, 09-09 close → 09-10 close, **A ≥ +0.1514% / B ≤ −0.1492%**,
registration state **49.2nd percentile = dead centre**). ⚠ **Note the two are not the same object and
must not be read as confirming each other**: `P147` measures the **inflation-vs-real decomposition**;
the tickets express a directional equity/energy pair. `P147` settles; the tickets do not.

### The bracket that is NOT here, and why

**No cycle-GAP core-starter is emitted.** `cycle_exposure` reports **no GAP** (AI-compute 17.57% vs
≥12.0%; Energy/refining 10.73% vs ≥8.0%), **but PREMORTEM Lens 4 established that the ✅ covers only
the three cycles the registry knows**, and **two of the week's loudest have no registry row at all** —
the **gas/LNG dislocation** and the **AI-power interconnect-permit** lane. Emitting a core-starter off
a ✅ this desk cannot verify would be the opposite of what the module is for. **Stated as an absence
with its reason, not left blank.**

### Standing conditional handed to the next run

**A confirmed Strait-of-Hormuz reopening (≥3 outlets) is a correlated hit across the whole board** —
it takes the gas leg, the refining premium, the breakevens and the three duration underweights at
once (PREMORTEM §2a). It is on `catalyst_calendar` as an **undated 🔀binary**, so no dated ticket can
be written for it; it is `P145`'s VOID clause and `P122`'s KPI. ⚠ **The QatarEnergy force majeure runs
into November — a reopening headline that does not lift it is not the event** (the `M1363` OPEC+
precedent).

*Analytical artifact. Zero buy/sell advice. No order is sent by this desk (`P4`).*
