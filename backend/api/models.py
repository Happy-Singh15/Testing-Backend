from django.db import models

class Exercise(models.Model):
    title = models.CharField(max_length=120)
    reps_sets = models.CharField(max_length=50)
    exercise_type = models.CharField(max_length=50)
    bodypart = models.CharField(max_length=20)
    # equipment = models.CharField(max_length=255)
    level = models.CharField(max_length=20)
    url = models.URLField(max_length=200)