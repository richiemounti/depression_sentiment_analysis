from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream


consumer_key = 'GySFfOZkz9ze4XaNGhFojWWkD'
consumer_secret = '7FnEwAhcA4xtGXnjfpcH5Kg9jGfJPjtsNYI4dai1FG42tUL450'
access_token = '1282609786958368768-42nHwO6apCPONXqTfQ1FJVJ0Hh6TWj'
access_secret = 'OWk9iyV5VlTs8N8OzUngrYpVeLkq1b16n7Y825yneHCv1'



class StdOutListener(StreamListener):

    def on_data(self, data):
        with open('data/tweetdata.txt','a') as tf:
            tf.write(data)
        print(data)
        return True

    def on_error(self, status):
        print(status)


if __name__ == '__main__':


    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    stream = Stream(auth, l)

    stream.filter(track=['depression', 'anxiety', 'mental health', 'suicide', 'stress', 'sad'])