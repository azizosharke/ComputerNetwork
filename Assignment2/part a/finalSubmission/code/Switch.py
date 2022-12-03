from socket import socket

from h5py.h5g import TYPE
from pycparser.c_ast import Switch

from Packet import Node



class Router(Node):
    def __init__(self,packet):
        try:
            print(controllerDevice())
        except Exception as e:
            print(e)

    def transferMessage(packet):
        try:
            data = packet.forwardingTable()

            if data[TYPE] == getNextHop(packet):
                sendSignal(packet)
            elif sendSignal(data):
                print("Forwarder : Updated Table ")
                packet.updateTable(packet)
        except Exception as e:
            print(e)



        def nextDes(packet):

            print("Final destination")
            print("Packet source :")

            for m in range(0, controllerTable.size):
                if destination == controllerTable[m]:
                    if controllerTable[m] == bytes:
                        return forwardingTable[n]

            return "it does not exist !"

    def updateForwardingTable(self, packet):
        data = packet.getData()
        b = [packet.getLength() - 1]
        tableUpdate = str(b)
        switchTable = tableUpdate.split(", ")

        controllerTable: object = [switchTable / 7][7]

        def ACK(self):
            data = bytes()
            data[TYPE] = self.header
            data = InetSocketAddress("controller", printForwardingTable(self))
            packetRec = property(socket.sendto(data))
            socket.send(packetRec)

            print("Sign was sent to controller")

    def printDetails(self):
        print("Forwarding Table: \n")
        print("{:%-1s %1s %1s %1s %1s %n ".format('DEST', "->", 'IN', '->', 'OUT'))
        print("----------------------------")

    def sendSignal(self, packetLocation):
        recDes = self.nextDes(packetLocation)

        if recDes != "there is an error":
            print(f"Next destination ---> : {recDes}")

            packet = DatagramPacket(packetLocation.getData(), packetLocation.getLength())

            socket.send(packet)
            print("Message was forwarded to the next destination .")

        else:
            compile(packetLocation)

            def controllerDevice(self, packetSource):
                finalDes = packetSource.getData()
                finalDes[e] = range

                addressCont = InetSocketAddress("Controller", packetSource)
                nextPacket = socket.send(packetSource)
                finalDes[e] = nextPacket

                addressCont = socket("Controller", packetSource)

                socket.send(nextPacket)

                print("Error. Next destination cannot be found !!  forwarding packet to controller")






if __name__ == "__main__":

    try:
        Switch.start()
        print("ADSL Router program completed.")

    except Exception as e:
        print(e)
