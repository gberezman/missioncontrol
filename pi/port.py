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

        if not result:
            return None
        print "received command {}".format( result )

        try:
            parser = Parser( result )
            return self.commandFactory.getCommand( parser )
        except ValueError:
            return None

    def write(self, message):
        self.port.write( message )
