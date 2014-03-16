from audio import Audio
from time import sleep

class Rules:

    def noAction(self, *args):
        pass

    def switchOn(self, switch):
        self.onRule[switch]()

    def switchOff(self, switch):
        self.offRule[switch]()

    def applyPotRule(self, port, pot, potValue):
        self.potRule[pot](port, pot, potValue)

    def sendMeterSetting(self, port, pot, potValue):
        print "sending pot value {}".format( potValue )
        port.write( "Meter " + pot + " " + str(potValue) + "\n" )

    def __init__(self):
        self.audio = Audio()

        self.potRule = {
            'O2 Flow'    : lambda port, pot, potValue: self.sendMeterSetting(port, "O2", potValue),
            'Speaker'    : self.noAction,
            'Headset'    : self.noAction,
            'Voltage'    : self.noAction,
            'Resistance' : self.noAction,
            'Current'    : self.noAction,
            'Abort Mode' : self.noAction,
            'Ant Pitch'  : self.noAction,
            'Ant Yaw'    : self.noAction,
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
            'Docking Probe'     : self.noAction,
            'Glycol Pump'       : self.noAction,
            'SCE Power'         : self.noAction,
            'Waste Dump'        : self.noAction,
            'Cabin Fan'         : lambda : self.audio.fan.play(loops = -1),
            'H2O Flow'          : self.noAction,
            'Int Lights'        : self.noAction,
            'Suit Comp'         : self.noAction,
            'PTT'               : lambda : self.audio.quindarin.play(),
            'Arm Abort'         : self.noAction,
            'Abort'             : self.noAction,
            'O2 Fan'            : lambda : self.audio.o2fan.play(loops = -1),
            'H2 Fan'            : lambda : self.audio.h2fan.play(loops = -1),
            'Pumps'             : self.noAction,
            'Heat'              : self.noAction,
            'Main Deploy'       : self.noAction,
            'CSM/LV Deploy'     : lambda : self.audio.csmDeploy.play(),
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
            'undefined'         : self.noAction
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
            'undefined'         : self.noAction
        }

if __name__ == '__main__':

    rules = Rules()
    print "SPS on"
    rules.applySwitchRule('SPS', True)
    sleep(1)

    print "SPS off"
    rules.applySwitchRule('SPS', False)
    sleep(.25)

    print "Fan on"
    rules.applySwitchRule('Cabin Fan', True)
    sleep(1)

    print "Fan off"
    rules.applySwitchRule('Cabin Fan', False)
    sleep(.25)

    print "O2 Fan on"
    rules.applySwitchRule('O2 Fan', True)
    sleep(1)

    print "O2 Fan off"
    rules.applySwitchRule('O2 Fan', False)
    sleep(.25)

    print "H2 Fan on"
    rules.applySwitchRule('H2 Fan', True)
    sleep(1)

    print "H2 Fan off"
    rules.applySwitchRule('H2 Fan', False)

    sleep(.5)

    print "PTT In"
    rules.applySwitchRule('PTT', True)
    sleep(.5)

    print "PTT Out"
    rules.applySwitchRule('PTT', False)
    sleep(.5)
