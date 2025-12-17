# Puede ejecutarse desde cualquier carpeta; el script se posiciona en la carpeta backend.

$here = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
Set-Location -Path $here

$activate = Join-Path $here ".venv/Scripts/Activate.ps1"
if (-not (Test-Path $activate)) {
    Write-Error "[boot.ps1] No se encontro el entorno virtual. Ejecuta install.ps1 primero." -ErrorAction Stop
}

. $activate
python app.py
