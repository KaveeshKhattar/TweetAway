'''
import tweepy
import logging 
import os

# Authenticate to Twitter

#auth = tweepy.OAuthHandler("1363842412842426368-1xEL8FdwFLH9i2VWPfNK8Kh6KETKKd", "z9UjdHZYwY9v2KulRCvNiMJpomOgx5Y8fYuC2FkcI7kVG")
#auth.set_access_token("99mfrwuLuJErs7AUuM4dL2WhD", "ReA1R2GOMCM1vcKOOgGKrA2s7x89PwotsN0lUZ1BgQgNaHfEfR")

auth = tweepy.OAuthHandler("mku6TWJtRlZ74f8kgz0wSiUcc", "hppXen2cS6NrkuMdbKEXBWBGw2tg5gIRpDjRkcqIPWBs9hO67Y")
auth.set_access_token("1363842412842426368-BPzhaydb7WMO23pf6G1Tmjx4d5wjcM", "LBZqqUAYdzD56IbR4u2vHYTStAfuofIrTPVXNnMnys0T5")

# Create API object
api = tweepy.API(auth)
 
# Create a tweet
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

var=4
timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}") #most recent tweets by which user
api.update_status("Test tweet from I ",var) #create tweet
var+=1
'''

# tweepy-bots/bots/config.py
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = os.getenv("1363842412842426368-yv9S5iGu6zlSObw6KPPKkwBFf1xvpw")
    consumer_secret = os.getenv("55RgNfqnm4gd4nCUkG5vrPM4DJDrhrNZerdTENwypMzV2")
    access_token = os.getenv("1363842412842426368-jq1S87KJZEzA2S1jjWOKkUdFHbSfXH")
    access_token_secret = os.getenv("MNPWsiROlhUDVoEgbHSDXECSRyWdRDvXXj1CMPoy1zxmL")

    auth = tweepy.OAuthHandler("consumer_key", "consumer_secret")
    auth.set_access_token("access_token", "access_token_secret")
    api = tweepy.API(auth, wait_on_rate_limit=True, 
    wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api

display_api = create_api()
print(display_api)

'''
screen_name = "HitaJuneja"

for follower in display_api.followers(screen_name): 
    print(follower.screen_name)
'''