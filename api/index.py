# Vercel Configuration for 3D Asset Manager
from app import create_app

# Create the Flask app instance
app = create_app()

# This is the entry point for Vercel
if __name__ == "__main__":
    app.run(debug=False)
