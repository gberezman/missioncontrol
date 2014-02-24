from time import sleep
from time import time
import serial
import threading

serialDevice = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00"
baudRate = 115200

arduinoSerial = serial.Serial(port=serialDevice, baudrate=baudRate, timeout=0)
arduinoSerial.setDTR(level=False)
sleep(2)
arduinoSerial.flush()

current_milli_time = lambda: int(time() * 1000)

boardLed = b'+'
extLed = b'x'

lastBoardFlip = current_milli_time()

def state():
	while True:
		arduinoSerial.write( boardLed )
		arduinoSerial.write( extLed )
		sleep(.1)

def mainLoop():
	global extLed
	global boardLed
	global lastBoardFlip

	while True:
		try: 
			# bytes = arduinoSerial.read()
			# if( len(bytes) > 0 ):
				# extLed = bytes[0]

			if( current_milli_time() - lastBoardFlip > 500 ):
				lastBoardFlip = current_milli_time()
				if( boardLed == b'+' ):
					print "flipping to off"
					boardLed = b'-'
					extLed = b'x'
				else:
					print "flipping to on"
					boardLed = b'+'
					extLed = b'o'
			sleep(.1)

		except KeyboardInterrupt:
			exit()

mainThread = threading.Thread( target = mainLoop )
stateThread = threading.Thread( target = state )

mainThread.start()
stateThread.start()
