from rest_framework import generics

from .models import Url, Exercise
from .serializers import UrlSerializer, ExerciseSerializer

class UrlListCreateAPIView(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
url_list_create_view = UrlListCreateAPIView.as_view()


class ExerciseListCreateAPIView(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
exercise_list_create_view = ExerciseListCreateAPIView.as_view()
