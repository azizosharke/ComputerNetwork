import socket 
from threading import Thread


class Packet(Thread):


    des=0
    source=1
    router=2
    gatwey=3
    ISP=4
    GIVEN_ID=1
    packet_size=85241
    port =54321
    header: int=4




    def receivePacket(self,data:list, packet:socket):
       infoPacket  = data
        b =  [packet.getLength() - list]
        received = str(b)
        return received

     def ByteLoad (self,packet):
        b =  packet.countBytes()
        result =  [self.header+ b.length]
        return result

    def countDes(self, packet):
        data: object =  packet.getData()
        b= []
        des = str(b)
        return des

    def transfer(self, message):

        try:
            self.message.wait()

            while True:
                sign = recevied([self.size])
                self.socket.receive(sign)
                forward(sign)

        except Exception as w:
            if (not (type(w)== countDes(self))):
                print(end=2)
                }
    
    def forward(self , message):
        message.countDown()

    

