import bot
import bot_replies
import time
import threading

def post_tweet(time_interval):
    while True:
        quote = bot.make_quote()
        print(quote)
        client = bot.authorization()
        bot.post_to_twitter(client, quote)
        print("success")
        print("sleeping")
        time.sleep(time_interval)


def reply(time_interaval_for_tracking):
    while True:
        try:
            IDs = bot_replies.get()
            client = bot.authorization()

            if client != 1:
                for user in IDs.keys():
                    tweet = bot_replies.get_latest_tweet(int(user), client)
                    tweet_id = tweet[0]
                    if tweet != -1:
                        print("user: ", user, "tweetid: ", tweet_id)
                        id_in_file = bot_replies.get(user=user)

                        if tweet_id != id_in_file:
                            quote = bot.make_quote()
                            bot_replies.send_tweet_reply(client, quote, tweet_id)
                            if bot_replies.write(user, tweet_id) == 0:
                                print(
                                    tweet_id, "updated on mongodb altas: quotes.id")
                            time.sleep(1)
        except Exception as e:
            print(e)
            print("sleeping for 10sec")
            time.sleep(10)
            
            reply(time_interaval_for_tracking)

        print("sleeping for time interval")
        time.sleep(time_interaval_for_tracking)
        


if __name__ == "__main__":
    time_interval = 60*60*3  # in seconds
    time_interval_for_tracking = 60*5  # in seconds for 20 people per request
     t1 = threading.Thread(target=post_tweet, args=(time_interval,))
    t2 = threading.Thread(target=reply, args=(time_interval_for_tracking,))
#          t1 = threading.Thread(target=post_tweet, args=(time_interval,))
#     t2 = threading.Thread(target=reply, args=(time_interval_for_tracking,args=(time_interval_for_tracking,args=(time_interval,))
#          t1 = threading.Thread(target=post_tweet, args=(time_interval,))
#     t2 = threading.Thread(target=reply, args=(time_interval_for_tracking,))
     t1.start()
    t2.start()
