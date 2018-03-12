from bf import PacketHandler,BFServer,BFClient

class BFhandler(PacketHandler):
    
    def lights(self,value):
        if value == 1:
            print lights are on
        else:
            print lights are off
        
    def handle_packet(selft,packet):
        options = packet.split["/"]
        method  = options[1]
        uri     = options[2]
        if method == "PUT":
            payload = options[3]
            resource,value = payload.split("=")
            if resource == "lights"
                self.lights(value)
        client = BFClient()
        client.send_packet(0,"Hello")

handler  =  BFhandler()
bfserver = BFServer(handler)
bfserver.listen() 
