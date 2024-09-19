# backend/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dashboard.views import YouTubeVideoViewSet

router = DefaultRouter()
router.register(r'videos', YouTubeVideoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]