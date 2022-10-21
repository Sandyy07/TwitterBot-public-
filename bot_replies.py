import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv("MONGODB_URL")

HEADERS = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': os.getenv("MONGODB_API_KEY"),
}

def get(user=None):
    """takes a user:int or nothing
    If user == None: return dictionary
    else: return tweet id
    returns error
    """
    BODY = {
        "dataSource": "twitterbot",
        "database": "twitterbot",
        "collection": "ID",
    }

    try:

        r = requests.post(url=URL+"/action/findOne",
                          headers=HEADERS, json=BODY)
        if r.status_code == 200:
            if json.loads(r.text) == None:
                raise Exception("Nothing recieved: ", r.text)
            else:
                if user == None:
                    data = json.loads(r.text)["document"]
                    data.pop("_id")
                    return data
                else:
                    return json.loads(r.text)['document'][str(user)]
        else:
            raise Exception("Status code: ", r.status_code)

    except Exception as e:
        return e



def write(user, tweet_id):
    """takes a user:int and tweet_id:int
    returns error, 0: success, 1: failure"""

    BODY = {
        "dataSource": "twitterbot",
        "database": "twitterbot",
        "collection": "ID",
        "filter": {
            "_id": {"$oid": os.getenv("MONGODB_ID_OBJECTID")}
        },
        "update": {
            "$set": {
                user: {"$numberLong": str(tweet_id)}
            }
        }


    }

    r = requests.post(url=URL+"/action/updateOne",
                      headers=HEADERS, json=BODY)
    if r.status_code == 200:
        if json.loads(r.text) == None:
            raise Exception("Nothing recieved: ", r.text)
        else:
            if json.loads(r.text)['modifiedCount'] != 0:
                return 0
            else:
                raise Exception("MonogDB update error: ", r.content)
    else:
        raise Exception(r.status_code, r.text)


def send_tweet_reply(client, textoftweet, tweet_id):
    client.create_tweet(text=textoftweet, in_reply_to_tweet_id=tweet_id)
    print("reply sent")


def get_latest_tweet(userid, client):
    """ Takes: id of user, client authorization
        Returns: tuple(tweet id, tweet text) """
    try:
        tweets = client.get_users_tweets(id=userid, max_results=5)
        return tweets.data[0].id, tweets.data[0].text
    except Exception as e:
        print(e)
        return -1

# user = 44196397
# data = get()
# print(type(data))

# tweet_id = 1582031735172104192
# write(user = user, tweet_id=tweet_id)
# print(get(user))``