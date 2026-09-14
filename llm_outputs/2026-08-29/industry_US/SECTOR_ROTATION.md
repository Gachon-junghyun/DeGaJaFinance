# SECTOR_ROTATION — industry_US · 2026-08-29 (Stage 6 / L1·ROTATION)

> **Delta-only.** MACRO §D owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. This file writes **what changes, why, and what was declined** — nothing else.

## §0 · The axis count this run scored on, and what it forbids

`SECTOR_FLOW_US.json §scoring` = **`n_axes` 3 · `vel_coverage` 0.0% · `scored` 299 ·
`dropped_missing_axis` 0** · **`asof` 2026-08-27 (settled)**.

🚫 **No delta below cites theme freshness or news velocity** — the axis scored **0.0%** this run, and
`SWEEP_READ §0` measures that the zero was **caused by this run's own request load** (`M1060`), not by
the news. 🚫 **No delta cites Δflow** — the JSON's 299 `delta` values difference a settled 08-27 bar
against the 08-27 file's **intraday** 08-27 bar (`D401`); the field is populated and not comparable.
🚫 Per **`R108`**, the flipper list below **withholds** promotions; it does not certify the rest.

## §1 · Inherited — MACRO §D, verbatim, one line

`MACRO holds: COMM OW · FIN OW− · IT N · ENRG N · HLTH N · DISC N · MATR UW · STPL UW · RE UW · UTIL UW · INDU UW−`

## §2 · Deltas — four moves, every one carried by `eqflow`, none by a cap-weighted number

### 🚨 Flip list reproduced in full (4 of 11) — even where it changes nothing

| sector | `top1` | `wflow` | `wflow_ex_top1` | `eqflow` |
|---|---|---|---|---|
| Information Technology | `NVDA` | +0.008 | **−0.121** | +0.060 |
| Health Care | `LLY` | −0.027 | +0.053 | **+0.102** |
| Energy | `XOM` | −0.051 | **+0.168** | +0.092 |
| Consumer Discretionary | `AMZN` | −0.136 | +0.015 | **−0.325** |

⚠ **This list GREW 2 → 4 between PREFLIGHT's baseline and this run's own file** — same universe, same
axes, same session label, **only the terminal bar moved from intraday to settled** (`M1061`). It is
`R108`'s class measured on the US desk. **Every delta below therefore uses `eqflow`, which is not
cap-weighted**, and says so on the row.

| sector | matrix said | flow evidence (`asof 2026-08-27` settled) | new verdict | who resolves |
|---|---|---|---|---|
| **Health Care** | `N` | **`eqflow` +0.102 = the HIGHEST of 11** · `wflow` −0.027 (🚨1名 `LLY`) · breadth **0.03** · n=32 | **`OW`** | 🚨 **DEEP.** Promoted on `eqflow` **only** — `wflow` is inadmissible here (flipper). **And the promotion is made against the tape**: `XLV` `exc5` **−2.456pp vs `SPY`** is the board's worst. **DEEP's #1 question: the board's best money-flow breadth sits under the board's worst 5-day return — early, or a value trap?** |
| **Energy** | `N` | **`eqflow` +0.092 = 2nd-highest** · `wflow` −0.051 (🚨1名 `XOM`) · `wflow_ex_top1` **+0.168 = the largest ex-top1 positive of 11** · breadth 0.00 · n=16 | **`OW`** | 🚨 **DEEP.** Promoted on `eqflow`; the ex-top1 figure is cited as **corroboration only** because it is still cap-weighted. `XOM` alone carries the sector's sign negative. EVENT_ALPHA Card 3 hands `MPC`/`PSX`/`VLO` as CONFIRMED-EARLY (`rs60` **+36.7 / +29.8 / +32.7**, all OBV 매집) |
| **Consumer Discretionary** | `N` | **`eqflow` −0.325 = 2nd-WORST of 11** · `wflow` −0.136 (🚨1名 `AMZN`) · breadth 0.00 · n=28 | **`UW`** | Demoted on `eqflow` **only**. ⚠ Contradicts the 1-day tape (`XLY` `exc1` **+1.375pp vs `SPY`**, 2nd best) — **the 1-day pop is not in the money flow**, and the 5-day is negative (`exc5` −1.160pp) |
| **Financials** | `OW−` | `wflow` **−0.144** and `eqflow` **−0.144**, identical, **NOT a flipper** · breadth 0.02 · n=47 | **`N`** | Rule (a): *matrix-OW but flow-absent ⇒ rotate DOWN a notch.* **The only sector on the board where both flow reads agree, both are negative, and no instrument defect is available to explain it away**, while the settled tape is positive (`XLF` `exc5` **+0.605pp vs `SPY`**). 🚨 **Not resolved here — handed to PREMORTEM** (§4) |

### Declined with numbers — four attempts, so "we never looked" stays distinguishable

| sector | attempted move | declined because |
|---|---|---|
| **Information Technology** | `N` → `OW` on `eqflow` +0.060 (3rd-highest positive) | 🚫 **Declined.** The same file's `wflow_ex_top1` is **−0.121** — equal-weighted positive, cap-weighted-ex-`NVDA` negative — and the settled tape says `XLK` is **worst of 11 on 1 day (−1.321pp) and best of 11 on 5 (+0.824pp)** (`M1050`). **Three admissible numbers, three different signs.** A promotion here would be a choice of window, not a reading of flow. **Left at MACRO's `N`; `P113` is the row that decides it** |
| **Communication Services** | `OW` → `N` on `wflow` −0.260 | 🚫 **Declined.** `eqflow` is **−0.004 ≈ flat**, and G5 says the 45-day-stale caps make `eqflow` the citable one ⇒ **flat breadth cannot carry a demotion.** The settled tape is the board's best on **both** windows (`exc1` +1.645pp, `exc5` +0.953pp vs `SPY`). **`OW` held.** ⚠ Weakened: the sector produces **zero** shortlist names, and `SWEEP_READ §5` diagnoses that as a `vol_surge` filter artifact, not absence of flow |
| **Materials** | `UW` → `N` on `wflow` +0.028 (the board's only positive) | 🚫 **Declined.** `eqflow` is **−0.020** and G5 makes `eqflow` the citable read ⇒ mega-cap-led up, breadth down. Corroborant: **Copper speculative net at the 100th percentile of one year** (`M1049`) is contrarian ammunition, not confirmation. **`UW` held** |
| **Industrials** | `UW−` → `UW` (a half-notch up on the two dated catalysts) | 🚫 **Declined ON METHOD.** The only argument available was a **macro re-argument** (NFP 09-04, Canada tariffs 09-08) and the stage rule says that does not qualify — MACRO owns it, and this stage has worse macro inputs. The flow refuses anyway: `wflow` −0.188 / `eqflow` −0.204, both negative, no flipper. **`UW−` held** |

**Unchanged and not restated** (flow agrees with the matrix, no row earned): `STPL` `UW` ·
`RE` `UW` · `UTIL` `UW` · `INDU` `UW−`. These four are the board's worst `wflow`/`eqflow` pairs and
are the **only** part of the matrix where flow and wind agree without qualification.

### ★ The structural fact behind all four deltas, in one line

**`eqflow` is positive in exactly 3 of 11 sectors — HLTH +0.102, ENRG +0.092, IT +0.060 — and all
three are `top1_flips_sign` = True.** Every sector with positive breadth is a sector where the flipper
guard forbids a cap-weighted move. Two of the three were promoted on `eqflow`; the third (IT) was
declined because its non-cap-weighted and cap-weighted reads disagree in sign.

## §3 · DEEP picks + DEEP_LOG

**Protocol budget: N = 4** (2 continuous + 2 rotating), read from `pipeline/protocols/industry_us.md`.
**OW set after §2 deltas: `HLTH` · `ENRG` · `COMM`** — three sectors.

**Recency, from actual DEEP files on disk** (⚠ **not** from DEEP_LOG lines): the 08-28 run logged
`continuous=[HLTH, MATR] rotating=[ENRG, UTIL]` but **produced no `SECTOR_DEEP_*` file at all** — it
terminated between ROTATION and PREMORTEM (HANDOVER §1b). **A logged slot is not coverage**, so
recency below is computed from files:

| sector | last actual `SECTOR_DEEP_*` file |
|---|---|
| `ENRG` · `HLTH` | 2026-08-27 (and 08-24/25/26) |
| `INDU` · `DISC` · `STPL` | 2026-08-27 |
| `FIN` · `RE` | 2026-08-26 |
| `IT` · `MATR` | 2026-08-25 |
| **`COMM`** | **2026-08-24 — 3 runs ago, the least recent of any OW sector** |
| `UTIL` | 2026-08-02 |

**① Continuous ⌈4/2⌉ = 2** — today's top OW ranks, by `eqflow`:
- **`HLTH`** (+0.102, rank 1). ★ **Anti-thrash continuity applies and is stated**: HLTH held a
  continuous slot in the previous run **and** is still top-N OW today ⇒ **it KEEPS the slot.**
- **`ENRG`** (+0.092, rank 2). Takes the slot `MATR` vacated — `MATR` is not OW after §2's declined
  promotion.

**② Rotating ⌊4/2⌋ = 2 — only 1 filled:**
- **`COMM`** (rank 3 OW, last covered **2026-08-24 = 3 runs ago**). Qualifies on both legs of the rule.
- **Slot 4: DELIBERATELY UNFILLED.** No OW sector remains. The rule says *"never pad with Neutral/UW
  to reach N — fewer is fine if stated."*
  🚫 **The pad I considered and rejected**: giving the 4th slot to **`FIN`**, whose contradiction is
  the sharpest unresolved item on the board. **Rejected because it would be reverse-engineering the
  slot count** — `FIN` was demoted to `N` four lines above, and promoting a sector into a DEEP slot to
  fill a budget is exactly the gut-selection the rule forbids. **It goes to PREMORTEM instead** (§4).
  ⚠ **This is not a cut to N.** The protocol's budget line (N=4, unchanged 2026-07-31, and a cut
  "needs its own measurement first") governs the **budget**; this run under-fills it by one and the
  budget is untouched.

**Mandates handed to DEEP** — each sector gets the question its delta created, not a blank map:

| sector | slot | mandate — the one question the DEEP must answer |
|---|---|---|
| **`HLTH`** | continuous | **The board's best money-flow breadth (`eqflow` +0.102) sits under the board's worst 5-day return (`exc5` −2.456pp vs `SPY`). Early, or trap?** the six leaders carry `OBV 매집` **together with positive `rs20` (+5.4 to +11.3)** — **RULE D6**, the C-grade OBV read is paired, never alone. ⚠ `MRK`, the sector's only 🟢 on 08-26, **trades ABOVE its mean target (upside −4.4%)** ⇒ `L2` applies to the one green. And `LLY` — the flipper that owns the sector's `wflow` sign — got an **FDA approval for Mounjaro CV-risk reduction** on 08-28 (7 outlets) |
| **`ENRG`** | continuous | **`XOM` alone carries the sector negative (`wflow` −0.051 vs `wflow_ex_top1` +0.168). Is the sector the refiners?** ⚠ **`R89` is retracted and its successor `P83` FIRED-B — the desk has NO surviving instrument separating refining margin from the barrel.** The DEEP may **not** re-assert separation; it must either build a new instrument or state the claim is unavailable. Live contest: `P112` (Hormuz reopening vs Qatar LNG force majeure) with **Venezuela as its VOID at 14 outlets** |
| **`COMM`** | rotating | **The board's best settled tape on BOTH windows produces ZERO shortlist names.** `SWEEP_READ §5` diagnoses the zero as a `vol_surge` filter artifact (`WBD` +0.56 / `DIS` +0.59 / `CMCSA` +0.39 / `META` +0.29 all OBV 매집, all `vol_surge` < 1.00). **Is there a name here, or is the sector's `exc1` +1.645pp one index-level print?** ⚠ `GOOGL` — the sector's `top1` — is the only negative-flow name in it (−0.322) |

## DEEP_LOG 2026-08-29: continuous=[HLTH, ENRG] rotating=[COMM] · N=3/4 filled, 4th slot deliberately unfilled (no OW sector remained; padding with Neutral/UW declined per rule) · **OW sectors WITHOUT a DEEP slot this run: none — all 3 OW sectors got one** · **verdict deltas 4: HLTH N→OW · ENRG N→OW · DISC N→UW · FIN OW−→N, every one carried by `eqflow` (non-cap-weighted) and none by a `wflow` on a flipper bucket** · **flip list 4 of 11 — IT/`NVDA`, HLTH/`LLY`, ENRG/`XOM`, DISC/`AMZN` — and it GREW 2→4 versus PREFLIGHT's baseline when only the terminal bar moved intraday→settled (`M1061`, `R108`'s class measured on the US desk)** · **4 moves declined with numbers: IT N→OW (three admissible numbers, three different signs — `eqflow` +0.060 / `wflow_ex_top1` −0.121 / tape worst-1d-best-5d), COMM OW→N (`eqflow` −0.004 ≈ flat cannot carry a demotion), MATR UW→N (`wflow` +0.028 is the only positive but `eqflow` −0.020 and G5 makes `eqflow` citable), INDU UW−→UW (declined ON METHOD — the only argument was a macro re-argument)** · **`n_axes` 3, `vel_coverage` 0.0% ⇒ zero deltas cite freshness or velocity; `asof` 2026-08-27 settled after a phantom-bar truncation (`M1059`); zero deltas cite Δflow (`D401`)** · **the structural line: `eqflow` is positive in exactly 3 of 11 sectors and all three are flippers** · previous-run recency read from **files on disk, not from DEEP_LOG lines** — the 08-28 run logged 4 slots and produced 0 DEEP files

## §4 · Handed to PREMORTEM, not resolved here

1. 🚨 **The Financials contradiction.** `exc5` **+0.605pp vs `SPY`** (positive, 2nd-best on the board)
   against `wflow` **−0.144** and `eqflow` **−0.144** (identical, both negative, **no flipper to blame**).
   Every other contradiction on the board has an instrument defect available; **this one does not.**
   EVENT_ALPHA Card 8 offers a hypothesis (a take-private premium unwinding — `PYPL` `rs60` **+36.5**
   built on an offer that was withdrawn 08-28), **named as a hypothesis and not adopted.**
2. **The `IT` window-dependence.** `P113` (\|`XLK` 5d − `XLU` 5d\|, state **1.39pp**, branch B at
   ≤1.00pp) is the registered decider and it sits **0.39pp from the informative branch.**
3. **`AVGO` prints 2026-09-02 (D-4)** carrying the **worst `rs60` on the book (−24.4)**, `S127` armed
   with **hand-set** bands, and **`D295` (re-derive from the straddle) unmet for a 4th run.**
4. **6 of 11 held names are covered by no EVENT_ALPHA card** (`M1064`), and one of them is `AVGO`.

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, verbatim from MACRO §D. No unchanged sector gets a row, paragraph, or restated flow number — the four unchanged `UW`s are named in a single clause.
- [x] **Every §2 delta cites a flow number** (`eqflow` on all four). One attempted change (`INDU`) rested only on a macro argument and was **reverted to MACRO's verdict and logged as "declined ON METHOD"**.
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** All three flipper-bucket deltas (HLTH, ENRG, DISC) are made on **`eqflow`, which is not cap-weighted**, and say so inline; `IT`'s attempted promotion was **declined**. **The flip list is reproduced in full even though it changed nothing on its own** — and this run it also **grew 2→4**, which is reported rather than absorbed.
- [x] **The axis count is stated** (`n_axes` 3, `vel_coverage` 0.0%) and **no delta cites theme freshness or news velocity**; no delta cites Δflow (`D401`).
- [x] DEEP picks selected by the written rule, not by gut: continuous by top-OW `eqflow` rank with anti-thrash continuity **stated** (HLTH keeps its slot), rotating by least-recent OW coverage **read from files, not from DEEP_LOG**. The unfilled 4th slot and the specific pad that was rejected are both logged.
- [x] `DEEP_LOG` line appended with slots, the unfilled slot, OW-sectors-without-a-slot (**none**), the deltas, the declines, and the instrument state.
