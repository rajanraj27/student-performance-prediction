@echo off
echo ========================================
echo Git Repository Setup Script
echo ========================================
echo.

REM Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed!
    echo Please install Git from: https://git-scm.com/download/win
    echo Then run this script again.
    pause
    exit /b 1
)

echo [1/5] Git is installed. Version:
git --version
echo.

echo [2/5] Initializing git repository...
git init
if errorlevel 1 (
    echo ERROR: Failed to initialize git repository
    pause
    exit /b 1
)
echo ✓ Repository initialized
echo.

echo [3/5] Adding all files...
git add .
if errorlevel 1 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)
echo ✓ Files added
echo.

echo [4/5] Creating initial commit...
git commit -m "Initial commit: Student Performance Prediction System with ML"
if errorlevel 1 (
    echo ERROR: Failed to create commit
    echo Note: You may need to configure git first:
    echo   git config --global user.name "Your Name"
    echo   git config --global user.email "your.email@example.com"
    pause
    exit /b 1
)
echo ✓ Commit created
echo.

echo [5/5] Setup complete!
echo.
echo ========================================
echo Next Steps:
echo ========================================
echo 1. Create a repository on GitHub.com
echo 2. Run these commands (replace YOUR_USERNAME):
echo.
echo    git remote add origin https://github.com/YOUR_USERNAME/student-performance-prediction.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo Or follow the detailed guide in GIT_SETUP.md
echo ========================================
pause
