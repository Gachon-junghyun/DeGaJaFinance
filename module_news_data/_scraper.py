# -*- coding: utf-8 -*-
"""기사 본문 스크레이퍼 — URL → article_contents 본문 저장 (옛 news/scraper.py 포팅).

source별 CSS 셀렉터 → 실패 시 제네릭 추출. 이미 본문(status='ok') 있는 url 은 skip.
requests + BeautifulSoup(lxml). 저장은 _repository.
"""
from __future__ import annotations

import logging
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from . import _repository as db

log = logging.getLogger("news_data.scraper")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
}
SEC_EDGAR_HEADERS = {
    "User-Agent": "DeGaJa Research fivepeople201@gmail.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9",
    "Accept-Encoding": "gzip, deflate",
}
TIMEOUT = 15
MIN_BODY_LEN = 100

SOURCE_SELECTORS: dict[str, list[str]] = {
    "yonhap":       ["div.story-news.article", "article.story-news", "div[class*='article-txt']"],
    "hankyung":     ["div#articleBody", "div.article-body", "div[class*='article_body']"],
    "mk":           ["div#article_body", "div.news_cnt_detail_wrap", "div[itemprop='articleBody']"],
    "edaily":       ["div[itemprop='articleBody']", "div#articleBody", "div.article_body"],
    "mt":           ["div#textBody", "div.view_text", "div[class*='article']"],
    "heraldcorp":   ["div#articleText", "div.view-con", "article"],
    "chosun":       ["div.article-body", "section.article-body", "div[class*='article']"],
    "joongang":     ["div#article_body", "div.article_body_content", "div[class*='article']"],
    "donga":        ["div.article_txt", "div#content", "article"],
    "asiae":        ["div.article_con", "div[class*='article']", "article"],
    "sedaily":      ["div#article_view", "div.article_view", "div[class*='article']"],
    "bbc":          ["div[data-component='text-block']", "article", "div.story-body"],
    "cnbc":         ["div.ArticleBody-articleBody", "div[class*='article-body']", "article"],
    "marketwatch":  ["div.article__body", "div[class*='article-body']", "article"],
    "fxstreet":     ["div.fxs_article_content", "article", "div[class*='article']"],
    "nyt":          ["section[name='articleBody']", "div[class*='StoryBodyCompanion']", "article"],
    "google_kr":    [],
    "google_en":    [],
    "thediplomat":  ["div.td-post-content", "div.entry-content", "div[class*='post-content']", "div[class*='content']"],
    "scmp":         ["div.article-body", "div[data-qa='ArticleBody']", "article"],
    "upi":          ["article", "div.story-body", "div[class*='article']"],
    "foreignpolicy": ["article div[class*='content']"],   # 페이월: lead만
    "bloomberg":    [],   # 봇 차단 (RSS 헤드라인+요약만)
    "yahoo_finance": ["div.caas-body", "div[class*='caas-body']", "div[class*='article-body']", "article"],
    "seekingalpha":  ["div[data-test-id='content-container']", "div#a-body", "div[class*='article-body']", "article"],
    "sec_edgar":     ["div.formContent", "table.tableFile", "div#contentDiv", "div#main-content"],
    "prnewswire":    ["section.release-body", "div.release-body", "div[class*='release-body']", "article"],
}


def _extract_with_selectors(soup: BeautifulSoup, selectors: list[str]) -> str:
    for sel in selectors:
        try:
            tag = soup.select_one(sel)
            if tag:
                text = tag.get_text(separator="\n", strip=True)
                if len(text) >= MIN_BODY_LEN:
                    return text
        except Exception:
            continue
    return ""


def _extract_generic(soup: BeautifulSoup) -> str:
    for unwanted in soup.select("nav, header, footer, aside, script, style, .ad, [class*='ad-'], [id*='ad-']"):
        unwanted.decompose()
    for tag_name in ("article", "main", "div"):
        candidates = soup.find_all(tag_name)
        best = max((c.get_text(separator="\n", strip=True) for c in candidates), key=len, default="")
        if len(best) >= MIN_BODY_LEN:
            return best
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if len(p.get_text(strip=True)) > 30]
    return "\n".join(paragraphs)


def _clean_body(text: str) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def scrape_article(url: str, source: str = "") -> tuple[str, str]:
    headers = SEC_EDGAR_HEADERS if (source == "sec_edgar" or "sec.gov" in urlparse(url).netloc) else HEADERS
    try:
        resp = requests.get(url, headers=headers, timeout=TIMEOUT, allow_redirects=True)
        resp.raise_for_status()
        try:
            soup = BeautifulSoup(resp.content, "lxml")
        except Exception:
            soup = BeautifulSoup(resp.content, "html.parser")
        if not source:
            domain = urlparse(url).netloc
            for k in SOURCE_SELECTORS:
                if k in domain:
                    source = k
                    break
        body = _extract_with_selectors(soup, SOURCE_SELECTORS.get(source, []))
        if not body:
            body = _extract_generic(soup)
        body = _clean_body(body)
        if len(body) < MIN_BODY_LEN:
            return body, "short"
        return body, "ok"
    except requests.RequestException as e:
        log.warning(f"요청 실패 [{url[:60]}]: {e}")
        return "", "error"
    except Exception as e:
        log.warning(f"파싱 실패 [{url[:60]}]: {e}")
        return "", "error"


def scrape_batch(articles: list[dict], workers: int = 5, delay: float = 0.3) -> dict[str, int]:
    stats = {"ok": 0, "short": 0, "error": 0, "skip": 0}
    already_done: set[str] = db.get_scraped_urls({art["url"] for art in articles})

    def _job(art: dict) -> tuple[str, str, str]:
        if art["url"] in already_done:
            return art["url"], "", "skip"
        body, status = scrape_article(art["url"], art.get("source", ""))
        time.sleep(delay)
        return art["url"], body, status

    with ThreadPoolExecutor(max_workers=workers) as pool:
        futures = {pool.submit(_job, art): art for art in articles}
        for i, future in enumerate(as_completed(futures), 1):
            url, body, status = future.result()
            stats[status] = stats.get(status, 0) + 1
            if status != "skip":
                db.save_article_content(url, body, status)
            art = futures[future]
            log.info(f"[{i}/{len(articles)}] {status:5s} | {art.get('title', url)[:55]}")
    return stats
