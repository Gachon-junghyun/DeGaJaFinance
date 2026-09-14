# ACTION_TICKETS — 2026-08-06 (conditional DRY-RUN tickets · a human pulls every trigger)

> Weaves `CYCLE_EXPOSURE` (gap → core) + `CATALYST_WATCH` (binary → both-sides) + the risk model +
> the live KIS read. Book total ≈ **15,015,603원** · fx 1380 · per-trade risk 1.5% (core 0.8%) ·
> stop 7.0% · maxpos 25.0%.
> ⚠ **DRY-RUN. No order is sent by anything in this pipeline. Sizes, where they appear, are
> illustrative only; execution is a separate human `module_kis --order … --execute` step.**
> **Analytical artifact — zero buy/sell advice (P4).**

---

## 0 · 🚨🚨 `action_bracket.py` produced ZERO tickets and its own output contradicts itself — **D155, third occurrence**

The script's verbatim output:

```
**Nearest binary:** CEG earnings (D-0, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
```

**It names a D-0 binary and then reports that no dated binary is in the window, in consecutive
lines.** `CATALYST_WATCH.json`, written by this same run at 09:1x ET, carries **seven** binaries
(CEG 08-06 · LNG 08-06 · NFP 08-07 · VST 08-07 · CPI 08-12 · PPI 08-13 · the undated Hormuz
statement).

★ **This is exactly the defect `D155` documents — a silent false negative on any run that crosses
local midnight** — and this run did cross it (started **09:11 ET 2026-08-06**, this stage writes
after **00:00 KST 2026-08-07**). **The 08-04 run recorded the same failure on the same clock shape
(it reported "no GAP and no binary" against a live GAP and 11 binaries).** ⇒ **third documented
occurrence, and the first where the contradiction is visible inside a single output block.**
**Needs a human — it is a date-arithmetic bug, not a data problem.**

⇒ **The tickets below are written BY HAND from `CATALYST_WATCH.json` and
`BLINDSPOT_PREMORTEM.md §1`, because the generator could not.** Every one is a **pre-committed
conditional** with a frozen observable — the same discipline the script would have applied.

---

## 1 · Both-sides brackets, one per binary — **each already registered in `handoff/SCENARIOS_US.md`**

> **No ticket below is a recommendation.** Each states, in advance, *what observation would change a
> conclusion* — so that the outcome is scoreable rather than narrated after the fact.

### T1 · CPI 2026-08-12 → **S63** · the highest-leverage bracket on the board

| | |
|---|---|
| **Frozen observable** | `DUR = (XLU RS20 + XLRE RS20)/2 − XLF RS20`, all vs **SPY**, settled closes |
| **Anchor (08-05 settled)** | **−6.197** (XLU −7.02 · XLRE −0.89 · XLF +2.24) |
| **A — against us** | **DUR ≥ −3.3** at the 08-13 settle ⇒ **UW Utilities + UW Real Estate + OW Financials are ONE duration bet sized as three** |
| **B — with us** | **DUR ≤ −9.2** |
| **C** | −9.2 to −3.3 (~70%, modal) |
| **Bands** | D93-measured: 6-session change mean −0.15, sd **2.88**, p15 −3.01 / p85 +2.94 |
| **Implied-move check** | XLU **±0.9%**, XLF **±0.8%** (D1). ⚠ **No XLRE straddle exists and none is invented (C3).** A ~2.9pp composite move cannot be produced by either single implied move ⇒ **both lines carry information** |
| ⚠ **Live objection, logged same-run** | **DEEP-INDU: yields are FALLING while XLU is worst-on-every-axis** ⇒ **the UTIL leg may not be behaving as duration at all.** **S63 is NOT re-frozen** (frozen is frozen); the objection is recorded as an annex so branch A cannot later be read as proof of a duration mechanism it may not have |

### T2 · NFP 2026-08-07 → **S65** · the bracket on this run's own tilt change

| | |
|---|---|
| **Frozen observable** | **median RS20 vs SPY of {JPM, BAC, WFC, BRK-B}**, settled closes |
| **Anchor (08-05 settled)** | **+3.405** (JPM +5.38 · BAC +5.22 · WFC +0.95 · BRK-B +1.59) |
| **A — against us** | **≤ +0.34** at the 08-11 settle ⇒ the breadth that carried today's OW promotion was **a news count** |
| **B — with us** | **≥ +6.81** |
| **Bands** | D93 on the **correct 4-session horizon** (mean +0.11, sd **3.44**, p15 −3.06 / p85 +3.41) — **widened against the lens that proposed a 3-session sd** |
| **Implied-move check** | JPM **±1.2%**, XLF **±0.8%** (D1) ⇒ a ±3.1pp four-name-median move needs correlated bank movement, outside any single straddle ✅ |
| 🚨 **Named in advance** | **BRK-B reports 2026-08-09, inside the window.** S65's own invalidation clause covers it (*"a BRK-B-specific disclosure ⇒ VOID"*). ⚠ **And BET §B-FIN corrected the companion diagnostic: the +3.405 → +5.219 ex-BRK-B jump is an n=4 estimator artifact — removing WFC gives +5.22 identically.** Do **not** read branch A as "BRK-B did it" |

### T3 · crude path → **S64** · the falsifier for the Industrials mechanism

| | |
|---|---|
| **Frozen observable** | **XLI FORWARD 6-session excess vs SPY**, 08-05 → 08-13 |
| **A — against us** | **≤ −1.8pp** ⇒ **M91's fuel-tailwind leg falsified on a second observation**; OW− Industrials loses the mechanism MACRO §G names for it |
| **B — with us** | **≥ +1.9pp** |
| ⚠ **D122 guard, stated at registration** | the **trailing** 6-session excess is **−1.790**, sitting exactly on branch A's line — **that is NOT the observable** |
| **VOID** | **WTI settled 08-13 ≥ 75.22** ⇒ the discriminating tick never arrived; **do not score it** |
| ⚠ **Prediction on the record** | **DEEP-INDU predicts S64 settles NULL**, on primaries: UNP FY2025 surcharge revenue **−$218M** vs fuel expense −$84M = **−$134M net**; NSC −$134M vs −$55M = **−$79M net** ⇒ **the full-year net sign is NEGATIVE**, ~96%/89% contractually offset. **Recorded before the settle** |

### T4 · CEG (08-06) · VST (08-07) — **pre-declared NO-INFORMATION bands, not a ticket**

**Deliberately not bracketed** (third consecutive drop, same reason): S24/S35/S47/S40 own the
AI-power print cluster and **S62 settles 08-07 explicitly including these two prints**; neither
branch changes UW Utilities, which the sweep confirms **unanimously (0🟢 / 12🔴 of 15, wflow and
eqflow both ≈ −0.4)**.
★ **But `EVENT_ALPHA` Card 3 pre-registered its own kill — *"CEG/VST guiding contracted demand UP ⇒
the card is wrong"* — and it fires in the next 24h. So the bands are declared now:**
**CEG ±4.9% · VST ±6.1%** (both expiry 08-07, **D1**).
⇒ **A settled move INSIDE those bands is no-information by construction. Only a settle beyond the
band WITH contracted-demand or backlog guided UP counts as the kill firing.**

### T5 · SPCX 911.5m-share unlock (2026-08-06) → **S56** · not duplicated

**S56 owns it in full** (counted supply vs counted positioning, → 08-11). ⚠ **Recorded so the 08-11
scoring is not read as a clean event study: the tape front-ran it — SPCX settled −13.61% on 08-05
with a 20-day excess of −30.26 vs SPY, the day BEFORE the unlock.** 🚨 **SPCX is outside
`us_top300`, so this desk has no flow, OBV, RS or short row for it** — filed to the missed ledger
under `N.유니버스부재`.

---

## 2 · Cycle-GAP core-starter — **none required**

`cycle_exposure` returned **✅ no GAP**: rank-1 AI-compute epicenter **19.97%** (floor 12%),
rank-2 Energy/oil-refining **12.15%** (floor 8%). **No tape-independent core-starter is owed.**

⚠⚠ **Carried as instrument findings for a human, NOT as position statements (P4):**
- **`cycle_exposure.py:87` gates on `rank <= 2`, so a rank-3 floor set in the registry would be
  INERT** — rank-3 cannot produce a GAP by construction.
- **Rank-2's floor is object-blind**: a book holding XOM + CVX instead of MPC + PSX clears the same
  8% while owning crude beta into a 12% drawdown.
- **The registry's rank-2 name still reads *"(Hormuz + Russia crack)"* — an R46 violation in the
  title string**, now contradicted by the object's own operator: **XOM CEO Darren Woods, CNBC
  07-31 — *"Even after the Strait opens up… we've still got the Russia capacity that's been lost."***
- **AI-datacenter power sits in rank-1's `adjacent` list, which no GAP test reads**, and **EMR and
  AME are in no cycle at all.**

---

## 3 · Standing environment flag

🚨 **`ARMED(TIMEFOLIO_EXECUTE=1)` is set in the environment for a 4th consecutive run.**
**This was a read-only research run: no orders, no `--execute`, no order-desk staging, nothing
executable touched.** Recorded because a standing armed flag is something a human should see.
