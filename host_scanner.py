#!/usr/bin/python3
# -*- coding=utf-8 -*-

import nmap
import argparse
import json
from src import common

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument('--net', type=str, default="")

# Read arguments from cmd
args = parser.parse_args()

######################################
# 2022-04-20 - Steven Chiu
# NMAP host scanner
######################################
def nmap_host_scan(net):

    host_scanner_event = nmap.PortScanner();
    res_scan = host_scanner_event.scan(hosts=net, arguments="-sn -PE -n")
    print("starting:"+res_scan["nmap"]["command_line"])
    host_list=[]

    for ip in res_scan["scan"]:
        try:
            if res_scan["scan"][ip]["status"]["state"]=="up":
                IP=res_scan["scan"][ip]["addresses"]["ipv4"]
                host_list.append(IP)
        except Exception:
            pass
    
    jsonHost = common.convert_list_to_json(host_list)

    print(jsonHost)
    return jsonHost


if __name__ == '__main__':
    nmap_host_scan(args.net);
