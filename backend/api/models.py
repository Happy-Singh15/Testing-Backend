from django.db import models

class Url(models.Model):
    exercise = models.CharField(max_length=255)
    url = models.URLField(max_length=200)