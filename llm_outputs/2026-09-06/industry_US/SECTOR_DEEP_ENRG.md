# SECTOR_DEEP_ENRG — industry_US · 2026-09-06 (Sun) · Stage 8 / L1·DEEP · **CONTINUOUS TRACK**

> Continuous slot, held for a 3rd consecutive run (ROTATION anti-thrash). **Leads with the DELTA.**
> Structure carried by reference to `llm_outputs/2026-09-05/industry_US/SECTOR_DEEP_ENRG.md` — the
> 16-name roster, the chain map and the node definitions are unchanged and are NOT re-printed.
> **P4 — no sizing, no buy/sell language.**

## §0 · ⚠⚠ The delta this run is entirely non-price, and one of its findings REFUTES this run's own MACRO stage

**The price frame has no new session** (`asof 2026-09-04`; Labor Day 09-07; next settled close
**09-08**). Every flow, OBV, RS and short number below is Friday's and reproduces the 09-05 file's.
⇒ **there is no tape delta to lead with.** The delta is four things, all from outside the tape:

| # | delta | source |
|---|---|---|
| 1 | ★★★ **A two-way military escalation around Iranian oil-export infrastructure**, 09-05/06 | 46 articles, 16 outlets |
| 2 | ★★★ **A 65bn-barrel Venezuela supply deal, structure and TIMELINE now read from a body** | `fts --full`, 9,736-char body |
| 3 | ★★ **The distillate crack's 3-session rate is at the 6.0th percentile while its level is at the 95.6th** | own computation |
| 4 | ★ **`SLB` earned a 🟢 with NO news leg available** — the sector's cleanest signal | sweep + `us_live_shortlist` |

★★★ **And §2 below is a REFUTATION of the mechanism this run's own MACRO stage asserted three stages
ago.** It is written down rather than edited away (`§4c` / `D48`).

---

## §1 · The instrument finding that made §2 possible — and it is a `§4b` capability, not a data gap

At MACRO this run I registered **`D535`**: *"the 13-outlet Venezuela 'blindsided' story is title-only
across every outlet that carried it; the desk has the SUBJECT and not the MECHANISM."*

🚨 **`D535` is partly WRONG and this stage refuted it inside the same run.**

- The two Bloomberg items and the Japan Times item genuinely return `[no body]` / `[error]` — that
  part stands (blocked scraper, `D10` class).
- **But the same cluster contains `yahoo_finance`'s *"Gulf Coast Refineries Pour Cold Water on
  Trump's 65-Billion-Barrel Venezuelan Victory Lap"* (2026-09-01) with `body = 9,736 characters
  STORED IN THE DATABASE**, and `fts search` carries a **`--full`** flag that prints it.
- **`--full` is documented in `pipeline/L3_functions/drill_detail.md` and `pipeline/L2_modules/news.md`
  — the exact L3 that DEEP and EVENT_ALPHA are told to call for the direction body-read — and it was
  invoked ZERO times across the last six `industry_US` runs' outputs.** `--snippet` likewise.

⇒ **`D541`** [registered here]: *`fts search --full` / `--snippet` print stored article bodies and
have never been invoked by this desk. Every prior "body unreadable" finding must be re-read as
"no print path was tried," because `search` was already REPORTING the body length (`body=9736자`)
in the same output line that the desk read as evidence of absence.* ★ This is `handoff/README §4b`
exactly — *a capability nothing invokes is a capability that does not exist* — and the cost is
measurable: it produced a wrong dig (`D535`) in this run and contributed to `M1288`'s framing.

---

## §2 · ★★★ The Venezuela mechanism, read from the body — and it INVERTS the sign this desk assumed

**What `P139`'s registration asserted (MACRO §D, this run):** *"Venezuelan crude is heavy sour — the
design feed of the US Gulf Coast complex. A structural rise in heavy-sour supply is bearish the
barrel and bullish the heavy–light differential, i.e. bullish the refining margin."*

**What the body says** [yahoo_finance, 2026-09-01, 9,736 chars, read via `--full`]:

| # | fact | why it matters |
|---|---|---|
| 1 | **100-year concessions on 17 fields**, ~65bn barrels of proven reserves, into a JV with **North American Blue Energy Partners (NABEP)**, Venezuela's second-largest private producer. **The Pentagon's Office of Strategic Capital takes a 35% equity stake in NABEP's parent.** US gets **20% of production at cost** + right of first refusal on the other 80%. NABEP plans **up to $100bn of infrastructure** and **$200bn of royalties/taxes over 25 years** | The structure is **capex**, not barrels. **A defense-department equity stake in an oil JV is a structure this desk has no precedent for** and it is not a commercial contract |
| 2 | 🚨 **Venezuela produces ~1% of global output** despite the world's largest reserves. **Rystad: full production from EXISTING fields may not arrive until the mid-2030s.** CFR: **$10–20bn** to repair infrastructure; new fields **>a decade and ≥$100bn** | ★★★ **The supply is a DECADE out.** *"Reserves are oil in the ground. Production is oil coming out of a pipe."* |
| 3 | ★★★ **The binding constraint is REFINING, not crude.** Venezuelan crude is extra-heavy, high-sulfur, requiring **high-complexity coking refineries**. The Gulf Coast has the world's best — **and they are already busy.** **`VLO` told analysts on 2026-07-30: *"we've been the largest U.S. consumer of Venezuelan crude over the last several years"* and expects processing rates to EXCEED its historical maximum** | ⇒ **My stated mechanism is INVERTED.** More heavy crude does **not** widen the incumbent's margin through cheaper feed when the incumbent is **already running above its historical max** — it means the **scarce asset is the coker, not the barrel** |
| 4 | `VLO` management also flagged **~5 million b/d of global refining capacity OFFLINE** and **light-product inventories ~130 million barrels below normal seasonal levels** | ★★ **This is the actual bull case for the refining node, and it is a CAPACITY-scarcity case, not a feed-cost case** |
| 5 | **`CVX` is negotiating Venezuelan fiscal terms targeting debt recovery by 2027**; **`VLO` already leads US refiners in processing Venezuelan heavy crude**; `XLE` **+45% YTD** on the crude-and-product price shock | Names the two chain positions with actual exposure — and **`VLO` is the one refiner the book does NOT hold** |

### §2a · ⚠⚠ What this does and does NOT do to `P139` (`D242`)

- 🚫 **The observable and both branch lines are FROZEN and are NOT touched.** `EW{XOM,CVX,SLB}` −
  `EW{MPC,PSX,VLO}`, 5 sessions, 09-04 → 09-14, **A ≥ +2.719 · B ≤ −4.689**, state −3.260.
- ✅ **What changes is my stated grading of which branch is informative, and I am correcting it
  publicly rather than at scoring.** At registration I wrote *"B is the near branch and A is the far
  one; an A print is the informative one."* **The body says the upstream leg's barrels are mid-2030s
  and its near-term content is capex.** ⇒ **A is now not merely far, it is mechanically unlikely
  inside a 5-session window**, which **lowers the row's information content below what I claimed.**
  ⚠ It is still a legitimate row — a C print now *confirms* the timeline reading rather than being
  uninformative — but **the registration overstated its power and this line is the correction.**
- ★ **The chain-position specification of the Energy OW survives and is strengthened, on a different
  mechanism than the one the desk was carrying.** `M1245`/`M1246` said the OW is a *chain-position*
  bet, not a barrel bet. The body supplies a **capacity** reason for that (5 mb/d offline, product
  inventories 130 mb below normal) where this desk had been carrying a **spread** reason.

---

## §3 · Commodity-node rate-of-change series — the level and the rate point opposite ways

**Required by lens `L1`: price-cycle nodes are read on the second derivative.** Quarterly means,
`$/bbl`, computed this run from settled `CL=F`/`RB=F`/`HO=F`:

| quarter | distillate crack | **QoQ rate** | 3-2-1 blended | **QoQ rate** | WTI | **QoQ rate** |
|---|--:|--:|--:|--:|--:|--:|
| 2025Q3 | 33.63 | +24.7% | 26.45 | +3.6% | 64.99 | +2.1% |
| 2025Q4 | 38.21 | +13.6% | 25.30 | −4.3% | 59.14 | −9.0% |
| 2026Q1 | 51.16 | +33.9% | 32.06 | +26.7% | 72.67 | +22.9% |
| 2026Q2 | 64.47 | +26.0% | 50.96 | **+58.9%** | 92.70 | +27.6% |
| **2026Q3 QTD** | **90.59** | ★ **+40.5%** | 65.40 | +28.3% | 81.67 | ⚠ **−11.9%** |

⚠ **2026Q3 is QUARTER-TO-DATE (through 2026-09-04), not a complete quarter** — stated rather than
compared as a full period.

**`B1` kill-signal check, executed rather than asserted:** the signal is **two consecutive declines in
the RATE**. Distillate: `+13.6 → +33.9 → +26.0 → +40.5` — **one decline, then a rise. Not fired.**
Blended: `−4.3 → +26.7 → +58.9 → +28.3` — **one decline. Not fired.** `M1311` reproduces exactly.

★★ **But the daily series says something the quarterly series cannot**, and it is this run's new
number: the distillate crack **peaked at 106.23 on 09-01 and printed three consecutive lower closes**
to **99.21**, a **3-session change of −$7.02/bbl = the 6.0th percentile of trailing 252**, while the
**level stays at the 95.6th**. ⇒ **`P140`** (settles 09-11) is written on exactly that split.
⚠ **These are two different objects and are not conflated**: the quarterly rate is the B1 instrument;
the 3-session rate is a within-quarter shape. **Neither contradicts the other.**

### §3a · 🚨 Contract-terms check — executed, and the answer differs from the memory precedent

The EXIT CHECK requires that any *"the margin must mean-revert"* claim name the contract terms it
checked, from the filing. **This stage does not make that claim** — but it ran the check anyway,
because the check is what tells you whether the rate series is a demand signal or an arithmetic cap:

- **Refined products sell at SPOT / index-linked pricing.** There is **no floor/ceiling band** on the
  crack analogous to `MU`'s take-or-pay ceiling pinned to a dated market price.
- ⇒ **The distillate crack's deceleration is NOT arithmetic hitting a cap.** It is a price series
  moving. **This is the opposite of the memory case** (`M1311`'s own contractual-band check,
  reproduced here rather than inherited).
- ⚠ **The contracted share of the refiners' own throughput remains `unknown` (`C3`)** — no 10-Q
  Item-2 read was performed on `MPC`/`PSX`/`VLO` this run, and it is **the third consecutive run**
  that gap has been carried (`D514`). **Named, not papered over.**

### §3b · ★ Frame-transfer question — asked and answered

**The frame this desk trusts elsewhere:** take-or-pay / RPO lock-in (`KMI` $35.67B RPO, `LNG`
tolling, `VST` 20-year PPA floors — 21 files apply it, all listed as *"things the Fed can't reach"*).

**Does it apply to the refining node?** ⚠ **No, and the reason is the finding.** Refining margin is a
**spread between two spot series** with no contracted floor; the node's protection is **physical
capacity scarcity** (5 mb/d offline, coking complexity), not contractual. ⇒ **a refiner's margin has
no floor a filing can promise**, which is precisely why `P140`'s rate-of-change question is the right
one and why an `L2` peak-margin read on `MPC`/`PSX` cannot be dismissed by a contract argument the
way `MU`'s could. **Checked, does not apply** — which the stage's own rule counts as a pass.

---

## §4 · Node map, with the DELTA marked (structure by reference to the 09-05 file)

Chain, left → right: **reserves/concession → upstream production → oilfield services → transport
/ storage → REFINING (the bottleneck) → product distribution → end demand.**

| node | names (flow · OBV · rs20 · rs60) | delta this run |
|---|---|---|
| **Concession / upstream** | `XOM` 🚨 **+0.03 · −0.07 중립 · +4.6 · −0.3** (last of 16) · `CVX` **+0.66 · +0.37 매집 · +12.2 · +3.7** · `COP` +0.64 · +0.22 매집 · +14.6 · +5.8 · `EOG`/`DVN`/`OXY`/`FANG` +0.43→+0.64 | ★ **Venezuela-named: `XOM`, `CVX`.** The body puts their barrels **mid-2030s** and their near-term content at **capex** ⇒ the node's Venezuela exposure is **an option, not a cash flow** |
| **Oilfield services** | ★ **`SLB` +0.88 (sector #1) · +0.44 매집 · +14.2 · rs60 −2.6** · `BKR` +0.31 · +0.13 · +3.6 · −5.4 | ★★★ **`SLB` is the delta.** Venezuela-named; **positive rs20 on a NEGATIVE rs60 = a NEW catalyst, not a trend**; earned its 🟢 at universe position **173 with `velocity = None`**, i.e. **no news leg was available to it** — the one green on the board that cannot be a `D537` artifact; `[FINRA]` z **−1.21** ⇒ **✅ 저숏/숏커버 clean rise**; chart **CONFIRMED-TURN, OBV +87% 20d slope, no divergence, ignition trigger `close > 57.94` UNFIRED**. ⚠ `SLB`+`BKR` are **0.575 flow points apart on n=2** ⇒ **"services" is not a node at that dispersion** (`W5`) |
| **Transport / storage** | `WMB` **+0.77 · +0.15 매집 · +5.7 · −3.6 · Δ +0.35 (sector's largest)** · `OKE` +0.69 · `TRGP` +0.44 · `KMI` +0.17 | Unchanged. `WMB` is 🟢 with `velocity = None` (position 129) ⇒ also artifact-free |
| ★ **REFINING — the bottleneck, and the body confirms it** | `PSX` **+0.75 · +0.43 매집 · +25.5 · +34.2** (held) · `VLO` **+0.70 · +0.48 매집 · +24.7 · +37.5** (not held, standing rejection) · `MPC` **+0.69 · +0.62 매집 · +30.8 · +41.5** (held) | ★★ **The bottleneck is now attested by the node's own operator, not inferred**: `VLO` on 2026-07-30 — *"largest U.S. consumer of Venezuelan crude,"* processing rates expected to **exceed historical maximum**, **~5 mb/d global capacity offline**, **light-product inventories ~130 mb below normal seasonal.** ★★ **A bottleneck is a *binding constraint*, and this is the first run where the desk has the operator's own words for it rather than a spread reading** |
| **End demand** | not in `us_top300` as a node | ⚠ Demand-side proxy: **US diesel at an all-time high**, and *"Americans hit with record-high Labor Day Weekend gasoline prices"* [reuters, 09-05] — **a two-sided fact**: bullish crack, and a **political** input to the SPR/Venezuela push |

### §4a · Chain-hop — and it WORKED this run, after returning zero on 09-05

`chain-hop "Venezuela" --days 7 --scope foreign`:

| candidate | title hits | body proximity | industry | verdict |
|---|--:|--:|---|---|
| ★ **`COP`** | **0** | **23 proximity / 24 body** | Oil & Gas E&P | ✅ **VALID body-proximate candidate.** Never headline-named; example article *"Chevron and Halliburton Near Billion-Dollar Venezuela Oil Deals."* **Flow cross-check: +0.64, OBV +0.222 매집, rs20 +14.6, rs60 +5.8** ⇒ accumulating, but **RS has already partly moved** (+14.6 against the node's +25 to +31), so it is **not** the clean "OBV up, RS not yet" alpha shape the rule describes. **Logged as a candidate, NOT handed to BET** |
| `MPC` · `VLO` | 0 | 5/5 · 3/5 | Refining | Already held / already carried — not new |
| `META`·`MSFT`·`AMD`·`EBAY`·`WFC`·`HWM`·`STT`·`PCG` | 0 | 2–7 | — | 🚫 **`D509` artifacts** (three-letter/co-occurrence collisions; the `HWM` and `WFC` examples are a *Bitcoin* article). **Named as artifacts rather than filtered silently** |

⇒ **`M1375`**: *`chain-hop` produced its first valid US candidate in three runs, and the difference
was the query — a single high-frequency proper noun (`Venezuela`, 487 hits) rather than a multi-term
theme string (`"Venezuela heavy crude refinery"` returned **0 articles scanned**).* The tool is not
broken; **it is query-shaped**, and the desk has been feeding it theme strings.

---

## §5 · The customers, named, with their disclosed spend

**Required rule A6.** The refining node's customer is end-product demand, which has no filing. **The
node the desk can actually check the buyer of is the Venezuela concession, and its buyer is a
government:**

- **The US government is a 35% equity holder** in NABEP's parent via the **Pentagon's Office of
  Strategic Capital**, and takes **20% of production at cost**. ⇒ **the "customer" is also an owner**,
  which is a structure the desk's take-or-pay frame does not cover.
- **Disclosed spend, from the counterparty's plan**: NABEP **up to $100bn infrastructure**, **$200bn
  royalties/taxes over 25 years**. **Independent cost estimates** (CFR): **$10–20bn** to repair
  existing infrastructure, **≥$100bn** and **>a decade** for new fields.
- ⚠ **No SEC filing from `XOM` or `CVX` was opened this run to confirm either company's committed
  capital.** `CVX`'s **$7bn / double-output-in-five-years** figure is **press-attested across four
  outlets, not filing-attested** ⇒ tagged `[press]`, and **`D516`'s "no filing body opened" gap
  reproduces for a 3rd run.** Named, not concluded around.

---

## §6 · Sub-node dispersion — and the sector label survives, unlike IT's

| measure | value |
|---|---|
| best node mean flow (refining, n=3) | **+0.713** |
| worst node mean flow (integrated, n=2) | **+0.344** |
| **spread** | **0.369** |
| sector `eqflow` | **+0.562** |

⇒ **the sub-node spread (0.369) is SMALLER than the sector's own level (0.562)**, and **1 of 16 names
is negative on `exc5`** with `exc20` median **+11.52** vs mean **+12.29** (median ≈ mean).
★ **So unlike Information Technology — where `M1314` measured a 20.07pp sub-node spread against a
~0.16% sector move, ~75× — the Energy label IS the right unit of analysis**, and this file says so
explicitly because the rule requires the test, not just the caveat.
⚠ **The one genuine intra-sector split is `XOM` (+0.03) against everything else**, and the sector is
**more** positive without it (+0.440 → ex-top1 **+0.621**) ⇒ top-heaviness, not sign-dependence.

---

## §7 · Track-KPIs and anti-signals, as observables

| # | KPI / anti-signal | current | kills what |
|---|---|---|---|
| K1 | Distillate crack **5-session** change | **−0.37** (45.6th pctile) | `P140`-A at **≤ −4.209** ⇒ compression is the regime, not an air pocket |
| K2 | Distillate crack **quarterly rate** | **+40.5% QTD** (accelerating) | **Two consecutive quarterly declines** = the `B1` kill. **Not fired**, 0 of 2 |
| K3 | distillate − gasoline spread | **55.68 = 98.4th pctile** | Falling below the 90th would say the diesel-specific scarcity is normalising |
| K4 | WTI **5-session** change | **+9.688% = 87.7th pctile** | `S149`-B at **≤ −5.734** ⇒ Bessent's $40 framing wins and the OW's driver breaks |
| A1 | ⚠ **Form 144 insider-sale notices at the two HELD refiners** | `MPC` **7/20 = 4.2× base** · `PSX` **6/25 = 2.9×** · `VLO` **0/8** | Carried from `M1312` and **NOT re-measured this run** (no new session). ⚠ Limits attached at origin: a 144 is a *notice*, values `unknown` (`C3`), n=7 and 6 |
| A2 | 🚨 `MPC` short-volume **5v5 trend** | **+8.9, the largest build on the sheet** at an unremarkable z (+0.43) | The building is **recent** and has not moved the level yet |
| A3 | `PSX` chart divergence | 🚨 **BEARISH** (price HH, RSI LH) — **`MPC` has NONE** | ★ **The desk carries `MPC`/`PSX` as one node everywhere; only `PSX` carries the divergence.** PREMORTEM Lens 3 tagged `PSX` **EXHAUSTION-WATCH** and `MPC` **EXTENDED-BUT-LIVE** |
| A4 | Narrative instruments | `distillate` **0.64×** · `refining margin` **0.65×**, 4th consecutive decelerating run | `P136` (09-14) is the row on exactly this divergence |

---

## §8 · ROTATION's flagged divergence — explicit resolution verdict

**ROTATION handed this file one divergence**: *"Energy's flow level is unanimous and its driver
evidence has fractured three ways."*

**Verdict: the three drivers are NOT symmetric, and two of the three point the same way once the
timeline is read.**

1. **Iran escalation** — bullish the barrel, **ambiguous-to-bearish the crack** (input cost up without
   product following is exactly `P140`-A). **Undated, two-sided, and the de-escalation side is larger
   in outlet count.**
2. **Venezuela** — ★ **read from the body, it is NOT a near-term supply event at all.** Barrels are
   **mid-2030s**; near-term content is **capex and a Pentagon equity stake.** ⇒ **it does not threaten
   the barrel inside any window this desk holds**, and its refining leg **strengthens** the
   bottleneck reading (capacity already above historical max).
3. **The crack's level-vs-rate split** — the only one of the three that is **measurable today, on the
   desk's own instrument, inside a dated bracket** (`P140`, 09-11).

⇒ **The fracture is smaller than MACRO §E framed it.** Driver 2 resolves toward the existing
chain-position thesis rather than against it; driver 1 is genuinely two-sided and bracketed
(`S149`); driver 3 is the live question. ⚠ **This is a DEEP verdict on the thesis, not a verdict on
the sector rating — ROTATION issued 0 deltas and this stage does not re-open that** (P4).

---

## ✅ EXIT CHECK — DEEP-ENRG

- [x] **Continuous-track file LED with the delta** (§0); the 09-05 structure is carried **by
      reference** and no roster or chain map is re-printed.
- [x] flow → players (large-cap ∪ chain-hop candidate `COP`) → **IR anchor read from a primary
      body** (`VLO`'s 07-30 analyst remarks, via `fts --full`) → chain map (7 nodes, bottleneck
      marked and **operator-attested**) → chain-hop (1 valid, artifacts named) → KPIs + anti-signals
      as observables (§7).
- [x] **ROTATION's divergence has an explicit resolution verdict** (§8).
- [x] **Commodity node carries a QoQ rate-of-change series** (§3), with the `B1` two-consecutive-
      declines test **executed** (0 of 2 fired) and 2026Q3 declared **QTD, not a full quarter**.
- [x] **No "cheap on forward multiple" claim is made in this file**, so the margin-percentile /
      estimate-revision requirement does not fire. ⚠ Where the desk *does* carry one — `M1313`'s
      five-year-high operating margins on a **pre-spike** quarter — it is referenced, not re-argued.
- [x] 🚨 **The contract-terms check was RUN** (§3a): refined products are **spot/index-priced with no
      floor/ceiling band**, so the rate deceleration is **not** arithmetic hitting a cap — the
      opposite of the `MU` precedent. ⚠ The refiners' own **contracted throughput share is marked
      `unknown` (`C3`)**, 3rd run (`D514`).
- [x] **One frame-transfer question answered** (§3b): take-or-pay / RPO lock-in — **checked, does NOT
      apply**, with the reason (a spread between two spot series has no contractual floor).
- [x] **Customers named and their disclosed spend checked** (§5): the US government via the Pentagon's
      Office of Strategic Capital (35% equity, 20% of production at cost); NABEP's $100bn/$200bn plan;
      CFR's $10–20bn and ≥$100bn independent estimates. ⚠ `CVX`'s $7bn tagged **`[press]`, not
      filing-attested** (`D516`, 3rd run).
- [x] **No lead/lag claim is inherited as fact.** The one lead/lag-shaped statement in this file —
      *"positive rs20 on a negative rs60 is the signature of a new catalyst"* — is a **definition of
      the two windows**, not a lead/lag assertion, and is labelled as such.
- [x] **Sub-node dispersion stated** (§6): spread **0.369** vs sector level **0.562** ⇒ **the sector
      label IS the right unit here**, explicitly contrasted with IT's 75× failure.
- [x] Linter run — result appended below.

---

## 📋 Stage run log — open decisions resolved without a human

1. **Whether the body-read overturns `P139`** — resolved as **no to the thresholds (`D242`), yes to
   the branch grading**, corrected publicly in §2a rather than at scoring.
2. **Whether to re-register `D535`** — resolved as **leave `D535` standing and append `D541` that
   corrects it**, per the append-don't-edit rule. `D535`'s Bloomberg half is still true.
3. **Whether `COP` goes to BET** — resolved as **no**: the chain-hop rule wants OBV accumulating with
   RS *not yet* moved, and `COP`'s rs20 is already +14.6. Logged as a candidate only.
> **Linter** (`report_lint.py`, C1·C2·S6·D6): **0 findings** after fixes. Form check only.
