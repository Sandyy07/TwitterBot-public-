import os
import tweepy
import requests
import json
from dotenv import load_dotenv
import time

load_dotenv() #loads all the .env variables at the start.

def get_quote():
    pp = requests.get("https://api.quotable.io/random")
    if pp.status_code == 200:
        return json.loads(pp.text)  # all fine
    elif pp.status_code == 404:
        raise Exception("Invalid input or quote not found")
    else:
        raise Exception("Side Down")

# raw_quote = get_quote()

# print(type(raw_quote["tags"]))

def __make_quote_helper():
    raw_quote = get_quote()
    tags = " "
    quote = str(raw_quote["content"]) + " - " + str(raw_quote["author"]) + ". Tags- " + tags.join(raw_quote["tags"])
    return quote
def make_quote():
    quote = __make_quote_helper()
    if len(quote)>=250 and quote<=0:
        make_quote()
    else:
        return quote

def authorization():
    try:
        client = tweepy.Client(
            # OAuth 1.0a
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
            # OAuth 2.0
            bearer_token=os.getenv("BEARER_TOKEN")
        )
        return client
    except Exception as e:
        print("client authorization Failed: ", e)
        return 1

def post_to_twitter(client, quote):
    client.create_tweet(text=quote)





