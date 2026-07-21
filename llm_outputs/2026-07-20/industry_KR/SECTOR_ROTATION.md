# SECTOR_ROTATION — industry_KR · 2026-07-20 (Mon)

> Stage 4 / L1·ROTATION. **Transmission matrix (thesis = why) × SECTOR_FLOW (money = now) ×
> EVENT_ALPHA cards (stories = what's moving)** → 11-sector OW/UW + the 4 DEEP targets.
> Zero buy/sell calls. Inputs reread from disk: `MACRO_REPORT.md §4` · `SECTOR_FLOW_KR.json` ·
> `SWEEP_READ.md` · `EVENT_ALPHA.md`.

⚠ **Two staleness facts govern every row below.**
1. **The flow sweep is asof 2026-07-16** (`--refresh` would not advance it — no later daily bar).
   It is **2 sessions stale at a Monday pre-open** and contains **neither Friday's tape nor today's
   반도체 급락**. Where the sweep and today's news disagree, the disagreement is dated, not resolved.
2. **The new-🟢 ignition axis (rule c) is UNAVAILABLE this run.** `delta` is null for all 829 names,
   so `new_green` flagged **all 56 greens**. **No sector is promoted on an ignition signal**, because
   there is no trustworthy one. Stated rather than silently used.

---

## §1 The 11-sector table — matrix × flow × cards

| Rank | GICS | ROTATION verdict | MACRO matrix | SECTOR_FLOW (asof 07-16) | EVENT_ALPHA | AGREE / DIVERGE |
|---|---|---|---|---|---|---|
| **1** | **FIN (은행 only)** | **OW ★1** | OW (highest) | 금융 **wflow +0.095** / eq +0.019 (n=76) | card 5 (손보, 🟡 small) | ✅ **AGREE** — thesis (hike→NIM) and money (KB·신한·하나 all 기관 real-hands, KB RS positive into a falling index) point the same way. **The one double-confirmed leg.** |
| **2** | **ENRG** | **OW ★2** | tactical OW | 화학 **wflow +0.116** / eq −0.008 (mega-led) | — | ⚠ **DIVERGE (the run's #1 question)** — money is loudest on the board (S-Oil **RS20 +62.6% / RS60 +13.4%**, OBV 매집, 외국인·기관 동시매수; SK이노베이션·SK이터닉스 also real-hands) while the **narrative thread FADES 6→5→4→3 into "post-Iran oil market"**. → **DEEP owns this** → ✅ **RESOLVED: EARLY** (see addendum). |
| **3** | **HLTH** | **OW ★3** | modest OW (M-07) | 제약 **wflow +0.207 = top real sector** / eq **+0.044** | — | ⚠ **DIVERGE (breadth)** — top wflow but near-zero eqflow = **mega-cap-narrow**, i.e. possibly 삼바 alone (2.7조 인수 + RS20 +22.4%). Right thesis, but is it one name? → **DEEP owns this.** |
| **4** | **INDU (건설·EPC leg only)** | **OW ★4** | OW-split (downgraded) | 건설 **wflow −0.307 but eq +0.081** · 기계·장비 **−0.490 (board-worst)** · 운송장비 −0.357 | **card 1 CONFIRMED-EARLY** (GS건설) · **card 8 BINARY-GATED** (삼성E&A) | ⚠ **DIVERGE, and the split resolves it** — the sector tag is negative because its **전력기기/기계 leg is the worst on the board** (M-03 anti fired), while its **건설/EPC leg has positive breadth + the two cleanest real-hands prints**. **Do not carry INDU as one block.** |
| **5** | **STPL** | **Neutral ▲ promoted** | Neutral→UW | 음식료·담배 wflow +0.079 / **eq +0.205 (breadth-led)** | — | ⚠ **DIVERGE (b) — flow-led sector the matrix under-rated → promote a notch.** A *breadth-led* defensive bid is exactly the shape M-07 predicts for a cost-of-capital regime, and I tagged it UW on regime logic alone. Money moved before my thesis. → **DEEP owns this.** |
| **6** | **DISC** | **Neutral ▲ promoted** | Neutral (downgraded 07-20) | 섬유·의류 wflow +0.152 / **eq +0.356 = best breadth on the board** | — | ⚠ **DIVERGE (b)** — I downgraded DISC in MACRO §4 on *absence of narrative*, but 한국콜마 is still ✅real-hands (기관 +96만) and 섬유·의류 has the healthiest breadth shape in the sweep. **The downgrade was narrative-based and the flow does not agree.** Promoted back to Neutral, not to OW (no card, no fresh catalyst). |
| **7** | **COMM** | Neutral | Neutral | 통신 wflow +0.021 / eq −0.092 | — | ✅ AGREE — no wind either way. 알파벳 07-22 spillover is the only input. |
| **8** | **RE** | **UW** | UW (most rate-negative) | 부동산 wflow +0.322 **but n=3** · 리츠 −0.133 | card 1 (construction ≠ RE) | ✅ AGREE — the +0.322 is **n=3 = noise, dismissed**. 리츠 −0.133 is the readable proxy. Hike + 대출절벽 + 경기 3곳 규제 stand. |
| **9** | **MATR** | **UW** | UW | 금속 **−0.213 / eq −0.097** | **card 4 STORY-ONLY** (direction refuted) | ✅ **AGREE, triple-confirmed** — matrix UW + flow negative at both levels + the card's body-read **refuted the 철강 AI-DC headline** (뉴욕주 DC 1년 유예). Copper 95%ile crowded-long adds positioning risk. |
| **10** | **IT** | **UW ▼ (was Neutral)** | Neutral, flow-gated | 전기·전자 **−0.420 / eq −0.314** | book flag (009150) | ⚠ **DIVERGE, and I am resolving it DOWN, not deferring it.** MACRO had IT Neutral. The sweep says the complex is negative at **both** mega and breadth — and that is **asof 07-16, before today's 반도체 급락**. Add: 삼전 외국인 −4,672만 / 개인 +4,259만 weak-hands, **zero 전기·전자 name cleared the 🟢 screen**, 한은's own 네덜란드병 warning. **Downgraded to UW.** |
| **11** | **UTIL** | **UW** | UW | 전기·가스 wflow +0.030 / eq −0.065 · 기계·장비 −0.490 | — | ⚠ **DIVERGE (small, named)** — the *regulated utility* line (전기·가스) is marginally positive at mega while the **원전/기계 expression (두산에너빌리티 RS60 −45.9%) is the board's worst.** These are different animals: 한전-type regulated vs 원전 capex. UW applies to **the 원전 capex expression**; the regulated line is Neutral-but-uninvestable-here. |

### §1a Divergence register — every divergence has a named owner
| # | Divergence | Owner | The question it must answer |
|---|---|---|---|
| D-1 | **ENRG: money accumulating into a fading narrative** | **DEEP-ENRG** | Early or wrong? Is the S-Oil bid a **정제마진** fundamental, or a stale Hormuz-premium chase into a TACO binary? |
| D-2 | **HLTH: top wflow, near-zero eqflow** | **DEEP-HLTH** | Is this a *sector* bid or **삼바 alone**? Does the 2.7조 acquisition create a repeatable leg? |
| D-3 | **STPL: breadth-led bid the matrix under-rated** | **DEEP-STPL** | Is the 음식료 eqflow +0.205 a genuine defensive rotation (M-07), or margin relief from the *scenario* of a stronger won? |
| D-4 | **INDU: sector tag negative, sub-legs opposite** | **carried to BET** (cards already CONFIRMED-EARLY) | Resolved enough by EVENT_ALPHA cards 1/8 — 건설·EPC in, 전력기기·기계 out. No DEEP needed. |
| D-5 | **IT: narrative bullish, flow weak-hands** | **resolved here → UW** | Resolved by the flow, per the new failure-class rule (below). Not deferred. |
| D-6 | **DISC: my narrative downgrade vs positive breadth** | **watch (no DEEP slot)** | Re-check next run; promoted to Neutral in the meantime. |
| D-7 | **보험 sector −0.279 vs 삼성화재 RS60 +35.9%** | **DEEP-FIN** | Does the FIN OW extend past banks to a 손보 margin leg (card 5), or is 삼성화재 idiosyncratic? |

⚠ **Standing rule applied this run (from MACRO §5, new failure class):** *when narrative and measured
flow invert, the flow sets the tilt and the narrative becomes the anti-signal to track.* This is what
moved **IT to UW** and kept **MATR at UW** against a REIGNITED steel story — and, symmetrically, what
**promoted STPL and DISC** against my own narrative-based downgrade. The rule cuts both ways or it is
just a bear bias.

---

## §2 The 4 DEEP targets — selected by rule, not by gut

**Recency input** — prior KR DEEP_LOG lines:
`DEEP_LOG 2026-07-16: continuous=[FIN, IT] rotating=[ENRG, DISC] (rested: INDU, UTIL)` ·
07-15 KR DEEP set (via BET_SHEET §F): **INDU**. → **Covered within the last ~3 runs: FIN, IT, ENRG, DISC, INDU.**

### ① Continuous-track 2 = today's top-2 OW → **FIN, ENRG**
- **FIN** held a continuous slot on 07-16 **and is still top-4 OW today → KEEPS the slot** (anti-thrash
  continuity applied and stated).
- **ENRG** was *rotating* on 07-16 and is **today's #2 OW → promoted to continuous.**
- ⚠ **IT held a continuous slot on 07-16 and LOSES it** — it is no longer top-4 (downgraded to UW, rank 10).
  Stated explicitly so the drop is auditable rather than silent.

### ② Rotating 2 = next-highest OW **not** deep-dived in the last ~3 runs → **HLTH, STPL**
- **HLTH** (rank 3) — **not covered in any recent KR run** (the 07-13/07-14 HLTH deep-dives were the
  **US** desk). Qualifies cleanly. Carries divergence **D-2**.
- **INDU** (rank 4) — **skipped: deep-dived 07-15, inside the ~3-run window.** Its open questions are
  already resolved by EVENT_ALPHA cards 1 and 8, and **its candidates are carried to BET regardless**,
  so resting the sector loses nothing.
- **STPL** (rank 5) — **never deep-dived on the KR desk.** Adjacent-rank tiebreak vs INDU resolved by
  **least-recently-covered**, as the rule permits **and as stated here.** Carries divergence **D-3**.

**No padding.** Neutral/UW sectors (COMM, RE, MATR, IT, UTIL, DISC) were **not** used to fill slots.

### DEEP brief per target
| Target | Track | The one question DEEP must answer |
|---|---|---|
| **FIN** | continuous (kept) | Does the NIM leg still compound with 대출총량 1.5% capping volume — and does it extend to 손보 (D-7, 삼성화재) or stop at banks? |
| **ENRG** | continuous (promoted) | **D-1** — is the S-Oil/SK이노베이션/SK이터닉스 bid early or wrong, with the narrative fading into a TACO binary? |
| **HLTH** | rotating | **D-2** — sector bid or 삼바 alone? Is the 2.7조 폴리펩타이드 인수 a repeatable CDMO leg? |
| **STPL** | rotating | **D-3** — is the breadth-led 음식료 bid a real defensive rotation, or a won-scenario artifact? |

---

## DEEP_LOG 2026-07-20: continuous=[FIN, ENRG] rotating=[HLTH, STPL]  (dropped from continuous: IT — no longer top-4, downgraded to UW · rested: INDU — covered 07-15, questions resolved by EVENT_ALPHA cards · DISC — covered 07-16)

## ✅ EXIT CHECK
- [x] **11-sector OW/UW table written**, each row carrying matrix + flow + card evidence.
- [x] **Every matrix×flow divergence named with a resolution owner** — 7 registered (D-1…D-7); 4 handed to DEEP, 1 to BET, 1 resolved in-stage (IT→UW), 1 to watch.
- [x] **Rule (c) new-🟢 ignition explicitly unavailable** (delta null → all-greens artifact); **no sector promoted on it.**
- [x] **Sweep staleness (asof 07-16, 2 sessions) stated** and applied — the IT downgrade notes the sweep predates today's 반도체 급락, i.e. it understates the case.
- [x] **4 DEEP targets picked by the rule** — continuity kept (FIN) and lost (IT) both stated; recency window applied to skip INDU; adjacent-rank least-recently-covered tiebreak (INDU vs STPL) stated. **No padding.**
- [x] **DEEP_LOG line appended.**

**→ proceed to DEEP.**

---

# ✏️ POST-DEEP ADDENDUM (append-only) — 2026-07-20, after all 4 DEEP agents returned

> ROTATION's table above was written *before* DEEP ran. Three of its rows did not survive contact with
> the deep data. Recorded here rather than by editing the table, so the miss is auditable.

## A. Verdict per DEEP target

| Target | Divergence | Verdict | Effect on the §1 table |
|---|---|---|---|
| **FIN** | D-7 (보험) | ✅ **Thesis HOLDS, engine restated** | **OW ★1 confirmed.** NIM compounds via **price**, not volume: 코픽스 +0.15%p/월, 3개월 연속, >3% vs a +0.08%p H2 기업 연체 전망. Volume IS capped (5대은행 1.5% 목표 대비 ₩3,500억 초과; KB가 중도상환수수료 면제로 자기 book을 줄이는 중) → capped RWA ⇒ 자본 적치 ⇒ **자사주**(KB 취득결과+소각 07-16, 하나 07-14). **The cap is fuel for 밸류업, not its enemy.** Thesis: 성장 → **마진 × 자본환원**. Prior kill-switch #5(고정금리 전환) **REFUTED** — 차주는 변동형 선택 중. D-7: extends to **손보**(3사 모두 기관 주도; 보험 −0.279는 **생보**가 만든 것) but **NOT via 삼성화재**(이미 priced: 컨센 상단 +2.98%, PBR 1.23, 서지 0.61x, OBV 약세 다이버전스, 숏 building). |
| **ENRG** | D-1 (money vs narrative) | ✅ **EARLY — and my premise was wrong** | **OW ★2 confirmed, upgraded.** The "narrative FADING" premise **does not survive measurement**: `theme-age --scope domestic` splits it into **정제마진 🟡ACCELERATING 2.34x on only 28 articles** / 윤활기유 2.14x on 8, vs **호르무즈 ⚪ECHO 1.26x on 8,570**. The FADING curve was `thread` **bundling a saturated geopolitical story with a newborn margin story** — the event-vs-topic limit the `event_threads` L3 warns about, which **I read as one narrative**. Tape refutes the fade outright: **Brent Sep $90.85 (+3.12%), first >$90 since 06-11** [yonhap 07-20 07:40]; 호르무즈 통항 21→13척/일. |
| **HLTH** | D-2 (breadth) | ❌ **DOWNGRADE OW★3 → Neutral** | **Not a sector bid — a two-name bid.** 삼바 **76.0%** + 셀트리온 **23.8%** = **99.6%** of 제약's +0.207 wflow. The other 46 names = 21.6% of sector mcap and **+0.2%** of the flow, **26 of 46 negative**. |
| **STPL** | D-3 (breadth-led bid) | ❌ **REVERT promotion → UW** | **Artifact.** 6🟢/0🔴 of 37, totalling **₩0.70조 of ₩46.34조 = 1.50%**, median mcap ₩0.101조. **4 of the 6 are 사조 group affiliates** (DART: 사조산업→사조대림 5 filings in 6 weeks, last on **07-16 = the sweep's exact asof**; 사조대림→사조오양; 사조시스템즈+주진우→사조산업). 한성기업(RS20 +240.7%, 서지 8.17x) is an **애국테마주 meme on a 상폐-우려 stock** dragging the mean. 고려산업 invalidated live to 🔴. **기관 20d net across survivors = +3.5만주, less than KT&G alone.** |

## B. ★ M-07 is largely FALSIFIED — the run's biggest self-correction
**M-07 (defensive cash-flow bid) was the proposition I *created* this run, and DEEP knocked down BOTH
of its expressions.** HLTH is two mega-caps, not a rotation. STPL is a controlling family's disclosure
cadence read as breadth. **What survives of M-07 is FIN alone — which was already M-01.** M-07 is
therefore **downgraded to a sub-clause of M-01**, not carried as an independent proposition into BET.
⚠ Worse for M-07: 삼바's ₩2.7조 PolyPeptide 인수 is funded by **"보유자금 및 차입금"** — a **debt-funded**
acquisition **increases** rate sensitivity, which **contradicts the very rate-insensitivity premise**
that promoted HLTH. The catalyst I promoted the sector on argues against the thesis I promoted it with.

## C. ★ Benchmark trap — a measurement error that ran through every upstream stage
**`module_flow`'s default bench is SPY.** Every RS number in this run's files is **`--bench ^KS11`**,
which measures *relative to a broken KOSPI*, not absolute strength. DEEP measured the gap:
| Name | RS20 vs ^KS11 | RS20 vs SPY |
|---|---|---|
| 삼성바이오로직스 | **+22.4%** | **−2.7%** |
| 삼성화재 | **+24.9%** | **−0.2%** |
**Pharma is not rising; it is falling less than the index** — and 서지 **0.71x** means *less* money than
usual, not more. **Rule adopted: every RS figure must state its bench, and OW claims built on
KOSPI-relative strength must be re-checked absolute before they reach BET.**
(Separately: the earlier **column-shift** error — `OBV` is a state word; the two numbers are RS20/RS60 —
was corrected in MACRO §2 / SWEEP_READ. That fix *strengthened* FIN: KB RS20 is +35.8%, not +1.4%.)

## D. Two dated regulatory binaries DEEP found that §0's calendar MISSED
| When | Event | Axis | Why it matters |
|---|---|---|---|
| **≈07-24~26** | **8th 석유 최고가격제 상한 고시** | ENRG | Government text says caps **directly compress refiner profitability**; exit is blocked and a *hike* is on the table. `theme-age` has it **🔴FADING 0.21x = unpriced**. Lands inside the ENRG horizon. |
| **This month (undated)** | **금융위 금융지주 지배구조 개선안** — possible CEO 3연임 제한 | FIN | Directly touches the 밸류업/자본환원 leg that DEEP-FIN just made the core of the thesis. Content unknown. |
⚠ Both must be bracketed both ways by BET. `catalyst_calendar` carried **neither** — the third KR-specific
binary it missed today (after 대미투자 07-22~24). **The calendar module is not sufficient for the KR desk.**

## E. Revised OW/UW ranking handed to BET
1. **FIN — OW ★1** (margin × capital return; 손보 extension via **DB손해보험 005830**, not 삼성화재)
2. **ENRG — OW ★2** (정제마진 EARLY, TACO-defensible; **GS 078930** cheapest exposure)
3. **INDU (건설·EPC leg only) — OW ★3** (promoted by default; cards 1/8 already CONFIRMED-EARLY)
4. **HLTH — Neutral** (was OW★3; two-name bid, debt-funded catalyst, negative absolute RS)
5. **DISC — Neutral** · **COMM — Neutral**
6. **STPL — UW** (promotion reverted) · **RE — UW** · **MATR — UW** · **IT — UW** · **UTIL — UW**

## F. Tool defects logged this stage (4th and 5th of the run)
- **`module_business` fails on every ticker** — `data/news_alert.db` missing, **no API fallback** (P6: the client no longer owns that DB). Segment mix carried by reference, unverified. **Silent failure #4.**
- **`sector_flow` `eqflow` has no mcap floor and no same-group handling** — six micro-caps, four of them one family, produced a sector-level "breadth" signal that ROTATION promoted on. **This defect directly caused a wrong OW.**
- **`의료·정밀기기` wflow +0.170 is 160.5% made by 케이씨텍 — a semiconductor CMP/slurry company misfiled into the sector.** Sector labels in the KR universe are not trustworthy at small n. Flagged unusable.
