# SECTOR_ROTATION — industry_US — 2026-07-30 (Thu)

> **Delta-only.** MACRO owns the 11-sector verdict (`MACRO_REPORT.md §E`); `SECTOR_FLOW_US.json`
> owns the flow numbers; both are on disk. **Nothing unchanged is restated.** Benchmark **SPY**
> inline (C1). Flow asof **2026-07-29 settled** (D74 remediated in-run — `SWEEP_READ.md §0`).

## §1 · Inherited from MACRO §E — one line, verbatim

`ENRG OW− · IT N · FIN OW− · INDU OW− · HLTH N · COMM N− · UTIL N− · RE N · MATR UW · DISC N− · STPL N`

## §2 · Deltas — five, each carried by a flow number

| Sector | Matrix said | Flow evidence (wflow · eqflow · breadth · 🟢/🔴 · Δ) | New verdict | Who resolves |
|---|---|---|---|---|
| **Materials** | **UW** | **eqflow +0.142 POSITIVE against wflow −0.031** — the **only sector on the board with that sign pattern**; 0🟢 / 1🔴, breadth 0.000. ★ **And the 0🟢 is disqualified as evidence**: 5 of 12 names pass the `OBV-accumulation ∧ RS20>0` pre-condition and **all 5 are blocked by `vol_surge` alone**, the sector's **highest `vol_surge` being 1.14 against a 1.20 gate** (`SWEEP_READ §2a`) | **UW → N** | ★ Already owned by **S36**, window **08-05**. Its branch-A second leg ("green count still 0") is now **measured to be an instrument artifact**, so the bracket can no longer confirm the UW — it can only falsify it |
| **Comm Services** | **N−** | **eqflow +0.278 > wflow +0.123** — breadth-led, the inverse of Info Tech's sign; **breadth 0.230 = 2nd best of 11**; **3🟢 / 1🔴, and the single 🔴 is GOOG** | **N− → N** | **S16**, window **08-12** (currently tracking branch B on price while the flow axis says branch A — the disagreement is the finding, **C4**) |
| **Health Care** | **N** | **wflow +0.360 / eqflow +0.300 = 4th on the board**, **4🟢 / 2🔴**, breadth 0.120. ★ **C7's resolving observable is no longer zero**: **TMO (+0.88, the sector's #1 flow score) and HCA (+0.61, `new_green`) are greens outside the top-6 by cap** | **N → OW−** | **DEEP ③ this run** (see §3). ⚠ **C7 is NOT declared resolved** — the "top-6" is an undocumented arbitrary choice and the desk's own named block differs from the cap ranking (**C5**, `SWEEP_READ §2f`) |
| **Real Estate** | **N** | **breadth 0.330 = the board's best**, **4🟢 / ZERO🔴 — the only zero-red sector of 11**; wflow +0.420 / eqflow +0.402. ★ **Three of the four greens ignited in one session** (AMT Δ+0.70 · CCI Δ+0.82 · DLR Δ+0.50, all `new_green`) | **N → OW−** | **DEEP ④ this run.** ⚠ **n = 1 session (S1)**, and all three new greens still carry **negative RS60 vs SPY** — a turn off a weak base, not a continuation |
| **Info Tech** | **N (split unconfirmed)** | **wflow +0.085 against eqflow −0.195 = a 0.280 gap, the widest of the 11**; **32🔴 of 56 — more reds than the next three sectors combined**; and **no 🟢 anywhere in memory or semi-equipment** for a 2nd run | **N → N−** | **S30 (08-05) and S13 (08-12)** own the *split*; this notch is on the *label*, and it is deliberately **one notch, not two** |

### Attempts declined, logged rather than taken

- **Utilities N− → UW: DECLINED, and the reason is that the flow and the price disagree inside the
  label.** The sector-level flow supports a demote — it is **the only sector negative on BOTH wflow
  (−0.109) and eqflow (−0.122)**. But **S35's regulated-seven median RS20 vs SPY has crossed ABOVE
  zero (+0.39, from −1.99 and a registration −3.2)** while **S24's AI-power median deepened to
  −14.35**. ⇒ **a single label moving two ways by 14.7pp.** Demoting the label would deepen an
  underweight on the leg that is recovering. **Left at N−, and the split is named as the #1 question
  for PREMORTEM** — this is **W5's trigger**, not a rotation call.
- **Energy OW− → OW: DECLINED as a macro re-argument.** Energy is the board's **#1 on both wflow
  (+0.558) and eqflow (+0.477)** and would qualify on flow alone — **but the only new reason to
  upgrade is P4's crack direction, which is MACRO's argument, and S31's own observable is currently
  running AGAINST the desk's sub-segment choice (XOM RS20 vs SPY +16.97).** Upgrading a tilt whose
  internal composition is under an armed challenge is the R7 error. **Held at OW−.**
- **Industrials OW− → N: DECLINED.** XLI was the worst sector of 07-29 (−3.19%) and carries a
  **−2.31pp 20-day excess vs SPY**, but the flow says the opposite — **10🟢, the most of any sector,
  and breadth 0.200 (2nd best)** — and **S42 is armed on exactly this node to 08-12** with its
  in-bracket control (CAT, RS20 −24.04) diverging further. **The bracket resolves it; the label does
  not move while a registered test is running.**

## §3 · DEEP picks and DEEP_LOG

**Recency input, `DEEP_LOG` lines read from disk**: `07-22 [ENRG,FIN]` · `07-23 [ENRG,FIN]/[HLTH]` ·
`07-24 [ENRG,FIN]/[HLTH]` · `07-25 [ENRG,FIN]/[RE]` · `07-27 [ENRG,FIN]/[INDU]` ·
`07-28 [ENRG,FIN]/[IT,COMM]` · `07-29 [ENRG,FIN]/[INDU]` (+UTIL written same run).

**OW set after §2's deltas: ENRG · FIN · HLTH · RE — exactly four.**

| Slot | Sector | Selection basis | The question DEEP must answer |
|---|---|---|---|
| **① continuous** | **Energy (OW−)** | Held a continuous slot in the previous run **and** is still top-4 OW ⇒ **anti-thrash continuity KEEPS the slot** (stated per the rule). Board's #1 on both flow axes | **Is the OW pointed at the wrong sub-segment?** **S31's observable moved AGAINST the desk: XOM RS20 vs SPY +16.97 with RS60 +1.83**, while **PSX's days-21-60 excess is negative** and **BKR — a name on the reject ledger — is now the sector's #1 flow score (+0.93, `new_green`)**. ⚠ **XOM prints 07-31, INSIDE S31's own window.** ⚠ **P4's crack distance is unquotable under R30/D95 — DEEP must not restate a buffer** |
| **② continuous** | **Financials (OW−)** | Same rule: continuous in the previous run, still top-4 OW. **eqflow +0.407 > wflow +0.386 — breadth-led again**, 8🟢/1🔴, and **32 pre-condition names (24 blocked) = the deepest accumulation base of any sector** | **Which leg is the OW actually long?** The steepener leg died (**R11**), **S23's flattener moved 1bp AWAY** (MACRO §G-1), and **MA printed a beat inside its own pre-declared no-information band**. ⚠ **M239: the breadth claim was 46% one holding company (BRK-B).** Re-derive from all 47 rows — **do not inherit** (R20's lesson) |
| **③ rotating** | **Health Care (N → OW−)** | **Recency-clean**: last covered **2026-07-24, six runs ago** — the longest gap of any OW sector. Promoted on flow this run | **Is C7 finally resolvable, or is its observable broken?** **TMO and HCA are greens outside the cap-top-6, but the desk's own named block contains TMO and not AMGN (C5).** ⚠ **ABT — C7's standing watch name — carries RS20 +22.19 / RS60 +20.10 AND a FINRA 5v5 of +10.2▲**: the A-grade price and the B-grade short-pressure disagree on the one name the contradiction hangs on |
| **④ rotating** | **Real Estate (N → OW−)** | **Recency-eligible**: last covered **2026-07-25, five runs ago**. Promoted on the board's best breadth and its only zero-red count | **Did the three names R10/M131 SPLIT INTO SEPARATE UNITS turn on the same day by coincidence or by beta?** **AMT, CCI and DLR all flipped `new_green` in one session** — AMT and CCI were re-clustered into *duration* and DLR into the *data-centre* node, **so the measured clustering says this should not happen.** ⚠ n=1 (**S1**). Also: **S25's branch B is satisfied a 3rd session** and **EQIX printed today** |

**No padding**: the OW set is exactly four, so no Neutral or UW sector was promoted to fill a slot.
⚠ **Two sectors with larger fresh evidence than slots ③/④ were NOT selected, and that is stated
rather than hidden**: **Utilities** (the 14.7pp intra-label split) and **Materials** (the third failed
deferral). **Both are non-OW and therefore ineligible under the selection rule**, and **both already
have armed brackets that settle inside two weeks — S35 (08-07) and S36 (08-05)** — so they are handed
to **PREMORTEM**, not left unowned.

## §4 · Corroborant only — news velocity and the industry map

- **News velocity recount** (`--scope foreign`, pool-normalised, MACRO §C-1): **Rates/Fed 1.16× is
  the only elevated bucket; the two oil buckets are the two lowest (0.96× / 0.92×)** on a day whose
  #1 and #2 head events are both oil. **Used as a corroborant only** — raw term counts are frequency
  noise and the flow sweep is the primary intensity axis (M186/M244, 4th replication).
- **`module_industry_map` NOT run, with the reason stated**: it reads `data/corp_embeddings.db`,
  a **KR-language corpus**; **English seeds return 0 hits by construction** — a null from it would be
  a **D94-class vocabulary artifact**, not evidence about US industry structure. The US chain
  reference used instead was **`chain-hop`** (EVENT_ALPHA §Card 3), which returned **only two
  candidates one hop past the headline layer (WMT, JPM — both mis-attributions)** ⇒ **the
  AI-datacenter theme's exposure map is saturated at the headline layer**, which is itself the
  finding.

## ✅ EXIT CHECK

- [x] **§1 is ONE line**, inherited verbatim from MACRO §E. No unchanged sector has a row, paragraph
      or restated flow number anywhere in this file.
- [x] **Every §2 delta cites a flow number** (wflow · eqflow · breadth · 🟢/🔴 · Δ). **Three changes
      were attempted and declined** — Utilities, Energy and Industrials — **and each declination is
      logged with its reason**; the Energy one is explicitly logged as *"macro re-argument, declined"*.
- [x] Every matrix×flow divergence names a resolution owner: **MATR→S36 · COMM→S16 · HLTH→DEEP③ ·
      RE→DEEP④ · IT→S30/S13 · UTIL→PREMORTEM.**
- [x] **4 DEEP targets picked by the rule** — continuity stated for ①②, recency stated for ③④
      (six and five runs since last coverage). **No padding**; the OW set is exactly four.
- [x] DEEP_LOG line appended below.
- [x] Linter — see §5.

## §5 · Rule-linter result

`python -X utf8 scripts/report_lint.py "llm_outputs/2026-07-30/industry_US/SECTOR_ROTATION.md"`
→ **✅ 0 findings** across **C1 · C2 · S6 · D6**. No exemptions claimed.
⚠ Form only; a clean run is not a correct report — it cannot see that §2's Materials row rests on an
**artifact diagnosis** rather than on a positive flow reading, or that §3's ③/④ picks are **freshly
promoted this run** and therefore have one run of evidence, not several.

## DEEP_LOG 2026-07-30: continuous=[ENRG, FIN] rotating=[HLTH, RE]
