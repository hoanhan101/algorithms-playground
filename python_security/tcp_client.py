#!/usr/bin/env python3

import socket

target_host = '0.0.0.0'
target_port = 9000

# create a socket object using IPv4 and TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
message = "SOMETHING"
client.send(message.encode())

# receive some data
response = client.recv(4096)

print(response)