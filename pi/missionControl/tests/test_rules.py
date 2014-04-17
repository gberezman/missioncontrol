from time import sleep
import pytest
from missionControl.rules import EventRecord, Rules, LatchedLED
from missionControl.audio import Audio, StubbedAudio
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestEventRecord:

    def test_record_recordsHit(self):
        eventRecord = EventRecord()

        eventRecord.record()

        assert len( eventRecord.hits ) == 1

    def test_record_skips_ifNotOn(self):
        eventRecord = EventRecord()

        eventRecord.record( False )

        assert len( eventRecord.hits ) == 0

    def test_record_recordsLimitedHits(self):
        size = 5
        eventRecord = EventRecord( size )

        for c in range( 1, 2 * size ):
            eventRecord.record()

        assert len( eventRecord.hits ) == 5

    def test_hitsInTheLastNSeconds_returnsZeroIfAllExpired(self):
        eventRecord = EventRecord()
        eventRecord.record()
        sleep( .02 )

        assert eventRecord.hitsInTheLastNSeconds( .01 ) == 0

    def test_hitsInTheLastNSeconds_returnsCorrectCount(self):
        eventRecord = EventRecord()
        eventRecord.record()
        sleep( .05 )

        eventRecord.record()

        assert eventRecord.hitsInTheLastNSeconds( .04 ) == 1

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

class TestRules:

    def setup_method(self, method):
        self.audio = StubbedAudio()
        self.serial = StubbedArduinoSerial()
        self.rules = Rules( self.audio, ArduinoMatrixDriver( self.serial ) )

    def test_getBogusRule_returnsRule(self):
        rule = self.rules.getRule('Bogus')
        assert rule is not None

    def test_abortModePotentiometer_setsAbortMode(self):
        rule = self.rules.getRule( 'AbortMode' )
        rule( 10 )

        assert self.rules.abort.mode == 10

    def test_DockingProbeOn_setsDockingProbeLedOn(self):
        rule = self.rules.getRule( 'DockingProbe' )

        rule( True )
        
        assert self.serial.getLastWrite() == 'LED DockingProbe on\n'
        
    def test_DockingProbeOff_setsDockingProbeLedOff(self):
        rule = self.rules.getRule( 'DockingProbe' )

        rule( False )
        
        assert self.serial.getLastWrite() == 'LED DockingProbe off\n'
        
    def test_DockingProbeOn_playsDockingProbeExtend(self):
        rule = self.rules.getRule( 'DockingProbe' )

        rule( True )
        
        assert self.audio.lastFn == 'setPlayState'
