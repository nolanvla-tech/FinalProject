import os
from pathlib import Path
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings
from projects.models import Project, Skill, Experience, SiteProfile


class Command(BaseCommand):
    help = 'Initialize database with migrations and sync data from fixture'

    def handle(self, *args, **options):
        self.stdout.write('=' * 60)
        self.stdout.write('Initializing database...')
        self.stdout.write('=' * 60)

        try:
            # Run migrations
            self.stdout.write('Running database migrations...')
            call_command('migrate', '--noinput', verbosity=1)
            self.stdout.write('Migrations completed')

            # Use absolute path so it works regardless of working directory
            fixture_path = Path(settings.BASE_DIR) / 'projects' / 'fixtures' / 'projects_data.json'
            self.stdout.write(f'Looking for fixture at: {fixture_path}')
            self.stdout.write(f'Fixture exists: {fixture_path.exists()}')

            if fixture_path.exists():
                self.stdout.write('Clearing existing data...')
                Project.objects.all().delete()
                Skill.objects.all().delete()
                Experience.objects.all().delete()
                SiteProfile.objects.all().delete()
                self.stdout.write('Existing data cleared')

                self.stdout.write('Loading data from fixture...')
                call_command('loaddata', str(fixture_path), verbosity=2)

                self.stdout.write(f'Data synced successfully:')
                self.stdout.write(f'  - {Project.objects.count()} projects loaded')
                self.stdout.write(f'  - {Skill.objects.count()} skills loaded')
                self.stdout.write(f'  - {Experience.objects.count()} experiences loaded')
                self.stdout.write(f'  - {SiteProfile.objects.count()} profiles loaded')
            else:
                self.stdout.write('ERROR: Fixture file not found!')
                raise FileNotFoundError(f'Fixture not found at {fixture_path}')

        except Exception as e:
            self.stdout.write(f'ERROR: {e}')
            raise

        finally:
            self.stdout.write('=' * 60)
            self.stdout.write('Database initialization complete!')
            self.stdout.write('=' * 60)
