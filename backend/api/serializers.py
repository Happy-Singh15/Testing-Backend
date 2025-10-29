from rest_framework import serializers

from .models import Url, Exercise

class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields=[
            'id',
            'title',
            'url',
        ]

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields =[
            'id',
            'title',
            'exercise_type',
            'bodypart',
            'equipment',
            'level',
      ]