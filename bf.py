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
class BFClient:
    def __init__(self):
        self.s = socket(AF_PACKET, SOCK_RAW)
        self.s.bind(('ens3', 0))
        
    def send_packet(self,bf,payload):
        ip_packet         = ipv4()
        ip_packet.srcip   = IPAddr("192.168.130.9")
        ip_packet.dstip   = IPAddr("192.168.130.200")
        ip_packet.payload = payload
        ether             = ethernet()
        ether.type        = 0x0800
        ether.dst         = EthAddr(b"\x00\x00\x00\x00\x00"+chr(bf))
        #ether.src         = EthAddr(b"\xfa\x16\x3e\xae\xdc\xa6")
        ether.src         = EthAddr(b"\xfa\x16\x3e\xae\xdc\x00")
        ether.payload     = ip_packet
        self.s.send(ether.pack())
        

