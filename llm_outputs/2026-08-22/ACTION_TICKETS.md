# ACTION_TICKETS — 2026-08-22 · industry_US / L1·ALPHA

> **Pre-committed conditional tickets. DRY-RUN sizes are illustrative. A human executes separately;
> this desk never sends an order.** Book total ≈ **15,272,249원** · fx 1380 · per-trade risk 1.5%
> (core 0.8%) · stop 7.0% · max position 25.0%.
> **Zero buy/sell advice (P4)** — a ticket is a *conditional*, and every one below is stated with the
> condition that must be true first.

---

## §0 · 🚨 `scripts/action_bracket.py` contradicted itself in two consecutive lines — **4th consecutive run (`D294`)**

Its output is preserved verbatim in `industry_US/_action_bracket_raw.md`. The two lines, unedited:

```
**Nearest binary:** NVDA earnings (D-4, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
```

**The header names a dated binary and the body says there is none.** The 08-21 run logged this as
`D294`'s third consecutive reproduction; **this is the fourth, verbatim.**
⇒ **The tickets below are hand-built from `BLINDSPOT_PREMORTEM §6` and `CYCLE_EXPOSURE`.** The script
produced **zero** tickets on a window containing **three binaries inside seven days**.

⚠ **And there is a second, compounding failure in the same window**: `catalyst_calendar` carries **no
row at all** for the **Jackson Hole symposium 2026-08-27 → 08-29** (`D18`, and `R93` — see
`HANDOVER §7`). **So the calendar could not have handed `action_bracket` the window's biggest event
even if `action_bracket` worked.** Two instruments failed in series, again.

---

## §1 · Both-sides brackets — one ticket pair per binary

> Every pair is derived from a bracket registered this run with **frozen** thresholds
> (`BLINDSPOT_PREMORTEM §6`). **A ticket fires on the bracket's observable, not on a price feeling.**

### Ticket pair 1 — **Jackson Hole 08-27→29 + July PCE 08-28** *(the window's largest binary, calendar-invisible)*

**Governing bracket: `S112`** — `EW{XLU, XLRE, XLP}` **3-session excess vs `SPY`**, window
**2026-08-26 close → 2026-08-31 close**. State at registration **−0.225 = 49th %ile** ⇒ both branches
equally reachable.

| | **A-side (AGAINST the desk)** | **B-side (with the desk)** |
|---|---|---|
| **Fires when** | `S112` observable **≥ +1.653pp** (252-obs p85) | `S112` observable **≤ −1.757pp** (252-obs p15) |
| **What it means** | The three underweights ripped **together** — the correlated-UW pattern (`PREMORTEM §3-d`) is real and cost the desk | The credibility story did not land; the duration repression holds and UTIL/RE/STPL stay right |
| **Conditional action (illustrative only)** | **Re-argue three sector verdicts at once before any sizing.** No add to Energy/Health Care on this branch — a duration rip is the state in which the OW pair is most likely to be a rate trade in disguise | No new action. The existing tilt is confirmed and **confirmation is not a reason to add** |
| **Invalidation** | branch C (between) ⇒ **no ticket fires**, and `P78`'s dispersion range (**7.807 today**, far past its own branch A) is the reason C is likely: the four "duration" legs are demonstrably not one leg |
| **Hard stop stamp** | n/a — **no entry is proposed on either side.** This pair is a *verdict* ticket, not a position ticket |

### Ticket pair 2 — **`NVDA` earnings 2026-08-26**

**Governing bracket: `S113`** — `SMH` **5-session excess vs `SPY`**, window **2026-08-25 close →
2026-09-01 close**. State **−3.293 = 12th %ile of 252**.

| | **A-side (AGAINST the desk's IT UW)** | **B-side (with the UW)** |
|---|---|---|
| **Fires when** | `SMH` exc5 **≥ +4.461pp** (p85) — needs **+7.75pp**, a genuine reversal | `SMH` exc5 **≤ −2.627pp** (p15) — **pre-declared LOW-INFORMATION**: the state is already below it |
| **What it means** | The UW was the wrong verdict at the 12th percentile with four names held | Nothing new — the de-rate continued through its own catalyst |
| **Conditional action (illustrative only)** | **The IT UW is falsified and must be re-argued in the next ROTATION**, with `eqflow` rank 8 vs price rank 11 as the standing evidence that it was mega-cap-led | none |
| ⚠ **Threshold provenance** | 🚫 **NOT taken from the options market, and the reason is measured**: `module_flow NVDA --positioning` returns **예상변동 ±1.6%, 만기 2026-08-24, D2 — the straddle expires two days BEFORE the print** (`D315`). The threshold is distribution-based and is labelled as such |
| **Note on `S103`** | `S103` (`NVDA` the name, 08-26) keeps its **hand-set ±5.0pp bands and is NOT re-frozen** (`D242`). `S113` is additive, on the chain |

### Ticket pair 3 — **US–Canada metals/autos tariff resolution, ≤ 2026-09-03** *(against a HELD name)*

**Governing bracket: `S114`** — `EW{NUE, STLD}` **5-session excess vs `SPY`**, window **2026-08-26 →
2026-09-03**. State **−8.628 = 3rd %ile of 252**.

| | **A-side (the tariff bid is being removed)** | **B-side (already discounted)** |
|---|---|---|
| **Fires when** | `EW{NUE,STLD}` exc5 **≤ −6.219pp** (p05) — **pre-declared LOW-INFORMATION**, it only requires the extreme to persist | `EW{NUE,STLD}` exc5 **≥ +0.826pp** (p50) — needs **+9.45pp ≈ 1.2× `NUE`'s implied move** ⇒ **WEAK-INFORMATION**, labelled |
| **What it means** | 🚩 **The `NUE` thesis needs re-argument, not re-sizing** — its live thread (peak **23 outlets**, 08-19) runs against the position | The market had priced the tariff cut and `EVENT_ALPHA` CARD 4 was wrong |
| **Conditional action (illustrative only)** | **Re-justify or retire the `NUE` thesis line in `STANDING_VIEW_US`.** No sizing implication is stated here | Close CARD 4 as refuted |
| **Implied move** | `NUE` **±8.1%, expiry 2026-09-18, D27**, `P/C` 0.79, **IV skew +36.1 — the highest downside-fear skew this run pulled**. Both thresholds are stated against it |
| **Hard stop stamp** | ⚠ **`NUE` is a held position with `vol_surge` 1.41 and `rs20` −5.2 vs `SPY`** — high volume with falling relative price. **Any action on this name requires a hard stop**, and the desk does not set one here (P4) |

---

## §2 · Cycle-GAP core starter — **not issued, and the reason is a measurement gap**

`CYCLE_EXPOSURE` reports **no top-rank GAP**: AI-compute **16.52% ≥ 12.0% ✅** · Energy/refining
**9.84% ≥ 8.0% ✅** · missile-defense **3.79%, ⚪ no floor set**. ⇒ **no tape-independent core starter
is required, and none is issued.**

🚨 **Three attacks on that ✅ are carried forward as tickets-that-cannot-be-written** (`PREMORTEM §5`):

| # | The attack | Why no ticket |
|---|---|---|
| 1 | **Rank 3 has no floor, so it cannot fail** — and its one held name (`RTX`) was tagged **ROLLING OVER** this run (`obv_norm` +0.023, left accumulation; delta −0.304) | **Setting a floor is a human parameter change (P5)**, not a desk action |
| 2 | **`cycle_registry.json` has no optical/interconnect row — 10th run** (`D250`/`M731`) ⇒ exposure there is **unmeasurable, not zero** | A ticket needs a measurable exposure %. **There is none to compare against** |
| 3 | ★★ **The AI-compute ✅ is carried at the COMPUTE layer while the week's committed capital went to POWER** — `NVDA` guaranteeing **up to $105bn** of OpenAI's Ohio leases (8-GW campus, 08-17/08-18) — and **every measurable power-layer name is 🔴**: `GEV` −0.741 · `CEG` −0.625 · `VRT` −0.539 · `NEE` −0.600 · `VST` −0.689. **`ETN` cannot be counted there** (`M778`: β`XLI` **+1.402**, t +6.12) | ⚠ **A 🔴 tape gates ADD *timing*; it never justifies zero core.** But the desk cannot state whether it *has* core exposure to that layer — the registry has no node for it. **That is a measurement gap and the honest output is the gap, not a size** |

⇒ **The one ticket that would follow is a registry edit, and the registry is human-maintained (P5).**

---

## §3 · Standing conditionals carried from earlier runs, with their dates

| Bracket | Settles | Pre-settle reading today | Ticket status |
|---|---|---|---|
| `P79` — AI-compute flush vs de-rate | **08-25** | **−5.609** (was −7.178) — moved **+1.57pp AWAY** from branch B | armed, no action |
| `S108` — the 08-21 run's "D-0 equity bracket" | **08-25** | 1 session of 3: **−0.909pp** (branch A ≥ +1.68 / B ≤ −1.76) | ⚠ **armed but its PREMISE IS VOID** — its window (08-20 → 08-25) does not contain Jackson Hole (08-27→29). **It settles as registered (`D242`) and measures nothing about the event it was built for** (`R93`) |
| `P77` — can Treasury cap the long end | **08-26** | `DGS30` **5.23** `[FRED 08-20]` — between A (≤5.18) and B (≥5.38) | armed |
| `P78` — the duration complex is a DISPERSION question | **08-26** | **range 7.807** — far past branch A (≥4.71); legs `XLV` +5.700 / `XLP` +1.252 / `XLRE` +0.948 / `XLU` −2.108 | **tracking branch A strongly** |
| `P80` — the refiners' kill has reset | **08-26** | 3-2-1 crack **69.61** ✅ ∧ EW exc5 **+3.888** ✅ | **branch A tracking on both legs** |
| `P83` — the separation, re-registered on dist−gaso | **08-27** | **48.17**, down from **51.13** on 08-20 (**−2.96 into the settle**) | armed; the spread crude cannot widen is the one that narrowed |
| `P89` · `P85` · `P86` · `P87` · `P88` — registered this run | **08-28** | see `MACRO_REPORT §D` | armed |
| `S92` · `S94` · `S104` | **08-31** | `S94`: `EW{COHR,LITE}` exc5 **−7.412** ⇒ **already inside branch B**; branch A additionally needs `vol_surge` ≥1.0 on both and **`LITE` is 0.95** | armed |
| `S109` (`FRO`) | **09-02** | 🚫 **`FRO` has no flow reading on this desk — it is outside `us_top300`** (`D314`) | armed, unmeasurable |
| `S102` | **unarrived** | FRED's `DGS2`/`DGS10`/`DGS30` still end **2026-08-20** on a third independent pull | 🚨 **handed to the 2026-08-24 run** — a Friday-dated FRED row cannot be read by a weekend desk (`D309`) |

---

## §4 · What this file does not do

- **It sends no orders.** Execution is a separate, human `module_kis --order … --execute`.
- **It proposes no position and no size.** Every "conditional action" above is a *research* action
  (re-argue, re-justify, close a card) except where explicitly marked illustrative.
- **It sets no stop** — where a stop would be required (`NUE`), it says so and does not set one.
