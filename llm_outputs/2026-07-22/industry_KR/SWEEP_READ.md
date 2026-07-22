# SWEEP_READ — industry_KR · 2026-07-22 (Wed)

> Stage 2 / 7 · L1·SWEEP. Phase 0.5 — quantify **where the money actually flows** across the whole
> universe BEFORE rotation names anything (anti-tunnel).
> Artifacts: `SECTOR_FLOW_KR.json` (829 names / 28 sectors) · `KR_LIVE_SHORTLIST.json` (3 names).
> Serial dependency honoured: sweep ran to completion, then shortlist.
> ⚠ Sweep asof **2026-07-22 intraday (~09:35)** — a 35-minute session, not a close.

---

## ⚠ CARRIED TRAP — §4x(a) from MACRO, and it applies to THIS stage's output too

MACRO found `^KS11` is **missing its 2026-07-21 bar** in yfinance while every constituent has it, so
bar-count RS is inflated 5–11pp. **`sector_flow.py` computes `rs20` the same way.** Verified on this
stage's own output:

| Name | `SECTOR_FLOW_KR.json` rs20 | MACRO date-aligned rs20 |
|---|---|---|
| 삼성전자 | **10.1** | **−0.9** |
| SK하이닉스 | −0.3 | **−9.8** |
| 현대차 | 5.7 | **−4.2** |
| 한화오션 | 2.2 | **−6.5** |
| S-Oil | 61.1 | **+53.2** |

**Every `rs20` quoted below is the file's raw value and carries roughly +5 to +11pp of inflation.**
`rs60` is materially unaffected (1 missing bar of 61) and is the RS column to trust today.
**Disposition of §4x(a): ACKNOWLEDGED and BOUNDED — this stage ranks on `flow_score` / `obv_state` /
`vol_surge` / KIS actuals, none of which touch the benchmark. RS is used for context only.**

---

## §1 ★ THE HEADLINE FINDING — a +5.93% index morning produced **ZERO** flow ignitions

```
universe: 829 names · wflow −0.073 · 🟢 27 · 🔴 29 · NEW-🟢 ignitions: 0
```

**Not one name in 829 flipped to 🟢 today.** Day-over-day ignition is the sweep's early-cycle tell,
and on the second day of a **+9.7% two-session bounce** it read **zero**.

**This is the stage's most important output and it directly constrains ROTATION:** the bounce is not
being funded by new money entering names. Cross-reads that agree, from three independent instruments:
- **MACRO §3c bucket 3** (`코스피 외국인순매수 공매도 레버리지ETF 신용융자`) was the **only** bucket to
  rise in absolute level (+0.7% on a −9.0% pool = **+9.7pp**) — the market is talking about its own
  mechanics, not its fundamentals.
- **MACRO §2**: 삼전 20d 외국인 **−4,013만주**, 하이닉스 **−722만주** — unchanged in direction.
- **This stage §3**: the 🟢 list is a **micro-cap speculation signature** (below).

⚠ **Honest caveat: the session is 35 minutes old and `vol_surge` is depressed board-wide** (the FIN
triple reads 0.73–0.91×). A late-session re-run could produce ignitions. **The zero is recorded as
"no ignition as of 09:35", not "no ignition today."**

---

## §2 Sector rotation — universe-wide (`sector_flow --market kr`)

| Rank | Sector | n | **wflow** | **eqflow** | 🟢/🔴 | breadth | **delta (ignition)** | Read |
|---|---|---|---|---|---|---|---|---|
| 1 | 제약 | 48 | **+0.305** | +0.118 | 4/0 | 0.08 | −0.046 | ★ **#1 real sector. wflow > eqflow = MEGA-CAP-LED → this IS 삼바+셀트리온**, not the 4 micro-caps. **Independently confirms MACRO's HLTH-as-shelter flow** |
| 2 | 의료·정밀기기 | 8 | +0.206 | −0.065 | 0/0 | 0.00 | +0.068 | Narrow; n=8 |
| 3 | 섬유·의류 | 27 | +0.188 | +0.238 | 3/0 | 0.11 | +0.042 | Breadth-led micro-cap |
| 4 | 운송·창고 | 24 | +0.174 | −0.016 | 1/1 | 0.04 | −0.099 | Mega-cap-narrow |
| 5 | **화학** | 103 | **+0.157** | +0.031 | 2/2 | 0.02 | +0.026 | ★★ **This is NOT chemicals — it is the ENERGY complex.** S-Oil and **SK이노베이션 (18.4조, rank 22, 🟢)** are both classified 화학. **The sweep independently reproduces MACRO's ENRG tactical OW from the other direction** |
| … | 전기·가스 | 10 | +0.066 | −0.019 | **0/0** | 0.00 | +0.006 | ★ **UTIL: flat, zero greens, no ignition.** MACRO's UW confirmed universe-wide |
| … | **금융** | **76** | **−0.000** | +0.059 | **0/1** | 0.00 | +0.041 | ★★ **THE STAGE'S SHARPEST TENSION WITH MACRO. The sector averages ZERO and has ZERO 🟢 names across 76 constituents** — while MACRO carries FIN as its OW on three specific banks. See §4 |
| … | 건설 | 28 | −0.027 | **+0.136** | 2/0 | 0.07 | **+0.241** | ★ **2nd-largest ignition delta, breadth-led (eqflow ≫ wflow).** Contains **SK이터닉스 (1.67조, 🟢, real-hands)** — renewable-energy developer, i.e. **partly ENERGY again** |
| … | 유통 | 63 | −0.197 | +0.082 | 4/1 | 0.06 | +0.141 | Breadth-led; all 4 greens are micro-cap |
| … | **전기·전자** | **69** | −0.086 | **−0.217** | **2/13** | 0.03 | **+0.312** | ★★ **The board's WORST breadth (eqflow −0.217, 13 reds) AND its LARGEST ignition delta.** Exactly the "gate rattling, not opening" shape: mega-caps improving, the other 67 names not |
| … | 증권 | 18 | −0.086 | −0.178 | 0/0 | 0.00 | +0.049 | Matches 미래에셋 목표가↓ [4a/3s] |
| … | 보험 | 12 | −0.204 | +0.028 | 0/0 | 0.00 | +0.060 | ★ Matches the blindspot row *"보험정책 4전 전패"* — a FIN sub-lane nothing else surfaced |
| … | **금속** | 60 | **−0.247** | −0.081 | 1/2 | 0.02 | −0.035 | ★ **MATR UW confirmed universe-wide, 4th run.** 2nd-worst wflow, and the **only** major sector with a NEGATIVE delta |
| … | **기계·장비** | 32 | **−0.257** | −0.083 | 0/0 | 0.00 | +0.137 | ★ **Worst wflow of any large sector — and 두산에너빌리티 (rank 781) and 두산로보틱스 (rank 793) both live here** |
| … | 운송장비·부품 | 60 | −0.186 | −0.052 | 1/1 | 0.02 | +0.110 | 조선·자동차 parts. 한화오션 rank 568, 현대차 rank 758 |

---

## §3 ★ The 🟢 list is a **micro-cap speculation signature**, and that is a warning, not an opportunity

Of the **27 🟢가속** names in 829, the top-25 by flow_score are almost entirely **0.02–0.26조** with
`vol_surge` **1.5–7.2×** on a 35-minute session:

```
티엠씨 0.26조(2.70×) · 자이에스앤디 0.19조(2.83×) · 현대약품 0.15조(2.88×) · 한독 0.11조(1.85×)
샘표식품 0.10조(5.24×) · 삼성공조 0.08조(2.79×) · 신일전자 0.08조(2.73×) · 한성기업 0.06조(4.52×)
대구백화점 0.06조(2.27×) · 깨끗한나라 0.05조(7.24×) · 모나미 0.04조(5.09×) · 명문제약 0.04조(4.88×)
```

**Only THREE names ≥1조 carry 🟢가속 in the entire universe** — and they are the shortlist below.

★ **Read it against §1: money is surging into 0.05조 품절주 at 5–7× volume while producing zero new
large-cap ignitions.** That is a late-panic breadth signature, and it is the mechanical explanation for
MACRO §1's observation that **"the leadership inverted — the weak-hands names led and the flow-confirmed
names lagged"** (삼성전기 **+12.37%** while ranking **802/829** on flow, 🔴분산, RS20 −4.6).

**★ The single cleanest illustration in the whole run: the day's biggest gainer is the universe's
3rd-worst flow score.** Any stage that ranks on today's price change will invert this desk's evidence.

---

## §4 LIVE SHORTLIST — `KR_LIVE_SHORTLIST.json` (floor 1.0조 · 🟢가속 · KIS 20d actuals)

| Ticker | Name | Sector | mcap | flow | OBV | rs20 ⚠ | 외국인 | 기관 | 개인 | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|
| **096770.KS** | **SK이노베이션** | 화학 (**=ENRG**) | **18.44조** | **+0.93** (rank **22/829**) | **매집** +0.24 | 49.5 | −33만 | **+218만** | **−162만** | ✅ **real-hands · `vol_surge` 1.48× — the only genuine surge among large caps** |
| **475150.KS** | **SK이터닉스** | 건설 (**=renewable ENRG**) | 1.67조 | +0.92 | **매집** +0.46 | 87.8 | **+21만** | **+141만** | **−169만** | ✅ **real-hands, BOTH foreign and institution net-buying** |
| **089860.KS** | **롯데렌탈** | 일반서비스 (DISC) | 1.24조 | +0.95 | **매집** +0.31 | 58.5 | −5만 | +13만 | −8만 | ✅ real-hands (small absolute volumes) · matches **[2a/2s] "롯데렌탈, 하락장 방어주 부각…목표가 4.5만"-키움** |

### ★★ The anti-tunnel payoff, stated plainly
**MACRO reached ENRG tactical-OW through ONE name it already knew (S-Oil).** This stage swept 829 names
blind and returned **two of three large-cap real-hands names in the same complex** — **SK이노베이션**
(refining/battery, 18.4조, institution +218만 vs retail −162만) and **SK이터닉스** (renewables).
**Two independent instruments, opposite directions, same answer. ENRG is the desk's best-supported tilt
and it is now supported by breadth, not by a single name.**

⚠ **SK이노베이션 corroborating news, both legs:** [hana 07-16] *"SK이노, 올해 최대 영업익 전망…목표가
17→20만원"* (REIGNITED thread 3→3) · [07-22] *"NH투자증권 2분기 지배주주순익 예상 부합"* [4a/3s].
⚠ **Anti:** rs60 **−22.3%** — it has NOT outperformed on 60 days; the 🟢 is a 20-day phenomenon.

---

## §5 ★ Divergences handed down by MACRO §4x — dispositions

### (a) RS20 benchmark hole — **ACKNOWLEDGED & BOUNDED.** See the header. This stage ranks on
`flow_score`/OBV/`vol_surge`/KIS actuals; RS is context only. **DEEP and BET must do the same.**

### (c) IT gate — **SWEEP'S ANSWER: the gate is open on the mega-cap leg ONLY, and breadth says do not extrapolate.**
전기·전자 has the universe's **largest ignition delta (+0.312)** and simultaneously its **worst breadth
(eqflow −0.217, 13 🔴 vs 2 🟢 across 69 names)**. **wflow (−0.086) ≫ eqflow (−0.217) = a mega-cap-narrow
move.** Combined with MACRO's institutional leg (삼전 기관 +397 → **+832만주**), the honest read is:
**institutions are buying two names; the semiconductor complex is not being bought.**
**→ M-04's gate stays SHUT at the sector level. The re-specified condition #2 (기관 persistence) is the
only one live, and it is live for 삼전/하이닉스 specifically, not for IT.**

### (d) ★ ADR venue substitution — **DECLINED IN WRITING, AND DELETED FROM THE CARRY LIST.**
MACRO forced a disposition ("resolve it or decline it; it may not be carried a fourth time"). **Declined,
for cause:**
```
HXSCL  → 404 Quote not found      HXSCF  → no data, possibly delisted
SKHYY  → no data, possibly delisted
```
**No SK하이닉스 ADR price or volume series is retrievable from any data source this repo owns.** The
ADR–원주 괴리 test cannot be constructed. **Carrying an untestable hypothesis a fourth run is a P4
violation** ("결론은 관측값+출처+신선도를 채운 뒤에만"). **`ADR` stays in the blind-spot emergent-term
list as an observation (52 hits, decaying −22% vs a −9% pool); it is REMOVED as an open question.**
**If it is ever to be answered, it needs a data source this desk does not have** — recorded as a
capability gap, not a research task.

### (h) 휴머노이드/로봇 — **SWEEP'S ANSWER: the axis is right and the vehicles are measurably NOT being bought. DO NOT VEHICLE IT.**
The universe was swept for every robot name. Result:

| Rank / 829 | Ticker | Name | mcap | flow | tag | OBV | rs60 |
|---|---|---|---|---|---|---|---|
| **793** | 454910.KS | **두산로보틱스** | 4.57조 | **−0.56** | 🟡중립 | **분산** | **−34.5%** |
| **804** | 079900.KS | 전진건설로봇 | 0.49조 | **−0.71** | 🟡중립 | **분산** | **−64.6%** |

**The axis that has been RIGHT for three consecutive runs** (삼성 휴머노이드 [8a/4s], 휴머노이드 142
hits/7d, 블랙스톤 로봇관절) **has its two obvious KR vehicles in the bottom 5% of an 829-name universe,
both OBV 분산.** **Per MACRO's new failure class #4 (narrative-sourced vehicles), this is exactly the
configuration that turned a correct macro read into a measured loss on 조선 and 원전.**
**→ Disposition: the robot axis remains an AXIS. It is explicitly UN-VEHICLED. It may not enter BET.**

### (M-03 전력기기, raised by MACRO as the first candidate vehicle) — **FOUND, RANKED, AND NOT CONFIRMED.**

| Rank | Ticker | Name | flow | tag | OBV | **rs60** |
|---|---|---|---|---|---|---|
| 428 | 267260.KS | HD현대일렉트릭 | −0.08 | 🟡중립 | 중립 | −37.4% |
| **497** | **010120.KS** | **LS ELECTRIC** | −0.18 | 🟡중립 | **분산** | **−9.9%** ★ |
| 781 | 034020.KS | 두산에너빌리티 | −0.50 | 🟡중립 | 분산 | **−51.1%** |
| 800 | 272210.KS | 한화시스템 | −0.65 | 🟡중립 | 분산 | −64.9% |

★ **LS ELECTRIC's rs60 of −9.9% is 41pp better than 두산에너빌리티's** — the widest intra-complex spread
on the board, and it **quantitatively confirms M-03's central claim that the AI-power legs have separated.**
The 07-22 print **LGU+·LS일렉트릭 800V DC 공동 개발 [6a/4s]** names it directly.
**But it is rank 497/829, 🟡중립, OBV 분산 — no money.** **→ Per failure class #4: LS ELECTRIC is handed to
DEEP as the AI-power complex's best RS60 candidate, NOT to BET as a vehicle. It must earn a flow
confirmation first.**

---

## §6 ★ Where SWEEP disagrees with the MACRO matrix (named, not smoothed)

| # | MACRO §4 said | SWEEP measured | Resolution |
|---|---|---|---|
| 1 | **FIN = OW** (three banks, 매집, 기관 실매수, 외국인5일 전환) | **금융 sector wflow −0.000, eqflow +0.059, ZERO 🟢 across 76 names**; the triple is tagged **🟡중립** here (sector_flow's universe-relative threshold), not 🟢 | ★ **Both are true and the disagreement is the information: FIN's strength is THREE NAMES, not a sector.** MACRO's OW is a **name basket**, not a sector tilt. **ROTATION must not size it as a sector.** 보험 (−0.204) and 증권 (−0.086/eqflow −0.178) are actively weak inside the same GICS bucket |
| 2 | **ENRG = tactical OW** on S-Oil | **화학 wflow +0.157 (rank 5), and the blind sweep surfaced SK이노베이션 (rank 22, 🟢, 기관 +218만, surge 1.48×) + SK이터닉스** | ✅ **AGREEMENT, and it strengthens the tilt** — breadth-supported, not single-name |
| 3 | **HLTH = OW-as-shelter** | **제약 = #1 sector, wflow +0.305 > eqflow +0.118 (mega-cap-led = 삼바/셀트)** | ✅ **AGREEMENT.** The shelter is the sector's engine |
| 4 | **IT = Neutral, gate shut** | 전기·전자 **largest ignition (+0.312)** but **worst breadth (−0.217, 13🔴/2🟢)** | ✅ **AGREEMENT with a sharper edge** — the ignition is real and it is two names wide |
| 5 | **MATR = UW** | **금속 wflow −0.247, the only major sector with a negative delta** | ✅ **AGREEMENT, 4th run** |
| 6 | **UTIL = UW** | **전기·가스 0 🟢, delta +0.006 (flat)**; 기계·장비 (두산's sector) **worst wflow −0.257** | ✅ **AGREEMENT, strengthened** |
| 7 | **INDU = Neutral split**, 건설 order-flow as the positive leg | **건설 delta +0.241 (2nd-largest ignition), breadth-led, 2 🟢** | ✅ **AGREEMENT — and the 건설 leg is the one INDU positive with universe-wide support.** 운송장비·부품 (조선) wflow −0.186 |
| 8 | **DISC = UW** (현대차) | **롯데렌탈 is one of only 3 large-cap 🟢 real-hands names in the universe**; 현대차 rank **758/829** | ⚠ **PARTIAL DISAGREEMENT — but it is intra-sector, not directional.** DISC's UW is a 현대차 call; the sector's one live name is a **defensive** rental play ("하락장 방어주"). Consistent |

---

## ✅ EXIT CHECK
- [x] **sector_flow sweep done** → `SECTOR_FLOW_KR.json` (829 names / 28 sectors, universe wflow −0.073,
      27🟢 / 29🔴). **Sector ranking read in full (§2); wflow-vs-eqflow read per sector, not just ranked.**
- [x] **new-🟢 read — and it is the stage headline: ZERO ignitions across 829 names on a +5.93% index
      morning**, with the 35-minute-session caveat stated rather than buried.
- [x] **LIVE_SHORTLIST written** → `KR_LIVE_SHORTLIST.json`, 3 names, **real-hands verdicts read**
      (all 3 ✅; 개인 distributing into 기관 on two of three). **The 🟢 breadth signature behind the
      shortlist (micro-cap, 1.5–7.2× surge) is read as a warning, §3.**
- [x] **(US) CYCLE_EXPOSURE — N/A for the KR protocol** (industry_kr composition has no CYCLE_EXPOSURE /
      ACTION_TICKETS block). Explicitly skipped, not silently dropped.
- [x] **★ MACRO §4x items owned by SWEEP were all discharged in writing:** (a) bounded · (c) answered
      (mega-cap-only gate) · (d) **DECLINED for cause and deleted from the carry list** · (h) answered
      (un-vehicled, may not enter BET) · plus M-03's 전력기기 candidate located, ranked, and withheld
      from BET pending flow confirmation.
- [x] **Sweep asof stated** (2026-07-22 ~09:35 intraday, 35-min session) and the carried RS20 inflation
      re-verified against this stage's own file before any number was used.

**→ proceed to EVENT_ALPHA.**
