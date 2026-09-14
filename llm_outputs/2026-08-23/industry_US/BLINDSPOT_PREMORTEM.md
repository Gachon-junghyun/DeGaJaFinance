# BLINDSPOT_PREMORTEM — industry_US · 2026-08-23 (Sun) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **against this run's own tilt** before the DEEP budget is committed.
> Anti-tunnel. Output feeds ALPHA (brackets) and BET (cycle GAP).
> ⚠ **Declared execution constraint, 5th consecutive run**: the four lenses ran **in-context, serially**,
> not as a parallel adversarial agent fan-out. Standing session constraint, declared rather than hidden;
> the adversarial framing was applied but the independence of four separate contexts was not.

---

## ★★★ 0 · The calendar was audited before it was used, and it is wrong in BOTH directions

The protocol's run-start catalyst injection ran `catalyst_calendar.py --days 10`, which printed **five
binaries**. Because `R93` (the 08-21 run's false-positive override of this same calendar) is four days
old, **every date was re-derived from a second source and then corroborated from a news body** before
being used. The result is the sharpest instrument finding of this stage.

| Event | `catalyst_calendar` | `yfinance` calendar | **Body corroboration (`--scope foreign`)** | Verdict |
|---|---|---|---|---|
| **`NVDA` print** | **08-26** ✓ | 08-27 | `yahoo_finance` 08-21: *"Something Big Could Happen To NVIDIA Stock **on August 26**"*; 08-16: *"…After **Aug. 26**"* | ✅ **The calendar is RIGHT. `yfinance` is the outlier** (next-day convention) |
| **`MRVL` print** | 🚨 **ABSENT** | 08-28 | `yahoo_finance` 08-19: *"Dear Marvell Technology Stock Fans, **Mark Your Calendars for August 27**"* | 🚨 **08-27 — a binary the calendar does not carry** |
| **Jackson Hole / Warsh debut** | 🚨 **ABSENT** | — | `economictimes` body: *"the **August 27 to August 29** event"*; today's own probe: **22** body co-mentions of "August 27", **20** of "August 29" | 🚨 **08-27→29 — third consecutive run absent** |
| July PCE | 08-28 ✓ | — | scheduled release | ✅ |
| `AVGO` print | **09-02** | 09-03 | not corroborated to a body this run — **flagged, not resolved** | ⚠ **one-day ambiguity, recorded** |
| `FRO` · `AVGO` · MSCI review · `S8` (undated) | ✓ | — | — | ✅ |

★★ **The lesson of `R93` is applied in the direction it was learned.** That retraction was filed
because the desk read a Week-Ahead headline as a D-0 event and **overrode a calendar that was
correct**. Today the same audit **vindicates the calendar on `NVDA`** — and finds two genuine holes
elsewhere. **The audit is only credible because it was capable of clearing the tool, and it did.**

🚨 **`D18`'s most expensive instance to date, and it is quantified below**: `MRVL` reports **08-27**,
the day after `NVDA` and the day Jackson Hole opens. `MRVL` is the name that **took Alphabet custom-
silicon share from a held position (`AVGO`) on 08-19**, and its options carry the **highest implied
move on the board (±11.31%)**. **The desk's calendar cannot see the single most information-dense
binary in its own window.**

## ★★★ 0-b · `D295` DISCHARGED after four runs — the straddle table the desk has been owed

`module_flow NVDA --positioning` returns **`예상변동 ±1.6% (만기 2026-08-24, D1)`** — the **08-24
Monday** expiry, which **does not span the 08-26 print**. `D315` reproduces for a 4th run.
**The bands were therefore derived directly from the chain instead** (`yfinance`, ATM straddle at the
strike nearest the 08-21 settled close, mid where a two-sided quote exists):

| Name | Print | Spot (08-21) | Expiry **not** spanning the print | **First expiry spanning it** | **Implied move** | ATM IV (call/put) |
|---|---|---:|---|---|---:|---|
| **`NVDA`** (held) | **08-26** | 214.72 | 08-24 ±**1.61%** (IV 0.280) | **08-28** K=215, straddle **$13.12** | **±6.11%** | **0.606 / 0.588** |
| **`MRVL`** | **08-27** | 237.04 | — | **08-28** K=235, straddle **$26.80** | **±11.31%** | **1.122 / 1.096** |
| **`AVGO`** (held) | **09-02/03** | 368.45 | 08-28 ±**4.51%** (IV 0.461) | **09-04** K=370, straddle **$35.05** | **±9.51%** | **0.643 / 0.618** |
| `MU` (no print until 09-24) | — | 966.78 | 08-24 ±2.76% (IV 0.480) | 08-28 K=965, straddle **$63.90** | **±6.61%** | **0.650 / 0.643** |

**Three readings follow, and the third is the one no other instrument produced.**

1. **`S103`'s hand-set ±5.0pp bands sit INSIDE the implied move (±6.11%).** By this desk's own written
   rule — *"a bracket that fires inside the implied move is not a surprise"* — **`S103` is hereby
   pre-declared NO-INFORMATION.** ⚠ `D242` forbids re-freezing, so **`S103` still settles as
   registered**; what changes is that its verdict may not be read as a surprise either way. A
   successor with thresholds outside the implied move is registered below (**`S115`**).
2. **The event premium is measurable and large.** `NVDA` IV goes **0.280 → 0.606** between the expiry
   that misses the print and the one that spans it — a **2.16×** ratio. `AVGO` goes 0.461 → 0.643
   (**1.40×**). ⇒ **`AVGO`'s implied event move (±9.51%) is HALF AGAIN `NVDA`'s (±6.11%)**, on a print
   ~7 days later, which is not what a desk holding both would guess.
3. ★★★ **`MU` carries a HIGHER ATM IV than `NVDA` on the identical 08-28 expiry — 0.650 vs 0.606 —
   and `MU` has no scheduled print until 2026-09-24.** The options market is pricing more event risk
   into the **memory** name than into the company actually reporting.
   ⇒ **This is an independent, priced corroboration of EVENT_ALPHA Card 1**: the market also thinks
   the information in the 08-26 print is about **memory cost**, not about `NVDA`'s demand.
   ⚠ Stated as what it is — a **positioning/pricing** observation, `D6` class: context, not a trigger,
   and not a claim that either IV is mispriced.

---

## Lens 1 · UNDER-COMPUTED LEGS — the strongest bull case for something we did NOT deep-dive

The DEEP set is **ENRG · HLTH · DISC · UTIL**. The strongest argument against that allocation:

**★ PROMOTE-TO-DEEP: Information Technology (5th slot).** ROTATION explicitly routed it here rather
than taking a rotating slot one day after coverage, and the adversarial case is that the routing was
too polite:
- **Three dated binaries inside five sessions land in this one sector**: `NVDA` **08-26**, `MRVL`
  **08-27** (calendar-invisible), `AVGO` **09-02/03**. **No other sector has one.**
- **Two of the desk's eleven US holdings report inside the window** (`NVDA`, `AVGO`), and a third
  (`ANET`) is the book's largest positive one-session delta (+0.384).
- **`SECTOR_DEEP_SEMI.md` is 39 days old** and covers where **4 of 11 book names** live.
- The sector is **`exc5` rank 11 of 11 (−2.158)** while its epicenter announces a **>15%** price
  increase — the widest story-versus-tape gap on the board.
- ⚠ **Counter-argument, stated because it is real**: IT was deep-dived **yesterday** (08-22,
  PREMORTEM-promoted). A second consecutive DEEP is thrash, and the 08-22 file is one day old with an
  unchanged price frame. **Resolution: PROMOTE as the 5th slot with a NARROW mandate that the 08-22
  file cannot already answer** — see the final DEEP set below.

**WITHIN-RUN-WATCH (logged, not promoted):**
- **Materials** — `Copper` COT at the **100th percentile**, `NEM` fired `S89`-B on exhaustion
  geometry, breadth **+0.080 = rank 1 of 11**. Recency-blocked (covered 08-21). **Watch, not promoted.**
- **Financials** — `M805`'s three-businesses split is measured but the sector holds three book names
  (`NDAQ`, `MET`, and `KKR` adjacent) and **9 of 47 are 🔴, five of them insurers**. Covered 08-22.
- **Communication Services** — `T` is **9.74% of the real book's invested** with no cycle label, no
  card and **no DEEP file for a 6th run**, and `D297` means the flipper guard cannot see the 76.6%
  Alphabet complex. **This is the desk's longest-standing un-owned exposure and it is again not
  promoted** — logged as a cost, not passed over.

## Lens 2 · REGIME-FLIP / BOTH-SIDES — for every binary, the branch that hurts us

| Binary | Date | Our tilt | **The against-us branch, named** | Which OW it hits | Trigger / invalidation |
|---|---|---|---|---|---|
| **`NVDA` print** | **08-26** | IT UW−; `P90` says cost pass-through | **A demand-led beat with GM expansion**: guided GM **≥ +100bp**. Then the >15% increase was pricing power, `P90`-B fires, IT's UW− is wrong at the epicenter and the memory-cost frame loses its buy-side leg | **IT UW−** (against us), and it would **support** MATR/ENRG only indirectly | Trigger: guided GM ≥ +100bp. Invalidation of our read: `P90`-B |
| **`MRVL` print** | **08-27** 🚨 calendar-invisible | Card 3 says `AVGO` (held) lost share | **`MRVL` disappoints and the Alphabet warrant proves back-loaded** — the warrant *"doesn't fully vest until Google buys **$120 billion** of chips"* (`yahoo_finance` 08-21). A miss re-rates the share-shift narrative and `AVGO`'s −14.7 rs60 is then a discount, not a franchise loss | **Card 3's premise**, i.e. against our own new reading | Implied ±**11.31%**; a threshold must sit outside it |
| **Jackson Hole / Warsh debut** | **08-27→29** 🚨 calendar-invisible | `M822`: headline 3m-annualised **+0.49%** vs YoY **+3.30%** | **Warsh anchors on the YoY number and sounds hawkish.** `DGS2` **4.19 (88.7 %ile)** rises toward its 4.37 max; the front-end rally that owns 3/4 of the 24bp steepening (`M820`) reverses | **HLTH OW** (the longest-duration OW) and **DISC N+**; `UST 10Y` spec is **5th %ile short** = fuel in the other direction | `S112` (registered 08-22, settles 08-31) brackets it |
| **July PCE** | **08-28** | `P86` (registered 08-22) | **Core PCE MoM ≥ +0.35%** ⇒ the YoY side wins the wedge | HLTH, DISC | `P86`-B |
| **`AVGO` print** | **09-02/03** | Card 3: franchise event on a held name | **`AVGO` names a replacement custom-silicon win** and rs60 recovers above −5 ⇒ a one-customer scare | Card 3's premise | Implied ±**9.51%** |
| `FRO` | 08-28 | none | **No branch would change any conclusion** — the desk holds no tanker and has no tanker proposition | — | ⇒ **Dropped as not worth bracketing**, per the information-content rule, and the reason is stated |
| **MSCI review** | 08-31 | none | Passive flow, index-mechanical | — | Structural; no directional bracket |
| `S8` Hormuz statement | undated | — | **Unscoreable — 22nd consecutive run** | — | **A human must VOID it or date it (P5)** |

⚠ **Correlated-UW check (the 2026-07-15 field note).** Three UW sectors — **RE, INDU, UTIL** — are
**not** one bet in disguise this run, and the number says so: their `exc60` values are **−1.025 /
+1.380 / −7.284**, i.e. they disagree at the 60-day horizon. ⚠ **But RE and UTIL do share one driver
at the 20-day horizon** (−5.519 / −11.230, the two worst) **and both are long-duration cash-flow
proxies against `DGS30` at the 96.4th percentile.** ⇒ **Recorded as a partial correlation, and it is
the same rate leg that `S112` and `P91` already bracket** — no new bracket is spent on it.

## Lens 3 · MOMENTUM-CONTINUATION — "already ran" is not a verdict

| Runner | Move | Cycle KPI still accelerating? | **Re-tag** | Flip condition |
|---|---|---|---|---|
| **`MRVL`** | rs60 **+17.3**, rs20 +18.4, OBV 매집 | ★ **Yes, and it is contractual**: the Alphabet warrant is **$12.2bn / 59m shares** and *"doesn't fully vest until Google buys $120bn of chips"* — i.e. the KPI is a **purchase schedule**, not a sentiment | **EXTENDED-BUT-LIVE** | 08-27 print misses, **or** rs20 falls below 0 while OBV leaves 매집 |
| **`NEM`** | `S89` fired **B**, exc5 **+13.104**, rs20 **+37.6**, `obv_norm` **+0.487 = highest on the board** | 🚨 **No — `M779` measured 246.4% of its rs60 inside the last 20 sessions** (days 21–60 negative). The run has no base under it | **EXHAUSTED** | Would need rs60 to rebuild from days 21–60, not from the last 20 |
| **`MPC` · `PSX` · `VLO`** | rs60 **+44.0 / +37.0 / +43.1**, all OBV 매집 | Partly — `P66` re-corroborated **inside the window** (`bloomberg` 08-22, Samara refinery). But `P70` **MISSED on its control leg**: the refiners did **not** pay without the barrel (`BZ=F` 5-session **+6.631%**) | **EXTENDED-BUT-LIVE, with the separation claim dead** (`R89`) | The DEEP-ENRG contract read; a distillate crack below 90.0 (`P89`-B) |
| **`HPE`** | rs60 **+41.6**, flow +0.489, OBV 매집 | Unmeasured — **no card, no thesis line, no DEEP file names it** | ⚠ **UNCLASSIFIED, and that is the finding** — the book's 2nd-best rs60 has no owner | — |
| **`COIN` · `MSTR`** | flow **+1.000** both, the only two 🟢 with 🟢 breadth | Both are **one factor** (bitcoin beta) in two GICS labels; `MSTR` rs60 **−24.7** while rs20 **+26.5** | **EXTENDED-BUT-LIVE on rs20, EXHAUSTED on rs60** — the two horizons disagree by **51.2pp** | rs20 below 0 |
| **`ANET`** (held) | delta **+0.384**, the book's largest; OBV 매집, rs60 +20.2 | ⚠ **FINRA z +1.82, 5v5 +3.9▲ — the ONLY 🔴 short-surge on the book.** New shorts arrived **into** the improvement | **EXTENDED-BUT-LIVE, with a named opposing flow** | z above +2.5 with rs20 turning negative |

★ **The lens's own conclusion against the desk**: the run's instinct is to treat `NEM`'s +13.1% as
strength and `AVGO`'s −14.7 as weakness. **The measurements invert both** — `NEM`'s move has no base
(`M779`) and `AVGO`'s weakness has a named, dated, contractual cause with a **priced ±9.51% event**
still ahead of it.

## Lens 4 · CYCLE-EXPOSURE — registry vs coverage vs the REAL book

`cycle_exposure.py`, book read-only (total ≈ **$11,067** / 15,272,249원, invested **$5,126**):

| Cycle | rank | epicenter % | need ≥ | held epicenter | GAP |
|---|---|---:|---:|---|---|
| AI-compute / semiconductors | 1 | **16.52%** | 12.0% | `NVDA`, `ANET` | ✅ |
| Energy / oil-refining | 2 | **9.84%** | 8.0% | `MPC`, `PSX` | ✅ |
| Missile-defense / rearmament | 3 | 3.79% | — | `RTX` | ⚪ no threshold set |

**No top-rank cycle GAP.** ⇒ The 2026-07-14 postmortem failure (zero epicenter exposure in the #1
cycle) is **not** recurring.

🚨 **But the lens's real finding is what the registry cannot see, and it is now two cycles deep:**
1. **The optical/interconnect cycle still has NO ROW** (`D250`/`M731`, unfixed for weeks). `S86` and
   `S96` both settled **B**; `LITE` +0.639 (blocked from 🟢 on surge 0.95), `COHR` +0.158,
   `CIEN` −0.380 🔴 with rs60 −34.0. ⇒ **Exposure there is UNMEASURABLE, not zero**, and the ✅ above
   is a statement about three registered cycles, not about the book.
2. ★ **New this run — the custom-silicon / merchant-ASIC layer has no row either.** The Alphabet–
   `MRVL` warrant ($12.2bn, vesting against **$120bn** of purchases) and Amazon's custom chip business
   **crossing a $25bn run rate** (08-22, 15 articles/6 outlets) describe a layer in which the book
   holds **`AVGO`** — and `AVGO` is filed under *"AI-compute-EPICENTER"*, the same label as `NVDA`.
   **The registry cannot distinguish "sells the accelerator" from "co-designs someone else's".**
   ⇒ The book's 16.52% "epicenter" exposure is **two different businesses counted as one cycle**, and
   the 08-19 event moved them in opposite directions. **Registered as a dig.**
- ⚠ **Cleanest epicenter expressions, named as the lens requires** — and the honest note is that the
  desk already holds the epicenter (`NVDA`, `ANET`) and the gap is at the **layer below**: `MRVL`
  (LATE-MONEY, 32.0pp rs60 spread already realised), `MU`/`SNDK`/`LRCX`/`STX` (Card 2, filed to the
  miss ledger). **No name is advanced to BET** (P4 — this stage sizes nothing).

---

## Brackets registered this run — both-sided, thresholds OUTSIDE the implied move

> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md`, `llm_outputs/**`, `REPORT/**`:
> **`S115` `S116` `S117` returned 0 hits.** Highest existing **`S114`** (registered 08-22).
> ⚠ Observables and thresholds **frozen at registration**. `D300-KR` applied: every anti-signal is
> keyed to a **magnitude** or a **specific dated publication failure**, never to "an event occurring".
> ⚠ Prices settled **2026-08-21**, one provider (`yfinance`, `auto_adjust=False`), benchmark named
> inline (`C1`). Implied moves from the ATM straddle of the first expiry spanning each event.

### `S115` — ★★★ The `NVDA` print, with a threshold the options market cannot already contain
*(successor to `S103`, whose ±5.0pp bands are inside the ±6.11% implied move and are pre-declared
no-information above; `S103` itself still settles as registered per `D242`)*
- **Event**: `NVDA` FQ results, **2026-08-26** (corroborated to two bodies, §0).
- **Frozen observable**: `NVDA` **1-session return** on the first settled close after the print
  (2026-08-27), **and** its **excess vs `SPY`** on the same session.
- **Implied move at registration: ±6.11%** (08-28 straddle $13.12 / spot 214.72; ATM IV 0.606/0.588).
- **A — the print is a REAL surprise to the upside**: 1-session return **≥ +7.0%** (outside implied).
- **B — a real surprise to the downside**: 1-session return **≤ −7.0%**.
- **C** between — **disclosed as the heavy favourite (~70%)**, since ±6.11% is the market's own
  1-sigma-ish estimate for the whole path to 08-28.
- **Information grade: MEDIUM-HIGH.** Both branches are informative and asymmetric in *content*: an
  A that arrives **with** a gross-margin expansion falsifies `P90`; an A that arrives **with** flat
  margin confirms it. ⇒ **`S115` is scored jointly with `P90`, and that pairing is declared here.**
- **Anti-signal (VOID)**: `NVDA` does not report on 08-26 (delay), **or** US cash equities do not
  trade a full session on 08-27. ⚠ Base rate: very low; keyed to a publication/venue failure.

### `S116` — ★★★ The bracket the desk's own calendar could not have written: `MRVL` 08-27
- **Event**: `MRVL` FQ2 results, **2026-08-27** (`yahoo_finance` 08-19, body: *"Mark Your Calendars
  for August 27"*). 🚨 **Absent from `catalyst_calendar` — this row exists because the calendar was
  audited, not because it was read.**
- **Frozen observable**: the **`MRVL` − `AVGO` 1-session excess** on the first settled close after the
  print (2026-08-28), both vs their own prior close.
- **Implied move at registration: `MRVL` ±11.31%** (08-28 straddle $26.80 / spot 237.04; ATM IV 1.122).
- **A — the share shift is confirmed and widens**: `MRVL` − `AVGO` ≥ **+12.0pp**.
- **B — the share shift is over-priced**: `MRVL` − `AVGO` ≤ **−12.0pp** (i.e. `MRVL` disappoints into
  a 1.122 IV and `AVGO` holds).
- **C** between.
- **Why a SPREAD and not a raw excess**: `D308`'s registered remedy — a node-vs-name question written
  on a raw excess forces the anti-signal to arbitrate what the anti-signal cannot see. **Here the
  shared AI-semis move cancels and only the relative franchise move reaches the branches.**
- **Information grade: HIGH.** This is the only row on the board where **both** branches change a
  standing thesis on a **held** name (`AVGO`'s *"AI-compute-EPICENTER"* line, whose customer was
  unnamed for the life of the position, `W4`).
- **Anti-signal (VOID)**: an **announced acquisition of, or by, either company** inside 08-24 → 08-28.
  ⚠ Base rate: low, and keyed to a **named corporate action**, not to commentary.

### `S117` — ★★ Does the memory IV premium belong to memory, or is it `NVDA` beta?
- **Event**: the same 08-26 print, read through a name that is **not** reporting.
- **Frozen observable at registration** (`[measured]` today): on the **08-28 expiry**, `MU` ATM IV
  **0.650/0.643** vs `NVDA` **0.606/0.588** — **`MU`'s IV exceeds the reporting company's by ~4.5 vol
  points** while `MU`'s own print is **2026-09-24**.
- **Settle observable**: `MU`'s **1-session excess vs `NVDA`** on 2026-08-27 (first settled close after
  the print), both vs their own 08-26 closes.
- **A — the information was about MEMORY**: `MU` − `NVDA` ≥ **+3.0pp** (`MU` outperforms the reporter
  on the reporter's own event).
- **B — it was `NVDA` beta and `MU` is a levered follower**: `MU` − `NVDA` ≤ **−3.0pp**.
- **C** between — the favourite.
- **Information grade: MEDIUM, and disclosed.** C is likely; but **A is the only observable this desk
  has that can distinguish `P90`'s cost story from a generic AI-demand story using price rather than
  narrative.** That is why it is worth one bracket.
- **Anti-signal (VOID)**: a `MU`-specific dated announcement (guidance update, capacity announcement,
  M&A) inside 08-24 → 08-27. ⚠ Base rate checked: `MU`'s last dated corporate item in the window's
  news is *"Micron Quietly Pours $10 Billion Into Next Big Move"* (`yahoo_finance` **08-20**, i.e.
  **before** the window opens). **The clause is not near-certain.**

⚠ **Brackets deliberately NOT written, with reasons** (the information-content rule):
- **July PCE 08-28** — already carried by `P86` (both-sided, registered 08-22). A second row would be
  double-counting one observation.
- **Jackson Hole 08-27→29** — already carried by `S112` (registered 08-22, settles 08-31) on its
  **true** dates. ✅ The event is covered even though the calendar cannot see it; **the gap is in the
  tool, not in the scenario coverage**, and those are different defects with different owners.
- **`FRO` 08-28** — no branch would change any conclusion (Lens 2). Dropped with the reason stated.
- **MSCI review 08-31** — index-mechanical, no directional content.
- **The RE/UTIL duration correlation** — the rate leg is already bracketed by `S112` and `P91`.

---

## Final DEEP set — **N = 5** (4 + one PREMORTEM promotion)

| Slot | Sector | Mandate |
|---|---|---|
| Continuous 1 | **ENRG** | **The refiner CONTRACT question** — `module_disclosure_us MPC` → 10-Q MD&A + Item 1A. Fourth run unopened; `P70`'s MISS makes margin sustainability the binding gap. A closed market is the right session for it |
| Continuous 2 | **HLTH** | **18 names blocked by `vol_surge` alone — the largest blocked set of any sector.** Is the leadership broad, or is it `LLY` plus 18 names the gate cannot see? |
| Rotating 1 | **DISC** | `exc20` **rank 1 (+4.244)** against `exc60` **rank 10 (−4.938)** with **breadth 0.000** across 28 names and no live bracket since `S91` VOIDed. Reversal with a base, or five names? |
| Rotating 2 | **UTIL** | Morgan Stanley's named **38-GW** gap (08-20) against `eqflow` **−0.621** and **🔴 13 of 15**. `M802`'s $105bn guarantee unresolved for a 2nd run. **Is there ANY equity transmission from AI-power capex?** |
| ★ **PREMORTEM-promoted 5th** | **IT** | 🚨 **NARROW mandate, deliberately disjoint from the 08-22 IT file** (which was written on an identical price frame and would otherwise be re-run): **the custom-silicon layer as a distinct risk unit.** Does the book's 16.52% "AI-compute epicenter" contain **two** businesses — *sells the accelerator* (`NVDA`, `ANET`) versus *co-designs someone else's* (`AVGO`) — and did 08-19 move them apart? Inputs: the $12.2bn / 59m-share Alphabet–`MRVL` warrant vesting against **$120bn** of purchases; Amazon custom silicon at a **$25bn run rate**; the **32.0pp** `AVGO`↔`MRVL` rs60 spread; `SECTOR_DEEP_SEMI.md` at **39 days** |

---

## ✅ EXIT CHECK

- [x] **4 lenses run**, each returning **named tickers and dated catalysts**. ⚠ **Declared deviation**:
      in-context and serial, not a parallel agent fan-out (5th consecutive run, standing constraint).
- [x] **Every bracket names its observable, its frozen threshold and its date, with BOTH branches** —
      `S115` (08-26/27) · `S116` (08-27/28) · `S117` (08-26/27). **No one-way bracket.**
- [x] **Every magnitude threshold is stated against the implied move.** `S115` ±7.0% vs implied
      **±6.11%** · `S116` ±12.0pp vs `MRVL` implied **±11.31%** · `S117` ±3.0pp on a *spread*, whose
      components' implieds are given. **`S103` is explicitly pre-declared NO-INFORMATION** because its
      ±5.0pp sits **inside** ±6.11% — declared, not quietly re-banded (`D242`).
- [x] **Each branch graded by information content**; **four** candidate brackets dropped with reasons
      (`FRO`: no branch changes a conclusion · PCE and Jackson Hole: already covered without
      double-counting · RE/UTIL duration: already in `S112`/`P91`).
- [x] **`BLINDSPOT_PREMORTEM.md` written** — legs · both-sides brackets · momentum re-tags · cycle GAP.
- [x] **Every catalyst-bearing leg promoted or logged** — IT promoted to a 5th slot with a *narrow,
      disjoint* mandate; MATR / FIN / COMM logged as within-run watch with their costs named.
- [x] **Brackets handed to ALPHA; cycle GAP handed to BET** — GAP is ✅ on the three registered cycles,
      with **two unregistered cycles** named as unmeasurable rather than absent.
- [x] **DEEP set updated and stated: N = 5 — ENRG · HLTH · DISC · UTIL · IT.**
- [x] 🚨 **The protocol's catalyst-injection rule is satisfied in the stronger form**: not only was
      every binary ≤5 sessions bracketed both ways, **the calendar itself was audited against a second
      source and a news body before use** — vindicating it on `NVDA` and finding two missing binaries.
