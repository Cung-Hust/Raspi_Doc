#!/usr/bin/env python
import pika, sys, os
import time

def main():
    # connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))    
    connection = pika.BlockingConnection(
        pika.ConnectionParameters('localhost', 5672, '/', pika.PlainCredentials('avani', 'avani')))
    channel = connection.channel()

    channel.queue_declare(queue='Pi1')

    def callback(ch, method, properties, body):
        print(" [x] Received message: %r" % body.decode())
        print(" -- ")
    channel.basic_consume(queue='Pi1', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)