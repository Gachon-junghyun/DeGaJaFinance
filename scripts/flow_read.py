# -*- coding: utf-8 -*-
"""flow_read — 호환 shim. 엔진은 module_flow 가 단일 원본(P1 재사용, 수식 이식 0).

옛 리포에선 scripts/flow_read.py 가 엔진이었지만 여기선 module_flow 로 기능분해됐다.
sector_flow 등 `import flow_read` 하는 스크립트가 그대로 돌도록 이름을 re-export 한다.
CLI(flow 태그 테이블)는 `python -m module_flow` 를 쓴다.
"""
from __future__ import annotations

import _repo_path  # noqa: F401  — scripts/ 실행 시 sys.path 에 리포 루트 삽입(아래 import 전에)
from module_flow._investor import investor_flow
from module_flow._news_velocity import news_query as _news_query
from module_flow._news_velocity import news_velocity
from module_flow._price_flow import price_flow
from module_flow._short import positioning
from module_flow._synthesize import flow_tag

__all__ = ["price_flow", "news_velocity", "_news_query", "flow_tag", "positioning", "investor_flow"]
