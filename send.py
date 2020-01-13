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
    api.PostUpdate(i + '\n( ' + datetime.now() + " 現在)")

