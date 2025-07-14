import subprocess
import os

def run_nmap(target, out_dir):
    out_file = os.path.join(out_dir, 'nmap.txt')
    cmd = ["nmap", "-sV", target]
    with open(out_file, 'w') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)
    return out_file
