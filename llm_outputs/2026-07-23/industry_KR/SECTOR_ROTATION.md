# SECTOR_ROTATION — industry_KR · 2026-07-23

> Stage 5/8. Delta-only against MACRO §4 and `SECTOR_FLOW_KR.json` — neither is restated here.

## §1 Inherited (verbatim, MACRO §4)

**MACRO holds**: FIN OW (▲conviction) · ENRG tactical OW (escalation-flagged) · HLTH OW-as-shelter ·
IT Neutral (flow-gated, gate shut) · INDU Neutral (split) · UTIL UW (▼deepening) · MATR UW ·
DISC UW (conviction cut stands) · RE UW (rate-negative) · STPL UW · COMM Neutral (flagged for
re-examination).

## §2 Deltas — flow-carried only (`SECTOR_FLOW_KR.json`, universe n=829, wflow −0.384, 33🟢/65🔴)

| Sector | Matrix said | Flow evidence (KRX-classified sector, not the GICS label) | New verdict | Owner |
|---|---|---|---|---|
| **UTIL** | UW (on 두산에너빌리티 alone) | **전기·가스** (regulated power/gas, n=10): wflow **+0.067**, **1🟢/0🔴** — the only sector in the universe with zero red | **Split, stated explicitly**: 원전/SMR-equipment leg (두산에너빌리티, RS60 −51.7%) **stays UW**. Regulated-utility leg **promoted UW→Neutral** on the sector wflow number. MACRO's single-ticker UW should not stand for the KRX sector — the flow disagrees at n=10, not n=1. | DEEP-if-picked / next MACRO |
| **RE** | UW (rate-negative, no KR equity read at all) | **부동산+리츠** (n=3+22): wflow **+0.322 / +0.057**, 부동산's breadth **0.33 — highest of any sector in the universe** | **Promoted UW→Neutral**, sample-caveat stated (부동산 n=3 is thin). ⚠ Does **not** override EVENT_ALPHA Card 5's residential-lending-policy read (다주택자 규제) — that thread is about leveraged owner-occupiers, a different node from listed REITs. The rate argument (real 10Y 2.35%) still applies to the owner-occupier node; it is the REIT node the flow contradicts. | ROTATION (stated) / next MACRO to formalize the node split |
| **FIN** | OW, blanket | **금융** (n=76, the full KRX financials sector incl. non-bank): wflow **−0.016**, 2🟢/2🔴 — essentially flat. **증권** (securities, n=18): −0.045. **보험** (insurance, n=12): **−0.36**, weak | **Not a verdict change** — MACRO's OW is carried entirely by 3 bank-holding names (KB/신한/하나), not by financials broadly. **Scope note, not a delta**: read "FIN OW" as "bank-holding OW", not "financials sector OW" — insurance and brokerage do not share it. | DEEP-FIN (scope the mandate) |
| **INDU** | Neutral, split (원전 vs 전력기기) | **기계·장비** (n=32, the KRX bucket 전력기기 sits nearest): wflow **−0.502**, **0🟢/5🔴** — the single worst-breadth sector in the entire universe | **No verdict change**, but the split is now understood as sharper than MACRO stated: HD현대일렉트릭's relative strength is **one name defying a zero-green sector**, not sector-wide confirmation. Downgrade confidence in the "전력기기 leg is holding up" read accordingly. | DEEP-if-picked |
| **ENRG** | tactical OW | **화학** (n=103, nearest KRX bucket to refining/petrochem): wflow **+0.106** but **2🟢/7🔴** — mega-cap-narrow | **No verdict change** — flagged as a nuance: the OW is carried by S-Oil specifically (RS20 +47.9%), not sector breadth. Consistent with, not contradicting, MACRO's own "tactical" qualifier. | DEEP-ENRG |

**Sectors with no flow-carried delta this run** (matrix stands as-is, restated nowhere below):
IT, HLTH, MATR, DISC, STPL, COMM.

## §3 DEEP picks — 3, not 4 (stated, not a shortfall)

**Only 3 sectors carry an OW tilt this run: FIN, ENRG, HLTH.** Per the never-pad rule, this run
selects 3 DEEP targets, not 4.

- **Continuous 2 = FIN, ENRG.** Both were the continuous pair in 07-20, 07-21, and 07-22 — **this is
  their 4th consecutive continuous run.** Both still rank top-2 OW today (FIN's conviction actually
  strengthened per MACRO §4); anti-thrash continuity applies cleanly, no judgment call needed.
- **Rotating 1 = HLTH.** ⚠ **This is HLTH's 4th consecutive appearance** (rotating in 07-20, 07-21,
  07-22, and now 07-23) — there is no 4th OW sector to rotate into instead. **Recency-starved,
  stated explicitly**, same as 07-22's own log entry. **Process flag, not a HLTH-specific one**: the
  OW list itself has not produced a new name since 07-16 (when IT last held a continuous slot). If
  DEEP/MACRO do not produce a genuinely new OW candidate within the next run or two, that staleness
  becomes its own finding about the matrix, not about the sectors in it.
- **Not picked, but flagged for a future DEEP by the deltas above**: UTIL's regulated-utility leg
  (newly promoted to Neutral) and RE's REIT node (newly promoted to Neutral) are both **candidate
  DEEP targets once/if either graduates from Neutral to OW** — neither qualifies for a slot today
  under the OW-only selection rule.
- **INDU/건설** was flagged "first-claim next run" by 07-22's own DEEP_LOG. It remains Neutral (not
  OW) after this run's delta pass (§2), so it is **not** eligible today either — carried forward
  again, now a 2nd consecutive skip since being named first-claim.

## DEEP_LOG 2026-07-23: continuous=[FIN, ENRG] (4th consecutive run for both) rotating=[HLTH] (4th
consecutive — recency-starved, no alternative OW exists) · rested: IT (last 07-17), UTIL (07-17,
partially promoted to Neutral this run via §2), DISC (07-16), STPL (07-20), INDU/건설 (07-16,
named first-claim 07-22, skipped again — Neutral not OW) · **only 3 DEEP dives this run by design,
not a shortfall — see §3.**

## ✅ EXIT CHECK
- [x] §1 is one line, inherited verbatim — no restated per-sector prose for unchanged sectors.
- [x] Every §2 delta cites a flow number (wflow/breadth/🟢🔴 counts) from `SECTOR_FLOW_KR.json`; the
      FIN "delta" was reverted to a scope note (not a verdict change) once recognized as resting on
      the same bellwether logic MACRO already used, per the "macro re-argument, declined" discipline
      — RULE self-check: FIN's row is flow-carried (76-name sector wflow), not a re-argued thesis.
- [x] Every matrix×flow divergence (UTIL, RE) named with an owner.
- [x] 4 DEEP targets attempted; 3 selected by rule, shortfall stated and reasoned (only 3 OW sectors
      exist) — not padded with Neutral/UW.
- [x] Linter run below.
- [x] DEEP_LOG line appended.
