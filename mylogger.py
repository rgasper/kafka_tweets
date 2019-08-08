# -*- coding: utf-8 -*-
"""
mylogger.py
    :author: Raymond Gasper 
    :created: 08 August 2019
"""
import logging
from logging.handlers import RotatingFileHandler

logfile = 'log-kafka-tweets'
logging.basicConfig(
    format='[%(levelname)s] - [%(module)s:%(lineno)d] %(asctime)s - %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')
log = logging.getLogger(logfile)
log.addHandler(RotatingFileHandler(logfile, mode='a', backupCount=0))
log.handlers[0].doRollover() # make a new log each time