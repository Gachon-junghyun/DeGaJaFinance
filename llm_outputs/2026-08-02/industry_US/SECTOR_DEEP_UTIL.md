# SECTOR_DEEP_UTIL — Utilities — industry_US — 2026-08-02 (Sun) · **PROMOTED 5th SLOT (PREMORTEM, two-lens convergence)**

> Covered 07-31 (full fresh map, `llm_outputs/2026-07-31/industry_US/SECTOR_DEEP_UTIL.md`) — that file's
> structure (aggregate → two legs → dispersion → per-leg verdict → 5-node chain → customers →
> KPI/anti-signal → verdict) is **carried unchanged BY REFERENCE** and NOT rebuilt here. This run leads
> with the delta: **is a 20-day RS median a usable instrument on this tape at all (D121)?** Flow/RS
> settled **2026-07-31**, benchmark **SPY** inline throughout (C1). Zero buy/sell, no sizing (P4).

## 0 · The answer, first

**D121 is CONFIRMED — the raw 20-day RS median on this basket has no discriminating power at the
session-to-session horizon these brackets are scored on.** Measured on the last 40 settled sessions
(§1): the regulated-7 median RS20 vs SPY **crosses zero 10 times**, its day-to-day change carries a
**measured σ = 2.08pp**, and **60% of all 40 readings sit within one σ of zero.** The single session
S35 fired on (07-29, +0.39) was a **+2.38pp one-day move against a 2.08pp daily σ — a 1.1σ wobble, not
a regime signal.** **A second, independent finding not visible in either prior DEEP or MACRO: one of
the seven names in the "regulated" basket — D — is not trading on the regulated-utility driver at all.
It is a merger-arbitrage security tracking a fixed 0.8138-share NEE exchange ratio** (§2), and pulling
it out of the basket **changes the 07-29 answer**: the six-name median never crossed zero that session
(**−0.99**, not +0.39). **S35's fired branch A is an artifact of (a) noise and (b) a contaminated
basket, not a reversed thesis.** The whole-sector UW− should **stand**, and it stands on cleaner
grounds after this run than before it.

---

## 1 · ★★★ D121 — is the 20-day RS median a usable instrument? Measured, not asserted

**Method.** Pulled the desk's own settled OHLCV pickle (`llm_outputs/sector_flow/prices_2026-08-02.pkl`,
2026-04-01 → 2026-07-31, the same universe `SECTOR_FLOW_US.json` draws from) and reconstructed, for
every settled session, **median(RS20 vs SPY)** across the regulated-7 {WEC, ETR, EXC, SO, XEL, AEP, D}
exactly as S35 defines it. Cross-checked against the two dates this desk has already published: **07-29
= +0.388** (report: +0.39 ✅) and **07-31 = −4.890** (report: −4.89 ✅) — the reconstruction matches to
two decimals, so the series below is treated as reliable.

### 1a. The last 40 settled sessions (2026-06-04 → 2026-07-31)

| Statistic | Value |
|---|---|
| N sessions | 40 |
| **Zero-crossings (sign changes session-to-session)** | **10** |
| Sessions positive / negative | 26 / 14 |
| **σ of day-to-day change** | **2.084pp** |
| Max one-day move | +4.88pp / −4.35pp |
| **Fraction of readings within 1σ (2.08pp) of zero** | **60%** |
| Fraction of readings within 1.0pp of zero | 30% |

**⇒ 10 crossings in 40 sessions = a crossing roughly every 4 sessions.** A sign test that a single
session can trip (S35's design: median ≤ 0 through 08-07, i.e. one crossing above kills it) is, on this
measured base rate, **expected to fire falsely about once every four sessions even with zero change in
the underlying regime.** **This is D121, substantiated with numbers, not narrated.**

### 1b. What the raw crossings look like as runs (consecutive same-sign sessions)

Runs, oldest→newest: `(neg,3) (pos,6) (neg,3) (pos,12) (neg,1) (pos,6) (neg,2) (pos,1) (neg,3) (pos,1)
(neg,2 — current, incl. 07-31)`. **Three of the eleven runs are exactly ONE session long** — i.e.
**27% of the regime "changes" in this series self-reverse the very next session.** The 07-29 cross
(`(pos,1)`, sandwiched between a 3-session negative run and a 3-session negative run) is drawn from
**the same population as those other two one-session blips**, not a special case.

### 1c. A persistence filter removes most of the noise, and the report proposes it as the fix

Applying a **k-consecutive-session persistence requirement** to the same 40-session window (a sign
"counts" only once it has held for k sessions):

| k (sessions required) | Confirmed regime changes (of 11 raw runs) |
|---|---|
| 1 (current design) | 11 |
| 2 | 8 |
| **3** | **6** |
| 5 | 3 |

**Proposed fix, stated against the measured σ**: require **k ≥ 3 consecutive sessions** on the same
side of zero before a crossing counts, **or** widen the neutral band to **±2.1pp (≈1 measured σ)** and
require the level to clear the band on a settled close. Either construction would have refused to score
the 07-29 single-session print. **This is a proposal for a human to adopt, not a self-applied edit to
S35/S47's frozen thresholds** (P4 — analysis only).

### 1d. The S47 spread (regulated median − AI-power median) is *more* twitchy, not less

Same 40-session window, S47's frozen branches: **branch B (spread ≤ +7.0pp) is TRUE on 28 of 40
sessions (70%)** — it is the *modal* state, not a resolution — with **5 transitions across the 7.0
line**, and **branch A (spread > +20pp) never once fired in 40 sessions** (max observed = 18.9pp,
07-29). **⇒ S47 "firing branch B" on 07-31 is not informative: the spread spends most of its time
already inside branch B's condition.** The +14.74pp registration reading (07-29) was itself the
**outlier session** (one of only 5 sessions above the modal band in 40), not the baseline the
"convergence" is being measured against.

---

## 2 · ★★★ NEW FINDING — one of the seven "regulated" names is a merger-arbitrage security, not a rate-sensitive utility

Neither the 07-31 DEEP nor today's MACRO/SWEEP/EVENT_ALPHA files flag this. **D's 10-Q filed 2026-07-31
sits inside a stack of 49 Form-425 business-combination filings and a DEFM14A (definitive merger proxy,
filed 07-28)** (`module_disclosure_us D`). Cross-checked on the news feed:

- **NextEra Energy (NEE) agreed to acquire Dominion Energy (D) in an all-stock deal announced mid-May
  2026** at a fixed exchange ratio of **0.8138 NEE shares per D share** `[seekingalpha, multiple; a
  securities-notice source states the ratio verbatim]`, creating **enterprise value ≈ $420bn** per
  Lazard's own Q2 earnings call `[nasdaq, body, 07-23]` and a combined market cap **> $240bn**
  `[seekingalpha, body, 07-29]`. **The DEFM14A (07-28) is the shareholder-vote proxy — the deal is in
  its late, mechanical stage, not early speculation.**
- **The market has been pricing this the whole window.** Measured on the same price series as §1: the
  **D/NEE price ratio ran 0.65 in early May → 0.80 now**, converging toward the stated 0.8138 (the
  residual **2.2% gap is the deal-completion discount**, down from **~20% 60 sessions ago**).
  **D's daily returns correlate 0.89 with NEE and −0.21 with SPY over the last 40 sessions** — i.e. **D
  is now trading as a levered proxy for NEE's own share price, not as a member of the regulated-utility
  cohort it is being scored inside.**

**⇒ This explains the exact anomaly both this run's flow file and the 07-31 DEEP flagged without
explaining: D's OBV reads "accumulating" on the sector's lowest `vol_surge` (0.42).** A merger-arb
convergence trade produces exactly that signature — a slow, low-volume price drift toward a known
target, not genuine sector-rotation buying. **D6 binds: the OBV tag was already declined as
non-standalone evidence in the prior file; this run adds the mechanism that makes the decline
correct.**

**Consequence for §1's instrument test, measured, not asserted**: recomputing the regulated median
**excluding D** (6-name basket) over the same 40-session window:

| Basket | Crossings (40 sessions) | σ of daily change | Level, 07-29 | Level, 07-31 |
|---|---|---|---|---|
| Regulated-7 (incl. D) | 10 | 2.084pp | **+0.39** | −4.89 |
| **Regulated-6 (excl. D)** | **6** | 2.028pp | **−0.99** | **−5.85** |

**⇒ Two independent effects, both against S35's fired branch A**: (1) removing the one name that is
not actually trading on the regulated-duration driver **cuts the crossing count from 10 to 6 in the
same window** — a real noise reduction, not cherry-picked (§1c's k=3 filter and this exclusion point in
the same direction); (2) **on the exact session S35 scored, the clean 6-name median never left negative
territory.** The **07-31 reading is also more negative without D (−5.85 vs −4.89)**, so this correction
strengthens the UW−, it does not soften it. **Recommended construction for both S35 and S47 going
forward: regulated-6, excluding D, until the merger closes** (a proposal, not an edit to the frozen
bracket text).

---

## 3 · The two legs, mapped and separated (W5) — carried from settled 07-31 flow, corrected for §2

**Sector flow (settled 07-31)**: wflow **−0.284** / eqflow **−0.289** · **1🟢 / 8🔴 of 15** · breadth
**0.07** · delta **−0.175**. Price: **XLU is the board's worst on every window** — exc5d **−5.29** ·
exc20d **−3.38** · exc60d **−7.57** vs SPY.

| Leg | Name | flow | RS20 vs SPY | RS60 vs SPY | vol_surge | Note |
|---|---|---|---|---|---|---|
| Regulated | WEC | −0.703 | — | — | — | |
| | ETR | −0.596 | — | — | — | |
| | EXC | −0.492 | — | — | — | |
| | SO | −0.610 | — | — | — | |
| | XEL | −0.604 | — | — | — | |
| | AEP | −0.824 | — | — | — | |
| | **D** | −0.103 | **−0.1** | **+7.7** | **0.42 (sector low)** | **★ merger-arb security (§2), not a clean regulated read — the RS60 "base" is convergence, not fundamentals** |
| | **PCG** | **🟢 +0.617** | **+1.6** | **+3.2** | — | the sector's only green, **4th consecutive run** |
| | SRE | 🔴 −0.657 | — | — | — | |
| AI-power (GICS: CEG=Utilities; **GEV/VRT=Industrials, stated**) | **CEG** | 🟡 **+0.539** | **+9.5** | **−21.2** | — | delta +0.306. Prints **2026-08-06** |
| | **VST** | 🟡 **+0.009** | **−2.2** | **−10.8** | — | delta **+0.573 — the sector's largest**. Prints **2026-08-07** |
| | GEV | 🔴 −0.611 | — | — | — | GICS Industrials |
| | VRT | 🔴 −0.233 | — | — | — | GICS Industrials |

**S24's frozen threshold** (median RS20 vs SPY of {VST, CEG, GEV, VRT} turning **> 0 by 2026-08-12**):
currently **−6.75** (this run's own reconstruction from the price series gives −6.77, ≤0.5pp diff,
consistent). Measured on the same 40-session window as §1: **this median's day-to-day σ is 3.76pp,
larger than the regulated leg's**, with **4 zero-crossings in 40 sessions** (vs 10 for the noisier
regulated-7). **8 trading sessions remain to 08-12; a cumulative move to zero requires +6.75pp against
a diffusion budget of roughly σ√8 ≈ 10.6pp — inside one noise-band of the threshold, i.e. S24 is
genuinely live, not foreclosed by construction the way S35/S47's near-term crossings are.** That is the
one live-bracket distinction this run draws: **S24's window and gap size make it a real test; S35 and
S47's near-term crossing behavior does not, on the numbers in §1.**

---

## 4 · The dated catalysts this promotion exists for — CEG 08-06, VST 08-07 — what they would have to show

**For S24 to move (median > 0 by 08-12), CEG and VST together need roughly +6.75pp of combined RS20
lift against SPY inside two print days plus a few sessions of drift** — that is a large ask from two
prints alone, but not an outlier one given the measured σ (§3). Concretely, each print's pass/fail:

- **CEG (08-06)**: needs a **new, named hyperscaler PPA or capacity-expansion disclosure** (the
  90-day EDGAR pull is still empty on 수주/계약/M&A — confirmed again this run, `module_disclosure_us
  CEG`) **or** guidance that raises contracted-nuclear capacity beyond what is already priced. **Absent
  that, a "beat and reaffirm" print is confirmatory-only (low information, same shape as S53's branch
  A)** — the RS20 +9.5 already reflects two weeks of accumulation into the date; a clean beat without
  new contract news would be the market getting what it already bought.
- **VST (08-07)**: needs the **estimate momentum this desk already measured** (+1y revisions 3↑:1↓
  as of 07-31, carried unchanged) **to show up in the print's own guide**, since flow has stayed flat
  (+0.009) despite the estimate moves — i.e. **the test is whether money finally follows the
  estimates**, not whether the estimates were right.
- **Anti-signal, stated per the mandate**: CEG's OBV state flipping to distributing **or** RS20 turning
  negative post-print ⇒ the accumulation read fails; a peer utility print (WEC/SO/AEP, all reporting in
  this window per the standard utility calendar — **not separately verified this run, flagged
  `[unverified]`**) showing a datacenter-load cut would hit the whole leg, not just the two names.

---

## 5 · W4 — customers named, checked against primary sources

**NextEra Energy raised its Florida Power & Light large-load forecast from 6 GW to 8 GW by 2032** — a
**+33% raise attributed explicitly to "hyperscale data centers and other large industrial customers,"
not population growth** `[yahoo_finance, body, 2026-07-31]`. This is disclosure-grade (an operating
utility's own forward planning number), and it is the cleanest demand-side print in this run's window —
but it is **NEE's own system**, not a named hyperscaler contract, and NEE is the entity about to absorb
D (§2), so this is also, mechanically, **evidence for the acquirer's book, not the target's.**

**Dominion Energy targets its CVOW (Coastal Virginia Offshore Wind) final turbine installation by
end-2027, with the project's cost estimate moved to $11.65bn**, disclosed on D's own Q2 2026 earnings
call `[seekingalpha, body, 2026-07-31, "Earnings Call Insights: Dominion Energy (D) Q2 2026"]`. This is
a **capital-cost figure on an owned generation asset**, not a customer contract — it is context for
D's balance sheet heading into the NEE merger, and it does not carry a hyperscaler-demand signal on its
own.

**"Coal back in favour as US plant bidding war highlights rising demand to power AI"** `[ft, TITLE
ONLY — the body was not returned by this run's news pull]`. **Flagged `[unverified]` per the mandate's
own rule**: the headline is directionally consistent with the demand thesis (a supply-side bidding war
implies buyers competing for generation capacity), but **no primary figure or named buyer/seller is
confirmed here** — it is not cited as evidence for any proposition, only as an unresolved lead.

**Westinghouse Electric filed confidentially for a US IPO.** Confirmed with a primary detail this
run's earlier reads did not carry: **Westinghouse is a Cameco (49%) / Brookfield Renewable (51%) joint
venture**, not a name on this desk's tracked universe, filed a **confidential draft S-1** with **no
share count, no price range, and no determined timing** — one analyst quoted in the same piece says
**"the potential IPO window remains broad and could extend as far as 2029"** `[mining.com, body,
2026-07-31]`. **⇒ This is a capital-markets-appetite signal for the nuclear supply chain generally
(corroborating CEG's nuclear angle at one remove), not a near-term catalyst inside this DEEP's window,
and it names no hyperscaler spend at all.**

**CEG's and VST's own EDGAR, re-checked this run**: CEG's last-90-day filings carry **zero
수주/계약/M&A items** (9 filings total, all routine — 8-Ks, a 10-Q, one Form 4). VST carries **two
Item 1.01 Material Definitive Agreements (07-16, 06-30)**, both **financing** (accounts-receivable
securitization) — **not** named datacenter PPAs. **Both findings reproduce the 07-31 file's
conclusion**: the fresh hyperscaler-demand disclosure this leg needs sits on the **08-06/08-07 print
dates**, not in the trailing-90-day filing record.

---

## 6 · Is the AI-power leg turning, or bouncing? PREMORTEM's NO-BASE tags addressed directly

Applying the desk's own M149/M150 method (days-21-to-60 excess = rs60 − rs20) to both AI-power names,
reproducing PREMORTEM's underlying arithmetic from its Lens-1 table:

| Ticker | RS20 vs SPY | RS60 vs SPY | **days 21-60 (= rs60 − rs20)** | Read |
|---|---|---|---|---|
| **CEG** | **+9.5** | −21.2 | **−30.7** | **NO BASE.** A fresh 20-day accumulation sitting on top of a −30.7pp 60-day give-back — this is a bounce inside a drawdown, not a new base |
| **VST** | −2.2 | −10.8 | **−8.6** | **NO BASE**, smaller magnitude. Flow is flat (+0.009) and RS20 is itself still negative — there is no bounce to explain yet, only a stall |

**⇒ Answered directly, per the mandate: the AI-power leg is BOUNCING, not turning, on this test.**
CEG's +9.5 RS20 is real and it is accumulating on flow terms, but it is **arithmetically a partial
retrace of a much larger 60-day loss**, not a fresh breakout — the same distinction the 07-31 file
already drew ("EXTENDED-BUT-LIVE... fresh accumulation *inside* a 60-day drawdown, not a fresh
breakout") and PREMORTEM's numbers this run **quantify it rather than describe it**. **This does not
kill S24** — S24's threshold is about the median crossing zero, not about the shape of the base — but
it does mean **a CEG print that merely confirms the current trajectory extends a bounce, it does not
establish a base**, which sharpens §4's read of what the 08-06 print would need to show to matter.

---

## 7 · Binding-rule compliance, stated

- **C3 — no cheapness claim on any regulated name.** A regulated utility has no comparable gross-margin
  series; this file makes none. **D's case is the sharpest instance**: even its RS60 "base" (+7.7,
  §2/§3) is not a valuation signal — it is measured (§2) to be a merger-arbitrage convergence, i.e. not
  a fundamentals read of any kind.
- **D6 — OBV/🟢🟡🔴 never alone.** Every OBV-adjacent claim in §2/§3/§6 is paired with the RS pair or
  the flow score. **D's 0.42 `vol_surge` (sector low) is read together with the merger-arb mechanism
  (§2), not cited as an independent accumulation signal.**
- **n≈1 discipline.** §1 exists to formalize this: the 07-29 cross is measured as **1 of 40 sessions**,
  drawn from a population where **27% of "regime changes" self-reverse within one session** (§1b).
- **Lead/lag / unverified tags.** The coal-bidding-war item is explicitly `[unverified]` (§5, body not
  read). The utility-earnings-calendar claim in §4 is explicitly `[unverified]`. No lead/lag claim is
  inherited from outside this run's own measurement (W2).
- **Live brackets, status this run**: **S35** (fired A → 08-07, §1/§2 dispute the firing) · **S47**
  (fired B → 08-07, §1d shows branch B is the modal state, not a resolution) · **S24** (→ 08-12, §3/§6
  — genuinely live, currently bouncing not turning) · **S40** (capex-as-lease structure, → 09-30,
  no new observable this run — carried unchanged from EVENT_ALPHA Card 6).

---

## 8 · Track KPIs and anti-signals — dated observables

| # | Observable (benchmark SPY) | Now (settled 07-31) | Resolves / kills |
|---|---|---|---|
| 1 | **Regulated-6 median RS20 vs SPY (D121 fix, excl. merger-arb name)** | **−5.85** | **> 0 by 08-07 on a settled close** ⇒ the demote is genuinely wrong, not a basket artifact |
| 2 | Regulated-7 median RS20 vs SPY (S35, as currently defined) | −4.89 | > 0 by 08-07 — **but §1 says this metric alone is not adequate evidence either way at n=1** |
| 3 | **D/NEE price ratio (deal-convergence tracker)** | **0.796** (stated ratio 0.8138, 2.2% discount) | ratio *widening* back toward the 60-day-ago 0.65 ⇒ deal-completion risk re-emerging, D re-decouples from NEE and re-enters the regulated read; ratio *closing to ~0.81* ⇒ deal closing imminent, D should be dropped from the basket entirely |
| 4 | S47 spread (reg median − AI-power median) vs SPY | **+1.88pp** | **§1d: this is inside the modal 0–7pp band 70% of the time — treat as noise unless it exceeds +18.9pp (the 40-session max) on the upside or goes negative and holds 3+ sessions** |
| 5 | AI-power-4 median RS20 vs SPY (S24) | **−6.75 / −6.77** (this run) | **> 0 by 08-12** — session budget analysis (§3) says this is a live test, unlike #2 |
| 6 | CEG days-21-to-60 (rs60−rs20) | **−30.7 (NO BASE)** | turning positive (rs60 catching up to rs20) ⇒ bounce becomes a base |
| 7 | VST days-21-to-60 (rs60−rs20) | **−8.6 (NO BASE, smaller)** | flow turning ≥ +0.3 **with** RS20 > 0 together ⇒ money starts following the estimate momentum |
| 8 | CEG EDGAR 수주/계약/M&A count (90d) | **0** | any new hyperscaler-PPA filing ⇒ the 08-06 print gets a fundamentals leg, not just a flow leg |

**Anti-signal to this file's own D121 finding**: if the **regulated-6 (excl. D) median** ALSO crosses
positive on a settled close before 08-07 — not just the contaminated 7-name version — **that would be
real evidence against the UW−**, because it would survive the basket correction this run makes.
**Anti-signal to the merger-arb read**: the D/NEE ratio decoupling (correlation falling below ~0.5 on a
rolling 20-session window) would mean the market is pricing deal risk again and D's price action
reverts to being a genuine regulated-sector signal.

---

## 9 · Verdict for BET

**The whole-sector UW− should STAND, and this run's work makes the case for it CLEANER than 07-31's
did, not weaker.** (1) **D121 is confirmed with numbers**: the regulated-7 median RS20 crosses zero
roughly every 4 sessions (10/40) with a measured σ of 2.08pp, so a same-day sign test is expected to
misfire on pure noise about once a month — **S35's fired branch A (a +0.39 single-session print, a
1.1σ move) is not distinguishable from that noise floor.** (2) **A structural defect compounds it**:
**D, one of the seven names in the basket, is a merger-arbitrage security tracking a fixed NEE exchange
ratio (0.8138), not a rate-sensitive regulated utility** — its 60-day RS strength is deal-convergence,
not fundamentals, and **removing it from the basket means the 07-29 median never crossed zero at all
(−0.99), and the current reading is more negative, not less (−5.85 vs −4.89).** (3) **S47's "branch B
fired" reading is the modal state of the spread series 70% of the time**, so it resolves nothing on its
own. (4) **The AI-power leg is measurably bouncing, not turning** (CEG days-21-60 = −30.7, VST = −8.6,
both NO-BASE by the desk's own method) — **S24 remains the one genuinely live bracket in this cluster**,
with a session-budget analysis (§3) showing its remaining gap is inside one noise-band, unlike S35/S47's
near-term crossings. **Recommendation for a human: adopt the regulated-6 (excl. D) construction for
S35/S47 until the NEE-D merger closes, and/or apply a k≥3-session persistence filter to both — either
fix would have prevented this run's own bracket disagreement from firing on noise.**

---

## ✅ EXIT CHECK

- [x] **#1 deliverable answered with numbers, not assertion (§1)**: 40-session crossing count (10),
      measured σ (2.08pp), fraction of readings within 1σ of zero (60%), and a k≥3 persistence /
      band-width fix proposed with the σ it is based on stated.
- [x] **Two legs mapped and separated (§3)**, GEV/VRT explicitly stated as GICS Industrials.
- [x] **Dated catalysts (§4)**: CEG 08-06 / VST 08-07, what each would have to show, both branches.
- [x] **W4 customers checked against primary sources (§5)**: NEE 8GW (body-read, `[yahoo_finance]`),
      Dominion CVOW $11.65bn (body-read, `[seekingalpha]`), coal item flagged `[unverified]`
      (title-only), Westinghouse IPO corroborated with its own caveats (JV structure, no
      valuation/timing). CEG/VST EDGAR re-checked (0 / 2-financing-only).
- [x] **PREMORTEM's NO-BASE tags addressed directly (§6)**: CEG −30.7, VST −8.6, reproduced from the
      desk's own M149/M150 method; verdict stated as "bouncing, not turning."
- [x] **C3 — no cheapness claim on any regulated name**, D's case stated explicitly as non-fundamental.
- [x] **D6 — OBV never cited alone**; D's `vol_surge` 0.42 paired with the merger-arb mechanism.
- [x] **n≈1 discipline**: the 07-29 cross explicitly measured as 1 of 40 sessions with a stated
      self-reversal base rate (27%).
- [x] **Live brackets recapped with status**: S35 · S47 · S24 · S40.
- [x] **New finding not in any 08-02 upstream file**: D is a merger-arbitrage security (§2), with its
      own primary-source verification (EDGAR 425/DEFM14A stack, exchange ratio, price-ratio
      convergence) and a quantified consequence for the D121 instrument test.
- [x] **KPIs + anti-signals as dated observables (§8)**, explicit verdict on the UW− (§9).
- [x] Linter — 0 findings.

**Linter**: `python -X utf8 scripts/report_lint.py llm_outputs/2026-08-02/industry_US/SECTOR_DEEP_UTIL.md`
→ **✅ 0 findings** across rules C1 · C2 · S6 · D6.

---

*asof 2026-08-02 · flow asof 2026-07-31 settled · own price reconstruction from
`llm_outputs/sector_flow/prices_2026-08-02.pkl` (2026-04-01 → 2026-07-31, 84 sessions) cross-checked to
the desk's published 07-29/07-31 medians (±0.00pp). Analysis only, zero buy/sell, zero sizing (P4).*
