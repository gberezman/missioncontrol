#!/usr/bin/env python

def isBitSet(bitNum, value):
    offset = bitNum & 31
    mask = 1 << offset
    return ( value & mask ) != 0

class Board:

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

    def getLedArray(self, indicators):
        result = bytearray([0, 0, 0, 0, 0, 0, 0, 0])
        for indicator in indicators:
            try:
                coord = self.ledIndicators[indicator]
                offset = coord[1] & 31
                bit = 1 << offset
                result[coord[0]] |= bit
            except KeyError: 
                pass
        return result

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

        self.ledIndicators = {
            'Abort Indicator'             : [0, 0],
            'Push To Talk Indicator'      : [0, 1],
            'Drogue Chute Indicator'      : [0, 2],
            'Ulage Indicator'             : [0, 3],
            'Thrust Indicator'            : [0, 4],
            'Main Chute Indicator'        : [0, 5],
            'Hatch Indicator'             : [0, 6],
            'Docking Target Indicator'    : [0, 7],
            'SPS Pressure Indicator'      : [1, 0],
            'AC Bus I Indicator'          : [1, 1],
            'AC Bus 2 Indicator'          : [1, 2],
            'SPS Rough Eco Indicator'     : [1, 3],
            'AC Bus 1 Overload Indicator' : [1, 4],
            'AC Bus 2 Overload Indicator' : [1, 5],
            'SPS Flng Temp HI Indicator'  : [1, 6],
            'Crew Alert Indicator'        : [1, 7],
            'C/W Indicator'               : [2, 0],
            'FC Bus Disconnect Indicator' : [2, 1],
            'Suit Comp Indicator'         : [2, 2],
            'BMAG 1 Temp'                 : [2, 3],
            'BMAG 2 Temp'                 : [2, 4],
            'CO2PPHI'                     : [2, 5],
            'Pitch Gimbal 1'              : [2, 6],
            'Pitch Gimbal 2'              : [2, 7],
            'Yaw Gimbal 1'                : [3, 0],
            'Yaw Gimbal 2'                : [3, 1],
            'HG Antenna Scan Limit'       : [3, 2],
            'Cryo Pressure'               : [3, 3],
            'Glycol Temperature Low'      : [3, 4],
            'CM RCS 1'                    : [3, 5],
            'CM RSC 2'                    : [3, 6],
            'SM RCS A'                    : [3, 7],
            'SM RCS B'                    : [4, 0],
            'SM RCS C'                    : [4, 1],
            'SM RCS D'                    : [4, 2],
            'Uplink Activity'             : [4, 3],
            'Gimbal Lock'                 : [4, 4],
            'SPS Indicator'               : [4, 5],
            'TEI Indicator'               : [4, 6],
            'TLI Indicator'               : [4, 7],
            'S-IC Indicator'              : [5, 0],
            'SEI Indicator'               : [5, 1],
            'S-IVB Indicator'             : [5, 2],
            'M-I Indicator'               : [5, 3],
            'M-II Indicator'              : [5, 4],
            'M-III Indicator'             : [5, 5],
            'Docking Probe Indicator'     : [5, 6],
            'Glycol Pump Indicator'       : [5, 7],
            'SCE Power Indicator'         : [6, 0],
            'Wast Dump Indicator'         : [6, 1],
            'Cabin Fan Indicator'         : [6, 2],
            'H2O Flow Indicator'          : [6, 3],
            'Int Light Indicator'         : [6, 4],
            'Suit Comp Indicator'         : [6, 5],
            'Master Alarm Indicator'      : [6, 6],
            'Lamp Indicator'              : [6, 7],
            'Ack Indicator'               : [7, 0]
        }

        self.scaledIndicators = {
            'Mission Clock Indicator' : 0, 
            'Pitch Indicator'         : 1, 
            'Yaw Indicator'           : 2, 
            'Roll Indicator'          : 3, 
            'IHR Indicator'           : 4, 
            'AHR Indicator'           : 5, 
            'ABR Indicator'           : 6,
            'Voltage Indicator'       : 7,
            'Resistance Indicator'    : 8,
            'Current Indicator'       : 9,
            'O2 Flow Indicator'       : 10,
            'O2 Pressure Indicator'   : 11,
            'H2 Pressure Indicator'   : 12,
            'O2 Quantity Indicator'   : 13,
            'H2 Quantity Indicator'   : 14,
            'Voltage Indicator'       : 15,
            'Resistance Indicator'    : 16,
            'Current Indicator'       : 17,
            'O2 Flow Indicator'       : 18,
            'Signal Indicator'        : 19
        }
