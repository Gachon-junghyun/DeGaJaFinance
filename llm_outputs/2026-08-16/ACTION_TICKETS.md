# ACTION_TICKETS — industry_US · 2026-08-16 · Stage 10/11 (L1·ALPHA)

> **Freshness gate output.** Separates "interesting" from "bettable NOW". Benchmark **`SPY`** named
> inline (C1). Prices settled **2026-08-14**. **Zero buy/sell recommendation (P4)** — these are
> analytical tickets: what would have to be true, by when, and what kills it.

## §0 · 🚨 The instrument check this stage is required to run BEFORE reading its own zero

`theme_age` was probed **six times at 22:56–22:57 KST**, `--scope foreign`. **All six returned values**
— the remote bridge answered every call. So the result below is **not** a pipe artifact, and for the
first time this desk can separate the two explanations:

| Theme probed (22:56–22:57 KST) | Verdict | Age | 7d avg | Accel | Total 90d |
|---|---|---|---|---|---|
| `refinery` | **⚪ECHO** | ≥90d | 47.0 | **1.69×** | 1,400 |
| `optical` | **⚪ECHO** | ≥90d | 48.1 | **1.70×** | 1,724 |
| `retail` | ⚪ECHO | ≥90d | 332.3 | 1.48× | 12,450 |
| `sales` | ⚪ECHO | ≥90d | 834.3 | 1.43× | 30,023 |
| `assets` | ⚪ECHO | ≥90d | 582.7 | 1.36× | 23,044 |
| `alternative` | ⚪ECHO | ≥90d | 211.1 | 1.35× | 8,464 |
| `Hormuz` | ⚪ECHO | ≥90d | 195.3 | 1.33× | 8,461 |
| `diesel` | ⚪ECHO | ≥90d | 35.0 | 1.22× | 1,319 |

★★ **Zero 🟢FRESH · zero 🟡ACCELERATING · zero 🔴FADING. Eight probes, one verdict.**
The 🟢FRESH gate requires **age ≤14d AND accel ≥2×**. **Every theme this desk trades is >90 days old**,
and the highest acceleration on the board is **1.70×** — below the 2× threshold. ⇒ **The gate is
arithmetically unreachable on this corpus.**

🚨 **This closes a question `F1` has carried for 8+ runs.** Until today, "🟢LIVE fired 0 times" could
not be separated from "the pipe was dead" — the KR desk logged **18 consecutive zeros** without being
able to tell which. **Today the pipe answered 8 of 8 and the gate still cannot fire.** ⇒ **`F1` is a
property of the GATE, not of the instrument, and not of the market.** A gate that never fires looks
identical to a universe with nothing in it; **this is the measurement that tells them apart.**
⚠ **The correct inference is NOT "nothing is fresh."** It is: **`theme_age` as configured cannot grade
this desk's themes, so every tag below is issued on the LIVE evidence axis and the theme axis is
reported as non-discriminating.** (`M112`/`M154` reproduced a **fourth** time.)

⚠ **And the reverse is forbidden too** (PREFLIGHT G1): an ⚪ECHO reading may **not** be written as
"the theme has cooled." `refinery` at ⚪ECHO carries **1.69× acceleration and five dated strikes in six
days** — the tag and the world disagree, and the tag is the weaker instrument.

---

## §1 · Freshness tags — `BET_SHEET §B` is updated to match

| Ticket | Sector | Tag | Residual (what is NOT yet resolved) |
|---|---|---|---|
| **T1 · `MPC`** | ENRG | **🟡PARTIAL** | The catalyst **has partly fired** — the Salavat strike was **08-13** and the name ran **+19.19% in the five sessions to 08-14**. What is unresolved: whether the *mechanism* continues (further dated strikes) or the *off-switch* fires (`S92` branch C) |
| **T2 · `ABNB`** | CONSUMER | **🟡PARTIAL** | The wallet-share split is **registered but untested**. `S93` settles **08-21** on three prints that had not landed at registration |
| **T3 · `KKR`** | FIN (LIVE) | **🟡PARTIAL** | `M669`'s relocated breadth node has **one confirming date** (08-15) and its falsifier `S78` settles **08-19**. Its estimate book is split (0y +3.7% / +1y **−1.5%**) |
| **T4 · `PSX`** | ENRG | **🟡PARTIAL** | Same thesis as T1 at a cheaper multiple, **filtered out of its own shortlist on `vol_surge` 1.01** (`D251`, 2nd run). Residual = the filter, not the thesis |
| **T5 · `LITE`** | IT (LIVE) | **🟡PARTIAL** | Its 🟢 is **dated to its own 08-11/08-12 print** ⇒ reaction volume. Residual = whether accumulation survives the roll-off, **≈08-25** |
| **T6 · `COHR`** | IT (LIVE) | **🔴 NOT ISSUED — see §2** | — |
| — | — | **🟢LIVE: ZERO tickets** | **Structurally impossible today** (§0). Recorded as an instrument fact, **not** as "nothing qualifies" |

⚠ **No 🔴RESOLVED tag was issued either.** A 🔴 means *the catalyst has fired and the move is done*, and
it drops a name from the bettable list with a ledger row. **Nothing on this sheet meets that test**:
`MPC`'s mechanism is still producing dated events, and `COHR`'s problem is price structure, not a
consumed catalyst.

---

## §2 · The name that got NO tag — and it is written down, not dropped

★ The L1 is explicit: *"a name carried into ALPHA that receives no tag at all… is not a 🔴; it is a
**missed** entry, and it leaves no record unless you write one."*

**`COHR`** carried the **board's highest `flow_score` (+0.99)** and the **universe's largest
`vol_surge` (1.67)** into this stage and receives **no tag**, because the two axes that would decide it
point opposite ways and neither is dispositive:
- **Against**: it **round-tripped** — 379.13 (08-07) → **325.83** (08-14), **−14.06% in five sessions**,
  **−14.457pp excess vs `SPY`**, closing **below its own ignition trigger of 332.48** and above only
  **2 of 4** MAs (turn verdict **NEUTRAL/CHOP**).
- **For**: its OBV is **누적, 20d slope +57%** — accumulation is still rising *underneath* the
  round-trip, and `optical` carries the **joint-highest acceleration of the eight probes (1.70×)**.

⇒ **Filed to `missed_ledger`** rather than rejected or tagged:
`COHR · Q.확신부족 · --enters-if "closes above 332.48 with vol_surge ≥ 1.0 on a settled close" ·
--recheck-date 2026-08-25`.
**`LITE` filed alongside it** — `R.타이밍대기`, same recheck date, `--enters-if "holds OBV 매집 ∧ RS20>0
with vol_surge ≥ 1.2 after the print volume rolls off"`.
⇒ **Ledger totals after this stage: reject 176 / missed 136 (four rows added this run: `MSTR`, `RIOT`,
`COHR`, `LITE`), legacy 0 on both.**

---

## §3 · Action tickets — each with its trigger, its invalidation, and its date

> **P4**: these are analytical brackets. No order, no size, no recommendation. Any size language
> anywhere downstream is **"mechanical ¼"** (PREFLIGHT G6 — the `--ic` input is not evidence-backed:
> accrual **0.42 files/day vs an ideal 1.0**, ETA **≈72 days vs 30**).

### T1 · `MPC` — the cycle-GAP epicenter, post-move
| | |
|---|---|
| **Why it is a ticket** | 🚨 `CYCLE_EXPOSURE` GAP on the **rank-2** cycle: epicenter **7.1%** vs an **8.0%** floor = **−0.898pp**. The standing rule: a crowded/🔴 tape gates ADD *timing*; it never justifies zero core |
| **State (08-14)** | 355.42 · **🟢가속, 3-axis producible** · OBV 매집 · RS20 **+9.3** / RS60 **+29.3** vs `SPY` · `vol_surge` 1.25 · FINRA **z −0.71 clean-rise**, 2.8% float `covering`, DTC 3.4 |
| **Implied move** | **±4.4%, expiry 2026-08-21 (D5)** — genuinely covers the window. A move inside ±4.4% is **pre-declared no-information** |
| ⚠ **Timing caveat, stated at full weight** | The name ran **+19.19% in five sessions** and its chart reads **BREAKOUT at the upper Bollinger band, RSI 69.9, OBV 중립 (20d −3%) and a BEARISH RSI divergence.** **The GAP is being measured after the move** |
| **Invalidation** | `HO=F` − `CL=F` 20d gap **≤ 0pp** (08-21) · two consecutive negative weekly crack accelerations · close below **297.75** (the 08-05 base) · **`S92` branch C** — a US-brokered halt to strikes on Russian energy infrastructure, ≥3 outlets, by **08-31** |
| **Date** | 2026-08-21 (`P62`/`P66`) · 2026-08-31 (`S92`) · next issuer event **2026-11-03** |

### T2 · `ABNB` — the one name in the consumer complex the money confirms
| | |
|---|---|
| **State (08-14)** | 184.06 · **🟢가속, 3-axis producible** (`vol_surge` **1.55**) · OBV 매집 · RS20 **+21.6** / RS60 **+34.5** vs `SPY` · exc5 **still positive +2.966** ⇒ **not** `M149`'s decaying shape · FINRA **z −0.94 clean-rise**, 3.1% float `covering`, DTC 3.9 · P/C 0.85, skew +30.8 |
| **Implied move** | **±3.2%, expiry 2026-08-21 (D5)** |
| **Trigger to watch** | `S93` **branch B**: `ABNB` − `HD` 5-session excess spread vs `SPY` **> +5pp** (currently **+8.077pp**) ⇒ the wallet-share bottleneck is a real unit and the GICS label is the wrong object |
| ⚠ **Against it** | **Forward 29.98× · P/S 8.38 · P/B 13.92.** The estimate book is **+3.9% in 7 days after 83 days flat** — **n=1 (S1)**, not a trend. **This sheet does not make a value case** |
| **Invalidation** | RS20 turns negative while RS60 stays positive (Lens 3's flip condition) · spread **< 0** · 🚨 VOID on a consumer-goods tariff announcement |
| **Date** | **2026-08-21** (`S93`) · the three prints: `HD` ~08-19, `WMT` ~08-20, `TGT` ~08-20 |

### T3 · `KKR` — Financials' only admissible 🟢, and the most expensive optionality on the sheet
| | |
|---|---|
| **State (08-14)** | 114.01 · **🟢가속, 3-axis producible** (`vol_surge` 1.49) · OBV 매집 · RS20 +8.5 / RS60 **+16.9** vs `SPY` · forward **15.43× on PEG 0.59** — the cheapest growth-adjusted multiple on the sheet |
| ⚠ **Positioning is two-sided and both sides are stated** | FINRA **z +1.62 = ⚡crowded-short** (squeeze fuel **conditional on a turn**, never a standalone read, D6) — **but** options **P/C 1.20 = put-heavy (fear)** and the **implied move is ±10.8% (expiry 08-21, D5)** on a name with **no scheduled print**. ★ **A ±10.8% five-day straddle with no event is the widest unexplained implied move on this sheet** ⇒ the market is pricing something the desk has not identified. **`unknown` (C3)** |
| ⚠ **Estimate book disagrees with itself** | 0y **+3.7%/90d** while **+1y is CUT −1.5%/90d** ⇒ consensus is pulling earnings **forward**, not raising the level |
| **Invalidation** | `S78` (settles **08-19**) · `eqflow` stays below `wflow` in Financials ⇒ `R69` holds and the sector's breadth relocation is not spreading |
| **Date** | **2026-08-19** |

### T4 · `PSX` — the `D251` ticket: a sector leader its own filter removes
| | |
|---|---|
| **State (08-14)** | 233.61 · 🟡중립 **only because `vol_surge` is 1.01** — OBV 매집 ∧ RS20 **+8.5** both pass · RS60 **+22.3** vs `SPY` · exc5 **+14.17pp** · forward **11.11×**, **PEG 1.35**, **P/B 2.96** — cheaper than `MPC` on both |
| ★ **The ticket is about the instrument** | `PSX` and `VLO` are the sector's **#2 and #3 on RS60** and are excluded from its shortlist by a **volume** ratio, in a week whose **median last-bar volume is 0.649× the 20-day norm** (`D270`). **The filter is measuring the tape's thinness, not the name** |
| ★ **Its revision leg is the most extreme on the sheet — and it just turned** | 0y **16.30 → 25.80 = +58.3%/90d**; **0q 9.56 (7d ago) → 9.25 now = −3.2%, the first negative in the series.** Read on the second derivative (lens B1): **level extreme, rate turned. n=1 (S1)** |
| **Invalidation** | same as T1 (one risk unit with `MPC` at `--days` 250, 500 **and** 750) |
| **Date** | 2026-08-21 · 2026-08-31 |

### T5 · `LITE` — a timing ticket, not a thesis ticket
| | |
|---|---|
| **State (08-14)** | 926.14 · 🟢가속 3-axis producible (`vol_surge` 1.27) · OBV 매집 · RS20 **+21.9** · exc20 **+21.934** vs `SPY` and it **held** the move (unlike `COHR`) · best estimate book on the sheet (**+1y +7.0%/90d**) |
| ⚠ **Why it is only 🟡** | The green is **dated to its own 08-11/08-12 earnings print** ⇒ **reaction volume, not accumulation**. **P/S 27.22 · P/B 22.33** |
| **Trigger** | `vol_surge ≥ 1.2` **with** OBV 매집 ∧ RS20>0 **after the print volume rolls off** |
| **Date** | **≈2026-08-25** (also its `missed_ledger` recheck) |

---

## §4 · Where this stage's tickets do NOT go — the cycle the registry cannot see

🚨 **`S94`**: `cycle_registry.json` is **29 days stale**, its rank-3 floor is **0.0** (check OFF), and
it has **no entry** for **optical/interconnect** or **custom AI silicon**. `optical` carries the
**joint-highest acceleration of the eight probes (1.70×)** and the desk holds **zero** exposure to it.
⇒ **The epicenter-starter module in `BET_SHEET §GAP` can only be built for cycles the registry
contains.** For this one it **structurally cannot**, and PREMORTEM Lens 4 returns ✅ anyway.
**No ticket is issued. The gap is registered as a bracket (`S94`, settles 08-31) and handed to a human
(P5).**

---

## ✅ EXIT CHECK

- [x] 🚨 **The pipe was checked BEFORE the zero was read** (§0) — `theme_age` answered **8 of 8** probes
      at 22:56–22:57 KST, so the zero-🟢FRESH result is **arithmetic, not a tunnel failure**. ★ This is
      the measurement that separates `F1`'s two explanations for the first time.
- [x] **`theme_age` run FIRST, deterministically, token-0** — 8 themes, all values quoted with their
      probe time (PREFLIGHT's conditional permission satisfied). **No ⚪ECHO reading was written as
      "cooled"** — the inverse is explicitly forbidden and `refinery` is the worked counter-example.
- [x] **`module_flow --positioning` run per candidate** — implied moves **`MPC` ±4.4% · `ABNB` ±3.2% ·
      `KKR` ±10.8%**, all expiry 2026-08-21 (D5), all genuinely covering their windows. ⚠ `NVDA`'s
      straddle was **disqualified** (expires 08-17, prints 08-26 — `M47`).
- [x] **Every bet tagged 🟢LIVE / 🟡PARTIAL / 🔴RESOLVED with its residual stated** — 5 × 🟡PARTIAL,
      **0 × 🟢LIVE (with the arithmetic reason)**, 0 × 🔴RESOLVED (with the reason none qualified).
- [x] **The untagged name is written down, not dropped** (§2) — `COHR` **and** `LITE` filed to
      `missed_ledger` with `--enters-if` **and** `--recheck-date`, per the F1 lesson that a gate which
      never fires leaves no row.
- [x] **`BET_SHEET §B` freshness placeholders resolved** — the tag table in §1 is the update.
- [x] **Cycle GAP carried forward with its action bracket** (§4 · `BET_SHEET §GAP`), and the GAP is
      disclosed as **identical to the prior run, not widening**.
- [x] **No buy/sell recommendation, no size** (P4). Any downstream size language is **"mechanical ¼"**.
