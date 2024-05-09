#!/usr/bin/python3

import socket
import threading

clients = []
addresses = {}

# Handle client connections
def handle_client(client_socket, client_address):
    # Add client to list
    clients.append(client_socket)

    # Receive and broadcast msgs
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                broadcast(message, client_socket)
            else:
                print(f"Client {client_address} disconnected.")
                break
        except Exception as e:
            print(f"Error: {e}")
            client_socket.close()
            clients.remove(client_socket)
            print(f"Client {client_address} disconnected.")
            break

# Broadcast messages to all clients
def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message.encode('utf-8'))
            except Exception as e:
                print(f"Error: {e}")
                client_socket.close()
                clients.remove(client_socket)

def main():
    try:
        # Set up server as a socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('127.0.0.1', 8010))
        server_socket.listen(5)
        print("Chat server started...")

        # Accept client connections
        while True:
            if server_socket._closed:
                break
            client_socket, client_address = server_socket.accept()
            print(f"Connection from {client_address}")
            client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_handler.start()
    except KeyboardInterrupt:
        print("\nServer shutting down...")
        for client_socket in clients:
            client_socket.close()
        server_socket.close()

if __name__ == "__main__":
    main()
