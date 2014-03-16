from time import sleep
import serial

class Port:

    def __init__(self, port = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00", baudrate = 115200, timeout=0):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.port.setDTR(level=False)
        sleep(2)
        self.port.flush()
    
        self.command = None
        self.idx = 0

    def nonBlockingRead(self):
        result = self.port.read()

    def readline(self):
        self.command = None
        self.idx = 0
        result = self.port.readline()
        if len(result) > 0:
            self.command = result.split()

    def write(self, message):
        self.port.write( message )

    def isEmpty(self):
        return self.command == None

    def token(self):
        return self.command[self.idx]

    def next(self):
        self.idx += 1
        return self.idx < len( self.command )

    def tokenAsInt(self):
        try:
            return int( self.command[self.idx] )
        except ValueError:
            return None

    def tokenAsBoolean(self):
        if( self.command[self.idx] == 'True' ):
            return True

        return False
