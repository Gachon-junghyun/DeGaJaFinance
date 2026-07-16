@echo off
REM ============================================================
REM  DeGaJaFinance news search API server (server PC role).
REM  Exposes the news DB (news_fts) over HTTP so clients query via
REM  DEGAJA_NEWS_API=http://<this PC IP>:8787 using the same CLI.
REM  Change port: run_news_api.bat 9999  (or DEGAJA_NEWS_API_PORT).
REM  Allow inbound TCP 8787 in the firewall (LAN).  (Korean: Server\README.md)
REM ============================================================
chcp 65001 >nul
pushd "%~dp0.."
if not exist "data" mkdir "data"
title DeGaJa NEWS API server
python -X utf8 "Server\news_api.py" %1
pause
