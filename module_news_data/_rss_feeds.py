# -*- coding: utf-8 -*-
"""RSS 뉴스 수집 — 국내/해외 피드에서 헤드라인+요약 수집 (옛 news/fetcher.py 포팅).

feedparser + requests. SEC EDGAR 는 Fair Access 정책상 식별자 헤더 필요.
새 소스 추가 시 RSS_FEEDS 에 등록하고, 해외면 _config.FOREIGN_SOURCES 에도 넣는다.
"""
from __future__ import annotations

import logging
import time
from typing import Dict, List

import feedparser
import requests

log = logging.getLogger("news_data.rss")

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}
# SEC EDGAR Fair Access: 명시적 식별자(이메일) 없으면 403.
SEC_EDGAR_HEADERS = {
    "User-Agent": "DeGaJa Research fivepeople201@gmail.com",
    "Accept": "application/atom+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
}

RSS_FEEDS: List[Dict] = [
    {"name": "연합 경제",       "url": "https://www.yna.co.kr/rss/economy.xml",          "source": "yonhap"},
    {"name": "연합 국제",       "url": "https://www.yna.co.kr/rss/international.xml",    "source": "yonhap"},
    {"name": "연합 산업",       "url": "https://www.yna.co.kr/rss/industry.xml",         "source": "yonhap"},
    {"name": "연합 전체",       "url": "https://www.yna.co.kr/rss/news.xml",             "source": "yonhap"},
    {"name": "한경 경제",       "url": "https://www.hankyung.com/feed/economy",          "source": "hankyung"},
    {"name": "한경 증권",       "url": "https://www.hankyung.com/feed/finance",          "source": "hankyung"},
    {"name": "한경 국제",       "url": "https://www.hankyung.com/feed/international",    "source": "hankyung"},
    {"name": "한경 IT",         "url": "https://www.hankyung.com/feed/it",               "source": "hankyung"},
    {"name": "매경 경제",       "url": "https://www.mk.co.kr/rss/30100041/",             "source": "mk"},
    {"name": "매경 증권",       "url": "https://www.mk.co.kr/rss/30200030/",             "source": "mk"},
    {"name": "매경 국제",       "url": "https://www.mk.co.kr/rss/30300018/",             "source": "mk"},
    {"name": "이데일리 경제",   "url": "https://www.edaily.co.kr/rss/economy.xml",       "source": "edaily"},
    {"name": "이데일리 증권",   "url": "https://www.edaily.co.kr/rss/stock.xml",         "source": "edaily"},
    {"name": "머니투데이 전체", "url": "https://rss.mt.co.kr/mt_news.xml",               "source": "mt"},
    {"name": "헤럴드 금융",     "url": "https://biz.heraldcorp.com/rss/finance.xml",     "source": "heraldcorp"},
    {"name": "헤럴드 경제",     "url": "https://biz.heraldcorp.com/rss/economy.xml",     "source": "heraldcorp"},
    {"name": "조선비즈",        "url": "https://biz.chosun.com/arc/outboundfeeds/rss/?outputType=xml", "source": "chosun"},
    {"name": "중앙 경제",       "url": "https://rss.joins.com/joins_economy_list.xml",   "source": "joongang"},
    {"name": "동아 경제",       "url": "https://rss.donga.com/economy.xml",              "source": "donga"},
    {"name": "아시아경제",      "url": "https://www.asiae.co.kr/rss/all.htm",            "source": "asiae"},
    {"name": "서울경제 금융",   "url": "https://www.sedaily.com/RSS/Finance/",           "source": "sedaily"},
    {"name": "서울경제 경제",   "url": "https://www.sedaily.com/RSS/Economy/",           "source": "sedaily"},
    {"name": "BBC Business",    "url": "http://feeds.bbci.co.uk/news/business/rss.xml",  "source": "bbc"},
    {"name": "BBC World",       "url": "http://feeds.bbci.co.uk/news/world/rss.xml",     "source": "bbc"},
    {"name": "CNBC Economy",    "url": "https://www.cnbc.com/id/20910258/device/rss/rss.html", "source": "cnbc"},
    {"name": "CNBC Finance",    "url": "https://www.cnbc.com/id/10000664/device/rss/rss.html", "source": "cnbc"},
    {"name": "MarketWatch Top", "url": "https://www.marketwatch.com/rss/topstories",     "source": "marketwatch"},
    {"name": "FXStreet News",   "url": "https://www.fxstreet.com/rss/news",              "source": "fxstreet"},
    {"name": "NYT Business",    "url": "https://rss.nytimes.com/services/xml/rss/nyt/Business.xml", "source": "nyt"},
    {"name": "NYT Economy",     "url": "https://rss.nytimes.com/services/xml/rss/nyt/Economy.xml",  "source": "nyt"},
    {"name": "Google KR 경제",     "url": "https://news.google.com/rss/search?q=%EA%B2%BD%EC%A0%9C&hl=ko&gl=KR&ceid=KR:ko", "source": "google_kr"},
    {"name": "Google KR 주식증시", "url": "https://news.google.com/rss/search?q=%EC%A3%BC%EC%8B%9D+%EC%A6%9D%EC%8B%9C&hl=ko&gl=KR&ceid=KR:ko", "source": "google_kr"},
    {"name": "Google KR 금리연준", "url": "https://news.google.com/rss/search?q=%EA%B8%88%EB%A6%AC+%EC%97%B0%EC%A4%80&hl=ko&gl=KR&ceid=KR:ko", "source": "google_kr"},
    {"name": "Google KR 환율달러", "url": "https://news.google.com/rss/search?q=%ED%99%98%EC%9C%A8+%EB%8B%AC%EB%9F%AC&hl=ko&gl=KR&ceid=KR:ko", "source": "google_kr"},
    {"name": "Google KR 반도체",   "url": "https://news.google.com/rss/search?q=%EB%B0%98%EB%8F%84%EC%B2%B4+%EC%82%BC%EC%84%B1&hl=ko&gl=KR&ceid=KR:ko", "source": "google_kr"},
    {"name": "Google KR 무역관세", "url": "https://news.google.com/rss/search?q=%EB%AC%B4%EC%97%AD+%EA%B4%80%EC%84%B8&hl=ko&gl=KR&ceid=KR:ko", "source": "google_kr"},
    {"name": "Google EN economy",     "url": "https://news.google.com/rss/search?q=economy+stocks&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN Fed inflation", "url": "https://news.google.com/rss/search?q=Federal+Reserve+inflation&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN trade tariff",  "url": "https://news.google.com/rss/search?q=trade+tariff+US+China&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Bloomberg Markets",   "url": "https://feeds.bloomberg.com/markets/news.rss",   "source": "bloomberg"},
    {"name": "Bloomberg Politics",  "url": "https://feeds.bloomberg.com/politics/news.rss",  "source": "bloomberg"},
    {"name": "Bloomberg Economics", "url": "https://feeds.bloomberg.com/economics/news.rss", "source": "bloomberg"},
    {"name": "Foreign Policy",      "url": "https://foreignpolicy.com/feed/",                "source": "foreignpolicy"},
    {"name": "The Diplomat",        "url": "https://thediplomat.com/feed/",                  "source": "thediplomat"},
    {"name": "SCMP China",          "url": "https://www.scmp.com/rss/91/feed",               "source": "scmp"},
    {"name": "SCMP News",           "url": "https://www.scmp.com/rss/2/feed",                "source": "scmp"},
    {"name": "UPI",                 "url": "https://www.upi.com/rss/news.rss",               "source": "upi"},
    {"name": "Yahoo Finance AAPL",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AAPL&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Yahoo Finance NVDA",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=NVDA&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Yahoo Finance MSFT",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=MSFT&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Yahoo Finance TSLA",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=TSLA&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Yahoo Finance META",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=META&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Yahoo Finance GOOGL", "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=GOOGL&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Yahoo Finance AMZN",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AMZN&region=US&lang=en-US", "source": "yahoo_finance"},
    {"name": "Seeking Alpha Market Currents", "url": "https://seekingalpha.com/market_currents.xml", "source": "seekingalpha"},
    {"name": "Seeking Alpha Feed",            "url": "https://seekingalpha.com/feed.xml",            "source": "seekingalpha"},
    {"name": "SEC EDGAR 8-K current", "url": "https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=8-K&company=&dateb=&owner=include&count=40&output=atom", "source": "sec_edgar"},
    {"name": "PRNewswire News Releases", "url": "https://www.prnewswire.com/rss/news-releases-list.rss", "source": "prnewswire"},
    {"name": "MarketWatch MarketPulse",  "url": "https://www.marketwatch.com/rss/marketpulse",          "source": "marketwatch"},
]


def _fetch_feed(feed: Dict, max_items: int) -> List[Dict]:
    headers = SEC_EDGAR_HEADERS if feed.get("source") == "sec_edgar" else HEADERS
    try:
        resp = requests.get(feed["url"], headers=headers, timeout=12)
        resp.raise_for_status()
        parsed = feedparser.parse(resp.content)
        articles = []
        for entry in parsed.entries[:max_items]:
            title = (entry.get("title") or "").strip()
            url = (entry.get("link") or "").strip()
            pub = entry.get("published", entry.get("updated", ""))
            summary = (entry.get("summary") or "").strip()
            if title and url:
                articles.append({
                    "title": title, "url": url,
                    "source": feed.get("source", ""), "feed_name": feed.get("name", ""),
                    "published": pub, "summary": summary[:200] if summary else "",
                })
        return articles
    except Exception as e:
        log.warning(f"피드 실패 [{feed['name']}]: {e}")
        return []


def fetch_news(max_per_feed: int = 20, delay: float = 0.1) -> List[Dict]:
    all_articles: List[Dict] = []
    for i, feed in enumerate(RSS_FEEDS, 1):
        all_articles.extend(_fetch_feed(feed, max_per_feed))
        if delay > 0:
            time.sleep(delay)
    log.info(f"수집 완료: 총 {len(all_articles)}개 | 피드 {len(RSS_FEEDS)}개 | 피드당 최대 {max_per_feed}개")
    return all_articles


def filter_by_keywords(articles: List[Dict], keywords: List[str]) -> List[Dict]:
    if not keywords:
        return []
    kw_lower = [k.lower() for k in keywords]
    matched = []
    for art in articles:
        title_lower = art.get("title", "").lower()
        for kw in kw_lower:
            if kw in title_lower:
                matched.append({**art, "matched_keyword": kw})
                break
    return matched
