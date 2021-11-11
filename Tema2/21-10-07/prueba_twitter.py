from rx.core import observable
from tweepy import Stream
from rx import create, operators
from rx.core import Observer
import json

consumer_key="MMSLklg7hBXJ2gUvYaIc91jtu"
access_token="1444673170385088520-bTEehtJ5ZFP1tQgGVUQ27XWtL5LWBK"
consumer_secret="YvOiG77Oz0ub9AflLQ2Ecfo5djepWsSsnl4KUfwmp0PgFrmvy2"
access_token_secret="dsZXOs30G4geWX1Xg8RTrbz0t2OUwRWms4Cxum3KuCL6t"
keywords = ['volcan', 'belen esteban', 'willyrex', '. y digo si']


class PrintData(Observer):
    def on_next(self, data):
        print(data)
    def on_error(self, status):
        print(status)

def tweet_observable(observer, scheduler):
    class TweetStream (Stream):
        def on_data(self, data):
            observer.on_next(json.loads(data))
            #json.loads(data)
        def on_error(self):
            observer.on_error('dead')
            #print('Error')
    stream = TweetStream(consumer_key, consumer_secret, access_token, access_token_secret)
    stream.filter(track = keywords)

observable = create(tweet_observable)

cadena = observable.pipe(
    operators.map(lambda v: "User:\n" + str(v.get('user').get('name')) + "\n\nText:\n" + str(v.get('text')) + "\n\n\n")
)

cadena.subscribe(PrintData())