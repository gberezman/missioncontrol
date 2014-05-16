from time import sleep,time
import serial
from parser import Parser

current_milli_time = lambda: int(round(time() * 1000))

class ArduinoSerial:

    def __init__(self, port = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00", baudrate = 115200, timeout=0):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.port.setDTR(level=False)
        sleep(2)
        self.port.flush()

    def read(self):
        result = self.port.readline()
        if result:
            print "From arduino: {}".format( result )
        return result

    def write(self, message):
        print "To arduino:   {}".format( message )
        self.port.write( message )

class StubbedArduinoSerial:
    def __init__(self):
        self.__readResponse = None
        self.__lastWrite = None
        self.__sentMessages = []

    def setReadResponse(self, readResponse):
        self.__readResponse = readResponse

    def getLastWrite(self):
        return self.__lastWrite

    def read(self): 
        return self.__readResponse

    def write(self, message):
        self.__lastWrite = message
        self.__sentMessages.append( message )

    def hasSent(self, message):
        return self.__sentMessages.count( message ) > 0

class ArduinoMatrixDriver:
    
    def __init__(self, serial):
        self.serial = serial

    def setMeter(self, meterId, value):
        self.serial.write( "M {} {}\n".format( meterId, value ) ) 

    def setNumber(self, numberId, value):
        self.serial.write( "N {} {}\n".format( numberId, value ) )

    def setInco(self, lo, hi):
        self.serial.write( "I {} {}\n".format( lo, hi ) )

    def setIncoColor(self, values):
        self.serial.write( "C {}\n".format( values ) )

    def ledOn(self, ledId):
        self.serial.write( "L {} 1\n".format( ledId ) )

    def ledOff(self, ledId):
        self.serial.write( "L {} 0\n".format( ledId ) )

    def setLed(self, ledId, state):
        if state:
            self.ledOn(ledId)
        else:
            self.ledOff(ledId)
