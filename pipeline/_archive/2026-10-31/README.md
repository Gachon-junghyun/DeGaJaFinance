# pipeline/_archive/2026-10-31 — what was moved here, why, and how to bring it back

> Archive of the 2026-10-31 pipeline cleanup (orchestra `2026-10-31_pipeline`). Nothing here was deleted:
> every file was moved with `git mv` so `git log --follow` keeps its history. Each section below is owned by
> the branch that moved those files.

## company

**What and why.** The three single-name protocols — `company_research` (bet), `기업분석` (report) and
`real_alpha_kr` (forensic) — ran one name through largely the same blocks under three questions, compiled to
178 / 215 / 84 KB, and their runs ended with flow tables and little operating reading. module_lens's first
learning (2026-10-31) scored filings/earnings/guidance evidence 6 of 8 right and flow 5 of 32. They were merged
into one protocol, `protocols/company.md`, with three modes (`research` / `report` / `forensic`) on one spine:
filings → structure and competition → financial-environment transmission → money (flow only confirms) → value →
refutation → verdict with weights in module_lens. Compiled size: **79.8 KB**.

**Moved here → merged into**
| archived file | now lives in |
|---|---|
| protocols/company_research.md · protocols/기업분석.md · protocols/real_alpha_kr.md | protocols/company.md (modes research · report · forensic) |
| L1_stages/self_score.md | L1_stages/co_carry.md (with the company slice of HANDOVER: ledger rows, lens score/due) |
| L1_stages/forensic_pack.md · L1_stages/primary_source.md · L3_functions/estimate_revision.md · L3_functions/filing_diff.md | L1_stages/co_filings.md |
| L1_stages/value_chain.md · L1_stages/chain_alpha.md · L1_stages/driver_test.md · L3_functions/contract_alpha.md | L1_stages/co_structure.md |
| L1_stages/money_forensic.md · L2_modules/money_trail.md · L3_functions/accruals_check.md | L1_stages/co_money.md |
| L1_stages/set_diff.md · L3_functions/set_difference.md · L1_stages/valuation.md | L1_stages/co_value.md |
| L3_functions/holdco_split.md · L3_functions/implied_expectation.md · L3_functions/target_bridge.md | L3_functions/valuation_math.md (§A · §B · §C) |
| L1_stages/bet_verdict.md · L1_stages/verdict.md | L1_stages/co_verdict.md (gates G1–G8, 4-tier for forensic, lens weights) |
| protocols/_compiled/{company_research,기업분석,real_alpha_kr}.md | not tracked by git; regenerate from the archived sources if needed |
New: L1_stages/co_macro.md (no company protocol had a rates/dollar/oil/credit transmission step).
Kept in place and lightly edited: L1_stages/falsify.md · L1_stages/publish_report.md (report mode only) ·
protocols/company_batch.md · L1_stages/batch_select.md · L1_stages/batch_fanout.md (now call `company --mode research`).
No longer composed by any company protocol (files untouched, still used elsewhere): pulse · handover · size.

**How to bring it back.** From the repo root:
```bash
A=pipeline/_archive/2026-10-31
git mv $A/protocols/company_research.md pipeline/protocols/      # same for 기업분석.md, real_alpha_kr.md
git mv $A/L1_stages/<name>.md pipeline/L1_stages/                # every L1 the protocol links
git mv $A/L2_modules/money_trail.md pipeline/L2_modules/
git mv $A/L3_functions/<name>.md pipeline/L3_functions/
python -X utf8 pipeline/build_protocol.py company_research
```
The old protocols link the old stage names, so restoring one protocol means restoring every unit it links
(see the table). The new co_* files can stay alongside; they do not collide with the old names.

## industry

**What and why.** Hours-long `industry_us` / `industry_kr` runs (194 / 188 KB compiled; 69 + 74 runs since 07-10)
ended with flow tables: across six completed runs operating income was asked 0–2 times, market share 0 times,
guidance only as WebSearch summaries, and every gate that let a conclusion pass — the 🟢 candidate entrance, «a
rotation delta must be carried by a flow number», «flow still passes ⇒ do not remove», the KR investor-flow
confirmation, the ticket scoring — was flow or price (diagnosis: orchestra `2026-10-31_pipeline/K1/out.md` in the
agent repo). The lens ledger's first learning scored filings evidence 6/8 and flow 5/32. The desk was rebuilt on
one spine — financial environment by data-change size → EARNINGS (filings) → COMPETITION → FLOW_CHECK (confirm
only) → BET with lens weights by evidence kind → ALPHA → HANDOVER close-out. Compiled now ≈ 98 KB (US) / 93 KB (KR).
Two low-use desks went with it: `idle_probe` (1 run) and `morning_brief` (3 runs).

**Moved here → merged into**
| archived file | now lives in |
|---|---|
| L1_stages/rotation.md | L1_stages/macro.md §3 (sector verdicts, focus-sector rule, DEEP_LOG) |
| L1_stages/event_alpha.md · L2_modules/narrative_money.md | L1_stages/earnings.md §3 (events that change earnings; the narrative×money 2×2 was dropped) |
| L1_stages/sweep.md | L1_stages/flow_check.md (scoring health, one-name buckets, held-not-in-universe, agree/disagree) |
| L1_stages/deep.md | L1_stages/competition.md (carry rules L1 · L2 · contract terms · W4 · W2 · W5 · frame transfer) |
| L1_stages/drift.md | L1_stages/handover.md §6 close-out |
| L1_stages/leak_audit.md | not merged — no protocol called it; `scripts/leak_scan.py` still exists |
| protocols/idle_probe.md · L1_stages/pair.md · probe.md · control.md · adjudicate.md | not merged (census stays with preflight; size · stage_orders · kis_sync stay — order side) |
| protocols/morning_brief.md · L1_stages/brief_gather.md · brief_rank.md · brief_render.md · L3_functions/public_source.md | not merged |
| protocols/_compiled/{industry_us,industry_kr,idle_probe,morning_brief}_pre-2026-10-31.md | compiled from the pre-rebuild sources on 2026-10-31 (not tracked by git) |
New: L1_stages/earnings.md · competition.md · flow_check.md. Rewritten in place: macro · handover · bet · alpha
(and premortem, preflight, instrument_check lightly); their previous text is `git show HEAD:pipeline/L1_stages/<name>.md`.
Rules not carried into the new files are listed with reasons in `K2/out.md` («버린 규칙»).

**How to bring it back.** From the repo root:
```bash
A=pipeline/_archive/2026-10-31
git mv $A/L1_stages/{sweep,event_alpha,rotation,deep,drift}.md pipeline/L1_stages/
git mv $A/L2_modules/narrative_money.md pipeline/L2_modules/
git checkout HEAD -- pipeline/protocols/industry_us.md pipeline/protocols/industry_kr.md \
    pipeline/L1_stages/{macro,handover,bet,alpha,premortem}.md   # only if the old texts are wanted too
python -X utf8 pipeline/build_protocol.py industry_us industry_kr
# idle_probe / morning_brief: git mv the protocol and the L1/L3 files listed above back, then build_protocol.py <name>
```
The old industry protocols link `instrument_check` as stage −1; the new ones run protocol `preflight` before
HANDOVER instead.
