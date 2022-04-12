# NmapRecoonScanner
Tools for Red Team Recon

## Install Requirement
```
pip install -r requirements.txt
```

## How to Execute this tool ?
```
python3 port_scanner.py [nmap_target_host][nmap_port_scanner_arguments][nmap_port_scanner_result_search_key]
```

+ nmap_target_host : One target Host (ex : 127.0.0.1)
+ nmap_port_scanner_arguments : nmap port scanner arguments (ex : -T4 -sT)
+ nmap_port_scanner_result_search_key : Scanner result search key, default "all" will print every thing :)

### Example CMD : 
```
python port_scanner.py '192.168.13.134' '-T4 -sT' 'all'
```