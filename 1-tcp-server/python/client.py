#!/usr/bin/python3

import socket

# Socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET for IPv4
# SOCK_STREAM for TCP

# connect to server
host = '127.0.0.1' # localhost
port = 8010 # same port as server
client_socket.connect((host, port))

while True:
    # Input message from user
    message = input('Send message to server (type "quit" to exit): ')

    # Send message to server
    client_socket.send(message.encode('utf-8'))

    #check if user wants to quit
    if message.lower() == 'quit' or message.lower == 'q':
        print("Closing connection...")
        break

    # Receive server response
    response = client_socket.recv(1024).decode('utf-8')
    print("Received: ", response)


client_socket.close()
