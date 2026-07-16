# -*- coding: utf-8 -*-
"""수집 오케스트레이션 — RSS fetch → 중복제거 → 본문 스크랩 → FTS 증분색인 (옛 pipeline.py 포팅).

한 번 호출 = seen_news 헤드라인 + article_contents 본문 채우고, 이어서 FTS(US porter +
KR trigram) 증분 갱신까지. bat 루프(run_fetch_loop.bat)가 이 경로를 주기적으로 돈다.
텔레그램/시나리오 없음 — 순수 수집.
"""
from __future__ import annotations

import logging
import time
from typing import Dict, List

from . import _repository as db
from . import _rss_feeds as fetcher
from ._scraper import scrape_batch

log = logging.getLogger("news_data.fetch")

# 본문 스크랩 불가 source (페이월·봇차단·구글 리다이렉트) — fetch 직후 본문 풀이에서 제외.
NON_SCRAPABLE_SOURCES = {
    "google_kr", "google_en", "google_news_kr", "google_news_en", "bloomberg", "nyt",
}

_MODE_PARAMS = {
    "full":     (40, 0.15),
    "fast":     (20, 0.10),
    "veryfast": (10, 0.05),
}


def scrape_new_bodies(new_articles: List[Dict], workers: int = 5, delay: float = 0.4) -> Dict:
    """fetch 직후 — scrapable source 본문을 article_contents 에 저장 (신규분만)."""
    scrapable = [a for a in new_articles if a.get("source", "") not in NON_SCRAPABLE_SOURCES]
    if not scrapable:
        return {"ok": 0, "short": 0, "error": 0, "skip": 0}
    stats = scrape_batch(scrapable, workers=workers, delay=delay)
    log.info("body scrape - ok=%d short=%d error=%d skip=%d (of %d scrapable / %d new)",
             stats.get("ok", 0), stats.get("short", 0), stats.get("error", 0),
             stats.get("skip", 0), len(scrapable), len(new_articles))
    return stats


def fetch_and_store(mode: str = "full", scrape_bodies: bool = True) -> List[Dict]:
    """RSS fetch → seen_news 신규 저장 → 본문 스크랩. 신규 기사 목록 반환."""
    max_per_feed, delay = _MODE_PARAMS.get(mode, _MODE_PARAMS["full"])
    raw = fetcher.fetch_news(max_per_feed=max_per_feed, delay=delay)
    new_articles = db.filter_new_articles(raw)
    log.info("fetched mode=%s total=%d new=%d", mode, len(raw), len(new_articles))
    if scrape_bodies and new_articles:
        scrape_new_bodies(new_articles)
    return new_articles


def run_once(mode: str = "full", scrape_bodies: bool = True, update_fts: bool = True) -> Dict:
    """수집 1회 (헤드라인+본문) + 선택적 FTS 증분색인. bat 루프의 1틱."""
    started = time.time()
    db.init_db()
    new_articles = fetch_and_store(mode=mode, scrape_bodies=scrape_bodies)
    result = {"mode": mode, "fetched_new": len(new_articles)}
    if update_fts:
        from ._fts import build
        try:
            build(rebuild=False, kr=False)   # US porter 증분
            build(rebuild=False, kr=True)    # KR trigram 증분
            result["fts_updated"] = True
        except Exception as e:
            log.warning("FTS 증분 갱신 실패: %s", e)
            result["fts_updated"] = False
    result["elapsed_sec"] = round(time.time() - started, 2)
    return result


def cli_register(sub) -> None:
    p = sub.add_parser("fetch", help="RSS 수집(헤드라인+본문) + FTS 증분색인 1회")
    p.add_argument("mode", nargs="?", default="full", choices=["veryfast", "fast", "full"],
                   help="수집 깊이 (기본 full=피드당 40)")
    p.add_argument("--no-bodies", action="store_true", help="본문 스크랩 skip (헤드라인만)")
    p.add_argument("--no-fts", action="store_true", help="FTS 증분색인 skip")
    p.set_defaults(func=lambda a: _run_cli(a))


def _run_cli(a) -> None:
    from ._config import utf8_stdout
    utf8_stdout()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    res = run_once(mode=a.mode, scrape_bodies=not a.no_bodies, update_fts=not a.no_fts)
    print(f"DONE — new={res['fetched_new']} fts={res.get('fts_updated')} "
          f"elapsed={res['elapsed_sec']}s")
