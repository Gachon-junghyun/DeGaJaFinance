# ACTION_BRACKET — 2026-08-19  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,491,902원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** NVDA earnings (D-7, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---

# ADDENDUM — ALPHA stage (Stage 10/11), industry_US, 2026-08-19 KST 00:0x

> **Append-only.** The block above is `action_bracket.py`'s own output, unedited. This addendum records
> (a) why that output is internally contradictory, (b) what the calendar actually holds, and (c) the
> both-sides bracket the script could not emit. **Zero buy/sell advice, zero size (P4).**

## 1 · 🚨 The script's two lines contradict each other, and the cause is measurable

The header says **"Nearest binary: NVDA earnings (D-7) — both-sides armed below"**; the body says
**"no dated binary in window."** Both were rendered by the same run. Diagnosed this stage:

- `action_bracket.py` finds `near` correctly (NVDA, `axis="earnings"`, `days_until=7`) and prints it.
- It then looks up `data/catalysts/branch_map.json → axes.earnings`, which exists but whose branches
  hold **placeholder prose, not tickers**: `A_beat = ["<the reporting ticker> continuation add"]`,
  `B_miss = ["<avoid / opposite-leg>"]`.
- `_first_clean()` accepts a token only if `isalpha() and 1 ≤ len ≤ 5 and isupper()` ⇒ both branches
  return `None` ⇒ **zero tickets appended** ⇒ the "no dated binary" line fires on an empty ticket list.
- The same axis's `asymmetric` field is prose (`"confirm-then-enter (no front-run of a single-name
  binary)"`) rather than a branch key, so `is_asym` can never be `True` either.

⇒ **A single-name earnings binary can never produce a ticket from this script, by construction.** The
*intent* is defensible — the map is literally telling the desk not to front-run a single-name print —
but it renders as **"there is no binary"**, which is a different statement and a false one.
**This is the silent-zero class the whole PREFLIGHT protocol exists for: the tool returned a plausible
output, threw nothing, and said the opposite of what it had just measured.**
Filed to the carry as a dig; **editing `branch_map.json` or the renderer is a human call (P5).**

## 2 · What the calendar actually holds — and the ≤48h rule does NOT bind this run

`catalyst_calendar.py --days 10` (run at the 10-day window deliberately, per D26 — the 5-day default
would have shown **none** of these):

| When | Event | Axis | Source tag |
|---|---|---|---|
| **D-7 · 2026-08-26** | **`NVDA` earnings** | earnings | 🔀 binary |
| **D-9 · 2026-08-28** | **July PCE** (Personal Income & Outlays) | inflation | 🔀 binary `[bea~est]` — ⚠ `~` = pattern-estimate, not an official confirmation |
| undated | Iran "Strait of Hormuz open" statement (TACO trigger) | oil | 🔀 binary `[news👁]` |
| — | STRUCTURAL (lockups / index rebalance / conversions) | — | **none in window** — `data/catalysts/structural_schedule.json` is human-maintained |

⇒ **Nearest dated binary is D-7. There is no binary ≤48h**, so the protocol's hard rule — *"any binary
≤48h ⇒ PREMORTEM must produce a both-sides bracket"* — **is not triggered this run.** Stated explicitly
so that a future reader does not read the empty ticket list as a skipped obligation.

⚠ **But the 08-21 settle cluster is inside 48h and is already fully bracketed**: `S99` · `S100` · `S102`
settle **2026-08-21**, `S98` on **08-20**, `S101` on **08-26** — all registered both-sided in
`BLINDSPOT_PREMORTEM §6`, all frozen, all implied-move-checked. **Nothing in this window is one-way.**

## 3 · The bracket the script could not emit — `NVDA` 2026-08-26, written by hand

**Why it must exist despite the "don't front-run" intent:** `NVDA` is **15.60% of invested capital,
the book's largest single position** (live real-book read, 23:52 KST). A both-sides bracket on a
position that size is not a front-run — **it is the pre-commitment that stops the desk deciding after
the fact.** The map's caution applies to *opening* a new leg into a print, not to declaring in advance
what each branch would mean for a leg already held.

| | **Branch A — beat** | **Branch B — miss** |
|---|---|---|
| **Trigger** | `NVDA` 5-session excess vs `SPY`, **08-25 close → 08-29 close**, **≥ +5.0pp** | same window, **≤ −5.0pp** |
| **What it means** | The AI-compute epicenter re-accelerates; the registry's **19.82%-of-total** epicenter reading is *understated* by the three unlabelled chain names (`LITE` `COHR` `HPE` = **14.75% of total**, `BET_SHEET §F`) ⇒ true exposure ≈ **34.6% of total** into a re-accelerating cycle | The same understatement runs the other way: the book is **~15pp of total assets more exposed than any artifact prints** ⇒ the concentration question the desk has been unable to state as one number (G4) becomes the live one |
| **Which desk belief it falsifies** | the "AI-compute is fully accounted at 19.82%" reading that the ✅ GAP flag implies | ★ `S99`'s premise that `ETN` is or is not a *5th* AI unit — under B the count that matters is not 4 or 5 but **7 of 12** |
| **Pre-registered state** | `NVDA` settled 08-18: `flow_score` **+0.111**, tag 🟡중립, OBV **중립**, **RS20 +3.4 / RS60 −3.2 vs `SPY`**, `vol_surge` 0.72, two-session Δ **−0.347** — i.e. **the largest position enters its own print on the weakest flow reading of any book name** | (same row — one state, two branches) |
| **C (no-decision)** | −5.0pp < excess < +5.0pp ⇒ the print did not move the cycle. **Declared now, before the fact.** | |
| 🚨 **Anti-signal ⇒ VOID** | an index-level shock (`SPY` 08-25→08-29 beyond ±3%), a guidance withdrawal or M&A at `NVDA`, or an export-control announcement inside the window — none of which would be the print | |

⚠ **Threshold provenance, stated rather than assumed**: ±5.0pp is **hand-set**, not taken from the
straddle — `NVDA`'s 08-26 chain is **outside the nearest expiry this stage could read (2026-08-21, D2)**,
so no implied move governs it yet. **This is exactly the weakness `S100` fixed by moving its bands onto
the measured implied move.** ⇒ **Re-derive this threshold from the 08-26-or-later straddle at the
2026-08-20 or 08-21 run, before the print.** Recorded as an open item, not as a finished bracket.

## 4 · Core-starter — **none required, and the reason is not "the book is fine"**

`CYCLE_EXPOSURE` reports **✅ no top-rank cycle GAP** (AI-compute epicenter 19.82% vs need ≥12.0%;
Energy/refining 9.64% vs ≥8.0%; missile-defense 5.97%, no threshold set) ⇒ **no tape-independent
core-starter is owed by the pre-mortem this run, and none is written.**

⚠ **`BET_SHEET §F` measured why that ✅ is weaker than it looks**: **5 of the 12** real-book US names are
absent from `data/cycles/cycle_registry.json` entirely — `LITE` ✗ `COHR` ✗ `HPE` ✗ `T` ✗ `NUE` ✗.
Three of them (`LITE` `COHR` `HPE` = **$1,682.76 = 23.93% of invested / 14.75% of total**) are
AI-compute-chain names by the desk's own labelling elsewhere. **Under-counting cannot manufacture a
false ✅** — the flag stays conservative in the safe direction — **but the printed exposure number is
understated by ~15pp of total assets and nothing downstream would see it.** No action follows (P4).

## 5 · Sizing — **no share count is computed in this addendum, and that is a rights decision**

The block above carries the script's mechanical risk model (1.5% per trade, 0.8% core, 7% stop, 25%
max position). **This addendum adds no share counts**, for two independent reasons already on the record
this run:

1. **PREFLIGHT G6 FAILED** — the estimate-snapshot accrual runs at **≈76-day ETA against an ideal 30
   (2.6×, limit 1.5×)** ⇒ `kelly_size --ic` may not be reported as an evidence-backed size.
2. **The exposure state contradicts its own band** — `exposure_rule show` reads state `정상` while the
   band deviation reads **−14.0pp**, on an **unsettled `live` row at n=9**. A correction there is a
   **human call (P5)**, and sizing against a target the desk cannot verify is how a number gets
   invented.

⇒ **Every ticket above is a condition and a meaning, not a quantity.** A human converts conditions to
quantities, separately, with `module_KIS --order … --execute`.
