import json
import threading
from socket import *

class TopologyManager:

    servers = {}
    def __init__(self):
        topo   = json.load(open('config/topology.json'))
        for server in topo['servers']:
            self.servers[server['id']] = server['lid']
    
    def get_Bloom_filter(self,path):
        path   = path.split(" ")
        source = path[0]
        group  = path[1] 
        print "Creating BF from " + source + " to " + group
        groups  = json.load(open('config/groups.json'))
        names   = group.split(".")
        members = set(groups['groups']['all']['members'])
        for name in names:
            members = members & set(groups['groups'][name]['members'])
        Bloom_filter = 0
        for member in members:
            Bloom_filter = Bloom_filter | self.servers[member]
        return Bloom_filter
            
    def listen(self):
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('', 8000))
        while True:
            path, source = s.recvfrom(1024)
            response      = self.get_Bloom_filter(path)
            s.sendto(str(response),source)
            
if __name__ == "__main__":
    tm = TopologyManager()
    tm.listen()
    
