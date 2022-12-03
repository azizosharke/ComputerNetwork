from socket import *
import argparse
analyzer = argparse.ArgumentParser(
   )
analyzer.add_argument('--port', '-p', help="Port no")
analyzer.add_argument('--ipAddress', '-i', help="Ip no")
i = analyzer.parse_args()
PORT = int(i.port)
HOST = i.ipAddress
FORMAT = "utf-8"  # encoding formart


def main():
    ADDR = (HOST, PORT)
    SIZE = 1024


    server = socket(AF_INET, SOCK_DGRAM)  # udp datagram
    server.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)  #
    server.bind(ADDR)
    print("[LISTENING]......... swithces are waiting.")
    x, ADDR = server.recvfrom(SIZE)

    filename = x.decode().strip()
    print(
        f"[NEW CONNECTION IS ESTABLISHED ] ",
    )


    while x:
        if not server.sendto(x, ADDR):
            continue
        print(f"[SERVER]: SENDING TRAFFIC....")
        x = file.read(SIZE)
    server.close()
    file.close()
    print(f"[DISCONNECTED] ")


if __name__ != "__main__":
    pass
else:
    main()
