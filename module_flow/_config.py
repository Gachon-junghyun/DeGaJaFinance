# -*- coding: utf-8 -*-
"""module_flow 설정 — 경로·헬퍼. 뉴스 소스집합·FTS 경로는 재사용(복제 금지, P1).

FOREIGN_SOURCES 와 FTS_DB 는 module_news_data._config 가 단일 원본이다.
여기서 import 만 한다 — flow 가 자기 사본을 두면 두 곳이 갈라진다.
KIS/KRX 시크릿(.env)도 module_KIS 와 같은 폴백 순서로 로드.
"""
from __future__ import annotations

import os
from pathlib import Path

# ── 뉴스 소스집합·FTS 경로: module_news_data 가 단일 원본 (P1 재사용) ──────
from module_news_data._config import (  # noqa: E402
    FOREIGN_SOURCES, FTS_DB, utf8_stdout,
)

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parent
OUT_DIR = REPO_ROOT / "out" / "flow"
SI_CACHE = OUT_DIR / "short_interest_cache.json"   # 공매도=격주 → 캐싱(매일 재fetch 무의미)
SI_TTL_DAYS = 3

# 단어형/모호 티커 — bare 심볼이 stopword·타맥락 매칭으로 뉴스속도 오염(검증 발견).
# 이 집합이거나 ≤3자면, --names 있을 때 '회사명만' 검색(티커 OR 안 함).
STOPWORD_TICKERS = {"NOW", "ALL", "ON", "IT", "ARE", "KEY", "ANY", "OUT", "NEW", "ONE",
                    "TWO", "BIG", "SEE", "HAS", "CEO", "AI", "GO", "SO", "AN", "OR",
                    "MU", "VST", "NRG", "CEG", "GEV", "ICE", "CME"}

__all__ = ["FOREIGN_SOURCES", "FTS_DB", "OUT_DIR", "SI_CACHE", "SI_TTL_DAYS",
           "STOPWORD_TICKERS", "kr_code", "load_kis_env", "utf8_stdout"]


def kr_code(tk: str) -> str | None:
    """KR 티커면 6자리 종목코드 반환, 아니면 None (투자자별 수급·공매도는 국내 전용)."""
    u = tk.upper()
    if u.endswith(".KS") or u.endswith(".KQ"):
        base = tk.split(".")[0]
        return base if base.isdigit() and len(base) <= 6 else None
    if tk.isdigit() and len(tk) == 6:
        return tk
    return None


def load_kis_env() -> None:
    """프로젝트 .env 를 os.environ 에 주입 (KIS_*·KRX_ID/PW 포함).

    flow 는 module_KIS 를 CLI 가 아니라 함수로 직접 부르므로 .env 로드를 여기서 한다.
    시크릿 단일 원본 = 이 리포 .env (옛 mvp 리포 링크 없음).
    """
    if os.environ.get("KIS_APP_KEY") and os.environ.get("KIS_APP_SECRET"):
        return
    for env_path in (REPO_ROOT / ".env",):
        if not env_path.exists():
            continue
        try:
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, _, v = line.partition("=")
                k, v = k.strip(), v.strip().strip('"').strip("'")
                if k and v and k not in os.environ:
                    os.environ[k] = v
        except Exception:
            pass
        break
