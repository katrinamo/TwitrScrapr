#built using guide at http://www.dealingdata.net/2016/07/23/PoGo-Series-Tweepy/#search
import json #for formatting the output
import time
import os
import io
import sys
import tweepy
from tweepy import OAuthHandler




def main():

    consumer_key = CKEY
    consumer_secret = CSECRET
    access_token = ATOKEN
    access_secret = ASECRET
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #Ask what the user wants to search for    
    search_term = ""
    search_term = raw_input("search query: ")
    f=open(search_term+"Tweets.txt", "w")

    start_time = time.time();

    #Restrict tweets to the US
    location = api.geo_search(query="USA", granularity="country")
    place_id = location[0].id

    print "SEARCHING TWITTER FOR", search_term   
    print "SEARCHING TWEETS FROM", place_id
    
    max_tweets = 10000
    tweet_out = []
    num_tweets = 0

    #For every tweet returns by the query
    for tweet in tweepy.Cursor(api.search, q=search_term + "-filter:retweets", tweet_mode="extended").items(max_tweets):
        
        result=tweet._json

        #If the tweet is an original tweet from a user (not retweeted)
        if (not result["retweeted"]) and ('RT @' not in result["full_text"]):
            
            #gather user's name and the tweet content       
            real_name = result["user"]["name"]
            tweet_text = result["full_text"]

            #add to array storing relevant tweets
            tweet_out.append(real_name)
            tweet_out.append(tweet_text)
            tweet_out.append(u"\n")

        #keep track of how many tweets were found
        num_tweets = num_tweets + 1

    print"NUMBER OF TWEETS: ",num_tweets


    #write each tweet to the file, encode so emojis don't cause crashes
    for item in tweet_out:    
        f.write(item.encode('utf-8'))
        f.write(u"\n")

    f.close()
    
main()
