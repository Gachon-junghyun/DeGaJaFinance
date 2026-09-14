# SECTOR_DEEP_FIN — Financials — industry_US — 2026-07-30 (Thu) · CONTINUOUS-TRACK → **DELTA-LED**

> Continuous slot (7th consecutive run). Leads with the delta; unchanged structure by reference to
> `llm_outputs/2026-07-29/industry_US/SECTOR_DEEP_FIN.md`. Benchmark **SPY** inline (C1).
> All 47 rows **re-derived from `SECTOR_FLOW_US.json` asof 2026-07-29, not inherited** (R20's lesson).

## 0 · ⛔ THE DELTA — the "only breadth-led sector on the board" claim REVERSES SIGN when BRK-B is removed

The label the FIN OW has rested on since 2026-07-23 is **eqflow > wflow ⇒ breadth-led**. Re-derived
today from all 47 rows:

| | wflow | eqflow | gap (eq − w) |
|---|---|---|---|
| **All 47** | **+0.386** | **+0.407** | **+0.021 → "breadth-led"** |
| **Ex-BRK-B (46)** | **+0.4307** | **+0.4134** | **−0.017 → mega-cap-led** |

**BRK-B is $1,055.7bn = 13.94% of a $7,574bn sector at a flow score of +0.11** — the lowest score of
any name above $250bn. **Removing that one row flips the sign of the sector's defining statistic.**

⇒ ★★ **M173 → M239 → this run is not a decay, it is a threshold crossing**: the ex-BRK gap ran
**+0.028 (07-27) → +0.043 (07-28) → −0.017 (07-30)**. **The breadth label no longer survives its own
robustness check.** ⚠ **Scope discipline (C4)**: this does **not** say Financials is weak — it is the
board's **2nd-best 20-day sector (+8.04pp excess vs SPY)**. It says **the stated REASON for the OW is
an artifact of one holding company's low score**, which is the R15/M52 shape: *direction stands,
driver retracted.*

## 1 · Sub-node decomposition — the grouping is stated, and it is arbitrary (C5)

Four buckets by revenue engine (n=47, equal-weight mean flow score; the sector's eqflow is +0.407):

| Node | n | eq-mean flow | vs sector | 🟢 | Read |
|---|---|---|---|---|---|
| **Insurance** (P&C · L&H · multi-line · brokers) | **12** | **+0.603** | **1.48×** | **3** (TRV · MRSH · MET) | **The engine.** 25.5% of names, the top eq-mean of any node |
| **Payments** (V · MA · PYPL · XYZ · AXP · COF) | 6 | **+0.535** | 1.31× | 2 (V · MA) | Second engine, and **V/MA are a different residual unit from JPM/TRV/CB** (MA–JPM +0.238) |
| **Capital markets** (IB&B · asset mgmt · exchanges) | 19 | **+0.311** | 0.76× | 1 (BX) | **Nets to below the sector.** BX +0.83 carries it; **GS −0.02, HOOD −0.62, IBKR −0.28** drag |
| **Banks** (diversified + regional) | 9 | **+0.298** eq / **+0.424 cap-weighted** | 0.73× eq | 2 (JPM · BAC) | ⚠ **The ONE node where wflow > eqflow** ⇒ **inside banks it is JPM + BAC, not the bucket** |

★ **M40's "payments + insurance is the concentration wearing a breadth label" replicates a FOURTH
time and is now sharper**: **insurance + payments = 18 of 47 names (38%) and 5 of the 8 greens (63%)**,
at **1.48× and 1.31×** the sector mean, while **capital markets and banks both sit BELOW it.**

## 2 · The three OW legs, scored

| Leg | Status |
|---|---|
| **① The steepener** | **DEAD since R11 (2026-07-23).** Not revived: derived 2s10s went **+0.34 → +0.36 → +0.34 → +0.35**, i.e. **it STEEPENED 1bp on the last settled print** — ⚠ which is **against S23's flattener** but is **not** the bull steepener either, because **the whole post-FOMC move is unpublished (MACRO §A-1)** |
| **② Breadth** | **⛔ REVERSED THIS RUN (§0).** The statistic that carried it does not survive removing one name |
| **③ Credit quality / NII migration** | **Untested and now dated.** **WFC held FY26 NII flat and missed; JPM raised on markets NII (M138)** ⇒ **S23's flattener hits the half WFC guided flat.** JPM's own CEO issued a **"stark warning"** in a BUILDING 3→4→4 thread this window, and **JPM fell −3.53% on 07-29** |

⇒ **Two of three stated legs are now dead or reversed, and the surviving one is a migration argument
nobody has measured.** ⚠ **This DEEP does not move the tilt** — that is ROTATION's call and ROTATION
already made it (OW− held). **It records that the tilt is standing on its third leg for the first
time.**

## 3 · What the money actually did — and the S14 read

- **8 greens of 47** (BX · TRV · MRSH · MET · V · BAC · JPM · MA), **1 red (C, −0.68)**, breadth 0.170.
- ⚠ **5 of the 8 cleared on the VELOCITY path with `vol_surge` below the 1.20 gate** (V 0.88 · BAC
  0.87 · JPM 0.85 · MA 0.75 · plus MET/MRSH on volume) ⇒ **the green count is partly an instrument
  state (SWEEP §2c, D75).** Had `velocity` been null as it was on 07-28, **Financials would show 4
  greens, not 8.**
- **The deepest accumulation base on the board**: **32 of 47 names pass `OBV-accumulation ∧ RS20>0`
  and 24 are blocked by `vol_surge` alone** — more than any other sector.
- **S14 (MA Q2, 07-30)**: **profit and revenue beat, "robust transaction volumes driven by steady
  consumer spending", GDV and purchase transactions up, shares +3% pre-market** [cna/Reuters body;
  8-K filed 07-30] ⇒ **the volume half of branch A reads HOLD.** ⚠⚠ **+3% is INSIDE S14-num's
  pre-declared ±3.9% no-information band and may NOT be read as confirming the OW.**
  **S14's RS20 leg settles 08-06 with PYPL's contamination included, and S14 is NOT re-frozen.**
- ⚠ **PYPL's contamination is now visible in the numbers**: **RS20 +37.4 — the highest in the sector —
  against days-21-60 of −22.9.** **That is a merger-arb spread's signature**, not payments breadth
  (S14-ANNEX), and it is exactly why the {MA, V}-only reading was pre-registered.

## 4 · Momentum geometry — where the 60-day excess was earned (days 21–60 = RS60 − RS20)

| Deepest bases (money has a foundation) | Most concentrated (last 20 days are the whole move) |
|---|---|
| **HOOD +28.8** (but flow −0.62 🟡, RS20 −8.1) · **AJG +8.5** · **STT +8.5** · **FITB +8.3** · **PNC +8.2** · **ALL +7.9** · **PRU +7.2** | **CME −32.0** · **COIN −29.3** · **ICE −29.1** · **PYPL −22.9** · **NDAQ −20.1** · **KKR −16.0** · **BLK −14.2** |

★ **The exchanges node is the sector's concentration problem, and it is unchanged in kind but larger
in degree**: **four of the seven exchange names have a days-21-60 worse than −20**, i.e. **their entire
60-day relative performance is a last-20 event.** ⚠ **M135 stands: the registered RS60 test is BROKEN**
(on frozen prices it can only report CONFIRM), and its **replacement observable** — equal-weight excess
of the seven vs SPY — is the one that must be read at **08-07**, with **4 of 7 not printing inside the
window.**

★ **And the sector's two 🟢 with real bases are insurance**: **TRV +6.2** and **MET +2.7**, against
**TRV's M150 exhaustion warning improving from 98.6% to 76% last-20 share.** **TRV is re-tagged
EXTENDED-BUT-LIVE with a thin base** (PREMORTEM Lens 3), not exhausted.

## 5 · Value chain and the binding constraint

`policy rate → curve shape → deposit cost ↔ asset yield → NII → credit cost → capital return`
plus a parallel fee chain: `market volume → exchange fees ↔ payment volume → interchange`

- **Binding constraint = the curve, and it is currently UNOBSERVABLE.** FRED's daily curve stops at
  **07-28**; the FOMC was **07-29**. ⇒ **the sector's primary driver cannot be read at this run clock**,
  and this file says so rather than substituting a proxy (**D5**).
- **Second constraint = consumer transaction volume**, and **MA's print says it is holding** — the one
  leg of the chain that produced fresh primary evidence today.
- ⚠ **W4 check**: the customers of the *fee* chain are consumers and issuers; MA's disclosure covers
  them. The customers of the *NII* chain are depositors and borrowers; **WFC's flat NII guide and
  JPM's markets-driven raise are the disclosed spend, and they point opposite ways (M138).**

## 6 · Dated catalysts, KPI, anti-signal

| Date | Event | Settles |
|---|---|---|
| **2026-08-05** | **S23 / S19 windows close** | **T10Y2Y ≤ +0.20 with DGS2 in 4.15–4.45** = the bear-flattener that kills NII without tripping S19 or S9. **Now 15bp away and it moved 1bp AWAY** |
| **2026-08-06** | **S14 / S14-ANNEX / S14-num** | {MA, V, PYPL} RS20 vs SPY, and the pre-registered {MA, V}-only reading alongside |
| **2026-08-07** | The exchanges' replacement observable | Equal-weight excess of the 7 vs SPY. ⚠ 4 of 7 do not print inside the window |
| **2026-08-08** | JPM re-check | Carried from the registry |

- **Track KPI (this run's new one)**: **the ex-BRK-B eqflow − wflow gap.** It has crossed zero; the
  OW's stated reason is restored only if it goes positive again.
- **Anti-signal**: **HY OAS ≥ 3.10% on a close** (2.84% now, **six consecutive widening prints**) ⇒ it
  stops being a rate story and becomes **S26/S41**.
- ⚠ **Second anti-signal, newly relevant**: **IG OAS ≥ 0.90%** (0.81% now, 9bp away) ⇒ **S41**, and
  through **M147's shared beta (JPM 0.932)** that hits this sector first among the three OW carriers.

## 7 · Verdict on ROTATION's flagged divergence

**Question**: which leg is the OW actually long?
**Verdict**: **insurance and payments — and neither is what the OW was written on.** The steepener is
dead (R11), the breadth claim reversed on a robustness check (§0), and the **surviving carrier is a
12-name insurance node running at 1.48× the sector mean with 3 of 8 greens.** ⇒ **the OW is
defensible on the tape and mislabelled in the file.** Handed to BET as a composition finding.

## ✅ Coverage

flow ✅ (all 47 re-derived, not inherited) · players ✅ (4-node split, grouping stated as arbitrary,
C5) · IR/primary ✅ (MA 8-K + release; WFC/JPM NII guides carried) · chain map ✅ (dual chain, binding
constraint named **and named as currently unobservable**) · chain-hop — **n/a: no news thread in this
window names an under-covered financial** · KPI + anti-signal ✅ (one new KPI, two anti-signals, all
dated) · dispersion stated ✅ (**node spread +0.603 vs +0.298 = 0.305 flow points, against a sector
mean of +0.407 ⇒ the spread is 75% of the level, so the sector label is the wrong unit — W5**).
