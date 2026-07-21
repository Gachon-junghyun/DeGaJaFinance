# BET_SHEET — industry_KR · 2026-07-20 (Mon)

> Stage 6 / L1·BET. One file, per-sector sections §A–§E. Downstream desks read this exact filename.
> **Zero buy/sell recommendation.** Sizing language below is *influence illustration* only.
> Inputs reread from disk: `MACRO_REPORT.md` · `SWEEP_READ.md` · `EVENT_ALPHA.md` ·
> `SECTOR_ROTATION.md` (+ its **POST-DEEP ADDENDUM**) · `SECTOR_DEEP_{FIN,ENRG,HLTH,STPL}.md`.

## Candidate set construction (wide net, per the stage rule)
`(DEEP-agent thesis leaders)` ∪ `(sector screener setups)` ∪ `(★KR_LIVE_SHORTLIST names — incl. cross-sector)`.
The LIVE shortlist drags in names outside the DEEP sectors; those get their own section **§F**.

⚠ **Data asof discipline.** Prices/valuation pulled **2026-07-20 pre-open**; flow/RS **asof 2026-07-16 close**
(the sweep would not advance — 07-17 was 제헌절 and this ran pre-open). **All RS is `--bench ^KS11`** —
see the benchmark trap in ROTATION §C: KOSPI-relative strength is *not* absolute strength.

---

## §A Numbers (pulled 2026-07-20; blanks are blanks)

| Ticker | Name | Sector | 현재가 | 시총(억) | PER TTM | PER Fwd | PBR | 컨센 상승여력 | 외인% | 배당% | 업종PER |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 005830 | **DB손해보험** | FIN(손보) | 163,000 | 106,766 | 7.19 | **7.0** | **0.85** | **+34.93%** | 45.29 | — | 9.05 |
| 105560 | KB금융 | FIN(은행) | 181,100 | 642,339 | 11.45 | 10.0 | 1.08 | +21.94% | 79.37 | 2.41 | 9.33 |
| 078930 | **GS** | ENRG | 82,800 | 76,917 | 5.95 | **5.0** | **0.51** | +18.36% | **20.45** | — | 29.94 |
| 010950 | S-Oil | ENRG | 144,900 | 163,132 | 17.93 | 7.0 | 1.76 | **+7.70%** | 79.87 | — | 29.94 |
| 006360 | **GS건설** | INDU(건설) | 27,300 | 23,364 | 35.83 | 11.0 | **0.48** | **+64.40%** | 19.50 | — | 20.87 |
| 028050 | 삼성E&A | INDU(EPC) | 40,850 | 80,066 | 12.86 | 11.0 | 1.67 | **+64.21%** | 38.56 | — | 20.87 |

**Arithmetic cross-check (현재가 ÷ 추정EPS vs quoted Fwd PER)** — all six reconcile:
DB손보 163,000/23,285 = **7.00** ✓ · KB 181,100/18,271 = **9.91≈10.0** ✓ · GS 82,800/17,075 = **4.85≈5.0** ✓ ·
S-Oil 144,900/20,993 = **6.90≈7.0** ✓ · GS건설 27,300/2,527 = **10.80≈11.0** ✓ · 삼성E&A 40,850/3,609 = **11.32≈11.0** ✓.
⚠ **Blanks are blanks:** 배당% unavailable for DB손보/GS/GS건설/삼성E&A/S-Oil from this source — **not** imputed.
⚠ `module_valuation --peers` **silently returns empty rows when peers carry the `.KS` suffix** (bare 6-digit codes
required). Peer-average columns are therefore **blank, not zero** — a `0` in that table is a failed lookup, not a value.

---

## §B Thesis per candidate — freshness placeholder **→ ALPHA tag in §H**

### FIN — OW ★1 · thesis restated by DEEP: **margin × capital return**, not growth
- **The engine:** 코픽스 **+0.15%p in one month, 3 months running, back >3%**, vs a **+0.08%p** H2 corporate
  delinquency forecast [sedaily 07-19]; **zero household-delinquency prints in the 7d window.** Price
  repricing outruns both volume and credit cost.
- **The cap is fuel, not the enemy:** 5대은행 are **₩3,500억 over** the 1.5% 총량 target [donga 07-20] and
  **KB is waiving prepayment fees to shrink its own book** [sedaily 07-19/20]. Capped RWA ⇒ capital
  accumulates ⇒ **buybacks/cancellation** (KB 취득결과+소각결정 **07-16**, 하나 **07-14**).
- **Prior kill-switch #5 REFUTED:** borrowers are choosing **변동형**, not fixed [donga 07-15].
- **005830 DB손해보험 — the run's genuinely new name** (appeared in *no* upstream stage; DEEP-FIN found it).
  The 보험 sector's −0.279 is made by **생보**; all three 손보 names are institution-led. Cheapest of the
  set on both PER (7.0) and PBR (0.85), **and the least crowded by foreigners (45.29%)**. **→ ALPHA: 🟡PARTIAL** (§H)
- **105560 KB금융** — carried; the 밸류업 leg is now the thesis core rather than a kicker. **→ ALPHA tag in §H**
- ⚠ **삼성화재 (000810) DROPPED from the candidate list.** EVENT_ALPHA card 5 routed the 손보 thread to it;
  DEEP-FIN shows it is the **priced-in** winner — consensus upside **+2.98%**, PBR 1.23, 서지 0.61x, OBV
  neutral with a **bearish divergence**, short **0.71% building**, zero return filings in 30d. **Correction
  to my own card, applied.**

### ENRG — OW ★2 · **EARLY, and TACO-defensible** (the premise I got wrong, corrected)
- **My "narrative FADING" premise did not survive measurement.** `theme-age --scope domestic`:
  **정제마진 🟡ACCELERATING 2.34x on only 28 articles**, 윤활기유 2.14x on 8 — vs **호르무즈 ⚪ECHO 1.26x
  on 8,570**. The FADING curve was `thread` **bundling a saturated geopolitical story with a newborn
  margin story**; I read the bundle as one narrative.
- **Tape refutes the fade:** **Brent Sep $90.85 (+3.12%), first >$90 since 06-11** [yonhap 07-20 07:40];
  호르무즈 통항 **21→13척/일**.
- **Why it survives a TACO reversal** — three houses explicitly tested that branch and held:
  신한 07-12 *"유가 하락에도 정제마진 견고"* · 하나 07-07 *"유가 하락에도 윤활기유 호조"* · 한투 07-08
  *"윤활기유 공급부족·정제마진 강세"*. Drivers are the **Russian diesel export ban** and **destroyed Qatar
  Pearl GTL Group III supply** — **neither dies if Hormuz opens.** ⇒ **margin component early,
  Hormuz-premium component crowded; TACO strips one, not both.**
- **078930 GS — cheapest margin exposure, best TACO defence.** Fwd PER **5.0**, PBR **0.51**, 외인 **20.45%**
  (least crowded on the sheet), 공매도 **0.0%**. Same institutional signature as S-Oil (기관 +95.5만). **→ ALPHA tag in §H**
- **010950 S-Oil** — carried, but **consensus upside is only +7.70% and PBR 1.76**: the *name* is priced
  even though the *margin* is early. This is the sheet's clearest "right thesis, wrong vehicle" pair. **→ ALPHA tag in §H**
- ⚠ **475150 SK이터닉스 DOWNGRADED 🟠 and dropped from finalists** — short balance **flipped covering →
  building +0.54 at 3.12%**, which **falsifies the 07-16 squeeze thesis** SWEEP carried forward.
- ⚠ **남해화학 falsified and dropped** (DEEP-ENRG).

### INDU (건설·EPC leg only) — OW ★3 · from EVENT_ALPHA cards 1 and 8
- **006360 GS건설** — policy-driven **volume** wind, in force **today, retroactively**: 토지비 **80%** 선지원,
  사업비 3개월마다 지급, **착공 최대 5개월 단축** [yonhap/donga/mt 07-20, 본문]. PBR **0.48**, Fwd PER 11.0,
  consensus upside **+64.40%**, 외인 19.5%. **→ ALPHA tag in §H**
- **028050 삼성E&A** — the **대미투자 1호 = 에너지 프로젝트** leg (§E binary). PBR 1.67, upside **+64.21%**. **→ ALPHA tag in §H**
- ⚠ **The 전력기기/기계 leg is NOT here** — 기계·장비 **−0.490 = board-worst**; M-03's kill-switch fired.

### HLTH — **Neutral (downgraded from OW★3), no candidate promoted**
- **Not a sector bid — a two-name bid:** 삼바 **76.0%** + 셀트리온 **23.8%** = **99.6%** of 제약's wflow;
  the other 46 names = 21.6% of mcap and **+0.2%** of flow, **26 of 46 negative**.
- **The catalyst argues against the thesis.** ₩2,706,163,546,103 PolyPeptide 인수 **verified from primary
  source** (OPENDART `document.xml`, rcpNo 20260720000001 — exact match to the 2-outlet news). But it is
  funded by **"보유자금 및 차입금"** — a **debt-funded** deal **increases** rate sensitivity, contradicting
  the rate-insensitivity premise that promoted HLTH. Target **loss-making 3 straight years** (2025 rev
  ₩6,692억, net **−₩361억**), bought at **4.65x P/B / 4.04x P/S**, costing **36.32% of 삼바 equity**, and
  **conditional: 66.7% minimum tender vs only 55.65% committed** — below that, nothing is bought.
- **No HLTH name enters §A.** Watch-only: 셀트리온 (best flow quality, short 0.13% covering), 삼바.

### STPL — **UW (promotion reverted), no candidates**
6🟢/0🔴 of 37 = **₩0.70조 of ₩46.34조 (1.50%)**, median mcap ₩0.101조; **4 of 6 are 사조 group affiliates**
(DART: 사조산업→사조대림 **5 filings in 6 weeks, last 07-16 = the sweep's exact asof**). 기관 20d net across
survivors **+3.5만주 < KT&G alone**. **All 4 names clearing ₩2.5조 are 🟡 or worse.** **None qualify.**

---

## §C Flow / positioning cross-read (KIS per-investor actuals + KRX short, asof 2026-07-16)

| Ticker | Flow | OBV | RS20 | RS60 | 서지 | 외국인 / 기관 / 개인 (만주, 20d) | 공매도잔고 | Read |
|---|---|---|---|---|---|---|---|---|
| **005830 DB손보** | 🟢가속 | 매집 | **+33.5%** | −16.1% | 1.16x | −68.9 / **+69.7** / −13.0 | **0.01% flat** | ✅ cleanest risk profile on the sheet — real-hands, **no short overhang** |
| **078930 GS** | 🟢가속 | 분산 | **+40.9%** | **+5.0%** | 1.20x | −42.0 / **+95.5** / −54.4 | **0.0% flat** | ✅ **only name with RS20 AND RS60 both positive**; zero short |
| **006360 GS건설** | 🟢가속 | 매집 | +23.3% | −40.2% | 1.20x | **+148.0** / **+225.4** / −378.6 | **3.79% building 🔥크라우디드** | ⚠ **double-edged — see below** |
| 028050 삼성E&A | 🟡중립 | 분산 | +6.9% | −27.7% | **0.66x** | **+191.7** / **+125.4** / −304.9 | 0.25% flat | 🟡 real-hands but **no volume**; uncalled |
| 105560 KB금융 | 🟢가속 | 매집 | **+35.8%** | +1.4% | 1.27x | −256.6 / **+337.1** / −76.4 | — | ✅ real-hands, 기관-led |
| 010950 S-Oil | 🟢가속 | 매집 | **+62.6%** | +13.4% | 1.21x | **+12.6** / **+158.5** / −177.4 | 0.48% building | ✅ real-hands **both sides**; short nearing the 0.5% 주목 line |

### ★ Two positioning facts that change how these read
1. **GS건설's short balance is 3.79% of float and BUILDING (+0.08) — 🔥크라우디드.** The LIVE_SHORTLIST view
   does **not** display short interest, so this did **not** surface in SWEEP or EVENT_ALPHA, where I called
   GS건설 "the cleanest real-hands print on the board." **That description was incomplete.** It is
   simultaneously the sheet's best institutional-accumulation print **and** its most crowded short. Those
   are not contradictory — they are the setup — but it is a materially different risk shape from DB손보/GS
   at ~0%, and **must not be sized as if it were the same.** Correction applied here.
2. **Overheat across the FIN leads** (DEEP-FIN): 하나 RSI **85.4** · DB손보 **83.7** · KB **81.4**, all at the
   upper Bollinger band. The direction is confirmed; the *entry* is not clean.

---

## §D Competition / peers
- **FIN:** DB손보 vs 삼성화재 — DB손보 PER 7.0 / PBR 0.85 / upside +34.9% vs 삼성화재 PBR 1.23 / upside +2.98%.
  **The margin thesis is the same; only DB손보 is unpriced.** 업종PER 9.05 ⇒ DB손보 trades at a **discount to
  its own sector**. Banks: KB Fwd 10.0 vs 업종 9.33 = **slight premium**, i.e. the bank leg is *not* cheap;
  it is carried on capital return, not multiple.
- **ENRG:** GS Fwd **5.0** / PBR **0.51** vs S-Oil Fwd 7.0 / PBR **1.76**, against 업종PER **29.94**. Both are
  deep-discount to sector, **GS materially cheaper on both metrics with better flow and zero short**.
- **INDU:** GS건설 PBR **0.48** vs 삼성E&A **1.67**, identical consensus upside (~+64%) and identical Fwd PER
  (11.0). Different bets: GS건설 = domestic housing **volume**; 삼성E&A = **대미투자 1호 binary**.
- ⚠ Peer-average rows are **blank** (the `.KS`-suffix defect above), so these comparisons are **name-to-name,
  not name-to-peer-median**. Stated rather than papered over.

---

## §E Refutation + dated catalysts

| # | Candidate | What falsifies it (observable) | Dated catalyst |
|---|---|---|---|
| E-1 | **DB손보 / KB (FIN)** | 가계 **연체율** prints turning the hike into a credit-cost event; **핵심예금 이탈** offsetting NIM; buyback cadence stopping | **금융위 금융지주 지배구조 개선안 — THIS MONTH, undated**, possible **CEO 3연임 제한** ⚠ directly hits the capital-return leg DEEP made the thesis core |
| E-2 | **GS / S-Oil (ENRG)** | **정제마진·윤활기유 spread rolling over**; Russian diesel ban lifted; Qatar Pearl GTL supply restored | ⚠ **8th 석유 최고가격제 상한 고시 ≈07-24~26** — government text says caps **directly compress refiner profitability**; exit blocked, a *hike* on the table; `theme-age` **🔴FADING 0.21x = UNPRICED** |
| E-3 | **GS / S-Oil (ENRG) — the other branch** | **TACO**: Iran declares the Strait open → Brent gaps down, **WTI 10%ile crowded shorts** cover | **Undated, live.** ⚠ Strips the *premium* component only — **not** the margin component (§B). One-way tilt = protocol violation |
| E-4 | **삼성E&A (INDU)** | **쿠팡 의제 contaminating the talks → 1호 발표 연기**; 외국인·기관 flipping to net-sell | **07-22 출국 → 07-24 귀국 (D-2, HARD).** 김정관–러트닉. 1호 = **에너지 프로젝트** |
| E-5 | **GS건설 (INDU)** | 착공이 매출로 전환되지 않음; **대출절벽/총량규제** throttling the buyer side; **short 3.79% building** accelerating into a de-rating | 월간 주택 **착공 건수** · LH 매입약정 체결 건수. **Horizon 2026-08-20** |
| E-6 | **ALL (index-level)** | KOSPI extending 7,000 → 6,600 → foreign net-sell resuming; **알파벳 07-22** re-igniting AI risk-on and snapping the defensive rotation | **알파벳 실적 07-22 (D-2)** · TSLA 07-22 · RTX/LMT 07-23 |

⚠ **Three dated KR binaries land inside this sheet's horizon and `catalyst_calendar` carried NONE of them**
(대미투자 07-22~24 · 석유 최고가격제 ≈07-24~26 · 금융지주 지배구조 this month). All three were found by
body-reads and DEEP. **The calendar module is not sufficient for the KR desk** — logged for ALPHA.

---

## §F Cross-sector LIVE shortlist names — included or dropped **with reason**

| Ticker | Name | LIVE verdict | Disposition |
|---|---|---|---|
| 096770 | SK이노베이션 | ✅진짜손 (기관 +170만) | **CARRIED as ENRG alternate** — same margin thesis as GS/S-Oil, but DEEP-ENRG ranked it 3rd; no separate §A row |
| 475150 | SK이터닉스 | ✅진짜손 (기관 +87만) | **DROPPED** — short flipped covering→**building +0.54 at 3.12%**, falsifying the 07-16 squeeze thesis |
| 161890 | 한국콜마 | ✅진짜손 (기관 +96만) | **CARRIED to watch, not to §A** — DISC is Neutral; the K뷰티 ODM leg has real money but **no card and no fresh catalyst**. Honest status: my MACRO narrative-downgrade and the flow still disagree; unresolved, not resolved |
| 086790 | 하나금융지주 | ✅진짜손 (기관 +125만) | **CARRIED as FIN alternate** — same thesis as KB; **RSI 85.4 = most overheated of the three**, so not promoted to §A |
| 089860 | 롯데렌탈 | ✅진짜손 | **DROPPED** — 외국인 −0만 / 기관 +8만 / 개인 −8만 is **noise-level size**; the ✅ tag is not meaningful at that magnitude |
| 008930 | 한미사이언스 | △혼조 | **DROPPED** — mixed hands, and HLTH is Neutral |
| 073240 | 금호타이어 | ❌약한손 | **DROPPED** — 외국인 −899만 / 개인 **+1,390만** = textbook weak-hands; the 🟢 tag is invalidated |
| 000810 | 삼성화재 | (from EVENT_ALPHA card 5) | **DROPPED** — priced in (+2.98% upside); replaced by **DB손보** |

---

## §G Sizing language — *influence illustration only, NOT a recommendation*
Relative conviction implied by the evidence, **not** an instruction and **not** advice:
**DB손보 ≈ GS > KB ≈ S-Oil > GS건설 > 삼성E&A.**
Rationale in one line each: DB손보 and GS carry real-hands flow **with no short overhang and a discount
to sector**; KB and S-Oil carry the same theses at **fuller prices**; GS건설 carries the best accumulation
print **against a 3.79% building short**; 삼성E&A is **🟡 uncalled with 0.66x volume** and its thesis
resolves on a **07-24 binary** — i.e. it is a *catalyst* position, not a *flow* position.
**No order is implied, staged, or authorised by this file.**

## ✅ EXIT CHECK
- [x] **Every DEEP sector has a section** — FIN §B/§C (candidates), ENRG §B/§C (candidates), **HLTH §B (Neutral, no candidate promoted — stated)**, **STPL §B (UW, none qualify — stated)**. Plus INDU carried from EVENT_ALPHA cards.
- [x] **Cross-sector LIVE shortlist names included or explicitly dropped with reason** — §F, all 8 dispositioned.
- [x] **Numbers cross-checked** — all six Fwd PERs reconciled against 현재가÷추정EPS (§A). **Blanks are blanks** (배당%, peer averages) with the `.KS`-suffix defect named as the cause.
- [x] **Flow/positioning cross-read present per candidate** (§C), including the **GS건설 3.79% 크라우디드 short** that upstream stages missed and the **FIN overheat (RSI 81–85)**.
- [x] **`BET_SHEET.md` written as ONE file.**
- [x] Corrections applied to my own earlier stages: **삼성화재 → DB손보** (card 5), **SK이터닉스 dropped** (SWEEP), **GS건설 "cleanest print" qualified** (SWEEP/EVENT_ALPHA).

**→ proceed to ALPHA.**

---

# §H ALPHA FRESHNESS GATE (Stage 7) — 🟢LIVE / 🟡PARTIAL / 🔴RESOLVED

> The whole pipeline runs on lagging data (news ≤60d, EOD primaries). This gate asks per bet:
> **has the catalyst already fired, has the move already been made, is the thesis already consensus?**
> Method: `theme-age --scope domestic` (deterministic, token-0) **first**, then KRX/KIS positioning
> actuals, then targeted live WebSearch. **🔴 is DROPPED from the bettable list AND logged**, so
> "but it's cheap" cannot resurface next run.

## §H1 Deterministic novelty (`theme-age --scope domestic`, run 2026-07-20)
| Theme | Verdict | age(d) | accel | n | Read |
|---|---|---|---|---|---|
| 정제마진 | **🟡ACCELERATING** | 81 | **2.34x** | **28** | Accelerating on a *tiny* base = genuinely early |
| 신축매입임대 | **🟡ACCELERATING** | 69 | **2.14x** | **6** | Only 6 articles — the freshest, least-consumed thesis on the sheet |
| 대미투자 | **🟡ACCELERATING** | ≥90 | **17.14x** | **371** | ⚠ **17x accel on 371 articles = LOUD, not under-covered** |
| 손해보험 | **⚪ECHO** | ≥90 | 0.8x | 61 | Consumed — per the rule, needs *stronger* live evidence to survive |
| 코픽스 | **⚪ECHO** | 70 | 0.62x | 133 | The rate-transmission story is consumed |
| 자사주소각 | **🔴FADING** | 14 | **0.0x** | **1** | ⚠ See the interpretation note below — this is *not* a kill |

⚠ **`theme-age` measures ATTENTION, not truth (P4).** 자사주소각 at 0.0x/n=1 does **not** falsify the
buyback leg — DEEP-FIN verified the filings themselves (KB 취득결과+소각결정 **07-16**, 하나 **07-14**).
It says the leg is **uncrowded**, which for a thesis is the favourable reading. Do not invert an
attention metric into a fundamental one.

## §H2 ★ Live-search corrections — two bets changed materially

**(1) 대미투자 1호 — my EVENT_ALPHA card 8 premise is NOT confirmed. 🟡PARTIAL, residual stated.**
- I wrote "**1호 = 에너지 프로젝트**" from a single mt 07-20 body line, and routed exposure to 삼성E&A
  (에너지 EPC) while dismissing 조선 on flow. Live search says the street framing is
  **"미뤄지는 대미투자 1호 프로젝트 발표…원전·조선으로 압축되나"** — i.e. narrowing to **원전·조선**,
  with **Louisiana LNG** also in scope. **My exposure routing may be wrong**, and the 조선 leg I
  dismissed is partially rehabilitated by the *thesis* even though its *flow* stays weak-hands.
- **Base rate is against the up-branch:** the 1호 announcement has slipped repeatedly — "6월 이후"
  → "이르면 7월" → "미뤄지는". **Delay is the historically favoured branch**, which raises the
  probability weight on card 8's DOWN branch relative to how I wrote it.
- **Positioning gate:** 삼성E&A is **🟡중립 with 서지 0.66x** — real-hands but *no volume*. A
  catalyst position, not a flow position. **Tag: 🟡PARTIAL. Residual = (a) which sector the 1호
  actually names, (b) whether it lands inside 07-22~24 at all.**

**(2) 석유 최고가격제 — DEEP-ENRG's "biggest anti-signal" is REAL and DATED, but softer than stated.**
- Confirmed: the **7th cap cut 150원/L across all grades from 06-27, applied for 4 weeks**
  (휘발유 1,784 / 경유 1,773 / 등유 1,380). **4 weeks from 06-27 ⇒ the 8th notice is due ≈07-24~25.** ✅
- **Two mitigants DEEP did not weight:** (a) the 7th cut was made *because* crude fell to the **$70s**
  on a US–Iran ceasefire — **crude is now back to Brent $90.85**, so the 8th revision faces *rising*
  input cost and a cap **hike** is the mechanically consistent move, not a further cut; (b) the
  government is **already running 정유사 손실보전** (loss compensation), with "유종별 원가" as the
  core issue.
- **Net: still a live dated binary inside the ENRG horizon, but the tail is compensated and the
  direction is not obviously adverse.** Bracket both ways; do not carry it as a one-way kill.

## §H3 The gate — per-bet tags

| Bet | Tag | Evidence label + date | Flags |
|---|---|---|---|
| **078930 GS** (ENRG) | **🟢 LIVE** | 정제마진 🟡ACCEL **2.34x on n=28** (07-20); Brent **$90.85 +3.12%**, first >$90 since 06-11 [yonhap 07-20 07:40]; 3 broker notes explicitly holding the thesis through a *falling*-oil branch (신한 07-12 / 하나 07-07 / 한투 07-08); PBR **0.51**, 외인 **20.45%**, 공매도 **0.0%** (07-16) | ✅ Cleanest on the sheet. **Only name with RS20 AND RS60 both positive.** No momentum-only flag, no positioning demotion |
| **005830 DB손해보험** (FIN) | **🟡 PARTIAL** | 손해보험 theme **⚪ECHO 0.8x** (07-20) — consumed; but the bet rests on **valuation + flow**, not the news theme: PER 7.0 / PBR 0.85 / upside +34.9%, 기관 **+69.7만**, 공매도 **0.01% flat** (07-16) | ⚠ **Residual: ECHO theme.** Per the rule, an ECHO thesis needs stronger live evidence — supplied by filings/flow, **not** by narrative. ⚠ **RSI 83.7 = overheat: hard-stop required on entry timing** |
| **105560 KB금융** (FIN) | **🟡 PARTIAL** | 코픽스 **⚪ECHO 0.62x**; 자사주소각 **🔴FADING 0.0x/n=1 = uncrowded, verified by filing** (KB 07-16); Fwd PER 10.0 vs 업종 9.33 = **slight premium** | ⚠ **Not cheap** — carried on capital return, not multiple. ⚠ **RSI 81.4 overheat: hard-stop required** |
| **006360 GS건설** (INDU) | **🟡 PARTIAL** | 신축매입임대 **🟡ACCEL 2.14x on n=6** = freshest thesis here; policy **in force 07-20, retroactive**; 외국인 **+148만** AND 기관 **+225만** (07-16) | ⚠⚠ **POSITIONING FLAG: 공매도 3.79% float, BUILDING 🔥크라우디드** (07-16) — squeeze fuel **and** downside pressure; **never a standalone buy, hard-stop required.** ⚠ **MOMENTUM-ONLY CHECK: RS20 +23.3% but RS60 −40.2%** — the 20d strength sits on a badly broken 60d base |
| **010950 S-Oil** (ENRG) | **🟡 PARTIAL** | Same 정제마진 thesis as GS, but **consensus upside +7.70%, PBR 1.76, 외인 79.87%** | ⚠ **The move is substantially made.** Right thesis, **priced vehicle** — GS expresses the same thesis at PBR 0.51. ⚠ 공매도 0.48% building, approaching the 0.5% 주목 line |
| **028050 삼성E&A** (INDU) | **🟡 PARTIAL** | 대미투자 **🟡ACCEL 17.14x on n=371 = LOUD**; live search: 1호 **repeatedly delayed**, framing **원전·조선**, not clearly 에너지 EPC | ⚠ **Thesis-routing unconfirmed (§H2-1).** ⚠ **서지 0.66x = no volume.** Catalyst position on a **07-24 hard binary** with delay as the base-rate branch |
| **000810 삼성화재** (FIN) | **🔴 RESOLVED — DROPPED** | Consensus upside **+2.98%**, PBR 1.23, OBV bearish divergence, 공매도 0.71% **building**, **zero return filings in 30d** (DEEP-FIN, 07-20) | **Logged:** the 손보 margin thesis is right, but **this vehicle has already made the move.** Replaced by DB손보. Do not resurface on "it's the sector leader" |
| **475150 SK이터닉스** (ENRG) | **🔴 RESOLVED — DROPPED** | Short balance **flipped covering → building +0.54 at 3.12%** (07-16), **falsifying** the 07-16 squeeze thesis | **Logged:** the squeeze premise is dead, not merely weaker. Do not resurface on "still real-hands" |
| **HLTH (삼바/셀트리온)** | **🔴 RESOLVED for this run — NOT bettable** | 제약 wflow is **99.6% two names**; PolyPeptide is **debt-funded** (increases rate sensitivity, contradicting M-07) and **conditional on 66.7% tender vs 55.65% committed**; 삼바 SPY-relative RS20 **−2.7%**, 서지 0.71x, OBV 분배 −67% | **Logged:** a fresh ₩2.7조 catalyst landing on a name **money is leaving**. Do not resurface on "the acquisition is transformative" until the tender clears 66.7% |
| **STPL (6 greens)** | **🔴 RESOLVED — DROPPED** | Breadth signal is **4 사조-group affiliates + 1 애국테마 meme on a 상폐-우려 stock**; 기관 20d net **+3.5만주 < KT&G alone** | **Logged:** the sector's "breadth" was a metric artifact. Do not resurface on "eqflow is positive" |

## §H4 Flags summary (stamped where they apply)
- **Hard-stop required (positioning):** **GS건설** (3.79% building short, 🔥크라우디드) · **S-Oil** (0.48% building).
- **Hard-stop required (overheat):** **KB (RSI 81.4)** · **DB손보 (RSI 83.7)** · 하나금융 (RSI 85.4, alternate).
- **Momentum-only risk (RS green on a broken base):** **GS건설** (RS20 +23.3% vs RS60 −40.2%) ·
  삼성E&A (RS20 +6.9% vs RS60 −27.7%).
- **Weak-hands positioning demotion (KR rule):** none of the §A finalists — all six are 외국인/기관
  순매수. The demotion **was** applied upstream and removed 금호타이어, 삼성전자, SK하이닉스, 한화오션,
  삼성중공업 from consideration.
- **No name is stamped 🟢 except GS.** That is the honest output of this gate, not a hedge.

## §H5 ACTION_TICKETS
**Not produced — `ACTION_TICKETS.md` is US-desk-only** (`industry_kr` excludes CYCLE_EXPOSURE /
ACTION_TICKETS per the protocol composition). No tickets, no dry-run share counts, no staged orders.

## ✅ EXIT CHECK (Stage 7)
- [x] **Every §B tag filled** with an evidence label + date (§H3); **4 × 🔴 dropped AND logged with why**
      (삼성화재 · SK이터닉스 · HLTH · STPL) so each is blocked from silent resurfacing.
- [x] **Momentum-only and positioning flags stamped** where they apply (§H4) — incl. the GS건설
      3.79% 크라우디드 short and the FIN RSI 81–85 overheat cluster.
- [x] **`theme-age` run FIRST** as the deterministic gate before any WebSearch spend; ECHO/FADING
      theses required stronger live evidence and are tagged 🟡, not 🟢.
- [x] **Live search performed per bet** — and it **changed two bets** (§H2): 대미투자 routing
      unconfirmed + delay is the base-rate branch; 석유 최고가격제 confirmed dated but with
      compensation/crude-direction mitigants DEEP had not weighted.
- [x] **(US) ACTION_TICKETS — N/A for industry_kr**, stated rather than skipped silently.

**→ PROTOCOL COMPLETE.**
