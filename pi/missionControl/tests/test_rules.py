from time import sleep
import pytest

class TestRules:

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
    def rules(self, audio, serial):
        from missionControl.rules import Rules
        from missionControl.arduino import ArduinoMatrixDriver
        return Rules( audio, ArduinoMatrixDriver( serial ) )

    def test_getBogusRule_returnsRule(self, rules):
        rule = rules.getRule('Bogus')
        assert rule is not None

    def test_abortModePotentiometer_setsAbortMode(self, rules):
        rule = rules.getRule( 'AbortMode' )
        rule( 10 )

        assert rules.abort.mode == 10

    def test_DockingProbeOn_setsDockingProbeLedOn(self, serial, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( True )
        
        assert serial.hasSent( 'LED DockingProbe on\n' )
        
    def test_DockingProbeOff_setsDockingProbeLedOff(self, serial, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( False )
        
        assert serial.hasSent( 'LED DockingProbe off\n' )

    def test_DockingProbeOn_playsDockingProbeExtend(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( False )
        rule( True )

        assert audio.isPlaying( 'dockingProbeExtend' )

    def test_DockingProbeOff_playsDockingProbeRetract(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( True )
        rule( False )

        assert audio.isPlaying( 'dockingProbeRetract' )

    def test_DockingProbeOn_stopsDockingProbeRetract(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( False )
        rule( True )

        assert not audio.isPlaying( 'dockingProbeRetract' )

    def test_DockingProbeOff_playsDockingProbeExtend(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( True )
        rule( False )

        assert not audio.isPlaying( 'dockingProbeExtend' )

    def test_GlycolPumpOn_setsGlycolPumpLedOn(self, serial, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )

        assert serial.hasSent( 'LED glycolPump on\n' )

    def test_GlycolPumpOn_playsGlycolPump(self, audio, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )

        assert audio.isPlaying( 'glycolPump' )

    def test_GlycolPumpOff_stopsGlycolPump(self, audio, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )
        rule( False )

        assert not audio.isPlaying( 'glycolPump' )

    def test_GlycolPumpOn_setsGlycolPumpLedOn(self, serial, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )
        rule( False )

        assert serial.hasSent( 'LED glycolPump off\n' )

    def test_SCEPowerOn_setsSCEPowerLedOn(self, serial, rules):
        rule = rules.getRule( 'SCEPower' )

        rule( True )

        assert serial.hasSent( 'LED SCEPower on\n' )

    def test_SCEPowerOff_setsSCEPowerLedOff(self, serial, rules):
        rule = rules.getRule( 'SCEPower' )

        rule( False )

        assert serial.hasSent( 'LED SCEPower off\n' )

    def test_WasteDumpOn_setsWasteDumpLedOn(self, serial, rules):
        rule = rules.getRule( 'WasteDump' )

        rule( True )

        assert serial.hasSent( 'LED WasteDump on\n' )

    def test_WasteDumpOff_setsWasteDumpLedOff(self, serial, rules):
        rule = rules.getRule( 'WasteDump' )

        rule( False )

        assert serial.hasSent( 'LED WasteDump off\n' )

    def test_WasteDumpOn_playsWasteDumpClip(self, audio, rules):
        rule = rules.getRule( 'WasteDump' )

        rule( True )

        assert audio.isPlaying( 'wasteDump' )

    def test_WasteDumpOff_doesNotStopWasteDumpClip(self, audio, rules):
        rule = rules.getRule( 'WasteDump' )

        rule( True )
        rule( False )

        assert audio.isPlaying( 'wasteDump' )
