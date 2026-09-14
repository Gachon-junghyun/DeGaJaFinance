# BLINDSPOT_PREMORTEM — industry_US — 2026-07-29 (Wed) ★US-only

> Four adversarial lenses argue **AGAINST this run's own tilt** before the deep budget is committed.
> Draft tilt (post-ROTATION): **ENRG OW− · FIN OW− · INDU OW (promoted) · IT N− · MATR UW− ·
> HLTH N · COMM N− · UTIL N− · RE N · DISC N− · STPL N.** DEEP set as handed in: **ENRG · FIN · INDU.**
> Flow tags from `SECTOR_FLOW_US.json` **asof 2026-07-28 settled**. Benchmark **SPY** inline (C1).

## ⚠ 0 · Method limitation, stated at the top rather than buried

**This session's configuration does not permit spawning subagents unprompted**, so the four lenses ran
**in-line and serially** rather than as a parallel fan-out. Following the precedent the 2026-07-29
`industry_kr` run set and documented, **the adversarial function was preserved by ordering**: each lens
was run against a number written by an earlier stage of **this** run and required to re-measure rather
than inherit it. **Three of this run's own claims were attacked below and two changed.**
⚠ **What is NOT recovered is independence — every finding here carries one layer of checking, not
two**, and the brackets registered below are less independently verified than a fan-out run's.

## ⚠ 0b · A second instrument caveat, binding on every number in Lens 3

The `module_flow --positioning` calls in this stage ran at **~09:5x ET, inside a live session**. Their
**RS / OBV / `vol_surge` columns are live-contaminated** — the exact defect the 07-27 run measured when
two PREMORTEM agents returned **STX RS60 +22.9 against a settled +43.3**. Verified again here: the live
call returned **STX RS20 −19.1 / RS60 +3.5** against the settled **−22.8 / +7.8**.
⇒ **Only the ⑤⑥ positioning block (short balance, P/C, skew, implied move) is used from those calls.**
Every RS number in this file comes from the settled `SECTOR_FLOW_US.json`.

---

## LENS 1 — UNDER-COMPUTED LEGS

*The strongest bull case for a sector or sub-leg we did NOT deep-dive that has a catalyst ≤~5 trading days.*

### ★ Leg A — **Utilities, the REGULATED half. Verdict: PROMOTE-TO-DEEP (4th slot).**

**The catalyst density is the argument.** **Six of the seven names S35 brackets print inside 48 hours
— WEC · ETR today, EXC · SO · XEL · AEP tomorrow, D on 07-31 — and NOT ONE of them appears in
`CATALYST_WATCH.json` at `--days 10`.** ROTATION held **UTIL N−** on flow (wflow −0.265 / eqflow
−0.270, 1🟢/6🔴) **with no calendar awareness of any of them.**

**The bull case, made properly:**
- **S35's branch A explicitly falsifies this desk's own verdict**: *"the sector's flow collapse
  belonged to the AI-power leg and the desk demoted the regulated leg with it — a W5 label collapse of
  exactly the shape M26/M174 measured inside Industrials."* **The desk has now measured that shape
  twice and is carrying a third instance unexamined.**
- **The two legs are measurably different animals.** AI-power four: **VST −8.4 / −8.9 · CEG +0.2 /
  −20.1 · GEV −14.4 / −16.0 · VRT −12.2 / −21.0** (RS20 / RS60 vs SPY) ⇒ **median RS20 −10.31.**
  Regulated seven: **WEC −4.1 · ETR −3.4 · EXC +0.4 · SO 0.0 · XEL −2.0 · AEP −3.6 · D +2.1**
  ⇒ **median RS20 −2.0.** ★ **An 8.3pp gap inside one 15-name sector.**
- ★ **And one name inside the regulated seven is not behaving like the rest: `D` (Dominion) —
  RS20 +2.1 AND RS60 +6.4, the only one positive on both windows, with OBV 매집** and the sector's
  lowest `vol_surge` (0.48), i.e. **accumulation on no volume.** It prints **07-31**.
- **PCG** — Utilities' only 🟢 and a `new_green` (flow +0.722, `vol_surge` 1.46) — is also regulated,
  **and its next print is not until 2026-10-22**, so it cannot be the thing the sector is trading.

**Named tickers**: `D` · `PCG` · `EXC` · `SO` (the four with RS20 ≥ 0 or a green tag) against
`AEP` · `WEC` · `ETR` (the three 🔴). **Dated catalysts**: **07-29 WEC/ETR · 07-30 EXC/SO/XEL/AEP ·
07-31 D.** **Bracket already registered: S35, window to 2026-08-07.**

⇒ **DEEP set updated: ENRG · FIN · INDU · UTIL.** ROTATION correctly refused to *pad* to four with a
UW sector; this is not padding — it is a promotion carried by six dated binaries inside 48h and by an
8.3pp measured intra-sector gap.

### Leg B — **Real Estate / the data-centre node. Verdict: WITHIN-RUN-WATCH (not promoted).**

**EQIX prints 2026-07-30** and it is **S25's registered second settling point**. Its instrument is
unusually informative: **implied ±9.4% with expiry 2026-08-21 (D23) — it COVERS the event** (one of
only two event-covering straddles on the board, the other being STNG ±9.7%), and its **P/C OI is
4.25**, i.e. heavy put positioning into the print. Flow: **🔴분산 −0.58, RS20 −4.6 / RS60 −7.5.**
**Not promoted** because S25 already owns the observable on a frozen threshold to 08-08 and a DEEP
would re-derive it. **Watch: EQIX's print against DLR RS20 +1.4 vs the {PLD, AMT, WELL} median +5.9.**

### Leg C — **Consumer Staples. Verdict: WITHIN-RUN-WATCH, and the reason is uncomfortable.**

**XLP was the 3rd-best 5-day sector (+3.57%)**, its eqflow (+0.032) exceeds its wflow (−0.074), and
**5 of 19 names pass `OBV-매집 ∧ RS20>0` with 5 of 5 blocked by `vol_surge` alone** (CCEP 0.98 · ADM
0.97 · KO 1.00). ⇒ **the same gate artifact ROTATION diagnosed in Energy and Materials.**
**Not promoted, and the honest reason is that the desk has no proposition, no bracket and no thesis on
Staples at all** — there is nothing for a DEEP to attack. **That absence is the finding**, and it is
logged rather than converted into a view. **No catalyst ≤5 days.**

### Leg D — **Health Care. Verdict: WITHIN-RUN-WATCH, resolved by its own registered horizon.**

XLV +4.37% over 5 days (2nd best), eqflow +0.241 > wflow +0.162, **ABT RS20 +15.7 / RS60 +15.1.**
**C7's registered observable — one 🟢 from OUTSIDE the top-6 by cap — reads ZERO for a 4th run**
(the one green, TMO, is inside the named block). **Resolves 2026-08-06 on its own terms. No catalyst
≤5 days on the board.**

---

## LENS 2 — REGIME-FLIP / BOTH-SIDES

*For every known binary in `CATALYST_WATCH.json`, the against-us branch: what rips, which OW gets hit,
starter list + trigger + invalidation.*

### 2a · Binaries ALREADY bracketed both ways — no new bracket, stated so the coverage is auditable

| Binary | Date | Bracket | Against-us branch, in one line |
|---|---|---|---|
| **FOMC** | 07-29 14:00 ET | **S9 · S19 · S23** | **S23-B** (hold + further flattening) — **T10Y2Y +0.34, 0.14pp from the trigger and moving toward it.** Hits **FIN OW−** on both remaining legs; **UTIL UW loses on the same tick** ⇒ one rate bet with opposite signs |
| **META** | 07-29 AMC | **S13 · S16 · S24** | implied **±8.1%** (expiry 07-31, **D2 — covers the event**), P/C 0.65, skew **−26.4**, short 1.7% float **building** |
| **MSFT** | 07-29 AMC | **S13 · S24** | implied **±7.2%** (D2, covers), P/C 0.75, skew 0.0, short 1.2% **covering** |
| **STX** | 07-29 AMC | **S30** | implied **±13.4%** (D2, covers), P/C **1.26**, short 3.7% **covering**. ⚠ **S30's frozen no-information band is ±14.6% and is NOT re-frozen — today's ±13.4% is INSIDE it, so the frozen band stays the binding line and it is WIDER than the market's current price** |
| **June PCE** | 07-30 08:30 ET | **S15** | ⚠ **n≈1 pre-registered in S19**: FOMC and PCE share one driver (oil), one day apart |
| **MA** | 07-30 | **S14 · S14-ANNEX · S14-num** | implied **±3.5%** (D2) against **S14-num's frozen ±3.9%, NOT re-frozen.** Any move inside ±3.9% is **pre-declared no-information** |
| **VLO** | 07-30 | **S8 · MACRO P4** | implied **±4.8%** (D2); short **4.3% float covering, DTC 3.2**; FINRA 5v5 **+6.0▲** |
| **STNG** | 07-30 | **S21** | implied **±9.7%** (expiry 08-21, **D23 — covers**) against S21's registered ±10.0%, **NOT re-frozen**; short **4.8% float covering** |
| **EQIX** | 07-30 | **S25** (2nd settling point) | implied **±9.4%** (D23, covers), **P/C 4.25** |
| **XOM** | 07-31 | **S31** | implied **±4.1%** (D2, covers). ⚠ **XOM prints INSIDE its own observable's window — declared at S31's registration, not discovered now** |
| **SK이터닉스 SPA** | 07-31 | **S22** | branch B (a **second** deferral) is the kill |
| **MPC · PSX** | 08-04 / 08-05 | **S8 · P4** | one risk unit with VLO (ρ +0.878) |
| **CXMT / memory supply** | → 09-30 / 10-31 | **S34 · S37** | S37 brackets the branch in which a funded entrant **re-rates** the incumbents |
| **Materials** | → 08-05 | **S36** | branch A is **against us** and both legs currently read true |
| **Regulated utilities** | 07-29→31 | **S35** | branch A **falsifies this desk's own demote** |

### 2b · Binaries deliberately NOT bracketed, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **V (2026-07-29)** | **S14-ANNEX already pre-registered the {MA, V}-only reading**; a V-specific bracket double-counts one event. ⚠ **But log the positioning, because it is extreme and unexplained: V's option P/C OI is 5.90 with skew +12.5 and implied ±3.5% (D2), on a name carrying RS20 +7.3 / RS60 +8.0.** That is the heaviest put positioning on the board and **no bracket, thesis or dig accounts for it.** Recorded as an under-computed positioning fact, not converted into a view |
| **July NFP (2026-08-07)** | ★ **Neither branch changes a conclusion inside any live window.** S19's and S23's DGS2/T10Y2Y windows both **close 2026-08-05, before NFP prints.** A labor number that lands after every registered rate observable has settled cannot move them. **Dropped with the date arithmetic stated** |
| **AMD · ANET (2026-08-04)** | Re-checked rather than re-quoted: **AMD 🔴분산 −0.66, RS20 −15.7 / RS60 +25.2; ANET 🟡 +0.06, RS20 +3.4 / RS60 −4.8.** Neither carries a thesis, a tilt link or a covering straddle ⇒ **any threshold would still be fabricated.** Dropped, same reason as 07-27 |
| **CEG · VST · LNG (08-06/07)** | **CEG and VST sit inside S24's frozen basket** and LNG is **not in `us_top300`** (instrument gap). A separate bracket double-counts S24 |
| **A second crack bracket** | **S8 and MACRO P4 own it on one axis** (settled 3-2-1 below 60), and the buffer **widened again, 8.12 → 12.22.** Duplication |

### 2c · ★★★ THREE new brackets — the gaps nothing in S1–S39 contains

> All thresholds frozen **2026-07-29, pre-event**. Registered in `handoff/SCENARIOS.md`.
> IDs checked against every existing row (**S38/S39 were taken this morning by `industry_kr`** — the
> D76 collision class). **Next free ID is S40.**

**S40 — ★★★ A capex GUIDE is not a capex MEASUREMENT when a gigawatt arrives as a lease.**
*The gap*: **S13, S16 and S24 all score on "the capex guide" at MSFT and META.** On 2026-07-28 Meta
closed a **$14bn, one-gigawatt El Paso campus with BlackRock funds taking 80%** — **$12.5bn of it debt
— and leased the entire campus back** for up to 20 years as sole occupant, collecting a **~$1bn
distribution** at close and providing **residual-value guarantees with a ~$13bn aggregate threshold**
(EVENT_ALPHA Card 2). **A gigawatt of AI capacity that arrives as a lease does not appear in the line
item three registered brackets score on.** Nothing in S1–S39 contains this.
- **Branch A (against our framing)**: META's FY capex guide is **held or cut** at tonight's print
  **AND** at least one further off-balance-sheet AI-infrastructure structure (JV, sale-leaseback or
  residual-value guarantee ≥$5bn) is disclosed by **2026-09-30** ⇒ **the capex observable is measuring
  a financing choice, and S13/S16/S24's shared line item is structurally impaired.**
- **Branch B (with our framing)**: META's capex guide is **raised** ⇒ the lease was incremental, not
  substitutive, and the registered observable still measures spending.
- **Branch C**: guide held/cut with **no** further structure by 09-30 ⇒ `AMBIGUOUS` — re-register on
  disclosed lease-obligation growth rather than on deal count.
- **Frozen observable**: META's FY2026 capex guidance line **and** the count of disclosed
  off-balance-sheet AI-infrastructure structures ≥$5bn, **2026-07-29 → 2026-09-30.**
- ⚠ **No options instrument prices a financing structure** — the threshold is a **count**, and it is
  hand-set and declared as such. **This does NOT re-freeze S13, S16 or S24.**
- ★ **Information content: branch A impairs the observable that three registered brackets share.**
  Highest-information bracket of this run.

**S41 — ★★ The AI-issuer credit channel S26 explicitly excluded.**
*The gap*: **S26's frozen observable is HY OAS (index-level) and its own invalidation clause reads
*"widening driven by a single issuer or sector default rather than index-level (idiosyncratic,
re-register)."* Today's feed describes exactly that case**: **Oracle CDS ~200bp · NVDA ~78bp
("risen sharply this week") · META ~93bp against an IG CDS index ~53bp**, with tech CDS trading
**~$650m/day in Q2, +20% QoQ and ~+600% YoY** [Reuters via yahoo_finance, citing S&P Global Market
Intelligence / DTCC / ISDA]. **HY OAS sits at 2.81% and would not move on any of it.**
- **Branch A (against us)**: **IG OAS ≥ 0.90% on a close by 2026-08-12** ⇒ the single-name AI widening
  transmitted, and the desk's index instrument was simply **late** rather than right.
- **Branch B (with us)**: **IG OAS stays < 0.90% and HY OAS stays < 3.10% through 08-12** ⇒ the
  widening stayed idiosyncratic, S26-A held, and the index axis was the correct resolution.
- **Frozen observable**: **IG OAS (FRED `BAMLC0A0CM`) on a close, with HY OAS quoted alongside**
  (the two-series rule). **State at registration: IG 0.81% (07-27), HY 2.81% (07-27), NFCI −0.554.**
- ⚠ **This repo has no CDS feed (new dig D97)** — that is precisely why the observable is an index
  series this desk can actually pull, rather than a quote it cannot verify.
- ⚠ **Counter-evidence carried at registration (C2)**: the same body states **CDS trading is thin —
  "average daily trades, even for large companies, can sometimes be in the single digits"** ⇒ a CDS
  level is a low-liquidity quote, not a clearing consensus.
- **Tilt hit**: the book's **held AI-compute epicenter (NVDA, AVGO)** and, through the shared beta,
  all three OW carriers. **Invalidation**: a single-issuer default event ⇒ idiosyncratic, re-register.

**S42 — ★★ This run's OWN new verdict, bracketed against itself.**
*The gap*: **ROTATION promoted Industrials OW− → OW this run**, on **breadth 0.180 driven by nine
greens, four of which are CAPITAL GOODS (WAB · PCAR · MMM · ITW)** — the node **M174 measured five
days ago at flow −0.193 with 0🟢 / 16🔴.** **A verdict this run created, on a node its own prior
measurement contradicts, and nothing brackets it.**
- **Branch A (against us)**: the **median RS20 vs SPY of {WAB, PCAR, MMM, ITW} turns ≤ 0 by
  2026-08-12** ⇒ the ignition was a **date-clustered one-session event (S1: n≈1, not n=4)** and the
  promote was taken on noise.
- **Branch B (with us)**: that median stays **> 0** through 08-12 **and** at least **2 of the 4 still
  carry a 🟢 tag** ⇒ M174's split genuinely inverted at the capital-goods end.
- **Frozen observable**: that median, settled closes. **State at registration: WAB +14.0 · PCAR +15.6
  · MMM +12.4 · ITW +10.4 ⇒ median +13.2.** Control quoted alongside: **CAT 🔴분산 −0.76 with
  RS20 −18.6**, inside the same node — **so the answer is explicitly not "capital goods turned" (W5).**
- ⚠ **n≈1 declared at registration**: four names greening on one settled session is **one observation**,
  and `new_green` diffs against a **07-27** history key because **no 07-28 key exists** (SWEEP §0).
- ⚠ **No options instrument covers a four-name industrial basket** — a **sign test on a median**, so
  no magnitude is fabricated. **Invalidation**: HY OAS ≥3.10% on a close ⇒ **S26/S41** own it.
- ★ **Information content: branch A falsifies a verdict this run itself made.** Asymmetric in the
  useful direction — **the bracket can hurt us.**

---

## LENS 3 — MOMENTUM-CONTINUATION RE-TAGS

*"Already ran +100%" ≠ avoid. Each runner re-tagged, with the flip condition.*
*(RS from settled `SECTOR_FLOW_US.json`; the live-call caveat in §0b applies.)*

| Name | RS20 / RS60 vs SPY | `vol_surge` | Tag | Flip condition |
|---|---|---|---|---|
| **DDOG** | **+0.9 / +86.7** | 0.64 | **EXTENDED-BUT-LIVE — and it is the LAST one standing in its node** | RS20 crossing ≤0 ⇒ EXHAUSTED. **It is 0.9pp away** |
| **PANW** | **−3.9 / +74.8** | 0.72 | ★ **CROSSED → EXHAUSTED** *(new this run)* | RS20 back >0 for 3 settled sessions |
| **CRWD** | **−2.1 / +60.1** | 0.59 | ★ **CROSSED → EXHAUSTED** *(new this run)* | ditto; ledger recheck 09-02 |
| **FTNT** | **−3.5 / +74.8** | 0.76 | **EXHAUSTED** (crossed 07-28) | **prints 07-30** |
| **HPE** | **+2.7 / +55.4** | **0.51** | **EXTENDED-BUT-LIVE** — the only AI-server name still positive on both windows | RS20 ≤0. ⚠ `vol_surge` 0.51 is the lowest measured — **thin** |
| **DELL** | **−5.4 / +84.6** | 0.67 | ★ **CROSSED — first negative RS20** *(was +5.5)* | ⚠ **Do not tag EXHAUSTED yet**: its days-21-60 excess is **+89.9, the board's largest**, and FINRA gives it the board's cleanest short-collapse (**z −2.28, 5v5 −9.0▼**). **A-grade price and B-grade positioning disagree ⇒ `indistinguishable` (C4)** |
| **MU** | **−28.3 / +55.6** | 0.84 | **EXHAUSTED** (long-standing) | S30-A: median RS20 of {STX,MU,WDC} >0 by 08-05 |
| **SNDK** | **−46.5 / −3.1** | 1.33 | ★ **BROKEN — the RS60 cushion is GONE** | RS60 back >0 |
| **AAPL** | **+20.7 / +22.2** | 0.81 | **EXTENDED-BUT-LIVE — the strongest two-window agreement in IT, and it carries NO thesis anywhere** | RS20 ≤0 |
| **TRV** | **+19.7 / +27.1** | **1.15** | **EXTENDED-BUT-LIVE** | ⚠ M150: **98.6% of its 60-day excess was earned in the last 20 sessions** — the R9/AXON geometry |
| **RTX** | **+16.7 / +21.1** | **1.38** | **EXTENDED-BUT-LIVE, volume-confirmed** | 🟢 lost, or FINRA z >+1.5 |
| **MMM** | **+12.4 / +21.5** | 1.21 | **NEW RUNNER** (`new_green`) | **S42's basket** |
| **MPC · PSX · VLO** | **+18.1/+20.2 · +18.3/+11.8 · +12.2/+15.2** | 0.96 / 0.95 / 0.80 | **EXTENDED-BUT-LIVE** | ⚠ **PSX's days-21-60 excess has flipped NEGATIVE (−5.91)** — the `core_pick` is the degrading leg |
| **ICE · NDAQ · CME** | **+24.3/−6.5 · +24.9/+1.3 · +19.0/−12.8** | 0.93 / 1.00 / 0.70 | **PURE LAST-20 EVENTS** — RS20 large, RS60 ≈0 or negative | The exchanges' replacement observable: **EW excess vs SPY 07-24→07-28 = +3.21pp** (07-27 read +3.17) — **essentially unchanged over one more settled session**, window to 08-07 |

★★ **The lens's actual finding, and it is against this desk's own carry.** **Three of the four
security/observability names crossed to negative RS20 this run** (PANW, CRWD joining FTNT), leaving
**DDOG alone at +0.9 and 0.9pp from crossing.** The node has been carried for weeks as *"the four
cleanest instances of the desk's only A-grade verified signal"* and as the **named carve-out** from
every IT underweight. **That carve-out now protects three EXHAUSTED names.** ⚠ **This is not a reason
to fold them into the N−** — the carve-out exists so a blanket verdict cannot arithmetically short
them — **but the reason for the carve-out has changed from "momentum is live" to "the label is the
wrong unit", and C5 stays unresolved.**

---

## LENS 4 — CYCLE-EXPOSURE (registry × coverage × the REAL book)

`CYCLE_EXPOSURE.json`, live read-only KIS account call. Book **≈$11,582 total, $4,332 invested ⇒
~62.6% cash.**

| Cycle | rank | epicenter % | need ≥ | held epicenter | Flag |
|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | **8.32%** | 12.0% | AVGO · NVDA · TSM | 🚨 **GAP −3.683pp** |
| Energy / oil-refining | 2 | **7.72%** | 8.0% | **MPC · PSX · XOM** | 🚨 **GAP −0.277pp** |
| Missile-defense / rearmament | 3 | **7.54%** | **— (no floor set)** | RTX | ⚪ n/a |

**① The GAP is mark-to-market drift for an EIGHTH consecutive reading, and nothing was traded.**
The AI-compute margin over its floor has run **−0.001 → +0.252 → +0.254 → +0.136 → +0.011 → −3.447 →
−3.769 → −3.683pp** across eight dates with the held set unchanged. **M146/M181 replicate.**

**② The two flags must NOT be read the same way.** Under D61's proposed ±0.5pp band:
**AI-compute's −3.683pp is OUTSIDE it ⇒ the GAP is real.** **Energy's −0.277pp is INSIDE it ⇒ that
flag is `unresolved`, not a fail** — it can flip on drift alone, which is exactly what M181
pre-registered as a warning and what happened on 07-28.

**③ Cleanest epicenter expressions, named — and the honest answer is that none of them is clean.**
- **AI-compute**: the held names are **NVDA 🟡 +0.14 (OBV 매집, RS20 +1.1 / RS60 −4.4)** and
  **AVGO 🟡 −0.07 (RS60 −11.8)** — both negative on the 60-day window, in the sector with **0 greens
  of 56 and 29 reds.** ⚠ **There is no 🟢 anywhere in Information Technology to point at.** The
  cleanest *measured* expressions in the cycle's value chain are **DELL and HPE**, which are
  **one layer off the epicenter** and whose RS20 has just crossed (Lens 3). ⇒ **the GAP is real and
  the registry offers no clean instrument to close it today. That is the finding, and it is stated
  rather than resolved by naming a name the data does not support.**
- **Energy**: **MPC now reads as held epicenter for the first time**, joining PSX and XOM. Its own
  numbers are the best of the three (**RS20 +18.1 / RS60 +20.2**, OBV 매집) — and it is 🟡 only because
  `vol_surge` is 0.96 (ROTATION's diagnosed gate artifact).
- **Missile-defense (rank 3)**: **7.54% exposure against NO floor** — the registry has never set one.
  **RTX is 🟢 with `vol_surge` 1.38 and a clean FINRA read.** ⚠ **A rank-3 cycle with no minimum
  cannot ever fire a GAP** — the same silent-failure class as **D20(a)**'s missing AI-security row.
  **Registry edits need a human; escalated, not made.**

**④ ★ The registry's blind spot, second consecutive occurrence.** An **AI-security** thread built
**5→3→7 outlets** this run (EVENT_ALPHA Card 5) and **no cycle-registry row exists for it**, so a 0%
book exposure can never raise a flag (**D20a**). Two runs, two builds, zero mechanism.

---

## 5 · Synthesis — what changed, and what is handed where

| Output | Destination |
|---|---|
| **DEEP set updated: ENRG · FIN · INDU · + UTIL** (Lens 1 Leg A promoted on six dated binaries in 48h and an 8.3pp intra-sector RS gap) | **DEEP stage** |
| **Three new brackets — S40 · S41 · S42**, each with both branches, a frozen observable, a frozen threshold and a date | **`handoff/SCENARIOS.md`** (registered this stage) |
| **Both-sides coverage table for all 15 in-window binaries** (§2a), plus **5 dropped with information-content reasons** (§2b) | **ALPHA's action bracket** |
| **Momentum re-tags: PANW · CRWD CROSSED → EXHAUSTED; DELL CROSSED but `indistinguishable`; SNDK BROKEN; DDOG last-standing at +0.9** | **BET / STANDING_VIEW §3a** |
| **Cycle GAP: AI-compute real (−3.683pp, no clean instrument exists today) · Energy `unresolved` (−0.277pp, inside the band) · rank-3 has no floor** | **BET's epicenter-starter module** |
| **Under-computed positioning facts logged, not converted**: V's **P/C 5.90**, EQIX's **P/C 4.25** | **watch** |

**Did all four lenses agree with the draft? No — and two changed it.**
Lens 1 **added a fourth DEEP**. Lens 3 **downgraded two names inside the carve-out ROTATION had just
written**. Lens 2 found **three unbracketed branches, one of which impairs an observable three
existing brackets share.** Lens 4 confirmed the deterministic GAP and **found that the cleanest
instrument to close it does not exist in the registry today.**

## ✅ EXIT CHECK

- [x] Four lenses run, each returning **named tickers + dated catalysts**. ⚠ **Run in-line, not as a
      parallel fan-out** — the configuration limit and its cost (one layer of checking, not two) are
      stated at the top (§0), not buried.
- [x] **Every new bracket names its observable + frozen threshold + date and carries BOTH branches**
      (S40 three branches, S41 two, S42 two). Registered in `handoff/SCENARIOS.md`. **No one-way
      bracket was written.**
- [x] **Every magnitude threshold is stated against the implied move with its `D±n`**: META ±8.1% (D2)
      · MSFT ±7.2% (D2) · STX ±13.4% (D2) **against S30's frozen ±14.6%, NOT re-frozen** · MA ±3.5%
      (D2) **against S14-num's frozen ±3.9%, NOT re-frozen** · VLO ±4.8% · XOM ±4.1% · EQIX ±9.4%
      (D23) · STNG ±9.7% (D23) **against S21's ±10.0%, NOT re-frozen**. **Where no instrument exists
      (FOMC, PCE, S40's count, S41's index series, S42's median) it is stated, not dressed up.**
- [x] **Each branch graded by information content**; **five binaries dropped with the reason stated**
      (§2b), including **NFP on date arithmetic** — its event post-dates every live rate window.
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] Every catalyst-bearing leg promoted (**UTIL**) or logged as within-run watch (**RE · STPL ·
      HLTH**); **none silently dropped.** Brackets handed to ALPHA; GAP handed to BET.
- [x] **DEEP set updated and stated: ENRG · FIN · INDU · UTIL.**
