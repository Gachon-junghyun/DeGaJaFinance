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
    # ── 해외 대량 확장 (2026-07-19) — 아래 전 피드 라이브 검증(HTTP 200 + 최신 항목 확인) 후 등록.
    #    CNN RSS(2017년 정지)·Politico US·The Hill·Kitco·BLS·IMF 등은 죽어 있거나 봇차단이라 제외.
    # US 마켓/종합
    {"name": "WSJ Markets",        "url": "https://feeds.content.dowjones.io/public/rss/RSSMarketsMain",   "source": "wsj"},
    {"name": "WSJ Business",       "url": "https://feeds.content.dowjones.io/public/rss/WSJcomUSBusiness", "source": "wsj"},
    {"name": "WSJ World",          "url": "https://feeds.content.dowjones.io/public/rss/RSSWorldNews",     "source": "wsj"},
    {"name": "WSJ Economy",        "url": "https://feeds.content.dowjones.io/public/rss/socialeconomyfeed","source": "wsj"},
    {"name": "WSJ Tech",           "url": "https://feeds.content.dowjones.io/public/rss/RSSWSJD",          "source": "wsj"},
    {"name": "FT Home",            "url": "https://www.ft.com/rss/home",               "source": "ft"},
    {"name": "FT International",   "url": "https://www.ft.com/rss/home/international", "source": "ft"},
    {"name": "Fortune",            "url": "https://fortune.com/feed/",                 "source": "fortune"},
    {"name": "Forbes Business",    "url": "https://www.forbes.com/business/feed/",     "source": "forbes"},
    {"name": "Business Insider",   "url": "https://www.businessinsider.com/rss",       "source": "businessinsider"},
    {"name": "BI Markets",         "url": "https://markets.businessinsider.com/rss/news", "source": "businessinsider"},
    {"name": "Yahoo Finance All",  "url": "https://finance.yahoo.com/news/rssindex",   "source": "yahoo_finance"},
    {"name": "TheStreet",          "url": "https://www.thestreet.com/.rss/full/",      "source": "thestreet"},
    {"name": "Benzinga",           "url": "https://www.benzinga.com/feed",             "source": "benzinga"},
    {"name": "ZeroHedge",          "url": "https://feeds.feedburner.com/zerohedge/feed", "source": "zerohedge"},
    {"name": "Motley Fool",        "url": "https://www.fool.com/a/feeds/foolwatch?format=rss2&id=foolwatch&apikey=foolwatch-feed", "source": "fool"},
    {"name": "Axios",              "url": "https://api.axios.com/feed/",               "source": "axios"},
    {"name": "Semafor",            "url": "https://www.semafor.com/rss.xml",           "source": "semafor"},
    # Nasdaq 카테고리
    {"name": "Nasdaq Markets",     "url": "https://www.nasdaq.com/feed/rssoutbound?category=Markets",          "source": "nasdaq"},
    {"name": "Nasdaq Stocks",      "url": "https://www.nasdaq.com/feed/rssoutbound?category=Stocks",           "source": "nasdaq"},
    {"name": "Nasdaq Earnings",    "url": "https://www.nasdaq.com/feed/rssoutbound?category=Earnings",         "source": "nasdaq"},
    {"name": "Nasdaq Commodities", "url": "https://www.nasdaq.com/feed/rssoutbound?category=Commodities",      "source": "nasdaq"},
    {"name": "Nasdaq IPOs",        "url": "https://www.nasdaq.com/feed/rssoutbound?category=IPOs",             "source": "nasdaq"},
    {"name": "Nasdaq Crypto",      "url": "https://www.nasdaq.com/feed/rssoutbound?category=Cryptocurrencies", "source": "nasdaq"},
    {"name": "Nasdaq AI",          "url": "https://www.nasdaq.com/feed/rssoutbound?category=Artificial-Intelligence", "source": "nasdaq"},
    {"name": "Nasdaq Technology",  "url": "https://www.nasdaq.com/feed/rssoutbound?category=Technology",       "source": "nasdaq"},
    # Investing.com 카테고리
    {"name": "Investing News",        "url": "https://www.investing.com/rss/news.rss",    "source": "investing_en"},
    {"name": "Investing Stock",       "url": "https://www.investing.com/rss/news_25.rss", "source": "investing_en"},
    {"name": "Investing EconIndicators", "url": "https://www.investing.com/rss/news_95.rss", "source": "investing_en"},
    {"name": "Investing Forex",       "url": "https://www.investing.com/rss/news_1.rss",  "source": "investing_en"},
    {"name": "Investing Commodities", "url": "https://www.investing.com/rss/news_11.rss", "source": "investing_en"},
    {"name": "Investing Economy",     "url": "https://www.investing.com/rss/news_14.rss", "source": "investing_en"},
    # MarketWatch·CNBC 추가 카테고리
    {"name": "MarketWatch Bulletins",   "url": "https://www.marketwatch.com/rss/bulletins",         "source": "marketwatch"},
    {"name": "MarketWatch RTHeadlines", "url": "https://www.marketwatch.com/rss/realtimeheadlines", "source": "marketwatch"},
    {"name": "CNBC Top News",   "url": "https://www.cnbc.com/id/100003114/device/rss/rss.html", "source": "cnbc"},
    {"name": "CNBC Investing",  "url": "https://www.cnbc.com/id/15839069/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC Earnings",   "url": "https://www.cnbc.com/id/15839135/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC Technology", "url": "https://www.cnbc.com/id/19854910/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC World",      "url": "https://www.cnbc.com/id/100727362/device/rss/rss.html", "source": "cnbc"},
    {"name": "CNBC Asia",       "url": "https://www.cnbc.com/id/19832390/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC US News",    "url": "https://www.cnbc.com/id/15837362/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC Business",   "url": "https://www.cnbc.com/id/10001147/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC Energy",     "url": "https://www.cnbc.com/id/19836768/device/rss/rss.html",  "source": "cnbc"},
    {"name": "CNBC Health",     "url": "https://www.cnbc.com/id/10000108/device/rss/rss.html",  "source": "cnbc"},
    # 영국/유럽
    {"name": "Guardian Business",  "url": "https://www.theguardian.com/uk/business/rss",         "source": "guardian"},
    {"name": "Guardian Economics", "url": "https://www.theguardian.com/business/economics/rss",  "source": "guardian"},
    {"name": "Guardian World",     "url": "https://www.theguardian.com/world/rss",               "source": "guardian"},
    {"name": "Guardian Tech",      "url": "https://www.theguardian.com/uk/technology/rss",       "source": "guardian"},
    {"name": "Sky News Business",  "url": "https://feeds.skynews.com/feeds/rss/business.xml",    "source": "skynews"},
    {"name": "Sky News World",     "url": "https://feeds.skynews.com/feeds/rss/world.xml",       "source": "skynews"},
    {"name": "Independent Business","url": "https://www.independent.co.uk/news/business/rss",    "source": "independent"},
    {"name": "Economist Finance",  "url": "https://www.economist.com/finance-and-economics/rss.xml", "source": "economist"},
    {"name": "Economist Business", "url": "https://www.economist.com/business/rss.xml",          "source": "economist"},
    {"name": "DW Business",        "url": "https://rss.dw.com/rdf/rss-en-bus",                   "source": "dw"},
    {"name": "DW All",             "url": "https://rss.dw.com/rdf/rss-en-all",                   "source": "dw"},
    {"name": "France24 Business",  "url": "https://www.france24.com/en/business/rss",            "source": "france24"},
    {"name": "Euronews Business",  "url": "https://www.euronews.com/rss?level=vertical&name=business", "source": "euronews"},
    {"name": "Euronews All",       "url": "https://www.euronews.com/rss",                        "source": "euronews"},
    {"name": "Politico EU",        "url": "https://www.politico.eu/feed/",                       "source": "politico"},
    # 아시아/월드
    {"name": "Nikkei Asia",        "url": "https://asia.nikkei.com/rss/feed/nar",                "source": "nikkei"},
    {"name": "Japan Times",        "url": "https://www.japantimes.co.jp/feed/",                  "source": "japantimes"},
    {"name": "Al Jazeera",         "url": "https://www.aljazeera.com/xml/rss/all.xml",           "source": "aljazeera"},
    {"name": "CNA Business",       "url": "https://www.channelnewsasia.com/api/v1/rss-outbound-feed?_format=xml&category=6936", "source": "cna"},
    {"name": "Straits Times Biz",  "url": "https://www.straitstimes.com/news/business/rss.xml",  "source": "straitstimes"},
    {"name": "Times of India Biz", "url": "https://timesofindia.indiatimes.com/rssfeeds/1898055.cms", "source": "toi"},
    {"name": "EconomicTimes Markets", "url": "https://economictimes.indiatimes.com/markets/rssfeeds/1977021501.cms", "source": "economictimes"},
    # 중앙은행/공식 발표
    {"name": "Fed Press All",      "url": "https://www.federalreserve.gov/feeds/press_all.xml",  "source": "federalreserve"},
    {"name": "Fed Speeches",       "url": "https://www.federalreserve.gov/feeds/speeches.xml",   "source": "federalreserve"},
    {"name": "ECB Press",          "url": "https://www.ecb.europa.eu/rss/press.html",            "source": "ecb"},
    {"name": "BOE News",           "url": "https://www.bankofengland.co.uk/rss/news",            "source": "boe"},
    # 원자재/크립토/물류
    {"name": "OilPrice",           "url": "https://oilprice.com/rss/main",                       "source": "oilprice"},
    {"name": "Mining.com",         "url": "https://www.mining.com/feed/",                        "source": "mining"},
    {"name": "CoinDesk",           "url": "https://www.coindesk.com/arc/outboundfeeds/rss/",     "source": "coindesk"},
    {"name": "Cointelegraph",      "url": "https://cointelegraph.com/rss",                       "source": "cointelegraph"},
    {"name": "CryptoSlate",        "url": "https://cryptoslate.com/feed/",                       "source": "cryptoslate"},
    {"name": "Hellenic Shipping",  "url": "https://www.hellenicshippingnews.com/feed/",          "source": "hellenicshipping"},
    # 테크 (시장영향)
    {"name": "TechCrunch",         "url": "https://techcrunch.com/feed/",                        "source": "techcrunch"},
    {"name": "The Verge",          "url": "https://www.theverge.com/rss/index.xml",              "source": "theverge"},
    {"name": "Ars Technica",       "url": "https://feeds.arstechnica.com/arstechnica/index",     "source": "arstechnica"},
    {"name": "VentureBeat",        "url": "https://venturebeat.com/feed/",                       "source": "venturebeat"},
    {"name": "Tom's Hardware",     "url": "https://www.tomshardware.com/feeds/all",              "source": "tomshardware"},
    {"name": "EE Times",           "url": "https://www.eetimes.com/feed/",                       "source": "eetimes"},
    {"name": "The Register",       "url": "https://www.theregister.com/headlines.atom",          "source": "theregister"},
    {"name": "Wired Business",     "url": "https://www.wired.com/feed/category/business/latest/rss", "source": "wired"},
    {"name": "MIT Tech Review",    "url": "https://www.technologyreview.com/feed/",              "source": "mittr"},
    # 보도자료
    {"name": "GlobeNewswire Public Cos", "url": "https://www.globenewswire.com/RssFeed/orgclass/1/feedTitle/GlobeNewswire%20-%20News%20about%20Public%20Companies", "source": "globenewswire"},
    # Google News EN 토픽 (Reuters·AP·Caixin 은 직접 RSS 가 없어 site: 검색으로 우회)
    {"name": "Google EN Reuters biz",   "url": "https://news.google.com/rss/search?q=site:reuters.com+business&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN AP biz",        "url": "https://news.google.com/rss/search?q=site:apnews.com+business&hl=en&gl=US&ceid=US:en",  "source": "google_en"},
    {"name": "Google EN Caixin",        "url": "https://news.google.com/rss/search?q=site:caixinglobal.com&hl=en&gl=US&ceid=US:en",     "source": "google_en"},
    {"name": "Google EN stock market",  "url": "https://news.google.com/rss/search?q=stock+market+today&hl=en&gl=US&ceid=US:en",        "source": "google_en"},
    {"name": "Google EN earnings",      "url": "https://news.google.com/rss/search?q=quarterly+earnings+results&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN semiconductor", "url": "https://news.google.com/rss/search?q=semiconductor+chips+TSMC+Nvidia&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN oil OPEC",      "url": "https://news.google.com/rss/search?q=oil+prices+OPEC&hl=en&gl=US&ceid=US:en",           "source": "google_en"},
    {"name": "Google EN AI",            "url": "https://news.google.com/rss/search?q=artificial+intelligence+AI+companies&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN treasury yields", "url": "https://news.google.com/rss/search?q=Treasury+yields+bond+market&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN China economy", "url": "https://news.google.com/rss/search?q=China+economy+stimulus&hl=en&gl=US&ceid=US:en",    "source": "google_en"},
    {"name": "Google EN BOJ yen",       "url": "https://news.google.com/rss/search?q=Bank+of+Japan+yen&hl=en&gl=US&ceid=US:en",         "source": "google_en"},
    {"name": "Google EN ECB euro",      "url": "https://news.google.com/rss/search?q=ECB+eurozone+economy&hl=en&gl=US&ceid=US:en",      "source": "google_en"},
    {"name": "Google EN crypto",        "url": "https://news.google.com/rss/search?q=bitcoin+cryptocurrency&hl=en&gl=US&ceid=US:en",    "source": "google_en"},
    {"name": "Google EN Korea",         "url": "https://news.google.com/rss/search?q=South+Korea+economy+Samsung&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    {"name": "Google EN M&A",           "url": "https://news.google.com/rss/search?q=merger+acquisition+deal&hl=en&gl=US&ceid=US:en",   "source": "google_en"},
    {"name": "Google EN IPO",           "url": "https://news.google.com/rss/search?q=IPO+listing+shares&hl=en&gl=US&ceid=US:en",        "source": "google_en"},
    {"name": "Google EN sanctions",     "url": "https://news.google.com/rss/search?q=sanctions+export+controls&hl=en&gl=US&ceid=US:en", "source": "google_en"},
    # Yahoo Finance 추가 티커
    {"name": "Yahoo Finance AVGO",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AVGO&region=US&lang=en-US",   "source": "yahoo_finance"},
    {"name": "Yahoo Finance AMD",   "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=AMD&region=US&lang=en-US",    "source": "yahoo_finance"},
    {"name": "Yahoo Finance MU",    "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=MU&region=US&lang=en-US",     "source": "yahoo_finance"},
    {"name": "Yahoo Finance TSM",   "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=TSM&region=US&lang=en-US",    "source": "yahoo_finance"},
    {"name": "Yahoo Finance INTC",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=INTC&region=US&lang=en-US",   "source": "yahoo_finance"},
    {"name": "Yahoo Finance QCOM",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=QCOM&region=US&lang=en-US",   "source": "yahoo_finance"},
    {"name": "Yahoo Finance JPM",   "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=JPM&region=US&lang=en-US",    "source": "yahoo_finance"},
    {"name": "Yahoo Finance XOM",   "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=XOM&region=US&lang=en-US",    "source": "yahoo_finance"},
    {"name": "Yahoo Finance LLY",   "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=LLY&region=US&lang=en-US",    "source": "yahoo_finance"},
    {"name": "Yahoo Finance PLTR",  "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=PLTR&region=US&lang=en-US",   "source": "yahoo_finance"},
    {"name": "Yahoo Finance BA",    "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=BA&region=US&lang=en-US",     "source": "yahoo_finance"},
    {"name": "Yahoo Finance SPX",   "url": "https://feeds.finance.yahoo.com/rss/2.0/headline?s=%5EGSPC&region=US&lang=en-US", "source": "yahoo_finance"},
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
