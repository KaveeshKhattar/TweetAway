# tweepy-bots/bots/autoreply.py
#python3 -m pip install tweepy
import tweepy
import logging
from config import create_api
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

def check_mentions(api, keywords, since_id):
    logger.info("Retrieving mentions")
    new_since_id = since_id
    for tweet in tweepy.Cursor(api.mentions_timeline,
        since_id=since_id).items():
        new_since_id = max(tweet.id, new_since_id)
        if tweet.in_reply_to_status_id is not None:
            continue
        if any(keyword in tweet.text.lower() for keyword in keywords):
            logger.info(f"Answering to @{tweet.user.name}")

            if not tweet.user.following:
                tweet.user.follow()

            api.update_status(
                
                status= f"Please reach us via DM @{user.screen_name}",
                in_reply_to_status_id=tweet.id,
            )
    return new_since_id

def main():
    id = tweet.user.id
    api = create_api()
    user = api.get_user(id)
    since_id = 1
    while True:
        since_id = check_mentions(api, ["help", "support","tweetawaybot","please"], since_id)
        logger.info("Waiting...")
        time.sleep(60)

if __name__ == "__main__":
    main()