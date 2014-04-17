from time import sleep,time

class CautionWarning:

    def __init__(self, audio, matrixDriver):
        self.audio = audio
        self.matrixDriver = matrixDriver
        self.state = 'inactive'

    def alert(self):
        self.state = 'active'
        self.audio.playCaution()
        self.matrixDriver.ledOn( 'caution' )

    def clear(self):
        self.state = 'inactive'
        self.audio.stopCaution()
        self.matrixDriver.ledOff( 'caution' )

class Abort:

    def __init__(self, audio, matrixDriver):
        self.audio = audio
        self.matrixDriver = matrixDriver

        self.armed = False
        self.mode = 1

    def arm(self, isOn = True):
        if isOn:
            self.armed = True
            self.matrixDriver.ledOn( 'Abort' ),
        else:
            self.disarm()

    def disarm(self):
        self.armed = False
        self.matrixDriver.ledOff( 'Abort' ),

    def setMode(self, mode):
        self.mode = mode

    def abort(self, doAbort = True):
        if doAbort and self.armed:
            if self.mode == 1:
                self.audio.play( 'abortPad' )
            elif self.mode == 2:
                self.audio.play( 'abortI' )
            elif self.mode == 3:
                self.audio.play( 'abortII' )
            elif self.mode == 4:
                self.audio.play( 'abortIII' )
            elif self.mode == 5:
                self.audio.play( 'abortSIVB' )
            elif self.mode == 6:
                self.audio.play( 'somethingElse' )

            # shutdown sequence "sudo halt"

class EventRecord:

    def __init__(self, size = 10):
        self.size = size
        self.hits = []

    def record(self, isOn = True):
        if isOn:
            self.hits.insert( 0, time() )
            del self.hits[self.size:]

    def hitsInTheLastNSeconds(self, seconds):
        now = time()
        checkTime = now - seconds
        return sum( logTime > checkTime for logTime in self.hits )

class LatchedLED:

    def __init__(self, matrixDriver, led):
        self.matrixDriver = matrixDriver
        self.led = led
        self.buttonCount = 0

    def on(self, isOn = True):
        if isOn:
            self.buttonCount += 1
            if self.buttonCount > 0:
                self.matrixDriver.ledOn(self.led)
        else:
            self.off()
    
    def off(self):
        self.buttonCount = self.buttonCount - 1 if self.buttonCount > 0 else 0
        if self.buttonCount <= 0:
            self.matrixDriver.ledOff(self.led)

class Rules:
   
    def noAction(self, *args):
        sleep( 0.05 )

    def applyTemporalRules(self):
        if self.SPSPresses.hitsInTheLastNSeconds(2) > 5:
            self.matrixDriver.LedOn('SPSPress')
            self.cw.alert()
        else:
            self.matrixDriver.ledOff('SPSPress')

        if self.SPSPresses.hitsInTheLastNSeconds(4) > 5:
            self.matrixDriver.LedOn('SPSFlngTempHi')
            self.cw.alert()
        else:
            self.matrixDriver.ledOff('SPSPress')

    def getRule(self, name):
        return self.__rules.get(name, lambda value: self.noAction())

    def __init__(self, audio, matrixDriver):
        self.matrixDriver = matrixDriver
        self.audio = audio

        self.abort = Abort(audio, matrixDriver)
        self.thrustStatus = LatchedLED(matrixDriver, 'Thrust')
        self.SPSPresses = EventRecord()
        self.cw = CautionWarning(audio, matrixDriver)

        self.__rules = {
            # CAPCOM Potentiometers
            # 'Speaker'    # Adjust speaker volume
            # 'Headset'    # Adjust headset volume
            # Consideration: How do I manage these separately. I definitely need a switch or switch recognition

            # ABORT Potentiometers
            'AbortMode'  : lambda potValue: self.abort.setMode(potValue),

            # EECOM Potentiometers
            # 'Voltage'
            # 'Current'
            # 'Resistance'
            # 'O2Flow'
            # In Arduino, tie the 4 pots directly to their LED graphs

            # INCO Potentiometers
            # 'AntPitch'
            # 'AntYaw'
            # 'Tune'
            # 'Beam'
            # In Arduino, tie the 4 pots directly to the LED graph:
                # Tune moves the focal section up and down the graph (i.e. moves the beam)
                # Beam adjusts the width of the focal section
                # AntPitch changes the focus of the green section (yellow, red the further you move away from focus)
                # AntYaw changes the the width of the green section

            # CONTROL Switches
            'DockingProbe'    : lambda isOn: matrixDriver.setLed( 'DockingProbe', isOn ) \
                                             or audio.togglePlay( 'dockingProbeRetract', not isOn ) \
                                             or audio.togglePlay( 'dockingProbeExtend', isOn ),

            'GlycolPump'      : lambda isOn: matrixDriver.setLed( 'glycolPump', isOn ) \
                                             or audio.setContinuousPlayState( 'glycolPump', isOn ),

            'SCEPower'        : lambda isOn: matrixDriver.setLed('SCEPower', isOn ),

            'WasteDump'       : lambda isOn: matrixDriver.setLed( 'WasteDump', isOn ) \
                                             or ( audio.play('waste') if isOn else self.noAction() ),

            'CabinFan'        : lambda isOn: matrixDriver.setLed( 'CabinFan', isOn ) \
                                             or audio.setContinuousPlayState( 'fan', isOn ),

            'H2OFlow'         : lambda isOn: matrixDriver.setLed( 'H2OFlow' ) \
                                             or audio.setContinuousPlayState( 'H2OFlow', isOn ),

            'IntLights'       : lambda isOn: matrixDriver.setLed('IntLights', isOn ),

            'SuitComp'        : lambda isOn: matrixDriver.setLed('SuitComp', isOn ),

            # ABORT
            'ArmAbort'        : lambda isOn: self.abort.arm( isOn ),

            'Abort'           : lambda isOn: self.abort( isOn ),

            # BOOSTER Switches
            # Service propulsion system
            'SPS'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'spsThruster', isOn ) \
                                             or self.SPSPresses.record( isOn ),

            # Trans-Earth injection (from parking orbit around moon, sets on burn towards Earth)
            'TEI'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'teiThruster' ),

            # Trans-Lunar injection (puts on path towards moon)
            'TLI'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'tliThruster' ),
            
            # Saturn, first stage
            'S-IC'            : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'sicThruster' ),

            # Saturn, second stage
            'S-II'            : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'siiThruster' ),

            # Saturn V, third stage
            'S-iVB'           : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'sivbThruster' ),

            'M-I'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'miThruster' ),

            'M-II'            : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'miiThruster' ),

            'M-III'           : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.setContinuousPlayState( 'miiiThruster' ),

            # C&WS Switches
            # square wave alternating between 750 and 2000cps changing 2.5 times per second
            # 'Caution' # lights up when C&WS fires
                # pressing clears tone, but leaves lights on
            # 'Power'  # Resets the C&WS system
            # 'Mode' # what systems to be monitored (CM deactivates the SM monitors)
            # 'Lamp' # Wire Lamp to light all LED's directly
            # 'Ack' # no lights, audio and master alarm only, probably should be illuminated

            # CAPCOM Switches
            'PTT'             : lambda isOn: audio.togglePlay( 'quindarin', isOn ) \
                                             or audio.togglePlay( 'quindarout', not isOn ),

            # EVENT SEQUENCE Switches
            'ES1'             : lambda isOn: audio.playEventSequence( audio.ES1 ) or matrixDriver.LedOn( 'ES1' ) if isOn else self.noAction(),
            'ES2'             : lambda isOn: audio.playEventSequence( audio.ES2 ) or matrixDriver.LedOn( 'ES2' ) if isOn else self.noAction(),
            'ES3'             : lambda isOn: audio.playEventSequence( audio.ES3 ) or matrixDriver.LedOn( 'ES3' ) if isOn else self.noAction(),
            'ES4'             : lambda isOn: audio.playEventSequence( audio.ES4 ) or matrixDriver.LedOn( 'ES4' ) if isOn else self.noAction(),
            'ES5'             : lambda isOn: audio.playEventSequence( audio.ES5 ) or matrixDriver.LedOn( 'ES5' ) if isOn else self.noAction(),
            'ES6'             : lambda isOn: audio.playEventSequence( audio.ES6 ) or matrixDriver.LedOn( 'ES6' ) if isOn else self.noAction(),
            'ES7'             : lambda isOn: audio.playEventSequence( audio.ES7 ) or matrixDriver.LedOn( 'ES7' ) if isOn else self.noAction(),
            'ES8'             : lambda isOn: audio.playEventSequence( audio.ES8 ) or matrixDriver.LedOn( 'ES8' ) if isOn else self.noAction(),
            'ES9'             : lambda isOn: audio.playEventSequence( audio.ES9 ) or matrixDriver.LedOn( 'ES9' ) if isOn else self.noAction(),
            'ES10'            : lambda isOn: audio.playEventSequence( audio.ES10 ) or matrixDriver.LedOn( 'ES10' ) if isOn else self.noAction(),

            # CRYOGENICS Switches

            'O2Fan'           : lambda isOn: audio.setContinuousPlayState( 'o2fan', isOn ),
            'H2Fan'           : lambda isOn: audio.setContinuousPlayState( 'h2fan', isOn ),
            'Pumps'           : lambda isOn: audio.setContinuousPlayState( 'pumps', isOn ),
            'Heat'            : lambda isOn: audio.setContinuousPlayState( 'heat', isOn ),

            # PYROTECHNICS Switches
            'DrogueDeploy'    : lambda isOn: audio.play('DrogueDeploy') or matrixDriver.LedOn('DrogueChute') if isOn else self.noAction(),

            # manually deploy the CM main parachutes.
            'MainDeploy'      : lambda isOn: audio.play('mainDeploy') or matrixDriver.LedOn('MainChute') if isOn else self.noAction(),

            # Manually separate the CSM from the launch vehicle during an abort or in normal operation.
            'CSM/LVDeploy'    : lambda isOn: audio.play('CSM/LVDeploy') if isOn else self.noAction(),

            # Separate for reentry
            'SM/CMDeploy'     : lambda isOn: audio.play('SM/CMDeploy') if isOn else self.noAction(),

            # Deploy the Launch Escape System Canard Parachutes
            'CanardDeploy'    : lambda isOn: audio.play('CanardDeploy') if isOn else self.noAction(),

            # Push-switch to jettison CM apex cover if automatic system fails during an abort or earth landing after a normal mission. 
            'ApexCoverJettsn' : lambda isOn: audio.play('ApexCoverJettsn') or matrixDriver.LedOn('Hatch') if isOn else self.noAction(),

            # Manually operates the Launch Escape System, either to jettison the LES tower or to fire the motor in the event of an LES abort.  In the former case, the explosive bolts connecting the LES tower to the CSM must fire first.
            'LesMotorFire'    : lambda isOn: audio.play('LesMotorFire') if isOn else self.noAction()
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
