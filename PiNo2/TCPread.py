#!/usr/bin/env python
import socket
import pika

TCP_IP = '192.168.1.8'
TCP_PORT = 1234
BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

# connect tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print("Connection address:", addr)

# connect to rabbit
# connection = pika.BlockingConnection(
#     # pika.ConnectionParameters(host='localhost'))
#     pika.ConnectionParameters('192.168.1.6', 5672, '/', pika.PlainCredentials('avani', 'avani')))
# channel = connection.channel()
# channel.queue_declare(queue='Pi1')

while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    print("received data:", data)
    conn.send(data)  # echo
    # channel.basic_publish(exchange='', routing_key='Pi1', body= data)
conn.close()