from topology_manager      import TopologyManager
from proxies.http          import HTTTProxy
from proxies.proxylistener import ProxyListener
from bf                    import PacketHandler,BFServer, BFClient
import threading

class SoftFIRE(ProxyListener, PacketHandler):

    def __init__(self):
        self.bfclient = BFClient()
        self.bfserver = BFServer(self)
        self.wait_resp= threading.Event()
        self.wait_resp.clear()
        self.bfserver.nb_listen()
        
    def from_proxy(self,path):
        self.wait_resp.clear()
        self.response = "Empty response"
        self.bfclient.send_packet(15,path)
        self.wait_resp.wait(3)
        return self.response
        
    def handle_packet(self,packet):
        self.response = packet
        self.wait_resp.set()
        print packet
        
    def listen_for_HTTP(self):
        proxy = HTTTProxy()
        proxy.listen(8080,self)
        
if __name__ == "__main__":
    softfire =  SoftFIRE()
    softfire.listen_for_HTTP()
    
