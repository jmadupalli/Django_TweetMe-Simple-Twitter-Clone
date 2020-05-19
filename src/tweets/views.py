from django.shortcuts import render
from django.http import HttpResponse
from .models import Tweet
# Create your views here.
def home_view(request, *args, **kwargs):
    return HttpResponse('Hello')

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    obj = Tweet.objects.get(id=tweet_id)
    return HttpResponse('<h1>Hello, '+str(tweet_id)+'</h1>')