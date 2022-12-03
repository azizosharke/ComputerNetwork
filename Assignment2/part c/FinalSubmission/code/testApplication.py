# https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b
from socket import *
import zlib
from itertools import chain
import struct
import argparse

# parser
analyzer = argparse.ArgumentParser()
analyzer.add_argument('--port', '-p', help="Port no")
analyzer.add_argument('--ipAddress', '-i', help="Ip no")
i = analyzer.parse_args()
HOST = i.ipAddress
PORT = int(i.port)


def ApplicationTest(j=None, file_name=None):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    ADDR = (HOST, PORT)
    server_buffer = 512
    key = "*asdasdasdhhssss*"
    source = PORT
    destination = PORT
    sock.bind(ADDR)
    print(f"Testing Server")
    directory = ""
    while True:
        packets = f.read(server_buffer)
        chunks.append(packets)
        if not packets:
            break
    for data in chunks:
        def calculate_status(packets):
            return zlib.crc32(packets)
        status = calculate_status(data)
        j += 1
        print(f"[SEND TRAFFIC]:No. #{j}, Checksum: {status}")
    file_error = ""
    if file_error != "None":
        for i, chunk in enumerate(chunks):
            for error_id in file_error:
                if i != error_id:
                    continue
                header_info = len(chunk)
                k = i
                sock.sendto(packet, ADDR)
                print(" All packets were sent!\n\n")
    else:
        print(" No errors received!")

    sock.close()
try:
    while True:

        for x in chain(forwarders.values()):
                    print(x)
except timeout:
    print()
    print("[STATUS]...Application is Timed Out.\n")
    print(
        f"[CONNECTION]:  Is Disconected.\n",
    )
