# PROTOCOL — industry_us

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file** — L1 units are
> independent and do not know their sequence. L1s are **referenced only** (content lives in each L1 file).
> Purpose: rank sectors by macro proposition → deep-dive only the 3–4 OW sectors down to the value chain.
> Zero buy/sell recommendations. Output root `llm_outputs/{YYYY-MM-DD}/industry_US/` (see File-output rules).
> Runtime = `--market us`. **English-pure runtime** — no Korean in outputs (Korean context skews the frame).

## File-output rules (locked 2026-07-15 — the scripts' hardcoded paths are the single source)
- **Run outputs (LLM reports + run JSONs) → `llm_outputs/{YYYY-MM-DD}/industry_US/`.** This matches
  the scripts' hardcoded defaults: `us_live_shortlist` READS `SECTOR_FLOW_US.json` there, and
  `drift_watch` READS `MACRO_REPORT.md` there — writing anywhere else breaks the chain.
  Previous date folders are **read-only** (never overwrite; corrections are append-only ADDENDUMs).
- **Script byproducts land one level up**, in `llm_outputs/{date}/` root (script-owned, don't fight it):
  `CATALYST_WATCH.json` · `CYCLE_EXPOSURE.md/.json` · `ACTION_TICKETS.md`. Sweep caches/history live in
  `llm_outputs/sector_flow/` · `llm_outputs/us_screen/`.
- **Filenames are LOAD-BEARING** (downstream desks glob them — never rename/split): `MACRO_REPORT.md` ·
  `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `EVENT_ALPHA.md` · `SECTOR_ROTATION.md`
  (+DEEP_LOG line) · `SECTOR_DEEP_{code}.md` · `BET_SHEET.md` (ONE file, per-sector sections).
- Module scratch output → `out/` (repo rule; not committed). No secrets in any output.
- Handoff ledger: `module_report_tags` scans `DEGAJA_REPORT_DIR` (default `REPORT/`) — run it as
  `DEGAJA_REPORT_DIR=llm_outputs` OR copy finalized reports into `REPORT/`. ⚠ Open decision
  (PROMPT_MAP §6) — a human locks which; until then state which mode you used in the run log.

## DEEP budget — **N = 4** (2 continuous-track + 2 rotating)

ROTATION reads this line to size its selection rule. **Unchanged 2026-07-31** when `industry_kr`
cut to N=2: that cut was justified by KR-specific measurement (the contest book's own return
decomposition + M224's negative grade on the KR sweep axes), and importing a conclusion across
markets is exactly the W1 violation this repo keeps logging. If the US desk should shrink too, it
needs **its own** measurement first.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| −1 | [INSTRUMENT_CHECK](../L1_stages/instrument_check.md) ★preflight | `preflight/PREFLIGHT.md` — 7 gates; **a FAIL removes a citation right for this run** (protocol [preflight](preflight.md)) |
| 0 | [HANDOVER](../L1_stages/handover.md) | `HANDOVER.md` (inherited standing view + scenarios scored + dig list) |
| 1 | [MACRO](../L1_stages/macro.md) | `MACRO_REPORT.md` (propositions + ★transmission matrix + self-backtest hit-rate) |
| 2 | [SWEEP](../L1_stages/sweep.md) | `SECTOR_FLOW.json` · `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.md` |
| 3 | [EVENT_ALPHA](../L1_stages/event_alpha.md) | `EVENT_ALPHA.md` (forward cards: building threads × money flow — bottom-up rotation cross-check) |
| 4 | [ROTATION](../L1_stages/rotation.md) | `SECTOR_ROTATION.md` (11-sector OW/UW + 4 DEEP picks + DEEP_LOG) |
| 5 | [PREMORTEM](../L1_stages/premortem.md) ★US-only | `BLINDSPOT_PREMORTEM.md` |
| 6 | [DEEP](../L1_stages/deep.md) | `SECTOR_DEEP_{code}.md` ×4 (+ any pre-mortem-promoted 5th) |
| 7 | [BET](../L1_stages/bet.md) | `BET_SHEET.md` (one file, per-sector sections — downstream readers depend on the single filename) |
| 8 | [ALPHA](../L1_stages/alpha.md) | `BET_SHEET §B` freshness tags + `ACTION_TICKETS.md` |
| 9 | [DRIFT](../L1_stages/drift.md) ★US-only | post-run ADDENDUM appended to MACRO_REPORT §5 |

## US runtime deltas (vs industry_kr)
- **PREMORTEM·DRIFT blocks added** (anti-tunnel; born from the 2026-07-14 postmortem: one-way
  tilt into a known binary + zero exposure to the #1 cycle's epicenter).
- MACRO primary data = `module_macro_us` (FRED) directly (`--json`; cite `[FRED]`).
- News `--scope foreign` — **hard rule, every news call including `brief`/`thread`**: never let the
  KR domestic feed rank the US frame (measured 787 rate hits : 0 US-bank hits in a bank-earnings
  week; the KR pool's obsession is not the US market's attention). Universe `us_top300` (GICS);
  flow = FINRA short-vol / CFTC COT
  (⚠ US has NO investor-type feed — KR's KIS foreign/institution actuals have no US equivalent;
  the substitute is short-pressure + COT-percentile *positioning*, which is context, not a trigger).
- Catalyst injection at run-start: any binary ≤48h ⇒ PREMORTEM must produce a both-sides bracket
  (a one-way tilt into a known binary is a protocol violation).

**Start → read HANDOVER (stage 0) first, then MACRO, and execute.** Advance only after each L1's EXIT
CHECK passes. Finish with [handoff](../handoff.md) to update the tag ledger — and write the analytical
carry back to `handoff/*.md` per the HANDOVER stage. The two are different objects: the ledger records
*what was covered*, the carry records *what we believe, what we pre-committed to, and what we retracted*.
