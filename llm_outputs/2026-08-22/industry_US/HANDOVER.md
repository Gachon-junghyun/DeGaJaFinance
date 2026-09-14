# HANDOVER — industry_US · 2026-08-22 (Sat) · Stage 2/11 · L1·HANDOVER

> Inheritance packet. **This stage transports analysis; it makes no market call, names no size and
> issues no buy/sell language (P4).** Run clock **KST 22:09–23:0x = ET 09:09–10:0x, SATURDAY — US cash
> CLOSED all day.** Terminal settled bar throughout: **2026-08-21 (Friday close)**.
> Read: `handoff/STANDING_VIEW.md` (spine §1–§6 + §5 retracted ledger through **`R92`**) ·
> `STANDING_VIEW_US.md` (§2 fact table, §3a per-name rows) ·
> `SCENARIOS.md` (spine: scoring log + MASTER INDEX) ·
> `SCENARIOS_US.md` (**S1–S111**, opened in full for past-dated rows) ·
> `SCENARIOS_KR.md` (**opened** — the other market's file is this run's to score if past-dated) ·
> `RESEARCH.md` (Part A triggers · Part B lenses · Part C dig list through **`D306`** / **`D308-KR`**).

---

## ★★★ The three things this packet exists to hand forward

1. **A carried claim from yesterday's own run is FALSE and is retracted here (`R93`).** *"Kevin Warsh's
   Jackson Hole debut is TODAY, 2026-08-21"* — measured today: the symposium is the **August 27 to
   August 29 event** (`economictimes` body, 08-22, verbatim). The desk **manufactured a D-0 binary that
   did not exist**, and in doing so overwrote a HANDOVER sentence that was **correct**. §7.
2. **`C11` — an open contradiction carried since 08-19 — is RESOLVED today, and only a Saturday could
   have resolved it.** Market closed ⇒ zero clock difference ⇒ if the two OBV instruments were a clock
   artifact they had to agree. **5 of 5 still disagree.** Reading both sources settles it: they compute
   **different quantities** (level vs. rate-of-change of signed volume). §8.
3. **The desk's own pre-registered kill-threshold for `vol_surge` has been crossed** — `t(NW) −3.86`
   at h=1 and `−3.38` at h=5, both past Bonferroni `|t|>2.8`, both `n_eff ≥ 4`. **And `W1` forbids this
   run from acting on it**, because the ledger is `market=kr`. §6.

---

## §0 · Instrument health inherited — what this run may NOT claim

`llm_outputs/2026-08-22/preflight/PREFLIGHT_US.md` **was run** (22:09–22:22 KST, this run's own stage
−1). **PASS 3 / FAIL 5.** The rights table binds every stage below and is not re-litigated here.

**Revoked for this run:** the sweep's news-velocity axis · theme freshness · any "it went quiet"
sentence sourced from the sweep · the velocity survivors **as a set** · the **Consumer Staples `wflow`
sign** (`WMT` at 28.9% owns it) · any concentration number without its `--days`, **and today not even
as a single count** · how concentrated the **AI-compute** book is · `wflow` cap-weights described as
*current* (weights are **38 days** old) · any flow/RS/OBV/short call on **`EA`** · `--ic`-derived sizes
as evidence-backed · **any 2026-08-22 price** (there is no Saturday bar).

**Granted:** settled prices and every price-derived statistic through the **2026-08-21** close · a
**one-session Δ (08-20 → 08-21)**, the fourth clean single-session Δ in a row · `flow_score`, RS, OBV,
`vol_surge` · `eqflow` for all 11 sectors and `wflow` signs for the ten non-flippers · **today's tag
layer and green set** (see the correction below) · FINRA short pressure · CFTC COT · FRED · primary
filings · `module_chart --read` and `margin_history <T>` (with the "`--help` dead, output probed"
stamp) · hand-probed per-name news velocity (**40/40 valid at 22:14 KST**).

★ **The instrument fact that changes how every downstream stage should spend its news budget.** The
news axis's failure is no longer a description; it is a measured mechanism: **a budget of ≈100 remote
calls (≈51 names at 2 calls each), a hard contiguous wall, and a ≈90-second cooldown.** Two sweeps run
four minutes apart on one price frame returned **16.4%** and then **0.0%**; a 150-name hand burst
returned **51 ok / 99 fail with the cut at index 51 and no gaps on either side**; a single-call probe
recovered at **22:17:57**, ~100 s after the burst drained it. The tunnel answered **3536** before the
sweeps and **3536** after. ⇒ **The desk is not starved of news. The desk spends its whole news budget
on a 299-name loop and then discards 96% of the answers**, because the axis is dropped below 80%
coverage — which it always is. **Any stage needing news today should spend ≤50 names at a time on the
handful it actually cares about.**

⚠ **Correction made inside this run and kept visible rather than edited away (`§4c`/`D48`).** The
preflight's first draft revoked `breadth`/`green`/`red` outright. **The ledger audit in §3 refuted it**
— a `missed_ledger` row (`CBRE`) whose condition reads *"enters the green set on an admissible
(non-velocity) axis"* forced a source read. With `vel = None` the green term `(vel or 0) >= 1.2` and
the red term `(vel is not None and vel < 0.7)` are **both False**, so the tag collapses to a pure
3-axis price function. **The persisted file has `velocity: null` on all 299 names**, therefore
**today's tags are provably velocity-free and ARE citable** — as *3-axis unanimity*, never as
*news-confirmed*, and **never compared to an earlier run's breadth** (every prior run had partial
coverage).
★★ **The corollary is the sharper half**: zero coverage is *uniform*; partial coverage is
*selection-biased upward*. **The sweep that failed hardest at news produced the cleanest tag layer in
this ledger.** Yesterday's run measured *"3 of the 7 greens are velocity-derived ⇒ admissible green
count 4"* (`R81`/`D290`, 11th measurement). **Today the admissible green count equals the printed green
count: 6 of 6.** First time in the series.

⚠ **Two carried rules travel with the granted Δ into SWEEP and ROTATION, unchanged:**
- **`D293`** — `sector_flow` publishes `delta` but not `rs20_earned` / `rs20_rolloff`. Today's Δ spans
  **one** session, so the roll-off share is one session in twenty — smaller, **not zero**.
- **`R81`/`D290`** — `flow_tag` does not take the run-level axis set. **The rule is unchanged; today it
  simply has nothing to bite on**, because the axis set is empty for every name. It re-binds the moment
  a run gets partial coverage again, which is every other run.

---

## §1 · Inherited regime call and standing view

**Regime (spine §1, `[inferred]`, unchanged):** *memory is a price-cycle industry in rate-of-change
deceleration while its level stays tight* — the equity tracks the **second derivative** of price, not
the level, which is why "shortage persists" and "stocks struggle" are both true.

★ **That sentence turns out to describe this desk's own instruments too** — see §8, where the two OBV
tools are shown to be a level reading and a rate-of-change reading of the same series, and were being
compared as if they measured one thing.

**Carried per-name theses (§3a).** Tags preserved; no `[inferred]` row is passed downstream as
evidence. The right-hand column is **this run's own measurement on the 08-21 settled close**.
⚠ Per `C11`'s standing constraint, every OBV figure below names its instrument: all are the **sweep's
`obv_norm` (20-session change of a cumulative signed-volume series ÷ 20-day mean volume)**, read on the
**settled 2026-08-21 bar with the market closed**.

| Node | Carried state | Tag | Measured today (08-21 settle) |
|---|---|---|---|
| **`MPC` · `PSX` · `VLO`** | Refining-**capacity** destruction; the constraint is `L2` peak margin, not the barrel | `[measured]` price · `[filing]` structure | 🟡 PARTIAL ×3. flow **+0.700 / +0.728 / +0.506**, rs60 **+44.0 / +37.0 / +43.1**, all three OBV 매집. **`S88` settled C** (§2). ⚠ **`P70` MISSED on its control leg** — `BZ=F` 5-session **+6.631%** against a **≤ +2.0%** bar ⇒ `R89`'s retraction of the separation claim is **confirmed by the settle, not merely anticipated**. ★ New: **`VLO`'s gross-margin percentile is measurable after all** — FY2025 **4.43% = 50th percentile of 10 years** (§3) |
| **`RTX`** | The defense group's **beta**, not its leader; the book's diversifier | `[measured]` | 🟡 PARTIAL. flow **−0.122**, rs20 **−5.0**, rs60 **+16.8**; OBV **neutral +0.023** — it has left accumulation, and its **delta −0.304 is the book's largest single-session deterioration** for a second consecutive run. ⚠ **`M778` measured `ETN`–`RTX` at −0.006**, so the diversification claim survives. **Customer still unmeasured, now 205 days (`W4`)** |
| **`LHX`** | Succession priced as a **discontinuity** (`S97` FIRED-A, scored by the sibling desk) | `[measured]` | 🟡. flow **−0.113**, rs20 **−14.8**, rs60 **−15.7**, OBV 중립, `vol_surge` **1.21**. ⇒ **`M704`'s defense EW must be re-run ex-`LHX`** — carried to DEEP as an obligation, not a note |
| **`NUE`** | Post-earnings re-rate; the 08-21 packet corrected its stale FINRA sentence to **z −2.33 (covering)** | `[measured]` | 🟡. flow **+0.319**, rs20 **−5.2**, rs60 **−3.2**, OBV 매집 **+0.148**, `vol_surge` **1.41** — clears 1.2 but **fails the rs20 leg**, so it is not 🟢. 🚨 **It is also one of the five `C11` names and it inverts: chart-OBV slope −71% vs sweep 매집** (§8) |
| **`T`** | 🚨 An orphan position — **9.74%** of the real book's invested, no cycle label, no card | `[measured]` | 🟡. flow **+0.089**, rs20 +1.2, rs60 **−0.4**, OBV 매집 **+0.296**, `vol_surge` **0.47** — the lowest surge on the carried set for a second run. `S107` → **09-03** |
| **`WMT` · `TGT`** | The Staples carriers, and they disagree | `[measured]` | 🚨 **The disagreement widened again and it is now the sector's whole sign.** `TGT` flow **+0.950 🟢**, rs20 +17.3, rs60 **+26.9**, OBV 매집, surge 1.51. `WMT` flow **−0.333 🔴**, rs20 −8.9, rs60 −14.6, OBV **분산**, surge **1.68**. **`WMT` is today's G3 flipper** — the sector reads −0.013 on `wflow` and **+0.116 ex-Walmart**. `S93` **VOIDed** (§2) |
| **`GOOGL`** | Half the COMM underweight is already wrong | `[measured]` | 🟡. flow +0.245, rs20 +4.2, rs60 **−13.4**, OBV 매집 +0.135. ⚠ It has **left** the flipper set (yesterday it was it) — COMM +0.108 → ex-top1 **+0.022**, same sign. **`D297` still unfixed**: `GOOG` is a second 38.3% row, so the Alphabet complex is **76.6%** of the sector while `top1_w` reports half |
| **`KKR` · `LITE` · `ORCL`** | Cross-sector orphans, carried because their sectors hold no DEEP slot | `[measured]` | 🟡 ×3. `KKR` +0.458 (**delta −0.193**) · `LITE` **+0.639, delta +0.236** · `ORCL` +0.444 with rs60 **−25.3** |
| **`XOM`** | 🔴 RESOLVED — the crack-attribution **control**, and a control is not a bet | `[measured]` | **It has turned negative**: flow **−0.183**, OBV **분산 −0.101** (it was 중립), delta **−0.200**. Ledger `A.flow미도착` → **09-16** |
| **`NEM` / `FCX` / the `Copper` COT** | 🔴 RESOLVED — survives as a risk, not a thesis | `[measured]` | 🚨 **`NEM` fired `S89` branch B** (§2): exc5 **+13.104**, rs20 **+37.6**, OBV 매집 **+0.487** — the highest `obv_norm` on the whole board. ⚠ **`M779` measured 246.4% of its rs60 in the last 20 sessions** (days 21–60 negative) ⇒ branch B fired **on exhaustion geometry**, which is `D306`'s exact defect class |
| **The optical/interconnect cycle** | 🚨 `cycle_registry.json` has **no row** for it ⇒ exposure is **unmeasurable, not zero** | `[measured]` | **`S86` and `S96` both settled B** (sibling desk). Today the three names have re-converged downward: `LITE` **+0.639** OBV 매집 · `COHR` **+0.158** OBV 중립 (delta +0.207) · `CIEN` **−0.380 🔴** rs60 **−34.0**. `D250`/`M731` unfixed |

**Settled 08-21 read on the 11 book names** (three-axis; tags stated separately and admissible today):

```
PSX  +0.728 rs20 +13.8 rs60 +37.0 OBV accum   surge 1.11  d −0.005    MPC  +0.700 rs20 +13.0 rs60 +44.0 OBV accum   surge 1.06  d  0.000
HPE  +0.489 rs20  +8.5 rs60 +41.6 OBV accum   surge 0.68  d +0.002    ANET +0.417 rs20  +4.8 rs60 +20.2 OBV accum   surge 0.82  d +0.384
NUE  +0.319 rs20  −5.2 rs60  −3.2 OBV accum   surge 1.41  d +0.095    ETN  +0.210 rs20  +0.1 rs60  +1.1 OBV accum   surge 0.77  d +0.285
NDAQ −0.025 rs20  +3.0 rs60  +6.5 OBV neutral surge 0.67  d −0.004    RTX  −0.122 rs20  −5.0 rs60 +16.8 OBV neutral surge 1.07  d −0.304
MET  −0.164 rs20  −4.1 rs60 +11.4 OBV neutral surge 0.87  d +0.011    NVDA −0.181 rs20  +0.2 rs60  −1.0 OBV neutral surge 0.75  d +0.018
AVGO −0.221 rs20  −7.2 rs60 −14.7 OBV neutral surge 1.00  d +0.176
```

★ **All 11 are 🟡 for a second consecutive run — not one green, not one red.** ⚠ And today that
sentence carries an instrument caveat it did not carry yesterday: with the news bucket empty the tag
layer has **one fewer axis available to push any name off neutral**, so "all neutral" is partly a
property of the instrument. **Do not read it as a market statement.**
★ `ANET` improved most among the eleven (**delta +0.384**, flow +0.033 → +0.417) and `AVGO` recovered second-most (**+0.176**, −0.397 → −0.221);
`ETN` is third (**+0.285**) — ⚠ and `M778` says that delta belongs to
**`XLI`** (β +1.402, t +6.12) rather than to the AI-compute basket, so it is **not** a compute datapoint.

### Retracted ledger read BEFORE forming today's view (spine §5, through `R92`)

The six that bind this run:
- **`R78` · `R81`** — *a 🟢 tag is not evidence while `vel_axis=false`*. **The rule stands and today it
  has nothing to bite on** (all 299 velocities null ⇒ every tag is price-only). It re-binds next run.
- **`R82`** — the **Consumer Staples UW− → UW promotion is withdrawn**. ⚠ Directly live today: Staples
  is **this run's G3 flipper**, and the flipper works *against* the sector (`wflow` −0.013 vs ex-`WMT`
  +0.116). **No stage may promote or demote it on the `wflow` sign.**
- **`R80`/`R84`** — the "survivor set is deterministic / burnt in the first 51 tickers" shape was
  retracted in both markets. 🚨 **This run RE-OPENS that question and lands on the opposite side, with a
  direct experiment rather than an inference** — see §0 and PREFLIGHT ①. **The retraction is not being
  laundered**: `R80`/`R84` killed the claim *about the sweep's survivors*, which remain scattered; what
  is measured today is the **underlying budget**, which the scatter never disproved.
- **`R87`/`D298`** — any carried claim containing a **COUNT** or a **STATE** needs re-computation each
  run. **Applied twice today**: the refiner kill counter (`P70` re-scored on the true 08-21 settle, not
  carried) and `NUE`'s FINRA sentence (already corrected 08-21, not re-carried stale).
- **`R89`** — the refiners' *separation* claim. **Its settle arrived today and confirms the retraction**:
  `BZ=F` 5-session **+6.631%**. The thesis survives; the separation does not.
- **`R90`** — `P65`'s bull-steepener framing. **Unchanged today**: `DGS2` **4.19** (pinned, 10-obs range
  4.15–4.25), `30y−10y` **0.54**, below its own 252-obs median.

**Nothing in this packet re-argues a retracted claim.** ⚠ One thing in this packet **retracts a claim of
its own predecessor** — §7, `R93` — and it is filed with the measurement that killed it, not asserted.

---

## §2 · Scenarios — five scored, two VOIDed, one not-yet-arrived, four P-rows settled

### (a) Already scored by the sibling desk this morning — verified, not re-scored

The `industry_kr` run (08:2x–09:5x KST) scored the **nine** US-owned rows whose 08-21 settle had
arrived at 05:00 KST. This desk opened `llm_outputs/2026-08-22/industry_KR/HANDOVER.md` §3-a and
**verified the entries exist**; ownership confers no exclusivity (README §3).

**`S84` C · `S85` C · `S86` B · `S87` A · `S95` A · `S96` B · `S97` A · `S99` A · `S100` C.**

★ The sibling desk's own headline on `S99` is carried forward verbatim as an input, because it is a
**sizing** fact: *"the verdict is recorded as A, and the concentration guard does not move on this A"* —
`M778`'s joint regression pre-declared branch A a false positive on the **label** question.

⚠ **One measurement discrepancy, recorded (`D5` class, new instance).** `BZ=F` **2026-08-21 settled
close** reads **93.870** in the sibling desk's 09:3x KST pull and **94.390** in this desk's 22:2x KST
pull — **same provider, same ticker, same settled session, 13 hours apart, 0.52 apart (0.55%)**. Both
readings sit above `S95`/`P69`'s A threshold of 93.00, so **no verdict moves either way**; the defect is
logged rather than reconciled away (§9, `D307`).

### (b) Scored by this run — the five rows the sibling desk did not take

All are **5-session excess vs `SPY`**, settled closes, window **2026-08-14 → 2026-08-21**,
`yfinance auto_adjust=False`, benchmark named inline (`C1`). **`SPY` 5-session return = −1.368%**
(776.34 → 765.72) — identical to the sibling desk's independently-computed figure, which is the
cross-check.

| ID | Observable (measured) | Frozen bands | **Verdict** | Effect on the standing view |
|---|---|---|---|---|
| **`S88`** | `EW{MPC +2.859, VLO +3.472, PSX +5.332}` = **+3.888** | A ≤ +0.061 · B ≥ +8.144 | **FIRED-C** | **The ENRG OW promotion is not falsified.** ⚠ Read the information content honestly: **A was the row's entire content** (B was declared NO-INFORMATION at registration), and A needed a **−15.6pp** collapse from a 100th-percentile state. **C was overwhelmingly the favourite and C is what came.** The row bought little. ★ What it *did* buy is the `VLO` ledger leg (§3) |
| **`S89`** | `NEM` exc5 = **+13.104** | A ≤ −5.217 · B ≥ +9.658 | **FIRED-B** | **The gold run is live, not exhausted.** ⚠ **Anti-signal checked FIRST, as the 08-21 packet pre-committed**: `GC=F` 4380.4 → 4624.1 = **+5.563%** over the window, inside the **±8%** void band ⇒ **NOT fired, the row scores.** ⚠⚠ But `M779` measured **246.4% of `NEM`'s rs60 sits in the last 20 sessions** (days 21–60 negative) ⇒ **B fired on exhaustion geometry**, the `D306` class. **B is a price fact; it is not evidence the run has a base under it** |
| **`S90`** | `DLR` exc5 = **−3.393** | A ≤ −3.199 · B ≥ +5.223 | **FIRED-A** *(anti-signal examined, not fired — see below)* | **The Real Estate accumulation was LATE.** This goes against the 08-21 run's own RE promotion, and it is recorded as such |
| **`S91`** | `XLY` exc5 = **+1.216** | A ≤ −2.467 · B ≥ +1.553 | 🚨 **VOID** | Its anti-signal fired unambiguously (below). ⚠ **Note what is being given up**: the un-voided reading was **C by 0.337pp from B** — the narrowest estimator on the board (sd 1.639) landing a third of a point from an informative branch, and the void throws it away |
| **`S93`** | `WMT` **−8.669** · `HD` **+0.409** · `TGT` **+8.463** · `ABNB`−`HD` **+2.719** | A = all three negative · B = `TGT`+ while `WMT`,`HD` − , OR spread > +5 | 🚨 **VOID** | Un-voided it was **C** (A fails on `HD` and `TGT`; B fails on `HD` and on the +2.719 OR-leg). ★ **But the void is the more interesting outcome** — see below |

**`S91`'s anti-signal — FIRED.** *"a September-FOMC-dated headline or an inflation print in window."*
Measured, `--scope foreign`, window 08-14 → 08-21: `investing_en` **2026-08-20** — *"Fed's Musalem says
on CNBC he won't prejudge rate call view for **September FOMC**"* — a literal September-FOMC-dated
headline; plus `fool`/`yahoo_finance` **08-14** *"Despite Lower Odds of a **September Fed Rate Hike**…"*;
plus the **FOMC minutes of 08-19**; **219 hits** on `September AND FOMC` over the 8 days. Second leg
independently: the **UMich inflation-expectations release, 08-14**, inside the window.

**`S93`'s anti-signal — FIRED, and it fired ON THE BRACKET'S OWN NAMES.** *"a tariff announcement
affecting consumer goods inside the window."* Measured: **2026-08-21**, three outlets — `bloomberg`
*"Trump to Allow Tariff Relief for Certain Ground Beef Imports"*, `scmp` *"Trump eases tariffs on ground
beef imports for 90 days"*, `fortune` (same event, with the mechanism). And separately `forbes` 08-21:
*"Americans' Top Retailers Are Getting Billions In Tariff Refunds — Including **Walmart, Target**"*.
⇒ **The void condition landed on two of the bracket's three legs by name.**

★★ **Two VOIDs in one batch, and both are the SAME construction defect — `D300-KR`, now measured for a
third time in six days** (`S98` VOIDed 08-21 on an FOMC communication inside an 8-day US window). **An
8-calendar-day US window essentially always contains an FOMC/CPI/PPI communication and almost always a
tariff headline.** These anti-signals were **designed to void**. The 08-21 run applied a base-rate check
to `S108`–`S111` precisely because of this; **`S91` and `S93` predate that fix and are its cost, paid
today.** ⇒ Registered as this run's #1 rule to carry into PREMORTEM (§9).

**`S90`'s anti-signal — examined and NOT fired, on two independent grounds, both recorded.**
The clause: *"`DLR`-specific acquisition or guidance event ⇒ name event, not node read."*
1. **Strict reading of what happened.** `module_disclosure_us DLR` shows an **8-K + 424B7 on
   2026-08-19**, inside the window, matching the `investing_en` headline *"Digital Realty Trust registers
   resale of shares issued in Columbia Capital acquisition."* But this is a **resale registration of
   shares already issued** in a previously-closed acquisition, and it is the **third in a recurring
   series** (424B7 on 06-29, 8-K+424B7 on 07-01, 8-K+424B7 on 08-19). **No acquisition was announced and
   no guidance was issued** — the last Item 7.01 guidance 8-Ks are **06-22 and 06-29**, the 10-Q is
   **07-31**, all before the window.
2. **The clause's own purpose, tested.** It exists to catch *name event, not node read*. **The peer
   decomposition refutes a name event**: over the identical window, `DLR` **−3.393** travels with
   `EQIX` **−1.963** and `IRM` **−4.357**, while the rest of the sector goes the other way — `XLRE`
   **+0.948**, `AMT` **+1.493**, `PLD` **+1.914**, `WELL` **+2.939**. **The digital-infrastructure node
   moved; `DLR` did not move alone.**

⚠ **And the disclosure that keeps this honest**: branch A is the branch that **costs** this desk — it
says the 08-21 run's own RE promotion was late. Choosing the reading that scores the row is choosing
the reading that convicts the desk, which is why it is defensible. **The construction defect is
registered anyway** (§9, `D308`): a node-vs-name bracket should be written on a **peer-relative**
observable, not a raw excess, so the anti-signal never has to arbitrate.

### (c) Not yet arrived — `S102`, second consecutive run, and now the reason is structural

**`S102`** — observable *"`[FRED]`, the first close covering 2026-08-21"*: `DGS2` ≥ 4.30 (A) /
`DGS2` ≤ 4.08 ∧ `30y−10y` ≥ 0.59 (B).
**FRED's last observation on `DGS2`/`DGS10`/`DGS30` is still 2026-08-20** — a **third** independent
pull (the sibling desk made two this morning; this is the third, ~14 hours later). Values at 08-20:
`DGS2` **4.19**, `30y−10y` **0.54**. **They are NOT substituted** — changing the observable after the
fact converts a prediction into a narrative.
🚨 **The reason it has slipped twice is now diagnosable and it is not a data problem**: FRED daily
series do not publish on weekends, and **the row's settle date (Friday 08-21) can only be read by a
Monday-or-later run.** A Saturday desk cannot score it by construction. Registered as `D309` (§9):
**a bracket on a FRED daily series must settle on the first BUSINESS DAY after the release, not on the
market close.** ⇒ **`S102` is scoreable by the 08-24 run and is handed to it explicitly.**

### (d) The P-row pre-commitments settling 08-21 — the 08-21 asof chain named five

| ID | Registered test | Measured on the **true 08-21 settle** | Verdict |
|---|---|---|---|
| **`P65`** | `30y−10y` ≥ 0.58 ∧ `DGS2` ≤ 4.15 | `30y−10y` **0.54** ❌ · `DGS2` **4.19** ❌ | **MISS on both legs — already retracted as `R90`.** Unchanged by today's data |
| **`P66`** | The Russia supply-destruction leg survives independently of Hormuz | **CONFIRMED and still being reported inside the window**: `toi` 08-17 *"Russia faces fresh fuel shortages as refinery attacks disrupt supplies"* · `oilprice` 08-17 *"Russia Receives First Gasoline Cargo From India as Fuel Shortages Spread"* · `cnbc` 08-19 *"Diesel in California rises to $7 a gallon as wars in Europe and Middle East strain supply"* | **HOLDS** |
| **`P69`** | Does a Hormuz shutdown reprice crude at all? A ≥ 93.00 · B ≤ 86.50 | `BZ=F` 08-21 settle **94.390** (this desk) / **93.870** (sibling desk) | **FIRED-A on both readings.** ★ The answer to the registered question is **yes — the barrel repriced.** It is the twin of `S95`-A and they agree |
| **`P70`** | `EW{MPC,PSX,VLO}` exc5 ≥ +2.0 **∧** `BZ=F` 5-session ≤ +2.0% | EW **+3.888** ✅ · `BZ=F` 5d **+6.631%** ❌ (bar +2.0%) | **MISS — the conjunction fails on the control leg by 4.63pp.** ⇒ `R89` is confirmed at settle: **the refiners did NOT pay without the barrel this week** |
| **`P75`** | *"the crack ≥ 95"* ∧ EW exc5 ≥ +2.0 | 3-2-1 crack **69.61** ❌ · distillate crack **101.72** ✅ · EW **+3.888** ✅ | 🚨 **CLOSED AS UNSCOREABLE-BY-CONSTRUCTION (P5), third consecutive recording.** The branch names *"the crack"* and the two series answer oppositely — as they did on 08-19 (67.64 / 101.17) and 08-20 (66.26 / 100.34). **A third deferral would be extinction, not caution** (the sibling desk's `S64-KR` precedent this morning). `P80`/`P83` are the successors and name both series explicitly |

★ **A reading the P-rows deliver jointly and no single row states.** Over 08-14 → 08-21 the **distillate
crack rose 97.48 → 101.72** while the **gasoline crack fell 51.33 → 53.55 through a 49.21 trough** and
**Brent rose 6.6%**. The refiners' excess (+3.888) came with the barrel this week, not despite it —
**but the distillate−gasoline spread (`P83`'s instrument) is 48.17 and was 51.13 on 08-20**, i.e. it
**narrowed 2.96 into the settle**. `P83` settles 08-27 and this is its pre-settle reading, not a score.

### (e) Still armed beyond this window, with dates

**08-24**: `S74` · **08-25**: `S108` (⚠ see §7 — its premise is void) · **08-26**: `S79` `S101` `S103` ·
**08-27**: `S81` `P83` · **08-28**: `P67` `P81` `S111` · **08-31**: `S92` `S94` `S104` ·
**09-02**: `S109` · **09-03**: `S105` `S106` `S107` `S110` `P84` · **09-30**: `S48`.
⚠ **`S103`** (`NVDA` 08-26) still carries **hand-set ±5.0pp bands**. `D295` obliges a re-derivation from
the 08-26-or-later straddle before the print. **Third consecutive run unmet. The print is now four days
out — this is ALPHA's obligation today and it is the last run with slack in it.**

### (f) 🚨 `S8` — undated and unscoreable for the **20th** consecutive run

Still on `CATALYST_WATCH` as its undated 🔀binary (*"Iran 'Strait of Hormuz open' statement"*, axis=oil).
**A human must `VOID` it or re-register it with a date (P5).** `S92`/`S95` bracket what `S8` cannot.
⚠ **`S95` fired A this morning** — the axis `S8` was built for has now produced a scored outcome through
a *different* row, which is the clearest possible evidence that `S8` is dead weight.

**Score this run: 5 newly scored by this desk (`S88` C · `S89` B · `S90` A) + 2 VOIDed (`S91`, `S93`) ·
9 verified as scored by the sibling desk · 4 P-rows settled (`P66` holds · `P69` A · `P70` MISS ·
`P75` closed as unscoreable) · 1 not-yet-arrived with a structural reason and a named successor run
(`S102`) · 0 `EXPIRED` · 0 silent skips.**

---

## §3 · Both ledgers — audited symmetrically

`reject_ledger.py due` **and** `missed_ledger.py due` were both run (not `score` alone).

**At entry:** rejections **218 rows · 133 resolved · 0 past-due · legacy 0** ·
misses **198 rows · 106 resolved · 4 past-due · legacy 0**.
★ **Legacy count is 0 on both ledgers for the 11th run.** **The rejection ledger is completely clean
today — zero rows due** (first time in this series).

### Misses resolved (2 of 4)

| Ticker | Missed | Outcome | The measurement (08-21 settled close) |
|---|---|---|---|
| **`VLO`** | 08-15 | ★ **entered** | **Both legs met.** Leg 1: **`S88` settled C** ("C or B" as written) ⇒ the node did not mean-revert to its 2-year median. Leg 2 — *"a `VLO` gross-margin percentile becomes measurable"* — **it is measurable, and the blocker was our own tool.** `scripts/margin_history.py VLO` returns *"연간 데이터 없음"* because it looks only for standard tags; SEC XBRL carries the pair `RevenueFromContractWithCustomerIncludingAssessedTax` + `CostOfRevenue`, giving **FY2016–FY2025, n=10: FY2025 4.43% = 50th percentile**, median 4.60%, range **−1.14% (FY2020) to 9.52% (FY2022)**. ⚠ **Content, stated because the entry is not a recommendation (P4)**: the percentile is **dead median** while the price sits at **348.86 against a 52-week high of 352.70** and consensus mean target **−10.4% below spot**. The margin is not what re-rated this name |
| `CBRE` | 08-15 | **reaffirmed** | Both OR-legs fail on measurement. Leg 1: **`S90` settled A, not B**. Leg 2: `CBRE` is not in today's green set — flow **+0.425**, OBV 매집 **+0.378**, rs20 **+5.4**, rs60 **+14.8**, but **`vol_surge` 0.76 < 1.20**, so the 3-axis unanimity gate fails **on the volume axis alone** (`M25`/`M144` shape, 11th measurement). ★ **Note the leg was genuinely testable today** — it asks for an *"admissible (non-velocity) axis"*, and today's tags are provably velocity-free. **It did not fail for want of an instrument; it failed** |

### Misses carried, explicitly and with the reason — 2 of 4

- 🚨 **`APH`** (08-07, `U.발굴부재`) — **this is its SECOND HANDOVER past due, and the 08-21 packet
  pre-committed in writing that "it must not cross a second HANDOVER unresolved."** Leg 2 is measured
  and **fails cleanly today**: flow **+0.131**, tag 🟡, `vol_surge` **0.85** ⇒ no volume-confirmed 🟢
  (⚠ though its **delta +0.435 is among the largest positive one-session moves on the board**). Leg 1
  — *"IT or an adjacent sector takes a DEEP slot and a file names the connector node"* — **is a function
  of this run's own ROTATION and is not determinable at HANDOVER.**
  ⇒ **Binding obligation handed forward, not a note: ALPHA must call `missed_ledger.py resolve` on
  `APH` today, once ROTATION's DEEP slots exist.** If this packet's successor writes the same paragraph
  a third time, the pre-commitment has failed twice and that fact goes in the asof chain.
- **`009830` 한화솔루션** (08-15, `M.숏리스트탈락`) — **handed back to `industry_kr`, named rather than
  dropped.** Its condition (*"정유·화학 bucket holds ≥2.0× for two consecutive runs AND 🟢 is
  maintained"*) is written against the KR sweep, which this desk cannot run (`W1`). ⚠ **And the KR desk
  could not measure it either this morning** — today's `SECTOR_FLOW_KR.json` came back **`scored: 0`**
  after a single `NaN` in the `^KS11` benchmark took the whole 832-name sweep to zero. **The row is
  blocked on both desks and that is stated, not glossed.**

⚠ **Sign hygiene (`3c`)**: the two ledgers' `excess` columns are **inverted** relative to each other and
are **not summed** anywhere in this packet.
⚠ **`score` is accumulation, not an edge** — the miss ledger's first rows are outcome-selected.
★ Carried and still binding (`T25`): any structural rejection this run makes must re-print the
rejection ledger's loss-asymmetry number beside it.

---

## §4 · Exposure state — carried as size context for BET/ALPHA (read-only; this stage never logs)

`exposure_rule.py state` + `show --tail 10`, both run.

| Quantity | Reading |
|---|---|
| Rule state | **정상 (normal)**, prior state normal — *"no firing condition"* |
| Target invested | **95%** |
| Current invested | 🚨 **BLANK in `state`** — the account query was not supplied, so `state`'s own gap is unavailable today |
| Ledger's last row (08-21, **live** bar) | invested **85.1%**, band gap **−9.9pp** |
| Band-gap trajectory | −39.4 → −27.1 → −14.0 → −13.9 → **−9.9pp** — **closing, five consecutive readings** |
| Cumulative decomposition, n=11 | total excess **−16.64pp** = cash **−6.46pp** + **selection −10.19pp** |

★★ **The carried sign has INVERTED and this is the packet's most consequential size input.** The
07-31 reading that the spine carries was a **+16.86pp lead of which ~14pp was cash weight**, with
selection *"+2.54pp on n=11 with one name carrying it — indistinguishable from zero (`C4`)."* **The
cumulative is now −16.64pp, and selection (−10.19pp) is the LARGER drag, not cash (−6.46pp).**
⚠ **`C4` binds in exactly the same way it did then, and in the opposite direction**: n=11, so **no
stage may claim the desk's selection has a negative edge.** What may be said is narrower and true:
**the "our lead is cash, not skill" story is no longer supported by its own ledger**, because the sign
flipped on both components.

⚠ **Two standing flags carried, not acted on** (P4 — this is a research run):
- 🚨🚨 **`ARMED (TIMEFOLIO_EXECUTE=1)`** on every ledger row. **Named, not touched.** No stage in this
  protocol may pass `--execute`.
- 🚨 **`밴드미설정`/`투자비중미상` on `state`** ⇒ the 4-state verdict is quoted with its gap missing;
  **no number is substituted** (P5). The band gap above comes from the *ledger's* 08-21 row and is
  labelled **live-bar**, not settled.
- ⚠ Carried from memory and still true: `exposure_rule`'s `state` and `target` can diverge (the
  minimum-maintenance gate), so a completed plan is **not** citable as evidence. Human fix.

---

## §5 · Reconciliation — belief vs mechanical coverage

`module_report_tags show` cross-queried.

- **Coverage without belief:** `industry_US/SECTOR_DEEP_SEMI.md` is dated **2026-07-15** — **38 days**,
  the oldest US DEEP file on the board, and it covers **the AI-compute epicenter, where 4 of the 11
  book names live** (`ANET`, `AVGO`, `NVDA`, + `HPE` adjacent). ⇒ **Top-ranked DEEP candidate on the
  reconciliation axis**, carried to ROTATION.
- **Belief without coverage:** `T` (9.74% of the real book's invested) still has **no DEEP file, no
  cycle label and no card** — 🚨 and per `M152` it is one of **two book names (`MET`, `T`) that
  `module_report_tags ticker` cannot index at all**, so this instrument **cannot** reconcile them by
  construction. That is *unindexable*, not *uncovered*, and the distinction is preserved.
- **Stale index, unchanged:** `industry_US/PREFLIGHT_US.md` in `REPORT/` still reads **2026-08-20** in
  the ledger, i.e. the 08-21 copy-to-`REPORT/` step did not refresh it. **Minor, logged**, and this run
  must not repeat it (§ run-end handoff).

---

## §6 · The signal scoreboard — a pre-registered threshold has been crossed, and `W1` blocks it

`axis_inflection.py` → `ic_ledger.py log` → `ic_ledger.py score`, all three run. **0 new rows accrued**
(729 rows, `market=kr`) — nothing newly resolved since the last run.

The standing item, carried every run, read: *"`vol_surge` is the only axis with a consistent sign
across two horizons (h=1 **−2.08** · h=5 −1.91) … **do not flip the gate until it clears Bonferroni**
(P4)."*

**It has cleared.**

| Axis | h | n | `n_eff` | mean IC | **t(NW)** | positive | verdict |
|---|---|---|---|---|---|---|---|
| **`vol_surge`** | **1** | 34 | **34.0** | **−0.0454** | **−3.86** | 24% | ★ **significant, passes Bonferroni** |
| **`vol_surge`** | **5** | 27 | **5.4** | **−0.0555** | **−3.38** | 18% | ★ **significant, passes Bonferroni** |
| `obv_norm` | 5 | 27 | 5.4 | −0.0704 | −2.08 | 22% | significant on a standalone bar only |

Both `vol_surge` cells clear **|t| > 2.8** with **`n_eff` ≥ 4**, same sign, two horizons. **The
condition this desk wrote down in advance is met.**

🚫 **And this run may not act on it.** The ledger is **`market=kr`** (729 rows, KR universe).
Importing a KR-measured axis IC into the US sweep is **exactly the `W1` violation this repo keeps
logging**, and it is the same reasoning the protocol used on 2026-07-31 to refuse importing KR's DEEP
budget cut into the US desk. **The threshold cleared in KR. The US desk has no equivalent measurement
and therefore no verdict.**

⇒ **Dig registered (`D310`, §9): the US desk needs its own IC accrual, or this pre-commitment can never
be honoured on the side that would act on it.** A pre-registration that is unreachable in the market
that owns the decision is a pre-registration in name only.

★ **What IS legitimately carried, with the `W1` caveat on its face.** `vol_surge ≥ 1.2` is one of the
three axes in today's 🟢 gate, and with velocity null it is the axis that blocks almost everything —
**`CBRE` failed its ledger leg on that axis alone today, and `NUE` fails 🟢 despite surge 1.41.**
If the KR-measured negative IC generalises, the gate is selecting **against** forward returns. **That
is a hypothesis to test on US data, not a finding to apply** — and every stage citing a 🟢 today should
carry the sentence *"selected partly on `vol_surge`, an axis measured negative in the KR ledger."**

---

## §7 · 🚨 `R93` — the retraction this run files against its own predecessor

**The claim.** The 2026-08-21 `industry_US` run wrote, in its MACRO headline, its asof chain, and the
registration text of `S108`: **"Kevin Warsh's Jackson Hole debut is TODAY, 2026-08-21"** — and drew from
it the conclusion **"`D18`/`D288-KR`'s most expensive instance yet: `catalyst_calendar` missed a
Fed-chair speech at D-0."** It then **overwrote its own HANDOVER §6 sentence, "No binary lands ≤48h
from this run,"** describing that as a self-correction.

**What killed it — measured today, `--scope foreign`.**

| Source | Date | Text |
|---|---|---|
| `economictimes` (body) | **2026-08-22** | *"the **August 27 to August 29 event** in Jackson Hole"* — **the explicit dates** |
| `fxstreet` (body, 14:43 GMT) | 2026-08-21 | *"**Forecasting the upcoming week**: Warsh's Jackson Hole debut and US inflation test a soft US Dollar"*; body in future tense throughout — *"Warsh's Jackson Hole speech **will** focus on…"* |
| `wsj` | 2026-08-21 | *"**Week Ahead** for FX, Bonds: Warsh Speech at Jackson Hole, U.S. PCE Data in Focus"* |
| `KITCO` via `google_en` | 2026-08-21 | *"Gold looks to PCE inflation, Jackson Hole for direction **next week**"* |
| `seekingalpha` | 2026-08-21 | *"**Catalyst Watch**: Nvidia blockbuster, Warsh at Jackson Hole…"* |
| `reuters`/`investing_en` + `economictimes` | 08-21 / 08-22 | *"Nvidia earnings, Jackson Hole to test pillars of stock rally"* — a Week-Ahead piece |

**⇒ Three consequences, and the second is the one worth carrying.**

1. **The date was wrong by six days.** The `fxstreet` piece is time-stamped **10:43 ET on 08-21** and
   is written entirely in advance of the speech.
2. ★★★ **The conclusion drawn from it was wrong in the opposite direction from the desk's usual error.**
   `catalyst_calendar` did **not** miss a D-0 binary — **there was no D-0 binary.** The calendar was
   right and the run overrode it on a "Week Ahead" headline. **The desk has spent runs building
   machinery to catch "the calendar missed a dated event"; that machinery, applied under time pressure,
   manufactured an event that did not exist.** This failure mode — a **news-based override of the
   calendar being wrong in the FALSE-POSITIVE direction** — has never been logged in this ledger.
   The original HANDOVER sentence it replaced was **true**.
3. **`S108`'s stated rationale is void, and the row still settles as registered (`D242` — no
   re-freezing).** Its window is **08-20 close → 08-25 close**; Jackson Hole is **08-27 → 08-29**.
   **The row measures nothing about the event it was built for.** ⚠ Note precisely where its own
   base-rate check went: it verified that the **anti-signal** was outside the window (*"July PCE on
   08-28 — OUTSIDE the window"*) with real care — and **never applied the same test to the event.**
   ⇒ Rule candidate for PREMORTEM (§9): **check that the EVENT is inside the window with the rigour
   already spent on the anti-signal.**

**What survives, and it matters:** **`D18` is still real.** `catalyst_calendar --days 10`, run today,
carries **zero rows for Jackson Hole 08-27–08-29** while listing July PCE 08-28, `NVDA` 08-26, `FRO`
08-28 and the MSCI review 08-31. **The gap is genuine; yesterday's dating of it was not.**

★ **And the live consequence for THIS run: three binaries land inside seven days** — **`NVDA` 08-26**,
**Jackson Hole / Warsh's debut 08-27→08-29** (calendar-invisible), **July PCE 08-28**. `bloomberg`
08-21 carries a named market view that ranks them: *"Allspring's Miletti Sees Jackson Hole as **Bigger
Risk Than Nvidia**."* **PREMORTEM must bracket the Jackson Hole event on its true dates**, and that is
handed forward as a requirement, not a suggestion.

---

## §8 · `C11` RESOLVED — and only a closed market could have resolved it

**The carried contradiction (spine §6, since 2026-08-19).** The sweep's `obv_state` and
`module_chart --read`'s "20d 기울기" flip sign on 5–6 of 22 names. DEEP-MATR called it a **clock
artifact** (`module_chart` pulls live data; those readings were taken after the 22:30 KST bell).
DEEP-INDU and PREMORTEM Lens 3 disagreed. **Unmeasured: clock or method.** Standing constraint: no
name-level claim on OBV alone, and every citation must name instrument and clock.

**Today's test, available for the first time.** US cash is **closed all day**. Both instruments
therefore read **the same settled 2026-08-21 bar with zero clock difference.** Under the clock
hypothesis they had to agree.

| Ticker | sweep `obv_state` / `obv_norm` | `module_chart --read` | agree? |
|---|---|---|---|
| `ANET` | 매집 **+0.152** | 분배 **−27%** | ❌ |
| `NUE` | 매집 **+0.148** | 분배 **−71%** | ❌ |
| `RTX` | 중립 **+0.023** | 분배 **−71%** | ❌ |
| `PYPL` | 매집 **+0.138** | 분배 **−50%** | ❌ |
| `CRWD` | 중립 **−0.058** | 누적 **+35%** | ❌ (inverts the other way) |

**5 of 5 still disagree with the clock difference removed. The clock hypothesis is refuted.**

**And reading both sources shows they were never measuring one quantity:**

| | sweep — `module_flow/_price_flow.py:28-32` | chart — `module_chart/_metadata.py:125-131` |
|---|---|---|
| OBV series | **cumulative from frame start** (`.cumsum()`) | **20-day ROLLING sum** (`.rolling(20).sum()`) |
| Change | `obv[-1] − obv[-21]` — 20-session change **of a cumulative series** | `obv[-1] − obv[-10]` — 10-session change **of a rolling-20 series** |
| Denominator | `vol20` (20-day mean volume) | `max(abs(obv[-20:]))` — the rolling series' own range |
| Threshold | ±0.08 | ±0.15 |

⇒ **The sweep asks *"did signed volume accumulate over 20 sessions?"* — a LEVEL. `module_chart` asks
*"is the 20-day accumulation window rising or falling over the last 10?"* — a RATE OF CHANGE. The
chart's quantity is approximately the derivative of the sweep's.** A name accumulating over 20 sessions
whose rolling window has been shrinking for 10 reads **매집 on one and 분배 on the other, correctly, at
the same instant.** That is 4 of the 5 names; `CRWD` is the mirror case (decumulating but decelerating).

★ **`C11` therefore resolves as METHOD — and further, as NOT A CONTRADICTION AT ALL once the
definitions are read.** ⚠ **DEEP-MATR's reconstruction is not overturned**: it rebuilt OBV from settled
bars using the *sweep's* definition and agreed with the sweep 12 of 12, which is exactly what should
happen. Its **interpretation** — that the `NUE` flip was a clock artifact — is what today's measurement
refutes.

**⇒ The standing constraint is REPLACED, not lifted:**
- ✅ **Lifted**: the requirement to name the *clock* alongside every OBV citation. Both instruments
  read the frame they are given.
- 🚫 **Kept and sharpened**: every OBV citation must name **which instrument** and **which quantity** —
  *"sweep `obv_norm`, 20-session level"* or *"`module_chart`, 10-session slope of the rolling-20"*.
  **Calling both "OBV" is what created a phantom contradiction that survived three runs.**
- ⚠ **`D6` (OBV is a grade-C signal) is untouched.** Nothing here promotes it.

★★ And the finding rhymes with the desk's own regime call (§1): **a level and its second derivative
pointing opposite ways is not a contradiction — it is the shape of a decelerating cycle.** The desk
wrote that sentence about memory prices in July and then spent three runs failing to apply it to its
own instrumentation.

---

## §9 · Stale flags, digs registered, and the dig list ranked for today

### Suspensions whose clearing date has passed ⇒ converted to dig instructions
- **`C11`** — cleared and resolved today (§8). **Moved out of §6.**
- **`S102`** — its settle is structurally unreachable by a weekend desk; **handed to the 08-24 run.**
- **`APH`** — second HANDOVER past due; **hard obligation on ALPHA today** (§3).
- **`D295`** — `S103`'s `NVDA` bands hand-set for a **third** run, with the print **four days out**.
- **`SECTOR_DEEP_SEMI.md`** — 38 days old, covering where 4 of 11 book names live (§5).

### Digs registered by this run
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md`, `llm_outputs/`, `REPORT/`: `D307` `D308` `D309`
> `D310` `D311` returned **0 hits**. Highest existing **`D306`** (US) / **`D308-KR`** (KR) — numbers
> taken beyond **both** series so suffixed and unsuffixed cannot collide (the `D76` class).

| ID | Dig | Evidence (measured this run) |
|---|---|---|
| **`D307`** | ⚠ **The same provider returns different settled closes for the same session hours apart, and nothing flags it.** | `BZ=F` **2026-08-21** settle: **93.870** (sibling desk, ~09:3x KST) vs **94.390** (this desk, 22:2x KST) — **0.52 / 0.55% apart**, same ticker, same provider, same settled session, on a day with no trading between the pulls. **Both sit above `S95`/`P69`'s 93.00 bar so no verdict moved — this time.** **Positive-form remedy: a settled-price citation used to score a bracket should record the pull timestamp beside the value**, so a later run can tell a revision from a disagreement. `D5` class, first instance on a continuous futures contract |
| **`D308`** | 🚨 **A node-vs-name bracket written on a RAW excess forces its anti-signal to arbitrate something the anti-signal cannot see.** | `S90`'s clause (*"`DLR`-specific acquisition or guidance event ⇒ name event, not node read"*) had to be adjudicated by hand today because a **424B7 resale registration** landed inside the window while the price move was **provably a node move**: `DLR` −3.393 with `EQIX` −1.963 and `IRM` −4.357, against `XLRE` +0.948 / `AMT` +1.493 / `PLD` +1.914 / `WELL` +2.939. **Positive-form remedy: write the observable as the name's excess vs its OWN sub-node peer basket**, so a shared move cancels and only idiosyncratic moves reach the branches — then the anti-signal has nothing left to arbitrate |
| **`D309`** | 🚨 **A bracket on a FRED daily series cannot settle on a market close; it settles on a publication.** | **`S102` has now slipped two consecutive runs** for the same reason: its observable is *"`[FRED]`, the first close covering 2026-08-21"*, FRED's `DGS2`/`DGS10`/`DGS30` end at **2026-08-20** on **three independent pulls** across 14 hours, and **FRED does not publish on weekends** — so a Saturday desk can never score a Friday-dated FRED row. **Positive-form remedy: date a FRED-observable bracket to the first BUSINESS DAY after the release** and state the release lag at registration, the way `D93` already requires a baseline beside a threshold |
| **`D310`** | 🚨 **A pre-registered kill-threshold has been met in the market that cannot act on it, and unmet in the market that can.** | `vol_surge` cleared its written Bonferroni condition today — **h=1 t(NW) −3.86 (`n_eff` 34.0), h=5 −3.38 (`n_eff` 5.4)** — in an `ic_ledger` that is **`market=kr`, 729 rows**. `W1` forbids the US desk from importing it, and **the US desk has no IC accrual of its own**, so the US 🟢 gate keeps weighting `vol_surge` **positively** with no measurement either way. **Positive-form remedy: accrue `ic_ledger` on the US universe** — the axis files already exist; what is missing is a US `axis_inflection` run in the pipeline |
| **`D311`** | 🚨 **A news-based override of the calendar can be a FALSE POSITIVE, and nothing in the harness checks that direction.** | The 08-21 run read a **Week-Ahead headline** as a D-0 event, declared *"the calendar missed a Fed-chair speech at D-0"*, and **overwrote a HANDOVER sentence that was correct** (§7 / `R93`). Every guard this desk owns points the other way — at events the calendar *omits*. **Positive-form remedy: when a news item is promoted to a dated catalyst, require an explicit DATE STRING from a body, not a headline** (today's resolution came from a body: *"the August 27 to August 29 event"*), and record the sentence it came from beside the date |

### Method observations (rule candidates — not promoted to triggers)
- ★ **Check that the EVENT is inside the bracket's window with the rigour spent on the anti-signal.**
  `S108` base-rate-checked its anti-signal carefully and never checked its own event's date (§7).
- ★ **Two VOIDs in one batch from one cause is a design fact, not bad luck** (`S91`, `S93`; `S98` on
  08-21). **An 8-day US window contains an FOMC/CPI/PPI communication almost surely, and a
  consumer-tariff headline nearly as often.** `D300-KR`'s base-rate check must be applied to *every*
  new anti-signal, and PREMORTEM should prefer clauses keyed to **magnitude** (`S89`'s ±8% gold band —
  which behaved correctly today) over clauses keyed to **an event occurring**.
- ★ **A zero-coverage instrument can be cleaner than a partial-coverage one.** Today's tag layer is
  citable precisely because the news pipe failed completely rather than partially (§0). **Uniform
  missingness is a scale; selective missingness is a bias.**
- ★ **A weekend run is not a degraded weekday run — it is a different instrument.** It cannot score
  FRED rows (`D309`) and has no fresh session; but it is the **only** configuration that can separate
  clock effects from method effects (`C11`, §8) and the only one with no partial-bar risk at all.

### The dig list ranked for today (candidate DEEP assignments)
1. **`SECTOR_DEEP_SEMI` at 38 days** with 4 of 11 book names inside it (§5) — reconciliation-driven.
2. **The Jackson Hole bracket on its true dates** (§7) — PREMORTEM obligation, not optional.
3. **`M704`'s defense EW re-run ex-`LHX`** — `S97` FIRED-A made this due (§1).
4. **`D295` / `S103`'s `NVDA` bands** — third run, print in four days (§2e).
5. **The refiner CONTRACT question** (`module_disclosure_us MPC` → 10-Q MD&A + Item 1A) — carried
   unopened from 08-21; `P70`'s MISS today makes the margin-sustainability leg more, not less, urgent.

---

## §10 · What this run asserted and then refuted — written down, not edited away (`§4c`, `D48`)

**One self-refutation, and it was caught by a ledger row rather than by review.**

This run's own PREFLIGHT first wrote *"`breadth`, `green`, `red`, and 'new 🟢' may not be cited at
all"* — a blanket revocation, justified by a real measurement (9 greens vs 6 on one price frame).
**It was too broad.** The `CBRE` miss-ledger row, whose condition asks for *"the green set on an
admissible (non-velocity) axis"*, forced a source read that showed the tag collapses to a pure price
function when `vel` is `None` — which is the case for **all 299** names in the persisted file. **The
rule was narrowed to partial-coverage runs, the original wording was kept beside the correction, and
the rights tables were re-propagated.**

★ **The general lesson is the useful part: the audit step found the error in the gate step.** The two
are meant to be independent, and today the dependency ran in the productive direction.

⚠ **Zero self-refutations would not have been a good sign.** Per the standing note, a run that reports
none usually means its controls were not adversarial.

---

## §11 · RESEARCH triggers loaded as binding constraints — which group binds which stage

| Group | Fires when | IDs | Binds, this run specifically |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO + every stage.** ⚠ **`C4` is live in §4** — n=11 on the exposure decomposition forbids a selection-edge claim **in either direction**. ⚠ **`C5` is live in §2/G4** — the risk-unit `dist 0.65` threshold does the work, and 250d/500d both print 11 with different membership |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **§6 above.** `n_eff` and Bonferroni are applied; `vol_surge` is the only axis quoted, and it is quoted **as a KR result** |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · **D5 cross-provider** · D6 signal grade (OBV is C) | **SWEEP · ALPHA · DEEP.** ⚠ **`D5` fired today** (`D307`, `BZ=F`). ⚠ **`D6` binds §8** — resolving `C11` does **not** promote OBV |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION.** 🚨 **`W1` is the binding constraint of §6** — it is what stops this run acting on a cleared threshold. **`W5` fired twice**: `WMT`/`TGT` at **17.1pp** intra-sector on one window, and `DLR`/`EQIX`/`IRM` vs `AMT`/`PLD`/`WELL` at **~6pp** inside `XLRE` (§2). **`W4`: `RTX`'s customer is unmeasured for 205 days** |
| **L** | lenses, not triggers | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM.** ★ **`L1` is the key to §8.** **`L3` binds §2**: `S88`'s C was the disclosed heavy favourite and the row bought little — PREMORTEM should not register another 100th-percentile-state row whose only informative branch needs a 15pp reversal |

---

## ✅ EXIT CHECK

- [x] Spine `STANDING_VIEW.md` + `SCENARIOS.md` **in full**, plus `STANDING_VIEW_US.md`,
      `SCENARIOS_US.md`, `RESEARCH.md` read. **`SCENARIOS_KR.md` and the KR HANDOVER opened** — the
      other market's file held rows this run had to verify, and one row (`009830`) it had to hand back.
- [x] **Retracted ledger read BEFORE forming today's view** (through `R92`). Six binding entries listed;
      one (`R80`/`R84`) explicitly re-opened **with a new experiment and a statement of what is and is
      not being overturned**, not laundered.
- [x] **Every past-dated scenario scored or explicitly dispositioned**: 3 scored + 2 VOIDed by this
      desk · 9 verified as scored by the sibling desk · 4 P-rows settled · **1 not-yet-arrived with a
      structural reason, a registered dig and a named successor run**. **`EXPIRED` 0 · silent skips 0.**
      `S8` named for the **20th** run.
- [x] **`reject_ledger.py due` run** — **0 due, 0 legacy** (cleanest in the series; the legacy count has
      now held at 0 for **11** runs, so this is a trend, not a quiet pass).
- [x] **`missed_ledger.py due` run** — 4 due → **2 resolved** (`VLO` entered, `CBRE` reaffirmed),
      **2 carried with named reasons and one hard obligation** (`APH` → ALPHA today; `009830` → KR).
      Sign inversion respected; the two ledgers are never summed.
- [x] **Exposure state read and carried** (§4) — verdict **정상**, target **95%**, current **blank in
      `state`**, ledger band gap **−9.9pp (live bar)**, cumulative **−16.64pp = cash −6.46 + selection
      −10.19 on n=11**. Not a cold start (38 rows). `밴드미설정`/`투자비중미상` reported as 🚨 with **no
      number substituted**.
- [x] 🚨 **Instrument health inherited before any number was trusted** (§0) — `PREFLIGHT_US.md` run,
      **PASS 3 / FAIL 5**, rights table binding, **plus one in-run correction to it** (§10).
- [x] **Self-refutation written down, not edited away** (§10) — one, caught by the ledger audit.
- [x] **Stale rows flagged with dates; every cleared suspension converted into a dig** (§9) — and one
      carried contradiction (`C11`) **measured to resolution** rather than carried a fourth run.
- [x] `[measured]` / `[inferred]` tags preserved. The regime call is carried **`[inferred]`** and is not
      cited as evidence anywhere in this packet.
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L**, with the stage each binds
      **and the specific rule that fired this run** named (§11) — not summarized.
- [x] `HANDOVER.md` written. `handoff/*.md` updated **at run end** (append-only for `R93` and
      `D307`–`D311`), per the protocol.
- [x] **No position sizing, no buy/sell language anywhere** (P4).
