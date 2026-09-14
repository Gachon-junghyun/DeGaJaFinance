# SECTOR_ROTATION — industry_US · 2026-08-22 (Sat) · Stage 6 / L1·ROTATION

> **Delta-only.** MACRO owns the 11-sector verdict; `SECTOR_FLOW_US.json` owns the flow numbers. Both
> are on disk. This file writes **only what changes and why**, plus the DEEP picks.
> Flow `asof` **2026-08-21** settled. `exc5` = 5-session excess vs **`SPY` (−1.368%)**, named inline
> (`C1`). **No sizing, no buy/sell language (P4).**

## §1 · Inherited — one line, verbatim from `MACRO_REPORT §E`

`MACRO holds: HLTH OW · ENRG OW · MATR N+ · STPL N · DISC N · COMM N · FIN N− · RE UW · INDU UW− · UTIL UW · IT UW`

## §2 · Deltas — **1 verdict change from 7 attempts**

| Sector | Matrix said | Flow evidence (`eqflow` · breadth · 🟢/🔴 · `exc5` · Δ) | New verdict | Who resolves |
|---|---|---|---|---|
| **Real Estate** | UW *(already moved by MACRO from the 08-21 N−)* | `eqflow` **−0.446 rank 10 of 11** · breadth **0.00** · **0🟢 / 6🔴 of 12** · `exc5` **+0.948 rank 6** · `DLR` Δ **−1.083, the largest single-session deterioration on all 299 names** | **UW — confirmed, not re-argued** | resolved by a **scored bracket**: `S90` **FIRED-A** (`DLR` exc5 **−3.393** ≤ p15 −3.199), the registered falsifier of the 08-21 price-only promotion |

★ **The one change on this board was made by a pre-registered bracket settling against the desk's own
prior promotion, not by a fresh reading.** The 08-21 run promoted RE to N− *"only on price"* and said so
in writing; `S90` was registered on 08-15 to falsify exactly that; it fired A. **That is the process
working, and it is the reason this file is one row long instead of eleven.**

⚠ **And the sub-node split is measured, so the UW is not applied blind** (`W5`): `DLR` **−3.393** ·
`EQIX` **−1.963** · `IRM` **−4.357** against `AMT` **+1.493** · `PLD` **+1.914** · `WELL` **+2.939** ·
`XLRE` **+0.948**. **The digital-infrastructure third of the sector fell; the rest rose.** The UW is a
sector verdict; the mechanism is a sub-node one, and DEEP does not own RE this run (covered 08-21).

### §2b · Attempts DECLINED, with the number that declined them — **7**

| Attempt | Declined because |
|---|---|
| **MATR N+ → OW** | `eqflow` **+0.046 rank 5**, breadth 0.08 (1🟢 `ECL` of 12). The price rank (3rd, `exc5` +3.271) is carried by **two commodities**: `NEM` fired `S89`-**B** but **`M779` puts 246.4% of its rs60 in the last 20 sessions** (days 21–60 negative), and **Copper spec is at the 100th %ile** `[COT 08-18]`. **A promotion on a 5th-ranked `eqflow` would be a price argument wearing a flow label** |
| **ENRG OW → OW+** | breadth **0.00 — zero greens of 16** (it was 1🟢 on 08-21), and `P70` **MISSED** on its control leg (`BZ=F` 5d **+6.631%** vs a ≤ +2.0% bar). ⚠ The zero is a `vol_surge` artifact (`SWEEP_READ §3`) and is **not** cited as evidence against Energy — but neither can it support a promotion |
| **DISC N → N+** | `eqflow` **+0.103 rank 2** — the strongest case on the board — **against breadth 0.00 of 28.** A sector can be broadly mildly positive and have **not one name clear the 3-axis gate**; that is a description, not a promotion. ⚠ And `S91`, the row registered to test precisely this, **VOIDed** today |
| **IT UW → N−** | `eqflow` **−0.102 rank 8** *is* better than its price (`exc5` −2.158, rank 11), and `eqflow − wflow` **+0.129** is the widest positive gap on the board ⇒ mega-cap-led weakness. **But `Nasdaq-100` spec at the 4th %ile is positioning — context, not a trigger (`D6`)** — and `P79` at **−5.609** has moved *away* from its own branch B. **Routed to DEEP-adjacent, not promoted** |
| **FIN N− → N** | `exc5` **+0.199** (positive) and `eqflow` **−0.034 rank 7** (mid, not bottom). **Declined on composition**: the sector's **only green of 47 is `COIN`**, which is bitcoin beta, not a bank signal — the same `MSTR`/`COIN` one-risk-unit-two-labels finding the 08-21 run made. **Made FIN's #1 DEEP question instead** |
| **STPL N → any notch** | 🚨 **Flipper-blocked.** `WMT` is **28.9%** of the bucket and `wflow` **−0.013 → ex-top1 +0.116** ⇒ `top1_flips_sign = true`. Per the rule, **neither a promotion nor a demotion may rest on this bucket.** `eqflow` **+0.048** and breadth 0.05 (1🟢 `TGT`) are the admissible axes and they are unremarkable. **Left where MACRO put it** |
| **HLTH OW → lower** | breadth **0.03 — `MRK` alone of 32** is thin under a rank-1 price. **Declined**: rank 1 on **both** axes (`exc5` +5.700, `eqflow` +0.229) and `S82` fired A with a named, dated driver (`M776`). **The thinness is HLTH's DEEP question, not a demotion** |

★ **Zero of the seven was declined by inertia.** Each carries the number that stopped it, and **two
(MATR, ENRG) are declines of positions MACRO itself ranked in the top three today.**

### §2c · Flip list, reproduced in full — **1 of 11**

| Sector | `wflow` | `ex_top1` | top1 | weight | flips? |
|---|---|---|---|---|---|
| **Consumer Staples** | **−0.013** | **+0.116** | **`WMT`** | **28.9%** | **🚨 YES** |
| Health Care | +0.196 | +0.205 | LLY | 19.4% | no |
| Consumer Discretionary | +0.122 | +0.254 | AMZN | 40.2% | no |
| Communication Services | +0.108 | +0.022 | GOOGL | 38.3% | no |
| Energy | +0.076 | +0.189 | XOM | 30.5% | no |
| Materials | +0.064 | +0.201 | LIN | 24.7% | no |
| Financials | +0.003 | +0.034 | BRK-B | 13.9% | no |
| Information Technology | −0.231 | −0.243 | NVDA | 19.4% | no |
| Industrials | −0.259 | −0.218 | CAT | 8.7% | no |
| Real Estate | −0.543 | −0.491 | WELL | 16.9% | no |
| Utilities | −0.648 | −0.659 | NEE | 17.7% | no |

**Yesterday's flipper (Communication Services / `GOOGL`) has LEFT the set** — it holds its sign today
(+0.108 → +0.022, positive but thin). 🚨 **`D297` reproduces unfixed**: `GOOG` is a second **38.3%** row
in the same bucket, so the Alphabet complex is **76.6%** of COMM while `top1_w` reports half. **No
verdict moved on COMM either way today, so the defect cost nothing this run — but the guard still could
not have caught a flip.**

### §2d · Instrument replications this run

- **`M144`/`D270` — the 🟢 gate is a volume gate, 12th measurement and the cleanest yet.** **94** names
  pass `OBV 매집 ∧ rs20 > 0 vs SPY`; **6** are 🟢; **88 blocked, 100% of them on `vol_surge` alone.**
  22 names clear `vol_surge ≥ 1.2` and **16 of those are 🟡/🔴**.
- ★ **`R81`/`D290` — first run in the series with NOTHING to replicate.** All 299 velocities are `null`,
  so **0 of 6 greens are velocity-derived** and **the admissible green count equals the printed green
  count (6 = 6)** for the first time. `US_LIVE_SHORTLIST`'s 6 rows are **all admissible**. ⚠ The rule is
  not retired; it re-binds the moment a run gets partial coverage again.
- ⚠ **`module_industry_map` is not a US instrument and this run stopped rather than misuse it.** Probed
  with `data center power`: the tool itself printed *"시드가 전부 영문입니다 — `corp_embeddings.db` 는
  KR 사업보고서 코퍼스라 영문 시드는 0히트가 정상입니다 … US 가치사슬 발굴은 `scripts/chain_hop.py`
  를 쓰세요"* and returned an empty pool. **The guard works; the L2's reference call is a KR-only
  capability and is recorded as such rather than as a zero.**

## §3 · DEEP picks — **N = 4** (protocol budget: 2 continuous + 2 rotating)

### Continuous ⌈N/2⌉ = 2 — **ENRG, HLTH** (both KEEP their slots)

Anti-thrash continuity applies: both held a continuous slot on 08-21 **and** are still the board's only
two OW ranks today (`exc5` ranks 1–2, `eqflow` ranks 1 and 3). **Slots kept, stated.**

| Sector | The #1 question DEEP must resolve |
|---|---|
| **ENRG** | 🚨 **Can a node hold a 100th-percentile expression while its own narrative decelerates?** `BZ=F` **94.39** (window high, `S95`/`P69` both FIRED-A) · `theme-age Hormuz` **0.80× DECELERATING on 141.9 articles/day** · WTI spec **36th %ile** · breadth **0.00 of 16** with the four best names **all blocked by `vol_surge` alone**. **And `P70` MISSED on the barrel control**, so the separation claim is withdrawn (`R89`) while the thesis is not. **`P89` and `P83` both settle inside DEEP's horizon** |
| **HLTH** | **Rank 1 on both axes with breadth 0.03 — is the flow one name?** `MRK` is the sector's only green of 32 (flow +0.978, obv **+0.370**, rs60 +24.8). `S82` FIRED-A with a dated driver (`M776`: the Moderna/Merck Phase-3 mRNA result, 08-19, `XLV` +3.51% that session). **DEEP must separate "a sector decoupled" from "one trial result"** |

### Rotating ⌊N/2⌋ = 2 — **FIN, INDU** · ⚠ **declared recency-starved deviation, 9th consecutive run**

**The deviation, stated rather than hidden.** The rule wants the next-highest **OW** not covered in ~3
runs. **The board has exactly two OW ranks and both took continuous slots.** MATR (N+) is the only other
positive rank and it was **covered 08-21, one run ago**. ⇒ R1/R2 are filled from non-OW by evidence
density, with **least-recently-covered as the tiebreak**, exactly as the previous eight runs did.

| Sector | Last DEEP | Runs since | Why it wins the slot |
|---|---|---|---|
| **FIN** | **2026-08-14** | **~7 — the largest recency cost on the board, and it was logged as a cost on 08-21 and not paid** | **Three things converge on it this run.** (a) `EVENT_ALPHA` **CARD 1** — US public debt crossed **$40tn on 08-19** and Treasury **doubled** its buyback; the BBH body-read says the operation *should* have flattened the curve and the realised 20 sessions **steepened** (`DGS30` +0.06 vs `DGS2` −0.18). A bank sector's P&L is a curve function and the desk has not looked in seven runs. (b) The sector's **only green of 47 is `COIN`** — crypto beta wearing a Financials label. (c) **Three book names live here** (`NDAQ`, `MET`, and `KKR` as a carried orphan), and **`MET` is `module_report_tags`-unindexable (`M152`)**, so its coverage cannot be reconciled by any other instrument |
| **INDU** | 2026-08-19 | ~3 | **A dated mandate arrived this morning that cannot wait.** `S97` **FIRED-A** — `LHX` exc5 **−7.230**, succession priced as a **discontinuity** — which means **`M704`'s defense EW must be re-run ex-`LHX`** before any defense claim is made, and **`RTX` is held**. Corroborating: `RTX` `obv_norm` **+0.023 — it has LEFT 매집** and its delta **−0.304** is the book's largest deterioration for a second run. Sector breadth **0.00 of 50**, `eqflow` −0.231. ⚠ And `M778` bars the easy escape: **`ETN`'s +0.285 delta belongs to `XLI` (β +1.402, t +6.12), not to AI-compute** |

**Not padded.** No Neutral/UW sector was added to reach N; both rotating slots are justified by
evidence density and both mandates are dated.

### §3b · The seven un-covered sectors — named with last-covered date and mandate

| Sector | Verdict | Last DEEP | The mandate that goes unpaid this run |
|---|---|---|---|
| **DISC** | N | **2026-08-15 (~7 runs, tied-worst recency)** | `eqflow` **+0.103 rank 2 with breadth 0.00 of 28** — an unresolved internal contradiction, and **`S91` VOIDed today**, so the row that would have tested it is gone. **This is now the board's largest un-tested contradiction** |
| **STPL** | N | 2026-08-17 | Flipper-blocked (`WMT` 28.9%). `TGT` **+8.463** vs `WMT` **−8.669** exc5 — a **17.1pp** intra-sector split (`W5`), and `S93` **VOIDed on a tariff clause that named both companies** |
| **COMM** | N | 2026-08-19 | `T` orphan at **9.74% of the real book's invested for a 5th run**, no cycle label, no card. `D297` unfixed (Alphabet complex 76.6%) |
| **MATR** | N+ | 2026-08-21 | `NEM`'s `S89`-B fired on **exhaustion geometry** (`M779` 246.4%); Copper spec **100th %ile**; **the gold chain is entirely outside `us_top300`** (08-21 finding, unfixed) |
| **RE** | **UW (changed today)** | 2026-08-21 | The verdict moved on `S90`; the **sub-node split** (`DLR`/`EQIX`/`IRM` down vs `AMT`/`PLD`/`WELL` up) is measured here and not deep-dived |
| **IT** | UW | 2026-08-20 | `P79` settles **08-25** at −5.609; `EVENT_ALPHA` **CARD 2** — an **$105bn `NVDA` guarantee** to OpenAI with **every power-chain name 🔴 or deeply negative** and the guarantor flat. **The largest story-vs-money mismatch on the board** |
| **UTIL** | UW | 2026-08-20 | Worst flow for a **third** run (`eqflow` −0.621, **0🟢/13🔴 of 15**) and still **`P78`'s strongest single row**. ⚠ **`C12` carried unresolved**: the desk has no mechanism for it |

## DEEP_LOG 2026-08-22: continuous=[ENRG, HLTH] rotating=[FIN, INDU] · N=4/4 · **ONE verdict delta (RE N− → UW) from SEVEN attempts declined with numbers, and the delta was produced by a PRE-REGISTERED BRACKET settling against this desk's own prior promotion (`S90` FIRED-A, `DLR` exc5 −3.393 ≤ p15 −3.199) rather than by a fresh reading — two of the seven declines (MATR, ENRG) were declines of sectors MACRO ranks in today's top three** · **flip list 1 of 11 — Consumer Staples/`WMT`/28.9% (`wflow` −0.013 → `ex_top1` +0.116); yesterday's flipper Communication Services/`GOOGL` LEFT the set (+0.108 → +0.022, sign held)** · 🚨 **`D297` reproduces unfixed (`GOOG` a second 38.3% row ⇒ Alphabet complex 76.6% of COMM) — cost nothing this run because COMM did not move** · **`M144`/`D270` replicated a TWELFTH time: 94 names pass `OBV 매집 ∧ rs20>0 vs SPY`, 6 are 🟢, 88 blocked and 100% of them on `vol_surge` alone; 22 clear `vol_surge ≥1.2` and 16 of those are 🟡/🔴** · **★ `R81`/`D290` had NOTHING to replicate for the first time in the series — all 299 velocities `null` ⇒ 0 of 6 greens velocity-derived, admissible green count 6 = printed green count 6, and all 6 `US_LIVE_SHORTLIST` rows admissible; the rule is NOT retired, it re-binds on the next partial-coverage run** · **★★ the run's structural headline is a MACRO event absent from every desk instrument: US public debt crossed $40tn on 08-19 and Treasury DOUBLED its long-end buyback, `theme-age Bessent` 🟡ACCELERATING 3.01× on 1,310 articles — the fastest-accelerating named macro term of the week — while `catalyst_calendar` carries no row, the `thread` tag taxonomy filed it as FADING (weekend window-end artifact, `D312` upgraded), and the BBH body-read says the operation's own predicted effect was a FLATTENER while the realised 20 sessions STEEPENED (`DGS30` +0.06 / `DGS2` −0.18)** · **★★ and the second structural headline is a STORY-vs-MONEY mismatch at maximal size: `NVDA` is guaranteeing up to $105bn of OpenAI's Ohio data-centre leases (8-GW campus) and every power-chain name is 🔴 or deeply negative (`GEV` −0.741 · `CEG` −0.625 · `VRT` −0.539) while the guarantor itself is flat (`NVDA` −0.181, obv −0.024) — filed STORY-ONLY, no name handed to BET §B** · **⚠ `module_industry_map` is KR-corpus-only and its own guard said so on an English seed — recorded as a capability boundary, not a zero; `scripts/chain_hop.py` is the US instrument** · **rotating slots are a DECLARED recency-starved deviation for a NINTH run: only 2 OW exist and both took continuous slots, MATR (the only other positive rank) was covered 08-21 ⇒ R1/R2 filled from non-OW by evidence density with recency as tiebreak** · **uncovered=[DISC(N, **08-15 = ~7 runs, tied-worst recency**, `eqflow` +0.103 rank 2 vs breadth 0.00 of 28, and `S91` VOIDed today so the testing row is gone — the board's largest un-tested contradiction), STPL(N, 08-17, flipper-blocked, `TGT` +8.463 vs `WMT` −8.669 = 17.1pp intra-sector `W5`, `S93` VOIDed on a tariff clause naming both companies), COMM(N, 08-19, `T` orphan at 9.74% of real invested for a 5th run, `D297` unfixed), MATR(N+, 08-21, `NEM` `S89`-B fired on exhaustion geometry `M779` 246.4%, Copper spec 100th %ile, gold chain entirely outside `us_top300`), RE(**UW — changed today**, 08-21, sub-node split `DLR`/`EQIX`/`IRM` vs `AMT`/`PLD`/`WELL` measured but not deep-dived), IT(UW, 08-20, `P79` settles 08-25 at −5.609, and EVENT_ALPHA CARD 2's $105bn-vs-🔴-chain mismatch), UTIL(UW, 08-20, worst flow for a 3rd run 0🟢/13🔴, `P78`'s strongest row, `C12` still has no mechanism)]**

## ✅ EXIT CHECK
- [x] **§1 is ONE line**, inheriting MACRO's matrix verbatim. No unchanged sector gets a row, a
      paragraph, or a restated flow number.
- [x] **The single §2 delta cites flow numbers** (`eqflow` −0.446 rank 10 · breadth 0.00 · 0🟢/6🔴 ·
      `DLR` Δ −1.083) **and a scored bracket** (`S90` FIRED-A). **No change rests on a macro argument** —
      and the seven declines each name the number that declined them (§2b).
- [x] 🚨 **No promotion or demotion rests on a `top1_flips_sign` bucket.** Consumer Staples is the sole
      flipper and is explicitly **left where MACRO put it**, with `eqflow`/breadth cited as the
      admissible axes.
- [x] **Flip list reproduced in full — all 11 rows**, including the ten that do not flip (§2c).
- [x] **DEEP picks made by the rule, not by gut**: continuity stated for both continuous slots; the
      rotating slots are a **declared** recency-starved deviation (9th run) with the tiebreak named.
      **No padding** to reach N.
- [x] **All seven un-covered sectors named with last-covered date and the unpaid mandate** (§3b +
      DEEP_LOG) — so "we never looked" stays distinguishable from "we looked and passed".
- [x] **`DEEP_LOG` line appended** for the next run's recency rule.
- [x] Sweep `asof` **2026-08-21** stated; the US market has not traded since, so no same-day catalyst
      sits outside these numbers.
