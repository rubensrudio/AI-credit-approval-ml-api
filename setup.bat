@echo off
echo =========================================
echo   Credit Approval ML API - Setup (Windows)
echo =========================================
echo.

:: Create .env if not exists
if not exist ".env" (
    copy .env.example .env
    echo [OK] .env file created
) else (
    echo [OK] .env file already exists
)

:: Create virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo [OK] Virtual environment already exists
)

:: Activate and install
call venv\Scripts\activate.bat

echo Installing dependencies...
python -m pip install -r requirements.txt

echo Installing project in editable mode...
python -m pip install -e ".[dev]"

echo.
echo =========================================
echo   Installation complete!
echo =========================================
echo.
echo Next steps:
echo   1. Activate:  call venv\Scripts\activate.bat
echo   2. Train:     python -c "from scripts.train_model import main; main()"
echo   3. Run API:   uvicorn src.api.main:app --reload
echo.
pause
