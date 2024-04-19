#!/usr/bin/python3

import socket

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# AF_INET means use IPv4
# SOCK_DGRAM means use UDP

# Bind socket to host and port
host = '127.0.0.1' # localhost
port = 8010 # any available port
server_socket.bind((host, port))

print("Server is listening on port", port)

while True:
    # Receive data from client
    data, addr = server_socket.recvfrom(1024)
    print("Received: ", data.decode('utf-8'))

    # Respond to client
    response = "Hello from server!"
    server_socket.sendto(response.encode('utf-8'), addr)
