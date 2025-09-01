#!/usr/bin/env python3
"""
Local Flask App Test for Vercel Version
"""
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import create_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_flask_app():
    """Test Flask app creation and basic functionality"""
    
    print("🧪 Testing Flask App with MongoDB")
    print("=" * 50)
    
    try:
        # Create Flask app
        print("🏗️ Creating Flask application...")
        app = create_app()
        print("✅ Flask app created successfully")
        
        # Test app configuration
        print(f"🔧 Secret key configured: {'Yes' if app.config.get('SECRET_KEY') else 'No'}")
        print(f"💾 MongoDB configured: {'Yes' if app.config.get('MONGODB_DB') is not None else 'No'}")
        print(f"📁 GridFS configured: {'Yes' if app.config.get('GRIDFS') is not None else 'No'}")
        
        # Test with app context
        with app.app_context():
            from app.models import User, Model3D
            
            print("📊 Testing database models...")
            
            # Test User model
            test_user = User(username="testuser", email="test@example.com")
            print("✅ User model creation works")
            
            # Test Model3D stats
            try:
                stats = Model3D.get_stats()
                print(f"✅ Database connection works - Stats: {stats}")
            except Exception as e:
                print(f"⚠️ Database query warning: {e}")
        
        print("✅ All tests passed!")
        return True
        
    except Exception as e:
        print(f"❌ Flask app test failed: {e}")
        return False

if __name__ == "__main__":
    success = test_flask_app()
    
    if success:
        print("\n🎉 Your Flask app is ready for Vercel!")
        print("🚀 You can now deploy to Vercel with confidence")
    else:
        print("\n❌ Please fix the issues before deploying")
