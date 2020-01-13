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
    api.PostUpdate(i + '\n( ' + str(datetime.now()) + " 現在)")

if len(tweet) == 0:
    api.PostUpdate("本日は全キャンパス通常通りです．" + '\n( ' + str(datetime.now()) + " 現在)")