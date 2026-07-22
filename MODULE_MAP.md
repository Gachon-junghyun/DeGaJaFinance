# MODULE_MAP — 모듈 지도 (중복 방지 원장)

> 이 리포의 모든 모듈을 한 곳에 엮는다. 모듈을 **쓰기 전엔 트리거로 찾고**, **만들기 전엔
> 여기서 같은 기능이 있는지 확인**한다. "소유"는 그 기능/상수의 단일 원본(P1), "재사용"은
> 다른 모듈에서 import 해 쓰는 것 — 이 두 열이 겹치지 않으면 중복이 없는 것이다.
> 방법론(원칙·규약)은 [`CLAUDE.md`](CLAUDE.md).

---

## 한눈에

| 모듈 | 한 줄 | 트리거(언제) |
|---|---|---|
| [module_KIS](#module_kis) | 한국투자증권 Open API — 시세·수급·잔고·주문 | KR/US 시세·OHLCV, 투자자별 수급, 계좌 조회, (휴먼)주문 |
| [module_news_data](#module_news_data) | 뉴스 **수집**·검색·색인·커버리지·발굴 | 뉴스 수집 루프, 찾기, 커버리지 점검, 사각 발굴, 테마 나이, 사슬-홉 |
| [module_chart](#module_chart) | 텍스트(ASCII) 차트 + 결정론 구조판정 | 차트 모양·OBV·다이버전스·턴 판정을 브리프에 임베드 |
| [module_flow](#module_flow) | 수급·기대감 흐름 → 🟢/🟡/🔴 | "지금 돈·관심이 들어오나" 방아쇠 판정 |
| [module_disclosure](#module_disclosure) | DART 공시 조회·분류 + 사업보고서 본문 | KR 종목 단기 catalyst(수주·자사주·지분·실적), 사업보고서 |
| [산업 데스크 모듈 10](#산업-데스크-모듈) | industry_us/kr 프로토콜이 호출하는 분석 모듈 | 매크로·밸류·공시·사업·산업지도·워치리스트 등 |
| [module_report_tags](#module_report_tags) | REPORT/ 태그추출 + 인수인계 원장(증분) | 데스크 재검색 방지 — 리포트 태그를 인수받기 |
| [module_paper_book](#module_paper_book) | 데스크 리포트 → 모의투자(paper) 장부 | 리포트를 읽어 사이징·체결시뮬·시가평가·저널 (paper_desk 프로토콜 엔진) |
| [module_epistemics](#module_epistemics) | 베이지안 충돌평가·민감도 학습·verify·registry_audit | 신호 모순 해소, 종목 민감도 축적, 코드↔맵 감사 |
| [module_inflection](#module_inflection) | 가격 변곡점 ↔ 뉴스 정렬 + 과거 전례 검색 | "이런 말 나올 때 이렇게 흘렀다", 변곡 주변 기사, 유사국면 |
| [module_order_desk](#module_order_desk) | KIS 주문 데스크(Tkinter GUI) — 스택형 휴먼 주문 | 시세 보며 주문을 스택에 쌓아 카드마다 [체결], 포폴·인기·흐름·만약에 |
| [scripts/](#스크립트-데스크-호출) | 데스크가 `python scripts/X.py`로 호출하는 단일파일 도구 9 | 수급·섹터로테이션·촉매·숏리스트·스크리너 |

> 층위 설계(큰축→모듈→기능 + 인수인계)는 [`pipeline/`](pipeline/README.md).

**의존 그래프(재사용 = 중복 없음의 증거 · 옛 리포 런타임 링크 0):**
```
module_flow ─ news velocity ─▶ module_news_data (_config: FOREIGN_SOURCES·FTS 경로·utf8)
            └ ⑦ 투자자수급 ──▶ module_KIS (_investor)
module_disclosure ─ 사업보고서 corp_code ─▶ 자체 _corp_codes (corp_codes.csv)
module_fundamentals_us ──▶ module_disclosure_us   ·   module_timefolio ──▶ module_webctl
scripts/sector_flow ──▶ scripts/flow_read(shim) ──▶ module_flow
데이터·DB·유니버스 ──▶ 이 리포 data/ (로컬 소유). 시크릿 ──▶ 이 리포 .env.
```

> **이름 주의**: 옛 프로토콜은 `module_kis`·`module_text_chart`를 호출하지만 이 리포에선
> `module_KIS`·`module_chart`로 이관됨. 프로토콜을 옮길 때 이 두 이름을 치환한다.
> `module_scenario_scan`은 은퇴(scenario 계통)라 미포팅 — 호출부는 제거 대상.

---

## module_KIS
한국투자증권 Open API. 조회는 자유, **주문은 휴먼 트리거 전용**(기본 드라이런, `--execute`는 사람만).

- **트리거**: 국내/미국 시세·밸류에이션·기간별 OHLCV·투자자별 수급·계좌잔고가 필요할 때. yfinance 추정보다 안정적인 인증 소스.
- **CLI**:
  ```bash
  python -m module_KIS 005930                     # 시세 스냅샷(밸류에이션 포함)
  python -m module_KIS 005930 --ohlcv D --count 120
  python -m module_KIS 005930 --investor 20       # 외국인/기관/개인 순매수
  python -m module_KIS --balance                  # 국내 잔고(읽기전용)
  ```
- **공개 API**: `fetch_quote · fetch_ohlcv · fetch_investor_trend/net_summary · fetch_balance · fetch_us_quote · place_order`(휴먼) …
- **소유**: KIS 인증(`_auth`)·시세/수급/주문 전 계열. KIS/KRX 시크릿 `.env` 폴백 로직.
- **재사용됨**: `module_flow._investor` 가 `_investor.fetch_investor_trend` 를 부른다.
- **환경변수**: `KIS_APP_KEY/SECRET` (계좌·주문은 `KIS_ACCOUNT_NO` 추가). 토큰 캐시는 이 리포 루트 `.kis_token_cache.json`.

## module_order_desk
KIS 주문 데스크 — Tkinter 스택형 주문 GUI. 주문을 '스택'에 카드로 쌓아 **카드마다 [체결]로 사람이 하나씩 발사**(자동매매 아님, 확인 다이얼로그 1회). 옛 mvp `kis_desk.py`를 이관.

- **트리거**: 시세·잔고를 보며 국내/미국 주문을 손으로 쌓아 발사할 때. 포트폴리오 도넛·인기종목·흐름(수급)·'만약에'(반사실 결정 추적)를 한 창에서.
- **실행**:
  ```bash
  python -m module_order_desk        # GUI 실행 (cwd=리포 루트)
  run_kis_desk.bat                   # 더블클릭(윈도우)
  ```
- **기능 파일**: `_desk`(GUI·주문카드·포폴/인기/흐름/만약에 창) · `_decisions`(반사실 결정 추적) · `_stack`(계획 스택 저장/로드). 공개 API `KisDesk · main`.
- **재사용**: 시세/잔고/주문은 `module_KIS`(복제 0). 흐름창은 `python -m module_flow` 서브프로세스 → `out/flow/<date>.json` 읽기.
- **소유**: 없음(순수 GUI 오케스트레이션). 산출은 `out/order_desk/`(계획 `kis_stack.json`·결정 `kis_decisions.json`), 오류로그 `kis_desk_error.log`.
- **안전(P5·규약)**: 기본 드라이런 미리보기 카드, `execute=True`는 [체결] 버튼+확인 1회로만. 스케줄러 자동발사 없음. `KIS_ENV=prod`면 상단 붉은 실전 배너.
- **환경변수**: `KIS_APP_KEY/SECRET` + `KIS_ACCOUNT_NO`(리포 루트 `.env`), 선택 `USDKRW_FALLBACK`.

## module_news_data
뉴스 **수집 + 소비**. 이 리포가 수집을 소유·구동(`run_fetch_loop.bat`). 기능 하나 = `_파일` 하나.

- **소유**: `_config` 가 **FOREIGN_SOURCES 집합·DB 경로·utf8 헬퍼의 단일 원본**(옛 리포에선 4파일 복붙 → 여기 1곳).
  수집(`_rss_feeds`·`_scraper`·`_repository`·`_fetch`)·색인(`_fts`)·검색·발굴 전부.
  ⚠ **피드 추가는 두 곳이 짝**: `_rss_feeds.RSS_FEEDS` + (해외면) `_config.FOREIGN_SOURCES`.
  후자를 빠뜨리면 영문 소스가 KR 로 태깅돼 국내 스코프로 새고, 한국어 학습 분류기가 영문을 판정한다.
  ⚠ **피드는 조용히 죽는다**: 2026-07-18 실측 — 한경 4피드 403(일평균 158.8건→0, 무경고),
  이데일리·헤럴드·중앙 7피드는 **HTTP 200 + entries=0** 이라 예외가 안 나 `log.warning` 조차 안 찍혔다
  (DB 기사 0건). 현재 76피드/33소스 전부 entries>0 확인. 소스별 물량이 갑자기 0이면 뉴스가 없는 게
  아니라 **피드가 죽은 것**부터 의심할 것.
  `_timeaxis` 가 **시간축(published_at→UTC)의 단일 원본** — 시계열을 재는 모든 기능은 여기서 import.
  `_tokenize` 가 **토큰화의 단일 원본**(한글 조사절단+영문, 형태소분석기 0) — 단어를 세는 기능은 여기서 import.
  `_universe` 가 **상장사 언급 판정**(KR=kr_all.csv 3글자+, US=`_chain_hop.load_universe` 재사용).
- **재사용됨**: `module_flow` 가 `_config` 에서 FOREIGN_SOURCES·FTS 경로·utf8 을 import.
- **데이터(로컬 소유)**: `data/news_alert.db`·`news_fts.db`/`news_fts_kr.db`·`us_universe/*`·`news_synonyms*.json`.
  `data/news_vectors.db` 는 **클라이언트 소유 파생물**(articles+vectors+커서) — 서버 DB 스키마는 안 건드린다.
- ⚠️ **역할 분리**: 서버 PC = 수집·검색 서빙(저사양, **torch 없음**). 클라이언트 = GPU 임베딩·클러스터·브리핑.
  그래서 `_embed`/`_cluster` 는 **torch·sklearn 을 모듈 최상단에서 import 하면 안 된다** — 서버가
  `__main__.build_parser` 로 이 파일들을 import 하므로 기동이 깨진다. 무거운 import 는 함수 안에서만.
  같은 이유로 `embed`·`cluster` 는 `DB_READ_CMDS` 에서 제외(원격 실행 금지, `_export.pull` 로 제목만 받아옴).
  실측(RTX 3080): 2,082건/초 — 전량 206,224건 백필 **2분 27초**, 하루치 2초. float16 저장 463MB(1년 ~2.4GB).
- ⚠️ **단위는 기사가 아니라 사건**(`cluster`). 같은 일을 27번 내는 게 기본이고(재배포 포함),
  단어 단위로 보면 한 사건이 `한화오션`·`잠수함`·`캐나다`·`TKMS` 로 쪼개진다. 실측 하루 3,782건
  → 사건 512개(2매체+). **중요도 = 몇 개 매체가 다뤘나**(편집자들이 독립적으로 내린 판정을 빌림).
  ⚠ `burst`(단어 z급등)는 "새로운 것"만 잰다 — 7/07 코스피 8%급락·서킷브레이커 날 `코스피`는
  평소 1.3배라 후보에도 못 들었다(`영업이익` 23.6배가 1위). `cluster` 는 같은 날 [39건/8매체]로 잡는다.
  둘은 대체재가 아니라 **다른 축**(새로움 vs 큼)이다.
- ⚠️ **뉴스풀의 62%가 종합지**라 `classify` 없이는 폭우·송파구·호날두가 반도체를 이긴다.
  라벨은 URL 섹션(`mt.co.kr/politics/`)에서 **공짜**(23,508건, 사람 손 0) → 섹션이 URL 에 없는
  신문(yonhap·asiae·hankyung = 국내 62%)에 일반화. 실측 홀드아웃 95.1% · **LOSO 85~88%**(실사용 기준).
  **폐기된 방법**: '제목에 상장사명이 있나'(`_universe`) — 정밀하나 경제기사 재현율 **10.6%**.
  7/07 최대 사건 "코스피 급락에 매도 사이드카"의 상장사 관련도가 7% 였다(제목에 회사명이 없다).
  트랜스포머를 안 쓴 이유: 라벨이 같으니 상한도 같고, NB 는 `explain()` 으로 판정 근거어를 보여준다(P4).
- ⚠️ **파이프라인**: `embed sync`(하루2초) → `cluster`(7초) → `classify` → `brief` → `thread`(7일 17초).
  실측 하루 3,782건 → 사건 512 → 시장 394 → 머리61/몸통143/꼬리190 → **44k 토큰**(제목전부 146k 대비 3배 압축).
  꼬리는 **자르지 않고** 분모+무작위표본으로 준다 — 매체수는 중요도의 대리지표지 진실이 아니다.
- ⚠️ **`brief`(사진) 와 `thread`(필름)도 대체재가 아니다.** `thread` 는 일별 사건을 주간 윈도우로
  재연결해 매체수 곡선(BUILDING/FADING/REIGNITED/ENDED)을 준다. 실측(7/11~17): 한은 금리인상
  사가가 **7/11 [14건/2매체] 꼬리 → 7/16 [101건/8매체] 발표**로 5일 활주로가 곡선에 미리 보였다
  — 하루 뷰에선 첫날이 꼬리라 안 보인다. 이런 전조형(2매체 시작→5매체+ 정점)이 한 윈도우에 12개.
  연결임계 0.40 은 실측 타협점(0.30=사가 토막, 0.50='오늘의 운세'까지 스레드). 윈도우 끝이
  휴일이면 FADING 과대(물량 편향) — per-day 분모 먼저 읽는다. 태그는 곡선 모양이지 판정이 아니다(P4).
- ⚠️ **`brief --lede` 는 기본 OFF (본문이 못 쓸 상태)**: asiae·sedaily 는 본문 **앞** 400자가 100%
  페이지 가구('함께 보면 좋은 기사' 목록 등)라, 리드의 22%가 그 사건과 무관한 기사였다(실측).
  서킷브레이커 사건 근거로 "푸드나무 유상증자"가 붙는 식 — LLM 이 사건을 오독한다. 가구 제거
  규칙을 넣었더니 멀쩡한 리드를 떨어뜨려 27%로 악화. **스크래퍼 수정 전까지 방향(호재/악재)은
  브리핑이 말하지 않는다**(빈칸이 거짓보다 낫다).

| 서브커맨드 | 트리거 | CLI |
|---|---|---|
| `fetch` | RSS 수집(헤드라인+본문)+FTS 증분 1회 (bat 루프의 1틱) | `python -m module_news_data fetch full` |
| `search` | 키워드로 기사 다 보기(본문까지 `--field any`) | `... search 변압기 HVDC --days 14` |
| `fts` | 정밀·관련도순(BM25)·동의어·구문 검색 + 색인 | `... fts search "rate cut" --days 14 --scope foreign --syn` / `... fts update` |
| `coverage` | "내 검색어가 풀의 몇 %를 보나"(분모 포함) | `... coverage nuclear --days 30 --scope foreign` |
| `blindspot` | 못 본 풀 랜덤샘플 + 토큰0 신흥어 발굴 | `... blindspot --days 7 --scope foreign` |
| `burst` | **고정 검색어 0** — 그날 평소보다 튄 단어 + 근거(①z급등 ②신생어) | `... burst --date 2026-07-07 --scope domestic --json` |
| `export` | 제목 벌크 반출(증분) — 서버(수집)→클라(GPU) 동기화. 기계 소비 전용 | `... export --count --since <커서>` / `... export --since <커서>` |
| `embed` | 제목 → 문장벡터(ko-sroberta·GPU). **클라 전용**·증분 따라잡기 | `... embed sync` · `... embed status` |
| `cluster` | 하루 기사 → **사건**(같은 일 27건→1줄, 매체수=중요도). **클라 전용** | `... cluster --date 2026-07-07 --scope domestic --json` |
| `classify` | 제목 → 시장/비시장(NB·의존성0·URL 라벨 자가학습). 근거어 감사 | `... classify --eval` · `... classify --words` |
| `brief` | 하루 → **계층 브리핑**(머리5매체+/몸통3+/꼬리표본+분모). **클라 전용** | `... brief --date 2026-07-07 --scope domestic --json` |
| `thread` | 여러 날 사건 **궤적**(스레드) — BUILDING/FADING/REIGNITED/ENDED + 일별 매체수 곡선. **클라 전용** | `... thread --days 7 --scope domestic` |

| `theme-age` | 테마 나이·가속(FRESH vs ECHO) | `... theme-age humanoid "Strait of Hormuz" --scope foreign` |
| `drift` | 기준시각(리포트 완주) 이후 킬스위치 텀 버스트 — 리포트 스테일 감지 | `... drift --since 2026-07-17T18:00:00 --scope foreign` |
| `chain-hop` | 제목 미명명 + 본문 근접 공동언급 수혜후보(US) | `... chain-hop "data center" power --days 14` |

- **수집 루프**: 서버 PC 는 [`Server/`](Server/README.md) — `Server/run_fetch_loop.bat`(수집: fetch full + fts update 영/한, 매 INTERVAL 기본 3600s) + `Server/run_news_api.bat`(검색 API). 루트 `run_fetch_loop.bat` 는 Server 위임 shim. 로그 `data/fetch_loop.log`.
- **API 검색 transport**: 클라이언트가 `DEGAJA_NEWS_API=http://<서버IP>:8787` 를 켜면 `fts search/count` 가 로컬 DB 대신 서버에서 끌어온다(헤더에 ` ·via API`). 쿼리 단일 원본 = `_fts.query_fts`(서버 `Server/news_api.py` 가 재구현 않고 재사용, P1). `_api_client`(urllib) ↔ `news_api`(http.server), **stdlib만**. 비면 로컬 폴백.
- ⚠️ **원격 허용목록의 단일 원본 = `__main__.DB_READ_CMDS`** — `Server/news_api.py` 가 그걸 import 한다.
  예전엔 서버에 복붙본이 있어, 클라에 서브커맨드를 추가해도 서버만 모른 채 "원격 실행 불가"로 거부됐다.
  새 조회 서브커맨드는 `DB_READ_CMDS` 한 줄만 추가(서버 코드 수정 0). 단, **서버는 이 리포 코드를 돌리므로
  git pull + API 재시작이 필요**하다. 명령별 타임아웃은 `__main__.REMOTE_TIMEOUT`(export=600s).
- ⚠️ KR FTS는 trigram — 2글자 한글(실적·수주)은 0 반환(부재 아님). 3글자+ 대체어로.
- 수집/색인은 append-only(`INSERT OR IGNORE`) — 중복 재수집 무해.
- ⚠️ **시계열은 `fetched_at` 로 비닝하지 않는다** — 수집이 밀렸다 몰리면(밤 공백→아침 catch-up)
  사흘치가 한 시각에 뭉쳐 **수집 공백이 가짜 뉴스 스파이크로 둔갑**한다(실측: 761건 틱이 발행일로는
  7/16 509 + 7/17 246 로 갈림). 축은 `_timeaxis`(published_at→UTC). 전수 파싱률 100%(205,866/205,866).
- ⚠️ **일별 비닝은 `_timeaxis.market_day(raw, source)`** — `utc_day` 아님. UTC 일자로 세면 한국 아침
  뉴스가 전날 칸에 쌓인다(실측 국내 22.0% → market_day 로 0.0%). 소스 국적 판정은 `origin_tag` 재사용:
  KR→KST(+9), EN→UTC(BBC·SCMP·bloomberg 섞여 단일 현지시각 없음). `utc_day/utc_hour` 는 절대축 원시 함수.
- ⚠️ published_at 은 **2026-05-01 이후만 존재**(그 이전 35,021건 빈값) — `PUBLISHED_AT_SINCE`.

## module_chart
가격을 LLM이 읽는 ASCII 캔들 차트로 렌더 + 사람이 눈대중하던 구조신호를 결정론 판정(CHART_READ).

- **트리거**: 차트 모양(OBV 누적/분배·다이버전스·MA정렬·볼린저·턴 판정)을 에이전트 브리프에 임베드할 때.
  메타데이터로 퉁치지 말고 `--read` 블록을 그대로 박는다.
- **CLI**:
  ```bash
  python -m module_chart 005930.KS            # 차트 파일 저장(out은 module/output)
  python -m module_chart AAPL --read          # CHART_READ 블록만(브리프 임베드용)
  ```
- **공개 API**: `save_text_chart · plot_combined_chart · generate_metadata · generate_chart_read · fetch_ohlcv`
- **소유**: OHLCV→ASCII 렌더·지표·구조판정. self-contained(yfinance만).

## module_flow
가치(4Phase)·차트가 못 보는 '돈·관심의 흐름'을 결정론으로 → 🟢가속 / 🟡중립 / 🔴분산.
4Phase가 바닥이면 이건 방아쇠.

- **트리거**: "지금 이 종목에 돈·내러티브가 들어오나"를 물을 때. 후보 스윕 뒤 방아쇠 판정.
- **CLI**:
  ```bash
  python -m module_flow NVDA GEV VRT MU --bench SPY --json
  python -m module_flow 005930.KS --names 삼성전자      # KR = ⑦수급·⑧공매도 자동
  python -m module_flow NVDA --positioning              # ⑤공매도%float+⑥옵션(느림, 최종후보만)
  ```
- **축**: ①뉴스속도 ②③④OBV·RS·거래량서지 ⑦투자자수급(KR) ⑧공매도잔고(KR) ⑤⑥포지셔닝(US, 선택).
- **소유**: 흐름 합성(`_synthesize.flow_tag`)·가격흐름 수식·포지셔닝.
- **재사용함**: 뉴스속도는 `module_news_data._config`(FTS·소스집합), ⑦수급은 `module_KIS._investor`. 이 모듈은 이 둘을 **다시 구현하지 않는다.**
- ⚠️ 🟢가속이라도 진입은 하드스탑 필수(기대감=꼭지위험). 4Phase '바닥'과 교차.

## module_disclosure
DART(OpenDART) 공시 조회·카테고리 분류 + 사업보고서 본문. 100% DART API, self-contained(`corp_codes.csv`).

- **트리거**: KR 종목의 단기 catalyst(수주·자사주·자본변동·지분변동·실적)를 공시 원문으로 볼 때. 사업보고서 "II. 사업의 내용".
- **CLI**:
  ```bash
  python -m module_disclosure 034020 --days 60                # 공시 스냅샷(카테고리 분류)
  python -m module_disclosure 034020 --days 60 --guidance 13.3 # 수주 진척률 자동계산
  python -m module_disclosure 034020 --category contract --json
  python -m module_disclosure 005930 --business-report        # 최근 사업보고서 본문(옛 module_business 흡수)
  python -m module_disclosure 000720 --guarantees --days 365  # 채무보증(PF 우발채무) 금액·총잔액
  ```
- **공개 API**: `fetch_disclosures · fetch_disclosure_detail · resolve_corp_code · categorize · parse_contract/treasury/capital/guarantee · summarize_contracts · fetch_business_report · fetch_toc/fetch_toc_section`
- **소유**: DART list.json·document 조회, corp_code 매핑, 공시 카테고리 분류·계약 상세파싱.
- **환경변수**: `DART_API_KEY`(.env). `corp_codes.csv`는 7일 TTL 자동 갱신(`refresh_corp_codes`).
- 사업보고서 본문 fetch(`--business-report`)는 **뷰어 프레임셋을 우회해 실본문을 읽는다**(2026-07-20 수정).
  `dsaf001/main.do` 는 목차·네비 껍데기라 예전엔 "잠시만 기다려주세요·전체문서·다운로드" 같은 UI 문자열을
  본문이라고 반환했다. 지금은 main.do 의 JS 목차트리에서 절별 좌표(dcmNo/eleId/offset/length)를 파싱해
  `report/viewer.do` 로 실본문을 받는다. 목차가 없는 단일문서 공시는 `viewDoc(...)` 리터럴로 폴백.
  `--section` 상당은 `fetch_business_section(rcept_no, section="재무제표")` 로 다른 절도 가능.
- `--guarantees` = **PF 우발채무**. 시행사(PFV·조합) 차입에 시공사가 선 보증은 재무제표 부채에 안 잡히고
  "타인에대한채무보증결정" 공시로만 드러난다 — 건설사 리스크의 본체. 총잔액은 공시 시점 누적치라 **합산하지 않는다**
  (실측: 현대건설 17.4조=자기자본 172%, 대우건설 13.5조=388%).

---

## 산업 데스크 모듈
industry_us/kr 프로토콜이 호출하는 분석 모듈. 전부 기능별 `_파일` + `__main__` CLI. 옛 이름 유지(크로스임포트·프로토콜 호출 호환).

| 모듈 | 트리거 | CLI(예) | 소유/의존 |
|---|---|---|---|
| `scripts/report_lint.py` | 데스크 산출물 **규칙 린터**(형식 검사) | `python -X utf8 scripts/report_lint.py "llm_outputs/{date}/**/*.md"` | — |
| `module_macro_us` | US 매크로 레짐(FRED **19개** — 금리·물가·달러 + **신용/유동성**) | `python -m module_macro_us --series hy_oas,nfci` | FRED_API_KEY |
| `module_valuation` | KR 밸류에이션 스냅샷·목표가·peer 비교(수동 `--peers`) | `python -m module_valuation 005930 --peers 000660` | DART/KRX |
| `module_industry_map` | 임베딩 클러스터로 산업 지도·밸류체인 | `python -m module_industry_map` | data/corp_embeddings.db (직접 sqlite) |
| `module_business` | KR 사업모델(매출표·제품)+IR 발췌 | `python -m module_business 005930` | data/corp_embeddings.db + news_alert.db |
| `module_business_us` | US 사업모델(EDGAR/yf) | `python -m module_business_us AAPL` | 자립(yf/EDGAR) |
| `module_disclosure_us` | US 공시(SEC EDGAR) | `python -m module_disclosure_us AAPL` | ticker_cik 캐시(자체) |
| `module_fundamentals_us` | US 펀더멘털(매출·이익엔진 + **추정치 모멘텀**) | `python -m module_fundamentals_us AAPL` | ▶module_disclosure_us |
| `module_fundamentals_kr` | **KR 재무제표 + 수익의 질**(발생액·미청구공사) | `python -m module_fundamentals_kr 000720` | DART 전체재무제표 ▶module_disclosure |
| `module_math_check` | 리포트 수치 산술 검증 | `python -m module_math_check ...` | 자립(stdlib) |
| `module_watchlist` | thesis 단위 워치리스트 DB | `python -m module_watchlist init` | data/watchlist.db |
| `module_publish` | 산출물 렌더·발행 헬퍼 | `python -m module_publish ...` | 자립 |

- **재사용(중복0)**: `module_fundamentals_us`→`module_disclosure_us`, `module_fundamentals_kr`→`module_disclosure`(corp_code 해석).
  corp_embeddings.db 는 industry_map·business 가 직접 sqlite 로 읽음(로컬 data/).
- `module_business` 의 IR 발췌는 **news_alert.db 가 없으면 그 부분만 비운다**(2026-07-20 수정). 그 DB 는 서버 소유(P6)라
  클라이언트에 없는 게 정상인데, 예전엔 `FileNotFoundError` 로 **전 종목이 죽었다**. 사업모델 본체(corp_embeddings.db)는
  로컬이라 그대로 나온다.

### 수익의 질(Block B2) — KR
`module_fundamentals_kr` 이 DART `fnlttSinglAcntAll`(전체재무제표)로 **발생액·미청구공사·운전자본**을 낸다.
계정 식별은 **account_id(IFRS 표준태그) 우선, 한글명 폴백** — 한글명은 회사마다 제각각이라("매출액" vs "수익(매출액)",
IS 가 비고 CIS 만 있는 회사) 이름 매칭은 조용히 빗나간다.
수주산업(건설·조선)에선 **미청구공사(계약자산)/매출과 그 YoY 방향**이 1번 지표 — 진행률로 인식했지만 청구 못 한 매출이고,
매출보다 빨리 늘면 공기지연·정산분쟁·원가초과 이연이 고인 것이다.
US 대응(`module_fundamentals_us`)과 **미러 복제가 아니다** — 데이터 소스 자체가 달라(yfinance/SEC XBRL vs DART) P3 의 시장인자로 흡수 불가.

## module_paper_book
데스크 리포트(BET_SHEET·ACTION_TICKETS·평결)를 읽어 **모의투자(paper) 장부**를 굴린다. `paper_desk` 프로토콜의 결정론 엔진 — 판단(무엇을 살지)은 프로토콜(에이전트)이, 이 모듈은 '얼마나·어떻게'의 기계만 제공한다(P4).

- **트리거**: 산업/기업 데스크 산출물을 읽어 리스크 사이징·체결 시뮬레이션·시가평가·결정 저널을 남길 때. 실제 주문 아님(모의).
- **기능 지도**: `_book`(SQLite 장부 단일원본: 현금슬리브·포지션·체결원장·자기자본 스냅샷 + `equity_krw` 총자산 계산 단일원본) · `_intake`(리포트→실행가능 후보; ▶module_report_tags 유니버스·태그 재사용) · `_risk`(리스크기반 사이징+집중도가드) · `_mark`(시가평가; ▶module_KIS(KR)/yfinance(US)) · `_journal`(결정저널+트랙레코드) · **`_allocate`(랩어카운트 배분규율: 섹터 만다트·드리프트·포트폴리오 베타·리밸런스 계획)**.
- **CLI**:
  ```bash
  python -m module_paper_book init --capital-krw 10000000 --capital-usd 5000
  python -m module_paper_book intake                 # REPORT/ → 프레시니스별 후보 원장
  python -m module_paper_book size AVGO --price 393 --stop 360 --core
  python -m module_paper_book fill --ticker AVGO --side buy --qty 3 --price 393 --commit  # 기본 드라이런
  python -m module_paper_book status | mark | snapshot | journal | track
  python -m module_paper_book pulse                              # 라이브 진단: "지금 나락?"(현재가·당일등락+시장맥락)
  python -m module_paper_book mirror --from-json holdings.json   # 실 KIS 보유 → paper book(이미보유)
  python -m module_paper_book stage  --from-json intents.json    # 추천 → KIS 주문 데스크 스택(계획만)
  # ── 랩어카운트(만다트) 계열 — wrap_account 프로토콜 엔진 ──
  python -m module_paper_book mandate --market us --band 5 --set '{"Information Technology":25,"Energy":12}'
  python -m module_paper_book mandate --map TSM="Information Technology" --target-beta 1.0 --beta-band 0.15
  python -m module_paper_book drift [--period 1y --no-beta --json]   # 섹터 괴리(pp)+밴드+책 베타
  python -m module_paper_book rebalance [--to target|band]           # 트림/애드 계획(기본 드라이런)
  python -m module_paper_book rebalance --commit                     # 계획을 모의장부에 반영(사람만)
  ```
- **랩어카운트(`_allocate`)**: 섹터 **목표비중(만다트)** 을 걸고 장부를 그 만다트로 굴린다 — 목표 대비 괴리(pp)·밴드 이탈,
  포트폴리오 베타(일별수익률 회귀, KR `^KS11` / US `SPY`), 밴드 복원 트림/애드 계획. 만다트 테이블(`mandate`·`mandate_meta`·
  `sector_override`)은 **`paper_book.db` 안에** 산다(두 번째 DB 금지). 섹터 출처 = `data/kr_universe/kr_all.csv:sector` ·
  `data/us_universe/us_top300.csv:gics_sector`, 유니버스 밖(ADR·비top300)은 `(unmapped)` 로 두고 `--map` 으로 사람이 박는다(추측 0).
  **판단 경계(P4)**: 트림 대상은 규칙(스탑거리 최소=약한 것 우선)으로 결정론이지만, **언더웨이트 섹터에 넣을 새 종목은 고르지 않는다** —
  `NEEDS_CANDIDATE` + 금액만 내놓고 선정은 프로토콜([`wrap_account`](pipeline/protocols/wrap_account.md))에 넘긴다.
  산출 `out/paper_book/WRAP_REBALANCE_{date}.json`. ⚠ 현금은 통화별 슬리브라 **원화 현금으로 US 종목을 못 산다**(FX 전환 프리미티브 없음) —
  막힌 레그는 슬리브 잔액과 함께 드러낸다. ⚠ KIS 키가 없는 PC 는 KR 마크가 통째로 실패하므로 `_mark.price_move`(yfinance) 로 메운다.
- **소유**: 모의 장부 상태·체결 회계·리스크 사이징·트랙레코드 + **미러(_mirror: 실계좌↔paper↔주문스택 동기화)** + **랩 만다트·섹터 드리프트·회귀 베타(_allocate — 리포 유일의 베타 구현체. `module_flow` 의 RS 는 수익률 차, `module_fundamentals_us` 의 beta 는 yfinance `.info` 값이라 둘 다 대체 불가)**. **재사용(중복0)**: 리포트 태그/유니버스는 `module_report_tags`, 시세는 `module_KIS`/yfinance(`_mark`), 집중도 상한(MAX_POS_PCT·MAX_THEME_PCT)은 `_risk`, 총자산은 `_book.equity_krw`, **주문 스택은 `module_order_desk.stack`, 학습된 민감도는 `module_epistemics`** — 다시 구현하지 않는다.
- **미러링(`_mirror`)**: `mirror`=실 KIS 보유를 '이미 보유'로 시드(현금 슬리브 셋). `stage`=추천을 `out/order_desk/kis_stack.json`(주문 데스크 스택)에 intent 카드로 적재 — **사람이 [체결]로 발사, 자동 아님**. `learned_sensitivity/record_sensitivity`=epistemics 원장 조회/되먹임. 프로토콜 [`미러링`](pipeline/protocols/미러링.md).
- **데이터**: `data/paper_book.db`(`PAPER_BOOK_DB_PATH` 로 이동가능). **안전**: 체결은 기본 드라이런, `--commit` 사람 명시 전용. 스케줄러 자동발사 없음.
- **환경변수**: (KR 마크에) `KIS_APP_KEY/SECRET`. US 마크는 yfinance(무인증).

## module_report_tags
REPORT/ 폴더의 데스크 산출물(.md)에서 태그(종목·섹터·평결·테마·날짜)를 추출해 **인수인계 원장**을 증분 갱신. 매번 재검색·재리포트하는 대신 다운스트림이 이 원장을 읽는다.

- **트리거**: 데스크가 리포트를 쓴 뒤 / 다른 데스크가 "이 종목 이미 누가 다뤘나"를 알고 싶을 때.
- **CLI**:
  ```bash
  python -m module_report_tags update          # REPORT/ 증분 스캔 → HANDOFF.md + _tags.json
  python -m module_report_tags show            # 인수인계 원장 출력
  python -m module_report_tags ticker GEV      # 그 종목 다룬 리포트 역검색
  ```
- **증분(인수인계 핵심)**: 파일 mtime 추적 → 새/변경 리포트만 재추출, 나머진 이전 결과 승계.
- **재사용**: 티커 검증에 `data/us_universe·kr_universe`, 모호티커 필터는 `module_news_data._chain_hop.AMBIGUOUS_TICKERS` 재사용(중복0).
- **폴더**: `DEGAJA_REPORT_DIR`(기본 `REPORT/`). 데스크 산출물이 여기 쌓이면 태그가 잡힌다.

## module_epistemics
신호가 모순일 때 손퉁하지 않고 **구조화**한다. 베이지안 충돌평가 + 종목별 민감도 학습 + verifier 플러그인 + 코드↔맵 감사 (HANDOFF_SPEC §4.8).

- **트리거**: 신호 충돌(OBV vs 실투자자 등) 해소 / 종목 민감도 축적 / 리팩토링 진척 감사.
- **CLI**:
  ```bash
  python -m module_epistemics audit                                   # 코드↔맵 정합성 + 커버리지 추세
  python -m module_epistemics adjudicate 000660 --thesis "…" --signals '[{"axis":..,"dir":"+","lr":2.1}]'
  python -m module_epistemics sensitivity 000660 --add "HBM ASP" --dir +강 --conf 0.8 --event "…"
  python -m module_epistemics verify --seed
  ```
- **닫힌 루프**: 민감도 원장(`epistemics/sensitivity/{id}`) → adjudicate가 학습된 신뢰도 자동 조회(conf 생략 시) → 지배축(argmax LR×신뢰도) → catalyst 후 가격반응 관측 → 민감도 갱신 ↺.
- **registry_audit**: `module_*`·`scripts/` 실행표면 스캔 → MODULE_MAP 대조 → OK/UNDOCUMENTED/STALE 분류 + `REGISTRY_AUDIT_LOG.jsonl` 커버리지 추세(진척 계량기). 실측 커버리지 100% (29 capability).
- **재사용**: 티커 정규화 자체(`_config.canon`), 사후검증 패턴은 alert-postmortem 계열과 동형.

## module_inflection
가격 **변곡점**을 표준편차로 뽑고 그 주변 뉴스를 붙여 "이런 말이 나올 때 이렇게 흘렀다"를 관측으로 만든다 + 과거 유사국면 검색. 판단은 안 한다(P4) — 관측·분포·전례만 낸다. 실측 노트 [`lab/INFLECTION_NEWS_KR.md`](lab/INFLECTION_NEWS_KR.md).

- **트리거**: "이 급등락에 어떤 재료가 있었나", "이런 헤드라인 뒤엔 보통 어떻게 됐나", "지금과 닮은 과거 국면".
- **CLI**:
  ```bash
  python -m module_inflection build --top 200        # 파생DB 재생성(가격·언급·변곡·지문)
  python -m module_inflection stats                  # 리드래그·리프트·순열2종·날짜클러스터
  python -m module_inflection phrases                # 말의 종류별 이후 초과수익
  python -m module_inflection events --kind shock_down --min-arts 3
  python -m module_inflection analog --text "원전 수주"   # 과거 전례 + 그 후 실제 수익
  ```
- **소유**: 변곡 판정(shock=|r|≥Zσ · pivot=추세 부호전환) · 리드래그/리프트/순열 검정 · 제목유형 사전 · 이벤트 지문(제목벡터 평균) 검색.
- **재사용(중복0)**: 벡터·제목·market_day 는 `news_vectors.db`(module_news_data 소유) **읽기만**, 임베딩 모델명은 `_embed.MODEL_NAME`, 2글자 사명 제외 규칙은 `_universe.KR_MIN_NAME_LEN`, 경로·utf8 은 `module_news_data._config`, 유니버스는 `data/kr_universe/kr_all.csv`. 지표 산식은 만들지 않는다(`module_chart._indicators`).
- **데이터**: `data/inflection.db` = **클라이언트 소유 파생물**(px·universe·mentions·events). 언제든 지우고 `build` 로 재생성. 산출 `out/inflection/*.json`, 노트 `lab/`.
- ⚠ **P6**: `analog --text` 만 GPU(문장 인코딩) — lazy import. 나머지는 CPU. 이 모듈은 클라 전용이라 `DB_READ_CMDS` 에 넣지 않는다.
- ⚠️ **pivot 은 미래 10일을 쓰는 사후 라벨러**다(순환논리). 진입신호로 쓰면 백테스트가 완벽하고 실전이 0 이 된다. 출력에 경고가 박혀 있다.
- ⚠️ **날짜로 묶기 전 t값을 믿지 않는다** — 실측: 급락충격 233건 중 65건이 2026-06-08 하루. pooled 로 세면 "급락 뒤 5일 +4.78pp, t=+6.55"인데, 하루=한 표본으로 접으면 **−1.03%±1.39(t=−0.74)로 효과가 사라진다**. `_stats.day_clustered()` 가 기본 보고 단위인 이유.
- ⚠️ **조건부 수익은 기준선을 뺀 초과로만 읽는다** — 실측 창(2026-05~07)의 무조건부 5일이 −1.72%라, 안 빼면 모든 결론이 "시장이 빠졌다"가 된다.
- ⚠️ **변곡의 50.3%만 제목 근거가 있다** — 나머지는 뉴스가 없는 게 아니라 시장 전체 사건이라 제목에 회사명이 없다(`_universe` 의 경제기사 재현율 10.6% 가 변곡 축에서 재현됨).

## 브라우저·집행 모듈
| 모듈 | 트리거 | 안전장치 |
|---|---|---|
| `module_webctl` | CDP(9222) 브라우저 제어 | 조회/제어만 |
| `module_timefolio` | 타임폴리오 미러 자동매매 | **이중게이트**: `--execute` + `TIMEFOLIO_EXECUTE=1` 둘 다 있어야 제출, 아니면 드라이런. ▶module_webctl |

## 스크립트 (데스크 호출)
데스크가 `python scripts/X.py`로 호출하는 단일파일 도구. 데이터는 전부 로컬 `data/` 참조로 수정됨.

| 스크립트 | 트리거 | 의존 |
|---|---|---|
| `us_flow.py` | US 수급(CFTC COT + FINRA 공매도) | 자립(공개피드) |
| `sector_flow.py` | 유니버스 섹터 로테이션 정량 스윕 | `flow_read`(shim→module_flow), data/us_universe·kr_universe |
| `flow_read.py` | **shim** — `import flow_read` 호환(엔진=module_flow) | module_flow 재export |
| `drift_watch.py` | 완주 후 킬스위치 버스트 감시(리포트 mtime·anti-signal 추출·렌더) | `module_news_data drift`(DB 질의 위임 → API 라우팅). **DB 직접 열지 않음(P6)** |
| `theme_age`·`chain_hop`·`news_blindspot` | (이미 module_news_data 서브커맨드) | — |
| `cycle_exposure.py` | 사이클 노출 GAP | data/cycles, module_KIS |
| `catalyst_calendar.py` | 촉매 날짜 캘린더 | data/catalysts |
| `action_bracket.py` | 진입 브래킷(스탑/타겟) | data/cycles·catalysts, module_KIS |
| `us_live_shortlist.py`·`kr_live_shortlist.py` | 장중 라이브 숏리스트 | data/us_universe·kr_universe |
| `us_setup_screener.py` | US 셋업 스크리너(top300 3바구니) | `yf_snapshot`, data/us_universe (⚠️indicator_alerts.db=옛 alert_bot, 미포팅→graceful) |
| `yf_snapshot.py` | 일봉 OHLCV → 스칼라 지표(last·rsi14·sma50/200·px_vs_sma200). 스크리너 전용 어댑터 | `module_chart._indicators`(RSI·MA 단일 원본 — 산식 재구현 안 함) |
| `_repo_path.py` | **부트스트랩** — `python scripts/foo.py` 가 module_* 를 import 하게 sys.path 에 리포 루트 삽입 | 없음(스크립트 dir 이 sys.path[0]) |

---

## 다음 후보 (미착수)
- 유니버스 빌더(us_top300·aliases) 자체 생성 스크립트(현재 data/에 스냅샷만 복사).
- `registry.json` 자동렌더로 이 표를 코드↔맵 정합성까지 기계 검증(모듈 늘면).
- DART 재무정보 API(fnlttSinglAcnt 등) 추가 — 현재는 공시목록·원문·사업보고서까지.
