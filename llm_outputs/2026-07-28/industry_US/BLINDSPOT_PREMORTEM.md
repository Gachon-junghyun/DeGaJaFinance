# BLINDSPOT_PREMORTEM — industry_US — 2026-07-28 (Tue) ★US-only

> Stage 6/10. Four adversarial lenses argue **AGAINST our own tilt** before the deep budget is
> committed. Every bracket carries **both branches**, a **frozen observable + threshold**, and a
> **date**, and is written into `handoff/SCENARIOS.md`. Magnitude thresholds come from the options
> market, not from judgement. Analytical only (P4).

## ⚠ 0 · Method limitation, stated at the top rather than buried

**The four lenses were executed IN-RUN by the orchestrator, not as a parallel subagent fan-out.**
This session's standing configuration does not permit spawning agents unprompted, and the protocol's
own text calls for a 4-agent parallel fan-out.

**What that costs, in the desk's own measured terms**: the 07-27 KR run recorded that *"four subagents
were given mandates containing numbers and three of them refuted the numbers they were given"*, and
the 07-27 US run recorded *"two of three mid-run corrections were made by a SUBAGENT against the
mandate it was handed."* **A fan-out is this desk's cheapest adversarial audit of the orchestrator's
own inputs, and today it did not happen.** Every number below therefore carries **only** the
orchestrator's own checking, and the standing conclusion applies: **an unchallenged mandate is a
single point of failure.** ⚠ **Read the brackets below as less independently verified than the ones
registered on 07-25 and 07-27.**

★ Partial substitute actually performed: **three carried numbers were re-measured rather than
inherited this run and two of them moved** — the S33 betas (reproduced), the settled crack series
(**disagreed with two prior runs by 5 points**, §G of MACRO), and the exchanges' replacement
observable (**−3.00pp → +3.17pp**, Lens 3 below).

---

## Positioning table — every magnitude threshold below is stated against this

`module_flow --positioning`, pulled **2026-07-28 intraday**. ⚠ **The RS/OBV columns of that same call
are contaminated by the live bar (D31/D74) and are NOT used**; only the options/short block is, which
is not price-bar-derived.

| Ticker | Event | **Implied move** | Expiry (D±n) | Covers event? | P/C | Skew | Short |
|---|---|---|---|---|---|---|---|
| **STX** | **07-29** | **±22.5%** | 07-31 (D3) | ✅ | 1.26 | −7.2 | 3.7% covering |
| **META** | **07-29** | **±8.1%** | 07-31 (D3) | ✅ | 0.65 | −1.7 | 1.7% **building** |
| **MSFT** | 07-29/30 | **±7.1%** | 07-31 (D3) | ✅ | 0.74 | −3.8 | 1.2% covering |
| **AMZN** | 07-30/31 | ±2.3% | **07-29 (D1)** | ❌ **expires BEFORE its event** | 0.76 | +3.8 | 1.1% building |
| **VLO** | **07-30** | **±5.7%** | 07-31 (D3) | ✅ | 0.94 | +2.2 | 4.3% covering |
| **MA** | **07-30** | **±5.6%** | 07-31 (D3) | ✅ | 0.73 | +6.4 | 1.0% building |
| **EQIX** | **07-30** | ±8.7% | 08-21 (D24) | ✅ (wide) | **4.54** | +8.6 | 2.2% covering |
| **STNG** | **07-30** | ±8.7% | 08-21 (D24) | ✅ (wide) | 1.43 | +1.1 | 4.8% covering |
| **XOM** | **07-31** | **±4.0%** | 07-31 (D3) | ✅ | 0.92 | **+14.3** | 1.1% covering |
| **T** | none | ±5.4% | 07-31 (D3) | — | **0.09** | **+31.0** | 1.6% covering |

★★★ **M89 is SUPERSEDED for two of its three names, and this is the first usable event threshold the
desk has had on the spenders.** M89 has recorded for five consecutive runs that *"MSFT/META/AMZN
straddles all expire before their own events."* **Measured today: META ±8.1% and MSFT ±7.1% both
expire 2026-07-31, AFTER their 07-29/30 prints.** Only **AMZN** still expires early (07-29, D1).
⇒ **META and MSFT are event-priced for the first time; AMZN is not and no threshold may be taken from it.**

⚠ **Two carried no-information bands are NOT re-frozen, and both are now narrower than the market's:**
**S30 froze STX at ±14.6%** against today's **±22.5%** (1.54× wider); **S14-num froze MA at ±3.9%**
against today's **±5.6%** (1.44× wider). **Moving them would convert a forecast into a description.**
★ The direction of the gap **strengthens** both declarations: a band narrower than the implied move is
*more* likely to contain the outcome, so "inside the band = no information" becomes a stronger, not a
weaker, pre-commitment.

⚠ **T's option pair is internally inconsistent and is reported as such, not as a verdict**:
**P/C 0.09** (almost no puts outstanding = complacency) beside **skew +31.0** (extreme downside-fear
pricing). The tool prints *"안일(연료적음)"*. **Two axes of the same instrument disagree; DEEP-COMM
inherits this as an open question, not as a reading.**

---

## Lens 1 — UNDER-COMPUTED LEGS (not deep-dived, catalyst ≤ ~5 trading days)

| Leg | The bull case against our own tilt | Catalyst | Verdict |
|---|---|---|---|
| ★★★ **Regulated Utilities** (WEC · ETR · EXC · SO · XEL · AEP · D) | **This run demoted UTIL N− → UW on flow, and SIX of its constituents print within 48 hours** — WEC/ETR **07-29**, EXC/SO/XEL/AEP **07-30**, D **07-31**. ⚠ **All six are ABSENT from `CATALYST_WATCH.json` (D18)**, so the demote was taken with no calendar awareness of them. The regulated leg is a **different bet from the AI-power leg S24 brackets** (VST/CEG/GEV/VRT): its driver is rate base and allowed ROE, not datacentre demand | 07-29 / 07-30 | ★ **BRACKETED — new S35.** Not promoted to a 5th DEEP: a UW sector cannot justify deep budget on a bracket alone, and the bracket settles it in 8 sessions |
| ★★ **Real Estate / EQIX** | **EQIX carries P/C 4.54 — the most put-heavy instrument measured anywhere on the board — into a 07-30 print**, on a name that is 🔴분산 (−0.629) with RS20 −5.5 / RS60 −7.7 vs SPY. **S25 already names EQIX as its second settling point**, and S25's own condition is **currently satisfied** (DLR RS20 +0.04 below the {PLD, AMT, WELL} median +3.82) | **07-30** | **WITHIN-RUN-WATCH.** ROTATION §4 declined RE as a DEEP *because* its two brackets settle on their own dated windows; that decision stands and is not re-argued |
| ★★ **Health Care / ABT** | HLTH was demoted **N → N−** on flow today, yet **ABT carries RS20 +9.6 / RS60 +10.5 vs SPY** — positive on both windows — and is STANDING_VIEW's named watch for **C7's resolving observable** (one 🟢 from outside the top-6 by cap). **Measured today: zero of 32.** A demote taken on a sector whose one positive-both-windows name is not the demote's cause | **08-06** (C7 horizon) | **WITHIN-RUN-WATCH.** Logged, not dropped |
| ★ **Payments / V** | **V prints 2026-07-29 — a day BEFORE MA — and is absent from `CATALYST_WATCH`.** S14's basket contains V but its observable is a **basket** read scored 08-06, so a V-specific print has **no branch anywhere** | **07-29** | **WITHIN-RUN-WATCH.** Not bracketed — see Lens 2's drop list for the information-content reason |
| ★ **Defense / GD** | **GD prints 2026-07-29** and is **M179's last partially-closed W4 name** (68% USG revenue, backlog $130.8bn on Q1 data). Flow +0.700, RS20 +10.9 / RS60 +11.0, `vol_surge` 1.06 | **07-29** | **WITHIN-RUN-WATCH.** Dropped from bracketing — see Lens 2 |

**No leg promoted to a 5th DEEP.** The DEEP set stays **ENRG · FIN · IT · COMM**. ⚠ Every leg above is
**logged, not silently dropped**, per the stage rule.

---

## Lens 2 — REGIME-FLIP / BOTH-SIDES: the branches nothing in the book contains

**Verified against every ARMED row of `handoff/SCENARIOS.md` (S1–S34).** Three genuine gaps found.

### ★★★ S35 (NEW) — the regulated-Utilities print cluster: the bracket on a verdict this run just made

Registered **2026-07-28 by the `industry_US` PREMORTEM (Lens 1/2), before the events.**

**The gap it fills.** **S24 brackets the AI-power four (VST/CEG/GEV/VRT).** **Nothing in S1–S34
brackets the REGULATED utilities**, whose driver is rate base and allowed ROE — and this run demoted
the whole sector **N− → UW** on flow, 24 hours before six of them print.

- **Frozen observable**: the **median RS20 vs SPY of {WEC, ETR, EXC, SO, XEL, AEP, D}**, settled closes.
- **State at registration** (`asof 2026-07-27 settled`): **−5.6 · −3.2 · −1.9 · −2.1 · −3.2 · −5.1 ·
  −0.1 ⇒ median −3.2.** Sector flow: **0 🟢 of 15, breadth 0.00, wflow −0.381.**
- **Frozen threshold**: that median **crossing above 0 by 2026-08-07.**

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | median RS20 vs SPY **> 0 by 2026-08-07** | **The UW demote taken today was wrong**, and it was wrong for a specific reason: the sector's flow collapse was the **AI-power** leg, and the desk demoted the **regulated** leg with it — a W5 label-collapse of exactly the shape M26/M174 measured in Industrials |
| **B (with us)** | median RS20 vs SPY **stays ≤ 0** through 2026-08-07 | The demote holds; UTIL UW and the AI-power leg were the same trade after all |

- ⚠ **No options instrument covers a six-name utility cluster** — stated, not dressed up. The
  threshold is a **sign test on a median**, deliberately, so no magnitude is fabricated.
- ⚠ **Invalidation**: HY OAS ≥3.10% on a close ⇒ **S26** owns it, not this.
- ★ **Information content graded (L3)**: branch A **falsifies a verdict this run made**; branch B
  confirms it. **Asymmetric in the useful direction — the bracket can hurt us.**

### ★★ S36 (NEW) — Materials: A-grade price and sweep breadth disagree, and nothing brackets it

Registered **2026-07-28 by the `industry_US` PREMORTEM (Lens 2), before the window closes.**

**The gap it fills.** ROTATION §2b held **MATR UW** while recording that **XLB beat SPY on both the
1-day (+0.25% vs +0.02%) and 5-day (+2.72% vs −0.40%) windows** and that the sector's flow is the
**second-worst on the board (wflow −0.328, 🟢 0 of 12, breadth 0.00)**. **Two of the desk's own axes
point opposite ways on one sector on one date, and no row of S1–S35 contains it.**

- **Frozen observable**: **XLB's 5-day excess return vs SPY** on settled closes, **quoted alongside
  the sector's 🟢 count from `SECTOR_FLOW_US.json`** (a one-axis read hides which side moved).
- **State at registration**: **5-day excess +3.12pp · 🟢 0 of 12 · breadth 0.00 · Copper COT 98th
  percentile.**
- **Frozen threshold**: **by 2026-08-05**, is XLB's 5-day excess vs SPY still **> 0** while the 🟢
  count is still **0**?

| Branch | Observable | Meaning |
|---|---|---|
| **A (against us)** | excess **> 0** AND 🟢 count still **0** | ⇒ **the UW is being carried against its own tape for a second week, and the sweep's breadth is not seeing what the price is doing.** The UW must be re-argued, and **rule D6's "A-grade RS outranks a C-grade OBV tag" applies against the desk's own verdict** |
| **B (with us)** | excess **≤ 0**, or the 🟢 count rises above 0 | The divergence resolves itself; the UW stands and the 07-27 → 07-28 price move was noise |

- ⚠ **n≈1 declared at registration**: a 5-day window containing **one** −2%-crude session is not five
  observations (S1).
- ⚠ **No options instrument covers a sector ETF spread here** — stated.
- ★ **Information content**: branch A **forces a re-argument of a standing tilt**; branch B costs
  nothing. Asymmetric in the useful direction.

### ★★★ S37 (NEW) — the CXMT branch in which a funded entrant is BULLISH for the incumbents

Registered **2026-07-28 by the `industry_US` PREMORTEM (Lens 2), before its window.**

**The gap it fills, and it is this run's most important one.** **MACRO P9, EVENT_ALPHA Card 1 and
S34 all frame CXMT as a SUPPLY threat.** ⚠ **Nothing anywhere brackets the opposite reading** — that a
state-funded fourth entrant *validates DRAM as a strategic asset class* and **re-rates the incumbents**
rather than de-rating them. **The direct evidence for that branch is inside the desk's own body-read**:
CXMT listed at **≈$487bn on ~7.7% share — "roughly half that of Micron and SK Hynix"** — i.e. the
market assigned it **several times the incumbents' capitalisation per point of share.**

**A book that only brackets one direction of its own headline story is running the 2026-07-14
one-way-tilt failure this stage exists to prevent.**

- **Frozen observable**: **MU's forward P/E**, with **its next-year consensus EPS quoted alongside**
  (a multiple alone hides whether the numerator or the denominator moved — the C2 rule applied to
  valuation).
- **State at registration** `[carried, M6, 2026-07-22]`: **forward P/E 6.31× on +1y EPS 153.74.**
  ⚠ **This is a 6-day-old carried figure and is labelled as such** — it is **re-pulled at scoring, not
  assumed**; that re-pull is the first act of scoring this bracket.
- **Frozen threshold**: **by 2026-09-30** (which contains MU's FQ4 print, S4), is MU's forward P/E
  **above 8.0×** with next-year EPS **not lower** than 153.74?

| Branch | Observable | Meaning |
|---|---|---|
| **A (against our framing)** | forward P/E **> 8.0×** with next-year EPS **≥ 153.74** | **A re-rate on an intact denominator.** The CXMT event was read by the market as *validation of the asset class*, not as supply risk ⇒ **P9's direction is wrong even if its facts are right**, and **L2's peak-margin read on MU weakens rather than strengthens** |
| **B (with our framing)** | forward P/E **≤ 8.0×**, **or** next-year EPS falls below 153.74 | The supply reading holds: either the multiple stays at cycle-trough levels, or the denominator starts coming down. **P9/S34 stand** |
| **C** | EPS **rises** while the multiple **falls** | ⇒ **the market is de-rating a rising denominator — the sharpest possible form of the supply thesis**, and stronger than B. Recorded separately so it cannot be scored as B |

- ⚠ **The threshold is hand-set and declared as such.** **No options instrument prices a two-month
  multiple**, and 8.0× is chosen as **1.27× the carried 6.31×**, i.e. roughly the distance a one-notch
  re-rate would travel. It is **not** taken from a measurement, and it is written down here rather
  than dressed up.
- ⚠ **Do NOT score this on price.** A multiple is a ratio; **both legs are re-pulled at scoring.**
- **Invalidation**: an Entity List designation actually implemented (then **P9's own anti-signal**
  owns the outcome and this bracket voids).
- ★ **Information content**: **branch A falsifies the framing of this run's single largest new
  proposition.** This is the highest-information bracket registered today.

### Brackets CONSIDERED and DROPPED, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **V (2026-07-29) standalone** | **S14 / S14-ANNEX / S14-num already own the payments binary** and the ANNEX pre-registered the {MA, V}-only reading. A V-specific bracket would double-count one event. ⚠ **Logged as an under-computed leg in Lens 1 rather than dropped silently** |
| **GD (2026-07-29) standalone** | Neither branch changes a conclusion. **INDU is held OW− on the rail/freight node's flow (4 of the shortlist's top 5), not on defense**, and W4 on defense is already 3 of 5 closed from primary sources. A backlog print moves a `[measured]` gap from 3/5 to 4/5 and moves **no tilt** ⇒ **not worth a bracket; spend it elsewhere** |
| **FTNT (2026-07-30)** | **Folded into the Lens-3 re-tag** (it is the one security name that flips to EXHAUSTED today: RS20 **−0.7** with **OBV 분산**). A separate bracket on a name already on the reject ledger's watch adds nothing |
| **A second crack bracket** | **S8 and P4 already own it on one axis (settled 3-2-1 < 60)**, and the distance **widened to 8.12 points** this run. A second threshold on the same series is duplication |
| **The KOSPI / KR memory rout** | **S34 forbids scoring on a price reaction at registration**, and this is the US desk — a KR index session is not this desk's observable (**W1**). Recorded as evidence the thread is traded, never as a bracket |

---

## Lens 3 — MOMENTUM-CONTINUATION: "already ran" ≠ avoid. Re-tags with flip conditions

Method stated (C5 — the choice is arbitrary and exposed): a runner is **EXTENDED-BUT-LIVE** when
**both** RS20 and RS60 vs SPY are positive on the settled 07-27 bar; **EXHAUSTED** when RS60 is
positive and RS20 has turned negative; **SINGLE-WINDOW** when the RS60 is essentially the RS20.

| Name | RS20 / RS60 vs SPY | Re-tag | Flip condition |
|---|---|---|---|
| **DELL** | +5.5 / **+103.7** (days 21–60: **+98.2**) | ★ **EXTENDED-BUT-LIVE** — the cleanest on the board | RS20 < 0 |
| **HPE** | +8.9 / **+66.4** (days 21–60: +57.6) | ★ **EXTENDED-BUT-LIVE** | RS20 < 0 |
| **DDOG** | +3.7 / +84.1 | **EXTENDED-BUT-LIVE, thin** (`vol_surge` 0.66) | RS20 < 0 |
| **PANW** | +2.9 / +70.9 | **EXTENDED-BUT-LIVE, thin** | RS20 < 0 |
| **CRWD** | +1.4 / +55.4 | **EXTENDED-BUT-LIVE, thin** — already on the reject ledger, recheck 09-02 | RS20 < 0 |
| **FTNT** | **−0.7** / +73.1, **OBV 분산** | ⚠ **EXHAUSTED — the first of the security node to flip**, and it **prints 07-30** | RS20 > 0 restores it |
| **MU** | **−21.9** / +69.8, 🔴분산 | **EXHAUSTED on the 20-day window** — and this is exactly what **S30** tests | S30 branch A (median of {STX,MU,WDC} > 0 by 08-05) |
| **AMAT · LRCX · KLAC · SNDK** | −18.9/+31.2 · −24.5/+13.4 · −19.6/+8.1 · **−40.2**/+16.2, all 🔴 | **EXHAUSTED**, four names, one date ⇒ **n≈1 (S1), not n=4** | same as MU |
| **MPC** | **+21.6 / +25.3**, OBV 매집 | ★ **EXTENDED-BUT-LIVE — the strongest two-window agreement in Energy.** Prints 08-04 | RS20 < 0 |
| **TRV** | +17.9 / +25.3, flow **+0.750** (🟡 only by `vol_surge` 1.15) | ⚠ **SINGLE-WINDOW** — M150/M178 measured its last-20 share at **98.6–99.5%**, so the RS60 *is* the RS20 | RS20 < 0 collapses both |
| **RTX** | +14.8 / +22.5, 🟢 **`vol_surge` 1.22 = volume-confirmed** | ★ **EXTENDED-BUT-LIVE**, one of the few greens that is not a velocity path | RS20 < 0 |
| **AAPL** | **+17.3 / +20.8**, 🟢 | **EXTENDED-BUT-LIVE** — ⚠ **and it still has no thesis in any desk file** (§3a's named coverage gap) | RS20 < 0 |
| **LLY** | **−2.3** / +36.8 | **EXHAUSTED** | RS20 > 0 |
| **ICE · NDAQ · CME · MCO · MSCI · COIN · SPGI** | +18.7/−8.6 · +18.2/−0.9 · +14.2/−15.0 · +6.6/+1.8 · +1.5/−8.4 · +11.0/−11.7 · +12.5/+3.5 | **PURE LAST-20 EVENTS** — see the measurement below | — |

### ★★★ The exchanges' registered replacement observable MOVED, and it moved against the desk

**M135 replaced the exchanges node's broken RS60 test with**: *"equal-weight excess of the 7 vs SPY,
2026-07-24 → 08-07."* The last two runs reported it **unchanged at −3.00pp because no settled close
existed.** **One settled close now exists.** Measured, 2026-07-24 → 2026-07-27 settled:

```
NDAQ +3.89% · SPGI +4.72% · ICE +3.85% · CME +0.41% · MCO +2.91% · MSCI +3.35% · COIN +3.93%
SPY  +0.12%       equal-weight +3.29%   ⇒   EXCESS  +3.17pp     (was −3.00pp)
```

⇒ **a +6.17pp swing in one session, with all seven names positive against a flat SPY.** The observable
runs to **2026-08-07** and is **not scored here**; it is reported because two runs called it unchanged
and it is no longer unchanged. ★ **And the direction matters**: the node was carried as *"highest flow,
worst RS60 — a de-rate"*, and its replacement observable has just moved **the opposite way**.

---

## Lens 4 — CYCLE-EXPOSURE: both ranked cycles now flag, and one flipped on drift alone

Full measurement in `SWEEP_READ.md` §5; the adversarial reading is here.

| Cycle | rank | epicenter | need | margin | held | flag |
|---|---|---|---|---|---|---|
| AI-compute / semis | 1 | **8.23%** | 12.0% | **−3.769pp** | AVGO, NVDA, TSM | 🚨 GAP |
| Energy / oil-refining | 2 | **7.67%** | 8.0% | **−0.327pp** | PSX, XOM | 🚨 **GAP (was ✅ at +0.027pp)** |

**The adversarial point, and it is against this desk's own instrument.** **M181 pre-registered that
Energy's ✅ was *"UNRESOLVED, not a pass"* because its margin was 0.027pp — inside D61's proposed 0.5pp
band. It flipped to 🚨 the very next session, on mark-to-market drift, with nothing bought or sold.**
⇒ **D61's proposal is now supported by a live flip rather than by back-reading**, and the desk should
stop reporting a sub-0.5pp margin as a pass. **Escalated to a human; a threshold change is not this
stage's to make.**

**Cleanest epicenter expressions, named as the rule requires** (a crowded/🔴 tape gates ADD *timing*,
never the core's existence) — **stated as analysis, with no sizing and no recommendation (P4)**:

- **AI-compute epicenter**: the registry's own epicenter set is the held one (AVGO, NVDA, TSM). On the
  settled bar **all three carry negative RS60 vs SPY** (AVGO −9.3 · NVDA −10.0), i.e. **the held names
  are the worst-performing members of their own bucket** — M146's finding, now on its **seventh**
  reading. **The cleanest *measured* expressions in the same layer today are DELL (+5.5 / +103.7) and
  HPE (+8.9 / +66.4)**, and ⚠ **neither sits in any registry row at any layer (D60)**.
- **Energy epicenter**: the registry's human-locked `core_pick` is **PSX**, and **PSX now reads as
  held** for the first time in six runs. The **flow-strongest refiner is MPC (+21.6 / +25.3, OBV 매집)**,
  which is **not** in the registry.

⚠ **The registry itself is the binding constraint**: `data/cycles/cycle_registry.json` is
**`updated: 2026-07-17` = 11 days stale, 3 rows**, and its own artifact footer cites a **path that does
not exist** (`data_build/cycles/`, D60). **The GAP guard can only see cycles someone wrote down**, and
four of the board's strongest RS60 names sit in no row.

---

## 7 · Synthesis — what this stage injects

1. **Three new brackets registered in `handoff/SCENARIOS.md`, all with both branches, frozen
   observables and dates**: **S35** (regulated Utilities, 08-07 — brackets a verdict *this run made*),
   **S36** (Materials price-vs-breadth, 08-05), **S37** (the CXMT branch in which the entrant is
   bullish for incumbents, 09-30 — **the highest-information bracket today**).
2. **Five under-computed legs logged, none promoted to a 5th DEEP.** Final DEEP set unchanged:
   **ENRG · FIN · IT · COMM**.
3. **Momentum re-tags handed to BET**: 6 EXTENDED-BUT-LIVE · 6 EXHAUSTED · 1 SINGLE-WINDOW (TRV) ·
   **FTNT flips to EXHAUSTED two days before its print.**
4. **Two cycle GAPs handed to BET's action bracket**, with **D61's band proposal now supported by a
   live flip**.
5. **M89 superseded on 2 of 3 names** — META and MSFT are event-priced for the first time; **AMZN is
   not, and no threshold may be taken from it.**
6. ⚠ **The method limitation in §0 is part of the output**: these findings carry one layer of checking,
   not two.

## ✅ EXIT CHECK

- [x] Four lenses executed and each returned **named tickers + dated catalysts**. ⚠ **Executed in-run,
      not as a parallel fan-out — the deviation and its measured cost are stated in §0.**
- [x] **Every bracket names its observable + frozen threshold + date, with BOTH branches**, and is
      written into `handoff/SCENARIOS.md`. **No one-way bracket registered.**
- [x] **Every magnitude threshold stated against the implied move**, with its `D±n`. **S30's ±14.6%
      and S14-num's ±3.9% are pre-declared no-information and were NOT re-frozen** despite the market
      now pricing ±22.5% and ±5.6%. Where no instrument exists (S35, S36, S37) that is **stated**, and
      the threshold is a sign test or an explicitly hand-set level.
- [x] **Each branch graded by information content**; **two binaries dropped** (V, GD) with the reason
      that no branch would change a conclusion, plus three more duplicative candidates.
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] Every catalyst-bearing leg promoted or logged; brackets handed to ALPHA; GAP handed to BET.
- [x] **DEEP set unchanged and stated: ENRG · FIN · IT · COMM.**
