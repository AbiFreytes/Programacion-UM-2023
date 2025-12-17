# Ejecutar en PowerShell: .\\install.ps1

$here = Split-Path -Path $MyInvocation.MyCommand.Path -Parent
Set-Location -Path $here

python -m venv .venv
$activate = Join-Path $here ".venv/Scripts/Activate.ps1"

if (-not (Test-Path $activate)) {
    Write-Error "[install.ps1] No se pudo crear el entorno virtual. Verifica que Python este instalado y vuelve a intentarlo." -ErrorAction Stop
}

. $activate
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
