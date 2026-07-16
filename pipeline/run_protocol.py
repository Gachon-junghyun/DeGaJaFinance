# -*- coding: utf-8 -*-
"""Stage-gated protocol runner — feeds ONE L1 stage at a time (context-loss guard).

`build_protocol.py` inlines all L1 stages into one monolith; reading 8 stages at once
dilutes the early context by the time you reach the verdict. This runner instead emits a
single stage's slice — that L1 stage + only the L2 modules it calls + only the L3 functions
those L2s (and the L1 itself) call — plus an EXIT-CHECK gate. Do the stage, pass the gate,
advance. Each stage is loaded fresh and small, so nothing upstream is forgotten.

A checkpoint at out/pipeline_runs/{name}.json tracks the current stage, which passed, and the
run's target (e.g. ticker). One active run per protocol.

Usage:
    python pipeline/run_protocol.py real_alpha_kr --start --target 009150
    python pipeline/run_protocol.py real_alpha_kr --show     # reprint current stage
    python pipeline/run_protocol.py real_alpha_kr --next      # mark current passed → print next
    python pipeline/run_protocol.py real_alpha_kr --status    # progress table
    python pipeline/run_protocol.py real_alpha_kr --goto 4    # jump to stage 4
"""
from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

from build_protocol import PROTO_DIR, _ordered_refs, _read  # reuse the same link resolver

RUN_DIR = Path(__file__).resolve().parent.parent / "out" / "pipeline_runs"


def _l1_order(name: str) -> list[str]:
    proto = (PROTO_DIR / f"{name}.md").read_text(encoding="utf-8")
    return _ordered_refs(proto, "L1_stages")


def _stage_slice(name: str, idx1: int) -> str:
    """Compile ONLY stage idx1 (1-based): its L1 + the L2s it calls + the L3s those L2s
    (and the L1 directly) call. Self-contained, small."""
    l1_names = _l1_order(name)
    total = len(l1_names)
    n = l1_names[idx1 - 1]
    l1_text = _read("L1_stages", n)

    l2_names = _ordered_refs(l1_text, "L2_modules")
    l2_texts = {m: _read("L2_modules", m) for m in l2_names}

    l3_names: list[str] = []
    for m in l2_names:  # L3s reached via this stage's L2s
        for x in _ordered_refs(l2_texts[m], "L3_functions"):
            if x not in l3_names:
                l3_names.append(x)
    for x in _ordered_refs(l1_text, "L3_functions"):  # L3s the L1 calls directly
        if x not in l3_names:
            l3_names.append(x)

    prev_n = l1_names[idx1 - 2] if idx1 > 1 else None
    next_n = l1_names[idx1] if idx1 < total else None

    parts = [
        f"# ═══ STAGE {idx1}/{total} · {n}  (protocol: {name}) ═══",
        f"> prev: {prev_n or '—(첫 스테이지)'}   |   next: {next_n or '—(마지막)'}",
        "> Do ONLY this stage. Pass its EXIT CHECK, then `run_protocol.py "
        f"{name} --next`. Earlier stages' outputs are on disk — reread the run dir, not memory.",
        "",
        "## L1 stage",
        "",
        l1_text.strip(),
    ]
    if l2_names:
        parts += ["", "---", "", "## L2 called by this stage (orchestration)"]
        for m in l2_names:
            parts += ["", f"### L2 · {m}", "", l2_texts[m].strip()]
    if l3_names:
        parts += ["", "---", "", "## L3 called (single-role functions)"]
        for x in l3_names:
            parts += ["", f"### L3 · {x}", "", _read("L3_functions", x).strip()]
    parts += [
        "",
        "---",
        f"> ✅ When this stage's EXIT CHECK passes → `python pipeline/run_protocol.py {name} --next`",
    ]
    return "\n".join(parts)


def _ckpt_path(name: str) -> Path:
    return RUN_DIR / f"{name}.json"


def _load_ckpt(name: str) -> dict | None:
    p = _ckpt_path(name)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else None


def _save_ckpt(name: str, ck: dict) -> None:
    RUN_DIR.mkdir(parents=True, exist_ok=True)
    _ckpt_path(name).write_text(json.dumps(ck, ensure_ascii=False, indent=2), encoding="utf-8")


def _status(name: str, ck: dict) -> str:
    rows = []
    for i, s in enumerate(ck["stages"], 1):
        mark = "✅" if ck["passed"][i - 1] else ("▶" if i == ck["stage"] else "·")
        rows.append(f"  {mark} {i}/{len(ck['stages'])} {s}")
    head = (f"# RUN {name} · target={ck.get('target') or '—'} · started {ck['started']} · "
            f"현재 스테이지 {ck['stage']}/{len(ck['stages'])}")
    return head + "\n" + "\n".join(rows)


def main() -> None:
    try:
        import sys
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("--start", action="store_true")
    ap.add_argument("--next", dest="advance", action="store_true")
    ap.add_argument("--show", action="store_true")
    ap.add_argument("--status", action="store_true")
    ap.add_argument("--goto", type=int, default=0)
    ap.add_argument("--target", default="")
    a = ap.parse_args()
    name = a.name
    stages = _l1_order(name)
    if not stages:
        print(f"프로토콜 {name} 에 L1 스테이지가 없다."); return

    if a.start:
        ck = {"target": a.target, "started": date.today().isoformat(),
              "stages": stages, "stage": 1, "passed": [False] * len(stages)}
        _save_ckpt(name, ck)
        print(_status(name, ck)); print("\n" + "=" * 80 + "\n")
        print(_stage_slice(name, 1)); return

    ck = _load_ckpt(name)
    if ck is None:
        print(f"체크포인트 없음 — 먼저 `run_protocol.py {name} --start` 하라."); return
    # keep checkpoint stage-list fresh if the protocol was recompiled/edited
    ck["stages"] = stages
    if len(ck["passed"]) != len(stages):
        ck["passed"] = (ck["passed"] + [False] * len(stages))[:len(stages)]

    if a.status:
        print(_status(name, ck)); return
    if a.goto:
        ck["stage"] = max(1, min(a.goto, len(stages))); _save_ckpt(name, ck)
        print(_stage_slice(name, ck["stage"])); return
    if a.show:
        print(_stage_slice(name, ck["stage"])); return
    if a.advance:
        ck["passed"][ck["stage"] - 1] = True
        if ck["stage"] >= len(stages):
            _save_ckpt(name, ck)
            print(_status(name, ck))
            print(f"\n🏁 {name} 완주 — 모든 스테이지 통과. VERDICT 산출물/원장 확인.")
            return
        ck["stage"] += 1
        _save_ckpt(name, ck)
        print(f"✅ 이전 스테이지 통과. → 다음\n\n" + "=" * 80 + "\n")
        print(_stage_slice(name, ck["stage"])); return
    # default: show status + current stage
    print(_status(name, ck)); print("\n" + "=" * 80 + "\n"); print(_stage_slice(name, ck["stage"]))


if __name__ == "__main__":
    main()
