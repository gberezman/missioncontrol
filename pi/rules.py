from time import sleep
from audio import Audio

class Meter:
   
    def __init__(self, port):
        self.port = port

    def setMeter(self, meterId, meterValue):
        self.port.write( "Meter {} {}\n".format( meterId, meterValue ) )

class LED:

    def __init__(self, port):
        self.port = port

    def on(self, ledId):
        self.port.write( "LED {} on\n".format( ledId ) )
        
    def off(self, ledId):
        self.port.write( "LED {} off\n".format( ledId ) )

class Abort:

    def __init__(self, audio, led):
        self.audio = audio
        self.led = led

        self.armed = False
        self.mode = 1

    def arm(self):
        self.armed = True
        self.led.on( 'ArmAbort' )
        self.led.on( 'Abort' ),

    def disarm(self):
        self.armed = False
        self.led.off( 'ArmAbort' )
        self.led.off( 'Abort' ),

    def setAbortMode(self, mode):
        self.mode = mode

    def abort(self):
        if self.armed:
            if self.mode == 1:
                self.audio.abortPad.play()
            elif self.mode == 2:
                self.audio.abortI.play()
            elif self.mode == 3:
                self.audio.abortII.play()
            elif self.mode == 4:
                self.audio.abortIII.play()
            elif self.mode == 5:
                self.audio.abortSIVB.play()
            elif self.mode == 6:
                self.audio.abortSomething.play()

            # shutdown sequence "sudo halt"

class ThrustStatus:

    def __init__(self, led):
        self.led = led
        self.buttonCount = 0

    def on(self):
        self.buttonCount += 1
        if self.buttonCount > 0:
            self.led.on('Thrust')

    def off(self):
        self.buttonCount -= 1
        if self.buttonCount <= 0:
            self.led.off('Thrust')

class Rules:
   
    def noAction(self, *args):
        pass

    def checkTimers(self):
        pass

    def __init__(self, audio, port):
        self.audio = audio
        self.port = port
        self.led = LED(port)
        self.abort = Abort(audio, self.led)
        self.thrustStatus  = ThrustStatus(self.led)

        self.potReadings = {}

        self.potRule = {
            # CAPCOM
            'Speaker'    : lambda potValue: self.noAction, # Adjust speaker volume
            'Headset'    : lambda potValue: self.noAction, # Adjust headset volume
            # Consideration: How do I manage these separately. I definitely need a switch or switch recognition

            # ABORT
            'AbortMode'  : lambda potValue: self.abort.setAbortMode(potValue),

            # EECOM
            'Voltage'    : lambda potValue: self.potReadings.update({'Voltage': potValue}),
            'Current'    : lambda potValue: self.potReadings.update({'Current': potValue}),
            'Resistance' : lambda potValue: self.potReadings.update({'Resistance': potValue}),
            'O2Flow'     : lambda potValue: self.potReadings.update({'O2Flow': potValue}),
            # In Arduino, tie the 4 pots directly to their LED graphs

            # INCO
            'AntPitch'   : lambda potValue: self.potReadings.update({'AntPitch': potValue}),
            'AntYaw'     : lambda potValue: self.potReadings.update({'AntYaw': potValue}),
            'Tune'       : lambda potValue: self.potReadings.update({'Tune': potValue}),
            'Beam'       : lambda potValue: self.potReadings.update({'Beam': potValue}),
            # In Arduino, tie the 4 pots directly to the LED graph:
                # Tune moves the focal section up and down the graph (i.e. moves the beam)
                # Beam adjusts the width of the focal section
                # AntPitch changes the focus of the green section (yellow, red the further you move away from focus)
                # AntYaw changes the the width of the green section
        }

        self.switchRules = {
            # CONTROL
            # Replace with three way switch:
            'DockingProbeRetract' : { 'on'  : lambda : self.audio.dockingProbeRetract.play() 
                                                       or self.led.on('DockingProbe'),
                                      'off' : lambda : self.audio.dockingProbeRetract.stop() 
                                                       or self.led.off('DockingProbe') },

            'DockingProbeExtend'  : { 'on'  : lambda : self.audio.dockingProbeExtend.play() 
                                                       or self.led.on('DockingProbe'),
                                      'off' : lambda : self.audio.dockingProbeExtend.stop() 
                                                       or self.led.off('DockingProbe') },

            'GlycolPump'          : { 'on'  : lambda : self.audio.glycolPump.play(loops = -1) 
                                                       or self.led.on('GlycolPump'),
                                      'off' : lambda : self.audio.glycolPump.stop() 
                                                       or self.led.off('GlycolPump') },

            'SCEPower'            : { 'on'  : lambda : self.led.on('SCEPower'),
                                      'off' : lambda : self.led.off('SCEPower') },

            'WasteDump'           : { 'on'  : lambda : self.audio.waste.play() 
                                                       or self.led.on('WasteDump') },

            'CabinFan'            : { 'on'  : lambda : self.audio.fan.play(loops = -1) 
                                                       or self.led.on('CabinFan'),
                                      'off' : lambda : self.audio.fan.stop() 
                                                       or self.led.off('CabinFan') },

            'H2OFlow'             : { 'on'  : lambda : self.audio.H2OFlow.play(loops = -1) 
                                                       or self.led.on('H2OFlow'),
                                      'off' : lambda : self.audio.H2OFlow.stop() 
                                                       or self.led.off('H2OFlow') },

            'IntLights'           : { 'on'  : lambda : self.led.on('IntLights'),
                                      'off' : lambda : self.led.off('IntLights') },

            'SuitComp'            : { 'on'  : lambda : self.led.on('SuitComp'),
                                      'off' : lambda : self.led.off('SuitComp') },

            # ABORT
            'ArmAbort'            : { 'on'  : lambda : self.abort.arm(),
                                      'off' : lambda : self.abort.disarm() },

            'Abort'               : { 'on'  : lambda : self.abort() },

            # BOOSTER
            'SPS'                 : { 'on'  : lambda : self.audio.spsThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.spsThruster.stop() 
                                                       or self.thrustStatus.off() },

            'TEI'                 : { 'on'  : lambda : self.audio.teiThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.teiThruster.stop() 
                                                       or self.thrustStatus.off() },

            'TLI'                 : { 'on'  : lambda : self.audio.tliThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.tliThruster.stop() 
                                                       or self.thrustStatus.off() },

            'S-IC'                : { 'on'  : lambda : self.audio.sicThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.sicThruster.stop() 
                                                       or self.thrustStatus.off() },

            'S-II'                : { 'on'  : lambda : self.audio.siiThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.siiThruster.stop() 
                                                       or self.thrustStatus.off() },

            'S-iVB'               : { 'on'  : lambda : self.audio.sivbThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.sivbThruster.stop() 
                                                       or self.thrustStatus.off() },

            'M-I'                 : { 'on'  : lambda : self.audio.miThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.miThruster.stop() 
                                                       or self.thrustStatus.off() },

            'M-II'                : { 'on'  : lambda : self.audio.miiThruster.play(loops = -1) 
                                                       or self.thrustStatus.on(),
                                      'off' : lambda : self.audio.miiiThruster.stop() 
                                                       or self.thrustStatus.off() },

            # C&WS
            # 'Caution'
            # 'Power' 
            # 'Mode'
            # 'Lamp' # Wire Lamp to light all LED's directly
            # 'Ack'

            # CAPCOM
            'PTT'                 : { 'on'  : lambda : self.audio.quindarin.play(),
                                      'off' : lambda : self.audio.quindarout.play() },

            # EVENT SEQUENCE
            'ES1'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES1 ) },
            'ES2'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES2 ) },
            'ES3'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES3 ) },
            'ES4'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES4 ) },
            'ES5'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES5 ) },
            'ES6'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES6 ) },
            'ES7'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES7 ) },
            'ES8'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES8 ) },
            'ES9'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES9 ) },
            'ES10'                : { 'on'  : lambda : self.audio.playES( self.audio.ES10 ) },

            # CRYOGENICS

            'O2Fan'               : { 'on'  : lambda : self.audio.o2fan.play(loops = -1),
                                      'off' : lambda : self.audio.o2fan.stop() },

            'H2Fan'               : { 'on'  : lambda : self.audio.h2fan.play(loops = -1),
                                      'off' : lambda : self.audio.h2fan.stop() },

            'Pumps'               : { 'on'  : lambda : self.audio.pumps.play(loops = -1),
                                      'off' : lambda : self.audio.pumps.stop() },

            'Heat'                : { 'on'  : lambda : self.audio.heat.play(loops = -1),
                                      'off' : lambda : self.audio.heat.stop() },

            # PYROTECHNICS
            'CSM/LVDeploy'        : { 'on'  : lambda : self.audio.csmDeploy.play() },
            # 'MainDeploy'
            # 'SM/CMDeploy'
            # 'CanardDeploy'
            # 'ApexCoverJettsn'
            # 'LesMotorFire'
        }

class StubbedPort:

    def write(self, arg):
        self.lastMessage = arg

if __name__ == '__main__':

    port = StubbedPort()
    rules = Rules(Audio(), port)

    res = rules.switchRules['DockingProbeRetract']['on']()
    assert port.lastMessage == 'LED DockingProbe on\n'

    res = rules.switchRules['DockingProbeRetract']['off']()
    assert port.lastMessage == 'LED DockingProbe off\n'
