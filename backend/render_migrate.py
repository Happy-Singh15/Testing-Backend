import os
import django

# Make sure this matches your settings.py path
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.home.settings')

django.setup()

from django.core.management import call_command

call_command('migrate')
print("✅ Migrations completed successfully.")
