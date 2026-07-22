# SECTOR_DEEP_ENRG — 정유·에너지전환/신재생 · 2026-07-22 (Wed)

> **CONTINUOUS track (07-16 / 07-17 / 07-20 / 07-21 → 5th consecutive run). DELTA-LED.**
> Unchanged structure carried **by reference**, not re-printed:
> [`2026-07-21/SECTOR_DEEP_ENRG.md`](../../2026-07-21/industry_KR/SECTOR_DEEP_ENRG.md) (the correlation panel §1,
> the two-bet verdict §1(g), the KKR SPA §4(a), the risk-contribution table) ·
> [`2026-07-20`](../../2026-07-20/industry_KR/SECTOR_DEEP_ENRG.md) (7-node chain §D, 샤힌 §C-2) ·
> [`2026-07-17`](../../2026-07-17/industry_KR/SECTOR_DEEP_ENRG.md) (segment mix, Group III 병목 — **re-verified from source today, §5(d)**).
> **Analysis product. Zero buy/sell calls. Zero sizing (BET's job).** Blanks stay blanks. Every claim carries source + asof.
> **Inputs re-read from disk:** `MACRO_REPORT.md` §1/§2/§3a/§4a M-02/§4x(e) · `SWEEP_READ.md` §2 화학·건설/§4 shortlist ·
> `EVENT_ALPHA.md` Cards 1 & 4 · `SECTOR_ROTATION.md` §1 rank 1/§3/§4/§5 · `SECTOR_FLOW_KR.json` (829 names, 09:35).
> **Handoff ledger queried BEFORE analysis** (`module_report_tags ticker`, `DEGAJA_REPORT_DIR=llm_outputs`) —
> **096770 = 27 reports · 010950 = 28 · 475150 = 16 · 078930 = 20.** Prior desk verdicts inherited, not re-derived (§10).
> **Tools:** `module_flow`(KIS 20d 실측 + KRX 공매도, **10:02–10:03 KST intraday**) · `module_chart --read`(VERBATIM) ·
> `module_valuation` · `module_disclosure --days 60` + **OpenDART `document.xml` 원문** · **`module_business` (WORKED today
> after 3 failed runs — §5(d) is the first re-verified segment mix since 07-16)** · `module_industry_map` ·
> `module_news_data fts --scope domestic --kr` (NEWS API) · yfinance NYMEX 3-2-1 rebuild.
> ⚠ **RS20 IS CORRUPTED TODAY** (`^KS11` missing its 07-21 bar; +5~11pp board-wide inflation). **Nothing in this file
> ranks on RS20.** Ranking is on OBV state · KIS 외/기/개 actuals · KRX short · vol_surge · **own-price returns**.
> ⚠ **Everything is INTRADAY (~09:35–10:05 KST, a 35–65-minute session).** `vol_surge` is depressed board-wide.

---

## §0 ★★ THE ANSWER, UP FRONT — both halves of the assigned question

### (A) *"Does the ENRG long broaden from S-Oil alone to a 3-name complex?"*
> ### ▶ **IT ALREADY BROADENED — AND IT BROADENED BY LEAVING S-OIL BEHIND. The answer is "yes, but not to the three names ROTATION named, and not as one complex."**

**The measurement is today's own tape, and it is unambiguous** (own price, not RS — the benchmark is corrupt):

| Name | 07-21 close | **07-22 (10:0x)** | **1d** | vs **^KS11 +5.93%** | 1y high | dist. from high |
|---|---|---|---|---|---|---|
| **475150 SK이터닉스** | 55,900 | **68,100~68,700** | **+22.9%** | **+17.0pp** | 68,200 (04-03) | ★ **+0.0% — AT/THROUGH the record** |
| **078930 GS** | 82,500 | **85,400~85,900** | **+4.1%** | −1.8pp | 85,400 (**07-22**) | ★ **new 1-y high today** |
| **096770 SK이노베이션** | 116,300 | **119,400~120,900** | **+4.0%** | −1.9pp | 149,800 (04-29) | −20.3% |
| **010950 S-Oil** | 141,600 | **140,900~141,400** | ★ **−0.14%** | ★ **−6.1pp** | 146,700 (**07-20**) | −4.0% |

★ **S-Oil — the single name MACRO built the ENRG tactical-OW on, and the name ROTATION's question treats as the
anchor — is the ONLY one of the four that did not participate.** It topped on **07-20**, and it is now the sole
member of the complex that is red on a +5.93% index morning. This is the **second consecutive session** of it
(MACRO §2: *"S-Oil −0.07% today"* on 07-21 as well).

**Three further measured facts settle the shape of the "broadening":**
1. **The sweep's universe-relative tags do not say what the per-name tags say.** `module_flow` (per-name absolute
   scale) tags **all four 🟢가속**. `sector_flow` (829-name relative scale, `SECTOR_FLOW_KR.json` 09:35) tags
   **S-Oil 🟡중립 rank 59** and **GS 🟡중립 rank 104**, with only **SK이노 (rank 22)** and **SK이터닉스 (rank 24)**
   at 🟢. **This is the exact same two-scale disagreement SWEEP §6 #1 recorded for the FIN triple, and it resolves
   the same way: the ENRG green is TWO names on the universe scale, not four.**
2. **GS is the run's genuine upgrade and it reverses yesterday's downgrade.** 07-21: 🟡중립 / OBV **중립** / MA 혼조.
   Today: **🟢가속 / OBV 매집 (20d 기울기 +22% → +49%) / MA 강세스택 4/4 / new 1-year high.** The 07-21 file
   downgraded GS ("*the money left it while the thesis stayed*"). **That downgrade is withdrawn on today's
   measurement** — with one unresolved leg: **외국인 −58.5만 → −64.7만**, i.e. the foreign exit *deepened* while
   everything else turned. Institutions (+119.0 → +122.0만) and OBV did the turning.
3. **475150 did NOT broaden anything — the rest of its own value chain is being sold.** Every listed KR name at the
   renewable/offshore-wind nodes is 🟡/🔴 with OBV **분산** (§7). **세아제강**, the named 강관 supplier to
   **475150's own 신안우이 390MW** project, is rank **519/829, OBV 분산**. **두산퓨얼셀** (the listed peer to
   475150's SOFC leg) is rank **818/829, 🔴분산**. **One name is being bought; its chain is not.**

> **▶ VERDICT (A):** The **REFINING leg broadened for real** — 096770 + 078930 now both carry OBV 매집 + 기관 실매수
> + 개인 분산, and **it broadened away from 010950**, which topped 07-20 and has now underperformed the index on two
> consecutive sessions. **475150 did not join a complex; it detached from one** — +22.9% on **zero same-day news**
> (§3c) into an **all-time high** with a **fresh bearish RSI divergence** and a chain that is uniformly 분산.
> The 07-21 file's **two-bet** verdict is **CONFIRMED and sharpened**: Bet A is now best described as
> **096770 + 078930 (with 010950 fading out of the leadership)**, and Bet B (475150) is a **single-name event**,
> not a renewable-sector exposure. **The three names ROTATION listed are not the three names the tape selected.**

### (B) *"Does the new anti-print make a Red Sea / Hormuz disruption a COST to the KR refiner's own crude slate?"*
> ### ▶ **YES — AND I FOUND THE PRIMARY NUMBER, PLUS A SECOND ONE THAT MAKES IT NAME-SPECIFIC TO S-OIL. This is the most consequential finding in the file.**

**The industry number, quoted from the article body** [mt 2026-07-22, sourced to 정유업계 as of 07-21]:
> *"21일 정유업계에 따르면 지난 **1~5월 국내에 도입된 중동산 원유 비중은 62.8%**로 집계됐다. **2024년 71.5%,
> 2025년 69.1%**와 비교하면 2년도 안돼 10%포인트 가까이 떨어진 수치다. 지난 **2월28일 이란전쟁 발발** 이후
> 북미와 아프리카 등으로 원유 도입선을 다변화한 영향이다."*

| Middle-East crude share of KR imports | Value | Δ |
|---|---|---|
| 2024 | **71.5%** | — |
| 2025 | **69.1%** | −2.4pp |
| **2026 Jan–May** | **62.8%** | **−6.3pp vs 2025 · −8.7pp vs 2024** |

**And the cost, also quantified in the same body:**
- **Voyage days: 중동→한국 20~25일 vs 미국 걸프만→한국 40일 안팎** (**≈1.8× the sailing time**) → 용선료·연료비·보험료 all rise.
- ★★ **The freight subsidy that paid for the diversification EXPIRED ON 2026-06-30.** Quoted:
  > *"중동산 원유보다 추가로 발생하는 운임에 대해 전쟁 이전에는 약 **25%만 환급**했지만 **4~6월에는 …
  > 리터당 16원 범위 내에서 운임차액 전액(100%)을 지원**했다. 하지만 해당 조치가 **지난 6월말 종료**되면서
  > 현재는 환급률이 다시 기존 수준인 **25%로 돌아갔다**."*
  **→ 3Q26 is the first quarter in which KR refiners carry the full non-Middle-East freight differential at a 25%
  rebate. This is a dated, mechanical 3Q margin drag and it appears in NO other file in this run.**
- **Process cost, not just freight:** *"국내 정유시설은 그동안 **중동산 중질유를 중심으로 운영되도록 최적화**돼왔다 …
  성상이 다른 원유 비중이 확대되면서 **공정운영 난도가 크게 높아졌다** … 기존 비율대로 투입할 경우 **정제효율이
  떨어질 뿐 아니라 공정운영 자체에 문제가 발생**할 수 있는 탓이다."* Unquantified (no $/bbl figure exists in the source).

**★ And then the primary filing makes it name-specific — this is the part the news cannot see.**
`module_business 010950`, quoting S-Oil's own 사업보고서:
> *"당사의 최대주주는 **Aramco Overseas Company B.V.(AOC, 사우디아라비아 국영 석유회사인 Saudi Aramco의 종속회사)**로
> 총 지분의 **63.4%**를 보유하고 있습니다. 당사는 **장기원유공급계약**을 통하여 … **Saudi Aramco로부터 안정적으로
> 원유를 공급**받고 있으며…"*

Against `module_business 096770`, SK이노베이션's own 사업보고서:
> *"석유사업은 석유제품 생산을 위해 원유를 **중동 등 전 세계 다양한 공급망**을 통해 안정적으로 조달하며…"*
> plus a real upstream leg: *"**9개국 13개 광구 및 3개 LNG 프로젝트** … 2024년 말 확인 매장량 기준 총 **3.0억
> 석유환산배럴** … 2025년 지분 원유 분배 물량 **19.8백만 boe**, 일산 약 **54.2천 boe**."*

> **▶ VERDICT (B):** **The anti-print is correct, and the two refiners sit on OPPOSITE sides of it.**
> **The 62.8% industry average does not describe S-Oil.** S-Oil is **63.4%-owned by Saudi Aramco and buys its crude
> from its own controlling shareholder under a long-term supply contract** — it is, by its own filing, the KR
> refiner **structurally least able to diversify away from Middle-East crude**, and the Houthi action is
> specifically a **blockade of SAUDI ARABIA** (*"사우디 항구 이용 선박도 표적"*, EVENT_ALPHA Card 1).
> **SK이노베이션's filing describes a multi-source slate plus 3.0억 boe of its own reserves.**
> **→ A Red Sea / Saudi-port disruption is a crack-spread gift to SK이노베이션 and a two-sided event for S-Oil.**
> **That is a mechanism the desk has been treating as sector-uniform for five runs, and it is not.**
> ⚠ **What I could NOT measure (P4, stated as a blank): S-Oil's own Middle-East share is not disclosed as a number
> in any filing or article this desk can reach. 63.4% ownership + a long-term Aramco contract is a strong
> structural inference; it is NOT a percentage. I will not invent one.** The 62.8% is an industry aggregate.

---

## §1 ★ THE DELTA — six things changed since 07-21, and four of them cut against the position

1. **★★ 475150 +22.9% into an all-time high, on ZERO same-day news.** `fts 이터닉스 --days 1` returns **19 hits and
   not one of them is a 07-22 article about the company** — 18 are sedaily sidebar boilerplate repeating the
   **07-20** headline, and the single 07-22 item is an **mt retail tip column whose picks today are 대원전선·에스피지**,
   naming SK이터닉스 only as a prior call. **No DART filing today. No broker note. Named as unexplained, not invented**
   — the same discipline MACRO §1 applied to 삼성전기 +12.37%.
2. **★★ The 07-24 최고가격제 decision is now a presidential-level, dated, DIRECTIONAL negative — and it is 2 sessions
   away.** The 07-21 file called this *"the least-narrated risk, still unfired."* **It fired.** §4.
3. **★★ The Group III bottleneck got its first hard prices — and the SAME article carries the consensus that
   contradicts the bull case.** 그룹3 윤활기유 **≈$4,000/t**, 6월 수출 **$708.79M (+124.8% YoY)** — and
   **에프앤가이드 2Q OP QoQ: SK이노 −34.7%, S-Oil −24.1%.** §5(d), §6.
4. **★ GS's 07-21 downgrade is withdrawn; S-Oil's leadership is gone.** §0(A), §2.
5. **★ Two new primary-source items on the two largest names**, neither in yesterday's file: **국민연금 5.11% 신규
   대량보유 on 475150** [DART 07-01] and **SK차이나 유상감자 ₩9,000억 → SK이노 이사회 2026-07-30** [sedaily 단독 07-21]. §5.
6. **KPI #9 moved AWAY from firing.** 9월 원유 확보율 **74% (07-19) → 90%+**, 7~8월 **전년평균 대비 110%+**
   [산업통상부 양기욱 산업자원안보실장 via yonhap 07-21 11:30]. §8.

**Carried unchanged, explicitly:** the KKR SPA (strike ₩23,700, closing **07-31**), the conditional EGM **07-28**,
and the 100MW/25yr PPA — **`module_disclosure 475150 --days 60` shows no new filing since 2026-07-13.** The
07-21 file's §4(a)/(b) quotations stand as written and are **not re-printed here.**

---

## §2 Flow — measured delta vs 07-21 (`module_flow`, 10:02–10:03 KST intraday · KIS 20d 실측 · KRX 공매도)

| Name | 흐름 | OBV (20d 기울기) | RS60 | 서지 | 외 / 기 / 개 (만주, 20d) | 공매도 %float | own 20d / 60d |
|---|---|---|---|---|---|---|---|
| **096770 SK이노** | **🟢가속** | **매집 (+112% → +152%)** ▲ | **−21.7%** | **1.49×** ★board-top large-cap | **−33.0** / **+218.0** / −161.9 | 0.13% flat(−0.02) | +27.4% / **−10.9%** |
| **010950 S-Oil** | 🟢가속 *(sweep: 🟡, rank 59)* | 매집 (+39% → **+27%**) ▼ | **+12.6%** | **0.97×** | −14.9 / **+191.1** / −183.4 | **0.49% building(+0.04)** ⚠주목 | +38.8% / +23.5% |
| **475150 SK이터닉스** | **🟢가속** | **매집 (+22% → +37%)** ▲ | **+12.1%** | **1.58×** | **+20.8** / **+141.2** / −168.6 | **2.53% 🔥크라우디드 covering(−0.03)** | **+80.9%** / +23.8% |
| **078930 GS** | **🟢가속 ▲▲** | **매집 (중립 → +49%)** ▲▲ | +10.2% | 0.97× | **−64.7** ▼ / **+122.0** / −58.6 | 0.02% flat(+0.02) | +31.4% / +20.6% |

**Deltas that matter, ranked:**
- **★ GS reversed its own downgrade** (§0(A) point 2). The one leg that did **not** turn is foreign: **−58.5 → −64.7만**.
- **★ S-Oil's OBV slope decayed +39% → +27%** — still 매집, but the only one of the four decelerating, and its
  `vol_surge` is **0.97×** (no money surge) while SK이노 prints **1.49×** and 이터닉스 **1.58×**.
  ⚠ **Both surge figures are on a ~65-minute session and must be re-read at the close** (EVENT_ALPHA Card 4's own
  kill condition: *"the surge failing to hold ≥1.3× on a full-session re-read"*).
- **All four retain the real-hands signature** (기관 net-buy + 개인 net-sell). **It is the single strongest fact in
  the sector's favour and it is unchanged for a fifth run.**
- **475150's foreign leg held positive (+20.8만)** — still the only one of the four with foreigners net-buying,
  while SK이노 (−33.0) and GS (−64.7) both have foreigners leaving.
- ✅ **RS60 reconciliation (a divergence I owe the reader):** SWEEP carries 475150 rs60 **+2.0/+4.8%**, this file
  **+12.1%**. **It is not a module disagreement — it is the +22.9% intraday move between 09:35 and 10:03.**
  Own-price 60d = +23.8%; KOSPI 60d ≈ +10.5pp of that. Reconciled, not smoothed.

### 📊 CHART_READ — `module_chart <ticker>.KS --read` · **VERBATIM**
*(⚠ tool note: bare 6-digit tickers 404 on this module too — `.KS` required, same trap as `module_flow`.)*

**SK이노베이션 (096770)**
```
OBV: 누적(매수압력↑) (20d기울기 +152%)
다이버전스: 없음
MA정렬: 혼조 · 가격 4/4 MA 위
볼린저: 확장 38.2% · 중단
RSI: 68.6 · 모멘텀20d +22.6%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 89,500
```

**S-Oil (010950)**
```
OBV: 누적(매수압력↑) (20d기울기 +27%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 3/4 MA 위
볼린저: 확장 55.8% · 중단
RSI: 75.4 · 모멘텀20d +31.7%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>142,980 + OBV→누적 / 스탑(스윙저점): 93,200
```

**SK이터닉스 (475150)**
```
OBV: 누적(매수압력↑) (20d기울기 +37%)
다이버전스: 약세(가격 고점↑ · RSI 고점↓)
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 확장 59.3% · 상단밴드
RSI: 59.6 · 모멘텀20d +82.0%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 37,750
```

**GS (078930)**
```
OBV: 누적(매수압력↑) (20d기울기 +49%)
다이버전스: 없음
MA정렬: 강세스택(5>20>60>120) · 가격 4/4 MA 위
볼린저: 확장 37.3% · 중단
RSI: 69.3 · 모멘텀20d +30.1%
턴-판정: CONFIRMED-TURN (확인된 반전)
트리거(점화): close>—(전 MA 위) + OBV→누적 / 스탑(스윙저점): 62,500
```

★ **Three resolutions the chart delivers, two of them against the position:**
1. ★★ **475150 printed a BEARISH DIVERGENCE for the first time** (07-21: *다이버전스 없음*). At an all-time high,
   **RSI is only 59.6** — lower than the RSI at the April ₩68,200 peak. **Price made a higher high; momentum did not.**
   Its 턴-판정 upgraded PULLBACK-TO-SUPPORT → **CONFIRMED-TURN**, at the **상단밴드**, with 모멘텀20d **+48.3% → +82.0%**.
   **This resolves yesterday's "consolidation inside a completed +189% advance" — the consolidation broke UP.
   It is now a breakout to a record on a negative momentum divergence. Both halves belong in the same sentence.**
2. ★ **S-Oil LOST an MA (4/4 → 3/4 위) and a trigger reappeared: `close>142,980`.** Yesterday it had no trigger
   (전 MA 위). **It is the only one of the four that went backwards on structure**, consistent with §0(A).
3. **SK이노 gained an MA (3/4 → 4/4 위)** and its OBV slope is the steepest of the four (+152%).

---

## §3 The three names, one at a time — what today's evidence says about each

### (a) 096770 SK이노베이션 — **the leg with the most improving evidence and the least primary catalyst**
- **Flow:** the only large cap on the board with a genuine surge (1.49×), OBV slope +152%, 기관 **+218.0만**, short
  **0.13% flat** (effectively unshorted — no squeeze fuel and no bear).
- **But:** own 60d is **−10.9%**, RS60 **−21.7%** — **it is the only one of the four that has not outperformed on 60
  days**, and it is **−20.3% from its 04-29 high**. **The 🟢 is a 20-day phenomenon** (SWEEP §4 said exactly this).
- **Thread quality (EVENT_ALPHA Card 4's own named fragility, and I confirm it):** the thread is **two sell-side
  notes**, six days apart. `module_disclosure --days 60` returns **수주 0 / 실적 0 / 자본변동 0 / 자기주식 0** — 12
  filings, all 자회사 or 보고서 items. **There is no company event in this thread.**
- ★ **New today, and it lands on the same date as the earnings call:** [sedaily 단독 07-21 17:30] **SK차이나
  유상감자 ₩9,000억**. §5(b). **2026-07-30 is now a double event: 2Q 실적 컨콜 16:00 + 이사회.**

### (b) 010950 S-Oil — **the name the sector thesis is built on, and the name today's tape and today's filings both single out**
- Topped **07-20** at ₩146,700; **−0.14% today, −0.07% on 07-21** — two sessions of non-participation.
- OBV slope decaying (+39% → +27%); `vol_surge` **0.97×**; universe-relative tag **🟡중립, rank 59/829**.
- **Short 0.49% building for a fourth consecutive run** (0.44 → 0.48 → 0.49 → 0.49), still just under the ⚠주목 0.50 line.
- ★ **§0(B) is the fact that reframes it:** by its own filing it is **63.4% Saudi-Aramco-owned with a long-term
  Aramco crude contract**, while the Houthi action is a **Saudi** blockade. **The 07-21 file's short-interest read
  ("a short of the crude LEVEL, coherent with the TACO branch") now has a second, structural mechanism available
  to it — supply-chain concentration — and the 0.49% short has been building through all of it.**
- ⚠ **Counter, stated at equal weight:** S-Oil's **윤활 segment is where the money is.** 8.8% of revenue
  (₩3.01조 of ₩34.25조) produced **2Q OP ₩4,663억 (+180%) out of ₩9,283억 total OP ≈ half** [iM證 via mt 07-14,
  inherited]. **The Group III node (§6) is S-Oil's best asset and it is tightening, not loosening.**

### (c) 475150 SK이터닉스 — **an unexplained 22.9%, a record high, a bearish divergence, and a chain that is being sold**
- **Positive, measured:** OBV slope +22% → **+37%**; 외국인 **+20.8만** (only name of the four); 기관 **+141.2만**;
  short **2.53% 🔥크라우디드 covering**; a groundbreaking on its own named 390MW asset (§5(c)); NPS at 5.11% (§5(a)).
- **Negative, measured:**
  - **No same-day catalyst in 19 hits.** §1.1.
  - **Bearish RSI divergence at an all-time high.** §2.
  - **The chain is 분산.** §7 — the strongest single counter in this file.
  - **Consensus room is now negative:** 목표주가 **₩57,250** vs price **₩68,200** → **−16.1%**, at **Fwd PER 77 /
    PBR 8.55 / TTM PER 93.1** [`module_valuation`, 10:04]. **07-21 it was +2.42%. In one session the name went from
    "the sell-side is out of room" to "the price is 16% through the target."**
  - **Retail-broadcast naming is now on its FOURTH consecutive day:** [sedaily/chosun/yonhap 07-20 특징주 ×3] ·
    [mt 07-21 적중!대박예감] · [mt 07-21 오늘 이 종목/시선집중] · [mt 07-22 적중!대박예감, as a prior pick].
    ⚠ **And the framing is drifting** — the 07-21 mt column now calls it *"AI 데이터센터"*, a **fourth narrative
    wrapper** after 유가급등 수혜 / 신재생 정책 / KKR JV. **A name that accepts any story is a crowding observable.**
  - ★ **The revenue base does not look like a power producer.** From its own 사업보고서 (§5(d)):
    **전력판매(제품매출) = ₩15,348M of ₩385,641M revenue = 3.98%.** The largest line is **상품매출 44.6%
    (₩171,949M), and it SHRANK YoY from ₩230,698M.** **At PBR 8.55 the market is not paying for the current P&L.**
  - **mcap correction (checkable, and it matters for thresholds):** DART gives **의결권있는 발행주식총수
    34,067,004주** [20260701000185]. **34,067,004 × ₩68,200 = ₩2.32조** — cross-checks to `module_valuation`'s
    23,131억 at ₩67,900 to the decimal. ⚠ **`SECTOR_FLOW_KR.json` carries mcap ₩1.67조 at last=62,600, which implies
    26.68M shares — ~22% below the DART count. SWEEP, EVENT_ALPHA and ROTATION all inherited ₩1.67조.**
    **The name is ~₩2.3조 today — it has crossed the ~₩2조 sub-threshold the 07-21 file flagged.**

---

## §4 ★★ The 8차 최고가격제 — the 07-21 file's least-narrated risk fired, at presidential level, dated 07-24

**Quoted from [mt 2026-07-22] and [mt/뉴시스 07-21], 국무회의 2026-07-21:**
> **이재명 대통령:** *"중동상황이 다시 악화하고 있어 다시 경계심을 높여야 할 것같다 … **(최고가격제는) 원래 계획에
> 의하면 사실 더 내리든지 폐지됐어야 하는데 오히려 더 강화해야 할 것같다**"*
> **구윤철 부총리 겸 재정경제부 장관:** *"유가가 지금 올라가는 상황이어서 유가 상황까지 감안해서 결정하겠다"*

**The full schedule, on record for the first time in this desk's files:**

| 차수 | 적용 | 휘발유 | 경유 | 실내등유 |
|---|---|---|---|---|
| 1차 | 2026-03-13~ | 1,724 | 1,713 | 1,320 |
| 2차 | 2026-03-27~ | 1,934 | 1,923 | 1,530 |
| 3~6차 | — | **동결** | 동결 | 동결 |
| **7차 (현행)** | **2026-06-27~** | **1,784** | **1,773** | **1,380** (6차 대비 **−150원**) |
| **8차** | **★ 2026-07-24 (D+2)** | *pending* | *pending* | *pending* |

**Why the 7차 cut happened, and why it is about to reverse — in the ministry's own words** [산업통상부 via mt]:
> *"미국-이란 종전 MOU 합의 이후 유조선의 호르무즈해협 통항 사례가 증가하는 등 중동정세의 불확실성이 다소
> 줄어든 상황 … 국제유가 하락분을 선제적으로 반영해 최고가격을 인하하기로 했다."*
**Brent: 2026-07-01 $71.6 → 2026-07-20 $90.3 = +26.1%** [구윤철 국무회의 보고]. **The input cost that justified the
−150원 cut has fully reversed, and the government is signalling it will TIGHTEN the output price ceiling.**

★★ **This is the cleanest, nearest, and least-priced negative in the file, and it lands on the DOMESTIC
distribution node — the one node the crack spread cannot reach.** It also has an unresolved P&L tail:
[mt 07-20] *"**최고가격제로 인한 손실 보전 확정 절차도 아직 남아있다**"* — **the compensation for prior ceiling
losses is not yet fixed.**

**Narrative velocity, measured (this is MACRO §4x(e)'s assignment, answered):**

| Term | 1d | 2d | 3d | 5d | 7d | Read |
|---|---|---|---|---|---|---|
| **최고가격제** | **20** | 25 | 27 | 31 | **31** | ★★ **65% of the entire week printed in the last 24 hours. Zero new hits between 5d and 7d.** |
| **중동산** | **9** | 10 | 11 | 13 | 14 | ★ **64% in one day** |
| **해상봉쇄** | 5 | 8 | 8 | 14 | **30** | the working synonym (홍해/후티/예멘반군/선박보호/홍해봉쇄 all = **0**, trigram-dead) |
| 정제마진 | 5 | 5 | 5 | 6 | 7 | ★ **flat all week — the margin story is NOT what is being written** |
| 윤활기유 | 2 | 3 | 3 | 3 | 4 | thin |

> **▶ RESOLUTION of MACRO §4x(e) ("is bucket 4's −28.2% real attention loss, or trigram blindness?"):**
> **NEITHER, exactly — and the third answer is the useful one. Attention did not leave ENRG; it ROTATED inside it,
> from the margin leg to the policy/cost leg.** 정제마진 is **flat at 5–7 all week** while 최고가격제 went
> **0 → 20 in a day** and 중동산 **5 → 9**. The bucket-4 terms are a **margin-and-geopolitics** vocabulary; the news
> is now writing a **cost-and-price-control** story. **The −28.2% is partly index blindness (해상봉쇄 is the only
> working geopolitical term) and partly a genuine, measurable topic rotation — into the leg that is NEGATIVE for
> the refiners.** **Scoring it as "attention loss" would have been wrong in a way that flattered the position.**

---

## §5 ★ IR / primary-filing anchor — two new items, one re-verified segment mix

### (a) 475150 — **국민연금공단 crossed 5%, and it did so by open-market purchase** *(NEW — not in the 07-21 file)*
**[DART 20260701000185, 주식등의대량보유상황보고서(약식), 제출 2026-07-01, 보고기준일 2026-06-23]** — from the filing:

| Field | Value |
|---|---|
| 보고자 | **국민연금공단 / 국민연금기금** (연기금등 전문투자자) |
| 보고구분 | **신규** |
| 직전보고 (2026-06-22) | 1,702,461주 = **5.00%** |
| **이번보고 (2026-06-23)** | **1,740,358주 = 5.11%** (증감 +37,897주 / +0.11pp) |
| 변동방법 / 보유목적 | **장내매수 / 단순투자** |
| **의결권있는 발행주식총수** | **34,067,004주** |

★ **Two uses.** (1) It puts a **name** on part of the 기관 +141.2만 — NPS, buying on-market, 단순투자, not a
strategic or deal-related holder. (2) The share count **corrects the mcap** (§3(c)) and re-checks the 07-21 file's
derived count (33.75M from 10,455,825 ÷ 30.98%) → **the true count is 34,067,004, so SK디스커버리's block is 30.69%.**
The **KKR strike of ≈₩23,700 is unaffected** (247,800,000,000 ÷ 10,455,825).
⚠ **Freshness caveat:** 기준일 **2026-06-23** — one month stale, and it precedes both the +80.9% 20-day move and
the 07-31 closing. **It says nothing about whether NPS still holds 5.11% today.**

### (b) 096770 — **SK차이나 유상감자 ₩9,000억, 이사회 2026-07-30** *(NEW — single-outlet, no filing)*
**[sedaily 단독 2026-07-21 17:30, IB 업계]** — quoted:
> *"**SK온은 22일, SK이노베이션은 30일** 각각 이사회를 열어 해외 투자 법인 지분구조 변경에 관한 안건을 의결할
> 계획이다 … SK차이나에 대한 지분 축소로 약 **9000억 원**을 국내로 가져오는 유상감자다 … SK이노베이션 계열의
> 지분은 **33%에서 10% 수준**으로 줄어들고 … **SK차이나의 유보금은 1조 원이 넘는 것으로 알려졌다**."*
> Use of proceeds, per the article: *"인공지능(AI) 산업의 성장에 따라 전력 수요가 급증하면서 **에너지 분야에 대한
> 투자를 확대**하기 위해서다 … **전력과 에너지솔루션 분야**에 투자할 것으로 보고 있다."*

★ **Why it matters:** **2026-07-30 becomes a double event for 096770** — the 2Q 실적 컨콜 (16:00, **[DART
20260716800628]**, confirmed still on file today) **plus** the board resolution. And **the stated use of proceeds
puts SK이노베이션 on the AI-power axis, not the refining axis** — which is a *different* thesis from the one
MACRO/EVENT_ALPHA are carrying.
⚠⚠ **Discipline check, applied against this desk's own standard:** this is **one outlet, [단독], sourced to
"IB 업계", with NO DART filing.** EVENT_ALPHA Card 5 downgraded the **LG엔솔 [단독]** to **STORY-ONLY** on exactly
this basis. **The same rule applies here: this is not a confirmed capital event. It is a dated, falsifiable claim
that DART settles on 07-30.**
⚠ **One factual error inside the same article, corrected against the filing (P1):** it writes *"**SK㈜**는 KKR와
국내 최대 신재생에너지 합작법인(JV)을 설립하기로 했다."* **The DART filing names the seller as 에스케이디스커버리㈜
→ Eclipse Holdco L.P.** [20260630801211]. **The 07-21 file's structural correction stands; the press does not.**

### (c) 475150 — **its own named 390MW asset broke ground, with sovereign policy financing** *(NEW)*
**[mt/yonhap 2026-07-20] 신안군, '신안우이 해상풍력 발전사업' 착공** — 총사업비 **₩3.4조**, **15MW 터빈 26기 =
390MW**, 김성환 기후부 장관 참석, and: *"정부의 **'국민성장펀드 제1호 메가 프로젝트'로 선정**돼 대규모 정책금융
지원을 받는다."*
★ **The link is a filing link, not a headline link** — the article never names SK이터닉스; **the company's own
사업보고서 does:** *"**신안우이(390MW)** 및 굴업도(755MW) 등 총 **1.3GW** 규모의 해상 풍력 파이프라인."*
⚠ **P4 blank, stated:** **the filing says "파이프라인." It does not state SK이터닉스's equity share, role, or
economics in 신안우이. I cannot size the benefit and will not guess.** This is a real catalyst of **unknown magnitude.**

### (d) ★ Segment mix — **RE-VERIFIED FROM PRIMARY SOURCE for the first time since 07-16** (`module_business` worked)
The 07-21 file recorded this as an open data-quality item for a **third consecutive run** (*"still 07-16 DART
inheritance and was NOT re-verified"*). **`module_business` ran cleanly today on all three names. The item is closed.**

**S-Oil 010950** — 사업보고서, 생산능력 표:
| 부문 | 주요 제품 | 매출액 | 비중 |
|---|---|---|---|
| 정유 | 휘발유·경유·항공유 | ₩27,005,329백만 | **78.8%** |
| **윤활** | **윤활기유·윤활유** | ₩3,007,417백만 | **8.8%** |
| 석유화학 | 방향족·올레핀 | ₩4,234,211백만 | 12.4% |
| 합계 | | **₩34,246,957백만** | 100.0% |
**→ The 07-16/07-17 inheritance (78.8 / 8.8 / 12.4) is CONFIRMED exact.** ★ And the asymmetry is now explicit:
**8.8% of revenue is carrying ~50% of 2Q operating profit.**

**SK이노베이션 096770** — 사업보고서 (2025년 4분기 누적):
석유 **₩47.19조 (59%)** · E&S CIC **₩11.86조 (15%)** · 화학 **₩8.92조 (11%)** · 배터리 **₩6.98조 (9%)** ·
윤활유 **₩3.84조 (5%)** · 석유개발 ₩1.37조 · 소재 ₩840억.
**→ 07-16's "석유 59%" CONFIRMED exact.** ★ **41% of SK이노베이션's revenue is not refining** — LNG/전력 (E&S)
alone is 15%, i.e. **larger than its battery business**. **"SK이노 = a refiner" is a 59% statement.**

**SK이터닉스 475150** — 사업보고서, 보고부문·매출유형별 (제2기):
| 부문 | 유형 | 금액(백만) | 비중 |
|---|---|---|---|
| 신재생에너지 | **상품매출** | **171,949** | **44.6%** (제1기 230,698 = 69.5% → **shrinking**) |
| 신재생에너지 | 용역수입 | 82,541 | 21.4% (제1기 7.8% → **growing**) |
| 신재생에너지 | 공사수입 | 80,770 | 20.9% (제1기 10.8% → **growing**) |
| 신재생에너지 | **제품매출(전력판매)** | **13,600** | **3.5%** |
| ESS | 용역수입 | 35,033 | 9.1% |
| ESS | 제품매출(전력판매) | 1,748 | 0.5% |
| **합계** | | **385,641** | 100.0% |
★ **전력판매 합계 = ₩15,348백만 = 3.98% of revenue.** The company is, on its own numbers, primarily a
**개발·시공·용역·트레이딩** business, not an IPP. **Asset base (filing):** 태양광 솔라닉스 1~3호 **120MW** (5호 추진) ·
풍력 군위풍백 **75MW** 준공 + 직접 PPA · 해상풍력 파이프라인 **1.3GW** (신안우이 390 + 굴업도 755) ·
연료전지 SOFC 충주에코파크 **40MW** 상업운전 + 대소원 40 + 파주 31 → **누적 200MW+ 예정** ·
ESS **국내 1위, 795MWh** + 텍사스 100MW + 제주 표선 BESS 40MW · VPP 확장.

### (e) Valuation (`module_valuation 010950 --peers "096770,078930,475150"`, asof 2026-07-22 ~10:04 intraday)
| 코드 | 종목 | 현재가 | 시총(억) | PER(TTM) | PER(Fwd) | PBR | 목표주가 | 상승여력% | 외인% | 배당% |
|---|---|---|---|---|---|---|---|---|---|
| 010950 | S-Oil | 141,600 | 159,417 | 17.52 | **7** | 1.72 | 159,000 | **+12.29** | **79.75** | 0.23 |
| 096770 | SK이노베이션 | 120,200 | 203,201 | — | 9 | **0.86** | 170,917 | **+42.19** | 14.34 | 1.66 |
| 078930 | GS | 86,100 | 79,983 | 6.19 | **5** | **0.53** | 103,000 | +19.63 | 20.35 | **3.48** |
| **475150** | **SK이터닉스** | **67,900** | **23,131** | **93.14** | **77** | **8.55** | 57,250 | ★ **−15.68** | 3.76 | — |

★ **The single largest valuation delta in the run: 475150's 상승여력 went +2.42% (07-21) → −15.68% in one session,
with Fwd PER 64 → 77 and PBR 7.04 → 8.55.** **The sell-side is not out of room; the price is through the room.**
GS's 상승여력 **fell** +24.85% → +19.63% (price rose into a static target) while SK이노's **fell** +46.96% → +42.19%.

---

## §6 Value chain — **by reference**, plus the three nodes that moved and the binding constraint

**Carried unchanged from [07-20 §D](../../2026-07-20/industry_KR/SECTOR_DEEP_ENRG.md) — not re-printed:** the 7-node
map, the "not a bottleneck" list ([3] 정제 capacity, [5] 에틸렌 과잉, [7] 수출), `module_industry_map` clusters.
`module_industry_map 정유 윤활기유 원유도입 신재생` re-run today reproduces the same partition:
**Cluster #2 = {010950 S-Oil, 014530 극동유화, 017940 E1, 018670 SK가스}** · **#3 = {034730 SK, 096770 SK이노,
006120 SK디스커버리}** · **#4 = {078930 GS, 004990 롯데지주}** · **#5 = {003650 미창석유공업, 004250 엔피씨}**.

```
[1] 원유조달          [2] 해상수송        [3] 정제         [4] 윤활기유 GrIII   [5] 석유화학   [6] 국내유통      [7] 수출
    ★★ COST 신규         ★ 통항              중립              ★★★ 최대구속          과잉         ★★ 규제 신규       확대
 중동산 62.8%          중동 20~25d        정제효율↓         $4,000/t (3.2×)       —          8차 07-24        6월 윤활기유
 (24년 71.5%)         美걸프 40d         배합 재검증        SK엔무브+S-Oil            대통령 "강화"     $708.79M
 운임환급 100→25%      ↑용선·보험         FnGuide 2Q         = 세계 GrIII 40%                   현행 1,784원      (+124.8% YoY)
 (6/30 종료)                            −34.7% / −24.1%    완성차 인증=진입장벽
```

- ★★★ **BINDING CONSTRAINT = [4] 윤활기유 Group III, and it is now quantified — a genuine physical bottleneck,
  not "strong demand."** From [mt 07-20], quoted:
  > *"최근 국제 고성능(**그룹3**) 윤활기유 가격은 **톤당 4000달러를 육박**하는 수준까지 치솟았다 … 올해 초
  > **톤당 1000달러대 초중반**에 거래됐던 것과 비교하면 … **3배 이상 급등** … **SK이노베이션의 자회사 SK엔무브와
  > 에쓰오일(S-OIL)은 글로벌 그룹3 윤활기유 생산의 약 40%**를 담당해왔다 … 지난달 한국의 윤활기유 수출액은
  > **7억879만달러로 사상 최대** … 지난해 같은 달(**3억1533만달러**)과 비교하면 **두 배 이상**"*
  **Why it is a BINDING constraint and not just strong demand — the supply-side reasons are named:**
  (i) *"카타르의 **펄 GTL**, 사우디아라비아의 **사다라** 등 중동 주요 생산기지가 가동에 차질"*;
  (ii) refiners are **shifting yield to light products** (휘발유·항공유), structurally reducing heavy-cut GrIII output;
  (iii) ★ **the real barrier: "그룹3 윤활기유는 완성차 업체의 **품질 인증**까지 거쳐야 해 공급처를 단기간에
  대체하기도 쉽지 않다."** **A certification-gated node with 40% concentrated in two Korean producers is a moat,
  and it is the node that is neither the crude level nor the crack spread** — i.e. the one node the 07-21 file's
  correlation panel showed the price does not track. **Derived: +124.8% YoY export value, ~3.2× price.**
- ★★ **[6] 국내유통 became a SECOND binding node today, from the regulatory side.** §4. **Ceiling tightening into a
  +26.1% input cost is a direct domestic-margin compression, and it is the only node with a hard date (07-24).**
- ★ **[1] 원유조달 flipped from a supply risk to a COST.** §0(B). Two-sided by name: **S-Oil (Aramco 63.4% +
  장기공급계약) vs SK이노 (다변화 + 3.0억 boe 자체 매장량).**
- **[2] 해상수송 — the government says it is not binding, in its own words** [산업통상부 양기욱 실장 via yonhap 07-21]:
  *"7∼8월 원유는 전년 평균 대비 **110% 이상** 확보했으며 **9월 도입 원유도 … 전년 대비 90% 이상** 확보 … **홍해가
  막히더라도 특별한 문제는 없을 것** … 홍해에서 현재까지 **정상 운행** … (문제가 생기면) **수에즈 운하 등 다른
  대체 수단**"*. **KPI #9 moved from 74% to 90%+.**
- **[3] 정제 — the margin node's global print is intact but the KR P&L print is not.** [yonhap 07-21 10:01]:
  3-2-1 ≈**$70/bbl** (07-20), 유럽 경유 마진 ≈**$65/bbl** 사상 최고, 북서유럽 ≈**$30/bbl**, IEA 2Q 생산 **−500만 b/d**,
  Kpler 6월 역내 수출 **≈100만 b/d = 전쟁 전의 1/4**, 미국 2019년 이후 **120만~130만 b/d 영구 폐쇄**.
  ★ **New in the same body, and it contradicts a 07-22 op-ed: "최근 미·이란 갈등이 재차 격화하면서 통행이 다시 막힌
  상태다"** — Hormuz is **blocked again**. **[donga 07-22 기고, 에너지경제연구원 김태환 석유정책연구실장] opens
  "호르무즈 해협이 다시 열렸다. 국제유가는 전쟁 이전 수준으로 내려앉았고" — that premise is stale against
  BZ=F $91.67 (07-21) and against yonhap's own 07-21 line. Flagged rather than used.**
  ⚠ **And the same article's other half is a warning worth carrying:** *"2022년 러시아-우크라이나 전쟁으로
  러시아산 도입이 끊기자 **중동 의존도는 60% 선에서 2년 만에 72%로 되돌아갔다**"* — **the 62.8% diversification
  has a documented precedent of fully mean-reverting once the crisis passes.**

---

## §7 Chain-hop candidates — body-proximate only, each with the mandatory flow cross-check

**Rule applied:** never headline-named in the sector's own thread; a news co-mention alone is **not** a candidate;
**every one gets a flow cross-check before it may reach BET.** Ranks are `SECTOR_FLOW_KR.json` (829 names, 09:35).

| # | Candidate | Body-proximate link (not headline) | **Flow cross-check** | **Verdict** |
|---|---|---|---|---|
| 1 | **306200 세아제강** (0.34조) | [sedaily 07-20] **신안우이 해상풍력에 강관 납품, "국내 단일 프로젝트 기준 최대 수준"** — the physical supplier to 475150's own filed 390MW asset | rank **519/829**, flow −0.21, 🟡중립, **OBV 분산**, rs60 **−25.6%**, surge 0.55× | ❌ **FAILS. Money is leaving it.** |
| 2 | **100090 SK오션플랜트** (0.84조) | 해상풍력 하부구조물 — same node | rank 168, flow +0.34, 🟡중립, **OBV 매집**, rs60 **−52.0%**, surge 0.49× | ⚠ **the only 매집 in the chain, but rs60 −52% and no surge. NOT confirmed.** |
| 3 | **336260 두산퓨얼셀** (2.97조) | listed peer to 475150's SOFC leg (충주 40MW 상업운전, 누적 200MW+) | rank **818/829**, flow **−0.93, 🔴분산**, OBV 분산, surge 0.43× | ❌❌ **FAILS hardest.** |
| 4 | **112610 씨에스윈드** (1.75조) | 풍력 타워 | rank 402, 🟡중립, **OBV 분산**, rs60 −54.3% | ❌ **FAILS.** |
| 5 | **009830 한화솔루션** (5.49조) | 태양광 — and [yonhap 07-20] **유상증자 1.2조 확정, 당초 계획의 절반 수준** | rank 487, 🟡중립, **OBV 분산**, rs60 −53.7% | ❌ **FAILS, with a dilution fact attached.** |
| 6 | **003650 미창석유공업** (0.24조) | `industry_map` Cluster #5 — 윤활유 blender, i.e. the **downstream of the binding node [4]** | `module_flow`: **🟢가속, OBV 매집, rs60 +9.2%**; sweep: rank **105**, 🟡중립, surge 0.92×, short **0.2% building** | ⚠ **PARTIAL — the only hop whose flow does not fail.** But **0.24조 mcap** sits inside SWEEP §3's micro-cap speculation signature and **far below the ~₩2조 players floor. Handed as an OBSERVATION, not a candidate.** |
| 7 | 014530 극동유화 (0.11조) · 017940 E1 · 018670 SK가스 | `industry_map` Cluster #2 (S-Oil's own cluster) | ranks 313 / 369 / 261, all 🟡중립, **all OBV 중립**, rs60 −31.0 / −23.4 / −18.7 | ❌ **FAIL — the cluster is not being bought.** |
| 8 | 267250 HD현대 (15.57조) | HD현대오일뱅크 (unlisted) is the 4th refiner; [sedaily 07-21] 윤활유 플래그십 스토어 | rank **501**, 🟡중립, **OBV 분산**, rs60 −33.4%, 기관 **−7.9만** | ❌ **FAILS — and it is the cleanest control in the file.** |

> ★★ **The hop table IS the finding, and it points two ways at once.**
> **(i) The refining hop fails everywhere except one 0.24조 blender** — including **HD현대 (the 4th KR refiner) at
> rank 501 with OBV 분산.** **If this were a sector-wide refining-margin trade, HD현대 would not be at rank 501.
> The money is in TWO tickers (096770, 078930) plus a fading third (010950), not in "정유."**
> **(ii) The renewable hop fails everywhere, without exception.** Six chain names, **five OBV 분산**, ranks
> 168–818. **475150 is +22.9% into a record while its entire physical value chain is being distributed.**
> **This is the strongest single piece of evidence in the file that Bet B is a name event, not a sector.**
> **Per SWEEP §5(h)'s own failure-class-#4 rule (narrative-sourced vehicles), NO name in this table may reach BET
> on a co-mention. Only #6 survives the flow test, and it fails the scale test.**
> ⚠ `chain-hop` itself remains **not run as evidence** — its universe is hardcoded `us_top300` and returns 0/0 on
> KR themes (07-20 §H, unchanged). **Not a negative result; a capability gap.**

---

## §8 Track KPIs — observable, dated, each able to fire

| # | KPI | **Now (07-22)** | Was (07-21) | What fires it |
|---|---|---|---|---|
| **1** ★★ | **8차 석유 최고가격 고시 — 2026-07-24 (D+2)** | ★ **대통령 "오히려 더 강화" (국무회의 07-21)**; 현행 7차 휘발유 1,784 / 경유 1,773 / 등유 1,380 | *"unfired, least-narrated"* | **인상/강화** = domestic node [6] compressed into a +26.1% input cost. **동결** = neutral. **인하/폐지** = the president was overruled |
| **2** ★★ | **SK이노 2Q 컨콜 + 이사회 — [DART] 2026-07-30 16:00** | ★ **consensus SHAPE now known: FnGuide 2Q OP QoQ SK이노 −34.7%, S-Oil −24.1%** [mt 07-20]; 1Q 정유4사 합산 ≈₩6조 | 하나證 연간 OP ₩6.5조 | **A 정유 segment beat vs −34.7% QoQ** = the sell-side case survives its first primary print. **A miss** = falsified with a number. **Plus** the ₩9,000억 유상감자 board item |
| **3** ★★ | **475150 임시주총 — [DART] 2026-07-28 09:00** (KKR 이사 2인, **정지조건부**) | **unchanged — no new filing since 07-13** | same | **Resolution passes → SPA closing. Auto-voids → SPA terminated.** Binary, free, 4 sessions |
| **4** ★ | **475150 SPA 거래종결 — [DART] 2026-07-31** (already slipped 06-30 → 07-31) | strike **₩23,700** vs price **₩68,200** = **+187.8%** | +135.9% | **A second slip** = execution risk on Bet B's one contracted driver |
| **5** ★★ | **475150 — does the +22.9% acquire a reason?** | ★ **ZERO same-day articles about the company in 19 hits; no DART filing** | +0% day, explained | **A catalyst prints within 2 sessions** = real. **Nothing prints and the move retraces** = it was the 4th-day retail-tip signature |
| **6** ★ | **US 3-2-1 crack (NYMEX proxy, rebuilt today)** | **$62.16 (07-21), 95.7th pct of 187** | desk printed **$63.36** same-day | **Two consecutive closes < $60** = margin cycle rolled. ⚠ **the series revised −$1.20 after the fact — see §10** |
| **7** ★ | **Group III 윤활기유** | **≈$4,000/t (≈3.2× YTD)**; 6월 수출 **$708.79M, +124.8% YoY**; SK엔무브+S-Oil = **세계 40%** | 미상 | **Price back < $2,500/t, or 카타르 펄GTL / 사우디 사다라 restart** = the binding constraint releases |
| **8** ★ | **중동산 원유 비중 + 운임 환급률** | **62.8% (1~5월)**; ★ **환급 100% → 25%, 2026-06-30 종료** | 미상 | **Rebound toward 70%** (the 2022 precedent: 60%→72% in 2y) = the diversification cost reverses. **환급 재개** = the 3Q drag is removed |
| **9** | **9월 원유 도입 확보율** | ★ **90%+** (7~8월 **110%+**) [산업통상부 07-21] | **74%** | **<80%** = node [1] re-binds. **Moved AWAY from firing** |
| **10** | **475150 공매도** | **2.53% 🔥크라우디드 covering(−0.03)** — unchanged | 2.53% covering | **Covers through 07-28/07-31** = event positioning. **Rebuilds after** = directional |
| **11** | **S-Oil 공매도** | **0.49% building(+0.04)** — **4th consecutive run below the line** | 0.49% building | **≥0.50%** = ⚠주목 crossed. **Covering** = the short capitulated |
| **12** ★ | **S-Oil relative participation** | ★ **−0.07% (07-21), −0.14% (07-22) vs index +5.93%** — 2 sessions; topped 07-20 | board-best RS | **A third under-delivery on an up day** = MACRO M-02's own stated reclassification test ("a shelter tell") fires |
| **13** | **GS 078930 re-confirmation** | ★ **🟡→🟢, OBV 중립→매집(+49%), new 1-y high** — 07-21's downgrade withdrawn | 🟡중립, OBV 중립 | **외국인 (−64.7만, still deepening) turning** = fully confirmed. **OBV back to 중립** = the reversal was one session |
| **14** | **Ceasefire signature** — MACRO §4a M-02 both branches | Hormuz **"통행이 다시 막힌 상태"** [yonhap 07-21]; BZ=F **91.67** | live proposal rejected | **Signature** = the crude-level driver cuts. ⚠ WTI COT 10%ile crowded-SHORT (stale) = a ceasefire removes the bid |
| **15** | **475150 mcap / SECTOR_FLOW data integrity** | **DART 34,067,004주 → ₩2.32조**; sweep carries **₩1.67조** (implies 26.68M shares) | 07-21 flagged ₩1.67 vs ₩1.90조 | **Sweep mcap uncorrected next run** = the ≥1조 shortlist floor and ~2.5조 players floor are both being applied to a wrong denominator |

---

## §9 Anti-signals — as observables, ranked by proximity

1. **★★ 8차 최고가격제, 2026-07-24, with the president on record saying "강화."** The nearest dated negative in the
   file, on the one node no margin metric covers, into Brent **+26.1% since 07-01**, with the prior ceiling-loss
   compensation **still unfixed**. *Observable: the 산업부 고시 on 07-24.* **§4.**
2. **★★ The 2Q consensus is a ~third QoQ DECLINE, and the desk has been carrying "사상 최대" for five runs.**
   **FnGuide: SK이노 −34.7%, S-Oil −24.1% QoQ**, on **역래깅** [mt 07-20]. The 하나證 "연간 OP ₩6.5조 (+1,505% YoY)"
   and this are not contradictory — but **07-30 reports the quarter, not the year.**
   ⚠ **Symmetric ammunition, stated:** the 2Q 역래깅 came from *falling* crude in 2Q. **Crude rose +26.1% in 3Q to
   date, which mechanically reverses inventory effects.** **Both branches carried.**
3. **★★ 475150 is +22.9% into an all-time high with (a) zero same-day news, (b) a fresh bearish RSI divergence at
   the 상단밴드, (c) a price 16.1% THROUGH consensus target at PBR 8.55 / Fwd PER 77, (d) a fourth consecutive day
   of retail-broadcast naming with a drifting story (유가→신재생→KKR→"AI 데이터센터"), and (e) a value chain in
   which 5 of 6 listed peers are OBV 분산.** *Observable: KPI 5 — does a reason print within 2 sessions?*
4. **★★ The Middle-East configuration cost is real, dated, and name-specific to the desk's anchor name.**
   중동산 62.8%; **운임 환급 100% → 25% from 2026-07-01**; 40일 vs 20~25일 voyages; 정제효율 저하.
   **And S-Oil is 63.4% Aramco with a long-term Aramco supply contract.** *Observable: KPI 8.* **§0(B).**
5. **★ S-Oil has now under-delivered on two consecutive up days and topped on 07-20**, while its OBV slope decays
   (+39% → +27%), its `vol_surge` is 0.97×, it lost an MA, and the universe-relative sweep tags it **🟡 rank 59**.
   **The name the ENRG OW was built on is the name leaving the leadership.** *Observable: KPI 12.*
6. **★ Zero 수주 / 실적 / 자본변동 filings across 096770, 010950 and 475150 in 60 days.** SK이노 12 filings, S-Oil 7,
   이터닉스 9 — **all 보고서·자회사·주총 items. The entire Bet A case is still sell-side + tape**, exactly as 07-21
   recorded. **07-30 remains the first primary print.**
7. **★ The chain-hop table fails 7 of 8, including HD현대 (the 4th refiner) at rank 501 OBV 분산.** A sector thesis
   whose fourth-largest participant is being distributed is a two-name thesis. *Observable: §7.*
8. **The KKR strike ₩23,700 vs a ₩68,200 market = +187.8%** (was +135.9% yesterday). **The gap widened by 52pp in one
   session.** No premium-tender catalyst exists at these levels; the strike is **March-dated** and is not a valuation
   claim. *Observable: any revised consideration in a 정정공시.*
9. **The SK차이나 ₩9,000억 item is a single-outlet [단독] with no filing** — and this desk downgraded the LG엔솔
   [단독] to STORY-ONLY on the same basis today. *Observable: DART on 07-30.* **§5(b).**
10. **The diversification has a documented mean-reversion precedent:** 2022 러-우 전쟁 후 중동 의존도 **60% → 72%
    in two years** [donga 07-22, 에너지경제연구원]. *Observable: KPI 8.*
11. **Latent, unchanged and NOT re-verified this run:** 검찰 정유4사 26조 유가담합 (07-06, 재부상 07-20) ·
    **SKIET 매각설 재공시 2026-12-09** [DART 20260610800638] · 샤힌 에틸렌 180만t vs 울산 구조조정 (07-20 §C-2).
12. ⚠ **The crack proxy revised against me.** The 07-21 desk published **$63.36** for 07-21; the identical
    construction re-pulled today prints **$62.16** for the same date. **KPI 6's "$60" threshold is being evaluated on
    a series that moves ~$1.2 after the fact.** The 07-21 file's structural caveat also stands unresolved:
    **the 3-2-1 is a US Gulf construct; S-Oil is paid on the Singapore/Dubai complex, which this desk cannot measure.**

---

## §10 Tool limits · data quality (P4)

- ✅ **`module_business` WORKED on all three names — the 07-20/07-21 breakage (`FileNotFoundError: news_alert.db`)
  did not recur.** **The three-run-old open item ("segment mix is 07-16 inheritance, not re-verified") is CLOSED**,
  and the inherited figures were **confirmed exact** (§5(d)). ⚠ **S-Oil and 475150 still return
  `매출 표 추출: FAIL`** — their numbers were read out of the raw `section_text`, not the parsed table.
- ✅ **`.KS` suffix required on `module_chart` too** — bare 6-digit tickers return `404 Quote not found` /
  `possibly delisted`. **This is not documented alongside the known `module_flow` trap. Worth adding.**
- ⚠ **`SECTOR_FLOW_KR.json` mcap for 475150 (₩1.67조) is inconsistent with DART's 34,067,004주 and with
  `module_valuation`** (which agrees with DART to the decimal). **SWEEP/EVENT_ALPHA/ROTATION all inherited ₩1.67조.**
  KPI 15.
- ⚠ **Two flow scales disagree by design and the disagreement was not flagged upstream:** `module_flow` (per-name)
  tags all four **🟢가속**; `sector_flow` (universe-relative) tags **S-Oil 🟡 rank 59** and **GS 🟡 rank 104**.
  **Both are correct on their own scale.** This file names which scale each claim uses.
- **`module_flow` 뉴스속도 = n/a on all four names** — fifth consecutive run, same root cause. Narrative velocity in
  §4 was measured with `fts --count` ladders instead.
- ⚠ **KR FTS is a trigram index and the assigned dead terms were re-verified dead:** `홍해` `후티` `예멘반군`
  `선박보호` `홍해봉쇄` = **0 each**. `해상봉쇄` **= 30 (7d)** works. **`9월` (2 chars) also returns 0** — a search
  for the September-crude article failed twice before I dropped the 2-char token. **All terms passed as separate
  argv; `--scope domestic` on every call.**
- ⚠ **The `--days N` ladder is not a clean daily histogram** (해상봉쇄 5d=14 → 7d=30 implies heavy hits on 07-15/16,
  before the thread began). **Reported as raw cumulative counts, not converted into a fake per-day velocity.**
- **`fetch_disclosure_detail_all()` still returns `[detail] 0건 본문 파싱 완료`** for every name — the 07-21 bug is
  unfixed. **§5(a) was parsed by fetching OpenDART `document.xml` directly and decoding the ZIP** (works, HTTP 200).
- **Oil complex has NO 07-22 bar yet** in yfinance (last row = 07-21: CL 84.78 / BZ 91.67). ⚠ **MACRO §1's
  "CL=F 84.72 (+1.79%)" is the 07-21 print measured against 07-20 — the KR session today is trading on 07-21 oil.**
- **Singapore/Dubai complex refining margin: 미상.** No module carries it. Anti-signal 12.
- **S-Oil's own Middle-East crude share: 미상.** Not disclosed in any filing or article reachable here. §0(B).
- **475150's equity share/economics in 신안우이 390MW: 미상.** The filing says "파이프라인" only. §5(c).
- **CFTC COT (WTI 10%ile crowded-short) = inherited from MACRO, not re-pulled; stale by 3~4d. Context, not a trigger.**
- **Ledger inherited, not re-derived** [`module_report_tags`, `DEGAJA_REPORT_DIR=llm_outputs`]:
  **096770 = 27 reports** (latest verdict chain CONFIRMED / FADING / RESOLVED, 07-21 DEEP-ENRG) ·
  **010950 = 28** (same) · **475150 = 16** (07-21 DEEP-ENRG, CONFIRMED FADING RESOLVED 🟡) ·
  **078930 = 20** (07-21 DEEP-ENRG). **Per the standing rule the prior verdicts are carried forward; this file
  amends only what today's measurement changed, and says so each time it does (§0(A) GS, §3(c) 475150 base).**
- **No correlation panel re-run this file.** The 07-21 panel (residualised r 0.788, 475150 90.9% idiosyncratic,
  risk-contribution table) is **carried by reference**; a one-session +22.9% outlier would distort a 20-day
  correlation and produce a spurious update. **Stated rather than silently skipped.**

---

_Generated 2026-07-22 · DEEP-ENRG (CONTINUOUS, 5th run · DELTA-LED) · `module_flow`(KIS/KRX 실측, 10:02 intraday) ·
`module_chart --read`(VERBATIM) · `module_valuation` · `module_business` (re-verified) · `module_disclosure --days 60`
\+ OpenDART 원문 · `module_industry_map` · `module_news_data fts`(NEWS API) · `module_report_tags` · yfinance.
**Zero buy/sell calls. Zero sizing. TACO both branches carried. RS20 never used. Blanks left blank.**_
