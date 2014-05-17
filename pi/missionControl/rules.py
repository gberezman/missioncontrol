from time import sleep,time
import random

class SwitchState:

    def __init__(self, switch, isOn = False):
        self.switch = switch
        self.isOn = isOn

    def setState(self, isOn):
        self.isOn = isOn

class CautionWarning:

    def __init__(self, audio, matrixDriver):
        self.audio = audio
        self.matrixDriver = matrixDriver
        self.state = 'inactive'

    def alert(self):
        self.state = 'active'
        self.audio.play( 'caution', dedicatedChannel = self.audio.cautionChannel, continuous = True )
        self.matrixDriver.ledOn( 'MasterAlarm' )

    def clear(self):
        self.state = 'inactive'
        self.audio.stop( 'caution' )
        self.matrixDriver.ledOff( 'MasterAlarm' )

class Abort:

    def __init__(self, audio, matrixDriver):
        self.audio = audio
        self.matrixDriver = matrixDriver

        self.armed = False
        self.mode = 1

    def setArm(self, armed = True):
        self.armed = armed
        if self.armed:
            self.matrixDriver.ledOn( 'Abort' ),
        else:
            self.matrixDriver.ledOff( 'Abort' ),

    def setMode(self, mode):
        self.mode = mode

    def abort(self):
        if self.armed:
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
                self.audio.play( 'abortIV' )

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

class Pyrotechnics:

    def __init__(self, led, clip):
        self.led = led;
        self.clip = clip
        self.fired = False

    def fire(self, isOn, matrixDriver, audio):
        #if isOn and not self.fired:
        matrixDriver.setLed( self.led, isOn )
        if isOn:
            audio.play( self.clip )

class Inco:

    def __init__(self):
        self.pitch = 5
        self.yaw = 12
        self.tune = 5
        self.beam = 12

    def setAntPitch(self, value, matrixDriver):
        self.pitch = int( value )
        self.write(matrixDriver)

    def setAntYaw(self, value, matrixDriver):
        self.yaw = int( value ) 
        self.write(matrixDriver)

    def setTune(self, value, matrixDriver):
        self.tune = int( value )
        self.write(matrixDriver)

    def setBeam(self, value, matrixDriver):
        self.beam = int( int( value ) )
        self.write(matrixDriver)

    def write(self, matrixDriver):
        pitchOffset = int( self.pitch / 2 )
        yawLo = self.yaw - pitchOffset
        yawHi = self.yaw + pitchOffset
        colors = ""
        for idx in range( 1, 24 ):
            if idx < yawLo - 2:
                colors += "R"
            elif idx < yawLo:
                colors += "Y"
            elif idx > yawHi + 2:
                colors += "R"
            elif idx > yawHi:
                colors += "Y"
            else:
                colors += "G"
            
        matrixDriver.setIncoColors( colors )

        beamOffset = int( self.beam ) / 2
        matrixDriver.setInco( self.tune - beamOffset, self.tune + beamOffset )

class FluctuatingMeter:

    def __init__(self, meter, initialValue = 12, frequency_s = 3):
        self.meter = meter
        self.value = initialValue
        self.frequency_s = frequency_s
        self.lastUpdate = time()

    def update(self, matrixDriver, isFanOn):
        now = time()
        if now - self.lastUpdate > self.frequency_s:
            if ( not isFanOn ) or ( random.randint( 1, 10 ) > 4 ):
                self.value += random.randint(-1, 1)
                self.value = max( self.value, 1 )
                self.value = min( self.value, 12 )

            self.write( matrixDriver )
            self.lastUpdate = now

    def write(self, matrixDriver):
        matrixDriver.setMeter( self.meter, self.value )

    def normalize(self, isOn, matrixDriver):
        if isOn and self.value < 4:
            self.value = random.randint( 4, 6 )
        elif isOn and self.value > 9:
            self.value = random.randint( 6, 9 )
        self.write( matrixDriver )

class DecayingMeter:

    def __init__(self, meter, initialValue = 12, decayRate_s = 120):
        self.meter = meter
        self.value = initialValue
        self.decayRate_s = decayRate_s
        self.lastUpdate = time()

    def decay(self, matrixDriver):
        now = time()
        if now - self.lastUpdate > self.decayRate_s:
            self.value = max( self.value - 1, 1 )
            self.write( matrixDriver )
            self.lastUpdate = now

    def write(self, matrixDriver):
        matrixDriver.setMeter( self.meter, self.value )

class ThreeDigitControl:
    
    def __init__(self, numberLabel, frequency_s = 2, lower = 150, upper = 350, range = 20 ):
        self.updateTime = 0
        self.value = random.randint( lower, upper )
        self.frequency_s = frequency_s
        self.lower = lower
        self.upper = upper
        self.range = range
        self.numberLabel = numberLabel

    def update(self, matrixDriver):
        now = time()
        if now - self.updateTime > self.frequency_s:
            self.adjustTime()
            self.write( matrixDriver )
            self.updateTime = time()

    def adjustTime(self):
        self.value += random.randint( - self.range, self.range )
        self.value = min( self.value, self.upper )
        self.value = max( self.value, self.lower )

    def write(self, matrixDriver):
        matrixDriver.setNumber( self.numberLabel, self.value )

class Rules:
   
    def noAction(self, *args):
        sleep( 0.05 )

    def applyTemporalRules(self):
        now = time()

        #if self.SPSPresses.hitsInTheLastNSeconds(2) > 5:
        #    self.matrixDriver.LedOn('SPSPress')
        #    self.cw.alert()
        #else:
        #    self.matrixDriver.ledOff('SPSPress')
 
        # if self.SPSPresses.hitsInTheLastNSeconds(4) > 5:
        #     self.matrixDriver.LedOn('SPSFlngTempHi')
        #     self.cw.alert()
        # else:
        #     self.matrixDriver.ledOff('SPSPress')

        self.IHR.update( self.matrixDriver )
        self.AHR.update( self.matrixDriver )
        self.ABR.update( self.matrixDriver )
        self.Pitch.update( self.matrixDriver )
        self.Yaw.update( self.matrixDriver )
        self.Roll.update( self.matrixDriver )

        self.O2Pressure.update( self.matrixDriver, self.O2FanState.isOn )
        self.H2Pressure.update( self.matrixDriver, self.H2FanState.isOn )

        self.O2Qty.decay( self.matrixDriver )
        self.H2Qty.decay( self.matrixDriver )

    def getRule(self, name):
        if name:
            return self.__rules.get(name, lambda value: self.noAction())
        else:
            return lambda value: self.noAction()

    def __init__(self, audio, matrixDriver):
        self.matrixDriver = matrixDriver
        self.audio = audio

        self.abort = Abort(audio, matrixDriver)
        self.thrustStatus = LatchedLED(matrixDriver, 'Thrust')
        self.ullageStatus = LatchedLED(matrixDriver, 'Ullage')
        self.SPSPresses = EventRecord()
        self.cw = CautionWarning(audio, matrixDriver)

        self.IHR = ThreeDigitControl( "IHR" )
        self.AHR = ThreeDigitControl( "AHR", frequency_s = 2.5 )
        self.ABR = ThreeDigitControl( "ABR", frequency_s = 3 )
        self.Pitch = ThreeDigitControl( "Pitch", lower = 0, upper = 359, range = 3, frequency_s = 2.5 )
        self.Yaw = ThreeDigitControl( "Yaw", lower = 0, upper = 359, range = 3, frequency_s = 4 )
        self.Roll = ThreeDigitControl( "Roll", lower = 0, upper = 359, range = 3 )

        self.mainDeploy      = Pyrotechnics( 'MainChute', 'MainDeploy' )
        self.drogueDeploy    = Pyrotechnics( 'DrogueChute', 'DrogueDeploy' )
        self.csmDeploy       = Pyrotechnics( 'SMRCSA', 'CsmDeploy' )
        self.canardDeploy    = Pyrotechnics( '', 'CanardDeploy' )
        self.smDeploy        = Pyrotechnics( 'SMRCSB', 'SmDeploy' )
        self.apexCoverJettsn = Pyrotechnics( 'Hatch', 'ApexCoverJettsn' )
        self.lesMotorFire    = Pyrotechnics( 'CMRCS1', 'LesMotorFire' )

        self.O2FanState = SwitchState( False )
        self.H2FanState = SwitchState( False )

        self.O2Pressure = FluctuatingMeter( "O2Pressure", initialValue = random.randint( 7, 9 ), frequency_s = 4 )
        self.O2Pressure.write( matrixDriver )
        self.H2Pressure = FluctuatingMeter( "H2Pressure", initialValue = random.randint( 7, 9 ) )
        self.H2Pressure.write( matrixDriver )

        self.O2Qty      = DecayingMeter( "O2Qty" )
        self.O2Qty.write( matrixDriver )
        self.H2Qty      = DecayingMeter( "H2Qty", decayRate_s = 180 )
        self.H2Qty.write( matrixDriver )

        self.inco = Inco()

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
            'AntPitch' : lambda value: self.inco.setAntPitch( 12 - value, matrixDriver ),
            'AntYaw'   : lambda value: self.inco.setAntYaw( 12 - value, matrixDriver ),
            'Tune'     : lambda value: self.inco.setTune( 12 - value, matrixDriver ),
            'Beam'     : lambda value: self.inco.setBeam( 12 - value, matrixDriver ),

            # In Arduino, tie the 4 pots directly to the LED graph:
                # Tune moves the focal section up and down the graph (i.e. moves the beam)
                # Beam adjusts the width of the focal section
                # AntPitch changes the focus of the green section (yellow, red the further you move away from focus)
                # AntYaw changes the the width of the green section

            # CONTROL Switches
            'DockingProbe'    : lambda isExtending: matrixDriver.setLed( 'DockingProbe', isExtending ) \
                                                    or matrixDriver.setLed( 'DockingTarget', isExtending ) \
                                                    or audio.togglePlay( 'DockingProbeRetract', not isExtending ) \
                                                    or audio.togglePlay( 'DockingProbeExtend', isExtending ),

            # Game condition: Show GlycolTempLow to get user to run glycol pump and clear warning
            'GlycolPump'      : lambda isOn: matrixDriver.setLed( 'GlycolPump', isOn ) \
                                             or audio.togglePlay( 'GlycolPump', isOn, continuous = True ),
            'SCEPower'        : lambda isOn: matrixDriver.setLed( 'SCEPower', isOn ),
            'WasteDump'       : lambda isOn: matrixDriver.setLed( 'WasteDump', isOn ) \
                                             or ( audio.play( 'WasteDump' ) if isOn else self.noAction() ),
            'CabinFan'        : lambda isOn: matrixDriver.setLed( 'CabinFan', isOn ) \
                                             or audio.togglePlay( 'CabinFan', isOn, continuous = True ),
            'H2OFlow'         : lambda isOn: matrixDriver.setLed( 'H2OFlow', isOn ) \
                                             or audio.togglePlay( 'H2OFlow', isOn, continuous = True ),
            'IntLights'       : lambda isOn: matrixDriver.setLed( 'Lights', isOn ),
            'SuitComp'        : lambda isOn: matrixDriver.setLed( 'SuitComp', isOn ),

            # ABORT
            #'ArmAbort'        : lambda armed: self.abort.setArm( armed ),
            #'Abort'           : lambda pressed: self.abort.abort() if pressed else self.noAction(),

            # BOOSTER Switches
            # Service propulsion system
            'SPS'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'spsThruster', isOn, continuous = True ),
                                             # or self.SPSPresses.record( isOn ),

            # Trans-Earth injection (from parking orbit around moon, sets on burn towards Earth)
            'TEI'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'teiThruster', isOn, continuous = True ),

            # Trans-Lunar injection (puts on path towards moon)
            'TLI'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'tliThruster', isOn, continuous = True ),
            
            # Saturn, first stage
            'S-IC'            : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'sicThruster', isOn, continuous = True ),

            # Saturn, second stage
            'S-II'            : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'siiThruster', isOn, continuous = True ),

            # Saturn V, third stage
            'S-iVB'           : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or audio.togglePlay( 'sivbThruster', isOn, continuous = True ),

            # Maneuvering thruster (ullage)
            'M-I'             : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or self.ullageStatus.on( isOn ) \
                                             or audio.togglePlay( 'miThruster', isOn, continuous = True ),

            # Maneuvering thruster (ullage)
            'M-II'            : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or self.ullageStatus.on( isOn ) \
                                             or audio.togglePlay( 'miiThruster', isOn, continuous = True ),

            # Maneuvering thruster (ullage)
            'M-III'           : lambda isOn: self.thrustStatus.on( isOn ) \
                                             or self.ullageStatus.on( isOn ) \
                                             or audio.togglePlay( 'miiiThruster', isOn, continuous = True ),

            # C&WS Switches
            # square wave alternating between 750 and 2000cps changing 2.5 times per second
            # 'Caution' # lights up when C&WS fires
                # pressing clears tone, but leaves lights on
            # 'Power'  # Resets the C&WS system
            # 'Mode' # what systems to be monitored (CM deactivates the SM monitors)
            # 'Lamp' # Wire Lamp to light all LED's directly
            # 'Ack' # no lights, audio and master alarm only, probably should be illuminated

            # CAPCOM Switches
            #'PTT'             : lambda isOn: audio.togglePlay( 'quindarin', isOn ) \
                                             #or audio.togglePlay( 'quindarout', not isOn ),

            # EVENT SEQUENCE Switches
            #'ES1'             : lambda isOn: audio.play( audio.ES1, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES1' ) if isOn else self.noAction(),
            #'ES2'             : lambda isOn: audio.play( audio.ES2, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES2' ) if isOn else self.noAction(),
            #'ES3'             : lambda isOn: audio.play( audio.ES3, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES3' ) if isOn else self.noAction(),
            #'ES4'             : lambda isOn: audio.play( audio.ES4, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES4' ) if isOn else self.noAction(),
            #'ES5'             : lambda isOn: audio.play( audio.ES5, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES5' ) if isOn else self.noAction(),
            #'ES6'             : lambda isOn: audio.play( audio.ES6, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES6' ) if isOn else self.noAction(),
            #'ES7'             : lambda isOn: audio.play( audio.ES7, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES7' ) if isOn else self.noAction(),
            #'ES8'             : lambda isOn: audio.play( audio.ES8, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES8' ) if isOn else self.noAction(),
            #'ES9'             : lambda isOn: audio.play( audio.ES9, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES9' ) if isOn else self.noAction(),
            #'ES10'            : lambda isOn: audio.play( audio.ES10, dedicatedChannel = audio.eventSequenceChannel ) or matrixDriver.LedOn( 'ES10' ) if isOn else self.noAction(),

            # CRYOGENICS Switches

            'O2Fan'           : lambda isOn: self.O2FanState.setState( isOn ) \
                                             or matrixDriver.setLed( 'O2Fan', isOn ) \
                                             or self.O2Pressure.normalize( isOn, matrixDriver ) \
                                             or audio.togglePlay( 'o2fan', isOn, continuous = True ),
            'H2Fan'           : lambda isOn: self.H2FanState.setState( isOn ) \
                                             or matrixDriver.setLed('H2Fan', isOn ) \
                                             or self.H2Pressure.normalize( isOn, matrixDriver ) \
                                             or audio.togglePlay( 'h2fan', isOn, continuous = True ),
            'Pumps'           : lambda isOn: matrixDriver.setLed('Pumps', isOn ) \
                                             or audio.togglePlay( 'pumps', isOn, continuous = True ),
            'Heat'            : lambda isOn: matrixDriver.setLed('Heat', isOn ) \
                                             or audio.togglePlay( 'heat', isOn, continuous = True ),

            # PYROTECHNICS Switches
            # manually deploy the CM main parachutes.
            'MainDeploy'       : lambda isOn: self.mainDeploy.fire( isOn, matrixDriver, audio ),

            # Parachute to slow ship down
            'DrogueDeploy'     : lambda isOn: self.drogueDeploy.fire( isOn, matrixDriver, audio ),

            # Manually separate the CSM from the launch vehicle during an abort or in normal operation.
            'CSM/LVDeploy'    : lambda isOn: self.csmDeploy.fire( isOn, matrixDriver, audio ),

            # Deploy the Launch Escape System Canard Parachutes
            'CanardDeploy'    : lambda isOn: self.canardDeploy.fire( isOn, matrixDriver, audio ),

            # Separate for reentry
            'SM/CMDeploy'     : lambda isOn: self.smDeploy.fire( isOn, matrixDriver, audio ),

            # Push-switch to jettison CM apex cover if automatic system fails during an abort or earth landing after a normal mission. 
            'ApexCoverJettsn' : lambda isOn: self.apexCoverJettsn.fire( isOn, matrixDriver, audio ),

            # Manually operates the Launch Escape System, either to jettison the LES tower or to fire the motor in the event of an LES abort.  In the former case, the explosive bolts connecting the LES tower to the CSM must fire first.
            'LesMotorFire'    : lambda isOn: self.lesMotorFire.fire( isOn, matrixDriver, audio )
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

if __name__ == '__main__':

    from arduino import StubbedArduinoSerial, ArduinoMatrixDriver
    from audio import Audio
    from time import sleep

    rules = Rules( Audio(), ArduinoMatrixDriver( StubbedArduinoSerial() ) )

    print "Abort IV"
    rules.getRule( 'AbortMode' )(6)
    rules.getRule( 'ArmAbort' )( armed = True )
    rules.getRule( 'Abort' )( pressed = True )
    sleep(2)

    print "H2O Flow on"
    rule = rules.getRule( 'H2OFlow' )
    rule( isOn = True )
    sleep(2)
    print "H2O Flow off"
    rule( isOn = False )

    print "Waste dump on"
    rule = rules.getRule( 'WasteDump' )
    rule( isOn = True )
    print "Waste dump off"
    rule( isOn = False )
    sleep(3)

    rule = rules.getRule( 'DockingProbe' )
    print( "Extend docking probe" )
    rule( isExtending = True )
    sleep(3)
    print( "Retract docking probe" )
    rule( isExtending = False )
    sleep(8)

    print "Glycol pump on"
    rule = rules.getRule( 'GlycolPump' )
    rule( isOn = True )
    sleep(2)
    print "Glycol pump off"
    rule( isOn = False )


