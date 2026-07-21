# SECTOR_DEEP_ENRG — 정유·에너지전환/신재생 · 2026-07-21 (Tue)

> **CONTINUOUS track (07-16 / 07-17 / 07-20 → 4th consecutive run). DELTA-LED.**
> Unchanged structure is carried **by reference**, not re-printed:
> [`2026-07-20/SECTOR_DEEP_ENRG.md`](../../2026-07-20/industry_KR/SECTOR_DEEP_ENRG.md) (value-chain §D, TACO branches, 최고가격제 §C-1, 샤힌 §C-2) ·
> [`2026-07-17/SECTOR_DEEP_ENRG.md`](../../2026-07-17/industry_KR/SECTOR_DEEP_ENRG.md) (segment mix, Group III 병목).
> **Analysis product. Zero buy/sell calls. Zero sizing (BET's job).** Blanks stay blanks. Every claim carries source + asof.
> Inputs re-read from disk: `MACRO_REPORT.md` §2/§4a M-02 · `SWEEP_READ.md` §2(c)/§5 · `EVENT_ALPHA.md` CARD 2 · `SECTOR_ROTATION.md` §2/§4.
> Tools: `module_flow`(KIS 20d 실측 + KRX 공매도, asof 2026-07-21 close) · `module_chart --read`(VERBATIM) · `module_valuation` ·
> `module_disclosure --days 60` + **OpenDART `document.xml` 원문 직접 파싱** · `module_news_data fts`(NEWS API) · `module_report_tags` ·
> **yfinance correlation panel (this file's core measurement, script retained in scratchpad)**.

---

## §0 ★ THE DELTA — three things changed in one session, and two of them cut against the position

1. **The crack spread finally got a number — and it broke the same day it got one.** The 07-20 file recorded
   *"복합정제마진·크랙스프레드 정량치 미상 — 이 데스크에 해당 시계열 모듈 없음"* as its **#2 anti-signal**. It is
   no longer missing. **[yonhap 07-21 10:01 본문]** quotes VanEck's Matthew Sigel: **the US 3-2-1 crack reached
   ≈$70/bbl on 07-20, above even the 2022 energy-crisis level.** My independently constructed NYMEX 3-2-1 proxy
   prints **$69.33 on 07-20 — agreement within $0.67, and the 98.9th percentile of 9 months.**
   ★ **And on 07-21 the same proxy fell to $63.36 — −$5.97, −8.6% in one session.**
   **The celebratory record article and the first real break printed on the same day.**
2. **★ The one question is answered, and the answer is "TWO bets, and neither is the crack spread."** §1.
3. **475150's KKR change-of-control is no longer 미해소 — it is in the primary filings with a strike price,
   a closing date (07-31) and a conditional EGM (07-28).** The 07-20 file wrote *"오늘 확인 가능한 1차 출처(DART)에
   관련 공시 없음"*. **That was a 30-day-window artifact. At 60 days the filings are all there.** §4.

**Carried unchanged, explicitly:** 최고가격제 8차 고시 (≈07-24~26) still pending — `fts 최고가격제 --days 5` returns
**no new print since [yonhap 07-19]**; 9월 원유 확보율 **74%** (7~8월 100%+) unchanged [산업통상부 via yonhap 07-19].

---

## §1 ★★ THE ONE QUESTION — "096770 · 010950 · 475150: one bet or three?" **MEASURED, not asserted**

### Verdict: **TWO bets, not one and not three. And the driver named by MACRO/EVENT_ALPHA — the crack spread — is refuted as the daily mechanism of either.**

MACRO §4a M-02 and EVENT_ALPHA CARD 2 both close with *"096770 · 010950 · 475150 are ONE driver, not three…
BET must size them as a single exposure."* **That warning is half right, and the half that is wrong is the
expensive half.** Measurement follows.

#### (a) Method, stated before the numbers (so the caveats bind me, not just the result)

Daily log-free simple returns, `yfinance`, **asof the 2026-07-21 close** (last index verified = 2026-07-21).
Crack proxy = **NYMEX 3-2-1** = `(2×RB=F + 1×HO=F)×42/3 − CL=F` in $/bbl.
⚠ **Three limits I am not hiding:**
- **The 3-2-1 is a US Gulf construct.** The margin that actually pays S-Oil is the **Singapore complex /
  Dubai** margin. **That series remains 미상 — no module on this desk carries it.** The US crack is a proxy
  whose validity rests on the *global* co-movement the yonhap article itself describes, not on identity.
- **Non-synchronous trading.** KR closes 15:30 KST; NYMEX and NYSE settle *after* it. A same-day
  `corr(KR_t, WTI_t)` mixes in information Korea could not have seen. **I therefore report lag-0, lag-1, and
  a 5-day overlapping-window spec, and I lead with the 5-day one** — it is the least time-zone-contaminated.
- **n is small** (20d = 20 observations). The 20d numbers are directional; the 60d and 5d-overlap carry the weight.

#### (b) Pairwise return correlation — the headline table

| Pair | **20d** | **60d** | **120d** | KOSPI-residualised 60d | **5d-overlap (60 sess)** |
|---|---|---|---|---|---|
| **096770 SK이노 ↔ 010950 S-Oil** | **+0.768** | **+0.727** | +0.612 | **+0.788** | **+0.705** |
| 010950 S-Oil ↔ 078930 GS | +0.469 | +0.520 | +0.534 | +0.528 | **+0.744** |
| 096770 SK이노 ↔ 078930 GS | +0.484 | +0.518 | +0.608 | +0.526 | +0.653 |
| **096770 SK이노 ↔ 475150 이터닉스** | **+0.255** | +0.367 | +0.330 | +0.335 | +0.460 |
| **010950 S-Oil ↔ 475150 이터닉스** | **−0.002** | +0.189 | +0.134 | +0.216 | **+0.141** |

★ **The residualised column is the one that settles it.** Stripping KOSPI *raises* the refiner pair from
0.727 → **0.788**. Their co-movement is **not** market beta — it is a genuine shared factor. It is also
**stable, not a spike**: rolling-20d over the last 8 sessions ran **0.78 · 0.81 · 0.82 · 0.82 · 0.80 · 0.80 · 0.80 · 0.77.**

★ **The 이터닉스 pair is going the other way.** Rolling-20d 096770↔475150 over the same 8 sessions:
**0.36 · 0.36 · 0.36 · 0.39 · 0.35 · 0.34 · 0.29 · 0.25 — decaying.** Against S-Oil it is **−0.002**, i.e. nothing.

#### (c) Variance decomposition — how much is actually shared

- **r² (096770, 010950) = 0.529 → 52.9% of S-Oil's daily variance is shared with SK이노; 47.1% idiosyncratic.**
- **475150 regressed on the refiner-pair average: 60d r = 0.301, β = 0.681, idiosyncratic share = 90.9%.
  20d: r = 0.136, idiosyncratic share = 98.1%.**
- **PCA on KOSPI-residualised returns of the three (60d):** PC1 explains **65.0%**, loadings
  **SK이노 −0.667 / S-Oil −0.641 / 이터닉스 −0.381**. **PC2 explains 28.3% and loads +0.917 on 이터닉스 alone.**
  At 20d it is starker: PC1 61.9% (−0.701 / −0.676 / **−0.227**), **PC2 32.5% loading +0.961 on 이터닉스.**
  **→ There are two factors here, and the second factor IS SK이터닉스.**

#### (d) ★ The refutation nobody asked for: **neither refiner tracks the crack spread**

| Name | vs **WTI** | vs **Brent** | vs **Crack 3-2-1** | vs **US refiner equities** (MPC/PSX/VLO avg) |
|---|---|---|---|---|
| **5-day overlapping, 60 sessions** | | | | |
| 096770 SK이노 | **+0.434** | +0.444 | **+0.093** | **+0.420** |
| 010950 S-Oil | **+0.535** | **+0.578** | **+0.051** | **+0.578** |
| 078930 GS | +0.271 | +0.311 | −0.088 | +0.301 |
| **475150 SK이터닉스** | **−0.068** | −0.053 | +0.343 | **−0.001** |
| **daily, 60d, lag 0** | | | | |
| 096770 SK이노 | +0.173 (r²=3.0%) | +0.140 | **−0.054** | +0.018 |
| 010950 S-Oil | +0.185 (r²=3.4%) | +0.173 | **+0.013** | +0.101 |
| 475150 SK이터닉스 | +0.135 | +0.124 | +0.175 | +0.125 |

**Read it plainly:**
- **At the weekly horizon the two refiners are an oil-complex / global-refiner-equity beta** (r 0.43–0.58 vs
  WTI and vs MPC/PSX/VLO) — **and they are ~zero against the crack spread (0.051, 0.093).**
- **The thesis names the crack as the mechanism. The tape says the crack is not what they trade on.**
  They trade on the *level* of crude and on what US refining equities do. **That matters because the two
  legs have opposite TACO exposure**: a ceasefire cuts the crude level immediately, whereas the 07-20
  file's surviving-margin argument (러시아 경유 금수, Group III 부족) lives in the crack — **the component
  the price is measurably NOT tracking.** The defensive part of the 07-20 thesis is the part with no
  measured price transmission.
- **475150 is −0.068 vs WTI and −0.001 vs US refiners at the weekly horizon. It is not an oil security.**

⚠ **Honest counter to my own finding:** over 20 sessions the *cumulative* moves are directionally consistent
with an oil-margin story — S-Oil **+32.3%**, SK이노 **+16.1%**, GS **+22.0%**, while MPC **+23.3%** / PSX
**+23.5%** / VLO **+20.3%** since 06-30 (article claims 24/23/20 — **matched to ~1pt**). **Low daily correlation
with a spread is not proof the spread is irrelevant to earnings**; it proves the spread is not what the daily
tape prices. Both statements are in this file.

#### (e) ★ A benchmark artifact every RS20 in this run is sitting on

**KOSPI 20-session return = −25.97%** (2026-06-22 **9,114.55** → 2026-07-21 **6,747.95**; that 06-22 print is
the 9-month peak, so the index is −26.0% from its high; worst sessions 03-04 −12.06%, 06-23 −9.99%, 07-13 −8.95%).

**Therefore RS20 is ~26 points of benchmark collapse before any name does anything:**

| Name | own 20d price | + |KOSPI 20d| | = RS20 (module) |
|---|---|---|---|
| 096770 | **+16.1%** | +26.0 | **+42.0%** ✓ |
| 010950 | **+32.3%** | +26.0 | **+58.3%** ✓ |
| 475150 | **+39.4%** | +26.0 | **+65.4%** ✓ |

Reconstructed to the decimal against `module_flow`. **"RS20 +65.4%" is +39.4% of stock and +26.0% of index
wreckage.** Not a correction to the flow module — a caution about how the number reads.

#### (f) ★ And the "base, not a bounce" claim needs one dated qualifier

EVENT_ALPHA CARD 2 and SWEEP §5 call 475150's flat RS60 (−0.6%) **"a base, not a bounce"** — *"the only name
on the whole 829-name board"*. The RS60 arithmetic is correct (475150 +5.1% / KOSPI +5.6% over 60 sessions).
**But the price path is not a virgin base:**

> 120 sessions ago (2026-01-21) **₩19,350** → **peak ₩68,200 on 2026-04-03** → today **₩55,900**.
> **120d = +188.9%. Currently −18.0% from the April peak.**

**→ It is a consolidation inside a completed +189% advance, not a floor.** That does not falsify the setup;
it changes what it is. **A base after a triple is a different risk object from a base after a decline**, and
`module_chart` agrees — 475150 is the only one of the four tagged **PULLBACK-TO-SUPPORT**, not CONFIRMED-TURN.

#### (g) ▶ **RESOLUTION VERDICT**

> **NOT one bet. NOT three. TWO.**
>
> **Bet A = 096770 SK이노베이션 + 010950 S-Oil (+ 078930 GS).** Residualised r **0.788**, 5d-overlap **0.705**
> (GS↔S-Oil **0.744**), shared daily variance **52.9%**, and a **diversification ratio of 1.076** for a 50/50
> refiner pair — **1.000 means zero diversification.** These are one position wearing two-to-three tickers.
> **MACRO and EVENT_ALPHA were right about the concentration.**
> **They were wrong about its name: measurably it is a crude-level + global-refiner-equity beta, not a
> crack-spread bet** (r vs crack = **+0.051 / +0.093**).
>
> **Bet B = 475150 SK이터닉스.** **90.9% idiosyncratic at 60d, 98.1% at 20d**, r vs S-Oil **−0.002**, r vs
> WTI **−0.068** and vs US refiners **−0.001** at the weekly horizon, its own principal component
> (**PC2 = 28–33% of the complex's variance, loading 0.92–0.96 on it alone**), correlation to the refiners
> **decaying** (0.39 → 0.25 over 8 sessions) — **and, independently of any statistic, its primary filings
> name three drivers that contain no crude term** (§4). **Folding it into the oil bet is the error, not the fix.**
>
> **What this means for the risk budget (arithmetic, not a recommendation — sizing is BET's):**
> 60d annualised vol — **SK이노 67.8% · S-Oil 66.1% · 이터닉스 139.3%.** 이터닉스 carries **~2.1× the volatility
> of either refiner.** Consequently, on measured covariance:
>
> | Basket | portfolio vol | risk contribution SK이노 / S-Oil / 이터닉스 |
> |---|---|---|
> | equal 1/3 each | 70.6% | 25.1% / 20.4% / **54.5%** |
> | refiners only, 1/2 each | 62.0% | 50.8% / 49.2% / — |
> | 0.4 / 0.4 / 0.2 | 63.6% | 37.7% / 33.1% / 29.2% |
> | **equal-risk solve** | 64.3% | **36.5% / 41.4% / 22.1% weights → 33.3% each** |
>
> **★ Two binding observations for BET:**
> **(1)** Sizing 096770 and 010950 as independent names **double-counts one position** — the diversification
> ratio is 1.076.
> **(2)** An *equal-weight* three-name basket is **not** diversified into 이터닉스 — it is **54.5% 이터닉스 risk**.
> **The concentration error MACRO warned about is real, but it runs in the opposite direction from the warning:**
> the danger is not that 475150 is secretly the same bet — it is that at equal weight it silently becomes
> **the majority of the risk** while being the one name whose driver the sector thesis does not describe.

---

## §2 Flow — measured delta vs 07-20 (asof 2026-07-21 close · KIS 20d 실측 · KRX 공매도)

| Name | flow | OBV | RS20 | RS60 | 서지 | 외 / 기 / 개 (만주, 20d) | 공매도 %float |
|---|---|---|---|---|---|---|---|
| **096770 SK이노** | **+1.00 🟢가속** | 매집 | **+42.0%** | −18.5% | **1.70×** ★board-top large-cap | −31.2 / **+205.0** / −152.4 | 0.13% flat(−0.02) |
| **010950 S-Oil** | 🟢가속 | 매집 | **+58.3%** | **+18.3%** | 1.15× | −9.4 / **+186.8** / −184.5 | **0.49% building(+0.04)** ⚠주목선 |
| **475150 SK이터닉스** | **+1.00 🟢가속** | 매집 | **+65.4%** | −0.6% | **1.60×** | **+21.8** / **+144.0** / −172.6 | **2.53% 🔥크라우디드 covering(−0.03)** |
| 078930 GS | 🟡중립 ▼ | **중립** ▼ | +48.0% | +10.9% | 1.19× | **−58.5** / +119.0 / −61.7 | 0.02% flat |

**Deltas that matter:**
- **GS downgraded itself.** 07-20: 🟢가속 / OBV 누적 / CONFIRMED-TURN. Today: **🟡중립, OBV 중립**, 외국인
  **−58.5만** (largest exit of the four). ⚠ **The 07-20 file's unresolved "GS OBV 상충 (flow 분산 ↔ chart 누적)"
  is now resolved — downward.** GS was ranked **#1 candidate** on 07-20 as *"마진 테제의 최저가 노출"*.
  **The money left it while the thesis stayed.** Its valuation is still the cheapest (Fwd PER 5.0 / PBR 0.51).
- **All four still show 기관 net-buying and 개인 net-selling.** The real-hands signature is intact and is the
  strongest single fact in this file's favour.
- **The foreign side has quietly inverted vs 07-20 on 475150:** 07-20 read 외국인 **−6.0만 (순매도 전환)**;
  today **+21.8만**. It is the only one of the four with foreigners net-buying.

### 📊 CHART_READ — `module_chart --read` · **VERBATIM**

**SK이노베이션 (096770)**
```
OBV: 누적(매수압력↑) (20d기울기 +112%)
다이버전스: 없음
MA정렬: 혼조 · 가격 3/4 MA 위
볼린저: 확장 36.3% · 중단
RSI: 68.0 · 모멘텀20d +24.1%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>116,385 + OBV→누적 / 스탑(스윙저점): 89,500
```

**S-Oil (010950)**
```
OBV: 누적(매수압력↑) (20d기울기 +39%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 확장 57.1% · 중단
RSI: 77.0 · 모멘텀20d +39.5%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 93,200
```

**SK이터닉스 (475150)**
```
OBV: 누적(매수압력↑) (20d기울기 +22%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 확장 51.8% · 중단
RSI: 54.9 · 모멘텀20d +48.3%
턴-판정: PULLBACK-TO-SUPPORT (추세 눌림목)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 37,700
```

**GS (078930)**
```
OBV: 누적(매수압력↑) (20d기울기 +22%)
다이버전스: 없음
MA정렬: 혼조 · 가격 4/4 MA 위
볼린저: 확장 37.6% · 중단
RSI: 72.0 · 모멘텀20d +26.9%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 62,500
```

★ **Two resolutions the chart delivers:**
1. **The 07-20 file's 4-day-old "475150 OBV 상충" (chart −10% vs flow 매집) is RESOLVED** — chart OBV is now
   **+22% 누적**, agreeing with flow. And **RSI fell 59.2 → 54.9 while 모멘텀20d rose +20.4% → +48.3%** —
   price advancing with RSI cooling is the shape of a consolidation, consistent with PULLBACK-TO-SUPPORT.
2. **S-Oil's 과열 eased materially: RSI 86.2 → 77.0.** The 07-20 file's anti-signal #4 ("RSI 86.2 극단") has
   **decayed, not fired.** SK이노 RSI 73.8 → **68.0** and lost a MA (4/4 → **3/4 위**).

---

## §3 ★ Short interest — the secondary question, both directions

### (a) 475150 SK이터닉스 — **2.53% 🔥크라우디드, covering.** Read: **neither pure squeeze fuel nor the smart side — it is most likely event positioning around a dated deal.**

**The measurement first:**

| asof | %float | tag | source |
|---|---|---|---|
| 2026-07-16 | 3.05% | covering (−0.23) | 07-16 SECTOR_DEEP_ENRG |
| 2026-07-17 (basis of the 07-20 file) | **3.12%** | **building (+0.54)** | 07-20 SECTOR_DEEP_ENRG |
| **2026-07-21** | **2.53%** | **covering (−0.03)** | `module_flow` today |

**Over 4 sessions the short book fell 3.12% → 2.53% = −0.59pp = −19% of the position, while the stock rose
₩52,000 → ₩55,900 (+7.5%).** That is covering into strength, and it is the *third* direction-flip in five
sessions (covering → building → covering).
⚠ **Unresolved measurement discrepancy, stated not smoothed:** the module's own delta tag reads **(−0.03)**
while the level moved **−0.59pp**. The tag and the level disagree by an order of magnitude — the tag is
presumably a shorter lookback than the interval between my two observations, and **KRX short-balance data is
itself T+2/T+3 lagged.** Do not treat either number as same-day truth.

**Why "squeeze fuel vs smart side" is the wrong binary here — and this is the §4 finding doing the work:**
475150 has **a change-of-control SPA closing 2026-07-31 and a conditional EGM on 2026-07-28** (§4a). A 2.5%
short into a dated deal with a **known strike price ₩23,700 versus a ₩55,900 market** is far more consistent
with **event/deal positioning** than with either a directional bear or trapped shorts.
**What is observable and what is not:**
- **Observable, and it did happen:** the book shrank 19% in 4 sessions into a rising price.
- **Not observable with this desk's tools:** whether the residual 2.53% is directional, arbitrage, or hedge.
  **KRX publishes balances, not intent. I cannot resolve it and I am not going to guess.**
- **The dated test that resolves it for free: 07-28 (EGM) and 07-31 (closing).** If the short covers *through*
  those dates, it was event positioning. If it rebuilds after them, it is directional. **No inference needed —
  wait 5 sessions.**
⚠ **Crowding counter-evidence the flow tags cannot see:** 475150 was named as a **retail broadcast tip on two
consecutive days** — [mt/MTN 시선집중 07-20] *"KKR과 2조 규모 합작, 국내 최대 신재생 기업 출범"* and
[mt/MTN 07-21] *"정책·유가·금리 수혜 더해진 신재생에너지 기대감"*. **These are TV tip sheets, not sell-side
research, and they are a crowding observable pointing the opposite way from "under-owned base."**

### (b) 010950 S-Oil — **0.49% building, right at the ⚠주목 threshold.** Read: **small, persistent, and directionally informed so far.**

**0.44% → 0.48% → 0.49%, building on every one of the last three runs**, and the 07-20 file already flagged it
at *"0.5% 주목선 바로 아래"*. It is **still below the line, four sessions later** — the build is **slow**, which
argues against an imminent event trade and for a steady position.
★ **The asymmetry worth naming:** this short is building into the name with **RS20 +58.3% (board-best), RS60
+18.3%, 4/4 MA 위, RSI 77.0.** Shorting the strongest chart in the sector is either wrong or early. **§1(d)
supplies a mechanism under which it is early**: S-Oil's 5d correlation to **WTI is +0.535** and to the **crack
+0.051** — so a short here is a short of the *crude level*, which is exactly what the live ceasefire document
would cut. **The 0.49% short and the TACO anti-branch are the same trade.** That is a coherent position, not a mistake.
**Scale check, so this is not over-read:** 0.49% of float is **small**. 현대차 is at 1.99% and 한화오션 at 1.44%
[MACRO §2]. **S-Oil's short is one-quarter of the board's most crowded. It is a signal about direction, not size.**

---

## §4 ★★ IR anchor — from primary filings (OpenDART 원문, not headlines)

⚠ **Correction to the 07-20 file, which is the reason this section exists.** 07-20 §C-3 recorded the KKR
question as *"오늘 확인 가능한 1차 출처(DART)에 관련 공시 없음 (최근 30일 공시 6건)"* and left it 미해소.
**With `--days 60` and the document API, every piece is on file.** The 30-day window was the failure, not DART.

### (a) 475150 SK이터닉스 — change of control, **priced, dated, and conditional**
**[DART 20260630801211, 투자판단관련주요경영사항, 정정 2026-06-30; 최초 2026-03-06]** — quoted from the filing:
> *"당사 최대주주인 에스케이디스커버리㈜가 보유하고 있는 당사의 보통주식 **10,455,825주(지분율 약 30.98%)**를
> **Eclipse Holdco L.P.**에게 처분하는 이사회 안건에 대해 승인… **처분금액: 247,800,000,000원** …
> **상기 양수인은 "KKR"이 운용하는 펀드가 당사 지분 취득을 위해 설립한 법인임** … **처분예정일: 2026년 7월 31일**"*

| Fact | Value | Note |
|---|---|---|
| Stake sold | **10,455,825주 = 30.98%** — SK디스커버리's **entire** holding | 최대주주 변경 |
| Consideration | **₩247,800,000,000 (₩2,478억)** | |
| **Implied strike** | **≈₩23,700/share** (247,800,000,000 ÷ 10,455,825 = 23,699.7) | derived, arithmetic shown |
| **vs 07-21 close ₩55,900** | **market is +135.9% above the negotiated control price** | |
| Board approval | 2026-03-06 | ⚠ **the strike is a March-dated price** |
| Closing | **2026-07-31** — **already slipped once from 06-30** | 정정사유: *"처분예정일 변경"* |

⚠ **The date caveat is load-bearing and I will not let the number oversell.** The SPA was struck **2026-03-06**;
the stock was ₩19,350 as recently as 2026-01-21. **₩23,700 was a premium when agreed.** It does **not** mean
the shares are 136% overvalued. **What it does mean, and this is the usable part: there is no premium-tender
catalyst available at these levels.** Any thesis component resting on "KKR will pay up for the rest" is
inconsistent with the only price KKR has actually put in writing.

**[DART 20260713800255, 주주총회소집결의, 2026-07-13]** — **임시주주총회 2026-07-28 09:00**, single agenda item
**기타비상무이사 2인 선임: Masahiko Kato (현 KKR Infrastructure Japan Director) · Abhishek Sharma (현 KKR
Climate/Infrastructure Singapore Director)**, and from the filing:
> *"상기 안건은 … 주식매매계약에 따라 **거래종결이 되는 것을 정지조건**으로 하여 그 거래종결 시점에 효력이
> 발생하고, 거래종결이 이루어지지 아니한채 주식매매계약이 해제·해지되는 경우 위 결의의 효력은 **자동으로 소멸**합니다."*

★ **This is a free, dated, binary observable in 5 sessions — the cleanest kill-switch/confirm in this file.**
**07-28 EGM → 07-31 closing.** KKR seating its own directors is the deal completing; the resolution
self-voiding is the deal failing. **No interpretation required.**

### (b) 475150 — the fundamental catalyst that has nothing to do with crude
**[DART 20260529800288, 투자판단관련주요경영사항, 2026-05-29]** — **직접전력거래계약 (Direct PPA)**:
> *"재생에너지전기공급사업자로서 … **계약용량: 100MW** · **거래기간: 거래시작일로부터 25년** … 거래금액
> **502,298,400,000원** … 당사의 2025년 연결재무제표 기준 매출액(385,640,769,900원) 대비 약 **130.25%**에 해당"* ·
> 상대방은 *"국내 대기업 계열사"*, **공시유보 기한 2051-05-28**.

⚠ **The filing's own "130.25% of revenue" is a 25-year cumulative and will be mis-quoted as a growth number.
Annualised it is ₩502,298,400,000 ÷ 25 = ₩201억/yr ≈ 5.21% of FY2025 revenue per year.** Still material,
contracted for 25 years, and **completely orthogonal to the crack spread** — which is §1's statistical
result arriving by a second, independent route.
Corroborating policy tape: *"정부가 재생에너지 **직접전력거래계약(PPA) 활성화**를 검토"* + RE100 이행 압박 [mt 07-21].

**[DART 20260624000151, 주요사항보고서(유형자산 양도 결정), 2026-06-24]** — solar asset securitization:
**50건 (자산양도 6 + 지위이전 44), ₩77,032,500,000 = 자산총액의 11.77%**, 거래상대방 **솔라닉스일호(Solarnix1)**,
양도목적 *"태양광 발전자원 **금융구조화**를 통해 자본효율성 및 수익성 제고"*, 계약체결일 **2026-06-30**,
양도기준일 **2027-03-31**, 외부평가 **이촌회계법인 "적정"**. Company total assets = **₩654,491,386,587**.

### (c) 096770 SK이노베이션 — **a hard earnings date, and the refinery-margin number arrives on it**
**[DART 20260716800628, 기업설명회(IR)개최, 2026-07-16]**:
> *"일시 **2026-07-30 16:00** … 개최목적 **2026년 2분기 경영실적 발표** … Online 실적발표 후 질의응답
> (Conference call, 한/영 동시통역)"*

★ **This is the single most important date in this file for Bet A.** The 07-20 report's #2 anti-signal was
that the entire margin case rested on **8–13-day-stale sell-side commentary with no hard $/bbl anchor**.
**2026-07-30 is when the anchor stops being a proxy** — actual 2Q refining and lubricant segment results,
with Q&A, from the larger of the two refiners.
Sell-side into it [yonhap 07-16, 하나證 윤재성]: *"2026년 연간 영업이익 전년 대비 **1,505% 급증한 6조5,000억원**,
사상 최대"*, 목표가 17→**20만원**, on *"정제마진 강세와 원유시장의 구조적 변화에 따른 **OSP의 마이너스 국면 진입**"*.
For S-Oil [mt 07-14, iM證]: 2Q OP **9,283억** (컨센 9,415억), **윤활유 OP +180% 4,663억 — 매출·영업이익 모두 역대 최고**,
목표가 13.5→17만원, and explicitly *"하반기는 유가 하향 안정화로 재고이익 소멸되고, **오버슈팅했던 정제마진도
레벨다운**되면서 상반기 대비 영업이익 감소는 불가피"* — **the bull note contains the bear case, dated.**

**Other primary-filing facts, recorded without inflation:**
- **096770 60일 공시 13건 — 수주 0 / 자기주식 0 / 자본변동 0 / 실적 0.** The 자회사 items are **SK온's China
  battery JV swap** (Huizhou EVE 49% 처분 ₩4,759억 ↔ SK On Jiangsu 30% 취득 ₩4,347억, 종결 2026-06-22) —
  **battery portfolio rebalancing, not refining and not renewables.**
- ⚠ **Latent [DART 20260610800638]:** SKIET 매각설 해명 **(미확정)**, *"지분 일부매각 등 사업 포트폴리오 조정과
  관련하여 다양한 방안을 검토 중이나, 현재까지 구체적으로 결정된 바 없습니다"* — **재공시예정일 2026-12-09.**
- **010950 60일 공시 7건 — 수주 0 / 실적 0.** Only 사외이사 선임(07-16) and **[기재정정]신규시설투자등(06-30)**
  (샤힌 관련, 07-20 §C-2 참조). **No new contract or capital event in 60 days.**
- ★ **A structural fact that cuts against "one SK bet":** 475150's selling shareholder is **에스케이디스커버리㈜**,
  **not SK이노베이션.** 475150 sits in the **SK디스커버리** sub-group; 096770 is under **SK㈜**.
  **They are not affiliates of each other, and no SK이노베이션 filing in 60 days transfers renewable assets
  to any KKR vehicle.** The 07-20 file's §C-3 framing ("SK이노베이션·SK에코플랜트·SK디스커버리 3사가 신재생
  자산을 KKR에 매각") is, **for 475150 specifically, a single-seller transaction: SK디스커버리 → Eclipse Holdco.**

### (d) Valuation (`module_valuation`, asof 07-21 close)

| Code | Name | 현재가 | 시총(억) | PER(TTM) | PER(Fwd) | PBR | 목표주가 | 상승여력% | 외인% | 배당% |
|---|---|---|---|---|---|---|---|---|---|
| 010950 | S-Oil | 141,600 | 159,417 | 17.52 | **7** | 1.72 | 159,000 | **+12.29** | **79.68** | 0.23 |
| 096770 | SK이노베이션 | 116,300 | 196,608 | — | 9 | **0.83** | 170,917 | **+46.96** | 14.31 | 1.72 |
| 475150 | SK이터닉스 | 55,900 | **19,043** | **76.68** | **64** | **7.04** | 57,250 | **+2.42** | 2.63 | — |
| 078930 | GS | 82,500 | 76,639 | 5.93 | **5** | **0.51** | 103,000 | +24.85 | 20.40 | **3.64** |

- **S-Oil 상승여력 +7.7% (07-20) → +12.29%** — consensus target rose faster than price; the 07-20 "연료 소진"
  concern **eased**, it did not fire.
- **475150 상승여력 +2.42%.** ★ **Consensus target ₩57,250 vs price ₩55,900 — the sell-side is out of room**,
  at **Fwd PER 64 / PBR 7.04**. **Whatever is buying this name is not buying it on consensus earnings.** §4(a)(b)
  say what it might be buying instead; the file does not claim to know.
- ⚠ **시총 discrepancy noted:** SWEEP §5 and EVENT_ALPHA carry 475150 at **₩1.67조**; `module_valuation` at
  today's close prints **₩1.90조** (19,043억). Cross-check: 10,455,825 ÷ 30.98% = **33.75M shares × ₩55,900 = ₩1.89조**.
  **₩1.90조 is right as of today; ₩1.67조 is a stale-price figure.** Either way it clears the ~₩2.5조 players
  threshold **only by continuous-track inheritance** — this remains a **sub-threshold name**, as 07-20 flagged.

---

## §5 Value chain — **by reference**, plus the two nodes that actually moved

**Carried unchanged from [07-20 §D](../../2026-07-20/industry_KR/SECTOR_DEEP_ENRG.md) — not re-printed:** the
7-node map [1]원유조달 → [2]해상수송 → [3]정제 → [4]윤활기유 GrIII → [5]석유화학 → [6]국내유통 → [7]수출,
the bottleneck ranking (★★[4] Group III = 최대구속; ★[1] 9월 물량; ★[2] 통항; ★[6] 최고가격제), the explicit
"not a bottleneck" list ([3] 정제 capacity, [5] 에틸렌 과잉, [7] 수출), and `module_industry_map` Cluster #2/#3.

**What changed at exactly two nodes:**

- **[3] 정제 — the margin node got its first quantitative print, and it is a two-sided one.**
  [yonhap 07-21 본문]: **미국 3-2-1 크랙 ≈$70/bbl (07-20), above 2022 크라이시스 수준** · **유럽 경유 마진
  ≈$65/bbl 사상 최고** · **북서유럽 정제마진 ≈$30/bbl 계절 최고** · **IEA: 2Q 전세계 정제유 생산 전년비
  −500만 b/d** · **Kpler: 6월 역내 석유제품 수출 ≈100만 b/d = 전쟁 전의 1/4** · 구조 요인 *"미국이 2019년 이후
  하루 120만∼130만 배럴 규모 정제설비를 **영구 폐쇄**"*.
  ★ **And my proxy says the node broke on 07-21: $69.33 → $63.36, −8.6%, from the 98.9th percentile.**
  **The supply-side facts are structural; the spread is not.** Both belong in the same paragraph.
- **[8] 신재생 leg — reclassified from "별개 레그 (유가 무관)" to a *measured* separate factor with named,
  filed drivers.** 07-20 called it a separate leg on judgement. **§1 and §4 now make it a measurement**
  (98.1% idiosyncratic; −0.001 vs US refiners) **with three primary-source drivers** (KKR SPA closing 07-31 ·
  100MW/25yr PPA · ₩770억 solar securitization) **and zero crude terms.**

**chain-hop:** unchanged and still **not run as evidence** — `chain-hop`'s universe is hardcoded `us_top300`
and returns 0/0 on KR themes (07-20 §H). **Not a negative result.** No new chain-hop candidate is proposed
this run; **GS (078930), the 07-20 promote, is downgraded on its own flow (§2) rather than replaced.**

---

## §6 Track KPIs — observable, dated, and each one able to fire

| # | KPI | Now | What fires it |
|---|---|---|---|
| **1** ★ | **US 3-2-1 crack (my NYMEX proxy; corroborated to $0.67 vs [yonhap 07-21])** | **$63.36 (07-21)**, from **$69.33 (07-20, 98.9th pct)** | **Two consecutive closes below $60** = the margin cycle rolled. **$55** = Bet A's stated mechanism is gone |
| **2** ★★ | **SK이노 2Q 실적 컨콜 — [DART] 2026-07-30 16:00** | consensus 연간 OP **₩6.5조** [하나證 07-16] | **The first hard $/bbl-equivalent anchor this desk will have owned.** Miss on 정유 segment = the 8–13d-stale sell-side case is falsified with a real number |
| **3** ★★ | **475150 임시주총 — [DART] 2026-07-28 09:00** (KKR 이사 2인, **정지조건부**) | 정지조건 = SPA 거래종결 | **Resolution passes → deal closing. Resolution auto-voids → SPA terminated.** Binary, free, 5 sessions |
| **4** ★ | **475150 SPA 거래종결 — [DART] 2026-07-31** (already slipped 06-30 → 07-31) | strike **₩23,700** vs price **₩55,900** | **A second slip** = execution risk on the one driver Bet B has |
| **5** | **475150 공매도** | **2.53% covering** (3.12% @07-17 → −19% of the book) | **Covers through 07-28/07-31** = it was event positioning. **Rebuilds after** = directional. §3(a) |
| **6** | **S-Oil 공매도** | **0.49% building(+0.04)**, 3 runs | **≥0.50%** = ⚠주목 threshold crossed. **Covering** = the TACO short capitulated |
| **7** ★ | **Ceasefire signature** — US desk's **live 10-day proposal, rejected so far by Khamenei** [MACRO §4a M-02] | rejected | **Signature** = Bet A's crude-level driver (r=+0.43~0.58) cuts immediately. §7 |
| **8** | **8차 석유 최고가격 고시 — ≈07-24~26** | **no new print since [yonhap 07-19]** (`fts 최고가격제 --days 5`) | **인상** = margin cap tightens. Still the least-narrated risk |
| **9** | **9월 원유 도입 확보율** | **74%** (7~8월 100%+) [산업통상부 via yonhap 07-19] | **<70%** = node [1] 구속 심화 |
| **10** | **475150 correlation to the refiner pair** | **20d r = 0.136, decaying (0.39→0.25 over 8 sessions)** | **r > 0.5 sustained** = §1's two-bet verdict is wrong and it IS one bet |
| **11** | **GS 078930 재확인** | **🟡중립, OBV 중립, 외국인 −58.5만** | 07-20's #1 candidate lost its flow. **🟢 return** = re-promotable; **another leg down** = drop it |

---

## §7 Anti-signals — as observables, ranked by proximity

1. **★★ THE CRACK BROKE ON THE DAY THE RECORD WAS PRINTED.** $69.33 → **$63.36 (−8.6%)**, from the **98.9th
   percentile**. Narratives peak with the number, and the number turned first. *Observable: two closes < $60.*
   ⚠ **Held against my own §1(d) finding, both ways:** the refiners' daily correlation to the crack is ~0
   (+0.051/+0.093), **so a crack collapse may not transmit to the price at all** — but it will transmit to the
   **earnings** the 07-30 call reports. **The spread breaks the story before it breaks the stock.**
2. **★★ TACO / ceasefire — the anti-branch got a document, and it must be carried at equal weight.**
   [MACRO §4a M-02] the US desk holds a **live 10-day ceasefire proposal, so far rejected by Khamenei**.
   **Crude already fell −1.07% on 07-21 (CL=F 82.34).** ★ **§1(d) makes this branch WORSE than the 07-20 file
   assumed:** 07-20 argued a TACO removes only the "프리미엄 성분" and leaves the margin component intact.
   **Measurement says the refiners track the crude LEVEL (5d r = +0.535 / +0.434) and NOT the crack (+0.051 /
   +0.093)** — i.e. **they track precisely the component a ceasefire cuts, and not the component that would
   survive it.** **The 07-20 "부분 되돌림, 0이 아니다" conclusion is weakened by today's measurement.**
   ⚠ Symmetric ammunition, as MACRO notes: **WTI COT is 10%ile crowded-SHORT** — a ceasefire removes the bid
   rather than squeezing anything. *Observable: signature headline; BZ=F < $75.*
   **Both branches are carried. This file does not tilt one way into a live binary.**
3. **★ Bet A is one position, and the desk has been sizing it as two-to-three for four runs.** Diversification
   ratio **1.076**. *Observable: it already happened; §1(g) is the correction.*
4. **★ An equal-weight three-name basket is 54.5% 이터닉스 risk** at **139.3% annualised vol** — the majority
   of the risk sits in the name whose drivers the ENRG thesis does not describe. *Observable: §1(g) table.*
5. **475150's consensus room is gone: 목표주가 ₩57,250 vs ₩55,900 (+2.42%), Fwd PER 64, PBR 7.04**, on a name
   **−18.0% from its April peak after a +188.9% 120-day advance** — and **named on retail TV two days running**.
   *Observable: the 07-28/07-31 dates settle whether there is a non-consensus driver.*
6. **The KKR strike is ₩23,700 vs a ₩55,900 market (+135.9%).** No premium-tender catalyst exists at these
   levels. ⚠ **Dated 2026-03-06** — it is not a valuation claim. *Observable: any revised consideration in a 정정공시.*
7. **GS's flow left while its thesis stayed** (🟢→🟡, OBV 누적→중립, 외국인 −58.5만) — **the 07-20 run's #1
   candidate**, on the cheapest multiples on the board (Fwd 5.0 / PBR 0.51). **The cheapest exposure is the one
   money is leaving.** *Observable: KPI 11.*
8. **8차 최고가격제 (≈07-24~26) — still the least-narrated risk, and still unfired.** 07-20 measured it at
   **theme-age 0.21× FADING**. **Nothing new in 5 days.** Silence is not absence. *Observable: 산업부 고시 문구.*
9. **Zero 수주 / 실적 / 자본변동 filings across 096770 and 010950 in 60 days.** The entire Bet A case is
   sell-side + tape. **07-30 is the first primary print.**
10. **Latent, unchanged: 검찰 정유4사 26조 유가담합** (07-06, 재부상 07-20) · **SKIET 매각설 재공시 2026-12-09** ·
    **샤힌 에틸렌 180만t vs 울산 구조조정** (07-20 §C-2).
11. ⚠ **My own instrument could be wrong.** The 3-2-1 is a **US Gulf** construct; **S-Oil is paid on the
    Singapore/Dubai complex, which this desk cannot measure.** The $0.67 agreement with [yonhap] validates the
    *proxy's construction*, **not its applicability to Korean margins.** If the two complexes diverge, KPI 1 misleads.

---

## §8 Tool limits · data quality (P4)

- **`module_business` skipped, not failed silently.** The 07-20 run recorded it as broken
  (`FileNotFoundError: data/news_alert.db`, `_ir_news.py:65`). **Segment revenue mix (S-Oil 정유78.8/윤활8.8/
  석화12.4, SK이노 석유59%) is still 07-16 DART inheritance and was NOT re-verified today** — third consecutive run.
- **`module_flow` 뉴스속도 = n/a on all four names** — same root cause. theme-age not re-run this file;
  narrative axis taken from EVENT_ALPHA CARD 2 and MACRO §3c rather than duplicated.
- ✅ **`.KS` suffix rule observed** — bare 6-digit tickers silently return empty rows (MACRO §2's caught trap).
- ✅ **`module_disclosure --days 60` beat `--days 30`.** The 07-20 "no DART disclosure" conclusion was a
  **window artifact**. Recommend 60d as the default for continuous-track names.
- ⚠ **`fetch_disclosure_detail_all()` returns 0 chars** for all four rcpNos tested; the OpenDART
  `document.xml` endpoint works fine (HTTP 200, valid ZIP). **The repo helper has a bug** — bodies in §4 were
  parsed by fetching and decoding the ZIP directly. **One filing (20260630000277) returns a non-ZIP payload
  and could not be read.** *Task logged.*
- **Singapore/Dubai complex refining margin: 미상.** No module carries it. §7-11.
- **Correlation caveats already stated in §1(a):** 20d n=20; non-synchronous KR/US sessions (hence lag-1 and
  5-day-overlap specs reported); 5-day overlapping windows inflate apparent significance — **no t-statistics
  or p-values are claimed anywhere in this file, deliberately.**
- **Ledger inherited, not re-derived** [`module_report_tags`]: **096770 = 21 reports, CONFIRMED** ·
  **010950 = 22, CONFIRMED** · **475150 = 10.** Per instruction, the CONFIRMED verdict is carried forward.
- **KRX short balances are T+2/T+3 lagged**; the level-vs-tag discrepancy on 475150 is flagged unresolved in §3(a).
- **CFTC COT (WTI 10%ile crowded-short) = Tuesday-close +3~4d lag → context, not a trigger.** Inherited from
  MACRO; not independently queried.

---

_Generated 2026-07-21 · DEEP-ENRG (CONTINUOUS · DELTA-LED) · `module_flow`(KIS/KRX 실측) · `module_chart --read`(VERBATIM) ·
`module_valuation` · `module_disclosure --days 60` + OpenDART 원문 · `module_news_data fts`(NEWS API) · `module_report_tags` ·
yfinance correlation panel. **Zero buy/sell calls. Zero sizing. TACO both branches carried. Blanks left blank.**_
