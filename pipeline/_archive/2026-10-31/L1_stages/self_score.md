# L1 · SELF_SCORE — STEP 0.5 revisit self-scoring (stage)

> Phase 0.5 (required when the ledger has a prior verdict for this code). Before any new reasoning,
> **grade the last report** — this is the routine's falsification memory. Skipped only on a first-ever
> research of a code. Calls L2/L3 for the evidence. Output: a delta block into REPORT + `prev_op_review`.

## Why this exists
A forensic desk that never checks its own prior calls is just narrative. The ledger's dated
observation_points are the receipts; SELF_SCORE cashes them. The KPI is not report count — it is
"could I put real money on this desk's word?", and only the hit/miss track record answers that.

## What this stage does
- Load `prev_research` from the ledger (loaded in FORENSIC_PACK). For **each** prior observation_point,
  grade **적중 / 기각 / 미도래** with evidence from: today's DATAPACK, news-DB (`fts --days …`), and price/chart.
- For every **기각** (miss), name *which block's judgment was wrong* last time (A? B? C?) — that is the lesson.
- **Adversarial stance**: do not defend the prior verdict. Hunt the refuting evidence first.
- Write the grades as a block directly under the REPORT delta line; mirror into `verdict.json.prev_op_review`.
- Accumulate **only matured** points into ledger `op_hits`/`op_misses` (미도래 excluded) — this counter is
  the promotion track record (§0 참고-only → binding).

## ✅ EXIT CHECK
- [ ] Every prior observation_point graded 적중/기각/미도래 with dated evidence (or "prev 없음 — 최초 리서치" stated).
- [ ] Each 기각 attributes the error to a specific block. op_hits/op_misses incremented for matured points only.
- [ ] No defense of the old verdict — refutation attempted first.
