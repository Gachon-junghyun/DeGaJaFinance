# SCENARIOS_KR — brackets registered by the `industry_kr` desk

> ★ **Split from `SCENARIOS.md` on 2026-07-29** (the 8-run size escalation, resolved by a human).
> **The shared spine — the status legend, the scoring rules and the MASTER SCORING LOG + MASTER
> INDEX — stays in [`SCENARIOS.md`](SCENARIOS.md) and is read IN FULL by both desks every run.**
>
> ⚠⚠ **Ownership is the registering desk, NOT the subject market, and it does not confer exclusivity.**
> **S8** was registered by the US desk and **scored by the KR desk**; **S33** was registered by KR and
> **scored by US**; **S28** likewise. **A desk with a past-dated row in the other file must open that
> file and score it** — the "score everything or log EXPIRED" rule is unchanged and un-splittable.
>
> A scenario is valid only if it was written **before** its event, carries **both** branches, and names
> a **date** and an **observable with a threshold**. Scoring is L3 `scenario_score`. Not advice.

# SCENARIOS — pre-registered branches, scored after the fact

> Read at HANDOVER (run start) and at PREMORTEM. A scenario is only valid if it was written
> **before** its event, carries **both** branches, and names a **date** and an **observable with a
> threshold**. Registered-after-the-fact entries are worthless — they are hindsight wearing a table.
> Scoring is done by L3 [`scenario_score`](../pipeline/L3_functions/scenario_score.md). Not advice.

**asof 2026-07-27 08:2x KST** (KR pre-open at run start; ⚠ the run's DEEP stages executed 09:0x~09:1x, i.e. intraday) · **S12 held PENDING a 4th time (deadline 2026-07-28) · S27 · S28 · S29 registered by the industry_kr run**
· *(prior header)* asof 2026-07-24 09:xx KST (KR pre-open; the US 2026-07-23 regular session HAS closed)
· **S6 · S7(band leg) · S10 scored by the 2026-07-24 `industry_kr` HANDOVER · S12 held PENDING
(its frozen observable has not printed) · S17–S18 registered by the 2026-07-24 `industry_kr` run.**
· *(prior header)* asof 2026-07-23 22:3x KST (US Eastern 2026-07-23 09:3x — every price in that
header's tables is the **2026-07-22 close**; the 07-23 session was not open at registration)
· **S12–S16 registered by the 2026-07-23 `industry_US` PREMORTEM, all before their events.**
· *(prior header, kept for the record)* asof 2026-07-22 19:5x KST (US Eastern 2026-07-22 06:5x — the US 07-22 session has **not opened**)
· S1–S5 registered 2026-07-22 12:12 KST · **S6–S9 registered by the 2026-07-22 industry_US PREMORTEM,
all before their events.**

## S10 — USTR Section 301 "forced-labor tariff" on Korea · ARMED · 2026-07-24 (D-1 at registration)

Registered 2026-07-23 by the `industry_kr` EVENT_ALPHA/BET stages, before the event. USTR representative
quoted across 8+ domestic outlets 2026-07-23: announcement "as soon as tomorrow," targeting **60
countries** including Korea, under a forced-labor rationale. Korea's government disputed the rate as
unfair ("12.5%는 부당") at a 2026-07-09 public hearing. **Named corporate casualty already on file**:
LG그룹 disclosed the tariff risks delaying a **$28.0bn** US investment (2026-07-09, unretracted).

**Observable (frozen)**: the announced rate on Korea, vs the disputed **12.5%** figure.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Rate confirmed **materially below 12.5%**, or a Korea-specific carve-out | Tariff risk was overstated; LG그룹's $28bn delay risk eases |
| **B** | Rate lands **at or near 12.5–15%** as threatened | Confirms the disclosed risk; watch whether LG디스플레이's already-heavy foreign selling (20d −660.9만, `industry_kr` BET_SHEET 2026-07-23) extends |
| **C** | Announcement slips past 07-24 with no new date | Re-register with the new date; do not silently let this go EXPIRED |

**Pre-existing measured split (not to be flattened into one "LG" read)**: on 2026-07-23, **034220
LG디스플레이** flow-confirms the bad-tariff narrative (🔴, heavy foreign exit, crowded/building short)
while **066570 LG전자** flow-contradicts it (🟡, foreign+institution buying, short covering) — the same
headline, opposite money. Score each name separately when this fires.

---

## S11 — Financial holding company governance reform · ARMED · 2026-07-29 (D-6 at registration)

Registered 2026-07-23 by `catalyst_calendar.py --days 10` (the standard 5-day window used inside
`industry_kr` MACRO never reaches this date — this scenario sat un-registered through every prior
run despite 07-29 already being tracked as "the single most loaded date" via S2). **Not a company
event — a regulatory one, hitting the desk's own continuously-OW-tilted sector (FIN) directly.**

**What it is**: 금융위·금감원 지배구조 선진화 방안, aimed at all major financial holding companies —
CEO/chairman **3-term limit** (proposed as statutory, not just a code-of-conduct recommendation),
reappointment requiring **2/3 shareholder approval**, and a **clawback** provision. Domestic coverage
confirms this affects "사실상 전 금융사" (in effect all financial companies), not only the "8 major
holdcos" label the calendar entry carries — named executives already in the press include KB·신한·
하나·우리·NH농협·iM금융 chairmen.

**Observable (frozen)**: whether the 3-term limit is enacted **as originally proposed (statutory
ban)**, watered down to a **recommendation/code provision**, or **delayed** — the calendar itself has
already downgraded this from "D-1 with content" to "**contested**" on reports of a constitutional
challenge under review, before the event has even printed. That contest is itself part of the
observable, not noise to filter out.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Statutory 3-term ban + 2/3 reappointment rule enacted as proposed | Succession-uncertainty repricing across **all** major bank/financial holdcos simultaneously — a sector-wide governance shock, not a single-name event |
| **B** | Watered down to code-level guidance, or the constitutional challenge delays it | Uncertainty persists rather than resolving; **do not read a delay as "resolved bullish"** — the challenge itself can run for months |
| **C** | Withdrawn/shelved entirely | The succession-risk discount (if any is currently priced) should unwind |

**Why this matters to the standing book, named explicitly**: today's `industry_kr` BET_SHEET priced
KB(105560)·하나(086790)·신한(055550)·삼성카드(029780) as the FIN candidate set. A same-day re-check
(2026-07-23) found **우리금융(316140)·iM금융지주(139130)·기업은행(024110) all independently
real-hands** (foreign+institution net buying, retail selling) — the same signature as the four
priced names — **and none of the three had been priced or even named in today's BET_SHEET.** iM금융
carries the highest news-velocity of the seven (4.29x), driven substantially by this same governance
thread plus a 하나증권 "저평가" note (2026-07-20) on 우리금융/iM금융 specifically. **The FIN OW this
run has been running on a candidate set narrower than the sector-wide flow signal it's justified by**
(same shape as `SECTOR_ROTATION.md` §2's own "FIN OW is carried by 3 bank-holding names, not
financials broadly" finding — except here the miss runs the other direction: real money is also
arriving in names the desk hasn't priced, not only in the ones it has).

**Track KPI**: the enacted-vs-watered-down-vs-delayed distinction, dated 2026-07-29. Until then, read
KB/신한/하나's unusually strong simultaneous flow (SECTOR_DEEP_FIN.md, 2026-07-23) as **partly a
succession-clarity trade**, not only the carried NIM-expansion thesis — the two are not mutually
exclusive, but conflating them would misattribute the driver if branch A fires and the flow reverses
on "clarity achieved, priced in" rather than continuing on NIM alone.

---

---

## S17 — ★ SK hynix ADR–ordinary premium · ARMED · 2026-07-29 → 2026-08-05

Registered 2026-07-24 by the `industry_kr` MACRO stage. **This scenario exists because S2's ADR leg
was found to have an unscoreable observable**, on primary-participant testimony.

**What broke S2's ADR leg.** Korea Securities Depository (KSD) president **이윤수**, named on-record
interview conducted 2026-07-22, published [sedaily 2026-07-23 19:04, 「"SK하이닉스 ADR 전환 낭설"」]
— KSD is the operator of the very share-registration step 07-29 refers to:
- *"The belief that the ADR issuance ceiling is **25%** is a misunderstanding — that figure is an
  SEC fee-calculation estimate. **The conversion ceiling is the 2.5% currently listed.**"*
- Even after the 07-29 new-share registration, conversion is blocked by the 2.5% ceiling: ADRs must
  first convert **into** Korea to free headroom, and *"because the ADR premium is so high, **there
  will be no conversion demand for the time being**."*
- Raising the ceiling is **the issuer's** decision (not KSD's, not Citibank's), and exceeding 2.5%
  requires a process equivalent to a **secondary offering** (board + regulator + SEC registration) —
  the path **TSMC actually walked, 2001–2007**.
- Ordinary–ADR price gap at the time of the interview: **~30%**.

⇒ **07-29 is a share-registration date, not a two-way-conversion opening.** S2's ADR row
(*"un-suspends the 000660 flow read"*) and dig **D6** (*"re-run the 000660 flow read after
2026-07-29"*) both rest on a premise that a primary participant denies on the record.

**Observable (frozen)**: the **ADR-to-ordinary premium**, measured on closes, **07-29 → 08-05**.
This replaces "does conversion open" — which is near-unobservable — with a number that prints daily.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Premium compresses to **≤15%** by 2026-08-05 | Arbitrage did open. The KSD statement was wrong, the mechanical distortion is ending, and the 000660 flow read can be un-suspended on schedule |
| **B** | Premium stays **≥25%** through 2026-08-05 | The KSD statement holds. **The 000660 flow suspension must be extended indefinitely**, not lifted on a calendar date, and dig D6's trigger date is void |
| **C** | Premium lands **15–25%** | Partial. Re-register with a tighter band; do not read a partial move as resolution |

**Anti-signal (what kills this scenario outright)**: **the issuer (SK hynix) disclosing a ceiling
increase.** The KSD president himself said the ceiling is the issuer's to set — an issuer disclosure
voids this bracket the day it prints, and that is exactly why it is written here rather than treated
as settled fact.

**Tag**: `[measured — named primary-participant testimony, institutional remit]`. **It is not price
data and is not to be cited as price evidence.**

⚠ **The suspension stays on today.** This finding is a reason to hold the 000660 flow read suspended
**longer**, never a reason to lift it (rule **D1** / retracted **R1**).

---

## S18 — KT regulatory sanction hearing · ARMED · 2026-07-29 (D-5 at registration)

Registered 2026-07-24 by the `industry_kr` DEEP-COMM stage. ★ **Registered because the calendar
missed it** — `CATALYST_WATCH.json` pulled `--days 10` this run contains **no KT row**, which is the
**fourth consecutive occurrence** of dig **D18** (GOOGL 07-22, INTC + ECB 07-23, KT 07-24).

**What it is**: 개인정보보호위원회 sanction deliberation on KT, reported maximum fine **₩200bn**
≈ **1.5% of market cap**.

**Why it matters beyond one name**: 2026-07-29 was already carried as *"the single most loaded date
on the calendar"* with **five** stacked triggers (S2). **This makes six**, and it is the second one
on that date that no calendar produced (S11 was the first, found by a manual 10-day re-pull).

**Observable (frozen)**: the **announced fine**, against the reported **₩200bn** maximum.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Fine **≥ ₩150bn** (≥75% of the reported max) | A ~1%+ market-cap hit lands on one of the three names carrying the desk's newly promoted COMM OW. The COMM promotion was already flagged weak (see the 2026-07-24 BET_SHEET §0-④) — this would be the second independent reason to unwind it |
| **B** | Fine **< ₩150bn**, or deferred | Priced-in / non-event at the sector level. COMM's verdict has to stand or fall on its own flow, not on this |

⚠ **KT is not a desk candidate** — it carries no ALPHA tag and appears in no §A/§B row. This is
registered as a **sector-level risk to a position the desk did promote**, not as a bet.

---

## S22 — SK이터닉스 KKR SPA closing · ARMED · 2026-07-31 (D-6 at registration)

Registered **2026-07-25 by the `industry_kr` BET/ALPHA stages, before the event.** ★ Registered
because 475150 is the board-strongest real-hands name (외+147.3만·기+210.3만, vsurge 2.94) and its
whole thesis is **structural, not a news theme** — so it needs a dated, falsifiable settling point,
and the desk's most expensive ledger rows (+41.2pp/+26.9pp) came from rejecting this exact name on
narrative grounds while its money never stopped.

**What it is**: KKR SPA to acquire SK디스커버리's **30.98%** stake at **₩23,700/share ≈ −58% to
market**. ⚠ **Already deferred once (06-30 → 07-31)** per `CATALYST_WATCH.json`.

**Observable (frozen)**: whether the SPA **closes on 2026-07-31** (DART disclosure), or is deferred again.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | SPA closes 07-31 as scheduled (DART) | The structural catalyst realized; the real-hands accumulation was event-positioning that resolves |
| **B** | **Deferred a SECOND time** | ★ **This is the kill** — a second deferral, per the carried rule, ends the thesis regardless of flow |
| **C** | Terms revised (price/stake) | Re-register; do not read a revision as clean closing |

**Anti-signal**: crowded-short 2.53% covering is **turn-conditional squeeze fuel, never a standalone
reason** — score the SPA, not the short move. **Tag** `[measured]` flow, `[inferred]` on deferral risk.

---

## Scoring-log rows added 2026-07-25 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | — **STILL PENDING** | re-checked 2026-07-25 | **The frozen observable still has not printed.** `DTWEXBGS` reads **120.5315 asof 2026-07-17** — unchanged; range unchanged [117.44, 121.41]. Re-check deadline **2026-07-28**; if still unprinted, score **`AMBIGUOUS`** and **do NOT substitute a proxy** (D46: 3-session window on a ~5-business-day-lag series cannot settle by construction). Decision axis already `AMBIGUOUS` (D35: hold-with-hawkish-tilt is in neither branch) |
| **S22** | **2026-07-25 (industry_kr BET/ALPHA)** | 2026-07-31 | — | — | ARMED — SK이터닉스 KKR SPA closing; branch B (a SECOND deferral) is the kill. Registered so the board's strongest real-hands name has a dated settling point and cannot be rejected on narrative (its two prior narrative rejections cost +41.2pp/+26.9pp) |

---

## Scoring-log rows added 2026-07-27 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | — **STILL PENDING (4th check)** | re-checked 2026-07-27 | **The frozen observable still has not printed.** `DTWEXBGS` reads **120.5315 asof 2026-07-17** — unchanged for **10 calendar days**; 120-day range unchanged **[117.4396, 121.412]**. ⚠ **Four consecutive runs have now carried this** (07-24 US · 07-25 KR · 07-25 US · 07-27 KR), which is not a scoring failure but the **measured consequence of defect D46**: a **3-session** invalidation window written on a series with a **~5-business-day publication lag** cannot settle inside its own window by construction. **Deadline 2026-07-28 (tomorrow).** If it still has not printed, score **`AMBIGUOUS`** with the reason and **do NOT substitute a proxy**. The decision axis is already `AMBIGUOUS` (D35 — hold-with-**hawkish**-tilt is in neither branch). **A 5th carry IS a scoring failure and must be logged as one.** |
| **S27** | **2026-07-27 (industry_kr MACRO/DEEP-ENRG)** | ~2026-08 late | — | — | ARMED — ★ the **9th 최고가격 designation**; full bracket below |
| **S28** | **2026-07-27 (industry_kr DEEP-INDU)** | 2026-07-28 09:00 | — | — | ARMED — ★ an **earlier warning light than S22**, found in a DART filing no calendar carried (**D18's 7th occurrence**) |
| **S29** | **2026-07-27 (industry_kr DEEP-HLTH/ALPHA)** | 2026-08-06 | — | — | ARMED — separates 셀트리온's remaining live branches on a pre-registered observable |

---

## S27 — ★★ Korea's 9th 석유제품 최고가격 designation · **SCORED `FIRED-B` 2026-08-25** (was ARMED · ~2026-08 late)

Registered **2026-07-27 by the `industry_kr` MACRO stage and quantified by DEEP-ENRG, before the event.**
★ **This exists because a hard, dated, fully public administrative constraint on a position the desk has
held OW for seven consecutive runs had never been named in any desk file.**

**What it is** (산업통상부, primary): a cap on 석유제품 prices, in force since **2026-03-13**, designated
**7 times plus an 8th freeze on 07-24**. Path: 1차 휘발유 ₩1,724 / 경유 ₩1,713 / 등유 ₩1,320 →
2차 (03-27) ₩1,934 / ₩1,923 / ₩1,530 → 3~6차 frozen → **7차 (06-27) cut ₩150 each →
₩1,784 / ₩1,773 / ₩1,380** → **8차 (07-24) FROZEN**, while Brent ran
**$71.6 (07-01) → $90.3 (07-20) → $100+ (07-23)**.
President 이재명, on record 2026-07-21 국무회의: *"원래 계획에 의하면 사실 더 내리든지 폐지됐어야 하는데
**오히려 더 강화해야 할 것 같다**."*

**Why it is load-bearing, measured (M157)**: refining operating margins are **0.559% (SK이노)** and
**0.688% (S-Oil)**, so regulated-3-product domestic revenue — **₩10.14tn = 25.68%** and
**₩8.85tn = 25.84%** of revenue — equals **22.6× and 37.6× operating profit**. A 25%-of-revenue
exposure is a 22–38× exposure at the line that decides the thesis.

**Observable (frozen)**: the **9th designation's 휘발유 and 경유 cap levels**, against the standing
7차 levels **₩1,784 / ₩1,773**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Cap **raised**, or the regime **abolished** | The domestic leg's administrative constraint clears; the ENRG OW's domestic half is confirmed rather than assumed |
| **B** | Cap **frozen again, or cut** | With Brent near $100 a frozen nominal cap tightens in real terms — crack gains do not transmit domestically, and M-12 is a live drag on 22–38× exposure |
| **C** | Regime **restructured** (converted to a subsidy / margin-compensation scheme) | Re-register. A compensation scheme is a different object from a cap and must **not** be scored as branch A |

**Anti-signal, named by the decision-maker himself**: the President's *"강화"* remark — branch B has
explicit top-level political backing, which is the opposite of the desk's prior implicit assumption
that a March cap would be phased out.
⚠ **The date is not guessed.** The cadence has run roughly 4-weekly (donga 07-21 states it explicitly),
putting the 9th designation in **late August**; the exact day is 산업부's to announce, so it is written
as **`~2026-08 late`** rather than as a specific date.
⚠ **Score the cap level, not the price reaction** of 096770 / 010950.

**Cross-check KPI, separately dated**: the **손실 보전 확정 절차** is still incomplete —
*"최고가격제로 인한 손실 보전 확정 절차도 아직 남아 있다"* (mt 07-20 and 07-21, identical sentence in two
outlets) — and **all three filers carry zero booked amounts**. **The first booked amount at any of the
three is the moment M-12's transmission becomes a number**, and it has no date.

---

## S28 — ★ SK이터닉스 임시주총 · ARMED · 2026-07-28 09:00 (D-1 at registration)

Registered **2026-07-27 by the `industry_kr` DEEP-INDU stage from a DART filing dated 07-13, before the
event.** ★ **Registered because it arrives BEFORE S22 and no calendar produced it** — this run's
`CATALYST_WATCH.json` (`--days 14`) carries the 07-31 SPA closing but **not** this meeting.

**What it is**: an extraordinary general meeting to elect **two KKR-nominated directors**, which the
filing itself states is a **거래종결 정지조건** — a condition precedent to the KKR SPA closing that
S22 brackets.

**Observable (frozen)**: whether **both** nominated directors are elected at the 07-28 meeting.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Both elected | The condition precedent clears ⇒ S22 branch A (closing 07-31) becomes materially more likely. **This is not itself a closing** |
| **B** | Meeting postponed, or either nominee fails | ★ A **leading indicator of S22 branch B** (the second deferral, which is the carried kill) — arriving **three days early** |

⚠ **This does not replace or re-freeze S22.** S22's observable remains *"does the SPA close on 07-31 per
DART"* and its kill remains **a second deferral, nothing else**. S28 is a separate, earlier read on the
same chain, registered precisely so the desk does not learn on 07-31 what it could have known on 07-28.
⚠ **Carried rule, restated because this is the name that taught it**: 475150's two prior
narrative-grounded rejections cost **+41.2pp and +26.9pp**, the ledger's two most expensive rows.
**Valuation, theme age (재생에너지 is 🔴FADING at 0.42× on 969 hits), a 투자주의 designation and an
intraday fall are each recorded as facts, and none of them is a kill.**

---

## S29 — 셀트리온: which branch is live · ARMED · 2026-08-06

Registered **2026-07-27 by the `industry_kr` DEEP-HLTH / ALPHA stages, before the window closes.**

**Why**: the actor axis and the price axis disagree, and DEEP-HLTH narrowed the disagreement to three
readings — **(a) leading accumulation · (b) a distribution handoff · (c) nothing yet.**
**(b) is already directly refuted on measurement**: retail net-sold **16 of 19** sessions (−1.956m
shares) and real-hands net-bought **+505k even across the 9 down/flat sessions**. So the live question
is **(a) vs (c)**, and it needs an observable rather than a fourth flow re-read.

**Observable (frozen), two legs, reported separately and never merged**:
1. **`close > 189,737`** — the carried trigger, **−6.4% away** at registration;
2. **the 5d/50d volume ratio**, **0.78** at registration (the 07-24 index-crash session reached only
   **1.23×** the 50-day mean, against 삼바's **3.12×** the same day).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Trigger taken **and** the volume ratio above **1.0** by 2026-08-06 | (a) confirmed — the accumulation was leading, and it finally cleared the elastic retail supply inside the ₩170,100–183,600 box |
| **B** | Trigger untaken **and** the volume ratio still below **1.0** | (c) — real-hands accumulation that cannot make price. The shelter thesis survives as a **relative** claim only and must stop being written as an accumulation thesis |
| **C** | Trigger taken on a volume ratio still below **1.0** | Ambiguous by construction — re-register with a tighter volume band rather than reading a thin breakout as confirmation |

⚠ **A future scorer must read the FOREIGN leg, not the institutional one (M168)**: foreign ran
first-10 **−205k** (positive on 2/10) → last-9 **+510k** (positive on 8/9, final four
**+33k → +61k → +83k → +117k**, monotone), while institution went **+1.022m → +298k** (net −89k over
07-15~23). **M120's "sustained institutional accumulation" is a first-half fact.**
⚠ **No KR implied move exists**, so both thresholds are **hand-set and declared as such** — one carried
trigger and one round volume ratio. Do not dress either as measured; the options-IV v1.1 module is the
prerequisite for a genuine KR threshold, and until it lands a KR threshold taken from anything else
would be fabricated.

---

## Scoring-log rows added 2026-07-28 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| **S12** | 2026-07-23 (PREMORTEM) | 2026-07-23 | **FIRED-B** (frozen observable) · decision axis **AMBIGUOUS** | **2026-07-28 HANDOVER (industry_kr)** | ★ **The observable finally printed after 5 carries.** `DTWEXBGS` **120.5315 (asof 07-17) → 120.71 (asof 07-24)** — the first new print since registration. 120-day range unchanged **[117.4396, 121.412]**, midpoint 119.425 ⇒ **120.71 sits in the upper half = branch B's DXY condition**; branch A (a close below 117.44) did not fire; the invalidation (outside the range) did not fire. ⚠ **Three caveats, stated rather than buried**: (i) only **one** of the three window sessions (07-24) has printed — the other two publish ~08-04 on the same lag, and branch A would need a **−2.7%** move on a series whose 30-day change is −0.70 (**arithmetic, not a forecast**); (ii) **the decision axis stays `AMBIGUOUS` (D35)** — the actual outcome, a hold with a **hawkish** tilt, is in neither branch, so **the branch label is right and its stated reason is wrong**; (iii) ★ **D46 is retro-validated** — the 07-17 value published on ~07-27/28, i.e. a **~5-business-day lag measured**, so the **3-session invalidation window could never settle inside itself.** The 5-carry chain was a registration defect, not inattention, and **this run closes it** |
| **S8** | 2026-07-22 (PREMORTEM) | undated | **FIRED-B** | **2026-07-28 HANDOVER (industry_kr)** | Scored on the line the 07-27 `industry_US` run **froze pre-outcome**. Crude fell hard (**WTI 89.310 → ~81.6, −8.7%**; Brent 96.780 → 87.750) while the **distillate crack held 86.275 → ~85.1, ≥ 84** ⇒ branch B, both legs. Branch A (crack <60 **∧** distillate <80) fired on neither. ⚠ **The desk's own input was defective and the verdict survived it**: the first reading (WTI 82.050 / distillate 85.484) was an **unsettled electronic-session tick** labelled 07-27 and kept moving on re-pull — **FIRED-B is invariant across all three readings**, but the distillate buffer is only **~1.1** and the 3-2-1 crack sits **~2.5 above its 60 kill line**. ★★ **And the KR read-across is refuted, not supported (M188)**: during KR regular hours the **screen** crack was **59.58–59.85, below 60**, and distillate **83.12–83.97, below 84** — the recovery came after the KR close. **KR refiners fell −11pp against a rising benchmark because they were watching branch A**, so this firing does **not** close **C4** |
| **S28** | 2026-07-27 (industry_kr DEEP-INDU) | **2026-07-28 09:00** | — **ARMED, fired AFTER this run** | — | ⚠ **The event is 35 minutes after this run's start clock and the run ended before it.** **Not EXPIRED — not yet scoreable.** Named here explicitly so it cannot be dropped: **next run's #1 scoring job.** ⚠ **`CATALYST_WATCH.json` did not carry it (D18, 8th consecutive occurrence — and this time it missed a D-0 binary)** |
| **S33** | **2026-07-28 (industry_kr MACRO)** | 2026-07-28 close | — | — | ARMED — full bracket below. ⚠ **Registered before M188 was known**; M188 reverses the sign of its information delta and makes it a **stronger** test |
| **S33-ANNEX** | **2026-07-28 (industry_kr ALPHA)** | 2026-07-28 close | — | — | ARMED — ★ **beta-contamination notice, NOT a rewrite of S33** |
| **S34** | **2026-07-28 (industry_kr EVENT_ALPHA)** | 2026-10-31 | — | — | ARMED — ★★★ the **funded-new-supply-entrant** branch that no row of S1–S32 contains |

---

## S33 — ★ KR refiners on the first session that knows the crack held · ARMED · 2026-07-28 close

Registered **2026-07-28 by the `industry_kr` MACRO stage, before the KR close.**

**Why.** **S8 scored FIRED-B on the 07-27 settle** (crude −8.7%, distillate crack ≥84), but the **KR session
had closed before that settle**, so 07-27 cannot separate **C4**. Today is the first KR session that opens
with the crack's recovery public.

**Observable (frozen)**: the **median excess return of 096770 and 010950 vs `069500.KS` (KODEX200)**,
**2026-07-28 settled close.** ⚠ **KR has no implied-move axis**, so the threshold is **hand-set and declared
as such** — the options-IV v1.1 module is the prerequisite for a genuine KR threshold.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | median excess **≥ +1.5pp** | The crack information is being priced ⇒ one vote for the **margin** reading |
| **B** | median excess **≤ −1.5pp** | They keep selling even though the crack held ⇒ one vote for the **war-premium** reading; the ENRG tilt loses another leg |
| **C** | between **−1.5 and +1.5pp** | No information. Re-register; do **not** widen the band |

⚠ **Contamination declared at registration**: (i) **096770 prints 07-30 and 010950 on 08-03**, so later sessions
carry earnings expectation — which is why the window is **one day**; (ii) a technical bounce off −10% is mixed in
regardless of direction; (iii) **n = 1 (S1)**.
⚠ **Score the observable, not the price-reaction narrative.**
★ **Post-registration finding that STRENGTHENS it (M188)**: KR was not information-blind on 07-27 — it was
watching a **sub-60 crack**. So the information delta today is **larger** than at registration, not smaller.

## S33-ANNEX — ★★ beta-contamination notice (**S33 is NOT re-frozen**)

Registered **2026-07-28 by the `industry_kr` ALPHA stage, before the close**, on the **S14-ANNEX precedent**.

**2026-07-28 is a crash session — `069500.KS` was −6.6% intraday and KOSPI200 settled the day at −7.85%,
with sell sidecars on both boards.** Measured 60-day betas vs `069500.KS`: **010950 −0.120 · 096770 +0.241.**
On a −7% benchmark day, **low/negative-beta names mechanically print large positive excess** — the intraday raw
S33 median read **+7.16pp**, which is almost exactly the pure-beta prediction.

⚠⚠ **S33 IS NOT RE-FROZEN.** Moving a registered threshold after the fact is what L3 `scenario_score` forbids.
Instead, **both readings are recorded side by side at scoring**:
1. **the raw excess median**, exactly as S33 froze it; and
2. **the beta-adjusted residual.**
**If the two disagree, that disagreement is the finding** — and it becomes the **first KR instance of L3-bis**
(*"a bracket whose observable can settle on frozen mechanics is not a test"*).
★ **Control, pre-registered**: the **07-27** observation is robust to the same correction — **−11.33pp raw
survives as −10.12pp adjusted**, because that benchmark day was **+1.28%**. **Yesterday's reading is sturdy;
today's is fragile, and that was knowable before the close.**
**Registration-discipline defect logged as D82**: *before freezing a relative-return observable, check the legs'
betas against the benchmark and state what the bracket reports on a large benchmark move.*

## S34 — ★★★ CXMT's capacity ramp: the supply-side falsifier the regime call never bracketed · ARMED · 2026-10-31

Registered **2026-07-28 by the `industry_kr` EVENT_ALPHA stage.**

**The gap it fills.** The regime call is *"memory is a price-cycle industry decelerating in rate of change."*
Its **only** registered frontal falsifier is **S3 (4Q26 DRAM contract guidance)**. **No row of S1–S32 contains
"a funded new supply entrant."** A price cycle is ended by supply as much as by demand, and CXMT has now raised
**₩14.5tn explicitly for capacity** after taking DRAM share from **3% to 8% in one year**.

**Observable (frozen)**: **CXMT's 12-inch wafer capacity per month, from a primary source** (Chinese regulatory
filing / annual report / earnings call). **Frozen baseline: 300k wpm now, company-stated 350k by year-end.**

| Branch | Observable | Meaning |
|---|---|---|
| **A** | **350k wpm reached or exceeded** by year-end | The supply-side falsifier is live ⇒ **M1's deceleration is reinforced, but its MECHANISM changes** — supply, not demand. Commodity DRAM and HBM must be scored separately from here |
| **B** | **stalls at ≤320k wpm**, or the company guides the target down | The EUV-absence yield constraint is real; this bracket voids and the regime call stands on its existing demand/price axes |
| **C** | no primary source publishes a capacity figure | **`AMBIGUOUS` — recorded as a construction defect**, and re-registered on a substitute observable (Chinese DRAM export volume statistics). **The threshold is not widened after the fact** |

⚠ **HBM is deliberately excluded** — the bodies put **CXMT's HBM3E at 2027 and the gap at 3–4 years**. This is a
**commodity-DRAM bracket, not a memory bracket** (W5).
⚠ **The price counter-argument (a 2.2% JD.com premium over Samsung/SK-based modules) is excluded from the
observable**: single-outlet, cross-confirmation failed, **and it uses a level observation to argue about a rate**.
⚠ **`[news]` grade declared**: every capacity figure above is from news bodies (mt 07-26 citing SemiAnalysis),
**not from an issuer filing** — which is exactly why the observable is written *"from a primary source"*.
**Confirming it is half of what this scenario is for.**
⚠⚠ **Do NOT score this on the KOSPI.** On the day of registration the KR feed named CXMT as the driver of a
**−7.4%** memory-led session (M196). **That is a price reaction, not this bracket's observable.**

---

## Scoring-log rows added 2026-07-29 by the `industry_kr` run

| ID | Registered | Event date | Branch fired | Scored on | Note |
|---|---|---|---|---|---|
| — | — | — | ★ **ZERO past-dated rows were unscored this run** | 2026-07-29 HANDOVER (industry_kr) | **Every row whose event predates today was already settled by the two 07-28 runs**: S8 FIRED-B · S12 FIRED-B(observable)/AMBIGUOUS(decision axis) · S20 FIRED-B · S28 FIRED-A · S33 FIRED-A raw / branch-B beta-adjusted. **S32 is not scoreable (its CFTC release publishes 07-31), not EXPIRED.** ⚠ **The eight rows dated 2026-07-29 — S2 · S9 · S11 · S13 · S16 · S17(window opens) · S18 · S19 · S23 · S24 · S30 · S35 — had NOT printed at this run's 08:39 KST clock** (KR pre-open; the US events land tonight). **This stage deliberately did not attempt to score them**: filling a 07-29 close from a pre-open tape is exactly the observable-fabrication L3 `scenario_score` forbids. `EXPIRED` count = **0**; silent skips = **0** |
| **S33** *(independent reproduction, not a re-score)* | 2026-07-28 (industry_kr MACRO) | 2026-07-28 close | *(already FIRED-A raw / B adjusted)* | 2026-07-29 (industry_kr MACRO §D-2) | ★ **The KR desk re-derived the beta-adjusted leg from its own code path and reproduced the US desk's scoring to 0.003pp**: S-Oil **−6.37** (US read −6.374) · SK이노 **−0.77** (−0.771) ⇒ median **−3.57pp** (−3.573). **The L3-bis verdict is not an arithmetic error.** ⚠ Also reproduced: **010950's beta is −0.118**, a negative equity beta — a window artifact, so that leg is the weakest row in the table and is labelled as such |
| **S38** | **2026-07-29 (industry_kr DEEP-INDU / BET)** | → **2026-08-12** | — | — | ARMED — ★ **accumulation vs a crowded short on ONE name; nothing in S1–S37 brackets a short-balance observable** |
| **S39** | **2026-07-29 (industry_kr DEEP-HLTH / ALPHA)** | **event-conditional → next benchmark ≤−3% session** | — | — | ARMED — ★★ **the shelter claim's second observation, and it is beta-adjusted BY CONSTRUCTION (the D82 fix applied at registration rather than after)** |

---

## S38 — ★ 006360 GS건설: accumulation against the largest crowded short this desk has measured in KR · ARMED · → 2026-08-12

Registered **2026-07-29 by the `industry_kr` DEEP-INDU and BET stages.**

**The gap it fills.** Every KR bracket in S1–S37 uses price, flow, a filing or a macro series.
**None uses the short-balance series**, even though `module_flow ⑧` has printed it all along.
This name is the cleanest possible test because the two forces are **directly opposed on one ticker**:

**State at registration** `[measured, asof 2026-07-28 settled]`:
- **Short balance 3.63% of float, `building(+0.08)`, 🔥crowded** — the largest this desk has measured in KR.
- **KIS 20d actuals: 외 +80.4만 · 기 +328.5만 · 개 −411.2만** = unambiguous real-hands accumulation.
- `vol_surge` **2.07**, OBV 매집, RS20 **+30.9** / RS60 **−34.9** vs `069500.KS`.
- Crash-day beta-adjusted residual **−6.64pp** (β 0.513), i.e. **outside the ±2pp noise band**.

**Observable (frozen)**: the **KRX short balance as % of float**, on **2026-08-12**.
⚠ **This is a stock-of-shorts observable, not a price observable** — chosen deliberately so the
bracket cannot be settled by frozen mechanics (the L3-bis failure mode, and D82's lesson).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Short balance **≤ 2.00%** on 2026-08-12 (a `covering` unwind) | The accumulation won. A crowded short unwinding into measured real-hands buying is the one configuration where the desk's B-grade axis and the positioning axis agree — and it would make the **−6.64pp residual a short-driven distortion, not information about the business** |
| **B** | Short balance **≥ 5.00%**, still `building` | The short won. **The 🟢 is accumulation being sat on**, and this name's flow tag must be read with the short balance attached from here on — a general lesson, not a single-name one |
| **C** | Between **2.00% and 5.00%** | No information. **Re-register with a tighter band; do not widen it after the fact** |

**Anti-signal (kills the bracket outright)**: a **domestic housing-policy or PF/credit event** that moves
the whole 건설 bucket — then the short move is a sector event and this name's specific test is void.
Live risk, quantified at registration: illegal private lending **₩1.5tn**, bank household-loan
delinquency at a **10-year high**, and this name is **domestic housing only** (plant exposure zero).

⚠ **Not a position.** GS건설 carries a `🟡PARTIAL` ALPHA tag with a hard-stop stamp; this bracket
exists to score the **mechanism**, not to justify the name.

---

## S39 — ★★ The pharma shelter property: a second observation, beta-adjusted at registration · ARMED · event-conditional

Registered **2026-07-29 by the `industry_kr` DEEP-HLTH and ALPHA stages.**

**The gap it fills.** This run's **M-07 HIT** and **M-13's shelter half** both rest on **one session**:
on 2026-07-28 (`069500.KS` **−11.190%**) the beta-adjusted residuals were **삼성바이오 +2.49 and
셀트리온 +2.16, the board's #1 and #2**, with 삼바 absolutely positive at **+0.26%**.
**n = 1 (S1).** A property observed once is a coincidence with a name.

★ **And this bracket applies D82 at registration rather than after the fact** — the defect that forced
the S33-ANNEX. The observable is **the beta-adjusted residual**, not raw excess return, precisely
because on a large benchmark move a low-beta name prints a large positive excess **mechanically**
(measured: pure beta predicted **+8.96pp** for 삼바 and it delivered **+11.45pp**; the information is
the **+2.49pp difference**, not the 11.45).

**Observable (frozen)**: the **beta-adjusted residual** of **207940 and 068270** vs `069500.KS`,
on the **next session where `069500.KS` closes ≤ −3.0%**.
**Method frozen with it** (so a later scorer reproduces it): β estimated on the **60 sessions ending
the day before that session**, `residual = excess − (β−1) × benchmark return`.
**Betas at registration: 207940 = 0.200 · 068270 = 0.258.**

| Branch | Observable | Meaning |
|---|---|---|
| **A** | **Both** residuals **> +1.0pp** | Shelter is a **property**, not a one-day coincidence. M-07's OW keeps its only genuinely tested leg, and M-13's *"the defensive label broke in two directions"* keeps its positive half |
| **B** | **Either** residual **< 0** | The 07-28 reading was **n=1 luck**. M-07's OW falls back to flow and multiples with **no tested price axis**, and **M-13's shelter half dies** |
| **C** | Both inside **0 to +1.0pp** | Inside the estimation-error band (this desk's own ±2pp caveat) ⇒ **`AMBIGUOUS`, recorded as such.** Do not read a small positive as confirmation |

**Undated by construction, and that is stated rather than hidden**: it fires on the market's schedule,
not the calendar's. ⚠ **Expiry to prevent an unscoreable row living forever: if no ≤−3.0% session
occurs by 2026-10-31, score `VOID` and re-register on a different observable.**

⚠ **Do NOT substitute an up-day.** A shelter property is only testable on a down day; the 07-24 run
already logged a rising session as `unknown` (C3) rather than scoring it, and that discipline holds.

---

---

## Brackets registered 2026-07-30 by the `industry_kr` run

## S43 — ★★ Is the shelter property a NAME or a SECTOR? · ARMED · event-conditional

Registered **2026-07-30 by the `industry_kr` MACRO stage, before the event.** **S39's successor.**

**Why.** S39 asked *"do BOTH pharma legs print a positive residual"* and scored **FIRED-B**: on the
2026-07-29 session (`069500.KS` **−6.344%**) the residuals were **207940 −3.38pp** and
**068270 +2.98pp** — a **6.4pp split** one session after they were the board's #1 and #2. So the
sector reading is dead (**R27**), and the remaining question is different and sharper:
**is 068270's two-session run (+2.16 → +2.98, monotone, absolutely positive at +1.47% on a −6.3%
session) a low-beta shelter property, or is it simply a name holding good news?** That name printed
**2Q OP ₩451.8bn, +86.3% YoY** and carries *"obesity and ADC readouts imminent"* [8 articles / 7
outlets, 07-29], with **바이오시밀러 🟡ACCELERATING 3.98×** against **CDMO 🔴FADING 0.28×**.

**Observable (frozen)**: the **beta-adjusted residual of 068270** vs `069500.KS`, on the **next
session where `069500.KS` closes ≤ −3.0%**. **Method frozen with it** (so a later scorer reproduces
it): β estimated on the **60 sessions ending the day before that session**,
`residual = excess − (β−1) × benchmark return`. **β at registration = 0.24.**
**Reported alongside but NEVER merged into the verdict**: the same session's residuals for
**207940 · 128940 · 326030**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 068270 residual **> +1.0pp** ∧ **at least 2 of the other 3 negative** | The property belongs to the **NAME**. "제약 OW" is confirmed as the wrong unit of analysis (**W5** settled), and the desk stops writing sector-level shelter claims |
| **B** | 068270 residual **< 0** | The two-session run was **its own news, not shelter** ⇒ the shelter claim dies outright and **M-16 dies with it** |
| **C** | 068270 **0 ~ +1.0pp**, **or all four names carry the same sign** | `AMBIGUOUS`. Four same-sign names is a **bucket event** and does not support the name hypothesis. **Re-register with a tighter band; do not widen it after the fact** |

**Anti-signal (kills the bracket outright)**: **a 068270-specific disclosure** (trial data, an order,
an equity raise) landing on that session ⇒ the low-beta axis and the news axis become inseparable,
so score `VOID` and re-register on a different session.
⚠ **Expiry**: if no `069500.KS` session ≤ −3.0% occurs by **2026-10-31**, score `VOID`.
⚠ **KR has no implied-move axis**, so the ±1.0pp band is **hand-set and declared as such** (the
`module_KIS` options-IV **v1.1** is the prerequisite for a genuine KR threshold).
⚠ **Do NOT substitute an up-day.** A shelter property is only testable on a down day.

## S43-ANNEX — ★★ estimator-error notice (**S43 is NOT re-frozen**)

Registered **2026-07-30 by the `industry_kr` ALPHA stage**, on the **S14-ANNEX / S33-ANNEX precedent**.

**S43 was frozen at MACRO with a ±1.0pp band. Hours later this run's own DEEP-STPL measured the
same estimator's error on a sibling cohort and it is wider than the band:** beta regression
**R² 0.00–0.01**, β **sign-flips with window length**, and the **own-residual σ runs 2.3–3.8pp**.
A ±1.0pp threshold sits entirely inside that σ, which means S43 could settle on estimation noise —
the L3-bis failure mode ("a bracket whose observable can settle on frozen mechanics is not a test").

⚠⚠ **S43 IS NOT RE-FROZEN.** Moving a registered threshold after the fact is what L3
`scenario_score` forbids. Instead, **at scoring both readings are recorded side by side**:
1. the **±1.0pp verdict exactly as S43 froze it**; and
2. the **residual σ of 068270 and 207940, measured on that session's own estimation window.**
**If the verdict falls inside σ, that is the finding** — and it becomes the **second KR instance of
L3-bis**.
★ **What is NOT yet known and is recorded as `unknown` (C3)**: σ 2.3–3.8pp was measured on the
**staples** cohort. **The pharma legs' σ has never been measured.** The S43 scoring run must measure
it in the same pass rather than importing the staples number (that would be a **W1** violation
inside one market).
**Registration-discipline defect logged as D93**: *before freezing a relative-return or residual
observable, measure the estimator's own residual σ and state whether the threshold lies outside it.*
(**D82** was "check the legs' betas"; this is "check the error".)

## S44 — ★★ Who sold? The crash's agent, read off the KRW sign · ARMED · event-conditional

Registered **2026-07-30 by the `industry_kr` MACRO stage, before the event.**

**Why.** On **2026-07-29** `069500.KS` fell **−6.344%** (KOSPI −5.99% to 5,663.08, the **first-ever
back-to-back circuit breakers**) while the **won STRENGTHENED 15 to the 1,440s — a five-month high
for the currency** [39 articles / 6 outlets, the day's lowest-dispersion head item]. The domestic
feed's repeated causal story was *"foreigners and leveraged ETFs drove a selling spiral"* (₩3,000tn
of value erased). **A foreign-capital-flight equity crash comes with a weaker currency. The sign does
not match.** Supporting the domestic-liquidation alternative: **credit-financing balance −15.2%**
(M159), the FSC opening **leverage-ETF multiplier and professional-investor restrictions**,
**`증안펀드` appearing as a brand-new token (3 hits in 30 days, all of them yesterday)**, **₩22tn
into term deposits in one month**, and **index-futures 괴리율 −0.01% = no derivative dislocation
across both circuit-breaker sessions**. Against it: a *"dollar at a one-week low"* narrative exists
after the hawkish FOMC hold.
★ **This bracket exists partly because the axis is unsweepable**: **`환율` is two characters, so the
`--kr` trigram index returns 0 for it forever (D63)** — the trajectory axis and the price series are
the only ways to see Korea's largest macro variable.

**Observable (frozen), two legs reported SEPARATELY and never merged**:
1. the **won/dollar close direction** (sign vs the prior close) on the **next session where
   `069500.KS` closes ≤ −3.0%**; and
2. **`DTWEXBGS`'s next print (~2026-08-04)**, as a percentage change against **120.71 (asof 07-24)**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | index ≤ −3% ∧ **won stronger** ∧ DTWEXBGS change **> −1.0%** | **Domestic-liquidation reading.** The "foreign flight" story is sign-wrong, and this is the class of decline that policy tools act on directly |
| **B** | index ≤ −3% ∧ **won weaker** | Ordinary capital-flight shape ⇒ **M-15 is retracted** |
| **C** | won stronger **but** DTWEXBGS **≤ −1.0%** | Dollar weakness explains it ⇒ **M-15 is retracted** (hypothesis (b) wins) |

⚠ **Price series only** — the news axis cannot cross-check this (D63).
⚠ **Expiry**: if no `069500.KS` session ≤ −3.0% occurs by **2026-09-30**, score `VOID`.
⚠ **Score the sign pair, not the magnitude.** n will be 1 (**S1**).

## S45 — ★★ The FSC governance package's announced clause form · ARMED · → 2026-09-30

Registered **2026-07-30 by the `industry_kr` ALPHA stage, before the event.** **S11's successor.**

**Why S11 could not settle.** S11 froze *"is the three-term limit **enacted** as originally proposed"*
and took its date from `catalyst_calendar` (2026-07-29). **Enactment is a National Assembly act; the
07-29 date was an executive-announcement date — two observables that cannot settle on one day.**
And the announcement itself has slipped at least twice: expected **07-22**, deferred, and an FSC
official states the date **is still not set**. ⇒ S11 stays **PENDING (deadline 08-06)**, is **not
re-frozen**, and this bracket runs beside it on something that actually prints.

**Draft content confirmed from primary reporting at registration** (hankyung 07-27 exclusive + same-week
corroboration): **one reappointment only = 3 + 3 = six years maximum, written into the
금융회사지배구조법**; **two-thirds shareholder approval to reappoint**; `사외이사` renamed
`독립이사` with an **all-independent nomination committee**; **nomination rights at 0.1% ownership**.
An alternative option — escalating approval thresholds **majority → 70% → 90%** — is on the table but
a 정무위 source calls option 1 *"effectively the centre of the discussion."*

**Observable (frozen)**: the **form of the chairman-tenure clause in the package the FSC actually
announces**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Announced **as statutory amendment text** (tenure limit in the 지배구조법) | Succession uncertainty reprices **every major holdco at once** — a sector-wide governance event, not a single name. **105560 KB금융 is named in the primary reporting as the first affected, its next chairman being selected in November** |
| **B** | Announced as **administrative guidance / best-practice code**, or the statutory clause is dropped from the package | Uncertainty **persists rather than resolving.** ⚠ **Do not read a softer form as "resolved bullish"** |
| **C** | **No announcement by 2026-09-30** | `AMBIGUOUS`, and **re-register on "referral to the National Assembly 정무위"** rather than widening this threshold |

**Anti-signal (voids the bracket)**: the presidential office or the ruling party **formally
withdrawing** the legislative approach.
⚠ **Score the clause form, not the share-price reaction** of any holdco.
⚠ **Carried, not resolved**: the desk's FIN verdict stays **Neutral with M-01 retracted** either way
— this bracket scores a regulatory observable, not a sector view.

## Brackets registered 2026-07-31 by the `industry_kr` run

## S17-ANNEX — ★★ leg-timing notice (**S17 is NOT re-frozen**)

Registered **2026-07-31 by the `industry_kr` HANDOVER/MACRO stages**, on the
**S14-ANNEX / S33-ANNEX / S43-ANNEX** precedent.

**Why this exists.** S17 froze *"the ADR-to-ordinary premium, measured on closes, 07-29 → 08-05"*.
**Until today the desk had never computed that number itself** — M162's "29%" was a WSJ quote.
This run built the series `[measured]`:

`SKHY` (Nasdaq, longName *SK hynix Inc.*, USD) **x ADR ratio 10:1** x `KRW=X` / `000660.KS` − 1.

| date | ADR $ | ordinary KRW | USDKRW | ADR in KRW (x10) | **premium** |
|---|---|---|---|---|---|
| 07-22 | 165.27 | 1,830,000 | 1,479.72 | 2,445,533 | +33.6% |
| 07-23 | 169.50 | 1,919,000 | 1,475.63 | 2,501,193 | +30.3% |
| **07-24** | 154.57 | 1,759,000 | 1,474.04 | 2,278,424 | **+29.5%** |
| 07-27 | 143.02 | 1,816,000 | 1,458.01 | 2,085,246 | +14.8% |
| 07-28 | 130.17 | 1,550,000 | 1,464.44 | 1,906,261 | +23.0% |
| **07-29 (window D+0)** | 126.79 | 1,401,000 | 1,453.16 | 1,842,462 | **+31.5%** |
| **07-30 (window D+1)** | 149.00 | 1,322,000 | 1,442.28 | 2,148,997 | **+62.6%** |

⚠ **The 10:1 ratio is `[inferred]`** — derived from yfinance `sharesOutstanding` 7,098,548,910 / 10 =
709.85m, which reconciles with the pre-issue ordinary share count. **But it passed an independent
external check: the computed 07-24 premium 29.53% against WSJ's reported 29% — a 0.5pp match against
a source the construction never saw.** Tagged `[inferred, externally corroborated at one point]`; the
premium series itself is `[measured]`.

**The defect this annex records.** The ADR trades **~13.5 hours after** the KR close, so a same-date
pairing is a **stale-leg spread, not a contemporaneous premium**. On 07-30 the ordinary fell **−5.6%**
while the ADR rose **+17.5%** — the 62.6% therefore embeds information the KR session had not traded.
The series ran **14.8% to 62.6% in three sessions**, which is the volatility that mismatch produces.

⚠⚠ **S17 IS NOT RE-FROZEN.** Moving a registered threshold after the fact is what L3
`scenario_score` forbids. Instead, **at the 2026-08-05 scoring both readings are recorded side by
side**:
1. the **same-date premium exactly as S17 froze it**; and
2. the **ADR leg lagged one session** so the two legs share an information timestamp.

**If the two readings point to different branches, that is the finding** — and it becomes the
**third KR instance of L3-bis** (after S33 and S43-ANNEX).

★ **Current standing, on the frozen same-date reading**: both in-window sessions are **>=25% =
branch B territory**, and branch A (**<=15%**) was touched only on **07-27, before the window opened**.
⇒ **the 000660 flow suspension stays on**, and this is a reason to hold it **longer**, never to lift
it (rule D1 / retracted R1). Anti-signal unchanged: **an issuer disclosure raising the 2.5% ceiling
voids S17 outright.**
**Registration-discipline note (D93 family)**: *before freezing an observable built from two markets'
closes, state whether the legs share an information timestamp.*

## S46-KR — ★★★ The first session that knows SK이노's profit was lubricants, not crack · ARMED · 2026-07-31 close

Registered **2026-07-31 by the `industry_kr` MACRO stage, before the session's close.**
⚠ **ID suffixed `-KR` because S46–S49 were taken by the 2026-07-30 `industry_US` PREMORTEM (D76).**

**Why.** 096770 SK이노베이션 filed 2Q at **2026-07-30 16:03 KST — after the 15:30 close.** The +6.48%
it printed on 07-30 (residual **+7.02pp** vs `069500.KS` −2.199%, beta 0.24) happened **before the
information existed.** What the filing actually says `[measured, company release + yonhap body]`:

- OP **KRW 3.4873tn** (from a −KRW 401.6bn operating loss a year earlier), revenue KRW 29.1572tn (+49.9% YoY)
- **SK엔무브 (lubricants) KRW 691.9bn, QoQ +KRW 503.4bn** — reason given: *"중동 지역 주요 경쟁사 공급
  차질에 따라 윤활기유 사업 마진이 상승"*, on **Group III** base oil
- **SK온 (battery) KRW 821.8bn, QoQ +KRW 1.1710tn** — the largest quarterly profit since the 2021 spin-off
- **SK에너지 (refining) KRW 651.2bn, of which inventory-related gain approx. KRW 560.0bn = 86.0%**, and
  ***"분기 말 유가 하락으로 6월에는 손실로 전환"***
- ⚠ **C2, both halves**: pre-tax income **KRW 569.7bn** (QoQ −KRW 825.2bn) — an operating-to-pretax gap
  of **KRW 2.9tn** (1H derivative loss KRW 1.2169tn on SK온 PRS, non-cash per the company; SKIET
  impairment approx. KRW 1.4720tn). The company's non-cash characterisation is **recorded, not
  verified (C3)**.

⇒ **crack margin explains approx. KRW 91.2bn = 2.6% of operating profit.** The "정유주" label does not
describe this quarter.

**Observable (frozen)**: the **beta-adjusted residual of 096770 on the 2026-07-31 close**,
benchmark **`069500.KS`**, **beta estimated on the 60 sessions ending 2026-07-30**,
`residual = excess − (beta − 1) x benchmark return`. **beta at registration = 0.24.**

| Branch | Observable | Meaning |
|---|---|---|
| **A** | residual **> +3.8pp** | The market re-prices the non-refining profit as good news ⇒ **M-19's (a) reading is supported: the tracking KPI is Group III spread + SK온 ESS orders, not the crack** |
| **B** | residual **< −3.8pp** | The market reads "only 2.6% of profit is margin" as bad news ⇒ **M-19's (a) is still supported, with the opposite sign** — either way the label was the live variable |
| **C** | residual **−3.8 to +3.8pp** | `AMBIGUOUS` — no information. The print did not move the name relative to its benchmark |

★ **The ±3.8pp band is derived, not hand-set**: it is **M260's measured own-residual sigma (2.3–3.8pp)
for this estimator**, and the upper bound is taken. **This is D93 applied at registration rather than
discovered afterwards — the first KR bracket to do so.**
**Anti-signal (voids the bracket)**: if 2026-07-31 sees `069500.KS` **<= −3.0%** or crude (`BZ=F`)
**moves ±5%**, the name's move cannot be separated from a sector/commodity event ⇒ score **`VOID`**
and re-register on the next clean session.
⚠ **Score the residual, not the headline.** n = 1 (**S1**).

## S47-KR — ★★ Does S-Oil reproduce the "86% inventory gain" split? · ARMED · 2026-08-03 10:00

Registered **2026-07-31 by the `industry_kr` MACRO stage, before the print.**

**Why.** S46-KR's finding is one company. **M-19 generalises it to "KR refining 2Q profit is inventory
and oil level, not crack margin" — and that generalisation is exactly what should be bracketed rather
than assumed.** 010950 S-Oil files 2Q at **2026-08-03 10:00**.
⚠ Note the estimator constraint carried on this name: **010950's beta is indistinguishable from zero
across 7 windows (|beta| <= 0.068, sign flips 3x, M253)**, so **a residual bracket is not usable
here** — which is why this bracket is written on a **filing ratio**, not on a return.

**Observable (frozen)**: **inventory-related gain / refining-segment operating profit**, as disclosed
in 010950's 2Q release.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | ratio **>= 50%** | The split is a **KR refining property**, not an SK accounting position ⇒ **M-19 generalises**, and `정제마진` is formally dropped as a KPI for this node (already at n=35 with a 7d mean of 0.4, D45's 11th run) |
| **B** | ratio **< 50%** | The 86% is **SK-specific** ⇒ **M-19's generalisation is withdrawn**, and the two refiners must be tracked on different KPIs |
| **C** | the company **does not disclose an inventory-gain figure** | `AMBIGUOUS`. ⚠ **Do NOT substitute an estimate** — that is precisely the failure D95 recorded when a crack level was reconstructed from a different bar granularity. Record the non-disclosure as the finding and re-register on the 반기보고서 |

**Anti-signal (voids)**: a **재고자산평가손실** driven by a post-quarter crude collapse changes the
accounting question being asked ⇒ re-register rather than force a branch.
**Side observations to record at scoring (not part of the verdict)**: whether the release mentions the
**샤힌 프로젝트** capex/start-up schedule (EVENT_ALPHA CARD 8 could not obtain a body and was held
below card status), and whether **M-12's 최고가격 loss-compensation booking** finally carries a number
— the filing deadline moved **August to September** with final settlement *"around year-end"*, so a
blank here is **expected, not a new finding**.

## Brackets registered 2026-08-02 by the `industry_kr` run

## S48-KR — ★★★ S38's bigger twin: a crowded short against the sheet's largest accumulation · ARMED · 2026-08-12

Registered **2026-08-02 by the `industry_kr` BET/ALPHA stages, before the event.**
⚠ **ID suffixed `-KR`: S48 was taken by the 2026-07-30 `industry_US` PREMORTEM (D76).**

**Why.** **M219** recorded 006360 GS건설's **3.63% of float, `building`, 🔥crowded** as *"the largest
short pressure this desk has measured in KR"*, and **S38** brackets it on **2026-08-12**.
**This run measured a bigger one on a different name**, and it sits against this sheet's largest
real-hands accumulation:

**State at registration** `[measured, asof 2026-07-31 settled]` — **006340 대원전선**:
- **Short balance 4.00% of float, `building(+0.99)`, 🔥crowded** (KRX via `module_flow ⑧`) — **larger
  than the 3.63% M219 called the desk's maximum.**
- **KIS 20d actuals: 외 +152.6만 · 기 +299.7만 · 개 −462.3만** = both legs positive, and the
  institutional leg is **the largest on this run's entire sheet**.
- 07-31 beta-adjusted residual **+7.60pp (+2.63σ against the session's own base rate)**; `flow_score`
  +0.77, OBV +0.34, RS20 +22.2, RS60 −20.1; **not price-limit censored** (+? intraday; close move
  inside the ±30% band).
- ⚠ **The name's driver is contested and that is stated at registration**: this run's DEEP-UTIL read it
  as a **copper** chain and its own ALPHA stage **retracted that** — the domestic body names
  **MS earnings → AI-capex** (*"MS '깜짝 실적'에 AI 투자 수익성 'OK'… 전선주, 두 자릿수대 급등"*
  [mt 07-31]) and **all four copper theme probes are dead** (`구리가격` 🔴 0.0× · `신동` 🔴 0.0× ·
  `비철금속` 🔴 0.37× · `전선` ⚪ 0.62×). **Direction stands, driver retracted.**

**Observable (frozen)**: the **KRX short balance as % of float for 006340**, on **2026-08-12**.
⚠ **A stock-of-shorts observable, not a price observable** — chosen so the bracket cannot be settled
by frozen mechanics (the L3-bis failure mode; D82's lesson).
★ **The date is deliberately the SAME as S38's** so the two names settle on one date and the pair
becomes a 2-observation test of the same configuration instead of two anecdotes.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | Short balance **≤ 2.50%** on 2026-08-12 (a `covering` unwind) | The accumulation won. Two names, same date, same configuration ⇒ **the first KR datapoint on "crowded short + measured real-hands accumulation" that is not n=1** |
| **B** | Short balance **≥ 5.50%**, still `building` | The short won, and **the 🟢-adjacent flow reading is accumulation being sat on** — a general lesson about reading KR flow tags without the short balance attached |
| **C** | Between **2.50% and 5.50%** | No information. **Re-register with a tighter band; do not widen it after the fact** |

**Anti-signal (kills the bracket outright)**: a **copper-price shock (`HG=F` ±10% over the window)**
or a **006340-specific disclosure** (order, equity raise, control transfer) ⇒ the short move is a
commodity/company event and the configuration test is void; score `VOID` and re-register.
⚠ **The band is hand-set and declared as such** — KR has no implied-move axis, and **the desk has never
measured the distribution of 2-week changes in KRX short balance**, so ±1.5pp around the current 4.0%
is a choice, not an estimate (**C5**). ⚠ **Do NOT read "short building" as bearish** — that sits in
this desk's **REJECTED** signal ledger (D6), and Law 3 says shorts *supply* liquidity.
⚠ **Not a position.** 006340 carries a **🟡PARTIAL** tag with a momentum-only flag and a hard-stop
stamp; this bracket scores the **mechanism**, not the name.

## S49-KR — ★★ 롯데렌탈: the control transfer the theme axis could not see · ARMED · 2026-10-30

Registered **2026-08-02 by the `industry_kr` DEEP-DISC / ALPHA stages, before the event.**

**Why this exists, and it is a lesson about this desk's instruments before it is about the name.**
`STANDING_VIEW_KR §3b` carried 089860 for two runs as *"a LIVE name with clean legs and **no thesis
at all** … its theme is `자동차렌탈` **⚫SILENT, 0 hits ⇒ zero live narrative**."*
**Both halves of that were measured correctly and the conclusion was still wrong.**
- `자동차렌탈` **⚫SILENT, 0 hits** — reproduced this run. ✅
- **`지분매각` 🟡ACCELERATING, 7d mean 2.1, accel 10.71×, 31 hits — the fastest accelerating theme
  this run measured.** ⇒ **the name's live narrative exists; the desk was querying the wrong axis.**
- **DART carries the object**: **rcpNo 20260731800783**「풍문 또는 보도에 대한 해명(미확정)」, a
  **re-disclosure** of the 2026-07-01 filing. Rumour: 「**롯데렌탈, TPG에 팔린다…1조대 빅딜**」
  [한국경제 등]. Company: ***"최대주주 등에게 확인한 결과, TPG 측과 롯데렌탈 지분매각 관련 실사 등
  논의를 진행한 바 있으나, 아직까지 구체적으로 확정된 사항은 없습니다."***
  **재공시예정일 2026-10-30**, 공시책임자 IR실장 권성율.
- **A second bidder is named in the feed and not in the filing**: 「한국타이어, 렌터카 시장 뛰어든다…
  **롯데렌탈·SK렌터카 인수 추진**」[hankyung 07-27] and 「조현범 한국앤컴퍼니 회장, 오늘 **가석방**…
  렌터카 사업 **M&A 직접 챙길 듯**」[sedaily 07-30].
- Money `[measured]`: **KIS 20d 외 +7.2만 · 기 +13.9만 · 개 −19.4만** (both legs), **RS20 +43.2 = the
  highest of the 95 names in 유통 ∪ 일반서비스**, RS60 +24.2, 🟢가속 flow +0.97, short balance
  **0.56%float `covering(−0.19)`**.

**Observable (frozen)**: the **form of the 2026-10-30 re-disclosure by 089860** (DART).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | A **확정** disclosure — a signed SPA / 최대주주 변경 / 지분양수도 계약 체결, with a counterparty named | The transaction thesis settles. **And the instrument lesson is confirmed: the desk's theme axis was blind to a live control transfer for two runs** |
| **B** | **Another 「미확정」 re-disclosure**, or a disclosure that the process ended without a deal | **The transaction thesis is not confirmed.** ⚠ **A second "미확정" is NOT automatically the kill** — S22 taught the opposite lesson, that a deferral only counts as a kill if it was *pre-registered* as one, and **it is pre-registered here: a third 「미확정」 (i.e. one beyond this bracket's own settlement) IS the kill** |
| **C** | **No disclosure by 2026-10-30** | `AMBIGUOUS` — and it is a **filing-obligation** failure, which is itself the finding. **Re-register on the 3Q 분기보고서; do not widen this threshold** |

**Anti-signal (voids the bracket)**: a **counterparty other than TPG or 한국앤컴퍼니** signing, or a
**롯데그룹 형태의 구조 변경**(합병·분할)이 매각을 대체 ⇒ the observable is measuring a different object;
score `VOID` and re-register.
⚠ **Score the disclosure form, not the share-price reaction.**
⚠ **W4 is unmet and stated**: the name's customers (corporate/retail long-term rental users) have no
disclosed spend series this desk can read ⇒ the thesis rests on **the transaction, not on demand**.
⚠ **Live negative recorded at registration, not buried**: 「'공짜 사은품'이라더니 3배 바가지…편법 영업한
롯데렌탈, 할부금 30% 깎는다」[asiae **2026-08-02**] — a consumer-protection action, **not part of the
observable**, and **not scored**.

---

## Brackets registered 2026-08-04 by the `industry_kr` run

⚠ **IDs suffixed `-KR`: S50 and S51 were taken by the 2026-07-31 `industry_US` PREMORTEM (D76).**
Checked at WRITE time against all three `SCENARIOS*.md`, both `STANDING_VIEW*.md` and `RESEARCH.md`
— `grep S50-KR|S51-KR` returned **0 in all seven**.

## S50-KR — ★★★ Is the desk's own benchmark tracking its index? · ARMED · → 2026-08-07

Registered **2026-08-04 by the `industry_kr` MACRO stage**, on this run's largest instrument finding.

**Why this is a bracket and not a footnote.** `069500.KS` is not a name on the sheet — it is
**the input to `scripts/exposure_rule.py`**, which sets the desk's target invested weight, and it is
**the denominator of every excess-return figure this desk computes.** Measured this run:

| session | `069500.KS` | KOSPI composite `^KS11` | gap |
|---|---|---|---|
| 2026-07-31 | **+24.174%** | **+17.911%** | **+6.26pp** |
| 2026-08-03 | **−8.928%** | **−5.129%** `[KIS 기초지수 역산]` | **−3.80pp** |

⇒ a **10.06pp two-session swing** in the instrument that decides how much the desk is invested.
On 08-03 the exposure rule read *"당일 −8.928%"* where the index fell **−5.13%**.
★ The 08-03 index value is **re-derived from a primary** (`module_KIS --futopt A05608` → 기초지수
종합 6,335.42, +1.25% ⇒ prior close 6,257.2); cross-checked on the same call's KOSPI200 leg
(999.40 / 1.0129 = 986.68 vs yfinance's 986.72 = **0.004% agreement**).

**Observable (frozen)**: **`|069500.KS daily % − ^KS11 daily %|`** on each of the **next three settled
KR sessions** (2026-08-04, 08-05, 08-06 closes; if a session is missing, extend to the next settled one).
⚠ **`auto_adjust=False`**, stated because the convention has already moved a number on this desk
(the 07-30 −2.199 / −2.00 case). ⚠ If `^KS11` has no bar for a session, substitute the **`module_KIS
--futopt` 기초지수 종합** for that session and say so — **do not use `^KS200`** (D146: path-dependent).

**Threshold — taken from the measured spread, not chosen round.** The two observed gaps are 6.26 and
3.80pp; their mean is 5.03pp. **The line is set at one third of the smaller observation: 1.5pp**, so
branch A requires the deviation to fall to well under half of anything yet seen.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | **all three** sessions < **1.5pp** | The 07-31/08-03 deviation was a **crash/rebound ETF-premium artifact** ⇒ only those two sessions' residuals are contaminated, and the benchmark choice needs no human decision |
| **B** | **any one** session **≥ 3.0pp** | The deviation is **recurring**, not an artifact ⇒ **the benchmark used by `exposure_rule` becomes a human decision item (P5)**, and every stage must publish residuals against **two** indices |
| **C** | all three in **[1.5, 3.0)pp** | `AMBIGUOUS` — persistent but small. **Re-register with a longer window; do not widen this band** |

**Anti-signal (voids)**: a **KRX-wide trading halt / circuit breaker** truncating any of the three
sessions ⇒ the ETF and the index trade on different clocks by construction, so the gap is not the
object being measured. Score `VOID` and re-register on the next three uninterrupted sessions.
⚠⚠ **Scope, stated so branch B is not over-read (C4)**: `069500.KS` tracks **KOSPI200**, and the
comparison index here is the **composite**. **KOSPI200's history is unavailable** (`^KS200` stale
since 07-16 in one path, single-row in the other — D129/D146), so part of any gap is
**composite-vs-200 dispersion**, which was itself extreme on 08-03 (**KOSPI −5.1% vs KOSDAQ +2.4%,
KOSDAQ buy sidecar**). **Branch B therefore establishes "the desk's benchmark and the most-quoted
index diverge repeatedly" — NOT "the ETF has tracking error."**
⚠ **This bracket changes no sector direction and sizes nothing.** It is an instrument test.

## S51-KR — ★★ S47-KR's primary-source re-confirmation · **SCORED `FIRED-C` 2026-08-17** (was ARMED · → 2026-08-17)

> ✅ **SETTLED 2026-08-17 by the `industry_kr` HANDOVER stage. Full verdict + evidence is in the MASTER scoring log**
> (`SCENARIOS.md`, "Scored by the 2026-08-17 `industry_kr` run"). One-line: **the filing exists (2026-08-14, day one of the
> window), the DENOMINATOR reproduces to 0.0041% (2Q26 refining OP 532,378 vs the 532,400 scored off a news body), and the
> NUMERATOR does not exist — 「재고관련」 appears 0 times in the entire filing.** Anti-signal NOT fired (segment basis unchanged)
> ⇒ not `VOID`. **S47-KR is not re-scored; M-19″'s ratio anchor loses its primary.**


Registered **2026-08-04 by the `industry_kr` DEEP-ENRG stage, immediately after scoring S47-KR.**

**Why.** S47-KR was scored **FIRED-B on a conference-call figure carried by news bodies**, because the
observable (「재고관련이익 ÷ 정유부문 영업이익」) **does not exist in the 공정공시 form**. The desk's own
staged rule from 2026-08-03 says: *"when a number arrives from the news feed and a filing exists for
the same event, the filing decides the magnitude — every time, not when it feels doubtful"*, measured
at **9.3×** on the KDDX case. **This bracket pre-commits the desk to running that check on its own
verdict, before it can quietly become settled fact.**

**Observable (frozen)**: **010950's 2026 반기보고서 segment note** (DART), specifically the
**2Q refining-segment operating profit** and any **inventory-related gain** disclosed there, against
the values this run scored on: **정유 OP ₩532,400m** and **재고관련이익 ₩113,700m (ratio 21.36%)**.
Filing window: **2026-08-14 ± 3 business days** (the KR semi-annual deadline).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | The filing's numbers reproduce the scored ratio **within ±5pp** (i.e. ratio in **[16.4%, 26.4%]**) | **S47-KR's FIRED-B stands on a primary.** The news-body path is validated **for this class of figure**, and M-19″ keeps its anchor |
| **B** | The filing's ratio lands **outside ±5pp** but still **< 50%** | **The verdict stands, the anchor does not.** ⇒ **S47-KR is NOT re-scored** (thresholds are frozen; the branch is unchanged) but **M-19″'s numbers are rewritten from the primary**, and the news-body path is recorded as **unreliable at this precision** |
| **C** | The filing's ratio is **≥ 50%**, or the segment note carries **no inventory-gain line at all** | ★ **The most informative branch.** ≥50% would mean **the desk scored a bracket the wrong way off a news body** — a first for this desk, and it would force S47-KR to be marked with a primary-source correction notice (not a re-score) plus a retraction of M-19″. A **missing line** returns the observable to `AMBIGUOUS` and confirms the figure is IR-only, never filed |

**Anti-signal (voids)**: 010950 **changes its segment reporting basis** in the 반기보고서 (e.g. merges
윤활 into 정유, or restates 1Q), so the two numbers are not on the same definition ⇒ `VOID`, and
re-register on the 3Q 분기보고서 with the new basis named.
⚠ **Score the filing's number, not the share-price reaction.**
⚠ **Threshold is hand-set and declared as such** — KR has no implied-move axis, and ±5pp was chosen as
roughly a quarter of the scored ratio. **It is not derived from a measured estimator error**, because
this desk has never measured the dispersion between a KR conference-call figure and its later filing.
★ **Producing that measurement is the second thing this bracket buys, regardless of which branch fires.**

---

## Brackets registered 2026-08-05 by the `industry_kr` run

## S52-KR — ★★★ Is the pharma OW a SECTOR proposition or a ONE-NAME proposition? · ARMED · → 2026-08-19

Registered **2026-08-05 by the `industry_kr` DEEP-HLTH stage.**
⚠ **ID note (D137, three greps run at WRITE time)**: highest `S##-KR` = S51-KR · highest `M###` = 383
(KR) / 381 (US) · highest `D###` = 160 · highest `R##` = 45. This bracket takes **S52-KR**.

**Why this exists.** **S43 was `VOID`ed on 2026-08-03** and since then this node has run with **no
falsifier at all**. Worse, this run discovered that **S29's own ignition session was contaminated by
the same anti-signal class that killed S43** — on 2026-07-30, the session whose close (190,000 >
189,737) scored S29 `FIRED-A`, **068270 filed a company-specific disclosure** (CTP55 코센틱스
바이오시밀러 **미국 품목허가 신청**), and the two prior sessions carried the same shape
(07-24: four 투자판단관련주요경영사항 filings; 08-03: CTP44 다잘렉스 국내 임상 3상 — the S43 VOID day).
⇒ **S29 is evidence of a regulatory milestone, not of sector money**, which is why the narrative leg
(`바이오시밀러` 🔴FADING 0.31~0.37×) being dead is **not** a contradiction. **The two legs never
diverged; they were different objects.**

**This bracket fixes S43's two measured failure modes, each explicitly:**
1. **S43's band sat inside its own estimator's noise** (±1.0pp against a measured own-window residual
   σ of **2.923pp** = 0.34×). ⇒ **every threshold here is taken from a measured σ (D93).**
2. **One contaminated observable killed the whole bracket.** ⇒ **two independent observables, scored
   separately; AS-1 VOIDs O1 only.**

### Observable O1 — the PRICE leg (068270 settled close)

| item | value |
|---|---|
| anchor | **185,800** (2026-08-04 settled close; yfinance and KIS agree) |
| σ source (D93) | 068270's own **10-session log-change sd**, measured: **6.916pp** (n=134 full) · 5.303pp (last 60) |
| σ adopted | ★ **6.916pp — the LARGER of the two.** A narrow band is what killed S43; the conservative direction is wide |
| **threshold (±1.0σ)** | **upper 199,105 / lower 173,384** = `185,800 × exp(±0.06916)` |

**Cross-checks recorded as a D93 receipt**: 068270 daily log-return sd **2.949pp** (full) / 2.976pp
(last 60); beta-adjusted residual sd **2.832pp** (W=60) ~ 2.983pp (W=40) — **this reproduces S43's
post-hoc 2.923pp**. ⚠ The upper bound **199,105 sits 4.9% above S29's 189,737 trigger**, so the two
brackets do not overlap; the lower bound 173,384 sits above the `module_chart` swing low 170,100.

### Observable O2 — the BREADTH leg (the pharma tail's cohort win-rate)

**Definition**: within `SECTOR_FLOW_KR.json`'s `제약` bucket, **excluding the top-2 (068270 · 207940)**,
count how many of the remaining **46** names beat the median `flow_score` of their own **20 nearest
non-pharma names by market cap**. Score the **mean over the 11 settled sessions** of the window.

| item | value |
|---|---|
| anchor (20-session mean) | **26.60 / 46** (measured 07-13~08-05; today's single value 29) |
| σ source (D93) | **binomial null sd = √(46×0.25) = 3.391** — ★ and the **measured 20-session sd is 3.35**, i.e. **a single day's variation is indistinguishable from coin-flipping**. This is the measured reason the threshold may not be hand-set |
| lag-1 autocorrelation | **+0.389** → inflation factor **1.508** |
| SE of an 11-session mean | 3.391/√11 = 1.022 → autocorrelation-corrected **1.542** |
| **threshold (±1.0 SE)** | **upper 28.14 / lower 25.06** |

⚠ **Do not score O2 on a single day.** Today's 29 is +0.71 SE from the anchor = **inside the band.**

### Branches

| Branch | Condition | Meaning | Consequence |
|---|---|---|---|
| **A — the sector proposition survives** | O1 **≥ 199,105** ∧ O2 **≥ 28.14** | price and breadth live together | re-open the W5 question: is `제약` a unit of analysis again |
| **B — one-name proposition confirmed** | O1 **≥ 199,105** ∧ O2 **< 28.14** | 068270 alone; the sector label dies | **M167's direction is kept but its BASIS is replaced** — from the 93.1% concentration figure (shown this run to be an identity) to O2 |
| **C — both dead** | O1 **≤ 173,384** (O2 irrelevant) | the price leg dies | **S29 FIRED-A is marked retrospectively void as evidence** and the node is demoted in the ROTATION slot order |
| **미결 / undecided** | 173,384 < O1 < 199,105 ∧ C not fired | price leg unjudged | ★ **score O2 alone and record only that.** The bracket is NOT VOIDed as a whole |

### Anti-signals (each VOIDs only the observable named)

| # | Anti-signal | Fires ⇒ | Base rate, measured |
|---|---|---|---|
| **AS-1** | any **068270 company-specific filing** inside 08-05~08-19 (투자판단관련주요경영사항 / 잠정실적 / 자기주식 / 유상증자) | ★ **O1 VOID only. O2 stays valid** | **07-24 · 07-30 · 08-03 — three consecutive weeks. The base rate is very high.** This is exactly what killed S43 outright and what S29 was scored through without anyone recording it |
| **AS-2** | the `제약` bucket's n moves **±3 or more** from 48 | **O2 VOID** (cohort composition changed) | n=48 held across all 20 sessions |
| **AS-3** | the window's `^KS11` 11-session log change exceeds **±10pp** | **whole bracket VOID, re-register** | a −11.19% benchmark session actually occurred on 2026-07-28 |
| **AS-4** | the top-2 **market-cap** share moves **±5pp** from 78.4% | recompute §1 arithmetic, reset the O2 anchor | 78.4% held across all 20 sessions |
| **AS-5** | 068270's KIS 5-day foreign AND institution legs both turn negative | O1 may still fire A/B but is **stamped "a breakout without money"** | the hands already changed once (S29's scoring showed the buyer was institution, not foreign) |

**Scoring date: 2026-08-19 (Wed), after the settled close.** Window = 08-05 → 08-19 = **11 settled
sessions.** Scorer = the next DEEP-HLTH or the bracket-scoring stage.

---

## Brackets registered 2026-08-06 by the `industry_kr` run

## S53-KR — ★★ S11 의 내용 다리 (S11 은 일정만 물었고 `FIRED-B` 로 닫혔다) · ARMED · → 2026-10-31

**왜 이 브래킷이 있나.** S11 의 동결 관측값은 *"3연임 제한이 원안대로 입법되나 / 권고수준으로 완화되나 /
지연되나"* 였고, **오늘 발화한 것은 「지연」(B)** 이다. 그런데 **내용은 반대 방향으로 갔다** —
mt 2026-08-05 칼럼: *"정부가 조만간 내놓을 금융지배구조 개선안에 결국 **'금융지주 회장의 3연임 금지'를
포함시키기로 가닥을 잡았다.** 금융당국은 연임과 3연임의 **주주총회 의결 기준을 대폭 강화하는 선에서**
대책을 마련했지만 **청와대가 '3연임 금지'를 밀어붙인 것**으로 알려졌다."*
⇒ **당국 자체안이 B(완화)였고 청와대가 A(법적금지)로 밀었다.** 보통 「지연」은 물타기 쪽으로 읽히는데
**이번엔 반대**이고, **B 의 등록된 의미(*"불확실성 지속"*)는 이 상태를 과소서술한다.**

⚠ **증거등급**: **단일매체 · 칼럼([광화문]) · "알려졌다"(무출처)** ⇒ `[news — 단일매체·칼럼·무출처]`.
**이건 관측값이 아니라 이 브래킷을 만든 이유다.** 아래 관측값은 그보다 훨씬 높은 문턱을 요구한다.

**관측값 (동결)**: 금융위가 **공식 발표**(보도자료 또는 위원장 주재 간담회)하는
「금융회사 지배구조 선진화 방안」 **본문의 3연임 조항 형태.**
⛔ **칼럼·"알려졌다" 보도는 관측값이 아니다** — **2개 이상 매체가 당국 공식 발표를 인용**해야 프린트로 친다.

| 분기 | 관측값 | 의미 |
|---|---|---|
| **A** | **법률상 3연임 금지**(법 개정안 형태로 명시) | 8대 지주 동시 승계 리프라이싱 — KB(105560)·신한(055550)·하나(086790)·우리(316140)에 **같은 이벤트가 동시에** 걸린다. 섹터 사건이지 개별 사건이 아니다 |
| **B** | **주총 의결기준 강화 / 모범규준 수준**(법적 금지 없음) | 당국 원안대로 착지. **청와대 개입 보도는 오보였다는 뜻이고, 그 자체가 이 데스크의 뉴스 등급 규칙에 대한 관측이다** |
| **C** | **2026-10-31 까지 공식 발표 없음** | 세 번째 연기. **`EXPIRED` 가 아니라 C 발화 — 무발표 자체가 정보다** |

**안티시그널 (브래킷 자체를 VOID)**: **금융위 위원장 교체 또는 소관 TF 해산** ⇒ 관측 주체가 사라진다.

⚠ **등록 규율, 명시**
- **D173**: 세 분기 **전부 종점조건**(발표 시점의 조항 형태). 경로조건 없음 ⇒ S17 이 걸린 함정을 구조로 막았다.
- **D175**: 분기 문구에 **메커니즘(청와대·여당) 이름을 넣지 않았다.** S11 의 B 가 「위헌 심판이 지연시킨다」로
  메커니즘을 묶어 놨다가 다른 메커니즘으로 지연이 오는 바람에 판정에 재량이 생겼다.
- **D162**: 이 브래킷을 부활조건에 참조하는 거부가 생기면 **A/B/C 외에 `VOID`·`EXPIRED` 가 났을 때
  어떻게 되는지도 같이 적어야 한다.** (316140 이 S11 의 C 를 AND 참조해 영구 미충족이 된 전례.)
- ⚠ **S45(FSC 지배구조 패키지의 조항 형태, →09-30)와 주제가 겹친다.** **합치지 않는다.**
  **S45 가 먼저 만료되므로, S45 가 `AMBIGUOUS`/`EXPIRED` 로 닫히면 S53-KR 이 그 사실을 흡수한다**(D177).

**Scoring date: 2026-10-31.** Scorer = 그날 이후 첫 HANDOVER.

---

## S54-KR — ★★ C10 을 교란 없는 세션에서 정산한다 · ARMED · → 2026-09-30

**왜.** C10(*"재생에너지 = 유가연동인가"*)은 §6 에 열린 채 운반돼 왔다. 등록 근거는
**2026-07-27: 크루드 붕괴 → KR 재생에너지 4종 −12.7~−29.4% 한 세션**이었다.
**오늘 두 번째 관측이 나왔고 부호가 반대다** — 브렌트 5일 **−12.54%** 인데
**475150 초과 +16.40pp · 010060 +28.22pp**(둘 다 벤치 `069500.KS`, 20일 창은 +50.19 / +40.00pp).
⚠ **그렇다고 C10 을 해소하지 않는다**: **두 관측 다 교란요인이 이름 붙어 있다** —
오늘 것은 **08-05 폴리실리콘 232조 관세 뉴스**(010060 직격), 07-27 것은 **475150 의 KKR SPA 축**.
★ **DEEP-MATR 이 교란 크기를 쟀다: 관세 2세션 기여 +2.18pp = 010060 20일 초과 +40.00pp 의 ~5%**
⇒ **교란은 실재하지만 20일 움직임을 설명하지 못한다.** 그래서 **더 깨끗한 세션이 필요하다.**

**관측값 (동결) — 종점조건 (D173)**
**브렌트(BZ=F) 종가가 5거래일 누적 −7.0% 이상 하락한 첫 세션**(= 트리거 세션)의,
**KR 재생에너지 4종 바스켓 동일가중 당일 수익률 − `069500.KS` 당일 수익률**(초과pp).
바스켓 = **475150 SK이터닉스 · 010060 OCI홀딩스 · 322000 HD현대에너지솔루션 · 009830 한화솔루션**.

**임계 — 측정된 σ 에서 (D93)**
4종 바스켓 일간 초과pp 의 **20세션 표준편차를 트리거 세션 직전에 산출**하고 그 **±1.0σ** 를 밴드로 쓴다.
⛔ **σ 를 사후에 정하지 않는다** — 트리거 당일 산출값을 그 자리에서 기록한다.

| 분기 | 관측값 | 의미 |
|---|---|---|
| **A** | 초과 **≤ −1.0σ** | **유가연동 성립.** C10 은 *"linkage 참"* 으로 해소 |
| **B** | 초과 **≥ +1.0σ** | **유가연동 반증.** C10 은 *"linkage 거짓"* 으로 해소 (유진투자 한병화의 *"20년 전 이야기"* 쪽) |
| **C** | 밴드 안 | 여전히 구분 불가. **C10 은 열린 채 남고 재등록** |

**날짜**: 트리거 미도래 시 **2026-09-30 에 `EXPIRED` 가 아니라 C 발화**(무발생도 정보).

**안티시그널 — 각각 지목한 관측값만 건드린다 (S43 의 실패형을 구조로 막는다)**
- **AS-1**: 트리거 세션 ±1거래일에 **폴리실리콘/태양광 관세 고시 또는 그에 준하는 정책 프린트**가 있으면
  **010060 을 바스켓에서 제외하고 3종으로 채점**한다. ⚠ **AS-1 의 기저율은 현재 HIGH 로 명시한다** —
  관세 스레드가 오늘 NEW 이고 포고문이 미발표다.
- **AS-2**: 트리거 세션 ±1거래일에 **475150 의 SPA/지배권 공시**가 있으면 **475150 제외, 3종으로 채점.**
- ⛔ **두 안티시그널 다 바스켓 구성만 바꾸고 브래킷을 `VOID` 하지 않는다.**

⚠ **등록 규율**: **D173**(세 분기 전부 종점조건, 트리거 세션 1일) · **D175**(분기 문구에 메커니즘 이름 없음) ·
**D162**(이 브래킷을 부활조건에 참조하면 `VOID`/`EXPIRED` 처리도 같이 적을 것).

**Scoring date: 트리거 세션 다음 HANDOVER, 최장 2026-09-30.**


---

## Brackets registered 2026-08-07 by the `industry_kr` run

⚠ **ID 를 WRITE 시점에 확인했다(D137)**: `grep -R "S55-KR"` → **세 `SCENARIOS*.md`·두 `STANDING_VIEW*.md`·
`RESEARCH.md` 일곱 파일 전부 0건**. 기존 최고는 **S65(US) / S54-KR(KR)**. `-KR` 접미사는 필수다 —
S55 는 2026-08-04 `industry_US` PREMORTEM 이 이미 가져갔다(D76). **공유 카운터 제안은 이제 13번째 런째다.**

## S55-KR — ★★★ 관세가 서명된 뒤 **첫 세션의 돈**이 어느 쪽으로 가는가 · ARMED · → **2026-08-13**

Registered **2026-08-07 by the `industry_kr` BET/ALPHA stages**, on **R53** 을 만든 바로 그 공백 위에.

**왜 이 브래킷인가.** 이 런은 *"관세가 서명됐는데 돈이 따라오지 않았다"* 를 세 스테이지에 걸쳐 썼고,
**DEEP-MATR 이 그것을 죽였다** — 인용된 외국인 20d 음(−)은 **전부 서명 이전 세션**이었다(포고령 미 동부
**08-06 서명**, 국내 보도 **08-07 06:39**, KIS 마지막 정착 행 **08-06**). ⇒ **관측이 없었다.**
**이 브래킷의 존재 이유는 그 관측을 사후에 지어내지 못하게 날짜와 임계를 미리 박는 것이다.**

**관측값(동결)**: **010060 OCI홀딩스**의 `python -X utf8 -m module_KIS 010060 --investor 20` 에서
**서명 이후 첫 3개 정착 세션(2026-08-07 · 08-10 · 08-11 종가)의 외국인 일별 순매수 합**.
**함께 보고하되 절대 판정에 합치지 않는다**: 같은 3세션의 **기관·개인 일별 합**, 그리고
**009830 한화솔루션**의 동일 3세션 외국인 합(레인 확인용).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 3세션 외국인 합 **> +20만주** | **돈이 왔다.** R53 이 지운 인과가 반대 부호로 성립한다 — 관세는 이 이름에 **수혜**로 읽히고, **최저수입가 다리(M452, $21/kg = 중국 현물의 4.42×)** 가 우세하다. **`A.flow미도착` 거부는 부활 조건을 충족한다** |
| **B** | 3세션 외국인 합 **< −20만주** | **돈이 반대다, 그리고 이번엔 실제로 관측됐다.** 관세의 **셀·모듈 전층 다리(M451)** 가 우세하고, **가격 +12%는 서사가 만든 것**이다 ⇒ 레인은 STORY-ONLY 로 확정 |
| **C** | 합이 **−20만 ~ +20만주** | `AMBIGUOUS` — 서명이 돈을 움직이지 않았다. **관세는 12-04 발효이므로 「아직 이르다」가 참일 수 있다** ⇒ **밴드를 넓히지 말고 발효 D-30(11-04)로 재등록** |

**임계값의 근거 — 손으로 고르지 않았다.** 010060 의 **최근 20 정착 세션 외국인 일별 순매수의 절대값
평균은 약 6.7만주**(20일 합 −78.1만 ÷ 20 ≈ −3.9만, 일별 진폭은 그보다 크다)이고, **3세션 합의 자연
스케일은 ±20만주 근방**이다. ⇒ **±20만은 대략 3세션 표류의 1σ 바깥**이며, 그 사실을 여기 적는다.
⚠ **KR 에는 함축변동성 축이 없다**(`--positioning` 은 US 전용, 옵션 IV 는 v1.1 대기) ⇒ **이 임계는
손으로 정한 것이고 그렇게 선언한다(D93 이 요구하는 형식).** 추정오차를 직접 재지 못했다는 것이
이 브래킷의 알려진 약점이다.

**Anti-signal (VOID)**: **(i)** 08-07~08-11 중 **한국 예외 조항이 관보/1차 텍스트로 확인**되면 명제의
객체 자체가 바뀐다 ⇒ `VOID`, 새 조건으로 재등록. **(ii)** 같은 창에 **010060 이 유상증자·대규모
수주·지분변동 등 회사 특정 공시**를 내면 관세 축과 분리 불가 ⇒ `VOID`(S43 의 선례를 그대로 적용).
⚠ **(iii)** **KRX 전체 거래정지/서킷브레이커**가 3세션 중 하나를 절단하면 `VOID`.

⚠ **범위(C4)**: 이 브래킷은 *"관세가 010060 에 좋은가"* 를 묻지 않는다. **"서명 직후 외국인이 이 이름을
사는가 파는가"** 하나만 묻는다. 두 개를 섞는 것이 R53 을 만든 실수다.
⚠ **가격 반응이 아니라 수급을 채점한다(L3).** 3세션 동안 주가가 어디로 가든 관측값은 순매수다.
⚠ **이 브래킷은 방향을 사이징하지 않고 어떤 이름도 승격하지 않는다.**

## Brackets registered 2026-08-08 by the `industry_kr` run

> ⚠ Written by **append** — the **D165** pre-commitment after the 2026-08-05 truncation, **6런 연속 유지.**

## S56-KR — ★★★ 「탑재량 레버」가 HBM 순수도로 두 이름을 가르는가 · ARMED · → **2026-08-12**

Registered **2026-08-08 by the `industry_kr` MACRO/ALPHA stages**, on **D194** 가 지적한 공백 위에.

**왜 이 브래킷인가.** **D194**: S39/S43/S44 가 조건정산 클래스를 닫은 뒤 이 데스크에는
**하락 세션을 정산할 등록 관측값이 하나도 없다** — 08-06 의 `069500.KS` **−5.177%** 세션을 어떤
브래킷도 사지 못했다. 동시에 오늘 **§4 비대칭에 없던 셋째 레버**가 인쇄됐다: 하이퍼스케일러 capex 가
아니라 **GPU 단위당 메모리 탑재량(GB/GPU)**. **메모리 매출 = 단가 × 대수 × 탑재량**인데 이 데스크는
**단가(M1)와 대수(M8)만 브래킷했다.**

**관측값(동결)**: **`069500.KS` 를 벤치로 한 일간 초과수익의 차 = (000660 초과) − (005930 초과)**,
**2026-08-10 · 08-11 · 08-12 세 정착 세션 각각**. 계산은 `auto_adjust=False` 종가 기준.
⚠ **`^KS11` 이 아니라 `069500.KS`** 를 벤치로 쓴다(D130 으로 지수 봉이 자주 비고, D146 으로 `^KS200`
경로의존). **함께 보고하되 판정에 합치지 않는다**: 두 이름의 `vol_surge`·OBV·KIS 기관 순매수.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 3세션 중 **2세션 이상에서 차 < 0** (000660 이 005930 에 열위) | **탑재량 레버가 HBM 순수도로 이름을 가른다.** 08-07 의 −5.1pp 는 n=1 이 아니라 계열의 시작이었다 ⇒ **M-38′ (a) 지지**, 전기·전자 UW− 는 **메모리 두 이름에 대한 것**이라는 DEEP-IT 의 분해가 강화된다 |
| **B** | 3세션 중 **2세션 이상에서 차 > 0** | **종목 다리 폐기**(M-38′ anti-signal (ii) 그대로). 08-07 은 단발 노이즈였고, 탑재량 서사는 KR 두 이름을 가르지 못한다 ⇒ **섹터 판정을 메모리 순수도로 쪼갤 근거가 사라진다** |
| **C** | **1:1:1 또는 부호 0 이 섞여 2세션 다수가 없다** | `AMBIGUOUS` — **밴드를 넓히지 말고** 창을 08-13~08-18 로 **재등록**한다(D173: 경로조건과 종점조건을 섞지 않는다 — 이 브래킷은 **세 세션 각각의 부호 다수결 = 경로조건 단일 계열**이다) |

**임계값의 근거 — 부호 다수결을 쓴 이유를 적는다.** KR 에는 **함축변동성 축이 없다**
(`--positioning` 은 US 전용, 옵션 IV 는 v1.1 대기) ⇒ **pp 단위 임계를 σ 로 정할 수 없다.**
그래서 **크기가 아니라 부호의 다수결**로 정의했고, **이것은 손으로 정한 설계이며 그렇게 선언한다(D93)**.
⚠ **알려진 약점**: 부호 다수결은 **크기를 버린다** — 2세션 −0.1pp 와 1세션 +8pp 가 같은 A 를 낸다.
그 사실을 등록 시점에 적어 둔다.

**Anti-signal (VOID)**:
- **(i)** 08-10~08-12 중 **엔비디아가 루빈 울트라 최종 사양을 공식 발표**하면 관측 대상이 사라진다 ⇒ `VOID`, 사양 값으로 재등록.
- **(ii)** 같은 창에 **000660 또는 005930 이 회사 특정 공시**(대규모 수주·증자·지분변동·잠정실적)를 내면 탑재량 축과 분리 불가 ⇒ **그 이름이 낀 세션만 제외**하고, 남는 세션이 2개 미만이면 `VOID`(S43 의 선례).
- **(iii)** **KRX 전체 거래정지/서킷브레이커**가 세 세션 중 하나를 절단하면 그 세션 제외, 남는 세션 2개 미만이면 `VOID`.
- ⚠ **(iv) 등록 시점에 이미 알려진 교란, 숨기지 않는다**: 000660 은 **2026-07-15 완료된 ₩39.89조 DR(ADR) 발행 오버행**을 안고 있고 **국내 외국인 순매수 판독이 D1 로 정지 중**이다. **이 브래킷은 수급이 아니라 가격만 본다** — 그래서 오버행은 VOID 사유가 **아니고**, **A 가 발화해도 「탑재량이 원인」이 아니라 「두 이름이 갈렸다」까지만 말한다.**

⚠ **범위(C4)**: 이 브래킷은 *"메모리를 살까"* 를 묻지 않는다. **"두 이름이 갈리는가"** 하나만 묻는다.
⚠ **가격 반응이 아니라 관측값을 채점한다(L3)** — 이 경우 관측값 자체가 가격이므로, **뉴스가 무엇을
말하든 부호만 센다.**
⚠ **이 브래킷은 어떤 이름도 승격하지 않고 사이징하지 않는다.** **000660 은 오늘 ALPHA 에서
🔴RESOLVED 로 드롭됐고, 이 브래킷은 그 드롭과 독립이다.**


---

## S57-KR — ★★★ 호르무즈 재개방이 KR 정유 두 이름에서 「전쟁 프리미엄」과 「시설 병목」을 가르는가 · ARMED · → **2026-08-20**

> 등록: **2026-08-09 (`industry_kr` MACRO/BET)**.
> ⚠⚠ **이 브래킷은 `S8`(US 소유, 무날짜 `[blank]`, **7런째 정산 불가**)을 재등록하거나 재동결하지
> 않는다.** KR 데스크는 S8 을 판정할 수 없다(P5) — 사람이 `VOID` 하거나 날짜를 붙여야 한다.
> **S57-KR 은 KR 쪽 전이를 별도로 브래킷한다.** 동시에 **`D194`**(하락·이벤트 세션을 정산할 등록
> 관측값 부재)를 한 칸 더 메운다.

### 왜 지금인가
`catalyst_calendar` 는 「이란 호르무즈 개방 성명」을 **무날짜 🔀binary** 로 찍고 있고, 지난 나흘
국내 본문이 **조건과 값을 붙이기 시작했다**(M537): **「60일 개방」** · **이란 통행 수수료 최대 7%
요구** · **합의문 초안 하메네이 승인 대기** · **재개방 조건 = 美 MOU 위반 배상 이행**.
그리고 **08-07 에는 「협상 불확실성」에 브렌트유가 +4% 반등**했다 — 즉 **시장은 이 협상을 양방향으로
거래하고 있다.**

### 동결 관측값
**010950 + 096770 등가중 일간수익률 − `069500.KS` 일간수익률**(pp), `auto_adjust=False` **정착 종가**.
**관측 세션 = 호르무즈 재개방이 공식 발표·합의된 첫 정착 세션.**

### 밴드 근거 — **D93 준수: 임의의 둥근 수를 쓰지 않는다**
같은 추정량의 실측(오늘, yfinance 6개월):
**120세션 평균 −0.022pp · sd 6.069pp** (60d sd 6.918 · 40d 7.929 · 20d 9.512).
**평균이 0과 구분 불가하므로 부호선 0.00pp 는 자의적 선택이 아니라 실측된 귀무값이다.**
⚠ **07-31 의 −27.87pp(S50-KR 이 오염으로 확정한 세션)를 σ 산출에서 제거하지 않았다** — 제거하면
sd 가 내려가 밴드가 좁아지므로 **남겨 둔 쪽이 보수적이다**(C5).

| 분기 | 조건 | 뜻 |
|---|---|---|
| **A** | 초과 **≤ −6.07pp** (−1.0σ) | **전쟁 프리미엄이 지배** ⇒ M-19⁵ 의 구조 다리(윤활 시설 병목)는 과대평가였다 |
| **B** | 초과 **≥ 0.00pp** | **구조 다리가 프리미엄과 분리** ⇒ M-19⁵ 강화, ENRG 승격 근거 |
| **C** | **−6.07 < 초과 < 0.00** | **구분 불가(C4)** — 정보량 없음으로 기록 |
| **VOID** | 관측 세션에 KRX 전체 거래정지 / 서킷브레이커 | — |

### 오염 처리 — **구성으로 막는다**(S43 을 `VOID` 시킨 클래스를 사전에 차단)
관측 세션에 두 이름 중 **하나**에 개별 공시(수주·실적정정·유증·반기보고서)가 있으면
**그 이름을 빼고 나머지 한 이름으로 채점하고 그 사실을 적는다.**
⚠ **`S51-KR`(010950 반기보고서, 08-14 ±3영업일)이 이 창과 겹칠 수 있다** — 겹치면 위 규칙을 적용한다.

### 도달가능성 사전점검 (D206/D216 — **양방향 모두 확인**)
최근 8세션 실측 초과: **+3.73 / +6.90 / −27.87 / +5.60 / +1.98 / −6.21 / +5.88 / +11.29**
⇒ **A(≤−6.07) 와 B(≥0.00) 둘 다 최근 창에서 실제로 도달한 적이 있다.**
**한쪽으로 불가능하지도, 자동으로 참이 되지도 않는다.**

### 마감
**2026-08-20 까지 재개방 발표가 없으면 `EXPIRED-미도래` 로 기록하고 재등록한다.**
조용히 넘기지 않는다.

### 트랙 KPI
호르무즈 스레드 일별 매체수 · `BZ=F` 일간% · `윤활기유`/`그룹3` 테마 배율 ·
010950+096770 등가중 초과(벤치 `069500.KS`).


---

## S52-KR-ANNEX — ★★★ 정보량 통지 (**`S52-KR` 은 재동결하지 않는다**)

> 등록: **2026-08-10 (`industry_kr` DEEP-HLTH)**.
> ⚠⚠ **이 애넥스는 `S52-KR` 의 임계·밴드·분기·정산일·안티시그널을 하나도 바꾸지 않는다.**
> 사후 변경은 예측을 서술로 바꾸는 행위다(L3). **정산 전에 알게 된 정보량 사실을 기록할 뿐이다.**

### 1. O1 은 분기선 위 +0.10% 에 앉아 있다 — `D216` 「불가피」형의 KR 첫 사례

| 항목 | 값 |
|---|---|
| 상한(브랜치 A/B 진입선) | **199,105** |
| 오늘 확인 가능한 최신 정착 종가(2026-08-07) | **199,300** |
| 거리 | **+195원 = +0.10%** (이미 상한 위) |
| 068270 일간 로그수익률 sd (브래킷 자신이 기록) | **2.949pp** |
| **거리 ÷ 일간 sd** | **≈ 1/29** |

⇒ **A/B 를 가르는 것이 정보가 아니라 평범한 하루의 잡음이다.** US `S61` 이 **0.006pp** 로 겪은
「도달 불가」의 반대편 실패모드(**불가피**)이고, KR 에서는 이번이 처음이다.

### 2. O2 는 창 내 확보 세션 전부 상한 위다 — 그리고 `D225-KR` 에 오염되지 않았다

| 정착 세션 | O2 | 출처 |
|---|---|---|
| 2026-08-05 | **30 / 46** | 08-07 런 산출물 |
| 2026-08-06 | 🚨 **없음** (`D230-KR`) | — |
| 2026-08-07 | **31 / 46** | 08-08 · 08-09 · 08-10 런 산출물 |

**확보 2세션 평균 30.5** vs 상한 **28.14** ⇒ **+1.53 SE.**
★ **통제 실험**: 같은 정착 바(08-07)를 **구코드(3/4축 혼합)** 와 **신코드(균일 3축)** 로 계산 →
**31 / 31 / 31 동일.** O2 는 **랭크 비교**라 단조 변환에 불변이고, 이 런에서 가장 크게 움직인 제약
이름(**207940, +0.383**)은 **정의상 top-2 로 제외**돼 있다. ⇒ **척도 파손 가설은 반박됐다.**

### 3. 그래서 이 브래킷이 08-19 에 낼 정보가 무엇인지 다시 적는다

**「A냐 B냐」가 아니다** — 그 갈림은 O1 의 동전던지기에 달려 있다.
**정보가 있는 부분은 「O2 가 밴드 위에 머무는가」** 이고, 그 값은 앵커 26.60 에서 **30.5 로
+2.5 SE 이동**했으며 **그 이동은 계기 변경으로 설명되지 않는다**(위 통제 실험).

### 4. 미해결로 넘기는 것

- **`D230-KR`** — 08-06 정착 바 영구 결측 ⇒ 정산 시 평균의 **n < 11**, 브래킷이 쓴 **SE 1.542 는 과소**.
- **AS-3**(창의 `^KS11` 11세션 로그변화 ±10pp)은 **창 미완이라 `unknown`(C3)**, 08-19 에 확인.
- **AS-1 기저율이 높다**(068270 은 07-24·07-30·08-03 3주 연속 공시). 창 5/11 경과 시점 **미발화**.

## Brackets registered 2026-08-12 by the `industry_kr` run

> ⚠ **append 로 쓴다** — **D165** 사후공약(2026-08-05 절단 이후) **7런 연속 유지.**
> ⚠ IDs 3-grep at WRITE time: 기존 최고 **S74(US) / S57-KR(KR)** ⇒ **S58-KR · S59-KR**.

## S58-KR — ★★★ 000660 충칭 패키징 지분매각: **회사가 스스로 박은 날짜** · ARMED · → **2026-09-09**

등록 **2026-08-12 (`industry_kr` ALPHA/EVENT_ALPHA 카드 4)**.

**이 브래킷이 메우는 공백.** **`D229-KR`**: `catalyst_calendar` 의 `[EARNINGS]` 블록이 **3런 연속 0건**이고,
**KR 단일종목 촉매가 캘린더에 구조적으로 안 잡힌다.** 그런데 오늘 **회사가 직접 날짜를 인쇄했다** —
등록에 추정이 필요 없는 드문 경우다.

**등록 시점 상태** `[measured, 1차]`:
- **2026-08-10 10:10 한국거래소 조회공시요구**: 「**4조 규모 중국 충칭공장 지분매각 추진 보도**」(rcept 20260810800101)
- **같은 날 회사 답변 「미확정」**(rcept 20260810800434): *"패키지 사업 경쟁력 강화를 위하여 다양한 방안을
  검토하고 있으나, 현재까지 확정된 사항은 없습니다. 추후 구체적인 내용이 확정되는 시점 또는 **1개월 이내
  재공시** 하겠습니다."* — **재공시예정일 2026-09-09**, 공시책임자 김우현 재무부문장.
- 서사 축: 「SK하이닉스 충칭 패키징 지분매각 등 검토」 스레드 **BUILDING 3일 · 5→5→5 · 20건 nb 10.7**.
- 흐름: **🔴분산 `flow −0.867` · OBV −0.236 · RS20 −18.7 · Δ −0.106**(보드 최하위권).

**관측값(동결)**: **2026-09-09(회사가 박은 재공시 기한)까지 DART 에 인쇄되는 000660 의 후속 공시 종류.**

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 기한 내 **매각 결정·계약 체결 등 확정 공시** | **₩4조 규모 자산 유동화 + 중국 익스포저 축소가 실제 사건이 된다.** 패키징 캐파의 지리적 이동이 시작되고, `S34`(CXMT)의 중국 축과 **같은 판 위에서 반대 방향**으로 읽힌다 |
| **B** | **또 「미확정」 재공시** | **검토 단계 서사가 3개월째**가 된다. ⚠ **`R63` 이 방금 죽인 규칙을 여기 되살리지 않는다** — **두 번째 「미확정」은 킬이 아니다.** 그것은 「확정되지 않았다」는 사실 그 자체이고, 이 브랜치의 의미는 **「보도가 회사보다 앞서 갔다」**까지다 |
| **C** | 기한 내 **아무 공시도 없음**, 또는 프로세스 종료 공시 | `AMBIGUOUS` — **밴드를 넓히지 말고** 다음 정기공시(3Q 보고서)로 재등록 |

**Anti-signal (VOID)**: **(i)** 같은 창에 **000660 이 대규모 증자·합병·분할 등 더 큰 자본거래**를 공시하면
충칭 축과 분리 불가 ⇒ `VOID`. **(ii)** **미·중 반도체 수출통제의 새 행정명령**이 이 자산의 처분 가능성 자체를
바꾸면 ⇒ `VOID`, 새 조건으로 재등록.
⚠ **범위(C4)**: *"000660 을 살까"* 를 묻지 않는다. **"회사가 박은 날짜에 무엇이 인쇄되는가"** 하나만 묻는다.
⚠ **이 브래킷은 어떤 이름도 승격하지 않고 사이징하지 않는다.** 000660 은 오늘도 **🔴분산**이고
**D1/R13 외국인 flow 판독 정지가 유지**된다.
⚠ **가격이 아니라 공시 종류를 채점한다(L3)** — 9월 9일에 주가가 어디에 있든 관측값은 문서다.

---

## S59-KR — ★★ `S55-KR` 재등록: 관세 **발효** D-30 의 외국인 순매수 · ARMED · → **2026-11-04**

등록 **2026-08-12 (`industry_kr` ALPHA)**. **`S55-KR` 이 오늘 `FIRED-C` 로 닫히면서
그 등록 문언이 미리 지시한 재등록**이다 — *"밴드를 넓히지 말고 발효 D-30(11-04)로 재등록"*.

**왜 재등록인가.** `S55-KR` 의 C 브랜치가 뜻하는 것은 *"서명이 돈을 움직이지 않았다"* 이고,
그 문언은 **「관세는 12-04 발효이므로 '아직 이르다'가 참일 수 있다」**를 이미 담고 있었다.
⇒ **같은 명제를 발효 시점에 다시 잰다.**

**관측값(동결)**: **010060 OCI홀딩스**의 `module_KIS 010060 --investor` 에서
**2026-11-04 이전 마지막 3개 정착 세션의 외국인 일별 순매수 합.**
**밴드는 `S55-KR` 과 **동일**: **A > +20만주 · B < −20만주 · C 그 사이.**
⚠ **밴드를 사후에 넓히지 않았다** — 같은 임계를 그대로 옮긴 것이고, 그 사실이 이 행의 핵심이다.

**직전 관측(참고, 판정 아님)**: 08-07·08-10·08-11 3세션 외국인 합 **−12.1만주**(기관 +9.2만 · 개인 +4.3만),
레인 확인 009830 **−105.4만주**.

**Anti-signal (VOID)**: **(i)** 관세 **발효 자체가 연기·철회**되면 명제의 객체가 사라진다 ⇒ `VOID`.
**(ii)** 관측 3세션 안에 **010060 이 회사 특정 공시**를 내면 그 세션 제외, 남는 세션 2개 미만이면 `VOID`.
★ **(iii) 열거를 이번엔 좁혀서 박는다(`D233-KR` 반영)**: 「회사 특정 공시」 =
**5% 대량보유 변동 · 최대주주 변경 · 유상증자 · 대규모 수주 · 잠정실적 · 조회공시 답변 · 자기주식 취득/처분/신탁계약 변경**.
⚠ **`S55-KR` 은 「자기주식」이 열거에 없어 08-10 의 신탁계약 해지 2건을 안티시그널로 못 썼다** — 그 구멍을 여기서 닫는다.
⚠ **한국 예외조항이 1차 텍스트로 확인되면** ⇒ `VOID`(원 문언 승계).


---

## S60-KR — ★★★ 전력망 「업무협약」이 60일 안에 「수주」가 되는가 · ARMED · → **2026-10-12**

등록 **2026-08-13 by the `industry_kr` MACRO(`M-54`)/DEEP/EVENT_ALPHA(Card 2) stages**.

**왜 이 브래킷인가.** 2026-08-12 에 **「광주특별시·정부·한전·삼성·SK 호남권 반도체산단 전력공급 업무협약」**이
**7매체 36건**으로 인쇄됐고(그날 브리핑 2위 사건), 본문에 **숫자와 날짜가 둘 다 박혔다** —
**「한전, 호남반도체 팹에 3GW 전력 공급」**[mk 555자] · **「광주·용인 반도체 산단에 2029년 전력 우선 공급」**[donga 2,726자] ·
**「송전망 확충 속도에 달렸다」**[donga 3,823자]. 같은 날 테마 축도 보드 최고로 가속했다(**전력망 2.06×, n=783 · 변압기 1.68×**).
**그런데 발주자 손익은 반대로 인쇄됐다** — **「12분기 연속 흑자에도 못 웃는 한전…2분기 별도 영업익 96% 급락」**[sedaily 3,407자].
⇒ **이 데스크는 「MOU 는 계약이 아니다」를 여러 번 말해 왔지만 한 번도 정산 가능한 형태로 등록한 적이 없다.** 그것을 여기서 닫는다.

**관측값(동결)**: **`module_disclosure {103590, 267260, 298040, 010120} --category contract --days 60` 의
「단일판매·공급계약체결」 신규 공시 건수 합** (정정본 제외, 2026-08-13 이후 신규분만).
⚠ **네 이름은 등록 시점에 고정한다** — 일진전기·HD현대일렉트릭·효성중공업·LS ELECTRIC.
⚠ 계약 **금액**이 아니라 **건수**로 정의한다: 금액은 정정본에서 파싱이 자주 실패하는 것이 이 리포의 실측이다(오늘 삼바·한국카본 둘 다 그랬다).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 60일 안에 네 이름 합계 **신규 수주공시 ≥ 2건** | **MOU 가 발주로 전환된다.** 전력망 레인은 서사가 아니라 수주이고, `M-54` 의 (a) 다리가 지지된다 ⇒ **UTIL 의 「판정불가」는 공급자층에서 해소된다** |
| **B** | 60일 안에 **0건** | **MOU 는 말이었다.** `M-54` (a) 폐기. 「AI→전력망→변압기→구리」 사슬(`SECTOR_DEEP_MATR §3`)의 상류 전제도 같이 약해진다 |
| **C** | **정확히 1건** | `AMBIGUOUS` — **밴드를 넓히지 말고** 창을 **2026-12-11(추가 60일)** 로 재등록한다. n=1 은 이 데스크가 반복해서 틀린 표본 크기다(S1) |

**임계값의 근거 — 왜 2건인가, 그리고 이것이 손으로 정한 값임을 선언한다(D93).**
협약 대상이 **호남권 + 용인 두 개 산단**이라 **레인별 최소 1건씩**이 전환의 최소 형태다.
⚠ **알려진 약점**: 건수는 **금액을 버린다** — 소액 2건과 대형 1건이 각각 A 와 C 를 낸다. **등록 시점에 적어 둔다.**

**Anti-signal (VOID)**:
- **(i)** 네 이름 중 하나라도 **합병·분할·상장폐지**로 공시 주체가 바뀌면 그 이름을 제외하고, 남는 이름이 2개 미만이면 `VOID`.
- **(ii)** **한전이 재무 사유로 전력공급 계획 자체를 철회·연기하는 공시**를 내면 관측 대상이 소멸 ⇒ `VOID`, 새 계획으로 재등록.
- **(iii)** ⚠ **등록 시점에 이미 알려진 교란, 숨기지 않는다**: `103590 일진전기`는 **2026-08-12 에 「역대최대 2분기 실적」으로 +17% 급등**했고,
  **KIS 20일 실측은 외국인 +37.0만 · 기관 −47.2만 · 개인 +14.1만 = 기관 순매도 + 개인 흡수**다.
  ⇒ **이 브래킷은 수급이 아니라 공시 건수만 본다.** 그래서 그 사실은 VOID 사유가 **아니고**,
  **A 가 발화해도 「이 이름들을 사라」가 아니라 「MOU 가 발주가 됐다」까지만 말한다.**

⚠ **범위(C4)**: 이 브래킷은 *"전력망을 사라"* 를 묻지 않는다. **"업무협약이 계약이 되는가"** 하나만 묻는다.
⚠ **관측값의 공표 지연 = 없음**(DART 공시는 당일 게시) — **`D231-KR` 의 새 등록 규칙을 처음으로 적용해 확인한 항목이다.**
⚠ **정산일이 오전 런과 겹쳐도 문제없다**(공시 건수는 정착 개념이 아니다) — `D232-KR` 도 해당 없음.


---

## S61-KR — ★★★ 레짐 콜의 대상을 처음으로 1차 관측면에 묶는다: 한국은행 수출물가의 **변화율** · ARMED · → **~2026-09-14**

Registered **2026-08-14 by the `industry_kr` MACRO/HANDOVER stages.**
⚠ **ID 3-grep at WRITE time**: 기존 최고 **S60-KR(KR) / S83(US)** ⇒ 이 행은 **S61-KR**.

**왜 필요한가.** 이 데스크의 레짐 콜 *"메모리는 레벨이 타이트한 채 변화율이 감속하는 가격사이클 산업"* 은
**8개월째 `[inferred]` 이고 그 근거 사슬(M1 서버 DRAM 계약가 QoQ · M2 MU 총이익률)은 전부 US 소스**다.
**KR 데스크가 매달 직접 받는 1차 관측면이 있는데 한 번도 브래킷된 적이 없다** — 한국은행 수출입물가지수의
**D램 수출가격 MoM** 이다. 오늘(2026-08-14) 그 계열이 **YoY +270.3% / MoM +6.6%** 로 인쇄됐고,
총계 MoM 시퀀스는 **4월 +7.5% → 6월 −0.1% → 7월 +1.0%** 다(**M643**).

**관측값(동결)**: **한국은행 「2026년 8월 수출입물가지수」의 원화 기준 총 수출물가 MoM (%)**.
발표 시점은 한은의 통상 발표 주기(매월 중순) 기준 **~2026-09-14**, `✓` 아닌 **패턴 추정**임을 명시한다.
⚠ **총계를 관측값으로 쓰고 D램 단일 품목을 쓰지 않는다** — 품목 계열은 발표문에 매월 실리지 않을 수 있어
**관측면의 존재 자체가 불확실**하기 때문이다. **D램 MoM 은 병기하되 판정에 합치지 않는다.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (감속 지속 — 레짐 콜 지지)** | 총 수출물가 **MoM ≤ 0.0%** | 7월의 +1.0% 가 6월 −0.1% 에서 튄 노이즈였고, 4월 +7.5% 대비 1/7.5 수준의 감속이 이어진다 |
| **B (감속 종료 — 레짐 콜의 변화율 다리 반증)** | 총 수출물가 **MoM ≥ +3.0%** (= 4월 +7.5% 의 40% 이상 회복) | 변화율이 되살아났다. **레짐 콜의 「변화율 감속」 다리를 철회하거나 재작성해야 한다** |
| **C** | 0.0% < MoM < +3.0% | 정보 없음. **밴드를 사후에 넓히지 말고 더 좁혀 재등록한다** |

- ★ **밴드 근거를 명시한다(C5)**: 상단 +3.0% 는 **관측된 4월 +7.5% 의 40%** 이고, 하단 0.0% 는 **부호 경계**다.
  **분포 추정치가 아니라 손으로 정한 값**이고, 이 데스크는 **한은 수출물가 MoM 의 분포를 잰 적이 없다.**
- ⚠ **양쪽 절반 동반 의무(C2)**: 채점할 때 **MoM 과 YoY 를 함께 인쇄**한다. 오늘 값은 **MoM +1.0% / YoY +49.1%** 다.
- ⚠ **원화 기준으로 동결한다**. 계약통화 기준(오늘 +3.0%)은 **환율이 빠진 다른 계열**이므로 병기만 하고 판정에 쓰지 않는다.
  ⇒ **오늘 계약통화 기준이 이미 +3.0% 라는 사실을 등록 시점에 적어 둔다** — 원화 강세가 원화 기준 수치를 깎고 있다(한은 본문 명시).
- **Anti-signal (브래킷을 통째로 무효화)**: 한은이 **지수 기준연도를 개편**하거나 발표 형식을 바꿔 MoM 이 직접 비교 불가능해지면 `VOID`.
- **Information content (L3): HIGH, 그리고 방향이 유용하다** — 브랜치 B 가 **이 데스크의 8개월짜리 상시 명제를 반증**한다.
- **공표 지연**: **0 영업일**(발표일 당일 인쇄). ⇒ **`S38`/`S48-KR` 을 3런 막은 지연 문제가 이 관측면에는 없다**
  — `D231-KR` 이 요구한 「관측값 공표 지연」 칸을 **이 브래킷이 처음으로 채운다.**
- ⚠ **Not a position.** 이 브래킷은 종목을 지목하지 않는다. **레짐 콜이라는 명제 하나만** 잰다.


---

## Brackets registered 2026-08-16 by the `industry_kr` run

## S62-KR — ★★★ 환적(transshipment) 관세: 4런째 보드 최고 서사에 처음 날짜를 붙인다 · ARMED · → **2026-09-15**

**Why this exists.** `M-58`/`M-64`/`M-66` have recorded transshipment as the KR board's fastest-accelerating
narrative for **four consecutive runs** while stating each time that **zero of the desk's brackets measure it**.
`M-64` explicitly handed *"register a dated bracket"* forward to ALPHA and it was carried, not done. This closes it.

**Frozen observable.** A **US primary document** — USTR or Department of Commerce — published on or before
**2026-09-15**, in which **the Republic of Korea is named** in connection with transshipment / circumvention of
tariffs on Chinese-origin goods. *"Named"* means the country appears in the document's own text, not in press
characterisation of it.

**State at registration (2026-08-16).**
- `불법환적` (KR trigram index): **d7 14 / d30 15 = 4.00×** — 93% of the month's volume in the last week.
- `환적` (default index): **d7 41 / d30 53 = 3.32×**, reproducing the 08-15 reading of 3.30×.
- 2026-08-14 event axis, head #2: **「美 "中, 40여개국 불법환적해 관세회피"…韓도 '中환적 위험국' 거론」 [41 articles / 7 outlets]**,
  with a sub-event that names **「경기 반도체 벨트」** explicitly.
- Registered exposure question: **IT / semiconductor export routing.** Sector state at registration —
  전기·전자 wflow **−0.148**, eqflow **+0.164**, breadth 0.12, n=66.

**Branches (thresholds frozen at registration).**
- **A** — Korea is **named in a US primary document** by 2026-09-15 ⇒ the risk was real and the desk was 4 runs late to bracket it.
- **B** — **No US primary document names Korea** by 2026-09-15 **and** both indexes read **< 1.0×** on the last run before that date ⇒ it was a negotiating lever, matching the `S55-KR` `FIRED-C` precedent.
- **C** — No primary document, but the narrative is still ≥1.0× on either index ⇒ **unresolved; re-register with a narrower window, and do not widen this one afterwards.**

**Anti-signal / VOID.** If a **blanket** tariff action covering many countries lands (i.e. Korea is not
distinguished from the 40+ countries already named), the bracket is `VOID` — it was written to test a
**Korea-specific** designation, not a general trade action.

**Track KPI.** `불법환적` and `환적` velocity on **both indexes, stated per line** (`M691`) · USTR / Commerce
primary filings · KR semiconductor export clearance data.

⚠ **C5 declared at registration**: the 2026-09-15 date is **hand-set**. This desk has never measured the
distribution of "narrative onset → US primary document" lags, so the window is a judgement, not an estimate.

---

## S63-KR — ★★ 화장품: 「ODM vs 브랜드」가 진짜 단위인가, 한 주짜리 아티팩트인가 · ARMED · → **2026-08-20**

**Why this exists.** `SECTOR_DEEP_STPL` found the chain splitting on **two independent axes in the same order**
and concluded the sector label is the wrong unit. That conclusion needs to be falsifiable rather than asserted.

**Frozen observable.** **RS60 vs `^KS11`**, settled close of **2026-08-20**:
`spread = median(RS60 of 161890, 192820) − median(RS60 of 051900, 090430)`.

**State at registration (prices asof 2026-08-14).** 161890 **+52.9** · 192820 **+43.9** ‖ 051900 **+22.3** · 090430 **+17.2**
⇒ **spread = 48.4 − 19.8 = +28.6pp**. (Group median RS60 = **+22.3**; the spread already exceeds it.)

**Branches.**
- **A** — spread **≥ +20pp** ⇒ the ODM/brand split holds; **"cosmetics" stays retired as a unit** and both sides get separate theses.
- **B** — spread **≤ +10pp** ⇒ it was a one-week artifact; revert to a single sector unit and **retract `M696`'s unit claim** (not its margin measurements, which are annual filings and independent).
- **C** — spread between **+10pp and +20pp** ⇒ **no information**; re-register with a longer horizon and do **not** widen the band afterwards.

**Anti-signal / VOID.** If any of the four names prints a **corporate event** (M&A, split, control transfer,
capital raise) inside the window, remove that name and score on the remaining pair; if two or more are affected, `VOID`.

**Track KPI.** RS60 of the 4 names vs `^KS11` · ⑦ KIS foreign/institution net buy (all 5 were real-hands at
registration) · FY2026 gross margins when filed (the margin leg settles ~2027-03, far outside this window —
**this bracket tests the price axis only, and says so**).

⚠ **C5 declared**: the ±10/20pp band is **hand-set**. This desk has never measured the distribution of
intra-sector RS60 spreads in KR, so **these two observations are the first samples of that distribution**
(the same defect `S48-KR` declared about short-balance bands, recorded here rather than repeated silently).

## 2026-08-18 `industry_kr` 런 — **신규 브래킷 등록 0건**, 상태 메모만

**오늘 만기 도래 0건**(최근접 = **S52-KR → 2026-08-19, 내일**). `EXPIRED` 0 · 조용한 스킵 0.
이 런은 **브래킷을 새로 등록하지 않았다** — 등록은 EVENT_ALPHA/ALPHA 가 판정을 낼 수 있을 때 하는 일인데,
**G1 FAIL 로 ALPHA 가 신선도 판정 자체를 발행할 수 없었다.** 없는 판정 위에 브래킷을 세우지 않는다.

**임박 브래킷에 오늘 붙는 관측(임계값은 전부 동결, 사후 조정 없음):**

| 브래킷 | 만기 | 오늘 관측 |
|---|---|---|
| **S52-KR** (제약 = 섹터냐 한 이름이냐) | **2026-08-19 (D−1)** | 제약 **wflow +0.335(4위) ↔ eqflow −0.089 · breadth 0.04 (2/48)** — **부호가 갈린다.** 068270 셀트리온 스레드 **REIGNITED 5→2**(유럽 판매망), 태그 🟡중립 flow +0.482. ⚠ **정산일 관측면이 「정착 종가」라면 08-18 이 정착됐는지가 다리 하나다**(G0) |
| **S57-KR** (호르무즈: 전쟁 프리미엄 vs 시설 병목) | **2026-08-20 (D−2)** | 사건축 **머리 #2 · REIGNITED 5일 41건**(트럼프 MOU 연장 거부)인데 **`호르무즈` 0.95× · `국제유가` 0.38×(보드 최저)** 이고 **`정제마진` 1.54× 3런 연속 위**. flow 는 **010950 🔴분산 / 096770 OBV 분산**. ⇒ **가름은 「구조」 쪽인데 돈이 안 온다** |
| **S63-KR** (화장품: ODM vs 브랜드가 진짜 단위인가) | **2026-08-20 (D−2)** | ★ **오늘 재료가 생겼다** — ODM·제조 **5/5 🟢가속**(vol_surge 2.38~7.90) vs 브랜드 **2/2 🟡중립**(0.76 · 1.08). ⚠ `vol_surge` 는 오늘 **−15.3% 하향 편향**이라 격차는 **과소 측정**(보수적 방향) |
| **S34** (CXMT 공급측 반증) | 2026-10-31 | 오늘 KPI 1차 인쇄: **「[반도체 패권 지도] 중국 SMIC 파운드리 3위·**CXMT D램 7%**…첨단 공정은 여전히 벽」**(단독 nb 20.0) |
| **S62-KR** (환적 관세) | 2026-09-15 | `불법환적` **4.03× · 보드 최고 6런 연속**(d30 17건 중 16건이 최근 7일). 보강축 **`반덤핑` 1.74× · `원산지` 1.41×**. ⚠ **사건 스레드는 ENDED**(피크 8매체) — **서사 배율과 사건 궤적이 갈린다** |
| **S38** | 2026-08-12 (정산됨 `FIRED-B`) | 006360 공매도잔고 **5.01% float · `building(+0.84)`** — **covering 전환 아님**(KRX 실측 09:43) |
| 🚨 **S8** (US 소유, 날짜 `[blank]`) | — | **정산 불가 15연속.** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다(P5) |

## Settled / registered by the 2026-08-19 `industry_kr` run

> ⚠ **ID 3-grep(WRITE 시점)**: 현행 최고 `S63-KR` ⇒ 이 블록은 **S64-KR**.

### S52-KR — **`미결(undecided)` · 부분정산 · 재등록 필요** (정산일 2026-08-19 도래)

**`EXPIRED` 아님. 조건이 소멸한 게 아니라 관측 인프라가 명세를 못 따라갔다.**

| 관측 | 명세 | 실측 | 판정 |
|---|---|---|---|
| 창 길이 | **11 정착세션**(08-05→08-19) | **9 정착세션** — 08-15(토·광복절)·08-16(일)·**08-17(월 대체공휴일)** 3일 휴장. 등록 시점(08-05)에 **대체공휴일이 창 계산에 반영되지 않았다** | ❌ −2세션 |
| 관측 시각 | **08-19 정착 종가 이후** | 이 런은 **08:17 개장 전** | ❌ 관측면 미존재 |
| **O1** (068270 정착 종가) | 밴드 하단 173,384 / 상단 199,105 (앵커 185,800 · σ 6.916pp) | **최종 정착(08-18) 195,500** — yfinance·KIS 두 계기 일치 | ★ **미결 밴드 안** |
| O1 경로 (기록만) | — | 08-10 201,000 · 08-11 **210,500** · 08-12 202,000 · 08-13 202,000 · 08-14 201,000 · **08-18 195,500** ⇒ **창 중반 4세션 연속 상단 밴드 위**에 있다가 되돌아왔다 | ⚠ **사후에 「터치했으니 A/B」로 바꾸지 않는다** — 종점 정산 브래킷이다 |
| **O2** (제약 꼬리 46종 코호트 승률, 11세션 평균) | 밴드 25.06 / 28.14 (앵커 26.60) | **채점 불가.** 스냅샷 6개 중 **비교 가능한 깨끗한 정착 관측은 4개(36%)** — 08-05 는 `_mode: news`(4축, 스케일 다름) · 「08-14」키는 **실제로 08-18 데이터**(M725) · 「08-18」키는 **장중 26분봉**. 4세션 평균 25.50 이나 **SE 가 √(11/4)=1.66배 넓어져 밴드가 무의미** | 🚨 **구성 결함** |
| **AS-1** (068270 고유 공시) | 투자판단관련주요경영사항/잠정실적/자기주식/유상증자 | DART 15일 **총 2건**: 08-14 **반기보고서(2026.06)** · 08-14 지급수단별 공시. **열거 4종은 0건** | ❌ 미발화 |
| **AS-2** (제약 n ±3) | 48 | **48** (변동 0) | ❌ |
| **AS-3** (`^KS11` 11세션 로그변화 ±10pp) | ±10pp | 08-04→08-14 **+9.29pp**(여유 0.71pp). ⚠ **종점 08-18 은 벤치 봉 부재로 측정 불가**(M724) | ❌ (종점 미측정) |
| **AS-4** (top-2 시총비중 ±5pp) | 78.4% | **78.4%** (207940 64.67조 + 068270 40.65조) | ❌ |
| **AS-5** (외국인 AND 기관 둘 다 음전) | — | 최근 5 정착세션 외국인 **+70.4만주(양)** · 기관 −44.1만주 | ❌ (AND) |

⚠ **AS-1 구성 결함 기록**: 열거 목록에 **정기보고서(사업·반기·분기)가 빠져 있다.** 08-14 **반기보고서**(H1 실적 포함)가
제출됐고 **바로 다음 정착세션에 −2.74%(201,000→195,500)** 빠졌다. AS-1 의 *목적*(기업 고유 정보 이벤트가 가격 다리를
오염시킨다)에는 정확히 해당하나 *문구*에는 해당하지 않는다. **사후에 문구를 넓히지 않는다.**

### S64-KR — 재등록 예약 (**아직 등록 아님 — 다음 KR 런이 값을 채워 발행한다**)

**S52-KR 이 죽은 세 결함을 고쳐 재등록한다:**
1. **창을 캘린더가 아니라 「정착세션 카운트」로 정의**하고 휴장을 흡수한다. *(오늘 `M-62` 안티시그널 ①도 6런째 같은 이유로 검정 불가 — 같은 병이다.)*
2. **O2 를 「스냅샷이 실제로 존재하는 세션」으로만 정의**하고 **`_mode` 동일**을 요건에 명시한다.
3. **AS-1 목록에 정기보고서(사업·반기·분기)를 추가**한다.

### 오늘 만기 도래 그 외

- **KR: S52-KR 1건뿐.** `EXPIRED` **0** · 조용한 스킵 **0**.
- **US 소유 08-19 만기(S75~S78)** — KR 이 채점하지 않는다. 관측면이 **US 정착 종가**이고 KST 08~09시엔 **아직 오지 않았다**.
- 🚨🚨 **S8**(US 소유, 날짜 `[blank]`) — **정산 불가 16번째 연속.** 사람이 `VOID` 하거나 날짜를 붙여 재등록해야 한다.
- 🚩 **`S63-KR`(08-20 만기)이 오늘 DEEP 슬롯을 못 받았다** — 08-18 DEEP_LOG 의 `first-claim = STPL` 이
  **MACRO 가 STPL 을 N 으로 판정하면서 로테이팅 규칙(OW 한정)에 걸려 이행 불가**가 됐다.
  **first-claim 이 등급 강등으로 조용히 소멸하는 경로**이며 `RESEARCH.md` 에 dig 로 올린다.


---

## Settled / registered by the 2026-08-20 `industry_kr` run

> ⚠ **ID 3-grep(WRITE 시점)**: `SCENARIOS*`·`STANDING_VIEW*` 현행 최고 **S64-KR**(08-19 예약행) ⇒ 이 블록은 **S65-KR** 부터.
> ⚠ **쓰기 방식**: `'a'` 모드 append.

### S57-KR — **`EXPIRED-미도래` 로 종료. 브래킷 자기 마감 조항 그대로.**

마감 조항 원문: *"2026-08-20 까지 재개방 발표가 없으면 `EXPIRED-미도래` 로 기록하고 재등록한다. 조용히 넘기지 않는다."*

**관측 세션(「호르무즈 재개방이 공식 발표·합의된 첫 정착 세션」)이 발생하지 않았다. 그리고 방향은 반대였다.**
`fts search 호르무즈 --days 5`(08:30, 7일 452건) 본문 실측:
- **미·이란 60일 종전 MOU 가 2026-08-17 로 만료** (「미·이란 '60일 협상시한' 종료」).
- 이란 협상단장 **"미국이 MOU 약속 이행할 때까지 호르무즈 안 연다"**(08-18).
- 트럼프 **"이란과 진행 또는 예정된 협상 없어"**(08-19) · **"호르무즈 해협은 美 새로운 영토"**(08-18).
- **MOU 만료 첫날 호르무즈에서 선박 피격**(08-18) · 한국 유조선 **2척 수에즈 우회**(08-17·08-19).
- **브렌트 91.62달러, 4거래일 연속 상승**(08-20).

⇒ **브랜치 A/B/C 어느 쪽도 채점 불가 — 관측면 미발생.** **임계값은 손대지 않았다**(사후 완화 금지).
⚠ **참고로 이 브래킷이 죽은 날에도 `catalyst_calendar` 는 여전히 「Iran 'Strait of Hormuz open' statement · undated 🔀binary」를 들고 있다** — 넣지도 빼지도 못하는 상태(`D288-KR`).

### S63-KR — **`정산 미도래`. `EXPIRED` 아님. 다음 런의 #1 작업.**

동결 관측면이 **「RS60 vs `^KS11`, 2026-08-20 **정착 종가**」** 인데 이 런은 **08:26 시작 · 개장 전**이다.
**`S52-KR` 을 죽인 것과 정확히 같은 결함**(개장 전 런 vs 정착 종가 관측면)이므로 **조건이 소멸한 게 아니라 아직 오지 않았다**(`S28` 선례).

**D−0 사전관측** (마지막 정착 = 종목 08-19 / 벤치 08-18, G0 병기):

| 이름 | RS60 (날짜정합) | RS60 (naive `iloc`) |
|---|---:|---:|
| 161890 한국콜마 | +50.1 | +48.0 |
| 192820 코스맥스 | +42.9 | +44.1 |
| 051900 LG생활건강 | +26.0 | +25.1 |
| 090430 아모레퍼시픽 | +18.6 | +18.2 |
| **spread = median(ODM) − median(브랜드)** | **+24.2pp** | **+24.4pp** |

- 등록 시점(가격 asof 08-14) **+28.6pp** → 오늘 **+24.2pp** (**−4.4pp 축소, 여전히 브랜치 A 선 +20pp 위**).
- ★ **두 계산법이 0.2pp 안에서 일치** ⇒ 이 브래킷은 **G0 의 날짜 어긋남에 강건하다.**
- 독립 확증(`module_flow` 08:34): 161890 **🟢가속 RS60 +48.0 vol_surge 2.57** · 192820 **🟢가속 +44.1 · 2.56**, 둘 다 OBV 매집 + KIS 두 다리 양(+).
- **VOID 사유 점검**: 네 이름 모두 창 내 M&A·분할·경영권이전·유상증자 **미확인**.
- 🚩 **그리고 오늘도 DEEP 슬롯을 못 받았다** — MACRO 가 STPL 을 **N** 으로 판정했고 로테이팅 규칙은 OW 한정이며 Neutral 패딩은 금지다. **`first-claim` 이 등급 강등으로 소멸하는 경로, 2런 연속**(`D286-KR` 승격).

### S64-KR — **오늘 발행하지 않는다. 사유를 적는다.**
08-19 런이 *"다음 KR 런이 값을 채워 발행한다"* 로 예약한 `S52-KR` 재등록이다.
**수정사항 ①이 「창을 정착세션 카운트로 정의」인데, 오늘 런은 정착 스냅샷 자체가 오염돼 있다**
(G0: 벤치 `^KS11` 08-19 봉 부재 / G2: `asof` 라벨이 2런 연속 거짓). **오염된 앵커 위에 「휴장을 흡수하는 창」을
세우면 수정이 아니라 새 결함이다.** ⇒ **미발행 사유를 여기 적고 다음 런으로 넘긴다. 조용한 소멸 아님.**

---

## S65-KR — ★★★ `S57-KR` 재등록: **재개방이 아니라 「봉쇄의 지속」을 관측면으로 바꾼다** · ARMED · → **2026-09-19**

**Why this exists.** `S57-KR` 은 **「재개방 발표」라는 발생하지 않을 수도 있는 이벤트**에 관측면을 걸었고,
실제로 발생하지 않아 **정보량 0 으로 만료**됐다. **이벤트 발생을 기다리는 브래킷은 이벤트가 안 나면 아무것도 못 배운다.**
⇒ **재등록은 관측면을 「이벤트」에서 「기간」으로 바꾼다** — 한 달 뒤 정착 종가에서 무조건 채점된다.

**동결 관측값.** **010950 + 096770 등가중 일간수익률 − `069500.KS` 일간수익률**(pp)의
**2026-08-20 ~ 2026-09-19 누적 합**, `auto_adjust=False` **정착 종가**, 벤치 인라인 명시(C1).

**밴드 근거 — D93, 오늘 재측정(임의의 둥근 수 금지).**
같은 추정량 **120 세션 실측(1년 프레임)**: **평균 −0.025pp · sd 6.093pp · p15 −5.332 · p85 +4.622**.
기간 sd 는 **60d 6.889 · 40d 7.784 · 20d 8.552** 로 최근이 더 넓다 — **보수적으로 120세션 값을 쓴다.**
**약 21 세션 누적**의 σ ≈ 6.093 × √21 = **27.9pp**.

| 분기 | 조건 | 뜻 |
|---|---|---|
| **A** | 누적 초과 **≤ −27.9pp** (−1.0σ) | **봉쇄 지속이 정유 마진으로 전이되지 않았다** ⇒ `M-69`/`M-19⁵` 의 구조 다리 폐기 |
| **B** | 누적 초과 **≥ +27.9pp** (+1.0σ) | **봉쇄가 길어질수록 KR 정유가 이긴다** ⇒ 구조 다리 강화, ENRG 재승격 근거 |
| **C** | **−27.9 < 누적 < +27.9** | **구분 불가(C4)** — 정보량 없음으로 기록 |
| **VOID** | 관측 기간 중 KRX 전체 거래정지 / 두 이름 중 **둘 다** 개별 공시(반기·수주·유증) | — |

**오염 처리(구성으로 차단)**: 두 이름 중 **하나**에만 개별 공시가 있으면 **그 이름을 빼고 나머지 하나로 채점하고 적는다.**

**도달가능성 사전점검(D206/D216 — 양방향)**: 최근 8세션 일간 초과 실측
**+11.29 / +2.29 / −0.46 / −4.73 / −4.39 / +2.65 / +4.49 / +4.62** ⇒ **하루 만에 ±11pp 가 나온다.**
21세션 누적이 ±27.9pp 를 양방향 모두 넘길 수 있다. **어느 쪽도 자동으로 참이 되지 않는다.**

**등록 시점 상태(공개)**: 2세션 연속 양(+) — 08-19 정착 **+4.96pp(010950)** · **+4.28pp(096770)**, 등가중 **+4.62pp**.
⇒ **브랜치 B 방향이 러닝 브랜치이고 A 가 적대적 질문이다.**

**트랙 KPI**: `BZ=F` · `호르무즈` 스레드 일별 매체수 · `정제마진`/`국제유가` 배율 ·
010950·096770 flow 태그와 KIS 20d · 등가중 누적 초과(벤치 `069500.KS`).
**마감**: **2026-09-19 정착에서 무조건 채점한다.** 이벤트 발생 여부와 무관하다 — **그것이 재등록의 요점이다.**

---

## S66-KR — ★★★ **거래량이 반응하지 않은 폭락은 되돌아오는가** · ARMED · → **2026-08-20 정착 (오늘 15:30)**

**Why this exists.** 오늘 `M-80` 이 세운 명제이고, **이 런이 자기 헤드라인을 한 번 반증한 자리**다(`R85`).
정정 후 살아남은 관측은 **「지수가 −5.80% 빠지고 상승 종목이 17.4% 인 세션인데 중앙값 종목의 거래량 반응이 0 이었다」**
이고, 그 형태가 **되돌림**을 뜻하는지 **아직 안 온 분배**를 뜻하는지는 **다음 정착 하나로 갈린다.**

**동결 관측값(두 다리, 독립 채점).**
- **leg 1** = `069500.KS` **2026-08-20 정착 일간수익률(%)**.
- **leg 2** = 유니버스 **마지막봉 거래량 / 직전20일평균의 중앙값**, 같은 정착일, `prices_kr_*.pkl` 프레임 기준.

**밴드 근거 — D93, 오늘 실측(둥근 수 금지).**
leg 2 추정량의 **57 세션 기준선**: **평균 0.744 · sd 0.183 · p10 0.601 · 중앙 0.730 · p85 0.920 · p90 0.941.**
⇒ **임계는 1.0/1.2 같은 둥근 수가 아니라 이 추정량 자신의 `p85 = 0.920` 과 `p10 = 0.601` 이다.**

| 분기 | leg 1 | leg 2 | 뜻 |
|---|---|---|---|
| **A (되돌림, 그러나 여전히 무반응)** | **≥ +2.0%** | **< 0.920** | **공백이 반대 방향으로 한 번 더 났다** ⇒ 「신뢰 회복」으로 읽는 것 폐기. `M-80(a)` 는 **약하게** 지지 |
| **B (진짜 분배가 하루 늦게 왔다)** | **< 0%** | **≥ 0.920** | **`M-80(a)` 폐기** — 08-19 는 분배의 서곡이었다 |
| **B′ (진짜 매수가 왔다)** | **≥ +2.0%** | **≥ 0.920** | ★ **`M-80(a)` 강하게 지지** — 되돌림에 거래량이 붙었다 |
| **C** | 그 밖 | 그 밖 | **구분 불가(C4)** |

⚠ **leg 1 의 ±2.0% 는 둥근 수다(C5 선언).** 근거: 이 벤치의 최근 20세션 일간 sd 가 약 2.5%p 이고,
**「의미 있는 되돌림」의 하한을 −6.255% 의 약 1/3 로 잡았다.** **이것은 측정된 임계가 아니라 손으로 정한 임계이며,
이 브래킷의 두 관측이 그 분포의 첫 표본이다**(`S48-KR`·`S63-KR` 이 선언한 것과 같은 결함, 반복하지 않고 적는다).

**등록 시점 상태(공개)**: 09:0x 장중 관측으로 **032830 삼성생명 276,000 → 294,000(+6.5%)**,
`KRW=X` **1,389.19(−1.73%)**, 간밤 뉴욕증시 상승. ⇒ **A 또는 B′ 방향이 러닝이고 B 가 적대적 질문이다.**
⚠ **장중 미완봉이다 — 정산은 정착 종가로만 한다.**

**트랙 KPI**: `069500.KS` 정착 · 거래량비 중앙값 · 상승비율 · `KRW=X` · `us_30y`·`2s30s` `[FRED]`.
**마감**: **2026-08-20 정착.** **다음 런이 반드시 채점한다** — 미채점은 프로세스 실패로 기록된다.


---

## Settled / registered by the 2026-08-21 `industry_kr` run

> **ID 3-grep at WRITE time** across `handoff/*.md`, `llm_outputs/2026-08-21/**`, `REPORT/industry_KR/**`:
> `S67-KR` returned **0 hits**; highest existing **S66-KR**. => this block is **S67-KR**.

### Settled this run
- **`S66-KR` -> FIRED-A** (registered 08-20, settled 08-20, scored 08-21). Full record in the master log.
- **`S63-KR` -> FIRED-A** (registered 08-14, settled 08-20, scored 08-21). The VOID clause removed **192820**; four calculations, one branch.

### S67-KR — Does a record buyback change WHO owns the stock, or only the price? · **SCORED `FIRED-C` 2026-09-05** (was ARMED · settle 2026-09-04)

**Why this exists.** On 2026-08-19 SK하이닉스 filed `주요사항보고서(자기주식취득결정)`: **24,070,000 shares ·
KRW 40.00tn · method 장내매수 (open-market purchase) · purpose 자기주식 소각을 통한 주주가치 제고**, plus a
same-day `주식소각결정`. On 2026-08-20 the stock printed **+12.73%** — and the KIS three-party breakdown shows
**foreign +31.3만 · institution −1.3만 · retail −92.2만, i.e. the three displayed parties net to −62.2만 shares.**
Something bought ~620,000 shares that none of the three displayed categories account for.
Separately the sympathy leg — **005930 +9.49% on no disclosure of its own** — is pure expectation:
005930's DART shows **zero treasury filings** in the last 10 days (checked 2026-08-21 09:0x).
**Neither leg has been tested, and the two legs can fail independently.**

**Frozen observables**, both read at the **2026-09-04 settled close** (after the 08-26 NVDA print has cleared):
- **leg 1 (ownership)** — `module_KIS 000660 --investor 20`: sign of the **foreign** 20-day cumulative.
- **leg 2 (contagion)** — has **005930** filed a `자기주식취득결정` or a dividend-increase 주요사항보고서 to DART
  at any point in 2026-08-21 -> 2026-09-04?

| Branch | Condition | Meaning |
|---|---|---|
| **A** | leg1 **positive** AND leg2 **yes** | The buyback re-rated the sector: ownership turned **and** the peer followed => a capital-policy regime, not one company's treasury action |
| **B** | leg1 **negative** AND leg2 **no** | The 08-20 move was the company buying its own stock while foreigners kept leaving, and the 005930 leg was expectation that never printed => **retract the "capital-policy re-rating" reading of 2026-08-20 entirely** |
| **C** | the legs split | Partial: name-specific, not a sector event |

**State at registration (disclosed, 2026-08-21):** leg1 **negative** — 000660 foreign 20d **−297.0만주**
(and 005930 **−445.2만** with institutions **−423.0만**, retail absorbing **+781.3만**). leg2 **no**.
=> **The row currently sits in branch B.** Registered anyway because **branch A is the adversarial ask**
and because a live counter-signal exists: `module_flow` stamps *외국인5일 매수전환* on **both** names —
the 20-day is an exit while the last five sessions are a turn. **This bracket is exactly the question of which one wins.**

**Anti-signal / VOID.** If SK하이닉스 announces a **capital raise, a major M&A, or suspends the buyback**
inside the window => `VOID` (the treasury programme is no longer the object being tested).

**Track KPI.** 000660 / 005930 KIS 20d foreign and institution legs (both signs, separately — `D273-KR`
says a sum can hide a split) · DART 005930 treasury filings · `자사주` theme multiplier (2.60x at registration) ·
**000660 자기주식 취득 결과보고서** when filed.

**C5 declared**: leg 1 uses a **sign**, not a magnitude, because this desk has never measured the
distribution of KR foreign-flow reversals after a buyback announcement. A sign test is low-resolution and
that is stated at registration rather than discovered at scoring.


---

## Registered by the 2026-08-22 `industry_kr` run

> ⚠ **ID 3-grep(WRITE 시점)**: `S64-KR` 은 08-19 런이 **예약한 ID** 이고 아직 발행되지 않았다(현행 최고 발행분 `S67-KR`).
> `S68-KR`~ 은 미사용 확인. **예약된 ID 를 그대로 쓴다** — 새 번호를 쓰면 08-19 의 예약이 미아가 된다.
> ⚠ **쓰기 방식**: `'a'` 모드 append(2026-08-05 truncation 사고 재발 방지, D165).

## S64-KR — ★★★ `S52-KR` 재등록: **제약이 섹터 명제인가 한 이름 명제인가** · ARMED · → **2026-09-19**

**왜 지금 발행하나.** 08-19 런이 예약하고 **08-20·08-21 두 런이 「정착 앵커 오염」을 이유로 연기**했다.
스파인 규칙: *"다음 런도 연기하면 그건 신중이 아니라 소멸 — 그 시점에 브래킷을 닫거나 관측면을 바꾼다, 문서로."*
**오늘 앵커 문제는 더 나빠졌다** — `^KS11` 의 2026-08-21 행에 `Close`=NaN 이 들어와 **832종목 스윕이 통째로 `scored=0`** 이 됐다.
**그런데 같은 창에서 `069500.KS` 는 08-21 정착봉 109,980 을 갖고 있고 1개월 결측이 0 이다.**
⇒ **닫지 않고, 앵커를 바꿔 발행한다.**

**`S52-KR` 이 죽은 세 결함, 각각 어떻게 고쳤는지 명시한다:**
1. **창을 캘린더가 아니라 「정착세션 카운트」로 정의** ⇒ 이 브래킷의 창은 **`069500.KS` 의 정착 거래일 21개**다
   (2026-08-21 정착일을 0일차로 하여 21번째 정착 종가 ≈ **2026-09-19**). **휴장은 자동 흡수된다.**
2. **O2 를 「스냅샷이 실제로 존재하는 세션」으로만 정의하고 `_mode` 동일을 요건에 명시** ⇒
   **O2 는 `n_axes` 가 동일한(=3축, `vel_axis=false`) 스냅샷에서만 계산한다.** 스냅샷이 없거나 축 수가 다르면 **O2 는 `unmeasured`** 이고 O1 만으로 채점한다.
   ⚠ **그리고 오늘 그 조건이 실제로 문제가 됨을 확인했다** — 오늘 원본 스냅샷은 `scored=0` 이라 O2 를 계산할 수 없었을 것이다.
3. **AS-1 목록에 정기보고서(사업·반기·분기)를 추가** ⇒ 아래 안티시그널에 명시.

### 관측면 O1 — 가격 다리 (**068270 셀트리온** 정착 종가)

| 항목 | 값 |
|---|---|
| 앵커 | **192,300** (2026-08-21 정착 종가, `069500.KS` 정착일 기준 정렬) |
| σ 출처 (D93, 오늘 재측정) | 068270 의 **21세션 로그변화 sd = 8.076pp**(n=460, 2년). 참고: 10세션 sd 6.052pp(full) / 7.523pp(최근134) / 6.108pp(최근60) · 일간 로그 sd 2.314pp(full) / 2.858pp(최근60) |
| σ 채택 | ★ **8.076pp — 창 길이(21세션)와 일치하는 sd 를 쓴다.** `S52-KR` 이 10세션 σ 를 21일 창에 썼던 불일치를 고친다 |
| **임계 (±1.0σ)** | **상단 208,475 / 하단 177,380** = `192,300 × exp(±0.08076)` |

| 분기 | 조건 | 의미 |
|---|---|---|
| **A (한 이름 명제)** | O1 이 **≥ 208,475** ∧ **O2 가 Bonferroni 미통과** | 대장주는 갔는데 폭은 안 왔다 ⇒ **제약 OW 는 한 이름 명제** |
| **B (섹터 명제)** | **O2 가 Bonferroni 통과**(O1 방향 무관) | 폭이 우연과 구분된다 ⇒ **섹터 명제** |
| **C** | 그 외 | 정보 없음 — **등록 시 favourite 로 선언한다**(아래 근거) |

### 관측면 O2 — 폭 다리 (**24섹터 동시 이항검정**, 오늘 새로 만든 계기)

**정의**: 정산일 스냅샷에서 **유니버스 🟢 비율 `p` 를 분모로 삼아**, `n≥5` 인 각 섹터의 🟢 개수 `k` 에 대해
**정확 이항 `P(X≥k)`** 를 구하고, **동시 검정 개수 `m`(오늘 24)로 Bonferroni 보정**한다.
**제약 버킷의 보정 후 p 가 0.05 미만이면 O2 통과.**

**오늘(2026-08-21 스냅샷) 사전 상태 — 등록 시 공개한다(D93·D122):**
- 유니버스 🟢 **80 / 806 = 9.926%.**
- **제약 n=48 · 🟢 1 · 기대 4.76 · z −1.82 · `P(X≥1)` = 0.9934** ⇒ **통과와 정반대 쪽 끝에 있다.**
- 같은 검정에서 **오늘 단독 p<0.05 를 넘긴 섹터는 보험 1개뿐**(P 0.0250, 보정 후 **0.600**)이고,
  **α=0.05·24검정의 기대 발생 수 1.2개와 실제 1개가 일치**한다.
⇒ ★ **branch B 는 매우 어렵다. 그것을 등록 시점에 숫자로 공개한다** — 「폭이 있다」가 나오면 그때는 정말 정보다.

### 정산 · 모드 · 안티시그널
- **정산 모드**: **TERMINAL 봉만.** 두 관측면 모두 **정착 종가**, 벤치가 필요한 경우 **`069500.KS` 인라인 명시**(C1).
- 🚨 **AS-1 (VOID — O1 만)**: 창 안에 **068270 의 ① 투자판단관련주요경영사항 ② 단일판매·공급계약 ③ 임상/품목허가 관련 공시**
  **④ ★신규: 정기보고서(사업·반기·분기)** 중 하나라도 제출되면 **O1 은 VOID**(O2 는 살아 있다).
  ⚠ ④가 이번에 추가된 이유: `S52-KR` 은 정기보고서를 목록에서 빠뜨렸고, 정기보고서는 **날짜가 미리 알려진 확정 이벤트**라 브래킷이 그것을 모르면 안 된다.
- 🚨 **AS-2 (O2 `unmeasured`)**: 정산일 스냅샷이 없거나 `n_axes` 가 **3 이 아니면** O2 를 계산하지 않는다(오늘의 `scored=0` 이 정확히 그 경우다).
- ⚠ **KR 내재변동성(옵션 IV)이 없어 implied-move 체크를 수행할 수 없다.** 지수선물 베이시스는 **컨텍스트지 임계가 아니다**(오늘 근월 괴리 +0.16%, OI 41,634). **그것으로 임계를 만들지 않았다.**
- **소유**: `industry_kr`.


---

## Registered by the 2026-08-23 `industry_kr` run

> ⚠ **ID 3-grep(WRITE 시점)**: `S68-KR` 은 `handoff/*.md` 에서 **1 hit** — 08-22 런의 *"`S68-KR`~ 은 미사용 확인"* 메모뿐이고 **실제 발행분은 없다.** 현행 최고 발행 **`S67-KR`**.
> ⚠ **쓰기 방식**: `'a'` 모드 append(2026-08-05 truncation 사고 재발 방지, `D165`).

## S68-KR — ★★ **KR 밸류 축의 반쪽 다리가 통과했을 때 그것이 초과수익이 되는가** · ARMED · → **2026-09-19**

**왜 이 브래킷인가.** 이 데스크의 프로토콜 델타는 KR 밸류 축을 이렇게 규정한다: *"「싸다」 판정은 두 다리를 요구하는데 KR 에는 하나뿐이다 —
(i) 마진이 자기 역사에서 어디 있는가는 `margin_history` 로 잴 수 있고, (ii) 추정치 리비전 추세는 **KR 에 존재하지 않는다.**"*
**그래서 지금까지 KR 「싸다」 주장은 전부 `[revision leg: unavailable — KR]` 로 반쪽 처리돼 왔고, 그 반쪽이 실제로 값을 갖는지 잰 적이 없다.**
**오늘 그 반쪽 다리를 명확히 통과한 이름이 보드에 하나 나왔다** — 그래서 **그 다리 자체를 검정 대상으로 올린다.**

**대상: 004370 농심.** 왜 이 이름인가(전부 2026-08-23 실측):

| 축 | 값 | 통과 |
|---|---|:---:|
| **밸류 — 마진 다리** | FY2025 총이익률 **29.0% = 11기 중 9위 · 백분위 27.3**(중앙 30.6 · 최고 FY2017 33.3%) ⇒ **피크가 아니다, 렌즈 L2 미적용** | ✅ |
| **밸류 — 멀티플** | Fwd PER **13.0** / TTM 13.36 / PBR 0.84 vs **동일업종 28.78** | ✅ |
| **밸류 — 리비전 다리** | **없다** | 🚫 `[revision leg: unavailable — KR]` |
| **A급(KIS 20d)** | 외 **+10.2만** ∧ 기 **+12.5만** = 두 다리 양 · 개 −21.9만 | ✅ |
| **가격** | rs20 **+21.4** · rs60 **+24.3**(벤치 `^KS11`) | ✅ |
| **C급** | OBV 매집 · `vol_surge` **2.22** | ⚠ **부호가 음(−)으로 유의한 축에 크게 의존** |
| **서사** | 뉴스속도 **2.14×** · `라면` **🟡ACCEL 2.02× (2,220건)** | ✅ |
| 포지셔닝 | 공매도 **0.70% float `covering(−0.18)`** ⚠주목 | — |

★ **대조군이 이 브래킷의 절반이다**: 같은 섹터·같은 테마의 **003230 삼양식품은 FY2025 총이익률 44.8% = 백분위 100.0**(자기 11기 최고, PBR **7.41**)이라
**렌즈 L2 정면 발화**이고 오늘 거부 원장 `H.밸류소진` 에 등재됐다. **두 이름은 마진 위치가 정반대인데 라벨과 테마는 같다**(W5).

### 관측면 — **21 정착세션 초과수익, 벤치 `069500.KS` 인라인**

| 항목 | 값 |
|---|---|
| 앵커 | **004370 = 432,500** · **`069500.KS` = 109,980** (둘 다 **2026-08-21 정착 종가**, `yfinance auto_adjust=False`, 조회 2026-08-23 10:1x) |
| 창 | **`069500.KS` 의 정착 거래일 21개** — 08-21 을 0일차로 하여 **21번째 정착 종가 ≈ 2026-09-19**(`S64-KR` 과 같은 규약, 휴장 자동 흡수) |
| 추정량 | **21세션 초과 로그변화** = `ln(004370_t/004370_0) − ln(069500_t/069500_0)`, pp 단위 |
| **σ · 중심 출처 (`D93`, 오늘 재측정)** | 2년 표본 **n=460**: **평균 −4.773pp · sd 14.938pp.** 참고 10세션 −2.122/9.729 · 5세션 −1.039/6.981 |
| 🚨 **중심을 0 이 아니라 −4.773pp 에 둔다** | **이 추정량은 0 에 중심이 없다.** 0 을 기준으로 밴드를 잡았으면 **branch A 가 4.8pp 쉬워지고 branch B 가 4.8pp 어려워졌을 것이다.** `D93` 준수 |

| 분기 | 조건 | 의미 |
|---|---|---|
| **A (다리가 값을 갖는다)** | 21세션 초과 **≥ −4.773 + 14.938 = +10.165pp** | **마진 백분위 하위 + 저멀티플 + A급 두 다리** 조합이 **1σ 초과**를 냈다 ⇒ **KR 의 반쪽 밸류 다리는 인용할 값이 있다** |
| **B (다리가 값이 없다 / 반대다)** | 21세션 초과 **≤ −4.773 − 14.938 = −19.711pp** | 같은 조합이 **1σ 미달** ⇒ **반쪽 다리를 「싸다」 근거로 쓰던 관행을 재검토해야 한다** |
| **C** | 그 사이 | 정보 없음 — **등록 시점에 favourite 로 선언한다**(정규 가정 하 ~68%) |

### 안티시그널 (VOID) — **base-rate 를 등록 시점에 확인했다** (`D300-KR` 교훈)

창(≈30 캘린더일) 안에 **004370 이 다음 중 하나를 DART 에 제출하면 `VOID`**:
① `단일판매·공급계약체결` ② `자기주식취득/처분/소각결정` ③ `유상증자/전환사채 발행결정` ④ `기업가치제고계획(자율공시)`.

🚨 **base-rate 실측(`module_disclosure 004370 --days 90`, 2026-08-23)**: 90일 창(2026-05-28~08-13) 공시 **13건** 중
**①②③ 은 0건**이고 **④는 2건**(06-29 2025년 이행현황 · 07-28 2026년). 12건은 전부 정기·계열거래·지배구조 류이며
**3Q 정기보고서는 2026-11-15 로 창 밖**이다.
⇒ **①②③ 의 30일 발화 확률 ≈ 0. ④는 ≈ 0.5건/30일**로 **비영(非零)이지만 「거의 확실히 발화」와는 거리가 멀다.**
**④를 남겨 둔 이유**: 밸류업 공시는 이 이름의 멀티플을 직접 움직일 수 있고, 그러면 검정 대상이 「마진 다리」가 아니라 「자본정책」이 된다.
**이 확률을 등록 시점에 숫자로 공개한다** — `S91`/`S93` 이 「발화하도록 설계된」 절 때문에 VOID 된 것을 반복하지 않기 위해서다.

⚠ **추가 VOID (섹터 레벨)**: 창 안에 **라면·가공식품 카테고리 전체를 움직이는 규제·관세 조치가 3매체 이상으로 인쇄**되면 `VOID`
(이 브래킷은 이름의 밸류 다리를 묻는 것이지 카테고리 충격을 묻는 것이 아니다).

### Track KPI · 모드 · 소유
- **정산 모드**: **TERMINAL 봉만.** 두 종가 모두 **정착 종가**, 벤치 **`069500.KS` 인라인 명시**(C1).
- **Track KPI**: 004370 KIS 20d **앞반/뒤반 분할** · 분기·연간 총이익률 백분위 · Fwd PER vs 동일업종 · `라면` 배율 · 공매도 `covering/building` ·
  **대조군 003230 의 마진 백분위**(현재 100.0).
- ⚠ **KR 옵션 IV 부재로 implied-move 체크 불가**(옵션-IV v1.1 대기). **선물 베이시스로 임계를 만들지 않았다.**
- ⚠ **정보 등급 선언**: **C 가 favourite** 이고 A/B 는 각각 ~16%다. **이 브래킷의 값은 A/B 가 나올 때 크고, C 가 나오면 거의 0 이다.** 등록 시점에 적는다.
- **소유**: `industry_kr`.

### ⚠ 이 브래킷이 **묻지 않는 것**
**「농심을 사야 하나」가 아니다.** 이 데스크는 사이즈를 내지 않는다(P4).
묻는 것은 **「KR 에서 유일하게 잴 수 있는 밸류 다리(마진 백분위)가, 나머지 축이 전부 같은 방향일 때, 21세션 초과수익과 관계가 있는가」** 이고,
**n=1 이므로 이 한 행으로는 답이 안 나온다**(C4). **이 행의 목적은 그 시계열을 시작하는 것이다.**


---

## S27 정산 노트 — appended 2026-08-25 by the `industry_kr` run (append-only)

**평결 `FIRED-B`.** 관측면(동결) = *"9차 지정의 휘발유·경유 상한 수준, 7차 기준 ₩1,784 / ₩1,773 대비"*.
**실측**: 산업통상부 **2026-08-21 발표 · 2026-08-22 00:00 시행 · 향후 4주간** ⇒
**휘발유 1,784 · 경유 1,773 · 등유 1,380 = 8차와 동일 = 동결** ⇒ **브랜치 B**("Cap frozen again, or cut").
브랜치 A(인상·폐지) 불발 · 브랜치 C(보조금·마진보전 스킴으로 재구조화) 불발 — **상한제 자체는 그대로다.**

- **소스**: 국내 코퍼스 8매체 교차(mt · newsis · chosun · yonhap · einfomax · donga · mk · sedaily), **본문 2건 전문 실독.**
  원문 인용: *"9차 석유 최고가격을 기존 8차와 동일하게 유지"*(mt 08-21) · *"두 차례 연속 같은 수준"*(newsis 08-22) ·
  *"석유제품 최고가격제 4주 더 연장"*(sedaily 08-21).
- ★ **등록 시 명시한 안티시그널이 옳은 방향을 가리켰다** — 대통령 *"오히려 더 강화해야 할 것 같다"*(2026-07-21 국무회의).
  **브랜치 B 에 최상위 정치적 뒷받침이 있었고 B 가 발화했다.**
- **브랜치 B 의 의미가 실현됐다**: 브렌트 **93.8**(08-20) · 두바이 95.6 · WTI 87.8, 국제 휘발유 **114달러/배럴**(8월 첫주 105) ·
  경유 **164**(148) 위에서의 **명목 동결 = 실질 기준 강화** ⇒ **크랙 개선이 국내로 전달되지 않는다**는 다리가 관측으로 확인됐고,
  `M157` 의 **국내 규제 3제품 매출 = 영업이익의 22.6×(SK이노) / 37.6×(S-Oil)** 노출은 **살아 있는 드래그**다.
- ★ **교차확인 KPI 가 처음으로 날짜를 얻었다**: 손실보전은 *"정유 4사가 원가 자료 준비·제출 중, 산업부가 **이달 말**까지 접수 →
  원가 검토 → **연말께** 규모 확정"*(newsis 08-22 본문). **어제까지 이 KPI 는 "날짜가 없다"였다.**
  ⇒ **후속 브래킷 등록 후보로 남긴다**(이 스테이지는 등록하지 않는다).
- 🚨 **프로세스 실패 기록**: 관측면은 **08-21 에 인쇄**됐는데 **08-22·08-23·08-24 세 런이 전부 "KR 정산 도래 0건"** 으로 넘겼다.
  원인은 시장이 아니라 **열거 방법**이다 — 이 행의 정산일이 `~2026-08 late` 라는 **퍼지 문자열**이라
  **날짜 정렬 전수표에 한 번도 나타나지 않았다**. **`EXPIRED` 는 아니다**(오늘 채점) — **3런 지연을 실패로 기록**하고
  처방은 **`D347-KR`**(전수표에 "날짜 미파싱 행" 칸 강제).
- ⚠ **다음 지정(10차)은 4주 주기상 ~2026-09-18 이다.** **이번엔 날짜를 퍼지로 두지 않는다** — 위 칸이 그것을 잡는다.

---

## S69-KR — ★★★ 보유 이름의 **자본구조 이벤트**를 처음으로 브래킷에 묶는다 · **SCORED `FIRED-A`(부분 — `O1` 만) 2026-09-05** (was ARMED · → 2026-09-05)

> 등록 2026-08-31 (`industry_kr`, MACRO/ALPHA). **이 행은 같은 런이 등록한 dig `D401-KR` 의 즉시 이행이다.**

### 왜 이 행이 존재하나
**`316140` 우리금융지주(보유)의 신주 8,697,000주 추가상장이 오늘(2026-08-31)인데,
`SCENARIOS_KR.md` 의 `08-31` grep 은 **0건**이었다.** 이 이벤트를 오늘 런에 상기시킨 것은 정산 기계가 아니라
**`STANDING_VIEW_KR §3b` 의 산문 한 줄**뿐이었다. **등록부의 산문은 정산 표가 읽지 않는다.**
⇒ 증자·상장·감자·분할·CB 만기처럼 **날짜가 확정된 자본구조 이벤트는 관측면과 임계값이 있는 행이어야 한다.**

### 등록 시점 상태 (사후에 바꾸지 않는다)
- **발행**: 8,697,000주, **합병 대가 발행**(DART **2026-08-11 증권발행실적보고서(합병등)**) — 현금 조달 아님.
- **반대편**: **2026-07-24 자기주식취득 신탁계약 4,854,368주**(발행량의 **55.8%** 규모) + **2026-07-24 주식소각결정**.
  ⚠ **신탁 집행 진도와 소각 수량은 `unknown`(C3, DART 본문 파싱 0 = `D360-KR`).**
- **flow(asof 08-27)**: 🟡중립 **−0.222** · OBV +0.315 매집 · **`rs20` −18.4**(벤치 `^KS11`) · `vol_surge` 0.60 · Δ −0.028.
- **KIS 20일 누적**: 외국인 **−9.8만주** / 기관 **+273.6만주**.
- **08-31 개장(⚠미완봉, 점수 아님)**: 09:08 −0.44%(`069500.KS` −3.70% 대비 **+3.26pp**) →
  09:19 **+0.59%**(지수 −2.56% 대비 **+3.15pp**).

### 관측면 (하나만, 사전 고정)
**`O1` = 2026-08-31 부터 5 정착세션(08-31·09-01·09-02·09-03·09-04) 의 `module_KIS --investor` 기관 순매수 누적 부호.**
**`O2` = 같은 5세션의 `316140` 종가 수익률 − `069500.KS` 종가 수익률 (pp).** 둘 다 **정착 종가**로만 읽는다.

### 분기
- **A (희석 흡수)**: **`O1` 양(+) **그리고** `O2` ≥ 0** ⇒ **추가상장 물량을 기관이 받아냈고 가격이 지수를 안 밑돌았다.**
  ⇒ `STANDING_VIEW_KR §3b` 의 「희석 = 하방 축」 절을 **폐기**하고 `M1113`(합병대가+자기주식 상쇄)을 본 판정으로 승격.
- **B (희석 발현)**: **`O1` 음(−) **또는** `O2` ≤ −3.0pp** ⇒ **희석이 실제로 가격에 왔다.**
  ⇒ `M1113` 의 「상쇄」 절은 **규모만 맞고 실현은 틀렸다**로 기록하고, 보유 테제를 재작성한다.
- **C** = 그 사이(`O1` 양(+)인데 `O2` −3.0 ~ 0). ⇒ **정보 없음.** 기관은 받았는데 가격은 안 따라온 상태.

### 등록 시점 favourite 과 정보량 (사전 선언)
**`O1` 은 최근 20일 기관 +273.6만주로 이미 강하게 양(+)** ⇒ **`O1` 양(+)은 modal 이고 정보량이 낮다.**
⇒ **이 행의 정보는 `O2` 에 있다.** **`O2` ≤ −3.0pp(분기 B)가 이 행의 고정보 갈래**이고,
**그 사실을 등록 시점에 선언한다**(사후에 「A 가 나왔으니 확인됐다」로 읽지 않기 위해).

### Anti-signal / VOID
- **VOID ①**: 5세션 창 안에 **`069500.KS` 가 어느 하루라도 ±3.0% 를 넘는 세션**이 있으면
  **`O2` 는 시장 사건에 오염된 것으로 보고 `O1` 만으로 채점한다**(부분 채점, VOID 전체 아님).
  ⚠ **08-31 개장이 이미 −3.70% 였다** ⇒ **이 절은 발화 가능성이 높다. 발화하면 그렇게 기록한다.**
- **VOID ②**: 창 안에 **`316140` 의 새로운 자본거래 공시**(추가 증자·소각 실행·대량보유 변동)가 나오면
  **그 공시일에서 창을 끊고 그때까지로 채점**한다.
- ⚠ **건수 임계값 안티시그널 0개**(`M-117`① 이 휴일 분모에 발화해 죽은 사례).
- ⚠ **`D394-KR` 확인 완료**: 2026-09-05 는 **금요일, KRX 개장일**이다.
- ⚠ **`D402-KR` 확인 완료**: 관측면이 **KR 종가**이므로 **KST 15:30 이후 채점 가능** — KR 데스크가 채점한다.

### Track KPI
`module_KIS 316140 --investor 20`(기관 일별·누적) · `316140` 과 `069500.KS` 의 일별 정착 종가 ·
`module_disclosure 316140 --days 14`.

---

## S151-KR — ★★★ 한 날에 두 바이너리: 동시만기인가 매크로인가 · ARMED · → **2026-09-11**

**등록 2026-09-07 (`industry_kr` BET §5).** ID 는 `module_evidence next-id S` **라이브 스캔** 발급(현재 최고 S150).
⚠ **KR 프로토콜에는 PREMORTEM 블록이 없다** — 그래서 BET 이 걸었다. **L2 `schedule` 의 등록 문턱
「근월 잔존일 ≤5」가 오늘 4 로 처음 발화**했고, `catalyst_calendar` 는 `--days 5`·`--days 10` 둘 다에서
이 날짜를 **못 본다**(`D391-KR` 4번째 재현).

### 질문
**2026-09-10 은 KOSPI200 선물·옵션 동시만기(네 마녀의 날) ∧ 미 8월 PPI 발표일이다.
그날 KR 가격 움직임의 주인은 만기 물량인가, 매크로인가?**

### 동결 관측면 (등록 시점에 고정 — 사후 변경 금지)
**`069500.KS`(KODEX 200)** 의 두 값:
- **O1 = 09-10 거래량 ÷ 직전 20 정착세션 거래량 중앙값**
- **O2 = |09-11 종가 − 09-10 종가| ÷ |09-10 종가 − 09-09 종가|** (되돌림 비율)

### 분기 (전수 · 「위 어느 것도 아님 ⇒ 정보 없음」 포함, `D443-KR`)
- **A · 만기가 지배**: **O1 ≥ 1.5** ∧ **O2 ≥ 0.50**
  ⇒ 09-10 의 움직임은 지수차익·롤오버 물량이고, **그날 KR 가격을 PPI 로 귀속하면 오귀속이다.**
- **B · 매크로가 지배**: **O1 < 1.5** ∧ **O2 < 0.50**
  ⇒ 만기 물량이 지배하지 않았고, **PPI 로 읽어도 된다.**
- **C · 정보 없음**: 위 어느 것도 아님(O1·O2 가 갈리거나 O2 가 0.30~0.70 구간).

### 안티시그널 (필수)
1. **09-08~09-09 에 근월 미결제(등록 시 48,473)가 차월(33,037) 아래로 떨어지면** ⇒ 롤이 완료된 것 ⇒ **B 쪽으로 기운다**(전제 약화).
2. **09-10 에 KRX 가 휴장하거나 거래가 중단되면** ⇒ **관측면 미발생 ⇒ `VOID`.**
3. **미 8월 PPI 가 09-10 에 발표되지 않으면**(연기·셧다운) ⇒ **두 바이너리가 아니라 하나 ⇒ 명제 재작성**, 채점하지 않는다.
4. 위 어느 것도 발화하지 않고 **09-12 까지 O1·O2 를 못 재면 `C` 로 닫는다.**

### 등록 시점 상태 `[measured]` — ⚠ **정산일에 이 상태를 인용하지 말고 원천을 재조회한다**
`module_KIS --futboard` / `--futopt A05609` (2026-09-07 개장 전):
**근월 A05609 잔존일 4 · 최종거래일 20260910 · 현재가 1,052.50 · 이론가 1,052.03 · 베이시스 +0.51 ·
괴리율 +0.04% · 미결제 48,473** · **차월 A05610 미결제 33,037** ⇒ **D-4 에 근월 비중 59.5%(롤 미완).**
기초지수 종합 6,687.21 · KOSPI200 1,051.52.
벤치 `069500.KS` 09-04 정착 종가 **105,720**(당일 +2.036%).
⚠ **`feedback_bracket_registration_state_stale` 준수**: 위 숫자는 **등록 시점의 상태**다. 정산일에는
`--futboard`·`069500.KS` 를 **다시 조회**한다.

### 정보량 선언
**favourite 없음.** 이 데스크는 **KR 만기 세션의 거래량 분포를 측정한 적이 없다**(`C3`).
⇒ **A·B·C 어느 갈래가 나와도 새 정보다.** 그것이 이 행을 등록하는 이유이고,
**`B4`(favourite 이 확실하면 정보량이 없다)의 정반대 조건**이다.

### 추적 KPI
근월/차월 미결제 일별 · 근월 잔존일 · `069500.KS` 일별 거래량 · 09-09/09-10/09-11 종가.

**상태: `ARMED` · 정산 2026-09-11 · 소유 `industry_kr`**

## S153-KR — ★★★ 표적관세는 **세율이 붙는 순간** KR 메모리의 진짜손을 뒤집는가 · ARMED · → **2026-09-30**

**등록 2026-09-08 (`industry_kr` BET/ALPHA).** ID 는 `module_evidence next-id S` **라이브 스캔** 발급(현재 최고 S152).
⚠ **KR 프로토콜에는 PREMORTEM 이 없다** — 그래서 BET/ALPHA 가 건다.

### 질문
**09-07 에 KR 하드웨어 4종을 외국인·기관이 동시에 샀다(개인은 팔았다). 그 매수는 「표적관세를 알고도 산 것」인가,
「아직 안 본 것」인가?**

### 동결 관측면 (등록 시점에 고정 — 사후 변경 금지)
- **O1 = `module_KIS <code> --investor` 의 외국인 20일 누적 부호**, 대상 **`005930`·`000660`** 2종.
- **O2 = 미 행정부가 반도체 표적관세의 「세율 또는 국가별 할당량」을 공표했는가**(공표일 = D0).
- 판정 창 = **D0 이후 3 정착세션**. D0 가 2026-09-30 까지 없으면 아래 (c).

### 분기 (전수 · 「위 어느 것도 아님 ⇒ 정보 없음」 포함, `D443-KR`)
- **A · 관세는 이미 가격에 있다**: D0 발생 ∧ **3세션 뒤 2종 모두 O1 이 양(+) 유지**
  ⇒ **진짜손은 관세를 알고 샀다.** 09-07 매수는 정보에 기반한 것이고 서사(「훈풍」)가 아니라 실측이 옳았다.
- **B · 랠리는 관세를 안 봤다**: D0 발생 ∧ **3세션 뒤 2종 중 1종 이상이 O1 음(−)으로 전환**
  ⇒ **09-07 의 4/4 진짜손 매수는 미공개 리스크 위에서 난 것**이고, `M1446` 을 「정보」로 읽으면 안 된다.
- **C · 정보 없음**: D0 가 09-30 까지 없거나, O1 두 종의 부호가 갈린 채 창이 끝난다.

### 안티시그널 (필수)
1. **세율이 공표됐는데 KR 이 명시적으로 제외되면** ⇒ **전제(표적이 KR 메모리) 소멸, 즉시 `VOID`.**
2. **삼성전자 또는 SK하이닉스가 미국 내 「메모리」 생산 투자를 공시하면** ⇒ 본문이 세운 표적 조건이
   사라진다 ⇒ **명제 재작성**(관세가 아니라 투자 협상 명제가 된다).
3. **`module_KIS --investor` 가 개장전 플레이스홀더 행을 실세션으로 오독되면** ⇒ 관측 무효.
   **정산 시 마지막 행의 수급 3칸이 비어 있지 않은지 반드시 확인한다**(오늘 09-08 행이 그랬다).
4. 위 어느 것도 발화하지 않고 **2026-09-30** 까지 O2 가 없으면 **(c)** 로 닫는다.

### 등록 시점 상태 `[measured]` — ⚠ **정산일에 이 상태를 인용하지 말고 원천을 재조회한다**
09-07 정착 KIS(만주): `005930` **외 +324.6 · 기 +456.8 · 개 −964.9** · `000660` **외 +77.2 · 기 +36.6 · 개 −177.2**.
1차 인용(09-02, 러트닉): *"반도체를 미국에서 생산하면 관세를 내지 않지만, 그렇지 않다면 … 대가를 각오하라"* ·
*"표적화되고 신중한 관세"*; Politico 국가별 세율·할당량 검토를 러트닉이 *"정확하게 맞다"* 확인.
**양사 모두 미국 내 메모리 생산 계획 없음**(같은 본문). 어휘 `표적관세` d7 **89** · `theme-age` **🟢FRESH 나이 5일**.

### 정보량 선언
**favourite 은 A** 다 — 진짜손 4/4 는 이 데스크가 오늘 가진 가장 깨끗한 신호이고, 그것이 무지의 산물이라고
가정할 근거가 없다. ⇒ **이 행의 값은 B 가 날 때 크다**: B 는 **「KIS 실측을 A급으로 쓴다」는 이 데스크의
가장 자주 쓰는 근거 자체를 깎는다.**

### 추적 KPI
`005930`·`000660` 외국인 20일 누적 일별 · `표적관세` d7 과 theme-age · 세율·할당량 공표 여부 ·
전기·전자 정렬 `eqflow`.


---

## Brackets registered 2026-09-09 by the `industry_kr` run

> ⚠ IDs issued with `module_evidence next-id S --count 3` (live scan; highest existing **S153**)
> ⇒ **S154 · S155 · S156** allotted; **two used**.

## S154-KR — ★★★ 세 사건이 한 날에 겹치는데 캘린더는 하나만 안다 · ARMED · → **2026-09-11**

등록 **2026-09-09 (`industry_kr` DEEP-IT §1 / ALPHA)**.

**이 브래킷이 메우는 공백.** `catalyst_calendar --days 14` 의 `[STRUCTURAL]` 은 **09-18 S&P 분기 리밸런스
하나만** 싣는다. 이 런이 실측한 09-10 의 세 사건 중 **둘을 캘린더가 못 본다** — `D391-KR`/`D510` **7번째**.

**등록 시점 상태** `[measured, 1차 + 3매체]`:
- **KR 지수선물·옵션 동시만기**: `module_KIS --futboard` 근월 `A05609` **잔존일수 2 · 최종거래일 20260910** ·
  미결제 **52,259**(+204) · 차월 `A05610` **48,838**(+10,871) · **근월 비중 51.7%**(09-07 59.5% → 09-08 57.8%) ·
  베이시스 **+0.16**(3세션 연속 축소) · 괴리율 **−0.17%**.
- **반도체 ETF 리밸런싱**, 3매체 독립: chosun 09-07 「**10일 장 막판** 수급 대이동…반도체 ETF 리밸런싱에
  **1.8조** 몰린다」 · yonhap 09-08 「미래에셋 "삼전닉스, ETF 리밸런싱에 **1.4조 매물** 가능성"」 ·
  한국경제 09-08 「삼전닉스 팔고 '이 종목' 쓸어 담는다…**1.3조** 뭉칫돈 대이동」.
- **美 8월 PPI** — `catalyst_calendar` `[bls✓]` 확인, 유일하게 캘린더가 아는 것.
- 등록 시점 두 이름: `005930` 🟡 · 9세션 외 **+397.9만** · 기 **+120.7만** / `000660` 🟡 · 외 **−17.7만** · 기 **−142.7만**.

**관측값(동결)**: **2026-09-10 정착 종가 기준** ① `069500.KS` 의 **거래량 / 직전 20세션 중앙값** 배수(O1) ·
② `005930` 과 `000660` 의 **당일 등락률 차**(O2, 부호 포함).

| Branch | Observable | Meaning |
|---|---|---|
| **A** | **O1 ≥ 2.0×** ∧ **abs(O2) ≥ 2.0pp** | **구조적 물량이 실제로 지배했고, 두 이름을 다르게 쳤다.** ⇒ 「삼전닉스」를 한 단위로 묶는 보도 관행이 틀렸다는 것이 가격으로 확인된다(`M1463` 의 가격 쪽 확증) |
| **B** | **O1 ≥ 2.0×** ∧ **abs(O2) < 2.0pp** | **물량은 왔는데 두 이름을 같게 쳤다.** ⇒ 실측 수급의 반대 부호가 하루짜리 이벤트를 이기지 못한다 — 이 데스크의 A급 축이 이벤트 앞에서 약하다는 뜻 |
| **C** | **O1 < 2.0×** | `AMBIGUOUS` — **밴드를 넓히지 않는다.** 1.3~1.8조는 보도값이지 실현값이 아니었다는 뜻이고, **09-18 S&P 리밸런스로 재등록**한다 |

**Anti-signal (VOID)**: **(i)** 09-10 에 **미·이란 사태의 새 군사 전개**나 **PPI 서프라이즈 ≥0.3%p** 가
같은 세션에 들어오면 거래량 배수의 귀속이 불가능 ⇒ `VOID`, 새 조건으로 재등록.
**(ii)** 동시만기가 **연기·변경**되면 전제 소멸 ⇒ `VOID`.
⚠ **범위(C4)**: *"삼성전자를 살까"* 를 묻지 않는다. **"겹친 하루에 구조적 물량이 두 이름을 다르게 치는가"** 하나만.
⚠ **임계 근거(`D497-KR` 준수)**: O1 의 2.0× 는 **동시만기일의 알려진 거래량 배수 관행이 아니라**
이 데스크가 관측한 `069500.KS` 최근 거래량비(09-08 **1.347×**, 09-07 0.906×)의 **약 1.5~2배**에서 잡았다.
**O2 의 2.0pp 는 09-07 두 이름의 실제 차(+5.68% vs +8.26% = 2.58pp)에서 왔다** — 지어낸 라운드 넘버가 아니다.
⚠ **정산일이 09-11 인 이유**: 09-10 종가는 **09-10 런이 열릴 때 아직 없다**(`D572` 의 KR 형태).

### 정보량 선언
**favourite 은 A** — `M1463` 이 두 이름의 실측 수급을 반대로 보여줬으니 가격도 갈리는 쪽에 무게가 있다.
⇒ **이 행의 값은 B 가 날 때 크다**: B 는 **KIS 실측(A급 축)이 이벤트 하루를 이기지 못한다**는 뜻이고,
그것은 이 데스크가 가장 자주 쓰는 근거의 유효 지평을 깎는다.

### 추적 KPI
`module_KIS --futboard` 근월/차월 미결제·근월 비중·베이시스(일별) · `069500.KS` 거래량 · 두 이름 일별 등락 ·
`리밸런싱`·`동시만기` 어휘.

---

## S155-KR — ★★ 「진짜 구동에는 서사가 없다」를 처음으로 채점 가능한 명제로 만든다 · ARMED · → **2026-10-09**

등록 **2026-09-09 (`industry_kr` DEEP-CONS / ALPHA)**.

**이 브래킷이 메우는 공백.** 이 데스크는 이름을 **서사(스레드·어휘)**로 고르고 **흐름**으로 확인한다.
오늘 그 순서가 **한 이름에서 정면으로 깨졌다**: 대우건설의 실제 60일 수주 ₩2.4953조 중 **52%가 공공발주**인데
어휘축 `공공발주` 는 **🔴FADING · 90d 총 5건 · 7d 평균 0.0** 이고, 데스크가 이 칸에 붙여온 `대미투자` 는
**🟡ACCEL 3.58× · 787건**인데 **계약서에 0건**이다(`M1464`·`M1465`).

**관측값(동결)**: **2026-10-09 까지** ① `module_disclosure 047040 --days 30` 의 **신규 수주공시 발주처 구성**
(공공·준공공 건수 / 금액명시 건수) · ② 같은 날 `theme_age --scope domestic` 의 **`공공발주` 90d 총건수**.

| Branch | Observable | Meaning |
|---|---|---|
| **A** | 30일 수주에서 **공공·준공공 비중이 금액 기준 40% 이상 유지** ∧ `공공발주` 90d 총건수 **여전히 20건 미만** | **구동과 서사의 괴리가 구조적이다.** ⇒ **이 데스크의 「서사로 후보를 고른다」 절차가 이 칸에서 체계적으로 반대쪽을 고른다**는 것이 확정되고, EVENT_ALPHA 의 카드 선택 규칙에 **「계약서 우선」 다리를 추가**한다 |
| **B** | `공공발주` 90d 총건수가 **50건 이상으로 확대** | **서사가 뒤늦게 따라왔다.** ⇒ 괴리는 **지연**이지 구조가 아니고, 서사 축은 유효하되 **지연 보정**이 필요하다 |
| **C** | 30일 수주 **0건**이거나 공공 비중이 **40% 아래** | `AMBIGUOUS` — 구동 자체가 바뀐 것이므로 **재등록**한다. **밴드를 넓히지 않는다** |

**Anti-signal (VOID)**: **(i)** 대우건설에 **경영권·자본거래**(매각·합병·대규모 증자)가 발생하면
수주 구성이 회사 사정으로 왜곡 ⇒ `VOID`. **(ii)** `module_disclosure` 가 **금액 파싱에 실패**해
현대건설처럼 「정정만 4건」 형태가 되면 **관측면 소실** ⇒ `C`, `D583` 에 연결.
⚠ **범위(C4)**: 이 행은 **대우건설을 사는가**를 묻지 않는다. **이 데스크의 후보 선택 절차가 옳은 축을 쓰는가**를 묻는다.
⚠ **한 이름 표본이다** — A 가 나와도 **일반화하지 않고 「이 칸에서 그렇다」로 닫는다**(`W5`).

### 정보량 선언
**favourite 은 A** — 오늘 관측이 이미 A 모양이다. ⇒ **값은 B 가 날 때 크다**: B 면 이 데스크의 서사 축은
**틀린 게 아니라 늦은 것**이고, 그건 고칠 수 있는 결함이다.

### 추적 KPI
`module_disclosure 047040 --days 30` 발주처·금액 · `theme_age` 의 `공공발주`·`대미투자`·`도시정비` ·
대우건설 태그·KIS 기관/외국인.


## Scoring-log rows added 2026-09-13 by the `industry_kr` run (verdicts live in `SCENARIOS.md` master log; headers above stay `ARMED` — `D472`)

| id | settle | verdict | frozen observable → measured |
|---|---|---|---|
| **S58-KR** | 2026-09-09 (scored 2 runs late — logged as a process failure) | **`FIRED-B`** | 000660 follow-up filing type by the company's own deadline → **09-09 「조회공시요구에대한답변(미확정)」** on the 충칭 sale, 3-month window, 재공시예정일 **2026-12-08** (rcept 20260909800559, body cp949 via `viewer.do…dtd=HTML`). Anti-signal (i) 자본변동 0 ✅ · (ii) `[unchecked]` (G1) |
| **S154-KR** | 2026-09-11 | **`FIRED-C`** | O1 `069500.KS` 09-10 vol/20d-median = **1.187×** (<2.0) · O2 −0.02pp → `AMBIGUOUS`, band not widened. ★ `D597`: the rebalance flowed through KRX 반도체 ETFs, not `069500.KS` — observable measured the wrong vehicle. Not re-registered (`D343`) |

**Next due**: `S61-KR` ~09-14 (pattern date) · `S62-KR` 09-15 · `S64-KR`·`S65-KR`·`S68-KR` 09-19.


## Brackets registered 2026-09-14 by the `industry_kr` run

## S158-KR — ★★ 09-14 의 보험 「버팀」은 금리 축 로테이션인가, −2.6% 세션의 저베타 착시인가 · ARMED · → **2026-09-16 정착 종가**

Registered **2026-09-14 by the `industry_kr` BET/ALPHA stages** (ID by `module_evidence next-id S`). Prepared by `SECTOR_DEEP_INS.md §7`; threshold set from the desk's own measured distribution, not by hand (`C5` satisfied).

**왜 필요한가.** 오늘 ROTATION 이 보험을 breadth 0.58·🟢 시총점유 92.5% 로 `OW−` 승격했다가 **같은 런에서 철회**했다 — 그 🟢 는 뉴스속도 결함 상수 4.29 가 만든 태그였다(`M1510`). 살아남은 다리는 **가격**(보험 EW +0.15% vs `^KS11` −2.63%, 장중) 과 **기관 단독 수급**(외국인 6/6 음) 뿐이고, 이 둘은 「하락 세션에 저베타가 이긴다」로도 설명된다(캐시 6세션: 벤치 상승일 2/2 패배 · 하락일 3/3 승리 = 저베타 서명). 태그가 아니라 수익률로 갈라야 한다.

**동결 관측면**: 보험 **11종 등가중**(032830·000810·005830·001450·088350·000370·000540·000400·003690·085620·031210 — **082640 동양생명 제외**, 08-28 이후 거래 0) 의 **09-14·09-15·09-16 3정착세션 누적 수익 − `^KS11` 3정착세션 누적 수익**, 기준가 09-11 정착 종가(`prices_kr_*.pkl` Close, 벤치 yfinance `auto_adjust=False`).

| Branch | Observable | Meaning |
|---|---|---|
| **A (로테이션)** | 누적 초과 **≥ +3.0pp** ∧ 3세션 중 **벤치 상승일 최소 1일에 초과 양(+)** ∧ 대형 3사(032830·000810·005830) 09-14~16 KIS 외국인+기관 합 **양(+)** | 금리/언더라이팅 축이 섹터 축을 지배한다 — `M-144` (a). INS 를 DEEP 재커버, 건설 「폭」 근거 철회 |
| **B (착시)** | 누적 초과 **≤ −3.0pp** 또는 벤치 상승일 **전패** | 09-14 순위는 저베타 아티팩트 — `M-144` (b). 보험 🟢/EW 를 `R143` 류로 기록 |
| **C** | 그 사이 | 정보 없음. 밴드를 넓히지 않는다 |

- ★ **임계 근거(`C5`)**: 캐시 29세션 보험 EW 일별 초과 **sd 3.20pp**, 3세션 합 **sd 5.20pp**, |초과|>1.0pp 인 날 83% ⇒ `M-144` 의 ±1.0pp 는 **0.19σ(노이즈)**. ±3.0pp ≈ 0.6σ — 여전히 손으로 고른 배수이나 **분포를 잰 뒤 고른 값**이다.
- **하위 분산 의무(`W5`)**: 생보 3(032830·088350·085620) · 손보 8 을 따로 보고. **손보만 통과하면 「보험」이 아니라 「손보 언더라이팅」으로 명제를 재작성**한다(20세션 생보−손보 −6.68pp, `M1514`).
- **Anti-signal (VOID / 재시작)**: ① 09-16 FOMC 가 인상 이외(동결·50bp) ⇒ 창을 09-17 부터 재시작 ② `^KS11` 3세션 중 하루라도 **±4%** ⇒ `VOID`(베타 지배) ③ 종가 후 재스윕에 velocity 4.29 가 잔존 ⇒ 🟢 관련 KPI 무효(판정엔 안 씀) ④ 09-19 까지 미발화 ⇒ C.
- **등록 시점 상태 `[measured]`** (⚠ 정산일에 이 상태를 인용하지 말고 원천을 재조회): 장중 12종 EW +0.15% vs `^KS11` −2.72% = +2.86pp(1세션, 카운트 안 함) · KR 커브 베어 플래트닝(3y +2.4bp / 30y −2.7bp) · 대형 3사 외+기 9세션 합 ≈ +365억 · 근월 선물 OI 54,054(+1,113).
- **정보량(L3)**: favourite **A** (`M-144` 와 같음) ⇒ 값은 **B** 에 있다 — 하락일 RS 착시를 처음으로 수익률로 잡는 표본. **공표 지연 0 영업일**(정착 종가).
- **Track KPI**: 보험 11종 EW 일별 초과 · 벤치 상승일 승패 · 대형 3사 KIS 일별 · KR 30y 방향 · 서지≥1.2 이름 수 · 삼성화재·삼성생명 10-02 재공시.
- ⚠ **Not a position.** 종목을 지목하지 않는다 — 섹터 명제 하나만 잰다(P4).

## Scoring-log rows added 2026-09-14 by the `industry_kr` run (verdicts live in `SCENARIOS.md` master log; headers above stay `ARMED` — `D472` 16th)

| id | settle | verdict | frozen observable → measured |
|---|---|---|---|
| **S61-KR** | ~09-14 (pattern) | **pending — not `EXPIRED`** | BoK Aug export-price MoM not printed by 13:xx 09-14 (7 domestic hits, all previews). Re-check daily until printed |
| **S62-KR** | 09-15 | (not due) | D-1: both indexes < 1.0× (`불법환적` 0.00× · `환적` default 0.54×), no US document naming Korea; thin denominator 09-09~13 |
| **S125** (US-owned) | 09-11 | **`FIRED-A`** (scored by KR — missing from US 09-12 table) | ADM +2.773 / XLP −2.205 = **+4.978pp** ≥ +0.602 |

**Next due**: `S62-KR` 09-15 · `S61-KR` when printed · `S158-KR` 09-16 close · `S64-KR`·`S65-KR`·`S68-KR` 09-19.
