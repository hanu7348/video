# dashboard/views.py
from rest_framework import viewsets
from .models import YouTubeVideo
from .serializers import YouTubeVideoSerializer

class YouTubeVideoViewSet(viewsets.ModelViewSet):
    queryset = YouTubeVideo.objects.all()
    serializer_class = YouTubeVideoSerializer
