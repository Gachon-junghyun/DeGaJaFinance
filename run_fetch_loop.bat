@echo off
REM 뉴스 수집기는 Server\ 로 이관됐다(서버 PC 역할). 이 파일은 하위 호환 shim.
REM 서버 PC 에서는 Server\run_fetch_loop.bat(수집) + Server\run_news_api.bat(검색 서빙)을 쓴다.
REM 클라이언트는 DEGAJA_NEWS_API 만 켜면 같은 CLI 로 원격 검색(Server\README.md 참고).
call "%~dp0Server\run_fetch_loop.bat"
