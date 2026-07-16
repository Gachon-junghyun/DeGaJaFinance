"""한국 주식 밸류에이션·수급 데이터 수집 모듈.

빠른 사용:
    from module_valuation import fetch_naver_snapshot, build_peer_table

    snap = fetch_naver_snapshot("267260")              # HD현대일렉트릭
    print(snap.per_fwd, snap.target_price)

    df = build_peer_table("267260", ["298040", "010120"])
    print(df)

CLI:
    python -m module_valuation 267260 --peers 298040,010120

데이터 소스: 네이버 금융 종목 페이지 (무인증).
KRX는 2026 인증 의무화로 pykrx 무인증 사용 불가 — 네이버가 가장 안정적인 무인증 채널.
"""
from ._naver_fetch import NaverSnapshot, fetch_naver_snapshot, to_dict
from ._peer_compare import build_peer_table, add_peer_avg, render_markdown

__all__ = [
    "NaverSnapshot",
    "fetch_naver_snapshot",
    "to_dict",
    "build_peer_table",
    "add_peer_avg",
    "render_markdown",
]
