# ACTION_TICKETS — 2026-08-26 · industry_US (Stage 7 / L1·ALPHA)

> **HAND-BUILT for a 4th consecutive run** — see §0. Pre-committed conditional tickets only.
> 🚫 **DRY-RUN share counts are DELIBERATELY OMITTED** under this run's analytical-only mandate
> (P4). **No order is sent by anything in this pipeline; a human executes separately.**
> Book context (read-only, from `action_bracket`): total ≈ **15,222,546원**, fx 1380.

---

## §0 · 🚨 `D294` reproduces for the **8th** time, and today it is on a D-0 binary

`scripts/action_bracket.py` printed, four lines apart, in the same output:

```
**Nearest binary:** NVDA earnings (D-0, axis=earnings) — both-sides armed below.

_No tickets — no cycle GAP and no dated binary in window._
```

**`CATALYST_WATCH.json` carries SIX binaries in the window** (`NVDA` D-0 · July PCE D-2 · `FRO` D-2 ·
`AVGO` D-7 · Aug NFP D-9 · the undated Hormuz statement), **plus two this desk added by hand**
(`MRVL` 08-27, Jackson Hole 08-27~29). The script names the nearest one **and then reports there are
none.** ⇒ **the file below is written by hand, for the 4th run running.**

---

## §1 · Both-sides brackets, by binary — every one is an ARMED registered row, not a new ticket

> The pre-mortem's mandate is *"a one-way tilt into a known binary is a protocol violation."*
> **It is met**: every binary in the window is bracketed both ways by a row with a frozen observable,
> a frozen threshold and a `D93` baseline. **Nothing new was registered on the saturated dates.**

| Binary | Date | Bracket(s) | A (against us) | B (with us) | Implied move check |
|---|---|---|---|---|---|
| **`NVDA` earnings** | **08-26 D-0** | `P90` (08-26) · `S79` `S115` `S117` (08-27) · `S118` (08-28) · `S103` (08-29) · `S113` (09-01) — **SEVEN rows** | A beat re-rates the sector this desk holds at `UW` | A miss confirms the hardware de-rate | **±6.0% (expiry 08-28, D2 — correctly spans the print)**; P/C **0.5**, skew **0.0** ⇒ complacent, little hedging fuel |
| **`MRVL` earnings** | **08-27 D-1** | **`S116`** (settle 08-28), spread `MRVL − AVGO` | ≥ **+12.0pp** | ≤ **−12.0pp** | **±10.3% (08-28, D2)** ⇒ **the ±12.0 thresholds sit OUTSIDE the priced move — information-carrying.** Not re-banded (`D242`) |
| **Jackson Hole (Warsh)** | 08-27~29 | `S120` (08-28) · `S112` (08-31) | dovish ⇒ the three underweights rip | hawkish ⇒ the underweights are right | ⚠ `S108`'s window contained **no event** (`R93` moved the date after freezing) ⇒ `D365` |
| **July PCE** | 08-28 D-2 | `S111` (08-28) · `S104` `S112` (08-31) | hot ⇒ `RE`/`UTIL` hit | cool ⇒ duration relief | 🚨 **08-28 carries NINE rows** (`D343`) — nothing added |
| **`FRO` earnings** | 08-28 D-2 | `S109` (settle 09-02) | — | — | 🚨 **`FRO` is OUTSIDE `us_top300`** (`D341`) — armed on a name this desk cannot flow-tag |
| **`AVGO` earnings** | 09-02 D-7 | ✅ **`S127` — REGISTERED THIS RUN** (settle 09-08) | ≥ **+5.928pp** (p85) | ≤ **−4.922pp** (p15) | 🚨 **UNREADABLE — `module_flow` returns ±1.3% at an 08-26 D0 expiry for a 09-02 event** (`D353`/`M948`). Thresholds taken from the trailing-252 tails, **labelled**, with an obligation to re-derive at the 08-28/08-31 run |
| **Aug payrolls** | 09-04 D-9 | `S126` (09-04) | weak ⇒ `INDU UW−` is a cycle call | strong ⇒ it is a tariff call | — |
| **Hormuz statement** | 🚨 **UNDATED** | **`S8` — unscoreable for a 27th consecutive run** | — | — | **A human must `VOID` it or re-register it with a date (P5).** Its object was in the 08-25 head layer at 9 articles / 8 outlets |

★ **One row registered against the desk's own strongest signal, not against a market binary**:
**`S128`** (settle **09-09**) tests `rs60`'s Bonferroni-passing NEGATIVE IC cell out of sample —
`EW{35 reversal}` − `EW{117 decay}`, A ≥ **+5.433** · B ≤ **−3.158**, state **−0.556 = 31.7th %ile**.
**Branch B kills a cell of the desk's own before it becomes doctrine.**

---

## §2 · Cycle-GAP core-starter — **NOT triggered, and the ✅ is qualified**

`cycle_exposure`: **no GAP.** AI-compute epicenter **16.69%** (need ≥12.0) via `NVDA`/`ANET`;
Energy/refining **9.7%** (need ≥8.0) via `MPC`/`PSX`; missile-defense 3.83% (`RTX`, no threshold set).
🚨 **PREMORTEM downgraded that ✅ to ⚠ UNDER-DETERMINED** — `cycle_registry.json` has **no
optical/interconnect row** (`D250`, **12th run**), on a run where `COHR` and `LITE` were `P79`'s
largest contributors and both sit in `S128`'s reversal basket. **An epicenter percentage computed
against a registry missing a live chain layer cannot say "no gap."**
⇒ **No core-starter is emitted, and the reason is that the gate could not be trusted either way** —
not that the book was found complete.

---

## §3 · Conditional tickets — the desk's own re-checks, as dated appointments

> 🚫 **No share counts.** These are **observation appointments**, not orders. Each one already exists
> as a ledger row or a registered bracket, so nothing here can be forgotten by omission.

| # | Name / object | Condition to re-examine | Owner row | Date |
|---|---|---|---|---|
| 1 | **`MRVL`** | `S116` settles on the first close after the 08-27 print | `S116` | **08-28** |
| 2 | **`AVGO`** (held) | re-derive `S127`'s thresholds from the **09-04-or-later straddle** before the print — the registration says the current implied move is unreadable | `S127` | **08-28 / 08-31** |
| 3 | **Refiner complex** (`MPC` `PSX` held, `VLO` not) | `P100`: `EW{MPC,VLO,PSX}` `exc20` vs `SPY` at the settle. A ≥ +13.478 · B ≤ −4.731; state **+11.597 = 77.4th %ile** | `P100` | **09-01** |
| 4 | **The crack kill** | `P96`: settled 5-session crack rate. A ≤ −2.887 · B ≥ +0.468; state **−1.675**. ⚠ base rate of the kill condition = **36.1%** | `P96` | **08-27** |
| 5 | **The duration complex** | `P78`: range across `{XLU,XLRE,XLP,XLV}`. **Pre-settle 4.889pp is ABOVE branch A (4.71)** | `P78` | **tonight, 08-26** |
| 6 | **The `vol_surge` gate** | `S101`: excluded-vs-admitted basket spread. Pre-settle **+1.616**, inside C leaning A. 🚨 **This is `C15`'s US-side settle** | `S101` | **tonight, 08-26** |
| 7 | **`MSTR`** | rejected `H.밸류소진`; revives if **CY consensus EPS turns positive AND `rs60` > 0** on a settled sweep | reject ledger | **09-16** |
| 8 | **`ORCL`** · **`KLAC`** | missed `Q.확신부족` / `M.숏리스트탈락`; enter if `rs60` > −15 while 🟢 / if 🟢 on a **SETTLED-bar** sweep with `vol_surge ≥ 1.2` | missed ledger | **09-16** |
| 9 | **`XOM`** (held) | rejected `K.본문반증`; revives if OBV → 매집 **and** Δ > 0 on two consecutive settled sweeps | reject ledger | **09-09** |
| 10 | **`AMD`** · **`AAPL`** | missed `M.숏리스트탈락` / `Q.확신부족` | missed ledger | **09-09 / 09-16** |
| 11 | **Canada tariffs effective** | `S123` owns implementation (09-12). ⚠ `P93` settles **08-28, eleven days early** (`D342`) — the announcement is bracketed, the implementation is not | `S123` | **09-08 → 09-12** |
| 12 | **`FCX` / `NEM` concentration** | `P102`: `EW{FCX,NEM}` − `EW{other 10 MATR}` 10-session. A ≥ +13.450 (p95) · B ≤ +2.505 (p50); state **+18.731 = 98.8th %ile** | `P102` | **09-09** |

---

## §4 · Positioning stamps (`⚡`/momentum-only), where they apply

- **`MRVL` — ⚠ TWO INSTRUMENTS DISAGREE ON ITS SHORT BOOK, one session before its print.**
  `us_live_shortlist` reads **✅ 저숏/숏커버 "clean rise"** from the FINRA daily z (**−1.11**);
  `module_flow --positioning` reads **short 4.8% of float and BUILDING**, DTC 1.4, skew **+3.5**.
  ⇒ **Neither is used alone.** ⚡-style squeeze language is **not** stamped, because the two sources
  do not agree that a crowded short exists. Handed to `S116`'s settle.
- **`MSTR` · `ORCL` — MOMENTUM-ONLY, and PREMORTEM re-tagged both NOT-A-RUNNER.**
  `rs20 +28.9 / rs60 −17.5` and `rs20 +22.6 / rs60 −40.5`: **20-day reversals off negative 60-day
  bases, not continuations.** Both are stamped momentum-only and both are now ledger rows.
- **`NVDA` (held) — ⚠ FINRA `z +1.78`, 5v5 **+2.4▲** = a short surge INTO its own D-0 print**, while
  `module_flow` reads short 1.3% float *covering*. **Same disagreement class as `MRVL`.** Options are
  **complacent** (P/C 0.5, skew 0.0) ⇒ **little squeeze fuel in either direction.**
- **`ANET` (held) — FINRA `z +2.06`, 5v5 +6.7▲ = the board's highest short pressure**, against
  accumulating OBV and `rs20 +17.4`. **Two-sided; no stamp issued, the disagreement is reported.**
- 🚫 **No `⚡crowded-short` stamp is issued anywhere this run**, and that is a finding rather than an
  omission: **no candidate showed a crowded short on which two instruments agreed.**

---

## §5 · What this file is NOT
- 🚫 **No share counts, no sizes, no buy/sell.** Any fraction that appeared would read
  **"mechanical 1/4 — IC not yet estimable (G6 FAIL)"**; none appears.
- 🚫 **No freshness verdict** — see `BET_SHEET §H`. G1 FAILED and ALPHA may not issue one.
- 🚫 **No epicenter core-starter** — the GAP gate is ⚠ UNDER-DETERMINED, not ✅.
