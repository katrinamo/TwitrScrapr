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
    access_token =  ATOKEN
    access_secret = ASECRET
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #Ask what name the user wants to search for    
    name = raw_input("Accused name: ")
    start_time = time.time();

    #search for accuser + rape
    rape_search = name + " rape"
    sexAssault_search = name + " sexual assault"

    search_tot = rape_search + " " + sexAssault_search

    location = api.geo_search(query="USA", granularity="country")
    place_id = location[0].id
    print"SEARCHING IN USA...", place_id
    print"Searching for", rape_search,",", search_tot
    
    maxTweets = 500
    f=open(name+"_rape_raw_tweets.json", "w")
    tweet_out = []
    numTweets = 0

    for tweet in tweepy.Cursor(api.search, q=rape_search + "-filter:retweets").items(maxTweets):
        result=tweet._json
        if (not result["retweeted"]) and ('RT @' not in result["text"]):
           screen_name = result["user"]["screen_name"]
           real_name = result["user"]["name"]
           prof_pic = result["user"]["profile_image_url_https"]
           tweet_text = result["text"]

           tweet_out.append(screen_name)
           tweet_out.append(real_name)
           tweet_out.append(prof_pic)
           tweet_out.append(tweet_text)
           tweet_out.append(u"\n")
           numTweets = numTweets + 1

    print"NUMBER OF TWEETS (R): ",numTweets

    for item in tweet_out:    
        f.write(item.encode('utf-8'))
        f.write(u"\n")
    f.close()

    maxTweets = 500
    f2=open(name+"_sexAssault_raw_tweets.json", "w")
    tweet_out1 = []
    numTweets = 0
    for tweet in tweepy.Cursor(api.search, q=sexAssault_search + "-filter:retweets").items(maxTweets):
        result=tweet._json
        if (not result["retweeted"]) and ('RT @' not in result["text"]):
           screen_name = result["user"]["screen_name"]
           real_name = result["user"]["name"]
           prof_pic = result["user"]["profile_image_url_https"]
           tweet_text = result["text"]

           tweet_out1.append(screen_name)
           tweet_out1.append(real_name)
           tweet_out1.append(prof_pic)
           tweet_out1.append(tweet_text)
           tweet_out1.append(u"\n")
           numTweets = numTweets + 1

    print"NUMBER OF TWEETS (SA): ",numTweets

    for item in tweet_out1:    
        f2.write(item.encode('utf-8'))
        f2.write(u"\n")
    f2.close()

    
main()
