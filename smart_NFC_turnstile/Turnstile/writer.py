import RPi.GPIO as GPIO 
from mfrc522 import SimpleMFRC522
import datetime

reader = SimpleMFRC522()

# the authentication data
Key = input('Auteh Key:')
#Id = "Key1"



text = Key

try:
        print("Now place your tag to write")
        reader.write(text)
        print("AuthenKey: " +  text)
        print("Written")
finally: 
        GPIO.cleanup()

