# L3 · contract_alpha — contract / backlog decomposition (function)

> **Single-role unit.** Independent — no ordering; an L2/L1 calls it when needed. Does ONE thing:
> turn a 수주공시 (single supply-contract disclosure) into the numbers an analyst actually models —
> not "big order 👍" but book-to-bill, revenue-conversion timing, counterparty, and per-unit price.
> No judgment — it emits the decomposed figures; the caller reads them against demand.

- **Role**: decompose each material contract/backlog item into revenue-relevant quantities.
- **Input**: ticker (KR 6-digit) · the disclosure stream.
- **CLI**:
  ```bash
  python -X utf8 -m module_disclosure <code> --days 400   # 수주(단일판매·공급계약) rows + rcept 원문
  python -X utf8 -m module_business   <code>              # annual revenue (the book-to-bill denominator)
  python -X utf8 -m module_math_check                     # verify each ratio
  ```
- **Decompose (each `[검증함, rcept_no]`)**:
  1. **계약금액 / 매출대비%** — contract value ÷ trailing annual revenue (공시의 "매출액 대비" 필드가 있으면 그대로, 없으면 계산).
  2. **Book-to-bill proxy** — Σ(신규 수주, 최근 N개월) ÷ 같은 기간 매출. >1 = 백로그 팽창(수요 가속), <1 = 소진.
  3. **매출 전환 타임라인** — 계약기간(시작~종료)에서 언제 매출로 인식되는지(균등/후행). 단발 대형계약은 lumpiness 주의.
  4. **상대사 실명** — "글로벌 대형기업" 같은 익명이면 뉴스DB·밸류체인으로 추정하되 [직감] 라벨. 실명 공시면 [검증함].
  5. **단가/물량** — 공시에 수량·단가 있으면 per-unit; 없으면 미확보.
- **Output**: `{contracts:[{date, value, pct_of_rev, counterparty, period, conv_timeline, [label]}], book_to_bill, note}`.
  The caller (CHAIN_ALPHA / money_trail) reads book-to-bill against reported revenue growth. **No verdict here** (P4).
