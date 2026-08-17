#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""handoff_id_audit — READ-ONLY census of the three handoff/ ID counters.

Why this exists
---------------
`handoff/` runs three hand-incremented counters and nothing checks them:

    M###   fact rows      STANDING_VIEW*.md §2  (+ ARCHIVE_FACTS.md)
    S##    brackets       SCENARIOS*.md         (one `## S# — …` header per bracket)
    D##    open digs      RESEARCH.md Part C

Two desks (`industry_US`, `industry_kr`) append to the same counters from separate
files, so a collision is invisible until someone happens to grep. Measured 2026-08-03:
the 08-03 KR run drafted M306~M320 into a range the 08-02 US run had already shipped —
found by accident, not by a check.

This script does NOT fix anything and does NOT write to `handoff/`. It only counts.

Usage
-----
    python -X utf8 scripts/handoff_id_audit.py                # duplicate census
    python -X utf8 scripts/handoff_id_audit.py --next         # next free id per counter
    python -X utf8 scripts/handoff_id_audit.py --cite M250-M256   # who cites this range
    python -X utf8 scripts/handoff_id_audit.py --verbose      # print every dup site

Exit code 1 when a duplicate declaration exists (usable as a pre-writeback gate).
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from collections import defaultdict

try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HANDOFF = os.path.join(HERE, "handoff")

SV_FILES = ("STANDING_VIEW.md", "STANDING_VIEW_US.md", "STANDING_VIEW_KR.md")
SC_FILES = ("SCENARIOS.md", "SCENARIOS_US.md", "SCENARIOS_KR.md")
RS_FILES = ("RESEARCH.md",)
ARCHIVE = "ARCHIVE_FACTS.md"
ALL_FILES = SV_FILES + SC_FILES + RS_FILES + (ARCHIVE, "README.md")

# a declaration = the ID sits in the FIRST cell of a markdown table row
ROW_KEY = re.compile(r"^\|\s*~*\*{0,2}\s*([A-Z]\d+)\b")
# a scenario declaration = a `## S12 — …` header. The suffix is PART OF THE ID:
# `S14-ANNEX`/`S14-num` are deliberate annexes and `S46-KR` is the KR desk's own
# collision workaround (D76) — none of them are duplicate declarations.
SC_HDR = re.compile(r"^#{2,3}\s+(S\d+(?:-[A-Za-z]+)?)\s*[—\-–]")
SEC_HDR = re.compile(r"^#{2,3} ")

# ── the collisions that have ALREADY SHIPPED as of 2026-08-03 ────────────────
# Listed so this script can be used as a pre-writeback gate: it exits 1 only on a
# collision that is NOT on this list. ★ These are NOT to be renumbered — the rows
# are append-only and every existing citation would break (D137). A human decides
# the remedy; this list only stops the gate from crying wolf about known debt.
KNOWN = {
    # fact-row counter — 2026-07-29 industry_US vs 2026-07-30 industry_kr (D137)
    "M250", "M251", "M252", "M253", "M254", "M255", "M256",
    # dig counter — 27 shipped collisions found by this script 2026-08-03
    "D51", "D52", "D53", "D54", "D55", "D56", "D57", "D58", "D59",
    "D60", "D61", "D62", "D63", "D64", "D65",
    "D93", "D94", "D95", "D96", "D97", "D98", "D99",
    "D100", "D101", "D102", "D105", "D106",
    # dig ids re-declared as a STATUS UPDATE on the same dig (legitimate, not a collision)
    "D15", "D33", "D44", "D74",
}


def cells(line: str) -> int:
    return len([c for c in line.strip().strip("|").split("|")])


def load(fn: str) -> list[str]:
    p = os.path.join(HANDOFF, fn)
    if not os.path.exists(p):
        return []
    return open(p, encoding="utf-8-sig").read().split("\n")


def scan():
    """→ (declarations, citations)

    declarations[counter][id] = [ (file, lineno, section, ncells, text) ]
    citations[id]             = [ (file, lineno, text) ]
    """
    decl = {"M": defaultdict(list), "S": defaultdict(list), "D": defaultdict(list)}
    cites = defaultdict(list)
    for fn in ALL_FILES:
        lines = load(fn)
        sec = ""
        for i, line in enumerate(lines, 1):
            if SEC_HDR.match(line):
                sec = line.strip()[:90]
            # ── declarations ──────────────────────────────────────────────
            h = SC_HDR.match(line)
            if h and fn in SC_FILES:
                decl["S"][h.group(1)].append((fn, i, sec, 0, line.strip()[:110]))
            m = ROW_KEY.match(line)
            if m:
                fid = m.group(1)
                k = fid[0]
                n = cells(line)
                if k == "M" and fn in SV_FILES + (ARCHIVE,):
                    decl["M"][fid].append((fn, i, sec, n, line.strip()[:110]))
                elif k == "D" and fn in RS_FILES:
                    decl["D"][fid].append((fn, i, sec, n, line.strip()[:110]))
            # ── citations (any mention, anywhere) ─────────────────────────
            for fid in set(re.findall(r"\b([MSD]\d+)\b", line)):
                cites[fid].append((fn, i, line.strip()[:130]))
    return decl, cites


def is_definition(counter: str, ncells: int) -> bool:
    """A DEFINITION row carries the full schema; a status/update row is narrower.

    §2 fact table  : | # | Fact | Value | Source | asof | run |   -> 6
    Part C dig list: | # | Dig | Why it matters | Owner |         -> 4
    'Corrected this run' tables are | # | Change |                -> 2
    """
    if counter == "M":
        return ncells >= 5
    if counter == "D":
        return ncells >= 3
    return True


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--next", action="store_true", help="print the next free id per counter")
    ap.add_argument("--cite", help="report citation sites for an id or range, e.g. M250-M256")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()

    decl, cites = scan()

    if args.next:
        # This is the mechanical form of D137's "three greps, one line each" —
        # run it at WRITE time, not read time (D128).
        print("# next free id per counter  (max declared across BOTH markets + 1)")
        for k, where in (("M", "STANDING_VIEW*.md + ARCHIVE_FACTS.md"),
                         ("S", "SCENARIOS*.md headers"),
                         ("D", "RESEARCH.md Part C")):
            if not decl[k]:
                print(f"  {k}: (none declared)")
                continue
            mx = max(int(re.match(r"[A-Z](\d+)", i).group(1)) for i in decl[k])
            print(f"  {k}: highest declared {k}{mx}   ->  NEXT FREE {k}{mx + 1}"
                  f"        [{where}]")
        return 0

    if args.cite:
        rng = args.cite
        if "-" in rng and rng.count("-") == 1:
            a, b = rng.split("-")
            k = a[0]
            ids = [f"{k}{n}" for n in range(int(a[1:]), int(b[1:]) + 1)]
        else:
            ids = [rng]
        tot = 0
        for fid in ids:
            sites = cites.get(fid, [])
            dsites = {(f, l) for f, l, _, _, _ in decl[fid[0]].get(fid, [])}
            ext = [s for s in sites if (s[0], s[1]) not in dsites]
            print(f"\n## {fid} — {len(decl[fid[0]].get(fid, []))} declaration(s), "
                  f"{len(ext)} citation site(s) outside its own row")
            for f, l, t in ext:
                print(f"   {f}:{l}  {t}")
            tot += len(ext)
        print(f"\n  TOTAL external citation sites: {tot}")
        return 0

    # ── duplicate census ─────────────────────────────────────────────────
    print("# handoff ID counter audit  (read-only)\n")
    rc = 0
    num = lambda i: int(re.match(r"[A-Z](\d+)", i).group(1))
    for k, label in (("M", "fact rows"), ("S", "brackets"), ("D", "digs")):
        d = decl[k]
        ids = sorted(d, key=num)
        defs = {i: [s for s in d[i] if is_definition(k, s[3])] for i in ids}
        dups = {i: defs[i] for i in ids if len(defs[i]) > 1}
        new = {i: v for i, v in dups.items() if i not in KNOWN}
        nmax = max((num(i) for i in ids), default=0)
        holes = [n for n in range(1, nmax + 1) if f"{k}{n}" not in d]
        print(f"## {k}### {label}")
        print(f"   declared ids            {len(ids)}   (max {k}{nmax})")
        print(f"   declaration rows total  {sum(len(v) for v in d.values())}")
        print(f"   full-schema definitions {sum(len(v) for v in defs.values())}")
        print(f"   ★ COLLIDING ids         {len(dups)}"
              + (f"   -> {', '.join(dups)}" if dups else "   -> none"))
        print(f"     of which NEW (not in the known-shipped list): {len(new)}"
              + (f"   -> {', '.join(new)}" if new else "   -> none  [gate PASS]"))
        print(f"   unused numbers in range {len(holes)}"
              + (f"   ({', '.join(k + str(h) for h in holes[:14])}"
                 + (" …)" if len(holes) > 14 else ")") if holes else ""))
        if new:
            rc = 1
        if dups:
            for i, sites in dups.items():
                print(f"\n   ── {i} declared {len(sites)}× ──")
                for f, ln, sec, n, txt in sites:
                    print(f"      {f}:{ln}  [{n} cells]  {sec}")
                    if args.verbose:
                        print(f"          {txt}")
        print()
    return rc


if __name__ == "__main__":
    sys.exit(main())
