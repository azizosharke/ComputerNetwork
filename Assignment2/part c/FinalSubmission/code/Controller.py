from typing import List, Union, Any


from . import Packet


class Controller():
    controllerTable: list[Union[list[str], Any]] = [
        ['homeConnection - >', 'CLP - >', 'GW1 - >', 'CLP- >', 'ISP- >', 'CLP'],
        ['homeConnection - >', 'CLP - >', 'ISP - >', 'GW1- >', 'FWR- >', 'CLP'],
        ['homeConnection - >', 'CLP - >', 'FWR - >', 'ISP- >', 'DS1- >', 'CLP'],
        ['homeConnection - >', 'PLP - >', 'GW2 - >', 'PLP- >', 'ISP- >', 'PLP'],
        ['homeConnection - >', 'PLP - >', 'ISP - >', 'GW2- >', 'FWR- >', 'PLP'],
        ['homeConnection - >', 'PLP - >', 'FWR - >', 'ISP- >', 'DS2- >', 'PLP'],
        ['homeConnection - >', 'MLP - >', 'GW3 - >', 'CLP- >', 'ISP- >', 'MLP'],
        ['homeConnection - >', 'MLP - >', 'ISP - >', 'GW3- >', 'FWR- >', 'MLP'],
        ['homeConnection - >', 'MLP - >', 'FWR - >', 'ISP- >', 'DS1- >', 'MLP'],
        ['homeConnection - >', 'ALP - >', 'GW4 - >', 'PLP- >', 'ISP- >', 'ALP'],
        ['homeConnection - >', 'ALP - >', 'ISP - >', 'GW4- >', 'FWR- >', 'ALP'],
        ['homeConnection - >', 'ALP - >', 'FWR - >', 'ISP- >', 'DS2- >', 'ALP'],
        ['homeConnection - >', 'SLP - >', 'GW5 - >', 'CLP- >', 'ISP- >', 'SLP'],
        ['homeConnection - >', 'SLP - >', 'ISP - >', 'GW5- >', 'FWR- >', 'SLP'],
        ['homeConnection - >', 'SLP - >', 'FWR - >', 'ISP- >', 'DS1- >', 'SLP'],
        ['homeConnection - >', 'WLP - >', 'GW6 - >', 'PLP- >', 'ISP- >', 'WLP'],
        ['homeConnection - >', 'WLP - >', 'ISP - >', 'GW6- >', 'FWR- >', 'WLP'],
        ['homeConnection - >', 'WLP - >', 'FWR - >', 'ISP- >', 'DS2- >', 'WLP'],

    ]


    def controlTable(self, packet):

            info.self=  packet.getInfo()
            packetSource =  packet.findAdd()

            if info == signPacket:
                print(f"Sign was received from Switch  {packetSource}")

            elif data== emptyPacket
                print(f"packet was received with unclear destination  {packetSource}")

                if searchDes(packet):
                    return
                print(" packet was dropped")

            else:
                print(f"unexpected packet was received {str(packet)}")



    def linkControlTable(self, switch):

        table = []

        for i in range(0,controllerTable.length):
            
            if switch.equals(controllerTable[m]):
                table.append(controllerTable[m])
                table.append(controllerTable[m])
                table.append(controllerTable[m])



        switchLookLocation =  InetSocketAddress(switch,port)
        p =  switch(switchLookLocation, switchLookLocation.length, switchLookLocation)
        socket.send(p)

        print(f"New forwarding table was sent to {s}")



    def lookUpDestination(self,packet):

        print("Looking for the destination")

            if des ==  controllerTable[i][DEST_ADDR]:
                print("Creating new table")
                return True 
        

        return False

    

if __name__ == '__main__ ':
    try:
        Controller().start()
    except Exception as e:
        print(e)