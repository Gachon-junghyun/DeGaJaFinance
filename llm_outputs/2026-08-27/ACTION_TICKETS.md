# ACTION_TICKETS — 2026-08-27 · industry_US (Stage 10 / L1·ALPHA)

> **Pre-committed conditionals. Analytical/scheduling artifact — zero buy/sell advice, no order is
> sent by anything here, and no `--execute` path is touched.**
> 🚫 **DRY-RUN share counts are deliberately OMITTED** for a **5th consecutive run**: `kelly_size --ic`
> cannot be reported as an evidence-backed size while **PREFLIGHT G6 FAILs** (18 files / 36 calendar
> days = 0.50/day, **2.0× slower** than the accrual the IC estimate needs), and a printed share count
> next to a conditional reads as a recommendation. **Any fraction anywhere in this desk's output today
> is "mechanical 1/4 — IC not yet estimable (G6 FAIL)".**

---

## 🚨 §0 · Why this file is hand-built — `D294` reproduces for a **10th** run, in a new and worse form

`scripts/action_bracket.py` ran and produced two tickets. **Both are conditioned on an event that had
already happened.**

Verbatim from its output: **`Nearest binary: July PCE (Personal Income & Outlays) (D-1, axis=inflation)
— both-sides armed below`**, then `BRACKET::A_cool — NVDA … IF July PCE (D-1) prints toward cool` and
`BRACKET::B_hot ★asym-hedge — MPC … IF July PCE (D-1) prints toward hot`.

**July core PCE printed on 2026-08-26** — **+3.3% YoY unchanged from June, +0.2% MoM, both in line**,
corroborated across 6 outlets and sitting in the 08-26 `brief` head layer at **14 outlets / 44
articles** (`M977`). ⇒ **the script armed a two-sided bracket on a resolved observation.**

**Root cause, traced rather than assumed**: the script reads `CATALYST_WATCH.json`, whose PCE row is
flagged **`[bea~est]`** — a *pattern estimate*, not an official-source-confirmed date. **The `~` did
its job; three consecutive stages read past it** (`M978`/`D381`).
⇒ 🚨 **This is a NEW failure mode for `D294`.** The previous nine reproductions were *omission* — the
script naming a binary and then reporting there were none. **This one is commission: it emitted
tickets, with names and sizes, on a dead condition.** A ticket file that is silently empty is a gap;
a ticket file that is confidently wrong is worse. ⇒ **`D386`, `M995`.**
✅ **The script's chosen names were not unreasonable** (`NVDA` cool-side, `MPC` hot-side) — **only the
condition was dead.** Recorded so the diagnosis is precise.

**⇒ The script's output is superseded by this file. Its two tickets are void.**

---

## §1 · Tickets — both-sides, on binaries that have NOT yet occurred

> Every ticket names an **observable**, a **frozen threshold** and a **date**, and every one is
> **two-sided**. No ticket carries a size.

### T-1 · `MRVL` prints **tonight (2026-08-27, D-0)** — and the calendar cannot see it
| | |
|---|---|
| **Binary** | `MRVL` FQ2 results, after tonight's close. 🚨 **Absent from `catalyst_calendar --days 12`** — recovered from the 08-26 head layer (*"Marvell Reports Thursday"*, 5 outlets) |
| **Owning bracket** | **`S116`**, settles **2026-08-28** — `MRVL − AVGO` 1-session excess, **A ≥ +12.0pp / B ≤ −12.0pp** |
| **Implied move, checked** | `MRVL` **±9.9%** (08-28 expiry, D1). `AVGO` ±2.8%. Independent-spread implied ≈ **√(9.9² + 2.8²) ≈ 10.3%** ⇒ **the ±12.0pp threshold sits OUTSIDE it and therefore carries information** |
| **Side A (share shift confirmed)** | `MRVL` and the optical/interconnect layer re-rate — `LITE`, `COHR` print the same RS20-positive / RS60-negative / OBV-매집 shape |
| **Side B (over-priced)** | **`AVGO`'s `RS60 −25.4` was a discount, not a franchise loss** — and `AVGO` is **held**, prints **09-02**, and is the board's worst-reading position on every axis |
| **What it changes** | Both sides change a standing thesis on a **held** name. `AVGO` has been carried as *AI-compute-EPICENTER* with **its customer unnamed for the life of the position** (`W4`, open) |
| ⚠ | **No size. No entry.** The point of the bracket is that the desk does not act into the print |

### T-2 · The 09-08 Canadian retaliation — the agricultural leg, newly bracketed
| | |
|---|---|
| **Binary** | Canadian retaliatory tariffs **take effect 2026-09-08** |
| **Owning bracket** | **`S129`** (registered by this run's PREMORTEM), settles **2026-09-09** — `ADM` 5-session excess vs `SPY`, 09-02 → 09-09, **A ≤ −4.00pp / B ≥ +2.50pp** |
| **Side A (the channel prices)** | `STPL N−` becomes a **tariff** call rather than a defensive-rotation call |
| **Side B (already priced)** | `ADM` is **already** flow −0.643 🔴분산 with OBV −0.154 분산 **before** the effective date, and its **own 10-K says the impairment is past tense** — *"Increases in tariff and restrictive trade policies … **has, and could,** negatively impact…"* ⇒ B falsifies the forward tariff channel |
| 🚨 **Residual gap, named** | **The INDUSTRIAL leg of the same date is still bracketed only by `S123`, which settles 09-12 — four days late.** `D342`, **3rd run.** This file closes the agricultural half and **states plainly that it does not close the industrial half** |

### T-3 · `AVGO` prints **2026-09-02** — a held name with no live narrative
| | |
|---|---|
| **Owning bracket** | **`S127`**, settles **2026-09-08** |
| **Implied move, checked** | 🚨 `module_flow --positioning` returns **±2.8% at an 08-28 (D1) expiry for a 09-02 print** — **`D353`'s 9th reproduction.** A D1 straddle cannot price an event six days out ⇒ **`S127`'s thresholds were correctly NOT taken from the options market**, and that decision is re-confirmed here rather than assumed |
| **Both sides** | Held by `S127` as registered; not restated (`D242` — thresholds do not move) |

### T-4 · `NVDA` / Hugging Face **$12.9bn** — reported, not announced
| | |
|---|---|
| **Binary** | An acquisition on the book's **largest single position**, carried by `cnbc`, `techcrunch`, `fortune`, `yahoo_finance` on 08-27 — **every one says "report says" / "reports"; there is no company statement** |
| **Owning bracket** | **`S130`** (registered by this run's PREMORTEM), settles **2026-09-10** — two legs: (1) whether an `NVDA` statement or SEC filing exists by 09-10; (2) `NVDA` 10-session excess vs `SPY`, 08-27 → 09-10. **A: confirmed ∧ ≥ +2.00pp · B: ≤ −4.00pp regardless of leg 1** |
| **Why B is the informative side** | A **$12.9bn acquisition announced the day after a 100bp gross-margin guide-down** (`P90` → **FIRED-A** this run) being **sold** is `L2`'s peak-margin trap arriving on the epicenter of the #1 cycle |
| ⚠ | Positioning context only: **±3.0% (08-28 D1), skew +16.3, P/C 0.59** — the tool reads it **"안일 (complacent, little fuel)"**. Not a threshold |

### T-5 · Rows settling at **tonight's close** — no ticket, because there is nothing to arm
`S79` · `S81` · `S115` · `S117` · `S119` · `P83` · `P96` all settle on the **2026-08-27 settled close**,
which has not occurred (this run fires at 09:1x ET, pre-market). **They are already armed and frozen;
a ticket would add nothing.** 🚨 **But two of them settle on a contaminated bar** — `P96` and `P83` land
on an **RBOB Sept→Oct contract roll** that moves them in **opposite directions** (`M981`,
`SECTOR_DEEP_ENRG §1b`). **`P103` (09-02) is the roll-free re-read.** **Named here so tomorrow's run
inherits the warning rather than discovering it at scoring.**

---

## §2 · Cycle-exposure core-starter — **none emitted**, and the reason is a registry hole

`cycle_exposure` reports **✅ no GAP**: AI-compute (rank 1) epicenter **17.41%** vs need ≥12.0%
(`NVDA`, `ANET`); Energy/refining (rank 2) **9.77%** vs need ≥8.0% (`MPC`, `PSX`); missile-defense
(rank 3) 3.79% with **no threshold set ⇒ ⚪ n/a, not ✅**.

🚨 **That ✅ is a statement about three registry rows, not about the book.** `cycle_registry.json` has
carried **no optical/interconnect cycle for 13 consecutive runs** (`D250`/`M731`), while this run
measured **`MRVL` (`RS20` +32.6 / `RS60` −15.3 / OBV 매집), `LITE` (+32.4 / −9.5 / 매집), `COHR`
(+17.9 / −30.3 / 매집)** all printing the same turn shape, **`MRVL` reporting tonight**, and the
cleanest pure-play (`FN` Fabrinet) **outside `us_top300` entirely** (`D341`) so the desk cannot tag it.
**A cycle with no registry row can never produce a GAP flag no matter what the book holds.**
⇒ 🚫 **No epicenter-starter is emitted in either direction** — 2nd consecutive run, same reason.
✅ `COHR` and `LITE` are on the **missed ledger** (`Q.확신부족`, rechecks 09-10 / 09-09) so the
opportunity cost is scored rather than invisible.

---

## §3 · What this file does not do
- **No share counts, no notional, no stop prices** (§0 header) — the script's `10 sh @ ~$225.51` and
  `3 sh @ ~$359.0951` are **void along with their condition.**
- **No `--execute`, no order, no telegram.**
- **No freshness verdict** — see `BET_SHEET §B-FRESHNESS`: **G1 FAILed and ALPHA may not issue one.**
