from enum import unique
from django.db import models

# Create your models here.

class VideosModel(models.Model):
    title = models.CharField("Video Title",max_length=255)
    description = models.CharField("Description",max_length=500)
    published_on = models.DateTimeField("Publishing datetime")
    thumbnails_urls = models.URLField("Thumbnail URLs",max_length=255)
    video_link = models.URLField("Video Link",max_length=255)
    
    class Meta:
        ordering = ["-published_on"]
        db_table = "Videos Database"
        # unique_together = [['title','description']]