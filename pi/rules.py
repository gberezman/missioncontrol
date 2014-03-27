from audio import Audio
from time import sleep

class Rules:

    def noAction(self, *args):
        print "no action"

    def switchOn(self, switch):
        self.onRule.get(switch, self.noAction)()

    def switchOff(self, switch):
        self.offRule.get(switch, self.noAction)()

    def potEvent(self, port, pot, potValue):
        self.potRule.get(pot, self.noAction)(port, potValue)

    def sendMeterSetting(self, port, potId, potValue):
        print "sending pot value {}".format( potValue )
        port.write( "Meter " + potId + " " + str(potValue) + "\n" )
        return True

    def __init__(self):
        self.audio = Audio()

        self.potRule = {
            'O2Flow'     : lambda port, potValue: self.sendMeterSetting(port, "O2", 12 - potValue),
            'Speaker'    : self.noAction,
            'Headset'    : self.noAction,
            'Voltage'    : lambda port, potValue: self.sendMeterSetting(port, "V", 12 - potValue) and self.sendMeterSetting(port, "O2", 12 - potValue),
            'Resistance' : self.noAction,
            'Current'    : self.noAction,
            'AbortMode'  : self.noAction,
            'AntPitch'   : self.noAction,
            'AntYaw'     : self.noAction,
            'Tune'       : self.noAction,
            'Beam'       : self.noAction
        }

        self.onRule = {
            'SPS'               : lambda : self.audio.spsThruster.play(loops = -1),
            'TEI'               : self.noAction,
            'TLI'               : self.noAction,
            'S-IC'              : self.noAction,
            'S-II'              : self.noAction,
            'S-iVB'             : self.noAction,
            'M-I'               : self.noAction,
            'M-II'              : self.noAction,
            'M-III'             : self.noAction,
            'Power'             : self.noAction,
            'Mode'              : self.noAction,
            'Lamp'              : self.noAction,
            'Ack'               : self.noAction,
            'DockingProbe'      : self.noAction,
            'GlycolPump'        : self.noAction,
            'SCEPower'          : self.noAction,
            'WasteDump'         : self.noAction,
            'CabinFan'          : lambda : self.audio.fan.play(loops = -1),
            'H2OFlow'           : self.noAction,
            'IntLights'         : self.noAction,
            'SuitComp'          : self.noAction,
            'PTT'               : lambda : self.audio.quindarin.play(),
            'ArmAbort'          : self.noAction,
            'Abort'             : self.noAction,
            'O2Fan'             : lambda : self.audio.o2fan.play(loops = -1),
            'H2Fan'             : lambda : self.audio.h2fan.play(loops = -1),
            'Pumps'             : self.noAction,
            'Heat'              : self.noAction,
            'MainDeploy'        : self.noAction,
            'CSM/LVDeploy'      : lambda : self.audio.csmDeploy.play(),
            'SM/CMDeploy'       : self.noAction,
            'DrogueDeploy'      : self.noAction,
            'CanardDeploy'      : self.noAction,
            'ApexCoverJettsn'   : self.noAction,
            'LesMotorFire'      : self.noAction,
            'ES1'               : self.noAction,
            'ES2'               : self.noAction,
            'ES3'               : self.noAction,
            'ES4'               : self.noAction,
            'ES5'               : self.noAction,
            'ES6'               : self.noAction,
            'ES7'               : self.noAction,
            'ES8'               : self.noAction,
            'ES9'               : self.noAction,
            'ES10'              : self.noAction,
        }

        self.offRule = {
            'SPS'               : lambda : self.audio.spsThruster.stop(),
            'TEI'               : self.noAction,
            'TLI'               : self.noAction,
            'S-IC'              : self.noAction,
            'S-II'              : self.noAction,
            'S-iVB'             : self.noAction,
            'M-I'               : self.noAction,
            'M-II'              : self.noAction,
            'M-III'             : self.noAction,
            'Power'             : self.noAction,
            'Mode'              : self.noAction,
            'Lamp'              : self.noAction,
            'Ack'               : self.noAction,
            'Docking Probe'     : self.noAction,
            'Glycol Pump'       : self.noAction,
            'SCE Power'         : self.noAction,
            'Waste Dump'        : self.noAction,
            'Cabin Fan'         : lambda : self.audio.fan.stop(),
            'H2O Flow'          : self.noAction,
            'Int Lights'        : self.noAction,
            'Suit Comp'         : self.noAction,
            'PTT'               : lambda : self.audio.quindarout.play(),
            'Arm Abort'         : self.noAction,
            'Abort'             : self.noAction,
            'O2 Fan'            : lambda : self.audio.o2fan.stop(),
            'H2 Fan'            : lambda : self.audio.h2fan.stop(),
            'Pumps'             : self.noAction,
            'Heat'              : self.noAction,
            'Main Deploy'       : self.noAction,
            'CSM/LV Deploy'     : self.noAction,
            'SM/CM Deploy'      : self.noAction,
            'Drogue Deploy'     : self.noAction,
            'Canard Deploy'     : self.noAction,
            'Apex Cover Jettsn' : self.noAction,
            'Les Motor Fire'    : self.noAction,
            'ES 1'              : self.noAction,
            'ES 2'              : self.noAction,
            'ES 3'              : self.noAction,
            'ES 4'              : self.noAction,
            'ES 5'              : self.noAction,
            'ES 6'              : self.noAction,
            'ES 7'              : self.noAction,
            'ES 8'              : self.noAction,
            'ES 9'              : self.noAction,
            'ES 10'             : self.noAction,
        }

if __name__ == '__main__':

    rules = Rules()
    print "SPS on"
    rules.switchOn('SPS')
    sleep(1)

    print "SPS off"
    rules.switchOff('SPS')
    sleep(.25)

    print "Fan on"
    rules.switchOn('Cabin Fan')
    sleep(1)

    print "Fan off"
    rules.switchOff('Cabin Fan')
    sleep(.25)

    print "O2 Fan on"
    rules.switchOn('O2 Fan')
    sleep(1)

    print "O2 Fan off"
    rules.switchOff('O2 Fan')
    sleep(.25)

    print "H2 Fan on"
    rules.switchOn('H2 Fan')
    sleep(1)

    print "H2 Fan off"
    rules.switchOff('H2 Fan')

    sleep(.5)

    print "PTT In"
    rules.switchOn('PTT')
    sleep(.5)

    print "PTT Out"
    rules.switchOff('PTT')
    sleep(.5)

    print "PTT Out"
    rules.switchOff('PTT')
    sleep(.5)

    print "undefined switch on"
    rules.switchOn('undefined')

    print "undefined switch off"
    rules.switchOff('undefined')

    print "undefined pot" 
    rules.setPot( None, 'undefined', None )
