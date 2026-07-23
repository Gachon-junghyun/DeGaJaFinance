# L1 · DECIDE — the PM judgment (stage)

> Phase 2. **This is where the desk earns its keep.** The module supplies data; here the agent decides,
> as a professional PM, what to do with each name. No new module call is required — this is reasoning over
> INTAKE + MARK. Output: `DECISIONS.md`.

## Inputs (from prior stages, no L2 needed)
- `INTAKE_LEDGER.md` (candidates + freshness + ★core) · `BOOK_STATE.md` (positions + P&L + stop-hits + concentration).

## What this stage does — one verdict per name
For **every open position** → HOLD / ADD / TRIM / EXIT. For **every 🟢LIVE / ★core candidate not held** → ENTER / PASS.
Decide by composing, in this order:
1. **Hard gates first (non-discretionary):** a ⛔ stop-hit ⇒ EXIT. A 🔴RESOLVED tag ⇒ EXIT if held / PASS if not
   (the "it's cheap" veto — never re-enter a resolved thesis). A ⚡crowded-short / momentum-only stamp ⇒ any ENTER
   carries a mandatory hard-stop.
2. **Freshness → conviction:** 🟢LIVE = full conviction; 🟡PARTIAL = starter-only, state the residual that must
   resolve; 🔴RESOLVED = out.
3. **Price vs stop/target:** near the report's stop = smaller / wait; already at target = TRIM or PASS (move spent).
4. **Portfolio fit — the correlation guard:** if the name shares the premortem **"one risk unit"** axis with
   existing exposure (e.g. long-duration real-yield: UTIL bond-proxy + high-multiple IT/semis; or RE+Disc shorts),
   treat the basket as ONE position — do not stack correlated ENTERs that are secretly the same bet.
5. **★core exception:** epicenter cycle-GAP starters may ENTER regardless of tape (tape gates only the adds).
- State conviction (high/med/low) and the one observable that would flip each verdict. Fewer, higher-conviction
  actions beat a long list — it is fine to HOLD the whole book on a quiet day.

## ✅ EXIT CHECK
- [ ] Every open position has a HOLD/ADD/TRIM/EXIT verdict; every 🟢LIVE/★core candidate an ENTER/PASS.
- [ ] Hard gates applied (stop-hit→EXIT, RESOLVED→out, momentum-only→hard-stop stamped).
- [ ] Correlation guard applied (no stacked ENTERs on one risk unit); each verdict carries a flip-condition.
- [ ] **Every PASS/EXIT is a ledger row with a reason class and a `--revives-if` condition** — L3
      [reject_ledger](../L3_functions/reject_ledger.md). A PASS whose stated condition later comes true
      (e.g. "wait for the breakout", "revisit after the print") returns as a candidate on evidence.
      ★ Measured: the correlation guard is the one rejection class that has *earned* its keep so far
      (−5.3pp avg); a PASS with no revival condition is where ideas quietly disappear.
