#!/etc/bin/python3

import socket
import threading

# Receive message from server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print("\r" + message + "\n > ", end="", flush=True)
        except Exception as e:
            print(f"Error: {e}")
            break

def main():
    # Connect to server
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 8010))

    # Receive messages in thread
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Send messages to server
    while True:
        message = input(" > ")
        client_socket.send(message.encode('utf-8'))

if __name__ == "__main__":
    main()
