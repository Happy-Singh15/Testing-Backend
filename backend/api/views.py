from rest_framework import generics

from .models import Url
from .serializers import UrlSerializer

class UrlListCreateAPIView(generics.ListCreateAPIView):
    queryset = Url.objects.all()
    serializer_class = UrlSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)
    
url_list_create_view = UrlListCreateAPIView.as_view()
