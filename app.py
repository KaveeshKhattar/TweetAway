import tweepy
import sys
import os
import autoreply
from config import create_api
import followfollowers
import favretweet
import autoreply
import time

print(sys.path)

from flask import Flask, url_for, render_template, request, redirect


app = Flask(__name__)


@app.route("/",methods=["GET", "POST"])
def index():
    return render_template("index.html")




@app.route("/follow")
def followfollowers():
    if request.method =="GET"
        followers=followfollowers.return_followers()    
        return render_template('following.html',followers=followers)
    elif request.method == "POST":
        followers=followfollowers.return_followers()
        return render_template('following.html',followers=followers)


@app.route("/autoreply",methods=["POST"])
def autoreply():
    if request.method=="POST":
        


    tweets =[]
    username = []
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger()
    print("1")
    def check_mentions(api, keywords, since_id):
        print("4")
        logger.info("Retrieving mentions")
        new_since_id = since_id
        for tweet in tweepy.Cursor(api.mentions_timeline,
            since_id=since_id).items():
            new_since_id = max(tweet.id, new_since_id)
            tweets.append(tweet.text) #appending list
            if tweet.in_reply_to_status_id is not None:
                continue
            if any(keyword in tweet.text.lower() for keyword in keywords):
                username.append(tweet.user.name)
                logger.info(f"Answering to @{tweet.user.name}")

                if not tweet.user.following:
                    tweet.user.follow()

                api.update_status(
                    
                    status= f"Please reach us via DM @{tweet.user.name}",
                    in_reply_to_status_id=tweet.id,
                )
        return new_since_id

    def main():
        print("2")
        api = create_api()
        since_id = 1
        while True:
            print("3")
            since_id = check_mentions(api, ["help", "support","tweetawaybot","please"], since_id)
            logger.info("Waiting...")
            time.sleep(60)

    
    main()
    
    return render_template('templates/mentions.html', username = username, tweets = tweets)


    
  
@app.route("/favourite", methods =["GET","POST"])
def followfollowers():
    favretweet.main(keywords)
    return render_template(favourite.html)



if __name__ == '__main__':
   app.debug = True
   app.run()

















