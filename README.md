# IP Scanner & Brute Force Toolkit

This toolkit automates reconnaissance and brute force attacks against a target IP or domain. It runs several popular tools in sequence and saves all results in the `output/` folder.

## Features & Underlying Commands

**Nmap (Port Scan):**
Runs a basic port scan to discover open ports.

```
nmap <target>
```

**Gobuster (Directory Enumeration):**
Finds common directories and files on web servers.

```
gobuster dir -u http://<target>/ -w wordlists/common.txt
```

**WhatWeb (Web Fingerprinting):**
Identifies technologies and gathers metadata from web servers.

```
whatweb <target>
```

**Nikto (Web Vulnerability Scan):**
Performs a fast scan for interesting files and vulnerabilities (limited to 2 minutes for speed).

```
nikto -h <target> -Tuning 1 -maxtime 2m
```

**Hydra (Brute Force Login):**
If login forms are detected, attempts brute force using provided wordlists.

```
hydra -L wordlists/usernames.txt -P wordlists/passwords.txt <target> http-post-form "/login.php:username=^USER^&password=^PASS^:F=Invalid"
```

## Usage

```bash
python main.py <target>
```

**Requirements:**

- nmap
- gobuster
- hydra
- whatweb
- nikto

All results are saved in the `output/` folder, organized by target.
