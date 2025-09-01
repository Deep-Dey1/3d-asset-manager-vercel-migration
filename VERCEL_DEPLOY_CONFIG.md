# 🚀 Vercel Deployment Configuration

## 📝 Environment Variables for Vercel Dashboard

Copy these exact values to your Vercel project's environment variables:

### 1. MONGODB_URI
```
mongodb+srv://admin:Deep%400210@cluster0.hbtw6u0.mongodb.net/3d_asset_manager?retryWrites=true&w=majority&appName=Cluster0
```

### 2. SECRET_KEY
```
3d-asset-manager-vercel-super-secret-key-2025-change-this-in-production
```

### 3. FLASK_ENV
```
production
```

---

## 🔧 **Step-by-Step Vercel Deployment**

### **Step 1: Push to GitHub**
```bash
cd 3d-asset-manager-vercel-migration
git init
git add .
git commit -m "Initial commit: 3D Asset Manager with MongoDB Atlas"

# Create new repository on GitHub first, then:
git remote add origin https://github.com/Deep-Dey1/3d-asset-manager-vercel.git
git branch -M main  
git push -u origin main
```

### **Step 2: Deploy to Vercel**
1. Go to [vercel.com](https://vercel.com)
2. Click **"New Project"**
3. Import your GitHub repository: `3d-asset-manager-vercel`
4. **Framework Preset**: Other
5. Click **"Deploy"**

### **Step 3: Configure Environment Variables**
1. Go to **Project Settings** → **Environment Variables**
2. Add each variable:

**MONGODB_URI:**
```
mongodb+srv://admin:Deep%400210@cluster0.hbtw6u0.mongodb.net/3d_asset_manager?retryWrites=true&w=majority&appName=Cluster0
```

**SECRET_KEY:**
```
3d-asset-manager-vercel-super-secret-key-2025-change-this-in-production
```

**FLASK_ENV:**
```
production
```

3. Click **"Save"** for each variable

### **Step 4: Redeploy**
1. Go to **Deployments** tab
2. Click **"Redeploy"** on the latest deployment
3. Wait for successful deployment

---

## 🧪 **Testing Your Deployment**

Once deployed, test these endpoints:

### **1. Homepage**
```
https://your-project-name.vercel.app/
```

### **2. API Health Check**
```bash
curl https://your-project-name.vercel.app/api/models
```
Should return: `{"models": [], "pagination": {...}}`

### **3. Register Test User**
Visit: `https://your-project-name.vercel.app/auth/register`

### **4. Upload Test Model**
After login: `https://your-project-name.vercel.app/upload`

---

## 🔑 **Important Notes**

### **MongoDB URI Encoding**
- Password `Deep@0210` is URL-encoded as `Deep%400210`
- The `@` symbol becomes `%40` in URLs
- Database name `3d_asset_manager` is added to the path

### **Security**
- Change `SECRET_KEY` to a random 50+ character string for production
- Consider restricting MongoDB network access to Vercel IPs
- Enable MongoDB Atlas monitoring and alerts

### **Limits (Free Tier)**
- **MongoDB Atlas**: 512 MB storage, 100 connections
- **Vercel**: 100 GB bandwidth, 10 second function timeout

---

## 🎯 **Success Checklist**

- [ ] MongoDB connection tested successfully
- [ ] GitHub repository created and pushed
- [ ] Vercel project deployed
- [ ] Environment variables configured
- [ ] Homepage loads correctly
- [ ] User registration works
- [ ] File upload functional
- [ ] 3D model preview working
- [ ] API endpoints responding

---

Your 3D Asset Manager is ready for Vercel deployment! 🚀
