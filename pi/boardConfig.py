class BoardConfig:

    def __init__(self):
        self.switches = { 
            'Arm Abort'         : [0, 0],
            'Abort'             : [0, 1], 
            'Push To Talk'      : [0, 2], 
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
            'Abort'             : [0, 0],
            'Push To Talk'      : [0, 1],
            'Drogue Chute'      : [0, 2],
            'Ulage'             : [0, 3],
            'Thrust'            : [0, 4],
            'Main Chute'        : [0, 5],
            'Hatch'             : [0, 6],
            'Docking Target'    : [0, 7],
            'SPS Pressure'      : [1, 0],
            'AC Bus I'          : [1, 1],
            'AC Bus 2'          : [1, 2],
            'SPS Rough Eco'     : [1, 3],
            'AC Bus 1 Overload' : [1, 4],
            'AC Bus 2 Overload' : [1, 5],
            'SPS Flng Temp HI'  : [1, 6],
            'Crew Alert'        : [1, 7],
            'C/W'               : [2, 0],
            'FC Bus Disconnect' : [2, 1],
            'Suit Comp'         : [2, 2],
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
            'Docking Probe'     : [4, 5],
            'Glycol Pump'       : [4, 6],
            'SCE Power'         : [4, 7],
            'Wast Dump'         : [5, 0],
            'Cabin Fan'         : [5, 1],
            'H2O Flow'          : [5, 2],
            'Int Light'         : [5, 3],
            'Suit Comp'         : [5, 4],
            'Master Alarm'      : [5, 5],
            'Lamp'              : [5, 6],
            'Ack'               : [5, 7]
        }

        self.scaledIndicators = {
            'Mission Clock' : 0, 
            'Pitch'         : 1, 
            'Yaw'           : 2, 
            'Roll'          : 3, 
            'IHR'           : 4, 
            'AHR'           : 5, 
            'ABR'           : 6,
            'Voltage'       : 7,
            'Resistance'    : 8,
            'Current'       : 9,
            'O2 Flow'       : 10,
            'O2 Pressure'   : 11,
            'H2 Pressure'   : 12,
            'O2 Quantity'   : 13,
            'H2 Quantity'   : 14,
            'Voltage'       : 15,
            'Resistance'    : 16,
            'Current'       : 17,
            'O2 Flow'       : 18,
            'Signal'        : 19
        }
