import subprocess
import os


def print_gobuster_progress(line_count):
    total_lines = 100
    percent = min(int((line_count / total_lines) * 100), 100)
    bar_len = 30
    filled_len = int(bar_len * percent // 100)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)
    print(f"\r[Gobuster] [{bar}] {percent}%", end='')

import re

def strip_ansi_progress(text):
    return re.sub(r'\x1b\[2K', '', text)

def run_gobuster(target, out_dir):
    out_file = os.path.join(out_dir, 'gobuster.txt')
    wordlist = 'wordlists/common.txt'  # Use common.txt for directory enumeration
    url = f"http://{target}/" if not str(target).endswith('/') else f"http://{target}"
    cmd = ["gobuster", "dir", "-u", url, "-w", wordlist]
    line_count = 0
    with open(out_file, 'w') as f:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            clean_line = strip_ansi_progress(line)
            f.write(clean_line)
            line_count += 1
            print_gobuster_progress(line_count)
        process.wait()
    print()
    return out_file
