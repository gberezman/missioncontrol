from time import sleep
import pytest
from missionControl.rules import Abort
from missionControl.audio import Audio, StubbedAudio
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

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

