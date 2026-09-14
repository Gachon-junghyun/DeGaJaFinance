# BLINDSPOT_PREMORTEM — industry_US · 2026-08-25 (Tue) · Stage 7 / L1·PREMORTEM ★US-only

> Four adversarial lenses argue **AGAINST this run's own tilt** before the DEEP budget is committed.
> ⚠⚠ **DECLARED DEVIATION, 8th consecutive run**: the four lenses ran **in-context and serially**, not
> as a parallel adversarial agent fan-out (standing session constraint — this session may not spawn
> subagents). **They therefore share this run's blind spots**, and each lens states below what it could
> not independently check. This is a real weakness of the stage, recorded rather than papered over.

**Draft tilt under attack**: `ENRG OW · HLTH OW · STPL N · MATR N · COMM N · DISC N · FIN N · RE N− ·
UTIL UW− · INDU UW− · IT UW`. DEEP set: continuous `[ENRG, HLTH]`, rotating `[MATR, IT]`.

---

## §0 · Binaries in the window — and every one is accounted for

`CATALYST_WATCH.json` (`--days 10`) returned **6 binaries**; the true in-window count is **8** — the
calendar again misses **Jackson Hole (08-27→29)**, a **4th consecutive miss** (`M872`), and misses
**MRVL's 08-27 print**, which appears nowhere in it.

| Date | Binary | ≤48h? | Bracketed both ways? |
|---|---|---|---|
| **2026-08-26** | **`NVDA` earnings** | ✅ **D-1** | ✅ **YES, four-fold**: `S79`, `S103`, `P90`, `S118` — plus `P79` settles the night before it by construction |
| **2026-08-27** | **`MRVL` earnings** | ✅ **D-2** | 🚨 **NO — and this lens does NOT add a 10th row to 08-28.** Covered instead by **`S124`** (below), at the level where the desk's verdict actually lives |
| **2026-08-27** | **Jackson Hole opens (Warsh)** | ✅ D-2 | ✅ `S108` (settles tonight), `P91`, `S120`, `S119` |
| **2026-08-28** | **July PCE** | D-3 | ✅ — and **over**-bracketed: **9 P-rows plus `S118`** (`D343`) |
| **2026-08-28** | **`FRO` earnings** | D-3 | ✅ `S109` (settles 09-02) |
| **2026-08-31** | MSCI quarterly review | D-4 | ⚪ structural passive-flow event, **not** a directional binary — **deliberately not bracketed**, and the reason is stated: neither branch would change a sector verdict (B4) |
| **2026-09-02** | **`AVGO` earnings** | D-6 | ⚪ **no row.** Held name. **Named as a gap, not filled** — see lens 1 |
| **2026-09-04** | **Aug NFP** | D-8 | 🚨 **NO** → **`S126`** (below) |
| undated | Iran "Strait open" statement | — | 🚨 **`S8`, undated for a 25th run** — a human must `VOID` it or date it (P5) |

---

## LENS 1 · UNDER-COMPUTED LEGS — the bull case for what we did NOT deep-dive

**Candidates, ranked by (recency starvation × evidence density), with a ≤5-trading-day catalyst required:**

| Leg | Last DEEP | The bull case AGAINST our tilt | Catalyst ≤5 sessions? | **Verdict** |
|---|---|---|---|---|
| **UTIL / AI-power** (`GEV` `CEG` `VRT`) | 08-23 (2 runs) | ★★ **The board's TWO LARGEST positive flow deltas sit inside the board's WORST sector**: `GEV +0.440`, `CEG +0.300`. EVENT_ALPHA Card 4: the "AI needs power" story runs at **7 outlets** while UTIL's `eqflow` is **−0.616** with **10 🔴 of 15** — a story/money divergence that has persisted for months and could be the desk mis-reading a *lagging* instrument | ✅ **MSCI review 08-31 = 4 sessions** | **WITHIN-RUN-WATCH — promotion DECLINED, and the reason is a rule, not a preference**: the entire bull case rests on `delta`, i.e. a **Δflow against a snapshot with a different terminal-bar regime** (`D355`: 08-21 settled vs 08-25 stub). ROTATION barred Δ-based arguments this run for exactly that reason, and this lens does not get an exemption. **Re-check when a settled-bar snapshot exists** |
| **`AVGO` 09-02 print** | held name, IT DEEP R2 | ★★ **A held name prints in 6 sessions with NO row on the board.** `AVGO` is 🟡 −0.432, OBV −0.002, `rs20 −8.2`, **`rs60 −20.1`** — the worst 60-day relative strength of the four IT book names, and it is one of `P79`'s five legs | ✅ D-6 (just outside 5) | **WITHIN-RUN-WATCH → handed to the 08-26/08-27 run as a REGISTRATION OBLIGATION.** Not bracketed today because a 09-02 row registered before the 08-26 and 08-27 prints would have to be re-derived after them (`D295`'s exact failure) |
| **Real Estate** | 08-22 (**4 runs**) | `eqflow −0.410` rank 10 with 0🟢/3🔴, **against** a price **median `exc5` +2.782 = 2.1× its mean** — the sector is better than its own aggregate and nobody has looked in four runs | ❌ none dated | **WITHIN-RUN-WATCH.** Logged in DEEP_LOG with the `C5` contradiction named |
| **Financials** | 08-22 (**4 runs**) | Price `exc5 +2.662` with its mean/median sign split **closed**, `NDAQ`/`MET` held, and **`COIN` is a FIN-labelled 🟢 that is really bitcoin beta** | ❌ none dated | **WITHIN-RUN-WATCH** |
| **Consumer Discretionary** | 08-23 (3 runs) | **The board's widest single contradiction**: `0 🟢 / 8 🔴 of 28` with **breadth 0.00** against **24 of 28 positive on price** (`exc5 +3.091`). No live bracket since `S91` VOIDed | ❌ none dated | **WITHIN-RUN-WATCH** |

⇒ **NO 5th DEEP slot promoted. DEEP set is UNCHANGED: `[ENRG, HLTH]` + `[MATR, IT]`, N = 4/4.**
★ That is a change from the last two runs, which each promoted a 5th slot, and it is a *decline made
with a number* rather than a quiet omission: the one leg with a qualifying catalyst (UTIL) fails on
`D355`.

⚠ **What this lens could not independently check** (serial-execution cost): it re-used this run's own
sweep and price frame, so any error in those propagates. It did **not** re-pull `GEV`/`CEG` from a
settled-bar source, which is precisely the check that would have decided the UTIL promotion.

---

## LENS 2 · REGIME-FLIP / BOTH-SIDES — for each binary, the branch that hurts us

### 2a · `NVDA` 08-26 — the against-us branch, and it is NOT the one the desk is positioned for

**Our tilt**: `IT UW`, downgraded today on **43 of 56 names negative**, with `P79` sitting at
**−10.852, inside its own branch B**.
**The branch that hurts us**: a clean Rubin beat + resolved financing ⇒ the 5-session `exc5` of
−4.761 reverts violently, `P79` settles **A or C**, and the desk will have downgraded IT **at the
5.6th percentile of its own two-year breadth distribution** — i.e. sold the bottom decile.
**The mechanism is live and measured, not hypothetical**: `Nasdaq-100` spec is at the **4th
percentile short with +30,838 of weekly covering** `[COT 08-18]`, and `NVDA`'s own implied move is
**±6.13% (08-28 expiry, D3)** — the fuel exists.
⚠ **`NVDA` is `🟡`, OBV 중립 −0.073, `rs20 +4.2`, `rs60 −0.8`** — the epicenter is *flat*, not broken.
**Starter list, epicenter-first (analysis only, no sizing — P4)**: `NVDA` (held) · `MRVL`
(`rs20 +36.7`, the sector's price leader) · `AVGO` (held, `rs60 −20.1`, the worst leg).
**Trigger**: IT positive-`exc5` count rising from **13 of 56** toward its **252-day median of 30**.
**Invalidation**: the count staying **≤13** through 08-31. ⇒ **registered as `S124`.**

### 2b · Jackson Hole 08-27 — the against-us branch on the duration underweights

**Our tilt**: `UTIL UW−`, `RE N−`, `STPL N` — three of the four legs `S108` brackets.
**The branch that hurts us**: a dovish Warsh ⇒ the three rip together and three sector calls break at
once. **`S108` settles tonight and its pre-settle is +0.484 with 2 of 3 sessions in.**
★ **But this lens's own finding is that the against-us branch is INTERNALLY INCOHERENT**: the three
legs span **3.75pp** (`XLP +2.382` / `XLRE +0.440` / `XLU −1.371`) and one is **negative**.
⇒ **"the correlated-UW pattern" — the exact field note this stage exists to catch — is weakening on
its own evidence before its own settle.** And the measured rate betas say why: `XLU +0.0049`,
`XLRE −0.0072`, `XLP +0.0224` pp/bp ≈ **zero**, while `XLE` is **+0.1534**.
⇒ **The desk's only rate-exposed tilt is its ENERGY OVERWEIGHT, with a positive sign.** A dovish
Warsh helps the overweight and barely touches the underweights. **No new bracket** — `S108`, `P91`,
`S120` and `S119` already cover this from four angles, and a fifth would be `D343`.

### 2c · July PCE 08-28 — **declined, with the reason stated (B4)**

**9 P-rows plus `S118` already settle on 08-28.** Per `D343`, date-clustered rows resolving together
read as N confirmations from **n ≈ 1**. **A tenth row would add zero information and would inflate the
apparent confirmation count.** ⇒ **not bracketed, deliberately.** `S121` was dropped for exactly this
reason on 08-24 and its ID consumed unused; that precedent is followed rather than re-litigated.

### 2d · Aug NFP 09-04 — **UNBRACKETED, and it is the window's cleanest open binary** ⇒ `S126`

**Our tilt**: `INDU UW−` on **18 🔴 of 50** and `exc5 −1.881`.
**The branch that hurts us**: a strong labour print ⇒ cyclicals rip and the Industrials underweight —
the desk's *stated live transmission channel* — is on the wrong side of a labour-led rotation, with
the tariff channel not yet effective (09-08). ⇒ **registered as `S126`.**

### 2e · The Canada tariff's **agricultural half** — `D342`'s explicitly named gap, unbracketed for a 3rd run ⇒ `S125`

Canada's retaliation list names **steel, dairy, appliances and agricultural goods**, effective
**2026-09-08**. `S123` brackets the **Industrials** leg (09-05→09-12). **The Staples/agricultural leg
has been named as unbracketed in two consecutive runs and still has no row.** `ADM` is that leg's name
and its **`exc5` vs `XLP` is −6.511 = the 4.4th percentile of 252**. ⇒ **registered as `S125`.**

---

## LENS 3 · MOMENTUM-CONTINUATION — "already ran" ≠ avoid. Re-tag every runner.

Runners = the board's top `rs60` vs `SPY`, from `SECTOR_FLOW_US.json` asof 2026-08-25.

| Name | `rs60` | `rs20` | OBV | surge | **Re-tag** | Flip condition |
|---|---:|---:|---|---:|---|---|
| **`MPC`** (held) | **+43.3** | +14.1 | 매집 | 0.84 | **EXTENDED-BUT-LIVE** — the cycle KPI is the crack, and the settled 5-session crack rate is **−2.862 = 15.5th %ile, one of two declines** | **`P96` branch A** (rate ≤ −2.887 at the 08-27 settle) ⇒ **EXHAUSTED.** The kill is one settled session away and the LIVE bar already has it |
| **`PSX`** (held) | **+35.5** | +13.5 | 매집 | 0.80 | **EXTENDED-BUT-LIVE**, same KPI | same |
| **`MRK`** | **+27.0** | +12.1 | 매집 | **1.53** | 🚨 **EXHAUSTED-BY-DENOMINATOR, not by tape.** The tape is pristine — only 🟢 surviving the velocity withdrawal, FINRA z **−0.72** clean-rise, OBV 매집. **The denominator is not**: revisions **1↑ / 5↓ (30d)**, RSI **86.7**, **98.7% of its 52-week high**. `L2`'s peak-margin trap in its purest form | Revisions turning ≥3↑/≤2↓ by the **09-03** recheck ⇒ back to EXTENDED-BUT-LIVE |
| **`TGT`** | **+26.3** | +9.0 | 매집 | **1.31** | **EXTENDED-BUT-LIVE** — and it clears the surge gate on a **stub-depressed** universe (`D355`), so it is **understated, not overstated** | `P84` (09-03): its Q2 beat contained **$1.65 of $4.11 EPS = 40.1% tariff refund**. If that reverses ⇒ EXHAUSTED |
| **`HPE`** (held) | **+23.6** | +14.5 | 매집 | 0.50 | **EXTENDED-BUT-LIVE on price, UNRESOLVED on the pair** — `S110` (09-03) tests `HPE − DELL` precisely because `S87` averaged two opposite states | `S110` branch B (`≤ −6.14`) ⇒ the exhaustion verdict lands on the held name |
| **`ANET`** (held) | **+19.5** | +10.1 | 매집 | 0.60 | **EXTENDED-BUT-LIVE** — best OBV of the four IT book names (+0.222) | OBV flipping 분산, or `S99`'s successor joint-loading test landing it in AI-compute |
| **`MRVL`** | **+18.0** | **+36.7** | 매집 | 0.74 | ★ **EXTENDED-BUT-LIVE and the board's clearest case for the lens's own thesis** — `rs20 +36.7` is the highest on the board and its 🟢 was withdrawn only because it came from the **news** axis; the **price** leadership is unaided | Prints **08-27** with implied **±13.3% (08-28, D3)**. `rs20` falling below **+10** post-print ⇒ EXHAUSTED |
| **`MSTR`** | **−24.6** | **+23.4** | 매집 | 1.67 | 🚨 **NOT a runner — the sign is the finding.** `rs20 +23.4` sits on top of `rs60 −24.6` = a 20-day bounce inside a 60-day downtrend, and it was **rejected on 08-24** (`C.차트붕괴`, revives on `rs60 ≥ 0`) | Its own revive condition, **09-08** |

★ **The lens's verdict against our tilt**: the desk holds **four EXTENDED-BUT-LIVE names** (`MPC`
`PSX` `HPE` `ANET`) and **not one of them is 🟢**, every one blocked by `vol_surge` alone — on a run
where `D355` cut universe `vol_surge` by **18%**. ⇒ **"already ran, therefore avoid" is not this
desk's error today; "the gate is measuring a stub bar" is.**
⚠ **What this lens could not independently check**: it read `rs60` from the same stub-bar snapshot.
`rs` is only lightly contaminated (median stub price change −0.048%), but it is not zero.

---

## LENS 4 · CYCLE-EXPOSURE — registry vs coverage vs the REAL book

`CYCLE_EXPOSURE.json` (deterministic, read-only against the KIS book):

| Cycle | rank | epicenter % | need | verdict |
|---|---:|---:|---:|---|
| AI-compute / semiconductors | 1 | **16.59%** (`NVDA`, `ANET`) | 12.0% | ✅ |
| Energy / oil-refining | 2 | **9.82%** (`MPC`, `PSX`) | 8.0% | ✅ |
| Missile-defense / rearmament | 3 | 3.8% (`RTX`) | **unset** | ⚪ **n/a — reported, not passed** |

**✅ No top-rank cycle GAP. The 2026-07-14 postmortem's failure (0% of the #1 cycle) does not recur.**

### 🚨 But the lens's job is to attack, and there are three holes in that ✅

1. **`D250`, 11th run — the optical/interconnect cycle has NO registry row**, so `LITE`/`COHR`
   exposure is **unmeasurable, not zero**. And today those two are **the board's worst 5-session
   names (`COHR −20.37`, `LITE −13.13`)** and **the largest single contributors to `P79` entering
   branch B**. ⇒ **the ✅ is computed over a registry that omits the cycle doing the most damage.**
   The ✅ is downgraded to **⚠ UNDER-DETERMINED**, as the 08-24 run also found.
2. **Rank-3 has no threshold**, so `RTX` at 3.8% is neither passing nor failing — and `RTX` is this
   run's **🔴 분산 with `delta −0.629`, the book's largest negative**. A cycle whose only expression is
   distributing, against a threshold nobody has set, is not a ✅.
3. **The epicenter percentages are computed against a book whose AI-compute label spans 2–3 measured
   risk units at `--days` 250/500/750** (`D329`, and **G4 FAILED this run**). ⇒ **"16.59% of the
   epicenter" is one number where the instrument gives three groupings.** Per G4, it is quoted here
   **with its `--days` unavailable**, because `cycle_exposure` does not take one — which is itself the
   gap: **the exposure figure and the concentration figure are computed on different bases and cannot
   be read together.**

⚠ **What this lens could not independently check**: the registry itself. It read
`data_build/cycles/cycle_registry.json` as given and cannot know which cycles are missing except
through `D250`, which was found by a human, not by the instrument.

---

## §2 · Brackets registered this run — `S124` · `S125` · `S126` (all both-sided)

> **ID 3-grep at WRITE time** across `handoff/*.md` · `llm_outputs/**` · `REPORT/**`:
> `S124` `S125` `S126` → **0 hit in all three trees**. Current highest **`S123`** (2026-08-24).
> All three are added to `handoff/SCENARIOS_US.md` **and** indexed in the `handoff/SCENARIOS.md` spine
> at run end.

### `S124` — ★★★ Does IT's breadth repair through its own two prints? (the row that tests this run's ONLY verdict change)

| | |
|---|---|
| **Frozen observable** | **The COUNT of `us_top300` Information Technology names (n = 56) with a positive 5-session excess return vs `SPY`**, settled closes, at the **2026-08-31** close |
| **Branch A (our UW is wrong)** | **≥ 30** — the trailing-252 **median**. Breadth returns to normal through the `NVDA` (08-26) and `MRVL` (08-27) prints ⇒ **the IT downgrade was taken at a bottom decile** |
| **Branch B (our UW is right)** | **≤ 13** — no repair at all; the count stays at or below where it is today |
| **Branch C** | between = 14–29 |
| **`D93` executed BEFORE freezing** | trailing 252 of the count: mean **29.5** · sd **9.0** · p05 **13** · p15 **20** · p50 **30** · p85 **39** · p95 **43** ⇒ **A ≈50% · B ≈6% · C ≈44%. A is the favourite and is disclosed.** ⚠ That asymmetry is the point: **B is the rare branch and B is the one that vindicates us** |
| **State at registration** | **13 of 56 = the 5.6th percentile of two years** |
| **★ Implied move, and why this observable does not sit inside it** | `NVDA` **±6.13% (expiry 2026-08-28, D3)** · `MRVL` **±13.3% (expiry 2026-08-28, D3)**. **The observable is a CROSS-SECTIONAL COUNT, which no straddle prices** — an option chain prices one name's magnitude, not how many of 56 names beat a benchmark. ⇒ **the threshold is outside the implied move by construction**, and this is stated rather than assumed |
| **Information content (`B4`)** | **Both branches change a conclusion.** A falsifies the IT `UW` taken today; B converts it from a one-session-old call into a tested one. ⚠ **And this is deliberately NOT a fifth reading of the `NVDA` print** — `S79`/`S103`/`P90`/`S118` own the print itself; this row owns the **sector-breadth consequence**, which none of them measures |
| **Anti-signal (VOID)** | a **GICS reclassification moving ≥3 names into or out of Information Technology**, or a **market-wide trading halt**, inside 08-25 → 08-31. ⚠ **Base rate checked (`D300-KR`)**: **MSCI's 08-31 quarterly review falls inside the window and does NOT change GICS assignment**, so it is explicitly **not** a voider; a 3-name GICS reclassification in five sessions is not the base case ⇒ **the clause is not near-certain to fire.** ⚠ **The `NVDA` and `MRVL` prints are deliberately NOT anti-signals — they are the event** |
| **Non-redundancy (`D343`)** | 08-31 carries `S92`, `S94`, `S104`, `S112` and the MSCI review. **All four existing rows are single-name or single-pair; `S124` is the only cross-sectional breadth row on that date** |
| **Owner** | `industry_US` |

### `S125` — ★★ The agricultural half of the trade war, unbracketed for a third run

| | |
|---|---|
| **Frozen observable** | **`ADM` 5-session excess return vs `XLP`** (benchmark named inline — the sector, not the index, because the question is intra-Staples transmission), settled closes, at the **2026-09-11** close. The window **contains Canada's 2026-09-08 effective date** |
| **Branch A (the ag leg was priced in advance)** | **≥ +0.602** (trailing-252 **p50**) — `ADM` reverts to its median relationship with Staples through the implementation |
| **Branch B (the ag leg is the live transmission channel)** | **≤ −6.146** (trailing-252 **p05**) — it keeps underperforming its own sector through the effective date |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252: mean **+0.555** · sd **3.849** · p05 **−6.146** · p15 **−3.426** · p50 **+0.602** · p85 **+4.461** · p95 **+6.949** ⇒ **A ≈50% · B ≈5% · C ≈45%** |
| **State at registration, and the branch grading that follows from it** | **−6.511 = the 4.4th percentile**, i.e. **already inside branch B's region.** ⇒ **B is the LOW-information branch here and A is the informative one, and that is stated at registration rather than discovered at scoring** (`B4`). The row is a **persistence** test: does an already-extreme dislocation survive the event that is supposed to cause it? |
| **Implied move** | **none readable** — `ADM`'s nearest chain is not event-priced for 09-08. **Stated as unavailable rather than fabricated** (P4). ⚠ This is the `D2` caveat: a threshold taken from a non-event-dated straddle would be invented |
| **Information content** | **A falsifies** the desk's two-run-old claim that the ag leg is an un-modelled channel — it would mean the market already discounted it. **B confirms** it and dates the cost. ⚠ `ADM` is **not** a desk position and this row **hands no name to BET** (P4) |
| **Anti-signal (VOID)** | a **US–Canada agreement removing agricultural goods from the retaliation list**, or an **`ADM`-specific corporate action** (M&A, guidance withdrawal, restatement) inside the window. ⚠ Base rate: the tariff thread is **accelerating, not resolving** (`theme-age "Canada tariff"` **10.99×** on an 85 base, up from 9.86×) ⇒ the first clause is **not** near-certain |
| **Non-redundancy (`D343`)** | 09-11 currently carries **zero** rows. `S123` (09-12) brackets the **Industrials** leg over 09-05→09-12; **`S125` brackets the Staples/agricultural leg, which `S123` explicitly does not cover.** ⚠ **They are correlated** — one policy event, two sectors — and if both A-branches fire together that is **one object measured twice**, named here in advance |
| **Owner** | `industry_US` |

### `S126` — ★★ August payrolls: is the Industrials underweight a tariff call or a cycle call?

| | |
|---|---|
| **Frozen observable** | **`XLI` 5-session excess return vs `SPY`**, settled closes, at the **2026-09-04** close (NFP prints that morning) |
| **Branch A (our `UW−` is on the wrong side of a cycle)** | **≥ −0.087** (trailing-252 **p50**) — Industrials reverts fully to its median relationship on a labour-led rotation, **before** the tariffs take effect |
| **Branch B (the weakness is structural, not a dislocation)** | **≤ −2.500** (trailing-252 **p05**) — it stays in the bottom tail through the print |
| **Branch C** | between |
| **`D93` executed BEFORE freezing** | trailing 252 of `XLI exc5` vs `SPY`: mean **+0.012** · sd **1.619** · p05 **−2.500** · p15 **−1.572** · p50 **−0.087** · p85 **+1.767** · p95 **+3.121** ⇒ **A ≈50% · B ≈5% · C ≈45%** |
| **State at registration** | **−2.738 = the 2.8th percentile** — already below p05, so **B is the low-information branch and A is the informative one**, stated at registration (`B4`) |
| **Implied move** | `XLI`'s nearest chain is **not NFP-dated**; **no event-priced straddle exists for this observable** ⇒ stated as unavailable rather than invented (`D2`) |
| **★ Why this row exists at all** | `INDU UW−` is the desk's **stated live transmission channel** for the trade war, and **every existing test of it settles on the wrong dates**: `P92`/`P93` on **08-28, eleven days before the tariffs take effect** (`D342`), `S123` on **09-12, after**. **Nothing separates "Industrials is weak because of tariffs" from "Industrials is weak because the cycle is weak"** — and NFP is the one dated event in the window that moves the second and not the first |
| **Information content** | **A falsifies** the tariff attribution (the sector recovers on labour data, before any tariff takes effect). **B does not confirm the tariff story** — it only rules out the labour explanation — **and that asymmetry is stated rather than glossed** |
| **Anti-signal (VOID)** | an **intermeeting FOMC action**, or a **BLS release delay/cancellation** of the August employment report inside the window. ⚠ Base rate checked: no FOMC meeting falls inside; the BLS calendar carries 09-04 as scheduled ⇒ **not near-certain to fire** |
| **Non-redundancy (`D343`)** | 09-04 carries **zero** rows today. Against `S123` (Industrials EW, 09-05→09-12): **different date, different driver (labour vs tariff implementation), different construction (ETF vs equal-weight constituents).** If both fire the same way the correlation is named here |
| **Owner** | `industry_US` |

---

## §3 · Injections — what this stage hands forward

| To | What |
|---|---|
| **DEEP** | **Set UNCHANGED: `[ENRG, HLTH]` + `[MATR, IT]`, N = 4/4. No 5th slot promoted** — the only leg with a qualifying catalyst (UTIL/AI-power) was declined because its entire case is a Δ against a stub-bar snapshot (`D355`). ★ **IT's mandate is sharpened by lens 2a**: the sector was downgraded at **the 5.6th percentile of its own two-year breadth distribution**, and DEEP must address that directly |
| **ALPHA (action bracket)** | `S124` (08-31) · `S125` (09-11) · `S126` (09-04), all both-sided with frozen thresholds |
| **BET (epicenter starter)** | **No GAP to fill** — rank-1 and rank-2 epicenter exposure both clear. ⚠ But the ✅ is downgraded to **⚠ UNDER-DETERMINED** on three grounds (lens 4), and the strongest is that the registry has **no optical row for an 11th run** while `LITE`/`COHR` are the board's worst names today |
| **Book desk** | `RTX` 🔴 분산 with `delta −0.629` (book's largest negative) against a rank-3 cycle whose **threshold is unset** — flagged as a measurement gap, not a position call (P4) |
| **The next run** | 🚨 **REGISTRATION OBLIGATION: `AVGO` prints 2026-09-02 and no row on this board is keyed to it.** It is a held name, `rs60 −20.1`, and one of `P79`'s five legs. **Register after the 08-26/08-27 prints, from a 09-04-or-later straddle** (`D295`'s lesson applied forward) |

---

## ✅ EXIT CHECK
- [x] 4 lenses executed and each returned **named tickers + dated catalysts**. ⚠ **NOT a parallel agent
      fan-out** — declared deviation, 8th run, with each lens stating what it could not independently check.
- [x] **Every bracket names observable + frozen threshold + date, with BOTH branches.** `S124` `S125`
      `S126` registered; **zero one-way brackets**.
- [x] **Every magnitude threshold is stated against the implied move.** `S124` states that a
      **cross-sectional count is not priced by any straddle** and quotes `NVDA` ±6.13% / `MRVL` ±13.3%
      (both 08-28, D3) beside it. `S125` and `S126` state that **no event-priced straddle exists** and
      therefore **decline to fabricate one** (`D2`, P4).
- [x] **Each branch graded by information content**, including two rows (`S125`, `S126`) where the
      state is **already inside one branch** and that branch is pre-declared **low-information**.
- [x] **A binary was dropped with its reason stated** — July PCE 08-28, on `D343` (9 rows already);
      and MSCI 08-31, because neither branch would change a sector verdict.
- [x] `BLINDSPOT_PREMORTEM.md` written — legs · brackets · re-tags · cycle GAP.
- [x] **Every catalyst-bearing leg promoted or logged**: 5 legs, 0 promoted, 5 WITHIN-RUN-WATCH, each
      with the decline argued. **`AVGO` 09-02 handed forward as a registration obligation, not dropped.**
- [x] **DEEP set stated and unchanged** (N = 4/4), with the non-promotion argued by rule.
