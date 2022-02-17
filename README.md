# TweetThief

Our project, “Tweet Thief” will allow a user to automatically generate tweets in the “voice” of a specified user over a specified time period through a web application. 

The first portion of the project will be to either find or build a tool to scrape tweets from specific users. We will compile a dataset that we can train our model on with certain caveats such as: links need to be deleted, images and media need to be deleted, and special characters will be removed. This will form the basis of our project and this initial phases’ functionality will be extended to live download users for our final stage.

The second portion of the project will be to complete and train the model that will be responsible for generating the tweets. We are not completely sure as of yet on how to do this but we will have to spend additional time learning more about this topic. Our original plan was to use GPT-3 but this specific use case is explicitly disallowed.

The third portion of our project will be to build a simple user interface that would allow a user to input a specific twitter handle and time period to generate tweets from. If the twitter user has a sufficient amount of tweets from that time period, it will output a tweet that is reminiscent of something they might tweet.
