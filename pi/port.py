from time import sleep
from parser import Parser
import serial

class Port:

    def __init__(self, commandFactory, port = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00", baudrate = 115200, timeout=0):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.port.setDTR(level=False)
        sleep(2)
        self.port.flush()
        self.commandFactory = commandFactory

    def readCommand(self):
        result = self.port.readline()

        if result:
            try:
                print "Received command {}".format( result )
                parser = Parser( result )
                return self.commandFactory.getCommand( parser )
            except ValueError:
                pass

    def write(self, message):
        print "Sending {}".format( message )
        self.port.write( message )

    def setMeter(self, meterId, meterValue):
        self.write( "Meter {} {}\n".format( meterId, meterValue ) ) 

    def ledOn(self, ledId):
        self.write( "LED {} on\n".format( ledId ) )

    def ledOff(self, ledId):
        self.write( "LED {} off\n".format( ledId ) )

class StubbedPort:
    def readCommand(self): pass
    def write(self, message): pass
    def setMeter(self, meterId, meterValue): pass
    def ledOn(self, ledId): pass
    def ledOff(self, ledId): pass
