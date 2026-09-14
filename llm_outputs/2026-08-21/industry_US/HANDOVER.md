# HANDOVER — industry_US · 2026-08-21 (Fri) · Stage 2/11 · L1·HANDOVER

> Inheritance packet. **This stage transports analysis; it makes no market call, names no size and
> issues no buy/sell language (P4).** Run clock **KST 22:09–23:0x = ET 09:09–10:0x, US cash
> pre-market** (bell 22:30 KST). Terminal settled bar throughout: **2026-08-20**.
> Read: `handoff/STANDING_VIEW.md` (spine §1–§6 + §5 retracted ledger through **`R88`**) ·
> `STANDING_VIEW_US.md` (§2 fact table, §3a per-name rows) ·
> `SCENARIOS.md` (spine: scoring log + MASTER INDEX) ·
> `SCENARIOS_US.md` (**S1–S107**, opened in full for past-dated rows) ·
> `SCENARIOS_KR.md` (**opened** — the other market's file is this run's to score if past-dated) ·
> `RESEARCH.md` (Part A triggers · Part B lenses · Part C dig list through **`D298`** / **`D303-KR`**).

---

## §0 · Instrument health inherited — what this run may NOT claim

`llm_outputs/2026-08-21/preflight/PREFLIGHT_US.md` **was run** (22:09–22:26 KST, this run's own
stage −1). **PASS 3 / FAIL 5.** The rights table binds every stage below and is not re-litigated here.

**Revoked for this run:** the sweep's news-velocity axis · theme freshness · any "it went quiet"
sentence · `breadth` as a news-informed reading · the 50 velocity survivors **as a set** · the
**Communication Services `wflow` sign** (`GOOGL` at 38.3% owns it) · any concentration number
without its `--days` · `wflow` cap-weights described as *current* (weights are **37 days** old) ·
any flow/RS/OBV/short call on **`EA`** · `--ic`-derived sizes as evidence-backed · any 08-21 price.

**Granted:** settled prices and every price-derived statistic through the **2026-08-20** close · a
**one-session Δ (08-19 → 08-20)**, the third clean single-session Δ in a row · `eqflow` and the ten
non-flipper sector signs · FINRA short pressure · CFTC COT · FRED · primary filings ·
`module_chart --read` and `margin_history <T>` (with the "`--help` dead, output probed" stamp) ·
hand-probed per-name news velocity (**40/40 valid at 22:18 KST**).

★ **One genuinely new instrument fact, and it changes how G1 must be read downstream.** The news
tunnel was **verifiably UP** across the whole sweep window — `fts search Nvidia --days 7 --count
--scope foreign` returned **3523 at 22:09 (before the sweep)** and **3523 · 3523 · 3523 at 22:20** —
and the sweep's velocity axis died anyway at **16.72% (50/299)**. This morning's KR run measured the
opposite condition (a real TLS outage, `curl` exit 35) and got **6.05% (50/806)**. **The same ~50
answered names under a dead tunnel and under a live one** ⇒ the survivor count is not a function of
news availability *or* of server health, and no stage may treat it as one.

⚠ **Two carried rules travel with the granted Δ into SWEEP and ROTATION, unchanged:**
- **`D293`** — `sector_flow` publishes `delta` but not `rs20_earned` / `rs20_rolloff`. A rolling
  20-session excess advances by dropping sessions off the back as well as adding them at the front.
  On 08-19 that defect **cost one promotion of two** (`R82`). Today's Δ spans **one** session, so the
  roll-off share is one session in twenty — smaller, **not zero**.
- **`R81`/`D290`** — `flow_tag` does **not** take the run-level axis set while `flow_score` does.
  With `vel_axis=false`, a 🟢 may still be velocity-derived. **No stage may promote on a tag today.**
  ⚠ Two prior runs wrote that sentence and then used the tag anyway. Writing it is not complying
  with it. **Today's board carries 3 greens** (`MSTR` +0.900 new-🟢 · `TGT` +0.889 · `MRVL` +0.539);
  all three are unusable **as tags**, and their underlying `obv_norm`/`rs20`/`flow_score` are not.

---

## §1 · Inherited regime call and standing view

**Regime (spine §1, `[inferred]`, unchanged):** *memory is a price-cycle industry in rate-of-change
deceleration while its level stays tight* — the equity tracks the **second derivative** of price, not
the level, which is why "shortage persists" and "stocks struggle" are both true.

**Carried per-name theses (§3a).** Tags preserved; no `[inferred]` row is passed downstream as
evidence. The right-hand column is **this run's own measurement on the 08-20 settled close**, not the
inherited sentence.

| Node | Carried state | Tag | Measured today (08-20 settle) |
|---|---|---|---|
| **`MPC` · `PSX` · `VLO`** | Refining-**capacity** destruction; constraint is `L2` peak-margin, not the barrel | `[measured]` price · `[filing]` structure | 🟡 PARTIAL. flow **+0.700 / +0.733 / +0.506**, rs60 **+42.8 / +36.4 / +39.8**, all three OBV 매집. ⚠ **`PSX` FINRA short-vol z flipped to +1.95 🔴 (5v5 +13.5▲)** — new, and it is the *only* refiner with that shape (`MPC` −0.52, `VLO` +0.49). `S88` settles **08-21**; pre-settle **+2.930** |
| **`RTX`** | The defense group's **beta**, not its leader; negative tech beta makes it the book's diversifier | `[measured]` | 🟡 PARTIAL. rs60 **+17.0** but rs20 **−1.8** and **delta −0.435 — the largest single-session deterioration among the book's 11 names.** **Customer still unmeasured, now 204 days (`W4`)** |
| **`LMT` · `NOC` · `GD`** | The defense accumulation is real and is **not `RTX`'s** — replicates on both OBV instruments | `[measured]` | 🟡 PARTIAL. All three OBV 매집; rs20 −2.8 / +2.4 / −2.2. 🚨 **New and unattributed: FINRA short-vol z `NOC` +2.43 · `LMT` +1.76 · `LHX` +1.35 — three of the four defense names now print a 🔴/elevated short axis on the same settled close.** `S97` settles 08-21 |
| **`NUE`** | Post-earnings re-rate predating the tariff thread by 12 sessions; carried as *"the sheet's only 🔴 FINRA axis (z +1.99)"* | `[measured]` | 🚨 **The carried FINRA sentence is STALE and is corrected here, not deleted (§11).** Measured today **z −2.33 = 🟢 short covering**, 5v5 **+1.2▲**, short% 35.8 vs base 50.6. **The registered kill (z > +1.5 for 5 sessions with OBV still 매집) did not fire; it reversed.** flow +0.224, OBV 매집, `vol_surge` **1.25** — the only book name clearing 1.2 |
| **`T`** | 🚨 An orphan position — **9.74%** of the real book's invested, no cycle label, no card, no thread | `[measured]` | 🟡 PARTIAL. rs20 **+6.2**, rs60 **−1.1**, OBV 매집, `vol_surge` **0.46** (lowest on the board's carried set). **Its rejection row was resolved this run — see §3.** `S107` → **09-03** |
| **`WMT` · `TGT`** | The Staples carriers, and they disagree | `[measured]` | 🚨 **They disagreed violently on the print.** `WMT` **−9.15% on 08-20 alone** (114.30 → 103.84), flow −0.160, rs60 −14.0, FINRA z **+3.02 🔴 (5v5 +10.9▲)** — the largest short-side reading on the board. `TGT` flow **+0.889**, rs20 +14.4, rs60 +24.6, OBV 매집. `S100` settles **08-21**; pre-settle **−2.407** |
| **`GOOGL`** | Half the COMM underweight is already wrong | `[measured]` | 🟡 PARTIAL. flow +0.251, **delta +0.459 — 2nd largest on the board**, OBV 매집, FINRA z −1.34. ⚠ **It is also today's G3 flipper** (38.3% of COMM) ⇒ the sector sign may not be cited, the name may |
| **`KKR` · `LITE` · `ORCL`** | Cross-sector orphans, carried because their sectors hold no DEEP slot | `[measured]` | 🟡 PARTIAL ×3. `KKR` +0.651 / `LITE` +0.403 (delta **+0.221**) / `ORCL` +0.444 with rs60 **−28.0** |
| **`XOM`** | 🔴 RESOLVED — the crack-attribution **control**, and a control is not a bet | `[measured]` | Still flat: flow **+0.017**, rs20 +2.6, OBV 중립. Ledger `A.flow미도착` → **09-16** |
| **`FCX` / the `Copper` COT** | 🔴 RESOLVED — survives as a risk, not a thesis | `[measured]` | **Copper COT back to the 100th percentile** this week (+3,265 WoW, 27.1% of OI). Unchanged in kind |
| **The optical/interconnect cycle** | 🚨 `cycle_registry.json` has **no row** for it ⇒ exposure is **unmeasurable, not zero** | `[measured]` | `LITE` +0.403 OBV 매집 vs `COHR` −0.049 OBV 중립 vs `CIEN` **−0.654 🔴 rs60 −36.4** — the three names have stopped agreeing. `S86`/`S96` settle 08-21; pre-settle **−6.400 / −6.254**, both already inside branch B |

**Settled 08-20 read on the 11 book names** (three-axis; tag NOT used as evidence per `R81`):

```
PSX  +0.733 rs20 +12.6 rs60 +36.4 OBV매집 surge 1.12    MPC  +0.700 rs20 +11.4 rs60 +42.8 OBV매집 surge 1.06
HPE  +0.487 rs20  +7.7 rs60 +37.4 OBV매집 surge 0.70    NUE  +0.224 rs20  −3.6 rs60  −1.5 OBV매집 surge 1.25
RTX  +0.182 rs20  −1.8 rs60 +17.0 OBV매집 surge 0.99    ANET +0.033 rs20  +0.7 rs60 +14.7 OBV중립 surge 0.73
NDAQ −0.021 rs20  +4.6 rs60  +5.7 OBV중립 surge 0.55    ETN  −0.075 rs20  −3.3 rs60  +1.4 OBV매집 surge 0.73
MET  −0.175 rs20  −2.3 rs60 +10.6 OBV중립 surge 0.73    NVDA −0.199 rs20  +0.6 rs60  −0.7 OBV중립 surge 0.71
AVGO −0.397 rs20 −10.6 rs60 −15.3 OBV중립 surge 1.07
```

★ **All 11 are 🟡. Not one green, not one red** — the first time this run's HANDOVER has been able to
write that sentence about the whole book. `AVGO` remains the weakest on price (rs20 −10.6, rs60 −15.3)
but its OBV moved **분산 → 중립** and its FINRA z is **−1.60 🟢 (short covering)**; the 08-20 packet's
*"the only book name tagged 🔴"* no longer holds on either axis.

### Retracted ledger read BEFORE forming today's view (spine §5, through `R88`)

The five that bind this run:
- **`R78` · `R81`** — *a 🟢 tag is not evidence while `vel_axis=false`*. **Binding constraint, not a
  caution.** Applies today to `MSTR`, `TGT`, `MRVL`.
- **`R82`** — the **Consumer Staples UW− → UW promotion is withdrawn** (Δ +0.325 was 77.7% roll-off).
  ⚠ Health Care N → N+ is explicitly **not** retracted. ⚠ Energy was the only sector whose
  improvement was fully earned. **`S100` still settles regardless** — a withdrawn verdict does not
  release the desk from scoring what it registered.
- **`R80`/`R84`** — the "survivor set is deterministic / burnt in the first 51 tickers" shape is
  **refuted in both markets**. Today's US shape (41 runs, longest 3, 33 singletons, indices 1–289)
  reproduces the *arbitrary* shape a third time. `W1`.
- **`R83`** — `theme_age` does **not** cap its age readout; 🟢LIVE reads zero because the
  **conjunction** is unmet on a desk trading multi-quarter cycles. **Arithmetic, not a tool defect.**
- **`R87`/`D298`** — the refiner kill counter *"one has fired"* had silently reset. **The general form
  binds this packet directly**: any carried claim containing a COUNT or a STATE needs re-computation
  each run. **This run found a second instance of exactly that class and fixed it in §1 (`NUE`'s
  FINRA sentence) and a third in §5 (the ledger-staleness claim).**

**Nothing in this packet re-argues a retracted claim.** Any stage wanting a Staples promotion, a
survivor-set selection reading, a `theme_age` cap story, or a tag-as-evidence promotion must bring a
*new* measurement and name the retraction it is overturning.

---

## §2 · Scenarios — verified, deferred with pre-settle readings, and one flagged

### (a) Already scored by the sibling desk — verified, not re-scored

The `industry_kr` run of this morning (09:2x KST) scored the **three US-owned rows whose 08-20 settle
had arrived at 05:00 KST**. This desk opened `llm_outputs/2026-08-21/industry_KR/HANDOVER.md` §3c–3e
and **verified the entries exist**; ownership confers no exclusivity (README §3).

| ID | Verdict | Observable at settle | Note verified |
|---|---|---|---|
| **`S82`** | **FIRED-A** | `XLV` exc5 − EW{`XLU`,`XLRE`,`XLP`} exc5 = **+2.879** ≥ +2.45 | Health Care **decoupled upward** out of the duration complex ⇒ it is **not** the 4th leg. ⚠ The KR desk records the honest caveat that the state was **already above A (+3.091)** at registration |
| **`S83`** | **FIRED-C** | [`ANET` exc5] − [`HPE` exc5] | The board's widest estimator (sd 8.417) landed in its disclosed heavy-favourite branch — **`L3` fired as registered** |
| **`S98`** | 🚨 **VOID** | — | Its own anti-signal fired: the **FOMC minutes of 2026-08-19** are an FOMC-dated communication inside the 08-13 → 08-20 window. **The 08-20 US HANDOVER flagged this VOID risk BEFORE the observable settled**, on a board whose pre-settle read (all four legs positive) pointed at the branch the desk would most have liked to fire. **The clause governed, and that is the point of pre-registration** |

★ **`S98`'s VOID is the more useful of the three**, and the KR desk registered why: **`D300-KR`** —
an 8-calendar-day US window essentially always contains an FOMC/CPI/PPI communication, so that
anti-signal was **designed to void**, and the mechanism it assumes was **already refuted by this
desk's own `S102` regression** (four legs at +0.0049 / −0.0072 / +0.0224 / +0.0185 pp per bp of Δ10y
⇒ **no measurable rate beta**). **The dig is handed back to this desk as its owner** and appears in §9.

### (b) Deferred with the settle clock stated — the 08-21 dense batch

**Fifteen rows settle on the 2026-08-21 close, which arrives 05:00 KST 2026-08-22, after this
pre-market run ends.** They are **deferred, not `EXPIRED`** — the mechanical D→D+1 rule. Pre-settle
readings below are **4 of 5 sessions (08-14 → 08-20 settled closes)**, `yfinance auto_adjust=False`,
benchmark **`SPY`** named inline (`C1`), `SPY` 08-14 → 08-20 = **−1.770%**. **These are readings, not
scores.**

| ID | Observable | A / B thresholds | **Pre-settle (08-20)** | Where it sits |
|---|---|---|---|---|
| **`S84`** | `XLE` exc5 − EW{`XLU`,`XLRE`} exc5 | A ≤ −3.174 · B ≥ +5.544 | **+3.791** | **C**, 1.75pp below B |
| **`S85`** | `RSPT` ret5 − `XLK` ret5 | A ≤ −0.994 · B ≥ +2.046 | **−0.244** | **C**, 0.75pp above A |
| **`S86`** | EW{`COHR`,`LITE`,`CIEN`} exc5 | A ≥ +12.584 · B ≤ −5.948 | **−6.400** | 🚨 **already inside B** |
| **`S87`** | EW{`DELL`,`HPE`} exc5 | A ≤ −4.961 · B ≥ +16.143 | **−8.895** | 🚨 **already inside A (EXHAUSTED)** |
| **`S88`** | EW{`MPC`,`VLO`,`PSX`} exc5 | A ≤ +0.061 · B ≥ +8.144 | **+2.930** | **C**, 2.87pp above A |
| **`S89`** | `NEM` exc5 | A ≤ −5.217 · B ≥ +9.658 | **+10.160** | 🚨 **already inside B** — ⚠ **check the anti-signal first** (below) |
| **`S90`** | `DLR` exc5 | A ≤ −3.199 · B ≥ +5.223 | **−1.153** | **C** |
| **`S91`** | `XLY` exc5 | A ≤ −2.467 · B ≥ +1.553 | **+0.484** | **C**, 1.07pp below B |
| **`S93`** | consumer sign test | A = `WMT`∧`HD`∧`TGT` all negative · B = `TGT`+ while `WMT`,`HD` both − , OR `ABNB`−`HD` > +5 | `WMT` **−8.146** · `HD` **+0.480** · `TGT` **+4.210** · `ABNB`−`HD` **+1.800** | **C** — A fails (`HD`,`TGT` positive), B fails (`HD` positive; the OR-leg is +1.800) |
| **`S95`** | `BZ=F` settlement | A ≥ 93.00 · B ≤ 86.50 | **93.78 (08-20 settle)** | 🚨 **already inside A** — ⚠ anti-signal governs |
| **`S96`** | EW{`COHR`,`LITE`} exc5 ∧ thread outlet count | A ≥ +5.0 ∧ ≥4 outlets · B ≤ −5.0 | **−6.254** | 🚨 **already inside B** |
| **`S97`** | `LHX` exc5 | A ≤ −4.0 · B ≥ 0 | **−5.557** | 🚨 **already inside A (discontinuity)** |
| **`S99`** | `M` = EW{`ANET`,`AVGO`,`HPE`} exc5 · `E` = `ETN` exc5 | A: \|M\|≥3.0 ∧ same sign ∧ \|E\|≥1.5 | **M −6.517 · E −6.252** | 🚨 **all three of A's conditions already met** |
| **`S100`** | EW{`TGT`,`WMT`} 08-18→08-21 − `SPY` | A ≥ +6.5 · B ≤ −6.5 | **−2.407** (`TGT` +3.784 · `WMT` **−9.861** · `SPY` −0.632) | **C** — ⚠ but see the dispersion note |
| **`S102`** | `DGS2` and `30y−10y` `[FRED]` | A: `DGS2` ≥ 4.30 · B: `DGS2` ≤ 4.08 ∧ 30y−10y ≥ 0.59 | `DGS2` **4.19** · 30y−10y **0.54** (FRED asof **08-19**) | **C**, as disclosed at registration |

★ **Four rows are already past a branch line with one session to run, and three of the four are the
branch that goes AGAINST a live desk position.** `S87` (A: the `DELL`/`HPE` runners were EXHAUSTED,
`HPE` is held), `S97` (A: `LHX` succession priced as a discontinuity ⇒ `M704`'s defense EW must be
re-run ex-`LHX`), and above all **`S99` branch A — `ETN` moved with the AI-compute basket, same sign,
both legs far beyond their gates ⇒ the book's AI concentration reads 5 of 12, not 4 of 12, and the
Industrials OW−'s "diversifying leg" is not one.** That is a **live sizing input** and it is handed
to ROTATION and BET as a reading, not a score.

⚠ **Two anti-signals must be checked BEFORE either row is scored tomorrow, and they are named now so
the check cannot be made after seeing the branch (`§4c`/`D48`):**
- **`S89`** voids on *"a gold price move beyond ±8% over the window"*. Measured: `GC=F` 08-14
  **4380.4** → 08-20 **4516.3** = **+3.10%** (settled) and **4641.0 = +5.95%** on the 08-21 live
  quote. **Not fired at the settled bar, and inside 2.1pp of firing on the live one.**
- **`S95`** voids on *"a US refinery outage, PADD3 hurricane landfall, or an OPEC+ quota decision"*
  inside the window. **This run did not measure that clause** — recorded as **unmeasured**, not as
  not-fired (the `AMZN` precedent). It is the scorer's first job.

⚠ **`S99` carries a construction defect** recorded ~90 minutes after its own registration (its
premise, `ETN`–`ANET` +0.722, was cited without the machinery control: `ETN`–`CMI` **+0.811** and
`ETN`–`CAT` **+0.807** are higher, and a joint regression gives β`XLI` **1.396** vs β`XLK` **0.619**).
**The row settles as registered and is not withdrawn**; its branches do not contain the answer, and
the successor test is a **joint-loading** test. **A branch-A firing tomorrow is therefore evidence
about carry, not about labels.**

⚠ **`S100`'s C reading hides its own content.** The basket excess is −2.407, comfortably inside C —
but the two legs are **`TGT` +3.784 and `WMT` −9.861**, a **13.6pp intra-basket dispersion on a
2-session window** against a registered unconditional sd of **2.27pp**. An EW basket built to test
"the big-box node" averaged away the largest single-name print of the window. **Recorded now, before
the settle, as a construction observation — the row is not re-frozen (`D242`).**

### (c) Still armed beyond this window, with dates

**08-24**: `S74` · **08-26**: `S79` `S101` `S103` · **08-27**: `S81` · **08-29**: `S103` readthrough ·
**08-31**: `S92` `S94` `S104` · **09-03**: `S105` `S106` `S107` · **09-30**: `S48`.
⚠ **`S103`** (`NVDA` 08-26) still carries **hand-set ±5.0pp bands** because the readable chain expired
08-21. **`D295` obliges a re-derivation from the 08-26-or-later straddle before the print. Still not
done — second consecutive run.** The chain is now readable (08-21 has passed into the next expiry
cycle); **this is ALPHA's obligation today, not a note.**

### (d) 🚨 `S8` — undated and unscoreable for the **19th** consecutive run

Still on `CATALYST_WATCH` as its undated 🔀binary. **A human must `VOID` it or re-register it with a
date (P5).** `S92`/`S95` bracket what `S8` could not. One line, as last run pre-committed.

**Score this run: 0 newly scored by this desk · 3 verified as scored by the sibling desk · 15
deferred with pre-settle readings and the settle clock stated · 2 anti-signals flagged pre-settle ·
0 `EXPIRED` · 0 silent skips.**

---

## §3 · Both ledgers — audited symmetrically

`reject_ledger.py due` **and** `missed_ledger.py due` were both run (not `score` alone).

**At entry:** rejections **210 rows · 120 resolved · 9 past-due · legacy (no `revives_if`) 0** ·
misses **191 rows · 98 resolved · 5 past-due · legacy 0**.
**At exit:** rejections **126 resolved · 3 past-due** · misses **102 resolved · 1 past-due**.
★ **Legacy count is 0 on both ledgers for the 10th run.** **10 rows resolved this run.**

### Rejections resolved (6 of 9)

| Ticker | Rejected | Outcome | The measurement (08-20 settled close) |
|---|---|---|---|
| **`T`** | 07-24 | ★ **REVIVED** (on ownership) | **Bookkeeping close, the `LITE`/`316140` precedent (`T22`)**: `T` is **held in the real book at 9.74% of invested**. The registered condition **still fails on its own terms** — rs60 vs `SPY` **−1.1**, OBV 매집 — and that is recorded rather than laundered. A rejected name the desk owns is a ledger error, not an open rejection |
| **`PLTR`** | 07-24 | ★ **REVIVED** | **Leg 1 met as written: rs60 vs `SPY` +25.7.** Corroboration only: rs20 +37.7, OBV 매집, flow +0.403 |
| `SLB` | 07-25 | **reaffirmed** | Both legs of the AND fail: rs60 **−9.2** (needs positive) and delta **+0.113** (needs > +0.20) |
| `BKR` | 08-07 | **reaffirmed** | The AND fails on its measurable half: rs60 **−7.5**. The body-proximate co-mention leg was **NOT measured** — recorded as *unmeasured*, not as failed |
| **`TRI`** | 08-07 | ★ **REVIVED** | **OR-leg 2 met**: `llm_outputs/2026-08-10/industry_US/SECTOR_DEEP_INDU.md` names `TRI` inside its value-chain node table (node 8, information/legal-tech). ⚠ **Honest caveat**: the same row says *"Not chain-mapped — outside the AI-power/aerospace value chains entirely"*, so it is a node of its own, not a link in an existing chain. Corroboration only: flow +0.700, rs20 +20.3, rs60 +24.9, OBV 매집 |
| `CF` | 08-08 | **reaffirmed** | Leg 1 fails and is not close: **FY2025 gross margin 38.5% against a 19-year median of 34.6%** (SEC XBRL FY2007–FY2025, high 52.4% FY2022, low 10.5% FY2017) — the condition needs **below** the median. 🚩 **Leg 2 is unmeasurable as written and is flagged, not scored** (§9) |

**Three rejection rows are handed back to `industry_kr`, named rather than dropped**: `073240`
금호타이어 · `047040` 대우건설 · `000720` 현대건설. Their revival conditions are written against **KIS
investor actuals and domestic-scope news**, which this desk cannot measure under `--scope foreign`
(`W1`). ⚠ `047040`'s condition is also the subject of **`D299-KR`** (a *"flow tag turns green"* clause
that scores two ways depending on which instrument is opened) — that is a second reason this desk
should not resolve it.

### Misses resolved (4 of 5)

| Ticker | Missed | Outcome | The measurement |
|---|---|---|---|
| **`TMUS`** | 08-07 | ★ **entered** | **OR-leg 1 met on both halves**: rs20 vs `SPY` **+3.0** AND current-year revision breadth 30d **18↑/3↓**. Corroboration: next-year 15↑/6↓, next-year consensus +2.6%/90d, FINRA z −0.68. ⚠ The desk does **not** hold `TMUS`; this closes as a measured coverage fact |
| `FSLR` | 08-07 | reaffirmed | 🚨 **Structural, the `SPCX` class.** `us_top300.csv` unchanged (300 rows, **37 days**), no `FSLR` row. **And the substitute leg has no population**: a case-insensitive scan of `us_top300.csv` for solar/polysilicon names returns **zero** in-universe candidates. **This row cannot resolve on any market outcome** (P5) |
| `LYB` | 08-08 | reaffirmed | Leg 1 fails at the extreme: **FY2025 gross margin 8.5% is the MINIMUM of the 15-year series** (median 13.9%, high 21.5% FY2015) — 0th percentile against a bar of the 20th. Leg 2: a 21-day foreign-scope scan (21 hits) shows no disclosed price increase following European capacity closures; the Q2 narrative is Middle East disruption lifting EBITDA to $2.1bn |
| `XLY` | 08-14 | reaffirmed | **The AND splits, and both legs were measured on the same settled close as the condition requires**: leg 1 **MET** — `XLY` exc5 vs `SPY` **+0.470pp** (08-13 → 08-20); leg 2 **FAILS** — FINRA short-vol z **−0.64** against a bar of ≤ −1.0. The row stays out on the short-pressure leg alone |

**One miss row is carried, explicitly and not silently**: **`APH`** (08-07, `U.발굴부재`). Its OR-leg 1
— *"IT or an adjacent sector takes a DEEP slot and a file names the connector node"* — is **not
determinable at HANDOVER**; it is a function of this run's own ROTATION. Leg 2 fails cleanly
(`APH` flow −0.304, tag 🟡, `vol_surge` 0.79 ⇒ no volume-confirmed 🟢). **Carried to ROTATION/DEEP
with the `PRU` precedent, and it must not cross a second HANDOVER unresolved.**

⚠ **Sign hygiene (`3c`)**: the two ledgers' `excess` columns are **inverted** relative to each other
and are **not summed** anywhere in this packet.
⚠ **`score` is accumulation, not an edge** — the miss ledger's first rows are outcome-selected.
★ Carried and still binding (`T25`): the rejection ledger's loss asymmetry, and the class this desk
reached for most recently. **Any structural rejection this run makes must re-print that number beside
itself.**

---

## §4 · Exposure state — size context for BET/ALPHA (read-only; this stage never runs `log`)

`exposure_rule.py state` · `show --tail 8`.

- **Rule state `정상`** (previous state also 정상; no firing condition). Bench `069500.KS` closed
  **109,980**, **+1.654%**, 20d-high **−0.07%**, 20d-low **+25.5%**, volume **1.481×**.
- **Target invested 95% · current invested 85.1% · band gap −9.9pp.** ⚠ The `state` call itself
  **could not fetch the account** and printed *투자비중 미상* — **the 85.1% is the 08-21 `live` row in
  `out/exposure/ledger.csv`, an intraday, unsettled mark.** Stated, not laundered.
- **Ledger n = 11.** Cumulative decomposition: **total excess −16.64pp = cash −6.46pp + selection
  −10.19pp.**
- ★ **The band gap has closed for a fifth consecutive session**: −39.4 (08-13) → −27.1 (08-14) →
  −14.0 (08-19) → −13.9 (08-20) → **−9.9pp** (08-21); invested 55.5 → 67.9 → 81.0 → 81.1 → **85.1%**.
- ⚠ **`n=11` is a sample, not a sign (`C4`).** Neither the −6.46 nor the −10.19 may be quoted as an
  established contribution; the report's own line asks for n≈20 before the question is posed.
- 🚨 **Standing alarm on every row: `ARMED (TIMEFOLIO_EXECUTE=1)`.** Analytical note only — this desk
  issues no orders and never passes `--execute`.

---

## §5 · Reconciliation — belief vs coverage. ★ The deferred check came back, and it reconciles

The 08-20 packet deferred this section with the sentence *"whether it then reconciles is the next
run's check, not a claim this one may make."* **This is that check, and it passes.**

`module_report_tags show` (default `DEGAJA_REPORT_DIR=REPORT/`): index **`2026-08-21T14:25:21` · 73
reports · 299 tickers · 13 sectors**, and `REPORT/industry_US/` carries the **08-20** files
(`SECTOR_DEEP_IT.md`, `SECTOR_ROTATION.md`, `SWEEP_READ.md`, all `Aug 20 23:34`).

★ **And the 08-20 staleness claim is corrected, not deleted (`D48`).** It said *"`REPORT/_tags.json`
is stale; the newest `industry_US` rows are dated 2026-07-21 — 30 days behind."* **That was true at
its own 22:5x clock and was repaired by its own writeback at run end.** What is now measurable is
that the sentence was **mode-specific**: run with `DEGAJA_REPORT_DIR=llm_outputs`, the index is
`llm_outputs/_tags.json` and **that** file is still **2026-07-21 (31 days)**; run in the default
`REPORT/` mode it is **today**. ⇒ **The protocol's own open decision (which mode) is not cosmetic —
it decides whether this section can run at all.** This run used **`REPORT/` mode** and says so.

### The reconciliation, per book name

| Name | Ledger reports | Belief carried in §1? | Reconciled? |
|---|---|---|---|
| `MPC` 28 · `PSX` 25 · `AVGO` 27 · `NVDA` 34 · `NUE` 12 · `RTX` 15 · `ANET` 24 · `HPE` 17 | yes | ✅ belief and coverage agree |
| `ETN` **8** · `NDAQ` **7** | yes (ETN via `S99`, NDAQ via the 08-13 miss row) | ✅ thin but present |
| **`MET`** | **0 — "no report covers it"** | **no belief carried either** | 🚨 **but the zero is NOT a gap — see below** |
| **`T`** | **0 — "no report covers it"** | yes (9.74% orphan) | 🚨 **the zero is NOT a gap — see below** |

🚨 **`M152` replicates exactly, and this time it lands on a held name.** `module_report_tags/_extract.py`'s
`_US_STOP` guard (single letters ∪ `_CHAIN_AMBIG` ∪ report abbreviations) blocks **28 real tickers in
`us_top300`**: `A · AIG · ALL · C · CAT · CB · COST · D · F · FAST · GS · ICE · KR · LOW · MA · MET ·
MS · NOW · O · ON · PEG · PM · Q · SO · T · TT · V · WELL`. **`MET` and `T` are both on it.** ⇒
**their zeros mean `unindexable`, not `uncovered`, and no stage may read them as coverage gaps.**
**Two of the eleven book names cannot be reconciled by this instrument at all, by construction.**
The guard itself is sensible; **the silence is the defect** — a blocked ticker should report
`unindexable`, not `0`.

★ **Positive form for the writeback**: with `MET` and `T` set aside as unindexable, **every remaining
book name has both a carried belief and ledger coverage, and no name carries coverage without a
belief.** The reconciliation is clean on the 9 names where it can run.

---

## §6 · Catalyst injection and the ≤48h binary rule

`catalyst_calendar.py --days 10` (saved to `llm_outputs/2026-08-21/CATALYST_WATCH.json`) —
**4 binaries in window**.

| Window | Event | Axis | Status |
|---|---|---|---|
| **D-5** | **`NVDA` earnings 2026-08-26** | earnings | 🔀binary — bracketed by `S79` (name), `S81` (readthrough), `S103` (cycle, **bands still hand-set**) |
| **D-7** | **July PCE 2026-08-28** | inflation | 🔀binary `[bea~est]` — **now bracketed by `S104`** (registered 08-20), settle 08-31 |
| **D-10** | **`FRO` earnings 2026-08-31** | earnings | 🔀binary — **NEW on the calendar this run.** `FRO` is a crude-tanker name, i.e. it sits on the **same Hormuz axis** as `S74`/`S84`/`S92`/`S95`. **No bracket is keyed to it.** Flagged for PREMORTEM |
| **D-10** | MSCI quarterly review 2026-08-31 | market | `[derived≈]` structural — no bracket, and none is obviously needed |
| undated | Iran "Strait of Hormuz open" statement | oil | 🔀binary — **still undated for the 20th run** |

⇒ **No binary lands ≤48h from this run.** The protocol's mandatory both-sides bracket rule
**does not trigger today**, and this line exists so an empty `ACTION_TICKETS.md` cannot be confused
with a tool that could not emit one (**`D294`**: `action_bracket.py`'s `earnings` axis holds
placeholder prose and can never produce a ticket).

⚠ **`D288-KR` reproduces on the US calendar for a second run**: the calendar still carries the
**undated** Hormuz row and still could not add the **FOMC minutes of 08-19** — the single dated macro
binary of the last window, and the event that VOIDed `S98`. **It can neither add a known date nor
remove an expired row.** ★ It *did* add `FRO` this run, which is the first new dated row it has
produced in three runs — recorded as the positive half.

---

## §7 · The cross-market check, carried and re-stated — `vol_surge` does NOT transfer

No new IC accrual is claimed by this stage. The 08-20 measurement stands and **binds every downstream
citation**:

| Axis · horizon | market | n_eff | mean IC | t(NW) | verdict |
|---|---|---:|---:|---:|---|
| `vol_surge` h=1 | **KR** | 27.0 → **33.0** (08-21 KR run) | −0.0479 → **−0.0492** | −3.30 → **−3.92** | ★ clears Bonferroni, **strengthened** |
| **`vol_surge` h=1** | **US** | 20.0 | **+0.0253** | **+1.49** | **indistinguishable — and the sign is POSITIVE** |
| **`rs60` h=1** | **US** | 20.0 | **−0.0843** | **−3.00** | ★ the only US cell clearing Bonferroni — **and it is negative** |

⇒ **Two constraints, stated positively.**
1. **`D290-KR` must not be imported into this desk's gate reasoning** (`W1`). The US gate question is
   **open, not answered.** Every `vol_surge` citation downstream names its market.
2. **`rs60` at h=1 has a negative IC in this window**, and `rs60` is the desk's own ranking axis
   inside `flow_score`. **`MPC` (+42.8), `PSX` (+36.4), `VLO` (+39.8), `HPE` (+37.4) and `RTX`
   (+17.0) are all carried on RS60 arguments.** ⚠ The window is the **August drawdown-and-rebound
   tape** and the regime label is mandatory; one significant cell of 15 is **a clock, not a verdict**.
   Handed to DEEP as a question, exactly as last run handed it.

---

## §8 · RESEARCH rules loaded as binding constraints — which group binds which stage

Loaded from `handoff/RESEARCH.md` (Part A triggers · Part B lenses · Part C dig list). **Grouped by
the moment they fire, not summarized.**

| Group | Fires when | IDs | Binds, this run |
|---|---|---|---|
| **C** | you cite a number | C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · C5 arbitrary choice | **MACRO** and every stage. ★ **C4 is live on three objects today**: exposure `n=11`, US `vol_surge` `t +1.49`, and the `S100` basket's 13.6pp intra-basket dispersion |
| **S** | you make a statistical claim | S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · S5 short samples · S6 future labels | **any stage citing a test** — §7's IC table, every `D93` band, and the 15 pre-settle readings in §2(b), which are **one observation each** |
| **D** | you read data | D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | **SWEEP · ALPHA · L2 indicators · L2 money_trail**. ★ **D6 is stamped on `PSX` today** (OBV 매집 against a fresh 🔴 FINRA z +1.95) and on the three defense names (`NOC` +2.43, `LMT` +1.76, `LHX` +1.35 against OBV 매집) |
| **W** | you write a conclusion | W1 cross-market transfer · W2 inherited lead/lag · W3 real≠profitable · W4 name the customers · W5 sub-sector dispersion · W6 reader's-market spine | **DEEP · BET · ROTATION**. ★ **W1 is again the run's headline constraint** (§7, `R80`/`R84`, and the 3 KR ledger rows handed back in §3). ★ **W4 is unmet on `RTX` for 204 days.** ★ **W5 fires on `S100`** — an EW basket averaged a +3.784/−9.861 split |
| **L** | lenses, not triggers | L1 second derivative · L2 peak-margin trap · L3 branch information content | **DEEP · PREMORTEM**. ★ **L2 is the live constraint on the refiners.** ★ **L3 fired twice yesterday as registered** (`S83` C, `S98` designed-to-void) and is the origin of `D300-KR` |

**Rules added 08-19/08-20 that bind from this run on:** **`T22`** (name the book unit in the same
sentence — **paper 11 US + 2 KR vs real 12**; this packet does so throughout) · **`T23`** (a term
burst must be body-read **and** sat next to `HY OAS`/`NFCI`) · **`T24`** (print the denominator next
to any "quiet/fading" tag) · **`T25`** (re-print a rejection class's own ledger score beside the
rejection).

---

## §9 · Dig list ranked for today — candidate DEEP assignments

| Rank | Dig | Why it is today's | Owner |
|---|---|---|---|
| **1** | **`D290` / `R81`** — `flow_tag` must take the run-level axis set | `vel_axis=false` for the **9th** consecutive run. Until fixed, the board's 3 greens (`MSTR` `TGT` `MRVL`) are unusable **as tags** and the shortlist is not a quality signal | code fix = human (P5); this run works around it |
| **2** | **🆕 `S99`'s pre-settle branch A** — `ETN` moved with the AI-compute basket, same sign, both gates cleared with a session to run | If it settles A, **the book's AI concentration is 5 of 12, not 4 of 12**, and the Industrials OW−'s diversifying leg is not one. **G4 has now failed 12 consecutive runs on exactly this grouping question** (250d splits `ANET`↔`ETN`; 500d/750d merge them) | ROTATION · DEEP-INDU · the D+1 scorer |
| **3** | **🆕 The defense short axis turned as a group and nothing explains it** | `NOC` z **+2.43** · `LMT` **+1.76** · `LHX` **+1.35** on the same settled close, against **OBV 매집 at all three**. `D6` says the B-grade axis outranks the C-grade one. `S97` settles 08-21 already inside branch A | DEEP-INDU candidate |
| **4** | **`D300-KR`, handed back to this desk as owner** — a bracket whose anti-signal fires almost surely is designed to void | `S98` VOIDed on a clause an 8-day US window essentially always satisfies, and the mechanism it assumed was already refuted by `S102`'s own regression. **Registration should require a hit-probability line on the anti-signal, the way `D93` already requires a baseline on the threshold** | PREMORTEM (registration discipline) |
| **5** | **`D295`** — `S103`'s bands are still hand-set, **second consecutive run** | `NVDA` is **D-5**. The 08-21 chain has now rolled, so the re-derivation is possible today and was not possible on 08-19 | **ALPHA, today** |
| **6** | **`D250` / `M731`** — `cycle_registry.json` has no row for optical/interconnect | The GAP check **cannot fire** on that cycle at all, and the three optical names stopped agreeing this run (`LITE` 매집 vs `CIEN` 🔴 rs60 −36.4) | registry maintenance = human (P5) |
| **7** | **🆕 A revival condition may not name a series the desk cannot pull** | `CF`'s leg 2 reads *"average natural-gas cost falls below 4.00/MMBtu"* — that is the **company's realized cost**, which has no reachable series; read on the spot proxy (`NG=F` **$2.803**) it was **already true at registration** ⇒ a `D122` zero-information leg either way. Same family as `D279-KR` and `D299-KR` | condition-writing rule candidate |
| **8** | **`M152` now blocks a HELD name** — `MET` and `T` are both `_US_STOP`-unindexable | 28 real tickers return `0` instead of `unindexable`. **2 of the 11 book names cannot be reconciled by the ledger at all** (§5) | scripts owner |
| **9** | **`us_top300.csv` staleness blocks two ledger rows, not just weighting** | 37 days. `SPCX` and now **`FSLR`** both have entry conditions that **cannot resolve on any market outcome** — and `FSLR`'s substitute leg has **zero in-universe candidates** to draw from | human (P5) |
| **10** | **`T`'s missing label** | 9.74% of the real book's invested, revived on the ledger this run, and still **zero artifacts**. `S107` (09-03) is its first bracket in three runs | DEEP-COMM candidate |

⚠ **`D10` carried forward, not re-discovered**: the news-body boilerplate defect needs human approval
**and a server console** (FTS writes are server-only, P6).
⚠ **`D9` remains half-closed**: measured units are surfaced (`RISK_UNITS.json`), but whether a
label/unit mismatch **blocks** or only **warns** is a human call. **`S99` is about to make that
question expensive.**

---

## §10 · Staleness flags

| Object | `asof` | Flag |
|---|---|---|
| `data/us_universe/us_top300.csv` | **2026-07-15** | 🚨 **37 days** (limit ≤8). Every `wflow` this run is weighted on 37-day-old caps, and it blocks two ledger rows (§9) |
| `REPORT/_tags.json` (default mode) | **2026-08-21 14:25** | ✅ **fresh — §5 reconciliation available for the first time in two runs** |
| `llm_outputs/_tags.json` (alternate mode) | **2026-07-21** | 🚨 31 days — the mode this desk used on 08-20; the open decision is load-bearing |
| §3a per-name rows | 2026-08-18/19 settle | ⚠ **one to two sessions behind today's terminal bar**, and one of them (`NUE`'s FINRA line) was measured **false** today (§11) |
| §3b KR rows | 2026-07-25 ~ 07-29 | ⚠ **~4 weeks** — read-only for this desk, **not cited as evidence anywhere in this packet** |
| `data/estimates` snapshot history | 13 files / 31 days | 🚨 G6 — accrual **2.4× slower** than ideal; **cannot be back-filled**. ★ It did fire today, third straight day |
| `[FRED]` yield series | **2026-08-19** | ⚠ **one session behind the equity tape.** `S102`'s observable is not yet readable; `breakeven_10y`, `rrp` and `sofr` do print through 08-20 |
| `dxy` (`DTWEXBGS`) | **2026-08-14** | ⚠ **7 days** — the series that has slipped repeatedly. Not cited in this packet |
| `cycle_registry.json` | — | 🚨 no row for optical/interconnect or custom AI silicon ⇒ **unmeasurable, not zero** |

**Cleared suspensions converted into dig instructions:** the `REPORT/_tags.json` suspension cleared
and became §5, which is the section it was blocking. **`D295`'s option-chain suspension has also
cleared** (the 08-21 expiry has rolled) and becomes ALPHA's obligation today (§9 rank 5).

---

## §11 · §4c — what this run asserted, inherited, and then refuted (`D48`)

**Two, and both are corrections of *carried* claims by this run's own measurement. Neither earlier
sentence is edited; both are left in place and appended to.**

1. **`NUE`'s carried FINRA line is false as of today.** The 08-20 packet carried *"the sheet's only 🔴
   FINRA axis (short-vol z **+1.99**)"* with the kill *"z > +1.5 for 5 sessions with OBV still 매집."*
   Measured on the 08-20 settled close: **z −2.33 = 🟢 short covering**, short% 35.8 against a 20-day
   base of 50.6, 5v5 **+1.2▲**. **The kill did not fire; the axis reversed.** ⚠ **This is exactly the
   `D298` class the previous run registered** — a state variable living in prose with nothing that
   re-computes it — and it is the **second** instance found in two runs. It is marked **stale and
   updated by measurement, not retracted** (the `M168` convention).
2. **The 08-20 §5 conclusion *"no reconciliation is possible"* no longer holds, and the reason is a
   mode, not a clock.** Its staleness measurement was correct at its own clock; the **inference** that
   the ledger could not reconcile was specific to `DEGAJA_REPORT_DIR=llm_outputs`. In the default
   `REPORT/` mode the index is **today's**. §5 runs.

★ **And one thing this stage caught in ITSELF, recorded rather than smoothed.** The pre-settle table
in §2(b) was first drafted as a *scoring* table because four rows sit past a branch line. **They are
readings on 4 of 5 sessions.** `S86`'s own registration discloses **sd 8.998 — the widest estimator
on the board** — so a −6.400 with one session to run is **not** a settled B; `S89`'s sd is 6.056 and
its anti-signal is **2.1pp from firing on the live gold quote.** The table was rewritten with
"pre-settle" in its header and the thresholds printed beside every reading, so no downstream stage
can read a distance-to-branch as a verdict.

⚠ **Zero *analytical* self-refutations would be worth suspicion; this run's controls were real.**
`CF` was decided by pulling a **19-year primary margin series** rather than trusting the flow tag;
`LYB` by pulling a **15-year** one and finding the current reading is the series **minimum**; `XLY`
by measuring **both** legs on the **same settled close** the condition names rather than the nearest
available one; and `MET`/`T`'s ledger zeros by **reading `_extract.py`** rather than reporting the
number the tool printed.

---

## §12 · Handoff to MACRO (stage 1)

1. **Frame ends 2026-08-20.** No 08-21 price. Nothing re-pulled after 22:30 KST may be mixed with
   sweep statistics. `[FRED]` yields end **08-19** — one session behind the tape; say so on every
   rate sentence.
2. **The Δ is one session (08-19 → 08-20).** Say "one session"; do not say "recent". 294/299 scores
   moved, median |Δ| 0.067.
3. **No tag is evidence** (`R81`). **No Δ-only verdict** (`D293`). **No Communication Services `wflow`
   sign** (G3 — `GOOGL` owns 38.3%; use `eqflow` **+0.151** or `breadth` **0.00**, and note those two
   disagree). **No news velocity, no theme freshness, no "quiet"** (G1).
4. **The board is broadly negative and narrowly positive.** Universe `wflow` **−0.105**, **7 green :
   68 red of 299**. Only four sectors print a positive `wflow` — **Energy +0.169 · Health Care +0.150
   · Communication Services +0.090 (flipper) · Consumer Staples +0.050** — against **Utilities
   −0.647 · Real Estate −0.335 · IT −0.279 · Industrials −0.247**. MACRO owns whether that is a
   duration story, a rate story, or a breadth story; **`S102` says the four duration legs have no
   measurable rate beta and `XLE` has +0.1534 pp/bp**, so the desk's only rate-exposed tilt is its
   overweight, with a positive sign.
5. **`S82` FIRED-A: Health Care decoupled UPWARD out of the duration complex.** It is not the fourth
   leg. MACRO's transmission matrix owns this.
6. **`S98` VOIDed on a clause that was designed to void** (`D300-KR`). MACRO should not re-use the
   four-leg sign test as an instrument; the successor changes it from a SIGN to a cross-sectional
   DISPERSION.
7. **Four rows sit past a branch line with one session to run, three of them against a live position**
   (`S87` A · `S97` A · `S99` A). **They are readings, not scores.** PREMORTEM and ROTATION may use
   them as questions; no stage may cite them as settled.
8. **Two anti-signals must be checked before tomorrow's scoring** — `S89` (gold ±8%, currently
   +5.95% on the live quote) and `S95` (refinery outage / PADD3 hurricane / OPEC+ decision,
   **unmeasured this run**).
9. **New on the calendar: `FRO` earnings 08-31**, on the same Hormuz axis as `S74`/`S84`/`S92`/`S95`
   and unbracketed. PREMORTEM should own it alongside July PCE (already bracketed by `S104`).
10. **`vol_surge` carries opposite signs in the two markets' IC ledgers; `rs60` h=1 has a negative US
    IC.** Every citation names its market (§7).
11. **Exposure: `정상`, invested 85.1% (live mark), band gap −9.9pp, n=11 and therefore unquotable as
    a contribution.** BET/ALPHA inherit this as size *context* — not as a size.

> ⚠ No position sizing, no buy/sell language appears anywhere above (P4). This stage transports
> analysis; the carry writeback to `handoff/*.md` happens at run end, append-only for retractions.
