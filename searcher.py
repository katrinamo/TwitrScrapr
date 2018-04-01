#built using guide at http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/#search
import json #for formatting the output
import time
import os
import io
import sys
import tweepy
from tweepy import OAuthHandler

name = ""



def main():
    consumer_key = CKEY
    consumer_secret = CSECRET
    access_token = ATOKEN
    access_secret = ASECRET
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #Ask what name the user wants to search for    
    name = raw_input("search query: ")
    start_time = time.time();

    location = api.geo_search(query="USA", granularity="country")
    place_id = location[0].id
    print"SEARCHING IN USA...", place_id
    
    print "Searching for", name   
    maxTweets = 2000
    f=open(name+"Tweets.txt", "w")
    tweet_out = []
    numTweets = 0

    for tweet in tweepy.Cursor(api.search, q=name + "-filter:retweets", tweet_mode="extended").items(maxTweets):
        result=tweet._json
        if (not result["retweeted"]) and ('RT @' not in result["full_text"]):
           real_name = result["user"]["name"]
           tweet_text = result["full_text"]

           tweet_out.append(real_name)
           tweet_out.append(tweet_text)
           tweet_out.append(u"\n")
        numTweets = numTweets + 1

    print"NUMBER OF TWEETS (R): ",numTweets


#    print tweet_out
    for item in tweet_out:    
        f.write(item.encode('utf-8'))
        f.write(u"\n")
    f.close()
    
main()
