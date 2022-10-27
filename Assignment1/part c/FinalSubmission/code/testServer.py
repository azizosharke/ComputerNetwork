from socket import *
import argparse
analyzer = argparse.ArgumentParser(
    description='UDP Protocol for retreiving and sending files to clients')
analyzer.add_argument('--port', '-p', help="Port no")
analyzer.add_argument('--ipAddress', '-i', help="Ip no")
i = analyzer.parse_args()
PORT = int(i.port)
HOST = i.ipAddress
FORMAT = "utf-8"  # encoding formart


def main():
    ADDR = (HOST, PORT)
    SIZE = 1024
    print('-----------------------------------------------------\n')
    print('UDP Protocol for retrieving and sending files to client')
    print('-----------------------------------------------------')

    # Staring a UDP socket.
    print("[STARTING]..... Server is starting.")

    server = socket(AF_INET, SOCK_DGRAM)  # udp datagram
    server.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # BROACAST TO WORKERS
    server.bind(ADDR)
    # server.listen()  # server islitsening, waiting for client connection to be estabished
    print("[LISTENING]......... Server is listening.")

    x, ADDR = server.recvfrom(SIZE)  # Receiving info from client

    filename = x.decode().strip()
    print(
        f"[NEW CONNECTION IS ESTABLISHED ] {ADDR} connected.\n",
    )
    print('Receiving the filename from the client.\n')
    print(f"[SERVER]: {filename} , is Downloading...")  # Scanning for file
    file = open(filename, "rb")
    x = file.read(SIZE)  # binary format

    while x:
        if not server.sendto(x, ADDR):
            continue
        print(f"[SERVER]: SENDING TRAFFIC....")
        x = file.read(SIZE)
    server.close()
    file.close()
    print(f"[DISCONNECTED] {ADDR} disconnected.")


if __name__ != "__main__":
    pass
else:
    main()
