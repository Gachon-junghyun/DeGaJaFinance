# -*- coding: utf-8 -*-
"""scripts/ 에서 리포 모듈(module_*)을 import 하기 위한 sys.path 부트스트랩.

왜 있나: `python scripts/foo.py` 로 돌리면 파이썬은 **스크립트가 있는 디렉토리**(scripts/)를
sys.path[0] 에 넣지, cwd(리포 루트)를 넣지 않는다. 그래서 리포 루트에서 실행해도
`from module_flow import …` 가 ModuleNotFoundError 로 죽는다 —
실측 2026-07-17: `python scripts/sector_flow.py --market us` (SWEEP 스테이지)가 이걸로 기동 불능,
매번 PYTHONPATH 를 손으로 걸어야 했다.

소비자마다 3줄씩 복붙하는 대신 여기 한 곳에서 붙인다(P1). scripts/ 는 스크립트 실행 시
항상 sys.path[0] 이므로 이 모듈 자체는 부트스트랩 없이 import 된다.

사용 — 리포 모듈을 import 하는 scripts/ 파일 맨 위에서, 그 import 보다 **먼저**:
    import _repo_path  # noqa: F401  (side-effect import: sys.path 에 리포 루트 삽입)
    from module_flow._investor import investor_flow
"""
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
