from audio import Audio
from time import sleep

class Rules:
   
    def noAction( self, *args ):
        pass

    def sendMeterSetting(self, port, meterId, meterValue):
        print "sending meter {} = {}".format( meterId, meterValue )
        port.write( "Meter " + meterID + " " + str(meterValue) + "\n" )
        return True

    def __init__(self):
        self.audio = Audio()

        self.potRule = {
            # CAPCOM
            'Speaker'    : lambda port, potValue: noAction,
            'Headset'    : lambda port, potValue: noAction,

            # ABORT
            'AbortMode'  : lambda port, potValue: noAction,

            # EECOM
            'Voltage'    : lambda port, potValue: self.sendMeterSetting(port, "Voltage", 12 - potValue)
            'Current'    : lambda port, potValue: noAction,
            'Resistance' : lambda port, potValue: noAction,
            'O2Flow'     : lambda port, potValue: self.sendMeterSetting(port, "O2Flow", 12 - potValue),

            # INCO
            'AntPitch'   : lambda port, potValue: noAction,
            'AntYaw'     : lambda port, potValue: noAction,
            'Tune'       : lambda port, potValue: noAction,
            'Beam'       : lambda port, potValue: noAction
        }

        self.onRule = {
            # CONTROL
            'DockingProbe'    : lambda : self.audio.spsThruster.play(loops = -1),
            'GlycolPump'      : lambda: noAction,
            'SCEPower'        : lambda: noAction,
            'WasteDump'       : lambda: noAction,
            'CabinFan'        : lambda : self.audio.fan.play(loops = -1),
            'H2OFlow'         : lambda: noAction,
            'IntLights'       : lambda: noAction,
            'SuitComp'        : lambda: noAction,

            # ABORT
            'ArmAbort'        : lambda: noAction,
            'Abort'           : lambda: noAction,

            # BOOSTER
            'SPS'             : lambda : self.audio.spsThruster.play(loops = -1),
            'TEI'             : lambda: noAction,
            'TLI'             : lambda: noAction,
            'S-IC'            : lambda: noAction,
            'S-II'            : lambda: noAction,
            'S-iVB'           : lambda: noAction,
            'M-I'             : lambda: noAction,
            'M-II'            : lambda: noAction,
            'M-III'           : lambda: noAction,

            # C&WS
            'Power'           : lambda: noAction,
            'Mode'            : lambda: noAction,
            'Lamp'            : lambda: noAction,
            'Ack'             : lambda: noAction,

            # CAPCOM
            'PTT'             : lambda : self.audio.quindarin.play(),

            # EVENT SEQUENCE
            'ES1'             : lambda: noAction,
            'ES2'             : lambda: noAction,
            'ES3'             : lambda: noAction,
            'ES4'             : lambda: noAction,
            'ES5'             : lambda: noAction,
            'ES6'             : lambda: noAction,
            'ES7'             : lambda: noAction,
            'ES8'             : lambda: noAction,
            'ES9'             : lambda: noAction,
            'ES10'            : lambda: noAction,

            # CRYOGENICS
            'O2Fan'           : lambda : self.audio.o2fan.play(loops = -1),
            'H2Fan'           : lambda : self.audio.h2fan.play(loops = -1),
            'Pumps'           : lambda: noAction,
            'Heat'            : lambda: noAction,

            # PYROTECHNICS
            'MainDeploy'      : lambda: noAction,
            'CSM/LVDeploy'    : lambda : self.audio.csmDeploy.play(),
            'SM/CMDeploy'     : lambda: noAction,
            'DrogueDeploy'    : lambda: noAction,
            'CanardDeploy'    : lambda: noAction,
            'ApexCoverJettsn' : lambda: noAction,
            'LesMotorFire'    : lambda: noAction
        }

        self.offRule = {
            # CONTROL
            'DockingProbe'    : lambda: noAction,
            'GlycolPump'      : lambda: noAction,
            'SCEPower'        : lambda: noAction,
            'WasteDump'       : lambda: noAction,
            'CabinFan'        : lambda : self.audio.fan.stop(),
            'H2OFlow'         : lambda: noAction,
            'IntLights'       : lambda: noAction,
            'SuitComp'        : lambda: noAction,

            # ABORT
            'ArmAbort'        : lambda: noAction,
            'Abort'           : lambda: noAction,

            # BOOSTER
            'SPS'               : lambda : self.audio.spsThruster.stop(),
            'TEI'             : lambda: noAction,
            'TLI'             : lambda: noAction,
            'S-IC'            : lambda: noAction,
            'S-II'            : lambda: noAction,
            'S-iVB'           : lambda: noAction,
            'M-I'             : lambda: noAction,
            'M-II'            : lambda: noAction,
            'M-III'           : lambda: noAction,

            # C&WS
            'Power'           : lambda: noAction,
            'Mode'            : lambda: noAction,
            'Lamp'            : lambda: noAction,
            'Ack'             : lambda: noAction,

            # CAPCOM
            'PTT'             : lambda : self.audio.quindarout.play(),

            # EVENT SEQUENCE
            'ES1'             : lambda: noAction,
            'ES2'             : lambda: noAction,
            'ES3'             : lambda: noAction,
            'ES4'             : lambda: noAction,
            'ES5'             : lambda: noAction,
            'ES6'             : lambda: noAction,
            'ES7'             : lambda: noAction,
            'ES8'             : lambda: noAction,
            'ES9'             : lambda: noAction,
            'ES10'            : lambda: noAction,

            # CRYOGENICS
            'O2Fan'           : lambda : self.audio.o2fan.stop(),
            'H2Fan'           : lambda : self.audio.h2fan.stop()
            'Pumps'           : lambda: noAction,
            'Heat'            : lambda: noAction,

            # PYROTECHNICS
            'MainDeploy'      : lambda: noAction,
            'CSM/LVDeploy'    : lambda: noAction,
            'SM/CMDeploy'     : lambda: noAction,
            'DrogueDeploy'    : lambda: noAction,
            'CanardDeploy'    : lambda: noAction,
            'ApexCoverJettsn' : lambda: noAction,
            'LesMotorFire'    : lambda: noAction
        }
