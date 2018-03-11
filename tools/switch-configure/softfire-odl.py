import json
import itertools
import httplib

def post_flow (flow_json,flow_name):
    api_token = "75654a9a3498641a63aa3b12b3940ba4"
    odl_host  = "10.44.56.254"
    switch_id = "openflow:247147007260025"
    odl_path  = "/restconf/config/opendaylight-inventory:nodes/node/%s/table/2/flow/%s"%(switch_id,flow_name)
    headers = {
        'Content-Type': "application/json",
        'Accept': "application/json",
        'API-token': api_token,
        'Cache-Control': "no-cache",
    }
    conn = httplib.HTTPConnection(odl_host, 8001)
    conn.request("PUT", odl_path, flow_json,headers)
    #conn.request("DELETE", odl_path,None, headers)
    response = conn.getresponse()
    print response.status, response.reason

add_new_flow = """
{
      "flow-node-inventory:flow": [
        {
          "id": "%s",
          "flow-name": "%s",
          "match": {
            "ethernet-match": {
              "ethernet-destination":{
              	"address" :"00:00:00:00:00:0%x"
              },
              "ethernet-type": {
                "type": 2048
              }
            }
          },
          "priority": 100,
          "table_id": 2,
          "cookie": 134217728,
          "instructions": {
            "instruction": [
              {
                "order": 0,
                "apply-actions": {
                  "action": [%s
                  ]
                }
              }
            ]
          }
        }
      ]
    }
"""
output_node_connector = """
                        {
                          "order": %s,
                          "output-action": {
                            "output-node-connector":"%s"
                          }
                        },
"""
topo         = json.load(open('../../config/topology.json'))
servers      = topo['servers']
flow_counter = 1
for x in range(1, len(servers)+1):
    for paths in itertools.combinations(servers, x):
        Bloom_filter = 0
        flow_id      = "BF-flow-" + str(flow_counter)
        print "------------------------"
        print flow_id
        output_counter = 0
        output_nodes   = ""
        for path in paths:
            Bloom_filter = Bloom_filter | path['lid']
            output_node = output_node_connector%(output_counter,path['port'])
            output_nodes += output_node.rstrip('\n')
            output_counter +=1
        post_flow (add_new_flow%(flow_id,flow_id,Bloom_filter,output_nodes.rstrip(',')),flow_id)
        flow_counter +=1

    
 
