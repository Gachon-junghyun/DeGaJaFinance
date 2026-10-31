# STANDING_VIEW — the live thesis carried between runs (thin spine)

> **What this is.** The *currently valid* beliefs only: regime call · seed measured chain · the asymmetry ·
> **§5 retracted ledger (every ID, one line each — lossless)** · open contradictions. Rebuilt 2026-10-31 from
> [`_archive/2026-10-31/STANDING_VIEW.md`](_archive/2026-10-31/STANDING_VIEW.md) (967 KB, 5,469 lines), which is kept **byte-identical**.
> Every row below names its date and its archive line (`A:Lnnn` = that archive file, line nnn).
> **When to read:** HANDOVER, every run, in full. **Not here:** per-run append blocks, spent fact rows, the
> asof chain, in-run self-corrections — all in the archive; reach them with `grep -n` or
> `python -X utf8 -m module_evidence cite <words>` / `show <M####>` (it scans `handoff/**` incl. `_archive/`).
> Tags: `[measured]` / `[inferred]` — an inferred claim may be carried, never cited as evidence. Not advice.

**Freshness.** Last runs that wrote here: `industry_kr` **2026-09-28** (pre-open; last settled KR session 09-23) ·
`industry_US` **2026-09-27** (last settled US bar 09-25). A 2026-10-15 `industry_US` output exists in `llm_outputs/`
but wrote nothing back here. ⇒ **Every market row below is ≥ 33 days old on 2026-10-31 — re-measure before use (P6).**

**Write rule (new).** Append a run block here only for: a regime change · a new `R` (§5, one line, same format) ·
a new/closed contradiction (§6). Fact rows go to `STANDING_VIEW_{US|KR}.md`; numbers for dated questions go to
`module_lens`. Keep this file ≤ 30 KB; move older blocks to `_archive/<date>/`, never delete.

## 1. Regime call

**"Memory is a price-cycle industry with tight levels and a decelerating rate of change."** `[inferred]` — unchanged
in sentence since 2026-07-22 (A:L72). The equity tracks the **second derivative of price**, not the level (lens L1).
- KR measured leg (2026-09-28 `industry_kr`, A:L5456): 000660 2Q26 GM **83.2%** (record) with the increment
  +10.5 → +3.9pp and revenue QoQ +60.2% → +50.9% (DART) — level at record, rate decelerating; `M1582` GM ΔΔ negative
  two quarters. Exogenous input = **MU's print, transmitting to 000660 only** (ρ +0.65, n=29; 005930 ρ +0.15) `M1687`.
- US state (2026-09-26/27 `industry_US`, A:L5377, A:L5430): three real-rate legs (10y 5.18%, 19-year high; real +22bp,
  breakeven 0bp — `M1675`) that the index absorbed; `hy_oas` 2.66 → 2.80 (first credit response, still low). The OW side
  narrowed to a **semis(+semicap) node, price-led, AI attribution unconfirmed** (`R152` killed sector-unit IT OW).
  Node = two mechanisms: memory (price cycle; contracted-volume ceiling/floor of unknown share) and semicap (order-book
  cycle, no floor); MU's print moves the node (23 prints, corr +0.72 with SMH−SPY — `M1684`).
- US sector matrix carried 09-27 (0 deltas vs 09-26 post-DEEP, A:L5436): `IT N+ (semis+semicap node OW)` · `ENRG N` ·
  `COMM N` · `HLTH N` · `STPL UW` · `INDU UW` · `FIN UW−` · `DISC UW` · `RE/UTIL UW−` · `MATR UW`. Correlated: IT-semis OW +
  FIN/UTIL/RE/STPL UW = **one tech-vs-duration factor** (XLK−SPY vs duration-trio corr −0.70, `M1669`).
- Dated tests that were pending at the last write (all now past — score via `module_lens due` / `SCENARIOS.md`):
  `P173` 09-28 · `S171` PCE + `S170` MU 09-30 · `P174` 10-01 · `S172` NFP + `P175` 10y 10-02.

## 2. Seed measured chain (the evidence under §1)

Seed rows from 2026-07-22 (A:L81–L238, verbatim there with full source columns). Later fact rows live in the market
halves and the archive; `module_evidence show M####` returns any of the ~1,700 numbered claims.

| # | Fact | Value (shortened — archive has the full row) | Source | asof |
|---|---|---|---|---|
| M1 | Server DRAM contract price, QoQ | 1Q26 +90~95% → 2Q26 +58~63% → 3Q26 +13~18% | TrendForce | 2026-07 |
| M2 | Micron gross margin, quarterly | 37.7 → 44.7 → 56.0 → 74.4 → 84.6% | yfinance x SEC XBRL (4/4 quarters agree… | FQ3'26 |
| M3 | Micron gross margin, annual | FY22 45.2% · FY23 −9.1% · FY24 22.4% · FY25 39.8% | same | FY25 |
| M4 | Prior-cycle GM peak | 59% (Q4 2018) | press | 2018 |
| M5 | Micron FQ3 revenue | $41.5B, +74% QoQ, +346% YoY; FQ4 guide $50B / GM ~86% | company release | 2026-06-24 |
| M6 | Micron forward P/E · forward EPS | 6.31x · $153.74 (price $970.82) | module_fundamentals_us | 2026-07-22 |
| M7 | New DRAM capacity online | SK M15X + Micron Idaho mid-2027; Samsung P5 2028 | press | 2026-07 |
| M8 | Hyperscaler 2026 capex | >$800B (consensus ~$1T for 2027); Alphabet guide $180–190B, 2027 "significantly increase" | press / Alphabet Q1 | 2026-04 |
| M9 | Memory share of hyperscaler capex | ~8% (CY23-24) → ~30% (CY26) → 48% est. CY27 | SemiAnalysis / CLSA `[est]` | 2026-07 |
| M10 | KR 20d investor flow | 005930 foreign −40.13M sh vs retail +31.16M · 000660 −7.22M vs +7.74M · 042700 foreign +1.40M | KIS (matches Naver + KRX exactly) | 2026-07-21 |
| M11 | KR short-interest (%float) | 005930 0.01% · 000660 0.01% · 042700 5.32% covering | KRX | 2026-07-22 |
| M12 | KR exports, 1–20th of month | Jul $54.93B (semis $22.11B, +180.6% YoY) vs Jun $61.9B = −11.3% MoM | Korea Customs | 2026-07-21 |
| M13 | EDA lead-lag vs SOXX/SMH | same-month +0.63; lag-12 +0.05; lag-18 −0.05 (SPY-excess: +0.24 / +0.02 / −0.06) | own calc, 199 monthly obs 2010–2026 | 2026-07-22 |
| M14 | MU estimate revisions | +1y EPS 100.53 → 150.91 over 90d (+50.1%); breadth 30↑ : 0↓ (30d) | module_fundamentals_us (new axis) | 2026-07-22 |
| M15 | GOOGL estimate revisions | Current quarter 1↑ : 4↓ (30d), next quarter 2↑ : 3↓; +1y level +9.7% | module_fundamentals_us | 2026-07-22 |
| M16 | Credit spreads | HY OAS 2.69% (365d low 2.63, −16bp/90d) · IG OAS 0.78% · NFCI −0.54 | module_macro_us (new axis) | 2026-07-20 |
| M18 | MU gross margin, 17-year series | peak FY2018 58.9% · trough FY2009 −9.2% (FY2023 −9.1%) · median 32.0% → current 84.6% = 100th percentile… | own calc, SEC XBRL (`scripts/margin_his… | 2026-07-22 |
| M19 | Estimate-revision IC (US, single date) | Two non-overlapping windows: W1 (sig 90→60, ret 60→30) +0.36 · W2 (sig 60→30, ret 30→0) +0.28 → folded +… | own calc, `scripts/measure_ic.py` | 2026-07-22 |
| M17 | Implied moves | GOOGL ±7.1% (0DTE) · MU ±4.5% · AMD ±3.6% | module_flow --positioning (new axis) | 2026-07-22 |

## 4. The asymmetry that governs every upcoming print (A:L307, verbatim)

> **A hyperscaler capex CUT changes the thesis. A capex RAISE only moves its timing.**

A cut breaks both the volume leg and the price leg at once. A raise confirms volume only — it cannot un-measure M1,
because the long-term agreements that cap price increases are signed **by those same buyers**. Encode this before
each print, not after.

## 5. Retracted ledger — every ID, one line (append-only, NEVER split — both desks read it)

A retracted claim must not resurface. Each line: **ID** · date · the claim once made (shortened) · archive line with the
killing measurement. ⚠ R27–R45 were *reconstructed* after the 2026-08-05 truncation incident (A:L7–L38): claim and
killer are right, original numbers are lost. ⚠ `R62` was issued **twice** (KR and US runs, both 08-12) — both bind.
`R17` · `R17-b` have no ledger row in the archive: they are named only in the 2026-07-24 `industry_US` asof entry (A:L61)
together with `C-A`·`C-B`·`C-C`, so their text is lost (the 07-24 `industry_US` run files in `llm_outputs/2026-07-24/` may hold it).

- **R1** 07-22 · "SK hynix foreign selling is the strongest bearish datapoint" · A:L321
- **R2** 07-22 · "Semi exports +180.6% is a strong bullish catalyst" · A:L322
- **R3** 07-22 · "Low VIX implies 20d underperformance (t −3.5)" · A:L323
- **R4** 07-22 · "20-day excess returns are all deeply negative" · A:L324
- **R5** 07-22 · "EDA weakness leads semis by 12–18 months" · A:L325
- **R6** 07-22 · "Semiconductor demand is real, therefore the sector turns" · A:L326
- **R7** 07-22 · "Real Estate is the purest duration expression on the board" · A:L327
- **R8** 07-22 · "PSX is the cheapest large refiner on forward" · A:L328
- **R9** 07-22 · "AXON is the most accelerating defense name on the board" · A:L330
- **R10** 07-22 · "IT + Real Estate + Utilities underweights are ONE risk concentration (the AI-d… · A:L329
- **R11** 07-23 · "The long-end move is bear-STEEPENING — term premium, not cut-pricing" · A:L331
- **R12** 07-23 · "The C4 refining detachment counter is at 4 consecutive observations" · A:L332
- **R13** 07-24 · "The 000660 flow suspension resolves on a known date — 2026-07-29 opens two-way… · A:L334
- **R14** 07-24 · "yfinance has no KR 2026-07-23 bar" · A:L335
- **R15** 07-24 · "M-01 (FIN OW) — flow led the earnings: HIT" · A:L336
- **R16** 07-24 · "Shipbuilding: the story and the money died together" · A:L337
- **R18** 07-25 · "M-04 (memory gate) = 유지·강화, 삼성전자 institution turning buyer" · A:L338
- **R19** 07-25 · "the diesel-minus-gasoline gap narrowed 35.50 → 32.96 — the FIRST narrowing of… · A:L339
- **R20** 07-27 · "The KR RS baseline to subtract is the 828-name median +26.4, and a positive RS… · A:L341
- **R21** 07-27 · "Korea's 석유제품 최고가격제 caps the RETAIL sale price, so the transmission to refiner… · A:L342
- **R22** 07-27 · "096770 SK이노 · 010950 S-Oil · 078930 GS are ONE bet, not three (index-removed r… · A:L343
- **R23** 07-27 · "STX's gross margin is +15.1pp above its own prior peak" · A:L501
- **R24** 07-28 · "475150 SK이터닉스 is driven by something STRUCTURAL, not thematic — the KKR SPA cl… · A:L349
- **R25** 07-28 · "`capex cut` has returned ~0 for six consecutive measurements, therefore the ca… · A:L350
- **R26** 07-29 · "SKT's −13.09pp crash-day residual is because its 60-day beta 0.263 is STALE —… · A:L351
- **R27** 08-05 · "The pharma shelter property" · A:L544
- **R28** 08-05 · M199's "000660 raised ₩39.89tn and no desk file recorded it" · A:L545
- **R29** 08-05 · M156's "zero domestic articles" on 009150's 06-30 order · A:L546
- **R30** 08-05 · The US-Gulf crack proxy used as a KR read · A:L547
- **R31** 08-05 · "`theme_age` produces zero discrimination on the foreign feed" · A:L548
- **R32** 08-05 · "Financials is the board's only breadth-led sector" · A:L549
- **R33** 08-05 · M168's "the live leg is foreign" on 셀트리온 · A:L550
- **R34** 08-05 · The index-futures 괴리율 leg of M-15 · A:L551
- **R35** 08-05 · M-05″'s two tariff anchors · A:L552
- **R36** 08-05 · M254's residual LEVELS · A:L553
- **R37** 08-05 · 089860's "no thesis at all / zero live narrative" · A:L554
- **R38** 08-05 · M91's "~8 of UNP's 12 revenue growth points are fuel surcharge" · A:L555
- **R39** 08-05 · M146's "XOM is 0% refining" · A:L556
- **R40** 08-05 · The "regulated seven" basket construction frozen into S35 AND S47 · A:L557
- **R41** 08-05 · "The largest crowded short this desk has measured in KR" · A:L558
- **R42** 08-05 · M-15's domestic-liquidation reading · A:L559
- **R43** 08-05 · M-19's generalisation that KR refining 2Q profit is inventory-and-oil-level rat… · A:L560
- **R44** 08-05 · A PREMORTEM line asserting the opposite sign on the S54 leg · A:L561
- **R45** 08-05 · (filed by the 2026-08-04 `industry_US` run alongside R44) · A:L562
- **R46** 08-05 · "A confirmed Hormuz reopening normalises the KR lubricant-base-oil spread" · A:L568
- **R47** 08-05 · "S49-B's break is PRODUCT-LED" · A:L581
- **R48** 08-06 · "S17-ANNEX 의 이중읽기가 처음으로 CONVERGE 한다 — 동일일자 읽기와 ADR-지연 읽기가 둘 다 07-31 에 25% 아래로 내… · A:L651
- **R49** 08-06 · "Health Care is the ONLY sector whose entire green set is volume-lit" · A:L665
- **R50** 08-06 · "Financials' rank-1 breadth (0.15, highest of 11) and its 5 new-🟢 carry the pro… · A:L666
- **R51** 08-06 · "Energy's 0.285 wflow−eqflow concentration gap is the widest on the board and i… · A:L667
- **R52** 08-06 · "Materials' eqflow +0.167 (3rd of 11) and Δ +0.204 (3rd) against 0 greens carry… · A:L668
- **R53** 08-07 · "폴리실리콘 관세가 서명됐는데 B등급 돈축은 따라오지 않았다 — 서사와 돈이 오늘 보드에서 가장 크게 갈렸다" · A:L701
- **R54** 08-07 · "화장품 수출 데이터가 인쇄되지 않았다 — 그래서 090430 아모레퍼시픽의 진입조건 AND 는 미충족이다" · A:L702
- **R55** 08-07 · "금속 섹터 delta +0.141(보드 2위)의 구동은 민주콩고의 구리·코발트 정광 수출 금지다" · A:L703
- **R56** 08-07 · 🚨🚨 "Comm Services' flow is breadth-led and carries a UW → UW− promotion: eqflow… · A:L743
- **R57** 08-07 · "Financials' eqflow +0.1251 is the 2nd-LOWEST of 16 sessions" · A:L744
- **R58** 08-07 · "VST reports AMC, so the S62 contamination cannot mechanically hit S62's own se… · A:L745
- **R59** 08-07 · "`velocity` is populated on EXACTLY universe mcap-ranks 1–51, zero exceptions (… · A:L746
- **R60** 08-08 · "폴리실리콘 232조 관세는 셀·모듈 전층에 원산지 무관으로 걸리므로 010060·009830 에 음(−)의 다리다" · A:L805
- **R61** 08-08 · "🟢FRESH = 0 for N consecutive foreign measurements is ARITHMETIC — the gate nee… · A:L832
- **R62** 08-12 · "475150 SK이터닉스의 지배권 인수자는 KKR" · A:L1033
- **R62** 08-12 · "S57's branch A will fire and it means NOTHING about Materials — 85% of the obs… · A:L1051
- **R63** 08-12 · "두 번째 연기는 flow 와 무관하게 명제를 끝낸다" · A:L1034
- **R64** 08-13 · "Five of six names in the memory sub-chain carry the identical signature — stro… · A:L1109
- **R65** 08-13 · "`XLE`'s 5-session excess vs SPY collapsed to −0.09 while crude rose 10.70% — t… · A:L1110
- **R66** 08-13 · "`AVGO` · `NVDA` · `ANET` · `HPE` — 4 of 11 = the AI-compute epicentre" · A:L1111
- **R67** 08-13 · "Energy's narrative leg is decaying" · A:L1112
- **R68** 08-13 · "The HLTH leg is devices + tools; biotech is not in it" · A:L1113
- **R69** 08-14 · "Financials is the board's only breadth-led sector" · A:L1194
- **R70** 08-15 · "The Fed-hike premium is an OIL function" · A:L1265
- **R71** 08-16 · "🟢LIVE has fired zero times because the board structurally cannot produce a FRE… · A:L1359
- **R72** 08-16 · "051900 LG생활건강 is not on the board" · A:L1360
- **R73** 08-16 · "The long end is repricing TERM PREMIUM — 30y−10y widened +0.48 → +0.56 with `D… · A:L1411
- **R74** 08-17 · "010950's 2Q26 refining OP fell −48.8% QoQ because the refining MARGIN itself c… · A:L1413
- **R75** 08-17 · "S47-KR's scored ratio 재고관련이익 ₩113,700m ÷ 정유 OP ₩532,400m = 21.36% rests on a f… · A:L1414
- **R76** 08-17 · "`D277` — the velocity survivor set is MONOTONE-NESTING: 51 → 51 → 50, with ZER… · A:L1437
- **R77** 08-17 · "`D276` — the news bridge FLICKERS on a minute timescale, and a sequential full… · A:L1438
- **R77-REARGUED** 08-18 · `R77`(2026-08-17 `industry_US` 등록) — 「뉴스 다리는 분 단위로 명멸한다」를 회수하고 「실패는 전송이 아니라 전수… · A:L1490
- **R78** 08-17 · "`TGT` is 🟢가속" · A:L1439
- **R79-REARGUED** 08-19 · `R77`(08-17 US 등록) → `R77-REARGUED`(08-18 KR) 계보의 3차 교정. 08-18 KR 런은 *"블록 명멸이 살… · A:L1508
- **R80** 08-19 · `R79-REARGUED`'s determinism corollary — *"~50-call quota per ~2-min window; th… · A:L1532
- **R81** 08-19 · `M25` — *"the US 🟢 tag is a volume-surge count, not a flow count: with `velocit… · A:L1533
- **R82** 08-19 · This run's own `SECTOR_ROTATION §2b` promotion of Consumer Staples UW− → UW, ca… · A:L1534
- **R83** 08-19 · The 2026-08-17 `F1` mechanism — *"`theme_age` caps its own age readout at `">=9… · A:L1570
- **R84** 08-20 · 어제(2026-08-19) PREFLIGHT 이 「확정」으로 적은 `M726` 의 형태 — *"뉴스 다리의 실패 메커니즘이 ~2분 창당 ~50… · A:L1605
- **R85** 08-20 · 오늘 이 런의 MACRO 헤드라인 첫 판 — *"어제 −5.8% 는 「투매」가 아니었다. 거래량이 없었다. … 지수는 −5.8% 빠졌는데 중앙… · A:L1606
- **R86** 08-20 · `P74`, registered by this same desk 24 hours earlier: *"the beta correction, no… · A:L1627
- **R87** 08-20 · The refiner kill-clause carried in `§3a` since 2026-08-19: *"kill = a second co… · A:L1628
- **R88** 08-21 · "The news pipe is down — the ngrok agent behind the edge has gone offline." · A:L1696
- **R89** 08-21 · `P70`'s separator — *"the refiners pay WITHOUT the barrel"* — registered 2026-0… · A:L1743
- **R90** 08-21 · `P65`'s framing — *"the long end is a BULL steepener and `DGS2` is not pinned"*… · A:L1744
- **R91** 08-22 · 「건설에는 돈이 없다」 — `breadth 0.04`(26종 중 녹색 1종, 최근에는 0종)를 근거로 8~9런 연속 DEEP 파일과 ROTAT… · A:L1784
- **R92** 08-22 · 「`^KS11` 벤치 결함은 지연이지 드롭아웃이 아니므로 고치기 싼 문제다」 — `D291-KR` 이 08-21 에 그렇게 닫혔고, 그래서 승… · A:L1785
- **R93** 08-22 · "Kevin Warsh's Jackson Hole debut is TODAY, 2026-08-21" · A:L1870
- **R94** 08-23 · 「006360 GS건설은 한 다리 매집이다 — 기관 +419.2만 vs 외국인 −65.7만」 — 08-21·08-22 §3b 가 *"⚠ 한 다… · A:L1966
- **R95** 08-23 · 「005930 삼성전자는 두 다리가 다 판다 — 외 −445.2만 · 기 −423.0만 · 개 +781.3만」 — 08-21 §3b 의 005… · A:L1967
- **R96** 08-23 · "The partial-coverage tag layer is selection-biased UPWARD — three names were p… · A:L2011
- **R97** 08-24 · 「`D303-KR`(000660 08-14 파생상품거래손실 공시 미개봉)를 이 런이 4런 만에 처음 열었다」 — 오늘 `HANDOVER §★③… · A:L2062
- **R98** 08-24 · "The ledger is `market=kr` … the US desk has no equivalent measurement and ther… · A:L2147
- **R99** 08-25 · 「`^KS11` 벤치의 08-24 결함은 지연이다」 — 오늘 `preflight/PREFLIGHT.md §①` 이 그 단어를 썼다(*"결측이… · A:L2305
- **R100** 08-25 · 「자사주 소각 서사는 뉴스에 없고 공시에만 있다」 — `자사주소각` 총 1건 · 0.00× 🔴 를 근거로 6런 동안 실렸고, 어제 `M-100… · A:L2306
- **R101** 08-25 · "`server prices` reads 🟡ACCELERATING 6.79× (base 34)" · A:L2429
- **R102** 08-26 · "IRS short-end strength = the August back-to-back hike is pre-priced" · A:L2608
- **R103** 08-26 · ★★★ "The news axis fails because the 300-query SWEEP overloads the tunnel — the… · A:L2723
- **R104** 08-26 · "`RUBIN` entered the blind-spot pass at z 8.4" · A:L2724
- **R105** 08-27 · ★★ *"The MPC consensus moved from a coin-flip to 8:2 hold, therefore the inform… · A:L2926
- **R106** 08-27 · "July PCE prints on 2026-08-28." · A:L3099
- **R107** 08-28 · "On a hike day, a ≥5bp FALL in the KTB 3y means the hike was already priced in." · A:L3324
- **R108** 08-29 · ★★★ "The `rs20` bench-misalignment bias is a constant offset, therefore CROSS-S… · A:L3434
- **R109** 08-29 · "`module_KIS --investor` returns 10 rows regardless of the argument, therefore… · A:L3435
- **R110** 08-30 · ★★ "The foreign news ingest has been dark for two days" (`M1090`) — written int… · A:L3539
- **R111** 08-30 · "`MU` has no take-or-pay structure and no floor/ceiling band, therefore a contr… · A:L3540
- **R112** 08-30 · `D298`: "`GOOG` (Class C) is entirely missing from this run's per-name JSON des… · A:L3541
- **R113** 08-31 · `M-117` 의 핵심 절 — *"KRX 는 그 다음 사건(잭슨홀)을 아직 거래하지 않았다 … 08-31 개장은 이 사건 위에 「매파 연준」이… · A:L3600
- **R114** 08-31 · 오늘 이 런 자신이 08:30:04 에 `preflight/PREFLIGHT.md` G1 에 쓴 문장 — *"회복(+6분)과 재차단(+7분)이… · A:L3601
- **R115** 08-31 · ★ "`fast_info.previousClose` is a third, simpler recovery path for the 2026-08-… · A:L3647
- **R116** 08-31 · "Brent fell despite the escalation" · A:L3648
- **R117** 09-01 · "`rs20` is unaffected by the asof misalignment — median 0.0, 49.1% positive, a… · A:L3730
- **R118** 09-01 · "`M-118`: today's session is the first observation that separates the tariff la… · A:L3731
- **R119** 09-01 · "`005930`·`000660`: Fwd 5.0x sits on top of an all-time-high gross margin — it… · A:L3732
- **R120** 09-01 · "The 5m-proxy close error is ≤ 0.0448% with 0 names over 0.05%" · A:L3823
- **R121** 09-02 · "Every in-window US item on the Strait of Hormuz is rhetoric, not a dated actio… · A:L3917
- **R122** 09-02 · "The `rs20` alignment bias is harmless today — median 0.00" · A:L3918
- **R123** 09-02 · "`096770` SK이노베이션 is not a pure refining proxy BECAUSE of SK On's 1.5tn KRW US… · A:L3919
- **R124** 09-02 · "`088350` 한화생명 KIS 20-day foreign net-buy +818만주 = the board's largest, 7x the… · A:L3920
- **R125** 09-02 · "The 5m-proxy repair injects ZERO `obv_state` label flips (0 of 42)" · A:L3947
- **R126** 09-02 · "California Wildfire Legislation Postponed, Utility Stocks Bounce = a dated cau… · A:L3948
- **R127** 09-05 · "`^KS11` and `^KQ11` have no 2026-09-04 close — the index level does not exist;… · A:L4073
- **R128** 09-05 · "The observable surface of KR trade risk has MOVED from 'US reciprocal tariffs'… · A:L4074
- **R129** 09-05 · "`S130` (`NVDA` / Hugging Face) is a dead thread" · A:L4103
- **R130** 09-06 · "「금속이 팔렸다」는 오늘 성립하지 않는다. 「비철이 팔렸다」이다." · A:L4197
- **R131** 09-06 · "이 런이 측정한 유일한 행렬×흐름 괴리가 금속에 있다" · A:L4198
- **R132** 09-06 · "수출은 사상 최대인데 네 이름 모두 `rs60` 이 음(−)이다 ⇒ 「기록적 수출」은 60일 상대성과를 만들지 못했다" · A:L4199
- **R133** 09-06 · "금속 노드 분해: 비철 = ['영풍','동국제강','고려아연','동국씨엠','알루코','풍산','대양금속'] (n=7), 교차 쌍상관 중앙… · A:L4200
- **R134** 09-06 · "The 13-outlet Venezuela 'blindsided' story is title-only across every outlet t… · A:L4223
- **R135** 09-06 · "Venezuelan crude is heavy sour — the design feed of the US Gulf Coast complex,… · A:L4224
- **R136** 09-07 · "처방은 「더 많은 텀」이 아니라 「더 긴 텀」이다" · A:L4302
- **R137** 09-07 · "보험 4종이 한 위험단위이므로 보험 섹터가 한 단위" · A:L4303
- **R138** 09-07 · "「보험 `OW−`」와 「금융 `N−`」는 두 개의 판정이다" · A:L4304
- **R139** 09-07 · "Share-normalized the entire board collapses to ±5% flat, with a median of −1.4… · A:L4349
- **R140** 09-07 · "the 50 names that do carry a velocity are positions 0–49 = the 50 largest caps" · A:L4350
- **R141** 09-07 · "the uniform decline is produced by a truncated final day; re-run the identical… · A:L4351
- **R142** 09-07 · "`MSTR` — the board's largest 20-day momentum (+46.7%)" · A:L4352
- **R143** 09-08 · "`wflow` ≈ `eqflow` is the signature that a sector is NOT one name" · A:L4403
- **R144** 09-08 · "M-130's 파병 vocabulary leg is UNMEASURABLE" · A:L4404
- **R145** 09-08 · "`M-135` branch (a) requires the `search` count to sit within ±30% of the event… · A:L4405
- **R146** 09-08 · "The `fts` two-character failure is worked around by quoted juxtaposition — `\" · A:L4406
- **R147** 09-08 · `D427`'s stated cause — *"H.15 does not publish on a federal holiday, so `DGS2`… · A:L4427
- **R148** 09-09 · "The news-API cooldown after a sweep is 65–85 seconds" · A:L4484
- **R149** 09-20 · "2026-09-18 oil fell ~6% (WTI 95.47 −6.32% · Brent 98.77 −5.77%, Brent below 10… · A:L5146
- **R150** 09-21 · "The KR single-name 09-18 yfinance D+0 Close carried the after-hours print (4/4… · A:L5172
- **R151** 09-23 · "The KR bank-holdco sub-unit is a low-beta defensive basket: it wins on index-d… · A:L5196
- **R152** 09-26 · "IT is OW at the sector unit (capped)" · A:L5392
- **R17 · R17-b** 07-24 · retracted by the 2026-07-24 `industry_US` run; no ledger row survives · A:L61

## 6. Open contradictions (carried deliberately — do not resolve by picking a side)

Numbered `C`s: registration gist · registered · last mention in the archive. ★ = named "carried" in the last
`industry_US` §6 (2026-09-27, A:L5444–L5458). Others: status is whatever the last-mention line says — **not re-judged here** (P6).
⚠ For `C1–C5` the last mention can be the RESEARCH rule of the same ID, not the contradiction. `≤07-28` = registered in the pre-split body (07-22…07-28).

- **C1** reg ≤07-28 · LTA price floors. They cap the upside (TrendForce's stated reason for dece… · def A:L372 · last A:L3448 (08-29)
- **C2** reg ≤07-28 · 009150 Samsung Electro-Mechanics. Flow out, relative strength top-quartile… · def A:L375 · last A:L3333 (08-28)
- **C3** reg ≤07-28 · Level vs rate. "Shortage through 2027" (M7) and "price growth decelerating… · def A:L411 · last A:L5152 (09-20)
- **C4** reg ≤07-28 · The refining node: margin or war premium? Both readings survive their own… · def A:L413 · last A:L5368 (09-26)
- **C5** reg ≤07-28 · Security/observability: the strongest measured momentum meets the weakest… · def A:L430 · last A:L4991 (09-18)
- **C6** reg ≤07-28 · The un-narrated branch. Going into the 07-22 hyperscaler print, `"capex cu… · def A:L436 · last A:L445 (07-28)
- **C7** reg ≤07-28 · Health Care: the biggest belief-vs-money gap on the board, and both readin… · def A:L450 · last A:L688 (08-06)
- **C8** reg ≤07-28 · Information Technology is one label over three legs that want opposite ver… · def A:L461 · last A:L461 (07-28)
- **C9** reg ≤07-28 · KR's own edge axis is missing from the instrument that ranks its sectors.… · def A:L400 · last A:L400 (07-28)
- **C10** reg ≤07-28 · Is "renewables = oil-linked" still true? Registered 2026-07-28. · def A:L361 · last A:L5113 (09-19)
- **C11** reg 08-19 · the two OBV instruments disagree, and the desk does not yet know whether i… · def A:L1538 · last A:L1975 (08-23)
- **C12** reg 08-19 · `NUE` (a book holding) has two admissible axes pointing opposite ways, one… · def A:L1574 · last A:L1680 (08-20)
- **C13** reg 08-19 · the name carrying the Staples promotion is the one whose estimate axis con… · def A:L1581 · last A:L1681 (08-20)
- **C14** reg 08-23 · IT/전기·전자에서 C급 폭 지표와 A급 수급이 정반대를 가리키고, 두 축 다 이 데스크가 인정한 축이다. C급: `eqflow` −… · def A:L1995 · last A:L3448 (08-29)
- **C15** reg 08-24 · `breadth`(🟢율)와 `participation`(OBV매집 ∧ rs20>0)이 KR 섹터 순위를 크게 다르게 매기는데, 두 지… · def A:L2105 · last A:L3448 (08-29)
- **C16** reg 08-25 · ★★★ The desk's two admissible instrument families disagree about who is wi… · def A:L2466 · last A:L3448 (08-29)
- **C17** reg 08-26 · (opened by this run — ⚠ first drafted as `C16` and CORRECTED at write time… · def A:L2628 · last A:L3448 (08-29)
- **C18** reg 08-26 · ★★ The desk's two short-interest instruments disagree about DIRECTION, and… · def A:L2759 · last A:L3526 (08-29)
- **C19** reg 08-27 · ⚠ Ledger revival conditions whose observable is a DESK ACTION, not a marke… · def A:L2971 · last A:L3448 (08-29)
- **C20** reg 08-27 · 🚨 The freshness gate's own base filter excluded the theme that actually dr… · def A:L2972 · last A:L3151 (08-27)
- **C21** reg 08-27 · ★★ The desk's own screener and its own chart module disagree about what "R… · def A:L3137 · last A:L5113 (09-19)
- ★ **C22** reg 08-30 · carried unresolved (the two ledgers name different hands; the `HII` reviva… · def A:L3558 · last A:L5447 (09-27)
- ★ **C23** reg 08-30 · the desk owns two different books and every stage reads whichever one its… · def A:L3545 · last A:L5447 (09-27)
- ★ **C24** reg 08-30 · a sector's flow instrument and its positioning instrument point opposite w… · def A:L3553 · last A:L5447 (09-27)
- ★ **C25** reg 08-31 · 이 데스크의 두 계기가 같은 이름·같은 날에 OBV 부호를 반대로 읽는다. · def A:L3605 · last A:L5447 (09-27)
- **C26** reg 08-31 · the desk's own DEEP selection rule cannot reach the board's most extreme s… · def A:L3658 · last A:L5113 (09-19)
- ★ **C27** reg 09-02 · Two rejection rows on the SAME ticker, filed one day apart by the same des… · def A:L3975 · last A:L5447 (09-27)
- **C28** reg 09-05 · carried from 09-04 · def A:L4173 · last A:L5113 (09-19)
- ★ **C29** reg 09-05 · a desk cannot audit an axis it has no ledger for, and it is currently neit… · def A:L4143 · last A:L5447 (09-27)

Un-numbered, open at the last write:
- US 09-27 (A:L5456–L5458): **book vs OW object** (paper book holds 0% memory, 0% semicap inside the rank-1 cycle) · 09-19 (e)
  *"UW driver may be flow/positioning, not rates"* · semis bid vs AI-DC attribution · tools price vs estimates · `META` flow vs
  estimates · `ANET` flow vs tape · refiner estimates vs refiner equity · airlines vs the barrel.
- KR 09-28 (A:L5462–L5467): KRW strength vs foreign selling (09-23) · Korean memory ADR vs US memory (09-25) · KR cable/PCB
  5-session surge vs US AI-DC flat (09-27) · Hormuz axis direction (Globex Brent up vs one article "below $100").
- KR 09-17 candidate, un-numbered (human call, A:L4850): memory **bottleneck (100% utilisation, LTA expansion) vs
  decelerating margin (GM ΔΔ negative two quarters)** — both true in the same company on the same day.

## 7. Data-plumbing state at the last write (re-check first)

KIS token issuance failing (`EGW00103`) since 09-23 · news collection stopped 2026-09-19 13:54 KST · yfinance `^KS11`
bars intermittently NaN (A:L5468–L5469, A:L5449–L5452). These blocked every investor-flow read in the last six runs.

## Change log
- 2026-10-31 — thinned from the 967 KB file (moved to `_archive/2026-10-31/`, byte-identical) by orchestra branch K3.
