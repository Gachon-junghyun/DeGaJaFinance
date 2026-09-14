# L2 · money_trail — follow the money (orchestration)

> Called by L1s (MONEY_FORENSIC, FORENSIC_PACK). Assembles the **"돈의 진위"** evidence — the axis
> that separates a real business from a narrative: who is actually buying/selling, is the profit cash,
> and do management's *actions* match their *words*. KR has an edge here (per-day investor net-buy +
> short balance) the US book lacks — use it. Reuses existing modules (P1); adds no new API.

## Calls
- **Investor flow (KR edge)** — `python -X utf8 -m module_KIS <code> --investor 20`
  외국인/기관/개인 **일별 순매수 실측**(수량). Strong-hand (foreign) accumulation into a decline ≠ retail
  distribution — the tape's true owner. **This is the measured version of what OBV only approximates**
  (OBV correlates r≈0.49 with it, per name 0.005–0.67, and adds no leading information once this is
  known — PLAY19). ★ **Where both exist, this overrides OBV; never the reverse** (carry rule D6).
  ⚠ It is **B-grade, not A**: the only surviving leading axis (20d NW-t 3.73) but **non-stationary**
  (first 18 months IC ≈ 0) — a confirmation layer on top of another reason, never a standalone system.
- **Insider / ownership** — `python -X utf8 -m module_disclosure <code> --days 120`
  DART `equity`(5%·임원 지분변동 = Form4 대응) · `treasury`(자기주식) · `capital`(증자/CB/BW = dilution).
  ⚠ KR insider filings carry **direction + quantity only, no trade price** — no VWAP floor/ceiling. Label 미확보 for price.
- **Short balance** — `python -X utf8 -m module_flow <code>` (KRX 공매도잔고% + OBV/RS/surge).
  Crowded short **covering** into a base = squeeze fuel (turn-conditional, never a standalone buy).
  ⚠ **"Building short interest = bearish" is in the rejected ledger** — indistinguishable from noise
  (PLAY25, 16-month post-resumption power limit). What *was* measured is the opposite framing:
  shorts **supply** liquidity — net-buy→return slope falls monotonically across short-ratio terciles
  **0.112 → 0.084 → 0.066** (all p<0.001), so heavy-short days are easier to execute into. Cite the
  measured version, not the folk version.
- **Quality of earnings** — L3 [accruals_check](../L3_functions/accruals_check.md): NI↔OCF, 재고/채권 vs 매출, one-off.
- **Words** — `python -X utf8 -m module_news_data fts search "<한글명>" --days 30 --snippet` (IR statements,
  밸류업/기업가치제고 promises) — the claim side of the 괴리표.

## Output — the 괴리표 (words vs actions), one table
`IR 발언 ↔ 내부자/지분(equity) ↔ 자사주(treasury) ↔ 실제 capex ↔ 투자자수급(foreign/inst)` — each cell
`[검증함]/미확보`. A row where the *words* say growth but insiders sell / treasury shrinks / foreigners
distribute is the tell. **Blanks stay blanks; the calling L1 renders the money verdict, not this L2** (P4).

---

## 🚨 U4 · Form 4 는 **세 필드를 더** 파싱한다 — 「보유의 몇 %」가 여기서 나온다

`<transactionShares>` 만 읽으면 **총액**밖에 안 나오고, 총액만으로는
「확신 상실」인지 「분산」인지 **판정할 수 없다**(`C4`). 세 필드를 같이 읽어라:

| 필드 | 왜 |
|---|---|
| `<sharesOwnedFollowingTransaction>` | 거래後 잔량 ⇒ **판 비중** = 매도 ÷ (매도 + 잔량) |
| `<directOrIndirectOwnership>` | `D`(직접) / `I`(간접) |
| `<natureOfOwnership>` | `By Trust`·`By LLC` 등 — 신탁·법인 라인인지 |

🚨 **라인을 안 가르면 보유가 «늘어» 보인다.** 실측 (2026-09-03, NVDA·STEVENS MARK A):
여러 Form 4 의 마지막 `sharesOwnedFollowingTransaction` 을 그냥 이어 읽으면
**11,543,401 → 15,017,750 으로 증가**한다(직접/간접 라인 + 다른 accession 이 섞임).
라인을 갈라 읽으면: **2026-09-02 매도 1,848,501주 전량이 `I` / `By Trust`,
거래後 잔량 3,358,770주 ⇒ 그 라인의 35.5% 를 하루에 매도.**

**그리고 `10b5-1` 여부를 본문에서 찾아라** — 플랜 매도면 정보량이 크게 떨어진다.
실측: NVDA 5월 이후 공개시장 매도 $828M 중 **98.8%가 이사 1인이고 셋 다 플랜 밖**,
경영진 매도는 1건($6.5M)이고 **그건 플랜 매도**였다.

## ⚠ U5 · Form 144 는 같은 창의 Form 4 와 **금액이 일치하면 스킵해도 된다**
실측 (2026-09-03 NVDA): 144 의 `aggregateMarketValue` **6,536,514 / 3,343,863 / 133,750** 이
Form 4 집행액과 **완전 일치**했다. 같은 거래의 **사전신고**라 새 정보가 0 이다.
⇒ 「Form 144 미파싱」을 `미확보` 목록에 **올리지 마라** — 값이 없는 칸을 결손으로 세면
결손 목록의 신호대잡음이 떨어진다. (불일치가 나오면 그때가 진짜 발견이다.)

## 🚨 U6 · 지분 포트폴리오는 **총액이 아니라 건별 시가평가**로 잰다
「지분평가익 $X bn」은 방향을 못 준다. **상대방 10-Q 에 매입가·주식수가 있으면 손익이 산출된다.**
실측: CoreWeave 10-Q — *"In January 2026, we entered into a securities purchase agreement with
**NVIDIA Corporation** … approximately **23 million shares** … at **$87.20 per share** …
**$2.0 billion**"* ⇒ 2026-09-02 종가 $80.93 기준 **−$144M (−7.19%)**.
⇒ 「순이익의 20% 가 지분평가익」이라는 총액 서술 아래에서 **개별 포지션은 손실 중**일 수 있다.
