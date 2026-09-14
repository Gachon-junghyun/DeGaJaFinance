# BLINDSPOT_PREMORTEM — industry_US — 2026-07-27 (Mon) ★US-only

> Stage 6/10. Four adversarial lenses argued **against our own tilt** before the deep budget was
> committed. Fanned out in parallel, one message. Analytical only — zero sizing, zero buy/sell (P4).
> All relative numbers vs **SPY**, `asof` **2026-07-24 settled**, unless a live call is flagged.

## 0 · ⚠⚠ A verification note that changes how three lens outputs are read

**Two lenses called `module_flow` live and got numbers contaminated by today's partial bar** — the
same **D74** defect this run found in `sector_flow` at universe scale, reproducing at name level:

| Name | Lens's live call | This run's settled sweep (`asof 07-24`) |
|---|---|---|
| STX RS20 vs SPY | −10.8 | **−17.6** |
| STX RS60 vs SPY | +22.9 | **+43.3** |
| EQIX RS20 / RS60 vs SPY | −3.9 / −6.2 | **−0.9 / −3.1** |

⇒ **Every RS figure below is taken from the settled sweep, not from the lens text.** The lenses'
*revision-book* and *filing* pulls (which are not price-derived) are used as returned. ★ **This is
D74's third confirmation in one run** — universe sweep, name-level agent call, and the price cache —
and it means **any agent given a live `module_flow` call during a US session returns contaminated RS**.

Two further corrections applied before use:
- **Bracket IDs renumbered.** Lens 2 proposed S27–S30; **S27, S28 and S29 were taken this morning by
  the `industry_kr` run.** Registered here as **S30 · S31 · S32** — the same collision that forced
  R19's renumbering, caught before the write this time.
- **One lens citation dropped**: a *"yahoo_finance, 7/30"* STX article — a **future-dated** source in a
  07-27 run. Not used.

---

## 1 · LENS 1 — UNDER-COMPUTED LEGS

**Leg A — STX (prints 2026-07-29): PROMOTE-TO-DEEP.**
The bull case is a real revision book, pulled fresh: **current-quarter EPS +30.6%, next-quarter
+32.5%, next-FY +38.3% over 90 days, with 0 downward revisions in 30 days**, on last-quarter revenue
**$3.11bn, +44.1% YoY**.
⚠ **And the desk's own carried fact points the other way on the same name**: STX is **L2's
hardest-confirmed peak-margin case** — FY25 gross margin **35.2% = the 100th percentile of a 17-year,
three-cycle series, +15.1pp above its own prior peak — at 29.9× forward.** Lens 1 adds the trailing
multiples (P/E 77.8×, P/S 16.7×).
⇒ **The strongest revision book and the most extreme margin percentile are on the same ticker.** That
is not a contradiction to resolve here; it is precisely what a DEEP is for. **Implied ±14.6% (exp
07-31, D4) with skew −5.8** — genuinely event-priced, and the negative skew says the option market is
paying up for *upside*, not protection.

**Leg B — EQIX (prints 2026-07-30): WITHIN-RUN-WATCH, not promoted.**
Revisions positive (current-quarter EPS **+13.8%/90d**, 3–4↑ : 0–1↓, 26 Buy/Strong-Buy vs 5 Hold, 0
Sell, mean target **+12.5%** to spot) **against a flow score of −0.449 and RS20/RS60 vs SPY of
−0.9 / −3.1** — analysts up, money out. ⚠ **Its straddle is unusable for the event**: ±10.2% expiring
**2026-08-21 (D25)** covers three extra weeks, so **no admissible event threshold exists.** P/C **4.67**
is the most put-heavy book in the set. **Held as a watch; the 07-30 print is the resolving datum.**

**Also checked and explicitly not built into a leg**: COMM/META — its straddle expired **today**,
before its own event, so there is nothing to threshold (see §5).

---

## 2 · LENS 2 — REGIME-FLIP / BOTH-SIDES · three new brackets, four dropped

**Every registered bracket below carries both branches, a frozen observable, a frozen threshold and a
date. All three are absent from S1–S29.**

### S30 — the SUPPLIER leg's 20-day reversal · 2026-07-29 → 2026-08-05
**The gap it fills**: S13 brackets a capex raise priced as a margin drag **at the spenders**. **Nothing
in the book brackets the supplier leg's own 20-vs-60-day split**, which is C8's live form and M149's
"decaying stock of past excess" measurement.
- **Branch A (against us)**: the suppliers snap back — the 60-day run was pausing, not topping, and the
  IT-Neutral's implicit "wait for the roll-off" defence is wrong for the whole 08-19→09-07 expiry stack.
- **Branch B (with us)**: the 20-day reversal continues and M149's decaying-stock reading is confirmed.
- **Frozen observable**: **median RS20 vs SPY of {STX, MU, WDC}** (settled closes).
- **Frozen threshold**: that median **crosses above 0 by 2026-08-05**. Current: **−17.6 / −24.7 /
  −23.7 ⇒ median −23.7.**
- ★ **Control pair registered inside the bracket, not as a separate one**: **DELL (+6.2 / +108.6) and
  HPE (+1.4 / +66.8)** — the only two names whose 60-day excess sits in days 21–60 rather than the last
  20 (M149: +5.9% and +2.2%). **If the memory median turns while DELL/HPE do not, the move is a memory
  event; if both turn, it is an IT-beta event.**
- **Implied move**: STX **±14.6% (D4)** — any STX move **inside ±14.6% is pre-declared no-information**.
  MU and WDC have no covering straddle.
- **Tilt hit**: IT **N**. **Rips on A**: STX · MU · WDC · SNDK · AMAT.
- **Invalidation**: HY OAS ≥3.10% on a close (then it is S26, not an IT event).

### S31 — is the book's Energy epicenter the business or the war premium? · → 2026-08-05
**The gap it fills**: **S8** brackets the *commodity* (crude vs the diesel crack). **Nothing brackets
the book's own held expression.** XOM carries **RS20 +13.5 vs RS60 +0.4 — a 13.1pp gap opened entirely
inside the last 20 sessions**, which is the exact exhaustion geometry M149/M150 flag on TRV and VTR,
sitting on the one Energy name the book actually holds and the one with **0% refining exposure**.
- **Branch A (against us)**: XOM's RS20 vs SPY **holds > +10% through 2026-08-05** even with crude ≥5%
  below its pre-pause range ⇒ the integrated leg decouples, and the ENRG OW− is pointed at the wrong
  sub-segment.
- **Branch B (with us)**: XOM's RS20 vs SPY **reverts to ≤ 0 by 2026-08-05** ⇒ the last 20 days were
  war premium and the refining-margin thesis is the only surviving Energy leg.
- **Frozen observable**: **XOM RS20 vs SPY on settled closes**, with **XOM RS60 vs SPY quoted alongside**
  (a 20-day number alone hides whether the gap closed by RS20 falling or RS60 rising).
- **Frozen threshold**: as stated. Current **+13.5 / +0.4**.
- **XOM prints 2026-07-31** — inside the window, so the observable is contaminated by an earnings event
  and **that is declared at registration, not discovered afterwards**.
- **Tilt hit**: ENRG **OW−** and the rank-2 cycle's held exposure. **Rips on A**: XOM · CVX · COP.
- **Invalidation**: a Hormuz reopening statement (then S8 owns it, not this).

### S32 — the positioning branch nothing brackets · 2026-07-28 COT → 2026-07-31
**The gap it fills**: **M125 is the desk's own headline positioning fact — Nasdaq-100 net-spec at the
5th percentile (crowded SHORT) against S&P 500 at the 84th, a 79-percentile-point spread inside one
asset class — carried for three runs and bracketed nowhere.** Two days before the largest prints of
the window, the book has no branch in which the mega-caps rise **on positioning rather than on
fundamentals**.
- **Branch A (against us)**: the crowded short covers into the prints and IT/COMM rise **without any
  capex/margin question being answered** ⇒ S13 and S16 score on observables that the tape ignores.
- **Branch B (with us)**: positioning stays crowded-short and the prints are settled on fundamentals.
- **Frozen observable**: **CFTC Nasdaq-100 net-spec 1-year percentile** (next release covers the
  07-28 Tuesday close), **with QQQ RS5 vs SPY quoted alongside.**
- **Frozen threshold**: the percentile **rises more than 15 points from 5th AND QQQ RS5 vs SPY > +2%
  by 2026-07-31** ⇒ branch A.
- ⚠⚠ **Registered with an explicit constraint: "COT crowded-long/short contrarian" sits in the
  desk's REJECTED signal ledger (D6).** This bracket does **not** re-buy it. It registers an
  **observable to be scored**, so that if the prints are overwhelmed by a positioning unwind the
  record says it was foreseeable — the same reason **C6** exists. **It may not be cited as a signal.**
- **Tilt hit**: IT **N**, COMM **N−**. **Rips on A**: META · MSFT · AMZN · NVDA.
- **Invalidation**: HY OAS ≥3.10% (S26 owns it).

### Brackets considered and DROPPED, with the information-content reason (L3)

| Candidate | Reason dropped |
|---|---|
| **EQIX vs DLR RS20 spread (07-30)** | **Duplicative of S25**, which already freezes DLR's RS20 vs the {PLD, AMT, WELL} median to 08-08 and already names EQIX's 07-30 print as its second settling point. Adding a second spread on the same names would double-count one event |
| **V (07-29) standalone** | S14 / S14-ANNEX / S14-num already own the payments binary, and the ANNEX pre-registered the **{MA, V}-only** reading. **No incremental information** |
| **PSX (08-05) standalone** | Same mechanism as **S8 branch B**; PSX/VLO/MPC sit in one risk unit (ρ +0.878). No new observable |
| **AMD / ANET (08-04)** | **No implied move and no flow baseline exist for either at this clock — any threshold would be fabricated.** Stated rather than manufactured; revisit when the options data covers the event |
| **FTNT standalone** | Same 20-vs-60-day shape as S30's basket; folded in rather than duplicated |

---

## 3 · LENS 3 — MOMENTUM RE-TAGS · "already ran" is not a verdict

| Name | Re-tag | Deciding KPI (revision book = the "is the cycle KPI still accelerating" test) | Flip condition · date |
|---|---|---|---|
| **MU** | **EXTENDED-BUT-LIVE** | current-qtr **25↑:0↓ (30d)**, FY **29↑:0↓** — unanimous. ⚠ against GM 84.6% = 100th pctile of 17y and the margin **rate** decelerating +18.4 → +10.2pp | RS60 window rolls **08-25**; FQ4 ~09 (S4) |
| **AMAT** | **EXTENDED-BUT-LIVE** | **strongest book in the equipment tail: 26↑:0↓ (7d), 25↑:0↓ (30d)** — and *rising* while price fell | expiry **09-07**; prints 08-14 |
| **WDC** | **EXTENDED-BUT-LIVE** | margin is **NOT** a trap (+1.5pp over its own peak at 28.0× fwd); book thin but unanimous | expiry **08-21** |
| **SNDK** | EXTENDED-BUT-LIVE, **low conviction** | revisions positive but 2–5 analysts; **margin UNMEASURABLE** (3-yr post-spin series contains no cycle — C3) | expiry **07-31 (4 days)** |
| **STX** | **EXHAUSTED** | **L2 confirmed hardest** (35.2% GM = 100th pctile of 17y, +15.1pp over peak, 29.9× fwd); revision book **thin (1–4 names)** despite big % moves | **07-29 print**, implied ±14.6% |
| **LRCX** | **EXHAUSTED** | **worst days-21-60 erosion in the set (−141.2%)**; revision breadth is 1–2 analysts, not a book | expiry **08-20** |
| **KLAC** | **EXHAUSTED** | ★ **the only equipment name with net NEGATIVE breadth: current-qtr 0↑:1↓ (7d), next-qtr 4↑:3↓ (30d)** | expiry **09-02** |
| **DDOG** | **EXTENDED-BUT-LIVE** | **37↑:0↓** current-qtr, **36↑:0↓** next-qtr (30d); best flow in the security node (+0.478), RS20 **+11.1** | next print |
| **PANW** | **EXTENDED-BUT-LIVE** | **40↑:1↓** current-qtr, FY **47↑:1↓**; soft spot: next-qtr **1↑:4↓ (30d)** | next-qtr breadth |
| **FTNT** | **EXTENDED-BUT-LIVE on revisions / high near-term risk** | **38–40↑:0↓** across three horizons — the cleanest book in the node — against flow **−0.228**, RS20 **+1.0**, GM 80.5% ≈ its FY24 peak 80.6%, **mean target 13.8% BELOW spot**, 28 Hold vs 11 Buy | **07-30 print**, implied **±13.0%**, P/C 2.85 |
| **CRWD** | **EXHAUSTED-leaning** | **29↑:11↓** current-qtr, 27↑:11↓ next-qtr — **the most downgrades of any name reviewed**, and exactly the axis its ledger row was filed on | 30d breadth |
| **VLO** | **borderline EXTENDED, weakest of the three refiners** | **genuine downgrades: 7↑:5↓ current-qtr.** ⚠ `margin_history.py VLO` returns **"연간 데이터 없음"** (D56) ⇒ **no margin percentile is claimed** rather than invented | **07-30 print**, implied ±5.4% |
| **MPC · PSX** | **EXTENDED-BUT-LIVE** | cleaner books; next-qtr 90d **+119.7% / +62.1%** | 08-04 / 08-05 prints |
| **DELL** | **EXTENDED-BUT-LIVE** | **20–23↑:0↓ on every horizon**; margin **not** at peak (FY26 20.0% vs its own FY19 peak 27.6%) at 19.7× fwd ⚠ *annual basis — M140's 21.1 → 17.8% is the five-quarter basis; different instruments, both stated* | prints **09-04**, outside every window |
| **HPE** | **EXTENDED-BUT-LIVE** | ★ **17–19↑:0↓ on ALL FOUR horizons — the only unanimity in a 24-name set** | expiry **08-27**; prints **09-04** |

### ★ The single name the desk is most likely avoiding for the wrong reason: **HPE**

**RS20 vs SPY is +1.4 — indistinguishable from the benchmark — while RS60 vs SPY is +66.8.** A screen
reads that as *"ran 67% and now going nowhere"* and moves on. The revision book says the opposite:
**17–19 analysts up and ZERO down on current-quarter, next-quarter, this-year and next-year** — no
other name in the set has that. **M149 already measured that HPE's excess sits in days 21–60 (+2.2% of
it in the last 20)**, which makes the flat 20-day a **digestion of the move, not a reversal**. And
unlike FTNT it carries **no imminent binary** — it prints 09-04, outside every dated window.
⚠ **The honest gap, stated rather than papered over**: `margin_history.py` returns HPE's XBRL only
through FY2018, so **the "cheap on 11.8× forward" claim cannot be paired with a margin percentile**,
and **L2 forbids calling anything cheap without one.** ⇒ **the name is flagged, not concluded.**

---

## 4 · LENS 4 — CYCLE-EXPOSURE AUDIT

**(a) GAP verdicts, with D61's proposed 0.5pp UNRESOLVED band applied:**

| Cycle | rank | epicenter % | floor | **margin_pp** | Verdict |
|---|---|---|---|---|---|
| **AI-compute / semiconductors** | 1 | **8.55%** | 12.0% | **−3.447pp** | 🚨 **GAP — clears the band decisively. Not borderline.** |
| **Energy / oil-refining** | 2 | 8.03% | 8.0% | **+0.027pp** | ⚠ **inside |margin| < 0.5pp ⇒ UNRESOLVED, not a pass.** The tool's "✅ by 0.03pp" is a rounding verdict, indistinguishable from a miss |
| Missile-defense | 3 | 7.53% | — | n/a | ⚪ ungated by design |

★★ **M146 replicates and completes**: with the held set **unchanged for a sixth consecutive run**, the
AI-compute margin ran **−0.001 → +0.252 → +0.254 → +0.136 → +0.011 → −3.447pp**. **Nothing was bought
or sold. The flag is pure mark-to-market drift** — which is exactly why D61 asked for `margin_pp` as a
first-class field, and why the 07-25 run's ✅ (clearing by 1.1 basis points) should never have read as
a pass.

**(b) Epicenter vs one-layer-off — the book holds the label, not the engine.**
- **AI-compute**: held **AVGO (RS60 vs SPY −8.3) · NVDA (−6.8) · TSM** are the laggard slice, while the
  bucket's movers run away — **DELL +108.6 · MU +78.8 · HPE +66.8 · AMD +57.7 · AMAT +36.9**.
- **Energy**: the held name is **XOM (RS60 vs SPY +0.4, near the bottom of the Energy set) with 0%
  refining**, while the registry's **human-locked `core_pick` is PSX (RS60 +21.4), unheld** — and this
  run's shortlist independently surfaced XOM and **not** the refiners (SWEEP §3). **Three instruments,
  one blind spot, third replication.**
⚠ Per the standing rule: **a 🔴 or crowded tape gates ADD timing; it never justifies zero core in a
multi-year cycle.** MU's and AMAT's deeply negative RS20 (−24.7 / −20.4 vs SPY) is a timing fact.

**(c) ✅ D62 RESOLVED — and the evidence is stronger than the lens's version.**
Claim under audit: *"`RISK_UNITS.json` lists the book WITHOUT TSM while `cycle_exposure` counts TSM in
epicenter dollars every day."* **Verified directly this run:**
- `CYCLE_EXPOSURE.json` carries `['AVGO','NVDA','TSM']` as held epicenter on **all six dates 07-21 →
  07-27**, from a live read-only KIS `fetch_overseas_balance` call — i.e. **the account itself**.
- `RISK_UNITS.json`: TSM appears **14×** on 07-22, **0×** on 07-24 and 07-25 — **and AVGO, which is
  indisputably held, also drops to 0× on 07-25.**
⇒ **`RISK_UNITS`' name set churns run to run with data availability; it is a correlation utility, not a
position record.** **cycle_exposure is authoritative on holdings. TSM is held. D62 is closed**, and the
12.01% epicenter figure it was blocking is unblocked. **Fix for a human: RISK_UNITS should emit the
names it dropped and why, rather than silently shrinking its universe.**

**(d) Registry-edit proposals — for a human, not applied here** (`data/cycles/cycle_registry.json`,
`updated: 2026-07-17`, **10 days stale, 3 rows**; ⚠ the tool's footer still cites `data_build/cycles/`,
**verified this run not to exist**):
1. **CXMT belongs in the AI-compute row as a capacity-clock note, NOT as a ticker.** It is a real
   change to the desk's supply clock (M7 names only SK M15X / Micron Idaho mid-2027 and Samsung P5
   2028 — no fourth supplier) but it carries a **DoD "Chinese Military Company" designation and a
   pending Entity-List action**, so there is no clean US-book expression. Proposal: a `capacity_clock`
   field, so the supply-side risk is recorded without implying an investable exposure.
2. **Add an `enterprise_infra_security` sub-layer** carrying **DELL · DDOG · PANW · FTNT**. Four of the
   board's top-six RS60-vs-SPY names sit in **no registry row at any layer**, so a 0% exposure to them
   **cannot flag** — the registry is blind to its own biggest movers.

**(e) Cleanest epicenter expressions, with the numbers** — **coverage measurements, not
recommendations (P4)**: AI-compute — **MU (RS60 vs SPY +78.8)** and **AMAT (+36.9)**, both
epicenter-layer, both with deeply negative RS20 that gates *timing*. Energy — **PSX (+21.4)** and
**MPC (+29.1)**; **XOM (+0.4) is the weakest epicenter name currently held.** Missile-defense —
**RTX (+17.3, flow +0.792)**, ahead of LMT (+9.9) and NOC (**−10.0**, distributing).

---

## 5 · The magnitude-threshold audit — every implied move, stated

Pulled **2026-07-27**, `module_flow --positioning`:

| Name | Implied | Expiry (D) | Covers its event? | P/C · skew | Verdict on usability |
|---|---|---|---|---|---|
| **UPS** | **±6.8%** | 07-31 (D4) | ✅ | **0.34** · +1.6 | Usable. **The most complacent book on the board sits on the desk's own registered falsifier** (S20-ANNEX's ±6.9% holds one day later) |
| **STX** | **±14.6%** | 07-31 (D4) | ✅ | 1.58 · **−5.8** | Usable and **genuinely event-priced**; negative skew = paying up for upside |
| **FTNT** | **±13.0%** | 07-31 (D4) | ✅ | **2.85** | Usable; put-heavy |
| **VLO** | **±5.4%** | 07-31 (D4) | ✅ | 0.98 · +1.1 | Usable. **Any VLO move inside ±5.4% is pre-declared no-information** |
| **MA** | **±4.7%** | 07-31 (D4) | ✅ | 0.85 · +5.0 | Usable — ⚠ **wider than S14-num's frozen ±3.9%**, which stands as written and is **not** re-frozen |
| **EQIX** | ±10.2% | **08-21 (D25)** | ❌ path, not event | **4.67** | **Not admissible as an event threshold** |
| **MSFT · META · AMZN** | ±1.1% · ±1.7% · ±0.9% | **07-27 (D0)** | ❌ **expire TODAY, before their events** | 0.74 / 0.68 / 0.76 | ★★ **M89 replicates a FIFTH time. No admissible price threshold exists for the three largest prints of the window** — every bracket touching them (S13, S16, S24, S32) is therefore written on a non-price observable, by necessity and by design |

---

## 6 · Injection — what this stage changes

**① DEEP set updated: 3 → 4. Information Technology is PROMOTED.**
**Three of four lenses converged on it independently**: Lens 1 promoted **STX** on its revision book;
Lens 3 found the **most-wrongly-avoided name (HPE)** and the **only net-negative breadth (KLAC)** both
inside IT; Lens 4's **🚨 GAP is the AI-compute cycle** and its two cleanest unheld expressions (MU,
AMAT) are IT. ROTATION had already escalated IT as the **#1 promotable extra** on P9/CXMT.
**Final DEEP set: ENRG · FIN · INDU · IT.**
⚠ **This is a PREMORTEM promotion, not a ROTATION pad** — IT is Neutral and has the board's worst
breadth (eqflow −0.206, 25 🔴 / 4 🟢 of 56). **The promotion is on information content, not on flow,
and the mandate says so**: resolve (a) the **STX contradiction** — the strongest revision book and the
most extreme margin percentile on one ticker; (b) **P9/CXMT** — does a funded fourth DRAM entrant
change the capacity clock, given its own modules price **2.2% ABOVE** the Big Three; (c) **S30's
supplier-leg split** with DELL/HPE as the control.

**② Three brackets registered → `handoff/SCENARIOS.md`: S30 · S31 · S32.** Four candidates dropped with
information-content reasons (§2). **No one-way tilt into a known binary remains**: UPS (S20), FOMC
(S19/S23/S9), capex (S13/S16/S24/**S32**), PCE (S15), MA (S14 family), VLO/STNG (S8/S21/**S31**),
EQIX (S25), IT suppliers (**S30**) — every binary in the window now carries both sides.

**③ Cycle GAP → BET's epicenter-starter module**: 🚨 **AI-compute, margin −3.447pp**, with the
UNRESOLVED flag on Energy's +0.027pp and the two registry-edit proposals for a human. **D62 closed.**

**④ Momentum re-tags → DEEP/BET**: EXHAUSTED = **STX · LRCX · KLAC · CRWD(-leaning)**;
EXTENDED-BUT-LIVE = **MU · AMAT · WDC · SNDK(low) · DDOG · PANW · FTNT(revisions) · MPC · PSX ·
DELL · HPE**; borderline = **VLO**. ★ **HPE flagged as the most-likely-wrongly-avoided name, with its
margin-percentile gap stated so it is not read as a conclusion.**

**⑤ Two new digs** (§0): **D74 confirmed at name level** — an agent given a live `module_flow` call
during a US session returns contaminated RS; and the **bracket-ID collision** between concurrently
running desks, caught pre-write this time (proposal for a human: have `scenario` IDs allocated from a
shared counter rather than by each run's own count).

## ✅ EXIT CHECK

- [x] **4 lenses fanned out in parallel, one message**; each returned named tickers and dated catalysts.
- [x] **Every new bracket names its observable + frozen threshold + date and carries BOTH branches**
      (S30 · S31 · S32), registered in `handoff/SCENARIOS.md`. **Zero one-way brackets.**
- [x] **Every magnitude threshold stated against the implied move** (§5), with the three that expire
      before their own events pre-declared **no-information** and their brackets written on non-price
      observables instead.
- [x] **Each branch graded by information content**; **five candidates dropped with the reason**, not
      silently.
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] Every catalyst-bearing leg promoted (STX→DEEP-IT) or logged as within-run watch (EQIX);
      brackets handed to ALPHA; **GAP handed to BET**; **D62 closed with file evidence.**
- [x] **DEEP set updated and stated: ENRG · FIN · INDU · IT.**
- [x] Zero sizing, zero buy/sell language (P4). English-pure.
