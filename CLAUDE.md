# DeGaJaFinance — 리포 헌법

> 이 문서는 **방법론만** 담는다: 원칙과 규약. "어떤 모듈이 있고, 언제, 어떻게 쓰는지"는
> 여기 적지 않는다 — [`MODULE_MAP.md`](MODULE_MAP.md)를 읽어라. 모듈을 만들거나 쓰기 전에
> 그 지도를 먼저 봐서 이미 있는 기능을 다시 짓지 않도록 한다.

---

## 원칙 (P1~P6)

- **P1 단일 원본.** 기능·상수·시크릿은 한 곳에만 정의하고, 다른 곳은 import 해서 **재사용**한다.
  같은 외부 API를 두 번 구현하지 않는다. 무엇이 어디의 단일 원본인지는 MODULE_MAP.md의 "소유/재사용" 열이 기록한다.
- **P2 기능별 파일.** 모듈 = 패키지 디렉토리. 기능 하나 = `_기능.py` 하나. `__init__.py`가 공개 API를
  re-export 하고, `__main__.py`가 서브커맨드 CLI를 연다.
- **P3 시장 파라미터화.** KR/US 차이는 모듈 내부 인자(`--market`·`--scope`, KR 티커 자동감지)로 흡수한다.
  시장별로 파일을 미러 복제하지 않는다.
- **P4 알아야 말한다.** 결론(매매 판단·리포트)은 관측값+출처+신선도를 채운 뒤에만 낸다. 모듈은 결정론
  데이터/분석만 산출하고, 판단은 상위(에이전트) 몫으로 남긴다.
  - **라이브 판단은 후행 데이터로 하지 않는다.** "지금 나락?" 같은 현재상황 질문은 (a) 뉴스 DB **1일내**
    (`fts search … --days 1`) 촉매 + (b) 관련 종목 **싹 현재가·당일등락**(`module_paper_book pulse`)로 판단한다.
    파이프라인 기본 재료(뉴스 60일·EOD)는 라이브 진단에 늦다. **불안에 맞춰 폭락을 지어내지 않는다** —
    데이터가 보합이면 보합이라 말하고(광의폭락/섹터이벤트/개별/노이즈로 분류), 데이터 asof 시점을 밝힌다.
    루틴 원본은 [`pipeline/L1_stages/pulse.md`](pipeline/L1_stages/pulse.md)(PULSE 스테이지).
- **P5 라이브 보호.** 옛 mvp 리포의 cron·수집·페이퍼북은 이 리포가 건드리지 않는다. 그 산출(DB·유니버스)은
  읽기 전용으로만 참조한다. 기능을 옮겨 컷오버하는 결정은 사람이 내린다.
- **P6 서버·클라이언트 분리.** 서버 PC 는 **수집·검색 서빙 전용**(저사양, GPU·torch 없음, 24시간 가동),
  무거운 계산(임베딩·클러스터링)은 **클라이언트**(고사양 PC, 필요할 때만 켬)가 한다. 둘은 **같은 리포
  코드**를 돌리므로 — 서버에 없는 것을 최상단에서 import 하면 서버가 통째로 죽는다.
  - 무거운 서드파티(`torch`·`sentence_transformers`·`sklearn`)는 **모듈 최상단 import 금지**.
    서버가 `__main__.build_parser` 로 모든 기능 파일을 import 하므로 최상단 import 하나가
    **서버를 기동 불능으로 만든다.** 반드시 실제 계산 함수 안에서 import 한다.
  - 그 기능은 `__main__.DB_READ_CMDS` 에 **넣지 않는다**(원격 실행 금지). 서버 뉴스DB 대신 클라이언트
    소유 파생물(`data/news_vectors.db`)을 읽고, 원본이 필요하면 `_export.pull` 로 받아온다
    (전송 분기는 거기 한 곳에만 — 소비자마다 다시 짜면 P1 위반).
  - 조회 서브커맨드 허용목록의 단일 원본은 `__main__.DB_READ_CMDS` — `Server/news_api.py` 가 import 한다.
    거기 한 줄 추가하면 서버가 자동으로 따라오지만, **서버에도 git pull + API 재시작이 필요**하다.
  - 클라이언트는 켤 때마다 밀린 만큼 **따라잡는다**(증분, `url_hash` 로 멱등). 꺼져 있어도 수집은 계속된다.

## 규약 (모듈 작성·사용 시)

- 새 모듈 = `module_이름/` + 기능별 `_파일` + `__init__`(공개 API) + `__main__`(CLI) + **MODULE_MAP.md에 한 줄 등록.**
- 새 프로토콜/스테이지 = `pipeline/`(protocols·L1_stages·L2_modules·L3_functions)에 두고 **`pipeline/README.md`·`PROMPT_MAP.md`에 등록**(MODULE_MAP은 모듈 전용). 스테이지 링크는 composition 표에만(산문은 plain-text — 컴파일 순서 보호). **긴 프로토콜은 `run_protocol.py <name>`로 스테이지별(그 L1+호출 L2/L3만) 실행해 컨텍스트 누락을 막는다** — 한 스테이지 → EXIT CHECK → `--next`, 이전 산출물은 메모리 말고 run 디렉토리를 다시 읽는다.
- 다른 모듈의 기능이 필요하면 **그 모듈에서 import** 한다(복제 금지). 새로 지어야 할 것 같으면 먼저 MODULE_MAP.md에
  같은 기능이 있는지 확인한다.
- 의존성은 표준라이브러리 + `requests` + (데이터 모듈은) `pandas`/`numpy`/`yfinance`. 그 밖의 서드파티는 추가 전에 사람 확인.
  - **승인된 예외 (2026-07-17, 사람 승인): `sentence-transformers`·`torch`·`scikit-learn`.**
    뉴스 사건 클러스터링 전용 — 어휘 기반(자카드·코사인·LSA)으로는 같은 사건을 못 묶는다는 걸
    실측으로 소진한 뒤 도입했다(근거는 `module_news_data/_embed.py`·`_cluster.py` 상단).
    **이 셋은 무거운(≈GB) GPU 계열이라 아래 P6 의 제약을 받는다.** 다른 용도로 확장하기 전에 다시 확인.
- **GPU 계열을 쓰는 새 기능은 P6 를 반드시 지킨다** — lazy import + `DB_READ_CMDS` 제외.
  어긴 채 커밋하면 서버 PC 의 수집·검색이 **전부** 멈춘다(기동 실패).
- CLI 진입점마다 `utf8_stdout()` (또는 `sys.stdout.reconfigure`) — Windows cp949 콘솔 크래시 방지.
- 주문·집행 계열은 **기본 드라이런, `--execute`는 사람이 명시.** 스케줄러가 자동 발사하는 코드는 만들지 않는다.
- 모듈 산출 파일은 `out/` 아래에 쓴다(커밋 대상 아님). 시크릿(`.env`)·토큰 캐시는 커밋하지 않는다.

## 시크릿·데이터

- 이 리포는 **자립**한다 — 옛 mvp 리포에 런타임 링크가 없다. 데이터·DB·시크릿 전부 로컬 소유.
- 데이터는 `data/`(환경변수 `DEGAJA_DATA_DIR`로 이동 가능): `news_alert.db`(수집)·`news_fts*.db`(색인)·
  `us_universe/`·`kr_universe/`·`news_synonyms*.json`. 어느 모듈이 무엇을 쓰는지는 MODULE_MAP.md.
- **소유가 갈린다(P6)**: `news_alert.db`·`news_fts*.db` = **서버**가 쓰고 클라는 읽기만(원격이면 API 경유).
  `news_vectors.db` = **클라이언트 소유 파생물**(임베딩·동기화 커서) — 서버는 존재도 모른다. 서버 DB 의
  스키마를 클라 편의로 바꾸지 않는다. 파생물은 언제든 지우고 다시 만들 수 있어야 한다(실측 재생성 2분 27초).
- 시크릿(`KIS_*`·`KRX_*`·`DART_API_KEY` 등)의 단일 원본은 이 리포 `.env`. 평문 시크릿을 코드에 넣지 않는다.
- 뉴스 수집은 이 리포가 소유·구동한다. **서버 PC 역할 = [`Server/`](Server/README.md)**: `Server/run_fetch_loop.bat`(수집 루프)
  + `Server/run_news_api.bat`(검색 API, stdlib http.server, 기본 :8787). 루트 `run_fetch_loop.bat` 는 Server 로 위임하는 shim.
- **뉴스 접근 = API 우선.** 클라이언트/Claude Code 는 DB 파일을 직접 열지 않고 `DEGAJA_NEWS_API=http://<서버IP>:8787` 만
  켜면 **DB 를 읽는 모든 조회 서브커맨드**(`search·fts search·coverage·blindspot·theme-age·chain-hop`)를 서버 `/exec` 로
  넘겨 실행한다 — **클라이언트 로컬 뉴스 DB 를 지워도 동작**(서버가 자기 DB 로 실행). 비면 로컬 폴백. 서버는 클라이언트
  argv 를 같은 CLI 파서(`__main__.build_parser`)로 실행하고 stdout 을 반환(재구현 0, P1). 쓰기(`fetch·fts build/update`)는
  서버 콘솔에서만 — 클라이언트에선 거부. stdlib(http.server/urllib)만.
