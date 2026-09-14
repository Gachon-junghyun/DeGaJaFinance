# SWEEP_READ — industry_US — 2026-08-02 (Sun)

> The **reading**, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json`,
> `US_LIVE_SHORTLIST.json` and `CYCLE_EXPOSURE.json` and are cited by artifact, never reprinted.
> `asof 2026-07-31 settled` — today is a Sunday, so the whole sweep is on a settled bar (no D74).

## 1 · Universe headline — three numbers

**n = 300 · wflow +0.002 · 🟢16 / 🔴86.**
The whole universe's mega-cap-weighted flow is **arithmetically zero**, with reds outnumbering greens
**5.4 : 1**, and **every sector's `delta` is negative except Consumer Discretionary (+0.032)**.
`new_green`: **STX · ICE · MPWR · ETN · FTNT · ADM** (6).

⚠ **`us_top300.csv` is 18 days stale** (the sweep warned) — market caps, and therefore every
`wflow`, carry a two-and-a-half-week-old weighting. Rebuild is weekly by rule.

---

## 2 · Cross-checks against the MACRO matrix — where the money agrees and where it does not

### ✅ CONFIRMS

- **Energy OW−.** `SECTOR_FLOW_US.json §sector_rotation` puts Energy **#1 on both wflow and eqflow
  with ZERO reds of 16** — the only sector on the board with no red name. The MACRO matrix ranks it
  #1 on 20-day excess vs SPY. **Both axes point the same way.** ⚠ See §3 — its green count does not.
- **Utilities UW− and Materials UW.** Both sit at the bottom of the flow board (Utilities wflow
  −0.284 / 8 reds; Materials −0.313 / 5 reds / 0 greens) and both are negative on 5-day *and* 20-day
  excess vs SPY. **S36 FIRED-B is corroborated by the flow instrument, not just by the price leg.**
- **Health Care's money side has reversed.** wflow **−0.112**, eqflow −0.051, and the **board's worst
  delta at −0.472**. **C7's four-run "money without narrative" gap closed from the money side.**

### ⛔ CONTRADICTS — and this is the file's reason to exist

- **⛔ Industrials.** MACRO holds **UW−** on price (**XLI −2.52pp exc20d / −2.64pp exc5d vs SPY**).
  The flow board gives Industrials **the universe's BEST breadth (0.10), the most greens of any sector
  (5 of the board's 16), and eqflow +0.048 ABOVE wflow +0.001 — i.e. breadth-led, not mega-cap-led.**
  **The money is broader than the price.** ⇒ **ROTATION must resolve this, not average it.** The
  candidate reconciliation is the one S42 already frames: a **sub-node** (capital goods + defence
  primes, median RS20 +10.1 against the **CAT control −15.7**) rising inside a sector whose index is
  falling — i.e. **W5, a label carrying two opposite things**, the same shape as R7 and the Utilities
  split.
- **⛔ Info Tech.** MACRO restated the label as "split, now asymmetric." The flow board makes the
  asymmetry sharper: **wflow +0.081 against eqflow −0.144 — the widest wflow−eqflow gap on the board
  (+0.225) — with 25 reds of 56, the worst red count anywhere.** ⇒ **the memory turn S30 scored is
  MEGA-CAP-NARROW at the breadth level.** The turn is real on the frozen observable and it is **not**
  a sector-wide participation event. Both readings are handed forward; neither is dropped.
- **⚠ Financials — R32's statistic re-tested and it did NOT flip today, but it still cannot be used.**
  Recomputed directly from all 47 rows: **all-47 gap eqflow−wflow = +0.0370 (breadth-led)**;
  **ex-BRK-B = +0.0095.** The sign survives (on 07-30 it flipped to −0.0166), but **74% of the
  statistic is one row**: **BRK-B = $1,055.7bn = 13.94% of a $7,574bn sector at flow −0.116.**
  ⇒ **R32 stands. "Breadth-led" may not be re-bought as the OW's reason on a +0.0095 gap** — the
  reason has to be P13's steepener or the insurance node, not this number.

---

## 3 · Shortlist composition — the ABSENCES, each diagnosed

`US_LIVE_SHORTLIST.json` — 15 names at mcap ≥ $10B, 🟢 filter, FINRA short-z verdicts.
**Clean-rise set (🟢 ∧ low-short/covering): MET · ITW · MPWR · RTX · TRI · EA.**

### ⛔⛔ The largest absence is the sector the whole board agrees is #1

**Energy contributes ONE green of sixteen — and it is a filter artifact, diagnosed, not cited.**
**12 of the 16 Energy names pass the accumulation pre-condition (`OBV 매집 ∧ RS20 > 0`) and 11 of
those 12 are blocked from 🟢 by `vol_surge` ALONE**: COP 0.93 · XOM 0.89 · CVX 0.88 · PSX 0.88 ·
MPC 0.82 · VLO 0.80 · FANG 0.80 · OXY 0.80 — **every one of them against a 1.20 gate, while carrying
RS20 vs SPY of +13.1 to +19.7.** The sector's maximum `vol_surge` across all 16 names is **1.37**.
⇒ **This is precisely the failure the SWEEP protocol names in its own field notes** (*"an ENRG
shortlist of 0 turned out to be a 🟢-tag filter artifact — the refiners were OBV-accumulating but
tagged 🟡"*), reproducing on the sector with the board's best flow, best 20-day excess and zero reds.
**The green count is not admissible as Energy evidence this run.**

### Other absences

| Sector | Absence | Diagnosis |
|---|---|---|
| **Health Care** | 0 shortlist names, 0 greens of 32 | ⚠ **Split verdict.** The *sector* call is evidence (wflow −0.112, delta −0.472, 7 reds). The *green count* is **partly artifact** — 6 names pass the pre-condition and **all 6 are blocked** (BMY 1.11 / rs20 +12.0 · REGN 1.03 / +16.3 · ABT 0.83 / +10.5 · TMO 1.02 / +9.4). **Cite the flow scores, not the zero.** ★ This **corrects this run's own MACRO §E line**, which leaned on the zero |
| **Real Estate** | 0 greens **and 0 reds** of 12 | **Pure limbo artifact.** wflow +0.078 / eqflow +0.091 (positive, breadth-led) with **nothing being sold**; 4 names pass the pre-condition and **all 4 are blocked** (DLR 0.82 · PLD 1.08 · IRM 1.14 · CBRE 1.17). **A sector with no reds and no greens is an instrument saying nothing, not a market saying nothing** |
| **Materials** | 0 greens of 12 | **Evidence, with a name-level caveat.** 5 reds, wflow −0.313, negative 5d and 20d excess ⇒ **S36 FIRED-B is corroborated.** ⚠ But **only 2 names even reach the pre-condition and both are steel carrying RS20 +16.3 (NUE) and +13.7 (STLD) vs SPY** — the S36 price/breadth tension survives at the name level even though it resolved at the sector level |
| **Utilities** | 1 green of 15 | **Evidence.** 8 reds, wflow −0.284 / eqflow −0.289. The single green is **PCG for a 4th consecutive run** — the *regulated* leg, not the AI-power leg, which is the S35/S47 split showing up in the tag column |

### ★ What the shortlist surfaced that the desk does not own

- **GRMN is the shortlist's #1 flow (+0.92) with RS20 +22.1 vs SPY, and it has no thesis anywhere —
  third consecutive run.** The 07-30 PREMORTEM explicitly declined to bracket it (*"a bracket needs a
  proposition to threaten and there is none"*). **It is now a three-run coverage gap, not a one-run
  observation.**
- **STX is a `new_green` and on the shortlist at +0.80** — the memory turn S30 scored, now confirmed
  on the flow instrument rather than only on RS. ⚠ **Its FINRA short-z is +1.23 — shorts are BUILDING
  into the turn**, which is a disagreement between the A-grade price axis and the B-grade positioning
  proxy, recorded as `indistinguishable` (C4) rather than resolved.
- **ETN is a `new_green` at +0.70 with the shortlist's HIGHEST short build (z +1.49)** — and it sits
  in the **AI physical layer the desk's own §3a row carries as six names / six 🔴** (GEV · VRT · ETN ·
  PWR · VST · CIEN). **One of the six just turned green.** Corroborated on the feed: *"Eaton Stock
  Jumps on AI Relief After Earnings Beat"*.
- **ICE (`new_green`, +0.79)** re-lights the exchanges node whose registered RS60 test M135 measured
  **broken**; **FTNT (`new_green`, +0.56)** re-lights the security node carried under **C5**.
- **BKR is #2 on the shortlist (+0.87)** and **its reject-ledger basis is already known-false** — it
  was filed 07-27 as *"the only negative flow score of 11 Energy names"* and has since been the
  sector's #1. Its recheck date has not arrived, so it is not `due`; **it is named here so a second
  run does not pass it silently.**

---

## 4 · 🚨 Cycle-exposure GAP — handed to ALPHA's action bracket

`CYCLE_EXPOSURE.json` (read-only KIS book, ≈ $10,722 total / $5,808 invested):

- **rank 1 · AI-compute / semiconductors — ✅ 13.02% vs a 12.0% floor.** Margin **+1.02pp**, held via
  AVGO / NVDA / TSM. ⚠ **M146 measured that these ✅s have been mark-to-market drift with nothing
  traded** — a 1.02pp margin is inside that drift band, so ✅ is not a construction claim.
- **rank 2 · Energy / oil-refining — 🚨 GAP: 6.9% epicenter vs 8.0% required, margin −1.10pp.** Held
  epicenter = MPC, PSX; the rest of the cycle is touched only through **LNG (adjacent/fuel)** — beta
  to the *consequence*, none to the *engine*.
- **rank 3 · Missile-defence — ⚪ n/a**, no threshold set in the registry.

⚠⚠ **The honest juxtaposition, stated rather than smoothed:** the deterministic registry says the
book is **under-exposed to the rank-2 cycle's engine on the same weekend that (a) the settled 3-2-1
crack fell −16.7% in two sessions on its gasoline leg and (b) the Iran strike-cancellation went
conditional.** The standing rule is that **a 🔴 tape gates ADD timing and never justifies zero core**
— but this tape is not 🔴; it is #1 on flow with a broken commodity underneath. **Both facts go to
ALPHA together; neither cancels the other, and no sizing follows from either here (P4).**

⚠ **`data_build/cycles/cycle_registry.json` still has NO AI-security row (D20)** — on the weekend an
AI-security event led the entire foreign feed by outlet count. A 0% exposure to it cannot raise a GAP
because the registry has nowhere to raise it from.

---

## 5 · Instrument note — the 🟢 gate's arity changed for a FOURTH distinct state

Measured on this sweep: **`velocity` is non-null on 0 of 300** (07-27: 50/300 · 07-28: 0/300 ·
07-30: 50/300 · today: 0/300), so the gate is back to **3-axis unanimity** and **zero of the 16
greens cleared on the velocity path.** **85 names pass `OBV 매집 ∧ RS20 > 0`; 16 are 🟢; 69 are
blocked and 100% of the 69 fail on `vol_surge` alone.**

⇒ **M144's mechanism replicates a 7th time across two markets and five dates**, and **M272's
"the arity changed" finding reproduces** — the `velocity` join **oscillates 50 → 0 → 50 → 0 between
runs**, which is a code-level instability, not a market fact. **New dig D126.**
**Consequence binding on every downstream stage: a 🟢/🟡 difference this run carries no news-velocity
information at all, and 69 accumulation candidates were removed by a volume test wearing a flow
label (C9 / D11).**

---

*asof 2026-08-02 · sweep asof 2026-07-31 settled · artifacts: `SECTOR_FLOW_US.json` ·
`US_LIVE_SHORTLIST.json` · `llm_outputs/2026-08-02/CYCLE_EXPOSURE.{md,json}`.
Analysis only, zero buy/sell (P4).*
