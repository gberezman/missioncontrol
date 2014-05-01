import pytest
from missionControl.rules import LatchedLED
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestLatchedLED:

    @pytest.fixture
    def serial(self):
        return StubbedArduinoSerial()

    @pytest.fixture
    def latch(self, serial):
        return LatchedLED( ArduinoMatrixDriver( serial ), 'Button' )

    def test_on_incrementsButtonCount(self, latch):
        latch.on()

        assert latch.buttonCount == 1

    def test_on_decrementsButtonCount_ifNotOn(self, latch):
        latch.on()

        latch.on( False )

        assert latch.buttonCount == 0

    def test_off_decrementsButtonCount(self, latch):
        latch.on()
        latch.off()

        assert latch.buttonCount == 0

    def test_off_doesNotdecrementBelowZero(self, latch):
        latch.off()
        latch.off()

        assert latch.buttonCount == 0

    def test_on_enablesLed(self, serial, latch):
        latch.on()

        serial.getLastWrite() == 'LED Button on\n'

    def test_on_disablesLed(self, serial, latch):
        latch.on()
        latch.off()

        serial.getLastWrite() == 'LED Button off\n'
