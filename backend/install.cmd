@echo off
REM Uso: puede ejecutarse desde cualquier carpeta; el script se posiciona en la carpeta backend.
REM Equivalente a install.ps1 para quienes no usan PowerShell (ej. Visual Studio).

setlocal
pushd "%~dp0"

python -m venv .venv
if not exist ".venv\Scripts\activate.bat" (
  echo [install.cmd] No se pudo crear el entorno virtual. Verifica que Python este instalado y vuelve a intentarlo.
  popd
  exit /b 1
)

call ".venv\Scripts\activate.bat"
pip install -r requirements.txt

popd
endlocal
