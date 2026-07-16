"""산업 지도 모듈 (1번 프롬프트 / INDUSTRY_LANDSCAPE 자동화).

thesis 시드 키워드 → corp pool 자동 매핑 + 가치사슬 노드 cluster 자동 식별.
LLM 은 클러스터 라벨 부여 + ASCII 다이어그램 그리기에만 집중.

다른 module_X 와 결합도 0:
- 자체 corp_embeddings.db 직접 query (sqlite3 read-only)
- numpy + scipy(optional) 만 사용
- module_business / module_embedding / scripts/iterative_research 등 import 안 함

CLI:
    python -m module_industry_map "{seed1}" "{seed2}" --clusters 6
    python -m module_industry_map "{seed1}" "{seed2}" --top-n 30 --out llm_outputs/{thesis}/industry_map.md

Public API:
    extract(seeds, top_n=30, n_clusters=6) → dict
    render_markdown(extracted) → str
"""
from __future__ import annotations

from typing import Optional

from ._corp_pool import CorpHit, grep_corp_pool, expand_seeds_from_pool
from ._cluster import Cluster, cluster_tickers
from ._renderer import render_industry_map


__all__ = [
    "CorpHit",
    "Cluster",
    "extract",
    "render_markdown",
    "render_industry_map",
]


def extract(
    seeds: list[str],
    *,
    top_n: int = 30,
    n_clusters: int = 6,
    expand_top_k: int = 25,
) -> dict:
    """seeds → 산업 지도 데이터.

    Returns:
        {
            "seeds": list[str],
            "corp_pool": list[CorpHit],
            "expanded_keywords": list[tuple[str, int]],
            "clusters": list[Cluster],
        }
    """
    corp_pool = grep_corp_pool(seeds, top_n=top_n)
    expanded = expand_seeds_from_pool(corp_pool, top_k=expand_top_k) if corp_pool else []
    tickers = [h.ticker for h in corp_pool]
    clusters = cluster_tickers(tickers, n_clusters=n_clusters) if len(tickers) >= 2 else []
    return {
        "seeds": seeds,
        "corp_pool": corp_pool,
        "expanded_keywords": expanded,
        "clusters": clusters,
    }


def render_markdown(extracted: dict) -> str:
    return render_industry_map(
        seeds=extracted["seeds"],
        corp_pool=extracted["corp_pool"],
        clusters=extracted["clusters"],
        expanded_keywords=extracted["expanded_keywords"],
    )
