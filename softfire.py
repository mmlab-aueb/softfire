from topology_manager      import TopologyManager
from proxies.http          import HTTTProxy
from proxies.proxylistener import ProxyListener
from bf                    import PacketHandler,BFServer, BFClient


class SoftFIRE(ProxyListener, PacketHandler):
    bfclient = BFClient()
    bfserver = BFServer()
    
    
    def __init__(self):
        bfserver.nb_listen()
        
    def from_proxy(self,path):
        return "Hello"
        
    def handle_packet(packet):
        print packet
        
    def listen_for_HTTP(self):
        proxy = HTTTProxy()
        proxy.listen(8080,self)
        
if __name__ == "__main__":
    softfire =  SoftFIRE()
    softfire.listen_for_HTTP()
    
