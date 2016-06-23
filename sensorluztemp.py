#!/bsolre/bin/python

import signal
import sys

import time
import pyupm_grove as grove
import pyupm_i2clcd as lcd

def interruptHandler(signal, frame):
	sys.exit(0)

if __name__=='__main__':
	signal.signal(signal.SIGINT, interruptHandler)

	myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
	sensorluz = grove.GroveLight(0)
	sensortemp = grove.GroveTemp(1)

	colorR = 255;
	colorG = 0;
	colorB = 0;
	myLcd.setColor(colorR, colorG, colorB)

	# Read the input and print, waiting 1/2 second between readings
	while True:
		valorSensor = sensorluz.value()
		valorSensor2 = sensortemp.value()
		myLcd.setCursor(0,0)
		myLcd.write("Luz %6d"%valorSensor)
		myLcd.setCursor(1,0)
		myLcd.write("Temp %6d"%valorSensor2)
		time.sleep(0.5)
	del sensorluz
