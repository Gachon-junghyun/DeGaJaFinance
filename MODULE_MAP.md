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
| [module_growth](#module_growth) | 이익 성장 기업 스크리너(실험 모델) | "이익 성장 기업 찾기", 유니버스 성장 스윕·랭킹(순이익 YoY·가속·선행) |
| [module_epistemics](#module_epistemics) | 베이지안 충돌평가·민감도 학습·verify·registry_audit | 신호 모순 해소, 종목 민감도 축적, 코드↔맵 감사 |
| [module_order_desk](#module_order_desk) | KIS 주문 데스크(Tkinter GUI) — 스택형 휴먼 주문 | 시세 보며 주문을 스택에 쌓아 카드마다 [체결], 포폴·인기·흐름·만약에 |
| [scripts/](#스크립트-데스크-호출) | 데스크가 `python scripts/X.py`로 호출하는 단일파일 도구 9 | 수급·섹터로테이션·촉매·숏리스트·스크리너 |

> 층위 설계(큰축→모듈→기능 + 인수인계)는 [`pipeline/`](pipeline/README.md).

**의존 그래프(재사용 = 중복 없음의 증거 · 옛 리포 런타임 링크 0):**
```
module_flow ─ news velocity ─▶ module_news_data (_config: FOREIGN_SOURCES·FTS 경로·utf8)
            └ ⑦ 투자자수급 ──▶ module_KIS (_investor)
module_disclosure ─ 사업보고서 corp_code ─▶ 자체 _corp_codes (corp_codes.csv)
module_fundamentals_us ──▶ module_disclosure_us   ·   module_timefolio ──▶ module_webctl
module_growth ─ US 재무 ──▶ module_fundamentals_us   ·   ─ KR 선행 ──▶ module_valuation
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
- ⚠️ **파이프라인**: `embed sync`(하루2초) → `cluster`(7초) → `classify` → `brief`.
  실측 하루 3,782건 → 사건 512 → 시장 394 → 머리61/몸통143/꼬리190 → **44k 토큰**(제목전부 146k 대비 3배 압축).
  꼬리는 **자르지 않고** 분모+무작위표본으로 준다 — 매체수는 중요도의 대리지표지 진실이 아니다.
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

| `theme-age` | 테마 나이·가속(FRESH vs ECHO) | `... theme-age humanoid "Strait of Hormuz" --scope foreign` |
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
  ```
- **공개 API**: `fetch_disclosures · fetch_disclosure_detail · resolve_corp_code · categorize · parse_contract/treasury/capital · summarize_contracts · fetch_business_report`
- **소유**: DART list.json·document 조회, corp_code 매핑, 공시 카테고리 분류·계약 상세파싱.
- **환경변수**: `DART_API_KEY`(.env). `corp_codes.csv`는 7일 TTL 자동 갱신(`refresh_corp_codes`).
- 사업보고서 본문 fetch(`--business-report`)는 DART 뷰어가 프레임셋이라 best-effort(옛 코드 그대로).

---

## 산업 데스크 모듈
industry_us/kr 프로토콜이 호출하는 분석 모듈. 전부 기능별 `_파일` + `__main__` CLI. 옛 이름 유지(크로스임포트·프로토콜 호출 호환).

| 모듈 | 트리거 | CLI(예) | 소유/의존 |
|---|---|---|---|
| `module_macro_us` | US 매크로 레짐(FRED 지표) | `python -m module_macro_us` | FRED_API_KEY |
| `module_valuation` | KR 밸류에이션 스냅샷·목표가·peer 비교(수동 `--peers`) | `python -m module_valuation 005930 --peers 000660` | DART/KRX |
| `module_industry_map` | 임베딩 클러스터로 산업 지도·밸류체인 | `python -m module_industry_map` | data/corp_embeddings.db (직접 sqlite) |
| `module_business` | KR 사업모델(매출표·제품)+IR 발췌 | `python -m module_business 005930` | data/corp_embeddings.db + news_alert.db |
| `module_business_us` | US 사업모델(EDGAR/yf) | `python -m module_business_us AAPL` | 자립(yf/EDGAR) |
| `module_disclosure_us` | US 공시(SEC EDGAR) | `python -m module_disclosure_us AAPL` | ticker_cik 캐시(자체) |
| `module_fundamentals_us` | US 펀더멘털(매출·**순이익·EPS**엔진) | `python -m module_fundamentals_us AAPL` | ▶module_disclosure_us · ◀module_growth |
| `module_math_check` | 리포트 수치 산술 검증 | `python -m module_math_check ...` | 자립(stdlib) |
| `module_watchlist` | thesis 단위 워치리스트 DB | `python -m module_watchlist init` | data/watchlist.db |
| `module_publish` | 산출물 렌더·발행 헬퍼 | `python -m module_publish ...` | 자립 |

- **재사용(중복0)**: `module_fundamentals_us`→`module_disclosure_us`. corp_embeddings.db 는 industry_map·business 가 직접 sqlite 로 읽음(로컬 data/).

## module_paper_book
데스크 리포트(BET_SHEET·ACTION_TICKETS·평결)를 읽어 **모의투자(paper) 장부**를 굴린다. `paper_desk` 프로토콜의 결정론 엔진 — 판단(무엇을 살지)은 프로토콜(에이전트)이, 이 모듈은 '얼마나·어떻게'의 기계만 제공한다(P4).

- **트리거**: 산업/기업 데스크 산출물을 읽어 리스크 사이징·체결 시뮬레이션·시가평가·결정 저널을 남길 때. 실제 주문 아님(모의).
- **기능 지도**: `_book`(SQLite 장부 단일원본: 현금슬리브·포지션·체결원장·자기자본 스냅샷) · `_intake`(리포트→실행가능 후보; ▶module_report_tags 유니버스·태그 재사용) · `_risk`(리스크기반 사이징+집중도가드) · `_mark`(시가평가; ▶module_KIS(KR)/yfinance(US)) · `_journal`(결정저널+트랙레코드).
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
  ```
- **소유**: 모의 장부 상태·체결 회계·리스크 사이징·트랙레코드 + **미러(_mirror: 실계좌↔paper↔주문스택 동기화)**. **재사용(중복0)**: 리포트 태그/유니버스는 `module_report_tags`, 시세는 `module_KIS`/yfinance, **주문 스택은 `module_order_desk.stack`, 학습된 민감도는 `module_epistemics`** — 다시 구현하지 않는다.
- **미러링(`_mirror`)**: `mirror`=실 KIS 보유를 '이미 보유'로 시드(현금 슬리브 셋). `stage`=추천을 `out/order_desk/kis_stack.json`(주문 데스크 스택)에 intent 카드로 적재 — **사람이 [체결]로 발사, 자동 아님**. `learned_sensitivity/record_sensitivity`=epistemics 원장 조회/되먹임. 프로토콜 [`미러링`](pipeline/protocols/미러링.md).
- **데이터**: `data/paper_book.db`(`PAPER_BOOK_DB_PATH` 로 이동가능). **안전**: 체결은 기본 드라이런, `--commit` 사람 명시 전용. 스케줄러 자동발사 없음.
- **환경변수**: (KR 마크에) `KIS_APP_KEY/SECRET`. US 마크는 yfinance(무인증).

## module_growth
유니버스(us_top300·kr_all)를 훑어 분기 이익 시계열에서 **결정론 성장 지표**를 계산·랭킹하는 실험 스크리너. 판단(매수/매도)은 내지 않고 관측값·출처·신선도만(P4) — 무엇을 살지는 상위(에이전트).

- **트리거**: "이익 성장 기업 찾기" / 성장주 스윕·랭킹. 후보 발굴 뒤 흐름·촉매·차트로 교차확인.
- **CLI**:
  ```bash
  python -m module_growth --market us --limit 50 --top 20        # top50 시총 스윕 → 성장 랭킹
  python -m module_growth --market us --sector Semiconductors    # 섹터(gics_sector·industry 둘 다 매칭)
  python -m module_growth --ticker NVDA AMD AVGO --detail        # 임의 티커 직접 비교
  python -m module_growth --market us --limit 30 --json          # 기계 소비용
  ```
- **기능 파일**: `_metrics`(순수 성장수식: YoY·TTM YoY·가속·선행EPS성장·PEG태그+성장점수/등급, **네트워크 0·합성 픽스처로 검증가능**) · `_universe`(유니버스 CSV 로더) · `_screen`(fetch 오케스트레이션+랭킹) · `_render`(마크다운 표) · `__main__`(CLI).
- **성장 점수**: 대략 '연 YoY %'. 실현 순이익 성장(TTM YoY→분기 YoY→EPS YoY) 1순위, 없으면 선행·매출로 강등. 가속 보정 + 이익성장이 매출 뒷받침 없으면 감점. 가중치·임계값은 `_metrics` 모듈 상수(실험자가 튜닝).
- **재사용(중복0)**: 재무 fetch 를 **재구현하지 않는다** — US=`module_fundamentals_us.fetch_fundamentals`(분기 손익+컨센), KR=`module_valuation.fetch_naver_snapshot`. 둘 다 lazy import.
- **소유**: 성장 지표 계산(`_metrics`)·성장 점수/등급.
- ⚠️ **시장별 데이터 한계(P4)**: US=yfinance 분기 손익=실현 순이익/매출/EPS 히스토리(보통 4~5분기, YoY 는 5분기+ 필요, 최대 8). **KR=네이버 스냅샷이라 선행 EPS 성장(컨센)만** — 실현 분기 이익 히스토리 부재. **KR 실현 성장은 DART 재무제표 API(fnlttSinglAcnt) 도입 후**(아래 '다음 후보').
- **데이터**: `data/us_universe/us_top300.csv`·`kr_universe/kr_all.csv`(읽기전용 참조). 산출은 `--out` 지정 시 그 경로(기본 stdout).

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
| `drift_watch.py` | 완주 후 킬스위치 버스트 감시 | data/news_fts.db |
| `theme_age`·`chain_hop`·`news_blindspot` | (이미 module_news_data 서브커맨드) | — |
| `cycle_exposure.py` | 사이클 노출 GAP | data/cycles, module_KIS |
| `catalyst_calendar.py` | 촉매 날짜 캘린더 | data/catalysts |
| `action_bracket.py` | 진입 브래킷(스탑/타겟) | data/cycles·catalysts, module_KIS |
| `us_live_shortlist.py`·`kr_live_shortlist.py` | 장중 라이브 숏리스트 | data/us_universe·kr_universe |
| `us_setup_screener.py` | US 셋업 스크리너(top300 3바구니) | data/us_universe (⚠️indicator_alerts.db=옛 alert_bot, 미포팅→graceful) |

---

## 다음 후보 (미착수)
- 유니버스 빌더(us_top300·aliases) 자체 생성 스크립트(현재 data/에 스냅샷만 복사).
- `registry.json` 자동렌더로 이 표를 코드↔맵 정합성까지 기계 검증(모듈 늘면).
- DART 재무정보 API(fnlttSinglAcnt 등) 추가 — 현재는 공시목록·원문·사업보고서까지.
  이게 붙으면 `module_growth` 의 **KR 실현 이익 성장**(현재는 네이버 선행 컨센만)이 열린다.
