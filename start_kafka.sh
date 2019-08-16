#!/bin/bash
# Mac OSX
# you'll have to have the kafka commands added to your path for this to work
#run the following comands in separate screens, if you just execute this they don't wait for eachother and it doesn't work.
zookeeper-server-start zookeeper.properties
kafka-server-start server.properties
kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic tweets