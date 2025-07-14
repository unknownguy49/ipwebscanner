import subprocess
import os

def run_gobuster(target, out_dir):
    out_file = os.path.join(out_dir, 'gobuster.txt')
    wordlist = 'wordlists/usernames.txt'  # Replace with your dir wordlist
    cmd = ["gobuster", "dir", "-u", f"http://{target}", "-w", wordlist]
    with open(out_file, 'w') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)
    return out_file
