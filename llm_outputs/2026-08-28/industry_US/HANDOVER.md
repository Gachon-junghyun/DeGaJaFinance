# HANDOVER — industry_US · 2026-08-28 (Stage 2 / L1·HANDOVER)

> Run fires **09:15 ET Fri 2026-08-28 = 22:15 KST**, i.e. **US pre-market**. That single fact
> determines most of §2: rows whose observable is the **08-28 settled close have not arrived**,
> and rows whose observable was the **08-27 settled close now have**.
> P4 — this stage transports analysis. No sizing, no buy/sell language anywhere below.

---

## 0 · Instrument health inherited — read BEFORE any number is trusted

`llm_outputs/2026-08-28/industry_US/preflight/PREFLIGHT.md` **was run** (Stage −1, this run).
**4 FAIL / 3 PASS.** The rights it removes bind every stage after this one:

| Gate | Verdict | What this run may NOT do |
|---|---|---|
| G1 news axis (`vel_coverage` **16.72%**, 50/299; probes alive: NVDA 5161 / LLY 180 / NUE 26 / MPC 23) | **FAIL** | No news-velocity or theme-freshness citation, anywhere. No "quiet"/"no news" verdict on any name or sector. `BET_SHEET §B` freshness tags read `UNMEASURED (G1 FAIL)`. **And the partial velocity subset may not be used cross-sectionally** — its coverage is `us_top300` **ranks 1–50, contiguous** ⇒ a mega-cap-only sample |
| G2 scale continuity (`n_axes`=3 on 7 snapshots) | **PASS** | conditional: SWEEP re-reads `§scoring.n_axes` **and `§asof`** before any Δflow subtraction — 08-22/23/24 all carry a **stale `asof: 2026-08-21`** |
| G3 sector-sign ownership (flippers **2 of 11**: Health Care/`LLY`, Energy/`XOM`) | **PASS** | **HLTH and ENRG may not be promoted or demoted on `wflow`** (ROTATION §2). Rank them on `eqflow`/`breadth`, and say so inline |
| G4 risk-unit stability (250d **11** / 500d **10** / 750d **10**; groupings differ) | **FAIL** | No bare concentration number. Every unit count carries its `--days` on the same line |
| G5 universe covers holdings (0 outside; file **44 days** old) | **FAIL** | `wflow` is not a *current* weighting. On `wflow`/`eqflow` disagreement, **`eqflow` is the citable one** |
| G6 accrual (**19 files / 38 days = 0.50/day = 2.0× slow**) | **FAIL** | No IC-backed sizing language. Any fraction is "mechanical 1/4 — IC not yet estimable" |
| G7 tool liveness (26 exit-0; `module_chart` non-standard, verified live) | **PASS** | — |

★ **The asymmetry G3 creates is the run's largest available instrument error**: Health Care and
Energy carry the **only two positive `eqflow` readings in the 11-sector table** (+0.086, +0.042)
while both print a negative `wflow`. A naive weighted read ranks them mid-table-negative.

---

## 1 · Inherited standing view — and a **process failure to name first**

### 1a 🚨 The 2026-08-27 `industry_US` run did not write its analytical carry back

Measured, not inferred: `grep "2026-08-27" handoff/STANDING_VIEW_US.md` → **0 hits**;
file mtime **2026-08-26 23:31**. The 08-27 run **did** write its scenario side
(`SCENARIOS_US.md` mtime 08-27 22:56, and its scoring block is in `SCENARIOS.md`), and it **did**
produce its full report set (`BET_SHEET.md` 23:14, `MACRO_REPORT.md` 23:16 = the DRIFT addendum).
**What is missing is §2 (the measured chain) and §3a (the per-name registry) for 08-27.**

⇒ **The newest US per-name carry this run inherits is `asof` 2026-08-26 — two days old, not one.**
Any 08-27 measurement lives only inside `llm_outputs/2026-08-27/industry_US/*.md`, which is a
report directory, not the carry. **Registered as a dig this run (`D394`, §8).** Not repaired here.

### 1b Regime call (shared spine §1, carried unchanged)

> **Memory is a price-cycle industry in rate-of-change deceleration while its level stays tight.**
> `[inferred]` — the equity tracks the **second derivative** of price, not the level, which is why
> "shortage persists" and "stocks struggle" are both true.

⚠ Carried with its tag intact. **`[inferred]` — it may not be cited as evidence** for any new
proposition this run. It frames; it does not prove.

### 1c Per-name carry, `asof` 2026-08-26 (tags preserved; ⚠ = 2 days stale, see §1a)

| Name | Carried state | Tag | Stale? |
|---|---|---|---|
| `MPC`·`PSX`·`VLO` | Refining **margin, not crude beta**: `exc20` +12.57/+11.70/+10.51, `exc60` +41.41/+33.45/+37.80, all OBV 매집, the three **smallest** negative flow deltas in a sector where E&P ran −0.52…−0.57 (`M952`) | `[measured]` | ⚠ 2d — **and §2 kills two of its instruments today** |
| `XOM` (ENRG top1) | The sweep's only Energy red; flow −0.590, OBV 분산, **Δ −0.424 = board's worst**. In `reject_ledger` (`K.본문반증`), recheck 09-09 | `[measured]` | ⚠ 2d |
| `NVDA` (held) | The epicenter, printed 08-26 AMC. Δ +0.409 = largest positive of 11 holdings | `[measured]` | ✅ **superseded by §2 — the print settled** |
| `AVGO` (held) | Worst `rs60` on the book (−24.1), `exc5` −5.920 = 9.9th %ile, FINRA **z −2.17 / 5v5 −10.4▼**. Prints **2026-09-02**; `S127` armed (settle 09-08) | `[measured]` | ⚠ 2d |
| `ANET` (held) | OBV 매집, `rs20 +17.4 / rs60 +12.3` **against FINRA z +2.06 = board's highest short pressure**. Genuine two-sided read, no stamp | `[measured]` | ⚠ 2d |
| `MRVL` | The only confirmed-early hand-off whose **denominator is rising** (+13.2% NY). Printed **08-27**; `S116` settles at tonight's close | `[measured]` | ⚠ 2d |
| `COIN` | 🚨 Board's #1 flow (+0.978) on the board's **worst revision book** (CY +1.01 → −2.06 = −303.5%). **Carried ONLY with its denominator attached** — BET may not cite the flow score without the revision book on the same line | `[measured]` | ⚠ 2d |
| `HOOD` | The clean version of the same node: `exc5/20/60` +22.66/+17.46/+17.62, positive revisions on all four | `[measured]` | ⚠ 2d |
| `MSTR` | Not a runner, not cheap — 2.52× forward off a **−115.3%** CY consensus. Rejected (`H.밸류소진`), recheck 09-16 | `[measured]` | ⚠ 2d |
| `MRK` | Health Care's only 🟢 — **and it trades ABOVE its mean target** (upside −4.4%) ⇒ `L2` on the sector's only green | `[measured]` | ⚠ 2d |
| `MET`·`NDAQ` (held) | Both in `S128`'s **decay** basket (`rs20<0 ∧ rs60>0`); `S128` settles 09-09 | `[measured]` | ⚠ 2d |
| `RTX` (held) | 🔴분산, `delta −0.629` = book's largest negative. Its cycle has **no threshold set**; `W4` unpaid **209 days** | `[measured]` | ⚠ 2d |
| `NUE` (held) | Two instruments, neither a turn: screener "leader pullback" at +22% over 200DMA vs `module_chart` NEUTRAL/CHOP, OBV 분배 −65%, RSI 22.4 | `[measured]` | ⚠ 2d |
| `EQIX`·`DLR`·`IRM` | The carried data-centre grouping is **not observed** (`M953`): `EQIX`/`DLR` carry RE's two largest positive deltas, `IRM` is negative on all three windows. ⚠ n=1 frame | `[measured]` | ⚠ 2d |
| optical (`LITE`·`COHR`) | 🚨 `cycle_registry.json` still has **no optical row, 12th run** (`D250`) ⇒ exposure **unmeasurable, not zero** | `[measured]` | ⚠ 2d |

### 1d Retracted ledger (§5) — read BEFORE forming today's view, per the stage rule

Read tail-first. Two entries bind this run directly:

- **`R103`** — *"The news axis fails because the 300-query SWEEP overloads the tunnel"* → **RETRACTED
  2026-08-26** by `M947` (contiguous rank prefix). This run's PREFLIGHT reproduced the prefix for a
  **4th** time and **wrote it up as a reproduction, not a discovery** — which is the specific error
  `D379` says PREFLIGHT keeps making. ✅ **`D379`'s failure mode did NOT recur this run.**
- **`R89`** — *"the refiners pay WITHOUT the barrel"* (the separation claim) → **RETRACTED 2026-08-21**
  when its own registered control failed (`BZ=F` 5d +7.71% vs a ≤+2.0% leg). `P83` was registered as
  **the replacement instrument, not a replacement conclusion.** 🚨 **§2 settles `P83` and it fires B**
  — see §2c. Any refining language this run must be checked against this pair before it is written.

### 1e Open contradictions (§6) — carried, not resolved

Carried deliberately and **not resolved by picking a side** this run: (i) the label-vs-measured risk
unit question (`D9`, human call: block or warn); (ii) `MAX_THEME_PCT` counting as 2 what residual
correlation measures as 1 — reproduced in **all three** G4 windows today.

---

## 2 · Scenarios settled this run

> Scored **only** against the pre-registered observable and threshold (`D242`). No band re-derived,
> no threshold improvised. Prices: `yfinance`, `auto_adjust=False`, settled closes.
> ★ **`D393-KR` applied first**: the tail of `SCENARIOS.md`'s master log was read **before** writing
> anything here. That read is why `S115`·`S117`·`P77`·`P90` are **not** re-scored below — the
> `industry_kr` run of this morning (pre-open KST) already settled them.

### 2a · `S79` — NVDA 08-26 print · **LEG 1 = `FIRED-A` · LEG 2 = `U-MIXED`**

**Leg 1** (frozen: NVDA 1-session excess vs `SPY` on the first settled session after the AMC print
= 2026-08-27). Measured **NVDA 209.66 → 227.98 = +8.738%**, `SPY` +0.655% ⇒ **excess +8.083pp**.
Branch A is **≥ +5.0pp** ⇒ **A fires, clearing by 3.08pp**, and it sits outside the **±6.11%**
implied move recorded at registration. Meaning, as registered: *the #1 cycle's epicenter re-rates;
`IT N` was too low, and ROTATION's repeated decline to move IT was right on dispersion but wrong on
the epicenter.*
⚠ **`S115` fired A on the same session against a ≥ +7.0% line.** `S79` Leg 1 and `S115` are **one
event read twice**, not two confirmations — stated here so no downstream stage double-counts it.

**Leg 2** (frozen: same session, AVGO and TSM 1-session excess vs `SPY`) — ★ **the leg that exists
to settle what PREFLIGHT `G4` cannot**:

| | measured excess | U-ONE needs | U-SPLIT needs |
|---|---|---|---|
| `NVDA` | **+8.083pp** | \|·\| ≥ 5.0 ✅ | \|·\| ≥ 5.0 ✅ |
| `AVGO` | **+3.830pp** | same sign ✅ ∧ \|·\| ≥ 2.0 ✅ | \|·\| < 2.0 ❌ |
| `TSM` | **+1.645pp** | same sign ✅ ∧ \|·\| ≥ 2.0 **❌ (short by 0.355pp)** | \|·\| < 2.0 ✅ |

⇒ **Neither U-ONE nor U-SPLIT. `U-MIXED` fires** — *"one peer moves, the other does not."*
★ The registration called U-MIXED **"the most informative outcome, because it retires a framing the
desk uses for its concentration guard."* It is now on the record: **on the one day of the year when
the answer was observable, neither the 250d split nor the 500/750d merge described the tape.**
⇒ **G4's cross-window disagreement is not resolved by observation either** — the honest state is
that the desk has **no validated grouping** for event risk, and the removed right (§0, G4) stands
for a reason stronger than instrument instability.
⚠ **Margin disclosed**: TSM missed the bar by **0.355pp on a 2.0pp line**. A verdict that turns on
0.36pp is reported as such, not as a clean result.

### 2b · `S81` — the readthrough basket, NVDA **excluded** · **`C`, but AMBIGUOUS by its own anti-signal**

Frozen: **EW{`AVGO`,`ANET`,`HPE`} 2-session cumulative excess vs `SPY`, 08-25 close → 08-27 close.**
Measured: `AVGO` +4.149 · `ANET` +5.316 · `HPE` +1.815 ⇒ **EW +3.760%**, `SPY` +0.678% ⇒
**excess +3.082pp**. Branch A **≥ +3.66** (short by **0.578pp**); branch B **≤ −2.86** ⇒ **inside C.**

🚨 **The anti-signal fired and it is honoured, not waved through.** Registration: *"a separate ≤48h
macro binary on 2026-08-26/27 ⇒ AMBIGUOUS, because a macro shock counterfeits a readthrough."*
**July PCE printed 2026-08-26** — inside the observable window — and it printed **hot**:
*"Hotter-Than-Expected Inflation Puts Pressure on Warsh…"* (`yahoo_finance` 08-26),
*"US Equity Indexes Decline After July PCE Inflation Rate Rises"* (`yahoo_finance` 08-26).
⇒ **Verdict recorded as `AMBIGUOUS`, with the C-side reading disclosed (+3.082pp, 0.578pp under A).**
The number is reported because suppressing it would hide how near A it came; the verdict is not
upgraded, because the pre-registration says a macro binary in-window voids the read.

### 2c · `P83` — the refiners' **successor** separator · **`FIRED-B`**

Frozen: **(`HO=F` − `RB=F`) × 42, change from the 08-20 settle of 51.131, at the 08-27 close.**
Branches A ≥ +4.0 · B ≤ −4.0 · C between.
Reproduced series (settled closes): **51.131 (08-20) → 48.170 → 41.870 → 41.618 → 39.476 →
37.569 (08-27)** ⇒ **change −13.562** ⇒ **B by 9.56 points.**

★★ **This matters more than a single row.** `P83` was registered on 2026-08-21 as *the replacement
instrument* after `R89` retracted the separation claim — the distillate−gasoline spread, chosen
because *"a pure crude move cannot widen it."* **It did not widen. It collapsed 13.6 points in five
sessions.** ⇒ **the successor separator has now failed too**, and the desk has **no surviving
instrument that separates the refining excess from the barrel.** The refining *thesis* is not
retracted by this row — the crack levels and the capacity mechanisms are separate evidence — but
**the claim of separation may not be re-asserted this run on any instrument.** Recorded for §5.
⚠ Composition disclosed: the collapse is two-sided, **not** a gasoline artifact alone —
`HO=F` 4.480 → 4.279 (**−4.5%**) and `RB=F` 3.263 → 3.384 (**+3.7%**).

### 2d · `P96` — the 3-2-1 crack 5-session rate · **`FIRED-B`** ★ and the live read had the sign backwards

Frozen: **settled 3-2-1 crack 5-session rate at the 08-27 close.** A ≤ −2.887 · B ≥ +0.468 · C between.
Reconstruction validated against the registration's own prints before use: my series returns
**−2.862 @ 08-24** and **−1.675 @ 08-25** — **byte-matching** the values `M936` registered.
Measured at the **08-27 settled close: +4.874** ⇒ **B, clearing by 4.41.**

🚨 **The 08-27 run's own `SECTOR_DEEP_ENRG` wrote *"as printed −8.584 = deep inside A"*** off a
**live intraday** 08-27 bar. **The settled bar is +4.874 — the opposite branch, 13.5 points away.**
This is `D355` (intraday bar read as settled) landing on a *registered row*, and it is the second
consecutive session it happened: `M958` had already withdrawn the 08-26 live crack figure as a
probable RBOB roll artifact. ✅ **`M958`'s withdrawal is vindicated by the settled tape** —
`RB=F` settled **3.320 (08-26) → 3.384 (08-27)**, i.e. it **rose**; the 2.9495 that produced the
"−9.34%" read never settled. (The roll shows up on **today's 08-28 live bar, `RB=F` 2.994** —
still incomplete, and therefore not used for anything.)

### 2e · `S119` — Bessent's Iran sanctions presser, D-0 · **`FIRED-C`** — ★ scored, and the reason it is scoreable is measured, not asserted

This row was **handed to `industry_US` by name** this morning by the KR run, which declined it
under `C5`: *"the row never enumerates the basket's membership"* (⇒ `D388-KR`). The refusal was
right. **Reconstructing one basket would make this desk choose the observable.**

**What this run did instead: scored it under every plausible enumeration and tested whether the
branch depends on the choice.** Frozen window 08-24 close → 08-27 close, bands **±2.60pp**,
**untouched** (`D242`).

| enumeration | basket 3-session return | excess vs `SPY` (+0.999%) | branch |
|---|---|---|---|
| (a) EW of the sweep's own 16 GICS-Energy names (identical membership in the **08-24 and 08-27** snapshots) | −0.710% | **−1.709pp** | **C** |
| (b) `RSPG` — S&P 500 **equal-weight** energy ETF | −0.363% | **−1.363pp** | **C** |
| (c) `XLE` — cap-weighted, carried as a robustness read only | −1.299% | **−2.299pp** | **C** |

⇒ **The verdict is invariant across all three. `C` fires regardless of which basket the row meant.**
The construction defect is real and `D388-KR` stands as a rule; what is *not* true is that the row
was unscoreable — **it was unscoreable by a single arbitrary pick, and scoreable by showing the pick
does not matter.** Nearest branch is B at **−2.299pp vs a −2.60pp line (0.30pp away, read (c))**;
disclosed.

**Anti-signal probed, NOT fired** (both legs checked, not assumed):
1. *Presser postponed/cancelled* — corroborated as held: `fxstreet` **08-24**, *"Gold rallies as
   Iran sanctions stoke haven demand."*
2. *A US–Iran direct-talks announcement **with a named date*** — **no such item found.** What the
   window actually contains is an **Iran–Oman** deal (`foreignpolicy`/`semafor`/`aljazeera` 08-26,
   *"Iran, Oman Agree to Temporary Strait of Hormuz Deal"*), and on the US leg the opposite:
   `aljazeera` **08-26**, *"Trump tells Al Jazeera 'not in a hurry' for Iran to return to talks"*,
   plus `wsj` **08-27**, *"Iran Talks Sputter as Trump Spurns a Return to His June Deal."*
   ⇒ **no named date ⇒ the anti-signal's condition is not met.** Recorded with its sources so a
   later run can overturn the judgement on evidence rather than re-litigate it.

★★ **The state fact this scoring surfaced is larger than the row**: a **temporary Iran–Oman Hormuz
transit deal was struck on 2026-08-26**, and `catalyst_calendar` still carries the Hormuz item as
an **undated** *"Iran 'Strait of Hormuz open' statement"*. Handed to MACRO/PREMORTEM, not resolved here.

### 2f · Named, NOT scored — every one with its reason (zero silent skips)

| id | why not scored |
|---|---|
| `S116` `S118` `S120` `S124` | **Observable is the 2026-08-28 settled close, which has not arrived** — this run fires 09:15 ET, pre-market. **NOT `EXPIRED`** (`D355` class). `S116` (`MRVL`) and `S118` (`NVDA`→memory) both hinge on tonight |
| `S111` `P67` | settle at *the first `[FRED]` close covering 2026-08-28* — cannot exist before tonight |
| `S104` | settles **08-31**. 🚨 **Construction problem recorded, not repaired**: the row is titled *"July PCE **2026-08-28**"*, and **July PCE printed 2026-08-26** (six outlets, §2b). The row's *date* is wrong even though its *settle* is later. Flagged for its owner stage; **no threshold touched** |
| `P77` `P90` `S115` `S117` | ✅ **already settled this morning by `industry_kr`** (`FIRED-A` / `FIRED-A` / `FIRED-A` / `FIRED-B`). Re-scoring them would be double-counting. Read before writing, per `D393-KR` |
| `P86` | PCE conjunct **met**; rate conjunct unreadable (`DGS2` 4.17 vs A ≤ 4.10 / B ≥ 4.32). **Stays ARMED.** ⚠ its PCE leg now inherits §2b's date discrepancy |
| `P97` | unreadable — `DTWEXBGS` still lags the joint date the row requires |
| `P81` `P85` `P87`–`P89` `S109`(`FRO`) | not yet due (09-02 and later) |
| `S8` | ⛔ unscoreable for a **30th** consecutive run — date field still `[blank]`. **Named again rather than dropped.** This is a human item and it has been one for a month |
| KR-owned rows | zero due; earliest `S67-KR` **09-04** |

---

## 3 · Both ledgers audited — symmetric, per `carryover §3b/§3c`

| ledger | total | resolved | **legacy (no revival/entry condition)** | **due today** |
|---|---|---|---|---|
| `reject_ledger` | 247 | 148 | **0** | **0** |
| `missed_ledger` | 258 | 156 | **0** | **0** |

- ⚠ **A clean `due` is not read as proof of health** (the stage says so explicitly). The evidence
  that the practice is holding is the **legacy count, and it is 0 on both ledgers for an 11th
  consecutive run** — that is the real number, not the empty `due` list.
- **Zero rows carried a second HANDOVER unresolved.** No process failure on this axis this run.
- ⚠ `missed_ledger`'s `excess` sign is **inverted** relative to `reject_ledger`. The two are not
  summed anywhere in this run.

---

## 4 · Exposure state — carried as size context for BET/ALPHA (read-only; this stage never `log`s)

`exposure_rule.py state` (settled, bench `069500.KS`): rule state **정상**, *"발화 조건 없음"*.
Target invested **95%**; `state` could not read current % (*"수익분해 불가 — NAV/투자비중이 없다"*).
`show --tail 10` **does** carry it: **invested 85.5%**, band gap **−9.5pp** (🚨밴드이탈), and the gap
has closed steadily: −39.4pp (08-13) → −27.1 → −14.0 → −9.5pp today.

**Cumulative decomposition, n=16**: total excess **−11.68pp = cash −5.94pp + selection −5.74pp.**
- ⚠ **n=16.** The tool's own line: *"a month gets n≈20, and only then may the sign be asked"* (`C4`).
  This is carried as **accumulation, not as an edge and not as a verdict on selection.**
- ⚠ Not a cold start (43 ledger rows), so the `2026-07-31` cold-start caveat does not apply.
- 🚨 **Standing alarm, unchanged and not this desk's to clear**: `ARMED (TIMEFOLIO_EXECUTE=1)` on
  every row. Reported because it is on the instrument's own output; **no action taken** (P4/P6).
- ⚠ Every ledger row is tagged **미정착봉 (live intraday)**. Given §2d — where a live bar put a
  registered row on the wrong branch by 13.5 points — that tag is carried forward as a live caveat,
  not as boilerplate.

---

## 5 · Signal scoreboard (`ic_ledger score`) — ★ the standing item CHANGED and the change is constrained

**`vol_surge` h=1 now reads `n=39 · n_eff=39.0 · mean IC −0.0444 · t(NW) −3.84 · 26% positive ·
필요n 11` — and the tool grades it `★유의(다중비교 통과)`, i.e. it clears Bonferroni |t| > 2.8.**
`vol_surge` h=5 agrees in sign (−0.0380, t −2.18, `유의(단독기준)`); h=10 agrees but is
`n_eff 2.6` ⇒ **unquotable**.

**What this does and does not license:**
- ✅ It is the **first cell on this board to clear the multiple-comparison bar** at a quotable
  `n_eff`, and it agrees independently with **`M224`**. The standing note — *"`sector_flow`'s 🟢
  verdict still weights `vol_surge` positively while the measured sign is negative"* — is now
  backed by a Bonferroni-passing cell rather than by a single-test one.
- 🚫 **It does NOT license flipping the gate this run.** Two reasons, both binding: (i) **P4** — a
  gate change is a code/human decision, not a research-run action; (ii) ★ **`W1`** — **this ledger
  is `KR`-labelled** (`# IC LEDGER — KR`). Importing a KR-measured axis sign into the **US** desk is
  precisely the cross-market transfer `W1` forbids, and the protocol's own N=4 note says a US change
  *"needs its own measurement first."* ⇒ carried as **a KR-measured result with a US implication
  that is unmeasured**, and the US-side measurement is registered as a dig (`D395`, §8).
- ⚠ **14 of 21 cells remain unquotable** (`n_eff < 4`). Not quoted anywhere in this run.
- ⚠ Regime label required and stated: the window spans the **08-13 → 08-28 drawdown-and-rebound**
  band (bench −1.9% today, +9.27% off its 20-day low). A crash-window IC does not generalise.

---

## 6 · Reconciliation — belief (`handoff/`) vs coverage (`module_report_tags show`)

| finding | detail |
|---|---|
| **Coverage without belief** | `REPORT/industry_US/` carries **`SECTOR_DEEP_COMM`**, **`SECTOR_DEEP_IT`**, **`SECTOR_DEEP_MATR`**, **`SECTOR_DEEP_UTIL`**, **`SECTOR_DEEP_FIN`**, **`SECTOR_DEEP_RE`** — six sectors with a fresh DEEP and **no standing per-name thesis** in §3a beyond one or two names each. Candidate DEEP material for ROTATION |
| **Belief without coverage** | `LITE`/`COHR` (optical) carry a standing §3a row and **`cycle_registry.json` has no optical row for a 12th run** (`D250`) ⇒ the belief is un-instrumented, not merely uncovered |
| **Resolved-but-live** | none surfaced this run |
| **Stale index** | `SECTOR_DEEP_SEMI.md` in `REPORT/` is dated **2026-07-15** (44 days) while the AI-compute complex is the book's largest concentration — and §2a just measured that complex's grouping as **U-MIXED**. Flagged; the ledger records coverage, and this coverage is stale |

---

## 7 · Stale flags and cleared suspensions

- **Every §3a US row is `asof` 2026-08-26 = 2 days** (§1a). Horizon for a daily desk is 1 day ⇒
  **all flagged stale**, and the cause is a missing writeback, not an aging market.
- `us_top300.csv` **44 days** (G5) — the single defect behind both the stale weights **and** the
  news-coverage frontier.
- **Cleared suspension → dig, not silent trust**: `D295` (re-derive `S127`'s `AVGO` bands from the
  options market once the straddle chain rolls past the 09-02 print) became actionable on the
  **08-28** roll. **It is a dig for this run's PREMORTEM (§8), not an assumption.**
- ⚠ **Do not retroactively clean the 08-22/23/24 stale-`asof` stretch.** Those snapshots stay
  unreadable for Δflow; the window is not repaired by knowing why it broke.

---

## 8 · Dig list, ranked for today (Part C + what this run adds)

| rank | dig | why today |
|---|---|---|
| 1 | **`D394` (new, this run)** — *a run's report set is not its carry.* The 08-27 US run wrote `BET_SHEET`, `MACRO_REPORT` and its scenario block but **no §2/§3a writeback**, so the desk's per-name view silently aged 2 days. **Positive form**: the writeback pass verifies `grep "<today>" handoff/STANDING_VIEW_US.md` returns ≥1 hit before the run is called complete | it already cost this run its freshest carry |
| 2 | **`D295`** — re-derive `S127`'s `AVGO` bands from a straddle that spans the 09-02 print | **the chain rolled today**; unmet for 3 runs |
| 3 | **`D395` (new, this run)** — the `vol_surge` result is **KR-measured**; build the US-side `ic_ledger` cell before any US gate change is even discussed (`W1`) | the KR cell cleared Bonferroni today (§5) |
| 4 | **`D250`** — no optical row in `cycle_registry.json`, **12th run** ⇒ optical exposure unmeasurable | two §3a names ride it |
| 5 | **`D355`** — live-vs-settled bar confusion, now demonstrated **on a registered row** (§2d, −8.584 live vs +4.874 settled) | second consecutive session |
| 6 | **`D379`** — PREFLIGHT's DIFF column reads yesterday's *frozen* file, so a late retraction is invisible next morning. **Prescription unchanged**: PREFLIGHT reads `STANDING_VIEW.md §5` before building the column | ✅ did **not** recur today, but the fix is still unapplied |
| 7 | **`D9`** (block or warn on unit/label mismatch) · **`D10`** (news-body boilerplate; needs a server console, `P6`) | carried untouched — human items |

---

## 9 · RESEARCH triggers loaded as **binding constraints**, and what they bind

| group | fires when | binds, this run |
|---|---|---|
| **C** — C1 baseline · C2 both halves · C3 unknown column · C4 "indistinguishable" · **C5 arbitrary choice** | you cite a number | **MACRO, every stage.** `C5` is live in §2e (basket enumeration) and `C4` in §4 (n=16 decomposition) |
| **S** — S1 date-fold · S2 diagnose the null · S3 power first · S4 in-sample≠done · **S5 short samples** · S6 future labels | a statistical claim | any stage citing a test. `S5` binds G4's 250d window and `M953`'s n=1 frame |
| **D** — D1 second venue · D2 proxy sign · D3 signed vs unsigned · D4 regime contamination · D5 cross-provider · **D6 signal grade (OBV is C)** | you read data | **SWEEP · ALPHA · L2 indicators.** `D6` binds every OBV 매집/분산 word downstream |
| **W** — **W1 cross-market transfer** · W2 inherited lead/lag · W3 real≠profitable · **W4 name the customers** · W5 sub-sector dispersion · W6 reader's-market spine | you write a conclusion | **DEEP · BET · ROTATION.** `W1` is the binding constraint on §5. `W4` is **unpaid on `RTX` for 209 days** |
| **L** (lenses) — L1 second derivative · **L2 peak-margin trap** · L3 branch information content | — | **DEEP · PREMORTEM.** `L2` binds `MPC`/`PSX`/`VLO`/`MRK`/`MSTR`/`VLO` |

---

## 10 · Catalyst injection — **≤48h binaries, and the PREMORTEM obligation they create**

`catalyst_calendar --days 14` → **7 binaries in window**:

| when | event | bracket state |
|---|---|---|
| **D-0 · 2026-08-28** | **`FRO` earnings** | `S109` armed (settle **09-02**) — ⚠ verify at PREMORTEM that its observable actually spans **tonight's** print |
| **D-0 · 2026-08-28** | Jackson Hole — **Warsh's first speech as Chair** | `S120` armed, settles tonight's close |
| **D-0 · 2026-08-28 (calendar)** | *"July PCE"* | 🚨 **the calendar is wrong — it printed 08-26** (§2b). Recorded as an instrument fact, not scored |
| D-3 · 08-31 | MSCI quarterly review | `S92` `S94` `S104` `S112` `S124` settle 08-31 |
| D-5 · 09-02 | **`AVGO` earnings** (held) | `S127` armed (settle 09-08) — bands **hand-set**, `D295` says re-derive |
| D-7 / D-13 / D-14 | Aug NFP · Aug PPI · Aug CPI | `S126` covers NFP |
| **undated** | *"Iran 'Strait of Hormuz open' statement"* | 🚨 **an Iran–Oman temporary transit deal was struck 08-26** (§2e). The calendar still carries this as undated |

⇒ **PREMORTEM (Stage 7) inherits a hard obligation**: a **both-sides** bracket for every ≤48h binary
that is not already spanned. **A one-way tilt into a known binary is a protocol violation.** The
`FRO` D-0 print and the Hormuz-reopening state change are the two that most plausibly lack coverage.

---

## 11 · What this run has asserted and then refuted, so far (`§4c` / `D48`)

**One, and it is recorded rather than edited away.** PREFLIGHT `G2` passed the gate it measures
(`n_axes` continuous, 7 snapshots) and, **in the same read**, found that three of those seven
snapshots (08-22/23/24) carry `asof: 2026-08-21`. ⇒ the sentence *"Δflow arithmetic is scale-legal
against this history"* is **true as written and misleading if used alone** — the scale is legal and
the **content is duplicated**, so a difference across that band returns ~0 and reads as calm.
The G2 verdict is left standing at PASS (it measures axis count, and the axis count is continuous);
the additional constraint is **appended**, not substituted.

⚠ Beyond that: **zero self-refutations at this stage is itself worth a line** — it usually means the
controls were not adversarial. The genuinely adversarial checks this stage ran were §2e's
three-enumeration invariance test and §2d's reproduction of the registration's own printed values
before trusting my series; **both survived**, which is reported as a result, not as a formality.

---

## ✅ EXIT CHECK
- [x] Shared spines (`STANDING_VIEW.md`, `SCENARIOS.md`) + `STANDING_VIEW_US.md` + `SCENARIOS_US.md` + `RESEARCH.md` read; `SCENARIOS_KR.md` opened to confirm **zero** KR-owned past-dated rows. `module_report_tags show` cross-queried (§6).
- [x] **Retracted ledger read BEFORE today's view formed** (§1d). `R103` and `R89` both bind, and `R89` is directly implicated by §2c's result.
- [x] **Every past-dated scenario scored or named with a reason** (§2a–§2f). Zero silent skips. `S8` named for a 30th run.
- [x] `reject_ledger.py due` run — **0 due, 0 legacy** (§3). Not substituted with `score`.
- [x] `missed_ledger.py due` run — **0 due, 0 legacy** (§3). Signs not summed.
- [x] **Exposure state read and carried** (§4): 정상 · target 95% · current **85.5%** · gap **−9.5pp** · cumulative **−11.68pp = cash −5.94 + selection −5.74, n=16**. Not a cold start; `n` caveat stated.
- [x] 🚨 **Instrument health inherited before any number was trusted** (§0) — `PREFLIGHT.md` exists and was written by this run's Stage −1. Four FAILs converted into explicit removed rights.
- [x] **A claim asserted and then qualified by this run is written down, not edited away** (§11).
- [x] Stale rows flagged with `asof` (§1c, §7); the cleared `D295` suspension converted into a dig, not a trust.
- [x] `[measured]`/`[inferred]` preserved on every carried claim; the `[inferred]` regime call is explicitly barred from being cited as evidence (§1b).
- [x] **RESEARCH triggers loaded as binding constraints, grouped C/S/D/W/L, with the stages they bind named** (§9).
- [x] `HANDOVER.md` written. `handoff/*.md` writeback happens **at run end** (append-only for retractions) — and §1a is exactly why this run will verify that writeback landed.
- [x] **No position sizing and no buy/sell language anywhere above** (P4).
