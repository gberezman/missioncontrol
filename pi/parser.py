from time import sleep
import serial

class Parser:

    def __init__(self, text):
        self.index = 0
        if text:
            self.tokens = text.split()
        else:
            self.tokens = None

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
