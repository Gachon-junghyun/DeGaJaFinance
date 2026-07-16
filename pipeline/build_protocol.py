# -*- coding: utf-8 -*-
"""Protocol compiler — literally executes "protocol = a composition of L1 blocks".

Reads the L1 links of protocols/{name}.md in order, inlines each L1 (stage) body, then
appends the L2s (orchestration) those L1s call and the L3s (atomic functions) those L2s
call as appendices — emitting **one complete executable protocol** to
protocols/_compiled/{name}.md.

Because it composes by following the call hierarchy (protocol→L1→L2→L3) through links,
each L1 is defined once and protocols just reorder them (DRY). Adding a new L1/protocol
requires no change to this script.

Usage:
    python pipeline/build_protocol.py industry_us
    python pipeline/build_protocol.py industry_us industry_kr
    python pipeline/build_protocol.py --all
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PIPELINE = Path(__file__).resolve().parent
PROTO_DIR = PIPELINE / "protocols"
OUT_DIR = PROTO_DIR / "_compiled"

_LINK = re.compile(r"\]\(\.\./(L1_stages|L2_modules|L3_functions)/([\w./-]+?)\.md\)")


def _ordered_refs(text: str, layer: str) -> list[str]:
    """Return `../{layer}/NAME.md` links in text, in order of appearance, deduplicated."""
    seen, out = set(), []
    for lyr, name in _LINK.findall(text):
        if lyr == layer and name not in seen:
            seen.add(name)
            out.append(name)
    return out


def _read(layer: str, name: str) -> str:
    p = PIPELINE / layer / f"{name}.md"
    return p.read_text(encoding="utf-8") if p.exists() else f"_(missing: {layer}/{name}.md)_"


def compile_protocol(name: str) -> Path:
    proto = (PROTO_DIR / f"{name}.md").read_text(encoding="utf-8")

    # 1) L1 order (the protocol's composition)
    l1_names = _ordered_refs(proto, "L1_stages")
    l1_texts = {n: _read("L1_stages", n) for n in l1_names}

    # 2) L2s the L1s call (appearance order, global dedup)
    l2_names: list[str] = []
    for n in l1_names:
        for m in _ordered_refs(l1_texts[n], "L2_modules"):
            if m not in l2_names:
                l2_names.append(m)
    l2_texts = {n: _read("L2_modules", n) for n in l2_names}

    # 3) L3s the L2s call (appearance order, global dedup)
    l3_names: list[str] = []
    for n in l2_names:
        for m in _ordered_refs(l2_texts[n], "L3_functions"):
            if m not in l3_names:
                l3_names.append(m)

    parts = [
        f"# COMPILED PROTOCOL — {name}",
        "",
        f"> Auto-composed (build_protocol.py). Sources = `protocols/{name}.md` + L1/L2/L3 blocks.",
        f"> Composition order (L1): {' → '.join(l1_names)}",
        "> ⚠️ Do NOT edit — fix the L1/L2/L3 sources and recompile.",
        "",
        "---",
        "",
        "## Composition recipe (protocol)",
        "",
        proto.strip(),
        "",
        "---",
        "",
        "# ═══ L1 STAGES (execute in order) ═══",
    ]
    for i, n in enumerate(l1_names, 1):
        parts += ["", f"## [{i}/{len(l1_names)}] L1 · {n}", "", l1_texts[n].strip()]

    parts += ["", "---", "", "# ═══ APPENDIX A · L2 called by the L1s (orchestration) ═══"]
    for n in l2_names:
        parts += ["", f"### L2 · {n}", "", l2_texts[n].strip()]

    parts += ["", "---", "", "# ═══ APPENDIX B · L3 called by the L2s (single-role functions) ═══"]
    for n in l3_names:
        parts += ["", f"### L3 · {n}", "", _read("L3_functions", n).strip()]

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / f"{name}.md"
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"compiled {name}: L1 {len(l1_names)} · L2 {len(l2_names)} · L3 {len(l3_names)} → {out.relative_to(PIPELINE.parent)}")
    return out


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    args = sys.argv[1:]
    if not args:
        print("usage: python pipeline/build_protocol.py <protocol…> | --all")
        sys.exit(1)
    if args == ["--all"]:
        names = [p.stem for p in PROTO_DIR.glob("*.md")]
    else:
        names = args
    for n in names:
        compile_protocol(n)


if __name__ == "__main__":
    main()
