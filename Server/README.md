# Server — 뉴스 수집기 + 검색 API (서버 PC 역할)

이 폴더가 **서버 PC 역할**이다: 뉴스를 계속 수집해 DB 에 쌓고(수집기), 그 DB 를
HTTP API 로 노출한다(검색 서빙). 다른 PC(또는 Claude Code)는 DB 파일을 직접 열지
않고 **API 로 검색을 끌어온다** — 명령어는 그대로, 환경변수 하나만 켜면 된다.

```
┌───────────── 서버 PC (이 Server/ 폴더 구동) ─────────────┐
│  run_fetch_loop.bat  ─수집→  data/news_alert.db·news_fts*.db │
│  run_news_api.bat    ─서빙→  http://0.0.0.0:8787            │
└──────────────────────────────┬───────────────────────────┘
                               │ HTTP (LAN)
┌──────────────────────────────▼───────────────────────────┐
│  클라이언트 PC / Claude Code                                │
│  set DEGAJA_NEWS_API=http://<서버IP>:8787                   │
│  python -m module_news_data fts search "Micron" --days 1   │  ← 같은 CLI, 원격 검색
└───────────────────────────────────────────────────────────┘
```

## 서버 PC 에서 (2개 창)
1. **수집 루프** — `Server\run_fetch_loop.bat` 더블클릭. 한 틱 = RSS+본문+FTS 증분색인(영/한). 창 닫으면 멈춤. 로그 `data\fetch_loop.log`.
2. **검색 API** — `Server\run_news_api.bat` 더블클릭(기본 :8787). `run_news_api.bat 9999` 로 포트 변경.
3. 방화벽에서 **인바운드 TCP 8787**(LAN) 허용. 서버 PC 자신은 `DEGAJA_NEWS_API` 를 **비운다**(로컬 DB 직접).

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

## API 엔드포인트 (직접 호출도 가능)
| GET | 반환 |
|---|---|
| `/health` | DB 경로·존재여부 |
| `/fts/search?terms=A&terms=B&days=14&scope=foreign&mode=and&snippet=1&limit=40[&kr=1][&syn=1][&full=1]` | `{match,count,rows:[…]}` |
| `/fts/count?terms=…&days=…&scope=…` | `{count:N}` |

- `terms` 는 반복 파라미터(`terms=A&terms=B`), `scope`=all/foreign/domestic, `mode`=and/or.
- 쿼리 로직은 `module_news_data._fts.query_fts` **단일 원본을 재사용**(서버가 재구현 안 함, P1).
- 의존성 **표준 라이브러리만**(http.server/urllib) — 서드파티 없음.

## 커버리지/블라인드스팟 등 무거운 분석은?
`coverage·blindspot·theme-age·chain-hop` 은 아직 DB 직접 읽기다. 그 명령들은 **서버 PC 에서**
돌리거나(로컬 DB 있음), 클라이언트에 DB 사본이 있을 때만 동작한다. 현재 API 라우팅은 데스크가
제일 많이 쓰는 **fts search / count** 만 커버한다(필요하면 같은 패턴으로 엔드포인트 추가).
