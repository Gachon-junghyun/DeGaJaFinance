# -*- coding: utf-8 -*-
"""module_epistemics — 인식 루프 (베이지안 충돌평가 + 민감도 학습 + verify).

HANDOFF_SPEC §4.8 구현. 신호가 모순일 때 손퉁하지 않고 구조화하고, 종목별 민감도를
축적·검증하며, 확장 가능한 verifier 플러그인으로 코드↔맵 정합성까지 감사한다.

닫힌 루프:
    [인지] 알아야 말한다 → [충돌평가] 학습된 민감도로 가중 → 지배축 → [결과관측]
    catalyst 후 실제가격 → [민감도 갱신] ↺ 다음 판단의 prior/weight로 되먹임.

기능 지도:
    _bayes          충돌평가 — prior×LR×신뢰도 → posterior + 지배축(argmax LR×신뢰도)
    _sensitivity    민감도 원장 — 종목×factor 탄력·신뢰도 축적, factor_confidence 조회
    _verify         verifier 플러그인 레지스트리
    _registry_audit 코드↔맵 정합성 파수꾼 + 커버리지 추세(진척 계량기)

CLI:
    python -m module_epistemics audit
    python -m module_epistemics adjudicate 000660 --thesis "HBM 재평가" --signals '[...]'
    python -m module_epistemics sensitivity 000660 [--add FACTOR --dir +강 --conf 0.85 --event ...]
    python -m module_epistemics verify [--seed]
"""
from ._bayes import adjudicate, render as render_adjudication
from ._sensitivity import factor_confidence, load as load_sensitivity, update as update_sensitivity
from ._registry_audit import run as registry_audit
from ._verify import ensure_seeded as seed_verifiers

__all__ = [
    "adjudicate", "render_adjudication",
    "factor_confidence", "load_sensitivity", "update_sensitivity",
    "registry_audit", "seed_verifiers",
]
