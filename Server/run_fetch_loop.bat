@echo off
REM ============================================================
REM  DeGaJaFinance 뉴스 수집 루프 (서버 PC 용).
REM  한 틱 = RSS 헤드라인 + 본문 스크랩 + FTS 증분색인(영문 porter + 한글 trigram).
REM  더블클릭하면 이 창이 계속 열려 주기적으로 수집한다. 창 닫으면 멈춤.
REM  로그: data\fetch_loop.log   |  간격: 아래 INTERVAL(초), 기본 3600 = 1시간.
REM  검색 서빙은 별도로 run_news_api.bat 를 띄운다(이 창은 수집 전담).
REM ============================================================
chcp 65001 >nul
setlocal
set INTERVAL=3600
cd /d %~dp0..
title DeGaJa NEWS FETCH loop (interval=%INTERVAL%s)

:loop
echo ===== %DATE% %TIME%  fetch full + FTS update =====
echo ===== %DATE% %TIME%  fetch full + FTS update ===== >> data\fetch_loop.log
python -X utf8 -m module_news_data fetch full   >> data\fetch_loop.log 2>&1
python -X utf8 -m module_news_data fts update    >> data\fetch_loop.log 2>&1
python -X utf8 -m module_news_data fts update --kr >> data\fetch_loop.log 2>&1
echo    done %TIME% -- sleeping %INTERVAL%s (Ctrl+C 로 종료)
timeout /t %INTERVAL% /nobreak >nul
goto loop
