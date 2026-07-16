# module_kis — 한국투자증권(KIS) Open API 조회 모듈

국내주식 **현재가·밸류에이션·기간별 OHLCV·투자자별 수급·계좌잔고**를 KIS 공식 API로 수집한다.
`yfinance`(.KS/.KQ 접미사 추정)·네이버 스크랩의 무인증 채널 대비 **인증 기반 안정 소스**.

> **조회(시세/잔고)는 자유. 주문은 휴먼 트리거 전용.** `place_order` 는 기본 드라이런이고
> 사람이 `--execute`(=execute=True)를 명시할 때만 실제 발사한다. 자동매매/스케줄 자동발사 아님.
> 정정/취소/이체는 미포함.

## 설치 / 설정

추가 의존성 없음 — `requests`(mvp 공용)만 쓴다.

`.env` 또는 셸에 KIS 키 설정:

```
KIS_APP_KEY=...
KIS_APP_SECRET=...
KIS_ENV=prod          # prod=실전 | vps=모의투자
KIS_CUST_TYPE=P       # P=개인 | B=법인
KIS_ACCOUNT_NO=12345678-01   # 잔고조회(--balance) 시만 필요. 시세조회엔 불필요.
```

앱키/시크릿 발급: https://apiportal.koreainvestment.com
(실전과 모의는 **앱키가 서로 다르다** — 모의 조회는 모의 키 필요)

접근토큰은 발급 후 24h 유효하나 KIS가 재발급을 분당 1회로 제한하므로,
`.kis_token_cache.json`(프로젝트 루트, gitignore됨)에 캐시해 만료 직전까지 재사용한다.

## CLI

```bash
python -m module_kis 005930                        # 시세 스냅샷
python -m module_kis 005930 --ohlcv D --count 120  # 일봉 120개
python -m module_kis 005930 --ohlcv W --count 60    # 주봉
python -m module_kis 005930 --investor 20          # 외국인/기관 수급 20영업일
python -m module_kis 005930 --all                  # 시세+일봉+수급
python -m module_kis 005930 --all --out llm_outputs/kis_005930.md
python -m module_kis 005930 --json                 # 시세 JSON
python -m module_kis --balance                     # 계좌 잔고(예수금+보유종목), 코드 불필요
python -m module_kis 005930 --all --balance        # 종목조회 + 잔고

# 주문 — 기본 드라이런(미리보기). 실제 발사는 --execute 를 사람이 직접.
python -m module_kis 005930 --order buy --qty 1 --price 349000            # 미리보기
python -m module_kis 005930 --order buy --qty 1 --price 349000 --execute  # 실발사
python -m module_kis 005930 --order sell --qty 1 --market                 # 시장가 매도(미리보기)
```

## Python API

```python
from module_kis import fetch_quote, fetch_ohlcv, fetch_investor_trend

q = fetch_quote("005930")                  # KisQuote
print(q.price, q.per, q.pbr, q.foreign_pct)

bars, name = fetch_ohlcv("005930", "D", count=250)   # list[KisBar] (날짜 오름차순)
rows = fetch_investor_trend("005930", days=20)        # list[InvestorDay]
```

## 구조

| 파일 | 역할 |
|------|------|
| `_auth.py` | 설정 로딩 + OAuth2 토큰 발급/디스크 캐시, `KisError` |
| `_client.py` | 공통 GET 래퍼(헤더·tr_id·토큰만료 재시도) |
| `_parse.py` | 응답 문자열 → 숫자 변환 헬퍼 |
| `_quote.py` | 현재가/밸류에이션 (`inquire-price`, tr_id `FHKST01010100`) |
| `_chart.py` | 기간별 OHLCV (`inquire-daily-itemchartprice`, `FHKST03010100`) |
| `_investor.py` | 투자자별 순매수 (`inquire-investor`, `FHKST01010900`) |
| `_account.py` | 국내 잔고(읽기전용) (`inquire-balance`, `TTTC8434R`/`VTTC8434R`) |
| `_overseas.py` | 외화/해외 잔고(읽기전용) (`inquire-present-balance`, `CTRP6504R`) |
| `_order.py` | 현금 주문(휴먼 트리거) (`order-cash`, `TTTC0802U`/`TTTC0801U`, hashkey) |
| `_renderer.py` | markdown 렌더러 |

## 엔드포인트 메모

- 모든 조회는 `FID_COND_MRKT_DIV_CODE=J`(KRX 주식/ETF/ETN) 기준.
- `inquire-price`는 한글 종목명을 안 준다 → `_chart` output1(`hts_kor_isnm`)로 보강.
- `inquire-daily-itemchartprice`는 1콜당 최대 100봉 → `_chart`가 날짜창을 밀며 페이지네이션.
- OHLCV 기본은 **수정주가**(`FID_ORG_ADJ_PRC=0`). `--raw-price`로 원주가 전환.
