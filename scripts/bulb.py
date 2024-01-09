import requests
import time
url_on = "http://192.168.1.127/light/kauf_bulb/turn_on"
url_off = "http://192.168.1.127/light/kauf_bulb/turn_off"
i=0
while i<10:
    response = requests.post(url_off)
    time.sleep(1)
    i += 1
    requests.post(url_on)
    time.sleep(1)
    i += 1