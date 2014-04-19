from time import sleep
import serial
from parser import Parser

class ArduinoSerial:

    def __init__(self, port = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00", baudrate = 115200, timeout=0):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.port.setDTR(level=False)
        sleep(2)
        self.port.flush()

    def read(self):
        result = self.port.readline()
        print "From arduino: {}".format( result )
        return result

    def write(self, message):
        print "To arduino:   {}".format( message )
        self.port.write( message )

class StubbedArduinoSerial:
    def __init__(self):
        self.__readResponse = None
        self.__lastWrite = None

    def setReadResponse(self, readResponse):
        self.__readResponse = readResponse

    def getLastWrite(self):
        return self.__lastWrite

    def read(self): 
        return self.__readResponse

    def write(self, message):
        self.__lastWrite = message

class ArduinoMatrixDriver:
    
    def __init__(self, serial):
        self.serial = serial

    def setMeter(self, meterId, meterValue):
        self.serial.write( "Meter {} {}\n".format( meterId, meterValue ) ) 

    def ledOn(self, ledId):
        self.serial.write( "LED {} on\n".format( ledId ) )

    def ledOff(self, ledId):
        self.serial.write( "LED {} off\n".format( ledId ) )

    def setLed(self, ledId, state):
        if state:
            self.ledOn(ledId)
        else:
            self.ledOff(ledId)
