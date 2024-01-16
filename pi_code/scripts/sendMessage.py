import requests
from credentials import ifttt
import urllib.parse
print(ifttt)
url = ifttt["url"]
values = ifttt['values']

def sendSMS(msg=False, phone=False):
    print("send sms")
    values['value2'] = msg or "No Message given"
    if(phone):
        values['value1'] = phone
    x=requests.get(url + "?" + urllib.parse.urlencode(values))
    print("SMS sent")
