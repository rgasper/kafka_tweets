from confluent_kafka import Consumer, KafkaException
import sys
from mylogger import log
import json
import logging


if __name__ == '__main__':

    topics = ["tweets"]

    # Consumer configuration
    log.info("Setting up the configs")
    conf = {'bootstrap.servers': "127.0.0.1", 'group.id': "group_test", 'session.timeout.ms': 7000,
         'auto.offset.reset': 'earliest'}

    # Create logger for consumer (logs will be emitted when poll() is called)
    log.info("Creating a consumer on the basis of configs")
    logger = logging.getLogger('consumer')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter('%(asctime)-15s %(levelname)-8s %(message)s'))
    logger.addHandler(handler)

    # Create Consumer instance
    # Hint: try debug='fetch' to generate some log messages
    c = Consumer(conf, logger=logger)

    def print_assignment(consumer, partitions):
        print('Assignment:', partitions)


    log.info("subscribing to the topic : " + str(topics))
    # Subscribe to topics
    c.subscribe(topics, on_assign=print_assignment)

    log.info("Reading msg from  the topic : " + str(topics))
    # Read messages from Kafka, print to stdout
    try:
        while True:
            msg = c.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                # Proper message
                sys.stderr.write('%% %s [%d] at offset %d with key %s:\n' %
                                 (msg.topic(), msg.partition(), msg.offset(),
                                  str(msg.key())))
                print(msg.value())

    finally:
        # Close down consumer to commit final offsets.
        c.close()