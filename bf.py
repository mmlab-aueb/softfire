import threading
from socket import *
from pox.lib.packet import ethernet,ipv4
from pox.lib.addresses import IPAddr,EthAddr 

class PacketHandler():
    def handle_packet(packet):
        return

class BFServer:
    handler = PacketHandler()
    def __init__(self,handler):
        self.handler = handler
        
    def listen(self):
        #Open a Socket
        s = socket(AF_PACKET, SOCK_RAW, htons(0x0003) )
        #bind an interface
        s.bind(('ens3', 0))
        #parse packet payload and print it
        ether = ethernet()
        while True:
            data = s.recv(2048)
            ether.parse(data)
            if ether.type == 0x0800: #IP
                ip_packet = ether.payload 
                if ip_packet.dstip == IPAddr("192.168.130.200"):
                   self.handler.handle_packet(ip_packet.payload)

if __name__ == "__main__":
    server =  RawServer()
    server.listen()
