# import requests
# import bot

# client = bot.authorization()

# list = [
#     "elonmusk",
#     "narendramodi",
#     "BarackObama",
#     "justinbieber",
#     "katyperry"	,
#     "rihanna",
#     "Cristiano",
#     "taylorswift13",
#     "narendramodi",
#     "TheEllenShow"
# ]
# d = {}
# for username in list:
#     user = client.get_user(username = username)
#     d[user.data.id] = 0
# print(d)



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

# with open("C:/Users/rebca/Documents/rePro/twitterBot/quotes.json", "r",encoding="utf8") as f:
#     # control + arrow key to move a word and delete to delete the right character

#     data = json.load(f)
#     # print(data)


def write():
    """takes a user:int and tweet_id:int
    returns error, 0: success, 1: failure"""

    BODY = {
        "dataSource": "twitterbot",
        "database": "twitterbot",
        "collection": "quotes",
        "documents": data[40000: ]
        # "filter": {
        #     "_id": {"$oid": os.getenv("MONGODB_ID_OBJECTID")}
        # },
        # "update": {
        #     "$set": {
        #         user: {"$numberLong": str(tweet_id)}
        #     }
        # }


    }

    r = requests.post(url=URL+"/action/insertMany",
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

# write()