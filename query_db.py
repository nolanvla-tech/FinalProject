from projects.models import SiteProfile
for p in SiteProfile.objects.all():
    print(f"ID: {p.id}, Name: {p.name}, Profile Image: {p.profile_image}")
