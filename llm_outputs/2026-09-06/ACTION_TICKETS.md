# ACTION_BRACKET — 2026-09-06  (conditional DRY-RUN tickets · human pulls the trigger)

> Weaves CYCLE_EXPOSURE (gap→core) + CATALYST_WATCH (binary→both-sides) + risk model + live KIS.
> Book total ≈ 15,210,744원 · fx 1360 · per-trade risk 1.5% (core 0.8%) · stop 7.0% · maxpos 25.0%
> ⚠️ DRY-RUN — sizes are illustrative; execution is a separate human `module_kis --order ... --execute`. US = USD limit only.

**Nearest binary:** Aug PPI (D-4, axis=inflation) — both-sides armed below.

### BRACKET::A_cool — NVDA  (BUY)
- **condition:** IF Aug PPI (D-4) prints toward cool
- **size:** 10 sh @ ~$230.36 (≈$2,303.6 notional, risk $167.83 = 1.5% )
- **stop:** $214.23 (−7.0%) · exch NASD

### BRACKET::B_hot  ★asym-hedge — MPC  (BUY)
- **condition:** IF Aug PPI (D-4) prints toward hot
- **size:** 3 sh @ ~$388.9 (≈$1,166.7 notional, risk $89.51 = 0.8% )
- **stop:** $361.68 (−7.0%) · exch NYSE

*Analytical/scheduling artifact — zero buy/sell advice. Tickets are pre-committed conditionals; no order is sent by this script.*
---

# ADDENDUM — appended by `industry_US` ALPHA, 2026-09-06

> The block above is `scripts/action_bracket.py`'s own output. This addendum reconciles it with what
> PREMORTEM actually registered, and adds the brackets the script could not see.
> **P4 — every line below is a pre-committed conditional. No order is sent by anything here.**

## 1 · 🚨 `D518` reproduces: the script armed a binary PREMORTEM deliberately DECLINED

`action_bracket` armed **Aug PPI (D-4)** as its nearest binary and generated two tickets
(`A_cool → NVDA` · `B_hot → MPC`). **PREMORTEM declined to bracket PPI standalone**, on the ground
that its transmission already sits inside **`S148`**'s window (09-04 → 09-14, which contains PPI, CPI,
`ORCL` and `ADBE`) and inside **`S149`**'s CPI/PPI energy leg, and that a standalone row would
duplicate `P121`/`P125`'s leg question — rows that are **blocked on `D427`**, not absent.

⇒ **Carry both, reconcile neither** (the 09-05 run's decision #5, applied again). The structural cause
is `D518`: **`action_bracket` selects by DATE PROXIMITY; PREMORTEM selects by INFORMATION CONTENT
(`B4`).** Those are two different rules and they will disagree whenever the nearest binary is not the
most informative one. **Second consecutive reproduction.**

⚠ **And the script's ticket names are not the desk's exposure map**: `NVDA` is `IT N` with `OBV
−0.084 분산`, and `MPC` is 🚨 the name carrying the sheet's largest short build (+8.9 5v5) and an IV
skew of **+42.0**. **Neither was proposed by any stage of this run.** Recorded, not adopted.

⚠ **`fx` mismatch, recorded**: `action_bracket` used **fx 1360** while `module_paper_book status` reads
**fx 1380** in the same session — a **1.5%** difference on every USD notional above. **Illustrative
sizes only** (P4), but the two instruments should not disagree. Filed as **`D544`**.

## 2 · The brackets PREMORTEM actually registered — the both-sides tickets that matter

**All three are in `handoff/SCENARIOS_US.md` AND indexed in the `SCENARIOS.md` spine.** Windows count
**settled** sessions: **2026-09-07 is Labor Day**, so 09-08 · 09-09 · 09-10 · 09-11 · 09-14.

| id | observable | branch A | branch B | settles | state at registration |
|---|---|---|---|---|---|
| **`S148`** | `EW{SW n=19}` − `EW{HW n=37}`, 5 sessions, 09-04 → 09-14. **`ORCL` and `ADBE` both report 09-10 16:00 ET and both are IN the SW leg** | ≥ **+3.927** (p85) — software repairs | ≤ **−7.906** (p15) — the `P101` inversion deepens into a regime | **09-14** | **−6.511 = 21.0th pctile** — 1.40pp from B, 10.4pp from A ⇒ **A is the informative branch** |
| **`S149`** | `CL=F` 5-session % change, 09-04 close ($91.48) → 09-11 close | ≥ **+8.343** (p85) — escalation priced into the barrel | ≤ **−5.734** (p15) — ★ **the against-us branch: Bessent's $40 framing wins and `ENRG OW+` breaks** | **09-11** | 🚨 **+9.688% = 87.7th pctile** — the level is above A, but the observable is the NEXT five sessions ⇒ **B is the more reachable branch** |
| **`S150`** | `EW{RTX,LMT,NOC,GD,LHX}` − `SPY`, 5 sessions, 09-04 → 09-14 | ≥ **+2.902** (p85) — node air-pocket repairs | ≤ **−3.611** (p15) — the node de-rates and the book's `RTX` is inside it | **09-14** | 🚨 **−5.166 = 7.1st pctile, already BELOW B** ⇒ **B carries little information; A and C carry it** |

⚠ **Threshold-vs-implied-move, stated per row** (the stage's own rule):
- `S148` — `ORCL` implied **±11.8%**, `ADBE` **±8.1%** (both to 09-11). **A 1-session magnitude
  bracket on the pair is NO-INFORMATION** (its p85/p15 vs `SMH` are +3.15/−3.66, a third of the
  implied move) and was **deliberately not registered**; the 5-session leg spread is registered instead.
- `S149` — the only Energy straddle (`XLE` **±1.6%**) **expires 09-09, before the row settles**, so it
  cannot bound the window ⇒ thresholds from `D93` on the observable itself, **stated rather than
  borrowed from a proxy that expires early** (the `M1305` error, corrected by `M1326`).
- `S150` — `RTX` implied **±2.1%**; a 5-name equal-weight basket diversifies that down, so the
  **±2.90 / −3.61** lines sit **outside** a diversified basket move ⇒ they carry information.

## 3 · Cycle-GAP core-starter — **NOT issued, and the reason is not "no gap"**

`cycle_exposure` reports **no top-rank cycle GAP** (AI-compute epicenter 17.48% vs a ≥12% bar;
Energy/refining 10.47% vs ≥8%). ⇒ **the tape-independent core-starter does not fire.**

⚠⚠ **But the ✅ is "not measured," not "covered," and the three reasons are carried here so the next
run does not read the green as coverage:**

1. **The AI-power cycle is absent from `cycle_registry.json` entirely** (`M1308`, 3rd run) ⇒ **a
   registry that cannot see a cycle cannot flag a gap in it.** The lane's money is in generation
   (`CEG` +0.64 · `VST` +0.62, both accumulating, **both blocked from the shortlist by `vol_surge`
   alone**) and the book's only holding is **`ETN`, the lane's single distributing name.**
   **`S146` settles 09-14.** ⚠ **Adding the cycle to the registry is a human-approval item (P5).**
2. **The rank-1 cycle's held epicenter is on the non-accumulating side of its own node** — `NVDA` OBV
   −0.08 분산, `ANET` 중립 with `vol_surge` 0.60 (its tag *cannot* fire), `AVGO` −0.45 분산 with
   rs20 −15.9 — **while storage/memory, carrying the board's two largest Δflows, is 0% of the book.**
   **`S145` settles 09-11.**
3. **The rank-3 cycle (missile-defense) has NO bar set**, so the GAP check is **silent on it by
   construction** — at the exact moment its node printed a **7.1st-percentile** 5-session extreme
   (`M1374`). **`S150` settles 09-14.**

## 4 · What this run did NOT arm, and why

| binary | date | not armed because |
|---|---|---|
| `ORCL` / `ADBE` **magnitude** | 09-10 | NO-INFORMATION at any settable threshold (§2). Measured precedent: `S132` (±9.00) and `S138` (±11.00) **both fired C on the identical −3.792pp `AVGO` realization** (`D503`) |
| FOMC + SEP | 09-16 | Outside every window this run opens; deferred to a run with a **settled tape** and the **09-11 COT** |
| S&P rebalance / quad witching | 09-18 | Structural, not directional — it moves volume, and no proposition here is volume-conditioned. `P124` already settles that date |
| KOSPI200 quad witching | 09-10 | 🚫 Out of scope for `--market us` (`W1`). The 09-06 KR run asked the next US run to bracket it; **a US-pure desk cannot discharge it either**, so **`D533` stays OPEN** and needs a human or a KR protocol change (**P5**) |

**A one-way tilt into a known binary is a protocol violation.** Every dated binary inside this run's
windows carries a both-sides row: **PPI and CPI inside `S148`; the barrel inside `S149`; the defense
node inside `S150`; plus the six CPI rows already live (`P137`, `P138`, `S135`, `S142`+ANNEX, `S125`,
`S145`).** **No one-way row was written.**
