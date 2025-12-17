@echo off
REM Uso: puede ejecutarse desde cualquier carpeta; el script se posiciona en la carpeta backend.

setlocal
pushd "%~dp0"

if not exist ".venv\Scripts\activate.bat" (
  echo [boot.cmd] No se encontro el entorno virtual. Ejecuta install.cmd primero.
  popd
  exit /b 1
)

call ".venv\Scripts\activate.bat"
python app.py

popd
endlocal
