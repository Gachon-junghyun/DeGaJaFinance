#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""handoff_compact — keep the analytical carry inside a size budget, by measurement.

Why this exists
---------------
`handoff/` is read IN FULL at the start of every run. Measured 2026-07-25:

    STANDING_VIEW.md  132 KB   (76% of it un-curated per-run append blocks)
    SCENARIOS.md       72 KB
    RESEARCH.md        82 KB
    ------------------------
    handoff/          286 KB   every run, growing ~30 KB per run

The 2026-07-25 `industry_US` run alone appended **26.9 KB** to STANDING_VIEW — more than the
file's entire live view (§1+§3+§4+§5+§6 = 25.7 KB). Meanwhile the evidence for the file's own
top-line regime call (the 84.6% / 59% / 41.5 margin series) sits **only** inside an 07-22 append
block and appears nowhere in the live view.

`handoff/README.md` says **"Append-only for reversals."** That rule is scoped to reversals — the
§5 retracted ledger. It was being applied to everything, which is what produced the archaeology.

What this does
--------------
Moves spent facts out of STANDING_VIEW into `handoff/ARCHIVE_FACTS.md`. **Nothing is deleted.**
A fact is RETAINED when any of these holds:

  KEEP-1  cited by ID anywhere in the live view (§1/§3/§4/§5/§6), SCENARIOS.md or RESEARCH.md
  KEEP-2  listed in PIN (load-bearing but cited by prose, not by ID — e.g. the margin series
          the regime call rests on)
  KEEP-3  younger than --age-guard runs (a new fact has not had time to be cited; pruning it
          would be the "verify runs after assert" failure this desk keeps logging)
  KEEP-4  it is the LATEST member of a replication family (repeated measurements of one
          mechanism collapse to one row + a counter, rather than N rows)

Everything else is archived with its source-run header intact, so it stays greppable.

§5 (the retracted ledger) is never touched — it is byte-identical before and after, by assertion.

Usage
-----
    python -X utf8 scripts/handoff_compact.py                 # dry-run, prints the plan
    python -X utf8 scripts/handoff_compact.py --apply         # writes
    python -X utf8 scripts/handoff_compact.py --budget-only   # just report sizes vs budget
"""
from __future__ import annotations

import argparse
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANDOFF = os.path.join(HERE, "handoff")
SV = os.path.join(HANDOFF, "STANDING_VIEW.md")
ARCHIVE = os.path.join(HANDOFF, "ARCHIVE_FACTS.md")

# ── budgets (KB). Breaching one is a finding to report, not an error to raise. ──
# Set from the measured floor, not from a wish: after the 2026-07-25 consolidation the
# genuinely-live content is §3 registry 17.9 + §5 ledger 10.5 (permanent) + §6 contradictions 7.6
# + §1/§4 0.9 = 36.9 KB. §2 gets the remaining ~23 KB, which at ~0.25 KB/row is ~90 facts.
# ★ SPLIT BY MARKET 2026-07-29 (the 8-run escalation, resolved by a human). No desk reads all
# five carry files any more: a US run reads the two spines + the two _US files; a KR run reads the
# two spines + the two _KR files. RESEARCH.md is shared and un-split (its rules bind both desks).
BUDGET = {
    "STANDING_VIEW.md": 45,      # spine: asof chain + §1 regime + §2 seed chain + §4 + §5 + §6
    "STANDING_VIEW_US.md": 50,   # §2 US fact rows + §3a registry
    "STANDING_VIEW_KR.md": 50,   # §2 KR fact rows + §3b registry
    "SCENARIOS.md": 20,          # spine: legend + scoring rules + master log + master index
    "SCENARIOS_US.md": 50,
    "SCENARIOS_KR.md": 50,
    "RESEARCH.md": 85,
}
# what each desk actually reads — the number that matters after the split
READS = {
    "US": ("STANDING_VIEW.md", "STANDING_VIEW_US.md", "SCENARIOS.md", "SCENARIOS_US.md",
           "RESEARCH.md", "README.md"),
    "KR": ("STANDING_VIEW.md", "STANDING_VIEW_KR.md", "SCENARIOS.md", "SCENARIOS_KR.md",
           "RESEARCH.md", "README.md"),
}
PER_DESK_BUDGET = 250  # KB, excluding README

# ⚠ The row-length rule that keeps §2 inside its share. Measured 2026-07-25: the industry_US run
# wrote 33 fact rows in 19.6 KB = 0.59 KB/row — one run's facts outweighed the file's entire live
# view. A fact row is a NUMBER PLUS ITS SOURCE, not a paragraph; the argument belongs in §3 or in
# the run's own report.
ROW_KB_WARN = 0.35

# KEEP-2 — load-bearing by content, not cited by ID. Curated by a human; the script
# never adds to this list on its own.
PIN = {
    # the measured chain §1's regime call rests on (margin level/rate + capacity + multiple)
    "M1", "M2", "M3", "M4", "M5", "M6", "M7", "M18",
    # the two mechanisms the desk re-measures every run
    "M25", "M74",
}

# KEEP-4 — replication families: {family: [members oldest→newest]}. Only the newest is
# retained inline; the rest are archived and the survivor gets a counter appended.
FAMILIES = {
    "green-gate is a volume test": ["M25", "M38", "M55", "M75", "M144"],
    "duration REITs vs digital infrastructure": ["M24", "M37", "M88", "M131"],
    "US has no KR RS-baseline defect": ["M74", "M145"],
    "epicenter check is one layer off": ["M81", "M146"],
    "every event straddle expires before its event": ["M89", "M47"],
}

RUN_HDR = re.compile(r"^#{3} (Added by|Retracted by|Retracted this run|Per-name)", re.M)
FACT_ROW = re.compile(r"^\|\s*\*{0,2}(M\d+)\*{0,2}\s*\|")
SEC_HDR = re.compile(r"^#{2,3} ")
LIVE_SEC = re.compile(r"^#{2,3} (1\.|2\.|3\.|4\.|5\.|6\.)")


def kb(s: str) -> float:
    return len(s.encode("utf-8")) / 1024


def split_blocks(text: str):
    """→ [(header_line, block_text)] split on every ## / ### header."""
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if SEC_HDR.match(l)]
    if not starts:
        return [("", text)]
    out = []
    pre = "\n".join(lines[: starts[0]])
    if pre.strip():
        out.append(("__PREAMBLE__", pre))
    bounds = starts + [len(lines)]
    for a, b in zip(bounds, bounds[1:]):
        out.append((lines[a], "\n".join(lines[a:b])))
    return out


def cited_ids(*texts: str) -> set[str]:
    hits: set[str] = set()
    for t in texts:
        hits |= set(re.findall(r"\bM\d+\b", t))
    return hits


def run_date_of(header: str) -> str:
    m = re.search(r"(20\d{2}-\d{2}-\d{2})", header)
    return m.group(1) if m else ""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--apply", action="store_true", help="write the files (default: dry-run)")
    ap.add_argument("--budget-only", action="store_true")
    ap.add_argument("--age-guard", type=int, default=2,
                    help="protect facts from the N most recent run-blocks (default 2)")
    args = ap.parse_args()

    # ── budget report ────────────────────────────────────────────────────────
    print("# handoff budget")
    total = 0.0
    NOT_READ = {"ARCHIVE_FACTS.md"}   # written here, deliberately NOT read at HANDOVER
    for f in sorted(os.listdir(HANDOFF)):
        if not f.endswith(".md"):
            continue
        size = os.path.getsize(os.path.join(HANDOFF, f)) / 1024
        if f in NOT_READ:
            print(f"  {f:22s}{size:>8.1f} KB   (archive — not read at HANDOVER, excluded)")
            continue
        total += size
        bud = BUDGET.get(f)
        flag = ""
        if bud:
            flag = f"  budget {bud:>3} KB  {'OVER by %.0f KB' % (size - bud) if size > bud else 'ok'}"
        print(f"  {f:22s}{size:>8.1f} KB{flag}")
    def _kb(f):
        _q = os.path.join(HANDOFF, f)
        return os.path.getsize(_q) / 1024 if os.path.exists(_q) else 0.0
    print()
    for _desk, _files in READS.items():
        _t = sum(_kb(f) for f in _files)
        _over = _t - PER_DESK_BUDGET
        print(f"  {_desk} run reads {_t:>7.1f} KB   budget {PER_DESK_BUDGET} KB   "
              f"{'OVER by %.0f KB' % _over if _over > 0 else 'ok'}")
        print(f"       ({' + '.join(_files)})")

    # row-length check on §2 — the axis that actually drives regrowth
    _sv = ""
    for _f in ("STANDING_VIEW.md", "STANDING_VIEW_US.md", "STANDING_VIEW_KR.md"):
        _p2 = os.path.join(HANDOFF, _f)
        if os.path.exists(_p2):
            _sv += open(_p2, encoding="utf-8").read()
    _rows = [l for l in _sv.split("\n") if FACT_ROW.match(l)]
    if _rows:
        avg = sum(len(r.encode()) for r in _rows) / len(_rows) / 1024
        verdict = "ok" if avg <= ROW_KB_WARN else f"OVER (rule: <= {ROW_KB_WARN} KB/row)"
        print(f"\n  §2 fact rows: {len(_rows)}   avg {avg:.2f} KB/row   {verdict}")
        if avg > ROW_KB_WARN:
            fat = sorted(_rows, key=lambda r: -len(r))[:3]
            for r in fat:
                print(f"    fattest: {len(r.encode())/1024:.2f} KB  {r[:76]}")
    if args.budget_only:
        return 0

    sv = open(SV, encoding="utf-8").read()
    blocks = split_blocks(sv)

    live = "".join(b for h, b in blocks if h == "__PREAMBLE__" or LIVE_SEC.match(h))
    appended = [(h, b) for h, b in blocks if h != "__PREAMBLE__" and not LIVE_SEC.match(h)]

    others = ""
    for f in ("SCENARIOS.md", "SCENARIOS_US.md", "SCENARIOS_KR.md",
              "STANDING_VIEW_US.md", "STANDING_VIEW_KR.md",
              "RESEARCH.md", "README.md"):
        p = os.path.join(HANDOFF, f)
        if os.path.exists(p):
            others += open(p, encoding="utf-8").read()

    keep_cited = cited_ids(live, others)

    # age guard: protect the most recent N distinct run-dates among append blocks
    dates = sorted({run_date_of(h) for h, _ in appended if run_date_of(h)}, reverse=True)
    young = set(dates[: args.age_guard])

    # replication families: newest member survives inline
    fam_survivor = {members[-1]: name for name, members in FAMILIES.items()}
    fam_superseded = {m for members in FAMILIES.values() for m in members[:-1]}

    kept, archived = [], []
    for h, body in appended:
        d = run_date_of(h)
        for line in body.split("\n"):
            m = FACT_ROW.match(line)
            if not m:
                continue
            fid = m.group(1)
            why = None
            if fid in PIN:
                why = "KEEP-2 pinned"          # absolute — a human put it here
            elif fid in fam_superseded:
                why = None                     # a superseded replication is archived even if cited
            elif fid in keep_cited:
                why = "KEEP-1 cited"
            elif d in young:
                why = f"KEEP-3 age-guard ({d})"
            elif fid in fam_survivor:
                why = f"KEEP-4 family survivor ({fam_survivor[fid]})"
            (kept if why else archived).append((fid, d, why, line))

    print("\n# STANDING_VIEW.md compaction plan")
    print(f"  live view (S1-S6)      {kb(live):>8.1f} KB")
    app_kb = sum(kb(b) for _, b in appended)
    print(f"  per-run append blocks  {app_kb:>8.1f} KB   ({len(appended)} blocks)")
    print(f"  fact rows: {len(kept) + len(archived)} total -> KEEP {len(kept)} / ARCHIVE {len(archived)}")
    saved = sum(kb(l) for _, _, _, l in archived)
    print(f"  archivable weight      {saved:>8.1f} KB")

    from collections import Counter
    for why, n in Counter(w for _, _, w, _ in kept).most_common():
        print(f"    KEEP  {n:>3}  {why}")

    if archived:
        print("\n  archived (first 12):")
        for fid, d, _, line in archived[:12]:
            print(f"    {fid:6s} {d}  {line[:88]}")
        if len(archived) > 12:
            print(f"    … and {len(archived) - 12} more")

    if not args.apply:
        print("\n(dry-run — nothing written. re-run with --apply)")
        return 0

    # ── apply: strip archived rows from the append blocks, write the archive ──
    arch_ids = {fid for fid, _, _, _ in archived}
    new_blocks = []
    for h, body in blocks:
        if h == "__PREAMBLE__" or LIVE_SEC.match(h):
            new_blocks.append(body)
            continue
        out_lines = []
        for line in body.split("\n"):
            m = FACT_ROW.match(line)
            if m and m.group(1) in arch_ids:
                continue
            out_lines.append(line)
        kept_rows = [l for l in out_lines if FACT_ROW.match(l)]
        # drop a block that no longer carries any fact row and is not a thesis/retraction block
        if not kept_rows and h.startswith("### Added by"):
            new_blocks.append(
                h + f"\n\n> Fully archived to `ARCHIVE_FACTS.md` by `handoff_compact.py` "
                    f"— {len([1 for fid,_,_,_ in archived if True])} rows moved, none deleted.\n"
            )
            continue
        new_blocks.append("\n".join(out_lines))

    before5 = re.search(r"## 5\. Retracted ledger.*?(?=\n## 6\.)", sv, re.S)
    new_sv = "\n".join(new_blocks)
    after5 = re.search(r"## 5\. Retracted ledger.*?(?=\n## 6\.)", new_sv, re.S)
    assert before5 and after5 and before5.group(0) == after5.group(0), \
        "§5 retracted ledger changed — refusing to write"

    header = "" if os.path.exists(ARCHIVE) else (
        "# ARCHIVE_FACTS — spent measurements, moved out of STANDING_VIEW\n\n"
        "> Written by `scripts/handoff_compact.py`. **Nothing here was deleted** — these rows left the\n"
        "> live carry because nothing cites them any more. Greppable by fact id when one is needed again.\n"
        "> The retracted ledger (STANDING_VIEW §5) is never archived; a killed claim must stay visible.\n"
    )
    with open(ARCHIVE, "a", encoding="utf-8") as fh:
        fh.write(header)
        fh.write(f"\n## Archived {len(archived)} rows on this pass\n\n")
        cur = None
        for fid, d, _, line in archived:
            if d != cur:
                fh.write(f"\n### from the {d} run\n\n")
                cur = d
            fh.write(line + "\n")

    open(SV, "w", encoding="utf-8").write(new_sv)
    print(f"\n[written] {SV}  {kb(sv):.1f} KB -> {kb(new_sv):.1f} KB")
    print(f"[written] {ARCHIVE}  (+{len(archived)} rows)")
    print("[asserted] §5 retracted ledger byte-identical")
    return 0


if __name__ == "__main__":
    sys.exit(main())
