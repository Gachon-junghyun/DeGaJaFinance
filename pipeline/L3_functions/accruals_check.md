# L3 · accruals_check — quality-of-earnings forensics (function)

> **Single-role unit.** Independent — no ordering; an L2 calls it when needed. Does ONE thing:
> turn reported profit into *cash-verified* profit. This is the deterministic engine of Block B2
> ("is the earnings real?"). No judgment — it emits the gaps; the caller decides.

- **Role**: measure whether reported net income is backed by cash, not accruals/one-offs.
- **Input**: ticker (KR 6-digit) · latest annual + quarter figures.
- **CLI (numbers first, arithmetic checked)**:
  ```bash
  python -X utf8 -m module_business  <code>            # DART 사업보고서: revenue, segment, ASP, receivables notes
  python -X utf8 -m module_valuation <code>            # EPS/PER/PBR (market-implied E)
  python -X utf8 -m module_disclosure <code> --days 120 # earnings filings (분기/사업보고서 rcept)
  python -X utf8 -m module_math_check                  # verify every derived ratio
  ```
- **Compute (each with a `[검증함]` label, blanks stay blank — never guess a line)**:
  1. **NI ↔ OCF gap (accruals)** — 영업이익/순이익 vs 영업활동현금흐름. Persistent NI≫OCF = accrual-heavy earnings.
  2. **Accrual ratio** — (NI − OCF) / avg total assets. Higher = lower earnings quality.
  3. **Working-capital tell** — 재고·매출채권 증가율 **vs** 매출 증가율. Receivables/inventory outrunning sales = channel-stuffing / demand-pull risk.
  4. **SBC / revenue**, **capex vs D&A** (under-investing inflates FCF), **one-off isolation** (분리 후 recurring E).
- **KR data note (honest)**: DART cashflow is annual/semi-annual granular; if OCF for the latest quarter is
  未공시, compute on the most recent full period and label the staleness. No US-style XBRL quarterly cashflow.
- **Output**: a QoE row set `{metric, value, [검증함]/미확보, read}` — e.g. "NI 8,300억 vs OCF 3,100억 → accrual gap 5,200억 [검증함] = 이익의 질 낮음". The calling L2 (money_trail) folds it into the money verdict; **no verdict here** (P4).
