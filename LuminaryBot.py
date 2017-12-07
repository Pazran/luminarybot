#LuminaryBot.py

import json
import time
import codecs
from urllib.request import urlopen
from twython import Twython, TwythonError
from twython import TwythonStreamer
from secret import *

def quote():
    # Retrieve quote of the day from the life category
    urlA = urlopen("http://quotes.rest/qod.json?category=life")
    readerA = codecs.getreader("utf-8")
    valueA = json.load(readerA(urlA))
    quoteA = valueA['contents']['quotes'][0]['quote']
    authorA = valueA['contents']['quotes'][0]['author']

    # Retrieve quote of the dat from the inspire category
    urlB = urlopen("http://quotes.rest/qod.json?category=inspire")
    readerB = codecs.getreader("utf-8")
    valueB = json.load(readerB(urlB))
    quoteB = valueB['contents']['quotes'][0]['quote']
    authorB = valueB['contents']['quotes'][0]['author']

    return authorA, quoteA, authorB, quoteB

# Check bot credintal
def auth():
    twitter = Twython(C_KEY,
                  C_SECRET, 
                  A_TOKEN, 
                  A_TOKEN_SECRET)
    return twitter

# Main function start here
def main():

    authorA, quoteA, authorB, quoteB = quote()
    twitter = auth()
    tweetA = ""
    tweetB = ""

    # Check if the first quote too long since twitter has 140 character limit
    # 140-6 to reserve for SPACES
    if len(authorA) >= 1 and len(quoteA)+len(authorA) <= (140-6):
        try:
                    tweetA = "\"" + quoteA + "\"\n\n- " + authorA
                    twitter.update_status(status=tweetA)
                    print("\nTwitted one quote. Check the log for more info...")
        except TwythonError as errA:
                    print(errA)
    else:
        print("Skipped! The quote is too long.")

    if len(authorB) >= 1 and len(quoteB)+len(authorB) <= (140-6):
        try:
                    tweetB = "\"" + quoteB + "\"\n\n- " + authorB
                    twitter.update_status(status=tweetB)
                    print("\nTwitted one quote. Check the log for more info...")
        except TwythonError as errB:
                    print(errB)
    else:
        print("Skipped! The quote is too long.")
		
if __name__ == "__main__":
    main()
    time.sleep(86400)
