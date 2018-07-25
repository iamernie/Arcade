import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# Grab the system variables
emulator= sys.argv[1]

#If Statement
if emulator == "nes": 
	GPIO.output(18,GPIO.LOW)
elif emulator == "snes":
	GPIO.output(23,GPIO.LOW)
else:
	GPIO.output(18,GPIO.HIGH)
	GPIO.output(23,GPIO.HIGH)



print emulator
