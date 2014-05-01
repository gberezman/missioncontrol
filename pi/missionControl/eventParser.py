from time import sleep
from parser import Parser
import serial

class EventParser:
    def getEventTuple(self, data):
        parser = Parser( data )

        eventType  = parser.token() 
        eventId    = parser.next()
        eventValue = parser.next()

        if eventType == 'S':
            eventValue = self.__toBoolean( eventValue )
        elif eventType == 'P':
            eventValue = self.__toInt( eventValue )

        return eventId, eventValue

    def __toBoolean(self, value):
        try:
            return value.lower() in ( "yes", "true", "1", "t", "on", 1 )
        except AttributeError:
            return False

    def __toInt(self, value):
            try:
                return int( value )
            except TypeError:
                return None

