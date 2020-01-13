# -*- coding: utf-8 -*-

import os
import fetch
import twitter
from datetime import datetime

# tweet string settings
tweet = fetch.fetch()
tags = ["立命館", "立命館大学", "休講", "警報", "拡散希望"]

# api settings
api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )

for i in tweet:
    tweetstring = i + '\n( ' + datetime.now().strftime('%Y年%m月%d日 %H:%M:%S') + " 現在)\n\n"
    for j in tags:
        
    api.PostUpdate(tweetstring)

# heroku config:set NormalTweet=True と打つと通常の通知も送れる
if os.environ["NormalTweet"] == "True":
    if len(tweet) == 0:
        tweetstring = "本日は全キャンパス通常通りです．" + '\n( ' + str(datetime.now()) + " 現在)"
        api.PostUpdate(tweetstring)