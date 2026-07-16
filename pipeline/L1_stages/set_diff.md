# L1 · SET_DIFF — Block C, the pre-priced set difference (stage)

> Phase C (main thread, after Block A + Block B — and Block D if it ran). Converts "is it cheap/expensive?"
> into "what do I know that the tape doesn't?". Calls L3. Output: the Block-C section of REPORT.

## Why this exists
Multiple level alone decides nothing (valuation veto). The edge is a **set difference**: the gap between
what the market already prices and what the forensic blocks actually verified. That gap — not the PER — is
the trade.

## L3 called
- [set_difference](../L3_functions/set_difference.md) — feed it two lists and it returns the deltas:
  - **① market-knows** — consensus target/rating(valuation), analyst & news-DB narrative, 52w-range implied
    expectation, rally decomposition(E-driven vs multiple-driven).
  - **② I-measured** — the labeled findings from Block A(product/bottleneck/moat) + Block B(money) + Block D(ops).

## What this stage does
- **② − ① = alpha_delta** — verified and *not* yet priced → the scoop (drives REAL).
- **① − ② = risk_unseen** — priced but I couldn't confirm → the blind spot (drives caution/BROKEN watch).
- **Sector cross-read**: before synthesizing, read this code's GICS-sector row in
  `llm_outputs/SECTOR_ALPHA_MAP_KR.md` (if present) — does the bottom-up single-name finding *agree or clash*
  with the top-down sector story? A clash is itself alpha or risk. If absent, this company is the first lens on that sector.
- **Guard**: to write "already priced in", attach the *list* of what is priced. alpha_delta empty ⇒ headed for
  REAL-but-PRICED, not REAL.

## ✅ EXIT CHECK
- [ ] ①/② lists both explicit; alpha_delta and risk_unseen both populated (or "비어있음" stated with meaning).
- [ ] No bare "밸류 부담" — every priced-in claim carries its list.
- [ ] Sector map row read/created; agreement-or-clash with the single-name finding noted.
