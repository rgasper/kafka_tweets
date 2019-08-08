# -*- coding: utf-8 -*-
"""
tweetProducer.py
    :author: Raymond Gasper 
    :created: 08 August 2019
"""
from mylogger import log
import twitter
from access_keys import *
import json

global USERS
global LANGUAGES
USERS = ['@twitter','@twitterapi','@support']
LANGUAGES = ['en']


if __name__ == '__main__':
    # log into twitter api
    api = twitter.Api(consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET_KEY,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)
    log.info("Connected to Twitter API!")
    # log some tweet dumps
    for tweet in api.GetStreamFilter(track=USERS, languages=LANGUAGES):
        log.info(json.dumps(tweet))
    