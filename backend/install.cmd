@echo off
REM Uso: ejecutar en el simbolo del sistema desde la carpeta backend.
REM Equivalente a install.ps1 para quienes no usan PowerShell (ej. Visual Studio).
python -m venv .venv
call .venv\Scripts\activate.bat
pip install -r requirements.txt
