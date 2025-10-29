from django.db import models

class Url(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200)

class Exercise(models.Model):
    title = models.CharField(max_length=255)
    exercise_type = models.CharField(max_length=255)
    bodypart = models.CharField(max_length=255)
    equipment = models.CharField(max_length=255)
    level = models.CharField(max_length=255)