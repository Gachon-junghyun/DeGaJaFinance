@echo off
REM ============================================================
REM  DeGaJaFinance news fetch loop (server PC role).
REM  One tick = RSS headlines + body scrape + FTS incremental (EN porter + KR trigram).
REM  Double-click to run; closing the window stops it. Log: data\fetch_loop.log
REM  Change INTERVAL (seconds) below. Default 3600 = 1 hour.
REM  Search serving is separate: run_news_api.bat.  (Korean guide: Server\README.md)
REM ============================================================
chcp 65001 >nul
setlocal
set "INTERVAL=3600"
pushd "%~dp0.."
if not exist "data" mkdir "data"
title DeGaJa NEWS FETCH loop

:loop
echo ===== %DATE% %TIME%  fetch full + FTS update =====
echo ===== %DATE% %TIME%  fetch full + FTS update ===== >> "data\fetch_loop.log"
python -X utf8 -m module_news_data fetch full      >> "data\fetch_loop.log" 2>&1
python -X utf8 -m module_news_data fts update       >> "data\fetch_loop.log" 2>&1
python -X utf8 -m module_news_data fts update --kr  >> "data\fetch_loop.log" 2>&1
echo    done %TIME% -- sleeping %INTERVAL%s (Ctrl+C to stop)
timeout /t %INTERVAL% /nobreak >nul
goto loop
