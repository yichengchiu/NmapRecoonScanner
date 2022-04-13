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

### Scan Result Sample:
```
{
  "192.168.13.134": {
    "hostnames": [
      {
        "name": "",
        "type": ""
      }
    ],
    "addresses": {
      "ipv4": "192.168.13.134"
    },
    "vendor": {

    },
    "status": {
      "state": "up",
      "reason": "syn-ack"
    },
    "tcp": {
      "22": {
        "state": "open",
        "reason": "syn-ack",
        "name": "ssh",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "80": {
        "state": "open",
        "reason": "syn-ack",
        "name": "http",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "110": {
        "state": "open",
        "reason": "syn-ack",
        "name": "pop3",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "143": {
        "state": "open",
        "reason": "syn-ack",
        "name": "imap",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "902": {
        "state": "open",
        "reason": "syn-ack",
        "name": "iss-realsecure",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "3128": {
        "state": "open",
        "reason": "syn-ack",
        "name": "squid-http",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "3389": {
        "state": "open",
        "reason": "syn-ack",
        "name": "ms-wbt-server",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      },
      "8080": {
        "state": "open",
        "reason": "syn-ack",
        "name": "http-proxy",
        "product": "",
        "version": "",
        "extrainfo": "",
        "conf": "3",
        "cpe": ""
      }
    }
  }
}
```