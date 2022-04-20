#!/usr/bin/python3
# -*- coding=utf-8 -*-

from ast import arguments
from plistlib import load
import nmap
import json
from sys import argv
import argparse
from src import common
######################################
# 2022-04-16 - Steven Chiu
# ArgumentParser
######################################

# Initialize parser
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument('--host', type=str, default="")
parser.add_argument('--nmaparg', type=str, default="")
parser.add_argument('--searchKey', type=str, default="")

# Read arguments from cmd
args = parser.parse_args()

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
    load_jsonObj = common.convert_list_to_json(recon_raw_result);
    # default = "all"
    get_item_by_key = common.get_value_by_key_fromJson(load_jsonObj, search_key);
    print(get_item_by_key);

    
if __name__ == '__main__':
    # 2022-4-16 - Steven Chiu - change parameter to match ArgumentParser
    nmap_port_scanner(args.host, args.nmaparg, args.searchKey);