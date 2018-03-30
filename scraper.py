#built using guide at https://marcobonzanini.com/2015/03/02/mining-twitter-data-with-python-part-1/
import json #for formatting the output
import time
import os
import io
import sys
import tweepy
from tweepy import OAuthHandler

name = ""

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, start_time, time_limit=60):
        self.time = start_time
        self.limit = time_limit
        self.tweet_data = []    
    
    def on_data(self, data):
        f = io.open(name + '_raw_tweets.json', 'a', encoding='utf-8')
        
        #while we still have time left
        while(time.time() - self.time) < self.limit:
            try:
                self.tweet_data.append(data)
                return True
            except BaseException, e:
                print 'failed data_saver', str(e)
                time.sleep(5)
                pass
        
        f = io.open(name+'_raw_tweets.json', 'w', encoding='utf-8')
        f.write(u'[\n')
        f.write(','.join(self.tweet_data))
        f.write(u']\n')
        f.close()
        exit()

    def on_error(self, status):
        print (status)

    def on_disconnect(self, notice):
        print ('bye')


def main():
    consumer_key = KEY
    consumer_secret = SECRET
    access_token =  TOCKEN
    access_secret = SECRET
    
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth_handler=auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    #Ask what name the user wants to search for    
    name = raw_input("Accused name: ")
    start_time = time.time();
    
    search_terms = []

    #search for accuser + rape
    rape_search = name + " rape"
    sexAssault_search = name + " sexual assault"

    search_terms.append(rape_search)
    search_terms.append(sexAssault_search)


    print("Listening for the terms: " + rape_search + " " + sexAssault_search)
    stream1 = tweepy.Stream(auth, MyStreamListener(start_time, time_limit=200))
    stream1.filter(track=search_terms)

main()
