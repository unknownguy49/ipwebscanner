import subprocess
import os

def run_nikto(target, out_dir):
    out_file = os.path.join(out_dir, 'nikto.txt')
    cmd = ["nikto", "-h", target]
    with open(out_file, 'w') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)
    return out_file
