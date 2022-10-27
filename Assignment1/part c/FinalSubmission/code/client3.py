#https://abdesol.medium.com/udp-protocol-with-a-header-implementation-in-python-b3d8dae9a74b
from socket import *
import zlib
import argparse
from multiplexEncrypt import AESCipher
import struct

# parser
analyzer = argparse.ArgumentParser()
analyzer.add_argument('--port', '-p', help="Port no")
analyzer.add_argument('--ipAddress', '-i', help="Ip no")
i = analyzer.parse_args()
HOST = i.ipAddress
PORT = int(i.port)

def client(filename):
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
    ADDR = (HOST, PORT)
    client_buffer = 512
    key = "*asdasdasdhhssss*"
    protocol = AESCipher(key)
    file_name = protocol.encrypt(filename.encode())
    packets = file_name
    source = PORT
    destination = PORT
    def calculate_status(packets):
        return zlib.crc32(packets)
    header_info = len(packets)
    status = calculate_status(packets)
    m = 0
    print("[CLIENT]: Sending filename...")
    new_header= struct.pack(
        "!IIII", source, destination, header_info, status, m)
    packet = new_header + packets
    sock.sendto(packet, ADDR)
    print("[CLIENT]: Receiving file ...")
    file_chunks, forward_error = [], []
    try:
        while packets:
            print(
                f" [SEND TRAFFIC]:No #{new_header[4]} |{new_header[3]}| Status: "
                f"{new_header[3] == calculate_status(packets)}")
            if new_header[3] != calculate_status(packets):
                file_chunks.append(packets)
            sock.settimeout(2)
    except timeout:
        print()
    if len(forward_error) != 0:
        print("[CLIENT]: Requesting error packets from the server!")
        packets = str(forward_error).encode()
        print("[CLIENT]: Receiving errors!")
        new_header = struct.unpack("!IIII", new_header)
        try:
            while packets:
                packets = protocol.decrypt(packets)
                print(
                    f"#{new_header[4]}->{new_header[3]}->{new_header[3] == calculate_status(packets)}")
                sock.settimeout(4)
        except:
            sock.close()
    else:
        print("[CLIENT]: No error packets found!")
    print(f"[STATUS]: Ok!")
    print(f"[CLIENT]:{filename} downloaded!\n")
files_input = int(input("How many files do you want to transfer? :\n "))
for i in range(files_input):
    command_input = input("Please state the name of the file :\n ")
    client(command_input)

