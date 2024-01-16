# Project Setup and Usage Guide

## Setup Instructions:

### 1. Install Python Libraries:
   - Ensure that the required Python libraries are installed for your project.

### 2. Configure Device IPs:
   - Note down the IP addresses of the Android device, KAUF smart bulb, and server (laptop).
   - Config Smart bulb IP in `scripts/credentials.py` 

### 3. Configure Known Faces:
   - Open `scripts/findFace.py`.
   - Write the names of persons in sequence at line 16, like: `KNOWN_FACES = ["", "Tanish", "ABC", "XYZ"]`.

### 4. Configure Access Granted List:
   - Open `scripts/index.py`.
   - Write the names of persons with access granted at line 70, like: `ACCESS_GRANTED_LIST = ['Tanish', 'CCC', 'AAA']`.

### 5. Configure Phone Number to recieve SMS using ifttt:
   - open `scripts/credentials.py` line number 12 `Value1 = ""` write number on which you want to recieve sms
   - open index.py and edit number there too at line number 85

### 6. Connect Speaker:
   - Connect a speaker to the system for sound alerts.
   ### optional setting 
   -  we can config voice pitch, rate, voice
   -  Goto `scripts/index.py` there we can set at line number 16, 18, 20

### 7. Save Data Samples :
   - Add your photos in folder scripts/faceData after making the folder like person1, person2
   
   ### Other way to save sample data sample for laptop (server) 
   - Open `scripts/save_sample_face_data.py`.
   - Change the person folder names to [ "person1", "person2"] etc., in line 7.
   - Run the command: `python3 scripts/save_sample_face_data.py`.


## Running the System:

### 1. Run the System:
   - Execute the command: `python3 scripts/index.py`.

### 2. Door Bell Activation:
   - Press '1' on the keyboard to activate the doorbell.

## To activate server side processing:

### 3. Server Processing (In raspberry pi):
   - To enable server processing, open `scripts/credentials.py`.
   - Change the value to `True` : `send_image_to_server = False`.
   - Config Ip and port number at line number 13
   - Rerun the code in raspberry pi to apply changes
   - Run server script

### 4. Server Processing (Optional):
   - If server processing is enabled, image processing will be done on the laptop(server) and we need run the server and config the ip of server


# IoTDoorBell

built credentials.py file in scripts folder as

<pre>
#scripts/credentials.py
cloudinary = {
    "key": "YOUR_KEY",
    "secret": "YOUR_SECRET",
    "env": "YOUR_ENV_VARIABLE",
    "name": "YOUR_CLOUD_NAME"
}

ifttt = {
    "url": "IFTTT_WEBHOOK_URL",

    "values": {
        "value1": "PHONE_NUMBER",
        "value2": "MESSAGE_TO_SEND"
    }
}

server_IP_address = 'SERVER_IP'

buld_on_ip="KAUF_Bulb_IP"

android_ip = 'IP_of_Android_mobile' 

android_port = "port_Number"  

</pre>