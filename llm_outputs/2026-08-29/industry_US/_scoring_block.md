

---

# ═══ MASTER SCORING LOG — append by `industry_US`, 2026-08-29 (Sat 09:1x ET · US session 08-28 SETTLED) ═══

> ⚠ **Append-only** (`D165`); text staged in `llm_outputs/2026-08-29/industry_US/_scoring_block.md`
> first (`D357`), file backed up to `SCENARIOS.md.bak_0829us` before the write.
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `M1039`–`M1045` · `D400`–`D402` → **0 hits**. IDs issued by
> `module_evidence next-id` (D highest before: `D399`; M highest before: `M1038`), **not hand-grepped**.
> ⚠ **Language: English** — the US desk's documented practice.
> ⚠ **This block is written at HANDOVER time, not at run end.** Deviation from the usual writeback
> point, taken deliberately: **§A below exists because the 2026-08-28 run deferred exactly this write
> and then terminated before reaching it.** Logged as a resolved decision, not a silent change.

## §A · 🚨 RECOVERY — five verdicts the 2026-08-28 `industry_US` run produced and **never landed**

`llm_outputs/2026-08-28/industry_US/HANDOVER.md §2a–§2e` carries full, sourced verdicts for `S79`,
`S81`, `P83`, `P96` and `S119`. **None of them reached this log.** The 08-28 run wrote
`HANDOVER.md`, `MACRO_REPORT.md`, `SECTOR_FLOW_US.json`, `SECTOR_ROTATION.md`, `SWEEP_READ.md` and
`EVENT_ALPHA.md`, then produced **no `BLINDSPOT_PREMORTEM.md`, no `SECTOR_DEEP_*`, no `BET_SHEET.md`**
⇒ it terminated between ROTATION and PREMORTEM and its writeback pass never executed.

**These are NOT re-scored here.** Re-scoring a frozen observable risks writing the same fact with a
different value. Instead the 08-29 run **re-derived each leg's arithmetic independently and checked
it against the 08-28 run's printed figures**; all six legs matched to four decimals (receipts in
`llm_outputs/2026-08-29/industry_US/HANDOVER.md §2a`). The verdicts below are **attributed to the
2026-08-28 run**, which measured them.

| id | owner | verdict | measurement that settled it · (08-29 reproduction) |
|---|---|---|---|
| **`S79` Leg 1** | `industry_US` | **`FIRED-A`** | `NVDA` 1-session excess vs `SPY` on the first settled session after the 08-26 AMC print (**08-27**): `NVDA` 209.66 → 227.98 = **+8.738%**, `SPY` 766.08 → 771.10 = **+0.655%** ⇒ **excess +8.083pp** vs branch A **≥ +5.0pp** ⇒ **A clears by 3.08pp**, outside the ±6.11% implied move recorded at registration. ⚠ **`S115` fired A on the same session against a ≥ +7.0% line — `S79` L1 and `S115` are ONE event read twice** (`D343`), stated so no stage double-counts. *(08-29 reproduction: +8.0828pp ✅)* |
| **`S79` Leg 2** | `industry_US` | ★★★ **`U-MIXED`** | Same session, `AVGO` and `TSM` 1-session excess vs `SPY`: `NVDA` **+8.083pp** (\|·\|≥5.0 ✅) · `AVGO` **+3.830pp** (same sign ✅, \|·\|≥2.0 ✅) · `TSM` **+1.645pp** (same sign ✅, \|·\|≥2.0 **❌ by 0.355pp**). ⇒ neither `U-ONE` nor `U-SPLIT`. ★ The registration called `U-MIXED` *"the most informative outcome, because it retires a framing the desk uses for its concentration guard."* **On the one day the answer was observable, neither the 250d split (ANET/ETN/AVGO/NVDA standalone) nor the 500/750d merge described the tape** ⇒ **PREFLIGHT `G4`'s cross-window disagreement is not resolved by observation either; the desk has no validated grouping for event risk.** ⚠ **Margin disclosed: TSM missed by 0.355pp on a 2.0pp line.** *(08-29 reproduction: AVGO +3.8301pp, TSM +1.6454pp ✅)* |
| **`S81`** | `industry_US` | **`C`, recorded as AMBIGUOUS by its own anti-signal** | `EW{AVGO,ANET,HPE}` 2-session cumulative excess vs `SPY`, 08-25 → 08-27: `AVGO` +4.149 · `ANET` +5.316 · `HPE` +1.815 ⇒ **EW +3.760%**, `SPY` +0.678% ⇒ **excess +3.082pp**. A ≥ +3.66 (**short by 0.578pp**) · B ≤ −2.86 ⇒ inside C. 🚨 **The registered anti-signal fired and is honoured**: *"a separate ≤48h macro binary on 08-26/27 ⇒ AMBIGUOUS."* **July PCE printed 08-26, in-window and hot** (`yahoo_finance` ×2, 08-26). The C-side number is disclosed because suppressing it would hide how near A it came; **the verdict is not upgraded**. *(08-29 reproduction: +3.0822pp ✅)* |
| **`P83`** | `industry_US` (MACRO) | ★★ **`FIRED-B`** | (`HO=F` − `RB=F`) × 42, change from the 08-20 settle of **51.131**, at the 08-27 close. Settled series **51.131 → 48.170 → 41.870 → 41.618 → 39.476 → 37.569** ⇒ **change −13.562**, branch B **≤ −4.0** ⇒ **B by 9.56 points.** ★★ **`P83` was registered 2026-08-21 as the replacement INSTRUMENT after `R89` retracted the refining-separation claim**, chosen because *"a pure crude move cannot widen it."* It did not widen; it collapsed. ⇒ **the successor separator has failed too, and the desk has no surviving instrument that separates the refining excess from the barrel.** The refining *thesis* is not retracted by this row — crack levels and capacity mechanisms are separate evidence — but **separation may not be re-asserted on any instrument.** ⚠ Composition disclosed: two-sided, `HO=F` 4.480 → 4.279 (−4.5%) and `RB=F` 3.263 → 3.384 (+3.7%). *(08-29 reproduction: 51.1308 → 37.5690, −13.5618 ✅)* |
| **`P96`** | `industry_US` (MACRO) | **`FIRED-B`** ★ and the live read had the sign backwards | Settled 3-2-1 crack **5-session change** at the 08-27 close. A ≤ −2.887 · B ≥ +0.468. Reconstruction validated against the registration's own printed values before use (**−2.862 @ 08-24**, **−1.675 @ 08-25** — byte-matching `M936`). Measured at the settled 08-27 close: **+4.874** ⇒ **B, clearing by 4.41.** 🚨 **The 08-27 run's `SECTOR_DEEP_ENRG` wrote *"as printed −8.584 = deep inside A"* off a LIVE INTRADAY 08-27 bar — the settled bar is the opposite branch, 13.5 points away.** `D355` landing on a **registered row**. ✅ `M958`'s withdrawal of the 08-26 live crack figure is vindicated by the settled tape (`RB=F` 3.320 → 3.384, i.e. it **rose**). *(08-29 reproduction: 66.2554 → 71.1294 = +4.8740 ✅)* |
| **`S119`** | `industry_US` | **`FIRED-C`** — ★ and the reason it is scoreable is measured, not asserted | Handed to this desk by name by the KR run of 08-28, which declined it under `C5` (*"the row never enumerates the basket's membership"*, ⇒ `D388-KR`). **The refusal was right; reconstructing one basket would make this desk choose the observable.** What the 08-28 US run did instead: scored it under **every plausible enumeration** and tested whether the branch depends on the choice. Window 08-24 → 08-27, bands **±2.60pp**, untouched (`D242`), `SPY` +0.999%: **(a)** EW of the sweep's own 16 GICS-Energy names (identical membership in the 08-24 and 08-27 snapshots) −0.710% ⇒ **−1.709pp**; **(b)** `RSPG` (S&P 500 equal-weight energy) −0.363% ⇒ **−1.363pp**; **(c)** `XLE` (cap-weighted, robustness read) −1.299% ⇒ **−2.299pp**. ⇒ **C fires on all three. The verdict is invariant to which basket the row meant.** `D388-KR` stands as a rule; what is **not** true is that the row was unscoreable — it was unscoreable by a single arbitrary pick and scoreable by showing the pick does not matter. ⚠ Nearest branch is B at −2.299pp vs −2.60pp (**0.30pp**), disclosed. **Anti-signals probed, neither fired**: the presser held (`fxstreet` 08-24); **no US–Iran direct-talks announcement with a named date** — the window instead contains an **Iran–Oman temporary Strait of Hormuz transit deal (08-26**, `foreignpolicy`/`semafor`/`aljazeera`) and, on the US leg, the opposite (`aljazeera` 08-26 *"not in a hurry"*; `wsj` 08-27 *"Iran Talks Sputter"*). *(08-29 reproduction: XLE −1.299% / RSPG −0.363% / SPY +0.999% ✅)* |

⇒ **`D400` registered**: *a scoring verdict that exists only in a run directory is not scored.*
**Positive form**: the writeback pass verifies `grep "<id>" handoff/SCENARIOS.md` returns ≥1 hit
**for every id the run scored**, before the run is called complete.

## §B · Scored by the 2026-08-29 `industry_US` run

> The **2026-08-28 US session is settled** and this run fires after it — the first US run in four
> to have its own settle date behind it rather than ahead of it.
> ⚠ **Both rows were scored under TWO price surfaces and the branch reported only because it is
> invariant across them** (`C5`). See §C for why that was necessary.

| id | owner | verdict | measurement that settled it |
|---|---|---|---|
| **`S116`** | `industry_US` | **`FIRED-C`** | Frozen observable = `MRVL` − `AVGO` **1-session excess** on the first settled close after the 08-27 print (**08-28**), each vs its own 08-27 close. A ≥ **+12.0pp** · B ≤ **−12.0pp**. Measured: `MRVL` 241.45 → **216.62** = **−10.2837%**, `AVGO` 371.54 → **368.79** = **−0.7402%** ⇒ **spread −9.5435pp** ⇒ **C**. Second surface (`repair=True`): −10.3748% / −0.6513% ⇒ **−9.7235pp** ⇒ **C**. **Invariant.** ⚠ **Margin disclosed and it is the informative part**: the spread is **79% of the way to B** (2.46pp short) on a **beat-and-raise** print — *"Marvell Leads AI Stocks Lower After Earnings That Narrowly Topped Estimates"*, *"Marvell forecasts $18B fiscal 2028 revenue, data center growth >60%"* (`seekingalpha` 08-27). **C is the verdict and the direction is not neutral; saying so is not moving the line.** **Anti-signal** (*"an announced acquisition of, or by, either company inside 08-24→08-28"*) **probed, NOT fired** — argued from a **loud** query, not a zero-hit one (`D94`): `Marvell` returns **482** foreign hits/7d, **380**/4d, and the window's content is the print, not a corporate action. ⇒ **`M1039`** |
| **`S118`** | `industry_US` | **`FIRED-C`** | Frozen observable = `EW{MU,SNDK,WDC}` **2-session excess vs `NVDA`**, 08-26 close → 08-28 close. A ≥ **+6.50pp** (the print is about MEMORY) · B ≤ **−6.50pp** (the print is about NVDA). Measured: `MU` **−0.5904%** · `SNDK` **−0.9597%** · `WDC` **−2.0112%** ⇒ **EW −1.1871%**; `NVDA` 209.66 → **217.55** = **+3.7632%** ⇒ **spread −4.9503pp** ⇒ **C**. Second surface (`repair=True`): EW −1.2267% vs `NVDA` +3.9254% ⇒ **−5.1521pp** ⇒ **C**. **Invariant.** ⚠ Spread is **76% of the way to B** (1.55pp short). **Anti-signal** (*"a memory-maker pre-announcement **or guidance revision** with a named date inside 08-24→08-28"*) **probed, near-miss disclosed, NOT fired**: the window contains ***"Micron Technology to Report Fiscal Fourth Quarter Results on September 30, 2026"*** (`yahoo_finance` 08-26) — **an announcement with a named date**, but an earnings-*calendar* notice, **neither a pre-announcement nor a guidance revision**; also *"Micron Announces Leadership Appointments"* (08-26), likewise non-qualifying. ⇒ **NOT fired on the row's own words**, recorded with sources so a later run can overturn it on evidence. ★ **The same item corrects a carried fact the row's base-rate argument rested on**: registration read *"`MU` does not print until **09-24**"*; it prints **09-30**. The base rate was argued from a wrong date and is **safer** than claimed, not less safe ⇒ **`M1044`**. ⚠ **`S116` and `S118` are NOT independent** — `NVDA`'s +3.76% two-session move is inside both, and `S79` L1 measured the 08-27 leg of that same path (`D343`) |

### Not scored by this run, and why — named rather than dropped

| id | why not scored |
|---|---|
| **`S120`** | Needs *"the first observation where **BOTH** `DGS30` and `T10YIE` carry 2026-08-28."* `T10YIE` **has 08-28 (2.31)**; `DGS30` ends **08-27 (5.19)**. **Not readable ⇒ stays ARMED, NOT `EXPIRED`.** ✅ **The row's own observation-lag clause working as designed** — it was written in at registration so this would be a deferral, not a discovery. That is exactly what `S102` lacked for five runs |
| **`S111`** | `BAMLC0A0CM` (`ig_oas`) ends **08-27 = 0.79**; needs the first close covering 08-28. **Stays ARMED.** ⚠ Pre-settle read disclosed: 0.79 is inside **C** (A ≥ 0.85 / B ≤ 0.77), **2bp above B** — 🚫 not to be inherited as "C fired" |
| **`P67`** | `hy_oas` ends **08-27 = 2.63** vs a **≥ 2.85%** line ⇒ **22bp below**. **Stays ARMED**; disclosed, not scored |
| **`S103`** | Handed here by the KR run of 08-29. Registered to settle **2026-08-29, a Saturday**; its `"first settled close on/after"` clause moves it to **08-31**. **NOT due.** ⚠ The KR run's 4-session preview (**+1.663pp**) was **independently reproduced by this run at +1.6630pp** — used as instrument corroboration (§C), **explicitly not as a score** |
| **`S124`** | 🚨 **Correction to the 08-28 HANDOVER, which listed this as settling 08-28.** It settles **2026-08-31** (cross-sectional count of `us_top300` IT names with positive `exc5` vs `SPY`). **Not due.** ⚠ It is the **only cross-sectional row on 08-31** and it tests this desk's own `IT` underweight — **branch B is the one that vindicates the desk**, stated so C is not read as a win |
| `S92` `S94` `S104` `S112` | settle **08-31**. ⚠ `S104`'s title still carries the `R106` date defect (*"July PCE 2026-08-28"* when PCE printed **08-26**); **its settle is later and no threshold is touched** |
| `P86` | PCE conjunct **met**; rate conjunct unreadable (`DGS2` **4.20** @08-27 vs A ≤ 4.10 / B ≥ 4.32). **Stays ARMED** |
| `P97` | unreadable — `DTWEXBGS` ends **08-21**, eight days behind the joint date the row requires. **`D333`'s 11th reproduction** |
| `S109`(`FRO`) `P81` `P85` `P87`–`P89` `S127` `S128` `S129` `S130` | not yet due (09-02 and later) |
| **`S8`** | ⛔ **unscoreable for a 31st consecutive run** — date field still `[blank]`. **Named again rather than dropped.** A human must `VOID` it or re-register it with a date (P5) |
| KR-owned rows | **zero due**; earliest `S67-KR` **09-04** |

## §C · 🚨 The instrument finding that forced §B's two-surface method — `M1040`–`M1043`

Scoring `S116` required the **2026-08-28 settled close**, and the provider returned **three different
values for it**. Measured 2026-08-29 ~22:2x KST, one provider (`yfinance`), three surfaces:

| surface | NVDA 08-28 | SPY 08-28 | MRVL 08-28 |
|---|---|---|---|
| `yf.download(...)` daily bar | **NaN** | **NaN** | **NaN** |
| `yf.download(..., repair=True)` | 217.89 (`Repaired? True`) | 769.35 | 216.40 |
| `Ticker.fast_info['last_price']` | **217.55** | **769.35** | **216.62** |

- **`M1040`** — the 08-28 row is **present with Volume and with Open/High/Low; only `Close` is NaN.**
  NVDA 08-28: O **227.33** / H **229.26** / L **216.81** / C **NaN** / V **194,036,188**. The session
  happened. Reproduced on all nine tickers probed (`NVDA SPY MRVL AVGO MU SNDK WDC XLE RSPG`) and on
  the three energy futures (`CL=F HO=F RB=F`).
- **`M1041`** — this is the **same defect class the KR desk measured this morning** (`M1026`: a phantom
  08-28 bar for **831 of 833** KR names), **independently re-measured here on US names** — not a
  cross-market transfer — and **the signature differs**: KR lost all of OHLC, **US lost `Close` only**.
- **`M1042`** — ★ **the tie was broken by measurement, not by preference.** The KR run, eleven hours
  earlier and through a different path, quoted `NVDA` 08-28 = **217.55** / `SPY` = **769.35** and
  published a four-session `S103` preview of **+1.663pp**. Recomputing that preview from **this run's**
  `fast_info` values returns **+1.6630pp** — byte-identical. ⇒ **`fast_info.last_price` is the settled
  close; `repair=True`'s 217.89 is a synthetic outlier, flagged as such by its own `Repaired?` column.**
- **`M1043`** — a **fourth** disagreement inside the same instrument: `fast_info['previous_close']`
  returns **226.149** where the daily bar's 08-27 close is **227.98**. Not used; recorded, not diagnosed.
- ⚠ **`D5` (cross-provider) is UNMET.** A second provider was attempted and **failed**: Stooq returned
  **HTTP 404** for every US symbol (`nvda.us` `spy.us` `mrvl.us` `avgo.us` `mu.us` `sndk.us` `wdc.us`),
  retried once with a raw-response diagnostic, same result. The corroboration above is
  **temporal + cross-path within one provider**, which is weaker. **Stated, not glossed.**
- 🚫 **Right removed for the rest of this run**: `repair=True` output may not be used as a settled
  price. Where an 08-28 close is needed it comes from `fast_info.last_price`, and both readings are
  shown wherever a threshold sits within one reading's width of the other.
- ⇒ **`D402` registered**: *`repair=True` fabricates a settled price and flags it only in a column
  nobody reads.* **Positive form**: any settled-price read asserts `Repaired? == False`, or falls back
  to `fast_info.last_price` **and says which it used**.
- ⚠ **Contaminated stretch registered, not cleaned**: the **2026-08-28 daily-close bar** is unreadable
  via `yf.download` for US names. Prior runs' figures are **not** retro-corrected; they carry this note.

## §D · 🚨 A finding about the snapshot files this log's rows are read beside — `M1045` / `D401`

Found while checking PREFLIGHT `G2`, and it **refutes that gate's own summary sentence**, which is
left standing in `PREFLIGHT.md` per `D48` rather than edited.

`SECTOR_FLOW_US.json`'s `asof` is set from **the bench frame's last index date**
(`scripts/sector_flow.py:507-509`) — which a **live intraday** row satisfies. Measured:

| snapshot | its `asof` | its `last` for `NVDA` | that date's **settled** close | gap |
|---|---|---|---|---|
| 08-27 file | 2026-08-27 | **224.17** | **227.98** | **−1.67%** |
| 08-28 file | 2026-08-28 | **227.46** | **217.55** | **+4.56%** |

Both `last` values sit **inside their own date's intraday range** (08-27 H/L 230.47 / 220.90;
08-28 H/L 229.26 / 216.81), which excludes *"it is the prior close"* and *"it is an adjusted value"*.
⇒ **the snapshots' terminal bars are live intraday prints taken minutes after the 09:1x ET open**, and
**a `Δflow` between two snapshots differences two intraday photographs, each labelled with a settled
date.** `G2`'s PASS stands (it measures axis-count continuity, which is continuous); the constraint is
**appended, not substituted**. 🚫 **No stage may describe a `SECTOR_FLOW_US.json` figure as a settled
reading this run.**
⇒ **`D401` registered**: *PREFLIGHT's `asof` gate reads a field, not a bar.* **Positive form**: `G2`
compares the snapshot's `last` for one liquid name against that date's **settled** close and reports
the gap in %.

★ This row belongs in the scoring log rather than only in a run directory for the same reason §A
exists: **`P96` was put on the wrong branch by exactly this defect** — the 08-27 `SECTOR_DEEP_ENRG`
read a live intraday crack of **−8.584** where the settled value was **+4.874**, the opposite branch,
13.5 points away. `D355` and `D401` are the same mechanism at two altitudes.

## §E · Two observations this log leaves

1. **The desk's scoring is now three-for-three on "the pre-settle read pointed the wrong way."**
   `S101` registered −0.677, pre-settle +1.616, final −0.744. `P78` pre-settle **above branch A**,
   final **branch B**. `P96` live **−8.584 (deep in A)**, settled **+4.874 (B)**. ⇒ **a pre-settle
   read is not a weak version of a verdict; on this desk's record it has been an inverted one.**
   Rows `S111`/`P67`/`P86`/`P97` are deferred **with their pre-settle numbers disclosed** precisely so
   the next run inherits the number *and* this warning together.
2. **Nothing was registered by this stage.** New brackets are PREMORTEM's to write (Stage 7); the
   ≤48h obligation handed forward is **MSCI 08-31 (inside 48h, six rows already on that date)** plus
   two **uncovered** dated binaries — **Aug PPI 09-10** and **Aug CPI 09-11, zero rows on either** —
   and the **Hormuz state change**, which `catalyst_calendar` still carries as *undated* although a
   temporary Iran–Oman transit deal was struck **2026-08-26**.
