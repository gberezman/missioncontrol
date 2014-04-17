import pytest
from missionControl.rules import LatchedLED
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestLatchedLED:

    def test_on_incrementsButtonCount(self):
        latch = LatchedLED( ArduinoMatrixDriver( StubbedArduinoSerial() ), 'Button' )

        latch.on()

        assert latch.buttonCount == 1

    def test_on_decrementsButtonCount_ifNotOn(self):
        latch = LatchedLED( ArduinoMatrixDriver( StubbedArduinoSerial() ), 'Button' )

        latch.on()
        latch.on( False )

        assert latch.buttonCount == 0

    def test_off_decrementsButtonCount(self):
        latch = LatchedLED( ArduinoMatrixDriver( StubbedArduinoSerial() ), 'Button' )

        latch.on()
        latch.off()

        assert latch.buttonCount == 0

    def test_off_doesNotdecrementBelowZero(self):
        latch = LatchedLED( ArduinoMatrixDriver( StubbedArduinoSerial() ), 'Button' )

        latch.off()
        latch.off()

        assert latch.buttonCount == 0

    def test_on_enablesLed(self):
        serial = StubbedArduinoSerial()
        latch = LatchedLED( ArduinoMatrixDriver( serial ), 'Button' )

        latch.on()

        serial.getLastWrite() == 'LED Button on\n'

    def test_on_disablesLed(self):
        serial = StubbedArduinoSerial()
        latch = LatchedLED( ArduinoMatrixDriver( serial ), 'Button' )

        latch.on()
        latch.off()

        serial.getLastWrite() == 'LED Button off\n'
