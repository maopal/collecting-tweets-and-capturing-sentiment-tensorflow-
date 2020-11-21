# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:38:16 2020

@author: Main
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sqlite3

import time 

#consumer key, consumer secret, access token, access secret.
ckey="eL0ocs5U4RixeM3W92y7TP1kP"
csecret="wtMO6P4j78S9fp0M1Vbh7GUKz1WtMVuirz2NXXLBhYSoWwnAAu"
atoken="1233555223374901258-sVOqza4c74RVcnJeh2Vb3BC6YFjBBt"
asecret="GekBrd1dJDzX09g1y3eO7OhVzdvzRT1u6HsvZSM21GWMq"

conn = sqlite3.connect('etwitter.db')
c = conn.cursor()

def create_table():
    try:
        c.execute("CREATE TABLE IF NOT EXISTS testers(dattime REAL, tweet TEXT, likes REAL, noofretweets REAL)")
       # c.execute("CREATE INDEX fast_dattime ON testers(dattime)")
        #c.execute("CREATE INDEX fastt_tweet ON testers(tweet)")
        #c.execute("CREATE INDEX fastt_likes ON testers(likes)")
       # c.execute("CREATE INDEX fastt_noofretweets ON testers(noofretweets)")
        conn.commit()
    except Exception as e:
        print(str(e))
create_table()



class listener(StreamListener):

    def on_data(self, data):
        try:
            data = json.loads(data)
            tweet = data['text']
            time_ms = data['created_at']
            try:
                likes = data["retweeted_status"]["favorite_count"]
            except:
                likes = data["favorite_count"]
            try:
                retweets = data["retweeted_status"]["retweet_count"]
            except:
                retweets = data["retweet_count"]
            
            print(time_ms, tweet, likes, retweets)
            c.execute("INSERT INTO testers(dattime, tweet, likes, noofretweets) VALUES (?, ?, ?, ?)",
                  (time_ms, tweet, likes, retweets))
            conn.commit()

        except KeyError as e:
            print(str(e))
        return(True)

    def on_error(self, status):
        print(status)


while True:

    try:
        auth = OAuthHandler(ckey, csecret)
        auth.set_access_token(atoken, asecret)
        twitterStream = Stream(auth, listener())
        twitterStream.filter(track=["Bitcoin", "Ethereum", "Tezos", "Stellar", "Cardano", "Neo", "Tron", "Quant", "DigiByte"])
    except Exception as e:
        print(str(e))
        time.sleep(5)
