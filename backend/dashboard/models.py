from django.db import models

# Create your models here.
# dashboard/models.py
from django.db import models

class YouTubeVideo(models.Model):
    video_id = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=200)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    published_at = models.DateTimeField()
