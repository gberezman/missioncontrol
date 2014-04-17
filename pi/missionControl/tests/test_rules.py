from time import sleep
import pytest
from missionControl.rules import Rules
from missionControl.audio import StubbedAudio
from missionControl.arduino import StubbedArduinoSerial, ArduinoMatrixDriver

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
