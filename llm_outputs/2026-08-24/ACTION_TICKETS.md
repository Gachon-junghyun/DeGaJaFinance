# ACTION_TICKETS — 2026-08-24 · industry_US / L1·ALPHA

> Pre-committed **conditional** tickets. **A human executes; this desk never sends an order.**
> ⚠⚠ **This file is HAND-BUILT and its DRY-RUN share counts are deliberately OMITTED.** Two reasons,
> both stated rather than silent: **(1)** this run's mandate is *analytical output only, zero buy/sell
> recommendations*, so no size is written anywhere; **(2)** the generator contradicted itself — see §0.
> **Logged as a deviation from documented practice, 2nd consecutive run.**

## §0 · 🚨 `D294` reproduces a SIXTH time, and today it is a self-contradiction inside three lines

`scripts/action_bracket.py`, verbatim, consecutive output lines:

```
**Nearest binary:** NVDA earnings (D-2, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
```

**The window holds five binaries on `CATALYST_WATCH` alone** (July PCE 08-28 · `NVDA` 08-26 ·
`FRO` 08-28 · `AVGO` 09-02 · the undated Hormuz row) **and three more that the calendar misses and
this run recovered from news bodies** (Jackson Hole **08-27**, 3rd consecutive miss · Bessent's
sanctions presser **14:00 ET TODAY**, 1st · Canada's retaliation effective **2026-09-08**, 1st).
⇒ **The tool names the nearest binary and then denies one exists.** Positive-form remedy carried in
`RESEARCH.md` Part C; the tickets below are therefore written by hand from PREMORTEM's registered
brackets.

## §1 · Both-sides brackets — the two ≤48h binaries

> **A one-way tilt into a known binary is a protocol violation.** Both are bracketed.

### T-1 · `NVDA` prints 2026-08-26 (D-2) — **the bracket is RELATIVE, not directional**
- **Registered as `S118`.** Observable: **`EW{MU, SNDK, WDC}` 2-session excess vs `NVDA`**, over
  **2026-08-26 close → 2026-08-28 close**.
- **A (memory carries the information)** — `EW{MU,SNDK,WDC}` − `NVDA` **≥ +6.50pp**.
- **B (NVDA carries it)** — the same spread **≤ −6.50pp**.
- **C** between — the disclosed favourite; the band is 13pp wide because all four implied moves are large.
- ★ **Threshold set OUTSIDE the implied move** (LIVE INTRADAY chain read, identical 08-28 expiry):
  `NVDA` **±6.13%** (ATM IV 0.692) · `MU` ±6.52% (0.770) · `SNDK` **±8.41%** (0.926) ·
  `WDC` **±11.56%** (0.880). **Three non-printing memory names price a bigger move than the printer.**
- 🚨 **The threshold was NOT taken from the desk's own tool**: `module_flow NVDA --positioning`
  returned **`±1.3% (expiry 2026-08-24, D0) → complacent, little fuel`** — it priced an expiry that
  expires **today**, two days before the print, **4.7× too small**, with a confident wrong adjective
  (`D315`, 5th run). **Read the chain, not the tool, for any event name.**
- **No size, no direction.** This is a measurement appointment, not a position.

### T-2 · Bessent's sanctions press conference — **14:00 ET TODAY (D-0)**
- **Registered as `S119`.** Observable: the equal-weight **Energy** basket's **3-session excess vs
  `SPY`**, over **2026-08-24 close → 2026-08-27 close**.
- **A (escalation prices; the ENRG OW is helped)** — Energy 3-session excess **≥ +2.60pp**.
- **B (already priced / the exception channel dominates; the ENRG OW is hit)** — **≤ −2.60pp**.
- **C** between — the favourite.
- **Threshold derivation, stated**: the measured trailing-60 **5-session** Energy excess has
  mean **+0.607** and sd **4.325** ⇒ a 3-session sd ≈ **3.35** and mean ≈ +0.36; **±2.60pp ≈ ±0.60σ.**
- ★ **B is the branch this run's own evidence points at.** The **LIVE INTRADAY** tape already sold
  crude on the Iraqi-permit news (**Brent −1.3% to $93.16**, 04:32 ET) **before** the presser.
  **Graded and disclosed: A confirms, B falsifies.**
- ⚠ **This binary is NOT on `CATALYST_WATCH`** — it was recovered from a wire body that named the
  time of day. **The calendar would have let the desk sit through it unbracketed.**

## §2 · Dated brackets beyond 48h, carried so they are not re-derived

| Ticket | Event | Date | Observable (frozen) | Both sides |
|---|---|---|---|---|
| **T-3** | Jackson Hole — Warsh's first speech as Chair | **08-27** | `DGS30` **and** `T10YIE` `[FRED]` at the **first observation where BOTH carry 08-28** | **A** `DGS30 ≥ 5.31` ∧ `T10YIE ≤ 2.38` · **B** `DGS30 ≤ 5.10` ∧ `T10YIE` 2.28–2.40 (`S120`) |
| **T-4** | July PCE | **08-28** | *(no new ticket — see §4)* | — |
| **T-5** | Shell's $8bn US chemicals sale | by **09-30** | a **definitive agreement naming buyer and price**, ≥2 outlet bodies | **A** `XOM` is the buyer ⇒ its 🔴RESOLVED *control* status is falsified · **B** non-`XOM` or no agreement (`S122`) |
| **T-6** | **Canada's retaliatory tariffs TAKE EFFECT** | **09-08** | equal-weight **Industrials** 5-session excess vs `SPY`, **09-05 → 09-12** (straddling the date) | **A** ≤ **−3.10pp** (−2.0σ) · **B** ≥ **+0.44pp** (`S123`) |

⚠ **T-3 carries an observation-lag clause written INTO the row** (`D333-KR`): the H.15 family publishes
**≥1 business day behind** `T10YIE`, which is exactly why `S102` has sat unsettled for five runs. The
row settles on the first observation where **both** series carry the date, and that rule is frozen at
registration rather than discovered at settle.
⚠ **T-6 exists because `P92` and `P93` both settle 08-28 — ELEVEN DAYS BEFORE the tariffs they measure
take effect.** They can measure the announcement; nothing on the board reached the implementation
until today.
⚠ **T-6 is correlated with `P93`.** If both A-branches fire that is **one** compounding object measured
twice, not two independent confirmations. Registered so it is not double-counted.

## §3 · Cycle-GAP core starter — **NONE WRITTEN, and the ✅ is downgraded**

`cycle_exposure.py` prints **✅ no GAP** (AI-compute epicenter **16.4%** ≥ 12.0% · Energy/refining
**10.0%** ≥ 8.0% · Missile-defense 3.83%, **no threshold set**).
🚫 **No starter ticket is written** — no rank≤2 cycle is at zero, so the standing rule (*a 🔴 tape
gates ADD timing, never zero core*) is **not invoked** today.
🚨 **But PREMORTEM Lens 4 downgraded the ✅ to ⚠ UNDER-DETERMINED and this file carries the downgrade:**
1. The **optical/interconnect** cycle has **no registry row** (`D250`/`M731`, 4th run) ⇒ `LITE`/`COHR`/
   `CIEN` exposure is **unmeasurable, not zero**.
2. The rank-1 **16.4%** is computed over a label spanning **2–3 measured risk units** at `--days`
   250/500/750 (`D329`) — one number over an inconsistent unit.
3. **Missile-defense has no threshold, so rank 3 can never flag**, and **`RTX`'s customer has been
   unmeasured for 207 days** (`W4`).

## §4 · Tickets deliberately NOT written, with reasons

| Not written | Why |
|---|---|
| **July PCE 08-28** | **08-28 already carries SEVEN pre-registered rows** (`P67` `P81` `P85`–`P89` `S116`) plus `FRO` earnings. An eighth adds no information and would inflate apparent coverage. ⇒ **`S121` was graded, dropped, and its ID consumed unused** so it cannot be silently re-allocated. ★ The finding it produced instead: **date-clustered rows resolving together read as seven confirmations from n ≈ 1** (`B3`) |
| **Any entry ticket on a DEEP-sector name** | The mandate is analytical-only, and separately **BET handed forward zero candidates** — `MRK`, `MRVL`, `MSTR`, `FCX` all went to the ledgers, not to a list |
| **`FRO` 08-28** | `S109` is already armed. ⚠ **`FRO` is outside `us_top300`** — the desk brackets a name it cannot flow-tag (`D341`) |
| **Any size, anywhere** | P4, and this run's explicit mandate |

---
*Analytical / scheduling artifact. Pre-committed conditionals only — zero buy/sell advice, zero
position sizing, and no order is sent by anything in this file.*
