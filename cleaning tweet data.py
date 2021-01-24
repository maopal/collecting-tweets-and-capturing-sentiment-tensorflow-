# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 17:07:13 2021

@author: Main
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import re

## IMPORT DATA/ COULD BE DONE USING LIVE DATA STREAM ASWELL IF YOU CONNECTION TO DATABASE
df = pd.read_csv(r"tester1.csv")

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

df['tweet']= [clean_at(i) for i in df['tweet']]

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


df['tweet']= [clean_rt(i) for i in df['tweet']]

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

df['tweet']= [clean_url(i) for i in df['tweet']]


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


df["tweet"] = [deEmojify(i) for i in df["tweet"]]








