# L1 · CO_CARRY — inherit this name's past calls and grade them before reading anything new

> Company stage 1 (all modes). Merges the old SELF_SCORE with the company slice of HANDOVER.
> **Reads**: the ledger rows and prior verdict files for this ticker, `module_lens` due questions.
> **Writes**: `CARRY.md` (cap **3 KB**). **Next stages use**: the open questions (CO_FILINGS starts from
> them), the graded observation points (CO_VERDICT's delta line), the reject/missed row (gate G8).

## Why it is first
A desk that never checks its own prior calls is narrative. The dated observation points written by the
last run are the receipts; this stage cashes them **before** new evidence can colour the reading.

## Steps
0. **First line of `CARRY.md` = `mode: research|report|forensic`** (default research). `run_protocol.py` has no mode flag; every later stage reads the mode from this line.
1. **Prior verdicts** — `llm_outputs/*/company_{ticker}/` and `llm_outputs/*/company_batch/{ticker}/verdict.json`
   (latest first) + the forensic ledger `llm_outputs/real_alpha_kr/ledger.json` if the code is there.
   None ⇒ write `prev 없음 — 최초 리서치` and skip to step 4.
2. **Grade every prior observation point** `적중 / 기각 / 미도래` with dated evidence (filing, news-DB
   `fts --days N`, price). **Adversarial**: hunt the refuting evidence first; do not defend the old call.
   For every 기각 name **which stage's judgment was wrong** (filings? structure? money? valuation?) — that is the lesson.
   Count only matured points into `op_hits` / `op_misses` (미도래 excluded) — this counter is the track record.
3. **Ledger rows for this ticker** — `python -X utf8 scripts/reject_ledger.py due` and
   `python -X utf8 scripts/missed_ledger.py due`; copy the row (date · class · `--revives-if`/`--enters-if`)
   if the ticker appears. Read the book position (`module_paper_book`) — G8 needs both side by side.
4. **Lens** — `python -X utf8 -m module_lens score`, then `due`, then `find "<company> <open question>" --limit 8`
   (commands and rules: L2 [lens](../L2_modules/lens.md)). Any past-due question on this subject is
   resolved now or recorded `AMBIGUOUS` with a reason — never carried silently.
5. **If a desk HANDOVER already ran today**, cite its file for standing view and exposure state; do not redo it.

## ✅ EXIT CHECK
- [ ] Each prior observation point graded with dated evidence, or `최초 리서치` stated.
- [ ] Each 기각 attributed to a stage; op counters updated for matured points only.
- [ ] Reject/missed row and book position for this ticker copied (or `없음`).
- [ ] Lens `score` + `due` run; due questions on this subject resolved or AMBIGUOUS with reason; related Q IDs listed.
