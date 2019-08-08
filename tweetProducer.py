# -*- coding: utf-8 -*-
"""
tweetProducer.py
    :author: Raymond Gasper 
    :created: 08 August 2019
"""
import logging
from logging.handlers import RotatingFileHandler
import twitter
from access_keys import *
import json

global log
global USERS
global LANGUAGES
USERS = ['@twitter','@twitterapi','@support']
LANGUAGES = ['en']


if __name__ == '__main__':
    # setup logging
    logfile = __name__+'.log'
    logging.basicConfig(
        format='[%(levelname)s] - [%(module)s:%(lineno)d] %(asctime)s - %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')
    log = logging.getLogger(logfile)
    log.addHandler(RotatingFileHandler(logfile, mode='a', backupCount=14)) # will keep 14 backup logs: log.1, log.2 ... log.14
    log.handlers[0].doRollover() # make a new log each time
    # log into twitter api
    api = twitter.Api(consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET_KEY,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)
    log.info("Connected to Twitter API!")
    # log some tweet dumps
    for tweet in api.GetStreamFilter(follow=USERS, languages=LANGUAGES):
        log.debug(json.dumps(tweet))
    