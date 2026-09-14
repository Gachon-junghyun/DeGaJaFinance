# EVENT_ALPHA — industry_US · 2026-08-12 · Stage 5/11 (L1·EVENT_ALPHA)

> Bottom-up complement to MACRO's top-down matrix: **which stories are building, and is money already
> following.** Scope **`--scope foreign`** on every call (hard rule). Analytical only (P4) — this stage
> never sizes.
> Narrative **asof 2026-08-10** · money **asof 2026-08-11** — a **one-day skew, stated inline** (C1).

## 🚨 0. The stage's own instrument state, stated BEFORE any card

**This stage cannot body-read anything today.** Both news query routes are dead (PREFLIGHT G1: remote
`/exec` returns `URLError`; local FTS index **0 bytes**), so `search`/`fts`/`chain_hop`/`theme_age` are
all unavailable. What **does** run is `thread`, because it reads the **client-owned** `news_vectors.db`
rather than the query API — and that store stops at **2026-08-10 21:45 UTC** with its sync cursor at
**2026-08-11 08:00 KST**.

**Two consequences, and neither is negotiable:**

1. ★★★ **Every one of the 300 multi-day threads reads `ENDED`, and that tag is 100% an artifact.**
   `thread --days 7` reports **살아있는 0** (zero alive) — because the window's last two days are
   **08-11: 0 articles · 08-12: 0 articles** against a weekday mean of ~750. The tool prints this
   warning itself (*"윈도우 끝이 휴일/저물량이면 FADING 이 과대해진다 — per-day 분모 먼저"*).
   ⇒ **NO thread may be called ENDED, FADING or DEAD today, and no card is filed to the rejection
   ledger on a story axis.** A `DEAD` verdict needs both axes and this desk has one.
2. ★★ **Every card below is `[title-only]`, i.e. D6 **C-grade**.** The stage's own EXIT CHECK says
   *"headline-only cards are a failed stage — the biggest measured thread was a LOSS the headline never
   said."* ⇒ **this stage refuses the CONFIRMED-EARLY hand-off entirely.** No name below goes to BET as
   a fresh candidate. The cards exist so ROTATION has the sector-level cross-evidence, **graded**.

**Selection, logged (no silent truncation):** 2,823 daily events → **2,315 threads** (multi-day **300** ·
one-day 2,015, of which **0 new today**). Of the 300, the tool surfaced the **10 largest by peak**;
**8 selected** for cards (the protocol's cap), **2 not selected** — *"Senate Confirms Todd Blanche"*
(peak 13, no market transmission this desk can name) and *"First OpenAI, now Meta — why do AI hacks keep
happening"* (peak 13, folded into Card 6 as the same object). **The remaining 290 multi-day threads were
NOT read** — they are the denominator and are named as unread, not as absent.

---

## Card 1 — 🛢 **"Oil prices, stocks surge as Hormuz closure drags"** · CONFIRMED (money + story agree)

- **Thread**: `[08-06~08-10] 13→16→6→7→20` · **peak 20 outlets, and the peak is the LAST readable day**
  — the only top-10 thread whose curve is at its maximum on 08-10. Denominator: 720 articles that day.
- **Direction** `[title-only — NO body read available, §0]`: the title asserts closure *persisting*, not
  resolving. ⚠ **Card 3 is the same object read the other way and is still alive** — the two are not
  reconciled here.
- **Exposure** (flow asof 2026-08-11, 3-axis, bench SPY):
  | Name | Chain position | Flow | Note |
  |---|---|---|---|
  | **CVX** | integrated major | **🟢가속** +0.560, RS20 +5.7 | ⚠⚠ **VELOCITY-LIT (surge 0.98, vel 1.64)** — SWEEP §2a: its 🟢 rests on the axis PREFLIGHT G1 revoked. **Not citable as a money signal** |
  | **XOM** | integrated major, headline layer | 🟡 +0.594, RS20 +7.6, OBV 매집 | **FINRA z −0.41 — the only clean-rise on this run's pull** |
  | **COP** | E&P | 🟡 +0.672, RS20 +10.1, OBV 매집, surge 1.01 | one hop past the majors |
  | **OXY · EOG** | E&P | 🟡 +0.339 / +0.442 | thinner |
  | **STNG · FRO** | tankers — the freight leg | 🚨 **NOT IN `us_top300`** | **no flow, RS or short row exists.** "Not measured," never "no signal" (G5) |
- **The money, independent of the story**: `CL=F` **+10.611% over five settled sessions**; XLE exc5
  **−6.95 (08-07) → +4.22 (08-11)**, worst-to-best of eleven in two sessions; **WTI spec positioning at
  the 18th percentile SHORT and adding +3,275** (fresh 08-11 COT).
- **Future — both branches**:
  - **IF the closure thread keeps building AND XLE holds exc5 > 0** → the ENRG N+ has a live macro
    carrier for the first time since 08-05, and the squeeze geometry (crowded short into a supply
    rally) is the marginal buyer. **Track KPI**: `CL=F` settle · XLE exc5 · **S67 refiner median RS20
    (+8.392) settles 2026-08-13** · the 08-14 COT.
  - **KILL** → a settled `CL=F` close back below **78.18** (the 08-07 level, i.e. the whole move given
    back) **or** XLE exc5 turning negative on a settled close. Either falsifies the card outright.
- **Cell**: **CONFIRMED — but at the CROWDED layer** (peak-20 outlets is the headline layer by
  construction). **Horizon 2026-08-13.** ⚠ Handed to ROTATION as sector evidence; **no name handed to BET.**

## Card 2 — ⛽ **"Ukraine hits refineries deep inside Russia"** · CONFIRMED (the product-supply leg)

- **Thread**: `[08-06~08-10] 20→19→12→11→16` · peak 20, **rising again into 08-10**.
- **Direction** `[title-only]`: physical refining capacity being removed. **This is the one card whose
  mechanism is a *product* mechanism rather than a crude one** — which is exactly the leg S55 was
  written to isolate and **could not** (it scored **C** at +3.217pp, §HANDOVER 2b).
- **Exposure**: **MPC** 🟡 +0.750, RS20 +8.4, RS60 **+32.2**, OBV 매집, surge 1.15 · **VLO** 🟡 +0.514,
  RS20 +5.0, RS60 +29.3 · **PSX** 🟡 +0.443, RS20 +8.9, RS60 +27.8, surge 1.10 (all asof 08-11).
  ⚠ **None is 🟢** — the tag gate blocks all three on `vol_surge`, which SWEEP §2a shows is the modal
  block, **not** a money verdict.
- **The money**: **S67's median RS20 = +8.392 with all three legs positive and rising** (was +3.852 on
  08-07). `HO=F` **+13.828%/5 sessions**, outrunning crude by **+3.2pp**.
- **Future — both branches**:
  - **IF the strikes continue AND the refiner median RS20 stays > 0** → the margin leg is physical and
    **S55's branch B direction is right even though its threshold was not met**. **Track KPI: S67
    settles 2026-08-13.**
  - **KILL** → S67's median RS20 turning ≤ 0 at the 08-13 settle, **or** a settled `HO% − CL%` ≤ **−3.0**
    (S55 branch A's frozen line), which would say the product leg is *weakening* independently.
- ⚠ **R47 binds**: no stage may state *"the distillate bottleneck released"* as established fact.
- **Cell**: **CONFIRMED.** **Horizon 2026-08-13.**

## Card 3 — ☮ **"Iran says Hormuz deal close amid attack on UAE tanker"** · CONTRADICTS Card 1 — carried, not resolved

- **Thread**: `[08-06~08-10] 14→12→15→9→7` · peak 15, **decaying into 08-10** — the mirror image of
  Card 1's curve over the identical window.
- **Direction** `[title-only]`: reconciliation. ★ **The point of this card is that two threads about the
  same strait ran simultaneously in opposite directions for five days, and the DECAYING one is the
  peace thread.** That is the shape P41 registered on 08-10 (*"the reopening condition is named and it is
  NOT the Oman track"*) — **and it is carried UNREFRESHED**, because §0 forbids a fresh read.
- **Exposure**: the **inverse** of Card 1 (airlines as fuel-cost beneficiaries). **UAL · DAL**:
  ⚠ **S54 could not be scored — its frozen text names an anchor and a session count that disagree
  (`D233`)**, giving **−1.467 (branch C)** or **−5.130 (branch B)** depending on construction. **This
  card therefore has no scored money leg and says so.**
- **Future — both branches**:
  - **IF the peace thread re-accelerates while crude falls** → Card 1 is wrong and **S74's reopening
    condition set (→2026-08-24) becomes the live object**.
  - **KILL** → an unconditional Iranian "Strait open" statement, which is **`S8`'s registered trigger —
    un-scoreable for a TENTH run and needing a human (P5)**.
- **Cell**: **STORY-ONLY (money axis unavailable).** **Horizon 2026-08-24 (S74).** ⚠ Filed to **neither**
  ledger: a rejection needs a money verdict this desk does not have today.

## Card 4 — 🚀 **"SpaceX insiders get their first chance to sell"** · CONFIRMED, and it moved a METHOD rule

- **Thread**: `[08-06~08-10] 14→10→5→5→9` · peak 14, **re-accelerating into 08-10**.
- **Direction** `[title-only]`: a dated, share-counted supply event (up to **911.5M shares**, float ~5%
  → ~12%).
- **The money — and it is the whole point**: **S56 FIRED-A at +27.722pp** (SPCX 108.27 → 138.74 over the
  three settled sessions straddling the 08-06 unlock, vs SPY). **The counted short (219.3M sh ≈ 34% of
  float) beat the counted supply by 24pp over branch A's line.**
- ★★★ **What this changes is a rule, not a tilt**: this desk carries **`D6` — "positioning is not a
  signal"** — in its REJECTED ledger. **D6 survives for *percentile* positioning and is measured wrong
  for *share-counted* positioning.** ⇒ **PREMORTEM owns writing the scope limit** (it is a method
  conclusion, and the desk holds no SPCX exposure).
- **Exposure**: **SPCX — 🚨 not in `us_top300`**, so no flow/RS/short row exists; the bracket was scored
  on a hand-built price series, **disclosed at registration**.
- **Future — both branches**:
  - **IF** a second share-counted unlock resolves the same way → the scope limit is a rule, not an n=1.
  - **KILL / VOID** → a lock-up waiver, staged release, secondary or index inclusion inside the window.
    ⚠⚠ **This check COULD NOT BE RUN** (the D149 evidence standard needs the news path, §0). **The
    verdict is recorded with that gap named, not laundered.**
- **Cell**: **CONFIRMED (method).** **Horizon: the next share-counted unlock, undated `[blank]`.**

## Card 5 — 💼 **"US Loses 23,000 Jobs in July, Unemployment 4.1%"** · the money answered and the answer was counter-intuitive

- **Thread**: `[08-07~08-08] 21→5` · **peak 21, the largest single peak in the readable window**, and it
  collapsed in one day.
- **Direction** `[title-only, both halves cited — C2]`: payrolls **−23,000** against a **+83,000**
  consensus, **and** unemployment **4.1%, DOWN from 4.2%** — the rate fell on a shrinking denominator.
- **The money, settled and scored**: **`DGS2` +7bp · 2s10s +2bp to +0.47 · HY OAS −5bp to 2.70.**
  Three brackets settled together — **S51 FIRED-A · S66 FIRED-B · S70 FIRED-A** (HANDOVER §2b).
- ★ **The card exists because the story and the money point opposite ways and the money is scored**: a
  contracting payroll print produced a **front-end selloff and a credit tightening**. The growth-scare
  reading is refuted on this desk's own primary series.
- **Exposure**: **JPM** 🟢 (⚠ **velocity-lit, surge 0.56** — SWEEP §2a) · **BRK-B** 🟢 (⚠ velocity-lit,
  surge 0.92) · **BAC** 🟡 +0.290 · **WFC** 🟡 +0.085. **These four ARE S65's frozen basket**, which
  scored **C** at median RS20 **+2.871** — neither conversion nor collapse.
- **Future — both branches**:
  - **IF** tonight's CPI extends the front-end selloff → **P46-A** and FIN keeps the mechanism.
  - **KILL** → HY OAS ≥ **2.96** on a settled close (S70's own branch-B line, **26bp** away), which
    would say the credit read was a publication-lag artifact after all.
- **Cell**: **CONFIRMED-then-CONSUMED** — the event is scored and the thread is spent. **No forward
  candidate.** **Horizon: the CPI macro settle.**

## Card 6 — 🤖 **"AI has now moved beyond…" + the AI-breach thread** · ★ STORY-ONLY — the cleanest divergence on the board

- **Thread**: `[08-06~08-10] 13→8→10→7→16` · **rising into 08-10, peak on the last readable day**
  (merged with *"First OpenAI, now Meta — why do AI hacks keep happening"*, `13→9→3→6`).
- **Direction** `[title-only]`: AI narrative broadening.
- **The money says the opposite, and it is not close**: **IT `eqflow −0.218` is WORSE than
  `wflow −0.151`** (the average name lags the cap-weighted index), **23 reds of 56**, `XLK` exc5
  **−0.33** / exc20 **−1.15**. Name level: **MU 🔴** (−0.861, RS20 −14.1) · **AMD 🔴** (−0.711, RS20
  −16.0) · **META 🔴** (−0.844, RS20 −11.9) · **GOOGL 🟡** (−0.531, RS60 −17.3). The exceptions are
  **MSFT** 🟡 (+0.517, RS20 **+28.4**) and **PLTR** 🟢 (+0.817, surge **1.27 — volume-confirmed, not
  velocity-lit**).
- **Future — both branches**:
  - **IF** the thread keeps building **and** IT's eqflow crosses above its wflow → money is arriving at
    the average name and the divergence resolves toward the story.
  - **KILL** → IT eqflow staying below wflow for two more settled runs ⇒ the AI narrative is being told
    about a sector whose breadth is deteriorating, and the card is a **story about six names**.
- **Cell**: ★ **STORY-ONLY.** **Dated re-check 2026-08-14.** ⚠ **Not filed to the rejection ledger** —
  §0 forbids a story-axis drop today, and the money axis alone is not a DEAD verdict.

## Card 7 — 📱 **"Meta ordered to pay $567M in New Mexico child-harm case"** · precursor shape, negative direction

- **Thread**: `[08-06~08-07] 2→20` · ★ **the only PRECURSOR-form curve in the readable set** (starts at
  2 outlets and jumps to 20) — the shape the protocol says to select first.
- **Direction** `[title-only]`: an adverse judgment, i.e. a **cost**, not an opportunity.
- **The money agrees**: **META 🔴분산**, flow −0.844, RS20 −11.9, RS60 −6.1, OBV 분산, surge 0.68 —
  and the sector is the board's worst: **XLC negative on all four windows (−0.18 / −0.59 / −2.65 /
  −7.98)**, `wflow −0.474` vs `eqflow −0.016` (a **0.458** gap owned by GOOGL at 38.2% of sector cap).
- **Future — both branches**:
  - **IF** the thread extends into further jurisdictions → the COMM UW gains a **named, dated** carrier
    rather than resting on flow alone.
  - **KILL** → META's OBV flipping to 매집 with RS20 crossing 0 ⇒ the ruling was a single-event cost the
    tape absorbed.
- ⚠ **R56 binds any COMM breadth claim: EA is a delisted security still sitting in `us_top300.csv`.**
- **Cell**: **CONFIRMED-negative** (story and money agree on the downside). **Horizon 2026-08-19.**

## Card 8 — 🕊 **"Netanyahu says Israel rejects Trump's Gaza peace"** · UNMAPPED — named, not dropped

- **Thread**: `[08-09~08-10] 13→6` · peak 13.
- **Direction** `[title-only]`: geopolitical escalation risk, **distinct from the Iran/Hormuz axis**.
- **Exposure**: 🚨 **this desk cannot map it.** The transmission would run through crude and freight —
  **already owned by Cards 1–3** — or through defense, where **RTX** 🟡 (+0.556, RS20 **+13.3**) is the
  only book-relevant name and its move is not attributable to this thread on a title-only read.
- **Future**: **KILL** → any settled session where crude and RTX move in opposite directions ⇒ the
  threads are separable and this one has no independent transmission.
- **Cell**: **UNMAPPED — recorded so it cannot later be discovered as a "new" story.** This is the
  `D168` class (a Red-Sea/Levant event that fires none of the Iran-scoped brackets); **S61** is the
  nearest instrument and it is **1.78pp from its branch B** at the 08-12 settle.

---

## 9. Book cross-check — ENDED threads under open positions

⚠⚠ **This section cannot be executed as written today, and that is the honest output.** The check is
*"any ENDED thread that an open position's thesis rides on"* — but **§0 established that all 300 threads
read ENDED for instrumental reasons**, so the test would flag **every** position and mean nothing.

**What is stated instead, positively**: the paper book's holdings map to the readable threads as
**AVGO · NVDA · TSM → Card 6 (STORY-ONLY)** · **KMI · LNG → Cards 1–2 (CONFIRMED, but KMI is 🟡 with
RS20 −5.7, i.e. the pipeline leg is NOT participating in the crude move)** · **RTX → Card 8 (UNMAPPED)**
· **MA · VST → no readable thread at all.** 🚨 **LNG and TSM cannot be tagged on any axis (G5, 12th
run).** **No book flag is emitted this run**; the next run with a live news axis owes this check.

## 10. Hand-off

| To | What |
|---|---|
| **ROTATION** | **ENRG**: Cards 1+2 are the sector-level cross-evidence, and they **CONFIRM** MACRO §G's promotion argument from the bottom up. **IT**: Card 6 is a **STORY-ONLY** divergence and argues **against** any IT upgrade. **COMM**: Card 7 gives the UW a named carrier. **HLTH · MATR**: **no thread reached them at all** — their case rests entirely on SWEEP §4's filter-artifact diagnosis, not on narrative |
| **BET** | 🚫 **NOTHING.** Every card is `[title-only]` (§0) and the stage's own EXIT CHECK makes a headline-only card ineligible for the CONFIRMED-EARLY hand-off. **Zero fresh candidates are handed forward this run** |
| **PREMORTEM** | **Card 4's method finding: `D6` needs a scope limit for share-counted positioning.** Also **Card 8's unmapped thread** and **S8's tenth un-scoreable run** |
| **Ledgers** | **Zero rejections and zero missed entries filed from this stage** — both require a money-or-story verdict this desk cannot form today, and a filing made on half an instrument is worse than none |

---

## ✅ EXIT CHECK

- [x] **Scope market-correct** — `--scope foreign` on every call; no cross-market feed cited
- [x] **Selection logged** — 2,823 events → 2,315 threads (multi-day 300 · one-day 2,015) → **10 surfaced → 8 carded, 2 named as not-selected, 290 named as unread.** No silent cap
- [ ] ⚠ **Direction body-read NOT done — the instrument is dead (§0).** Rather than fail silently, **every card is graded `[title-only]` (D6 C-grade) and the CONFIRMED-EARLY hand-off is REFUSED entirely.** This checkbox is left unticked deliberately: the stage did not meet its own standard and says so
- [x] **Every exposure name carries a flow tag with its asof date**; the six **velocity-lit** greens are marked wherever they appear (SWEEP §2a); **STORY-ONLY names did not leak into any hand-off** — because no hand-off was made
- [x] **Every card carries both branches, a kill condition and a dated horizon** (Card 4's horizon is `[blank]` — **not guessed**)
- [x] `EVENT_ALPHA.md` written; **ENDED-thread book flags NOT emitted, with the reason measured (§9)**; **no ledger filing made, with the reason stated (§10)**

---
---

# ═══ RUN-2 ADDENDUM · EVENT_ALPHA — 2026-08-12 22:55–23:15 KST · **APPEND-ONLY** ═══

> Nothing above is rewritten. Analytical output only — **no buy/sell language, no sizing** (P4).
> **This is the stage RUN-2 exists for.** RUN-1 ran EVENT_ALPHA with the news axis **dead** (G1 FAIL:
> `brief` returned 0 articles, `thread` returned 0 events for 08-11 and 08-12). RUN-2 has
> **2,237 articles → 337 events for 08-12** and **481 multi-day threads, 122 alive**.

## §R2-0 · Selection ledger — no silent truncation

| Item | Count |
|---|---|
| Multi-day threads in window | **481** |
| **Alive** (BUILDING / REIGNITED) | **122** |
| **Selected for cards** | **6** |
| **NOT selected** | **116** — dominated by non-market-transmitting clusters (solar eclipse [7 outlets], Zhu Rongji obituary [7], Zimbabwe ferry, North Korea missile [5], Europe heatwave, Tata Sons succession, FX pair commentary threads) |
| Selection rule applied | **precursor-form first** (curve starting ≤2 outlets and climbing), then remaining BUILDING/REIGNITED by peak |

⚠ **All flow tags below are RUN-2 direct 4-axis `module_flow` calls, 22:45–22:55 KST, bench SPY named
inline, on the 2026-08-11 settled bar.** They are **not** sweep outputs and may not be differenced
against RUN-1's 3-axis sweep scores (G2). ⚠ **No 08-12 price exists** — nothing below is a reaction to
the CPI print.

---

## CARD 1 · ★★★ The AI bottleneck moves to the electrical layer — **precursor form, and the thread's own two candidates split**

- **Thread**: *"Jabil: The AI Infrastructure Bottleneck Is Moving Into I…"* → *"Better AI Infrastructure
  Stock: Vertiv vs. Eaton"* · **BUILDING 2→4 outlets** (08-11→08-12) · window denominator
  **337 events / 2,237 articles today**.
- **Why it is first**: it is the **only precursor-form thread on this desk's transmission path** —
  starts at 2 outlets and climbs, the measured shape that gave 5 days of runway in the BOK case.
- **Direction (body-read)**: the argument is that the binding constraint is migrating **from compute
  to power distribution inside the datacenter** — switchgear, busway, UPS, transformers.
- **Exposure — ★ the thread names two candidates and the money separates them cleanly:**

| Name | Chain position | Flow (4-axis, 08-11 bar) | Crowding note |
|---|---|---|---|
| **ETN** | electrical distribution / switchgear | **🟡 neutral · vel 1.11× · OBV ACCUMULATING · RS20 +12.0% · RS60 +13.6%** | the **only** name here positive on **both** windows |
| **VRT** | datacenter power/cooling — the headline name | **🟡 neutral · vel 0.98× · OBV neutral · RS20 −5.6% · RS60 −25.1%** | headline layer, **and the worst RS60 in the whole sample** |
| **PWR** | electrical construction | 🟡 · vel 1.06× · OBV accumulating · RS20 +4.0% · RS60 **−14.9%** | — |
| **JBL** | the thread's originating name | 🟡 · **vel 1.98×** · OBV neutral · RS20 +12.8% · RS60 +3.6% | narrative running ahead of money |

- ★★ **The card's content is the split, not the theme**: the story that "power is the bottleneck" is
  **13 months old in the price** for its headline name — **VRT is −25.1% vs SPY over 60 days** — while
  **ETN is +13.6% and accumulating.** The thread frames it as *"Vertiv vs. Eaton"*; **the tape has
  already answered on the 08-11 bar.**
- **Future — IF** the thread keeps building (≥5 outlets) **AND** ETN's OBV stays accumulating →
  the constraint-migration story is being **bought**, not just written. **KPI: ETN RS60 vs SPY, and
  whether VRT's RS20 crosses back above 0. Horizon: 2026-08-26** (NVDA print, the sector's next dated
  read-through).
- **ELSE / kill**: **VRT's RS20 recovers above +5% while ETN's OBV turns to distribution** ⇒ the split
  is noise and this card is falsified — it was a rotation inside one theme, not a constraint migration.
- **Cell: CONFIRMED-EARLY on ETN (money present, narrative early) · STORY-ONLY on VRT and JBL**
  (narrative present, money absent or negative). → **hand to BET as a cross-check on the UTIL/INDU
  transmission; VRT/JBL to watchlist with the kill condition above.**

---

## CARD 2 · ★★★ Oil: the deficit is now a NUMBER, and it is the day's largest cluster

- **Thread**: *"Oil rises as doubts over US-Iran deal heighten supply concerns"* · **28 articles /
  14 outlets — the day's #1 by outlet count** (dispersion 0.96). Sub-events: *"Hormuz closure squeezes
  global economy as oil demand destruction…"* [4/3] · ★ ***"IEA: Global Oil Deficit To Hit 1.8 Million
  Bpd This Quarter"*** [3/3] · *"IEA Says Oil Markets Are Facing a Wider Shortfall"* [2/2].
  Adjacent BUILDING threads: **Libya refinery drone strikes** [4→4] · **Europe gas storage at a
  historical August low** [3→2→3] · **Ukraine strikes Black Sea grain terminals** [13/9].
- **Direction (body-read)**: supply loss is being **quantified by an agency**, not asserted by a
  headline — and the loss is broadening beyond Hormuz to **Libyan refining and Russian export
  infrastructure**. ⚠ The same cluster carries the **counter-mechanism in its own sub-event**:
  *"demand destruction"* — a deficit driven by a blockade destroys demand as well as supply.
- **Exposure**:

| Name | Chain position | Flow (4-axis, 08-11 bar) |
|---|---|---|
| **PSX** | refining | **🟢 accelerating · vel 2.07× · OBV accumulating · RS20 +11.2% · RS60 +21.9%** |
| **MPC** | refining | **🟢 accelerating · vel 1.27× · OBV accumulating · RS20 +9.4% · RS60 +26.6% · vol surge 1.01×** |
| **VLO** | refining | 🟡 · vel 1.15× · OBV accumulating · RS20 +7.5% · RS60 +23.7% |
| **OXY** | E&P | 🟢 · vel 1.47× · OBV accumulating · RS20 +6.3% · RS60 −6.6% |
| **XOM · CVX** | integrated (headline layer) | 🟡 · vel 0.82× / 0.85× — **both BELOW 1** |
| **KMI · LNG** | midstream / LNG | **🔴 · KMI vel 0.40× (lowest in sample) · LNG OBV distribution** |

- ★★ **The crowding read is the finding**: the **refining** leg is where narrative *and* money agree
  (three names, all OBV-accumulating, RS60 +21.9 to +26.6), while the **integrated headline layer runs
  news velocity BELOW 1** and **midstream is outright distributing.** ⇒ **"Energy is working" is false
  as a sector statement and true as a refining statement** — consistent with the sweep's **breadth
  0.06** on 16 Energy names (SWEEP §R2-5).
- **Future — IF** the IEA deficit persists **AND** refiner OBV stays accumulating → the crack-spread
  leg keeps carrying the sector. **KPI: MPC/PSX RS60 vs SPY; the IEA quarterly deficit revision.
  Horizon: 2026-08-24** (S74's Hormuz date).
- **ELSE / kill**: **a dated, ≥2-outlet-body-corroborated Strait reopening** (S74's registered
  observable) **OR** refiner OBV turning to distribution while RS20 stays positive ⇒ the premium is
  unwinding and this card dies. ⚠ **Demand destruction is the silent third branch** — if crude rallies
  while refiner RS20 rolls over, the deficit is destroying the customer, not the margin.
- **Cell: CONFIRMED-EARLY (refining) · STORY-ONLY (integrated, midstream).**
  → **hand to ROTATION as the ENRG breadth caveat; to PREMORTEM as S74's live tape.**

---

## CARD 3 · ★★ Optical / interconnect — two names inflect, the third does not

- **Thread**: *"Market's Momentum Darlings Resurface as Optical Stocks Tak…"*, inside the head cluster
  *"The Stock Market Is Flashing the Same Warning Signal That It…"* [11/6].
- **Why it matters here**: **S48** registered the optical/interconnect layer (→ 2026-09-30) as *"the
  layer no bracket has ever covered."* **This is the first run with a live news axis since.**
- **Direction (body-read)**: leadership rotating **back** into optical after a drawdown.
- **Exposure — and the layer is NOT uniform:**

| Name | Flow (4-axis, 08-11 bar) | Shape |
|---|---|---|
| **ANET** | **🟢 · vel 2.59× (highest in sample) · OBV accumulating · RS20 +17.6% · RS60 +40.7%** | **both windows strongly positive — no inflection needed, already leading** |
| **COHR** | **🟢 · vel 1.95× · OBV accumulating · RS20 +14.2% · RS60 −13.3% · vol surge 1.23×** | ★ **inflection shape**: recent window positive, older negative |
| **LITE** | **🟢 · vel 1.47× · OBV accumulating · RS20 +14.1% · RS60 −14.3%** | ★ **same inflection shape, near-identical magnitudes** |
| **CIEN** | **🔴 distributing · vel 0.95× · RS20 −2.6% · RS60 −29.2%** | **does not participate** |

- ★★ **COHR and LITE carry the same signature to within 0.3pp on both windows** (RS20 +14.2/+14.1,
  RS60 −13.3/−14.3) — **two independent names describing one turn**, with **CIEN as the control that
  did not turn.** ⚠ **This is a description of a shape, not a verdict** (P4), and **RS60 is still
  negative for both** — the older window has not been repaired.
- **Future — IF** COHR **and** LITE both push **RS60 above 0** while OBV stays accumulating → the
  inflection is a re-rating, not a bounce. **KPI: RS60 crossing zero on both. Horizon: 2026-09-30**
  (S48's settle).
- **ELSE / kill**: either name's OBV turns to distribution, **or** ANET's RS20 rolls over ⇒ this was a
  laggard bounce inside a leader's trend.
- **Cell: CONFIRMED-EARLY (COHR · LITE) · CONFIRMED-LATE (ANET — money and narrative both already
  there) · dead (CIEN).** → **hand to PREMORTEM as live evidence on S48.**

---

## CARD 4 · ★★★ NVDA's $500bn financing — the story became a CREDIT story

- **Thread**: *"Nvidia's $500 Billion Financing Plan Is 20 Times What the Te…"* [11 articles /
  6 outlets] + *"Why Wall Street and Nvidia Are Building an Exotic Money Pi…"* [3/2] + ★ ***"Nvidia's
  show of financial force soothes credit markets"*** [2/2].
- **Direction (body-read)**: AI capex is being funded through a **structured credit channel**, and the
  coverage frames it as **reassuring** to credit markets.
- **Why this is the highest-information card on the board**: **S41** was registered as *"the AI-issuer
  credit channel S26's own invalidation clause explicitly excluded"* — **and this is that channel
  arriving as news, on the day the desk has no post-print credit data.**
- **Exposure**: **NVDA** (🟢 · vel 1.28× · OBV accumulating · RS20 +0.2% · RS60 **−10.9%**) ·
  **CRWV** (🟡 · vel 1.87× · OBV **neutral** · RS20 **+41.2%** · RS60 −1.4%) · **ANET** (🟢, above) ·
  credit-side observable **`BAMLH0A0HYM2` 2.70 / `BAMLC0A0CM` 0.78** `[FRED, asof 08-10]`.
- ⚠⚠ **Two cautions, both measured:**
  1. **NVDA's RS60 is −10.9%** — the epicenter name of the #1 cycle has **underperformed SPY over
     60 days** while its financing plan is described as a *"show of financial force."*
  2. **CRWV is +41.2% RS20 with OBV NEUTRAL** — a 41-point move vs SPY with **no accumulation
     signature**. **That is the definition of a crowded move, and it is the name most levered to this
     card's mechanism.**
- **Future — IF** the credit framing holds → HY/IG OAS stay at/inside **2.70 / 0.78** on the first
  `[FRED]` close covering 08-12. **KPI: HY OAS. Horizon: the S73 Leg-1 settle (08-14–08-18 on the
  current publication clock).**
- **ELSE / kill**: **HY OAS ≥ 3.10** (S26's carried kill line, 40bp away) **or** IG OAS ≥ 0.90 (12bp
  away) ⇒ the "exotic money pipe" is repricing and the AI-capex funding channel is the transmission.
- **Cell: STORY-ONLY on the credit claim** — **the desk has NO post-print credit print and cannot
  confirm "soothed"** — **CONFIRMED-LATE on NVDA itself.**
  → 🚨 **hand to PREMORTEM: this thread is the mechanism behind the un-bracketed NVDA 08-26 binary.**

---

## CARD 5 · ★★ Fed hike odds collapse — the thread that argues against MACRO §R2-C

- **Thread**: *"Cleveland Fed's Hammack: it will take more than one inte…"* [08-10, 4 outlets] →
  *"…says multiple rate hikes needed"* [08-11, 2] → ★ ***"The Odds of a September Rate Hike Have
  Plunged, but the…"*** [08-12, 7 articles / 5 outlets] · **BUILDING 4→2→5**.
  Adjacent: *"Dollar subdued as markets await US inflation data"* [23/6] · *"Gold firms below a
  10-week high"* [4] · *"Japanese Yen heading back toward 160"* [2→2→2].
- **Direction (body-read)**: **an in-line CPI removed September hike urgency** — traders moved from a
  ~50-50 hold/hike split to a **hold** tilt `[WebSearch]`. **A hawkish regional-Fed voice is being
  priced out in real time.**
- ★★ **This card is registered because it CONTRADICTS this run's own MACRO proposition `P-R2-1`**
  (that the benign print measures a stale window). **Both are on the board; the disagreement is the
  finding, and S73 settles it on tonight's bar.**
- **Exposure — where a hold-tilt transmits, per the sweep's own ranking:**
  **UTIL (wflow −0.475, weakest of 11)** and **RE (−0.222)** are the duration-sensitive sectors, and
  they are where money is **least** present. Named power/IPP tape: **CEG 🟡 (vel 1.57×)** ·
  **TLN 🟡 (vel 1.29×, RS20 −9.9%)** · **VST 🟡 (vel 2.21×)** · ★ **NRG 🔴 distributing with
  vel 3.16× — the highest news velocity of any name measured this run, and the money is leaving.**
- **Future — IF** the hold tilt holds → **S73 branch C** (`ΔDGS2 ≤ −0.15` **and** `ΔHY OAS ≤ −0.05`)
  becomes live, and **UTIL UW / RE UW are the desk's most exposed calls** (S73's own text).
  **KPI: `DGS2` at the first `[FRED]` close covering 08-12. Horizon: 08-14–08-18.**
- **ELSE / kill**: `ΔDGS2 ≥ +0.15` with `ΔHY OAS ≥ +0.10` ⇒ **branch H**, and the hold tilt was a
  one-day read of a stale window — `P-R2-1` survives instead.
- **Cell: STORY-ONLY** — **narrative is loud and the desk has zero post-print rate data.**
  ★ **NRG is the cleanest STORY-ONLY instance on the board: 3.16× velocity against OBV distribution.**

---

## CARD 6 · ⚠ S61's own observable has a **zero-velocity leg** — an instrument note, not a card

- **Thread**: Black Sea / tanker war-risk — *"Ukraine Strikes Grain Terminals at Russia's Key Black Sea
  Port"* [13 articles / 9 outlets, 08-12].
- **Measured**: **`STNG` returns news velocity `0.00×`** — 🔴 distributing, RS20 −7.6%, RS60 −13.9%.
  **`FRO` returns 1.11×**, 🟡.
- 🚨 **S61's frozen observable is EW{STNG, FRO}, and one of its two legs has a velocity of exactly
  zero on a day its own thread ran 9 outlets.** A hard zero next to a live 1.11× on the sibling name
  is **more consistent with a name-matching failure than with silence** — and **PREFLIGHT G1's central
  rule is that a zero is not evidence of absence** (reproduced today by `search "SPCX SpaceX"`
  returning 0 while `fts` returned 5).
- ⚠ **This does NOT touch S61's bands or its price observable** — S61 is scored on **price excess vs
  SPY**, which is unaffected. **The note is registered so that no stage reads STNG's `0.00×` as
  "the tanker story went quiet."**
- **Cell: none — this is a dig item, not a forward card.**
  → **hand to DRIFT/`idle_probe`: candidate name-resolution defect in the velocity axis.**

---

## §R2-7 · What this stage hands forward

| To | Item |
|---|---|
| **ROTATION** | ENRG's strength is a **refining** phenomenon (3 names accumulating) against **breadth 0.06** — the sector label overstates it. UTIL/RE weakness now has a **named counter-narrative** (Card 5) that settles tonight |
| **PREMORTEM** | 🚨 **Card 4 is the mechanism behind the un-bracketed NVDA 08-26 binary** · Card 3 is live evidence on **S48** · Card 2 is live tape on **S74** |
| **BET** | **CONFIRMED-EARLY: ETN · MPC · PSX · COHR · LITE.** **STORY-ONLY: VRT · JBL · NRG · CRWV · XOM · CVX.** ⚠ All tags are 4-axis direct reads on the **08-11** bar, pre-CPI |
| **DRIFT / idle_probe** | **STNG velocity `0.00×`** while its thread ran 9 outlets — candidate name-resolution defect |
