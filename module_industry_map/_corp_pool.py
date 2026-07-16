"""산업 키워드 → corp pool top-N (corp_descriptions.section_text grep).

iterative_research_topdown.py 와 같은 로직이지만 모듈 내부에 직접 격리.
다른 module_X / scripts 와 코드 결합 없음.
"""
from __future__ import annotations

import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import Optional


DB_PATH = Path(__file__).resolve().parent.parent / "data" / "corp_embeddings.db"


@dataclass
class CorpHit:
    ticker: str
    corp_name: str
    hit_count: int
    matched_seeds: list[str]


def _connect() -> sqlite3.Connection:
    if not DB_PATH.exists():
        raise FileNotFoundError(f"corp_embeddings.db 가 없습니다: {DB_PATH}")
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def grep_corp_pool(seeds: list[str], top_n: int = 30) -> list[CorpHit]:
    """thesis seeds → corp_descriptions.section_text 매칭 회사 top-N.

    ⚠️ 코퍼스는 KR 사업보고서(한국어) 전용 — 영문 시드는 원래 0히트가 정상.
    영문만 넘기면 아래 가드가 stderr 힌트를 낸다(US 사슬-홉은 scripts/chain_hop.py 사용).
    """
    if not seeds:
        return []
    if all(s.isascii() for s in seeds):
        import sys
        print(
            "[industry_map] 시드가 전부 영문입니다 — corp_embeddings.db 는 KR 사업보고서(한국어) 코퍼스라 "
            "영문 시드는 0히트가 정상입니다. KR은 한국어 시드로(예: '전력' '변압기'), "
            "US 가치사슬 발굴은 scripts/chain_hop.py 를 쓰세요.",
            file=sys.stderr,
        )

    with _connect() as conn:
        cur = conn.execute("SELECT ticker, corp_name, section_text FROM corp_descriptions")
        hits: list[CorpHit] = []
        for ticker, name, text in cur.fetchall():
            if not text:
                continue
            matched = [s for s in seeds if s in text]
            if matched:
                hits.append(CorpHit(
                    ticker=ticker,
                    corp_name=name or "",
                    hit_count=len(matched),
                    matched_seeds=matched,
                ))

    # hit_count 내림차순, ticker 오름차순
    hits.sort(key=lambda h: (-h.hit_count, h.ticker))
    return hits[:top_n]


_STOP_WORDS = {
    # generic 동사·접속사·연결어
    "있습니다", "당사는", "사업의", "주요", "있는", "있어", "있고", "있으며",
    "통해", "따라", "위한", "또한", "그리고", "다만", "한편",
    "현재", "기준", "관련", "포함", "다양한", "지속적", "다음과",
    "가능", "사용", "방법", "수준", "기간", "경우", "이상", "이하",
    # 너무 흔한 명사
    "회사", "당사", "고객", "시장", "제품", "사업", "기업", "분야",
    "산업", "기술", "글로벌", "국내", "해외", "전체", "구분", "단위",
    "대한", "위해", "통한", "기타", "전년", "지속", "이를", "이러한",
    "있을", "있도록", "다음", "이는", "동안", "따른", "통상",
    "운영", "관리", "수행", "수익", "매출", "발생", "제공",
    # 숫자·연도
    "2024년", "2025년", "2026년", "2024", "2025", "2026",
    "100", "1000", "300", "500", "200",
    "10", "11", "12", "20", "30", "50",
    "000", "1억", "2억", "3억",
    # 영문 generic
    "the", "and", "for", "with", "are", "was", "were",
}


def expand_seeds_from_pool(hits: list[CorpHit], top_k: int = 30) -> list[tuple[str, int]]:
    """corp pool 내 사업보고서 텍스트에서 자주 등장하는 키워드 추출.

    seed 외 specific term 자동 발견용 (HVDC, STATCOM, 765kV 등).
    Stop words 강화로 generic term 제외.
    """
    if not hits:
        return []
    import re
    from collections import Counter

    counter: Counter[str] = Counter()
    seed_set = set()
    for h in hits:
        seed_set.update(h.matched_seeds)

    with _connect() as conn:
        for h in hits:
            cur = conn.execute(
                "SELECT section_text FROM corp_descriptions WHERE ticker=?",
                (h.ticker,),
            )
            row = cur.fetchone()
            if not row or not row[0]:
                continue
            text = row[0]
            tokens = re.findall(r"[가-힣A-Za-z0-9]{2,12}", text)
            for t in tokens:
                if t in seed_set or len(t) < 2:
                    continue
                if t.lower() in _STOP_WORDS:
                    continue
                # 순수 숫자 제외
                if re.fullmatch(r"\d+", t):
                    continue
                # 1글자 한자 또는 단음절 의미없는 토큰 제외
                if len(t) <= 2 and re.fullmatch(r"[가-힣]+", t):
                    continue
                counter[t] += 1

    return [(w, c) for w, c in counter.most_common(top_k * 3) if w not in seed_set][:top_k]
