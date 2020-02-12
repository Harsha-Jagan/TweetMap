from textblob import TextBlob
import re #regular expression

#Tweet processing - removes punctuation, filters non-english letters and
#provides the text info from tweetObj
class TextProcessor():
    def __init__(self, sentence):
        self.tweetObj = TextBlob(sentence)
        print(self.tweetObj.sentiment)
        polarity = self.tweetObj.sentiment.polarity
        print(polarity)

    #tweet formatter - removes URLs
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
