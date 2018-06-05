import requests
import time

Server = "http://127.0.0.1:8001"
while True:
    r = requests.get(Server)
    print r.text
    time.sleep(3.0)

