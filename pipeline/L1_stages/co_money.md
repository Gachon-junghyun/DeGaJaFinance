# L1 · CO_MONEY — is the money real (cash, insiders, words vs actions); flow only confirms

> Company stage 5 (all modes). Merges the old MONEY_FORENSIC, L2 money_trail and L3 accruals_check.
> **Reads (primary)**: cash-flow statement and notes (DART / XBRL), insider and treasury filings
> (DART equity/treasury/capital; Form 4 XML), IR promises (밸류업 공시, call text); flow last.
> **Writes**: `MONEY.md` (cap **6 KB**). **Next stages use**: recurring earnings (CO_VALUE), the words-vs-actions
> table (FALSIFY), the flow row (CO_VERDICT timing line T2 only).

## B1 · Is revenue real
Cross reported growth against independent demand: customer capex, contract filings, delivery references,
CO_STRUCTURE's book-to-bill. Growth no external measure corroborates is suspect.

## B2 · Are earnings real (deterministic; `module_fundamentals_kr` / `_us`, `module_math_check` on every ratio)
1. NI/OP ↔ OCF gap and accrual ratio `(NI − OCF) / avg total assets` (KR half/quarter: cumulative columns — see CO_FILINGS).
2. Working capital: receivables and inventory growth **vs** revenue growth; order-driven industries: **미청구공사/sales and its YoY** first.
3. SBC/revenue · capex vs D&A (under-investing flatters FCF) · one-offs isolated ⇒ **recurring earnings**.
Latest quarter OCF unpublished ⇒ compute on the last full period and label staleness. Blanks stay blank.

## B3 · Words vs actions — one table
`IR statement ↔ insider equity ↔ treasury ↔ actual capex ↔ investor flow`, each cell `[검증함]/미확보`.
Words say growth while insiders sell / treasury shrinks / foreigners distribute = the tell.
- KR insider filings: direction + quantity only, **no price** ⇒ floor/ceiling 미확보.
- 🚨 US Form 4 — parse three more fields (measured 2026-09-03 NVDA): `sharesOwnedFollowingTransaction`
  (⇒ share of holding sold), `directOrIndirectOwnership` (D/I), `natureOfOwnership` (By Trust/LLC).
  Without splitting lines, holdings appear to **rise** 11.54M → 15.02M; split, the 2026-09-02 sale of 1,848,501
  sh was all `I / By Trust`, 35.5% of that line. Check **10b5-1** in the text (NVDA: 98.8% of $828M open-market
  sales by one director, off-plan; the one executive sale, $6.5M, was a plan sale).
- Form 144 whose `aggregateMarketValue` equals the same-window Form 4 (6,536,514 / 3,343,863 / 133,750) is the
  pre-notice of the same trade — do **not** list it as 미확보; a mismatch is the finding.
- 🚨 Equity stakes are marked **per position**, not as a total gain: CoreWeave 10-Q gives 23M sh at $87.20 = $2.0bn ⇒
  at $80.93 (2026-09-02) **−$144M (−7.19%)** under a headline «investment gains ≈ 20% of NI».

## B4 · Flow — one row, confirmation only
KR: `module_KIS <code> --investor 20` foreign/institution daily actuals (**B-grade**: the only surviving leading
axis, 20d NW-t 3.73, but non-stationary — first 18 months IC ≈ 0); overrides OBV (r≈0.49), never the reverse.
Short balance `module_flow <code>`: shorts **supply liquidity** (net-buy→return slope 0.112 → 0.084 → 0.066 across
short-ratio terciles); «building short = bearish» is in the **rejected** ledger. US: FINRA short-vol z (`us_flow.py`) +
`module_flow --positioning`. Read flow as **who owns the move**, never as a reason.
🔴 Measured: flow evidence was right **5 of 32 (0.18)**; «weighted vs equal-weight flow against breadth/volume
thresholds» **0 of 7**. Flow may confirm or contradict; it may not carry the verdict.

## ✅ EXIT CHECK
- [ ] B1/B2/B3 each judged and labeled; accrual gap computed or 미확보 with reason; recurring earnings stated.
- [ ] Words-vs-actions table rendered, every cell 검증/미확보.
- [ ] Flow is one row (≤ 5 lines) read as attribution; no conclusion rests on it alone.
