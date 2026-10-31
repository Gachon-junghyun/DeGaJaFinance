# handoff/_archive/2026-10-31 — the full ledgers before the 2026-10-31 thinning

> **What this is.** The seven handoff ledgers exactly as they stood on 2026-10-31 (last written 2026-09-28), moved here
> with `git mv` so nothing is lost. **When to read:** when a thin file in `handoff/` points here with `A:Lnnn`
> (= this file, line nnn), or when you need a bracket's prose, an old fact row, an archived rule or a closed dig.
> **Not here:** the live view — that is the thin file of the same name in `handoff/`.

## What moved, and why

The desk read **4.65 MB** of handoff at every HANDOVER (STANDING_VIEW 968 KB · RESEARCH 971 KB · SCENARIOS 574+565+205 KB ·
STANDING_VIEW_US/KR 684/669 KB). Runs could not read that linearly, and conclusions drifted to whatever was easiest to
re-measure (investor flow) instead of earnings, competition and the financial environment. Owner's request, 2026-10-31:
keep only what has impact, move the rest to an archive.

| File here (byte-identical, SHA-256 checked) | Replaced in `handoff/` by | What the thin file keeps |
|---|---|---|
| `STANDING_VIEW.md` (967,724 B) | `STANDING_VIEW.md` (≈30 KB) | regime call · seed chain · asymmetry · **every retraction ID R1–R152 (one line each)** · contradictions C1–C29 + open un-numbered ones |
| `STANDING_VIEW_US.md` (683,599 B) | `STANDING_VIEW_US.md` (≈14 KB) | US registry rows touched since 09-10 · fact rows since 09-23 |
| `STANDING_VIEW_KR.md` (668,715 B) | `STANDING_VIEW_KR.md` (≈13 KB) | KR registry rows touched since 09-19 · fact rows since 09-20 |
| `RESEARCH.md` (970,700 B) | `RESEARCH.md` (≈30 KB) | 20 Part-A/B rules verbatim, ranked by impact, + T23 · U3 · U6 · the live dig list |
| `SCENARIOS.md` (573,533 B) | `SCENARIOS.md` (≈10 KB) | how to use the `module_lens` ledger · its open questions · open brackets NOT in the ledger · scoring rules |
| `SCENARIOS_US.md` (565,296 B) · `SCENARIOS_KR.md` (204,732 B) | pointers (≈1 KB each) | "read SCENARIOS.md and the ledger" |
| `handoff_README_pre-2026-10-31.md` (12,492 B) | `handoff/README.md` (rewritten) | copy of the old README, for its retention/toolkit history |

Numbers for dated questions now live in `module_lens` (`data/lens_ledger.db`, 165 legacy `S` brackets migrated).
⚠ `P###`, `M-###` and colliding `S##-KR` brackets were **not** migrated — only the ones still open on 09-28 are listed in
the thin `SCENARIOS.md`; the rest are here only.

## Older backups (untouched, still in `handoff/`)

The pre-existing snapshots stay where they were: `handoff/.STANDING_VIEW*.bak_*`, `.RESEARCH*.bak_*`, `.SCENARIOS*.bak_*`,
the `*.md.bak_08xx/09xx` files, and the folders `.bak_20260805/`, `.bak_20260806/`, `.presplit_bak_20260729/`.
`module_evidence` skips dot-prefixed paths but **does scan this folder**, so ID allocation (`next-id`) still sees every
M/D/R/P/C/S number used here.

## Restore

`git mv handoff/_archive/2026-10-31/<FILE>.md handoff/<FILE>.md` (after moving the thin file aside), or just read the
file here. Nothing was deleted. The thinning was produced by a one-off script kept with the orchestra run notes,
outside this repository.

## Change log
- 2026-10-31 — created by orchestra branch K3 (handoff thinning).
