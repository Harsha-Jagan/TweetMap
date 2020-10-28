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
    consumer_key = "XXXXXXXXXXXXXXXXXXXXX"
    consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
    access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

    #pass twitter credentials to tweepy
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    twitterStream = Stream(auth, listener(), tweet_mode='extended')
    twitterStream.filter(languages=["en"], track=["trump"])
