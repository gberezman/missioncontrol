import threading
from time import sleep
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver
from missionControl.rules import Rules
from missionControl.audio import Audio
from missionControl.eventParser import EventParser

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
