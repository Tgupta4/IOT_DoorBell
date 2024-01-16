cloudinary = {
    "key": "KEY",
    "secret": "SECRET_KEY",
    "env": "ENVIRNMENT",
    "name": "NAME"
}

ifttt = {
    "url": "URL_HERE",

    "values": {
        "value1": "PHONE_NUMBER",
        "value2": "MESSAGE_TO_SEND" # don't change this
    }
}
# To turn on server processing write "True"
send_image_to_server = False

# Replace with the IP address of your Laptop Server device    
server_IP_address = 'http://192.168.1.126:47947'

# Replace with the IP address of your Smart Bulb    
buld_on_ip="http://192.168.1.127/"

# Replace with the IP address of your Android device    
android_ip = '192.168.106.163'  # False or ip of android device to recieve message on android app

# Should match the port in your Android app`
android_port = 49100  # if app message not arrived use 49162 port number 