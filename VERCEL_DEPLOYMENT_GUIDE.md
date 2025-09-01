# 🚀 Vercel Deployment Guide - 3D Asset Manager with MongoDB

## 📋 **Complete Step-by-Step Guide**

### **Phase 1: MongoDB Atlas Setup (Free Tier)**

#### **Step 1.1: Create MongoDB Atlas Account**
1. Go to [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Click **"Try Free"**
3. Sign up with email or Google account
4. Verify your email address

#### **Step 1.2: Create Free Cluster**
1. **Choose Deployment Type**: Select **"Shared"** (Free tier)
2. **Cloud Provider**: Choose **"AWS"** (recommended)
3. **Region**: Select closest to your users (e.g., US East Virginia)
4. **Cluster Name**: `3d-asset-manager-cluster`
5. Click **"Create Cluster"** (takes 3-5 minutes)

#### **Step 1.3: Create Database User**
1. Go to **"Database Access"** in left sidebar
2. Click **"Add New Database User"**
3. **Authentication Method**: Password
4. **Username**: `3d-admin` (or your choice)
5. **Password**: Generate secure password (save it!)
6. **Database User Privileges**: Select **"Read and write to any database"**
7. Click **"Add User"**

#### **Step 1.4: Configure Network Access**
1. Go to **"Network Access"** in left sidebar
2. Click **"Add IP Address"**
3. Select **"Allow Access from Anywhere"** (0.0.0.0/0)
   - *Note: For production, restrict to specific IPs*
4. Click **"Confirm"**

#### **Step 1.5: Get Connection String**
1. Go to **"Clusters"** → Click **"Connect"**
2. Choose **"Connect your application"**
3. **Driver**: Python, **Version**: 3.6 or later
4. Copy the connection string:
   ```
   mongodb+srv://<username>:<password>@3d-asset-manager-cluster.xxxxx.mongodb.net/?retryWrites=true&w=majority
   ```
5. Replace `<username>` and `<password>` with your actual credentials
6. Add database name: `/3d_asset_manager` before the `?`

**Final MongoDB URI Example:**
```
mongodb+srv://3d-admin:yourpassword@3d-asset-manager-cluster.xxxxx.mongodb.net/3d_asset_manager?retryWrites=true&w=majority
```

---

### **Phase 2: Vercel Deployment**

#### **Step 2.1: Prepare Repository**
1. **Initialize Git** (if not already done):
   ```bash
   cd 3d-asset-manager-vercel-migration
   git init
   git add .
   git commit -m "Initial Vercel deployment setup"
   ```

2. **Push to GitHub**:
   ```bash
   # Create new repository on GitHub first
   git remote add origin https://github.com/yourusername/3d-asset-manager-vercel.git
   git branch -M main
   git push -u origin main
   ```

#### **Step 2.2: Deploy to Vercel**
1. Go to [https://vercel.com](https://vercel.com)
2. Sign up/Login with GitHub account
3. Click **"New Project"**
4. **Import Git Repository**: Select your `3d-asset-manager-vercel` repo
5. **Configure Project**:
   - **Framework Preset**: Other
   - **Root Directory**: `./` (default)
   - **Build Command**: (leave empty)
   - **Output Directory**: (leave empty)
6. Click **"Deploy"**

#### **Step 2.3: Configure Environment Variables**
1. Go to **Project Settings** → **Environment Variables**
2. Add the following variables:

**Required Variables:**
```bash
# Variable Name: MONGODB_URI
# Value: mongodb+srv://3d-admin:yourpassword@3d-asset-manager-cluster.xxxxx.mongodb.net/3d_asset_manager?retryWrites=true&w=majority

# Variable Name: SECRET_KEY  
# Value: your-super-secret-random-string-here-make-it-long-and-complex

# Variable Name: FLASK_ENV
# Value: production
```

3. Click **"Save"** for each variable
4. **Redeploy** the project (Vercel → Deployments → Click "Redeploy")

---

### **Phase 3: Testing & Verification**

#### **Step 3.1: Verify Deployment**
1. **Check Vercel URL**: `https://your-project-name.vercel.app`
2. **Test Homepage**: Should load with 3D Asset Manager interface
3. **Check Logs**: Vercel Dashboard → Functions → View logs for any errors

#### **Step 3.2: Test Core Functionality**
```bash
# Test API endpoint
curl https://your-project-name.vercel.app/api/models

# Should return: {"models": [], "pagination": {...}}
```

#### **Step 3.3: Full Feature Testing**
1. **Registration**: Create a test account
2. **Login**: Test authentication
3. **Upload**: Try uploading a small 3D model
4. **Browse**: Check if models appear
5. **Download**: Test file download
6. **3D Preview**: Verify model viewer works

---

### **Phase 4: Production Optimization**

#### **Step 4.1: MongoDB Optimization**
1. **Indexes**: Automatically created by the app
2. **Connection Pooling**: Configured in the app
3. **Performance Monitoring**: MongoDB Atlas → Metrics

#### **Step 4.2: Vercel Optimization**
1. **Custom Domain** (optional):
   - Vercel Dashboard → Settings → Domains
   - Add your custom domain
2. **Function Timeout**: Already set to 30s max
3. **Error Monitoring**: Check Function logs regularly

---

## 🔧 **Configuration Files Overview**

### **Vercel Configuration (`vercel.json`)**
```json
{
  "version": 2,
  "builds": [{"src": "api/index.py", "use": "@vercel/python"}],
  "routes": [{"src": "/(.*)", "dest": "api/index.py"}]
}
```

### **Python Dependencies (`requirements.txt`)**
```
Flask==3.0.0
pymongo==4.6.1
flask-login==0.6.3
werkzeug==3.0.1
python-dotenv==1.0.0
dnspython==2.4.2
```

### **Entry Point (`api/index.py`)**
- Serverless function entry point
- Creates Flask app instance
- Handles all routes

---

## 🐛 **Troubleshooting Common Issues**

### **Issue 1: "Module not found" errors**
**Solution**: Check `requirements.txt` and redeploy

### **Issue 2: MongoDB connection timeout**
**Solution**: 
- Verify connection string format
- Check Network Access settings in MongoDB Atlas
- Ensure IP 0.0.0.0/0 is whitelisted

### **Issue 3: File upload failures**
**Solution**: GridFS is used for file storage in MongoDB

### **Issue 4: 3D Models not loading**
**Solution**: Check CORS headers and file MIME types

---

## 📊 **MongoDB Free Tier Limits**
- **Storage**: 512 MB
- **RAM**: Shared
- **Connections**: 500 concurrent
- **Bandwidth**: No specific limit
- **Duration**: Forever free

---

## 🎯 **Success Criteria**
✅ MongoDB Atlas cluster created and accessible  
✅ Vercel deployment successful  
✅ Environment variables configured  
✅ User registration/login working  
✅ File upload to GridFS working  
✅ 3D model preview functional  
✅ API endpoints responding  
✅ Download functionality working  

---

## 🔗 **Important URLs**
- **MongoDB Atlas**: https://cloud.mongodb.com
- **Vercel Dashboard**: https://vercel.com/dashboard
- **Your Live Site**: `https://your-project-name.vercel.app`

---

## 🎉 **Post-Deployment**
Once deployed successfully, you'll have:
- Professional 3D asset management platform
- MongoDB Atlas database (free tier)
- Serverless hosting on Vercel
- Global CDN distribution
- HTTPS enabled by default
- Automatic deployments from Git

**Total Cost: $0** (using free tiers of both services)
