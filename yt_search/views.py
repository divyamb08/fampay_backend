from django.shortcuts import render
import requests
import datetime
from django.http import HttpResponse
from django.conf import settings
from isodate import parse_duration
from datetime import datetime, timedelta
from . import video_search
from rest_framework.decorators import api_view
import time
from rest_framework import status
from rest_framework.response import Response
from yt_search.models import VideosModel
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView




query = settings.DEFAULT_QUERY



def index(request):
    
    if len(VideosModel.objects.all()) == 0:
        videos = video_search.video_search_func(query)
        
    else:  
        videos = VideosModel.objects.all()[:12]
    

    context = {
        'videos': videos, 
    }
        
    return render(request, 'search/index.html',context)
