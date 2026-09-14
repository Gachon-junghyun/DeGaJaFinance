# PROTOCOL — company_batch (컴패니 배치 · N기업 오케스트라 → 점수판)

> A protocol = an ordered composition of L1 blocks. **Order is owned by this file.** L1s are referenced only.
> Purpose: run **N companies (default 10)** through [`company_research`](company_research.md) as
> **parallel subagents**, convert the N verdicts to **one comparable scale**, and publish a scoreboard the
> **top-down run reads instead of re-digging**. Daily or on demand.
> Output: `llm_outputs/{date}/company_batch/{ticker}/` ×N + `REPORT/COMPANY_SCOREBOARD.md`.

## What this desk is (and is NOT)
- **IS**: an orchestrator. It owns *which* names, *how many*, and *how they are ranked*. It owns no
  research of its own — every number comes from a child running `company_research`.
- **IS NOT**: a portfolio view. N verdicts are N observations; the scoreboard is a **reading order**, not
  an allocation. Sizing stays with SIZE + `kelly_size` against the live book.
- **IS NOT**: a replacement for the top-down run. It **supplies** it — see the handshake below.

## Composition (L1 order)

| # | L1 block | Output |
|---|---|---|
| 1 | [BATCH_SELECT](../L1_stages/batch_select.md) ★new | `roster.json` — N names, each with a **mandate**, plus the published **skip list** |
| 2 | [BATCH_FANOUT](../L1_stages/batch_fanout.md) ★new | N subagents in one message → `{ticker}/REPORT.md` + `verdict.json` each |
| 3 | [BATCH_SCORE](../L1_stages/batch_score.md) ★new | `COMPANY_SCOREBOARD.md` + `scoreboard.json` + `out/ic/axes/` |

Three stages, three new L1s, **zero new L2** — select reuses carryover · report_read · bookkeeping;
fanout is an Agent idiom (same as PREMORTEM's four lenses); score is a script plus the existing
`ic_ledger` plumbing. That "zero new L2" is the test that these were stages and not orchestration.

## ★ The handshake with the top-down run (this is the point of the protocol)
The reason the batch exists is that `industry_us` was re-deriving, inside every run, numbers a company
report already held — and doing it in a context already carrying nine other stages.

```
company_batch  ──► REPORT/COMPANY_SCOREBOARD.md ──►  industry_us · L1 BET
    (overnight / on demand)      thesis · verdict · stop      "confirm, don't re-derive"
                                 score · obs points · path
```

**BET's rule (wired into `L1_stages/bet.md`)**: for any candidate that has a scoreboard row, BET
**confirms the thesis** and writes only the delta. It re-derives **only** when confirmation fails:

| confirmation test | fails when | then |
|---|---|---|
| **age** | row older than `--stale-sessions` (default 10 settled sessions) | re-dig |
| **observation point** | a dated observation point has matured | grade it first (that is the delta), then confirm or re-dig on the result |
| **event** | an earnings print or 8-K/주요사항 landed after the row's date | re-dig |
| **driver band** | the roll-adjusted driver percentile crossed a band | re-dig that name's driver only |
| **direction** | the run's own flow/RS now disagrees with the row's `frame`/`evidence_grade` | state the disagreement; do **not** silently override the report |

A confirmed name contributes its §A numbers, §C flow read and stop **by citation** — README §Core:
*cite upstream artifacts, never re-print them.* The BET section for a confirmed name should be short;
if it is long, either confirmation failed or the stage is re-printing.

## Cost, stated (so it can be argued with)
Default **10** names. Each child runs `company_research` FORENSIC_PACK→BET_VERDICT — the heaviest calls
are the segment/driver/peer pulls and the news axis. `--count` is the knob; `--stale-sessions` is the
other one and it is usually the better one: **raising staleness reduces the roster more cheaply than
lowering the count**, because it removes exactly the names whose answers have not changed.

⚠ **Never pad the roster to reach N.** If the freshness gate leaves 4 names, run 4 and say so. A batch
that invents 6 more slots to look full spends its whole budget on the names it least needed.

## Invocation
```bash
# stage-by-stage (context-loss guard)
python -X utf8 pipeline/run_protocol.py company_batch --start
python -X utf8 pipeline/run_protocol.py company_batch --next

# the score conversion (stage 3's engine)
python -X utf8 scripts/company_score.py rank --run {date}
python -X utf8 scripts/company_score.py axes --run {date}
```
Skill wrapper: `company-batch` (`~/.claude/skills/company-batch/SKILL.md`) — *"기업 배치 돌려"*,
*"오늘 10개 돌려"*, *"배치 점수판"*.

⚠ **Not wired to a scheduler.** Order-adjacent automation is human-triggered in this repo (CLAUDE.md
규약); this desk writes files only, but the roster it produces feeds a desk that sizes, so the batch is
launched by a person or by an existing launcher — **not** by a new cron.

**Start → read [BATCH_SELECT](../L1_stages/batch_select.md) and execute.** Advance only after each EXIT
CHECK passes. Finish at BATCH_SCORE with `COMPANY_SCOREBOARD.md` written and `module_report_tags update` run.
