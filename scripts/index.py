import subprocess
from findFace import *
from uploadToCloudinary import UploadPhoto
from sendMessage import sendSMS
import requests
import time
import socket
import pyttsx3
from credentials import buld_on_ip
from credentials import android_ip
from credentials import android_port

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


# change ip of kauf bulb for visual alert
url_on = buld_on_ip+"light/kauf_bulb/turn_on"
url_off = buld_on_ip+"light/kauf_bulb/turn_off"

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
        if any(i in name for i in ACCESS_GRANTED_LIST):
            message += "\n Access Granted... Door Unlocked"
    else:
        message+=" Not in Database. \nDoor cannot be open"
        mssge1 = "Hello, There is someone at the door."

    ImgUrl = UploadPhoto(path)

    message += "\n Here is link of photo "+ImgUrl

    print(message)
    command_to_send = mssge1
    send_command(android_ip, android_port, command_to_send)
    sendSMS(message)
    trigger_blub()
    engine.say(message)
    # Wait for the speech to finish
    engine.runAndWait()
    
print('*****************************EXIT********************************')
