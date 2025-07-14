import subprocess
import os

def run_whatweb(target, out_dir):
    out_file = os.path.join(out_dir, 'whatweb.txt')
    cmd = ["whatweb", target]
    with open(out_file, 'w') as f:
        subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)
    return out_file
