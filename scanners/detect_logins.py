import requests
from bs4 import BeautifulSoup

def find_login_forms(gobuster_file, target):
    login_forms = set()
    # Always check the exact target URL (including any path)
    if not str(target).startswith("http"):
        base_url = f"http://{target}"
    else:
        base_url = target
    try:
        resp = requests.get(base_url, timeout=5)
        soup = BeautifulSoup(resp.text, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            if 'login' in str(form).lower():
                login_forms.add(base_url)
    except Exception:
        pass

    # Check Gobuster results as before
    with open(gobuster_file) as f:
        for line in f:
            if "Status: 200" in line:
                url = line.split()[0]
                try:
                    resp = requests.get(url, timeout=5)
                    soup = BeautifulSoup(resp.text, 'html.parser')
                    forms = soup.find_all('form')
                    for form in forms:
                        if 'login' in str(form).lower():
                            login_forms.add(url)
                except Exception:
                    continue
    return list(login_forms)
