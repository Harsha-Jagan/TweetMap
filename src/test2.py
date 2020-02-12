#imports
import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import re #regular expression
import json
import time
from textblob import TextBlob
from flask import Flask
#flask setup
app = Flask(__name__)

#tweet format
def remove_url(txt):
    """Replace URLs found in a text string with nothing 
    (i.e. it will remove the URL from the string).

    Parameters
    ----------
    txt : string
        A text string that you want to parse and remove urls.

    Returns
    -------
    The same txt string with url's removed.
    """

    return " ".join(re.sub("([^0-9A-Za-z \t])|(\w+:\/\/\S+)", "", txt).split())

class TextProcessor():
    def __init__(self, sentence):
        self.tweetObj = TextBlob(sentence)
        print(self.tweetObj.sentiment)
        polarity = self.tweetObj.sentiment.polarity
        print(polarity)

tweetyyy = ''

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
            
            refined = remove_url(temp)
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



@app.route('/')
def Tweety():
    #activate stream
 #   twitterStream = Stream(auth, listener(), tweet_mode='extended')
  #  twitterStream.filter(languages=["en"], track=["Kobe"])
  
    return str(num + num)

if __name__=="__main__":
    num = 10975
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

'''
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)


'''








