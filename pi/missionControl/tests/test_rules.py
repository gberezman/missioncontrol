from time import time, sleep
from missionControl.rules import CautionWarning, Abort, EventRecord, Rules, LatchedLED
from missionControl.audio import StubbedAudio
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestCautionWarning:
    def test_defaultState_isInactive(self):
        cw = CautionWarning(None, None)
        
        assert cw.state == 'inactive'

    def test_alertState_isActive(self):
        cw = CautionWarning( StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        
        assert cw.state == 'active'

    def test_alert_playsCaution(self):
        audio = StubbedAudio()
        cw = CautionWarning( audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        
        assert audio.lastFn == 'playCaution'

    def test_alert_enablesCautionLed(self):
        serial = StubbedArduinoSerial()
        cw = CautionWarning( StubbedAudio(), ArduinoMatrixDriver( serial ) )
    
        cw.alert()
        
        assert serial.getLastWrite() == 'LED caution on\n'

    def test_clearState_isInactive(self):
        cw = CautionWarning( StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        cw.clear()
        
        assert cw.state == 'inactive'

    def test_clear_stopsCaution(self):
        audio = StubbedAudio()
        cw = CautionWarning( audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        cw.clear()
        
        assert audio.lastFn == 'stopCaution'

    def test_clear_disablesCautionLed(self):
        serial = StubbedArduinoSerial()
        cw = CautionWarning( StubbedAudio(), ArduinoMatrixDriver( serial ) )
    
        cw.alert()
        cw.clear()
        
        assert serial.getLastWrite() == 'LED caution off\n'

class TestAbort:
        
    def test_defaultMode_isOne(self):
        abort = Abort( StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
        
        assert abort.mode == 1

    def test_defaultArm_isFalse(self):
        abort = Abort( StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
        
        assert abort.armed == False

    def test_arm_EnablesAbortLed(self):
        serial = StubbedArduinoSerial()
        abort = Abort( StubbedAudio(), ArduinoMatrixDriver( serial ) )

        abort.arm()

        assert serial.getLastWrite() == 'LED Abort on\n'

    def test_disarm_DisablesAbortLed(self):
        serial = StubbedArduinoSerial()
        abort = Abort( StubbedAudio(), ArduinoMatrixDriver( serial ) )
        abort.arm()

        abort.disarm()

        assert serial.getLastWrite() == 'LED Abort off\n'

    def test_abort_playsAudio_ifArmed(self):
        audio = StubbedAudio()
        abort = Abort( audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
        abort.arm() 

        abort.abort() 

        assert audio.lastFn == 'play'

    def test_abort_doesNotPlayAudio_ifNotArmed(self):
        audio = StubbedAudio()
        abort = Abort( audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
      
        abort.abort() 

        assert audio.lastFn == None

    def test_abort_doesNotPlayAudio_ifExplicitlyToldNotToAbort(self):
        audio = StubbedAudio()
        abort = Abort( audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
      
        abort.abort( False ) 

        assert audio.lastFn == None

    def test_armed_setExplicitlyOff_disarms(self):
        serial = StubbedArduinoSerial()
        abort = Abort( StubbedAudio(), ArduinoMatrixDriver( serial ) )
        abort.arm()

        abort.arm(isOn = False)

        assert serial.getLastWrite() == 'LED Abort off\n'


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

    def test_getBogusRule_returnsRule(self):
        rules = Rules( StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
        
        rule = rules.getRule('Bogus')
        
        assert rule is not None
