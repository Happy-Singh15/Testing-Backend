from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from algoliasearch_django import raw_search



from .models import Exercise
from .serializers import ExerciseSerializer

class ExerciseListAPIView(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
exercise_list_view = ExerciseListAPIView.as_view()


class SearchView(APIView):
    def get(self, request):
        query = request.GET.get('q', '')
        results = raw_search(Exercise, query)
        return Response(results)
search_api_view = SearchView.as_view()
