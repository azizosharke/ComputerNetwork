from socket import *
import argparse
# import socket
analyzer = argparse.ArgumentParser(
    description='UDP Protocol for retrieving and sending files to clients')
analyzer.add_argument('--port', '-p', help="Port number")
analyzer.add_argument('--ipAddress', '-i', help="Ip number")
analyzer.add_argument('--filename', '-f', help=" file name")

i = analyzer.parse_args()
PORT = int(i.port)
HOST = i.ipAddress
filename = i.filename
FORMAT = "utf-8"  # encodihg formart


def main():
    print('-----------------------------------------------------\n')
    print('UDP Protocol for retrieving and sending files to client')
    print('-----------------------------------------------------')

    # Staring a UDP socket.
    print("[STARTING]..... Client is starting.")

    ADDR = (HOST, PORT)
    SIZE = 1024

    client = socket(AF_INET, SOCK_DGRAM)
    client.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    print(f'[CLIENT]: {filename}, is downloading ...')
    client.sendto(filename.encode(), ADDR)

    file = open("./code/" + filename, 'wb')
    x, ADDR = client.recvfrom(SIZE)

    try:
        while x:
            file.write(x)
            client.settimeout(3)
            x, ADDR = client.recvfrom(SIZE)

    except timeout:
        file.close()
        print(f"[CLIENT]: {filename}, Downloaded Successfully !! ")

        client.close()
        print(f"[DISCONNECTED] {ADDR} disconnected.")


if __name__ != "__main__":
    pass
else:
    main()
