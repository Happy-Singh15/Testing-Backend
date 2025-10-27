import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','home.settings')
django.setup()

import pandas as pd
from api.models import Url

df = pd.read_csv('../data/backend_test.csv')
print(df)

for _, row in df.iterrows():
    Url.objects.create(
        exercise = row['Exercise'],
        url = row['URL']
    )

print('data imported Successfully')