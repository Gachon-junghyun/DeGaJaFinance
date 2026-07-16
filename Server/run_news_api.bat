@echo off
REM ============================================================
REM  DeGaJaFinance 뉴스 검색 API 서버 (서버 PC 용).
REM  뉴스 DB(news_fts)를 HTTP 로 노출한다. 클라이언트 PC 는
REM  DEGAJA_NEWS_API=http://<이 PC IP>:8787 만 켜면 같은 CLI 로 원격 검색.
REM  포트 바꾸려면: run_news_api.bat 9999  (또는 DEGAJA_NEWS_API_PORT).
REM  방화벽에서 인바운드 TCP 8787 허용 필요(LAN).
REM ============================================================
chcp 65001 >nul
cd /d %~dp0..
title DeGaJa NEWS API server
python -X utf8 Server\news_api.py %1
pause
