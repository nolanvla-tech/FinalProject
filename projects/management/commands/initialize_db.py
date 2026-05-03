import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from projects.models import Project, SiteProfile


class Command(BaseCommand):
    help = 'Initialize database with migrations and load initial data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
        self.stdout.write(self.style.SUCCESS('🔄 Initializing database...'))
        self.stdout.write(self.style.SUCCESS('=' * 60))

        try:
            # Run migrations
            self.stdout.write('\n📍 Running database migrations...')
            call_command('migrate', '--noinput', verbosity=0)
            self.stdout.write(self.style.SUCCESS('✅ Migrations completed'))

            # Check if data already exists
            project_count = Project.objects.count()
            profile_count = SiteProfile.objects.count()

            if project_count > 0 and profile_count > 0:
                self.stdout.write(self.style.SUCCESS(f'\n✅ Database already populated:'))
                self.stdout.write(f'   - {project_count} projects found')
                self.stdout.write(f'   - {profile_count} profiles found')
                return

            # Load fixture data
            self.stdout.write('\n📍 Loading initial data...')
            fixture_path = 'projects/fixtures/projects_data.json'

            if os.path.exists(fixture_path):
                call_command('loaddata', fixture_path, verbosity=0)

                # Verify data loaded
                new_project_count = Project.objects.count()
                new_profile_count = SiteProfile.objects.count()

                self.stdout.write(self.style.SUCCESS(f'\n✅ Data loaded successfully:'))
                self.stdout.write(f'   - {new_project_count} projects loaded')
                self.stdout.write(f'   - {new_profile_count} profiles loaded')
            else:
                self.stdout.write(self.style.WARNING(f'\n⚠️  Fixture file not found'))
                self.stdout.write('   Add data via the admin panel at /admin/')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error: {e}'))
            self.stdout.write('   You can add data manually via the admin panel')

        finally:
            self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
            self.stdout.write(self.style.SUCCESS('✨ Database initialization complete!'))
            self.stdout.write(self.style.SUCCESS('=' * 60 + '\n'))
