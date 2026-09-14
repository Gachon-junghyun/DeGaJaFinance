# ACTION_BRACKET — 2026-09-01  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,146,236원 · fx 1380 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** AVGO earnings (D-1, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*

---

# ADDENDUM — `industry_US` ALPHA (Stage 10), 2026-09-01

> Appended by the run, not by the script. **Analytical only — no order is sent, no size is recommended** (P4).

## 1 · 🚨 `D294` reproduced a SIXTH time, and the two lines are still adjacent

`action_bracket.py` printed, in consecutive lines of one output:

```
**Nearest binary:** AVGO earnings (D-1, axis=earnings) — both-sides armed below.
_No tickets — no cycle GAP and no dated binary in window._
```

**`M1217` [measured] — the window holds THREE binaries** (`catalyst_calendar --days 5`:
`AVGO` **D-1 2026-09-02** · August NFP **D-3 2026-09-04** · the undated Hormuz/TACO trigger), the
script **names the nearest one by ticker and date in the line above**, and then reports "no dated
binary in window" and emits **zero tickets**. ⇒ **6th consecutive reproduction.**
⚠ **Not fixed here** — code changes are a human-approval item. Recorded with its count.

## 2 · Why zero tickets is nevertheless the CORRECT output today

Independently of `D294`, this run would not have written entry tickets:

1. **No cycle GAP exists.** `cycle_exposure` (real KIS book): AI-compute epicenter **16.85%** vs a
   ≥12.0% floor · Energy/refining **10.28%** vs ≥8.0% · missile-defense 3.77% (no threshold set).
   ⇒ **no tape-independent core-starter is owed.** Third consecutive run.
2. **Every binary in the window already carries a both-sides bracket**, so issuing a ticket against
   one would re-freeze a live threshold (`D242`):
   - `AVGO` → **`S138` (±11.00pp, outside the measured ±9.6% implied move)** + `S132` (±9.00pp,
     **pre-declared no-information** because it now sits inside that move) + `S127` (09-08).
   - **August NFP** → `S126` (into) · `P114` (out of) · **`P121`** (`DGS2`, registered at MACRO today)
     · **`S139`** (the correlated-UW basket, re-armed at PREMORTEM today).
   - **Hormuz / oil** → **`P122`** (registered at MACRO to replace the bracket `S92` consumed when it
     scored) · `P107` · `P112` · `P117`.
3. **The run's mandate is analytical output only** — zero buy/sell recommendations — so **DRY-RUN
   share counts are deliberately omitted**, a logged deviation from the script's documented format.

## 3 · The bracket inventory this stage hands forward (what a ticket WOULD have been keyed to)

| binary | date | armed rows | the against-us branch |
|---|---|---|---|
| `AVGO` earnings | **09-02 or 09-03** ⚠ `D420` unresolved (issuer says 09-03, calendar says 09-02) | **`S138`** · `S132` (no-info) · `S127` | a **beat** rips the deepest-discounted half of IT (`MRVL` `rs60` −34.4 with `rs20` **+8.0** already turning · `AMAT` · `NXPI` · `ARM` · `ON`) — **none of which the book owns.** The cost is **opportunity, not drawdown** |
| August NFP | **09-04** | `S126` · `P114` · **`P121`** · **`S139`** | a **cold** payroll collapses September hike odds and `XLU`+`XLRE`+`XLP` rip **together** — the correlated-UW pattern that `S112` **FIRED-B** on today (−2.331pp vs `SPY`) reversing in one window |
| Hormuz / oil | undated | **`P122`** · `P107` · `P112` · `P117` | `CL=F` **≤ 80.00** takes **Energy** — rank 1 on both flow axes, both `new_green` ignitions — down first and hardest. Named bear leg: the **Venezuela** cluster (15 outlets, `theme-age` **2.74× ACCELERATING**) |

## 4 · 🚨 The ticket this run WOULD have wanted, and why it was not written

★ **A `UTIL` observation ticket.** Utilities is the board's **worst** sector on both non-cap-weighted
measures (`eqflow` **−0.454 rank 11/11**, red-rate **10 of 15 = 66.7%**), it has the **longest recency
gap on the board (7 runs)**, and it is **structurally unreachable** by ROTATION's selection rule
because UW sectors do not take DEEP slots — for a **third** consecutive run.
And this run gave it a live question for the first time: **if the AI-power leg is real, `UTIL` owns
it** — while **`ghost demand` (🟢FRESH, age 0)** and a tape in which **every AI-power name is 🟡 or 🔴**
say it is not.
⇒ **No ticket was written**, because a ticket is an execution conditional and this run issues none.
**`P123` (settles 09-08) is the instrument that carries the question instead**, and its
post-registration evidence is disclosed inside it.

## 5 · Handed to the next run
- **8 ALPHA-tagged names carry forward independently of their sectors' DEEP status**: `MU` `SNDK`
  `LITE` `SLB` `WMB` `CRM` `INTU` `A`, plus `AVGO` as a held-name watch.
- **Re-check dates armed**: **09-08** (`CRM` · `SLB` · `NEM` · `MPC` · `S140` · `P122` · `P123` ·
  `S127`) · **09-09** (`LITE` · `WMB` · `S136` · `S137`) · **09-14** (`MU` · `A` · `P111` · `S133`) ·
  **09-15** (`INTU` · `DIS` · `WBD` · `FCX` · `RTX`-thread) · **09-22** (`MSTR`) · **09-24** (`MU` print).
- **`D294` count = 6** · **`D304` reproduced** (`us_setup_screener` ran on a live partial bar; its 21
  new names are recorded as a list only) · **`D420` still open** on the `AVGO` date.
