@echo off
REM Diretório onde está o seu projeto
set "PROJECT_DIR=%~dp0"

REM Diretório do ambiente virtual
set "VENV_DIR=%PROJECT_DIR%venv\Scripts"

REM Diretório do script Python
set "SCRIPT_PATH=%PROJECT_DIR%main.py"  REM Aqui, coloque o nome correto do seu script

REM Checar se o ambiente virtual existe e ativar
if exist "%VENV_DIR%\activate.bat" (
    call "%VENV_DIR%\activate.bat"
) else (
    echo O ambiente virtual nao foi encontrado.
    exit /b 1
)

REM Executar o script Python
python "%SCRIPT_PATH%"

REM Desativar o ambiente virtual
if exist "%VENV_DIR%\deactivate.bat" (
    call "%VENV_DIR%\deactivate.bat"
)

echo Script executado com sucesso.
pause
