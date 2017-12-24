#!/usr/bin/env python3
# UDP client and server on localhost

import argparse, socket
from datetime import datetime

# Greatest length that a UDP datagram can possibly have 
MAX_BYTES = 65535

def server(port):
    # Create a socket using UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Request UDP network addresss as localhost
    sock.bind(('127.0.0.1', port))

    # Print the IP and port
    print('Listening at {}'.format(sock.getsockname()))

    # Keep listening forever
    while True:
        # Listen for data
        data, address = sock.recvfrom(MAX_BYTES)

        # Decode the data from byte to ascii before printing it 
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))

    # Prepare a new text to send back a repsonse
        text = 'Your data was {} bytes long'.format(len(data))
        data = text.encode('ascii')
        sock.sendto(data, address)

def client(port):
    # Create a socket using UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Get the current time
    text = 'The time is {}'.format(datetime.now())

    # Encode data to send
    data = text.encode('ascii')
    sock.sendto(data, ('127.0.0.1', port))

   # OS assign a random port
    print('The OS assigned me the address {}'.format(sock.getsockname()))

    # Listen for response
    # This is dangerous because client haven't verified the sender's host
    data, address = sock.recvfrom(MAX_BYTES)

    # Decode data and print
    text = data.decode('ascii')
    print('The server {} replied {!r}'.format(address, text))

if __name__ == '__main__':
    # Make choices
    choices = {'client': client, 'server': server}

    # Add commandline interface
    parser = argparse.ArgumentParser(description='Send and receive UDP locally')

    # Specify role
    parser.add_argument('role', choices=choices, help='Server or Client')

    # Port has to be above 1023 in order to use without being a system admin
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')

    # Parse argument, choose a role and execute corressponding function
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)
