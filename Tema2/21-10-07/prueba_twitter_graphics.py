from rx.core import observable, Observer
from rx import create, operators
import tweepy
from tweepy import Stream
import json
from secret import consumer_key, access_token, consumer_secret, access_token_secret
from textblob import TextBlob
from os import error
from tkinter import *
from tkinter.ttk import Combobox
from functools import partial

keywords = ['volcan', 'belen esteban', 'willyrex', '. y digo si']

class App:
    tweet_user = ''
    tweet_text = ''
    def __init__(self):
        self.window = Tk()
        self.window.title = 'Aplicación Gráfica!'
        self.current_row = 3
        self.input_text = Entry(text='input text here', font=('Arial', 18))
        self.input_text.grid(column=0, row=0, columnspan=2)
        self.search_button = Button(text='Search', command=partial(self.search_tweets, self.input_text), pady=15, padx=20)
        self.search_button.grid(column=0, row=1)
        self.search_button = Button(text='Reset', command=partial(self.reset), pady=15, padx=20)
        self.search_button.grid(column=1, row=1)
        '''
        self.g_tweet_user = Label(text='', font=('Arial', 36))
        self.g_tweet_user.grid(column=0, row=2)
        self.g_tweet_text = Label(text='', font=('Arial', 24))
        self.g_tweet_text.grid(column=1, row=2)
        '''        
        self.mega_text = Text(font=('Arial', 12))
        self.mega_text.grid(column=0, row=2, columnspan=2)

        self.mega_text.tag_config('positivo', background = "green yellow", foreground = "dark green")
        self.mega_text.tag_config('neutral', background = "cyan", foreground = "blue")
        self.mega_text.tag_config('negativo', background = "light salmon", foreground = "red")
        
        self.window.mainloop()

    def reset(self):
        self.mega_text.delete("1.0","end")

    def updateApp(self, user, text):
        username = user if user != None else 'Anon'
        tweet_text = text if text != None else ''
        sentiment_value = TextBlob(tweet_text).sentiment.polarity
        if(sentiment_value > 0.05):
            sentiment = 'positivo'
        elif(sentiment_value < -0.05):
            sentiment = 'negativo'
        else:
            sentiment = 'neutral'
        self.mega_text.insert(END, f'\n{username}:\t{tweet_text}\n', sentiment)
        self.mega_text.insert(END, '________________________________________________________________________________\n', sentiment)

    def search_tweets(self, input_text):
        def observe_tweets(o, s):
            class TweetStream(Stream):
                def on_data(self, data):
                    o.on_next(data)
                def on_error(self, status):
                    o.on_error(status)
            stream = TweetStream(consumer_key, consumer_secret, access_token, access_token_secret)
            stream.filter(track = [input_text.get()], threaded= True)

        create(observe_tweets).pipe(
            operators.map(lambda txt: json.loads(txt)),
            operators.map(lambda d: [d["user"]["name"], d["text"]])
        ).subscribe(on_next = lambda v: self.updateApp(v[0], v[1]))

if __name__ == '__main__':
    App()
