@echo off


REM check FFMpeg existence..
where ffmpeg >nul 2>nul
if %errorlevel% equ 0 (
    echo FFMpeg already installed.
    exit /b 0
) else (
    echo FFMpeg not found.
    exit /b 1
)

