

---

# Registered 2026-08-29 by the `industry_US` PREMORTEM — **`S131` – `S134`**

> ⚠ **Append-only write** (`D165`); text staged in
> `llm_outputs/2026-08-29/industry_US/_scenarios_us_block.md` first (`D357`), and both
> `SCENARIOS_US.md` and `SCENARIOS.md` backed up to `*.bak_0829us_premortem` before the write.
> ⚠ **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**` (excluding this
> run's own files): `S131` `S132` `S134` → **0 hits**. `S133` returned **1 apparent hit which was
> inspected and is a false positive** — the substring sits inside the FRED series id `MTSDS133FMS` in
> a 2026-08-28 KR company report. **Inspected rather than assumed** (`D94`). IDs issued by
> `module_evidence next-id S` (highest existing **`S130`**), not hand-grepped (`D76`).
> ⚠ **Language: English** — the US desk's documented practice.
> ⚠ **All spot prices settled 2026-08-28**, read via `fast_info.last_price` because `yf.download`
> returns `Close = NaN` on 300 of 301 US names for that session (`M1040`/`M1059`, `D402`).
> ⚠ **Implied moves read DIRECTLY from the option chain**, at the strike nearest the settled 08-28
> close on the first expiry **spanning** each event — because `module_flow --positioning` returned
> **`예상변동 ±nan%` on every ticker probed** (`M1065`) and, when it works, picks a **non-spanning**
> expiry (`D315`, 6th run). **No threshold was invented** (`M47`).
> ⚠ **SETTLEMENT MODE = TERMINAL on both branches** for all four (`D242`).
> ⚠ **`D388-KR` honoured**: the one basket row (`S133`) **enumerates its membership** inline.

## `S131` — ★★★ MSCI 08-31: does the passive print concentrate or broaden? · ARMED · → settle **2026-08-31**

**The mandatory ≤48h bracket.** `catalyst_calendar` puts the MSCI quarterly review at **D-2**, and
**six rows already settle 2026-08-31** (`S92` `S94` `S104` `S112` `S124` `S103`) — **not one observes
the rebalance itself.** A one-way tilt into a known binary is a protocol violation, so this row exists.

| Field | Value |
|---|---|
| **Event** | MSCI quarterly review, **2026-08-31** (passive print concentrates at that close) |
| **Frozen observable** | **`RSP` − `SPY` 1-session excess return**, settled closes, **2026-08-28 → 2026-08-31** |
| **Implied move at registration** | `RSP` **±1.06%** (2026-09-04 expiry, ATM K=220.00, straddle 2.34, IV 0.374/0.216) · `SPY` **±0.45%** (08-31 expiry, K=769.00, straddle 3.47). **Both branches sit outside `RSP`'s own priced move** |
| **Branch A (broadening)** | `RSP` − `SPY` **≥ +1.30pp** — the passive print favours the median stock ⇒ `M1051`'s sector-breadth-vs-stock-breadth split narrows and `P106`'s narrowing claim weakens |
| **Branch B (concentration)** | `RSP` − `SPY` **≤ −1.30pp** — the rebalance pushes further into the mega-caps ⇒ **`M1051` gets a mechanical explanation instead of a behavioural one**, and every `eqflow`-carried delta this run made stands on a number the index is actively working against |
| **Branch C** | between — **disclosed favourite** |
| **State at registration** | `RSP` 220.69 · `SPY` 769.35 (both settled 08-28). `RSP` `exc1` on 08-28 = **−0.116pp**; `exc5` = **−0.916pp** |
| **Information grade (B4)** | **HIGH on both, and asymmetric in a way worth stating**: this run made **four** verdict deltas entirely on `eqflow`, and **B is the branch that says the market is paying for the other number** |
| **Anti-signal (VOID)** | a market-wide trading halt, **or** MSCI postponing/withdrawing the review, inside 08-28 → 08-31. ⚠ Base rate low; the review date is calendar-confirmed |
| **Non-redundancy (`D343`)** | 08-31 carries six rows; all six are single-name, cross-sectional-count, or macro-print rows. **`S131` is the only one whose observable is the cap-weight-vs-equal-weight axis the rebalance actually moves** |
| **Owner** | `industry_US` |

## `S132` — ★★★ `AVGO` 09-02: a threshold that can carry information, four runs after `D295` asked for one · ARMED · → settle **2026-09-03**

| Field | Value |
|---|---|
| **Event** | `AVGO` FQ3 earnings, **2026-09-02 (D-4)**. **Held.** `rs60` **−24.4 = the worst on the book** |
| **Frozen observable** | **`AVGO` 1-session excess vs `SPY`** on the first settled close after the print (**2026-09-03**), each vs its own 2026-09-02 close |
| **Implied move at registration** | **±8.11%** — ATM straddle **K=370.00 = 29.91** on the **2026-09-04** expiry, the first that spans the print (IV 0.736/0.731). **Cross-checked** on the 09-02 expiry (K=380.00, straddle 29.94) → **±8.12%, agreeing to 0.01pp** |
| **Branch A (the discount was wrong)** | excess **≥ +9.00pp** — outside the implied move ⇒ the −24.4 `rs60` was a discount, not a franchise loss, and `S116`'s B-leaning read (that `MRVL` took the socket) is falsified |
| **Branch B (the discount was right)** | excess **≤ −9.00pp** ⇒ the franchise loss is real and **the AI-compute epicenter is narrower than the book's three names assume** |
| **Branch C** | between — **disclosed favourite, and disclosed as LARGE**: the band spans 18pp against an 8.11% priced move. Stated rather than tightened |
| **Relationship to `S127`** | 🚫 **`S127` is NOT re-frozen** (`D242`) and stays ARMED on its own bands (**A ≥ +5.928 / B ≤ −4.922**, settle 09-08). ★ **Those bands sit INSIDE ±8.11% ⇒ pre-declared NO-INFORMATION** — exactly what `D295` predicted when it flagged them as hand-set, unmet for four runs. **This row is `D295`'s prescription executed.** If the two rows disagree, **the disagreement is the finding** (`S14-ANNEX` precedent) |
| **Anti-signal (VOID)** | `AVGO` postpones the print, **or** an announced acquisition of/by `AVGO` inside 2026-08-31 → 2026-09-03 |
| **Information grade** | **HIGH on both** — each branch changes a standing thesis on a **held** name |
| **Owner** | `industry_US` |

## `S133` — ★★★ Health Care: is the sector its constituents or its ETF? · ARMED · → settle **2026-09-14**

**This row brackets a verdict change this run made today**, which is the point of it.
`SECTOR_ROTATION §2` promoted `HLTH` `N`→`OW` on **`eqflow` +0.102 (the board's highest)** *against*
**`XLV` `exc5` −2.456pp vs `SPY` (the board's worst)**.

| Field | Value |
|---|---|
| **Frozen observable** | **`EW{REGN, AMGN, TMO, BDX, MRK, VRTX}` 10-session excess return vs `XLV`**, settled closes, **2026-08-28 → 2026-09-14** |
| **Membership, enumerated** (`D388-KR`) | Exactly those six tickers — the six `us_top300` Health Care names with the highest `rs60` on the **2026-08-27 settled** sweep (`REGN` +32.4 · `AMGN` +31.6 · `TMO` +29.3 · `BDX` +28.7 · `MRK` +27.8 · `VRTX` +27.3), **all six `OBV 매집`, all six `rs20` positive**. Equal-weighted, no rebalancing inside the window |
| **Benchmark, named inline (`C1`)** | **`XLV`, not `SPY`** — the question is constituents-versus-cap-weighted, so the sector ETF *is* the correct counterparty. Using `SPY` here would measure the sector, not the split |
| **Implied move at registration** | `XLV` **±2.20%** (2026-09-11 expiry, ATM K=171.00, straddle 3.77, IV 0.368/0.219). Both thresholds outside it |
| **Branch A (the constituents are the sector — the promotion was right)** | EW6 − `XLV` **≥ +3.00pp** ⇒ `XLV` is reporting on `LLY` (its `top1` **flipper**), `eqflow` was the better instrument, and G5's "prefer `eqflow` on a 45-day-stale universe" rule earned its keep |
| **Branch B (the ETF is the sector — the promotion was wrong)** | EW6 − `XLV` **≤ −3.00pp** ⇒ **`SECTOR_ROTATION §2`'s promotion was wrong**, and a 60-day relative-strength screen selected six names that were about to mean-revert together |
| **Branch C** | between — disclosed favourite |
| **State at registration** | `eqflow` +0.102 vs `wflow` −0.027 (🚨1名 `LLY`), breadth 0.03, n=32. `XLV` settled 08-28 **171.16**; `exc1` −0.018pp, `exc5` **−2.456pp** vs `SPY` |
| **Information grade (B4)** | **HIGH on B, MEDIUM on A.** A largely confirms a direction this run already took; **B falsifies a verdict change made today**, which is rarer and more useful. **Stated at registration, not discovered at scoring** |
| **Anti-signal (VOID)** | an **FDA action or trial readout with a named date** at **≥2 of the six** inside 2026-08-28 → 2026-09-14. ⚠ **Base rate checked and NOT remote** — `LLY` took an FDA Mounjaro CV-risk approval on **08-28** (7 outlets) and the same day's head layer carried three other FDA items (`Revolution Medicines`, ivermectin EUA, `Pfizer`/`BioNTech` XFG vaccine). **Disclosed as live rather than assumed away** |
| **`L2` (peak-margin) not waived** | `MRK` **trades ABOVE its mean target** (upside −4.4%) on the carried §3a row. The basket is live **and** its one prior 🟢 is the expensive member — both stated |
| **Owner** | `industry_US` |

## `S134` — ★★ Financials: the contradiction with no instrument defect to blame · ARMED · → settle **2026-09-04**

| Field | Value |
|---|---|
| **Why it exists** | The **only** sector where both flow reads agree (`wflow` −0.144, `eqflow` −0.144), **neither is a `top1_flips_sign` bucket**, and the settled tape is **positive** (`XLF` `exc5` **+0.605pp vs `SPY`**, 2nd-best on the board). Every other contradiction this run found has an instrument defect available; **this one does not**, and `SECTOR_ROTATION §4` handed it here unresolved |
| **Frozen observable** | **`XLF` 5-session excess vs `SPY`**, settled closes, **2026-08-28 → 2026-09-04** |
| **Implied move at registration** | `XLF` **±1.36%** (2026-09-04 expiry, ATM K=58.00, straddle 0.79, IV 0.158/0.134). Both thresholds outside it |
| **Branch A (the tape was right, the flow axes were late)** | `XLF` exc5 **≥ +2.00pp** ⇒ ROTATION's `OW−`→`N` demotion was wrong, **and it would be the first evidence this desk has that `eqflow` can be wrong for a full week on a non-flipper bucket** |
| **Branch B (the flow was right)** | `XLF` exc5 **≤ −2.00pp** ⇒ the demotion was early and correct |
| **Branch C** | between — disclosed favourite |
| **State at registration** | `XLF` settled 08-28 **58.10**; `exc1` +0.607pp, `exc5` **+0.605pp** vs `SPY`; `wflow` −0.144 / `eqflow` −0.144 / breadth 0.02 / n=47, `top1` `BRK-B`, **not** a flipper |
| **Anti-signal (VOID)** | **Aug NFP prints 2026-09-04, the window's last day.** The window deliberately ends **ON** the print so the observable is the five sessions **before** it; **if the print is moved earlier, the row VOIDs** |
| **Hypothesis recorded, NOT adopted** | `EVENT_ALPHA` Card 8 — a take-private premium unwinding inside the sector (`PYPL` `rs60` **+36.5**, built on an Advent/Stripe offer **withdrawn 2026-08-28**, `OBV 중립`). **Named so a later run can test it; this row does not depend on it** |
| **Information grade (B4)** | **HIGH on A** (falsifies a demotion made today, and a rule the desk leans on), confirm-only on B |
| **Non-redundancy (`D343`)** | 09-04 carries `S126` (`XLI` exc5 vs `SPY` **into** NFP) and, from 09-04, `P114` (`XLI` exc5 **out of** NFP). **`S134` is a different sector on the same date**, and it is registered as sharing that date deliberately: if `S134`-B and `S126`-B both fire, that is **one macro observation**, not two sector verdicts |
| **Owner** | `industry_US` |
