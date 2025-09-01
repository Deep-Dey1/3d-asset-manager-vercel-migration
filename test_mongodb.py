#!/usr/bin/env python3
"""
Test MongoDB Atlas Connection
"""
import os
from pymongo import MongoClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_mongodb_connection():
    """Test MongoDB Atlas connection"""
    
    print("🧪 Testing MongoDB Atlas Connection")
    print("=" * 50)
    
    # Get connection string
    mongodb_uri = os.environ.get('MONGODB_URI')
    
    if not mongodb_uri:
        print("❌ MONGODB_URI not found in environment variables")
        return False
    
    print(f"📡 Connection String: {mongodb_uri[:50]}...")
    
    try:
        # Create MongoDB client
        print("🔗 Connecting to MongoDB Atlas...")
        client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=10000)
        
        # Test connection
        print("🏓 Testing ping...")
        client.admin.command('ping')
        print("✅ MongoDB Atlas connection successful!")
        
        # Get database
        db = client.get_database()
        print(f"📊 Database: {db.name}")
        
        # Test collections
        collections = db.list_collection_names()
        print(f"📋 Collections: {collections if collections else 'None (new database)'}")
        
        # Test insert and read
        print("🧪 Testing database operations...")
        
        # Insert test document
        test_collection = db.test_connection
        test_doc = {"test": "connection_successful", "timestamp": "2025-09-01"}
        result = test_collection.insert_one(test_doc)
        print(f"✅ Test insert successful: ID {result.inserted_id}")
        
        # Read test document
        found_doc = test_collection.find_one({"_id": result.inserted_id})
        print(f"✅ Test read successful: {found_doc['test']}")
        
        # Clean up test document
        test_collection.delete_one({"_id": result.inserted_id})
        print("🧹 Test document cleaned up")
        
        # Close connection
        client.close()
        print("✅ Connection closed successfully")
        
        return True
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False

if __name__ == "__main__":
    success = test_mongodb_connection()
    
    if success:
        print("\n🎉 MongoDB Atlas is ready for your 3D Asset Manager!")
        print("💡 You can now deploy to Vercel with confidence")
    else:
        print("\n❌ Please check your MongoDB Atlas configuration")
        print("🔧 Verify connection string and network access settings")
