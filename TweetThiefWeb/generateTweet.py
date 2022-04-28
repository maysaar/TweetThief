
def getFinalTweet(tweets):
    splitTweets = tweets.split('.')
    strippedTweets = []
    finalTweet = ''

    for tweet in splitTweets:
        strippedTweets.append(tweet.strip())

    for tweet in strippedTweets:
        if len(tweet) > 0 and (len(tweet) + len(finalTweet) <= 240):
            finalTweet += tweet + '. '

    return finalTweet.strip()

tweets = 'The death of Brian Doherty by an apparent suicide bomber apparently came down to personal choice #2.In states like Georgia and North Carolina. The best way to go about doing business is to follow the rules. Always glad to have as a partner in the fight to eradicate COVID-19.'
print(getFinalTweet(tweets))