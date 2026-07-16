"""corp pool + cluster + 자동 키워드 → markdown 산업 지도."""
from __future__ import annotations

from ._corp_pool import CorpHit
from ._cluster import Cluster


def render_industry_map(
    seeds: list[str],
    corp_pool: list[CorpHit],
    clusters: list[Cluster],
    expanded_keywords: list[tuple[str, int]],
) -> str:
    """전체 산업 지도 markdown.

    구성:
    1. 입력 시드
    2. corp pool top-N 표
    3. 자동 확장 키워드 top-K
    4. cluster 별 멤버 (가치사슬 노드 후보)
    5. LLM에 넘길 다음 행동 안내
    """
    parts: list[str] = []
    parts.append("# 산업 지도 (1번 프롬프트 산출 — INDUSTRY_LANDSCAPE)")
    parts.append(f"\n_시드 키워드: {', '.join(seeds)}_\n")

    parts.append("## 1. corp pool top-30 (section_text grep)\n")
    parts.append("| rank | ticker | hit | name | matched seeds |")
    parts.append("|---:|---|---:|---|---|")
    for i, h in enumerate(corp_pool[:30], 1):
        seeds_str = ", ".join(h.matched_seeds[:6])
        parts.append(f"| {i} | {h.ticker} | {h.hit_count} | {h.corp_name} | {seeds_str} |")
    parts.append("")

    if expanded_keywords:
        parts.append("## 2. 자동 확장 키워드 (corp 사업보고서 텍스트)\n")
        kw_str = ", ".join(f"`{w}`({c})" for w, c in expanded_keywords[:25])
        parts.append(kw_str)
        parts.append("")

    parts.append("## 3. 가치사슬 노드 후보 (cosine 클러스터)\n")
    parts.append(f"_총 {len(clusters)} 개 클러스터. 같은 클러스터 = 사업보고서 임베딩 유사 = 가치사슬 같은 노드 후보._\n")
    for i, c in enumerate(clusters, 1):
        parts.append(f"### Cluster #{i} ({len(c.members)}개 종목)")
        for tk, nm in c.members[:10]:
            parts.append(f"- {tk}  {nm}")
        if len(c.members) > 10:
            parts.append(f"- ... 외 {len(c.members) - 10}건")
        parts.append("")

    parts.append("## 4. 다음 행동 (LLM 합성 단계)\n")
    parts.append("위 클러스터 / corp pool / 자동 키워드를 가지고:")
    parts.append("- (a) 좌→우 가치사슬 ASCII 다이어그램 작성 (노드 5~8개로 압축)")
    parts.append("- (b) 각 클러스터 = 가치사슬의 어느 칸인지 라벨 부여 (LLM 판단)")
    parts.append("- (c) `module_scenario_scan` + `search_news_alert` 로 병목·정량 anchor 추가")
    parts.append("- (d) `module_business` 로 핵심 5종목 회사 단위 매출 분해")
    parts.append("")
    return "\n".join(parts)
