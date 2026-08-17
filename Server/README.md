# Server — 뉴스 수집기 + 검색 API (서버 PC 역할)

이 폴더가 **서버 PC 역할**이다: 뉴스를 계속 수집해 DB 에 쌓고(수집기), 그 DB 를
HTTP API 로 노출한다(검색 서빙). 다른 PC(또는 Claude Code)는 DB 파일을 직접 열지
않고 **API 로 검색을 끌어온다** — 명령어는 그대로, 환경변수 하나만 켜면 된다.

```
┌───────────── 서버 PC (이 Server/ 폴더 구동) ─────────────┐
│  run_fetch_loop.bat     ─수집→ data/news_alert.db·news_fts*.db │
│  run_news_api.bat       ─서빙→ http://0.0.0.0:8787          │
│  run_snapshot_loop.bat  ─적립→ data/estimates/eps_*.json     │
└──────────────────────────────┬───────────────────────────┘
                               │ HTTP (LAN)
┌──────────────────────────────▼───────────────────────────┐
│  클라이언트 PC / Claude Code                                │
│  set DEGAJA_NEWS_API=http://<서버IP>:8787                   │
│  python -m module_news_data fts search "Micron" --days 1   │  ← 같은 CLI, 원격 검색
└───────────────────────────────────────────────────────────┘
```

## 서버 PC 에서 (3개 창)
1. **수집 루프** — `Server\run_fetch_loop.bat` 더블클릭. 한 틱 = RSS+본문+FTS 증분색인(영/한). 창 닫으면 멈춤. 로그 `data\fetch_loop.log`.
2. **검색 API** — `Server\run_news_api.bat` 더블클릭(기본 :8787). `run_news_api.bat 9999` 로 포트 변경.
3. **추정치 스냅샷 루프** — `Server\run_snapshot_loop.bat` 더블클릭(신규, dig **D16**). 로그 `data\snapshot_loop.log`.
4. 방화벽에서 **인바운드 TCP 8787**(LAN) 허용. 서버 PC 자신은 `DEGAJA_NEWS_API` 를 **비운다**(로컬 DB 직접).

### 3번이 서버로 온 이유 (P6 · 2026-08-09 실측)
`yfinance eps_trend` 는 시계열이 아니라 **스냅샷**이고 **소급 복구가 안 된다** — 안 쌓은 날은 영영 없다.
이 작업은 원래 **클라이언트 PC 의 08:10 스케줄 태스크**였는데, 클라이언트는 *"필요할 때만 켜는"* 기계이고
24시간 도는 것은 이 서버다. 실측: **19 캘린더일에 파일 6개**, 간격 **2→3→4→6 으로 단조 증가** ⇒
40일 패널이 34일이 아니라 **약 108일** 뒤에 온다. 간격 수열은 사실상 **클라 PC 를 켠 빈도**였다.

⚠ **고정시각 태스크가 아니라 루프인 이유**: 08:10 에 기계가 꺼져 있으면 그날을 통째로 잃는다.
루프는 매시간 재시도하고 스크립트 자체가 **멱등**(같은 날 파일이 있으면 `--force` 없이는 덮지 않는다)이라,
**그날 중 아무 때나 켜져 있으면 그 날짜를 회수**한다.

⚠ 클라이언트에 남아 있는 Windows 태스크 `DeGaJa-EstimateSnapshot` 은 **꺼도 된다**(멱등이라 켜 둬도
해는 없다). 진행률은 `python -X utf8 scripts\snapshot_estimates.py --status` — **파일 개수가 아니라
실측 속도와 캘린더 ETA** 를 낸다(옛 출력은 개수를 일수로 보고해 고장을 숨겼다).

건강확인: 브라우저로 `http://127.0.0.1:8787/health` → `{"ok":true,...}`.

## 클라이언트 PC / Claude Code 에서
```bat
setx DEGAJA_NEWS_API "http://192.168.0.50:8787"   REM 서버 PC IP:PORT (새 셸부터 적용)
```
그 뒤엔 **평소 그대로**:
```
python -X utf8 -m module_news_data fts search "삼성전기" --days 1 --snippet
python -X utf8 -m module_news_data fts search "Micron" HBM --scope foreign --days 3 --count
```
헤더에 ` ·via API` 가 붙으면 원격에서 끌어온 것. `DEGAJA_NEWS_API` 를 지우면 즉시 로컬 DB 폴백.
접속 실패 시 결과 dict 에 `error` 가 담겨 사유를 알려준다(서버 다운/방화벽/오타).

## 라우팅되는 조회 = 전부 (로컬 DB 없어도 됨)
`DEGAJA_NEWS_API` 가 켜지면 **DB 를 읽는 모든 조회 서브커맨드**가 서버에서 실행된다:
`search · fts search · coverage · blindspot · theme-age · chain-hop`. 클라이언트는 **뉴스 DB 를 지워도**
이 명령들이 다 동작한다(서버가 자기 로컬 DB 로 실행 → 결과 텍스트 반환). stderr 에 `(via NEWS API @ …)` 표시.
쓰기(`fetch · fts build/update`)는 **서버 PC 콘솔에서만** — 클라이언트에서 부르면 거부된다.

## API 엔드포인트 (직접 호출도 가능)
| GET | 반환 |
|---|---|
| `/health` | DB 경로·존재여부·허용 조회목록 |
| `/exec?argv=fts&argv=search&argv=Micron&argv=--days&argv=3&argv=--scope&argv=foreign` | `{stdout: "<렌더 텍스트>"}` |

- `argv` = 반복 파라미터로 CLI 인자를 순서대로(`argv=coverage&argv=nuclear&argv=--days&argv=30`).
- 서버는 클라이언트가 보낸 argv 를 **module_news_data 의 같은 CLI 파서**(`build_parser`)로 파싱·실행하고
  stdout 을 캡처해 돌려준다 — 쿼리/분석 로직 재구현 0(P1). 조회 서브커맨드만 화이트리스트(쓰기 거부).
- 의존성 **표준 라이브러리만**(http.server/urllib) — 서드파티 없음.
