# 3D Asset Manager - Vercel Edition

A Flask-based 3D model management platform optimized for Vercel deployment with MongoDB Atlas.

## 🔧 Technology Stack

- **Backend**: Python Flask (Serverless)
- **Database**: MongoDB Atlas (Free Tier)
- **File Storage**: MongoDB GridFS
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **3D Viewer**: Google Model-Viewer.js
- **Deployment**: Vercel

## 🚀 Quick Deployment Guide

### Prerequisites
1. Vercel account
2. MongoDB Atlas account (free tier)
3. Git repository

### Step-by-Step Deployment

1. **Setup MongoDB Atlas**
2. **Configure Environment Variables** (see SECURITY.md)
3. **Deploy with Vercel**
4. **Test Functionality**

See `VERCEL_DEPLOYMENT_GUIDE.md` for detailed instructions.

## 🔒 Security

**IMPORTANT**: This project handles sensitive data. Please read `SECURITY.md` before deployment.

### Environment Variables Required:
- `MONGODB_URI` - Your MongoDB Atlas connection string
- `SECRET_KEY` - Flask session encryption key
- `FLASK_ENV` - Application environment

### Setup:
1. Copy `.env.example` to `.env`
2. Fill in your credentials (never commit `.env`)
3. Set production variables in Vercel dashboard

**⚠️ Never commit sensitive credentials to version control**

## 📋 Features

- ✅ User Authentication with MongoDB
- ✅ 3D Model Upload/Download
- ✅ MongoDB GridFS for File Storage
- ✅ Professional 3D Model Viewer
- ✅ RESTful API
- ✅ Responsive Design
- ✅ Serverless Architecture

