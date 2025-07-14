import requests
from bs4 import BeautifulSoup

def find_login_forms(gobuster_file, target):
    login_forms = []
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
                            login_forms.append(url)
                except Exception:
                    continue
    return login_forms
