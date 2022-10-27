# https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b
from socket import *
import zlib
from itertools import chain
import worker
import worker2
import worker3
from multiplexEncrypt import AESCipher
import struct
import argparse

# parser
analyzer = argparse.ArgumentParser()
analyzer.add_argument('--port', '-p', help="Port no")
analyzer.add_argument('--ipAddress', '-i', help="Ip no")
i = analyzer.parse_args()
HOST = i.ipAddress
PORT = int(i.port)


def server(j=None, file_name=None):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    ADDR = (HOST, PORT)
    server_buffer = 512
    key = "*asdasdasdhhssss*"
    source = PORT
    destination = PORT
    sock.bind(ADDR)
    aes = AESCipher(key)
    full_packet, ADDR = sock.recvfrom(server_buffer)
    file_name = aes.decrypt(file_name).decode()
    print(f"[SERVER]: Search for {file_name} Request in Available workers")
    directory = ""
    print(f"[SERVER]: Retrieving {file_name} ...")
    f = open(directory, "rb")
    chunks = []
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
                new_header = struct.pack(
                    "!IIII", source, destination, header_info, status, k)
                traffic = aes.encrypt(chunk)
                packet = new_header + traffic
                sock.sendto(packet, ADDR)
                print("[SERVER]: All packets were sent!\n\n")
    else:
        print("[SERVER]: No errors received!")
        print("[STATUS]: Ok!")
        print(f"[SERVER]: {file_name} send successfully!")
    sock.close()
try:
    while True:

        ADDR = (HOST, PORT)

        print('-----------------------------------------------------')
        print(
            'UDP PROTOCOL FOR SENDING / RETRIEVING\n    FILES FROM CLIENTS AND SERVER')
        print('-----------------------------------------------------')
        # Staring a UDP socket.
        print("[STARTING]...Server is Starting.\n")

        print(
            f"[CONNECTION]:New Connection {ADDR} Is Established.\n",
        )

        print(f"[SERVER]: Files located:\n")
        for x in chain(worker.values()):
            for i in chain(worker2.values()):
                for j in chain(worker3.values()):
                    print(x)
                    print(i)
                    print(j)

        server()
except timeout:
    print()
    print("[STATUS]...Server is Timed Out.\n")
    print(
        f"[CONNECTION]: {ADDR} Is Disconected.\n",
    )
