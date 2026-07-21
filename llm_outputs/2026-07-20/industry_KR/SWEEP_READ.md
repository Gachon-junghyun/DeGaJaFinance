# SWEEP read — industry_KR · 2026-07-20 (Mon)

> Stage 2 / L1·SWEEP. Artifacts: `SECTOR_FLOW_KR.json` · `KR_LIVE_SHORTLIST.json` (both written to the
> hardcoded protocol path). This note is the human read handed to ROTATION.

## ⚠ Data-quality flags (read before using any number below)
- **Sweep asof = 2026-07-16**, not 07-17. `--refresh` did **not** advance it (no later daily bar available).
  So the sweep is **2 sessions stale** at a Monday pre-open and does **not** contain Friday's tape or
  today's 반도체 급락. **It therefore UNDERSTATES the IT/전기·전자 damage**, which is already worst-but-one.
- **The new-🟢 ignition axis is UNAVAILABLE this run.** `delta` is **null for all 829 names**, so
  `new_green` was set true for **all 56 greens** — that is the full green set, not 56 ignitions.
  **Do not read it as early-cycle ignition.** (History has 07-14…07-17 snapshots; the delta join failed
  against this asof.)

## Universe
**n=829 · wflow −0.296 · 🟢56 / 🔴65.** Net-negative, red>green — a de-rating tape, consistent with the
MACRO §1 "tightening-into-de-rating" regime. Not a crash reading; a drift-lower-with-rotation reading.

## Sector rotation (KRX taxonomy) — wflow vs eqflow
| Sector | wflow | eqflow | n | Read |
|---|---|---|---|---|
| 제약 | **+0.207** | +0.044 | 48 | **Top real sector. Mega-led/narrow** (삼바) — matches MACRO M-07 HLTH upgrade |
| 운송·창고 | +0.195 | +0.013 | 24 | Mega-led, thin breadth |
| 의료·정밀기기 | +0.170 | −0.136 | 8 | **wflow≫eqflow = narrow concentration tell**; breadth negative |
| 섬유·의류 | +0.152 | **+0.356** | 27 | **Breadth-led** (eqflow>wflow) — small/mid bid, the healthiest shape on the board |
| 화학 | +0.116 | −0.008 | 103 | Mega-led (SK이노베이션·S-Oil complex) |
| **금융** | **+0.095** | +0.019 | 76 | Positive but **narrow-top** — see the split below |
| 음식료·담배 | +0.079 | **+0.205** | 37 | **Breadth-led defensive bid** — ⚠ contradicts my STPL Neutral→UW |
| 전기·가스 | +0.030 | −0.065 | 10 | Utilities barely positive at mega, negative breadth |
| 건설 | **−0.307** | **+0.081** | 28 | **Split: mega drags, breadth positive** — supports the MACRO "건설 수주 ≠ RE 자산" separation |
| 유통 | −0.275 | +0.016 | 63 | Mega weak, breadth flat |
| 증권 | −0.223 | −0.299 | 18 | ↓ |
| 보험 | −0.279 | −0.067 | 12 | ↓ |
| 금속 | −0.213 | −0.097 | 60 | Confirms MATR UW (POSCO) |
| 운송장비·부품 | −0.357 | −0.139 | 60 | ⚠ **caution on the 조선 up-branch of M-06** |
| **전기·전자** | **−0.420** | **−0.314** | 69 | **Broad, deep negative — both mega AND breadth.** Confirms the IT downgrade decisively |
| **기계·장비** | **−0.490** | −0.234 | 32 | **Board-worst.** Capital goods / 전력기기 / 두산 complex — confirms the UTIL ▼UW and the INDU 전력기기 leg cut |

### ★ Three refinements the sweep forces onto the MACRO matrix
1. **FIN OW is BANKS ONLY.** 금융 +0.095 hides a split: banks green (KB·신한·하나 all real-hands, below)
   while **증권 −0.223 and 보험 −0.279 are both negative.** ROTATION must not carry "Financials" as one block.
2. **STPL needs revisiting.** 음식료·담배 eqflow **+0.205** is a *breadth-led* defensive bid — the exact
   shape M-07 predicts for a cost-of-capital regime, but I tagged STPL Neutral→UW in §4. **Flag: the
   defensive-bid proposition (M-07) is broader than the two names I built it on.**
3. **전기·전자 −0.420 with eqflow −0.314** is not a mega-cap-only problem. The whole electronics complex is
   being sold, breadth included — and this is measured **before** today's 반도체 급락. IT ▼Neutral holds, if anything it is generous.

## LIVE shortlist (시총≥1조 · 🟢가속 · KIS 20d 실측) — 10 screened → **8 real-hands**
| Ticker | Name | flow | OBV | RS20 | 외국인 | 기관 | 개인 | Verdict |
|---|---|---|---|---|---|---|---|---|
| 096770 | **SK이노베이션** | +1.00 | +0.22 | 42.0 | −19만 | **+170만** | −137만 | ✅ 진짜손 |
| 089860 | 롯데렌탈 | +1.00 | +0.28 | 47.0 | −0만 | +8만 | −8만 | ✅ (tiny size — noise-level) |
| 475150 | **SK이터닉스** | +0.91 | +0.34 | 31.5 | −6만 | **+87만** | −86만 | ✅ 진짜손 |
| 161890 | **한국콜마** | +0.79 | +0.28 | 47.3 | −13만 | **+96만** | −85만 | ✅ 진짜손 |
| 086790 | **하나금융지주** | +0.78 | +0.15 | 33.2 | −69만 | **+125만** | −51만 | ✅ 진짜손 |
| 010950 | **S-Oil** | +0.78 | +0.52 | 62.6 | **+13만** | **+158만** | −177만 | ✅ 진짜손 (양방) |
| 105560 | **KB금융** | +0.77 | +0.14 | 35.8 | −257만 | **+337만** | −76만 | ✅ 진짜손 |
| 006360 | **GS건설** | +0.73 | +0.14 | 23.3 | **+148만** | **+225만** | −379만 | ✅ **cleanest print on the board** (both institutional types buying, retail selling) |
| 008930 | 한미사이언스 | +0.97 | +0.18 | 33.4 | −64만 | +62만 | −1만 | △ 혼조 |
| 073240 | 금호타이어 | +1.00 | +0.52 | 47.1 | **−899만** | −452만 | **+1,390만** | ❌ **약한손** — 🟢 invalidated |

### ★ What the shortlist says
- **ENRG is the broadest confirmed leg, not a single name**: SK이노베이션 + S-Oil + SK이터닉스 all real-hands.
  This strengthens M-02's **flow** branch (while its narrative branch keeps fading) — the divergence widens.
- **FIN confirmed on a third bank**: 하나금융지주 joins KB·신한, all 기관-led. Banks-only, as above.
- **GS건설 is the single cleanest real-hands print** (외국인 +148만 AND 기관 +225만, 개인 −379만) and sits in a
  sector whose *breadth* is positive while its mega is negative. **Handed to DEEP as a candidate.**
- **한국콜마 survives** — I downgraded DISC to Neutral in MACRO §4 on absence of narrative evidence; the
  **money for the K뷰티 ODM leg is still real-hands.** ⚠ Flag for ROTATION: DISC downgrade was
  narrative-based and the flow does not agree with it.
- **★ Zero 전기·전자 / semiconductor names cleared the 🟢가속 screen.** Negative confirmation for IT.

## ✅ EXIT CHECK
- [x] sector_flow sweep done → `SECTOR_FLOW_KR.json` (asof 07-16, staleness flagged); 28-sector ranking read.
- [x] new-🟢 read **and rejected as unusable** (delta null → all-greens artifact) — stated, not silently used.
- [x] `KR_LIVE_SHORTLIST.json` written; real-hands / weak-hands verdicts read (8 ✅ / 1 △ / 1 ❌).
- [x] (US) CYCLE_EXPOSURE — **N/A for industry_kr** (protocol excludes it).

**→ proceed to EVENT_ALPHA.**
