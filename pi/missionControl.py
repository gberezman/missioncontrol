from port import Port
from audio import Audio

port = Port()
audio = Audio()

def isSwitched(reading):
    return reading < 128

switches = {
    0  : 'SPS'
    1  : 'TEI'
    2  : 'TLI'
    3  : 'S-IC'
    4  : 'S-II'
    5  : 'S-iVB'
    6  : 'M-I'
    7  : 'M-II'
    8  : 'M-III'
    9  : 'Power'
    10 : 'Mode'
    11 : 'Lamp'
    12 : 'Ack'
    16 : 'Docking Probe'
    17 : 'Glycol Pump'
    18 : 'SCE Power'
    19 : 'Waste Dump'
    20 : 'Cabin Fan'
    21 : 'H2O Flow'
    22 : 'Int Lights'
    23 : 'Suit Comp'
    24 : 'PTT'
    25 : 'Arm Abort'
    26 : 'Abort'
    32 :  'O2 Fan'
    33 :  'H2 Fan'
    34 :  'Pumps'
    35 :  'Heat'
    36 :  'Main Deploy'
    37 :  'CSM/LV Deploy'
    38 :  'SM/CM Deploy'
    39 :  'Drogue Deploy'
    40 :  'Canard Deploy'
    41 :  'Apex Cover Jettsn'
    42 :  'Les Motor Fire'
    48 :  'ES 1'
    49 :  'ES 2'
    50 :  'ES 3'
    51 :  'ES 4'
    52 :  'ES 5'
    53 :  'ES 6'
    54 :  'ES 7'
    55 :  'ES 8'
    56 :  'ES 9'
    57 :  'ES 10'
}

def eventLoop():

    SPSDown = False
 
    while True:
        try:
            sleep( .01 )
            switchReading = ord( port.nonBlockingRead() )
            if( switchReading is None ):
                continue

            isSwitchOn = isSwitched( switchReading )
            switch = switches[ switchReading & 127 ]

            if switch == 'SPS':
                if isSwitchOn:
                    audio.thruster.play(loops = -1)
                else:
                    audio.thruster.stop()

        except KeyboardInterrupt:
            exit()
