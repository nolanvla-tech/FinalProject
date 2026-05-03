#!/usr/bin/env python
"""
Script to migrate database and load initial fixtures.
Run this before starting the server in production.
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio.settings')
django.setup()

from django.core.management import call_command

def main():
    print("🔄 Running database migrations...")
    call_command('migrate')
    
    print("📦 Loading initial data...")
    fixture_path = 'projects/fixtures/projects_data.json'
    
    if os.path.exists(fixture_path):
        try:
            call_command('loaddata', fixture_path)
            print("✅ Data loaded successfully!")
        except Exception as e:
            print(f"⚠️  Error loading data: {e}")
            print("   (This is OK - you can add data via the admin panel)")
    else:
        print(f"⚠️  Fixture file not found at {fixture_path}")
        print("   (This is OK - you can add data via the admin panel)")

if __name__ == '__main__':
    main()
