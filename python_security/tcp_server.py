#!/usr/bin/env python3

import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

# set maximum backlog connection to 5
server.listen(5)

print("[*] Listening on {0} : {1}".format(bind_ip, bind_ip))

# client handling thread
def handle_client(client_socket):
    request = client_socket.recv(1024).decode()

    print("[*] Received {0}".format(request))

    # send back a packet
    message = "ACK!"
    client_socket.send(message.encode())

    client_socket.close()

while True:
    client, addr = server.accept()

    print("[*] Accepted connection from {0} : {1}".format(addr[0], addr[1]))

    # spin up our client thread to handle incoming data
    client_handler = threading.Thread(target=handle_client(client))
    client_handler.start()