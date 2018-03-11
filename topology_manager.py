import json

class TopologyManager:

    servers = {}
    groups  = {}
    
    def __init__(self):
        self.groups = json.load(open('config/groups.json'))
        topo        = json.load(open('config/topology.json'))
        for server in topo['servers']:
            self.servers[server['id']] = server['lid']
        print self.servers
        
    def get_Bloom_filter(self,group):
        for server in  self.groups['groups'][group]['members']:
            print self.servers[server]
    
