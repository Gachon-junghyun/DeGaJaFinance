# MACRO_REPORT — industry_KR · 2026-07-20 (Mon)

> Stage 1 / L1·MACRO. Runtime `--market kr`, English-instructions / KR-market output.
> Primary data: **no same-day US `MACRO_REPORT` exists** (US desk last ran 07-19 without MACRO) →
> **FRED read directly via `module_macro_us --json`** for §1 cross-read, cited `[FRED]` with asof dates.
> News = `module_news_data` via **NEWS API server `http://127.0.0.1:8787` (routed /exec)** — event axis
> (`brief --body 2`) + trajectory axis (`thread --days 7`) + 7-bucket + blindspot.
> KR edge axis = `module_flow` per-investor actuals (KIS) + KRX short interest.
> Deliverable = the **§4 transmission matrix** (ROTATION's input). Zero buy/sell calls.

⚠ **Read this report's timestamp as PRE-OPEN, not full-session.** The 07-20 domestic pool is
**145 articles** vs 472–493 on a normal weekday — the day is ~1/3 collected. Consequence: **head tier
= 0 events at ≥5 outlets** (nothing has yet been carried by 5 desks today), and every FADING tag in
§3b is mechanically inflated by the thin window end. Nothing here may be read as "attention collapsed."

---

## §0 Catalyst injection (`catalyst_calendar --days 5` → `llm_outputs/2026-07-20/CATALYST_WATCH.json`)

| When | Event | Axis | Binary? |
|---|---|---|---|
| **Undated / live** | **Iran "Strait of Hormuz open" (TACO trigger)** | oil | 🔀 **binary, open-ended** → both-sides bracket mandatory (M-02) |
| **07-22 → 07-24** | **김정관 산업장관 방미 — 러트닉 회담, 대미투자 1호 + 조선 + 쿠팡** [mt/sedaily/donga 07-19~20] | trade/policy | 🔀 **binary, D-2** → both-sides bracket mandatory (M-06) |
| D-1 07-21 | SCHW earnings (US fin read-through) | earnings | 🔀 |
| D-2 07-22 | **TSLA** · KMI earnings | earnings | 🔀 |
| D-3 07-23 | RTX · LMT earnings (KR 방산 read-through) | earnings | 🔀 |
| D-2 07-22 | **알파벳 실적** [brief #32 "삼전닉스 반등할까… 알파벳 실적 주목"] | AI-capex | 🔀 → M-03/M-04 both-sides |

★ **The calendar module did not carry the KR-native binary.** `catalyst_calendar` returned only the
Hormuz axis + US earnings; the **방미/대미투자 1호 (07-22 출국, 07-24 귀국)** binary came from the news
body-read, not the calendar. Injected manually above — this is the week's dominant KR-specific event.

---

## §1 Regime read — primary numbers explicit

### ★ KR-native regime spine (inherited, REALIZED 07-16): BOK at **2.75%**, hiking bias
- **한은 기준금리 2.75% 인상 — 만장일치, "3년 6개월 만에 통화 긴축"** [news thread, ENDED 07-14~07-17,
  curve 7→5→8→5, peak 8 outlets]. The 07-16 report scored this as the durable KR spine; **the +4d
  transmission is now measurable in the tape** (§2) and in the credit thread (§3b): 코픽스 3% 돌파,
  주담대 금리 8% 눈앞, 가계 이자부담 +年 3.3조, 대출총량 1.5% 규제.
- ⚠ **The hike thread has ENDED** (attention rotated). Per the trajectory rule, an ENDED thread under a
  still-open proposition is a **staleness flag** — M-01 is re-justified below on *transmission evidence*
  (bank OBV 매집 + 기관 실매수, §2), not on the headline it was born from.

### Cross-read of US primaries [FRED, direct — asof dates explicit]
| Series | Latest | asof | Read-through to KR |
|---|---|---|---|
| Fed funds | **3.63%** | 2026-07-16 | US on hold/easing-mature vs **BOK hiking** — rate gap narrowing, KRW-supportive *in theory* (contradicted by spot, below) |
| US 10Y | **4.57%** (from 4.19 @01-02) | 07-16 | Global term premium ↑ **+38bp YTD** = imported cost-of-capital headwind for KR growth/RE |
| US 2Y | **4.16%** (from 3.47) | 07-16 | Curve **+41bp positive** (10s2s) — no inversion signal |
| **Real 10Y (TIPS)** | **2.35%** (from 1.94) | 07-16 | **+41bp YTD real** — the multiple-compression variable; caps KR long-duration/growth |
| Headline CPI | 332.568 (prev 333.979) | **2026-06-01** | **MoM −0.42%** — matches the 07-16 KR read "美 물가 둔화에 달러 약세" |
| Core CPI | 336.065 (prev 336.121) | **2026-06-01** | MoM ~flat. ⚠ **~1 month lagged** — not a live read |
| Unemployment | 4.2% (prev 4.3) | 2026-06-01 | Slight improvement. ⚠ 1 month lagged |
| DXY (Broad) | 120.50 | **2026-07-10** | ⚠ **10 days stale** — cannot speak to this week's KRW |
| VIX | 16.73 | **2026-07-16** | ⚠ **STALE and load-bearing**: this print **pre-dates** the KOSPI break to 6,600 and today's 반도체 급락. Do **not** cite 16.73 as "no fear" |
| M2 | $23,052.3bn (from 21,938.7 @2025-06) | **2026-05-01** | ~1 month lag; liquidity still expanding |

### ★ The KRW — corrected and current
- **원·달러 1487.28원** [brief #34, 07-20 조세일보, 강보합권]. Week path from the FX thread
  (REIGNITED, 6→6→5→2): **1493 (07-14) → 1484.7 (07-15) → 1480s (07-16) → 1487.28 (07-20)**.
- **The won is WEAK and range-bound near 1,490, not strengthening.** This confirms the 07-16 §5b
  correction and kills any residual "softening-dollar → foreign-inflow tailwind" framing. Note the
  brief carries a *counter*-framed item — "환율 더 떨어지면… 1인당 GDP 4만 달러 초읽기" [#24, 5a/2s] —
  that is a **conditional scenario piece, not a print**; the print is 1487.
- **Structural offset (new, real):** 원화 국제화 is being legislated — "9월부터 해외 은행에서도 원화
  계좌 만들어 실시간 결제" [#10, 4a/3s] on top of the ENDED-but-peak-8 thread "원화로 수출입하면
  인센티브…외국인 국채 대차 허용" [07-15~07-19, 2→2→8]. Slow-burn KRW-positive / KR-bond-access-positive.

**Net regime:** KR = **tightening-into-de-rating**. BOK at 2.75% with a hiking bias, credit visibly
throttled, a weak ~1,487 won, rising US real yields, and an index that broke 7,000 → 6,600. This is a
**cost-of-capital regime, not a liquidity regime** — the winners are cash-flow-now and rate-levered,
the losers are duration and story.

---

## §2 Positioning — ★ the KR edge axis (`module_flow`, KIS per-investor actuals, 20d)

| Ticker | Name | Flow | OBV | RS20 | RS60 | 서지 | 외국인 / 기관 / 개인 (만주, 20d) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 105560 | **KB금융** | 🟢가속 | 매집 | **+35.8%** ★2nd | +1.4% | **1.27x** | −256.6 / **+337.1** / −76.4 | ✅ **real-hands** (기관 매집) |
| 055550 | **신한지주** | 🟢가속 | 매집 | **+31.8%** | −1.8% | 0.94x | −134.8 / **+245.7** / −61.7 | ✅ **real-hands** |
| 010950 | **S-Oil** | 🟢가속 | 매집 | **+62.6%** ★top | **+13.4%** | 1.21x | **+12.6** / **+158.5** / −177.4 | ✅ **real-hands, both sides buying** |
| 207940 | 삼성바이오로직스 | 🟡중립 | 중립 | **+22.4%** | −23.0% | 0.71x | +9.4 / +2.0 / −11.0 | ✅ quiet real-hands, 20d recovering |
| 005490 | POSCO홀딩스 | 🟡중립 | 분산 | +9.6% | **−29.2%** | **0.68x** | +32.4 / −33.1 / +0.6 | ⚠ 혼조, **no money** |
| **005930** | **삼성전자** | **🔴분산** | **분산** | **−4.9%** | +7.9% | 0.89x | **−4,672.6** / +327.8 / **+4,259.1** | ❌ **weak-hands — textbook 외국인 이탈 / 개인 흡수** |
| **000660** | **SK하이닉스** | **🔴분산** | 중립 | **−6.6%** | +53.1% | 1.16x | **−875.4** / −114.2 / **+960.7** | ❌ **weak-hands — same pattern** |
| **034020** | **두산에너빌리티** | **🔴분산** | **분산** | −5.3% | **−45.9%** ★worst | 0.85x | −20.0 / +62.7 / −32.1 | ❌ **money fleeing hard** |

> ✏️ **CORRECTION (applied post-DEEP, 2026-07-20).** An earlier version of this table **shifted the
> `module_flow` columns by one** for the 🟢 rows: `OBV` carries only a *state word* (매집/분산/중립),
> and the two numbers after it are **RS20 and RS60**, not "OBV %" and RS20. Caught by DEEP-FIN.
> Corrected above. **The correction strengthens the FIN call rather than weakening it** — KB's
> relative strength is **RS20 +35.8%**, not +1.4%, against a benchmark that broke 7,000 → 6,600.
> Same fix applied to `SWEEP_READ.md` and `SECTOR_ROTATION.md`. ⚠ Note the default bench matters:
> DEEP-FIN measured 삼성화재 at RS20 −0.2% on the **SPY** default vs +24.9% on **^KS11** — always
> state the bench.

★ **This table is the run's single most decisive input, and it overrides narrative in three places:**
1. **The banks are being accumulated into a falling index** — KB **RS20 +35.8%**, 신한 **RS20 +31.8%**
   (both OBV 매집), **기관 실매수 both**, against a benchmark that broke 7,000 → 6,600. M-01 (hike→NIM) is confirmed on
   *transmission evidence*, not on the (now-ENDED) headline. This is the 07-16 §5a "defensive-into-
   tightening" read, now +4d and still working.
2. **Both memory names are weak-hands.** 삼성전자 foreign **−4,672만주** with retail **+4,259만주**
   absorbing is the exact `⑦` blocked pattern (외국인 이탈 + 개인 흡수 ⇒ OBV '매집' is disqualified).
   The narrative side reads bullish today ("칩플레이션" #1, "펀더멘털 훼손 아니다" #22, 최태원 "갖고
   있어라") — **the money says the opposite.** Narrative and flow are on opposite sides of this trade.
3. **S-Oil is the board's best relative performer (RS20 +62.6%, RS60 +13.4%) with foreign AND
   institutions both net-buying** — while the oil *narrative* thread is FADING and a "post-Iran oil market" is already
   being written [#thread 07-20]. Money accumulating into a fading story = either early or wrong;
   it is explicitly bracketed in M-02.

### Short interest (KRX actuals)
S-Oil **0.48% float, building (+0.05)** — the only name near the ≥0.5% 주목 threshold; a building
short into the board's best RS is squeeze fuel *or* a smart fade. 두산 0.26% flat, POSCO 0.15% flat,
삼바 0.39% flat, 삼전/하이닉스 ~0.0%.

### US COT cross-read [context, not trigger — Tue-close, +3–4d lag]
- **WTI 10%ile 🔴 crowded-SHORT** (was 13%ile on 07-16 — *more* crowded short) → feeds M-02's squeeze branch.
- **Nat Gas 6%ile 🔴 crowded-SHORT** — same asymmetry, second energy leg.
- **Nasdaq-100 4%ile 🔴 crowded-SHORT** → any US tech squeeze supports KR semi *sentiment*, not flow.
- **Copper 95%ile 🟢 crowded-LONG (overheated)** → caution on KR Materials / 이차전지 소재.

---

## §3 Narrative

### §3a Event axis — the day, all of it [`brief --body 2 --scope domestic`]
**Denominator: 788 articles → 360 clusters → 145 events (2src+) → 72 market / 73 nonmarket.
Tiers: head 0 · body 72 · tail 0. All 72 market events read** (text view truncates at 30 — the full
set was pulled from `out/news_brief/2026-07-20_domestic.json`).

⚠ **head = 0.** No event has been carried by ≥5 outlets today. That is a *collection-window* fact
(145 articles so far), **not** evidence of a quiet day.

Load-bearing events (with counts, so the claims carry their denominator):
- **[11a/4s] "칩플레이션에 우는 삼성전자, 더블 스토리지 혜택 올해가 막차?"** — the day's most-carried
  item. Memory **price inflation** = the pro-branch of M-04, and it is being framed as a *cost* to the
  set maker, not only a margin win for the memory maker.
- **[6a/2s] "[증시키워드] 반도체 급락에도 '펀더멘털 훼손 아니다'…SK하이닉스·삼성전자 반등 조건은"** —
  semis fell again; the narrative is defensive. Cross-read §2: the flow is 분산 on both.
- **[5a/3s] "이익증가율 둔화되면 코스피 피크아웃?"** + **[2a/2s] "버핏의 경고, 증시는 도박판"** —
  peak-out framing is now mainstream in the KR press.
- **[5a/2s] "환율 더 떨어지면… 韓 1인당 GDP 4만 달러 초읽기"** vs **[2a/2s] "원·달러 1487.28원"** —
  scenario vs print (§1).
- **[2a/2s] "한국, 반도체 의존하다 '네덜란드병' 걸릴 수도" — 한은의 경고** — the central bank itself
  flagging semiconductor concentration risk. 2 outlets = would have been **invisible without `--body 2`**.
- **[2a/2s] "발표만 남은 대미투자 1호… 이번주 막판 조율"** — 2 outlets, and it is **this week's dominant
  KR binary** (§0). The clearest single vindication of the `--body 2` rule this run.
- **[속보][2a/2s] "삼성바이오로직스, 2.7조원에 스위스 폴리펩타이드 그룹 인수"** — a ₩2.7tn cross-border
  acquisition at **2 outlets**. Also tail-tier, also structural.
- **[3a/3s] Oracle 52-week low + credit cut toward junk / "Has the AI-Capex Panic Overshot?"** ·
  **[2a/2s] IBM's 25% crash reveals AI's hidden corporate casualty** · **[3a/3s] A Hidden Threat for
  Micron? Apple Is Eyeing a Fix for AI Memory Demands** · **[2a/2s] 中 문샷 2조8000억 파라미터 '키미
  K3' 공개** · **[2a/2s] Alphabet's Gemini 3.5 Pro Is Late** — **five independent AI-capex-doubt prints
  in one day.** This is the M-03 kill-switch I named on 07-16 ("AI capex 회의") firing, loudly.
- **[5a/3s] 철강업계 "AI 데이터센터용 강재 잡아라"** + **[2a/2s] 中 과잉공급에 주저앉은 '산업의 쌀'…
  AI가 탈출구** — a steel/AI-DC narrative. §2 refutes it: POSCO 서지 **0.68x**, RS60 −29.2%.
- **[5a/3s] 이라크서 미군 1명 사망 (이란 드론 불발탄)** + nonmarket-bucket **[5s] "3 US troops killed
  in the Middle East amid Iranian attacks"** — ⚠ a 5-outlet **market-relevant** geopolitical event
  sitting in the *nonmarket* bucket. Concrete instance of the classifier's 10–14% LOSO error.
- **[6a/4s] 신축 매입임대 토지비 80% 선지원** · **[4a/3s] "대출도 고소득·고신용자만"… 대출절벽** ·
  **[2a/2s] 경기 3곳 부동산 추가 규제** — supply push + demand throttle, simultaneously.
- **[2a/2s] "새벽 2시부터 한국기업 분석한다"…달라진 韓증시에 월가 암살자 '군침'** — foreign short
  interest in KR names as a *theme*. Watch-flag only.
- **[3a/3s] 기술유출 피해 23조 · 국민 91% 경제안보 법체계** — regulatory tailwind for 보안/국가전략기술.

### §3b Trajectory axis — motion [`thread --days 7 --scope domestic`]
**Per-day denominator: 07-14 472 · 07-15 493 · 07-16 485 · 07-17 244 · 07-18 233 · 07-19 339 ·
07-20 145.** 2,411 daily events → 1,853 threads (341 multi-day, **69 alive**, 1,512 one-day incl. 74 new today).
⚠ **The window ends on a 145-article partial Monday after a 233-article weekend — every FADING tag
below is inflated by that. Read the curve, not the label.**

| Thread | Tag | Curve (outlets) | Read |
|---|---|---|---|
| **환율 1493→1484.7→1480s→1487.28** | REIGNITED | 6→6→5→2 | The FX print, alive all week (§1) |
| **미-이란 공습 / 중동전** | FADING | 4→5→4→3→2→**6**→3 | ⚠ **not fading** — it re-spiked to 6 on 07-19 (군인 2명 전사). The tag is a window artifact |
| **유가 / 호르무즈** | FADING | 6→5→4→3 | Genuinely decaying **narrative**, ending on "post-Iran oil market" — vs S-Oil accumulation (§2). **The divergence is M-02's core** |
| **가계대출 조이기 (코픽스 3%·주담대 8%)** | FADING | 5→7→6→4→5→3 | 6-day sustained. The **transmission channel** of M-01 |
| **반도체 (하이닉스 ADR·급등→급락)** | FADING | 4→7→3→2 | 07-15 삼전 +6%/하이닉스 +9% → 07-20 급락. Whipsaw, not trend |
| **최태원 "팔지 마라" + 성과급** | FADING | 7→3→4→2 | 4일째 damage control. §2 says the money left anyway |
| **코스피 급락·수급** | FADING | 6→6→3→4→4→3 | 7000 붕괴 → 6600 → 목표가 하향 역전 |
| **AI 일반** | FADING | 6→2→3→8→6→**12**→3 | Peaked at **12 outlets 07-19** (AI위클리·국산 NPU). Highest-outlet thread of the week |
| **정부 AI 메가프로젝트** | REIGNITED | 7→4→7→2 | Policy-side AI, still alive |
| **LH·주택공급 (보상 조기·매입임대)** | REIGNITED | 5→4→4 | **건설 수주 flow ≠ RE 자산** — separate these |
| **철강 AI-DC 강재** | REIGNITED | 2→3 | Narrative building from a 2-outlet base — but money absent (§2) |
| **기초연금 하후상박** | REIGNITED | 2→3→4→3 | Fiscal/welfare reform, steady climb |
| **법인 코인투자 지연** | BUILDING | 2→2 | Early, 2-outlet. Watch-flag |
| **금감원-자생한방병원 (손보)** | BUILDING | 2→2 | Early, 2-outlet. Insurance-sector micro |

**ENDED this window (attention-rotation ledger — 175 threads; peak-8 items):**
**한은 기준금리 2.75% 인상** (7→5→8→5) · **코스피 6600·매도 사이드카** (8→7→7→5→2) ·
**호르무즈 재봉쇄 → 유가 +10%** (8→3→4→3) · **원화 국제화** (2→2→**8**) · **레버리지 ETF 보완책**
(7→7→8) · **6월 고용 (고용률 3개월 연속 하락)** (4→8→5) · **대출총량제** (5→8→4) ·
**정부 성장률 3% 상향** (8→6) · 최태원 AI 발언 (5→8→5→6→2).

⚠ **Staleness flags raised by ENDED threads under still-open propositions:**
- **M-01's originating headline (BOK hike) has ENDED** → re-justified on §2 transmission evidence. Held.
- **M-02's originating headline (호르무즈 재봉쇄 → 유가 +10%) has ENDED**, and the successor thread is
  FADING toward "post-Iran oil market" → **the oil premium is losing its narrative engine.** M-02 is
  now carried *only* by flow (S-Oil accumulation) + COT positioning, not by news. Explicitly flagged.
- **원화 국제화 ENDED at its peak (2→2→8)** — but a fresh 07-20 print (해외 은행 원화 계좌, 4a/3s)
  restarts it. Treat as a live slow-burn, not a closed story.

**BUILDING threads with no matching bucket** (→ candidate new terms): 법인 코인투자/가상자산 제도,
손해보험-의료기관 분쟁.

### §3c Term axis — 7-bucket velocity [server /exec · domestic · 7d · OR+`--syn`+`--kr`, terms as separate argv]
| Rank | Bucket | 7d count | Note |
|---|---|---|---|
| 1 | 반도체 · 메모리 · 인공지능 · 데이터센터 · 파운드리 | **4,963** | Loudest by 3x. But flow 🔴 on both memory names (§2) |
| 2 | 부동산 · 가계대출 · 주택담보대출 · 총량규제 · 전세 | **1,596** | The live transmission channel of the hike |
| 3 | 코스피 · 외국인순매수 · 공매도 · 레버리지ETF · 신용융자 | **1,303** | De-rating + leverage-unwind chatter |
| 4 | 호르무즈 · 국제유가 · 이란 · 중동정세 · 원유 | **1,002** | Still large in *level* while the thread FADES in *shape* |
| 5 | 금융위원회 · 상법개정 · 세제개편 · 규제완화 · 대미투자 · 관세협상 · 공정거래 | **425** | ⚠ **corrected** — see trap below |
| 6 | 기준금리 · 통화정책 · 한국은행 · 코픽스 · 국고채 | **538** | Low count, **highest-conviction** (the realized regime, §1–§2) |
| 7 | 원달러 · 환율하락/상승 · 외환시장 · 원화가치 · 달러화 · 원화국제화 | **136** | ⚠ **corrected** — see trap below |

⚠ **The 2-char trigram trap fired again, and I caught it by testing terms individually (EXIT CHECK).**
My first bucket-2 pass returned **115** and bucket-6 **361**. Per-term probes on the KR trigram index:

| Term | Hits | Term | Hits |
|---|---|---|---|
| 환율 | **0** | 상법 | **0** |
| 외환 | **0** | 세제 | **0** |
| 원화 | **0** | 관세 | **0** |
| 달러 | **0** | 금융위원회 | 384 |
| 원달러 | 28 | 대미투자 | 139 |

**Every 2-char term returns 0 — absence of INDEX, not absence of news.** A "환율 is quiet" proposition
built on that 0 would have been fabricated, on the exact week the FX thread ran 136 articles across
6→6→5→2 outlets. Re-run with 3+ char forms only: bucket 2 → **136**, bucket 6 → **425**.
**No 0/near-0 count in this table is trusted; all seven were passed as separate argv.**

**Coverage check** [`coverage 기준금리 원달러 반도체 부동산 코스피 국제유가 인공지능 --days 7 --scope domestic`]:
pool **18,400건** (본문 보유 11,342 = 61.6%) · 현재 검색 2,053 · 본문 매칭 4,664 · **놓침 3,386** ·
**recall 37.7% → 🔴 심각, 본문 블라인드 62.3%.** Non-zero denominator, so the 🔴 is real (not the
0-denominator-prints-🟢 artifact). **My fixed term set sees ~38% of relevant news** — the blindspot
pass below is not optional garnish, it is covering a 62% hole.

### §3d Blind-spot pass [`blindspot --sample-pct 35 --days 7 --scope domestic`, 18,400 pool / 6,440 sample, read RAW]
Token-0 emergent terms are mostly ticker/acronym noise (AI 679, LG 105, KT 98). The **rank-jumps**
worth a body-read:
- **ADR (75)** — SK하이닉스's US ADR listing thread (세종 상장 자문 07-14 → 07-16 ADR −10.2% froth
  unwind → 07-19 "미국선 잘나가는데 국내선 답답"). A **structural KR-market change**: foreign capital
  can now express a hynix view *without* touching the KOSPI tape. Plausible partial explanation for
  the foreign −875만주 domestic exit in §2 (venue substitution, not thesis exit). **New term: `ADR/원주 괴리`.**
- **SMR (14)** — small modular reactor, persistent at low level while 두산 RS60 is −45.9%. Thesis alive,
  money gone. Reinforces the UTIL downgrade.
- **MBK (24)** — PE/거버넌스 activity. **New term: `사모펀드/행동주의`** (extends the 07-16 얼라인 leg).
- **AX (26)** — "AI Transformation" as a KR corporate-spend category, distinct from AI capex.
- **Vietnam (17)** — KR outbound manufacturing footprint. Watch-flag.
- Raw sample surfaced: **한화에어로스페이스 군 다목적 무인차량 사업 최종 선정** [yonhap 07-16] — a defense
  award that **no bucket queried** (방산 terms are 2-char-crippled). **New term: `무인차량/방산수주`.**
- Raw sample surfaced: **李대통령 "담합·체납 과감히 바로잡아야" 경제질서 정상화 드라이브** — a regulatory-
  enforcement axis. **New term: `경제질서/담합규제`.**

**Living term-table additions this run:** `ADR/원주 괴리` · `사모펀드/행동주의` · `AX(AI전환)` ·
`무인차량/방산수주` · `경제질서/담합규제` · `법인 코인투자` · `원화국제화` · `네덜란드병/반도체 쏠림` ·
`칩플레이션`. (Carried from 07-16: `비료/공급망`, `자체 AI칩/내재화`, `CXMT`, `AI capex 회의`.)

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Not equal-weight analysis. Δ = change vs 07-16.

| # | GICS Sector | Tilt | Δ vs 07-16 | Driving prop | One-line why (KR) |
|---|---|---|---|---|---|
| 1 | **Financials (FIN)** | **OW** (highest conviction) | = | M-01 | **BOK 2.75% + hiking bias → 코픽스 3%·주담대 8% repricing = NIM**; and the tape agrees — KB OBV **+35.8%**, 신한 **+31.8%**, **기관 실매수 both**, KB RS **+1.4% vs a falling index**. The one macro+flow double-confirmed leg |
| 2 | **Energy (ENRG)** | **tactical OW** | ↑ conviction, ↓ narrative | M-02 | **S-Oil = board-best RS20 +13.4%, OBV +62.6%, 외국인 AND 기관 동시 순매수**, WTI **10%ile crowded-short**. ⚠ Carried by **flow only** — the oil narrative thread is FADING into "post-Iran oil market" |
| 3 | **Health Care (HLTH)** | **modest OW** | ▲ **UP** from Neutral | M-07 | **삼바 2.7조 폴리펩타이드 인수 (today)** + RS20 **+22.4%** + 외국인·기관 동시 순매수. Rate-insensitive cash-flow ballast with a *fresh* catalyst — the correct shape for a tightening regime |
| 4 | **Industrials (INDU)** | **OW (split, downgraded)** | ▼ conviction | M-03, M-06 | 조선 leg has a **dated catalyst (러트닉 회담 07-22~24)**; 전력기기 leg is **directly hit by the AI-capex panic** (M-03 anti fired). Split the legs — do not carry them as one |
| 5 | **Information Tech (IT/반도체)** | **Neutral, flow-GATED** | ▼▼ **DOWN** from OW-gated | M-04 | Thesis intact (칩플레이션·기록적 경상흑자) but **the money is weak-hands**: 삼전 외국인 **−4,672만** vs 개인 **+4,259만**, 하이닉스 same, both **🔴분산**. Plus 5 AI-capex-doubt prints in one day + 한은's own 네덜란드병 warning. **Do not add on narrative** |
| 6 | **Consumer Disc (DISC)** | **Neutral** | ▼ from modest OW | — | The 07-16 K뷰티 순환매 leg has no fresh wind this run (외국인 관광객 소비 진화 = 2 outlets). Downgrade on absence of evidence, not on refutation |
| 7 | **Comm Services (COMM)** | Neutral | = | — | No distinct KR wind; 알파벳 07-22 spillover only |
| 8 | **Materials (MATR)** | **UW** | ▼ from Neutral→UW | M-05 | 철강 AI-DC narrative REIGNITED (2→3) but **money refutes it**: POSCO 서지 **0.68x**, RS60 **−29.2%**, 기관 순매도. Plus 中 과잉공급 + **Copper 95%ile crowded-long** |
| 9 | **Utilities (UTIL/원전)** | **UW** | ▼ **DOWN** from Neutral | M-03 | **두산에너빌리티 RS60 −45.9% (board-worst), 🔴분산.** Thesis fresh (SMR persistent in blindspot) but the AI-capex panic hits the AI-power leg at its source. Thesis-alive / money-gone = UW |
| 10 | **Consumer Staples (STPL)** | Neutral→UW | = | M-01 | No relief from a hiking central bank; no fresh KR catalyst |
| 11 | **Real Estate (RE)** | **UW** (most rate-negative) | = | M-01 | Hike + **대출절벽 (고소득·고신용자만)** + 경기 3곳 추가규제 + PF risk. ⚠ **Separate 건설 수주 from RE 자산** — LH 조기보상·매입임대 토지비 80% 선지원 is an **INDU/건설 order-flow** positive, not an RE-asset one |

### §4a Falsifiable propositions — both branches on every oscillating variable (M- = KR macro spine)

- **M-01 — Hike transmission → bank NIM (CARRIED, upgraded to flow-confirmed).**
  *BOK 2.75% + hiking bias → 코픽스 3% 돌파·주담대 8% 눈앞·가계 이자 +3.3조 → variable-rate repricing →
  bank NIM expansion → FIN OW; RE/STPL UW.*
  - **Evidence added this run:** KB/신한 both **OBV 매집** with **RS20 +35.8% / +31.8%** and **기관 실매수**,
    against a falling benchmark. Bought *into* the de-rating = defensive-into-tightening (the 07-16 §5a shape, +4d).
  - **DEEP-FIN refinement (post-stage):** the NIM leg compounds, but **the engine changed** — price moves
    faster than volume (코픽스 **+0.15%p in one month, 3 months running, >3%** vs a **+0.08%p** H2 corporate
    delinquency forecast [sedaily 07-19]), while volume is genuinely capped (5대은행 **₩3,500억 over** the
    1.5% target [donga 07-20]; **KB is waiving prepayment fees to shrink its own book**). Capped RWA ⇒ capital
    piles up ⇒ **buybacks** (KB 취득결과+소각결정 07-16, 하나 07-14). **The cap is fuel for the 밸류업 leg,
    not its enemy.** Thesis restated: growth → **margin × capital return**. The prior file's kill-switch
    #5 (shift to fixed-rate) is **REFUTED** — borrowers are choosing 변동형 [donga 07-15].
  - **Anti-signal / other branch:** **대출총량 1.5% 규제 caps the volume side** — NIM per won rises while
    won-lent is capped; and the **대출절벽 / 연체율** thread turns the hike into a **credit-cost** event.
    Also 증시활황發 핵심예금 이탈 (now weaker — the 증시 is *not* 활황).
  - **Track KPI:** bank 2Q NIM prints · 연체율 · 예금 mix · 가계대출 증가율 vs the 1.5% cap.
  - **Catalyst:** KR bank 2Q earnings (late July). **Thread status:** originating thread **ENDED** →
    re-justified on transmission, flagged.

- **M-02 — Oil / Hormuz (oscillating; both branches equal weight — narrative and flow DISAGREE).**
  *Blockade premium + **WTI 10%ile crowded-short** + **S-Oil 실매수 양방 (외국인 +12.6만, 기관 +158.5만),
  RS20 +13.4%, OBV +62.6%** → tactical ENRG OW.*
  - **Anti-branch (now the louder one in news):** the oil thread is **FADING 6→5→4→3 into "The world is
    looking ahead toward a post-Iran oil market"**; the **TACO trigger stays an undated live binary**
    (Iran declares strait open → Brent gaps down, crowded shorts cover, premium gone in a day).
  - ⚠ **Named divergence:** money is accumulating S-Oil while the story decays. One of the two is wrong.
    A one-way tilt here is a protocol violation — **size this as tactical, stop-defined, both-sided.**
  - **Track KPI:** Hormuz transit count · Brent spot · whether S-Oil's 0.48% **building** short is squeeze
    fuel or the smart side · WTI COT %ile direction.

- **M-03 — AI-power / DC capex (★ THE ANTI-BRANCH I NAMED ON 07-16 HAS FIRED).**
  *07-16 thesis: AI-DC 전력 병목 → INDU 전력기기 · UTIL 원전. Named kill-switch: "AI capex 회의" spreading.*
  - **★ The kill-switch fired, in five independent prints in one day:** Oracle **52-week low + credit cut
    toward junk** ["Has the AI-Capex Panic Overshot?"] · **IBM −25%** ["AI's hidden corporate casualty"] ·
    **Apple eyeing a memory fix = hidden threat to Micron** · **中 문샷 '키미 K3' 2.8조 파라미터** (cheap
    frontier compute undercuts the capex premise) · **Alphabet Gemini 3.5 Pro late**.
  - **Confirmed in KR money:** 두산에너빌리티 **RS60 −45.9%, 🔴분산.** Thesis-alive/money-gone.
  - **Surviving pro-branch:** 정부 AI 메가프로젝트 REIGNITED (7→4→7→2), 국산 NPU (AI thread peaked at
    **12 outlets** 07-19), 기술유출 규제 tailwind. **The domestic-policy AI leg is intact; the
    global-hyperscaler-capex leg is the one breaking.** Separate them.
  - **Track KPI:** **알파벳 실적 07-22 (D-2, binary)** · DART 단일공급계약 전환 · 두산 RS60 stabilization.

- **M-04 — Memory supercycle (thesis OW / flow-gated → gate now CLOSED).**
  *Pro: **칩플레이션** (memory price inflation, the day's #1 event 11a/4s) · 반도체가 이끈 기록적 경상흑자 ·
  하이닉스 RS60 **+53.1%** (the 6-month trend is still intact).*
  - **Anti (dominant, and now measured):** **외국인 −4,672만주 (삼전) / −875만주 (하이닉스) with 개인
    absorbing +4,259만 / +960만** — the module's own weak-hands disqualifier. Both **🔴분산**, RS20
    −4.9% / −6.6%. Plus **한은's own "네덜란드병" concentration warning**, Apple's memory-demand fix,
    CXMT oversupply (carried), 자체 AI칩 내재화 (carried).
  - ⚠ **Narrative and flow are on opposite sides.** Today's press is defensive-bullish ("펀더멘털 훼손
    아니다", 최태원 "갖고 있어라" — 4 days of damage control). **The tape disagrees.** Per P4, the
    measured flow outranks the quoted reassurance.
  - **Partial alternative explanation (blindspot):** the **ADR** venue — foreign hynix exposure may be
    *migrating* to the US listing rather than being sold outright. This would soften the "foreign exit"
    read. **Unresolved — SWEEP must test it** (ADR 원주 괴리 + ADR volume vs domestic foreign net).
  - **Track KPI:** foreign net-buy sign flip on 삼전/하이닉스 · breadth 확산 · ADR-원주 괴리 · 알파벳 07-22.

- **M-05 — Materials / 철강 AI-DC (narrative-only, refuted by flow → UW).**
  *Narrative: 철강업계 "AI 데이터센터용 강재 잡아라" REIGNITED 2→3, 中 과잉공급 탈출구로 AI.*
  - **Anti (dominant):** **POSCO 서지 0.68x (money leaving), RS60 −29.2%, 기관 −33.1만.** A REIGNITED
    narrative with no money behind it. Plus **Copper 95%ile crowded-long** = the metals complex is the
    overheated side of COT.
  - **Track KPI:** POSCO 서지 >1.3x + 기관 순매수 flip would upgrade; until then this is a story.

- **M-06 — 대미투자 / 관세 (★ DATED BINARY THIS WEEK, both branches).**
  *김정관 산업장관 **07-22 출국 → 07-24 귀국**, 러트닉 회담. Agenda: **대미투자 1호 (에너지 프로젝트,
  "발표만 남음, 이번주 막판 조율")** + **조선** + **쿠팡 변수**. Backdrop: "8월 트럼프 청구서",
  주미대사 긴급호출, 靑 경제안보비서관 신설 (김성열).*
  - **Up-branch:** 1호 프로젝트 서명 → 수출주(조선·에너지·기자재) relief rally, tariff overhang lifts.
  - **Down-branch:** **쿠팡 사태가 협상을 오염** → 발표 연기, "청구서" 압박 재점화 → exporter overhang
    re-prices wider. ⚠ The catalyst module **did not carry this** — injected manually (§0).
  - **Track KPI:** 07-22~24 headlines · 1호 프로젝트 서명 여부 · 쿠팡 의제 분리 여부.

- **M-07 — Defensive cash-flow bid (NEW this run).**
  *In a cost-of-capital regime, the bid rotates to rate-insensitive cash flow with fresh catalysts:
  **삼바 2.7조 폴리펩타이드 인수 + RS20 +22.4% + 외국인·기관 동시 순매수**; banks accumulated into the
  selloff (M-01); 기초연금/복지 fiscal thread REIGNITED.*
  - **Anti-branch:** if the 알파벳 07-22 print re-ignites AI risk-on, this defensive bid unwinds fast and
    the rotation snaps back to IT/UTIL — the exact whipsaw that burned M-05 (밸류업) on 07-15→16.
  - **Track KPI:** 삼바 RS60 (−23.0% → does it cross 0?) · bank OBV persistence · 알파벳 07-22.

---

## §5 Self-backtest — prior propositions scored at +4d (07-16 → 07-20)

| # | Prior proposition (MACRO_REPORT 07-16 §4a) | Δ to 07-20 (measured) | Score |
|---|---|---|---|
| M-01 | BOK hike → NIM → FIN OW | 코픽스 3%↑·주담대 8% 눈앞 transmission visible; **KB/신한 OBV +35.8/+31.8%, 기관 실매수, KB RS positive vs falling index** | **HIT** — and upgraded from narrative to flow-confirmed |
| M-02 | Hormuz premium × WTI crowded-short → tactical ENRG | **S-Oil RS20 +13.4% board-best, OBV +62.6%, 외국인·기관 동시 매수**; WTI 13%ile → **10%ile** (more crowded short) | **HIT on flow / MISS on narrative** — thread FADING into "post-Iran". Both branches were carried, so no one-way loss |
| M-03 | AI-DC 전력 → INDU 전력기기·UTIL 원전. **Anti named: "AI capex 회의"** | **ANTI-BRANCH FIRED HARD** — Oracle junk-ward + 52wk low, IBM −25%, Apple memory fix, 키미 K3, Gemini 지연; 두산 **RS60 −45.9%** | **ANTI-HIT** — ✅ the bracket saved the call. A one-way UTIL OW would have been a −45.9% RS60 loss |
| M-04 | Memory OW-but-flow-gated (gate = breadth + OBV 매집 확산) | **Gate never opened, then closed**: 삼전/하이닉스 both 🔴분산, **외국인 대량 이탈 + 개인 흡수**; 07-15 +6/+9% 급등은 whipsaw | **HALF → gate correctly held** — the *gate discipline* is the win; the OW thesis is unproven |
| M-05 | 밸류업 / 외국인 복귀 rotation (07-15 3조 매수) | **Anti-branch fully realized** — KOSPI 7000 붕괴 → **6600 + 매도 사이드카**, 목표가 하향 역전, 증시서 자금 이탈; foreign still net-sellers in §2 | **ANTI-HIT (call correctly killed on 07-16 §5a/§5b)** — the same-day correction prevented carrying it |
| M-06 | 관세/무역 overhang (KR deal 미확정) | Overhang persists and now has a **date**: 방미 07-22~24, 1호 "발표만 남음", 쿠팡 변수 | **CARRIED → upgraded to dated binary** |

**Running hit-rate: 6 propositions scored → 2 HIT · 2 ANTI-HIT (bracket paid) · 1 HALF (gate held) ·
1 CARRIED.** No proposition failed one-way.

**Recurring failure class — status:** the class under watch is *banking a one-sided read of an
oscillating regime variable*. This run it was tested twice and the bracket paid twice: **M-03's named
kill-switch fired** (AI-capex panic) and **M-02's narrative branch decayed while its flow branch
strengthened**. Both were carried two-sided, so neither produced a one-way loss. **Continue mandatory
two-sided treatment of M-02 (oil), M-06 (trade binary), and M-07 (defensive bid vs 07-22 알파벳).**

**New failure class observed this run (fold into the standing watch): *narrative–flow inversion*.**
On IT and MATR, the press and the tape point in **opposite** directions (defensive-bullish semis
coverage vs foreign 4,672만주 exit; REIGNITED 철강 story vs 0.68x volume). The 07-16 report weighted
narrative more heavily and had IT at OW-gated. **Rule going forward: when narrative and measured flow
invert, the flow sets the tilt and the narrative becomes the anti-signal to track** — which is what
§4 does this run (IT ▼ Neutral, MATR ▼ UW).

---

## ✅ EXIT CHECK
- [x] **Catalysts injected** — `catalyst_calendar --days 5` → `CATALYST_WATCH.json`; ⚠ the module missed
      the week's dominant KR binary (방미/대미투자 07-22~24) → **manually injected** in §0. 6+1 binaries, all bracketed.
- [x] **Events read via `--body 2`** — 788 → 360 → 145 → **72 market, tail count = 0, all 72 read**
      (full set pulled from JSON; the text view truncated at 30). Head = 0 → flagged as a partial-day
      collection artifact, not a quiet day.
- [x] **Trajectories read** (`thread --days 7`) — every §4a proposition carries its thread tag + curve.
      **ENDED-under-open-proposition staleness flags raised for M-01 (BOK), M-02 (호르무즈), 원화국제화.**
      Window-end thinning (145 vs 472–493) flagged as a FADING inflator; 미-이란 thread's "FADING" tag
      explicitly overridden by its own 6-outlet re-spike on 07-19.
- [x] **Every "quiet" claim carries its denominator** — DISC downgraded on *stated absence of evidence*
      (2-outlet count cited), not on an unbacked "nothing happened."
- [x] **No 0/near-0 bucket trusted.** All 7 buckets passed as **separate argv**. The 2-char trigram trap
      fired (환율·외환·원화·달러·상법·세제·관세 = **0 each**) and was caught by per-term probes;
      buckets 2 and 6 re-run with 3+ char forms (115→**136**, 361→**425**). Coverage checked with a
      **non-zero denominator** (18,400) → 🔴 심각 / recall 37.7% — the 🔴 is real, not the 0-denominator artifact.
- [x] **Transmission matrix produced** — all 11 GICS sectors, one line each, with Δ vs 07-16 and driving prop.
- [x] **MACRO_REPORT.md written** with primary numbers explicit (FRED asof dates + staleness flags on
      DXY/VIX/CPI/M2), self-backtest hit-rate appended (6 scored), and 9 new blind-spot terms folded
      into the living term table.

**News source = server DB via NEWS API `127.0.0.1:8787` (routed /exec, not local fallback).**
**Flow source = `module_flow` — KIS per-investor actuals + KRX short interest (the KR edge axis).**

**→ proceed to SWEEP.**
