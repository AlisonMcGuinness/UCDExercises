import tweepy
import json
import re

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0


    def on_status(self, status):
        tweet = status._json
        with open("tweets.txt", "w") as my_file:
            my_file.write(json.dumps(tweet) + '\n' )
            self.num_tweets += 1

        if self.num_tweets < 100:
            return True
        else:
            return False


    def on_error(self, status):
        print(status)


# is word in text
def word_in_text(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)

    if match:
        return True
    return False