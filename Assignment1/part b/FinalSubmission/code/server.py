from socket import *
import argparse
from sys import exit

analyzer = argparse.ArgumentParser()
analyzer.add_argument('--port', '-p', help="Port no")
analyzer.add_argument('--ipAddress', '-i', help="Ip no")

i = analyzer.parse_args()

PORT = int(i.port)
HOST = i.ipAddress

FORMAT = "utf-8"


def server():
    ADDR = (HOST, PORT)
    SIZE = 1024
    print('-----------------------------------------------------')
    print(
        'UDP PROTOCOL FOR SENDING / RETRIEVING\n    FILES FROM CLIENTS AND SERVER')
    print('-----------------------------------------------------')
    # Staring a UDP socket.
    print("[STARTING]...Server is Starting.")

    server = socket(AF_INET, SOCK_DGRAM)  # udp datagram
    server.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  # BROACAST TO WORKERS

    server.bind(ADDR)
    # server.listen()  # server islitsening, waiting for client connection to be estabished
    print("[LISTENING]...Server is Listening.")

    x, ADDR = server.recvfrom(SIZE)  # Receiving info from client

    filename = x.decode().strip()
    print(
        f"[CONNECTION]:New Connection {ADDR} Is Established.\n",
    )

    option = int(input(f"[SERVER]: Kindly Enter[1,2,3] To Choose a Worker: "))
    # a socket for multicast
    sock = socket(AF_INET, SOCK_DGRAM)
    # timeout is 10 seconds
    sock.settimeout(1)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

    try:
        # send to a multicast group
        if option == 1:
            print(f"[SERVER]: Forwarding, {filename} Request To Worker: 1\n")
            multicast_group = ('172.20.0.4', 9999)
            sock.sendto(filename.encode(FORMAT), multicast_group)
            file = open("./code/worker1/" + filename, 'wb')
        elif option == 2:
            multicast_group = ('172.20.0.5', 9999)
            sock.sendto(filename.encode(FORMAT), multicast_group)
            file = open("./code/worker2/" + filename, 'wb')
        elif option == 3:
            multicast_group = ('172.20.0.6', 9999)
            sock.sendto(filename.encode(FORMAT), multicast_group)
            file = open("./code/worker3/" + filename, 'wb')
        else:

            print(f"[ERROR]: This worker Ip Address is not Authorised!!!")
            print(f"[ERROR]: Enter a valid ip !!!\n")

            # wait for responces from workers
        while True:

            try:

                data, s = sock.recvfrom(SIZE)
                file.write(data)

            except timeout:
                file.close()
                print('\n')

                print(
                    f"[STATUS]: Timed Out, No More Responses From, {s} !!!\n")
                break
            else:
                print(f"[SERVER]: Received % s bytes from % s" %
                      (len(data), s))

        print(f"[SERVER]: {filename} , is Downloaded!!")
        print(f"[STATUS]: Success!\n")

    finally:
        sock.close()

    file = open(filename, "rb")
    x = file.read(SIZE)  # binary format

    while x:
        if not server.sendto(x, ADDR):
            continue
        print(f"[SERVER]: Sending Traffic to Client....")

        x = file.read(SIZE)
    print(f"[STATUS]: Ok.")

    file.close()
    server.close()
    print(f"[CONNECTION]: {ADDR}Is Disconnected.")


if __name__ == "__main__":

    server()
