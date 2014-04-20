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

        assert audio.isPlaying( 'DockingProbeExtend' )

    def test_DockingProbeOff_playsDockingProbeRetract(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( True )
        rule( False )

        assert audio.isPlaying( 'DockingProbeRetract' )

    def test_DockingProbeOn_stopsDockingProbeRetract(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( False )
        rule( True )

        assert not audio.isPlaying( 'DockingProbeRetract' )

    def test_DockingProbeOff_playsDockingProbeExtend(self, audio, rules):
        rule = rules.getRule( 'DockingProbe' )

        rule( True )
        rule( False )

        assert not audio.isPlaying( 'DockingProbeExtend' )

    def test_GlycolPumpOn_setsGlycolPumpLedOn(self, serial, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )

        assert serial.hasSent( 'LED GlycolPump on\n' )

    def test_GlycolPumpOn_playsGlycolPump(self, audio, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )

        assert audio.isPlaying( 'GlycolPump' )

    def test_GlycolPumpOff_stopsGlycolPump(self, audio, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )
        rule( False )

        assert not audio.isPlaying( 'GlycolPump' )

    def test_GlycolPumpOn_setsGlycolPumpLedOn(self, serial, rules):
        rule = rules.getRule( 'GlycolPump' )

        rule( True )
        rule( False )

        assert serial.hasSent( 'LED GlycolPump off\n' )

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

        assert audio.isPlaying( 'WasteDump' )

    def test_WasteDumpOff_doesNotStopWasteDumpClip(self, audio, rules):
        rule = rules.getRule( 'WasteDump' )

        rule( True )
        rule( False )

        assert audio.isPlaying( 'WasteDump' )

    def test_CabinFanOn_setsCabinFanLedOn(self, serial, rules):
        rule = rules.getRule( 'CabinFan' )
        
        rule( True )

        assert serial.hasSent( 'LED CabinFan on\n' )

    def test_CabinFanOff_setsCabinFanLedOff(self, serial, rules):
        rule = rules.getRule( 'CabinFan' )
        
        rule( False )

        assert serial.hasSent( 'LED CabinFan off\n' )

    def test_CabinFanOn_playsCabinFan(self, audio, rules):
        rule = rules.getRule( 'CabinFan' )
        
        rule( True )

        assert audio.isPlaying( 'CabinFan' )

    def test_CabinFanOff_stopsCabinFan(self, audio, rules):
        rule = rules.getRule( 'CabinFan' )
        
        rule( True )
        rule( False )

        assert not audio.isPlaying( 'CabinFan' )

    def test_H2OFlowOn_setsH2OFlowLedOn(self, serial, rules):
        rule = rules.getRule( 'H2OFlow' )

        rule( True )

        assert serial.hasSent( 'LED H2OFlow on\n' )

    def test_H2OFlowOff_setsH2OFlowLedOff(self, serial, rules):
        rule = rules.getRule( 'H2OFlow' )

        rule( False )

        assert serial.hasSent( 'LED H2OFlow off\n' )

    def test_H2OFlowOn_playsH2OFlow(self, audio, rules):
        rule = rules.getRule( 'H2OFlow' )

        rule( True )

        assert audio.isPlaying( 'H2OFlow' )

    def test_H2OFlowOff_stopsH2OFlow(self, audio, rules):
        rule = rules.getRule( 'H2OFlow' )

        rule( True )
        rule( False )

        assert not audio.isPlaying( 'H2OFlow' )

    def test_IntLightsOn_setsntLightsLedOn(self, serial, rules):
        rule = rules.getRule( 'IntLights' )
        
        rule( True )

        assert serial.hasSent( 'LED IntLights on\n' )

    def test_IntLightsOn_setsntLightsLedOn(self, serial, rules):
        rule = rules.getRule( 'IntLights' )
        
        rule( False )

        assert serial.hasSent( 'LED IntLights off\n' )
