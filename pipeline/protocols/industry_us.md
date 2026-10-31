# PROTOCOL — industry_us

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file** — L1 units are
> independent and do not know their sequence. L1s are **referenced only** (content lives in each L1 file).
> Purpose: read the financial environment and what companies are actually earning, then the industry
> structure, and only then ask whether the money agrees. Zero buy/sell recommendations.
> Output root `llm_outputs/{YYYY-MM-DD}/industry_US/`. Runtime = `--market us`. **English-pure runtime**.

## Spine (rebuilt 2026-10-31)
financial environment by the **size of data changes** → earnings, guidance and estimates **from the filing** →
industry structure and competition → flow **as a short confirmation** → conclusions registered in `module_lens`
with evidence weights by kind → handover (`module_lens score` · `due`).
Why: runs ended with flow tables and no operating-income, guidance or competition reading; the lens ledger scored
filings evidence 6/8 and flow 5/32; earnings words and large rate/oil/dollar moves move prices (`lab/NEWS3D_20261030.md` E2).

## Before stage 1 — run protocol `preflight`
It writes `llm_outputs/{date}/preflight/PREFLIGHT.md`, a claim-permission table (a FAILED gate removes a citation
right for this run). HANDOVER copies it; if it was not run, HANDOVER says so.

## Composition (L1 order)

| # | L1 block | Output (cap) | Next stage uses |
|---|---|---|---|
| 1 | [HANDOVER](../L1_stages/handover.md) | `HANDOVER.md` (8 KB) | due list · permissions · exposure state · rule map |
| 2 | [MACRO](../L1_stages/macro.md) | `MACRO_REPORT.md` (14 KB) | transmission lines · sector verdicts · focus sectors · catalysts |
| 3 | [PREMORTEM](../L1_stages/premortem.md) ★US-only | `BLINDSPOT_PREMORTEM.md` (10 KB) | promoted legs · both-sides brackets · cycle GAP |
| 4 | [EARNINGS](../L1_stages/earnings.md) | `EARNINGS.md` (24 KB) | candidate set · OP margin · guide vs prior guide · estimate direction |
| 5 | [COMPETITION](../L1_stages/competition.md) | `SECTOR_DEEP_{code}.md` × N (12 KB each) | share · price · capacity · customers · contract terms · kill conditions |
| 6 | [FLOW_CHECK](../L1_stages/flow_check.md) | `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.md` · `FLOW_CHECK.md` (4 KB) | one agree/disagree line per sector and name |
| 7 | [BET](../L1_stages/bet.md) | `BET_SHEET.md` (16 KB) + lens Q IDs | §B theses with weights by kind |
| 8 | [ALPHA](../L1_stages/alpha.md) | `BET_SHEET §B` tags + `ACTION_TICKETS.md` (6 KB) | carry-forward tags · tickets |
| — | HANDOVER §6 close-out | write-back · `module_lens export` · coverage ledger · drift +3–6h | next run |

## FOCUS budget — **N = 4** (2 continuous + 2 rotating)
MACRO reads this line to size its focus-sector rule. Unchanged 2026-07-31 when `industry_kr` cut to N=2: that
cut was justified by KR-specific measurement, and importing it across markets is the W1 violation. The US desk
needs its own measurement before it shrinks.

## File-output rules (the scripts' hardcoded paths are the single source)
- Run outputs → `llm_outputs/{date}/industry_US/`. `us_live_shortlist` reads `SECTOR_FLOW_US.json` there and
  `drift_watch` reads `MACRO_REPORT.md` there. Previous date folders are read-only (corrections append-only).
- Script byproducts land in `llm_outputs/{date}/`: `CATALYST_WATCH.json` · `CYCLE_EXPOSURE.md/.json` ·
  `ACTION_TICKETS.md`. Sweep caches in `llm_outputs/sector_flow/` · `llm_outputs/us_screen/`.
- Load-bearing filenames (globbed downstream — never rename or split): `MACRO_REPORT.md` · `SECTOR_FLOW_US.json` ·
  `US_LIVE_SHORTLIST.json` · `SECTOR_DEEP_{code}.md` · `BET_SHEET.md`. New 2026-10-31: `EARNINGS.md` ·
  `FLOW_CHECK.md` (`SECTOR_ROTATION.md`, `EVENT_ALPHA.md`, `SWEEP_READ.md` are no longer written).
- Module scratch → `out/`. No secrets in outputs. Coverage ledger: `module_report_tags` scans `DEGAJA_REPORT_DIR`
  (default `REPORT/`) — state which mode you used in `HANDOVER.md` (open decision, PROMPT_MAP §7).

## US runtime deltas (vs industry_kr)
- **PREMORTEM** runs (anti-tunnel, 2026-07-14 postmortem); drift is US-default in HANDOVER close-out.
- MACRO primary data = `module_macro_us` (FRED) `--json`; cite `[FRED]`.
- News `--scope foreign` on every call (measured 787 rate hits : 0 US-bank hits when the KR feed ranked the US
  frame). Universe `us_top300` ∪ book holdings.
- Filings: EDGAR via `module_disclosure_us` / `module_fundamentals_us --json` (no operating-income field — read it
  from the 8-K ex 99.1 or 10-Q); exhibits and IR pages via `web_errand`.
- Flow = FINRA short-volume z / CFTC COT — context, not a trigger (US has no investor-type feed).
- Catalyst injection: any binary ≤48h ⇒ PREMORTEM brackets both sides (a one-way tilt into a known binary is a
  protocol violation).

**Start → protocol `preflight`, then HANDOVER, and execute in order.** Advance only after each EXIT CHECK passes.
Finish with HANDOVER §6 close-out.
