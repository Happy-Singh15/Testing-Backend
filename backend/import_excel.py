import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','home.settings')
django.setup()

from django.db import transaction
import pandas as pd
from api.models import Exercise

df_exercise = pd.read_csv('data/Exercise__data.csv')
print(f"Total rows to import: {len(df_exercise)}")

count = 0
with transaction.atomic():
    for _, row in df_exercise.iterrows():
        Exercise.objects.create(
            title = row['Exercise_name'],
            reps_sets = row['Exercise_count'],
            exercise_type = row['Type'],
            bodypart = row['Bodypart'],
            # equipment = row['Equipment'],
            level = row['Level'],
            url = row['YouTube Link'],
        )
        count += 1
        if count % 10 == 0:  # print every 100 rows
            print(f"Imported {count} rows...")

print("Import completed.")
