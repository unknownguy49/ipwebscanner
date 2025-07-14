# IP Scanner & Brute Force Toolkit

Takes an IP or domain and performs:

- Nmap service scan
- Gobuster dir enum
- WhatWeb fingerprint
- Nikto web vuln scan
- Hydra brute force on detected login pages

## Usage

```bash
python main.py <target>
```

Tools Required:

- nmap
- gobuster
- hydra
- whatweb
- nikto

Example output is saved in the output/ folder.
