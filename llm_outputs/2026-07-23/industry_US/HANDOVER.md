# HANDOVER — industry_US · 2026-07-23

> Stage 0/9 of protocol `industry_us`. Inherits the analytical carry (`handoff/*.md`) BEFORE any view
> is formed this run. Analysis only — zero buy/sell language (P4).

**Run clock (binds every stage below)**: started **2026-07-23 22:09 KST = 09:09 ET**.
The US regular session **has not opened** at run start (09:30 ET). Consequences, stated once:

1. **Every US price/flow number in this run is the 2026-07-22 close.** No stage may describe a
   07-23 move; if one does, it is fabricating.
2. **RTX and LMT printed pre-market this morning; INTC prints after today's close.** The earnings
   *lines* are readable now; the *price reactions* are not. See S7 scoring below.

---

## 1. Inherited standing view (from `handoff/STANDING_VIEW.md`, asof 2026-07-23)

### Regime call — carried unchanged
**"Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight."**
`[inferred]`, built on M1–M6. Carried, not re-derived. Nothing in the 07-22→07-23 window touches the
contract-price series (M1), which is the only thing that could move it (see S3).

### Measured chain carried (29 rows) — the ones that bind this run
| # | Fact | Tag | asof | Stale? |
|---|---|---|---|---|
| M20 | US long-end move is **real rate, not inflation** — real 10y **2.35% = 120-day high**, ~79% of the nominal move | `[measured]` | 07-20/21 | ⚠ **3 days old — MACRO must re-pull** |
| M21 | No credit confirmation — HY OAS **2.69%**, IG 0.78%, NFCI −0.538 loosening | `[measured]` | 07-20 | ⚠ **3 days old — MACRO must re-pull** |
| M22 | 3-2-1 crack **$68.23/bbl = 99.5th pctile of 3y**; rate series fired two consecutive declines before the 07-10 truce collapse overwrote it | `[measured]` | 07-21 | 2d |
| M23 | Refiner consensus cliff FY26→FY27: VLO −31.6% · MPC −25.8% · **PSX −7.2%** | `[measured]` | 07-22 | 1d |
| M24 | Three "underweights" (IT/RE/UTIL) are **narratively** one AI-datacenter exposure — ⚠ **strong form killed by R10** | `[measured]` sub-numbers | 07-21 | 2d |
| M25 | The US 🟢 tag is a **volume-surge count, not a flow count** — `vel` is None on all 300 US rows, so 🟢 = OBV ∧ RS20>0 ∧ vol_surge≥1.2; **99 of 300 blocked by `vol_surge` alone** | `[measured]` | 07-22 | 1d · **binds SWEEP** |
| M26 | Industrials = 5 primes (wflow **+0.250**, zero reds) vs capital goods/electricals (**−0.455**, 14 of 17 reds); spread **0.705** | `[measured]` | 07-21 | 2d |
| M27 | Bank credit costs falling from the borrowers' books (KEY/TFC/MTB/WFC/USB/ALLY/UCB) | `[measured]`, lagging Apr–Jun | 07-16~21 | 2–7d |
| M28 | Security/observability carries the cleanest live momentum: DDOG **+93.7** · PANW +91.9 · FTNT +85.4 · CRWD +66.0 RS60 vs SPY, all with positive RS20 | `[measured]` | 07-21/22 | 1–2d |
| M29 | **GOOGL FY26 capex raised to $195–205B** (2nd consecutive raise); Q2 capex $44.9B **+100% YoY**; "supply-constrained environment" | `[measured]` | 07-22 AMC | fresh |

### Per-name theses carried (US names only — this is the English-pure runtime)
`MU/SNDK/WDC` · `NVDA/AVGO` (**separate boat — do not fold into a memory verdict**) ·
`VLO/MPC/PSX` · `GS` (+ MS/IBKR same shape; **C is the only genuinely broken bank**) ·
`PANW/CRWD/FTNT/DDOG` · `AXON` (**not a defense name** — carried only so R9 cannot resurface).

KR names in the carry (005930 · 000660 · 042700 · 009150 · the energy four · 068270/207940) are read
and **not cited** — market-tagged to `industry_kr`, and W1 forbids transferring a signal across its
market of measurement.

---

## 2. Retracted ledger — read BEFORE forming today's view (this is the point of the stage)

R1 · R2 · R3 · R4 · R5 · R6 · R7 · R8 · R9 · R10 all read. **Five bind directly on stages this run
is about to execute** — recorded here so a downstream stage cannot re-derive them:

| # | Killed claim | Which stage would re-derive it, and what it must do instead |
|---|---|---|
| **R7** | *"Real Estate is the purest duration expression on the board"* | **ROTATION.** The RE reds are digital infrastructure (AMT/EQIX/DLR/CCI); the duration REITs are **bid** (WELL +16.0, VTR +17.0 RS20 vs SPY). An RE underweight written on a rate rationale is re-writing R7. |
| **R10** | *"IT + RE + UTIL are ONE risk concentration"* | **PREMORTEM.** Measured refutation: 699 trading days of SPY-residual correlation puts them in **four** units; DLR–NVDA +0.049, EQIX–NVDA **−0.118**. Only the **weak form survives**: they share one *catalyst* (hyperscaler capex) ⇒ **event concurrency, not correlation concentration**. ⚠ C4 — "not supported", never "rejected". |
| **R9** | *"AXON is the most accelerating defense name"* | **PREMORTEM/DEEP.** Primary source killed it: no customer >10% of sales, municipal/state buyers, **the word "backlog" is absent from the 10-K**, FY26 estimate **cut 1.24%** while price outran SPY 24.6pp. Today's RTX/LMT prints and the $87.6bn supplemental **do not transmit to it**. |
| **R8** | *"PSX is the cheapest large refiner on forward"* | **DEEP/BET.** False like-for-like: MPC 8.8x · VLO 9.4x · **PSX 10.8x**. The surviving PSX argument is M23's **−7.2% cliff**, not cheapness. ⚠ `core_pick` is **human-locked** — no stage may rewrite that field. |
| **R5** | *"EDA leads semis by 12–18 months"* | Any stage reaching for a leading indicator. Same-month **+0.63**, lag-12 **+0.05**. **Coincident.** |

---

## 3. Scenario scoring — every past-dated row settled or explicitly named

`SCENARIOS.md` carries S1–S11. Status at this run's clock:

| ID | Event date | At run clock | Verdict this HANDOVER |
|---|---|---|---|
| S1 | 07-22 AMC | past | **FIRED-A** — already scored at the 07-23 `industry_kr` HANDOVER. Not re-scored. |
| **S7** | **07-23 pre-market** | **event occurred** | **★ SCORED IN PART — see below** |
| **S6** | **07-23 AMC** | **not yet occurred** (INTC prints ≈16:00 ET) | **ARMED — stays armed.** Not EXPIRED: the date is today and the event is in the future at run time. Must be scored at the **next** HANDOVER; if it is not, that is the process failure. |
| S10 | 07-24 | future (D−1) | ARMED |
| S2 · S9 · S11 | 07-29 | future (D−6) | ARMED |
| S8 | `[blank]` undated | — | ARMED · undated by construction |
| S3 | ~09/10 | future | ARMED |
| S4 | ~09 late | future | ARMED |
| S5 | ~08-11 | future | ARMED |

**Zero EXPIRED rows this run.**

### ★ S7 — RTX + LMT · scored on its frozen observable

Frozen observable at registration (2026-07-22 PREMORTEM): **backlog / book-to-bill at *both* names.**
Branch A additionally required **both to move outside their implied bands** (RTX ±5.0%, LMT ±5.4%).

**Observable pulled (07-23 pre-market prints):**

| Name | Backlog | Orders / book-to-bill | Guidance |
|---|---|---|---|
| **RTX** | **$289B** (commercial $170B + defense $119B), from **$271B** carried into the print | — | **Raised**: FY26 adj. revenue to **$95–96B** from a prior ≤$93.5B ceiling. Q2 sales $24.7B **+14% YoY**; non-GAAP EPS $1.89 (beat $0.23) |
| **LMT** | **$230.4B — a record** | **$65B of new orders in the quarter** on $20.1B of sales ⇒ book-to-bill ≈ **3.2×** | **Raised**: FY26 sales to **$79.75–81.75B** from $77.5–80.0B; FCF now >$7B; Missiles & Fire Control **+19%** on PAC-3/THAAD/PrSM ramps |

**Verdict: `FIRED-A` on the backlog leg — unambiguous.** Backlog is up at both, both raised FY
guidance, and LMT's book-to-bill is not marginal.
**The band leg is unresolvable at this run's clock** — the US session had not opened. It is scoreable
only against the **07-23 close**, i.e. at the next HANDOVER.

⚠ **This is a finding about the scenario's construction, not about the market** (L3 rule).
S7 mixed an *observable* (backlog) with a *price reaction* (the implied band) inside one branch
condition — and the very same L3 unit that scores it says **"score the observable, not the price
reaction."** The scenario contradicted the scoring rule at registration. Recorded as a registration
defect to fix in future PREMORTEM brackets: **bands belong in a separate, explicitly-labelled
reaction test, never inside the observable's branch condition.**

**Meaning for the standing view**: the *sector* half of the 07-22 PREMORTEM promotion (M26 — five
primes carrying positive flow with zero reds against a −0.455 capital-goods complex) receives direct
fundamental confirmation from the two largest primes. ⚠ **This does not revive R9** — AXON's 10-K
has no backlog line and no >10% customer, so a primes backlog record is precisely the datum that
*cannot* transmit to it. Two separate things: the primes node is confirmed; the name R9 killed stays
killed.

⚠ **Two data traps hit while pulling this observable, both logged:**
- A `nasdaq`/Zacks article dated **today** in the feed reports *"quarterly earnings of $1.41 … quarter
  ended June 2024 … revenues of $19.72 billion"* — a **recycled 2024 template republished under a
  2026 date**. It contradicts the actual $24.7B/+14% print. Any stage that quotes a Zacks-syndicated
  "Q2 Earnings and Revenues Surpass Estimates" body must check the quarter label inside the text.
- The genuine prnewswire press releases for both names were **not yet in the FTS index** at run
  clock (fetch is hourly; the prints landed ≈06:30 ET). The numbers above came from the news feed
  plus a web cross-check, and are tagged accordingly.

---

## 4. Rejection-ledger audit (`reject_ledger.py due`, run this HANDOVER — not substituted)

```
전체 25건 · 해소됨 2건 · 부활조건 없는 레거시(감사 필요) 22건 · 재확인일 도래/경과 0건
```

- **Recheck-date due/overdue: 0.** Nothing has a passed `recheck_date`.
- **Legacy (no `revives_if` ever set): 22** — down from **24** at the 2026-07-23 `industry_kr` run,
  which closed two (both 475150 SK이터닉스, `resolve --outcome revived`). ✅ **The legacy count is
  moving, not flat** — that is the only real evidence this practice is taking hold, and it is the
  check the L2 explicitly says not to substitute with a quiet pass.
- ⚠ **All 22 legacy rows are KR tickers.** This is the English-pure US runtime; re-pulling KR flow
  here would (a) import the Korean frame the protocol exists to keep out and (b) duplicate work the
  `industry_kr` desk owns. **Named as still-pending, not silently carried**: the audit queue belongs
  to `industry_kr`, and the next KR HANDOVER should close ≥1 more.
- **Structural note carried forward**: this US desk has **never** entered a row in the ledger — every
  one of the 25 is KR. A US desk that rejects candidates every run (SWEEP cuts 300 names to a
  shortlist; ROTATION cuts 11 sectors to 4) and logs **zero** rejections is not disciplined, it is
  unmeasured. Registered below as **new dig D27**.

---

## 5. Stale-check and cleared suspensions

| Item | State | Action this run |
|---|---|---|
| **M20/M21 macro block** (real 10y, breakeven, HY/IG OAS, NFCI) | asof **07-20**, 3 days old | ⚠ **MACRO must re-pull** — S9's kill line (real 10y >2.55%) and S2 branch C both key off a series the carry has stale. Do not cite 2.35% as current. |
| **000660 flow read** | SUSPENDED until **2026-07-29** | Still suspended; **not** a dig yet. Becomes one on 07-30 (dig D6). Not this desk's name in any case. |
| **`^KS11` 07-22 close disagreement** (D24) | unresolved | KR-only. No US calculation touches it. |
| **Estimate snapshot series** (D16) | day 1/~40 stored, started 07-22 | Not yet usable as a time series. Any IC cited this run is still **single-date, effective n=1** (S1). |
| M22 crack, M23 cliffs, M24–M28 | 1–2 days | Usable; SWEEP/ROTATION should refresh M24/M26 from today's own sweep rather than quoting the 07-21 aggregation. |

---

## 6. RESEARCH rules loaded as binding constraints — which group binds which stage

Loaded from `handoff/RESEARCH.md` (21 triggers + 3 lenses). **Not summarized — carried as gates:**

| Group | Fires when | IDs | Binds, this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO** (C1/C2 on every FRED and every export/CPI print) · **every stage** |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **SWEEP · ROTATION · PREMORTEM.** ★ S1 is the live one: today's US session is **one date** — an 18-of-18-green style observation is **n≈1** |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade** | **SWEEP · ALPHA.** ★ **D6 + M25 together are the hardest gate this run**: the US 🟢/🔴 tags are OBV-derived (**C-grade**) *and* the 🟢 gate is really a volume-surge gate. A 🟢/🔴 tag may **corroborate**; it may not carry a proposition, and it may not override RS20/RS60 (**A-grade**) |
| **W** | you write a conclusion | W1 market of measurement · W2 lead/lag tested-or-tagged · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion | **ROTATION · DEEP · BET.** ★ W5 is pre-armed by M26 (Industrials is two opposite things) and M24 (Real Estate is two opposite things). ★ W4 is pre-armed by D23 — three refiner customers already printed and were never read |
| **L** | lenses | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM** |

**Specific pre-commitments carried into this run's stages:**
- **PREMORTEM must produce a both-sides bracket** for any binary ≤48h. At this clock that is
  **INTC tonight (S6)** and **USTR 07-24 (S10)** — and the 07-29 cluster sits at D−6, just outside.
  A one-way tilt into any of them is a protocol violation.
- **D26 fires immediately**: MACRO's default `catalyst_calendar --days 5` **cannot reach 07-29** from
  07-23. Pull **≥10 days** — this exact gap is what hid S11 for a week of runs.
- **C1 in every RS sentence**: name the benchmark inline. The US desk's benchmark is SPY; the sign
  flips against other bases (R4).

---

## 7. Reconciliation — belief vs coverage (`module_report_tags show`, 26 reports · 136 names · 13 sectors)

| Class | Names | Read |
|---|---|---|
| **Belief with no coverage** | *(none this run)* — every US name in STANDING_VIEW §3 has ≥3 reports | Healthy |
| **Coverage with no standing thesis** | **AMAT · LRCX · KLAC** (4 reports each, verdicts `GO LIVE 🔴🟡🟢`, last seen `industry_KR/HANDOVER.md`) · **MRVL** (2) · **STT · PYPL · HUM · UNH · NOC · GD · USB** (3–4 each, all last seen in `industry_US/ACTION_TICKETS.md`) | ⚠ **The semicap trio is the live gap.** Four reports each and **no per-name thesis in STANDING_VIEW** — while **S6 (INTC, tonight) is registered specifically as the equipment-leg test** and its branch A says *"the IT underweight is short the wrong thing."* Carrying a sector underweight over a node with coverage but no thesis is the shape that produced C2 in the KR book |
| **Resolved-but-live** | none flagged | — |

**Consequence for this run (a HANDOVER instruction, not a verdict):** ROTATION and PREMORTEM must
treat **semicap (AMAT/LRCX/KLAC)** as an owned question, not a residual of the IT label. It has the
coverage; it lacks the belief; and tonight's print is its registered test.

---

## 8. Dig list ranked for today (from RESEARCH.md Part C, re-ordered for this run)

| Rank | Dig | Why it is today's | Owner stage |
|---|---|---|---|
| **1** | **D26** — widen `catalyst_calendar` to ≥10 days | Mechanical, free, and 07-29 (five stacked events) is unreachable at 5 days from 07-23 | MACRO, this run |
| **2** | **D23** — refiner customers printed and were never read (DAL 07-10, UAL 07-16, FDX 06-24; **LUV prints 07-23**, UPS 07-28) | W4 is armed and the prints already exist. Cheapest omission on the list | DEEP |
| **3** | **D20** — cycle-registry defects; no AI-security row exists, so **no GAP can fire** against a 0% book exposure to the board's fastest thread (M28) | The anti-tunnel backstop can only see cycles someone wrote down. ⚠ registry edits need a human | PREMORTEM (flag) / human |
| **4** | **D3** — hyperscaler capex → memory revenue lead-lag, tested the way W2 demands | M29 just added a second consecutive capex raise. The capex→memory link is the standing view's load-bearing `[inferred]` joint and has never had a lag table | DEEP |
| **5** | **D22** — "BOJ tightening leads US long-end yields" has no lag table; `[unverified]` under W2 | It is the carried explanation for M20's real-rate move, and W2 exists because exactly this claim class was wrong last time | MACRO |
| **6** | **D1** — do LTA price floors actually hold margin? | C1's open contradiction and the best counterargument on file against the regime call | DEEP |
| **7** | **D12** — borrow fee & utilization, not just short balance | US flow is short-pressure + COT only (no investor feed); we measure size, not scarcity | ALPHA |
| — | **D9 · D10 · D11 · D15 · D17–D21 · D24 · D25** | **Open code/registry defects needing human approval** — carried forward, not re-discovered. ⓘ **D17 appears CLOSED**: `drift` is now present in `module_news_data.__main__.DB_READ_CMDS`. DRIFT stage must verify it actually executes remotely before the fix is declared | human |

### New digs registered by this HANDOVER

| # | Dig | Why | Owner |
|---|---|---|---|
| **D27** ★ | **The US desk has never entered a `reject_ledger` row.** All 25 entries are KR. Every US run drops ~296 of 300 swept names and 7 of 11 sectors, and logs none of it | The ledger's whole finding — that **rejection is asymmetric** (loss tail +83.8pp vs gain −38.4pp) — was measured on KR data only. The US book's rejections are entirely unmeasured, so no US reason-class has any score. Fix is procedural: BET/ALPHA enters ≥1 US rejection per run with `--revives-if` + `--recheck-date` | BET / ALPHA |
| **D28** | **S7's registration mixed an observable with a price reaction** inside one branch condition, contradicting L3 `scenario_score`'s own "score the observable, not the price reaction" rule | It made a clean fundamental result (backlog record at both names) unscoreable as a whole branch. Future PREMORTEM brackets: implied-move bands go in a **separate labelled reaction test** | PREMORTEM |
| **D29** | **Zacks/nasdaq-syndicated earnings bodies can carry a recycled prior-year template under a current date** — measured today on RTX (`$1.41 EPS, quarter ended June 2024, $19.72B` vs the actual `$1.89, Q2'26, $24.7B`) | The desk reads news bodies as primary-ish evidence. A body that is internally dated two years stale and externally dated today defeats every freshness check the pipeline has | module_news_data / any stage quoting a body |

---

## 9. EXIT CHECK

- [x] `STANDING_VIEW.md` · `SCENARIOS.md` · `RESEARCH.md` all read; `module_report_tags show`
      cross-queried (§7) — belief vs coverage reconciled, one gap named (semicap).
- [x] **Retracted ledger read before forming today's view** (§2); R5·R7·R8·R9·R10 mapped to the
      specific stages that would otherwise re-derive them.
- [x] **Every past-dated scenario settled**: S1 already FIRED-A; **S7 scored FIRED-A on its frozen
      observable**, band leg explicitly deferred to the 07-23 close with the reason. **Zero EXPIRED.**
      S6 stays ARMED because its event is still in the future at run clock (INTC prints AMC).
- [x] **`reject_ledger.py due` run** (§4) — 0 due, 22 legacy, count **shrinking 24→22**; the legacy
      queue is named as still-pending with its owner (`industry_kr`), not silently carried.
- [x] Stale rows flagged with `asof` (§5); no suspension has cleared (000660 clears 07-29).
- [x] `[measured]`/`[inferred]` tags preserved; no `[inferred]` claim passed downstream as evidence.
      M20/M21 flagged stale so MACRO re-measures rather than inherits.
- [x] RESEARCH triggers loaded as binding constraints, grouped C/S/D/W + L, with the stage each
      binds (§6) — plus three run-specific pre-commitments.
- [x] `HANDOVER.md` written. `handoff/*.md` write-back is scheduled for **run end** (per stage spec).
- [x] No position sizing, no buy/sell language anywhere in this file.
