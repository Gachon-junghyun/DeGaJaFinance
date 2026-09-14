# ACTION_TICKETS — 2026-08-14 · written by `industry_US` stage 10 (L1·ALPHA)

> **Analytical / scheduling artifact — zero buy/sell advice.** Tickets are **pre-committed
> conditionals**; no order is sent, and execution would be a separate human
> `module_kis --order … --execute`. **This desk issues none (P4).**
> ⚠ **`scripts/action_bracket.py` output is superseded by this file** — see §0.

## §0 · 🚨 The script returned a FALSE NEGATIVE, and the cause is not the one `D155` names

`python -X utf8 scripts/action_bracket.py` (23:1x KST) printed:

> *"No tickets — no cycle GAP and no dated binary in window."*

**Both clauses are literally true and together they are analytically wrong.**

| Clause | Literally | Analytically |
|---|---|---|
| *"no cycle GAP"* | ✅ correct — `cycle_exposure` returns ✅ (AI-compute 16.68% ≥ 12.0%, Energy 11.1% ≥ 8.0%) | ⚠ **the ✅ rests on 2 armed tests of 3** (rank-3 floor is `0.0` ⇒ OFF), over **~82% of the book** (`HPE`·`MET`·`NDAQ`·`NUE` map to no cycle), on a **28-day-old registry with no entry for either cycle this run found** (`PREMORTEM §4`) |
| *"no **dated** binary in window"* | ✅ correct — `CATALYST_WATCH.json` carries **one** binary and its `"undated": true`, `"days_until": null` | 🚨 **there IS a binary and the protocol makes a both-sides bracket MANDATORY for it.** The script filters on a date the event does not have, so **an un-dated binary is invisible to the desk's own ticket generator** |

★ **This is NOT `D155`.** `D155` describes a silent false negative on runs crossing **local midnight**;
this run started **22:10 KST** and this call ran at **23:1x KST — before midnight**, so that path is
not implicated. **The cause here is `undated: true`, which is a different and previously unrecorded
filter hole.** ⇒ registered **`D263`**: *`action_bracket` should emit an **undated-conditional**
ticket (trigger-on-occurrence, no settle date) rather than dropping the row — a binary without a date
is exactly the kind the desk most needs pre-committed, because it cannot be diarised.*

## §1 · The mandatory both-sides ticket, written by hand because the script dropped it

**Binary**: *Iran "Strait of Hormuz open" statement (TACO trigger)* · axis **oil** · **UNDATED** ·
confidence `watch` · source note: *"ceasefire collapsed 2026-07-10, strikes on vessels resumed."*

**Pre-committed observable — `S84`** (registered this run, `BLINDSPOT_PREMORTEM §5`):
`[XLE 5-session excess vs SPY] − [EW{XLU, XLRE} 5-session excess vs SPY]`, settled closes, **`SPY`
named inline (C1)**. **State at registration: +3.880.**

| Side | Trigger | What it says · what it hits |
|---|---|---|
| **AGAINST US** | spread **≤ −3.174** at the 2026-08-21 settle (measured p15, base rate **15.1%**) | De-escalation ⇒ **ENRG's only positive `wflow` compresses WHILE the duration underweights rip.** One headline hits **ENRG OW−** and helps **UTIL UW · RE UW · STPL UW− · IT N+** — five tilts, one tick |
| **WITH US** | spread **≥ +5.544** (measured p95, base rate **5.2%**) | Escalation extends a premium already sitting **at its own 252-day 85th percentile** |
| **NEITHER** | between | Modal (~80%). No conclusion changes |

- **Settlement mode stated (`D242`'s remedy)**: **TERMINAL bar only, both sides.**
- **Branch B is at p95 rather than p85 and the reason is disclosed**: the state **+3.880** already sits
  **at p85 (+3.899)**, so a p85 branch would fire on **no move** — the `D122` zero-information class.
  **The 15.1% / 5.2% asymmetry is stated, not hidden.**
- **Invalidation**: a **non-Hormuz** energy event dominating the window (OPEC emergency meeting, SPR
  action), evidenced by a filing or two independent outlets ⇒ **`AMBIGUOUS`**, not scored.

⚠ **Sizing: none.** **G6 FAILED (estimate accrual 2.4× slow)** ⇒ any size this desk wrote today would
be labelled **"mechanical ¼"**, and **G4 FAILED** (11/10/10 units at 250/500/750d) ⇒ **no
single-number concentration guard exists to size against.** **No ticket below carries a share count.**

## §2 · Cycle-exposure tickets — none, and the reason is recorded rather than assumed

**No GAP ⇒ no epicenter-starter ticket.** ⚠ Recorded so a later run can tell *"no gap"* from
*"no registry"*: the two cycles this run actually found — **optical/interconnect** (`COHR` `LITE`
`CIEN`, holding 2 of the desk's 6 admissible 🟢) and **custom AI silicon / Maia 300** (a named product,
a September window, a 300,000-unit target) — **are not entries in `data/cycles/cycle_registry.json`**,
so `cycle_exposure` **cannot** report a gap against either. **Registry curation is a human item (P5).**

## §3 · Dated settles the next runs inherit

| Date | Rows |
|---|---|
| **2026-08-19** | `S75` (ENRG) · `S76` (HLTH) · `S77` (MATR) · `S78` (FIN) · `S80` (UTIL/RE/STPL) |
| **2026-08-20** | `S82` (HLTH vs duration) · `S83` (ANET−HPE) |
| **2026-08-21** | ★ `S84` (Hormuz spread) · `S85` (IT promotion falsifier) · `S86` (optical) · `S87` (runners) — **all four registered today** |
| **2026-08-24** | `S74` (Hormuz reopening, undated-or-first-occurrence) |
| **2026-08-26/27** | `NVDA` print · `S79` · `S81` |

**Nothing settles between 2026-08-14 and 2026-08-18.**
