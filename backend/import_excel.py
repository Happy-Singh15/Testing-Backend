import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','home.settings')
django.setup()

import pandas as pd
from api.models import Url, Exercise

df_url = pd.read_csv('data/backend_test.csv')
df_exercise = pd.read_csv('data/filename.csv')

for _, row in df_url.iterrows():
    Url.objects.create(
        title = row['Exercise'],
        url = row['URL']
    
    )
    
for _, row in df_exercise.iterrows():
    Exercise.objects.create(
        title = row['Title'],
        exercise_type = row['Type'],
        bodypart = row['BodyPart'],
        equipment = row['Equipment'],
        level = row['Level']
    )

print('data imported Successfully')