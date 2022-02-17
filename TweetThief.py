import re
import os
import csv
import pandas as pd
import math


def cleanTweet(tweet):
    tweetDecoded = tweet.encode('ascii', 'ignore').decode('ascii')
    tweetRemovedLinks = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', tweetDecoded)
    tweetRemovedLinks = tweetRemovedLinks.replace('\n', ' ')
    return tweetRemovedLinks


def openFile(csv):
    tweets = []
    
    df = pd.read_csv(csv)
    
    for index,row in df.iterrows():
        t = row['tweet']
        tweets.append(t)
    
    return tweets



csv = 'aoc.csv'
rawTweets = openFile(csv)


cleanTweets = []
for tweet in rawTweets:
    cleanTweets.append(cleanTweet(tweet))
print(cleanTweets)
