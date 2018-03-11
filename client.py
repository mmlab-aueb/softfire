from socket import *
from pox.lib.packet import ethernet,ipv4
from pox.lib.addresses import IPAddr,EthAddr

#Create an IP packet
# Open a socket and send the packet through it
s = socket(AF_PACKET, SOCK_RAW)
s.bind(('ens3', 0))

ip_packet         = ipv4()
ip_packet.srcip   = IPAddr("192.168.130.9")
ip_packet.dstip   = IPAddr("192.168.130.200")

for x in (1,2,4,8,3,5,9,6,10,12,7,11,13,14,15):
    ip_packet.payload = " Bloom filrer = " + '%x'%x
    ether      = ethernet()
    ether.type = 0x0800
    ether.dst  = EthAddr(b"\x00\x00\x00\x00\x00\x0"+'%x'%x)
    ether.src  = EthAddr(b"\xfa\x16\x3e\xae\xdc\xa6")
    ether.payload = ip_packet

    s.send(ether.pack())
