# -*- coding: utf-8 -*-

import os
import fetch
import twitter
from datetime import datetime

# tweet string settings
tweet = fetch.fetch()

# api settings
api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )

for i in tweet:
    api.PostUpdate(i + '\n( ' + datetime.now().strftime('%Y年%m月%d日 %H:%M:%S') + " 現在)")

# heroku config:set NormalTweet=True と打つと通常の通知も送れる
if os.environ["NormalTweet"] == "True":
    if len(tweet) == 0:
        api.PostUpdate("本日は全キャンパス通常通りです．" + '\n( ' + str(datetime.now()) + " 現在)")