from bf import BFClient

client = BFClient()
#for x in (1,2,4,8,3,5,9,6,10,12,7,11,13,14,15):
x=0
payload = " Bloom filrer = " + '%x'%x
client.send_packet(x,payload)
