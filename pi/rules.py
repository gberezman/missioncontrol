from audio import Audio
from time import sleep

class Rules:

    def sendMeterSetting(self, port, potId, potValue):
        print "sending pot {} = {}".format( potId, potValue )
        port.write( "Meter " + potId + " " + str(potValue) + "\n" )
        return True

    def __init__(self):
        self.audio = Audio()

        self.potRule = {
            'O2Flow'     : lambda port, potValue: self.sendMeterSetting(port, "O2", 12 - potValue),
            # 'Speaker'  : ?
            # 'Headset'  : ?
            'Voltage'    : lambda port, potValue: self.sendMeterSetting(port, "Voltage", 12 - potValue)
            # 'Resistance' : ?
            # 'Current'    : ?
            # 'AbortMode'  : ?
            # 'AntPitch'   : ?
            # 'AntYaw'     : ?
            # 'Tune'       : ?
            # 'Beam'       : ?
        }

        self.onRule = {
            'SPS'              : lambda : self.audio.spsThruster.play(loops = -1),
            # 'TEI'            : ?
            # 'TLI'            : ?
            # 'S-IC'           : ?
            # 'S-II'           : ?
            # 'S-iVB'          : ?
            # 'M-I'            : ?
            # 'M-II'           : ?
            # 'M-III'          : ?
            # 'Power'          : ?
            # 'Mode'           : ?
            # 'Lamp'           : ?
            # 'Ack'            : ?
            # 'DockingProbe'   : ?
            'DockingProbe'     : lambda : self.audio.spsThruster.play(loops = -1),
            # 'GlycolPump'     : ?
            # 'SCEPower'       : ?
            # 'WasteDump'      : ?
            'CabinFan'         : lambda : self.audio.fan.play(loops = -1),
            # 'H2OFlow'        : ?
            # 'IntLights'      : ?
            # 'SuitComp'       : ?
            'PTT'              : lambda : self.audio.quindarin.play(),
            # 'ArmAbort'       : ?
            # 'Abort'          : ?
            'O2Fan'            : lambda : self.audio.o2fan.play(loops = -1),
            'H2Fan'            : lambda : self.audio.h2fan.play(loops = -1),
            # 'Pumps'          : ?
            # 'Heat'           : ?
            # 'MainDeploy'     : ?
            'CSM/LVDeploy'     : lambda : self.audio.csmDeploy.play(),
            # 'SM/CMDeploy'    : ?
            # 'DrogueDeploy'   : ?
            #'CanardDeploy'    : ?
            #'ApexCoverJettsn' : ?
            #'LesMotorFire'    : ?
            #'ES1'             : ?
            #'ES2'             : ?
            #'ES3'             : ?
            #'ES4'             : ?
            #'ES5'             : ?
            #'ES6'             : ?
            #'ES7'             : ?
            #'ES8'             : ?
            #'ES9'             : ?
            #'ES10'            : ?
        }

        self.offRule = {
            'SPS'               : lambda : self.audio.spsThruster.stop(),
            # 'TEI'             : ?
            # 'TLI'             : ?
            # 'S-IC'            : ?
            # 'S-II'            : ?
            # 'S-iVB'           : ?
            # 'M-I'             : ?
            # 'M-II'            : ?
            # 'M-III'           : ?
            # 'Power'           : ?
            # 'Mode'            : ?
            # 'Lamp'            : ?
            # 'Ack'             : ?
            # 'DockingProbe'    : ?
            'DockingProbe'      : lambda : self.audio.spsThruster.stop(),
            # 'GlycolPump'      : ?
            # 'SCEPower'        : ?
            # 'WasteDump'       : ?
            'CabinFan'          : lambda : self.audio.fan.stop(),
            # 'H2OFlow'         : ?
            # 'IntLights'       : ?
            # 'SuitComp'        : ?
            'PTT'               : lambda : self.audio.quindarout.play(),
            # 'ArmAbort'        : ?
            # 'Abort'           : ?
            'O2 Fan'            : lambda : self.audio.o2fan.stop(),
            'H2 Fan'            : lambda : self.audio.h2fan.stop()
            # 'Pumps'           : ?
            # 'Heat'            : ?
            # 'MainDeploy'      : ?
            # 'CSM/LVDeploy'    : ?
            # 'SM/CMDeploy'     : ?
            # 'DrogueDeploy'    : ?
            # 'CanardDeploy'    : ?
            # 'ApexCoverJettsn' : ?
            # 'LesMotorFire'    : ?
            # 'ES1'             : ?
            # 'ES2'             : ?
            # 'ES3'             : ?
            # 'ES4'             : ?
            # 'ES5'             : ?
            # 'ES6'             : ?
            # 'ES7'             : ?
            # 'ES8'             : ?
            # 'ES9'             : ?
            # 'ES10'            : ?
        }
