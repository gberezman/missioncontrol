from time import sleep,time
from audio import Audio

class Meter:
   
    def __init__(self, port):
        self.port = port

    def setMeter(self, meterId, meterValue):
        self.port.write( "Meter {} {}\n".format( meterId, meterValue ) )

class LEDDriver:

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

    def setMode(self, mode):
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

class EventRecord:

    def __init__(self, size = 10):
        self.size = size
        hits = []

    def record(self):
        hits.insert(0, int(time())
        del hits[size:]

    def hitsInTheLastNSeconds(self, seconds):
        now = int(time())
        checkTime = now - seconds
        return sum(logTime > checkTime for logTime in hits)

class LatchedLED:

    def __init__(self, ledDriver, led):
        self.ledDriver = ledDriver
        self.led = led
        self.buttonCount = 0

    def on(self, button):
        self.buttonCount += 1
        if self.buttonCount > 0:
            self.ledDriver.on(led)

    def off(self, button):
        self.buttonCount -= 1
        if self.buttonCount <= 0:
            self.ledDriver.off(led)

class Rules:
   
    def noAction(self, *args):
        pass

    def applyTemporalRules(self):
        if self.SPSPresses.hitsInTheLastNSeconds(2) > 5:
            self.ledDriver.on('SPSPress')
        else:
            self.ledDriver.off('SPSPress')

        if self.SPSPresses.hitsInTheLastNSeconds(4) > 5:
            self.ledDriver.on('SPSFlngTempHi')
        else:
            self.ledDriver.off('SPSPress')

    def getPotRule(self, pot):
        return self.__potRules.get(pot, lambda potValue: self.noAction())

    def getSwitchOnRule(self, switch):
        rules = self.__switchRule.get(switch, {})
        return rules.get('on', lambda : self.noAction())

    def getSwitchOffRule(self, switch):
        rules = self.__switchRule.get(switch, {})
        return rules.get('off', lambda : self.noAction())

    def __init__(self, audio, port):
        self.audio = audio
        self.port = port
        self.ledDriver = LEDDriver(port)
        self.abort = Abort(audio, self.ledDriver)
        self.thrustStatus = LatchedLED(self.ledDriver, 'Thrust')
        self.SPSPresses = EventRecord()

        self.__potRules = {
            # CAPCOM
            # 'Speaker'    # Adjust speaker volume
            # 'Headset'    # Adjust headset volume
            # Consideration: How do I manage these separately. I definitely need a switch or switch recognition

            # ABORT
            'AbortMode'  : lambda potValue: self.abort.setMode(potValue),

            # EECOM
            # 'Voltage'
            # 'Current'
            # 'Resistance'
            # 'O2Flow'
            # In Arduino, tie the 4 pots directly to their LED graphs

            # INCO
            # 'AntPitch'
            # 'AntYaw'
            # 'Tune'
            # 'Beam'
            # In Arduino, tie the 4 pots directly to the LED graph:
                # Tune moves the focal section up and down the graph (i.e. moves the beam)
                # Beam adjusts the width of the focal section
                # AntPitch changes the focus of the green section (yellow, red the further you move away from focus)
                # AntYaw changes the the width of the green section
        }

        self.__switchRules = {
            # CONTROL
            # Replace with three way switch:
            'DockingProbeRetract' : { 'on'  : lambda : self.audio.play('dockingProbeRetract')
                                                       or self.ledDriver.on('DockingProbe'),
                                      'off' : lambda : self.audio.stop('dockingProbeRetract')
                                                       or self.ledDriver.off('DockingProbe') },

            'DockingProbeExtend'  : { 'on'  : lambda : self.audio.play('dockingProbeExtend')
                                                       or self.ledDriver.on('DockingProbe'),
                                      'off' : lambda : self.audio.stop('dockingProbeExtend')
                                                       or self.ledDriver.off('DockingProbe') },

            'GlycolPump'          : { 'on'  : lambda : self.audio.playContinuous('glycolPump')
                                                       or self.ledDriver.on('GlycolPump'),
                                      'off' : lambda : self.audio.stop('glycolPump')
                                                       or self.ledDriver.off('GlycolPump') },

            'SCEPower'            : { 'on'  : lambda : self.ledDriver.on('SCEPower'),
                                      'off' : lambda : self.ledDriver.off('SCEPower') },

            'WasteDump'           : { 'on'  : lambda : self.audio.play('waste')
                                                       or self.ledDriver.on('WasteDump') },

            'CabinFan'            : { 'on'  : lambda : self.audio.playContinuous('fan')
                                                       or self.ledDriver.on('CabinFan'),
                                      'off' : lambda : self.audio.stop('fan')
                                                       or self.ledDriver.off('CabinFan') },

            'H2OFlow'             : { 'on'  : lambda : self.audio.playContinuous('H2OFlow')
                                                       or self.ledDriver.on('H2OFlow'),
                                      'off' : lambda : self.audio.stop('H2OFlow')
                                                       or self.ledDriver.off('H2OFlow') },

            'IntLights'           : { 'on'  : lambda : self.ledDriver.on('IntLights'),
                                      'off' : lambda : self.ledDriver.off('IntLights') },

            'SuitComp'            : { 'on'  : lambda : self.ledDriver.on('SuitComp'),
                                      'off' : lambda : self.ledDriver.off('SuitComp') },

            # ABORT
            'ArmAbort'            : { 'on'  : lambda : self.abort.arm(),
                                      'off' : lambda : self.abort.disarm() },

            'Abort'               : { 'on'  : lambda : self.abort() },

            # BOOSTER
            # Service propulsion system
            'SPS'                 : { 'on'  : lambda : self.audio.play('spsThruster')
                                                       or self.thrustStatus.on('SPS')
                                                       or self.SPSPresses.record(),
                                      'off' : lambda : self.audio.stop('spsThruster')
                                                       or self.thrustStatus.off('SPS') }

            # Trans-Earth injection (from parking orbit around moon, sets on burn towards Earth)
            'TEI'                 : { 'on'  : lambda : self.audio.playContinuous('teiThruster')
                                                       or self.thrustStatus.on('TEI'),
                                      'off' : lambda : self.audio.stop('teiThruster')
                                                       or self.thrustStatus.off('TEI') },

            # Trans-Lunar injection (puts on path towards moon)
            'TLI'                 : { 'on'  : lambda : self.audio.playContinuous('tliThruster')
                                                       or self.thrustStatus.on('TLI'),
                                      'off' : lambda : self.audio.stop('tliThruster')
                                                       or self.thrustStatus.off('TLI') },

            
            # Saturn, first stage
            'S-IC'                : { 'on'  : lambda : self.audio.playContinuous('sicThruster')
                                                       or self.thrustStatus.on('S-IC'),
                                      'off' : lambda : self.audio.stop('sicThruster')
                                                       or self.thrustStatus.off('S-IC') },

            # Saturn, second stage
            'S-II'                : { 'on'  : lambda : self.audio.playContinuous('siiThruster')
                                                       or self.thrustStatus.on('S-II'),
                                      'off' : lambda : self.audio.stop('siiThruster')
                                                       or self.thrustStatus.off('S-II') },

            # Saturn V, third stage
            'S-iVB'               : { 'on'  : lambda : self.audio.playContinuous('sivbThruster')
                                                       or self.thrustStatus.on('S-iVB'),
                                      'off' : lambda : self.audio.stop('sivbThruster')
                                                       or self.thrustStatus.off('S-iVB') },

            'M-I'                 : { 'on'  : lambda : self.audio.playContinuous('miThruster')
                                                       or self.thrustStatus.on('M-I'),
                                      'off' : lambda : self.audio.stop('miThruster')
                                                       or self.thrustStatus.off('M-I') },

            'M-II'                : { 'on'  : lambda : self.audio.playContinuous('miiThruster')
                                                       or self.thrustStatus.on('M-II'),
                                      'off' : lambda : self.audio.stop('miiThruster')
                                                       or self.thrustStatus.off('M-II') },

            'M-III'               : { 'on'  : lambda : self.audio.playContinuous('miiiThruster')
                                                       or self.thrustStatus.on('M-III'),
                                      'off' : lambda : self.audio.stop('miiiThruster')
                                                       or self.thrustStatus.off('M-III') },

            # C&WS
            # square wave alternating between 750 and 2000cps changing 2.5 times per second
            # 'Caution' # lights up when C&WS fires
                # pressing clears tone, but leaves lights on
            # 'Power'  # Resets the C&WS system
            # 'Mode' # what systems to be monitored (CM deactivates the SM monitors)
            # 'Lamp' # Wire Lamp to light all LED's directly
            # 'Ack' # no lights, audio and master alarm only, probably should be illuminated

            # CAPCOM
            'PTT'                 : { 'on'  : lambda : self.audio.play('quindarin'),
                                      'off' : lambda : self.audio.play('quindarout') },

            # EVENT SEQUENCE
            'ES1'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES1 ) 
                                                       or self.ledDriver.on( 'ES1' ) },
            'ES2'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES2 )
                                                       or self.ledDriver.on( 'ES2' ) },
            'ES3'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES3 )
                                                       or self.ledDriver.on( 'ES3' ) },
            'ES4'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES4 )
                                                       or self.ledDriver.on( 'ES4' ) },
            'ES5'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES5 )
                                                       or self.ledDriver.on( 'ES5' ) },
            'ES6'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES6 )
                                                       or self.ledDriver.on( 'ES6' ) },
            'ES7'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES7 )
                                                       or self.ledDriver.on( 'ES7' ) },
            'ES8'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES8 )
                                                       or self.ledDriver.on( 'ES8' ) },
            'ES9'                 : { 'on'  : lambda : self.audio.playES( self.audio.ES9 )
                                                       or self.ledDriver.on( 'ES9' ) },
            'ES10'                : { 'on'  : lambda : self.audio.playES( self.audio.ES10 )
                                                       or self.ledDriver.on( 'ES10' ) },

            # CRYOGENICS

            'O2Fan'               : { 'on'  : lambda : self.audio.playContinuous('o2fan'),
                                      'off' : lambda : self.audio.stop('o2fan') },

            'H2Fan'               : { 'on'  : lambda : self.audio.playContinuous('h2fan'),
                                      'off' : lambda : self.audio.stop('h2fan') },

            'Pumps'               : { 'on'  : lambda : self.audio.playContinuous('pumps'),
                                      'off' : lambda : self.audio.stop('pumps') },

            'Heat'                : { 'on'  : lambda : self.audio.playContinuous('heat'),
                                      'off' : lambda : self.audio.stop('heat') },

            # PYROTECHNICS
            'DrogueDeploy'        : { 'on'  : lambda : self.audio.play('DrogueDeploy')
                                                       or self.ledDriver.on('DrogueChute') },

            # manually deploy the CM main parachutes.
            'MainDeploy'          : { 'on'  : lambda : self.audio.play('mainDeploy')
                                                       or self.ledDriver.on('MainChute') },

            # Manually separate the CSM from the launch vehicle during an abort or in normal operation.
            'CSM/LVDeploy'        : { 'on'  : lambda : self.audio.play('CSM/LVDeploy') },

            # Separate for reentry
            'SM/CMDeploy'         : { 'on'  : lambda : self.audio.play('SM/CMDeploy') },

            # Deploy the Launch Escape System Canard Parachutes
            'CanardDeploy'        : { 'on'  : lambda : self.audio.play('CanardDeploy') },

            # Push-switch to jettison CM apex cover if automatic system fails during an abort or earth landing after a normal mission. 
            'ApexCoverJettsn'     : { 'on'  : lambda : self.audio.play('ApexCoverJettsn')
                                                       or self.ledDriver.on('Hatch') },

            # Manually operates the Launch Escape System, either to jettison the LES tower or to fire the motor in the event of an LES abort.  In the former case, the explosive bolts connecting the LES tower to the CSM must fire first.
            'LesMotorFire'        : { 'on'  : lambda : self.audio.play('LesMotorFire') },
        }

# Overuse of SPS engine:
    # SPSPress  # SPS engine pressure
    # SPSFlngTempHi # lights when sps flange temperature is too high

# Major overuse of SPS, shuts down engine
    # SPSRoughEco # lights when fcsm senses rough combustion and terminates thrust

# All engine overuse
    # BMag1Temp # Body mounted attitude gyro temperature out of range (detects spacecraft rate)
    # BMag2Temp # Body mounted attitude gyro temperature out of range

# M-I to M-III engines (like Thrust):
    # Ullage # small engines prior to big fire for fine control

# Overuse of M-I to M-III
    # PitchGimbl1 # overcurrent conditions based on time/pressure
    # PitchGimbl2
    # yawGimbl1
    # yawGimbl2
    # CMRCS1 # Reaction Control System pressure out of range - only when CM/CSM is in CM position
    # CMRCS2 # RCS pressure out of range - only when CM/CSM is in CM position
    # SMRCSA # Service Module RCS
    # SMRCSB
    # SMRCSC
    # SMRCSD

# Massive overuse of M-I to M-III
    # GimbalLock # bad, no orientation in space (flash to warn)

# Voltage too low for too long
    # ACBus1 # Power bus voltage low
    # ACBus2 # Power bus voltage low

# Current too high for too long
    # ACBus1Overload # too much current over timer period
    # ACBus2Overload # too much current over timer period
    # FCBusDiscnnct # Forward current hi, reverse current low

# O2 flow too high (or leak...)
    # O2FlowHi # too much O2 flow 

# O2 flow to low for too long
    # CO2PPHi # CO2 pressure too hi

# H2 / O2 too high or too low for too long
    # CryoPress # H2 or O2 pressure out of rnage

# Random, fix by switching on suit comp
    # SuitComp # suit compressor pressure low

# Signal out of band for too long:
    # HGAntScanLimit # high gain antenna scan limit problems

# DockingTarget
# CrewAlert # activated by ground crew; cleared by ground crew
# CW # Alarm tone inoperative
# UplinkActivity # data transmission to ship
# GlycolTempLow # glycol (water) temp low

