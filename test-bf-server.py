from bf import PacketHandler,BFServer

class BFhandler(PacketHandler):
        
    def handle_packet(packet):
        print packet

bfserver = BFServer(BFhandler)
bfserver.listen() 
