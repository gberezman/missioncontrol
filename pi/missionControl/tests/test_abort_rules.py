import pytest
from missionControl.rules import Abort

class TestAbort:
    @pytest.fixture
    def audio(self, request):
        from missionControl.audio import Audio
        audio = Audio()

        def fin():
            audio.stopAll()
        request.addfinalizer(fin)
            
        return audio

    @pytest.fixture
    def serial(self):
        from missionControl.arduino import StubbedArduinoSerial
        return StubbedArduinoSerial()

    @pytest.fixture
    def abort(self, audio, serial):
        from missionControl.arduino import ArduinoMatrixDriver
        return Abort( audio, ArduinoMatrixDriver( serial ) ) 
        
    def test_defaultMode_isOne(self, abort):
        assert abort.mode == 1

    def test_defaultArm_isFalse(self, abort):
        assert abort.armed == False

    def test_arm_EnablesAbortLed(self, serial, abort):
        abort.setArm()

        assert serial.getLastWrite() == 'LED Abort on\n'

    def test_disarm_DisablesAbortLed(self, serial, abort):
        abort.setArm()

        abort.setArm( armed = False )

        assert serial.getLastWrite() == 'LED Abort off\n'

    def test_abort_playsAudio_ifArmed(self, audio, abort):
        abort.setArm() 

        abort.abort() 

        assert audio.isPlaying( 'abortPad' )

    def test_armed_setExplicitlyOff_disarms(self, serial, abort):
        abort.setArm()

        abort.setArm( armed  = False )

        assert serial.getLastWrite() == 'LED Abort off\n'

