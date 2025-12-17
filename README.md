# Programacion1_UM_2023
# Maquetas: https://www.figma.com/file/PfUjNonVVa67pMe1g460RU/Gym-App?type=design&node-id=0%3A1&mode=design&t=a18cntue0uQJMz78-1

## Puesta en marcha del backend

El backend se puede levantar tanto en Linux como en Windows utilizando los scripts provistos en la carpeta `backend`.

### Linux / WSL

```bash
cd backend
source install.sh
source boot.sh
```

### Windows (PowerShell)

```powershell
cd backend
./install.ps1
./boot.ps1
```

### Windows (Símbolo del sistema / Visual Studio)

Si prefieres no usar PowerShell, puedes ejecutar los mismos pasos desde el símbolo del sistema (por ejemplo, la consola integrada de Visual Studio):

```cmd
cd backend
install.cmd
boot.cmd
```

Los archivos `install.cmd` y `boot.cmd` existen únicamente para quienes prefieren el símbolo del sistema en lugar de PowerShell (por ejemplo, cuando se trabaja dentro de Visual Studio). Ejecutan exactamente el mismo flujo que los scripts de PowerShell: crean el entorno virtual local, instalan las dependencias y lanzan el backend.

En todos los casos se crea un entorno virtual local `.venv`, se instalan las dependencias listadas en `requirements.txt` y se ejecuta `app.py` con la misma estructura y funcionalidades en ambos sistemas operativos.

### Variables de entorno

El backend lee las variables desde un archivo `.env` en la carpeta `backend`. Si `JWT_ACCESS_TOKEN_EXPIRES` no está definido o tiene un valor inválido, la aplicación usa un valor predeterminado de `3600` segundos para evitar errores de arranque. Un ejemplo mínimo de archivo `.env` es:

```
JWT_SECRET_KEY=una_clave_segura
JWT_ACCESS_TOKEN_EXPIRES=3600
```
