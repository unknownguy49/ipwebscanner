import subprocess
import os

def run_hydra(target, login_forms, out_dir):
    for url in login_forms:
        out_file = os.path.join(out_dir, f"hydra_{url.replace('/', '_')}.txt")
        cmd = [
            "hydra",
            "-L", "wordlists/usernames.txt",
            "-P", "wordlists/passwords.txt",
            target,
            "http-post-form",
            f"{url}:username=^USER^&password=^PASS^:F=Invalid"
        ]
        with open(out_file, 'w') as f:
            subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT)
