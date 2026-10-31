# PROTOCOL — company (single name · three modes: research / report / forensic)

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file.** L1s are referenced only.
> Merged 2026-10-31 from `company_research` (bet), `기업분석` (report) and `real_alpha_kr` (forensic) — originals in
> `pipeline/_archive/2026-10-31/` with the restore steps. Market-parameterized (`--market us|kr`, KR 6-digit auto-detect).
> Output root `llm_outputs/{YYYY-MM-DD}/company_{ticker}/` (batch: `company_batch/{ticker}/`).

## Why it was merged
Three protocols ran the same name through the same blocks under different questions, and the runs ended with
**flow tables and no operating reading**. Measured (module_lens first learning, 2026-10-31): filings/earnings/guidance
evidence was right **6 of 8**, flow **5 of 32**. So one spine, in the order that reads the company:
**filings (earnings · margin · guidance) → structure and competition → financial-environment transmission → money
(flow only confirms) → value → refutation → verdict with weights in module_lens.** The mode changes the question
and the depth, not the spine.

## Modes
| mode | question | ends in | weight |
|---|---|---|---|
| `research` (default; `company_batch` uses it) | do we bet? | `ENTER·ADD·HOLD·TRIM·EXIT·PASS` + stop + one ledger row | medium |
| `report` | what is it, what is it worth, should a person buy? | own target + execution table + Word/PDF delivered | heavy, not daily |
| `forensic` | is it real? (참고-only, binding:false, READ-ONLY) | REAL / REAL-but-PRICED / INFLATED / BROKEN + ledger.json | medium |
A stage not used by the mode writes `SKIPPED (mode)` in its EXIT CHECK and the run advances.

## Composition (L1 order)

| # | L1 block | research | report | forensic | writes (cap) |
|---|---|---|---|---|---|
| 1 | [CO_CARRY](../L1_stages/co_carry.md) | ✔ | ✔ | ✔ | `CARRY.md` 3 KB |
| 2 | [CO_FILINGS](../L1_stages/co_filings.md) | ✔ | ✔ | ✔ | `DATAPACK.md` 20 KB + `SOURCES.md` 8 KB |
| 3 | [CO_STRUCTURE](../L1_stages/co_structure.md) | ✔ lenses 1–6 | ✔ lenses 1–6 | ✔ lenses 1–7 | `STRUCTURE.md` 15 KB |
| 4 | [CO_MACRO](../L1_stages/co_macro.md) | ✔ | ✔ | ✔ | `MACRO_LINK.md` 4 KB |
| 5 | [CO_MONEY](../L1_stages/co_money.md) | ✔ | ✔ | ✔ | `MONEY.md` 6 KB |
| 6 | [CO_VALUE](../L1_stages/co_value.md) | split · implied · ladder | full (+ scenarios, cross-checks) | split · implied | `VALUE.md` 10 KB |
| 7 | [FALSIFY](../L1_stages/falsify.md) | ✔ | ✔ | ✔ | `FALSIFY.md` 4 KB |
| 8 | [CO_VERDICT](../L1_stages/co_verdict.md) | action + G1–G8 + T1/T2 timing | action + G1–G8 + T1/T2 + execution table | 4-tier | `COMPANY_VERDICT.md` 6 KB + `verdict.json` |
| 9 | [PUBLISH_REPORT](../L1_stages/publish_report.md) | — | ✔ | — | `.docx` + `.pdf`, delivered |

Prose names stages in plain text on purpose — **only the composition table's links set the run order.**

## What each stage hands down (cite upstream; never re-print it)
CARRY → open questions and graded points · DATAPACK/SOURCES → segment table, margins, guidance, revision table, dated catalysts ·
STRUCTURE → covered share (D1), holdco split, frame (D3), backlog, moat count · MACRO_LINK → sensitivity rows ·
MONEY → recurring earnings, words-vs-actions, one flow row · VALUE → alpha_delta / risk_unseen, own target, transition signals ·
FALSIFY → bear case (quoted in G5) · VERDICT → ledger row, lens Q with weights, `thesis` for top-down BET.
Self-test for any stage: delete every sentence whose content exists upstream — what remains is the stage's yield.

## Outside this protocol (named in plain text, not composed)
- **preflight** is stage −1 of every desk; a failed gate removes a citation right for this run.
- **pulse** (same-day tape sanity) — run it separately first if the name is moving hard today.
- **handover** belongs to the desk day; CO_CARRY cites it if it ran today and otherwise does the company slice itself.
- **size** — research/report verdicts hand `NEEDS_SIZE` to a human-run SIZE against the live book. This protocol never sizes and never orders.
- Removed on purpose and still removed: the 11-branch chart matrix (grade table does it with measurements) · a separate
  catalyst-calendar stage (dates live in the transition-signal table) · the legacy order tail (`trading_engine`/`alert_bot`, not in this repo).

## Runtime deltas (`--market us|kr`)
| axis | KR | US |
|---|---|---|
| business text | `module_disclosure --business-report` ⚠ **not** `module_business --include-dart` (frameset shell) | `module_business_us --full --json` |
| segment P&L | DART periodic report | earnings 8-K ex 99.1 |
| consensus trend | ✅ wisereport `c1050001` | ❌ 미확보 → own snapshots |
| stakes in subsidiaries | ✅ DART 타법인출자 (shares + %) | 10-K Ex 21 (% only) |
| insiders | direction + qty, **no price** | Form 4 with price (parse XML; see CO_MONEY) |
| investor flow | ✅ KIS actuals (B-grade) | ❌ none — FINRA short-vol z + options |
| ledger scoring | ✅ scored | 🚨 rows score `채점불가` silently — state it |

**Start → read CO_CARRY and execute.** Advance only after each EXIT CHECK passes.
Stage by stage: `python -X utf8 pipeline/run_protocol.py company --start --target <TKR>` then `--next`; state the mode in the first line of `CARRY.md`.
