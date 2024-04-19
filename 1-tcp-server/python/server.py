#!/usr/bin/python3

import socket

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET is IPv4
# SOCK_STREAM is TCP

# Bind socket to host and port
host = '127.0.0.1' # localhost
port = 8010 # Any available port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen(5) # Allows up to 5 connections

print("Server is listening on port ", port)

while True:
    # Accept connections from client
    client_socket, addr = server_socket.accept()
    print(addr, " connected to the server")

    # Receive data from client
    data = client_socket.recv(1024).decode('utf-8')
    print("Received: ", data)

    # Respond to client
    response = "Hello from server!"
    client_socket.send(response.encode('utf-8'))

    # Close client socket
    client_socket.close()
