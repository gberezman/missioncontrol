from audio import Audio
from time import sleep

class Rules:
   
    def noAction( self, *args ):
        pass

    def sendMeterSetting(self, port, meterId, meterValue):
        print "sending meter {} = {}".format( meterId, meterValue )
        port.write( "Meter " + meterId + " " + str(meterValue) + "\n" )

    def playES(self, sound):
        self.audio.esChannel.stop() 
        self.audio.esChannel.play( sound )

    def playCaution(self, sound):
        self.audio.cautionChannel.stop() 
        self.audio.cautionChannel.play( sound )
        
    def __init__(self):
        self.audio = Audio()

        self.potRule = {
            # CAPCOM
            'Speaker'    : lambda port, potValue: self.noAction,
            'Headset'    : lambda port, potValue: self.noAction,

            # ABORT
            'AbortMode'  : lambda port, potValue: self.noAction,

            # EECOM
            'Voltage'    : lambda port, potValue: self.sendMeterSetting(port, "Voltage", 12 - potValue),
            'Current'    : lambda port, potValue: self.noAction,
            'Resistance' : lambda port, potValue: self.noAction,
            'O2Flow'     : lambda port, potValue: self.sendMeterSetting(port, "O2Flow", 12 - potValue),

            # INCO
            'AntPitch'   : lambda port, potValue: self.noAction,
            'AntYaw'     : lambda port, potValue: self.noAction,
            'Tune'       : lambda port, potValue: self.noAction,
            'Beam'       : lambda port, potValue: self.noAction
        }

        self.onRule = {
            # CONTROL
            'DockingProbe'    : lambda : self.audio.spsThruster.play(loops = -1),
            'GlycolPump'      : lambda : self.noAction,
            'SCEPower'        : lambda : self.noAction,
            'WasteDump'       : lambda : self.noAction,
            'CabinFan'        : lambda : self.audio.fan.play(loops = -1),
            'H2OFlow'         : lambda : self.noAction,
            'IntLights'       : lambda : self.noAction,
            'SuitComp'        : lambda : self.noAction,

            # ABORT
            'ArmAbort'        : lambda : self.noAction,
            'Abort'           : lambda : self.noAction,

            # BOOSTER
            'SPS'             : lambda : self.audio.spsThruster.play(loops = -1),
            'TEI'             : lambda : self.noAction,
            'TLI'             : lambda : self.noAction,
            'S-IC'            : lambda : self.noAction,
            'S-II'            : lambda : self.noAction,
            'S-iVB'           : lambda : self.noAction,
            'M-I'             : lambda : self.noAction,
            'M-II'            : lambda : self.noAction,
            'M-III'           : lambda : self.noAction,

            # C&WS
            'Power'           : lambda : self.noAction,
            'Mode'            : lambda : self.noAction,
            'Lamp'            : lambda : self.noAction,
            'Ack'             : lambda : self.noAction,

            # CAPCOM
            'PTT'             : lambda : self.audio.quindarin.play(),

            # EVENT SEQUENCE
            'ES1'             : lambda : playES( self.audio.ES1 ),
            'ES2'             : lambda : playES( self.audio.ES2 ),
            'ES3'             : lambda : self.noAction,
            'ES4'             : lambda : self.noAction,
            'ES5'             : lambda : self.noAction,
            'ES6'             : lambda : self.noAction,
            'ES7'             : lambda : self.noAction,
            'ES8'             : lambda : self.noAction,
            'ES9'             : lambda : self.noAction,
            'ES10'            : lambda : self.noAction,

            # CRYOGENICS
            'O2Fan'           : lambda : self.audio.o2fan.play(loops = -1),
            'H2Fan'           : lambda : self.audio.h2fan.play(loops = -1),
            'Pumps'           : lambda : self.noAction,
            'Heat'            : lambda : self.noAction,

            # PYROTECHNICS
            'MainDeploy'      : lambda : self.noAction,
            'CSM/LVDeploy'    : lambda : self.audio.csmDeploy.play(),
            'SM/CMDeploy'     : lambda : self.noAction,
            'DrogueDeploy'    : lambda : self.noAction,
            'CanardDeploy'    : lambda : self.noAction,
            'ApexCoverJettsn' : lambda : self.noAction,
            'LesMotorFire'    : lambda : self.noAction
        }

        self.offRule = {
            # CONTROL
            'DockingProbe'    : lambda : self.noAction,
            'GlycolPump'      : lambda : self.noAction,
            'SCEPower'        : lambda : self.noAction,
            'WasteDump'       : lambda : self.noAction,
            'CabinFan'        : lambda : self.audio.fan.stop(),
            'H2OFlow'         : lambda : self.noAction,
            'IntLights'       : lambda : self.noAction,
            'SuitComp'        : lambda : self.noAction,

            # ABORT
            'ArmAbort'        : lambda : self.noAction,
            'Abort'           : lambda : self.noAction,

            # BOOSTER
            'SPS'               : lambda : self.audio.spsThruster.stop(),
            'TEI'             : lambda : self.noAction,
            'TLI'             : lambda : self.noAction,
            'S-IC'            : lambda : self.noAction,
            'S-II'            : lambda : self.noAction,
            'S-iVB'           : lambda : self.noAction,
            'M-I'             : lambda : self.noAction,
            'M-II'            : lambda : self.noAction,
            'M-III'           : lambda : self.noAction,

            # C&WS
            'Power'           : lambda : self.noAction,
            'Mode'            : lambda : self.noAction,
            'Lamp'            : lambda : self.noAction,
            'Ack'             : lambda : self.noAction,

            # CAPCOM
            'PTT'             : lambda : self.audio.quindarout.play(),

            # EVENT SEQUENCE
            'ES1'             : lambda : self.noAction,
            'ES2'             : lambda : self.noAction,
            'ES3'             : lambda : self.noAction,
            'ES4'             : lambda : self.noAction,
            'ES5'             : lambda : self.noAction,
            'ES6'             : lambda : self.noAction,
            'ES7'             : lambda : self.noAction,
            'ES8'             : lambda : self.noAction,
            'ES9'             : lambda : self.noAction,
            'ES10'            : lambda : self.noAction,

            # CRYOGENICS
            'O2Fan'           : lambda : self.audio.o2fan.stop(),
            'H2Fan'           : lambda : self.audio.h2fan.stop(),
            'Pumps'           : lambda : self.noAction,
            'Heat'            : lambda : self.noAction,

            # PYROTECHNICS
            'MainDeploy'      : lambda : self.noAction,
            'CSM/LVDeploy'    : lambda : self.noAction,
            'SM/CMDeploy'     : lambda : self.noAction,
            'DrogueDeploy'    : lambda : self.noAction,
            'CanardDeploy'    : lambda : self.noAction,
            'ApexCoverJettsn' : lambda : self.noAction,
            'LesMotorFire'    : lambda : self.noAction
        }
