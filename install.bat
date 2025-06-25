@echo off
echo 🚀 Installing Cursor Unlimited Tool Calls (CUTC)
echo --------------------------------------------------

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python from https://python.org
    pause
    exit /b 1
)

REM Run the Python installation script
python install.py

echo.
echo 🎉 Installation completed!
echo.
echo 📋 Next steps:
echo 1. Restart Cursor IDE
echo 2. Verify that CUTC rules are active
echo 3. Use Agent Mode to get started
echo.
pause 