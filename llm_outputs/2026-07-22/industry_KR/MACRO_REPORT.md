# MACRO_REPORT — industry_KR · 2026-07-22 (Wed)

> Stage 1 / 7 · L1·MACRO. Runtime `--market kr`, English instructions / KR-market output.
> Primary data: **no same-day US MACRO_REPORT exists** (last US desk run = 07-21) → §1 pulls FRED
> directly via `module_macro_us --json`, cited `[FRED]` with asof dates. This is **fresher** than what
> the 07-21 KR desk cross-read (07-20 prints vs 07-17).
> News = `module_news_data` via NEWS API (`/exec`, ngrok) — event axis (`brief --body 2 --scope domestic`)
> + trajectory (`thread --days 7`) + 7-bucket + coverage + blindspot.
> KR edge axis = `module_flow` KIS per-investor actuals + KRX short interest — **re-derived by hand
> today; see the §2 trap.**
> Continuity anchor: `llm_outputs/2026-07-21/industry_KR/MACRO_REPORT.md` (incl. its post-DEEP CORRECTION).
> Handoff ledger: 252 reports / 350 tickers / 15 sectors, updated 2026-07-21T18:58.
> Deliverable = the **§4 transmission matrix** (ROTATION's input). Zero buy/sell calls.

---

## ⚠⚠ TWO CAVEATS, BOTH STATED BEFORE ANY PROPOSITION

### (1) This is an **early-session** run, not a completed day
Embedding cursor **08:58 KST**; flow pulled **09:32 KST — 32 minutes into the session.**

| | 07-21 (prior run) | **07-22 (this run)** |
|---|---|---|
| Articles → clusters → events | 3,770 → 1,113 → 612 | **710 → 347 → 102** |
| Market / nonmarket | 369 / 243 | **72 / 30** |
| Tiers (head ≥5s / body 2–4s / tail) | 42 / 327 / 0 | **5 / 67 / 0** |
| 7d pool | 20,578 | **18,731 (−9.0%)** |

**Consequences, binding on the whole report:** (a) every raw count fell because the pool fell — **−9.0% is
the normalizer, not zero**; (b) **every 거래량 서지 in §2 is 0.50–0.95× because the session is 32 minutes
old — the surge column is uninterpretable today and is not used anywhere below**; (c) the trajectory window
ends on a **102-event partial day after a 517-event day**, which **mechanically inflates FADING** — the
inverse of 07-21's caveat, and every FADING tag below is read against it.

### (2) ★★ A NEW TOOLING TRAP — and unlike yesterday's, it does not print empty. It prints *plausible*.

**`^KS11`'s yfinance history is MISSING the 2026-07-21 bar. Every constituent name has it.**

```
^KS11 bars:  … 07-15 7284.41 · 07-16 6820.60 · 07-20 6516.27 · [07-21 ABSENT] · 07-22 7153.11
names  bars: … 07-15 · 07-16 · 07-20 · 07-21 ✓ · 07-22
```

`module_flow` computes RS by **bar count**, so the benchmark's 21-bar lookback reaches **one extra trading
day back** — on a −26%/1m tape that means a higher start, a more negative measured benchmark return, and
therefore **every RS20 on the board inflated by 5–11pp.**

| Name | `module_flow` RS20 | **date-aligned RS20** | error |
|---|---|---|---|
| **삼성전자** | **+9.9%** | **−0.9%** | **+10.8pp** |
| **SK하이닉스** | **−0.3%** | **−9.8%** | **+9.5pp** |
| **현대차** | **+5.8%** | **−4.2%** | **+10.0pp** |
| 한화오션 | +2.5% | **−6.5%** | +9.0pp |
| 두산에너빌리티 | +0.8% | **−3.7%** | +4.5pp |
| LG화학 | +12.3% | +2.9% | +9.4pp |
| S-Oil | +61.5% | **+53.2%** | +8.3pp |
| KB금융 | +37.1% | **+34.3%** | +2.8pp |

**Read raw, this board says "RS20 improved for 16 of 16 names" — and this desk would have upgraded IT,
DISC, 조선 and UTIL simultaneously on a benchmark data hole.** RS60 is far less affected (1 missing bar of
61) and its aligned values are within ~1pp of the module's. **§2 and §4 below use the date-aligned column
throughout.** Filed as the second `module_flow` trap in two runs (07-21: bare 6-digit tickers → silent
empty rows). **A fix belongs in `module_flow` — reindex name and benchmark on their date intersection
before differencing.** Recorded, not fixed here (this is a research stage).

---

## §0 Catalyst injection (`catalyst_calendar --days 5` → `llm_outputs/2026-07-22/CATALYST_WATCH.json`)

**5 binaries in the module's window. The KR-native ones are missing for a THIRD consecutive run and are
injected manually.**

| When | Event | Axis | Note |
|---|---|---|---|
| **D-0 · TODAY** | ★★ **김정관 산업장관 방미 — 러트닉 회담, 대미투자 1호 + 조선 + 쿠팡** | trade/policy | 🔀 **binary, D-0.** Still absent from the calendar module. Body-read: *"김정관 22일 방미"* [mt 07-20], *"발표만 남은 대미투자 1호…이번주 막판 조율"* [mt], *"76일 만에 만나는 김정관·러트닉"* [sedaily]. **Zero 07-22 articles yet — it has not printed** |
| **D-0 · tonight** | **알파벳(구글) 실적** | AI-capex | 🔀 The KR feed itself frames it: **[4a/3s] "구글 실적 발표 D-1, 반도체주 반등 분수령 될까…관건은 '돈 버는 AI'"** → M-03/M-04 both-sides |
| **Undated / LIVE** | **홍해 봉쇄 — 트럼프 "美가 처리…이란 곡괭이산 곧 타격"** | oil | 🔀 binary. **Escalated from the 07-21 "Strait of Hormuz open" TACO framing into an explicit US strike threat.** [6a/5s, head] |
| **Undated, LIVE** | **'글로벌 관세 10%' 만료 → 301조 관세 / 캐나다 50%** | trade | 🔀 binary. **196-article thread, the week's largest.** 301조 = 97 hits/7d |
| D-0 · 07-22 | **TSLA · KMI** earnings | earnings | 🔀 |
| D-1 · 07-23 | **RTX · LMT** earnings (KR 방산 read-through) | earnings | 🔀 |

★ **Third consecutive run in which `catalyst_calendar` missed the week's dominant KR binary — and this run
it missed it on the day it fires.** Filed as a standing module gap, not a one-off.

---

## §1 Regime read — primary numbers explicit

### ★ The tape, and it is violent — but the desk must not read a melt-up as a regime change

⚠ **The `^KS11` 07-21 bar is absent from yfinance (see the trap above), so 1d% from any tool is computed
against 07-20.** The 07-21 close is taken from the prior run's news-sourced print (**6,747.95**).

| | Level | 1d (vs true prior close) | 5d | 1m |
|---|---|---|---|---|
| **^KS11** | **7,148.02** (09:32, live) | **+5.93%** vs 6,747.95 | — | **−21.58%** |
| ^KQ11 | 787.37 | **+4.52%** vs 753.34 | −1.51% | −18.71% |
| **KRW=X** | **1,478.58** | **+0.24% (won WEAKER, +3.6원)** | −0.61% | −3.43% |
| CL=F | 84.72 | **+1.79%** | +6.78% | +13.23% |
| **BZ=F** | **91.54** | **+2.60%** | **+8.04%** | **+17.51%** |
| ^VIX | 17.05 | −8.58% | +3.33% | −1.33% |
| JPY=X | **163.06** | +0.35% | +0.54% | +1.01% |

**Two-day KOSPI: +3.56% then +5.93% = +9.7%.** Against **−21.58%/1m**. **This is a violent bounce inside a
de-rating, not the end of one** — and the desk's own 07-21 lesson (*"an anti-branch is only tested when it is
tested with a measurement, not with a day"*) applies with the sign reversed: **two days is not a regime.**

Name-level moves today (09:32): **삼성전기 +12.37%** · **SK하이닉스 +8.93%** · **현대차 +8.27%** ·
삼성전자 +5.79% · 두산에너빌리티 +5.69% · LG화학 +5.19% · HD한국조선 +5.03% · POSCO +3.30% ·
한화오션 +2.81% · 셀트리온 +2.51% · 삼바 +2.22% · **KB금융 +2.07% · 하나 +1.28% · 신한 +1.05%** ·
**S-Oil −0.07%**.
★ **The leadership inverted from the last three runs: the weak-hands names led and the flow-confirmed names
lagged.** That is what a beta-squeeze looks like, and it is the single most important thing to *not*
over-read. ⚠ **삼성전기 +12.37% has no catalyst in the feed** — 2-day FTS returns 77 hits, all of them
brokerage-target/[시선강탈] retail-pick columns and one bare *"삼성전기(009150)"* title. **Named as
unexplained, not invented.**

### Cross-read of US primaries [**FRED**, pulled directly — fresher than the 07-21 KR desk's]
| Series | Latest | asof | Δ vs what the 07-21 KR desk had | Read-through to KR |
|---|---|---|---|---|
| Fed funds | **3.63%** | 07-20 | = | US on hold vs **BOK 2.75% hiking** |
| US 10Y | **4.60%** | 07-20 | **+5bp** (4.55 @07-17) | Long end backed up |
| US 2Y | **4.21%** | 07-20 | **+3bp** (4.18) | Front end still rising |
| **2s10s** | **+39bp** | 07-20 | ★ **+2bp — the bear-flattening PAUSED** (42→41→37→**39**) | The US desk's FIN-thesis pressure eased marginally |
| **Real 10Y** | **2.35%** | 07-20 | **+4bp — highest of the sequence** | ★ **The KR long-duration / RE discount rate got WORSE, not better** |
| Core CPI / CPI | 336.065 / 332.568 | **Jun** | = | ⚠ ~1-month lag, not a live read |
| Unemployment | 4.2% | **Jun** | = | ⚠ 1-month lag |
| DXY | 120.53 | **07-17** | = | ⚠ **3 sessions stale.** Cannot speak to 원달러 1,478.6 or **엔 163** |
| VIX | 18.65 | 07-20 | −0.12 | live **^VIX 17.05 (−8.58%)** — risk-off came off further |
| M2 | $23,052B | **May** | = | Expanding, lagging |

⚠ **US rates are 2 sessions behind the KR tape and DXY is 3.** A KOSPI +5.9% morning is in none of them.

### ★ The KR-native prints of the day — and the loudest one is an anti-print for our top sector
- **[5a/4s] 은행 연체율 2016년 10월 이후 최고…중소기업 대출도 '빨간불'** + **[3a/3s] 5월 국내은행 대출
  연체율 0.67% — 9년 7개월 만에 최고** + [단독, 07-21] **카드론 금리 15% 돌파**.
  ★ **This is new, hard, and it is the FIRST measured credit-cost print of the hiking cycle.** M-01 has run
  for six sessions on *margin* evidence; **the cost side has now printed a number**, not a mechanism.
- **[6a/5s, head] 오락가락 '롤러코스피'에 질린 개미들…은행 예금에 '16조' 뭉칫돈** — the deposit war carried
  from 07-21, now framed as *retail capitulation out of equities*, and it is the head tier.
- **[5a/5s, head] 국제유가 꺾이자…생산자물가 상승세 10개월 만에 멈췄다** — ⚠ **this print is already stale
  against its own driver: Brent is +2.60% today and +8.04% on 5d.** A PPI relief headline printed into a
  re-accelerating oil tape. Both branches carried in M-02.
- **[3a/3s] 코스피 흔들리자 다시 美로…서학개미 순매수 5개월 최대** (49 hits/7d) — ★ **domestic capital
  flight measured on the retail side**, sitting alongside the 20-day foreign exit in §2. Two different
  cohorts leaving the same market.
- **[11a/2s] [뉴욕환시] 달러 이틀째↑…달러-엔 40년 만에 163엔 돌파** — the won firmed on 07-21 into a
  strengthening dollar; **today it gave back +3.6원 while the dollar rose a third day.** The 07-21 read
  ("export-driven, not dollar-driven, and therefore hostage") is holding.

---

## §2 Positioning — ★ the KR edge axis (`module_flow`, KIS actuals + KRX short, asof 09:32 intraday)

⚠ **RS20 is the DATE-ALIGNED figure (hand-derived). RS60 is the module's (error <1pp).
서지 column omitted — 32 minutes of session makes it meaningless.** 수급/공매도 are KIS/KRX actuals and
are **not** affected by the benchmark hole.

| Ticker | Name | 흐름 | OBV | **RS20 aligned** | RS60 | 외/기/개 (만주, 20d) | Verdict |
|---|---|---|---|---|---|---|---|
| 105560.KS | **KB금융** | 🟢가속 | **매집** | **+34.3%** | −0.8% | −274.8 / **+375.5** / −96.3 | ✅ **real-hands · 외국인5일 매수전환↑ NEW** |
| 086790.KS | **하나금융** | 🟢가속 | **매집** | **+33.6%** | −1.9% | −71.1 / **+155.4** / −78.3 | ✅ real-hands · 외5일전환↑ · short **building(+0.09)** |
| 055550.KS | **신한지주** | 🟢가속 | **매집** | **+29.6%** | −5.6% | −180.5 / **+293.7** / −64.2 | ✅ **real-hands · 외국인5일 매수전환↑ NEW** |
| 010950.KS | **S-Oil** | 🟢가속 | **매집** | **+53.2%** ★top | **+11.3%** | −14.9 / **+191.1** / −183.4 | ✅ real-hands · short 0.49% building |
| 207940.KS | **삼성바이오** | 🟢가속 | **매집** | **+31.4%** | −22.4% ▼ | **+7.7 / +5.2** / −12.7 | ✅ both sides buying |
| **068270.KS** | **셀트리온** | **🟢가속 ▲** | **매집 ▲** | **+25.7%** | −21.1% ▼ | **+17.1 / +126.8** / **−195.5** | ✅ ★ **UPGRADED 🟡→🟢, OBV 중립→매집** |
| 015760.KS | 한국전력 | 🟡중립 | 중립 | +11.5% | −37.6% ▼ | −49.9 / **+204.4** / −159.4 | ✅ 기관 실매수 · 외5일전환↑ |
| 005490.KS | POSCO홀딩스 | 🟡중립 | **분산** | +11.7% | −37.5% ▼ | **+28.8** / −27.0 / −1.3 | ⚠ **4th run: OBV 분산, 기관 매도.** 외국인만 순매수 |
| **005930.KS** | **삼성전자** | 🟡중립 | 중립 | **−0.9%** (= −0.8%) | **+13.3%** | **−4,013.4** / **+832.1** ▲▲ / +3,116.1 | ⚠ **RS20 UNCHANGED. But 기관 순매수 2배(+397→+832만)** |
| **000660.KS** | **SK하이닉스** | 🔴분산 | 분산 | **−9.8%** (▲ from −11.1) | **+51.8%** ▲ | **−721.9** ▲ / **−79.8** ▲ / +773.8 | ❌ weak-hands, **but all three legs improved** · short covering |
| 034020.KS | **두산에너빌리티** | 🟡중립 ▲ | **분산** | −3.7% ▼ | **−51.1%** ★worst ▼ | **+2.6** ▼▼ / +49.8 / −42.3 | ⚠ ★ **the 07-21 inversion WEAKENED — 외국인 +52.3 → +2.6만** |
| **042660.KS** | **한화오션** | **🔴분산** | 분산 | **−6.5%** ▼ | **−48.1%** ▼ | **−421.4** / −41.6 / **+457.4** | ❌ **weak-hands + 공매도 1.44% building(+0.17) ⚠주목 — unchanged INTO D-0** |
| 012450.KS | 한화에어로 | 🟡중립 | 중립 ▲ | +1.4% ▼ | **−47.3%** ▼ | −4.8 / +14.9 / −10.0 | ⚠ thesis-alive / RS gone (worse) |
| 009540.KS | HD한국조선해양 | 🟡중립 | 분산 | +10.5% | −29.3% ▼ | −10.6 / +14.7 / −4.5 | ⚠ short **building(+0.09)** |
| **005380.KS** | **현대차** | 🟡중립 ▲ | 분산 | **−4.2%** (▲ from −5.4) | −32.6% | −2.8 / **+36.2** / −30.6 | ⚠ **외국인5일 매수전환↑ NEW** · short **1.99% covering(−0.51) ⚠주목** |
| 051910.KS | LG화학 | 🟡중립 | 분산 | +2.9% | −44.4% ▼ | +25.5 / −36.7 / +10.8 | ⚠ 혼조, no money |

### ★ What this table decides, ranked by how much it changes the prior run

1. **THE FIN TRIPLE IS INTACT AND ITS FOREIGN LEG COMPLETED — but the sector got its first hard cost print.**
   All three banks now carry **외국인5일 매수전환↑** (KB and 신한 are new today; 하나 held it), all three
   **OBV 매집**, all three **기관 실매수**, aligned RS20 **+34.3 / +33.6 / +29.6** against a benchmark
   **−21.58%/1m**. **Fourth consecutive run confirmed on flow.** ⚠ **And they were the day's worst
   performers (+1.0~+2.1% on a +5.9% index) — which is exactly what a defensive-carry basket does in a
   beta-squeeze, and is NOT evidence against them.** The evidence against them is in §1: **연체율 9년 7개월
   최고.**

2. **THE MEMORY GATE DID NOT OPEN — the number that said it did was the artifact.** Raw output said
   삼전 RS20 −0.8% → **+9.9%**; date-aligned it is **−0.9%, i.e. unchanged.** 하이닉스 −11.1% → aligned
   **−9.8%**, still deeply negative. ⚠ **But one leg improved for real, and it is not benchmark-relative:
   기관 net-buy on 삼전 DOUBLED (+397 → +832만주)** and 하이닉스's 기관 selling shrank (−171.6 → −79.8만)
   while its foreign exit shrank (−815.7 → −721.9만). **Institutions are the leg that moved. Foreigners are
   not (−4,013만 on 삼전, 20d).** → **half-step, on the institutional leg only.** M-04's gate is re-specified.

3. **THE 조선 SHORT DID NOT BLINK AT ITS OWN D-0.** 한화오션 공매도 **1.44% of float, still building
   (+0.17), ⚠주목**, 외국인 −421만 / 개인 +457만, aligned RS60 **−48.1% (worse than −43.2%)**; HD한국조선
   short also **building (+0.09)**. **The 방미/조선 catalyst fires today and the measured money spent the
   whole run positioned against it.** ★ **And a hard fact arrived to back the shorts:** [chosun 07-21]
   **"LNG선도 거세지는 中 추격… 김정관·김동관 만나고도 中에 1.3조 주문한 UAE '큰손'"** — a customer met the
   Korean minister and the Hanwha chairman **and ordered ₩1.3tn from China anyway.**

4. **두산에너빌리티: the 07-21 "institutional inversion" WEAKENED — resolve it toward the price, not the flow.**
   Foreign net-buy collapsed **+52.3 → +2.6만주**; 기관 +60.7 → +49.8만; OBV still **분산**; aligned RS60
   deteriorated further to **−51.1%, board-worst.** 07-21 named this "early positioning or dead-cat, not
   resolved." **One session of decay is not proof, but the burden of proof moved.** Corroborating print
   today: **[2a/2s] KB증권 "현대건설, 원전 모멘텀 하반기에 재점화…목표가 28% 하향"** — the 원전 catalyst
   is being **pushed out**, in writing, with a target cut attached.

5. **셀트리온 is the run's cleanest upgrade, and it is a shelter name behaving like a shelter.**
   🟡→🟢가속, OBV 중립→**매집**, 기관 **+126.8만**, 개인 **−195.5만** (retail distributing into
   institutions), catalyst = **트룩시마 북미 점유율 38.6%, 4개월 연속 1위** [3 outlets 07-21].

### Short interest (KRX actuals)
| Name | %float | Direction | Read |
|---|---|---|---|
| **현대차** | **1.99%** ⚠주목 | **covering (−0.51)** | Most crowded short, actively covering — **and the stock is +8.27% today.** Mechanical, not fundamental |
| **한화오션** | **1.44%** ⚠주목 | **building (+0.17)** | ★ Pressing **into** the D-0 binary. Unchanged conviction |
| S-Oil | 0.49% | building (+0.04) | At threshold, building into the board's best RS |
| 삼바 / 한전 | 0.40% / 0.23% | flat | — |
| 두산에너빌리티 / HD한국조선 | 0.27% / 0.27% | **building** (+0.03 / +0.09) | Consistent with 분산 |
| 하나금융 | 0.18% | building (+0.09) | Only FIN name with a building short |
| 셀트리온 / POSCO / 신한 | 0.14 / 0.09 / 0.09% | flat | — |
| **삼전 / 하이닉스** | **0.01% / 0.01%** | flat / **covering(−0.06)** | ⚠ **Still effectively unshorted. 하이닉스 +8.93% today had NO squeeze fuel — that was cash buying** |

### US COT cross-read
⚠ **Not re-pulled this run and the 07-21 desk already reported it byte-identical to 07-19 (no new CFTC
release). It carries zero new information and is not permitted to move anything.** Carried for context only:
WTI **10%ile** 🔴crowded-short · Nat Gas 6%ile 🔴 · Nasdaq-100 4%ile 🔴 · Copper 95%ile 🟢overheated.

---

## §3 Narrative

### §3a Event axis [`brief --body 2 --scope domestic`]
**Denominator: 710 articles → 347 clusters → 102 events (2src+) → 72 market / 30 nonmarket.
Tiers: head 5 · body 67 · tail 0. All 72 market events read** (stdout truncates the body at ~30 with
`… 외 37개`; the remainder read from `out/news_brief/2026-07-22_domestic.json`).
⚠ **The nonmarket bucket was checked** — its 5-row sample is genuinely non-market (연예·날씨·법조).
**Unlike 07-20 and 07-21, no 9-outlet market item was found misfiled today.** Sample only (5 of 30) — the
classifier is not exonerated, but this run has no evidence against it.

**★ Oil / Red Sea — the head-tier escalation, and it is now a US military threat:**
- **[6a/5s, HEAD] 트럼프 "후티 홍해 봉쇄시 美가 처리…이란 곡괭이산 곧 타격"(종합)** — thread
  **BUILDING 2→5→4→5** (07-16 예멘 반군·소말리아 홍해입구 봉쇄 준비 → 07-20 후티 사우디 해상봉쇄 선언 →
  07-21 사우디 항구 이용 선박도 표적 → 07-22 US strike threat).
- **[4a/3s] 유가 또 90달러 위협…다시 고개 든 '3고', 한국 경제 압박** · **BZ=F 91.54 (+2.60%)**
- **↔ anti: [5a/5s, HEAD] 국제유가 꺾이자…생산자물가 상승세 10개월 만에 멈췄다** ← the relief print,
  **already contradicted by its own driver today**
- **↔ anti, and it is name-specific: [2a/2s] 설비는 '중동산 맞춤형'인데… 정유사 '수입선 다변화' 진땀**
  ← ★ **the first print that makes a Hormuz/Red Sea disruption a COST to the KR refiner, not only a margin.**
  S-Oil's configuration is built for Middle East crude. Folded into M-02's anti-branch.

**★ Trade — the week's largest thread by article count, and the KR binary fires TODAY:**
- **[33a/4s] 트럼프 행정부, 캐나다에 50% 관세** — thread 4→4→2→7→4, **196건, the largest on the board**
  (07-21 peak: 134 articles / 7 outlets). Tagged FADING **only because the window ends on a 102-event day.**
- **301조 관세 / '글로벌 관세 10%' 만료: 97 hits/7d.** A **statutory** US action aimed at Korea, separate
  from the negotiation.
- **방미 D-0, unprinted:** *"김정관 22일 방미"* [mt] · *"발표만 남은 대미투자 1호…막판 조율"* [mt] ·
  *"76일 만에 만나는 김정관·러트닉"* [sedaily] · *"쿠팡이 변수"* [sedaily/mk/donga]. **Zero 07-22 hits.**
- [yonhap/mt 07-21] 트럼프, **'美에 공장 건설' 조건부 알루미늄 관세 절반 인하** (러트닉) — the carrot.

**★ Semis — narrative intact, and the KR feed itself names tonight's binary:**
- **[17a/7s, HEAD] [뉴욕증시] 실적 호조·반도체주 반등에 상승** — thread **BUILDING 6→7→6→6→7, 129건**
  (한은 총재 "반도체 가격 주시" → 한은 "반도체發 교역조건 개선, 내수 파급 클 것" → 코스피 6700 회복 →
  today's NY session)
- **[4a/3s] 구글 실적 발표 D-1, 반도체주 반등 분수령 될까…관건은 '돈 버는 AI'** ← the binary, named by the press
- [2a/2s] **7월 수출 549억달러 역대 최대, 반도체 +180%** (thread FADING 8→2 — day-2 decay of a real print)
- **[3a/3s] 이재용·최태원·이해진, 미국서 젠슨황 만난다…AI리더 총집결** ← ★ new, 3 outlets, no bucket saw it
- [2a/2s] **엔비디아 차세대 '베라루빈' 본격 공급** · [2a/2s] **'K-디스플레이 2026' — 삼성D·LGD·소부장 '피지컬AI'**
- [2a/2s] **신한투자 "하나머티리얼즈, 올해 고성장…목표주가↑"** · [4a/2s] **SK㈜ 31일 이사회 — SK실트론 매각 GO/STOP**

**★ Robotics / physical AI — the axis 07-21 flagged as un-owned is now an 8-outlet event:**
- **[8a/4s] 반도체 다음은 로봇… 삼성전자, '휴머노이드' 승부수** (thread 2→7→4; **휴머노이드 142 hits/7d**)
- **[2a/2s] 블랙스톤도 찜한 로봇 관절…냉장고 모터회사에 개미들 몰려간 이유** ← the value-chain hop, retail already there
- [mt] [시선강탈] 삼성전기 vs 하나마이크론 vs **로보티즈**
⚠ **Still no measured KR vehicle in §2.** See the §5 structural lesson — this is the third run in a row
this axis has been *right and un-ownable*.

**★ Financials — the credit-cost print (see §1) plus structure:**
- **[5a/4s] 은행 연체율 2016년 10월 이후 최고 · [3a/3s] 5월 0.67%, 9년 7개월 최고** — thread FADING
  6→4→3→7→4→4, **45건, 6 sustained days** (주담대 8% → DSR 우회 서민급전 → 카드사 조달비용 → 은행권
  3분기 문턱↑ → 카드론 15% → **연체율**). ★ **A 6-day thread that has walked from margin to delinquency.**
- **[6a/5s, HEAD] 롤러코스피에 질린 개미들…은행 예금에 16조** (thread 2→4→7→7→5, 42건)
- **[3a/3s] 서학개미 순매수 5개월 최대** (49 hits/7d) · [2a/2s] JP모건 "코스피 급락은 삼전닉스 레버리지 탓"
- **[2a/2s] 李대통령 "레버리지 보완책 충실히"…당국 조기 시행 협의 착수** — regulatory response to the ETF leg
- [4a/3s] **미래에셋증권 목표가 하향** ("변동성 해소 관건") · [4a/3s] NH투자 2Q 예상 부합 · [2a/2s] 당정 서민금융법

**Utilities / power-equipment — the pro-vector landed in INDU, not UTIL:**
- **[6a/4s] LGU+·LS일렉트릭, AI 데이터센터 800V DC 공동 개발** ← ★ 4 outlets, **전력기기 = INDU**
- **[2a/2s] KB증권 "현대건설, 원전 모멘텀 하반기에 재점화…목표가 28% 하향"** ← catalyst pushed out, in writing
- [3a/3s] '모두의 AI' 윤곽, 부분 유료화 허용 (AI 메가프로젝트 thread FADING 7→8→6→4→8→6→3, 114건)

**Autos · industrials · materials · staples · RE:**
- **[2a/2s] 수출에 답 있었다… 현대차 中공장 '활로'** (BUILDING 2→2) — ★ the first *positive* 현대차 print in
  three runs, against 07-21's KB증권 목표가↓
- [2a/2s] **LIG D&A·KAI, 에어버스와 차세대 항공체계 협력** · [2a/2s] "LIG디펜스앤에어로스페이스…CAPEX·선호주↑"
  (LIG D&A×LG AI 지휘통제 thread FADING 5→7→4) · **`LIG` is a ★new emergent term (17) in §3d**
- [2a/2s] **재가동하는 LG엔솔 전기차 배터리 공장…'캐즘' 변곡점** (REIGNITED 3→2)
- **[2a/2s] 5월 서울 아파트값 1.3% 껑충…전셋값도 1.0% 상승** ← into a **real 10Y at 2.35%, the sequence high**
- [2a/2s] "롯데렌탈, 하락장 방어주 부각…목표가 4.5만"-키움 · [4a/3s] GS25 아이돌 컴백 플랫폼

### §3b Trajectory axis [`thread --days 7 --scope domestic`]
**Per-day denominator: 07-16 453 · 07-17 185 · 07-18 165 · 07-19 246 · 07-20 475 · 07-21 517 · 07-22 102.**
2,143 daily events → 1,634 threads (303 multi-day, **51 alive**, 1,331 one-day incl. 51 new today).

⚠⚠ **The window-end correction is the strongest it has been in three runs: 102 events after 517.
EVERY "FADING" tag below is presumed a window artifact until a per-day count refutes it.** The 07-20 rule
("a FADING tag on a live physical driver is an attention gap") applied for a third time and was right
twice; today it applies to **four** threads at once.

| Thread | Tag | Curve (outlets) | Read |
|---|---|---|---|
| **반도체/한은 교역조건** | **BUILDING** | 6→7→6→6→**7** · 129건 | ★ **The only large thread that BUILT into a shrinking window** — genuinely accelerating |
| **홍해/후티 해상봉쇄** | **BUILDING** ★ | 2→5→4→**5** · 31건 | ★★ **New independent supply axis, 4 days old, now carrying a US strike threat.** Does NOT run through Hormuz |
| **호르무즈/유가** | FADING ⚠artifact | 4→3→6→**8**→3 | **Peaked at 8 outlets yesterday**, 3 today on a 102-event day. Brent +2.60%. **Not fading** |
| **관세(캐나다 50%/301조)** | FADING ⚠artifact | 4→4→2→**7**→4 · **196건 ★largest** | 134 articles/7 outlets on 07-21. **Not fading — the window shrank 5×** |
| **대출/연체율/조달비용** | FADING ⚠artifact | 6→4→3→7→4→**4** · 45건 | ★ **6 sustained days and it ESCALATED in content today** (margin → delinquency). Tag is meaningless here |
| **롤러코스피 → 예금 16조** | FADING ⚠artifact | 2→4→7→7→**5** · 42건 | **Head tier today.** Retail capitulation, sustained |
| **AI 메가프로젝트/정책** | FADING | 7→8→6→4→8→6→**3** · 114건 | Week's 2nd-largest. **First curve where decay may be real** — 3 outlets even scaled |
| **코스피 급락/사이드카** | FADING | 2→5→2→8→6→**3** · 102건 | Decaying with the bounce — **consistent, not artifact** |
| **7월 수출 549억달러** | FADING | 8→**2** | Day-2 decay of a one-print event. Normal |
| **삼성 로봇/RX사업추진실** | FADING ⚠artifact | 2→7→**4** | Peaked at 7. **8-outlet event today in `brief`** — the thread tag disagrees with the day view |
| **LIG D&A×LG AI 지휘통제** | FADING ⚠artifact | 5→7→**4** | Peaked 7; new KAI·에어버스 leg today |
| **현대차 中공장 활로** | **BUILDING** ★new | 2→**2** | Small, but the first 현대차 positive in 3 runs |
| **LG엔솔 배터리 재가동** | REIGNITED | 3→**2** | '캐즘' 변곡점 framing returned |
| **환율(달러-엔 163)** | REIGNITED | 2→**2** | 07-18 1,490원 돌파 → today 40-year yen low |

**ENDED this window (171 threads; peak-8 items):** **코스피·코스닥 매도 사이드카** (8→5→5→3→7) ·
**이억원 금융위원장 레버리지 ETF 보완책** (8→2→4) · **한은 기준금리 2.75% 인상** (8→5) ·
**원화 국제화** (8→2) · **1인가구 머니무브** (8→2) · **원·달러 1478.4원** (5→3→7→6) ·
**메리츠 홈플러스 2000억** (7→4→7→7) · **종부세 주택수 기준** (7→2→6→6) · **한화 방산·조선 상생금융** (5→7→5) ·
**한화 필리조선소 美 계측선 수주** (7→6→2).

⚠ **Staleness flags on ENDED threads under still-open propositions:**
- **M-01 (BOK hike) — ENDED for a 3rd consecutive run.** Re-justified again on §2 transmission flow only.
  **And this run its ENDED status is joined by a live, escalating COST thread (연체율).** The proposition is
  now carried by flow alone while both news legs point the other way. **Flagged as a maturing thesis.**
- **매도 사이드카 / 레버리지 ETF 보완책 ENDED** — the crash-mechanics narrative is genuinely over; the
  **예금 16조 / 서학개미** successor threads are where that attention went. Consistent with the bounce.
- **원화 국제화 ENDED for a 2nd run** — dormant, held there.
- **한화 필리조선소 수주 ENDED (7→6→2)** — ★ the 조선 leg's last *positive* thread died this window,
  the same window in which its short built. Recorded.

**BUILDING/escalating threads with no matching bucket → candidate new terms:** **해상봉쇄/후티** ·
**연체율** · **휴머노이드** · **서학개미** · **젠슨황 회동**.

### §3c Term axis — 7-bucket velocity [domestic · 7d · OR + `--syn` + `--kr`, **terms as separate argv**]
**Pool 20,578 → 18,731 = −9.0%. That is the bar every bucket must clear.**

| Rank | Bucket (argv verbatim) | 7d now | 07-21 | Δ | vs pool (−9.0%) |
|---|---|---|---|---|---|
| 1 | `반도체 메모리 인공지능 데이터센터 파운드리` | **4,619** | 5,275 | −12.4% | underperformed (−3.4pp) |
| 2 | `부동산 가계대출 주택담보대출 총량규제 전세` | **1,592** | 1,671 | −4.7% | **outperformed (+4.3pp)** |
| 3 | `코스피 외국인순매수 공매도 레버리지ETF 신용융자` | **1,284** | 1,275 | **+0.7%** | ★★ **+9.7pp — the ONLY bucket to rise in absolute level** |
| 4 | `호르무즈 국제유가 이란 중동정세 원유` | **786** | 1,095 | **−28.2%** | ★★ **−19.2pp — the sharpest collapse on the board** |
| 5 | `금융위원회 상법개정 세제개편 규제완화 대미투자 관세협상 공정거래` | **444** | 477 | −6.9% | ~pool |
| 6 | `기준금리 통화정책 한국은행 코픽스 국고채` | **742** | 785 | −5.5% | outperformed (+3.5pp) |
| 7 | `원달러 환율하락 환율상승 외환시장 원화가치 달러화 원화국제화` | **90** | 119 | −24.4% | underperformed (−15.4pp) |

⚠ **All seven passed as separate argv, 3+ char forms only** (the 2-char trigram trap verified 07-20 and
carried forward unchanged — deltas are comparable).

**The two buckets that moved against the pool, and they disagree with each other's sector:**
- **Bucket 3 +0.7% on a −9.0% pool.** ★ **The crash/leverage/short-interest narrative is the only thing
  gaining share — on a +9.7% two-day bounce.** That is not a bullish tape reading itself bullish; it is
  **the market talking about its own mechanics** (예금 16조, 서학개미, 레버리지 보완책, JP모건).
  **Records as a fragility signal, not a momentum signal.**
- **Bucket 4 −28.2% while Brent printed +2.60%/+8.04%(5d) and the 홍해 thread BUILT.**
  ★★ **This is a fresh narrative–flow inversion, in the same sector where the rule was validated on 07-21 —
  and it is pointing the OTHER way this time (story down, price up).** Failure class #2's rule
  ("when narrative and measured flow invert, the flow sets the tilt") applies symmetrically: **back the
  price/flow, track the narrative as the anti-signal.** ENRG tilt held on that basis in §4.

**★ NEW TRIGRAM-TRAP ENTRY — and it is why bucket 4 undercounts:**
`홍해` **0** · `후티` **0** · `예멘반군` **0** · `선박보호` **0** · `홍해봉쇄` **0** — **every key noun of
the run's newest supply axis is 2-char or an unjoined phrase, so the KR term index is STRUCTURALLY BLIND
to it.** The only working form found: **`해상봉쇄` = 30.** **The event axis carried this thread at 5 outlets
in the head tier while the term axis scored it at zero.** Added to the living trap list.

**Coverage** [`coverage 기준금리 원달러 반도체 부동산 코스피 국제유가 인공지능 --days 7 --scope domestic`]:
pool **18,731건** (본문 보유 11,511 = 61.5%) · 현재 검색 2,001 · 본문 매칭 4,543 · **놓침 3,325** ·
**recall 37.6% → 🔴 심각, 본문 블라인드 62.4%.** **Non-zero denominator → the 🔴 is real.** Recall is flat
for a third run (37.7 → 37.3 → **37.6%**) — **the fixed term set sees ~37% and that number will not move
until body-search is on by default. The blindspot pass is covering a 62% hole.**

### §3d Blind-spot pass [`blindspot --sample-pct 35 --days 7`, 18,731 pool / 6,555 sample, read RAW]
Token-0 emergent terms (07-21 in parentheses): `AI 729 · LG 129 · KT 105 · YTN 68 · KB 65 · BTS 56 ·
**ADR 52 (67)** · SSG 52 · KIA 51 · SNS 41 · EU 35 · SK 32 · MOU 30 · **AX 25 (32)** · **TSMC 23 (24)** ·
**Vietnam 22 (21)** · **LIG 17 (—)** · SKT 16 · **MBK 16 (22)** · KAIST 15`.

- **`ADR` 67 → 52 (−22%, vs a −9% pool) — decaying, but present for a third run and STILL UNRESOLVED.**
  The question stands: does SK하이닉스's US listing explain the **−721.9만주** 20-day domestic foreign exit
  (venue substitution) rather than a thesis exit? **07-20 assigned it to SWEEP; 07-21 escalated it because
  SWEEP declined it. It is now the oldest open item on this desk.** §4x gives it a forced disposition.
- **`LIG` 17 ★NEW to the top-30** — 방산 surfacing as an emergent *name* on the day LIG D&A prints twice
  (LG AI 지휘통제 + 에어버스 회전익) and a broker raises it to 선호주. ⚠ **The flow says the opposite
  (한화에어로 RS60 −47.3%).** Named as a narrative–flow divergence in the making, not a tilt.
- **`Vietnam` 22 (17→21→22) — third consecutive rise against a falling pool.** KR outbound manufacturing
  footprint. **Fourth run at watch-flag; if it clears again next run it should become a bucket term.**
- **`AX` 32→25 · `TSMC` 24→23 · `MBK` 22→16** — all decaying with or faster than the pool. Nothing new.
- ⚠ **`관세`·`301조`·`연체율`·`휴머노이드` do NOT appear in the top-30 emergent terms** despite a 196-article
  trade thread, a 6-day credit thread, and 142 hits for 휴머노이드. **Third consecutive run of the same
  structural failure: a 7-day emergent-term window cannot see a fast-moving event, and it cannot see terms
  that are already common words.** **The event axis caught all four; the term axis caught none.** This is now
  a *characterized* limitation, not a surprise — the blindspot pass finds **proper nouns**, not themes.
- Raw sample rows worth the read: *"[오늘의 브릿지경제 1면] 내놓는 족족 소비자 외면… 보험정책 '4전 전패'"*
  — an insurance-policy failure lane inside FIN, invisible to every bucket; *"반도체 수출 호조에 코스피
  3%대 반등…6700선 회복[마감시황]"* — the 07-21 close confirmed from the blind pool (this is the print the
  yfinance benchmark is missing); *"CJ제일제당 증류주 '자리'"* — STPL product lane.

**Living term-table additions this run:** `해상봉쇄/후티/홍해` (⚠ **index-blind — use 해상봉쇄**) ·
`연체율/조달비용` · `휴머노이드/로봇관절` · `서학개미` · `젠슨황 회동` · `800V DC/전력기기` ·
`SK실트론 매각` · `LIG D&A`. (Carried: `301조 관세/무역법338조`, `예금금리/수신경쟁`, `ADR/원주 괴리`,
`AX`, `Vietnam`, `CXL`, `신규팹 4곳`, `비은행 자금조달/근저당`, `전력감독원`, `MBK/홈플러스`.)

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Δ = change vs 07-21. Not equal-weight analysis.
> **All RS20 figures are DATE-ALIGNED (§2 trap). All flow asof 09:32 intraday. US rates asof 07-20.**
> ⚠ **No tilt below moves on today's price action alone** — a +5.93% morning inside a −21.58% month is
> a beta event, and this desk's own 07-21 lesson forbids scoring a regime on one session.

| # | GICS Sector | Tilt | Δ vs 07-21 | Prop | One-line why (KR) |
|---|---|---|---|---|---|
| 1 | **Financials (FIN)** | **OW** ▼ *conviction cut from "highest"* | = tilt, **▼conviction** | M-01 | **Flow 4th-run confirmed and the foreign leg COMPLETED: KB +34.3% / 하나 +33.6% / 신한 +29.6% aligned RS20, all OBV 매집, all 기관 실매수, and now ALL THREE 외국인5일 매수전환↑** vs a benchmark −21.58%/1m. ★ **But the cost side printed a NUMBER for the first time: 은행 연체율 2016년 10월 이후 최고 [5a/4s] · 5월 0.67% 9년7개월 최고 [3a/3s] · 중소기업 대출 빨간불 · 카드론 15% 돌파.** Plus the carried deposit war (예금 16조), 카뱅 파업 07-31, 하나 short building. **M-01 is now carried by flow while BOTH news legs (BOK ENDED, 연체율 escalating) point away — that is a maturing thesis, not a broken one, but it loses the top slot** |
| 2 | **Energy (ENRG)** | **tactical OW** | = tilt, **★narrative INVERTED again (other way)** | M-02 | **S-Oil aligned RS20 +53.2% board-best, RS60 +11.3%, OBV 매집, 기관 +191.1만, 개인 −183.4만.** **BZ=F 91.54 (+2.60% 1d, +8.04% 5d, +17.51% 1m).** ★ **New independent supply axis: 홍해/후티 해상봉쇄 BUILDING 2→5→4→5, now with 트럼프 "美가 처리…이란 곡괭이산 곧 타격" [6a/5s HEAD] — it does NOT run through Hormuz, so a Hormuz TACO does not close it.** ⚠⚠ **But bucket 4 collapsed −28.2% vs a −9.0% pool — a narrative–flow inversion pointing the OPPOSITE way from 07-21's.** Per failure-class-#2's rule, **the flow sets the tilt**. ⚠ New anti: **정유사 "설비는 중동산 맞춤형" 수입선 다변화 진땀** [2a/2s] = disruption is a COST to S-Oil too; **국제유가 꺾여 PPI 멈춤** [5a/5s HEAD] already stale; **S-Oil −0.07% today**, short building |
| 3 | **Health Care (HLTH)** | **OW-as-SHELTER** (per the 07-21 CORRECTION) | = tilt, **★model CONFIRMED out-of-sample** | M-07 | **셀트리온 UPGRADED 🟡→🟢가속, OBV 중립→매집, 기관 +126.8만 / 개인 −195.5만**, catalyst 트룩시마 북미 점유율 38.6% 4개월 연속 1위; 삼바 매집 held, 외국인·기관 동시 매수. ★★ **The corrected β-0.44 shelter model made a prediction and it held: on a +5.93% index morning, 셀트 +2.51% / 삼바 +2.22% = ~−3.4pp under-delivery, exactly the "leaks on up days" behaviour.** **Do NOT re-upgrade to a destination — the 07-21 correction was earned and is now confirmed twice.** ⚠ RS60 deteriorated for both (−22.4 / −21.1) |
| 4 | **Information Tech (IT/반도체)** | **Neutral, flow-GATED** | = tilt, **★the "gate opened" reading was a DATA ARTIFACT** | M-04 | ★★ **Raw output said 삼전 RS20 −0.8% → +9.9%; date-aligned it is −0.9% — UNCHANGED. 하이닉스 aligned −9.8%, still deeply negative. The gate did not open; the benchmark had a hole.** ⚠ **One leg improved for real and it is NOT benchmark-relative: 기관 net-buy on 삼전 DOUBLED (+397 → +832만주), 하이닉스 기관 selling shrank (−171.6 → −79.8만), foreign exit shrank (−815.7 → −721.9만).** Narrative intact (수출 +180.6%, thread BUILDING 129건, 한은 교역조건). **삼전 +5.79% / 하이닉스 +8.93% today came on ~0.01% short interest = no squeeze fuel, i.e. cash buying — durable if it persists, but 32 minutes is not persistence.** **알파벳 실적 tonight is the named binary** |
| 5 | **Industrials (INDU)** | **Neutral (split), 조선 leg ▼▼ downgraded again** | ▼ within-tilt | M-03, M-06 | ★ **조선: the short did not blink at its own D-0.** 한화오션 공매도 **1.44% still building(+0.17) ⚠주목**, aligned RS60 **−48.1% (worse)**, 외국인 −421만 / 개인 +457만; HD한국조선 short building(+0.09). ★ **And a hard fact arrived for the shorts: UAE ordered ₩1.3tn of LNG carriers from CHINA after meeting 김정관·김동관** [chosun]. **The leg's last positive thread (필리조선소 수주) ENDED this window.** 방산: events yes (LIG D&A×에어버스·KAI, `LIG` ★new emergent term, 선호주↑) — **flow no** (한화에어로 aligned RS60 −47.3%). ★ **New positive vector: LGU+·LS일렉트릭 AI DC 800V DC [6a/4s] — 전력기기 belongs HERE, not in UTIL** |
| 6 | **Utilities (UTIL/원전)** | **UW** | = tilt, **★contest RESOLVING toward UW** | M-03 | **두산에너빌리티: the 07-21 institutional inversion WEAKENED — 외국인 +52.3 → +2.6만주 (evaporated), 기관 +60.7 → +49.8만, OBV still 분산, aligned RS60 −51.1% board-worst.** ★ **Corroborating and dated: KB증권 "현대건설 원전 모멘텀 하반기에 재점화…목표가 28% 하향"** — the catalyst is being **pushed out in writing with a target cut**. 한전 기관 +204.4만 held (the one intact leg). **UW held with more confidence than 07-21** |
| 7 | **Materials (MATR)** | **UW** | = | M-05 | **4th consecutive run of narrative-without-money: POSCO OBV 분산 held, 기관 −27.0만, aligned RS60 −37.5% (worse than −33.7%)**, price +3.30% on a +5.93% index = **underperformed the bounce.** ⚠ **One thing to watch, not act on: 외국인 has now been the ONLY net buyer for 3 straight runs (+31.7 → +28.8만).** LG화학 aligned RS60 −44.4%, 기관 −36.7만. Copper 95%ile crowded-long (stale COT) |
| 8 | **Consumer Disc (DISC)** | **UW** ▲ *conviction cut* | = tilt, **▲conviction cut — genuinely two-sided now** | — | **현대차 aligned RS20 −4.2% (NOT the +5.8% the tool printed), aligned RS60 −32.6%, OBV 분산, KB증권 목표가↓ carried.** ⚠ **But three things moved for it in one session: 외국인5일 매수전환↑ NEW, 기관 +25.9 → +36.2만, and the first positive thread in three runs (수출에 답…中공장 활로, BUILDING).** ⚠ **And the mechanical leg is loud: short 1.99% ⚠주목 COVERING (−0.51), stock +8.27% today.** **A UW into a covering crowded short is the most uncomfortable position on this board — held, but flagged for ROTATION** |
| 9 | **Real Estate (RE)** | **UW (most rate-negative)** | = tilt, **↑evidence** | M-01 | ★ **The discount rate got WORSE, not better: real 10Y 2.35% [FRED 07-20] is the highest of the sequence (+4bp).** Into **5월 서울 아파트값 +1.3%, 전셋값 +1.0%** [2a/2s] and **은행 연체율 9년 7개월 최고**. 보금자리론 인상 · 대출총량 1.5% cap · 비은행 자금조달 확산 all carried. ⚠ **Keep separating 건설 order-flow from RE asset** — LGU+·LS일렉트릭 DC, 부천 신뉴딜, 중앙·지방 건축현안 협의 are **INDU/건설**, not RE-asset positives |
| 10 | **Consumer Staples (STPL)** | **UW** | = | M-01 | No fresh macro print. Carried: 나프타 cost-push, 고물가 가성비. Name-level only: GS25 아이돌 컴백 플랫폼 [4a/3s], 신세계 제주 기획전, CJ제일제당 증류주. **A sector with no wind and a throttled consumer — held UW on the credit prints, not on its own news** |
| 11 | **Comm Services (COMM)** | **Neutral** | = | — | No distinct KR wind. Watch-flags: **알파벳 실적 tonight** (spillover), **'모두의 AI' 부분 유료화 허용** [3a/3s], **프랑스 15세 미만 SNS 금지** [5a/2s] (platform-regulation read-through, 2nd REIGNITED appearance) |

**Net wind:** **the tape exploded and almost nothing in the evidence moved with it — which is the finding.**
**The single largest change vs 07-21 is not a sector; it is that yesterday's most exciting conclusion
("the memory gate rattled and may be opening") turns out to have been reading a benchmark data hole.**
On corrected numbers: **FIN and ENRG still own the only two positive-RS flow structures on the board**, and
**both acquired a real anti-signal today** (연체율 for FIN, 정유설비 중동 의존 + a −28% narrative collapse
for ENRG). **HLTH's corrected shelter model made an out-of-sample prediction and it held** — the most
valuable single result of this run. **What deteriorated: 조선 (short building into its own D-0, plus the UAE
→ China order), UTIL (the institutional inversion evaporated, 원전 catalyst pushed out in writing).**
**What is genuinely new and un-owned: 해상봉쇄** (index-blind), **연체율**, **휴머노이드** (third run
right and un-ownable), **서학개미**.

### §4x ★ Divergences ROTATION must resolve (named explicitly per the L1 rule)
- **(a) ★★ HIGHEST PRIORITY — the RS20 benchmark hole.** `module_flow` RS is bar-count-differenced and
  `^KS11` is missing 2026-07-21. **Every downstream stage that reads RS20 today (SWEEP shortlist, DEEP,
  BET sizing) will be reading numbers inflated 5–11pp unless it re-derives them date-aligned.**
  **Owner: SWEEP — first action, before shortlisting.** Use the §2 aligned column, or patch the module.
- **(b) 조선 — the D-0 fired today and the short was still building into it.** 한화오션 1.44% ⚠주목 +
  UAE→China ₩1.3tn + the last positive thread ENDED. **Owner: ROTATION** (KR has no PREMORTEM block).
  **A one-way 조선 tilt in either direction before the 방미 outcome prints is a protocol violation.**
- **(c) IT — the gate, re-specified.** The benchmark-relative leg did NOT move; **the institutional leg
  did (기관 +397→+832만).** **Owner: SWEEP.** Specific test in M-04.
- **(d) ★ ADR venue substitution — UNRESOLVED FOR THREE RUNS, now the desk's oldest open item.**
  `ADR` 67→52. Does SK하이닉스's US listing explain the −721.9만주 domestic foreign exit?
  **Owner: SWEEP. Forced disposition: resolve it with the ADR–원주 괴리 + ADR volume vs domestic foreign
  net, or DECLINE IT IN WRITING and delete it from the carry list. It may not be carried a fourth time.**
- **(e) ENRG — the narrative–flow inversion flipped sign.** Bucket 4 **−28.2%** vs a −9.0% pool while
  Brent +2.60%/+8.04% and the 홍해 thread BUILT. **Owner: DEEP-ENRG.** Is the term collapse real, or is it
  the trigram blindness (홍해·후티·예멘 all = 0)? **Re-run bucket 4 with `해상봉쇄` added before concluding.**
- **(f) FIN — margin vs delinquency.** 예대마진 expansion (flow says yes, 4 runs) vs **연체율 9년 7개월
  최고 + 카드론 15% + 중소기업 빨간불**. **Owner: DEEP-FIN.** The 2Q NIM prints (late July) settle it.
- **(g) 현대차 — a UW into a covering 1.99% short with a fresh foreign 5-day flip.** **Owner: ROTATION.**
- **(h) 휴머노이드/로봇 — right for three runs, un-vehicled for three runs.** [8a/4s] 삼성 RX사업추진실,
  142 hits/7d, 블랙스톤 로봇관절, 로보티즈. **Owner: SWEEP** — find a measurable KR vehicle or state
  explicitly that the axis stays a term, never a tilt (P4: a thesis with no measurable vehicle is not a tilt).

---

### §4a Falsifiable propositions — both branches mandatory on every oscillating variable

- **M-01 — Hike transmission → bank NIM (CARRIED, flow-confirmed a 4th time; ★THE ANTI-BRANCH PRINTED A NUMBER).**
  *BOK 2.75% + hiking bias → 코픽스 3%·주담대 8% → variable-rate repricing → NIM. **Flow: KB aligned RS20
  +34.3%, 하나 +33.6%, 신한 +29.6% — all OBV 매집, all 기관 실매수, and this run ALL THREE carry
  외국인5일 매수전환↑**, against ^KS11 −21.58%/1m.*
  **Thread:** originating BOK thread **ENDED for a 3rd consecutive run** → re-justified on transmission flow
  only. **대출/연체율 thread ran 6 sustained days and ESCALATED in content** (주담대 8% → DSR 우회 →
  카드사 조달비용 → 문턱↑ → 카드론 15% → **연체율**), tagged FADING **only by window artifact**.
  **★ Anti-signal (upgraded from mechanism to measurement):** **은행 연체율 2016년 10월 이후 최고** [5a/4s],
  **5월 0.67%, 9년 7개월 만의 최고** [3a/3s], **중소기업 대출 빨간불**, 카드론 15% 돌파. Plus the carried
  liability-side repricing (예·적금, 16조), 카카오뱅크 노조 07-31 파업, 하나 short building(+0.09),
  대출총량 1.5% cap.
  **Track KPI:** **예대금리차** · **연체율 6월치** (the new primary — does 0.67% keep climbing?) ·
  bank 2Q NIM prints (late July) · whether all three hold OBV 매집 and the 외국인 5일 flip.
  **Kill-switch:** any of the three flipping to OBV 분산, **or** a 2Q NIM that contracts QoQ, **or**
  연체율 climbing a third month → M-01 becomes a credit-cost story and FIN loses its OW.
  ⚠ **Both news legs now point away from this proposition and only the flow holds it up. That is exactly
  the configuration failure-class-#2 says to trust — but it is also the configuration in which a thesis
  dies quietly. It is on notice.**

- **M-02 — Oil / Red Sea (★ THE INVERSION FLIPPED SIGN — same sector, opposite direction).**
  *07-21: "money accumulating S-Oil while the story decays" → the story came back. **Today the story left
  again: bucket 4 −28.2% against a −9.0% pool, the sharpest collapse on the board — while Brent printed
  +2.60% / +8.04%(5d) / +17.51%(1m) and the 홍해/후티 thread BUILT 2→5→4→5 into a US strike threat.***
  ★ **The new axis is genuinely independent: 홍해 does not run through Hormuz**, so a Hormuz-opening TACO
  does not close it. **[6a/5s HEAD] 트럼프 "후티 홍해 봉쇄시 美가 처리…이란 곡괭이산 곧 타격."**
  ⚠ **Measurement caveat, and it may explain the whole bucket-4 collapse: 홍해·후티·예멘반군·홍해봉쇄 all
  return 0 hits (2-char trigram / unjoined phrase). The KR term index is structurally blind to this axis.
  Only `해상봉쇄` (30) works.** **Do not score the −28.2% as attention loss until bucket 4 is re-run with
  the working synonym** — assigned to DEEP-ENRG in §4x(e).
  **Anti-branch (equal weight, and it gained a NEW name-level leg):**
  **[2a/2s] "설비는 '중동산 맞춤형'인데… 정유사 '수입선 다변화' 진땀"** — ★ **a Middle East supply
  disruption is a COST to S-Oil's own configuration, not only a crack-spread gift.** Plus
  **[5a/5s HEAD] 국제유가 꺾이자 PPI 상승 멈춤** (a relief print already contradicted by today's tape),
  **S-Oil −0.07% on a +5.93% index**, S-Oil short **building at 0.49%**, WTI COT 10%ile crowded-short
  (a ceasefire removes the bid rather than squeezing).
  **Track KPI:** BZ=F 91.54 · **해상봉쇄 headline count (the working synonym)** · S-Oil OBV + the 0.49%
  short direction · **whether S-Oil keeps underperforming the index on up days** (a shelter tell that would
  reclassify it out of "tactical OW").

- **M-03 — AI-power / DC capex (kill-switch STILL FIRING on the hyperscaler leg; ★the two legs separated further).**
  - **Hyperscaler/원전 leg: still breaking, and now with a dated broker cut.** 두산 aligned RS60 **−51.1%**
    (board-worst), OBV 분산, **the foreign net-buy that made 07-21 interesting evaporated (+52.3 → +2.6만)**;
    **KB증권 "현대건설 원전 모멘텀 하반기에 재점화…목표가 28% 하향"** [2a/2s].
  - **Domestic-policy AI leg: DECAYING for the first time.** 재경부/메가프로젝트 thread **7→8→6→4→8→6→3,
    114건 — 3 outlets even after scaling for the shrunken window.** The 07-21 report called this "the week's
    largest thread, intact." **It is no longer building.** Recorded as a genuine change, not an artifact.
  - **★ New sub-leg with an actual print: 전력기기, and it belongs to INDU.** **LGU+·LS일렉트릭 AI DC 800V
    DC 공동 개발** [6a/4s]. **This is the first AI-power print in three runs with a named KR corporate pair.**
  **Anti-branch (pro-capex, equal weight):** **알파벳 실적 tonight** — the KR feed itself calls it
  *"반도체주 반등 분수령…관건은 '돈 버는 AI'"* [4a/3s]; **이재용·최태원·이해진 × 젠슨황 회동** [3a/3s];
  엔비디아 베라루빈 본격 공급; 블랙록 DC 18조 채권 (carried).
  ⚠ **Un-tunneling note, third consecutive run: the domestic-policy leg still has NO measurable KR vehicle
  in §2. 전력기기 (LS일렉트릭·HD현대일렉트릭) is the first candidate the desk has seen — it is not on the
  §2 board and should be added by SWEEP.**
  **Track KPI:** **알파벳 tonight** · 두산 RS60 stabilization · 한전 기관 +204.4만 persistence ·
  **LS일렉트릭 / HD현대일렉트릭 flow once SWEEP adds them.**

- **M-04 — Memory supercycle (thesis OW / flow-gated. ★ THE GATE IS STILL SHUT — 07-21's "rattle" was a data artifact).**
  *07-21 recorded "the named KPI fired: 삼전 RS20 −4.9% → −0.8%, both names 외국인5일 매수전환↑."
  **Today's raw output said RS20 improved a further +10.8pp. Date-aligned, it is −0.9% — unchanged. The
  improvement was the benchmark's missing 07-21 bar.** 하이닉스 aligned **−9.8%**, still deeply negative.*
  **★ The gate is therefore RE-SPECIFIED to conditions that cannot be faked by a benchmark hole:**
  1. **20-day 외국인 net-buy turns positive** (currently 삼전 **−4,013만**, 하이닉스 **−721.9만**) —
     an absolute quantity, not benchmark-relative.
  2. **기관 net-buy persists ≥2 more sessions** (this is the one leg that genuinely moved: 삼전
     **+397 → +832만**, hynix 기관 selling **−171.6 → −79.8만**).
  3. **개인 흡수 flag clears** (currently 삼전 개인 +3,116만 = still the absorber).
  **Narrative intact and building:** 반도체/한은 교역조건 thread **BUILDING 6→7→6→6→7, 129건** (the only
  large thread to build into a shrinking window); 수출 +180.6%; 삼전 +5.79% / 하이닉스 +8.93% today.
  ⚠ **Both names carry ~0.01% short interest — today's move had NO squeeze fuel, so it was cash buying.
  That is better quality than a squeeze and worth less as evidence than 32 minutes suggests.**
  **Anti-branch (equal weight):** 7월 수출's own **MoM −13%** (carried, unrefuted); **알파벳 tonight**
  can close this in one print; ADR venue substitution unresolved (§4x-d); 하이닉스 aligned RS20 still −9.8%.
  **Track KPI:** the 3 re-specified gate conditions · 알파벳 · MoM 수출 in the 8월 1~10일 print.

- **M-05 — 철강/소재 narrative refuted by flow → UW (CARRIED, 4th consecutive run).**
  *POSCO: OBV **분산** held, 기관 **−27.0만**, aligned RS60 **−37.5%** (worse than −33.7%), price **+3.30%
  on a +5.93% index = underperformed the bounce.** LG화학 aligned RS60 −44.4%, 기관 −36.7만.*
  **Anti-branch (equal weight, and it is the one thing that keeps this from being closed):**
  **외국인 has been POSCO's only net buyer for three consecutive runs** (+31.7 → +28.8만). If 기관 flips
  positive while 외국인 holds, the refutation breaks.
  **Track KPI:** POSCO 기관 net-buy sign · OBV 매집 crossover · whether MATR outperforms on the NEXT
  up-day (today it did not).

- **M-06 — Trade: TWO instruments, TWO dates (★the 07-21 lesson applied, and the negotiated one fires TODAY).**
  *07-21 opened failure-class #3 — "watching the negotiation and missing the calendar." **The rule
  ("every policy proposition must name BOTH the negotiated instrument and the automatic one, and their
  dates separately") is applied here for the first time:***
  | Instrument | Type | Date | Status |
  |---|---|---|---|
  | **김정관–러트닉 방미 (대미투자 1호 · 조선 · 쿠팡)** | **negotiated, bilateral** | **D-0, TODAY** | 🔀 **unprinted — zero 07-22 articles** |
  | **301조 관세 / '글로벌 관세 10%' 만료** | **statutory, unilateral** | **undated, imminent** | 97 hits/7d, live |
  | **캐나다 50% (무역법 338조 선례)** | statutory, precedent | live | **196건 — the week's largest thread** |
  **Both branches, mandatory:** a 대미투자 1호 announcement is a **조선/INDU catalyst** — but §2 says the
  measured money is short into it (한화오션 1.44% building), **and the UAE ordered ₩1.3tn from China after
  meeting the same minister.** A 301조 imposition is a **broad 수출주 overhang** (반도체·조선·방산·자동차)
  that no negotiation outcome cancels.
  **Track KPI:** 방미 outcome headlines 07-22~24 · 301조 발효일 · 한화오션 short direction through the print.
  ⚠ **Nothing in §4 tilts on this binary before it prints.**

- **M-07 — HLTH as a low-β SHELTER, not a destination (★THE CORRECTED MODEL MADE AN OUT-OF-SAMPLE PREDICTION AND IT HELD).**
  *The 07-21 post-DEEP CORRECTION retracted "defensive bid as destination" and re-specified KR HLTH as
  **β ≈ 0.44 shelter that LEAKS on up days** (under-delivers its own beta by ~0.47pp; 삼바 lost to the index
  on 10 of the 10 largest up days, mean −4.56%).*
  **★ Today was the test, and the test was not run by choosing a day — it was the model's own stated
  behaviour on the next up-day that happened: index +5.93%, 셀트리온 +2.51%, 삼바 +2.22% — roughly −3.4pp
  under-delivery. The shelter sheltered and it leaked, as specified.**
  **Flow is genuinely better underneath:** 셀트리온 **UPGRADED 🟡→🟢가속, OBV 중립→매집, 기관 +126.8만,
  개인 −195.5만**, catalyst 트룩시마 **북미 점유율 38.6%, 4개월 연속 1위**; 삼바 매집 held, both sides buying.
  **Anti-branch (equal weight):** RS60 deteriorated for both (**삼바 −22.4%, 셀트 −21.1%**) — the shelter's
  20-day RS is, by the correction's own arithmetic, **mostly index collapse, not alpha**; the sector's binary
  risk is name-level and violent (코오롱티슈진 3상 실패 하한가, carried); the 07-21 "바이오헬스 수출 161억$"
  catalyst was overstated 2.7× (43.3% cosmetics).
  **Track KPI:** **셀트리온 OBV 매집 persistence** (the new primary — it is the upgraded name) · 삼바 RS60
  crossing 0 · **up-day excess on the next ≥+2% index day** (the model's own falsification test).

---

## §5 Self-backtest — **+7d** (07-15 → 07-22), the protocol horizon

⚠ **07-21's score was +1d and said so. This one is a true +7 calendar days / +4 sessions**
(07-16 · 07-17 · 07-20 · 07-21 · 07-22), scored against the **07-15** KR run's §4a.

| # | 07-15 proposition | Δ to 07-22 (measured) | Score (+7d) |
|---|---|---|---|
| M-01 | **한은 인상 초읽기 — 유가 defuse가 인상 여력 개방 (승격)** | **BOK hiked 25bp to 2.75% on 07-16/17**, unanimous, "continue hiking" | ★ **HIT — realized in 1–2 sessions** |
| M-02 | **호르무즈 — 비대칭 defuse (통행료 off / 봉쇄 on), both branches** | ★ **The "봉쇄 on" branch is the one that fired, via a route the proposition did not name:** Brent **91.54 (+17.51%/1m)**, 홍해/후티 **해상봉쇄 BUILDING**, Trump strike threat. S-Oil aligned RS20 **+53.2% board-best** | ★★ **HIT — and the both-branches bracket is what made it ownable** |
| M-03 | **메모리 슈퍼사이클 — 펀더 held ↔ vehicle 리레이팅 안 됨, funda-flow 디버전스** | **Funda held emphatically** (수출 +180.6%, 반도체 221억$ 역대최대, thread BUILDING 129건). **Vehicle STILL not re-rated after 7 days:** 삼전 aligned RS20 **−0.9%**, 하이닉스 **−9.8%**, 외국인 20d **−4,013 / −722만**. **ADR divergence unresolved for a 3rd run** | **HALF — the divergence the proposition named is exactly what persisted** |
| M-04 | **전력기기 슈퍼사이클 — 병목 규제화로 강화** | **UN-VEHICLED for 7 days.** No 전력기기 name was ever placed on the §2 board; the proxy used (두산) is 원전, not 전력기기. **The first real print arrived TODAY (LGU+·LS일렉트릭 800V DC, 6a/4s)** — 7 days late to be owned | **UNSCORABLE — and that is the finding** |
| M-05 | **K조선·방산 — war-premium 휘발·구조로 재평가, NATO 파이프라인 held** | ❌ **한화오션 aligned RS60 −48.1%, 한화에어로 −47.3%, HD한국조선 −29.3%; 한화오션 short 1.44% BUILDING; 필리조선소 수주 thread ENDED; UAE ordered ₩1.3tn from China after meeting 김정관·김동관** | ❌ **MISS — one-way, 7 days, no bracket** |
| M-06 | **로봇·피지컬AI — 정책+부품 상용화 지속 (watch, delta 약)** | ★ **Right, and it accelerated: 삼성 휴머노이드/RX사업추진실 [8a/4s], 휴머노이드 142 hits/7d, 블랙스톤 로봇관절, K-디스플레이 피지컬AI.** **Filed at "watch, delta 약" — the weakest confidence on the sheet — and it was the strongest call** | ★ **HIT — but un-vehicled, so unmonetizable** |
| M-07 | **UTIL 원전·SMR — AI 전력 종착 노드 (회전 deep 후보)** | ❌ **두산 aligned RS60 −51.1% board-worst, OBV 분산, foreign accumulation evaporated; KB증권 현대건설 원전 목표가 −28%, 모멘텀 "하반기" = pushed out** | ❌ **MISS — one-way, 7 days** |

**+7d tally: 3 HIT · 1 HALF · 2 MISS · 1 UNSCORABLE.**

### ★ The structural lesson, and it is uncomfortable

**Sort the +7d results by whether the proposition named a tradeable vehicle:**

| | Named a vehicle | Score |
|---|---|---|
| M-05 K조선·방산 | ✅ 한화오션·한화에어로·HD한국조선 | ❌ **MISS** |
| M-07 UTIL 원전 | ✅ 두산에너빌리티 | ❌ **MISS** |
| M-02 오일 | ✅ **S-Oil — the only vehicle chosen from FLOW** | ★★ **HIT (+53.2% RS20)** |
| M-06 로봇 | ❌ none | ★ **HIT, unmonetizable** |
| M-04 전력기기 | ❌ none | **UNSCORABLE** |

**Both 7-day MISSes are propositions where the desk DID name vehicles — and named them from narrative
(NATO pipeline, AI-power end-node). The one narrative-named vehicle that worked (S-Oil) had already been
confirmed by OBV 매집 + 기관 실매수 before it was named.** Meanwhile **the two propositions that were
RIGHT (로봇, 전력기기) were the two the desk never vehicled at all**, and both were filed at the lowest
confidence on the sheet.

**★ NEW failure class #4 — *narrative-sourced vehicles*: a vehicle named because the story implies it
should benefit is worse than no vehicle at all, because it converts a correct macro read into a measured
loss.** **Rule folded into the standing watch: a proposition may name a vehicle ONLY when that name already
carries a flow confirmation in §2 (OBV 매집 or 기관 실매수 or a foreign net-buy flip). Otherwise it names
the AXIS and explicitly says "un-vehicled — SWEEP must find one."** M-03 and M-04 above are written to
that rule for the first time.

### Standing failure classes — status this run
- **#1 (banking a one-sided read of an oscillating variable): CONTAINED.** M-02's bracket paid at +7d,
  through a branch (홍해, not 호르무즈) the proposition did not anticipate — which is the whole point of
  bracketing rather than forecasting.
- **#2 (narrative–flow inversion → the flow sets the tilt): TESTED A THIRD TIME, AND SYMMETRICALLY.**
  07-20 story-down/flow-up → flow won. 07-21 story returned to the flow → flow won. **07-22 the story left
  again (bucket 4 −28.2%) while the price ran (+8.04% 5d) — the rule says hold ENRG, and it is held.**
  ⚠ **But this run it must be applied with a measurement caveat: part of that −28.2% is a trigram blindness,
  not attention loss.** Assigned to DEEP-ENRG.
- **#3 (watching the negotiation, missing the calendar): APPLIED, not just recorded.** M-06 now carries
  both instruments with separate dates, per the rule written on 07-21.
- **#4 (narrative-sourced vehicles): ★OPENED THIS RUN** — see above.
- **★ Tooling-trap class (2 runs running): `module_flow` produced silently-wrong output twice.**
  07-21: bare 6-digit tickers → empty rows (fails loud enough to notice). **07-22: benchmark missing a bar
  → plausible, uniformly-flattering RS (fails silently and in the direction of taking risk).**
  **The second is strictly more dangerous.** Standing rule added: **whenever RS moves in the same direction
  for >80% of the board in one session, verify the benchmark series before believing it.**

---

## ✅ EXIT CHECK
- [x] **Catalysts injected** — `catalyst_calendar --days 5` → `llm_outputs/2026-07-22/CATALYST_WATCH.json`.
      ⚠ Module missed the KR binary for a **3rd consecutive run**, on the day it fires (방미 D-0) — manually
      injected in §0 along with the 알파벳 and 홍해 binaries. 6 binaries, all bracketed both ways in §4a.
- [x] **Events read via `--body 2`, tail count = 0** — 710 → 347 → 102 → **72 market, head 5 / body 67, ALL 72
      read** (stdout truncated the body at ~30 with `… 외 37개`; the remainder read from
      `out/news_brief/2026-07-22_domestic.json`). **The partial-day denominator is stated up front so no
      count delta is read as a signal.** Nonmarket bucket checked (5-of-30 sample) — no misfiled market item
      found this run, unlike 07-20/07-21.
- [x] **Trajectories read** (`thread --days 7`) — every §4a proposition carries its thread tag + curve.
      **Window-end inflation flagged at its strongest yet (102 events after 517) and applied to FOUR threads
      individually**, not waved at. **ENDED-under-open-proposition staleness flags raised for M-01 (BOK, 3rd
      run — now with an escalating counter-thread), 매도 사이드카/레버리지 보완책, 원화국제화 (2nd run
      dormant), and 한화 필리조선소 (the 조선 leg's last positive thread).**
- [x] **Every "quiet"/"declining" claim carries its denominator (P4)** — the pool is **18,731 (−9.0%)** and
      every bucket is scored against that bar, not against zero. **Bucket 4's −28.2% is explicitly NOT
      concluded as attention loss** because the trigram blindness is an untested alternative explanation.
- [x] **No 0/near-0 bucket trusted.** All 7 passed as **separate argv**, 3+ char forms only.
      ★ **New trigram-trap entry found and verified this run: `홍해`·`후티`·`예멘반군`·`선박보호`·`홍해봉쇄`
      = 0 each; only `해상봉쇄` (30) works** — the KR term index is structurally blind to the run's newest
      supply axis, which the event axis carried at 5 outlets in the head tier.
      **Coverage run with a non-zero denominator (18,731) → 🔴 심각 / recall 37.6%** — the 🔴 is real, not the
      0-denominator-prints-🟢 artifact.
- [x] **Transmission matrix produced** — all 11 GICS sectors, one line each, Δ vs 07-21 + driving prop;
      **8 divergences named with owners in §4x**, including a forced disposition on the 3-run-old ADR item.
- [x] **MACRO_REPORT.md written** with primary numbers explicit (`[FRED]` pulled directly, asof dates +
      staleness flags on DXY/CPI/M2 + "US rates are 2 sessions behind the KR tape"), **self-backtest appended
      at the protocol's +7d horizon**, and **8 new blind-spot terms folded into the living term table**.
- [x] **★★ Tooling trap recorded and CORRECTED IN-REPORT (§2): `^KS11` is missing its 2026-07-21 bar in
      yfinance while every constituent has it, so `module_flow`'s bar-count RS20 is inflated 5–11pp
      board-wide.** All 16 RS20 figures were re-derived date-aligned and §4 uses the corrected column.
      **Uncorrected, this run would have upgraded IT, DISC, 조선 and UTIL simultaneously on a data hole.**
      Escalated to SWEEP as §4x(a), first action.
- [x] **★ Partial-session caveat honoured** — 서지 column dropped entirely (32 minutes of session), and no
      §4 tilt moves on today's +5.93% price action alone.

**News source = server DB via NEWS API (`/exec` routed), not local fallback.**
**Flow source = `module_flow` — KIS per-investor actuals + KRX short interest — with RS20 hand-corrected.**
**Macro source = `module_macro_us --json` [FRED] direct (no same-day US desk run to cross-read).**

**→ proceed to SWEEP.**
