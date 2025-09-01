#!/usr/bin/env python3
"""
Simple Flask App Test - Vercel Ready
"""
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_imports():
    """Test all required imports"""
    print("📦 Testing Python imports...")
    
    try:
        import pymongo
        print("✅ PyMongo imported")
        
        import gridfs
        print("✅ GridFS imported")
        
        import flask
        print("✅ Flask imported")
        
        import flask_login
        print("✅ Flask-Login imported")
        
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_mongodb_basic():
    """Test basic MongoDB connection"""
    print("🔗 Testing MongoDB connection...")
    
    try:
        from pymongo import MongoClient
        import gridfs
        
        mongodb_uri = os.environ.get('MONGODB_URI')
        if not mongodb_uri:
            print("❌ MONGODB_URI not found")
            return False
            
        client = MongoClient(mongodb_uri, serverSelectionTimeoutMS=5000)
        client.admin.command('ping')
        
        # Test database access
        db = client['3d_asset_manager']
        fs = gridfs.GridFS(db)
        
        print("✅ MongoDB connection successful")
        print("✅ GridFS initialized")
        
        client.close()
        return True
        
    except Exception as e:
        print(f"❌ MongoDB error: {e}")
        return False

def test_flask_minimal():
    """Test minimal Flask app creation"""
    print("🏗️ Testing Flask app creation...")
    
    try:
        from flask import Flask
        from flask_login import LoginManager
        
        app = Flask(__name__)
        app.config['SECRET_KEY'] = 'test-key'
        
        login_manager = LoginManager()
        login_manager.init_app(app)
        
        @app.route('/')
        def home():
            return "Hello from 3D Asset Manager!"
        
        print("✅ Flask app created successfully")
        return True
        
    except Exception as e:
        print(f"❌ Flask error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Vercel Deployment Readiness Test")
    print("=" * 50)
    
    tests = [
        ("Python Imports", test_imports),
        ("MongoDB Connection", test_mongodb_basic), 
        ("Flask App", test_flask_minimal)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        result = test_func()
        results.append(result)
    
    print("\n" + "=" * 50)
    print("🎯 TEST RESULTS:")
    
    all_passed = all(results)
    
    for i, (test_name, _) in enumerate(tests):
        status = "✅ PASS" if results[i] else "❌ FAIL"
        print(f"  {test_name}: {status}")
    
    if all_passed:
        print("\n🎉 ALL TESTS PASSED!")
        print("🚀 Your app is ready for Vercel deployment!")
        print("\n📋 Next steps:")
        print("1. Push to GitHub")
        print("2. Deploy to Vercel") 
        print("3. Configure environment variables")
        print("4. Test live deployment")
    else:
        print("\n❌ Some tests failed")
        print("🔧 Please fix issues before deploying")
    
    return all_passed

if __name__ == "__main__":
    main()
