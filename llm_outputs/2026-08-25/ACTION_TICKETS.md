# ACTION_TICKETS — 2026-08-25 · industry_US / L1·ALPHA

> **HAND-BUILT.** `scripts/action_bracket.py` was run and produced **no tickets** — see §0.
> **Pre-committed conditionals only. No order is sent by anything here. Zero buy/sell advice (P4).**
> ⚠ **DRY-RUN share counts are deliberately OMITTED** under this run's analytical-only mandate —
> a logged deviation from the script's documented output, 3rd consecutive run.

---

## §0 · 🚨 `D294`, SEVENTH reproduction — the script named the binary and then reported there was none

`action_bracket.py` printed, four lines apart:

```
**Nearest binary:** NVDA earnings (D-1, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
```

**The window holds EIGHT binaries** (PREMORTEM §0): `NVDA` 08-26 · `MRVL` 08-27 · Jackson Hole
08-27→29 · July PCE 08-28 · `FRO` 08-28 · MSCI 08-31 · `AVGO` 09-02 · Aug NFP 09-04, plus the undated
Hormuz row. The calendar itself carried **6**; the script converted **0**.
⇒ **An empty `ACTION_TICKETS.md` must never be read as "nothing was due."** Its `earnings` axis is
unpopulated and will produce no ticket for any single-name earnings binary until it is.

---

## §1 · Both-sides brackets in force — the tickets are the pre-registered rows

Every binary in the window is bracketed. **Nothing below is a trigger to act; each is an observable
with a frozen threshold and a settle date.**

| # | Binary | Date | Row(s) | Branch A | Branch B | Owner |
|---|---|---|---|---|---|---|
| 1 | **`NVDA` earnings** | **08-26 (D-1)** | `S79` · `S103` · `P90` · `S118` | (see rows) | (see rows) | `industry_US` |
| 2 | **`MRVL` earnings** | **08-27 (D-2)** | **`S124`** — bracketed at the SECTOR-BREADTH level, deliberately not with a 10th row on 08-28 | IT positive-`exc5` count **≥ 30** at 08-31 | count **≤ 13** | `industry_US` |
| 3 | **Jackson Hole / Warsh** | 08-27→29 | `S108` (settles tonight) · `P91` · `S120` · `S119` | (see rows) | (see rows) | `industry_US` |
| 4 | **July PCE** | 08-28 | `P67` `P81` `P85`–`P89` `P92` `P93` + `S118` | — | — | ⚠ **9 rows on one date (`D343`) — deliberately NOT added to** |
| 5 | **Crack-rate kill** | **08-27** | **`P96`** (registered today) | 5-session crack rate **≤ −2.887** ⇒ kill fires | **≥ +0.468** ⇒ counter resets | `industry_US` |
| 6 | **`FRO` earnings** | 08-28 | `S109` (settles 09-02) | ≥ +8.04pp | ≤ −4.62pp | ⚠ `FRO` **outside `us_top300`** (`D341`) |
| 7 | **MSCI quarterly review** | 08-31 | **none, deliberately** | — | — | Neither branch would change a sector verdict (`B4`) |
| 8 | **`AVGO` earnings** | **09-02** | 🚨 **NONE — a HELD name prints with no row** | — | — | **Registration obligation handed to the 08-26/08-27 run**, from a 09-04-or-later straddle (`D295`) |
| 9 | **Aug NFP** | 09-04 | **`S126`** (registered today) | `XLI exc5` **≥ −0.087** | **≤ −2.500** | `industry_US` |
| 10 | **Canada tariffs effective** | **09-08** | `S123` (Industrials, 09-12) + **`S125`** (agricultural leg, 09-11, registered today) | see rows | see rows | `industry_US` |
| 11 | Iran "Strait open" statement | **undated** | 🚨 **`S8` — undated for a 25th consecutive run** | — | — | **A human must `VOID` it or re-register it with a date (P5)** |

## §2 · Cycle-GAP core starter — **not required this run**

`CYCLE_EXPOSURE.json`: rank-1 AI-compute epicenter **16.59% ≥ 12.0%** need · rank-2 Energy/refining
**9.82% ≥ 8.0%**. **No GAP ⇒ no tape-independent core-starter ticket is issued.**
⚠ **Downgraded to `⚠ UNDER-DETERMINED` by PREMORTEM lens 4**, on three grounds: no optical registry
row (`D250`, 11th run) while `LITE`/`COHR` are the board's worst 5-session names; **rank-3's threshold
is unset** so `RTX` at 3.8% neither passes nor fails; and the epicenter % is computed on a book whose
AI-compute label spans **2–3 measured risk units at `--days` 250/500/750** (G4 FAILED).

## §3 · Standing conditional watch items (no ticket, dated re-check)

| Item | Condition to re-read | Date |
|---|---|---|
| `MRVL` | `rs20` holding **> +10** after its 08-27 print (now **+36.7**, the board's best) | 2026-08-28 |
| `MRK` | **current-YEAR** revision breadth (now **6↑/2↓ 30d**, 13↑/3↓ 7d) — **not the quarter** | 2026-09-03 |
| `MPC` `PSX` | `vol_surge` on a **settled-bar** sweep (today 0.84 / 0.80 on a stub-depressed universe, `D355`) | next settled-bar run |
| `ORCL` | ⚡ crowded-short **z +1.75** — turn-conditional squeeze fuel, **never a standalone signal** (`D6`); `rs60 −36.9` | 2026-09-03 |
| `MSTR` | revives on `rs60 ≥ 0` (now **−24.6**) — its own rejection condition | 2026-09-08 |
| `BLK` `DE` `GEV` | the three `missed_ledger` `--enters-if` conditions filed today | 09-03 / 09-08 / 09-08 |

---
*Analytical artifact. Tickets are pre-committed conditionals; no order is sent, and no share count is
issued in this run.*
