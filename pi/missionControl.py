import threading
from time import sleep
from missionControl.arduino import ArduinoSerial, ArduinoMatrixDriver
from missionControl.rules import Rules
from missionControl.audio import Audio
from missionControl.eventParser import EventParser

class Mission( threading.Thread ):

    def __init__(self, audio, serial):
        self.audio  = audio
        self.serial = serial

    def run(self):

        matrixDriver = ArduinoMatrixDriver( serial )

        rules = Rules( self.audio, matrixDriver )
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

if __name__ == '__main__':

    mainThread = Mission( Audio(), ArduinoSerial( timeout = .5 ) )
    mainThread.start()
