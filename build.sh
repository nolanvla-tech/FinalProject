#!/bin/bash
# Render build script - runs before web service starts

echo "==================================="
echo "🔨 Render Build Script"
echo "==================================="

# Install dependencies
echo "📦 Installing Python dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📦 Collecting static files..."
python manage.py collectstatic --noinput

# Initialize database (migrations + load data)
echo "🗄️  Initializing database..."
python manage.py initialize_db

echo "✅ Build complete!"
