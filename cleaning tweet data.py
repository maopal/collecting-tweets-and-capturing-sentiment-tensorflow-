# -*- coding: utf-8 -*-



import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import re

## IMPORT DATA/ COULD BE DONE USING LIVE DATA STREAM ASWELL IF YOU CONNECTION TO DATABASE
df = pd.read_csv(r"BTC_tweets_daily_example.csv")
tweetcolname= 'Tweet'

"""
Cleans @ symbol from tweet strings data
"""

def end_indexat(tweet):
 for i in range(tweet.index('@'), len(tweet)):
     if (tweet[i] == " "):
        break 
 return i+1

def clean_at(tweets):
 try:
   while(tweets.index("@")+1):
    startindex = tweets.index("@")
    endindex = end_indexat(tweets)
    tweets = tweets.replace(tweets[startindex:endindex], "")
 except:
    pass
 return tweets

df[tweetcolname]= [clean_at(i) for i in df[tweetcolname]]
df = df.dropna()


"""
Cleans "RT" at the beginning of tweets data
"""

def clean_rt(tweets):
 try:
  if tweets.index("RT") ==0:
    tweets= tweets.replace("RT", "")
 except:
     pass
 return tweets


df[tweetcolname]= [clean_rt(i) for i in df[tweetcolname]]

"""
Cleans URLs from TWEETS
"""

def end_index(tweet):
 for i in range(tweet.index('https'), len(tweet)):
     if (tweet[i] == " "):
        break 
 return i+1 

def clean_url(tweets):
 try:
   while(tweets.index("https")+1):
    startindex = tweets.index("https")
    endindex = end_index(tweets)
    tweets = tweets.replace(tweets[startindex:endindex], "")
 except:
    pass
 return tweets

df[tweetcolname]= [clean_url(i) for i in df[tweetcolname]]
df = df.dropna()

"""
Cleans emojis from tweets
"""


def deEmojify(text):
    regrex_pattern = re.compile(pattern = "["
        u"\U0001F600-\U0001F64F"  # emoticons
                u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                u"\U0001F680-\U0001F6FF"  # transport & map symbols
                u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                u"\U00002702-\U000027B0"
                u"\U000024C2-\U0001F251"
                u"\U0001f926-\U0001f937"
                u'\U00010000-\U0010ffff'
                u"\u200d"
                u"\u2640-\u2642"
                u"\u2600-\u2B55"
                u"\u23cf"
                u"\u23e9"
                u"\u231a"
                u"\u3030"
                u"\ufe0f"  # flags (iOS)
                           "]+", flags = re.UNICODE)
    return regrex_pattern.sub(r'',text)


df[tweetcolname] = [deEmojify(i) for i in df[tweetcolname]]
df = df.dropna()



indexneutral = df[df['Sentiment'] == "['neutral']"].index
indexpos = df[df['Sentiment'] == "['positive']"].index
indexneg = df[df['Sentiment'] == "['negative']"].index

df.loc[indexneutral,'Sentiment'] = 'neutral' 
df.loc[indexpos,'Sentiment'] = 'positive' 
df.loc[indexneg,'Sentiment'] = 'negative' 

indexneutral = df[df['sent_score'] == 0].index
indexpos = df[df['sent_score'] == 1].index
indexneg = df[df['sent_score'] == -1].index

df.loc[indexneutral,'sent_score'] = 0
df.loc[indexpos,'sent_score'] = 1
df.loc[indexneg,'sent_score'] = 2

indexzero = df[df['Sentiment'] == "0"].index
indexneg = df[df['Sentiment'] == "negative"].index
blanktweetindex = df[df['Tweet'] == ''].index

df = df.dropna()

df.drop(indexzero , inplace=True)
df.drop(indexneg , inplace=True)
df.drop(blanktweetindex , inplace=True)

sorte = df.sort_values(['Tweet', 'sent_score'], ascending = [True, False])
uniq = sorte.groupby('Tweet').first().reset_index()


df.to_csv("cleanedbtctestdata1.csv")


#uniq.to_csv("uniquetweets.csv") 


