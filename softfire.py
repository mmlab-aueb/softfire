from topology_manager      import TopologyManager
from proxies.http          import HTTTProxy
from proxies.proxylistener import ProxyListener
from bf                    import PacketHandler,BFServer, BFClient
from socket                import *

class SoftFIRE(ProxyListener, PacketHandler):

    def __init__(self):
        self.bfclient = BFClient()
        self.bfserver = BFServer(self)
        self.wait_resp= threading.Event()
        wait_resp.unset()
        self.bfserver.nb_listen()
        
    def from_proxy(self,path):
        wait_resp.unset()
        self.response = ""
        options = path.split["/"]
        method  = options[1]
        uri     = options[2]
        bf      = self.get_BF(uri)
        self.bfclient.send_packet(bf,path)
        if method == "GET": wait_resp.wait(3)
        return self.response
        
    def handle_packet(selft,packet):
        self.response = packet
        wait_resp.set()
        print packet
        
    def listen_for_HTTP(self):
        proxy = HTTTProxy()
        proxy.listen(8080,self)
    
    def get_BF(self, group):
        s = socket(AF_INET, SOCK_DGRAM)
        s.sendto("aueb-02 " + group,('',8000))
        bf, tm = s.recvfrom(1024)
        return bf
        
if __name__ == "__main__":
    softfire =  SoftFIRE()
    softfire.listen_for_HTTP()
    
