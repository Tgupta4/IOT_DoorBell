
# 1. save photo with name using opencv
# 2. upload photo to server

from findFace import *
from uploadToCloudinary import UploadPhoto
from sendMessage import sendSMS
# import requests
import time
url_on = "http://192.168.1.127/light/kauf_bulb/turn_on"
url_off = "http://192.168.1.127/light/kauf_bulb/turn_off"
print('*****************************START*******************************')
while True:
    z = input('Press 1 to Capture: \n')
    if(z!='1'):
        break
    [path,username] = Capture_Face()
    message = "Hello, There is someone at the door.\n"
    message += "Name:"
    if(username):
        name=username
        message += username
        ACCESS_GRANTED_LIST=['Tanish','CCC','AAA']
        if any(i in name for i in ACCESS_GRANTED_LIST):
            i=0
            while i<10:
                requests.post(url_off)
                time.sleep(1)
                requests.post(url_on)
                time.sleep(1)
                i += 1
            message += "\n Access Granted... Door Unlocked"
    else:
        message+=" Not in Database. \nDoor cannot be open"

    ImgUrl = UploadPhoto(path)

    message += "\n Here is link of photo "+ImgUrl

    print(message)
    #
    # sendSMS(message,phone number)
    sendSMS(message)
print('*****************************EXIT********************************')
