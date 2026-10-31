# L3 · filing_diff — Lazy Prices language diff (function)

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing:
> surface what *changed in the words* of consecutive filings. Academic basis = **Lazy Prices**
> (Cohen-Malloy-Nguyen): firms that quietly rewrite risk/business language subsequently
> under-perform — the *change* leads the price. No judgment — it emits the added/deleted sentences.

- **Role**: diff this period's DART 사업보고서 **"사업의 내용" · "사업위험/주요 위험"** sections against the
  prior same-form filing → added sentences, deleted sentences, and a jaccard similarity.
- **Input**: ticker (KR 6-digit) · two most-recent comparable filings.
- **CLI**:
  ```bash
  python -X utf8 -m module_disclosure <code> --days 400   # list 사업보고서/분기보고서 rcept_no (find the two to compare)
  python -X utf8 -m module_business   <code>              # section_text of the latest (the body to diff)
  ```
- **Method (until a dedicated module exists)**: pull the two filings' section bodies, sentence-split, set-diff.
  Low jaccard = large language shift → the **added** sentences are the entry point for close reading
  (where is management moving the narrative?); the **deleted** sentences are the quiet retreat
  (a risk they stopped disclosing, or a claim they walked back).
- ⚠ **Repo gap (honest)**: this repo has no `module_filing_diff` yet (the mvp had `kr_filing_diff`).
  Do the diff best-effort from `module_business` section_text + two `module_disclosure` rcepts, and
  **flag the result `[best-effort]`**. If only one filing is retrievable, emit "미확보 — 직전 대비 불가"
  rather than a fake diff. (Candidate future single-source: `module_disclosure` gains a `--diff` verb.)
- **Output**: `{jaccard, added:[sentences], deleted:[sentences], [검증함]|[best-effort]|미확보}`.
  The caller reads the *added* lines against Block A/B (words vs the money). **No verdict here** (P4).
