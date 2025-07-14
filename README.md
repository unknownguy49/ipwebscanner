# IP Scanner & Brute Force Toolkit 🔍

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

Example Output
Saved in output/ folder.

---

## 🧪 Sample Hydra Format Explained

```bash
hydra -L wordlists/usernames.txt -P wordlists/passwords.txt 10.10.10.10 http-post-form "/login.php:username=^USER^&password=^PASS^:F=Invalid"
```
Modify F= depending on the failed login message you find.

You can automate this using requests + BeautifulSoup later to fingerprint HTML forms.
