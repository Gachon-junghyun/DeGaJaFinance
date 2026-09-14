# SWEEP_READ — industry_US — 2026-08-03 (Mon) · reading only (tables live in the JSONs)

## 1 · Universe headline — three numbers

**n = 300 · wflow (Energy, #1) +0.567 · 26 🟢 / 82 🔴.** `asof 2026-07-31` ✅ — **no D74 trim was
needed and none was applied**, because at a 09:1x ET pre-open clock **no 08-03 equity bar exists.**
Artifacts: `SECTOR_FLOW_US.json` · `US_LIVE_SHORTLIST.json` · `CYCLE_EXPOSURE.md/.json`.

---

## 2 · ★★★ The controlled experiment: **D126 is confirmed, isolated, and quantified**

MACRO §I asked SWEEP to treat this run as a controlled test — **same settled date, second pull, two
days apart, zero new price information.** It is the first time this desk has been able to separate
*instrument noise* from *market movement*, because the market half is held at zero.

**Result — `SECTOR_FLOW_US.json` (08-02 run) vs `SECTOR_FLOW_US.json` (this run), both `asof 2026-07-31`:**

| | 08-02 run | this run |
|---|---|---|
| `velocity` non-null | **0 / 300** | **51 / 300** |
| 🟢 count | **16** | **26** |
| 🟢 that disappeared | — | **0** |
| 🟢 that appeared | — | **10: AMZN · AVGO · BAC · CSCO · CVX · JPM · MA · NVDA · WDC · XOM** |

⇒ **Ten greens were manufactured by a code-level join, on identical prices.** The change is **purely
additive**, which is the signature the mechanism predicts: `has_conviction = (obv=="매집") or (vel ≥ 1.2)`
— when the `velocity` join is wired, it can only *add* a path to 🟢, never remove one.

### ★★★ And it is not confined to the tag — **three sectors flipped the SIGN of their wflow**

| Sector | wflow 08-02 run → this run | eqflow |
|---|---|---|
| **Communication Services** | **−0.217 → +0.061** 🔄 sign flip | −0.071 → +0.031 🔄 |
| **Health Care** | **−0.112 → +0.045** 🔄 sign flip | −0.051 → −0.002 🔄 |
| **Consumer Staples** | **−0.130 → +0.003** 🔄 sign flip | −0.126 → −0.091 |
| Information Technology | +0.081 → **+0.264** (3.3×) | −0.144 → −0.041 |
| Financials | +0.086 → **+0.214** (2.5×) | +0.123 → +0.161 |
| Cons. Discretionary | +0.072 → **+0.216** (3.0×) | −0.045 → −0.013 |
| Energy | +0.519 → +0.567 | +0.463 → +0.475 |
| Industrials | +0.001 → +0.028 | +0.048 → +0.053 |
| **Real Estate · Utilities · Materials** | **identical to 3dp** | identical |

**8 of 11 sectors moved and 3 changed sign, with no price input.** The three that did **not** move
(RE, UTIL, MATR) are the three with **zero or one 🟢** — i.e. exactly the sectors the velocity path
had nothing to add to. **The mechanism explains its own exceptions**, which is what makes this a
measurement rather than a coincidence.

⚠⚠ **This is a finding AGAINST the desk's own recent output.** ROTATION promotes and demotes on these
numbers. The 08-02 run demoted **Health Care to N−** citing, among other things, a negative sector
flow; on the identical settled bar that flow now reads **positive**. **The demote may still be right
on other evidence (XLV exc20d −1.03, and the 08-02 run explicitly withdrew its green-count leg
already) — but the flow leg of it is not reproducible, and no stage may cite a `wflow` sign this
run without stating which pull it came from.**

★ **M144's blocked-side mechanism replicates an EIGHTH time, and it is the stable half:**
**85 names pass `OBV-accumulation ∧ RS20 > 0`; 25 are 🟢; 60 are blocked and 60 of 60 fail on
`vol_surge` alone**, with the **highest blocked `vol_surge` at 1.190 against a 1.20 gate — 0.01
away.** The *blocking* rule is deterministic and reproduces across two markets and six dates; only
the *unlocking* rule oscillates. ⇒ **D6 binds as before: a 🟢 count is a volume test wearing a flow
label, and this run adds that the label is not even stable run-to-run.**

⇒ **D126 is upgraded from "oscillation observed" to "oscillation isolated, with a measured
magnitude: 10 tags and 3 sector signs."** Needs a human (behavioural change to a live shared module,
D11-class). **Not fixed here.**

---

## 3 · Cross-checks against the MACRO matrix — one confirm, one contradict, one that cannot be read

**CONFIRMS — Energy.** The sweep's **#1 wflow (+0.567) with ZERO reds of 16 and eqflow +0.475**
agrees with the matrix's ENRG **OW−** and with MACRO §D's revision finding (the crack break was 28%
smaller than the prior run recorded). ⚠ **This is one of the three sectors that barely moved between
pulls**, so it is one of the few flow readings this run can quote without a pull caveat.

**CONTRADICTS — Utilities is confirmed by the very instrument that is unstable elsewhere.**
UTIL is **−0.284 wflow / −0.289 eqflow, identical to 3dp across both pulls, 1🟢 / 8🔴** — and XLU is
the board's worst on **all three** windows (§B of MACRO). ⇒ **the UW− is the single cleanest read on
the board and it needs neither the contaminated regulated-seven basket (R40) nor a stable velocity
join.** That is worth stating positively: *the one sector verdict this run can make without any
instrument caveat is Utilities UW−.*

**CANNOT BE READ — Information Technology.** wflow moved **+0.081 → +0.264 (3.3×)** and greens
**4 → 8** on frozen prices. The matrix holds **N (split, asymmetric)** on P3/P10/P15, none of which
is a flow argument — **so the matrix survives, but any stage tempted to promote IT on "flow improved"
would be reading the join, not the tape.** Flagged for ROTATION.

---

## 4 · Shortlist composition — the absences, and one presence that is a bigger finding

`US_LIVE_SHORTLIST.json` — 15 names, mcap ≥ $10B, 🟢 filter, flow-desc.

**★★ The presence that matters: 4 of the 15 were REJECTED by the previous run, one run ago.**
The 08-02 run filed **GRMN · EA · TRI · PSX · ICE** to the reject ledger with revival conditions and
recheck dates. **GRMN (#1 flow, +0.92) · ICE (+0.79) · TRI (+0.78) · EA (+0.75) are all back on
today's shortlist** — and **not one of their revival conditions has been met**, because *nothing
happened*: same prices, same books, rechecks dated **08-12 / 08-16**.

⇒ **The shortlist instrument re-surfaces rejected names on identical data.** This is precisely what
the rejection ledger exists to prevent, and it would have leaked into BET unexamined. **All four stay
rejected**; their `--revives-if` conditions govern, not the tag. ⚠ **And `EA` and `TRI` additionally
carry the "✅ 청정 상승" badge**, which is the most persuasive label the instrument emits — **a
rejected name wearing a clean-rise badge is the highest-risk row on this sheet.**

**Absences, each diagnosed rather than cited:**

| Sector | 🟢 count | Diagnosis |
|---|---|---|
| **Materials** | **0** | ⚠ **Filter artifact, pre-registered.** M273/M238 measured 5 of 12 passing the accumulation pre-condition with **all 5 blocked by `vol_surge` alone** (sector max 1.14 vs a 1.20 gate). ⇒ **S36's confirming leg is disqualified; the bracket can only falsify the UW.** Not evidence. |
| **Real Estate** | **0** (and **0 reds**) | ⚠ **Genuinely inert, not filtered** — wflow +0.078 / eqflow +0.091, **identical across both pulls**, zero tags either way. The sector is not being sold; it is not being traded. **S25 already scored zero-information (D122)**, so RE currently has no live instrument at all. |
| **Health Care** | **0** of 32, **7 reds** | ⚠ **Mixed, and this run cannot separate them.** The 08-02 run measured 6 names passing the pre-condition with all 6 blocked by `vol_surge` ⇒ artifact; but the sector's flow **sign flipped between pulls** (§2), so **the flow evidence is unusable this run and only the 7 reds and XLV exc20d −1.03 survive.** ⇒ **C7's resolving observable stays undefined (M278) and unreadable.** |
| **Energy** | **3** of 16, **0 reds** | ✅ Real. The board's only zero-red sector, and stable across pulls. |

---

## 5 · CYCLE_EXPOSURE — one 🚨 GAP, and its magnitude is `unknown` by this desk's own retraction

Book (read-only KIS): total ≈ **$10,618** · invested **$5,741** · cash ₩5,685,059.

| Cycle | rank | epicenter % | need | held | flag |
|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | **12.96%** | 12.0% | AVGO · NVDA · TSM | ✅ (**+0.96pp**) |
| **Energy / oil-refining** | 2 | **6.89%** | 8.0% | MPC · PSX | 🚨 **GAP (−1.109pp)** |
| Missile-defense / rearmament | 3 | 8.13% | — | RTX | ⚪ no floor set |

★ **AI-compute flipped 🚨GAP → ✅ on drift again — M146/M181/M209/M246's pattern, now a 9th reading.**
The held set (AVGO, NVDA, TSM) is **unchanged**; the margin ran **−3.683pp (07-29) → +0.96pp** with
**nothing bought.** Both flags now sit **outside** D61's proposed ±0.5pp band, so **both are real
rather than unresolved** — the first run in which that is true of both.

⚠⚠ **The Energy GAP's MAGNITUDE may not be quoted, and this is R39 firing exactly as written.**
The registry excludes **XOM** from the Energy epicenter on the ground that it is *"0% refining"* —
**a claim this desk retracted on 2026-08-02** after XOM's own segment disclosure printed **$4.1–5.5bn
of refining, a four-year high.** ⇒ **the 6.89% is computed on a wrong tag and understates by an
unknown amount (C3).** The GAP's **existence** is not in question; its **size** is. **Registry
correction needs a human.**

⚠ Second caveat, from this desk's own last run: **PSX — one of the two names carrying that 6.89% —
was filed 🔴RESOLVED at ALPHA on 08-02** on three agreeing axes. **The GAP is therefore partly held
by a name the desk has already resolved against.** Handed to ALPHA's action bracket.

⚠ Third, unchanged for a 6th run: **TSM and LNG are outside `us_top300`** (M252) ⇒ **the instrument
that grades every other holding cannot see a rank-1 epicenter holding.** The ✅ above is computed on
a book the sweep cannot fully tag.

---

## 6 · Hand-forward to EVENT_ALPHA / ROTATION

1. ⚠⚠ **No `wflow` sign may be cited this run without naming its pull.** Three flipped on frozen data.
2. ✅ **Quotable without caveat: Utilities UW− · Energy OW− · the 60/60 `vol_surge` block.**
3. ⛔ **Not quotable: any IT or Health Care flow improvement.**
4. ⛔ **GRMN · EA · TRI · ICE stay rejected** — their conditions are dated 08-12/08-16 and nothing has
   happened. **PSX stays 🔴RESOLVED.**
5. 🚨 **Energy GAP exists, size `unknown` (R39).** To ALPHA.
