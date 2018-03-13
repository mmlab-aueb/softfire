from bf import PacketHandler,BFServer,BFClient

class BFhandler(PacketHandler):
        
    def handle_packet(selft,packet):
        print packet
        #client = BFClient()
        #client.send_packet(0,"Hello")

handler  =  BFhandler()
bfserver = BFServer(handler)
bfserver.listen() 
