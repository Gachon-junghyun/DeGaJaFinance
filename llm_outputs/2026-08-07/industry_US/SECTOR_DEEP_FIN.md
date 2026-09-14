# SECTOR_DEEP_FIN — Financials · industry_US · 2026-08-07 · **CONTINUOUS track → DELTA ONLY**

> Structure carried by reference to `llm_outputs/2026-08-06/industry_US/SECTOR_DEEP_FIN.md` (§2 method, §5
> A6/velocity contamination, §6 rate table) and `2026-08-04`'s regression/sub-node work. Neither is
> re-printed or overturned below except where a fresh primary changes the finding, named. Benchmark **SPY,
> inline**, everywhere (**C1**). **P4 — analysis only. No position language, no sizing.** Prices/flow:
> `SECTOR_FLOW_US.json`, **asof 2026-08-06 settled**. Rates: `[FRED]`, newest common date **2026-08-05**.
> Three bank primaries below are Q2-2026 10-Qs filed **this week** (JPM 08-06, GS 08-03, BAC 07-31) — the
> "8 months stale" caveat from 08-04/08-06 is **retired for these three names only.**

---

## 0 · The one-line answer

**OW− is arithmetically survivable — carried by wflow rank 2 (still positive), a never-negative 16-session
eqflow floor, and the sector's strongest un-owned leg (GS/JPM/BAC revision books) — but it now has zero
margin left: WFC is confirmed out on both flow and revisions, three of six remaining greens are
velocity-only, GS's 5-run split stays a genuine (not artifactual) flow/fundamental gap, and the freshest
primary filings show the sector's actual NII engine is balance-sheet volume, not curve shape — so a BULL
steepener (today's live risk, MACRO §0-a/§0-b) threatens the same volume leg it would need to protect,
unlike the bear steepener the original OW thesis assumed.**

---

## 1 · Delta since 08-06 — numbers only

| metric | 08-06 (asof 08-05) | 08-07 (asof 08-06) | Δ |
|---|---|---|---|
| wflow | +0.317 (rank 1) | **+0.241 (rank 2)** | −0.076 |
| eqflow | +0.190 | **+0.125** | −0.065 |
| breadth | 0.149 (7🟢/47) | **0.130 (6🟢/47, 8🔴)** | −0.019 |
| WFC | +0.457 🟢 (`new_green`), velocity 1.89 | **+0.272 🟡, RS20 −1.5, Δ −0.185** | exited green |
| GS | +0.095 🟡, RS20 −0.3 | **−0.167 🔴분산, RS20 −4.5, Δ −0.262** | 5th run unresolved |
| XLF / KRE | — | **XLF −0.33% (exc5 −2.20 / exc20 +1.85) · KRE −1.10% (exc5 −2.85)** | new |
| 2s10s (`[FRED]`) | +0.43 (3rd flattening print) | **+0.45 (4th print, WIDENED — trend refuted)** | +0.02 |
| Primaries | JPM/BAC FY2025 10-K only, "stale" | **JPM 10-Q 08-06 · GS 10-Q 08-03 · BAC 10-Q 07-31 — all period 2026-06-30** | new this run |

---

## 2 · Is the OW− survivable — the arithmetic

**Every axis fell (§1) and none hit zero.** wflow stayed rank 2 of 11 and positive; breadth fell 1.9pp but
6 greens remain; eqflow fell 6.5pp but stayed positive. The question is whether this is noise inside a
range or the start of a slide — the mandate's own scope test (C4) is the instrument for that.

**Reproducing the never-negative-eqflow claim** `[own calc over llm_outputs/sector_flow/history.json,
current 47-name Financials membership projected across 16 sessions 2026-07-14→08-06]`: I reproduce **16
of 16 sessions positive, mean +0.2588, minimum +0.0547 on 08-04** — matching `BLINDSPOT_PREMORTEM.md` §3d
exactly. **One number does not reproduce**: PREMORTEM calls today's +0.1251 the *"2nd-LOWEST of 16."* My
ranking puts **08-04 (0.0547) lowest, 08-03 (0.1014) 2nd, 07-15 (0.1169) 3rd, today (0.1251) 4th-lowest** —
one rank off. ⚠ **Correction with receipts**: the ordinal is off by one; the substance is not — today is
still bottom-quartile in a series that has never gone negative, and 4th-lowest supports the same reading:
**"near the floor of a never-negative range" holds; "the floor" (a UW-triggering zero-cross) does not.**

**What the range actually argues for.** A series that is 16/16 positive with mean +0.2588 sitting at
+0.1251 is at the **19th percentile of its observed range (0.0547–0.4070)** — weak, not broken. A
one-notch demotion (OW → OW−) matches a 19th-percentile print; a UW would require the series to do
something it has not done once in 16 sessions.

**Combined with the revision-book leg (§4, §6d of 08-06's file, reconfirmed below): GS +19.2%/90d 19↑/0↓,
JPM +8.2%/90d 8↑/0↓, BAC +4.6%/90d 16↑/0↓** — three of the sector's largest names carry clean, un-contested
up-revision books that **no flow tag currently owns** and that did not move this run.

**Verdict: OW− survives, on the same two legs the 08-06 file identified (mega-cap wflow rank, un-owned
revision books) — but breadth keeps shrinking, and three of six remaining greens (JPM `vol_surge` 0.68,
BAC 0.74, BRK-B 0.86) have no volume confirmation.** A further eqflow leg-down, or the flow axis
flickering off again as it did 07-31→08-03 (08-06 file §1a), would put OW− itself in question. **A
survivable notch with no slack left in it.**

---

## 3 · WFC resolved on both axes, and what it does to S65's median

**Flow axis, arithmetic reproduced** `[module_flow gate: ≥3 of {OBV 매집, RS20>0, vol_surge≥1.2,
velocity≥1.2}]`: WFC clears **OBV 매집 (✓) and velocity 1.76 (✓) but fails RS20 −1.5 vs SPY (✗) and
`vol_surge` 0.82 (✗)** — 2 of 4, one short of the gate. **Not an instrument flicker like the 08-06 file
found for JPM/BAC/MA** (§1a there) — WFC's velocity axis stayed populated both runs (1.89 → 1.76); what
changed is RS20 turning negative on real price action.

**Revision axis** `[module_fundamentals_us WFC, 2026-08-07]`: **next-quarter breadth 7↑/10↓ (30d), 1↑/3↓
(7d), next-quarter estimate −0.7%/90d — the only negative book of the four S65 legs.** For contrast, same
pull: **JPM CY +8.2%/90d (30d 8↑/0↓) · BAC CY +4.6%/90d (30d 16↑/0↓) · BRK-B CY +1.6%/90d (30d 1↑/0↓, n≈4,
S1).** ⇒ **both axes agree independently** — flow sees a 20-day price fact, revisions a forward-estimate
fact — for the first time in this desk's WFC coverage.

**S65 median, recomputed** `[own calc, settled 08-06 RS20 vs SPY]`: {JPM +4.0, BAC +4.1, WFC −1.5, BRK-B
+3.6} → **median +3.8** (reproduces the registered +3.805 to rounding). **Ex-WFC: median(JPM, BAC, BRK-B)
= +4.0** — a **+0.2pp move**, not the +1.8pp jump the earlier BRK-B-drag question produced on 08-05 data
(08-06 file §3). Registration is **A ≤ +0.34 · B ≥ +6.81 · C between**; both the actual (+3.805) and the
ex-WFC counterfactual (+4.0) sit deep inside branch C. **WFC being confirmed negative is a finding about
WFC, not a lever on S65's settle.**

---

## 4 · GS — resolved or declared unresolvable, 5th run: the primary evidence

`[module_fundamentals_us GS + GS 10-Q, filed 2026-08-03, period 2026-06-30 — fetched and read directly this
run, closing the staleness gap the desk has carried since 08-04]`

- **Fundamentals**: CY EPS **+19.2%/90d, 19↑/0↓ at both 7d and 30d**; CQ **15↑/1↓ (30d)**; **Q2-2026 total
  net revenues $20,338mm vs $14,583mm Q2-2025 = +39.5% YoY** (from the fresh 10-Q, not the FY2025 filing).
  **Forward P/E 14.03** — below JPM's 14.20, near BAC's 11.90 — **not a rich multiple correcting** (B2:
  no de-rate story on valuation).
- **Flow/price**: 🔴분산 (**D6 — OBV grade C, not carrying this claim alone**), flow **−0.167**, **RS20
  −4.5 vs SPY** (RS60 **+5.3 vs SPY** — a 20-day fact sitting inside a 60-day outperformance), Δ **−0.262**,
  `vol_surge` 0.84.
- **Positioning, filled this run** (mandate flagged "GS not pulled"): `[scripts/us_flow.py, FINRA
  Reg SHO 08-06]` **GS short-vol z +0.91, 5v5 +3.0▲ — inside ±1.5, a mild build, not a divergence.**
- **News**: `[module_news_data fts search "Goldman Sachs", foreign, 3d]` **416 hits, top-ranked items are
  ETF product comparisons and byline mentions — no name-specific adverse event found (A6 satisfied by
  absence).**

**Verdict.** **Not a data artifact** — flow_score and RS20 both reproduce cleanly and GS's velocity axis
(1.69) has stayed populated across runs, unlike the JPM/BAC/MA flicker the 08-06 file found. **Not a
de-rate** — the multiple is the cheapest of the sector's three biggest revision books, not the richest.
**It is a genuine flow/fundamental split**: estimates and 20-day price/volume are measuring different
windows and disagreeing on this one name for a **5th consecutive run**, with no negative primary evidence
on either side to arbitrate it. **Falsifier, stated positively**: RS20 turning positive on a settled bar,
or CY breadth net-down for two consecutive weeks — either ends the split; neither has happened yet.

---

## 5 · The rate mechanism, from PRIMARY filings — where NII actually comes from now

`[JPM 10-Q filed 2026-08-06, BAC 10-Q filed 2026-07-31, GS 10-Q filed 2026-08-03 — period 2026-06-30,
fetched and read directly this run]`. **This retires the 08-06 file's "Q2-2026 segment attribution
`unknown` (C3)" note for these three names — all now have a Q2 primary under a week old.**

| bank | Q2-2026 NII | the bank's own words |
|---|---|---|
| **JPM** | **$25.5bn, +10%** | *"driven by higher Markets net interest income, higher deposit balances, higher revolving balances in Card Services, and higher wholesale loan balances, **partially offset by the impact of lower rates**."* Avg interest-earning assets **$4.3T, +$442bn**; yield **4.75%, −29bp.** |
| **BAC** | **+$1.3bn to $16.0bn** | *"primarily driven by higher net interest income related to **Global Markets activity**, deposit and loan growth, and fixed-asset repricing, **partially offset by the impact of lower interest rates**."* NIY (FTE) 2.08%, +14bp. |
| **GS** | **+27% to $3.95bn** | *"reflecting an **increase in interest income**, partially offset by an **increase in interest expense**."* Income: higher avg balances in other interest-earning assets/investments and trading assets. Expense: higher avg balances in deposits, collateralized financings. Segment note (FICC/Equities only): *"an increase in interest-earning assets **and a decrease in funding costs**."* |

★★★ **All three now attribute Q2-2026 NII growth primarily to balance-sheet VOLUME, with rates named as a
negative-to-mixed factor, not a positive one.** This updates the FY2025 finding (08-06 file §6a): **GS's
FY2025 mechanism — "NII rose 68% because interest expense fell on lower rates" — does not repeat in the
fresher quarter.** In Q2-2026, GS's interest EXPENSE **rose** (higher balances on deposits/collateralized
financings outweighing the rate saving); "decrease in funding costs" language survives only at the
FICC/Equities segment level, not the consolidated line. **JPM and BAC are consistent across both filing
vintages: lower rates are named as a headwind in both FY2025 and Q2-2026.** ⇒ **the sector's rate sign has
converged, not diverged: the dominant, shared NII driver across all three banks is now balance-sheet
volume, and where rate direction is named at all, it points negative for two of three and only partially
positive for the third.**

**What a BULL steepener does that a bear steepener does not.** The volume leg — deposit and loan growth,
wholesale balances, Card Services revolving balances — is **growth-dependent**, not rate-dependent. A
**bear steepener** (long rates rising on strong-growth/inflation expectations, what this Fed's hike
dissents on 07-29 point toward) is historically consistent with continued loan demand — it does not
threaten the volume leg these filings just named as primary. A **bull steepener** (front-end rally on a
weak print, MACRO §0-a/§0-b's read of July NFP −23,000) carries a different signature: it typically
**arrives with the growth deceleration that threatens loan/deposit volume growth itself** — the leg JPM,
BAC and GS all just cited as their actual driver — while delivering the "lower rates" outcome JPM/BAC
already call a **headwind**. ⇒ **a bull steepener offers no clean win on either half of these banks' own
mechanism — it risks the rate half (already negative) and the volume half (currently positive) at once,
which a bear steepener would not.** This is why **S51's own registered caveat (MACRO §0-b) says branch A
firing tonight "may NOT be read as confirming"** the tilt — the primaries now show why, at the mechanism
level, not just the curve-shape level.

---

## 6 · W5 dispersion by sub-node

`[own calc, mean flow_score / mean RS20 vs SPY, settled 08-06, grouped by GICS industry within Financials]`

| sub-node | n | mean flow_score | mean RS20 vs SPY |
|---|---|---|---|
| Insurers (MET/PRU/TRV/ALL/AIG/AFL/CB/HIG/PGR) | 9 | **+0.356** | **+2.77** |
| Asset managers/alts (BLK/BX/KKR/APO/AMP) | 5 | **+0.472** | **+6.98** |
| Payments/fintech (MA/V/PYPL/XYZ/COIN/SCHW) | 6 | +0.217 | +5.73 |
| Money-centres (JPM/BAC/WFC/C) | 4 | +0.178 | +0.05 |
| Other (BRK-B/HOOD/GS/COF) | 4 | −0.025 | −4.15 |
| Regionals (USB/PNC/TFC/FITB/HBAN/STT/BNY) | 7 | +0.030 | −0.59 |
| Exchanges/data (ICE/NDAQ/CME/MCO/SPGI/MSCI) | 6 | −0.097 | +0.12 |
| Brokers/insur-brokers (MS/IBKR/AON/AJG/MRSH) | 5 | **−0.211** | **−3.22** |

**Spread: asset-mgrs/alts +0.472 to brokers/insur-brokers −0.211 = 0.683 — 5.5× the sector's own eqflow
move of +0.125.** Confirms the 08-06 file's §5 W5/B5 finding: **"Financials" is not a usable unit.** (**C5**:
BRK-B sits in "Other" rather than insurers/asset-managers because its flow tag and holdings mix fit
neither — the grouping, not the data, drives that row's negative mean.) XLF **−0.33% (exc5 −2.20/exc20
+1.85)** vs KRE **−1.10% (exc5 −2.85)**: regionals underperformed the sector ETF by 0.77pp on the day, an
ETF-level confirmation of the sub-node table.

---

## 7 · Track KPIs · anti-signals · dated observables

| KPI | State (settled 08-06 unless noted) | Anti-signal, dated | Date |
|---|---|---|---|
| **Eqflow floor** | +0.1251, **4th-lowest of 16** (corrected from PREMORTEM's "2nd-lowest," §2) | ⛔ first **negative** eqflow print in the 17-session record breaks the never-negative scope, reopens UW | next run |
| **Breadth flicker** | 6/47 today; axis went 51/300→0/300 across two 08-06-file runs with no market event | ⛔ velocity coverage returning to 0/300 mechanically drags breadth to 0.04–0.09 | next run |
| **WFC** | 🟡, RS20 −1.5, NQ est −0.7%/90d, 7↑/10↓(30d) | NQ breadth net-positive over next 30d reopens the green | ~09-06 |
| **GS split** | 🔴분산 RS20 −4.5 vs CY +19.2%/90d 19↑/0↓ — 5th run unresolved | RS20 positive settled, **or** CY breadth net-down 2 weeks | rolling |
| **S65** | median RS20 {JPM,BAC,WFC,BRK-B} = **+3.805 = branch C**; ex-WFC ≈ **+4.0**, still C | A ≤ +0.34 or B ≥ +6.81 | 08-11 |
| **S66** (new) | bull-steepener-with-credit-fear leg — `ΔDGS2` from 4.18, `ΔHY OAS` from 2.75 | branch A: ΔDGS2 ≤ −0.15 AND ΔHY ≥ +0.15 | post-08-07 |
| **HY OAS** | 2.75, 15bp below the 2.90 credit-fear line, **not printed since NFP** — `unknown` (C3) | first post-NFP print ≥ 2.90 | next FRED |
| **2s10s** | +0.45, widened on its 4th print — flattening refuted | ≤ +0.20 kills the sector's only rate leg (0/273 historically) | rolling |
| **GS short-vol** | z +0.91, 5v5 +3.0▲, inside ±1.5 | z crossing ±1.5 | rolling |
| **Fresh 10-Qs** | JPM/BAC/GS Q2-2026 on file, all convergent on volume-driven NII | Q3 10-Q tests volume-leg vs rate-headwind dominance under an actual bull-steepener print | 10-13/14 |

---

## 8 · What this hands to BET

**Greens (asof `SECTOR_FLOW_US.json`, 2026-08-06 settled; the file's `names` array sorts by `flow_score`
DESC, not market cap):** **MET** (+0.769, RS20 +7.4/RS60 +24.2 vs SPY, `vol_surge` 1.23, volume-confirmed)
· **MA** (+0.702, +7.8/+11.7, velocity-only) · **PRU** (+0.697, +3.4/+16.2, `vol_surge` 1.40,
volume-confirmed) · **BRK-B** (+0.554, +3.6/+5.4, velocity-only, **reports Q2 08-09, inside S65's window**)
· **BAC** (+0.520, +4.1/+20.7, velocity-only) · **JPM** (+0.492, +4.0/+14.8, velocity-only).

**Demoted out of the green set:** **WFC** (🟡, RS20 −1.5 vs SPY, NQ estimate −0.7%/90d, the only negative
revision book among S65's four legs — §3).

**Unresolved, un-owned, flag for a 6th run if it persists:** **GS** (🔴분산, RS20 −4.5 vs SPY, best revision
book in the sector at CY +19.2%/90d 19↑/0↓ — §4).

**Sector state to carry forward:** wflow +0.241 (rank 2 of 11), eqflow +0.125 (4th-lowest of 16 sessions,
never negative), breadth 0.130 (6🟢/8🔴 of 47), XLF −0.33% (exc5 −2.20/exc20 +1.85), KRE −1.10% (exc5
−2.85). **The rate leg cannot resolve either direction cleanly**: 2s10s +0.45 refutes the flattening trend
this run, HY OAS's post-NFP print is missing (C3), and the freshest primaries (§5) show a bull steepener
would hit the sector's actual (volume-driven) NII engine, not protect it. **No sizing implied above — that
is BET's decision, not this file's.**
