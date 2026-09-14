# ACTION_TICKETS — 2026-08-23 · industry_US / L1·ALPHA

> **Pre-committed conditional MONITORING tickets. No order is sent by anything here, and no size is
> stated.** See the deviation note in §0.
> Book context (read-only, for scale): total ≈ **15,272,249원** · fx 1380 · invested **$5,126** ·
> `exposure_rule` state **정상**, target 95%, ledger band gap **−9.9pp (live bar)**.
> ⚠ **`n_new_sessions_since_prior_run = 0`.** Every price below is the **2026-08-21** settle.

## §0 · Two things about this file, both declared rather than hidden

**(1) 🚨 `D294` reproduces for a FIFTH time — this file is hand-built.**
`scripts/action_bracket.py`, run at 23:5x KST, printed these two lines **consecutively**:

> *"**Nearest binary:** NVDA earnings (D-3, axis=earnings) — both-sides armed below."*
> *"_No tickets — no cycle GAP and **no dated binary in window**._"*

**The window holds five binaries** (`NVDA` 08-26 · **`MRVL` 08-27** · Jackson Hole 08-27→29 · July PCE
08-28 · `AVGO` 09-02/03). The script names one in its own header and then denies all of them.
⇒ **The generated file is unusable and this one replaces it.**

**(2) Share counts are deliberately OMITTED, and this is a logged resolution of an open decision.**
The protocol describes tickets as carrying *"DRY-RUN share counts"*. **This run's operating mandate is
`Analytical output only — zero buy/sell recommendations`**, and an illustrative share count on a
conditional entry is the one element of a ticket that reads as a recommendation. ⇒ **Triggers,
thresholds, invalidations and dates are stated in full; sizes are not.** A human sizing any of these
would use `module_paper_book size` / `action_bracket` directly. **Logged as a deviation from
documented practice, not as an omission.**

---

## §1 · Both-sides brackets — one ticket per binary, each pointing at a registered scenario

| # | Binary | Date | Watch — branch A | Watch — branch B | Registered as |
|---|---|---|---|---|---|
| **T1** | **`NVDA` FQ results** | **2026-08-26** (corroborated to two bodies) | **Gross-margin guide ≤ the reported quarter's**, and the reported quarter ≤ +50bp vs prior ⇒ **cost pass-through confirmed**; the >15% price increase is defending a margin, not expanding one | **Guided GM ≥ +100bp** ⇒ pricing power; **`P90`'s premise is wrong** and the desk's *"memory level stays tight"* reading loses its only buy-side corroboration | **`P90`** |
| **T2** | same print, price leg | **2026-08-27** (first settled close) | 1-session return **≥ +7.0%** | 1-session return **≤ −7.0%** | **`S115`** — thresholds set **outside** the **±6.11%** implied move (08-28 straddle $13.12 / spot 214.72, ATM IV 0.606) |
| **T3** | 🚨 **`MRVL` FQ2 results — the binary the desk's calendar cannot see** | **2026-08-27** | **`MRVL` − `AVGO` 1-session spread ≥ +12.0pp** ⇒ the Alphabet share shift widens; `AVGO`'s **−14.7 rs60** is a franchise event | **spread ≤ −12.0pp** ⇒ over-priced; `AVGO`'s discount is a discount | **`S116`** — spread form per `D308`; `MRVL` implied **±11.31%** (ATM IV **1.122**, highest on the board) |
| **T4** | same print, memory read-through | **2026-08-27** | **`MU` − `NVDA` 1-session excess ≥ +3.0pp** ⇒ the information was about **memory** | **≤ −3.0pp** ⇒ `NVDA` beta, `MU` a levered follower | **`S117`** — registration fact: `MU` ATM IV **0.650** > `NVDA` **0.606** on one expiry, with **no `MU` print until 09-24** |
| **T5** | **Jackson Hole / Warsh debut** | **2026-08-27 → 08-29** 🚨 calendar-invisible | Dovish ⇒ the front-end rally that owns **3/4 of the 24bp steepening** extends; `DGS2` toward 4.08 | Hawkish ⇒ `DGS2` toward its 4.37 max; hits **HLTH** (the desk's longest-duration OW) and **DISC** | **`S112`** (registered 08-22, settles **08-31**) · macro leg **`P91`** (first business day ≥ 08-31, per `D309`) |
| **T6** | **July PCE** | **2026-08-28** | core PCE MoM **≤ +0.20%** ∧ `DGS2` ≤ 4.10 ⇒ the run-rate wins the wedge (headline 3m-ann. **+0.49%** vs YoY **+3.30%**) | core PCE MoM **≥ +0.35%** or `DGS2` ≥ 4.32 ⇒ the YoY side wins | **`P86`** (registered 08-22) |
| **T7** | **US–Canada 50% tariff, already IN FORCE since 08-22** | settles **2026-08-28** | `XLI` 5-session excess vs `SPY` **≤ −2.50pp** **or** `XLB` **≤ −1.00pp** ⇒ it prices | **both** `XLI` ≥ −0.50pp **and** `XLB` ≥ +2.00pp ⇒ headline only | **`P92`** |
| **T8** | **`AVGO` FQ results** | **2026-09-02 or 09-03** ⚠ one-day ambiguity, unresolved | Guides AI revenue **below** the prior quarter's sequential growth rate, **or** rs60 vs `SPY` still ≤ −10 at the first settled close after ⇒ franchise event | rs60 recovers **above −5** **and** the print names a replacement custom-silicon win ⇒ one-customer scare | EVENT_ALPHA **Card 3**; implied **±9.51%** (09-04 straddle, ATM IV 0.643) |
| **T9** | `FRO` print | 2026-08-28 | — | — | 🚫 **No ticket.** No branch would change any conclusion — the desk holds no tanker and carries no tanker proposition. **Dropped with the reason stated** |
| **T10** | MSCI quarterly review | 2026-08-31 | — | — | 🚫 **No ticket.** Index-mechanical, no directional content |

## §2 · Cycle-GAP core-starter — **none required**

`cycle_exposure.py`: **AI-compute epicenter 16.52%** (need ≥12.0) ✅ · **Energy/refining 9.84%**
(need ≥8.0) ✅ · Missile-defense 3.79% ⚪ (no threshold set). **No top-rank cycle GAP ⇒ no
tape-independent core-starter is written.**

🚨 **But two cycles have no registry row and are therefore UNMEASURABLE, not zero:**
- **Optical / interconnect** (`D250`/`M731`, unfixed): `LITE` +0.639 (blocked on surge 0.95) ·
  `COHR` +0.158 · `CIEN` −0.380 🔴 rs60 −34.0.
- ★ **Custom-silicon / merchant-ASIC** (new, `M838`): the book's 16.52% "epicenter" conflates
  *sells the accelerator* (`NVDA`, `ANET`) with *co-designs someone else's* (`AVGO`), and **`M837`
  measured `NVDA` as a singleton risk unit in all three windows (250/500/750d), never grouped with
  `AVGO`.** ⇒ **`label_split_across_units` — the theme cap is TOO TIGHT on this book. Human call.**

## §3 · 🟡PARTIAL residuals — dated appointments, handed to `carryover`

| Name | Residual | **Re-check date** |
|---|---|---|
| `MU` · `SNDK` · `LRCX` · `STX` | flow **level** still negative while the one-session **delta** ranks 7/10/16/42 of 299 — a rate inflection, not accumulation | **2026-09-03** (miss ledger, filed) |
| `MRVL` | LATE-MONEY: 32.0pp rs60 spread over `AVGO` already realised | **2026-09-19** (miss ledger, filed) |
| `REGN` · `ABT` · `COP` | blocked from 🟢 by `vol_surge` alone, with the other two axes clear | **2026-09-19** (miss ledger, filed) |
| `VST` | consensus target **+61.9%** above spot against the sector's worst rs20 (−20.3) | **2026-09-03** (miss ledger, filed) |
| `CAH` · `ISRG` | screener raw candidates, turn unconfirmed | **2026-09-19** (miss ledger, filed) |
| `S102` | FRED daily series unreadable by a weekend desk (`D309`, 5× replicated) | **2026-08-24 run**, handed explicitly |
| `S8` | undated, unscoreable — **22nd consecutive run** | **A human must VOID or date it (P5)** |

## §4 · Standing stamps that travel with every ticket above

1. **Every 🟢 on this run's sheet is partly a `vol_surge` selection**, and that axis is measured
   **t(NW) −3.86 (h=1) / −3.38 (h=5)**, past Bonferroni, **negative** — in a **`market=kr`** ledger.
   **`W1` bars this desk from acting on it** (`D310`, open 2 runs).
2. **`ANET` carries the only 🔴 short-surge on the book** (FINRA z **+1.82**, 5v5 +3.9▲) **into** the
   book's largest positive one-session delta. **Momentum-only flag: hard stop required if acted on.**
3. **`AVGO` shorts are COVERING into a −14.7 rs60** (z −2.53) — the **third `M804` instance this run**
   (`RTX` z −2.15 into delta −0.304; `LHX` on 08-21). **Covering into decline removes a future buyer;
   it is not a bottom signal.**
4. **🚨🚨 `ARMED (TIMEFOLIO_EXECUTE=1)`** sits on every `exposure_rule` ledger row. **Named, not
   touched. No stage in this protocol may pass `--execute`.**

*Analytical / scheduling artifact — zero buy/sell advice, zero sizing. Tickets are pre-committed
conditionals; a human executes separately, and nothing here sends an order.*
