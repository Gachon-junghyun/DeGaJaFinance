# L2 · money_trail — follow the money (orchestration)

> Called by L1s (MONEY_FORENSIC, FORENSIC_PACK). Assembles the **"돈의 진위"** evidence — the axis
> that separates a real business from a narrative: who is actually buying/selling, is the profit cash,
> and do management's *actions* match their *words*. KR has an edge here (per-day investor net-buy +
> short balance) the US book lacks — use it. Reuses existing modules (P1); adds no new API.

## Calls
- **Investor flow (KR edge)** — `python -X utf8 -m module_KIS <code> --investor 20`
  외국인/기관/개인 **일별 순매수 실측**(수량). Strong-hand (foreign) accumulation into a decline ≠ retail
  distribution — the tape's true owner. This is the OBV axis a chart can't attribute.
- **Insider / ownership** — `python -X utf8 -m module_disclosure <code> --days 120`
  DART `equity`(5%·임원 지분변동 = Form4 대응) · `treasury`(자기주식) · `capital`(증자/CB/BW = dilution).
  ⚠ KR insider filings carry **direction + quantity only, no trade price** — no VWAP floor/ceiling. Label 미확보 for price.
- **Short balance** — `python -X utf8 -m module_flow <code>` (KRX 공매도잔고% + OBV/RS/surge). Building short
  interest into a bounce = pressure; crowded short into a base = squeeze fuel.
- **Quality of earnings** — L3 [accruals_check](../L3_functions/accruals_check.md): NI↔OCF, 재고/채권 vs 매출, one-off.
- **Words** — `python -X utf8 -m module_news_data fts search "<한글명>" --days 30 --snippet` (IR statements,
  밸류업/기업가치제고 promises) — the claim side of the 괴리표.

## Output — the 괴리표 (words vs actions), one table
`IR 발언 ↔ 내부자/지분(equity) ↔ 자사주(treasury) ↔ 실제 capex ↔ 투자자수급(foreign/inst)` — each cell
`[검증함]/미확보`. A row where the *words* say growth but insiders sell / treasury shrinks / foreigners
distribute is the tell. **Blanks stay blanks; the calling L1 renders the money verdict, not this L2** (P4).
