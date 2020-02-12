import json
import time
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import TextProcessor as tp

class listener(StreamListener):
    def on_data(self, data):
        try:
            jsonTweet = json.loads(data)

            text = jsonTweet['text']

            temp = text
            if(text[:3] == 'RT '):
                temp = text[text.index(': ')+2:]

            if(jsonTweet['truncated'] == True):
                temp = jsonTweet['extended_tweet']['full_text']

            refined = tp.remove_url(temp)
            print(refined)
            nlpBot = TextProcessor(refined)
            tweetyyy = refined
            '''
            saveFile = open('twitData.csv', 'a')
            saveFile.write(text)
            saveFile.close()
            '''
            return True

        except BaseException as e:
            print("failed ondata : ", str(e))
            time.sleep(5)

    def on_error(self, status):
        print(status)
