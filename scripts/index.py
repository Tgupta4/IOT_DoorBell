
# 1. save photo with name using opencv
# 2. upload photo to server
import subprocess
from findFace import *
from uploadToCloudinary import UploadPhoto
from sendMessage import sendSMS
import requests
import time
import socket
import pyttsx3

# Initialize the Pyttsx3 engine
engine = pyttsx3.init()
# Set the voice to use
engine.setProperty('voice', 'english-us')
# Set the speech rate
engine.setProperty('rate', 150)
# Set the pitch
engine.setProperty('pitch', 40)

def send_command(host, port, command):
    if(host):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((host, port))
            s.sendall(command.encode())
            print(f"Sent command: {command}")
    else:
        print(f"No Host Present: Sent command: {command}")

# Replace with the IP address of your Android device    
android_ip = '192.168.106.163'  # False or ip of android device to recieve message on android app
# Should match the port in your Android app`
port = 49100  # if app message not arrived use 49162 port number 

# change ip of kauf bulb for visual alert
url_on = "http://192.168.1.127/light/kauf_bulb/turn_on"
url_off = "http://192.168.1.127/light/kauf_bulb/turn_off"

print('*****************************START*******************************')

def trigger_blub():
    try:
        i=0
        while i<10:
            requests.post(url_off)
            time.sleep(1)
            requests.post(url_on)
            time.sleep(1)
            i += 1
    finally:
        print("trigger_blub: okay")

while True:
    z = input('Press 1 to Capture: \n')
    if(z!='1'):
        break
    [path,username] = Capture_Face()
    print("this is index py-> capture face")
    print(username)
    print(">> this above")
    message = "Hello, There is someone at the door.\n"
    message += "Name:"
    
    if(username):
        name=username
        message += username
        mssge1 = f"Hello, There is {username} at the door."
        # Add name to grant the access
        ACCESS_GRANTED_LIST=['Tanish','CCC','AAA']
        trigger_blub()
        if any(i in name for i in ACCESS_GRANTED_LIST):
            message += "\n Access Granted... Door Unlocked"
    else:
        message+=" Not in Database. \nDoor cannot be open"
        mssge1 = "Hello, There is someone at the door."

    ImgUrl = UploadPhoto(path)

    message += "\n Here is link of photo "+ImgUrl

    print(message)
    command_to_send = mssge1
    send_command(android_ip, port, command_to_send)
    sendSMS(message)
    engine.say(message)
    # Wait for the speech to finish
    engine.runAndWait()
    
print('*****************************EXIT********************************')
