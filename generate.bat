@echo off
setlocal
cd /d "%~dp0"
where node >nul 2>nul
if errorlevel 1 (
  echo ERROR: Node.js tidak ditemukan. Install dari https://nodejs.org
  pause
  exit /b 1
)
node generate.js %*
if errorlevel 1 (
  echo.
  echo Generate selesai dengan error. Periksa pesan di atas.
  pause
  exit /b 1
)
echo.
echo Selesai. Tekan tombol apa saja untuk keluar...
pause >nul
