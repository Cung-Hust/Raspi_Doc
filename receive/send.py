#!/usr/bin/env python
import pika
import time

nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
connection = pika.BlockingConnection(
    # pika.ConnectionParameters(host='localhost'))
    pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('avani', 'avani')))
channel = connection.channel()

channel.queue_declare(queue='hello')
while True:
    # channel.basic_publish(exchange='', routing_key='hello', body='Hello 1!')
    for x in nums:
        channel.basic_publish(exchange='', routing_key='hello', body=x)
        print(" [+] Sent " + x)
    print("       ---------------       ")
    time.sleep(1)
connection.close()