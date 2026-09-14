# SECTOR_ROTATION — industry_US · 2026-08-21 (Fri) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO §G owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers.
> Both are on disk. This file writes **only what changes and why**, plus the DEEP picks.
> Settled bar **2026-08-20** · **`§scoring.n_axes` = 3 (`nonews`)** ⇒ **no delta below cites theme
> freshness or news velocity** (`G1`). Δ spans **one session (08-19 → 08-20)**.

## §1 · Inherited — one line, verbatim from MACRO §G

**MACRO holds: ENRG OW · HLTH OW · MATR N · STPL N · COMM N · DISC N · RE N− · FIN N− · INDU UW− ·
UTIL UW · IT UW.**

## §2 · Deltas — **ZERO verdict changes**, and the zero was produced by six attempts declined with numbers

### 2a · Flip list, reproduced in full even though it changes nothing

`top1_flips_sign` — **1 of 11**:

| Sector | `wflow` | `ex_top1` | top1 | weight | flips? |
|---|---:|---:|---|---:|---|
| **Communication Services** | **+0.090** | **−0.010** | `GOOGL` | **38.3%** | 🚨 **YES** |
| Energy · Health Care · Staples · Discretionary · Materials · Financials · Industrials · IT · Real Estate · Utilities | — | — | — | — | **no (10 of 11)** |

🚨 **`D297` reproduces and is not fixed**: `GOOG` is a **separate row in the same bucket at the same
38.3%**, so the Alphabet complex is **76.6%** of Communication Services while `top1_w` reports half of
it. **No verdict moves on COMM today either way**, but the guard could not have caught a two-class
flip. Scope re-measured: still exactly one dual-class pair in `us_top300`.

### 2b · Attempts considered and DECLINED, each with the number

| Attempt | Flow evidence | Verdict |
|---|---|---|
| **MATR `N` → back to `N−`** (revert MACRO's promotion) | `eqflow` **−0.010** · **0🟢/2🔴** · breadth **0.00**. `SWEEP_READ §2` calls it CONTRADICTED, and it is | 🚫 **DECLINED — not because the flow disagrees, but because MACRO made the promotion WITH that number printed in the same line.** Reverting inside one run on evidence the promoting stage already weighed is thrash, not a delta. ⇒ **held at `N`, and the contradiction becomes MATR's #1 DEEP question** |
| **RE `N−` → back to `UW`** | `eqflow` **−0.231** (rank 10 of 11) · **0🟢/4🔴** · breadth **0.00**, against exc5 +1.876 (rank 4) | 🚫 **DECLINED for the same reason, and the contradiction is sharper here than in Materials.** ⇒ **held at `N−`, and it becomes RE's #1 DEEP question** |
| **COMM `N` → `N+`** | `eqflow` **+0.151 = rank 3 of 11** (not cap-weighted, flipper-immune) — but **breadth 0.00, 0🟢 of 12**, and `wflow` is flipper-owned | 🚫 **DECLINED.** The two admissible axes disagree with each other; **a promotion on the higher of two contradictory numbers is a choice, not a reading** (`C5`). ⚠ And per `G3` the third axis is unusable |
| **DISC `N` → `N+`** | `eqflow` **+0.107 = rank 4** · Δ **+0.243 = 3rd largest on the board** | 🚫 **DECLINED — `D293` bars a Δ-only verdict**, and the non-Δ leg is **breadth 0.00, 0🟢/2🔴** |
| **INDU `UW−` → `UW`** | `eqflow` **−0.212** (rank 9) · **0🟢 / 13🔴 of 50 = the largest red count on the board after IT** | 🚫 **DECLINED, and the reason is `W5`, not the number.** The desk's actual Industrials position is **defense**, whose OBV is 매집 at all four names (`RTX`·`LMT`·`NOC`·`GD`). **Demoting the label demotes something the desk does not own.** The label-vs-sub-node mismatch is logged, not resolved here |
| **IT `UW` → lower** | `eqflow` **−0.208**, **21🔴 of 56** — worst absolute red count | 🚫 **DECLINED — no notch below `UW` exists** on this desk's scale. Routed to the standing `P79` bracket instead |

★ **Two of the six declines are declines of this run's OWN promotions**, and that is stated plainly:
**MACRO promoted Materials and Real Estate one notch each today, and the flow axis contradicts both.**
Rather than oscillate inside a single run, **both keep MACRO's level and both become DEEP mandates** —
which is the only mechanism this protocol has for turning a disagreement into a measurement.

### 2c · One structural item that is NOT a delta and must not be read as one

🚨 **`MSTR` (Information Technology, new-🟢, Δ +0.601) and `COIN` (Financials, new-🟢, Δ +0.873 = the
board's largest) are ONE risk unit wearing two GICS labels** — both are bitcoin beta, and the day's #6
head event is *"Bitcoin rockets past $71,000"* (43 articles / 11 outlets). **Counting them as two
sector ignitions would promote IT and Financials on the same trade** (`W5`). **Neither sector is
promoted on them.** ⚠ Both also carry **negative rs60** (−31.3 / −5.9) — a reversal off a losing base,
not a continuation — and `COIN`'s FINRA z is **+2.20 crowded-short**, which is turn-conditional squeeze
fuel and never a buy signal alone (`D6`). Source: `EVENT_ALPHA` card §4.

⚠ **`R81` enforced across this stage**: the board's 3 greens (`MSTR` · `TGT` · `MRVL`) and the 7-name
shortlist are **not used as evidence for any verdict above**. Measured this run: **3 of the 7
shortlist tags are velocity-derived** (`MRVL` `vol_surge` 0.77 · `MA` 0.87 · `CVX` 0.94), i.e. they
rest on the axis `G1` revoked. ⇒ **the admissible green count is 4, not 7.**

⚠ **`M144`/`D270` replicates for a TENTH measurement**: **92 names pass `OBV 매집 ∧ rs20 > 0`; 7 are
🟢; 85 are blocked and 100% of them by `vol_surge` < 1.2 alone.** **18 names clear `vol_surge` ≥ 1.2
and 14 of them are 🟡/🔴.** The gate is not selecting on flow.

---

## §3 · DEEP picks and DEEP_LOG — **N = 4** (protocol budget: 2 continuous + 2 rotating)

### 3a · Continuous ⌈N/2⌉ = 2 — **ENRG · HLTH**, both by the anti-thrash continuity rule

Both held a continuous slot in the 08-20 run **and** are still the board's top-2 OW today
(ENRG rank 1 on `eqflow` **+0.160** and on exc5 **+6.370**; HLTH rank 2 on both, `eqflow` **+0.159**,
exc5 **+4.346**). **The rule keeps the slot; it is not re-argued.**

| Sector | The #1 question this DEEP must resolve |
|---|---|
| **ENRG** | 🚨 **`P70`'s control leg FAILED.** The registered separator was *"the refiners pay **without** the barrel"*, enforced by `BZ=F 5d ≤ +2.0%`; measured **+7.71%**. ⇒ **this week the refiner excess (`EW{MPC,VLO,PSX}` exc5 +3.060) cannot be separated from crude beta by the desk's own instrument.** DEEP must (i) test the successor separator — the **distillate−gasoline spread, 51.13 $/bbl at the 08-20 settle**, distillate crack **100.34 = 98.4th %ile** vs gasoline **49.21** (`P83`); (ii) resolve **`PSX`'s FINRA z +1.95 🔴, 5v5 +13.5▲** against `MPC` −0.52 and `VLO` +0.49 — three names, one thesis, and the B-grade axis has stopped agreeing (`D6`); (iii) fold in `EVENT_ALPHA` card §2's **third mechanism** (Jazan refinery closed since end-July, Red Sea re-routing) which a Hormuz de-escalation cannot falsify |
| **HLTH** | **`S82` FIRED-A on 08-20 — the sector decoupled UPWARD out of the duration complex**, so the OW's premise changed from *"a duration leg"* to *"idiosyncratic"* and has not been re-derived since. DEEP must ask what the idiosyncratic driver actually is, given **breadth 0.03 and 1🟢/3🔴 under a rank-2 `eqflow`** — thin flow beneath a strong price. ⚠ **`MRK` was filed to the missed ledger this run** (`M.숏리스트탈락`, flow **+0.894 = board #2**, `vol_surge` **1.41** — one of only four greens clearing the volume bar on its own); **its `--enters-if` names this DEEP slot explicitly**, so this DEEP either closes that row or leaves it open on the record |

### 3b · Rotating ⌊N/2⌋ = 2 — **MATR · RE**, and the selection rule is a DECLARED deviation for an 8th run

**The rule as written cannot execute.** Rotating slots go to *"the next-highest OW not deep-dived in
the last ~3 runs"* — **there are only two OW sectors and both took continuous slots.** Fallback per
the documented 08-15/16/17/19/20 practice: **fill from non-OW by evidence density, recency as
tiebreak.** **Declared, 8th consecutive run.**

| Sector | Last covered | Evidence density today |
|---|---|---|
| **MATR** ✅ selected | 08-19 | **This run's own promotion, contradicted by flow** (`eqflow` −0.010, breadth 0.00) · **`NUE` is held and its carried FINRA line inverted this run** (z +1.99 → **−2.33**, short covering) · **`S89` (`NEM`) settles TONIGHT already inside branch B (+10.160 vs +9.658)** with its anti-signal 2.1pp from firing · `EVENT_ALPHA` card §5 gives the sector a **non-steel** driver |
| **RE** ✅ selected | **08-15 (5 runs)** | **This run's own promotion, contradicted harder** (`eqflow` −0.231 = rank 10, 0🟢/4🔴, against exc5 +1.876 = rank 4) · `S90` (`DLR`) settles tonight at **−1.153**, inside C · `DLR` is `EVENT_ALPHA` card §1's **most rate-sensitive layer** and its FINRA 5v5 is **+9.0▲** · **best recency of the four candidates** |
| **FIN** ❌ not selected | **08-14 — least recent on the board, ~6 runs** | `eqflow` −0.097 (rank 7), 2🟢/8🔴; `COIN`'s new-🟢 is **crypto beta, not a Financials signal** (§2c); `KKR`·`NDAQ`·`MET` held. **Real mandate, but no dated settle and no self-made promotion to resolve.** 🚨 **The recency cost is logged and it is now the largest on the board** |
| **INDU** ❌ not selected | 08-19 | 🚨 **The highest-information single item on the board is here**: **`S99`'s pre-settle meets ALL THREE of branch A's conditions** (`M` = EW{ANET,AVGO,HPE} exc5 **−6.517**, `E` = `ETN` exc5 **−6.252**, same sign, both far beyond their gates) ⇒ **`ETN` may be a 5th AI-compute risk unit and the book's concentration reads 5-of-12, not 4-of-12.** Plus the **defense short-axis group turn** (`NOC` +2.43 · `LMT` +1.76 · `LHX` +1.35 against OBV 매집 at all three — **RULE D6 exemption: the C-grade OBV reading is not carrying anything here; it is the thing the B-grade FINRA axis is cited AGAINST, which is what D6 asks for**) and **`S97` already inside branch A**. ⇒ **Routed to PREMORTEM as a 5th-slot candidate** rather than dropped — PREMORTEM is the stage that can promote one, and this is exactly the class of finding it exists for |

**Never padded**: no Neutral/UW sector was added to reach N. N = **4/4** filled.

> **RULE D6 — exemption stated for the table above.** `report_lint` flags the string "OBV 매집" in the
> INDU row as a lone C-grade citation. It is **not** alone: the same clause pairs it with the **B-grade
> FINRA short-vol axis** (`NOC` **+2.43** · `LMT` **+1.76** · `LHX` **+1.35**, settled 08-20) and the
> sentence's whole point is that **the two axes DISAGREE** — the B-grade one is cited *against* the
> C-grade one, which is exactly what `D6` asks for. The same applies to the ENRG row (`PSX` z **+1.95**
> against OBV 매집). **No proposition in this file rests on OBV alone.**

### 3c · Value-chain reference for the two rotating slots (L2 · deepdive)

⚠ **`module_industry_map` is a KR-corpus tool** (`data/corp_embeddings.db` is Korean) and is **not
called for a US sector**; the US analogue is `chain-hop`. Run for both mandates, `--days 14`,
`--scope foreign`:

- **`chain-hop distillate refinery`** (911 articles scanned) — headline-named, i.e. **already crowded**:
  `XOM` 9 · `PSX` 9 · `CVX` 6 · `VLO` 4 · `MPC` 3 · `DAL` 3 (the customer leg `M34` established).
  **The refining node is fully named; there is no un-named beneficiary to find here**, which is itself
  the answer to *"is this crowded?"*
- **`chain-hop gold mining`** (1,500 articles scanned) — 🚨 **the candidate list is
  ticker-collision noise and is NOT used.** Its top "unnamed" rows are `XYZ`, `NFLX`, `META`, `SNDK`,
  `SPGI` — and the example articles beside them are *Royal Gold*, *Wheaton Precious Metals*,
  *Metalla Royalty*, *Hecla Mining*, *Fortuna Mining*, *Barrick*. ⇒ **the real gold chain is
  ENTIRELY outside `us_top300`.** Verified against the universe: **Materials has 12 names and exactly
  ONE is classified `Gold` (`NEM`)**; the others are 2 Industrial Gases, 2 Specialty Chemicals,
  3 Construction Materials, **2 Steel**, 1 Copper, 1 Fertilizers.
  ★ **That is the MATR DEEP's real constraint, stated up front**: *the desk's Materials exposure to the
  week's live metals story is one ticker, and its instruments cannot see the chain behind it* — the
  same structural class as `FSLR`/solar (zero in-universe candidates, HANDOVER §3).
- Real Estate composition, for the RE DEEP's `W5` check: **12 names = 2 Data Center REITs
  (`EQIX`,`DLR`) · 2 Telecom Tower (`AMT`,`CCI`) · 2 Health Care (`WELL`,`VTR`) · 2 Retail (`SPG`,`O`)
  · 1 Industrial (`PLD`) · 1 Self-Storage (`PSA`) · 1 Other Specialized (`IRM`) · 1 Services (`CBRE`)**.
  ⚠ **`M131` already measured this bucket to be THREE risk units, not one** — the DEEP must not read
  `eqflow −0.231` as one object.

---

## DEEP_LOG 2026-08-21: continuous=[ENRG, HLTH] rotating=[MATR, RE] · N=4/4 · **ZERO verdict deltas — flow confirms MACRO's matrix on all 11, and the zero was produced by SIX attempts declined with numbers, TWO of which were declines of this run's OWN promotions** (MATR N→N− revert: `eqflow` −0.010 / breadth 0.00 / 0🟢2🔴 — declined as intra-run thrash, routed to DEEP · RE N−→UW revert: `eqflow` −0.231 rank 10 / 0🟢4🔴 — same, routed to DEEP · COMM→N+: `eqflow` +0.151 rank 3 vs breadth 0.00, two admissible axes contradict, `C5` · DISC→N+: Δ +0.243 is 2nd/3rd largest but `D293` bars Δ-only and breadth is 0.00 · INDU→UW: 0🟢/13🔴 but the desk's position is defense with OBV 매집 ×4, `W5` · IT→lower: no notch below UW exists) · **flip list 1 of 11 — Communication Services/`GOOGL`/38.3% (`wflow` +0.090 → `ex_top1` −0.010); yesterday's flipper Materials/`LIN` LEFT the set (+0.008 → +0.149, sign held)** · 🚨 **`D297` reproduces unfixed: `GOOG` is a second 38.3% row in the same bucket ⇒ the Alphabet complex is 76.6% of COMM while `top1_w` reports 38.3%** · **`M144`/`D270` replicated a TENTH time: 92 names pass `OBV 매집 ∧ rs20>0`, 7 are 🟢, 85 blocked and 100% of them on `vol_surge` alone; 18 clear `vol_surge ≥1.2` and 14 of those are 🟡/🔴** · **`R81`/`D290` replicated an ELEVENTH time: 3 of 7 greens are velocity-derived (`MRVL` 0.77 · `MA` 0.87 · `CVX` 0.94) ⇒ admissible green count 4, and `US_LIVE_SHORTLIST` is tag-filtered so 3 of its 7 rows are inadmissible** · **★ the run's structural headline is that BOTH of the board's new-🟢 ignitions are ONE risk unit in two GICS labels (`MSTR` IT Δ+0.601 · `COIN` FIN Δ+0.873 = board's largest, both bitcoin beta, both with NEGATIVE rs60 −31.3/−5.9, `COIN` crowded-short z +2.20) — neither sector promoted on them** · **★ and the run's largest un-taken mandate is `S99`: its pre-settle meets ALL THREE of branch A's conditions (M −6.517, E −6.252, same sign, both gates cleared) ⇒ `ETN` may be a 5th AI-compute risk unit and the book's concentration reads 5-of-12 not 4-of-12; G4 has failed 12 consecutive runs on exactly this grouping. ROUTED TO PREMORTEM as a 5th-slot candidate, not dropped** · **rotating slots are a DECLARED recency-starved deviation for an 8th run: only 2 OW exist and both took continuous slots, so R1/R2 were filled from non-OW by evidence density with recency as tiebreak** · **★ MATR's DEEP carries a structural constraint found this run: the gold chain is ENTIRELY outside `us_top300` (`chain-hop gold mining` returns ticker-collision noise — XYZ/NFLX/META/SNDK against example articles naming Royal Gold, Wheaton, Metalla, Hecla, Fortuna, Barrick), and Materials holds exactly ONE `Gold` row (`NEM`) of 12 — the `FSLR`/solar class** · **uncovered=[FIN(N−, **08-14 = least recent on the board, ~6 runs**, `eqflow` −0.097 rank 7, 2🟢/8🔴, `KKR`·`NDAQ`·`MET` held, `COIN`'s green is crypto beta not a FIN signal — the recency cost is now the board's largest and is logged as a cost, not a pass), INDU(UW−, 08-19, **`S99` branch-A pre-settle + the defense short-axis group turn `NOC` +2.43/`LMT` +1.76/`LHX` +1.35 against OBV 매집 ×3 + `S97` already inside branch A** — routed to PREMORTEM), COMM(N, 08-19, `T` orphan at 9.74% of real invested for a 4th run, two admissible axes contradict), STPL(N, 08-17, `S100` settles tonight; `TGT`'s beat contains **$1.65 of $4.11 = 40.1% tariff refund** vs `WMT` −9.15% on the print — `P84` carries it to 09-03), DISC(N, 08-15 = 6 runs, `eqflow` +0.107 rank 4 with breadth 0.00), IT(UW, 08-20, `P79` settles 08-25 at −7.178 = 0.54pp from branch B), UTIL(UW, 08-20, worst flow on the board for a 2nd run — `eqflow` −0.606, 0🟢/12🔴 — and `P78`'s strongest single row)]**

---

## ✅ EXIT CHECK — self-audit

- [x] **§1 is ONE line**, inherited verbatim from MACRO §G. No unchanged sector gets a row, paragraph
      or restated flow number.
- [x] **Every §2 attempt cites a flow number**, and the two attempts that rested on a macro re-argument
      were not made at all. **Zero verdict changes; six declines, each with its number.**
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** COMM is the only flipper and
      its promotion attempt was **declined**; the flip list is reproduced in full (§2a) even though it
      changes nothing.
- [x] **Axis count stated**: `§scoring.n_axes` = **3 (`nonews`)**, `vel_coverage` 16.72% ⇒ **no delta
      cites theme freshness or news velocity**, and the 3 velocity-derived greens are named as
      inadmissible.
- [x] **DEEP picks by rule, not by gut**: continuous = the two top-OW sectors, both protected by the
      anti-thrash continuity clause; rotating = a **declared** recency-starved deviation, filled by
      evidence density with recency as tiebreak, and the two un-selected candidates (**FIN**, **INDU**)
      are named with their mandates and their costs.
- [x] **N = 4/4, never padded** with a Neutral/UW sector to reach the number.
- [x] **All seven un-covered sectors named with last-covered date and mandate** (DEEP_LOG).
- [x] **DEEP_LOG line appended** for the next run's recency rule.
- [x] `report_lint` run below.
