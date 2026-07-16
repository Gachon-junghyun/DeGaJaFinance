# -*- coding: utf-8 -*-
"""registry_audit — 코드↔맵 정합성 파수꾼 (§4.8 ★, verify 유닛의 하나).

module_*/ 와 scripts/ 의 실행 표면(CLI·서브커맨드)을 스캔 → MODULE_MAP.md(문서 맵)와
registry.json(기계 맵)에 등록됐는지 대조 → 분류표 축적. 읽기전용(코드 안 고침).

분류: OK(코드∧맵) · UNDOCUMENTED(코드엔 있는데 맵 모름=drift) · STALE(맵이 죽은 경로) · CLI_UNMAPPED.
산출: REGISTRY_AUDIT.md(분류표) + REGISTRY_AUDIT_LOG.jsonl(실행마다 커버리지% 1줄=진척 계량기).
맵 없어도 동작 → 발견 전량이 registry.json 시드.
"""
from __future__ import annotations

import json
import re
from datetime import datetime

from ._config import (
    AUDIT_LOG, AUDIT_MD, MODULE_GLOB, MODULE_MAP, REGISTRY_JSON, REPO_ROOT,
    SCRIPTS_DIR, utf8_stdout,
)

_ADD_PARSER = re.compile(r"""add_parser\(\s*["']([\w][\w-]*)["']""")


def _scan_code() -> dict[str, dict]:
    """실행 표면 스캔 → {capability: {kind, path, cli, subcommands[]}}."""
    caps: dict[str, dict] = {}
    # 모듈
    for mdir in sorted(REPO_ROOT.glob(MODULE_GLOB)):
        if not mdir.is_dir():
            continue
        main = mdir / "__main__.py"
        subs: list[str] = []
        if main.exists():
            text = "".join((f.read_text(encoding="utf-8", errors="ignore")
                            for f in mdir.glob("*.py")))
            subs = sorted(set(_ADD_PARSER.findall(text)))
        caps[mdir.name] = {"kind": "module", "path": str(mdir.relative_to(REPO_ROOT)),
                           "cli": main.exists(), "subcommands": subs}
    # 스크립트
    if SCRIPTS_DIR.exists():
        for s in sorted(SCRIPTS_DIR.glob("*.py")):
            name = f"scripts/{s.name}"
            has_cli = "__main__" in s.read_text(encoding="utf-8", errors="ignore")
            caps[name] = {"kind": "script", "path": str(s.relative_to(REPO_ROOT)),
                          "cli": has_cli, "subcommands": []}
    return caps


def _documented(name: str, map_text: str) -> bool:
    """capability 이름(또는 스크립트 stem)이 MODULE_MAP 에 등장하나."""
    if name in map_text:
        return True
    if name.startswith("scripts/"):
        stem = name[len("scripts/"):].removesuffix(".py")
        return stem in map_text
    return False


def run(as_json: bool = False) -> dict:
    utf8_stdout()
    caps = _scan_code()
    map_text = MODULE_MAP.read_text(encoding="utf-8", errors="ignore") if MODULE_MAP.exists() else ""
    prev = json.loads(REGISTRY_JSON.read_text(encoding="utf-8")) if REGISTRY_JSON.exists() else {"capabilities": {}}
    prev_caps = prev.get("capabilities", {})

    ok, undocumented, cli_unmapped = [], [], []
    for name, info in caps.items():
        documented = _documented(name, map_text)
        info["documented"] = documented
        if documented:
            ok.append(name)
        else:
            undocumented.append(name)
            if info["cli"]:
                cli_unmapped.append(name)

    # STALE = 이전 registry.json에 있었는데 지금 코드에 없는 것(죽은 경로)
    stale = [n for n in prev_caps if n not in caps]

    total = len(caps)
    coverage = round(100.0 * len(ok) / total, 1) if total else 0.0
    n_cli = sum(1 for i in caps.values() if i["cli"])

    stamp = datetime.now().isoformat(timespec="seconds")
    summary = {
        "date": stamp, "total": total, "cli": n_cli, "coverage_pct": coverage,
        "ok": len(ok), "undocumented": len(undocumented),
        "cli_unmapped": len(cli_unmapped), "stale": len(stale),
    }

    # registry.json 시드/갱신 (발견 전량 등록)
    REGISTRY_JSON.parent.mkdir(parents=True, exist_ok=True)
    REGISTRY_JSON.write_text(json.dumps(
        {"updated_at": stamp, "capabilities": caps}, ensure_ascii=False, indent=2), encoding="utf-8")
    # 추세 로그 append
    with open(AUDIT_LOG, "a", encoding="utf-8") as f:
        f.write(json.dumps(summary, ensure_ascii=False) + "\n")
    _render(caps, ok, undocumented, cli_unmapped, stale, summary)

    if as_json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(f"# registry_audit — 커버리지 {coverage}%  (문서화 {len(ok)}/{total}, CLI {n_cli})")
        print(f"  OK {len(ok)} · UNDOCUMENTED {len(undocumented)} · CLI_UNMAPPED {len(cli_unmapped)} · STALE {len(stale)}")
        if undocumented:
            print("  drift(맵이 모름): " + ", ".join(undocumented[:12]) + ("…" if len(undocumented) > 12 else ""))
        print(f"  → {AUDIT_MD.relative_to(REPO_ROOT)} · 추세 {AUDIT_LOG.relative_to(REPO_ROOT)}")
    return summary


def _render(caps, ok, undoc, cli_unmapped, stale, summary) -> None:
    L = ["# REGISTRY AUDIT — 코드↔맵 정합성", "",
         f"_갱신 {summary['date']} · 커버리지 **{summary['coverage_pct']}%** "
         f"(문서화 {summary['ok']}/{summary['total']} · CLI {summary['cli']})_", "",
         "> 리팩토링 진척 계량기. UNDOCUMENTED=코드엔 있는데 MODULE_MAP이 모름(drift). "
         "커버리지가 오르면 문서가 코드를 따라잡는 것. 추세는 REGISTRY_AUDIT_LOG.jsonl.", "",
         "| capability | kind | CLI | 서브커맨드 | 상태 |", "|---|---|---|---|---|"]
    for name in sorted(caps):
        i = caps[name]
        state = "✅ OK" if i["documented"] else ("🟠 CLI_UNMAPPED" if i["cli"] else "🟡 UNDOCUMENTED")
        subs = ", ".join(i["subcommands"][:6]) if i["subcommands"] else "—"
        L.append(f"| `{name}` | {i['kind']} | {'✓' if i['cli'] else ''} | {subs} | {state} |")
    if stale:
        L += ["", "## 🔴 STALE (맵이 죽은 경로 참조)", ""] + [f"- `{s}`" for s in stale]
    AUDIT_MD.write_text("\n".join(L), encoding="utf-8")


def cli_register(sub) -> None:
    p = sub.add_parser("audit", help="코드↔맵 정합성 스캔 → REGISTRY_AUDIT.md + 커버리지 추세")
    p.add_argument("--json", action="store_true")
    p.set_defaults(func=lambda a: run(as_json=a.json))
