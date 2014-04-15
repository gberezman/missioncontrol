from time import sleep,time

class CautionWarning:

    def __init__(self, audio, matrixDriver):
        self.audio = audio
        self.matrixDriver = matrixDriver
        self.state = 'inactive'

    def alert(self):
        if self.state == 'inactive':
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

    def arm(self):
        self.armed = True
        self.matrixDriver.ledOn( 'ArmAbort' )
        self.matrixDriver.ledOn( 'Abort' ),

    def disarm(self):
        self.armed = False
        self.matrixDriver.ledOff( 'ArmAbort' )
        self.matrixDriver.ledOff( 'Abort' ),

    def setMode(self, mode):
        self.mode = mode

    def abort(self):
        if self.armed:
            if self.mode == 1:
                self.audio.play('abortPad')
            elif self.mode == 2:
                self.audio.play('abortI')
            elif self.mode == 3:
                self.audio.play('abortII')
            elif self.mode == 4:
                self.audio.play('abortIII')
            elif self.mode == 5:
                self.audio.play('abortSIVB')
            elif self.mode == 6:
                self.audio.play('somethingElse')

            # shutdown sequence "sudo halt"

class EventRecord:

    def __init__(self, size = 10):
        self.size = size
        self.hits = []

    def record(self):
        hits.insert(0, int(time()))
        del self.hits[size:]

    def hitsInTheLastNSeconds(self, seconds):
        now = int(time())
        checkTime = now - seconds
        return sum(logTime > checkTime for logTime in self.hits)

class LatchedLED:

    def __init__(self, matrixDriver, led):
        self.matrixDriver = matrixDriver
        self.led = led
        self.buttonCount = 0

    def on(self, button):
        self.buttonCount += 1
        if self.buttonCount > 0:
            self.matrixDriver.LedOn(led)

    def off(self, button):
        self.buttonCount -= 1
        if self.buttonCount <= 0:
            self.matrixDriver.ledOff(led)

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
            # Replace with three way switch:
            'DockingProbeRetract' : lambda isOn: audio.play('dockingProbeRetract') or matrixDriver.ledOn('DockingProbe') if isOn 
                                                 else audio.stop('dockingProbeRetract') or matrixDriver.ledOff('DockingProbe'),

            'DockingProbeExtend'  : lambda isOn: audio.play('dockingProbeExtend') or matrixDriver.LedOn('DockingProbe') if isOn
                                                 else audio.stop('dockingProbeExtend') or matrixDriver.ledOff('DockingProbe'),

            'GlycolPump'          : lambda isOn: audio.playContinuous('glycolPump') or matrixDriver.LedOn('GlycolPump') if isOn
                                                 else audio.stop('glycolPump') or matrixDriver.ledOff('GlycolPump'),

            'SCEPower'            : lambda isOn: matrixDriver.LedOn('SCEPower') if isOn
                                                 else matrixDriver.ledOff('SCEPower'),

            'WasteDump'           : lambda isOn: audio.play('waste') or matrixDriver.LedOn('WasteDump') if isOn else self.noAction(),

            'CabinFan'            : lambda isOn: audio.playContinuous('fan') or matrixDriver.LedOn('CabinFan') if isOn
                                                 else audio.stop('fan') or matrixDriver.ledOff('CabinFan'),

            'H2OFlow'             : lambda isOn: audio.playContinuous('H2OFlow') or matrixDriver.LedOn('H2OFlow') if isOn
                                                 else audio.stop('H2OFlow') or matrixDriver.ledOff('H2OFlow'),

            'IntLights'           : lambda isOn: matrixDriver.LedOn('IntLights') if isOn
                                                 else matrixDriver.ledOff('IntLights'),

            'SuitComp'            : lambda isOn: matrixDriver.LedOn('SuitComp') if isOn
                                                 else matrixDriver.ledOff('SuitComp'),

            # ABORT
            'ArmAbort'            : lambda isOn: self.abort.arm() if isOn
                                                 else self.abort.disarm(),

            'Abort'               : lambda isOn: self.abort() if isOn else self.noAction(),

            # BOOSTER Switches
            # Service propulsion system
            'SPS'                 : lambda isOn: audio.play('spsThruster') or self.thrustStatus.on('SPS') or self.SPSPresses.record() if isOn
                                                 else audio.stop('spsThruster') or self.thrustStatus.off('SPS'),

            # Trans-Earth injection (from parking orbit around moon, sets on burn towards Earth)
            'TEI'                 : lambda isOn: audio.playContinuous('teiThruster') or self.thrustStatus.on('TEI') if isOn
                                                 else audio.stop('teiThruster') or self.thrustStatus.off('TEI'),

            # Trans-Lunar injection (puts on path towards moon)
            'TLI'                 : lambda isOn: audio.playContinuous('tliThruster') or self.thrustStatus.on('TLI') if isOn
                                                 else audio.stop('tliThruster') or self.thrustStatus.off('TLI'),

            
            # Saturn, first stage
            'S-IC'                : lambda isOn: audio.playContinuous('sicThruster') or self.thrustStatus.on('S-IC') if isOn
                                                 else audio.stop('sicThruster') or self.thrustStatus.off('S-IC'),

            # Saturn, second stage
            'S-II'                : lambda isOn: audio.playContinuous('siiThruster') or self.thrustStatus.on('S-II') if isOn
                                                 else audio.stop('siiThruster') or self.thrustStatus.off('S-II'),

            # Saturn V, third stage
            'S-iVB'               : lambda isOn: audio.playContinuous('sivbThruster') or self.thrustStatus.on('S-iVB') if isOn
                                                 else audio.stop('sivbThruster') or self.thrustStatus.off('S-iVB'),

            'M-I'                 : lambda isOn: audio.playContinuous('miThruster') or self.thrustStatus.on('M-I') if isOn
                                                 else audio.stop('miThruster') or self.thrustStatus.off('M-I'),

            'M-II'                : lambda isOn: audio.playContinuous('miiThruster') or self.thrustStatus.on('M-II') if isOn
                                                 else audio.stop('miiThruster') or self.thrustStatus.off('M-II'),

            'M-III'               : lambda isOn: audio.playContinuous('miiiThruster') or self.thrustStatus.on('M-III') if isOn
                                                 else audio.stop('miiiThruster') or self.thrustStatus.off('M-III'),

            # C&WS Switches
            # square wave alternating between 750 and 2000cps changing 2.5 times per second
            # 'Caution' # lights up when C&WS fires
                # pressing clears tone, but leaves lights on
            # 'Power'  # Resets the C&WS system
            # 'Mode' # what systems to be monitored (CM deactivates the SM monitors)
            # 'Lamp' # Wire Lamp to light all LED's directly
            # 'Ack' # no lights, audio and master alarm only, probably should be illuminated

            # CAPCOM Switches
            'PTT'                 : lambda isOn: audio.play('quindarin') if isOn
                                                 else audio.play('quindarout'),

            # EVENT SEQUENCE Switches
            'ES1'                 : lambda isOn: audio.playES( audio.ES1 ) or matrixDriver.LedOn( 'ES1' ) if isOn else self.noAction(),
            'ES2'                 : lambda isOn: audio.playES( audio.ES2 ) or matrixDriver.LedOn( 'ES2' ) if isOn else self.noAction(),
            'ES3'                 : lambda isOn: audio.playES( audio.ES3 ) or matrixDriver.LedOn( 'ES3' ) if isOn else self.noAction(),
            'ES4'                 : lambda isOn: audio.playES( audio.ES4 ) or matrixDriver.LedOn( 'ES4' ) if isOn else self.noAction(),
            'ES5'                 : lambda isOn: audio.playES( audio.ES5 ) or matrixDriver.LedOn( 'ES5' ) if isOn else self.noAction(),
            'ES6'                 : lambda isOn: audio.playES( audio.ES6 ) or matrixDriver.LedOn( 'ES6' ) if isOn else self.noAction(),
            'ES7'                 : lambda isOn: audio.playES( audio.ES7 ) or matrixDriver.LedOn( 'ES7' ) if isOn else self.noAction(),
            'ES8'                 : lambda isOn: audio.playES( audio.ES8 ) or matrixDriver.LedOn( 'ES8' ) if isOn else self.noAction(),
            'ES9'                 : lambda isOn: audio.playES( audio.ES9 ) or matrixDriver.LedOn( 'ES9' ) if isOn else self.noAction(),
            'ES10'                : lambda isOn: audio.playES( audio.ES10 ) or matrixDriver.LedOn( 'ES10' ) if isOn else self.noAction(),

            # CRYOGENICS Switches

            'O2Fan'               : lambda isOn: audio.playContinuous('o2fan') if isOn else audio.stop('o2fan'),

            'H2Fan'               : lambda isOn: audio.playContinuous('h2fan') if isOn else audio.stop('h2fan'),

            'Pumps'               : lambda isOn: audio.playContinuous('pumps') if isOn else audio.stop('pumps'),

            'Heat'                : lambda isOn: audio.playContinuous('heat') if isOn else audio.stop('heat'),

            # PYROTECHNICS Switches
            'DrogueDeploy'        : lambda isOn: audio.play('DrogueDeploy') or matrixDriver.LedOn('DrogueChute') if isOn else self.noAction(),

            # manually deploy the CM main parachutes.
            'MainDeploy'          : lambda isOn: audio.play('mainDeploy') or matrixDriver.LedOn('MainChute') if isOn else self.noAction(),

            # Manually separate the CSM from the launch vehicle during an abort or in normal operation.
            'CSM/LVDeploy'        : lambda isOn: audio.play('CSM/LVDeploy') if isOn else self.noAction(),

            # Separate for reentry
            'SM/CMDeploy'         : lambda isOn: audio.play('SM/CMDeploy') if isOn else self.noAction(),

            # Deploy the Launch Escape System Canard Parachutes
            'CanardDeploy'        : lambda isOn: audio.play('CanardDeploy') if isOn else self.noAction(),

            # Push-switch to jettison CM apex cover if automatic system fails during an abort or earth landing after a normal mission. 
            'ApexCoverJettsn'     : lambda isOn: audio.play('ApexCoverJettsn') or matrixDriver.LedOn('Hatch') if isOn else self.noAction(),

            # Manually operates the Launch Escape System, either to jettison the LES tower or to fire the motor in the event of an LES abort.  In the former case, the explosive bolts connecting the LES tower to the CSM must fire first.
            'LesMotorFire'        : lambda isOn: audio.play('LesMotorFire') if isOn else self.noAction()
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
