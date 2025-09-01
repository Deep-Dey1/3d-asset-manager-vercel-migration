@echo off
echo 🚀 3D Asset Manager - Vercel Deployment Setup
echo ==============================================

REM Check if git is initialized
if not exist ".git" (
    echo 📦 Initializing Git repository...
    git init
    git add .
    git commit -m "Initial commit: 3D Asset Manager Vercel version"
) else (
    echo ✅ Git repository already initialized
)

REM Create .env file from template
if not exist ".env" (
    echo 📝 Creating .env file from template...
    copy .env.example .env
    echo ⚠️  Please edit .env file with your MongoDB Atlas connection string
) else (
    echo ✅ .env file already exists
)

echo.
echo 🔧 Next Steps:
echo 1. Edit .env file with your MongoDB Atlas URI
echo 2. Push to GitHub repository  
echo 3. Deploy to Vercel
echo 4. Configure environment variables in Vercel dashboard
echo.
echo 📚 See VERCEL_DEPLOYMENT_GUIDE.md for detailed instructions

pause
