from rest_framework import serializers

from .models import Exercise

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields =[
            'id',
            'title',
            'reps_sets',
            'bodypart',
            'exercise_type',
            # 'equipment',
            'level',
            'url',
      ]