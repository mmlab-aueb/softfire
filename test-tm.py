from socket import *

s = socket(AF_INET, SOCK_DGRAM)
s.sendto("aueb-02 east.first-floor",('',8000))
bf, tm = s.recvfrom(1024)
print bf
