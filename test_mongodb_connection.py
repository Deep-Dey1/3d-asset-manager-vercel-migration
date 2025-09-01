#!/usr/bin/env python3
"""
Minimal MongoDB connection test for Vercel deployment debugging
"""
import os
from urllib.parse import quote_plus
from pymongo import MongoClient

# Test different connection string formats
def test_mongodb_connection():
    print("🔌 Testing MongoDB Connection...")
    
    # Original connection string from user
    original_uri = "mongodb+srv://admin:Deep@0210@cluster0.hbtw6u0.mongodb.net/3d_asset_manager?retryWrites=true&w=majority&appName=Cluster0"
    
    # Properly URL encoded version
    password = "Deep@0210"
    encoded_password = quote_plus(password)
    encoded_uri = f"mongodb+srv://admin:{encoded_password}@cluster0.hbtw6u0.mongodb.net/3d_asset_manager?retryWrites=true&w=majority&appName=Cluster0"
    
    print(f"Original password: {password}")
    print(f"Encoded password: {encoded_password}")
    print(f"Connection URI: mongodb+srv://admin:{encoded_password}@cluster0.hbtw6u0.mongodb.net/...")
    
    # Test the connection
    try:
        print("\n🧪 Testing MongoDB connection...")
        client = MongoClient(encoded_uri, serverSelectionTimeoutMS=10000)
        
        # Test connection
        client.admin.command('ping')
        print("✅ MongoDB connection successful!")
        
        # Test database access
        db = client['3d_asset_manager']
        print(f"✅ Database '3d_asset_manager' accessible")
        
        # Test collection creation (just check, don't actually create)
        collections = db.list_collection_names()
        print(f"✅ Can list collections: {len(collections)} collections found")
        
        client.close()
        return True
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_mongodb_connection()
    
    if success:
        print("\n🎉 SUCCESS: MongoDB connection works!")
        print("📋 Use this connection string in Vercel:")
        print("MONGODB_URI=mongodb+srv://admin:Deep%400210@cluster0.hbtw6u0.mongodb.net/3d_asset_manager?retryWrites=true&w=majority&appName=Cluster0")
    else:
        print("\n❌ FAILED: Check your MongoDB Atlas configuration")
        print("📋 Troubleshooting steps:")
        print("1. Verify cluster is running")
        print("2. Check username/password")
        print("3. Verify network access (IP whitelist)")
        print("4. Check database user permissions")
