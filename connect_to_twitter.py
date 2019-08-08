# -*- coding: utf-8 -*-
"""
connect_to_twitter.py
    :author: Raymond Gasper 
    :created: 08 August 2019
    :copyright: 2019 Dun & Bradstreet 
"""
import twitter
from access_keys import *
api = twitter.Api(consumer_key=consumer_api_key,
                  consumer_secret=consumer_api_secret_key,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)
print "Connected to Twitter API!"
