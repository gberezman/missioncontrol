#!/usr/bin/env python

def isBitSet(bitNum, value):
    offset = bitNum & 31
    mask = 1 << offset
    return ( value & mask ) != 0

class Readings:

    def isSwitchOn(self, switch, switchSettings):
        try:
            coord = self.switches[switch]
            bitNum = coord[1]
            segment = switchSettings[coord[0]]
            return isBitSet(coord[1], segment)
        except KeyError:
            return None
        except IndexError:
            return None

    def getPotentiometerReading(self, meter, potentiometerSettings):
        try:
            return potentiometerSettings[self.potentiometers[meter]]
        except KeyError:
            return None
        except IndexError:
            return None

    def __init__(self):
        self.switches = { 
            'Arm Abort'         : [0, 0],
            'Abort'             : [0, 1], 
            'Push to Talk'      : [0, 2], 
            'SPS'               : [0, 3],
            'TEI'               : [0, 4],
            'TLI'               : [0, 5], 
            'S-IC'              : [0, 6], 
            'SEI'               : [0, 7],
            'S-IVB'             : [1, 0],
            'M-I'               : [1, 1], 
            'M-II'              : [1, 2],
            'M-III'             : [1, 3],
            'Docking Probe'     : [1, 4], 
            'Glycol Pump'       : [1, 5], 
            'SCE Power'         : [1, 6], 
            'Wast Dump'         : [1, 7],
            'Cabin Fan'         : [2, 0], 
            'H2O Flow'          : [2, 1], 
            'Int Light'         : [2, 2], 
            'Suit Comp'         : [2, 3], 
            'Lamp'              : [2, 4], 
            'Ack'               : [2, 5], 
            'Power'             : [2, 6], 
            'Mode'              : [2, 7],
            'ES1'               : [3, 0], 
            'ES2'               : [3, 1], 
            'ES3'               : [3, 2], 
            'ES4'               : [3, 3], 
            'ES5'               : [3, 4], 
            'ES6'               : [3, 5], 
            'ES7'               : [3, 6],
            'ES8'               : [3, 7], 
            'O2 Fan'            : [4, 0], 
            'H2 Fan'            : [4, 1], 
            'Pump'              : [4, 2], 
            'Heat'              : [4, 3], 
            'Main Deploy'       : [4, 4], 
            'Drogue Deploy'     : [4, 5],
            'Canard Deploy'     : [4, 6], 
            'CSM/LV Sep'        : [4, 7], 
            'Apex Cover Jettsn' : [5, 0], 
            'SM/CM Sep'         : [5, 1], 
            'Les Motor Fire'    : [5, 2], 
        }
        
        self.potentiometers = {
            'Voltage'    : 0,
            'Resistance' : 1,
            'Current'    : 2,
            'O2 Flow'    : 3,
            'Speaker'    : 4,
            'Abort Mode' : 5,
            'Headset'    : 6,
            'Tune'       : 7,
            'Beam'       : 8,
            'Ant Pitch'  : 9,
            'Ant Yaw'    : 10
        }
