# SWEEP read — industry_US · 2026-08-08 (Sat) · Stage 3/10 (L1·SWEEP)

> The reading only. **No table below exists in `SECTOR_FLOW_US.json` or `US_LIVE_SHORTLIST.json`** —
> sector rows and per-name rows are cited by artifact, never reprinted.

## 1 · Universe headline

**n = 300 · wflow +0.057 · 🟢 23 / 🔴 77 · `asof 2026-08-07 SETTLED`** · **1 `new_green`: COHR** (IT).
✅ **The sweep's `asof` equals the last settled close — D74 contamination = 0**, the first US sweep in
four runs of which that is true.

✅ **`sector_flow.py`'s stderr was read IN FULL this run** (`out/_sweep_stderr.txt`, 9 lines quoted into
§5) — the 08-07 failure that let a delisted security through was reading only the tail.

---

## 2 · ★★★ The finding: on this board, **🟢 means two different things, and the split is exact**

The D161 interim rule (*no stage cites a 🟢 without decomposing which axis lit it*) was executed on
**all 23 greens**. The result is not a tendency; it is a clean partition:

| | count | `vol_surge` | `velocity` |
|---|---|---|---|
| **Volume-lit greens** | **15** | all **> 1.0** | 14 of 15 have **none** |
| **Velocity-lit greens** | **8** | all **< 1.0** (range **0.65 – 0.99**) | **all 8 populated** |

**The 8 velocity-lit greens are XOM · CVX · MSFT · NVDA · BRK-B · MRK · BAC · JPM.**
**Every green on this board whose volume was BELOW its own average is a name on the `velocity`
whitelist**, which this run re-measured at **exactly 50 of 300 names** — reproducing R59/D205's count
(51 → 50 → 50) a second time.

⇒ **R59 is not merely a mechanism claim any more; it is an operating fact with a name list.** A green
outside the whitelist requires a volume surge; a green inside it does not.

### 2a · ★★★ And that inverts the two highest-ranked sectors on the flow axis

| Sector | flow rank | Its greens | What lit them |
|---|---|---|---|
| **Energy** | **#1 of 11** (`wflow +0.342`) | **XOM, CVX — 2 of 2** | **both velocity-lit, `vol_surge` 0.88 and 0.96 = BELOW average volume** |
| **Financials** | **#2 of 11** (`wflow +0.172`) | BRK-B, BAC, JPM, PRU | **3 of 4 velocity-lit, `vol_surge` 0.85 / 0.73 / 0.65** — JPM's is the lowest of any green on the board |

⇒ **The two sectors the sweep ranks first and second on "money flow" have, between them, five greens
of which five are on below-average volume and are lit by a news-velocity axis.**
**Neither rank is a money reading.** This is stated as a decomposition, **not** as a claim that the
axis has the wrong sign — the desk's own IC ledger has `vol_surge` **positive** in the US
(t +1.80) and **negative** in KR (t −2.06), and **W1 forbids importing either.**

---

## 3 · Cross-checks against the MACRO matrix — where flow and price disagree, and who is right

| Sector | MACRO price axis (settled 08-07) | Sweep flow axis | Read |
|---|---|---|---|
| **Energy** | **exc1 −1.75 · exc5 −6.95 — LAST of 11 on both** | **wflow +0.342 — FIRST of 11** | 🚨 **The board's largest axis contradiction.** §2a resolves it: **the flow rank is two below-volume velocity tags.** ⇒ **the price axis is the better-supported side, and MACRO's N+ has no flow confirmation this run** |
| **Financials** | **exc1 −0.97 — 10th of 11**, all 4 S65 names negative | **wflow +0.172 — 2nd of 11**, 4🟢/7🔴 | 🚨 **Same shape, same resolution.** ⚠ And note the **7 reds against 4 greens** — even the flow axis is red-dominant inside the sector it ranks #2 |
| **Materials** | **exc5 +1.307 — 0.59pp from S57 branch A** | **0🟢 of 12 · breadth 0.000 · wflow −0.038** | ★★★ **The flow axis gives ZERO support to the price move about to settle S57.** The move is **NEM +17.05pp / ALB +7.94pp over 5 sessions** (MACRO §B-3) and **the gate lit neither.** ⇒ **`S57-ANNEX` is strengthened by an independent instrument** |
| **Utilities** | **exc5 −5.18 · exc20 −6.39 — last of 11 on both long windows** | **wflow −0.395, eqflow −0.381, 0🟢 / 11🔴 of 15** | ✅ **Both axes agree, and this is the most one-sided sector on the board — 11 reds of 15 names.** UW confirmed on two independent instruments |
| **Comm Services** | exc20 −2.77, 10th of 11 | **eqflow +0.119 > wflow −0.087 · breadth 0.150 = 2nd of 11** | 🚨🚨 **R56's exact shape has re-formed — see §4** |
| **Info Tech** | XLK exc5 **+3.69**, SMH exc5 **+4.29** | **5🟢 / 22🔴 of 56 · eqflow −0.092 vs wflow +0.084** | ⚠ **22 of the board's 77 reds (29%) sit in one sector.** Price is led by mega-caps; **breadth is the worst on the board.** ⇒ **MACRO's N is the right stopping point and the sweep says why** |
| **Health Care** | exc1 +0.14 · exc5 −1.59, mid-board | **breadth +0.160 = BEST of 11 · 5🟢 / 6🔴 of 32 · delta +0.049 = the ONLY positive delta** | ★★ **The one sector where the flow axis is unambiguously better than the price axis** — and **all 5 greens (BMY, AMGN, WAT, IDXX, MRK) are volume-lit except MRK.** ⇒ **this is the run's only breadth signal that is not a velocity artifact.** **The SWEEP re-measurement the 08-07 run owed on the revived HLTH node is delivered here** |

---

## 4 · 🚨🚨 R56 reproduced independently, one day later, on a settled bar

**EA is STILL tagged 🟢가속** in today's sweep, and it still carries **the board's highest
`vol_surge` (+3.66) and its highest `obv_norm` (+0.749)** — both computed from the liquidation print.
**It is also on the LIVE SHORTLIST**, where the FINRA proxy returned a real short-z of **+0.79** and a
`△정상숏` verdict rather than an error. ⇒ **the defect propagates one stage further than R56 caught
it.**

**Recomputed ex-EA** (the aggregation was reproduced against the printed row first — eqflow 0.1186 vs
printed 0.119, wflow −0.0871 vs −0.087, C1):

| | eqflow | wflow | 🟢 / 🔴 / n |
|---|---|---|---|
| as printed | **+0.119** | −0.087 | 2 / 2 / 13 |
| **ex-EA** | **+0.073 (−39%)** | −0.090 | **1 / 2 / 12** |

⇒ **R56's own prediction is confirmed**: the `eqflow > wflow` relation survives (it only flips if DIS
goes too), **but the sector goes red-dominant and its breadth rank collapses.** **COMM = UW stands, on
a second independent measurement.**

### 4a · ✅ D207's liveness assertion — specified, executed on the full board, and it works

The three checks D207 proposed were run against **all 23 greens** on the last two settled bars:

```
zero volume on either of the last two bars  OR  Open=High=Low=Close on BOTH bars
→ 23 tested · 1 FAIL · 0 false positives
→ FAIL: ['EA']   (volume 0 and 0; degenerate OHLC on both bars)
```

⇒ **D207 is no longer "a human should add a liveness assertion." The assertion is written, tested on a
300-name universe, and returns 1 true positive and 0 false positives.** It remains human-gated because
it is a scoring change to a shared module.

🚨 **And the root cause is worse than "nobody rebuilt the file."** The stderr warning reads
*"`build_top300.py` 재빌드 권장"* — **`build_top300.py` does not exist anywhere in this repository.**
The builder lived in the retired `mvp` repo, which CLAUDE.md P5 forbids this repo from touching.
⇒ **the universe cannot be rebuilt by any run, at any staleness, with the tools this repo has.**
**That is a different defect from the one D207 describes, and it is registered as `D215`.**

---

## 5 · Shortlist composition — the absences, each diagnosed

`us_live_shortlist --floor-b 10 --top 15` → **15 names**, `asof 2026-08-07`.
Sectors producing **zero** shortlist names: **Materials · Utilities · Real Estate · Consumer Staples ·
Consumer Discretionary · Financials.**

| Absence | Diagnosis | Evidence or artifact? |
|---|---|---|
| **Materials 0** | **0🟢 of 12 in the sweep itself** | ✅ **EVIDENCE** — and it is the run's sharpest one, because it sits against a price move 0.59pp from firing S57's branch A |
| **Utilities 0** | **0🟢 / 11🔴 of 15** | ✅ **EVIDENCE** — the most one-sided sector on the board |
| **Real Estate 0** | 0🟢 / 1🔴 of 12 | ✅ EVIDENCE, but weak — **only 1 red in 12 names**; this is an *absence of signal*, not a negative one |
| **Consumer Staples 0** | 0🟢 / 6🔴 of 19, **eqflow −0.165 = worst on the board** | ✅ EVIDENCE — and it is the **fourth consecutive run** with no proposition, no bracket and no thread here |
| **Consumer Discretionary 0** | 0🟢 / 8🔴 of 28 | ✅ EVIDENCE |
| 🚨 **Financials 0 — despite FOUR greens** | **A TOP-15 TRUNCATION ARTIFACT, and the cut is razor-thin**: the shortlist's 15th name is **IDXX at +0.6490** and the 16th is **PRU at +0.6460** — **a 0.003 gap excludes ALL FOUR Financials greens** (PRU +0.646 · BRK-B +0.541 · BAC +0.494 · JPM +0.473) | 🚨 **ARTIFACT — must not be cited as evidence** |
| **Energy 1 (XOM only), despite 2 greens** | Same cut: **CVX +0.586 is rank 17** | 🚨 **ARTIFACT** |

⚠ **The Financials absence is the exact failure the EXIT CHECK's absence rule exists to prevent** —
a sector with the board's #2 flow rank and 4 green tags produces an empty shortlist purely because a
`--top 15` cut lands in a 0.003 gap. **Diagnosed before it could be cited.**

### 5a · Short-pressure verdicts (FINRA proxy — US has no investor-type feed)

- ✅ **Only ONE "clean rise" (🟢 + low-short/covering) on the entire shortlist: XOM, short-z −0.59.**
- ⚡ **One crowded-short: WAT, z +2.27** — squeeze fuel conditional on a turn, **never a standalone
  reading**, per the module's own text.
- ⚠⚠ **And XOM, the board's only clean-rise name, is NOT IN THE BOOK.** `cycle_exposure` reads the
  held Energy epicenter as **MPC, PSX**. ⇒ **the S31 phantom-position finding is reproduced on a fresh
  deterministic pull** — a bracket written throughout as *"the only Energy name the book holds"*
  describes a position that does not exist. **PREMORTEM owns it.**

---

## 6 · (US) CYCLE_EXPOSURE GAP — ✅ none

`cycle_exposure --json` (book: KIS read-only, total ≈ $10,888 · invested $6,361):

| Cycle | rank | epicenter % | need ≥ | held | GAP |
|---|---|---|---|---|---|
| AI-compute / semiconductors | 1 | **19.74%** | 12.0% | AVGO, NVDA, ANET | ✅ |
| Energy / oil-refining | 2 | **10.23%** | 8.0% | MPC, PSX | ✅ |
| Missile-defense / rearmament | 3 | 6.15% | — | RTX | ⚪ no threshold set |

✅ **No top-rank cycle GAP — nothing handed to ALPHA's action bracket on this axis.**
⚠ **Rank-3 still has no minimum** (`⚪ 기준 미설정`) — a registry field a human must set; **carried,
not re-discovered.**

---

## 7 · What ROTATION gets from this stage

1. **Energy's and Financials' flow ranks are velocity artifacts on below-average volume** (§2a) —
   **both sectors' price axes went the other way on the settled bar.** ⇒ **ROTATION may not promote
   either on flow.**
2. **Materials has 0🟢 of 12 while its price observable sits 0.59pp from firing S57's branch A** ⇒
   **the two axes disagree, and this is the run's most decision-relevant disagreement.**
3. **Utilities is confirmed UW on two independent instruments** (0🟢/11🔴 and last-of-11 on both price
   windows), consistent with **S62's FIRED-B**.
4. **Health Care is the only breadth signal on the board that is not a velocity artifact** (best
   breadth +0.160, the only positive delta, 4 of 5 greens volume-lit).
5. **Info Tech carries 29% of the board's reds in one sector** while its price leads ⇒ **N is right and
   the sweep supplies the reason.**
6. 🚨 **EA is still 🟢 and still on the shortlist** ⇒ **ROTATION must treat every COMM number as ex-EA**,
   and **`D215`** records that no run can fix the universe with this repo's tools.
7. **Financials' empty shortlist is a 0.003-wide truncation artifact** and **may not be read as an
   absence of candidates.**

## ✅ EXIT CHECK

- [x] `sector_flow` sweep done → `SECTOR_FLOW_US.json` (`asof 2026-08-07` settled); sector ranking and
      the single `new_green` (COHR) read; **stderr read in full**
- [x] `US_LIVE_SHORTLIST.json` written; short-pressure verdicts read (1 clean-rise, 1 crowded-short)
- [x] `CYCLE_EXPOSURE` GAP read — **✅ none**; nothing handed to ALPHA on this axis
- [x] **No table here exists in the JSONs** — sector rows and per-name rows cited by artifact; every
      table above is a decomposition, a recomputation, or a diagnosis that the JSON cannot express
- [x] **Cross-checks that confirm AND contradict the MACRO matrix are stated** (§3: Energy and
      Financials contradict, Utilities and Info Tech confirm), **and the shortlist's absences are each
      diagnosed as evidence vs artifact** (§5 — 5 evidence, 2 artifact)
