"""news_alert.db 에서 1Q 실적/IR 보도자료 발췌.

목적: 매출 비중·제품 정보가 사업보고서(2025/12) 시점 락인 corp_descriptions 와
     달리 1Q 실적 발표 보도자료에는 "옴리클로 신제품 견인", "북미 직판 매출 +X%"
     같은 제품별 매출 모멘텀이 들어 있다. 이를 회사명 + 실적 키워드로 grep.

본 모듈은 news_alert.db 만 의존. 다른 module_X import 0.
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "news_alert.db"


@dataclass
class IRArticle:
    title: str
    body: str
    source: str
    published_at: str
    url: str


# 1Q 실적·IR 키워드 (제목 grep) — V0.3 확장
_IR_KEYWORDS = [
    # 잠정실적·분기실적
    "1분기 실적", "1Q 실적", "1분기 영업", "1Q 영업",
    "분기 영업", "분기 실적", "분기 매출", "잠정실적", "잠정 실적",
    "영업이익", "영업익", "분기 보고서",
    # IR·기업설명회
    "IR 개최", "기업설명회", "실적 발표", "컨퍼런스콜",
    # 분석가 노트·증권사 의견
    " 분석]", " 분석 ", "목표가", "목표 주가", "기대치", "추정치",
    "추정", "전망", "리포트", "보고서",
    # 모멘텀
    "역대 최대", "분기 최대", "사상 최대",
]


# corp_name 변형 매핑 — 뉴스 헤드라인은 보통 짧은 통칭 사용
_NAME_VARIANTS = {
    "현대자동차": ["현대자동차", "현대차"],
    "기아": ["기아", "기아차", "Kia"],
    "삼성전자": ["삼성전자", "삼전"],
    "에스케이바이오팜": ["에스케이바이오팜", "SK바이오팜"],
    "에스케이바이오사이언스": ["SK바이오사이언스", "에스케이바이오사이언스"],
    "에스케이텔레콤": ["SK텔레콤", "에스케이텔레콤", "SKT"],
    "케이티": ["KT", "케이티"],
    "엘지유플러스": ["LG유플러스", "엘지유플러스", "LGU+"],
    "LG화학": ["LG화학", "엘지화학"],
    "케이비금융": ["KB금융", "케이비금융"],
    "신한지주": ["신한지주", "신한금융"],
    "하나금융지주": ["하나금융지주", "하나금융"],
    "한국항공우주": ["한국항공우주", "KAI"],
}


def _connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"news_alert.db 가 없습니다: {DB_PATH}")
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def find_q1_ir_articles(
    corp_name: str,
    *,
    days: int = 60,
    min_body_chars: int = 100,
    limit: int = 15,
) -> list[IRArticle]:
    """{corp_name} + IR 키워드 매칭 기사 본문. 최신순.

    Args:
        corp_name: 회사명 (예: "셀트리온", "삼성바이오로직스")
        days: 최근 N일. 기본 60.
        min_body_chars: body 최소 길이. 분석가 노트 (200자 미만)도 잡도록 100 default.
        limit: 최대 개수. default 15.
    """
    if not corp_name:
        return []
    # 종목명 변형 — 뉴스 헤드라인은 보통 통칭 사용 (현대자동차 → 현대차)
    name_variants = set(_NAME_VARIANTS.get(corp_name, [corp_name]))
    name_variants.add(corp_name)
    name_variants.add(corp_name.replace(" ", ""))
    if "에스케이" in corp_name:
        name_variants.add(corp_name.replace("에스케이", "SK"))
    if corp_name.startswith("SK"):
        name_variants.add("에스케이" + corp_name[2:])
    # 짧은 회사명 (3자 이하) 은 false-positive 방지로 변형 제외
    name_variants = {n for n in name_variants if len(n) >= 3}

    name_clauses = " OR ".join("title LIKE ?" for _ in name_variants)
    name_params = [f"%{n}%" for n in name_variants]

    keyword_clauses = " OR ".join("title LIKE ?" for _ in _IR_KEYWORDS)
    keyword_params = [f"%{k}%" for k in _IR_KEYWORDS]

    # news_alert.db 스키마는 seen_news + article_contents 두 테이블.
    # title 매칭은 seen_news, body 는 article_contents.body
    sql = f"""
        SELECT s.title, COALESCE(c.body, ''), s.source,
               COALESCE(s.published_at, s.fetched_at), s.url
        FROM seen_news s
        LEFT JOIN article_contents c ON c.url = s.url
        WHERE ({name_clauses})
          AND ({keyword_clauses})
          AND COALESCE(s.published_at, s.fetched_at) >= date('now', ?)
          AND length(COALESCE(c.body, '')) >= ?
        ORDER BY COALESCE(s.published_at, s.fetched_at) DESC
        LIMIT ?
    """
    params = (
        list(name_params)
        + list(keyword_params)
        + [f"-{days} days", min_body_chars, limit]
    )

    try:
        with _connect() as conn:
            cur = conn.execute(sql, params)
            return [
                IRArticle(
                    title=r[0] or "",
                    body=r[1] or "",
                    source=r[2] or "",
                    published_at=r[3] or "",
                    url=r[4] or "",
                )
                for r in cur.fetchall()
            ]
    except sqlite3.OperationalError:
        # 스키마 변경 시 fallback (테이블/컬럼명 다른 경우)
        return []


def render_ir_summary(articles: list[IRArticle], max_chars: int = 3000) -> str:
    """IRArticle 리스트 → markdown 요약 (본문 일부 발췌)."""
    if not articles:
        return "_해당 기간 IR/실적 보도자료 없음._\n"
    out: list[str] = []
    total = 0
    for art in articles:
        snippet = art.body[:600]
        block = (
            f"### {art.published_at[:10]} [{art.source}] {art.title}\n"
            f"{snippet}{'…' if len(art.body) > 600 else ''}\n"
            f"[원문]({art.url})\n"
        )
        if total + len(block) > max_chars:
            break
        out.append(block)
        total += len(block)
    return "\n".join(out)
