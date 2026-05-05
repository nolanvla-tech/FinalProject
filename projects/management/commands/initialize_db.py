import os
from django.core.management.base import BaseCommand
from django.core.management import call_command
from projects.models import Project, Skill, Experience, SiteProfile


class Command(BaseCommand):
    help = 'Initialize database with migrations and sync data from fixture'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
        self.stdout.write(self.style.SUCCESS('🔄 Initializing database...'))
        self.stdout.write(self.style.SUCCESS('=' * 60))

        try:
            # Run migrations
            self.stdout.write('\n📍 Running database migrations...')
            call_command('migrate', '--noinput', verbosity=0)
            self.stdout.write(self.style.SUCCESS('✅ Migrations completed'))

            # Always clear and reload from fixture to keep Render in sync
            fixture_path = 'projects/fixtures/projects_data.json'

            if os.path.exists(fixture_path):
                self.stdout.write('\n📍 Clearing existing data...')
                Project.objects.all().delete()
                Skill.objects.all().delete()
                Experience.objects.all().delete()
                SiteProfile.objects.all().delete()
                self.stdout.write(self.style.SUCCESS('✅ Existing data cleared'))

                self.stdout.write('\n📍 Loading data from fixture...')
                call_command('loaddata', fixture_path, verbosity=0)

                self.stdout.write(self.style.SUCCESS(f'\n✅ Data synced successfully:'))
                self.stdout.write(f'   - {Project.objects.count()} projects loaded')
                self.stdout.write(f'   - {Skill.objects.count()} skills loaded')
                self.stdout.write(f'   - {Experience.objects.count()} experiences loaded')
                self.stdout.write(f'   - {SiteProfile.objects.count()} profiles loaded')
            else:
                self.stdout.write(self.style.WARNING(f'\n⚠️  Fixture file not found'))
                self.stdout.write('   Add data via the admin panel at /admin/')

        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error: {e}'))
            raise

        finally:
            self.stdout.write(self.style.SUCCESS('\n' + '=' * 60))
            self.stdout.write(self.style.SUCCESS('✨ Database initialization complete!'))
            self.stdout.write(self.style.SUCCESS('=' * 60 + '\n'))
