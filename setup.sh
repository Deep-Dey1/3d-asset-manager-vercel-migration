#!/bin/bash

# 3D Asset Manager - Vercel Quick Setup Script

echo "🚀 3D Asset Manager - Vercel Deployment Setup"
echo "=============================================="

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit: 3D Asset Manager Vercel version"
else
    echo "✅ Git repository already initialized"
fi

# Create .env file from template
if [ ! -f ".env" ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your MongoDB Atlas connection string"
else
    echo "✅ .env file already exists"
fi

echo ""
echo "🔧 Next Steps:"
echo "1. Edit .env file with your MongoDB Atlas URI"
echo "2. Push to GitHub repository"
echo "3. Deploy to Vercel"
echo "4. Configure environment variables in Vercel dashboard"
echo ""
echo "📚 See VERCEL_DEPLOYMENT_GUIDE.md for detailed instructions"
