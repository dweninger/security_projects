import socket

def sniff_packets(host, port=None):
    print(f"Sniffing packets on host {host} and port {port}...")
    try:
        # Create a raw socket
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        sniffer.bind((host, 0))

        # If no port is specified, sniff all TCP traffic, otherwise filter by port
        if port:
            filter_port = port
        else:
            filter_port = 0  # Sniff all ports

        while True:
            # Receive a packet
            packet, _ = sniffer.recvfrom(65565)

            # Print packet data
            print("[Packet data]: ", packet)

    except KeyboardInterrupt:
        print("Sniffing stopped.")

if __name__ == "__main__":
    host = input("Enter the host to sniff packets from: ")
    port_input = input("Enter the port to sniff packets from (leave blank to sniff all TCP traffic): ")
    if port_input:
        try:
            port = int(port_input)
        except ValueError:
            print("Invalid port number. Exiting.")
            exit()
    else:
        port = None
    sniff_packets(host, port)

