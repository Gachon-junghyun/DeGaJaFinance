# L1 · MONEY_FORENSIC — Block B, is the money real (stage)

> Phase B (runs parallel to the reused Block-A product dive). Treats the P&L as a defendant's statement
> and cross-examines it against cash and behavior. Calls L2. Output: the Block-B section of REPORT.

## L2 called
- [money_trail](../L2_modules/money_trail.md) — investor flow(외/기/개) · insider/treasury/capital · short% ·
  L3 [accruals_check](../L3_functions/accruals_check.md)(NI↔OCF·재고/채권 vs 매출·SBC·capex vs D&A·one-off).

## The three questions (each answered with a `[검증함]/[차트만]/[직감]` label)
- **B1 매출이 진짜인가** — cross the reported revenue growth against *physical/independent* demand: customer
  capex, 수주공시(contract), 납품 레퍼런스(news). Growth that no external measure corroborates is suspect.
- **B2 이익이 진짜인가** — the accruals_check output: is NI backed by OCF? are receivables/inventory outrunning
  sales? is capex starving to flatter FCF? Isolate one-offs and restate the *recurring* earnings.
- **B3 말 vs 행동 (괴리표)** — the money_trail table: IR/컨콜 발언 ↔ 내부자 지분(equity) ↔ 자사주(treasury) ↔
  실제 capex ↔ 투자자수급. **밸류업/기업가치제고 공시**가 있으면 약속 지표를 뽑아 실제 행동과 대조.
  A row where words say growth but insiders sell / treasury shrinks / foreigners distribute is the tell.

## Guards
- Numbers only from DATAPACK / DART original (rcept_no). Re-verify any figure from memory.
- KR insider = direction+qty only (no price) → 실링/플로어는 미확보로 둔다.
- High PER is **not** a Block-B verdict — it is an input to Block C's set difference.

## ✅ EXIT CHECK
- [ ] B1/B2/B3 each judged + labeled. Accrual gap (NI−OCF) computed or 미확보-stated with the reason.
- [ ] 괴리표 rendered: words vs insiders vs treasury vs capex vs flows, every cell 검증/미확보.
- [ ] Foreign/inst per-day flow read as attribution (who owns the move), not as a price line.
