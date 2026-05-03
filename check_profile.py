#!/usr/bin/env python
"""Check SiteProfile objects in database."""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ai_portfolio.settings')
django.setup()

from projects.models import SiteProfile

print("=" * 60)
print("SiteProfile Objects in Database")
print("=" * 60)

for p in SiteProfile.objects.all():
    print(f"\nID: {p.id}")
    print(f"Name: {p.name}")
    print(f"Profile Image: {p.profile_image}")
    print(f"Profile Image URL: {p.profile_image.url if p.profile_image else 'None'}")
    print(f"Profile Image Exists: {bool(p.profile_image)}")

print("\n" + "=" * 60)
