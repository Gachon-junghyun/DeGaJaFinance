# L1 · BATCH_SELECT — pick the N names, deterministically, and skip what is already fresh

> Phase 1 of the company batch. Chooses **which N companies** get a research slot today (default 10)
> from sources that already exist, and — the load-bearing half — **removes every name whose report is
> still valid**, so the fan-out spends its budget on what the desk cannot already answer.
> Calls L2. Output: `BATCH_ROSTER.md` + `roster.json`.

## Belief
A batch that re-researches a name the desk covered three sessions ago has spent a subagent to reproduce
a file it already owns. The desk has a mechanical ledger of exactly that (`module_report_tags`) and it
was built to stop this. **The selection stage's yield is the names it removed, not the names it kept.**

## L2 called
- [carryover](../L2_modules/carryover.md) — the carry + `reject_ledger due` + `missed_ledger due`
  + the exposure state. **A due recheck is a research slot with its question already written.**
- [report_read](../L2_modules/report_read.md) — `module_report_tags ticker <T>` reverse-lookup per
  candidate: who covered this, when, with what verdict.
- [bookkeeping](../L2_modules/bookkeeping.md) — what the book actually holds (a held name with no
  fresh report is the highest-priority slot: we own the risk and cannot cite a reason).

## Candidate sources, in priority order (each row is a reason, not a hunch)
| # | Source | Why it earns a slot |
|---|---|---|
| 1 | **held in the book with no fresh company report** | we own it and cannot say why — this is the PSX/G8 case |
| 2 | **`reject_ledger due`** — recheck date passed | the question is pre-written (`--revives-if`); answering it is cheap |
| 3 | **`missed_ledger due`** — recheck date passed | same, with `--enters-if` |
| 4 | **🟢LIVE names on the latest `BET_SHEET.md`** lacking a company report | the top-down run is about to lean on them |
| 5 | **`LIVE_SHORTLIST.json` cross-sector names** | surfaced by the sweep, never dissected |
| 6 | user-supplied list | explicit override — fills from the top, does not replace the dedupe |

## ★ The freshness gate — when a name is REMOVED from the roster
A name is skipped (and recorded as skipped, with its reason) when **all** hold:
- [ ] a `company_research` verdict exists for it, **≤ `--stale-sessions` settled sessions old** (default **10**);
- [ ] **no dated observation point** from that verdict has matured since;
- [ ] **no earnings print or 8-K/주요사항 filing** since that verdict's date;
- [ ] the driver's roll-adjusted percentile has not crossed a band since (L3 [driver_link](../L3_functions/driver_link.md)).

Any one failing ⇒ the name stays on the roster and the failing condition becomes its **research mandate**
(it is written into the roster row, so the subagent starts with the question rather than from zero).

⚠ **The skip list is published, with counts.** A roster that silently dropped names looks identical to a
roster that had none — the same failure mode `brief` had before its recall was measured (README).

## ✅ EXIT CHECK
- [ ] `roster.json` holds exactly N rows (or fewer, with the shortfall explained — never padded to reach N).
- [ ] Every row carries `source` (which of the 6), `mandate` (the question this slot answers), `market`, and prior-verdict age if any.
- [ ] The **skip list is written with its count** and each skip names which freshness condition held.
- [ ] Names from `reject_ledger due` / `missed_ledger due` carry their stored condition verbatim as the mandate.
- [ ] No name appears twice; KR/US tickers are in the format their market's tools need.
