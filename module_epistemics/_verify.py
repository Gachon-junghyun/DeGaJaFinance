# -*- coding: utf-8 -*-
"""verify 루프 (§4.8 c) — verifier 플러그인 레지스트리.

verify/registry.json 에 verifier 하나 = {id, trigger, updates_ledger, module}.
새 검증 아이디어 = 유닛 등록 → 자동 편입(P5). 지금 등록: registry_audit(코드↔맵 파수꾼),
sensitivity_update(catalyst→가격반응→민감도 갱신), conflict_adjudicate(충돌→베이지안표).
"""
from __future__ import annotations

import json

from ._config import VERIFY_REGISTRY, utf8_stdout

_DEFAULT_VERIFIERS = {
    "registry_audit": {
        "trigger": "매 리팩토링 Phase 끝 / 수동",
        "updates_ledger": "REGISTRY_AUDIT.md · REGISTRY_AUDIT_LOG.jsonl",
        "module": "module_epistemics audit",
        "desc": "코드↔맵 정합성 스캔 + 커버리지 추세(진척 계량기)",
    },
    "conflict_adjudicate": {
        "trigger": "신호 충돌 시",
        "updates_ledger": "(산출: 베이지안 충돌표)",
        "module": "module_epistemics adjudicate",
        "desc": "모순 신호 → prior×LR×신뢰도 → posterior + 지배축",
    },
    "sensitivity_update": {
        "trigger": "catalyst 발화 → 실제 가격반응 관측",
        "updates_ledger": "sensitivity/{id}.md",
        "module": "module_epistemics sensitivity --add",
        "desc": "종목×factor 탄력·신뢰도 사후검증 갱신(alert-postmortem 패턴 재사용)",
    },
    "grounding_audit": {
        "trigger": "결론 산출 후",
        "updates_ledger": "(사후검사)",
        "module": "(미구현 — 인지 게이트 통과 여부 검사)",
        "desc": "결론이 관측값+출처+신선도 인지체크를 통과했나",
    },
}


def _load() -> dict:
    if VERIFY_REGISTRY.exists():
        try:
            return json.loads(VERIFY_REGISTRY.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"verifiers": dict(_DEFAULT_VERIFIERS)}


def ensure_seeded() -> dict:
    """레지스트리 없으면 기본 verifier로 시드."""
    VERIFY_REGISTRY.parent.mkdir(parents=True, exist_ok=True)
    reg = _load()
    for k, v in _DEFAULT_VERIFIERS.items():
        reg.setdefault("verifiers", {}).setdefault(k, v)
    VERIFY_REGISTRY.write_text(json.dumps(reg, ensure_ascii=False, indent=2), encoding="utf-8")
    return reg


def cli_register(sub) -> None:
    p = sub.add_parser("verify", help="verifier 플러그인 레지스트리 조회/시드")
    p.add_argument("--seed", action="store_true", help="기본 verifier로 registry.json 시드")
    p.set_defaults(func=lambda a: _run_cli(a))


def _run_cli(a) -> None:
    utf8_stdout()
    reg = ensure_seeded() if a.seed else _load()
    print("# verify 레지스트리 — verifier 플러그인")
    print(f"| id | trigger | 갱신 원장 | 실행 |")
    print("|---|---|---|---|")
    for vid, v in reg.get("verifiers", {}).items():
        print(f"| `{vid}` | {v.get('trigger','')} | {v.get('updates_ledger','')} | `{v.get('module','')}` |")
    if a.seed:
        print(f"\n시드 완료 → {VERIFY_REGISTRY}")
