from missionControl.rules import CautionWarning, Abort, EventRecord, Rules
from missionControl.audio import StubbedAudio
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestCautionWarning:
    def test_defaultState_isInactive(self):
        cw = CautionWarning(None, None)
        
        assert cw.state == 'inactive'

    def test_alertState_isActive(self):
        cw = CautionWarning(StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        
        assert cw.state == 'active'

    def test_alert_playsCaution(self):
        audio = StubbedAudio()
        cw = CautionWarning(audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        
        assert audio.lastFn == 'playCaution'

    def test_alert_enablesCautionLed(self):
        serial = StubbedArduinoSerial()
        cw = CautionWarning(StubbedAudio(), ArduinoMatrixDriver( serial ) )
    
        cw.alert()
        
        assert serial.getLastWrite() == 'LED caution on\n'

    def test_clearState_isInactive(self):
        cw = CautionWarning(StubbedAudio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        cw.clear()
        
        assert cw.state == 'inactive'

    def test_clear_stopsCaution(self):
        audio = StubbedAudio()
        cw = CautionWarning(audio, ArduinoMatrixDriver( StubbedArduinoSerial() ) )
    
        cw.alert()
        cw.clear()
        
        assert audio.lastFn == 'stopCaution'

    def test_clear_disablesCautionLed(self):
        serial = StubbedArduinoSerial()
        cw = CautionWarning(StubbedAudio(), ArduinoMatrixDriver( serial ) )
    
        cw.alert()
        cw.clear()
        
        assert serial.getLastWrite() == 'LED caution off\n'

class TestAbort:
    pass

class TestEventRecord:
    pass

class TestLatchedLED:
    pass

class TestRules:
    pass
