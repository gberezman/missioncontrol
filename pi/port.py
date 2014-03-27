from time import sleep
import serial

class Command:

    def __init__(self, text):
        self.index = 0
        if text == None or len( text ) == 0:
            self.tokens = None
        else:
            self.tokens = text.split()

    def token(self):
        if self.tokens is None or self.index >= len( self.tokens ):
            return None
        return self.tokens[self.index]

    def next(self):
        if self.token() is None:
            return None
        self.index += 1
        return self.token()

    def token(self):
        return self.tokens[self.index]

    def tokenAsInt(self):
        try:
            return int( self.token() )
        except ValueError:
            return None

    def tokenAsBoolean(self):
        if self.token().lower() in ( "yes", "true", "1", "t" ):
            return True

        return False

class Port:

    def __init__(self, port = "/dev/serial/by-id/usb-Arduino__www.arduino.cc__0042_741333534373512161B1-if00", baudrate = 115200, timeout=0):
        self.port = serial.Serial(port=port, baudrate=baudrate, timeout=timeout)
        self.port.setDTR(level=False)
        sleep(2)
        self.port.flush()

    def readline(self):
        result = self.port.readline()
        if result == None or len(result) == 0:
            return None
        print "received command {}".format( result )
        return Command( result )

    def write(self, message):
        self.port.write( message )
