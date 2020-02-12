#import dependencies
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from listener import listener
import TextProcessor as tp

from flask import Flask

#main
if __name__ == '__main__':
    #access keys
    consumer_key = "GoCALOwINkSteUzVV9w5NNjOc"
    consumer_secret = "G9rpjSN9Zh6GxpGjWuQZcvGpdoRTsmwR0PQsmdmvqvAohcsS5k"

    access_token = "838946038610292740-EEjxlKqX7r29GTaVy7vpYNOAwZxgdOa"
    access_token_secret = "G7kkEw4Kq5JVNw4QNpPWar2wuUbLghyRN9TiVG0M2odkE"

    #pass twitter credentials to tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    twitterStream = Stream(auth, listener(), tweet_mode='extended')
    twitterStream.filter(languages=["en"], track=["trump"])
