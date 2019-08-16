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
from confluent_kafka import Producer

global USERS
global LANGUAGES
USERS = ['@twitter','@twitterapi','@support']
LANGUAGES = ['en']


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        log.info('Message delivery failed: {}'.format(err))
    else:
        log.info('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))


if __name__ == '__main__':
    # log into twitter api
    api = twitter.Api(consumer_key=CONSUMER_API_KEY,
    consumer_secret=CONSUMER_API_SECRET_KEY,
    access_token_key=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET)
    log.info("Connected to Twitter API!")
    prod = Producer({'bootstrap.servers': '0.0.0.0:9092'})
    log.info("Producer connected to Python Server")
    # log some tweet dumps
    max_tweets = 5
    count = 0
    for tweet in api.GetStreamFilter(track=USERS, languages=LANGUAGES):
        count += 1
        data_str = tweet['text']
        log.info(data_str)
        prod.produce('tweets', data_str.encode('utf-8'), callback=delivery_report)
        if count >= max_tweets:
            log.info('done logging tweets, hit max count')
            break
    prod.flush()
    log.info('exited gracefully...')



