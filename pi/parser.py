from time import sleep
import serial

class Parser:

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
