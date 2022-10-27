from socket import *
import argparse
# import socket
analyzer = argparse.ArgumentParser()
analyzer.add_argument('--port', '-p', help="Port number")
analyzer.add_argument('--ipAddress', '-i', help="Ip number")
analyzer.add_argument('--filename', '-f', help=" file name")

i = analyzer.parse_args()
PORT = int(i.port)
HOST = i.ipAddress
filename = i.filename
FORMAT = "utf-8"


def client():
    print('-----------------------------------------------------')
    print(
        'UDP PROTOCOL FOR SENDING / RETRIEVING\n    FILES FROM CLIENTS AND SERVER')
    print('-----------------------------------------------------')
    # Staring a UDP socket.
    print("[STARTING]....Client is starting.")

    ADDR = (HOST, PORT)
    SIZE = 1024

    client = socket(AF_INET, SOCK_DGRAM)
    client.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    print(f'[CLIENT]: Request, {filename}, Is Awaiting Reply...\n')
    client.sendto(filename.encode(), ADDR)

    x, ADDR = client.recvfrom(SIZE)

    try:
        while x:

            client.settimeout(1)
            x, ADDR = client.recvfrom(SIZE)

    except timeout:

        print(f"[CLIENT]: {filename}, Downloaded Successfully !! ")
        print(f"[STATUS]: Success! \n")

        client.close()
        print(f"[CONNECTION] Host {ADDR} Is Disconected.")


if __name__ == "__main__":

    client()
