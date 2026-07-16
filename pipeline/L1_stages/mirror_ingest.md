# L1 · MIRROR_INGEST — sync the real KIS book in (stage) ★mirror-only

> Phase 0. Before any judgment, make the paper book **equal the real account** — so decisions are made
> against what is actually held, not a fantasy book. US-knowledge-limited by default. Calls L2.
> Output: `MIRROR_STATE.md`.

## L2 called
- [kis_sync](../L2_modules/kis_sync.md) — `module_paper_book mirror`: seed the real holdings as already-held
  (from live `module_KIS` balance, or screenshot-derived qty/avg when KIS creds are absent) + set the real cash sleeves.

## What this stage does
- **Mirror the real book (US-limited):** every real US position → a paper position at its true qty/avg-cost;
  the real KRW/USD cash sleeves → the paper cash. A KR holding outside the US-knowledge scope is noted, not traded.
- **Tag each holding's correlation-theme** so the concentration guard is meaningful (e.g. the book's KMI/LNG =
  energy-fuel, VST/CEG = AI-power-IPP — flag when the holdings collapse into one risk unit).
- **Reconcile:** state total assets vs the real account (they should match within fx/price timing); if a mark is
  missing, leave it blank, never fabricate a position.
- ⚠ This overwrites the paper positions with reality (the mirror is the source of truth) — it is the ONLY stage
  allowed to reset the book to the real holdings.

## ✅ EXIT CHECK
- [ ] `MIRROR_STATE.md`: every real US holding seeded (qty/avg), cash sleeves set, KR-scope holding noted.
- [ ] Correlation-themes tagged; any one-risk-unit concentration in the existing book flagged.
- [ ] Paper total assets reconciled against the real KIS total (delta stated).
