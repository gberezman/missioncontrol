from time import sleep
import serial
import threading

serialDevice = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00"
baudRate = 115200

arduinoSerial = serial.Serial(serialDevice, baudRate)
arduinoSerial.flush()

def mainLoop():
	while True:
		try: 
			print "on"
			arduinoSerial.write( b'+' )
			sleep(1)
			print "off"
			arduinoSerial.write( b'-' )
			sleep(1)
		except KeyboardInterrupt:
			exit()

mainThread = threading.Thread( target = mainLoop )

mainThread.start()
