from socket import *
from pox.lib.packet import ethernet,ipv4
from pox.lib.addresses import IPAddr,EthAddr 


'''
This is a Server  binding an interface and waiting
to receive a packet from the client and print it. (e.g icmp)
'''

#Open a Socket
s = socket(AF_PACKET, SOCK_RAW, htons(0x0003) )
#bind an interface
s.bind(('ens3', 0))
#parse packet payload and print it
ether = ethernet()
while True:
    data = s.recv(2048)
    ether.parse(data)
    if ether.type == 0x0800: //IP
        ip_packet = ether.payload 
        if ip_packet.srcip == IPAddr("192.168.130.9"):
            print ip_packet.payload
