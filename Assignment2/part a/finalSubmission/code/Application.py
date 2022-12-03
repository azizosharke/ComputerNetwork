from socket import socket

class Application():


    def userEndInteraction(self, packet):
        data = packet.getData()
        message = getMessage(data, packet)
        print("Receive message:  " + message)
    def userStartInteraction(self):
        d = input("Forwarder: Enter the destination for the message : ")
        m = input(f"Forwarder: Enter the message  + {d}  :")
        addreess = socket("GW1", port)
        packetA = format(data, data.length)
        socket.send(packetA)
        addreess = socket('GW2', port)
        packetB = format(data, data.length)
        socket.send(packetB)
        print(f"Message {m} +was sent to {d}")
    def applicationRun(self):
        while (not executed):
            print("Forwarder: Enter SEND or RECEIVE : ")
            value = input()
            if value.equalsIgnoreCase('SEND'):
                self.sendMessage()
            elif value.equalsIgnoreCase("RECEIVE"):
                print("Waiting to receive the message")
                self.wait()
            else:
                print("Error !! ")

if __name__ == "__main__":
    try:
        Application().start()
    except Exception as e:
        print(e)
