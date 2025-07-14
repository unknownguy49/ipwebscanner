import subprocess
import os


def print_whatweb_progress(line_count):
    total_lines = 50
    percent = min(int((line_count / total_lines) * 100), 100)
    bar_len = 30
    filled_len = int(bar_len * percent // 100)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)
    print(f"\r[WhatWeb] [{bar}] {percent}%", end='')

def run_whatweb(target, out_dir):
    out_file = os.path.join(out_dir, 'whatweb.txt')
    cmd = ["whatweb", "--no-color", target]
    line_count = 0
    with open(out_file, 'w') as f:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        for line in process.stdout:
            f.write(line)
            line_count += 1
            print_whatweb_progress(line_count)
        process.wait()
    print()
    return out_file
