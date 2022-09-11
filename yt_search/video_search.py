
from django.conf import settings
from isodate import parse_duration
from dateutil import parser
from datetime import datetime, timedelta
import requests

def video_search_func(video_query):
    try:
        videos = []
        # if request.method=='POST':
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'
        
        timestamp = (
            datetime.now() - timedelta(minutes=1)
        ).isoformat() + "Z"
        
        search_params = {
            'part':'snippet',
            'q':video_query,
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults' : 12,
            'order':"date",
            'publishedAfter':timestamp,
            'type':'video'
            
        }
        
        video_ids = []
        r = requests.get(search_url, params=search_params)
        # print(r.text)
        results = r.json()['items']
        
        for result in results:
            video_ids.append(result['id']['videoId'])
        
        
            
        video_params = {
            'key':settings.YOUTUBE_DATA_API_KEY,
            'part':'snippet,contentDetails',
            'id':','.join(video_ids),
            'order':"date",
            'publishedAfter':timestamp,
            'maxResults':12
        }
        r = requests.get(video_url, params=video_params)
        video_results = r.json()['items']
        videos = []
        # video_titles = []
        # video_video_ids = []
        # video_duration = []
        # video_thumbnails = []
        for result in video_results:
            # video_titles.append(result['snippet']['title'])
            # video_video_ids.append(result['id'])
            # video_duration.append(parse_duration(result['contentDetails']['duration']).total_seconds())
            # video_thumbnails.append(result['snippet']['thumbnails']['high']['url'])
            video_data = {
                'title': result['snippet']['title'],
                'id': result['id'],
                'description':result['snippet']['description'],
                'published_on':(result['snippet']['publishedAt']),
                'video_link':f'https://www.youtube.com/watch?v={result["id"]}',
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds()//60),
                'thumbnails_urls': result['snippet']['thumbnails']['high']['url'],
            }
            videos.append(video_data)
        print('Working fine')
            
        return videos
    except:
        print('An error occurred')
          