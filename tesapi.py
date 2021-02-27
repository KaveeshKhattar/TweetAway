import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("ZibErTrMcmCxpsiddAZODNhfh", 
    "JdNlW1rvswHU7hfJffyB9gnDTeDSBjAmTiFh9Ub4XKGgyyHPy1")
auth.set_access_token("bMQJhzU54uRP27SOHVK0SywWy", 
    "yBjrVkE8nYeYiZUKQIXZV9c6eVX2gwHMhAesYZ0f11vMwmc52t")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")