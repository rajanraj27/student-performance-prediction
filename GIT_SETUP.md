# Git & GitHub Setup Guide

## Step 1: Install Git

### For Windows:
1. Download Git from: https://git-scm.com/download/win
2. Run the installer with default settings
3. Restart your terminal/VS Code after installation

### Verify Installation:
```bash
git --version
```

## Step 2: Configure Git (First Time Only)

```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

## Step 3: Initialize Git Repository

Navigate to your project folder and run:

```bash
cd "D:\project 3\Minnor Project\student-performance-prediction"
git init
```

## Step 4: Add All Files

```bash
git add .
```

## Step 5: Create First Commit

```bash
git commit -m "Initial commit: Student Performance Prediction System with ML"
```

## Step 6: Create GitHub Repository

1. Go to https://github.com
2. Click the "+" icon in the top right
3. Select "New repository"
4. Name it: `student-performance-prediction`
5. Description: "Flask-based ML application for predicting student final exam scores using Linear Regression"
6. Choose Public or Private
7. **DO NOT** initialize with README, .gitignore, or license (we already have these)
8. Click "Create repository"

## Step 7: Connect Local Repository to GitHub

After creating the repository, GitHub will show you commands. Use these:

```bash
git remote add origin https://github.com/YOUR_USERNAME/student-performance-prediction.git
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

## Step 8: Push Your Code

```bash
git push -u origin main
```

## Alternative: Using GitHub Desktop (Easier)

If you prefer a GUI:
1. Download GitHub Desktop: https://desktop.github.com/
2. Sign in with your GitHub account
3. File → Add Local Repository
4. Select your project folder
5. Click "Publish repository" button

## Troubleshooting

### If you get authentication error:
Use GitHub Personal Access Token:
1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Generate new token with `repo` permissions
3. Use token as password when pushing

### If repository already exists on GitHub:
```bash
git remote add origin https://github.com/YOUR_USERNAME/student-performance-prediction.git
git pull origin main --allow-unrelated-histories
git push -u origin main
```
