# BLINDSPOT_PREMORTEM — industry_US · 2026-08-24 (Mon) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **AGAINST this run's own tilt** before the deep budget is committed.
> Draft tilt inherited: `ENRG OW · HLTH OW · MATR N+ · STPL N · COMM N · DISC N · FIN N · RE N− ·
> INDU UW− · UTIL UW− · IT N`; DEEP set `[ENRG, HLTH] + [COMM, STPL]`.

⚠⚠ **Declared deviation, 7th consecutive run**: the four lenses ran **in-context and serially**, not
as a parallel adversarial Agent fan-out. This is a standing session constraint and it is declared,
not hidden. **Cost of the deviation**: the lenses share this run's context and therefore its blind
spots — an independent agent could not have inherited them. Every lens below states what it could
*not* independently check.

## 0 · Binaries in the window — and the calendar carries three of six

`catalyst_calendar --days 10` returns **5 binaries**: July PCE **08-28** · `NVDA` **08-26** ·
`FRO` **08-28** · `AVGO` **09-02** · the **undated** Hormuz row (`S8`, 23rd run undated).

🚨 **Three dated binaries inside the window are ABSENT from the calendar and were recovered from news
bodies instead** (`M872`):

| Missing binary | Date | Source it was recovered from | Run of this miss |
|---|---|---|---|
| **Jackson Hole — Warsh's FIRST speech as Fed Chair** | **08-27 → 08-29** | `thread` one-liner + `theme-age "Jackson Hole"` **14.9×** (board's 2nd-fastest) | **3rd consecutive** |
| **Bessent's sanctions press conference** | **TODAY, 14:00 ET 08-24** | `hellenicshipping` 08-24 body, verbatim: *"Bessent is expected to unveil the new sanctions against Iran during a press conference at 14:00 ET (18:00 GMT) on Monday"* | **1st** |
| **Canada's retaliatory tariffs take effect** | **2026-09-08** | `aljazeera` 08-23 body (named effective date) | **1st** (`D342`) |

⇒ **Two binaries are ≤48h out — `NVDA` (D-2) and the Bessent presser (D0) — and both MUST carry a
both-sides bracket** (a one-way tilt into a known binary is a protocol violation). The presser is
**D0 and fires during this run's own working window.**

## 0-a · 🚨 The instrument that sets magnitude thresholds is broken on the one name that matters most

`module_flow NVDA --positioning` returned: **`예상변동 ±1.3% (만기 2026-08-24, D0) → 안일(연료적음)`**
— i.e. it priced the **expiry that expires TODAY**, two days *before* the print, and rendered the
verdict **"complacent, little fuel."** **`D315`, 5th consecutive run, and this is its worst instance:
the tool did not merely pick a non-spanning expiry, it produced a confident wrong adjective on a
🔀binary held in both books** (`M873`).
⚠ **The same call on `MRVL` picked correctly** (08-28, D4, ±11.2%) — so the defect is *silent and
intermittent*, which is worse than a consistent one.
⇒ **All NVDA-family thresholds below are read from the option chain directly** (LIVE INTRADAY, spot
209.69), reproducing the 08-23 method:

| Name | Prints? | 2026-08-28 ATM straddle | ATM IV (call / put) |
|---|---|---:|---|
| **`NVDA`** | **08-26** | **±6.13%** | 0.692 / 0.617 |
| `MU` | **no** (09-24) | **±6.52%** | **0.770** / 0.639 |
| `SNDK` | **no** | **±8.41%** | **0.926** / 0.884 |
| `WDC` | **no** | **±11.56%** | **0.880** / 0.708 |

★★★ **`S117` is not merely re-confirmed — it is much stronger than when it was registered** (`M874`).
It was written on `MU` IV 0.650 vs `NVDA` 0.606 = **1.07×**. Today, on the identical expiry, **three
memory/storage names with NO print in the window all carry higher ATM IV than the name that actually
prints**, and `SNDK` at 0.926 is **1.34×** `NVDA`. **The options market is pricing NVDA's print as an
event about memory, not about NVDA.**
🚨 **And their tapes say the opposite**: `MU` 🟡중립 −0.278 · `WDC` **🔴분산 −0.781, rs20 −15.2** ·
`SNDK` 🟡 +0.144. **Highest implied volatility on the board, worst realised flow on the board.**

---

## Lens 1 · UNDER-COMPUTED LEGS — what we did NOT deep-dive that has a catalyst ≤5 sessions

| Leg | Catalyst (dated) | Strongest bull case AGAINST our tilt | Verdict |
|---|---|---|---|
| ★★★ **IT / memory-storage sub-node** | **`NVDA` 08-26 (D-2)** · **`MRVL` 08-27 (D-3)** | The tilt holds IT at `N` and gave it no slot. But: `MRVL` reads **🟢가속, news velocity 1.67×, OBV 매집, rs20 +15.5%** on a **LIVE INTRADAY** pull, with short interest **4.8% of float and BUILDING** into a print — squeeze fuel with a dated trigger. `M818`'s >15% NVDA server price increase names **memory costs** as the cause. `exc20` **+1.992** contradicts `exc5` −2.655. **Four of eleven book names sit here and `SECTOR_DEEP_SEMI.md` is 40 days old.** | ★ **PROMOTE-TO-DEEP — 5th slot** |
| **ENRG / tanker-freight leg** | **`FRO` 08-28 (D-4)** | `S109` is already armed on `FRO`. Hormuz traffic is at "single digits" against >130 vessels/day pre-war; supertanker rates are at record highs (`oilprice` 08-20 body) | **WITHIN-RUN-WATCH** — 🚫 **cannot be promoted: `FRO`, `STNG`, `DHT`, `TNK` are ALL outside `us_top300`** (`D341`), so a DEEP slot could produce no flow-tagged name |
| **MATR / US petrochemicals** | none ≤5 sessions (the transaction has no dated milestone) | **Shell's $8bn US chemicals exit with `XOM`, LyondellBasell and Apollo bidding** — surfaced only by `burst` (`CHEMICALS` z **13.2**, 100% market relevance) against a term table with no chemicals bucket. If `XOM` is the buyer, its standing 🔴RESOLVED *control* role is falsified | **WITHIN-RUN-WATCH**, dated **2026-09-30** (`S122`). 🚫 `LYB`/`DOW` untaggable |
| **UTIL / rates-sensitive leg** | **Jackson Hole 08-27 (D-3)** · **July PCE 08-28 (D-4)** | The against-us case: our UW− rests on flow (`participation` **0.0%**, `exc20` −11.469), and the desk's own measured rate betas say the duration underweight has **no rate beta** (`XLU` +0.0049/bp). **A dovish Warsh would not rescue UTIL by our own measurement** — which means the UW is *not* a rates bet, and its real risk is elsewhere | **WITHIN-RUN-WATCH** — the lens **agrees** with the tilt here, and says so explicitly rather than manufacturing a challenge |
| **INDU / trade transmission** | **08-28** (`P92`/`P93` settle) — but the object's own effective date is **09-08** | Already the tilt's only live transmission test at **−1.29σ** | **WITHIN-RUN-WATCH** + `S123` bracket (below) |

⚠ **What this lens could NOT independently check** (the in-context cost): it inherited this run's
universe, so any leg whose names are outside `us_top300` is invisible to it by construction — the
tanker leg is the known case, and there may be others it cannot name.

## Lens 2 · REGIME-FLIP / BOTH-SIDES — for each binary, the branch that hurts us

> Every threshold below is stated **against the implied move**. A threshold inside the implied move is
> **pre-declared no-information** and is not presented as a trigger (`D242` — bands are not re-set).

### `S118` — ★★★ `NVDA` 08-26: is the print about NVDA, or about memory? (**D-2 binary, mandatory bracket**)
- **Registered 2026-08-24 by the `industry_US` PREMORTEM.** ID 3-grep at WRITE time: **0 hit** in
  `handoff/*.md`, `llm_outputs/**`, `REPORT/**`; current highest `S117`.
- **Why it exists — and why it is NOT a duplicate of `S115`/`S117`/`P90`.** Those bracket NVDA's own
  print and the memory-cost mechanism. **This row brackets the RELATIVE pricing** that §0-a measured:
  three non-printing memory/storage names carry higher ATM IV than the printer.
- **Frozen observable**: over **2026-08-26 close → 2026-08-28 close**, `EW{MU, SNDK, WDC}` 2-session
  excess return **vs `NVDA`** — ⚠ **the benchmark is `NVDA` itself, named inline (`C1`), and it is
  deliberately NOT `SPY`**: the row asks which chain layer gets paid **relative to the printer**, so
  an index benchmark would answer a different question.
- **A (the print is about memory — against our IT `N` and against the AI-compute epicentre framing)**:
  `EW{MU,SNDK,WDC}` − `NVDA` **≥ +6.50pp**. ★ **Outside the implied move**: `NVDA`'s own 08-28
  straddle is **±6.13%**, so a 6.50pp *relative* gap requires more than NVDA's whole priced move in
  one direction. **Carries information.**
- **B (the print is about NVDA)**: `EW{MU,SNDK,WDC}` − `NVDA` **≤ −6.50pp**.
- **C** between — **the favourite, disclosed (`L3`)**, and it spans 13pp because all four implied
  moves are large.
- **Information content (B4)**: **A falsifies** the desk's `AI-compute-EPICENTER` label as the right
  unit — the money would be saying the cycle's marginal information lives one layer back. **B
  falsifies** `S117`/`M874`'s options-market inference. **Neither branch merely confirms.**
- **Anti-signal (VOID)**: a **memory-maker pre-announcement or guidance revision with a named date**
  (`MU`, `SNDK`, `WDC`, Samsung or SK hynix) inside 08-24→08-28. ⚠ **Base-rate checked**: `MU` does not
  print until **09-24** and no memory name has a scheduled event in the window, so this is a genuine
  low-probability void, not an escape hatch.
- **Owner**: `industry_US`.

### `S119` — ★★ Bessent's 14:00 ET sanctions presser TODAY (**D-0 binary, mandatory bracket**)
- ID 3-grep at WRITE time: **0 hit** in all three trees.
- **Why it exists**: a dated binary that **`catalyst_calendar` does not carry**, firing inside this
  run's own working window, on the axis carrying our only OW with a live macro driver.
- **Frozen observable**: over **2026-08-24 close → 2026-08-27 close**, the equal-weight **Energy**
  basket's 3-session excess vs **`SPY`**.
- **A (escalation prices — our ENRG OW is helped)**: Energy 3-session excess vs `SPY` **≥ +2.60pp**.
  ★ Threshold set at **+0.60σ** of the trailing-60 3-session distribution scaled from the measured
  5-session sd **4.325** (⇒ 3-session sd ≈ **3.35**), against a mean of +0.607×3/5 ≈ +0.36.
- **B (sanctions are already priced / the exception channel dominates — our ENRG OW is hit)**:
  Energy 3-session excess **≤ −2.60pp**.
- **C** between — the favourite, disclosed.
- **Information content**: **B falsifies** the war-premium leg of ENRG OW directly, and it is the
  branch this run's own evidence points at — the **LIVE INTRADAY** tape already sold crude
  (Brent −1.3%) on the Iraqi-permit news **before** the presser. **A confirms**, and is graded the
  weaker branch. ⚠ **Registered anyway** because the desk's ENRG OW is its largest live macro tilt and
  a D-0 binary on it with no bracket is the exact violation this stage exists to prevent.
- **Anti-signal (VOID)**: the presser is **postponed or cancelled**, or a **US–Iran direct-talks
  announcement with a named date** lands in the window. ⚠ Base-rate checked: the presser is confirmed
  in an outlet body with a time-of-day, so postponement is the low-probability leg.
- **Owner**: `industry_US`.

### `S120` — ★★ Jackson Hole 08-27: Warsh's first speech as Chair — and our duration UW has no rate beta
- ID 3-grep: **0 hit**.
- **Frozen observable**: `DGS30` and `T10YIE` from `[FRED]`, at the **first observation where BOTH
  carry 2026-08-28**. ⚠ **The observation-lag clause is written INTO the row** (`D333-KR`): H.15
  publishes ≥1 business day behind `T10YIE`, which is why `S102` has sat unsettled for five runs.
- **A (supply/term-premium dominates)**: `DGS30` **≥ 5.31** (its 365-day maximum, 08-20 value 5.23)
  **AND** `T10YIE` ≤ **2.38**.
- **B (Warsh is read dovish and the long end retraces)**: `DGS30` **≤ 5.10** **AND** `T10YIE` within
  2.28–2.40.
- **C** between — the favourite, disclosed. `DGS30`'s realised 8-observation range is **5.19–5.31**.
- **Information content**: **A falsifies** any residual "the long end is inflation" reading
  (breakeven at the 59th percentile vs real yield at the 89.5th already argues against it). **B
  falsifies** `P94` and this run's whole supply framing. Neither confirms.
- **Anti-signal (VOID)**: an **intermeeting Fed action** or a **Treasury refunding announcement**
  inside the window. ⚠ **Base-rate checked and NOT remote** — `Treasury buyback` is the board's only
  🟢FRESH theme (age 5) and `brief` carried *"Treasury may tap $1 trillion cash account for bond
  buybacks."* **Disclosed as live rather than assumed away.**
- ⚠ **Deliberately NOT double-counted with `P94`**: `P94` settles on 08-27, `S120` on 08-28, and they
  share the `DGS30`/`T10YIE` pair. **If both fire the same way that is ONE observation, not two** —
  registered here so no later stage counts it twice.
- **Owner**: `industry_US`.

### `S121` — ★ July PCE 08-28 · **DROPPED, and the reason is the point**
- **Graded before registration and dropped**: `P67`, `P81`, `P85`–`P89` and `S116` **already settle on
  08-28**, all keyed to the same print. **The desk holds seven rows on one binary.** Per the standing
  rule — *"if neither branch would change the conclusion, the event is not worth bracketing"* — an
  eighth row on July PCE adds no information and would inflate the board's apparent coverage.
- ★ **The finding this produces instead**: **date-clustered brackets are one observation, not seven**
  (`B3`). **08-28 currently carries 7 rows + `FRO` earnings + July PCE.** If they resolve together the
  desk will read seven confirmations from **n ≈ 1**. ⇒ **`D343`.**
- **ID `S121` is consumed and left unused** so the number cannot be silently re-allocated later.

### `S122` — ★★ Shell's $8bn US chemicals sale: does `XOM`'s "control" role survive?
- ID 3-grep: **0 hit**.
- **Frozen observable**: a **definitive agreement naming the buyer and the price**, reported in **≥2
  outlet bodies**, by **2026-09-30**. Grade `[news]`, not `[measured]` — no price threshold.
- **A (`XOM` is the buyer)**: `XOM`'s standing **🔴RESOLVED *control*** status is **falsified** — a
  control does not commit $8bn to a downstream asset — and its ledger row (`A.flow미도착` → 09-16)
  must be re-argued or retracted at BET.
- **B (a non-`XOM` buyer, or no definitive agreement by 09-30)**: the item is Shell portfolio news with
  no US read-through, and EVENT_ALPHA Card 8 is void.
- **C**: an agreement naming `XOM` as one of several parties in a consortium — **disclosed as a live
  outcome, not a dodge**.
- **Information content**: **A falsifies a role this desk assigned itself** ("a control, not a bet"),
  which is the most expensive kind of error to leave standing. **B falsifies the card.** Neither confirms.
- **Anti-signal (VOID)**: Shell **withdraws the asset from sale** with a named announcement.
- **Owner**: `industry_US`.

### `S123` — ★★ The trade war's IMPLEMENTATION, which no existing row reaches
- ID 3-grep: **0 hit**.
- **Why it exists — `D342`**: `P92` and `P93` both settle **2026-08-28**, and **Canada's retaliation
  takes effect 2026-09-08.** Both rows can only measure the announcement. **No row on this board spans
  the effective date.**
- **Frozen observable**: over **2026-09-05 close → 2026-09-12 close** (a window straddling 09-08), the
  equal-weight **Industrials** basket's 5-session excess vs **`SPY`**.
- **A (implementation prices — INDU UW− is right for the right reason)**: Industrials excess
  **≤ −3.10pp** (−2.0σ on the trailing-60 mean **+0.437** / sd **1.681**).
- **B (implementation is a non-event — the announcement was the whole move)**: Industrials excess
  **≥ +0.44pp** (i.e. at or above its own trailing mean) over the same window.
- **C** between — the favourite, disclosed.
- **Information content**: **A** distinguishes a transmission story from an announcement story that
  `P93` cannot, because `P93` closes before the tariffs exist. **B falsifies** the INDU UW−'s trade
  rationale entirely — the sector would have absorbed a 50% tariff regime taking effect. Neither confirms.
- **Anti-signal (VOID)**: a **US–Canada agreement with a named effective date**, or a **US
  proclamation with a named effective date excluding Canada**, before 09-08. ⚠ Base-rate checked:
  *"Canada Turned Down a US Tariff Deal"* (08-23 head) — a deal was live and was refused.
- ⚠ **Correlated with `P93`, and the flag is registered so it is not double-counted**: if `P93`-A and
  `S123`-A both fire, that is **one compounding object measured twice**, not two independent confirmations.
- **Owner**: `industry_US`.

### `FRO` 08-28 and `AVGO` 09-02 — bracketed already, not re-registered
`S109` (`FRO` 5-session excess vs `SPY`) and the `AVGO`-side rows are armed. **No new row.** ⚠ `FRO` is
**outside the universe**, so `S109` settles on a name this desk cannot flow-tag — noted, not fixed here.

## Lens 3 · MOMENTUM-CONTINUATION — "already ran" is not a verdict

> Re-tagged against the standing rule that **`rs60` h=5 IC is `−0.1310`, `t(NW) −5.46` in the US
> ledger** (HANDOVER §6) — i.e. this desk's own measurement says high 60-day RS ranks *against*
> 1–5-session forward returns in the 07-13→08-20 window. **That makes this lens the run's most
> load-bearing, and it argues for EXHAUSTED more often than the tape does.**

| Runner | rs20 / rs60 | Re-tag | Flip condition (dated) |
|---|---|---|---|
| **`MPC`** | +13.0 / **+44.0** | **EXTENDED-BUT-LIVE** — OBV 매집, `M833` R&M margin **+106.7% YoY on LOWER utilisation**. The cycle KPI is still accelerating | ⚠ **but the issuer attributes it to conflict-driven supply disruption (`M832`) — event-durable, not structure-durable.** Flips **EXHAUSTED** if `S119`-B fires (Energy 3-session excess ≤ −2.60pp by 08-27) |
| **`PSX`** | +13.8 / **+37.0** | **EXTENDED-BUT-LIVE**, same chain, same KPI | Same flip. Additionally: `MPC`+`PSX` are **one measured risk unit in all three `--days` windows** — the only `G4`-robust grouping this desk owns, so they cannot be treated as two confirmations |
| **`VLO`** | +11.7 / **+43.1** | ⚠ **EXHAUSTED-WATCH** — highest rs60 of the three but **`vol_surge` 0.71**, the weakest volume in the group | Flips **EXTENDED-BUT-LIVE** if `vol_surge` ≥ 1.0 with OBV still 매집 by 08-28 |
| **`HPE`** | +8.5 / **+41.6** | **EXTENDED-BUT-LIVE** — OBV 매집, held. `S110` (the `HPE`−`DELL` pair test) is armed | Flips if `S110` settles against the pair |
| **`DELL`** | −2.6 / **+42.8** | 🚨 **EXHAUSTED** — the clearest case on the board: **rs60 +42.8 with rs20 −2.6 and OBV 분산**. The 60-day number is entirely historic | Flips back only if OBV returns to 매집 **and** rs20 > 0 |
| **`MSTR`** | **+26.5** / **−24.7** | 🚨 **EXHAUSTED-GEOMETRY (`D306` class)** — a 20-day spike sitting on a **losing** 60-day base. ⚠ **This is the shortlist's only "clean rise" (FINRA z −1.23)**, i.e. the lens contradicts the shortlist | Filed to the miss ledger with `--enters-if rs60 ≥ 0`. **Not handed to BET** |
| **`COIN`** | +14.2 / +5.3 | **EXTENDED-BUT-LIVE** but ⚠ **`COIN` and `MSTR` are one bet in two GICS labels** (both bitcoin beta, Financials and IT) — **the correlated-UW pattern in its long form.** Counting them as two greens overstates board breadth by one | Flips if bitcoin's own 20-day trend turns while both remain 🟢 |
| **`MRK`** | +12.8 / +24.8 | **EXTENDED-BUT-LIVE** — 🟢, surge 1.56, sector rank 1 on three instruments | ⚠ **Zero narrative coverage** — flips to unrateable, not to EXHAUSTED, if HLTH DEEP finds no mechanism |
| **`TGT`** | +17.3 / +26.9 | **EXTENDED-BUT-LIVE** — clears the gate on volume (1.51) | Flips if `WMT`'s −14.6 rs60 spreads to the sector's equal-weight |
| **`FCX`** | +18.8 / +18.4 | ⚠ **EXTENDED-BUT-CROWDED** — `Copper` COT at the **100th percentile** long | Flips **EXHAUSTED** if Copper's percentile holds ≥ 95 while rs20 rolls under 0 |
| **`SCHW` · `BAC` · `JPM`** | +6.5/+29.1 · −4.2/+18.7 · −4.1/+15.4 | ⚠ **EXHAUSTED-WATCH ×2** — `BAC` and `JPM` both carry **negative rs20 on strongly positive rs60**, the `DELL` shape one notch milder | Flip on rs20 > 0 with OBV 매집 held |
| **`ANET` · `MRVL`** | +4.8/+20.2 · +18.4/+17.3 | **EXTENDED-BUT-LIVE** both — the only two AI-compute names with **both** RS legs positive | `MRVL` prints **08-27**; short interest **4.8% of float BUILDING** (LIVE INTRADAY) is squeeze fuel on a dated trigger |

★ **Lens-3 headline: seven of thirteen runners re-tag to EXHAUSTED or EXHAUSTED-WATCH, and the desk's
own `rs60` measurement predicts exactly that shape.** ⚠ **Counter-caution, stated so the lens does not
over-fire**: the `rs60` cell's window contains the mid-August drawdown, `n_eff` is 5.4, and a
mean-reversion result from a drawdown does not generalise to a trending tape. **The re-tags are
watch-conditions, not verdicts.**

## Lens 4 · CYCLE-EXPOSURE — epicenter vs one-layer-off, against the REAL book

`cycle_exposure.py` prints **✅ no GAP**: AI-compute rank 1 epicenter **16.4%** vs need ≥12.0%
(`NVDA`, `ANET`) · Energy/refining rank 2 **10.0%** vs need ≥8.0% (`MPC`, `PSX`) · Missile-defense
rank 3 **3.83%** (`RTX`, **no threshold set**).

🚨 **The lens rejects the ✅ as under-determined, and gives three numbered reasons:**

1. **A cycle with no registry row cannot produce a GAP flag — it produces a silence.** The
   **optical/interconnect** cycle has **no row** (`D250`/`M731`, 4th run). `LITE` **+0.639**,
   `COHR` +0.158, `CIEN` **−0.380 🔴 rs60 −34.0** are carried in the standing view on sweep numbers
   with **no file of their own**. ⇒ **exposure is unmeasurable, not zero — and "unmeasurable" is
   exactly what the 2026-07-14 postmortem that created this stage was about.**
2. **The rank-1 cycle's 16.4% is computed on a label that spans 2–3 measured risk units** (`D329`,
   `M837`): `risk_units` puts **`NVDA` as a singleton in all three windows and never groups it with
   `AVGO`**, while `ANET`+`AVGO` merge at 500d and 750d. ⇒ **"16.4% epicenter" is one number over an
   inconsistent unit**, and per `G4` any concentration sentence must carry its `--days`. **It does not.**
3. **Missile-defense has no threshold**, so rank 3 can never flag. ⚠ **`RTX`'s customer has been
   unmeasured for 207 days (`W4`)** — the exposure is held without the buyer being named.

★ **Cleanest epicenter expressions, named as the lens is required to** (analytical, not a
recommendation): within AI-compute the only two names with **both RS legs positive vs `SPY`** —
`ANET` **rs20 +4.8 / rs60 +20.2** (held) and `MRVL` **+18.4 / +17.3** (**not held**, prints 08-27) —
**and OBV 매집 alongside them** *(RULE D6 — grade-C, cited only beside the two RS legs, never alone)*. Within
Energy/refining the epicenter is already held at 10.0% (`MPC`, `PSX`, one risk unit).
🚫 **A 🔴 tape gates ADD timing; it never justifies zero core** — and no rank≤2 cycle is at zero today,
so that rule is not invoked.

⚠ **What this lens could NOT check**: whether `cycle_registry.json`'s rank ordering is itself current.
It is a static file and this run did not re-derive the ranks.

## 5 · Synthesis — what this stage changes

| Output | Result |
|---|---|
| **DEEP set** | ★ **UPDATED to N=5**: continuous `[ENRG, HLTH]` · rotating `[COMM, STPL]` · **+ PREMORTEM-PROMOTED `IT`** (Lens 1 — `NVDA` D-2, `MRVL` D-3, `exc5`/`exc20` sign split, 4 of 11 book names, `SECTOR_DEEP_SEMI` 40 days). **Mandate is narrow and disjoint from the other four: resolve §0-a — is the printer or the memory layer carrying the information?** |
| **Brackets → ALPHA** | **`S118`** (NVDA-vs-memory relative, 08-28) · **`S119`** (Bessent presser, D-0, 08-27) · **`S120`** (Jackson Hole, 08-28) · **`S122`** (Shell/`XOM`, 09-30) · **`S123`** (trade-war implementation, 09-12). **`S121` graded and DROPPED with its reason.** All five carry both branches, frozen thresholds, dated settles, and base-rate-checked anti-signals |
| **Momentum re-tags → BET** | 7 of 13 runners to EXHAUSTED / EXHAUSTED-WATCH, each with a dated flip condition. ⚠ **`MSTR` contradicts the shortlist's only "clean rise"** — the lens wins, the name is not handed forward |
| **Cycle GAP → BET** | **✅ overturned to ⚠ UNDER-DETERMINED**, three numbered reasons. No new epicenter purchase implied (P4) |
| **New digs** | **`D343`** — 08-28 carries **7 pre-registered rows + July PCE + `FRO` earnings**; resolving together they would read as seven confirmations from **n ≈ 1** (`B3`). **Positive-form remedy: print a per-settle-date row count at registration, and when a date exceeds ~3 rows, require the new row to name which existing row it is NOT redundant with** — `S118` and `S120` each do this above, and `S121` was dropped by it |

## ✅ EXIT CHECK

- [x] 4 lenses run — ⚠ **serially in-context, deviation declared (7th run)** with its cost stated.
- [x] Every bracket names observable + frozen threshold + date, **both branches**, and is registered
      below to `SCENARIOS_US.md` + the `SCENARIOS.md` MASTER INDEX at run end. **Zero one-way brackets.**
- [x] Every magnitude threshold stated against the implied move (`NVDA` ±6.13% / `MU` ±6.52% /
      `SNDK` ±8.41% / `WDC` ±11.56%, all 08-28, read from the chain because **`D315` broke the tool**).
      `S118`'s ±6.50pp is **outside** NVDA's implied move and is declared so.
- [x] Each branch graded by information content; **`S121` dropped** because no branch would change the
      conclusion, with the reason written.
- [x] Both **≤48h** binaries bracketed — `NVDA` (D-2, `S118`) and the Bessent presser (**D-0**, `S119`).
- [x] Under-computed legs **promoted (IT) or logged as within-run watch** (ENRG-tanker, MATR-chemicals,
      UTIL-rates, INDU) — none silently dropped.
- [x] Cycle GAP re-read and **overturned to UNDER-DETERMINED** with three reasons; handed to BET.
- [x] **DEEP set restated: N=5 — `[ENRG, HLTH, COMM, STPL, IT]`.**

---
*Adversarial analysis only. No buy/sell recommendation, no sizing, no grade change (P4).*
