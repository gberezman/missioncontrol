from eventParser import EventParser

class TestCommandFactory:

    def test_getEventTuple_returnsNoneAndFalse_withNoneInput(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( None )

        assert id is None
        assert value is None

    def test_getEventTuple_returnsNoId_withNoSwitchEventData(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'S' )

        assert id is None
        
    def test_getEventTuple_returnsFalseValue_withNoSwitchEventData(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'S' )

        assert value == False
        
    def test_getEventTuple_returnsEventId_withSwitchEvent(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'S event True' )

        assert id == 'event'

    def test_getEventTuple_returnsTrueValue_withSwitchOnEvent(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'S event True' )

        assert value == True

    def test_getEventTuple_returnsFalseValue_withSwitchOffEvent(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'S event False' )

        assert value == False

    def test_getEventTuple_returnsName_withNonSwitchEvent(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'P event 1' )

        assert id == 'event'

    def test_getEventTuple_returnsInt_withNonSwitchEvent(self):
        parser = EventParser()
        (id, value) = parser.getEventTuple( 'P event 7' )

        assert value == 7
 
