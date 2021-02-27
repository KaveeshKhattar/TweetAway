#from __future__ import unicode_literals
import tweepy
import logging
import os

logger = logging.getLogger()

def create_api():
    consumer_key = "pFJ11iHOw8zUbOQCzsh4ljOOh"
    consumer_secret = "YXP0CYbSZvlhmzW89KhIylbjBXhb4dNP128QeumZbHegtCpPPD"
    access_token = "1363842412842426368-9VggGHS2x60F92ZfjEnak4JgYXAdP7"
    access_token_secret = "RvnPUQ1PoNJWrVWOP1e1545nmeUTa1g2CH8Ql45A8IWwh"
    '''
    consumer_key = os.environ.get('Name[0]')
    consumer_key.decode()
    consumer_secret = os.environ.get('Name[1]')
    consumer_secret.decode()
    access_token = os.environ.get('Name[2]')
    access_token.decode()
    access_token_secret = os.environ.get('Name[3]')
    access_token_secret.decode()
    print(access_token_secret)
    '''
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, 
        wait_on_rate_limit_notify=True)
    try:
        api.verify_credentials()
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e
    logger.info("API created")
    return api
    