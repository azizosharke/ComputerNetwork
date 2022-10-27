import socket
import struct
import argparse

analyzer = argparse.ArgumentParser()
analyzer.add_argument('--port', '-p', help="Port number")
analyzer.add_argument('--ipAddress', '-i', help="Ip number")
i = analyzer.parse_args()

PORT = int(i.port)
HOST = i.ipAddress
FORMAT = "utf-8"

multicast_group = '224.0.0.0'
server_address = ('', 9999)
SIZE = 1024


def worker1():
    address = (HOST, PORT)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(server_address)
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack('4sL', group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    while True:
        print('-----------------------------------------------------')
        print(
            'UDP PROTOCOL FOR SENDING / RETRIEVING\n    FILES FROM CLIENTS AND SERVER')
        print('-----------------------------------------------------')
        print(f"[WORKER1]: Waiting to Receive Message\n")
        x, address = sock.recvfrom(SIZE)
        filename = x.decode().strip()
        print(f"[WORKER1]: Uploading {filename} .... ")
        file = open(filename, "rb")
        x = file.read(SIZE)

        while x:
            if not sock.sendto(x, address):
                continue
            print(f"[WORKER1]: Sending Traffic To The [SERVER]....")
            x = file.read(SIZE)
            sock.sendto('ack'.encode(), address)
            print(f"[RESPONSE]: Sending Acknowledgement To", address)

            print(f"[STATUS]: SUCCESS")

            exit()


if __name__ == "__main__":

    worker1()
