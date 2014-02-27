#!/usr/bin/env python 

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

lastBoardLedFlip = current_milli_time()
flipBoardLed = False

def state():
    global flipBoardLed
    while True:
        bytes = arduinoSerial.read()
        if( len(bytes) > 0 ):
            print( "external led: " + bytes[0] )
            arduinoSerial.write( bytes[0] )
        if( flipBoardLed ): 
            arduinoSerial.write( boardLed )
            flipBoardLed = False

def mainLoop():
    global boardLed
    global lastBoardLedFlip
    global flipBoardLed

    while True:
        try: 
            if( current_milli_time() - lastBoardLedFlip > 500 ):
                lastBoardLedFlip = current_milli_time()
                if( boardLed == b'+' ):
                    print( "board LED: off" )
                    boardLed = b'-'
                else:
                    print( "board LED: on" )
                    boardLed = b'+'
                flipBoardLed = True

        except KeyboardInterrupt:
            exit()

mainThread = threading.Thread( target = mainLoop )
sendStateThread = threading.Thread( target = state )

mainThread.start()
sendStateThread.start()
