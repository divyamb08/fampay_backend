from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.utils.log import get_task_logger
import yt_search.video_search


os.environ.setdefault('DJANGO_SETTINGS_MODULE','fampay_backend.settings')
app = Celery('fampay_backend')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')
app.config_from_object(settings, namespace='CELERY')

app.autodiscover_tasks()


logger = get_task_logger(__name__)
 
@app.task(bind=True)
def update_db(self):
    from yt_search.models import VideosModel
    query = settings.DEFAULT_QUERY
    videos = yt_search.video_search.video_search_func(query)
    # print(videos)
    logger.info("Successfully fetched videos")
    for item in videos:
        if VideosModel.objects.filter(title=item['title']).exists():
            continue
        else:
            video = VideosModel(title=item['title'],
                description=item['description'],
                published_on=item['published_on'],
                thumbnails_urls=item['thumbnails_urls'],
                video_link=item['video_link'])
            video.save()
    
    