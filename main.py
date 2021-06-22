import os
import tweepy
import html
from dotenv import load_dotenv

load_dotenv(".env")

consumer_key = os.environ.get("CONSUMER_KEY", None)
consumer_secret = os.environ.get("CONSUMER_SECRET", None)
access_token = os.environ.get("ACCESS_TOKEN", None)
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET", None)

userID = "python_tip"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

since_id = 1404562236451000329

tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=5,
                           # since_id=since_id,
                           # include_rts=False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode='extended'
                           )

print(len(tweets))


# def limit_handled(cursor):
#     while True:
#         try:
#             yield next(cursor)
#         except tweepy.RateLimitError:
#             time.sleep(15 * 60)
#
#
# for follower in limit_handled(tweepy.Cursor(api.followers).items()):
#     if follower.friends_count < 300:
#         print(follower.screen_name)

for info in tweets:
    print("=======================================")
    # print("ID: {}".format(info.id))
    # print(f"timestamp: {info.created_at}\n")
    print(f"python_tip: {html.unescape(info.full_text)}\n")
    # print(f"retweets: {info.retweet_count}\n")
    # print(f"likes: {info.favorite_count}\n")
    # print("\n")
    print(info.entities.get("urls", None))
    print(info.entities.get("media", None))
    print("\n=======================================")
