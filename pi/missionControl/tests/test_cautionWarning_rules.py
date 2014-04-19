import pytest
from missionControl.rules import CautionWarning
from missionControl.audio import Audio
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

class TestCautionWarning:

    @pytest.fixture
    def audio(self, request):
        audio = Audio()

        def fin():
            audio.stopAll()
        request.addfinalizer(fin)
            
        return audio

    @pytest.fixture
    def serial(self):
        return StubbedArduinoSerial()

    @pytest.fixture
    def cautionWarning(self, audio, serial):
        return CautionWarning( audio, ArduinoMatrixDriver( serial ) ) 

    def test_defaultState_isInactive(self, cautionWarning):
        assert cautionWarning.state == 'inactive'

    def test_alertState_isActive(self, cautionWarning):
        cautionWarning.alert()
        
        assert cautionWarning.state == 'active'

    def test_alert_playsCaution(self, audio, cautionWarning):
        cautionWarning.alert()
        
        assert audio.isPlaying( 'caution' ) == True

    def test_alert_enablesCautionLed(self, serial, cautionWarning):
        cautionWarning.alert()
        
        assert serial.getLastWrite() == 'LED caution on\n'

    def test_clearState_isInactive(self, cautionWarning):
        cautionWarning.alert()
        cautionWarning.clear()
        
        assert cautionWarning.state == 'inactive'

    def test_clear_stopsCautionAudio(self, audio, cautionWarning):
        cautionWarning.alert()
        cautionWarning.clear()

        assert audio.isPlaying( 'caution' ) == False

    def test_clear_disablesCautionLed(self, serial, cautionWarning):
        cautionWarning.alert()
        cautionWarning.clear()
        
        assert serial.getLastWrite() == 'LED caution off\n'
