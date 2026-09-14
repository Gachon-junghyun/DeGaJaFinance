# SWEEP_READ — industry_US · 2026-08-14 · Stage 4/11 (L1·SWEEP)

> The **reading**, not a second copy of the data. Numbers live in `SECTOR_FLOW_US.json` ·
> `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.json` and are **cited by artifact, not reprinted**.
> Sweep `asof` **2026-08-13** (settled). Feeds ROTATION §2.

## 0 · Instrument health line, read BEFORE the numbers

`§scoring` = `{vel_axis: false, vel_coverage: 0.17, n_axes: 3, scored: 300, dropped_missing_axis: 0}`.
The sweep printed its own 🚨 line. **News axis dead for scoring — and the cause is the pipe, not
silence**: the same bridge returned 3,835 `Nvidia` hits **22 minutes after the sweep ran**
(`MACRO_REPORT.md §0`). ⇒ **`vel_coverage 17.0%` describes the tunnel at 22:12 KST, not the world.**

## 1 · Universe headline — three numbers

**n = 300 · cap-weighted `wflow` −0.152 · equal-weighted −0.089 · 11 🟢 / 221 🟡 / 68 🔴.**
The whole universe is negative on both weightings, and **`wflow` < `eqflow` ⇒ the megacaps are
dragging harder than the median name.** Only **one of eleven sectors** carries a positive `wflow`.

## 2 · 🚨🚨 THE FINDING — **5 of the 11 🟢 tags cannot be produced by the 3-axis rule**

The `scoring` block says the **score** is 3-axis. It does **not** say the **tag** is. Decomposed:

| 🟢 name | Reproducible from OBV ∧ RS20>0 ∧ vol_surge≥1.2? |
|---|---|
| COHR · KKR · ABNB · LITE · MPC · ALL | ✅ **yes** — all six clear `vol_surge` 1.26–2.12 |
| **CSCO · DELL · CVX · NVDA · BAC** | ❌ **NO.** `vol_surge` 1.26 / **0.78 / 0.93 / 0.76 / 0.73**, and **`CSCO`'s RS20 is −0.1, i.e. NEGATIVE.** Each of the five carries a **velocity** value (2.44 / 1.41 / 1.24 / 1.27 / 1.71) and **only the velocity axis can be lighting them** |

★ **So `flow_score` is 3-axis while `flow_tag` is 4-axis, and nothing in the output says so.**
`dropped_missing_axis: 0` is true **of the score** and tells the reader nothing about the tag.
★★ **The enrichment is not marginal.** Velocity exists for **51 of 300 names (17%)**. If greenness
were independent of coverage you would expect **11 × 0.17 ≈ 1.9** greens carrying velocity.
**Observed: 5 — a 2.6× over-representation.** ⇒ **the green list is disproportionately drawn from the
survivor sample of a failing tunnel**, which PREFLIGHT G1 explicitly revoked as non-random.

🚨 **And it reaches the sector call.** `NVDA` is one of the five. `NVDA` is also the G3 flipper that
**owns Information Technology's sign** (`wflow +0.016`, ex-top1 **−0.078**). ⇒ **the board's only
non-Energy positive sector reading traces, through one name, to an axis this run has revoked.**

**Binding, handed to ROTATION**: the five names are **🟡, not 🟢, for every purpose in this run** —
they may not be counted in a green tally, cited as ignitions, or used as breadth evidence. The
shortlist's own header count of "11" is therefore **6** on admissible axes. Registered **`D261`**.

## 3 · Cross-checks against the MACRO matrix — two confirmations and two contradictions

**✅ CONFIRMS — Utilities / Real Estate (P56-A).** UTIL `wflow −0.491` with **0🟢 / 9🔴 of 15**;
RE `−0.252`, breadth 0.00. The two sectors MACRO put on long-end pressure are the two the sweep finds
with no internal support at all. The money and the matrix agree.

**✅ CONFIRMS — Materials is one name (P59).** `wflow −0.179` flips to **+0.016 without `LIN`**
(G3 flipper, 24.7%), breadth **0.00**, 0🟢/4🔴 of 12. Same conclusion the ex-NEM basket reached from
the price side, reached independently from the flow side.

**❌ CONTRADICTS — Energy: the sweep is long the WRONG HALF of the sector.** `wflow +0.259` is the
board's only positive, but `eqflow` is **+0.099** — i.e. **the positive is cap-weighted into the
integrateds** (`XOM` alone is 30.5% of sector cap). MACRO's tape read (§C-3) says the move is the
**crack**, and the refiners lead RS20 (`MPC +12.9 · PSX +11.9 · VLO +10.6`) while `XOM` reads **+5.1**.
⇒ **`wflow` and the crack point at different companies.** The tape is the better instrument here
because `wflow`'s weights are **30 days stale** (G5).
⚠ **And Energy's `delta` is −0.157, the board's second worst** — the only positive sector is also the
one losing flow fastest session-over-session.

**❌ CONTRADICTS — Financials' "breadth-led" label, carried for weeks, has INVERTED.**
`wflow −0.066` vs **`eqflow −0.144`** ⇒ **the median financial is now WORSE than the cap-weighted
sector**, the opposite of the M40 shape (eqflow +0.320 > wflow +0.253) this desk carried since 07-23.
3🟢/9🔴 of 47. ⇒ **any Financials thesis resting on breadth needs re-justification, not carry.**

⚠ **One more the JSON alone would hide — Information Technology's two breadth measures disagree.**
`eqflow +0.034` > `wflow +0.016` says *"the median name is doing better than the megacaps"*; the
**count** says **5🟢 / 10🔴 of 56, breadth 0.09 — twice as many reds as greens.** Both are "breadth".
⚠ **G3 bars any `wflow`-based promotion or demotion for IT, HLTH and MATR this run.**

## 4 · Shortlist composition — the ABSENCES, diagnosed before they are cited

11 names, **four sectors only**: IT 5 · FIN 3 · ENRG 2 · DISC 1.
**Seven of eleven sectors produced ZERO**: HLTH · INDU · MATR · UTIL · RE · STPL · COMM.

**Diagnosis — is the absence evidence or a filter artifact? Both, and they must be separated:**
1. **Not a market-cap-floor artifact.** Those seven sectors have a literal **0 🟢 count** in
   `§sector_rotation`; the $10B floor never binds because there is nothing to filter.
2. **But the 🟢 gate itself is compromised twice over.** (a) §2 above — 5 of the 11 that *did* pass
   are lit by a revoked axis. (b) The gate's third conjunct is **`vol_surge`**, and `vol_surge` is
   **the one axis with a Bonferroni-clearing IC on this repo's ledger — with a NEGATIVE sign**
   (h=1 t −3.20 · h=5 t −2.90, `HANDOVER.md §3e`), while `sector_flow` weights it **positively**.
   ⇒ **a name can be excluded from the shortlist by the axis whose measured sign says it should have
   been included.** ⚠ **W1/R3: that IC is measured on the KR ledger and there is no US column
   (`D243`)** — it is a reason to distrust the gate, not a licence to invert it.
3. ★ **ENRG reproduces the 2026-07-21 precedent exactly, and it is the cleanest instance yet.**
   **`PSX` (flow +0.637, OBV 매집, RS20 +11.9) and `VLO` (+0.639, 매집, +10.6) are both 🟡 — blocked
   by `vol_surge` 1.04 and 0.95.** The two names the tape says are leading the sector are **filtered
   out of the sector's own shortlist by a volume test.** Meanwhile `CVX` (RS20 **+3.9**) is on the
   list — via velocity, i.e. via §2's revoked axis. **The ENRG shortlist inverts the sector's own
   ranking.**

⇒ **The seven zeros are real as measured, and the measure has two named defects.** No stage may read
"no shortlist name in sector X" as "no money in sector X" this run.

## 5 · Held-but-not-in-universe · cycle GAP

✅ **11/11 US holdings are inside `us_top300` AND scored** (G5) — zero held-but-unmeasurable names,
third consecutive run. The `LNG`/`TSM` hole stays closed.
⚠ **Book tags, for ROTATION**: only **`MPC` and `NVDA`** are 🟢 among the eleven — and **`NVDA`'s
green is one of the five §2 disqualifies**, so on admissible axes **the book holds exactly ONE
🟢 name.** Largest positive deltas: `AVGO +0.300`, `NVDA +0.195`; largest negative: `NDAQ −0.288`,
`MET −0.174` (`MET` also just fired `S69` branch A).

✅ **`cycle_exposure`: no GAP** — AI-compute **16.68%** vs a 12.0% floor (`AVGO·NVDA·ANET`), Energy
**11.1%** vs 8.0% (`MPC·PSX`). Rank-3 (missile-defense, `RTX` 5.7%) is **⚪ n/a — its floor is `0.0`,
i.e. the check is silently OFF**.
⚠ **`R66` binds and is unchanged**: `HPE` is **not in the epicentre registry**, so the 16.68% is
understated by an unknown amount, and **four holdings (`HPE`·`MET`·`NDAQ`·`NUE`) map to no registered
cycle at all** ⇒ the ✅ is computed over part of the book, on a registry **28 days old** whose
`core_pick_why` still quotes **`R8`, a retracted claim**. **The ✅ is a pass on 2 armed tests, not 3.**

## 6 · What this stage hands to ROTATION

1. **The 🟢 count is 6, not 11** (§2) — and **`NVDA`'s green is disqualified**, which matters because
   `NVDA` also owns IT's `wflow` sign.
2. **G3 bars `wflow` promotion/demotion for IT · HLTH · MATR.**
3. **Energy: `wflow` and the tape name different companies** — use the crack/RS side, not the cap side.
4. **Financials' breadth premium has inverted** (`eqflow` < `wflow`); the carried label is stale.
5. **Seven sectors produced no shortlist name, and the filter is defective in two named ways** — the
   absences are reportable, but not as evidence of absent money.
