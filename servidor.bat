@echo off
REM Script para iniciar el servidor en Windows
echo Iniciando servidor del Sistema de Viaticos...
echo.

REM Verificar si Python esta instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado o no esta en el PATH
    echo Por favor instala Python desde https://www.python.org/
    pause
    exit /b 1
)

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Ejecutar el servidor
python servidor.py

pause
