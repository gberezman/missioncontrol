#!/usr/bin/env python

from time import sleep
import serial
import threading

serialDevice = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00"
baudRate = 115200

arduinoSerial = serial.Serial(serialDevice, baudRate)
arduinoSerial.setDTR(level=False)

sleep(2)

arduinoSerial.flush()

sleep_seconds = .05

def mainLoop():
	while True:
		print "off"
		arduinoSerial.write( b'-' )
		sleep(sleep_seconds)
		print "on"
		arduinoSerial.write( b'+' )
		sleep(sleep_seconds)

mainThread = threading.Thread( target = mainLoop )
mainThread.start()
