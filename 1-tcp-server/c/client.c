#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>

#define PORT 8010
#define MSG_SIZE 1024

int main() {
    int sock;
    struct sockaddr_in serv_addr;
    char message[MSG_SIZE];
    char buffer[MSG_SIZE];

    // Create socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket creation failed");
        exit(EXIT_FAILURE);
    }

    // Connect to server
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);
    if (inet_pton(AF_INET, "127.0.0.1", &serv_addr.sin_addr) <= 0) {
        perror("Invalid address/ Address not supported");
        exit(EXIT_FAILURE);
    }
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("connection failed");
        exit(EXIT_FAILURE);
    }

    while(1) {
        // Input message from user
        printf("Enter your message: ");
        fgets(message, MSG_SIZE, stdin);

        // Send message to server
        send(sock, message, strlen(message), 0);

        // Check if user wants to quit
        if (strcmp(message, "quit\n") == 0) {
            printf("Closing connection...\n");
            break;
        }

        // Receive response from server
        if (recv(sock, buffer, MSG_SIZE, 0) <= 0) {
            perror("recv failed");
            exit(EXIT_FAILURE);
        }
        printf("Received from server: %s\n", buffer);
    }

    // Close the socket
    close(sock);
    return 0;
}
