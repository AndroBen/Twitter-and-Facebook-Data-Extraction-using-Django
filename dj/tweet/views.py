from django.shortcuts import render
from django.http import HttpResponse
import tweepy
import pandas as pd
# Create your views here.
def tw(request):
    return render(request,'twname.html')

def twit(request):
    username=request.GET['name']
    consumer_key = ""
    consumer_secret = ""
    access_key = ""
    access_secret = ""
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    number_of_tweets=10
    tweets=tweepy.Cursor(api.search_tweets,q=username,lang="en").items(10) 
    users_locs=[[tweet.user.screen_name,tweet.text]for tweet in tweets] 
    #A List of Tweet Data (pandas) 
    tweet_text=pd.DataFrame(data=users_locs,columns=['USERS','TWEETS'])

    return HttpResponse(f'''
    <html>
    <head></head>
    <body bgcolor="turquoise">
    {tweet_text.to_html()}
    </body>
    </html>''') 
