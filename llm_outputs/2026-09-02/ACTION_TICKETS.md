# ACTION_BRACKET — 2026-09-02  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,177,874원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** AVGO earnings (D-0, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ═══ ADDENDUM — hand-written tickets, appended 2026-09-02 by `industry_US` ALPHA ═══

> **Append-only.** Nothing above this line is rewritten — the script's own output stays visible beside
> its refutation, which is the point of the addendum (`D48`).

## 🚨 `D294` reproduces for a **7th** time, and it is quantified this run
The block above prints **"Nearest binary: AVGO earnings (D-0, axis=earnings) — both-sides armed
below"** and then, three lines later, **"no dated binary in window."**
**`CATALYST_WATCH.json` (`--days 10`) holds FIVE binaries**: `AVGO` **D-0 (tonight)** · August NFP
**09-04 (D-2)** · August PPI 09-10 · August CPI 09-11 · the undated Hormuz "Strait open" statement.
⇒ **The tool names the binary in one line and denies it exists in the next.** PREMORTEM §6
pre-committed that if this reproduced, *"the tickets are written by hand and the reproduction is
logged"* — both are done here. **Not fixed** — a code change is a human-approval item (P5).

## Risk frame (from the block above, unchanged)
Book total **≈15,177,874원 ≈ $10,998** at fx 1380 · per-trade risk **1.5%** (core 0.8%) · stop
**7.0%** · max position **25.0%** ⇒ **max risked $165/trade ⇒ ≈$2,357 notional at a 7% stop**, capped
at **$2,749** by `maxpos`. **All prices below are the 2026-09-01 SETTLED closes.**
⚠ **DRY-RUN. Illustrative sizes only. No order is sent by this desk (P4/P5).**

---

## Ticket set 1 — `AVGO` earnings, **D-0 tonight**. Both sides, because a one-way tilt into a known binary is a protocol violation.

**State entering the print** (all 09-01 settled): `AVGO` **369.68**, flow **−0.711 🔴분산**, OBV
−0.264, `rs60` **−10.4 vs `SPY`**, chart **FALLING-KNIFE / RSI 24.5 / 0-of-4 MAs**, short **1.2% float
COVERING**, DTC 3.0, **P/C 1.62**, **implied move ±9.5% (D0)**. `SMH` **545.22**.

| | **Branch A — the print re-rates semis** | **Branch B — the print de-rates semis** |
|---|---|---|
| **trigger (pre-committed, observable)** | `SMH` 1-session excess vs `SPY` at the **09-03** close **≥ +1.802pp** (252-obs p85) — this is **`S141`-A** | `SMH` 1-session excess vs `SPY` at the 09-03 close **≤ −1.732pp** (p15) — **`S141`-B** |
| **what it says** | the software/semis split (`SECTOR_DEEP_IT §1`) narrows; `S124`'s 41-of-56 breadth extends; this run's declined `IT N → UW` was **wrong** | the distribution reading was right; `AVGO` OBV −0.264 and `ANET` z +2.25 were the tell |
| **illustrative expression** | **`SMH` ≈ 4 shares @ ≤ 545.22** (≈$2,181, inside the $2,357 risk box) — the **sector**, deliberately, because `BET_SHEET §0c` bars the names inside it: `AVGO` is not in the real book, and `NVDA`+`ANET` are already **35.9%** of invested capital | **no add.** The held names are already 35.9%; branch B is an information event, not an action |
| **hard stop (`module_chart` swing low)** | `SMH` −7.0% from fill; `AVGO`'s own swing-low reference is **355.59**, `NVDA`'s **208.48** | — |
| **invalidation** | a market-wide halt, or a **dated** US export-control action on advanced semiconductors. ⚠ **Base rate pre-stated**: the recent tungsten / battery black-mass action and the tomshardware **draft** rule are **different product classes and do NOT invalidate** | same |
| **⚠ threshold provenance** | **`implied-move UNCHECKED`** — `SMH`'s only straddle is **±0.9% at a D0 expiry that lapses before the window opens**, so it bounds today's residual move, not the print reaction (`C3`). `AVGO`'s own ±9.5% confirms **`S138` (±11.00pp) is outside** and **`S132` (±9.00pp) is inside ⇒ pre-declared NO-INFORMATION** (`D451`) | same |

## Ticket set 2 — **August NFP, 09-04 (D-2)**. Both sides, on the correlated-underweight basket the desk has already MEASURED.

**Why this basket**: `S112` **FIRED-B** on it (**−2.331pp** against a −1.757 threshold) — the
correlated-UW pattern is measured, not hypothesised — and `S139` re-armed it across this print.
⚠ **And it is now FOUR legs, not three**: ROTATION demoted **`FIN` → UW** today, so `XLU` · `XLRE` ·
`XLP` · `XLF` may all be one duration/policy-path bet (`S135` settles 09-11 on exactly that question).

| | **Branch A — hot NFP, hike odds rise** | **Branch B — weak NFP, hike odds collapse** |
|---|---|---|
| **trigger** | `EW{XLU, XLRE, XLP}` 3-session excess vs `SPY` at the 09-04 close **≤ −1.757pp** — **`S139`-B**, i.e. the underweights keep working | the same basket **≥ +1.757pp** — the three UWs **rip together** and three verdicts break at once |
| **the leg that cuts the other way** | **`FIN`**: a steeper curve pays the bucket demoted today ⇒ **`S142`-A** (`XLF` exc3 vs `SPY` **≥ +1.315pp** at the **09-11 CPI**) would falsify the demotion | `FIN` lags with the rest ⇒ `S142`-B confirms it |
| **illustrative expression** | **none — the desk is already positioned in this direction by omission.** Writing an add here would be sizing an existing tilt, not bracketing a binary | **`XLU` ≈ 55 shares @ ≤ 42.56** (≈$2,341) as the *reversal* leg, ⚠ **NOT armed**: `XLU`'s exc1 +1.47 is partly a **legislative round-trip** (`D477`), so its strength is not clean |
| **hard stop** | — | 7.0% from fill; `NEE`'s swing-low reference is **82.34** |
| **invalidation** | an unscheduled Fed action, or a BLS release-date change | same |
| **leg prices (09-01 settled)** | `XLU` 42.56 · `XLRE` 44.04 · `XLP` 85.25 · `XLF` 57.20 · `SPY` 761.78 | |

## Ticket set 3 — the cycle flag the instrument could **not** raise

`cycle_exposure` prints **✅ no GAP**, and that is why the script emitted zero tickets. **PREMORTEM
Lens 4 raised one anyway, manually**, and it is carried here so it is not lost between stages:

- **The AI-power cycle has no registry row** (`D416`, 6th run) ⇒ **no GAP can be computed for it.**
  The real book's only exposure is **`ETN` 7.5%**, tagged *adjacent*, and `ETN` is **🔴분산 with
  Δ −0.633** (4th-worst in the universe) and `[FINRA]` z **−1.72** — shorts leaving a *falling* name.
- **Illustrative core-starter, tape-independent by the rule** (a 🔴 tape gates ADD *timing*, never
  core): the cleanest offtake expressions are **`CEG` @ 280.31** (chart OBV **+90%**, 4/4 MAs, `rs20`
  **+6.1 vs `SPY`**, swing-low **260.70**) and **`VST` @ 138.08** (chart OBV **+93%**, coiling 10.5%,
  swing-low **135.66**, forward P/E **13.56**, consensus **+54.7%**).
  ⚠ **Neither is armed.** `CEG` is filed to `missed_ledger` as `Q.확신부족` (enters if 🟢 **or**
  `P127` fires A, recheck **09-10**), and `VST`'s own out-year estimate line is being **cut −5.0%**,
  which is the denominator attack showing up in numbers.
- ⚠ **`NRG` — an obvious offtake name — is not in `us_top300` and cannot be tagged at all.**

## What is deliberately NOT ticketed, with the reason
- **`CRM`** — the board's rank-1 flow (+1.000, `vol_surge` 2.00): **standing 08-31 rejection**
  (`B.모멘텀only`), revival needs `rs20 > +20` ✅ **and** a new dated catalyst inside 30 days ❌.
  **Barred by `D463`, which is exactly the check the 08-31 run failed.**
- **`MSTR`** — two standing rejections whose conditions disagree (`BET_SHEET §0c`); the
  better-specified one says the bitcoin beta **did not detach** (BTC **+22.08%** over the same 20
  sessions).
- **`NEM`** · **`MDT`** — 🟡PARTIAL, not 🟢: both sit on **cut** estimate lines (`NEM` −12.1% with
  30-day breadth **1↑/11↓**; `MDT` −1.8% with **+5.2%** consensus upside).
- **`MPC`/`PSX`** (held) — extended: within **0.4%** of 52-week highs with consensus targets
  **12.8–16.1% BELOW** the price, and **refining has no take-or-pay** (`M831`) ⇒ no add is ticketed.

*Analytical artifact. Pre-committed conditionals only. **Zero buy/sell advice; no order is sent, and
`--execute` is not used by this desk** (P4/P5).*
