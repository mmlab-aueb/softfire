from bf import PacketHandler,BFServer

class BFhandler(PacketHandler):
        
    def handle_packet(selft,packet):
        print packet

handler  =  BFhandler()
bfserver = BFServer(handler)
bfserver.listen() 
