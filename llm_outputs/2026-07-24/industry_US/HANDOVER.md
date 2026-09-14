# HANDOVER — industry_US · 2026-07-24 (Fri)

> Stage 1/10. Inherits `handoff/STANDING_VIEW.md` · `SCENARIOS.md` · `RESEARCH.md`, reconciles them
> against the mechanical ledger (`module_report_tags show`), scores every past-dated scenario, and
> audits the rejection ledger. **Transports analysis only — zero buy/sell language (P4).**

---

## 0. Run clock — binding on every downstream stage

| | |
|---|---|
| Run start | **2026-07-24 22:09 KST = 09:09 ET (Fri)** |
| US regular session | **NOT OPEN** (opens 09:30 ET, 20 minutes after this stage started) |
| ⇒ Every price / RS / flow number this run may cite | the **2026-07-23 regular close** |
| Any 2026-07-24 bar | an **incomplete or non-existent bar** — label it as one, never score against it |

⚠ **D31 applies with full force today.** `module_flow` includes the current-session bar while
`sector_flow` excludes it; at 09:09 ET the current bar is either absent or ~0% of a day. **Every
pre-close `module_flow` call this run must state that its `vol_surge` and OBV are unusable.** RS20/RS60
over 20/60-day windows are barely affected — that is the axis to build on (and it is the A-grade one
anyway, rule D6).

⚠ **The immediately prior run was `industry_kr`, finished earlier TODAY (2026-07-24).** Its carry is
already folded into `STANDING_VIEW.md` (M48–M68, R13–R16). This run does **not** re-derive it.
Its KR-measured findings do **not** transfer to US conclusions without replication (rule **W1**) —
except where the KR run explicitly replicated a US finding (M55 replicating M25/M38), which is
evidence about **code structure**, not about a market.

---

## 1. Inherited regime call

**Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
`[inferred]`, built on M1–M6, M14, M18.

- The equity tracks the **second derivative of price** (lens L1), not the level. "Shortage persists"
  (M7, capacity to mid-2027/2028) and "the equity struggles" are both true and not contradictory.
- ⚠ **The governing asymmetry (STANDING_VIEW §4) is now measured, not assumed**: a hyperscaler capex
  **cut** changes the thesis; a **raise** only moves its timing. S1 fired branch A (GOOGL $195–205B)
  and the *stock fell anyway* — which is why **S13** exists and is the highest-information bracket
  the desk is carrying into 07-29.
- **Nothing in today's inheritance revises §1.** Four independent volume confirms have arrived
  (M29, M58) and **none of them touches M1/M2/M18**, which is the price/margin leg.

### Carried `[measured]` chain most load-bearing for a **US** run today

| # | Fact | Value | asof |
|---|---|---|---|
| M30 | Front-end led, **2s10s flattened** | 2y 4.26% (120d high) vs 10y 4.63%; 2s10s +0.37, −2bp; real 10y 2.37% (120d high) | 07-21/22 |
| M31 | **Credit confirms nothing, 5th week** | HY OAS 2.69% (6bp off 365d low) · IG 0.78% · NFCI −0.552 loosening | 07-21/17 |
| M32 | Crude ↑ / crack ↓, and the split is **gasoline** | WTI +5.2% while 3-2-1 crack −11.2%; gasoline −19.7% vs distillate −3.6% ⇒ diesel−gasoline gap 30.3 → 38.5 | 07-23 intraday ⚠ |
| M37 | **M24 replicated on an independent date** | RE digital-infra mean RS20 −9.85 vs duration REITs +8.37 vs SPY = **18.2pp**, identical to 07-21 | 07-22 close |
| M38 | **The US 🟢 tag is a volume test** | `velocity` None on all 300 rows; 93 pass OBV ∧ RS20>0, **only 25 are 🟢 — 68 blocked by `vol_surge` alone** | 07-22/23 |
| M39 | **Health Care #1 flow of 11** | wflow +0.351, breadth 0.19, 6🟢/3🔴 — against **Δ −0.102** and flat revision books | 07-22/23 |
| M40 | Financials is the only **breadth-led** sector, and the gap narrowed | eqflow +0.320 > wflow +0.253, but the gap went +0.145 → **+0.067** | 07-22 close |
| M42 | Revision books | Best **AMAT 25↑:0↓ · MU 25↑:0↓ · PANW 40↑:1↓ · FTNT 39↑:0↓ · DDOG 37↑:0↓ · GS 9↑:0↓**. Worst **MRK CY −46.0%/90d · XOM 0↑:4↓ · CVX 0↑:3↓ · HUM −128.2%** | 07-23 |
| M43 | All three refiners trade **above** consensus target | upside −9.3% / −7.1% / −5.1% on CY EPS +54.2 / +70.7 / +51.0% over 90d | 07-23 |
| M44 | Mega-caps separated | META/MSFT/AMZN/AAPL all 🟢 `new_green`; **GOOGL alone 🔴분산** — *before* the EU decisions printed | 07-22 close |
| M45 | The blockade's literal beneficiaries **are not being bought** | STNG/FRO/INSW/DHT/TNK RS20 vs SPY −0.7 / −6.5 / +1.7 / −5.9 / −2.2 on 2.76–4.29× news velocity | 07-23 |
| M46 | **C6 stands** | `"capex cut"` d1 = **0**, d7 = 1, `--scope foreign` — unchanged after S1 fired and GOOGL fell | 07-23 |
| M47 | Implied moves are structurally unusable for 07-29/07-30 events | META ±4.4% · MSFT ±2.9% · VLO ±3.2% **all expire 07-24, before their events** | 07-23 |

⚠ **`[inferred]` claims carried but NOT admissible as evidence** (they may not be laundered into a
new proposition): §1's regime call · the "pullback not downtrend" read on AMAT/LRCX/KLAC · the
war-premium-vs-margin reading of the refining node (C4) · the M45 "crowded narrative ≠ owned
exposure" read · D22's "BOJ tightening leads the US long end" (explicitly `[unverified]` under W2).

---

## 2. Retracted ledger — read BEFORE forming today's view

Sixteen entries (R1–R16). **The four that a US run is most likely to re-invent today:**

| # | Do not resurface | The measurement that killed it |
|---|---|---|
| **R7** | "Real Estate is the purest duration expression on the board" | The tape says the reverse: WELL +16.0 / VTR +17.0 RS20 vs SPY *bid* at a 120-day-high real yield, while the reds are digital infrastructure. **RE is a third copy of the AI-datacenter short**, replicated 07-22 (M37) |
| **R10** | "IT + RE + UTIL underweights are ONE risk concentration" **in its strong form** | 699 trading days of SPY-residual correlation: DLR–NVDA +0.049, EQIX–NVDA **−0.118**, CEG–NVDA +0.182 — all below the 0.35 unit threshold, clustering into **four** separate units. ⚠ C4: "not supported", **not** "rejected". **Surviving weak form (usable): they share one *catalyst* — hyperscaler capex — so they can move together on an event.** That is event concurrency, not correlation concentration |
| **R11** | "The long-end move is bear-**steepening** — term premium, not cut-pricing" | 2s10s **flattened** −2bp the next day (M30). ⚠ **The Financials OW rested on the steepener; this removed one of its two legs**, and the survivor (breadth) is itself weaker than first written (M40) |
| **R12** | "The refining detachment counter is at 4 consecutive observations" | On 07-22 VLO/MPC/PSX **fell** −1.2/−1.2/−0.4% while crude rose and the crack fell — the *opposite* of detachment. **Corrected: 3 confirmed · 1 broken · 1 unconfirmed.** The counter's threshold is **further away, not closer** |

Also live and easy to re-invent: **R5** (EDA does **not** lead semis — same-month +0.63, lag-12 +0.05) ·
**R8** (PSX is **not** the cheapest large refiner — MPC 10.99 < PSX 11.72 < VLO 12.73) ·
**R9** (AXON is **not** a defense name — no customer >10% of net sales, the word "backlog" does not
appear in its 10-K) · **R3** (a KR-measured fear-gauge result may not be applied to VIX/US).

★ **Pattern flagged by the prior run and carried as an instruction, not an observation**: R7, R12,
R14, R15 and R16 were all killed **by the same run's own later stages**, i.e. an assertion gets ~4
stages of life before anything checks it. **This run's counter, applied at MACRO rather than at
DEEP**: quote the benchmark in the same sentence (C1), pull the stored history before calling a
delta #1 (D38), and state which `module_flow` path produced any 🟢/🔴 (D43).

---

## 3. Scenarios — scored, pending, armed

### 3a. Past-dated rows

| ID | Event date | Status | Settlement |
|---|---|---|---|
| **S1** | 07-22 AMC | **FIRED-A** (scored 07-23) | GOOGL FY26 capex $180–190B → **$195–205B**. Volume leg extends; **M1 unaffected** |
| **S6** | 07-23 AMC | **FIRED-A** (scored 07-24 by the KR HANDOVER) | Both legs: a **named external foundry customer (Fortinet)** *and* **capex guided up** — INTC "boosts spending plans on AI boom", sales +25% YoY. ⚠ The customer is on **Intel 4 (mature), not 18A**; leg (ii) alone satisfies branch A so the node dispute does not change the verdict. **The registered ±4.4% "a FLOOR, not a fair estimate" caveat is measured correct (fresh pull ±12.7%)** |
| **S7** | 07-23 pre-mkt | **FIRED-A, branch now COMPLETE** | Backlog leg scored 07-23 (RTX $289B, LMT record $230.4B, b:b ≈3.2×); band leg scored 07-24 on settled closes — **RTX +7.33% vs ±5.0%, LMT +10.54% vs ±5.4%, both outside** |
| **S10** | 07-24 | **FIRED-B** (scored 07-24 by the KR run) | Korea rate **12.5%**, inside the registered 12.5–15% band. KR-side; carried here only because it is the live example of **W5** (034220 vs 066570: same headline, opposite money) |
| **S12** | 07-23 (ECB) | ⚠ **PENDING — and now with a second, structural defect** | see 3b |
| **S8** | `[blank]` undated | ARMED | Date is not in `CATALYST_WATCH.json` and is deliberately **not guessed** |

**Zero silent skips. Zero `EXPIRED` rows this run.**

### 3b. ★ S12 — the observable has now failed to print for a second consecutive check

The ECB decision printed on 07-23 (**held at 2.25% with a hawkish tilt**; Lagarde: *"Some asked
whether we should consider a hike"*; market pricing a September hike). **But the frozen observable is
`DTWEXBGS`, and today's FRED pull returns `2026-07-17 = 120.5315` — byte-identical to the value at
registration, seven calendar days ago.** 120-day range measured today: **[117.4396, 121.412]**, i.e.
the registered range boundaries are confirmed unchanged.

⇒ **Still PENDING, not EXPIRED.** The registered re-check deadline is **2026-07-28**.

★ **New finding, and it is about the scenario's construction, not about the market** (companion to
**D35**, filed as **D46** below): a **3-session invalidation window was written on a series with a
~5-business-day publication lag.** The observable is *structurally incapable* of settling inside its
own window. This is the second independent defect in one scenario — D35 (branch grid written on two
axes, the actual outcome in neither) and now the lag mismatch. **Do not substitute a proxy** (rule
D5 / L3's own rule); if 07-28 arrives with no print, score `AMBIGUOUS` and record why.

### 3c. Still ARMED — and **six** of them stack on one date

| Date | Scenarios landing | Note |
|---|---|---|
| **2026-07-29** | **S2** (MSFT + META capex · FOMC · 000660 share-registration · governance reform) · **S9** (real-rate branch) · **S11** (KR FIN governance) · **S13** ★ · **S16** · **S18** | **SIX triggers.** Two of them (S11, S18) were produced by **no calendar** — found by hand |
| **2026-07-30** | **S14** (MA Q2 — the Financials-breadth test) · **S15** (June PCE — the frontal test of P1's framing) | |
| **~2026-08-11** | **S5** (KR semis exports 1–10 Aug) | |
| **~2026-09/10** | **S3** (4Q26 DRAM guide — *the only frontal falsifier of §1*) · **S4** (MU FQ4 + FQ1'27 guide) | |
| **07-29 → 08-05** | **S17** (SK hynix ADR premium) | Replaced S2's ADR leg, which had an unscoreable observable |

⚠ **S2's ADR row is SUPERSEDED and must not be scored as written** (R13): KSD's president, named and
on-record, states the conversion ceiling is **2.5%**, that 07-29 is a **share-registration** date, and
that *"because the ADR premium is so high there will be no conversion demand for the time being."*
**The 000660 flow suspension is EXTENDED, not lifted** — and per rule **D1**, the pre-07-29 series is
**not retroactively clean** whatever happens.

★ **The single most valuable thing this run inherits**: **S13 brackets the branch nothing else in the
book brackets** — *a capex raise the market prices as a margin drag anyway*. That branch has already
fired **once** in the wild (S1: GOOGL raised, stock fell) while the phrase `"capex cut"` appeared
**zero times in 24 hours** across the entire foreign feed (M46/C6). It cannot be anticipated from the
news axis. **PREMORTEM must not re-bracket it; it must check whether anything new has become
observable about it.**

---

## 4. Rejection-ledger audit — `due` run, not substituted

```
REJECT LEDGER — asof 2026-07-24 · 40 rows · 3 resolved · legacy (no revives_if) 21 · DUE 0
```

- **재확인일 도래/경과: 0 rows.** Nothing has a passed recheck date today. The four US rows filed
  2026-07-23 (**STNG** `A.flow미도착` · **MRK** `B.모멘텀only` · **HUM** `H.밸류소진` ·
  **CRWD** `B.모멘텀only`) all carry future recheck dates (07-31 / 08-06) — **not yet due, and named
  here so they cannot go missing.**
- ✅ **The legacy count is falling: 24 (07-23) → 21 (today).** The EXIT CHECK asks for exactly this —
  a legacy count sitting flat across runs is itself the next dig. It is not flat.
- ⚠ **Still-pending legacy audits, named rather than silently carried.** All 21 are **KR** rows, so a
  US-runtime desk cannot resolve them without a KR flow pull it has no business making today. **D42's
  designated priority four** — 000500 가온전선 · 161890 한국콜마 · 008930 한미사이언스 ·
  073240 금호타이어, all in the top-12 blocked-by-`vol_surge` list with RS20 +35~+62 — **carry into a
  second HANDOVER unresolved, and that is stated here as a process gap, not waved through.** ⚠ They
  are **not** a revival argument: those rejections were filed on **B-grade weak-hands actuals**, an
  axis the 🟢 gate never reads.
- **`score` (context only, never a gate)**: 30 scored rows · mean excess **+1.5pp** · **20 of 30 (67%)
  are |excess| ≤5pp = noise** · loss tail **+113.1pp vs gain tail −59.4pp**. By type: `narrative`
  **+12.0pp** (n=7) · `measured` **−0.9pp** (n=19) · `structural` **−5.6pp** (n=4).
  ⚠ **`narrative`'s number is still dominated by a single name (475150)** and every class has n ≤ 7.
  **This is sample accrual, not a verified edge (P4)** — it does not license a rule today.
  ⚠⚠ **Rule W1 binds here**: all 30 scored rows are **KR**-measured. **None of it transfers to a US
  rejection made this run.** **D27 stands: this run files ≥1 US row, with `--revives-if` and
  `--recheck-date`, at BET or ALPHA.**

---

## 5. Stale-check — every carry has an expiry

| Carry | `asof` | Status today |
|---|---|---|
| Every US price/flow/RS number in §1 | **2026-07-22 / 07-23 close** | ⚠ **1–2 sessions old and the 07-24 session is not open.** SWEEP must re-pull; do not reuse M37/M38/M39/M40 as if current |
| M32's crack decomposition | **07-23 intraday, incomplete bar** | ⚠ Must be re-pulled on the settled 07-23 close before any DEEP conclusion rests on it |
| M45's tanker 🔴 tags | 07-23, `module_flow` **including the incomplete bar** (D31) | The **RS numbers stand**; the **OBV / `vol_surge` do not** |
| `DTWEXBGS` | **2026-07-17** | 5 business days stale — the direct cause of S12's non-settlement |
| `NFCI` | 07-17 (weekly) | Within its publication cadence, not stale |
| 000660 flow suspension | opened 07-10 | **EXTENDED indefinitely** (R13/S17) — its expiry is now an **observable**, not a date |
| `data/cycles/cycle_registry.json` | `updated: 2026-07-17` | **7 days stale** — the GAP guard can only see cycles someone wrote down (D20) |
| `REPORT/industry_US/` | undated | ⚠ **Not date-partitioned (D33)** — `SECTOR_DEEP_INDU/SEMI/UTIL.md` from *earlier* runs sit alongside today's and enter the ledger with equal authority |

**Cleared suspensions converted into dig items**: none cleared today. The one suspension with a
calendar expiry (000660 / D6) had that expiry **voided**, so it converts into **watching S17's
observable**, not into a re-pull.

---

## 6. RESEARCH triggers — loaded as binding constraints, grouped, with the stages they bind

| Group | Fires when | IDs | **Binds this run's** |
|---|---|---|---|
| **C** | you cite a number | C1 baseline·C2 both halves·C3 unknown column·C4 "indistinguishable"·C5 arbitrary choice | **MACRO · SWEEP · ROTATION · DEEP · BET · ALPHA — every stage** |
| **S** | you make a statistical claim | S1 date-fold·S2 diagnose the null·S3 power first·S4 in-sample≠done·S5 short samples·S6 future labels | **SWEEP · ROTATION · DEEP · PREMORTEM** (any stage quoting a breadth count or a t) |
| **D** | you read data | D1 second venue·D2 proxy sign·D3 signed vs unsigned·D4 regime contamination·D5 cross-provider·**D6 signal grade** | **SWEEP · DEEP · ALPHA** (and every `module_flow` / FINRA / COT read) |
| **W** | you write a conclusion | W1 cross-market transfer·W2 inherited lead/lag·W3 real≠profitable·W4 name the customers·W5 sub-sector dispersion·W6 reader's-market spine | **ROTATION · DEEP · BET · EVENT_ALPHA** |
| **L** | lenses, not triggers | L1 second derivative·L2 peak-margin trap·L3 branch information content | **DEEP · PREMORTEM** |

**The five that will fire hardest today, with the number that makes each concrete:**

1. **C1 — name the benchmark in the same sentence.** The KR run measured this rule's own failure mode
   yesterday: `RS20 vs ^KS11` was positive on **91.3% of 828 names, median +18.3**, so four stages
   cited an automatic arithmetic as a signal (**D41**). The US universe has no equivalent measured
   baseline — **SWEEP must produce one** (universe-median RS20/RS60 vs SPY and a percentile) before
   ROTATION ranks anything on it.
2. **D6 — grade before you cite.** **OBV is C-grade**: r ≈ 0.49 vs real flow, **no leading power
   (t = 1.00)**. It may corroborate; it may **never** carry a proposition or override RS20/RS60 (A).
   And on the US path there is **no investor feed at all**, so short-pressure + COT percentile are
   **context, never a trigger** — the protocol says so in its own runtime deltas.
3. **W5 — state the dispersion.** The desk has now measured this shape **three times**: RE (18.2pp,
   two independent dates) · Industrials (0.705 → **0.285**, decayed 60% in two sessions, M36) ·
   **IT, the only one still carried as a single label** (C8/S13).
4. **W4 — name the customers.** Closed 4 of 5 for the refiners (M34: DAL/UAL/FDX/LUV, fuel +66~84%
   YoY, two cut guidance). **UPS prints 2026-07-28 and is still unread.**
5. **S1 — fold by date.** Six Health Care greens on one date is **n ≈ 1**, not n = 6. The same
   arithmetic killed a t of +6.55 → −0.74.

---

## 7. Reconciliation — belief vs coverage

Ledger: **29 reports · 168 tickers · 11 sectors**, refreshed 2026-07-24T09:30 KST.

| Class | Names | Reading |
|---|---|---|
| **Belief with no coverage** | none material on the US side | Every US name carrying a standing thesis has ≥3 reports |
| **Heavy coverage, no standing thesis** | **INTC (9 reports)** · **META (10)** · **AVGO / NVDA (7 each)** | ★ **INTC is this run's clearest instance.** It is the desk's 3rd-most-covered name, it just settled the *only* scenario keyed to the equipment leg (**S6 FIRED-A**), and STANDING_VIEW §3 has **no INTC row** — the equipment thesis is filed under AMAT/LRCX/KLAC instead. NVDA/AVGO carry an explicit "separate boat, do not fold into a memory verdict" note, which is a **guard**, not a thesis |
| **Resolved-but-live** | **LRCX · KLAC · MSFT** all tagged `RESOLVED` while carrying live theses | Re-justify or retract at DEEP. ⚠ Contaminated by **D33** — the tag may come from a `SECTOR_DEEP_*` file written **three rotations ago** |
| **Coverage the ledger over-credits** | `industry_US/SECTOR_DEEP_SEMI.md` (2026-07-15) · `SECTOR_DEEP_UTIL.md` (07-15) · `SECTOR_DEEP_INDU.md` (07-22) | 9 and 2 days old respectively, sitting undated in `REPORT/industry_US/` next to today's output |

---

## 8. Dig list, ranked for **today's US run**

| Rank | Dig | Why it is #n today | Owner stage |
|---|---|---|---|
| 1 | **D18** — the calendar misses the day's biggest binary | **4th consecutive occurrence**, and a `--days 10` pull did **not** fix it ⇒ the defect is **source coverage of single-name earnings and central-bank decisions**, not window length. Six triggers now stack on 07-29, **two of which no calendar produced** | **MACRO** — pull `--days 10` *and* hand-check next-week single-name earnings + CB decisions |
| 2 | **D31 / D43** — the two `module_flow` paths disagree about the date *and* the verdict | The session is not open. Anything built on a pre-close `vol_surge`/OBV today is built on ~0% of a day | **SWEEP**, every stage citing a tag |
| 3 | **C1 baseline for the US universe** (the US analogue of **D41**) | KR measured that beating its benchmark was ~automatic (91.3%). **Nobody has measured whether the US universe has the same defect.** One line in SWEEP settles it | **SWEEP** |
| 4 | **D42 / D11** — the 🟢 gate is a volume test | Now measured in **two independent markets** (US M25/M38: 68 of 93 blocked by `vol_surge` alone; KR M55: 191 of 240, 100% by `vol_surge`). ⇒ **code structure, not a market quirk.** ⚠ Needs human approval; handle at the interpretation layer via D6 | SWEEP / ROTATION (interpretation) · human (code) |
| 5 | **D27** — file ≥1 **US** rejection row | 30 scored rows and **all of them KR**. Rule W1 says none of that transfers | **BET / ALPHA** |
| 6 | **D23 (5th of 5)** — **UPS prints 2026-07-28** | W4's last unread refiner customer. Not actionable today; carried so it is not re-discovered | DEEP (next run) |
| 7 | **D30** — Brent provider disagreed **with itself** (`BZ=F` 86.72 vs WTI 91.37; Brent = WTI's prior close exactly) | The Energy thesis rests on this series and D5's cross-check cannot detect a source disagreeing with itself | MACRO |
| 8 | **D33** — `REPORT/industry_US/` is not date-partitioned | Directly contaminates §7's reconciliation, i.e. the object every downstream desk queries first | human |
| 9 | **D20** — cycle registry 7 days stale, and has **no AI-security row** | The GAP guard cannot fire against a 0% book exposure to a cycle nobody wrote down — and that theme carried the board's cleanest live momentum (M28) | PREMORTEM |
| 10 | **D1 / D3 / D8 / D22** — the standing `[inferred]` mechanism claims | Each is one correlation table to test and expensive to keep assuming (W2). D22 in particular is tagged `[unverified]` and **may not be cited as evidence** | DEEP |

**New dig registered by this stage:**

| # | Dig | Why it matters | Owner |
|---|---|---|---|
| **D46** | **S12's invalidation window (3 sessions) is shorter than its observable's publication lag (~5 business days).** `DTWEXBGS` has not advanced since 2026-07-17 — it read 120.5315 at registration and reads 120.5315 today, so the bracket cannot settle inside its own window by construction | A scenario that **cannot** be scored on time is a registration defect of the same class as **D35** (branch grid on two axes) and **D28** (a price reaction inside an observable's branch). ⇒ **Registration rule: check the observable's publication cadence against the invalidation window before freezing it.** Daily-printing observables (S17's ADR premium) are the pattern that works | PREMORTEM (registration discipline) |

---

## ✅ EXIT CHECK

- [x] `STANDING_VIEW.md` · `SCENARIOS.md` · `RESEARCH.md` all read; `module_report_tags show`
      cross-queried (§7) so belief and coverage are reconciled rather than duplicated.
- [x] **Retracted ledger read before today's view formed** (§2, placed ahead of every downstream
      instruction). R7/R10/R11/R12 surfaced verbatim with the measurements that killed them.
- [x] **Every past-dated scenario scored or explicitly resolved** (§3a): S1·S6·S7·S10 FIRED,
      S12 **PENDING with its reason and its 07-28 deadline stated**, S8 undated by design.
      **Zero `EXPIRED`. Zero silent skips.**
- [x] **`reject_ledger.py due` run this HANDOVER** (§4), not substituted with `score`. 0 rows due;
      **21 legacy rows named as still-pending, with D42's priority four called out by name**;
      legacy count reported and **falling, 24 → 21**.
- [x] Stale rows flagged with their `asof` (§5); the one suspension whose date arrived had that date
      **voided** (R13) and converts to an observable (S17), not to a silent trust.
- [x] `[measured]` / `[inferred]` tags preserved (§1); the five `[inferred]` carries named explicitly
      as **not admissible as evidence**.
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W + L**, with the stages each
      group binds (§6) — not summarized.
- [x] `HANDOVER.md` written. `handoff/*.md` update deferred to run end, per the stage spec.
- [x] **No position sizing, no buy/sell language.**

> ✅ EXIT CHECK passes → advance to MACRO.
