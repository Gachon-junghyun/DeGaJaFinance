# MACRO_REPORT — industry_KR · 2026-07-21 (Tue)

> Stage 1 / L1·MACRO. Runtime `--market kr`, English instructions / KR-market output.
> Primary data: **same-day US `MACRO_REPORT` EXISTS** (`llm_outputs/2026-07-21/industry_US/`) →
> §1 cross-reads its §1 primaries, cited `[FRED via US-desk]` with the US desk's own asof dates.
> News = `module_news_data` via NEWS API `http://127.0.0.1:8787` (routed `/exec`) — event axis
> (`brief --body 2 --scope domestic`) + trajectory (`thread --days 7`) + 7-bucket + coverage + blindspot.
> KR edge axis = `module_flow` KIS per-investor actuals + KRX short interest.
> Continuity anchor: `llm_outputs/2026-07-20/industry_KR/MACRO_REPORT.md`.
> Handoff ledger: `DEGAJA_REPORT_DIR=llm_outputs module_report_tags show` — 243 reports / 333 tickers /
> 15 sectors, updated 2026-07-21T11:10. Inherited KR coverage read (000660, 010950, 009150).
> Deliverable = the **§4 transmission matrix** (ROTATION's input). Zero buy/sell calls.

---

## ⚠⚠ THE CAVEAT THAT INVERTS FROM LAST RUN — and it inverts in *our* favour, which is the dangerous direction

**The 07-20 report was written on a 145-article partial pre-open Monday.** Its head tier was **0 events**
and it said so. **This run is the opposite: a complete, and in fact the largest, session of the window.**

| | 07-20 (prior run) | **07-21 (this run)** |
|---|---|---|
| Articles → clusters → events | 788 → 360 → 145 | **3,770 → 1,113 → 612** |
| Market / nonmarket | 72 / 73 | **369 / 243** |
| Tiers (head ≥5s / body ≥2s / tail) | 0 / 72 / 0 | **42 / 327 / 0** |

**Consequence, stated before any proposition:** last run's report carried "head = 0" as a collection
artifact. This run has a **42-event head** and a 3,770-article denominator. **Every cross-run count
delta below is contaminated by that ~2.6× pool jump** (the 7-day pool went 18,400 → **20,578**, +11.8%).
**No tilt in §4 rests on a raw count that merely rose 5–12%** — only on counts that moved *against* the
pool, and on the flow tape, which is pool-independent.

**And the tape reversed hard:** **KOSPI 6,747.95 (+3.56%)**, **삼성전자 +6%대**, 코스닥 753.34 (+0.49%),
**원·달러 1,473.4원 (−5.0원)**. **A desk that downgraded IT to Neutral yesterday is now being invited to
buy the bounce it just called weak-hands.** §4a P-M04 handles that invitation with a volume-qualified
gate rather than a mood change.

---

## §0 Catalyst injection (`catalyst_calendar --days 5` → `llm_outputs/2026-07-21/CATALYST_WATCH.json`)

**6 binaries in the module's window; the KR-native one is again missing and is injected manually.**

| When | Event | Axis | Note |
|---|---|---|---|
| **Undated / LIVE** | **Iran "Strait of Hormuz open" (TACO trigger)** | oil | 🔀 binary, open-ended. ★ The US desk has this **upgraded to a concrete 10-day ceasefire proposal, so far rejected** — read the KR oil leg against a *document*, not a hypothetical |
| **D-1 · 07-22 → 07-24** | ★ **김정관 산업장관 방미 — 러트닉 회담, 대미투자 1호 + 조선 + 쿠팡** | trade/policy | 🔀 **binary, D-1.** Still not in the calendar module; re-injected from body-read (fts: 45 hits/3d, mk·sedaily·donga·yonhap·mt) |
| **Undated, BUILDING** | ★ **NEW — '글로벌 관세 10%' 만료 → 트럼프 '301조 관세' 부과 초읽기** [49a/4s, thread 2→4] | trade | 🔀 binary. **A second, separate trade axis from 방미** — it is a US *statutory* action, not a negotiation |
| D-0 · 07-21 | SCHW earnings (US FIN read-through) | earnings | 🔀 prints after this stage's cutoff |
| D-1 · 07-22 | **TSLA · KMI** earnings | earnings | 🔀 |
| D-1 · 07-22 | **알파벳 실적** (AI-capex read-through) | AI-capex | 🔀 → M-03 both-sides |
| D-2 · 07-23 | **RTX · LMT** earnings (KR 방산 read-through) | earnings | 🔀 |

★ **Second consecutive run in which `catalyst_calendar` missed the week's dominant KR binary.** Filed.

---

## §1 Regime read — primary numbers explicit

### ★ The hard KR print of the day, and its anti-print, which sat one tier down

- **[13a/8s] 7월 1~20일 수출 549억 달러 — 역대 최대, +52.3% YoY, 일평균 +62.9%.
  반도체 +180.6%, 반도체 수출 221억 달러 역대 최대 재경신** [yonhap 1보/종합 · mt 속보 · chosun · donga · asiae].
- ⚠ **The anti-print is real, and it is in the body, not the head:**
  **"7월 수출 뜨겁지만 … 반도체 수출 전월 대비 13% 줄어"** [mk] · **"6월 고점서 숨고르기"** [sedaily].
  **The YoY is a record; the MoM is negative.** Any proposition citing "역대 최대" without the −13% MoM
  is quoting half a print. Both are carried in M-04.

### ★ KR-native regime spine (inherited): BOK **2.75%**, hiking bias — and today the *liability* side repriced

The 07-20 report carried M-01 as an asset-side story (코픽스 3%·주담대 8% → NIM). **Today the other side
of the balance sheet moved, loudly, and it is the first genuine two-sided input this proposition has had:**
- **[6a/5s] 은행 예·적금 금리 잇달아 인상 — 보름 만에 16조 유입(종합)** [yonhap]
- **신한은행 예·적금 금리 최고 +0.4%p 인상 "시장금리 반영"** [yonhap] · **"3%대 중반 정기예금 등장"** [mk]
- **"기준금리 인상 기조에… 저축銀 수신경쟁 데자뷔 — 1년 만기 예금금리 4%"** [mt]
- 울산시 금고 경남·농협은행 예금금리 상향 [yonhap/asiae]
**Funding cost is repricing upward at the same time as lending yield.** This does not refute M-01 — the
banks' flow says otherwise (§2) — but it is the mechanism by which M-01 would break, and it is now live.

### Cross-read of US primaries [**FRED via US-desk**, `llm_outputs/2026-07-21/industry_US/MACRO_REPORT.md` §1]
| Series | Latest | asof | Read-through to KR |
|---|---|---|---|
| Fed funds | **3.63%** | 07-17 | Unchanged. US on hold vs **BOK hiking** — the gap keeps narrowing |
| US 10Y | **4.55%** | 07-17 | **−2bp** vs the 07-19 US run. Long end eased |
| US 2Y | **4.18%** | 07-17 | **+2bp** — front end still rising |
| **2s10s** | **+37bp** | 07-17 | ★ **Bear-flattening accelerated: 42 → 41 → 37.** The US desk's own FIN thesis is weakening on this |
| Real 10Y | **2.31%** | 07-17 | **−4bp** — the KR long-duration/RE cost driver eased *slightly* |
| Core CPI / CPI | 336.065 / 332.568 | **Jun** | ⚠ ~1-month lag. Not a live read |
| Unemployment | 4.2% | **Jun** | ⚠ 1-month lag |
| **DXY** | **120.53** | **07-17** | ⚠ 2 sessions stale; rose into the escalation. **Cannot speak to today's 1,473원** |
| VIX | 18.77 (FRED 07-17) | 07-17 | live **^VIX 17.52 (07-21, −6.06%)** — risk-off came off |
| M2 | $23,052B | **May** | Liquidity expanding, lagging |

⚠ **Every US rate print above is 2 sessions behind the KR tape.** A KOSPI +3.56% day and a −5원 won move
are **not** in the 2s10s figure.

### ★ The KRW — and it moved the right way for the first time this month
- **원·달러 1,473.4원 (−5.0원, 15:30)** [32a/6s, 뉴스1] · yfinance `KRW=X` **1,475.28, −0.81% 1d, −1.50% 5d, −3.66% 1m**.
- Week path: **1,493 (07-14) → 1,484.7 → 1,480s → 1,487.28 (07-20) → 1,473.4 (07-21)**.
- ⚠ **Two-sided, immediately:** **[16a/6s] "Dollar near one-week high as markets grapple with Gulf tensions"**
  and **[2a/2s] 미·이란 충돌 격화에 달러 '유사시 매수' 폭발… 엔·달러 162엔대** — the won firmed on a
  **record semiconductor export print**, into a **strengthening dollar**. That is an export-driven, not a
  dollar-driven, move, and it is therefore hostage to the same MoM −13% that §1 just flagged.

### The tape [asof 2026-07-21 close]
| | Last | 1d | 5d | 1m |
|---|---|---|---|---|
| **^KS11** | **6,747.95** | **+3.56%** | −0.87% | **−25.97%** |
| ^KQ11 | 753.34 | +0.49% | −5.76% | −22.21% |
| KRW=X | 1,475.28 | −0.81% | −1.50% | −3.66% |
| CL=F | 82.34 | **−1.07%** | +3.78% | +10.05% |
| BZ=F | 88.94 | −0.31% | +4.97% | **+14.17%** |
| ^VIX | 17.52 | −6.06% | +6.18% | +1.39% |

**Net regime: KR is still tightening-into-de-rating (−25.97% in a month is the number that matters), but
the de-rating took its first real breath — powered by an export print, not by a policy change.**
**[8a/6s] JP모건 "코스피 급락 키운 건 레버리지 ETF… 목표 1만2500 유지"** frames the crash as
*structural/leverage*, not fundamental. **[2a/2s] "코스피 6000이 바닥"** is the same argument at the tail.
This desk records both as *claims*, not observations — the observation is −25.97%/1m and +3.56%/1d.

---

## §2 Positioning — ★ the KR edge axis (`module_flow`, KIS per-investor actuals, 20d, bench `^KS11`)

⚠ **TOOLING TRAP CAUGHT — record it, because it would have silently emptied this entire section.**
**Bare 6-digit KR tickers (`005930`) returned `?` / `(empty)` rows for all 8 names today** — yfinance
404s them ("possibly delisted") and the module prints an empty table **without failing**. The `.KS`
suffix works. A stage that read that output as data would have concluded "no flow signal" on a day the
flow *inverted*. **All rows below were re-run as `NNNNNN.KS`.**

| Ticker | Name | 흐름 | OBV | RS20 | RS60 | 서지 | 외/기/개 (만주, 20d) | Verdict |
|---|---|---|---|---|---|---|---|---|
| 105560.KS | **KB금융** | 🟢가속 | **매집** | **+36.8%** | +2.9% | 1.07x | −286.1 / **+382.0** / −91.3 | ✅ **real-hands** |
| 055550.KS | **신한지주** | 🟢가속 | **매집** | **+33.3%** | −0.7% | 0.89x | −167.0 / **+286.6** / −70.0 | ✅ **real-hands** |
| **086790.KS** | **하나금융** ★new | **🟢가속** | **매집** | **+36.7%** | +2.2% | **1.16x** | −68.2 / **+145.4** / −71.7 | ✅ **real-hands, 외국인 5일 매수전환↑** |
| 010950.KS | **S-Oil** | 🟢가속 | **매집** | **+58.3%** ★top | **+18.3%** | **1.14x** | −9.4 / **+186.8** / −184.5 | ✅ real-hands (⚠ 외국인 flipped slightly negative vs 07-20's +12.6) |
| 207940.KS | **삼성바이오로직스** | **🟢가속** ▲ | **매집** ▲ | **+33.7%** ▲ | −17.8% ▲ | 0.74x | **+8.7 / +5.1** / −13.7 | ✅ **both sides buying; upgraded from 🟡중립** |
| 068270.KS | **셀트리온** ★new | 🟡중립 | 중립 | **+27.8%** | −16.9% | 0.80x | **+26.3 / +123.0** / −208.0 | ✅ quiet real-hands |
| 015760.KS | **한국전력** ★new | 🟡중립 | 중립 | **+14.6%** | −32.4% | 0.76x | −58.2 / **+221.3** / −168.2 | ✅ 기관 실매수, 외국인 5일 매수전환↑ |
| 005490.KS | POSCO홀딩스 | 🟡중립 | **분산** | +13.4% ▲ | **−33.7%** ▼ | **0.68x** | +31.7 / **−31.7** / +0.2 | ⚠ **no money — 서지 0.68x for a 2nd run** |
| **005930.KS** | **삼성전자** | **🟡중립** ▲ | **중립** ▲ | **−0.8%** ▲▲ | +12.6% | 0.89x | **−4,238.6** / +397.3 / **+3,765.3** | ⚠ **still weak-hands on 20d — but 외국인 5일 매수전환↑** |
| **000660.KS** | **SK하이닉스** | **🔴분산** | 분산 | **−11.1%** ▼ | +44.4% | 1.10x | **−815.7** / −171.6 / **+958.9** | ❌ **weak-hands; RS20 DETERIORATED** — 외국인 5일 매수전환↑ |
| 034020.KS | **두산에너빌리티** | 🔴분산 | 분산 | −3.1% | **−47.9%** ★worst ▼ | 0.85x | **+52.3 / +60.7** / −103.0 | ⚠ **inverted: both institutions now net-BUYING the worst RS60 on the board** |
| **042660.KS** | **한화오션** ★new | **🔴분산** | 분산 | −3.7% | **−43.2%** | 0.91x | **−425.1** / −74.4 / **+493.6** | ❌ **weak-hands + 공매도 1.44% building(+0.17) ⚠주목** |
| 012450.KS | **한화에어로** ★new | 🟡중립 | 분산 | +5.9% | **−41.0%** | 1.06x | −3.9 / +16.7 / −12.7 | ⚠ thesis-alive / RS gone |
| 009540.KS | HD한국조선해양 ★new | 🟡중립 | 분산 | +11.0% | −26.6% | 0.93x | −9.7 / +13.9 / −4.5 | ⚠ 공매도 building(+0.09) |
| 005380.KS | **현대차** ★new | **🔴분산** | 분산 | −5.4% | −32.6% | **0.59x** | −30.1 / +25.9 / +6.8 | ❌ weak-hands · **공매도 1.99% ⚠주목, covering(−0.51)** |
| 051910.KS | LG화학 ★new | 🟡중립 | 분산 | +3.5% | **−41.3%** | 0.67x | +22.6 / −41.6 / +18.5 | ⚠ 혼조, no money |

★ **The four things this table decides, in order of how much they change the prior run:**

1. **THE BANK LEG IS NOW A TRIPLE, AND IT IS THE ONLY UNAMBIGUOUS SIGNAL ON THE BOARD.**
   KB **+36.8%**, 하나 **+36.7%**, 신한 **+33.3%** RS20 — **all three OBV 매집, all three 기관 실매수**,
   하나 with **서지 1.16x** and a **5-day foreign buy-flip**. Against a benchmark **−25.97%/1m**. This is
   the third consecutive run in which FIN is confirmed on *flow*, not on the (ENDED) hike headline.

2. **THE MEMORY GATE MOVED — PARTIALLY, AND ASYMMETRICALLY.** 삼성전자 went **🔴분산 → 🟡중립**, OBV
   **분산 → 중립**, **RS20 −4.9% → −0.8%**, and **both memory names printed `외국인5일 매수전환↑`.**
   **That is the exact KPI M-04 named yesterday ("foreign net-buy sign flip"), firing on the 5-day window.**
   ⚠ **But the 20-day disqualifier is intact and 하이닉스 got worse, not better:** 삼전 외국인 **−4,238만**
   vs 개인 **+3,765만**; 하이닉스 **−815만 / +958만** and **RS20 −6.6% → −11.1%**. **삼전's +6% day came on
   서지 0.89× — below-average volume.** **One name improved on light volume while its twin deteriorated.
   That is not a gate opening; it is a gate rattling.** Volume-qualified condition in M-04.

3. **THE 조선 LEG IS BEING SHORTED INTO ITS OWN BINARY — the run's sharpest new fact.**
   **한화오션 공매도 1.44% of float, building (+0.17), ⚠주목**, with 외국인 **−425만** and 개인 **+493만**
   absorbing; HD한국조선해양 short also **building (+0.09)**. **The 방미/조선 catalyst is D-1 and the
   measured money is positioned against it.** Yesterday's report carried 조선 as INDU's *catalyst-backed*
   leg. It still has the catalyst. **It now also has an identified short building into it.** Both branches.

4. **두산에너빌리티 INVERTED and it is the one row I cannot resolve.** RS60 fell further to **−47.9%**
   (board-worst) and OBV is still 분산 — **yet 외국인 +52.3만 AND 기관 +60.7만 are now both net buyers on
   20d, with 개인 −103.0만 distributing.** That is the *opposite* pattern from the memory names. Either
   institutions are early into an AI-power capitulation, or this is a dead-cat accumulation into a
   −47.9% RS60. **Named, not resolved — assigned to DEEP in §4x.**

### Short interest (KRX actuals) — the one column that changed character this run
| Name | %float | Direction | Read |
|---|---|---|---|
| **현대차** | **1.99%** ⚠주목 | **covering (−0.51)** | ★ The board's most crowded short, **actively covering** — squeeze fuel against a 목표가↓ tape |
| **한화오션** | **1.44%** ⚠주목 | **building (+0.17)** | ★ Shorts pressing **into** the 07-22~24 binary |
| S-Oil | 0.49% | building (+0.04) | At the 주목 threshold; building into the board's best RS |
| 삼바 | 0.40% | flat | — |
| 두산에너빌리티 | 0.27% | building (+0.03) | Consistent with 분산 |
| HD한국조선해양 | 0.27% | building (+0.09) | Same direction as 한화오션 |
| 하나금융 | 0.18% | building (+0.09) | ⚠ small, but the only FIN name with a building short |
| 삼전 / 하이닉스 | 0.01% / 0.01% | flat / **covering** | Effectively unshorted — **the memory selloff was cash selling, not shorting** |

⚠ **The memory names carry ~zero short interest.** That matters for M-04: **there is no squeeze fuel under
삼전/하이닉스.** A +6% day with no shorts to cover and below-average volume is buyers, not mechanics —
which is *better* news than a squeeze, and *weaker* news than a squeeze in terms of durability.

### US COT cross-read [via US desk; Tue-close +3–4d lag ⇒ context, not trigger]
⚠ **The US desk reports this table is byte-identical to its 07-19 run — no new CFTC release.**
**It therefore carries zero new information this run and is not permitted to move anything.**
WTI **10%ile** 🔴crowded-short · Nat Gas **6%ile** 🔴 · Nasdaq-100 **4%ile** 🔴 · Copper **95%ile** 🟢overheated.

---

## §3 Narrative

### §3a Event axis — the day, all of it [`brief --body 2 --scope domestic`]
**Denominator: 3,770 articles → 1,113 clusters → 612 events (2src+) → 369 market / 243 nonmarket.
Tiers: head 42 · body 327 · tail 0. All 369 market events read** — the terminal view prints ~30 body rows
with `… 외 297개`; **the remaining 297 were read from `out/news_brief/2026-07-21_domestic.json`.**
**A stage reading only stdout would have been ~80% blind even with `--body 2`.**

**★ Trade — the loudest axis on the KR feed today, and it is not the one we were watching:**
- **[66a/20s, the day's max-dispersion event] 트럼프, 최우방 캐나다에 50% '추가 관세' — 관세법 338조 첫 적용**
  ← the KR feed carried a **US** event at **20 outlets**. Our M-06 was written about *Korea's* negotiation.
- **[49a/4s] '글로벌 관세 10%' 곧 만료…트럼프 '301조 관세' 부과 초읽기** [연합뉴스TV] — thread **BUILDING 2→4**
  (07-20 [15a/2s] 美 10% 임시관세 종료…韓, 301조 관세 덮친다). ★ **A statutory US action aimed at Korea,
  building for two days, and this desk had no term for it.**
- [yonhap/mt] **트럼프, '美에 공장 건설' 조건부로 알루미늄 관세 절반 인하** — 러트닉 named. The
  build-in-America carrot beside the 301조 stick.
- 방미 binary (fts, 45 hits/3d): *"발표만 남은 대미투자 1호… 이번주 막판 조율"* [mt] · *"김정관 이번주
  방미…대미투자 속도전에 '쿠팡'이 변수"* [sedaily] · *"한미, 이번 주 연쇄 고위급 협상…쿠팡 의제 촉각"* [mk].

**★ Semis — the day's engine, with its own brake attached:**
- **[40a/7s] 반도체 수출 훈풍에 코스피 6700선 회복…삼성전자 6%대 급등** · **[13a/8s] 수출 549억달러 역대 최대**
- **[10a/3s] 반도체주 전망은 '극과 극'…"피크아웃 vs 2차 랠리"** ← the split, named by the press itself
- [4a/2s] **모건스탠리 "메모리 주가 약세는 진입 기회 제공"** · [5a/3s] 삼성·SK하이닉스 **CXL 양산 경쟁**
- **[2a/2s] 삼성전자, 2030년까지 신규 팹 4곳 구축…용인·평택·호남 전방위 투자** ← ₩-scale capex at **2 outlets**
- **[7a/5s] 노조가 반도체 공장 입지까지 정하나… '호남 프로젝트' 교섭 범위 논란** ← siting/labor risk on that capex
- [5a/4s] **TSMC도 증설 경쟁… 美투자 1000억달러 늘려** · [3a/3s] 글로벌 반도체 장비 시장 2028년 339조원
- [5a/3s] 과기정통부, 김기남 고문과 **'K-문샷' 반도체 미션** 논의
- **↔ anti:** [mk] **반도체 수출 전월 대비 −13%** · [sedaily] **6월 고점서 숨고르기** · [3a/2s] 삼전·SK하닉
  급락 후 반등 시도 · [4a/3s] **대만, TSMC 前직원 기밀유출 기소** (+[2a/2s] 징역 7년 구형)

**★ AI / capex doubt — M-03's kill-switch, still firing, now with a China vector:**
- **[7a/5s] 딥시크·키미 급성장에 긴장했나…美, 반도체 이어 중국산 AI 차단 검토**
- [5a/5s] **Chinese AI sensation Moonshot's gamble on big models pays off** · [2a/2s] "**키미 쇼크**" 문샷
  창업자 양즈린 · [3a/2s] [시시비비] 키미 K3이 보여준 위기감 · [3a/3s] China's AI models have Trump's AI world at war
- [6a/5s] **Nebius −40% from ATH** · [3a/3s] **Iren shares jump 16% as $2.8B AI cloud deals**
- **↔ pro (domestic-policy leg, intact):** **[26a/8s] AI가 만드는 미래경제…재경부, 에이전트 커머스·피지컬 AI
  전략 논의** (thread **BUILDING 8→7→7→6→2→8→8, 124건**) · [3a/2s] 삼성SDS 국산 NPU(퓨리오사) AI 클라우드 ·
  [3a/2s] **블랙록, 데이터센터 건설 위해 18조원 채권 발행 계획**
- **[17a/8s] 삼성전자, 로봇사업 추진 본격화 — 대표 직속 RX사업추진실 신설** ← ★ new axis, 8 outlets, no bucket saw it

**★ Oil — the thread REVERSED from FADING to BUILDING, exactly where the money already was:**
- **[19a/7s] 호르무즈 이어 홍해 봉쇄 위협에 다시 치솟는 유가…석유 최고가격제 유지 불가피**
  (thread **BUILDING 3→4→3→6→7**, 07-20 브렌트 90달러 재돌파)
- **[9a/2s] 사우디, 후티 해상봉쇄 맞서 홍해 지나는 선박 보호조치 착수** ← the KR-side confirmation of the
  US desk's "Houthi maritime embargo" vector — **a supply threat that does not run through Hormuz**
- **[20a/6s] 이란 대통령 "미국과 전면전 치르는 중"** (미-이란 thread **BUILDING 5→4→3→2→6→5→6**, 123건)
- ⚠ **In the *nonmarket* bucket at 9 outlets: "Goldman Sachs says crude prices could cross $120 if Strait
  of Hormuz disruptions continue"** and **"Iran war: US launches fresh strikes"** — **two 9-outlet,
  unambiguously market-moving items misfiled as nonmarket.** Second consecutive run with this exact
  classifier failure (LOSO 10–14%). **The nonmarket bucket must be read, not trusted.**
- **↔ anti:** **CL=F −1.07% on the day** · [2a/2s] 호르무즈發 고유가 충격 — 라이언에어 순이익 −34%
  (the oil→consumer transmission, priced) · [6a/2s] 금 선물 $4,000 돌파 · US desk's **live 10-day ceasefire proposal**

**★ Financials — the liability side repriced (see §1) plus structure:**
- [6a/5s] 예·적금 금리 인상, **보름 만에 16조 유입** · [mt] 저축銀 **4%** 수신경쟁 · [mk] 3%대 중반 정기예금
- [15a/5s] 우리은행–태광산업 상생금융 · **[12a/4s] 카카오뱅크 노조 31일 전일 파업** (임금교섭 결렬)
- **[3a/2s] 광주상의 "JB·BNK금융 합병 논의 우려"** ← ★ regional-bank M&A chatter, 2 outlets
- [16a/4s] 상반기 증권결제대금 4,701조, 주식 결제대금 **+314.5%** · [5a/4s] ELS·ELB 27.8조 **+27.7%**
- [2a/2s] 역대급 실적 전망에도 **고점서 −40% 하락한 증권주** · [8a/6s] **JP모건: 급락 주범은 레버리지 ETF, 목표 12,500 유지**

**Real estate / credit — supply push + demand throttle, simultaneously, again:**
- **[15a/6s] 李대통령 "부동산 세제, 국민 눈높이"…공급·실수요자 대책 예고** · [2a/2s] 서울 집값 1년새 **+13%**
  인데 **보금자리론 금리 인상** · [3a/3s] 경기도 부동산 교란 특별대책반 연말 연장
- **[5a/4s] "근저당 최대 10억"…대출 막히자 비은행 자금조달 확산** ← ★ the credit throttle pushing borrowers
  off-bank; 대출총량제 thread FADING **8→7→2→5→6**
- [2a/2s] 내년 서울 전세 '이중 공급 공백' · [2a/2s] 비싼 서울 대신 **경기 매수 4년 만에 최대**
- **건설 order-flow (separate from RE asset):** [11a/5s] 부천시–민간건설사 신뉴딜 협약 · [6a/4s] **여의도 10배
  군사시설보호구역 해제** · [3a/2s] LH 민간참여 최대 90% 보증 · [2a/2s] 광주 신가재개발 삼성물산 협의

**Health care — a second consecutive day of hard catalysts:**
- [8a/5s] 삼성바이오, **비만약 진출 — 2.7조 폴리펩타이드 인수** · [2a/2s] '마운자로 원료' 강자 품고 **281조
  비만약 시장** 도전 · **[4a/3s] 바이오헬스 수출 상반기 161억달러, 역대 반기 최대**
- [12a/6s] 신테카바이오 ADME·PK 모델 · [3a/3s] 셀트리온 트룩시마 북미 점유율 1위 4개월째
- **↔ anti:** **[12a/5s] 코오롱티슈진, 美3상 통계적 유의성 확보 실패 → 장초반 하한가** · [2a/2s] 알테오젠
  SC효소 '위협론' · [5a/3s] Novartis Q2 profit drops

**Industrials / defense · autos · materials · staples:**
- [22a/7s] **LIG D&A·LG AI연구원, AI 기반 지휘통제 체계 공동 개발** · [7a/5s] 한화에어로 **해외 공모채 5억달러**
  · [5a/4s] SNT모티브 K17 전력화 · [2a/2s] **KAI 판보로 에어쇼** 유럽 수출 마케팅
- **[7a/5s] KB증권 "현대차, 2분기 실적 기대치 밑돌 것…목표가↓"** · [2a/2s] "주주환원 외면하는 현대차" 거버넌스포럼
- **[15a/5s] 쿠팡 인천 화재에 물류·유통업계 비상** (thread FADING 6→5→5→5) + [8a/3s] 카드업계 홈플러스 대금 지급보류
- [2a/2s] **'저가 공세' 中 보고 있나… AI 올라탄 K철강 수출액 들썩** + [2a/2s] 철강·석화 'AI 특수' 노린다
  + [8a/4s] 석유화학 위기 속 **노사정** 맞손 + [2a/2s] 산업은행, 환영철강 지분 매각 착수
- [2a/2s] **다시 뛰는 나프타… 빗장 풀린 식품 가격 인상 '뇌관'** · [3a/3s] 정부, **전력감독원** 신설 추진
- [3a/2s] **블랙록, 에코프로 지분 5.01%(₩5,000억) 보유** · [2a/2s] **상법개정 1년 — 전문가 75% "코리아
  디스카운트 해소 기여"** · [2a/2s] 다이먼 "개인적으론 장기물 미국채·지수 매입 안 한다"

### §3b Trajectory axis [`thread --days 7 --scope domestic`]
**Per-day denominator: 07-15 494 · 07-16 484 · 07-17 247 · 07-18 239 · 07-19 342 · 07-20 730 · 07-21 612.**
3,148 daily events → 2,399 threads (440 multi-day, **185 alive**, 1,959 one-day incl. 415 new today).

⚠ **The window-end correction inverts from last run.** 07-20's window ended on a 145-article partial day
and **inflated FADING**. This window ends on **612 events after a 730-event Monday** — the two largest days
of the week — which **mechanically inflates BUILDING/REIGNITED**. Curves are read against that, not naively.

| Thread | Tag | Curve (outlets) | Read |
|---|---|---|---|
| **AI 정책/메가프로젝트** | **BUILDING** | 8→7→7→6→2→8→**8** · 124건 | The week's largest thread. **Domestic-policy AI leg, intact** — the split M-03 named holds |
| **코스피 사이드카/급등락** | **BUILDING** | 7→4→2→5→2→7→**7** · 151건 | Whipsaw regime itself is the story. nb=29.9, the highest on the board |
| **반도체 수출/삼전·하이닉스** | **BUILDING** | 7→6→7→6→**7** · 134건 | 07-15 삼전+6%/하닉+9% → 07-20 급락 → **07-21 삼전 +6% again.** ★ **A 3-cycle whipsaw, not a trend** |
| **호르무즈/유가** | **BUILDING** ▲ | 3→4→3→6→**7** · 46건 | ★★ **REVERSED from FADING (07-20) to BUILDING.** The narrative caught up to the S-Oil money |
| **미-이란 공습/중동전** | **BUILDING** ▲ | 5→4→3→2→6→5→**6** · 123건 | ★ Also re-tagged from FADING. **The 07-20 rule — "a FADING tag on a live physical driver is an attention gap" — was right for a third time** |
| **301조 관세 / 10% 만료** | **BUILDING** ★new | 2→**4** · 64건 | ★ **The new trade axis. Two days old, no bucket covered it** |
| **홈플러스 회생** | BUILDING | 5→4→7→**7** | 법원 회생폐지 취소, 가결기간 연장. Carries the 카드업계 대금 지급보류 leg |
| **제약·바이오 임상** | BUILDING | 6→4→2→4→**6** · 75건 | The HLTH catalyst engine, sustained |
| **한화 유증/에어로 해외채** | BUILDING | 4→**5** | 한화솔루션 유증 1.2조(계획의 절반) → 한화에어로 5억달러 |
| **AI위클리/국산 NPU** | FADING | 2→3→6→6→**12**→11→5 | Peaked at **12 outlets 07-19** — the week's highest single print. Now decaying |
| **코픽스 3%/대출문턱** | FADING | 7→6→4→5→7→**4** | M-01's transmission channel, 6 days sustained |
| **대출총량제** | FADING | 8→7→2→5→**6** | Re-spiked to 6 — **not fading**; the 비은행 자금조달 leg is new |
| **원·달러 환율** | FADING | 6→5→7→**6** | ⚠ Tag is a window artifact — the FX print is the day's [32a/6s] head item |
| **쿠팡 물류센터 화재** | FADING | 6→5→5→**5** | Steady 5 outlets. The M-06 contaminating variable, now with a physical event attached |
| **삼바 폴리펩타이드 인수** | FADING | 7→**5** | Still 5 outlets on day 2 |
| **TSMC 2Q 사상 최대** | FADING | 6→4→5→**4** | Attention decayed; capex did not (美투자 +1000억달러) |

**ENDED this window (163 threads; peak-8 items):** **한은 기준금리 2.75% 인상** (5→8→5) ·
**원화 국제화** (8→2) · **6월 취업자/고용률 3개월 연속 하락** (8→5) · **1인가구 머니무브** (8→2) ·
**코스피·코스닥 매도 사이드카** (7→6→5→3→7) · **최태원 "팔지 말라"** (4→7→3→3) ·
**한화 필리조선소 美 미사일시험 계측선 수주** (7→6→2) · **홈플러스 MBK-메리츠 2000억** (7→7) ·
**세메스 노조 출범** (7→2) · **포스코 협력사 상생** (5→7).

⚠ **Staleness flags on ENDED threads under still-open propositions:**
- **M-01 (BOK hike) — ENDED for a second run.** Re-justified again on §2 transmission evidence (3 banks
  accumulating), **not** on the headline. Now *also* carrying a live liability-side counter (§1).
- **M-02 (호르무즈 재봉쇄) ENDED — but its successor thread flipped to BUILDING.** The proposition's
  narrative engine, which yesterday I recorded as *lost*, is **back**. Recorded as a re-ignition, not as
  proof: the tag is inflated by a 612-event window end.
- **최태원 "팔지 말라" ENDED** — 5 days of damage control finished; §2 says the 20-day foreign exit did not.
- **원화 국제화 ENDED again** at 8→2 with no fresh print today. Downgraded from "live slow-burn" to dormant.

**BUILDING threads with no matching bucket → candidate new terms:** **301조 관세** · **홍해 봉쇄** ·
**로봇 RX사업추진실** · **예금금리/수신경쟁**.

### §3c Term axis — 7-bucket velocity [server `/exec` · domestic · 7d · OR + `--syn` + `--kr`, **terms as separate argv**]
| Rank | Bucket (argv verbatim) | 7d now | 07-20 | Δ | vs pool (+11.8%) |
|---|---|---|---|---|---|
| 1 | `반도체 메모리 인공지능 데이터센터 파운드리` | **5,275** | 4,963 | +6.3% | **underperformed the pool** |
| 2 | `부동산 가계대출 주택담보대출 총량규제 전세` | **1,671** | 1,596 | +4.7% | underperformed |
| 3 | `코스피 외국인순매수 공매도 레버리지ETF 신용융자` | **1,275** | 1,303 | **−2.1%** | ★ **fell in level** |
| 4 | `호르무즈 국제유가 이란 중동정세 원유` | **1,095** | 1,002 | +9.3% | ~pool |
| 5 | `금융위원회 상법개정 세제개편 규제완화 대미투자 관세협상 공정거래` | **477** | 425 | +12.2% | ~pool |
| 6 | `기준금리 통화정책 한국은행 코픽스 국고채` | **785** | 538 | **+45.9%** | ★★ **4× the pool — the only real term-axis signal** |
| 7 | `원달러 환율하락 환율상승 외환시장 원화가치 달러화 원화국제화` | **119** | 136 | **−12.5%** | ★ **fell hard** |

⚠ **All seven passed as separate argv, 3+ char forms only** (the 2-char trigram trap — 환율·외환·원화·
달러·상법·세제·관세 all return **0** = absence of INDEX — was verified on 07-20 and the corrected forms
carried forward unchanged, so these deltas are comparable).
**The honest reading: five of seven buckets moved with the pool and say nothing.** Two moved against it:
- **Bucket 6 +45.9% against a +11.8% pool** — and §1 and §3a say exactly what it is: **the deposit-rate
  repricing** (예·적금 인상 · 16조 유입 · 저축은행 4% · 코픽스). **A rate-axis signal that is NOT the hike
  headline (that thread ENDED) — it is the hike's second-order funding effect.** This is the run's single
  cleanest term-axis fact and it feeds M-01's *anti*-branch.
- **Buckets 3 and 7 fell in absolute level** on a 2.6×-larger day. **The 코스피 급락/레버리지 and 환율
  narratives are genuinely losing share** — consistent with a +3.56% index day and a −5원 won.

**Coverage check** [`coverage 기준금리 원달러 반도체 부동산 코스피 국제유가 인공지능 --days 7 --scope domestic`]:
pool **20,578건** (본문 보유 12,821 = 62.3%) · 현재 검색 2,284 · 본문 매칭 5,267 · **놓침 3,832** ·
**recall 37.3% → 🔴 심각, 본문 블라인드 62.7%.** **Non-zero denominator, so the 🔴 is real** (not the
0-denominator-prints-🟢 artifact). Recall is flat vs 07-20 (37.7% → 37.3%) — **my fixed term set still sees
~37% of relevant news; the blindspot pass is covering a 63% hole, and this run it caught 301조 관세.**

### §3d Blind-spot pass [`blindspot --sample-pct 35 --days 7 --scope domestic`, 20,578 pool / 7,202 sample, read RAW]
Token-0 emergent terms (07-20 in parentheses): `AI 847 · LG 125 · KT 101 · KB 70 · YTN 68 · **ADR 67 (75)** ·
BTS 61 · SSG 50 · MOU 35 · SK 36 · Chosunbiz 34 · **AX 32 (26)** · **TSMC 24 (—)** · **MBK 22 (24)** ·
**Vietnam 21 (17)** · LH 17 · SKT 17`.
- **`ADR` 67, holding rank against a +11.8% pool** — the SK하이닉스 US-listing venue thread persists.
  **This remains M-04's single best alternative explanation for the −815만주 foreign exit (venue
  substitution, not thesis exit), and it is STILL unresolved after two runs.** Re-assigned to SWEEP in §4x.
- **`AX` 26→32 and `TSMC` newly at 24** — AI-transformation as a KR corporate *spend* category, and TSMC
  as a KR-feed reference name (증설 경쟁 / 기밀유출 기소).
- **`MBK` 22** — holds; the 홈플러스 회생 thread (BUILDING 5→4→7→7) is its live expression.
- **`Vietnam` 17→21** — KR outbound manufacturing footprint, third run at the same low level. Watch-flag.
- ⚠ **`관세`/`301조` do NOT appear in the top-30 emergent terms despite a 49-article, 4-outlet, 2-day
  BUILDING thread.** **Identical structural failure to the US desk's Canada blind spot: a 7-day emergent-term
  window cannot see a 2-day regime event.** **The event axis caught it; the term axis could not.** Named.
- Raw sample rows worth the read: *"변동장서 빛바랜 액티브 ETF…10개 중 7개 비교지수 밑돌아"* [sedaily] —
  an active-management underperformance lane; *"AI 은행이라더니…카뱅 고액 송금 먹통"* [sedaily] — operational
  risk at the digital bank whose union strikes on the 31st; *"신축매입임대 초기사업비 조기 지원"* [yonhap ×2]
  — the LH supply-push leg again, from the blind pool.

**Living term-table additions this run:** `301조 관세/무역법338조` · `홍해봉쇄` · `예금금리/수신경쟁` ·
`로봇 RX사업추진실` · `신규팹 4곳(용인·평택·호남)` · `공장입지 노조교섭` · `CXL` · `전력감독원` ·
`비은행 자금조달/근저당`. (Carried: `ADR/원주 괴리`, `사모펀드/행동주의`, `AX`, `무인차량/방산수주`,
`경제질서/담합규제`, `법인 코인투자`, `네덜란드병/반도체 쏠림`, `칩플레이션`, `CXMT`, `AI capex 회의`.)

---

## §4 ★ SECTOR TRANSMISSION MATRIX — the deliverable (ROTATION's input)
> Wind direction only, one line per GICS sector. Δ = change vs 07-20. Not equal-weight analysis.
> **All flow tags asof the 2026-07-21 close. All US rate inputs asof 07-17 (2 sessions behind).**

| # | GICS Sector | Tilt | Δ vs 07-20 | Prop | One-line why (KR) |
|---|---|---|---|---|---|
| 1 | **Financials (FIN)** | **OW ★highest conviction** | = tilt, **↑evidence, ↑risk** | M-01 | **A triple now: KB RS20 +36.8%, 하나 +36.7% (서지 1.16x, 외국인 5일 매수전환), 신한 +33.3% — all 매집, all 기관 실매수**, vs a benchmark −25.97%/1m. ⚠ **NEW anti, and it is the mechanism: the liability side repriced** (예·적금 인상, **16조/보름**, 저축銀 4%, bucket-6 **+45.9%**). Plus 카뱅 파업 07-31, JB·BNK 합병 우려, 하나 short **building** |
| 2 | **Energy (ENRG)** | **tactical OW** | = tilt, **★narrative RESTORED** | M-02 | **S-Oil RS20 +58.3% board-best, RS60 +18.3%, 매집, 서지 1.14x, 기관 +186.8만.** ★ **The oil thread flipped FADING → BUILDING (3→4→3→6→7)** — 홍해 봉쇄 위협 [19a/7s] + 사우디 선박 보호 [9a/2s] + Goldman **$120** [9 outlets, misfiled nonmarket]. **Yesterday's flow-narrative divergence resolved in the flow's favour.** ⚠ Crude **−1.07% today**; US desk holds a live 10-day ceasefire proposal; S-Oil short **building at 0.49%** |
| 3 | **Health Care (HLTH)** | **OW** | ▲ **UP** from modest OW | M-07 | **삼바 upgraded 🟡→🟢가속, OBV 매집, RS20 +22.4%→+33.7%, 외국인·기관 동시 매수**; 셀트리온 RS20 +27.8%, 기관 +123만. **바이오헬스 수출 상반기 161억달러 역대 최대**; 비만약 281조 시장 진입. Bio thread BUILDING. ⚠ Anti is name-level and real: **코오롱티슈진 3상 실패 하한가** |
| 4 | **Information Tech (IT/반도체)** | **Neutral, flow-GATED (gate RATTLED, not open)** | = tilt, **★KPI partially fired** | M-04 | **The named KPI fired on the 5-day window: both memory names print `외국인5일 매수전환↑`, 삼전 🔴분산→🟡중립, RS20 −4.9%→−0.8%**, on a **record 반도체 수출 +180.6% / 221억달러** print. ⚠ **But: 20d foreign −4,238만 vs 개인 +3,765만 intact; 하이닉스 RS20 DETERIORATED −6.6%→−11.1%; 삼전's +6% came on 서지 0.89× (below average) with ~zero short interest (no squeeze fuel); and the export print's own MoM is −13%.** **Do not upgrade on a 1-session beta move** |
| 5 | **Industrials (INDU)** | **Neutral (split, ▼downgraded)** | ▼ from OW-split | M-03, M-06 | ★ **The 조선 leg is being shorted into its own D-1 binary: 한화오션 공매도 1.44% building(+0.17) ⚠주목, 외국인 −425만 / 개인 +493만; HD한국조선 short also building.** 방산 leg has events (LIG×LG AI 지휘통제 22a/7s, 한화에어로 5억달러 채권, KAI 판보로) but **no flow: 한화에어로 RS60 −41.0% 분산**. 건설 order-flow is the one positive (군사시설보호구역 해제, LH 90% 보증) |
| 6 | **Utilities (UTIL/원전)** | **UW (contested)** | = tilt, **flow INVERTED** | M-03 | **두산에너빌리티 RS60 −45.9% → −47.9% (board-worst), still 분산 — yet 외국인 +52.3만 AND 기관 +60.7만 both flipped to net-buying** while 개인 −103.0만 distributes. **The exact inverse of the memory pattern.** 한전 quietly accumulated (기관 +221.3만, 외국인 5일 전환). 전력감독원 신설. **UW held on price; the flow inversion is escalated to DEEP** |
| 7 | **Materials (MATR)** | **UW** | = | M-05 | **Third consecutive run where the narrative builds and the money refuses: POSCO 서지 0.68x (unchanged), RS60 −29.2% → −33.7%, 기관 −31.7만, OBV 분산** vs *"AI 올라탄 K철강 수출액 들썩"* [2a/2s ×2]. Plus **나프타 상승**, 석유화학 노사정 위기, LG화학 RS60 −41.3%, **Copper 95%ile crowded-long** |
| 8 | **Consumer Disc (DISC)** | **UW** | ▼ **DOWN** from Neutral | — | **현대차 🔴분산, RS60 −32.6%, 서지 0.59x (board-lowest), and a dated earnings cut: KB증권 "2분기 기대치 밑돌 것, 목표가↓" [7a/5s].** 쿠팡 인천 화재 [15a/5s] + 카드업계 홈플러스 대금 지급보류 = live distribution disruption. ⚠ **Counter, and it is mechanical: 현대차 short is 1.99% and COVERING (−0.51)** — squeeze risk against the downgrade |
| 9 | **Real Estate (RE)** | **UW (most rate-negative)** | = | M-01 | Hike + **보금자리론 금리 인상 into +13%/1yr 서울 집값** + 경기 특별대책반 연장 + **"근저당 최대 10억" 비은행 자금조달 확산** (the throttle pushing credit off-bank). ⚠ **Keep separating 건설 수주 from RE 자산** — 군사시설보호구역 해제·LH 90% 보증·부천 신뉴딜 are **INDU/건설 order-flow**, not RE-asset positives |
| 10 | **Consumer Staples (STPL)** | **UW** | ▼ from Neutral→UW | M-01 | **나프타 재상승 → "식품 가격 인상 뇌관"** [2a/2s] = cost-push into a throttled consumer; 커피 원두 수입 6년 최소(환율); 고물가 가성비 뷔페. No hiking-cycle relief, no fresh catalyst, and now an input-cost print |
| 11 | **Comm Services (COMM)** | **Neutral** | = | — | No distinct KR wind. Watch-flags only: 네이버 결제규모 쿠팡 턱밑 추격, 앤트로픽 저작권 2조 합의, **알파벳 실적 07-22** spillover |

**Net wind:** **the de-rating took a breath and every sector-level conclusion from 07-20 survived it, except
two.** FIN got a third name and its first real counter-mechanism. **ENRG's narrative came back to where its
money already was — the 07-20 divergence resolved in favour of the flow, which is a scored win for the flow
rule.** **IT's gate rattled without opening.** What *changed*: **INDU downgraded because the 조선 leg is
being shorted into its own catalyst**, and **DISC/STPL downgraded on dated, name-level evidence** (현대차
목표가↓ + 나프타 cost-push). What is **new and un-owned**: **301조 관세**, **홍해 봉쇄**, and **the deposit-rate
war** — none of which existed in yesterday's term table.

### §4x ★ Divergences ROTATION must resolve (named explicitly per the L1 rule)
- **(a) ★ NEW — 두산에너빌리티: matrix UW, flow INVERTED to institutional accumulation.** RS60 −47.9%
  (board-worst), OBV 분산, yet **외국인 +52.3만 AND 기관 +60.7만 both net-buying** with retail distributing.
  **Owner: DEEP.** Is this early positioning into an AI-power capitulation, or accumulation into a broken name?
- **(b) 조선 — dated catalyst (D-1) vs a building short at 1.44% ⚠주목.** 한화오션 외국인 −425만 / 개인 +493만.
  **Owner: PREMORTEM-equivalent within ROTATION (KR has no PREMORTEM block).** The 07-22~24 headlines settle it.
  **A one-way 조선 tilt into this binary is a protocol violation.**
- **(c) IT — the gate rattled: 5-day foreign flip + record export print vs 20-day weak-hands + 하이닉스 RS
  deterioration.** **Owner: SWEEP.** The specific test is in M-04's volume-qualified condition.
- **(d) ADR venue substitution — UNRESOLVED FOR TWO RUNS.** `ADR` 67 emergent hits. Does SK하이닉스's US
  listing explain the −815만주 domestic foreign exit? **Owner: SWEEP** (ADR–원주 괴리 + ADR volume vs domestic
  foreign net). ⚠ **07-20 assigned this to SWEEP and SWEEP did not take it. Escalated: resolve it or decline
  it in writing.**
- **(e) FIN — asset-side NIM vs liability-side repricing.** Bucket 6 **+45.9%** is the deposit war, not the
  hike. **Owner: DEEP-FIN.** Does 예대마진 still expand when 정기예금 hits 3%대 중반 and 저축銀 offers 4%?
- **(f) 현대차 — a downgrade into a covering 1.99% short.** Fundamental cut vs mechanical squeeze fuel.
  **Owner: ROTATION.**

---

### §4a Falsifiable propositions — both branches mandatory on every oscillating variable

- **M-01 — Hike transmission → bank NIM (CARRIED, flow-confirmed a 3rd time; ★ANTI-BRANCH NOW LIVE).**
  *BOK 2.75% + hiking bias → 코픽스 3%·주담대 8% → variable-rate repricing → NIM. **Flow: KB RS20 +36.8%,
  하나 +36.7% (서지 1.16x), 신한 +33.3% — all OBV 매집, all 기관 실매수, 하나 외국인 5일 매수전환**, against
  ^KS11 −25.97%/1m.*
  **Thread:** originating BOK thread **ENDED for a 2nd run** (5→8→5) → re-justified on transmission only.
  코픽스 thread FADING 7→6→4→5→7→4; **대출총량제 re-spiked to 6, not fading.**
  **★ Anti-signal (new, equal weight, and it is the mechanism not a mood):** **the liability side repriced
  today** — 예·적금 금리 잇달아 인상, **보름 만에 16조 유입** [6a/5s], 신한 **+0.4%p**, **3%대 중반 정기예금**,
  **저축銀 1년 4%** 수신경쟁. Bucket 6 **+45.9% vs a +11.8% pool** is this, not the hike. Plus **카카오뱅크
  노조 07-31 전일 파업**, **JB·BNK 합병 우려**, 하나금융 short **building (+0.09)**, and the standing
  **대출총량 1.5% cap** on the volume side.
  **Track KPI:** **예대금리차** (the new primary) · bank 2Q NIM prints (late July) · 연체율 · 가계대출 증가율
  vs the 1.5% cap · whether all three banks hold OBV 매집.
  **Kill-switch:** any of the three banks flipping to OBV 분산, **or** a 2Q NIM print that contracts QoQ
  despite the hike → M-01 is a funding-cost story, not a margin story, and FIN loses its top slot.

- **M-02 — Oil / Hormuz (★ THE 07-20 DIVERGENCE RESOLVED — in the flow's favour).**
  *Yesterday I wrote: "money is accumulating S-Oil while the story decays; one of the two is wrong."
  **Today the story turned: the 호르무즈/유가 thread flipped FADING (6→5→4→3) → BUILDING (3→4→3→6→7)**,
  on **홍해 봉쇄 위협** [19a/7s], **사우디 선박 보호조치** [9a/2s], 브렌트 90달러 재돌파, and **Goldman's
  "$120 if Hormuz disruptions continue"** [9 outlets — misfiled nonmarket]. Flow strengthened with it:
  **S-Oil RS20 +62.6%→+58.3% but RS60 +13.4%→+18.3%, 매집, 서지 1.14x, 기관 +186.8만.***
  ⚠ **A new independent supply vector, matching the US desk's:** the **Red Sea / Houthi** leg does **not**
  run through Hormuz — so a Hormuz-opening TACO does not close it.
  **Anti-branch (equal weight, and it got MORE concrete, not less):** **the US desk reports a live 10-day
  ceasefire proposal on the table, rejected so far by Khamenei** — the TACO trigger now has a *document*.
  **Crude fell today: CL=F −1.07%, BZ=F −0.31%.** WTI COT **10%ile crowded-short** is symmetric ammunition:
  a ceasefire removes the bid rather than squeezing anything. **S-Oil's own short is building at 0.49%.**
  **Track KPI:** BZ=F 88.94 · **홍해/사우디 선박 protection headlines (the non-Hormuz leg)** · S-Oil OBV +
  the 0.49% short direction · ceasefire-signature headlines.

- **M-03 — AI-power / DC capex (kill-switch STILL FIRING; the two legs have now visibly separated).**
  *07-16 named the kill-switch "AI capex 회의"; 07-20 recorded it firing in five prints. **Today it fired
  again with a China vector:** **美, 반도체 이어 중국산 AI 차단 검토** [7a/5s] · Moonshot/키미 K3 in **three
  independent prints** · **Nebius −40% from ATH** [6a/5s].*
  **★ The separation the 07-20 report demanded is now measurable:**
  - **Global-hyperscaler-capex leg: still breaking.** 두산 RS60 **−47.9%**, 한화에어로/조선 all RS60 −41~−43%.
  - **Domestic-policy AI leg: intact and it is the week's largest thread** — 재경부 에이전트 커머스·피지컬 AI
    [26a/8s], **BUILDING 8→7→7→6→2→8→8, 124건**; 삼성SDS 국산 NPU; **블랙록 DC 18조 채권**.
  **Anti-branch (pro-capex, equal weight):** **삼성전자 2030년까지 신규 팹 4곳** [2a/2s], TSMC 美투자
  +1,000억달러, 반도체 장비 시장 339조원/2028, **알파벳 실적 07-22 (D-1 binary)**.
  ⚠ **Un-tunneling note:** the domestic-policy leg's money has **not** been located — no KR name in §2
  expresses it. A thesis with no measurable vehicle is a term, not a tilt.
  **Track KPI:** **알파벳 07-22** · 두산 RS60 stabilization · whether 한전's 기관 +221만 persists · DART 단일공급계약.

- **M-04 — Memory supercycle (thesis OW / flow-gated. ★ THE GATE RATTLED — it did not open).**
  ***Pro, and it is the hardest print of the day:** **7/1~20 수출 549억달러 +52.3% 역대 최대, 반도체 +180.6%,
  반도체 수출 221억달러 역대 최대 재경신** [13a/8s]. **KOSPI +3.56% to 6,747.95, 삼성전자 +6%대.**
  **The KPI this desk named yesterday — "foreign net-buy sign flip on 삼전/하이닉스" — fired on the 5-day
  window: both print `외국인5일 매수전환↑`.** 삼전 **🔴분산 → 🟡중립**, OBV **분산 → 중립**, RS20 **−4.9% → −0.8%**.
  Corroborants: 모건스탠리 "메모리 약세는 진입 기회", CXL 양산 경쟁, 하이닉스 RS60 **+44.4%** still intact.*
  **Verdict: the gate is UPGRADED from CLOSED to RATTLED. IT stays Neutral. It is not promoted.**
  ⚠ **Why not — the falsification is low-quality and it is named as such, not smoothed over:**
  (1) **20-day weak-hands intact**: 삼전 외국인 **−4,238만** vs 개인 **+3,765만**; 하이닉스 **−815만 / +958만**.
  (2) **하이닉스 got WORSE, not better: RS20 −6.6% → −11.1%.** One name improved; its twin deteriorated.
  (3) **삼전's +6% came on 서지 0.89× — below-average volume**, on a day the whole index rose 3.56%.
  (4) **Short interest is ~0.01% on both — there is no squeeze fuel.** The move was cash buying, on light
      volume, on beta. (5) **The export print's own MoM is −13%** [mk] / "6월 고점서 숨고르기" [sedaily].
  (6) The 반도체 thread is a **3-cycle whipsaw** (07-15 +6/+9% → 07-20 급락 → 07-21 +6%), which the press
      itself frames as **"피크아웃 vs 2차 랠리"** [10a/3s].
  **★ Volume-qualified upgrade condition (so it cannot be re-fired by beta):**
  **삼전 AND 하이닉스 both print 20d foreign net-buying positive, AND 하이닉스 RS20 turns > −5%, AND at least
  one prints 서지 > 1.3× — for 3 consecutive sessions.** Then the gate is open and IT goes OW.
  **★ Kill condition (restores the UW):** 삼전 returns to OBV 분산 **on 서지 > 1.2×**, or the next 수출 print
  shows semiconductors down MoM a second time.
  **Unresolved for two runs:** the **ADR venue-substitution** alternative explanation (§4x d).
  **Track KPI:** 20d foreign net sign on both · 하이닉스 RS20 · 서지 · 8월 1~10일 수출 · **알파벳 07-22**.

- **M-05 — Materials / 철강 AI-DC (narrative-only, refuted by flow for a 3rd consecutive run → UW).**
  *Narrative persists: **"'저가 공세' 中 보고 있나… AI 올라탄 K철강 수출액 들썩"** + **"지금 주문해도 내년에…
  철강·석화 'AI 특수' 노린다"** [2a/2s each].*
  **Anti (dominant, and unchanged in three measurements): POSCO 서지 0.68× — identical to 07-20 — RS60
  −29.2% → −33.7%, OBV 분산, 기관 −31.7만.** Plus **나프타 재상승**, 석유화학 노사정 위기, LG화학 RS60 −41.3%,
  Copper **95%ile crowded-long**, 산업은행 환영철강 매각.
  ⚠ **This is the cleanest running instance of the narrative–flow inversion rule.** Three runs, the story
  builds, 서지 does not move off 0.68×. **Upgrade condition (unchanged): POSCO 서지 > 1.3× + 기관 순매수 flip.**

- **M-06 — 대미투자 / 관세 (★ D-1 BINARY, and it SPLIT INTO TWO AXES today).**
  *Axis 1 — **negotiation**: 김정관 산업장관 **07-22 출국 → 07-24 귀국**, 러트닉 회담. 대미투자 1호(에너지)
  "발표만 남음, 막판 조율", 조선, **쿠팡 변수** [45 hits/3d].
  ★ Axis 2 — **NEW, statutory, and unilateral**: **'글로벌 관세 10%' 만료 → 트럼프 '301조 관세' 부과 초읽기**
  [49a/4s, thread BUILDING 2→4, 64건], alongside **캐나다 50% 추가관세 (무역법 338조 첫 적용)** at **20 outlets**
  and **알루미늄 관세 절반 인하 — 단, 美 공장 건설 조건부**.*
  **★ Why the split matters: axis 1 is bilateral and can be won; axis 2 fires on a calendar regardless of
  what 김정관 agrees to.** A relief rally on a 1호 signature would not neutralize a 301 action.
  **Up-branch:** 1호 서명 + 쿠팡 의제 분리 → 수출주(조선·에너지·기자재) relief; **but 한화오션's 1.44%
  building short is positioned against exactly this** (§4x b).
  **Down-branch:** 쿠팡 사태가 협상을 오염 → 발표 연기 **AND** 301조 발동 → exporter overhang re-prices wider.
  **Track KPI:** 07-22~24 headlines · 1호 서명 여부 · **10% 임시관세 만료일 [blank — not in any calendar, not guessed]**
  · 한화오션 short direction · 쿠팡 의제 분리 여부.

- **M-07 — Defensive cash-flow bid (CARRIED, strengthened — and it survived a risk-on day, which is the test).**
  ***삼바 upgraded 🟡중립 → 🟢가속, OBV 중립 → 매집, RS20 +22.4% → +33.7%, 외국인·기관 동시 순매수**; 셀트리온
  RS20 +27.8% with 기관 +123.0만; **바이오헬스 수출 상반기 161억달러 역대 최대**; banks accumulated (M-01).*
  ★ **The named anti-branch was tested today and did NOT fire.** 07-20 said: *"if AI risk-on re-ignites,
  this defensive bid unwinds fast."* **Today the index rose 3.56% and 삼전 6% — and 삼바 was UPGRADED, not
  unwound.** That is the opposite of the US desk's XLV finding (worst sector on a risk-on day = hedge, not
  destination). **In KR, the defensive bid is behaving as a destination.** Recorded as a measured divergence
  between the two desks, not smoothed.
  **Anti-branch (still live):** **코오롱티슈진 3상 실패 하한가** [12a/5s] shows the sector's binary risk is
  name-level and violent; 알테오젠 SC효소 위협론; 삼바 RS60 still **−17.8%**.
  **Track KPI:** 삼바 RS60 (−17.8% → does it cross 0?) · bank OBV persistence · **알파벳 07-22** as the risk-on test.

---

## ✏️ CORRECTION (applied post-DEEP, 2026-07-21) — M-07 and the HLTH tilt

**M-07's headline claim in §4a is REFUTED by measurement, and it is retracted here rather than left standing.**

I wrote: *"The named anti-branch was tested today and did NOT fire… the index rose 3.56% and 삼바 was
UPGRADED, not unwound… **In KR, the defensive bid is behaving as a destination.** Recorded as a measured
divergence between the two desks."* **That was one session read as a regime.**

DEEP-HLTH measured it properly (120d daily vs `^KS11`), **after validating the method against the US desk**
(its code reproduces XLV/SPY at β −0.17 / up-day excess −0.75% vs the US desk's −0.16 / −0.74% — same ruler):

| | β vs index | up-day excess | down-day excess |
|---|---|---|---|
| 삼성바이오로직스 | **0.40** | **−2.08%** | +2.09% |
| 셀트리온 | 0.47 | −1.78% | +1.98% |
| **EW basket, 10 KOSPI pharma** | **0.44** | **−1.94%** | +2.07% |
| *control:* 삼성전자 | **1.26** | **+0.92%** | — |

- **Normalized per 1% of index up-move** (KOSPI up days average **+2.63%** vs SPY **+0.73%** — a **3.6×
  amplitude trap** that made the raw numbers look incomparable): **XLV −0.92~−1.13 vs KR HLTH −0.74~−0.95.**
  **Same sign, same order of magnitude. The two desks did NOT measure opposite things.**
- **On 07-21 itself:** 삼바 **+0.16% excess (essentially zero)**, 셀트리온 **−4.14% excess**, basket **−3.47%**
  — KR HLTH behaved exactly as XLV did on its own risk-on day. **Over the 10 largest KOSPI up days, 삼바 lost
  to the index 10 times out of 10** (mean −4.56%).
- **The RS20 I leaned on is a down-day artifact:** 삼바's 20d cumulative excess **+36.0% = −18.1% from up days
  + 54.1% from down days**. Absolute 20d: **KOSPI −26.0%, 삼바 +7.7%** — **the "+33.7%" is 77% index collapse.**
- **Refinement, not just a reversal:** KR β is **+0.44, not negative** like XLV's −0.17 → **a low-beta SHELTER,
  not an offset hedge**, and it **leaks** (under-delivers its own beta on up days by ~0.47pp). 삼바's single-day
  divergence was **the 2.7조 M&A as a NAME event inside a hedge wrapper**, not a sector regime.

**→ §4 #3 HLTH "OW ▲ up" is corrected to OW-as-SHELTER (hedge role), converging with the US desk's P7
rather than diverging from it. ROTATION's rank-1 "TRIPLE AGREE" is corrected in that file's C2.**

⚠ **A cited catalyst in §3a/§4 was overstated 2.7×:** *"바이오헬스 수출 상반기 161억달러 역대 반기 최대"*
is **43.3% cosmetics** (69.8억$, the fastest-growing component). **HLTH-attributable is 60.6억$.**

⚠ **Recurring failure class #1 (banking a one-sided read of an oscillating variable) did NOT hold this run.**
§5 scores M-07 as **HIT** on the grounds that its anti-branch was "tested and failed to fire." **That score is
withdrawn — the anti-branch was tested by a method too weak to detect it (one session, no beta control).**
**New rule, folded into the standing watch: an anti-branch is only "tested" when it is tested with a
measurement, not with a day.** This is the run's most expensive lesson and it was caught inside the run.

---

## §5 Self-backtest — prior propositions scored at **+1 session** (07-20 → 07-21)

⚠ **Horizon caveat, stated first: this is a +1d score, not the protocol's +7/+14/+30d.** The prior KR run
was yesterday. **One session on a +3.56% index day is a weak test and several of these are provisional.**
The +5d score of the **07-16** run is given underneath, which is the honest window.

| # | Prior proposition (07-20 §4a) | Δ to 07-21 (measured) | Score (+1d) |
|---|---|---|---|
| M-01 | Hike → bank NIM → FIN OW | **3rd bank added: 하나 RS20 +36.7%, 매집, 서지 1.16x, 기관 +145만**; all three intact. **BUT the liability side repriced (예·적금 16조/보름, 저축銀 4%)** | **HIT — with a newly live anti-branch** |
| M-02 | Oil: flow accumulating into a FADING narrative; explicitly bracketed | **The thread flipped FADING → BUILDING (3→4→3→6→7)**; 홍해 봉쇄 + Goldman $120; S-Oil RS60 +13.4% → **+18.3%** | ★ **HIT — the named divergence resolved in the flow's favour.** The "flow sets the tilt when narrative inverts" rule paid |
| M-03 | AI-capex kill-switch fired; separate domestic-policy leg from hyperscaler leg | Kill-switch fired again (中 AI 차단 검토, 키미×3, Nebius −40%); **두산 RS60 −45.9% → −47.9%**; policy leg = **week's largest thread (124건)** | **ANTI-HIT — the separation was correct and is now measurable** |
| M-04 | Memory OW-but-gated; gate CLOSED. **Named KPI: "foreign net-buy sign flip"** | **KPI fired on the 5d window (both names), 삼전 🔴→🟡, RS20 −4.9%→−0.8%, record export print** — but 20d weak-hands intact, **하이닉스 RS20 −6.6%→−11.1%**, 서지 0.89× | **HALF — the gate discipline is the win.** A desk that had gone OW yesterday would now be long the twin that deteriorated |
| M-05 | 철강 narrative refuted by flow → UW | **POSCO 서지 0.68× unchanged, RS60 −29.2% → −33.7%, 기관 −31.7만** while the AI-철강 story ran again | **HIT (3rd consecutive)** |
| M-06 | 대미투자 dated binary 07-22~24, both branches | Binary now **D-1**, unresolved; ★ **and it split — a second, statutory 301조 axis appeared (BUILDING 2→4)** that the proposition did not contain | **CARRIED → widened.** ⚠ **A miss of scope, not of direction: I was watching the negotiation and the calendar fired** |
| M-07 | Defensive cash-flow bid; **anti: "unwinds fast if AI risk-on re-ignites"** | **AI risk-on DID re-ignite (+3.56%, 삼전 +6%) and 삼바 was UPGRADED (🟡→🟢, OBV 매집)** | **HIT — and the anti-branch was tested and failed to fire, which is stronger than an untested hit** |

**+1d tally: 4 HIT · 1 ANTI-HIT · 1 HALF · 1 CARRIED-widened. No proposition failed one-way.**

**The honest +5d score (07-16 → 07-21), which is the horizon that means something:** the 07-16 run's calls
were M-01 FIN OW (**HIT** — three banks accumulating, +33~37% RS20 vs an index −25.97%/1m), M-02 tactical
ENRG (**HIT** — S-Oil RS60 +18.3%, board-best), M-03 AI-power with a named kill-switch (**ANTI-HIT** — the
switch fired; a one-way UTIL OW would have carried a −47.9% RS60), M-04 memory gated (**HALF** — the gate
held through a −25% month and is only now rattling), M-05 밸류업 rotation (**ANTI-HIT** — killed same-day
on 07-16 §5a). **Running: 2 HIT · 2 ANTI-HIT · 1 HALF at +5d.**

**Recurring failure class #1 — banking a one-sided read of an oscillating variable: still contained.**
Tested three times this run (M-02 narrative reversal, M-04 gate rattle, M-07 anti-branch test) and the
bracket paid each time.

**Recurring failure class #2 — narrative–flow inversion (opened 07-20): CONFIRMED as a working rule.**
It made two correct calls in a row: **M-02** (flow was right, the story came back to it) and **M-05**
(story was wrong, 서지 never moved). **Rule retained: when narrative and measured flow invert, the flow
sets the tilt and the narrative becomes the tracked anti-signal.**

**★ NEW failure class observed this run — *watching the negotiation and missing the calendar* (M-06).**
I carried the trade axis as a **bilateral negotiation with a date I could see** (방미 07-22~24) and
therefore missed a **unilateral statutory action building in plain sight** (301조 관세, 2-day BUILDING
thread, 49 articles) — **and the blindspot pass structurally could not catch it** (a 2-day event is
invisible to a 7-day emergent-term window; only the event axis saw it). **Rule going forward: every
policy proposition must name BOTH the negotiated instrument and the automatic one, and their dates
separately.** This is the same failure the US desk logged on Canada, in the same week, from the other side.

---

## ✅ EXIT CHECK
- [x] **Catalysts injected** — `catalyst_calendar --days 5` → `llm_outputs/2026-07-21/CATALYST_WATCH.json`.
      ⚠ Module missed the KR binary for a **2nd consecutive run** (방미 07-22~24) **and** the new 301조 axis →
      both manually injected in §0. 7 binaries, all bracketed both ways in §4a.
- [x] **Events read via `--body 2`, tail count = 0** — 3,770 → 1,113 → 612 → **369 market, head 42 / body 327,
      ALL 369 read** (stdout truncates the body at ~30 with `… 외 297개`; the remainder was read from
      `out/news_brief/2026-07-21_domestic.json`). The pool jump vs 07-20 (145 → 369 market events) is stated
      up front so no count delta is read as a signal.
- [x] **Trajectories read** (`thread --days 7`) — every §4a proposition carries its thread tag + curve, or
      states "no thread". **Window-end inflation flagged in the opposite direction from 07-20** (612-event
      end inflates BUILDING). **ENDED-under-open-proposition staleness flags raised for M-01 (BOK, 2nd run),
      M-02 (호르무즈 — successor thread re-ignited), 원화국제화 (downgraded to dormant), 최태원.**
- [x] **Every "quiet" claim carries its denominator** — buckets 3 and 7 called *declining* only on an
      absolute-level fall against a **+11.8% pool**; DISC/STPL downgrades cite named dated events
      (KB증권 목표가↓ 7a/5s; 나프타 2a/2s), not unbacked absence.
- [x] **No 0/near-0 bucket trusted.** All 7 passed as **separate argv**, 3+ char forms only (the 2-char
      trigram trap verified on 07-20 — 환율·외환·원화·달러·상법·세제·관세 = 0 each = absence of INDEX).
      **Coverage run with a non-zero denominator (20,578) → 🔴 심각 / recall 37.3%** — the 🔴 is real, not
      the 0-denominator-prints-🟢 artifact.
- [x] **Transmission matrix produced** — all 11 GICS sectors, one line each, with Δ vs 07-20 and driving prop;
      6 divergences named with owners in §4x.
- [x] **MACRO_REPORT.md written** with primary numbers explicit ([FRED via US-desk] asof dates + staleness
      flags on DXY/VIX/CPI/M2 + "US rates are 2 sessions behind the KR tape"), **self-backtest appended at
      both +1d and +5d with the horizon caveat stated**, and **9 new blind-spot terms folded into the living
      term table**.
- [x] **★ Tooling trap recorded (§2): bare 6-digit KR tickers returned silent empty rows in `module_flow`
      today; `.KS` suffix required.** A stage that trusted that output would have reported "no flow signal"
      on the day the flow inverted.

**News source = server DB via NEWS API `127.0.0.1:8787` (routed `/exec`, not local fallback).**
**Flow source = `module_flow` — KIS per-investor actuals + KRX short interest (the KR edge axis).**
**Cross-read source = `llm_outputs/2026-07-21/industry_US/MACRO_REPORT.md` §1 (same-day US desk).**

**→ proceed to SWEEP.**
