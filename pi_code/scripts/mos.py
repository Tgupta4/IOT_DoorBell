#  If we need to implement the morse code then we can add this code
import requests
import time
# Replace these placeholder URLs with the actual URLs of your LED control endpoints
url_on = "http://192.168.1.127/light/kauf_bulb/turn_on"
url_off = "http://192.168.1.127/light/kauf_bulb/turn_off"

morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

def mos_dot():
    requests.post(url_off)
    time.sleep(0.75)
    requests.post(url_on)

def mos_dash():
    requests.post(url_off)
    time.sleep(1.50)
    requests.post(url_on)

def convert_to_morse(text):
    encoded_morse = ""
    for character in text.upper():
        if character in morse_code_dict:
            morse_code = morse_code_dict[character]
            for symbol in morse_code:
                if symbol == '.':
                    mos_dot()
                elif symbol == '-':
                    mos_dash()
        else:
            # Handle invalid characters
            print("Invalid character:", character)

# Example usage
text = "tanish"  
convert_to_morse(text)
