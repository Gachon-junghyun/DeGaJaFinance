@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Starting KIS order desk (Tkinter)...
echo.

python -m module_order_desk
if errorlevel 1 (
    echo.
    echo [python failed] trying py launcher...
    py -3 -m module_order_desk
)

echo.
echo ============================================================
echo Window closed. If an error appeared, see kis_desk_error.log
echo ============================================================
pause
