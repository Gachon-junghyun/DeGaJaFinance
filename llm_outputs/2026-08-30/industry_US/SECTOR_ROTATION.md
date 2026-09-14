# SECTOR_ROTATION — industry_US · 2026-08-30 (Stage 6 / L1·ROTATION)

> Delta-only. MACRO owns the 11-sector verdict (`MACRO_REPORT.md §D`); the flow numbers live in
> `SECTOR_FLOW_US_REPAIRED.json §sector_rotation`. Neither is reprinted. **N = 4** (protocol line).

## §0 · The axis this run scored on, stated before any delta

**`n_axes` = 3 · `vel_coverage` = 17.06% ⇒ the news axis is OUT.** 🚫 **No delta below cites theme
freshness or news velocity.**
🚫 **No delta below cites Δflow.** Two independent reasons, either sufficient: the native run scored
**0 of 299** so there is no operand (G2), and the last comparable snapshot carries **`D401`** (its
terminal bar was an intraday print wearing a settled date).
⚠ **All flow numbers below come from the REPAIRED reconstruction** (`SECTOR_FLOW_US_REPAIRED.json`,
`asof` **2026-08-28**, 08-28 Close replaced by the 5m proxy, engine unmodified, **299/299 scored**).
The native `SECTOR_FLOW_US.json` is empty and is left that way. **Every delta below is therefore a
delta on a repaired basis and says so once, here.**
⚠ `module_industry_map` was **not** invoked: its corpus is Korean and English seeds return 0 by
construction (a measured property, not a failure). The chain-hop substitute ran in EVENT_ALPHA.

## §1 · Inherited — one line, verbatim from MACRO §D

`MACRO holds: FIN OW · HLTH OW · IT N · COMM N(OW-lean) · MATR N · ENRG N · DISC N · STPL N · INDU UW · RE UW · UTIL UW`

## §2 · Deltas — four moved, seven declined, every one with its number

🚨 **Flip list reproduced in full (3 of 11), even where it changes nothing** — a silent flipper is how
one company becomes a sector call:

| sector | top1 | top1 weight | `wflow` | `wflow_ex_top1` |
|---|---|---:|---:|---:|
| Information Technology | `NVDA` | 19.4% | +0.034 | **−0.015** |
| Energy | `XOM` | 30.5% | −0.097 | **+0.074** |
| Consumer Discretionary | `AMZN` | **40.2%** | −0.262 | **+0.056** |

**Moved:**

| sector | matrix said | flow evidence (repaired, asof 08-28) | new verdict | who resolves |
|---|---|---|---|---|
| **Materials** | **N** | `eqflow` **+0.164 = rank 1 of 11** · `wflow` +0.225 · **0 reds of 12 — the only sector on the board with zero** · `top1_flips_sign` **False** and `wflow_ex_top1` **+0.233 is HIGHER than `wflow`** ⇒ the strength is **not** its largest name | **N → OW** | **DEEP (continuous C1)** — the money moved before the thesis (case *b*), and the mandate is the conflict MACRO already flagged: **Copper speculative net at the 100th percentile of its year** |
| **Communication Services** | **N (OW-lean)** | `eqflow` **+0.079 = rank 3** · `top1_flips_sign` **False** · **breadth 0.00 (0🟢/3🔴 of 12)** | **N → OW** | **DEEP (rotating R2)** — ⚠ the promotion rests on `eqflow` **only**, because `wflow` is **−0.424** and the **0.503 wflow/eqflow gap is the widest on the board** with `GOOGL` at 38.3%. **`D297` says exactly this gap is what `top1_flips_sign` does not catch** — so the flip test passing is *not* treated as a clean bill |
| **Financials** | **OW** | `eqflow` **−0.090 = rank 6** · **0 🟢 of 47 — the largest sector on the board with no accelerating name** · `top1_flips_sign` False | **OW → OW−** | **DEEP (rotating R1)** — case *(a)*, right thesis / money not here yet. Rotated **down a notch, not out**, because the divergence is the board's biggest and the DEEP mandate is to resolve **early vs trap** |
| **Consumer Discretionary** | **N** | `eqflow` **−0.247 = rank 8** · **12 reds of 28 = 42.9% red-rate, 2nd-worst on the board** | **N → UW** | — (no DEEP slot; UW) · ⚠ **`AMZN` is 40.2% of the bucket and `wflow` flips without it (−0.262 → +0.056)** ⇒ 🚨1名. **The demotion is carried by `eqflow` and the red-rate, both non-cap-weighted. `wflow` is not used.** |

**Declined — with the number that failed, not silently:**

| sector | move considered | why declined |
|---|---|---|
| **Information Technology** | N → OW | 🚨 **1名 bucket (`NVDA` 19.4%, flips).** `wflow` may not carry it. The two admissible instruments **disagree in size and agree in sign**: `eqflow` **−0.033** (rank 5, negative) against **breadth 0.05 — 3 greens, the most of any sector.** ⚠ **And the three greens are `CRM`, `INTU`, `MSTR` — all software, not one semiconductor**, while `SMH`'s `exc60` is **−15.31 vs SPY**. **Left at N**, routed to **PREMORTEM** as the concentration carrier (`AVGO` prints **D-3**) |
| **Energy** | N → OW | 🚨 **1名 bucket (`XOM` 30.5%, flips).** The non-cap-weighted number is `eqflow` **+0.005 ≈ flat**, and **flat cannot carry a promotion** (the symmetric decline this desk made on 08-29 at −0.004). **Left at N.** ⚠ `R89`+`P83` independently bar a refining-margin-vs-barrel claim, so the sector could not be promoted on its two strongest names (`MPC` +0.650, `PSX` +0.388) even if the number allowed it |
| **Consumer Staples** | N → UW | `eqflow` **−0.187 = rank 7 of 11 — mid-table**, 4 reds of 19 (21.1%, 3rd-lowest red-rate). **A mid-table number does not carry a demotion.** Left at N |
| **Health Care** | OW → OW+ | `eqflow` **+0.135 = rank 2** confirms the OW; there is **no notch above OW** in this desk's grammar. **Confirmed, not moved** |
| **Industrials** | UW → UW− | `eqflow` −0.291 (rank 9) and **17 reds of 50 = the most reds in absolute terms**. Both confirm UW; **no notch below UW.** Left at UW |
| **Real Estate** | UW → — | `eqflow` −0.333 (rank 10). Confirms; no notch below UW |
| **Utilities** | UW → — | `eqflow` **−0.524 = rank 11**, **10 reds of 15 (66.7% red-rate, worst on the board)**, 0 greens. Confirms UW emphatically; no notch below. ⚠ **A macro re-argument was available and is DECLINED ON METHOD** — EVENT_ALPHA Card 4 gives a *capex* cause for the same weakness, but that is an argument, not a flow number, and re-arguing MACRO here is the duplication this stage is told not to do |

★ **Four verdict deltas from eleven attempts, and every one is carried by a non-cap-weighted number
(`eqflow` / red-rate).** **No delta rests on a `wflow` from a flipper bucket.**

## §3 · DEEP picks + DEEP_LOG

**OW set after §2: `HLTH` · `MATR` · `COMM` · `FIN`(OW−) — exactly 4.**
**Recency read from DEEP FILES ON DISK, not from DEEP_LOG lines** (the 08-28 run logged 4 slots and
produced 0 files; the 08-29 run logged 3 and produced 4):

| sector | last DEEP file | runs since |
|---|---|---:|
| HLTH · ENRG · COMM · IT | 2026-08-29 | **0** |
| DISC · INDU · STPL | 2026-08-27 | 1 |
| FIN · RE | 2026-08-26 | **2** |
| MATR | 2026-08-25 | **3** |
| UTIL | 2026-08-23 | 5 |

**① Continuous track (⌈4/2⌉ = 2) — today's top OW ranks by `eqflow`:**
- **`MATR`** (`eqflow` +0.164, rank 1) — enters the continuous track. Also the **least-recently-covered
  OW at 3 runs**, so continuity and recency agree here rather than competing.
- **`HLTH`** (`eqflow` +0.135, rank 2) — **anti-thrash continuity applied and stated**: HLTH held a
  continuous slot in the previous run and is still top-N OW today, so it **KEEPS** the slot.

**② Rotating track (⌊4/2⌋ = 2) — next-highest OW not covered in ~3 runs:**
- **`FIN`** (OW−, `eqflow` rank 6) — last DEEP **2026-08-26 = 2 runs**. Qualifies on recency without a
  waiver. It is the run's **largest unresolved divergence** (`exc60` +12.19pp vs `SPY` against 0 greens
  of 47), which is precisely the case-(a) question the DEEP stage exists to settle.
- **`COMM`** (OW, `eqflow` rank 3) — 🚨 **DECLARED RECENCY VIOLATION: 0 runs** (deep-dived 08-29).
  **Taken anyway under the rule's recency-starved fallback**, because the OW set has exactly 4 members
  and the alternative is padding with a Neutral/UW, which the rule forbids. **Justification stated
  rather than assumed**: the 08-29 DEEP consumed a sweep with `vel_coverage` **0.0%** and `asof`
  **08-27**; today's basis is a **repaired 08-28** sweep in which COMM's `wflow`/`eqflow` gap
  (**0.503**) is the widest on the board. **It is a different measurement, not a re-read of the same one.**

**No padding. No 5th slot promoted at this stage** (PREMORTEM may promote one).
**OW sectors without a DEEP slot: none — all four OW sectors got one.**

**Divergences named, each with a resolution owner:**

| divergence | owner |
|---|---|
| `FIN`: 60-day price leadership (+12.19pp vs `SPY`) against 0 accelerating names in 47 — **early or trap?** ⚠ EVENT_ALPHA Card 1 adds that 6 of 7 majors are **OBV-accumulating with rs20 flat**, which is a third reading and not a tiebreak | **DEEP R1** |
| `COMM`: `eqflow` +0.079 vs `wflow` −0.424 — is the breadth real, or is a 12-name bucket with a 38.3% top-1 simply unmeasurable (`D297`)? | **DEEP R2** |
| `MATR`: rank-1 `eqflow` and zero reds against **Copper COT at the 100th percentile** — flow and positioning point opposite ways | **DEEP C1** |
| `HLTH`: `exc60` **+13.99pp vs `SPY`** (best of 11) against `exc5` **−2.46pp** (worst of 11); `MRK` trades **above** its mean target (`L2` peak-margin lens) | **DEEP C2** |
| `IT`: 3 greens (most on the board) **all software**, zero semiconductors, `SMH` `exc60` **−15.31pp vs `SPY`**, `AVGO` prints **D-3** | **PREMORTEM** (not a DEEP slot — IT is N, and padding is forbidden) |
| `ENRG`: `XOM` alone owns the sector's negative sign (**flipper**, `wflow_ex_top1` +0.074) while the two held refiners are the board's strongest energy flow — **and `R89`/`P83` bar the attribution** | **unowned this run — named, not dropped** (ENRG is N; DEEP'd 0 runs ago) |

## DEEP_LOG 2026-08-30: continuous=[MATR, HLTH] rotating=[FIN, COMM] · N=4/4 filled · **OW sectors WITHOUT a slot: none** · **verdict deltas 4 of 11 attempts — `MATR N→OW` · `COMM N→OW` · `FIN OW→OW−` · `DISC N→UW`, every one carried by a NON-cap-weighted number (`eqflow` / red-rate) and none by a `wflow` on a flipper bucket** · **declines with numbers: `IT N→OW` (1名 `NVDA` 19.4% flips; `eqflow` −0.033 negative while breadth 0.05 is the board's best — routed to PREMORTEM instead), `ENRG N→OW` (1名 `XOM` 30.5% flips; `eqflow` +0.005 flat cannot promote), `STPL N→UW` (`eqflow` rank 7 = mid-table), `UTIL UW→UW−` (declined ON METHOD — the only new argument was EVENT_ALPHA's capex cause, i.e. a macro re-argument), `INDU`/`RE` (no notch below UW), `HLTH OW→OW+` (no notch above OW)** · **flip list 3 of 11 — IT/`NVDA` 19.4%, ENRG/`XOM` 30.5%, DISC/`AMZN` 40.2% — DOWN from 4 on 08-29; `AMZN` at 40.2% is the largest single-name share on the board and Consumer Discretionary's entire negative sign is that one company (`wflow_ex_top1` +0.056)** · 🚨 **the instrument state that governs every line above: the NATIVE sweep scored 0 of 299 (all 301 cached tickers carried a 2026-08-28 Close=NaN with O/H/L/Volume present, bench SPY included) and `SECTOR_FLOW_US.json` is left EMPTY as the honest record; every number here comes from `SECTOR_FLOW_US_REPAIRED.json`, a labelled reconstruction that patches only the 08-28 Close with a 5m-proxy value validated at 0.018% mean / 0.045% max error on the prior session, runs the unmodified engine, and scores 299/299** · 🚨 **`D411`: the foreign news ingest returned 3 articles on 08-29 and 0 on 08-30, so the default `thread` window reports 525 ENDED / 0 alive — ROTATION's news inputs were taken from a window ending 08-28 and no delta cites velocity or freshness (`n_axes` 3, `vel_coverage` 17.06%)** · **`COMM` R2 is a DECLARED 0-run recency violation taken under the recency-starved fallback because the OW set has exactly 4 members and padding with N/UW is forbidden** · **`MATR` C1 is the rare case where continuity and recency agree (rank-1 `eqflow` AND least-recently-covered OW at 3 runs)** · **uncovered=[IT(N — routed to PREMORTEM, 08-29 = 0 runs, the book's largest concentration and the sector whose 3 greens are all software while `SMH exc60` is −15.31pp vs `SPY`), ENRG(N, 08-29 = 0 runs, 1名 `XOM`, and the desk still has NO instrument separating refining margin from the barrel after `R89`→`P83` both failed), DISC(UW — DEMOTED TODAY, 08-27 = 1 run, 1名 `AMZN` 40.2%), STPL(N, 08-27 = 1 run, `eqflow` rank 7 mid-table), INDU(UW, 08-27 = 1 run, 17 reds = board's most in absolute terms), RE(UW, 08-26 = 2 runs, `eqflow` rank 10), UTIL(UW, 08-23 = 5 runs — the board's worst `eqflow` (−0.524) and worst red-rate (66.7%), NOT slotted because UW sectors do not take DEEP slots, and this is the longest recency gap on the board)]**

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, verbatim from MACRO §D. No unchanged sector gets a row, paragraph, or restated flow number.
- [x] **Every §2 delta cites a flow number** (`eqflow` rank / red-rate / `wflow_ex_top1`). The one move whose only support was a macro argument (`UTIL UW→UW−`) is **declined on method and logged**.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** `IT` and `ENRG` were both declined with their flip weights written out; `DISC` was moved **only** on `eqflow` and red-rate with the flip stated. **The flip list is reproduced in full in §2 even though it changed nothing for two of the three.**
- [x] **The axis count is stated** (`n_axes` 3, `vel_coverage` 17.06%): **no delta cites theme freshness or velocity**, and **no delta cites Δflow** (G2 has no operand; `D401` contaminates the comparator).
- [x] Every matrix×flow divergence named with a resolution owner — including the one that is **unowned** (`ENRG`), named rather than dropped.
- [x] **4 DEEP targets by the rule**: continuity applied and stated (`HLTH` keeps its slot), recency read **from files on disk**, the `COMM` **0-run recency violation DECLARED with its justification**, **no padding**, and every uncovered sector named in DEEP_LOG with its recency and its reason.
- [x] **Linter run on this stage's own output** — `report_lint.py SECTOR_ROTATION.md` ⇒ **0 findings** (C1/C2/S6/D6). ⚠ Form only; a clean run is not a correct report.

---

## 🚨 POST-HOC CORRECTION — appended 2026-08-30 23:3x KST (`D48`; full detail in `MACRO_REPORT.md`)

The `DEEP_LOG` line above contains: *"`D411`: the foreign news ingest returned 3 articles on 08-29 and
0 on 08-30, so the default `thread` window reports 525 ENDED / 0 alive."* **That clause is WITHDRAWN.**
The ingest was current; the **client-side `brief`/`thread` mirror** was 38 hours stale because
`embed sync` was not run. After syncing, the same window returns **50 alive threads** and per-day market
events of 791 / 832 / 832 / 854 / 733 / **295** / **123**.

✅ **No delta, decline, DEEP pick or flip-list entry in this file changes.** Every one of them rests on
`eqflow`, red-rate, `wflow_ex_top1` or settled ETF excess vs `SPY` — **not one cites a news number** —
which is precisely why the §0 prohibition ("no delta cites theme freshness or velocity") kept the
sector verdicts insulated from an instrument fault the run had not yet found. **That is the rule
earning its keep, and it is worth recording as such rather than only recording the fault.**
