# ACTION_BRACKET — 2026-09-05  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,210,744원 · fx 1360 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** Aug PPI (D-5, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF Aug PPI (D-5) prints toward cool
- **size:** 10 sh @ ~$230.36 (≈$2,303.6 notional, risk $167.83 = 1.5% )
- **stop:** $214.23 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF Aug PPI (D-5) prints toward hot
- **size:** 3 sh @ ~$388.9 (≈$1,166.7 notional, risk $89.51 = 0.8% )
- **stop:** $361.68 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ═══ APPENDED BY `industry_US` ALPHA — 2026-09-05 ═══

> The block above is `scripts/action_bracket.py`'s own output. This block records what the stage
> owes the file that the script cannot generate, and **one disagreement between the two**.
> **Analytical artifact. No order is sent, no size is recommended (P4).**

## ✅ `D294` did NOT reproduce — first clean run in 8

`action_bracket` has printed *"no GAP and no binary"* against a live GAP and live binaries on
**seven** prior runs (`D294`, and `D155` for the local-midnight false negative). **Today it correctly
named the nearest binary (Aug PPI, D−5) and armed both sides.** Recorded because a defect's
non-reproduction is evidence and is as worth logging as a reproduction.

## ⚠ The script and PREMORTEM disagree about PPI, and both are right

`action_bracket` armed **PPI** because it is the *nearest dated binary*. **PREMORTEM Lens 2
deliberately did NOT bracket PPI**, on `B4` grounds: *neither branch would change the conclusion*
(a hot print confirms `ENRG OW+` **and** `INDU UW−` **and** `STPL UW` simultaneously; a cool print is
already absorbed by `P136`'s kill condition).
⇒ **These are two different objects and the file carries both rather than reconciling them away.**
An **execution ticket** is a pre-committed conditional for a human; an **information bracket** is a
registered scoreable row. **A binary can deserve the first and not the second.** Registered as
**`D518`**: *`action_bracket` selects on date-proximity while PREMORTEM selects on information
content, so the two will routinely disagree and nothing currently says which governs.*

## The registered both-sides brackets this run — the information objects

**Not tickets. No size. Scoreable rows, thresholds from `D93` measured dispersion.**
(`M1305`: the ETF straddles `SPY` ±0.5% / `SMH` ±1.8% expire **09-08** and `XLE` ±1.6% expires
**09-09**, i.e. **before both binaries** — so no ETF-level threshold could be taken from the options
market and every line below comes from measured dispersion instead.)

| row | observable | branch A | branch B | settles |
|---|---|---|---|---|
| **`P136`** | `EW{16 Energy}` − `SPY`, 5 settled sessions | ≥ **+4.508** | ≤ **−3.863** | **09-14** |
| **`P137`** | `SMH` − `SPY`, 4 settled sessions | ≥ **+4.217** | ≤ **−2.886** | **09-11** |
| **`P138`** | `^TYX − ^FVX` 4-session change, bp | ≥ **+4.40** (steepen) | ≤ **−5.97** (flatten) | **09-11** |
| **`S145`** | `EW{STX,WDC,AMD}` − `SMH`, 4 settled sessions | ≥ **+6.825** | ≤ **−3.406** | **09-11** |
| **`S146`** | `EW{VST,CEG,VRT}` − `ETN`, 5 settled sessions | ≥ **+7.651** (p95) | ≤ **−5.037** | **09-14** |
| **`S147`** | `EW{MPC,PSX,VLO}` − `SPY`, 5 settled sessions | ≥ **+7.059** | ≤ **−3.740** | **09-14** |

🚨 **2026-09-07 is Labor Day (`D507`)** — every window above is counted in **settled sessions**, so
the 5-session rows settle **09-14**, not 09-11.

## The cycle observations this stage hands forward INSTEAD of a core-starter

**`cycle_exposure` reports NO top-rank GAP** (AI-compute epicenter **17.48%** vs a ≥12% bar;
Energy/refining **10.47%** vs ≥8%), so **the tape-independent core-starter module is not triggered
and none is written.** PREMORTEM Lens 4 nevertheless found two things the flag cannot see, and they
are carried here as **named observations, not as tickets**:

1. **`M1308` / `D513`** — the **AI-power cycle is not in the registry**, so its absence reads as
   "no gap". The lane is coherent (`CEG` +0.644, `VST` +0.619, `VRT` Δ +0.444, all OBV 매집 with
   positive flow) and **the book's only exposure to it is `ETN`, the lane's one 🔴분산 name**.
2. **`M1309`** — the rank-1 cycle's held epicenter is on the **non-accumulating** side of its own
   node: `NVDA` **분산**, `ANET` **중립**, while storage/memory — carrying the board's three largest
   Δflows — is **0% of the book**.

⇒ Both are **structural observations for the book desk and for a human**, not conditionals. This
stage issues **no size and no order** (P4).
