#!/usr/bin/python 

import json
import requests 
from requests.auth import HTTPBasicAuth 
 
def http_get(url):     
	url= url     
	headers = {'Content-Type':'application/json'}     
	resp = requests.get(url,headers=headers,auth=HTTPBasicAuth('admin', 'admin'))     
	return resp           
if __name__ == "__main__":     
	url = 'http://127.0.0.1:8181/restconf/config/opendaylight-inventory:nodes/node/openflow:1/flow-node-inventory:table/0'     
	resp = http_get(url)    
	j = json.loads(resp.content)
	print len(j["flow-node-inventory:table"][0]["flow"])
