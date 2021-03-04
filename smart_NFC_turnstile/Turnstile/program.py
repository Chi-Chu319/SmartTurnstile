import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from picamera import PiCamera
import requests
from time import sleep
import datetime
from multicolorLED import MulticolorLED
from TempSensor import TempSensor
import json


with open('./config.json', 'r') as f:
    config = json.load(f)

# pin for w1 interface is set to gpio12, modify it in /boot/config.txt
# pins
red_pin = 21
green_pin = 20
blue_pin = 16
# the photo will be sent to the server to store so its not necessarily available on the turnstile
photoPath = './photos' 
tempSensor = TempSensor()

# declare all the global varibles.
multicolorLed = MulticolorLED(red_pin, green_pin, blue_pin)
reader = SimpleMFRC522()
camera = PiCamera()
# if the camera is placed upside down 
camera.rotation = 180


# def Authen_fail():
#     print('Authentication fails')
#     multicolorLed.Red()
#     sleep(3)
#     multicolorLed.White()

# def Authen_succeed():
# 	multicolorLed.Green()

endpoint = config["endpoint"] + ":" + str(config["port"])



while True:
	# read the UID from the card
	multicolorLed.White()
	print("Welcome! please place your card in proximity to the reader.")
	try:
		print("Ready to read.")
		Id, AuthenKey = reader.read()
	    UID_hex = hex(Id)[2:]
		data = {'keyUID':UID_hex}
		print("Your card UID is: "+UID_hex)
		r = requests.post(url=endpoint+"/IOT/VerifyAuth", data=data)
		responds = r.json()
		exists = responds["exists"]
		message = responds["message"]
		enterId = responds["enterId"]	
		valid = responds["valid"]	
	except:
		# break the loop and start again when errors occur reading from the card
		multicolorLed.Red()
		print("error occors when reading from the tag")
		sleep(2)
		print("please try again")
		print()
		continue
	# finally:
	#     GPIO.cleanup()

	# when the enter is rejected
	print(message)
	sleep(1)
	if not valid:
		print("restarting...")
		multicolorLed.Red()
		sleep(2)
		print()
		continue

	
	multicolorLed.Yellow()
	print("processing...")
	sleep(2)



	print("Taking photo, please turn your face to the camera...")
	camera.start_preview()
	# time delay for the camera
	sleep(3)
	temperature = TempSensor.measureTemperature()
	camera.exif_tags['IFD0.Copyright'] = 'Copyright (c) 2020 Smart_Turnstile.'
	camera.capture(photoPath + '/foo.jpg')
	camera.stop_preview()



	print("Your temperature is: " + str(temperature))

	f = open(photoPath + '/foo.jpg', 'rb')
	files = {'photo': f}
	data = {"visitorId": enterId, "temperature": temperature}

	r = requests.post(url=endpoint+"/IOT/Visitors/Enter/UpdateInfo", data=data, files=files)
	responds =r.json()

	permission = responds["permission"]
	message = responds["message"]


	if not permission:
		multicolorLed.Red()
		print("You are suspected to have fever.")
		sleep(1)
		print(message)
		print()
		continue

	print("Your temperature is normal.")
	print(message)
	multicolorLed.Green()
	sleep(5)
	print()






