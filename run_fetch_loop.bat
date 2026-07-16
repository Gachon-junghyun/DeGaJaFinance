@echo off
REM News collector moved to Server\ (server PC role). This is a back-compat shim.
REM Server PC uses Server\run_fetch_loop.bat (collect) + Server\run_news_api.bat (serve).
REM Clients set DEGAJA_NEWS_API for remote search via the same CLI. See Server\README.md.
call "%~dp0Server\run_fetch_loop.bat"
