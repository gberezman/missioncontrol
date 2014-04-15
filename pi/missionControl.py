from arduino import StubbedArduinoSerial, ArduinoMatrixDriver
from time import sleep
from rules import Rules
from audio import Audio
from eventParser import EventParser
import threading

def eventLoop():

    #serial = ArduinoSerial( timeout = .5 )
    serial = StubbedArduinoSerial()
    matrixDriver = ArduinoMatrixDriver( serial )
    audio = Audio()

    rules = Rules( audio, matrixDriver )
    eventParser = EventParser()

    print "Starting event loop"

    while True:
        try:
            rules.applyTemporalRules()

            data = serial.read()
            (eventId, eventValue) = eventParser.getEventTuple( data )

            rule = rules.getRule( eventId )
            rule( eventValue )
            
        except KeyboardInterrupt:
            exit()

mainThread = threading.Thread( target = eventLoop )
mainThread.start()
