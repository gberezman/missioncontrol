from port import Port
from time import sleep
from rules import Rules
import threading

port = Port(timeout = .5)

pots = [
    'O2 Flow',
    'Speaker',
    'Headset',
    'Voltage',
    'Resistance',
    'Current',
    'Abort Mode',
    'Ant Pitch',
    'Ant Yaw',
    'Tune',
    'Beam'
]

switches = [
    # expander 0:
    'SPS',
    'TEI',
    'TLI',
    'S-IC',
    'S-II',
    'S-iVB',
    'M-I',
    'M-II',
    'M-III',
    'Power',
    'Mode',
    'Lamp',
    'Ack',
    'undefined',
    'undefined',
    'undefined',

    # expander 1:
    'Docking Probe',
    'Glycol Pump',
    'SCE Power',
    'Waste Dump',
    'Cabin Fan',
    'H2O Flow',
    'Int Lights',
    'Suit Comp',
    'PTT',
    'Arm Abort',
    'Abort',
    'undefined',
    'undefined',
    'undefined',
    'undefined',
    'undefined',

    # expander 2:
    'O2 Fan',
    'H2 Fan',
    'Pumps',
    'Heat',
    'Main Deploy',
    'CSM/LV Deploy',
    'SM/CM Deploy',
    'Drogue Deploy',
    'Canard Deploy',
    'Apex Cover Jettsn',
    'Les Motor Fire',
    'undefined',
    'undefined',
    'undefined',
    'undefined',
    'undefined',

    # expander 3:
    'ES 1',
    'ES 2',
    'ES 3',
    'ES 4',
    'ES 5',
    'ES 6',
    'ES 7',
    'ES 8',
    'ES 9',
    'ES 10',
    'undefined',
    'undefined',
    'undefined',
    'undefined',
    'undefined',
    'undefined'
]

def readingIsPot(reading):
    return ( reading & 0b01000000 ) != 0

def readingIsPotValue(reading):
    return ( reading & 0b11000000 ) != 0

def isSwitched(switchReading):
    return ( switchReading & 0b10000000 ) != 0

def safe_list_get (aList, idx, default):
  try:
    return aList[idx]
  except IndexError:
    return default

def eventLoop():

    print "Starting event loop"

    rules = Rules()

    while True:
        try:
            command = port.readline()
            if command is None:
                sleep( .01 )
                continue

            if command.token() == "P":
                if command.next():
                    pot = safe_list_get(pots, command.tokenAsInt(), None)
                    if pot != None and command.next():
                        try:
                            value = command.tokenAsInt()
                            print "pot {} = {}".format(pot, value)
                            rules.setPot(port, pot, value)
                        except ValueError:
                            print "Invalid numeric pot value {}".format(command.token())

            elif command.next():
                switch = safe_list_get(switches, command.tokenAsInt(), None)
                if switch != None and command.next():
                    isSwitchOn = command.tokenAsBoolean()
                    print "switch {} is {}".format(switch, isSwitchOn)
    
                    if( isSwitchOn ):
                        rules.switchOn( switch )
                    else:
                        rules.switchOff( switch )

        except KeyboardInterrupt:
            exit()

mainThread = threading.Thread( target = eventLoop )
mainThread.start()
