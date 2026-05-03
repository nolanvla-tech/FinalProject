#!/usr/bin/env python
"""
Script to run migrations and load initial data for Render deployment.
This is called before the web server starts.
"""
import os
import sys
import django
from pathlib import Path

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio.settings')
django.setup()

from django.core.management import call_command
from projects.models import Project, SiteProfile

def main():
    print("=" * 60)
    print("🔄 Initializing database for deployment...")
    print("=" * 60)
    
    try:
        # Run migrations
        print("\n📍 Step 1: Running database migrations...")
        call_command('migrate', '--noinput', verbosity=1)
        print("✅ Migrations completed")
    except Exception as e:
        print(f"❌ Migration error: {e}")
        return False
    
    try:
        # Check if data already exists
        project_count = Project.objects.count()
        profile_count = SiteProfile.objects.count()
        
        if project_count > 0 and profile_count > 0:
            print(f"\n✅ Database already populated:")
            print(f"   - {project_count} projects found")
            print(f"   - {profile_count} profiles found")
            return True
        
        # Load fixture data
        print("\n📍 Step 2: Loading initial data from fixture...")
        fixture_path = 'projects/fixtures/projects_data.json'
        
        if os.path.exists(fixture_path):
            call_command('loaddata', fixture_path, verbosity=1)
            
            # Verify data loaded
            new_project_count = Project.objects.count()
            new_profile_count = SiteProfile.objects.count()
            
            print(f"\n✅ Data loaded successfully:")
            print(f"   - {new_project_count} projects loaded")
            print(f"   - {new_profile_count} profiles loaded")
            return True
        else:
            print(f"⚠️  Fixture file not found: {fixture_path}")
            print("   You can add data via the admin panel at /admin/")
            return True
            
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        print("   You can add data manually via the admin panel at /admin/")
        return True
    finally:
        print("\n" + "=" * 60)
        print("✨ Database initialization complete!")
        print("=" * 60)

if __name__ == '__main__':
    success = main()
    sys.exit(0 if success else 1)

