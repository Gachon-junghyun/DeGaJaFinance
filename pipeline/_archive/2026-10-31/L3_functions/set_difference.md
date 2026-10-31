# L3 · set_difference — pre-priced set difference (function)

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> compute the alpha as a *set difference*, not a multiple opinion. This is the engine of Block C.
> **Pure method — no module, no external call.** Its inputs are two lists the caller already built.

- **Role**: given ① what the market already knows and ② what I actually measured, return the two
  differences that matter. Replaces the "high multiple → sell / low multiple → buy" reflex (valuation veto).
- **Input**:
  - **① market-knows** — consensus target & rating (`module_valuation`), analyst narrative, news-DB
    story (`module_news_data`), 52w-range implied expectation, rally decomposition (E-driven vs multiple-driven).
  - **② I-measured** — the concrete findings from Block A (product/bottleneck/moat) + Block B
    (accruals/money-trail) + Block D (ops intel), each carrying its `[검증함]/[차트만]/[직감]` label.
- **Compute**:
  - **② − ① = alpha_delta** — what I verified that the tape/consensus has *not* priced. This is the scoop.
  - **① − ② = risk I have not seen** — what the market prices that I could not confirm. This is the blind spot.
- **Guard**: to write "already priced in" you MUST attach the *list* of what is priced — a bare
  "밸류 부담" is rejected. A high PER is an **input** to ①, never a standalone verdict.
- **Output**: `{priced_in:[…], measured:[…], alpha_delta:[…], risk_unseen:[…]}`.
  Feeds the verdict's REAL vs REAL-but-PRICED split (alpha_delta empty ⇒ PRICED). **No verdict here** (P4).
