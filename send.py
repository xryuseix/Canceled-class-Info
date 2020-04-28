# -*- coding: utf-8 -*-

import os
import fetch
import print_logs
import twitter
from datetime import datetime
import pytz

def addtags(string, tags):
    string += "\n\n"
    for j in tags:
        string += "#" + j + ' '
    return string

def adddate(string):
    string += '\n( ' + datetime.now(pytz.timezone('Asia/Tokyo')).strftime('%Y年%m月%d日 %H:%M:%S') + " 現在)"
    return string

# tweet string settings
tweet, status, campus = fetch.fetch()
tags = ["立命館", "立命館大学", "休講", "警報"]

# api settings
api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                  consumer_secret=os.environ["CONSUMER_SECRET"],
                  access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                  access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                  )

# heroku config:set EmergencyTweet=True と打つと休講情報が送れる
if os.environ["EmergencyTweet"] == "True":
    for i in tweet:
        tweetstring = i
        tweetstring = adddate(tweetstring)
        tweetstring = addtags(tweetstring, tags)
        api.PostUpdate(tweetstring)

# heroku config:set NormalTweet=True と打つと通常の通知も送れる
if os.environ["NormalTweet"] == "True":
    if len(tweet) == 0:
        tweetstring = "本日は全キャンパス通常通りです．"
        tweetstring = adddate(tweetstring)
        tweetstring = addtags(tweetstring, tags)
        api.PostUpdate(tweetstring)

# heroku config:set TestTweet=True と打つとテストができる
if os.environ["TestTweet"] == "True":
    tweetstring = "これは訳あってテストする羽目になった時に送るツイートです．"
    tweetstring = adddate(tweetstring)
    tweetstring = addtags(tweetstring, tags)
    api.PostUpdate(tweetstring)

print_logs.print_logs(status, campus)