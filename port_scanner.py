# -*- coding:utf-8 -*-

from ast import arguments
from plistlib import load
import nmap
import json
from sys import argv

if len(argv) >=4:
    nmap_target_host                    = argv[1]
    nmap_port_scanner_arguments         = argv[2]
    nmap_port_scanner_result_search_key = argv[3]
else:
    print('參數錯誤，正確參數為：python3 port_scanner.py [nmap_target_host][nmap_port_scanner_arguments][nmap_port_scanner_result_search_key]')
    quit()

######################################
# 2022-04-12 - Steven Chiu
# Convert list obj to json obj
######################################
def convert_list_to_json(listObj):
    json_object = json.dumps(listObj);
    return json_object;

######################################
# 2022-04-12 - Steven Chiu
# Get value from json obj by key
######################################
def get_value_by_key_fromJson(jsonObj, key):
    _jsonObj = json.loads(jsonObj);
    
    if key == "all":
        return _jsonObj;
    else:
        get_value_by_key = _jsonObj[key];
        return json.dumps(get_value_by_key);

######################################
# 2022-04-12 - Steven Chiu
# NMAP port scanner
######################################
def nmap_port_scanner(target_host, port_scanner_arguments, search_key):
    # Creat port scan event
    port_scanner_event = nmap.PortScanner()
    # Port scan raw result (raw data)
    recon_raw_result = port_scanner_event.scan(hosts=target_host,arguments=port_scanner_arguments);
    # Get port scan result by key
    load_jsonObj = convert_list_to_json(recon_raw_result);
    # default = "all"
    get_item_by_key = get_value_by_key_fromJson(load_jsonObj, search_key);
    print(get_item_by_key);
    print(type(get_item_by_key));
    
    
if __name__ == '__main__':
    nmap_port_scanner(nmap_target_host, nmap_port_scanner_arguments, nmap_port_scanner_result_search_key);