#LuminaryBot.py
import json
import sys
import time
import codecs
import time
from datetime import datetime
from unidecode import unidecode
from twython import Twython, TwythonError
from twython import TwythonStreamer
from urllib.request import urlopen
from secret import *

def quote():
    e = urlopen("http://quotes.rest/qod.json?category=life")
    reader1 = codecs.getreader("utf-8")
    value = json.load(reader1(e))
    quote_e = value['contents']['quotes'][0]['quote']
    author_e = value['contents']['quotes'][0]['author']

    f = urlopen("http://quotes.rest/qod.json?category=inspire")
    reader = codecs.getreader("utf-8")
    values = json.load(reader(f))
    quote_f = values['contents']['quotes'][0]['quote']
    author_f = values['contents']['quotes'][0]['author']

    return author_e, quote_e, author_f, quote_f

def auth():
    twitter = Twython(C_KEY,
                  C_SECRET, 
                  A_TOKEN, 
                  A_TOKEN_SECRET)
    return twitter

def main():

    author_e, quote_e, author_f, quote_f = quote()
    twitter = auth()
    tweet_e = ""
    tweet_f = ""

    if len(author_f) >= 1 and len(quote_f)+len(author_f) <= (140-6):
        try:
                    tweet_f = "\"" + quote_f + "\"\n\n- " + author_f
                    twitter.update_status(status=tweet_f)
                    print("\nTwitted one quote. Check the log for more info...")
        except TwythonError as f:
                    print(f)
    else:
        print("Skipped! The quote is too long.")

    if len(author_e) >= 1 and len(quote_e)+len(author_e) <= (140-6):
        try:
                    tweet_e = "\"" + quote_e + "\"\n\n- " + author_e
                    twitter.update_status(status=tweet_e)
                    print("\nTwitted one quote. Check the log for more info...")
        except TwythonError as e:
                    print(e)
    else:
        print("Skipped! The quote is too long.")
		
if __name__ == "__main__":
    main()
    time.sleep(86400)
