from port import Port
from time import sleep
from rules import Rules
import threading

port = Port()

pots = {
    0  : 'O2 Flow',
    1  : 'Speaker',
    2  : 'Headset',
    3  : 'Voltage',
    4  : 'Resistance',
    5  : 'Current',
    6  : 'Abort Mode',
    7  : 'Ant Pitch',
    8  : 'Ant Yaw',
    9  : 'Tune',
    10 : 'Beam'
}

switches = {
    0  : 'SPS',
    1  : 'TEI',
    2  : 'TLI',
    3  : 'S-IC',
    4  : 'S-II',
    5  : 'S-iVB',
    6  : 'M-I',
    7  : 'M-II',
    8  : 'M-III',
    9  : 'Power',
    10 : 'Mode',
    11 : 'Lamp',
    12 : 'Ack',
    13 : 'undefined',
    14 : 'undefined',
    15 : 'undefined',
    16 : 'Docking Probe',
    17 : 'Glycol Pump',
    18 : 'SCE Power',
    19 : 'Waste Dump',
    20 : 'Cabin Fan',
    21 : 'H2O Flow',
    22 : 'Int Lights',
    23 : 'Suit Comp',
    24 : 'PTT',
    25 : 'Arm Abort',
    26 : 'Abort',
    27 : 'undefined',
    28 : 'undefined',
    29 : 'undefined',
    30 : 'undefined',
    31 : 'undefined',
    32 : 'O2 Fan',
    33 : 'H2 Fan',
    34 : 'Pumps',
    35 : 'Heat',
    36 : 'Main Deploy',
    37 : 'CSM/LV Deploy',
    38 : 'SM/CM Deploy',
    39 : 'Drogue Deploy',
    40 : 'Canard Deploy',
    41 : 'Apex Cover Jettsn',
    42 : 'Les Motor Fire',
    43 : 'undefined',
    44 : 'undefined',
    45 : 'undefined',
    46 : 'undefined',
    47 : 'undefined',
    48 : 'ES 1',
    49 : 'ES 2',
    50 : 'ES 3',
    51 : 'ES 4',
    52 : 'ES 5',
    53 : 'ES 6',
    54 : 'ES 7',
    55 : 'ES 8',
    56 : 'ES 9',
    57 : 'ES 10',
    58 : 'undefined',
    59 : 'undefined',
    60 : 'undefined',
    61 : 'undefined',
    62 : 'undefined',
    63 : 'undefined'
}

def readingIsPot(reading):
    return ( reading & 0b01000000 ) != 0

def readingIsPotValue(reading):
    return ( reading & 0b11000000 ) != 0

def isSwitched(switchReading):
    return ( switchReading & 0b10000000 ) != 0

def eventLoop():

    print "Starting event loop"

    rules = Rules()

    while True:
        try:
            sleep( .01 )
            input = port.nonBlockingRead()
            if len(input) == 0:
                continue

            reading = ord( input )

            if readingIsPot( reading ):
                pot = pots[reading & 0b00111111]
                input = port.nonBlockingRead()
                if len(input) != 0:
                    reading = ord( input )
                    if readingIsPotValue( reading ):
                        potValue = reading & 0b00111111
    
                        print "pot {} = {}".format(pot, potValue)
    
                        rules.applyPotRule(port, pot, potValue)

            else:
                isSwitchOn = isSwitched( reading )
                switch = switches[ reading & 127 ]
    
                print "switch {} is {}".format(switch, isSwitchOn)
    
                if( isSwitchOn ):
                    rules.switchOn( switch )
                else:
                    rules.switchOff( switch )

        except KeyboardInterrupt:
            exit()

mainThread = threading.Thread( target = eventLoop )
mainThread.start()
