#!/usr/bin/env python3
"""
Quick test to verify the Flask app can be created successfully for Vercel deployment
"""
import os
import sys

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

print("🧪 Testing Flask App Creation for Vercel...")

try:
    # Test 1: Import the create_app function
    print("✅ Step 1: Testing imports...")
    from app import create_app
    print("   ✓ Successfully imported create_app")
    
    # Test 2: Create the app instance
    print("✅ Step 2: Creating Flask app...")
    app = create_app()
    print("   ✓ Successfully created Flask app")
    
    # Test 3: Check app configuration
    print("✅ Step 3: Checking app configuration...")
    print(f"   ✓ App name: {app.name}")
    print(f"   ✓ Debug mode: {app.debug}")
    print(f"   ✓ Environment: {app.config.get('ENV', 'Not set')}")
    
    # Test 4: Check MongoDB configuration
    print("✅ Step 4: Checking MongoDB configuration...")
    mongodb_uri = app.config.get('MONGODB_URI')
    if mongodb_uri:
        print("   ✓ MongoDB URI configured")
        # Don't print the full URI for security
        print(f"   ✓ MongoDB URI starts with: {mongodb_uri[:20]}...")
    else:
        print("   ⚠️  MongoDB URI not configured (this is expected in test)")
    
    # Test 5: Check routes
    print("✅ Step 5: Checking routes...")
    routes = [rule.rule for rule in app.url_map.iter_rules()]
    print(f"   ✓ Found {len(routes)} routes:")
    for route in routes[:5]:  # Show first 5 routes
        print(f"      - {route}")
    if len(routes) > 5:
        print(f"      ... and {len(routes) - 5} more")
    
    print("\n🎉 SUCCESS: Flask app is ready for Vercel deployment!")
    print("📋 Next Steps:")
    print("   1. Push these changes to GitHub")
    print("   2. Redeploy in Vercel dashboard")
    print("   3. Check build logs for any remaining issues")
    
except ImportError as e:
    print(f"❌ IMPORT ERROR: {e}")
    print("   Check that all dependencies are installed")
    print("   Check that all Python files are present")
    
except Exception as e:
    print(f"❌ APPLICATION ERROR: {e}")
    print("   Check environment variables")
    print("   Check MongoDB connection string")
    print("   Check application configuration")

print("\n" + "="*50)
