#!/usr/bin/python3

import socket

# Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define address and port
server_address = ('127.0.0.1', 8010)

while True:
    # Get message from user
    message = input("Enter message to server ('quit' to exit): ")

    # Send message to server
    client_socket.sendto(message.encode('utf-8'), server_address)

    # Check for quit
    if message.lower() == 'quit' or message.lower() == 'q':
        print("Closing connection...")
        break

    # Receive response from server
    response, addr = client_socket.recvfrom(1024)
    print("Received: ", response.decode('utf-8'))
