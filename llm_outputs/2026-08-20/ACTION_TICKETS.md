# ACTION_BRACKET — 2026-08-20  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,390,404원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** NVDA earnings (D-6, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — hand-written both-sides brackets (`industry_US` ALPHA, 2026-08-20)

> 🚨 **Read this before reading the empty ticket list above.** The script printed
> *"**Nearest binary:** NVDA earnings (D-6, axis=earnings) — both-sides armed below"* in its header
> and *"No tickets — no cycle GAP and no dated binary in window"* in its body. **Those two lines
> contradict each other and the second one is the artifact.**
>
> **Cause (`D294`, second consecutive run, unchanged):** `data/catalysts/branch_map.json →
> axes.earnings` holds **placeholder prose** (`"<the reporting ticker> continuation add"` /
> `"<avoid / opposite-leg>"`); `_first_clean()` accepts only tokens matching `isalpha ∧ len≤5 ∧
> isupper`, so both branches resolve to `None`, the ticket list empties, and the empty-list message
> fires. **A single-name earnings binary can NEVER produce a ticket** until a human populates that
> axis. Its `asymmetric` field is prose too, so `is_asym` can never be True. **Repair is a
> human-approval item (P5); this addendum is the workaround, not the fix.**
>
> **⚠ An empty machine section here does NOT mean nothing was due.** It means the script cannot
> express what was due.

## Ticket state, stated plainly

- **Cycle GAP: NONE.** `CYCLE_EXPOSURE` clears every rank≤2 cycle (AI-compute epicentre **19.78%** vs
  a 12.0% floor; Energy **9.89%** vs 8.0%). ⇒ **No tape-independent core-starter is owed, and none is
  written.** ⚠ Three caveats travel with that clear, all re-confirmed by PREMORTEM Lens 4:
  the any-layer figure is **under-counted** (`M731` — `LITE` `COHR` `HPE` `T` `NUE` are absent from
  the registry); **rank-3 has no floor so it cannot fail**; and **optical/interconnect has no registry
  row at all**, so two real-book holdings sit in an **unmeasurable**, not a zero, cycle.
- **Binaries in window: 3.** `NVDA` earnings **08-26** (D-6) · **July PCE 08-28** (D-8) · the
  **undated** Iran/Hormuz statement (19th run).
- **No binary lands ≤48h**, so the protocol's mandatory-bracket clock did not trigger. It triggered on
  a **gap** instead: **PCE had no bracket anywhere on the board.**

## The both-sides brackets, pre-committed (analysis → conditional; a human executes, never the desk)

| # | Binary | Date | **Branch A** | **Branch B** | Observable is frozen in |
|---|---|---|---|---|---|
| **T1** | **July PCE** | **08-28** (settles 08-31) | `T10YIE` 2-obs change **≥ +3.0bp** ⇒ the print reprices **inflation compensation**, and the desk's "the whole 10y move is real yield" frame — which underwrites `P77`, `P78` and the UTIL/RE underweights — is measuring the wrong variable | **≤ −3.0bp** ⇒ compensation falls again; the real-yield frame survives | **`S104`** (D93: mean −0.07bp, sd 2.60, p10/p90 = ±3.0 ⇒ A ~10% · B ~10% · C ~80%) |
| **T2** | **`NVDA` earnings** | **08-26** *(⚠ see date note)* | *(the print itself)* | *(the print itself)* | **`S79`** (name) · **`S81`** (readthrough, deliberately excluding `NVDA`) · **`S103`** (cycle) — **already three-way bracketed; a fourth was DECLINED on information content (B4)** |
| **T3** | **`NVDA` readthrough to the held basket** | settles **08-25, one session BEFORE the print, by construction** | `EW{AVGO,ANET,HPE,COHR,LITE}` exc5 vs `SPY` **≥ +8.02** (252d p85) ⇒ the 0.8th-percentile reading was a positioning flush | **≤ −7.72** (252d **p05**) a second time ⇒ two consecutive p05 weeks; the theme's multiple is being reset | **`P79`** — deliberately pre-print so it scores **carry**, not an event |
| **T4** | Iran / Hormuz (**undated**) | — | — | — | **`S92`** · **`S95`** cover the expiry. 🚨 **`S8` remains undated and unscoreable for an 18th run — a human must `VOID` it or date it (P5)** |

## Two obligations that are UNMET and are recorded as unmet

1. 🚨 **`D295`** — **`S103`'s ±5.0pp bands are hand-set** because the nearest readable option chain
   expires **2026-08-21**, five sessions before the event. The rule requires re-derivation from an
   **08-26-or-later straddle before the print**. **Not done this run.** Every straddle readable today
   is `D1` (08-21): `NVDA` **±1.9%** · `AVGO` ±2.2% · `MRVL` ±5.3% · `COHR` ±6.1% · `MPC` ±3.4% ·
   `TGT` ±2.3% · `WMT` ±2.0% · `XLU` ±0.9% · `XLV` ±1.6% · `XLK` ±1.9%. **A D1 straddle prices one
   session ⇒ a FLOOR, not an estimate**, and none of the thresholds above is claimed to sit outside
   what is priced.
2. 🚨 **Date discrepancy on the most-bracketed binary on the board.** `catalyst_calendar`, `S79`,
   `S81`, `S103` and `P79` all key `NVDA` to **2026-08-26**; `yfinance`'s calendar returns
   **2026-08-27**. Both are consistent with an after-the-close print on 08-26, but **four rows are
   dated against one of the two readings and nothing reconciles them.** `P79` is safe under either
   (it settles 08-25); `S79` (settle 08-27) and `S103` (settle 08-29) are not obviously safe.
   **Handed to the scoring desk as a check, not silently normalised.**

## New dated catalyst this run surfaced that the calendar does not carry

★ **Belarus's Novopolotsk refinery undergoes scheduled maintenance in September** (`euronews` 08-20,
body-read). Belarus supplied a **record 212k t petrol / 162k t diesel** to Russia in July and is its
most important external fuel source; its two refineries have a combined export capacity of roughly
**2 million t/year**. **A scheduled turnaround is a structural, knowable-in-advance supply date** —
the `D13`/`D18` class `catalyst_calendar` routinely misses — and it lands directly on the ENRG OW's
mechanism. **No ticket is written for it** (no date more precise than "September"), but it is
recorded here so the next run can date it.

*Analytical/scheduling artifact — zero buy/sell advice. Every row above is a pre-committed
conditional; no order is sent by this desk, and no `--execute` flag was used anywhere in this run.*
