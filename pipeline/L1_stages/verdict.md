# L1 · VERDICT — the forensic verdict (stage)

> Terminal phase. Renders the 4-tier "is this company real?" verdict and writes the ledger — the definition
> of a completed run. **참고-only / binding:false** (§0): the verdict informs, it does not size the book.
> No L2/L3 call — it synthesizes the prior stages. Output: `REPORT.md` + `verdict.json` + ledger merge.

## The verdict (4 tiers)
- **REAL** — product and money both verified, and Block C's alpha_delta is non-empty (market underrates it).
- **REAL-but-PRICED** — real, but ① covers ② (alpha_delta empty) → a pullback-watch name, not a fresh idea.
- **INFLATED** — narrative > substance (Block A moat weak or Block B accruals/괴리표 fail).
- **BROKEN** — substance impaired (demand gone, earnings non-cash, capital structure cracking).

## What this stage writes
- **Delta line = the FIRST line of REPORT.md**: `평결: {직전}→{이번}` (first-ever ⇒ `평결: 신규→{이번}`).
  The market prices the *level*; the forensic axis's *change* leads — for a transition (REAL→INFLATED) add one
  sentence naming *which axis cracked and when*.
- **2–3 dated observation points** — each must be falsifiable: "by {date}, if {Y} does not appear, this verdict is wrong."
  These are what SELF_SCORE / catalyst-check grade next time. They are the receipts.
- **4-layer close**: 1 essence → 2 causal chain → 3 the numbers → 4 one line.
- **verdict.json** (`binding:false`), then **merge the ledger** — observation_points replaced with this run's,
  op_hits/op_misses carried from SELF_SCORE. Forget the ledger merge and rotation + self-scoring break.

## Guards
- Not licensed advice; analytical/illustrative; the book is untouched (READ-ONLY).
- Every quantitative claim traces to DATAPACK or a DART rcept_no. A verdict with an unlabeled number is unfinished.
- On mid-run failure do **not** merge the ledger (so it re-runs next time) and drop a `FAILED.md` with the reason.

## ✅ EXIT CHECK
- [ ] REPORT.md first line is the delta verdict; 4-tier chosen with the cracked/confirmed axis named.
- [ ] 2–3 dated, falsifiable observation points written; verdict.json emitted with binding:false.
- [ ] ledger.json merged (observation_points replaced, op counters carried). Numbers all traceable + labeled.
