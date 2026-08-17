# L2 · carryover — read and reconcile the standing view (orchestration)

> Called by L1·HANDOVER. Turns `handoff/` (the analytical carry) plus the mechanical tag ledger into
> one reconciled inheritance packet. Reuses `module_report_tags` — never re-implements it. Composes L3.

## Calls (all `python -X utf8`)

**1. Read the carry** — plain file reads, no module needed:
```
handoff/STANDING_VIEW.md          SHARED SPINE — regime call · seed measured chain · §4 · §5 retracted ledger · §6
handoff/STANDING_VIEW_{US|KR}.md  this desk's §2 fact rows + its per-name registry (§3a / §3b)
handoff/SCENARIOS.md              SHARED SPINE — legend · scoring rules · MASTER scoring log · MASTER index (46)
handoff/SCENARIOS_{US|KR}.md      this desk's registered brackets in full
⚠ Split by market 2026-07-29. §5 and the master scoring log are NOT split. Ownership = the
  REGISTERING desk and confers no exclusivity — S8 was US-registered and KR-scored, S33/S28 the
  reverse. A past-dated row in the other file is still this run's to score: open it.
handoff/RESEARCH.md         Part A rules · Part B lenses · Part C dig list
```

**2. Reconcile against the mechanical ledger** — what we *believe* vs what we *covered*:
```bash
python -X utf8 -m module_report_tags show            # who covered what, with which verdict
python -X utf8 -m module_report_tags ticker <TKR>    # per-name report history
```
The two are different objects and must be cross-read, not merged:
- A name in STANDING_VIEW with **no** ledger coverage = a belief no report supports → demote or dig.
- A name with heavy ledger coverage and **no** standing thesis = an unowned coverage gap → candidate
  DEEP (this is exactly how 009150 surfaced as C2).
- A ledger 🔴RESOLVED that still has a live thesis = staleness → re-justify or retract.

**3. Score matured scenarios** — L3 [scenario_score](../L3_functions/scenario_score.md), one call per
`ARMED` row whose event date has passed. Atomic: one scenario → one branch verdict.

**3b. Audit the rejection ledger for anything due — do not rely on `score` alone for this.**
L3 [reject_ledger](../L3_functions/reject_ledger.md). Rejections are the one desk action that used
to leave no score. Run **both**:
```bash
python -X utf8 scripts/reject_ledger.py due     # ★ run this one first, every HANDOVER, no exceptions
python -X utf8 scripts/reject_ledger.py score   # per-class / per-type excess return (context, not a gate)
```
`score` benchmarks against the **equal-weight 1조+ universe**, never the index (measured 2026-07-23,
equal-weight −2.6% vs cap-weight −15.7% — an index benchmark flatters every rejection). It tells you
which reason classes are earning their keep. It does **not** by itself surface a revived name — that
is `due`'s job, and until 2026-07-23 nothing called it: 24 of the ledger's 25 rows were entered with
no `revives_if`/`recheck_date` at all, so "any row whose condition has now come true" was silently
unstatable for almost the whole ledger. That gap cost **+41.2pp and +26.9pp on SK이터닉스 alone** —
the ledger's two most expensive rows, both narrative-class, both never re-examined until a user
prompted a manual re-audit.

⚠ **A HANDOVER that skips `due` is not a lighter HANDOVER — it is the same failure mode as an
unscored SCENARIOS.md row, just on the candidate side instead of the macro side.** `due` output has
two sections and neither may be waved through silently:
- **재확인일 도래/경과** (recheck date has passed) — re-pull flow/news for each name named here
  (same re-pull commands as §4 below) and either `resolve --outcome revived` (back into §A/§B with
  its original evidence, per the 2026-07-23 SK이터닉스 precedent) or `resolve --outcome reaffirmed`
  (stays out, but now on fresh evidence, not a stale one).
- **부활조건 없는 레거시** (no revival condition was ever set) — these cannot be re-checked on a
  schedule because there is no schedule; HANDOVER may not carry them forward unexamined a second
  time. Either audit one now with a fresh pull, or explicitly note it as still-pending audit in
  `HANDOVER.md` so the gap is visible, not silent.
- A `due` row that surfaces two HANDOVERs in a row without a `resolve` call against it is a process
  failure to name in `HANDOVER.md`, the same way an `EXPIRED` scenario is named, never dropped quietly.

**3c. Audit the *opportunity-cost* ledger — the symmetric half of 3b.**
L3 [missed_ledger](../L3_functions/missed_ledger.md). Until 2026-07-31 this desk scored what it
**rejected** and had no instrument at all for what it **did not buy** (F2), so "we were disciplined"
and "we never saw it" produced identical evidence — none.
```bash
python -X utf8 scripts/missed_ledger.py due     # ★ same standing as 3b's `due` — run it, every HANDOVER
python -X utf8 scripts/missed_ledger.py score   # per-class / per-type, same bench as reject_ledger
```
⚠ **The sign is inverted** relative to 3b: here `excess > 0` means *missing it cost us*. Do not add
the two ledgers' `excess` columns without aligning signs first.
⚠ A `due` row here gets exactly the treatment 3b's rows get — re-pull, then `resolve --outcome
entered | reaffirmed | expired`. Two HANDOVERs without a `resolve` is a process failure to name.
⚠ **`score` currently carries a seeded, outcome-selected block** (the first 6 rows were harvested
from `leak_scan --top`, i.e. from names that had already risen). The script prints this warning
itself. Quote the class means as *accumulation*, never as an edge, until pre-registered rows exist.

**3d. Read the exposure state before forming any candidate list.**
L3 [exposure_state](../L3_functions/exposure_state.md). Read-only here — **this L2 never runs `log`**
(the 09:10/15:00 timefolio tasks own accrual; a research run must not write a second row for the day).
```bash
python -X utf8 scripts/exposure_rule.py state           # 4-state verdict + band gap
python -X utf8 scripts/exposure_rule.py show --tail 10  # accrued rows + cumulative decomposition
```
This is inherited context, not a gate: the stage that picks names must know **how much** is being
allocated. Measured 2026-07-31 — of a **+16.86pp** lead, **~14pp was cash weight** while selection
contributed **+2.54pp on n=11 with one name carrying it** (indistinguishable from zero, C4); the next
session **the same cash weight gave back −12.5pp**. A candidate list built without the exposure state
is a list with no size.
⚠ If `show` returns no rows the state machine is **cold-starting** and its verdict is unreliable —
measured that day: cold start read `방어`/−1.9pp where the backfilled path read `복귀`/**−37.2pp**.
Say so in `HANDOVER.md` rather than quoting the cold verdict.
⚠ If the state is `밴드미설정`, report it as 🚨 and **do not substitute a number** (P5).

**3e. Read the signal scoreboard — does this desk's own ranking have a sign yet?**
L3 [ic_ledger](../L3_functions/ic_ledger.md) (+ producer L3 [axis_inflection](../L3_functions/axis_inflection.md)).
```bash
python -X utf8 scripts/axis_inflection.py     # pattern signals -> axis files
python -X utf8 scripts/ic_ledger.py log       # accrue every newly-resolved (run x axis x horizon)
python -X utf8 scripts/ic_ledger.py score     # mean IC / NW t / n_eff / n-needed
```
Carry **only the cells with `n_eff >= 4`**, and carry the **`필요n`** column — it is the number that
says when an axis gets killed or kept. Learning skill from 11 positions' P&L takes decades; learning it
from an 828-name ranking takes **months**, and this is the unit that makes the difference.
⚠ **Do not quote a cell with `n_eff < 4`** — overlapping forward windows inflate t. Measured: an
uncorrected `h=10` cell read `n=3 · 100% positive · t=+6.7` while **all three windows ended on the same
2026-07-31 rebound**. 14 of 21 cells are currently unquotable for this reason.
⚠ **Bonferroni**: 15–21 simultaneous tests ⇒ read against **|t| > 2.8**, not 2.
⚠ **`n < 10` cells: do not quote `필요n` either.** Measured the same day — `mention_z` read
`IC −0.029, 필요n 44` at n=7 and **`−0.006, 필요n 757` at n=14**. The estimate of how long it will take
is itself unstable at small n.
⚠ Label the window's regime; a crash-window IC does not generalize.
★ **Standing item**: `vol_surge` is the only axis with a consistent sign across two horizons
(h=1 **−2.08** · h=5 −1.91), agreeing independently with **M224** — **and `sector_flow`'s 🟢 verdict
still weights it positively.** Report it every run; **do not flip the gate until it clears Bonferroni** (P4).

**4. Re-measure anything the carry marked suspended-until-a-date.** When a suspension's clearing date
has passed, the carry does not tell you the answer — it tells you to go get it. This includes any
**watch condition an earlier stage armed** ("enter on the breakout", "revisit after the 2Q NIM print"):
an armed condition that nobody re-reads is an idea the desk paid for and never collected. Typical re-pulls:
```bash
python -X utf8 -m module_flow <TKR>.KS --bench ^KS11              # KR flow + short balance
python -X utf8 -m module_KIS <6-digit> --investor 20              # KR investor actuals
python -X utf8 -m module_fundamentals_us <TKR>                    # valuation vs its own history
```
⚠ **KR tickers need the `.KS` suffix in `module_flow`.** A bare 6-digit code returns empty rows
**without erroring** — measured, and it silently reads as "no flow signal" on a day flow reversed.

## Output

An inheritance packet for HANDOVER, in six parts:
1. **Carried theses**, tags (`[measured]`/`[inferred]`) intact, each with `asof` and a stale flag.
2. **Retracted ledger**, surfaced verbatim so today's view is checked against it before it forms.
3. **Scenario status** — scored this run / still armed with dates / expired-unscored (a logged failure).
4. **Reconciliation deltas** — beliefs without coverage, coverage without beliefs, resolved-but-live.
5. **Both ledgers' `due` lists** — rejections (3b) *and* missed entries (3c), each row either resolved
   this run or explicitly carried with a reason. One list without the other is the asymmetry that
   made "disciplined" and "blind" look the same.
6. **Exposure state** (3d) — the 4-state verdict, target vs current invested %, band gap, and the
   cumulative cash/selection split from the ledger. Carried as *size context* for BET/ALPHA.

**HANDOVER folds this into `HANDOVER.md`. This L2 adds no new views and no names — it transports and
reconciles what already exists, and says plainly where the two ledgers disagree.**
