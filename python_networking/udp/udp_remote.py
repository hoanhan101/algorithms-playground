#!/usr/bin/env python3
# UDP client and server for talking over the network

import argparse, random, socket, sys

MAX_BYTES = 65535

def server(interface, port):
    # Create a socket using UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to an IP and Port
    sock.bind((interface, port))

    # Print the IP and Port
    print('Listening at', sock.getsockname())

    # Keep listening
    while True:
        # Get data from sender
        data, address = sock.recvfrom(MAX_BYTES)

        # Randomly answer the request
        if random.random() < 0.5:
            print('Pretending to drop packet from {}'.format(address))
            continue

        # Decode the message
        text = data.decode('ascii')
        print('The client at {} says {!r}'.format(address, text))

        # Send back a response
        message = 'Your data was {} bytes long'.format(len(data))
        sock.sendto(message.encode('ascii'), address)

def client(hostname, port):
    # Create a socket using UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Connect to host ahead of time so we can use send() instead of sendto()
    # It solves the problem of the client being promiscuous - prevent middleman attack
    # It basically discard any incoming packet whose host doesn't match 
    sock.connect((hostname, port))
    print('Client socket name is {}'.format(sock.getsockname()))

    # Set delay time
    delay = 0.1  # seconds

    # Prepare a message
    text = 'This is another message'
    data = text.encode('ascii')

    # Keep listening
    while True:
        # Send data
        sock.send(data)

        # Set timeout for delay
        print('Waiting up to {} seconds for a reply'.format(delay))
        sock.settimeout(delay)

        # Try listening for data
        try:
            data = sock.recv(MAX_BYTES)

        # Exponential back-off: wait longer for the next request
        except socket.timeout as exc:
            delay *= 2
            if delay > 2.0:
                raise RuntimeError('Server is down') from exc
        else:
            # We are done, and can stop looping
            break

    print('The server says {!r}'.format(data.decode('ascii')))

if __name__ == '__main__':
    # Make choices
    choices = {'client': client, 'server': server}

    # Parser's description
    parser = argparse.ArgumentParser(description='Send and receive UDP,'
                                     ' pretending packets are often dropped')

    # Specify role
    parser.add_argument('role', choices=choices, help='Server or Client')

    # Specify host. Can use '' as a wildcard to accept any role.
    parser.add_argument('host', help='interface the server listens at;'
                        ' host the client sends to')

    # Specify port
    parser.add_argument('-p', metavar='PORT', type=int, default=1060,
                        help='UDP port (default 1060)')

    # Parse argument and execute the function
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host, args.p)