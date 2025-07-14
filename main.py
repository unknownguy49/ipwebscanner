import sys
import os
from scanners.nmap_scan import run_nmap
from scanners.gobuster_scan import run_gobuster
from scanners.whatweb_scan import run_whatweb
from scanners.nikto_scan import run_nikto
from scanners.detect_logins import find_login_forms
from scanners.hydra_brute import run_hydra

def ensure_output_dir(target):
    out_dir = os.path.join('output', target)
    os.makedirs(out_dir, exist_ok=True)
    return out_dir

def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <target>')
        sys.exit(1)
    target = sys.argv[1]
    out_dir = ensure_output_dir(target)
    print(f"[+] Scanning {target}, results will be saved in {out_dir}")
    nmap_file = run_nmap(target, out_dir)
    gobuster_file = run_gobuster(target, out_dir)
    whatweb_file = run_whatweb(target, out_dir)
    nikto_file = run_nikto(target, out_dir)
    login_forms = find_login_forms(gobuster_file, target)
    if login_forms:
        run_hydra(target, login_forms, out_dir)
    print("[+] Scan complete.")

if __name__ == "__main__":
    main()
