# SWEEP_READ — industry_KR · 2026-07-21 (Tue)

> Stage 2 / L1·SWEEP (Phase 0.5). Universe-wide flow BEFORE rotation — orient from money, then name things.
> Data: `sector_flow.py --market kr --json` (universe `kr_all`, **829 of 832 names**, asof 2026-07-21)
> → `SECTOR_FLOW_KR.json`; then **serially** `kr_live_shortlist.py --floor-jo 1 --top 15`
> → `KR_LIVE_SHORTLIST.json` (KIS per-investor 20d actuals = the KR edge axis).
> Cross-check target: `MACRO_REPORT.md` §4 transmission matrix. **The sweep cross-checks the matrix; it
> never replaces it** (flow = money now, matrix = why).

---

## §0 Universe state — the number that frames everything below

| | Value |
|---|---|
| Names swept | **829** (of 832 requested; 3 unresolved) |
| **Universe wflow** | **−0.283** |
| 🟢 green / 🔴 red | **43 / 56** |
| **new-🟢 ignitions** | **7** — and **not one is ≥₩1조 in the sectors the matrix is long** |

**Read: this was a +3.56% index day inside a −25.97%/1m de-rating, and the universe-wide flow is still
negative with red outnumbering green 56:43.** MACRO's core framing survives the bounce. **The bounce did
not produce ignitions where the matrix is positioned** — the 7 new-🟢 are ₩0.02–0.80조 micro/small caps
(SNT홀딩스, 국도화학, 티엠씨, 효성ITX, 오리엔트바이오, 티비에이치글로벌, 에이엔피), **six of the seven with
RS60 between −11% and −60%** — i.e. **oversold-bounce ignitions, not new leadership.**

⚠ **Do not read "7 ignitions" as breadth.** Every one carries a negative RS60. An ignition off a −60%
six-month base is a mean-reversion print until it holds.

---

## §1 Sector rotation sweep — all 28 KRX sectors, ranked by wflow

| # | Sector | n | **wflow** | eqflow | 🟢/🔴 | breadth | **Δ** | Read vs MACRO §4 |
|---|---|---|---|---|---|---|---|---|
| 1 | 미분류 | 2 | +0.912 | +0.718 | 1/0 | 0.50 | −0.027 | ⚠ n=2, ignore |
| **2** | **제약** | **48** | **+0.352** | +0.120 | **5/0** | 0.10 | **+0.145** | ★★ **CONFIRMS HLTH OW.** Best real sector, **best Δ on the board**, **zero red in 48 names** |
| 3 | 부동산 | 3 | +0.322 | +0.445 | 1/1 | 0.33 | 0.000 | ⚠ n=3, ignore |
| **4** | **운송·창고** | **24** | **+0.272** | +0.058 | **2/0** | 0.08 | **+0.078** | ★ **NOT IN THE MATRIX.** See §3 — this is the Red Sea leg |
| 5 | 섬유·의류 | 27 | +0.146 | +0.267 | **5/0** | 0.19 | −0.006 | eqflow > wflow = **breadth-led**, zero red. K-fashion/consumer, unowned |
| 6 | 의료·정밀기기 | 8 | +0.138 | −0.128 | 0/0 | 0.00 | −0.032 | Mega-cap only (케이씨텍 RS60 **+77.1**) |
| 7 | **화학** | **103** | **+0.131** | +0.046 | 5/4 | 0.05 | +0.015 | ⚠ **Contains the refiners** — see §2. Sector label hides the signal |
| 8 | 종이·목재 | 17 | +0.124 | +0.180 | 1/0 | 0.06 | +0.041 | — |
| 9 | 음식료·담배 | 37 | +0.113 | +0.185 | 4/1 | 0.11 | +0.034 | ⚠ **CONTRADICTS STPL UW** — breadth-led positive. See §4 |
| 10 | 비금속 | 21 | +0.091 | +0.081 | 1/1 | 0.05 | −0.007 | — |
| 11 | 전기·가스 | 10 | +0.060 | −0.008 | 0/0 | 0.00 | +0.030 | Mildly positive — consistent with 한전 기관 +221만 (MACRO §2) |
| 12 | 통신 | 5 | +0.051 | −0.020 | 0/0 | 0.00 | +0.029 | COMM Neutral, confirmed as *nothing* |
| 13 | 제조 | 8 | −0.021 | +0.143 | 1/1 | 0.12 | **+0.173** | Best Δ after 제약; n=8 |
| 14 | 리츠 | 22 | −0.024 | +0.041 | 0/0 | 0.00 | **+0.109** | ⚠ **RE UW's first counter-signal** — Δ +0.109 with real 10Y easing |
| 15 | 오락·문화 | 13 | −0.032 | −0.075 | 0/2 | 0.00 | +0.017 | — |
| **16** | **금융** | **76** | **−0.041** | **+0.057** | 2/3 | 0.03 | **−0.136** | ★★ **CONTRADICTS FIN OW at sector level.** Worst Δ on the board. See §2 |
| 17 | 일반서비스 | 33 | −0.097 | −0.018 | 2/2 | 0.06 | +0.093 | — |
| 18 | 증권 | 18 | −0.135 | −0.224 | 0/0 | 0.00 | +0.088 | Confirms *"고점서 −40% 하락한 증권주"* (MACRO §3a) |
| 19 | 외국증권 | 1 | −0.172 | −0.172 | 0/0 | 0.00 | +0.028 | n=1 |
| **20** | **금속** | **60** | **−0.212** | −0.068 | 3/3 | 0.05 | +0.001 | ✅ **CONFIRMS MATR UW.** Δ ≈ 0 on the day the K-철강 AI story ran again |
| 21 | 인프라투용 | 1 | −0.250 | −0.250 | 0/0 | 0.00 | −0.022 | n=1 |
| 22 | **보험** | 12 | **−0.264** | −0.055 | **0/2** | 0.00 | +0.015 | ★ FIN's weak leg (⚠ but DB손보 individually 매집 — §2) |
| 23 | IT 서비스 | 26 | −0.264 | −0.124 | 0/2 | 0.00 | +0.054 | 현대오토에버 **flow −1.00, 서지 0.29×** — the board's deadest large name |
| 24 | **건설** | 28 | **−0.268** | **+0.089** | 2/1 | 0.07 | +0.039 | ★ **wflow≪eqflow — the exact split MACRO §4 #9 demanded.** Mega-cap builders dead, breadth alive |
| 25 | 운송장비·부품 | 60 | −0.296 | −0.091 | **1/5** | 0.02 | +0.061 | ✅ **CONFIRMS DISC UW + INDU downgrade** (조선·자동차 both live here) |
| 26 | 유통 | 63 | −0.338 | **+0.068** | 4/2 | 0.06 | −0.063 | 쿠팡 화재 / 홈플러스 — mega-cap distribution broken, breadth positive |
| 27 | 기계·장비 | 32 | **−0.395** | −0.170 | **0/4** | 0.00 | +0.095 | ✅ **CONFIRMS M-03 kill-switch** — the capex-equipment lane, zero green |
| **28** | **전기·전자** | **69** | **−0.398** | **−0.314** | **3/22** | 0.04 | +0.022 | ★★ **WORST SECTOR, 22 red — on the day 삼성전자 rose 6%.** See §2 |

---

## §2 ★ The three places the sweep CORRECTS or SHARPENS the matrix

### (a) ★★ FIN — the sector says UW, the three banks say OW. **Both are true, and that is the finding.**
**금융 wflow −0.041 with the board's worst Δ (−0.136)**, 보험 **−0.264 (0 green / 2 red)**, 증권 **−0.135**.
**Yet the top-flow table is full of banks:** **KB금융 +0.71 매집 RS20 +36.8**, **하나금융 +0.69 매집 +36.7
(서지 1.16×)**, **신한지주 +0.54 매집 +33.3**, **케이뱅크 +0.71 매집**, **DB손해보험 +0.67 매집 RS20 +40.4**.

**Resolution: MACRO's FIN OW is a 3–5 NAME call wearing a sector label.** The 76-name 금융 sector is
**net-negative and deteriorating fastest on the board** — the money is going into large banks *and coming
out of everything else financial*. **This is a dispersion trade, not a sector trade.**
⚠ **Consequence for ROTATION: an index/sector expression of FIN OW (금융 ETF) would buy the −0.136 Δ.**
The MACRO tilt survives; **the vehicle does not.** Named here so BET cannot quietly express it as a sector.
⚠ Note the honest counter to my own §1 line: **보험 is −0.264 at sector level while DB손해보험 is 매집 with
RS20 +40.4** — the same dispersion one level down. Do not short the insurance label either.

### (b) ★★ IT/전기·전자 — the worst sector on the board (**3 green vs 22 red**) on a +6% 삼성전자 day. **But the redness is NOT memory.**
Bottom-of-board by flow_score (≥₩1조), and read what they actually are:
| Ticker | Name | flow | RS60 | 서지 | What it is |
|---|---|---|---|---|---|
| 450080 | 에코프로머티 | −0.91 | **−65.5%** | 0.56 | **2차전지 소재** |
| 066970 | 엘앤에프 | −0.87 | **−63.5%** | 0.63 | **2차전지 소재** |
| 020150 | 롯데에너지머티리얼즈 | −0.96 | **−52.9%** | 0.47 | **2차전지 소재** |
| 454910 | 두산로보틱스 | **−1.00** | −36.6% | **0.31** | 로봇 |
| 336260 | 두산퓨얼셀 | −0.98 | −17.0% | 0.44 | 연료전지 |
| 307950 | 현대오토에버 | **−1.00** | −20.5% | **0.29** | IT서비스 |
| 000990 | DB하이텍 | −0.88 | −19.8% | 0.44 | 파운드리(레거시) |
| 011070 | LG이노텍 | −0.94 | +42.4% | 0.51 | 부품 |

**Not one of these is a memory name.** 삼성전자 and SK하이닉스 sit in the middle of the sector, not the
bottom. **The "worst sector in KR" is the battery-materials + robotics/fuel-cell complex**, whose RS60s
(−53% to −66%) are far worse than memory's. **MACRO's IT Neutral is not contradicted by the −0.398 wflow —
it is a different animal wearing the same GICS bucket.**
★ **New finding for ROTATION/DEEP: there is a distinct, unowned, ₩10조+ 2차전지-소재 wreck inside 전기·전자
that no MACRO proposition covers.** Related: **블랙록이 에코프로 지분 5.01%(₩5,000억) 보유** [MACRO §3a, 2 outlets]
— a global allocator buying into a −65% RS60 complex. Flagged, not tilted (**M-05's rule: story without 서지
is a story** — every name above is **서지 < 0.65×**).

### (c) ★★ ENRG — the sweep found a **second, larger** refining leg that MACRO missed
**096770 SK이노베이션 — ₩18.44조, flow_score +1.00, 🟢가속, OBV 매집, RS20 +42.0%, 서지 1.69× (highest of
any large-cap 🟢 on the board), KIS 20d: 외국인 −31만 / 기관 +205만 / 개인 −152만 → ✅진짜손.**
MACRO's M-02 carried **S-Oil alone** (RS20 +58.3, 서지 1.14×). **SK이노베이션 is a bigger vehicle with a
higher volume surge and the same real-hands verdict** — and it sits in the **화학** GICS bucket, which is
why a sector-level read missed it. **The 화학 sector's +0.131 wflow is substantially these two names.**
⚠ Both are refiners; **this is concentration, not diversification** — same crack-spread driver, same TACO
kill-switch. **It widens the vehicle choice, not the thesis.**

---

## §3 ★ The one genuinely new lane the sweep surfaced: **운송·창고 (shipping/logistics)**

**Sector: wflow +0.272, Δ +0.078, 2🟢/0🔴 — 4th best on the board and absent from MACRO §4.**
- **011200 HMM — ₩18.48조, flow +0.65, OBV 매집, RS20 +28.8%**, 서지 0.97×
- **003490 대한항공 — ₩9.56조, flow +0.65, OBV 매집, RS20 +19.7%**, 서지 0.97×

★ **This is M-02's missing value-chain layer.** MACRO recorded the Red Sea vector as an *oil-price* input
(홍해 봉쇄 위협 [19a/7s], 사우디 선박 보호조치 [9a/2s], Goldman $120). **A Red Sea blockade is also, and
more directly, a FREIGHT-RATE event** — rerouting around the Cape lengthens voyages, tightens tonnage, and
lifts container/tanker rates. **HMM accumulating at RS20 +28.8% is that transmission, and the desk never
named it.**
⚠ **Two-sided, and the anti-branch is the same one as M-02's:** a ceasefire that reopens Red Sea transit
deflates freight rates *and* crude together — **HMM is not a hedge against the TACO trigger, it is a second
expression of the same bet.** Do not size it as diversification.
⚠ 대한항공 cuts the other way on the same input: **higher jet fuel is an airline cost** (cf. MACRO §3a:
라이언에어 순이익 −34% on 고유가). **HMM (rate beneficiary) and 대한항공 (fuel victim) accumulating
simultaneously is a divergence, not a theme.** Handed to DEEP.

---

## §4 Where the sweep DISAGREES with the matrix (must be resolved downstream, not smoothed)

| # | Matrix says | Sweep says | Owner |
|---|---|---|---|
| **(a)** | **FIN OW ★highest conviction** | **금융 wflow −0.041, Δ −0.136 (worst on board)**; 보험 −0.264, 증권 −0.135 | **ROTATION** — keep the tilt, **forbid a sector-ETF expression** (§2a) |
| **(b)** | **STPL UW** (나프타 cost-push) | **음식료·담배 wflow +0.113, eqflow +0.185, 4🟢/1🔴, Δ +0.034** — breadth-led positive | **ROTATION.** The cost-push thesis is 2-outlet news; the flow is 37 names positive. **The flow is the harder evidence** |
| **(c)** | **RE UW (most rate-negative)** | **리츠 Δ +0.109** (3rd-best Δ), 부동산 +0.322 (n=3) | **DEEP.** Real 10Y fell 4bp; the UW's own driver eased. ⚠ Same unresolved divergence the US desk carries on XLRE — **two desks, two runs, nobody has resolved it** |
| **(d)** | **INDU Neutral (split)** | **건설 wflow −0.268 but eqflow +0.089** | ✅ **Not a disagreement — a confirmation of MACRO's own instruction** to separate 건설 order-flow from RE asset. Mega-cap builders are dead; the breadth is where the LH/군사시설보호구역 order-flow lands |
| **(e)** | — (not covered) | **운송·창고 +0.272, HMM 매집** | **DEEP** (§3) |
| **(f)** | — (not covered) | **2차전지 소재 complex at RS60 −53~−66%, 서지 <0.65×** | **DEEP** (§2b) |

---

## §5 ★ LIVE SHORTLIST — wide sweep → filter → KIS actuals
`kr_live_shortlist.py --floor-jo 1 --top 15` → **filter (시총 ≥₩1조 · tag 🟢가속 · flow desc top15) yielded
only 4 names.** ⚠ **That is itself the headline: on a +3.56% index day, exactly four ≥₩1조 names were
🟢가속.** Breadth did not participate in the bounce.

| Ticker | Name | flow | OBV | RS20 | 외국인 | 기관 | 개인 | Verdict |
|---|---|---|---|---|---|---|---|---|
| **096770.KS** | **SK이노베이션** | **+1.00** | +0.18 | **+42.0** | −31만 | **+205만** | −152만 | ✅ **진짜손** |
| **475150.KS** | **SK이터닉스** | **+1.00** | +0.42 | **+65.4** | **+22만** | **+144만** | −173만 | ✅ **진짜손 (both sides buying)** |
| **089860.KS** | **롯데렌탈** | **+1.00** | +0.25 | **+53.6** | −4만 | **+12만** | −8만 | ✅ **진짜손** (small absolute flows) |
| 073240.KS | 금호타이어 | +0.84 | +0.53 | +60.3 | **−829만** | **−451만** | **+1,318만** | ❌ **약한손 — textbook 개인 흡수** |

**★ 진짜 LIVE (🟢 AND foreign/institution net-buying): SK이노베이션 · SK이터닉스 · 롯데렌탈.**

- **SK이노베이션** — see §2c. The run's single best large-cap flow print; **it is an ENRG/refining
  expression, which means the LIVE list and the matrix's #2 tilt agree.**
- **SK이터닉스 (475150, ₩1.67조, 건설 bucket, RS20 +65.4%, RS60 −0.6%, 서지 1.60×, both sides buying)** —
  ★ **the only name on the board with a flat RS60 and an accelerating RS20**, i.e. a *base* rather than a
  bounce. It is an **energy-solutions/renewables** developer sitting in the 건설 bucket — **which is exactly
  the eqflow-positive breadth §1 #24 and §4(d) flagged.** ⚠ **Unowned by any MACRO proposition.** → DEEP.
- **롯데렌탈** — 일반서비스, RS60 +3.6%. Absolute KIS flows are tiny (+12만 institutional); **the ✅ verdict
  is technically true and materially thin.** Recorded with that caveat rather than promoted.
- **금호타이어 is the cautionary row and the reason this filter exists:** flow +0.84, OBV +0.53, RS20 +60.3%
  — **every price/OBV signal says buy, and the KIS actuals say 외국인 −829만 + 기관 −451만 vs 개인 +1,318만.**
  **Without the KR edge axis this name reads as a top-5 idea.** The US desk has no equivalent check.

---

## §6 ★ Resolving the two items MACRO escalated to SWEEP

### (a) §4x(d) — **ADR venue substitution: RESOLVED. It is real, it is large, and it splits the two memory names.**
MACRO carried this unresolved for two runs. **The measurement:**
- **"SK하이닉스 ADR, 美반도체 약세에도 본주 대비 '25% 프리미엄'"** [yonhap, 07-19]
- **"'SK하닉 ADR을 담아라'…국내 11개 액티브 ETF에 편입"** [yonhap, 07-19] ← ★ **domestic Korean funds are
  buying the ADR instead of the 원주**
- Listing sequence: 나스닥 상장 07-13 → **원주 −15.4% (역대 최대) 같은 날**, ADR −9.3% → ADR **+27%** 07-14 →
  바클레이스 *"ADR 2배 상승 여력"*, 젠슨황 *"믿을 수 없을 정도로 성공적"*, *"2009년 엔비디아처럼 저평가"*
- 000660.KS: **−37.10% over 1 month**, +4.08% today, 5d volume ≈ 20d average (1.02×)
- **삼성전자, ADR 상장 가능성에 "검토 안 해"** [yonhap 07-14] — vs 블룸버그 *"발행 검토 중"* [mt]

**Verdict: a security trading at a 25% PREMIUM to its home line, with domestic funds migrating into it, is
not a thesis exit — it is a venue migration.** A thesis exit prices the ADR at a *discount*.
**★ Therefore MACRO §2's "both memory names show the same weak-hands pattern" is WRONG, and the two must
be split:**
- **SK하이닉스 — the foreign −815만주 domestic exit is substantially MECHANICAL (venue), not directional.**
  The weak-hands disqualifier should be **discounted, not applied at full weight**. Its RS20 deterioration
  (−6.6% → −11.1%) is measured **against a benchmark that does not contain its own ADR.**
- **삼성전자 — no ADR exists (company denies it). Its foreign −4,238만주 vs 개인 +3,765만주 has NO venue
  explanation and stands at full weight.**
**This inverts the intuitive ranking: the name MACRO treated as healthier (삼전, 🟡중립) has the *cleaner
bearish* flow signal; the name it treated as worse (하이닉스, 🔴분산) has the *contaminated* one.**
→ **Handed to DEEP-IT and to M-04's gate: the gate condition must be restated per-name, not per-pair.**

### (b) §4x(c) — memory gate: **the sweep does not open it, and adds one fact against.**
전기·전자 is the **worst sector (3🟢/22🔴)** and neither memory name is 🟢. 하이닉스 today: **+4.08% on
5d volume 1.02× (average)**. **삼전 +6% on 서지 0.89×.** **A 4–6% up-day on average-or-below volume, in the
board's worst sector, is not an ignition.** M-04's volume-qualified condition (서지 >1.3× + 20d foreign flip
+ 하이닉스 RS20 > −5%, three sessions) **remains unmet.** ⚠ **With the caveat from (a): the 하이닉스 RS20
leg of that condition is now known to be venue-contaminated and must be re-specified by DEEP.**

---

## ✅ EXIT CHECK
- [x] **sector_flow sweep done** → `llm_outputs/2026-07-21/industry_KR/SECTOR_FLOW_KR.json` (829/832 names,
      asof 2026-07-21). **All 28 sectors ranked and read** (§1), **wflow vs eqflow divergences named**
      (건설 −0.268/+0.089, 유통 −0.338/+0.068, 금융 −0.041/+0.057), **7 new-🟢 ignitions read and
      characterised as oversold bounces, not leadership** (§0).
- [x] **LIVE_SHORTLIST written** → `KR_LIVE_SHORTLIST.json`. **4 names passed the ≥₩1조 + 🟢가속 filter;
      3 verdicted 진짜손, 1 약한손 (금호타이어 — 외국인 −829만 + 기관 −451만 vs 개인 +1,318만).**
      Real-hands verdicts read per name (§5).
- [x] **(US-only) CYCLE_EXPOSURE — N/A for industry_kr** (protocol: "No CYCLE_EXPOSURE / ACTION_TICKETS").
      Explicitly declined, not skipped.
- [x] **Cross-checked against the matrix, disagreements NAMED not smoothed** (§4): FIN sector-vs-name
      dispersion, STPL flow-vs-thesis, RE 리츠 Δ, plus two lanes the matrix does not cover
      (운송·창고 §3, 2차전지 소재 §2b).
- [x] **Both items MACRO escalated to SWEEP were TAKEN, not deferred a third time** (§6): the ADR
      venue-substitution question is **resolved with a measured 25% premium** and **splits M-04 per name**;
      the memory gate is **re-tested and remains closed** on volume.

⚠ **Field notes for the unit (new this run):**
- `kr_live_shortlist.py` takes **`--floor-jo`** (조), **not** `--floor-b` (the US script's flag). Passing the
  US flag is an `unrecognized arguments` hard error — noisy, so it fails safe.
- Piping `sector_flow.py --json` into `head` raises **BrokenPipeError** after it has already emitted valid
  JSON. **Redirect to the file first, then read** — a stage that treated the traceback as failure would
  have re-run a multi-minute sweep for nothing.
- **The serial dependency held**: sweep → file → shortlist. Confirmed, no JSONDecodeError.

**→ proceed to EVENT_ALPHA.**
