# SECTOR_ROTATION — industry_US — 2026-08-05 (Wed) · **delta-only**

## §1 · Inherited — one line, verbatim from `MACRO_REPORT §G`

`MACRO holds: ENRG OW−− · IT N+ · FIN N+ · MATR UW− · UTIL UW · HLTH UW · INDU N · DISC N · COMM N− · STPL UW− · RE UW−`

Flow source: `SECTOR_FLOW_US.json` (**trimmed, asof 2026-08-04 settled** — see `SWEEP_READ §0`).
**Five sectors are unchanged and get no row**: FIN · HLTH · UTIL · COMM · STPL.

## §2 · Deltas — six, every one carried by a flow number

| Sector | matrix said | flow evidence (wflow · eqflow · breadth · Δd/d · 🟢/🔴) | **new verdict** | who resolves |
|---|---|---|---|---|
| **INDU** | **N** | **eqflow +0.156 > wflow +0.116 — the ONLY breadth-led sector on the board** · breadth **0.10 (highest)** · **🟢 5 of 50 = 5 of the board's 13** · Δ **+0.089** · **3 of the 7 new-🟢 ignitions** | **OW−** | **DEEP-INDU** |
| **ENRG** | **OW−−** | **wflow +0.360 — highest on the board** · eqflow **+0.215 (2nd)** · 🟢 **0** / 🔴 2 · breadth **0.00** · Δ **−0.133** | **OW−** (one notch back) | **DEEP-ENRG** |
| **IT** | **N+** | wflow **+0.175** vs eqflow **+0.017** ⇒ **mega-cap-narrow, 10.3× gap** · breadth **0.05** · 🟢 3 / **🔴 17 of 56** · Δ +0.158 | **N** (one notch down) | **DEEP-IT** |
| **RE** | **UW−** | Δ **−0.246 — the worst day-over-day deceleration on the board** · wflow −0.125 · 🔴 5 of 12 | **UW−−** | — (S25 settles 08-08) |
| **DISC** | **N** | **eqflow −0.037 NEGATIVE against wflow +0.077** ⇒ the mega-caps are carrying a sector whose breadth is not · **🔴 11 of 28** · Δ −0.094 | **N−** | — |
| **MATR** | **UW−** | Δ **+0.138 — 3rd-best acceleration on the board** against wflow −0.132 · 🟢 0, but **NUE (OBV +0.502, RS20 +17.3) and STLD (+0.312, +12.3) fail the gate on `vol_surge` alone** (`SWEEP_READ §5`) | **UW** (one notch up) | — (S36 today · S57 08-12) |

### ⛔ Attempts DECLINED as macro re-arguments (logged, per the EXIT CHECK)

- **ENRG to OW** on the Hormuz adjudication (S52-A unfired) — **declined.** That is MACRO's
  argument, not a flow number. The **only** admissible reason ENRG moved is **wflow +0.360 /
  eqflow +0.215**, and the notch stops at OW−.
- **UTIL to UW−−** on the electrical↔utility inversion (EVENT_ALPHA Card 6) — **declined as a
  verdict change.** UTIL's flow (wflow −0.353 / eqflow −0.349 / 🔴 10 of 15) **already** carries UW;
  deepening it on a *cross-sector* argument would be re-arguing the thesis. **The inversion is
  handed to DEEP as a question, not spent as a notch.**

### ⚠ The ENRG delta's honest weakness, stated where it is made

**Two of ENRG's three flow numbers point up and one points down, and the down one is the freshest.**
wflow **+0.360** and eqflow **+0.215** are levels; **Δ −0.133 is the change**, and it is the second
worst on the board. **C2 — both halves quoted.** ★ And the breadth number (**0.00**) that would
normally break the tie **is inadmissible today**: `SWEEP_READ §3` measured that **13 of 16 Energy
names carry OBV 매집 and 11 carry RS20 > 0, while `vol_surge` is below the 1.2 gate on all 16.**
**The sector's zero is a volume-axis censor.** ⇒ **the notch moves one step and stops.**

## §3 · DEEP picks — **N = 4** (protocol budget: 2 continuous + 2 rotating)

| Slot | Sector | Rule applied | The ONE question the DEEP must answer |
|---|---|---|---|
| **Continuous 1** | **ENRG** | **Anti-thrash continuity** — held a continuous slot every run since 07-27 and is **still a top OW today** ⇒ **keeps the slot** | **Is the −12.3% two-session crude move a war-premium deflation or a demand event — and does the answer change what the OW is standing on?** `S55`'s window is open (→08-11) and `S31` settles today between its own branches. |
| **Continuous 2** | **INDU** | **Today's other top OW rank** (promoted §2). ⚠ **FIN LOSES its continuous slot** — it was continuous every run since 07-27, but the rule requires *still top-N OW today* and FIN is **N+**. **Stated, not quietly dropped.** | **Is the breadth-led signal the AI-power ELECTRICAL leg, or is it the whole sector?** ETN·EMR·AME·PWR are 4 of the 5 greens. **W5 is the whole question.** |
| **Rotating 1** | **IT** | ★ **Written pre-commitment**: `DEEP_LOG 2026-08-04` reads *"IT(★next run's first rotating pick — 3 instruments converged)"*. **Honoured.** Last covered **07-31** ⇒ recency clean. | **XLK's exc5 is +5.13 (board's best) and its breadth is 0.05 with 17 reds. Which one is the sector?** Plus **S30 settles today** and the optical-ban thread (EVENT_ALPHA Card 1) sits inside IT. |
| **Rotating 2** | **UTIL** | ⚠ **Deliberate departure, stated rather than hidden.** The OW family is **exhausted at two**, and the rule says *never pad with Neutral/UW*. This is **not** padding: **`S35` + `S35-ANNEX` + `S47` ALL settle 2026-08-07 — 2 days out — on a sector nobody has deep-dived since 07-31**, and **R40 says the basket they settle on is contaminated.** Taking the slot to arrive un-prepared at three simultaneous settlements would be the worse error. | **Do S35/S47 survive R40 on the regulated SIX?** And: **is UTIL's collapse the same cycle as INDU's ignition, seen from the other side?** CEG prints 08-06, VST 08-07. |

**Not padded to a 5th.** ⚠ **HLTH is the board's 3rd-worst flow (wflow −0.253, Δ −0.201) and was
last covered 07-30 with a C7 re-check dated 08-06** — **it gets no slot and that is a real cost**,
logged below rather than absorbed.

## DEEP_LOG 2026-08-05: continuous=[ENRG, INDU] rotating=[IT, UTIL] · N=4/4 · FIN dropped from continuous (N+, no longer top-OW — first time since 07-27) · uncovered=[HLTH(UW, C7 re-check due 08-06 — ★next run's first rotating pick), FIN(N+, covered 08-04, S51 settles 08-10), MATR(UW, covered 08-03, S36 today + S57 08-12), RE(UW−−, worst Δ on board, covered 08-04, S25 08-08), DISC(N−, covered 08-03), COMM(N−, covered 07-28 — 8 runs uncovered), STPL(UW−, never claimed by a proposition — ADM/CTAS on the missed ledger, recheck 08-16)]
