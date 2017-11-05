#!/usr/bin/env python3

import socket

target_host = '127.0.0.1'
target_port = 80

# create a socket object using IPv4 and UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


# because UDP is a connectionless protocol, no call to connect()
# send some data
client.sendto("SOME DATA", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

print(data)

